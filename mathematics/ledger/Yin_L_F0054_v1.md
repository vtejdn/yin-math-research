---
author: Yin
---

# Affine determinant quadratic corrections and their matrix definitions

Context: the strict Hilbert--Schmidt and unrestricted affine determinant formulas of [C_F0124](../claims/Yin_C_F0124_v1.md#statement) and [C_F0126](../claims/Yin_C_F0126_v1.md#statement).
The energy-order argument was developed and self-checked by root on 2026-10-10, including the congruence, real Hilbert-space decomposition, inverse-order direction and normalization by 2m.
This account retains that mathematical scope; no new independent project-proof finding is claimed.

## Matrix geometric mean

**Definition.** For a positive integer m and positive definite Hermitian matrices A,B in M_m(C), their matrix geometric mean is
\[
 A\# B=A^{1/2}(A^{-1/2}BA^{-1/2})^{1/2}A^{1/2},
\]
where every square root is the positive square root.
The adopted formulation uses the unnormalized matrix trace and the strict positive cone.
[BJL19's inspected Section 2, equations (8)--(14)](../audits/literature/BJL19/readme.md) gives this definition and its characterization as the unique positive solution of X A^{-1} X=B.
Thus for R,H_R>0 the solution of b_R R b_R=H_R is R^{-1}#H_R.
The geometric mean alone does not prove strict Hilbert--Schmidt feasibility or the parameterization below; those use the separate completely positive map argument in [C_F0164](../claims/Yin_C_F0164_v1.md#argument).
The BJL19 source check covers the recorded 2017 arXiv v1 passages and Theorem 2, not the whole paper or a transport identification with endpoints depending on R.

## Wigner-Yanase skew information

**Definition.** For a positive integer m, a positive semidefinite density matrix d in M_m(C) with Tr(d)=1, and a Hermitian matrix a, the Wigner--Yanase skew information is
\[
 I_{\rm WY}(d,a)=-\frac12\operatorname{Tr}([d^{1/2},a]^2).
\]
The trace is unnormalized and the commutator is d^{1/2}a-a d^{1/2}.
[Han08's inspected introduction and definition on p.3](../audits/literature/Han08/readme.md) owns the exact arXiv v6 source and definition-check scope; no original Wigner--Yanase proof inspection is claimed.
For b>0 and a_0=a_0^*, direct multiplication gives
\[
 \operatorname{Tr}(ba_0^2)-\operatorname{Tr}(b^{1/2}a_0b^{1/2}a_0)
 =\frac12\|[b^{1/2},a_0]\|_{\rm HS}^2
 =\operatorname{Tr}(b)I_{\rm WY}(b/\operatorname{Tr}(b),a_0).
\]
The first equality uses skew-adjointness of the commutator, and the second uses its square-root homogeneity.
The difference vanishes exactly when b commutes with a_0.
This is the covariance-zero comparison; it does not identify a general nonzero-covariance correction with skew information.
For the normalized trace-log convention \((2m)^{-1}\operatorname{Tr}\), the corresponding correction is the displayed trace difference divided by \(2m\).

## Common positive coordinates


Let all coefficients of
\[
 S=a+\sum_j a_j\otimes s_j
\]
be selfadjoint matrices in size \(m\), and let \(\eta(X)=\sum_j a_jXa_j\).
Finite traces in this material are unnormalized.
Put
\[
 \mathcal B_\eta=\{b>0:\mathcal C_b-\eta\succ0
       \text{ on Hilbert--Schmidt space}\},\qquad
 \mathcal C_b(X)=bXb.
\]
For every \(R>0\), define
\[
 H_R=I+\eta(R),\qquad
 b_R=R^{-1/2}\bigl(R^{1/2}H_RR^{1/2}\bigr)^{1/2}R^{-1/2}.
 \tag{1}
\]
Then
\[
 b_RRb_R-\eta(R)=I.                                      \tag{2}
\]
The map \(R\mapsto b_R\) is a bijection onto \(\mathcal B_\eta\), with inverse
\[
 R_b=(\mathcal C_b-\eta)^{-1}(I)>0.                       \tag{3}
\]

The complete parameterization and its strict-domain justification are supplied by [C_F0164](../claims/Yin_C_F0164_v1.md#argument), with its actual [self-reviewed finding](../audits/reviews/Yin_R_F0175_v1.md#positive-cone-finding).
In particular the normalized completely positive, Hilbert--Schmidt selfadjoint map used below has norm strictly below one.
Taking determinants in (2) yields
\[
 2\log\det b_R=\log\det H_R-\log\det R.                  \tag{4}
\]
Consequently the determinant/capacity factors coincide exactly, before taking any infimum.

## Quadratic energy order

The complete [pointwise energy-order statement and proof](../claims/Yin_C_F0182_v1.md#statement) and its [strict example and coincidence cases](../claims/Yin_C_F0182_v1.md#strict-example-and-coincidence-cases) retain the original author self-check scope.
The comparison uses the common positive coordinates above and does not use either determinant equality in proving the pointwise order.

## Limit of the implication

The common determinant factors and the energy order give only the inequality from the strict-domain infimum to the general infimum.
For a nonzero determinant with noncommuting data, the reverse inequality still uses C_F0124's separate global comparison; it does not follow from the [pointwise energy inequality](../claims/Yin_C_F0182_v1.md#quadratic-energy-order).
Once the two established determinant formulas are used, the objectives have the same infimum despite the possible strict pointwise gap.
For arbitrary complex coefficients the comparison applies after selfadjoint hermitization in size 2m; it does not identify every original-size complex trial domain.
