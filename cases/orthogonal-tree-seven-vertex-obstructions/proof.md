# Proof

## Tree-Metric Model

In an orthogonal copy of a tree, give every tree edge its own coordinate
direction and let `w_f>0` be the squared Euclidean length of edge `f`. For tree
vertices `u` and `v`,

```text
||u-v||^2 = sum w_f over f in the tree path P(u,v).
```

Thus induced unit-copies in orthogonal trees are exactly equality graphs at
value `1` in positive weighted tree metrics.

## Exact Even Leaf Powers

For graphs with at least two vertices, orthogonal-tree representability is
equivalent to being an exact `k`-leaf power for some even integer `k`.

The reverse direction is direct. Given an unweighted exact even-`k` leaf root,
assign squared weight `1/k` to every tree edge and embed distinct tree edges in
orthogonal coordinate directions.

For the forward direction, start with a positive weighted-tree representation
and restrict to the minimal subtree spanning the marked vertices. The edge
equations

```text
sum_{f in P(u,v)} w_f = 1
```

for graph edges have rational coefficients. The positive solutions avoiding
all nonedge equations are a nonempty relatively open subset of a rational
affine space; in dimension zero the unique solution is rational, and otherwise
rational points are dense. Hence the representation may be chosen with
positive rational weights and with every nonedge path sum different from `1`.

Clear denominators by a positive integer `M`. Replace each weighted edge `f` by
a path of `2M w_f` unit edges, and attach one new unit pendant edge at each
marked vertex. The resulting tree has exactly those pendant endpoints as
leaves, and the distance between leaves corresponding to old marked vertices
`u,v` is

```text
2M d(u,v) + 2.
```

This equals the even integer `2M+2` exactly when `d(u,v)=1`, so the graph is an
exact even leaf power.

## The Two Graphs

Let `H_adj` have vertex set `{0,1,2,3,4,5,6}` and edge set

```text
{05, 06, 14, 16, 23, 25, 34, 46, 56}.
```

This is a chordless five-cycle with triangle ears on two adjacent carrier
edges. Its graph6 string is `F@UeW`.

Let `H_dis` have the same vertex set and edge set

```text
{05, 06, 14, 16, 23, 25, 34, 35, 46}.
```

This is the corresponding chordless five-cycle with triangle ears on two
disjoint carrier edges. Its graph6 string is `F@UuO`.

The public checker confirms the graph6 strings, edge sets, canonical
bitstrings, and absence of induced gem, house, or `HVN`.

## Unit-Triangle Lemma

Recall the four-point condition for a tree metric: for any four points, the
largest of

```text
d(1,2)+d(3,4), d(1,3)+d(2,4), d(1,4)+d(2,3)
```

occurs at least twice.

Suppose `u,v,w` are pairwise at distance `1`, while `z` is at distance `1` from
`u` and at nonunit distance from `v` and `w`. Let
`alpha=d(z,v)` and `beta=d(z,w)`. Applying the four-point condition to
`u,v,w,z` gives the three sums

```text
2, 1+alpha, 1+beta.
```

If `alpha` and `beta` differed, the largest sum would be unique unless the
larger of `alpha,beta` were `1`, which is excluded. Thus `alpha=beta`. Their
common value cannot be below `1`, because then `2` would be the unique maximum,
and it cannot equal `1`. Hence `d(z,v)=d(z,w)>1`.

Geometrically, if `m` is the median of the unit triangle, every arm from `m` to
one of its corners has length `1/2`. The same lemma forces `z` into the
component of `T-m` containing `u`, with `d(z,m)>1/2`.

## Nonrepresentability of `H_adj`

Use the labeling `(a,b,c,d,e,x,y)=(5,2,3,4,6,0,1)`. Then `H_adj` has chordless
cycle

```text
a-b-c-d-e-a
```

and triangle ears `aex` and `dey`.

Assume that a positive weighted tree metric represents `H_adj`. Set

```text
p=d(a,c), q=d(a,d), r=d(b,d), s=d(b,e), t=d(c,e).
```

The unit-triangle lemma gives `q>1`, `s>1`, and `t>1`: respectively use vertex
`d` against triangle `aex`, vertex `b` against triangle `aex`, and vertex `c`
against triangle `dey`.

Apply the four-point condition:

- On `{a,b,c,d}`, the sums are `2`, `p+r`, and `q+1>2`, so `p+r=q+1`.
- On `{a,b,d,e}`, the sums are `2`, `q+s`, and `1+r`, so `1+r=q+s`.
- On `{a,b,c,e}`, the sums are `1+t>2`, `p+s`, and `2`, so `p+s=1+t`.

The first two equations give `s=2-p`. Substituting into the third gives
`1+t=p+s=2`, so `t=1`, contradicting `t>1`. Therefore `H_adj` is not
orthogonal-tree representable.

## Nonrepresentability of `H_dis`

Use the numeric labeling. The triples `(2,3,5)` and `(1,4,6)` are unit
triangles. Let their tree medians be `L` and `R`.

Vertex `4` is at unit distance from `3` and at nonunit distance from `2` and
`5`. The geometric form of the unit-triangle lemma puts `4` in the `3`-branch
at `L` and gives `d(4,L)>1/2`. Since `d(4,R)=1/2`, the medians are distinct,
and `R` must lie in the same `3`-branch at `L`.

Symmetrically, because `3` is at unit distance from `4` and at nonunit distance
from `1` and `6`, the point `L` lies in the `4`-branch at `R`.

Now `0` is at unit distance from `5` and at nonunit distance from `2` and `3`,
so `0` lies in the `5`-branch at `L`. Since `R` is in the distinct `3`-branch,
the path from `0` to `R` passes through `L`:

```text
d(0,R)=d(0,L)+d(L,R).
```

On the other hand, `0` is at unit distance from `6` and at nonunit distance
from `1` and `4`, so `0` lies in the `6`-branch at `R`. Since `L` is in the
distinct `4`-branch, the path from `0` to `L` passes through `R`:

```text
d(0,L)=d(0,R)+d(L,R).
```

The two equations force `d(L,R)=0`, contradicting `L != R`. Therefore `H_dis`
is not orthogonal-tree representable.

## Induced Minimality

The public checker confirms that every five-vertex induced subgraph of each
displayed graph avoids the gem, house, and `HVN`. The frozen six-vertex census
in the source work says that every graph on at most six vertices avoiding those
three old obstructions is representable. The certificate included here also
contains explicit positive rational weighted-tree witnesses for each one-vertex
deletion, and the checker verifies those witness distance tables exactly.

Thus every proper induced subgraph of `H_adj` and `H_dis` is representable,
while neither graph itself is representable. Both are induced-minimal
seven-vertex obstructions.

## Computational Boundary

The symbolic arguments above are the primary nonrepresentability proofs. The
source work also checked a complete reduced seven-marked topology denominator
of 143,816 objects for each graph over exact rational arithmetic. The retained
public certificate records the denominator hashes and blocker counts. This
corroborates the proof but does not extend the public scope to a full
seven-vertex classification.
