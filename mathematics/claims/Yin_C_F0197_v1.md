---
author: Yin
---

# Divergent residual inverse energy and physical reservoirs for the two-sided product

This Claim narrows the original-law distance problem for \(AB+2BA-zI\) to its high inverse-energy branch and supplies a coordinate reservoir for that branch.
The complete statement is adopted after [independent whole-proof review](../audits/reviews/Yin_R_F0205_v1.md#whole-candidate-finding).
It does not bound the complete Schur determinant or the averaged column-distance probability.

<a id="statement"></a>
## Exact conclusions

Use two independent complex Hermitian Wigner matrices with the fixed centered variance-one off-diagonal laws of [C196](Yin_C_F0196_v1.md#statement), each having a finite fourth absolute moment.
For each input, the real diagonal coordinates are independent copies of a fixed centered law with finite second moment, divided by \(\sqrt N\), as in the original Task model.
All upper off-diagonal coordinates are divided by \(\sqrt N\), with independence of upper pairs, diagonal coordinates and input colors within each size; coupling across sizes is arbitrary.
Put \(P_N=A_NB_N+2B_NA_N\) and \(P=s_1s_2+2s_2s_1\).
Fix an integer \(r\ge0\).
For \(D\subset[N]\), \(|D|\le r\), write \(n=N-|D|\), retain the original \(N^{-1/2}\) normalization in \(A_D,B_D\), and set
\[
 L_D(z)=\begin{pmatrix}-zI_n&A_D&2B_D\\B_D&-I_n&0\\A_D&0&-I_n\end{pmatrix}.
\]
The free counterpart is denoted by \(L(z)\), and its normalized trace by \(\tau_3=\operatorname{tr}_3\otimes\tau\).

There is a deterministic planar set \(Z_0\subset\mathbb C\) of full Lebesgue measure such that for every fixed \(z\in Z_0\), all these finite matrices are invertible almost surely, simultaneously over \(N,D\).
For every \(z\in\mathbb C\), the free affiliated inverse of \(P-z\) exists, and
\[
 P-z\text{ has a bounded inverse}
 \quad\text{or}\quad
 \tau(|P-z|^{-2})=\infty.
 \tag{Free-inverse-dichotomy}
\]
In the second case, for every fixed \(z\in Z_0\cap\sigma(P)\) and every deterministic nonnegative integer sequence \(k_N=o(N)\), write
\(q_{1,D}\ge\cdots\ge q_{3n,D}\) for the singular values of \(L_D(z)^{-1}\).
Then, under every allowed cross-size coupling,
\[
 \min_{|D|\le r}\frac1N\sum_{j>k_N}q_{j,D}^2
 \longrightarrow\infty\quad\text{almost surely}.
 \tag{Residual-energy-divergence}
\]
This gives no rate of divergence.

Here is the finite-matrix reservoir statement, including spectral parameters outside that second case.
Fix \(K\ge1\) and \(Z<\infty\).
There exist \(a,c_*,\delta_*,c,C>0\), independent of \(N\), such that outside an event of probability at most \(Ce^{-cN}\), simultaneously for all \(|D|\le r\) and all \(|z|\le Z\), the following implication holds on \(\|A_D\|,\|B_D\|\le K\).
Let \(V_D\) and \(U_D\) be the right and left singular subspaces of \(L_D(z)\) for singular values at most \(a\).
For every physical set \(S\subset[N]\setminus D\) with \(|S|\le\delta_*N\), let \(P_T\) retain the three auxiliary coordinates over \(T=[N]\setminus(D\cup S)\).
Then
\[
 \|P_Tv\|\ge c_*\|v\|\quad(v\in V_D),
 \qquad \|P_Tu\|\ge c_*\|u\|\quad(u\in U_D).
 \tag{Whole-space-restriction}
\]
Consequently every matrix \(E\) with \(\operatorname{Ran}E\subset V_D\) and \(\operatorname{Ran}E^*\subset U_D\) satisfies
\[
 c_*^2s_j(E)\le s_j(P_TEP_T)\le s_j(E)
 \quad\text{for all }j,
 \qquad \|P_TEP_T\|_{\mathrm{HS}}\ge c_*^2\|E\|_{\mathrm{HS}}.
 \tag{Reservoir-energy}
\]
Zeros are appended to singular-value lists where needed.

For \(E\ne0\) and \(\epsilon>0\), let \(P_i\) be its physical block projections and define
\[
 \ell_i=\|P_iE\|_{\mathrm{HS}}^2+\|EP_i\|_{\mathrm{HS}}^2,
 \qquad S=\{i:\ell_i>\epsilon\|E\|_{\mathrm{HS}}^2\}.
\]
Whenever \(2/\epsilon\le\delta_*N\), this choice has \(|S|\le2/\epsilon\) and, for \(E_T=P_TEP_T\),
\[
 \|E_T\|_{\mathrm{HS}}^2\ge c_*^4\|E\|_{\mathrm{HS}}^2,
 \qquad
 \max_i\frac{\|P_iE_T\|_{\mathrm{HS}}^2+\|E_TP_i\|_{\mathrm{HS}}^2}{\|E_T\|_{\mathrm{HS}}^2}
 \le c_*^{-4}\epsilon.
 \tag{Low-load-reservoir}
\]
In particular \(\epsilon=N^{-1/4}\) is allowed for all sufficiently large \(N\).
When E is chosen measurably from the actual minor, these coordinate selections also use only that minor before its fresh border is sampled; this applies in particular to the inverse spectral remainder below.
The fixed norm guard remains an event restriction; its complement is not claimed summable.

For \(z\in Z_0\cap\sigma(P)\), retain the inverse singular terms numbered \(j>k_N\) whose corresponding singular values of \(L_D(z)\) are at most \(a\), and call their sum \(E_D\).
Then
\[
 \min_{|D|\le r}\|E_D\|_{\mathrm{HS}}^2/N\longrightarrow\infty
 \quad\text{almost surely}.
 \tag{Low-space-energy-divergence}
\]
On the preceding good norm-guarded event, this inverse energy therefore admits the stated reservoir.
This is an inverse-matrix conclusion, not a determinant-coefficient or small-ball conclusion.

## Current assessment
[Selected decision](#decision-reservoir-reviewed)

## Assessment history

### Decision reservoir-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-11T14:23 |
| status | open |
| reason | The complete free-inverse reduction, uniform deletion argument and two-sided physical reservoir are retained for independent checking. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Free inverse dichotomy, almost-everywhere finite invertibility, uniform residual divergence after any sublinear number of modes, and guarded two-sided reservoirs. |
| argument | [Complete proof](#argument) | Exact companion inverse, fixed bounded truncations, interlacing, simultaneous right/left incompressibility and singular-value compression. |
| dependency | [Miy26 spectral interface](../audits/literature/Miy26/Yin_U003.md#miy26-u003) | Corollary 1.2 for nonscalar rational functions of finitely many free semicircular variables, with the skew-field and L2-to-boundedness scopes retained there. |
| dependency | [Finite-variance spectral controls](Yin_C_F0186_v4.md#statement) | Almost-sure weak spectral convergence for the fixed Hermitian matrix-polynomial dilation, under every allowed coupling. |
| dependency | [Two-sided incompressibility](Yin_C_F0196_v1.md#statement) | Uniform bounded-shift compressible-vector exclusion on a fixed norm guard, applied also with A and B interchanged. |

### Decision reservoir-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-11T14:45 |
| status | proved |
| reason | The complete stated free-inverse reduction, uniform residual divergence and two-sided reservoir are supported by the independently checked argument; no determinant or distance floor is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Free inverse dichotomy, almost-everywhere finite invertibility, uniform residual divergence after any sublinear number of modes, and guarded two-sided reservoirs. |
| argument | [Complete proof](#argument) | Exact companion inverse, fixed bounded truncations, interlacing, simultaneous right/left incompressibility and singular-value compression. |
| dependency | [Miy26 spectral interface](../audits/literature/Miy26/Yin_U003.md#miy26-u003) | Corollary 1.2 for nonscalar rational functions of finitely many free semicircular variables, with the skew-field and L2-to-boundedness scopes retained there. |
| dependency | [Finite-variance spectral controls](Yin_C_F0186_v4.md#statement) | Almost-sure weak spectral convergence for the fixed Hermitian matrix-polynomial dilation, under every allowed coupling. |
| dependency | [Two-sided incompressibility](Yin_C_F0196_v1.md#statement) | Uniform bounded-shift compressible-vector exclusion on a fixed norm guard, applied also with A and B interchanged. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0205_v1.md#whole-candidate-finding) | Complete statement, argument and consumed dependency interfaces, with the finding's exact inspection and consequence limits. |

<a id="argument"></a>
## Free inverse and finite-dimensional rank branches

The [accepted Miy26 interface](../audits/literature/Miy26/Yin_U003.md#miy26-u003) gives \(D(s)\cap L^2\subset M\) and the skew-field inverse statement used in Corollary 1.2.
The exact source is Miyagawa, [arXiv:2603.19528v2](https://arxiv.org/pdf/2603.19528v2), Theorem 1.1 and Corollary 1.2, PDF pp. 1--2.
Those source statements and the corollary proof were checked for this use; the retained U002/U004 accounts preserve the full boundedness proof and the precise external free-field acceptance limits.
The nonzero quadratic polynomial \(s_1s_2+2s_2s_1\) is nonscalar by algebraic freeness of the semicircular tuple.
Thus \(P-z\) is nonzero in \(D(s)\) for every \(z\), has an affiliated inverse there, and a finite inverse \(L^2\) norm would make that inverse bounded.
This proves (Free-inverse-dichotomy).

The exact bounded-coefficient companion identity is
\[
 L(z)^{-1}=
 \begin{pmatrix}1\\s_2\\s_1\end{pmatrix}
 (P-z)^{-1}
 \begin{pmatrix}1&s_1&2s_2\end{pmatrix}
 +\operatorname{diag}(0,-1,-1),
 \tag{Free-companion-inverse}
\]
interpreted in the affiliated matrix algebra.
Direct multiplication verifies both inverse identities on that algebra.
The top-left corner is \((P-z)^{-1}\), so \(\tau(|P-z|^{-2})=\infty\) implies \(\tau_3(|L(z)|^{-2})=\infty\).
No bounded inverse or finite logarithmic expectation for the finite matrices is inferred.

For each realized finite pair and each deletion, \(\det(P_D-zI)\) is a monic polynomial up to the harmless sign of its leading coefficient, with finitely many zeros.
Tonelli's theorem on each compact planar disk gives \(\mathbb P\{\det(P_D-zI)=0\}=0\) for almost every fixed \(z\).
A countable intersection over dimensions, finite deletion sets and disks supplies the deterministic full-area set \(Z_0\).
The exact finite companion identity makes the same assertion true for \(L_D(z)\).
For fixed \(z\in Z_0\), a countable union of null events then supplies simultaneous invertibility under any prescribed cross-size coupling.
This is the direct principal-minor specialization of the almost-everywhere observation in [C186v4](Yin_C_F0186_v4.md#remaining-defect).
It supplies no polynomial quantitative separation from singularity.

## Residual energy from fixed bounded truncations

Hermitize the full companion as \(H_N=\left(\begin{smallmatrix}0&L_N\\L_N^*&0\end{smallmatrix}\right)\).
The accepted C186v4 weak theorem applies to this fixed selfadjoint matrix pencil.
For each fixed \(R>0\), the even function
\[
 f_R(t)=\min\{|t|^{-2},R\},\qquad f_R(0)=R,
\]
is bounded and continuous, with total variation \(2R\).
Consequently, on one probability-one event for positive integer \(R\),
\[
 \frac1{2N}\operatorname{Tr}f_R(H_N)
 \longrightarrow3\tau_3(f_R(|L(z)|)).
\]
Deleting \(|D|\le r\) physical coordinates removes \(6|D|\) scalar rows and columns from this Hermitian dilation.
Hermitian interlacing bounds the difference of their unnormalized counting functions by \(6r\).
Integration against a bounded-variation test vanishing at infinity therefore bounds the difference of the displayed normalized traces by \(6rR/N\), uniformly in \(D\).
The precise constant is immaterial; the common bound tends to zero for fixed \(R\).

The inverse singular values satisfy, simultaneously for every deletion,
\[
 \frac1N\sum_{j>k_N}q_{j,D}^2
 \ge \frac1N\sum_{j=1}^{3n}\min(q_{j,D}^2,R)-\frac{k_NR}{N}
 =\frac1{2N}\operatorname{Tr}f_R(H_D)-\frac{k_NR}{N}.
\]
Taking the minimum over \(D\), then the almost-sure lower limit, gives a lower bound of \(3\tau_3(f_R(|L(z)|))\).
For \(z\in\sigma(P)\), this quantity increases to infinity as \(R\to\infty\) by (Free-companion-inverse) and monotone convergence.
This proves (Residual-energy-divergence) without a rate, independence across sizes, or a union bound over minor events.

## Both low-singular spaces survive physical coordinate deletion

For each fixed physical minor, rescale its inputs by \(\sqrt{N/n}\) to apply C196 at dimension \(n\).
The resulting off-diagonal laws are the same fixed raw laws, while \(P_D\) is \(n/N\) times the rescaled polynomial.
Eventually \(n/N\ge1/2\), the rescaled norm guard is bounded by \(2K\), and the rescaled shifts lie in \(|z'|\le2Z\).
C196's simultaneous bounded-shift event therefore supplies common positive compressibility constants and a uniform positive lower residual threshold for the original minors.
Apply it also with \(A_D,B_D\) interchanged.
A union over at most \((r+1)N^r\) deletions keeps the combined exception exponentially small.
The norm guards are used only as intersections throughout this application.

Let \(w=(u,v,t)\) be a unit vector with \(\|L_D(z)w\|\le\varepsilon\).
Its residual equations give
\[
 v=B_Du-r_1,\quad t=A_Du-r_2,\qquad
 (P_D-zI)u=r_0+A_Dr_1+2B_Dr_2.
\]
For \(\varepsilon\le1/4\), it follows that
\[
 \|u\|\ge[2(1+2K)]^{-1},\qquad
 \|(P_D-zI)u\|\le(1+3K)\varepsilon.
\]
Choose \(a>0\) sufficiently small that the normalized root \(u/\|u\|\) must be outside the C196 compressible set whenever \(\varepsilon\le a\).
For a unit vector \(v_0\) and coordinate set \(S\), normalized truncation gives
\[
 \left\|v_0-\frac{(v_0)_S}{\|(v_0)_S\|}\right\|^2
 =2(1-\|(v_0)_S\|)\le2\|(v_0)_{S^c}\|^2
\]
when the head is nonzero; if it is zero, the tail already has norm one.
Incompressibility thus forces a fixed positive root mass outside every permitted sparse support.
After reducing \(\delta_*\) to account for \(n/N\), the full companion vector retains a fixed norm outside every \(|S|\le\delta_*N\).
Every unit vector in \(V_D\) has residual at most \(a\), so this argument is simultaneous over that entire subspace.

For a unit left-space vector \((\alpha,\beta,\gamma)\), the equations of \(L_D(z)^*\) instead give
\[
 \beta=A_D\alpha-r_1,\quad\gamma=2B_D\alpha-r_2,
\]
\[
 (B_DA_D+2A_DB_D-\overline zI)\alpha
 =r_0+B_Dr_1+A_Dr_2.
\]
The root norm is at least \([2(1+3K)]^{-1}\), and its polynomial residual is at most \((1+2K)\varepsilon\).
The swapped C196 event applies and proves the second restriction inequality after decreasing \(a,c_*\) if necessary.
This proves (Whole-space-restriction), also for zero singular values.

## Compression, coordinate loads and divergent retained energy

Choose orthonormal column matrices \(X,Y\) spanning \(V_D,U_D\).
Then \(E=XFY^*\) for a matrix \(F\), and (Whole-space-restriction) says that \(P_TX\) and \(P_TY\) have all singular values in \([c_*,1]\).
Their polar decompositions reduce the nonzero singular values of \(P_TEP_T\) to those of \(G_X^{1/2}FG_Y^{1/2}\), where \(c_*^2I\preceq G_X,G_Y\preceq I\).
The singular-value product inequalities in both directions give (Reservoir-energy).
They also cover unequal subspace dimensions and appended zero singular values.

The load identity \(\sum_i\ell_i=2\|E\|_{\mathrm{HS}}^2\) implies \(|S|\le2/\epsilon\).
For each retained coordinate, compression can only decrease both loads, whereas its total squared energy remains at least \(c_*^4\|E\|_{\mathrm{HS}}^2\).
This proves (Low-load-reservoir), uniformly for every admitted \(E\).

Finally the inverse piece supported on singular values greater than \(a\) has squared Hilbert--Schmidt norm at most \(3N/a^2\).
Discarding any additional selected inverse modes cannot increase that bound.
Thus (Residual-energy-divergence) forces the complementary low-space remainder \(E_D\) to satisfy (Low-space-energy-divergence), uniformly over the stated deletions.
All selections may be made from the actual minor by spectral projections and a measurable choice within tied singular spaces; the conclusions hold for any such choice.

## Boundary of the deduction

The theorem removes bounded residual inverse energy after any sublinear number of modes from the spectral case and retains diffuse inverse-matrix energy on a lawful fresh-row reservoir.
It does not prove a lower bound for the complete multilinear coefficient tensor after that restriction.
The unequal left and right graph maps, possible cancellation between inverse modes and the same-row normalization remain in the required distance small-ball estimate.
Consequently the averaged original-law probability floor and the Brown conclusion remain open at this point.
