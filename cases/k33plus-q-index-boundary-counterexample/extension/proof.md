# Proof guide

The full statements, constructions and proofs are in the [manuscript](../paper/extension.pdf). This file gives its dependency structure, not a substitute proof by numerical checking.

## Precise result

At s=t=3,n=6 the unique feasible Q-index maximizer is K2 join (K3 disjoint union K1), with Q-index 5+sqrt(13). This lies outside both printed families.

K2 join R is K_(3,3)^+-free exactly when R has maximum degree at most two and no four-cycle component. For n>=7 the sharp maximum in this entire class is (n+6+sqrt(n^2-4n+20))/2, attained exactly by joins with unions of cycles having no four-cycle. The source classification fails at n=8 and every n>=10, without needing an unrestricted extremal classification.

## Argument

For six vertices, a vertex of degree at most two embeds the graph in the displayed maximizer. Otherwise the complement has maximum degree two. A component of order at least four yields a fixed path-complement upper bound; the remaining component partitions give only two inferior possibilities.

The forbidden graph is detected by a triple containing an edge with three common neighbors. This gives the exact two-universal-vertex criterion. A positive vector constant on the two vertex types proves the sharp spectral bound and its equality condition. Finally, triangle-containing cycle unions match every clique-pair source candidate; either they are outside maximizers or the unrestricted maximum is still larger and all source candidates lose.

## Attribution

The manuscript identifies the source question, the earlier public result and its classical inputs. No public priority or novelty certification is claimed.
