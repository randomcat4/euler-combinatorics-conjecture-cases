# Problem

Question 15 of Axenovich, Liu, and Sagdeev asks for necessary and sufficient
conditions for a finite graph to admit an induced unit-copy in an orthogonal
copy of a tree.

Equivalently, assign each tree edge a positive squared length. A graph is
orthogonal-tree representable when its vertices can be marked on the tree so
that two marked vertices are adjacent exactly when their weighted tree distance
is `1`.

## Public Scope

This case proves a strict partial result:

```text
The induced-obstruction rule "avoid the gem, the house, and K4 plus a
degree-two vertex" is not sufficient for orthogonal-tree representability.
```

It gives two seven-vertex graphs, `H_adj` and `H_dis`, that satisfy all three
avoidance conditions but are not orthogonal-tree representable. Each proper
induced subgraph is representable, so both examples are induced-minimal
obstructions beyond the three five-vertex examples.

The case does not answer the full characterization problem in Question 15. It
does not assert that the two displayed graphs are the only seven-vertex
obstructions, and it does not classify the non-prime seven-vertex tier.

## Source Locator

- Maria Axenovich, Dingyuan Liu, and Arsenii Sagdeev, *Ramsey problems for
  graphs in Euclidean spaces and Cartesian powers*, arXiv:2512.15516v2.
- Location: Appendix B.2, "Orthogonal trees", Question 15, physical PDF
  page 27.

The exact old-obstruction names used in this case are the gem, the house, and
`HVN`, where `HVN` is `K4` plus a degree-two vertex.
