# Proof

We prove the following theorem.

**Theorem.** Let `G` be a finite simple graph on `n>=3` vertices with
`delta(G)=2`. Then `G` has a spanning subgraph `H` such that

```text
m(H,j) <= B := floor(n/3) + 2
```

for every integer `j>=0`.

Throughout, all subgraphs are spanning subgraphs unless explicitly stated
otherwise.

## 1. Thread Words

Let a path thread have internal vertices `x_1,...,x_l`, where `l>=1`, and let
the selected or unselected physical edges along the thread be encoded by a
binary word

```text
y_0 y_1 ... y_l in {0,1}^{l+1}.
```

The internal vertex `x_i` has degree `y_{i-1}+y_i`. Hence the number of degree
one internal vertices is exactly the number of transitions in the word.

For fixed endpoint bits `alpha,beta` and a nonnegative triple `(c0,q,c2)`,
there is such a word with `c_i` internal vertices of degree `i` and `q` degree
one internal vertices if and only if either:

- `q=0` and the word is constant, giving `(l,0,0)` or `(0,0,l)`;
- `q>=1`, `q == alpha xor beta mod 2`, and `c0` can be any integer from `0` to
  `l-q`, with `c2=l-q-c0`.

This is the usual run decomposition of a binary word. If the word is not
constant, the run endpoints force the parity of the number of transitions; once
that transition count is fixed, extra zero-runs and one-runs can absorb the
remaining `l-q` internal adjacencies in all possible splits.

## 2. The Positive-Thread Pseudokernel Lemma

We need a constructive lemma for graphs obtained by subdividing all edges of a
kernel.

**Lemma 2.1.** Let `Q` be a finite pseudograph, possibly disconnected and
possibly with parallel edges and loops. Loops count twice toward degree, and
`delta(Q)>=3`. Replace every non-loop edge by a path with `l_e>=1` internal
degree-two vertices, and every loop by a closed thread based at its kernel
vertex with `l_e>=2` internal degree-two vertices. If the expanded graph has
`N` vertices, then it has a spanning subgraph whose degree `0`, `1`, and `2`
classes all have size at most `floor(N/3)+2`.

**Proof.** The construction is a finite-state selection of endpoint bits and
thread words.

For every kernel half-edge choose an endpoint bit. Each thread is then put into
one of six states:

```text
C0  endpoint bits 00, constant zero
E0  endpoint bits 00, active even transitions
O   endpoint bits 01 or 10, active odd transitions
E2  endpoint bits 11, active even transitions
C2  endpoint bits 11, constant one
```

For a loop, the two endpoint bits are still the two distinct physical half-edge
positions of the closed thread. Thus an `O` loop contributes one selected
half-edge to its base vertex, while `C2` and `E2` contribute two. The condition
`l_e>=2` is exactly what makes the same-end active states available for loops.

Let `t=|V(Q)|`, `m=|E(Q)|`, `L=sum_e l_e`, and

```text
B = floor((L+t)/3) + 2.
```

For a fixed six-state choice, let `lambda_v` be the number of selected incident
half-edges at `v`, and let

```text
d_i = |{v : lambda_v=i}|,          i=0,1,2,
P_i = sum_{e in C_i} l_e,          i=0,2.
```

Let `q^-` and `q^+` be the minimum and maximum possible total transition counts
over all active threads, with the forced parity. By the run-word lemma, the
possible total transition counts are exactly the parity interval
`{q^-, q^-+2, ..., q^+}`.

Therefore a fixed state choice is feasible exactly when

```text
d_0 + P_0 <= B,
d_2 + P_2 <= B,
[max(q^-, L-2B+d_0+d_2), min(q^+, B-d_1)] contains an integer
with the forced parity.
```

Necessity is immediate from the three degree classes. For sufficiency, choose
such a transition total. The interval-sum property distributes it among active
threads. The remaining active internal vertices can then be split between
degree zero and degree two, again by the run-word lemma, to fill the remaining
two capacities.

It remains to produce a six-state choice satisfying this criterion. First
delete the kernel loops and orient the non-loop multigraph so that every vertex
not incident with a loop has indegree different from one. To see this, attach a
new vertex by three parallel edges to every loop-bearing vertex, apply the
standard no-indegree-one orientation lemma to the resulting loopless multigraph
of minimum degree at least three, and then delete the auxiliary vertices. Put
all non-loop edges in the corresponding `O` state and all loops in `O`.
If a loop-bearing vertex now has load one, it has exactly one loop and no
non-loop indegree; changing that loop from `O` to `E2` changes the load from
one to two. Thus initially `d_1=0`, except for these isolated active `E2` loop
repairs.

When `m<=B` and the resulting load parameter already lies above the lower
threshold, the full parity interval criterion finishes directly: the lower
transition count is at most `B`, the endpoint load classes have size at most
`t<=2m/3<=B`, and the upper transition count remains above the two-box lower
bound because at most `m` threads lose one endpoint from parity.

Otherwise a platform step increases the number of rigid states until the load
parameter reaches `r+2` or `r+3`, where `r=m-B`. The available platform set is
the union of all loops and all non-loop threads of length at most two. This set
cannot get stuck before the threshold: if the remaining platform edges formed a
matching, then

```text
L >= 3m - 2s + h,
t >= 2(s-k),
```

where `s` is the platform size, `h` the number of loops, and `k` the current
number of rigid platform edges. Since `L+t=3B-eta` with `eta in {4,5,6}`, this
would force `2k >= 3r+eta+h`, contradicting the pre-threshold bound
`k<=r+1`. Thus a loop, a safe short edge, or two adjacent short edges can
always be flipped while keeping `d_1=0`.

At the first platform state with load parameter `r+p`, `p in {2,3}`, the two
rigid boxes cannot both exceed `B`. The exact slack identity is

```text
2B-(A_0+A_2) =
eta-p + unused_length_excess + high_load_credit,
```

where `A_i=P_i+d_i`. Hence there is either no bad box, or exactly one bad box.
If there is no bad box, the minimum-transition form of the parity criterion
applies.

If the zero box is bad, order the short `C0` edges so that, at every prefix,
at most two zero-load vertices with no outgoing `O` root have prefix degree
one. Such an order is obtained greedily: follow an existing degree-one
frontier when it exists; otherwise take any unused edge. Flipping a prefix
from `C0` to `C2` releases zero-box mass. Vertices that have an outgoing
`O` root and become degree one can choose either to remain a one-load vertex
or to flip one outgoing root to `C2`; these choices give all needed parities in
the interval `[-p,0]` and keep the overshoot within the slack above. If the
edge prefix alone does not release enough, isolated zero-load vertices are
handled one at a time by flipping an outgoing root, which releases exactly one
unit. The total-box identity charges every long root to its own previously
unused length excess, so the opposite box remains within `B`.

If the two box is bad, first move any still-active loop repairs from `E2` to
`E0` until either the excess disappears or all such repairs are used. These
loop repairs are isolated at their base vertices. Then order the rigid `C2`
edges by putting loops first and using the same two-frontier greedy rule for
the remaining short non-loop edges. Along the complement process, flipping
unused `C2` mass toward `C0` releases the two box. A long rigid loop is not
treated as one indivisible short edge: it is passed through the intermediate
state `C0 -> E2 -> C2`, and the active intermediate state releases exactly the
same length mass that would otherwise cause a large jump. Thus any first
undershoot is paid for by the loop itself. After the edge phase, temporarily
closed incoming roots to original two-load vertices are reopened one at a
time, each decreasing the release by exactly one without changing the load
parameter. The same slack identity then keeps both boxes within capacity.

In all cases we obtain a six-state choice satisfying the fixed-state interval
criterion, so the expanded pseudokernel has the desired low-degree capacities.
This proves the lemma.

## 3. The Pure-Cycle Capacity Lemma

**Lemma 3.1.** Let `C` be a nonempty disjoint union of simple cycles, with total
vertex count `s`. Suppose integers `R_0,R_1,R_2` satisfy

```text
R_i >= floor(s/3)        for i=0,1,2,
R_0+R_1+R_2 >= s+4.
```

Then `C` has a spanning subgraph `J` with `m(J,i)<=R_i` for `i=0,1,2`, except
for the single static case where `C=C5` and `(R_0,R_1,R_2)=(4,1,4)`.

**Proof.** For one cycle of length `s`, the possible profiles are exactly

```text
(s,0,0), (0,0,s), and (a,2j,c) with j>=1 and a+c+2j=s.
```

This is the cyclic binary-word run argument: nonconstant cyclic words have an
even positive number of transitions, and the remaining adjacencies are split
between `00` and `11`.

For one cycle, if `R_1>=2`, choose the largest even `b<=min(R_1,s)`. The two
outer capacities have enough total room for `s-b`, so a profile `(a,b,c)` can
be chosen under `R`. If `R_1<=1`, the coordinate lower bounds force `s<=5`;
the only failure after checking constant profiles is precisely
`s=5, R=(4,1,4)`.

For several cycles, first handle the all-`C5` family. Direct profile sums cover
two through seven copies:

```text
2C5: (3,4,3) or (5,2,3) and symmetries
3C5: (5,6,4) or (6,4,5) and symmetries
4C5: (6,8,6) or (8,6,6) and symmetries
5C5: (8,10,7) or (9,8,8) and symmetries
6C5: (10,10,10)
7C5: (12,10,13) and symmetries
```

For at least eight copies, remove six copies using `(10,10,10)` and induct on
the rest. The floor and total-sum inequalities are preserved.

For a general cycle family, induct on the number of components. Choose a
component whose length is not five, reserve `floor(s'/3)` capacity in each
coordinate for the remaining total length `s'`, and apply the one-cycle result
to the chosen component. The remaining capacities still satisfy the same
three lower bounds and the same `+4` total slack. If the remainder would be the
exceptional single `C5` with `(4,1,4)`, adjust the first component profile: a
nonconstant profile can move one unit between its two outer coordinates, and
an all-transition even cycle can be replaced by `(1,s-2,1)`. This avoids the
exception without breaking the reserved capacities. This proves the lemma.

## 4. Reduction to Pseudokernels and Cycles

Starting from `G`, repeatedly delete an edge whose two endpoints both have
current degree at least three. The process terminates and preserves minimum
degree at least two. Let `F` be the resulting spanning subgraph. Then every
edge of `F` touches a vertex of `F`-degree two.

Let `Y` be the union of all connected components of `F` consisting entirely of
degree-two vertices. Since `F` is simple, the components of `Y` are disjoint
simple cycles. Put

```text
C = |V(Y)|,       X = F - V(Y),       N = |V(X)|,
n = N+C.
```

Assume first that `X` is nonempty. Let

```text
D = {v in V(X) : d_F(v)>=3},
U = {v in V(X) : d_F(v)=2}.
```

There are no edges inside `D`, because every edge of `F` touches a degree-two
vertex. Each component of `F[U]` is a path. It cannot be a cycle, since then it
would be a pure degree-two component already placed in `Y`. Compress each such
path to a kernel edge between the high vertices it meets. If the two ends meet
the same high vertex, this gives a loop; different paths can give parallel
edges. Every kernel vertex has degree at least three. Ordinary kernel edges
have at least one internal vertex. A loop has at least two internal vertices:
with only one internal vertex it would require two parallel edges between that
internal vertex and the same high vertex in the simple graph `F`.

Thus `X` is exactly a positive-thread pseudokernel expansion. By Lemma 2.1
there is a spanning subgraph `H_X` of `X` such that

```text
a_i := m(H_X,i) <= B_X := floor(N/3)+2,       i=0,1,2.
```

## 5. Adding the Pure Cycles Once

If `C=0`, take `H=H_X`. Now suppose `C>0` and `X` is nonempty. Let

```text
B = floor((N+C)/3)+2,
R_i = B-a_i.
```

The floor inequality gives

```text
R_i >= floor(C/3).
```

Let `h` be the number of vertices of `X` having degree at least three in
`H_X`. Since every vertex of `X` has `H_X`-degree `0`, `1`, `2`, or at least
three,

```text
a_0+a_1+a_2 = N-h.
```

Write `eta=3B-(N+C)`, so `eta in {4,5,6}`. Then

```text
R_0+R_1+R_2 = C + eta + h >= C+4.
```

Lemma 3.1 therefore inserts all pure cycles into the same three global boxes,
unless the exceptional static case occurs:

```text
Y = C5,      (R_0,R_1,R_2)=(4,1,4).
```

In that case the last equality forces `eta=4`, `h=0`, and

```text
(a_0,a_1,a_2)=(B-4,B-1,B-4).
```

Because `X` is nonempty and has no pure degree-two component, it has a high
vertex. Since `h=0`, every high vertex has `H_X`-degree `0`, `1`, or `2`.
There are three cases.

If some high vertex has `H_X`-degree two, add one unselected incident edge
from it to a degree-two neighbor. The neighbor previously has degree `0` or
`1`. The resulting non-pure low-degree vector is respectively
`(B-5,B,B-5)` or `(B-4,B-2,B-4)`, which can be paired with the `C5` profiles
`(5,0,0)` or `(0,2,3)`.

If no high vertex has degree two but some high vertex has degree one, delete
its unique selected incident edge. The degree-two neighbor previously has
degree `1` or `2`. The resulting vectors are respectively
`(B-2,B-3,B-4)` and `(B-3,B-1,B-5)`, paired with `C5` profiles `(0,2,3)` and
`(0,0,5)`.

If all high vertices have degree zero in `H_X`, take the edge-complement of
`H_X` inside `X`. Degree-two vertices swap degree zero and degree two, while
high vertices leave the low-degree classes. If there are `d>=1` high vertices,
the new low-degree vector is `(B-4,B-1,B-4-d)`, and the `C5` profile
`(0,0,5)` finishes.

Hence the static `C5` exception is always removable in the presence of `X`.

If `X` is empty, then the whole graph is a disjoint union of cycles. Apply
Lemma 3.1 with `R=(B,B,B)`. For `Y=C5` one has `B=3`, so the exceptional
capacity `(4,1,4)` does not occur. Thus, in all cases, we obtain a spanning
subgraph `H` of `F` with

```text
m(H,i) <= B,       i=0,1,2.
```

## 6. Higher Degree Classes

It remains to control `j>=3`. Fix such a `j` and set

```text
S_j = {v : deg_H(v)=j}.
```

Every vertex in `S_j` is a high vertex of `F`. Since every edge of `F` touches
a degree-two vertex, every selected edge incident with `S_j` has its other
endpoint in the set of `F`-degree-two vertices. Therefore

```text
j |S_j| <= m(H,1) + 2 m(H,2) <= 3B.
```

Since `j>=3`, this gives `|S_j|<=B`. Together with the low-degree bounds, this
proves the theorem for all `j>=0`. Because `H` is a spanning subgraph of
`F` and `F` is a spanning subgraph of `G`, it is also a spanning subgraph of
`G`. This proves the theorem.

## 7. Sharpness of the Integer Bound at 2C4

Let `G=2C4`. In any spanning subgraph of one copy of `C4`, the possible
profiles `(m_0,m_1,m_2)` are

```text
(4,0,0), (2,2,0), (1,2,1), (0,4,0), (0,2,2), (0,0,4).
```

Thus the number of degree-one vertices in each component is even. If a
spanning subgraph of `2C4` had all three degree classes of size at most three,
the three counts would sum to eight and so would have to be `(3,2,3)`. One
copy of `C4` would then contribute zero degree-one vertices and the other two.
The zero-degree-one copy is either empty or the whole cycle, contributing four
vertices to degree zero or degree two, contradicting `(3,2,3)`.

Conversely, choosing two adjacent edges in each copy of `C4` gives total
profile `(2,4,2)`. Hence

```text
min_H max_j m(H,j) = 4 = floor(8/3)+2.
```
