#!/usr/bin/env python3
"""Exact verifier for a distinct-shape Hadamard determinant counterexample.

The target coefficient is evaluated in two independent ways:

1. a column-by-column dynamic program for 0-1 incidence matrices;
2. a closed multinomial sum.

No floating point arithmetic and no randomness are used.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, Sequence, Tuple

N = 3
LEFT_LAMBDA = (18, 18, 15)
LEFT_MU = (2, 0, 0)
RIGHT_LAMBDA = (20, 18, 18)
RIGHT_MU = (2, 2, 0)
LEFT_EXPONENT_COUNTS = (49, 0, 0)   # (# exponent-1, # exponent-2, # exponent-3 variables)
RIGHT_EXPONENT_COUNTS = (20, 16, 0)
EXPECTED_LEFT_PROFILE = (3472519098347437335120, 2741462446063766317200, 2924226609134684071680, 1029816646405790443200, 2193169956851013053760, 978325814085500921040)
EXPECTED_RIGHT_PROFILE = (3051252895132450, 2388914981277920, 2388914981277920, 1719046929283200, 902433439091120, 829443998405960)
EXPECTED_COEFFICIENT = -1288935568443079606185991333432800

Partition = Tuple[int, ...]
DegreeTriple = Tuple[int, int, int]
Shape = Tuple[Partition, Partition]
PERMUTATIONS = tuple(itertools.permutations(range(N)))


def permutation_sign(perm: Sequence[int]) -> int:
    inversions = sum(
        1
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
        if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1


SIGNS = tuple(permutation_sign(perm) for perm in PERMUTATIONS)


def is_partition(parts: Sequence[int]) -> bool:
    return all(parts[i] >= parts[i + 1] >= 0 for i in range(len(parts) - 1)) and parts[-1] >= 0


def shape_size(shape: Shape) -> int:
    lam, mu = shape
    return sum(lam[i] - mu[i] for i in range(N))


def cells_of(shape: Shape) -> set[Tuple[int, int]]:
    lam, mu = shape
    return {
        (row, col)
        for row in range(N)
        for col in range(mu[row], lam[row])
    }


def has_three_by_two_block(shape: Shape) -> bool:
    cells = cells_of(shape)
    if not cells:
        return False
    max_col = max(col for _, col in cells)
    return any(
        all((row, col + delta) in cells for row in range(N) for delta in (0, 1))
        for col in range(max_col)
    )


def has_no_empty_internal_column(shape: Shape) -> bool:
    cells = cells_of(shape)
    if not cells:
        return False
    columns = {col for _, col in cells}
    return min(columns) == 0 and columns == set(range(max(columns) + 1))


def validate_shape(shape: Shape) -> Dict[str, object]:
    lam, mu = shape
    checks = {
        "lambda_is_partition": is_partition(lam),
        "mu_is_partition": is_partition(mu),
        "mu_is_contained": all(0 <= mu[i] <= lam[i] for i in range(N)),
        "three_nonempty_rows": all(mu[i] < lam[i] for i in range(N)),
        "leftmost_column_zero_and_no_internal_empty_column": has_no_empty_internal_column(shape),
        "contains_3x2_block": has_three_by_two_block(shape),
    }
    if not all(checks.values()):
        raise AssertionError(f"invalid shape or failed premise: {shape!r}; checks={checks!r}")
    return checks


def degree_matrix(shape: Shape) -> Tuple[DegreeTriple, DegreeTriple, DegreeTriple]:
    lam, mu = shape
    return tuple(
        tuple(lam[i] - mu[j] - i + j for j in range(N))
        for i in range(N)
    )  # type: ignore[return-value]


def target_degrees(
    matrix: Tuple[DegreeTriple, DegreeTriple, DegreeTriple],
    perm: Sequence[int],
) -> DegreeTriple:
    return tuple(matrix[i][perm[i]] for i in range(N))  # type: ignore[return-value]


def coefficient_table_dp(p: int, q: int, r: int) -> Dict[DegreeTriple, int]:
    """Method A: multiply the column choices one target variable at a time.

    An exponent-1 target variable occurs in exactly one of the three selected
    elementary factors; an exponent-2 variable occurs in exactly two; an
    exponent-3 variable occurs in all three.
    """
    dp: Dict[DegreeTriple, int] = {(0, 0, 0): 1}
    for _ in range(p):
        nxt: Dict[DegreeTriple, int] = defaultdict(int)
        for (a, b, c), value in dp.items():
            nxt[(a + 1, b, c)] += value
            nxt[(a, b + 1, c)] += value
            nxt[(a, b, c + 1)] += value
        dp = dict(nxt)
    for _ in range(q):
        nxt = defaultdict(int)
        for (a, b, c), value in dp.items():
            nxt[(a + 1, b + 1, c)] += value
            nxt[(a + 1, b, c + 1)] += value
            nxt[(a, b + 1, c + 1)] += value
        dp = dict(nxt)
    if r:
        dp = {(a + r, b + r, c + r): value for (a, b, c), value in dp.items()}
    return dp


def multinomial3(n: int, a: int, b: int, c: int) -> int:
    if min(a, b, c) < 0 or a + b + c != n:
        return 0
    return math.factorial(n) // (
        math.factorial(a) * math.factorial(b) * math.factorial(c)
    )


def coefficient_multinomial(p: int, q: int, r: int, degrees: DegreeTriple) -> int:
    """Method B: closed sum over assignments of exponent-1 variables.

    If k_i exponent-1 variables are assigned to row i, then the number l_i of
    exponent-2 variables omitted from row i is forced by
        degrees_i = k_i + (q-l_i) + r.
    """
    total = 0
    d0, d1, d2 = degrees
    for k0 in range(p + 1):
        for k1 in range(p - k0 + 1):
            k2 = p - k0 - k1
            l0 = k0 + q + r - d0
            l1 = k1 + q + r - d1
            l2 = k2 + q + r - d2
            if min(l0, l1, l2) < 0 or l0 + l1 + l2 != q:
                continue
            total += multinomial3(p, k0, k1, k2) * multinomial3(q, l0, l1, l2)
    return total


def profile_dp(
    matrix: Tuple[DegreeTriple, DegreeTriple, DegreeTriple],
    counts: Tuple[int, int, int],
) -> Tuple[int, ...]:
    table = coefficient_table_dp(*counts)
    return tuple(table.get(target_degrees(matrix, perm), 0) for perm in PERMUTATIONS)


def profile_multinomial(
    matrix: Tuple[DegreeTriple, DegreeTriple, DegreeTriple],
    counts: Tuple[int, int, int],
) -> Tuple[int, ...]:
    return tuple(
        coefficient_multinomial(*counts, target_degrees(matrix, perm))
        for perm in PERMUTATIONS
    )


def monomial_label(prefix: str, counts: Tuple[int, int, int]) -> str:
    p, q, r = counts
    pieces = []
    start = 1
    for power, amount in ((1, p), (2, q), (3, r)):
        if amount == 0:
            continue
        end = start + amount - 1
        if amount == 1:
            block = f"{prefix}_{start}"
        else:
            block = f"{prefix}_{start},...,{prefix}_{end}"
        pieces.append(f"variables {block} have exponent {power}")
        start = end + 1
    return "; ".join(pieces)


def canonical_sha256(data: object) -> str:
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def run() -> Dict[str, object]:
    left_shape: Shape = (LEFT_LAMBDA, LEFT_MU)
    right_shape: Shape = (RIGHT_LAMBDA, RIGHT_MU)
    left_checks = validate_shape(left_shape)
    right_checks = validate_shape(right_shape)

    left_matrix = degree_matrix(left_shape)
    right_matrix = degree_matrix(right_shape)

    if shape_size(left_shape) != sum((i + 1) * n for i, n in enumerate(LEFT_EXPONENT_COUNTS)):
        raise AssertionError("left target monomial has wrong total degree")
    if shape_size(right_shape) != sum((i + 1) * n for i, n in enumerate(RIGHT_EXPONENT_COUNTS)):
        raise AssertionError("right target monomial has wrong total degree")

    left_dp = profile_dp(left_matrix, LEFT_EXPONENT_COUNTS)
    left_closed = profile_multinomial(left_matrix, LEFT_EXPONENT_COUNTS)
    right_dp = profile_dp(right_matrix, RIGHT_EXPONENT_COUNTS)
    right_closed = profile_multinomial(right_matrix, RIGHT_EXPONENT_COUNTS)

    if left_dp != left_closed or right_dp != right_closed:
        raise AssertionError("the two independent coefficient methods disagree")
    if left_dp != EXPECTED_LEFT_PROFILE:
        raise AssertionError("left profile differs from frozen expected values")
    if right_dp != EXPECTED_RIGHT_PROFILE:
        raise AssertionError("right profile differs from frozen expected values")

    summands = tuple(
        SIGNS[index] * left_dp[index] * right_dp[index]
        for index in range(len(PERMUTATIONS))
    )
    coefficient = sum(summands)
    if coefficient != EXPECTED_COEFFICIENT:
        raise AssertionError("signed determinant coefficient differs from frozen value")
    if coefficient >= 0:
        raise AssertionError("candidate is not a negative coefficient")

    script_path = Path(__file__).resolve()
    result: Dict[str, object] = {
        "status": "DISPROVED",
        "source": "arXiv:2511.08969v1, Conjecture 1.2",
        "unit": "determinant Temperley-Lieb immanant, k=2, matrix size n=3",
        "scope_note": (
            "The two skew shapes differ; "
            "the same-shape conjecture is not settled by this witness."
        ),
        "left": {
            "lambda": LEFT_LAMBDA,
            "mu": LEFT_MU,
            "size": shape_size(left_shape),
            "checks": left_checks,
            "dual_jacobi_trudi_degrees": left_matrix,
            "variable_count": sum(LEFT_EXPONENT_COUNTS),
            "target_exponent_counts_1_2_3": LEFT_EXPONENT_COUNTS,
            "target_monomial": monomial_label("x", LEFT_EXPONENT_COUNTS),
            "permutation_profile": left_dp,
        },
        "right": {
            "lambda": RIGHT_LAMBDA,
            "mu": RIGHT_MU,
            "size": shape_size(right_shape),
            "checks": right_checks,
            "dual_jacobi_trudi_degrees": right_matrix,
            "variable_count": sum(RIGHT_EXPONENT_COUNTS),
            "target_exponent_counts_1_2_3": RIGHT_EXPONENT_COUNTS,
            "target_monomial": monomial_label("y", RIGHT_EXPONENT_COUNTS),
            "permutation_profile": right_dp,
        },
        "permutation_order": PERMUTATIONS,
        "permutation_signs": SIGNS,
        "signed_summands": summands,
        "negative_coefficient": coefficient,
        "two_independent_methods_agree": True,
        "arithmetic": "exact Python integers only",
        "randomness": "none",
        "script_sha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
    }
    result["certificate_sha256"] = canonical_sha256(result)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args(argv)

    result = run()
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
