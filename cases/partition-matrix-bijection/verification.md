# Verification

## Mathematical review

The same all-order proof was checked in two independent read-only reviews. Both reviews accepted the construction as complete. In particular, the reviewers checked:

1. the column-pair collapse and expansion are mutually inverse;
2. odd last-column size is exactly the source minus condition;
3. the partition-matrix, inversion-table, permutation, and ordered-partition maps are defined on their claimed domains;
4. the mutually recursive encoders terminate because the represented sequence length decreases at every recursive call;
5. the singleton and nonsingleton inverse branches produce legal restricted inversion sequences;
6. the target minus class, including `n=1`, is exactly the image;
7. the two displayed inverse compositions are identities; and
8. `v(Q)=dist(\rho_n(Q))` holds object by object, with zero included in `dist`.

## Exhaustive calibration

The public checker independently enumerates the target inversion sequences and generates the source objects through the proved collapse representation. For every `1 <= n <= 8`, it checks source validity, forward and inverse recovery at every layer, equality of the computed image with the independently enumerated target set, and equality of the statistic profiles.

The resulting source/target counts are:

| `n` | source | target | `dist` profile |
|---:|---:|---:|---|
| 1 | 1 | 1 | `1:1` |
| 2 | 1 | 1 | `2:1` |
| 3 | 3 | 3 | `2:2, 3:1` |
| 4 | 7 | 7 | `3:6, 4:1` |
| 5 | 21 | 21 | `3:6, 4:14, 5:1` |
| 6 | 67 | 67 | `4:36, 5:30, 6:1` |
| 7 | 237 | 237 | `4:24, 5:150, 6:62, 7:1` |
| 8 | 907 | 907 | `5:240, 6:540, 7:126, 8:1` |

See [exhaustive-check.md](exhaustive-check.md) for reproduction instructions and limitations.

## Verification boundary

The proof is a conventional mathematical proof supplemented by finite exhaustive tests. It has not been encoded in a proof assistant. The status of public novelty and priority remains `NOT_ESTABLISHED`.
