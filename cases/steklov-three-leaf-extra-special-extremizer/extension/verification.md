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

All nonisomorphic trees on 2 through 12 vertices are enumerated. At r=1 the matching threshold selects 5, 22, and 19 trees with 2, 3, and 4 leaves. Equality occurs only at the expected candidates. Matching numbers use exact tree dynamic programming; Steklov eigenvalues are cross-checked using both a Schur complement and the leaf-current energy form. Formula checks cover 45 ordered central splits with 2 through 6 leaves and r=1 through 3. Spectral tolerance is 2e-8; these eigenvalue comparisons are numerical.

All reported checks passed within this stated range. The arithmetic used and any numerical tolerances are identified explicitly above. The machine-readable output gives the individual cases and tolerances.

## General proof review

A separate fresh-context adversarial model review examined the matching-cover diameter bound, rigidity at minimum diameter, the same-sign maximizer argument, the rank-three Gram calculation, and all equality cases. It reported no unresolved logical defect in the supplied argument. This review was independent of the implementation and finite results. The checking and proof-review requests used GPT-5.6 Sol at high and xhigh reasoning, respectively; these are requested configurations, not separately measured runtime identities.

Finite checking and model review do not constitute a formal proof-assistant certificate, human domain review, or a novelty determination. The original public package remains available separately.

Reviewed PDF SHA-256: `927c1e39f1a9afad82c768acdc295a2bcd470190cd068c955b5f9d07f4423672`.
