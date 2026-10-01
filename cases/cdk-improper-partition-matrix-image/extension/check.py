from __future__ import annotations

import itertools
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MAX_N = 8


def compositions(n: int):
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        for tail in compositions(n - first):
            yield (first,) + tail


def poly_add(a, b, scale=1):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += scale * x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_pow(a, exponent):
    out = [1]
    base = a[:]
    while exponent:
        if exponent & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        exponent //= 2
    return out


def ie_polynomial(m):
    d = len(m)
    total = [0]
    for mask in range(1 << d):
        sign = -1 if mask.bit_count() & 1 else 1
        term = [1]
        for c, mc in enumerate(m, start=1):
            k = sum(1 for row in range(1, c + 1) if not (mask >> (row - 1)) & 1)
            if mc & 1:
                term = [x * k for x in term]
            pair_poly = [k, k * (k - 1) // 2]
            term = poly_mul(term, poly_pow(pair_poly, mc // 2))
        total = poly_add(total, term, sign)
    return total


def decode(e):
    n = len(e)
    values = sorted(set(e))
    assert values and values[0] == 0
    endpoints = values + [n]
    d = len(values)
    row_of_value = {v: i + 1 for i, v in enumerate(values)}
    rows = [row_of_value[x] for x in e]
    cols = []
    for label in range(1, n + 1):
        c = next(c for c in range(1, d + 1) if endpoints[c - 1] < label <= endpoints[c])
        cols.append(c)
    m = tuple(endpoints[c] - endpoints[c - 1] for c in range(1, d + 1))
    words = []
    record = []
    p = q = unequal = 0
    for c in range(1, d + 1):
        lo, hi = endpoints[c - 1], endpoints[c]
        word = tuple(rows[lo:hi])
        words.append(word)
        rec = []
        for j in range(0, len(word) - 1, 2):
            x, y = word[j], word[j + 1]
            rec.append((min(x, y), max(x, y)))
            if x < y:
                p += 1
                unequal += 1
            elif x > y:
                q += 1
                unequal += 1
        if len(word) & 1:
            rec.append((word[-1],))
        record.append(tuple(rec))
    cell = tuple(
        tuple(sum(1 for rr, cc in zip(rows, cols) if rr == r and cc == c) for c in range(1, d + 1))
        for r in range(1, d + 1)
    )
    recovered = tuple(endpoints[r - 1] for r in rows)
    return {
        "m": m,
        "rows": tuple(rows),
        "cols": tuple(cols),
        "words": tuple(words),
        "record": tuple(record),
        "p": p,
        "q": q,
        "d": unequal,
        "cell": cell,
        "improper": unequal == 0,
        "recovered": recovered,
    }


def run():
    failures = []
    summary = {}
    for n in range(1, MAX_N + 1):
        groups = defaultdict(list)
        matrix_count = 0
        improper_count = 0
        for e in itertools.product(*[range(i) for i in range(1, n + 1)]):
            obj = decode(e)
            matrix_count += 1
            if obj["recovered"] != e:
                failures.append(f"n={n}: CDK round trip failed for {e}")
            if obj["improper"] != all(
                word[j] == word[j + 1]
                for word in obj["words"]
                for j in range(0, len(word) - 1, 2)
            ):
                failures.append(f"n={n}: improper criterion failed for {e}")
            improper_count += int(obj["improper"])
            groups[(obj["m"], obj["record"])].append(obj)

        if matrix_count != math.factorial(n):
            failures.append(f"n={n}: got {matrix_count} inversion sequences, expected {math.factorial(n)}")

        hm = defaultdict(Counter)
        for (m, record), orbit in groups.items():
            ds = {x["d"] for x in orbit}
            cells = {x["cell"] for x in orbit}
            if len(ds) != 1:
                failures.append(f"n={n}, m={m}: unequal-pair count varies in an orbit")
                continue
            d = next(iter(ds))
            if len(orbit) != 2 ** d:
                failures.append(f"n={n}, m={m}: orbit size {len(orbit)} != 2^{d}")
            if len(cells) != 1:
                failures.append(f"n={n}, m={m}: cell cardinalities changed in an orbit")
            dist = Counter((x["p"], x["q"]) for x in orbit)
            expected = Counter({(r, d - r): math.comb(d, r) for r in range(d + 1)})
            if dist != expected:
                failures.append(f"n={n}, m={m}: orientation distribution mismatch")
            if sum(x["q"] == 0 for x in orbit) != 1 or sum(x["p"] == 0 for x in orbit) != 1:
                failures.append(f"n={n}, m={m}: one-sided representative is not unique")
            hm[m][d] += 1

        aggregate = Counter()
        for m in compositions(n):
            brute = [hm[m][i] for i in range(max(hm[m].keys(), default=0) + 1)] or [0]
            while len(brute) > 1 and brute[-1] == 0:
                brute.pop()
            formula = ie_polynomial(m)
            if brute != formula:
                failures.append(f"n={n}, m={m}: inclusion-exclusion {formula} != brute {brute}")
            for d, count in hm[m].items():
                aggregate[d] += count

        total_from_orbits = sum(count * (2 ** d) for d, count in aggregate.items())
        one_sided = sum(aggregate.values())
        if total_from_orbits != math.factorial(n):
            failures.append(f"n={n}: H_n(2)={total_from_orbits} != {n}!")
        if aggregate[0] != improper_count:
            failures.append(f"n={n}: H_n(0)={aggregate[0]} != improper count {improper_count}")
        summary[str(n)] = {
            "partition_matrices": matrix_count,
            "orbit_polynomial_coefficients": [aggregate[i] for i in range(max(aggregate) + 1)],
            "orbits": one_sided,
            "improper_matrices": improper_count,
            "H_n_at_2": total_from_orbits,
        }

    result = {
        "status": "PASS_FINITE" if not failures else "FAIL",
        "scope": {"n_min": 1, "n_max": MAX_N, "arithmetic": "exact integers"},
        "checks": [
            "CDK inverse construction and round trip for every inversion sequence",
            "matched-pair criterion for improper matrices",
            "complete orbit records, 2^d sizes, cell-cardinality invariance, and binomial orientation distribution",
            "inclusion-exclusion polynomial for every positive composition",
            "H_n(2)=n! and H_n(0)=improper count",
        ],
        "summary": summary,
        "failures": failures,
        "limitation": "Finite exhaustive verification through n=8; it is not a proof for arbitrary n.",
    }
    (ROOT / "results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(result["status"])
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
