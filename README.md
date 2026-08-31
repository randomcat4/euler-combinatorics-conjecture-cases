# EULER Mathematical Research Outcomes

This repository is a growing public index of curated mathematical outcomes produced with the EULER agent system. It is one of the first public release surfaces from EULER's case-study program on conjectures posed by authors who had published in leading combinatorics journals within the program's preceding 24-month selection window.

The index is not tied to one computer, one workspace, one batch size, or one repository. It records the portion of a broader research program that has completed its public curation process.

## The EULER system

The [public EULER demonstration repository](https://github.com/randomcat4/ai4math-research-kernel) exposes an earlier version of the Research Kernel and selected auditable research workflows. That public version is a demo and lags behind the EULER system used in current research, which has a wider orchestration, verification, formalization, and long-horizon research surface.

## Counterexamples

### Zhao's restricted-length zero-sum conjecture

Kevin Zhao's Conjecture 6.1 predicts a sharp endpoint for short zero-sum subsequences in a class of finite abelian groups. The public case gives a symbolic counterexample in

$$
C_2\oplus C_4^3.
$$

The displayed length-12 sequence has exactly nine nonempty zero-sum occurrence-subsequences, all of length 10, and therefore none of length at most 9. The package includes the complete classification and a dependency-free exhaustive checker over all 4,095 nonempty occurrence-subsets.

[Open the Zhao counterexample package](cases/zhao-restricted-zero-sum-counterexample/)

### Volume rigidity in dimension seven

Conjecture 22 in the cited volume-rigidity paper predicts rigidity for a family built from a simplicial 2-sphere. The public case constructs a symbolic non-Euclidean infinitesimal motion for every six-vertex simplicial 2-sphere and disproves the complete `d=7` slice.

[Open the volume-rigidity counterexample package](cases/volume-rigidity-dimension-seven/)

## Complete solutions and full arguments

### The Gao constant for generalized dihedral groups

The Gao release proves

$$
E\bigl(\operatorname{Dih}(A)\bigr)
=2|A|+D(A)
=|\operatorname{Dih}(A)|+d\bigl(\operatorname{Dih}(A)\bigr)
$$

for every nontrivial finite abelian odd-primary group $A$. Its public scope is the completed [13-page manuscript](https://github.com/randomcat4/gaoLEAN/blob/main/paper/arxiv/main.pdf) and the corresponding [Lean formalization](https://github.com/randomcat4/gaoLEAN/blob/main/GaoLean/PR7ThirteenPage.lean), collected in [Gao Lean](https://github.com/randomcat4/gaoLEAN).

Other Gao-related problems are being curated and actively advanced. Their public packages will be added when the corresponding arguments and release materials are ready.

### A Catalan--Schett statistic on plane trees

Problem 2.18 asks for a natural statistic on rooted plane trees that directly interprets a bivariate distribution on 231-avoiding permutations. The public case defines an intrinsic terminating tree statistic and gives an explicit all-order bijection, inverse, and objectwise preservation proof.

[Open the plane-tree solution](cases/catalan-schett-plane-tree-statistic/)

### A direct bijection for improper partition matrices

Question 5.7 asks for a direct statistic-preserving bijection between a signed class of improper partition matrices and a signed class of restricted inversion sequences. The public case gives a uniform all-order map, an explicit inverse, an exact image proof, and objectwise preservation of both statistics.

[Open the partition-matrix solution](cases/partition-matrix-bijection/)

## Complete parameter layers

### Nonnormal Cayley graph eigenvalues

Conjecture 4.7 concerns representation-level uniqueness for a family of nonnormal Cayley graphs on symmetric groups. The public case proves the complete `k=n-3` layer for every admissible `n`, with a symbolic general argument and exact low-order certificates.

[Open the Cayley eigenvalue package](cases/cayley-eigenvalue-codimension-three/)

## Public result index

| Outcome | Result type | Public scope | Verification | Novelty |
|---|---|---|---|---|
| Zhao short zero sums | Counterexample | Conjecture 6.1 disproved by one explicit group and sequence | Symbolic classification and exhaustive exact check | `NOT_ESTABLISHED` |
| Volume rigidity | Counterexample | Complete dimension-seven slice disproved | Independent mathematical review | `NOT_ESTABLISHED` |
| Gao constant | Full theorem with formal proof | Odd-primary generalized dihedral family | Lean-checked manuscript theorem | `NOT_ESTABLISHED` |
| Plane-tree statistic | Complete solution | Complete cited open problem | Independent mathematical review | `NOT_ESTABLISHED` |
| Partition-matrix bijection | Complete solution | Complete cited open problem | Independent mathematical review | `NOT_ESTABLISHED` |
| Cayley eigenvalues | Complete parameter layer | Complete `n-k=3` layer | Independent mathematical review | `NOT_ESTABLISHED` |

## Quick navigation

- [Collection status](docs/status.md)
- [Source bibliography](docs/sources.md)
- [Evidence and verification workflow](docs/workflow.md)
- [Publication and provenance boundary](docs/provenance.md)
- [Case index](cases/README.md)

## Repository principles

1. Counterexamples, complete solutions, full theorems, and parameter-layer results are reported as different result types.
2. Correctness, scope, computation, formal verification, novelty, and publication priority are separate judgments.
3. A finite calculation may certify a finite witness or discharge a proved finite remainder; it does not replace a general argument.
4. Candidate construction and independent verification are kept logically separate.
5. Public files contain curated mathematical artifacts rather than operational research logs or private coordination history.
6. Source-paper problem numbers remain visible as public citation anchors; internal project identifiers do not.

## Scope and attribution

This is an independent research archive produced with the EULER system. The cited authors, journals, publishers, and source repositories are not presented as maintainers or endorsers of this archive.

Authorship, licensing, journal submission, and priority decisions remain part of the human publication process.
