# A q-difference sum-product for partition matrices

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

This case gives an all-order formula for the ordinary generating series

\[
F(q,t)=\sum_{n\geq 1} S_n(q)t^n
\]

of the inversion-weighted partition-matrix polynomials introduced by Chern and
Fu. The formula uses finitely specified auxiliary series, each determined by a
triangular q-difference equation, and proves coefficient equality for every
`n >= 1`.

The source question asks for a closed expression. Because the source does not
turn those words into a formal class of expressions, this public case states
the answered contract explicitly: the expression must be an all-order formal
identity over a specified coefficient ring, with every auxiliary series fixed
by a finite equation or recurrence and with a uniqueness proof. The result
below satisfies that contract without using the original partition-matrix
enumeration as an oracle.

## Contents

- [Problem](problem.md): source definitions, source locator, and exact public
  scope.
- [Proof](proof.md): the self-contained q-difference, column-word,
  inclusion-exclusion, and prefix-path proof.
- [Status](status.md): separate assessments of correctness, completeness, and
  public priority.
- [Verification](verification.md): independent mathematical checks and finite
  regression.
- [Sources](sources.md): the source question and auxiliary prior work.
- [Formula check](formula-check.md): reproduction instructions and output
  boundary.
- [Checker](check_formula.py): a standard-library finite regression through
  size eight.

## Result at a glance

Let \(T_q f(t)=f(qt)\). For each `k >= 1`, let \(R_k(q,t)\in
\mathbb{Z}[q][[t]]\) be the unique constant-term-one solution of

\[
R_k=1+\sum_{r=1}^k(-1)^{r+1}\binom{k}{r}t^r
       \prod_{s=1}^{r-1}(1-q^sT_q)R_k .
\]

Then

\[
\sum_{n\geq1}S_n(q)t^n
  =\sum_{d\geq1}\prod_{k=1}^d\left(1-R_k(q,t)^{-1}\right).
\]

The outer sum is well-defined in the \(t\)-adic topology. At `q=0` it
specializes to the positive-weight Fishburn sum-product, and at `q=1` it
specializes to \(\sum_{d\geq1}d!t^d\).

Public novelty or priority is **NOT_ESTABLISHED**. See [Status](status.md).
