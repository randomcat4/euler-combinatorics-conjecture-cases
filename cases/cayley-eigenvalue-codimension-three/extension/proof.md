# Proof guide

The full statements, constructions and proofs are in the [manuscript](../paper/full_conjecture.pdf). This file gives its dependency structure, not a substitute proof by numerical checking.

## Precise result

The manuscript gives the full-range uniqueness argument for n>=5 and 1<=r<k<=n-2. This is a readable exposition of the theorem already claimed in public PR17, not a new extension theorem.

The proof uses finite representation-block inputs at (n,k,r)=(6,4,1),(6,4,2),(7,5,1). The companion checker now supplies exact rational characteristic polynomials, threshold multiplicities and Sturm counts. Its numerical orthogonal-model spectra are only supplementary cross-checks.

## Argument

Make the endpoint r=k-1 strict by characterizing equality in the eigenvalue inequalities. Two-subset and exterior-square models exclude the unwanted equality spaces. Strictness then propagates backwards through the published recurrence.

Small cycle lengths k=2,3 use Jucys--Murphy arguments. The n-k=2 boundary combines the cited boundary results with the three finite inputs. The codimension-four case follows by direct specialization. The argument does not address k=n-1.

## Attribution

The manuscript identifies the source question, the earlier public result and its classical inputs. No public priority or novelty certification is claimed.
