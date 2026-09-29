# A four-marked four-cycle cone

Fix `n>=8`, a four-set `R`, and give each four-cycle with support `A` the
weight `f(|A intersect R|)`, where

```text
0<=f(0)<=f(1)<=f(2)<=f(3)<=f(4).
```

If `f(1)>0`, then the largest nondegree eigenvalue is attained only by the
standard representation. This is a representation-level statement; it does
not assert a uniform multiplicity inside the standard block.

The deeper closed face `f(0)=f(1)=0` remains open. No result for `n=6,7` is
claimed here.

## Threshold decomposition

Let `T_j` be the sum of four-cycles whose support meets `R` in exactly `j`
points, and put `B_s=sum_{j>=s}T_j`, with `B_0=K_4` the normal four-cycle
class. Then

```text
T_f = f(0)K_4 + sum_{s=1}^4 (f(s)-f(s-1)) B_s.
```

All five rays attain their comparison values on the common standard space

```text
W={x : x|_R=0 and sum_{i notin R}x_i=0},   dim W=n-5.
```

The normal ray is strict outside the standard representation. The hit ray
`B_1` is also strict. The remaining rays have compatible non-strict bounds.
Thus `f(1)>0` means that either `K_4` or `B_1` has positive coefficient, and
the loss form of Weyl's inequality makes the whole combination strict.

## The hit ray

Write `m=n-4`. Since `B_1=K_{m+4}-K_m`, the four-cycle content formula reduces
its scalar on a branch `nu subset lambda`, `|lambda|-|nu|=4`, to

```text
h(lambda,nu)
 = sum_{i=1}^4 [x_i^3-(2m+5)x_i] - 8 C(nu),
```

where the `x_i` are the four added-box contents and `C(nu)` is the content
sum. The common standard value is

```text
H_m=4m^3-6m^2+6m-2.
```

If at least three boxes of `nu` lie below its first row, bounding the added
contents and minimizing `C(nu)` gives a positive uniform gap. The positive
endpoint reduces to the two polynomials

```text
3m^2-m-1,
2m^3-5m^2+21m-89,
```

and the negative endpoint, after squaring, reduces at `m=z+4` to a polynomial
with strictly positive coefficients. The remaining tail sizes `0,1,2` have
only finitely many stable increment patterns; the exact certificate exhausts
all 76 patterns and finds no nonstandard equality. Hence `B_1` is strict.

## The middle ray

For `B_2`, split by the two marked points used by the support:

```text
B_2 = sum_{S subseteq R, |S|=2} D_S + B_3,
```

where `D_S` is an embedded `C(m+2,4;2)^+`. The published non-strict bound
gives

```text
D_S <= d_m I + (6m-4)P_S,
```

with `P_S` the subgroup-trivial projection. Branching shows that the sum of
these projections can occur only in `(n-2,2)` and `(n-2,1,1)` outside the
degree and standard blocks. In the unsigned two-subset model and the exterior-
square model, respectively, the required joint compensation with `B_3`
reduces to five explicit positive rational inequalities. This proves the
compatible non-strict bound

```text
lambda_max(B_2) <= 18m^2-30m+6.
```

The files in `evidence/four_marked` record the exact low-tail content audit and
the two model computations for `m=4,...,8`. The formulas themselves are
symbolic in `m`; the finite runs are regression checks, not an extrapolation.

## The last two rays

The ray `B_3` is a positive sum of four embedded hard-containment operators
plus the local `B_4` term. The complete Conjecture 4.7 bound and the trivial
degree bound give the compatible non-strict estimate. The local ray `B_4`
uses the degree bound directly.

Combining the five endpoint bounds on their common standard space proves the
theorem. The argument leaves the cone generated only by `B_2,B_3,B_4`
unresolved, exactly the face `f(0)=f(1)=0` stated above.
