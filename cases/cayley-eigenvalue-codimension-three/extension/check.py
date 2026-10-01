from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parent
TOL = 2e-8


def partitions(n, cap=None):
    cap = n if cap is None else min(cap, n)
    if n == 0:
        yield ()
    else:
        for first in range(cap, 0, -1):
            for tail in partitions(n - first, first):
                yield (first,) + tail


def tableaux(shape):
    n = sum(shape)

    def rec(current, k, positions):
        if k == 0:
            yield tuple(positions[i] for i in range(1, n + 1))
            return
        for row in range(len(current)):
            below = current[row + 1] if row + 1 < len(current) else 0
            if current[row] <= below:
                continue
            col = current[row] - 1
            nxt = list(current)
            nxt[row] -= 1
            while nxt and nxt[-1] == 0:
                nxt.pop()
            positions[k] = (row, col)
            yield from rec(tuple(nxt), k - 1, positions)
            del positions[k]

    return list(rec(tuple(shape), n, {}))


def hook_dimension(shape):
    n = sum(shape)
    hooks = 1
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            below = sum(1 for rr in range(r + 1, len(shape)) if shape[rr] > c)
            hooks *= (row_len - c) + below
    return math.factorial(n) // hooks


def generators(shape):
    tabs = tableaux(shape)
    index = {tab: j for j, tab in enumerate(tabs)}
    n = sum(shape)
    gens = []
    for i in range(1, n):
        diag = np.empty(len(tabs), dtype=float)
        partner = np.full(len(tabs), -1, dtype=int)
        off = np.zeros(len(tabs), dtype=float)
        for j, tab in enumerate(tabs):
            c_i = tab[i - 1][1] - tab[i - 1][0]
            c_j = tab[i][1] - tab[i][0]
            axial = c_j - c_i
            diag[j] = 1.0 / axial
            if abs(axial) != 1:
                swapped = list(tab)
                swapped[i - 1], swapped[i] = swapped[i], swapped[i - 1]
                jj = index[tuple(swapped)]
                partner[j] = jj
                off[j] = math.sqrt(1.0 - 1.0 / (axial * axial))
        gens.append((diag, partner, off))
    return tabs, gens


def dense_generator(info):
    diag, partner, off = info
    out = np.diag(diag.copy())
    for j, jj in enumerate(partner):
        if jj >= 0:
            out[jj, j] = off[j]
    return out


def right_multiply(m, info):
    diag, partner, off = info
    out = m * diag[np.newaxis, :]
    for j, jj in enumerate(partner):
        if jj >= 0:
            out[:, j] += off[j] * m[:, jj]
    return out


def adjacent_word(p):
    a = list(p)
    sorting_swaps = []
    for target in range(len(a) - 1, -1, -1):
        pos = a.index(target)
        while pos < target:
            a[pos], a[pos + 1] = a[pos + 1], a[pos]
            sorting_swaps.append(pos)
            pos += 1
    assert a == list(range(len(a)))
    return tuple(reversed(sorting_swaps))


def connection_permutations(n, k, r):
    required = set(range(r))
    out = []
    for support in itertools.combinations(range(n), k):
        if not required.issubset(support):
            continue
        anchor = min(support)
        rest = tuple(x for x in support if x != anchor)
        for order in itertools.permutations(rest):
            cyc = (anchor,) + order
            p = list(range(n))
            for a, b in zip(cyc, cyc[1:] + cyc[:1]):
                p[a] = b
            out.append(tuple(p))
    return out


def mu2(n, k, r):
    value = Fraction(math.factorial(k - 2), n - r) * math.comb(n - r, k - r)
    inside = Fraction((k - 1) * (n - k), 1) - Fraction((k - r - 1) * (k - r), n - r - 1)
    return value * inside


def block_sum(shape, words):
    tabs, gen_info = generators(shape)
    d = len(tabs)
    total = np.zeros((d, d), dtype=float)
    for word in words:
        rep = np.eye(d)
        for idx in word:
            rep = right_multiply(rep, gen_info[idx])
        total += rep
    dense = [dense_generator(g) for g in gen_info]
    residuals = []
    eye = np.eye(d)
    for s in dense:
        residuals.append(float(np.max(np.abs(s @ s - eye))))
    for i in range(len(dense) - 1):
        residuals.append(float(np.max(np.abs(dense[i] @ dense[i + 1] @ dense[i] - dense[i + 1] @ dense[i] @ dense[i + 1]))))
    for i in range(len(dense)):
        for j in range(i + 2, len(dense)):
            residuals.append(float(np.max(np.abs(dense[i] @ dense[j] - dense[j] @ dense[i]))))
    content_sum = sum(c - r for r, row_len in enumerate(shape) for c in range(row_len))
    expected_char = Fraction(d * content_sum, math.comb(sum(shape), 2))
    char_error = abs(float(np.trace(dense[0])) - float(expected_char))
    symmetry_error = float(np.max(np.abs(total - total.T)))
    vals = np.linalg.eigvalsh((total + total.T) / 2.0)
    return {
        "dimension": d,
        "hook_dimension": hook_dimension(shape),
        "coxeter_max_residual": max(residuals, default=0.0),
        "transposition_character_expected": str(expected_char),
        "transposition_character_error": char_error,
        "block_symmetry_residual": symmetry_error,
        "eigenvalues": [float(x) for x in vals],
        "top": float(vals[-1]),
    }


def exact_generators(shape):
    tabs = tableaux(shape)
    index = {tab: j for j, tab in enumerate(tabs)}
    n = sum(shape)
    gens = []
    for i in range(1, n):
        diag = []
        partner = []
        off = []
        for j, tab in enumerate(tabs):
            c_i = tab[i - 1][1] - tab[i - 1][0]
            c_j = tab[i][1] - tab[i][0]
            axial = c_j - c_i
            diag.append(Fraction(1, axial))
            if abs(axial) == 1:
                partner.append(-1)
                off.append(Fraction(0))
            else:
                swapped = list(tab)
                swapped[i - 1], swapped[i] = swapped[i], swapped[i - 1]
                partner.append(index[tuple(swapped)])
                off.append(Fraction(1) if axial > 0 else Fraction(axial * axial - 1, axial * axial))
        gens.append((diag, partner, off))
    return tabs, gens


def exact_right_multiply(matrix, info):
    diag, partner, off = info
    rows = len(matrix)
    cols = len(diag)
    out = [[Fraction(0) for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        source = matrix[i]
        target = out[i]
        for j in range(cols):
            value = source[j] * diag[j]
            jj = partner[j]
            if jj >= 0:
                value += source[jj] * off[j]
            target[j] = value
    return out


def exact_dense_generator(info):
    diag, partner, off = info
    d = len(diag)
    out = [[Fraction(0) for _ in range(d)] for _ in range(d)]
    for j in range(d):
        out[j][j] = diag[j]
        if partner[j] >= 0:
            out[partner[j]][j] = off[j]
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in out])


def exact_block_sum(shape, words, threshold):
    tabs, gen_info = exact_generators(shape)
    d = len(tabs)
    total = [[Fraction(0) for _ in range(d)] for _ in range(d)]
    for word in words:
        rep = [[Fraction(int(i == j)) for j in range(d)] for i in range(d)]
        for idx in word:
            rep = exact_right_multiply(rep, gen_info[idx])
        for i in range(d):
            for j in range(d):
                total[i][j] += rep[i][j]
    dense_gens = [exact_dense_generator(g) for g in gen_info]
    eye = sp.eye(d)
    coxeter_ok = all(s * s == eye for s in dense_gens)
    coxeter_ok = coxeter_ok and all(
        dense_gens[i] * dense_gens[i + 1] * dense_gens[i]
        == dense_gens[i + 1] * dense_gens[i] * dense_gens[i + 1]
        for i in range(len(dense_gens) - 1)
    )
    coxeter_ok = coxeter_ok and all(
        dense_gens[i] * dense_gens[j] == dense_gens[j] * dense_gens[i]
        for i in range(len(dense_gens)) for j in range(i + 2, len(dense_gens))
    )
    content_sum = sum(c - r for r, row_len in enumerate(shape) for c in range(row_len))
    expected_char = sp.Rational(d * content_sum, math.comb(sum(shape), 2))
    character_ok = sp.trace(dense_gens[0]) == expected_char
    exact_matrix = sp.Matrix([
        [sp.Rational(x.numerator, x.denominator) for x in row]
        for row in total
    ])
    x = sp.symbols("x")
    poly = sp.Poly(exact_matrix.charpoly(x).as_expr(), x, domain=sp.QQ)
    mu = sp.Rational(threshold.numerator, threshold.denominator)
    linear = sp.Poly(x - mu, x, domain=sp.QQ)
    quotient = poly
    multiplicity = 0
    while quotient.eval(mu) == 0:
        quotient = quotient.exquo(linear)
        multiplicity += 1
    shifted = sp.Poly(quotient.as_expr().subs(x, x + mu), x, domain=sp.QQ)
    roots_strictly_above = int(shifted.count_roots(0, sp.oo))
    coeffs = [str(c) for c in poly.all_coeffs()]
    factorization = str(sp.factor(poly.as_expr()))
    return {
        "coxeter_relations_exact": bool(coxeter_ok),
        "transposition_character_exact": bool(character_ok),
        "characteristic_polynomial_coefficients": coeffs,
        "characteristic_polynomial_factorization": factorization,
        "threshold_multiplicity": multiplicity,
        "roots_strictly_above_threshold": roots_strictly_above,
        "sturm_certified_no_root_above": roots_strictly_above == 0,
    }


def run_case(n, k, r):
    perms = connection_permutations(n, k, r)
    words = [adjacent_word(p) for p in perms]
    degree_expected = math.comb(n - r, k - r) * math.factorial(k - 1)
    target = float(mu2(n, k, r))
    blocks = {}
    failures = []
    for shape in partitions(n):
        row = block_sum(shape, words)
        key = "(" + ",".join(map(str, shape)) + ")"
        row["exact"] = exact_block_sum(shape, words, mu2(n, k, r))
        blocks[key] = row
        if row["dimension"] != row["hook_dimension"]:
            failures.append(f"{key}: tableau count differs from hook dimension")
        if row["coxeter_max_residual"] > TOL:
            failures.append(f"{key}: Coxeter residual {row['coxeter_max_residual']}")
        if row["transposition_character_error"] > TOL:
            failures.append(f"{key}: character residual {row['transposition_character_error']}")
        if row["block_symmetry_residual"] > TOL:
            failures.append(f"{key}: block symmetry residual {row['block_symmetry_residual']}")
        if not row["exact"]["coxeter_relations_exact"]:
            failures.append(f"{key}: exact rational Coxeter check failed")
        if not row["exact"]["transposition_character_exact"]:
            failures.append(f"{key}: exact rational character check failed")
    trivial = f"({n})"
    sign = "(" + ",".join(["1"] * n) + ")"
    standard = f"({n-1},1)"
    sign_standard = "(2," + ",".join(["1"] * (n - 2)) + ")"
    degree_blocks = {trivial} | ({sign} if k % 2 == 1 else set())
    target_blocks = {standard} | ({sign_standard} if k % 2 == 1 else set())
    attaining = [key for key, row in blocks.items() if key not in degree_blocks and abs(row["top"] - target) <= TOL]
    exact_attaining = [
        key for key, row in blocks.items()
        if key not in degree_blocks and row["exact"]["threshold_multiplicity"] > 0
    ]
    target_multiplicity = {
        key: sum(abs(x - target) <= TOL for x in blocks[key]["eigenvalues"])
        for key in sorted(target_blocks)
    }
    exact_target_multiplicity = {
        key: blocks[key]["exact"]["threshold_multiplicity"]
        for key in sorted(target_blocks)
    }
    challengers = [(row["top"], key) for key, row in blocks.items() if key not in degree_blocks | target_blocks]
    challenger_top, challenger_key = max(challengers)
    if len(perms) != degree_expected:
        failures.append(f"connection size {len(perms)} != expected {degree_expected}")
    if set(attaining) != target_blocks:
        failures.append(f"numerical attaining blocks {attaining} != expected {sorted(target_blocks)}")
    if set(exact_attaining) != target_blocks:
        failures.append(f"exact attaining blocks {exact_attaining} != expected {sorted(target_blocks)}")
    for key, row in blocks.items():
        if key in degree_blocks:
            continue
        exact = row["exact"]
        if exact["roots_strictly_above_threshold"] != 0:
            failures.append(f"{key}: exact Sturm count found roots above mu2")
        if key not in target_blocks and exact["threshold_multiplicity"] != 0:
            failures.append(f"{key}: unexpected exact threshold root")
    return {
        "parameters": [n, k, r],
        "connection_size": len(perms),
        "degree_expected": degree_expected,
        "mu2_exact": str(mu2(n, k, r)),
        "mu2_float": target,
        "numerical_attaining_blocks": attaining,
        "exact_attaining_blocks": exact_attaining,
        "target_block_multiplicity": target_multiplicity,
        "exact_target_block_multiplicity": exact_target_multiplicity,
        "closest_non_target_block": challenger_key,
        "closest_non_target_top": challenger_top,
        "numerical_gap_to_mu2": target - challenger_top,
        "blocks": blocks,
        "failures": failures,
    }


def run():
    cases = [run_case(6, 4, 1), run_case(6, 4, 2), run_case(7, 5, 1)]
    failures = [f"{c['parameters']}: {x}" for c in cases for x in c["failures"]]
    result = {
        "status": "PASS_EXACT_FINITE" if not failures else "EXACT_CHECK_FAILED",
        "arithmetic": "Independent rational Young seminormal blocks with exact characteristic polynomials and SymPy Sturm counts; float64 orthogonal blocks retained as a cross-check",
        "tolerance": TOL,
        "dependencies": {"numpy": np.__version__, "sympy": sp.__version__},
        "cases": cases,
        "failures": failures,
        "certification_boundary": "Exact only for the three finite parameter triples listed here. It does not certify the manuscript's general representation-theoretic argument.",
    }
    (ROOT / "results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(result["status"])
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
