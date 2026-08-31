"""Regression checks for the partition-matrix q-sum-product formula.

Finite computation is not the proof. This script compares two independent
constructions through n=8: the finite q-difference recurrence and direct
enumeration of the column-word encoding of partition matrices.
"""

from __future__ import annotations

from itertools import product


MAX_N = 8


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def neg(a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-x for x in a)


def q_factor(start: int, stop: int) -> tuple[int, ...]:
    out = (1,)
    for exponent in range(start, stop + 1):
        term = [0] * (exponent + 1)
        term[0] = 1
        term[exponent] = -1
        out = mul(out, tuple(term))
    return out


def choose(n: int, r: int) -> int:
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    value = 1
    for i in range(1, r + 1):
        value = value * (n - r + i) // i
    return value


def word_series(k: int) -> list[tuple[int, ...]]:
    """Return coefficients H_{m,k} from the recurrence, for 0 <= m <= MAX_N."""
    h: list[tuple[int, ...]] = [(1,)]
    for m in range(1, MAX_N + 1):
        total = (0,)
        for r in range(1, min(k, m) + 1):
            term = mul(q_factor(m - r + 1, m - 1), h[m - r])
            scalar = choose(k, r) * (1 if r % 2 else -1)
            total = add(total, tuple(scalar * x for x in term))
        h.append(total)
    return h


def series_mul(
    a: list[tuple[int, ...]], b: list[tuple[int, ...]]
) -> list[tuple[int, ...]]:
    out = [(0,) for _ in range(MAX_N + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b[: MAX_N + 1 - i]):
            out[i + j] = add(out[i + j], mul(x, y))
    return out


def series_inv(a: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    assert a[0] == (1,)
    out = [(0,) for _ in range(MAX_N + 1)]
    out[0] = (1,)
    for n in range(1, MAX_N + 1):
        total = (0,)
        for i in range(1, n + 1):
            total = add(total, mul(a[i], out[n - i]))
        out[n] = neg(total)
    return out


def formula_coefficients() -> list[tuple[int, ...]]:
    total = [(0,) for _ in range(MAX_N + 1)]
    running = [(1,)] + [(0,) for _ in range(MAX_N)]
    for k in range(1, MAX_N + 1):
        r = word_series(k)
        inverse = series_inv(r)
        factor = [neg(x) for x in inverse]
        factor[0] = add((1,), factor[0])
        running = series_mul(running, factor)
        total = [add(x, y) for x, y in zip(total, running)]
    return total


def compositions(n: int, d: int):
    if d == 1:
        yield (n,)
        return
    for first in range(1, n - d + 2):
        for rest in compositions(n - first, d - 1):
            yield (first,) + rest


def inversions(word: tuple[int, ...]) -> int:
    return sum(
        word[i] > word[j]
        for i in range(len(word))
        for j in range(i + 1, len(word))
    )


def direct_coefficient(n: int) -> tuple[int, ...]:
    counts: dict[int, int] = {}
    object_count = 0
    for d in range(1, n + 1):
        for lengths in compositions(n, d):
            column_spaces = [
                product(range(1, j + 1), repeat=lengths[j - 1])
                for j in range(1, d + 1)
            ]
            for words in product(*column_spaces):
                if set().union(*(set(word) for word in words)) != set(
                    range(1, d + 1)
                ):
                    continue
                degree = sum(inversions(word) for word in words)
                counts[degree] = counts.get(degree, 0) + 1
                object_count += 1
    assert object_count == factorial(n)
    return tuple(counts.get(i, 0) for i in range(max(counts, default=0) + 1))


def factorial(n: int) -> int:
    value = 1
    for i in range(2, n + 1):
        value *= i
    return value


SOURCE = {
    1: (1,),
    2: (2,),
    3: (5, 1),
    4: (15, 7, 2),
    5: (53, 41, 20, 5, 1),
    6: (217, 240, 161, 68, 24, 8, 2),
    7: (1014, 1475, 1253, 716, 334, 154, 62, 22, 9, 1),
    8: (5335, 9677, 9950, 7066, 4034, 2192, 1098, 527, 271, 108, 40, 18, 4),
}


def main() -> None:
    formula = formula_coefficients()
    for n in range(1, MAX_N + 1):
        direct = direct_coefficient(n)
        assert formula[n] == direct == SOURCE[n]
        assert formula[n][0] > 0
        assert sum(formula[n]) == factorial(n)
        print(
            f"n={n}: objects={factorial(n)}, "
            f"q_degree={len(formula[n]) - 1}, PASS"
        )
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
