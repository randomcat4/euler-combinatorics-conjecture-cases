#!/usr/bin/env python3
"""Finite quotient/support calibration for the P58 public theorem."""

from __future__ import annotations

import argparse
from collections import deque
from itertools import permutations, product
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
Perm = tuple[int, ...]
Vec = tuple[int, ...]
Elt = tuple[Vec, Perm]


def compose(h: Perm, ell: Perm) -> Perm:
    return tuple(h[ell[i]] for i in range(len(h)))


def act(h: Perm, v: Vec) -> Vec:
    out = [0] * len(v)
    for i, image in enumerate(h):
        out[image] = v[i]
    return tuple(out)


def add(u: Vec, v: Vec) -> Vec:
    return tuple((a + b) % 2 for a, b in zip(u, v))


def mul(x: Elt, y: Elt) -> Elt:
    v, h = x
    w, ell = y
    return add(v, act(h, w)), compose(h, ell)


def group_elements(k: int) -> tuple[Elt, ...]:
    perms = tuple(permutations(range(k)))
    vecs = tuple(product((0, 1), repeat=k))
    return tuple((v, h) for v in vecs for h in perms)


def closure(gens: frozenset[Elt]) -> frozenset[Elt]:
    subgroup = set(gens)
    queue = deque(gens)
    while queue:
        x = queue.popleft()
        for y in tuple(subgroup):
            for z in (mul(x, y), mul(y, x)):
                if z not in subgroup:
                    subgroup.add(z)
                    queue.append(z)
    return frozenset(subgroup)


def enumerate_subgroups(k: int) -> list[frozenset[Elt]]:
    elems = group_elements(k)
    identity = ((0,) * k, tuple(range(k)))
    trivial = frozenset({identity})
    seen = {trivial}
    out = [trivial]
    queue = deque([trivial])
    while queue:
        subgroup = queue.popleft()
        for g in elems:
            if g in subgroup:
                continue
            generated = closure(frozenset(set(subgroup) | {g}))
            if generated not in seen:
                seen.add(generated)
                out.append(generated)
                queue.append(generated)
    return out


def top_group(q: frozenset[Elt]) -> frozenset[Perm]:
    return frozenset(h for _v, h in q)


def kernel_code(q: frozenset[Elt], k: int) -> frozenset[Vec]:
    identity_top = tuple(range(k))
    return frozenset(v for v, h in q if h == identity_top)


def is_transitive_top(hs: frozenset[Perm], k: int) -> bool:
    orbit = {0}
    changed = True
    while changed:
        changed = False
        for h in hs:
            for x in tuple(orbit):
                y = h[x]
                if y not in orbit:
                    orbit.add(y)
                    changed = True
    return len(orbit) == k


def has_weight_one(code: frozenset[Vec]) -> bool:
    return any(sum(v) == 1 for v in code)


def parity(p: Perm) -> int:
    inv = 0
    for i, x in enumerate(p):
        for y in p[i + 1 :]:
            inv += x > y
    return inv % 2


def apply_lift(m: int, sigmas: tuple[Perm, ...], top: Perm, point: int) -> int:
    block, x = divmod(point, m)
    new_block = top[block]
    return new_block * m + sigmas[block][x]


def moved_count(m: int, sigmas: tuple[Perm, ...], top: Perm) -> int:
    return sum(
        apply_lift(m, sigmas, top, point) != point
        for point in range(m * len(sigmas))
    )


def brute_mu_for_quotient_m3(k: int, q: frozenset[Elt]) -> int:
    m = 3
    perms = tuple(permutations(range(m)))
    by_parity = {
        0: tuple(p for p in perms if parity(p) == 0),
        1: tuple(p for p in perms if parity(p) == 1),
    }
    best = m * k + 1
    identity_top = tuple(range(k))
    identity_sigmas = (tuple(range(m)),) * k
    for v, top in q:
        choices = [by_parity[bit] for bit in v]
        for sigmas in product(*choices):
            if top == identity_top and sigmas == identity_sigmas:
                continue
            best = min(best, moved_count(m, sigmas, top))
    return best


def verify(certificate: dict[str, Any]) -> dict[str, Any]:
    expected_by_k = certificate["calibration"]["expected_by_k"]
    rows = []
    for key in sorted(expected_by_k, key=int):
        k = int(key)
        subgroups = enumerate_subgroups(k)
        transitive_mu3 = []
        transitive_mu2 = []
        nontransitive = []
        for q in subgroups:
            h = top_group(q)
            code = kernel_code(q, k)
            top_transitive = is_transitive_top(h, k)
            weight_one = has_weight_one(code)
            mu = brute_mu_for_quotient_m3(k, q)
            if top_transitive and not weight_one:
                if mu != 3:
                    raise AssertionError((k, "expected mu=3", mu))
                transitive_mu3.append(q)
            elif top_transitive and weight_one:
                if mu != 2:
                    raise AssertionError((k, "expected mu=2", mu))
                transitive_mu2.append(q)
            else:
                nontransitive.append(q)

        row = {
            "k": k,
            "quotient_order": len(group_elements(k)),
            "subgroups": len(subgroups),
            "transitive_mu3": len(transitive_mu3),
            "transitive_mu2": len(transitive_mu2),
            "nontransitive": len(nontransitive),
            "brute_m3_support_checked": True,
        }
        expected = expected_by_k[key]
        for field in (
            "quotient_order",
            "subgroups",
            "transitive_mu3",
            "transitive_mu2",
            "nontransitive",
        ):
            if row[field] != expected[field]:
                raise AssertionError(f"k={k} {field}: {row[field]} != {expected[field]}")
        rows.append(row)

    return {
        "ok": True,
        "case": certificate["case"],
        "result": certificate["result"],
        "source": certificate["source"],
        "public_scope": certificate["public_scope"],
        "checks": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=ROOT / "quotient_certificate.json",
        help="path to the JSON quotient certificate",
    )
    parser.add_argument(
        "--summary-out",
        type=Path,
        help="optional path for the compact verification summary",
    )
    args = parser.parse_args()

    certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    summary = verify(certificate)
    text = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    if args.summary_out:
        args.summary_out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
