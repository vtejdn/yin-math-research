---
author: Yin
---

# Spectral flow between two diagonal sign words of a Hermitian pencil

<a id="statement"></a>
## A positive difference of two sign words

Fix Hermitian \(m\)-square matrices \(C,A_1,\ldots,A_g\) and suppose that for some \(d\in\{-1,0,1\}^g\),
\[
 B=\sum_{j=1}^g d_j A_j\ge c I_m,\qquad c>0.
\]
For each \(N\), let \(W_1,\ldots,W_g\) be independent real symmetric matrices whose upper triangular entries, including the diagonals, are independent fair signs divided by \(\sqrt N\).
Set \(H_N=C\otimes I_N+\sum_j A_j\otimes W_j\) and \(\mathcal S(T)=\sum_j A_j T A_j\).
Fix \(E\in\mathbb R\) such that on the ray \(z=E+i\eta,\ \eta>0\), both the positive-imaginary-part solution \(M\) of \(-M^{-1}=zI-C+\mathcal S(M)\) and the inverse of \(T\mapsto T-M\mathcal S(T)M\) are uniformly bounded.
For sufficiently large \(N\),
\[
 \mathbb P\{s_{\min}(H_N-EI)\le N^{-3}\}\le C_E N^{-1/4}. \tag{1}
\]
Writing \(s_1,\ldots,s_g\) for a free standard semicircular family with trace \(\tau\), define
\[
 U_N=\frac{1}{mN}\log|\det(H_N-EI)|,\qquad
 u_E=\log\Delta_{\operatorname{tr}_m\otimes\tau}
 \left((C-EI_m)\otimes1+\sum_j A_j\otimes s_j\right).
\]
Then \(u_E\) is finite and \(U_N\to u_E\) in probability through all sizes.
Under every cross-size coupling, \(U_{2^k}\to u_E\) and \(\limsup_N U_N=u_E\) almost surely.
These statements concern each fixed energy; they require no individual \(A_j\) to be definite.

<a id="argument"></a>
## Conditioning on the two endpoint counts

Choose two words \(u^-,u^+\in\{\pm1\}^g\) with \(u^+-u^-=2d\).
Call a site's diagonal word active when it is either endpoint, an event of probability \(p=2^{1-g}\).
Conditional on activity the two endpoints are equally likely, and at an inactive site the word is uniform on the remaining words.
Draw the active set, the inactive words and all strict upper triangular entries once according to this law.
Conditional on the active set of size \(r\), choose a uniform permutation of its sites and independently \(Q\sim\operatorname{Bin}(r,1/2)\).
Let \(H_q\) use \(u^+\) at the first \(q\) sites of the permutation and \(u^-\) at the remaining active sites.
Then \(H_Q\) has the original law and each flip increases the matrix by \(2B/\sqrt N\) at its site.

Call \(r\) central if \(|r-pN|\le\sqrt{6N\log N}\), using just \(r=N\) when \(p=1\).
Set \(q_-=\lfloor r/2-\sqrt{6r\log N}\rfloor\) and \(q_+=\lceil r/2+\sqrt{6r\log N}\rceil\); for central \(r\) and large \(N\) these lie in \([0,r]\).
The joint probability of a noncentral \(r\) or \(Q\notin[q_-,q_+]\) is \(O(N^{-10})\) by the binomial tail bound.
Stirling's formula gives \(\mathbb P(r=r_0,Q=q)\ge N^{-K_p}\) uniformly over the central pairs \((r_0,q)\), and \(\sup_q\mathbb P(Q=q\mid r=r_0)\le C_p/\sqrt N\).
Indeed both central displacements are \(O_p(\sqrt{N\log N})\) and the binomial variances are comparable to \(N\), omitting the deterministic first factor when \(p=1\).
Given \(r=r_0\), the state at a deterministic \(q\) has the original law conditioned on both counts \((r_0,q)\).
Consequently an original-law event failing with probability \(O_D(N^{-D})\) for every \(D\) retains that property uniformly over central pairs, also after a union over the polynomially many states.
This transfer averages over active locations and inactive words; it does not assert a local law conditional on particular locations.

<a id="negative-sites"></a>
## The active sites still available for flipping

Use \(a=N^{-31/32},\ b=N^{-1/3},\ l=\lceil N^{1/8}\rceil\) and \(D_i=I_m\otimes e_i e_i^*\).
For the original matrix the [stable block local law](../audits/literature/AEKN19/Yin_U001.md#stable-block-law) gives \(\|\big((H_N-E-it)^{-1}\big)_{ii}\|\le C_E\) on all sites at \(b,2a\) and the dyadic scales from \(a\) to at least one, with arbitrary polynomial failure.
In particular \(\mathbf1_{[-t,t]}(H_N-E)\le2t\,\operatorname{Im}(H_N-E-it)^{-1}\) gives counts \(O(Nt)\) and projection diagonal blocks \(O(t)\).
The preceding conditioning transfers these estimates to the central states.

Let \(H_*\) have the same drift and strict upper entries as \(H_N\), with all random diagonal terms removed.
It is independent of the full array of diagonal words and differs from any state by norm at most \(L/\sqrt N\), where \(L=\sum_j\|A_j\|\).
At \(E+ib\), the resolvent identity gives \(\|R_*v\|\le (1-L/(b\sqrt N))^{-1}\|R v\|\) for the original resolvent \(R\).
Since \(\operatorname{Im}R=bR^*R\), the projection \(P=\mathbf1_{[-b,b]}(H_*-E)\) has \(\max_i\|P_{ii}\|\le Cb\) with arbitrary polynomial failure.
On its range the matrices \(D'_i=PD_iP\) sum to the identity and satisfy \(0\le D'_i\le CbI\).

In the original independent array, let \(J\) be the sites carrying the single word \(u^-\).
Except with arbitrary polynomial failure,
\[
 \sum_{i\in J}D'_i\ge 4^{-g} I_{\operatorname{ran}P}. \tag{2}
\]
To see this, reveal successively the \(g\) signs that define \(u^-\).
At each stage let \(S\) be the sites retained by previous tests.
Conditional on \(P,S\), the next retained sum is half the sum on \(S\) plus half a fair-sign sum over \(S\).
The [matrix sign moment estimate](Yin_C_F0356_v1.md#negative-sites) bounds the \(2k\)-th norm moment of the latter sign sum (before halving) by \(mN(C k b)^k\), since \(\|\sum_{i\in S}(D'_i)^2\|\le Cb\).
For \(k=\lceil\log N\rceil\) the norm is at most the fixed \(4^{-g}\) except with arbitrary polynomial failure.
If the sum on \(S\) is at least \(4^{-j}I\) after \(j<g\) tests, the next is at least \((4^{-j}-4^{-g})I/2\ge4^{-(j+1)}I\).
This proves (2), including the conditioning on the guard for \(P\), which sees none of the words.
By the two-count transfer, (2) holds with \(J=J_q\), the still-negative active sites at every central state.

Let \(V_q=\operatorname{ran}\mathbf1_{[-2a,2a]}(H_q-E)\).
For \(v\in V_q\), \(\|(1-P)v\|\le b^{-1}(2a+L/\sqrt N)\|v\|=o(1)\|v\|\).
Thus the guarded states have \(\sum_{i\in J_q}\|v_i\|^2\ge c_g\|v\|^2\) on \(V_q\), dimension \(O(Na)\) and diagonal projection blocks \(O(a)\).
Given the active locations, inactive words, off-diagonals and the first \(q\) positions, the next \(l\) positions form a uniform set \(I_q\) of size \(l\) in \(J_q\) when \(q\le q_+-l\).
The single-state guard just described is measurable before those positions are drawn.
The [weighted sampling and sphere-net argument](Yin_C_F0356_v1.md#negative-sites) therefore gives, with arbitrary polynomial conditional failure on this guard,
\[
 \sum_{i\in I_q}\|v_i\|^2\ge c'_g(l/N)\|v\|^2,\qquad v\in V_q. \tag{3}
\]
Indeed \(|J_q|=r-q\asymp_p N\); the scalar lower-tail exponent \(c l/(Na)\) dominates the net entropy \(CNa\log N\) and the logarithmic cost of conditioning on sample size.
Union over the central positions only after testing the present guard.

<a id="crossings"></a>
## Endpoint crossings and the floor

Conditional on a central \(r\), let \(\lambda_j(q)\) be the ordered eigenvalues of \(H_q-E\).
They are nondecreasing and the change from \(q\) to \(q+l\) is \(2B\otimes\sum_{i\in I_q} e_i e_i^*/\sqrt N\).
For an index in \([-N^{-3},N^{-3}]\), the [min-max splitting at \(\lambda_j(q)+a\)](Yin_C_F0356_v1.md#crossings) applies by (3), giving an increase at least \(c'(l/N)\min(a,N^{-1/2})>2N^{-3}\) for large \(N\).
Consequently each index has at most \(l\) visits in the central interval on the simultaneous guards; indices first entering within the last \(l\) locations obey the same bound.

Write \(K_-=H_{q_-}-E,\ K_+=H_{q_+}-E\) and \(\mathcal D=K_+-K_-\ge0\).
The number of indices that can visit the small interval is bounded by the drop of the strict negative inertia from \(K_-\) to \(K_+\) plus the two endpoint counts in \([-2a,2a]\).
Their expected near counts are \(O(Na)\) by the conditional local law.
On the initial local-law guard move the eigenvalues of \(K_-\) in \([-a,a]\) to \(2a\), obtaining \(K'\) at rank cost \(O(Na)\).
By the [two Schur complements and dyadic count estimate](Yin_C_F0356_v1.md#crossings), the inertia drop is at most \(O(Na)+\operatorname{Tr}(\mathcal D |K'|^{-1})\), and \(\operatorname{Tr}|K'|^{-1}\le CN\log N\).
Given the initial state including the active set and order up to \(q_-\), the sites flipped by \(q_+\) form a uniform set of \(q_+-q_-\) out of \(r-q_-\asymp_p N\).
In particular
\[
 \mathbb E[\mathcal D\mid\text{initial state}]
 \le \frac{2\|B\|(q_+-q_-)}{\sqrt N(r-q_-)}I.
\]
Take this conditional expectation on the initial guard alone; its complement contributes at most \(mN\) times its probability to the eligible index count.
Thus uniformly in central \(r\) the expected number of eligible indices is \(O(Na+(\log N)^{3/2})\).
Multiplying by \(Cl/\sqrt N\), using the maximum atom of \(Q\) given \(r\) and its independence from the path given \(r\), and adding tails and the simultaneous-guard exceptions proves (1).

A scalar evaluation \(x_j=t d_j\) makes \(C-EI+tB\) invertible for large \(t\), so the pencil is full.
The [free power estimate for full pencils](Yin_C_F0352_v1.md#statement) gives \(u_E>-\infty\).
By the [clipped-log assembly](Yin_C_F0186_v40.md#determinant), its normalized logarithm with all singular values clipped from below at \(N^{-3}\) converges almost surely on the full sequence under the original sign law, before any use of translation regularity.
The ordinary logarithm equals this clipped value outside the event in (1), which has vanishing probabilities on the full sequence and summable probabilities along \(N=2^k\).
This proves convergence in probability, dyadic almost-sure convergence and the full-size almost-sure limsup since every ordinary logarithm is bounded above by its clipped value.

<a id="examples"></a>
## Three indefinite coefficients at bulk energies

For \(0<\theta<1\), take \(m=2,C=0\) and
\[
 A_1=\theta I+\sigma_z,\qquad A_2=\theta I-\sigma_z,\qquad A_3=\sigma_x,\qquad
 \sigma_z=\operatorname{diag}(1,-1),\quad \sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Each coefficient is indefinite and invertible, whereas \(A_1+A_2=2\theta I>0\).
Their span is three-dimensional and generates \(M_2(\mathbb C)\).
The variance map is \(\mathcal S(T)=2\theta^2 T+2\sigma_zT\sigma_z+\sigma_xT\sigma_x\).
On \(I,\sigma_x,\sigma_y,\sigma_z\), with \(\sigma_y=i\sigma_x\sigma_z\), its eigenvalues are respectively \(v=3+2\theta^2,\,2\theta^2-1,\,2\theta^2-3,\,2\theta^2+1\).
The last three have modulus strictly below \(v\).
The positive Dyson solution is \(M=m_v I\), where \(-1/m_v=z+v m_v\).
For \(\operatorname{Im}z>0\), taking imaginary parts gives \(|m_v|<v^{-1/2}\), so the three nonscalar stability factors stay uniformly bounded away from zero.
For each \(|E|<2\sqrt v\), the quadratic formula gives a boundary value with positive imaginary part, excluding \(1-vm_v(E+i0)^2=0\).
The scalar factor also cannot vanish at positive height and tends to one at infinity; continuity gives the required uniform bound on the ray.
Thus (1) and the determinant conclusions hold at every such fixed energy for this original three-color law.
The [tridiagonal scalar continuants](Yin_C_F0356_v1.md#examples) remain covered by the single-color case.

## Current assessment
[Selected decision](#decision-sign-chord-reviewed)

## Assessment history

### Decision sign-chord-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:33 |
| status | open |
| reason | Conditioning on the two endpoint counts yields a monotone chain with enough remaining active coordinates; independent proof review of this extension is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Positive sign differences](#statement) | Stable Hermitian pencils at each fixed energy and the stated determinant limits. |
| argument | [Two-count conditioning](#argument) | Exact original sign law, central states and polynomial costs. |
| support | [Remaining negative sites](#negative-sites) | All-diagonal deletion, successive sign restrictions and predictable sampling. |
| support | [Endpoint crossing estimate](#crossings) | Expected eligible index count and ordinary determinant consequences. |
| support | [All-indefinite example](#examples) | Strict interior stability for the irreducible Pauli family. |

### Decision sign-chord-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:38 |
| status | proved |
| reason | A positive difference of two diagonal sign words gives the stable-energy polynomial floor under the original independence law. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original diagonal sign words](#statement) | Exact coefficient, law and parameter hypotheses. |
| argument | [Complete proof](#argument) | A positive difference of two diagonal sign words gives the stable-energy polynomial floor under the original independence law. |
| support | [Available endpoints](#negative-sites) | Correct conditional marginal law and uniform mass for future flips. |
| support | [Crossing estimate](#crossings) | Monotonicity and the dimension-dependent incidence count. |
| support | [Three invertible indefinite directions](#examples) | Explicit positive difference, stability interval and scope of the scalar realization. |
| review | [Independent whole-proof assessment](../audits/reviews/Yin_R_F0364_v2.md#sign-chord-whole-proof) | The fixed statement and proof including its stated limitations. |
