---
author: Yin
---

# Finite-variance Wigner convergence: precise obstructions and source frontier

This synthesis concerns the [reactivated finite-variance Task](../tasks/Yin_T_F0012_v3.md#contract).
It retains mathematical comparisons, failed transfers and source applicability inspected on 2026-11-05; it is not independent proof-review evidence.
None of the auxiliary obstructions below is a counterexample to the full almost-sure weak-convergence contract.
The now fixed [spectral and potential controls](../claims/Yin_C_F0186_v4.md#statement) replace the previously missing preliminary weak-limit argument.
Their exact defect condition and the [intermediate singular-value theorem](../claims/Yin_C_F0187_v1.md#statement) identify the smaller remaining small-value problem.
The cyclic nonnormal subclass is retained with its complete proof in [C_F0186_v4](../claims/Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction), rather than duplicated here.

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

## Two distinctions that change the proof route

Finite second moments do not imply convergence of every normalized trace moment, even for a single Wigner matrix with a fixed atom law.
They also do not imply almost-sure bounded normalized Hilbert--Schmidt norm under every allowed coupling between sizes.
Neither failure contradicts weak convergence of the empirical measures against bounded continuous functions.
These distinctions prevent importing stronger intermediate statements into the current Task.

### A fixed-law example with divergent fourth trace moments

Let \(\eta\) be a symmetric real random variable with a Pareto tail of exponent \(5/2\), rescaled to variance one.
Thus, for some \(c>0\) and all sufficiently large \(t\),
\[
 \mathbb P\{|\eta|>t\}=ct^{-5/2},\qquad
 \mathbb E\eta=0,\qquad \mathbb E\eta^2=1.
\]
This law even has a moment of order \(2+\varepsilon\) for every \(0<\varepsilon<1/2\).
At each size \(N\), take independent copies \(\eta_{ij}^{(N)}\), \(i<j\), above the diagonal, reflect them across the diagonal, and take independent Rademacher diagonal entries.
Let \(W_N\) be this real symmetric matrix divided by \(\sqrt N\).
The model satisfies the current contract, independently of how the matrices of different sizes are coupled.
Writing \(\operatorname{tr}_N=N^{-1}\operatorname{Tr}\), Hermiticity gives
\[
 \operatorname{tr}_N(W_N^4)
 \ge \frac{\|W_N\|^4}{N}
 \ge \frac{\max_{i<j}|\eta_{ij}^{(N)}|^4}{N^3}.
 \tag{1}
\]
For every fixed \(R>0\), the independence within each size therefore implies, for all sufficiently large \(N\),
\[
 \begin{aligned}
 \mathbb P\{\operatorname{tr}_N(W_N^4)\le R\}
 &\le
 \left(1-cR^{-5/8}N^{-15/8}\right)^{N(N-1)/2}\\
 &\le \exp(-c_RN^{1/8}).
 \end{aligned}
 \tag{2}
\]
This upper bound is summable in \(N\).
First Borel--Cantelli, followed by the countable intersection over positive integers \(R\), proves
\[
 \operatorname{tr}_N(W_N^4)\longrightarrow+\infty
 \quad\text{almost surely under every cross-size coupling.}
 \tag{3}
\]
In particular, convergence of all normalized trace moments to semicircular moments is false under the bare second-moment hypotheses.
For \(P(x)=x^4\), (3) concerns an unbounded test function of the input empirical law; it does not refute the weak spectral limit of \(P(W_N)\).
This is an elementary calculation developed here, not a theorem attributed to a source.

### Independent sizes can have unbounded second trace moments

Keep the same fixed law, and now choose the matrices independently across different sizes.
This is one of the couplings permitted by the contract.
For fixed \(R>0\), let
\[
 E_{N,R}=\left\{\max_{i<j}|\eta_{ij}^{(N)}|>\sqrt R\,N\right\}.
\]
Then
\[
 \mathbb P(E_{N,R})
 =1-\left(1-cR^{-5/4}N^{-5/2}\right)^{N(N-1)/2}
 \asymp_R N^{-1/2}.
 \tag{4}
\]
On \(E_{N,R}\),
\[
 \operatorname{tr}_N(W_N^2)
 =N^{-2}\sum_{i,j}|\eta_{ij}^{(N)}|^2>R.
 \tag{5}
\]
The events \(E_{N,R}\) are independent across \(N\), and their probabilities have divergent sum.
Second Borel--Cantelli and the countable intersection over positive integers \(R\) yield
\[
 \limsup_N\operatorname{tr}_N(W_N^2)=+\infty
 \quad\text{almost surely.}
 \tag{6}
\]
By comparison, with the usual nested infinite-array construction, enumerate the upper triangular entries in increasing order of their maximal index.
The ordinary strong law for the iid integrable variables \(|\eta_{ij}|^2\), along the subsequence of the first \(N(N-1)/2\) entries, gives \(\operatorname{tr}_N(W_N^2)\to1\) almost surely; the Rademacher diagonal contributes only \(1/N\).
Thus a proof that silently replaces arbitrary cross-size coupling by a nested-array strong law loses a genuine quantifier in the Task.
Equation (6) remains a failure of an auxiliary norm bound, not a failure of weak empirical-measure convergence.

<a id="source-frontier"></a>
## Inspected primary-source boundaries

The following are direct inspections of selected primary sources, rather than an exhaustive literature search or complete audits of their proofs.
The comparisons below do not adopt the cited full theorems as solutions of the current Task.
GNT14 contributes only the bounded-product concentration input at the exact interface in [C_F0187_v1](../claims/Yin_C_F0187_v1.md#argument).
The search found no theorem that discharges the exact general-polynomial finite-variance almost-sure contract.

### Belinschi--Capitaine: do not read Proposition 2.2 as a bare-second-moment moment theorem

The inspected edition is [arXiv:1611.07440v2](https://arxiv.org/pdf/1611.07440v2), dated 19 September 2017.
The global model on PDF p. 5 assumes fourth-moment tail domination in (1.5) and a uniform third-moment bound.
PDF p. 12 defines \(\theta_* = \sup_{i<j}\mathbb E|X_{ij}|^3\) and repeats fourth-moment domination in (2.4).
Proposition 2.2 on PDF pp. 15--16 explicitly restates only centered unit second moments, while its proof imports the operator-norm approximation (2.15), expressed in terms of that \(\theta_*\), and the preceding truncation argument.
Its conclusion uses noncommutative distribution, defined through all normalized trace moments.
Equations (1)--(3) rule out the bare-finite-variance interpretation of that conclusion.
The safe boundary is to retain the stronger carried model hypotheses when using the cited norm argument; this inspection does not assert an official erratum or resolve the authors' intended scope.
For the present Task, prove weak self-adjoint spectral convergence by a finite-variance truncation/rank argument instead of citing this proposition as all-moment freeness.

### Han: nonnormal universality has a different input class

The inspected primary edition is [Han, arXiv:2606.01664v1](https://arxiv.org/html/2606.01664v1), particularly Theorems 1.2 and 1.4 and Questions 1.7--1.8.
The retained repository source and audit are [Han26.pdf](../literature/pdf/Han26.pdf) and [the existing source audit](../audits/literature/Han26/Yin_U001.md).
Theorem 1.2 treats holomorphic polynomials in independent complex Ginibre matrices and states weak convergence in probability.
Theorem 1.4 treats centered variance-one complex iid full matrices with bounded planar density and all moments; the discussion after it allows a sufficiently high finite moment depending on the polynomial.
It does not identify a universal second-moment threshold.
Real Gaussian variables, removal of density, and polynomials involving adjoints are explicit further questions in that introduction.
Consequently this theorem does not supply the Wigner-symmetry, atomic-law, finite-variance, or arbitrary-coupling almost-sure interfaces required here.

### Two Wigner factors are an informative benchmark

The inspected edition is [O'Rourke--Renfrew--Soshnikov--Vu, arXiv:1403.6080v3](https://arxiv.org/pdf/1403.6080v3), dated 2 March 2015, PDF pp. 4--5.
Theorem 2.8 gives almost-sure square-circular convergence for two real Wigner factors with iid on-or-above-diagonal entries and \(2+\tau\) moments.
The general elliptic-product Theorem 2.3 requires \(2+\tau\) moments and \(|\rho_k|<1\); Remark 2.5 discusses removing those restrictions.
This supplies a concrete special-case comparison, not a finite-variance theorem for arbitrary Wigner polynomials.
For research triage, \(P(x,y)=xy\) with two real Wigner inputs and only second moments is already a useful target for the new logarithmic-tail interface.

### A sharper finite-variance smallest-value starting point

Nguyen's [journal article, EJP 17 (2012), no. 53](https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2165/2165-10579-1-PB.pdf), DOI 10.1214/EJP.v17-2165, was inspected at Condition 1.3 and Theorem 1.4 on PDF p. 2 and the initial truncation on PDF p. 3.
For real symmetric matrices whose on-or-above-diagonal entries are iid, it assumes centered unit variance and \(\mathbb P\{|\xi-\xi'|\ge c_1\}\ge c_2>0\), and allows a deterministic symmetric perturbation with entries bounded by a fixed power of \(N\).
For every \(B>0\), it gives an \(A>0\) with \(\mathbb P\{s_{\min}(X_N+F_N)\le N^{-A}\}\le N^{-B}\) eventually.
The [author-hosted 23-page preprint](https://people.math.osu.edu/nguyen.1261/cikk/singular-noLO.pdf) labels this Theorem 1.3 and has placeholder journal metadata; the actual journal theorem number is 1.4, not the number 1.5 cited in the product paper.
The full proof has not been audited here, and the complex-symmetric deterministic-shift extension is not silently included.

The anti-concentration condition is automatic for each fixed nondegenerate real law: since \(\mathbb P\{\xi\ne\xi'\}>0\), some positive threshold \(c_1\) has positive exceedance probability.
This observation uses no moment above two.
The equality of diagonal and off-diagonal laws in this statement is an extra restriction relative to the current Task.

Section 7 of the product paper, especially Theorems 7.2--7.3 and the proof on PDF pp. 25--26, conditions on the second factor and uses the identity
\[
 (W_1W_2-wI)^{-1}
 =W_2^{-1}(W_1-wW_2^{-1})^{-1}.
 \tag{8}
\]
For real symmetric \(W_2\), the conditional shift \(-wW_2^{-1}\) is complex symmetric, and its norm is polynomially bounded on the good invertibility event.
The product paper attributes the complex-symmetric-shift extension to a personal communication with Nguyen.
Its Theorem 7.3 explicitly retains the assumptions of Theorem 2.8, including \(2+\tau\) moments and iid diagonal/off-diagonal laws; it does not itself state the finite-variance or arbitrary-diagonal extension.
Thus checking that extension at finite variance is a specific source/proof interface, rather than a reason to require \(2+\tau\) for the preliminary smallest-value estimate.
Its crude polynomial upper-norm step uses only a second-moment Markov bound.
Even success with (8) gives neither intermediate singular-value counting nor the full negative-log uniform integrability in (7).

### Finite-variance elliptic sources do not automatically include the Wigner boundary

The inspected [Nguyen--O'Rourke elliptic-law edition, arXiv:1208.5883v4](https://arxiv.org/pdf/1208.5883v4), is dated 9 September 2014.
Definition 1.3 uses an infinite double array with independent mirror pairs.
Theorem 1.5, PDF p. 3, gives the real finite-variance elliptic law almost surely for \(|\rho|<1\), including specified deterministic perturbations.
Theorem 1.8 uses the complex covariance pattern in Definition 1.6, not merely a bound on one complex correlation.
In particular, its real and imaginary mirror covariances have opposite prescribed signs, so it cannot be applied automatically to the equal complex mirror entries of \(W_1+iW_2\) formed from real symmetric Wigner matrices.
The paragraph following that theorem conjectures a fuller complex extension.
The source's nested-array formulation also needs attention before importing its almost-sure statement under arbitrary size coupling.

The inspected [Götze--Naumov--Tikhomirov edition, arXiv:1404.7013v1](https://arxiv.org/pdf/1404.7013v1), has arXiv date 28 April 2014 and internal date 6 July 2021.
Its Theorem 1.1, PDF p. 2, proves convergence in probability of products of at least two real elliptic matrices under uniform integrability of squared entries, with strict \(|\rho|<1\).
This is a genuinely low-moment result, but neither the real Wigner boundary \(\rho=1\) nor the almost-sure conclusion is included in that theorem.

## Complex covariance scope beyond the scalar elliptic benchmark

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

## A strictly finite-variance coupling example

The same binomial and second Borel--Cantelli calculation also applies to a centered symmetric variance-one law with
\[
 \mathbb P\{|\xi|>t\}\asymp[t^2(\log t)^2]^{-1}.
\]
Its second moment is finite by integration of \(1/[t(\log t)^2]\), while every moment above two is infinite.
With independent sizes and zero diagonals, the probability of some upper raw entry exceeding \(N\sqrt K\) is comparable to \(1/[K(\log N)^2]\).
This is nonsummable, and on that event \(\operatorname{tr}_N W_N^2>2K\).
Countable intersection over integer \(K\) gives almost-sure unbounded normalized Frobenius norm, without contradicting weak convergence.

## Consequence for the active route

The general question should be attacked through the [planar logarithmic defect](../claims/Yin_C_F0186_v4.md#remaining-defect), not by extending an all-fixed-shift Gaussian determinant statement to real or atomic entries.
The selfadjoint, Hermitized, positive-tail, regularized and planar tightness interfaces now have a complete candidate argument at exact second moments.
The intermediate singular-value estimate controls all but the bottom order \(N^{3/4}\) singular values for a single real Wigner matrix with an independent arbitrary complex shift.
For the two-factor pilot \(W_1W_2-z\), the remaining proposed input is a summable polynomial least-singular-value bound for real Wigner plus a polynomially bounded complex symmetric shift.
The [original CS development](../claims/Yin_C_F0188_v1.md#argument) is preserved as a fixed candidate.
Its [revised profile argument](../claims/Yin_C_F0188_v2.md#argument) and the [two-factor deduction](../claims/Yin_C_F0186_v5.md#argument) have their own explicit assessments.
The general fixed matrix-coefficient pencil requires additional treatment of coefficient-space degeneracy beyond this scalar shift pilot.

## Source preparation and inspection boundary

The selected source notes are [BC17](../audits/literature/BC17/readme.md), [ORSV15](../audits/literature/ORSV15/readme.md), [Ngu12](../audits/literature/Ngu12/readme.md), [NO15](../audits/literature/NO15/readme.md), [CO22](../audits/literature/CO22/readme.md), and [GNT14](../audits/literature/GNT14/readme.md).
They distinguish the actual arXiv or journal editions, metadata, theorem numbers and external-proof limits.
The retained [Han26 inspection](../audits/literature/Han26/Yin_U001.md) remains the responsible home for that source's detailed input boundary.
This is a bounded source search, not a claim that the full literature contains no stronger theorem.
