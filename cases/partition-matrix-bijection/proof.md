# An explicit statistic-preserving bijection

## 1. Overview

For integers `k,q >= 1`, let `Ord(k,q)` be the set of linearly ordered set partitions of `[k]` into `q` nonempty blocks, and let `Cyc(k,q)` be the corresponding cyclically ordered set partitions, where a simultaneous cyclic rotation of all blocks changes nothing.

We construct two explicit bijections:

\[
\Gamma_n\colon\{Q\in\operatorname{IPPM}_n^-:v(Q)=k\}
\longrightarrow \operatorname{Ord}(k,n-k+1)
\]

and

\[
\Mu_n\colon\{e\in I_n(-,-,=)^-:\operatorname{dist}(e)=k\}
\longrightarrow \operatorname{Ord}(k,n-k+1).
\]

The required map and its inverse are

\[
\rho_n=\Mu_n^{-1}\circ\Gamma_n,
\qquad
\rho_n^{-1}=\Gamma_n^{-1}\circ\Mu_n.
\]

No global ordering or matching of the two object sets is used.

## 2. Collapsing parity pairs in improper columns

Consider column `c` of a partition matrix `Q`. Its labels form a consecutive interval

\[
\{b_c+1,\ldots,b_c+N_c\}.
\]

Subtracting `b_c` gives local labels `[N_c]`.

### Lemma 1: column-pair characterization

The matrix `Q` is improper if and only if, in every column and for every `2r <= N_c`, the local labels `2r-1` and `2r` lie in the same row, hence in the same cell.

### Proof

If consecutive local labels `t,t+1` occupy different rows, they form an ascent or descent. The least global label in the column is `j=b_c+1`, while the boundary label is `i=b_c+t`. If `t=2r-1`, then

\[
i-j=t-1=2r-2
\]

is even, so this ascent or descent is proper. It cannot occur in an improper matrix. Thus every local pair `2r-1,2r` must share a row.

Conversely, if all those pairs share a row, the row can change only after an even local label `t=2r`. Then `i-j=t-1` is odd, so every ascent or descent that occurs is improper. ∎

### Lemma 2: pair collapse

In column `c`, collapse each same-cell pair

\[
\{1,2\}\mapsto\{1\},\quad
\{3,4\}\mapsto\{2\},\quad\ldots
\]

and, when `N_c` is odd, collapse the final singleton `N_c` to `ceil(N_c/2)`. Keep every cell position fixed and relabel cumulatively by columns. Let the resulting partition matrix be `P`, and set

\[
S=\{c:N_c\text{ is odd}\}.
\]

This gives an explicit bijection

\[
\operatorname{IPPM}\longleftrightarrow
\{(P,S):P\in\operatorname{PM},\ S\subseteq[\dim P]\}.
\]

Its inverse expands each local label `r` of column `c` into the same-cell pair `2r-1,2r`; if `c in S`, it deletes the last label `2m_c`, where `m_c` is the size of column `c` in `P`. It then restores cumulative global labels by columns.

Moreover,

\[
w(Q)=2w(P)-|S|,
\qquad
v(Q)=w(P).
\]

### Proof

Lemma 1 makes the collapse well-defined. Every formerly nonempty cell retains a label, so no row or column becomes empty. Cell positions are unchanged, hence upper triangularity is preserved. Each column remains a consecutive label interval, so cumulative relabeling produces a partition matrix.

In the reverse direction, every expanded parity pair occupies one cell, so Lemma 1 gives an improper matrix. Collapse and expansion are visibly inverse column by column. If column `c` of `P` has size `m_c`, its expanded size is `2m_c-1` when `c in S` and `2m_c` otherwise. Summing these identities gives both formulas. ∎

### Corollary 3: the minus condition

If `D=dim(P)=dim(Q)`, then

\[
Q\in\operatorname{IPPM}_n^- \quad\Longleftrightarrow\quad D\in S.
\]

### Proof

The largest label lies in the last column. Before collapse, each cell is a union of complete even pairs, except that the cell containing the last label has one additional unpaired label exactly when the column size is odd. Thus the cell containing `n` is odd precisely when the last column belongs to `S`. ∎

Consequently, fixing `n` and `k=v(Q)`, source objects are equivalent to pairs

\[
P\in\operatorname{PM}_k,\qquad
S\subseteq[D],\qquad
D\in S,\qquad
|S|=2k-n. \tag{1}
\]

## 3. From a collapsed matrix to an ordered set partition

### 3.1 Partition matrices and inversion tables

For `P in PM_k`, let `c_i` be the smallest label in column `i`. If label `ell` lies in row `i`, define

\[
f_\ell=c_i-1.
\]

Then `f=(f_1,\ldots,f_k)` is an inversion table: `0 <= f_ell < ell`.

The inverse is explicit. Write

\[
\operatorname{Alph}(f)=\{y_1=0<y_2<\cdots<y_D\},
\qquad y_{D+1}=k.
\]

Set

\[
P_{ij}=\{\ell:f_\ell=y_i\text{ and }y_j<\ell\le y_{j+1}\}. \tag{2}
\]

Every alphabet value occurs, so every row is nonempty. Every interval `(y_j,y_{j+1}]` is nonempty, so every column is nonempty. If `f_ell=y_i` and `ell <= y_{j+1}`, then `i <= j`, which gives upper triangularity. The column intervals and row values recover `f`, while the column-order condition recovers the original cells of `P`. Thus the formulas are mutually inverse.

The maximum label in column `j` is

\[
M_j=y_{j+1}\quad(j<D),
\qquad M_D=k. \tag{3}
\]

Therefore `S` is equivalent to a marked set

\[
B=\{M_j:j\in S\},
\qquad
k\in B,
\qquad
B\setminus\{k\}\subseteq\operatorname{Alph}(f)\setminus\{0\}. \tag{4}
\]

### 3.2 Inversion tables and permutations

Define `T(f)=sigma` by starting with the empty word and processing `i=1,\ldots,k`. If `f_i=0`, append `i`; if `f_i>0`, insert `i` immediately before the already present letter `f_i`.

The inverse sends a permutation `sigma` to the table in which `f_i` is the first letter smaller than `i` to the right of `i`, or zero if none exists.

### Lemma 4

The map `T` is a bijection, and `Alph(f)` with zero removed is exactly the set of descent-bottom values of `sigma`, meaning the right-hand values `b` in adjacent descents `a>b`.

### Proof

When `i` is inserted, all existing letters are smaller. If `f_i=b>0`, then `b` is immediately to the right of `i`; later insertions are larger than `i`, so `b` remains the first smaller letter to its right. If `f_i=0`, the letter `i` is appended, and no later, larger insertion can put a smaller letter to its right. This proves the inverse formula.

If `b>0` occurs in `f`, choose the largest `i` with `f_i=b`. In the final word, `i` is immediately before `b`, so `b` is a descent bottom. Conversely, an adjacent descent `a>b` can only be created by inserting some letter immediately before `b`; hence `b` occurs as a table entry. ∎

### 3.3 Cutting the permutation

By (4) and Lemma 4, `B\setminus{ k }` selects a set of descents of `sigma`. Retain precisely those selected descent adjacencies and cut at every other adjacent position. Every resulting word is strictly decreasing. Forget the within-block writing order but retain block order. This produces

\[
\Gamma_n(Q)=L\in\operatorname{Ord}(k,q).
\]

There are `|S|-1` retained adjacencies, so

\[
q=k-(|S|-1)=k-|S|+1=n-k+1. \tag{5}
\]

### Lemma 5

The map `Gamma_n` is a bijection

\[
\{Q\in\operatorname{IPPM}_n^-:v(Q)=k\}
\longrightarrow \operatorname{Ord}(k,n-k+1).
\]

### Explicit inverse

Given `L=(L_1,\ldots,L_q)` in `Ord(k,q)`:

1. write each block in decreasing order and concatenate the blocks to form `sigma`;
2. mark all descents internal to blocks and record their bottom values in `B_0`;
3. recover `f` with the inverse in Lemma 4;
4. recover `P` from (2); if `Alph(f)={y_1<...<y_D}`, set
   \[
   S=\{r-1:y_r\in B_0\}\cup\{D\};
   \]
5. expand `(P,S)` by Lemma 2 to recover `Q`.

Internal block adjacencies are exactly the marked descents, so cutting and concatenation are inverse. Also

\[
|S|=|B_0|+1=(k-q)+1,
\]

and hence the expansion has weight `2k-|S|=k+q-1=n`. Since `D in S`, it lies in the source minus class. Every remaining step already has an explicit inverse, proving the lemma. ∎

## 4. Restricted inversion sequences and ordered set partitions

Every `e in I_N(-,-,=)` has a unique block factorization

\[
e=a_1^{\varepsilon_1}a_2^{\varepsilon_2}\cdots a_d^{\varepsilon_d}, \tag{6}
\]

where the `a_i` are distinct, each `epsilon_i` is `1` or `2`, and `d=dist(e)`. If block `i` begins at

\[
p_i=1+\sum_{j<i}\varepsilon_j,
\]

the inversion-sequence condition is exactly `0 <= a_i < p_i`. The minus condition is `epsilon_d=1`, including the endpoint `(0)`.

Let `E(N,d)` be the full restricted class of length `N` with `d` distinct values, and let `E^-(N,d)` be its minus subclass. Put `q=N-d+1`. For a cyclic partition `C`, let `can(C)` be its unique linear representative beginning with the block that contains `1`.

We now define two mutually recursive maps.

### 4.1 The full encoder `Phi`

Define

\[
\Phi:E(N,d)\longrightarrow\operatorname{Cyc}(d+1,q).
\]

The empty sequence maps to the one-block cyclic partition `({1})`.

For nonempty `e`, use factorization (6).

If `epsilon_d=2`, delete the final duplicate to obtain `h in E^-(N-1,d)`. If

\[
\Mu(h)=(L_1,\ldots,L_{q-1}),
\]

set

\[
\Phi(e)=({d+1},L_1,\ldots,L_{q-1}) \tag{7}
\]

as a cyclic partition.

If `epsilon_d=1`, delete the unique final entry and call the result `e' in E(N-1,d-1)`. Write

\[
\operatorname{can}(\Phi(e'))=(C_1,\ldots,C_q).
\]

The values allowed as a new final entry but unused by `e'` are

\[
U=[0,N-1]\setminus\operatorname{Val}(e')
=\{u_1<\cdots<u_q\}. \tag{8}
\]

Since the deleted final value is unique, it equals one `u_j`. Add the new element `d+1` to block `C_j`, preserving cyclic order. This is `Phi(e)`.

### 4.2 The minus encoder `Mu`

For `e in E^-(N,d)`, use the same `e'`, canonical blocks, unused values, and index `j` from the singleton case above, and define

\[
\Mu(e)=(C_j,C_{j+1},\ldots,C_q,C_1,\ldots,C_{j-1})
\in\operatorname{Ord}(d,q). \tag{9}
\]

The only ordering in (8) is the natural order on value labels inside one object; the cyclic starting point is fixed intrinsically by the block containing `1`. This is not a ranking of objects.

### 4.3 Explicit inverse recursion

First define `Mu^{-1}`. Given `L=(L_1,\ldots,L_q)` in `Ord(d,q)`:

1. forget the starting point to obtain a cyclic partition `C`, and write `can(C)=(C_1,\ldots,C_q)`;
2. let `j` be the unique index with `L_1=C_j`;
3. recursively compute `e'=Phi^{-1}(C)`; since `C` partitions `[d]`, the recovered sequence has `dist=d-1` and length `N-1=d+q-2`;
4. form the ordered unused-value list (8), and output
   \[
   e'u_j. \tag{10}
   \]

Next define `Phi^{-1}`. Given `C in Cyc(d+1,q)`, let `H` be the block containing the largest element `d+1`.

- If `C=({1})`, return the empty sequence.
- If `H={d+1}`, delete `H`. Except for the already handled base case, at least one block remains. Starting with the block that followed `H`, read the remaining cycle as `L in Ord(d,q-1)`. Compute `h=Mu^{-1}(L)` and duplicate the final entry of `h`.
- If `|H|>1`, remove `d+1` from `H` to obtain `C' in Cyc(d,q)`. Compute `e'=Phi^{-1}(C')`. In `can(C')`, let the reduced block `H\setminus{d+1}` have index `j`; form (8) and output `e'u_j`.

Every recursive call lowers the represented sequence length by one, so the mutual recursion terminates.

### Lemma 6

For all legal parameters, `Phi` and `Phi^{-1}` are mutually inverse, and `Mu` and `Mu^{-1}` are mutually inverse. In particular,

\[
\Mu:E^-(N,d)\longrightarrow\operatorname{Ord}(d,N-d+1)
\]

is an explicit bijection.

### Proof

Proceed by induction on `N`. The empty base for `Phi` is immediate. For `N=1`, equation (9) sends `(0)` to `({1})`, while (10) restores the unique unused value `0`.

For `Phi`, an image from the doubled-final-entry branch has the largest element `d+1` as a singleton block. The inverse recognizes this, deletes that block, recovers `h` by induction, and duplicates its last value. An image from the singleton-final-entry branch has `d+1` in a nonsingleton block. The inverse removes `d+1`, recovers `e'` by induction, locates the same canonical block index `j`, and restores the same unused value `u_j`. The two images are disjoint and exhaust the inverse branches.

For `Mu`, forgetting the starting point in (9) recovers `Phi(e')`; the position of `L_1` in the canonical cycle is exactly `j`. Induction recovers `e'`, and (10) restores `u_j=a_d`. Starting from `L` reverses the same cycle, starting block, and index.

It remains to check legality. In `Mu^{-1}` and in the nonsingleton branch of `Phi^{-1}`, the appended value `u_j` did not occur in `e'` and satisfies `0 <= u_j < N`. Thus it obeys the inversion bound and creates one new singleton value-block. In the singleton-block branch of `Phi^{-1}`, the final entry of `h` occurs only once because `h` is minus; duplication creates exactly one adjacent double block and preserves the inversion bound. All recursive outputs therefore remain in the restricted class. ∎

## 5. The final bijection

### Theorem

For every `n >= 1`, define

\[
\rho_n(Q)=\Mu_n^{-1}(\Gamma_n(Q)). \tag{11}
\]

Then

\[
\rho_n\colon\operatorname{IPPM}_n^-\longrightarrow I_n(-,-,=)^-
\]

is a bijection, its image is exactly the displayed target class, and

\[
v(Q)=\operatorname{dist}(\rho_n(Q))
\]

for every source object.

### Proof

Let `k=v(Q)`. Lemma 5 sends `Q` to `Ord(k,n-k+1)`. Lemma 6 sends that ordered partition to a minus restricted inversion sequence of length

\[
k+(n-k+1)-1=n
\]

and with exactly `k` distinct values. Thus (11) is defined everywhere in the source, lands in the claimed target, and preserves `v=dist` object by object.

The explicit inverse is

\[
\rho_n^{-1}(e)=\Gamma_n^{-1}(\Mu_n(e)). \tag{12}
\]

Using the two inverse pairs proved in Lemmas 5 and 6 gives both compositions:

\[
\rho_n^{-1}(\rho_n(Q))
=\Gamma_n^{-1}(\Mu_n(\Mu_n^{-1}(\Gamma_n(Q))))
=Q,
\]

and

\[
\rho_n(\rho_n^{-1}(e))
=\Mu_n^{-1}(\Gamma_n(\Gamma_n^{-1}(\Mu_n(e))))
=e.
\]

Hence the image is not merely contained in but is exactly `I_n(-,-,=)^-`. At `n=1`, the layers give

\[
[\{1\}]\longmapsto({1})\longmapsto(0),
\]

and both statistics equal one. ∎

## 6. Example

Take the collapsed representation

\[
f=(0,0,1,0),\qquad S=\{1,2\}.
\]

It expands to the dimension-two improper matrix

\[
Q_{11}=\{1\},\qquad Q_{12}=\{2,3,6\},\qquad Q_{22}=\{4,5\}.
\]

The cell containing `6` has odd size, so `Q` is in the source minus class, and `v(Q)=4`. The insertion map gives `sigma=(3,1,2,4)`. The marked column selects descent bottom `1`, and hence

\[
\Gamma_6(Q)=(\{3,1\},\{2\},\{4\}).
\]

The recursive decoder gives

\[
\rho_6(Q)=(0,0,1,2,2,3).
\]

This sequence is in the target minus class and has distinct-value set `{0,1,2,3}`, so `dist=4=v(Q)`. Formula (12) recovers the same `f`, `S`, and `Q`.
