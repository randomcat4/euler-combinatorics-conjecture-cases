#!/usr/bin/env python3
"""Check the exact finite boundary certificates for the monotone cones."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).with_name("evidence") / "monotone"


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def check_r2():
    rows = load("k4r2n6.json")["nonstandard_gap_rows"]
    bad = []
    central_zero = []
    for row in rows:
        gap = tuple(int(value) for value in row["gap_u_v_w"])
        if gap[1] <= 0 or gap[2] <= 0:
            bad.append({"row": row, "gap": gap})
        if gap[0] == 0:
            central_zero.append(tuple(row["lambda"]))
    return {
        "rows": len(rows),
        "noncentral_gaps_positive": not bad,
        "central_zero_partitions": sorted(set(central_zero)),
        "pass": not bad and set(central_zero) == {(2, 2, 2)},
    }


def least_gap(record):
    if "target_difference" in record:
        return int(record["target_difference"])
    return min(int(value) for value in record["target_differences"])


def check_r3():
    data = load("k4r3n6.json")
    rows = []
    bad = []
    central_zero = []
    for row in data["H_types"]:
        partition = tuple(row["lambda"])
        if row["is_degree"] or partition == (5, 1):
            continue
        rows.append(row)
        gap2 = least_gap(row["rays"]["B2"])
        gap3 = least_gap(row["rays"]["B3"])
        gap0 = least_gap(row["rays"]["K4"])
        if gap2 <= 0 or gap3 <= 0:
            bad.append({"partition": partition, "B2": gap2, "B3": gap3})
        if gap0 == 0:
            central_zero.append(partition)
    return {
        "rows": len(rows),
        "B2_B3_gaps_positive": not bad,
        "central_zero_partitions": sorted(set(central_zero)),
        "pass": not bad and set(central_zero) == {(2, 2, 2)},
    }


def check_b1():
    data = load("k4r3b1.json")
    status = data.get("status")
    return {
        "status": status,
        "pass": status == "PASS",
        "scope": data.get("scope"),
    }


def main():
    result = {"k4r2n6": check_r2(), "k4r3n6": check_r3(), "k4r3b1": check_b1()}
    result["status"] = "PASS" if all(item["pass"] for item in result.values()) else "FAIL"
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
