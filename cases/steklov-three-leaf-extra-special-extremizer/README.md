# Steklov Three-Leaf Extra-Special Extremizer

*Huiqiu Lin and Da Zhao · [arXiv](https://arxiv.org/abs/2508.13466v1)*

This case records a partial result for Conjecture 1.3 in Lin and Zhao,
*Comparison between the first Steklov eigenvalue and algebraic connectivity on
trees*. The public scope is the complete infinite \(b=3\) slice.

Let \(T\) be a finite simple unweighted tree whose boundary is its leaf set.
For every integer \(r\geq1\), if \(T\) has exactly three leaves and matching
number \(\nu(T)=3r+2\), then

\[
\sigma_2(T)\leq \sigma_2^-(ES_{3,2r}),
\]

with equality if and only if \(T\) is the extra-special tree

\[
ES_{3,2r}=Sp_{1,1,1;2r+2,2r+1,2r}.
\]

Equivalently, the unique unordered arm-length triple attaining equality is
\(\{2r+2,2r+1,2r\}\).

The case proves only this \(b=3\) slice. It does not address the source
conjecture for \(b=2\) or \(b\geq4\), and it does not claim public priority.

## Contents

- [Problem](problem.md): source locator, definitions, and exact public scope.
- [Proof](proof.md): spider reduction, Steklov formula, matching formula, and
  parity optimization.
- [Status](status.md): correctness, completeness, and priority boundaries.
- [Verification](verification.md): independent mathematical review and
  executable calibration.
- [Sources](sources.md): source and related-work boundary.
- [Certificate](spider_certificate.json): expected finite calibration summary.
- [Checker](check_three_leaf_extremizer.py): standard-library bounded
  reproduction of the arithmetic and matching checks.

Public novelty or priority is **NOT_ESTABLISHED**. See [Status](status.md).
