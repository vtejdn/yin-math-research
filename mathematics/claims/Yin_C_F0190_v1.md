---
author: Yin
---

# Marginal criteria for determinant limits under arbitrary and independent couplings

This candidate was developed for the distinct coupling requirements in [Wigner-pencil F0013](../tasks/Yin_T_F0013_v1.md#contract), [scalar-polynomial F0014](../tasks/Yin_T_F0014_v1.md#contract), [Haar-pencil F0015](../tasks/Yin_T_F0015_v1.md#contract), and [permutation F0016](../tasks/Yin_T_F0016_v1.md#contract).
Its statements are elementary probability reductions and do not prove the unresolved marginal estimates for a random-matrix model.
The argument was developed on 2026-11-05 by the coordinated determinant research agents for Yin.
No novelty or priority claim is made, and no earlier review is asserted to cover it.

<a id="statement"></a>
## Exact marginal criteria

For every positive integer \(N\), let \((\Omega_N,\mathcal F_N,\mu_N)\) be a standard Borel probability space of inputs, and let \(X_N:\Omega_N\to[-\infty,\infty)\) be measurable.
A coupling means any probability law on the sequence of inputs with these complete prescribed marginals.
The independent coupling is their product law.
Fix \(c\in\mathbb R\).

For the upper-limit assertions, assume
\[
 \limsup_{N\to\infty}X_N\le c
 \quad\text{almost surely under every coupling}.
 \tag{Upper}
\]
Then the following arbitrary-coupling statements are equivalent:
\[
 \begin{split}
 &\limsup_NX_N=c\quad\text{almost surely under every coupling};\\
 &\forall\eta>0:\quad\liminf_N\mu_N\{X_N<c-\eta\}=0;\\
 &\exists N_1<N_2<\cdots:\quad
 \mu_{N_k}\{X_{N_k}<c-1/k\}\le2^{-k}\quad\text{for all }k.
 \end{split}
 \tag{Arbitrary-limsup}
\]
Under (Upper), the independent coupling instead has \(\limsup_NX_N=c\) almost surely if and only if
\[
 \forall\eta>0:\quad
 \sum_N\mu_N\{X_N\ge c-\eta\}=\infty.
 \tag{Independent-limsup}
\]

Without needing (Upper), these full-limit statements are equivalent:
\[
 \begin{split}
 &X_N\to c\quad\text{almost surely under every coupling};\\
 &X_N\to c\quad\text{almost surely under the independent coupling};\\
 &\forall\varepsilon>0:\quad
 \sum_N\mu_N\{|X_N-c|>\varepsilon\}<\infty.
 \end{split}
 \tag{Full-limit}
\]
Use \(|-\infty-c|=\infty\).
Strict and non-strict thresholds give the same all-tolerance criteria after shrinking a tolerance.
These conclusions retain the full input law within each dimension, including any prescribed independence among entries or matrices.

If the target is \(c=-\infty\) and (Upper) holds with that extended value, every coupling already satisfies \(X_N\to-\infty\).
The finite-target recurrence and deviation criteria are not needed for that branch.

<a id="argument"></a>
## Complete candidate argument and application boundaries

The proof uses first Borel--Cantelli, the independent-event product calculation written below, ordinary conditional restriction to one positive-probability event, and countable product probability measures.
It invokes no new random-matrix theorem or unverified external estimate.
The first-Borel--Cantelli assertion follows directly from the union bound on tail unions and summability.

<a id="coupling-criterion"></a>
## Exact marginal criterion for an arbitrary-coupling upper limit

Use the prescribed input spaces, complete marginal laws and measurable statistics from the statement.
Fix \(c\in\mathbb R\), and assume that every coupling of the prescribed input laws satisfies \(\limsup_N X_N\le c\) almost surely.
Then the following are equivalent.

1. Every such coupling satisfies \(\limsup_N X_N=c\) almost surely.
2. For every \(\eta>0\), \(\liminf_N\mathbb P\{X_N<c-\eta\}=0\).
3. There is a deterministic increasing sequence \(N_k\) such that \(\mathbb P\{X_{N_k}<c-1/k\}\le2^{-k}\).

Condition 2 allows different favorable subsequences at different tolerances.
Choose \(N_k>N_{k-1}\) satisfying its tolerance \(1/k\) and failure bound \(2^{-k}\) to obtain condition 3.
First Borel--Cantelli then gives \(X_{N_k}\ge c-1/k\) eventually under every coupling, because its proof uses only the summable marginal failure probabilities.
Together with the assumed almost-sure upper bound this proves condition 1.

For necessity, suppose that some \(\eta>0\) has
\[
 b=\liminf_N\mathbb P(B_N)>0,
 \qquad B_N=\{X_N<c-\eta\}.
\]
Choose \(0<a<b\) and \(N_0\) such that \(\mathbb P(B_N)\ge a\) for \(N\ge N_0\).
Write the prescribed input law at dimension \(N\) as \(\mu_N\), and put \(\nu_N=\mu_N(\,\cdot\mid B_N)\).
Then \(\mu_N-a\nu_N\) is a nonnegative measure of mass \(1-a\), since on \(B_N\) its density with respect to \(\mu_N\) is \(1-a/\mu_N(B_N)\), and off \(B_N\) its density is one.
Define the residual probability law \(\rho_N=(\mu_N-a\nu_N)/(1-a)\).
Choose one Bernoulli variable \(Z\) of success probability \(a\).
Conditional on \(Z=1\), sample every input at \(N\ge N_0\) from \(\nu_N\); conditional on \(Z=0\), sample it from \(\rho_N\).
The conditional samples may be independent across dimensions in each branch, and the finitely many earlier dimensions can be sampled from their prescribed laws independently.
Each unconditional input marginal is exactly \(\mu_N\), so its within-dimension independence and entry laws are preserved.
On \(\{Z=1\}\), every \(N\ge N_0\) has \(X_N<c-\eta\), and therefore \(\limsup_N X_N\le c-\eta\).
This is a lawful coupling with a failure event of probability at least \(a\), contradicting condition 1.
The construction changes dependence between dimensions only.

For F0013 take \(X_N=(mN)^{-1}\log|\det L_N|\) and \(c=\log\Delta(L)\); for F0014 take \(X_N=N^{-1}\log|\det(P(W)-zI)|\).
The [regularized-potential argument](../ledger/Yin_L_F0061_v2.md#upper-limit) supplies the required upper bound for every allowed coupling.
The criterion applies when the free logarithm is finite; the \(c=-\infty\) branch is already settled by the upper bound.
It gives an exact lower-tail obligation, rather than establishing that obligation for the unresolved Wigner classes.
Unlike all-dimension probability convergence, it does not conflict with the real commutator's forced singularity at odd dimensions.

## Independent dimensions require a weaker recurrence estimate

For independent inputs at distinct dimensions, the events \(G_N(\eta)=\{X_N\ge c-\eta\}\) are independent.
Under the same almost-sure upper bound, the independent model has \(\limsup_N X_N=c\) almost surely if and only if
\[
 \sum_N\mathbb P(G_N(\eta))=\infty
 \quad\text{for every }\eta>0.
\]
If each sum diverges, second Borel--Cantelli and a countable intersection over positive rational tolerances give the lower bound.
If a sum is finite, first Borel--Cantelli gives only finitely many visits above its threshold, so \(\limsup_N X_N\le c-\eta\) almost surely.
Thus persistent positive good probability can suffice under independence even when an arbitrary coupling can align bad dimensions.
This comparison is relevant to the separate Haar and permutation contracts, whose coupling regimes are both explicit.


## Full convergence is equivalent in the two coupling regimes

For any prescribed scalar input marginals and finite constant \(c\), the following conditions are equivalent, without needing an a priori almost-sure upper bound.

1. \(X_N\to c\) almost surely under every coupling of the input laws.
2. \(X_N\to c\) almost surely when inputs at distinct dimensions are independent.
3. For every \(\varepsilon>0\), \(\sum_N\mathbb P\{|X_N-c|>\varepsilon\}<\infty\).

The first condition contains the independent coupling as a special case.
Under independent inputs, the deviation events are independent, and a divergent probability sum would make deviations occur infinitely often almost surely by second Borel--Cantelli.
Thus condition 2 implies condition 3.
Under condition 3, first Borel--Cantelli and intersection over positive rational tolerances give convergence under every coupling, proving condition 1.
For the second-Borel--Cantelli step one may use the direct product calculation: if independent event probabilities have divergent sum, the probability of avoiding every event after any fixed index is at most \(\prod(1-p_N)\le\exp(-\sum p_N)=0\).
These arguments work unchanged for \(X_N=-\infty\), interpreting its deviation from finite \(c\) as infinite.
The strict or non-strict threshold convention does not change any criterion quantified over every positive tolerance, since one may replace a tolerance by half of it.



## Current assessment

[Selected decision](#decision-coupling-criteria-reviewed)

## Assessment history

### Decision coupling-criteria-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:24 |
| status | open |
| reason | The complete elementary marginal criteria and explicit bad-event coupling are fixed as a candidate for mathematical review; no random-matrix lower-tail estimate or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact criteria](#statement) | Finite-target arbitrary and independent upper-limit criteria, full-convergence equivalence, and the separate minus-infinite upper-bound branch. |
| argument | [Complete candidate argument](#argument) | Explicit mixture coupling, subsequence extraction, independent-event recurrence and summable-deviation equivalence. |

### Decision coupling-criteria-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:34 |
| status | proved |
| reason | Independent review checked every elementary probability equivalence and the exact marginal-law mixture construction; no random-matrix lower-tail estimate is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact marginal criteria](#statement) | All finite-target arbitrary and independent upper-limit equivalences, full-convergence equivalence, and the separate minus-infinite upper-bound branch. |
| argument | [Complete probability proof](#argument) | Explicit failure coupling, deterministic subsequence, independent-event recurrence and summable-deviation equivalence. |
| review | [Independent marginal-criteria finding](../audits/reviews/Yin_R_F0196_v1.md#marginal-criteria-finding) | Complete stated elementary theorem and application boundaries; the unresolved matrix-model marginal estimates remain conditional obligations. |
