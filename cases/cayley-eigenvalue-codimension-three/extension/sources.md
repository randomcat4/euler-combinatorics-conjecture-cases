# Sources

The source problem and all boundary inputs below are stated in Li--Xia--Zhou, *The second largest eigenvalue of some nonnormal Cayley graphs on symmetric groups*, [arXiv:2402.02427v1](https://arxiv.org/html/2402.02427v1), subsequently JCTA 218 (2026), 106097, [DOI](https://doi.org/10.1016/j.jcta.2025.106097).

| Input | Source location | Exact range used here |
|---|---|---|
| Original target | Conjecture 4.7 | n>=5, 1<=r<k<=n-2; representation-level uniqueness |
| Non-strict bound | Theorems 4.4 and 4.6; equation (14) | 4<=k<=n-2; odd k begins at 5. The source gives the eigenvalue, not the full equality classification. |
| Odd-order boundary | Theorem 3.3(d) | m>=5 odd, k=m-1, m/2<r<m-1: standard representation uniquely attains the second eigenvalue. |
| Even-order boundary | Theorem 3.5(b), especially (b.2) | m>=6 even, k=m-1; exclude (m,r)=(6,1). Non-strict bound for the remaining range; exactly the standard and sign-twisted standard representations attain it when 3<=r<=m-2. |
| Even n, k=n-2 | Lemmas 4.2 and 4.3 | n>=8 even, 1<=r<(n-1)/2: standard representation uniquely attains it. |
| Generation and sign twist | Lemmas 2.6 and 2.14 | Even k generates S_n; odd k generates A_n. The latter gives two degree blocks and identical operators on conjugate partitions. |

These theorem statements and parameter ranges were checked against the linked source. The model review does not replace the cited papers' proofs. Cases k=2,3 are treated directly in the manuscript.

- [Original public proof PR](https://github.com/randomcat4/euler-combinatorics-conjecture-cases/pull/17).
- [Initial case bibliography](../sources.md), including the antecedent representation-theoretic sources.
- [Current manuscript](../paper/full_conjecture.pdf) and [reproducible finite evidence](verification.md).

Attribution and correctness are separate from novelty; public priority is not established.
