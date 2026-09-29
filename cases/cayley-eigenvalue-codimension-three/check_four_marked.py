#!/usr/bin/env python3
"""Validate the public exact certificates for the four-marked cone."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).with_name("evidence") / "four_marked"


def main():
    b1 = json.loads((ROOT / "b1_content.json").read_text(encoding="utf-8"))
    b2 = json.loads((ROOT / "b2_models.json").read_text(encoding="utf-8"))

    small_bad = [
        item
        for rows in b1["small_orders_bad_nonstandard"].values()
        for item in rows
    ]
    b1_pass = (
        b1["status"] == "EXACT_SMALL_TAIL_AUDIT"
        and not b1["generic_bad_nonstandard"]
        and not small_bad
        and all(int(value) > 0 for value in b1["coarse_negative_shift_m4_coefficients"])
    )
    b2_pass = (
        b2["status"] == "EXACT_RATIONAL_FORMULA_CHECK"
        and len(b2["audits"]) == 10
        and all(row["formula_check"] for row in b2["audits"])
    )
    result = {
        "status": "PASS" if b1_pass and b2_pass else "FAIL",
        "B1": {
            "stable_patterns": len(b1["generic_m_at_least_4"]),
            "generic_bad": len(b1["generic_bad_nonstandard"]),
            "small_order_bad": len(small_bad),
            "pass": b1_pass,
        },
        "B2": {
            "exact_model_audits": len(b2["audits"]),
            "orders": sorted({row["n"] for row in b2["audits"]}),
            "pass": b2_pass,
        },
    }
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
