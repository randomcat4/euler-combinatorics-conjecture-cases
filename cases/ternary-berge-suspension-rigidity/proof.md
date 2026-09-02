# Proof

Throughout, `H` is a finite normalized hypergraph and `I(H)` is its independence
complex. Write `Sigma X` for the unreduced suspension of a finite simplicial
complex `X`.

## Lemma 1: Graphification Determines Integral Homology

Let `H` have nonempty vertex set and no ternary Berge cycle, and put
`K=I(H)`. There are an integer `r >= 0` and a graph `G` such that

```text
I(G) ~= Sigma^r K,
```

and `G` has no cycle whose length is divisible by three.

Indeed, if a hyperedge `e` has size at least three, replace it by Kim's
edge-star expansion. Lemma 5.1 of arXiv:2408.14321v2 gives
`I(H_e) ~= Sigma I(H)`, while Corollary 5.3 says that the expanded hypergraph
still has no ternary Berge cycle. The expansion deletes one edge of size at
least three and adds only two-edges, so iterating over the large edges
terminates at a graph `G`.

In a graph, Berge cycles are ordinary cycles. Thus `G` has no cycle of length
divisible by three, and in particular has no induced cycle of such a length.
Kim's graph theorem, arXiv:2101.07131v3, Theorem 1.1, implies that `I(G)` is
contractible or homotopy equivalent to a sphere.

Reduced integral suspension homology now descends along
`I(G) ~= Sigma^r K`. Therefore `K` is integrally acyclic or has the reduced
integral homology of exactly one sphere. If `r=0`, this is the graph theorem
itself. If `r>0` and `I(G) ~= S^d`, then `K` is nonempty and `Sigma^r K` has no
reduced homology below degree `r`, so `d >= r`; the descended sphere dimension
is `d-r >= 0`. No torsion is hidden in this step, because the input is the full
homotopy type of `I(G)`, not a Betti-rank bound.

## Lemma 2: The Disconnected Case Is `S^0`

Assume that `H` is normalized and has no Berge 3-cycle. If `I(H)` is
disconnected, then it is the disjoint union of two simplices, hence is homotopy
equivalent to `S^0`.

Connectivity of a simplicial complex is connectivity of its one-skeleton. If
vertices `x` and `y` lie in different components of `I(H)`, then `{x,y}` is not
a face. Since both singletons are faces and the hyperedges of normalized `H`
are precisely the minimal nonfaces, `{x,y}` is a two-edge of `H`.

There cannot be three components: choosing one vertex in each component would
give three distinct two-edges among them, forming a Berge triangle. Hence there
are exactly two components, on vertex sets `A` and `B`.

If the component on `A` were not a simplex, it would contain a minimal nonface
`e` with at least two vertices. Choose distinct `a_1,a_2 in e` and a vertex
`b in B`. The three distinct hyperedges

```text
e, {a_2,b}, {b,a_1}
```

with cycle vertices `a_1,a_2,b` form a Berge 3-cycle, a contradiction. The
component on `A` is therefore a simplex, and the same argument applies to `B`.

## Lemma 3: Suspension Rigidity

Let `X` and `Y` be finite simplicial complexes, with `X` connected and
`X ~= Sigma Y`. Suppose either:

1. `X` is integrally acyclic; or
2. `X` has the reduced integral homology of `S^n` for some `n >= 1`.

Then `X` is contractible in the first case and `X ~= S^n` in the second.

Reduced integral suspension homology gives
`H~_{i+1}(X;Z) = H~_i(Y;Z)`.

If `X` is acyclic, then `Y` is connected and acyclic. The suspension `Sigma Y`
is simply connected and acyclic, so the homology Whitehead theorem makes it
contractible.

If `n >= 2`, then `Y` is connected, hence `X` is simply connected and has the
integral homology of `S^n`. The least-nonzero-homotopy form of the Hurewicz
theorem shows that `X` is `(n-1)`-connected. Hurewicz then identifies
`pi_n(X)` with `H_n(X;Z)=Z`; a map `S^n -> X` representing a generator is a
homology equivalence between simply connected CW complexes, hence a homotopy
equivalence by homology Whitehead.

It remains to consider `n=1`. Then `H~_0(Y;Z)=Z` and all higher reduced
homology groups of `Y` vanish. Thus `Y` has exactly two connected integrally
acyclic components `Y_1` and `Y_2`. The standard splitting

```text
Sigma(Y_1 disjoint-union Y_2) ~= S^1 wedge Sigma Y_1 wedge Sigma Y_2
```

applies. Each `Sigma Y_i` is simply connected and acyclic, hence contractible
by the acyclic case. Therefore `X ~= S^1`.

## Theorem

If a finite hypergraph `H` has no Berge cycle whose length is divisible by
three, then `I(H)` is contractible or homotopy equivalent to a sphere.

Normalize `H` as in the source. If the normalized vertex set is empty, this is
the conventional `S^{-1}` case. If `H` has an isolated vertex, `I(H)` is a cone
and is contractible. We may therefore assume that the normalized vertex set is
nonempty and that `H` has no isolated vertex.

If every hyperedge has size two, then `H` is a graph with no cycle whose length
is divisible by three. The result follows directly from Kim's graph theorem.

Now assume that some hyperedge has size at least three, and put `K=I(H)`.
Lemma 1 says that `K` is integrally acyclic or an integral homology sphere. If
`K` is disconnected, Lemma 2 gives `K ~= S^0`.

It remains that `K` is connected. Choose any vertex `v`. It is nonisolated, and
the hypothesis excludes every Berge 3-cycle, so in particular `v` lies in no
induced Berge 3-cycle. Kim's star-cluster suspension theorem,
arXiv:2408.14321v2, Theorem 1.3, supplies a finite hypergraph `H'` with

```text
K ~= Sigma I(H').
```

Lemma 3 applies. It makes `K` contractible in the acyclic case and homotopy
equivalent to a sphere in the integral-homology-sphere case. This proves
Question 5.5.

## Boundary Checks

- Edge-star expansion is iterated only in the direction covered by Kim's
  Lemma 5.1 and Corollary 5.3.
- Star dissolution is not iterated. The closure obstruction noted in Kim's
  Remark 5.6 is therefore not used as a false induction hypothesis.
- The graph theorem is applied to a graph with no divisible-by-three cycle at
  all, which is stronger than the required absence of induced such cycles.
- The homology descent uses integral coefficients.
- The earlier finite no-hit enumeration is not a premise of the proof.
