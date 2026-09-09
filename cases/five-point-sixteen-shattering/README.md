# Five-Point Sixteen-Shattering Permutation Families

This case records the complete `k=5` parameter slice of the partially
shattering permutation-family conjecture of Girao--Michel--Tamitegama.

## Result

For every integer `n>=5`, there is a family of permutations of `[n]`, chosen
before any five-element subset is tested, that induces at least 16 distinct
relative orders on every five-element subset and has size

```text
O(sqrt(log n * log log n)).
```

Consequently, for every fixed `1<=t<=16`,

```text
f_5(n,t) = o(log n).
```

This proves the complete `k=5` slice of Conjecture 4.2. It does not prove the
conjecture for general `k`, determine the exact growth rate, or remove the
remaining `sqrt(log log n)` gap for `13<=t<=16`.

## Public Status

- Result type: `PARTIAL_RESULT`.
- Correctness: `PROVED` for the stated `k=5` slice.
- Verification: `INDEPENDENTLY_VERIFIED` by two fresh mathematical reviews
  of the same fixed theorem and proof.
- Formalization: `LEAN_PARTIALLY_CHECKED` for one isolated crossing lemma
  only; the theorem itself is not formally verified.
- Novelty and public priority: `NOT_ESTABLISHED`.

## Files

- [problem.md](problem.md) states the source conjecture and exact released
  scope.
- [proof.md](proof.md) gives the complete analytic construction and proof.
- [check_crossing_obstruction.py](check_crossing_obstruction.py) exhaustively
  checks the four-point crossing lemma used in the proof.
- [verification.md](verification.md) records the independent verification and
  computation boundary.
- [sources.md](sources.md) gives public source locators and attribution.
