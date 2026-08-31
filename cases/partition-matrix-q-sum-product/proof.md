# An all-order q-difference sum-product

Let \(T_q\) be the q-shift operator on formal power series in `t`:

\[
(T_q f)(t)=f(qt).
\]

For each integer `k >= 1`, let \(R_k(q,t)\) be the unique series in
\(\mathbb{Z}[q][[t]]\) with constant term one satisfying

\[
R_k(q,t)=1+\sum_{r=1}^k(-1)^{r+1}\binom{k}{r}t^r
       \prod_{s=1}^{r-1}(1-q^sT_q)R_k(q,t). \tag{A}
\]

An empty operator product is the identity. We prove

\[
\sum_{n\geq1}S_n(q)t^n
  =\sum_{d\geq1}\prod_{k=1}^d\left(1-R_k(q,t)^{-1}\right)        \tag{B}
\]

in \(\mathbb{Z}[q][[t]]\).

## 1. The auxiliary word series

For `m >= 0` and `k >= 1`, let

\[
H_{m,k}(q)=\sum_w q^{\operatorname{inv}(w)},
\]

where the sum is over all length-`m` words on the ordered alphabet `[k]` and
\(\operatorname{inv}(w)\) is the usual word inversion number. Sorting words by
letter multiplicities gives

\[
H_{m,k}(q)=
\sum_{a_1+\cdots+a_k=m}
\begin{bmatrix}m\\a_1,\ldots,a_k\end{bmatrix}_q.        \tag{1}
\]

Set

\[
\widehat R_k(q,t)=\sum_{m\geq0}H_{m,k}(q)t^m .
\]

We first identify this series as the unique solution of (A), so the final
formula does not need to query the partition-matrix definition.

Write \((q;q)_m=\prod_{i=1}^m(1-q^i)\), with \((q;q)_0=1\), and work
temporarily in \(\mathbb{Q}(q)[[z]]\). Equation (1) implies

\[
E_k(q,z):=\sum_{m\geq0}\frac{H_{m,k}(q)}{(q;q)_m}z^m
=\left(\sum_{a\geq0}\frac{z^a}{(q;q)_a}\right)^k .
\]

For \(e(z)=\sum_{a\geq0}z^a/(q;q)_a\), direct coefficient comparison gives
\[
e(qz)=(1-z)e(z).
\]
Indeed, for `a >= 1`, the coefficient of \(z^a\) on the right is
\[
\frac{1}{(q;q)_a}-\frac{1}{(q;q)_{a-1}}=\frac{q^a}{(q;q)_a},
\]
and the constant terms also agree. Raising to the `k`th power gives

\[
E_k(q,qz)=(1-z)^kE_k(q,z).                         \tag{2}
\]

Comparing the coefficient of \(z^m\), moving the `r=0` term to the left, and
multiplying by \((q;q)_{m-1}\) yields, with \(H_{j,k}=0\) for `j < 0`,

\[
H_{m,k}(q)=
\sum_{r=1}^{\min(k,m)}(-1)^{r+1}\binom{k}{r}
\prod_{s=1}^{r-1}\left(1-q^{m-r+s}\right)H_{m-r,k}(q).        \tag{3}
\]

Multiplying (3) by \(t^m\) and summing over `m >= 1` gives (A), because the
coefficient of \(t^u\) in

\[
\prod_{s=1}^{r-1}(1-q^sT_q)\widehat R_k
\]

is

\[
\prod_{s=1}^{r-1}\left(1-q^{u+s}\right)H_{u,k}(q).
\]

Conversely, the coefficient of \(t^m\) on the right side of (A) depends only
on coefficients of degrees at most `m-1`. The constant term one therefore
gives uniqueness over any coefficient ring, and recurrence (3) constructs the
solution in \(\mathbb{Z}[q][[t]]\). Hence \(R_k=\widehat R_k\).

## 2. Partition matrices as column words

Fix a partition matrix `P` of dimension `d`. Since the column positions are
weakly increasing with the labels and every column is nonempty, the labels in
column `j` form a nonempty consecutive interval. Read those labels in
increasing order and record their row indices. This produces a nonempty word
\(w_j\in[j]^+\), because upper triangularity restricts column `j` to rows
`1,\ldots,j`.

Every row of `P` is nonempty exactly when every letter in `[d]` occurs in at
least one of \(w_1,\ldots,w_d\). Conversely, any sequence of nonempty words
\[
w_j\in[j]^+,\qquad 1\leq j\leq d,
\]
in which every letter of `[d]` occurs reconstructs a unique partition matrix:
split `[n]` into consecutive intervals of lengths
\(|w_1|,\ldots,|w_d|\), and place each label in the row specified by its word
letter. This proves a bijection.

If `i > j` lie in the same matrix column, then `j` is read before `i` in the
associated word. The matrix inversion condition \(\operatorname{row}(i) <
\operatorname{row}(j)\) says exactly that the earlier word letter is larger
than the later one. Hence

\[
\operatorname{inv}(P)=\sum_{j=1}^d\operatorname{inv}(w_j).       \tag{4}
\]

Let \(W_k(q,t)=R_k(q,t)-1\) for `k >= 1`; this is the nonempty-word series on
alphabet `[k]`. Set \(W_0=0\).

## 3. Complete row inclusion-exclusion

Let \(F_d(q,t)\) be the weight series for dimension-`d` partition matrices.
Apply inclusion-exclusion to the row letters that fail to occur. If
\(A\subseteq[d]\) is forbidden, then column `j` retains the ordered alphabet
\([j]\setminus A\), which is order-isomorphic to an alphabet of size

\[
j-|A\cap[j]|.
\]

Using (4), the column contributions multiply and we get

\[
F_d(q,t)=\sum_{A\subseteq[d]}(-1)^{|A|}
       \prod_{j=1}^d W_{j-|A\cap[j]|}(q,t).                \tag{5}
\]

Column nonemptiness is enforced by \(W\), upper triangularity by the prefix
alphabet, and row nonemptiness by the alternating sum.

## 4. Binary prefix paths

Encode \(A\subseteq[d]\) by the path \(k_0=0\) and

\[
k_j-k_{j-1}=
\begin{cases}
1,&j\notin A,\\
0,&j\in A.
\end{cases}
\]

A rise arriving at level `k` contributes \(W_k\), while a stay at level `k`
contributes \(-W_k\). If the first step is a stay, the path has factor
\(W_0=0\), so every nonzero path first rises to level one.

When (5) is summed over all dimensions, a finite nonzero path with maximum
level \(\ell\) has exactly one rise into each level \(1,\ldots,\ell\),
followed by a uniquely determined number \(s_k\geq0\) of stays at that level.
The total contribution of level `k` is therefore

\[
\sum_{s_k\geq0}W_k(-W_k)^{s_k}
  =\frac{W_k}{1+W_k}
  =1-R_k^{-1}.                                           \tag{6}
\]

The geometric series is legitimate formally because \(W_k\) has zero constant
term. Multiplying (6) over the attained levels and summing over \(\ell\geq1\)
gives the right side of (B).

The infinite regrouping is coefficientwise finite: each factor
\(1-R_k^{-1}\) has \(t\)-adic order at least one, so the summand with maximum
level \(\ell\) has order at least \(\ell\). Only finitely many summands can
contribute to a fixed coefficient of \(t^n\). Also, every \(R_k\) is
invertible because its constant term is one. Equations (4) and (5) show that
the coefficient of \(t^n\) in (B) is exactly \(S_n(q)\) for every `n >= 1`.

This proves the theorem.

## 5. Boundary specializations

For `k=1`, equation (A) is \(R_1=1+tR_1\), so \(R_1=(1-t)^{-1}\).

At `q=0`, a word has inversion weight one exactly when it is weakly
increasing. Hence

\[
R_k(0,t)=\sum_{m\geq0}\binom{m+k-1}{k-1}t^m=(1-t)^{-k},
\]

and (B) becomes

\[
F(0,t)=\sum_{d\geq1}\prod_{k=1}^d\left(1-(1-t)^k\right),
\]

the positive-weight Fishburn sum-product.

At `q=1`, every word of length `m` on `[k]` has weight one, so
\(R_k(1,t)=(1-kt)^{-1}\). Therefore

\[
F(1,t)=\sum_{d\geq1}\prod_{k=1}^d kt
       =\sum_{d\geq1}d!t^d,
\]

as required by \(S_d(1)=|PM_d|=d!\).
