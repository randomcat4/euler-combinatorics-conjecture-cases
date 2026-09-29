#!/usr/bin/env python3
"""Validate the public exact certificates for the n=5 product-activity ray."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).with_name("evidence") / "product_activity"


def main():
    base = json.loads((ROOT / "n5ray_certificate.json").read_text(encoding="utf-8"))
    ranges = json.loads((ROOT / "n5ray_range.json").read_text(encoding="utf-8"))
    diagnostic = json.loads((ROOT / "reflected_diagnostic.json").read_text(encoding="utf-8"))

    minors = [
        minor
        for block in base["blocks"].values()
        for minor in block["leading_principal_minors"]
    ]
    base_pass = (
        base["status"] == "EXACT_CERTIFICATE"
        and base["standard_trial_vector_identity_exact"]
        and len(minors) == 11
        and all(minor["all_coefficients_positive"] for minor in minors)
    )
    range_pass = ranges["status_by_shift"]["13/5"] is True
    diagnostic_pass = (
        diagnostic["status"] == "FINITE_NO_HIT_NOT_A_PROOF"
        and not diagnostic["violations"]
        and not diagnostic["unexpected_maximizers"]
        and not diagnostic["standard_branch_failures"]
    )
    result = {
        "status": "PASS" if base_pass and range_pass and diagnostic_pass else "FAIL",
        "leading_principal_minors": len(minors),
        "q_shift_13_over_5_certified": range_pass,
        "reflected_parameter_cases": diagnostic["parameter_cases"],
        "reflected_diagnostic_only": True,
    }
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
