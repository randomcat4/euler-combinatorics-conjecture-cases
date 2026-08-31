# Status

## Mathematical result

**Proved.** The case gives a complete all-order characterization of the CDK
image of improper partition matrices:

\[
\Pi_n(IPPM_n)=\{e\in I_n:\ e\text{ satisfies }C_{\mathrm{pair}}\}
\]

for every `n >= 1`.

The proof supplies:

- the explicit inverse structure of the CDK map in terms of distinct values of
  the inversion sequence;
- proof that CDK columns are exactly the intervals \((a_r,a_{r+1}]\);
- proof that row equality is exactly equality of the corresponding
  inversion-sequence values;
- both inclusions between the improper image and the intrinsic predicate;
- the exact parity translation from Chern-Fu proper ascent/descent pairs; and
- boundary checks for `n=1`, length-one intervals, odd-length intervals, value
  boundaries, and adjacent-label scope.

Two independent read-only mathematical reviews returned `CORRECT` for the same
frozen theorem and proof. A finite checker also compares the characterization
with the CDK inverse impropriety test through size eight. The finite check is
supporting evidence, not the general proof.

## Public priority

**NOT_ESTABLISHED.** The material in this case does not claim novelty,
priority, first discovery, or absence of unpublished or subsequently published
work. The bounded literature audit found no same or stronger public result in
its denominator, but that is not an exhaustive public-priority determination.

## Scope

This directory presents a conventional mathematical proof and a reproducible
finite regression. It is not proof-assistant verification, journal peer review,
an authorship determination, or an arXiv submission.

The source locator is version-sensitive: this case treats Question 5.5 in
arXiv:2508.21318v2. In arXiv version 1, Question 5.5 is a different problem.
