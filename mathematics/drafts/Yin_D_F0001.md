---
author: Yin
---

# Direct comparison of the C_F0124 and C_F0126 affine determinant objectives

Date: 2026-10-10.
Authoring agent: root.
Status: bounded, user-directed comparison, self-checked; not independently reviewed.
The finite-matrix comparison below is a new draft deduction, not an adopted Claim or a new independent proof of the full C_F0124 determinant theorem.

## Question and scope

The original user question asked how far C_F0126 implies the Speicher-type formula in C_F0124, and whether the formulas have a direct mathematical connection.
This material develops that comparison without reopening the completed Task or altering fixed Claims or source provenance.

Start in the selfadjoint coefficient setting of [C_F0124](../claims/Yin_C_F0124_v1.md).
Reuse the normalized positive-certificate bijection in [C_F0164](../claims/Yin_C_F0164_v1.md#argument), whose complete retained argument has the actual [internal self-review](../audits/reviews/Yin_R_F0175_v1.md#positive-cone-finding).
Compare its resulting objective with [C_F0126](../claims/Yin_C_F0126_v1.md).
Arbitrary complex coefficients can subsequently be treated by selfadjoint hermitization; no unsupported identification of the original-size complex trial domains is intended.

The established starting link is the bijection R > 0 to b > 0 defined by b R b = I + eta(R).
It identifies the determinant factors exactly.
The remaining question is the relation between the two different inverse quadratic forms in the deterministic mean.
A valid general implication must account for both infimum inequalities, not just a common determinant value or a formal substitution.

## 1. Exact common coordinates in the selfadjoint setting

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
This is the existing L_F0031 construction, rather than a new parameterization claim.
Here is its finite-matrix justification.
For any positive \(b\), let
\[
 \Psi=\mathcal C_{b^{-1/2}}\eta\mathcal C_{b^{-1/2}}.
\]
It is completely positive and Hilbert--Schmidt selfadjoint.
Strict feasibility gives \(I-\Psi\succ0\), and hence \(\|\Psi\|_{2\to2}<1\): for a completely positive selfadjoint map, the largest eigenvalue dominates the absolute value of its negative eigenvalues.
In the present selfadjoint Kraus representation this follows by applying \( |\langle x,\Psi(x)\rangle|\le\langle |x|,\Psi(|x|)\rangle\) to Hermitian eigenvectors.
Thus the Neumann series for \((I-\Psi)^{-1}\) is completely positive and its identity term makes (3) strictly positive.

Conversely, a certificate \(bRb-\eta(R)=I\) gives, with \(P=b^{1/2}Rb^{1/2}>0\),
\[
 P-\Psi(P)=b^{-1}>0.
\]
Conjugating \(\Psi\) by \(\mathcal C_{P^{1/2}}\) produces a strictly subunital completely positive map, whose operator norm and spectral radius are less than one.
Similarity preserves spectral radius, and selfadjointness of \(\Psi\) gives strict Hilbert--Schmidt feasibility.
Uniqueness of the positive square root in (1) proves both compositions.
This argument uses no determinant equality from C_F0124.

Taking determinants in (2) yields
\[
 2\log\det b_R=\log\det H_R-\log\det R.                  \tag{4}
\]
Consequently the determinant/capacity factors coincide exactly, before taking any infimum.

## 2. The two remaining quadratic forms

Let
\[
 h_R=(\mathcal C_{b_R}+\eta)^{-1}(a)=h_R^*,\qquad
 Z_R=(Z\mapsto H_RZR^{-1}+\eta(Z^*))^{-1}(a).
\]
The first inverse is complex-linear and preserves adjoints; the second is real-linear on all complex matrices.
Define
\[
 q_{82}(R)=\operatorname{Tr}(a h_R),\qquad
 q_{84}(R)=\operatorname{Re}\operatorname{Tr}(a Z_R).
\]
Both are nonnegative.
After the bijection (1), the logarithmic objectives are
\[
 \Phi_{82}(b_R)=\frac{\log\det H_R-\log\det R-m+q_{82}(R)}{2m},
 \quad
 \Phi_{84}(R)=\frac{\log\det H_R-\log\det R-m+q_{84}(R)}{2m}.
 \tag{5}
\]
The finite-matrix comparison is
\[
 q_{82}(R)\le q_{84}(R),\qquad
 \Phi_{82}(b_R)\le\Phi_{84}(R)\quad(R>0).                 \tag{6}
\]
The inequality can be strict.
Its proof follows and does not use either determinant equality.

## 3. Proof of the quadratic-form comparison

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
Moreover \(q_{82}=\langle c,w\rangle_{\mathbb R}\) and \(q_{84}=\langle c,X\rangle_{\mathbb R}\), where \(\langle U,V\rangle_{\mathbb R}=\operatorname{Re}\operatorname{Tr}(U^*V)\).

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
 q_{84}=\langle c,F^{-1}c\rangle_{\mathbb R}
 \ge\langle c,(I+\Psi_+)^{-1}c\rangle_{\mathbb R}=q_{82}.
\]
This proves (6).

A useful sufficient equality condition is \([P,w]=0\).
Then the second equation of (7) has solution \(X=w\), so both energies coincide.
This includes the scalar selfadjoint case and the zero-mean case.
No general commutation of trial matrices with coefficients is assumed.

## 4. An exact strict example and exact coincidence cases

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
so \(q_{84}=5\), \(q_{82}=4\), and
\[
 \Phi_{84}(R)-\Phi_{82}(b_R)=\frac14.
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

## 5. Exactly which implication follows from C_F0126

By bijectivity and (6), C_F0126 alone, together with the finite lemmas proved here, gives
\[
 \inf_{b\in\mathcal B_\eta}\Phi_{82}(b)
 =\inf_{R>0}\Phi_{82}(b_R)
 \le\inf_{R>0}\Phi_{84}(R)
 =\log\Delta(S).                                        \tag{10}
\]
If \(\Delta(S)=0\), (10) forces the left infimum to be \(-\infty\), so the full C_F0124 equality follows in that case as well.

For general nonzero determinant and noncommuting data, the missing direction in this route is
\[
 \Phi_{82}(b)\ge\log\Delta(S)
       \quad\text{for every }b\in\mathcal B_\eta.          \tag{11}
\]
This is precisely C_F0124's universal comparison.
In normalized coordinates it is
\[
 \log\Delta(c+T_\Psi)
 \le-\frac12+\frac1{2m}
       \operatorname{Tr}\bigl(c(I+\Psi)^{-1}(c)\bigr),
 \qquad \|\Psi\|_{2\to2}<1,\quad c=c^*.
\]
The existing C_F0124 proof establishes it by a separate global argument.
Reusing that lemma together with (10) proves the entire formula without reusing C_F0124's physical approximating-sequence step.
It is not a proof solely by changing variables in C_F0126.
The comparison (6) has the wrong direction to prove (11), so it cannot silently substitute for that lemma.

This is a precise boundary for the derivation supplied here, not a theorem that C_F0126 cannot imply C_F0124 through some additional argument.
Once both existing determinant theorems are admitted, the two objectives in (5) have the same infimum, although the first is pointwise no larger.

## 6. Complex coefficients and relation to the earlier two-scale comparison

For arbitrary complex coefficients, apply this discussion to the selfadjoint hermitization
\[
 \mathscr H_S=\begin{pmatrix}0&S\\S^*&0\end{pmatrix},
 \qquad \Delta_{2m}(\mathscr H_S)=\Delta_m(S).
\]
This gives the same finite comparison and one-sided derivation for the size-\(2m\) strict-domain formula stated in C_F0124.
It does not identify the original size-\(m\) variable of C_F0126 with every variable of a two-positive-scale complex representation.
In particular, the formal pair \((I+\eta(R),R^{-1})\) from the earlier comparison need not satisfy its strict Hilbert--Schmidt norm condition.
The positive balanced matrix (1) is a different construction.

## 7. Verification and remaining scope

The proof above was checked by the authoring agent, including the congruence, the real versus complex Hilbert-space distinction, the order of inverse inequalities, and the normalization by \(2m\).
An interactive NumPy check with seed 10010 used 24 random selfadjoint coefficient/mean examples in sizes 2 and 3, with two Kraus matrices and positive trials.
The smallest observed energy difference was 0.0495689789, and the largest residual in (2) was 8.1e-14.
The exact example gave energies 4 and 5; a scalar control agreed to 4.5e-16.
These checks are not premises of the proof and are not an independent audit.

No general direct proof of (11) from C_F0126 has been supplied here.
No geodesic convexity assertion, original-size complex-domain equivalence, or new literature-priority conclusion is made.
