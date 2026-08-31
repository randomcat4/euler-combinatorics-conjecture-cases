# A Plane-Tree Statistic for the Catalan–Schett Distribution

This case gives an intrinsic statistic on rooted plane trees and a complete
bijective proof of the bivariate identity asked for in Problem 2.18 of Lin,
Liu, and Yan, *Parity Statistics on Restricted Permutations and the
Catalan–Schett Polynomials*.

The statistic is defined entirely by a terminating decomposition of a rooted
ordered tree. Its definition does not refer to a permutation, a binary tree,
an enumeration rank, a matching table, or the target generating function.
The proof supplies:

- the intrinsic tree statistic;
- an explicit bijection from rooted plane trees with `n` edges to
  `231`-avoiding permutations of length `n`;
- an explicit inverse;
- objectwise preservation of both statistics; and
- the resulting joint bivariate identity for every `n >= 1`.

This is one of the first publicly releasable results prepared from the Euler
system's case library for conjectures and open problems posed by authors who
had published in leading combinatorics journals within the preceding 24
months.

## Contents

- [problem.md](problem.md) states the original problem, definitions, and the
  semantic requirement that the statistic be intrinsic to plane trees.
- [proof.md](proof.md) is a self-contained proof package.
- [verification.md](verification.md) records the mathematical review and the
  independent computational checks.
- [status.md](status.md) separates correctness, completeness, and public
  priority.
- [sources.md](sources.md) gives the public sources and the relation of this
  case to prior work.
- [check_small_cases.py](check_small_cases.py) exhaustively checks every case
  through eight edges.
- [small_case_summary.json](small_case_summary.json) records the checker's
  compact output.

## Scope of the claim

The all-order proof, rather than the finite computation, establishes the
identity. The computation is included only to expose conventions, boundary
cases, and implementation errors.

No claim of novelty, priority, or first discovery is made here. Public
priority is **NOT_ESTABLISHED**.
