# Reproduction guide

The commands below reproduce the initial-pass checks. Total runtime depends on the selected case and machine; the complete suite is not a guaranteed 60-second run.

```bash
git clone https://github.com/randomcat4/euler-combinatorics-conjecture-cases.git
cd euler-combinatorics-conjecture-cases
python scripts/validate_repo.py
python cases/zhao-restricted-zero-sum-counterexample/check_counterexample.py
python cases/k33plus-q-index-boundary-counterexample/check_counterexample.py
python cases/toroidal-grid-representation-counterexample/check_counterexample.py
python cases/path-set-tree-representation-counterexample/check_counterexample.py
python cases/f29-inducibility-recursive-graphon-counterexample/check_counterexample.py
python cases/minimal-degree-three-imprimitive-groups/check_quotient_criterion.py
python cases/steklov-three-leaf-extra-special-extremizer/check_three_leaf_extremizer.py
python cases/minimum-degree-two-degree-multiplicity/check_sharpness.py
python cases/five-point-sixteen-shattering/check_crossing_obstruction.py
python cases/orthogonal-tree-seven-vertex-obstructions/check_counterexamples.py
python cases/catalan-schett-plane-tree-statistic/check_small_cases.py
python cases/partition-matrix-bijection/verify_bijection.py
python cases/partition-matrix-q-sum-product/check_formula.py
python cases/cdk-improper-partition-matrix-image/mine_cdk_image.py --n-max 8 --check cases/cdk-improper-partition-matrix-image/mining_n_le_8.json
python cases/ternary-berge-suspension-rigidity/check_statement_certificate.py
python cases/entropy-bounded-sidon-concentration-stability/check_sidon_stability.py
```

The initial-pass checks above use the Python standard library and verify the repository boundary,
the published artifact manifest, and the executable finite certificates. Each new extension package
has its own reproduction instructions and recorded coverage; spectral checks list their additional
dependencies and numerical tolerances.


## Current extension checks

- [catalan-schett-plane-tree-statistic](../cases/catalan-schett-plane-tree-statistic/extension/verification.md)
- [cayley-eigenvalue-codimension-three](../cases/cayley-eigenvalue-codimension-three/extension/verification.md)
- [cdk-improper-partition-matrix-image](../cases/cdk-improper-partition-matrix-image/extension/verification.md)
- [k33plus-q-index-boundary-counterexample](../cases/k33plus-q-index-boundary-counterexample/extension/verification.md)
- [minimal-degree-three-imprimitive-groups](../cases/minimal-degree-three-imprimitive-groups/extension/verification.md)
- [partition-matrix-bijection](../cases/partition-matrix-bijection/extension/verification.md)
- [partition-matrix-q-sum-product](../cases/partition-matrix-q-sum-product/extension/verification.md)
- [steklov-three-leaf-extra-special-extremizer](../cases/steklov-three-leaf-extra-special-extremizer/extension/verification.md)


## New case submissions

- [Subgroup normality and Cayley integrality](../cases/subgroup-cayley-integrality/verification.md)
- [Local connectivity of star friends-and-strangers graphs](../cases/star-friends-and-strangers-local-connectivity/verification.md)
- [A distinct-shape Hadamard dual Jacobi--Trudi counterexample](../cases/dual-jacobi-trudi-hadamard-counterexample/verification.md)
