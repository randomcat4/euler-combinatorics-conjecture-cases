#!/usr/bin/env python3
"""Exact/numerical checker for the partition-matrix inversion series.

The checker is self-contained and uses the Python standard library only.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter, defaultdict
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "results.json"
MAX_N = 8


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def padd(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def pscale(a, c):
    return trim([c * x for x in a])


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pshift(a, s):
    return (0,) * s + tuple(a)


ZERO = (0,)
ONE = (1,)


def sadd(a, b, nmax):
    return [padd(a[i] if i < len(a) else ZERO, b[i] if i < len(b) else ZERO) for i in range(nmax + 1)]


def smul(a, b, nmax):
    out = [ZERO for _ in range(nmax + 1)]
    for i in range(min(len(a), nmax + 1)):
        for j in range(min(len(b), nmax + 1 - i)):
            out[i + j] = padd(out[i + j], pmul(a[i], b[j]))
    return out


def sinv(a, nmax):
    assert a[0] == ONE
    out = [ZERO for _ in range(nmax + 1)]
    out[0] = ONE
    for n in range(1, nmax + 1):
        total = ZERO
        for i in range(1, min(n, len(a) - 1) + 1):
            total = padd(total, pmul(a[i], out[n - i]))
        out[n] = pscale(total, -1)
    return out


def compositions(n, parts):
    if parts == 1:
        yield (n,)
        return
    for first in range(1, n - parts + 2):
        for rest in compositions(n - first, parts - 1):
            yield (first,) + rest


def word_inv(word):
    return sum(word[i] > word[j] for i in range(len(word)) for j in range(i + 1, len(word)))


def direct_partition_matrix_data(n, weight_families):
    inv_counter = Counter()
    weighted = {name: Counter() for name in weight_families}
    profile_counter = Counter()
    object_count = 0
    for dim in range(1, n + 1):
        for lengths in compositions(n, dim):
            alphabets = [range(col + 1) for col, length in enumerate(lengths) for _ in range(length)]
            for rows in itertools.product(*alphabets):
                if set(rows) != set(range(dim)):
                    continue
                object_count += 1
                pos = 0
                inv = 0
                cell_sizes = []
                for col, length in enumerate(lengths):
                    word = rows[pos : pos + length]
                    pos += length
                    inv += word_inv(word)
                    counts = Counter(word)
                    cell_sizes.extend(counts.values())
                profile = tuple(sorted(Counter(cell_sizes).items()))
                inv_counter[inv] += 1
                profile_counter[inv, profile] += 1
                for name, weights in weight_families.items():
                    w = math.prod(weights[size] for size in cell_sizes)
                    weighted[name][inv] += w
    return object_count, inv_counter, weighted, profile_counter


def column_series(k, nmax, weights=None):
    """R_k coefficients via exact DP over word letter-count states."""
    states = {(0,) * k: ONE}
    answer = [ONE]
    for m in range(1, nmax + 1):
        nxt = {}
        for counts, poly in states.items():
            for x in range(k):
                increment = sum(counts[x + 1 :])
                new_counts = list(counts)
                new_counts[x] += 1
                key = tuple(new_counts)
                nxt[key] = padd(nxt.get(key, ZERO), pshift(poly, increment))
        states = nxt
        total = ZERO
        for counts, poly in states.items():
            content_weight = 1 if weights is None else math.prod(weights[c] for c in counts)
            total = padd(total, pscale(poly, content_weight))
        answer.append(total)
    return answer


def product_formula(nmax, weights=None):
    total = [ZERO for _ in range(nmax + 1)]
    running = [ONE] + [ZERO for _ in range(nmax)]
    for k in range(1, nmax + 1):
        r = column_series(k, nmax, weights)
        rinv = sinv(r, nmax)
        factor = [pscale(x, -1) for x in rinv]
        factor[0] = padd(ONE, factor[0])
        running = smul(running, factor, nmax)
        total = sadd(total, running, nmax)
    return total


def peval(poly, q):
    total = type(q)(0)
    power = type(q)(1)
    for coeff in poly:
        total += coeff * power
        power *= q
    return total


def qpoch_fraction(q: Fraction, m: int) -> Fraction:
    out = Fraction(1)
    for j in range(1, m + 1):
        out *= 1 - q**j
    return out


def exact_borel_checks():
    checks = []
    for q in (Fraction(1, 2), Fraction(2, 3)):
        for k in range(1, 6):
            r = column_series(k, 8)
            left = [peval(poly, q) / qpoch_fraction(q, m) for m, poly in enumerate(r)]
            e = [Fraction(1, 1) / qpoch_fraction(q, m) for m in range(9)]
            right = [Fraction(1)] + [Fraction(0)] * 8
            for _ in range(k):
                conv = [Fraction(0)] * 9
                for i, a in enumerate(right):
                    for j, b in enumerate(e[: 9 - i]):
                        conv[i + j] += a * b
                right = conv
            assert left == right
            checks.append({"q": str(q), "k": k, "max_coefficient": 8, "equal": True})
    return checks


def qpoch_decimal(a: Decimal, q: Decimal, terms: int) -> Decimal:
    out = Decimal(1)
    power = Decimal(1)
    for _ in range(terms):
        out *= 1 - a * power
        power *= q
    return out


def numeric_word_series(k: int, q: Decimal, t: Decimal, max_m: int) -> Decimal:
    states = {(0,) * k: Decimal(1)}
    total = Decimal(1)
    tpower = Decimal(1)
    qpowers = [q**j for j in range(max_m * max_m + 1)]
    for _m in range(1, max_m + 1):
        nxt = defaultdict(Decimal)
        for counts, value in states.items():
            for x in range(k):
                increment = sum(counts[x + 1 :])
                new_counts = list(counts)
                new_counts[x] += 1
                nxt[tuple(new_counts)] += value * qpowers[increment]
        states = dict(nxt)
        tpower *= t
        total += sum(states.values(), Decimal(0)) * tpower
    return total


def hypergeometric_numeric_checks():
    getcontext().prec = 70
    cases = [(Decimal("0.2"), Decimal("0.03")), (Decimal("0.45"), Decimal("0.015"))]
    out = []
    max_m = 32
    product_terms = 400
    for q, t in cases:
        qinf = qpoch_decimal(q, q, product_terms)
        tinf = qpoch_decimal(t, q, product_terms)
        for k in range(1, 5):
            hyper_sum = Decimal(0)
            tq = Decimal(1)
            qq = Decimal(1)
            qpower = Decimal(1)
            for r in range(product_terms):
                if r > 0:
                    tq *= 1 - t * q ** (r - 1)
                    qq *= 1 - q**r
                    qpower *= q
                hyper_sum += (tq**k) * qpower / qq
            hyper_value = qinf * hyper_sum / (tinf**k)
            word_value = numeric_word_series(k, q, t, max_m)
            difference = abs(hyper_value - word_value)
            kt = Decimal(k) * t
            word_tail_bound = kt ** (max_m + 1) / (1 - kt)
            assert difference <= word_tail_bound + Decimal("1e-55")
            out.append(
                {
                    "q": str(q),
                    "t": str(t),
                    "k": k,
                    "word_truncation_degree": max_m,
                    "hypergeometric_terms": product_terms,
                    "absolute_difference": str(difference),
                    "word_tail_bound": str(word_tail_bound),
                    "within_bound": True,
                }
            )
    return out


def main():
    weight_families = {
        "affine": {r: 2 * r + 1 for r in range(MAX_N + 1)},
        "with_zero": {r: (0 if r == 3 else r + 1) for r in range(MAX_N + 1)},
        "signed": {r: (-1) ** r * (r * r + 1) for r in range(MAX_N + 1)},
    }
    for weights in weight_families.values():
        weights[0] = 1

    direct = []
    direct_unweighted = [ZERO for _ in range(MAX_N + 1)]
    direct_weighted = {name: [ZERO for _ in range(MAX_N + 1)] for name in weight_families}
    for n in range(1, MAX_N + 1):
        count, invs, weighted, profiles = direct_partition_matrix_data(n, weight_families)
        assert count == math.factorial(n)
        p = trim([invs[i] for i in range(max(invs) + 1)])
        direct_unweighted[n] = p
        weighted_rows = {}
        for name, counter in weighted.items():
            wp = trim([counter[i] for i in range(max(counter) + 1)])
            direct_weighted[name][n] = wp
            weighted_rows[name] = list(wp)
        direct.append(
            {
                "n": n,
                "partition_matrices": count,
                "S_n_q_coefficients_low_to_high": list(p),
                "cell_profile_terms": len(profiles),
                "weighted_coefficients": weighted_rows,
            }
        )

    formula = product_formula(MAX_N)
    assert formula[1:] == direct_unweighted[1:]
    for name, weights in weight_families.items():
        refined_formula = product_formula(MAX_N, weights)
        assert refined_formula[1:] == direct_weighted[name][1:]

    # Independent endpoint checks from the displayed q=0 and q=1 forms.
    assert [sum(p) for p in formula[1:]] == [math.factorial(n) for n in range(1, MAX_N + 1)]
    q0_coeffs = [p[0] for p in formula]
    q0_expected = [0] * (MAX_N + 1)
    running = [1] + [0] * MAX_N
    for k in range(1, MAX_N + 1):
        factor = [0] * (MAX_N + 1)
        for j in range(1, k + 1):
            factor[j] = -((-1) ** j) * math.comb(k, j)
        conv = [0] * (MAX_N + 1)
        for i, a in enumerate(running):
            for j, b in enumerate(factor[: MAX_N + 1 - i]):
                conv[i + j] += a * b
        running = conv
        q0_expected = [a + b for a, b in zip(q0_expected, running)]
    assert q0_coeffs == q0_expected

    result = {
        "problem": "partition-matrix-q-sum-product",
        "status": "PASS_FINITE_EXACT_AND_NUMERIC",
        "claim_scope": "partition-matrix inversion sum-product, q-Borel transform, and cell-size refinement",
        "coverage": {
            "coefficient_degree_n": [1, MAX_N],
            "direct_matrix_enumeration": True,
            "exact_column_word_dynamic_program": True,
            "cell_weight_families": list(weight_families),
            "q_borel_exact_rational_checks": "q in {1/2,2/3}, k<=5, coefficients through 8",
            "hypergeometric_numeric_checks": "two (q,t) points, k<=4",
        },
        "per_n": direct,
        "q0_coefficients_n0_to_n8": q0_coeffs,
        "q1_coefficients_n1_to_n8": [sum(p) for p in formula[1:]],
        "exact_q_borel": exact_borel_checks(),
        "hypergeometric_numeric": hypergeometric_numeric_checks(),
    }
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"problem": result["problem"], "status": result["status"]}, ensure_ascii=False))
    print("S_n(1), n=1..8", result["q1_coefficients_n1_to_n8"])


if __name__ == "__main__":
    main()
