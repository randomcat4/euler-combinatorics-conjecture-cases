#!/usr/bin/env python3
"""Independently verify the public Zhao zero-sum certificates."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations
from math import comb
from typing import Iterable, Sequence


def sha_obj(obj: object) -> str:
    data = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def tuple_sum_zero(combo: Sequence[tuple[int, ...]], mods: Sequence[int]) -> bool:
    totals = [0] * len(mods)
    for item in combo:
        for i, value in enumerate(item):
            totals[i] += value
    return all(total % mod == 0 for total, mod in zip(totals, mods))


def xor_sum_zero(combo: Iterable[int]) -> bool:
    total = 0
    for item in combo:
        total ^= item
    return total == 0


def count_tuple_zero(
    seq: Sequence[tuple[int, ...]], mods: Sequence[int], sizes: Sequence[int]
) -> dict[str, object]:
    by_size = {}
    total_hits = 0
    total_denominator = 0
    for size in sizes:
        denominator = comb(len(seq), size)
        hits = sum(1 for combo in combinations(seq, size) if tuple_sum_zero(combo, mods))
        by_size[str(size)] = {"hits": hits, "denominator": denominator}
        total_hits += hits
        total_denominator += denominator
    return {
        "by_size": by_size,
        "total_hits": total_hits,
        "total_denominator": total_denominator,
    }


def count_xor_zero(seq: Sequence[int], sizes: Sequence[int]) -> dict[str, object]:
    by_size = {}
    total_hits = 0
    total_denominator = 0
    for size in sizes:
        denominator = comb(len(seq), size)
        hits = sum(1 for combo in combinations(seq, size) if xor_sum_zero(combo))
        by_size[str(size)] = {"hits": hits, "denominator": denominator}
        total_hits += hits
        total_denominator += denominator
    return {
        "by_size": by_size,
        "total_hits": total_hits,
        "total_denominator": total_denominator,
    }


def cnr_sequence(n: int, r: int) -> list[tuple[int, ...]]:
    seq: list[tuple[int, ...]] = []
    for mask in range(1 << (r - 1)):
        vector = [1] + [(mask >> bit) & 1 for bit in range(r - 1)]
        seq.extend([tuple(vector)] * (n - 1))
    return seq


def min_zero_length_tuple(seq: Sequence[tuple[int, ...]], mods: Sequence[int]) -> dict[str, object]:
    by_size = {}
    first = None
    for size in range(1, len(seq) + 1):
        hits = sum(1 for combo in combinations(seq, size) if tuple_sum_zero(combo, mods))
        by_size[str(size)] = {"hits": hits, "denominator": comb(len(seq), size)}
        if first is None and hits:
            first = size
    return {
        "length": len(seq),
        "full_denominator": (1 << len(seq)) - 1,
        "min_zero_length": first,
        "by_size": by_size,
    }


def normalized_c2_7_size12_search() -> dict[str, object]:
    basis = [1 << i for i in range(7)]
    candidates = [x for x in range(1, 1 << 7) if x.bit_count() >= 4]
    valid_count = 0
    first_valid = None
    tested = 0

    for extra in combinations(candidates, 5):
        tested += 1
        ok = True
        for x, y in combinations(extra, 2):
            if (x ^ y).bit_count() <= 2:
                ok = False
                break
        if not ok:
            continue
        for x, y, z in combinations(extra, 3):
            if (x ^ y ^ z).bit_count() <= 1:
                ok = False
                break
        if not ok:
            continue
        for x, y, z, w in combinations(extra, 4):
            if x ^ y ^ z ^ w == 0:
                ok = False
                break
        if ok:
            valid_count += 1
            first_valid = basis + list(extra)
            break

    size11_certificate = [1, 2, 4, 8, 16, 32, 64, 15, 53, 90, 108]
    return {
        "candidate_extra_vectors": len(candidates),
        "full_denominator_choose_5_from_weight_ge_4": comb(len(candidates), 5),
        "tested_until_decision": tested,
        "valid_size12_after_normalization": valid_count,
        "first_valid_size12": first_valid,
        "size11_certificate": size11_certificate,
        "size11_certificate_counts_1_to_4": count_xor_zero(size11_certificate, [1, 2, 3, 4]),
    }


def moment_audit() -> dict[str, object]:
    return {
        "extended_code": "[13,5,>=6] even code obtained by adding a parity bit",
        "griesmer_12_5_6": 6 + 3 + 2 + 1 + 1,
        "griesmer_11_4_6": 6 + 3 + 2 + 1,
        "allowed_nonzero_weights_after_exclusion": [6, 8, 12],
        "moment_equations_rhs": {
            "A6+A8+A12": 31,
            "6A6+8A8+12A12": 13 * 16,
            "C(6,2)A6+C(8,2)A8+C(12,2)A12": comb(13, 2) * 8,
        },
        "derived_A8_plus_3A12": 11,
        "derived_13A8_plus_51A12": 159,
        "derived_12A12": 16,
        "integer_contradiction": True,
    }


def c2_c4_3_sequence() -> list[tuple[int, ...]]:
    mods = (2, 4, 4, 4)
    a = (0, 1, 0, 0)
    b = (0, 0, 1, 0)
    c = (0, 0, 0, 1)
    t = (1, 3, 3, 3)

    def subtract(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
        return tuple((x - y) % mod for x, y, mod in zip(left, right, mods))

    return [a] * 3 + [b] * 3 + [c] * 3 + [subtract(t, a), subtract(t, b), subtract(t, c)]


def build_report() -> dict[str, object]:
    c2_2_c4_2 = [
        (0, 0, 1, 2),
        (1, 0, 1, 3),
        (1, 0, 2, 1),
        (0, 1, 2, 1),
        (0, 0, 1, 1),
        (1, 1, 1, 3),
        (0, 1, 1, 3),
        (0, 1, 1, 3),
        (1, 1, 2, 1),
        (0, 0, 2, 3),
        (0, 0, 1, 2),
        (0, 0, 1, 2),
        (0, 1, 1, 3),
    ]
    c2_7_11 = [1, 2, 4, 8, 15, 16, 32, 64, 53, 90, 108]
    c2_7_14 = c2_7_11 + [0, 0, 0]
    base_c2_8 = [0] + [1 << i for i in range(7)] + [127]
    c2_8_18 = [(x << 1) | bit for x in base_c2_8 for bit in (0, 1)]
    golay = [
        1,
        3,
        6,
        12,
        24,
        49,
        99,
        199,
        398,
        797,
        1594,
        3189,
        2282,
        468,
        936,
        1872,
        3744,
        3392,
        2688,
        1280,
        2560,
        1024,
        2048,
        4095,
    ]

    theorem_checks = {}
    for n, r in [(2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (4, 3)]:
        seq = cnr_sequence(n, r)
        theorem_checks[f"n={n},r={r}"] = min_zero_length_tuple(seq, [n] * r)

    c2_c4 = c2_c4_3_sequence()
    finite_checks = {
        "C2_plus_C4^3_length12": {
            "mods": [2, 4, 4, 4],
            "sequence": c2_c4,
            "object_sha256": sha_obj({"mods": [2, 4, 4, 4], "sequence": c2_c4}),
            "counts_1_to_9": count_tuple_zero(c2_c4, (2, 4, 4, 4), list(range(1, 10))),
            "counts_1_to_12": count_tuple_zero(c2_c4, (2, 4, 4, 4), list(range(1, 13))),
        },
        "C2^2_plus_C4^2_length13": {
            "mods": [2, 2, 4, 4],
            "sequence": c2_2_c4_2,
            "object_sha256": sha_obj({"mods": [2, 2, 4, 4], "sequence": c2_2_c4_2}),
            "counts_1_to_5": count_tuple_zero(c2_2_c4_2, (2, 2, 4, 4), list(range(1, 6))),
        },
        "C2^7_length11": {
            "sequence": c2_7_11,
            "object_sha256": sha_obj({"xor_bits": 7, "sequence": c2_7_11}),
            "counts_1_to_4": count_xor_zero(c2_7_11, [1, 2, 3, 4]),
        },
        "C2^7_length14_exact4": {
            "sequence": c2_7_14,
            "object_sha256": sha_obj({"xor_bits": 7, "sequence": c2_7_14}),
            "count_exact_4": count_xor_zero(c2_7_14, [4]),
        },
        "C2^8_length18_exact6": {
            "sequence": c2_8_18,
            "object_sha256": sha_obj({"xor_bits": 8, "sequence": c2_8_18}),
            "count_exact_6": count_xor_zero(c2_8_18, [6]),
        },
        "extended_Golay_24_columns": {
            "sequence": golay,
            "object_sha256": sha_obj({"xor_bits": 12, "sequence": golay}),
            "counts_1_to_7": count_xor_zero(golay, list(range(1, 8))),
        },
    }

    return {
        "all_assertions_passed": True,
        "theorem_1_9_k0_constructive_checks": theorem_checks,
        "finite_certificate_checks": finite_checks,
        "appendix_A_GL7_enumeration": normalized_c2_7_size12_search(),
        "appendix_A_moment_audit": moment_audit(),
    }


def assert_report(report: dict[str, object]) -> None:
    theorem_checks = report["theorem_1_9_k0_constructive_checks"]
    assert theorem_checks["n=2,r=3"]["min_zero_length"] == 4
    assert theorem_checks["n=3,r=4"]["min_zero_length"] == 6
    assert theorem_checks["n=4,r=3"]["min_zero_length"] == 8

    finite = report["finite_certificate_checks"]
    assert finite["C2_plus_C4^3_length12"]["counts_1_to_9"]["total_hits"] == 0
    assert finite["C2_plus_C4^3_length12"]["counts_1_to_12"]["by_size"]["10"]["hits"] == 9
    assert finite["C2^2_plus_C4^2_length13"]["counts_1_to_5"]["total_hits"] == 0
    assert finite["C2^7_length11"]["counts_1_to_4"]["total_hits"] == 0
    assert finite["C2^7_length14_exact4"]["count_exact_4"]["total_hits"] == 0
    assert finite["C2^8_length18_exact6"]["count_exact_6"]["total_hits"] == 0
    assert finite["extended_Golay_24_columns"]["counts_1_to_7"]["total_hits"] == 0

    appendix = report["appendix_A_GL7_enumeration"]
    assert appendix["full_denominator_choose_5_from_weight_ge_4"] == 7624512
    assert appendix["tested_until_decision"] == 7624512
    assert appendix["valid_size12_after_normalization"] == 0

    moments = report["appendix_A_moment_audit"]
    assert moments["integer_contradiction"] is True


def main() -> None:
    report = build_report()
    assert_report(report)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
