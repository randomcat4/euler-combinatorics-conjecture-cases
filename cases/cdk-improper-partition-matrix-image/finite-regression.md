# Finite regression

Run from the repository root:

```bash
python cases/cdk-improper-partition-matrix-image/mine_cdk_image.py --n-max 8 --check cases/cdk-improper-partition-matrix-image/mining_n_le_8.json
```

The script uses only the Python standard library. It enumerates every
inversion sequence for `1 <= n <= 8`, computes:

1. membership in the CDK image of improper partition matrices by constructing
   the CDK inverse and testing Chern-Fu impropriety; and
2. membership in the intrinsic \(C_{\mathrm{pair}}\) predicate.

The check passes when the two sets have zero symmetric difference for every
tested `n` and the generated summary matches the stored JSON certificate.

The finite denominator is 46,233 inversion sequences. This finite check is not
the all-order proof.
