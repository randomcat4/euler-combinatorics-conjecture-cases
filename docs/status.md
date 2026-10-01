# Public index status

This repository is a continuing public index rather than a count of all EULER research outcomes. Public material may be hosted here or linked from another curated repository, and it may have been produced across different workspaces and compute environments.

## Counterexamples

- Zhao short zero-sum conjectures: Conjectures 6.1 and 6.2 are disproved; Conjecture 6.4's lower branch is refuted at `C_2^7`; Conjecture 1.2 has a supplemental even-rank witness. The package is supported by symbolic arguments, exact enumeration, and Sidorenko's cited exact value for `s_4(C_2^7)`.
- Volume rigidity: Conjecture 22 is disproved for every dimension `d>=7` and independently reviewed.
- K33+ Q-index classification: the original six-vertex counterexample is now proved uniquely extremal by an analytic argument. The extension gives the sharp bound and all equality graphs throughout the two-universal-vertex class for n>=7, and disproves the printed families at n=8 and every n>=10. It does not classify unrestricted large-order maximizers.
- Toroidal-grid representation number: Conjecture 1 of the cited word-representation paper is disproved as printed by a length-45 3-uniform word for `TGr_{3,5}=C_3 square C_5`, giving `R(TGr_{3,5}) <= 3` despite the printed lower bound `R(TGr_{m,n}) >= 4` for `m,n >= 3` and `m+n >= 8`.
- Path-set tree representation: the sufficiency question after Theorem 3.2 of the cited path-set paper is disproved by a five-subset family on `{0,1,2,3,4}` satisfying finite Helly, chordal intersection graph, and every local Tucker interval condition, but admitting no tree whose path vertex sets include all five members.
- F29 inducibility: Conjecture 4.7 of the cited six-vertex graph inducibility paper is disproved by an equal-measure six-part recursive graphon with exact density `6232/402745`, strictly larger than the conjectured value `24/1555`.

## Partial results

- Minimum-degree-two degree multiplicity: complete `delta(G)=2` slice of Alon--Wei Conjecture 1.2 / Ma--Xie Conjecture 5.4. It proves that every finite simple graph on `n>=3` vertices with minimum degree two has a spanning subgraph whose every degree class has size at most `floor(n/3)+2`; it does not prove the stronger general minimum-degree bounds for `delta(G)>2`.
- Five-point permutation shattering: complete `k=5` slice of Girao--Michel--Tamitegama Conjecture 4.2. For every `n>=5`, one preselected family of `O(sqrt(log n * log log n))` permutations induces at least 16 relative orders on every five-element subset, and hence `f_5(n,t)=o(log n)` for every fixed `1<=t<=16`. General `k` and the exact growth rate remain open.
- Orthogonal-tree obstructions: two seven-vertex induced-minimal nonrepresentable graphs avoiding the previously identified gem, house, and HVN obstructions. This disproves the three-obstruction sufficiency rule for Question 15 but does not solve the full orthogonal-tree characterization problem.
- Gao constant: a restricted-family result for generalized dihedral groups with an abelian odd-primary kernel, presented in a 13-page manuscript with the corresponding Lean formalization. It does not resolve the full Gao conjecture.

## Complete solutions and classifications

- Minimal-degree-three groups: the initial displayed-family quotient criterion is retained; the extension gives the intrinsic alternating-block/code/cocycle parametrization of all transitive minimal-degree-three actions and the full cyclic-top conjugacy classification.
- Steklov extremizer: the initial b=3 slice is retained; the extension proves the all-leaf theorem for b>=2 and r>=1, strengthens matching equality to nu(T)>=br+2, and determines the sharp central-split bound and equality trees.

- Nonnormal Cayley graph eigenvalues: complete proof of Conjecture 4.7 for every `n>=5` and `1<=r<k<=n-2`. An independent model review examines the general argument and its published inputs; all three finite inputs now have reproducible rational characteristic polynomials and Sturm certificates. Initial human review is completed; see [the review record](provenance.md).
- Catalan--Schett plane-tree statistic: complete all-order solution with an explicit bijection and inverse, extended to the full inverse ascending-run composition and arbitrary multiplicative run weights.
- CDK image of improper partition matrices: complete characterization for Question 5.5 in arXiv v2, extended to commuting pair-swap orbits, one-sided images, defect distributions and exact row-nonempty enumeration.
- Improper partition matrices: explicit mutual inverses for the minus and full classes, preserving semi-weight, dimension and the complete ordered column-parity signature, with attributed Eulerian/Stirling counts.
- Partition-matrix q-sum-product: a self-contained formula for Question 5.1, a basic-hypergeometric expression for each fixed column series, and arbitrary cell-cardinality weights. The outer ordinary series is interpreted formally.
- Ternary-Berge-free hypergraph independence complexes: complete solution of Kim's Question 5.5 for all finite hypergraphs with no Berge cycle whose length is divisible by three.
- Entropy-bounded Sidon concentration stability: complete solution of the Section 5 unnumbered open problem in Li, Gavalakis, and Kontoyiannis, giving an explicit function of `C` and `D` for arbitrary discrete finite-entropy random variables on arbitrary abelian groups; the same case also proves the fixed-`D` optimal stability modulus `M(C,D)=D/log(1/C)*(1+o(1))`.

Other Gao-related problems are being curated and actively advanced. Additional EULER results will enter this index after their public artifacts and scope statements are ready.

Each local case records its status in its own directory and in `PROJECT_STATE.json`. Public novelty and priority remain `NOT_ESTABLISHED` unless a release explicitly records a completed prior-art determination.

## Merged release and reuse

PR #17 and PR #22 are merged. The current eight-case extensions are published,
with their earlier restricted results retained as historical records.
All repository-authored proofs and code are MIT licensed, with research-credit
and priority claims waived. The [review record](provenance.md) identifies the
LLM re-review, initial human review, and counterexample-specialist invitations.
