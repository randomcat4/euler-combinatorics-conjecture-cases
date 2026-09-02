# F29 Inducibility Recursive-Graphon Counterexample

*Levente Bodnar, Jun Gao, Jared Leon, Xizhi Liu, Oleg Pikhurko, and Shumin Sun - [arXiv](https://arxiv.org/abs/2606.00290v3)*

This package records a counterexample to Conjecture 4.7 in Bodnar, Gao, Leon,
Liu, Pikhurko, and Sun, *The inducibility of 6-vertex graphs*.

The source conjecture states that, for

```text
F29=(6,{03,04,13,15,45}),
```

the inducibility value is `lambda_F29 = 24/1555`. Under the source induced
density normalization, the equal-measure six-part recursive graphon pattern

```text
off=010100000100101;diag=RRRRRR
```

has exact density

```text
p(F29,W)=6232/402745 = 24/1555 + 16/402745.
```

This is strictly larger than the conjectured value, so the equality statement
of Conjecture 4.7 is false.

The case does not determine the true inducibility of `F29`, does not classify
other six-vertex graphs, and does not claim public priority.

## Contents

- [problem.md](problem.md) records the source statement, definitions, scope, and non-claims.
- [proof.md](proof.md) gives the recursive-graphon witness and exact-density argument.
- [verification.md](verification.md) explains the independent mathematical review and executable check.
- [status.md](status.md) separates correctness, scope, computation, and public priority.
- [sources.md](sources.md) gives the public source and citation anchor.
- [counterexample_certificate.json](counterexample_certificate.json) records the graphon patterns and exact expected densities.
- [check_counterexample.py](check_counterexample.py) verifies the densities using only the Python standard library.
- [verification_summary.json](verification_summary.json) records the checker's compact output.

Public priority is **NOT_ESTABLISHED**.
