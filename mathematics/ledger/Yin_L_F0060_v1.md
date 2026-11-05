---
author: Yin
---

# Affine determinant formulas: finite-GUE comparison barriers and one-sided targets

Date and owner: 2026-11-04T17:20 UTC, Yin.
The following exact comparison tests and source boundaries were retained from the parallel determinant investigation.

<a id="comparison"></a>
For [F0012](../tasks/Yin_T_F0012_v1.md#contract), the local affine formulas identify the exact free target but do not supply a lower bound for the finite-GUE expected logarithmic determinant.
An asymptotically sharp lower bound for that expectation would suffice, without a separate concentration theorem for the unregularized determinant.
The finite-dimensional versions of both the capacity lower bound and the monotonicity in the deterministic mean fail in explicit examples below.
These failures concern proposed comparison mechanisms, not F0012 or an eventual large-N comparison.
Within the expectation-comparison approach, a sharp fractional inverse-determinant estimate remains a separate quantitative target, rather than the expectation of a positive determinant power.
This is retained development and source comparison by Yin's agents, not a formal proof review or a claim of general finite-GUE convergence.
The general probability limit is established separately in [C_F0186_v2](../claims/Yin_C_F0186_v2.md#statement), including arbitrary constant matrices and a zero limiting determinant.
That proof does not assert convergence of logarithmic expectations or establish the proposed fractional inverse-determinant bound; the finite-dimensional counterexamples below remain valid.
The later [C_F0186_v3 strengthening](../claims/Yin_C_F0186_v3.md#statement) proves almost-sure logarithmic convergence and, for finite free logarithm, convergence in \(L^1\) and of expectations, by a global integrable singular-value tail.
It therefore supplies the finite-limit mean premise (5) below, while the proposed sharp fractional inverse-determinant bound remains unproved and unnecessary for these convergence conclusions.

## Exact reused formulas and their limits

Write
\[
 T=a_0+\sum_{j=1}^d a_js_j,\qquad
 L_N=a_0\otimes I_N+\sum_{j=1}^d a_j\otimes H_j^{(N)},
 \qquad a_j\in M_m(\mathbb C).
\]
The coefficient dimension m is fixed and the GUE matrices have the normalization in the Task.
The normalizations relevant here are
\[
 u=\log\Delta(T),\quad
 U_N=\frac1{mN}\log|\det L_N|,\quad
 U_{N,\varepsilon}=\frac1{2mN}\log\det(L_N^*L_N+\varepsilon^2I).
\]
All statements below can be applied separately at a spectral shift, by replacing the deterministic coefficient with the actual shifted coefficient of the chosen linearization.
They do not claim uniformity in that shift.

[C_F0124, Sections 1--3](../claims/Yin_C_F0124_v1.md#1-exact-formula-and-freely-variable-domain) gives, for selfadjoint coefficients and \(\eta(X)=\sum_j a_jXa_j\),
\[
 u=\inf_{b>0,\,\mathcal C_b-\eta\succ0}
 \left\{-\frac12+\operatorname{tr}_m\log b
 +\frac12\langle a_0,(\mathcal C_b+\eta)^{-1}a_0\rangle_2\right\}.
 \tag{1}
\]
The strict inequality is Hilbert--Schmidt positivity of a linear map, not positivity preservation.
Every trial value is an upper bound for u.
The reverse inequality is obtained from the *free* physical resolvent and its Dyson identity.
It is not a comparison with the finite random resolvent.
Its current [R_F0178 finding](../audits/reviews/Yin_R_F0178_v1.md#affine-infimum-whole-proof) is an independent whole-proof finding at the disclosed accepted-source boundary.

For arbitrary complex coefficients, [C_F0126](../claims/Yin_C_F0126_v1.md#setting-and-primary-unregularized-formula) uses
\[
 \eta(R)=\sum_j a_jRa_j^*,\quad \rho(Y)=\sum_j a_jYa_j,
 \quad H_R=I+\eta(R),\quad
 \mathcal T_R(Y)=H_RYR^{-1}+\rho(Y^*).
\]
It proves
\[
 u=\frac1{2m}\inf_{R>0}
 \left[\log\det H_R-\log\det R-m
 +\operatorname{Re}\operatorname{Tr}(a_0^*\mathcal T_R^{-1}a_0)\right].
 \tag{2}
\]
The inverse is real linear and its quadratic energy is nonnegative.
The unrestricted positive variable, the order of any inner maximization, and the possible nonattainment are essential.
The [regularized minimum](../claims/Yin_C_F0126_v1.md#regularized-minimum-used-in-the-proof) has the unique *free* optimizer \(Q_0=\varepsilon^2 E[(T^*T+\varepsilon^2I)^{-1}]\).
Its selected reviews are the disclosed signed-Schur and determinant-presentation self-reviews, not the independent R_F0178 finding on C_F0124.

[C_F0164](../claims/Yin_C_F0164_v1.md#statement) and [C_F0165](../claims/Yin_C_F0165_v1.md#statement) reparametrize the admissible cone and the complex inner problem.
They add no finite-GUE comparison.
[C_F0166](../claims/Yin_C_F0166_v1.md#statement) rules out discarding the phase-sensitive pseudo-covariance term and rules out an unrestricted joint matrix maximum.
[C_F0167](../claims/Yin_C_F0167_v1.md#statement) gives an independent circular signed-Schur minimum with positive regularization; circularity and the ordered extrema cannot be removed.
[C_F0168](../claims/Yin_C_F0168_v1.md#statement) gives a circular infimal convolution only under strictly Hilbert--Schmidt-positive covariance and an explicit obstruction to using the raw positive/negative covariance eigenspaces as saddle directions.
The actual review scopes of these five materials are the [self-reviewed bindings in R_F0175_v2](../audits/reviews/Yin_R_F0175_v2.md#review-bindings).

[C_F0172](../claims/Yin_C_F0172_v1.md#1-the-deterministic-mean-cannot-lower-the-determinant-below-the-centered-value) derives from (2)
\[
 u(a_0)\ge c_\eta:=-\frac12+\frac1{2m}\log\operatorname{cap}(\eta),
 \qquad
 t\longmapsto u(\sqrt t\,a_0)\text{ nondecreasing and concave}.
 \tag{3}
\]
This is a statement about the free determinant.
[C_F0171](../claims/Yin_C_F0171_v1.md#6-all-possible-brown-atoms-lie-among-the-deterministic-mean-eigenvalues) also proves finite free potential whenever the deterministic coefficient is invertible.
The R_F0177 [review bindings](../audits/reviews/Yin_R_F0177_v1.md#review-bindings) are self-reviewed and preserve the distinction between free singular-value kernel mass, Brown atoms, spectral support and positive-regularizer identities.
None supplies finite-N logarithmic uniform integrability.

## A mean lower bound would close the comparison

Here is a direct conditional reduction that isolates exactly the needed direction.
Assume \(u> -\infty\), \(U_N\) is integrable, and for each fixed \(\varepsilon>0\),
\[
 U_{N,\varepsilon}\longrightarrow u_\varepsilon
 \quad\text{in probability and in }L^1,
 \qquad u_\varepsilon\downarrow u.
 \tag{4}
\]
If
\[
 \liminf_{N\to\infty}\mathbb E U_N\ge u,
 \tag{5}
\]
then \(U_N\to u\) in probability.
Indeed, \(D_{N,\varepsilon}:=U_{N,\varepsilon}-U_N\ge0\), and
\[
 \limsup_N\mathbb E D_{N,\varepsilon}
 \le u_\varepsilon-u.
 \tag{6}
\]
Markov's inequality controls the nonnegative difference, while (4) controls the regularized part.
First taking N to infinity and then \(\varepsilon\downarrow0\) proves the assertion.
For the upper deviation one can directly use \(U_N\le U_{N,\varepsilon}\).
This argument needs no separate variance estimate for \(U_N\).
In the fixed-coefficient GUE setting, positive Gaussian norm moments make the fixed-regularizer moment convergence available; the genuinely missing assertion is (5).

A uniform bound \(\mathbb E U_N\ge c_\eta-o(1)\) would only replace the right side of (6) by \(u_\varepsilon-c_\eta\).
That need not vanish.
For instance, a nonzero real shift in the bulk of a scalar semicircle has potential \(-1/2+x^2/4>-1/2\).
Thus even a finite-GUE version of the constant capacity bound alone would not close the affine problem.

## Why deterministic trials and Jensen do not give (5)

For every positive definite k-by-k matrix B,
\[
 \log\det B=\inf_{Q>0}\{\operatorname{Tr}(BQ)-\log\det Q-k\}.
 \tag{7}
\]
This follows by diagonalizing \(B^{1/2}QB^{1/2}\) and using \(x-\log x-1\ge0\), with equality at \(Q=B^{-1}\).
Consequently, restricting random optimizers to deterministic trials and then taking expectation gives
\[
 \mathbb E\log\det B_N
 \le\inf_{Q>0}\{\operatorname{Tr}((\mathbb EB_N)Q)-\log\det Q-k\}
 =\log\det\mathbb EB_N.
 \tag{8}
\]
This is the upper direction.
It cannot be reversed by the free formula (1) or (2).
The free physical optimizer is constructed from the limiting operator and does not make the finite-N entropy loss disappear.
Likewise, positive determinant moments yield \(\mathbb E\log D\le p^{-1}\log\mathbb ED^p\), again the upper direction.

Replacing the finite Gaussian integration-by-parts identity by the exact free Dyson equation introduces resolvent fluctuation errors.
Bounds with powers of \(\varepsilon^{-1}\) prove fixed-positive-regularizer comparisons and possibly a mesoscopic cutoff.
They cannot be integrated to zero without a new integrable bound on those errors or on the small-singular-value contribution.
Writing the known free value as an unrestricted infimum does not itself provide either bound.

## A capacity lower bound fails at finite Gaussian size

Take m=3, N=1 and the three integer coefficient matrices
\[
 A_1=E_{12}-E_{21},\quad A_2=E_{13}-E_{31},\quad
 A_3=E_{23}-E_{32}.
\]
For independent real standard Gaussians \(g_1,g_2,g_3\), the matrix
\(M=\sum_j A_jg_j\) is antisymmetric of odd size, so \(\det M=0\) identically.
On the other hand,
\[
 \eta(X)=\sum_j A_jXA_j^*=\operatorname{Tr}(X)I-X^{\mathsf T}.
\]
If X has positive eigenvalues \(x_1,x_2,x_3\),
\[
 \frac{\det\eta(X)}{\det X}
 =\frac{(x_1+x_2)(x_1+x_3)(x_2+x_3)}{x_1x_2x_3}\ge8,
\]
with equality at X=I.
Thus \(\operatorname{cap}(\eta)=8\), and the local centered capacity formula gives
\[
 \log\Delta\left(\sum_j A_js_j\right)=\frac{\log2-1}{2}>-\infty.
\]
There is no all-size inequality comparing the Gaussian expected logarithmic determinant from below by the free capacity value with a finite additive error.
Multiplying every coefficient by i also gives a selfadjoint-coefficient version of this obstruction.
The example uses N=1 and does not exclude eventual invertibility or an asymptotically vanishing comparison error as N tends to infinity with m fixed.

## Deterministic-mean monotonicity and concavity also fail at finite size

This counterexample has a finite centered expected logarithmic determinant.
Put m=2, N=1,
\[
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
 Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 M_t=g_1 I+g_2J+tZ,
\]
with independent real standard Gaussians and real \(t\ge0\).
Direct multiplication gives
\[
 \det M_t=g_1^2+g_2^2-t^2.
 \tag{9}
\]
The random variable \(Y=(g_1^2+g_2^2)/2\) has density \(e^{-y}1_{y>0}\).
Writing \(r=t^2/2\) and \(I(r)=\int_0^\infty e^{-y}\log|y-r|\,dy\),
\[
 \mathbb E\frac12\log|\det M_t|
 =\frac12\bigl[\log2+I(r)\bigr].
 \tag{10}
\]
The two sides of the logarithmic singularity are integrable.
Splitting the integral at r and changing variables gives the exact identity
\[
 I(r)=e^{-r}\left[-\gamma+\int_0^r e^v\log v\,dv\right]
 =\log r-e^{-r}\operatorname{Ei}(r),\quad r>0,
 \qquad I(0)=-\gamma.
 \tag{11}
\]
Here the exponential-integral convention and series are [DLMF 6.2.5](https://dlmf.nist.gov/6.2#E5) and [DLMF 6.6.1](https://dlmf.nist.gov/6.6#E1), checked directly in this exploration.
The first integral identity in (11) also justifies differentiation without differentiating across an unresolved principal-value singularity.
It gives
\[
 I'(r)=e^{-r}\operatorname{Ei}(r),\qquad
 I''(r)=\frac1r-e^{-r}\operatorname{Ei}(r).
 \tag{12}
\]
For \(0<r\le e^{-2}\), the series implies
\[
 \operatorname{Ei}(r)=\gamma+\log r+
   \sum_{k\ge1}\frac{r^k}{k\,k!}
 \le\gamma-2+e^r-1<0.
\]
The last inequality uses \(\gamma<1\) and \(e^{e^{-2}}<2\).
Hence (10) strictly decreases as the squared deterministic mean increases from zero, and it is strictly convex on this interval.
Both finite-size analogues of the monotonicity and concavity in (3) fail.
This is an ordinary direct check of a proposed extension, not a correction to C_F0172.

There is a useful structural control at general N.
A constant unitary diagonalizes J to \(\operatorname{diag}(i,-i)\), while Z becomes an off-diagonal unitary involution whose phase can be removed by a diagonal unitary.
With \(G=(H_1+iH_2)/\sqrt2\), the pencil is therefore unitarily equivalent to
\[
 \begin{pmatrix}\sqrt2G&tI\\tI&\sqrt2G^*\end{pmatrix}.
\]
Its determinant equals \(\det(2G^*G-t^2I)\), first by the Schur complement when G is invertible, and then by polynomial continuity.
Thus this example reduces to a selfadjoint squared-singular-value logarithmic potential.
The N=1 obstruction supplies no negative large-N conclusion.
It does identify a microscopic finite-size defect that any proposed monotone interpolation must retain or estimate.

## A distinct candidate: fractional inverse determinants

The target value u in (2) could be used in an asymptotically sharp inverse-determinant estimate.
For example, for some fixed \(\theta>0\), suppose one can prove
\[
 \mathbb E|\det L_N|^{-\theta}
 \le \exp\{-\theta mN(u-e_N)\},\qquad e_N\longrightarrow0.
 \tag{13}
\]
This is an unproved candidate, not a consequence of capacity or the local variational formulas.
Jensen applied to \(e^{-\theta mN U_N}\) would immediately imply (5).
It would also give the one-sided estimate
\[
 \mathbb P\{U_N\le u-\delta\}
 \le \exp\{-\theta mN(\delta-e_N)\}.
 \tag{14}
\]
The new target controls the product of singular values directly and need not establish a polynomial lower bound for the smallest one.
It may still fail at a proposed exponent because of structural multiplicities, so the first discriminating check is uniform integrability of a sufficiently small negative determinant power for the actual coefficient family and fixed shift.
An integer replica or bosonic formula at positive regularization does not justify analytic continuation in the power or removal of regularization.
The odd antisymmetric example shows why a claim covering every N is too strong even for positive capacity.
The nonzero deterministic coefficient of a monic pencil removes that particular identically-zero polynomial obstruction, but does not establish a sharp negative-moment estimate.

## Source relation and actual search boundary

The search on 2026-11-05 was triggered by the proposed use of a free capacity formula as a finite-Gaussian determinant estimate.
Queries combined Gaussian expected log determinant, operator capacity, noncommutative rank, and negative determinant moments.
The relevant primary finding is [Mai--Speicher, arXiv:2406.15922v1, Section 5, Conjecture 1, PDF p. 17](https://arxiv.org/pdf/2406.15922v1#page=17).
It explicitly conjectures eventual invertibility and convergence of \(\Delta(\sum_j a_j\otimes H_j^{(N)})\) to \(e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)}\), both almost surely and in expectation, for integer coefficients with rank-nondecreasing covariance.
This is a conjecture, not a random-matrix theorem supplied by the capacity identity.
Its expectation statement concerns \(\Delta\), not \(\log\Delta\).

The relationship with the proposed F0012 pencil mechanism is not direct inclusion in either direction.
The cited conjecture is centered and at the fixed shift zero, whereas the monic route has an invertible deterministic coefficient and generally arbitrary complex coefficients depending on the chosen shift.
Adding another GUE variable does not replace a deterministic identity coefficient.
Conversely, an almost-everywhere shifted-potential result cannot simply be specialized to the possibly exceptional point zero.
A sufficiently general affine logarithmic-determinant theorem would resolve the centered conjecture at its applicable full-rank scopes, but that theorem is precisely additional mathematics.

The main agent also directly inspected [Kargin, arXiv:2610.15180v1](https://arxiv.org/abs/2610.15180), its abstract and Section 12, including the random-matrix discussion and unconstrained-formula comparison.
That discussion explicitly retains the small-singular-value difficulty and formulates a shifted random-matrix analogue as a question.
This comparison relies on the local fixed formulas, not an adoption of that preprint's nonstrict-domain formulation or a whole-source review.
The [source notes](../audits/literature/Kar26/readme.md) retain the inspected edition and its actual scope.

The search stops here because it has located the exact existing random-matrix conjecture and the precise missing direction, while the finite-mean counterexample gives a decisive test of the simplest proposed transfer.
No absence-of-literature or novelty claim is made.
The useful next investigation is a family-specific negative determinant moment or a sharp asymptotic lower comparison, with the two explicit counterexamples retained as tests.
