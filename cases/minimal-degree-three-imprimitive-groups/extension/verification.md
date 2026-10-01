# Verification

The [proof manuscript](../paper/extension.pdf) supplies the general argument. The independent checker supplies the finite evidence described below; it does not prove the all-parameter theorem by enumeration.

## Reproduce

Run from this directory with Python 3.12:

```sh
python check.py
```

The script regenerates [results.json](results.json). Its mathematical implementation was written in a fresh context from the manuscript, without access to the author's checker, prior outputs, or previous reviews.

## Actual coverage

Exact binary linear algebra for every cyclic code of lengths 1 through 12: norm-kernel/coboundary quotients, multiplier orbits, and the Burnside formula. The class counts are 1, 3, 3, 7, 3, 11, 5, 15, 7, 11, 3, 39. Code-lattice closure is additionally checked through length 10.

All reported checks passed within this stated range. The arithmetic used and any numerical tolerances are identified explicitly above. The machine-readable output gives the individual cases and tolerances.

## General proof review

A separate fresh-context adversarial model review examined intrinsic alternating blocks, recovery of code/cocycle data, the full conjugacy criterion, cyclic primary decomposition, and multiplier equivalence. It reported no unresolved logical defect in the supplied argument. This review was independent of the implementation and finite results. The checking and proof-review requests used GPT-5.6 Sol at high and xhigh reasoning, respectively; these are requested configurations, not separately measured runtime identities.

Finite checking and model review do not constitute a formal proof-assistant certificate, human domain review, or a novelty determination. The original public package remains available separately.

Reviewed PDF SHA-256: `c21a5c0371cbe47cc3736d9ae3bfd0609b8213584b4aafa49f33430348b81080`.
