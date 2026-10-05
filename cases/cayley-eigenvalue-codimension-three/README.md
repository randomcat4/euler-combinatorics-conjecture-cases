# Representation-Level Uniqueness for Support-Constrained Cycle Walks

*Yuxuan Li, Binzhou Xia, and Sanming Zhou · [DOI](https://doi.org/10.1016/j.jcta.2025.106097) · [arXiv](https://arxiv.org/abs/2402.02427)*

This case records a proof of Conjecture 4.7 in Li, Xia, and Zhou,
*The Second Largest Eigenvalue of Some Nonnormal Cayley Graphs on Symmetric
Groups*.

For every `n>=5` and `1<=r<k<=n-2`, let `C(n,k;r)` be the set of `k`-cycles
whose support contains `{1,...,r}`. The relevant eigenvalue was already known:
the new conclusion is the exact classification of the irreducible blocks that
attain it. When `k` is even, only the standard representation attains the
second eigenvalue. When `k` is odd, exactly the standard representation and
its sign twist attain the strictly second eigenvalue.

The [seven-page full proof](paper/full_conjecture.pdf) makes the
published induction strict by proving the missing endpoint `r=k-1`, then
handles the exceptional `k=n-2` layer using the published boundary results and
three finite exact cases. The earlier nine-page note and its source remain in
the package as an independently reviewed proof of the `n-k=3` slice.

The [companion case files](extension/) give the original problem, proof guide,
source-theorem map, exact verification range and a self-contained checker.
The three finite proof inputs now have public rational characteristic
polynomials, threshold multiplicities and Sturm root counts.

## Contents

- `problem.md` states Conjecture 4.7 and the resolved parameter range.
- `proof_outline.md` records the dependency graph and the finite-computation
  boundary of the full proof.
- `status.md` separates correctness, external review, and priority.
- `sources.md` identifies the public primary sources.
- `verification.md` records the completed audit and its limitations.
- `monotone_orbit_cones.md` states the closed three-cycle and two-/three-marked
  four-cycle classifications; `coneproof.md` gives the complete analytic proofs.
- `checkcone.py` rebuilds the symbolic content patterns and exact six-point
  boundary from representation matrices; it uses the SymPy dependency listed
  in `extension/requirements.txt`.
- `check_monotone_cones.py` checks the stored finite boundary summaries.
- `product_activity.md` states two structured product-activity families.
- `activityproof.md` gives their complete branching and parameter-regime proofs,
  including the standard quotient formula and target simplicity.
- `weighted_positive_cone.md` proves a support-weighted extension with an
  exact hypergraph-component formula for the standard top space.
- `check_weighted_positive_cone.py` checks representative component formulas
  in exact arithmetic using only the Python standard library.
- `paper/full_conjecture.pdf` is the complete seven-page proof.
- `extension/check.py` and `extension/results.json` reproduce the exact
  three-case boundary verification; `extension/requirements.txt` lists dependencies.
- `paper/main.tex` and `paper/main.pdf` are the earlier `n-k=3` note.
- `evidence/low_order_cases.json` contains the exact certificates for that
  earlier slice.

## Scope and priority

The primary mathematical statement covers the full range of Conjecture 4.7,
and the weighted extension records a positive-cone consequence. The case does
not address the different `k=n-1` questions in the source paper. The full
proof and its inputs have undergone LLM re-review. Initial human review is
recorded in the shared review statement below; a completed specialist referee
process is not claimed. No research-credit or priority claim is made.

## Review and reuse

These proofs were generated autonomously by EULER and are released under the
[MIT License](../../LICENSE), with research-credit and priority claims waived.
The [review record](../../docs/provenance.md) describes Sol High and Opus 4.8
xhigh re-review, initial human review by the author and doctoral students at
ETH Zürich and Peking University, and the invitation to specialists for
preliminary counterexample review. Mathematical and computational scope is
stated separately in this package.
