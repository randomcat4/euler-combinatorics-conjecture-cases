# Product-activity cycle weights

For positive activities `x_1,...,x_n`, give every `k`-set `A` the weight
`prod_{i in A}x_i` and assign that weight to every `k`-cycle supported on
`A`. This note records three proved families. It does not claim the general
product-activity conjecture.

## One exceptional activity, every fixed cycle length

Let `n>=5`, `2<=k<=n-2`, and

```text
x=(tc,c,...,c),     c>0, 0<t<1.
```

The largest nondegree eigenvalue is attained only by the standard
representation when `k` is even, and exactly by the standard representation
and its sign twist when `k` is odd. The target root is simple inside each
target block.

After dividing by `c^k`, write `K_n` for the normal `k`-cycle class and
`K_{n-1}` for the class avoiding the exceptional point. The operator is

```text
T(t)=tK_n+(1-t)K_{n-1}.
```

On a branch `mu nearrow lambda` of the multiplicity-free restriction to
`S_{n-1}`, its eigenvalue is

```text
t a_lambda + (1-t)b_mu,
```

where `a_lambda` and `b_mu` are central class scalars. The normal-class Aldous
bound gives `a_lambda<=a_standard`. Equality with the degree scalar of
`K_{n-1}` forces `mu` to be trivial, or sign when `k` is odd; branching then
forces `lambda` to be a degree or target representation. Hence every
nontarget block is strict because `0<t<1`. The relevant target branch is
one-dimensional, proving simplicity.

## Three-cycles with at most two exceptional activities

Let `n>=5`, put `N=n-2`, and take

```text
x=(a,b,c,...,c),     0<a<min(b,c).
```

The largest nondegree eigenvalue is attained exactly by `(n-1,1)` and its
sign twist `(2,1^(n-2))`, and is simple in each target block.

Define the three conductances

```text
p=abNc,
r=ac[b+(N-1)c],
s=bc[a+(N-1)c],
```

and

```text
T=2p+(N+1)(r+s),
S=(N+2)[p(r+s)+Nrs].
```

The smaller nonzero root of the standard three-class Laplacian quotient is

```text
gamma=(T-sqrt(T^2-4S))/2.
```

Thus the target adjacency eigenvalue is

```text
D-gamma,     D=2 sum_{i<j<l}x_i x_j x_l.
```

The proof divides into the exhaustive regimes `b<c`, `b=c`, and `b>c`.
Positive rescaling reduces them respectively to

```text
(t,1,Q,...,Q),   (t,1,...,1),   (t,Q,1,...,1),
```

with `0<t<1<Q` in the two unequal cases. Multiplicity-space reduction along
`S_n downarrow S_{n-2}` gives scalar one-path blocks and explicit `2x2`
two-path blocks. The three regime inequalities place every nontarget block
strictly below the smaller standard quotient root. The two-class case is the
branch-diagonal argument above. The three regimes meet without a gap at
`b=c`, proving the displayed all-parameter statement.

## A four-scale all-parameter ray at `n=5`

Let `n=5`, `k=3`, `q>=13/5`, `0<t<1`, and

```text
x=(t,1,q,2q,3q).
```

The largest nondegree eigenvalue is attained exactly by `(4,1)` and its sign
twist `(2,1,1,1)`. This assertion is representation-level only; no target-
block simplicity is claimed.

At `t=0`, subtract the comparison gap

```text
g_*(q)=22q^2+18q
```

from the two nonexceptional competitor pencils `(3,2)` and `(3,1,1)`. After
the shift `q=r+13/5`, all eleven leading principal minors have strictly
positive coefficients, so Sylvester's criterion makes both gap forms positive
definite. Increasing `t` adds a positive-semidefinite group Laplacian to each
competitor gap. In the standard block, the vector `e_1-e_2` at `t=1` has
Rayleigh gap exactly `g_*(q)`, and the standard gap pencil is Loewner monotone.
Therefore every `0<t<1` has strict representation-level separation.

The exact coefficient certificates are in `evidence/product_activity`. The
bound `13/5` is a convenient sufficient value, not asserted to be optimal.

## Boundary

The first theorem's `k=2` slice is covered by more general published weighted-
transposition results. The second theorem allows at most one nontail activity
besides the unique minimum. The third theorem is a one-dimensional ray. None
of them resolves arbitrary positive activities, and finite no-hit diagnostics
are not used as proofs.
