---
author: Yin
---

# Whole fourth-layer energy above a fixed effective inverse rank

This result continues the bounded actual-minor branch of the [matrix-coefficient F0013 contract](../tasks/Yin_T_F0013_v1.md#contract).
It bounds the complete fourth Walsh layer of the single-input Schur determinant when the full inverse has effective rank above a sufficiently large fixed threshold.
Actual inverse-block identities and the fixed independent-input approximate-mode gap force a positive six-Gram term; a rank-sensitive four-cycle error then controls full-layer cancellation.
The proof uses the fixed physical spread theorem to remove physical diagonals and obtain vanishing coordinate loads.
No probability lower bound for the effective-rank branch, invertibility assertion, or completion of the original determinant contract is included.

<a id="statement"></a>
## Exact bounded model and conclusion

For \(j=1,2\), let \(W_j^{(N)}\) be independent real symmetric Wigner matrices with independent upper off-diagonal entries distributed as \(\xi_j/\sqrt N\).
The fixed real laws satisfy \(\mathbb E\xi_j=0\), \(\mathbb E\xi_j^2=1\), and \(|\xi_j|\le L\).
The diagonal entries of input \(j\) are independent copies of \(\zeta_j/\sqrt N\), where \(\zeta_j\) is fixed, real, centered and bounded by \(L\).
Zero diagonal laws are allowed.
All raw upper-triangular coordinates and both inputs are independent within each size, while the cross-size coupling is arbitrary.
The finite constant \(L\) covers all four fixed laws.

For \(S\subset[N]\), \(|S|\le1\), put \(n:=N-|S|\), and let \(C_{N,S},D_{N,S}\) be the corresponding principal submatrices of the first and second inputs.
Their entries retain the original \(N^{-1/2}\) normalization.
Set
\[
 \alpha:=\sqrt2,\qquad X:=C_{N,S}+D_{N,S},\qquad
 Y:=C_{N,S}+\alpha D_{N,S},\qquad
 \mathcal M_{N,S}:=\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix}.
\]
On the invertible branch write
\[
 Z:=\mathcal M_{N,S}^{-1}
   =\begin{pmatrix}G&H\\H^T&J\end{pmatrix},\qquad
 T:=(H+H^T)/2,\qquad
 A_Z:=\|Z\|_{\rm F},\qquad r_Z:=A_Z^2/\|Z\|^2.
\]
The norm without subscript is the operator norm.
Define the raw homogeneous polynomial
\[
 h_Z(x):=(x^TGx)(x^TJx)-(x^TTx)^2.
\]
Substitute \(x_i=\varepsilon_i/\sqrt N\) and reduce every \(\varepsilon_i^2\) to one.
Let \(h_4:=\Pi_4h_Z\) be its degree-four multilinear sign component, and set
\[
 \sigma_4^2:=\sum_{|I|=4}|(h_4)_I|^2,\qquad
 L_i^{(4)}:=\sum_{\substack{|I|=4\\i\in I}}|(h_4)_I|^2,\qquad
 \tau_4:=\frac{\max_iL_i^{(4)}}{\sigma_4^2}
 \quad\text{when }\sigma_4>0.
\]
Distinct sign monomials are orthogonal, so these sums are their exact squared Walsh coefficient norms.

There are fixed constants \(r_*,c_*>0\), depending only on the fixed laws, such that
\[
 \mathbb P\{\exists S\subset[N],\ |S|\le1:\quad
  \mathcal M_{N,S}\text{ invertible},\ r_Z\ge r_*,\quad
  \sigma_4^2<c_*A_Z^4/N^4\}\longrightarrow0.
 \tag{High-rank-whole-layer-energy}
\]
For every fixed \(\varepsilon>0\), the same \(r_*\) also satisfies
\[
 \mathbb P\{\exists S\subset[N],\ |S|\le1:\quad
  \mathcal M_{N,S}\text{ invertible},\ r_Z\ge r_*,\quad
  [\,\sigma_4=0\text{ or }(\sigma_4>0\text{ and }\tau_4>\varepsilon)\,]\}
 \longrightarrow0.
 \tag{High-rank-whole-layer-load}
\]
These are unconditional bad-event statements intersected with the stated branch.
They do not divide by its probability and do not assert that it occurs with high probability.
The effective-rank threshold is fixed; divergence of \(r_Z\) is not assumed.

<a id="fresh-row-scope"></a>
### Complete-layer and actual fresh-row interpretation

For general bounded laws this is a formal sign coefficient functional.
Only for a single physical deletion and a Rademacher first off-diagonal law is it the actual conditional fourth Walsh layer of the original \(N\)-dimensional parent matrix's fresh first-input row.
Indeed, condition on the first-input minor and exposed diagonal, and on the whole second input.
After moving the exposed physical coordinate first, write the retained second-input border as \(b\) and the exposed diagonals as \(a,b_0\), and set \(u:=x+b,v:=x+\alpha b\).
The two-by-two Schur matrix is
\[
 \begin{pmatrix}
 a+b_0-u^TGu&1-u^THv\\
 1-u^THv&a+\alpha b_0-v^TJv
 \end{pmatrix}.
\]
Its determinant has raw fourth homogeneous part exactly \(h_Z(x)\); all other raw degrees are at most three.
Thus its complete fourth Walsh layer is \(h_4\), independently of \(a,b_0,b\).
This includes any cancellation between a removed-pole cross contribution and the residual fourth contribution.
For \(S=\varnothing\), the functional remains a formal sign probe and is not a fresh border of the original \(N\)-dimensional parent.
No assertion about the lower layers, exact singularity, or matrix-distance normalization follows from this identification alone.

<a id="inputs"></a>
## Fixed inputs and provenance

The [fixed joint approximate-mode theorem](Yin_C_F0187_v5.md#statement) supplies, for each fixed \(R>0\), a fixed \(\epsilon_R>0\) such that
\[
 \min_{|S|\le1}\Gamma_R(C_{N,S},D_{N,S})\ge\epsilon_R
\]
outside probability tending to zero, where
\[
 \Gamma_R(C,D):=
 \inf_{\substack{\|z\|=1,\ z\in\mathbb R^n\\a,b\in[-R,R]}}
 \max\{\|(C-aI)z\|,\|(D-bI)z\|\}.
\]
Only this approximate-mode conclusion from v5 is used; its auxiliary Gram and cross-energy conclusions are not needed to prove the present version.
The [fixed spectral residual proof](Yin_C_F0187_v4.md#spectral-residual-spread) supplies the uniform bounded norm event, residual Frobenius energy divided by \(n\) tending to infinity, vanishing normalized physical row energy, and negligible physical diagonal-block energy on the invertible branch.
Its [physical projector and closest-mode input](Yin_C_F0187_v4.md#fresh-row-projector), together with the weighted minor mass in that proof, supplies vanishing physical leverage for every closest-to-zero mode.
All these inputs apply to the exact bounded real laws, original normalization, and full or single-deletion minors stated above.
Their original independent reviews do not constitute a review of this new whole-layer deduction.

The extraction source is the [whole-layer development](../drafts/Yin_D_F0033.md#full-layer-high-effective-rank).
That rolling draft supplies provenance only; all new deterministic arguments are given below and all probabilistic inputs are the fixed versions just identified.
The argument uses direct finite-dimensional tensor expansion, Cauchy--Schwarz and the displayed inverse identities, without a new external theorem or novelty claim.

<a id="argument"></a>
## Complete proof

<a id="rank-refined-four-cycle-error"></a>
### Exact sign coefficients and a rank-sensitive six-Gram error

Put
\[
 A:=\operatorname{off}G,\qquad B_1:=\operatorname{off}J,\qquad
 C_1:=\operatorname{off}T,\qquad
 \kappa:=\max\{\|A\|,\|B_1\|,\|C_1\|\},
\]
\[
 B_\Sigma^2:=\|A\|_{\rm F}^2+\|B_1\|_{\rm F}^2+\|C_1\|_{\rm F}^2,
 \qquad
 \ell_i(U):=\sum_{j\ne i}|U_{ij}|^2.
\]
The off-diagonal operation is in the original independent-coordinate basis.
Use the real Frobenius inner product and define
\[
 \begin{split}
 \mathcal G:={}&\|A\|_{\rm F}^2\|B_1\|_{\rm F}^2
        +\langle A,B_1\rangle_{\rm F}^2+2\|C_1\|_{\rm F}^4\\
        &-4\langle A,C_1\rangle_{\rm F}\langle B_1,C_1\rangle_{\rm F}.
 \end{split}
\]
Then
\[
 \left|\sigma_4^2-\frac4{N^4}\mathcal G\right|
 \le\frac{C\kappa^2B_\Sigma^2}{N^4}.
 \tag{Rank-refined-fourth-Gram}
\]
Also
\[
 \mathcal G
 =2\left\|\frac{A\otimes B_1+B_1\otimes A}{2}
                    -C_1\otimes C_1\right\|_{\rm F}^2\ge0.
 \tag{Six-Gram-tensor}
\]
These tensor products use the real Hilbert space of symmetric matrices with its Frobenius inner product.

Here is a direct verification of the coefficient normalization and error.
Index unordered coordinate edges by \(e\), put \(a_e:=A_e,b_e:=(B_1)_e,c_e:=(C_1)_e\), and define
\[
 d_{ef}:=a_eb_f+a_fb_e-2c_ec_f.
\]
For a four-element set \(I\), let \(\Theta_I\) be the sum of \(d_{ef}\) over its three partitions into two unordered edges.
The raw product expansion gives
\[
 (h_4)_I=\frac4{N^2}\Theta_I,\qquad
 \sigma_4^2=\frac{16}{N^4}\sum_{|I|=4}\Theta_I^2.
 \tag{Exact-fourth-coefficients}
\]
No diagonal entry contributes to degree four on the sign support.
Expanding and summing over all ordered edges gives
\[
 \frac12\sum_{e,f}d_{ef}^2
 =\|a\|_2^2\|b\|_2^2+\langle a,b\rangle^2
      +2\|c\|_2^4-4\langle a,c\rangle\langle b,c\rangle
 =\mathcal G/4.
\]
Each off-diagonal entry is counted twice in a matrix Frobenius sum, giving the last factor.
Restricting this half-sum to disjoint edges gives exactly the sum of the three separate pairing squares in \(\sum_I\Theta_I^2\).
The removed shared-vertex contributions have total absolute value bounded by a fixed multiple of sums
\[
 \sum_i\ell_i(U)\ell_i(V)
 \le\kappa^2\|V\|_{\rm F}^2
 \le\kappa^2 B_\Sigma^2,\qquad U,V\in\{A,B_1,C_1\}.
\]
Every cross term between two different pairings of the same four vertices is a four-cycle.
Expanding the finitely many pairings and assignments expresses their total as a fixed linear combination of distinct-index sums
\[
 \sum_{i,j,k,l\ {\rm distinct}}U_{ij}V_{jk}W_{kl}(Z_1)_{li},
 \qquad U,V,W,Z_1\in\{A,B_1,C_1\}.
\]
The unrestricted sum is \(\operatorname{Tr}(UVWZ_1)\), whose absolute value is at most
\[
 \|UV\|_{\rm F}\|WZ_1\|_{\rm F}
 \le\kappa^2\|V\|_{\rm F}\|Z_1\|_{\rm F}
 \le\kappa^2 B_\Sigma^2.
\]
Adjacent vertex coincidences vanish because the matrices have zero diagonal.
For either opposite-vertex coincidence, the absolute sum is at most
\[
 \sum_i\sqrt{\ell_i(U)\ell_i(V)\ell_i(W)\ell_i(Z_1)}
 \le\kappa^2\sum_i\sqrt{\ell_i(W)\ell_i(Z_1)}
 \le\kappa^2 B_\Sigma^2.
\]
Their intersection satisfies the same bound, so excluding repeated vertices changes the cycle sum by at most a fixed multiple of that scale.
Therefore \(\sum_I\Theta_I^2=\mathcal G/4+O(\kappa^2B_\Sigma^2)\), proving (Rank-refined-fourth-Gram).
For an actual inverse, \(B_\Sigma^2\le A_Z^2\) and \(\kappa\le2\|Z\|\).
The error is consequently at most \(C\|Z\|^2A_Z^2/N^4\).

There is also a direct coordinate-load bound.
For \(E(U):=\sum_{a<b}|U_{ab}|^2\), the nine products in each \(\Theta_I\), the inequality \(|\sum_{j=1}^9z_j|^2\le9\sum_{j=1}^9|z_j|^2\), and summation over the edge containing \(i\) give
\[
 L_i^{(4)}\le\frac{C}{N^4}
   \{\ell_i(G)E(J)+\ell_i(J)E(G)+\ell_i(T)E(T)\}.
 \tag{Fourth-load}
\]
The fixed numerical constant absorbs the coefficients of the three \(TT\) products.
Discarding disjointness only increases the nonnegative sums.
If \(P_i\) is the rank-two projection onto physical coordinate \(i\) in both auxiliary channels and \(d_i(Z):=\|P_iZ\|_{\rm F}^2\), then
\[
 \ell_i(G),\ell_i(J),\ell_i(T)\le d_i(Z),\qquad
 E(G),E(J),E(T)\le A_Z^2/2.
\]
For \(T\), use \(|T_{ij}|^2\le(|H_{ij}|^2+|H_{ji}|^2)/2\).
Thus
\[
 L_i^{(4)}\le C A_Z^2d_i(Z)/N^4.
 \tag{Full-row-fourth-load}
\]

<a id="actual-six-gram-coercivity"></a>
### Joint mode separation forces the full six-Gram term

We next prove the deterministic coercivity needed for the probability statement.
Fix \(\Lambda\ge1\) and \(\epsilon>0\), suppose \(\|X\|,\|Y\|\le\Lambda\), and put
\[
 C:=\frac{\alpha X-Y}{\alpha-1},\qquad
 D:=\frac{Y-X}{\alpha-1},\qquad
 R_\Lambda:=\frac{2(\alpha+1)\Lambda}{\alpha-1}.
\]
Assume \(\Gamma_{R_\Lambda}(C,D)\ge\epsilon\), with \(\Gamma\) defined in the fixed joint-gap theorem.
There are constants \(L_*,d_*>0\), depending only on \(\Lambda,\epsilon\), such that an invertible actual pencil with \(A_Z^2\ge L_*n\) satisfies
\[
 \left\|\frac{G\otimes J+J\otimes G}{2}-T\otimes T\right\|_{\rm F}
 \ge d_* A_Z^2.
 \tag{Actual-six-Gram-coercivity}
\]
Here the tensor product is in the real Hilbert space of symmetric matrices with the Frobenius inner product; it is not matrix multiplication or the fully symmetrized four-coordinate tensor.
That distinction is essential, since four-cycle contractions can cancel this tensor's contribution when the effective inverse rank is small.

Set \(g:=\|G\|_{\rm F}\).
The identities \(H=I-GX\) and \(J=XGX-X\), obtained from the two products \(Z\mathcal M=\mathcal M Z=I\), give
\[
 A_Z\le B_\Lambda g+D_\Lambda\sqrt n,
 \qquad B_\Lambda:=1+\sqrt2\Lambda+\Lambda^2,
 \qquad D_\Lambda:=\sqrt2+\Lambda.
 \tag{Full-inverse-G-comparison}
\]
Consequently, if \(A_Z\ge2D_\Lambda\sqrt n\), then \(g\ge A_Z/(2B_\Lambda)>0\).
Define
\[
 F:=G/g,\qquad U:=(FX+XF)/2,\qquad V:=XFX,
 \qquad \delta:=\sqrt n/g,
\]
\[
 \mathscr K:=\frac{F\otimes V+V\otimes F}{2}-U\otimes U,
 \qquad k:=\|\mathscr K\|_{\rm F},\qquad c:=\langle F,U\rangle_{\rm F}.
\]
Then \(\|F\|_{\rm F}=1\), \(\|U\|_{\rm F}\le\Lambda\), and \(|c|\le\Lambda\).
Let \(P_F\) be the orthogonal projection in this matrix Hilbert space onto \(F^\perp\).
The double projection and the \(F\otimes F\) coefficient give
\[
 (P_F\otimes P_F)\mathscr K
 =-(U-cF)\otimes(U-cF),
 \qquad
 |\langle F,V\rangle_{\rm F}-c^2|\le k.
\]
In particular \(\|U-cF\|_{\rm F}^2\le k\).
The exact trace identity
\[
 \begin{split}
 \|(X-cI)F\|_{\rm F}^2
 &=2\|U\|_{\rm F}^2-\langle F,V\rangle_{\rm F}-c^2\\
 &=2\|U-cF\|_{\rm F}^2
      -(\langle F,V\rangle_{\rm F}-c^2)
 \le3k
 \end{split}
 \tag{Six-Gram-direction-control}
\]
uses \(2\|U\|_{\rm F}^2=\operatorname{Tr}(F^2X^2)+\operatorname{Tr}(FXFX)\) and \(c=\operatorname{Tr}(F^2X)\).
This estimate controls a direction defect directly and makes no positivity assumption on \(F\).

The other actual inverse-block identity is
\[
 (I-YX)G=-Y.
\]
It implies
\[
 \|(I-cY)F\|_{\rm F}
 \le\Lambda\sqrt{3k}+\Lambda\delta=:t_0.
 \tag{Six-Gram-second-direction}
\]
If \(t_0\le1/2\), then \(1=\|F\|_{\rm F}\le |c|\Lambda+t_0\), so \(|c|\ge(2\Lambda)^{-1}\).
In that case
\[
 \|(Y-c^{-1}I)F\|_{\rm F}\le2\Lambda t_0.
\]
Both proposed eigenvalue centers \(c,c^{-1}\) then lie in \([-2\Lambda,2\Lambda]\), and their corresponding \(C,D\) centers lie in \([-R_\Lambda,R_\Lambda]\).
Put \(L_\alpha:=(\alpha+1)/(\alpha-1)\).
For every real vector \(z\), conversion from the \(X,Y\) residuals to those of \(C,D\) bounds each converted residual by
\[
 L_\alpha\bigl(\|(X-cI)z\|^2+
                   \|(Y-c^{-1}I)z\|^2\bigr)^{1/2}.
\]
The assumed joint gap and homogeneity therefore give
\[
 \|(X-cI)z\|^2+\|(Y-c^{-1}I)z\|^2
 \ge(\epsilon/L_\alpha)^2\|z\|^2.
\]
Apply this to every column of \(F\) and sum, obtaining
\[
 3k+4\Lambda^2t_0^2\ge(\epsilon/L_\alpha)^2.
 \tag{Six-Gram-joint-gap-contradiction}
\]
Choose a fixed small \(k_0>0\), and then a fixed small \(\delta_0>0\), so that \(k\le k_0,\delta\le\delta_0\) would give \(t_0\le1/2\) and make the left side strictly smaller than the right side.
It follows that \(k>k_0\) whenever \(\delta\le\delta_0\).

The normalized tensor in (Actual-six-Gram-coercivity) differs from \(\mathscr K\) only through the terms \(J/g=V-X/g\) and \(T/g=-U+I/g\).
Its difference in Frobenius norm is at most
\[
 3\Lambda\delta+\delta^2.
\]
Decrease \(\delta_0\) further to make this at most \(k_0/2\).
Then the unnormalized tensor has norm at least \((k_0/2)g^2\ge k_0A_Z^2/(8B_\Lambda^2)\).
Choose \(L_*\) large enough that (Full-inverse-G-comparison) implies \(\delta\le\delta_0\), and put \(d_*:=k_0/(8B_\Lambda^2)\).
This proves (Actual-six-Gram-coercivity), with constants chosen before the dimension or the inverse.

<a id="whole-layer-physical-transfer"></a>
### Physical diagonal removal and the uniform probability statement

For the rank-two physical coordinate projections \(P_i\) defined above, put
\[
 \mathcal D(Z):=\sum_i\|P_iZP_i\|_{\rm F}^2,
 \qquad d_i(Z):=\|P_iZ\|_{\rm F}^2.
\]
Removing the diagonals of \(G,J,T\) changes each matrix by a Frobenius norm at most \(\sqrt{\mathcal D(Z)}\).
Their full and off-diagonal Frobenius norms are at most \(A_Z\), so the two-factor tensor changes by at most \(4A_Z\sqrt{\mathcal D(Z)}\).
Thus, if \(\mathcal D(Z)/A_Z^2\le(d_*/8)^2\), (Actual-six-Gram-coercivity) gives
\[
 \mathcal G
 =2\left\|\frac{A\otimes B_1+B_1\otimes A}{2}
                  -C_1\otimes C_1\right\|_{\rm F}^2
 \ge\frac{d_*^2}{2}A_Z^4.
 \tag{Actual-offdiagonal-six-Gram}
\]
Combining this with (Rank-refined-fourth-Gram) yields
\[
 \sigma_4^2
 \ge\frac{1}{N^4}
       \left(2d_*^2 A_Z^4-C\|Z\|^2A_Z^2\right).
\]
Choose once and for all \(r_*\ge C/d_*^2\).
Then \(r_Z\ge r_*\) gives \(\sigma_4^2\ge d_*^2 A_Z^4/N^4\).

The fixed [physical and residual spread proof](Yin_C_F0187_v4.md#spectral-residual-spread) supplies the remaining premises uniformly on actual invertible minors.
To check their transfer to the full inverse, choose any closest-to-zero unit mode \(w=(u,v)\) with eigenvalue \(\lambda\), and set \(q:=\lambda^{-1}\), \(\mathsf E_w:=Z-qww^T\), and \(\eta_i(w):=u_i^2+v_i^2\).
The fixed theorem gives \(\|\mathsf E_w\|_{\rm F}^2/n\to\infty\), negligible physical diagonal energy, and vanishing normalized maximum physical row energy, while its [closest-mode estimate](Yin_C_F0187_v4.md#fresh-row-projector) gives \(\eta_*:=\max_i\eta_i(w)\to0\).
Since \(\mathsf E_ww=0\), spectral orthogonality gives
\[
 A_Z^2=q^2+\|\mathsf E_w\|_{\rm F}^2,\qquad
 d_i(Z)=q^2\eta_i(w)+d_i(\mathsf E_w).
\]
Moreover,
\[
 \mathcal D(Z)\le2\mathcal D(\mathsf E_w)
                    +2q^2\sum_i\eta_i(w)^2
 \le2\mathcal D(\mathsf E_w)+2q^2\eta_*.
\]
Consequently, with the uniform unconditional invertible-branch meaning of the fixed input,
\[
 \frac{A_Z^2}{n}\longrightarrow\infty,\qquad
 \frac{\mathcal D(Z)}{A_Z^2}\longrightarrow0,\qquad
 \frac{\max_i d_i(Z)}{A_Z^2}\longrightarrow0.
 \tag{Full-inverse-physical-spread}
\]
No inverse-norm bound or lower bound on the invertibility probability is used in these deductions.
The fixed norm event chooses \(\Lambda\); next choose \(R_\Lambda\) and use C187v5's joint-gap theorem to choose \(\epsilon\).
Then choose the deterministic constants above in their stated order.
All premises except \(r_Z\ge r_*\) hold simultaneously for the stated minors outside probability tending to zero.
This proves (High-rank-whole-layer-energy).

Finally (Fourth-load) and \(\ell_i(G),\ell_i(J),\ell_i(T)\le d_i(Z)\) give
\[
 L_i^{(4)}\le\frac{C A_Z^2d_i(Z)}{N^4},\qquad
 \tau_4\le C_{\Lambda,\epsilon}
          \frac{\max_i d_i(Z)}{A_Z^2}
\]
on the displayed energy branch.
The last part of (Full-inverse-physical-spread) proves (High-rank-whole-layer-load).
In particular a fixed large effective-rank threshold suffices: load decay comes from the actual coordinate spread, not from sending that threshold to infinity.

<a id="remaining-boundary"></a>
## Scope left unresolved

The theorem controls the complete fourth layer on the branch \(r_Z\ge r_*\).
It does not prove that this branch has a probability sufficient for any determinant or logarithmic conclusion.
The complementary region includes bounded effective rank with no adequate pole-to-residual dominance.
Bounded effective rank does not by itself give approximation in relative Frobenius norm by a fixed number of eigenmodes.
For example, diagonal matrices with eigenvalues \(1,n^{-1/2},\ldots,n^{-1/2}\) have effective rank tending to two, while every fixed-rank spectral truncation leaves squared Frobenius tail tending to one.
This example concerns that general inference and is not asserted to be an actual pencil.

The low-effective-rank fourth tensor may have four-cycle contractions as large as its six-Gram term.
The present argument gives no estimate for that cancellation.
The fixed closest-mode cross-energy theorem remains available at its own scope, but its lower bound alone does not control the sum of the cross and residual fourth terms.
Singular minors, conversion to matrix-distance bounds, bottom logarithmic estimates, general coefficient tuples, and the original finite-second-moment laws remain outside this result.

## Current assessment
[Selected decision](#decision-whole-layer-rank-reviewed)

## Assessment history

### Decision whole-layer-rank-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T20:16 |
| status | open |
| reason | Complete candidate for whole fourth-layer energy and vanishing coordinate loads above a fixed effective inverse-rank threshold, uniformly on full and single-deletion bounded real pencils intersected with invertibility. Independent checking of the six-Gram normalization, rank-sensitive four-cycle bound, actual-identity coercivity, physical transfer and probability quantifiers remains required before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact whole-layer conclusion](#statement) | Fixed bounded real laws, original N normalization, all full and single-deletion minors, full fourth Walsh energy and load on a fixed effective-rank branch; actual fresh sign border only for one deletion and a Rademacher first input. |
| argument | [Complete candidate argument](#argument) | Exact sign coefficients, six-Gram expansion with rank-sensitive error, actual inverse coercivity, physical diagonal removal and uniform probability/load assembly. |
| dependency | [Joint approximate-mode gap](Yin_C_F0187_v5.md#statement) | The simultaneous fixed-center-range gap for both independent inputs and all stated physical minors; no auxiliary Gram or cross-energy conclusion from that version is needed. |
| dependency | [Norm and spectral residual bounds](Yin_C_F0187_v4.md#spectral-residual-spread) | Uniform bounded input norms, residual energy divided by n tending to infinity, physical row spread and negligible physical diagonal-block energy on the invertible branch. |
| dependency | [Closest-mode physical leverage](Yin_C_F0187_v4.md#fresh-row-projector) | Weighted minor mass and physical projector control give a closest eigenvalue tending to zero and vanishing physical leverage, uniformly over all stated minors and eigenspace choices. |

### Decision whole-layer-rank-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T20:26 |
| status | proved |
| reason | The independent whole-proof finding checks the exact full fourth-layer coefficients, rank-sensitive four-cycle error, actual inverse coercivity, physical diagonal removal and uniform energy/load assembly with all three fixed dependency interfaces. This adopts the bounded real fixed-effective-rank branch; its probability, the low-rank complement, singular minors and the original logarithmic contracts remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact whole-layer conclusion](#statement) | Fixed bounded real laws, original N normalization, all full and single-deletion minors, full fourth Walsh energy and load on a fixed effective-rank branch; actual fresh sign border only for one deletion and a Rademacher first input. |
| argument | [Complete proof](#argument) | Exact sign coefficients, six-Gram expansion with rank-sensitive error, actual inverse coercivity, physical diagonal removal and uniform probability/load assembly. |
| dependency | [Joint approximate-mode gap](Yin_C_F0187_v5.md#statement) | The simultaneous fixed-center-range gap for both independent inputs and all stated physical minors; no auxiliary Gram or cross-energy conclusion from that version is needed. |
| dependency | [Norm and spectral residual bounds](Yin_C_F0187_v4.md#spectral-residual-spread) | Uniform bounded input norms, residual energy divided by n tending to infinity, physical row spread and negligible physical diagonal-block energy on the invertible branch. |
| dependency | [Closest-mode physical leverage](Yin_C_F0187_v4.md#fresh-row-projector) | Weighted minor mass and physical projector control give a closest eigenvalue tending to zero and vanishing physical leverage, uniformly over all stated minors and eigenspace choices. |
| review | [Independent complete fourth-layer review](../audits/reviews/Yin_R_F0191_v6.md#whole-layer-fixed-rank) | Complete statement, fresh-row scope, deterministic proof and every direct dependency interface, including the fixed rank threshold and unconditional uniform invertible-branch probability interpretation. |

