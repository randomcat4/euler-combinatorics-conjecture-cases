# Disjoint paths in a connected star friends-and-strangers graph

## Theorem

Let $X$ be a finite simple graph on $[n]$, let $\mathsf{Star}_n$ be the star on $[n]$ with center $n$, and put
$$
G=\mathsf{FS}(X,\mathsf{Star}_n).
$$
Its vertices are the bijections $\tau:[n]\to[n]$, with $\tau(i')$ giving the person at position $i'$. Two vertices differ by a friendly swap when they exchange the people at adjacent positions of $X$, and one of the two exchanged people is $n$. Thus we use exactly the position-to-person convention of Krishnan and Li.

Assume that $G$ is connected. If $\sigma,\rho\in V(G)$ are distinct, then the maximum number of pairwise internally vertex-disjoint $\sigma$-$\rho$ paths is
$$
\min\{\deg_G(\sigma),\deg_G(\rho)\}.
$$
Here, as in the source paper, paths may meet at their two common endpoints but nowhere else. If $\sigma$ and $\rho$ are adjacent, the edge $\sigma\rho$ itself counts as one path.

## A connectivity theorem for Bi-Cayley graphs

We use the following theorem of Liang and Meng. Let $H$ be a finite group and $S\subseteq H$. The Bi-Cayley graph $\operatorname{BC}(H,S)$ has two copies of $H$ as its bipartition classes, with $(g,0)$ adjacent to $(sg,1)$ for $g\in H$ and $s\in S$. If $\operatorname{BC}(H,S)$ is connected, then its vertex connectivity is its degree $|S|$ [Liang--Meng, Theorem 3.7].

We will use the equivalent formulation that if a finite connected bipartite graph has a group of automorphisms acting regularly on each bipartition class, then its vertex connectivity equals its degree. Indeed, after choosing one vertex in each class, the two regular actions identify both classes with the group, and invariance under the action gives precisely a Bi-Cayley graph. If these identifications give edges from $(g,0)$ to $(gs,1)$ instead, replacing both group coordinates by their inverses gives the convention above, with connection set $S^{-1}$.

## Proof strategy

We first fix a type $h$ and prove the result for two permutations of that same type. Delete the whole type fibre $T_h$. Each component left behind represents one possible class of excursions during which the center $n$ leaves position $h$ and later returns. Contracting those components gives a bipartite incidence graph $J_h$.

The graph $J_h$ is generally only biregular, so the Bi-Cayley connectivity theorem does not apply to it directly. We use the symmetry among the ordinary people to show that every component has the same multiplicity $q$, and then replace each component-node by $q$ actual representatives. The resulting regular graph $K_h$ is a connected Bi-Cayley graph. Its connectivity transfers back to $J_h$, and disjoint paths in $J_h$ lift through the original components to disjoint paths in $G$. This settles equal-type endpoints.

Finally, a simple path in $X$ has $(n-1)!$ mutually disjoint lifts in $G$, one from each permutation of its initial type. These lifts, together with the equal-type result, join arbitrary endpoint types. When the endpoints are adjacent, we reserve their edge and apply the same argument after deleting that edge.

## Proof

The cases $n=1$ and $n=2$ are immediate: the first is vacuous, and in the second a connected $G$ is a single edge. Hence assume $n\geq 3$.

The source paper calls
$$
\operatorname{type}(\tau)=\tau^{-1}(n)\in V(X)
$$
the type of a permutation $\tau\in V(G)$. Thus the type is the position occupied by the center $n$ of $\mathsf{Star}_n$, or equivalently the empty position in the sliding-puzzle interpretation. A friendly swap moves $n$ to a neighboring position in $X$. Consequently
$$
\deg_G(\tau)=\deg_X\bigl(\operatorname{type}(\tau)\bigr).\tag{1}
$$
For $x\in V(X)$, write
$$
T_x=\{\tau\in V(G):\operatorname{type}(\tau)=x\}.
$$
Each $T_x$ has $(n-1)!$ elements and is an independent set in $G$.

### 1. Deleting any one position from $X$

First, $X$ is connected. Indeed, under any walk in $G$, the sequence of types is a walk in $X$; and every vertex of $X$ occurs as the type of some permutation. If $X$ had two components, permutations whose types lie in different components could not be joined in $G$.

We next record the stronger consequence that, for every $h\in V(X)$, the graph $X-h$ is connected.

Suppose instead that $X-h$ has at least two components. Consider a walk in $G$ whose first and last permutations lie in $T_h$. Split the walk into excursions between consecutive visits to $T_h$. During one such excursion, the type leaves $h$, stays in a single component $C$ of $X-h$, and eventually returns to $h$. The first move carries one ordinary person from $C$ to $h$, and the last move carries that same person back into $C$. All intervening moves take place inside $C$. Therefore the set of ordinary people occupying the positions of $C$ is unchanged by the excursion. The corresponding set is also unchanged for every other component of $X-h$.

It follows that along every walk between two permutations in $T_h$, the set of people in each component of $X-h$ is invariant. But two permutations in $T_h$ can be chosen by exchanging people in two different components of $X-h$. They could not be joined in $G$, contrary to the connectedness of $G$. Thus $X-h$ is connected.

In particular, every vertex of $X$ has degree at least two. Connectedness of $X$ rules out degree zero. If $x$ were a leaf with neighbor $y$, then $x$ would be isolated in $X-y$, which is impossible when $n\geq3$.

### 2. Delete one type fibre and form an incidence graph

Fix $h\in V(X)$ and set
$$
D=\deg_X(h).
$$
We will first prove the theorem for two permutations of type $h$. The reason for deleting the entire fibre $T_h$ is that, once a walk leaves type $h$, the ordinary person left at position $h$ cannot change until the walk returns to type $h$. The components of $G-T_h$ therefore retain exactly the information needed to describe excursions away from $h$.

Let $\mathcal B_h$ be the set of connected components of $G-T_h$. Define a bipartite incidence graph $J_h$ with bipartition
$$
T_h\sqcup\mathcal B_h.
$$
A permutation $\tau\in T_h$ is adjacent in $J_h$ to $B\in\mathcal B_h$ when $\tau$ has a neighbor in $B$ in the original graph $G$. This is a simple graph: adjacency records only whether such an edge exists. Equivalently, contract every component of $G-T_h$ to one vertex and retain the vertices of $T_h$. This gives $J_h$, so $J_h$ is connected because $G$ is connected.

Fix $B\in\mathcal B_h$. Every permutation $\beta\in B$ has the same ordinary person at position $h$. Indeed, an edge of $G-T_h$ cannot swap at $h$, since such a swap would have one endpoint of type $h$. Denote this fixed person by
$$
\ell(B)=\beta(h)\in[n-1].
$$
The component $B$ and the person $\ell(B)$ are different objects: several components could a priori have the same fixed person. We use $\ell(B)$ only to distinguish the possible attachments of $B$ to $T_h$.

The component $B$ contains permutations of every type $x\neq h$. To see this, start from any $\beta\in B$ and take a path in the connected graph $X-h$ from $\operatorname{type}(\beta)$ to $x$. Moving $n$ along this path gives a path in $G-T_h$, so its endpoint remains in $B$ and has type $x$.

More is true: the number of permutations of each type $x\neq h$ in $B$ is independent of $x$. If $P$ is a fixed path from $x$ to $y$ in $X-h$, moving $n$ along $P$ maps the type-$x$ permutations in $B$ bijectively to the type-$y$ permutations in $B$; moving along the reverse path is the inverse map. Write this common positive number as
$$
q_B=|B\cap T_x|\qquad(x\neq h).\tag{2}
$$

We now compute the two degrees in $J_h$. If $\tau\in T_h$, moving $n$ from $h$ to each of its $D$ neighbors in $X$ produces $D$ neighbors of $\tau$ in $G-T_h$. The $D$ moves leave $D$ different people at position $h$, so their endpoints belong to different components $B$. Hence
$$
\deg_{J_h}(\tau)=D.\tag{3}
$$

On the other side, let $B\in\mathcal B_h$. For every neighbor $x$ of $h$, there are $q_B$ permutations in $B\cap T_x$, and each is adjacent in $G$ to a permutation in $T_h$. These $Dq_B$ permutations give $Dq_B$ distinct neighbors of $B$ in $J_h$. The point requiring verification is that two of them cannot lead to the same $\tau\in T_h$. If $\tau$ is adjacent to $B$, then the move from $\tau$ into $B$ must swap $h$ with the unique position $x$ at which $\tau(x)=\ell(B)$. Thus $x$, and then the resulting neighbor of $\tau$ in $B$, is uniquely determined. Therefore
$$
\deg_{J_h}(B)=Dq_B.\tag{4}
$$
In particular, $J_h$ has minimum degree $D$, but it need not be regular because $q_B$ has not yet been shown to be constant and may exceed one.

### 3. Symmetry and regularization

Let
$$
\Gamma=\mathfrak S_{[n-1]}
$$
be the group permuting the ordinary people and fixing $n$. It acts on $V(G)$ by $\tau\mapsto\gamma\circ\tau$. This action preserves friendly swaps, hence gives automorphisms of $G$. It is transitive, in fact regular, on every type fibre $T_x$.

The same action is transitive on $\mathcal B_h$. Choose one position $p_0\neq h$. By the preceding paragraph, every $B\in\mathcal B_h$ contains a permutation of type $p_0$. Given $B_1,B_2\in\mathcal B_h$, choose $\beta_i\in B_i\cap T_{p_0}$. There is a unique $\gamma\in\Gamma$ such that $\gamma\circ\beta_1=\beta_2$. Since $\gamma$ preserves $T_h$, it maps components of $G-T_h$ to components and therefore maps $B_1$ onto $B_2$. It follows from (2) that all $q_B$ have a common value, say $q$.

The incidence graph $J_h$ is now $(D,Dq)$-biregular. We cannot apply the regular Bi-Cayley theorem directly when $q>1$. We therefore replace every component-node $B$ by its $q$ actual representatives in $B\cap T_{p_0}$.

Define an auxiliary bipartite graph $K_h$ with bipartition
$$
T_h\sqcup T_{p_0}.
$$
For $\tau\in T_h$ and $\beta\in T_{p_0}$, where $\beta$ belongs to the component $B\in\mathcal B_h$, declare $\tau\beta$ to be an edge of $K_h$ exactly when $\tau B$ is an edge of $J_h$. Thus the $q$ vertices of $B\cap T_{p_0}$ are $q$ copies of the component-node $B$, all with the same neighborhood. The graph $K_h$ is auxiliary; its edges need not be friendly swaps in $G$.

By (3) and (4), every vertex of $K_h$ has degree $Dq$. It is also connected. Map $T_h$ identically to $T_h$, and map each $\beta\in B\cap T_{p_0}$ to the node $B$ of $J_h$. A path in $J_h$ lifts to a path in $K_h$ by choosing, at each component-node $B$ on the path, any representative in $B\cap T_{p_0}$. If an endpoint of the lifted path is a prescribed representative, choose that representative at the corresponding endpoint. Two representatives over the same $B$ are joined through any common $T_h$-neighbor. It follows that any two vertices of $K_h$ can be joined.

The action of $\Gamma$ is regular on both $T_h$ and $T_{p_0}$, and the definition of $K_h$ is invariant under this action. Hence $K_h$ is a connected Bi-Cayley graph over $\Gamma$. The Liang--Meng theorem says that the vertex connectivity of $K_h$ is
$$
Dq.\tag{5}
$$

We transfer this connectivity back to the biregular graph $J_h$. Suppose that $Z$ is a vertex cut of $J_h$, and write
$$
a=|Z\cap T_h|,\qquad b=|Z\cap\mathcal B_h|.
$$
In $K_h$, delete the same $a$ vertices of $T_h$, and for every $B\in Z\cap\mathcal B_h$, delete all $q$ vertices of $B\cap T_{p_0}$. Call the resulting set $\widehat Z$. Then
$$
|\widehat Z|=a+qb\leq q(a+b)=q|Z|.\tag{6}
$$
Moreover, a path in $K_h-\widehat Z$ would project to a walk in $J_h-Z$. Thus vertices lying over different components of $J_h-Z$ cannot be joined in $K_h-\widehat Z$, so $\widehat Z$ is a vertex cut of $K_h$.

If $|Z|<D$, (6) would give $|\widehat Z|<Dq$, contradicting (5). Therefore every vertex cut of $J_h$ has size at least $D$. For the reverse bound, delete the $D$ neighbors of any $\tau\in T_h$. This isolates $\tau$, while another vertex of $T_h$ remains because $|T_h|=(n-1)!\geq2$. Hence the vertex connectivity of $J_h$ is exactly
$$
D.\tag{7}
$$

### 4. Permutations of the same type

Let $\sigma,\rho\in T_h$ be distinct. By (7) and Menger's theorem, $J_h$ contains $D$ pairwise disjoint $\sigma$-$\rho$ paths. We lift each one to $G$. Whenever a path passes through a component-node $B$, its two incident edges specify a neighbor of the preceding $T_h$-vertex in $B$ and a neighbor of the following $T_h$-vertex in $B$. Join these two attachment permutations by a path inside the connected component $B$, and include the two friendly-swap edges at the ends.

Different paths in $J_h$ have no common internal $T_h$-vertex and no common component-node $B$. Their lifts therefore have no common internal vertex in $G$: different components of $G-T_h$ are disjoint, and none contains a vertex of $T_h$. Erasing any cycles within an individual lifted walk gives $D$ pairwise disjoint $\sigma$-$\rho$ paths in $G$. By (1), both endpoints have degree $D$, so no larger family is possible. We have proved
$$
\max\{\text{number of disjoint $\sigma$-$\rho$ paths}\}=\deg_X(h)\tag{8}
$$
whenever $\sigma$ and $\rho$ have the same type $h$.

### 5. Arbitrary endpoint types

Now let $\sigma,\rho\in V(G)$ be arbitrary distinct vertices and put
$$
u=\operatorname{type}(\sigma),\qquad v=\operatorname{type}(\rho),\qquad
d=\min\{\deg_G(\sigma),\deg_G(\rho)\}
 =\min\{\deg_X(u),\deg_X(v)\}.\tag{9}
$$
The case $u=v$ is (8), so assume $u\neq v$.

Choose a simple path
$$
P:u=x_0,x_1,\ldots,x_r=v
$$
in $X$. Starting from any permutation in $T_u$, successively move person $n$ along $P$. This gives a path in $G$ ending in $T_v$. As the starting permutation ranges over the $(n-1)!$ elements of $T_u$, these lifted paths are pairwise vertex-disjoint. Indeed, at each fixed level $i$, moving along the first $i$ edges of $P$ is a bijection from $T_u$ to $T_{x_i}$, while different levels have different types because $P$ is simple. We therefore have $(n-1)!$ disjoint paths joining the two full fibres $T_u$ and $T_v$.

First suppose that $\sigma$ and $\rho$ are not adjacent. Let $Z\subseteq V(G)\setminus\{\sigma,\rho\}$ with $|Z|<d$. By (8), any two surviving permutations in $T_u$ are joined in $G-Z$: among the $\deg_X(u)$ disjoint paths between them, fewer than $d\leq\deg_X(u)$ can meet $Z$. Hence all of $T_u-Z$ lies in one component of $G-Z$. The same holds for $T_v-Z$.

Since the lifted copies of $P$ are vertex-disjoint and $|Z|\leq d-1\leq n-2<(n-1)!$, at least one of them avoids $Z$. It joins the component containing $T_u-Z$ to the component containing $T_v-Z$, and consequently joins $\sigma$ to $\rho$. Thus no set of fewer than $d$ vertices separates $\sigma$ from $\rho$. Menger's theorem gives $d$ disjoint paths.

It remains to handle adjacent $\sigma$ and $\rho$. Let $e=\sigma\rho$, and reserve $e$ as one of the desired paths. We show that $G-e$ contains $d-1$ further disjoint $\sigma$-$\rho$ paths.

Let $Z\subseteq V(G)\setminus\{\sigma,\rho\}$ with $|Z|\leq d-2$. We first check that the vertices of $T_u-Z$ lie in one connected component of the ambient graph $G-Z-e$. Between any two of its vertices, (8) supplies $\deg_X(u)$ disjoint paths in $G$. At most $|Z|$ of these meet $Z$, and at most one uses $e$. For the last assertion, note that a path between two type-$u$ permutations which uses $e$ contains $\rho$, whose type is $v$, as an internal vertex; two paths in a disjoint family cannot both do so. Hence at least
$$
\deg_X(u)-|Z|-1\geq \deg_X(u)-(d-2)-1\geq1
$$
paths avoid both $Z$ and $e$. Therefore all vertices of $T_u-Z$ lie in one connected component of the ambient graph $G-Z-e$. The same argument, with $\sigma$ as the forced internal vertex of a type-$v$ path using $e$, places all vertices of $T_v-Z$ in one connected component there as well.

Among the $(n-1)!$ lifted copies of $P$, at most $|Z|$ meet $Z$, and at most one uses $e$, because the lifts are vertex-disjoint. There is still a surviving lift. Indeed, if $n=3$, then $d=2$, $Z=\varnothing$, and $2!=(n-1)!>1$. If $n\geq4$, then
$$
|Z|+1\leq d-1\leq n-2<(n-1)!.
$$
This surviving lift joins $T_u-Z$ to $T_v-Z$ in $G-Z-e$, so it joins $\sigma$ to $\rho$. We have proved that no set of at most $d-2$ vertices separates $\sigma$ and $\rho$ in $G-e$. By Menger's theorem, $G-e$ contains $d-1$ disjoint $\sigma$-$\rho$ paths. Adding the reserved edge $e$ gives $d$ disjoint paths in $G$.

Finally, $d$ is also an upper bound. If the endpoints are nonadjacent, disjoint paths must leave either endpoint through distinct neighbors. If they are adjacent, at most one path is the edge $\sigma\rho$, and every other path must leave each endpoint through a different remaining neighbor. Thus no family has more than $\min\{\deg_G(\sigma),\deg_G(\rho)\}=d$ paths. This proves the theorem.

## References

N. Krishnan and R. Li, *Vertex Connectivity of Friends-and-strangers Graphs*, Electronic Journal of Combinatorics 33(3) (2026), P3.41; [arXiv:2410.21334v3](https://arxiv.org/abs/2410.21334v3), Conjecture 7.1. The original v1 labels the same conjecture 8.1.

X. Liang and J. Meng, “Connectivity of Bi-Cayley Graphs,” *Ars Combinatoria* **88** (2008), 27--32, Theorem 3.7. [Original article](https://combinatorialpress.com/article/ars/Volume%20088/volume-88-paper-3.pdf).
