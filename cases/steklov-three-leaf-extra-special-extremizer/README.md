# The Steklov extremizer for every leaf count

**Source problem:** Conjecture 1.3 of Lin--Zhao. [Original statement and sources](problem.md).

**[Read the clean proof PDF](paper/extension.pdf)**

**Extension pass (+2h).** For every b>=2 and integer r>=1, the matching threshold nu(T)>=br+2 implies the conjectured sharp Steklov bound, with the unique equality tree. The note also determines the sharp optimum for each positive-integer central leaf split at the smallest possible diameter.

**Initial pass (2h).** The initial package proved the complete three-leaf slice.

The trees are finite, simple and unweighted, with counting measure on the leaf boundary. The two-leaf path endpoint is explicit. Public priority is not established.

[Extension case files and independent checks](extension/)

## Initial public package

The original description and public files below document the initial pass. They remain available; the extension manuscript above gives the later scope.

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

### Contents

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
