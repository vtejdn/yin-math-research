---
author: Yin
---

# Physical spread of the actual two-sided inverse through Hermitian dilation

This candidate strengthens the [v1 physical reservoir](../claims/Yin_C_F0197_v1.md#statement) to spread of the actual inverse and adapts the original-row imaginary-resolvent argument of [C187v26](../claims/Yin_C_F0187_v26.md#full-imaginary-covariance) to the actual companion of \(AB+2BA-zI\).
The positive coefficient-frame hypothesis is replaced by the adopted [C187v29 joint gap](../claims/Yin_C_F0187_v29.md#statement) on approximate low-singular companion graphs.
The Hermitian dilation has a block-diagonal positive resolvent weight, which prevents cancellation between its left and right singular contributions.
The argument works for the full complex Hermitian input laws, including real laws and laws with dependent real and imaginary parts.
It proves geometric spread of the original inverse, without cropping that inverse or altering its exact algebraic identities.
It does not prove a determinant small-ball bound or an unconditional least-singular-value floor.
The complete theorem is adopted after [independent whole-proof review](../audits/reviews/Yin_R_F0205_v2.md#hermitized-spread-whole-proof); v1 remains fixed at its adopted scope.

<a id="inputs"></a>
## Inputs and source scope

The input model, free inverse dichotomy, almost-everywhere finite invertibility and almost-sure residual inverse-energy divergence are those of [C197v1](../claims/Yin_C_F0197_v1.md#statement), with its [complete proof](../claims/Yin_C_F0197_v1.md#argument).
The fixed laws have finite fourth absolute off-diagonal moments and fixed centered finite-second-moment real diagonal laws.
All original normalizations are retained under physical deletions.
The adopted [C186v4 weak theorem](../claims/Yin_C_F0186_v4.md#statement) applies to the fixed Hermitian dilation below.
The adopted [C187v29 erased joint gap](../claims/Yin_C_F0187_v29.md#statement) is used only with no extra erased coordinates, uniformly over the fixed physical deletions.
No compressible-vector exclusion is needed in the fresh-row covariance argument: the auxiliary identity blocks already bound the root mass of a low singular vector.

The only external concentration input is inequality (9) in [C187v2](../claims/Yin_C_F0187_v2.md#argument), for independent bounded Euclidean coordinate blocks and convex Lipschitz functions.
Its exact accepted source scope is Theorem 3.7 and Corollary 3.8 on PDF p. 30 of Götze--Naumov--Tikhomirov, arXiv:1404.7013, retained there; the source proof is not newly audited here.
In particular, one complex entry is one real two-dimensional coordinate block, and its two real components need not be independent.
The weighted fixed cutoff, polynomial auxiliary net and imaginary-Schur mechanism follow [C187v26](../claims/Yin_C_F0187_v26.md#full-imaginary-covariance), but all covariance and matrix interfaces for this companion are proved below.
The separate row and physical-diagonal splittings follow the elementary mechanism in [C187v26](../claims/Yin_C_F0187_v26.md#residual-spread), adapted explicitly to singular rather than eigenmode expansions.
No positive-frame theorem, Gaussian invariance, pseudo-variance assumption or local law is invoked.

<a id="statement"></a>
## Exact conclusions

Let \(A_N,B_N\) be independent complex Hermitian Wigner matrices.
Their strict upper entries are independent copies of fixed centered complex laws \(\xi_A/\sqrt N,\xi_B/\sqrt N\), respectively, with unit second absolute moments and finite fourth absolute moments.
The real diagonal entries have fixed centered finite-second-moment laws divided by \(\sqrt N\); all upper pairs, diagonals and input colors are independent within each size, and coupling across sizes is arbitrary.
No independence of the real and imaginary parts of an off-diagonal entry is assumed.
Put \(P=s_1s_2+2s_2s_1\), and fix \(z\in\sigma(P)\).
Fix \(K\ge1\) and an integer \(r\ge0\).
For \(|D|\le r+1\), write \(n=N-|D|\), retain the original normalization in \(A_D,B_D\), and set
\[
 Q_D=\begin{pmatrix}-zI&A_D&2B_D\\B_D&-I&0\\A_D&0&-I\end{pmatrix},
 \qquad H_D=\begin{pmatrix}0&Q_D\\Q_D^*&0\end{pmatrix}.
\]
Let \(\Pi_i\) retain the six coordinates above a physical position in the Hermitian dilation, and let \(P_i\) retain its three companion coordinates.
The norm guard of a minor means \(\max(\|A_D\|,\|B_D\|)\le K\).
Let \(Q(z)\) be the free companion, put \(\tau_3=\operatorname{tr}_3\otimes\tau\), and define
\[
 J(h)=\tau_3\bigl((Q(z)^*Q(z)+h^2I)^{-1}\bigr),
 \qquad q(h)=h^2J(h),\qquad h>0.
 \tag{Hermitized-energy}
\]
The free inverse result in C197v1 implies \(J(h)\to\infty\) as \(h\downarrow0\), and \(0<q(h)\le1\).
There are constants \(c>0\) and \(h_0>0\), depending only on the fixed data, such that for every fixed \(0<h\le h_0\), almost surely eventually, simultaneously for all \(|D|\le r\) on their own norm guards,
\[
 \max_{i\notin D}\|\Pi_i(H_D-ihI)^{-1}\Pi_i\|
 \le \frac1{h(1+cJ(h))},
\]
\[
 \max_{i\notin D}\|\Pi_i\mathbf1_{[-h,h]}(H_D)\Pi_i\|
 \le \rho(h):=\frac2{1+cJ(h)}.
 \tag{Hermitized-physical-projectors}
\]
A single probability-one event works for any prescribed countable set of such fixed \(h\)'s.
The thresholds in \(N\) may depend on \(h\); no estimate at a size-dependent spectral scale is asserted.
The norm-guard complement is not claimed summable.
All almost-sure guarded assertions mean that on one probability-one event, every sufficiently large minor satisfying its displayed norm guard obeys the conclusion; they do not assert that the guards themselves occur eventually.

In particular, let \(z\) also belong to the deterministic full-area set \(Z_0\) of C197v1, so every finite companion under consideration is almost surely invertible.
Put \(Z_D=Q_D^{-1}\) and \(F_D=\|Z_D\|_{\mathrm{HS}}\).
Uniformly over the guarded minors, almost surely,
\[
 \frac{F_D^2}{N}\longrightarrow\infty,
\qquad
 \frac{\max_i\{\|P_iZ_D\|_{\mathrm{HS}}^2+\|Z_DP_i\|_{\mathrm{HS}}^2\}}{F_D^2}
 \longrightarrow0,
\]
\[
 \frac{\sum_i\|P_iZ_DP_i\|_{\mathrm{HS}}^2}{F_D^2}\longrightarrow0.
 \tag{Actual-companion-spread}
\]
The same conclusions hold at each residual's own Hilbert--Schmidt scale after removal of any at most \(k_N=o(N)\) singular terms of \(Z_D\), uniformly over these removals and choices within tied singular spaces.
This residual assertion uses complete singular terms, not an arbitrary matrix perturbation.

For the actual root inverse
\[
 G_D=(A_DB_D+2B_DA_D-zI)^{-1},\qquad F_{G,D}=\|G_D\|_{\mathrm{HS}},
\]
one has \(F_{G,D}^2/N\to\infty\) uniformly along the same guarded minors.
For each member \(T_D\) of
\[
 \{G_D,\ B_DG_D,\ G_DB_D,\ B_DG_DB_D\},
\]
and also for its transpose or adjoint,
\[
 \max_i\bigl(\|e_i^*T_D\|^2+\|T_De_i\|^2\bigr)=o(F_{G,D}^2),
 \qquad \sum_i |(T_D)_{ii}|^2=o(F_{G,D}^2),
 \tag{Actual-root-block-spread}
\]
uniformly in the permitted guarded minors, almost surely.
The denominator is the complete root inverse energy \(F_{G,D}^2\), not the energy of an individual block.
These are statements about the actual matrices and preserve all identities involving their commutators.

The same root-block conclusions hold after removing any at most \(k_N=o(N)\) complete singular terms from \(G_D\), at that root residual's own Hilbert--Schmidt scale.
More precisely, for every such residual \(E_D\), uniformly over all permitted removals and guarded minors,
\[
 \|E_D\|_{\mathrm{HS}}^2/N\longrightarrow\infty,
\]
\[
 \max_i\bigl(\|e_i^*T_D\|^2+\|T_De_i\|^2\bigr)
       =o(\|E_D\|_{\mathrm{HS}}^2),
 \qquad \sum_i |(T_D)_{ii}|^2=o(\|E_D\|_{\mathrm{HS}}^2),
 \tag{Root-residual-block-spread}
\]
for \(T_D\in\{E_D,B_DE_D,E_DB_D,B_DE_DB_D\}\), its transpose, or its adjoint.
For every fixed number of largest singular terms \(q_ju_jv_j^*\) of \(G_D\), all six vectors
\[
 u_j,\ A_Du_j,\ B_Du_j,\ v_j,\ A_Dv_j,\ B_Dv_j
 \tag{Root-head-graph-vectors}
\]
have maximal absolute coordinate tending to zero, uniformly in the guarded minors and orthonormal choices within ties.
Their coordinatewise conjugates have the same conclusion.
For real inputs this includes \(\overline v_j,A_D\overline v_j,B_D\overline v_j\); for complex inputs it asserts \(\overline{A_Dv_j},\overline{B_Dv_j}\), without replacing those by multiplication of \(\overline v_j\) by the original complex matrices.

## Current assessment
[Selected decision](#decision-hermitized-physical-spread-reviewed)

## Assessment history

### Decision hermitized-physical-spread-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-11T15:07 |
| status | open |
| reason | Complete Hermitian-dilation covariance, original complex-row concentration, guarded projector bounds and actual inverse spread are fixed for independent review, without a determinant, distance or least-value conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conclusions](#statement) | Fixed-h physical projectors on the free spectrum; guarded complete and sublinear-mode-residual companion and root inverse spread; root graph-head delocalization and actual block transfer. |
| argument | [Complete proof](#argument) | Approximate singular graphs, separated left/right positive covariance, weighted original-law cutoff, complex auxiliary nets, imaginary Schur, separate singular splits, root-residual two-sided operator control and exact root blocks. |
| dependency | [Preceding inverse-energy theorem](../claims/Yin_C_F0197_v1.md#statement) | Free inverse-square divergence, full-area finite invertibility and residual divergence after sublinear mode removal, with all original laws and bounded deletions. |
| dependency | [Preceding theorem proof](../claims/Yin_C_F0197_v1.md#argument) | Exact companion inverse, free-to-companion energy implication and interlacing normalization; no coefficient or small-ball conclusion. |
| dependency | [Uniform joint gap](../claims/Yin_C_F0187_v29.md#statement) | Empty extra erasure, all complex centers and fixed physical deletions on the local norm guard. |
| dependency | [Joint-gap argument](../claims/Yin_C_F0187_v29.md#argument) | Summable guarded failure and actual Hermitian Wigner law scope. |
| dependency | [Weak matrix spectral limit](../claims/Yin_C_F0186_v4.md#statement) | Almost-sure weak limit of the fixed Hermitian dilation, under arbitrary cross-size coupling. |
| dependency | [Bounded complex-block convex concentration](../claims/Yin_C_F0187_v2.md#argument) | Exact inequality (9) only, after independent truncated complex coordinates remain; its GNT14 statement and unaudited source-proof boundary are retained in Inputs. |
| dependency | [Weighted original-row concentration mechanism](../claims/Yin_C_F0187_v26.md#full-imaginary-covariance) | Fixed cutoff, weighted survival and median mechanism only, with the new covariance proved here instead of a positive coefficient frame. |
| dependency | [Separate inverse split mechanism](../claims/Yin_C_F0187_v26.md#residual-spread) | Row and diagonal estimates are adapted explicitly to the two singular projectors; no positive-frame conclusion is imported. |

### Decision hermitized-physical-spread-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-11T15:29 |
| status | proved |
| reason | Independent whole-proof review supports the guarded Hermitized projector estimates, complete companion and root residual spread, and fixed-head graph delocalization, with the precise spectral and source limits retained. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conclusions](#statement) | Fixed-h physical projectors on the free spectrum; guarded complete and sublinear-mode-residual companion and root inverse spread; root graph-head delocalization and actual block transfer. |
| argument | [Complete proof](#argument) | Approximate singular graphs, separated left/right positive covariance, weighted original-law cutoff, complex auxiliary nets, imaginary Schur, separate singular splits, root-residual two-sided operator control and exact root blocks. |
| dependency | [Preceding inverse-energy theorem](../claims/Yin_C_F0197_v1.md#statement) | Free inverse-square divergence, full-area finite invertibility and residual divergence after sublinear mode removal, with all original laws and bounded deletions. |
| dependency | [Preceding theorem proof](../claims/Yin_C_F0197_v1.md#argument) | Exact companion inverse, free-to-companion energy implication and interlacing normalization; no coefficient or small-ball conclusion. |
| dependency | [Uniform joint gap](../claims/Yin_C_F0187_v29.md#statement) | Empty extra erasure, all complex centers and fixed physical deletions on the local norm guard. |
| dependency | [Joint-gap argument](../claims/Yin_C_F0187_v29.md#argument) | Summable guarded failure and actual Hermitian Wigner law scope. |
| dependency | [Weak matrix spectral limit](../claims/Yin_C_F0186_v4.md#statement) | Almost-sure weak limit of the fixed Hermitian dilation, under arbitrary cross-size coupling. |
| dependency | [Bounded complex-block convex concentration](../claims/Yin_C_F0187_v2.md#argument) | Exact inequality (9) only, after independent truncated complex coordinates remain; its GNT14 statement and unaudited source-proof boundary are retained in Inputs. |
| dependency | [Weighted original-row concentration mechanism](../claims/Yin_C_F0187_v26.md#full-imaginary-covariance) | Fixed cutoff, weighted survival and median mechanism only, with the new covariance proved here instead of a positive coefficient frame. |
| dependency | [Separate inverse split mechanism](../claims/Yin_C_F0187_v26.md#residual-spread) | Row and diagonal estimates are adapted explicitly to the two singular projectors; no positive-frame conclusion is imported. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0205_v2.md#hermitized-spread-whole-proof) | Complete statement, argument and exact consumed dependency interfaces, with the finding's scope and source limitations. |

<a id="argument"></a>
## Complete proof

<a id="graphs"></a>
## Uniform covariance of low-singular companion graphs

First fix deterministic Hermitian \(A,B\) with norms at most \(K\) satisfying the full-coordinate joint gap
\[
 \|(A-aI)u\|^2+\|(B-bI)u\|^2\ge\gamma^2\|u\|^2
 \quad(u\in\mathbb C^n,\ a,b\in\mathbb C).
 \tag{Full-joint-gap}
\]
The constants below depend only on \(K,\gamma\).
Write \(Q\) for their companion at \(z\).
A unit right singular vector \(v=(u,v_1,v_2)\) of singular value at most \(a_*\) satisfies
\[
 v=(u,Bu,Au)+e_R,\qquad \|e_R\|\le a_*.
\]
A unit left singular vector \(w=(t,w_1,w_2)\) satisfies
\[
 w=(t,At,2Bt)+e_L,\qquad \|e_L\|\le a_*.
\]
These identities follow from the lower two equations of \(Qv\) and \(Q^*w\), respectively.
If \(a_*\le1/2\), the bounded graph norms give
\[
 \|u\|\ge\frac1{2\sqrt{1+2K^2}},\qquad
 \|t\|\ge\frac1{2\sqrt{1+5K^2}}.
 \tag{Low-graph-root-mass}
\]
This is deterministic and requires no independence or distributional hypothesis.

At an exposed physical position, write the parent input blocks as
\[
 A_{\rm par}=\begin{pmatrix}a&x^*\\x&A\end{pmatrix},\qquad
 B_{\rm par}=\begin{pmatrix}b&y^*\\y&B\end{pmatrix}.
\]
The original companion border matrices are
\[
 R=\begin{pmatrix}0&x^*&2y^*\\y^*&0&0\\x^*&0&0\end{pmatrix},\qquad
 C=\begin{pmatrix}0&x&2y\\y&0&0\\x&0&0\end{pmatrix}.
 \tag{Complex-original-borders}
\]
After multiplying these matrices by \(\sqrt N\), let the coordinates of \(x,y\) be the original raw independent centered complex variables, each of second absolute moment one.
Each coordinate may have the fixed upper law or its conjugate, according to its position.
For \(\alpha\in\mathbb C^3\), the right exact graph gives the coefficient vectors of the scalar \((u,Bu,Au)^*\widehat R^*\alpha\) as
\[
 \alpha_1\overline{Bu}+\alpha_3\overline u,
 \qquad 2\alpha_1\overline{Au}+\alpha_2\overline u.
 \tag{Right-fresh-coefficients}
\]
The left exact graph gives the coefficient vectors of \((t,At,2Bt)^*\widehat C\alpha\) as
\[
 2\alpha_1\overline{Bt}+\alpha_2\overline t,
 \qquad \alpha_1\overline{At}+2\alpha_3\overline t.
 \tag{Left-fresh-coefficients}
\]
For each pair, its sum of squared coefficient norms is at least \(c\|\alpha\|^2\) whenever its graph root satisfies (Low-graph-root-mass).
Here is a direct quantitative verification.
For a normalized root, if \(|\alpha_1|\) is at least a sufficiently small fixed multiple of \(\|\alpha\|\), conjugating the two vectors and dividing by their nonzero fixed weights reduces the lower bound to (Full-joint-gap), with arbitrary complex centers.
If \(|\alpha_1|\) is smaller, the terms containing \(A,B\) have norm at most \(C_K|\alpha_1|\), while the two root terms have combined norm at least a fixed multiple of \((|\alpha_2|^2+|\alpha_3|^2)^{1/2}\).
The triangle inequality gives the same positive lower bound after reducing that fixed multiple.
Rescaling the root proves the assertion using its fixed positive lower mass.

Replacing either exact graph by the corresponding actual singular vector changes the combined coefficient norm by at most \(C a_*\|\alpha\|\).
This follows directly from (Complex-original-borders), whose fixed two coordinate matrices have bounded norms.
Choose \(a_*>0\) sufficiently small, once and for all, to absorb this error into half the exact graph lower bound.
Independence, centering and unit second absolute moments then give, for every normalized left or right singular vector of singular value at most \(a_*\),
\[
 \mathbb E|v^*\widehat R^*\alpha|^2\ge c_1\|\alpha\|^2,
 \qquad \mathbb E|w^*\widehat C\alpha|^2\ge c_1\|\alpha\|^2.
 \tag{Low-singular-row-covariance}
\]
The two expectations are separate assertions for the right and left vectors.
They use only covariance \(\mathbb E\eta_j\overline\eta_k=\delta_{jk}\); no restriction on \(\mathbb E\eta_j^2\) is imposed.
All constants are uniform over the actual singular vectors and their singular values in this interval.

<a id="hermitized-covariance"></a>
## The positive resolvent weight separates the left and right channels

Condition on a retained original local minor obtained by deleting one further physical position from a permitted parent.
The fresh lower border of its Hermitian dilation, in left/right ordering, is
\[
 \mathcal B=\begin{pmatrix}0&C\\R^*&0\end{pmatrix},\qquad
 \widehat{\mathcal B}=\sqrt N\mathcal B.
\]
For \(a=(a_L,a_R)\in\mathbb C^6\),
\[
 \widehat{\mathcal B}a=(\widehat C a_R,\widehat R^*a_L).
 \tag{Hermitian-fresh-border}
\]
Both components are complex-linear in the same original raw \(x,y\) coordinates.
They are not declared independent.
For the local Hermitian dilation \(\widetilde H\), put
\[
 W_h=h\operatorname{Im}(\widetilde H-ihI)^{-1}
     =h^2(\widetilde H^2+h^2I)^{-1}
 =\begin{pmatrix}
 h^2(QQ^*+h^2I)^{-1}&0\\
 0&h^2(Q^*Q+h^2I)^{-1}
 \end{pmatrix}.
 \tag{Block-diagonal-positive-weight}
\]
This is a minor-measurable positive contraction.
Let \(s_j\) be the singular values of \(Q\), with left and right orthonormal singular vectors \(w_j,v_j\), including any zero singular subspaces with arbitrary orthonormal pairing.
For a unit \(a\), exact spectral expansion gives
\[
 \begin{aligned}
 H_a&:=\mathbb E\|W_h^{1/2}\widehat{\mathcal B}a\|^2\\
 &=\sum_j\frac{h^2}{s_j^2+h^2}
 \left(\mathbb E|w_j^*\widehat C a_R|^2
       +\mathbb E|v_j^*\widehat R^* a_L|^2\right).
 \end{aligned}
\]
There are no cross terms between the two halves because \(W_h\) is block diagonal.
On the local norm guard and joint-gap event, (Low-singular-row-covariance) therefore implies
\[
 H_a\ge c_1\sum_{s_j\le a_*}\frac{h^2}{s_j^2+h^2}.
 \tag{Low-weight-covariance}
\]
No scalar coefficient frame on the full six-dimensional auxiliary space is assumed.

The full parent Hermitian dilation has the almost-sure weak limit supplied by C186v4.
Its scalar law is the symmetrized singular-value law of the free companion.
Deleting a bounded number of physical positions removes a bounded number of its scalar rows and columns.
The Hermitian interlacing bound, applied to the bounded continuous function \(h^2/(t^2+h^2)\), gives, simultaneously for all local minors at each fixed \(h>0\), almost surely,
\[
 \frac1N\sum_j\frac{h^2}{s_j^2+h^2}\longrightarrow 3q(h).
 \tag{Hermitian-local-trace}
\]
This retains the original \(N\) normalization and holds without conditioning on the norm guard.
The sum over \(s_j>a_*\) is at most \(3Nh^2/a_*^2\).
Choose \(h_0>0\) such that \(J(h)\ge4/a_*^2\) for \(h\le h_0\).
For each such fixed \(h\), (Hermitian-local-trace) implies eventually
\[
 \sum_{s_j\le a_*}\frac{h^2}{s_j^2+h^2}
 \ge \frac32Nq(h)-\frac{3Nh^2}{a_*^2}
 \ge\frac34Nq(h).
\]
Hence, uniformly in unit \(a\),
\[
 H_a\ge c_2 Nq(h)
 \tag{Full-complex-Hermitian-covariance}
\]
on the local trace condition, local norm guard and local joint gap.
The constants are independent of the fixed \(h\le h_0\).
Free inverse-square divergence is used precisely to dominate the high singular-mode loss; no lower bound of order \(hN\) for a spectral count is needed.

<a id="cutoff-concentration"></a>
## Original complex coordinates, fixed cutoff and convex concentration

For a fixed unit \(a\), express
\[
 \widehat{\mathcal B}a=\sum_{j=1}^2\sum_k g_{j,k}(a)\eta_{j,k},\qquad
 w_{j,k}=\|W_h^{1/2}g_{j,k}(a)\|^2.
\]
The two matrices defining each raw coordinate have fixed bounded coefficients, so
\[
 0\le w_{j,k}\le W_0,\qquad
 \sum_{j,k}w_{j,k}=H_a,
\]
where \(W_0\) is a universal fixed constant.
The raw map from all coordinate blocks to \(\widehat{\mathcal B}a\) has operator norm at most a fixed constant \(L_0'\), uniformly over \(N,a\).
Indeed it acts separately at each physical position before the contractive weight is applied, with the same fixed two coordinate coefficient matrices.
The same assertion holds with complex coordinate blocks viewed as real Euclidean blocks.

Choose a fixed raw cutoff \(M_0\), independent of \(h,N,a\), such that each input law and its conjugate obey
\[
 \mathbb P\{|\eta|\le M_0\}\ge\frac12,
 \qquad
 \mathbb E\bigl(|\eta-\mathbb E(\eta\mid |\eta|\le M_0)|^2
                    \mid |\eta|\le M_0\bigr)\ge\frac12.
\]
Fixed finite second moments imply that such \(M_0\) exists.
For the independent cutoff indicators \(I_{j,k}\),
\[
 \mathbb E\exp\left[-W_0^{-1}\sum I_{j,k}w_{j,k}\right]
 \le\exp[-(1-e^{-1})H_a/(2W_0)].
\]
This follows from \(1-e^{-w/W_0}\ge(1-e^{-1})w/W_0\) for \(0\le w\le W_0\), and each retention probability is at least one half.
Exponential Markov therefore bounds the probability of retained weight below \(H_a/4\) by \(e^{-cH_a}\).

Reveal the indicators and all discarded coordinate values.
The retained complex coordinates remain independent conditional truncated laws, each having support diameter at most \(2M_0\) and centered second absolute moment at least one half.
The discarded values and conditional means produce an arbitrary fixed offset.
The function
\[
 f_a=\|W_h^{1/2}\widehat{\mathcal B}a\|
\]
is convex and \(L_0'\)-Lipschitz on the product of retained real two-dimensional coordinate blocks.
On weighted survival, independence and centering give \(\mathbb E f_a^2\ge H_a/8\).
The bounded-product convex inequality (9) of C187v2 and integration give
\(\mathbb E|f_a-\operatorname{med}f_a|^2\le C\), uniformly in the revealed offset.
The \(L^2\) triangle inequality yields
\[
 \operatorname{med}f_a\ge(\mathbb E f_a^2)^{1/2}-\sqrt C
                         \ge c\sqrt{H_a}
\]
once \(H_a\) is sufficiently large.
A second application of the lower tail, followed by integration over the revealed data, proves
\[
 \mathbb P\{\|W_h^{1/2}\widehat{\mathcal B}a\|<c_3\sqrt{Nq(h)}
                   \mid\text{original local minor}\}
 \le Ce^{-cNq(h)}.
 \tag{Complex-fixed-direction-small-norm}
\]
It holds whenever the conditioned minor obeys its stated trace, norm and joint-gap conditions.
Neither a parent norm event nor a fresh row-norm event is conditioned into this law.

<a id="projector-proof"></a>
## Simultaneous auxiliary directions and imaginary Schur blocks

Use the single full-array guard
\[
 \mathcal W_N=\left\{\sum_{j=1}^2\sum_{u<v}|\xi_{j,uv}|^2\le N^4\right\}.
\]
Its complement has probability at most \(CN^{-2}\) by the fixed second moments, hence is summable.
On this event every raw Hermitian border, for every permitted physical deletion, has operator norm at most \(C N^2\).
A complex-unit-sphere net in \(\mathbb C^6\) of mesh
\(c_3\sqrt{Nq(h)}/(2CN^2)\) has at most \(Cq(h)^{-6}N^{18}\) points.
A lower bound \(c_3\sqrt{Nq(h)}\) at all its points implies half that bound for all unit directions, by the contractivity of \(W_h^{1/2}\).
The net is deterministic for fixed \(h,N\).

Integrate (Complex-fixed-direction-small-norm) over only the good local-minor conditions, then union over the net and the \(O_r(N^{r+1})\) parent/position pairs.
The probability that one of these good local minors has a direction violating
\[
 \mathcal B^*W_h\mathcal B\succeq c_4 q(h)I_6
 \tag{Hermitian-border-positive-bound}
\]
is at most
\[
 CN^{-2}+C_rq(h)^{-6}N^{r+19}e^{-cNq(h)}.
\]
For each fixed \(h\), this is summable.
The C187v29 joint-gap exceptional probability is exponentially small, uniformly over the bounded deletions on their local norm guards, and is also summable.
The local trace conditions hold almost surely eventually by (Hermitian-local-trace).
A parent norm guard implies the same norm bound for its local principal minor.
First Borel--Cantelli thus proves (Hermitian-border-positive-bound) simultaneously at every guarded parent/position pair, almost surely eventually.
The global raw-coordinate guard is used only for this deterministic net extension, not to change a conditional row distribution.

The physical Schur block of \(H_D-ihI\) is
\[
 S_i(h)=D_i^{H}-ihI_6-\mathcal B^*(\widetilde H-ihI)^{-1}\mathcal B,
\]
where \(D_i^H\) is Hermitian, including all exposed diagonal values and the fixed complex \(z\) through the dilation.
It follows that
\[
 -\operatorname{Im}S_i(h)
 \succeq hI_6+h^{-1}\mathcal B^*W_h\mathcal B
 \succeq h(1+c_4J(h))I_6.
\]
For every vector, the imaginary part of its Schur quadratic form bounds the Schur action below by this scalar times its norm.
Consequently
\[
 \|S_i(h)^{-1}\|\le[h(1+c_4J(h))]^{-1}.
\]
This inverse is exactly the physical block of \((H_D-ihI)^{-1}\).
Finally spectral calculus gives
\[
 \mathbf1_{[-h,h]}(H_D)\preceq2h\operatorname{Im}(H_D-ihI)^{-1}.
\]
Compression and the resolvent norm bound prove (Hermitized-physical-projectors).
Intersect these probability-one events over a fixed dyadic sequence tending to zero inside \((0,h_0]\); then \(\rho(h)\to0\).
Every assertion retains its fixed-\(h\)-then-large-\(N\) order.

<a id="inverse-spread-proof"></a>
## Separate physical row, column and diagonal bounds for the actual inverse

Let
\[
 P_R(h)=\mathbf1_{[0,h^2]}(Q_D^*Q_D),\qquad
 P_L(h)=\mathbf1_{[0,h^2]}(Q_DQ_D^*).
\]
The even spectral projection of the dilation is exactly \(\operatorname{diag}(P_L(h),P_R(h))\).
Thus (Hermitized-physical-projectors) bounds each corresponding three-coordinate physical compression by \(\rho(h)\).
For \(Z=Q_D^{-1}\), or a residual formed by removing whole singular terms of that inverse, write
\[
 Z_<=P_R(h)ZP_L(h),\qquad Z_>=Z-Z_<.
\]
Then \(\|Z_>\|\le h^{-1}\), and the left and right singular supports of the two pieces are mutually orthogonal.
Writing \(F=\|Z\|_{\mathrm{HS}}\), this gives
\[
 \|P_iZ_<\|_{\mathrm{HS}}^2\le\rho(h)F^2,
 \qquad \|Z_<P_i\|_{\mathrm{HS}}^2\le\rho(h)F^2,
\]
\[
 \|P_iZ_>\|_{\mathrm{HS}}^2,\ \|Z_>P_i\|_{\mathrm{HS}}^2\le3h^{-2}.
\]
The low and high row energies add because \(Z_<Z_>^*=0\); the column energies add because \(Z_<^*Z_>=0\).
Hence
\[
 \max_i\bigl(\|P_iZ\|_{\mathrm{HS}}^2+\|ZP_i\|_{\mathrm{HS}}^2\bigr)
 \le2\rho(h)F^2+6h^{-2}.
 \tag{Actual-singular-row-split}
\]

The diagonal estimate is separate.
For each physical position,
\[
 \|P_iZ_<P_i\|_{\mathrm{HS}}^2
 \le\|P_iP_R(h)\|^2\|Z_<P_i\|_{\mathrm{HS}}^2
 \le\rho(h)\|Z_<P_i\|_{\mathrm{HS}}^2.
\]
Every high diagonal block has squared norm at most \(3h^{-2}\).
The two-term square inequality and summation therefore give
\[
 \sum_i\|P_iZP_i\|_{\mathrm{HS}}^2
 \le2\rho(h)F^2+6nh^{-2}.
 \tag{Actual-singular-diagonal-split}
\]
The diagonal conclusion is not inferred merely from the maximum row conclusion.

C197v1 gives uniformly \(F^2/N\to\infty\) for the full inverse and the residual after its largest \(k_N=o(N)\) singular terms are removed.
Removing any other at most \(k_N\) singular terms leaves at least as much squared energy, so the same divergence holds uniformly for all stated residual choices.
The preceding deterministic splits apply separately to each such choice with its own \(F\).
Divide by \(F^2\), first let \(N\to\infty\) at fixed dyadic \(h\), and then let \(h\downarrow0\).
This proves (Actual-companion-spread), including the residual statement, uniformly over the guarded minors and choices.

<a id="root-block-transfer"></a>
## Transfer to the unmodified root inverse and its actual blocks

On the original norm guard, the exact inverse identity is
\[
 Q_D^{-1}=
 \begin{pmatrix}I\\B_D\\A_D\end{pmatrix}
 G_D
 \begin{pmatrix}I&A_D&2B_D\end{pmatrix}
 +\operatorname{diag}(0,-I,-I).
 \tag{Actual-companion-inverse-blocks}
\]
Its top-left block is \(G_D\), so
\[
 F_{G,D}\le F_D\le C_KF_{G,D}+\sqrt{2n}.
\]
Since \(F_D^2/N\to\infty\), this implies \(F_{G,D}^2/N\to\infty\) along the guarded minors and eventually \(F_D\le C_K'F_{G,D}\), uniformly.
The blocks at auxiliary positions \((1,1),(2,1),(1,3),(2,3)\) are, respectively,
\[
 G_D,\qquad B_DG_D,\qquad 2G_DB_D,\qquad 2B_DG_DB_D.
\]
Each scalar physical row or column of these blocks is contained in the corresponding full physical row or column of \(Q_D^{-1}\).
Likewise, the sum of squared diagonal entries of any one block is bounded by the sum of squared full physical diagonal blocks.
Applying (Actual-companion-spread) and \(F_D\le C_K'F_{G,D}\) proves both estimates in (Actual-root-block-spread).
Transpose or adjoint exchanges row and column norms and preserves absolute diagonal values, so it has the same conclusions.
No product is independently truncated, no coordinate is erased from \(G_D\), and every exact relation among these actual blocks remains available.

<a id="root-residual-transfer"></a>
## Root singular residuals retain the same physical spread

Fix an actual invertible minor, put \(M=A_DB_D+2B_DA_D-zI\), \(G=M^{-1}\), and write
\[
 W=\begin{bmatrix}I\\B_D\\A_D\end{bmatrix},\qquad
 V=\begin{bmatrix}I&A_D&2B_D\end{bmatrix},\qquad
 Z_0=\operatorname{diag}(0,-I,-I).
\]
If \(G=\sum_j q_ju_jv_j^*\) is an inverse singular expansion and \(E\) retains any subset of its complete singular terms, then
\[
 ME=\sum_{j\ \text{retained}}v_jv_j^*,\qquad
 EM=\sum_{j\ \text{retained}}u_ju_j^*.
 \tag{Root-residual-projections}
\]
Both are orthogonal projections and have operator norm at most one.
Define the actual graph matrix \(T=WEV\).
Direct multiplication, retaining the original companion rather than its Hermitian dilation, gives
\[
 Q_DW=\begin{bmatrix}M\\0\\0\end{bmatrix},\qquad
 VQ_D=\begin{bmatrix}M&0&0\end{bmatrix},
\]
\[
 Q_DT=\begin{bmatrix}MEV\\0\\0\end{bmatrix},\qquad
 TQ_D=W\begin{bmatrix}EM&0&0\end{bmatrix}.
 \tag{Root-residual-graph-actions}
\]
Consequently
\[
 \|Q_DT\|,\ \|TQ_D\|\le C_K,
 \qquad \|E\|_{\mathrm{HS}}\le\|T\|_{\mathrm{HS}}
                                      \le C_K\|E\|_{\mathrm{HS}}.
\]
The lower Hilbert--Schmidt inequality uses the top-left block of \(T\), which is exactly \(E\).

Let \(P_R(h),P_L(h)\) be the two singular projectors already controlled above.
On the right high singular space, the inverse of \(Q_D\) from its left high space has norm at most \(h^{-1}\).
Applying this to \(Q_DT\), and applying its other-sided form to \(TQ_D\), yields separately
\[
 \|(I-P_R(h))T\|\le C_Kh^{-1},\qquad
 \|T(I-P_L(h))\|\le C_Kh^{-1}.
 \tag{Root-residual-two-high-pieces}
\]
Explicitly, for a singular decomposition \(Q_D=X\Sigma Y^*\), the first high piece is
\(Y_>\Sigma_>^{-1}X_>^*Q_DT\), and the second is
\(TQ_DY_>\Sigma_>^{-1}X_>^*\), where \(\Sigma_>\) contains only singular values greater than \(h\).
Thus no commutation of \(T\) with either projector is required.

Write
\[
 T_0=P_R(h)TP_L(h),\qquad T_1=T-T_0
 =(I-P_R(h))T+P_R(h)T(I-P_L(h)).
\]
Then \(\|T_1\|\le2C_Kh^{-1}\) and \(\|T_0\|_{\mathrm{HS}}\le C_K\|E\|_{\mathrm{HS}}\).
The physical projector bound gives
\[
 \|P_iT_0\|_{\mathrm{HS}}^2,\ \|T_0P_i\|_{\mathrm{HS}}^2
 \le\rho(h)\|T_0\|_{\mathrm{HS}}^2,
\]
while each corresponding row or column of \(T_1\) has squared norm at most \(3\|T_1\|^2\).
The two-term square inequality therefore proves
\[
 \max_i\bigl(\|P_iT\|_{\mathrm{HS}}^2+\|TP_i\|_{\mathrm{HS}}^2\bigr)
 \le C_K\rho(h)\|E\|_{\mathrm{HS}}^2+C_Kh^{-2}.
 \tag{Root-residual-row-split}
\]
For the diagonal blocks, the separate estimate
\[
 \|P_iT_0P_i\|_{\mathrm{HS}}^2
 \le\rho(h)\|T_0P_i\|_{\mathrm{HS}}^2
\]
and the high-block operator bound give
\[
 \sum_i\|P_iTP_i\|_{\mathrm{HS}}^2
 \le C_K\rho(h)\|E\|_{\mathrm{HS}}^2+C_KNh^{-2}.
 \tag{Root-residual-diagonal-split}
\]
These inequalities are valid for every such root residual, without any spectral orthogonality between its two graph pieces.

It remains to prove their own-scale energy divergence uniformly over the root removals.
Suppose at most \(k_N=o(N)\) terms were removed from \(G\).
Then \(R=W(G-E)V\) has rank at most \(k_N\), and the exact identity gives
\[
 Q_D^{-1}-R=WEV+Z_0.
\]
Let \(\mathfrak q_{1,D}\ge\mathfrak q_{2,D}\ge\cdots\) be the singular values of \(Q_D^{-1}\).
For any matrix \(Z\) and any rank-at-most-\(k\) matrix \(R\),
\[
 \left(\sum_{j>k}s_j(Z)^2\right)^{1/2}\le\|Z-R\|_{\mathrm{HS}}.
\]
Indeed, projecting orthogonally off the range of \(R\) can only decrease the right norm, and the trace of \(ZZ^*\) on a subspace of dimension at most \(k\) is at most the sum of its \(k\) largest eigenvalues.
The latter assertion follows by expanding the trace in an eigenbasis, whose projection weights lie in \([0,1]\) and sum to at most \(k\).
Apply this elementary rank-approximation inequality to obtain
\[
 \left(\sum_{j>k_N}\mathfrak q_{j,D}^2\right)^{1/2}
 \le\|WEV+Z_0\|_{\mathrm{HS}}
 \le C_K\|E\|_{\mathrm{HS}}+\sqrt{2n}.
 \tag{Root-residual-energy-comparison}
\]
C197v1 makes the left side divided by \(\sqrt N\) diverge almost surely, uniformly over all the bounded deletions.
Hence \(\|E\|_{\mathrm{HS}}^2/N\to\infty\), uniformly over all permitted root removals on the norm guard.
Divide (Root-residual-row-split) and (Root-residual-diagonal-split) by this energy, send \(N\to\infty\) at fixed dyadic \(h\), and then send \(h\downarrow0\).
The four auxiliary blocks of \(T\) are exactly \(E,BE,2EB,2BEB\) at the same positions as before.
The row, column and diagonal block domination proves (Root-residual-block-spread), including transpose and adjoint.

<a id="root-head-spread"></a>
## Physical delocalization of the root singular heads and their graph images

For any fixed head index \(j\), apply the preceding root residual energy conclusion after removing its first \(j-1\) inverse singular terms.
Since the remaining squared energy is at most \(nq_j^2\), it follows that \(q_j\to\infty\), uniformly on the guarded minors.
For the established inverse expansion \(G=\sum q_ju_jv_j^*\), the exact singular-pair relations are
\[
 Mu_j=q_j^{-1}v_j,\qquad M^*v_j=q_j^{-1}u_j.
\]
Consequently
\[
 Q_DWu_j=\begin{bmatrix}q_j^{-1}v_j\\0\\0\end{bmatrix},\qquad
 Q_D^*V^*v_j=\begin{bmatrix}q_j^{-1}u_j\\0\\0\end{bmatrix}.
\]
The graph norms \(\|Wu_j\|,\|V^*v_j\|\) are bounded by \(C_K\).
Their high singular parts at a fixed \(h\) therefore have norms at most \(1/(hq_j)\), while the physical projector bound controls the low parts.
For every physical position,
\[
 \|P_iWu_j\|,\ \|P_iV^*v_j\|
 \le C_K\sqrt{\rho(h)}+\frac1{hq_j}.
\]
First let \(N\to\infty\) at fixed dyadic \(h\), then \(h\downarrow0\).
This proves the asserted maximal-coordinate bounds for \((u_j,Bu_j,Au_j)\) and \((v_j,Av_j,2Bv_j)\), including any fixed number of heads and choices within tied singular spaces.
Taking coordinatewise conjugates preserves those absolute values and gives exactly the conjugate scope stated above.

<a id="remaining-scope"></a>
## Scope of the bridge

The result supplies actual physical row and column loads and within-physical diagonal energy at the full root-inverse Hilbert--Schmidt scale, on the free spectral branch and the fixed norm guard.
It applies to full complex laws at this geometric level.
It does not establish physical multilinear coefficient lower bounds, original-law matching for complex laws, a distance estimate, or coverage of every inverse profile.
Those deductions require their own full numerator and same-row denominator arguments.
The free-gap case does not satisfy the divergent \(J(h)\) premise and is not covered by this projector proof.
