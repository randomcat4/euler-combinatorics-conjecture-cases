# Problem Statement and Scope

## Source Problem

Alon and Wei's Conjecture 1.2 asks for a spanning subgraph whose largest degree
multiplicity is bounded in terms of the number of vertices and the minimum
degree. Ma and Xie restate the same one-sided form as Conjecture 5.4.

For a finite simple graph `G=(V,E)` and a spanning subgraph `H=(V,F)`, define

```text
m(H,j) = |{v in V : deg_H(v)=j}|
```

for each integer `j>=0`.

## Released Statement

This case proves the following exact slice.

For every finite simple graph `G` on `n>=3` vertices with `delta(G)=2`, there
exists a spanning subgraph `H` of `G` such that

```text
m(H,j) <= floor(n/3) + 2
```

for every integer `j>=0`.

The integer form is equivalent to the real-valued source bound at
`delta(G)=2`, because each `m(H,j)` is an integer.

## Scope Boundary

This case is not a proof of the full Alon--Wei minimum-degree conjecture. In
particular, it does not claim the stronger right-hand side

```text
n/(delta(G)+1) + 2
```

for graphs with `delta(G)>2`.

The proof does not assume regularity, connectedness, planarity, bounded maximum
degree, or two-connectedness. The spanning subgraph `H` may be empty or
disconnected.

## Sharpness Boundary

The graph `2C4`, the disjoint union of two four-cycles, shows that the integer
bound cannot be lowered from `4` to `3` at `n=8`. This is a sharpness
certificate for the additive constant in this slice; it is not a classification
of all extremal graphs.
