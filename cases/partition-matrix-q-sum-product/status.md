# Status

## Mathematical result

**Proved.** The proof gives an all-order formal identity for
\(\sum_{n\geq1}S_n(q)t^n\) in \(\mathbb{Z}[q][[t]]\). It supplies:

- a finite q-difference specification of every auxiliary series \(R_k\);
- a coefficient-triangular uniqueness proof for those auxiliaries;
- a bijection from dimension-`d` partition matrices to nonempty column words
  whose combined alphabets contain every row letter;
- inversion preservation under that encoding;
- complete inclusion-exclusion over missing rows;
- a coefficientwise legitimate prefix-path resummation; and
- the `q=0`, `q=1`, and smallest-boundary checks.

Two independent read-only mathematical reviews returned `CORRECT` for the same
frozen all-order proof. A finite checker also compares the formula with direct
enumeration through size eight. The finite check is supporting evidence, not
the general proof.

## Public priority

**NOT_ESTABLISHED.** The material in this case does not claim novelty,
priority, first discovery, or absence of unpublished or subsequently published
work. The source question belongs to Chern and Fu. The bounded literature audit
found no same or stronger formula in its denominator, but that is not an
exhaustive public-priority determination.

## Scope

This directory presents a conventional mathematical proof and a reproducible
finite regression. It is not proof-assistant verification, journal peer review,
an authorship determination, or an arXiv submission.

The case answers the explicitly stated finite all-order expression contract in
[problem.md](problem.md). It does not assert that every possible meaning of
"closed expression" has been formalized or exhausted.
