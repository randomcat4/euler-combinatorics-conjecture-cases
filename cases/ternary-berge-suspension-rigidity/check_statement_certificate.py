"""Check the public release certificate for the ternary-Berge case.

This is a release-boundary check, not a proof assistant. The mathematical
content is in proof.md and was independently reviewed before public curation.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

EXPECTED = {
    "case_slug": "ternary-berge-suspension-rigidity",
    "result": "PROVED",
    "result_type": "COMPLETE_SOLUTION",
    "verification_status": "INDEPENDENTLY_VERIFIED",
    "verdict": "CORRECT",
    "novelty": "NOT_ESTABLISHED",
    "priority": "NOT_ESTABLISHED",
    "arxiv": "2408.14321v2",
    "doi": "10.1007/s00493-026-00198-y",
}

FORBIDDEN_PUBLIC_MARKERS = (
    re.compile(r"01a0[0-9a-f-]+"),
    re.compile(r"pull/\d+"),
    re.compile(r"issuecomment-"),
    re.compile(r"DRAFT_NEEDS_"),
    re.compile(r"\b[A-Za-z]:\\"),
    re.compile(r"/root/"),
)

REQUIRED_PROOF_MARKERS = (
    "edge-star expansion",
    "Corollary 5.3",
    "no cycle whose length is divisible by three",
    "integral suspension homology",
    "disconnected",
    "S^0",
    "Theorem 1.3",
    "Suspension Rigidity",
    "finite no-hit enumeration is not a premise",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def main() -> None:
    data = json.loads(read_text("verification_summary.json"))
    boundaries = data.get("boundaries", {})
    verification = data.get("verification", {})
    source = data.get("source", {})

    if data.get("case_slug") != EXPECTED["case_slug"]:
        fail("wrong case slug")
    if data.get("result") != EXPECTED["result"]:
        fail("wrong result status")
    if data.get("result_type") != EXPECTED["result_type"]:
        fail("wrong result type")
    if verification.get("status") != EXPECTED["verification_status"]:
        fail("verification status is not independently verified")
    if verification.get("verdict") != EXPECTED["verdict"]:
        fail("independent verdict is not CORRECT")
    if source.get("arxiv") != EXPECTED["arxiv"]:
        fail("wrong arXiv version")
    if source.get("doi") != EXPECTED["doi"]:
        fail("wrong DOI")
    if boundaries.get("novelty") != EXPECTED["novelty"]:
        fail("novelty boundary changed")
    if boundaries.get("priority") != EXPECTED["priority"]:
        fail("priority boundary changed")
    if boundaries.get("finite_enumeration_role") != "not used as a proof premise":
        fail("finite enumeration boundary changed")
    if boundaries.get("star_dissolution") != "not iterated":
        fail("star-dissolution boundary changed")

    proof = read_text("proof.md")
    for marker in REQUIRED_PROOF_MARKERS:
        if marker not in proof:
            fail(f"missing proof marker: {marker}")

    public_text = "\n".join(
        read_text(name)
        for name in (
            "README.md",
            "problem.md",
            "proof.md",
            "status.md",
            "verification.md",
            "sources.md",
            "verification_summary.json",
        )
    )
    for pattern in FORBIDDEN_PUBLIC_MARKERS:
        if pattern.search(public_text):
            fail("private or draft marker leaked into public case files")

    print(
        "PASS: ternary-Berge public certificate matches the released statement and boundary"
    )


if __name__ == "__main__":
    main()
