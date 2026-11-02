---
author: Yin
---

# Two unrestricted positive matrices for every affine semicircular determinant

## Current assessment
[Selected decision](#decision-internal-review)

## Statement

Let
\[
 T=a_0\otimes1+\sum_{j=1}^n a_j\otimes s_j,\qquad
 a_j\in M_m(\mathbb C),
\]
where the \(s_j\) are free standard semicircular elements.
Set
\[
 \eta(U)=\sum_j a_jUa_j^*,\qquad
 \eta^*(U)=\sum_j a_j^*Ua_j,\qquad
 \rho(U)=\sum_j a_jUa_j.
\]
All traces \(\operatorname{tr}_m\) are normalized.
For freely chosen \(X,Y>0\) in \(M_m(\mathbb C)\), define
\[
\begin{aligned}
 P&=X^{-1/2}
     [X^{1/2}(I+\eta(Y))X^{1/2}]^{1/2}X^{-1/2},\\
 Q&=Y^{-1/2}
     [Y^{1/2}(I+\eta^*(X))Y^{1/2}]^{1/2}Y^{-1/2}.
\end{aligned}                                                     \tag{1}
\]
These are ordinary positive square roots and matrix inverses.
They satisfy
\[
 PXP-\eta(Y)=I,\qquad QYQ-\eta^*(X)=I.                            \tag{2}
\]
Introduce the real quadratic optimization
\[
\begin{aligned}
 \mathcal E_{a_0,\rho}(P,Q)
 =\max_{Z\in M_m(\mathbb C)}
 \bigl\{&
 \operatorname{Re}\operatorname{tr}_m(a_0^*Z)
 -\tfrac12\operatorname{tr}_m(Z^*PZQ)\\
 &-\tfrac12\operatorname{Re}\operatorname{tr}_m
                         (Z^*\rho(Z^*))\bigr\}.
\end{aligned}                                                     \tag{3}
\]
The variable \(Z\) is an arbitrary complex matrix, regarded as a real vector variable.
In particular, the map \(Z\mapsto\rho(Z^*)\) is real linear, and must not be differentiated as a complex-linear map.

The exact derived formula is
\[
\begin{aligned}
 \log\Delta(T)=\inf_{X,Y>0}
 \biggl\{-\frac12
  +\frac1{4m}\log
   \frac{\det(I+\eta(Y))\det(I+\eta^*(X))}
        {\det X\det Y}
  +\mathcal E_{a_0,\rho}(P,Q)\biggr\}.
\end{aligned}                                                     \tag{4}
\]
The determinant uses \(\operatorname{tr}_m\otimes\tau\), and \(-\infty\) is allowed.
The inner maximum in (3) is finite and uniquely attained for every positive pair \(X,Y\); the outer infimum need not be attained.
Formula (4) requires no feasibility test on a space of linear maps and no inverse of a linear map in its displayed objective.
It does retain a matrix-valued quadratic maximization when \(\rho\ne0\).
The proof, circular specialization and complete zero-drift capacity reduction are retained below; the covariance maps and the real quadratic maximum are part of the displayed formula.

## Provenance and accepted inputs

This is the complete two-positive-matrix reformulation [retained here](#statement), developed by another AI agent with root's positive-certificate parametrization.
It depends on [C_F0124](Yin_C_F0124_v1.md#statement) and the [full positive-cone certificate](Yin_C_F0164_v1.md#statement).
The centered specialization uses the existing [capacity duality argument](../ledger/Yin_L_F0039_v1.md) at its disclosed audited scope.
The original R_F0123 expressly excluded the paired-matrix author's own L_F0028 module from certification.
At the original candidate checkpoint, this statement awaited its own actual complete internal review.
The [selected assessment](#current-assessment) now adopts the performed internal [self-review](../audits/reviews/Yin_R_F0175_v1.md#two-positive-matrices-finding).
This statement is not a separate discovery of the global C_F0124 comparison.

## Argument

### Why the Parametrization Covers the Required Domain

Hermitize with
\[
 A=\begin{pmatrix}0&a_0\\a_0^*&0\end{pmatrix},\qquad
 B_j=\begin{pmatrix}0&a_j\\a_j^*&0\end{pmatrix},\qquad
 \Theta(U)=\sum_jB_jUB_j.
\]
Write \(\mathcal C_b(U)=bUb\).
For \(b=\operatorname{diag}(P,Q)\) and \(W=\operatorname{diag}(X,Y)\), equations (2) give
\[
 (\mathcal C_b-\Theta)(W)=I_{2m}.                               \tag{5}
\]
The completely positive map \(L=\mathcal C_b^{-1}\Theta\) therefore satisfies
\[
 L(W)=W-b^{-2}<W.
\]
Conjugating by \(U\mapsto W^{1/2}UW^{1/2}\) gives a positive map sending \(I\) strictly below \(I\); its spectral radius is strictly less than one.
The map \(L\) is similar to the Hilbert-Schmidt selfadjoint map
\[
 \Psi=\mathcal C_{b^{-1/2}}\Theta\mathcal C_{b^{-1/2}}.
\]
Hence all eigenvalues of \(\Psi\) are below one, and \(\mathcal C_b-\Theta\succ0\).
This proves admissibility for every pair \(X,Y>0\).

Conversely, if \(b=\operatorname{diag}(P,Q)>0\) belongs to the strict domain of Yin_C_F0124, the same positive-map spectral-radius argument gives the positive convergent Neumann solution
\[
 W=(I-L)^{-1}(b^{-2})=\sum_{k\ge0}L^k(b^{-2})>0.                 \tag{6}
\]
The diagonal block space is invariant under \(L\), so \(W=\operatorname{diag}(X,Y)\).
Equation (5) follows.
The positive solution \(P\) of \(PXP=I+\eta(Y)\) is uniquely given by (1), since \(X^{1/2}PX^{1/2}\) is the positive square root of \(X^{1/2}(I+\eta(Y))X^{1/2}\).
The proof for \(Q\) is identical.
Thus (1) parametrizes exactly the admissible diagonal-block trial matrices.

### Why Restricting to Diagonal Blocks Does Not Change the Infimum

Let \(H_T=\left(\begin{smallmatrix}0&T\\T^*&0\end{smallmatrix}\right)\).
Its square is diagonal in blocks.
For the physical expected resolvent
\[
 R_\varepsilon=E((H_T-i\varepsilon I)^{-1})=H+iV,
\]
the identity
\[
 (H_T-i\varepsilon I)^{-1}
  =H_T(H_T^2+\varepsilon^2I)^{-1}
    +i\varepsilon(H_T^2+\varepsilon^2I)^{-1}
\]
shows that \(H\) is off-diagonal and \(V>0\) is diagonal in blocks.
Thus \(K=V^{-1/2}HV^{-1/2}\) is off-diagonal, \(K^2\) is diagonal, and the Yin_C_F0124 approximant
\[
 b_\varepsilon=V^{-1/2}(I+K^2)^{-1/2}V^{-1/2}
\]
is diagonal in blocks.
The global lower bound of that proof applies to every admissible \(b\), while this restricted sequence approaches the correct determinant.
Consequently the infimum over the diagonal-block part of its domain already has the full value, including zero determinants.

### Deriving the Objective and the Inner Maximum

The map \(\mathcal C_b+\Theta\) preserves the diagonal and off-diagonal selfadjoint spaces.
Its positive-definite quadratic form permits the elementary real Legendre identity
\[
 \tfrac12\langle A,(\mathcal C_b+\Theta)^{-1}A\rangle_{2,2m}
 =\max_{H=H^*}
   \{\langle A,H\rangle_{2,2m}
                -\tfrac12\langle H,(\mathcal C_b+\Theta)H\rangle_{2,2m}\}.
\]
Because \(A\) is off-diagonal, the unique maximizer has zero diagonal blocks.
Write it as \(H=\left(\begin{smallmatrix}0&Z\\Z^*&0\end{smallmatrix}\right)\); multiplying blocks gives precisely (3).
Positivity proves the asserted finiteness and uniqueness.
Its stationary equation, used only to describe the maximizer, is
\[
 PZQ+\rho(Z^*)=a_0.                                           \tag{7}
\]
Finally, taking determinants in (2) gives
\[
 (\det P)^2=\frac{\det(I+\eta(Y))}{\det X},\qquad
 (\det Q)^2=\frac{\det(I+\eta^*(X))}{\det Y}.
\]
Substituting in Yin_C_F0124 yields (4).
This proof makes the dependence on Yin_C_F0124 explicit; it is not an independent derivation of its global comparison.

### 3. Circular Noise: No Auxiliary Complex Matrix

When \(\rho=0\), equation (7) gives \(Z=P^{-1}a_0Q^{-1}\), so (3) becomes
\[
 \mathcal E_{a_0,0}(P,Q)
   =\tfrac12\operatorname{tr}_m(a_0^*P^{-1}a_0Q^{-1}).           \tag{8}
\]
Thus (4) is a genuine two-positive-matrix infimum involving only ordinary matrices of the original size.
The circularity condition is essential to this elimination: pairing coefficients \(c_j/\sqrt2\) and \(ic_j/\sqrt2\) makes \(\rho=0\), whereas a general semicircular pencil need not have that cancellation.

The expression (8) is a permissible two-sided external-field term for circular noise.
The [fixed elliptic-noise obstruction](Yin_C_F0166_v1.md#6-a-fixed-noise-obstruction-to-a-radial-drift-term) shows why it cannot be retained unchanged for a fixed genuinely elliptic family.

### 4. Zero Drift Reduces Directly to Ordinary Capacity

When \(a_0=0\), the inner maximum (3) is zero, attained at \(Z=0\).
The fraction in (4) separates as
\[
 \frac{\det(I+\eta(Y))}{\det Y}
 \ \frac{\det(I+\eta^*(X))}{\det X}.                            \tag{9}
\]
For any completely positive map \(\eta\),
\[
 \inf_{Y>0}\frac{\det(I+\eta(Y))}{\det Y}
   =\operatorname{cap}(\eta).                                  \tag{10}
\]
Indeed every trial value is at least \(\det\eta(Y)/\det Y\), hence at least capacity.
For fixed \(Y>0\), replacing it by \(tY\) gives a limit \(\det\eta(Y)/\det Y\) as \(t\to\infty\), even if \(\eta(Y)\) is singular.
Taking the infimum over shapes proves the opposite inequality.

The factors in (9) have independent variables and positive finite trial values, so their infimum is the product of their nonnegative infima, also if one is zero.
The [audited capacity duality](../ledger/Yin_L_F0039_v1.md) gives \(\operatorname{cap}(\eta^*)=\operatorname{cap}(\eta)\).
Exponentiating (4) therefore gives
\[
 \Delta\!\left(\sum_j a_j\otimes s_j\right)
  =e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)}.
\]
This reduction is at the level of freely chosen trial matrices and infima.
It neither presupposes a balanced optimizer nor substitutes a centered Dyson solution into an affine identity.

## Assessment history

### Decision registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:24 |
| status | open |
| reason | Register this complete retained argument for its actual current internal review; preserve the original derivation, attribution and dependency boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete hypotheses, conclusions, ordered extrema and limitations above. |
| argument | [Argument](#argument) | Entire retained proof and its disclosed accepted mathematical interfaces. |

### Decision internal-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:26 |
| status | proved |
| reason | The retained complete proof and exact current statement passed the actual internal mathematical and interface review at their disclosed accepted input scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete hypotheses, conclusions and precise limits above. |
| argument | [Argument](#argument) | Entire retained argument, including the original dependency and nonconclusion boundaries. |
| review | [Internal finding](../audits/reviews/Yin_R_F0175_v1.md#two-positive-matrices-finding) | Full unrestricted original-size positive-pair formula, its real quadratic maximum and circular/centered specializations. |

