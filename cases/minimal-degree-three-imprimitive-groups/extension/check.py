#!/usr/bin/env python3
"""Finite verification of the regular-cyclic classification claims.

All vector spaces are represented exactly by bit vectors over F_2.
The script is self-contained and uses only the Python standard library.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "results.json"
MAX_K = 12


def rotate(v: int, k: int, steps: int = 1) -> int:
    steps %= k
    mask = (1 << k) - 1
    return ((v << steps) & mask) | (v >> (k - steps) if steps else 0)


def rref(vectors: list[int] | tuple[int, ...], n: int) -> tuple[int, ...]:
    """Unique reduced row basis, ordered by decreasing pivot."""
    rows = [0] * n
    for raw in vectors:
        x = raw
        for p in range(n - 1, -1, -1):
            if rows[p] and ((x >> p) & 1):
                x ^= rows[p]
        if not x:
            continue
        p = x.bit_length() - 1
        for q in range(p - 1, -1, -1):
            if rows[q] and ((x >> q) & 1):
                x ^= rows[q]
        rows[p] = x
        for q in range(p + 1, n):
            if rows[q] and ((rows[q] >> p) & 1):
                rows[q] ^= x
    return tuple(rows[p] for p in range(n - 1, -1, -1) if rows[p])


def reduce_mod(v: int, basis: tuple[int, ...]) -> int:
    x = v
    for row in basis:
        p = row.bit_length() - 1
        if (x >> p) & 1:
            x ^= row
    return x


def cyclic_span(v: int, k: int) -> tuple[int, ...]:
    return rref([rotate(v, k, j) for j in range(k)], k)


def poly_degree(f: int) -> int:
    return f.bit_length() - 1


def poly_mod(a: int, b: int) -> int:
    db = poly_degree(b)
    while a and poly_degree(a) >= db:
        a ^= b << (poly_degree(a) - db)
    return a


def poly_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, poly_mod(a, b)
    return a


def xplus1_valuation(f: int) -> int:
    """Multiplicity of X+1 in a nonzero F_2 polynomial."""
    s = 0
    divisor = 0b11
    while f and poly_mod(f, divisor) == 0:
        q = 0
        r = f
        dd = poly_degree(divisor)
        while r and poly_degree(r) >= dd:
            shift = poly_degree(r) - dd
            q ^= 1 << shift
            r ^= divisor << shift
        assert r == 0
        f = q
        s += 1
    return s


def permute_multiplier(v: int, k: int, u: int) -> int:
    out = 0
    for i in range(k):
        if (v >> i) & 1:
            out |= 1 << ((u * i) % k)
    return out


def multiplier_units(k: int) -> list[int]:
    return [u for u in range(k) if math.gcd(u, k) == 1] if k > 1 else [0]


def doubling_orbits(d: int) -> list[tuple[int, ...]]:
    if d == 1:
        return [(0,)]
    unseen = set(range(d))
    answer = []
    while unseen:
        start = min(unseen)
        orbit = []
        x = start
        while x not in orbit:
            orbit.append(x)
            unseen.discard(x)
            x = (2 * x) % d
        answer.append(tuple(sorted(orbit)))
    return sorted(answer)


def cycles_on_doubling_orbits(d: int, a: int) -> int:
    orbits = doubling_orbits(d)
    index = {x: j for j, orb in enumerate(orbits) for x in orb}
    perm = [index[(a * orb[0]) % d] for orb in orbits]
    seen: set[int] = set()
    cycles = 0
    for i in range(len(orbits)):
        if i in seen:
            continue
        cycles += 1
        j = i
        while j not in seen:
            seen.add(j)
            j = perm[j]
    return cycles


def formula_count(k: int) -> int:
    e = k & -k
    d = k // e
    units = [a for a in range(1, d) if math.gcd(a, d) == 1] if d > 1 else [0]
    total = sum(2 * e * (e + 1) ** (cycles_on_doubling_orbits(d, a) - 1) for a in units)
    assert total % len(units) == 0
    return total // len(units) - 1


def enumerate_one_k(k: int) -> dict:
    modulus = (1 << k) | 1  # X^k + 1 = X^k - 1 over F_2
    code_to_generator: dict[tuple[int, ...], int] = {}
    for v in range(1 << k):
        code = cyclic_span(v, k)
        generator = poly_gcd(v, modulus)
        old = code_to_generator.setdefault(code, generator)
        assert old == generator

    # Closure under sums and intersections is an independent lattice sanity check.
    codes = sorted(code_to_generator, key=lambda b: (len(b), b))
    code_set = set(codes)
    lattice_sum_ok = True
    lattice_intersection_ok = True
    if k <= 10:
        element_sets = {
            b: {x for x in range(1 << k) if reduce_mod(x, b) == 0} for b in codes
        }
        for i, a in enumerate(codes):
            for b in codes[i:]:
                lattice_sum_ok &= rref(a + b, k) in code_set
                inter = element_sets[a] & element_sets[b]
                lattice_intersection_ok &= rref(tuple(inter), k) in code_set

    e = k & -k
    full_code = rref(tuple(1 << i for i in range(k)), k)
    for code in codes:
        g = code_to_generator[code]
        s = xplus1_valuation(g)
        quotient = sorted({reduce_mod(v, code) for v in range(1 << k)})
        norm_kernel = []
        for a in quotient:
            norm = 0
            for j in range(k):
                norm ^= rotate(a, k, j)
            if reduce_mod(norm, code) == 0:
                norm_kernel.append(a)
        coboundaries = sorted(
            {reduce_mod(b ^ rotate(b, k), code) for b in range(1 << k)}
        )
        assert all(a in norm_kernel for a in coboundaries)
        classes = {
            min(reduce_mod(a ^ b, code) for b in coboundaries)
            for a in norm_kernel
        }
        predicted_h1_size = 2 if 0 < s < e else 1
        assert len(classes) == predicted_h1_size

    # Compute multiplier orbits of proper codes directly on coordinates.
    proper_codes = [c for c in codes if c != full_code]
    remaining = set(proper_codes)
    code_orbits: list[list[tuple[int, ...]]] = []
    for seed in proper_codes:
        if seed not in remaining:
            continue
        orbit = {
            rref(tuple(permute_multiplier(row, k, u) for row in seed), k)
            for u in multiplier_units(k)
        }
        assert orbit <= set(proper_codes)
        remaining -= orbit
        code_orbits.append(sorted(orbit))
    assert not remaining, (k, len(remaining), remaining)

    weighted_orbit_count = 0
    orbit_twist_profile = Counter()
    for orbit in code_orbits:
        s_values = {xplus1_valuation(code_to_generator[c]) for c in orbit}
        assert len(s_values) == 1
        s = next(iter(s_values))
        weight = 2 if 0 < s < e else 1
        weighted_orbit_count += weight
        orbit_twist_profile["two_twists" if weight == 2 else "one_twist"] += 1

    predicted = formula_count(k)
    assert weighted_orbit_count == predicted
    if k & (k - 1) == 0:
        assert weighted_orbit_count == 2 * k - 1

    return {
        "k": k,
        "e": e,
        "d": k // e,
        "cyclic_code_count_including_full": len(codes),
        "proper_code_count_labelled": len(proper_codes),
        "proper_code_multiplier_orbits": len(code_orbits),
        "twist_profile_of_code_orbits": dict(orbit_twist_profile),
        "classified_group_count": weighted_orbit_count,
        "burnside_formula_count": predicted,
        "lattice_sum_ok": bool(lattice_sum_ok),
        "lattice_intersection_ok": bool(lattice_intersection_ok),
        "h1_rule_checked_for_all_codes": True,
    }


def main() -> None:
    per_k = [enumerate_one_k(k) for k in range(1, MAX_K + 1)]
    listed = [r["classified_group_count"] for r in per_k[:9]]
    assert listed == [1, 3, 3, 7, 3, 11, 5, 15, 7]
    result = {
        "problem": "minimal-degree-three-cyclic-actions",
        "status": "PASS_FINITE_EXACT",
        "claim_scope": "cyclic-code and cocycle classification for regular cyclic block actions",
        "coverage": {
            "k_range": [1, MAX_K],
            "listed_counts_k1_to_k9": listed,
            "checks": [
                "all cyclic spans generated by every vector",
                "shift-invariant code lattice closure under sum/intersection for k<=10",
                "direct norm-kernel/coboundary quotient H^1",
                "all even and odd k in range",
                "direct multiplier orbits on coordinates",
                "Burnside formula comparison",
                "power-of-two count 2k-1",
            ],
        },
        "per_k": per_k,
    }
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: result[k] for k in ("problem", "status")}, ensure_ascii=False))
    print("counts_k1_to_k12", [r["classified_group_count"] for r in per_k])


if __name__ == "__main__":
    main()
