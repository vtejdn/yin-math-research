---
author: Yin
---

# Finite-variance Wigner pencils: transfer obstructions and exact spectral reductions

## Question and development scope

This draft concerns the exact [finite-variance Wigner contract](../tasks/Yin_T_F0012_v3.md#contract).
The calculations and source comparisons were developed for Yin by the assigned small-singular-value subagent.
They are mathematical development and self-checking, not independent review.
The entry laws are fixed across matrix size, may be atomic or real, and have only the stated second moments.
The target is almost-sure weak convergence of the eigenvalue measure for every fixed scalar polynomial and every allowed coupling across sizes.
None of the obstructions below is a counterexample to that target.

The existing [GUE compression and tube proof](../claims/Yin_C_F0186_v1.md#compression) separates a deterministic error bound from an absolutely continuous probability estimate.
The former has useful extensions; the latter cannot simply be asserted for arbitrary product laws.
The general finite-variance nonselfadjoint assertion remains unresolved here.

<a id="atomic-tube-obstruction"></a>
## Atomic product measures do not satisfy a degree-only tube bound

Let \(g=(g_1,\ldots,g_n)\) have independent Rademacher coordinates and set
\[
 q_n(x)=\frac1n\sum_{i=1}^n(x_i^2-1)^2.
\]
This is a nonzero nonnegative real polynomial of degree four with \(q_n(0)=1\).
Nevertheless \(q_n(g)=0\) surely, so for every \(\rho\ge0\),
\[
 \mathbb P\{\operatorname{dist}(g,q_n^{-1}(0))\le\rho\}=1.
\]
Thus a bound tending to zero with tube radius, based only on degree and dimension and valid for all finite-variance product laws, is impossible.
The example already has bounded entries and moments of every order.
It rules out replacing the Gaussian input in [C_F0186 v1, tubes](../claims/Yin_C_F0186_v1.md#tubes) by a generic product-measure assertion.
It does not identify this polynomial as a pencil determinant and therefore does not disprove a determinant-specific small-ball estimate.
Any such estimate must use further structure of the determinant, entry law, conditional geometry or coefficient algebra.

<a id="real-affine-obstruction"></a>
## A positive free determinant does not force real-symmetric pencil invertibility

Take \(P(x,y)=xy-yx\) and real symmetric matrices \(X,Y\in M_N(\mathbb R)\).
Then
\[
 P(X,Y)^{\mathsf T}=-P(X,Y).
\]
If \(N\) is odd, its determinant equals its negative and is zero.
This holds deterministically, hence also for independent GOE inputs and for every real Wigner entry law.

On the free side \(Q=i(s_1s_2-s_2s_1)\) is the evaluation of a nonconstant selfadjoint scalar polynomial.
The scalar atomlessness and algebraic/Puiseux input of SS15, with the [previously retained exact scope](../ledger/Yin_L_F0058_v1.md), gives no atom at zero and a power bound for its spectral mass near zero.
Consequently
\[
 \int\log|t|\,d\mu_Q(t)>-\infty,
 \qquad \Delta(P(s_1,s_2))>0.
\]
The bounded support controls the positive logarithm, while the power bound controls the negative logarithm.

The obstruction already occurs for the fixed affine pencil
\[
 \mathcal L(x,y)=
 \begin{pmatrix}
 0&-x&y\\
 y&1&0\\
 x&0&1
 \end{pmatrix}.
 \tag{R1}
\]
Its lower-right block is \(I_2\), and its Schur complement is \(xy-yx\).
Thus, for finite matrices,
\[
 \det\mathcal L(X,Y)=\det(XY-YX).
\]
Bounded block factorization and [FK multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) give
\[
 \Delta_{\operatorname{tr}_3\otimes\tau}(\mathcal L(s_1,s_2))
 =\Delta_\tau(P(s_1,s_2))^{1/3}>0.
\]
Hence the analogue of eventual finite-dimensional invertibility for every affine pencil with positive free determinant is false for real-symmetric input spaces.
In particular, the normalized unregularized log determinant at this fixed shift cannot converge to its finite free value along odd sizes.

This does not invalidate [C_F0186 v2](../claims/Yin_C_F0186_v2.md), whose random inputs are complex Hermitian GUE.
Its generic-rank argument uses the Zariski density of Hermitian tuples in full complex matrix space.
Real symmetric tuples are not Zariski dense there: the equations \(X_{ab}=X_{ba}\) persist over the complex numbers.
The distinction matters even though both Gaussian models have semicircular limits.

Nor is (R1) a counterexample to the Task's weak eigenvalue conclusion.
The forced zero need only carry mass \(1/N\), and \(iP(X,Y)\) is selfadjoint.
For the usual scalar linearization at \(z\ne P(0)\), the constant coefficient is invertible and the determinant at the zero input is nonzero on every real-symmetric input space.
Thus this particular identically singular obstruction is absent from the monic, almost-every-shift application.

<a id="discrete-expectation-obstruction"></a>
## Discrete inputs obstruct fixed-shift unregularized expectation convergence

Let \(W_N=N^{-1/2}(\varepsilon_{ij})\) be real symmetric, with all upper-triangular and diagonal variables independent Rademacher variables.
The all-positive realization has positive probability and rank one, so for every \(N\ge2\),
\[
 \mathbb E\left[\frac1N\log|\det W_N|\right]=-\infty.
\]
The positive part is bounded for each \(N\), since \(\|W_N\|\le\sqrt N\), and the free semicircular determinant is positive.

Even an invertible constant coefficient does not remove this expectation obstruction.
For \(N=2^k\ge2\), let \(H_N=H_2^{\otimes k}\), where
\[
 H_2=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
The matrix \(H_N\) is symmetric, \(H_N^2=NI_N\), and \(\operatorname{Tr}H_N=0\).
It has eigenvalue \(\sqrt N\) with multiplicity \(N/2\).
The event \(\sqrt N W_N=H_N\) has probability \(2^{-N(N+1)/2}>0\), so
\[
 \mathbb E\left[\frac1N\log|\det(I_N-W_N)|\right]=-\infty
 \quad(N=2^k\ge2).
\]
In contrast \(\Delta(1-s)>0\), by the integrability of \(\log|1-t|\) against the semicircle density.
These rare events do not contradict almost-sure weak convergence; their probabilities are summable.
They show why the Task expressly excludes expectation convergence of unregularized logarithms.
A useful small-ball estimate may allow an \(N\)-dependent singularity probability rather than vanishing at fixed \(N\) as the radius tends to zero.

<a id="real-gaussian-monic-route"></a>
## Realification of the deterministic compression for a monic GOE route

For a real symmetric tuple \(H_j\) and a complex near-kernel vector \(v=(v_1,\ldots,v_m)\), replace the complex support space of [C_F0186 v1](../claims/Yin_C_F0186_v1.md#compression) by
\[
 W_{\mathbb R}=\operatorname{span}_{\mathbb R}
 \{\Re v_a,\Im v_a:1\le a\le m\},
 \qquad k\le2m.
\]
Let
\[
 W_{\mathrm{out},\mathbb R}
 =\sum_j P_{W_{\mathbb R}^{\perp}}H_jW_{\mathbb R},
 \qquad \ell\le dk.
\]
Choose real isometries \(U,V\) onto these orthogonal subspaces.
Then \(C_j=U^{\mathsf T}H_jU\) is real symmetric, \(B_j=V^{\mathsf T}H_jU\) is real, and \(w_a=U^{\mathsf T}v_a\) remains complex.
The exact relation \(H_jU=UC_j+VB_j\) gives the same two residual equations as in the complex proof.
Their real and imaginary parts and \(\|w\|^2-1\) form a quadratic real map in at most
\[
 d\frac{k(k+1)}2+d\ell k+2mk
\]
coordinates, bounded solely in terms of \(d,m\).
The same real polynomial error bound applies on a fixed norm-bounded set.
The lift
\[
 \delta H_j=U\delta C_jU^{\mathsf T}
 +V\delta B_jU^{\mathsf T}
 +U\delta B_j^{\mathsf T}V^{\mathsf T}
\]
is real symmetric and has the same Hilbert--Schmidt control.
This supplies a fixed-exponent real-symmetric distance-to-singularity implication on that norm set.

In Hilbert--Schmidt orthonormal coordinates, normalized GOE with off-diagonal variance \(1/N\) has the form \(H=\sqrt{2/N}\,g\) in \(dN(N+1)/2\) independent standard Gaussian coordinates.
For a monic pencil the determinant polynomial has value one at the origin, so it is nonzero on this real space for every \(N\).
The same degree-controlled Gaussian tube argument consequently supplies a polynomial least-singular-value floor on the norm-bounded event, with \(N\)-scaling of the same order as in the GUE argument.
This observation avoids the false general affine-rank extension above.

A complete GOE polynomial Brown proof still needs the intermediate-singular-value/logarithmic-tail interface, including an applicable quantitative resolvent comparison at a shrinking scale.
The retained CGP22 comparison was inspected for GUE, so it is not asserted here for GOE without checking or proving the needed modification.
Realification alone is therefore a partial proof route, not a completed GOE theorem and not a finite-variance Wigner theorem.

<a id="cyclic-selfadjoint-reduction"></a>
## An exact nonselfadjoint subclass reduces to the selfadjoint problem

Let \(A=A^*\) be a scalar noncommutative polynomial and let \(C\) be any scalar noncommutative polynomial.
Set
\[
 P=A C^*C,\qquad Q=CAC^*.
 \tag{C1}
\]
The polynomial \(Q\) is selfadjoint, whereas \(P\) need not be normal.
For every finite tuple of Hermitian matrices, put \(U=A(W)C(W)^*\) and \(V=C(W)\).
Then \(P(W)=UV\), \(Q(W)=VU\), and the determinant identity
\[
 \det(zI-UV)=\det(zI-VU)
 \tag{C2}
\]
holds for every \(z\in\mathbb C\), including multiplicities.
For \(z\ne0\), (C2) follows by taking the two Schur complements of \(\begin{pmatrix}zI&U\\V&I\end{pmatrix}\); polynomial continuity gives \(z=0\).
Thus the eigenvalue measures of \(P(W)\) and \(Q(W)\) agree exactly for every \(N\), with no inversion or least-singular-value assumption on \(C(W)\).

The free counterpart follows from the same block matrix and bounded FK multiplicativity.
For bounded \(u,v\) in a finite tracial algebra and \(z\ne0\),
\[
 \Delta_{\operatorname{tr}_2\otimes\tau}
 \left(\begin{pmatrix}z&u\\v&1\end{pmatrix}\right)^{2}
 =\Delta_\tau(z-uv)
 =|z|\,\Delta_\tau(1-vu/z)
 =\Delta_\tau(z-vu).
 \tag{C3}
\]
The triangular factors used in the two Schur decompositions have determinant one.
For completeness, an elementary upper unitriangular factor \(E(a)\) is similar through \(\operatorname{diag}(t,1)\) to \(E(ta)\), and its determinant is unchanged by this invertible similarity.
As \(t\downarrow0\), norm continuity of the determinant on invertible elements gives \(\Delta(E(a))=1\); the lower-triangular case is identical.
Block-diagonal normalization gives the square and the factor \( |z| \) in (C3).
The potentials in (C3) agree off one point and hence have identical distributional Laplacians, so the Brown measures of \(uv\) and \(vu\) coincide.
In (C1), this common Brown measure is the spectral measure of the selfadjoint \(Q(s)\).

Consequently any almost-sure weak-convergence theorem for fixed selfadjoint polynomials under the exact finite-variance model and its arbitrary cross-size couplings immediately proves the Task's conclusion for (C1).
For example \(P(x,y)=xy^2\) reduces to \(Q(x,y)=yxy\).
This transfer does not require almost-sure operator-norm bounds or moments of order \(2+\varepsilon\).
The selfadjoint finite-variance theorem is an explicit remaining input to this reduction; the algebraic argument itself supplies no proof of that input.

The same reduction extends to \(g(P)\) for any one-variable complex polynomial \(g\).
At finite size its eigenvalue measure is \(g_*\mu_{P(W)}\), by the ordinary spectral mapping identity with algebraic multiplicity.
For a nonconstant \(g\), write \(g(t)-z=b\prod_{j=1}^r(t-\lambda_j)\), with roots counted with multiplicity.
For any bounded element \(a\), FK multiplicativity and the Brown logarithmic potential formula give
\[
 \log\Delta(g(a)-z)
 =\log|b|+\sum_{j=1}^r\int\log|w-\lambda_j|\,d\mu_a^{\mathrm{Br}}(w)
 =\int\log|g(w)-z|\,d\mu_a^{\mathrm{Br}}(w).
\]
The equality is valid in the extended real sense, since the positive parts are bounded on the compact Brown support.
Taking distributional Laplacians proves \(\mu_{g(a)}^{\mathrm{Br}}=g_*\mu_a^{\mathrm{Br}}\); constant \(g\) gives the same identity directly.
Weak convergence is preserved under this continuous pushforward, because a bounded continuous test function composed with \(g\) is still bounded and continuous.

<a id="cross-size-frobenius-obstruction"></a>
## A Frobenius almost-sure shortcut fails under arbitrary size couplings

Choose a centered symmetric fixed real law of variance one whose tail satisfies
\[
 \mathbb P(|\xi|>t)\asymp\frac1{t^2(\log t)^2}
 \qquad(t\to\infty).
\]
Such a law has a finite second moment, since the tail integral is controlled by \(\int^\infty dt/(t(\log t)^2)\).
Take the Wigner matrices independent across sizes, with this off-diagonal law and zero diagonals.
For fixed \(K>0\), the chance that some upper off-diagonal raw entry exceeds \(N\sqrt K\) in magnitude is comparable to \(1/(K(\log N)^2)\).
Indeed there are \(N(N-1)/2\) independent opportunities, and their expected count tends to zero with this order, so \(1-(1-p_N)^{N(N-1)/2}\) has that same order.
The probabilities are not summable.
Independence across \(N\) and Borel--Cantelli show that such an entry occurs infinitely often almost surely.
On that event
\[
 \frac1N\operatorname{Tr}W_N^2
 =\frac1{N^2}\sum_{i,j}|\xi_{ij}^{(N)}|^2>2K.
\]
Taking a countable intersection over positive integer \(K\) proves that this normalized Frobenius quantity is almost surely unbounded.
Thus a nested-array strong law for this quantity cannot simply be used for every coupling in the Task.
This still does not refute weak spectral convergence: a vanishing fraction of exceptional large eigenvalues may destroy an unbounded-moment statistic while preserving every bounded continuous test.
Any positive-logarithm argument that needs stronger control must prove the appropriate weaker tail statement directly.

<a id="literature-boundaries"></a>
## Primary-source boundaries for the missing small-singular-value estimates

The following passages were inspected in primary online originals on 2026-11-05.
Their source statements were checked for applicability; their entire original proofs were not independently audited here.
The new literature is not registered or acquired by this draft.

Nguyen and O'Rourke, [The elliptic law, arXiv:1208.5883v4](https://arxiv.org/pdf/1208.5883v4), Definition 1.3 on PDF p. 2 and Theorems 1.5, 1.8, 1.9 on pp. 3--5, provide finite-second-moment results for scalar matrices with independent mirrored pairs.
The complex theorem imposes the \((\mu,\rho)\) covariance pattern of Definition 1.6, with real \(|\rho|<1\); it does not require independence of real and imaginary parts.
Its model uses a nested infinite array.
Theorem 1.9 gives arbitrary polynomial failure probabilities for a polynomial least-singular-value floor under a polynomially bounded deterministic shift.
These hypotheses concern scalar elliptic pairs, not an arbitrary fixed matrix-coefficient pencil.
Immediately after Theorem 1.8, the wider complex covariance formulation is presented as a conjecture in that inspected edition.

One useful application can be checked directly.
Assume additionally that every off-diagonal Wigner law satisfies \(\mathbb E\xi_j^2=0\), and consider \(L=\sum_j c_jW_j\).
Set \(\sigma^2=\sum_j|c_j|^2>0\), and choose a common phase so that
\[
 \rho=\frac{|\sum_jc_j^2|}{\sigma^2}<1.
\]
The normalized upper/lower pair then satisfies
\[
 \mathbb E X_{12}^2=\mathbb E X_{21}^2=0,
 \quad \mathbb E X_{12}\overline{X_{21}}=0,
 \quad \mathbb E X_{12}X_{21}=\rho,
\]
and the real covariance matrix is exactly the \((1/2,\rho)\) pattern.
Thus the inspected elliptic theorem applies to this additional subclass in its nested model.
The identification with the free elliptic Brown law can also be made by applying both this theorem and [C_F0186 v3](../claims/Yin_C_F0186_v3.md#statement) to the corresponding proper Gaussian inputs and using uniqueness of the deterministic limit.
A proof that its complete probability estimates cover every cross-size coupling remains separate from citing its stated nested model.

The real-symmetric example \(L=(W_1+iW_2)/\sqrt2\) is outside this complex covariance subclass.
Its mirrored raw entries are equal, with \(\mathbb E\Re X_{12}\Re X_{21}=1/2\) but \(\mathbb E X_{12}X_{21}=0\), contrary to the required covariance pattern at \(\mu=1/2,\rho=0\).
No conclusion that all Wigner linear combinations are covered is justified by this source.

Campbell and O'Rourke, [Spectrum of Heavy-Tailed Elliptic Random Matrices, arXiv:2010.01261v3](https://arxiv.org/pdf/2010.01261v3), Theorem 5.1 on PDF pp. 19--20, allows independent mirrored pairs and requires positive bounded-truncation variance and conditional correlation modulus strictly below one.
It gives an explicit least-singular-value estimate on an operator-norm event, for arbitrary deterministic shifts.
Its displayed bound retains a term of order \(n^{-1/8}\), up to logarithms for polynomial norm cutoffs, so this statement alone does not provide summable exceptional probabilities.
Equal complex mirrored entries have conditional correlation modulus one and are excluded.
The theorem is a useful paired-entry technique, not a theorem for all finite block pencils.

Han, [arXiv:2606.01664v1](https://arxiv.org/html/2606.01664v1), Theorem 1.4 and Section 6, treats non-Hermitian iid entries with bounded planar density and all moments finite.
Its conditional-column small-ball mechanism is a model for structured coefficient estimates, but neither its independence pattern nor its entry assumptions match the present Wigner contract.
The repository's [retained Han inspection](../audits/literature/Han26/Yin_U001.md) owns the detailed source boundary.

The abstract of Alt--Erdős--Krüger--Nemish, [Location of the spectrum of Kronecker random matrices, arXiv:1706.08343](https://arxiv.org/abs/1706.08343), was inspected only for its stated spectrum-location scope.
No full theorem or input hypothesis from that work is adopted here.
An exclusion of eigenvalues outside a deterministic region is not by itself the required logarithmic-tail estimate inside that region.

<a id="remaining-interface"></a>
## Remaining interface and route choice

For a general polynomial, exact linearization and convergence of Hermitized spectral measures still leave the negative logarithm near zero uncontrolled.
Exact zeros at a fixed shift have a simple almost-everywhere qualification that does not require any entry regularity.
For each realization, the union of the finite spectra \(\bigcup_{N\ge1}\operatorname{spec}(P(W^{(N)}))\) is countable and has planar measure zero.
Tonelli's theorem on each bounded disk therefore shows that, for almost every deterministic \(z\), almost surely no size \(N\) has \(\det(P(W^{(N)})-z)=0\).
This statement holds under arbitrary couplings across sizes.
It explains why the fixed-shift singularity examples above do not automatically obstruct hermitization, but gives no lower bound on nonzero singular values.
A sufficient route is, for almost every fixed complex \(z\), an almost-sure bound making
\[
 \lim_{\delta\downarrow0}\limsup_{N\to\infty}
 \int_{(0,\delta)}|\log t|\,d\nu_{P(W^{(N)})-z}(t)=0
\]
followed by the applicable planar potential argument and tightness.
An integrated version over \(z\) may be weaker and preferable, but it must still exclude a macroscopic logarithmic defect.
At the level of small singular values, a polynomial floor with summable failure probabilities and an adequate intermediate-singular-value count are distinct obligations.
Neither a fixed-shift floor alone nor weak convergence of the singular-value distribution supplies the intermediate contribution.

The promising distributional next step is a determinant-specific conditioning argument for mirrored entries or block rows, rather than a degree-only tube estimate.
The coefficient-dependent conditional covariance or anti-concentration statement must survive Schur complementation and the real/atomic cases actually allowed by the Task.
The scalar symmetric-shift and product benchmarks being studied in [D_F0010](Yin_D_F0010.md) provide narrower places to test this interface.
The real-Gaussian monic calculation above is another controlled benchmark, with an explicitly missing mesoscopic comparison.

The deterministic rank and vanishing-norm perturbation failures already have an adequate home in [L_F0058 v1, excluded shortcuts](../ledger/Yin_L_F0058_v1.md#failed-shortcuts).
They prohibit inferring the required nonnormal spectral stability from low-rank truncation or small added noise alone.
No inspected source or construction here proves or refutes the full finite-variance Task.
