# Problem

For a permutation `pi`, let its descending runs and ascending runs be the
maximal contiguous decreasing and increasing blocks, respectively. Define

```text
mnd(pi) = sum floor(r/2) over all descending-run lengths r,
mna(pi) = sum floor(r/2) over all ascending-run lengths r.
```

Equivalently, these are the maximum numbers of pairwise non-overlapping
adjacent descents and ascents.

Let `S_n(231)` be the set of `231`-avoiding permutations of `[n]`. Let `T_n`
be the set of rooted plane trees with `n` edges; the children of every vertex
are linearly ordered. A non-root internal vertex is marked when it has at
least one leaf child, and `mark(T)` denotes the number of marked vertices.

The problem is to find a **natural statistic** `st` on rooted plane trees such
that, for every `n >= 1`,

```text
sum_{pi in S_n(231)} x^mnd(pi) y^mna(pi^{-1})
  =
sum_{T in T_n} x^mark(T) y^st(T).
```

This is a joint distribution identity. The inverse in `mna(pi^{-1})`, the
order of the variables, and the exclusion of the root from `mark(T)` are all
essential.

## What counts as a solution

The word "natural" rules out defining `st(T)` by simply transporting
`mna(pi^{-1})` through a previously known bijection. A valid solution should
make `st(T)` computable directly from the rooted ordered tree and should
explain the combinatorial mechanism behind the identity.

Accordingly, this case proves a stronger certificate:

1. `st(T)` is given by a terminating recursion using only the plane-tree
   structure.
2. A bijection `Phi_n : T_n -> S_n(231)` and its inverse are explicit.
3. For every individual tree `T`, simultaneously,

   ```text
   mark(T) = mnd(Phi_n(T)),
   st(T)   = mna(Phi_n(T)^{-1}).
   ```

The empty tree with zero edges is used only as the recursion base. The
substantive statement remains quantified over every `n >= 1`.
