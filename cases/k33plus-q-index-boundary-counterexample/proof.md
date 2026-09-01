# Counterexample

Let `H` be the graph on vertices `0,1,2,3,4,5` with edge set

```text
{01,02,03,04,05,12,13,14,15,23,24,34}.
```

Equivalently, `H` is `K2 join (K3 union K1)`: vertices `0` and `1` form the `K2`, vertices `2,3,4` form the `K3`, vertex `5` is the isolated vertex in `K3 union K1`, and the join adds all edges from `{0,1}` to `{2,3,4,5}`.

The signless-Laplacian matrix of `H` is

```text
5 1 1 1 1 1
1 5 1 1 1 1
1 1 4 1 1 0
1 1 1 4 1 0
1 1 1 1 4 0
1 1 0 0 0 2
```

and

```text
det(xI-Q(H)) = x^6 - 24x^5 + 225x^4 - 1066x^3
             + 2700x^2 - 3456x + 1728
```

factors as

```text
(x^2 - 10x + 12)(x^4 - 14x^3 + 73x^2 - 168x + 144).
```

The Q-index is therefore

```text
q(H) = 5 + sqrt(13).
```

The checker also isolates the largest root in the rational interval

```text
[21513853/2500000, 86055613/10000000].
```

## `K_{3,3}^+`-Free

The non-edges of `H` are exactly

```text
25, 35, 45.
```

A six-vertex non-induced copy of `K_{3,3}^+` would use all vertices, split into a plus side of size three and the other side of size three, with every cross edge present. Thus all three non-edges above would have to lie inside one side of the split. That would place the four vertices `{2,3,4,5}` into one side of size three, which is impossible. Hence `H` is `K_{3,3}^+`-free.

## Not In The Printed Families

For `s=t=3,n=6`, the auxiliary graph in both source families is a 2-regular triangle-free graph on four vertices, hence `C4`.

The graph in `L_{6,3,3}` is `K2 join C4`. It has 13 edges, while `H` has 12 edges, so `H` is not in `L_{6,3,3}`. Moreover, this boundary `L_{6,3,3}` graph contains non-induced `K_{3,3}^+` subgraphs and is not itself feasible.

The graph in `Y_{6,3}` is `I2 join C4`. It is 4-regular and has Q-index `8`. The graph `H` has degree sequence

```text
5, 5, 4, 4, 4, 2,
```

so it is not isomorphic to `Y_{6,3}`. Also `5+sqrt(13)>8`.

## Exact Maximality Certificate

The finite denominator is all labelled simple graphs on six vertices, namely `2^15 = 32768` graphs. The checker canonicalizes by all `6! = 720` vertex relabellings, finds all 156 unlabelled graph classes, and filters the 147 unlabelled classes that are `K_{3,3}^+`-free.

For each non-candidate free class, the checker computes the characteristic polynomial of `Q(G)` exactly over the rationals and applies Sturm's theorem to prove that there is no Q-eigenvalue above the lower endpoint

```text
21513853/2500000 < 5 + sqrt(13).
```

For `H`, the same Sturm check proves that exactly one root lies in the displayed interval and no root lies above its upper endpoint. Thus `H` has strictly larger Q-index than every other `K_{3,3}^+`-free graph on six vertices. It is the unique extremal unlabelled class.

Since `H` is a maximum-Q-index `K_{3,3}^+`-free graph at an allowed parameter point and is not in `L_{6,3,3}` or `Y_{6,3}`, the exact printed Conjecture 5.1 is false.
