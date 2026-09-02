#!/usr/bin/env python3
"""Bounded arithmetic checks for the P66 three-leaf Steklov theorem."""

from __future__ import annotations

import argparse
from collections import defaultdict
from decimal import Decimal, getcontext
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
getcontext().prec = 80


def matching_formula(lengths: tuple[int, int, int]) -> int:
    floors = sum(length // 2 for length in lengths)
    return floors + int(any(length % 2 for length in lengths))


def spider_matching_dp(lengths: tuple[int, int, int]) -> int:
    """Compute maximum matching on the explicit spider by tree DP."""

    adjacency: list[list[int]] = [[]]
    for length in lengths:
        previous = 0
        for _ in range(length):
            vertex = len(adjacency)
            adjacency.append([previous])
            adjacency[previous].append(vertex)
            previous = vertex

    def visit(vertex: int, parent: int) -> tuple[int, int]:
        children = [child for child in adjacency[vertex] if child != parent]
        child_values = [visit(child, vertex) for child in children]
        not_matched_to_parent = sum(free for free, _used_to_parent in child_values)
        best = not_matched_to_parent
        for index, (_child_free, child_used_to_parent) in enumerate(child_values):
            candidate = 1 + child_used_to_parent
            for other_index, values in enumerate(child_values):
                if other_index != index:
                    candidate += values[0]
            best = max(best, candidate)
        return best, not_matched_to_parent

    return visit(0, -1)[0]


def parity_class(lengths: tuple[int, int, int]) -> int:
    return sum(length % 2 for length in lengths)


def denominator(lengths: tuple[int, int, int]) -> Decimal:
    a, b, c = lengths
    s = a + b + c
    q = a * b + a * c + b * c
    return Decimal(s) + Decimal(s * s - 3 * q).sqrt()


def target_lengths(r: int) -> tuple[int, int, int]:
    return tuple(sorted((2 * r + 2, 2 * r + 1, 2 * r)))


def feasible_spiders(r: int) -> list[tuple[int, int, int]]:
    out: list[tuple[int, int, int]] = []
    for odd_arms in range(4):
        total = 6 * r + 4 if odd_arms == 0 else 6 * r + 2 + odd_arms
        for a in range(1, total // 3 + 1):
            for b in range(a, (total - a) // 2 + 1):
                c = total - a - b
                lengths = (a, b, c)
                if (
                    parity_class(lengths) == odd_arms
                    and matching_formula(lengths) == 3 * r + 2
                ):
                    out.append(lengths)
    return out


def verify(certificate: dict[str, Any]) -> dict[str, Any]:
    arm_max = certificate["calibration"]["matching_formula_arm_max"]
    r_min, r_max = certificate["calibration"]["r_checked"]

    formula_mismatches = []
    for a in range(1, arm_max + 1):
        for b in range(1, arm_max + 1):
            for c in range(1, arm_max + 1):
                lengths = (a, b, c)
                if matching_formula(lengths) != spider_matching_dp(lengths):
                    formula_mismatches.append(lengths)

    extremizer_failures = []
    class_minima: dict[str, dict[str, list[tuple[int, int, int]]]] = defaultdict(dict)
    checked_spiders = 0
    for r in range(r_min, r_max + 1):
        spiders = feasible_spiders(r)
        checked_spiders += len(spiders)
        scored = [(denominator(lengths), lengths) for lengths in spiders]
        best_value = min(value for value, _lengths in scored)
        best = [lengths for value, lengths in scored if value == best_value]
        expected = target_lengths(r)
        if best != [expected]:
            extremizer_failures.append({"r": r, "best": best, "expected": expected})

        for odd_arms in range(4):
            subset = [
                (value, lengths)
                for value, lengths in scored
                if parity_class(lengths) == odd_arms
            ]
            if subset:
                class_value = min(value for value, _lengths in subset)
                class_best = [
                    lengths for value, lengths in subset if value == class_value
                ]
                class_minima[str(r)][str(odd_arms)] = class_best

    terminal_state = (
        "PASS" if not formula_mismatches and not extremizer_failures else "FAIL"
    )
    expected = certificate["calibration"]
    if checked_spiders != expected["feasible_spiders_checked"]:
        raise AssertionError(
            f"feasible spider count {checked_spiders} != "
            f"{expected['feasible_spiders_checked']}"
        )
    if terminal_state != expected["terminal_state"]:
        raise AssertionError(f"terminal state {terminal_state} != {expected['terminal_state']}")

    samples = {key: class_minima[key] for key in ("1", "2", "10", str(r_max))}
    return {
        "ok": terminal_state == "PASS",
        "case": certificate["case"],
        "result": certificate["result"],
        "source": certificate["source"],
        "public_scope": certificate["public_scope"],
        "matching_formula_arm_max": arm_max,
        "matching_formula_mismatches": formula_mismatches,
        "r_checked": [r_min, r_max],
        "feasible_spiders_checked": checked_spiders,
        "extremizer_failures": extremizer_failures,
        "sample_class_minima": samples,
        "terminal_state": terminal_state,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=ROOT / "spider_certificate.json",
        help="path to the JSON spider certificate",
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
