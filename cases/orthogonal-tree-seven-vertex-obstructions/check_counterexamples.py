"""Verify the public finite certificate for the orthogonal-tree case."""

from __future__ import annotations

import itertools
import json
import sys
from collections import deque
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERT = ROOT / "counterexample_certificate.json"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def normalized_edges(edges: list[list[int]]) -> set[tuple[int, int]]:
    return {tuple(sorted((int(a), int(b)))) for a, b in edges}


def edge_bits(n: int, edges: set[tuple[int, int]], order: tuple[int, ...] | None = None) -> str:
    if order is None:
        order = tuple(range(n))
    position = {vertex: index for index, vertex in enumerate(order)}
    relabelled = {
        tuple(sorted((position[a], position[b])))
        for a, b in edges
        if a in position and b in position
    }
    return "".join(
        "1" if (i, j) in relabelled else "0"
        for i, j in itertools.combinations(range(n), 2)
    )


def canonical_bits(n: int, edges: set[tuple[int, int]]) -> str:
    return min(edge_bits(n, edges, order) for order in itertools.permutations(range(n)))


def graph6_edges(code: str) -> tuple[int, set[tuple[int, int]]]:
    n = ord(code[0]) - 63
    if not 0 <= n <= 62:
        fail("this checker only supports small graph6 strings")
    bits: list[int] = []
    for char in code[1:]:
        value = ord(char) - 63
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    edges: set[tuple[int, int]] = set()
    cursor = 0
    for j in range(1, n):
        for i in range(j):
            if bits[cursor]:
                edges.add((i, j))
            cursor += 1
    return n, edges


def induced_edges(edges: set[tuple[int, int]], subset: tuple[int, ...]) -> set[tuple[int, int]]:
    position = {vertex: index for index, vertex in enumerate(subset)}
    return {
        tuple(sorted((position[a], position[b])))
        for a, b in edges
        if a in position and b in position
    }


def deletion_edges(edges: set[tuple[int, int]], deleted: int) -> set[tuple[int, int]]:
    kept = [vertex for vertex in range(7) if vertex != deleted]
    position = {vertex: index for index, vertex in enumerate(kept)}
    return {
        tuple(sorted((position[a], position[b])))
        for a, b in edges
        if a in position and b in position
    }


def distances_from_tree(
    topology_edges: list[list[int]], squared_edge_lengths: list[str]
) -> dict[tuple[int, int], Fraction]:
    if len(topology_edges) != len(squared_edge_lengths):
        fail("tree edge and weight counts differ")
    adjacency: dict[int, list[tuple[int, Fraction]]] = {}
    for pair, raw_weight in zip(topology_edges, squared_edge_lengths):
        a, b = pair
        weight = Fraction(raw_weight)
        if weight <= 0:
            fail("tree witness has a nonpositive edge length")
        adjacency.setdefault(a, []).append((b, weight))
        adjacency.setdefault(b, []).append((a, weight))
    node_count = len(adjacency)
    if sum(len(v) for v in adjacency.values()) // 2 != node_count - 1:
        fail("witness topology is not a tree")
    out: dict[tuple[int, int], Fraction] = {}
    for start in range(6):
        seen = {start: Fraction(0)}
        queue: deque[int] = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor, weight in adjacency.get(node, []):
                if neighbor not in seen:
                    seen[neighbor] = seen[node] + weight
                    queue.append(neighbor)
        if set(range(6)) - set(seen):
            fail("witness tree does not connect all marked vertices")
        for stop in range(start + 1, 6):
            out[(start, stop)] = seen[stop]
    return out


def witness_edges(witness: dict) -> set[tuple[int, int]]:
    distances = distances_from_tree(
        witness["topology_edges"], witness["squared_edge_lengths"]
    )
    return {pair for pair, distance in distances.items() if distance == 1}


def main() -> None:
    data = json.loads(CERT.read_text(encoding="utf-8"))
    if data.get("case_slug") != "orthogonal-tree-seven-vertex-obstructions":
        fail("wrong case slug")
    if data.get("result") != "PARTIAL_RESULT":
        fail("wrong result type")
    if data.get("verification", {}).get("status") != "INDEPENDENTLY_VERIFIED":
        fail("verification status is not independently verified")
    if data.get("verification", {}).get("verdict") != "CORRECT":
        fail("independent verdict is not CORRECT")
    if data.get("boundaries", {}).get("full_question_15") != "OPEN":
        fail("full Question 15 boundary changed")
    if data.get("boundaries", {}).get("priority") != "NOT_ESTABLISHED":
        fail("priority boundary changed")

    forbidden = {
        item["name"]: canonical_bits(5, normalized_edges(item["edges"]))
        for item in data["old_obstructions"]
    }
    forbidden_bits = set(forbidden.values())
    if len(forbidden_bits) != 3:
        fail("old obstruction definitions are not distinct")

    for graph in data["graphs"]:
        edges = normalized_edges(graph["edges"])
        n, decoded = graph6_edges(graph["graph6"])
        if n != 7 or decoded != edges:
            fail(f"graph6 mismatch for {graph['name']}")
        if canonical_bits(7, edges) != graph["canonical_bits"]:
            fail(f"canonical bits mismatch for {graph['name']}")
        degrees = sorted(
            (sum(1 for edge in edges if vertex in edge) for vertex in range(7)),
            reverse=True,
        )
        if degrees != graph["degree_sequence"]:
            fail(f"degree sequence mismatch for {graph['name']}")

        for subset in itertools.combinations(range(7), 5):
            bits = canonical_bits(5, induced_edges(edges, subset))
            if bits in forbidden_bits:
                names = [name for name, old_bits in forbidden.items() if old_bits == bits]
                fail(f"{graph['name']} contains old obstruction {names[0]}")

        if len(graph["deletion_witnesses"]) != 7:
            fail(f"missing deletion witnesses for {graph['name']}")
        for witness in graph["deletion_witnesses"]:
            deleted = int(witness["deleted_vertex"])
            actual = canonical_bits(6, deletion_edges(edges, deleted))
            if actual != witness["canonical_six_bits"]:
                fail(f"wrong deletion canonical bits for {graph['name']} minus {deleted}")
            represented = canonical_bits(6, witness_edges(witness))
            if represented != witness["canonical_six_bits"]:
                fail(f"witness tree mismatch for {graph['name']} minus {deleted}")

        if sum(graph["blocker_counts"].values()) != data["seven_marked_topology_denominator"]["count"]:
            fail(f"blocker counts do not match topology denominator for {graph['name']}")

    scope = data["targeted_search_scope"]
    if scope["full_topology_targets"] != len(data["graphs"]):
        fail("targeted full-topology target count mismatch")
    if scope["connected_complement_connected_module_prime"] != (
        scope["represented_by_six_vertex_witness_lifts"] + scope["full_topology_targets"]
    ):
        fail("targeted search funnel mismatch")

    print("PASS: orthogonal-tree obstruction certificate verified")


if __name__ == "__main__":
    main()
