# Proof of the Five-Point Sixteen-Shattering Theorem

Throughout, logarithm bases affect only absolute constants. For a finite set
of points in a product grid, a standard-priority lexicographic order compares
coordinates in the order `0,1,...,d-1`, using an independently selected total
order of the alphabet at each coordinate.

## 1. Two Covering Lemmas

**Lemma 1 (local lex orders).** For `b>=2` and `d>=1`, there is a family
`P` of standard-priority lexicographic orders of `{0,...,b-1}^d`, of size
`O(log(bd))`, which realizes every prescribed collection of local total
orders on at most four coordinates, with at most five specified values at
each coordinate.

**Proof.** Independently choose a uniformly random permutation of the `b`
values at each coordinate. A fixed demand prescribing orders on `s_i<=5`
values at each of at most four coordinates is met with probability

```text
1 / product_i(s_i!) >= (5!)^(-4) = p.
```

The number `K` of demands is at most

```text
sum_(q=0)^4 binom(d,q)
  * (sum_(s=0)^5 binom(b,s) s!)^q,
```

so `log(K+1)=O(log(bd))`. By averaging, some full tuple of local alphabet
orders covers at least a `p` fraction of the remaining demands. Repeating
this greedy choice leaves at most `K(1-p)^m` demands after `m` choices.
Taking `m>log(K)/(-log(1-p))` covers all demands. Each tuple defines one
standard-priority lexicographic order. This proves the lemma. `square`

**Lemma 2 (four-position sign cover).** For every positive integer `M`,
there is a set `H` of sign vectors in `{-1,+1}^M`, of size `O(log(M+1))`,
which realizes every sign assignment on every set of at most four positions.

**Proof.** There are

```text
K_M = sum_(q=0)^min(4,M) 2^q binom(M,q)
```

demands. A uniform sign vector meets each demand with probability at least
`1/16`. The same averaging and greedy-cover argument leaves at most
`K_M(15/16)^m` demands after `m` rows, so `O(log(M+1))` rows suffice.
`square`

Both lemmas are finite existence arguments. Choosing the lexicographically
first maximizing row at every greedy step makes the choices deterministic;
no efficient construction claim is needed.

## 2. First Differences and Ideal Orders

Fix five distinct points `X` in `{0,...,b-1}^d`. For distinct `x,y`, let
`i(x,y)` be their first differing coordinate in standard coordinate order,
and put

```text
I(X) = {i(x,y) : x,y in X, x != y}.
```

There are at most four coordinates in `I(X)`. Indeed, recursively split the
five points at their first nonconstant coordinate. The resulting trie has
five leaves and at most four internal branching nodes, and each pair's first
difference labels the node where its paths separate.

For a subset `Y` of `X` with at least two points, write `i(Y)` for its first
nonconstant coordinate and `S(Y)` for the values visible there. Projection
onto the coordinates `I(X)`, in increasing order, preserves distinctness and
every standard-priority first difference: the original first difference is
retained, and all earlier retained coordinates are equal. Coordinates deleted
by the projection may be nonconstant; no constancy assumption is used.

Let `L(X)` be the set of all restrictions to `X` of standard-priority lex
orders with arbitrary local alphabet orders. Each member depends only on at
most four coordinates and at most five visible values per coordinate. Lemma 1
therefore supplies a family `P` whose restrictions to `X` are exactly `L(X)`.

At each distinct coordinate, an orientation prescribed on a pair witnessed
at a first difference is independent of prescriptions at other coordinates.
Changing it reverses a witnessed pair and changes the induced point order.
Consequently,

```text
|L(X)| >= 2^|I(X)|.
```

More generally, independently prescribing all orders on one chosen
first-difference slice at each active coordinate gives the product of their
factorials as a lower bound. The prescriptions extend to alphabet orders and
Lemma 1 realizes them simultaneously.

## 3. Classification Below Sixteen

**Lemma 3.** If `|L(X)|<16`, exactly one of the following holds.

- **Type A.** There are three active coordinates. Every first-difference
  slice is a pair, and all pair slices at the same coordinate are the same
  pair. Then `|L(X)|=8`.
- **Type B.** There are two active coordinates `i<j`. After projection onto
  them, the classes of equal `i`-value have one of these forms:
  - sizes `3,2`, with the pair's `j`-values contained in the triple's
    `j`-values;
  - sizes `2,2,1`, with the same pair of `j`-values in the two two-point
    classes.
  In either form, `|L(X)|=12`.

**Proof.** Four active coordinates give at least 16 orders. Zero active
coordinates are impossible, and one active coordinate must distinguish all
five points and gives `5!=120` orders.

Suppose there are three active coordinates. If some first-difference slice
has at least three values, its six orders and the two orientations at each of
the other active coordinates give at least `6*2*2=24` orders. Thus every
slice is a pair. If two different pair slices occur at one coordinate, they
share at most one value. Either orientation of each pair can be imposed and
the two directed edges can be extended to a total order of their union: two
distinct directed edges cannot form a directed cycle. With two choices at
each other active coordinate, this gives at least `4*2*2=16` orders. Hence
the pair slices at each coordinate coincide. The three pair orientations
determine every point comparison, and all eight choices occur. This is Type A.

Now suppose there are two active coordinates `i<j`. Let `r` be the number of
`i`-value classes. Their order is arbitrary, contributing `r!`, independently
of the internal orders within classes. Values of `j` within each class are
distinct. If `r>=4`, then `r!>=24`.

If `r=2`, the class sizes are `4+1` or `3+2`. The first gives at least
`2!*4!=48` orders. In the second, the triple has six internal orders. If the
pair's value set is not contained in the triple's, either orientation of the
pair extends every order of the triple, giving at least `2!*3!*2=24` orders.
If it is contained, its orientation is determined by the triple order, giving
exactly `2!*3!=12` orders.

If `r=3`, the class sizes are `3+1+1` or `2+2+1`. The first gives at least
`3!*3!=36` orders. In the second, different `j`-value pairs allow their two
orientations independently and give `3!*2*2=24`; equal pairs have one shared
orientation and give exactly `3!*2=12`. This is Type B and exhausts all
possibilities. `square`

## 4. The Promoted Binary-Primary Family

Take `b=2^L`, and let `beta(v)` be the length-`L` binary representation of
`v`, most significant bit first and with leading zeros. Choose the sign cover
`H` from Lemma 2 with `M=L+d`.

For each coordinate `j` and each `h in H`, define `Q_(j,h)` by increasing
lexicographic comparison of the key

```text
(h_0 beta_0(x_j), ..., h_(L-1) beta_(L-1)(x_j),
 h_L x_0, ..., h_(L+d-1) x_(d-1)).
```

The final `d` entries make the key injective on the grid, so it defines a
total order. The first `L` entries compare primary values using a signed
binary lex order. Equal primary values fall back to the original coordinate
priority, with independently selected numerical orientations.

Let `Q_j={Q_(j,h):h in H}` and set

```text
R = P union union_(j=0)^(d-1) Q_j.
```

**Lemma 4 (joint realization).** Suppose `|I(X)|<=3`, `j in I(X)`, and
coordinate `j` takes two or three values on `X`. Then `Q_j` realizes every
combination of an ideal signed-binary lex order on those values and arbitrary
numerical fallback signs on `I(X)\{j}`.

**Proof.** Two distinct binary strings have one first-difference bit. Three
distinct strings have exactly two relevant first-difference bits: the first
branching bit splits a singleton from a pair, and the pair separates at a
later bit. Thus the primary order requires at most two bit signs. All sign
assignments give two orders for two values and four orders for three values;
changing an active bit reverses a witnessed comparison.

If two points have different `j`-values, these primary signs determine their
order. If their `j`-values agree, fallback uses their original first differing
coordinate, which lies in `I(X)\{j}`. At most two additional signs are needed.
The fallback positions are among the last `d` entries of `h` and are disjoint
from the primary-bit positions. Lemma 2 therefore realizes every requested
combination with one sign vector. The unchanged fallback priority ensures
that a deleted or redundant coordinate cannot become an earlier fallback
difference. `square`

## 5. The Eight-Plus-Eight Case

Assume Type A. List the points in their natural standard lex order as
`x_1,...,x_5`. The four adjacent first-difference coordinates lie in the
three-element set `I(X)`, so two gaps share a coordinate `j`. These gaps
cannot be adjacent: three consecutive endpoints would agree before `j` and
have three strictly increasing values at `j`, contrary to the pair-slice
condition.

Write the four distinct endpoints as `A,B,C,D` in their natural order, with
`i(A,B)=i(C,D)=j`, and put `i=i(B,C)`. We have `i<j`; otherwise the four
points agree before `j` and

```text
A_j < B_j <= C_j < D_j,
```

again producing a slice with at least three values. Therefore

```text
A_i=B_i != C_i=D_i,
A_j=C_j=a,  B_j=D_j=b,  a!=b.
```

Every order in `L(X)` separates `{A,B}` from `{C,D}`, while every order in
`Q_j` separates `{A,C}` from `{B,D}`. No order on four points can separate
both crossing partitions: in an order separating two pairs, its first two
points form one block, and the two partitions have no common block. Hence the
restrictions supplied by `P` and `Q_j` are disjoint.

Let `E` be the fifth point. If `E_j` equals `a` or `b`, the two primary fibers
have sizes three and two. The three-point fiber has exactly two original
first-difference coordinates. It has at most two by the trie argument and
cannot have only one, since that would produce a three-value slice. Both lie
in `I(X)\{j}`. Their two fallback signs give four distinct internal orders,
and the two primary values have two orientations. Lemma 4 realizes all
`2*4=8` combinations.

If `E_j` is a third value, the three actual binary values have four distinct
signed-binary primary orders. The tied pair `A,C` first differs at `i<j`, and
the fallback sign at `i` supplies both internal orientations. Lemma 4 gives
`4*2=8` distinct orders.

Thus `Q_j` contributes at least eight orders disjoint from the eight in
`P`, for a total of at least 16.

## 6. The Twelve-Plus-Four Case

Assume Type B, with active coordinates `i<j`. In either form, two distinct
`i`-value classes contain the same pair of `j`-values `a,b`. Choose `A,B`
from one class and `C,D` from the other so that

```text
A_j=C_j=a,  B_j=D_j=b.
```

Again, `P` separates `{A,B}` from `{C,D}`, while `Q_j` separates `{A,C}`
from `{B,D}`, so the two sets of restrictions are disjoint.

Coordinate `j` has at most three values on all five points. Lemma 4 permits
both primary orientations of `a,b` and both fallback signs at `i`,
independently. On the four-point core these give the four distinct orders

```text
ACBD, CADB, BDAC, DBCA.
```

Therefore `Q_j` contributes at least four orders outside the 12 in `P`.

If `|L(X)|>=16`, `P` already suffices. Lemma 3 and the two cases above prove
that `R` 16-shatters every five-element subset of every grid
`{0,...,2^L-1}^d`.

## 7. Size and Arbitrary Ground Sets

The construction has size

```text
|R| <= |P| + d|H|
     = O(log(bd) + d log(L+d+1))
     = O(L + log d + d log(L+d+1)).
```

The primary and fallback choices use the same sign cover `H`, so their cover
sizes are not multiplied.

For an integer `n>=5`, set

```text
N = log_2 n,
r = log_2(N+2),
d = ceil(sqrt(N/r)),
L = ceil(N/d),
b = 2^L.
```

Then `Ld>=N`, so the grid has `b^d=2^(Ld)>=n` points. Fix an injection of
`[n]` into the grid, construct `R` independently of any test set, restrict
each order to the image of `[n]`, and transport it back to `[n]`. Every
five-set retains at least 16 distinct induced orders.

For large `N`,

```text
d <= sqrt(N/r)+1,
L <= sqrt(Nr)+1,
dr <= sqrt(Nr)+r,
log(L+d+1) = O(r).
```

Since `r=Theta(log log n)`, the displayed size bound becomes

```text
O(sqrt(log n * log log n)).
```

Moreover `sqrt(Nr)/N=sqrt(r/N)` tends to zero. Hence
`f_5(n,16)=o(log n)`. The same family works for every `1<=t<=16`, proving
the complete `k=5` slice of Conjecture 4.2. `square`

## Attribution and Evidence Boundary

The standard lexicographic family, first-difference framework, and crossing
method build on Girao--Michel--Tamitegama, Lemmas 3.1--3.4 and the proof of
Theorem 1.7. They are credited even though the statements needed above are
proved in this package.

The promoted signed-binary primary key, the shared primary/fallback sign
cover, the complete five-point classification below 16, and the resulting
size analysis form the released extension. Finite diagnostics are not used
to justify any universal quantifier.
