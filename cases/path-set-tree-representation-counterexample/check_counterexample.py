#!/usr/bin/env python3
"""Verify the path-set tree representation counterexample."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent


def mask_from_vertices(items: list[int]) -> int:
    mask = 0
    for item in items:
        mask |= 1 << item
    return mask


def vertices(mask: int, n: int) -> list[int]:
    return [index for index in range(n) if mask & (1 << index)]


def is_interval(mask: int, order: list[int]) -> bool:
    positions = [index for index, value in enumerate(order) if mask & (1 << value)]
    if not positions:
        return True
    return positions[-1] - positions[0] + 1 == len(positions)


def pairwise_intersecting(combo: tuple[int, ...]) -> bool:
    return all(a & b for a, b in itertools.combinations(combo, 2))


def finite_helly_summary(family: list[int], n: int) -> dict[str, Any]:
    universe = (1 << n) - 1
    nonempty_count = 0
    pairwise_count = 0
    violations: list[list[int]] = []

    for size in range(1, len(family) + 1):
        for combo in itertools.combinations(family, size):
            nonempty_count += 1
            if not pairwise_intersecting(combo):
                continue
            pairwise_count += 1
            total = universe
            for mask in combo:
                total &= mask
            if total == 0:
                violations.append(list(combo))

    return {
        "ok": not violations,
        "nonempty_subfamilies_checked": nonempty_count,
        "pairwise_intersecting_subfamilies": pairwise_count,
        "violations": violations,
    }


def graph_edges(family: list[int]) -> set[tuple[int, int]]:
    edges: set[tuple[int, int]] = set()
    for i, a in enumerate(family):
        for j in range(i + 1, len(family)):
            if a & family[j]:
                edges.add((i, j))
    return edges


def adjacent(edges: set[tuple[int, int]], a: int, b: int) -> bool:
    return (min(a, b), max(a, b)) in edges


def is_clique(edges: set[tuple[int, int]], nodes: tuple[int, ...]) -> bool:
    return all(adjacent(edges, a, b) for a, b in itertools.combinations(nodes, 2))


def maximal_cliques(family: list[int]) -> list[list[int]]:
    edges = graph_edges(family)
    cliques: list[tuple[int, ...]] = []
    nodes = tuple(range(len(family)))
    for size in range(1, len(nodes) + 1):
        for combo in itertools.combinations(nodes, size):
            if is_clique(edges, combo):
                cliques.append(combo)
    maximal = [
        list(clique)
        for clique in cliques
        if not any(set(clique) < set(other) for other in cliques)
    ]
    return maximal


def is_perfect_elimination_order(order: tuple[int, ...], edges: set[tuple[int, int]]) -> bool:
    position = {node: index for index, node in enumerate(order)}
    for node in order:
        later = tuple(
            other
            for other in order
            if position[other] > position[node] and adjacent(edges, node, other)
        )
        if not is_clique(edges, later):
            return False
    return True


def chordal_summary(family: list[int]) -> dict[str, Any]:
    edges = graph_edges(family)
    for order in itertools.permutations(range(len(family))):
        if is_perfect_elimination_order(order, edges):
            return {
                "ok": True,
                "edge_count": len(edges),
                "missing_edges": [
                    [i, j]
                    for i, j in itertools.combinations(range(len(family)), 2)
                    if not adjacent(edges, i, j)
                ],
                "perfect_elimination_order": list(order),
            }
    return {"ok": False, "edge_count": len(edges), "missing_edges": [], "perfect_elimination_order": []}


def local_interval_summary(
    family: list[int], orders: dict[str, list[int]], n: int
) -> dict[str, Any]:
    failures: list[dict[str, Any]] = []
    normalized: dict[str, list[int]] = {}
    for s0 in family:
        key = str(s0)
        order = list(orders[key])
        if sorted(order) != vertices(s0, n):
            failures.append({"s0": s0, "reason": "order is not a permutation of S0"})
            continue
        normalized[key] = order
        for member in family:
            trace = member & s0
            if not is_interval(trace, order):
                failures.append({"s0": s0, "member": member, "trace": trace, "order": order})
    return {"ok": not failures, "orders": normalized, "failures": failures}


def prufer_trees(n: int) -> list[tuple[tuple[int, int], ...]]:
    if n == 1:
        return [tuple()]
    trees: list[tuple[tuple[int, int], ...]] = []
    for code in itertools.product(range(n), repeat=n - 2):
        degree = [1] * n
        for item in code:
            degree[item] += 1
        edges: list[tuple[int, int]] = []
        remaining = list(code)
        for item in remaining:
            leaf = min(index for index, value in enumerate(degree) if value == 1)
            edges.append((min(leaf, item), max(leaf, item)))
            degree[leaf] -= 1
            degree[item] -= 1
        leaves = [index for index, value in enumerate(degree) if value == 1]
        a, b = leaves
        edges.append((min(a, b), max(a, b)))
        trees.append(tuple(sorted(edges)))
    return trees


def path_masks_for_tree(n: int, edges: tuple[tuple[int, int], ...]) -> set[int]:
    if n == 1:
        return {1}
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    masks: set[int] = {1 << vertex for vertex in range(n)}
    for source in range(n):
        parent = [-1] * n
        parent[source] = source
        stack = [source]
        for node in stack:
            for neighbor in graph[node]:
                if parent[neighbor] == -1:
                    parent[neighbor] = node
                    stack.append(neighbor)
        for target in range(source + 1, n):
            mask = 0
            node = target
            while node != source:
                mask |= 1 << node
                node = parent[node]
            mask |= 1 << source
            masks.add(mask)
    return masks


def tree_representation_summary(family: list[int], n: int) -> dict[str, Any]:
    family_set = set(family)
    distribution: Counter[int] = Counter()
    witnesses: list[list[list[int]]] = []
    trees = prufer_trees(n)
    for edges in trees:
        path_masks = path_masks_for_tree(n, edges)
        distribution[len(path_masks)] += 1
        if family_set <= path_masks:
            witnesses.append([list(edge) for edge in edges])
    return {
        "ok": not witnesses,
        "labelled_trees_checked": len(trees),
        "path_set_count_distribution": dict(sorted((str(k), v) for k, v in distribution.items())),
        "representing_tree_count": len(witnesses),
        "representing_trees": witnesses,
    }


def public_family_hash(ground_set: list[int], family: list[int]) -> str:
    payload = {
        "case": "path-set-tree-representation-counterexample",
        "ground_set": ground_set,
        "family_masks": family,
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest().upper()


def load_certificate(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def verify(certificate: dict[str, Any]) -> dict[str, Any]:
    ground_set = list(certificate["ground_set"])
    n = len(ground_set)
    if ground_set != list(range(n)):
        raise AssertionError("ground set must be [0,1,...,n-1]")

    family_from_sets = [mask_from_vertices(list(items)) for items in certificate["family_sets"]]
    family = list(certificate["family_masks"])
    if family != family_from_sets:
        raise AssertionError("family_sets and family_masks disagree")
    if sorted(family) != family:
        raise AssertionError("family masks must be sorted")
    if any(mask == 0 for mask in family):
        raise AssertionError("family contains the empty set")

    helly = finite_helly_summary(family, n)
    chordal = chordal_summary(family)
    cliques = maximal_cliques(family)
    local = local_interval_summary(family, certificate["local_interval_orders"], n)
    trees = tree_representation_summary(family, n)

    expected = dict(certificate["expected"])
    checks = {
        "family_size": len(family),
        "nonempty_subfamilies_checked": helly["nonempty_subfamilies_checked"],
        "pairwise_intersecting_subfamilies": helly["pairwise_intersecting_subfamilies"],
        "maximal_clique_count": len(cliques),
        "labelled_trees_checked": trees["labelled_trees_checked"],
        "path_set_count_distribution": trees["path_set_count_distribution"],
        "representing_tree_count": trees["representing_tree_count"],
    }
    for key, expected_value in expected.items():
        if checks[key] != expected_value:
            raise AssertionError(f"unexpected {key}: {checks[key]} != {expected_value}")

    summary = {
        "ok": helly["ok"] and chordal["ok"] and local["ok"] and trees["ok"],
        "case": certificate["case"],
        "result": certificate["result"],
        "source_arxiv": certificate["source"]["arxiv"],
        "source_doi": certificate["source"]["doi"],
        "ground_set": ground_set,
        "family_masks": family,
        "family_sets": certificate["family_sets"],
        "family_sha256": public_family_hash(ground_set, family),
        "helly": helly,
        "intersection_graph_chordal": chordal,
        "maximal_cliques": cliques,
        "local_interval": local,
        "tree_representation": trees,
        "source_question_refuted": True,
    }
    if not summary["ok"]:
        raise AssertionError(json.dumps(summary, indent=2, sort_keys=True))
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=ROOT / "counterexample_certificate.json",
        help="path to the JSON counterexample certificate",
    )
    parser.add_argument(
        "--summary-out",
        type=Path,
        help="optional path for the compact verification summary",
    )
    args = parser.parse_args()

    summary = verify(load_certificate(args.certificate))
    text = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    if args.summary_out:
        args.summary_out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
