# Proof of the Three-Leaf Slice

Let \(r\geq1\), and let \(T\) be a finite tree with exactly three leaves and
matching number \(\nu(T)=3r+2\). The Steklov boundary is the leaf set.

## 1. Reduction to a Spider

For any finite tree,

\[
\sum_{v\in V(T)}(\deg(v)-2)=-2.
\]

If \(L\) is the number of leaves, then the vertices of degree at least three
satisfy

\[
\sum_{\deg(v)\geq3}(\deg(v)-2)=L-2.
\]

When \(L=3\), the right side is \(1\). Hence there is exactly one branch
vertex, it has degree \(3\), and all other non-leaf vertices have degree
\(2\). Therefore \(T\) is a three-arm spider. Write its positive arm lengths
as an unordered triple \((a,b,c)\), and set

\[
S=a+b+c,\qquad Q=ab+ac+bc.
\]

## 2. The Leaf-Boundary Steklov Formula

Set \(w_a=1/a\), \(w_b=1/b\), \(w_c=1/c\), and \(W=w_a+w_b+w_c\). If the
boundary values are \(x_a,x_b,x_c\), the harmonic value \(u\) at the center is

\[
u=\frac{w_ax_a+w_bx_b+w_cx_c}{W}.
\]

The outward normal derivative at leaf \(i\) is \(w_i(x_i-u)\). Thus the
Dirichlet-to-Neumann matrix on the three leaves is

\[
\Lambda=\operatorname{diag}(w_a,w_b,w_c)-\frac{1}{W}ww^T.
\]

It has kernel spanned by \((1,1,1)\). The sum of its two nonzero eigenvalues is

\[
\operatorname{tr}(\Lambda)=\frac{2S}{Q},
\]

and the product of the two nonzero eigenvalues is

\[
\frac{3}{Q},
\]

because the sum of the three principal \(2\times2\) minors is
\(3w_aw_bw_c/W\). Therefore the Steklov characteristic polynomial is

\[
x\left(x^2-\frac{2S}{Q}x+\frac{3}{Q}\right),
\]

and the first nonzero Steklov eigenvalue is

\[
\sigma_2(T)=\frac{S-\sqrt{S^2-3Q}}{Q}
           =\frac{3}{S+\sqrt{S^2-3Q}}.
\]

Maximizing \(\sigma_2(T)\) is therefore equivalent to minimizing

\[
D(a,b,c)=S+\sqrt{S^2-3Q}.
\]

## 3. Matching Number of a Three-Arm Spider

If the center is not matched to an arm of length \(a\), that arm contributes
\(\lfloor a/2\rfloor\) matching edges. If the center is matched into that arm,
the arm contributes

\[
1+\left\lfloor\frac{a-1}{2}\right\rfloor=\left\lceil\frac{a}{2}\right\rceil.
\]

At most one matching edge can use the center. Hence

\[
\nu(T)=
\left\lfloor\frac a2\right\rfloor+
\left\lfloor\frac b2\right\rfloor+
\left\lfloor\frac c2\right\rfloor+
\mathbf{1}_{\text{at least one of }a,b,c\text{ is odd}}.
\]

The formula is exact: if no arm is odd, use maximum no-center matchings on all
arms; if an odd arm exists, match the center into one odd arm and use maximum
no-center matchings elsewhere.

## 4. Four Parity Classes

Write each arm length as

\[
\ell_i=2u_i+\epsilon_i,\qquad \epsilon_i\in\{0,1\},
\]

and let \(t=\epsilon_1+\epsilon_2+\epsilon_3\) be the number of odd arms. The
condition \(\nu(T)=3r+2\) gives:

- if \(t=0\), then \(u_1+u_2+u_3=3r+2\);
- if \(t>0\), then \(u_1+u_2+u_3=3r+1\).

For fixed \(t\), the sum \(S\) is fixed. Since

\[
S^2-3Q=\frac{3(a^2+b^2+c^2)-S^2}{2},
\]

minimizing \(D(a,b,c)\) in a fixed parity class is equivalent to minimizing
\(a^2+b^2+c^2\) with the fixed sum and parity pattern.

The elementary smoothing rule is the following. If two same-parity entries
differ by at least \(4\), replacing them by \((x-2,y+2)\) preserves the sum
and parity pattern and lowers the square sum. If two opposite-parity entries
differ by at least \(3\), replacing them by \((x-1,y+1)\) preserves the number
of odd entries, swaps the two parities, and lowers the square sum. Thus a
minimizer must be parity-balanced.

The four forced class minimizers are:

| odd arms \(t\) | unique representative | \(D=S+\sqrt{S^2-3Q}\) |
| ---: | --- | --- |
| 0 | \((2r+2,2r+2,2r)\) | \(6r+6\) |
| 1 | \((2r+2,2r+1,2r)\) | \(6r+3+\sqrt3\) |
| 2 | \((2r+2,2r+1,2r+1)\) | \(6r+5\) |
| 3 | \((2r+3,2r+1,2r+1)\) | \(6r+7\) |

Because \(\sqrt3<2\), the unique smallest denominator is
\(6r+3+\sqrt3\), attained only when the arm lengths are

\[
\{a,b,c\}=\{2r+2,2r+1,2r\}.
\]

Since \(\sigma_2(T)=3/D(a,b,c)\), this is the unique maximizer.

## 5. Identification with the Source Extremizer

Source Definition 2.4 identifies

\[
ES_{3,2r}=Sp_{1,1,1;2r+2,2r+1,2r}.
\]

Source Lemma 2.5 gives

\[
\sigma_2^-(ES_{b;p})
=
\frac{2bp+3b-3-\sqrt{b^2-2b+9}}
     {2(bp^2+3bp-3p+2b-4)}.
\]

Substituting \(b=3\) and \(p=2r\) yields

\[
\sigma_2^-(ES_{3,2r})
=
\frac{6r+3-\sqrt3}{12r^2+12r+2}
=
\frac{3}{6r+3+\sqrt3}.
\]

Therefore every three-leaf tree with \(\nu(T)=3r+2\) satisfies

\[
\sigma_2(T)\leq\sigma_2^-(ES_{3,2r}),
\]

with equality if and only if \(T\cong ES_{3,2r}\). This proves the complete
\(b=3\) slice.
