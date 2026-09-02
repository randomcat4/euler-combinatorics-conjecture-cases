# Problem

Let `H=(V,E)` be a finite hypergraph. A Berge cycle of length `k` consists of
`k` distinct vertices and `k` distinct hyperedges, with each hyperedge
containing the corresponding consecutive pair of cycle vertices. A ternary
Berge cycle is a Berge cycle whose length is divisible by three.

The independence complex `I(H)` is the simplicial complex of vertex subsets that
contain no hyperedge of `H`.

Kim's Question 5.5 asks whether the following statement is true:

```text
If H has no ternary Berge cycle, then I(H) is contractible or homotopy
equivalent to a sphere.
```

The source paper uses the standard normalization in which redundant nonminimal
edges are deleted and singleton edges are removed together with their vertices.
These operations preserve the independence complex, up to the source's
empty-complex convention, and cannot create a Berge cycle.

## Public Scope

This case proves the complete question for all finite hypergraphs satisfying
the source definitions and normalization. It adds no assumptions of linearity,
uniformity, acyclicity, rank, connectedness, or bounded vertex count.

For a nonempty normalized vertex set, the resulting sphere has dimension at
least zero. The empty normalized vertex set is treated as the conventional
augmented `S^{-1}` case. An edgeless nonempty hypergraph has an isolated vertex,
so its independence complex is a simplex and is contractible.

## Source Locator

- Jinha Kim, *Topology of Independence Complexes and Cycle Structure of
  Hypergraphs*, arXiv:2408.14321v2, Section 5.1, Question 5.5, physical PDF
  page 13.
- DOI: <https://doi.org/10.1007/s00493-026-00198-y>.

The proof also uses Kim's graph theorem on independence complexes of ternary
graphs, arXiv:2101.07131v3, Theorem 1.1.
