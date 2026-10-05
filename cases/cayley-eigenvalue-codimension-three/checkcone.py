#!/usr/bin/env python3
"""Recompute symbolic hit-ray gaps and the exact S6 cone boundary.

Requires Python 3.10+ and SymPy. Reads no saved certificate or status flag.
Prints a JSON receipt; --full includes the 44 symbolic gap records.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from itertools import combinations, permutations
import json
from math import factorial

import sympy as sp


@lru_cache(None)
def partitions(n, maximum=None):
    if n == 0:
        return ((),)
    maximum = n if maximum is None else min(n, maximum)
    return tuple((a,) + tail for a in range(maximum, 0, -1)
                 for tail in partitions(n - a, a))


def contains(lam, nu):
    return len(lam) >= len(nu) and all(lam[i] >= nu[i] for i in range(len(nu)))


def added_contents(lam, nu):
    return [c - r for r, length in enumerate(lam, 1)
            for c in range((nu[r - 1] if r <= len(nu) else 0) + 1, length + 1)]


def content_sum(shape, power=1):
    return sum((c - r) ** power for r, length in enumerate(shape, 1)
               for c in range(1, length + 1))


def hit_gap(m, lam, nu):
    return (3 * m * (m - 1) * (m - 2)
            - sum(x ** 3 - (2 * m + 3) * x for x in added_contents(lam, nu))
            + 6 * content_sum(nu))


def symbolic_audit():
    m, z, rho = sp.symbols("m z rho")
    h2 = m * (m - 3) * (2 * m - 3)
    g2 = lambda x: x ** 3 - (2 * m + 1) * x
    u2 = 2 * g2(m - rho + 1) + 2 * m * (2 * rho + 1 - m)
    f2 = (6 * m ** 2 * rho - 9 * m ** 2 - 6 * m * rho ** 2
          + 4 * m * rho + 7 * m + 2 * rho ** 3 - 6 * rho ** 2 + 4 * rho)
    assert sp.expand(h2 - u2 - f2) == 0
    assert sp.expand(f2.subs(rho, 2) - 3 * m * (m - 3)) == 0
    assert sp.Poly(sp.expand(f2.subs(rho, m - 1).subs(m, z + 5)), z).all_coeffs() == [2, 19, 59, 58]
    neg2 = 27 * m ** 2 * (2 * m ** 2 - 11 * m + 11) ** 2 - 16 * (2 * m + 1) ** 3
    assert sp.Poly(sp.expand(neg2.subs(m, z + 5)), z).all_coeffs() == [108, 2052, 15255, 55438, 98895, 71004, 3004]

    h3 = 3 * m * (m - 1) * (m - 2)
    g3 = lambda x: x ** 3 - (2 * m + 3) * x
    u3 = 3 * g3(m - rho + 2) + 3 * m * (2 * rho + 1 - m)
    f3 = 3 * (rho - 2) * (3 * m ** 2 - 3 * m * rho + 2 * m + rho ** 2 - 4 * rho + 1)
    assert sp.expand(h3 - u3 - f3) == 0
    neg3 = 27 * m ** 2 * (m - 1) ** 2 * (m - 3) ** 2 - 4 * (2 * m + 3) ** 3
    assert sp.Poly(sp.expand(neg3.subs(m, z + 5)), z).all_coeffs() == [27, 594, 5319, 24700, 62124, 78024, 34412]

    records = []
    for r, tail in ((0, ()), (1, (1,)), (2, (2,)), (2, (1, 1))):
        nu = (8 - r,) + tail
        cnu = (m - r) * (m - r - 1) / 2 + content_sum(tail) - r
        for lam in partitions(11):
            if not contains(lam, nu):
                continue
            increments = tuple(lam[i] - (nu[i] if i < len(nu) else 0)
                               for i in range(len(lam)))
            xs = []
            for i, length in enumerate(lam, 1):
                old = nu[i - 1] if i <= len(nu) else 0
                for c in range(old + 1, length + 1):
                    xs.append(m + c - i - 8 if i == 1 else c - i)
            gap = sp.expand(h3 - sum(g3(x) for x in xs) + 6 * cnu)
            coeffs = sp.Poly(sp.expand(gap.subs(m, z + 5)), z).all_coeffs()
            degree = lam == (11,)
            standard = lam == (10, 1) and nu == (7, 1)
            if not degree and not standard:
                assert all(c >= 0 for c in coeffs) and coeffs[-1] > 0
            if standard:
                assert gap == 0
            records.append({"rho": r, "tail": list(tail), "increments": list(increments),
                            "gap": str(sp.factor(gap)), "coefficients_at_m_z_plus_5": [int(c) for c in coeffs],
                            "degree": degree, "common_standard": standard})
    assert len(records) == 44

    small = {}
    for order in (4, 5, 6, 7):
        count = 0
        for nu in partitions(order):
            if order > 4 and order - nu[0] > 2:
                continue
            for lam in partitions(order + 3):
                if not contains(lam, nu):
                    continue
                gap = hit_gap(order, lam, nu)
                degree = lam == (order + 3,)
                standard = nu == (order - 1, 1) and lam == (order + 2, 1)
                if not degree and not standard:
                    assert gap > 0
                if standard:
                    assert gap == 0
                count += 1
        small[str(order)] = count
    assert small["4"] == 42
    return {"analytic_identities": "PASS", "stable_pattern_count": len(records),
            "small_containment_counts": small, "symbolic_patterns": records}


@lru_cache(None)
def tableaux(shape):
    """Positions of 1,...,n in all standard tableaux, using corner deletion."""
    if not shape:
        return ((),)
    out = []
    for row, length in enumerate(shape):
        if row + 1 < len(shape) and length == shape[row + 1]:
            continue
        child = list(shape)
        child[row] -= 1
        if child[-1] == 0:
            child.pop()
        for t in tableaux(tuple(child)):
            out.append(t + ((row, length - 1),))
    return tuple(out)


def hook_dimension(shape):
    hooks = 1
    for r, length in enumerate(shape):
        for c in range(length):
            hooks *= length - c + sum(shape[t] > c for t in range(r + 1, len(shape)))
    return factorial(sum(shape)) // hooks


def seminormal(shape):
    """Rational Specht representation; verify its Coxeter relations exactly."""
    ts = tableaux(shape)
    n, dim = sum(shape), len(ts)
    assert dim == hook_dimension(shape)
    index = {t: j for j, t in enumerate(ts)}
    ident = sp.eye(dim)
    generators = []
    for i in range(n - 1):
        matrix = sp.zeros(dim)
        for j, t in enumerate(ts):
            d = (t[i + 1][1] - t[i + 1][0]) - (t[i][1] - t[i][0])
            assert d != 0
            matrix[j, j] = sp.Rational(1, d)
            swapped = list(t)
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
            k = index.get(tuple(swapped))
            if k is not None:
                matrix[k, j] = 1 + sp.Rational(1, d)
        assert matrix * matrix == ident
        generators.append(matrix)
    for i in range(n - 1):
        for j in range(i + 2, n - 1):
            assert generators[i] * generators[j] == generators[j] * generators[i]
        if i + 1 < n - 1:
            a, b = generators[i:i + 2]
            assert a * b * a == b * a * b

    @lru_cache(None)
    def matrix_of(p):
        current = list(p)
        word = []
        while current != list(range(n)):
            for i in range(n - 1):
                if current[i] > current[i + 1]:
                    current[i], current[i + 1] = current[i + 1], current[i]
                    word.append(i)
        matrix = ident
        for i in reversed(word):
            matrix = matrix * generators[i]
        return matrix

    for b in range(1, n):
        jm = sp.zeros(dim)
        for a in range(b):
            transposition = list(range(n))
            transposition[a], transposition[b] = transposition[b], transposition[a]
            jm += matrix_of(tuple(transposition))
        assert jm == sp.diag(*(t[b][1] - t[b][0] for t in ts))
    return matrix_of, dim


def four_cycles(n):
    for support in combinations(range(n), 4):
        for rest in permutations(support[1:]):
            order = (support[0],) + rest
            p = list(range(n))
            for a, b in zip(order, order[1:] + order[:1]):
                p[a] = b
            yield frozenset(support), tuple(p)


def root_audit(matrix, target):
    x = sp.Symbol("x")
    poly = sp.Poly(matrix.charpoly(x).as_expr(), x, domain=sp.QQ)
    multiplicity = 0
    while poly.degree() > 0 and poly.eval(target) == 0:
        poly = poly.exquo(sp.Poly(x - target, x, domain=sp.QQ))
        multiplicity += 1
    assert poly.count_roots(target, sp.oo) == 0
    return multiplicity


def boundary_audit():
    cycles = tuple(four_cycles(6))
    assert len(cycles) == 90 and len({p for _, p in cycles}) == 90
    assert {tuple(p.index(i) for i in range(6)) for _, p in cycles} == {p for _, p in cycles}
    targets = {2: (18, 20, 16), 3: (18, 24, 12)}
    rows = {2: [], 3: []}
    dimension_squared_sum = 0
    for shape in partitions(6):
        representation, dim = seminormal(shape)
        dimension_squared_sum += dim ** 2
        for marked in (2, 3):
            orbit = [sp.zeros(dim) for _ in range(marked + 1)]
            counts = [0] * (marked + 1)
            for support, p in cycles:
                j = len(support & frozenset(range(marked)))
                orbit[j] += representation(p)
                counts[j] += 1
            assert counts == ([6, 48, 36] if marked == 2 else [0, 18, 54, 18])
            normal = sum(orbit, sp.zeros(dim))
            scalar = content_sum(shape, 3) - 9 * content_sum(shape)
            assert normal == scalar * sp.eye(dim)
            rays = ((normal, orbit[1] + orbit[2], orbit[2]) if marked == 2
                    else (normal, orbit[2] + orbit[3], orbit[3]))
            if shape == (6,):
                assert [int(a[0, 0]) for a in rays] == ([90, 84, 36] if marked == 2 else [90, 72, 18])
                continue
            multiplicities = [root_audit(a, t) for a, t in zip(rays, targets[marked])]
            if shape == (5, 1):
                assert multiplicities == ([5, 3, 3] if marked == 2 else [5, 2, 2])
            else:
                assert multiplicities[1:] == [0, 0]
                assert multiplicities[0] == (dim if shape == (2, 2, 2) else 0)
            rows[marked].append({"partition": list(shape), "dimension": dim,
                                 "target_multiplicities": multiplicities})
    assert dimension_squared_sum == 720

    for marked in (2, 3):
        natural = [sp.zeros(6) for _ in range(3)]
        for support, p in cycles:
            j = len(support & frozenset(range(marked)))
            included = (True, j >= (1 if marked == 2 else 2), j >= marked)
            for ray, use in enumerate(included):
                if use:
                    for i in range(6):
                        natural[ray][p[i], i] += 1
        w = sp.zeros(6, 5 - marked)
        for j, i in enumerate(range(marked, 5)):
            w[i, j], w[5, j] = 1, -1
        assert all(a * w == t * w for a, t in zip(natural, targets[marked]))
    return {"irreducible_partition_count": len(partitions(6)),
            "dimension_squared_sum": dimension_squared_sum,
            "exact_coxeter_jucys_murphy_and_sturm_checks": "PASS",
            "r2": rows[2], "r3": rows[3], "extra_normal_equality": [2, 2, 2]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true")
    args = parser.parse_args()
    symbolic = symbolic_audit()
    if not args.full:
        del symbolic["symbolic_patterns"]
    result = {"status": "PASS", "symbolic": symbolic, "S6": boundary_audit(),
              "scope": "Symbolic low-tail rays plus the complete fixed S6 boundary. General large-tail inequalities and stable-pattern coverage are proved in coneproof.md."}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
