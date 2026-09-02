# Problem Statement

## Source

The source is the unnumbered open problem in Section 5 of Rupert Li, Lampros
Gavalakis, and Ioannis Kontoyiannis, *Entropic additive energy and entropy
inequalities for sums and products*, arXiv:2506.20813v2, physical PDF page 16.
The same work is associated with DOI `10.1109/TIT.2026.3653549`.

## Definitions

Let `G` be an abelian group, let `A` be a subset of `G`, and let `X,X'` be
independent identically distributed discrete random variables taking values in
`A`. Write

```text
p_a = P(X=a).
```

All logarithms are natural logarithms, and all entropy terms appearing below
are finite. Define

```text
s(X) = H(X+X') - H(X).
```

A set `B` in `G` is Sidon if every equality

```text
a+b = c+d,  a,b,c,d in B
```

comes from the same unordered two-element multiset:

```text
{a,b} = {c,d}.
```

## Original Stability Question

Given `C,D >= 0`, assume

```text
H(X) <= D
```

and

```text
s(X) >= H(X) - (log 2) * (1 - sum_a p_a^2) - C.        (42)
```

The source asks whether there is a function `f(C,D)`, depending only on `C` and
`D`, such that `f(C,D) -> 0` as `C -> 0` for every fixed `D`, and such that
there exists a Sidon set `B` contained in `A` with

```text
P(X in B) >= 1 - f(C,D).
```

## Public Result

This case proves that the following explicit function answers the question:

```text
f(C,D) =
  0,                                                     if C=0,
  min{1, 2D/log(1/C) + sqrt(C)/log 2},                   if 0<C<1,
  1,                                                     if C>=1.
```

The claim is a complete solution to the source open problem under the stated
finite-entropy convention. It does not assert optimality of `f`.
