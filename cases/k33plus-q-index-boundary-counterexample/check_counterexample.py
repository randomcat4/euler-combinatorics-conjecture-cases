#!/usr/bin/env python3
"""Verify the six-vertex K_{3,3}^+ Q-index counterexample."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
import json
from pathlib import Path


N = 6
S = 3
T = 3

EXPECTED_CANDIDATE_EDGES = [
    [0, 1],
    [0, 2],
    [0, 3],
    [0, 4],
    [0, 5],
    [1, 2],
    [1, 3],
    [1, 4],
    [1, 5],
    [2, 3],
    [2, 4],
    [3, 4],
]
EXPECTED_CANDIDATE_LABEL = "000111111111111"
EXPECTED_CANDIDATE_CHARPOLY = [1, -24, 225, -1066, 2700, -3456, 1728]
EXPECTED_Y_CHARPOLY = [1, -24, 228, -1104, 2880, -3840, 2048]
CANDIDATE_LOWER = Fraction(21513853, 2500000)
CANDIDATE_UPPER = Fraction(86055613, 10000000)
OUTPUT = Path(__file__).with_name("exhaustive_summary.json")


def edge_order(n: int) -> list[tuple[int, int]]:
    return [(i, j) for i in range(n) for j in range(i + 1, n)]


EDGES6 = edge_order(N)
EDGE_INDEX6 = {edge: i for i, edge in enumerate(EDGES6)}
PERM_MAPS6: list[list[int]] = []
for perm in permutations(range(N)):
    mapping = []
    for i, j in EDGES6:
        a, b = sorted((perm[i], perm[j]))
        mapping.append(EDGE_INDEX6[(a, b)])
    PERM_MAPS6.append(mapping)


def has_edge(mask: int, i: int, j: int, n: int = N) -> bool:
    if i > j:
        i, j = j, i
    if n == N:
        idx = EDGE_INDEX6[(i, j)]
    else:
        idx = edge_order(n).index((i, j))
    return bool(mask & (1 << idx))


def mask_from_edges(n: int, edges: list[list[int]] | list[tuple[int, int]]) -> int:
    idx = {edge: i for i, edge in enumerate(edge_order(n))}
    mask = 0
    for i, j in edges:
        if i > j:
            i, j = j, i
        mask |= 1 << idx[(i, j)]
    return mask


def edges_of(mask: int, n: int = N) -> list[list[int]]:
    return [
        [i, j]
        for idx, (i, j) in enumerate(edge_order(n))
        if mask & (1 << idx)
    ]


def edge_count(mask: int) -> int:
    return mask.bit_count()


def degree_sequence(mask: int, n: int = N) -> list[int]:
    degrees = [0] * n
    for i, j in edges_of(mask, n):
        degrees[i] += 1
        degrees[j] += 1
    return sorted(degrees, reverse=True)


def msb_value(mask: int, n: int = N) -> int:
    value = 0
    for idx in range(len(edge_order(n))):
        value = (value << 1) | ((mask >> idx) & 1)
    return value


def bits_from_msb_value(value: int, n: int = N) -> str:
    return format(value, f"0{len(edge_order(n))}b")


def permute_mask6(mask: int, mapping: list[int]) -> int:
    out = 0
    for idx, new_idx in enumerate(mapping):
        if mask & (1 << idx):
            out |= 1 << new_idx
    return out


def canonical_label6(mask: int) -> str:
    return bits_from_msb_value(
        min(msb_value(permute_mask6(mask, mp), N) for mp in PERM_MAPS6), N
    )


def canonical_orbits6() -> tuple[dict[str, int], dict[int, str]]:
    reps: dict[str, int] = {}
    canonical_by_mask: dict[int, str] = {}
    visited: set[int] = set()

    for mask in range(1 << len(EDGES6)):
        if mask in visited:
            continue
        orbit = {permute_mask6(mask, mapping) for mapping in PERM_MAPS6}
        canonical_member = min(orbit, key=lambda item: msb_value(item, N))
        label = bits_from_msb_value(msb_value(canonical_member, N), N)
        reps.setdefault(label, canonical_member)
        for item in orbit:
            visited.add(item)
            canonical_by_mask[item] = label

    return reps, canonical_by_mask


def canonical_label(mask: int, n: int) -> str:
    if n == N:
        return canonical_label6(mask)
    edges = edge_order(n)
    edge_index = {edge: i for i, edge in enumerate(edges)}
    best = None
    for perm in permutations(range(n)):
        out = 0
        for idx, (i, j) in enumerate(edges):
            if mask & (1 << idx):
                a, b = sorted((perm[i], perm[j]))
                out |= 1 << edge_index[(a, b)]
        value = msb_value(out, n)
        best = value if best is None or value < best else best
    assert best is not None
    return bits_from_msb_value(best, n)


def k33plus_witnesses(mask: int) -> list[dict[str, list[int]]]:
    vertices = tuple(range(N))
    witnesses = []
    for plus_side in combinations(vertices, S):
        other_side = tuple(v for v in vertices if v not in plus_side)
        if not all(has_edge(mask, a, b) for a in plus_side for b in other_side):
            continue
        for plus_edge in combinations(plus_side, 2):
            if has_edge(mask, plus_edge[0], plus_edge[1]):
                witnesses.append(
                    {
                        "plus_side": list(plus_side),
                        "other_side": list(other_side),
                        "plus_edge": list(plus_edge),
                    }
                )
    return witnesses


def q_matrix(mask: int) -> list[list[int]]:
    matrix = [[0] * N for _ in range(N)]
    degrees = [0] * N
    for i, j in edges_of(mask):
        matrix[i][j] = 1
        matrix[j][i] = 1
        degrees[i] += 1
        degrees[j] += 1
    for i, degree in enumerate(degrees):
        matrix[i][i] = degree
    return matrix


def mat_mul(
    a: list[list[Fraction]], b: list[list[Fraction]]
) -> list[list[Fraction]]:
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def charpoly_coeffs_q(mask: int) -> list[int]:
    q = [[Fraction(value) for value in row] for row in q_matrix(mask)]
    n = len(q)
    ident = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    b = ident
    coeffs: list[Fraction] = [Fraction(1)]
    for k in range(1, n + 1):
        qb = mat_mul(q, b)
        c = -sum(qb[i][i] for i in range(n)) / k
        coeffs.append(c)
        b = [
            [qb[i][j] + (c if i == j else 0) for j in range(n)]
            for i in range(n)
        ]
    out = []
    for coeff in coeffs:
        assert coeff.denominator == 1
        out.append(int(coeff))
    return out


def trim(poly: list[Fraction]) -> list[Fraction]:
    i = 0
    while i < len(poly) - 1 and poly[i] == 0:
        i += 1
    return poly[i:]


def derivative(poly: list[Fraction]) -> list[Fraction]:
    degree = len(poly) - 1
    if degree <= 0:
        return [Fraction(0)]
    return [poly[i] * (degree - i) for i in range(degree)]


def divrem_poly(
    a: list[Fraction], b: list[Fraction]
) -> tuple[list[Fraction], list[Fraction]]:
    a = trim(a[:])
    b = trim(b[:])
    if b == [0]:
        raise ZeroDivisionError
    quotient = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        factor = a[0] / b[0]
        pos = len(a) - len(b)
        quotient[len(quotient) - pos - 1] = factor
        subtraction = [factor * x for x in b] + [Fraction(0)] * pos
        a = trim(
            [
                x - y
                for x, y in zip(
                    a + [Fraction(0)] * (len(subtraction) - len(a)), subtraction
                )
            ]
        )
    return trim(quotient), trim(a)


def sturm_sequence(coeffs: list[int]) -> list[list[Fraction]]:
    sequence = [
        trim([Fraction(c) for c in coeffs]),
        trim(derivative([Fraction(c) for c in coeffs])),
    ]
    while sequence[-1] != [0]:
        _, remainder = divrem_poly(sequence[-2], sequence[-1])
        if remainder == [0]:
            break
        sequence.append([-x for x in remainder])
    return sequence


def poly_eval(poly: list[Fraction], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coeff in poly:
        value = value * x + coeff
    return value


def sign_at(poly: list[Fraction], x: Fraction) -> int:
    value = poly_eval(poly, x)
    return (value > 0) - (value < 0)


def variations(signs: list[int]) -> int:
    nonzero = [sign for sign in signs if sign]
    return sum(1 for a, b in zip(nonzero, nonzero[1:]) if a != b)


def count_roots(coeffs: list[int], lo: Fraction, hi: Fraction) -> int:
    sequence = sturm_sequence(coeffs)
    return variations([sign_at(poly, lo) for poly in sequence]) - variations(
        [sign_at(poly, hi) for poly in sequence]
    )


def root_bound(coeffs: list[int]) -> Fraction:
    return Fraction(1 + max(abs(c) for c in coeffs[1:]), 1)


def roots_in_largest_interval(coeffs: list[int]) -> dict[str, object]:
    return {
        "lower": f"{CANDIDATE_LOWER.numerator}/{CANDIDATE_LOWER.denominator}",
        "upper": f"{CANDIDATE_UPPER.numerator}/{CANDIDATE_UPPER.denominator}",
        "roots_in_interval": count_roots(
            coeffs, CANDIDATE_LOWER, CANDIDATE_UPPER
        ),
        "roots_above_upper": count_roots(coeffs, CANDIDATE_UPPER, root_bound(coeffs)),
    }


def is_triangle_free(mask: int, n: int) -> bool:
    for a, b, c in combinations(range(n), 3):
        if has_edge(mask, a, b, n) and has_edge(mask, a, c, n) and has_edge(
            mask, b, c, n
        ):
            return False
    return True


def h_representatives(order: int, t: int) -> list[int]:
    target = t - 1
    required = [target] * order
    if t % 2 == 0 and order % 2 == 1:
        required = [target] * (order - 1) + [target - 1]
    required = sorted(required, reverse=True)

    seen: dict[str, int] = {}
    for mask in range(1 << len(edge_order(order))):
        if degree_sequence(mask, order) != required:
            continue
        if not is_triangle_free(mask, order):
            continue
        seen.setdefault(canonical_label(mask, order), mask)
    return list(seen.values())


def build_l_graph(h_mask: int) -> int:
    edges: list[tuple[int, int]] = []
    clique = range(S - 1)
    h_vertices = range(S - 1, N)
    for i, j in combinations(clique, 2):
        edges.append((i, j))
    for i in clique:
        for j in h_vertices:
            edges.append((i, j))
    for idx, (i, j) in enumerate(edge_order(N - S + 1)):
        if h_mask & (1 << idx):
            edges.append((i + S - 1, j + S - 1))
    return mask_from_edges(N, edges)


def build_y_graph(h_mask: int) -> int:
    edges: list[tuple[int, int]] = []
    independent = range(T - 1)
    h_vertices = range(T - 1, N)
    for i in independent:
        for j in h_vertices:
            edges.append((i, j))
    for idx, (i, j) in enumerate(edge_order(N - T + 1)):
        if h_mask & (1 << idx):
            edges.append((i + T - 1, j + T - 1))
    return mask_from_edges(N, edges)


def poly_at_int(coeffs: list[int], x: int) -> int:
    value = 0
    for coeff in coeffs:
        value = value * x + coeff
    return value


def record_graph(mask: int) -> dict[str, object]:
    coeffs = charpoly_coeffs_q(mask)
    return {
        "canonical_label": canonical_label6(mask),
        "edge_count": edge_count(mask),
        "degree_sequence": degree_sequence(mask),
        "edges": edges_of(mask),
        "q_matrix": q_matrix(mask),
        "charpoly_det_xI_minus_Q": coeffs,
        "k33plus_witness_count": len(k33plus_witnesses(mask)),
        "k33plus_first_witnesses": k33plus_witnesses(mask)[:5],
    }


def verify() -> dict[str, object]:
    labelled_total = 1 << len(EDGES6)
    canonical_reps, canonical_by_mask = canonical_orbits6()
    free_canonical: dict[str, int] = {}
    free_labelled = 0

    for mask in range(labelled_total):
        if not k33plus_witnesses(mask):
            free_labelled += 1
            label = canonical_by_mask[mask]
            free_canonical.setdefault(label, mask)

    candidate = mask_from_edges(N, EXPECTED_CANDIDATE_EDGES)
    candidate_record = record_graph(candidate)
    candidate_coeffs = candidate_record["charpoly_det_xI_minus_Q"]

    assert labelled_total == 32768
    assert len(canonical_reps) == 156
    assert free_labelled == 32237
    assert len(free_canonical) == 147
    assert len(PERM_MAPS6) == 720
    assert candidate_record["canonical_label"] == EXPECTED_CANDIDATE_LABEL
    assert candidate_record["edge_count"] == 12
    assert candidate_record["degree_sequence"] == [5, 5, 4, 4, 4, 2]
    assert candidate_record["k33plus_witness_count"] == 0
    assert candidate_coeffs == EXPECTED_CANDIDATE_CHARPOLY
    assert roots_in_largest_interval(candidate_coeffs) == {
        "lower": "21513853/2500000",
        "upper": "86055613/10000000",
        "roots_in_interval": 1,
        "roots_above_upper": 0,
    }

    competitor_labels_above_threshold = []
    for label, mask in sorted(free_canonical.items()):
        if label == EXPECTED_CANDIDATE_LABEL:
            continue
        coeffs = charpoly_coeffs_q(mask)
        if count_roots(coeffs, CANDIDATE_LOWER, root_bound(coeffs)) != 0:
            competitor_labels_above_threshold.append(label)
    assert competitor_labels_above_threshold == []

    h_l = h_representatives(N - S + 1, T)
    h_y = h_representatives(N - T + 1, T)
    assert len(h_l) == len(h_y) == 1

    l_mask = build_l_graph(h_l[0])
    y_mask = build_y_graph(h_y[0])
    l_record = record_graph(l_mask)
    y_record = record_graph(y_mask)
    family_labels = {l_record["canonical_label"], y_record["canonical_label"]}

    assert l_record["edge_count"] == 13
    assert l_record["k33plus_witness_count"] > 0
    assert y_record["edge_count"] == 12
    assert y_record["degree_sequence"] == [4, 4, 4, 4, 4, 4]
    assert y_record["charpoly_det_xI_minus_Q"] == EXPECTED_Y_CHARPOLY
    assert poly_at_int(EXPECTED_Y_CHARPOLY, 8) == 0
    assert count_roots(EXPECTED_Y_CHARPOLY, Fraction(8), root_bound(EXPECTED_Y_CHARPOLY)) == 0
    assert EXPECTED_CANDIDATE_LABEL not in family_labels

    summary = {
        "verdict": "DISPROVED",
        "scope": "boundary case s=t=3,n=6 for Conjecture 5.1",
        "denominator": {
            "labelled_simple_graphs": labelled_total,
            "canonical_unlabelled_graphs": len(canonical_reps),
            "k33plus_free_labelled_graphs": free_labelled,
            "k33plus_free_canonical_graphs": len(free_canonical),
            "vertex_permutations_for_canonical_label": len(PERM_MAPS6),
            "forbidden_embedding_side_checks_per_labelled_graph": 20,
            "forbidden_embedding_side_plus_edge_checks_per_labelled_graph": 60,
        },
        "canonical_label_definition": {
            "edge_order": EDGES6,
            "label": "lexicographically minimum 15-bit upper-triangle edge string over all 6! vertex permutations",
        },
        "counterexample": {
            **candidate_record,
            "description": "K2 join (K3 union K1)",
            "charpoly_factor": "(x^2 - 10x + 12)(x^4 - 14x^3 + 73x^2 - 168x + 144)",
            "q_exact": "5 + sqrt(13)",
            "largest_root_interval": roots_in_largest_interval(candidate_coeffs),
        },
        "family_comparators": [
            {
                **l_record,
                "family": "L_6_3_3",
                "description": "K2 join C4",
                "is_k33plus_free": False,
            },
            {
                **y_record,
                "family": "Y_6_3",
                "description": "I2 join C4",
                "is_k33plus_free": True,
                "q_exact": "8",
            },
        ],
        "maximality_check": {
            "method": "exact characteristic polynomials and Sturm root counts",
            "candidate_lower_bound": "21513853/2500000",
            "non_candidate_free_classes_with_root_above_candidate_lower_bound": 0,
            "unique_extremal_unlabelled_class": True,
        },
        "belongs_to_L_or_Y": False,
        "random_seed": None,
    }
    return summary


def main() -> None:
    summary = verify()
    OUTPUT.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
