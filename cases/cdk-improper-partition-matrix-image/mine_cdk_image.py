"""Finite regression for the CDK image characterization.

This script is deliberately finite: it checks n <= 8 by default and does not
certify the all-order theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class BadTransition:
    position: int
    left_endpoint: int
    local_position: int
    lhs: int
    rhs: int


def inversion_sequences(n: int) -> Iterable[tuple[int, ...]]:
    ranges = [range(i) for i in range(1, n + 1)]
    yield from itertools.product(*ranges)


def alphabet(e: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(set(e)))


def column_left_endpoint(a: tuple[int, ...], i: int) -> int:
    """Return the left endpoint of the CDK column containing label i."""
    left = 0
    for value in a:
        if value < i:
            left = value
        else:
            break
    return left


def cdk_row_col(
    e: tuple[int, ...],
) -> tuple[dict[int, int], dict[int, int], dict[int, int]]:
    a = alphabet(e)
    row_of_value = {value: idx + 1 for idx, value in enumerate(a)}
    row = {label: row_of_value[e[label - 1]] for label in range(1, len(e) + 1)}

    endpoints = list(a[1:]) + [len(e)]
    col: dict[int, int] = {}
    col_min: dict[int, int] = {}
    left = 0
    for idx, right in enumerate(endpoints, start=1):
        for label in range(left + 1, right + 1):
            col[label] = idx
            col_min[label] = left + 1
        left = right
    return row, col, col_min


def cdk_inverse_is_improper(e: tuple[int, ...]) -> bool:
    row, col, col_min = cdk_row_col(e)
    for i in range(1, len(e)):
        if col[i] != col[i + 1]:
            continue
        if row[i] == row[i + 1]:
            continue
        if i % 2 == col_min[i] % 2:
            return False
    return True


def bad_transitions(e: tuple[int, ...]) -> list[BadTransition]:
    """Return bad positions for the intrinsic pair predicate."""
    a = alphabet(e)
    positive_boundaries = set(a[1:])
    out: list[BadTransition] = []
    for i in range(1, len(e)):
        if i in positive_boundaries:
            continue
        left = column_left_endpoint(a, i)
        local_position = i - left
        if local_position % 2 == 1 and e[i - 1] != e[i]:
            out.append(
                BadTransition(
                    position=i,
                    left_endpoint=left,
                    local_position=local_position,
                    lhs=e[i - 1],
                    rhs=e[i],
                )
            )
    return out


def intrinsic_pair_predicate(e: tuple[int, ...]) -> bool:
    return not bad_transitions(e)


def encode_set(sequences: Iterable[tuple[int, ...]]) -> str:
    return "\n".join(",".join(map(str, e)) for e in sorted(sequences)) + "\n"


def summarize(n_max: int) -> dict[str, object]:
    by_n = []
    total_sequences = 0
    total_image = 0
    for n in range(1, n_max + 1):
        sequences = list(inversion_sequences(n))
        total_sequences += len(sequences)
        image = [e for e in sequences if cdk_inverse_is_improper(e)]
        predicate = [e for e in sequences if intrinsic_pair_predicate(e)]
        image_set = set(image)
        predicate_set = set(predicate)
        only_image = sorted(image_set - predicate_set)
        only_predicate = sorted(predicate_set - image_set)
        total_image += len(image)
        first_bad_examples = []
        for e in sequences:
            bad = bad_transitions(e)
            if bad:
                first_bad_examples.append(
                    {
                        "e": list(e),
                        "bad": [bt.__dict__ for bt in bad[:3]],
                    }
                )
            if len(first_bad_examples) == 5:
                break
        by_n.append(
            {
                "n": n,
                "all_inversion_sequences": len(sequences),
                "cdk_ippm_image_count": len(image),
                "intrinsic_predicate_count": len(predicate),
                "symmetric_difference_count": len(only_image) + len(only_predicate),
                "only_cdk_image": [list(e) for e in only_image[:5]],
                "only_intrinsic_predicate": [list(e) for e in only_predicate[:5]],
                "image_sha256": hashlib.sha256(
                    encode_set(image).encode("utf-8")
                ).hexdigest(),
                "predicate_sha256": hashlib.sha256(
                    encode_set(predicate).encode("utf-8")
                ).hexdigest(),
                "first_bad_transition_examples": first_bad_examples,
            }
        )
    return {
        "scope": "finite regression only; n <= %d; not an all-order proof"
        % n_max,
        "candidate_predicate": (
            "For e in I_n, let A=sorted(set(e)). Treat the intervals "
            "(a_r,a_{r+1}] with a_{D+1}=n as intrinsic value blocks. "
            "For each adjacent label pair i,i+1 lying inside one block, "
            "if i-a_r is odd then require e_i=e_{i+1}."
        ),
        "total_inversion_sequences_checked": total_sequences,
        "total_cdk_ippm_image": total_image,
        "results": by_n,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, default=8)
    parser.add_argument("--write", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()

    data = summarize(args.n_max)
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if data != expected:
            raise SystemExit("generated summary does not match stored certificate")
        print("CHECK PASS")
    if args.write:
        args.write.write_text(
            json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    if not args.check:
        print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
