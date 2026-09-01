#!/usr/bin/env python3
"""Verify the TGr_{3,5} 3-word counterexample certificate."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent


def sorted_pair(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


def canonical_vertices(m: int, n: int) -> list[str]:
    return [f"x{i}{j}" for j in range(1, n + 1) for i in range(1, m + 1)]


def tgr35_edges() -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()

    for j in range(1, 6):
        column = [f"x{i}{j}" for i in range(1, 4)]
        for a, b in combinations(column, 2):
            edges.add(sorted_pair(a, b))

    for i in range(1, 4):
        for j in range(1, 6):
            a = f"x{i}{j}"
            b = f"x{i}{1 + (j % 5)}"
            edges.add(sorted_pair(a, b))

    return edges


def alternates(projected: list[str], uniformity: int) -> bool:
    return len(projected) == 2 * uniformity and all(
        projected[index] != projected[index + 1]
        for index in range(len(projected) - 1)
    )


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_certificate(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def verify(certificate: dict[str, Any]) -> dict[str, Any]:
    graph = certificate["graph"]
    expected = certificate["expected"]
    uniformity = int(expected["uniformity"])
    vertices = canonical_vertices(int(graph["m"]), int(graph["n"]))
    word = list(certificate["word"])

    certificate_vertices = list(graph["vertices"])
    if certificate_vertices != vertices:
        raise AssertionError("certificate vertex order does not match TGr_{3,5}")

    constructed_edges = tgr35_edges()
    certificate_edges = {
        sorted_pair(edge[0], edge[1])
        for edge in graph["edges"]
    }
    if certificate_edges != constructed_edges:
        raise AssertionError("certificate edge set does not match TGr_{3,5}")

    counts = Counter(word)
    unknown_symbols = sorted(set(word) - set(vertices))
    bad_counts = {
        vertex: counts[vertex]
        for vertex in vertices
        if counts[vertex] != uniformity
    }

    inverse_letter_map = {value: key for key, value in certificate["letter_map"].items()}
    compressed_word = "".join(inverse_letter_map[token] for token in word)
    if compressed_word != certificate["compressed_word"]:
        raise AssertionError("compressed word does not match the letter map")

    pair_rows: list[dict[str, Any]] = []
    mismatches: list[dict[str, Any]] = []
    edge_alternating = 0
    edge_non_alternating = 0
    nonedge_alternating = 0
    nonedge_non_alternating = 0

    for index, a in enumerate(vertices):
        for b in vertices[index + 1 :]:
            pair = sorted_pair(a, b)
            projected = [token for token in word if token == a or token == b]
            adjacent = pair in constructed_edges
            is_alternating = alternates(projected, uniformity)
            row = {
                "a": a,
                "b": b,
                "adjacent": adjacent,
                "alternates": is_alternating,
                "projection": " ".join(projected),
            }
            pair_rows.append(row)
            if adjacent and is_alternating:
                edge_alternating += 1
            elif adjacent:
                edge_non_alternating += 1
            elif is_alternating:
                nonedge_alternating += 1
            else:
                nonedge_non_alternating += 1
            if adjacent != is_alternating:
                mismatches.append(row)

    word_text = " ".join(word)
    summary = {
        "ok": (
            len(word) == expected["word_length"]
            and len(vertices) == expected["vertex_count"]
            and len(constructed_edges) == expected["edge_count"]
            and len(pair_rows) == expected["unordered_pair_count"]
            and not unknown_symbols
            and not bad_counts
            and not mismatches
        ),
        "case": certificate["case"],
        "result": certificate["result"],
        "source_arxiv": certificate["source"]["arxiv"],
        "source_statement": certificate["source"]["statement"],
        "graph": graph["name"],
        "graph_definition": graph["definition"],
        "word_length": len(word),
        "uniformity": uniformity,
        "vertex_count": len(vertices),
        "edge_count": len(constructed_edges),
        "nonedge_count": len(pair_rows) - len(constructed_edges),
        "unordered_pair_count": len(pair_rows),
        "edge_alternating": edge_alternating,
        "edge_non_alternating": edge_non_alternating,
        "nonedge_alternating": nonedge_alternating,
        "nonedge_non_alternating": nonedge_non_alternating,
        "mismatch_count": len(mismatches),
        "bad_counts": bad_counts,
        "unknown_symbols": unknown_symbols,
        "word_sha256": sha256_text(word_text),
        "compressed_word_sha256": sha256_text(certificate["compressed_word"]),
        "source_conjecture_refuted": True,
    }

    for key, value in expected.items():
        expected_key = {
            "word_length": "word_length",
            "vertex_count": "vertex_count",
            "edge_count": "edge_count",
            "unordered_pair_count": "unordered_pair_count",
            "nonedge_count": "nonedge_count",
            "mismatch_count": "mismatch_count",
        }.get(key)
        if expected_key and summary[expected_key] != value:
            raise AssertionError(f"unexpected {key}: {summary[expected_key]} != {value}")

    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=ROOT / "word_certificate.json",
        help="path to the JSON word certificate",
    )
    parser.add_argument(
        "--summary-out",
        type=Path,
        help="optional path for the compact verification summary",
    )
    args = parser.parse_args()

    summary = verify(load_certificate(args.certificate))
    text = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    if args.summary_out:
        args.summary_out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
