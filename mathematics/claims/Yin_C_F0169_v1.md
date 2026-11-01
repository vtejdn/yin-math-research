---
author: Yin
---

# Positive optimizer Hessians and finite variational Brown-density derivatives

## Current assessment
[Selected decision](#decision-adopted-retained-proof)

## Exact retained scope and provenance

<a id="statement"></a>

For every finite complex affine semicircular pencil in a faithful tracial von Neumann algebra, every complex shift and every positive regularizer, retain the exact variational envelope derivatives, arbitrary positive matrix regularization, strictly positive optimizer Hessian with its completely positive inverse response map and two-sided bounds, the finite Schur-complement Brown-density formula and regularization sensitivity.
The unregularized Hessian conclusion is restricted to boundedly invertible pencils.
No global convexity, uniform zero-regularizer stability or pointwise limiting Brown density is asserted.
The complete fixed argument below is retained from [Yin_L_F0041_v1](../ledger/Yin_L_F0041_v1.md) at 2026-10-21T02:21.
Its original mathematical development, attribution, review dates and historical status statements remain in that fixed L.
This placement preserves existing mathematics; it selects no Task, objective change, new theorem role, novelty or publication claim.

Dated candidate, “draft,” author-check and unadopted-status sentences within the retained text describe the original development.
The selected current decision above owns the present mathematical adoption and exact review evidence.

## Complete retained argument

<a id="argument"></a>

## 1. Setup and exact envelope derivatives

Let
\[
 T=a_0+\sum_j a_j\otimes s_j,\qquad S_z=T-zI,
 \qquad a(z)=a_0-zI,
\]
with arbitrary complex coefficient matrices in \(M_m(\mathbb C)\), free standard semicircular variables, and the faithful normalized trace \(\varphi=\operatorname{tr}_m\otimes\tau\).
The empty noise family is allowed.
Let \(E=\operatorname{id}\otimes\tau\), and keep \(\eta,\rho\) as in C_F0126.
All finite traces below are unnormalized unless marked otherwise.

For \(R>0\), define
\[
 H_R=I+\eta(R),\qquad
 \mathcal T_R(W)=H_RWR^{-1}+\rho(W^*),\qquad
 Z_R(z)=\mathcal T_R^{-1}(a(z)).
\]
The operator \(\mathcal T_R\) is positive definite and selfadjoint on the real Hilbert space of complex matrices with pairing
\(\langle A,B\rangle=\operatorname{Re}\operatorname{Tr}(A^*B)\).
For \(\varepsilon>0\), put
\[
 F_\varepsilon(x,y,R)
 =\log\det H_R-\log\det R-m
  +\langle a(z),\mathcal T_R^{-1}a(z)\rangle
  +\varepsilon^2\operatorname{Tr}R,
 \qquad z=x+iy.
\]
The regularized theorem in C_F0126, after \(Q=\varepsilon^2R\), gives
\[
 u_\varepsilon(z)
 :=\tfrac12\varphi\log(S_z^*S_z+\varepsilon^2I)
 =\frac1{2m}\min_{R>0}F_\varepsilon(x,y,R),
 \tag{1}
\]
with unique optimizer
\[
 R_\varepsilon(z)=E((S_z^*S_z+\varepsilon^2I)^{-1}).
 \tag{2}
\]
At that optimizer,
\[
 Z_\varepsilon(z):=Z_{R_\varepsilon(z)}(z)
 =E((S_zS_z^*+\varepsilon^2I)^{-1}S_z)
 =E(S_z(S_z^*S_z+\varepsilon^2I)^{-1}).
 \tag{3}
\]
These optimizer identifications are existing consequences of C_F0126, not additional assumptions.

The matrices in (2)-(3) depend real analytically on \((x,y)\) for fixed \(\varepsilon>0\).
Differentiating (1) at the unique minimizer is legitimate; it can also be justified directly by differentiating the explicit resolvent (2).
Since the inner quadratic energy has derivative \(2\langle da,Z\rangle\), the envelope identities are
\[
 \partial_xu_\varepsilon=-\frac1m\operatorname{Re}\operatorname{Tr}Z_\varepsilon,
 \qquad
 \partial_yu_\varepsilon=-\frac1m\operatorname{Im}\operatorname{Tr}Z_\varepsilon,
 \qquad
 \boxed{\partial_zu_\varepsilon
       =-\frac1{2m}\operatorname{Tr}Z_\varepsilon^*.}
 \tag{4}
\]
Here \(\partial_z=(\partial_x-i\partial_y)/2\).
Thus the variational optimizer already contains the regularized Brown Cauchy transform; no derivative of the optimizer is needed for the first derivative of the potential.

## 2. The optimizer Hessian is positive definite for positive regularization

This is a new direct consequence of the general determinant formula and its optimizer identification.
It is a statement at the unique minimizer, not a global convexity assertion.
A second proof through the existing Dyson stability result is retained below.

**Draft proposition.**
For every \(z\) and \(\varepsilon>0\), the real Hessian
\[
 \mathfrak H_\varepsilon(z)
 =D_R^2F_\varepsilon(x,y,R_\varepsilon(z))
 \tag{5}
\]
is positive definite on the real Hilbert space of Hermitian matrices with pairing \(\operatorname{Tr}(KL)\).

**Proof by matrix regularization.**
Fix a pencil \(S\), and allow any deterministic positive definite matrix \(D\).
Apply the positive-regularizer formula of C_F0126, with regularizer one, to \(S D^{-1/2}\).
Its coefficient maps are
\[
 \eta_D(X)=\eta(D^{-1/2}XD^{-1/2}),\qquad
 \rho_D(X)=\sum_j a_jD^{-1/2}Xa_jD^{-1/2}.
\]
Use the trial bijection \(R'=D^{1/2}RD^{1/2}\).
If \(Z=\mathcal T_R^{-1}(a)\), its inner solution is \(Z'=ZD^{1/2}\): both terms of the new inner equation equal the old ones multiplied on the right by \(D^{-1/2}\).
Hence the mean energy is unchanged, the logarithmic determinant ratio changes by \(-\log\det D\), and the linear regularization term becomes \(\operatorname{Tr}(DR)\).
Multiplicativity of the Fuglede--Kadison determinant on the positive congruence
\[
 (S D^{-1/2})^*(S D^{-1/2})+I
 =D^{-1/2}(S^*S+D)D^{-1/2}
\]
cancels the same \(-\log\det D\) term on the operator side.
Therefore
\[
 \boxed{\displaystyle
 \tfrac12\varphi\log(S^*S+D)
 =\frac1{2m}\min_{R>0}
       \{\mathcal V_a(R)+\operatorname{Tr}(DR)\},
 \qquad
 R_D=E((S^*S+D)^{-1}).}
 \tag{5a}
\]
The optimizer is unique.
Formula (5a) allows an arbitrary positive matrix regularizer on the right; it is a direct change of variables in C_F0126.

Let \(Q_D=S^*S+D\), with matrices embedded as \(B\otimes1\) in operator products.
Stationarity reads
\[
 \nabla\mathcal V_a(R_D)+D=0.
\]
The explicit formula for \(R_D\) is differentiable in every Hermitian direction \(B\), and
\[
 D_DR_D[B]=-E(Q_D^{-1}(B\otimes1)Q_D^{-1})=:-\mathcal A_D(B).
\]
Differentiating stationarity, with \(\mathfrak H_D=D_R^2\mathcal V_a(R_D)\), gives \(\mathfrak H_D\mathcal A_D=I\).
Moreover, \(\mathcal A_D\) is completely positive, selfadjoint and strictly positive for the Hilbert--Schmidt inner product:
\[
 \operatorname{Tr}(B\mathcal A_D(B))
 =(\operatorname{Tr}\otimes\tau)
   \left[(Q_D^{-1/2}(B\otimes1)Q_D^{-1/2})^2\right]>0
 \quad(B=B^*\ne0).
\]
Faithfulness proves strictness.
Consequently
\[
 \boxed{\displaystyle
 \mathfrak H_D^{-1}(B)
 =E(Q_D^{-1}(B\otimes1)Q_D^{-1}),
 \qquad \mathfrak H_D>0.}
 \tag{5b}
\]
This proves (5) on setting \(D=\varepsilon^2I\).
It also identifies the inverse Hessian as a completely positive response map; positivity of the inverse in this statement includes the Hilbert--Schmidt quadratic form. \(\square\)

For scale information, (5b) gives the quadratic-form bounds
\[
 \lambda_{\min}(D)^2 I
 \le \mathfrak H_D
 \le (\|S\|^2+\|D\|)^2 I.
 \tag{5c}
\]
Indeed the Hilbert--Schmidt norm of \(Q_D^{-1/2}B Q_D^{-1/2}\) lies between \(\|Q_D\|^{-1}\|B\|_2\) and \(\lambda_{\min}(D)^{-1}\|B\|_2\).
In particular the scalar-regularizer lower bound is \(\mathfrak H_\varepsilon\ge\varepsilon^4 I\); it degenerates as the regularizer vanishes.

If \(S\) is boundedly invertible, the optimizer from C_F0127 is \(R_*=E((S^*S)^{-1})\).
Passing to \(D=tI\downarrow0\) in (5b) gives the unregularized extension
\[
 [D_R^2\mathcal V_a(R_*)]^{-1}(B)
 =E((S^*S)^{-1}(B\otimes1)(S^*S)^{-1}).
 \tag{5d}
\]
The right side is again strictly Hilbert--Schmidt positive.
Thus every finite critical point furnished by C_F0127 is nondegenerate, with a positive definite Hessian.
The passage to the limit uses bounded invertibility and norm convergence of the resolvents, not a uniform statement across the spectrum.

**Alternative route retained briefly.**
In the original unscaled variables of C_F0126, put
\(q(Q)=\left(\begin{smallmatrix}C^{-1}-YQ^{-1}Y^*&Y\\Y^*&-Q\end{smallmatrix}\right)\).
Its block inverse satisfies the exact residual identity
\[
 q(Q)^{-1}=A-\Theta(q(Q))
  +\operatorname{diag}(0,\nabla_Q\widehat F_\varepsilon(Q)).
\]
The diagonal transformation from C_F0126 to the physical hermitized resolvent turns a Hessian kernel direction into a kernel direction of \(X\mapsto X-G\Theta(X)G\).
Fixed-positive-regularizer stability from C_F0123 excludes such a direction.
This independently explains nondegeneracy through the Dyson equation, but (5a)-(5b) is the shorter proof and gives the stronger inverse-Hessian formula.
Unique attainment by itself would not imply nonsingularity.

## 3. A finite Hessian formula for the regularized Brown density

All quantities in this section are evaluated at \((x,y,R_\varepsilon(z))\).
Set
\[
 h_x=\partial_x\nabla_RF_\varepsilon,\qquad
 h_y=\partial_y\nabla_RF_\varepsilon,
\]
and let \(\mathfrak H=\mathfrak H_\varepsilon(z)>0\).
Differentiation of the stationarity equation yields
\[
 \partial_xR_\varepsilon=-\mathfrak H^{-1}h_x,
 \qquad
 \partial_yR_\varepsilon=-\mathfrak H^{-1}h_y.
 \tag{8}
\]
Consequently the real Hessian of the minimum value is the Schur complement
\[
 \partial_{jk}u_\varepsilon
 =\frac1{2m}
 \left(F_{jk}-\langle h_j,\mathfrak H^{-1}h_k\rangle\right),
 \qquad j,k\in\{x,y\}.
 \tag{9}
\]
At fixed \(R\), the only dependence on \(x,y\) is the positive real quadratic form in \(a_0-zI\).
Therefore
\[
 F_{xx}=2\langle I,\mathcal T_R^{-1}(I)\rangle,
 \qquad
 F_{yy}=2\langle iI,\mathcal T_R^{-1}(iI)\rangle.
 \tag{10}
\]
The normalized regularized Brown density is thus
\[
 \boxed{\displaystyle
 \beta_\varepsilon(z)
 =\frac1{4\pi m}
 \left[
  2\langle I,\mathcal T_R^{-1}(I)\rangle
 +2\langle iI,\mathcal T_R^{-1}(iI)\rangle
 -\langle h_x,\mathfrak H^{-1}h_x\rangle
 -\langle h_y,\mathfrak H^{-1}h_y\rangle
 \right].}
 \tag{11}
\]
This computes the density from the minimizing positive matrix, the finite inner inverse already present in the main theorem, and two positive definite real linear systems on the \(m^2\)-dimensional space of Hermitian matrices.
It supplies a variational alternative to the \(2m\)-by-\(2m\) Dyson derivative system already recorded in C_F0123.
It is not an assertion that this alternative is faster or uniformly better conditioned.

The first two terms in (11) are the curvature of the objective with the trial matrix fixed; the last two quantify how allowing the optimizer to move reduces that curvature.
Their difference is nonnegative because (1) equals the regularized logarithmic potential.
The direct operator identity from C_F0123 is
\[
 \beta_\varepsilon(z)
 =\frac{\varepsilon^2}{\pi}
   \varphi\left((S_z^*S_z+\varepsilon^2I)^{-1}
                (S_zS_z^*+\varepsilon^2I)^{-1}\right)>0.
 \tag{12}
\]
The factors need not commute; positivity follows by cyclically moving a square root under the trace.
Formula (12) also gives
\[
 0<\beta_\varepsilon(z)
 \le\frac1\pi\operatorname{tr}_mR_\varepsilon(z).
 \tag{13}
\]

## 4. Regularization sensitivity and a scalar consistency check

Write \(t=\varepsilon^2>0\), and denote the regularized potential by \(u_t\).
Since the objective depends on \(t\) only through \(t\operatorname{Tr}R\), another envelope differentiation gives
\[
 \partial_tu_t(z)=\frac1{2m}\operatorname{Tr}R_t(z),
 \qquad
 \partial_t^2u_t(z)
 =-\frac1{2m}\langle I,\mathfrak H_t(z)^{-1}I\rangle<0.
 \tag{14}
\]
This agrees with direct spectral differentiation,
\(\partial_t^2u_t=-\tfrac12\varphi((S_z^*S_z+tI)^{-2})\).
When \(u(z)>-\infty\),
\[
 u_t(z)-u(z)
 =\frac1{2m}\int_0^t\operatorname{Tr}R_s(z)\,ds.
 \tag{15}
\]
The equality is understood by monotone integration, and does not provide a finite uniform error bound unless the optimizer trace can be controlled.

For the scalar empty-noise case \(a_0=c\in\mathbb C\), the objective is
\[
 F_\varepsilon(z,R)=-\log R-1+(|c-z|^2+\varepsilon^2)R.
\]
Then
\[
 R_\varepsilon=(|c-z|^2+\varepsilon^2)^{-1},\quad
 \mathfrak H=R_\varepsilon^{-2},\quad
 h_x=2(x-\operatorname{Re}c),\quad h_y=2(y-\operatorname{Im}c).
\]
Equation (11) reduces exactly to
\[
 \beta_\varepsilon(z)
 =\frac{\varepsilon^2}
       {\pi(|c-z|^2+\varepsilon^2)^2},
\]
the standard regularization of a unit point mass at \(c\).
Equivalently, with \(\delta=\varepsilon^2\), this is \(\delta/[\pi(|c-z|^2+\delta)^2]\).
This checks the signs and factors in (4) and (11), including the need for both real directions.

## 5. Exact scope

The minimizer contains the regularized Cauchy transform, its Hessian is positive definite for every positive regularizer with completely positive inverse (5b), and the Brown density is the Schur complement (11).
The matrix-regularization and residual arguments establish the same conclusion.

The following limits remain outside this draft:

- Positive definiteness at a regularized minimizer is not global convexity of the objective and does not by itself prove convergence of an optimization method.
- The explicit lower bound \(\mathfrak H_\varepsilon\ge\varepsilon^4I\) degenerates; no positive lower bound uniform as \(\varepsilon\downarrow0\), or uniform limiting stability, has been proved.
- Existing C_F0123 gives weak convergence \(\beta_\varepsilon\,d^2z\Rightarrow\mu_T\).
  It does not justify pointwise limiting densities or exclude atoms and curve-supported mass in general.
- The matrix-regularization argument, the alternative residual proof, and the Schur-complement consequence have been self-checked through the exact coefficient transformation, residual algebra and scalar example above.
  They have not undergone independent proof review and are not adopted fixed Claims.

## Assessment history

### Decision retained-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:21 |
| status | open |
| reason | Retain the exact complete argument in its responsible Claim home before selecting its applicable fixed review findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact scope](#statement) | Exact retained scope and hypotheses above and in the complete original statement below. |
| argument | [Complete retained argument](#argument) | Complete original argument, failed implications and limitations retained below. |
| dependency | [Exact input](Yin_C_F0126_v1.md#regularized-minimum-used-in-the-proof) | Unrestricted real-linear inner problem, unique regularized minimum and physical expected-resolvent optimizer; rescale Q=epsilon squared times R. |
| dependency | [Exact input](Yin_C_F0127_v1.md#statement) | Bounded-inverse attainment and unique critical point, only for the stated unregularized extension. |
| dependency | [Exact input](Yin_C_F0123_v1.md#exact-derivatives-from-one-finite-linear-system) | Accepted Brown normalization and weak-regularization interface, actual fixed-positive-regularizer derivative stability and direct positive density identity. |

### Decision adopted-retained-proof

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:24 |
| status | proved |
| reason | Adopt the actual complete self-reviewed internal finding on this unchanged retained argument. Preserve all exact hypotheses, accepted input scopes, failed inferences and remaining independent-inspection boundary; no Task or theorem role changes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact retained scope and hypotheses above and in the complete original statement below. |
| argument | [Exact material](#argument) | Complete original argument, failed implications and limitations retained below. |
| dependency | [Exact material](Yin_C_F0126_v1.md#regularized-minimum-used-in-the-proof) | Unrestricted real-linear inner problem, unique regularized minimum and physical expected-resolvent optimizer; rescale Q=epsilon squared times R. |
| dependency | [Exact material](Yin_C_F0127_v1.md#statement) | Bounded-inverse attainment and unique critical point, only for the stated unregularized extension. |
| dependency | [Exact material](Yin_C_F0123_v1.md#exact-derivatives-from-one-finite-linear-system) | Accepted Brown normalization and weak-regularization interface, actual fixed-positive-regularizer derivative stability and direct positive density identity. |
| review | [Actual finding](../audits/reviews/Yin_R_F0177_v1.md#envelope-hessian-finding) | Whole envelope and Hessian argument: scalar and arbitrary positive matrix regularization, actual unique physical optimizer, first derivatives, strict Hessian and completely positive inverse response, quadratic-form bounds, bounded-inverse zero-regularizer extension, Schur-complement density, sensitivity and scalar normalization. No global convexity or uniform boundary stability. |

