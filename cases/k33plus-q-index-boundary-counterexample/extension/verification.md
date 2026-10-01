# Verification

The [proof manuscript](../paper/extension.pdf) supplies the general argument. The independent checker supplies the finite evidence described below; it does not prove the all-parameter theorem by enumeration.

## Reproduce

Run from this directory with Python 3.12:

```sh
python -m pip install -r requirements.txt
python check.py
```

The script regenerates [results.json](results.json). Its mathematical implementation was written in a fresh context from the manuscript, without access to the author's checker, prior outputs, or previous reviews.

## Actual coverage

Exact forbidden-subgraph tests on all 32,768 labelled six-vertex graphs find 32,237 feasible graphs. Float64 spectral comparisons find 60 labelled maximizers, one isomorphism type, with Q-index 5+sqrt(13). The next value is about 8.44949, separated by about 0.15606. Every residual graph in the two-universal-vertex class is also checked for orders 5 through 8. Spectral tolerance is 1e-9; this is not an exact spectral certificate.

All reported checks passed within this stated range. The arithmetic used and any numerical tolerances are identified explicitly above. The machine-readable output gives the individual cases and tolerances.

## General proof review

A separate fresh-context adversarial model review examined the analytic six-vertex complement argument, the forbidden-subgraph criterion for joins, sharp equality throughout that class, and the infinite-order obstruction. It reported no unresolved logical defect in the supplied argument. This review was independent of the implementation and finite results. The checking and proof-review requests used GPT-5.6 Sol at high and xhigh reasoning, respectively; these are requested configurations, not separately measured runtime identities.

Finite checking and model review do not constitute a formal proof-assistant certificate, human domain review, or a novelty determination. The original public package remains available separately.

Reviewed PDF SHA-256: `862d78503263063778398dd51caf25b86b7d81f02fd1792fd757cc6da136d958`.
