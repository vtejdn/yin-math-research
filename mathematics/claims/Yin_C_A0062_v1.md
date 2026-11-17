---
author: Yin
---
# A single series of finite product moments for kernel decay on the whole four-line group

## Statement

Fix a finitely generated group \(G\), a finite group-ring matrix \(A\) with \(m\) columns, \(B=A^*A/M\) with \(M>\|A\|^2\), and \(Q_k=(I-B)^k\).
Use the rose word length on a four-line group, or any fixed finite generating set in the general statement.
Write \(p=1_{\{0\}}(B)\), \(\tau_m=\operatorname{Tr}_m\otimes\tau_G\), and \(\|X\|_2^2=\tau_m(X^*X)\).
For \(3<\beta<4\), consider the finite weighted moment
\[
   D_k(s)=\sum_g(1-e^{-s|g|})^4\|\widehat Q_k(g)\|_{\rm HS}^2.
\]
The two words defining a squared coefficient must end at the same element of \(G\). [C57, statement](Yin_C_A0057_v1.md#statement)
For any increasing positive integers \(k_j\to\infty\), define
\[
 \begin{split}
   \mathcal S(k_\bullet)=\sum_{j\ge0}2^{\beta j}\big[&
       D_{k_j}(2^{-j})+
       \tau_m(Q_{2k_j}+Q_{2k_{j+1}}-2Q_{k_j+k_{j+1}})\big].
 \end{split}                                                       \tag{1}
\]
Each summand is computed from finitely many product fibers in the original group.
The bracket contains only nonnegative contributions since the second term is the squared \(L^2(\tau_m)\) norm of an increment.
Then \(\sum_g(1+|g|)^\beta\|\widehat p(g)\|_{\rm HS}^2<\infty\) if and only if some schedule has \(\mathcal S(k_\bullet)<\infty\).
For a prescribed schedule with a summable weighted increment term, summability of the weighted endpoint term alone is equivalent to the projection condition.
Let \(\mathcal S_{\ge J}\) denote the tail of (1) starting at index \(J\).
For every \(R\ge1\), with \(J=\lfloor\log_2 R\rfloor\), one has the explicit bound
\[
 \sum_{|g|\ge R}(1+|g|)^\beta\|\widehat p(g)\|_{\rm HS}^2
 \le \frac{2^{2\beta+1}}{(1-e^{-1})^4(1-2^{-\beta/2})^2}\,\mathcal S_{\ge J}.    \tag{2}
\]
On a good four-line group this condition implies integral kernel dimension. [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace)

Suppose the positive spectral mass satisfies \(F_B(t)=\tau_m(1_{(0,t]}(B))\asymp t^\alpha\) at zero for some \(\alpha>0\).
For a projection satisfying the spatial condition, (1) is finite exactly when \(\sum_j2^{\beta j}k_j^{-\alpha}<\infty\).
For \(k_j\asymp2^{\kappa j}\), this is precisely \(\kappa\alpha>\beta\).
When only the corresponding upper mass bound is known, that strict inequality still suffices to make the weighted increments summable.

On every fixed pattern-free four-line group and for every integer \(d\ge1\), there is a rational-coefficient \(2\)-by-\(3\) matrix of nonclosed range with rank-one kernel projection of exponential Fourier decay and \(F_B(t)\asymp t^{1/(4d)}\).
The input and its projection each generate the whole group in the following support sense: even after multiplying the rows and columns independently by group units, their entries cannot all be carried by a proper subgroup.
The construction has two noncommuting coefficient polynomials.
A second choice based on the spectral radius of a generating random walk on the same group has exponent \(3/(4d)\).
Thus (1) has the respective sharp thresholds \(\kappa>4d\beta\) and \(\kappa>4d\beta/3\) for these genuine nonclosed-range matrices.

## Argument

Put \(e_j=\|Q_{k_j}-p\|_2\), \(a_j=\|Q_{k_{j+1}}-Q_{k_j}\|_2\).
The finite return expression in (1) is exactly \(a_j^2\), since the powers are selfadjoint and commute.
Spectral convergence gives \(Q_{k_j}\to p\) in trace \(L^2\).
Hence \(a_j\le e_j+e_{j+1}\), and telescoping gives \(e_j\le\sum_{h\ge0}a_{j+h}\).
After multiplication by \(2^{\beta j/2}\), the last sum is bounded in sequence \(\ell^2\) by convolution with \((2^{-\beta h/2})_{h\ge0}\), whose sum is finite.
Consequently
\[
         \sum_j 2^{\beta j} e_j^2<\infty
                  \quad\Longleftrightarrow\quad
         \sum_j 2^{\beta j} a_j^2<\infty .                              \tag{3}
\]
Taking the coefficient \(\ell^2\) norm after multiplication by \((1-e^{-2^{-j}|g|})^2\) gives the square root of the endpoint moment.
This multiplier contracts the coefficient \(\ell^2\) norm, so replacing \(Q_{k_j}\) with \(p\) changes the square root by at most \(e_j\).
The [dyadic comparison in C57](Yin_C_A0057_v1.md#argument) identifies the weighted sum for \(p\) with its spatial moment up to a fixed factor and the finite identity coefficient.
This proves the assertion for a prescribed schedule.
If the projection has the required decay, its trace \(L^2\) convergence allows successive \(k_j\) to be chosen with \(e_j\le2^{-(1+\beta)j/2}\), proving the existential direction.
The convergence rate used for that existence need not be known.

For the tail bound, each integer \(r=|g|\ge R\) has \(j=\lfloor\log_2 r\rfloor\ge J\) and
\((1+r)^\beta\le2^{2\beta}(1-e^{-1})^{-4}2^{\beta j}(1-e^{-2^{-j}r})^4\).
Thus the left side of (2) is at most \(2^{2\beta}(1-e^{-1})^{-4}\sum_{j\ge J}2^{\beta j}D_p(2^{-j})\), with \(D_p\) defined by using \(p\) in place of \(Q_k\).
The multiplier estimate gives \(D_p(2^{-j})\le 2 D_{k_j}(2^{-j})+2e_j^2\).
The preceding convolution bound restricted to \(j\ge J\) uses only \(a_{j+h}\) for \(h\ge0\).
Hence \(\sum_{j\ge J}2^{\beta j}e_j^2\le (1-2^{-\beta/2})^{-2}\sum_{j\ge J}2^{\beta j}a_j^2\), which gives (2).

The uncorrected choice \(k_j=j+1\) always has summable endpoint terms for this range of \(\beta\).
Indeed the support of \(Q_k\) lies in radius \(wk\) for some \(w\ge1\), and \(\|Q_k\|_2\le\sqrt m\).
This makes \(D_{j+1}(2^{-j})\le m(2^{-j}w(j+1))^4\).
The increment term controls the approximation error that such a diagonal misses.

The squared error at time \(k\) equals \(\int_{(0,1]}(1-t)^{2k}\,dF_B(t)\).
If \(F_B(t)\le Ct^\alpha\) at small \(t\), increase the constant to cover \((0,1]\).
The majorant \(e^{-2kt}\) and integration by parts bound the error squared by \(m e^{-2k}+2k C\int_0^1 e^{-2kt}t^\alpha dt=O(k^{-\alpha})\).
If also \(F_B(t)\ge c t^\alpha\) there, integrating on \((0,1/(4k)]\) gives the matching lower bound.
Now (3) gives the schedule criterion, including divergence at equality for geometric schedules.
With exponential localization of \(p\), one also has \(D_p(2^{-j})=O(2^{-4j})\) by its finite fourth spatial moment.
For the convergent geometric schedules in the examples, the tail after index \(J\) of (1) is consequently \(O(2^{-(4-\beta)J}+2^{-(\kappa\alpha-\beta)J})\), by the multiplier bound and \(a_j\le e_j+e_{j+1}\).

## A rational example using the whole group

Let \(S\) be the finite symmetric set of distinct nonidentity rose generators and their inverses in the fixed group.
Let \(P=(I+|S|^{-1}\sum_{s\in S}s)/2\), a positive contraction giving a lazy symmetric walk that generates \(G\).
The group is nonabelian because its [two nonzero binary factors have zero product](Yin_C_A0051_v1.md#statement), whereas any finite pair of supports in a torsion-free abelian group lies in a Laurent polynomial domain.
Choose a noncentral \(u\in S\) and enumerate \(\{e\}\cup S=\{g_0,\ldots,g_l\}\).
Set \(U=\sum_{i=0}^l2^{-i-1}g_i\), \(V=U+u\).
The positive coefficients of \(U\) are distinct, so a group element commuting with \(U\) must fix each of its support elements by conjugation and hence must be central.
It follows that \(UV\ne VU\).
Both supports contain the identity and a generating set.
With \(x=1-u\) put
\[
       Y=\frac{x^*(8I+P)x}{36},\qquad
       T=\begin{pmatrix}1&U&0\\0&1&V\end{pmatrix},\qquad
       A_d=\begin{pmatrix}1&0\\0&Y^d\end{pmatrix}T .                  \tag{4}
\]
All coefficients in (4) are rational.
The positive contraction \(Y\) satisfies \((8/9)Y_0\le Y\le Y_0\) for \(Y_0=x^*x/4\).
The infinite-order cyclic shift gives \(\tau(1_{[0,t]}(Y_0))=2\arcsin(\sqrt t)/\pi\) for \(0\le t\le1\), including zero mass at zero.
For positive operators \(C\le D\) in a finite matrix von Neumann algebra one has \(\tau_m(1_{[0,t]}(D))\le\tau_m(1_{[0,t]}(C))\).
Indeed the ranges of \(1_{[0,t]}(D)\) and \(1_{(t,\infty)}(C)\) have zero intersection by the quadratic form inequality, so the sum of their dimensions is at most \(m\).
Thus \(Y\) is injective with nonclosed range and \(F_Y(t)\asymp t^{1/2}\).

This scalar that causes the nonclosed range already requires the whole group.
Its coefficient at \(u\) is nonzero because the coefficient of \(8x^*x\) there is \(-8\), whereas \(\|x^*P x\|\le4\).
If \(Y\in\mathcal N(H)\) for a subgroup \(H\), then \(u\in H\), and \(x\) has an inverse affiliated with \(\mathcal N(H)\) by the cyclic shift calculation.
In the affiliated ring of \(H\), multiplying \(36Y\) by \((x^*)^{-1}\) on the left and \(x^{-1}\) on the right recovers \(8I+P\).
Indeed the affiliated inclusion into the ambient ring is the same direct sum on right cosets as for bounded subgroup operators, and a bounded element affiliated with \(\mathcal N(H)\) belongs to \(\mathcal N(H)\).
The support of \(P\) then forces \(H=G\).
The same holds for \(Y^d\) by its positive \(d\)-th root.
Its positive identity coefficient implies that translating it on either side can at most conjugate this subgroup test.

The row pair \(T\) has bounded right inverse \((a,b)\mapsto(a-Ub,b,0)\).
Thus \(c I_2\le TT^*\le C I_2\) for constants \(0<c\le C\).
The range of (4) is \(\ell^2(G)\oplus\operatorname{ran}Y^d\), which is nonclosed.
Sandwiching the bounds on \(TT^*\) by \(\operatorname{diag}(1,Y^d)\) gives comparison of \(A_d A_d^*\) with \(\operatorname{diag}(1,Y^{2d})\) in the same positive order.
The former has no atom at zero, and the positive spectral trace measures of \(A_d A_d^*\) and \(A_d^*A_d\) agree by polar decomposition.
The spectral comparison therefore gives \(F_{A_d^*A_d/M}(t)\asymp t^{1/(4d)}\) for any allowed fixed \(M\).

The kernel of (4) is the graph column \(W=(UV,-V,I)^t\) applied to \(\ell^2(G)\).
Since \(W^*W\ge I\), its orthogonal projection is \(p=W D W^*\) with \(D=(W^*W)^{-1}\).
The polar isometry of \(W\) shows that \(\tau_3(p)=1\).
Geometric inverse sums for \(D\) have propagation growing linearly and operator norm error decreasing geometrically. [C58, bounded rational inverses](Yin_C_A0058_v1.md#bounded-rational-inverses-have-exponential-tails)
Thus \(p\) has an exponentially weighted square sum in the ambient word metric, giving the spatial part of (1).

To check support after translations, suppose that a subgroup \(H\) carries all entries after multiplying the rows by \(a_i\in G\) on the left and the columns by \(b_j\in G\) on the right.
For the input the entry \(a_1 U b_2\) then has support in \(H\).
Since \(U\) contains the identity and the whole generating set, \(a_1b_2\in H\) and \(b_2^{-1}G b_2\subset H\), so \(H=G\).
For the projection, \(p_{33}=D\) has strictly positive identity coefficient, and \(p_{23}=-VD\).
The inclusion \(a_3 D b_3\in\mathcal N(H)\) implies \(a_3b_3\in H\), so \(b_3^{-1}D b_3\) and its bounded inverse belong to \(\mathcal N(H)\).
Combining this inverse with \(a_2 p_{23} b_3\) gives \(a_2 V b_3\in\mathcal N(H)\).
Its support again contains \(a_2b_3\) and every \(a_2s b_3\) with \(s\in S\), forcing \(H=G\).
Here membership in \(\mathcal N(H)\) for a bounded multiplier is equivalent to Fourier support in \(H\) by the subgroup conditional expectation.
These arguments allow the translations of the output and input coordinates to be independent, including on the projection.
C57 gives exponential decay after removal of an injective factor, and C58 gives exponential decay for free-subgroup matrices.
In (4) the true kernel projection itself requires coefficients throughout the original group under this subgroup test, and (1) has a sharp rate obtained from the actual positive spectrum.

## The spectral edge of the generating walk

In (4) one may instead take \(Y=I-P/\rho\), where \(\rho=\|P\|\).
This choice uses a real coefficient specified by the walk on the fixed group.
It retains the preceding projection and both full-group support conclusions.
By Gouëzel's local limit theorem the return probabilities satisfy \(\tau(P^k)\sim C\rho^k k^{-3/2}\) for some \(C>0\). [Gou14, Theorem 1.1, author preprint](../literature/pdf/Gou14--arxiv-v1.pdf#page=2)
The walk is admissible since its support generates the group, symmetric by construction, and aperiodic by its identity step.
The good four-line group is non-elementary and word-hyperbolic. [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace)

Let \(z=P/\rho\), a positive contraction, and write \(m_k=\tau(z^k)\).
Since \(m_k\to0\), the spectral measure of \(z\) has no atom at one.
On \([1-1/k,1]\) the function \(z^k\) is bounded below by a fixed positive constant for \(k\ge2\), giving \(\mu_z([1-1/k,1])=O(k^{-3/2})\).
For fixed \(b>0\) and \(k>b\), splitting the integral at \(1-b/k\) gives
\[
               m_{2k}\le \mu_z([1-b/k,1])+e^{-b}m_k .
\]
Choose \(e^{-b}<2^{-3/2}/2\).
The asymptotic ratio \(m_{2k}/m_k\to2^{-3/2}\) gives the matching lower bound on this slightly larger interval.
Monotonicity between consecutive values of \(1/k\) or \(b/k\) proves \(F_Y(t)\asymp t^{3/2}\) for all sufficiently small \(t\).
The same positive comparison in (4) now gives \(F_B(t)\asymp t^{3/(4d)}\).
This uses actual return probabilities for the generating walk; the single multiplication table of the binary factors in C51 does not determine the full collection of higher alternating moments in (1).

## Assessment history

### Decision finite-moment-schedules

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:53 |
| status | proved |
| reason | Independent review verified the equivalence of the schedule and spatial criteria, the explicit tail bound, the power-law thresholds and the two whole-group examples. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The finite-moment series for \(3<\beta<4\), its integrality consequence on good four-line groups, and the two nonclosed-range examples. |
| argument | [Proof](#argument) | Weighted endpoint and increment estimates, prescribed and existential schedules, and the respective spectral exponents \(1/(4d)\) and \(3/(4d)\). |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0098_v1.md#whole-argument-finding) | Independent review of the full criterion and both constructions at their stated coefficient and support scopes. |

## Current assessment

[Selected decision](#decision-finite-moment-schedules)
