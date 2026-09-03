# Minimum-Degree-Two Degree Multiplicity

This case records a complete `delta(G)=2` slice of the degree-multiplicity
problem of Alon--Wei, in the equivalent formulation stated by Ma--Xie.

## Result

Let `G` be a finite simple graph on `n>=3` vertices with minimum degree
`delta(G)=2`. For a spanning subgraph `H` of `G`, write

```text
m(H,j) = |{v in V(G) : deg_H(v)=j}|.
```

Then there is a spanning subgraph `H` such that, for every integer `j>=0`,

```text
m(H,j) <= floor(n/3) + 2.
```

This is a partial result for the general minimum-degree conjecture: it proves
the complete minimum-degree-two slice, but it does not prove the stronger
bound required when `delta(G)>2`.

The disjoint union `2C4` of two four-cycles attains the integer bound:
every spanning subgraph has some degree class of size at least `4`, and
`floor(8/3)+2=4`.

## Public Status

- Result type: `PARTIAL_RESULT`.
- Correctness: `PROVED` for the stated `delta(G)=2` slice.
- Verification: `INDEPENDENTLY_VERIFIED` by two fresh mathematical reviews of
  the fixed proof package.
- Sharpness: the integer bound is attained by `2C4`.
- Novelty and public priority: `NOT_ESTABLISHED`.

## Files

- [problem.md](problem.md) states the source question, released theorem, and
  scope boundary.
- [proof.md](proof.md) gives the public proof.
- [check_sharpness.py](check_sharpness.py) exhaustively checks the `2C4`
  sharpness certificate.
- [verification.md](verification.md) records the independent verification
  boundary.
- [sources.md](sources.md) gives public source locators.
