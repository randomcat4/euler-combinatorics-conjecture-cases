# Proof

Let `TGr_{3,5}` have vertices

```text
x11, x21, x31, x12, x22, x32, x13, x23, x33, x14, x24, x34, x15, x25, x35.
```

Its edges are the three edges in each `C_3` column and the five-cycle edges in
each row. Equivalently, the 30 edges are recorded in
[word_certificate.json](word_certificate.json).

Consider the word

```text
x11 x13 x22 x21 x32 x31 x12 x23 x22 x33 x32 x14 x13 x24 x23
x15 x34 x14 x33 x25 x24 x35 x34 x11 x15 x12 x13 x21 x22 x31
x11 x14 x23 x32 x12 x25 x21 x35 x15 x24 x33 x25 x34 x31 x35
```

It has length 45, and every one of the 15 vertices appears exactly three times.

For each unordered pair `{a,b}`, project the word to the symbols `a` and `b`.
Since the word is 3-uniform, each projected pair-word has length 6. Direct
inspection of the finite certificate gives the following complete counts:

```text
unordered vertex pairs:       105
edges:                         30
nonedges:                      75
edge pairs alternating:         30
nonedge pairs alternating:       0
mismatches:                     0
```

Thus two symbols alternate in the word if and only if the corresponding
vertices are adjacent in `TGr_{3,5}`. By the definition of word representation,
the displayed word is a 3-word representation of `TGr_{3,5}`.

Therefore `R(TGr_{3,5}) <= 3`. The source conjecture asserts
`R(TGr_{m,n}) >= 4` for every `m,n >= 3` with `m+n >= 8`; the pair `(3,5)`
satisfies those hypotheses. Hence Conjecture 1 is false as printed.

The executable checker recomputes the full 105-pair table from the graph
definition and the displayed word. The SAT search that found the word is not
used as a proof step.
