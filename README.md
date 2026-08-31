# EULER Mathematical Research Outcomes

This repository is a growing public index of curated mathematical outcomes produced with the EULER agent system. It is one of the first public release surfaces from EULER's case-study program on conjectures posed by authors who had published in leading combinatorics journals within the program's preceding 24-month selection window.

The index is not tied to one computer, one workspace, one batch size, or one repository. It records the portion of a broader research program that has completed its public curation process.

## Reproduce in 60 seconds

```bash
git clone https://github.com/randomcat4/euler-combinatorics-conjecture-cases.git
cd euler-combinatorics-conjecture-cases
python scripts/validate_repo.py
python cases/zhao-restricted-zero-sum-counterexample/check_counterexample.py
python cases/catalan-schett-plane-tree-statistic/check_small_cases.py
python cases/partition-matrix-bijection/verify_bijection.py
python cases/partition-matrix-q-sum-product/check_formula.py
```

The checks use the Python standard library and verify the repository boundary,
the published artifact manifest, and the executable finite certificates.

## Public result index

<table>
  <thead>
    <tr>
      <th><sub>Result</sub></th>
      <th><sub>Original publication</sub></th>
      <th><sub>Result type</sub></th>
      <th><sub>Public scope</sub></th>
      <th><sub>Verification</sub></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><sub><a href="cases/zhao-restricted-zero-sum-counterexample/">Zhao short zero sums</a></sub></td>
      <td><sub><a href="https://arxiv.org/abs/2506.21383">arXiv:2506.21383</a></sub></td>
      <td><sub>Counterexample</sub></td>
      <td><sub>Conjecture 6.1</sub></td>
      <td><sub>Symbolic classification and exhaustive exact check</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/volume-rigidity-dimension-seven/">Volume rigidity</a></sub></td>
      <td><sub><a href="https://doi.org/10.1007/s00493-026-00218-x"><em>Combinatorica</em> 46 (2026), Article 23</a></sub></td>
      <td><sub>Counterexample</sub></td>
      <td><sub>Complete dimension-seven slice</sub></td>
      <td><sub>Independent mathematical review</sub></td>
    </tr>
    <tr>
      <td><sub><a href="https://github.com/randomcat4/gaoLEAN">Gao constant</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.ejc.2004.06.014"><em>European Journal of Combinatorics</em> 26 (2005), 1053–1059</a></sub></td>
      <td><sub>Partial result with formal proof</sub></td>
      <td><sub>Restricted odd-primary generalized dihedral family</sub></td>
      <td><sub>Lean-checked manuscript theorem</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/catalan-schett-plane-tree-statistic/">Plane-tree statistic</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.jcta.2025.106049"><em>Journal of Combinatorial Theory, Series A</em> 215 (2025), Article 106049</a></sub></td>
      <td><sub>Complete solution</sub></td>
      <td><sub>Problem 2.18</sub></td>
      <td><sub>Independent mathematical review</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/partition-matrix-bijection/">Partition-matrix bijection</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.jcta.2026.106213"><em>Journal of Combinatorial Theory, Series A</em> 223 (2026), Article 106213</a></sub></td>
      <td><sub>Complete solution</sub></td>
      <td><sub>Question 5.7</sub></td>
      <td><sub>Independent mathematical review</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/partition-matrix-q-sum-product/">Partition-matrix q-sum-product</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.jcta.2026.106213"><em>Journal of Combinatorial Theory, Series A</em> 223 (2026), Article 106213</a></sub></td>
      <td><sub>Complete all-order formula</sub></td>
      <td><sub>Question 5.1 under the stated closed-expression contract</sub></td>
      <td><sub>Independent mathematical review</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/cayley-eigenvalue-codimension-three/">Cayley eigenvalues</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.jcta.2025.106097"><em>Journal of Combinatorial Theory, Series A</em> 218 (2026), Article 106097</a></sub></td>
      <td><sub>Partial parameter result</sub></td>
      <td><sub>The <code>n-k=3</code> regime of Conjecture 4.7 only</sub></td>
      <td><sub>Independent mathematical review</sub></td>
    </tr>
  </tbody>
</table>

## The EULER system

The [public EULER repository](https://github.com/randomcat4/EULER) exposes a demonstration and reference implementation of the Research Kernel and selected auditable research workflows. That public version is a demo and lags behind the EULER system used in current research, which has a wider orchestration, verification, formalization, and long-horizon research surface.

## Counterexamples

### Zhao's restricted-length zero-sum conjecture

*Kevin Zhao · [arXiv:2506.21383](https://arxiv.org/abs/2506.21383)*

Kevin Zhao's Conjecture 6.1 predicts a sharp endpoint for short zero-sum subsequences in a class of finite abelian groups. The public case gives a symbolic counterexample in

$$
C_2\oplus C_4^3.
$$

The displayed length-12 sequence has exactly nine nonempty zero-sum occurrence-subsequences, all of length 10, and therefore none of length at most 9. The package includes the complete classification and a dependency-free exhaustive checker over all 4,095 nonempty occurrence-subsets.

[Open the Zhao counterexample package](cases/zhao-restricted-zero-sum-counterexample/)

### Volume rigidity in dimension seven

*James Cruickshank, Bill Jackson, and Shin-ichi Tanigawa · [DOI](https://doi.org/10.1007/s00493-026-00218-x) · [arXiv](https://arxiv.org/abs/2503.01647)*

Conjecture 22 in the cited volume-rigidity paper predicts rigidity for a family built from a simplicial 2-sphere. The public case constructs a symbolic non-Euclidean infinitesimal motion for every six-vertex simplicial 2-sphere and disproves the complete `d=7` slice.

[Open the volume-rigidity counterexample package](cases/volume-rigidity-dimension-seven/)

## Partial results

### The Gao constant for generalized dihedral groups

*Jujuan Zhuang and Weidong Gao · [DOI](https://doi.org/10.1016/j.ejc.2004.06.014) · supporting sources: [Gao 1996](https://doi.org/10.1006/jnth.1996.0067), [Godara–Joshi–Mazumdar 2026](https://doi.org/10.1016/j.jnt.2025.11.011)*

The Gao release proves

$$
E\bigl(\operatorname{Dih}(A)\bigr)
=2|A|+D(A)
=|\operatorname{Dih}(A)|+d\bigl(\operatorname{Dih}(A)\bigr)
$$

for every nontrivial finite abelian odd-primary group $A$. This is a restricted-family result, not a resolution of the full Gao conjecture. Its public scope is the completed [13-page manuscript](https://github.com/randomcat4/gaoLEAN/blob/main/paper/arxiv/main.pdf) and the corresponding [Lean formalization](https://github.com/randomcat4/gaoLEAN/blob/main/GaoLean/PR7ThirteenPage.lean), collected in [Gao Lean](https://github.com/randomcat4/gaoLEAN).

Other Gao-related problems are being curated and actively advanced. Their public packages will be added when the corresponding arguments and release materials are ready.

### Nonnormal Cayley graph eigenvalues

*Yuxuan Li, Binzhou Xia, and Sanming Zhou · [DOI](https://doi.org/10.1016/j.jcta.2025.106097) · [arXiv](https://arxiv.org/abs/2402.02427)*

Conjecture 4.7 concerns representation-level uniqueness for a family of nonnormal Cayley graphs on symmetric groups. The public case establishes a result in the restricted `k=n-3` regime, with a symbolic general argument and exact low-order certificates. It does not resolve the conjecture outside that regime.

[Open the Cayley eigenvalue package](cases/cayley-eigenvalue-codimension-three/)

## Complete solutions

### A Catalan--Schett statistic on plane trees

*Zhicong Lin, Jing Liu, and Sherry H. F. Yan · [DOI](https://doi.org/10.1016/j.jcta.2025.106049) · [arXiv](https://arxiv.org/abs/2409.01558)*

Problem 2.18 asks for a natural statistic on rooted plane trees that directly interprets a bivariate distribution on 231-avoiding permutations. The public case defines an intrinsic terminating tree statistic and gives an explicit all-order bijection, inverse, and objectwise preservation proof.

[Open the plane-tree solution](cases/catalan-schett-plane-tree-statistic/)

### A direct bijection for improper partition matrices

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

Question 5.7 asks for a direct statistic-preserving bijection between a signed class of improper partition matrices and a signed class of restricted inversion sequences. The public case gives a uniform all-order map, an explicit inverse, an exact image proof, and objectwise preservation of both statistics.

[Open the partition-matrix solution](cases/partition-matrix-bijection/)

### A q-difference sum-product for partition matrices

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

Question 5.1 asks for a closed expression for the ordinary generating series of the inversion-weighted partition-matrix polynomials. The public case proves a finite q-difference specification of auxiliary word series and an all-order sum-product for `sum_{n>=1} S_n(q)t^n`, with coefficient equality in `Z[q][[t]]`.

Because the source does not define a formal grammar for "closed expression," the case states the answered all-order expression contract explicitly and does not attribute that contract to the source authors.

[Open the partition-matrix q-sum-product](cases/partition-matrix-q-sum-product/)

## Quick navigation

- [Collection status](docs/status.md)
- [Source bibliography](docs/sources.md)
- [Evidence and verification workflow](docs/workflow.md)
- [Publication and provenance boundary](docs/provenance.md)
- [Case index](cases/README.md)

## Repository principles

1. Counterexamples, complete solutions, and partial results are reported as different result types.
2. Correctness, scope, computation, formal verification, novelty, and publication priority are separate judgments.
3. A finite calculation may certify a finite witness or discharge a proved finite remainder; it does not replace a general argument.
4. Candidate construction and independent verification are kept logically separate.
5. Public files contain curated mathematical artifacts rather than operational research logs or private coordination history.
6. Source-paper problem numbers remain visible as public citation anchors; internal project identifiers do not.

## Scope and attribution

This is an independent research archive produced with the EULER system. The cited authors, journals, publishers, and source repositories are not presented as maintainers or endorsers of this archive.

Authorship, licensing, journal submission, and priority decisions remain part of the human publication process.

## License

Source code is licensed under the MIT License. Written mathematical content,
documentation, proofs, and manuscripts are licensed under Creative Commons
Attribution 4.0 International (CC BY 4.0). See [LICENSE](LICENSE) for the exact
scope and terms.
