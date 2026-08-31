"""Exhaustively calibrate the explicit bijection for sizes at most eight.

This program verifies the structural maps and both inverses against an
independent enumeration of the restricted inversion sequences. It is not a
replacement for the all-order proof.
"""

from __future__ import annotations

from bisect import bisect_left
from collections import defaultdict
from itertools import combinations, product


def inversion_tables(k: int):
    yield from product(*(range(i) for i in range(1, k + 1)))


def block_factor(e: tuple[int, ...]):
    values: list[int] = []
    multiplicities: list[int] = []
    i = 0
    while i < len(e):
        value = e[i]
        multiplicity = 2 if i + 1 < len(e) and e[i + 1] == value else 1
        values.append(value)
        multiplicities.append(multiplicity)
        i += multiplicity
    return tuple(values), tuple(multiplicities)


def in_restricted_class(e: tuple[int, ...]) -> bool:
    positions: dict[int, list[int]] = defaultdict(list)
    for i, value in enumerate(e, 1):
        if not 0 <= value < i:
            return False
        positions[value].append(i)
    return all(
        len(pos) <= 2 and (len(pos) < 2 or pos[1] == pos[0] + 1)
        for pos in positions.values()
    )


def is_minus(e: tuple[int, ...]) -> bool:
    return len(e) == 1 or e[-2] != e[-1]


def canonical_cycle(blocks):
    blocks = tuple(frozenset(block) for block in blocks)
    starts = [i for i, block in enumerate(blocks) if 1 in block]
    assert blocks and all(blocks) and len(starts) == 1
    start = starts[0]
    return blocks[start:] + blocks[:start]


def full_to_cycle(e: tuple[int, ...]):
    assert in_restricted_class(e)
    if not e:
        return (frozenset({1}),)
    values, multiplicities = block_factor(e)
    distinct = len(values)
    if multiplicities[-1] == 2:
        h = e[:-1]
        linear = minus_to_ordered_partition(h)
        return canonical_cycle((frozenset({distinct + 1}),) + linear)

    prefix = e[:-1]
    cycle = list(full_to_cycle(prefix))
    unused = sorted(set(range(len(e))) - set(prefix))
    index = unused.index(e[-1])
    cycle[index] = frozenset(set(cycle[index]) | {distinct + 1})
    return canonical_cycle(cycle)


def minus_to_ordered_partition(e: tuple[int, ...]):
    assert e and in_restricted_class(e) and is_minus(e)
    values, _ = block_factor(e)
    distinct = len(values)
    prefix = e[:-1]
    cycle = full_to_cycle(prefix)
    unused = sorted(set(range(len(e))) - set(prefix))
    index = unused.index(e[-1])
    assert max(set().union(*cycle)) == distinct
    return cycle[index:] + cycle[:index]


def cycle_to_full(cycle):
    cycle = canonical_cycle(cycle)
    universe = set().union(*cycle)
    top = max(universe)
    assert universe == set(range(1, top + 1))
    if top == 1 and len(cycle) == 1 and cycle[0] == frozenset({1}):
        return ()

    distinct = top - 1
    block_count = len(cycle)
    top_index = next(i for i, block in enumerate(cycle) if top in block)
    top_block = cycle[top_index]
    if len(top_block) == 1:
        successor = (top_index + 1) % block_count
        remaining = [
            cycle[(successor + offset) % block_count]
            for offset in range(block_count - 1)
        ]
        h = ordered_partition_to_minus(tuple(remaining))
        return h + (h[-1],)

    reduced_block = frozenset(set(top_block) - {top})
    reduced = list(cycle)
    reduced[top_index] = reduced_block
    reduced_cycle = canonical_cycle(reduced)
    prefix = cycle_to_full(reduced_cycle)
    length = distinct + block_count - 1
    unused = sorted(set(range(length)) - set(prefix))
    index = reduced_cycle.index(reduced_block)
    return prefix + (unused[index],)


def ordered_partition_to_minus(linear):
    linear = tuple(frozenset(block) for block in linear)
    universe = set().union(*linear)
    distinct = max(universe)
    assert universe == set(range(1, distinct + 1))
    block_count = len(linear)
    cycle = canonical_cycle(linear)
    prefix = cycle_to_full(cycle)
    length = distinct + block_count - 1
    unused = sorted(set(range(length)) - set(prefix))
    index = cycle.index(linear[0])
    e = prefix + (unused[index],)
    assert in_restricted_class(e) and is_minus(e)
    return e


def table_to_permutation(table: tuple[int, ...]):
    word: list[int] = []
    for i, value in enumerate(table, 1):
        if value == 0:
            word.append(i)
        else:
            word.insert(word.index(value), i)
    return tuple(word)


def permutation_to_table(permutation: tuple[int, ...]):
    position = {value: i for i, value in enumerate(permutation)}
    table = []
    for value in range(1, len(permutation) + 1):
        tail = permutation[position[value] + 1 :]
        table.append(next((item for item in tail if item < value), 0))
    return tuple(table)


def column_maxima(table: tuple[int, ...]):
    alphabet = sorted(set(table))
    return tuple(alphabet[1:] + [len(table)])


def source_to_ordered_partition(
    table: tuple[int, ...], marked_columns: frozenset[int]
):
    maxima = column_maxima(table)
    dimension = len(maxima)
    assert dimension in marked_columns
    marked_bottoms = {
        maxima[column - 1] for column in marked_columns if column < dimension
    }
    permutation = table_to_permutation(table)
    blocks: list[list[int]] = [[permutation[0]]]
    for left, right in zip(permutation, permutation[1:]):
        if right in marked_bottoms:
            assert left > right
            blocks[-1].append(right)
        else:
            blocks.append([right])
    return tuple(frozenset(block) for block in blocks)


def ordered_partition_to_source(linear):
    linear = tuple(frozenset(block) for block in linear)
    parts = [tuple(sorted(block, reverse=True)) for block in linear]
    permutation = tuple(value for part in parts for value in part)
    marked_bottoms = {value for part in parts for value in part[1:]}
    table = permutation_to_table(permutation)
    alphabet = sorted(set(table))
    assert marked_bottoms <= set(alphabet[1:])
    marked_columns = {alphabet.index(value) for value in marked_bottoms}
    marked_columns.add(len(alphabet))
    return table, frozenset(marked_columns)


def lambda_matrix(table: tuple[int, ...]):
    size = len(table)
    alphabet = sorted(set(table))
    bounds = alphabet[1:] + [size]
    matrix: dict[tuple[int, int], set[int]] = defaultdict(set)
    for label, value in enumerate(table, 1):
        row = alphabet.index(value) + 1
        column = bisect_left(bounds, label) + 1
        assert row <= column
        matrix[row, column].add(label)
    return len(alphabet), dict(matrix)


def expand_source(table: tuple[int, ...], marked_columns: frozenset[int]):
    dimension, collapsed = lambda_matrix(table)
    assert dimension in marked_columns
    column_sizes = [
        sum(len(collapsed.get((row, column), ())) for row in range(1, dimension + 1))
        for column in range(1, dimension + 1)
    ]
    collapsed_prefix = [0]
    expanded_prefix = [0]
    for column, size in enumerate(column_sizes, 1):
        collapsed_prefix.append(collapsed_prefix[-1] + size)
        expanded_prefix.append(
            expanded_prefix[-1]
            + 2 * size
            - (1 if column in marked_columns else 0)
        )

    expanded: dict[tuple[int, int], set[int]] = defaultdict(set)
    for (row, column), labels in collapsed.items():
        column_size = column_sizes[column - 1]
        for label in labels:
            local = label - collapsed_prefix[column - 1]
            pair = [2 * local - 1, 2 * local]
            if column in marked_columns and local == column_size:
                pair.pop()
            expanded[row, column].update(
                expanded_prefix[column - 1] + value for value in pair
            )
    return dimension, dict(expanded)


def validate_source(dimension: int, matrix: dict[tuple[int, int], set[int]]):
    labels = set().union(*matrix.values())
    size = len(labels)
    assert labels == set(range(1, size + 1))
    assert all(row <= column for row, column in matrix)
    assert all(
        any(matrix.get((row, column)) for column in range(1, dimension + 1))
        for row in range(1, dimension + 1)
    )
    assert all(
        any(matrix.get((row, column)) for row in range(1, dimension + 1))
        for column in range(1, dimension + 1)
    )
    position = {
        label: (row, column)
        for (row, column), cell in matrix.items()
        for label in cell
    }
    assert all(position[i][1] <= position[i + 1][1] for i in range(1, size))
    for i in range(1, size):
        row_1, column_1 = position[i]
        row_2, column_2 = position[i + 1]
        if column_1 == column_2 and row_1 != row_2:
            column_minimum = min(
                label for label, (_, column) in position.items() if column == column_1
            )
            assert (i - column_minimum) % 2 == 1
    assert len(matrix[position[size]]) % 2 == 1
    statistic = 0
    for column in range(1, dimension + 1):
        column_size = sum(
            len(matrix.get((row, column), ())) for row in range(1, dimension + 1)
        )
        statistic += (column_size + 1) // 2
    return size, statistic


def reduce_source(dimension: int, matrix: dict[tuple[int, int], set[int]]):
    expanded_sizes = [
        sum(len(matrix.get((row, column), ())) for row in range(1, dimension + 1))
        for column in range(1, dimension + 1)
    ]
    expanded_prefix = [0]
    collapsed_prefix = [0]
    marked = set()
    collapsed: dict[tuple[int, int], set[int]] = defaultdict(set)
    for column, size in enumerate(expanded_sizes, 1):
        expanded_prefix.append(expanded_prefix[-1] + size)
        collapsed_size = (size + 1) // 2
        collapsed_prefix.append(collapsed_prefix[-1] + collapsed_size)
        if size % 2:
            marked.add(column)
        local_row = {}
        for (row, current_column), cell in matrix.items():
            if current_column == column:
                for label in cell:
                    local_row[label - expanded_prefix[column - 1]] = row
        for local in range(1, size, 2):
            assert local_row[local] == local_row[local + 1]
        for local, row in local_row.items():
            collapsed[row, column].add(
                collapsed_prefix[column - 1] + (local + 1) // 2
            )

    column_minima = {
        column: min(
            label
            for (row, current_column), cell in collapsed.items()
            if current_column == column
            for label in cell
        )
        for column in range(1, dimension + 1)
    }
    position = {
        label: (row, column)
        for (row, column), cell in collapsed.items()
        for label in cell
    }
    table = tuple(
        column_minima[position[label][0]] - 1
        for label in range(1, collapsed_prefix[-1] + 1)
    )
    return table, frozenset(marked)


def target_sequences(n: int):
    for e in inversion_tables(n):
        if in_restricted_class(e) and is_minus(e):
            yield e


def source_pairs(max_n: int):
    by_size: dict[int, list[tuple[tuple[int, ...], frozenset[int]]]] = defaultdict(list)
    for k in range(1, max_n + 1):
        for table in inversion_tables(k):
            dimension = len(set(table))
            for marked_count in range(1, dimension + 1):
                for chosen in combinations(range(1, dimension), marked_count - 1):
                    marked = frozenset((*chosen, dimension))
                    n = 2 * k - marked_count
                    if n <= max_n:
                        by_size[n].append((table, marked))
    return by_size


def main(max_n: int = 8):
    full_counts = []
    for n in range(max_n + 1):
        full_image = {}
        full = [()] if n == 0 else [
            e for e in inversion_tables(n) if in_restricted_class(e)
        ]
        for e in full:
            cycle = full_to_cycle(e)
            assert cycle_to_full(cycle) == e
            assert full_to_cycle(cycle_to_full(cycle)) == cycle
            key = (len(set(e)), len(cycle), cycle)
            assert key not in full_image
            full_image[key] = e
        full_counts.append(len(full))
    print("full-class counts n=0..8:", ",".join(map(str, full_counts)))

    sources = source_pairs(max_n)
    print("n source target dist-profile")
    for n in range(1, max_n + 1):
        image = {}
        source_profile: dict[int, int] = defaultdict(int)
        for table, marked in sources[n]:
            dimension, matrix = expand_source(table, marked)
            source_size, statistic = validate_source(dimension, matrix)
            assert source_size == n
            assert reduce_source(dimension, matrix) == (table, marked)

            linear = source_to_ordered_partition(table, marked)
            assert ordered_partition_to_source(linear) == (table, marked)
            e = ordered_partition_to_minus(linear)
            assert minus_to_ordered_partition(e) == linear
            assert len(e) == n and len(set(e)) == statistic
            assert cycle_to_full(full_to_cycle(e)) == e
            assert e not in image
            image[e] = (table, marked)
            source_profile[statistic] += 1

        targets = set(target_sequences(n))
        assert set(image) == targets
        for e in targets:
            linear = minus_to_ordered_partition(e)
            assert ordered_partition_to_minus(linear) == e
            table, marked = ordered_partition_to_source(linear)
            assert image[e] == (table, marked)
        target_profile: dict[int, int] = defaultdict(int)
        for e in targets:
            target_profile[len(set(e))] += 1
        assert dict(source_profile) == dict(target_profile)
        profile = ",".join(
            f"{k}:{source_profile[k]}" for k in sorted(source_profile)
        )
        print(f"{n} {len(sources[n])} {len(targets)} {profile}")

    print("PASS: exhaustive structural bijection and both inverses verified for n<=8")


if __name__ == "__main__":
    main()
