"""Verify the 2C4 sharpness certificate for the delta(G)=2 slice."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SUMMARY = ROOT / "sharpness_summary.json"

EDGES = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
)


def profile(mask: int) -> tuple[int, int, int]:
    degrees = [0] * 8
    for index, (u, v) in enumerate(EDGES):
        if mask & (1 << index):
            degrees[u] += 1
            degrees[v] += 1
    counts = Counter(degrees)
    return (counts[0], counts[1], counts[2])


def main() -> None:
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))

    if [list(edge) for edge in EDGES] != summary["edges"]:
        raise SystemExit("edge list in summary does not match checker")

    profiles = [profile(mask) for mask in range(1 << len(EDGES))]
    max_counts = [max(item) for item in profiles]
    distribution = Counter(str(value) for value in max_counts)
    optimum = min(max_counts)
    optimal_profiles = Counter(item for item in profiles if max(item) == optimum)

    expected_optimal_profiles = {
        key: value for key, value in summary["optimal_profile_counts"].items()
    }
    actual_optimal_profiles = {
        f"({item[0]},{item[1]},{item[2]})": count
        for item, count in sorted(optimal_profiles.items())
    }

    checks = {
        "total_spanning_subgraphs": len(profiles),
        "minimum_possible_max_degree_multiplicity": optimum,
        "theorem_bound": 8 // 3 + 2,
        "distribution_by_max_degree_multiplicity": dict(sorted(distribution.items())),
        "optimal_profile_counts": actual_optimal_profiles,
    }

    for key, actual in checks.items():
        expected = summary[key]
        if actual != expected:
            raise SystemExit(f"{key} mismatch: expected {expected!r}, got {actual!r}")

    if optimum != 4:
        raise SystemExit("2C4 does not certify sharpness")

    print("PASS: 2C4 sharpness certificate verified")


if __name__ == "__main__":
    main()
