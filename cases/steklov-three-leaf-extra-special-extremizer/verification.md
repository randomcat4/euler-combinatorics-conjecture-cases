# Verification

## Independent Mathematical Review

A fresh read-only mathematical verifier checked the frozen \(b=3\) statement
and returned `CORRECT`. The review covered:

1. the source alignment with arXiv:2508.13466v1, Conjecture 1.3, and the
   leaf-boundary convention;
2. the identification \(ES_{3,2r}=Sp_{1,1,1;2r+2,2r+1,2r}\);
3. the proof that every three-leaf tree is a three-arm spider;
4. the Dirichlet-to-Neumann matrix and the exact formula
   \(\sigma_2=3/(S+\sqrt{S^2-3Q})\);
5. the matching-number formula for a three-arm spider;
6. the four parity-constrained optimizations and equality uniqueness;
7. the substitution into the source formula for \(\sigma_2^-(ES_{3,2r})\);
   and
8. the boundary statement that the result covers only \(b=3\).

The verifier confirmed that the proof establishes the complete infinite
three-leaf slice, not merely a finite no-hit search.

## Executable Reproduction

Run:

```bash
python cases/steklov-three-leaf-extra-special-extremizer/check_three_leaf_extremizer.py
```

The checker uses only the Python standard library. It verifies the matching
formula against an explicit tree dynamic program for all arm lengths up to 16,
then checks the parity-class extremizer arithmetic for all \(1\leq r\leq80\)
over the complete feasible spider denominator in that range.

The compact output is recorded in
[verification_summary.json](verification_summary.json).

## Scope Checks

- The result is recorded as `PARTIAL_RESULT`.
- The claim covers all \(r\geq1\) only when the tree has exactly three leaves.
- The old finite \(n\leq16\) no-hit computation is not used as a proof of the
  general theorem.
- Public novelty and priority remain `NOT_ESTABLISHED`.
