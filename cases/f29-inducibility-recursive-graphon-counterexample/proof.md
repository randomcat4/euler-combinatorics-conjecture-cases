# Proof

Let `F29=(6,{03,04,13,15,45})`. Its automorphism group has order `10`, hence
the source normalization gives

```text
p(F29,W)=72*t(F29,W).
```

Consider the equal-measure six-part recursive graphon pattern

```text
off=010100000100101;diag=RRRRRR.
```

With the pair-order convention from [problem.md](problem.md), its off-diagonal
one-cells are

```text
01,03,12,25,35.
```

All six diagonal cells are recursive copies of the whole graphon.

For any induced subgraph `H` of `F29`, let `t_H` be its labelled induced density
in this recursive graphon. Sampling the vertices of `H` independently from the
six top-level parts gives a finite sum over `6^|V(H)|` part assignments. Each
assignment either

1. violates an off-diagonal adjacency or non-adjacency condition and contributes `0`;
2. contributes a product of already determined densities for smaller induced subgraphs; or
3. puts all vertices into one recursive diagonal part and contributes `t_H`.

Applying this recurrence to the full graph `F29` gives the exact equation

```text
t(F29,W) = (7790/777 + 6*t(F29,W)) / 6^6.
```

Solving,

```text
t(F29,W)=779/3624705.
```

Therefore

```text
p(F29,W)=72*t(F29,W)=6232/402745.
```

The conjectured value is

```text
24/1555 = 6216/402745.
```

Thus

```text
p(F29,W)-24/1555 = 16/402745 > 0.
```

The displayed graphon is a valid graphon under the source recursive
construction convention, so Conjecture 4.7's equality `lambda_F29 = 24/1555`
is false.

The executable checker independently recomputes the automorphism count and the
recursive density equations from the graph and graphon codes in
[counterexample_certificate.json](counterexample_certificate.json).
