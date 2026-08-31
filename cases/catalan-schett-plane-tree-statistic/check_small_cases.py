"""Exhaustively verify the plane-tree identity through eight edges."""

from __future__ import annotations

from collections import Counter
from itertools import permutations
import json
from math import comb, factorial
from pathlib import Path
from typing import TypeAlias


Tree: TypeAlias = tuple["Tree", ...]
Permutation: TypeAlias = tuple[int, ...]


def edge_count(tree: Tree) -> int:
    return sum(1 + edge_count(child) for child in tree)


def node_count(tree: Tree) -> int:
    return edge_count(tree) + 1


def root_has_leaf_child(tree: Tree) -> bool:
    return any(not child for child in tree)


def mark(tree: Tree) -> int:
    total = 0
    for child in tree:
        total += int(bool(child) and root_has_leaf_child(child))
        total += mark(child)
    return total


def plane_trees_through(max_edges: int) -> list[tuple[Tree, ...]]:
    by_edges: list[tuple[Tree, ...]] = [((),)]
    for n in range(1, max_edges + 1):
        memo: dict[int, tuple[tuple[Tree, ...], ...]] = {}

        def forests(total: int) -> tuple[tuple[Tree, ...], ...]:
            if total == 0:
                return ((),)
            if total not in memo:
                result: list[tuple[Tree, ...]] = []
                for first_block in range(1, total + 1):
                    for first in by_edges[first_block - 1]:
                        for rest in forests(total - first_block):
                            result.append((first,) + rest)
                memo[total] = tuple(result)
            return memo[total]

        by_edges.append(tuple(forests(n)))
    return by_edges


def decompose(tree: Tree) -> tuple[Tree, Tree]:
    if not tree:
        raise ValueError("the zero-edge tree has no decomposition")
    if root_has_leaf_child(tree):
        split = next(i for i, child in enumerate(tree) if not child)
        return tree[:split], tree[split + 1 :]

    root_off_path = tree[1:]
    current = tree[0]
    intermediate: list[Tree] = []
    while current and current[0]:
        intermediate.append(current[1:])
        current = current[0]
    if not current:
        raise AssertionError("leftmost path ended incorrectly")
    return root_off_path + ((),) + current[1:], tuple(intermediate)


def recompose(left: Tree, right: Tree) -> Tree:
    if not root_has_leaf_child(left):
        return left + ((),) + right
    split = next(i for i, child in enumerate(left) if not child)
    root_off_path = left[:split]
    current: Tree = ((),) + left[split + 1 :]
    for off_path in reversed(right):
        current = (current,) + off_path
    return (current,) + root_off_path


def phi(tree: Tree) -> Permutation:
    if not tree:
        return ()
    left, right = decompose(tree)
    k = node_count(left)
    alpha, beta = phi(left), phi(right)
    return (k,) + alpha + tuple(k + value for value in beta)


def psi(pi: Permutation) -> Tree:
    if not pi:
        return ()
    k = pi[0]
    alpha = pi[1:k]
    beta = tuple(value - k for value in pi[k:])
    if set(alpha) != set(range(1, k)):
        raise ValueError("invalid first block")
    if set(beta) != set(range(1, len(pi) - k + 1)):
        raise ValueError("invalid second block")
    return recompose(psi(alpha), psi(beta))


def inverse(pi: Permutation) -> Permutation:
    result = [0] * len(pi)
    for position, value in enumerate(pi, start=1):
        result[value - 1] = position
    return tuple(result)


def run_lengths(pi: Permutation, ascending: bool) -> tuple[int, ...]:
    if not pi:
        return ()
    result: list[int] = []
    length = 1
    for a, b in zip(pi, pi[1:]):
        if (a < b) == ascending:
            length += 1
        else:
            result.append(length)
            length = 1
    result.append(length)
    return tuple(result)


def mnd(pi: Permutation) -> int:
    return sum(length // 2 for length in run_lengths(pi, False))


def mna(pi: Permutation) -> int:
    return sum(length // 2 for length in run_lengths(pi, True))


def iar(pi: Permutation) -> int:
    runs = run_lengths(pi, True)
    return runs[0] if runs else 0


def avoids_231(pi: Permutation) -> bool:
    n = len(pi)
    return all(
        not (pi[j] > pi[i] > pi[k])
        for i in range(n)
        for j in range(i + 1, n)
        for k in range(j + 1, n)
    )


def q(tree: Tree) -> int:
    if not tree:
        return 0
    left, right = decompose(tree)
    return q(right) + 1 if not left else q(left)


def st(tree: Tree) -> int:
    if not tree:
        return 0
    left, right = decompose(tree)
    return st(left) + st(right) + q(right) % 2


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def main() -> None:
    trees_by_n = plane_trees_through(8)
    summary: list[dict[str, int | bool]] = []

    for n, trees in enumerate(trees_by_n):
        expected = catalan(n)
        avoiders = {
            pi for pi in permutations(range(1, n + 1)) if avoids_231(pi)
        }
        assert len(trees) == len(avoiders) == expected

        images: set[Permutation] = set()
        tree_pairs: Counter[tuple[int, int]] = Counter()
        permutation_pairs: Counter[tuple[int, int]] = Counter()

        pair_count = 0
        if n:
            for left_edges in range(n):
                right_edges = n - 1 - left_edges
                for left in trees_by_n[left_edges]:
                    for right in trees_by_n[right_edges]:
                        rebuilt = recompose(left, right)
                        assert decompose(rebuilt) == (left, right)
                        pair_count += 1
            assert pair_count == expected

        for tree in trees:
            pi = phi(tree)
            inv = inverse(pi)
            images.add(pi)
            assert avoids_231(pi)
            assert psi(pi) == tree
            assert mark(tree) == mnd(pi)
            assert q(tree) == iar(inv)
            assert st(tree) == mna(inv)
            if tree:
                assert recompose(*decompose(tree)) == tree
            tree_pairs[(mark(tree), st(tree))] += 1

        assert images == avoiders
        for pi in avoiders:
            assert phi(psi(pi)) == pi
            permutation_pairs[(mnd(pi), mna(inverse(pi)))] += 1
        assert tree_pairs == permutation_pairs

        summary.append(
            {
                "n": n,
                "plane_trees": len(trees),
                "permutations_checked": factorial(n),
                "avoiders": len(avoiders),
                "decomposition_pairs": pair_count,
                "all_assertions_passed": True,
            }
        )

    output = {
        "range": "0 <= n <= 8",
        "total_plane_trees": sum(row["plane_trees"] for row in summary),
        "total_permutations_checked": sum(row["permutations_checked"] for row in summary),
        "all_assertions_passed": True,
        "by_n": summary,
    }
    output_path = Path(__file__).with_name("small_case_summary.json")
    output_path.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
