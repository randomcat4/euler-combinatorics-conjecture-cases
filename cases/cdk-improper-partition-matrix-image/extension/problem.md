# Original problem

**Chern--Fu, Question 5.5 in arXiv v2.** [Source paper](https://arxiv.org/abs/2508.21318v2).

Characterize intrinsically which inversion sequences are images of improper partition matrices under the Claesson--Dukes--Kubitzke (CDK) bijection.

## Definitions and scope

Distinct sequence values, with n appended as a sentinel, define intervals of positions. Within each interval pair the first two positions, the next two, and so on. These interval boundaries depend on the value set; they are not arbitrary adjacent pairs.

## Answer and extension

The CDK image of improper matrices consists exactly of sequences whose entries agree within every value-determined matched pair. Allowing unequal pairs gives a commuting family of swaps. With column sizes fixed, each orbit is completely determined by its unordered pairs and unpaired final letters.

An orbit with d unequal pairs has 2^d elements, unique all-increasing and all-decreasing representatives, and binomial(d,r) elements with r proper ascents. These swaps preserve every cell cardinality. Inclusion-exclusion over missing row letters gives the exact orbit enumerator.
