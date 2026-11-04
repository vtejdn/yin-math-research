---
author: Yin
---

# Normalized determinants of affine GUE pencils

This version extends the fixed-coefficient pencil analysis of [v1](Yin_C_F0186_v1.md#statement) to arbitrary deterministic constant matrices and to the normalized determinant itself.
It retains the previously discussed affine extension, including singular constant terms and a zero limiting determinant.
The [F0012 completion](../tasks/Yin_T_F0012_v1.md#decision-full-polynomial-proof) continues to select v1 and its original review; this version neither changes that contract nor transfers its review to the additional argument.
No novelty or priority claim is made.

<a id="statement"></a>
## Exact affine statement

Fix integers \(m,d\ge1\) and matrices \(A_0,\ldots,A_d\in M_m(\mathbb C)\), independent of \(N\).
Let \(H_1^{(N)},\ldots,H_d^{(N)}\) be independent Hermitian matrices, each with density proportional to \(\exp(-N\operatorname{Tr}(H^2)/2)\).
Let \(s_1,\ldots,s_d\) be free centered semicircular elements of variance one in a finite von Neumann algebra with faithful normal tracial state \(\tau\).
Put
\[
 L_N=A_0\otimes I_N+\sum_{j=1}^d A_j\otimes H_j^{(N)},\qquad
 L=A_0\otimes1+\sum_{j=1}^d A_j\otimes s_j,\qquad
 \tau_m=\operatorname{tr}_m\otimes\tau,\quad
 \operatorname{tr}_m=\operatorname{Tr}_m/m.
\]
Use the [ordinary Fuglede--Kadison determinant](../audits/literature/MS24/Yin_U001.md#determinant-convention), including zero spectral mass, and the conventions \(\log0=-\infty\), \(\exp(-\infty)=0\).
Then
\[
 U_N:=\frac1{mN}\log|\det L_N|
 \xrightarrow{\mathbb P}
 u:=\tau_m(\log|L|)\in[-\infty,\infty),
 \qquad
 |\det L_N|^{1/(mN)}\xrightarrow{\mathbb P}\Delta_{\tau_m}(L)=e^u.
 \tag{D}
\]
For \(u=-\infty\), convergence means \(\mathbb P\{U_N>-K\}\to0\) for every finite \(K>0\).
For finite \(u\), a value \(U_N=-\infty\) counts as an infinite deviation.

If \(u>-\infty\), there is \(B<\infty\) such that
\[
 \mathbb P\{s_{\min}(L_N)<N^{-B}\}\longrightarrow0.
 \tag{F}
\]
More precisely, for every fixed finite cutoff \(M>0\), there are \(N_0,C,\alpha,c,\varepsilon_0>0\), independent of \(N\), such that for \(N\ge N_0\) and \(0<\varepsilon\le\varepsilon_0\),
\[
 \mathbb P\{s_{\min}(L_N)\le\varepsilon,\ \max_j\|H_j^{(N)}\|\le M\}
 \le C N^{5/2}\varepsilon^\alpha
           \exp(CN^{5/2}\varepsilon^\alpha)+e^{-cN^2}.
 \tag{A}
\]
The constants may depend on all the fixed coefficients, \(m,d\), and \(M\).
Neither \(A_0\) invertible, irreducibility of the coefficient algebra, nor a positive bilinear covariance lower bound is assumed.
Using \(1/N\) in place of \(1/(mN)\) changes the determinant limit to \(\Delta_{\tau_m}(L)^m\).
There is no assertion about a complex determinant phase, convergence of \(\mathbb E U_N\), almost-sure convergence, growing coefficient dimension, or other input ensembles.

<a id="inputs"></a>
## Dependencies and source scope

The local geometric inputs are the real polynomial distance inequality and its bounded-coordinate use in [v1, error-bound section](Yin_C_F0186_v1.md#error-bound), and the nonzero nonnegative polynomial Gaussian tube estimate in [v1, tube section](Yin_C_F0186_v1.md#tubes).
The latter is the general estimate (T4), including its proved regular-level extension to singular zero sets, not an assumption that the affine determinant is monic.
The affine compression and the eventual nonidentity of its determinant are proved separately below.
The accepted external inputs behind those sections are the stated polynomial-map inequality of Kurdyka--Spodzieja, as recorded in KSS16 (KS2), and Lot15 Theorem 1.1.
Their full original proofs are not re-audited here.

The additional algebraic input is the Ivanyos--Qiao--Subrahmanyam rank regularity lemma, as stated in [DM17, Proposition 2.3, journal p. 49 / PDF p. 6](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.54.pdf#page=6).
The retained [published original](../literature/pdf/DM17.pdf) and [edition note](../audits/literature/DM17/readme.md) identify the inspected version.
The underlying IQS proof is accepted, not independently re-proved here.
The application is over the infinite field \(\mathbb C\); no small-field assertion is needed.

For the analytic input, [SS15, arXiv:1305.1920v1, Theorem 1.1(5)(6), pp. 1--2](https://arxiv.org/pdf/1305.1920v1#page=2) applies to self-adjoint matrix-valued polynomials in free semicircular elements.
[CGP22, arXiv:1912.04588v1, Corollary 1.3, p. 5](https://arxiv.org/pdf/1912.04588v1#page=5) allows fixed coefficient amplification and supplies the resolvent comparison below.
The matrix-valued statements and their hypotheses were inspected in the retained originals, [SS15](../literature/pdf/SS15--arxiv-v1.pdf) and [CGP22](../literature/pdf/CGP22--arxiv-v1.pdf).
Their original proofs, standard GUE moment/norm convergence, basic polynomial zero-set facts and spectral functional calculus are accepted inputs.
Scalar-polynomial atomlessness is not substituted for matrix-valued atomlessness.

<a id="argument"></a>
## Complete affine argument

Let \(\nu_N\) be the empirical spectral probability measure of \(L_N^*L_N\), with normalization \(1/(mN)\), and let \(\nu\) be the spectral distribution of \(L^*L\) under \(\tau_m\).
GUE star-moment convergence, the fixed coefficients and a bounded operator-norm event give \(\nu_N\to\nu\) weakly in probability.
Thus the deterministic expected measures \(\bar\nu_N=\mathbb E\nu_N\) converge weakly to \(\nu\), since integrals of bounded continuous functions are bounded random variables converging in probability.
These facts do not use logarithmic integrability.

<a id="zero-limit"></a>
## Zero limiting determinant

For fixed \(\delta>0\), set
\[
 U_{N,\delta}=\frac1{2mN}\log\det(L_N^*L_N+\delta^2 I_{mN}),
 \qquad
 u_\delta=\frac12\int\log(x+\delta^2)\,d\nu(x).
\]
The weak singular-value convergence and bounded norm event imply \(U_{N,\delta}\to u_\delta\) in probability.
Indeed, on that event the logarithm is a bounded continuous function on a fixed compact interval, and a bounded continuous extension handles the complement in probability.
For every \(N\), \(U_N\le U_{N,\delta}\), with the convention at a singular matrix.
Also \(u_\delta\downarrow u\) as \(\delta\downarrow0\), by monotone convergence after subtracting a fixed upper bound on the compact spectral support.

If \(u=-\infty\), fix \(K>0\) and choose \(\delta\) with \(u_\delta<-K-1\).
Then
\[
 \mathbb P\{U_N>-K\}
 \le \mathbb P\{U_{N,\delta}>-K\}\longrightarrow0.
\]
This proves (D) in the zero-determinant case without a minimum-singular-value estimate.
The rest of the proof assumes \(u>-\infty\), so \(\nu(\{0\})=0\).

<a id="matrix-space-rank"></a>
## Matrix-space rank and tensor blow-ups

**Definition.**
For a complex linear subspace \(\mathcal X\subseteq M_{p,q}(\mathbb C)\), its matrix-space rank is
\[
 \operatorname{rk}\mathcal X=\max_{X\in\mathcal X}\operatorname{rank}X.
\]
For an integer \(n\ge1\), its square tensor blow-up is
\[
 \mathcal X^{\{n\}}=\mathcal X\otimes M_n(\mathbb C)
 =\left\{\sum_{\ell=1}^{r}X_\ell\otimes Y_\ell:
       r<\infty,\ X_\ell\in\mathcal X,\ Y_\ell\in M_n(\mathbb C)\right\}
 \subseteq M_{pn,qn}(\mathbb C).
\]
These are the square specialization over \(\mathbb C\) of DM17 Definitions 2.1--2.2, journal p. 49.
DM17 Proposition 2.3 states
\[
 \operatorname{rk}(\mathcal X^{\{n\}})\in n\mathbb Z.
 \tag{Rk}
\]
The rank here is a maximum over the matrix space, not the assertion that every matrix in that space has rank divisible by \(n\).

<a id="generic-rank"></a>
## Eventual nonidentity of the affine determinant

Let \(\mathcal X=\operatorname{span}_{\mathbb C}\{A_0,\ldots,A_d\}\), and define
\[
 r_N=\max_{X_1,\ldots,X_d\in M_N(\mathbb C)}
       \operatorname{rank}\left(A_0\otimes I_N+\sum_{j=1}^d A_j\otimes X_j\right).
\]
Then \(r_N=\operatorname{rk}(\mathcal X^{\{N\}})\).
One inequality follows by setting the homogeneous variable \(X_0=I_N\).
For the other, choose a maximum-rank tuple for \(\sum_{j=0}^d A_j\otimes X_j\) with \(X_0\) invertible.
Such a tuple exists because the maximum-rank locus and \(\det X_0\ne0\) are nonempty Zariski open subsets of the same complex affine space, hence intersect.
Right multiplication by \(I_m\otimes X_0^{-1}\) preserves rank and gives the affine tuple with variables \(X_jX_0^{-1}\).
By (Rk), \(r_N\) is a multiple of \(N\).

The set of Hermitian tuples is Zariski dense in \(M_N(\mathbb C)^d\).
To see this directly, choose a real basis of \(\operatorname{Herm}_N\), which is also a complex basis of \(M_N(\mathbb C)\).
A complex polynomial vanishing for every real choice of those coordinates vanishes identically, by repeated use of the one-variable polynomial identity principle.
Consequently a nonzero maximum-rank minor remains a nonzero polynomial on Hermitian tuples.
Its zero set has Lebesgue measure zero in the real coordinate space, so the GUE tuple attains \(r_N\) almost surely.
If \(r_N=0\), all evaluations have rank zero and the same assertion is immediate.

If \(r_N<mN\) along an infinite subsequence, divisibility gives \(mN-r_N\ge N\).
Along that subsequence,
\[
 \bar\nu_N(\{0\})\ge \frac1m.
\]
The Portmanteau inequality for the closed set \(\{0\}\), applied to \(\bar\nu_N\Rightarrow\nu\), would imply \(\nu(\{0\})\ge1/m\), a contradiction.
Thus \(r_N=mN\) for every sufficiently large \(N\).
In particular, the determinant of the affine pencil is then a nonzero polynomial on Hermitian tuples and \(L_N\) is invertible almost surely.
No scalar tuple \(t\in\mathbb R^d\) with \(A_0+\sum_jt_jA_j\) invertible is required.

<a id="affine-repair"></a>
## Fixed-dimensional Hermitian repair with an arbitrary constant term

Fix \(M\) and deterministic Hermitian \(H_j\) with \(\max_j\|H_j\|\le M\).
Choose a unit vector \(v=(v_1,\ldots,v_m)\) with \(\|L_N(H)v\|\le\varepsilon\).
Put
\[
 W=\operatorname{span}\{v_1,\ldots,v_m\},\quad k=\dim W\le m,\qquad
 W_{\rm out}=\sum_jP_{W^\perp}H_jW,\quad \ell=\dim W_{\rm out}\le dk.
\]
Let \(U:\mathbb C^k\to W\) and \(V:\mathbb C^\ell\to W_{\rm out}\) be isometries, omitting \(V\) if \(\ell=0\), and set
\[
 C_j=U^*H_jU,\qquad B_j=V^*H_jU,\qquad w_a=U^*v_a.
\]
Then \(H_jU=UC_j+VB_j\), and the complete residual has the orthogonal coordinates
\[
 (A_0\otimes I_k)w+\sum_j(A_j\otimes C_j)w,\qquad
 \sum_j(A_j\otimes B_j)w.
 \tag{C}
\]
The constant coefficient maps the physical component span \(W\) into itself, so there is no additional outgoing term from \(A_0\).

Take real coordinates for \(C_j\in\operatorname{Herm}_k\), \(B_j\in M_{\ell,k}(\mathbb C)\), and \(w\in\mathbb C^{mk}\).
The real and imaginary parts of (C), together with \(\|w\|^2-1\), form a real polynomial map \(F_{k,\ell}\) of degree two.
Its input dimension and actual coordinate bound are
\[
 p_{k,\ell}=dk^2+2d\ell k+2mk\le m^2(2d^2+d+2),\qquad
 |x|^2\le2dkM^2+1,\qquad |F_{k,\ell}(x)|\le\varepsilon.
\]
These maps range over finitely many types depending only on the fixed coefficients, not on \(N\) or the orientations of \(W,W_{\rm out}\).

Apply the real polynomial distance inequality (KSS) in [v1](Yin_C_F0186_v1.md#error-bound) to each type with nonempty zero set.
It supplies a zero \(x'=(C',B',w')\) with \(\|w'\|=1\) and \(|x'-x|\le C\varepsilon^\alpha\), with a common positive \(\alpha\) independent of \(N\).
For a type with empty zero set, the residual has a positive minimum on the compact coordinate region above, excluding sufficiently small residuals of that type.
The finitely many types therefore have common \(C,\alpha,\varepsilon_0>0\).

Define
\[
 \Delta H_j=U(C_j'-C_j)U^*
       +V(B_j'-B_j)U^*+U(B_j'-B_j)^*V^*.
\]
These are Hermitian, and
\[
 (H_j+\Delta H_j)U=UC_j'+VB_j',\qquad
 \sum_j\|\Delta H_j\|_{\rm HS}^2
 =\sum_j\left(\|C_j'-C_j\|_{\rm HS}^2+2\|B_j'-B_j\|_{\rm HS}^2\right)
 \le2|x'-x|^2.
\]
The vector \(v'=(Uw_1',\ldots,Uw_m')\) is a unit exact kernel vector for \(L_N(H+\Delta H)\).
Thus
\[
 \operatorname{dist}_{\rm HS}\bigl(H,\{K:\det L_N(K)=0,\ K_j=K_j^*\}\bigr)
 \le C\varepsilon^\alpha.
 \tag{BE-A}
\]
The assertion is understood through the constructed perturbation; if that singular set is empty, sufficiently small residuals on the norm event cannot occur.
This deterministic construction requires no measurable choice or distributional assertion about the adaptive subspaces.

<a id="affine-tube"></a>
## Gaussian tubes and the polynomial floor

In real Hilbert--Schmidt orthonormal coordinates, the normalized GUE tuple is \(H=N^{-1/2}g\), with \(g\) standard Gaussian in \(n=dN^2\) dimensions.
For every sufficiently large \(N\), the previous rank argument shows that
\[
 q_N(g)=|\det L_N(N^{-1/2}g)|^2
\]
is a nonzero nonnegative real polynomial of degree at most \(2mN\).
Its value at \(g=0\) may be zero.
Only nonidentity, not a nonzero value at the origin, is needed in the singular-zero-set extension and Gaussian tube bound (T4) of [v1](Yin_C_F0186_v1.md#tubes).

On the norm event, (BE-A) puts a point with \(s_{\min}(L_N)\le\varepsilon\) within distance \(C\sqrt N\varepsilon^\alpha\) of \(q_N^{-1}(0)\).
If that zero set is empty, the event is empty for the common small-residual threshold.
Otherwise (T4), with \(D\le2mN\), \(\sqrt n=\sqrt d\,N\), and tube radius \(C\sqrt N\varepsilon^\alpha\), gives (A).
A nonzero constant \(q_N\) is covered by the empty-set case.

Choose \(M>2\) and \(B\alpha>5/2\).
The GUE norm event has probability tending to one, and (A) at \(\varepsilon=N^{-B}\) gives (F).
In particular, the exponent does not deteriorate with the physical dimension \(N\).

<a id="logarithmic-tail"></a>
## Matrix-valued resolvent comparison and logarithmic tails

Put \(Q=L^*L\) and \(Q_N=L_N^*L_N\).
This is a fixed self-adjoint matrix-valued polynomial in the inputs.
CGP22 Corollary 1.3 applies with amplification size \(m\), deterministic coefficients \(A_0,\ldots,A_d\) and their adjoints, and a scalar noncommutative expression for \(Q_N\) using these deterministic matrix variables.
After the tensor-factor interchange, its free comparison is precisely \(Q\) under \(\tau_m\).
Absorbing the fixed \(m^2\) and coefficient norms in \(C\), it gives
\[
 |\mathbb E G_{Q_N}(z)-G_Q(z)|
 \le CN^{-2}\left((\Im z)^{-5}+(\Im z)^{-2}\right),
 \qquad \Im z>0,
 \tag{G}
\]
where all Cauchy transforms use their normalized traces and \(G(z)=\int(z-x)^{-1}\,d\nu(x)\).

SS15 Theorem 1.1(5)(6) supplies algebraicity and convergent local Puiseux expansions for \(G_Q\).
Its matrix-valued theorem does not assert absence of all atoms.
The required fact \(\nu(\{0\})=0\) follows here from \(u>-\infty\).
The bound \(|G_Q(it)|\le1/t\) excludes Puiseux powers below \(-1\), and \(itG_Q(it)\to\nu(\{0\})=0\) excludes a term of order \(-1\).
Therefore, for some \(0<\beta\le1\),
\[
 t|\Im G_Q(it)|\le Ct^\beta\quad(0<t\le1).
\]
This also covers a spectral gap at zero.
The kernel inequality \(1_{[0,t]}(x)\le2t^2/(x^2+t^2)\) and (G) imply
\[
 \mathbb E\nu_N([0,t])\le C\left(t^\beta+N^{-2}t^{-4}\right).
\]
Choose \(0<\gamma<2/(4+\beta)\).
For \(N^{-\gamma}\le t\le1\),
\[
 \mathbb E\nu_N([0,t])\le Ct^\beta.
 \tag{W}
\]

On the event \(E_N=\{s_{\min}(L_N)\ge N^{-B}\}\), all squared singular values are at least \(N^{-2B}\), and hence
\[
 \int_{(0,N^{-\gamma}]}|\log x|\,d\nu_N(x)
 \le 2B(\log N)\nu_N([0,N^{-\gamma}]).
\]
The expectation of the right side tends to zero by (W).
For \(N^{-\gamma}<x<\varepsilon<1\), the identity
\(-\log x=-\log\varepsilon+\int_x^\varepsilon dt/t\) and (W) give
\[
 \mathbb E\int_{(N^{-\gamma},\varepsilon)}|\log x|\,d\nu_N(x)
 \le C\varepsilon^\beta\left(1+|\log\varepsilon|\right).
\]
If \(N^{-\gamma}\) is below the singular-value floor, the first integral on \(E_N\) is empty and these bounds remain valid.
For all sufficiently large \(N\), exact singularity has probability zero by the generic-rank result.
Markov's inequality and \(\mathbb P(E_N^c)\to0\) now yield, for every \(\eta>0\),
\[
 \lim_{\varepsilon\downarrow0}\limsup_{N\to\infty}
 \mathbb P\left\{\int_{(0,\varepsilon)}|\log x|\,d\nu_N(x)>\eta\right\}=0.
 \tag{UI}
\]
No untruncated logarithmic expectation on \(E_N^c\) is used.

<a id="determinant-limit"></a>
## Removing the cutoff and normalization consequences

For fixed \(0<\varepsilon<1<R<\infty\), the bounded continuous truncation
\[
 f_{\varepsilon,R}(x)=\log\bigl(\min(R,\max(\varepsilon,x))\bigr),\qquad x\ge0,
\]
has convergent integrals under \(\nu_N\to\nu\) in probability.
Choose \(R\) larger than the norm bound for \(Q_N\) on a fixed GUE norm event of probability tending to one and larger than \(\|Q\|\).
There is then no upper truncation error on that event.
For \(x<\varepsilon<1\), the lower truncation error is bounded by \(|\log x|\), so (UI) removes it in probability.
The same Puiseux bound gives logarithmic integrability for the limiting measure at zero.
Consequently
\[
 U_N=\frac12\int\log x\,d\nu_N(x)
 \xrightarrow{\mathbb P}
 \frac12\int\log x\,d\nu(x)=u.
\]
Exponentiation proves the determinant conclusion for finite \(u\), and the earlier extended-real argument proves it when \(u=-\infty\).

If \(A_0\) is invertible, the factorization
\[
 L_N=(A_0\otimes I_N)
 \left(I_{mN}+\sum_j A_0^{-1}A_j\otimes H_j^{(N)}\right)
\]
explains the direct relation with the monic case.
Its deterministic normalized factor is \(|\det A_0|^{1/m}\), consistent with the ordinary free determinant convention.
For singular \(A_0\), the rank argument supplies what this normalization cannot.
Neither case requires irreducibility or nondegenerate one-step covariance.
The completely deterministic case \(A_1=\cdots=A_d=0\) also satisfies (D) directly, including singular \(A_0\).

<a id="comparison-scope"></a>
## Relation to the determinant-formula investigation

The finite-dimensional counterexamples in [L_F0060](../ledger/Yin_L_F0060_v1.md#comparison) remain valid: a finite-GUE capacity lower bound or deterministic-mean monotonicity does not follow from the corresponding free formula.
Those counterexamples concern finite-dimensional inequalities, not the probability limit proved here.
Any applicable established formula for \(\Delta_{\tau_m}(L)\) identifies the deterministic limit in (D).
The theorem does not upgrade the selected evidence for any particular variational formula.
The expectation lower bound and fractional inverse-determinant estimates discussed in L_F0060 are no longer necessary to prove (D), but are not proved by this probability convergence.

## Current assessment
[Selected decision](#decision-affine-reviewed)

## Assessment history

### Decision affine-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-04T17:56 |
| status | open |
| reason | The affine determinant extension is retained with its full rank, geometric and logarithmic argument; its additional statement and interfaces await a recorded review specific to this version. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Affine statement](#statement) | Arbitrary fixed constant matrices, extended-real logarithmic convergence, determinant-root convergence and the positive-determinant singular-value floor. |

### Decision affine-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-04T18:04 |
| status | proved |
| reason | The complete affine determinant argument has resolved inputs and a separate independent whole-proof finding for this exact version, including singular constant matrices, the zero-limit branch, the generic-rank step, geometric repair and logarithmic tails. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact affine statement](#statement) | Extended-real logarithmic convergence and normalized determinant convergence for every fixed affine GUE pencil, with the stated positive-determinant small-singular-value bounds. |
| argument | [Complete affine argument](#argument) | The zero-limit proof, rank regularity application, Hermitian repair, Gaussian tube estimate and matrix-valued logarithmic cutoff removal. |
| dependency | [Real polynomial distance input](Yin_C_F0186_v1.md#error-bound) | The stated real polynomial-map inequality and bounded-coordinate consequence, with its affine application supplied in this version. |
| dependency | [General Gaussian tube bound](Yin_C_F0186_v1.md#tubes) | Estimate (T4) and the regular-level extension for nonzero nonnegative polynomials, without assuming the affine polynomial is nonzero at the origin. |
| review | [Independent affine proof finding](../audits/reviews/Yin_R_F0190_v2.md#independent-affine-proof) | The exact statement, complete proof, declared inputs and selected v1 geometric dependencies; external theorem proofs are accepted at the stated inspection boundary. |
