# Status

- Result type: `PARTIAL_RESULT`.
- Mathematical status: `PROVED` for the released minimum-degree-two slice.
- Verification status: `INDEPENDENTLY_VERIFIED`.
- Public priority: `NOT_ESTABLISHED`.
- Computation role: the finite checks certify the `2C4` sharpness witness and
  serve as regression tests. They do not replace the general proof.

## Exact Scope

For every finite simple graph `G` on `n>=3` vertices with `delta(G)=2`, there
exists a spanning subgraph `H` such that every degree class has size at most
`floor(n/3)+2`.

## Non-Claims

This case does not claim:

- the full Alon--Wei conjecture for `delta(G)>=3`;
- any result for regular graphs beyond what follows from the stated
  `delta(G)=2` hypothesis;
- connectedness, uniqueness, or nonemptiness of the chosen spanning subgraph;
- public priority or firstness.

## Sharpness

The graph `2C4` shows the integer bound is attained at `n=8`: no spanning
subgraph can keep all three degree classes below `4`, while a subgraph with
profile `(2,4,2)` exists.
