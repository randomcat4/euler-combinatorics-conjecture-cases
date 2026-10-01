# Proof guide

The full statements, constructions and proofs are in the [manuscript](../paper/extension.pdf). This file gives its dependency structure, not a substitute proof by numerical checking.

## Precise result

A reversible two-case cut of a plane tree yields an explicit bijection with 231-avoiding permutations. It preserves mark=mnd and identifies an intrinsic ordered list of positive integers with the entire ascending-run composition of the inverse permutation. Summing floor(r/2) over this list solves the original problem.

Let W(s)=1+sum_(r>=1) w_r s^r and W_+(s)=sum_(r>=0) w_(r+1)s^r. There is a unique zero-constant series a satisfying a=z+x*z^2*W(a)*W_+(a), and the generating series with first-run length marked by u is W(a*u). This allows arbitrary multiplicative run weights, including zero weights. The d-packet specialization w_r=y^floor(r/d) holds for every d>=2.

## Argument

The tree cut separates the cases according to whether the root has a leaf child and has an explicit inverse in both cases. The corresponding permutation decomposition places its first value between a lower and a higher block. Its inverse concatenation extends only the first ascending run on the right.

For weighted enumeration, temporarily omit the first run's weight instead of dividing by that weight. The two root-state equations then give a geometric first-run series 1/(1-a*u). Restoring the omitted weights gives W(a*u); eliminating the state variable gives the displayed equation for a. All inverses have constant coefficient one, so zero weight specializations are legitimate.

## Attribution

The manuscript identifies the source question, the earlier public result and its classical inputs. No public priority or novelty certification is claimed.
