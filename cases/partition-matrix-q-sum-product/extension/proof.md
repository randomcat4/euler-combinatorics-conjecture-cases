# Proof guide

The full statements, constructions and proofs are in the [manuscript](../paper/extension.pdf). This file gives its dependency structure, not a substitute proof by numerical checking.

## Precise result

Let R_k(q,t) enumerate words on k ordered letters by length and inversions, including the empty word. The partition-matrix series is sum_(d>=1) product_(k=1)^d (1-R_k(q,t)^(-1)). Every fixed R_k has the standard basic-hypergeometric expression displayed in the manuscript.

Give a cell of size a arbitrary weight u_a, with u_0=1. Replace R_k by its q-multinomial content sum with weight product_i u_(a_i). The same sum-product holds, and the normalized q-Borel transform of this weighted R_k is the kth power of sum_(a>=0) u_a*z^a/(q;q)_a.

## Argument

Read each matrix column as a nonempty row word. Inclusion-exclusion over missing rows gives rise/stay paths whose contribution at each attained level is (R_k-1)/R_k. Positive length order makes their regrouping legitimate as a formal series.

Divide the word coefficient of degree m by (q;q)_m: the q-multinomial content sum factorizes. Euler's q-binomial identity supplies an inverse kernel whose degree-m multiplier is (q;q)_m. Applying it gives the standard hypergeometric form. Arbitrary cell sizes work because forbidding a row only removes a letter; it does not alter any remaining content weight.

## Attribution

The manuscript identifies the source question, the earlier public result and its classical inputs. No public priority or novelty certification is claimed.
