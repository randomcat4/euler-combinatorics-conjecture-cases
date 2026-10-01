#!/usr/bin/env python3
"""Finite checker for the two cyclic-partition encodings.

Improper partition matrices and restricted inversion sequences are
enumerated independently.  Only the Python standard library is used.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "results.json"
MAX_N = 8

# Matrix representation: (dimension, original column lengths, row of each label).
Matrix = tuple[int, tuple[int, ...], tuple[int, ...]]
# Cycle representation: ordered blocks, rotated so the block containing 1 is first.
Cycle = tuple[tuple[int, ...], ...]


def compositions(n: int, parts: int):
    if parts == 1:
        yield (n,)
        return
    for first in range(1, n - parts + 2):
        for rest in compositions(n - first, parts - 1):
            yield (first,) + rest


def enumerate_matrices(n: int) -> tuple[Matrix, ...]:
    out = []
    for dim in range(1, n + 1):
        for lengths in compositions(n, dim):
            group_columns = []
            choices = []
            for col, length in enumerate(lengths):
                groups = (length + 1) // 2
                group_columns.extend([col] * groups)
                choices.extend([range(col + 1)] * groups)
            for group_rows in itertools.product(*choices):
                if set(group_rows) != set(range(dim)):
                    continue
                rows = []
                offset = 0
                for col, length in enumerate(lengths):
                    groups = (length + 1) // 2
                    local = group_rows[offset : offset + groups]
                    offset += groups
                    for g, row in enumerate(local):
                        repeat = 1 if length % 2 and g == groups - 1 else 2
                        rows.extend([row] * repeat)
                assert len(rows) == n
                out.append((dim, lengths, tuple(rows)))
    assert len(set(out)) == len(out)
    return tuple(out)


def collapse(matrix: Matrix):
    dim, lengths, rows = matrix
    collapsed_rows = []
    collapsed_lengths = []
    odd = []
    pos = 0
    for col, length in enumerate(lengths):
        local = rows[pos : pos + length]
        pos += length
        m = (length + 1) // 2
        collapsed_lengths.append(m)
        odd.append(length % 2)
        for g in range(m):
            collapsed_rows.append(local[2 * g])
            if 2 * g + 1 < length:
                assert local[2 * g] == local[2 * g + 1]
    return dim, tuple(collapsed_lengths), tuple(collapsed_rows), tuple(odd)


def canonical_cycle(blocks) -> Cycle:
    blocks = [tuple(sorted(block)) for block in blocks]
    idx = next(i for i, block in enumerate(blocks) if 1 in block)
    return tuple(blocks[idx:] + blocks[:idx])


def cycle_word(cycle: Cycle, start_largest: bool = True) -> tuple[int, ...]:
    blocks = list(cycle)
    if start_largest:
        largest = max(x for block in blocks for x in block)
        idx = next(i for i, block in enumerate(blocks) if largest in block)
        blocks = blocks[idx:] + blocks[:idx]
    return tuple(x for block in blocks for x in sorted(block, reverse=True))


def word_with_kept_edges_to_cycle(word: tuple[int, ...], kept: set[tuple[int, int]]) -> Cycle:
    h = len(word)
    cut_indices = [i for i in range(h) if (word[i], word[(i + 1) % h]) not in kept]
    assert cut_indices
    start = (cut_indices[0] + 1) % h
    blocks = []
    current = []
    for step in range(h):
        i = (start + step) % h
        current.append(word[i])
        edge = (word[i], word[(i + 1) % h])
        if edge not in kept:
            blocks.append(tuple(current))
            current = []
    assert not current
    return canonical_cycle(blocks)


def matrix_to_cycle(matrix: Matrix) -> Cycle:
    dim, col_lengths, rows, odd = collapse(matrix)
    k = len(rows)
    starts = []
    running = 1
    for length in col_lengths:
        starts.append(running)
        running += length
    sigma: list[int] = []
    for a in range(1, k + 1):
        anchor = starts[rows[a - 1]] - 1
        if anchor == 0:
            sigma.append(a)
        else:
            sigma.insert(sigma.index(anchor), a)
    assert sorted(sigma) == list(range(1, k + 1))
    omega = (k + 1,) + tuple(sigma)
    kept: set[tuple[int, int]] = set()
    for col in range(dim - 1):
        if odd[col]:
            bottom = starts[col + 1] - 1
            i = omega.index(bottom)
            kept.add((omega[i - 1], bottom))
    if odd[-1]:
        kept.add((k + 1, sigma[0]))
    assert all(a > b for a, b in kept)
    cycle = word_with_kept_edges_to_cycle(omega, kept)
    assert len(cycle) == k + 1 - sum(odd)
    return cycle


def first_smaller_right(sigma: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(next((b for b in sigma[i + 1 :] if b < a), 0) for i, a in enumerate(sigma))


def cycle_to_matrix(cycle: Cycle) -> Matrix:
    k = max(x for block in cycle for x in block) - 1
    word = cycle_word(cycle)
    assert word[0] == k + 1
    sigma = word[1:]
    f_by_position = first_smaller_right(sigma)
    f = {a: fa for a, fa in zip(sigma, f_by_position)}
    y = sorted(set(f.values()))
    assert y[0] == 0
    dim = len(y)
    bounds = y + [k]
    row_index = {value: i for i, value in enumerate(y)}
    collapsed_lengths = [0] * dim
    collapsed_rows = [0] * k
    for a in range(1, k + 1):
        col = next(j for j in range(dim) if bounds[j] < a <= bounds[j + 1])
        row = row_index[f[a]]
        assert row <= col
        collapsed_lengths[col] += 1
        collapsed_rows[a - 1] = row
    assert all(collapsed_lengths)

    block_of = {x: i for i, block in enumerate(cycle) for x in block}
    odd = []
    for col in range(dim - 1):
        bottom = y[col + 1]
        i = word.index(bottom)
        odd.append(int(block_of[word[i - 1]] == block_of[bottom]))
    odd.append(int(block_of[k + 1] == block_of[sigma[0]]))

    lengths = []
    rows = []
    pos = 0
    for col, m in enumerate(collapsed_lengths):
        length = 2 * m - odd[col]
        lengths.append(length)
        local = collapsed_rows[pos : pos + m]
        pos += m
        for g, row in enumerate(local):
            repeat = 1 if odd[col] and g == m - 1 else 2
            rows.extend([row] * repeat)
    return dim, tuple(lengths), tuple(rows)


def restricted(e: tuple[int, ...]) -> bool:
    for value in set(e):
        positions = [i for i, x in enumerate(e) if x == value]
        if len(positions) > 2 or positions != list(range(positions[0], positions[-1] + 1)):
            return False
    return True


def enumerate_sequences(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(e for e in itertools.product(*(range(i) for i in range(1, n + 1))) if restricted(e))


@lru_cache(maxsize=None)
def sequence_to_cycle(e: tuple[int, ...]) -> Cycle:
    if not e:
        return ((1,),)
    a = e[-1]
    eps = 2 if len(e) >= 2 and e[-2] == a else 1
    prefix = e[:-eps]
    assert a not in prefix
    k = len(set(e))
    available = [x for x in range(len(prefix) + 1) if x not in prefix]
    j = available.index(a)
    blocks = [set(block) for block in sequence_to_cycle(prefix)]
    if eps == 1:
        blocks[j].add(k + 1)
    else:
        blocks.insert(j, {k + 1})
    return canonical_cycle(blocks)


@lru_cache(maxsize=None)
def cycle_to_sequence(cycle: Cycle) -> tuple[int, ...]:
    if cycle == ((1,),):
        return ()
    largest = max(x for block in cycle for x in block)
    blocks = [set(block) for block in cycle]
    i = next(i for i, block in enumerate(blocks) if largest in block)
    if len(blocks[i]) > 1:
        blocks[i].remove(largest)
        selected = frozenset(blocks[i])
        eps = 1
    else:
        blocks.pop(i)
        selected = frozenset(blocks[i % len(blocks)])
        eps = 2
    smaller = canonical_cycle(blocks)
    prefix = cycle_to_sequence(smaller)
    selected_index = next(i for i, block in enumerate(smaller) if frozenset(block) == selected)
    available = [x for x in range(len(prefix) + 1) if x not in prefix]
    value = available[selected_index]
    answer = prefix + (value,) * eps
    assert restricted(answer)
    return answer


def all_cycles(h: int, q: int) -> tuple[Cycle, ...]:
    rg_strings = []

    def rec(prefix: tuple[int, ...], current_max: int):
        if len(prefix) == h:
            if current_max + 1 == q:
                rg_strings.append(prefix)
            return
        for x in range(min(current_max + 1, q - 1) + 1):
            rec(prefix + (x,), max(current_max, x))

    rec((0,), 0)
    cycles = set()
    for rg in rg_strings:
        blocks = [tuple(i + 1 for i, b in enumerate(rg) if b == j) for j in range(q)]
        root = next(block for block in blocks if 1 in block)
        others = [block for block in blocks if block != root]
        for perm in itertools.permutations(others):
            cycles.add((root,) + perm)
    return tuple(sorted(cycles))


def cycle_signature(cycle: Cycle) -> tuple[int, tuple[int, ...]]:
    word = cycle_word(cycle)
    largest = word[0]
    block_of = {x: i for i, block in enumerate(cycle) for x in block}
    descents = []
    for i, a in enumerate(word):
        b = word[(i + 1) % len(word)]
        if a > b:
            descents.append((a, b, int(block_of[a] == block_of[b])))
    other = sorted((edge for edge in descents if edge[0] != largest), key=lambda x: x[1])
    terminal = [edge for edge in descents if edge[0] == largest]
    assert len(terminal) == 1
    signature = tuple(edge[2] for edge in other + terminal)
    return len(descents), signature


@lru_cache(maxsize=None)
def eulerian(n: int, d: int) -> int:
    if n == 0:
        return int(d == 0)
    if d < 0 or d >= n:
        return 0
    return (n - d) * eulerian(n - 1, d - 1) + (d + 1) * eulerian(n - 1, d)


@lru_cache(maxsize=None)
def stirling2(n: int, q: int) -> int:
    if n == q == 0:
        return 1
    if n == 0 or q == 0:
        return 0
    return q * stirling2(n - 1, q) + stirling2(n - 1, q - 1)


def main() -> None:
    per_n = []
    signature_counts = Counter()
    state_counts = Counter()
    for n in range(1, MAX_N + 1):
        matrices = enumerate_matrices(n)
        sequences = enumerate_sequences(n)
        assert len(matrices) == len(sequences)
        m_cycles = defaultdict(set)
        b_cycles = defaultdict(set)

        for matrix in matrices:
            dim, lengths, _ = matrix
            k = sum((length + 1) // 2 for length in lengths)
            cycle = matrix_to_cycle(matrix)
            assert cycle_to_matrix(cycle) == matrix
            m_cycles[k].add(cycle)
            cdim, signature = cycle_signature(cycle)
            parity = tuple(length % 2 for length in lengths)
            assert cdim == dim and signature == parity
            signature_counts[k, dim, signature] += 1
            minus = int(lengths[-1] % 2 == 1)
            state_counts[n, k, dim, minus] += 1
            seq = cycle_to_sequence(cycle)
            assert sequence_to_cycle(seq) == cycle
            assert len(seq) == n and len(set(seq)) == k
            assert int(seq[-1] != seq[-2] if n > 1 else True) == minus

        for seq in sequences:
            k = len(set(seq))
            cycle = sequence_to_cycle(seq)
            assert cycle_to_sequence(cycle) == seq
            b_cycles[k].add(cycle)
            matrix = cycle_to_matrix(cycle)
            assert matrix_to_cycle(matrix) == cycle
            assert sum(matrix[1]) == n

        parameter_rows = []
        for k in sorted(set(m_cycles) | set(b_cycles)):
            q = n - k + 1
            expected = set(all_cycles(k + 1, q))
            assert m_cycles[k] == expected
            assert b_cycles[k] == expected
            full_formula = math.factorial(n - k) * stirling2(k + 1, q)
            minus_formula = math.factorial(q) * stirling2(k, q)
            full_count = len(expected)
            minus_count = sum(1 for c in expected if len(next(b for b in c if k + 1 in b)) > 1)
            assert full_count == full_formula and minus_count == minus_formula
            parameter_rows.append(
                {
                    "k": k,
                    "q": q,
                    "objects": full_count,
                    "minus_objects": minus_count,
                    "all_cycles_covered_by_both_encoders": True,
                }
            )
        per_n.append(
            {
                "n": n,
                "matrices": len(matrices),
                "restricted_inversion_sequences": len(sequences),
                "parameters": parameter_rows,
                "both_round_trips": True,
                "full_signature_pointwise": True,
            }
        )

    for (k, dim, signature), count in signature_counts.items():
        assert count == eulerian(k, dim - 1)
    for (n, k, dim, minus), count in state_counts.items():
        t = 2 * k - n
        choose = math.comb(dim - 1, t - minus) if 0 <= t - minus <= dim - 1 else 0
        assert count == eulerian(k, dim - 1) * choose

    result = {
        "problem": "improper-partition-matrix-cyclic-bijection",
        "status": "PASS_FINITE_EXACT",
        "claim_scope": "two cyclic-partition encodings for improper partition matrices and restricted inversion sequences",
        "coverage": {
            "n_range": [1, MAX_N],
            "matrix_side": "direct enumeration from column intervals, upper triangular rows, and improper local pairs",
            "sequence_side": "all inversion sequences filtered for consecutive runs of length at most two",
            "cycle_side": "all set partitions and all cyclic block orders",
            "checks": [
                "M and M_inverse in both directions",
                "B and B_inverse in both directions",
                "both images equal every cyclic partition at each parameter",
                "minus terminal state",
                "dimension and full ordered column-parity signature pointwise",
                "Eulerian signature count and refined terminal-state count",
                "Stirling full and minus counts",
            ],
        },
        "per_n": per_n,
        "signature_parameter_cases": len(signature_counts),
        "terminal_parameter_cases": len(state_counts),
    }
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"problem": result["problem"], "status": result["status"]}, ensure_ascii=False))
    print("totals_n1_to_n8", [row["matrices"] for row in per_n])


if __name__ == "__main__":
    main()
