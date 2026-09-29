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

The seven-page full proof is in `paper/full_conjecture.pdf`. It makes the
published induction strict by proving the missing endpoint `r=k-1`, then
handles the exceptional `k=n-2` layer using the published boundary results and
three finite exact cases. The earlier nine-page note and its source remain in
the package as an independently reviewed proof of the `n-k=3` slice.

## Contents

- `problem.md` states Conjecture 4.7 and the resolved parameter range.
- `proof_outline.md` records the dependency graph and the finite-computation
  boundary of the full proof.
- `status.md` separates correctness, external review, and priority.
- `sources.md` identifies the public primary sources.
- `verification.md` records the completed audit and its limitations.
- `monotone_orbit_cones.md` records the closed monotone three-cycle cone and
  the complete two- and three-marked four-cycle cones.
- `check_monotone_cones.py` checks the exact finite boundary certificates.
- `paper/full_conjecture.pdf` is the complete seven-page proof.
- `paper/main.tex` and `paper/main.pdf` are the earlier `n-k=3` note.
- `evidence/low_order_cases.json` contains the exact certificates for that
  earlier slice.

## Scope and priority

The mathematical statement covers the full range of Conjecture 4.7. It does
not address the different `k=n-1` questions in the source paper. The full
proof has passed a detailed internal audit, but has not yet been independently
refereed by a domain expert. Public novelty or priority is `NOT_ESTABLISHED`.
