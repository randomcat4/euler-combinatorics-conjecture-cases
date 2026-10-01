# Verification

The [proof manuscript](../paper/extension.pdf) supplies the general argument. The independent checker supplies the finite evidence described below; it does not prove the all-parameter theorem by enumeration.

## Reproduce

Run from this directory with Python 3.12:

```sh
python check.py
```

The script regenerates [results.json](results.json). Its mathematical implementation was written in a fresh context from the manuscript, without access to the author's checker, prior outputs, or previous reviews.

## Actual coverage

Exact direct enumeration of every partition matrix through size 8 is compared coefficient by coefficient in q with the independently generated column-series sum-product. Three cell-weight families include zero and signed weights. The q=0 and q=1 specializations are checked, and q-Borel coefficients through degree 8 are checked with exact fractions for q=1/2,2/3 and k<=5. Separately, decimal evaluations compare the word series and a 400-term basic-hypergeometric expression for k=1 through 4 at (q,t)=(0.2,0.03),(0.45,0.015); the script records discrepancies and a word-series tail bound. These last comparisons are numerical consistency tests, not an all-parameter analytic proof.

All reported checks passed within this stated range. The arithmetic used and any numerical tolerances are identified explicitly above. The machine-readable output gives the individual cases and tolerances.

## General proof review

A separate fresh-context adversarial model review examined row deletion, the formal sum-product, the q-Borel identity, convergence for each fixed column factor, and arbitrary cell weights. It reported no unresolved logical defect in the supplied argument. This review was independent of the implementation and finite results. The checking and proof-review requests used GPT-5.6 Sol at high and xhigh reasoning, respectively; these are requested configurations, not separately measured runtime identities.

Finite checking and model review do not constitute a formal proof-assistant certificate, human domain review, or a novelty determination. The original public package remains available separately.

Reviewed PDF SHA-256: `e4909c197b2f309787e7f10f1593ab4ae785223ce3610e7659134812ef73525b`.
