# Counterexample arguments

## Conjecture 6.1

Write elements of $G=C_2\oplus C_4^3$ as four coordinates modulo $(2,4,4,4)$. Define

$$
a=(0,1,0,0),\qquad
b=(0,0,1,0),\qquad
c=(0,0,0,1),\qquad
T=(1,3,3,3).
$$

Let

$$
p=T-a,\qquad q=T-b,\qquad r=T-c,
$$

and consider the length-12 sequence

$$
S=a^3b^3c^3pqr.
$$

Choose $i,j,k\in\{0,1,2,3\}$ occurrences from the three repeated blocks. Let $\alpha,\beta,\gamma\in\{0,1\}$ record whether $p,q,r$ are selected, and put $Q=\alpha+\beta+\gamma$. The selected sum is

$$
(i-\alpha)a+(j-\beta)b+(k-\gamma)c+QT.
$$

Consider the homomorphism

$$
\phi:C_4^4\longrightarrow G,\qquad
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

If the coefficient vector is $(0,0,0,0)$ modulo 4, then $Q=0$ because $0\leq Q\leq3$. Hence $\alpha=\beta=\gamma=0$, and the multiplicity bounds force $i=j=k=0$. This is the empty selection.

If the coefficient vector is $(2,2,2,2)$ modulo 4, then $Q=2$, and the bounds force

$$
i=2+\alpha,\qquad j=2+\beta,\qquad k=2+\gamma.
$$

The selected length is therefore

$$
i+j+k+Q=6+(\alpha+\beta+\gamma)+Q=6+2Q=10.
$$

Conversely, every selector satisfying these equations is zero-sum. Exactly two of $\alpha,\beta,\gamma$ equal 1. After choosing the zero indicator, there are three ways to choose two labelled occurrences from the corresponding repeated block. Hence $S$ has exactly nine nonempty zero-sum occurrence-subsequences, and every one has length 10.

In particular, $S$ has no nonempty zero-sum occurrence-subsequence of length at most 9. Since $|S|=12$,

$$
s_{\leq9}(G)\geq13.
$$

Zhao's Theorem 1.11 gives the matching upper bound $s_{\leq9}(G)\leq13$ for this group, so

$$
s_{\leq9}(C_2\oplus C_4^3)=13.
$$

Conjecture 6.1 predicts $D(G)+1=12$, so it is false.

## Conjecture 6.2: Infinite Upper-Branch Family

Let $G=C_n^4$, where $n\geq2$ is a prime power. Then $D(G)=D^*(G)=4n-3$. Let $e_1,e_2,e_3,e_4$ be the standard basis, and define the sequence

$$
S_n=\prod_{A\subseteq\{2,3,4\}}
\left(e_1+\sum_{i\in A}e_i\right)^{n-1}.
$$

It has length $8(n-1)$. Suppose a nonempty subsequence $U$ of $S_n$ is zero-sum and has length at most $2n-1$. The $e_1$ coordinate shows that $|U|$ is a positive multiple of $n$, so $|U|=n$.

For each $i\in\{2,3,4\}$, the $e_i$ coordinate sum is also $0$ modulo $n$ and lies between $0$ and $|U|=n$. Thus it is either $0$ or $n$. Therefore all selected vector types either all contain $i$ or all omit $i$, simultaneously for every $i=2,3,4$. All selected terms must have the same subset $A$, which would require selecting $n$ copies of one type. Only $n-1$ copies are available. This contradiction proves that $S_n$ has no zero-sum subsequence of length at most $2n-1$.

Consequently

$$
s_{\leq2n-1}(C_n^4)\geq8n-7.
$$

In Conjecture 6.2 put $D(G)-k=2n-1$, so $k=2n-2$. Since $2n-1=(D(G)+1)/2$, the upper branch predicts

$$
s_{\leq2n-1}(C_n^4)\leq D(G)+k=6n-5.
$$

But $8n-7>6n-5$ for every $n\geq2$, so Conjecture 6.2 is false for this infinite family.

## Conjecture 6.2: Finite Upper-Branch Witnesses

For $G=C_2^2\oplus C_4^2$, the Davenport constant is $D(G)=9$. The sequence recorded in the executable certificate has length 13 and has no zero-sum occurrence-subsequence of length at most 5. Thus

$$
s_{\leq5}(G)\geq14.
$$

The upper branch of Conjecture 6.2 at $D(G)-k=5$ has $k=4$ and predicts $s_{\leq5}(G)\leq13$. This is a counterexample.

For $G=C_2^{12}$, the extended Golay column certificate has length 24 and has no zero-sum subset of length at most 7. Since $D(G)=13$, the upper branch at $D(G)-k=7$ has $k=6$ and predicts $s_{\leq7}(G)\leq19$. The certificate gives $s_{\leq7}(G)\geq25$, so this is another counterexample.

## Conjecture 6.2: Lower-Branch Witness

For $G=C_2^7$, $D(G)=8$. The length-11 certificate in the executable checker has no zero-sum subset of length at most 4, so $s_{\leq4}(C_2^7)\geq12$.

It remains to know that the value is not larger. A length-12 subset of $F_2^7$ with no zero-sum subset of size at most 4 would give a binary linear $[12,5,\geq5]$ code by taking the parity-check kernel. Conversely, such a code would give such a length-12 subset. The appendix argument below proves that no such code exists. Therefore every length-12 sequence over $C_2^7$ has a zero-sum subsequence of length at most 4, and

$$
s_{\leq4}(C_2^7)=12.
$$

The lower branch of Conjecture 6.2 at $D(G)-k=4$ has $k=4$ and predicts $s_{\leq4}(G)>12$. Hence the lower branch is false.

## Conjecture 6.4: Lower-Branch Witness

For $G=C_2^7$, $D(G)=8$, so $2D(G)-1=15$. Since $4<(D(G)+1)/2$, Conjecture 6.4 predicts $s_4(C_2^7)>15$.

The length-14 certificate in the executable checker has no exact length-4 zero-sum subset, so $s_4(C_2^7)\geq15$. Sidorenko's exact-value theorem gives $s_4(C_2^7)=15$. Thus the strict lower-branch prediction is false.

## Conjecture 1.2: Supplemental Even-Rank Witness

For $G=C_2^8$, Zhao's Lemma 1.7(iii), originally due to Wang--Zhao in the cited source's attribution, gives $s_{\leq6}(C_2^8)=10$. The executable certificate records a length-18 sequence over $C_2^8$ with no exact length-6 zero-sum subset, so $s_6(C_2^8)\geq19$.

Conjecture 1.2 with $k=3$ predicts

$$
s_6(C_2^8)=s_{\leq6}(C_2^8)+6-1=15.
$$

This is false. The source paper already notes failures of Conjecture 1.2, so this is recorded only as a supplemental even-rank witness.

## Appendix: No Binary $[12,5,\geq5]$ Code

A length-12 sequence in $F_2^7$ with no nonempty zero-sum subset of size at most 4 has no zero column and no repeated column. Taking the columns as a $7\times12$ parity-check matrix $H$, the kernel

$$
C=\{x\in F_2^{12}:Hx=0\}
$$

has dimension at least 5 and minimum distance at least 5. If the dimension is larger, any 5-dimensional subcode still has minimum distance at least 5. Thus such a sequence implies a binary linear $[12,5,\geq5]$ code.

Conversely, a binary $[12,5,\geq5]$ code has a parity-check matrix with 7 rows whose columns give a length-12 sequence in $F_2^7$ with no zero-sum subsequence of size at most 4.

Assume such a binary $[12,5,\geq5]$ code exists and add the total parity bit. This gives an even $[13,5,\geq6]$ code $C'$. It has no zero coordinate; otherwise puncturing would give a $[12,5,\geq6]$ code, contradicting the Griesmer bound $6+3+2+1+1=13$. It has no two identical coordinates; otherwise deleting the two zero coordinates in a 4-dimensional kernel would give a $[11,4,\geq6]$ code, contradicting the Griesmer bound $6+3+2+1=12$.

There is no weight-10 word in $C'$. If there were, the kernel of projection to the other three coordinates would have dimension at least 2 and would contain another nonzero word supported inside those ten positions. Adding it to the weight-10 word would give a nonzero word of weight at most 5.

Thus the nonzero weights of $C'$ are only 6, 8, and 12. Let their counts be $A_6,A_8,A_{12}$. The zero-, first-, and second-moment identities are

$$
A_6+A_8+A_{12}=31,
$$

$$
6A_6+8A_8+12A_{12}=13\cdot2^4=208,
$$

and

$$
{6\choose2}A_6+{8\choose2}A_8+{12\choose2}A_{12}={13\choose2}2^3=624.
$$

The first two imply $A_8+3A_{12}=11$, while the first and third imply $13A_8+51A_{12}=159$. Eliminating $A_8$ gives $12A_{12}=16$, impossible. Therefore no binary $[12,5,\geq5]$ code exists.
