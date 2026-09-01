# Problem

## Primary Source

Nawaf Shafi Alshammari, Sergey Kitaev, and Artem Pyatkin, "On the
representation number of grid graphs and cylindric grid graphs,"
arXiv:2507.16469v1.

The source statement used here is Conjecture 1 in Section 4, Open problems,
on physical PDF page 10. It states that if `m,n >= 3` and `m+n >= 8`, then
`R(TGr_{m,n}) >= 4`.

## Definitions

A word over the vertex set of a graph represents the graph when, for every two
distinct vertices `a,b`, the subword obtained by deleting all symbols other
than `a` and `b` alternates if and only if `{a,b}` is an edge.

A `k`-word representation is such a word in which every vertex appears exactly
`k` times. The representation number `R(G)` is the least `k` for which `G` has
a `k`-word representation.

For `m,n >= 3`, the toroidal grid graph is

```text
TGr_{m,n}=C_m square C_n.
```

## Public Scope

This case treats only the parameter pair

```text
(m,n) = (3,5).
```

For this graph, `TGr_{3,5}=C_3 square C_5`, the public certificate gives a
3-word representation. Because `(3,5)` satisfies the source hypotheses
`m,n >= 3` and `m+n=8`, the certificate disproves the exact printed universal
claim.

## Non-Claims

- No value of `R(TGr_{3,5})` beyond the upper bound `R(TGr_{3,5}) <= 3` is claimed.
- No toroidal grid other than `TGr_{3,5}` is classified.
- No statement is made about a future corrected, weakened, or asymptotic version of the conjecture.
- Public priority and novelty are not established.
