# Original problem

**Chern--Fu, Question 5.7 in arXiv v2.** [Source paper](https://arxiv.org/abs/2508.21318v2).

Construct an explicit statistic-preserving bijection between improper partition matrices whose cell containing n has odd size and restricted inversion sequences whose final value occurs once. Preserve semi-weight v=sum over columns ceil(column size/2) and the number of distinct sequence values.

## Definitions and scope

A partition matrix is upper triangular, has no empty row or column, and has nondecreasing column indices along the ordered labels. Improperness means no proper ascent or descent: the disjoint first-second, third-fourth, ... pairs in each column must occupy a common cell. Restricted inversion sequences have 0<=e_i<i and no equal entries at positions separated by at least one other position.

## Answer and extension

Both full classes with semi-weight/distinct-value count k and length n are in bijection with cyclically ordered set partitions of [k+1] into n-k+1 blocks. The original minus subclasses correspond precisely to a nonsingleton block containing the largest label. Restricting the same algorithms therefore solves the original question.

Circular descents recover matrix dimension, and the selected descent bits recover the complete ordered column-parity signature. For a fixed dimension D and specified signature, the number is the Eulerian number A(k,D-1); the corresponding size n is determined by the signature's number of one-bits.
