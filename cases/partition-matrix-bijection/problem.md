# Problem

## Partition matrices

Write `[n] = {1,\ldots,n}`. A partition matrix on `[n]` is an upper-triangular square matrix whose entries are subsets of `[n]` and which satisfies:

1. every row and every column contains a nonempty cell;
2. the nonempty cells form a set partition of `[n]`; and
3. if `i < j`, then the column containing `i` is not to the right of the column containing `j`.

Its weight is the total number of elements in its nonempty cells. Let `PM_n` denote the partition matrices of weight `n`.

For an element `a`, write `row_Q(a)` and `col_Q(a)` for the row and column of its cell. Suppose `1 <= i < n` and `col_Q(i)=col_Q(i+1)`. The pair is an ascent when `row_Q(i)<row_Q(i+1)` and a descent when `row_Q(i)>row_Q(i+1)`. Let `j` be the smallest element in their common column. Such an ascent or descent is proper exactly when `i` and `j` have the same parity, and improper otherwise.

An improper partition matrix is one in which every ascent and descent is improper. Let `IPPM_n` be the improper partition matrices of weight `n`. The subclass `IPPM_n^-` consists of those matrices for which the cell containing the largest label `n` has odd cardinality.

If a matrix `Q` has dimension `D` and column sizes `N_1,\ldots,N_D`, define

\[
v(Q)=\sum_{c=1}^{D}\left\lceil\frac{N_c}{2}\right\rceil.
\]

## Restricted inversion sequences

An inversion sequence of length `n` is a sequence `e=(e_1,\ldots,e_n)` satisfying `0 <= e_i < i` for every `i`. Let `I_n(-,-,=)` be the class in which every value occurs at most twice and, when it occurs twice, the two occurrences are adjacent.

For `n >= 2`, let `I_n(-,-,=)^-` consist of the sequences with `e_{n-1} != e_n`. Equivalently, the last value occurs only once. To retain the all-order formulation at the endpoint, set

\[
I_1(-,-,=)^-=\{(0)\}.
\]

Let `dist(e)` be the number of distinct entries of `e`, including zero.

## The question

Construct, for every `n >= 1`, a direct and structural bijection

\[
\rho_n\colon\operatorname{IPPM}_n^-\longrightarrow I_n(-,-,=)^-
\]

such that `v(Q)=dist(\rho_n(Q))` for every source object.

A complete answer must provide a uniform all-order rule, prove that its image is exactly the target class, give an explicit inverse, prove both compositions are identities, preserve the statistics object by object, and cover `n=1`. Equality of generating functions, finite tables, or an arbitrary rank matching between equally large sets does not meet these requirements.
