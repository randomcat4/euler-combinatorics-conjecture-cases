# Toroidal Grid Representation-Number Counterexample

*Nawaf Shafi Alshammari, Sergey Kitaev, and Artem Pyatkin - [arXiv](https://arxiv.org/abs/2507.16469v1)*

This package records a boundary counterexample to Conjecture 1 in Alshammari,
Kitaev, and Pyatkin, *On the representation number of grid graphs and cylindric
grid graphs*.

The source conjecture asserts that, for `m,n >= 3` with `m+n >= 8`,
`R(TGr_{m,n}) >= 4`, where `TGr_{m,n}=C_m square C_n` and `R(G)` is the
representation number of the graph. At the boundary point

```text
(m,n) = (3,5),
```

the graph `TGr_{3,5}=C_3 square C_5` has a length-45 3-uniform word
representation. This proves `R(TGr_{3,5}) <= 3`, contradicting the printed
lower bound for a parameter pair satisfying all printed hypotheses. Therefore
the exact all-quantifier statement of Conjecture 1 is false as printed.

This case does not classify `R(TGr_{m,n})` for any other pair `(m,n)`, does not
address any amended version of the conjecture, and does not claim public
priority.

## Contents

- [problem.md](problem.md) records the source statement, definitions, scope, and non-claims.
- [proof.md](proof.md) gives the displayed word and the all-pairs verification argument.
- [verification.md](verification.md) explains the independent mathematical review and executable check.
- [status.md](status.md) separates correctness, scope, formalization, and public priority.
- [sources.md](sources.md) gives the public source and citation anchor.
- [word_certificate.json](word_certificate.json) records the graph, word, and expected finite counts.
- [check_counterexample.py](check_counterexample.py) verifies the word using only the Python standard library.
- [verification_summary.json](verification_summary.json) records the checker's compact output.

Public priority is **NOT_ESTABLISHED**.
