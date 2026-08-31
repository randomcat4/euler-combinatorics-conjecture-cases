# The CDK image of improper partition matrices

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

This case characterizes exactly which inversion sequences arise from improper
partition matrices under the Claesson-Dukes-Kubitzke bijection. The result is
a complete all-order answer to Chern and Fu's arXiv v2 Question 5.5.

For an inversion sequence \(e=(e_1,\ldots,e_n)\), let
\[
A(e)=\{a_1<\cdots<a_D\}
\]
be the set of distinct values of \(e\), with \(a_1=0\), and set
\(a_{D+1}=n\). The image is exactly the set of inversion sequences for which,
inside every interval \((a_r,a_{r+1}]\), the adjacent local pairs
\[
(a_r+1,a_r+2),\ (a_r+3,a_r+4),\ldots
\]
have equal \(e\)-values whenever both labels exist.

The statement is intrinsic to the inversion sequence: the membership test uses
only \(e\), its sorted set of values, the label order, and equality of adjacent
entries. The inverse partition matrix is used in the proof, not as the
definition of the right-hand side.

## Contents

- [Problem](problem.md): definitions, source locator, and exact theorem scope.
- [Proof](proof.md): CDK inverse structure and both inclusions.
- [Status](status.md): separate assessments of correctness, completeness, and
  public priority.
- [Verification](verification.md): independent mathematical checks and finite
  regression.
- [Sources](sources.md): the source problem and CDK reference.
- [Finite regression](finite-regression.md): reproduction instructions and
  limitations.
- [Checker](mine_cdk_image.py): a standard-library finite check through size
  eight.
- [Certificate](mining_n_le_8.json): compact output of the finite check.

## Result at a glance

Let \(\Pi_n:PM_n\to I_n\) be the CDK bijection in the form used by Chern and
Fu. For every `n >= 1`,

\[
\Pi_n(IPPM_n)=\{e\in I_n:\ e\text{ satisfies }C_{\mathrm{pair}}\}.
\]

The finite regression checks all 46,233 inversion sequences with `1 <= n <= 8`
and finds zero symmetric difference between the CDK improper image and the
intrinsic predicate. That computation is auxiliary; the all-order result is
proved in [proof.md](proof.md).

Public novelty or priority is **NOT_ESTABLISHED**. See [Status](status.md).
