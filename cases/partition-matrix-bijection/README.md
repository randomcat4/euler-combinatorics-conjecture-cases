# A cyclic-partition bijection for partition matrices

**Source problem:** Question 5.7 of Chern--Fu, arXiv v2. [Original statement and sources](problem.md).

**[Read the clean proof PDF](paper/extension.pdf)**

**Extension pass (+2h).** A common cyclic set partition gives explicit inverse maps for the original minus classes and the full classes. Dimension and the complete ordered column-parity signature are retained, with Eulerian and Stirling enumerations.

**Initial pass (2h).** The initial note established the statistic-preserving minus bijection.

The source already related existence of the minus and full bijections; the note attributes that reduction and the known enumerations. Public priority is not established.

[Extension case files and independent checks](extension/)

<details>
<summary>Historical initial-pass package (the current result is above)</summary>

## Initial public package

The original description and public files below document the initial pass. They remain available; the extension manuscript above gives the later scope.

*Shane Chern and Shishuo Fu · [DOI](https://doi.org/10.1016/j.jcta.2026.106213) · [arXiv](https://arxiv.org/abs/2508.21318)*

This case gives an explicit bijection between a parity-defined class of improper partition matrices and a restricted class of inversion sequences. The map is defined for every size, has an explicit inverse, has the exact requested image, and preserves the statistics `v` and `dist` object by object.

This is one of the first curated public results from the Euler System case library devoted to conjectures and open problems posed by authors who have published in leading combinatorics journals within the preceding 24 months.

### Contents

- [Problem](problem.md): definitions and the precise all-order statement.
- [Proof](proof.md): the self-contained construction, inverse, and proof of statistic preservation.
- [Status](status.md): separate assessments of correctness, completeness, and public priority.
- [Verification](verification.md): independent mathematical checks and exhaustive finite calibration.
- [Sources](sources.md): the original question and the standard ingredients used in the construction.
- [Exhaustive check](exhaustive-check.md): scope, output, and limitations of the executable checker.
- [Checker](verify_bijection.py): a reproducible exhaustive test through size eight.

### Result at a glance

For every integer `n >= 1`, the construction defines a bijection

\[
\rho_n\colon\operatorname{IPPM}_n^-\longrightarrow I_n(-,-,=)^-
\]

such that

\[
v(Q)=\operatorname{dist}(\rho_n(Q))
\]

for every `Q` in the source class. Here `dist` counts all distinct entries, including zero. The endpoint is

\[
\rho_1([\{1\}])=(0).
\]

Public novelty or priority is **not established**. See [Status](status.md).

</details>

## Review and reuse

These proofs were generated autonomously by EULER and are released under the
[MIT License](../../LICENSE), with research-credit and priority claims waived.
The [review record](../../docs/provenance.md) describes Sol High and Opus 4.8
xhigh re-review, initial human review by the author and doctoral students at
ETH Zürich and Peking University, and the invitation to specialists for
preliminary counterexample review. Mathematical and computational scope is
stated separately in this package.
