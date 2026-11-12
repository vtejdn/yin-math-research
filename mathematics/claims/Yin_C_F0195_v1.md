---
author: Yin
---

# Shrinking singular-value counts for fixed Wigner pencils under third moments

This Claim supplies the shrinking singular-value count premise for the direct Hermitization route in [F0012](../tasks/Yin_T_F0012_v3.md#contract).
The proof was developed jointly by the main and delegated authoring agents and has received [independent whole-proof review](../audits/reviews/Yin_R_F0201_v1.md#wigner-count-whole-proof), adopted below.
It does not assert a least-singular-value floor or the full Wigner Brown-measure theorem.

<a id="statement"></a>
## Affine comparison and count

Let the fixed Wigner laws satisfy \(\mathbb E\xi_j=0\), \(\mathbb E|\xi_j|^2=1\), \(\mathbb E|\xi_j|^3<\infty\), and \(\mathbb E\zeta_j=0\), \(\mathbb E\zeta_j^2<\infty\), with the within-size independence of the Task.
Complex \(\xi_j\), degenerate real two-coordinate covariance, and dependence of real and imaginary parts are allowed.
Let \(B_0,\ldots,B_d\in M_p(\mathbb C)\) be fixed Hermitian matrices, and define
\[
 H_n=B_0\otimes I_n+\sum_{j=1}^dB_j\otimes W_j^{(n)},
 \qquad H=B_0\otimes1+\sum_{j=1}^dB_j\otimes s_j.
\]
For normalized GOE inputs \(X_j^{(n)}\), with upper variance \(1/n\) and diagonal variance \(2/n\), write \(H_n^{\mathrm O}=B_0\otimes I_n+\sum_jB_j\otimes X_j^{(n)}\).
Use normalized full trace in
\[
 G_T(w)=\frac1{pn}\operatorname{Tr}(wI-T)^{-1}
\]
for finite \(pn\)-dimensional \(T\), and the corresponding \(\operatorname{tr}_p\otimes\tau\) in the free expression.
The comparison is
\[
 |\mathbb EG_{H_n}(i\eta)-\mathbb EG_{H_n^{\mathrm O}}(i\eta)|
 \le C\bigl(n^{-1/2}\eta^{-4}+n^{-1}\eta^{-3}\bigr),
 \qquad \eta>0.
 \tag{Wigner-GOE}
\]
The constant depends on the fixed coefficients, number of inputs, third off-diagonal moments and second diagonal moments, not on \(n\) or \(\eta\).
In particular it is uniform over a varying deterministic \(B_0\) at this comparison step.

Now take any fixed affine pencil
\[
 L_n=A_0\otimes I_n+\sum_jA_j\otimes W_j^{(n)},
 \qquad L=A_0\otimes1+\sum_jA_j\otimes s_j,
 \qquad A_j\in M_m(\mathbb C),
\]
and assume \(\log\Delta_{\operatorname{tr}_m\otimes\tau}(L)>-\infty\).
No invertibility of \(A_0\) is needed for the counting assertion.
For the singular-value law \(\nu_n=(mn)^{-1}\sum_i\delta_{s_i(L_n)}\), the consequence is
\[
 \mathbb E\nu_n([0,t])
 \le C\bigl(t^\beta+n^{-1/2}t^{-3}+n^{-1}t^{-6}\bigr),
 \qquad 0<t\le1,
 \tag{Affine-count}
\]
for some \(0<\beta\le1\).
For every \(0<\gamma<1/(6+2\beta)\), this implies
\[
 \mathbb E\nu_n([0,t])\le C't^\beta,
 \qquad n^{-\gamma}\le t\le1.
 \tag{Shrinking-count}
\]
The constants and exponents can depend on the fixed pencil.
The conclusions depend only on each within-size law and impose no restriction on coupling between sizes.

For every fixed nonconstant scalar polynomial \(P\) in the selfadjoint inputs and every fixed \(z\ne P(0)\), the squared-singular-value law \(\rho_{n,z}\) of \(P(W^{(n)})-zI_n\) consequently satisfies
\[
 \mathbb E\rho_{n,z}([0,x])\le C_zx^{\beta_z/2},
 \qquad n^{-2\gamma_z}\le x\le1,
\]
for suitable fixed \(C_z,\beta_z,\gamma_z>0\).
The [polynomial transfer](#polynomial-transfer) gives the precise deterministic implication and its finite free logarithm input.

## Current assessment
[Selected decision](#decision-count-reviewed)

## Assessment history

### Decision count-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-11T13:29 |
| status | open |
| reason | The complete candidate comparison and count proof is retained for independent checking at this exact scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Affine resolvent comparison, shrinking singular counts and their scalar-polynomial consequence under third off-diagonal and second diagonal moments. |
| argument | [Complete argument](#argument) | Coordinate replacement, Gaussian covariance interpolation, GOE comparison and deterministic Schur-count transfer. |
| dependency | [GOE affine comparison and free power bound](Yin_C_F0186_v8.md#goe-affine-input) | The affine Schultz estimate and following mesoscopic-count section, at their stated normalization. |
| dependency | [Exact scalar word-chain pencil](Yin_C_F0186_v1.md#polynomial-application) | Everywhere invertible triangular auxiliary block and exact Schur complement. |
| dependency | [Free polynomial logarithm](Yin_C_F0186_v8.md#goe-scalar-brown) | Free scalar atomlessness, algebraic edge behavior and the finite-log pencil factorization only. |

<a id="sources"></a>

### Decision count-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-11T13:37 |
| status | proved |
| reason | Independent whole-proof inspection supports the exact comparison and shrinking-count statement, all complex covariance cases, the diagonal moment scope and the polynomial transfer with their fixed source interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Affine resolvent comparison, shrinking singular counts and their scalar-polynomial consequence under third off-diagonal and second diagonal moments. |
| argument | [Complete argument](#argument) | Coordinate replacement, Gaussian covariance interpolation, GOE comparison and deterministic Schur-count transfer. |
| dependency | [GOE affine comparison and free power bound](Yin_C_F0186_v8.md#goe-affine-input) | The affine Schultz estimate and following mesoscopic-count section, at their stated normalization. |
| dependency | [Exact scalar word-chain pencil](Yin_C_F0186_v1.md#polynomial-application) | Everywhere invertible triangular auxiliary block and exact Schur complement. |
| dependency | [Free polynomial logarithm](Yin_C_F0186_v8.md#goe-scalar-brown) | Free scalar atomlessness, algebraic edge behavior and the finite-log pencil factorization only. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0201_v1.md#wigner-count-whole-proof) | Entire statement and argument, all declared dependencies and source interfaces, normalization and moment/complex-law boundaries. |

## Sources and exact reuse

The existing [GOE proof module C186v8](../claims/Yin_C_F0186_v8.md#goe-affine-input), covered together with v9 by its [adopted complete GOE finding](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed), supplies the affine Schultz comparison and its normalization.
Its [small-mass section](../claims/Yin_C_F0186_v8.md#goe-mesoscopic-count) supplies the accepted matrix-valued algebraic/Puiseux implication from a finite free logarithm to a power bound at zero.
The original external inputs and their reading limits remain at [Sch05-U001](../audits/literature/Sch05/Yin_U001.md#goe-hermitization-specialization) and the fixed Claim's SS15 interface.
No general-polynomial GOE comparison is assumed.

The replacement and interpolation mechanisms are established methods, inspected here in Chatterjee, [arXiv:math/0508519v3](https://arxiv.org/pdf/math/0508519v3), Theorem 1.1 on PDF p. 2, its Taylor replacement proof in Section 2 on pp. 5--6, Gaussian interpolation and integration by parts in Section 3, equation (13) and its continuation on pp. 10--11, and the resolvent derivatives in Section 4 on pp. 14--15.
This source is attribution for the methods implemented explicitly below, rather than a claim that its scalar exchangeable-matrix theorem directly states the present fixed matrix-coefficient result.
The selected statement and displayed proof passages were read; no whole-source audit is claimed.
The real two-coordinate replacement, low-moment diagonal treatment, covariance cancellation and polynomial count transfer are specified below at their actual scope.

<a id="argument"></a>
<a id="derivative-bound"></a>
## Uniform derivatives of a normalized affine resolvent

Fix all input coordinates except one physical entry pair and write \(R=(i\eta I-H_n)^{-1}\).
For a real direction with Hermitian perturbation matrix \(D\), differentiation gives
\[
 \frac{d^r}{du^r}\frac1{pn}\operatorname{Tr}(i\eta I-H_n-uD)^{-1}
 =\frac{r!}{pn}\operatorname{Tr}\bigl(R_u(DR_u)^r\bigr).
\]
Every \(H_n+uD\) is Hermitian, so \(\|R_u\|\le\eta^{-1}\) uniformly for real \(u\).
If \(D\) is a change of one raw off-diagonal entry in input \(j\), its rank is at most \(2p\) and its norm is at most \(\|B_j\|\,|h|/\sqrt n\), where \(h\in\mathbb C\) is the raw direction.
The trace bound \(|\operatorname{Tr}T|\le\operatorname{rank}(T)\|T\|\) therefore gives
\[
 |D_h^rG_{H_n}(i\eta)|
 \le 2r!\|B_j\|^r|h|^r n^{-1-r/2}\eta^{-r-1},
 \qquad r\ge1.
 \tag{Pair-derivative}
\]
A diagonal direction has rank at most \(p\) and obeys the same inequality without the factor two.
These bounds are uniform in the other entries and all intermediate replacement matrices.
They do not require norm bounds on those matrices or on the entry values.

<a id="diagonal-removal"></a>
## Finite second moments suffice on the diagonal

Temporarily replace every raw diagonal variable by zero.
For one centered raw diagonal \(\zeta_j\), first-order Taylor expansion at zero has a remainder bounded by
\[
 \frac12\sup_u|f''(u)|\,|\zeta_j|^2
 \le C\|B_j\|^2n^{-2}\eta^{-3}|\zeta_j|^2.
\]
The linear term vanishes after conditional expectation, since the entry is centered and independent of the other coordinates.
Summing over the \(dn\) diagonal coordinates bounds the resolvent expectation change by \(Cn^{-1}\eta^{-3}\).
The same estimate inserts the independent GOE diagonal coordinates of raw variance two at the end.
No matching diagonal variances and no diagonal third moments are needed.
For the next two steps all diagonals are zero.

<a id="pair-replacement"></a>
## Joint replacement of each complex entry by its covariance-matched Gaussian

For input \(j\), let \(Z_j\in\mathbb C\) be centered Gaussian as a real two-dimensional vector, with the same real covariance matrix as \(\xi_j\).
Allow this covariance to be singular.
Thus \(\mathbb E|Z_j|^2=1\), \(\mathbb EZ_j^2=\mathbb E\xi_j^2\), and \(\mathbb E|Z_j|^3\) has a universal finite bound.
Replace the independent complex upper entries one pair at a time by independent copies of \(Z_j\), replacing their lower conjugates simultaneously.

Apply multivariate Taylor expansion through degree two at the zero entry pair.
Equivalently, expand along the real line \(u\mapsto u\xi_j\) and retain its linear and quadratic forms in \((\operatorname{Re}\xi_j,\operatorname{Im}\xi_j)\).
Their conditional expectations agree with those of the Gaussian pair because means and the full two-coordinate covariance agree.
The degree-three remainder is bounded by (Pair-derivative), giving a one-pair expectation error at most
\[
 C\|B_j\|^3n^{-5/2}\eta^{-4}
   (\mathbb E|\xi_j|^3+\mathbb E|Z_j|^3).
\]
Summing the \(dn(n-1)/2\) replacements gives an error \(Cn^{-1/2}\eta^{-4}\).
This replacement is joint within each entry pair, so it assumes no independence of real and imaginary parts.

<a id="covariance-interpolation"></a>
## Removing the Gaussian pseudocovariance by a trace cancellation

It remains to compare the zero-diagonal Gaussian model just obtained with zero-diagonal GOE.
For each input write \(c_j=\mathbb EZ_j^2\), so \(|c_j|\le1\).
Interpolate its independent upper pairs by
\[
 Z_{j,ab}(\theta)=\sqrt\theta Z_{j,ab}
                 +\sqrt{1-\theta}\,g_{j,ab},
 \qquad 0\le\theta\le1,
\]
where all real \(g_{j,ab}\) are independent standard Gaussians, independent of all \(Z\).
The resulting matrices are Hermitian for every \(\theta\).
In each pair the real covariance difference from GOE is
\[
 \Delta\Sigma_{xx}=(\operatorname{Re}c_j-1)/2,
 \quad\Delta\Sigma_{yy}=(1-\operatorname{Re}c_j)/2,
 \quad\Delta\Sigma_{xy}=\operatorname{Im}c_j/2.
\]

Use physical \(p\)-by-\(p\) blocks after the canonical tensor-factor permutation.
Here \(\operatorname{Tr}_p\) is the unnormalized block trace, whereas \(\operatorname{tr}_p\) above is normalized.
For \(a<b\), let \(X=E_{ab}\otimes B_j\), \(Y=E_{ba}\otimes B_j\), and \(F(H)=(pn)^{-1}\operatorname{Tr}(i\eta I-H)^{-1}\).
The unnormalized real and imaginary pair directions are \(X+Y\) and \(i(X-Y)\).
The Hessian may be complexified algebraically at the Hermitian base matrix; the actual interpolation path remains Hermitian.
The covariance contraction is exactly
\[
 \Delta\Sigma_{xx}D_{X+Y}^2F
 +2\Delta\Sigma_{xy}D_{X+Y}D_{i(X-Y)}F
 +\Delta\Sigma_{yy}D_{i(X-Y)}^2F
 =(c_j-1)D_X^2F+(\overline c_j-1)D_Y^2F.
 \tag{Covariance-cancellation}
\]
The mixed \(D_XD_Y\) term disappears because the total entry variance agrees.

For \(R=(i\eta I-H)^{-1}\), the first of these second derivatives is
\[
 D_X^2F=\frac2{pn}\operatorname{Tr}(RXRXR)
       =\frac2{pn}\operatorname{Tr}(XRXR^2)
       =\frac2{pn}\operatorname{Tr}_p\bigl(B_jR_{ba}B_j(R^2)_{ba}\bigr).
\]
Consequently, for each input \(j\),
\[
 \sum_{a<b}|D_X^2F|
 \le\frac{2\|B_j\|^2}{pn}
      \left(\sum_{a<b}\|R_{ba}\|_{\mathrm{HS}}^2\right)^{1/2}
      \left(\sum_{a<b}\|(R^2)_{ba}\|_{\mathrm{HS}}^2\right)^{1/2}
 \le\frac{2\|B_j\|^2}{pn}\|R\|_{\mathrm{HS}}\|R^2\|_{\mathrm{HS}}
 \le2\|B_j\|^2\eta^{-3}.
 \tag{Block-sum}
\]
The same bound holds for \(D_Y^2F\), using the opposite blocks.
Here \(\|R\|_{\mathrm{HS}}\le\sqrt{pn}/\eta\) and \(\|R^2\|_{\mathrm{HS}}\le\sqrt{pn}/\eta^2\).

Gaussian integration by parts along the interpolation gives
\[
 \frac d{d\theta}\mathbb EF(H_n(\theta))
 =\frac1{2n}\sum_j\sum_{a<b}\mathbb E\bigl[
       (c_j-1)D_X^2F+(\overline c_j-1)D_Y^2F\bigr].
 \tag{Gaussian-interpolation}
\]
The factor \(n^{-1}\) is the square of the entry normalization.
For \(0<\theta<1\), the formula follows by differentiating the displayed independent Gaussian representation and integrating by parts in its underlying standard Gaussian coordinates.
Representing each covariance-matched pair as a linear image of two standard Gaussians proves the same identity for singular covariance matrices.
The derivative and resolvent bounds justify the expectations, and continuity handles the two endpoints.
By (Block-sum), \(|c_j-1|\le2\), and integration in \(\theta\), the comparison error is at most \(Cn^{-1}\eta^{-3}\).
Combining this with pair replacement and the two diagonal steps proves (Wigner-GOE).
In particular purely imaginary or phase-line laws cause no gap in this count comparison.

<a id="count-proof"></a>
## From the affine comparison to the shrinking count

Apply (Wigner-GOE) to the Hermitian dilation of \(L_n\), with \(p=2m\) and
\[
 B_j=\begin{pmatrix}0&A_j\\A_j^*&0\end{pmatrix},
 \qquad 0\le j\le d.
\]
The accepted [Schultz specialization](../audits/literature/Sch05/Yin_U001.md#goe-hermitization-specialization) gives
\[
 |\mathbb EG_{H_n^{\mathrm O}}(it)-G_H(it)|
 \le Cn^{-1}(t^{-7}+t^{-5}),\qquad0<t\le1.
\]
The assumption of a finite free logarithm excludes a zero atom in the free signed-singular-value law.
The [accepted matrix algebraicity and Puiseux argument](../claims/Yin_C_F0186_v8.md#goe-mesoscopic-count) yields some \(0<\beta\le1\) with
\[
 -t\operatorname{Im}G_H(it)\le Ct^\beta.
\]
The normalization of the two signed copies of each singular value gives
\[
 C_n(t):=\frac1{mn}\sum_{k=1}^{mn}\frac{t^2}{s_k(L_n)^2+t^2}
       =-t\operatorname{Im}G_{H_n}(it),
 \qquad\nu_n([0,t])\le2C_n(t).
\]
The imaginary part is nonpositive for this resolvent convention.
Multiply the two comparisons by \(t\), use \(0<t\le1\), and absorb the smaller error powers to obtain (Affine-count).
If \(t\ge n^{-\gamma}\), then
\[
 n^{-1/2}t^{-3}\le t^\beta
 \quad\text{when }\gamma\le\frac1{6+2\beta},
 \qquad
 n^{-1}t^{-6}\le t^\beta
 \quad\text{when }\gamma\le\frac1{6+\beta}.
\]
The stated strict choice \(0<\gamma<1/(6+2\beta)\) satisfies both, proving (Shrinking-count).

<a id="polynomial-transfer"></a>
## Deterministic count transfer to an arbitrary fixed polynomial

Let \(P\) be any fixed nonconstant scalar polynomial in selfadjoint indeterminates and fix \(z\ne P(0)\).
Use the exact word-chain pencil of [C186v1](../claims/Yin_C_F0186_v1.md#polynomial-application), written
\[
 L_{n,z}=\begin{pmatrix}D&B\\C&Q\end{pmatrix},
 \qquad D-BQ^{-1}C=P(W^{(n)})-zI_n=:S_{n,z}.
\]
The triangular auxiliary block \(Q\) is invertible at every input tuple.
For each \(t\ge0\), let \(E_t\subseteq\mathbb C^n\) be the span of right singular vectors of \(S_{n,z}\) whose singular values are at most \(t\).
The injective graph map
\[
 x\longmapsto v(x)=\binom{x}{-Q^{-1}Cx}
\]
satisfies \(\|v(x)\|\ge\|x\|\) and
\[
 L_{n,z}v(x)=\binom{S_{n,z}x}{0},
 \qquad \|L_{n,z}v(x)\|\le t\|x\|\le t\|v(x)\|\quad(x\in E_t).
\]
The singular-value min-max principle thus gives
\[
 \#\{i:s_i(S_{n,z})\le t\}
 \le\#\{i:s_i(L_{n,z})\le t\}.
 \tag{Schur-count}
\]
This holds even when either matrix is singular, without a norm bound on \(Q^{-1}\) or the input tuple.

The free finite-log condition for this pencil is exactly the one already checked using scalar atomlessness, Puiseux behavior and bounded FK block factorization in [C186v8](../claims/Yin_C_F0186_v8.md#goe-scalar-brown).
Those are statements about the free tuple and the algebraic pencil, independent of the finite input laws.
Therefore (Shrinking-count), together with (Schur-count) and its fixed auxiliary normalization factor, proves
\[
 \mathbb E\frac1n\#\{i:s_i(P(W^{(n)})-zI_n)\le t\}
 \le C_z t^{\beta_z},\qquad n^{-\gamma_z}\le t\le1,
\]
for suitable \(\beta_z,\gamma_z>0\).
For the squared-singular-value law \(\rho_{n,z}\), this becomes
\[
 \mathbb E\rho_{n,z}([0,x])\le C_zx^{\beta_z/2},
 \qquad n^{-2\gamma_z}\le x\le1.
 \tag{Polynomial-squared-count}
\]
No least singular value estimate follows from this count, since the expected mass of an exponentially small singular value can still be of order \(1/n\).
The independently reviewed (Polynomial-squared-count) supplies the count premise in [L61v4](../ledger/Yin_L_F0061_v4.md#conditional-small-values) for every fixed complex-input polynomial under third off-diagonal and second diagonal moments.
The original-law probability or summable least-value floor remains the distinct missing premise.
