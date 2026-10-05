#!/usr/bin/env python3
"""Exact, dependency-free supporting checks for the subgroup integrality theorem.

This script does two separate things.

1. It checks the integer expressions in the proposed square-gap lemma on a large
   audit box.  This finite loop is only a regression check; proof is in proof.md.
2. It constructs the Cayley graph in the frozen convention for four explicit
   pairs (G,H).  For each, it constructs an integer matrix-coefficient vector v
   and verifies exactly that q(A)v=0 for the advertised irreducible quadratic q.
   Thus q divides the characteristic polynomial over Q.  No floating point is
   used.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path


Perm = tuple[int, ...]
Mat = tuple[tuple[int, ...], ...]


def pmul(p: Perm, q: Perm) -> Perm:
    """p*q, with functions acting on the left: apply q, then p."""
    return tuple(p[q[i]] for i in range(len(p)))


def pinv(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


def generated_group(degree: int, generators: list[Perm]) -> list[Perm]:
    identity = tuple(range(degree))
    seen = {identity}
    queue = [identity]
    while queue:
        x = queue.pop()
        for s in generators:
            for y in (pmul(s, x), pmul(x, s)):
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
    return sorted(seen)


def generated_subgroup(identity: Perm, generators: list[Perm]) -> set[Perm]:
    seen = {identity}
    queue = [identity]
    while queue:
        x = queue.pop()
        for s in generators:
            for y in (pmul(s, x), pmul(x, s)):
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
    return seen


def is_normal(group: list[Perm], subgroup: set[Perm]) -> bool:
    return all(
        pmul(pmul(g, h), pinv(g)) in subgroup
        for g in group
        for h in subgroup
    )


def mmul(a, b):
    rows, mid, cols = len(a), len(b), len(b[0])
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(mid)) for j in range(cols))
        for i in range(rows)
    )


def madd(*matrices):
    return tuple(
        tuple(sum(a[i][j] for a in matrices) for j in range(len(matrices[0][0])))
        for i in range(len(matrices[0]))
    )


def mscale(c, a):
    return tuple(tuple(c * x for x in row) for row in a)


def eye(d: int) -> Mat:
    return tuple(tuple(int(i == j) for j in range(d)) for i in range(d))


def standard_rep(p: Perm) -> Mat:
    """The sum-zero standard representation in basis e_i-e_last."""
    m = len(p)
    d = m - 1
    return tuple(
        tuple(int(p[j] == i) - int(p[m - 1] == i) for j in range(d))
        for i in range(d)
    )


def d8_group_and_rep():
    # Vertices of a square are labelled counterclockwise 0,1,2,3.
    one = tuple(range(4))
    rot = (1, 2, 3, 0)
    ref = (0, 3, 2, 1)
    R = ((0, -1), (1, 0))
    S = ((1, 0), (0, -1))
    generators = [(rot, R), (ref, S)]
    rep = {one: eye(2)}
    queue = [one]
    while queue:
        x = queue.pop()
        for gp, gm in generators:
            y = pmul(gp, x)
            ym = mmul(gm, rep[x])
            if y in rep:
                assert rep[y] == ym
            else:
                rep[y] = ym
                queue.append(y)
    assert len(rep) == 8
    return sorted(rep), ref, rep


def cayley_adjacency(group: list[Perm], subgroup: set[Perm]):
    """Adjacency for x*y^{-1} in S_H, returned as neighbour index lists."""
    one = tuple(range(len(group[0])))
    vertices = [(a, b) for a in group for b in group]
    index = {x: i for i, x in enumerate(vertices)}
    outside = [g for g in group if g not in subgroup]
    gens = [(g, one) for g in outside]
    gens += [(one, g) for g in outside]
    gens += [(g, g) for g in outside]
    neighbours = []
    for a, b in vertices:
        row = []
        for s, t in gens:
            # y=(s,t)^(-1) x, so x*y^{-1}=(s,t).
            y = (pmul(pinv(s), a), pmul(pinv(t), b))
            row.append(index[y])
        assert len(set(row)) == len(row)
        neighbours.append(sorted(row))
    return vertices, neighbours


def matvec(neighbours: list[list[int]], v: list[int]) -> list[int]:
    return [sum(v[j] for j in row) for row in neighbours]


def polynomial_apply(neighbours, v, trace: int, determinant: int):
    av = matvec(neighbours, v)
    a2v = matvec(neighbours, av)
    return [a2v[i] - trace * av[i] + determinant * v[i] for i in range(len(v))]


def coefficient_vector(vertices, rep: dict[Perm, Mat], hgen: Perm) -> list[int]:
    """2 times the (0,0) coefficient of pi(x)^(-1)E on End(V)."""
    d = len(next(iter(rep.values())))
    I = eye(d)
    Rh = rep[hgen]
    twoE = tuple(tuple(I[i][j] + Rh[i][j] for j in range(d)) for i in range(d))
    out = []
    for a, b in vertices:
        # pi(a,b)^(-1) E = rho(a)^(-1) E rho(b).
        value = mmul(mmul(rep[pinv(a)], twoE), rep[b])[0][0]
        out.append(value)
    assert any(out)
    return out


def matrix_checks(neighbours, degree: int):
    n = len(neighbours)
    assert all(len(row) == degree for row in neighbours)
    assert all(i not in row for i, row in enumerate(neighbours))
    assert all(i in neighbours[j] for i, row in enumerate(neighbours) for j in row)
    edge_count = sum(map(len, neighbours)) // 2
    assert edge_count == n * degree // 2
    payload = b"".join(
        i.to_bytes(2, "little") + j.to_bytes(2, "little")
        for i, row in enumerate(neighbours)
        for j in row
    )
    return edge_count, sha256(payload).hexdigest().upper()


def audit_pair(name, group, hgen, rep, r):
    one = tuple(range(len(group[0])))
    H = generated_subgroup(one, [hgen])
    assert len(H) == 2
    assert not is_normal(group, H)
    n, h, d = len(group), len(H), len(next(iter(rep.values())))
    k = n // h
    vertices, neighbours = cayley_adjacency(group, H)
    graph_degree = 3 * (n - h)
    edge_count, adjacency_hash = matrix_checks(neighbours, graph_degree)

    # q(x)=x^2-trace*x+determinant is the two-dimensional block factor.
    trace = n - 4 * h
    determinant = 3 * h * h - 3 * n * h + Fraction(2 * n * h * r, d)
    assert determinant.denominator == 1
    determinant = determinant.numerator
    discriminant = trace * trace - 4 * determinant
    assert math.isqrt(discriminant) ** 2 != discriminant

    # Independently check the displayed two-dimensional block itself.  We use
    # 2E and 2(I-E), so all matrices stay integral.
    I = eye(d)
    twoE = madd(I, rep[hgen])
    twoF = madd(mscale(2, I), mscale(-1, twoE))
    zero = mscale(0, I)
    outside = [g for g in group if g not in H]
    def T(X):
        ans = zero
        for g in outside:
            Rg, Rgi = rep[g], rep[pinv(g)]
            ans = madd(ans, mmul(Rg, X), mmul(X, Rgi), mmul(mmul(Rg, X), Rgi))
        return ans
    a = Fraction(n * r, d) - 3 * h
    b = Fraction(n * r, d)
    c = Fraction(n * (d - r), d)
    e = Fraction(n * (d - r), d) - h
    assert T(twoE) == madd(mscale(a, twoE), mscale(b, twoF))
    assert T(twoF) == madd(mscale(c, twoE), mscale(e, twoF))

    v = coefficient_vector(vertices, rep, hgen)
    residual = polynomial_apply(neighbours, v, trace, determinant)
    assert residual == [0] * len(v)
    av = matvec(neighbours, v)
    # An irreducible quadratic cannot annihilate a rational eigenvector.
    assert not all(av[i] * v[0] == av[0] * v[i] for i in range(len(v)))

    return {
        "name": name,
        "group_order": n,
        "subgroup_order": h,
        "index": k,
        "subgroup_nonnormal": True,
        "graph_vertices": n * n,
        "graph_degree": graph_degree,
        "graph_edges": edge_count,
        "adjacency_row_hash_sha256": adjacency_hash,
        "representation_dimension_d": d,
        "fixed_dimension_r": r,
        "two_by_two_block_columns": [[int(a), int(b)], [int(c), int(e)]],
        "quadratic_factor_coefficients_high_to_low": [1, -trace, determinant],
        "quadratic_discriminant": discriminant,
        "certificate_vector": v,
        "certificate_vector_sha256": sha256(
            json.dumps(v, separators=(",", ":")).encode()
        ).hexdigest().upper(),
        "exact_check": "q(A)v is the zero vector over Z",
    }


def integer_regression_check():
    checked = 0
    for d in range(2, 501):
        for r in range(1, d):
            for k in range(d * r + 1, d * r + 202):
                N = d * (k + 2) - 4 * r
                M = d * d * (k + 2) ** 2 - 8 * k * d * r
                assert M == N * N + 16 * r * (d - r)
                assert math.isqrt(M) ** 2 != M
                checked += 1
    exceptions = []
    for d, r, k in [(2, 1, 3), (3, 1, 4)]:
        N = d * (k + 2) - 4 * r
        M = d * d * (k + 2) ** 2 - 8 * k * d * r
        exceptions.append({"d": d, "r": r, "k": k, "N": N, "M": M})
    return {"box_tuples_checked": checked, "exception_minima": exceptions}


def main():
    transposition3 = (1, 0, 2)
    S3 = generated_group(3, [transposition3, (1, 2, 0)])
    S3rep = {g: standard_rep(g) for g in S3}

    D8, reflection, D8rep = d8_group_and_rep()

    double_transposition = (1, 0, 3, 2)
    A4 = generated_group(4, [(1, 2, 0, 3), double_transposition])
    assert len(A4) == 12
    A4rep = {g: standard_rep(g) for g in A4}

    transposition4 = (1, 0, 2, 3)
    S4 = generated_group(4, [transposition4, (1, 2, 3, 0)])
    assert len(S4) == 24
    S4rep = {g: standard_rep(g) for g in S4}

    output = {
        "method": "actual Cayley adjacency plus exact integer polynomial-vector certificate",
        "integer_regression": integer_regression_check(),
        "examples": [
            audit_pair("S3, H=<transposition>", S3, transposition3, S3rep, 1),
            audit_pair("D8(order 8), H=<reflection>", D8, reflection, D8rep, 1),
            audit_pair("A4, H=<double transposition>", A4, double_transposition, A4rep, 1),
            audit_pair("S4, H=<transposition>", S4, transposition4, S4rep, 2),
        ],
    }
    destination = Path(__file__).with_name("certificates.json")
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "certificate_file": str(destination),
        "integer_regression": output["integer_regression"],
        "examples": [
            {k: v for k, v in x.items() if k not in {"certificate_vector"}}
            for x in output["examples"]
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
