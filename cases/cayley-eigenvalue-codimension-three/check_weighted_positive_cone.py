#!/usr/bin/env python3
"""Dependency-free exact checks for the hypergraph component formula."""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path


def cycle_permutation(n, cycle):
    permutation = list(range(n))
    for source, target in zip(cycle, cycle[1:] + cycle[:1]):
        permutation[source] = target
    return tuple(permutation)


def term_matrix(n, k, required):
    required = set(required)
    matrix = [[0] * n for _ in range(n)]
    for support in itertools.combinations(range(n), k):
        if not required.issubset(support):
            continue
        anchor = support[0]
        for rest in itertools.permutations(support[1:]):
            permutation = cycle_permutation(n, (anchor,) + rest)
            for source, target in enumerate(permutation):
                matrix[target][source] += 1
    return matrix


def rank(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    row = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[row], rows[pivot] = rows[pivot], rows[row]
        scale = rows[row][column]
        rows[row] = [value / scale for value in rows[row]]
        for i in range(len(rows)):
            if i == row or not rows[i][column]:
                continue
            scale = rows[i][column]
            rows[i] = [a - scale * b for a, b in zip(rows[i], rows[row])]
        row += 1
        if row == len(rows):
            break
    return row


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def standard_value(matrix, required):
    outside = [i for i in range(len(matrix)) if i not in required]
    p, q = outside[:2]
    vector = [0] * len(matrix)
    vector[p], vector[q] = 1, -1
    image = matvec(matrix, vector)
    assert image == [image[p] * value for value in vector]
    return image[p]


def components(n, hyperedges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for edge in hyperedges:
        for vertex in edge[1:]:
            union(edge[0], vertex)
    groups = {}
    for vertex in range(n):
        groups.setdefault(find(vertex), []).append(vertex)
    return list(groups.values())


def check_case(n, k, terms):
    total = [[0] * n for _ in range(n)]
    target = 0
    lower_union = set()
    local_edges = []
    for required, weight in terms:
        matrix = term_matrix(n, k, required)
        target += weight * standard_value(matrix, required)
        for i in range(n):
            for j in range(n):
                total[i][j] += weight * matrix[i][j]
        if 0 < len(required) < k:
            lower_union.update(required)
        elif len(required) == k:
            local_edges.append(required)

    groups = components(n, local_edges)
    free = [group for group in groups if lower_union.isdisjoint(group)]
    predicted = len(free) - 1
    shifted = [
        [total[i][j] - (target if i == j else 0) for j in range(n)]
        for i in range(n)
    ]
    actual = n - rank(shifted)

    constraints = [[1] * n]
    for vertex in sorted(lower_union):
        row = [0] * n
        row[vertex] = 1
        constraints.append(row)
    for edge in local_edges:
        for vertex in edge[1:]:
            row = [0] * n
            row[edge[0]], row[vertex] = 1, -1
            constraints.append(row)
    constrained = n - rank(constraints)
    return {
        "n": n,
        "k": k,
        "predicted_dimension": predicted,
        "constraint_dimension": constrained,
        "actual_target_eigenspace_dimension": actual,
        "pass": predicted == constrained == actual and predicted >= 1,
    }


def main():
    cases = [
        (7, 3, [((0,), 2), ((0, 1, 2), 3)]),
        (7, 3, [((0,), 1), ((0, 1, 2), 2), ((2, 3, 4), 1)]),
        (7, 3, [((), 2), ((3,), 1), ((0, 1, 2), 4)]),
        (6, 4, [((0, 1), 3), ((0, 1, 2, 3), 2)]),
        (6, 4, [((4,), 2), ((0, 1, 2, 3), 1)]),
        (7, 4, [((), 1), ((0, 1), 2), ((0, 1, 2, 3), 1)]),
        (9, 3, [((0,), 1), ((0, 1, 2), 1), ((3, 4, 5), 2), ((6, 7, 8), 3)]),
    ]
    rows = [check_case(*case) for case in cases]
    result = {
        "status": "PASS" if all(row["pass"] for row in rows) else "FAIL",
        "cases": rows,
        "scope": "Finite exact natural-module checks; the general proof is analytic.",
    }
    output = Path(__file__).with_name("weighted_positive_cone_summary.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
