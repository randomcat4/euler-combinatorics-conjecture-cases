# Self-Contained Proof

## 1. Plane-tree notation and the root decomposition

Write a rooted plane tree as

```text
P(T_1,...,T_d),
```

where `(T_1,...,T_d)` is the ordered list of subtrees rooted at the children
of the root. The one-vertex tree is `bullet = P()`. Write `|T|` for the number
of edges of `T`.

We first define a decomposition `Delta(T) = (L,R)` for every
`T != bullet`.

### Case A: the root has a leaf child

Let `bullet` be the leftmost leaf child of the root and write the root's child
list uniquely as

```text
(F_0, bullet, F_1),
```

where the ordered forest `F_0` contains no leaf tree. Set

```text
L = P(F_0),       R = P(F_1).
```

Thus the root of `L` has no leaf child.

### Case B: the root has no leaf child

Starting at the root, repeatedly follow the leftmost child until reaching the
first leaf in preorder. Write this path as

```text
v_0 = root, v_1, ..., v_m = y, x,
```

where `x` is the leaf, `y` is its parent, and `m >= 1`. For `0 <= i < m`,
let `F_i` be the ordered forest of children of `v_i` that occur after the path
child `v_{i+1}`. Let `F_m` be the ordered forest of children of `y` that occur
after `x`. Define

```text
L = P(F_0, bullet, F_m),
R = P(P(F_1),...,P(F_{m-1})).
```

Here the displayed `bullet` is the leftmost leaf child of the root of `L`.

The two cases are mutually exclusive and exhaustive. In both cases exactly
one distinguished edge disappears, so

```text
|L| + |R| = |T| - 1.                                  (1)
```

## 2. The intrinsic statistic

Define two nonnegative integer-valued functions on plane trees by

```text
q(bullet)  = 0,
st(bullet) = 0.
```

For `Delta(T) = (L,R)`, set

```text
q(T) = q(R) + 1,                 if L = bullet,
       q(L),                     if L != bullet,       (2)

st(T) = st(L) + st(R) + [q(R) is odd].                (3)
```

The bracket is `1` when its condition holds and `0` otherwise. Equation (1)
shows that the recursion terminates, so both functions are defined on every
finite rooted plane tree.

This definition is intrinsic. It reads only the ordered tree and its root
decomposition. Equivalently, repeatedly applying `Delta` produces a binary
decomposition tree. The state `q` follows its left branch unless that branch
is `bullet`, in which case it follows the right branch and increments. The
statistic `st` counts decomposition nodes whose right component has odd
boundary state. No permutation or intermediate Catalan object occurs in the
definition.

## 3. The root decomposition is invertible

For any ordered pair `(L,R)` of plane trees, define `Rec(L,R)` as follows.

If the root of `L` has no leaf child, write `L=P(F_0)` and `R=P(F_1)` and set

```text
Rec(L,R) = P(F_0, bullet, F_1).                        (4)
```

The inserted leaf is the leftmost leaf child, so applying Case A recovers
`(L,R)`.

If the root of `L` has a leaf child, split its child list at the leftmost one:

```text
L = P(F_0, bullet, F_*).
```

Write `R=P(Q_1,...,Q_s)`, set `m=s+1`, let `F_i` be the child list of `Q_i`
for `1 <= i < m`, and set `F_m=F_*`. The child list of `R` may be empty, in
which case `m=1`. Construct

```text
V_m = P(bullet,F_m),
V_i = P(V_{i+1},F_i)       for i=m-1,...,1,
Rec(L,R) = P(V_1,F_0).                                  (5)
```

The root in (5) has no leaf child. Its leftmost-child path ends at the
displayed `bullet`, and Case B recovers all forests `F_0,...,F_m` in their
original order. Conversely, applying (4) or (5) after decomposing a tree
restores every child position. Therefore

```text
Delta(Rec(L,R)) = (L,R),
Rec(Delta(T))   = T.                                    (6)
```

## 4. An explicit bijection with `231`-avoiding permutations

Let `epsilon` be the empty permutation. Define `Phi` recursively by

```text
Phi(bullet) = epsilon.
```

For `Delta(T)=(L,R)`, put `k=|L|+1`,
`alpha=Phi(L)`, and `beta=Phi(R)`, and define

```text
Phi(T) = (k, alpha_1,...,alpha_{k-1},
             k+beta_1,...,k+beta_|R|).                 (7)
```

The first block uses exactly the values `[k]`; the second uses exactly the
larger values. Thus (7) is a permutation of `[|T|]`.

Inductively, both `alpha` and `beta` avoid `231`. The word `(k,alpha)` also
avoids `231`: its first entry is the largest entry of that block and occurs
first. A `231` pattern cannot cross the block boundary because every entry in
the earlier block is smaller than every entry in the later block. Hence
`Phi(T)` avoids `231`.

To invert `Phi`, take any nonempty `pi in S_n(231)` and let `k=pi_1`. Every
entry less than `k` must precede every entry greater than `k`; otherwise
entries `pi_i>k>pi_j` with `1<i<j` would make `(k,pi_i,pi_j)` a `231` pattern.
Consequently `pi` has the unique form

```text
pi = (k, alpha_1,...,alpha_{k-1},
        k+beta_1,...,k+beta_{n-k}),                    (8)
```

with `alpha in S_{k-1}(231)` and `beta in S_{n-k}(231)`.

Define

```text
Psi(epsilon) = bullet,
Psi(pi) = Rec(Psi(alpha),Psi(beta))
```

using the unique split (8). The recursion decreases length. Equations (6)
and (8), followed by induction, give

```text
Psi(Phi(T)) = T,       Phi(Psi(pi)) = pi.              (9)
```

Thus `Phi` is a bijection from `T_n` to `S_n(231)` for every `n >= 0`.

## 5. Preservation of `mark` and `mnd`

Let `idr(pi)` be the length of the initial descending run, with
`idr(epsilon)=0`. From (7), the new initial entry `k` extends the initial
descending run of `alpha` by one, while the boundary to a nonempty `beta`
block is ascending. Therefore

```text
idr(Phi(T)) = idr(Phi(L)) + 1.                         (10)
```

Induction using the two decomposition cases gives

```text
idr(Phi(A)) is odd
  if and only if the root of A has a leaf child.       (11)
```

Indeed, for nontrivial `A`, Case A occurs exactly when the root of its left
component has no leaf child, while Case B occurs exactly when that root does
have a leaf child; equation (10) reverses the parity.

In (7), only the initial descending run of `alpha` changes. If that run has
length `r`, its contribution changes by

```text
floor((r+1)/2) - floor(r/2) = [r is odd].
```

All other descending runs remain separate, so

```text
mnd(Phi(T))
 = mnd(alpha) + mnd(beta) + [idr(alpha) is odd].       (12)
```

Now compare marked vertices. In Case A, the original root has a leaf child
but is excluded from `mark`; every other vertex retains its status in `L` or
`R`. Hence

```text
mark(T) = mark(L) + mark(R).
```

In Case B, the vertex `y` is a marked non-root vertex of `T`, but becomes the
root of `L` and is therefore excluded there. Every other relevant vertex
retains its status in one component. Hence

```text
mark(T) = mark(L) + mark(R) + 1.
```

By (11), these two recurrences agree exactly with (12). Starting from
`mark(bullet)=mnd(epsilon)=0`, induction yields

```text
mark(T) = mnd(Phi(T)).                                 (13)
```

## 6. Preservation of `st` and `mna` after inversion

For a permutation `gamma`, define

```text
rho(gamma) = iar(gamma^{-1}),
b(gamma)   = mna(gamma^{-1}),
```

where `iar` is the initial ascending-run length and both values are zero on
`epsilon`.

From the block form (7), reading positions in increasing value order gives

```text
Phi(T)^{-1}
 = (alpha^{-1}+1), 1, (beta^{-1}+k),                  (14)
```

where adding a constant means adding it to every entry of a word.

If `alpha` is nonempty, the last entry of `alpha^{-1}+1` is at least `2`, so
the following `1` creates a descent and leaves the initial ascending run in
the first block. If `alpha` is empty, the word begins with `1`, which extends
the initial ascending run coming from the `beta` block. Thus

```text
rho(Phi(T)) = rho(beta) + 1,     if alpha=epsilon,
              rho(alpha),       otherwise.            (15)
```

Under `alpha=Phi(L)` and `beta=Phi(R)`, recurrence (15) is identical to the
intrinsic recursion (2). Induction therefore proves

```text
q(T) = iar(Phi(T)^{-1}).                              (16)
```

Next consider all ascending runs in (14). A nonempty first block is separated
from the middle `1` by a descent and contributes `b(alpha)`. The middle `1`
extends the initial ascending run of the `beta` block from length
`rho(beta)` to `rho(beta)+1`. Every other run is unchanged. Consequently

```text
b(Phi(T))
 = b(alpha) + b(beta) + [rho(beta) is odd].            (17)
```

The formula remains valid when either block is empty. Combining (3), (16),
and (17), induction gives

```text
st(T) = mna(Phi(T)^{-1}).                              (18)
```

## 7. The bivariate identity

For the same tree and the same bijection, equations (13) and (18) give

```text
(mark(T), st(T))
  = (mnd(Phi(T)), mna(Phi(T)^{-1})).
```

Summing monomials over the bijection `Phi_n : T_n -> S_n(231)` proves, for
every `n >= 1`,

```text
sum_{pi in S_n(231)} x^mnd(pi) y^mna(pi^{-1})
  =
sum_{T in T_n} x^mark(T) y^st(T).
```

This proves the required joint identity with the inverse and both variable
positions unchanged.

## 8. Boundary examples

- The one-edge tree `P(bullet)` maps to `1` and has
  `(mark,st)=(0,0)`.
- The two-edge tree `P(bullet,bullet)` maps to `12` and has
  `(mark,st)=(0,1)`.
- The two-edge chain `P(P(bullet))` maps to `21` and has
  `(mark,st)=(1,0)`.

These examples cover the empty-left and empty-right branches and both cases
of the root decomposition.
