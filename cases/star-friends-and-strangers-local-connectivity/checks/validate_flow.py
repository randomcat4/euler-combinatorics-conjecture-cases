#!/usr/bin/env python3
"""Brute-force validation of search_fs.local_connectivity on tiny graphs."""

from itertools import combinations
from pathlib import Path
import json

from search_fs import graph_adjacency, local_connectivity


def is_connected_without(graph, s, t, blocked, omit_direct):
    seen = {s}
    queue = [s]
    for u in queue:
        for v in graph[u]:
            if omit_direct and {u, v} == {s, t}:
                continue
            if v not in blocked and v not in seen:
                seen.add(v)
                queue.append(v)
    return t in seen


def brute_local(graph, s, t):
    adjacent = t in graph[s]
    internal = [v for v in range(len(graph)) if v not in (s, t)]
    for size in range(len(internal) + 1):
        for subset in combinations(internal, size):
            if not is_connected_without(graph, s, t, set(subset), adjacent):
                return size + int(adjacent)
    raise AssertionError("deleting every internal vertex must block the edge-deleted graph")


def main():
    pairs = 0
    connected_graphs = 0
    adjacent_pairs = 0
    for n in range(2, 6):
        edges = n * (n - 1) // 2
        for mask in range(1 << edges):
            graph = graph_adjacency(n, mask)
            seen = {0}
            queue = [0]
            for u in queue:
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
            if len(seen) != n:
                continue
            connected_graphs += 1
            for s in range(n):
                for t in range(s + 1, n):
                    expected = brute_local(graph, s, t)
                    target = min(len(graph[s]), len(graph[t]))
                    actual, separator, adjacent = local_connectivity(graph, s, t, target)
                    assert expected == actual, (n, mask, s, t, expected, actual)
                    assert adjacent == (t in graph[s])
                    adjacent_pairs += int(adjacent)
                    pairs += 1
    result = {
        "scope": "all connected labelled simple graphs on 2..5 vertices, all endpoint pairs",
        "connected_graphs": connected_graphs,
        "pairs": pairs,
        "adjacent_pairs": adjacent_pairs,
        "status": "all node-split values equal brute-force vertex-cut values",
    }
    target = Path(__file__).with_name("flow_validation.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
