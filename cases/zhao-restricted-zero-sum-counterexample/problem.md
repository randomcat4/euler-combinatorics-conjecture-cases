# Problem

Let $G$ be a finite abelian group. Write $D(G)$ for its Davenport constant, $D^*(G)$ for the standard lower bound, and $s_{\leq k}(G)$ for the least integer $l$ such that every sequence of length $l$ over $G$ has a nonempty zero-sum subsequence of length at most $k$.

Conjecture 6.1 of the cited source states that

$$
s_{\leq D(G)-2}(G)=D(G)+1
$$

whenever all of the following hold:

1. $r(G)\geq 2$;
2. $D(G)=D^*(G)$;
3. $G\not\cong C_2^4$;
4. $D(G)-2\geq \exp(G)$; and
5. $\exp(G)<(D(G)-1)/2$.

## Counterexample group

Take

$$
G=C_2\oplus C_4^3.
$$

The standard formula for finite abelian $p$-groups gives

$$
D(G)=D^*(G)=1+(2-1)+3(4-1)=11.
$$

Thus $r(G)=4$, $G\not\cong C_2^4$, $D(G)-2=9\geq 4=\exp(G)$, and

$$
4<\frac{11-1}{2}=5.
$$

The group satisfies every stated hypothesis. A counterexample therefore consists of a length-12 sequence with no nonempty zero-sum occurrence-subsequence of length at most 9.
