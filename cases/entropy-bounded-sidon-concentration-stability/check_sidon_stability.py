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
    "extension_verdicts": ["CORRECT", "CORRECT"],
    "extension_review_count": 2,
    "fixed_d_rate": "for every fixed D>0, M(C,D)=D/log(1/C)*(1+o(1)) as C->0",
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

REQUIRED_EXTENSION_MARKERS = (
    "M(C,D) = D/log(1/C) * (1+o(1))",
    "x(C,D) = 2 W_0",
    "tau_* = exp(-x(C,D))",
    "a_{i,r} = b^(2i) + r b^(2i+1)",
    "Delta(X) = E^2 kappa_m / N",
    "d_Sid(X) = E * (1 - sigma_m/m)",
    "liminf_{C->0} (L/D) M(C,D) >= 1",
    "M(C,D_C)=Theta(sqrt(C))",
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


def binary_entropy(value: float) -> float:
    if value <= 0.0 or value >= 1.0:
        return 0.0
    return -value * math.log(value) - (1.0 - value) * math.log(1.0 - value)


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


def is_sidon_int(indices: set[int], values: list[int]) -> bool:
    seen = {}
    ordered = sorted(indices)
    for pos, i in enumerate(ordered):
        for j in ordered[pos:]:
            total = values[i] + values[j]
            pair = (i, j)
            previous = seen.setdefault(total, pair)
            if previous != pair:
                return False
    return True


def best_sidon_mass_int(values: list[int], probabilities: list[float]) -> float:
    best = 0.0
    for mask in range(1 << len(values)):
        indices = {i for i in range(len(values)) if mask & (1 << i)}
        if is_sidon_int(indices, values):
            best = max(best, sum(probabilities[i] for i in indices))
    return best


def delta_int(values: list[int], probabilities: list[float]) -> float:
    support = [i for i, p in enumerate(probabilities) if p > 0.0]
    h_x = entropy(probabilities)
    q: dict[int, float] = {}
    for i in support:
        for j in support:
            total = values[i] + values[j]
            q[total] = q.get(total, 0.0) + probabilities[i] * probabilities[j]
    h_sum = -sum(value * math.log(value) for value in q.values() if value > 0.0)
    collision = sum(p * p for p in probabilities)
    return max(0.0, 2.0 * h_x - h_sum - LN2 * (1.0 - collision))


def solve_lambert_x(c_value: float, d_value: float) -> float:
    target = math.log(d_value * LN2 / c_value)
    lo = 1e-15
    hi = 1.0
    while hi + 2.0 * math.log(hi) <= target:
        hi *= 2.0
    for _ in range(160):
        mid = (lo + hi) / 2.0
        if mid + 2.0 * math.log(mid) <= target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def interval_sigma(m_value: int) -> int:
    values = list(range(1, m_value + 1))
    best = 0
    for mask in range(1 << m_value):
        indices = {i for i in range(m_value) if mask & (1 << i)}
        if len(indices) > best and is_sidon_int(indices, values):
            best = len(indices)
    return best


def dense_block_values(m_value: int, n_blocks: int) -> tuple[list[int], list[tuple[int, int] | None]]:
    base = 2 * m_value + 1
    values = [0]
    labels: list[tuple[int, int] | None] = [None]
    for block in range(n_blocks):
        for label in range(1, m_value + 1):
            values.append(base ** (2 * block) + label * base ** (2 * block + 1))
            labels.append((block, label))
    return values, labels


def nu_interval(m_value: int, total: int) -> int:
    return sum(1 for r_value in range(1, m_value + 1) if 1 <= total - r_value <= m_value)


def kappa_interval(m_value: int) -> float:
    total = 0.0
    for r_value in range(1, m_value + 1):
        for s_value in range(1, m_value + 1):
            total += math.log(nu_interval(m_value, r_value + s_value))
            if r_value != s_value:
                total -= LN2
    return total / (m_value * m_value)


def audit_no_carry_classes(values: list[int], labels: list[tuple[int, int] | None]) -> None:
    seen: dict[int, tuple[int, int]] = {}
    for i in range(len(values)):
        for j in range(i, len(values)):
            total = values[i] + values[j]
            pair = (i, j)
            previous = seen.setdefault(total, pair)
            if previous == pair:
                continue
            first = (labels[previous[0]], labels[previous[1]])
            second = (labels[i], labels[j])
            if None in first or None in second:
                fail("zero atom participates in a dense-block collision")
            first_blocks = {item[0] for item in first if item is not None}
            second_blocks = {item[0] for item in second if item is not None}
            if len(first_blocks) != 1 or first_blocks != second_blocks:
                fail("cross-block dense collision found")
            first_sum = sum(item[1] for item in first if item is not None)
            second_sum = sum(item[1] for item in second if item is not None)
            if first_sum != second_sum:
                fail("dense collision is not explained by equal interval sums")


def audit_lambert_optimizer() -> None:
    for c_value, d_value in ((1e-4, 2.0), (0.01, 0.5), (0.2, 3.0), (0.7, 0.3)):
        x_value = solve_lambert_x(c_value, d_value)
        tau = math.exp(-x_value)
        if not 0.0 < tau < 1.0:
            fail("Lambert optimizer threshold is outside (0,1)")
        lhs = x_value * x_value * math.exp(x_value)
        rhs = d_value * LN2 / c_value
        if abs(lhs - rhs) > 1e-10 * max(1.0, rhs):
            fail("Lambert optimizer equation mismatch")
        tau_from_formula = c_value * x_value * x_value / (d_value * LN2)
        if abs(tau - tau_from_formula) > 1e-10:
            fail("Lambert optimizer threshold formula mismatch")
        optimum = d_value / x_value + (c_value / LN2) * math.exp(x_value)
        closed = d_value * (x_value + 1.0) / (x_value * x_value)
        if abs(optimum - closed) > 1e-10:
            fail("Lambert closed-form minimum mismatch")
        for scale in (0.5, 0.8, 1.25, 2.0):
            probe = x_value * scale
            value = d_value / probe + (c_value / LN2) * math.exp(probe)
            if value + 1e-10 < optimum:
                fail("Lambert optimizer is not minimal on probe points")


def audit_dense_blocks() -> None:
    for m_value, n_blocks, e_value in ((3, 2, 0.2), (4, 3, 0.35), (5, 2, 0.25)):
        values, labels = dense_block_values(m_value, n_blocks)
        probabilities = [1.0 - e_value] + [e_value / (m_value * n_blocks)] * (
            m_value * n_blocks
        )
        audit_no_carry_classes(values, labels)
        expected_entropy = binary_entropy(e_value) + e_value * math.log(m_value * n_blocks)
        if abs(entropy(probabilities) - expected_entropy) > 1e-10:
            fail("dense-block entropy formula mismatch")
        kappa = kappa_interval(m_value)
        if kappa - math.log(m_value) > 1e-10:
            fail("dense-block kappa exceeds log(m)")
        expected_delta = e_value * e_value * kappa / n_blocks
        if abs(delta_int(values, probabilities) - expected_delta) > 1e-10:
            fail("dense-block defect formula mismatch")
        sigma = interval_sigma(m_value)
        if sigma > (1.0 + math.sqrt(8 * m_value - 7)) / 2.0 + 1e-10:
            fail("interval Sidon positive-difference bound mismatch")
        best_mass = best_sidon_mass_int(values, probabilities)
        expected_best = 1.0 - e_value + e_value * sigma / m_value
        if abs(best_mass - expected_best) > 1e-10:
            fail("dense-block exact Sidon deletion mass mismatch")


def audit_four_point_regime() -> None:
    e_value = 0.2
    values = [0, 12, 23, 45, 56]
    probabilities = [1.0 - e_value] + [e_value / 4.0] * 4
    expected_delta = e_value * e_value * LN2 / 4.0
    if abs(delta_int(values, probabilities) - expected_delta) > 1e-10:
        fail("four-point defect formula mismatch")
    best_mass = best_sidon_mass_int(values, probabilities)
    if abs(best_mass - (1.0 - e_value / 4.0)) > 1e-10:
        fail("four-point deletion mass mismatch")
    d_c = binary_entropy(e_value) + e_value * math.log(4.0)
    if abs(entropy(probabilities) - d_c) > 1e-10:
        fail("four-point entropy formula mismatch")


def audit_optimal_modulus_extension() -> None:
    audit_lambert_optimizer()
    audit_dense_blocks()
    audit_four_point_regime()


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
    if verification.get("extension_verdicts") != EXPECTED["extension_verdicts"]:
        fail("extension independent verdicts are not both CORRECT")
    if verification.get("extension_review_count") != EXPECTED["extension_review_count"]:
        fail("extension review count mismatch")
    extension = data.get("optimal_modulus_extension", {})
    if extension.get("status") != EXPECTED["verification_status"]:
        fail("extension is not independently verified")
    if extension.get("fixed_D_rate") != EXPECTED["fixed_d_rate"]:
        fail("fixed-D optimal-modulus rate changed")
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
    extension_text = read_text("optimal_modulus.md")
    for marker in REQUIRED_EXTENSION_MARKERS:
        if marker not in extension_text:
            fail(f"missing extension marker: {marker}")

    public_text = "\n".join(
        read_text(name)
        for name in (
            "README.md",
            "problem.md",
            "proof.md",
            "optimal_modulus.md",
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
    audit_optimal_modulus_extension()

    print("PASS: entropy-bounded Sidon stability and optimal-modulus certificates verified")


if __name__ == "__main__":
    main()
