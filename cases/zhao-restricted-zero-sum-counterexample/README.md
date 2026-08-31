# Counterexample to Zhao's Conjecture 6.1

*Kevin Zhao · [arXiv:2506.21383](https://arxiv.org/abs/2506.21383)*

This package records an explicit counterexample to Conjecture 6.1 in Kevin Zhao's paper *On zero-sum subsequences in a finite abelian group of length not exceeding a given number*.

## Result

For

$$
G=C_2\oplus C_4^3,
$$

the Davenport constant is $D(G)=11$. The sequence displayed in [`proof.md`](proof.md) has length 12 and has no nonempty zero-sum occurrence-subsequence of length at most 9. Consequently,

$$
s_{\leq D(G)-2}(G)=s_{\leq 9}(G)\geq 13>D(G)+1=12,
$$

which disproves the conjectured equality.

## Evidence

- [`problem.md`](problem.md) records the source statement and checks every hypothesis.
- [`proof.md`](proof.md) gives a complete symbolic classification of the zero-sum occurrence-subsequences.
- [`check_counterexample.py`](check_counterexample.py) enumerates all 4,095 nonempty occurrence-subsets using exact modular arithmetic.
- [`exhaustive_summary.json`](exhaustive_summary.json) records the expected certificate output.
- [`verification.md`](verification.md) explains the relation between the symbolic proof and the finite certificate.

The public priority status is `NOT_ESTABLISHED`.
