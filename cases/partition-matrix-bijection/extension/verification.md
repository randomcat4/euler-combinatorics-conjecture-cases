# Verification

The [proof manuscript](../paper/extension.pdf) supplies the general argument. The independent checker supplies the finite evidence described below; it does not prove the all-parameter theorem by enumeration.

## Reproduce

Run from this directory with Python 3.12:

```sh
python check.py
```

The script regenerates [results.json](results.json). Its mathematical implementation was written in a fresh context from the manuscript, without access to the author's checker, prior outputs, or previous reviews.

## Actual coverage

Exact independent enumeration of improper matrices, restricted inversion sequences, and cyclic set partitions for sizes 1 through 8. Both encoders and both inverses cover the full target; the minus restriction, dimension, complete ordered parity signature, Eulerian coefficients, terminal binomial counts, and Stirling totals are checked.

All reported checks passed within this stated range. The arithmetic used and any numerical tolerances are identified explicitly above. The machine-readable output gives the individual cases and tolerances.

## General proof review

A separate fresh-context adversarial model review examined the first-smaller insertion anchor, circular wraparound, the inversion-sequence inverse, and the full ordered-signature enumeration. It reported no unresolved logical defect in the supplied argument. This review was independent of the implementation and finite results. The checking and proof-review requests used GPT-5.6 Sol at high and xhigh reasoning, respectively; these are requested configurations, not separately measured runtime identities.

Finite checking and model review do not constitute a formal proof-assistant certificate, human domain review, or a novelty determination. The original public package remains available separately.

Reviewed PDF SHA-256: `ea708f8d316177ffb0dcb20e47037f7539b87520eafd3302fb1a72a63ef098d0`.
