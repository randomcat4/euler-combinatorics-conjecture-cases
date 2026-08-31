# Problem

## Source locator

The source is Shane Chern and Shishuo Fu, "Signed counting of partition
matrices," *Journal of Combinatorial Theory, Series A* 223 (2026), Article
106213, DOI `10.1016/j.jcta.2026.106213`.

In arXiv:2508.21318v2, Section 5, "Outlook," Question 5.5 appears on
printed/PDF page 26 and asks for a characterization of the inversion sequences
obtained from improper partition matrices under the Claesson-Dukes-Kubitzke
map. This locator is version-sensitive: in arXiv version 1, Question 5.5 is a
different direct-bijection problem, now numbered Question 5.7 in version 2.

## Definitions

Write `[n]={1,\ldots,n}`. A partition matrix on `[n]` is an
upper-triangular square matrix whose nonempty entries partition `[n]`, whose
every row and column contains a nonempty entry, and whose labels weakly
increase by column: if `i < j`, then `col_P(i) <= col_P(j)`. Let `PM_n` be the
set of partition matrices on `[n]`.

An inversion sequence of length `n` is a sequence
\[
e=(e_1,\ldots,e_n)
\]
with `0 <= e_i <= i-1` for every `i`. Let `I_n` be the set of such sequences.

If `P` has dimension `D` and column sizes \(m_1,\ldots,m_D\), the
Claesson-Dukes-Kubitzke map \(\Pi_n:PM_n\to I_n\), in the form used by Chern
and Fu, is

\[
e_j=\sum_{c=1}^{\operatorname{row}_P(j)-1}m_c,
\qquad 1\leq j\leq n.
\]

For `1 <= i < n`, the adjacent pair `(i,i+1)` is a descent pair when both
labels lie in the same column and `row_P(i)>row_P(i+1)`, and an ascent pair
when both labels lie in the same column and `row_P(i)<row_P(i+1)`. Let `j` be
the smallest label in that common column. Chern and Fu call the ascent or
descent at `i` proper when `i` and `j` have the same parity, and improper
otherwise. A partition matrix is improper when every ascent or descent, when
present, is improper. Let `IPPM_n` be the subset of improper partition
matrices.

## The intrinsic predicate

For \(e\in I_n\), write the set of distinct values of \(e\) as

\[
A(e)=\{a_1<a_2<\cdots<a_D\}.
\]

Since \(e_1=0\), one has \(a_1=0\). Set \(a_{D+1}=n\). Define value intervals

\[
B_r(e)=(a_r,a_{r+1}]=\{a_r+1,\ldots,a_{r+1}\}.
\]

Say that \(e\) satisfies \(C_{\mathrm{pair}}\) if, whenever
\[
a_r<i<a_{r+1}\quad\text{and}\quad i-a_r\text{ is odd},
\]
one has \(e_i=e_{i+1}\). Equivalently, inside every interval \(B_r(e)\), the
adjacent local pairs
\[
(a_r+1,a_r+2),\ (a_r+3,a_r+4),\ldots
\]
must have equal \(e\)-values whenever both labels exist.

## The theorem

For every `n >= 1`,

\[
\Pi_n(IPPM_n)=\{e\in I_n:\ e\text{ satisfies }C_{\mathrm{pair}}\}.
\]

A complete answer must prove both inclusions for all `n`, cover the endpoint
`n=1`, handle intervals of length one and odd length, avoid imposing
conditions across value boundaries, and keep finite enumeration separate from
the all-order proof.
