# Complete counterexample argument

Write elements of

$$
G=C_2\oplus C_4^3
$$

as four coordinates modulo $(2,4,4,4)$. Define

$$
a=(0,1,0,0),\qquad
b=(0,0,1,0),\qquad
c=(0,0,0,1),\qquad
T=(1,3,3,3).
$$

Let

$$
p=T-a,
\qquad q=T-b,
\qquad r=T-c,
$$

and consider the length-12 sequence

$$
S=a^3b^3c^3pqr.
$$

The exponents denote repeated labelled occurrences.

## Zero-sum classification

Choose $i,j,k\in\{0,1,2,3\}$ occurrences from the three repeated blocks. Let $\alpha,\beta,\gamma\in\{0,1\}$ record whether $p,q,r$, respectively, are selected, and put

$$
Q=\alpha+\beta+\gamma.
$$

The selected sum is

$$
(i-\alpha)a+(j-\beta)b+(k-\gamma)c+QT.
$$

Consider the homomorphism

$$
\phi:C_4^4\longrightarrow G,
\qquad
\phi(x,y,z,t)=xa+yb+zc+tT.
$$

In coordinates,

$$
\phi(x,y,z,t)=
\bigl(t\bmod 2,\ x+3t,\ y+3t,\ z+3t\bmod 4\bigr).
$$

Solving these congruences gives

$$
\ker(\phi)=
\{(0,0,0,0),(2,2,2,2)\}.
$$

If the coefficient vector is $(0,0,0,0)$ modulo 4, then $Q=0$ because $0\leq Q\leq 3$. Hence $\alpha=\beta=\gamma=0$, and the multiplicity bounds force $i=j=k=0$. This is the empty selection.

If the coefficient vector is $(2,2,2,2)$ modulo 4, then $Q=2$, and the bounds force

$$
i=2+\alpha,
\qquad
j=2+\beta,
\qquad
k=2+\gamma.
$$

The selected length is therefore

$$
i+j+k+Q
=6+(\alpha+\beta+\gamma)+Q
=6+2Q
=10.
$$

Conversely, every selector satisfying these equations is zero-sum. Exactly two of $\alpha,\beta,\gamma$ equal 1. After choosing the zero indicator, there are three ways to choose two labelled occurrences from the corresponding repeated block. Hence $S$ has exactly nine nonempty zero-sum occurrence-subsequences, and every one has length 10.

In particular, $S$ has no nonempty zero-sum occurrence-subsequence of length at most 9. Since $|S|=12$,

$$
s_{\leq9}(G)\geq13>12=D(G)+1.
$$

This contradicts the conclusion of Conjecture 6.1 while satisfying all of its hypotheses. ∎
