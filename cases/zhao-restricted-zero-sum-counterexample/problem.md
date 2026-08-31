# Problem

Let $G$ be a finite abelian group. Write $D(G)$ for its Davenport constant, $D^*(G)$ for the standard lower bound, and $s_{\leq k}(G)$ for the least integer $l$ such that every sequence of length $l$ over $G$ has a nonempty zero-sum subsequence of length at most $k$.

The cited source also writes $s_q(G)$ for the least length forcing a zero-sum subsequence of exact length $q$.

This public package concerns only the following source statements.

## Conjecture 6.1

Conjecture 6.1 states that

$$
s_{\leq D(G)-2}(G)=D(G)+1
$$

whenever all of the following hold:

1. $r(G)\geq 2$;
2. $D(G)=D^*(G)$;
3. $G\not\cong C_2^4$;
4. $D(G)-2\geq \exp(G)$; and
5. $\exp(G)<(D(G)-1)/2$.

The counterexample group used here is

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

The group satisfies every stated hypothesis.

## Conjecture 6.2

Conjecture 6.2 assumes $r(G)\geq2$, $D(G)=D^*(G)$, and $D(G)-k\in[\exp(G),D(G)]$. It predicts:

- if $D(G)-k\geq (D(G)+1)/2$, then $s_{\leq D(G)-k}(G)\leq D(G)+k$;
- if $D(G)-k< (D(G)+1)/2$, then $s_{\leq D(G)-k}(G)>D(G)+k$.

This package records three upper-branch counterexamples and one lower-branch counterexample:

- the infinite family $G=C_n^4$ for every prime-power $n\geq2$;
- the finite group $C_2^2\oplus C_4^2$;
- the finite group $C_2^{12}$;
- the finite group $C_2^7$.

## Conjecture 6.4

Conjecture 6.4 is the exact-length analogue. For $q=k\exp(G)$, it predicts:

- if $q\in[(D(G)+1)/2,D(G)]$, then $s_q(G)\leq2D(G)-1$;
- if $q<(D(G)+1)/2$, then $s_q(G)>2D(G)-1$.

This package records only the lower-branch failure at $G=C_2^7$, where Sidorenko's exact value gives $s_4(C_2^7)=15$ while $2D(G)-1=15$.

## Conjecture 1.2

Conjecture 1.2 states

$$
s_{k\exp(G)}(G)=s_{\leq k\exp(G)}(G)+k\exp(G)-1.
$$

This package records a supplemental even-rank counterexample at $G=C_2^8$ and $k=3$. The source paper already notes that Conjecture 1.2 is not always true, so this item is not a priority claim.

## Non-claims

- The package does not assert that all conjectures in the cited paper are false.
- The package does not claim novelty or public priority.
- The package does not treat finite no-hit searches as evidence for any unbounded conjecture.
