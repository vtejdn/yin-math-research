---
author: Yin
---

# Positive imaginary matrix drift: global positive-cone minimum and exact zero-drift capacity recovery

## Current assessment
[Selected decision](#decision-m04-isolated-review)

## Positive Imaginary Drift and a Genuine Matrix Infimum

<a id="statement"></a>

<a id="yin_c_f0120"></a>
Record kind: project deduction and exploration record.
Date: 2026-09-12.
Owner: affine-capacity-optimization agent.
Authorization: the user asked to seek capacity-like variational formulas for affine semicircular determinants and explicitly prohibited network searches during this round.
This record uses the local argument [Yin_C_F0119](Yin_C_F0119_v1.md#yin_c_f0119), its MS24/MS17 inputs, and direct finite-dimensional proofs.
No external search, literature attribution or novelty claim is made.
No mathematical Role is assigned.

## Setting and Exact Positive-Cone Formula

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state.
Let \(s_1,\ldots,s_n\in M\) be freely independent standard semicircular elements, and let \(b_1,\ldots,b_n\in M_m(\mathbb C)\) be selfadjoint.
The empty family is allowed.
Write
\[
 T=\sum_jb_j\otimes s_j=T^*,\qquad
 \eta(Q)=\sum_jb_jQb_j,\qquad
 \varphi=\operatorname{tr}_m\otimes\tau.
\]
For an arbitrary positive definite matrix \(D\in M_m(\mathbb C)\), put
\[
 J_D(Q)=-\log\det Q+\operatorname{Tr}_m(DQ)
              +\frac12\operatorname{Tr}_m(Q\eta(Q)),\qquad Q>0.
                                                               \tag{1}
\]
Every trace in (1) is unnormalized.
Then
\[
 \boxed{\quad
 \log\Delta_\varphi(T-iD\otimes1)
       =\frac1m\left(\min_{Q>0}J_D(Q)-m\right).
 \quad}                                                       \tag{2}
\]
The minimum is attained at exactly one positive definite matrix.
Its equation is
\[
 Q^{-1}=D+\eta(Q).                                             \tag{3}
\]
Equation (3) characterizes the minimizer but is not a constraint on trial matrices in (2).
Every positive definite matrix can be inserted directly in (1), and its value yields an upper bound in (2).
The constant matrix \(D\) need not commute with any coefficient or with \(T\).
Thus \(T-iD\) need not be normal.
This is a genuine affine regime; it does not cover an arbitrary selfadjoint real drift \(a_0\).

To package (2) with determinants only, define the positive definite trial matrix
\[
 P_D(Q)=Q^{-1/2}
   \exp\!\left(Q^{1/2}\left(D+\tfrac12\eta(Q)\right)Q^{1/2}-I_m\right)
   Q^{-1/2}.
\]
Since \(\log\det P_D(Q)=J_D(Q)-m\), equation (2) is equivalently
\[
 \boxed{\quad
 \Delta_\varphi(T-iD\otimes1)
   =\min_{Q>0}\Delta_{\operatorname{tr}_m}(P_D(Q)).
 \quad}                                                       \tag{4}
\]
No branch of a matrix logarithm occurs in this expression.
The argument of the exponential is selfadjoint, and ordinary positive definite square roots are used.

## Existence, Strict Convexity Along Positive-Cone Paths and Uniqueness

The relevant convexity is along paths
\[
 Q(t)=Q_0^{1/2}e^{tX}Q_0^{1/2},\qquad X=X^*.
                                                               \tag{5}
\]
Any pair of positive definite matrices is joined by such a path on \([0,1]\), by choosing \(X=\log(Q_0^{-1/2}Q_1Q_0^{-1/2})\).
This defines precisely the pathwise convexity used here; no geometric theorem is required.

The term \(-\log\det Q(t)\) is affine in \(t\).
Diagonalize \(X\), with eigenvalues \(x_k\), and express the following matrices in that basis:
\[
 E=Q_0^{1/2}DQ_0^{1/2}>0,\qquad
 C_j=Q_0^{1/2}b_jQ_0^{1/2}=C_j^*.
\]
Then
\[
 \operatorname{Tr}(DQ(t))=\sum_kE_{kk}e^{tx_k},
\]
and
\[
 \operatorname{Tr}(Q(t)b_jQ(t)b_j)
       =\sum_{k,\ell}|(C_j)_{k\ell}|^2e^{t(x_k+x_\ell)}.
                                                               \tag{6}
\]
All coefficients are nonnegative.
Therefore each quadratic term is convex along (5).
If \(X\ne0\), the second derivative of the linear \(D\)-term is strictly positive because every \(E_{kk}>0\).
Hence \(J_D(Q(t))\) is strictly convex on every nonconstant path (5).

Existence also holds without an irreducibility hypothesis.
Indeed,
\[
 \operatorname{Tr}(Qb_jQb_j)
      =\operatorname{Tr}((Q^{1/2}b_jQ^{1/2})^2)\ge0.
\]
If \(D\ge\delta I_m\), \(\delta>0\), and \(\lambda_k\) are the eigenvalues of \(Q\), then
\[
 J_D(Q)\ge\sum_k(-\log\lambda_k+\delta\lambda_k).
                                                               \tag{7}
\]
Each summand has a finite lower bound and tends to positive infinity at zero and infinity.
Thus every sublevel set of \(J_D\) stays in a compact subset of the positive cone.
A minimizer exists in the interior.
Pathwise strict convexity proves its uniqueness.

Because the matrices \(b_j\) are selfadjoint, \(\operatorname{Tr}(X\eta(Y))=\operatorname{Tr}(\eta(X)Y)\).
The first variation on Hermitian directions is therefore
\[
 dJ_D(Q)[X]
   =\operatorname{Tr}((-Q^{-1}+D+\eta(Q))X).
\]
It vanishes precisely at (3).
Conversely, a critical point is the global minimum: along every path (5) starting there, the derivative at zero vanishes and convexity prevents a lower endpoint value.

Ordinary Euclidean convexity is not a valid replacement for this proof.
For example, take \(m=2\), \(b=\operatorname{diag}(1,-1)\), and a Hermitian off-diagonal matrix \(X\ne0\).
Then \(\operatorname{Tr}(XbXb)=-\operatorname{Tr}(X^2)\).
At \(Q=cI_2\), the Euclidean Hessian in direction \(X\) is \((c^{-2}-1)\operatorname{Tr}(X^2)\), which is negative when \(c>1\).
Complete positivity of \(\eta\) does not make its quadratic form nonnegative on all Hermitian matrices.
Equations (5)-(7) avoid this issue.

## Proof of the Determinant Identity

First take \(D=I_m\).
The expected resolvent
\[
 G=(\operatorname{id}\otimes\tau)((iI_m-T)^{-1})
\]
is purely imaginary: replacing the free semicircular family by its negative preserves its joint distribution, and resolvent adjunction then gives \(G^*=-G\).
Its imaginary part is strictly negative, so \(G=-iQ\) with \(Q>0\).
The Dyson equation in Yin_C_F0119, used directly in dimension \(m\) for this selfadjoint pencil, becomes (3) with \(D=I_m\).

The Cauchy-transform primitive proved in Yin_C_F0119 gives, at the spectral parameter \(i\),
\[
 \log\Delta_\varphi(T-iI_m)
       =-\frac1m\log\det Q
         -\frac1{2m}\operatorname{Tr}(Q\eta(Q)).                \tag{8}
\]
Multiplying (3) by \(Q\) and taking the trace gives
\[
 m=\operatorname{Tr}Q+\operatorname{Tr}(Q\eta(Q)).
\]
Substitution into (1) proves (2) for \(D=I_m\), since the unique positive solution is the unique minimizer already established.

For general \(D>0\), use a deterministic congruence rather than differentiating a noncentral operator-valued spectral parameter.
Set
\[
 c_j=D^{-1/2}b_jD^{-1/2}=c_j^*,\qquad
 T'=D^{-1/2}TD^{-1/2},\qquad
 \eta'(R)=\sum_jc_jRc_j.
\]
Then
\[
 T-iD=D^{1/2}(T'-iI_m)D^{1/2}.
\]
Fuglede-Kadison determinant multiplicativity, with the same normalized trace on all factors, yields
\[
 \log\Delta_\varphi(T-iD)
   =\frac1m\log\det D+\log\Delta_\varphi(T'-iI_m).              \tag{9}
\]
All factors are invertible: \(T'-iI_m\) is invertible by selfadjointness of \(T'\).
Thus only the elementary invertible multiplicativity interface from the [local determinant audit](../audits/literature/MS24/Yin_U001.md#determinant-convention) is needed.

The positive-cone bijection \(R=D^{1/2}QD^{1/2}\) gives
\[
 J_I^{\eta'}(R)=J_D^\eta(Q)-\log\det D.                       \tag{10}
\]
For the quadratic term this follows by direct multiplication and trace cyclicity: \(\operatorname{Tr}(R c_j R c_j)=\operatorname{Tr}(Qb_jQb_j)\).
Combining the \(D=I_m\) result, (9), and (10) proves (2) for arbitrary \(D>0\).
This also proves the asserted minimizer equation without assuming that \(D\) commutes with the covariance.

For the empty noise family, the minimizer is \(Q=D^{-1}\), the minimum is \(\log\det D+m\), and (2) gives \(\Delta(-iD)=\det(D)^{1/m}\), fixing the deterministic normalization.

## Removing the Drift and Recovering Ordinary Capacity

Define
\[
 J_0(Q)=-\log\det Q+\frac12\operatorname{Tr}(Q\eta(Q)),\qquad Q>0.
\]
No attainment is asserted at zero drift.
Nevertheless,
\[
 \boxed{\quad
 \log\Delta_\varphi(T)=\frac1m\left(\inf_{Q>0}J_0(Q)-m\right),
 \quad}                                                       \tag{11}
\]
with the extended-real value \(-\infty\) allowed.

Indeed, \(J_{\varepsilon I}(Q)=J_0(Q)+\varepsilon\operatorname{Tr}Q\).
Hence
\[
 \lim_{\varepsilon\downarrow0}\inf_{Q>0}J_{\varepsilon I}(Q)
          =\inf_{Q>0}J_0(Q).                                  \tag{12}
\]
To see this even when the right side is \(-\infty\), use the lower bound by \(\inf J_0\), and for the reverse bound test each fixed positive definite \(Q\) before taking the limit.
Selfadjoint spectral calculus gives
\[
 \log\Delta(T-i\varepsilon I_m)
      =\tfrac12\varphi\log(T^2+\varepsilon^2I_m)
      \downarrow\log\Delta(T).
\]
This proves (11) from (2).

Combining (11) with the centered MS24 formula already audited and used in Yin_C_F0119 gives the exact ordinary-capacity identity
\[
 \boxed{\quad
 \operatorname{cap}(\eta)
       =\exp\left(2\inf_{Q>0}J_0(Q)-m\right).
 \quad}                                                       \tag{13}
\]
In particular, the imaginary-drift functional does not merely share the original capacity's notation: removing the drift recovers its exact value, including zero capacity.

Homogeneity also eliminates one scalar variable and gives
\[
 \boxed{\quad
 \operatorname{cap}(\eta)
    =\inf_{Q>0}
        \frac{\bigl(\operatorname{Tr}(Q\eta(Q))/m\bigr)^m}
             {(\det Q)^2}
    =\left(\inf_{\substack{B>0\\\det B=1}}
              \frac{\operatorname{Tr}(B\eta(B))}{m}\right)^m.
 \quad}                                                       \tag{14}
\]
For verification, write \(Q=tB\), \(\det B=1\), and let \(\beta=\operatorname{Tr}(B\eta(B))\ge0\).
If \(\beta>0\), minimizing \(-m\log t+t^2\beta/2\) gives \(t^2=m/\beta\) and value \(m/2+(m/2)\log(\beta/m)\).
If \(\beta=0\), the infimum over \(t\) is \(-\infty\) and its exponential is zero.
Taking the remaining infimum proves (14).
This formula is justified here for the selfadjoint-Kraus map \(\eta\); it is not asserted for every completely positive map without that hypothesis.

## Scope and Continuation

The established formula is a global matrix infimum for centered selfadjoint semicircular noise plus a definite purely imaginary matrix drift.
It includes the imaginary-axis logarithmic potential \(\log\Delta(T-iyI_m)\), \(y>0\).
It is not an all-complex-\(z\) formula and does not settle arbitrary real selfadjoint drifts, arbitrary complex coefficient families, or a general matrix saddle-point representation.
No semidefinite nonzero \(D\) boundary extension is asserted; only \(D=0\) has been treated through selfadjoint spectral calculus.

The successful mechanism is that the positive imaginary drift creates a strictly convex linear term on the positive-cone paths (5), while the selfadjoint covariance produces nonnegative exponential coefficients in (6).
Real drift generally introduces real parts of the Cauchy transform, so this mechanism does not transfer by merely replacing \(D\) with a complex matrix.
A useful next route is to preserve this positive-cone minimization as one block of a correctly ordered saddle formulation, with a separate variable accounting for the real part and an explicit physical-branch test.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:09 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#existence-strict-convexity-along-positive-cone-paths-and-uniqueness) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0181_v1.md#dependencies-verification-and-boundaries) | Every original statement and proof for noncentral positive definite imaginary drift: existence, positive-cone strict convexity, unique global minimum, physical Dyson identification, determinant normalization, zero-drift passage and ordinary-capacity reformulation. No arbitrary real drift or general saddle is included. |


### Decision m04-isolated-review

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:23 |
| status | proved |
| reason | Adopt the separately performed isolated review of the complete unchanged fixed mathematics, retaining the precise drift, zero-drift, capacity and source boundaries and the historical unknown finding at its real date. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#existence-strict-convexity-along-positive-cone-paths-and-uniqueness) | Entire noncentral positive imaginary drift proof, its determinant normalization, separate zero-drift passage and selfadjoint-Kraus capacity reformulation. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0181_v1.md#f0078-complete-imaginary-drift-and-capacity-finding) | Complete current equations (1)-(14), noncentral D>0 and separately D=0, empty noise, positive-cone strict convexity and unique minimum, physical Dyson/congruence, determinant and capacity formulas; no arbitrary real drift, nonzero semidefinite boundary or general saddle. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#existence-strict-convexity-along-positive-cone-paths-and-uniqueness) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0181_v1.md#dependencies-verification-and-boundaries) | Independent complete variational review of every statement and proof: noncentral positive definite drift, existence and uniqueness of the global matrix minimum, determinant normalization, the zero-drift passage and the ordinary-capacity reformulation. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Independent complete variational review of every statement and proof: noncentral positive definite drift, existence and uniqueness of the global matrix minimum, determinant normalization, the zero-drift passage and the ordinary-capacity reformulation.

Review: [Exact material](../audits/reviews/Yin_R_F0181_v1.md#dependencies-verification-and-boundaries).

Material covered by that review: [Exact material](Yin_C_F0120_v1.md).
