# Public index status

This repository is a continuing public index rather than a count of all EULER research outcomes. Public material may be hosted here or linked from another curated repository, and it may have been produced across different workspaces and compute environments.

## Counterexamples

- Zhao short zero-sum conjectures: Conjectures 6.1 and 6.2 are disproved; Conjecture 6.4's lower branch is refuted at `C_2^7`; Conjecture 1.2 has a supplemental even-rank witness. The package is supported by symbolic arguments, exact enumeration, and Sidorenko's cited exact value for `s_4(C_2^7)`.
- Volume rigidity: Conjecture 22 is disproved for every dimension `d>=7` and independently reviewed.
- K33+ Q-index classification: Conjecture 5.1 of the cited signless-Laplacian spectral Turan paper is disproved as printed by the boundary case `s=t=3,n=6`. The graph `K2 join (K3 union K1)` is `K_{3,3}^+`-free, uniquely extremal over all six-vertex `K_{3,3}^+`-free graphs, and outside the printed `L_{6,3,3}` and `Y_{6,3}` families.
- Toroidal-grid representation number: Conjecture 1 of the cited word-representation paper is disproved as printed by a length-45 3-uniform word for `TGr_{3,5}=C_3 square C_5`, giving `R(TGr_{3,5}) <= 3` despite the printed lower bound `R(TGr_{m,n}) >= 4` for `m,n >= 3` and `m+n >= 8`.
- Path-set tree representation: the sufficiency question after Theorem 3.2 of the cited path-set paper is disproved by a five-subset family on `{0,1,2,3,4}` satisfying finite Helly, chordal intersection graph, and every local Tucker interval condition, but admitting no tree whose path vertex sets include all five members.
- F29 inducibility: Conjecture 4.7 of the cited six-vertex graph inducibility paper is disproved by an equal-measure six-part recursive graphon with exact density `6232/402745`, strictly larger than the conjectured value `24/1555`.

## Partial results

- Minimal-degree-three imprimitive groups: complete quotient criterion for the display (1.2) family `Alt(m)^k <= G <= Sym(m) wr Sym(k)` from Problem 2 of the cited paper, for all `m>=3` and `k>=1`. It does not classify all transitive permutation groups of minimal degree 3.
- Steklov three-leaf extra-special extremizer: complete infinite `b=3` slice of Conjecture 1.3 of the cited Steklov-tree paper, for all three-leaf trees with matching number `3r+2` and all `r>=1`. It does not address `b=2` or `b>=4`.
- Minimum-degree-two degree multiplicity: complete `delta(G)=2` slice of Alon--Wei Conjecture 1.2 / Ma--Xie Conjecture 5.4. It proves that every finite simple graph on `n>=3` vertices with minimum degree two has a spanning subgraph whose every degree class has size at most `floor(n/3)+2`; it does not prove the stronger general minimum-degree bounds for `delta(G)>2`.
- Orthogonal-tree obstructions: two seven-vertex induced-minimal nonrepresentable graphs avoiding the previously identified gem, house, and HVN obstructions. This disproves the three-obstruction sufficiency rule for Question 15 but does not solve the full orthogonal-tree characterization problem.
- Gao constant: a restricted-family result for generalized dihedral groups with an abelian odd-primary kernel, presented in a 13-page manuscript with the corresponding Lean formalization. It does not resolve the full Gao conjecture.
- Nonnormal Cayley graph eigenvalues: a result in the restricted `n-k=3` regime. It does not resolve Conjecture 4.7 outside that regime.

## Complete solutions

- Catalan--Schett plane-tree statistic: complete all-order solution with an explicit bijection and inverse.
- CDK image of improper partition matrices: complete all-order characterization for Question 5.5 in arXiv v2.
- Improper partition matrices: complete all-order statistic-preserving bijection with an explicit inverse.
- Partition-matrix q-sum-product: complete all-order formula for Question 5.1 under the stated closed-expression contract.
- Ternary-Berge-free hypergraph independence complexes: complete solution of Kim's Question 5.5 for all finite hypergraphs with no Berge cycle whose length is divisible by three.
- Entropy-bounded Sidon concentration stability: complete solution of the Section 5 unnumbered open problem in Li, Gavalakis, and Kontoyiannis, giving an explicit function of `C` and `D` for arbitrary discrete finite-entropy random variables on arbitrary abelian groups; the same case also proves the fixed-`D` optimal stability modulus `M(C,D)=D/log(1/C)*(1+o(1))`.

Other Gao-related problems are being curated and actively advanced. Additional EULER results will enter this index after their public artifacts and scope statements are ready.

Each local case records its status in its own directory and in `PROJECT_STATE.json`. Public novelty and priority remain `NOT_ESTABLISHED` unless a release explicitly records a completed prior-art determination.
