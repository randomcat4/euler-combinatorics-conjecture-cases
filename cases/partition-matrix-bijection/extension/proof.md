# Proof guide

The full statements, constructions and proofs are in the [manuscript](../paper/extension.pdf). This file gives its dependency structure, not a substitute proof by numerical checking.

## Precise result

Both full classes with semi-weight/distinct-value count k and length n are in bijection with cyclically ordered set partitions of [k+1] into n-k+1 blocks. The original minus subclasses correspond precisely to a nonsingleton block containing the largest label. Restricting the same algorithms therefore solves the original question.

Circular descents recover matrix dimension, and the selected descent bits recover the complete ordered column-parity signature. For a fixed dimension D and specified signature, the number is the Eulerian number A(k,D-1); the corresponding size n is determined by the signature's number of one-bits.

## Argument

Collapse each prescribed pair in a matrix column, retaining whether that column was odd. An insertion permutation records the resulting matrix by its row anchors. Adding one largest sentinel and retaining precisely the selected decreasing adjacencies gives the cycle of blocks. First-smaller-to-the-right anchors reconstruct the matrix.

On the sequence side remove its entire last run. The rank of its unused value selects one existing block. A singleton run adds the largest label to that block; a double run inserts a new singleton block before it. The location of the largest label uniquely reverses each step. The two independently proved encodings share the same object, giving both compositions and all terminal boundary cases.

## Attribution

The manuscript identifies the source question, the earlier public result and its classical inputs. No public priority or novelty certification is claimed.
