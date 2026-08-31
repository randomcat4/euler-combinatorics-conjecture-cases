# Verification

## Mathematical review

The all-order proof was checked in two independent read-only mathematical
reviews. Both reviews returned `CORRECT`. Their checks covered:

1. the exact source scope, including all `n >= 1` and
   \(S_n(q)=\sum_{P\in PM_n}q^{\operatorname{inv}(P)}\);
2. the q-difference equation, coefficient extraction, exponent range, and
   triangular uniqueness of each \(R_k\);
3. the bijection between partition matrices and nonempty column words with all
   row letters present;
4. the conversion of matrix inversions into ordinary word inversions;
5. complete row inclusion-exclusion, including the `W_0=0` empty-alphabet
   boundary;
6. the rise/stay prefix-path decomposition and the sign in
   \(W_k/(1+W_k)=1-R_k^{-1}\);
7. \(t\)-adic legitimacy of the infinite outer sum and of every inverse
   \(R_k^{-1}\);
8. `k=1`, `n=1`, `q=0`, and `q=1` boundary cases; and
9. the distinction between a bounded no-hit search and the all-order proof.

The independent paper-level review also checked that the public exposition did
not attribute a formal definition of "closed expression" to Chern and Fu.

## Finite regression

The checker [check_formula.py](check_formula.py) constructs coefficients from
the finite recurrence and independently enumerates the column-word encoding of
partition matrices through `n=8`. It checks the source polynomials in that
range and the endpoint specializations.

The deterministic output is:

```text
n=1: objects=1, q_degree=0, PASS
n=2: objects=2, q_degree=0, PASS
n=3: objects=6, q_degree=1, PASS
n=4: objects=24, q_degree=2, PASS
n=5: objects=120, q_degree=4, PASS
n=6: objects=720, q_degree=6, PASS
n=7: objects=5040, q_degree=9, PASS
n=8: objects=40320, q_degree=12, PASS
ALL CHECKS PASS
```

The direct-enumeration denominator contains \(1!+\cdots+8!=46,233\) objects.

## Verification boundary

The finite regression is a calibration and implementation check. Generality
comes from the symbolic proof in [proof.md](proof.md). The result has not
been encoded in a proof assistant, and public novelty or priority remains
`NOT_ESTABLISHED`.
