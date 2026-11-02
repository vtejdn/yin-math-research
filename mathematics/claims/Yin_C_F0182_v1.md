---
author: Yin
---

# Pointwise order of the strict Hilbert--Schmidt and unrestricted affine quadratic energies

## Provenance, inputs and checking scope

The complete pointwise argument and examples are retained from [L_F0054](../ledger/Yin_L_F0054_v1.md#quadratic-energy-order), in the selfadjoint coefficient setting of [C_F0124](Yin_C_F0124_v1.md#statement) and [C_F0126](Yin_C_F0126_v1.md#statement).
The energy-order argument was developed and self-checked by root on 2026-10-10, including the congruence, real Hilbert-space decomposition, inverse-order direction and normalization by 2m.
This material retains that mathematical scope; no new independent project-proof finding or selected mathematical assessment is claimed.
The existing manuscript comparison checks concern their actual TeX inputs, separately from this fixed mathematical account.

The finite positive-certificate and bijection argument of [C_F0164](Yin_C_F0164_v1.md#argument) supplies the strict domain, the map \(R\mapsto b_R\) and the normalized bound \(\|\Psi\|_{2\to2}<1\) used below.
For the general real-linear solve, use [C_F0126's inner positive-form estimate](Yin_C_F0126_v1.md#the-inner-quadratic-form-is-positive-for-every-trial-matrix) at \(\varepsilon=1\) and \(Q=R\): selfadjoint coefficient matrices give \(\rho=\eta\), and its lower bound is \(\operatorname{Tr}(Z^*ZR^{-1})\).
These are the actual finite-matrix proof inputs.
Neither determinant equality is used to prove the pointwise energy order; C_F0126's determinant theorem is used only for the centered determinant consequence stated with the examples.
The remaining implication comparison, including its reliance on C_F0124's separate global bound, stays in [L_F0054](../ledger/Yin_L_F0054_v1.md#limit-of-the-implication).

## Statement

Here \(m\) is a positive integer and the finite noise family may be empty.
For the determinant interpretation, \(s_j\) are free standard semicircular elements in a finite von Neumann algebra with faithful normal tracial state, and the determinant trace is \(\operatorname{Tr}/m\) tensored with that state.
The energy comparison itself is finite-dimensional.

### Common positive coordinates


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

### Quadratic energy order


Let
\[
 h_R=(\mathcal C_{b_R}+\eta)^{-1}(a)=h_R^*,\qquad
 Z_R=(Z\mapsto H_RZR^{-1}+\eta(Z^*))^{-1}(a).
\]
The first inverse is complex-linear and preserves adjoints; the second is real-linear on all complex matrices.
Define
\[
 q_{\rm HS}(R)=\operatorname{Tr}(a h_R),\qquad
 q_{\rm gen}(R)=\operatorname{Re}\operatorname{Tr}(a Z_R).
\]
Both are nonnegative.
After the bijection (1), the logarithmic objectives are
\[
 \Phi_{\rm HS}(b_R)=\frac{\log\det H_R-\log\det R-m+q_{\rm HS}(R)}{2m},
 \quad
 \Phi_{\rm gen}(R)=\frac{\log\det H_R-\log\det R-m+q_{\rm gen}(R)}{2m}.
 \tag{5}
\]
The finite-matrix comparison is
\[
 q_{\rm HS}(R)\le q_{\rm gen}(R),\qquad
 \Phi_{\rm HS}(b_R)\le\Phi_{\rm gen}(R)\quad(R>0).                 \tag{6}
\]
The inequality can be strict.
Its proof follows and does not use either determinant equality.

## Argument

### Proof

Fix \(R\) and abbreviate \(b=b_R\).
Set
\[
 P=b^{1/2}Rb^{1/2},\quad
 c=b^{-1/2}ab^{-1/2},\quad
 \Psi=\mathcal C_{b^{-1/2}}\eta\mathcal C_{b^{-1/2}}.
\]
The transformed equations, with \(w=b^{1/2}h_Rb^{1/2}\) and \(X=b^{1/2}Z_Rb^{1/2}\), are
\[
 (I+\Psi)w=c,\qquad PX P^{-1}+\Psi(X^*)=c.                \tag{7}
\]
Moreover \(q_{\rm HS}=\langle c,w\rangle_{\mathbb R}\) and \(q_{\rm gen}=\langle c,X\rangle_{\mathbb R}\), where \(\langle U,V\rangle_{\mathbb R}=\operatorname{Re}\operatorname{Tr}(U^*V)\).

On this real Hilbert space define \(J(X)=X^*\) and \(K(X)=PXP^{-1}\).
The map \(J\) is an orthogonal selfadjoint involution, \(K\) is positive definite and selfadjoint, and
\[
 JKJ=K^{-1},\qquad KJK=J.
\]
Split the space into the Hermitian and skew-Hermitian eigenspaces of \(J\).
Since \(\Psi\) commutes with \(J\), write
\[
 K=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},\qquad
 \Psi=\begin{pmatrix}\Psi_+&0\\0&\Psi_-\end{pmatrix}.
\]
Here stars denote real Hilbert-space adjoints.
The identity \(KJK=J\) gives
\[
 A^2-BB^*=I,\quad AB=BD,\quad D^2-B^*B=I.
\]
In particular \(A,D\ge I\), and
\[
 B(D+I)^{-1}B^*=A-I.                                    \tag{8}
\]
The operator in the second equation (7) is
\[
 K+\Psi J=
 \begin{pmatrix}A+\Psi_+&B\\B^*&D-\Psi_-\end{pmatrix}>0.  \tag{9}
\]
Strict positivity here is also the direct finite Cauchy--Schwarz estimate in C_F0126, applied at this trial: before congruence its quadratic form is at least \(\operatorname{Tr}(Z^*ZR^{-1})>0\).
Thus its Schur complement
\[
 F=A+\Psi_+-B(D-\Psi_-)^{-1}B^*
\]
is positive definite.
Since \(\|\Psi\|_{2\to2}<1\),
\[
 0<D-\Psi_-<D+I.
\]
Taking inverses and using (8) gives
\[
 0<F\le A+\Psi_+-B(D+I)^{-1}B^*=I+\Psi_+.
\]
The source \(c\) is Hermitian.
Block inversion of (9) therefore gives
\[
 q_{\rm gen}=\langle c,F^{-1}c\rangle_{\mathbb R}
 \ge\langle c,(I+\Psi_+)^{-1}c\rangle_{\mathbb R}=q_{\rm HS}.
\]
This proves (6).

A useful sufficient equality condition is \([P,w]=0\).
Then the second equation of (7) has solution \(X=w\), so both energies coincide.
This includes the scalar selfadjoint case and the zero-mean case.
No general commutation of trial matrices with coefficients is assumed.

## Strict example and coincidence cases


Take zero noise, \(m=2\),
\[
 a=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 R=\operatorname{diag}(1,4),\qquad
 b_R=\operatorname{diag}(1,1/2).
\]
Then
\[
 Z_R=aR=\begin{pmatrix}0&4\\1&0\end{pmatrix},\qquad
 h_R=b_R^{-1}ab_R^{-1}=\begin{pmatrix}0&2\\2&0\end{pmatrix},
\]
so \(q_{\rm gen}=5\), \(q_{\rm HS}=4\), and
\[
 \Phi_{\rm gen}(R)-\Phi_{\rm HS}(b_R)=\frac14.
\]
Thus the domain bijection and identical determinant factors do not make the full objectives identical, even without noise.

If \(a=0\), both energies vanish at every trial.
C_F0126 and (1)--(4) then directly yield the whole centered C_F0124 formula, including zero capacity.

For scalar selfadjoint data \(\eta(r)=\sigma r\), \(a\in\mathbb R\),
\[
 b(r)^2=\sigma+r^{-1},\qquad
 Z_r=h_r=\frac{a}{r^{-1}+2\sigma}
              =\frac{a}{b(r)^2+\sigma}.
\]
This is a complete pointwise change of variables for every scalar mean, including \(\sigma=0\).
