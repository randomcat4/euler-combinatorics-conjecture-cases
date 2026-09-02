# Minimal-Degree-Three Imprimitive Groups

*Antonio Montero and Primoz Potocnik · [DOI](https://doi.org/10.1016/j.jcta.2025.106065) · [arXiv](https://arxiv.org/abs/2405.10088v2)*

This case records a partial result for Problem 2 in Montero and Potocnik,
*Vertex-transitive graphs with small motion and transitive permutation groups
with small minimal degree*. The public scope is the full imprimitive family
displayed in the source as

\[
\operatorname{Alt}(m)^k \leq G \leq \operatorname{Sym}(m)\wr
\operatorname{Sym}(k),\qquad m\geq 3,\ k\geq 1.
\]

In the standard product action on \([m]\times[k]\), quotient by
\(\operatorname{Alt}(m)^k\). If

\[
Q=G/\operatorname{Alt}(m)^k\leq \mathbb{F}_2^k\rtimes\operatorname{Sym}(k),
\qquad H=\pi(Q),\qquad K=Q\cap\mathbb{F}_2^k,
\]

then \(G\) is transitive if and only if \(H\) is transitive on the block set.
Moreover \(G\) is transitive with minimal degree \(3\) if and only if \(H\) is
transitive and \(K\) contains no Hamming-weight-one vector.

The case also gives the exact labelled-block parameterization by a transitive
top group \(H\), an \(H\)-invariant binary code \(K\) of minimum Hamming weight
at least two unless \(K=0\), and a cocycle
\(c\in Z^1(H,\mathbb{F}_2^k/K)\). It does not claim the conjugacy quotient or
a classification of all transitive permutation groups of minimal degree three.

## Contents

- [Problem](problem.md): source locator, notation, and exact public scope.
- [Proof](proof.md): transitivity, support trichotomy, and cocycle
  parameterization.
- [Status](status.md): correctness, scope, and priority boundaries.
- [Verification](verification.md): independent mathematical review and finite
  quotient/support calibration.
- [Sources](sources.md): public source and prior-art boundary.
- [Checker](check_quotient_criterion.py): standard-library reproduction of
  the finite quotient/support calibration.
- [Certificate](quotient_certificate.json): expected finite calibration counts.

Public novelty or priority is **NOT_ESTABLISHED**. See [Status](status.md).
