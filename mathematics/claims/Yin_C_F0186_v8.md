---
author: Yin
---

# Almost-sure Brown limits for scalar polynomials in independent GOE matrices

This version records the real Gaussian extension within [the finite-variance F0012 question](../tasks/Yin_T_F0012_v3.md#contract).
The [reviewed real finite-variance carrier theorem](Yin_C_F0186_v7.md#decision-symmetric-carrier-reviewed) and all earlier fixed versions retain their statements, complete arguments and assessments at their exact scopes.
The present GOE statement has its own complete candidate argument and open assessment.
Its assembled real compression and logarithmic argument has not inherited an independent review from those earlier versions.
The full arbitrary-law finite-second-moment question remains outside this statement.

<a id="statement"></a>
## Exact GOE statement and auxiliary affine conclusion

Fix \(d\ge1\).
For each \(N\), let \(X_1^{(N)},\ldots,X_d^{(N)}\) be independent real symmetric normalized GOE matrices, with the [Sch05 variance convention](../audits/literature/Sch05/Yin_U001.md#gaussian-and-free-normalizations).
Within each matrix, the strict upper entries are independent \(N(0,1/N)\), the diagonal entries are independent \(N(0,2/N)\), and those families are independent.
All dimensions live on a common probability space with arbitrary cross-size coupling.
Let \(s_1,\ldots,s_d\) be free centered variance-one semicircular elements in a finite von Neumann algebra with faithful normal tracial state \(\tau\).

For every fixed scalar polynomial \(P\in\mathbb C\langle x_1,\ldots,x_d\rangle\), there is an event of probability one on which
\[
 \mu_N=\frac1N\sum_{k=1}^N\delta_{\lambda_k(P(X^{(N)}))}
 \Longrightarrow\mu_{P(s)}^{\mathrm{Br}}
 \tag{GOE-Brown}
\]
against every bounded continuous real function on \(\mathbb C\).
Eigenvalues are counted with algebraic multiplicity.
The polynomial need not be selfadjoint.
The event may depend on the fixed polynomial and coupling.

For every nonconstant \(P\) and fixed \(z\ne P(0)\), the following finite logarithmic limit also holds almost surely:
\[
 \frac1N\log|\det(P(X^{(N)})-zI_N)|
 \longrightarrow\log\Delta_\tau(P(s)-z)\in\mathbb R.
 \tag{GOE-fixed-log}
\]
Its event may depend on \(z\).
The excluded fixed parameter is not needed in the planar potential proof of (GOE-Brown).
For a constant \(P=c\), its spectral conclusion and determinant identity are deterministic, with \(\log|c-z|=-\infty\) when \(z=c\).

The proof also establishes the following auxiliary fixed-pencil assertion.
For fixed \(m\ge1\) and \(A_0,\ldots,A_d\in M_m(\mathbb C)\), assume \(A_0\) invertible and
\[
 L=A_0\otimes1+\sum_jA_j\otimes s_j,\qquad
 u=\log\Delta_{\tau_m}(L)>-\infty,\qquad
 \tau_m=\operatorname{tr}_m\otimes\tau.
\]
Then, with \(L_N=A_0\otimes I_N+\sum_jA_j\otimes X_j^{(N)}\),
\[
 \frac1{mN}\log|\det L_N|\longrightarrow u
 \quad\text{almost surely}.
 \tag{GOE-affine}
\]
This assertion retains the invertible-constant and finite-free-log hypotheses.
Every finite determinant and free determinant here is ordinary, with \(\log0=-\infty\).

## Exact proof inputs and source limits

- [Sch05-U001](../audits/literature/Sch05/Yin_U001.md#sch05-u001) supplies the exact affine Hermitian real-Ginibre resolvent comparison, including its GOE variance normalization and fixed matrix amplification.
  The source is Schultz, arXiv:math/0308192v1, Theorem 3.2, equation (3.6), PDF p. 15.
  Its retained statement and actual application were checked; the underlying Haagerup--Thorbjornsen and master-equation proofs were not newly audited in full.
- [C_F0186_v1](Yin_C_F0186_v1.md#argument) supplies the accepted real polynomial-map error-bound input, Gaussian algebraic tube bound with its singular-level extension, exact word-chain linearization, and the recorded SS15 scalar input.
  The real-coordinate compression is supplied completely below.
- [C_F0186_v2](Yin_C_F0186_v2.md#logarithmic-tail) supplies the exact SS15 matrix-valued algebraicity and convergent local Puiseux interface.
  Its GUE resolvent estimate is not used in this proof.
- [C_F0186_v3](Yin_C_F0186_v3.md#argument) supplies the singular-value Frobenius inequality, the accepted Gaussian Lipschitz concentration input and bounded FK block-factorization interface.
  The GOE coordinate scaling and its consequences are derived below.
- [C_F0186_v4](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) supplies fixed-polynomial Hermitized weak convergence, pathwise local planar potential bounds and tightness at the actual real Gaussian input law.

The source algebraicity and atomlessness inputs use SS15 arXiv:1305.1920v1, Theorem 1.1(5)(6) on PDF pp. 1--2 and Corollary 1.2 on PDF p. 3, at the recorded exact inspected scopes.
Matrix-valued atomlessness is not assumed.
The main quantitative comparison is applied to an affine Hermitization, so no general-polynomial GOE comparison theorem is needed.
This is a project deduction without a novelty or priority claim.

<a id="argument"></a>
## Complete GOE argument

Use \(X_{\mathrm O,j}^{(N)}=X_j^{(N)}\) throughout.
For every Hermitian finite matrix \(K\), write \(G_K(w)\) for its resolvent trace \(\operatorname{tr}(wI-K)^{-1}\), with the normalized trace of its full dimension.
For a free Hermitian operator use the corresponding normalized tracial Cauchy transform.
<a id="goe-affine-input"></a>
### Exact Schultz model match for an affine pencil

Fix
\[
 L_N=A_0\otimes I_N+\sum_{j=1}^d A_j\otimes X_{\mathrm O,j}^{(N)},
 \qquad
 L=A_0\otimes1+\sum_{j=1}^d A_j\otimes s_j,
\]
where \(A_j\in M_m(\mathbb C)\), \(m,d\) and the coefficients are fixed, and \(\tau_m=\operatorname{tr}_m\otimes\tau\).
For the logarithmic argument assume \(A_0\) invertible and
\[
 u=\log\Delta_{\tau_m}(L)>-\infty.
 \tag{Finite-free-log}
\]
The Gaussian real-compression floor below applies because multiplication by \(A_0^{-1}\) reduces the pencil to a monic one.
Its Hermitization is
\[
 \mathcal H_N=
 \begin{pmatrix}0&L_N\\L_N^*&0\end{pmatrix}
 =B_0\otimes I_N+\sum_j B_j\otimes X_{\mathrm O,j}^{(N)},
 \quad
 B_j=\begin{pmatrix}0&A_j\\A_j^*&0\end{pmatrix}.
\]
Every \(B_j\) is Hermitian, including the analogous \(B_0\).

Let \(Y_j^{(N)}\) have independent real \(N(0,1/N)\) entries.
Then
\[
 X_{\mathrm O,j}^{(N)}=(Y_j^{(N)}+Y_j^{(N)T})/\sqrt2
\]
has the required GOE law, including diagonal variance \(2/N\).
Apply the [exact source specialization](../audits/literature/Sch05/Yin_U001.md#goe-hermitization-specialization) with \(a_0=0\), \(a_j=B_j/\sqrt2\), and \(\lambda=itI_{2m}-B_0\).
Its imaginary part is \(tI_{2m}>0\), and the resolvent is exactly \((itI-\mathcal H_N)^{-1}\); the constant term is included once through \(\lambda\).
The [free normalization](../audits/literature/Sch05/Yin_U001.md#gaussian-and-free-normalizations) has independent circular \(y_j\), and \((y_j+y_j^*)/\sqrt2\) are independent variance-one semicircular elements, so its resolvent is exactly that of
\[
 \mathcal H=\begin{pmatrix}0&L\\L^*&0\end{pmatrix}.
\]
Taking normalized auxiliary trace of the source's matrix-valued resolvent estimate gives, for \(0<t\le1\),
\[
 \left|\mathbb E G_{\mathcal H_N}(it)-G_{\mathcal H}(it)\right|
 \le \frac C N(t^{-7}+t^{-5}).
 \tag{Schultz-comparison}
\]
All random coefficients and the auxiliary size are fixed.
For a deterministic constant family \(B_0(z)\) bounded on a compact parameter set, the source estimate is uniform there because only \(\lambda=itI-B_0(z)\) varies within its stated domain.
This use requires no quantitative theorem for a higher-degree polynomial and does not replace the source's affine hypothesis by one.

<a id="goe-mesoscopic-count"></a>
### A shrinking singular-value count from the exact affine input

Let \(\nu_N\) and \(\nu\) be the normalized laws of \(|L_N|\) and \(|L|\).
The symmetric Hermitization law has zero atom at zero by (Finite-free-log).
SS15 arXiv:1305.1920v1, Theorem 1.1(5)(6), applies to the selfadjoint matrix-valued polynomial \(\mathcal H\), supplying algebraicity and a convergent local Puiseux expansion of its Cauchy transform.
As in [the accepted matrix-valued interface](../claims/Yin_C_F0186_v2.md#logarithmic-tail), the bound \(|G(it)|\le1/t\) excludes powers below \(-1\), and absence of the zero atom excludes a pole of order one.
Hence for some \(0<\beta\le1\),
\[
 C_\infty(t):=t|\Im G_{\mathcal H}(it)|\le Ct^\beta,
 \qquad 0<t\le1.
\]
Define
\[
 c_t(s)=\frac{t^2}{s^2+t^2},\qquad
 C_N(t)=\frac1{mN}\sum_{k=1}^{mN}c_t(s_k(L_N)).
\]
The two Hermitization eigenvalues corresponding to \(s_k\) are \(s_k,-s_k\), so the normalization is exactly
\[
 \mathbb E C_N(t)=t|\Im\mathbb E G_{\mathcal H_N}(it)|.
\]
In particular \(\nu_N([0,t])\le2C_N(t)\).
Multiplying (Schultz-comparison) by \(t\) gives
\[
 \mathbb E\nu_N([0,t])
 \le C\bigl(t^\beta+N^{-1}t^{-6}\bigr).
 \tag{GOE-count}
\]
Choose
\[
 0<\gamma<\frac1{6+\beta},\qquad t_N=N^{-\gamma}.
\]
For \(t_N\le t\le1\), the comparison error is bounded by a constant times \(t^\beta\), so
\[
 \mathbb E\nu_N([0,t])\le C't^\beta.
 \tag{GOE-mesoscopic}
\]
This supplies exactly the shrinking-scale interface left open in the retained real-Gaussian route.

<a id="goe-concentration"></a>
### Gaussian concentration at the moving cutoff

In real Hilbert--Schmidt orthonormal coordinates of the real symmetric matrices, GOE is \(\sqrt{2/N}\,g\), with \(g\) standard Gaussian.
Set \(\kappa_A^2=\sum_j\|A_j\|_{\mathrm{HS}}^2\).
The tensor Hilbert--Schmidt inequality gives
\[
 \|L_N(g)-L_N(g')\|_{\mathrm{HS}}
 \le \sqrt{2/N}\,\kappa_A\|g-g'\|_2.
\]
The [accepted singular-value Frobenius inequality](../claims/Yin_C_F0186_v3.md#singular-value-perturbation) implies that for an \(L_h\)-Lipschitz \(h\),
\[
 \operatorname{Lip}\!\left(\frac1{mN}\sum_k h(s_k(L_N(g)))\right)
 \le \sqrt{2/m}\,\kappa_A L_h/N.
\]
Thus the same accepted Gaussian concentration input gives
\[
 \mathbb P\{|\Phi_{N,h}-\mathbb E\Phi_{N,h}|>a\}
 \le2\exp[-c_A N^2a^2/L_h^2].
 \tag{GOE-GC}
\]
The extra GOE coordinate variance changes a constant only.
The deterministic case \(\kappa_A=0\) is immediate.

Since \(\|c_t'\|_\infty\le2/t\), use \(a=t_N^\beta\) and (GOE-mesoscopic) in (GOE-GC).
The resulting bound is
\[
 2\exp[-cN^{\,2-2\gamma(1+\beta)}],
\]
which is summable because \(\gamma<1/(6+\beta)\).
First Borel--Cantelli yields
\[
 \nu_N([0,t_N])\le C N^{-\gamma\beta}
 \quad\text{eventually almost surely}.
 \tag{GOE-mass-AS}
\]
No independence between sizes is used.

<a id="goe-real-floor"></a>
### Summable real Gaussian floor for the monic pencil

Normalize the constant-invertible pencil by \(A_0^{-1}\), and write
\[
 T_N=I_m\otimes I_N+\sum_j R_j\otimes X_{\mathrm O,j}^{(N)}.
\]
Fix a norm cutoff \(M\) large enough that the Gaussian norm-tail bound below is summable.
The realification in [L_F0061_v1](../ledger/Yin_L_F0061_v1.md#real-gaussian-monic-route) can be checked directly as follows.
For a complex unit near-kernel vector \(v=(v_1,\ldots,v_m)\), let
\[
 W_{\mathbb R}=\operatorname{span}_{\mathbb R}
 \{\Re v_a,\Im v_a:1\le a\le m\},
 \qquad k\le2m,
\]
and let the real output space be
\[
 W_{\mathrm{out},\mathbb R}
 =\sum_j P_{W_{\mathbb R}^\perp}X_{\mathrm O,j}W_{\mathbb R},
 \qquad \ell\le dk.
\]
Take real isometries \(U,V\) onto these mutually orthogonal spaces.
Then \(C_j=U^TX_{\mathrm O,j}U\) are real symmetric, \(B_j=V^TX_{\mathrm O,j}U\) are real, and \(w_a=U^Tv_a\) remain complex.
The exact identity \(X_{\mathrm O,j}U=UC_j+VB_j\) gives the inside and outside residual equations
\[
 w+\sum_j(R_j\otimes C_j)w,\qquad
 \sum_j(R_j\otimes B_j)w.
\]
Their real and imaginary parts, together with \(\|w\|^2-1\), form a quadratic real polynomial map in at most
\[
 d\,k(k+1)/2+d\ell k+2mk
\]
real coordinates.
On the fixed norm event its coordinate vector ranges over a bounded set independent of \(N\).
There are finitely many \((k,\ell)\) types, depending only on \(m,d\).

The exact real polynomial-map error bound already used in [C_F0186_v1](../claims/Yin_C_F0186_v1.md#error-bound) therefore gives a fixed exponent \(\alpha>0\) and bounded-coordinate perturbations of size \(O(\varepsilon^\alpha)\) to an exact zero whenever the residual is at most \(\varepsilon\).
Types whose zero set is empty have a positive minimum residual on the compact coordinate set and are excluded once \(\varepsilon\) is sufficiently small.
For a nonempty type, lift the corrected blocks by
\[
 \delta X_j=U\delta C_jU^T+
           V\delta B_jU^T+U\delta B_j^TV^T.
\]
This is real symmetric and has the same dimension-independent Hilbert--Schmidt control as the complex compression.
The corrected coordinate vector has norm one and gives an exact kernel vector for the corrected pencil.
Consequently the small-value event on the norm cutoff lies within Hilbert--Schmidt distance \(C\varepsilon^\alpha\) of the real symmetric singular-input set.

The standard real Gaussian coordinates have dimension \(dN(N+1)/2\), and multiplication by \(\sqrt{2/N}\) turns that distance into \(C\sqrt N\,\varepsilon^\alpha\).
The determinant polynomial \(|\det T_N|^2\) has degree at most \(2mN\) and value one at zero.
It is nonzero on this real coordinate space for every \(N\).
The [accepted degree-controlled Gaussian tube bound](../claims/Yin_C_F0186_v1.md#tubes), including its singular-level extension, thus gives
\[
 \mathbb P\{s_{\min}(T_N)\le\varepsilon,\ \max_j\|X_{\mathrm O,j}\|\le M\}
 \le C N^{5/2}\varepsilon^\alpha
          e^{C N^{5/2}\varepsilon^\alpha}+e^{-cN^2}
\]
for sufficiently small \(\varepsilon\).
Empty singular sets are handled by the corresponding empty-tube case, exactly as in that bound.

For completeness, for every unit complex \(v\), the real Gaussian \(v^*X_{\mathrm O,j}v\) has variance at most \(2/N\).
A \(1/4\)-net of the complex unit sphere has size at most \(9^{2N}\), and its maximum quadratic form controls half the Hermitian operator norm.
The scalar Gaussian tail therefore gives
\[
 \mathbb P\{\|X_{\mathrm O,j}\|>2r\}
 \le2\exp(2N\log9-Nr^2/4).
\]
For a fixed sufficiently large cutoff \(M\), this is exponentially summable; it also yields uniform operator-norm moments of every fixed order.
Take \(\varepsilon=N^{-B_0}\) with \(B_0\alpha>7/2\).
The tube term and norm failure are summable, hence
\[
 s_{\min}(L_N)\ge N^{-B}
 \quad\text{eventually almost surely}
 \tag{GOE-floor}
\]
for an appropriate fixed \(B\), after restoring \(A_0\).
Increasing \(B\) if necessary preserves the assertion.

<a id="goe-logarithmic-limit"></a>
### Complete affine logarithmic limit at a finite free value

Put
\[
 U_N=\frac1{mN}\log|\det L_N|,\qquad
 V_N(t)=\frac1{mN}\sum_k\log\max(s_k(L_N),t).
\]
The clipped logarithm is \(1/t\)-Lipschitz.
At \(t=t_N\), (GOE-GC) at each fixed deviation has summable bound \(2e^{-cN^{2-2\gamma}a^2}\).
A countable intersection therefore gives
\[
 V_N(t_N)-\mathbb EV_N(t_N)\longrightarrow0
 \quad\text{almost surely}.
\]
For fixed \(\varepsilon>0\), the accepted finite-variance Hermitized weak limit applies to GOE and \(L_N^*L_N\).
The Gaussian norm moments make its clipped positive logarithm uniformly integrable, so
\[
 \mathbb EV_N(\varepsilon)\longrightarrow
 v(\varepsilon)=\int\log\max(s,\varepsilon)\,d\nu(s).
\]
For \(t_N<\varepsilon<1\), layer integration gives
\[
 V_N(\varepsilon)-V_N(t_N)
 =\int_{t_N}^{\varepsilon}\nu_N([0,t))\,dt/t.
\]
By (GOE-mesoscopic), its expectation is at most \(C\varepsilon^\beta\).
Since \(v(\varepsilon)\downarrow u\), this proves \(\mathbb EV_N(t_N)\to u\), and hence \(V_N(t_N)\to u\) almost surely.

Choose the floor exponent \(B>\gamma\).
On the eventual floor,
\[
 0\le V_N(t_N)-U_N
 \le B(\log N)\nu_N([0,t_N]).
\]
The right side tends to zero by (GOE-mass-AS).
Thus
\[
 \frac1{mN}\log|\det L_N|
 \longrightarrow\log\Delta_{\tau_m}(L)
 \quad\text{almost surely}
 \tag{GOE-affine-log}
\]
for every fixed constant-invertible pencil with (Finite-free-log), under arbitrary cross-size coupling.
The proof makes no expectation-convergence assertion for unregularized logarithms.

<a id="goe-scalar-brown"></a>
### Word-chain linearization and the original GOE Brown conclusion

Let \(P\) be a fixed nonconstant scalar polynomial and \(z\ne P(0)\).
Use the exact [word-chain pencil](../claims/Yin_C_F0186_v1.md#polynomial-application) \(L_P(z)\) of fixed auxiliary size \(q\).
Its constant matrix is \(\operatorname{diag}(P(0)-z,1,\ldots,1)\), which is invertible.
Its finite determinant is exactly \(\det(P(X_{\mathrm O}^{(N)})-zI)\), and its triangular auxiliary block has a polynomial inverse.
The [bounded FK block factorization](../claims/Yin_C_F0186_v3.md#linearization-transfer) gives
\[
 q\log\Delta_{\tau_q}(L_P(z;s))
 =\log\Delta_\tau(P(s)-z).
\]

The scalar selfadjoint polynomial \(Q_z=(P-z)^*(P-z)\) is nonconstant, because its highest homogeneous part is \(P_D^*P_D\ne0\).
The scalar atomlessness input is SS15 Corollary 1.2, arXiv:1305.1920v1 PDF p. 3, at the accepted scope used in [C_F0186_v1](../claims/Yin_C_F0186_v1.md#polynomial-application) and directly rechecked in the parallel source preparation.
Together with its algebraic/Puiseux input, this gives a bound \(\mu_{Q_z(s)}([0,t])\le C_z t^{\beta_z}\) for some \(\beta_z>0\), hence a finite logarithmic integral at zero by integration of \(t^{\beta_z-1}\).
Thus the free scalar logarithm, and consequently the free affine logarithm of \(L_P(z;s)\), are finite.
This does not invoke matrix-valued atomlessness.

Applying (GOE-affine-log) and multiplying the normalization by \(q\) proves
\[
 \frac1N\log|\det(P(X_{\mathrm O}^{(N)})-zI)|
 \longrightarrow\log\Delta_\tau(P(s)-z)
 \quad\text{almost surely for each fixed }z\ne P(0).
 \tag{GOE-pointwise}
\]
All random potentials and their parameter dependence are measurable.
Fubini on countably many disks gives one event of planar almost-everywhere convergence, because the excluded point \(P(0)\) has planar measure zero.
The [accepted finite-variance local planar \(L^2\) controls and tightness](../claims/Yin_C_F0186_v4.md#statement) apply to this very GOE model and polynomial.
They upgrade the convergence to local planar \(L^1\), identify the distributional Laplacian with the limiting Brown measure, and yield weak convergence of probability measures.
Hence on one event of probability one,
\[
 \mu_{P(X_{\mathrm O}^{(N)})}\Longrightarrow
 \mu_{P(s)}^{\mathrm{Br}}
\]
against every bounded continuous real test function on the plane, under every permitted cross-size coupling.

The fixed exceptional determinant parameter \(z=P(0)\) is not asserted in (GOE-pointwise).
The real odd-dimensional commutator obstruction retained in L_F0061_v1 shows why an unrestricted all-affine real-Gaussian floor cannot be silently substituted.
The Brown conclusion itself omits no test function or spectral mass: it uses only the legitimate planar-null exceptional parameter in its potential proof.
No arbitrary finite-variance extension beyond the GOE law is established here.


## Current assessment

[Selected decision](#decision-goe-candidate)

## Assessment history

### Decision goe-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:00 |
| status | open |
| reason | The complete GOE Brown and restricted logarithmic statements, real compression floor, exact Schultz specialization and one-event planar passage are fixed for independent review; earlier reviews retain their actual input scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact GOE and affine assertions](#statement) | All fixed scalar GOE polynomials under arbitrary cross-size coupling, the one-event Brown conclusion, fixed logarithmic limits away from P(0), and the stated constant-invertible finite-free-log affine assertion. |
| argument | [Complete GOE proof](#argument) | Exact real-Ginibre specialization, Puiseux singular count, GOE Gaussian concentration, full real compression and tube floor, moving clipped logarithm, word-chain transfer and planar identification. |
| dependency | [Exact real-Gaussian source](../audits/literature/Sch05/Yin_U001.md#sch05-u001) | Schultz Theorem 3.2 at its accepted exact arXiv v1 scope, used only for the displayed affine Hermitization with strictly positive imaginary parameter. |
| dependency | [Repair, tubes and word-chain inputs](Yin_C_F0186_v1.md#argument) | Only the polynomial-map error bound, general Gaussian tube lemma, word-chain identities and accepted SS15 scalar source interface; the real compression is established in this version. |
| dependency | [Matrix-valued Puiseux interface](Yin_C_F0186_v2.md#logarithmic-tail) | Only the accepted SS15 selfadjoint matrix-polynomial algebraicity and Puiseux statement, with zero atom excluded here by finite free logarithm. |
| dependency | [Perturbation, concentration and FK inputs](Yin_C_F0186_v3.md#argument) | Singular-value Frobenius perturbation, accepted Gaussian concentration and bounded free block determinant identity; GOE coordinate changes are supplied here. |
| dependency | [Finite-variance planar controls](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Hermitized weak convergence, local planar L2 potential control and tightness for the exact fixed-law GOE model and polynomial. |
