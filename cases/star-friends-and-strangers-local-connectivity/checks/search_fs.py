#!/usr/bin/env python3
"""Exact counterexample search for FS(X, Star_n), without external packages.

The default exhaustive range is all connected unlabeled simple X on n <= 5.
Use --max-n 6 for the substantially larger next range.  Only connected FS graphs
and endpoint pairs whose two hole degrees exceed delta(X) require max-flow tests.
"""

from __future__ import annotations

import argparse
from collections import deque
from hashlib import sha256
from itertools import combinations, permutations
import json
import math
from pathlib import Path
import sys
import time

sys.setrecursionlimit(10000)


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add(self, u, v, cap):
        a = [v, cap, None]
        b = [u, 0, a]
        a[2] = b
        self.g[u].append(a)
        self.g[v].append(b)

    def flow(self, s, t, limit):
        answer = 0
        while answer < limit:
            level = [-1] * self.n
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v, cap, rev in self.g[u]:
                    if cap and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                break
            it = [0] * self.n

            def dfs(u, amount):
                if u == t:
                    return amount
                while it[u] < len(self.g[u]):
                    edge = self.g[u][it[u]]
                    v, cap, rev = edge
                    if cap and level[v] == level[u] + 1:
                        sent = dfs(v, min(amount, cap))
                        if sent:
                            edge[1] -= sent
                            rev[1] += sent
                            return sent
                    it[u] += 1
                return 0

            while answer < limit:
                sent = dfs(s, limit - answer)
                if not sent:
                    break
                answer += sent
        return answer

    def reachable(self, source):
        seen = {source}
        q = deque([source])
        while q:
            u = q.popleft()
            for v, cap, rev in self.g[u]:
                if cap and v not in seen:
                    seen.add(v)
                    q.append(v)
        return seen


def edge_list(n):
    return list(combinations(range(n), 2))


def graph_adjacency(n, mask):
    adj = [[] for _ in range(n)]
    for bit, (u, v) in enumerate(edge_list(n)):
        if mask >> bit & 1:
            adj[u].append(v)
            adj[v].append(u)
    return [sorted(x) for x in adj]


def connected(adj):
    seen = {0}
    q = [0]
    for u in q:
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen) == len(adj)


def transform_mask(n, mask, p):
    edges = edge_list(n)
    pos = {edge: i for i, edge in enumerate(edges)}
    out = 0
    while mask:
        low = mask & -mask
        bit = low.bit_length() - 1
        u, v = edges[bit]
        a, b = sorted((p[u], p[v]))
        out |= 1 << pos[(a, b)]
        mask -= low
    return out


def unlabeled_connected_graphs(n):
    perms = list(permutations(range(n)))
    all_masks = 1 << (n * (n - 1) // 2)
    seen = set()
    for mask in range(all_masks):
        if mask in seen:
            continue
        orbit = {transform_mask(n, mask, p) for p in perms}
        seen.update(orbit)
        representative = min(orbit)
        if connected(graph_adjacency(n, representative)):
            yield representative


def automorphisms(n, mask):
    return [p for p in permutations(range(n)) if transform_mask(n, mask, p) == mask]


def orbit_representatives(vertices, automorphisms_):
    remaining = set(vertices)
    reps = []
    while remaining:
        v = min(remaining)
        orbit = {p[v] for p in automorphisms_}
        reps.append(v)
        remaining -= orbit
    return reps


def fs_graph(adj):
    n = len(adj)
    states = list(permutations(range(n)))
    index = {p: i for i, p in enumerate(states)}
    graph = [[] for _ in states]
    hole_positions = []
    for i, state in enumerate(states):
        hole = state.index(n - 1)
        hole_positions.append(hole)
        for v in adj[hole]:
            q = list(state)
            q[hole], q[v] = q[v], q[hole]
            graph[i].append(index[tuple(q)])
        graph[i].sort()
    return states, index, graph, hole_positions


def component_size(graph, start=0, blocked=frozenset(), omit_edge=None):
    if start in blocked:
        return 0
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if omit_edge is not None and {u, v} == set(omit_edge):
                continue
            if v not in blocked and v not in seen:
                seen.add(v)
                q.append(v)
    return len(seen)


def local_connectivity(graph, s, t, target):
    """Return exact value if below target, otherwise target as a lower bound.

    For adjacent endpoints, their direct edge is counted once and removed before
    the node-split calculation of all other paths.
    """
    adjacent = t in graph[s]
    need = target - int(adjacent)
    if need <= 0:
        return target, [], adjacent
    N = len(graph)
    net = Dinic(2 * N)
    INF = need
    for v in range(N):
        cap = INF if v in (s, t) else 1
        net.add(2 * v, 2 * v + 1, cap)
    for u, row in enumerate(graph):
        for v in row:
            if u < v:
                if adjacent and {u, v} == {s, t}:
                    continue
                net.add(2 * u + 1, 2 * v, INF)
                net.add(2 * v + 1, 2 * u, INF)
    value = net.flow(2 * s + 1, 2 * t, need)
    total = value + int(adjacent)
    if value == need:
        return target, [], adjacent
    reach = net.reachable(2 * s + 1)
    separator = [
        v for v in range(N)
        if v not in (s, t) and 2 * v in reach and 2 * v + 1 not in reach
    ]
    assert len(separator) == value
    omitted = (s, t) if adjacent else None
    # The separator blocks all paths after removing the direct edge if present.
    blocked = set(separator)
    seen = {s}
    q = deque([s])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if omitted is not None and {u, v} == {s, t}:
                continue
            if v not in blocked and v not in seen:
                seen.add(v)
                q.append(v)
    assert t not in seen
    return total, separator, adjacent


def canonical_start(n, hole):
    leaves = iter(range(n - 1))
    return tuple(n - 1 if v == hole else next(leaves) for v in range(n))


def target_orbit_representatives(states, state_index, sigma, source_hole,
                                 automorphisms_, allowed_holes):
    """Orbits of targets under the full symmetry stabilizing sigma.

    A base automorphism fixing the source hole is followed by the unique leaf-label
    permutation that returns the canonical source state sigma to itself.
    """
    n = len(sigma)
    actions = []
    for phi in automorphisms_:
        if phi[source_hole] != source_hole:
            continue
        psi = list(range(n))
        for q in range(n):
            psi[sigma[q]] = sigma[phi[q]]
        assert psi[n - 1] == n - 1

        def action(tau, phi=phi, psi=tuple(psi)):
            out = [None] * n
            for q in range(n):
                out[phi[q]] = psi[tau[q]]
            return tuple(out)

        assert action(sigma) == sigma
        actions.append(action)
    candidate_indices = {
        i for i, tau in enumerate(states)
        if tau != sigma and tau.index(n - 1) in allowed_holes
    }
    all_candidates = set(candidate_indices)
    reps = []
    while candidate_indices:
        i = min(candidate_indices)
        orbit = {state_index[action(states[i])] for action in actions}
        assert orbit <= all_candidates
        reps.append(i)
        candidate_indices -= orbit
    return reps


def graph_record(n, mask, adj):
    return {
        "n": n,
        "mask": mask,
        "edges": [[u, v] for u in range(n) for v in adj[u] if u < v],
        "degrees": list(map(len, adj)),
    }


def run(max_n, output_path):
    start_time = time.time()
    stats = {
        "range": f"all connected unlabeled simple X for 2 <= n <= {max_n}",
        "unlabeled_connected_X": 0,
        "connected_FS": 0,
        "irregular_connected_FS_with_high_degree_holes": 0,
        "source_hole_orbits": 0,
        "endpoint_pairs_maxflow_checked": 0,
        "counterexamples": [],
    }
    per_n = []
    for n in range(2, max_n + 1):
        row = {k: 0 for k in [
            "unlabeled_connected_X", "connected_FS",
            "irregular_connected_FS_with_high_degree_holes",
            "source_hole_orbits", "endpoint_pairs_maxflow_checked",
        ]}
        for mask in unlabeled_connected_graphs(n):
            row["unlabeled_connected_X"] += 1
            stats["unlabeled_connected_X"] += 1
            adj = graph_adjacency(n, mask)
            states, state_index, F, holes = fs_graph(adj)
            if component_size(F) != len(F):
                continue
            row["connected_FS"] += 1
            stats["connected_FS"] += 1
            degrees = list(map(len, adj))
            delta = min(degrees)
            high = [v for v in range(n) if degrees[v] > delta]
            if not high:
                continue
            row["irregular_connected_FS_with_high_degree_holes"] += 1
            stats["irregular_connected_FS_with_high_degree_holes"] += 1
            source_holes = orbit_representatives(high, automorphisms(n, mask))
            row["source_hole_orbits"] += len(source_holes)
            stats["source_hole_orbits"] += len(source_holes)
            for source_hole in source_holes:
                sigma = canonical_start(n, source_hole)
                s = state_index[sigma]
                for t, rho in enumerate(states):
                    if t == s or holes[t] not in high:
                        continue
                    target = min(degrees[source_hole], degrees[holes[t]])
                    value, separator, adjacent = local_connectivity(F, s, t, target)
                    row["endpoint_pairs_maxflow_checked"] += 1
                    stats["endpoint_pairs_maxflow_checked"] += 1
                    if value < target:
                        record = graph_record(n, mask, adj)
                        record.update({
                            "sigma": list(sigma),
                            "rho": list(rho),
                            "sigma_index": s,
                            "rho_index": t,
                            "sigma_hole": source_hole,
                            "rho_hole": holes[t],
                            "endpoint_degrees": [degrees[source_hole], degrees[holes[t]]],
                            "local_vertex_connectivity": value,
                            "adjacent_endpoints": adjacent,
                            "separator_state_indices": separator,
                            "separator_states": [list(states[v]) for v in separator],
                            "certificate_meaning": (
                                "after deleting separator and the direct endpoint edge if adjacent, "
                                "sigma and rho are disconnected; add one for that direct edge"
                            ),
                        })
                        stats["counterexamples"].append(record)
                        output_path.write_text(json.dumps({"stats": stats, "per_n": per_n + [row]}, indent=2) + "\n")
                        return stats, per_n + [row]
        per_n.append({"n": n, **row})
        print(json.dumps(per_n[-1]), flush=True)
    stats["elapsed_seconds"] = time.time() - start_time
    result = {"stats": stats, "per_n": per_n}
    canonical = json.dumps(result, indent=2) + "\n"
    output_path.write_text(canonical, encoding="utf-8")
    return stats, per_n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=5)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("search_n5.json"))
    args = parser.parse_args()
    stats, per_n = run(args.max_n, args.output)
    print(json.dumps({"output": str(args.output), "stats": stats, "per_n": per_n}, indent=2))


if __name__ == "__main__":
    main()
