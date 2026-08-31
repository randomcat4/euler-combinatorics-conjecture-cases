# Formula check

Run from the repository root:

```bash
python cases/partition-matrix-q-sum-product/check_formula.py
```

The script uses only the Python standard library. It compares:

1. coefficients produced by the q-difference recurrence for the auxiliary
   word series;
2. coefficients produced by the public sum-product formula; and
3. direct enumeration of the column-word encoding of partition matrices.

The finite denominator is every object in the direct enumeration for
`1 <= n <= 8`, a total of 46,233 objects. The run is deterministic and ends
with `ALL CHECKS PASS`.

This check is not the all-order proof. It is included to expose conventions,
endpoint behavior, and implementation errors.
