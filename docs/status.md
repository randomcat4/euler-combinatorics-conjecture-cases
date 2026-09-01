# Public index status

This repository is a continuing public index rather than a count of all EULER research outcomes. Public material may be hosted here or linked from another curated repository, and it may have been produced across different workspaces and compute environments.

## Counterexamples

- Zhao short zero-sum conjectures: Conjectures 6.1 and 6.2 are disproved; Conjecture 6.4's lower branch is refuted at `C_2^7`; Conjecture 1.2 has a supplemental even-rank witness. The package is supported by symbolic arguments, exact enumeration, and Sidorenko's cited exact value for `s_4(C_2^7)`.
- Volume rigidity: Conjecture 22 is disproved for every dimension `d>=7` and independently reviewed.
- K33+ Q-index classification: Conjecture 5.1 of the cited signless-Laplacian spectral Turan paper is disproved as printed by the boundary case `s=t=3,n=6`. The graph `K2 join (K3 union K1)` is `K_{3,3}^+`-free, uniquely extremal over all six-vertex `K_{3,3}^+`-free graphs, and outside the printed `L_{6,3,3}` and `Y_{6,3}` families.
- Toroidal-grid representation number: Conjecture 1 of the cited word-representation paper is disproved as printed by a length-45 3-uniform word for `TGr_{3,5}=C_3 square C_5`, giving `R(TGr_{3,5}) <= 3` despite the printed lower bound `R(TGr_{m,n}) >= 4` for `m,n >= 3` and `m+n >= 8`.

## Partial results

- Gao constant: a restricted-family result for generalized dihedral groups with an abelian odd-primary kernel, presented in a 13-page manuscript with the corresponding Lean formalization. It does not resolve the full Gao conjecture.
- Nonnormal Cayley graph eigenvalues: a result in the restricted `n-k=3` regime. It does not resolve Conjecture 4.7 outside that regime.

## Complete solutions

- Catalan--Schett plane-tree statistic: complete all-order solution with an explicit bijection and inverse.
- CDK image of improper partition matrices: complete all-order characterization for Question 5.5 in arXiv v2.
- Improper partition matrices: complete all-order statistic-preserving bijection with an explicit inverse.
- Partition-matrix q-sum-product: complete all-order formula for Question 5.1 under the stated closed-expression contract.

Other Gao-related problems are being curated and actively advanced. Additional EULER results will enter this index after their public artifacts and scope statements are ready.

Each local case records its status in its own directory and in `PROJECT_STATE.json`. Public novelty and priority remain `NOT_ESTABLISHED` unless a release explicitly records a completed prior-art determination.
