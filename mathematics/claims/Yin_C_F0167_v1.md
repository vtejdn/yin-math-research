---
author: Yin
---

# Independent circular signed-Schur minimum with every positive trial

## Current assessment
[Selected decision](#decision-internal-review)

## Statement

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state.
Let \(c_1,\ldots,c_n\) be free standard circular elements, normalized by \(c_j=(s_{2j-1}+is_{2j})/\sqrt2\) for a free standard semicircular family.
Let
\[
 S=a\otimes1+\sum_jb_j\otimes c_j,
 \qquad a,b_j\in M_m(\mathbb C),
 \qquad \eta(X)=\sum_jb_jXb_j^*.
\]
No selfadjointness or invertibility of these coefficients is assumed, and the empty noise family is allowed.
Put \(\varphi=\operatorname{tr}_m\otimes\tau\), where \(\operatorname{tr}_m=\operatorname{Tr}/m\), and
\[
 \log\Delta_\varepsilon(S)
 =\tfrac12\varphi\log(SS^*+\varepsilon^2I),\qquad\varepsilon>0.
\]
For every freely chosen positive definite \(Q\in M_m(\mathbb C)\), define
\[
 C_Q=\varepsilon^2I+\eta(Q)>0,
\]
\[
 V_\varepsilon(Q)
 =\log\det C_Q-\log\det Q+\operatorname{Tr}Q
    +\operatorname{Tr}(Qa^*C_Q^{-1}a)-m.                       \tag{1}
\]
All traces and finite determinants in (1) are unnormalized.
Then
\[
 \boxed{
  \log\Delta_\varepsilon(S)
    =\frac1{2m}\min_{Q>0}V_\varepsilon(Q).
 }                                                          \tag{2}
\]
The minimum is attained uniquely at
\[
 Q_0=\varepsilon^2E[(S^*S+\varepsilon^2I)^{-1}],
 \qquad E=\operatorname{id}\otimes\tau.                       \tag{3}
\]
In particular \(0<Q_0\le I\).
Every positive definite trial matrix is admissible in (2); a Dyson equation, spectral-radius bound or Hilbert-Schmidt operator inequality is not a feasibility constraint.

Equivalently, define the strictly positive Schur variables \(P,Q>0\) and an unconstrained matrix \(Z\in M_m(\mathbb C)\).
Then
\[
 \begin{aligned}
 \mathcal J_\varepsilon(P,Q,Z)
 ={}&-\log\det P-\log\det Q
      +\operatorname{Tr}(PC_Q)+\operatorname{Tr}Q-2m\\
    &-\operatorname{Tr}(QZ^*C_QZ)
      +2\operatorname{Re}\operatorname{Tr}(a^*ZQ).
 \end{aligned}                                               \tag{4}
\]
The ordered variational formula is
\[
 \boxed{
  \log\Delta_\varepsilon(S)
    =\frac1{2m}\min_{P,Q>0}\max_{Z\in M_m(\mathbb C)}
            \mathcal J_\varepsilon(P,Q,Z).
 }                                                          \tag{5}
\]
The inner maximum is taken first.
We do not exchange the extremum order or assert ordinary joint convexity.
The exact global comparison, ordered optimization, full centered capacity reduction and required regularization limit are part of this statement and are proved below.
No formula obtained by setting regularization to zero before nonzero-drift minimization is asserted.

## Provenance and accepted inputs

This is the complete independent circular signed-Schur mechanism from [L_F0032](../ledger/Yin_L_F0032_v1.md), authored by the yin_t_f0008-contract agent on 2026-09-13.
Its full [original R_F0123 reconstruction](../audits/reviews/Yin_R_F0123_v1.md#3-circular-physical-inverse-and-determinant-normalization) checked the physical, global, ordered and limiting chains at that fixed input.
The local analytic input is [C_F0119's Dyson primitive](Yin_C_F0119_v1.md); [C_F0121](Yin_C_F0121_v1.md) supplies the earlier action and the signed-Schur strategy connection.
The external comparison input is the actual [HP03-U001 unital-column Jensen interface](../audits/literature/HP03/Yin_U001.md#hp03-u001), accepted at its disclosed primary selected-statement/proof depth.
HLN07 is related source reading and the original numerical exploration is motivation, not a premise.
The proof uses neither Spe26 nor C_F0124.
Its vanishing pseudo-covariance is essential: arbitrary complex semicircular coefficients are not identified with circular noise.

## Argument

### Signed Schur origin and physical equations

Form the boundedly invertible selfadjoint pencil
\[
 L_\varepsilon=\begin{pmatrix}\varepsilon^2I&S\\S^*&-I\end{pmatrix}.
\]
The existing Schur factorization gives \(\log\Delta_{\operatorname{tr}_{2m}\otimes\tau}(L_\varepsilon)=\log\Delta_\varepsilon(S)\).
Its inverse expectation has the block form
\[
 q_0=E[L_\varepsilon^{-1}]
 =\begin{pmatrix}P_0&Y_0\\Y_0^*&-Q_0\end{pmatrix},
 \quad
 P_0=E[(SS^*+\varepsilon^2I)^{-1}]>0,
 \quad Q_0>0.                                                \tag{6}
\]
The constant coefficient is \(A=\left(\begin{smallmatrix}\varepsilon^2I&a\\a^*&-I\end{smallmatrix}\right)\).
Circularity makes the covariance of the centered selfadjoint linearization equal to
\[
 \Theta\begin{pmatrix}X&Y\\Z&W\end{pmatrix}
   =\begin{pmatrix}\eta(W)&0\\0&\eta^*(X)\end{pmatrix}.        \tag{7}
\]
The reduced Dyson equation at the real gap zero is \(q_0^{-1}=A-\Theta(q_0)\).
It can be obtained as the continuous boundary value of the Yin_C_F0119 equation; \(L_\varepsilon\) is invertible and (6) has one positive and one negative diagonal block, so \(q_0\) is invertible as well.

Write \(C_0=\varepsilon^2I+\eta(Q_0)\).
Block inversion yields
\[
 \begin{aligned}
 Y_0&=C_0^{-1}aQ_0,\\
 P_0&=C_0^{-1}-C_0^{-1}aQ_0a^*C_0^{-1},\\
 Q_0^{-1}&=I+a^*C_0^{-1}a+\eta^*(P_0).
 \end{aligned}                                               \tag{8}
\]
These identities retain all matrix multiplication orders.

The Yin_C_F0119 logarithmic primitive at zero, or equivalently the real part of its gap boundary value, gives
\[
 2m\log\Delta_\varepsilon(S)
   =-\log|\det q_0|+\tfrac12\operatorname{Tr}(q_0\Theta(q_0)).
\]
The Schur complement of \(-Q_0\) in \(q_0\) is \(C_0^{-1}\), while \(\tfrac12\operatorname{Tr}(q_0\Theta(q_0))=-\operatorname{Tr}(P_0\eta(Q_0))\).
Tracing the last equation of (8) after multiplication by \(Q_0\) therefore proves
\[
 2m\log\Delta_\varepsilon(S)=V_\varepsilon(Q_0).              \tag{9}
\]
Up to (9) this is only a formula at the physical point.
The next section proves the comparison with every trial matrix.

### Global comparison by operator Jensen and a positive left-right operator

Normalize a trial matrix and its covariance around the physical point:
\[
 U=Q_0^{-1/2}QQ_0^{-1/2},\qquad
 \Phi(X)=C_0^{-1/2}\eta(Q_0^{1/2}XQ_0^{1/2})C_0^{-1/2},
\]
\[
 R=C_0^{-1/2}C_QC_0^{-1/2}=I+\Phi(U-I),\qquad
 M=C_0^{-1/2}aQ_0^{1/2},\qquad W=I-MM^*.
\]
Equation (8) and \(P_0>0\) show
\[
 W=C_0^{1/2}P_0C_0^{1/2}>0,
 \quad \Phi(I)=I-\varepsilon^2C_0^{-1}<I,
 \quad Q_0+M^*M+\Phi^*(W)=I.                                 \tag{10}
\]
The adjoint here is for the unnormalized Hilbert-Schmidt inner product.
In particular \(\Phi\) is completely positive and subunital, although it need not be selfadjoint.

Let \(h(t)=t-\log t-1\).
Direct expansion of (1), followed by the last identity in (10), gives the exact difference
\[
 \begin{aligned}
 V_\varepsilon(Q)-V_\varepsilon(Q_0)
 ={}&\operatorname{Tr}h(U)-\operatorname{Tr}h(R)\\
   &+\operatorname{Tr}(MM^*(R-I))
     +\operatorname{Tr}(MUM^*(R^{-1}-I)).
 \end{aligned}                                               \tag{11}
\]
For example, before substituting (10), the same difference is
\[
 \log\det R-\log\det U+\operatorname{Tr}(Q_0(U-I))
      +\operatorname{Tr}(MUM^*R^{-1}-MM^*),
\]
which verifies the signs and trace normalization in (11).

Unitalize the completely positive map by sending \((X,t)\in M_m\oplus\mathbb C\) to \(\Phi(X)+t(I-\Phi(I))\).
Jensen's operator inequality, applied to \((U,1)\), gives
\[
 h(R)\le\Phi(h(U)),                                         \tag{12}
\]
because \(h(1)=0\).
Equivalently, take Kraus matrices for \(\Phi\), append the square root of \(I-\Phi(I)\), and use Theorem 2.1(ii) with the added input matrix \(I\).
Multiplication by \(W>0\) followed by the trace preserves (12).

Split \(-\operatorname{Tr}h(R)\) in (11) into its \(W\)-weighted and \(MM^*\)-weighted terms, using \(W+MM^*=I\).
After (12) and the last identity in (10), the result is
\[
 \begin{aligned}
 V_\varepsilon(Q)-V_\varepsilon(Q_0)
 \ge{}&\operatorname{Tr}(Q_0h(U))\\
 &+\operatorname{Tr}(MUM^*R^{-1})-\operatorname{Tr}(MM^*)\\
 &-\operatorname{Tr}(M(\log U)M^*)
      +\operatorname{Tr}(MM^*\log R).                        \tag{13}
 \end{aligned}
\]
To see that the last two lines are nonnegative without assuming any commutation of the matrices, consider the finite-dimensional Hilbert space of all matrices with inner product \(\langle X,Y\rangle=\operatorname{Tr}(X^*Y)\), and the operator
\[
 \mathcal D(X)=R^{-1}XU.
\]
Left multiplication by \(R^{-1}>0\) and right multiplication by \(U>0\) are commuting positive definite selfadjoint operators.
Thus \(\mathcal D>0\),
\[
 (\log\mathcal D)(X)=-(\log R)X+X\log U,
\]
and the last two lines of (13) equal \(\langle M,h(\mathcal D)M\rangle\ge0\).
This is just finite-dimensional spectral calculus for \(h(t)\ge0\), not an unproved noncommutative logarithm identity.

Finally \(\operatorname{Tr}(Q_0h(U))\ge0\); since \(Q_0>0\), it vanishes only when \(h(U)=0\), hence only when \(U=I\).
Therefore
\[
 V_\varepsilon(Q)\ge V_\varepsilon(Q_0),
 \qquad\text{with equality exactly when }Q=Q_0.              \tag{14}
\]
Together with (9), this proves (2), including attainment and uniqueness.
No compactness or conjectured convexity of \(V_\varepsilon\) is required.

### Ordered minimax and the relation to Yin_C_F0121

Every \(P,Q>0\) and \(Z\in M_m\) defines an invertible Hermitian matrix
\[
 q(P,Q,Z)=
 \begin{pmatrix}P-ZQZ^*&ZQ\\QZ^*&-Q\end{pmatrix}.             \tag{15}
\]
It has exactly \(m\) positive and \(m\) negative eigenvalues, by its Schur complement \(P>0\).
Its upper-left block need not itself be positive.
Substituting (15) and (7) into the same real Dyson action used by Yin_C_F0121,
\[
 -\log|\det q|+\operatorname{Tr}(Aq)
        -\tfrac12\operatorname{Tr}(q\Theta(q))-2m,
\]
gives precisely (4).
The negative quadratic term in \(Z\) is strictly negative definite, so completing its square gives
\[
 \max_Z\{-\operatorname{Tr}(QZ^*C_QZ)
           +2\operatorname{Re}\operatorname{Tr}(a^*ZQ)\}
      =\operatorname{Tr}(Qa^*C_Q^{-1}a),
 \quad Z=C_Q^{-1}a.                                         \tag{16}
\]
For this fixed \(Q\), minimizing \(-\log\det P+\operatorname{Tr}(PC_Q)\) gives the unique \(P=C_Q^{-1}\) and value \(\log\det C_Q+m\).
Equations (14) and (16) now prove (5) globally, with all variables freely specified before optimization.

Thus Yin_C_F0121's positive trial inverse is replaced here by an explicit fixed-inertia Schur parameterization.
The sign-changing directions are maximized first and the positive Schur variables are minimized afterwards.
The correctness of this extremum order is supplied by the global comparison, rather than inferred from the Dyson stationary equation.

At the optimum the upper-left block in (15) is \(P_0>0\).
Equivalently,
\[
 \varepsilon^2I+\eta(Q_0)-aQ_0a^*>0.                        \tag{17}
\]
This is an affine matrix inequality in \(Q_0\).
Consequently restricting the minimum in (2) to \(Q>0\) satisfying (17) leaves its value and unique minimizer unchanged.
Such a restriction is optional; (2) proves the stronger statement with no added inequality.

### Zero mean, ordinary capacity, and the order of limits

For \(a=0\), the final term involving the mean in (1) disappears.
For each fixed \(Q>0\), \(V_\varepsilon(Q)\) decreases as \(\varepsilon\downarrow0\), and its limit is
\[
 V_0(Q)=\log\det\eta(Q)-\log\det Q+\operatorname{Tr}Q-m,       \tag{18}
\]
with \(\log\det\eta(Q)=-\infty\) for singular outputs.
Taking an infimum commutes with this decreasing limit: the lower bound follows from \(V_\varepsilon\ge V_0\), and the reverse bound follows by testing each fixed \(Q\) before taking the limit.
This remains valid when the infimum is \(-\infty\).

The ratio \(\det\eta(tQ)/\det(tQ)\) is unchanged by \(t>0\), while \(\operatorname{Tr}(tQ)\downarrow0\) as \(t\downarrow0\).
Hence (18) gives
\[
 \inf_{Q>0}V_0(Q)=\log\operatorname{cap}(\eta)-m,
 \qquad
 \operatorname{cap}(\eta)=\inf_{Q>0}\frac{\det\eta(Q)}{\det Q}.
\]
Combining with (2) and spectral monotone convergence gives
\[
 \Delta\!\left(\sum_jb_j\otimes c_j\right)
      =e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)},              \tag{19}
\]
including zero capacity and possible failure of attainment at zero regularization.
This is the MS24 normalization for the doubled semicircular coefficient family \(b_j/\sqrt2,\,ib_j/\sqrt2\).
Every completely positive \(\eta\) occurs in this circular setting.
The argument above proves (19) without importing the MS24 equality into the comparison proof.

For nonzero mean one must keep the regularization outside the minimization:
\[
 \log\Delta(S)=\lim_{\varepsilon\downarrow0}
                    \frac1{2m}\min_{Q>0}V_\varepsilon(Q).
\]
We do not claim that the pointwise zero-regularization objective has the same infimum.
Already for a scalar circular element with unit variance and \(|a|>1\), the optimizer tends to zero on the scale \(Q_0\sim\varepsilon^2/(|a|^2-1)\).
Substituting \(\varepsilon=0\) into (1) before optimizing would give \((|a|^2-1)/2\), whereas the actual limiting logarithmic determinant is \(\log|a|\).
The original \(a=0\) recovery is simple and valid precisely because the monotonicity argument above applies there.

## Assessment history

### Decision registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:27 |
| status | open |
| reason | Register this complete retained argument for its actual current internal review; preserve the original derivation, attribution and dependency boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete hypotheses, conclusions, ordered extrema and limitations above. |
| argument | [Argument](#argument) | Entire retained proof and its disclosed accepted mathematical interfaces. |

### Decision internal-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:29 |
| status | proved |
| reason | Adopt the actual complete internal finding for the retained proof and exact statement at their disclosed accepted input depths. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact hypotheses, conclusions and explicit remaining limits above. |
| argument | [Argument](#argument) | Entire retained proof and mathematical input interfaces, with original source and failure distinctions. |
| review | [Internal finding](../audits/reviews/Yin_R_F0175_v2.md#circular-schur-finding) | Complete independent circular signed-Schur proof, every-positive-trial global comparison, uniqueness and all stated limiting boundaries. |

