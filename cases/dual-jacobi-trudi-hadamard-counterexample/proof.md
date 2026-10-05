# A counterexample for two different dual Jacobi–Trudi shapes

Let $x$ and $y$ be disjoint alphabets of commuting indeterminates, and let $e_d$ denote the elementary symmetric function of degree $d$. Write
$$
E_{\lambda/\mu}(x)=(e_{\lambda_i-\mu_j-i+j}(x))_{i,j=1}^3,
$$
where $e_0=1$ and $e_d=0$ for $d<0$. We use the shape convention of Angarone, Kim, Oh and Soskin, *Hadamard products of dual Jacobi–Trudi matrices*, [arXiv:2511.08969v1](https://arxiv.org/html/2511.08969v1), Introduction and Remark 2.1. Their Conjecture 1.2 asserts monomial positivity for every Temperley–Lieb immanant of every family of such matrices. Section 2.3 identifies the identity-diagram immanant with the determinant.

Take the legal skew shapes
$$
\lambda/\mu=(18,18,15)/(2,0,0),\qquad
\rho/\nu=(20,18,18)/(2,2,0).
$$
The outer and inner sequences are partitions, with componentwise containment; the inner partitions are padded with trailing zeros. Their sizes are 49 and 52. The degree matrices are
$$
\begin{pmatrix}16&19&20\\15&18&19\\11&14&15\end{pmatrix},\qquad
\begin{pmatrix}18&19&22\\15&16&19\\14&15&18\end{pmatrix}.
$$

We compute the coefficient of
$$
X=x_1\cdots x_{49},\qquad
Y=y_1\cdots y_{20}y_{21}^2\cdots y_{36}^2
$$
in $\det(E_{\lambda/\mu}(x)*E_{\rho/\nu}(y))$, where $*$ means entrywise product.

For $a+b+c=49$, the coefficient of $X$ in $e_a(x)e_b(x)e_c(x)$ is $49!/(a!b!c!)$: assign each distinct variable to exactly one factor. For the right alphabet,
$$
[Y]e_a(y)e_b(y)e_c(y)
=[u^av^bw^c](u+v+w)^{20}(uv+uw+vw)^{16}.
$$
Each variable of exponent one chooses one factor, and each variable of exponent two chooses two different factors. Thus every coefficient in this formula is an exact finite integer count.

Explicitly, for selected right degrees $(d_1,d_2,d_3)$, let $\ell_i$ count the doubled variables that omit factor $i$. The number of single variables assigned to that factor is then $d_i-16+\ell_i$, so its coefficient is
$$
\sum_{\substack{\ell_1,\ell_2,\ell_3\ge0\\\ell_1+\ell_2+\ell_3=16}}
\binom{16}{\ell_1,\ell_2,\ell_3}
\binom{20}{d_1-16+\ell_1,d_2-16+\ell_2,d_3-16+\ell_3}.
$$
A multinomial with a negative lower entry is zero. This finite sum evaluates every right coefficient in the table below.

For each permutation $\pi$, let $A_\pi$ and $B_\pi$ be the coefficients obtained from the three selected matrix entries. The six values are:

| $\pi$ | sign | $A_\pi$ | $B_\pi$ |
|---|---:|---:|---:|
| 123 | + | 3472519098347437335120 | 3051252895132450 |
| 132 | − | 2741462446063766317200 | 2388914981277920 |
| 213 | − | 2924226609134684071680 | 2388914981277920 |
| 231 | + | 1029816646405790443200 | 1719046929283200 |
| 312 | + | 2193169956851013053760 | 902433439091120 |
| 321 | − | 978325814085500921040 | 829443998405960 |

The Leibniz formula gives
$$
\begin{aligned}
[XY]\det(E_{\lambda/\mu}(x)*E_{\rho/\nu}(y))
&=\sum_{\pi\in S_3}\operatorname{sgn}(\pi)A_\pi B_\pi\\
&=-1288935568443079606185991333432800<0.
\end{aligned}
$$
This disproves the printed Conjecture 1.2. Separate symmetry in the two alphabets also makes this the coefficient of $m_{(1^{49})}(x)m_{(2^{16},1^{20})}(y)$.

The shapes differ, so this witness does not settle Sokal's same-shape Conjecture 1.1. Both shapes contain a $3\times2$ block, so they lie outside the hypothesis of Theorem 1.3 in the source. No minimality or priority claim is made.
