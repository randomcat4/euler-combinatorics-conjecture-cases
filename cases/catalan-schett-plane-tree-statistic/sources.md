# Public Sources

## Original problem

Zhicong Lin, Jing Liu, and Sherry H. F. Yan,
"Parity Statistics on Restricted Permutations and the Catalan–Schett
Polynomials," *Journal of Combinatorial Theory, Series A* 215 (2025),
Article 106049.

- [DOI: 10.1016/j.jcta.2025.106049](https://doi.org/10.1016/j.jcta.2025.106049)
- [arXiv:2409.01558](https://arxiv.org/abs/2409.01558)

Problem 2.18 asks for the natural plane-tree statistic used here. The same
paper provides two important interfaces:

- Theorem 1.3 interprets the pair
  `(mnd(pi), mna(pi^{-1}))` on binary trees.
- Theorem 1.4 gives a recursive bijection from plane trees to
  `231`-avoiding permutations that preserves `mark` and `mnd`.

The open obligation is not merely to pull the second statistic back through a
known bijection, but to identify it intrinsically on plane trees. The statistic
`st` in this package does exactly that.

## Earlier plane-tree bijection

Sergey Kitaev and Philip B. Zhang,
"Non-overlapping Descents and Ascents in Stack-sortable Permutations,"
*Discrete Applied Mathematics* 344 (2024), 112–119.

- [DOI: 10.1016/j.dam.2023.11.020](https://doi.org/10.1016/j.dam.2023.11.020)
- [Accepted manuscript](https://strathprints.strath.ac.uk/87088/)

Their Theorem 4 gives an earlier recursive plane-tree bijection preserving
`mark` and `mnd`. It supplies context for the first coordinate but does not by
itself provide the intrinsic second coordinate proved here.

## Related work

- Zhicong Lin and Sherry H. F. Yan, work on weakly increasing trees and
  multiset Schett polynomials: [arXiv:2104.10539](https://arxiv.org/abs/2104.10539).
- Further bijective work on weakly increasing trees:
  [arXiv:2502.09161](https://arxiv.org/abs/2502.09161).

These references are included to locate the problem mathematically. They do
not establish a claim of novelty or priority for this case.
