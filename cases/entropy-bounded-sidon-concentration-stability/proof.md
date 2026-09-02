# Proof

Let

```text
S = {a in A : p_a > 0}.
```

The set `S` is countable. For `z in G`, write

```text
q_z = P(X+X'=z) = sum_{c in S, z-c in S} p_c p_{z-c}.
```

For `a,b in S`, define the nonnegative collision surplus

```text
R(a,b) = log(q_{a+b}/(p_a p_b)) - (log 2) * 1_{a != b}.
```

If `a != b`, the two ordered representations `(a,b)` and `(b,a)` both
contribute to `q_{a+b}`, so `q_{a+b} >= 2p_a p_b`. If `a=b`, the ordered pair
`(a,a)` contributes, so `q_{2a} >= p_a^2`. Thus

```text
R(a,b) >= 0.                                             (1)
```

Since `H(X)<infinity`, the pair `(X,X')` has finite entropy and `X+X'` is a
function of it. The conditional entropy identity gives

```text
E log(q_{X+X'}/(p_X p_X')) = H(X,X' | X+X')
                           = 2H(X) - H(X+X')
                           = H(X) - s(X).
```

Therefore condition (42) is equivalent to

```text
E R(X,X') <= C.                                          (2)
```

Let

```text
E_bad = {R(X,X') >= log 2}.
```

By (1), (2), and Markov's inequality,

```text
P(E_bad) <= C/log 2.                                     (3)
```

All quantities here are computed for the original distribution of `X`; no
truncated or conditional distribution is assumed to inherit (42).

For an unordered two-element multiset `{a,b}` in `S`, define its total ordered
mass

```text
u(a,b) = 2p_a p_b / (1 + 1_{a=b}).
```

Then

```text
R(a,b) >= log 2  if and only if  q_{a+b} >= 2u(a,b).      (4)
```

Suppose two different unordered multisets `{a_1,b_1}` and `{a_2,b_2}` have the
same sum. Their ordered contributions to that sum are distinct, hence

```text
q_{a_1+b_1} >= u(a_1,b_1) + u(a_2,b_2).
```

Taking the multiset with smaller `u`, (4) shows that it is bad. Consequently,
every subset of `S` containing no bad unordered pair is a Sidon set. This
argument covers diagonal pairs and torsion in the ambient abelian group.

Now fix `0<tau<1` and split

```text
L_tau = {a in S : p_a < tau},
K_tau = {a in S : p_a >= tau}.
```

The entropy bound gives

```text
H(X) = sum_{a in S} p_a log(1/p_a)
     >= sum_{a in L_tau} p_a log(1/p_a)
     >= P(X in L_tau) log(1/tau),
```

so

```text
P(X in L_tau) <= D/log(1/tau).                           (5)
```

The set `K_tau` is finite because `|K_tau| <= 1/tau`.

Build a finite graph on `K_tau`, allowing loops, by putting an unordered edge
`{a,b}` whenever `R(a,b) >= log 2`. For each bad edge choose an endpoint of
smaller probability; for a loop choose its unique endpoint. Let `D_tau` be the
set of chosen endpoints and define

```text
B_tau = K_tau \ D_tau.
```

The set `D_tau` covers every bad edge, so `B_tau` has no bad unordered pair.
By the previous paragraph, `B_tau` is Sidon.

For a bad edge in `K_tau`,

```text
min(p_a,p_b) <= p_a p_b (1 + 1_{a != b}) / tau.           (6)
```

Indeed, for `a=b` this is `p_a <= p_a^2/tau`, and for `a != b` it follows from
both endpoints having probability at least `tau`. Hence

```text
P(X in D_tau)
  <= sum_bad_edges min(p_a,p_b)
  <= (1/tau) sum_bad_edges p_a p_b (1 + 1_{a != b})
  <= P(E_bad)/tau
  <= C/(tau log 2).                                      (7)
```

Combining (5) and (7),

```text
P(X notin B_tau)
  <= D/log(1/tau) + C/(tau log 2).                       (8)
```

Assume first that `0<C<1`. Choose `tau=sqrt(C)`. Then (8) becomes

```text
P(X notin B_tau)
  <= 2D/log(1/C) + sqrt(C)/log 2.
```

If the right side is at most `1`, take this `B_tau`. If it is greater than
`1`, take the empty Sidon set. In both cases there is a Sidon set `B` with

```text
P(X in B) >= 1 - min{1, 2D/log(1/C) + sqrt(C)/log 2}.
```

If `C>=1`, the empty Sidon set gives the stated bound because `f(C,D)=1`.

It remains to consider `C=0`. By (1) and (2), `R(X,X')=0` almost surely. If
the support `S` were not Sidon, the collision argument above would produce a
bad unordered pair with positive ordered probability, contradicting
`P(E_bad)=0`. Thus `S` is Sidon, and taking `B=S` gives `P(X in B)=1`.

Finally, for each fixed finite `D`,

```text
2D/log(1/C) -> 0,
sqrt(C)/log 2 -> 0
```

as `C` decreases to `0`. Therefore the displayed `f(C,D)` satisfies the
source open problem.
