# Problem

Let `Q(G)=D(G)+A(G)` be the signless Laplacian matrix of a graph `G`, and let `q(G)` be the spectral radius of `Q(G)`.

For integers `2 <= s <= t`, let `K_{s,t}^+` denote the graph obtained from the complete bipartite graph `K_{s,t}` by adding one edge inside the partite class of size `s`. The source uses the standard non-induced meaning of `F`-free: a graph is `F`-free when it has no subgraph isomorphic to `F`.

The public case concerns Conjecture 5.1 in the cited paper. In paraphrase, the conjecture states:

> If `2 <= s <= t`, `n >= s+t`, and `G` is an `n`-vertex `K_{s,t}^+`-free graph with maximum signless-Laplacian spectral radius, then `G` is a member of `L_{n,s,t}` or `Y_{n,t}`.

The family `L_{n,s,t}` is defined as a join of `K_{s-1}` with a nearly `(t-1)`-regular triangle-free graph on `n-s+1` vertices. The family `Y_{n,t}` is defined as a join of `I_{t-1}` with a nearly `(t-1)`-regular triangle-free graph on `n-t+1` vertices.

## Released Scope

This package treats only the boundary case

```text
s = t = 3, n = 6.
```

In this case the auxiliary triangle-free graph appearing in either family has order four and is 2-regular, so it is a copy of `C4`.

The case gives a graph that is `K_{3,3}^+`-free, has maximum Q-index among all six-vertex `K_{3,3}^+`-free graphs, and is not isomorphic to the corresponding `L_{6,3,3}` or `Y_{6,3}` graph. Because the printed conjecture quantifies over every `n >= s+t`, this single boundary example disproves the exact printed statement.

## Non-Claims

- The package does not claim to classify all extremal `K_{s,t}^+`-free graphs.
- The package does not address a modified conjecture with an added sufficiently-large-`n` hypothesis.
- The package does not claim novelty, first discovery, or public priority.
