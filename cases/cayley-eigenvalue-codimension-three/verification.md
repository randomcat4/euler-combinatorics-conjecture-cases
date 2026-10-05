# Verification

## Full Conjecture 4.7 proof

The seven-page proof was audited line by line against the cited Li--Xia--Zhou
paper. The audit checked:

- the representation-wise strict induction and its recurrence;
- the `r=k-1` endpoint induction and the equality condition in Weyl's
  inequality;
- the branching reduction to `(N-2,2)` and `(N-2,1,1)` and their sign twists;
- the two-subset and exterior-square zero-intersection models;
- the parity split and all ranges of the cited `k=n-1` and `k=n-2` results;
- the direct Jucys--Murphy arguments for `k=2,3`; and
- the three finite cases required at `n=6,7`.

Independent numerical diagnostics reconstructed the full regular matrices for
the two `S_6` cases and all Young-orthogonal blocks for the `S_7` case. They
reproduced degrees `60,36,360`, target values `18,16,84`, and target-block
multiplicities `4,3,5`. These floating-point diagnostics are checks, not the
exact certificates used by the proof draft.

The current update supplies a fresh independent [exact implementation](extension/check.py)
and [complete block results](extension/results.json). Rational Young seminormal
generators, Coxeter relations, transposition characters, characteristic
polynomials, threshold multiplicities and Sturm root counts are checked for
every partition in all three cases. Orthogonal-model floating-point spectra
remain a separate cross-check. See the [reproduction instructions](extension/verification.md).

A separate adversarial model review examined the general proof, the finite
implementation and the exact ranges of the [published inputs](extension/sources.md).
The historical repository gate `INTERNALLY_AUDITED` is retained: model review
does not constitute a fresh human domain-expert referee report. The former
missing-implementation condition has been addressed.

## Earlier `n-k=3` note

The earlier note was independently reviewed mathematically and at paper level.
Its 29 load-bearing low-order blocks were recomputed in exact arithmetic. That
verification remains valid for the restricted slice and is recorded in
`evidence/low_order_cases.json`.

## Boundary

Verification of correctness does not establish novelty or priority. The case
does not claim any result for the separate `k=n-1` problems.

## Weighted positive-cone extension

The extension proof was audited separately at the fixed-space, parity, and
multiplicity steps. A dependency-free exact checker tests seven configurations
for `k=3,4`, including overlapping local hyperedges, components killed by a
proper hard constraint, and a configuration in which local hyperedges cover
all vertices. In every case the direct target-eigenspace nullity equals both
the constraint-space nullity and the predicted `c-1`.

## Product-activity extensions

The two structured families have complete analytic proofs in `activityproof.md`.
The one-exceptional family uses normal-class bounds and one-step branching.
The two-exceptional three-cycle family includes explicit one- and two-path
matrices, strict comparisons in all three parameter regimes, and the standard
quotient calculation. The complete proof received independent mathematical
review, including the zero mixing coefficient and the reflected regime's
single-path estimates. No finite no-hit scan is used as proof.

## Closed monotone orbit cones

The complete analytic proofs in `coneproof.md` include the content estimates,
strict endpoint comparisons, stable-pattern coverage for arbitrary order, and
embedded-degree exclusions. The final proof received independent mathematical
review. `checkcone.py` independently rebuilds the 44 symbolic low-tail patterns
and the complete rational six-point boundary; it checks the representation
relations and exact Sturm root bounds. The older `check_monotone_cones.py`
only checks the stored finite summary data. General validity comes from the
analytic reductions and coverage proof, rather than finite scanning.
