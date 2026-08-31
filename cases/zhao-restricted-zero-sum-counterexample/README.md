# Counterexamples to Zhao's short zero-sum conjectures

*Kevin Zhao · [arXiv:2506.21383](https://arxiv.org/abs/2506.21383)*

This package records independently checked counterexamples and exact-value consequences around the short zero-sum conjectures in Kevin Zhao's paper *On zero-sum subsequences in a finite abelian group of length not exceeding a given number*.

## Result

The released claims are limited to the following statements.

- Conjecture 6.1 is disproved by `C_2 direct-sum C_4^3`: the displayed length-12 sequence has no zero-sum occurrence-subsequence of length at most 9, and the cited source gives the matching upper bound `s_{\leq 9}=13`.
- Conjecture 6.2's upper branch is disproved by an infinite family `C_n^4` for every prime-power `n>=2`.
- Conjecture 6.2's upper branch is also refuted by the finite witnesses `C_2^2 direct-sum C_4^2` and `C_2^12`.
- Conjecture 6.2's lower branch is refuted at `C_2^7`, where `s_{\leq 4}(C_2^7)=12`.
- Conjecture 6.4's lower branch is refuted at `C_2^7`, using Sidorenko's exact value `s_4(C_2^7)=15`.
- Conjecture 1.2 has a supplemental even-rank counterexample in `C_2^8`; this is not presented as a priority claim because the cited paper already notes other failures of that conjecture.

The package does not claim that every conjecture in the source paper is false, and it does not claim public priority.

## Evidence

- [`problem.md`](problem.md) records the source statements and the exact released scope.
- [`proof.md`](proof.md) gives the symbolic arguments, finite witnesses, and exact-value reductions.
- [`check_counterexample.py`](check_counterexample.py) independently enumerates all finite certificates using exact modular or binary arithmetic.
- [`exhaustive_summary.json`](exhaustive_summary.json) records the expected certificate output.
- [`verification.md`](verification.md) explains which parts are theorem-based, which parts are finite certificates, and which parts are scope-limited.

The public priority status is `NOT_ESTABLISHED`.
