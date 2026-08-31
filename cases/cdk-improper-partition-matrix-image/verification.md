# Verification

## Mathematical review

The all-order proof was checked in two independent read-only mathematical
reviews. Both reviews returned `CORRECT`. Their checks covered:

1. the source definitions of partition matrix, inversion sequence, the CDK map,
   and Chern-Fu proper/improper ascent and descent;
2. the version-sensitive source locator: arXiv v2 Question 5.5, not arXiv v1
   Question 5.5;
3. the inverse construction from \(A(e)=\{a_1<\cdots<a_D\}\), including
   nonempty rows, nonempty columns, column monotonicity, and upper
   triangularity;
4. the fact that applying \(\Pi_n\) to the constructed inverse returns the
   original inversion sequence;
5. the equivalence between CDK columns and the value intervals
   \((a_r,a_{r+1}]\);
6. the equivalence between row equality and equality of entries of the
   inversion sequence;
7. both inclusions in the theorem;
8. the parity translation from internal odd transition positions to proper
   ascent/descent pairs; and
9. boundary cases for `n=1`, singleton intervals, odd-length intervals,
   positive value boundaries, and adjacent-label scope.

The paper-level review also checked that the public exposition did not drift
from the independently verified theorem or proof.

## Finite regression

The checker [mine_cdk_image.py](mine_cdk_image.py) enumerates all inversion
sequences for `1 <= n <= 8`. For each sequence it computes the CDK inverse
impropriety test and the intrinsic \(C_{\mathrm{pair}}\) predicate, then
compares the resulting sets.

| `n` | all inversion sequences | CDK image | intrinsic predicate | symmetric difference |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 0 |
| 2 | 2 | 2 | 2 | 0 |
| 3 | 6 | 4 | 4 | 0 |
| 4 | 24 | 10 | 10 | 0 |
| 5 | 120 | 28 | 28 | 0 |
| 6 | 720 | 88 | 88 | 0 |
| 7 | 5040 | 304 | 304 | 0 |
| 8 | 40320 | 1144 | 1144 | 0 |

The finite denominator contains \(1!+\cdots+8!=46,233\) inversion sequences.
The compact certificate is [mining_n_le_8.json](mining_n_le_8.json).

## Verification boundary

The finite regression is a calibration and implementation check. Generality
comes from the symbolic proof in [proof.md](proof.md). The result has not
been encoded in a proof assistant, and public novelty or priority remains
`NOT_ESTABLISHED`.
