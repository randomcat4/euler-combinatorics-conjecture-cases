# Product-activity cycle weights

For positive activities $x_1,\ldots,x_n$, assign every $k$-cycle supported
on $A$ the weight $\prod_{i\in A}x_i$. Two structured families have a strict
representation-level classification. Their complete derivations are in
[the supplementary proof](activityproof.md).

## One exceptional activity

Let $n\ge5$, $2\le k\le n-2$, $c>0$, $0<t<1$, and

\[
 x=(tc,c,\ldots,c).
\]

The largest nondegree eigenvalue occurs only in the standard representation
$(n-1,1)$ for even $k$, and exactly in the standard representation and its
sign twist $(2,1^{n-2})$ for odd $k$. The root is simple in each attaining
block. Its value is

\[
 c^k\left[(1-t)\binom{n-1}{k}(k-1)!
 +t\binom nk(k-1)!\frac{n-k-1}{n-1}\right].
\]

After removing $c^k$, the operator is
$tK_{n,k}+(1-t)K_{n-1,k}$. Multiplicity-free branching diagonalizes its
branches. The published non-strict normal-class bound controls the first
summand; equality with the degree of the second summand is possible only
for trivial or sign children, whose parents are degree or target blocks.
The coefficient $1-t>0$ makes every other block strict.
See [Section 2](activityproof.md#2-one-exceptional-activity).

## Three-cycles with two exceptional activities

Let $n\ge5$, $N=n-2$, and $a,b,c>0$ satisfy $a<\min(b,c)$. For

\[
 x=(a,b,c,\ldots,c),
\]

the largest nondegree eigenvalue occurs exactly in $(n-1,1)$ and its sign
twist, and is simple in both. Put

\[
 \begin{aligned}
 p&=abNc,&r&=ac[b+(N-1)c],&s&=bc[a+(N-1)c],\\
 \mathcal T&=2p+(N+1)(r+s),&
 \mathcal S&=(N+2)[p(r+s)+Nrs].
 \end{aligned}
\]

The target adjacency eigenvalue is $D-\gamma$, where

\[
 D=2\sum_{i<j<\ell}x_ix_jx_\ell,\qquad
 \gamma=\frac{\mathcal T-\sqrt{\mathcal T^2-4\mathcal S}}2.
\]

The cases $b<c$, $b=c$, and $b>c$ reduce respectively to a repeated larger
tail, the one-exceptional family, and the reflected family with one larger
exceptional point. The full proof gives the scalar and explicit two-by-two
multiplicity matrices, the scalar hierarchy, and every uniform comparison.
For the reflected family it also treats all ordered one-path domino branches,
including the parameter regime where the smaller root coefficient exceeds
one. See [Sections 3–6](activityproof.md#3-three-cycle-scalars-and-two-step-branching).

## Scope

The first family has a repeated tail of size $n-1$; the second has a repeated
tail of size $n-2$ and a unique minimum among the two exceptional points and
the tail. Neither theorem resolves arbitrary positive activities. The $k=2$
slice of the first theorem lies within the more general published weighted
transposition theorem. Public novelty and priority are not established here.
