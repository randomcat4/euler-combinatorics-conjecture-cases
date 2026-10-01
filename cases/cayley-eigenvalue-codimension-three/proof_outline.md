# Proof outline for the complete uniqueness theorem

Write `N(n,k,r)` for the published non-strict bound on every nondegree block,
and `S(n,k,r)` for the strict version outside the standard block and, for odd
`k`, its sign twist. Conjecture 4.7 is equivalent to `S(n,k,r)`.

## 1. Strict propagation

Split `C(n,k;r)` according to whether `r+1` is fixed. On an irreducible
`S_n`-module the first part decomposes, by the multiplicity-free branching
rule, into `S_{n-1}` blocks for `C(n-1,k;r)`; the second part is
`C(n,k;r+1)`. Thus

```text
N(n-1,k,r) + S(n,k,r+1)  =>  S(n,k,r).
```

The target values satisfy the same additive recurrence. Weyl's inequality is
non-strict on the first summand and strict on the second, so their sum is
strict. This is the published induction with strictness retained block by
block.

## 2. The missing endpoint

At `r=k-1`, prove `S(n,k,k-1)` for all `k>=4` by induction on `n`. The base
`n=k+1` is supplied by the published `k=n-1` result. In the induction step,
equality in Weyl's inequality would require a common top vector for:

1. a standard child under restriction to the point stabilizer; and
2. the full `k`-cycle class on a `k`-set.

Branching leaves only `(n-2,2)`, `(n-2,1,1)`, and the relevant conjugate
partitions. In the two-subset model for `(n-2,2)` and the exterior-square model
for `(n-2,1,1)`, the required intersection is zero. Therefore equality is
impossible and the endpoint is strict.

## 3. Completing the parameter range

- For `k>=4` and `n-k>=3`, combine the endpoint with strict propagation and
  the published non-strict bounds.
- For `k=n-2`, use the published `k=n-1` boundary theorems where their ranges
  apply. The only remaining cases are `(6,4,1)`, `(6,4,2)`, and `(7,5,1)`,
  settled by exact block computations.
- For `k=2,3`, direct Jucys--Murphy formulas give strict inequalities outside
  the target representations.

These cases exhaust `n>=5` and `1<=r<k<=n-2`.

The three finite inputs are now supplied by the self-contained
[exact checker](extension/check.py). Its [results](extension/results.json)
record every block polynomial and threshold root count. The
[source map](extension/sources.md) identifies the precise published boundary
theorems used above.

## 4. What is new

The value carried by the standard representation and the required non-strict
bounds were known. The new step is the strict endpoint and its propagation,
which determines exactly which representations attain the known value.
