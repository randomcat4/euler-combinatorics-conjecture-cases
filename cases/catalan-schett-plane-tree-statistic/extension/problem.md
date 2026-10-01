# Original problem

**Lin--Liu--Yan, Problem 2.18.** [Source paper](https://arxiv.org/abs/2409.01558v1).

Find an intrinsic statistic st on rooted plane trees such that the joint distribution of (mark,st) on trees with n edges equals (mnd(pi),mna(pi inverse)) on 231-avoiding permutations. Here mark counts non-root vertices with a leaf child, and mnd/mna sum floor(run length/2) over descending/ascending runs.

## Definitions and scope

The inverse permutation is essential. The empty tree is included as the generating-function base; the source question concerns n>=1.

## Answer and extension

A reversible two-case cut of a plane tree yields an explicit bijection with 231-avoiding permutations. It preserves mark=mnd and identifies an intrinsic ordered list of positive integers with the entire ascending-run composition of the inverse permutation. Summing floor(r/2) over this list solves the original problem.

Let W(s)=1+sum_(r>=1) w_r s^r and W_+(s)=sum_(r>=0) w_(r+1)s^r. There is a unique zero-constant series a satisfying a=z+x*z^2*W(a)*W_+(a), and the generating series with first-run length marked by u is W(a*u). This allows arbitrary multiplicative run weights, including zero weights. The d-packet specialization w_r=y^floor(r/d) holds for every d>=2.
