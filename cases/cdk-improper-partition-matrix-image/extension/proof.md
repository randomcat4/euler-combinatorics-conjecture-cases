# Proof guide

The full statements, constructions and proofs are in the [manuscript](../paper/extension.pdf). This file gives its dependency structure, not a substitute proof by numerical checking.

## Precise result

The CDK image of improper matrices consists exactly of sequences whose entries agree within every value-determined matched pair. Allowing unequal pairs gives a commuting family of swaps. With column sizes fixed, each orbit is completely determined by its unordered pairs and unpaired final letters.

An orbit with d unequal pairs has 2^d elements, unique all-increasing and all-decreasing representatives, and binomial(d,r) elements with r proper ascents. These swaps preserve every cell cardinality. Inclusion-exclusion over missing row letters gives the exact orbit enumerator.

## Argument

The distinct values of a CDK sequence are precisely the prefix sums of column sizes. They recover the inverse matrix: interval position determines the column, value determines the row. The inversion-sequence bound gives upper triangularity.

Disjoint matched-pair swaps preserve the multiplicity of each row letter in each column. Thus they preserve all nonempty-row constraints and commute. The only choices left by an unordered record are the directions of its unequal pairs. Inclusion-exclusion is needed only to decide which records use every row; it never constrains those directions.

## Attribution

The manuscript identifies the source question, the earlier public result and its classical inputs. No public priority or novelty certification is claimed.
