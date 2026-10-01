# Verification

The [proof manuscript](../paper/extension.pdf) supplies the general argument. The independent checker supplies the finite evidence described below; it does not prove the all-parameter theorem by enumeration.

## Reproduce

Run from this directory with Python 3.12:

```sh
python check.py
```

The script regenerates [results.json](results.json). Its mathematical implementation was written in a fresh context from the manuscript, without access to the author's checker, prior outputs, or previous reviews.

## Actual coverage

Exact enumeration of all rooted plane trees and all permutations directly filtered for 231 avoidance, for 0 through 9 edges. Both sides have identical complete ordered inverse-run signatures; cut inverses, the original joint statistics, and weight specializations including zero and negative weights are checked.

All reported checks passed within this stated range. The arithmetic used and any numerical tolerances are identified explicitly above. The machine-readable output gives the individual cases and tolerances.

## General proof review

A separate fresh-context adversarial model review examined the inverse of the tree cut, the complete inverse-run recursion, omitted first-run weights (including zero weights), and formal-series uniqueness. It reported no unresolved logical defect in the supplied argument. This review was independent of the implementation and finite results. The checking and proof-review requests used GPT-5.6 Sol at high and xhigh reasoning, respectively; these are requested configurations, not separately measured runtime identities.

Finite checking and model review do not constitute a formal proof-assistant certificate, human domain review, or a novelty determination. The original public package remains available separately.

Reviewed PDF SHA-256: `13f9114aa9ab03fce811750ea51937caacb116fb47931125fb7f5f80898d583c`.
