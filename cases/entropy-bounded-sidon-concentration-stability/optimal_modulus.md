# Optimal Stability Modulus

This file records a verified quantitative extension of the stability theorem.
It uses the same notation and conventions as [problem.md](problem.md) and
[proof.md](proof.md): all logarithms are natural, `X,X'` are independent copies
of a discrete finite-entropy random variable on an abelian group, and

```text
Delta(X) = H(X) - s(X) - (log 2) * (1 - sum_a p_a^2).
```

Define

```text
d_Sid(X) = inf_B P(X notin B),
M(C,D) = sup d_Sid(X),
```

where `B` ranges over Sidon subsets of `supp(X)`, and the supremum defining
`M(C,D)` ranges over all ambient abelian groups and all `X` with `H(X)<=D` and
`Delta(X)<=C`.

## A. Closed-Form Upper Bound

The proof in [proof.md](proof.md) establishes, for every `0<tau<1`,

```text
d_Sid(X) <= D/log(1/tau) + C/(tau log 2).                (1)
```

It also gives `M(0,D)=M(C,0)=0`. For `C,D>0`, put

```text
x(C,D) = 2 W_0(0.5 * sqrt(D log 2 / C)),
```

where `W_0` is the principal real branch of Lambert's `W` function. Then

```text
M(C,D) <= min { 1 - exp(-D), D * (x(C,D)+1) / x(C,D)^2 }. (2)
```

The second term is the exact minimum of the right side of (1). Indeed, writing
`x=log(1/tau)` gives

```text
g(x) = D/x + (C/log 2) exp(x),       x>0.
```

This function is strictly convex and diverges at both endpoints. Its unique
critical point satisfies

```text
x^2 exp(x) = D log 2 / C,
```

which is equivalent to the displayed Lambert-W formula. At that point,
`(C/log 2) exp(x)=D/x^2`, so the minimum is `D(x+1)/x^2`. The optimizing
threshold is

```text
tau_* = exp(-x(C,D)) = C x(C,D)^2 / (D log 2).
```

The bound `1-exp(-D)` follows by keeping one maximum-probability atom: if
`p_max` is the largest atom, then `H(X)>=log(1/p_max)`, so
`p_max>=exp(-D)`, and a singleton is Sidon.

## B. Dense No-Carry Blocks

Let `m>=3`, let `N>=1`, and let `0<E<1`. Put `b=2m+1` and, in the integer
group, define

```text
a_{i,r} = b^(2i) + r b^(2i+1),    0<=i<N, 1<=r<=m.
```

Let `X` have mass `1-E` at `0` and mass `E/(mN)` at each point `a_{i,r}`.
Base-`b` addition has no carry in sums of two support points: even digits have
coefficient at most `2`, and odd digits have coefficient at most `2m=b-1`.
Thus all sums are unique up to exchanging the two summands except within one
block, where the only collisions are exactly the relations

```text
r+s = r'+s'  in [m].
```

Let

```text
nu_m(t) = |{(r,s) in [m]^2 : r+s=t}|
```

and

```text
kappa_m = (1/m^2) * sum_{r,s=1}^m
          (log nu_m(r+s) - (log 2) * 1_{r!=s}).
```

Then this construction satisfies

```text
H(X) = h(E) + E log(mN),
Delta(X) = E^2 kappa_m / N <= E^2 log(m) / N.           (3)
```

If `sigma_m` is the maximum size of a Sidon subset of `[m]`, then

```text
d_Sid(X) = E * (1 - sigma_m/m).                         (4)
```

The upper direction in (4) is forced because every global Sidon subset can keep
at most `sigma_m` points in each block. The lower direction is achieved by
taking a largest Sidon subset in every block and also keeping `0`; the no-carry
separation prevents collisions between different blocks or with the point `0`.

Finally,

```text
sigma_m <= (1 + sqrt(8m-7)) / 2.                         (5)
```

This is the elementary positive-difference bound: a Sidon subset of `[m]` with
`k` elements has `binom(k,2)` distinct positive differences, all lying in
`{1,...,m-1}`.

## C. Fixed Entropy Budget

For every fixed `D>0`,

```text
M(C,D) = D/log(1/C) * (1+o(1))  as C -> 0.               (6)
```

For the lower bound, set `L=log(1/C)`. Fix `m>=3` and `0<eta<1`, then use the
block construction with

```text
E = (1-eta)D/L,
N = ceil(E^2 log(m)/C).
```

For all sufficiently small `C`, this gives `0<E<1`, `Delta(X)<=C`, and

```text
H(X) <= E * (L + log E + 1 + log(2m log m)) < D.
```

Therefore

```text
M(C,D) >= ((1-eta)D/L) * (1 - sigma_m/m).
```

Letting first `C -> 0`, then `eta -> 0`, then `m -> infinity` and using (5)
gives

```text
liminf_{C->0} (L/D) M(C,D) >= 1.
```

For the upper bound, the optimized parameter in (2) satisfies

```text
x + 2 log x = L + log(D log 2).
```

Hence `x/L -> 1`, and (2) gives

```text
limsup_{C->0} (L/D) M(C,D) <= 1.
```

The lower and upper bounds prove (6). The lower-bound examples are finite
integer-valued distributions.

## D. A Low-Entropy Square-Root Regime

For `0<C<(log 2)/4`, set

```text
E_C = 2 sqrt(C/log 2),
D_C = h(E_C) + E_C log 4.
```

Then

```text
M(C,D_C) >= E_C/4 = sqrt(C)/(2 sqrt(log 2)).             (7)
```

To see this, take support `{0,12,23,45,56}` in the integers, put mass `1-E_C`
at `0`, and put mass `E_C/4` at each of the four nonzero points. The only
nontrivial collision among the four nonzero points is

```text
12 + 56 = 23 + 45.
```

It contributes four ordered pairs, each with surplus `log 2`, so
`Delta(X)=E_C^2 log 2/4=C`. Destroying the collision requires deleting at least
one of the four equal-mass nonzero atoms, and deleting one is sufficient, so
`d_Sid(X)=E_C/4`.

Conversely, `D_C = sqrt(C) log(1/C)/sqrt(log 2) * (1+o(1))`. In the optimized
upper bound (2), this gives `x(C,D_C)/log(1/C) -> 1/2`, and hence

```text
limsup_{C->0} M(C,D_C)/sqrt(C) <= 2/sqrt(log 2).         (8)
```

Equations (7) and (8) show `M(C,D_C)=Theta(sqrt(C))`. This is a genuine
low-entropy joint regime, not the fixed-`D` leading term from (6).

## Boundary

The four-point collision pattern used in the square-root lower bound is
already present in Example 5.4 of the source paper. The additional contribution
recorded here is the entropy-budgeted use of heavy atoms, the dense no-carry
block family, the optimized threshold bound, and the matching fixed-`D`
constant.

This extension does not claim exact finite-parameter optimality of (2), does
not claim matching constants in (7)-(8), and does not claim public priority.
