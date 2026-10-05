#!/usr/bin/env python3
"""Construct and exactly audit the fixed-hole quotient J used for star friends-and-strangers graphs."""

from __future__ import annotations

from collections import deque
from itertools import permutations
import json
from pathlib import Path

from search_fs import (
    automorphisms, canonical_start, component_size, fs_graph, graph_adjacency,
    local_connectivity, orbit_representatives, target_orbit_representatives,
    unlabeled_connected_graphs,
)
from search_n7_candidates import candidates as n7_candidates


def quotient_graph(states, state_index, F, holes, h):
    T_global = [i for i, x in enumerate(holes) if x == h]
    T_set = set(T_global)
    t_local = {x: i for i, x in enumerate(T_global)}
    comp = [-1] * len(F)
    representatives = []
    sizes = []
    count = 0
    for start in range(len(F)):
        if start in T_set or comp[start] >= 0:
            continue
        comp[start] = count
        queue = [start]
        for u in queue:
            for v in F[u]:
                if v not in T_set and comp[v] < 0:
                    comp[v] = count
                    queue.append(v)
        representatives.append(start)
        sizes.append(len(queue))
        count += 1

    J = [set() for _ in range(len(T_global) + count)]
    collision_rows = []
    for x in T_global:
        multiplicities = {}
        for y in F[x]:
            assert y not in T_set
            c = comp[y]
            multiplicities[c] = multiplicities.get(c, 0) + 1
        repeated = {c: m for c, m in multiplicities.items() if m > 1}
        if repeated:
            collision_rows.append({"T_state": list(states[x]), "multiplicities": repeated})
        a = t_local[x]
        for c in multiplicities:
            b = len(T_global) + c
            J[a].add(b)
            J[b].add(a)
    return {
        "T_global": T_global,
        "T_local": t_local,
        "component_of_global_state": comp,
        "component_representatives": representatives,
        "component_sizes": sizes,
        "J": [sorted(x) for x in J],
        "collisions": collision_rows,
    }


def leaf_orbits(states, state_index, quotient, n):
    leaf_perms = list(permutations(range(n - 1)))
    actions = [p + (n - 1,) for p in leaf_perms]

    def act(state, psi):
        return tuple(psi[token] for token in state)

    first_t = quotient["T_global"][0]
    t_orbit = {state_index[act(states[first_t], psi)] for psi in actions}
    comp = quotient["component_of_global_state"]
    first_b = quotient["component_representatives"][0]
    b_orbit = {comp[state_index[act(states[first_b], psi)]] for psi in actions}
    assert -1 not in b_orbit
    return len(t_orbit), len(b_orbit)


def audit_one(name, n, mask, h, adj, states, state_index, F, holes, aut):
    qdata = quotient_graph(states, state_index, F, holes, h)
    J = qdata["J"]
    D = len(adj[h])
    Tn = len(qdata["T_global"])
    Bn = len(qdata["component_representatives"])
    assert Tn == math_factorial(n - 1)
    assert component_size(J) == len(J)
    t_degrees = sorted({len(J[i]) for i in range(Tn)})
    b_degrees = sorted({len(J[Tn + i]) for i in range(Bn)})
    q_value = Tn // Bn if Tn % Bn == 0 else None
    t_orbit, b_orbit = leaf_orbits(states, state_index, qdata, n)

    sigma = canonical_start(n, h)
    sigma_global = state_index[sigma]
    sigma_local = qdata["T_local"][sigma_global]
    target_globals = target_orbit_representatives(
        states, state_index, sigma, h, aut, {h}
    )
    min_value = D
    counterexample = None
    for target_global in target_globals:
        target_local = qdata["T_local"][target_global]
        value, separator, adjacent = local_connectivity(J, sigma_local, target_local, D)
        assert not adjacent
        min_value = min(min_value, value)
        if value < D:
            decoded = []
            for x in separator:
                if x < Tn:
                    decoded.append({"side": "T", "state": list(states[qdata["T_global"][x]])})
                else:
                    c = x - Tn
                    decoded.append({
                        "side": "B",
                        "component": c,
                        "component_size": qdata["component_sizes"][c],
                        "representative_state": list(states[qdata["component_representatives"][c]]),
                    })
            counterexample = {
                "sigma": list(sigma),
                "rho": list(states[target_global]),
                "value": value,
                "D": D,
                "separator": decoded,
            }
            break
    row = {
        "name": name,
        "n": n,
        "mask": mask,
        "hole": h,
        "hole_degree_D": D,
        "T_vertices": Tn,
        "B_vertices": Bn,
        "q_T_over_B": q_value,
        "J_vertices": len(J),
        "J_edges": sum(map(len, J)) // 2,
        "contraction_parallel_edge_collisions": len(qdata["collisions"]),
        "T_degree_set": t_degrees,
        "B_degree_set": b_degrees,
        "expected_B_degree_Dq": None if q_value is None else D * q_value,
        "leaf_relabel_T_orbit_size": t_orbit,
        "leaf_relabel_B_orbit_size": b_orbit,
        "same_T_side_pair_orbits_checked": len(target_globals),
        "minimum_local_connectivity_seen": min_value,
        "counterexample": counterexample,
    }
    return row


def math_factorial(k):
    answer = 1
    for x in range(2, k + 1):
        answer *= x
    return answer


def main():
    rows = []
    # Exhaust all connected unlabeled X through n=6, retaining connected FS and
    # one representative of every high-degree hole orbit.
    for n in range(4, 7):
        for mask in unlabeled_connected_graphs(n):
            adj = graph_adjacency(n, mask)
            states, state_index, F, holes = fs_graph(adj)
            if component_size(F) != len(F):
                continue
            degree = list(map(len, adj))
            delta = min(degree)
            aut = automorphisms(n, mask)
            high_holes = [v for v in range(n) if degree[v] > delta]
            for h in orbit_representatives(high_holes, aut):
                row = audit_one(f"all_n{n}_mask{mask}", n, mask, h, adj,
                                states, state_index, F, holes, aut)
                rows.append(row)
                if row["counterexample"] is not None:
                    break

    # Selected high-risk n=7 structures from search_n7_candidates.py.
    for name, mask in n7_candidates():
        n = 7
        adj = graph_adjacency(n, mask)
        states, state_index, F, holes = fs_graph(adj)
        if component_size(F) != len(F):
            continue
        degree = list(map(len, adj))
        delta = min(degree)
        aut = automorphisms(n, mask)
        high_holes = [v for v in range(n) if degree[v] > delta]
        for h in orbit_representatives(high_holes, aut):
            row = audit_one(name, n, mask, h, adj, states, state_index, F, holes, aut)
            rows.append(row)
            print(json.dumps(row), flush=True)
            if row["counterexample"] is not None:
                break

    violations = [r for r in rows if (
        r["contraction_parallel_edge_collisions"] != 0 or
        r["T_degree_set"] != [r["hole_degree_D"]] or
        r["q_T_over_B"] is None or
        r["B_degree_set"] != [r["expected_B_degree_Dq"]] or
        r["leaf_relabel_T_orbit_size"] != r["T_vertices"] or
        r["leaf_relabel_B_orbit_size"] != r["B_vertices"] or
        r["minimum_local_connectivity_seen"] != r["hole_degree_D"]
    )]
    result = {
        "scope": "all connected-FS high-hole orbits for unlabeled X on n=4..6, plus selected high-risk n=7 X",
        "rows": rows,
        "row_count": len(rows),
        "violations": violations,
    }
    target = Path(__file__).with_name("quotient01.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "row_count": len(rows),
        "violations": violations,
    }, indent=2))
    if violations:
        raise RuntimeError("Quotient verification found a mathematical violation")


if __name__ == "__main__":
    main()
