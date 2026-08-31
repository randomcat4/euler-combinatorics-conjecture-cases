# Sources

## Original question

Shane Chern and Shishuo Fu, “Signed counting of partition matrices,” *Journal of Combinatorial Theory, Series A* 223, article 106213. The direct statistic-preserving bijection is posed as Question 5.7 in the current arXiv version; it appeared as Question 5.5 in an earlier version.

- [arXiv record](https://arxiv.org/abs/2508.21318)
- [DOI record](https://doi.org/10.1016/j.jcta.2026.106213)

The paper supplies the definitions of improper partition matrices, the semi-weight `v`, the restricted inversion-sequence class, and the plus/minus subclasses. Its analytic equidistribution theorem does not itself provide the direct cross-model bijection requested by the question.

## Standard ingredients used in the proof

- Chern and Fu, Lemma 3.2: the parity-pair structure within a column of an improper partition matrix. The proof here turns that structure into a two-way collapse/expansion algorithm and tracks the minus condition.
- Anders Claesson, Mark Dukes, and Martina Kubitzke, “[Partition and composition matrices](https://arxiv.org/abs/1006.1312)”: the explicit correspondence between partition matrices and inversion tables. The formulas and the inverse checks needed here are reproduced in the proof.
- Sylvie Corteel and Sandrine Dasse-Hartaut, “[Statistics on staircase tableaux, Eulerian and Mahonian statistics](https://doi.org/10.46298/dmtcs.2907)”: the insertion correspondence from inversion tables to permutations and its descent-bottom interpretation. The required statement is also proved directly here.

## Related background

- Published work on restricted inversion sequences gives equivalent descriptions and enumerative results for `I_n(-,-,=)`.
- Earlier generating-function results establish equidistribution of the two statistics but do not supply the explicit source-to-target map, its inverse, or the exact-image certificate proved here.

These references identify provenance for definitions and standard components only. They do not support a public novelty or priority claim for the composite construction.
