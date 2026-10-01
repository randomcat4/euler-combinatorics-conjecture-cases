# Original problem

**Lin--Zhao, Conjecture 1.3.** [Source paper](https://arxiv.org/abs/2508.13466v1).

Among finite simple unweighted trees with b leaves and matching number br+2, prove that the extra-special tree uniquely maximizes the first positive Steklov eigenvalue. For b>=3 the proposed spider has arms 2r+2, 2r+1, and b-2 arms of length 2r.

## Definitions and scope

Assume integers b>=2 and r>=1; the source spider definition begins at b=3. At b=2 the stated endpoint is the path of 4r+3 edges. The boundary consists of the leaves with counting measure.

## Answer and extension

For every integer b>=2,r>=1 and tree with matching number at least br+2, sigma_2(T)<=1/(2r+c_b), where c_b=[3(b-1)+sqrt(b^2-2b+9)]/(2b). Equality is the extra-special spider (or the stated path for b=2).

For a central edge separating s and t leaves at diameter 4r+3, the sharp bound is 1/(2r+lambda(s,t)). Here lambda(s,t) is the largest eigenvalue of the explicit three-by-three Gram matrix in the manuscript. Every positive-integer split has its unique equality tree.
