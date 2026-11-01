---
author: Yin
---

# Sum normalization and the full fraction-commutator liberation criterion

This version extends the [fixed v4 criterion](Yin_C_F0079_v4.md#statement) by retaining general sum normalization and a fourth equivalent condition on full natural-domain fraction commutators.
The v4 maximal-Delta, tensor-recovery and three-condition arguments remain the exact inputs specified below; their original assessments and reviews retain their scopes.
No normality, generation or finite-information assumption is added.

## Statement

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, let \(H=L^2(M,\tau)\), \(\Omega=1\), and \(U=L^0(M)\).
Elements of \(M\) act by left multiplication, \(\rho(x)\) denotes right multiplication by \(x\), and \(P_\Omega\) projects onto \(\mathbb C\Omega\).
Fix \(d\geq1\) and \(X=(X_1,\ldots,X_d)\in M^d\).
A liberation dual system means the [v4 domain formulation](Yin_C_F0079_v4.md#liberation-dual-system):
\[
 M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*,\qquad
 [X_j,L_i]\xi=\delta_{ij}[X_i,P_\Omega]\xi
 \quad(\xi\in M\Omega).
\]
Only these generator relations are required; adjoint-generator or von Neumann algebra relations are not assumed.

<a id="sum-normalization"></a>
Use the [sum-normalization convention](Yin_C_F0082_v1.md#sum-normalized-liberation-dual-system): a system is sum-normalized if
\[
 \sum_{i=1}^dL_i\xi=P_\Omega\xi\qquad(\xi\in M\Omega).
\]
**General normalization lemma.** Every liberation dual system for any bounded tuple admits a sum-normalized replacement on \(M\Omega\).
The replacement operators and their adjoints contain \(M\Omega\) in their domains, and their closures may also be used.
This assertion needs no scalar-shift regularity, normality, generation or finite-information hypothesis.
It asserts preservation of the relations on \(M\Omega\), not equality with the original full operator domains.

For the following criterion additionally assume that \(X_i-\lambda\) is invertible in \(U\) for every \(i\) and every \(\lambda\in\mathbb C\), and fix any sum-normalized liberation dual system \((L_i)\).
Put \(A_X=\mathbb C\langle X_1,\ldots,X_d\rangle\).
A fraction pair for \(u\in U\) is \(Q=(s,a,b,t)\) with \(s,a,b,t\in M\), \(s,t\) regular, and \(u=s^{-1}a=bt^{-1}\).
Define
\[
 \Gamma[Q,L_i]=sL_ib-aL_it,
 \qquad
 \operatorname{Dom}\Gamma[Q,L_i]
 =\{\xi\in H:b\xi,t\xi\in\operatorname{Dom}L_i\}.
\]
Write \(\mathcal F(H)\) for the bounded finite-rank operators on \(H\).
**Four-condition criterion.** For every \(u\in U\), the following are equivalent:

1. \(u\in\operatorname{Div}_{U}A_X\).
2. For some fraction pair \(Q\), there exist \(T_1,\ldots,T_d\in\mathcal F(H)\) such that
   \[
    \sum_i[\rho(X_i),T_i]=\Gamma[Q,P_\Omega]
    =sP_\Omega b-aP_\Omega t.
   \]
3. For every fraction pair \(Q\), there exist such finite-rank certificates.
4. For every fraction pair \(Q\), there exist \(T_1,\ldots,T_d\in\mathcal F(H)\) such that
   \[
    \overline{\Gamma[Q,L_i]}=[\rho(X_i),T_i]
    \qquad(1\leq i\leq d).
   \]

For a fixed \(Q\), the certificate tuple is unique, and the witnesses in condition 4 are that same tuple.
The closures in condition 4 are closures of the full natural-domain operators just defined.
The criterion holds for every choice of sum-normalized system, not just the replacement from the lemma.

## Argument

### General sum normalization

Given a system, define on \(M\Omega\)
\[
 C=\sum_kL_k-P_\Omega,\qquad
 \widetilde L_i=L_i-\frac1dC.
\]
Since bounded multiplication preserves \(M\Omega\), every displayed composition is defined there, and
\[
 [X_j,C]=\sum_k\delta_{kj}[X_k,P_\Omega]-[X_j,P_\Omega]=0.
\]
Thus \([X_j,\widetilde L_i]=\delta_{ij}[X_i,P_\Omega]\) and \(\sum_i\widetilde L_i=P_\Omega\) on \(M\Omega\).
For \(\eta,\xi\in M\Omega\), with the inner product linear in the second variable,
\[
 \langle\eta,\widetilde L_i\xi\rangle
 =\left\langle
 L_i^*\eta-\frac1d\sum_kL_k^*\eta+\frac1dP_\Omega\eta,\xi
 \right\rangle.
\]
The vector in the first slot belongs to \(H\), proving \(M\Omega\subseteq\operatorname{Dom}\widetilde L_i^*\).
The operators are densely defined and closable.
Passing to their closures preserves their values and relations on \(M\Omega\); the adjoints retain that domain as well.
This proves the lemma without imposing a commutant extension for any unbounded operator.

### Retained inputs and the full natural domain

Use [v4's maximal-Delta proposition and tensor recovery](Yin_C_F0079_v4.md#argument), with regularity of every scalar shift and the displayed common domains.
In particular \(\Delta(X)=d\), and [v4's rationality proof](Yin_C_F0079_v4.md#proof-of-the-rationality-criterion) supplies conditions 1–3 and fixed-pair certificate uniqueness.
That proof uses [C_F0068 Part A](Yin_C_F0068_v1.md#argument) for arbitrary bounded tuples, with its stated certificate-sign conversion; no new inspection of the original external inputs is asserted here.

The natural domain of \(\Gamma[Q,L_i]\) contains \(M\Omega\).
For \(\eta\in M\Omega\) and \(\xi\) in that natural domain,
\[
 \langle\eta,\Gamma[Q,L_i]\xi\rangle
 =\langle b^*L_i^*(s^*\eta)-t^*L_i^*(a^*\eta),\xi\rangle.
\]
All inputs to \(L_i^*\) are bounded vectors, so the formula proves \(M\Omega\subseteq\operatorname{Dom}\Gamma[Q,L_i]^*\).
Hence the full natural-domain operator is densely defined and closable, independently of rationality.

### Rationality implies condition 4

Suppose condition 1 holds and fix any fraction pair \(Q\).
Use the exact algebraic tensors from the v4 rationality proof:
\[
 h:=a\otimes t^{\mathrm{op}}-s\otimes b^{\mathrm{op}}
   =\sum_i\Psi_i(\ell_i),\qquad
 \Psi_i(k)=k(X_i\otimes1-1\otimes X_i^{\mathrm{op}}).
\]
For bounded tensors set \(\Phi_i(c\otimes e^{\mathrm{op}})=cL_ie|_{M\Omega}\), and use the v4 identification \(\Theta(c\otimes e^{\mathrm{op}})=cP_\Omega e\).
The [v4 tensor-recovery argument](Yin_C_F0079_v4.md#proof-of-tensor-recovery) proves
\[
 \ell_i\in H\otimes_{\mathbb C}H,\qquad
 \overline{\Phi_i(h)}=\Theta(\Psi_i(\ell_i)).
\]
In particular this closure is bounded and defined on all \(H\).
On \(M\Omega\), \(\Phi_i(h)=-\Gamma[Q,L_i]\).
The closure of the full natural-domain operator therefore extends \(-\overline{\Phi_i(h)}\), which is already an operator on all \(H\), so they are equal.
Put \(T_i=-\Theta(\ell_i)\in\mathcal F(H)\).
The v4 tensor-commutator identity gives
\[
 \overline{\Gamma[Q,L_i]}
 =-\Theta(\Psi_i(\ell_i))=[\rho(X_i),T_i].
\]
Since \(Q\) was arbitrary, condition 4 follows.

### Condition 4 implies the certificate and closes the cycle

Assume condition 4 and fix any fraction pair \(Q\) and its witnesses \(T_i\).
On \(M\Omega\), the sum normalization applies at both \(b\xi\) and \(t\xi\), giving
\[
 \sum_i[\rho(X_i),T_i]\xi
 =\sum_i\Gamma[Q,L_i]\xi
 =s\Bigl(\sum_iL_i\Bigr)b\xi-a\Bigl(\sum_iL_i\Bigr)t\xi
 =(sP_\Omega b-aP_\Omega t)\xi.
\]
Both end operators are bounded, so density extends this equality to all \(H\), proving condition 3.
Every affiliated operator has a fraction pair, so 3 implies 2.
The v4 criterion gives 2 implies 1, completing the cycle.
Any witnesses in condition 4 satisfy the certificate equation, so v4's fixed-pair uniqueness identifies them with the unique certificate tuple.

### Scope and normalization distinction

The general replacement lemma requires neither finite liberation Fisher information nor regularity of scalar shifts.
Regularity is required for the criterion and the reused maximal-Delta and tensor-recovery inputs.
No boundedness or selfadjointness of the \(L_i\), equality of their original full domains, or commutation with adjoint generators is concluded.
The sum identity for fraction commutators is first used on \(M\Omega\) under condition 4, then extended between bounded operators; it is not an unrestricted assertion about sums of arbitrary unbounded closures.
The [zero-vacuum existence normalization in v4](Yin_C_F0079_v4.md#vacuum-normalization) is a separate convention.
In a sum-normalized system \(\sum_iL_i\Omega=\Omega\), so its coordinates cannot all annihilate \(\Omega\).

## Current assessment
[Selected decision](#decision-sum-normalization-reviewed)

## Assessment history

### Decision sum-normalization-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-01T06:23 |
| status | open |
| reason | Retain the general sum correction and full natural-domain fourth characterization as an extension of the same liberation criterion; the complete added argument awaits its own fixed mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | General sum normalization for arbitrary bounded tuples and the four-condition criterion under regularity of every scalar shift. |
| argument | [Argument](#argument) | Common-domain sum correction and adjoint inclusion, full natural-domain closability, fourth-condition cycle and certificate uniqueness. |
| dependency | [Fixed v4](Yin_C_F0079_v4.md#argument) | Existing maximal-Delta, tensor-recovery and three-condition rationality arguments, including the precise algebraic tensor and sign interfaces reused here. |

### Decision sum-normalization-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-01T06:29 |
| status | proved |
| reason | Adopt the separately arranged whole-v5 mathematical finding for the general sum correction and four-condition criterion, at its exact fixed-input and source-inspection limits. Earlier versions and their selected evidence retain their own scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | General sum normalization for arbitrary bounded tuples and the four-condition criterion for every affiliated element and every sum-normalized system under regularity of every scalar shift. |
| argument | [Argument](#argument) | Complete sum correction, adjoint inclusion, full natural-domain closure, tensor-sign conversion, implication cycle and fixed-pair uniqueness. |
| dependency | [Fixed v4](Yin_C_F0079_v4.md#argument) | Necessary fixed maximal-Delta, tensor-recovery and three-condition rationality interfaces, with the exact accepted C_F0068 Part A scope. |
| review | [Whole v5 finding](../audits/reviews/Yin_R_F0093_v1.md#whole-v5-finding) | Complete exact v5 statement and argument, with necessary v4 interfaces checked and retained external inputs accepted at their stated limits; independently arranged mathematical review, not manuscript review or maintenance acceptance. |
