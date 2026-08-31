# Counterexamples to a Volume-Rigidity Conjecture in All Dimensions d >= 7

*James Cruickshank, Bill Jackson, and Shin-ichi Tanigawa · [DOI](https://doi.org/10.1007/s00493-026-00218-x) · [arXiv](https://arxiv.org/abs/2503.01647)*

This case records a symbolic counterexample to Conjecture 22 in Cruickshank, Jackson, and Tanigawa, *Volume Rigidity of Simplicial Manifolds*, for every dimension \(d\ge 7\).

For \(d\ge 7\), write \(m=d-4\). For every simplicial 2-sphere on \(\lceil d/2\rceil+2\) vertices and every \((d-3)\)-element cone set \(Z\), the construction chooses a nonzero symmetric \(m\times m\) matrix \(K\) satisfying three trace/facet equations and builds a non-Euclidean affine motion \(u(v)=DKD^{\mathsf T}(p(v)-p(z_0))\). The motion annihilates the derivatives of all squared \((d-2)\)-volumes, so the hypergraph is not volume rigid in \(\mathbb R^d\).

The directory name is retained for link stability from the earlier dimension-seven release. The certified public scope is now the full range \(d\ge 7\). The package does not claim an exact generic corank formula.

This is one of the first cleaned, publicly releasable results from the Euler system's case library for conjectures posed by authors who had published in top-tier combinatorics journals within the preceding 24 months.

## Contents

- `problem.md` states the original conjecture and the exact range addressed here.
- `status.md` gives the mathematical and publication status.
- `sources.md` identifies the public primary source.
- `verification.md` summarizes the completed checks and their limitations.
- `paper/main.tex` is the self-contained English note.
- `paper/main.pdf` is the compiled note.
- `paper/references.bib` contains the public bibliography.
- `evidence/hyperedges.md` lists the complete hyperedge data used for exact cross-checks.
- `evidence/modular_rank_summary_d4_d9.json` summarizes the finite modular rank checks.
- `evidence/affine_flex_summary_d4_d9.json` summarizes the finite affine-flex-space checks.

## Scope and priority

The result disproves Conjecture 22 for every \(d\ge 7\). It does not settle the lower-dimensional cases already treated in the source paper, the broader manifold conjecture discussed there, or any exact-rank refinement beyond non-rigidity.

Public novelty or priority: `NOT_ESTABLISHED`.
