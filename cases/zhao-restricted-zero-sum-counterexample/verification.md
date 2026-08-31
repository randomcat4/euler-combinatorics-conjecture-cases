# Verification

## Symbolic layer

The proof reduces every occurrence-subsequence to a coefficient vector in $C_4^4$, computes the two-element kernel of the displayed homomorphism, and treats both kernel vectors. The zero vector yields only the empty selection. The nonzero vector yields exactly the nine length-10 zero sums.

## Exact finite layer

The checker evaluates every one of the $2^{12}-1=4,095$ nonempty labelled occurrence-subsets in exact modular arithmetic. It asserts that:

- the only zero-sum length is 10;
- exactly nine zero-sum occurrence-subsets exist; and
- no zero-sum occurrence-subsequence has length at most 9.

The exact enumeration certifies the displayed finite witness. The general conclusion that the conjecture is false follows from the symbolic hypothesis check and this witness.
