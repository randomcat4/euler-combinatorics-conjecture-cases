from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
TOL = 1e-9


def edge_list(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


def adjacency_from_mask(n, mask):
    adj = [0] * n
    for bit, (i, j) in enumerate(edge_list(n)):
        if (mask >> bit) & 1:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
    return adj


def has_k33plus(adj):
    n = len(adj)
    for triple in itertools.combinations(range(n), 3):
        if not any((adj[a] >> b) & 1 for a, b in itertools.combinations(triple, 2)):
            continue
        common = (1 << n) - 1
        for v in triple:
            common &= adj[v]
        for v in triple:
            common &= ~(1 << v)
        if common.bit_count() >= 3:
            return True
    return False


def has_k33(adj):
    n = len(adj)
    for triple in itertools.combinations(range(n), 3):
        common = (1 << n) - 1
        for v in triple:
            common &= adj[v]
        for v in triple:
            common &= ~(1 << v)
        if common.bit_count() >= 3:
            return True
    return False


def q_index(adj):
    n = len(adj)
    q = np.zeros((n, n), dtype=float)
    for i in range(n):
        q[i, i] = adj[i].bit_count()
        for j in range(n):
            if (adj[i] >> j) & 1:
                q[i, j] = 1.0
    return float(np.linalg.eigvalsh(q)[-1])


def graph_mask(adj):
    out = 0
    for bit, (i, j) in enumerate(edge_list(len(adj))):
        out |= ((adj[i] >> j) & 1) << bit
    return out


def relabel_mask(adj, perm):
    n = len(adj)
    out = [0] * n
    for old_i in range(n):
        for old_j in range(old_i + 1, n):
            if (adj[old_i] >> old_j) & 1:
                i, j = perm[old_i], perm[old_j]
                out[i] |= 1 << j
                out[j] |= 1 << i
    return graph_mask(out)


def canonical_mask(adj):
    return min(relabel_mask(adj, perm) for perm in itertools.permutations(range(len(adj))))


def join_k2(r_adj):
    m = len(r_adj)
    n = m + 2
    adj = [0] * n
    adj[0] = ((1 << n) - 1) ^ 1
    adj[1] = ((1 << n) - 1) ^ 2
    for i in range(m):
        v = i + 2
        adj[v] |= 3
        for j in range(m):
            if (r_adj[i] >> j) & 1:
                adj[v] |= 1 << (j + 2)
    return adj


def components(adj):
    unseen = set(range(len(adj)))
    out = []
    while unseen:
        root = next(iter(unseen))
        stack = [root]
        unseen.remove(root)
        comp = []
        while stack:
            v = stack.pop()
            comp.append(v)
            for w in range(len(adj)):
                if w in unseen and ((adj[v] >> w) & 1):
                    unseen.remove(w)
                    stack.append(w)
        out.append(comp)
    return out


def class_condition(r_adj):
    if max((x.bit_count() for x in r_adj), default=0) > 2:
        return False
    for comp in components(r_adj):
        if len(comp) == 4 and all(sum((r_adj[v] >> w) & 1 for w in comp) == 2 for v in comp):
            return False
    return True


def build_h():
    r = [0] * 4
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        r[i] |= 1 << j
        r[j] |= 1 << i
    return join_k2(r)


def cycle_graph(m):
    adj = [0] * m
    for i in range(m):
        j = (i + 1) % m
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    return adj


def run():
    failures = []
    h = build_h()
    h_canon = canonical_mask(h)
    q_h = q_index(h)
    expected_h = 5 + math.sqrt(13)
    if abs(q_h - expected_h) > TOL:
        failures.append(f"H q-index {q_h} != 5+sqrt(13)")

    feasible = []
    for mask in range(1 << math.comb(6, 2)):
        adj = adjacency_from_mask(6, mask)
        if not has_k33plus(adj):
            feasible.append((q_index(adj), adj))
    max_q = max(x for x, _ in feasible)
    maximizers = [adj for x, adj in feasible if abs(x - max_q) <= TOL]
    canonical_types = {canonical_mask(adj) for adj in maximizers}
    if abs(max_q - expected_h) > TOL:
        failures.append(f"six-vertex maximum {max_q} != 5+sqrt(13)")
    if canonical_types != {h_canon}:
        failures.append(f"six-vertex maximizers have canonical types {canonical_types}, expected H only")
    if len(maximizers) != 60:
        failures.append(f"six-vertex labeled maximizer count {len(maximizers)} != 60")
    below = max(x for x, _ in feasible if x < max_q - TOL)

    c4 = cycle_graph(4)
    k2c4 = join_k2(c4)
    i2c4 = [0] * 6
    for i in range(2):
        for j in range(2, 6):
            i2c4[i] |= 1 << j
            i2c4[j] |= 1 << i
    for i in range(4):
        for j in range(i + 1, 4):
            if (c4[i] >> j) & 1:
                i2c4[i + 2] |= 1 << (j + 2)
                i2c4[j + 2] |= 1 << (i + 2)
    if not has_k33plus(k2c4):
        failures.append("K2 join C4 was not detected as forbidden")
    if has_k33plus(i2c4) or abs(q_index(i2c4) - 8.0) > TOL:
        failures.append("I2 join C4 feasibility/q=8 check failed")

    class_rows = {}
    for n in range(5, 9):
        m = n - 2
        total = 1 << math.comb(m, 2)
        feasible_count = 0
        k33_free_count = 0
        equality_count = 0
        class_max = -1.0
        for mask in range(total):
            r_adj = adjacency_from_mask(m, mask)
            g = join_k2(r_adj)
            forbidden = has_k33plus(g)
            criterion = class_condition(r_adj)
            if (not forbidden) != criterion:
                failures.append(f"n={n}, R-mask={mask}: class criterion mismatch")
                break
            if criterion:
                feasible_count += 1
                if not has_k33(g):
                    k33_free_count += 1
                q = q_index(g)
                class_max = max(class_max, q)
                is_2regular = all(x.bit_count() == 2 for x in r_adj)
                q_star = (n + 6 + math.sqrt(n * n - 4 * n + 20)) / 2
                if n != 6:
                    if q > q_star + TOL:
                        failures.append(f"n={n}, R-mask={mask}: q exceeds q_star")
                    if (abs(q - q_star) <= TOL) != is_2regular:
                        failures.append(f"n={n}, R-mask={mask}: equality classification mismatch")
                if is_2regular:
                    equality_count += 1
        if k33_free_count != feasible_count:
            failures.append(f"n={n}: not every feasible K2 join R is K33-free")
        q_star = (n + 6 + math.sqrt(n * n - 4 * n + 20)) / 2
        if n >= 7 and abs(class_max - q_star) > TOL:
            failures.append(f"n={n}: class maximum {class_max} != q_star {q_star}")
        class_rows[str(n)] = {
            "residual_graphs_checked": total,
            "feasible": feasible_count,
            "also_K33_free": k33_free_count,
            "two_regular_equality_residuals": equality_count,
            "maximum_q": class_max,
            "q_star": q_star,
        }

    result = {
        "status": "PASS_FINITE" if not failures else "FAIL",
        "tolerance": TOL,
        "dependencies": {"numpy": np.__version__},
        "six_vertex": {
            "all_labeled_graphs": 1 << 15,
            "feasible_graphs": len(feasible),
            "maximum_q": max_q,
            "expected_q": expected_h,
            "labeled_maximizers": len(maximizers),
            "maximizer_isomorphism_types": len(canonical_types),
            "next_lower_q": below,
            "gap": max_q - below,
            "K2_join_C4_forbidden": has_k33plus(k2c4),
            "I2_join_C4_forbidden": has_k33plus(i2c4),
            "I2_join_C4_q": q_index(i2c4),
        },
        "two_universal_class": class_rows,
        "failures": failures,
        "limitation": "The n=6 search is exhaustive over all labeled graphs. The K2-join-R classification is exhaustive only for 5 <= n <= 8. Spectral comparisons use float64 eigensolvers.",
    }
    (ROOT / "results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(result["status"])
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
