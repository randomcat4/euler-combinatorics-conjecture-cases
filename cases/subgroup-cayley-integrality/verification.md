# Verification and reproduction

Independent mathematical reviews returned CORRECT for the universal proof. The final review checked the original source contract, detecting coset constituent, genuine adjacency block, dimension bound with its trivial constituent, every unbounded square-gap branch, both exceptional parameter triples, and the normal-subgroup sufficiency theorem.

From the repository root, run:

```bash
python cases/subgroup-cayley-integrality/check.py
```

This standard-library check evaluates all 25,074,750 tuples with `2 <= d <= 500`, `1 <= r < d` and `dr+1 <= ell <= dr+201`, and four explicit Cayley adjacency certificates. The script uses `k` for the index `ell` in the proof. It writes `certificates.json` next to the script. These are supporting checks; the proof does not infer a universal theorem from them.

`arithmetic.lean` checks only the integer identity, the consecutive-square lemma, and the two exceptional square brackets. This source compiled using Lean 4.32.0 with Mathlib. Its axiom dependencies are only propext, Classical.choice and Quot.sound; there is no sorry/admit/custom axiom. Representation theory, the full parameter gap derivation and the graph theorem are not formalized. Status: `LEAN_PARTIALLY_CHECKED`.

Maintainer mathematical review of this submission is complete. The source paper's Theorem 3.1 provides normal-subgroup sufficiency; the new proof establishes necessity on its entire intended domain.
