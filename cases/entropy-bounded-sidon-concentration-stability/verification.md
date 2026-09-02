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

## Public Checker

The checker [check_sidon_stability.py](check_sidon_stability.py) validates the
machine-readable release certificate and runs finite sanity probes over small
abelian groups and rational probability distributions. The probes check the
same construction used in the proof and also enumerate the best Sidon subset
mass in those finite cases.

Run it from the repository root:

```bash
python cases/entropy-bounded-sidon-concentration-stability/check_sidon_stability.py
```

Expected output:

```text
PASS: entropy-bounded Sidon stability certificate and finite probes verified
```

## Verification Boundary

The finite probes do not prove the theorem. The theorem-level verification is
the independent mathematical review described above, and the general proof is
[proof.md](proof.md).

The proof has not been encoded in Lean or another proof assistant. Public
novelty and priority remain `NOT_ESTABLISHED`.
