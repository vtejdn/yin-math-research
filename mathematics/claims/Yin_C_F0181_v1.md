---
author: Yin
---
# Atiyah property for two free selfadjoint variables through graded subordination

Context: local repair of [ACSY24-U003's Atiyah interface](../audits/literature/ACSY24/Yin_U003.md#atiyah-property-convention), preserving ACSY24 Theorem 4.7's statement.
This mixed source reconstruction and local deduction uses BBL21 preprint v2, without a novelty claim or an assertion about the unavailable published Corollary 3.3.

## Statement

Let \((\mathcal M,\tau)\) be a finite von Neumann algebra with a faithful normal tracial state, and let \(X_1,X_2\in\mathcal M\) be free bounded selfadjoint operators with spectral distributions \(\mu_1,\mu_2\).
Let \(\Gamma\subseteq\mathbb R\) be an additive subgroup containing \(\mathbb Z\), with \(\mu_j(\{t\})\in\Gamma\) for every \(t\in\mathbb R\) and \(j\in\{1,2\}\).
Then \(\operatorname{rk}_{\mathcal M}A(X_1,X_2)\in\Gamma\) for every positive integer \(m\) and \(A\in M_m(\mathbb C\langle x_1,x_2\rangle)\).
The rank uses the unnormalized matrix trace, so \(\operatorname{rk}_{\mathcal M}(I_m)=m\).
No closure of \(\Gamma\) under limits or division by two is assumed.

## Current assessment
[Selected decision](#decision-reviewed-adoption)

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-02T04:28 |
| status | open |
| reason | The full candidate addresses expectation and parity; independent correction review is required before adopting this repair. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All polynomial matrices and arbitrary additive subgroups specified above. |
| argument | [Graded subordination proof](#graded-subordination-proof) | Square support cuts, subordination symmetry, one-variable nullities and linearization. |
| dependency | [BBL21 inspected inputs](../audits/literature/BBL21/Yin_U001.md#bbl21-u001) | Preprint v2 Theorem 3.5(vii), equation (3.7) and Theorem 3.2's norm limits, under invertible expected kernel; analytic foundations are accepted rather than re-audited. |
| dependency | [ACSY24 matrix linearization](../audits/literature/ACSY24/Yin_U002.md#acsy24-u002) | Definition 2.16 and Lemma 2.20, with actual evaluated inverse and integer matrix-size offset. |


### Decision reviewed-adoption

| Field | Value |
| --- | --- |
| date | 2026-11-02T04:41 |
| status | proved |
| reason | Adopt the complete independently reviewed proof and its exact source interfaces. R_F0185 found no mathematical gap for the full arbitrary-subgroup conclusion; final journal Corollary 3.3 identification remains a separate attribution limit, not a premise of this v2-based proof. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All polynomial matrices, bounded free selfadjoint inputs and arbitrary additive subgroups containing the integers and all marginal atomic weights. |
| argument | [Graded subordination proof](#graded-subordination-proof) | Unchanged complete proof: square support cuts, invertible expected kernels, subordination symmetry, structural parity cancellation, spectral minors and matrix linearization. |
| dependency | [BBL21 inspected inputs](../audits/literature/BBL21/Yin_U001.md#bbl21-u001) | Preprint v2 Theorem 3.5(vii), equation (3.7) and Theorem 3.2's actual norm limits, under the verified expected-kernel hypothesis; analytic foundations are accepted rather than re-audited. |
| dependency | [ACSY24 matrix linearization](../audits/literature/ACSY24/Yin_U002.md#acsy24-u002) | Definition 2.16 and Lemma 2.20 with actual evaluated auxiliary inverse and integer offset mk. |
| review | [Independent whole correction review](../audits/reviews/Yin_R_F0185_v1.md#whole-candidate-finding) | Entire statement and unchanged proof, including exact primary-source interfaces; actual independent review act 2026-11-02T04:39 UTC and the finding's source-access and analytic-foundation limits. |

## Graded subordination proof

### Trace conventions and square support cuts

For \(T\in M_n(\mathcal M)\), let \(p_T\) denote its right kernel projection and set
\[
 E_n:=\operatorname{id}_{M_n(\mathbb C)}\otimes\tau,\qquad
 \nu_n(T):=(\operatorname{Tr}_n\otimes\tau)(p_T),\qquad
 \operatorname{rk}_{\mathcal M}T:=n-\nu_n(T).
\]
Here \(\operatorname{Tr}_n\) is unnormalized and \(\nu_n(T)=n\tau_n(p_T)\) for the tracial state \(\tau_n:=\operatorname{tr}_n\otimes\tau\).
Polar decomposition in the finite algebra gives \(\nu_n(T)=\nu_n(T^*)\).

Let \(q\in M_n(\mathbb C)\) be the support of \(E_n(p_T)\), identifying scalar matrices with their tensors with \(1_{\mathcal M}\).
Faithfulness of \(E_n\) and \(E_n((1-q)p_T(1-q))=(1-q)E_n(p_T)(1-q)=0\) give \(p_T\le q\).
Since \(Tqv=0\) is equivalent to \(qv\in\ker T\),
\[
 p_{Tq}=p_T+(1-q),\qquad E_n(p_{Tq})=E_n(p_T)+(1-q)>0,\qquad
 \nu_n(Tq)-\nu_n(T)=n-\operatorname{Tr}_n(q)\in\mathbb Z.
\tag{1}
\]
The positive scalar matrix is invertible because \(E_n(p_T)\) is invertible on its finite-dimensional support.
Set \(U:=Tq\), let \(r\) be the scalar support of \(E_n(p_{U^*})\), and define \(S:=rU=rTq\).
Applying (1) to \(U^*\), with \(S^*=U^*r\), gives \(E_n(p_{S^*})>0\) and \(\nu_n(S^*)-\nu_n(U^*)=n-\operatorname{Tr}_n(r)\).
Also \(p_S\ge p_U\), so \(E_n(p_S)\ge E_n(p_U)>0\).
Equality of the nullities of each square operator and its adjoint yields
\[
 E_n(p_S)>0,\qquad E_n(p_{S^*})>0,\qquad
 \nu_n(S)-\nu_n(T)=2n-\operatorname{Tr}_n(q)-\operatorname{Tr}_n(r)\in\mathbb Z.
\tag{2}
\]
All matrices retain their full \(n\)-by-\(n\) padding.
We do not replace \(S\) by a rectangular scalar-corner matrix or assume equal scalar support ranks.
This explicitly extends BBL21 Lemma 4.7's support-cut calculation to arbitrary bounded square \(T\).

### Off-diagonal subordination and its symmetry

Take a linear pencil \(T:=a_0\otimes1+a_1\otimes X_1+a_2\otimes X_2\), where \(a_j\in M_n(\mathbb C)\) need not be selfadjoint.
Its cut matrix remains a scalar-coefficient linear pencil, say \(S=c_0\otimes1+c_1\otimes X_1+c_2\otimes X_2\).
Set
\[
 J:=\begin{pmatrix}I_n&0\\0&-I_n\end{pmatrix},\qquad
 b:=-\begin{pmatrix}0&c_0\\c_0^*&0\end{pmatrix},\qquad
 H_j:=\begin{pmatrix}0&c_j\\c_j^*&0\end{pmatrix}\otimes X_j,\qquad H:=H_1+H_2.
\]
Then \(b,H_1,H_2\) are selfadjoint, \(JbJ=-b\), \(JH_jJ=-H_j\), and
\[
 H-b=\begin{pmatrix}0&S\\S^*&0\end{pmatrix},\quad
 p_{H-b}=p_{S^*}\oplus p_S,\quad
 E_{2n}(p_{H-b})>0,\quad \nu_{2n}(H-b)=2\nu_n(S).
\tag{3}
\]
The expectation is invertible by (2), meeting the BBL21 hypothesis.
Proposition 4.1 gives freeness of \(H_1,H_2\) over \(B:=M_{2n}(\mathbb C)\otimes1\) with respect to \(E_{2n}\).

Accept BBL21 v2 Theorem 3.5 and its conditional-resolvent identity (3.7) at these hypotheses.
For the trace-preserving conditional expectation \(F_j\) onto \(W^*(B,H_j)\), that identity reads, for \(z:=b+\mathrm iyI_{2n}\), \(y>0\),
\[
 F_j((z-H)^{-1})=(\omega_j(z)-H_j)^{-1}.
\tag{4}
\]
The theorem uses the selfadjoint norm limits \(b_j:=\lim_{y\downarrow0}\omega_j(b+\mathrm iyI_{2n})\), by the construction in Theorem 3.2.
The equalities \(JzJ=-z^*\) and \(JHJ=-H\) imply \(J(z-H)^{-1}J=-((z-H)^{-1})^*\).
Since \(J\in B\subseteq W^*(B,H_j)\), bimodularity and adjoint preservation of \(F_j\) transport this through (4):
\[
 J(\omega_j(z)-H_j)^{-1}J=-((\omega_j(z)-H_j)^{-1})^*.
\]
Inversion gives \(J\omega_j(z)J=-\omega_j(z)^*\), and the actual selfadjoint norm limits therefore satisfy \(Jb_jJ=-b_j\).
Thus scalar \(n\)-by-\(n\) matrices \(d_j\) satisfy
\[
 b_j=\begin{pmatrix}0&d_j\\d_j^*&0\end{pmatrix},\qquad
 b_j-H_j=\begin{pmatrix}0&D_j\\D_j^*&0\end{pmatrix},\qquad
 D_j:=d_j\otimes1-c_j\otimes X_j.
\]
Because the blocks remain square, finiteness and polar decomposition give
\[
 \nu_{2n}(b_j-H_j)=\nu_n(D_j)+\nu_n(D_j^*)=2\nu_n(D_j).
\tag{5}
\]
Theorem 3.5(vii), converted from \(\tau_{2n}\) to the unnormalized trace, states
\[
 \nu_{2n}(b_1-H_1)+\nu_{2n}(b_2-H_2)=2n+\nu_{2n}(H-b).
\]
Substitution of (3) and (5) and cancellation of a common structural factor of two in this real equality give
\[
 \nu_n(S)+n=\nu_n(D_1)+\nu_n(D_2).
\tag{6}
\]
Cancellation precedes any subgroup conclusion and uses no implication \(2x\in\Gamma\Rightarrow x\in\Gamma\).

### One-variable nullities and polynomial matrices

Each scalar pencil \(d_j-tc_j\) attains its maximum rank outside a finite real set \(F_j'\): a nonzero maximum-size minor has finitely many real zeros, and a maximum-rank-zero pencil has constant rank.
Set \(k_j:=\min_{t\in\mathbb R}\dim_{\mathbb C}\ker(d_j-tc_j)\).
The spectral functional calculus gives
\[
 \nu_n(D_j)=\int_{\mathbb R}\dim_{\mathbb C}\ker(d_j-tc_j)\,d\mu_j(t)
 =k_j+\sum_{t\in F_j'}
 \bigl(\dim_{\mathbb C}\ker(d_j-tc_j)-k_j\bigr)\mu_j(\{t\}).
\tag{7}
\]
All coefficients and \(k_j\) are integers, so \(\nu_n(D_j)\in\Gamma\).
This is BBL21 Lemma 4.2's scalar-minor mechanism applied to the square blocks, whose coefficients need not be selfadjoint.
Only finitely many atoms enter (7), even if a marginal has infinitely many atoms.
Equations (6) and (2) yield \(\nu_n(T)\in\Gamma\), hence \(\operatorname{rk}_{\mathcal M}T=n-\nu_n(T)\in\Gamma\), for every linear pencil.

Apply ACSY24 Definition 2.16 and Lemma 2.20 to a polynomial expression representing the given \(m\)-by-\(m\) matrix \(A(X_1,X_2)\), allowing its finite set of scalar matrix coefficients as additional variables.
After evaluating the constant matrices, its display \(L\) is a square linear pencil in \(X_1,X_2\) with scalar coefficients.
The representation supplies an actual inverse for the evaluated auxiliary block \(Q\), so block elimination gives
\[
 \operatorname{rk}_{\mathcal M}A(X_1,X_2)=\operatorname{rk}_{\mathcal M}L-mk
\]
for the integer representation size \(k\), with unnormalized matrix traces throughout.
The linear-pencil result and \(mk\in\mathbb Z\subseteq\Gamma\) prove the statement.
The size convention and inverse requirement are retained at [ACSY24-U002](../audits/literature/ACSY24/Yin_U002.md#1-rank-conventions-and-linearization).

## Source and review limits

The primary BBL21 text inspected is [arXiv:1903.09002v2](../literature/pdf/BBL21--arxiv-v2.pdf), dated 2020-05-15, especially Theorems 3.2 and 3.5, equation (3.7), Proposition 4.1 and Lemma 4.7.
The analytic subordination theorem and conditional-resolvent identity are accepted external inputs at their explicit hypotheses; their analytic foundations are not independently re-proved here.
The support cuts, expectation invertibility, square padding, resolvent symmetry, parity cancellation, spectral minor argument and matrix-linearization interface form the local reconstruction.
This does not establish the contents of the unavailable published Corollary 3.3 or identify its text with v2.
The separate ACSY24 Lemma 3.3 tensor-adjoint input used by C_F0146 and C_F0149 is unchanged.
The repair agent's development checks are self-checks.
The separate [whole correction finding](../audits/reviews/Yin_R_F0185_v1.md#whole-candidate-finding), performed independently on 2026-11-02T04:39 UTC, checks the complete unchanged statement, proof and source interfaces and is adopted by the current decision.
That finding retains the accepted analytic foundations and unavailable final-journal identification as its explicit limits, with no formal verification claim.
