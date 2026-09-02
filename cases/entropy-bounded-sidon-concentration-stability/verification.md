# Verification

## Mathematical Review

The complete proof was checked by two fresh read-only mathematical reviewers.
Both reviews returned `CORRECT` for the same frozen statement and proof now
curated in this public case. The checks covered:

1. the exact source locator: arXiv:2506.20813v2, Section 5, physical PDF page
   16, with Proposition 5.2 and condition (42) on physical PDF page 14;
2. the source conventions that the ambient additive group is abelian, entropy
   is Shannon entropy with natural logarithms, and the appearing entropy terms
   are finite;
3. the conditional-entropy identity
   `E log(q_{X+X'}/(p_X p_X')) = 2H(X)-H(X+X')`;
4. the equivalence between condition (42) and the nonnegative surplus estimate
   `E R <= C`;
5. the use of Markov's inequality at threshold `log 2`;
6. the factor of two between ordered pairs and unordered two-element multisets;
7. diagonal collisions, shared endpoints, and torsion in the abelian group;
8. the finite heavy-atom bad-pair graph and the weighted vertex-cover deletion;
9. the infinite light-tail deletion using only `H(X) <= D`;
10. the endpoint cases `C=0`, `0<C<1`, and `C>=1`; and
11. the limit `f(C,D)->0` for each fixed finite `D`.

## Quantitative Extension Review

The optimized modulus extension in [optimal_modulus.md](optimal_modulus.md)
was checked by two additional fresh read-only mathematical reviewers. Both
reviews returned `CORRECT` for the fixed extension statement and proof. The
extension reviews covered:

1. the all-threshold estimate inherited from the main proof;
2. the Lambert-W optimization and the maximum-atom bound;
3. the `C=0` and `D=0` boundary cases;
4. the no-carry integer block construction and all sum-collision classes;
5. the formulas for entropy, defect, and exact Sidon deletion mass;
6. the interval Sidon positive-difference bound for `sigma_m`;
7. the fixed-`D` lower-bound quantifier order in `C`, `eta`, and `m`;
8. the optimized upper-bound asymptotic `x/log(1/C)->1`;
9. the four-point low-entropy construction and its exact deletion mass; and
10. the boundary separating mathematical correctness from public priority.

The public edition uses the corrected source locator: Section 5 spans physical
PDF pages 13-16 of arXiv:2506.20813v2; condition (42) is on page 14, Example
5.4 spans pages 15-16, and the unnumbered open problem is on page 16.

## Public Checker

The checker [check_sidon_stability.py](check_sidon_stability.py) validates the
machine-readable release certificate and runs finite sanity probes over small
abelian groups and rational probability distributions. The probes check the
same construction used in the proof and also enumerate the best Sidon subset
mass in those finite cases. The checker also probes the optimized modulus
certificate: it verifies representative Lambert-W optimizer equations, the
dense no-carry block identities, and the low-entropy four-point witness.

Run it from the repository root:

```bash
python cases/entropy-bounded-sidon-concentration-stability/check_sidon_stability.py
```

Expected output:

```text
PASS: entropy-bounded Sidon stability and optimal-modulus certificates verified
```

## Verification Boundary

The finite probes do not prove the theorem. The theorem-level verification is
the independent mathematical review described above, and the general proof is
[proof.md](proof.md).

The proof has not been encoded in Lean or another proof assistant. Public
novelty and priority remain `NOT_ESTABLISHED`.
