#!/usr/bin/env python3
"""Exact same-hole search on selected high-risk seven-vertex base graphs."""

from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path
import time

from search_fs import (
    automorphisms, canonical_start, component_size, edge_list, fs_graph,
    graph_adjacency, graph_record, local_connectivity, orbit_representatives,
    target_orbit_representatives,
)


N = 7
EDGE_POSITION = {e: i for i, e in enumerate(edge_list(N))}


def mask_of(edges):
    mask = 0
    for u, v in edges:
        if u > v:
            u, v = v, u
        mask |= 1 << EDGE_POSITION[(u, v)]
    return mask


def clique(vertices):
    return set(combinations(vertices, 2))


def complete_bipartite(left, right):
    return {(u, v) for u in left for v in right}


def cycle(vertices):
    return {
        tuple(sorted((vertices[i], vertices[(i + 1) % len(vertices)])))
        for i in range(len(vertices))
    }


def candidates():
    V = set(range(N))
    all_edges = clique(range(N))
    out = []

    rim = list(range(1, 7))
    out.append(("wheel_W7", cycle(rim) | {(0, v) for v in rim}))
    out.append(("wheel_W7_minus_one_spoke_plus_rim_chord",
                (cycle(rim) | {(0, v) for v in rim if v != 1} | {(1, 3)})))

    out.append(("K2_join_I5", {(0, 1)} | complete_bipartite({0, 1}, {2, 3, 4, 5, 6})))
    out.append(("K2_5_plus_edge_in_size5_part",
                complete_bipartite({0, 1}, {2, 3, 4, 5, 6}) | {(2, 3)}))
    out.append(("K3_join_I4", clique({0, 1, 2}) | complete_bipartite({0, 1, 2}, {3, 4, 5, 6})))
    out.append(("K4_join_I3", clique({0, 1, 2, 3}) | complete_bipartite({0, 1, 2, 3}, {4, 5, 6})))
    out.append(("complete_tripartite_2_2_3",
                complete_bipartite({0, 1}, {2, 3}) |
                complete_bipartite({0, 1}, {4, 5, 6}) |
                complete_bipartite({2, 3}, {4, 5, 6})))

    out.append(("two_cliques_K4_K5_overlap_K2", clique({0, 1, 2, 3}) | clique({0, 1, 4, 5, 6})))
    out.append(("two_K4_overlap_edge_plus_cross_chord",
                clique({0, 1, 2, 3}) | clique({0, 1, 4, 5}) | {(2, 6), (4, 6), (3, 5)}))

    c7 = cycle(list(range(7)))
    out.append(("C7_plus_chord_02", c7 | {(0, 2)}))
    out.append(("C7_plus_chords_02_03", c7 | {(0, 2), (0, 3)}))
    out.append(("C7_plus_chords_02_24_46", c7 | {(0, 2), (2, 4), (4, 6)}))
    out.append(("C7_triangulated_fan", c7 | {(0, 2), (0, 3), (0, 4), (0, 5)}))

    # A K4 with three different edges subdivided once; degrees are 2 and 3.
    subdivided = {(0, 4), (4, 1), (0, 5), (5, 2), (0, 6), (6, 3)}
    subdivided |= {(1, 2), (1, 3), (2, 3)}
    out.append(("K4_three_incident_edges_subdivided", subdivided))

    out.append(("K7_minus_edge", all_edges - {(0, 1)}))
    out.append(("K7_minus_matching2", all_edges - {(0, 1), (2, 3)}))
    out.append(("K7_minus_path2", all_edges - {(0, 1), (1, 2)}))

    # Preserve names even if two hand descriptions accidentally yield isomorphic graphs.
    return [(name, mask_of(edges)) for name, edges in out]


def main():
    started = time.time()
    rows = []
    counterexamples = []
    for name, mask in candidates():
        adj = graph_adjacency(N, mask)
        states, state_index, F, holes = fs_graph(adj)
        f_connected = component_size(F) == len(F)
        degrees = list(map(len, adj))
        delta = min(degrees)
        row = {
            "name": name,
            "mask": mask,
            "edges": sum(degrees) // 2,
            "degrees": degrees,
            "FS_connected": f_connected,
            "same_hole_pairs_checked_after_symmetry": 0,
        }
        if not f_connected:
            rows.append(row)
            print(json.dumps(row), flush=True)
            continue
        aut = automorphisms(N, mask)
        high = [v for v in range(N) if degrees[v] > delta]
        source_holes = orbit_representatives(high, aut)
        row["automorphism_group_order"] = len(aut)
        row["high_hole_orbit_representatives"] = source_holes
        for source_hole in source_holes:
            sigma = canonical_start(N, source_hole)
            s = state_index[sigma]
            targets = target_orbit_representatives(
                states, state_index, sigma, source_hole, aut, {source_hole}
            )
            row["same_hole_pairs_checked_after_symmetry"] += len(targets)
            for t in targets:
                value, separator, adjacent = local_connectivity(
                    F, s, t, degrees[source_hole]
                )
                assert not adjacent  # one move changes the hole position
                if value < degrees[source_hole]:
                    record = graph_record(N, mask, adj)
                    record.update({
                        "name": name,
                        "sigma": list(sigma),
                        "rho": list(states[t]),
                        "hole": source_hole,
                        "endpoint_degree": degrees[source_hole],
                        "local_vertex_connectivity": value,
                        "separator_state_indices": separator,
                        "separator_states": [list(states[v]) for v in separator],
                    })
                    counterexamples.append(record)
                    result = {"rows": rows + [row], "counterexamples": counterexamples}
                    Path(__file__).with_name("search_n7_candidates.json").write_text(
                        json.dumps(result, indent=2) + "\n", encoding="utf-8"
                    )
                    print(json.dumps(record, indent=2), flush=True)
                    return
        rows.append(row)
        print(json.dumps(row), flush=True)
    result = {
        "scope": "selected high-risk n=7 graphs; same-hole pairs only",
        "rows": rows,
        "total_pairs_after_symmetry": sum(r["same_hole_pairs_checked_after_symmetry"] for r in rows),
        "counterexamples": counterexamples,
        "elapsed_seconds": time.time() - started,
    }
    Path(__file__).with_name("search_n7_candidates.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "graphs": len(rows),
        "total_pairs_after_symmetry": result["total_pairs_after_symmetry"],
        "counterexamples": counterexamples,
        "elapsed_seconds": result["elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
