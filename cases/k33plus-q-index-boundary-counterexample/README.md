# A counterexample and a sharp two-universal-vertex theorem

**Source problem:** Conjecture 5.1 of Zheng--Li--Li. [Original statement and sources](problem.md).

**[Read the clean proof PDF](paper/extension.pdf)**

**Extension pass (+2h).** The six-vertex counterexample is proved uniquely optimal by an elementary complement argument. For all n>=7, the note determines the sharp Q-index and every equality graph in the entire two-universal-vertex class. The source classification also fails at n=8 and at every n>=10.

**Initial pass (2h).** The initial package certified the six-vertex counterexample by an exact finite enumeration.

The unrestricted large-order maximizing graphs are not classified. The infinite-order obstruction does not assume that the displayed constructions are unrestricted maximizers. Public priority is not established.

[Extension case files and independent checks](extension/)

<details>
<summary>Historical initial-pass package (the current result is above)</summary>

## Initial public package

The original description and public files below document the initial pass. They remain available; the extension manuscript above gives the later scope.

*Jian Zheng, Yongtao Li, and Honghai Li - [DOI](https://doi.org/10.1016/j.laa.2025.10.036) - [arXiv](https://arxiv.org/abs/2504.07852)*

This package records a boundary counterexample to Conjecture 5.1 in Zheng, Li, and Li, *The signless Laplacian spectral Turan problems for color-critical graphs*.

The source conjecture asserts that, for `2 <= s <= t` and `n >= s+t`, every `n`-vertex `K_{s,t}^+`-free graph with maximum signless-Laplacian spectral radius belongs to one of the two displayed families `L_{n,s,t}` or `Y_{n,t}`. At the boundary point

```text
s = t = 3, n = 6,
```

the graph `K2 join (K3 union K1)` is `K_{3,3}^+`-free, uniquely maximizes the Q-index among all six-vertex `K_{3,3}^+`-free graphs, and is not a member of either printed family. This disproves the exact all-quantifier statement of Conjecture 5.1 as printed.

This case does not address a separately amended or intended sufficiently-large-`n` version of the conjecture, and it does not claim public priority.

### Contents

- [problem.md](problem.md) records the source statement, definitions, scope, and non-claims.
- [proof.md](proof.md) gives the displayed counterexample and the finite maximality certificate.
- [verification.md](verification.md) explains the independent mathematical review and executable check.
- [status.md](status.md) separates correctness, scope, formalization, and public priority.
- [sources.md](sources.md) gives the public sources and citation anchors.
- [check_counterexample.py](check_counterexample.py) exhaustively verifies the boundary case using exact arithmetic and Sturm counts.
- [exhaustive_summary.json](exhaustive_summary.json) records the checker's compact output.

Public priority is **NOT_ESTABLISHED**.

</details>

## Review and reuse

These proofs were generated autonomously by EULER and are released under the
[MIT License](../../LICENSE), with research-credit and priority claims waived.
The [review record](../../docs/provenance.md) describes Sol High and Opus 4.8
xhigh re-review, initial human review by the author and doctoral students at
ETH Zürich and Peking University, and the invitation to specialists for
preliminary counterexample review. Mathematical and computational scope is
stated separately in this package.
