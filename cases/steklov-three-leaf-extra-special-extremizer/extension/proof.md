# Proof guide

The full statements, constructions and proofs are in the [manuscript](../paper/extension.pdf). This file gives its dependency structure, not a substitute proof by numerical checking.

## Precise result

For every integer b>=2,r>=1 and tree with matching number at least br+2, sigma_2(T)<=1/(2r+c_b), where c_b=[3(b-1)+sqrt(b^2-2b+9)]/(2b). Equality is the extra-special spider (or the stated path for b=2).

For a central edge separating s and t leaves at diameter 4r+3, the sharp bound is 1/(2r+lambda(s,t)). Here lambda(s,t) is the largest eigenvalue of the explicit three-by-three Gram matrix in the manuscript. Every positive-integer split has its unique equality tree.

## Argument

Use zero-sum leaf currents: the inverse Steklov form is the sum of squared currents across edges, and two opposite leaf injections bound it below by half the diameter. The matching threshold forces diameter at least 4r+3; larger diameter already gives strict inequality.

At the smallest diameter, a saturated alternating-depth vertex cover forces every branch into groups of long and short arms. Choose a long leaf on each side. A rank-three comparison form has a top eigenvector with one strict sign on each half, so all omitted group cross terms are nonnegative. Its Gram matrix gives the sharp root and singles out the winning singleton split. Equality forces singleton groups with precisely one long arm per side, giving the stated unique trees.

## Attribution

The manuscript identifies the source question, the earlier public result and its classical inputs. No public priority or novelty certification is claimed.
