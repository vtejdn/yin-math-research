---
author: Yin
---

# Circular infimal convolution and an exact raw-signature saddle obstruction

## Current assessment
[Selected decision](#decision-internal-review)

## Statement

Let \(b_j\in M_m(\mathbb C)\) be selfadjoint and \(\eta(X)=\sum_j b_jXb_j\).
Let \(T_\eta=\sum_jb_js_j\) and \(C_\eta=\sum_jb_jc_j\) for standard free semicircular and circular families, using the normalized tracial determinant.
If \(\eta\) is strictly positive as a Hilbert--Schmidt operator, then every selfadjoint \(a\in M_m(\mathbb C)\) satisfies
\[
 \log\Delta(a+T_\eta)=\inf_{U=U^*}
 \left\{\frac1{2m}\operatorname{Tr}((a-U)\eta^{-1}(a-U))+
 \log\Delta(U+C_\eta)\right\}.
\]
This is the disclosed circular-potential reformulation of C_F0125, with the extrema and zero-regularization limit justified by that theorem's accepted local uniform convergence and equicoercivity.
For an invertible indefinite Hilbert--Schmidt selfadjoint completely positive covariance, replacing that infimum with successive extrema on its original positive/negative spectral spaces is only a candidate.
The explicit selfadjoint size-two coefficients below give a physical centered point whose Hessian is strictly positive on one of the covariance's negative directions, so the raw-signature local-saddle mechanism fails.
This is a proved failure of that mechanism; it is not a proof that every possible ordered value of the candidate is incorrect.
Balancing repairs this particular local Hessian sign but supplies no general global formula, no zero-capacity limit and no unrestricted Task conclusion.

## Provenance and accepted inputs

The complete circular identification and raw-signature counterexample are retained from [L_F0030](../ledger/Yin_L_F0030_v1.md), authored by the indefinite-variation agent on 2026-09-13.
The first conclusion accepts the exact [C_F0125 matrix theorem](Yin_C_F0125_v1.md#matrix-positive-hs-minimax) and [C_F0119 primitive](Yin_C_F0119_v1.md); it is independent of C_F0124 and its source proposal.
The explicit Hessian failure and the local balancing observation are direct finite calculations with the original physical-branch uniqueness and implicit-function argument retained below.
Search context, the unresolved general signed candidate and provenance remain in the original L; no source theorem was accepted from its targeted external search.

## Argument

### An Equivalent Circular-Potential Description of the Successful Regime

Keep the selfadjoint coefficient family \(b_j\), and let
\[
 C_\eta=\sum_jb_j\otimes c_j,\qquad
 T_\eta=\sum_jb_j\otimes s_j,
\]
where \(c_j\) are free standard circular elements and \(s_j\) are free standard semicircular elements.
These models may be realized in a larger tracial probability space if necessary.
Both left and right circular covariances are \(\eta(X)=\sum_jb_jXb_j\); the circular mixed covariance is zero.
Use the normalized trace in both logarithmic determinants.

Under the Hilbert--Schmidt positive hypothesis of Yin_C_F0125, its ordered formula is equivalently the quadratic infimal convolution
\[
 \log\Delta(a+T_\eta)
 =\inf_{U=U^*}
    \left\{\frac1{2m}\operatorname{Tr}
       ((a-U)\eta^{-1}(a-U))
                 +\log\Delta(U+C_\eta)\right\}.             \tag{1}
\]
This identity makes the role of the inner matrix maximum more transparent: it computes a deformed circular determinant.
It is not an assertion for an arbitrary covariance.

Here is the identification directly from the existing proof.
At positive regularization, its inner maximizing \(V\) determines \(R=(U+iV)^{-1}=P-iQ\) and the auxiliary circular hermitization resolvent
\[
 G=\begin{pmatrix}iQ&P\\P&iQ\end{pmatrix}.
\]
Conjugating by the scalar Hadamard matrix gives blocks \(R^*\) and \(-R\), hence \(|\det G|=|\det R|^2\).
The circular covariance gives \(\operatorname{Re}\operatorname{Tr}(G\Xi(G))=-2\operatorname{Tr}(Q\eta(Q))\).
The Yin_C_F0119 primitive therefore identifies the circular part of the reduced objective as
\[
 -\log|\det R|-\tfrac12\operatorname{Tr}(Q\eta(Q)).
\]
Since \(V-\varepsilon\eta(I)=\eta(Q)\), this is exactly the optimized imaginary term of Yin_C_F0125.
The positive imaginary regularization on the two hermitization blocks is \(\varepsilon\eta(I)\).
Fixed positive congruence and bounded determinant multiplicativity make its zero limit the ordinary determinant of \(U+C_\eta\).
The local uniform convergence and equicoercivity already proved in Yin_C_F0125 permit the outer infimum limit.
This proves (1) without using Yin_C_F0124 or its source proposal.

### A Natural Signed Extension and Its Missing Global Argument

Suppose for exploration that \(\eta\) is invertible and Hilbert--Schmidt selfadjoint, but has negative eigenvalues.
On the real Hilbert space of Hermitian matrices, write \(\mathcal E_+\) and \(\mathcal E_-\) for its positive and negative spectral subspaces.
A plausible repair of (1) is
\[
 \inf_{U_+\in\mathcal E_+}\ \sup_{U_-\in\mathcal E_-}
 \left\{\frac1{2m}\operatorname{Tr}
    ((a-U_+-U_-)\eta^{-1}(a-U_+-U_-))
                  +\log\Delta(U_++U_-+C_\eta)\right\}.      \tag{2}
\]
The quadratic term has the intended sign in both successive variables.
For the simplest covariance \(\eta=\operatorname{Ad}Z\), a drift in an off-diagonal Pauli direction changes from an incorrect outer minimum to the correct scalar maximum.
That check alone does not prove (2).

In particular, the fixed positive and negative eigenspaces of the original covariance need not be the correct geometry.
The following example rules out the most direct proof that the physical zero-drift point is a saddle with respect to those raw eigenspaces.

### Explicit Failure of the Raw Signature Saddle Test

Take
\[
 b_1=E_{11},\qquad b_2=10E_{22},\qquad
 b_3=10(E_{12}+E_{21}).
\]
On the diagonal algebra, the covariance has matrix
\[
 V_0=\begin{pmatrix}1&100\\100&100\end{pmatrix}.
\]
On the off-diagonal Hermitian Pauli directions its eigenvalues are \(100\) and \(-100\).
Thus the full covariance is invertible and has both Hilbert--Schmidt signs.
Its positive balancing matrix is
\[
 Q_0=\operatorname{diag}\left(\frac1{\sqrt{11}},
                        \frac1{10\sqrt{11}}\right),\qquad
 \eta(Q_0)=Q_0^{-1}.                                        \tag{3}
\]
For the normalized covariance \(\Phi=\mathcal C_{Q_0^{1/2}}\eta\mathcal C_{Q_0^{1/2}}\), the diagonal block is \(\bigl[\begin{smallmatrix}1/11&10/11\\10/11&1/11\end{smallmatrix}\bigr]\), and its off-diagonal eigenvalues are \(10/11,-10/11\).
In particular, none of its eigenvalues equals \(-1\).

Near the zero Hermitian mean, the circular determinant in (2) is smooth and its unnormalized Hessian is \(\mathcal C_{Q_0}\).
This can be checked without a general regularity theorem.
At zero mean the symmetric circular inverse representation is \(R=-iQ_0\).
The imaginary stationary equation for that auxiliary circular model has linearization \(I+\eta\mathcal C_{Q_0}\), invertible by the spectrum of \(\Phi\) just computed.
The implicit-function theorem gives a positive imaginary branch near zero and small positive regularization; physical uniqueness identifies it with the actual circular resolvent.
Differentiating its real part at zero gives \(X\mapsto Q_0XQ_0\).
The determinant derivative under the normalized trace is the real resolvent, so the asserted Hessian follows after multiplying the potential by \(m\).

Consequently the unnormalized Hessian of the objective in (2), at \(a=U=0\), is
\[
 \eta^{-1}+\mathcal C_{Q_0}.
\]
On diagonal matrices its ordinary real matrix is
\[
 V_0^{-1}+\operatorname{diag}(1/11,1/1100)
  =\frac1{9900}\begin{pmatrix}800&100\\100&8\end{pmatrix}.
                                                               \tag{4}
\]
Let
\[
 \lambda_-=\frac{101-\sqrt{49801}}2<0,\qquad
 r=\frac{\lambda_--1}{100}.
\]
The diagonal vector \((1,r)\) lies in the negative eigenspace of \(V_0\), and \(-0.625<r<-0.62\).
Its quadratic form in (4) is
\[
 \frac{800+200r+8r^2}{9900}>0.                              \tag{5}
\]
Thus the physical point \(U=0\) is not a local maximum in this negative-covariance direction.
A proof of (2) by declaring this point a convex-concave saddle is impossible.

The exact conclusion here is a failure of that saddle mechanism.
Equation (5) alone is not promoted to a proof that every possible ordered value in (2) is wrong: such an assertion would also need a global optimizer or value comparison.
The distinction matters, since ordered variational formulas can remain correct when a raw saddle assertion fails.

### Balancing as a Possible Change of Geometry

A capacity-balancing congruence changes the spectral decomposition used in (2).
In the example, (3) transforms the covariance to the unital selfadjoint map \(\Phi\).
At its centered circular point the Hessian becomes \(\Phi^{-1}+I\); it is nonpositive on negative eigenspaces of \(\Phi\), since those eigenvalues lie in \([-1,0)\).
Therefore the local failure (5) disappears after balancing.

This suggests testing a signed real-mean optimization in the geometry selected by a positive balancing matrix, rather than the original covariance's Euclidean eigenspaces.
It remains only a strategy:

- A balanced center does not yet prove global minimum-maximum ordering for arbitrary drift.
- General centered covariance may have zero capacity, no attained balance, or zero Hilbert--Schmidt eigenvalues.
- Approximate balancing must have a controlled variational limit, rather than define trial matrices through an already selected Dyson branch.

The direct inverse-covariance route therefore still has substantial unrestricted obligations.
The independent signed-Schur/complex-inner-variable work pursued in parallel is another way to avoid these negative-direction obstructions, using covariance Cauchy--Schwarz and a positive-cone variable instead of an inverse covariance.
Its proof and assessment belong to that separate module.

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
| review | [Internal finding](../audits/reviews/Yin_R_F0175_v2.md#circular-signature-finding) | Complete circular infimal-convolution derivation and exact raw-signature local-saddle counterexample with its limited balancing observation. |

