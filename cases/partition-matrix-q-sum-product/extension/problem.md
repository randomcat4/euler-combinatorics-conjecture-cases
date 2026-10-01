# Original problem

**Chern--Fu, Question 5.1 in arXiv v2.** [Source paper](https://arxiv.org/abs/2508.21318v2).

Find a closed expression for the ordinary generating series of inversion-weighted partition matrices. A matrix inversion is a pair i>j in one column with row(i)<row(j).

## Definitions and scope

Rows and columns are nonempty. The answer is an all-order formal sum-product with explicit column factors. Analytic convergence of each fixed column series is distinct from convergence of the outer ordinary series.

## Answer and extension

Let R_k(q,t) enumerate words on k ordered letters by length and inversions, including the empty word. The partition-matrix series is sum_(d>=1) product_(k=1)^d (1-R_k(q,t)^(-1)). Every fixed R_k has the standard basic-hypergeometric expression displayed in the manuscript.

Give a cell of size a arbitrary weight u_a, with u_0=1. Replace R_k by its q-multinomial content sum with weight product_i u_(a_i). The same sum-product holds, and the normalized q-Borel transform of this weighted R_k is the kth power of sum_(a>=0) u_a*z^a/(q;q)_a.
