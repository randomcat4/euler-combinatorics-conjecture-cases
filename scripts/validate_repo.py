"""Validate the public EULER combinatorics case collection."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT = (
    "README.md",
    "LICENSE",
    "PROJECT_STATE.json",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "docs/status.md",
    "docs/sources.md",
    "docs/workflow.md",
    "docs/provenance.md",
    "cases/README.md",
    "manifests/artifacts.json",
)

CASE_SLUGS = (
    "volume-rigidity-dimension-seven",
    "k33plus-q-index-boundary-counterexample",
    "toroidal-grid-representation-counterexample",
    "path-set-tree-representation-counterexample",
    "f29-inducibility-recursive-graphon-counterexample",
    "minimal-degree-three-imprimitive-groups",
    "steklov-three-leaf-extra-special-extremizer",
    "orthogonal-tree-seven-vertex-obstructions",
    "cayley-eigenvalue-codimension-three",
    "catalan-schett-plane-tree-statistic",
    "cdk-improper-partition-matrix-image",
    "ternary-berge-suspension-rigidity",
    "partition-matrix-bijection",
    "partition-matrix-q-sum-product",
    "zhao-restricted-zero-sum-counterexample",
)

CASE_REQUIRED = {
    "volume-rigidity-dimension-seven": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "paper/main.tex",
        "paper/main.pdf",
        "paper/references.bib",
        "evidence/hyperedges.md",
    ),
    "k33plus-q-index-boundary-counterexample": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "check_counterexample.py",
        "exhaustive_summary.json",
    ),
    "toroidal-grid-representation-counterexample": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "word_certificate.json",
        "check_counterexample.py",
        "verification_summary.json",
    ),
    "path-set-tree-representation-counterexample": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "counterexample_certificate.json",
        "check_counterexample.py",
        "verification_summary.json",
    ),
    "f29-inducibility-recursive-graphon-counterexample": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "counterexample_certificate.json",
        "check_counterexample.py",
        "verification_summary.json",
    ),
    "minimal-degree-three-imprimitive-groups": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "quotient_certificate.json",
        "check_quotient_criterion.py",
        "verification_summary.json",
    ),
    "steklov-three-leaf-extra-special-extremizer": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "spider_certificate.json",
        "check_three_leaf_extremizer.py",
        "verification_summary.json",
    ),
    "orthogonal-tree-seven-vertex-obstructions": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "counterexample_certificate.json",
        "check_counterexamples.py",
        "verification_summary.json",
    ),
    "cayley-eigenvalue-codimension-three": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "paper/main.tex",
        "paper/main.pdf",
        "paper/references.bib",
        "evidence/low_order_cases.json",
    ),
    "catalan-schett-plane-tree-statistic": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "check_small_cases.py",
        "small_case_summary.json",
    ),
    "cdk-improper-partition-matrix-image": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "finite-regression.md",
        "mine_cdk_image.py",
        "mining_n_le_8.json",
    ),
    "ternary-berge-suspension-rigidity": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "check_statement_certificate.py",
        "verification_summary.json",
    ),
    "partition-matrix-bijection": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "verify_bijection.py",
        "exhaustive-check.md",
    ),
    "partition-matrix-q-sum-product": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "formula-check.md",
        "check_formula.py",
    ),
    "zhao-restricted-zero-sum-counterexample": (
        "README.md",
        "problem.md",
        "status.md",
        "sources.md",
        "verification.md",
        "proof.md",
        "check_counterexample.py",
        "exhaustive_summary.json",
    ),
}

EXPECTED_VERIFICATION = {
    "volume-rigidity-dimension-seven": "INDEPENDENTLY_VERIFIED",
    "k33plus-q-index-boundary-counterexample": "INDEPENDENTLY_VERIFIED",
    "toroidal-grid-representation-counterexample": "INDEPENDENTLY_VERIFIED",
    "path-set-tree-representation-counterexample": "INDEPENDENTLY_VERIFIED",
    "f29-inducibility-recursive-graphon-counterexample": "INDEPENDENTLY_VERIFIED",
    "minimal-degree-three-imprimitive-groups": "INDEPENDENTLY_VERIFIED",
    "steklov-three-leaf-extra-special-extremizer": "INDEPENDENTLY_VERIFIED",
    "orthogonal-tree-seven-vertex-obstructions": "INDEPENDENTLY_VERIFIED",
    "cayley-eigenvalue-codimension-three": "INDEPENDENTLY_VERIFIED",
    "catalan-schett-plane-tree-statistic": "INDEPENDENTLY_VERIFIED",
    "cdk-improper-partition-matrix-image": "INDEPENDENTLY_VERIFIED",
    "ternary-berge-suspension-rigidity": "INDEPENDENTLY_VERIFIED",
    "partition-matrix-bijection": "INDEPENDENTLY_VERIFIED",
    "partition-matrix-q-sum-product": "INDEPENDENTLY_VERIFIED",
    "zhao-restricted-zero-sum-counterexample": "INDEPENDENTLY_VERIFIED",
}

TEXT_SUFFIXES = {".bib", ".json", ".md", ".py", ".tex", ".txt", ".yml", ".yaml"}
SKIP_DIRS = {".git", "__pycache__"}

FORBIDDEN_PATTERNS = (
    ("CJK text", re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")),
    (
        "local Windows path",
        re.compile(
            r"\b[A-Za-z]:\\(?:Users|Windows|ProgramData|Program Files|game|tmp)\\",
            re.IGNORECASE,
        ),
    ),
    ("GitHub classic token", re.compile(r"ghp_[A-Za-z0-9]{20,}")),
    ("GitHub fine-grained token", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
    ("private key", re.compile(r"BEGIN [A-Z ]*PRIVATE KEY")),
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_required() -> None:
    missing = [name for name in REQUIRED_ROOT if not (ROOT / name).is_file()]
    if missing:
        fail("missing required files: " + ", ".join(missing))
    for slug in CASE_SLUGS:
        case_root = ROOT / "cases" / slug
        for name in CASE_REQUIRED[slug]:
            if not (case_root / name).is_file():
                fail(f"missing required case file: cases/{slug}/{name}")


def validate_state() -> None:
    state = json.loads((ROOT / "PROJECT_STATE.json").read_text(encoding="utf-8"))
    if state.get("language") != "en":
        fail("public repository language must remain English")
    cases = state.get("cases", {})
    if tuple(cases) != CASE_SLUGS:
        fail("PROJECT_STATE.json case order or membership changed")
    for slug, item in cases.items():
        if item.get("verification") != EXPECTED_VERIFICATION[slug]:
            fail(f"verification gate is not preserved for {slug}")
        if item.get("novelty") != "NOT_ESTABLISHED":
            fail(f"novelty boundary changed for {slug}")
    gao = state.get("external_releases", {}).get("gao-generalized-dihedral", {})
    if gao.get("repository") != "https://github.com/randomcat4/gaoLEAN":
        fail("public Gao release link changed")
    if gao.get("scope") != "completed 13-page manuscript and its corresponding Lean formalization":
        fail("public Gao release scope changed")


def validate_public_boundary() -> None:
    forbidden_suffixes = {".key", ".pem", ".pfx", ".zip"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        relative = path.relative_to(ROOT)
        if path.suffix.lower() in forbidden_suffixes or path.name == ".env":
            fail(f"forbidden file type: {relative}")
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if relative == Path("scripts/validate_repo.py"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                fail(f"{label} found in {relative}")


def digest(path: Path) -> str:
    if path.suffix.lower() != ".pdf":
        content = path.read_bytes().replace(b"\r\n", b"\n")
        return hashlib.sha256(content).hexdigest()
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def validate_manifest() -> None:
    manifest = json.loads(
        (ROOT / "manifests" / "artifacts.json").read_text(encoding="utf-8")
    )
    listed = {item["path"]: item["sha256"] for item in manifest["artifacts"]}
    expected = {
        path.relative_to(ROOT).as_posix()
        for slug in CASE_SLUGS
        for path in (ROOT / "cases" / slug).rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and not path.name.endswith(
            (".aux", ".bbl", ".blg", ".log", ".out", ".synctex.gz", ".toc")
        )
    }
    expected.add("cases/README.md")
    if set(listed) != expected:
        fail("artifact manifest membership does not match the public case files")
    for relative, expected_hash in listed.items():
        actual = digest(ROOT / relative)
        if actual.lower() != expected_hash.lower():
            fail(f"artifact hash mismatch: {relative}")


def main() -> None:
    validate_required()
    validate_state()
    validate_public_boundary()
    validate_manifest()
    print("PASS: structure, status gates, English-only policy, and public boundary")


if __name__ == "__main__":
    main()
