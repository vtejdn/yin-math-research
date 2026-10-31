---
author: Yin
---

# Finite liberation Fisher information gives normalized dual systems with bounded-vector domains

## Current assessment
[Selected decision](#decision-self-reviewed)

## Scope and retained input

The question is whether finite liberation Fisher information supplies implementing operators whose actual domains and adjoint domains contain all bounded vectors.
The general liberation contraction estimate is already retained in [C_F0063 Appendix A](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions).
This deduction makes the finite-information hypothesis, represented-derivation construction, two domain inclusions, commutator sign, normalization and ambient-algebra extension explicit.
It reuses that analytic argument without extending the scope of its earlier independent reviews.
The human explicitly requested fixed retention of this deduction if no adequate complete account existed.

## Statement

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, let \(H=L^2(M,\tau)\), and put \(\Omega=1\).
Elements of \(M\) act on \(H\) by left multiplication, and \(P_\Omega\) is the orthogonal projection onto \(\mathbb C\Omega\).
Fix \(d\geq1\) and an arbitrary tuple \(X=(X_1,\ldots,X_d)\in M^d\), and set
\[
 A_i=W^*(X_i),\qquad B_i=W^*(X_j:j\ne i),\qquad
 N=W^*(X_1,\ldots,X_d),
\]
with \(B_1=\mathbb C1\) when \(d=1\).
Use the trace restrictions for these algebras.
Assume that the [liberation Fisher information](../audits/literature/Voi99/Yin_U004.md#liberation-fisher-information) is finite:
\[
 \varphi^*(A_1;\ldots;A_d)=\sum_{i=1}^d\|j(A_i:B_i)\|_2^2<\infty.
 \tag{1}
\]
Then there are closed densely defined operators \(L_1,\ldots,L_d\) on \(H\) satisfying
\[
 M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*,
 \qquad [X_j,L_i]\xi=\delta_{ij}[X_i,P_\Omega]\xi
 \quad(\xi\in M\Omega),
 \tag{2}
\]
and
\[
 \sum_{i=1}^dL_i\xi=P_\Omega\xi\qquad(\xi\in M\Omega).
 \tag{3}
\]
No normality, generation of \(M\), or regularity of the scalar shifts is assumed.
The conclusion uses the [liberation dual-system domain variant](Yin_C_F0079_v4.md#liberation-dual-system), rather than Voi99's bounded selfadjoint definition.

<a id="sum-normalized-liberation-dual-system"></a>
**Definition (sum normalization).** A liberation dual system with the domain and commutator conditions in (2) is called normalized when it also satisfies (3).
This supplements the domain variant in [C_F0079 v4](Yin_C_F0079_v4.md#liberation-dual-system) and is distinct from requiring the individual operators to annihilate the vacuum.

## Argument

### Represented derivations and actual vacuum adjoints

Write \(j_i=j(A_i:B_i)\in L^2(N,\tau)\) and \(\mathcal A=\operatorname{Alg}(A_1,\ldots,A_d)\).
The [Voi99 convention](../audits/literature/Voi99/Yin_U003.md#liberation-derivation-and-gradient) is
\[
 \gamma_i(a)=a\otimes1-1\otimes a\quad(a\in A_i),\qquad
 \gamma_i(b)=0\quad(b\in B_i),\qquad
 \tau(j_ip)=(\tau\otimes\tau)(\gamma_i p).
 \tag{4}
\]
Tensor products here are algebraic, with outer bimodule actions.
If gradients are formulated directly through word moments, well-definedness on the represented algebra follows as below; algebraic freeness need not be added as a hypothesis.

Let \(\pi:*_{k=1}^d A_k\to\mathcal A\) be evaluation from the unital algebraic free product.
The first two rules in (4) define a formal derivation on this free product, and let \(\widetilde\gamma_i\) be its value after evaluating both tensor factors.
For \(r\in\ker\pi\) and arbitrary free-product elements \(u,v\), the moment identity and Leibniz rule give
\[
 0=\tau(j_i\pi(urv))
   =(\tau\otimes\tau)
      \bigl(\pi(u)\cdot\widetilde\gamma_i(r)\cdot\pi(v)\bigr).
 \tag{5}
\]
Every other Leibniz term contains \(\pi(r)=0\).
The tests in (5) separate \(\mathcal A\odot\mathcal A\) by the faithful product-trace pairing: choosing the two factors as adjoints tests against every elementary tensor in the dense subspace \(\mathcal A\odot\mathcal A\subset L^2(N)\otimes_2L^2(N)\).
Thus \(\widetilde\gamma_i(r)=0\), so \(\gamma_i\) descends to the represented algebra.

The source gives \(j_i^*=-j_i\) and \(\gamma_i^*(1\otimes1)=-j_i\).
Set
\[
 \delta_i=\mathrm i\gamma_i,\qquad
 \eta_i=\delta_i^*(1\otimes1)=\mathrm i j_i=\eta_i^*.
 \tag{6}
\]
These are actual Hilbert adjoints for the dense core \(\mathcal A\Omega\subset H_N:=L^2(N,\tau)\).
Use \(\langle p,q\rangle=\tau(q^*p)\), linear in the first variable.
The identity \(\gamma_i(p^*)=-(\gamma_i p)^\dagger\), where \((a\otimes b)^\dagger=b^*\otimes a^*\), makes \(\delta_i\) real, and \(\|\eta_i\|_2=\|j_i\|_2\).

Define
\[
 C_i^\circ(p\Omega)=(\operatorname{id}\otimes\tau)\delta_i(p),
 \qquad p\in\mathcal A.
 \tag{7}
\]
The [actual tensor-adjoint formula of Mai15 Lemmas 4.3 and 4.7](../audits/literature/Mai15/Yin_U001.md#the-stronger-formulas-and-estimates) yields
\[
 \mathcal A\Omega\subseteq\operatorname{Dom}(C_i^\circ)^*,\qquad
 (C_i^\circ)^*(p\Omega)=p\eta_i-C_i^\circ(p\Omega).
 \tag{8}
\]
Indeed \(\mathcal A\odot\mathcal A\subseteq\operatorname{Dom}\delta_i^*\), and the adjoint of the bounded partial trace sends \(p\Omega\) to \(p\otimes1\).
Thus (8) is the actual Hilbert-adjoint identity \(\delta_i^*(p\otimes1)\), and proves closability of \(C_i^\circ\).
Put \(C_i=\overline{C_i^\circ}\), so \(C_i^*=(C_i^\circ)^*\).

### Application of the retained analytic estimate

The exact defect is
\[
 (\delta_i\otimes\operatorname{id})\delta_i
  -(\operatorname{id}\otimes\delta_i)\delta_i
   =\mathrm i\kappa\delta_i,\qquad
 \kappa(a\otimes b)=a\otimes1\otimes b.
 \tag{9}
\]
Both sides are outer derivations into the triple tensor product; the mixed Leibniz terms cancel on the left.
On \(a\in A_i\) both sides equal \(-a\otimes1\otimes1+1\otimes1\otimes a\), and on each other coordinate algebra both vanish.
This proves (9) on \(\mathcal A\).

The final abstract liberation case of [C_F0063 Appendix A](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) therefore applies.
Its hypotheses are now verified: a weakly dense unital star algebra, algebraic tensor values, reality, an actual \(L^2\) vacuum, and the precise defect (9).
The retained proof contracts (9) to an energy identity with its first-order term, and applies the differentiated binomial series to the analytic unitaries \(a+\mathrm i(1-a^2)^{1/2}\), where \(a=a^*\in\mathcal A\) and \(\|a\|<1\).
Those steps require no normal-generator or conjugate-variable construction after the stated interfaces are supplied.
They give
\[
 \|C_i^\circ(p\Omega)\|_2\le(4\|\eta_i\|_2+2)\|p\|,
 \qquad
 \|(C_i^\circ)^*(p\Omega)\|_2\le(5\|\eta_i\|_2+2)\|p\|
 \quad(p\in\mathcal A).
 \tag{10}
\]
The second bound also follows from the first and (8).
This invokes the controlled-defect argument, not Mai15 Theorem 4.9, whose coassociativity premise fails in (9).
These are operator-norm-to-Hilbert-norm estimates, not bounded-operator estimates on \(H_N\).

### Both actual domains contain bounded vectors

For \(x\in N\), [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) gives a net \(p_\lambda\in\mathcal A\) with \(\|p_\lambda\|\le\|x\|\) and \(p_\lambda\Omega\to x\Omega\) in \(H_N\).
By (10), the pairs
\[
 \bigl(C_i^\circ(p_\lambda\Omega),(C_i^\circ)^*(p_\lambda\Omega)\bigr)
\]
are bounded in the reflexive Hilbert space \(H_N\oplus H_N\), and have a weakly convergent subnet.
The graphs of \(C_i\) and \(C_i^*\) are norm-closed linear subspaces, hence weakly closed.
The two graph limits prove
\[
 N\Omega\subseteq\operatorname{Dom}C_i\cap\operatorname{Dom}C_i^*.
 \tag{11}
\]
Weak lower semicontinuity preserves the constants in (10).
This is the bounded-net/closed-graph mechanism retained in [C_F0027 Section 5](Yin_C_F0027_v1.md#5-the-two-core-estimates-restore-the-entire-bounded-domain), applied to the actual closure and actual adjoint.
An arbitrary extension of a bounded map from \(N\) to \(H_N\) would not by itself establish (11).

### Commutators and sum normalization

The Leibniz rule gives, for \(p\in\mathcal A\),
\[
 [C_i^\circ,X_j](p\Omega)
  =\mathrm i\delta_{ij}\bigl(X_i\tau(p)-\tau(X_ip)1\bigr)
  =\mathrm i\delta_{ij}[X_i,P_\Omega](p\Omega).
 \tag{12}
\]
Since \(\mathcal A\Omega\) is a graph core for \(C_i\) and the right side is bounded, graph approximation extends (12) to \(\operatorname{Dom}C_i\), which each \(X_j\) preserves.
Consequently \([X_j,\mathrm i C_i]=\delta_{ij}[X_i,P_\Omega]\), with the generator-first sign in (2).

On \(\mathcal A\), the sum of the coordinate derivations is the inner derivation \(p\mapsto p\otimes1-1\otimes p\).
Hence
\[
 \sum_i C_i^\circ(p\Omega)=\mathrm i(p\Omega-P_\Omega p\Omega).
\]
For \(x\in N\), use one bounded Kaplansky net and a common weakly convergent subnet for the finitely many vectors \(C_i^\circ(p_\lambda\Omega)\).
Their graph limits are \(C_i(x\Omega)\), so
\[
 \sum_i\mathrm i C_i(x\Omega)=P_\Omega(x\Omega)-x\Omega.
 \tag{13}
\]
Set \(\ell_i=\mathrm i C_i+d^{-1}I_{H_N}\), with domain \(\operatorname{Dom}C_i\).
Bounded perturbation gives a closed operator and
\(\ell_i^*=-\mathrm i C_i^*+d^{-1}I_{H_N}\), with domain \(\operatorname{Dom}C_i^*\).
Equations (11)--(13) give the required domains, commutators and sum identity on \(N\Omega\).
Also \(\ell_i\Omega=d^{-1}\Omega\).

### The ambient algebra

Let \(E_N:M\to N\) be the trace-preserving conditional expectation.
Its standard finite-tracial implementation is the orthogonal projection \(e_N:H\to H_N\), with \(e_N(x\Omega)=E_N(x)\Omega\).
This is the conditional-expectation interface used in the [Voi99 source account](../audits/literature/Voi99/Yin_U003.md#results-and-checked-mechanisms).
The subspace \(H_N\) reduces left multiplication by every element of \(N\).
On \(H=H_N\oplus H_N^\perp\), define
\[
 L_i=\ell_i\oplus0,\qquad
 \operatorname{Dom}L_i=\operatorname{Dom}\ell_i\oplus H_N^\perp.
 \tag{14}
\]
Then \(L_i\) is closed and \(L_i^*=\ell_i^*\oplus0\), with the corresponding direct-sum domain.
For \(x\in M\), its \(H_N\) component is the bounded vector \(E_N(x)\Omega\); (11) therefore proves both inclusions in (2).
The commutators extend by reduction, since \(X_j\in N\) and \(P_\Omega\) vanishes on \(H_N^\perp\).
The sum is \(P_\Omega\) on \(N\Omega\) and zero on \(H_N^\perp\), proving (3) on every \(x\Omega\in M\Omega\).

## Applicability and limits

Condition (1) concerns the separate coordinate algebras; \(\varphi^*(N:\mathbb C)=0\) is not a replacement when \(d>1\).
The conclusion does not assert boundedness or selfadjointness of the operators on \(H\), and does not reverse Voi99 Proposition 13.3 in the bounded selfadjoint category.
It supplies no ordinary dual system, conjugate variables, nonatomic law or regularity of every scalar shift.
For example, for a single nontrivial projection \(X_1\), the gradient relative to scalars is zero and the construction gives \(L_1=P_\Omega\), although the spectral law has atoms and \(X_1\) is not regular.
This normalized one-coordinate choice remains \(P_\Omega\) even in a larger ambient algebra.

The source interfaces are Voi99 Sections 5.3--5.4, Proposition 6.1 and Definition 9.1, and Mai15 Lemmas 4.3 and 4.7, at the editions and inspection scopes in the linked source units.
The step from those interfaces to both full bounded-vector domains is the present project deduction using the retained liberation estimate.
No source is claimed to state this entire conclusion verbatim, and the bounded literature search does not establish novelty.
Earlier independent reviews of C_F0063 retain their actual input scope and do not automatically review this generalized formulation.

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-28T08:58 |
| status | open |
| reason | Complete finite-information deduction retained for reuse; the assembled statement and both domain conditions await their recorded self-review. |

Recorded role label: corollary.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary bounded tuples with finite coordinate liberation Fisher information admit closed normalized liberation duals with both full bounded-vector domains. |
| argument | [Argument](#argument) | Represented derivation, signed vacuum, actual adjoint, retained energy estimate, two weak graph limits, commutators, sum normalization and ambient extension. |
| dependency | [Liberation estimate](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Only the abstract algebraic-liberation estimate with an actual L2 vacuum and its real controlled-defect proof; no normal-core or rationality premise is imported. |
| dependency | [Gradient source interface](../audits/literature/Voi99/Yin_U003.md#voi99-u003) | Word-moment gradient, skewadjointness, the signed actual vacuum, and the accepted finite-tracial conditional-expectation interface; represented well-definedness is proved here. |
| dependency | [Fisher information](../audits/literature/Voi99/Yin_U004.md#voi99-u004) | Definition 9.1 for the coordinate algebras, so each coordinate gradient lies in L2. |
| dependency | [Actual tensor adjoints](../audits/literature/Mai15/Yin_U001.md#mai15-u001) | Lemmas 4.3 and 4.7 for a real derivation with an L2 vacuum; the coassociative norm theorem is not invoked. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded core approximation, accepted at the retained statement-and-applicability inspection depth. |

### Decision self-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-28T09:01 |
| status | proved |
| reason | Adopt the complete assembled deduction after its recorded authoring-agent self-review, including both actual bounded-vector domains, the generator-first sign, sum normalization and ambient extension; no independent review of this generalized statement is claimed. |

Recorded role label: corollary.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary bounded tuples with finite coordinate liberation Fisher information admit closed normalized liberation duals with both full bounded-vector domains. |
| argument | [Argument](#argument) | Represented derivation, signed vacuum, actual adjoint, retained energy estimate, two weak graph limits, commutators, sum normalization and ambient extension. |
| dependency | [Liberation estimate](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Only the abstract algebraic-liberation estimate with an actual L2 vacuum and its real controlled-defect proof; no normal-core or rationality premise is imported. |
| dependency | [Gradient source interface](../audits/literature/Voi99/Yin_U003.md#voi99-u003) | Word-moment gradient, skewadjointness, the signed actual vacuum, and the accepted finite-tracial conditional-expectation interface; represented well-definedness is proved here. |
| dependency | [Fisher information](../audits/literature/Voi99/Yin_U004.md#voi99-u004) | Definition 9.1 for the coordinate algebras, so each coordinate gradient lies in L2. |
| dependency | [Actual tensor adjoints](../audits/literature/Mai15/Yin_U001.md#mai15-u001) | Lemmas 4.3 and 4.7 for a real derivation with an L2 vacuum; the coassociative norm theorem is not invoked. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded core approximation, accepted at the retained statement-and-applicability inspection depth. |
| review | [Whole deduction self-review](../audits/reviews/Yin_R_F0080_v1.md#whole-deduction) | Complete statement, argument and each accepted input interface, with actual self-reviewed relationship and the bounded-selfadjoint, scalar-shift and source-scope limits retained. |

