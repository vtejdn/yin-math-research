---
author: Yin
---

# Auxiliary Gram separation and actual residual cross-energy for a bounded two-channel pencil

This theorem continues the bounded physical-block branch of the [matrix-coefficient F0013 contract](../tasks/Yin_T_F0013_v1.md#contract).
It proves a joint approximate-eigenvector gap, separates the two auxiliary components of every eigenmode, and uses the actual inverse-block identities to obtain a fourth cross-layer energy lower bound for closest-to-zero modes on the invertible branch.
The [reviewed physical and residual spread theorem](Yin_C_F0187_v4.md#decision-bounded-two-channel-reviewed) remains fixed at v4 and supplies the norm, closest-mode, residual-divergence and physical diagonal-energy inputs.
A separate deterministic kernel shows why Gram separation and spread alone are insufficient, and identifies the role of the actual pencil identities in the new coercivity argument.
This is a project deduction without a novelty claim, with [independent whole-proof coverage](../audits/reviews/Yin_R_F0191_v5.md#auxiliary-gram-and-actual-cross-energy) selected below.

<a id="statement"></a>
## Exact model and probability conclusions

For \(j=1,2\), let \(W_j^{(N)}\) be independent real symmetric Wigner matrices with independent upper off-diagonal entries distributed as \(\xi_j/\sqrt N\).
The fixed real laws satisfy
\(\mathbb E\xi_j=0\), \(\mathbb E\xi_j^2=1\), and \(|\xi_j|\le L\).
The diagonal entries of input \(j\) are independent copies of \(\zeta_j/\sqrt N\), where \(\zeta_j\) is fixed, real, centered and bounded by \(L\).
Zero diagonal laws are allowed.
All raw upper-triangular coordinates and both inputs are independent within each size.
Across different sizes the coupling is arbitrary.
The finite constant \(L\) is chosen to cover all four fixed laws.

For \(S\subset[N]\), \(|S|\le1\), put \(n:=N-|S|\) and let \(C_{N,S},D_{N,S}\) be the corresponding principal submatrices of the two inputs.
Their entries retain the original \(N^{-1/2}\) normalization.
For \(R>0\) and two real symmetric \(n\)-by-\(n\) matrices, define
\[
 \Gamma_R(C,D):=
 \inf_{\substack{\|z\|=1,\ z\in\mathbb R^n\\a,b\in[-R,R]}}
 \max\{\|(C-aI)z\|,\|(D-bI)z\|\}.
 \tag{Joint-residual-gap}
\]
For every fixed \(R>0\), there is a fixed \(\epsilon_R>0\), depending only on \(R\) and the fixed laws, such that
\[
 \mathbb P\left\{
 \min_{\substack{S\subset[N]\\|S|\le1}}
      \Gamma_R(C_{N,S},D_{N,S})<\epsilon_R
 \right\}\longrightarrow0.
 \tag{No-common-approximate-mode}
\]
In particular, the same event controls the full inputs and every single physical principal deletion.

Set \(\alpha:=\sqrt2\), \(J_\circ:=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), and \(T:=\operatorname{diag}(1,\alpha)\).
For the same minors define the actual pencil
\[
 \mathcal M_{N,S}
 :=J_\circ\otimes I_n+I_2\otimes C_{N,S}+T\otimes D_{N,S}
 =\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix},
 \qquad X:=C_{N,S}+D_{N,S},\quad
 Y:=C_{N,S}+\alpha D_{N,S}.
 \tag{Actual-pencil}
\]
For a real unit eigenvector \(w=(u,v)\in\mathbb R^n\oplus\mathbb R^n\), write
\[
 \mathcal G_w:=
 \begin{pmatrix}\|u\|^2&\langle u,v\rangle\\
                 \langle u,v\rangle&\|v\|^2\end{pmatrix}.
\]
There is a fixed \(g>0\), depending only on the fixed laws, such that
\[
 \begin{split}
 \mathbb P\{\exists S\subset[N],\ |S|\le1,\ \lambda\in\mathbb R,\ w\in\mathbb R^{2n}:\quad
 &\|w\|=1,\ \mathcal M_{N,S}w=\lambda w,\\
 &\lambda_{\min}(\mathcal G_w)<g\}\longrightarrow0.
 \end{split}
 \tag{Auxiliary-Gram-gap}
\]
This controls all eigenvalues and every real unit vector in each eigenspace, including zero eigenvalues and repeated eigenvalues.
No invertibility assumption is imposed.
These are probability statements for the bounded real model, not extensions to all fixed finite-second-moment laws or determinant lower bounds.

<a id="cross-polynomial"></a>
## Residual cross-layer functional and its actual lower bound

For any real unit \(w=(u,v)\) and real symmetric residual matrix
\[
 \mathsf E=\begin{pmatrix}F&H_0\\H_0^T&J_0\end{pmatrix},
 \qquad T_0:=(H_0+H_0^T)/2,
\]
define
\[
 s_{w,\mathsf E}(x)
 :=(u^Tx)^2(x^TJ_0x)+(v^Tx)^2(x^TFx)
       -2(u^Tx)(v^Tx)(x^TT_0x).
 \tag{Cross-polynomial}
\]
For the stated physical size \(n\) and normalization \(N\), \(\Pi_4s_{w,\mathsf E}\) denotes the degree-four multilinear sign component after substituting \(x_i=\varepsilon_i/\sqrt N\) and reducing every \(\varepsilon_i^2\) to one.
Write \(s_{4,w}:=\Pi_4s_{w,\mathsf E}\) and \(\sigma(s_{4,w})^2:=\sum_{|I|=4}|(s_{4,w})_I|^2\) for its squared Walsh coefficient norm.
Define its visible residual energy, row energies and physical mode masses by
\[
 \begin{split}
 \mathcal R^2(\mathsf E)&:=\|\operatorname{off}F\|_{\rm F}^2
   +\|\operatorname{off}J_0\|_{\rm F}^2
   +\|\operatorname{off}T_0\|_{\rm F}^2,\\
 \rho_i(\mathsf E)&:=\sum_{j\ne i}
       (|F_{ij}|^2+|(J_0)_{ij}|^2+|(T_0)_{ij}|^2),\\
 \eta_i(w)&:=u_i^2+v_i^2.
 \end{split}
 \tag{Residual-quantities}
\]
The operation \(\operatorname{off}\) removes the diagonal in the stated physical coordinate basis.

<a id="actual-cross-energy-statement"></a>
### Closest-mode cross-energy on actual invertible minors

For each invertible \(\mathcal M_{N,S}\), let \(\mathcal W_{N,S}\) consist of all real unit eigenvectors whose eigenvalues have smallest absolute value.
For \(w\in\mathcal W_{N,S}\), with eigenvalue \(\lambda\), put
\[
 q:=\lambda^{-1},\qquad
 \mathsf E_w:=\mathcal M_{N,S}^{-1}-qww^T.
\]
There is a fixed \(c_*>0\), depending only on the fixed laws, such that
\[
 \begin{split}
 \mathbb P\{\exists S,\ |S|\le1:\;&
 \mathcal M_{N,S}\text{ is invertible and }
 \exists w\in\mathcal W_{N,S}\\
 &\text{with }\sigma(s_{4,w})^2
       <c_*\|\mathsf E_w\|_{\rm F}^2/N^4\}
 \longrightarrow0.
 \end{split}
 \tag{Closest-mode-cross-energy}
\]
The same statement holds with \(\mathcal R^2(\mathsf E_w)\) on the right, since \(\mathcal R^2(\mathsf E_w)\le\|\mathsf E_w\|_{\rm F}^2\).
The estimate is uniform over the entire closest-mode set, including arbitrary unit choices inside repeated eigenspaces.
It is an unconditional bad-event bound intersected with invertibility, not a conclusion that invertibility has probability tending to one or a conditional probability estimate obtained by dividing by that probability.

For general bounded input laws this is a formal sign coefficient functional.
Only when \(|S|=1\) and the exposed first input is Rademacher does it identify the actual conditional cross fourth Walsh layer of a fresh row in the original \(N\)-dimensional parent matrix.
For \(S=\varnothing\), the same normalization defines a formal sign probe and is not a fresh border of that parent matrix.
No reduction of other entry laws to Rademacher support is asserted.
No pole-dominance condition is assumed in (Closest-mode-cross-energy).

<a id="generic-kernel-statement"></a>
### A deterministic cancellation boundary outside the actual pencil class

For \(n=4m\to\infty\) and \(N=n+1\), there are deterministic invertible real symmetric matrices \(\widetilde{\mathcal M}_n\), bounded in operator norm, with a real unit closest-to-zero eigenvector \(w_n\) and inverse eigenvalue \(q_n=n^3\), such that their genuine spectral residuals
\(\mathsf E_n:=\widetilde{\mathcal M}_n^{-1}-q_nw_nw_n^T\)
satisfy
\[
 \begin{gathered}
 \mathcal G_{w_n}=I_2/2,\qquad
 \eta_i(w_n)=1/n,\qquad \mathsf E_nw_n=0,\qquad
 \|\mathsf E_n\|_{\rm F}^2=12n^2+2n-1,\\
 \mathcal R^2(\mathsf E_n)=(5/2)n^2+O(n),\qquad
 \frac{\max_i\rho_i(\mathsf E_n)}{\mathcal R^2(\mathsf E_n)}=O(n^{-1}),
 \qquad
 \frac{|q_n|}{\mathcal R(\mathsf E_n)}\longrightarrow\infty,\\
 \Pi_4s_{w_n,\mathsf E_n}=0.
 \end{gathered}
 \tag{Spread-cross-kernel}
\]
Thus Gram nondegeneracy, physical and residual row spread, residual orthogonality, comparability of visible and full residual energies, and pole dominance do not imply cross-layer noncollapse by themselves.
This construction is not asserted to have off-diagonal auxiliary block \(I_n\), to be an actual minor of (Actual-pencil), or to occur under any fixed Wigner entry law.
It is a counterexample only to the inference from those listed abstract properties; it is not a counterexample to the actual pencil problem or the F0013 contract.

<a id="inputs"></a>
## Fixed inputs, source scope and extraction

The [bounded-product convex concentration inequality (9)](Yin_C_F0187_v2.md#proof) is used for a convex norm of independent raw bounded coordinates.
Its GNT14 source statement and inspection boundary remain those retained by that fixed input.
The [scalar weak spectral convergence](Yin_C_F0186_v4.md#statement) supplies the semicircle limit for the first input, with bounded continuous limiting density.
The [bounded-input norm event](Yin_C_F0187_v4.md#spectral-residual-spread) supplies a fixed simultaneous bound on the two full input norms outside probability \(Ce^{-cN}\).
For the cross-energy deduction, the same fixed proof's [uniform minor mass](Yin_C_F0187_v4.md#weighted-minor-mass) and [physical projector bound](Yin_C_F0187_v4.md#fresh-row-projector) supply a closest eigenvalue tending to zero and vanishing closest-mode physical leverage.
Its [residual-divergence and physical diagonal-energy estimates](Yin_C_F0187_v4.md#spectral-residual-spread) give \(\|\mathsf E_w\|_{\rm F}^2/n\to\infty\) and \(\sum_i\|P_i\mathsf E_wP_i\|_{\rm F}^2/\|\mathsf E_w\|_{\rm F}^2\to0\), uniformly over the stated minors and removed modes in the unconditional invertible-branch sense.
Here \(P_i\) is the rank-two projection onto physical coordinate \(i\) in the two auxiliary channels.
The approximate-mode and Gram arguments use only the norm-event input from v4; the additional fixed interfaces are used precisely in the closest-mode cross-energy passage.

Finite-dimensional principal interlacing, spectral projections, sphere nets and elementary matrix identities are used explicitly.
Interlacing is used only for unweighted scalar eigenvalue counts.
No local-law theorem, full-source proof re-audit, new source acquisition or fixed-matrix inverse bound is assumed.

The mathematical extraction is from the [auxiliary Gram development](../drafts/Yin_D_F0033.md#auxiliary-gram-gap), its [cross-layer kernel](../drafts/Yin_D_F0033.md#cross-layer-kernel), and the [actual residual cross-energy argument](../drafts/Yin_D_F0033.md#actual-residual-cross-coercivity).
Those rolling sections record development provenance, not proof dependencies.
All necessary arguments and definitions for the present fixed statement are supplied here and by the exact fixed inputs above.
Neither the v4 review nor the ordinary development check is treated as an independent review of this new version.

<a id="argument"></a>
## Complete argument

<a id="joint-gap-proof"></a>
### No common approximate eigenvector


Fix \(R>0\) and choose a fixed \(B\ge1\) such that the full input norms are at most \(B\) outside a set of probability \(Ce^{-cN}\).
Their principal minors then have the same norm bound.

For any deterministic real unit \(z\) and real \(b\), put \(Y:=\|(D-bI)z\|\).
If the raw second-input diagonal variance is \(\sigma_{\zeta_2}^2\), independence and centering give exactly
\[
 \mathbb E Y^2=\frac{n-1+\sigma_{\zeta_2}^2}{N}+b^2.
 \tag{Fixed-vector-second-moment}
\]
In particular the lower bound tends to one even for zero diagonal law.
As a function of the independent raw upper-triangular entries, \(Y\) is convex and \(\sqrt{2/N}\)-Lipschitz: the corresponding matrix difference has Frobenius norm at most \(\sqrt{2/N}\) times the Euclidean raw-coordinate difference.
The bounded-product inequality therefore gives
\[
 \mathbb P\{|Y-\operatorname{med}Y|>t\}\le C e^{-cNt^2},
 \qquad
 \mathbb E|Y-\operatorname{med}Y|^2\le C/N.
\]
The \(L^2\) triangle inequality implies
\(\operatorname{med}Y\ge(\mathbb E Y^2)^{1/2}-C/\sqrt N\ge1/2\)
eventually.
Consequently
\[
 \mathbb P\{\|(D-bI)z\|<\gamma\}\le C e^{-cN},
 \qquad \gamma:=1/4,
 \tag{Fixed-vector-gap}
\]
uniformly in \(z,b\), in the deletion index and in \(n\in\{N,N-1\}\).

Choose a sphere-net mesh \(0<\theta<1\) and a finite \(b\)-grid in \([-R,R]\) such that
\((B+R)\theta\le\gamma/8\) and the grid approximation error is at most \(\gamma/8\).
Then choose \(0<\kappa<1\) so that
\(\kappa\log(3/\theta)<c/2\), where \(c\) is the exponent constant in (Fixed-vector-gap).
For any subspace \(V\subset\mathbb R^n\) of dimension at most \(\kappa n\), independent of \(D\), a \(\theta\)-net of its unit sphere has at most \((3/\theta)^{\kappa n}\) elements.
Conditional on \(V\), apply (Fixed-vector-gap) to this net and the \(b\)-grid.
On the norm event for \(D\), approximation gives
\[
 \inf_{\substack{z\in V,\ \|z\|=1\\b\in[-R,R]}}\|(D-bI)z\|
 \ge\gamma/2
 \tag{Small-subspace-gap}
\]
outside a set of conditional probability at most \(C_R e^{-cN/2}\), after adjusting constants.
The norm-event failure has the same bound uniformly after conditioning on the first input, since the two full inputs are independent.

Choose a fixed \(h>0\), sufficiently small in terms of \(\kappa\), and an \(h\)-mesh grid \(a_j\) covering \([-R,R]\).
The semicircle density is bounded, so every interval \([a_j-2h,a_j+2h]\) has limiting spectral mass at most \(\kappa/4\) after decreasing \(h\).
Scalar weak convergence gives, with probability tending to one, at most \(\kappa N/2\) eigenvalues of the full first input in each of these finitely many windows.
Ordinary principal interlacing changes an interval count by at most two after one physical deletion.
Hence all the subspaces
\[
 V_{S,j}:=\operatorname{Ran}
  \mathbf1_{[a_j-2h,a_j+2h]}(C_{N,S}),\qquad |S|\le1,
\]
have dimension at most \(\kappa(N-|S|)\) eventually on that event.
This use of interlacing concerns unweighted scalar eigenvalue counts.
Conditional on the full first input, a union over the finitely many windows and the \(N+1\) minors in (Small-subspace-gap) still has failure tending to zero.

For \(a\in[-R,R]\), choose \(a_j\) within \(h\) of \(a\) and let \(P\) project onto \(V_{S,j}\).
If a unit \(z\) obeyed both residual bounds in (No-common-approximate-mode) with upper bound \(\epsilon\), spectral calculus would give
\[
 \|(I-P)z\|\le\epsilon/h.
\]
For \(\epsilon<h/4\), the unit vector \(z':=Pz/\|Pz\|\) exists and satisfies \(\|z-z'\|\le2\epsilon/h\).
On the norm event,
\[
 \|(D-bI)z'\|\le\epsilon+2(B+R)\epsilon/h.
\]
Choose a fixed \(\epsilon_R>0\) smaller than \(h/4\) and such that the last upper bound is below \(\gamma/2\).
This contradicts (Small-subspace-gap), proving (No-common-approximate-mode).
The constant order is \(B,R\), then \(\theta,\kappa\), then \(h\), then \(\epsilon_R\); all are fixed before \(N\) grows.

<a id="gram-gap-proof"></a>
### From the joint residual gap to auxiliary Gram separation

Now work on the same norm event for an actual pencil eigenpair.
Choose a fixed \(\Lambda\) bounding \(\|\mathcal M\|\), \(\|X\|\) and \(\|Y\|\), and put \(L_*:=2\Lambda\).
The equations
\[
 Xu+v=\lambda u,\qquad u+Yv=\lambda v
\]
give \(\|v\|\le L_*\|u\|\) and \(\|u\|\le L_*\|v\|\).
Thus
\[
 \|u\|,\|v\|\ge b_*:=(1+L_*^2)^{-1/2}>0.
\]
Let \(\Delta_w:=\|u\|^2\|v\|^2-\langle u,v\rangle^2\), and write
\[
 t:=\frac{\langle u,v\rangle}{\|u\|^2},\qquad
 v=tu+r,\qquad r\perp u,\qquad
 \|r\|^2=\Delta_w/\|u\|^2.
\]
If \(\Delta_w\le b_*^4/4\), then \(\|r\|\le b_*/2\), and therefore
\(b_*/2\le|t|\le1/b_*\).
For \(x_0:=\lambda-t\) and \(y_0:=\lambda-t^{-1}\), the two block equations give
\[
 (X-x_0I)u=-r,\qquad
 (Y-y_0I)u=t^{-1}(\lambda I-Y)r.
\]
The second residual has norm at most \(2L_*\|r\|/b_*\).
Since
\[
 C=\frac{\alpha X-Y}{\alpha-1},\qquad
 D=\frac{Y-X}{\alpha-1},
\]
the unit vector \(u/\|u\|\) has simultaneous \(C,D\) residuals bounded by \(K_*\|r\|\), where one can take
\[
 K_*:=\frac{\alpha+2L_*/b_*}{(\alpha-1)b_*}.
\]
Their scalar centers are
\[
 a_0:=\frac{\alpha x_0-y_0}{\alpha-1},\qquad
 b_0:=\frac{y_0-x_0}{\alpha-1}.
\]
They lie in a fixed interval \([-R,R]\), for example with
\(R:=(\alpha+1)(\Lambda+2/b_*)/(\alpha-1)\).
Apply (No-common-approximate-mode) at that \(R\).
If
\[
 0<g<\min\left\{b_*^4/4,\,
             b_*^2\epsilon_R^2/(4K_*^2)\right\},
\]
then \(\Delta_w<g\) would make both residuals smaller than \(\epsilon_R\), a contradiction.
Thus \(\Delta_w\ge g\) uniformly over all these eigenvectors and minors.
The Gram matrix has trace one, so its smallest eigenvalue is at least its determinant.
This proves (Auxiliary-Gram-gap), with no invertibility assumption.

<a id="kernel-proof"></a>
### Complete deterministic kernel construction

The Gram gap, residual orthogonality and row spread do not by themselves imply cross-layer noncollapse.
The following finite-dimensional construction tests precisely those conditions, not the actual pencil identities or a fixed Wigner law.
Take \(n:=4m\), \(N:=n+1\), and divide the physical coordinates into four equal blocks.
Let \(e,f,h\) be \(n^{-1/2}\) times the vectors constant on those blocks with respective sign patterns \((1,1,1,1)\), \((1,1,-1,-1)\), and \((1,-1,1,-1)\).
They are orthonormal, and every coordinate has absolute value \(n^{-1/2}\).
Set \(u:=e/\sqrt2\), \(v:=f/\sqrt2\), and \(w:=(u,v)\), so its auxiliary Gram matrix is \(I_2/2\) and its physical masses are exactly \(1/n\).
Define
\[
 F_\sharp:=eh^T+he^T,\qquad J_\sharp:=0,\qquad
 H_\sharp:=2fh^T-hf^T,\qquad
 T_\sharp:=(fh^T+hf^T)/2,
\]
\[
 \mathsf Z:=\begin{pmatrix}F_\sharp&H_\sharp\\H_\sharp^T&0\end{pmatrix}.
\]
Then \(F_\sharp e+H_\sharp f=h-h=0\) and \(H_\sharp^Te=0\), so \(\mathsf Zw=0\).
For the cross polynomial \(s\) defined in (Cross-polynomial), linearity in the residual blocks gives
\[
 s_{\mathsf Z}(x)
 =\tfrac12(f^Tx)^2\,2(e^Tx)(h^Tx)
       -(e^Tx)(f^Tx)(f^Tx)(h^Tx)=0
\]
for every real \(x\), before any sign restriction.

One can also retain a full residual spectrum and its large-energy normalization.
Put
\[
 \mathsf E_n:=I_{2n}-ww^T+n\mathsf Z.
\]
The identity component minus \(ww^T\) contributes exactly
\(\|x\|^2((u^Tx)^2+(v^Tx)^2)\) to \(s\).
On \(x_i=\varepsilon_i/\sqrt N\), \(\|x\|^2=n/N\) is constant, so
\[
 \Pi_4s_{\mathsf E_n}=0,\qquad \mathsf E_nw=0.
 \tag{Kernel-sign-vanishing}
\]
Orthogonality of \(e,f,h\) gives
\(\operatorname{Tr}\mathsf Z=0\) and \(\|\mathsf Z\|_{\rm F}^2=12\), hence
\[
 \|\mathsf E_n\|_{\rm F}^2=12n^2+2n-1.
\]
For the visible residual blocks, the squared off-diagonal energy of \(\mathsf Z\) is \(5/2-5/n\): the \(F_\sharp\) contribution is \(2-4/n\), and the \(T_\sharp\) contribution is \(1/2-1/n\).
The added rank-one block terms have bounded Frobenius norm.
Write \(\mathcal R_n:=\mathcal R(\mathsf E_n)\) and \(\rho_{i,n}:=\rho_i(\mathsf E_n)\).
It follows that
\[
 \mathcal R_n^2=(5/2)n^2+O(n),\qquad
 \max_i\rho_{i,n}=O(n),\qquad
 \frac{\max_i\rho_{i,n}}{\mathcal R_n^2}=O(n^{-1}).
\]
Thus the residual scale is comparable to its full Frobenius norm, that norm squared divided by \(n\) diverges, and both spread quantities vanish, while the cross fourth layer is zero.

For completeness, this can be a genuine spectral residual of some bounded real symmetric matrix, although not of the prescribed pencil.
On \(w^\perp\), \(\mathsf E_n=I+n\mathsf Z\).
All nonzero eigenvalues of \(\mathsf Z\) belong to one fixed finite list, since its action is supported on the two copies of \(\operatorname{span}\{e,f,h\}\).
Consequently \(\mathsf E_n\) is invertible on \(w^\perp\) for sufficiently large \(n\).
Indeed, each nonzero fixed eigenvalue \(\nu\) gives \(|1+n\nu|\ge1\) eventually, while the zero eigenvalues give one.
Taking \(q:=n^3\), the matrix
\[
 \widetilde{\mathcal M}_n:=(qww^T+\mathsf E_n)^{-1}
\]
is real symmetric and bounded in norm; \(w\) is its closest-to-zero mode, and \(|q|/\mathcal R_n\to\infty\).
There is no assertion that its off-diagonal auxiliary block equals \(I_n\), or that it occurs in the support of an actual Wigner minor.
The example therefore excludes an inference from Gram nondegeneracy, residual orthogonality, the established spread conditions and pole dominance alone.
The actual-pencil proof below uses the constrained inverse-block relations to control this kernel's tangent directions; no inference from the listed abstract properties alone is made.

<a id="actual-residual-cross-coercivity"></a>
### Actual residual cross-energy coercivity

First work deterministically with
\[
 \mathcal M=\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix},
 \qquad X=X^T,\quad Y=Y^T,\quad
 \mathcal M\text{ invertible},\quad \|X\|\le\Lambda.
\]
Let \(w=(u,v)\) be any real unit eigenvector with nonzero eigenvalue \(\lambda\), and assume
\[
 |\lambda|\le1,\qquad
 \begin{pmatrix}\|u\|^2&\langle u,v\rangle\\
                 \langle u,v\rangle&\|v\|^2\end{pmatrix}
 \succeq gI_2,\qquad g>0.
 \tag{Coercivity-hypotheses}
\]
No assertion for all eigenvalues outside \([-1,1]\) is made.
Write
\[
 q:=\lambda^{-1},\qquad
 \mathsf E:=\mathcal M^{-1}-qww^T
   =\begin{pmatrix}F&H_0\\H_0^T&J_0\end{pmatrix},
 \qquad T_0:=(H_0+H_0^T)/2.
\]
Thus \(\mathsf Ew=0\) and \(\mathcal M\mathsf E=\mathsf E\mathcal M=I_{2n}-ww^T\).
Let \(s:=s_{w,\mathsf E}\), \(s_4:=\Pi_4s\), and \(\mathcal R:=\mathcal R(\mathsf E)\) have the meanings in (Cross-polynomial) and (Residual-quantities).
The sign normalization remains \(x_i=\varepsilon_i/\sqrt N\); the following deterministic identities hold for any \(N\), with \(n=N-1\) at an actual single physical border.

For an ordered four-index tensor use its ordinary Frobenius norm, and let \(\operatorname{Sym}\) average over all \(24\) permutations of its indices.
Define
\[
 \mathscr S:=\operatorname{Sym}\!
 \left(u\otimes u\otimes J_0
       +v\otimes v\otimes F
       -2u\otimes v\otimes T_0\right).
 \tag{Cross-tensor}
\]
Here a matrix occupies the last two tensor positions before symmetrization.
Then
\[
 s(x)=\langle\mathscr S,x^{\otimes4}\rangle.
\]
There are constants \(c_{\Lambda,g},C_{\Lambda,g}>0\), independent of the dimension and inverse norm, such that
\[
 \|\mathscr S\|_{\rm F}^2
 \ge c_{\Lambda,g}\|\mathsf E\|_{\rm F}^2
      -C_{\Lambda,g}n.
 \tag{Actual-raw-coercivity}
\]
The error \(O(n)\) is essential to this argument and is handled by the residual divergence, rather than discarded at a fixed residual scale.

<a id="coercive-tensor-projection"></a>
#### A dimension-free projection and the actual residual identity

Put
\[
 P:=I_n-\frac{uu^T}{\|u\|^2},\qquad
 t:=Pv,\qquad A:=PFP.
\]
The Gram hypothesis ensures \(\|u\|>0\).
Writing \(c:=\langle u,v\rangle\), apply that hypothesis to \((-c/\|u\|^2,1)\) to obtain
\[
 \|t\|^2=\|v\|^2-\frac{c^2}{\|u\|^2}\ge g.
 \tag{Projected-auxiliary-size}
\]
Projection in all four tensor positions kills both terms containing \(u\), and hence
\[
 P^{\otimes4}\mathscr S
       =\operatorname{Sym}(t\otimes t\otimes A).
 \tag{Projected-cross-tensor}
\]

For completeness, if \(f\) is a unit vector and \(A\) is any real symmetric matrix, write
\[
 A=a\,ff^T+fb^T+bf^T+C,\qquad b\perp f,\quad Cf=0.
\]
The tensor components with respectively four, three, or two indices in the \(f\) direction are orthogonal.
Counting their permutation multiplicities gives exactly
\[
 \|\operatorname{Sym}(f\otimes f\otimes A)\|_{\rm F}^2
   =a^2+\|b\|^2+\tfrac16\|C\|_{\rm F}^2
   \ge\tfrac16\|A\|_{\rm F}^2 .
 \tag{Symmetric-product-coercivity}
\]
For example the perpendicular block has six possible locations for the two \(f\) indices, each with coefficient \(C_{ij}/6\); the mixed block is \(2\operatorname{Sym}(f^{\otimes3}\otimes b)\), whose squared norm is \(\|b\|^2\).
Since \(P^{\otimes4}\) is an orthogonal projection, (Projected-cross-tensor) therefore implies
\[
 \|PFP\|_{\rm F}
 \le\frac{\sqrt6}{\|t\|^2}\|\mathscr S\|_{\rm F}
 \le\frac{\sqrt6}{g}\|\mathscr S\|_{\rm F}.
 \tag{Perpendicular-F-control}
\]
This proves the needed distance to the tangent subspace without a dimension-dependent compactness argument or a classification of every triple in the generic kernel.

There exists a real vector \(a_*\) such that
\[
 F=ua_*^T+a_*u^T+A,\qquad A=PFP.
 \tag{F-tangent-decomposition}
\]
One explicit choice is
\[
 a_*:=\frac{Fu}{\|u\|^2}
       -\frac{u^TFu}{2\|u\|^4}\,u .
\]
The actual residual identities give
\[
 H_0=I_n-uu^T-FX,\qquad
 XH_0+J_0=-uv^T,\qquad
 Fu+H_0v=0.
 \tag{Coercive-residual-identities}
\]
The first equality is the top-left block of \(\mathsf E\mathcal M=I-ww^T\), the second is the top-right block of \(\mathcal M\mathsf E=I-ww^T\), and the third is \(\mathsf Ew=0\).
In particular, with
\[
 k:=u-Xv,\qquad d:=\langle u,k\rangle,
\]
one has
\[
 Fk=-v+cu,\qquad
 d=\|u\|^2-\langle Xu,v\rangle
   =1-\lambda c\ge\tfrac12.
 \tag{Actual-F-k}
\]
The last step uses \(Xu+v=\lambda u\), \(|c|\le1/2\), and \(|\lambda|\le1\).
Also \(\|k\|\le1+\Lambda\).
Substituting (F-tangent-decomposition) into (Actual-F-k) gives
\[
 (dI_n+uk^T)a_*=-v+cu-Ak.
\]
Since \(k^Tu=d\), the inverse is exactly
\[
 (dI_n+uk^T)^{-1}
   =d^{-1}I_n-\frac{uk^T}{2d^2}.
 \tag{Tangent-inverse}
\]
Its norm is bounded by a constant depending only on \(\Lambda\).
Consequently
\[
 \|a_*\|\le C_\Lambda(1+\|A\|_{\rm F}),\qquad
 \|F\|_{\rm F}\le C_{\Lambda,g}(1+\|\mathscr S\|_{\rm F}).
 \tag{Actual-F-control}
\]

The first two identities in (Coercive-residual-identities) now give
\[
 \|H_0\|_{\rm F}\le\sqrt n+1+\Lambda\|F\|_{\rm F},
 \qquad
 \|J_0\|_{\rm F}\le1+\Lambda\|H_0\|_{\rm F}.
\]
Using \(\|\mathsf E\|_{\rm F}^2=\|F\|_{\rm F}^2+\|J_0\|_{\rm F}^2+2\|H_0\|_{\rm F}^2\), we obtain
\[
 \|\mathsf E\|_{\rm F}^2
 \le C_{\Lambda,g}\bigl(n+\|\mathscr S\|_{\rm F}^2\bigr).
\]
This proves (Actual-raw-coercivity).
In particular an exact raw cross kernel at these actual-pencil hypotheses can have only \(\|\mathsf E\|_{\rm F}^2=O_{\Lambda,g}(n)\).
The earlier generic construction has a residual of order \(n^2\) in squared norm and cannot satisfy all these actual inverse identities with a bounded \(X\), a near-zero mode and the stated Gram gap.

<a id="distinct-index-transfer"></a>
#### Repeated physical indices and the exact Walsh normalization

Put
\[
 \eta_*:=\max_i(u_i^2+v_i^2),\qquad
 \mathcal D(\mathsf E):=\sum_i\|P_i\mathsf E P_i\|_{\rm F}^2,
\]
where \(P_i\) is the rank-two physical coordinate projection.
Let \(\mathscr S_{\rm rep}\) retain the tensor entries whose four physical indices have at least one coincidence, and let \(\mathscr S_{\rm dist}\) retain the entries with all indices distinct.
There is a universal \(C\) such that
\[
 \|\mathscr S_{\rm rep}\|_{\rm F}^2
 \le C\left(\eta_*\|\mathsf E\|_{\rm F}^2
                +\mathcal D(\mathsf E)\right).
 \tag{Repeated-index-error}
\]

To verify this, first consider an unsymmetrized tensor \(B_{ijkl}:=a_i b_j Z_{kl}\), with \(a,b\in\{u,v\}\) and a residual matrix block \(Z\).
Both vector norms are at most one, and every squared vector coordinate is at most \(\eta_*\).
A union over the six possible equalities among \(i,j,k,l\) gives
\[
 \sum_{\text{some indices equal}}|B_{ijkl}|^2
 \le5\eta_*\|Z\|_{\rm F}^2+\sum_k|Z_{kk}|^2.
 \tag{Six-collision-bound}
\]
For \(i=j\), use \(\sum_i a_i^2b_i^2\le\eta_*\); each of the four vector-matrix index coincidences is bounded by \(\eta_*\|Z\|_{\rm F}^2\); and \(k=l\) gives the diagonal term.
These are upper bounds on a union, so multiple coincidences cause no omission.
The repeated-index set is invariant under permutations.
Its coordinate projection commutes with \(\operatorname{Sym}\), which is an orthogonal projection and hence a Frobenius contraction.
Apply (Six-collision-bound) to the three terms in (Cross-tensor), followed by the finite-sum square inequality.
The facts
\[
 \|T_0\|_{\rm F}\le\|H_0\|_{\rm F},\qquad
 (T_0)_{ii}=(H_0)_{ii},\qquad
 \mathcal D(\mathsf E)
   =\sum_i\bigl(F_{ii}^2+(J_0)_{ii}^2+2(H_0)_{ii}^2\bigr)
\]
give (Repeated-index-error).
This step uses the physical diagonal-block energy, not just off-diagonal row spread.

For a four-element physical set \(\{i,j,k,l\}\), the coefficient of \(\varepsilon_i\varepsilon_j\varepsilon_k\varepsilon_l\) in \(s_4\) is exactly \(24\mathscr S_{ijkl}/N^2\).
Repeated-index monomials reduce to sign degree at most two and contribute no fourth coefficient.
Therefore
\[
 \sigma(s_4)^2
 :=\sum_{|I|=4}|(s_4)_I|^2
 =\frac{24}{N^4}\|\mathscr S_{\rm dist}\|_{\rm F}^2.
 \tag{Exact-cross-Walsh-energy}
\]
The factor is \(24\), because each unordered four-set occurs \(24\) times in the ordered tensor norm and its Walsh coefficient is multiplied by \(24\).
Combining the orthogonal decomposition of the tensor with (Actual-raw-coercivity) and (Repeated-index-error) yields
\[
 \frac{N^4}{24}\sigma(s_4)^2
 \ge
 (c_{\Lambda,g}-C\eta_*)\|\mathsf E\|_{\rm F}^2
       -C_{\Lambda,g}n-C\mathcal D(\mathsf E).
 \tag{Actual-cross-energy-inequality}
\]
In particular, for any deterministic sequence with the fixed coercivity hypotheses and
\[
 \frac{\|\mathsf E\|_{\rm F}^2}{n}\longrightarrow\infty,\qquad
 \eta_*\longrightarrow0,\qquad
 \frac{\mathcal D(\mathsf E)}{\|\mathsf E\|_{\rm F}^2}\longrightarrow0,
 \tag{Cross-energy-regularity}
\]
one has eventually
\[
 \sigma(s_4)^2
 \ge\frac{c_{\Lambda,g}\|\mathsf E\|_{\rm F}^2}{N^4}
 \ge\frac{c_{\Lambda,g}\mathcal R^2}{N^4},
 \tag{Actual-cross-noncollapse}
\]
after decreasing the positive constant.
The last inequality uses \(\mathcal R^2\le\|F\|_{\rm F}^2+\|J_0\|_{\rm F}^2+\|T_0\|_{\rm F}^2\le\|\mathsf E\|_{\rm F}^2\).
No ratio involving \(q\) is assumed.

<a id="actual-cross-energy-probability"></a>
#### The uniform closest-mode conclusion in the bounded input model

Return to the exact bounded real \(K=1\) model of [C_F0187_v4](Yin_C_F0187_v4.md#statement).
For its full pencil and single physical minors write \(n:=N-|S|\), \(|S|\le1\), retaining the original \(N^{-1/2}\) normalization in the sign coefficient calculation.
For general bounded off-diagonal laws, \(\sigma(s_4)\) here denotes the coefficient functional under the displayed formal sign substitution.
In the single-deletion case \(|S|=1\), it is the actual conditional fourth Walsh component of the cross polynomial when the exposed first input has the Rademacher law.
For \(S=\varnothing\), it is only a formal sign-probe functional with the original \(N\) normalization, not a border of the original \(N\)-dimensional matrix.
No reduction of other entry laws to Rademacher support is asserted.
For each invertible \(\mathcal M_{N,S}\), let \(\mathcal W_{N,S}\) consist of all real unit eigenvectors whose eigenvalues have smallest absolute value.
The assertions here are uniform over this entire set, including arbitrary unit choices in a repeated eigenspace.

The [auxiliary Gram argument](#gram-gap-proof) gives one fixed \(g>0\) for every eigenmode, on an event of probability tending to one.
The [fixed bounded-input norm event](Yin_C_F0187_v4.md#spectral-residual-spread) supplies a fixed \(\Lambda\) uniformly over these minors.
The [weighted minor mass](Yin_C_F0187_v4.md#weighted-minor-mass) at one sufficiently small fixed interval \([-\delta,\delta]\), with \(0<\delta<1\), ensures \(|\lambda|\le1\) for every closest mode, outside a set of probability tending to zero.
The [physical-projector conclusion](Yin_C_F0187_v4.md#statement) gives \(\eta_*\to0\) for all these closest modes, uniformly in the stated probability sense.

Finally, the same fixed proof's [residual divergence and physical diagonal energy](Yin_C_F0187_v4.md#spectral-residual-spread) assert
\[
 \|\mathsf E_w\|_{\rm F}^2/n\longrightarrow\infty,\qquad
 \mathcal D(\mathsf E_w)/\|\mathsf E_w\|_{\rm F}^2\longrightarrow0
\]
uniformly over all removed modes and these minors, as bad-event bounds intersected with invertibility.
These are actual established interfaces of that proof, beyond its off-diagonal row-spread statement alone.
Apply (Actual-cross-energy-inequality) on their intersection with the Gram and norm events.
There is a fixed \(c_*>0\) such that
\[
 \begin{split}
 \mathbb P\{\exists S,\ |S|\le1:\;&
 \mathcal M_{N,S}\text{ is invertible and }
 \exists w\in\mathcal W_{N,S}\\
 &\text{with }\ 
 \sigma(s_{4,w})^2<
       c_*\|\mathsf E_w\|_{\rm F}^2/N^4\}
 \longrightarrow0 .
 \end{split}
 \tag{Closest-mode-cross-energy-assembly}
\]
Writing \(\mathcal R_w:=\mathcal R(\mathsf E_w)\), the same conclusion follows with \(\mathcal R_w^2\) in place of the full residual squared norm on the right.
It does not divide by the probability of invertibility or condition on the whole second input.
There is no union over a chosen eigenbasis: all the deterministic estimates and the adopted input events hold uniformly in the mode.

This proves the new cross-energy bound at the stated bounded-model, closest-mode scope.
To distinguish it from the energy of the whole inverse quadratic determinant, put
\[
 e_4:=\Pi_4\bigl[(x^TFx)(x^TJ_0x)-(x^TT_0x)^2\bigr].
\]
For the full inverse blocks \(G=quu^T+F\), \(J=qvv^T+J_0\), and \(T=q(uv^T+vu^T)/2+T_0\), direct expansion gives
\[
 \Pi_4\bigl[(x^TGx)(x^TJx)-(x^TTx)^2\bigr]=q s_4+e_4.
 \tag{Full-fourth-decomposition}
\]
The \(q^2\) term vanishes identically.
The lower bound on \(s_4\) does not prevent cancellation in this sum.
Pole dominance, or another argument handling comparable inverse modes, remains separate from the present theorem.
No matrix-distance conversion, singular-minor estimate, unregularized logarithmic conclusion or extension to all original finite-second-moment laws is supplied here.


<a id="remaining-boundary"></a>
## Consequence and remaining boundary

For the actual bounded real pencil, auxiliary Gram degeneracy is excluded with probability tending to one uniformly over the full matrix and its single physical minors.
The actual inverse-block identities then give cross-layer coercivity for closest-to-zero modes, using the reviewed residual-divergence, leverage and physical diagonal-energy bounds.
The deterministic generic kernel explains why these actual identities are essential; it does not contradict the constrained result.
The full fourth-layer sum \(q s_4+e_4\) can still require a pole-dominance argument or a treatment of comparable inverse modes.
The singular branch, the matrix-distance normalization, bottom logarithmic control and extension to the full finite-second-moment contract remain unresolved by this version.

## Current assessment
[Selected decision](#decision-auxiliary-cross-energy-reviewed)

## Assessment history

### Decision auxiliary-gram-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T19:31 |
| status | open |
| reason | Complete fixed candidate for the independent-input approximate-mode gap, all-eigenmode auxiliary Gram separation and actual closest-mode cross-energy lower bound, with a deterministic generic kernel identifying the role of the actual inverse identities. Independent checking of the complete probability, tensor, repeated-index and source-interface chain remains required before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact probability conclusions and cancellation boundary](#statement) | Fixed bounded real inputs, original N normalization, all single physical minors, all-eigenmode Gram separation, invertible-branch closest-mode cross-energy and the separately defined generic kernel; actual sign-border interpretation only for one deletion and a Rademacher first input. |
| argument | [Complete fixed candidate](#argument) | Fixed-vector concentration, spectral-window nets, minor interlacing, Gram conversion, generic kernel, actual tensor coercivity, repeated-index control and the complete closest-mode probability assembly. |
| dependency | [Convex bounded-product concentration](Yin_C_F0187_v2.md#proof) | Equation (9), at its fixed bounded-coordinate and convex Lipschitz scope. |
| dependency | [Scalar semicircle weak convergence](Yin_C_F0186_v4.md#statement) | The first input's empirical spectral limit and the continuous bounded semicircle density. |
| dependency | [Bounded norm and spectral residual estimates](Yin_C_F0187_v4.md#spectral-residual-spread) | The bounded input-norm event, residual divergence and negligible physical diagonal-block energy, uniformly over all stated minors and removed modes on the invertible branch. |
| dependency | [Uniform minor mass and closest-mode leverage](Yin_C_F0187_v4.md#fresh-row-projector) | The fixed proof's weighted minor mass and physical-projector bounds ensure a small closest eigenvalue and vanishing physical leverage, uniformly over all choices in the closest eigenspaces. |

### Decision auxiliary-cross-energy-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T19:59 |
| status | proved |
| reason | The independent whole-proof finding checks the joint approximate-mode gap, all-eigenmode auxiliary Gram separation, actual residual tensor coercivity, repeated-index loss and complete closest-mode probability assembly, including every fixed input and the separately delimited generic kernel. This adopts the stated bounded-model cross-energy conclusion without assuming pole dominance; full fourth-layer cancellation, singular minors and the original logarithmic contracts remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact probability conclusions and cancellation boundary](#statement) | Fixed bounded real inputs, original N normalization, all single physical minors, all-eigenmode Gram separation, invertible-branch closest-mode cross-energy and the separately defined generic kernel; actual sign-border interpretation only for one deletion and a Rademacher first input. |
| argument | [Complete proof](#argument) | Fixed-vector concentration, spectral-window nets, minor interlacing, Gram conversion, generic kernel, actual tensor coercivity, repeated-index control and the complete closest-mode probability assembly. |
| dependency | [Convex bounded-product concentration](Yin_C_F0187_v2.md#proof) | Equation (9), at its fixed bounded-coordinate and convex Lipschitz scope. |
| dependency | [Scalar semicircle weak convergence](Yin_C_F0186_v4.md#statement) | The first input's empirical spectral limit and the continuous bounded semicircle density. |
| dependency | [Bounded norm and spectral residual estimates](Yin_C_F0187_v4.md#spectral-residual-spread) | The bounded input-norm event, residual divergence and negligible physical diagonal-block energy, uniformly over all stated minors and removed modes on the invertible branch. |
| dependency | [Uniform minor mass and closest-mode leverage](Yin_C_F0187_v4.md#fresh-row-projector) | The fixed proof's weighted minor mass and physical-projector bounds ensure a small closest eigenvalue and vanishing physical leverage, uniformly over all choices in the closest eigenspaces. |
| review | [Independent Gram and actual cross-energy whole-proof finding](../audits/reviews/Yin_R_F0191_v5.md#auxiliary-gram-and-actual-cross-energy) | Exact final statement, complete probability and deterministic arguments, all direct dependency interfaces, generic kernel, sign-border distinction, uniform invertible-branch scope and remaining full fourth-layer limitations. |

