---
author: Yin
---

# Singular-value counts for scalar word-chain pencils with finite-variance Wigner inputs

<a id="statement"></a>
## The original scalar model

Take the independent real symmetric or complex Hermitian Wigner colors of [F0013](../tasks/Yin_T_F0013_v1.md#input-model), allowing mixed colors, dependent real and imaginary parts of each complex upper entry, and arbitrary cross-size couplings.
The fixed upper laws have mean zero and absolute second moment one; the independent real diagonal laws have mean zero and finite second moments.
Fix a nonconstant scalar polynomial \(P\) in the selfadjoint indeterminates, a shift \(z\in\mathbb C\), and the [word-chain pencil](../ledger/Yin_L_F0061_v2.md#linearization-transfer) \(K(x)\) for \(P(x)-z\), of size \(m\).
Write \(\nu_N\) for the probability measure of all \(mN\) singular values of \(K(W)\), ordered with multiplicity.
There are \(C,\beta,\gamma>0\) depending only on the fixed data such that, in all sufficiently large dimensions,
\[
 \mathbb E\nu_N([0,t])\le Ct^\beta,\qquad N^{-\gamma}\le t\le1 .
 \tag{1}
\]
This count uses neither translation regularity nor a higher raw moment.

Suppose in addition that all raw laws enjoy the [translation bound (T)](Yin_C_F0186_v38.md#statement) in their declared real or complex coordinate spaces.
Let \(p=P(s)-z\) at a free standard semicircular tuple, \(u=\tau\log |p|\), and let \(\mathcal G_z\) be the dimensions admitting an invertible deterministic evaluation of \(P-z\) in the mixed input space.
Then
\[
 \frac1N\log|\det(P(W)-zI_N)|\ \longrightarrow\ u
 \quad\text{almost surely and in every finite }L^r,\quad 1\le r<\infty,
 \quad N\in\mathcal G_z .
 \tag{2}
\]
The almost-sure dimension limsup over all \(N\) equals \(u\).
All sufficiently large even dimensions are in \(\mathcal G_z\).
If \(z\ne P(0)\), all dimensions are good.
The limsup equality includes \(z=P(0)\) and gives [F0014](../tasks/Yin_T_F0014_v1.md#contract) throughout the translation-regular finite-variance submodel.
Constants have the expected deterministic answer with \(\log0=-\infty\).
For each fixed scalar polynomial, the eigenvalue probability measures converge weakly almost surely to its Brown measure under the same hypotheses.
The proof gives (1) for every fixed word-chain pencil.
For a general affine pencil the deterministic free singular-value estimate identified below is an additional input.

<a id="argument"></a>
<a id="bounded-core"></a>
## Conditional comparison for a general affine pencil

For any affine \(K\) of fixed size \(m\), let \(H= \left(\begin{smallmatrix}0&K\\K^*&0\end{smallmatrix}\right)=B_0+\sum_j B_jW_j\) denote its signed Hermitian dilation in the tensor notation, with fixed Hermitian coefficients of size \(p_0=2m\).
Write \(g(H)= (p_0N)^{-1}\operatorname{Tr}(it-H)^{-1}\) for \(0<t\le1\).
The conditional reductions here apply to this general dilation independently of the later word-chain application.

Choose a fixed radius in each upper law for which the event \(\{|\xi_j|\le K_j\}\) has probability \(p_j>0\) and its conditional centered variance \(v_j=\mathbb E(|\xi_j-\mu_j|^2\mid |\xi_j|\le K_j)\) is strictly positive, where \(\mu_j\) is its conditional mean.
Such a radius exists by nondegeneracy and convergence of the truncated first and second moments.
For each unordered pair draw the independent indicator \(\chi^j_{ab}\) of this event.
Expose every indicator, the upper values at the complementary pairs, and all the diagonals.
The original matrices have the form \(D_j+Y_j\), with \(D_j\) fixed under this exposure.
Its raw entries at active pairs are \(\mu_j\); the other entries are precisely the exposed values, and its normalized lower entries are conjugates.
The active upper entries of \(Y_j\) are independent centered copies of the bounded conditional law divided by \(\sqrt N\).
The other entries are zero.
There is a uniform bound \(\mathbb E\sum_j N^{-1}\|D_j\|_{\rm HS}^2\le C\) by the original second moments.

For \(M\ge1\) replace \(D_j\) by \(D_j^{(M)}=D_j{\bf1}_{[-M,M]}(D_j)\).
This costs expected normalized rank at most \(C/M^2\) in the pencil by the spectral theorem and bounded ranks of its coefficients.
By singular-value interlacing, the original expected count is at most the count after this replacement plus \(C/M^2\).
Even for real colors the comparison below will use physical GUE noise, while the final least-value estimate applies in the original mixed spaces.

Replace each bounded active entry of \(Y_j\) by a Gaussian with the same real covariance, keeping the conjugate below the diagonal.
The [third-order Taylor comparison](Yin_C_F0195_v1.md#derivative-bound) gives an error at most \(CN^{-1/2}t^{-4}\) in the conditional expectation of \(g\), uniformly over the exposed background, the masks and \(M\).
Indeed every raw third moment is uniformly bounded and the bound per physical pair is \(CN^{-5/2}t^{-4}\).
Denote the resulting centered Gaussian tuple by \(Z_j\).

<a id="covariance-mask"></a>
## Replacing the variance masks

Put \(c_j=\sqrt{p_jv_j}>0\); these constants are independent of dimension.
Compare \(Z_j\) to independent \(c_jG_j\), where \(G_j\) are standard normalized physical GUE matrices.
For off-diagonal pairs their raw variance difference is
\(\delta_{ab}=v_j(\chi^j_{ab}-p_j)\).
Using independent Gaussian interpolation and integration by parts, differentiate the expectation of \(g\) with respect to the covariance parameter as in [the physical-pair formula](Yin_C_F0195_v1.md#covariance-interpolation).
The integrand is one half the contraction of the raw covariance difference with the Hessian, divided by \(N\) for the raw normalization.
For \(a<b\), put \(X=E_{ab}\otimes B_j,\ Y=E_{ba}\otimes B_j\) in physical-block order and \(R=(it-H)^{-1}\) along the interpolation.
In the complexified directional Hessian the contraction before division by \(2N\) is
\[
 h_{ab}D_X^2g+\bar h_{ab}D_Y^2g+2\delta_{ab}D_XD_Yg ,
\]
where \(h_{ab}\) is the difference in raw pseudocovariances, of bounded modulus.
This follows by expanding the real and imaginary directions \(X+Y,i(X-Y)\), including when the real covariance is singular.
Each pseudocovariance term, summed over pairs with its bounded multiplier, is \(O(N^{-1}t^{-3})\) after the prefactor: use Cauchy--Schwarz on \(\|R_{ba}\|_{\rm HS}\|(R^2)_{ba}\|_{\rm HS}\) and \(\|R\|_{\rm HS}\le\sqrt{p_0N}/t,\ \|R^2\|_{\rm HS}\le\sqrt{p_0N}/t^2\).
The diagonal covariance difference gives the same \(O(N^{-1}t^{-3})\) by summing \(O(N)\) rank-\(p_0\) second derivatives.

For the mixed direction, cyclicity gives
\[
 D_XD_Y g=\frac1{p_0N}\operatorname{Tr}_{p_0}\big\{
 B_jR_{bb}B_j(R^2)_{aa}+B_jR_{aa}B_j(R^2)_{bb}\big\}.
\]
Let \(S=(\delta_{ab})\) be symmetric with zero diagonal.
Summing this part of the interpolated derivative amounts, up to fixed factors, to at most
\[
 N^{-2}\left|\sum_{a,b}S_{ab}\operatorname{Tr}_{p_0}
            (B_jR_{bb}B_j(R^2)_{aa})\right|
 \ \le\ C \|S\| N^{-1}t^{-3}.
\]
For each of the finitely many auxiliary matrix entries the two diagonal-block sequences have Euclidean norms at most \(C\sqrt N/t\) and \(C\sqrt N/t^2\).
This deterministic inequality applies to every realized interpolation resolvent, even when the drift depends on all the masks.
The original centered symmetric mask has \(\mathbb E\|S\|\le C\sqrt N\).
Indeed on any real unit vector its quadratic form is a sum of independent centered bounded variables with sum of squared coefficient bounds \(O(1)\).
Hoeffding's inequality, a fixed \(1/4\)-net of size at most \(9^N\), and integration above a sufficiently large multiple of \(\sqrt N\) give this expectation.
Integrate the interpolation and average the mask bound to obtain \(CN^{-1/2}t^{-3}\) in the expected trace resolvent, uniformly in \(M\).

<a id="free-background"></a>
## The Gaussian comparison with the frozen background

Conditional on the exposed background, the new model is the Hermitian Gaussian matrix with deterministic drift \(B_0\otimes I+\sum_j B_j\otimes D_j^{(M)}\) and independent noise \(\sum_j c_jB_j\otimes G_j\).
Use [Bandeira, Boedihardjo and van Handel, Theorem 2.8, author manuscript pp. 11–12](https://web.math.princeton.edu/~rvan/mconcfree-230228.pdf).
For a Hermitian Gaussian series \(A_0+\sum_l g_l U_l\) the norm distance of the expected resolvent and the matrix-valued free resolvent at \(itI\) is at most \(\sigma^2v^2t^{-5}\).
Here \(\sigma^2=\|\sum_l U_l^2\|\), \(v^2=\|\sum_l\operatorname{vec}(U_l)\operatorname{vec}(U_l)^*\|\), and \(\operatorname{vec}\) uses unnormalized Hilbert--Schmidt coordinates.
Its drift \(A_0\) is arbitrary and absent from this bound.
The [BBvH23 source notes](../audits/literature/BBvH23/Yin_U001.md#matrix-resolvent) record the Gaussian resolvent estimate used here.
We have checked the definitions and the stated Gaussian resolvent theorem, without re-auditing its original proof.

Represent the physical GUE as \(N^{-1/2}\sum_l g_lU_l^0\) in the Hermitian Hilbert--Schmidt orthonormal basis obtained from diagonal matrix units and the symmetric and antisymmetric parts of each off-diagonal pair.
It is also a complex orthonormal basis of \(M_N(\mathbb C)\), and \(N^{-1}\sum_l U_l^0 X U_l^0=\operatorname{tr}_N(X)I\).
The tensor coefficients of the dilation consequently satisfy \(\sigma^2\le\sum c_j^2\|B_j\|^2\) and \(v^2\le N^{-1}\sum c_j^2\|B_j\|_{\rm HS}^2\) by orthonormality in the physical factor.
The trace-resolvent comparison error is \(O(N^{-1}t^{-5})\).

In the normalized trace, the free comparison distribution is that of the same dilation evaluated at
\[
 X_j=D_j^{(M)}+c_js_j ,
\]
where the scalar semicircular family \(s\) is free from the algebra of the deterministic \(N\)-by-\(N\) matrices with its normalized trace.
Indeed the physical normalized sum of the free standard semicircular coordinates in this basis has matrix-valued covariance \(X\mapsto\operatorname{tr}_N(X)I\), with vanishing cross covariances between colors.
The matrix-valued semicircular Wick recursion with this covariance and deterministic matrix coefficients is exactly the scalar free-product Wick recursion for scalar semicirculars free from \(M_N\), by pairing two equal colors, taking the normalized trace of the enclosed matrix word and multiplying the remaining word.
Conditioning onto the auxiliary coefficient algebra leaves the trace-resolvent identity also for the Hermitian dilation.
The identity follows first for moments and then for resolvents by compact support at each fixed \(N,M\).

Write \(f_{D,M}(t)=\int t^2/(s^2+t^2)\,d\nu_{|K(X)|}(s)\) for this conditional free smoothed mass.
Multiplication of the trace-resolvent estimates by \(t\), with \(\nu([0,t])\le2\int t^2/(s^2+t^2)\,d\nu(s)\), gives the general affine bound
\[
 \mathbb E\nu_N([0,t])\le C\{M^{-2}+N^{-1/2}t^{-3}+N^{-1}t^{-4}
                               +\mathbb E f_{D,M}(t)\}.
 \tag{3}
\]
In particular a uniform free estimate \(f_{D,M}(t)\le C(1+M)^K t^\alpha\) for arbitrary bounded deterministic backgrounds in this realization suffices for a bound of the form (1), by taking \(M=t^{-\delta}\) for sufficiently small fixed \(\delta>0\).
We next prove that input for the word-chain pencil.

<a id="scalar-fisher"></a>
## Free regularity of the scalar polynomial and its pencil

In the trace free product each \(X_j=D_j^{(M)}+c_js_j\) has norm at most \(M+2\max_j c_j\).
The tuple has free Fisher information bounded by \(\sum_j c_j^{-2}\), independently of \(N,M,D\).
For a test word \(F\) in \(X\), semicircular integration by parts relative to the deterministic factor gives \(\tau(s_jF(X))=c_j(\tau\otimes\tau)((\partial_jF)(X))\).
This identity also follows directly by marking the \(s_j\) factor paired to the first letter in the joint Wick recursion.
The conditional expectation of \(s_j/c_j\) onto \(W^*(X)\) therefore gives a conjugate variable of squared \(L^2\) norm at most \(c_j^{-2}\).

Apply Banna and Mai, [Theorem 1.1(i), proof (3.10) and constant (3.12), arXiv v3 pp. 3, 13–14](https://arxiv.org/pdf/1809.11153v3), to \(Q=(P-z)^*(P-z)\).
This selfadjoint scalar polynomial has nonzero highest degree \(d=2\deg P\).
The spectral distribution function of \(Q(X)\) is Hölder continuous of exponent \(\alpha=2/(3(2^d-1))\).
Its constant is bounded by \(C(1+M)^h\) for some finite \(h\) depending on \(Q\).
Indeed take \(R=1+M+2\max c_j\) in (3.12) of the source: the polynomial norm \(\|Q\|_R\) lies between two fixed positive multiples of \(R^d\), and the leading weight \(\rho_R(Q)\) is bounded below by a positive constant since the largest leading coefficient of \(Q\) is nonzero.
Together with the Fisher bound this gives the claimed growth.
The [source inspection of the Hölder constant](../audits/literature/BM20/Yin_U001.md#finite-fisher-constant) records the formula and its applicability.
Thus the singular probability mass of \(P(X)-z\) below \(v\) is at most \(C(1+M)^hv^{2\alpha}\) for \(v>0\).

In the word-chain model \(K(X)\) is the product of two invertible triangular factors and \(\operatorname{diag}(P(X)-z,Q_{\rm aux}(X))\); the pivot \(Q_{\rm aux}\) is unit triangular with polynomial inverse.
The factors and their inverses as well as \(Q_{\rm aux}^{-1}\) have norms at most \(C(1+M)^l\) for some fixed \(l\), by [the exact Schur factorization](../ledger/Yin_L_F0061_v2.md#linearization-transfer).
Multiplication by these invertible factors enlarges the singular threshold for the middle block by at most the product of the inverse norms.
This is the singular-number variational inequality in a finite tracial algebra, obtained by transporting subspaces and using the polar decomposition to preserve their trace dimension.
At thresholds \(v\) with \(C(1+M)^{3l}v<1\), the auxiliary block therefore contributes no small mass.
The scalar bound gives \(\nu_{|K(X)|}([0,v])\le C(1+M)^{h'}v^{2\alpha}\) there for a fixed \(h'\).
After increasing \(h'\) and \(C\), the same right side dominates one whenever \(C(1+M)^{3l}v\ge1\), giving the bound throughout \(0<v\le1\).
In the smoothed mass split the integral at \(v=\sqrt t\); the part above this threshold is at most \(t\).
This proves \(f_{D,M}(t)\le C(1+M)^{h'}t^\alpha+t\).

Take \(M=t^{-\delta}\) with \(\delta>0\) small enough that \(\alpha-\delta h'>0\).
By (3) there is \(\beta>0\) for which the sum of the drift rank and free terms is \(O(t^\beta)\), uniformly on \(0<t\le1\).
Choose \(\gamma>0\) so small that \(\gamma(3+\beta)<1/2\) and \(\gamma(4+\beta)<1\).
This proves (1) on the full sequence for every fixed finite-variance model.

<a id="determinant"></a>
## Ordinary determinant and the scalar Brown law

The free scalar target is finite at each fixed \(z\), including \(P(0)\), by the scalar Hölder estimate itself with deterministic drift zero and all semicircular variances one.
The [word-chain identities](../ledger/Yin_L_F0061_v2.md#linearization-transfer) give the pencil target \(u/m\) and finite-dimensional ordinary scalar logarithm equal to \(m\) times the pencil logarithm, including exact zeros.
At each dimension \(\mathcal G_z\) is also the good set for the pencil, and [every sufficiently large even dimension is good](Yin_C_F0186_v9.md#all-even-witness).

For completeness take \(a_N=N^{-\gamma}\), reducing \(\gamma\) if necessary so \(2\gamma\beta<1\).
The expected negative log excess between a fixed clip \(d\in(0,1)\) and \(a_N\) is at most \(\int_{a_N}^d Ct^{\beta-1}dt\le Cd^\beta/\beta\) by (1).
Moreover \(\log(N+2)\,\mathbb E\nu_N([0,a_N])\to0\).
[Row-rank concentration](Yin_C_F0186_v4.md#row-concentration) applies in the original independent row groups: the centered negative log clipped at \(a_N\) and \(\log(N+2)\) times the centered count at \(a_N\) have summable tails \(2\exp(-cNx^2/\log^2(N+2))\) at each fixed deviation \(x>0\), and tend to zero in every finite \(L^r\) by tail integration.
The fixed-clip expectation converges by the weak singular law; sending \(d\downarrow0\) identifies the clipped negative limit.
On good sizes the remaining excess is bounded by
\[
 B\log(N+2)\,\nu_N([0,a_N])+\bigl(\log^-s_{\min}(K(W))-B\log(N+2)\bigr)_+ .
\]
In the original mixed-color model (T) gives the [polynomial least-value floor](Yin_C_F0186_v38.md#floor-statement), with tail \(CN^{5/2-Bc}e^{-cx}\) at extra depth \(x\).
Large \(B\) yields summability and convergence in all finite \(L^r\).
The positive log has the [pathwise limit and higher log moment bounds](Yin_C_F0186_v4.md#log-statistics).
Both log parts therefore converge in the asserted senses, and the exact scalar normalization proves (2).
The ordinary logarithm is identically \(-\infty\) on other sizes, so the good-size convergence and all-even witness give the full limsup.

At each \(z\ne P(0)\) the zero tuple witnesses every size.
For a fixed polynomial and coupling, Fubini gives one event of full-sequence pointwise convergence for planar almost every \(z\).
The [pathwise planar bounds and tightness](Yin_C_F0186_v4.md#noncompact-planar) give local \(L^1\) convergence of potentials and then weak convergence to the Brown measure by distributional Laplacians.
This step uses the full limit at each such fixed shift.

## Current assessment
[Selected decision](#decision-conditioned-core-reviewed)

## Assessment history

### Decision conditioned-core-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:15 |
| status | open |
| reason | The bounded conditional core compares to scalar semicircular noise free from a frozen background; the finite-Fisher estimate for the word-chain Schur complement closes its intermediate count. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Finite-variance counts and scalar limits](#statement) | All fixed scalar polynomials, every fixed shift, mixed spaces, the good dimensions and arbitrary coupling. |
| argument | [Conditional replacement](#argument) | Centered bounded coordinates and a frozen tail matrix with bounded mean normalized squared Hilbert--Schmidt norm. |
| support | [Covariance masks](#covariance-mask) | Uniform physical-block trace estimate after Gaussian interpolation. |
| support | [Free model](#free-background) | Arbitrary Gaussian drift and the scalar-free representation of physical GUE. |
| support | [Free polynomial regularity](#scalar-fisher) | Uniform free Fisher information, polynomial norm dependence and singular comparison through the Schur factors. |
| support | [Ordinary determinants](#determinant) | Removal of the last clip with (T) and the full local planar consequence. |

### Decision conditioned-core-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:25 |
| status | proved |
| reason | Independent whole-proof review and reinspection of the normalized GUE basis confirmed the conditional affine comparison, the scalar word-chain count and the ordinary limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Scalar word-chain results](#statement) | Finite-variance counts and the scalar determinant and Brown limits under translation regularity. |
| argument | [Complete comparison](#argument) | Bounded conditional entries, mask interpolation, scalar free bound and cutoff removal. |
| support | [Original random masks](#covariance-mask) | Drift-independent interpolation at fixed masks. |
| support | [Gaussian resolvents](#free-background) | Normalized physical covariance and scalar free comparison. |
| support | [Scalar-free estimate](#scalar-fisher) | Uniform free Fisher bound and polynomial growth of the Hölder constant. |
| support | [Ordinary logarithms](#determinant) | Every fixed shift and every permitted coupling. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0201_v4.md#conditioned-core-whole-proof) | Whole theorem and the rechecked normalization in the Gaussian comparison. |
