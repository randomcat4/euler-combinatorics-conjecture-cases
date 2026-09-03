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
python cases/orthogonal-tree-seven-vertex-obstructions/check_counterexamples.py
python cases/catalan-schett-plane-tree-statistic/check_small_cases.py
python cases/partition-matrix-bijection/verify_bijection.py
python cases/partition-matrix-q-sum-product/check_formula.py
python cases/cdk-improper-partition-matrix-image/mine_cdk_image.py --n-max 8 --check cases/cdk-improper-partition-matrix-image/mining_n_le_8.json
python cases/ternary-berge-suspension-rigidity/check_statement_certificate.py
python cases/entropy-bounded-sidon-concentration-stability/check_sidon_stability.py
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
      <td><sub>Conjectures 6.1 and 6.2; lower branch of Conjecture 6.4; supplemental Conjecture 1.2 witness</sub></td>
      <td><sub>Independent mathematical review and exhaustive exact checks</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/volume-rigidity-dimension-seven/">Volume rigidity</a></sub></td>
      <td><sub><a href="https://doi.org/10.1007/s00493-026-00218-x"><em>Combinatorica</em> 46 (2026), Article 23</a></sub></td>
      <td><sub>Counterexample</sub></td>
      <td><sub>Conjecture 22 for every <code>d&gt;=7</code></sub></td>
      <td><sub>Independent mathematical review</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/k33plus-q-index-boundary-counterexample/">K33+ Q-index classification</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.laa.2025.10.036"><em>Linear Algebra and its Applications</em> 730 (2026), 546-565</a></sub></td>
      <td><sub>Counterexample</sub></td>
      <td><sub>Conjecture 5.1 at <code>s=t=3,n=6</code></sub></td>
      <td><sub>Independent mathematical review and exhaustive exact check</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/toroidal-grid-representation-counterexample/">Toroidal-grid representation number</a></sub></td>
      <td><sub><a href="https://arxiv.org/abs/2507.16469v1">arXiv:2507.16469v1</a></sub></td>
      <td><sub>Counterexample</sub></td>
      <td><sub>Conjecture 1 at <code>TGr_{3,5}=C_3 square C_5</code></sub></td>
      <td><sub>Independent mathematical review and exact all-pairs check</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/path-set-tree-representation-counterexample/">Path-set tree representation</a></sub></td>
      <td><sub><a href="https://arxiv.org/abs/2506.03603v1">arXiv:2506.03603v1</a> / <a href="https://doi.org/10.37236/14646">DOI</a></sub></td>
      <td><sub>Counterexample</sub></td>
      <td><sub>Unnumbered sufficiency question after Theorem 3.2; five-vertex family</sub></td>
      <td><sub>Independent mathematical review and exact all-tree check</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/f29-inducibility-recursive-graphon-counterexample/">F29 inducibility</a></sub></td>
      <td><sub><a href="https://arxiv.org/abs/2606.00290v3">arXiv:2606.00290v3</a></sub></td>
      <td><sub>Counterexample</sub></td>
      <td><sub>Conjecture 4.7 equality <code>lambda_F29=24/1555</code></sub></td>
      <td><sub>Independent mathematical review and exact recursive-density check</sub></td>
    </tr>
    <tr>
      <td><sub><a href="https://github.com/randomcat4/gaoLEAN">Gao constant</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.ejc.2004.06.014"><em>European Journal of Combinatorics</em> 26 (2005), 1053–1059</a></sub></td>
      <td><sub>Partial result with formal proof</sub></td>
      <td><sub>Restricted odd-primary generalized dihedral family</sub></td>
      <td><sub>Lean-checked manuscript theorem</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/minimal-degree-three-imprimitive-groups/">Minimal-degree-three imprimitive groups</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.jcta.2025.106065"><em>Journal of Combinatorial Theory, Series A</em> 216 (2025), Article 106065</a></sub></td>
      <td><sub>Partial result</sub></td>
      <td><sub>Problem 2 display (1.2) family, all <code>m&gt;=3,k&gt;=1</code></sub></td>
      <td><sub>Independent mathematical review and exact quotient/support check</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/steklov-three-leaf-extra-special-extremizer/">Steklov three-leaf extremizer</a></sub></td>
      <td><sub><a href="https://arxiv.org/abs/2508.13466v1">arXiv:2508.13466v1</a></sub></td>
      <td><sub>Partial result</sub></td>
      <td><sub>Conjecture 1.3 complete <code>b=3</code> slice, all <code>r&gt;=1</code></sub></td>
      <td><sub>Independent mathematical review and spider arithmetic check</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/minimum-degree-two-degree-multiplicity/">Minimum-degree-two degree multiplicity</a></sub></td>
      <td><sub><a href="https://doi.org/10.1017/S0963548322000220"><em>Combinatorics, Probability and Computing</em> 32(2) (2023), 223-232</a>; <a href="https://doi.org/10.1016/j.jctb.2025.04.008"><em>Journal of Combinatorial Theory, Series B</em> 175 (2025), 203-243</a></sub></td>
      <td><sub>Partial result</sub></td>
      <td><sub>Complete <code>delta(G)=2</code> slice of Alon--Wei Conjecture 1.2 / Ma--Xie Conjecture 5.4</sub></td>
      <td><sub>Two independent mathematical reviews and exact <code>2C4</code> sharpness check</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/orthogonal-tree-seven-vertex-obstructions/">Orthogonal-tree obstructions</a></sub></td>
      <td><sub><a href="https://arxiv.org/abs/2512.15516">arXiv:2512.15516v2</a></sub></td>
      <td><sub>Partial result</sub></td>
      <td><sub>Two seven-vertex induced-minimal obstructions to the gem/house/HVN sufficiency rule; full Question 15 remains open</sub></td>
      <td><sub>Independent mathematical review and exact finite checks</sub></td>
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
      <td><sub><a href="cases/cdk-improper-partition-matrix-image/">CDK improper image</a></sub></td>
      <td><sub><a href="https://doi.org/10.1016/j.jcta.2026.106213"><em>Journal of Combinatorial Theory, Series A</em> 223 (2026), Article 106213</a></sub></td>
      <td><sub>Complete characterization</sub></td>
      <td><sub>Question 5.5 in arXiv v2</sub></td>
      <td><sub>Independent mathematical review</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/ternary-berge-suspension-rigidity/">Ternary-Berge hypergraphs</a></sub></td>
      <td><sub><a href="https://doi.org/10.1007/s00493-026-00198-y"><em>Combinatorica</em> 46 (2026), Article 8</a></sub></td>
      <td><sub>Complete solution</sub></td>
      <td><sub>Question 5.5 for finite hypergraphs with no ternary Berge cycle</sub></td>
      <td><sub>Independent mathematical review</sub></td>
    </tr>
    <tr>
      <td><sub><a href="cases/entropy-bounded-sidon-concentration-stability/">Entropy-bounded Sidon concentration</a></sub></td>
      <td><sub><a href="https://doi.org/10.1109/TIT.2026.3653549"><em>IEEE Transactions on Information Theory</em> 72(3):1553-1568 (2026)</a></sub></td>
      <td><sub>Complete solution with optimal-modulus extension</sub></td>
      <td><sub>Section 5 unnumbered open problem for arbitrary abelian groups; fixed-<code>D</code> optimal stability rate</sub></td>
      <td><sub>Independent mathematical reviews of the solution and extension, plus finite sanity probes</sub></td>
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

### Zhao's short zero-sum conjectures

*Kevin Zhao · [arXiv:2506.21383](https://arxiv.org/abs/2506.21383)*

The public case records a bounded-scope counterexample package around Zhao's short zero-sum conjectures. It disproves Conjecture 6.1 at `C_2 direct-sum C_4^3`; disproves both branches of Conjecture 6.2 using an infinite `C_n^4` family and finite witnesses; refutes the lower branch of Conjecture 6.4 at `C_2^7`; and records a supplemental even-rank witness for Conjecture 1.2.

The package includes the symbolic arguments, all finite witnesses, Sidorenko's exact input `s_4(C_2^7)=15`, and a dependency-free checker for the exact finite certificates. It does not claim that every conjecture in the source paper is false, and it does not claim public priority.

[Open the Zhao counterexample package](cases/zhao-restricted-zero-sum-counterexample/)

### Volume rigidity in dimensions d >= 7

*James Cruickshank, Bill Jackson, and Shin-ichi Tanigawa · [DOI](https://doi.org/10.1007/s00493-026-00218-x) · [arXiv](https://arxiv.org/abs/2503.01647)*

Conjecture 22 in the cited volume-rigidity paper predicts rigidity for a family built from a simplicial 2-sphere. The public case constructs a symbolic non-Euclidean infinitesimal motion for every permitted simplicial 2-sphere and cone set in every dimension `d>=7`. It disproves the conjecture throughout that range, while making no exact generic-corank claim.

[Open the volume-rigidity counterexample package](cases/volume-rigidity-dimension-seven/)

### A boundary counterexample to a K33+ Q-index classification

*Jian Zheng, Yongtao Li, and Honghai Li · [DOI](https://doi.org/10.1016/j.laa.2025.10.036) · [arXiv](https://arxiv.org/abs/2504.07852)*

Conjecture 5.1 in the cited signless-Laplacian spectral Turan paper predicts that every extremal `K_{s,t}^+`-free graph belongs to one of two displayed families for all `2<=s<=t` and `n>=s+t`. The public case gives a complete boundary counterexample at `s=t=3,n=6`: `K2 join (K3 union K1)` is `K_{3,3}^+`-free, uniquely maximizes the Q-index over the full six-vertex denominator, and is not in `L_{6,3,3}` or `Y_{6,3}`.

The package does not address a separately amended sufficiently-large-`n` version and does not claim public priority.

[Open the K33+ Q-index counterexample package](cases/k33plus-q-index-boundary-counterexample/)

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

### Minimal-degree-three imprimitive groups

*Antonio Montero and Primoz Potocnik · [DOI](https://doi.org/10.1016/j.jcta.2025.106065) · [arXiv](https://arxiv.org/abs/2405.10088v2)*

Problem 2 in the cited paper asks for a detailed description of transitive
permutation groups of minimal degree 3, including the displayed imprimitive
family `Alt(m)^k <= G <= Sym(m) wr Sym(k)`. The public case proves the
complete quotient criterion for that family, for every `m>=3` and `k>=1`:
transitivity is exactly transitivity of the top projection, and minimal degree
3 is obtained exactly when the base parity kernel has no Hamming-weight-one
vector.

This is a complete result for the displayed imprimitive family, not a full
classification of all transitive permutation groups of minimal degree 3.

[Open the minimal-degree-three imprimitive-groups package](cases/minimal-degree-three-imprimitive-groups/)

### Steklov three-leaf extra-special extremizer

*Huiqiu Lin and Da Zhao · [arXiv](https://arxiv.org/abs/2508.13466v1)*

Conjecture 1.3 in the cited paper predicts an extra-special extremal tree for
the first nonzero Steklov eigenvalue under fixed leaf count and matching
number. The public case proves the complete `b=3` slice: every three-leaf tree
with matching number `3r+2` satisfies
`sigma_2(T) <= sigma_2^-(ES_{3,2r})`, with equality exactly for the spider
whose arm lengths are `{2r+2,2r+1,2r}`.

This is a partial result and does not address `b=2` or `b>=4`.

[Open the Steklov three-leaf package](cases/steklov-three-leaf-extra-special-extremizer/)

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

### The CDK image of improper partition matrices

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

Question 5.5 in arXiv v2 asks for a characterization of the inversion sequences obtained from improper partition matrices under the Claesson-Dukes-Kubitzke bijection. The public case proves an intrinsic all-order predicate: inside the intervals cut out by the distinct values of the inversion sequence, adjacent local pairs starting at odd local position must have equal values.

The source locator is version-sensitive: arXiv v1 Question 5.5 is a different direct-bijection problem, now Question 5.7 in arXiv v2.

[Open the CDK image characterization](cases/cdk-improper-partition-matrix-image/)

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
