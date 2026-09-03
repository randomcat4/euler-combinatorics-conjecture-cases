# Verification

The released theorem was checked against a fixed proof package by two fresh
read-only mathematical reviews. Both reviews returned `CORRECT`.

The verification covered:

- the exact statement of the `delta(G)=2` slice and its equivalence to the
  source real-valued bound;
- the high--high edge deletion reduction;
- compression of the non-pure part into a positive-thread pseudokernel,
  including loops and parallel edges;
- the six-state thread encoding and the joint run-incidence interval;
- the platform and bank repairs for the two possible bad boxes;
- the pure-cycle capacity theorem with only one global `+2` loss;
- the exceptional `C5` splice repair;
- the double-counting bound for all degree classes `j>=3`;
- the `2C4` sharpness certificate.

The reviews were independent mathematical checks of the fixed statement and
proof, not paper-format reviews and not finite-regression-only checks.

The executable check in this case exhaustively enumerates the `2C4` sharpness
certificate:

```bash
python cases/minimum-degree-two-degree-multiplicity/check_sharpness.py
```

Expected result:

```text
PASS: 2C4 sharpness certificate verified
```
