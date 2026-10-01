#!/usr/bin/env python3
"""Finite verification of the plane-tree/run-composition claims.

Plane trees and 231-avoiding permutations are enumerated independently.
The script is self-contained and uses only the Python standard library.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "results.json"
MAX_N = 9

Tree = tuple["Tree", ...]


@lru_cache(maxsize=None)
def forests(total_edges: int) -> tuple[tuple[Tree, ...], ...]:
    if total_edges == 0:
        return ((),)
    out: list[tuple[Tree, ...]] = []
    for first_cost in range(1, total_edges + 1):
        for first in trees(first_cost - 1):
            for rest in forests(total_edges - first_cost):
                out.append((first,) + rest)
    return tuple(out)


@lru_cache(maxsize=None)
def trees(edge_count: int) -> tuple[Tree, ...]:
    return tuple(forests(edge_count))


@lru_cache(maxsize=None)
def tree_size(tree: Tree) -> int:
    return sum(1 + tree_size(child) for child in tree)


def cut(tree: Tree) -> tuple[Tree, Tree]:
    assert tree
    for i, child in enumerate(tree):
        if child == ():
            return tree[:i], tree[i + 1 :]

    side_forests: list[tuple[Tree, ...]] = []
    current = tree
    while True:
        assert current and current[0] != ()
        side_forests.append(current[1:])
        current = current[0]
        if current and current[0] == ():
            side_forests.append(current[1:])
            break
    left = side_forests[0] + ((),) + side_forests[-1]
    right = tuple(tuple(forest) for forest in side_forests[1:-1])
    assert tree_size(tree) == 1 + tree_size(left) + tree_size(right)
    return left, right


@lru_cache(maxsize=None)
def lambda_list(tree: Tree) -> tuple[int, ...]:
    if not tree:
        return ()
    left, right = cut(tree)
    lam_r = lambda_list(right)
    raised = (1,) if not lam_r else (lam_r[0] + 1,) + lam_r[1:]
    answer = lambda_list(left) + raised
    assert sum(answer) == tree_size(tree)
    return answer


def marked_vertices(tree: Tree, is_root: bool = True) -> int:
    here = int((not is_root) and any(child == () for child in tree))
    return here + sum(marked_vertices(child, False) for child in tree)


@lru_cache(maxsize=None)
def tree_to_perm(tree: Tree) -> tuple[int, ...]:
    if not tree:
        return ()
    left, right = cut(tree)
    alpha = tree_to_perm(left)
    beta = tree_to_perm(right)
    k = tree_size(left) + 1
    return (k,) + alpha + tuple(k + x for x in beta)


def avoids_231(p: tuple[int, ...]) -> bool:
    n = len(p)
    suffix_min = [n + 1] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix_min[i] = min(p[i], suffix_min[i + 1])
    for j in range(1, n - 1):
        low = suffix_min[j + 1]
        if any(low < p[i] < p[j] for i in range(j)):
            return False
    return True


def inverse_perm(p: tuple[int, ...]) -> tuple[int, ...]:
    inv = [0] * len(p)
    for pos, value in enumerate(p, 1):
        inv[value - 1] = pos
    return tuple(inv)


def run_lengths(p: tuple[int, ...], ascending: bool) -> tuple[int, ...]:
    if not p:
        return ()
    lengths = []
    start = 0
    for i in range(len(p) - 1):
        continues = p[i] < p[i + 1] if ascending else p[i] > p[i + 1]
        if not continues:
            lengths.append(i + 1 - start)
            start = i + 1
    lengths.append(len(p) - start)
    return tuple(lengths)


def mnd(p: tuple[int, ...]) -> int:
    return sum(r // 2 for r in run_lengths(p, ascending=False))


def mna(p: tuple[int, ...]) -> int:
    return sum(r // 2 for r in run_lengths(p, ascending=True))


def canonical_counter_hash(counter: Counter) -> str:
    rows = sorted((repr(key), value) for key, value in counter.items())
    data = json.dumps(rows, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return hashlib.sha256(data).hexdigest()


def weighted_polynomial(signature: Counter, weights: dict[int, int]) -> dict[int, int]:
    """Coefficient by marked/mnd exponent after arbitrary multiplicative weights."""
    out: Counter[int] = Counter()
    for (stat, runs), multiplicity in signature.items():
        weight = 1
        for r in runs:
            weight *= weights.get(r, 0)
        out[stat] += multiplicity * weight
    return dict(sorted(out.items()))


def check_n(n: int) -> dict:
    tree_list = trees(n)
    avoiders = tuple(p for p in itertools.permutations(range(1, n + 1)) if avoids_231(p))
    mapped = tuple(tree_to_perm(t) for t in tree_list)
    assert len(set(mapped)) == len(mapped)
    assert set(mapped) == set(avoiders)

    # The cut itself must be a bijection to all ordered pairs of smaller trees.
    cut_pairs = Counter(cut(t) for t in tree_list) if n else Counter()
    expected_pairs = Counter(
        (left, right)
        for left_size in range(n)
        for left in trees(left_size)
        for right in trees(n - 1 - left_size)
    ) if n else Counter()
    assert cut_pairs == expected_pairs

    tree_signature = Counter((marked_vertices(t), lambda_list(t)) for t in tree_list)
    perm_signature = Counter(
        (mnd(p), run_lengths(inverse_perm(p), ascending=True)) for p in avoiders
    )
    assert tree_signature == perm_signature

    tree_original = Counter(
        (marked_vertices(t), sum(r // 2 for r in lambda_list(t))) for t in tree_list
    )
    perm_original = Counter((mnd(p), mna(inverse_perm(p))) for p in avoiders)
    assert tree_original == perm_original

    weight_families = {
        "affine": {r: 2 * r + 1 for r in range(1, n + 1)},
        "with_zero": {r: (0 if r % 3 == 0 else r + 2) for r in range(1, n + 1)},
        "signed": {r: (-1) ** r * (r * r + 1) for r in range(1, n + 1)},
    }
    weighted = {}
    for name, weights in weight_families.items():
        lhs = weighted_polynomial(perm_signature, weights)
        rhs = weighted_polynomial(tree_signature, weights)
        assert lhs == rhs
        weighted[name] = lhs

    # Pointwise check of both statistics under the displayed bijection.
    for tree, p in zip(tree_list, mapped):
        assert marked_vertices(tree) == mnd(p)
        assert lambda_list(tree) == run_lengths(inverse_perm(p), ascending=True)

    return {
        "n": n,
        "plane_trees": len(tree_list),
        "avoiders_231": len(avoiders),
        "cut_pairs": len(cut_pairs),
        "distinct_full_signatures": len(tree_signature),
        "full_signature_sha256": canonical_counter_hash(tree_signature),
        "distinct_original_stat_pairs": len(tree_original),
        "original_joint_sha256": canonical_counter_hash(tree_original),
        "weighted_coefficient_vectors": weighted,
        "bijection_exact": True,
        "ordered_run_signature_equal": True,
        "original_joint_statistic_equal": True,
    }


def main() -> None:
    records = [check_n(n) for n in range(MAX_N + 1)]
    assert [r["plane_trees"] for r in records] == [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
    result = {
        "problem": "catalan-schett-plane-tree-runs",
        "status": "PASS_FINITE_EXACT",
        "claim_scope": "plane-tree to 231-avoiding-permutation bijection with full inverse ascending-run composition",
        "coverage": {
            "n_range": [0, MAX_N],
            "tree_enumeration": "all rooted plane trees",
            "permutation_enumeration": "all permutations filtered directly for 231 avoidance",
            "weight_families": ["affine", "with_zero", "signed"],
            "universal_finite_check": "equality of the full ordered run-list signature",
        },
        "per_n": records,
    }
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"problem": result["problem"], "status": result["status"]}, ensure_ascii=False))
    print("counts_n0_to_n9", [r["plane_trees"] for r in records])


if __name__ == "__main__":
    main()
