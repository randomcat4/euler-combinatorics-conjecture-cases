"""Exhaustively verify the four-point crossing-partition lemma."""

from __future__ import annotations

from itertools import permutations


POINTS = ("A", "B", "C", "D")
FIRST = (frozenset(("A", "B")), frozenset(("C", "D")))
SECOND = (frozenset(("A", "C")), frozenset(("B", "D")))


def separates(order: tuple[str, ...], partition: tuple[frozenset[str], ...]) -> bool:
    positions = {point: index for index, point in enumerate(order)}
    left, right = partition
    return max(positions[x] for x in left) < min(positions[x] for x in right) or max(
        positions[x] for x in right
    ) < min(positions[x] for x in left)


def main() -> None:
    orders = list(permutations(POINTS))
    first_orders = {order for order in orders if separates(order, FIRST)}
    second_orders = {order for order in orders if separates(order, SECOND)}

    assert len(orders) == 24
    assert len(first_orders) == 8
    assert len(second_orders) == 8
    assert first_orders.isdisjoint(second_orders)

    promoted_core = {
        tuple(word) for word in ("ACBD", "CADB", "BDAC", "DBCA")
    }
    assert promoted_core <= second_orders
    assert promoted_core.isdisjoint(first_orders)

    print("PASS: four-point crossing obstruction verified")


if __name__ == "__main__":
    main()
