# Path-Set Tree Representation Counterexample

*Maria Chudnovsky, Tung Nguyen, Alex Scott, and Paul Seymour - [arXiv](https://arxiv.org/abs/2506.03603v1) - [DOI](https://doi.org/10.37236/14646)*

This package records a five-vertex counterexample to the sufficiency question
asked after Theorem 3.2 in Chudnovsky, Nguyen, Scott, and Seymour, *The vertex
sets of subtrees of a tree*.

The source question asks whether three necessary conditions are sufficient for
a finite family of subsets of a finite set `W` to be exactly a family of vertex
sets of paths in a tree whose vertex set is `W`. The conditions are finite
Helly, chordality of the intersection graph, and Tucker's interval condition
on every local trace family.

For

```text
W = {0,1,2,3,4}
F = {{0,1}, {0,2}, {1,3}, {0,1,2,4}, {0,1,3,4}},
```

all three source conditions hold. However, no tree on vertex set exactly `W`
has all five members of `F` as vertex sets of simple paths. Therefore the
three necessary conditions are not sufficient.

This case does not propose a corrected characterization of path-set families
in trees, does not classify all five-vertex families, and does not claim public
priority.

## Contents

- [problem.md](problem.md) records the source statement, definitions, scope, and non-claims.
- [proof.md](proof.md) gives the finite family and the direct nonrepresentation proof.
- [verification.md](verification.md) explains the independent mathematical review and executable check.
- [status.md](status.md) separates correctness, scope, formalization, and public priority.
- [sources.md](sources.md) gives the public source and citation anchors.
- [counterexample_certificate.json](counterexample_certificate.json) records the family and expected finite counts.
- [check_counterexample.py](check_counterexample.py) verifies the family using only the Python standard library.
- [verification_summary.json](verification_summary.json) records the checker's compact output.

Public priority is **NOT_ESTABLISHED**.
