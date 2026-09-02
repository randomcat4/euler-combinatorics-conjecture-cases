# Verification

## Mathematical Review

The strict partial result was checked by a fresh read-only mathematical and
paper-level reviewer. The review returned `CORRECT` for the same frozen
statement and proof now curated in this public case. The check covered:

1. the exact source locator for arXiv:2512.15516v2, Appendix B.2, Question 15;
2. the equivalence between orthogonal-tree representability and equality
   graphs at value `1` in positive weighted tree metrics;
3. the translation to exact even leaf powers, including rationalization,
   denominator clearing, parity, marked vertices, and nonedge avoidance;
4. the graph data for `H_adj` and `H_dis`, including graph6 strings, edge
   sets, old-obstruction freeness, and induced minimality;
5. the four-point-condition proof excluding `H_adj`;
6. the unit-triangle median-branch proof excluding `H_dis`;
7. all fourteen one-vertex deletion witnesses;
8. the exact 143,816-topology certificate metadata and blocker counts;
9. the bounded search scope `1044 -> 427 -> 39 -> 37+2`, without upgrading it
   to a complete seven-vertex classification; and
10. the public boundaries: full Question 15 remains open and public priority is
    `NOT_ESTABLISHED`.

## Finite Certificate Check

The checker [check_counterexamples.py](check_counterexamples.py) verifies the
machine-readable certificate [counterexample_certificate.json](counterexample_certificate.json).
It checks:

- graph6 decoding and edge-set equality for both seven-vertex graphs;
- canonical bitstrings;
- absence of induced gem, house, and `HVN`;
- exact rational positive weighted-tree witnesses for every one-vertex
  deletion; and
- the recorded seven-marked topology denominator and blocker-count metadata.

Run it from the repository root:

```bash
python cases/orthogonal-tree-seven-vertex-obstructions/check_counterexamples.py
```

Expected output:

```text
PASS: orthogonal-tree obstruction certificate verified
```

## Verification Boundary

The checker verifies the finite graph and certificate data. It does not prove
the two symbolic nonrepresentability arguments; those are supplied in
[proof.md](proof.md) and were independently reviewed. The case has not been
encoded in a proof assistant. Public novelty and priority remain
`NOT_ESTABLISHED`.
