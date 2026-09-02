# Quotient Criterion Proof

Let \(m\geq3\), \(k\geq1\), and

\[
W=\operatorname{Sym}(m)\wr\operatorname{Sym}(k)
\]

act on \(\Omega=[m]\times[k]\) in the standard imprimitive action. Let
\(A=\operatorname{Alt}(m)^k\), and let

\[
Q=G/A\leq\mathbb{F}_2^k\rtimes\operatorname{Sym}(k),\qquad
H=\pi(Q),\qquad K=Q\cap\mathbb{F}_2^k
\]

for an intermediate subgroup \(A\leq G\leq W\).

## 1. The Quotient

The base group of \(W\) is \(B=\operatorname{Sym}(m)^k\). Since
\(\operatorname{Alt}(m)\triangleleft \operatorname{Sym}(m)\) for \(m\geq3\),
and since the top group permutes the factors, \(A\) is normal in \(W\). The
coordinatewise sign map identifies

\[
W/A \simeq \mathbb{F}_2^k\rtimes\operatorname{Sym}(k).
\]

Every intermediate subgroup \(G\) is the full preimage of \(Q=G/A\). Also
\(G\cap B\) maps onto \(K=Q\cap\mathbb{F}_2^k\), and for every \(v\in K\), the
whole base parity coset above \(v\) lies in \(G\cap B\) after multiplying by
elements of \(A\).

## 2. Transitivity

The orbits of \(A\) on \(\Omega\) are exactly the blocks

\[
\Delta_i=[m]\times\{i\},
\]

because \(\operatorname{Alt}(m)\) is transitive on \([m]\) for every
\(m\geq3\). Therefore the \(G\)-orbits on \(\Omega\) are unions of blocks, and
the induced action on the block set is exactly \(H\).

Thus \(G\) is transitive on \(\Omega\) if and only if \(H\) is transitive on
\([k]\). For \(k=1\), the trivial top group is transitive on the one-point
block set, so the statement includes that endpoint.

## 3. Support Analysis

The group \(A\) contains a single-block 3-cycle for every \(m\geq3\). Hence
every intermediate \(G\) contains a nonidentity element moving exactly three
points, so \(\mu(G)\leq3\).

Let \(g\in G\) be nonidentity.

If the top projection of \(g\) is nontrivial, then at least two blocks are
moved. Every point in each moved block changes its block coordinate, so \(g\)
moves at least \(2m\geq6\) points. Such an element cannot have support one or
two.

It remains to consider \(g\in G\cap B\). Let

\[
v=\epsilon(g)\in K
\]

be the coordinatewise parity vector.

If \(v=0\), then \(g\in A\). A nonidentity even permutation of
\(\operatorname{Sym}(m)\) moves at least three points, with equality realized
by a 3-cycle. Hence nonidentity elements of \(A\) have support at least three.

If \(v\) has Hamming weight at least two, then \(g\) has odd coordinates in at
least two blocks. An odd permutation of \(\operatorname{Sym}(m)\) moves at
least two points, so \(g\) moves at least four points in total.

If \(v\) has Hamming weight one, say \(v=e_i\), then \(G\) contains a
single-block transposition. Choose any
\[
g=(\sigma_1,\ldots,\sigma_k)\in G\cap B
\]
with parity vector \(e_i\), and choose a transposition
\(\tau\in\operatorname{Sym}(m)\). For \(j\neq i\), set
\(a_j=\sigma_j^{-1}\in\operatorname{Alt}(m)\). In coordinate \(i\), the
permutations \(\tau\) and \(\sigma_i\) are both odd, so
\[
a_i=\tau\sigma_i^{-1}\in\operatorname{Alt}(m).
\]
Then \(a=(a_1,\ldots,a_k)\in A\) and
\[
ag=(1,\ldots,1,\tau,1,\ldots,1),
\]
which moves exactly two points.

Therefore \(G\) has a support-two element if and only if \(K\) contains a
Hamming-weight-one vector. Since support one is impossible for a permutation,
and since \(A\) supplies support three, we have

\[
\mu(G)=3
\quad\Longleftrightarrow\quad
K\text{ contains no Hamming-weight-one vector}.
\]

Combined with the transitivity criterion, this proves the announced
minimal-degree-three criterion.

## 4. Labelled Quotient Parameterization

Let \(V=\mathbb{F}_2^k\). For every subgroup
\(Q\leq V\rtimes\operatorname{Sym}(k)\), the pair
\[
H=\pi(Q),\qquad K=Q\cap V
\]
satisfies that \(K\) is \(H\)-invariant, because conjugating an element of
\(K\) by an element above \(h\in H\) applies \(h\) to the vector.

Conversely, choose \(H\leq\operatorname{Sym}(k)\), an \(H\)-invariant subspace
\(K\leq V\), and a 1-cocycle
\[
c:H\to V/K,\qquad c(h\ell)=c(h)+h.c(\ell).
\]
Then
\[
Q_c=\{(v,h)\in V\rtimes H: v+K=c(h)\}
\]
is a subgroup with top projection \(H\) and base kernel \(K\).

Every subgroup \(Q\) arises in this way by defining \(c(h)=v+K\) for any
\((v,h)\in Q\). This is well-defined because two choices of \(v\) differ by an
element of \(K\), and the subgroup law gives the cocycle identity. Pulling
\(Q_c\) back under \(W\to W/A\) gives the corresponding intermediate subgroup
\(G\).

Thus, in the fixed labelled block system, the transitive minimal-degree-three
groups in the displayed family are exactly those determined by:

- a transitive \(H\leq\operatorname{Sym}(k)\);
- an \(H\)-invariant binary code \(K\leq\mathbb{F}_2^k\) with no
  Hamming-weight-one vector;
- a cocycle \(c\in Z^1(H,\mathbb{F}_2^k/K)\).

Passing from this labelled-block parameterization to permutation-isomorphism
classes would require quotienting the data by the normalizer action. That
extra conjugacy quotient is not claimed here.
