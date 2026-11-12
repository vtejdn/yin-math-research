---
author: Yin
---

# Stable residual Schur backgrounds for nonselfadjoint Wigner pencils

This development for general complex-input nonselfadjoint pencils extends the [rank-o(N) residual argument](../claims/Yin_C_F0194_v25.md#stable-background-statement) by Hermitization.
It isolates a complete candidate lemma, with authoring checks but no independent review or Claim adoption.
The proof does not give coverage of its bounded residual-energy hypothesis or a least-singular-value floor.
The actual single-pole and multiple-pole contributions remain separate from the residual background.

<a id="stable-nonnormal-statement"></a>
## Candidate statement

Fix complex matrices \(D,A_1,\ldots,A_d\in M_m(\mathbb C)\), without symmetry assumptions on these coefficients.
For each input, the fixed off-diagonal law is complex, centered, has second absolute moment one and finite fourth absolute moment.
The fixed real diagonal law is centered and has finite second moment.
Use independent Hermitian Wigner inputs with original normalization \(N^{-1/2}\), within-size independence of upper pairs and colors, and arbitrary coupling across sizes.
For a fixed deletion bound and any retained physical minor of size \(n=N-O(1)\), let
\[
 M=D\otimes I_n+\sum_j A_j\otimes W_{j,\mathrm{minor}},
 \qquad G=M^{-1},\qquad g_E=\frac1N\sum_{k=1}^n E_{kk}.
\]
All conclusions below are intersected with the invertible branch of \(M\).
The blocks in \(g_E\) are the physical \(m\)-by-\(m\) blocks.
Fix \(K\ge1\) and a deterministic \(r_N=o(N)\).
Allow any minor-measurable complex matrix \(E\) satisfying
\[
 \|E\|_{\mathrm{HS}}^2/N\le K,
 \qquad \operatorname{rank}(G-E)\le r_N.
 \tag{Nonnormal-residual-data}
\]
There is no requirement that \(E\) be Hermitian, normal, commute with \(G\), or arise by spectral truncation.
Put
\[
 \eta_A(g)=\sum_j A_jgA_j,
 \qquad K_E=D-\eta_A(g_E).
\]
The two occurrences of \(A_j\) are intentional; the original pencil has the same coefficient on both mirrored physical blocks.
For each fixed \(\varepsilon>0\), uniformly over the marginal fixed-deletion laws and every admitted choice of \(E\),
\[
 \mathbb P\{\text{(Nonnormal-residual-data)},\
       \|K_Eg_E-I_m\|>\varepsilon\}\longrightarrow0.
 \tag{Nonnormal-residual-identity}
\]
Consequently, with \(h=\sqrt{mK}\), outside such a vanishing marginal exception,
\[
 \|g_E\|\le h,\qquad
 \|K_E^{-1}\|\le2h,\qquad
 \|K_E\|\le\|D\|+\Lambda h,
 \quad \Lambda=\sum_j\|A_j\|^2.
 \tag{Nonnormal-residual-stability}
\]

At a parent physical position \(i\), condition on its original minor and the exposed diagonal entries, and let \(R_i,C_i\) be the actual off-diagonal row and column blocks of this nonselfadjoint pencil.
The complex scalar fresh coordinates of \(R_i\) and \(C_i\) are conjugate copies of the same original coordinates; the two blocks are not independent.
If \(D_i=\sum_j A_j\zeta_{j,i}/\sqrt N\), then
\[
 S_E=D+D_i-R_iEC_i,\qquad B=K_E+D_i
\]
satisfy, on the residual-data event,
\[
 \mathbb E[\|S_E-B\|\mid\mathcal F_i]
 \le C\sqrt{K/N},
 \tag{Nonnormal-residual-border}
\]
where \(C\) depends only on the fixed coefficients and fourth moments.
After paying the marginal diagonal event \(\|D_i\|>(4h)^{-1}\), whose probability tends to zero, one has
\[
 s_{\min}(B)\ge(4h)^{-1},\qquad
 \|B\|\le\|D\|+\Lambda h+(4h)^{-1}.
\]
The estimates survive averaging over physical positions without an index-union cost.
They do not assert simultaneous high-probability control of all minors or summable errors.

<a id="stable-nonnormal-proof"></a>
## Hermitization and the complete candidate proof

The proof reuses the fixed-imaginary-parameter Schur mechanism of [C194v18](../claims/Yin_C_F0194_v18.md#fixed-eta-identity) and the rank/nuclear comparison of [C194v25](../claims/Yin_C_F0194_v25.md#argument).
The required change of hypotheses is proved here rather than applying their real symmetric statements to a nonsymmetric matrix.
No new external theorem or novelty claim is invoked.

For a Hermitian affine pencil \(\mathcal H=B_0\otimes I_n+\sum_jB_j\otimes W_j\) with fixed Hermitian complex coefficients, write
\[
 \mathcal G_t=(\mathcal H-itI)^{-1},\quad
 g_t=\frac1N\sum_k(\mathcal G_t)_{kk},\quad
 \mathcal B_t=B_0-itI-\sum_jB_jg_tB_j.
\]
Every actual internal resolvent has norm at most \(t^{-1}\).
For independent centered complex variance-one coordinates with uniformly bounded fourth moments, expansion of the second absolute moment gives
\[
 \mathbb E|v^*Tv-\operatorname{Tr}T|^2
 \le C\|T\|_{\mathrm{HS}}^2
 \tag{Complex-quadratic-variance}
\]
for every deterministic complex \(T\).
The surviving off-diagonal pairings are the same-index pair and its reversed pair; the latter is bounded using \(|\mathbb Ev_a^2|\le1\).
The diagonal contribution is bounded by the fourth moment, and singleton indices vanish by centering.
This argument permits varying conjugate orientations of the original laws and dependence between the real and imaginary parts of each coordinate.
Applying this to each fixed auxiliary entry of the internal border expression gives an expected Schur error \(O_t(N^{-1/2})\).
The diagonal error is also \(O(N^{-1/2})\) by its second moment.

Decoupling one physical block changes rank by at most twice the auxiliary dimension.
Its coupled/decoupled resolvent difference has nuclear norm at most a fixed multiple of \(t^{-1}\); trace duality therefore changes the normalized partial trace by \(O((Nt)^{-1})\).
These facts give the actual leave-one-out identity
\[
 \mathcal B_tg_t=\frac nN I-
       \frac1N\sum_k\mathcal E_k(\mathcal G_t)_{kk},
 \qquad \sup_k\mathbb E\|\mathcal E_k\|\longrightarrow0,
\]
and hence, for every fixed \(t>0\),
\[
 \mathbb E\|\mathcal B_tg_t-(n/N)I\|\longrightarrow0.
 \tag{Hermitian-complex-fixed-parameter}
\]
Hermiticity, not reality of the coefficients or constant, supplies every resolvent norm and diagonal-block invertibility used here.
No stability or uniqueness of a limiting Dyson equation is assumed.
The calculation concerns the unconditional actual minor, before any residual-energy event is imposed.

Now Hermitize the original nonselfadjoint matrix and its residual inverse by
\[
 \mathcal H=\begin{pmatrix}0&M\\M^*&0\end{pmatrix},\qquad
 \mathcal H^{-1}=\begin{pmatrix}0&G^*\\G&0\end{pmatrix},\qquad
 \mathcal E=\begin{pmatrix}0&E^*\\E&0\end{pmatrix}.
\]
After the fixed tensor-factor permutation, this is the preceding affine Hermitian pencil with auxiliary dimension \(2m\), coefficients
\[
 B_0=\begin{pmatrix}0&D\\D^*&0\end{pmatrix},\qquad
 B_j=\begin{pmatrix}0&A_j\\A_j^*&0\end{pmatrix}.
\]
Moreover
\[
 \|\mathcal E\|_{\mathrm{HS}}^2/N\le2K,
 \qquad \operatorname{rank}(\mathcal H^{-1}-\mathcal E)\le2r_N.
\]
For any Hermitian \(X\), put \(f_t(X)=X(I-itX)^{-1}\).
The exact identity
\[
 f_t(X)-f_t(Y)
 =(I-itX)^{-1}(X-Y)(I-itY)^{-1}
\]
shows that the difference has rank at most \(\operatorname{rank}(X-Y)\), while the separate spectral bounds give operator norm at most \(2/t\).
Also \(\|f_t(Y)-Y\|_1\le t\|Y\|_{\mathrm{HS}}^2\).
Consequently the normalized partial traces of \((\mathcal H-it)^{-1}\) and \(\mathcal E\) differ in norm by at most
\[
 2Kt+\frac{4r_N}{Nt}.
 \tag{Hermitized-residual-trace-comparison}
\]
The normalized partial trace of \(\mathcal E\) is
\[
 \mathfrak g_E=\begin{pmatrix}0&g_E^*\\g_E&0\end{pmatrix},
 \qquad \|g_E\|\le\frac{\sqrt{mn}\|E\|_{\mathrm{HS}}}{N}\le h.
\]
The fixed coefficients make the product map \(g\mapsto(B_0-\sum_jB_jgB_j)g\) uniformly continuous on each bounded set.
Thus (Hermitian-complex-fixed-parameter) and (Hermitized-residual-trace-comparison), first with fixed sufficiently small \(t\) and then \(N\to\infty\), give
\[
 \left(B_0-\sum_jB_j\mathfrak g_E B_j\right)\mathfrak g_E
 \longrightarrow I_{2m}
\]
in the stated joint marginal probability sense on the residual-data event.
Its upper-left block is exactly
\[
 \left(D-\sum_jA_jg_EA_j\right)g_E=K_Eg_E.
\]
This proves (Nonnormal-residual-identity), uniformly in every admitted \(E\), since the deterministic trace comparison is uniform and the fixed-parameter error uses the actual minor alone.
On the product-defect event \(\|K_Eg_E-I\|\le1/2\),
\[
 K_E^{-1}=g_E(K_Eg_E)^{-1}
\]
proves (Nonnormal-residual-stability).

Finally the exact conditional mean of \(R_iEC_i\) is \(\sum_jA_jg_EA_j\), because mirrored scalar coordinates are conjugates and have second absolute moment one.
The fixed auxiliary coefficient maps bound each quadratic coefficient matrix's Frobenius norm by a constant times \(\|E\|_{\mathrm{HS}}\).
Equation (Complex-quadratic-variance), the original \(N^{-1/2}\) scaling on both borders, and the fixed number of auxiliary entries therefore give (Nonnormal-residual-border).
The exposed diagonal norm has expected square \(O(N^{-1})\), and singular-value perturbation gives the asserted bounds for \(B\).
This completes the candidate proof at its stated conditional residual scope.

<a id="root-transpose-identities"></a>
## Root transpose identities at a nonreal parameter

The following root identity is valid for every real matrix \(P\) and nonreal \(z\) with \(M=P-zI\) invertible.
Write
\[
 H_z=\frac{P+P^T}{2}-zI,\quad K=\frac{P-P^T}{2},\quad
 G=M^{-1},\quad G_s=\frac{G+G^T}{2},\quad G_a=\frac{G-G^T}{2}.
\]
Subtracting \(MG=I\) and \(M^TG^T=I\) yields \(H_zG_a=-KG_s\), and therefore
\[
 G=(I-H_z^{-1}K)G_s,
 \qquad \|G\|\le\left(1+\frac{\|K\|}{|\operatorname{Im}z|}\right)\|G_s\|.
\]
The same inequality holds for the Hilbert--Schmidt norms.
Also
\[
 G_s=G^TH_zG,\qquad
 s_{\min}(G_s)\ge\frac{|\operatorname{Im}z|}{\|M\|^2}.
\]
Thus transpose symmetrization cannot discard the root inverse scale under a bounded input norm guard at a nonreal parameter.
These identities do not by themselves bound the complete quartic matching coefficients relative to the same-row graph denominator.
