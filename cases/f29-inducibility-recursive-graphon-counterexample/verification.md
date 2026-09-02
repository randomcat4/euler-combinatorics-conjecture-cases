# Verification

## Independent Mathematical Review

A fresh read-only mathematical verifier checked the frozen counterexample
package and returned `CORRECT`. The review covered:

1. the exact source target `F29=(6,{03,04,13,15,45})`;
2. the source statement `lambda_F29 = 24/1555`;
3. the induced-density normalization `p(F,W)=|V(F)|!/|Aut(F)| * t(F,W)`;
4. the automorphism count `|Aut(F29)|=10`;
5. the six equal part recursive graphon convention;
6. the bit order and diagonal-state interpretation of the graphon code;
7. an independent exact recursive-density computation; and
8. the strict inequality `6232/402745 > 24/1555`.

The verifier confirmed that a single strict graphon witness is enough to refute
the equality statement, while the package does not claim the true global
optimum or public priority.

## Executable Reproduction

Run:

```bash
python cases/f29-inducibility-recursive-graphon-counterexample/check_counterexample.py
```

The checker uses only the Python standard library. It reads
[counterexample_certificate.json](counterexample_certificate.json), rebuilds the
graph `F29`, recomputes `|Aut(F29)|`, evaluates the recursive graphon densities
over vertex subsets, and checks the exact rational inequalities.

The compact output is recorded in
[verification_summary.json](verification_summary.json).

## Scope Checks

- The result is recorded as `COUNTEREXAMPLE`.
- The claim is limited to Conjecture 4.7's `F29` equality.
- The displayed witness disproves the equality but does not determine `lambda_F29`.
- The case does not claim public priority, first discovery, or novelty.
