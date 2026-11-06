---
author: Yin
---

# Complete fourth-layer control on invertible bounded two-channel minors

This version continues the bounded actual-pencil branch of the [matrix-coefficient F0013 contract](../tasks/Yin_T_F0013_v1.md#contract).
Two comparable inverse modes force a dimension-independent raw polynomial separation through the actual block identities and the joint approximate-mode gap.
A direct repeated-index bound transfers this separation to the original sign basis at bounded effective rank.
Together with the fixed high-effective-rank theorem and the separately reviewed operator-gap theorem, this covers every invertible minor with a scale matching its graph area.
The singular-minor probability remains explicit; no unconditional least-value floor, logarithmic conclusion, or completion of the original Tasks is asserted.
The exact statement and argument are adopted by the [comparable-mode decision](Yin_C_F0187_v9.md#decision-comparable-modes-reviewed) at the current family entrance; the candidate decision below preserves its original assessment.

<a id="statement"></a>
## Exact model and complete invertible-minor conclusion

For \(j=1,2\), let \(W_j^{(N)}\) be independent real symmetric Wigner matrices with independent upper off-diagonal entries distributed as \(\xi_j/\sqrt N\).
The fixed real laws satisfy \(\mathbb E\xi_j=0\), \(\mathbb E\xi_j^2=1\), and \(|\xi_j|\le L\).
The diagonal entries of input \(j\) are independent copies of \(\zeta_j/\sqrt N\), where \(\zeta_j\) is fixed, real, centered and bounded by \(L\).
Zero diagonal laws are allowed.
All raw upper-triangular coordinates and the two inputs are independent within each size; cross-size coupling is arbitrary.
The constant \(L\) covers all four laws.

For \(S\subset[N]\), \(|S|\le1\), put \(n:=N-|S|\), and let \(C_{N,S},D_{N,S}\) be the corresponding principal submatrices of the first and second inputs.
The retained entries have the original \(N^{-1/2}\) normalization.
Set
\[
 \alpha:=\sqrt2,\qquad X:=C_{N,S}+D_{N,S},\qquad
 Y:=C_{N,S}+\alpha D_{N,S},\qquad
 M:=\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix}.
\]
On the invertible branch define
\[
 Z:=M^{-1}=\begin{pmatrix}G&H\\H^T&J\end{pmatrix},\quad
 T:=(H+H^T)/2,\quad Q:=\|Z\|,\quad A_Z:=\|Z\|_{\rm F},
\]
\[
 r_Z:=A_Z^2/Q^2,\qquad E_F:=(A_Z^2-Q^2)^{1/2},\qquad
 m:=s_2^\downarrow(Z).
\]
Here \(s_2^\downarrow\) is the second singular value in decreasing order, and the unsubscripted norm is the operator norm.
For any closest-to-zero unit eigenmode \(w\), with inverse eigenvalue \(q\), these definitions give \(|q|=Q\), \(E_F=\|Z-qww^T\|_{\rm F}\), and \(m=\|Z-qww^T\|\).
They are independent of the choice within a repeated eigenspace, and \(E_F>0\) for \(n\ge1\).

Define
\[
 h_Z(x):=(x^TGx)(x^TJx)-(x^TTx)^2,\qquad p_4:=\Pi_4h_Z,
\]
where \(\Pi_4\) is the fourth multilinear sign component after \(x_i=\varepsilon_i/\sqrt N\) and reduction of every \(\varepsilon_i^2\) to one.
Put
\[
 \sigma_4^2:=\sum_{|I|=4}|(p_4)_I|^2,\qquad
 L_i^{(4)}:=\sum_{\substack{|I|=4\\i\in I}}|(p_4)_I|^2,
 \qquad \tau_4:=\max_iL_i^{(4)}/\sigma_4^2
\]
when \(\sigma_4>0\).
Fix the threshold \(r_*\) of [C187v6](Yin_C_F0187_v6.md#statement) and the constant \(\gamma_*\in(0,1/2]\) of [C187v7](Yin_C_F0187_v7.md#statement), without changing either.
Define a positive minor-measurable scale by
\[
 \mathfrak a(M):=
 \begin{cases}
 A_Z^2,&r_Z\ge r_*,\\
 Q E_F,&r_Z<r_*,\ m\le\gamma_*Q,\\
 Q^2,&r_Z<r_*,\ m>\gamma_*Q.
 \end{cases}
 \tag{Complete-inverse-scale}
\]
There is a fixed \(c>0\), depending only on the laws, such that
\[
 \mathbb P\{\exists S,\ |S|\le1:\quad
 M\text{ invertible},\quad
 \sigma_4^2<c\,\mathfrak a(M)^2/N^4\}\longrightarrow0.
 \tag{All-invertible-fourth-energy}
\]
For every fixed \(\eta>0\),
\[
 \mathbb P\{\exists S,\ |S|\le1:\quad M\text{ invertible},\quad
 [\sigma_4=0\text{ or }(\sigma_4>0\text{ and }\tau_4>\eta)]\}
 \longrightarrow0.
 \tag{All-invertible-fourth-load}
\]
These are unconditional uniform bad-event statements intersected with invertibility.
They neither assert invertibility nor divide by its probability.
For general bounded laws or \(S=\varnothing\), this is a formal sign functional.
For one physical deletion and a Rademacher first off-diagonal law, it is the actual conditional fourth Walsh layer of the original parent pencil's Schur determinant, by [the fixed fresh-row identification](Yin_C_F0187_v6.md#fresh-row-scope).

The new comparable-mode conclusion is separately valid for each fixed finite \(K\ge1\) and \(0<\gamma\le1\): on \(r_Z\le K\) and \(m\ge\gamma Q\), its energy scale is \(Q^2\) and its load tends to zero, with the same uniform invertible-branch interpretation.
Its deterministic raw separation is stated and proved below, without a rank bound.
The all-invertible combination uses the exact C187v7 statement under its [separate reviewed adoption](Yin_C_F0187_v9.md#decision-operator-gap-reviewed).

<a id="matrix-reduction"></a>
## Matrix consequence with only the singular-minor average remaining

Require additionally that the first off-diagonal law is Rademacher, and put
\[
 L_N:=\begin{pmatrix}W_1+W_2&I_N\\I_N&W_1+\sqrt2W_2\end{pmatrix},
 \qquad Q_N:=(W_1+\sqrt2W_2)(W_1+W_2)-I_N.
\]
Let \(M_i\) be its retained principal pencil after deleting the two coordinates at physical index \(i\).
There are fixed \(c,C>0\) such that
\[
 \mathbb P\{s_{\min}(L_N)\le cN^{-5}
                   \text{ or }s_{\min}(Q_N)\le cN^{-5}\}
 \le o(1)+\frac C N\sum_{i=1}^N\mathbb P\{M_i\text{ is singular}\}.
 \tag{Singular-minor-only-reduction}
\]
No estimate for the average on the right is asserted.
The error is dimension-wise and is not asserted summable.

<a id="argument"></a>
## Complete candidate argument

<a id="comparable-mode-raw-separation"></a>
## Two comparable inverse modes force raw fourth-degree separation

The next deterministic argument treats comparable inverse modes without assuming a small Frobenius tail.
It uses a countable Gram construction for three bounded operators, rather than compactness of the full inverse in Frobenius norm.

Fix \(\Lambda\ge1\), \(\epsilon>0\), and \(0<\gamma\le1\).
For real symmetric \(X,Y\), define
\[
 \Gamma_\Lambda(X,Y):=
 \inf_{\substack{\|z\|=1,\ z\in\mathbb R^n\\a,b\in[-\Lambda,\Lambda]}}
 \max\{\|(X-aI)z\|,\|(Y-bI)z\|\}.
\]
There exist \(c_0,Q_0>0\), depending only on these three constants, with the following property in every dimension.
Suppose
\[
 M:=\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix}
 \quad\text{is invertible},\qquad
 \|X\|,\|Y\|\le\Lambda,\qquad
 \Gamma_\Lambda(X,Y)\ge\epsilon,
\]
and put
\[
 Z:=M^{-1}=\begin{pmatrix}G&H\\H^T&J\end{pmatrix},\qquad
 T:=(H+H^T)/2,\qquad Q:=\|Z\|.
\]
Write \(s_2^\downarrow(Z)\) for the second singular value in decreasing order.
If \(Q\ge Q_0\) and \(s_2^\downarrow(Z)\ge\gamma Q\), then
\[
 \sup_{\|x\|=1}
 \left|(x^TGx)(x^TJx)-(x^TTx)^2\right|
 \ge c_0Q^2.
 \tag{Comparable-mode-raw-separation}
\]
The constants are existence constants; this argument does not provide numerical rates in \(\Lambda,\epsilon,\gamma\).
No effective-rank or Frobenius bound is assumed in this raw polynomial conclusion.

<a id="three-operator-gram-limit"></a>
### A dimension-independent contradiction construction

If the assertion fails, choose a sequence with \(Q_m\to\infty\) and the normalized polynomial supremum tending to zero.
Set
\[
 A_m:=Z_m/Q_m,
 \qquad \delta_m:=Q_m^{-1},
 \qquad G_m:=\text{the upper-left block of }A_m.
\]
Then \(\|A_m\|=1\), \(\|G_m\|\le1\), and the actual inverse identities give
\[
 A_m=
 \begin{pmatrix}
 G_m&\delta_m I-G_mX_m\\
 \delta_m I-X_mG_m&X_mG_mX_m-\delta_mX_m
 \end{pmatrix},
 \qquad (I-Y_mX_m)G_m=-\delta_mY_m.
 \tag{Normalized-actual-identities}
\]
Choose orthonormal real eigenvectors \(w_{j,m}=(u_{j,m},v_{j,m})\), \(j=1,2\), of \(A_m\), with eigenvalues \(a_{j,m}\) satisfying
\(|a_{1,m}|=1\) and \(|a_{2,m}|\ge\gamma\).
After taking a subsequence, assume \(a_{j,m}\to a_j\), with the same lower bounds.

Consider every finite word in the three matrices \(X_m,Y_m,G_m\), including the empty word, applied to any of the four vectors \(u_{1,m},v_{1,m},u_{2,m},v_{2,m}\).
This is a countable labeled family, and the norm of each fixed label is bounded uniformly in \(m\).
Successively extracting subsequences and taking a diagonal subsequence makes all pairwise Gram inner products converge.
Their limits give a positive semidefinite bilinear form on the real vector space of finite formal combinations of the labels.
Quotient by the zero-norm subspace and complete to a real Hilbert space \(\mathcal H\).

Prefixing a label by one of the three letters defines an operator on the formal span.
The inequalities \(\|X_m f_m\|\le\Lambda\|f_m\|\), \(\|Y_m f_m\|\le\Lambda\|f_m\|\), and \(\|G_m f_m\|\le\|f_m\|\), for each fixed finite combination \(f_m\), pass to the Gram limit.
Thus these operators respect the zero-norm quotient and extend to bounded operators \(X,Y,G\) on \(\mathcal H\), with the same bounds.
The identities \(\langle X_m f_m,g_m\rangle=\langle f_m,X_mg_m\rangle\), and their analogues, show that the extensions are selfadjoint.
This construction uses only countability, bounded scalar subsequences, and completion of an inner-product space.
It does not use compactness of a Frobenius ball, finite-rank approximation of a diffuse tail, or a compact-operator spectral theorem.

All fixed polynomial identities in these operators pass on the dense label span, since each residual squared norm is a finite linear combination of convergent Gram entries.
The limiting vectors \(w_j=(u_j,v_j)\in\mathcal H\oplus\mathcal H\) remain orthonormal.
By (Normalized-actual-identities), the bounded selfadjoint operator
\[
 A:=\begin{pmatrix}G&-GX\\-XG&XGX\end{pmatrix}
     =VGV^*,\qquad Vz:=(z,-Xz),
\]
satisfies \(Aw_j=a_jw_j\) and
\[
 (I-YX)G=0.
 \tag{Limit-kernel-relation}
\]
The two nonzero eigenvalues on orthonormal vectors imply \(\operatorname{rank}A\ge2\), and the factorization implies \(\operatorname{rank}G\ge2\).

The original joint gap also passes to the limit.
Indeed, for each fixed finite label combination \(f\) and every real \(a,b\in[-\Lambda,\Lambda]\), the homogeneous inequality
\[
 \max\{\|(X_m-aI)f_m\|,\|(Y_m-bI)f_m\|\}
 \ge\epsilon\|f_m\|
\]
passes through the convergent Gram entries.
Continuity then gives this inequality for every \(f\in\mathcal H\).

The normalized polynomial supremum tending to zero implies on the label span, and then by continuity on all of \(\mathcal H\), that
\[
 (\langle x,Gx\rangle)(\langle x,XGXx\rangle)
 =\left\langle x,\frac{GX+XG}{2}x\right\rangle^2.
 \tag{Limit-quadratic-product}
\]
To see the passage directly, represent \(x\) by a fixed finite label combination \(x_m\).
Every quadratic form in this display is a Gram limit, while the absolute value of the normalized original fourth polynomial at \(x_m\) is at most its unit-sphere supremum times \(\|x_m\|^4\).
The latter norm is bounded, and the terms containing \(\delta_m\) vanish.

<a id="finite-quadratic-product"></a>
### The finite-dimensional quadratic-product lemma

Let \(A,B,C\) be real quadratic forms on a finite-dimensional real space, with \(\operatorname{rank}A\ge2\) and \(AC=B^2\) as polynomials.
Then there is a real scalar \(c\) such that \(B=cA\) and \(C=c^2A\).
Here is the complete algebraic proof used in the limit argument.
Complexify the identity and make an invertible complex linear change of coordinates reducing \(A\) to \(z_1^2+\cdots+z_r^2\), where \(r\ge2\).
Every zero of \(A\) is a zero of \(B\).
Evaluating \(B\) at \(e_i+ie_j\) and \(e_i-ie_j\), for distinct \(i,j\le r\), shows that its active diagonal coefficients are all equal and its active off-diagonal coefficients vanish.
For a radical index \(k>r\), evaluate at \(e_i\pm ie_j+t e_k\) for arbitrary complex \(t\).
The linear and quadratic coefficients in \(t\) show that all active-radical coefficients and the radical diagonal coefficient vanish.
Replacing \(e_k\) by any vector in the radical removes all remaining radical coefficients.
Thus \(B=cA\), and the original real nonzero form \(A\) forces \(c\) to be real.
Since multiplication by a nonzero polynomial cannot annihilate another nonzero polynomial, \(A(C-c^2A)=0\) gives \(C=c^2A\).
This proves the lemma without a factorization theorem as an additional input.

<a id="infinite-space-zero-transfer"></a>
### The exact zero classification needs only finite-dimensional restrictions

Write
\[
 \mathsf a(x):=\langle x,Gx\rangle,\qquad
 \mathsf b(x):=\left\langle x,\frac{GX+XG}{2}x\right\rangle,
 \qquad \mathsf c(x):=\langle x,XGXx\rangle.
\]
Choose a finite-dimensional real subspace \(E_0\subset\mathcal H\) on which the form \(\langle x,Gx\rangle\) has rank at least two.
Such a space exists because \(G\) is selfadjoint of rank at least two: otherwise every finite matrix of its bilinear form has rank at most one, forcing the whole bilinear form, and hence \(G\), to have rank at most one.
For every finite-dimensional \(E\supset E_0\), restrict the three quadratic forms in (Limit-quadratic-product) to \(E\).
The finite-dimensional \(AC=B^2\) argument in the [finite quadratic-product lemma](#finite-quadratic-product) gives
\[
 \mathsf b|_E=c_E\mathsf a|_E,\qquad
 \mathsf c|_E=c_E^2\mathsf a|_E.
\]
The scalar \(c_E\) is uniquely determined on \(E_0\), where \(\mathsf a\) is not zero, so all such scalars equal one real \(c\).
Taking \(E\) to contain each prescribed vector and using polarization yields bounded-operator identities
\[
 (GX+XG)/2=cG,\qquad XGX=c^2G.
\]
Put \(D:=X-cI\).
These identities imply
\[
 DG+GD=0,\qquad DGD=0,
 \qquad D^2G=-DGD=0.
\]
For every \(z\), selfadjointness gives
\(\|DGz\|^2=\langle Gz,D^2Gz\rangle=0\), and hence \((X-cI)G=0\).
For a nonzero \(z\in\operatorname{ran}G\), (Limit-kernel-relation) now gives
\[
 Xz=cz,\qquad z=YXz=cYz.
\]
Thus \(c\ne0\), \(Yz=c^{-1}z\), and both eigenvalues lie in \([-\Lambda,\Lambda]\).
This contradicts the transferred joint gap and proves (Comparable-mode-raw-separation).

<a id="comparable-mode-walsh-transfer"></a>
## Transfer to the complete fourth sign layer at bounded effective rank

Let \(h_Z(x):=(x^TGx)(x^TJx)-(x^TTx)^2\), and let \(\mathscr S_Z\) be its fully symmetric order-four tensor, with the arithmetic-average convention
\[
 h_Z(x)=\langle\mathscr S_Z,x^{\otimes4}\rangle,
 \qquad \mathscr S_Z:=\operatorname{Sym}_4(G\otimes J-T\otimes T).
\]
Then (Comparable-mode-raw-separation) gives \(\|\mathscr S_Z\|_{\rm F}\ge c_0Q^2\).
Write \(\mathscr S_Z^{\rm rep}\) and \(\mathscr S_Z^{\rm dist}\) for its restrictions to tuples with a repeated physical index and to tuples with all four indices distinct.
For physical index \(i\), let \(P_i\) be the orthogonal projection onto its two auxiliary coordinates.
Put
\[
 A_Z:=\|Z\|_{\rm F},\quad r_Z:=A_Z^2/Q^2,\quad
 \mathcal D(Z):=\sum_i\|P_iZP_i\|_{\rm F}^2,\quad
 d_i(Z):=\|P_iZ\|_{\rm F}^2,\quad d_*:=\max_i d_i(Z).
\]
There is an absolute constant such that
\[
 \|\mathscr S_Z^{\rm rep}\|_{\rm F}^2
 \le C A_Z^2\bigl(\mathcal D(Z)+d_*\bigr).
 \tag{Full-tensor-collision-bound}
\]
For completeness, apply the union bound to the six possible index collisions in \(G_{ij}J_{k\ell}\).
The collisions \(i=j\) or \(k=\ell\) are bounded by a diagonal squared norm times a full squared norm, hence by \(\mathcal D(Z)A_Z^2\).
Each collision between the two factors is bounded by a sum of products of squared row norms, hence by \(d_*A_Z^2\).
The same estimates apply to \(T_{ij}T_{k\ell}\), because its diagonal and row squared norms are bounded by the corresponding physical block quantities of \(Z\).
Symmetrization preserves the collision set and contracts its Frobenius norm; the two-term square inequality proves the displayed bound.

If \(r_Z\le K\) for a fixed finite \(K\), then
\[
 \frac{\|\mathscr S_Z^{\rm rep}\|_{\rm F}^2}{Q^4}
 \le C K^2
       \left(\frac{\mathcal D(Z)}{A_Z^2}
                    +\frac{d_*}{A_Z^2}\right).
 \tag{Comparable-collision-normalization}
\]
Under the [fixed full-inverse physical controls](Yin_C_F0187_v6.md#whole-layer-physical-transfer), the right side tends to zero uniformly on the invertible branch.
The raw lower bound therefore survives restriction to distinct indices.
After \(x_i=\varepsilon_i/\sqrt N\), the coefficient of four distinct signs is \(24(\mathscr S_Z)_{ijkl}/N^2\).
Consequently the complete fourth Walsh layer satisfies
\[
 \sigma_4^2=\frac{24}{N^4}
                 \|\mathscr S_Z^{\rm dist}\|_{\rm F}^2
 \ge c_1 Q^4/N^4.
 \tag{Comparable-whole-layer-energy}
\]
This is the complete layer, so no separate assumption excludes cancellation between pole and residual terms.
The [fixed coefficient load bound](Yin_C_F0187_v6.md#rank-refined-four-cycle-error) gives
\[
 L_i^{(4)}\le C A_Z^2d_i(Z)/N^4,
 \qquad \tau_4\le C_{c_1}K^2\frac{d_*}{A_Z^2}\longrightarrow0.
 \tag{Comparable-whole-layer-load}
\]

<a id="actual-model-and-three-regimes"></a>
## Actual model inputs and the exhaustive three-regime conclusion

The fixed norm event supplies \(\Lambda\ge1\) bounding both \(\|X\|\) and \(\|Y\|\), uniformly in the stated minors.
The joint gap is available for the two inputs in [C187v5](Yin_C_F0187_v5.md#statement).
For centers \(a,b\in[-\Lambda,\Lambda]\), define
\[
 c:=(\alpha a-b)/(\alpha-1),\qquad
 d:=(b-a)/(\alpha-1),\qquad
 R_\Lambda:=(\alpha+1)\Lambda/(\alpha-1).
\]
Both \(c,d\) lie in \([-R_\Lambda,R_\Lambda]\), and the inverse linear transformation of the two residuals gives
\[
 \Gamma_\Lambda(X,Y)\ge
 \frac{\alpha-1}{\alpha+1}\Gamma_{R_\Lambda}(C_{N,S},D_{N,S}).
\]
The theorem at this one fixed \(R_\Lambda\) therefore supplies a fixed \(\epsilon>0\) outside a uniform bad event tending to zero.

The [fixed full-inverse transfer](Yin_C_F0187_v6.md#whole-layer-physical-transfer), before imposing its effective-rank branch, gives
\[
 A_Z^2/n\longrightarrow\infty,\qquad
 \mathcal D(Z)/A_Z^2\longrightarrow0,\qquad
 d_*/A_Z^2\longrightarrow0
\]
in the uniform unconditional invertible-branch sense.
Since \(Q^2\ge A_Z^2/(2n)\), one also has \(Q\to\infty\) in that sense.
Thus the fixed threshold \(Q_0\) required by the raw lemma excludes only another such bad event.
For fixed \(K,\gamma\), (Comparable-collision-normalization) proves (Comparable-whole-layer-energy) and (Comparable-whole-layer-load) on the stated comparable-mode branch.
All constants are chosen before letting \(N\) increase.

For completeness, the three branches in (Complete-inverse-scale) cover every invertible minor.
Put \(K_0:=\max\{1,r_*\}\) for their common low-rank load parameter; this does not change the branch cutoff \(r_*\).
On \(r_Z\ge r_*\), use exactly the energy and load statements of [C187v6](Yin_C_F0187_v6.md#statement).
On \(r_Z<r_*\) and \(m\le\gamma_*Q\), use [C187v7](Yin_C_F0187_v7.md#statement) at its unchanged \(\gamma_*\) and at the fixed load parameter \(K=K_0\).
For any closest mode, \(m\) and \(E_F\) are exactly its residual operator and Frobenius norms, so that statement has energy \(cQ^2E_F^2/N^4\).
On \(r_Z<r_*\) and \(m>\gamma_*Q\), use the present comparable-mode result with \(K=K_0\), \(\gamma=\gamma_*\), and energy \(cQ^4/N^4\).
Taking the minimum of three positive energy constants and a union of their three uniform bad events proves (All-invertible-fourth-energy) and (All-invertible-fourth-load).
This union introduces no factor equal to the number of minors, since each input already controls all of them simultaneously.
The scales and branch tests depend only on the retained minor, with no choice of eigenvector required in their definition.

<a id="complete-graph-assembly"></a>
## Matching every inverse regime to the graph bridge

Condition at physical index \(i\) on the whole second input, the first-input minor, and the exposed first diagonal, as in [C194v13](Yin_C_F0194_v13.md#statement).
The remaining original first row consists of independent fair signs.
The bounded laws give a fixed bound \(B_0\) on its boundary matrix \(\mathcal B_i\), uniformly over that entire sign support.
Write \(\Gamma_i:=I_2+\mathcal B_i^TZ_i^2\mathcal B_i\).
The full matrix has a fixed norm guard \(b_0\ge1\) outside an exponentially small event, using the norm event inherited by the [fixed graph assembly](Yin_C_F0194_v13.md#dominant-probability-assembly).
In each minor's measurable good event impose \(\|M_i\|\le b_0\), not a condition on the fresh-row-dependent full matrix.
The simultaneous failure of this minor norm condition is contained in the full norm exception.
For an invertible such minor,
\(E_{F,i}^2\ge(2n-1)/b_0^2\ge1\) eventually, because every inverse singular value is at least \(1/b_0\).
Also impose \(Q_i\ge1\), whose uniform failure tends to zero by the preceding divergence.

The general area estimate gives
\[
 \sqrt{\det\Gamma_i}\le1+B_0^2Q_i^2.
\]
This is at most a fixed multiple of \(A_{Z_i}^2\) on the high-rank branch and of \(Q_i^2\) on the comparable branch.
On the separated branch, choose any closest mode and apply the [fixed largest-mode area formula](Yin_C_F0194_v13.md#pole-area) with residual \(E_i\).
Since \(\|E_i\|\le Q_i\), \(\|E_i\|_{\rm F}=E_{F,i}\), and both \(Q_i,E_{F,i}\) are at least one, it gives
\[
 \sqrt{\det\Gamma_i}\le C Q_iE_{F,i}.
\]
No upper bound on \(Q_i\) or small Frobenius tail is needed.
Consequently, with one fixed \(C_0\), all three regimes satisfy
\[
 \sup_{\varepsilon}\sqrt{\det\Gamma_i(\varepsilon)}
 \le C_0\mathfrak a(M_i).
\]

Choose deterministic \(t_N\to0\), enlarged to be at least \(N^{-1/2}\), slowly enough that (All-invertible-fourth-load) fails at level \(t_N\) only with uniform probability tending to zero.
Let \(\mathcal G_i\) impose invertibility, the minor norm and size conditions just stated, the energy bound, and the load bound at level \(t_N\).
These conditions are measurable in the conditioned sigma-field.
Set \(a_i:=C_0\mathfrak a(M_i)\) on \(\mathcal G_i\) and assign any positive value off that event.
The complete fourth layer is independent of the exposed diagonal and retained second-input border, so its energy and load are also minor-measurable.
The [general graph-energy hypotheses](Yin_C_F0194_v13.md#statement) now hold with one fixed positive coefficient constant, and
\[
 \frac1N\sum_i\mathbb P(\mathcal G_i^c)
 \le\frac1N\sum_i\mathbb P\{M_i\text{ singular}\}+o(1).
\]
The fixed graph theorem at \(b_N=b_0\) proves the bound for \(L_N\) in (Singular-minor-only-reduction).
Its [exact quadratic conversion](Yin_C_F0194_v13.md#dominant-probability-assembly) gives \(s_{\min}(Q_N)\ge s_{\min}(L_N)\), including simultaneous singularity, and proves the union bound as stated.
No inverse-norm guard and no conditional division by an invertibility probability occurs.

<a id="scope-and-provenance"></a>
## Scope and development provenance

The new deterministic lemma uses the actual pencil identities, a joint approximate-mode gap, and two comparable large inverse modes.
It yields raw separation without any rank bound; the fixed effective-rank bound enters only in the repeated-index and coordinate-load transfer.
The all-invertible energy statement still permits singular minors of any probability.
The matrix consequence therefore retains their average explicitly and does not settle the logarithmic or original finite-second-moment contracts.

This argument was developed in [D33's comparable-mode calculation](../drafts/Yin_D_F0033.md#comparable-mode-raw-separation), including a parallel ordinary mathematical check of the Gram-limit construction.
That draft records provenance only; all new algebra and limiting arguments needed here are included in this fixed candidate.
The finite-dimensional quadratic-product proof originates in [the same draft's exact zero classification](../drafts/Yin_D_F0033.md#homogeneous-inverse-zero-locus) and is supplied completely here.
The only separate project premises are the exact fixed interfaces listed in the decision below.
The C187v7 input has its own [applicable reviewed adoption](Yin_C_F0187_v9.md#decision-operator-gap-reviewed); the original candidate decision below retains the earlier unresolved-dependency boundary.
No independent review of this version is claimed by its development checks.

## Current assessment

[Selected decision](#decision-comparable-modes-candidate)

## Assessment history

### Decision comparable-modes-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T20:52 |
| status | open |
| reason | Complete candidate raw separation proof by a three-operator Gram limit, original-coordinate Walsh transfer, and an exhaustive three-regime invertible-minor energy/load package with a singular-minor-only matrix reduction. Applicable review of this version and adoption of its separate C187v7 operator-gap dependency remain required. The singular-minor average and original determinant contracts are not resolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [All-invertible energy and exact matrix consequence](#statement) | Bounded real actual two-channel minors, original normalization, deterministic raw comparable-mode separation, all-invertible formal-sign energy/load, actual single-deletion Rademacher border, and matrix reduction retaining the singular-minor average. |
| argument | [Complete candidate argument](#argument) | Actual inverse identities, three-operator Gram construction, finite quadratic-product algebra and Hilbert-space transfer, collision/load bounds, exhaustive coefficient regimes and measurable graph normalization. |
| dependency | [Joint approximate-mode gap](Yin_C_F0187_v5.md#statement) | Uniform no-common-approximate-mode bound for the two bounded real inputs, transferred explicitly to X and Y at a fixed center range. |
| dependency | [Full-inverse physical controls](Yin_C_F0187_v6.md#whole-layer-physical-transfer) | Uniform invertible-branch divergence, physical diagonal negligibility and vanishing normalized maximum physical row energy before imposing a rank branch. |
| dependency | [Exact fourth coefficient loads](Yin_C_F0187_v6.md#rank-refined-four-cycle-error) | The direct complete-layer coordinate load upper bound, with original N normalization, used independently of the high-rank lower bound. |
| dependency | [High-effective-rank energy and loads](Yin_C_F0187_v6.md#statement) | Unchanged fixed high-rank threshold and whole-layer energy/load theorem; its fixed fresh-row identification also fixes the actual sign-border scope. |
| dependency | [Operator-gap energy and loads](Yin_C_F0187_v7.md#statement) | Separate candidate input for the unchanged gap constant, complete-layer energy at scale Q times residual Frobenius norm, and load decay at the fixed rank cutoff; applicable adoption is required before adopting the exhaustive combination. |
| dependency | [General conditional graph bridge](Yin_C_F0194_v13.md#statement) | Real fair-sign fourth-energy/load conditions, graph area normalization and many-index norm-guarded matrix probability reduction. |
| dependency | [Largest-mode graph area](Yin_C_F0194_v13.md#pole-area) | Uniform area bound at scale Q times residual Frobenius norm for the separated branch, without Frobenius dominance. |
| dependency | [Norm event and quadratic conversion](Yin_C_F0194_v13.md#dominant-probability-assembly) | Fixed bounded-model full norm exception, actual fresh-row support bound, and exact inverse-block comparison s_min(Q_N) at least s_min(L_N). |
