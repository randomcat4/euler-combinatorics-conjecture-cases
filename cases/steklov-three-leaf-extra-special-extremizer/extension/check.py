from __future__ import annotations

import json
import math
from pathlib import Path

import networkx as nx
import numpy as np


ROOT = Path(__file__).resolve().parent
TOL = 2e-8
MAX_VERTICES = 12


def matching_number(tree):
    root = next(iter(tree.nodes))

    def visit(v, parent):
        child_states = [visit(w, v) for w in tree.neighbors(v) if w != parent]
        matched_to_parent = sum(free for free, _ in child_states)
        free = matched_to_parent
        for i, (child_free, child_parent) in enumerate(child_states):
            candidate = 1 + child_parent + sum(x[0] for j, x in enumerate(child_states) if j != i)
            free = max(free, candidate)
        return free, matched_to_parent

    return visit(root, None)[0]


def zero_sum_basis(b):
    a = np.zeros((b, b - 1), dtype=float)
    for i in range(b - 1):
        a[i, i] = 1.0
        a[-1, i] = -1.0
    q, _ = np.linalg.qr(a)
    return q


def steklov_data(tree):
    nodes = list(tree.nodes)
    index = {v: i for i, v in enumerate(nodes)}
    leaves = [v for v in nodes if tree.degree(v) == 1]
    interior = [v for v in nodes if tree.degree(v) != 1]
    n = len(nodes)
    lap = np.zeros((n, n), dtype=float)
    for u, v in tree.edges:
        i, j = index[u], index[v]
        lap[i, i] += 1
        lap[j, j] += 1
        lap[i, j] -= 1
        lap[j, i] -= 1
    bi = [index[v] for v in leaves]
    ii = [index[v] for v in interior]
    lbb = lap[np.ix_(bi, bi)]
    if ii:
        lbi = lap[np.ix_(bi, ii)]
        lii = lap[np.ix_(ii, ii)]
        lam = lbb - lbi @ np.linalg.solve(lii, lbi.T)
    else:
        lam = lbb
    eig = np.linalg.eigvalsh((lam + lam.T) / 2)
    sigma2 = float(eig[1])
    b = len(leaves)
    q = zero_sum_basis(b)
    pinv = np.linalg.pinv(lam, rcond=1e-13)
    inverse_top = float(np.linalg.eigvalsh(q.T @ pinv @ q)[-1])

    leaf_index = {v: i for i, v in enumerate(leaves)}
    current_form = np.zeros((b, b), dtype=float)
    for u, v in tree.edges:
        seen = {u}
        stack = [u]
        while stack:
            x = stack.pop()
            for y in tree.neighbors(x):
                if (x == u and y == v) or (x == v and y == u):
                    continue
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        indicator = np.zeros(b)
        for x in seen:
            if x in leaf_index:
                indicator[leaf_index[x]] = 1.0
        current_form += np.outer(indicator, indicator)
    current_top = float(np.linalg.eigvalsh(q.T @ current_form @ q)[-1])
    return {
        "leaves": leaves,
        "sigma2": sigma2,
        "inverse_schur_top": inverse_top,
        "inverse_current_top": current_top,
        "schur_current_error": abs(inverse_top - current_top),
        "reciprocal_error": abs(1.0 / sigma2 - current_top),
    }


def add_arm(tree, center, length, next_node):
    cur = center
    for _ in range(length):
        tree.add_edge(cur, next_node)
        cur = next_node
        next_node += 1
    return next_node


def extra_special(b, r):
    if b == 2:
        return nx.path_graph(4 * r + 4)
    p = 2 * r
    tree = nx.Graph()
    tree.add_node(0)
    nxt = 1
    for length in [p + 2, p + 1] + [p] * (b - 2):
        nxt = add_arm(tree, 0, length, nxt)
    return tree


def central_split(s, t, r):
    p = 2 * r
    tree = nx.Graph()
    tree.add_edge(0, 1)
    nxt = 2
    for side, count in [(0, s), (1, t)]:
        for j in range(count):
            nxt = add_arm(tree, side, p + 1 if j == 0 else p, nxt)
    return tree


def c_b(b):
    return (3 * (b - 1) + math.sqrt(b * b - 2 * b + 9)) / (2 * b)


def lambda_split(s, t):
    b = s + t
    gram = np.array([[b - 1, 1, t], [1, b - 1, s], [t, s, s * t]], dtype=float) / b
    return float(np.linalg.eigvalsh(gram)[-1])


def run():
    failures = []
    tree_counts = {}
    eligible = {2: [], 3: [], 4: []}
    equality = {2: [], 3: [], 4: []}
    max_errors = {"schur_current": 0.0, "reciprocal": 0.0}

    for n in range(2, MAX_VERTICES + 1):
        count = 0
        for tree in nx.generators.nonisomorphic_trees(n):
            count += 1
            b = sum(tree.degree(v) == 1 for v in tree.nodes)
            if b not in eligible:
                continue
            matching = matching_number(tree)
            threshold = b + 2
            if matching < threshold:
                continue
            spec = steklov_data(tree)
            max_errors["schur_current"] = max(max_errors["schur_current"], spec["schur_current_error"])
            max_errors["reciprocal"] = max(max_errors["reciprocal"], spec["reciprocal_error"])
            bound = 1.0 / (2.0 + c_b(b))
            eligible[b].append({"vertices": n, "matching": matching, "sigma2": spec["sigma2"]})
            if spec["sigma2"] > bound + TOL:
                failures.append(f"n={n}, b={b}: sigma2 {spec['sigma2']} exceeds {bound}")
            if abs(spec["sigma2"] - bound) <= TOL:
                candidate = extra_special(b, 1)
                if not nx.is_isomorphic(tree, candidate):
                    failures.append(f"n={n}, b={b}: unexpected equality tree")
                equality[b].append(n)
        tree_counts[str(n)] = count

    for b in (2, 3, 4):
        candidate = extra_special(b, 1)
        expected_n = candidate.number_of_nodes()
        if equality[b] != [expected_n]:
            failures.append(f"b={b}: equality orders {equality[b]} != [{expected_n}]")

    constructed = []
    for b in range(2, 7):
        for r in range(1, 4):
            es = extra_special(b, r)
            data = steklov_data(es)
            matching = matching_number(es)
            expected = 1.0 / (2 * r + c_b(b))
            if matching != b * r + 2 or abs(data["sigma2"] - expected) > TOL:
                failures.append(f"extra-special b={b}, r={r} failed")
            constructed.append({
                "kind": "extra_special",
                "b": b,
                "r": r,
                "vertices": es.number_of_nodes(),
                "matching": matching,
                "sigma2": data["sigma2"],
                "formula": expected,
                "error": abs(data["sigma2"] - expected),
            })

    split_rows = []
    for b in range(2, 7):
        for r in range(1, 4):
            for s in range(1, b):
                t = b - s
                tree = central_split(s, t, r)
                data = steklov_data(tree)
                lam = lambda_split(s, t)
                expected = 1.0 / (2 * r + lam)
                matching = matching_number(tree)
                diameter = nx.diameter(tree)
                row = {
                    "b": b,
                    "r": r,
                    "s": s,
                    "t": t,
                    "vertices": tree.number_of_nodes(),
                    "matching": matching,
                    "diameter": diameter,
                    "lambda": lam,
                    "sigma2": data["sigma2"],
                    "formula": expected,
                    "error": abs(data["sigma2"] - expected),
                    "schur_current_error": data["schur_current_error"],
                }
                split_rows.append(row)
                if matching != b * r + 2 or diameter != 4 * r + 3 or row["error"] > TOL:
                    failures.append(f"central split b={b}, r={r}, s={s}, t={t} failed")
                max_errors["schur_current"] = max(max_errors["schur_current"], data["schur_current_error"])
                max_errors["reciprocal"] = max(max_errors["reciprocal"], data["reciprocal_error"])

    result = {
        "status": "PASS_FINITE" if not failures else "FAIL",
        "tolerance": TOL,
        "dependencies": {"numpy": np.__version__, "networkx": nx.__version__},
        "tree_enumeration": {
            "max_vertices": MAX_VERTICES,
            "unlabeled_tree_counts": tree_counts,
            "eligible_counts": {str(b): len(rows) for b, rows in eligible.items()},
            "equality_orders": {str(b): rows for b, rows in equality.items()},
            "eligible_by_b": {str(b): rows for b, rows in eligible.items()},
        },
        "constructed_extra_special": constructed,
        "central_split_checks": split_rows,
        "max_cross_check_errors": max_errors,
        "failures": failures,
        "limitation": "Complete only for unlabeled trees with at most 12 vertices (r=1 threshold tests for b=2,3,4). Constructed formula checks cover b=2..6 and r=1..3 but do not enumerate all trees at those larger sizes.",
    }
    (ROOT / "results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(result["status"])
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
