# EULER Mathematical Research Outcomes

This repository is a growing public index of curated mathematical outcomes produced with the EULER agent system. It is one of the first public release surfaces from EULER's case-study program on conjectures posed by authors who had published in leading combinatorics journals, specifically [Journal of Combinatorial Theory, Series A](https://www.sciencedirect.com/journal/journal-of-combinatorial-theory-series-a), [Journal of Combinatorial Theory, Series B](https://www.sciencedirect.com/journal/journal-of-combinatorial-theory-series-b), [Combinatorica](https://link.springer.com/journal/493), and [European Journal of Combinatorics](https://www.sciencedirect.com/journal/european-journal-of-combinatorics), within the program's preceding 24-26-month selection window. The aim is to anchor that window as closely as possible to the **training cutoff of the base model used by EULER**, and, as much as possible, to select problems posed after that cutoff. Preliminary ablation results suggest that, on this frozen conjecture library, an EULER configuration relying mainly on DeepSeek-V4P and GPT-5.5 High, with a post-trained Qwen3-7B model for routing, achieved outcomes close to those obtained with the 5.6 Pro + 5.6 Sol High configuration at roughly 27% of the cost.

It records the portion of a broader research program that has completed its public curation process.

## Reproduce in 60 seconds

```bash
git clone https://github.com/randomcat4/euler-combinatorics-conjecture-cases.git
cd euler-combinatorics-conjecture-cases
python scripts/validate_repo.py
python cases/zhao-restricted-zero-sum-counterexample/check_counterexample.py
python cases/k33plus-q-index-boundary-counterexample/check_counterexample.py
python cases/toroidal-grid-representation-counterexample/check_counterexample.py
python cases/path-set-tree-representation-counterexample/check_counterexample.py
python cases/f29-inducibility-recursive-graphon-counterexample/check_counterexample.py
python cases/minimal-degree-three-imprimitive-groups/check_quotient_criterion.py
python cases/steklov-three-leaf-extra-special-extremizer/check_three_leaf_extremizer.py
python cases/minimum-degree-two-degree-multiplicity/check_sharpness.py
python cases/five-point-sixteen-shattering/check_crossing_obstruction.py
python cases/orthogonal-tree-seven-vertex-obstructions/check_counterexamples.py
python cases/catalan-schett-plane-tree-statistic/check_small_cases.py
python cases/partition-matrix-bijection/verify_bijection.py
python cases/partition-matrix-q-sum-product/check_formula.py
python cases/cdk-improper-partition-matrix-image/mine_cdk_image.py --n-max 8 --check cases/cdk-improper-partition-matrix-image/mining_n_le_8.json
python cases/ternary-berge-suspension-rigidity/check_statement_certificate.py
python cases/entropy-bounded-sidon-concentration-stability/check_sidon_stability.py
```

The initial-pass checks above use the Python standard library and verify the repository boundary,
the published artifact manifest, and the executable finite certificates. Each new extension package
has its own reproduction instructions and recorded coverage; spectral checks list their additional
dependencies and numerical tolerances.

## Public result index

Every public result remains listed below. The first rows are the current extension-review batch, placed first for reviewer convenience; this ordering is not a ranking.

<code>2h</code> marks an outcome from the initial two-hour EULER research window. <code>+2h</code> marks an outcome from the later extension allocation; extension work may resume an interrupted earlier run and may reuse the earlier case state, so it should not be read as an independent four-hour rerun or as two full additional hours on every case.

Each updated <code>+2h</code> case includes a clean proof PDF and a companion package with the original problem, a proof guide, sources, precise status, and reproducible independent checks where available. Finite tests and numerical agreement are distinguished from general proofs. The original public files remain available as the initial-pass record; internal review transcripts, audit logs, routing, and verdict files are not mirrored into this repository.

<table>
  <thead>
    <tr>
      <th>Source problem</th>
      <th>EULER result</th>
      <th>Exact public scope</th>
      <th>Pass</th>
      <th>Verification</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://doi.org/10.1016/j.jcta.2025.106065">Montero–Potočnik, <em>JCTA</em> 216 (2025)</a><br>Problem 2</td>
      <td><a href="cases/minimal-degree-three-imprimitive-groups/"><strong>Minimal-degree-three groups</strong></a><br>Classification<br><a href="cases/minimal-degree-three-imprimitive-groups/paper/extension.pdf">Proof PDF</a></td>
      <td>All transitive permutation groups of minimal degree 3 via intrinsic blocks, invariant binary codes and cocycles; regular cyclic top actions are classified up to permutation conjugacy.</td>
      <td><code>+2h</code></td>
      <td>Independent model proof review; exact cyclic-code and cocycle checks through 12 blocks.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1016/j.jcta.2025.106049">Lin–Liu–Yan, <em>JCTA</em> 215 (2025)</a><br>Problem 2.18</td>
      <td><a href="cases/catalan-schett-plane-tree-statistic/"><strong>Plane-tree statistic</strong></a><br>Complete solution + run refinement<br><a href="cases/catalan-schett-plane-tree-statistic/paper/extension.pdf">Proof PDF</a></td>
      <td>Explicit tree/permutation bijection solves the original joint identity and retains the complete inverse ascending-run composition, with arbitrary multiplicative run weights.</td>
      <td><code>+2h</code></td>
      <td>Independent model proof review; exact full-signature enumeration through 9 edges.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1016/j.jcta.2026.106213">Chern–Fu, <em>JCTA</em> 223 (2026)</a><br>Question 5.7</td>
      <td><a href="cases/partition-matrix-bijection/"><strong>Partition-matrix bijection</strong></a><br>Complete solution + full-class refinement<br><a href="cases/partition-matrix-bijection/paper/extension.pdf">Proof PDF</a></td>
      <td>Explicit mutual inverses for the minus and full classes; preserves <code>v=dist</code>, dimension and the full ordered column-parity signature, with Eulerian/Stirling enumerations.</td>
      <td><code>+2h</code></td>
      <td>Independent model proof review; exact three-way bijection and signature checks through size 8.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1016/j.jcta.2026.106213">Chern–Fu, <em>JCTA</em> 223 (2026)</a><br>Question 5.1</td>
      <td><a href="cases/partition-matrix-q-sum-product/"><strong>Partition-matrix q-series</strong></a><br>Complete formula + cell-size refinement<br><a href="cases/partition-matrix-q-sum-product/paper/extension.pdf">Proof PDF</a></td>
      <td>Self-contained sum-product solution; standard basic-hypergeometric form for every fixed column series; arbitrary multiplicative weights for all cell cardinalities.</td>
      <td><code>+2h</code></td>
      <td>Independent model proof review; exact coefficients through size 8 and numerical series cross-checks.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1016/j.jcta.2026.106213">Chern–Fu, <em>JCTA</em> 223 (2026)</a><br>Question 5.5</td>
      <td><a href="cases/cdk-improper-partition-matrix-image/"><strong>CDK improper image</strong></a><br>Complete characterization + orbit theorem<br><a href="cases/cdk-improper-partition-matrix-image/paper/extension.pdf">Proof PDF</a></td>
      <td>Intrinsic value-interval characterization, followed by the complete commuting pair-swap orbit classification, one-sided images, defect distribution and exact row-nonempty enumeration.</td>
      <td><code>+2h</code></td>
      <td>Independent model proof review; exact CDK, orbit and counting checks through size 8.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1016/j.jcta.2025.106097">Li–Xia–Zhou, <em>JCTA</em> 218 (2026)</a><br>Conjecture 4.7</td>
      <td><a href="https://github.com/randomcat4/euler-combinatorics-conjecture-cases/pull/17"><strong>Cayley representation uniqueness</strong></a><br>Complete solution (proof draft)<br><a href="https://github.com/randomcat4/euler-combinatorics-conjecture-cases/blob/case/cayley-c47-complete/cases/cayley-eigenvalue-codimension-three/paper/full_conjecture.pdf">Proof PDF in PR #17</a></td>
      <td>Every <code>n&gt;=5</code> and <code>1&lt;=r&lt;k&lt;=n-2</code>; exact attaining representations are classified. The separate <code>k=n-1</code> questions are excluded.</td>
      <td><code>+2h</code></td>
      <td>Three quoted finite boundary computations; exact implementation is not supplied. Domain review pending.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1016/j.laa.2025.10.036">Zheng–Li–Li, <em>LAA</em> 730 (2026)</a><br>Conjecture 5.1</td>
      <td><a href="cases/k33plus-q-index-boundary-counterexample/"><strong>K33+ Q-index classification</strong></a><br>Counterexample + structural theorem<br><a href="cases/k33plus-q-index-boundary-counterexample/paper/extension.pdf">Proof PDF</a></td>
      <td>Analytic unique optimum at <code>s=t=3,n=6</code>; exact classification in the full two-universal-vertex class for <code>n&gt;=7</code>; source families fail at <code>n=8</code> and every <code>n&gt;=10</code>. No unrestricted large-order maximizer classification is claimed.</td>
      <td><code>+2h</code></td>
      <td>Independent model proof review; exhaustive six-vertex containment tests with numerical spectra.</td>
    </tr>
    <tr>
      <td><a href="https://arxiv.org/abs/2508.13466v1">Lin–Zhao, arXiv:2508.13466v1</a><br>Conjecture 1.3</td>
      <td><a href="cases/steklov-three-leaf-extra-special-extremizer/"><strong>Steklov extremizer</strong></a><br>Complete solution + strengthening<br><a href="cases/steklov-three-leaf-extra-special-extremizer/paper/extension.pdf">Proof PDF</a></td>
      <td>All <code>b&gt;=2</code> and <code>r&gt;=1</code>; strengthens matching equality to <code>nu(T)&gt;=br+2</code>, proves unique equality, and gives the sharp optimum for every central leaf split at minimum diameter.</td>
      <td><code>+2h</code></td>
      <td>Independent model proof review; trees through 12 vertices and numerical checks of both Steklov formulations.</td>
    </tr>
    <tr>
      <td><a href="https://arxiv.org/abs/2506.21383">arXiv:2506.21383</a><br>Conjectures 6.1, 6.2 and 6.4</td>
      <td><a href="cases/zhao-restricted-zero-sum-counterexample/"><strong>Zhao short zero sums</strong></a><br>Counterexamples</td>
      <td>Conjectures 6.1 and 6.2; lower branch of Conjecture 6.4; supplemental Conjecture 1.2 witness.</td>
      <td><code>2h</code></td>
      <td>Independent mathematical review and exhaustive exact checks.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1016/j.ejc.2004.06.014">Gao, <em>European Journal of Combinatorics</em> 26 (2005)</a></td>
      <td><a href="https://github.com/randomcat4/gaoLEAN"><strong>Gao constant</strong></a><br>Partial result with formal proof</td>
      <td>Restricted odd-primary generalized dihedral family.</td>
      <td><code>2h</code></td>
      <td>Lean-checked manuscript theorem.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1007/s00493-026-00218-x"><em>Combinatorica</em> 46 (2026), Article 23</a><br>Conjecture 22</td>
      <td><a href="cases/volume-rigidity-dimension-seven/"><strong>Volume rigidity</strong></a><br>Counterexample</td>
      <td>Conjecture 22 for every <code>d&gt;=7</code>.</td>
      <td><code>2h</code></td>
      <td>Independent mathematical review.</td>
    </tr>
    <tr>
      <td><a href="https://arxiv.org/abs/2507.16469v1">arXiv:2507.16469v1</a><br>Conjecture 1</td>
      <td><a href="cases/toroidal-grid-representation-counterexample/"><strong>Toroidal-grid representation number</strong></a><br>Counterexample</td>
      <td>Conjecture 1 at <code>TGr_{3,5}=C_3 square C_5</code>.</td>
      <td><code>2h</code></td>
      <td>Independent mathematical review and exact all-pairs check.</td>
    </tr>
    <tr>
      <td><a href="https://arxiv.org/abs/2506.03603v1">arXiv:2506.03603v1</a> / <a href="https://doi.org/10.37236/14646">DOI</a><br>Question after Theorem 3.2</td>
      <td><a href="cases/path-set-tree-representation-counterexample/"><strong>Path-set tree representation</strong></a><br>Counterexample</td>
      <td>Five-vertex family disproving the stated sufficiency rule.</td>
      <td><code>2h</code></td>
      <td>Independent mathematical review and exact all-tree check.</td>
    </tr>
    <tr>
      <td><a href="https://arxiv.org/abs/2606.00290v3">arXiv:2606.00290v3</a><br>Conjecture 4.7</td>
      <td><a href="cases/f29-inducibility-recursive-graphon-counterexample/"><strong>F29 inducibility</strong></a><br>Counterexample</td>
      <td>Refutes the equality <code>lambda_F29=24/1555</code>; no true global optimum is claimed.</td>
      <td><code>2h</code></td>
      <td>Independent mathematical review and exact recursive-density check.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1017/S0963548322000220"><em>CPC</em> 32(2) (2023)</a> / <a href="https://doi.org/10.1016/j.jctb.2025.04.008"><em>JCTB</em> 175 (2025)</a><br>Alon–Wei Conjecture 1.2 / Ma–Xie Conjecture 5.4</td>
      <td><a href="cases/minimum-degree-two-degree-multiplicity/"><strong>Minimum-degree-two degree multiplicity</strong></a><br>Partial result</td>
      <td>Complete <code>delta(G)=2</code> slice for all finite simple graphs on <code>n&gt;=3</code> vertices.</td>
      <td><code>2h</code></td>
      <td>Two independent mathematical reviews and exact <code>2C4</code> sharpness check.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1007/s00493-026-00201-6"><em>Combinatorica</em> 46 (2026), Article 10</a><br>Conjecture 4.2</td>
      <td><a href="cases/five-point-sixteen-shattering/"><strong>Five-point permutation shattering</strong></a><br>Partial result</td>
      <td>Complete <code>k=5</code> slice for all <code>1&lt;=t&lt;=16</code>.</td>
      <td><code>2h</code></td>
      <td>Two independent mathematical reviews and a finite crossing-obstruction check.</td>
    </tr>
    <tr>
      <td><a href="https://arxiv.org/abs/2512.15516">arXiv:2512.15516v2</a><br>Question 15</td>
      <td><a href="cases/orthogonal-tree-seven-vertex-obstructions/"><strong>Orthogonal-tree obstructions</strong></a><br>Partial result</td>
      <td>Two seven-vertex induced-minimal obstructions to the gem/house/HVN sufficiency rule; the full question remains open.</td>
      <td><code>2h</code></td>
      <td>Independent mathematical review and exact finite checks.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1007/s00493-026-00198-y"><em>Combinatorica</em> 46 (2026), Article 8</a><br>Question 5.5</td>
      <td><a href="cases/ternary-berge-suspension-rigidity/"><strong>Ternary-Berge hypergraphs</strong></a><br>Complete solution</td>
      <td>Question 5.5 for finite hypergraphs with no ternary Berge cycle.</td>
      <td><code>2h</code></td>
      <td>Independent mathematical review.</td>
    </tr>
    <tr>
      <td><a href="https://doi.org/10.1109/TIT.2026.3653549"><em>IEEE Transactions on Information Theory</em> 72(3) (2026)</a><br>Section 5 unnumbered open problem</td>
      <td><a href="cases/entropy-bounded-sidon-concentration-stability/"><strong>Entropy-bounded Sidon concentration</strong></a><br>Complete solution + optimal-modulus extension</td>
      <td>Arbitrary abelian groups; fixed-<code>D</code> optimal stability rate.</td>
      <td><code>2h</code></td>
      <td>Independent mathematical reviews of the solution and extension, plus finite sanity probes.</td>
    </tr>
  </tbody>
</table>

## The EULER system

The [public EULER repository](https://github.com/randomcat4/EULER) exposes a demonstration and reference implementation of the Research Kernel and selected auditable research workflows. That public version is a demo and lags behind the EULER system used in current research, which has a wider orchestration, verification, formalization, and long-horizon research surface.

## Counterexamples

### Zhao's short zero-sum conjectures

*Kevin Zhao · [arXiv:2506.21383](https://arxiv.org/abs/2506.21383)*

The public case records a bounded-scope counterexample package around Zhao's short zero-sum conjectures. It disproves Conjecture 6.1 at `C_2 direct-sum C_4^3`; disproves both branches of Conjecture 6.2 using an infinite `C_n^4` family and finite witnesses; refutes the lower branch of Conjecture 6.4 at `C_2^7`; and records a supplemental even-rank witness for Conjecture 1.2.

The package includes the symbolic arguments, all finite witnesses, Sidorenko's exact input `s_4(C_2^7)=15`, and a dependency-free checker for the exact finite certificates. It does not claim that every conjecture in the source paper is false, and it does not claim public priority.

[Open the Zhao counterexample package](cases/zhao-restricted-zero-sum-counterexample/)

### Volume rigidity in dimensions d >= 7

*James Cruickshank, Bill Jackson, and Shin-ichi Tanigawa · [DOI](https://doi.org/10.1007/s00493-026-00218-x) · [arXiv](https://arxiv.org/abs/2503.01647)*

Conjecture 22 in the cited volume-rigidity paper predicts rigidity for a family built from a simplicial 2-sphere. The public case constructs a symbolic non-Euclidean infinitesimal motion for every permitted simplicial 2-sphere and cone set in every dimension `d>=7`. It disproves the conjecture throughout that range, while making no exact generic-corank claim.

[Open the volume-rigidity counterexample package](cases/volume-rigidity-dimension-seven/)

### A counterexample and a sharp two-universal-vertex theorem

*Jian Zheng, Yongtao Li, and Honghai Li · [DOI](https://doi.org/10.1016/j.laa.2025.10.036) · [arXiv](https://arxiv.org/abs/2504.07852)*

**Initial 2h.** The initial package certified the six-vertex counterexample by an exact finite enumeration.

**+2h extension.** The six-vertex counterexample is proved uniquely optimal by an elementary complement argument. For all n>=7, the note determines the sharp Q-index and every equality graph in the entire two-universal-vertex class. The source classification also fails at n=8 and at every n>=10.

The unrestricted large-order maximizing graphs are not classified. The infinite-order obstruction does not assume that the displayed constructions are unrestricted maximizers.

[Read the proof PDF](cases/k33plus-q-index-boundary-counterexample/paper/extension.pdf) · [Open the case](cases/k33plus-q-index-boundary-counterexample/)

### A 3-uniform word for a toroidal grid boundary case

*Nawaf Shafi Alshammari, Sergey Kitaev, and Artem Pyatkin · [arXiv](https://arxiv.org/abs/2507.16469v1)*

Conjecture 1 in the cited toroidal-grid representation-number paper asserts
that if `m,n >= 3` and `m+n >= 8`, then `R(TGr_{m,n}) >= 4`, where
`TGr_{m,n}=C_m square C_n`. The public case gives a length-45 3-uniform word
for `TGr_{3,5}=C_3 square C_5`. It proves `R(TGr_{3,5}) <= 3`, and therefore
disproves the exact printed universal statement.

The package does not classify any other toroidal grid and does not claim public
priority.

[Open the toroidal-grid representation counterexample package](cases/toroidal-grid-representation-counterexample/)

### A five-set obstruction to path-set tree representation

*Maria Chudnovsky, Tung Nguyen, Alex Scott, and Paul Seymour · [DOI](https://doi.org/10.37236/14646) · [arXiv](https://arxiv.org/abs/2506.03603v1)*

The source asks whether finite Helly, chordality of the intersection graph, and
Tucker's interval condition on every local trace family are sufficient for a
finite family of subsets of `W` to be realized as vertex sets of paths in a tree
on vertex set exactly `W`. The public case gives a family of five subsets of
`{0,1,2,3,4}` satisfying all three conditions, then proves no such tree exists.

The package does not propose a corrected characterization and does not claim
public priority.

[Open the path-set tree representation counterexample package](cases/path-set-tree-representation-counterexample/)

### An F29 recursive-graphon counterexample

*Levente Bodnar, Jun Gao, Jared Leon, Xizhi Liu, Oleg Pikhurko, and Shumin Sun · [arXiv](https://arxiv.org/abs/2606.00290v3)*

Conjecture 4.7 in the cited inducibility paper states that
`lambda_F29=24/1555` for `F29=(6,{03,04,13,15,45})`. Under the source
normalization, the equal-measure six-part recursive graphon pattern
`off=010100000100101;diag=RRRRRR` has exact density
`6232/402745 = 24/1555 + 16/402745`, so it disproves the stated equality.

The package does not determine the true inducibility value of `F29`, classify
any other six-vertex graph, or claim public priority.

[Open the F29 inducibility counterexample package](cases/f29-inducibility-recursive-graphon-counterexample/)

## Partial results



### Minimum-degree-two degree multiplicity

*Noga Alon and Fan Wei · [DOI](https://doi.org/10.1017/S0963548322000220) · [arXiv](https://arxiv.org/abs/2108.02685v2); Jie Ma and Shengjie Xie · [DOI](https://doi.org/10.1016/j.jctb.2025.04.008) · [arXiv](https://arxiv.org/abs/2406.05675v1)*

The public case proves the complete `delta(G)=2` slice of the degree-multiplicity
problem: every finite simple graph on `n>=3` vertices with minimum degree two
has a spanning subgraph `H` such that every degree class of `H` has size at most
`floor(n/3)+2`. The proof allows disconnected graphs, unbounded maximum degree,
parallel edges in the compressed pseudokernel, and kernel loops arising from
closed degree-two threads.

The graph `2C4` attains the integer bound, so the bound cannot be lowered to
`3` at `n=8`. This is a partial result for the general minimum-degree
conjecture and does not claim the stronger bounds for `delta(G)>2`.

[Open the minimum-degree-two degree-multiplicity package](cases/minimum-degree-two-degree-multiplicity/)

### Five-point sixteen-shattering permutation families

*Antonio Girao, Lukas Michel, and Youri Tamitegama · [DOI](https://doi.org/10.1007/s00493-026-00201-6) · [arXiv](https://arxiv.org/abs/2407.05773v1)*

The public case proves the complete `k=5` slice of Conjecture 4.2. For every
`n>=5`, one preselected family of
`O(sqrt(log n * log log n))` permutations of `[n]` induces at least 16
relative orders on every five-element subset. Consequently
`f_5(n,t)=o(log n)` for every fixed `1<=t<=16`.

This does not address general `k` or determine the exact growth rate. The
proof is analytic; its finite checker covers only the crossing-partition
lemma used in the construction.

[Open the five-point sixteen-shattering package](cases/five-point-sixteen-shattering/)

### Seven-vertex orthogonal-tree obstructions

*Maria Axenovich, Dingyuan Liu, and Arsenii Sagdeev · [arXiv](https://arxiv.org/abs/2512.15516)*

Question 15 asks for a characterization of graphs representable by orthogonal
trees. The public case proves two seven-vertex induced-minimal obstructions
outside the previously identified gem, house, and HVN obstructions. The two
graphs are certified as nonrepresentable by exact tree-metric arguments, while
each proper induced subgraph is representable.

This disproves the three-obstruction sufficiency rule. It does not solve the
full orthogonal-tree characterization problem or classify all seven-vertex
obstructions.

[Open the orthogonal-tree obstruction package](cases/orthogonal-tree-seven-vertex-obstructions/)

### The Gao constant for generalized dihedral groups

*Jujuan Zhuang and Weidong Gao · [DOI](https://doi.org/10.1016/j.ejc.2004.06.014) · supporting sources: [Gao 1996](https://doi.org/10.1006/jnth.1996.0067), [Godara–Joshi–Mazumdar 2026](https://doi.org/10.1016/j.jnt.2025.11.011)*

The Gao release proves

$$
E\bigl(\mathrm{Dih}(A)\bigr)
=2|A|+D(A)
=|\mathrm{Dih}(A)|+d\bigl(\mathrm{Dih}(A)\bigr)
$$

for every nontrivial finite abelian odd-primary group $A$. This is a restricted-family result, not a resolution of the full Gao conjecture. Its public scope is the completed [13-page manuscript](https://github.com/randomcat4/gaoLEAN/blob/main/paper/arxiv/main.pdf) and the corresponding [Lean formalization](https://github.com/randomcat4/gaoLEAN/blob/main/GaoLean/PR7ThirteenPage.lean), collected in [Gao Lean](https://github.com/randomcat4/gaoLEAN).

Other Gao-related problems are being curated and actively advanced. Their public packages will be added when the corresponding arguments and release materials are ready.

## Proof draft under review

### Nonnormal Cayley graph eigenvalues

*Yuxuan Li, Binzhou Xia, and Sanming Zhou · [DOI](https://doi.org/10.1016/j.jcta.2025.106097) · [arXiv](https://arxiv.org/abs/2402.02427)*

Conjecture 4.7 concerns representation-level uniqueness for a family of nonnormal Cayley graphs on symmetric groups. The initial 2h package establishes the `k=n-3` slice. The +2h proof draft in [PR #17](https://github.com/randomcat4/euler-combinatorics-conjecture-cases/pull/17) covers every `n>=5, 1<=r<k<=n-2`; its three quoted finite computations remain a stated reproducibility limit. The separate `k=n-1` questions are excluded.

[Open the Cayley eigenvalue package](cases/cayley-eigenvalue-codimension-three/)

## Complete solutions

### The Steklov extremizer for every leaf count

*Huiqiu Lin and Da Zhao · [arXiv](https://arxiv.org/abs/2508.13466v1)*

**Initial 2h.** The initial package proved the complete three-leaf slice.

**+2h extension.** For every b>=2 and integer r>=1, the matching threshold nu(T)>=br+2 implies the conjectured sharp Steklov bound, with the unique equality tree. The note also determines the sharp optimum for each positive-integer central leaf split at the smallest possible diameter.

The trees are finite, simple and unweighted, with counting measure on the leaf boundary. The two-leaf path endpoint is explicit.

[Read the proof PDF](cases/steklov-three-leaf-extra-special-extremizer/paper/extension.pdf) · [Open the case](cases/steklov-three-leaf-extra-special-extremizer/)


### Minimal-degree-three groups

*Antonio Montero and Primoz Potocnik · [DOI](https://doi.org/10.1016/j.jcta.2025.106065) · [arXiv](https://arxiv.org/abs/2405.10088v2)*

**Initial 2h.** The initial note proved the quotient criterion for the displayed imprimitive family.

**+2h extension.** All transitive permutation groups of minimal degree three are described by intrinsic alternating blocks, invariant binary codes and cocycles. The note gives full permutation-conjugacy criteria and classifies every regular cyclic top action, including even lengths.

Conjugacy means conjugacy of permutation actions, not abstract group isomorphism or unrestricted equivalence of cyclic codes.

[Read the proof PDF](cases/minimal-degree-three-imprimitive-groups/paper/extension.pdf) · [Open the case](cases/minimal-degree-three-imprimitive-groups/)


### Plane trees and inverse ascending runs

*Zhicong Lin, Jing Liu, and Sherry H. F. Yan · [DOI](https://doi.org/10.1016/j.jcta.2025.106049) · [arXiv](https://arxiv.org/abs/2409.01558)*

**Initial 2h.** The initial note gave the intrinsic tree statistic and its original two-statistic bijection.

**+2h extension.** The original joint tree/permutation identity is proved by explicit inverse constructions. The extension retains the entire inverse ascending-run composition and allows arbitrary multiplicative run weights, including zero weights and disjoint d-packet statistics.

The coefficient formulas are formal power-series identities; classical Catalan coefficient formulas are attributed.

[Read the proof PDF](cases/catalan-schett-plane-tree-statistic/paper/extension.pdf) · [Open the case](cases/catalan-schett-plane-tree-statistic/)

### A cyclic-partition bijection for partition matrices

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

**Initial 2h.** The initial note established the statistic-preserving minus bijection.

**+2h extension.** A common cyclic set partition gives explicit inverse maps for the original minus classes and the full classes. Dimension and the complete ordered column-parity signature are retained, with Eulerian and Stirling enumerations.

The source already related existence of the minus and full bijections; the note attributes that reduction and the known enumerations.

[Read the proof PDF](cases/partition-matrix-bijection/paper/extension.pdf) · [Open the case](cases/partition-matrix-bijection/)

### Partition-matrix q-series and cell cardinalities

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

**Initial 2h.** The initial note specified the column series by finite q-difference equations.

**+2h extension.** A complete column-word proof gives the original sum-product. Each fixed column series then has a standard basic-hypergeometric expression, and the same formula extends to arbitrary multiplicative cell-cardinality weights.

The full ordinary generating series is formal. Analytic convergence is asserted only for each fixed column series when |q|<1.

[Read the proof PDF](cases/partition-matrix-q-sum-product/paper/extension.pdf) · [Open the case](cases/partition-matrix-q-sum-product/)

### The CDK image and independent pair orientations

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

**Initial 2h.** The initial note proved the all-order value-interval characterization.

**+2h extension.** The value-interval condition completely describes the improper image under the CDK bijection. Allowing unequal matched pairs gives every pair-swap orbit, its one-sided representatives, the binomial directional distribution and an exact row-nonempty enumeration.

The swaps preserve column sizes and every cell cardinality. The row-nonempty condition restricts possible records, not their orientations.

[Read the proof PDF](cases/cdk-improper-partition-matrix-image/paper/extension.pdf) · [Open the case](cases/cdk-improper-partition-matrix-image/)

### Ternary-Berge-free hypergraph independence complexes

*Jinha Kim · [DOI](https://doi.org/10.1007/s00493-026-00198-y) · [arXiv](https://arxiv.org/abs/2408.14321)*

Question 5.5 asks whether every finite hypergraph with no Berge cycle whose
length is divisible by three has independence complex contractible or homotopy
equivalent to a sphere. The public case proves the complete statement by
combining edge-star graphification, Kim's ternary-graph theorem, Kim's
star-cluster suspension theorem, and a finite-CW suspension-rigidity argument.

The package does not claim public priority.

[Open the ternary-Berge suspension-rigidity solution](cases/ternary-berge-suspension-rigidity/)

### Entropy-bounded Sidon concentration stability

*Rupert Li, Lampros Gavalakis, and Ioannis Kontoyiannis · [DOI](https://doi.org/10.1109/TIT.2026.3653549) · [arXiv](https://arxiv.org/abs/2506.20813v2)*

The Section 5 unnumbered open problem in the cited entropic additive-energy
paper asks whether the minimum-atom dependence in Proposition 5.2 can be
replaced by a stability function depending only on the defect `C` and entropy
bound `D`. The public case proves the complete statement for arbitrary
discrete finite-entropy random variables on arbitrary abelian groups, with
explicit bound
`min{1, 2D/log(1/C) + sqrt(C)/log 2}` for `0<C<1`, endpoint values `0` at
`C=0` and `1` for `C>=1`, and the required fixed-`D` limit as `C->0`.

The package also proves the leading-order optimal stability modulus
`M(C,D)=D/log(1/C)*(1+o(1))` for each fixed `D>0`, via a Lambert-W optimized
threshold upper bound and finite integer no-carry lower-bound constructions.
It separately records a low-entropy joint regime with `sqrt(C)` order. The
package does not claim exact finite-parameter optimality or public priority.

[Open the entropy-bounded Sidon concentration solution](cases/entropy-bounded-sidon-concentration-stability/)

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
