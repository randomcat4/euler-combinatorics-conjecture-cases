# Problem

The source is Antonio Montero and Primoz Potocnik, "Vertex-transitive graphs
with small motion and transitive permutation groups with small minimal degree",
arXiv:2405.10088v2 and *Journal of Combinatorial Theory, Series A* 216
(2025), article 106065.

Problem 2, in the Introduction on physical arXiv v2 PDF page 6, asks for a
detailed description of transitive permutation groups of minimal degree three.
It specifically points to the family in display (1.2), on physical PDF page 5:

\[
\operatorname{Alt}(m)^k\leq G\leq
\operatorname{Sym}(m)\wr \operatorname{Sym}(k).
\]

This public case addresses exactly that displayed family in its standard
imprimitive action on

\[
\Omega=[m]\times[k],
\]

for every \(m\geq3\) and \(k\geq1\). Put \(A=\operatorname{Alt}(m)^k\) and
write

\[
Q=G/A\leq \mathbb{F}_2^k\rtimes \operatorname{Sym}(k),\qquad
H=\pi(Q),\qquad K=Q\cap \mathbb{F}_2^k,
\]

where the quotient map is induced by the coordinatewise sign map from the base
group \(\operatorname{Sym}(m)^k\) to \(\mathbb{F}_2^k\), and \(\pi\) is the
top projection.

The result proves:

1. \(G\) is transitive on \(\Omega\) if and only if \(H\) is transitive on
   \([k]\).
2. \(G\) is transitive and has minimal degree \(3\) if and only if \(H\) is
   transitive and \(K\) contains no Hamming-weight-one vector.
3. In the labelled block system, the subgroups are parameterized by a
   transitive \(H\leq \operatorname{Sym}(k)\), an \(H\)-invariant binary code
   \(K\leq\mathbb{F}_2^k\), and a cocycle
   \(c:H\to \mathbb{F}_2^k/K\).

## Non-Claims

This is a `PARTIAL_RESULT`. It does not solve Problem 2 outside the displayed
imprimitive family, does not classify permutation-isomorphism classes up to the
normalizer action, and does not claim public priority.
