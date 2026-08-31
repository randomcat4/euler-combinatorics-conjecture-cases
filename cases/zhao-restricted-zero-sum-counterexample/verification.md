# Verification

## Symbolic layer

The Conjecture 6.1 proof reduces every occurrence-subsequence to a coefficient vector in $C_4^4$, computes the two-element kernel of the displayed homomorphism, and treats both kernel vectors. The zero vector yields only the empty selection. The nonzero vector yields exactly the nine length-10 zero sums.

The infinite `C_n^4` proof is a general argument: a zero-sum subsequence of length at most `2n-1` must have length exactly `n`, and then every non-first coordinate forces all selected vector types to be identical, which would require `n` copies of a type that appears only `n-1` times.

The `C_2^7` lower-branch exact value for `s_{\leq4}` uses the parity-check equivalence with binary `[12,5,>=5]` codes. The proof excludes such a code by extending to an even `[13,5,>=6]` code and deriving the impossible moment identity `12A_12=16`.

## Exact finite layer

The checker evaluates every finite witness in exact arithmetic. It asserts that:

- the `C_2 direct-sum C_4^3` length-12 sequence has zero hits in lengths 1 through 9 and exactly nine hits in length 10;
- the `C_2^2 direct-sum C_4^2` length-13 sequence has zero hits in lengths 1 through 5;
- the `C_2^7` length-11 sequence has zero hits in lengths 1 through 4;
- the `C_2^7` length-14 sequence has zero exact length-4 zero-sum subsets;
- the `C_2^8` length-18 sequence has zero exact length-6 zero-sum subsets;
- the extended Golay 24-column witness in `C_2^12` has zero hits in lengths 1 through 7; and
- the normalized `C_2^7` size-12 search checks all `C(64,5)=7,624,512` candidates and finds none.

The exact enumeration certifies only the displayed finite witnesses. General conclusions use the symbolic proofs and cited theorems stated in [`proof.md`](proof.md) and [`sources.md`](sources.md).

## Scope checks

- Conjecture 6.1 is stated as disproved.
- Conjecture 6.2 is stated as disproved, with upper- and lower-branch witnesses explicitly separated.
- Conjecture 6.4 is stated only as lower-branch-false at `C_2^7`.
- Conjecture 1.2 is stated only as having a supplemental even-rank counterexample with public priority `NOT_ESTABLISHED`.
- No claim is made that all source-paper conjectures or Section 1 theorems have been settled.
