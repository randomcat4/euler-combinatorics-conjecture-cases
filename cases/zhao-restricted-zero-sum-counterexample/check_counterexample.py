#!/usr/bin/env python3
"""Exhaustively verify the displayed Zhao Conjecture 6.1 counterexample."""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations


MODULI = (2, 4, 4, 4)
A = (0, 1, 0, 0)
B = (0, 0, 1, 0)
C = (0, 0, 0, 1)
T = (1, 3, 3, 3)


def subtract(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x - y) % modulus for x, y, modulus in zip(left, right, MODULI))


SEQUENCE = (
    (A,) * 3
    + (B,) * 3
    + (C,) * 3
    + (subtract(T, A), subtract(T, B), subtract(T, C))
)


def is_zero_sum(indices: tuple[int, ...]) -> bool:
    return all(
        sum(SEQUENCE[index][coordinate] for index in indices) % modulus == 0
        for coordinate, modulus in enumerate(MODULI)
    )


def main() -> None:
    counts: Counter[int] = Counter()
    checked = 0
    for size in range(1, len(SEQUENCE) + 1):
        for indices in combinations(range(len(SEQUENCE)), size):
            checked += 1
            if is_zero_sum(indices):
                counts[size] += 1

    assert checked == 2 ** len(SEQUENCE) - 1
    assert counts == Counter({10: 9})

    result = {
        "group": "C2 direct-sum C4^3",
        "sequence_length": len(SEQUENCE),
        "nonempty_occurrence_subsets_checked": checked,
        "zero_sum_occurrence_subsets_by_length": {
            str(size): count for size, count in sorted(counts.items())
        },
        "zero_sum_subsets_of_length_at_most_9": sum(
            count for size, count in counts.items() if size <= 9
        ),
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
