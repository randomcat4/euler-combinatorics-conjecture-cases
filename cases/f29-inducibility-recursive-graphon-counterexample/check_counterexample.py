#!/usr/bin/env python3
"""Verify the F29 inducibility recursive-graphon counterexample."""

from __future__ import annotations

import argparse
import json
import math
from functools import lru_cache
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
N = 6
PAIR_ORDER: tuple[tuple[int, int], ...] = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 3),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5),
    (4, 5),
)
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIR_ORDER)}
TARGET_VALUE = Fraction(24, 1555)
DIAG_STATES = "01R"
R_STATE = 2


def parse_edge(edge: str) -> tuple[int, int]:
    if len(edge) != 2 or not edge.isdigit():
        raise ValueError(f"bad edge label: {edge!r}")
    a, b = int(edge[0]), int(edge[1])
    if not (0 <= a < b < N):
        raise ValueError(f"bad edge endpoints: {edge!r}")
    return a, b


def bit(mask: int, a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    return (mask >> PAIR_INDEX[(a, b)]) & 1


def mask_from_edges(edges: list[str]) -> int:
    mask = 0
    for edge in edges:
        mask |= 1 << PAIR_INDEX[parse_edge(edge)]
    return mask


def diag_trits(diag_code: int) -> tuple[int, ...]:
    trits: list[int] = []
    for _ in range(N):
        trits.append(diag_code % 3)
        diag_code //= 3
    if diag_code:
        raise ValueError("diagonal code is out of range")
    return tuple(trits)


def diag_string(diag_code: int) -> str:
    return "".join(DIAG_STATES[state] for state in diag_trits(diag_code))


def pattern_code(off_mask: int, diag_code: int) -> str:
    return f"off={off_mask:015b};diag={diag_string(diag_code)}"


def automorphism_count(target_mask: int) -> int:
    count = 0
    for perm in permutations(range(N)):
        if all(bit(target_mask, a, b) == bit(target_mask, perm[a], perm[b]) for a, b in PAIR_ORDER):
            count += 1
    return count


def induced_edge(target_mask: int, vertices: tuple[int, ...], local_a: int, local_b: int) -> int:
    return bit(target_mask, vertices[local_a], vertices[local_b])


def labelled_density_for_subset(subset_mask: int, target_mask: int, off_mask: int, diag_code: int) -> Fraction:
    """Return t(F[subset], W) for one recursive graphon pattern."""

    diag = diag_trits(diag_code)

    @lru_cache(maxsize=None)
    def solve(mask: int) -> Fraction:
        vertices = tuple(index for index in range(N) if (mask >> index) & 1)
        size = len(vertices)
        if size <= 1:
            return Fraction(1)

        constant = Fraction(0)
        recursive_coeff = 0

        for assignment in product(range(N), repeat=size):
            buckets: list[list[int]] = [[] for _ in range(N)]
            for local_vertex, part in enumerate(assignment):
                buckets[part].append(local_vertex)

            ok = True
            for a in range(size):
                for b in range(a + 1, size):
                    part_a, part_b = assignment[a], assignment[b]
                    if part_a == part_b:
                        continue
                    if induced_edge(target_mask, vertices, a, b) != bit(off_mask, part_a, part_b):
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue

            term = Fraction(1)
            self_factor = False
            for part, bucket in enumerate(buckets):
                if len(bucket) <= 1:
                    continue
                state = diag[part]
                local_pairs = [(x, y) for index, x in enumerate(bucket) for y in bucket[index + 1 :]]
                if state in (0, 1):
                    if any(induced_edge(target_mask, vertices, x, y) != state for x, y in local_pairs):
                        term = Fraction(0)
                        break
                    continue

                child_mask = 0
                for local_vertex in bucket:
                    child_mask |= 1 << vertices[local_vertex]
                if child_mask == mask:
                    self_factor = True
                else:
                    term *= solve(child_mask)

            if term == 0:
                continue
            if self_factor:
                recursive_coeff += 1
            else:
                constant += term

        denominator = N**size - recursive_coeff
        if denominator <= 0:
            raise AssertionError(f"non-positive recursive denominator for subset {mask}")
        return constant / denominator

    return solve(subset_mask)


def induced_density(target_mask: int, off_mask: int, diag_code: int, aut_count: int) -> Fraction:
    labelled = labelled_density_for_subset((1 << N) - 1, target_mask, off_mask, diag_code)
    return labelled * Fraction(math.factorial(N), aut_count)


def verify_pattern(
    name: str,
    target_mask: int,
    pattern: dict[str, Any],
    aut_count: int,
) -> dict[str, Any]:
    off_mask = int(pattern["off_mask"])
    diag_code = int(pattern["diag_code"])
    if pattern_code(off_mask, diag_code) != pattern["code"]:
        raise AssertionError(f"{name}: pattern code mismatch")
    if mask_from_edges(list(pattern["off_edges"])) != off_mask:
        raise AssertionError(f"{name}: off-edge list disagrees with off_mask")
    if "".join(pattern["diag"]) != diag_string(diag_code):
        raise AssertionError(f"{name}: diagonal list disagrees with diag_code")

    labelled = labelled_density_for_subset((1 << N) - 1, target_mask, off_mask, diag_code)
    induced = induced_density(target_mask, off_mask, diag_code, aut_count)
    expected_labelled = Fraction(pattern["labelled_density_t"])
    expected_induced = Fraction(pattern["induced_density_p"])
    expected_difference = Fraction(pattern["target_difference"])

    if labelled != expected_labelled:
        raise AssertionError(f"{name}: labelled density {labelled} != {expected_labelled}")
    if induced != expected_induced:
        raise AssertionError(f"{name}: induced density {induced} != {expected_induced}")
    if induced - TARGET_VALUE != expected_difference:
        raise AssertionError(f"{name}: target difference mismatch")
    if induced <= TARGET_VALUE:
        raise AssertionError(f"{name}: pattern does not improve the target value")

    return {
        "name": name,
        "code": pattern["code"],
        "labelled_density_t": str(labelled),
        "induced_density_p": str(induced),
        "target_difference": str(induced - TARGET_VALUE),
        "strictly_improves_target": True,
    }


def verify(certificate: dict[str, Any]) -> dict[str, Any]:
    target = certificate["target_graph"]
    vertices = list(target["vertices"])
    if vertices != list(range(N)):
        raise AssertionError("target vertices must be [0,1,2,3,4,5]")

    pair_order = ["".join(map(str, pair)) for pair in PAIR_ORDER]
    if certificate["pair_order"] != pair_order:
        raise AssertionError("pair order mismatch")

    target_mask = mask_from_edges(list(target["edges"]))
    aut_count = automorphism_count(target_mask)
    expected = certificate["expected"]
    if aut_count != expected["automorphism_count"]:
        raise AssertionError("automorphism count mismatch")

    checks = [
        verify_pattern("witness", target_mask, certificate["witness"], aut_count),
        verify_pattern(
            "additional_strict_witness",
            target_mask,
            certificate["additional_strict_witness"],
            aut_count,
        ),
    ]

    summary = {
        "ok": True,
        "case": certificate["case"],
        "result": certificate["result"],
        "source_arxiv": certificate["source"]["arxiv"],
        "source_target": certificate["source"]["target"],
        "target_graph": target["name"],
        "target_edges": target["edges"],
        "automorphism_count": aut_count,
        "normalization_factor": str(math.factorial(N) // aut_count),
        "target_value": str(TARGET_VALUE),
        "checks": checks,
        "source_equality_refuted": True,
    }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=ROOT / "counterexample_certificate.json",
        help="path to the JSON counterexample certificate",
    )
    parser.add_argument(
        "--summary-out",
        type=Path,
        help="optional path for the compact verification summary",
    )
    args = parser.parse_args()

    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    summary = verify(certificate)
    text = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    if args.summary_out:
        args.summary_out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
