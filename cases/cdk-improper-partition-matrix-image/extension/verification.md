# Verification

The [proof manuscript](../paper/extension.pdf) supplies the general argument. The independent checker supplies the finite evidence described below; it does not prove the all-parameter theorem by enumeration.

## Reproduce

Run from this directory with Python 3.12:

```sh
python check.py
```

The script regenerates [results.json](results.json). Its mathematical implementation was written in a fresh context from the manuscript, without access to the author's checker, prior outputs, or previous reviews.

## Actual coverage

Exact integer enumeration of all inversion sequences for sizes 1 through 8 (up to 40,320 objects at size 8). The checker reconstructs the matrices, checks the CDK round trip, every pair-swap orbit, all cell cardinalities, the binomial orientation distribution, and the inclusion-exclusion polynomial for every column-size composition.

All reported checks passed within this stated range. The arithmetic used and any numerical tolerances are identified explicitly above. The machine-readable output gives the individual cases and tolerances.

## General proof review

A separate fresh-context adversarial model review examined intrinsic interval boundaries, independent pair swaps, preservation of nonempty rows, and the orbit inclusion-exclusion formula. It reported no unresolved logical defect in the supplied argument. This review was independent of the implementation and finite results. The checking and proof-review requests used GPT-5.6 Sol at high and xhigh reasoning, respectively; these are requested configurations, not separately measured runtime identities.

Finite checking and model review do not constitute a formal proof-assistant certificate, human domain review, or a novelty determination. The original public package remains available separately.

Reviewed PDF SHA-256: `cc4cd69c52774fa64643478946f94adb5dbd0f7bc08fccf0c82ce7a91f1dcdd0`.
