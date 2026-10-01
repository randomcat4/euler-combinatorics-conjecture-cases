# Verification

The [manuscript](../paper/full_conjecture.pdf) separates the published eigenvalue bound, the general uniqueness argument, and three load-bearing finite inputs. This companion package supplies a fresh, self-contained exact implementation for those inputs.

## Reproduce

Run in this directory with Python 3.12:

```sh
python -m pip install -r requirements.txt
python check.py
```

This regenerates [results.json](results.json). The implementation was written from the manuscript in a fresh context, without reading the author's code, earlier checkers, or earlier reviews. It needs no private files or manuscript source.

## Exact finite results

| (n,k,r) | Degree | Threshold | Attaining partitions | Multiplicity in each block |
|---|---:|---:|---|---:|
| (6,4,1) | 60 | 18 | (5,1) | 4 |
| (6,4,2) | 36 | 16 | (5,1) | 3 |
| (7,5,1) | 360 | 84 | (6,1), (2,1,1,1,1,1) | 5 |

For every partition of n, the checker enumerates standard tableaux, checks the hook dimension, constructs rational Young seminormal generators, and checks the Coxeter relations and transposition character exactly. It enumerates the required cycles and their adjacent-transposition words, forms the connection sum over the rationals, and computes its characteristic polynomial.

The exact threshold factor is removed with its full multiplicity before a Sturm root count on the remaining polynomial above that threshold. Every non-degree block has zero roots above the threshold; only the displayed target blocks have positive threshold multiplicity. Degree blocks mean the trivial representation for even k, and the trivial and sign representations for odd k. The JSON records each polynomial, factorization, multiplicity, and root count, including the deliberately excluded degree blocks.

A separately constructed Young orthogonal model gives float64 eigenvalues as a cross-check, with tolerance 2e-8. The exact certification relies on the rational branch, not on those numerical values. The four additional regression rows quoted from the old proof draft are historical data and are not part of this new three-case run.

## Proof and input review

A separate adversarial model review examined the general strictness and branching argument. Its original finite-input condition is addressed by the implementation above. The cited non-strict bound and boundary uniqueness theorems have also been checked against the source paper; precise theorem locations are listed in [sources.md](sources.md).

The same separate reviewer replayed the public implementation and checked the cycle enumeration, permutation-composition convention, complete irreducible coverage, representation identification, sign twists, degree-block exclusions and Sturm endpoint treatment. No unresolved implementation defect was reported.

The finite-check request used GPT-5.6 Sol with high reasoning; the separate proof/input review used xhigh reasoning. These are requested configurations, not independently measured runtime identities. Human domain review, proof-assistant formalization, and public priority are not established by these checks.

PDF SHA-256: `4f2afed176da116cf8c01b7c8d7e60e290d391476d7375a254fbe61d1dfdae6d`.
