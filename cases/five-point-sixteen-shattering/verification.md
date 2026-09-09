# Verification

## Mathematical Review

Two fresh, mutually independent, read-only mathematical reviews checked the
same fixed theorem and complete proof. Both returned `CORRECT`.

Their checks covered:

1. the quantifier order: one family is chosen for each `n` before the tested
   five-set is known;
2. the two finite covering lemmas and their logarithmic family sizes;
3. preservation of every original first-difference coordinate after
   projection, including arbitrary redundant nonconstant coordinates;
4. the complete classification of five-point lexicographic restrictions
   having fewer than 16 orders;
5. use of actual binary values rather than rank-compressed substitutes;
6. simultaneous realization of primary-bit and fallback signs by one
   four-position cover;
7. disjointness and distinctness in the `8+8` and `12+4` cases;
8. all rounding, embedding, and small-`n` boundaries in the final size bound.

The reviews did not use the author's finite row tables as evidence for the
universal theorem. One isolated crossing-partition lemma was also checked in
Lean, but that partial formal check is not a formalization of the construction
or theorem.

The independently reviewed paper exposition was checked separately. That
paper-level review is useful publication evidence, but it is not being used as
a substitute for the two mathematical reviews above.

## Executable Check

Run:

```bash
python cases/five-point-sixteen-shattering/check_crossing_obstruction.py
```

Expected result:

```text
PASS: four-point crossing obstruction verified
```

The script exhausts all 24 orders of four labeled points and verifies that no
order separates both crossing `2+2` partitions. This is a transparent sanity
check of one proof component. The general theorem is established by
[proof.md](proof.md).
