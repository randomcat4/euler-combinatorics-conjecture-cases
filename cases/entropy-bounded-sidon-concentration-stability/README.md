# Entropy-Bounded Sidon Concentration Stability

*Rupert Li, Lampros Gavalakis, and Ioannis Kontoyiannis · [DOI](https://doi.org/10.1109/TIT.2026.3653549) · [arXiv](https://arxiv.org/abs/2506.20813v2)*

This case gives a complete solution to the unnumbered open problem in Section 5
of Li, Gavalakis, and Kontoyiannis, *Entropic additive energy and entropy
inequalities for sums and products*. The source asks whether the
minimum-atom dependence in Proposition 5.2 can be replaced by a function of
only the defect `C` and the entropy bound `D`.

The public result proves that the following explicit function suffices:

```text
f(0,D) = 0,
f(C,D) = min{1, 2D/log(1/C) + sqrt(C)/log 2}  for 0<C<1,
f(C,D) = 1                                         for C>=1.
```

For every fixed finite `D`, this function tends to `0` as `C` tends to `0`.

## Contents

- [problem.md](problem.md) states the original source problem and the exact
  public scope.
- [proof.md](proof.md) gives the self-contained proof.
- [verification.md](verification.md) records the independent mathematical
  verification and the finite-probe boundary.
- [status.md](status.md) separates correctness, completeness, priority, and
  publication state.
- [sources.md](sources.md) gives the public source citations.
- [check_sidon_stability.py](check_sidon_stability.py) checks the public
  certificate and runs finite sanity probes.
- [verification_summary.json](verification_summary.json) records the curated
  release certificate.

## Scope of the Claim

The proof covers arbitrary discrete random variables of finite entropy on
arbitrary abelian groups, with no finite-support, minimum-atom, moment, or group
structure hypothesis beyond those stated in [problem.md](problem.md).

The release does not claim that the displayed function is optimal. It does not
claim public priority.
