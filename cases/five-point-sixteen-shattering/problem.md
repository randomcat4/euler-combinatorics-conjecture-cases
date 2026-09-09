# Problem and Released Scope

## Definitions

Let `[n]={1,...,n}`. A permutation of `[n]` induces a relative order on each
subset by restriction. A family `F` of permutations `t`-shatters a set `X`
when the restrictions of the members of `F` to `X` contain at least `t`
distinct relative orders.

Write `f_k(n,t)` for the minimum size of a family of permutations of `[n]`
that `t`-shatters every `k`-element subset.

## Source Conjecture

Conjecture 4.2 of Girao--Michel--Tamitegama asserts that, for every fixed
integer `k>=3` and every fixed `1<=t<=2^(k-1)`,

```text
f_k(n,t) = o(log n)
```

as `n` tends to infinity.

## Released Theorem

For every integer `n>=5`, there is a family `F_n` of permutations of `[n]`
such that:

1. `F_n` is fixed before any five-element subset is selected;
2. every five-element subset has at least 16 distinct induced orders under
   `F_n`; and
3. `|F_n|=O(sqrt(log n * log log n))`, with an absolute implied constant.

Thus `f_5(n,t)=o(log n)` for every fixed `1<=t<=16`. This is the complete
`k=5` parameter slice of the source conjecture.

## Scope Boundary

The released theorem does not claim:

- Conjecture 4.2 for any `k` other than `5`;
- an exact asymptotic formula or a matching upper and lower bound;
- an extension past `t=16`;
- a complete formal proof in Lean;
- public priority or firstness.

The finite executable check in this case verifies one four-point lemma only.
The all-`n` statement follows from the analytic construction in
[proof.md](proof.md), not from finite enumeration.
