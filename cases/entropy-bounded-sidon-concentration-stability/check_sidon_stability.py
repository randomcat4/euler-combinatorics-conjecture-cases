"""Check the public certificate for the entropy-bounded Sidon case.

This script is a release-boundary and finite sanity check, not a proof
assistant. The general theorem is proved in proof.md and was independently
reviewed before public curation.
"""

from __future__ import annotations

import itertools
import json
import math
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LN2 = math.log(2.0)
TOL = 1e-10

EXPECTED = {
    "case_slug": "entropy-bounded-sidon-concentration-stability",
    "result": "PROVED",
    "result_type": "COMPLETE_SOLUTION",
    "verification_status": "INDEPENDENTLY_VERIFIED",
    "verdicts": ["CORRECT", "CORRECT"],
    "arxiv": "2506.20813v2",
    "doi": "10.1109/TIT.2026.3653549",
    "novelty": "NOT_ESTABLISHED",
    "priority": "NOT_ESTABLISHED",
    "distribution_count": 995,
}

FORBIDDEN_PUBLIC_MARKERS = (
    re.compile(r"01a0[0-9a-f-]+"),
    re.compile(r"pull/\d+"),
    re.compile("issue" + "comment-"),
    re.compile(r"\b[A-Za-z]:\\"),
    re.compile("/" + "root/"),
    re.compile("combinatorics-" + "conjecture-" + "lab"),
    re.compile("ARXIV" + "_READY"),
)

REQUIRED_PROOF_MARKERS = (
    "R(a,b) = log(q_{a+b}/(p_a p_b))",
    "E R(X,X') <= C",
    "P(E_bad) <= C/log 2",
    "u(a,b) = 2p_a p_b / (1 + 1_{a=b})",
    "P(X in L_tau) <= D/log(1/tau)",
    "P(X in D_tau)",
    "tau=sqrt(C)",
    "C=0",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(name: str) -> str:
    return (ROOT / name).read_text(encoding="utf-8")


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def elements(mods: tuple[int, ...]) -> list[tuple[int, ...]]:
    return list(itertools.product(*(range(m) for m in mods)))


def add(a: tuple[int, ...], b: tuple[int, ...], mods: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % m for x, y, m in zip(a, b, mods))


def entropy(probabilities: list[float]) -> float:
    return -sum(p * math.log(p) for p in probabilities if p > 0.0)


def sidon_masks(elts: list[tuple[int, ...]], mods: tuple[int, ...]) -> list[int]:
    result = []
    n = len(elts)
    for mask in range(1 << n):
        seen = {}
        ok = True
        chosen = [i for i in range(n) if mask & (1 << i)]
        for idx, i in enumerate(chosen):
            for j in chosen[idx:]:
                z = add(elts[i], elts[j], mods)
                pair = (i, j)
                previous = seen.setdefault(z, pair)
                if previous != pair:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            result.append(mask)
    return result


def is_sidon(indices: set[int], elts: list[tuple[int, ...]], mods: tuple[int, ...]) -> bool:
    seen = {}
    ordered = sorted(indices)
    for pos, i in enumerate(ordered):
        for j in ordered[pos:]:
            z = add(elts[i], elts[j], mods)
            pair = (i, j)
            previous = seen.setdefault(z, pair)
            if previous != pair:
                return False
    return True


def f_bound(c_value: float, d_value: float) -> float:
    if c_value <= TOL:
        return 0.0
    if c_value >= 1.0:
        return 1.0
    return min(1.0, 2.0 * d_value / math.log(1.0 / c_value) + math.sqrt(c_value) / LN2)


def audit_distribution(
    mods: tuple[int, ...],
    elts: list[tuple[int, ...]],
    masks: list[int],
    probabilities: list[float],
) -> None:
    support = [i for i, p in enumerate(probabilities) if p > 0.0]
    h_x = entropy(probabilities)
    q = {}
    for i in support:
        for j in support:
            z = add(elts[i], elts[j], mods)
            q[z] = q.get(z, 0.0) + probabilities[i] * probabilities[j]
    h_sum = -sum(value * math.log(value) for value in q.values() if value > 0.0)
    collision = sum(p * p for p in probabilities)
    c_value = max(0.0, 2.0 * h_x - h_sum - LN2 * (1.0 - collision))
    d_value = h_x
    f_value = f_bound(c_value, d_value)

    best = 0.0
    for mask in masks:
        mass = sum(probabilities[i] for i in range(len(elts)) if mask & (1 << i))
        best = max(best, mass)
    if best + 5e-9 < 1.0 - f_value:
        fail(f"finite Sidon optimum violates bound for group {mods}")

    if c_value <= TOL:
        constructed = set(support)
        claimed_loss = 0.0
    elif c_value >= 1.0:
        constructed = set()
        claimed_loss = 1.0
    else:
        tau = math.sqrt(c_value)
        raw = 2.0 * d_value / math.log(1.0 / c_value) + math.sqrt(c_value) / LN2
        if raw >= 1.0:
            constructed = set()
            claimed_loss = 1.0
        else:
            heavy = [i for i in support if probabilities[i] >= tau]
            deleted = set()
            for pos, i in enumerate(heavy):
                for j in heavy[pos:]:
                    z = add(elts[i], elts[j], mods)
                    ratio = q[z] / (probabilities[i] * probabilities[j])
                    surplus = math.log(ratio) - (LN2 if i != j else 0.0)
                    if surplus + 1e-12 >= LN2:
                        if i == j:
                            deleted.add(i)
                        elif probabilities[i] < probabilities[j] - 1e-15:
                            deleted.add(i)
                        elif probabilities[j] < probabilities[i] - 1e-15:
                            deleted.add(j)
                        else:
                            deleted.add(min(i, j))
            constructed = set(heavy) - deleted
            claimed_loss = raw

    if not is_sidon(constructed, elts, mods):
        fail(f"constructed set is not Sidon for group {mods}")
    mass = sum(probabilities[i] for i in constructed)
    if mass + 5e-9 < 1.0 - claimed_loss:
        fail(f"constructed Sidon set violates proof loss for group {mods}")


def run_finite_probes() -> int:
    group_specs = [((n,), 6) for n in range(1, 6)] + [((2, 2), 6)]
    count = 0
    for mods, max_den in group_specs:
        elts = elements(mods)
        masks = sidon_masks(elts, mods)
        for den in range(1, max_den + 1):
            for counts in compositions(den, len(elts)):
                probabilities = [value / den for value in counts]
                audit_distribution(mods, elts, masks, probabilities)
                count += 1
    return count


def main() -> None:
    data = json.loads(read_text("verification_summary.json"))
    source = data.get("source", {})
    boundaries = data.get("boundaries", {})
    verification = data.get("verification", {})
    finite = data.get("finite_probe_summary", {})

    if data.get("case_slug") != EXPECTED["case_slug"]:
        fail("wrong case slug")
    if data.get("result") != EXPECTED["result"]:
        fail("wrong result status")
    if data.get("result_type") != EXPECTED["result_type"]:
        fail("wrong result type")
    if source.get("arxiv") != EXPECTED["arxiv"]:
        fail("wrong arXiv version")
    if source.get("doi") != EXPECTED["doi"]:
        fail("wrong DOI")
    if verification.get("status") != EXPECTED["verification_status"]:
        fail("verification is not independently verified")
    if verification.get("verdicts") != EXPECTED["verdicts"]:
        fail("independent verdicts are not both CORRECT")
    if boundaries.get("novelty") != EXPECTED["novelty"]:
        fail("novelty boundary changed")
    if boundaries.get("priority") != EXPECTED["priority"]:
        fail("priority boundary changed")
    if finite.get("expected_distribution_count") != EXPECTED["distribution_count"]:
        fail("finite-probe denominator changed")

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
            fail("private, draft, or local marker leaked into public case files")

    count = run_finite_probes()
    if count != EXPECTED["distribution_count"]:
        fail("finite-probe distribution count mismatch")

    print("PASS: entropy-bounded Sidon stability certificate and finite probes verified")


if __name__ == "__main__":
    main()
