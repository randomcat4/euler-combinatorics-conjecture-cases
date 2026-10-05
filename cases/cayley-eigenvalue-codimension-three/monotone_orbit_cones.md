# Closed monotone orbit cones for three- and four-cycles

The [complete analytic proofs](coneproof.md) give the comparison values,
uniform inequalities, stable-pattern coverage, and fixed-order boundary
construction. [checkcone.py](checkcone.py) rebuilds the symbolic and rational
inputs independently of the stored certificates.

Let `R subseteq [n]` be marked and give every `k`-cycle with support `A` the
weight `f(|A intersect R|)`, where the feasible values of `f` are nonnegative
and nondecreasing. This note records complete representation-level
classifications for `k=3` and for `k=4` with two or three marked points.

## Results

### Three-cycles

For `n>=5` and `1<=|R|<=n-2`, write the operator in threshold coordinates as

```text
T = a K_n + u B_hit + v M_R + w K_R,     a,u,v,w>=0.
```

Here `K_n` is the normal three-cycle class, `B_hit` is the support-at-least-one
threshold, `M_R` is the support-at-least-two threshold, and `K_R` is the local
three-cycle class on `R`. If `a+u+v>0`, the largest nondegree eigenvalue is
attained exactly by the standard representation and its sign twist. The only
nonzero face excluded by this condition is the pure local ray
`a=u=v=0,w>0`, which is genuinely degenerate. In particular, for
`|R|=1,2`, every nonzero closed monotone weight has the strict classification.

### Four-cycles with two marked points

Let `n>=6` and `|R|=2`.

- If `n>=7`, every nonzero closed monotone weight is standard-only.
- If `n=6`, every nonconstant closed monotone weight is standard-only. On the
  positive constant ray, `(2,2,2)` is the unique additional representation
  attaining the standard value.

### Four-cycles with three marked points

Let `n>=6` and `|R|=3`.

- If `n>=7`, every nonzero closed monotone weight is standard-only.
- If `n=6`, the unique additional attaining representation is `(2,2,2)`, and
  it occurs exactly when the feasible weights satisfy
  `f(1)=f(2)=f(3)>0`. The formal value `f(0)` is invisible at this order.

All conclusions above are representation-level statements. They do not assert
a uniform multiplicity inside the standard block on every boundary face.

## Common proof mechanism

Every monotone orbit weight has a nonnegative threshold decomposition

```text
T_f = sum_s d_s B_s,     d_s=f(s)-f(s-1)>=0,
```

with the normal class as `B_0`. The relevant threshold rays have a common
standard top space: vectors supported on `R^c` whose coordinates sum to zero.
For self-adjoint rays `A_i` with standard values `alpha_i`, Weyl's inequality
gives the loss estimate

```text
sum_i c_i alpha_i - lambda_max(sum_i c_i A_i)
  >= sum_i c_i (alpha_i-lambda_max(A_i))
```

for `c_i>=0`. Thus a single positive strict ray makes the whole combination
strict; the work is to classify equality for the threshold rays.

## Three-cycle endpoints

The normal class and the hit threshold are strict outside the two target
representations. The majority threshold satisfies the compatible standard
bound by restricting to `Sym(R)` types. For types other than the trivial and
sign types, the content estimate has strictly positive margin. On the two
one-dimensional types use the exact identity

```text
M_R = sum_{E subseteq R, |E|=2} C(n,3;E)^+ - 2 K_R.
```

The local class `K_R` is scalar there, while every hard term
`C(n,3;E)^+` has a strict gap by Conjecture 4.7. Hence `M_R` is strict as
well. The only ray with no such global strictness is `K_R`, producing exactly
the pure-local exception stated above.

## Four-cycle endpoints

For two marked points the three rays are the normal class `K_4`, the hit
threshold `B_1`, and the hard term `B_2=C(n,4;R)^+`. The two-box content
calculation makes `B_1` strict, while Conjecture 4.7 makes `B_2` strict. The
normal ray is strict for `n>=7`; at `n=6` its only extra equality block is
`(2,2,2)`. The exact `S_2 x S_4` certificate shows that both noncentral gaps
are positive even in that block, yielding the stated boundary.

For three marked points, `B_1` is controlled by a three-box content formula.
The low-tail patterns are exhausted by a stable symbolic certificate and the
remaining shapes by a uniform content bound. The middle threshold has the
positive decomposition

```text
B_2 = sum_{S subseteq R, |S|=2} D_S + B_3,
```

where every `D_S` is an embedded hard-containment operator with a compatible
non-strict bound and `B_3=C(n,4;R)^+` is strict by Conjecture 4.7. Therefore
`B_2` is strict. The exact `S_3 x S_3` certificate at `n=6` then leaves only
the displayed `(2,2,2)` equality face.

## Evidence boundary

The files in `evidence/monotone` are exact finite certificates for the two
`n=6` classifications and the stable low-tail patterns in the `B_1` content
argument. `check_monotone_cones.py` recomputes the boundary gap conditions
from those certificates. The general inequalities are the analytic arguments
above, not consequences of finite scanning.

The deeper four-marked closed face `f(0)=f(1)=0`, general larger marked sets,
and general `k>=4` remain open and are not claimed here.
