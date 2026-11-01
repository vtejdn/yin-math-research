---
author: Yin
---
# The arcsine liberation dual does not yield an ordinary dual or a finite-rank rationality criterion

Context: the human requested a fixed account of the further consequences of the arcsine counterexample in [C_F0080](Yin_C_F0080_v1.md#statement).
This Claim retains the new ordinary-dual obstruction and the failure of a finite-rank test using the liberation dual.
It does not revise the original conjugate-variable counterexample.

## Statement

Let
\[
 d\mu(x):=\frac{1_{(-1,1)}(x)}{\pi\sqrt{1-x^2}}\,dx,
 \qquad M:=L^\infty((-1,1),\mu),\qquad
 \tau(f):=\int f\,d\mu,
\]
and let \(X(x):=x\), \(H:=L^2(M,\tau)\), \(\Omega:=1\), with M represented on H by multiplication.
Let \(P_\Omega\) be the orthogonal projection onto the constants and set \(L:=P_\Omega\).
The following conclusions hold.

1. The selfadjoint generator X has nonatomic spectral distribution, every scalar shift X-lambda is regular, and L is a bounded selfadjoint normalized liberation dual system.
   There is nevertheless no densely defined linear operator D on H satisfying
   \[
    M\Omega\subseteq\operatorname{Dom}D\cap\operatorname{Dom}D^*,
    \qquad [X,D]|_{M\Omega}=P_\Omega|_{M\Omega}.
   \]
   Thus existence of a liberation dual system does not imply existence of an ordinary dual system with these common-domain conditions, even for a normal nonatomic generator.
2. For every \(u\in L^0(M)\) and every fraction pair \(Q=(s,a,b,t)\in M^4\) for u, the fraction commutator
   \[
    \Gamma[Q,L]:=sLb-aLt=sP_\Omega b-aP_\Omega t
   \]
   is bounded on H and has rank at most two.
   But the nontrivial projection \(p:=1_{(0,1)}(X)\) does not belong to \(\operatorname{Div}_{L^0(M)}\mathbb C[X]\), and \(Q=(1,p,p,1)\) is a fraction pair for p.
   Consequently the condition that the fraction commutator with this liberation dual has finite rank, even for every fraction pair, does not characterize rationality.

Here a fraction pair means that s and t are regular elements of M and \(u=s^{-1}a=bt^{-1}\) in \(L^0(M)\).
Regular means injective with dense range, equivalently invertible as an affiliated operator.
A normalized liberation dual for the one-element tuple means an operator L with \(M\Omega\subseteq\operatorname{Dom}L\cap\operatorname{Dom}L^*\), \([X,L]=[X,P_\Omega]\) on M Omega, and \(L=P_\Omega\) on M Omega.
An affiliated operator is rational here precisely when it belongs to the division closure of C[X] in L0(M).
The inner product on H is linear in its second entry, and \([A,B]:=AB-BA\).

## Argument

### The common counterexample and moment input

[C_F0080](Yin_C_F0080_v1.md#the-operator-and-its-liberation-dual) proves that X is a selfadjoint generator with nonatomic spectral distribution, that every X-lambda is regular, and that L=P_Omega has the stated domain, commutator and normalization properties.
We reuse those unchanged conclusions.
The elementary arcsine moment calculation in [C_F0080](Yin_C_F0080_v1.md#failure-of-the-vacuum-adjoint-condition) gives
\[
 m_{2r}:=\tau(X^{2r})=4^{-r}\binom{2r}{r},
 \qquad m_{2r+1}:=0,
 \qquad\sum_{r=0}^{n}m_{2r}m_{2(n-r)}=1.
\]
It also gives
\[
 \|X^{2n+1}\Omega\|_2\longrightarrow0,
\]
since |x|<1 almost everywhere and dominated convergence applies.

### Absence of an ordinary dual

Suppose D satisfies the common-domain and commutator conditions in the statement.
Every vector \(X^k\Omega\) belongs to M Omega and hence to Dom D; M Omega is invariant under multiplication by X.
Thus the generator relation can be applied successively to \(X^k\Omega\), and every term in the following telescoping identity is defined:
\[
 [X^k,D]\Omega
 =\sum_{j=0}^{k-1}X^jP_\Omega X^{k-1-j}\Omega
 \qquad(k\geq1).
\]
No invariance of Dom D under X outside M Omega is required.
For \(k=2n+1\), taking the vacuum expectation and using the moment identity yields
\[
 \begin{aligned}
 \langle\Omega,[X^{2n+1},D]\Omega\rangle
 &=\sum_{j=0}^{2n}\tau(X^j)\tau(X^{2n-j})\\
 &=\sum_{r=0}^{n}m_{2r}m_{2(n-r)}=1.
 \end{aligned}
\]
On the other hand, X is selfadjoint, \(\Omega\in\operatorname{Dom}D^*\), and \(X^{2n+1}\Omega\in\operatorname{Dom}D\), so the defining adjoint identity gives
\[
 \begin{aligned}
 1
 &=\left|\langle X^{2n+1}\Omega,D\Omega\rangle
       -\langle D^*\Omega,X^{2n+1}\Omega\rangle\right|\\
 &\leq\bigl(\|D\Omega\|_2+\|D^*\Omega\|_2\bigr)
             \|X^{2n+1}\Omega\|_2\longrightarrow0.
 \end{aligned}
\]
This contradiction proves the first conclusion.
In fact the proof needs only that C[X] Omega lie in Dom D, that the generator commutator hold there, and that Omega lie in Dom D*.
No implication from ordinary dual systems to conjugate variables is invoked.

### Finite-rank fraction commutators for every affiliated element

For any fraction pair Q, all four coefficients s,a,b,t act boundedly on H, and L=P_Omega is bounded on H.
The natural composition domain of Gamma[Q,L] is therefore all of H.
For every \(\xi\in H\),
\[
 \Gamma[Q,L]\xi
 =s\Omega\,\langle\Omega,b\xi\rangle
  -a\Omega\,\langle\Omega,t\xi\rangle.
\]
Its range is contained in \(\operatorname{span}\{s\Omega,a\Omega\}\), so its rank is at most two.
In particular it equals its Hilbert-space closure.
This argument applies to every u and every fraction pair for u; it makes no rationality assumption.

### A nonrational projection with finite-rank fraction commutators

Every nonzero polynomial has finitely many zeros, so it is nonzero mu-almost everywhere and has an inverse in L0(M).
Consequently scalar rational functions give an embedded field C(X) inside L0(M).
This field is division closed in L0(M): every one of its nonzero elements already has its rational-function inverse in C(X).
Conversely, any division-closed subring of L0(M) containing C[X] contains the inverse of every nonzero polynomial and hence contains C(X).
It follows that
\[
 \operatorname{Div}_{L^0(M)}\mathbb C[X]=\mathbb C(X).
\]
The projection \(p:=1_{(0,1)}(X)\) has trace 1/2, so it is neither zero nor one.
A field has no idempotents other than zero and one; therefore p does not lie in C(X).
The unit denominators in \(Q=(1,p,p,1)\) are regular, and \(p=1^{-1}p=p1^{-1}\), so Q is a valid fraction pair.
For this Q,
\[
 \Gamma[Q,L]=P_\Omega p-pP_\Omega=[P_\Omega,p]\in\mathcal F(H).
\]
The preceding range argument also gives finite rank for every other fraction pair for p.
This proves the failure of the proposed finite-rank characterization.

## Dependencies and limits

The only project proof input is the fixed construction, arcsine moments and L2 convergence from [C_F0080](Yin_C_F0080_v1.md#argument).
The remaining steps use direct commutator telescoping, the Hilbert-space adjoint identity, a rank-two range calculation and elementary facts about fields and scalar rational functions.
The ordinary-dual nonexistence proved here prevents this example from contradicting any rationality theorem whose hypotheses require an ordinary dual with the stated common-domain conditions.
It instead disproves replacing that hypothesis and its tested operators by the existence of a liberation dual and the finite-rank condition for its fraction commutators.
This claim does not assert failure of a characterization requiring membership in the commutator image \([X,\mathcal F(H)]\), which is a stronger requirement than finite rank.
It makes no comparison between existence of conjugate variables and ordinary dual systems for other tuples.
No historical novelty or literature-wide priority claim is made.

## Current assessment
[Selected decision](#decision-accepted-consequences)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.
The recorded Claim label was `corollary`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:42 |
| status | open |
| reason | The complete ordinary-dual obstruction and the finite-rank failure for liberation duals are fixed as a new deduction from the accepted arcsine counterexample, pending independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Nonatomic selfadjoint arcsine generator with a normalized liberation dual but no ordinary dual, and failure of a finite-rank rationality test using its liberation dual. |
| argument | [Argument](#argument) | Complete domain-checked vacuum obstruction, rank-two calculation and nonrational projection. |
| dependency | [C_F0080 argument](Yin_C_F0080_v1.md#argument) | The unchanged arcsine operator construction, regular scalar shifts, liberation dual, moments and L2 convergence. |

### Decision accepted-consequences

The recorded Claim label was `corollary`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:47 |
| status | proved |
| reason | The complete independent review verified the ordinary-dual obstruction, all fraction-pair quantifiers, the rank bound and the nonrational projection, with no remaining mathematical gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Nonatomic selfadjoint arcsine generator with a normalized liberation dual but no ordinary dual, and failure of the finite-rank rationality test using its liberation dual. |
| argument | [Argument](#argument) | Complete domain-checked vacuum obstruction, rank-two calculation and nonrational projection. |
| dependency | [C_F0080 argument](Yin_C_F0080_v1.md#argument) | The unchanged arcsine operator construction, regular scalar shifts, liberation dual, moments and L2 convergence. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0172_v1.md#whole-proof-finding) | All statement and argument sections, exact domains and signs, universal fraction quantifiers, direct input interface and rational-function division closure. |
