# Verification

## Independent Mathematical Review

A fresh read-only mathematical verifier checked the frozen counterexample
package and returned `CORRECT`. The review covered:

1. the exact source quantifiers `m,n >= 3` and `m+n >= 8`;
2. the source definition `TGr_{m,n}=C_m square C_n`;
3. the word-representation condition, with alternation if and only if adjacency;
4. the requirement that a 3-word representation contains exactly three copies of every vertex;
5. independent reconstruction of the 15-vertex, 30-edge graph `TGr_{3,5}`;
6. the length-45 word recorded in this public certificate;
7. all `binom(15,2)=105` unordered vertex pairs; and
8. the logical consequence `R(TGr_{3,5}) <= 3`, contradicting the printed lower bound.

The verifier confirmed that the displayed word is a complete counterexample to
the printed Conjecture 1, not a cylindric-grid certificate and not a
classification of other toroidal grids.

## Executable Reproduction

Run:

```bash
python cases/toroidal-grid-representation-counterexample/check_counterexample.py
```

The checker uses only the Python standard library. It rebuilds
`TGr_{3,5}=C_3 square C_5`, verifies the certificate's vertex and edge sets,
checks that the word is 3-uniform, and tests alternation for every unordered
vertex pair.

The compact output is recorded in
[verification_summary.json](verification_summary.json).

## Scope Checks

- The result is recorded as `COUNTEREXAMPLE`.
- The claim is limited to `TGr_{3,5}`.
- The exact printed Conjecture 1 is stated as disproved because it quantifies over all `m,n >= 3` with `m+n >= 8`.
- The case does not claim public priority, first discovery, or novelty.
