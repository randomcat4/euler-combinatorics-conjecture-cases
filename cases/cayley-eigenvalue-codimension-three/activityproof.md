# Product-activity cycle weights: two structured families

## 1. Operators and statements

For positive activities $x_1,\ldots,x_n$ and $2\le k\le n-2$, define

```math
 T_k(x)=\sum_{\substack{A\subseteq[n]\\|A|=k}}
 \left(\prod_{i\in A}x_i\right)
 \sum_{\substack{g\text{ a }k\text{-cycle}\\\operatorname{supp}(g)=A}}g
 \quad\in\mathbb R S_n.
```

Its degree is

```math
 D_k(x)=(k-1)!\sum_{|A|=k}\prod_{i\in A}x_i.
```

The inverse of a cycle has the same support and weight, so every irreducible
block is self-adjoint in a unitary realization. Write $S^\lambda$ for the
irreducible representation indexed by $\lambda\vdash n$ and $\lambda'$ for
the conjugate partition. The standard representation is $S^{(n-1,1)}$.
Conjugating a partition tensors its representation with sign.

All $k$-cycles have positive weights. They generate $S_n$ when $k$ is even
and $A_n$ when $k$ is odd. Equality with the degree in a unitary block forces
every generator to fix the vector: each summand has real inner product at
most its weight times the squared norm, and equality of their sum forces
equality term by term. Thus the degree occurs only in the trivial block for
even $k$, and only in the trivial and sign blocks for odd $k$. These are called
the degree blocks below. For odd $k$, conjugate partitions have identical
operators because every generator is even.

**Theorem 1 (one exceptional activity).** Let $n\ge5$, $2\le k\le n-2$,
$c>0$, and $0<t<1$. For

```math
 x=(tc,c,\ldots,c),
```

the largest nondegree eigenvalue occurs only in $(n-1,1)$ if $k$ is even,
and exactly in $(n-1,1)$ and $(2,1^{n-2})$ if $k$ is odd. It is simple
inside each attaining block. Its value is

```math
 c^k\left[(1-t)\binom{n-1}{k}(k-1)!
 +t\binom nk(k-1)!\frac{n-k-1}{n-1}\right].             \tag{1.1}
```

**Theorem 2 (three-cycles with two exceptional activities).** Let $n\ge5$,
$N=n-2$, and $a,b,c>0$ satisfy $a<\min(b,c)$. For

```math
 x=(a,b,c,\ldots,c),
```

the largest nondegree eigenvalue of $T_3(x)$ occurs exactly in $(n-1,1)$
and $(2,1^{n-2})$, and is simple in each attaining block. Set

```math
 \begin{aligned}
 p&=abNc, & r&=ac[b+(N-1)c], & s&=bc[a+(N-1)c],\\
 \mathcal T&=2p+(N+1)(r+s), &
 \mathcal S&=(N+2)[p(r+s)+Nrs].
 \end{aligned}
```

Then this adjacency eigenvalue is $D_3(x)-\gamma$, where

```math
 \gamma=\frac{\mathcal T-\sqrt{\mathcal T^2-4\mathcal S}}2. \tag{1.2}
```

These statements concern the displayed activity families. No assertion for
arbitrary positive activity vectors follows from them.

## 2. One exceptional activity

Divide by $c^k$. Let $K_{m,k}$ be the class sum of all $k$-cycles in $S_m$,
with the point stabilizer $S_{n-1}$ fixing the exceptional point. A support
avoiding that point has weight $1$ and a support containing it has weight $t$.
Consequently

```math
 T_k(t,1,\ldots,1)=tK_{n,k}+(1-t)K_{n-1,k}.             \tag{2.1}
```

The first class sum is central in $S_n$. On $S^\lambda$ it acts by

```math
 a_\lambda=\binom nk(k-1)!
 \frac{\chi^\lambda(\tau_k)}{\dim S^\lambda},
```

where $\tau_k$ is a $k$-cycle. Multiplicity-free branching gives

```math
 S^\lambda\!\downarrow_{S_{n-1}}
 =\bigoplus_{\mu\nearrow\lambda}S^\mu.
```

On the child $S^\mu$, the second class sum acts by the scalar

```math
 b_\mu=\binom{n-1}{k}(k-1)!
 \frac{\chi^\mu(\tau_k)}{\dim S^\mu}.
```

Every branch eigenvalue is therefore exactly

```math
 E_{\lambda,\mu}(t)=ta_\lambda+(1-t)b_\mu,              \tag{2.2}
```

with multiplicity $\dim S^\mu$.

We use the published non-strict Aldous bound for the normal single-cycle
class: for $n\ge5$ and $2\le k\le n-2$, every nondegree irreducible block
of $K_{n,k}$ has scalar at most

```math
 a_{\mathrm{std}}=\binom nk(k-1)!\frac{n-k-1}{n-1}.
                                                               \tag{2.3}
```

This is the only external spectral inequality required here. The full-range
normal-class result is due to Li, Xia, and Zhou [2]; its range and value are
also recorded in the introduction of [1]. No representation-level uniqueness
for that normal class is assumed.

Put $d_0=\binom{n-1}{k}(k-1)!$. Degree equality $b_\mu=d_0$ means that
the child has a vector fixed by every $k$-cycle in $S_{n-1}$. Thus $\mu$ must
be trivial for even $k$, and trivial or sign for odd $k$. By branching,
a trivial child has only the trivial and standard parents; a sign child has
only their conjugate parents. Every nondegree, nontarget parent consequently
has $b_\mu<d_0$ on every child. Equations (2.2) and (2.3) now give

```math
 E_{\lambda,\mu}(t)
 <ta_{\mathrm{std}}+(1-t)d_0\qquad(0<t<1).              \tag{2.4}
```

The standard parent restricts to the trivial child $(n-1)$ and the standard
child $(n-2,1)$. Both have the same $a_{\mathrm{std}}$ term, while only the
trivial child has $b_\mu=d_0$. Its dimension is one. This proves that the
right side of (2.4) is the simple standard top eigenvalue. For odd $k$, sign
twisting gives the identical simple root in the conjugate standard parent.
Multiplying by $c^k$ proves Theorem 1.

## 3. Three-cycle scalars and two-step branching

Let $C_m$ be the class sum of all three-cycles in $S_m$. For a box $z$ in a
Young diagram, let $\operatorname{ct}(z)$ be its column minus its row. Define

```math
 \kappa(\alpha)=\sum_{z\in\alpha}\operatorname{ct}(z)^2
 -\binom{|\alpha|}{2}.                                   \tag{3.1}
```

This is the scalar of $C_m$ on $S^\alpha$. Indeed, for the Jucys–Murphy
elements $J_i=\sum_{j<i}(ji)$, direct expansion gives

```math
 C_m=\sum_{i=1}^mJ_i^2-\binom m2\,1.
```

The diagonal terms in $J_i^2$ contribute $i-1$ copies of the identity; its
ordered off-diagonal terms are exactly the two three-cycles on each triple
whose largest point is $i$. In a Young path basis, $J_i$ acts by the content
of the box containing $i$, yielding (3.1). Content squares also show
$\kappa(\alpha')=\kappa(\alpha)$.

### 3.1 A scalar hierarchy

For $m\ge3$, write

```math
 K_m=\kappa((m)),\qquad A_m=\kappa((m-1,1)),
```

and for $m\ge5$ write $B_m=\kappa((m-2,1,1))$. Then

```math
 \begin{aligned}
 \kappa(\alpha)&\le A_m
 &&\text{if $\alpha$ is neither a row nor a column},\\
 \kappa(\alpha)&\le B_m
 &&\text{if $m\ge5$ and $\alpha$ is also neither standard nor conjugate standard},\\
 K_m-A_m&=m(m-2), & A_m-B_m&=m(m-4).                    \tag{3.2}
 \end{aligned}
```

To prove these statements, use the Frobenius coordinates
$(u_i\mid v_i)_{i=1}^{\ell}$ of $\alpha$ and put
$F(z)=\sum_{j=1}^zj^2$. The diagonal hooks give

```math
 \sum_{z\in\alpha}\operatorname{ct}(z)^2
 =\sum_{i=1}^{\ell}[F(u_i)+F(v_i)].                     \tag{3.3}
```

If $\ell=1$, then $u_1+v_1=m-1$. Conjugate if necessary so that
$u_1\ge v_1$. For fixed sum, $F(u_1)+F(v_1)$ strictly decreases as the
smaller coordinate moves toward the midpoint. The first three possibilities
$v_1=0,1,2$ are respectively the row, standard, and $(m-2,1,1)$ shapes.
This gives (3.2) for hooks.

If $\ell\ge2$, at least two Frobenius coordinates are positive and their
sum is $m-\ell\le m-2$. Convexity of $F$ bounds their square sum by

```math
 F(m-3)+F(1)<F(m-3)+F(2).                              \tag{3.4}
```

The last expression is the content-square sum of $(m-2,1,1)$. For $m\ge5$
this proves the second bound, hence also the first. For $m=4$, the only
nonhook is $(2,2)$, and (3.4) bounds it strictly below the standard shape;
for $m=3$ every diagram is a hook. Subtracting the relevant hook square
sums gives the two displayed gaps in (3.2).

### 3.2 Exact multiplicity-space matrices

Let $N=n-2$ and let $H=S_N$ permute the repeated-tail points. Consider an
operator of the form

```math
 T=a_0C_n+b_0C_{n-1}^{(2)}+c_0C_{n-1}^{(1)}+d_0C_N,    \tag{3.5}
```

where $C_{n-1}^{(i)}$ is the three-cycle class sum in the stabilizer of
special point $i$. The multiplicity of $S^\nu$, $\nu\vdash N$, in
$S^\lambda\downarrow_H$ is the number of paths
$\nu\nearrow\mu\nearrow\lambda$, and is at most two.

Choose the path basis along the stabilizer of point $2$. A one-path
multiplicity space through $\mu$ has the scalar

```math
 a_0\kappa(\lambda)+d_0\kappa(\nu)
 +(b_0+c_0)\kappa(\mu).                                \tag{3.6}
```

On a two-path space through $\mu_1,\mu_2$, put
$D=\operatorname{diag}(\kappa(\mu_1),\kappa(\mu_2))$.
Swapping the special points conjugates one point-stabilizer class sum into
the other. If the two added boxes have axial distance $e\ge2$, the Young
orthogonal matrix of this swap is, up to a choice of signs,

```math
 U_e=\begin{pmatrix}e^{-1}&\sqrt{1-e^{-2}}\\
 \sqrt{1-e^{-2}}&-e^{-1}\end{pmatrix}.
```

Thus the full multiplicity-space matrix is explicitly

```math
 [a_0\kappa(\lambda)+d_0\kappa(\nu)]I_2
 +b_0D+c_0U_eDU_e.                                    \tag{3.7}
```

Its eigenvalues are

```math
 \begin{aligned}
 E^{\pm}_{\lambda,\nu}
 ={}&a_0\kappa(\lambda)+d_0\kappa(\nu)
 +\frac{b_0+c_0}{2}[\kappa(\mu_1)+\kappa(\mu_2)]\\
 &\quad\pm\frac{|\kappa(\mu_1)-\kappa(\mu_2)|}{2}
 \sqrt{b_0^2+c_0^2+2b_0c_0(2e^{-2}-1)}.                \tag{3.8}
 \end{aligned}
```

Equations (3.6)–(3.8) account for every irreducible block. The multiplicity
matrix acts identically on each copy of the $S^\nu$ factor. These formulas
come from branching and the displayed Young orthogonal matrix, rather than
from a finite enumeration of partitions.

## 4. The regime $b<c$: a repeated larger tail

Positive rescaling reduces this case to

```math
 x=(t,1,q,\ldots,q),\qquad 0<t<1<q.
```

The support decomposition is

```math
 T=tqC_n+tq(q-1)C_{n-1}^{(2)}+q(q-t)C_{n-1}^{(1)}
 +q(q-1)(q-t)C_N.                                     \tag{4.1}
```

For supports containing both special points the coefficient is $tq$;
for those containing only point $1$ it is $tq+tq(q-1)=tq^2$; for those
containing only point $2$ it is $tq+q(q-t)=q^2$; and the sum of all four
coefficients for tail-only supports is $q^3$. These are the required weights.

Put

```math
 a_0=tq,\quad d_0=q(q-1)(q-t),\quad
 \beta=tq(q-1),\quad\delta=q(q-t),\quad s_0=\beta+\delta.
```

All these quantities are positive. Define

```math
 R_e=\beta^2+\delta^2+2\beta\delta(2e^{-2}-1).
```

Then

```math
 R_e=(\beta-\delta)^2+4\beta\delta e^{-2}>0,
 \qquad s_0^2-R_e=4\beta\delta(1-e^{-2})>0.             \tag{4.2}
```

Both one- and two-path top roots consequently satisfy

```math
 E^+_{\lambda,\nu}\le a_0\kappa(\lambda)+d_0\kappa(\nu)
 +s_0\max_{\nu\nearrow\mu\nearrow\lambda}\kappa(\mu).  \tag{4.3}
```

For the standard parent $\lambda_0=(n-1,1)$, the bottom child
$\nu_0=(n-2)$ has two paths through $(n-1)$ and $(n-2,1)$.
Their axial distance is $n-1$. Its upper root is

```math
 \begin{aligned}
 \Lambda={}&a_0A_n+d_0K_{n-2}
 +\frac{s_0}{2}(K_{n-1}+A_{n-1})\\
 &+\frac{K_{n-1}-A_{n-1}}{2}\sqrt{R_{n-1}}.
                                                               \tag{4.4}
 \end{aligned}
```

Let $\Lambda_0$ be the same expression without its last term. Equations
(3.2) and (4.2) give $\Lambda>\Lambda_0$ and two distinct roots. Because
$\nu_0$ is one dimensional, the upper root is simple in this component.
The only other standard $S_N$ type is $(n-3,1)$, through $(n-2,1)$;
its scalar is

```math
 E_{\mathrm{other}}=a_0A_n+d_0A_{n-2}+s_0A_{n-1}.
```

It is strictly below $\Lambda_0$ because

```math
 \Lambda_0-E_{\mathrm{other}}
 =d_0(K_{n-2}-A_{n-2})
 +\frac{s_0}{2}(K_{n-1}-A_{n-1})>0.                    \tag{4.5}
```

Thus $\Lambda$ is the simple top eigenvalue of the whole standard block.

Now exclude degree and standard-type parents. An intermediate child $\mu$
cannot be trivial or sign: adding one box to either gives only an excluded
parent. Hence

```math
 \kappa(\lambda)\le B_n,\qquad \kappa(\mu)\le A_{n-1}.
```

If $\nu$ is neither trivial nor sign, (3.2) and (4.3) give

```math
 E^+_{\lambda,\nu}\le a_0B_n+d_0A_{n-2}+s_0A_{n-1},
```

and therefore

```math
 \Lambda_0-E^+_{\lambda,\nu}
 \ge a_0(A_n-B_n)+d_0(K_{n-2}-A_{n-2})
 +\frac{s_0}{2}(K_{n-1}-A_{n-1})>0.                    \tag{4.6}
```

If $\nu$ is trivial or sign, the only remaining parents are $(n-2,2)$,
$(n-2,1,1)$, and their conjugates. Each has one intermediate standard-type
child. Consequently

```math
 E^+_{\lambda,\nu}\le a_0B_n+d_0K_{n-2}+s_0A_{n-1},
```

so

```math
 \Lambda_0-E^+_{\lambda,\nu}
 \ge a_0(A_n-B_n)+\frac{s_0}{2}(K_{n-1}-A_{n-1})>0.    \tag{4.7}
```

The displayed gaps are positive for every $n\ge5$, since
$A_n-B_n=n(n-4)>0$. Equations (4.6) and (4.7) exclude every competitor.

## 5. The regime $b>c$: one larger exceptional point

Rescaling reduces this case to

```math
 x=(t,Q,1,\ldots,1),\qquad 0<t<1<Q.
```

Here the exact decomposition is

```math
 T=tQC_n-t(Q-1)C_{n-1}^{(2)}+Q(1-t)C_{n-1}^{(1)}
 -(1-t)(Q-1)C_N.                                      \tag{5.1}
```

The support coefficients are respectively $tQ$, $t$, $Q$, and $1$ for
the four support types used in Section 4. Two coefficients in (5.1) are
negative, so the positive-coefficient comparison (4.3) is not available.

Write

```math
 a_0=tQ,\quad b_0=-t(Q-1),\quad c_0=Q(1-t),\quad
 d_0=-(1-t)(Q-1),\quad \sigma=b_0+c_0=Q+t-2tQ.
```

Put $u=-b_0=t(Q-1)>0$, $v=c_0=Q(1-t)>0$, and $P=Q+t$.
Then $u+v=Q-t$, $v-u=\sigma$, and $a_0(-d_0)=uv$. The root in
(3.8) is

```math
 \rho_e=\sqrt{(Q-t)^2-4tQ(1-t)(Q-1)e^{-2}}.             \tag{5.2}
```

For every $e\ge2$,

```math
 0\le|\sigma|<\rho_e<Q-t<P,                            \tag{5.3}
```

and $\rho_e$ strictly increases with $e$. Indeed,
$\rho_e^2-\sigma^2=4uv(1-e^{-2})>0$, while its squared difference
from $(Q-t)^2$ is negative. The value $\sigma=0$ is allowed.

### 5.1 Content form of all roots

In a two-path interval, let $x,y$ be the contents of its two added boxes.
Then $e=|x-y|$ and

```math
 \begin{aligned}
 \kappa(\lambda)&=\kappa(\nu)+x^2+y^2-(2N+1),\\
 \{\kappa(\mu_1),\kappa(\mu_2)\}
 &=\{\kappa(\nu)+x^2-N,\ \kappa(\nu)+y^2-N\}.
 \end{aligned}
```

Using $a_0+d_0+\sigma=1$ and $2a_0+\sigma=P$, equation (3.8)
becomes

```math
 F_N(\nu;x,y)=\kappa(\nu)+\frac P2(x^2+y^2)
 +\frac{\rho_e}{2}|x^2-y^2|-NP-tQ.                    \tag{5.4}
```

A one-path interval adds a horizontal or vertical domino. If $x$ is the
content added first and $y=x\pm1$ is added second, its scalar becomes

```math
 G_N(\nu;x,y)=\kappa(\nu)+(P-tQ)x^2+tQy^2-NP-tQ.      \tag{5.5}
```

Both coefficients $P-tQ=Q(1-t)+t$ and $tQ$ are positive. These formulas
retain the order of addition in the one-path case.

### 5.2 The standard top root

The standard parent $(N+1,1)$ has a two-path component over $\nu=(N)$,
with added contents $N,-1$ and axial distance $N+1$. Put
$\rho=\rho_{N+1}$. Its upper root is

```math
 \Lambda=K_N+\frac P2(N^2+1)+\frac\rho2(N^2-1)-NP-tQ.  \tag{5.6}
```

The roots are distinct by (5.3) and $N^2-1>0$, and this component has
one-dimensional $S^\nu$ factor. The other standard component is the one-path
interval from $(N-1,1)$ with added contents $N-1,N$.

To compare it with (5.6), first replace $\rho$ by $Q-t$. The difference
is exactly

```math
 \Delta_0=(1-t)[N^2+2NQ-2N-Q].                         \tag{5.7}
```

The loss from using the actual $\rho$ is
$\frac12(N^2-1)[(Q-t)-\rho]$. Rationalization gives

```math
 (Q-t)-\rho
 =\frac{4tQ(1-t)(Q-1)}{(N+1)^2[(Q-t)+\rho]}
 <\frac{4tQ(1-t)(Q-1)}{(N+1)^2(Q-t)}.
```

Since $t(Q-1)/(Q-t)<1$, this loss divided by $1-t$ is smaller than
$2Q(N-1)/(N+1)$. On the other hand,

```math
 N^2+2NQ-2N-Q=N(N-2)+Q(2N-1)
 >\frac{2Q(N-1)}{N+1}\qquad(N\ge3).
```

Thus the actual difference is positive. Equation (5.6) is the simple top
eigenvalue of the complete standard block.

### 5.3 All two-path competitors

For a nondegree, nonstandard-type two-path parent, the bottom partition
$\nu$ is neither a row nor a column. Otherwise its two distinct addable
corners produce only a standard-type parent. Hence
$\kappa(\nu)\le A_N$.

For two different addable corners of a non-row, non-column partition
$\nu\vdash N$, their contents satisfy

```math
 \max(x^2,y^2)\le(N-1)^2,\quad
 x^2+y^2\le(N-1)^2+4,\quad |x-y|\le N+1.              \tag{5.8}
```

Indeed, the largest positive and negative absolute contents are bounded by
the first row length and the number of rows. Both are at most $N-1$, and
their sum is at most $N+1$. For opposite signs, the maximal squared sum
under these integer bounds is attained at absolute values $N-1,2$.
For two positive contents $x>y>0$ in distinct rows, the corresponding row
lengths are at least $x$ and $y+1$, so $x+y\le N-1$ and their squared sum
is smaller. Negative contents follow by conjugation; a zero content causes
no exception. The same row-length bounds give the axial-distance bound.

Define

```math
 \alpha=\frac{P+\rho}{2},\qquad\beta=\frac{P-\rho}{2},
 \qquad\alpha>\beta>0.
```

For $X=\max(x^2,y^2)$ and $Y=\min(x^2,y^2)$, (5.2) and (5.8) give

```math
 \begin{aligned}
 \frac P2(X+Y)+\frac{\rho_e}{2}(X-Y)
 &\le\alpha X+\beta Y\\
 &=(\alpha-\beta)X+\beta(X+Y)\\
 &\le\alpha(N-1)^2+4\beta.                              \tag{5.9}
 \end{aligned}
```

Thus every two-path competitor is at most

```math
 \Lambda_C=A_N+\frac P2[(N-1)^2+4]
 +\frac\rho2[(N-1)^2-4]-NP-tQ.                         \tag{5.10}
```

This expression is the upper root of the interval from $(N-1,1)$ to
$(N,1,1)$ with contents $N-1,-2$. Direct subtraction, using
$K_N-A_N=N(N-2)$, gives

```math
 \Lambda-\Lambda_C=(N-2)(N+Q+t)+(N+1)\rho>0.           \tag{5.11}
```

All two-path competitors are therefore strictly excluded.

### 5.4 All one-path competitors

It remains to compare (5.5) with (5.6). Removing their common constant
$-NP-tQ$, the required inequality is

```math
 \kappa(\nu)+(P-tQ)x^2+tQy^2
 <K_N+\alpha N^2+\beta.                                \tag{5.12}
```

First suppose $\nu$ is neither a row nor a column. Its first added content
has $|x|\le N-1$. The intermediate partition is still neither a row nor a
column. If the second content had $|y|=N$, that intermediate partition
would be $(N,1)$ or its conjugate; continuing the same horizontal or vertical
domino would produce the excluded standard parent or its conjugate.
Consequently $|x|,|y|\le N-1$. The positive coefficients in (5.5) sum to
$P$, so the left side of (5.12) is at most $A_N+P(N-1)^2$.

The difference between the right side and this bound is

```math
 H=N(N-2)(1-\beta)+\alpha(2N-1).                       \tag{5.13}
```

If $\beta\le1$, it is strictly positive. For $\beta>1$, put

```math
 h_0=Q-t,\qquad E=\frac{4tQ(1-t)(Q-1)}{(N+1)^2},
 \qquad\rho=\sqrt{h_0^2-E}>0.
```

Positivity follows also from $h_0=u+v$, $E=4uv/(N+1)^2$, and
$4uv\le(u+v)^2$ with $N+1\ge4$. Rationalization yields

```math
 \beta=t+\frac{h_0-\rho}{2}
 =t+\frac E{2(h_0+\rho)}<t+\frac E{2h_0}.
```

Since $t<1$, it follows that

```math
 N(N-2)(\beta-1)
 <\frac{2tQ\,N(N-2)(1-t)(Q-1)}{(N+1)^2(Q-t)}.         \tag{5.14}
```

Equation (5.3) gives $\alpha>tQ$: indeed
$2tQ-P=-\sigma\le|\sigma|<\rho$. Moreover,

```math
 \frac{N(N-2)}{(N+1)^2}<1,\qquad
 \frac{(1-t)(Q-1)}{Q-t}<1.
```

The right side of (5.14) is therefore strictly less than $2\alpha$.
Equation (5.13) gives

```math
 H>\alpha(2N-1)-2\alpha=\alpha(2N-3)>0.
```

This proves (5.12) for every non-row, non-column bottom partition, with no
restriction on the size of $Q$.

Now let $\nu=(N)$; the column case follows by conjugation. The one-path
domino possibilities are: two boxes in the first row, giving the excluded
degree parent; two boxes in the second row, with contents $-1,0$, giving
$(N,2)$; or two boxes down the first column, with contents $-1,-2$, giving
$(N,1,1)$. In the last two cases $x^2,y^2\le4$ and $\kappa(\nu)=K_N$,
so their angle term is at most $4P$. The standard angle term has excess

```math
 \alpha N^2+\beta-4P
 =\alpha(N^2-4)-3\beta
 >\beta(N^2-7)>0\qquad(N\ge3).
```

Thus (5.12) holds for row and column bottom children as well. This exhausts
all one-path competitors. Together with (5.11), it proves strict dominance
over every nondegree, nonstandard-type block in the reflected regime.

## 6. Joining the three regimes and computing the standard root

Multiplying all activities by a positive number $h$ multiplies $T_3$ by
$h^3$, preserving eigenvalue order, attaining representations, and block
multiplicity. The three regimes for Theorem 2 are consequently exhausted as
follows:

* If $b<c$, divide by $b$: $t=a/b$ and $q=c/b$ satisfy $0<t<1<q$,
  and Section 4 applies.
* If $b=c$, divide by $c$ and apply Theorem 1 with $k=3$.
* If $b>c$, divide by $c$: $t=a/c$ and $Q=b/c$ satisfy $0<t<1<Q$,
  and Section 5 applies.

Each proof identifies the simple top standard root and excludes all
nondegree competitors. Three-cycles are even, so the conjugate standard
representation has the identical operator. This proves the attaining-block
and simplicity assertions in Theorem 2.

For completeness, the standard root has the unified form (1.2). In the natural
permutation representation, the sum of a three-cycle and its inverse on a
triple has group-Laplacian contribution equal to the edge Laplacian of its
three-point complete graph. Thus the conductance between points $i,j$ is

```math
 w_{ij}=x_ix_j\sum_{\ell\ne i,j}x_\ell.
```

For the classes $\{a\}$, $\{b\}$, and the $N$ repeated $c$ points, these
conductances are $p,r,s$ as defined in Theorem 2. On vectors constant on
each class, the natural Laplacian has quotient

```math
 L_{\mathrm{quot}}=
 \begin{pmatrix}
 p+Nr&-p&-Nr\\
 -p&p+Ns&-Ns\\
 -r&-s&r+s
 \end{pmatrix}.                                       \tag{6.1}
```

This quotient is self-adjoint for the class-size metric
$\operatorname{diag}(1,1,N)$ and has zero row sums. The trace is
$\mathcal T$, and the sum of its three principal two-by-two minors is
$\mathcal S$. Hence its two nonzero roots are

```math
 \frac{\mathcal T\pm\sqrt{\mathcal T^2-4\mathcal S}}2.
```

Both are positive because the three interclass conductances are positive.
The remaining natural modes are the tail-internal zero-sum vectors. Sections
4 and 5 identify the two-path component over the trivial $S_N$ child as
the strictly top standard adjacency component and exclude the other standard
child; Section 2 does the same when $b=c$. The class-constant subspace is
precisely the trivial $S_N$ isotypic component in the natural representation.
Its constant line has zero gap, and its other two dimensions lie in the
standard representation. Therefore the smaller nonzero root of (6.1) is the
smallest standard Laplacian root, is simple, and gives (1.2) after subtracting
it from the degree. All competitor adjacency roots are strictly below
$D_3(x)-\gamma$, equivalently all competitor Laplacian roots are strictly
above $\gamma$.

## References and dependencies

[1] Yuxuan Li, Binzhou Xia, and Sanming Zhou, *The second largest eigenvalue of
some nonnormal Cayley graphs on symmetric groups*, Journal of Combinatorial
Theory, Series A **218** (2026), 106097.
[Version of record](https://doi.org/10.1016/j.jcta.2025.106097);
[public preprint](https://arxiv.org/html/2402.02427v1).
Section 2 records the branching, conjugate-partition, and generation
conventions used here.

[2] Yuxuan Li, Binzhou Xia, and Sanming Zhou, *The second largest eigenvalue of
normal Cayley graphs on symmetric groups generated by cycles*.
[Public preprint, arXiv:2302.04022](https://arxiv.org/abs/2302.04022).
The singleton cycle-length case supplies the non-strict bound (2.3).

The only external spectral comparison in these proofs is the non-strict normal
single-cycle bound (2.3). The Young branching rule, the Young orthogonal form,
and the content action of Jucys–Murphy elements are the classical
representation-theoretic inputs. All activity decompositions, root formulas,
uniform competitor comparisons, and the unified standard quotient used in
Theorems 1 and 2 are displayed above. No finite diagnostic or stored
certificate flag is a premise.
