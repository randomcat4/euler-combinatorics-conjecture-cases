# Boundary Counterexample to the K33+ Q-Index Classification

*Jian Zheng, Yongtao Li, and Honghai Li - [DOI](https://doi.org/10.1016/j.laa.2025.10.036) - [arXiv](https://arxiv.org/abs/2504.07852)*

This package records a boundary counterexample to Conjecture 5.1 in Zheng, Li, and Li, *The signless Laplacian spectral Turan problems for color-critical graphs*.

The source conjecture asserts that, for `2 <= s <= t` and `n >= s+t`, every `n`-vertex `K_{s,t}^+`-free graph with maximum signless-Laplacian spectral radius belongs to one of the two displayed families `L_{n,s,t}` or `Y_{n,t}`. At the boundary point

```text
s = t = 3, n = 6,
```

the graph `K2 join (K3 union K1)` is `K_{3,3}^+`-free, uniquely maximizes the Q-index among all six-vertex `K_{3,3}^+`-free graphs, and is not a member of either printed family. This disproves the exact all-quantifier statement of Conjecture 5.1 as printed.

This case does not address a separately amended or intended sufficiently-large-`n` version of the conjecture, and it does not claim public priority.

## Contents

- [problem.md](problem.md) records the source statement, definitions, scope, and non-claims.
- [proof.md](proof.md) gives the displayed counterexample and the finite maximality certificate.
- [verification.md](verification.md) explains the independent mathematical review and executable check.
- [status.md](status.md) separates correctness, scope, formalization, and public priority.
- [sources.md](sources.md) gives the public sources and citation anchors.
- [check_counterexample.py](check_counterexample.py) exhaustively verifies the boundary case using exact arithmetic and Sturm counts.
- [exhaustive_summary.json](exhaustive_summary.json) records the checker's compact output.

Public priority is **NOT_ESTABLISHED**.
