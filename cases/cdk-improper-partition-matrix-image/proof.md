# The CDK image characterization

We prove that, for every `n >= 1`,

\[
\Pi_n(IPPM_n)=\{e\in I_n:\ e\text{ satisfies }C_{\mathrm{pair}}\}.
\]

The proof uses the inverse structure of the Claesson-Dukes-Kubitzke map and
then translates the Chern-Fu parity rule into the value-interval predicate.

## 1. The CDK inverse structure

Let \(P\in PM_n\) have dimension `D`. For `1 <= r <= D`, let \(m_r\) be the
number of labels in column `r`, and put

\[
s_0=0,\qquad s_r=m_1+\cdots+m_r.
\]

Since the column map is weakly increasing in the labels and every column is
nonempty, column `r` of \(P\) contains exactly

\[
\{s_{r-1}+1,s_{r-1}+2,\ldots,s_r\}.
\]

If \(e=\Pi_n(P)\), then the CDK formula gives

\[
e_j=s_{\operatorname{row}_P(j)-1}
\]

for each label `j`. Every row is nonempty, so the distinct values of \(e\) are
exactly

\[
\{s_0<s_1<\cdots<s_{D-1}\}.
\]

Thus, if \(A(e)=\{a_1<\cdots<a_D\}\) and \(a_{D+1}=n\), then
\(a_r=s_{r-1}\), and the interval

\[
B_r(e)=(a_r,a_{r+1}]
\]

is exactly column `r` of \(P\). Also,

\[
\operatorname{row}_P(i)=\operatorname{row}_P(j)
\quad\Longleftrightarrow\quad e_i=e_j,
\]

because the prefix values \(s_0,\ldots,s_{D-1}\) are strictly increasing.

Conversely, start from any \(e\in I_n\). Write
\(A(e)=\{a_1<\cdots<a_D\}\) with \(a_1=0\), and set \(a_{D+1}=n\). Place label
`j` in row `r` when \(e_j=a_r\), and in column `c` when
\(a_c<j\leq a_{c+1}\).

This constructs a partition matrix. Each row is nonempty because each
distinct value \(a_r\) occurs in \(e\). Each column is nonempty because
\(a_c<a_{c+1}\). Labels partition `[n]`, and the column map is weakly
increasing by construction. If a label `j` is placed in row `r` and column
`c`, then \(e_j=a_r<j\) and \(a_c<j\leq a_{c+1}\). If `r > c`, then
\(a_r\geq a_{c+1}\geq j\), a contradiction. Hence `r <= c`, so the matrix is
upper triangular.

The column sizes are \(a_{c+1}-a_c\), so the prefix sum of the first `r-1`
column sizes is

\[
\sum_{c=1}^{r-1}(a_{c+1}-a_c)=a_r.
\]

Applying \(\Pi_n\) to every label in row `r` returns \(a_r=e_j\). Therefore
this construction is \(\Pi_n^{-1}(e)\).

## 2. Improper matrices imply \(C_{\mathrm{pair}}\)

Take \(P\in IPPM_n\) and set \(e=\Pi_n(P)\). Let `i` be an internal odd
transition position of \(e\). Thus `i` and `i+1` lie in the same value interval
\(B_r(e)=(a_r,a_{r+1}]\), and \(i-a_r\) is odd.

By the inverse structure above, labels `i` and `i+1` lie in column `r` of \(P\),
whose minimum label is \(a_r+1\). The condition \(i-a_r\) odd is exactly

\[
i\equiv a_r+1\pmod 2.
\]

If \(e_i\neq e_{i+1}\), then
\(\operatorname{row}_P(i)\neq\operatorname{row}_P(i+1)\). The adjacent
same-column pair is therefore an ascent or descent, and it is proper by the
Chern-Fu parity rule because `i` has the same parity as the minimum label of
that column. This contradicts \(P\in IPPM_n\).

Therefore \(e_i=e_{i+1}\) at every internal odd transition position, so
\(e\) satisfies \(C_{\mathrm{pair}}\).

## 3. \(C_{\mathrm{pair}}\) implies impropriety

Take \(e\in I_n\) satisfying \(C_{\mathrm{pair}}\), and let
\(P=\Pi_n^{-1}(e)\) be the matrix constructed above. We prove \(P\in IPPM_n\).

Consider any ascent or descent at label `i` in \(P\). Then `i` and `i+1` lie in
a common column `r`, and their rows differ. By the inverse structure, they lie
in \(B_r(e)\), the minimum column label is \(a_r+1\), and row inequality is
equivalent to \(e_i\neq e_{i+1}\).

If \(i-a_r\) were odd, then \(C_{\mathrm{pair}}\) would force
\(e_i=e_{i+1}\), a contradiction. Hence \(i-a_r\) is even, or equivalently

\[
i\not\equiv a_r+1\pmod 2.
\]

By the Chern-Fu parity rule, this ascent or descent is improper. The chosen
ascent or descent was arbitrary, so every ascent or descent in \(P\) is
improper. Thus \(P\in IPPM_n\), and \(e\in\Pi_n(IPPM_n)\).

The two inclusions prove the theorem.

## 4. Boundary and semantic checks

For `n=1`, there is no label `i` with `1 <= i < n`. The predicate
\(C_{\mathrm{pair}}\) is vacuous, and the CDK inverse is the one-cell
partition matrix containing `{1}`, which has no ascent or descent.

Intervals of length one impose no condition. If an interval has odd length,
its last label is unpaired in the local matching
\((a_r+1,a_r+2),(a_r+3,a_r+4),\ldots\). No equality condition is attached to
that final label.

If \(i=a_{r+1}\), then `i` and `i+1` lie in adjacent columns rather than one
common column, so neither the Chern-Fu ascent/descent definition nor
\(C_{\mathrm{pair}}\) imposes a condition across that boundary.

Finally, \(C_{\mathrm{pair}}\) is an intrinsic sequence predicate. It is stated
using only \(e\), the sorted set \(A(e)\), the standard label order, and
equality comparisons between adjacent entries. The proof uses
\(\Pi_n^{-1}\) only to prove equivalence with source-side impropriety.
