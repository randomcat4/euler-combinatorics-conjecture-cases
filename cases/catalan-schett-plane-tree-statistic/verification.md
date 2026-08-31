# Verification

## Mathematical review

The complete proof was subjected to two fresh, mutually isolated, read-only
reviews. Both reviewers returned `CORRECT`. Their checks covered the following
load-bearing points:

1. The statistic `st` is defined in plane-tree language before any
   permutation is introduced, so it is not a transported or circular
   definition.
2. The two cases of `Delta` are mutually exclusive and exhaustive, and the
   construction `Rec` is a genuine two-sided inverse that preserves child
   order.
3. The image of `Phi` consists exactly of the `231`-avoiding permutations;
   the first-letter split used by `Psi` is forced by avoidance.
4. The root is never accidentally included in `mark`. The single correction
   in Case B comes from the path endpoint that is non-root in the original
   tree and becomes the root of the left component.
5. The second coordinate consistently uses `Phi(T)^{-1}`, not `Phi(T)`.
6. The ascending-run splice in equation (17) contributes exactly one when
   the right component's initial inverse ascending run has odd length.
7. Empty blocks, the shortest Case B path, and empty off-path forests are all
   covered by the stated recurrences.
8. The two statistics are preserved simultaneously by the same bijection, so
   the conclusion is a joint distribution identity rather than a pairing of
   unrelated marginal identities.

## Exhaustive finite check

The accompanying checker independently generates every rooted plane-tree
shape and every permutation through size eight. It checks:

- both inverse identities for `Delta` and `Rec`;
- the image and inverse identities for `Phi` and `Psi`;
- direct `231`-avoidance;
- `mark(T)=mnd(Phi(T))`;
- `q(T)=iar(Phi(T)^{-1})`;
- `st(T)=mna(Phi(T)^{-1})`; and
- equality of the complete bivariate frequency tables at each size.

The counts by size are the Catalan numbers:

| Edges/elements | Plane trees | `231`-avoiders |
|---:|---:|---:|
| 0 | 1 | 1 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 5 | 5 |
| 4 | 14 | 14 |
| 5 | 42 | 42 |
| 6 | 132 | 132 |
| 7 | 429 | 429 |
| 8 | 1430 | 1430 |

All assertions pass. This covers 2,056 plane trees in total, including the
single zero-edge recursion base, and checks all 46,234 permutations before
filtering for avoidance.

## Evidence boundary

The finite computation is a calibration and regression check. It cannot prove
the all-order statement. Generality comes from the invertible recursive
decomposition and the induction in [proof.md](proof.md).
