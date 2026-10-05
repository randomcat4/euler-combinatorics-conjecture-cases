# Verification and reproduction

Independent mathematical reviews returned CORRECT for the full original conjecture. The final review checked all connected position graphs, the n=1 and n=2 endpoints, connectedness consequences, incidence-degree injections, repeated fixed-label components, uniform clone multiplicities, regular Bi-Cayley action, separator transfer, equal-type lifts, arbitrary endpoints and the reserved-edge treatment of adjacent endpoints.

The original Liang--Meng article was checked directly: Theorem 3.7, printed page 31, requires a connected finite Bi-Cayley graph and gives connectivity equal to degree. The auxiliary regularized graph satisfies these exact prerequisites. No abelian or inverse-closed connection-set hypothesis is needed.

From the repository root, run:

```bash
python cases/star-friends-and-strangers-local-connectivity/checks/validate_flow.py
python cases/star-friends-and-strangers-local-connectivity/checks/quotient01.py
```

All code uses the Python standard library. The first check compares node-split flow and brute vertex cuts on all 7,521 endpoint pairs in connected labelled simple graphs of orders two through five. The second constructs 145 actual incidence quotients and checks their degrees and local connectivity. Its domain is the high-degree-hole orbits (`deg_X(h) > delta(X)`) of connected friends-and-strangers graphs on all connected unlabelled position graphs of orders four through six, together with selected order-seven graphs. It writes `quotient01.json` next to the script. The additional search modules provide definitions and fixed candidate graphs to that check; no search result is a premise of the general theorem.

Maintainer mathematical review is complete; the full theorem is not formalized.
