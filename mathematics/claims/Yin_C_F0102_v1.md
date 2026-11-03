---
author: Yin
---

# Weighted local dual orbits give automatic adjoint modules; coordinate-commuting projection windows suffice

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Projective Spectral Phases on Small Left Modules

<a id="statement"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Authorized scope: [Yin_T_F0005 Q1](../tasks/Yin_T_F0005_v1.md#yin_t_f0005).
The sufficient-condition deduction in Section 2 is registered as ordinary Claim Yin_C_F0102 after [complete independent review](../audits/reviews/Yin_R_F0112_v1.md#6-analytic-continuation-boundary-and-verification-limits).
Provenance: project deduction using the inputs below; no novelty is asserted.
The reviewed auxiliary obstruction and continuation boundary remain in Sections 3-4.
No proof-version replacement or goal-completion assertion is made.

## 1. Question and Reuse

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite faithful tracial \((\mathcal M,\tau)\), put \(H=L^2(\mathcal M)\), and let \(D_i:E\to H\) be closable normalized duals on an arbitrary dense left \(\mathcal M\)-module:
\[
[D_i,X_j]|_E=\delta_{ij}P_\Omega.
\]
The question is whether Yin_C_F0039's projectively summable conjugate spectral phase supplies dense left modules in the **actual** \(D_i^*\) domains, without assuming \(E=\mathcal M\) or a bounded reference dual.

The reuse check read [Yin_C_F0037](Yin_C_F0037_v1.md#yin_c_f0037), [Yin_C_F0039](Yin_C_F0039_v1.md#yin_c_f0039), [Yin_C_F0085](Yin_C_F0085_v1.md#yin_c_f0085), [Yin_C_F0086](Yin_C_F0086_v1.md#yin_c_f0086), and [Yin_C_F0040](Yin_C_F0040_v1.md#yin_c_f0040).
Yin_C_F0037 already determines the bounded Hilbert-Schmidt starred commutators.
Yin_C_F0086 supplies countable intersections, graph-core restriction and the non-Hermitian local-form argument.
Yin_C_F0040 concerns a different domain and vacuum-adjoint hypothesis; it does not turn the present \(E\) into a polynomial or all-bounded-vector domain.

Local literature was then checked: [Dab14's projective tensor conventions](../audits/literature/Dab14/Yin_U002.md#projective-tensor-action), [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005), and NS06 Definition 5.6, Example 5.7 and Proposition 5.11, printed pp. 66–68 / local PDF pp. 83–85.
The latter passages give the free-group/free-algebra interface used below; the elementary centered-second-moment calculation is included rather than invoking an unchecked law of large numbers.

A bounded primary-source search also opened de Pagter–Sukochev, *Commutator estimates and R-flows in non-commutative operator spaces*, Proceedings of the Edinburgh Mathematical Society **50** (2007), 293–324, [publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B6C326BAEE0653A9A7EB59B661233724/S0013091505000957a.pdf/commutator-estimates-and-rr-flows-in-non-commutative-operator-spaces.pdf), especially the introduction, printed pp. 293–295.
Its announced commutator applications use selfadjoint implementing operators and symmetric operator spaces.
Those hypotheses do not supply an arbitrary closable nonsymmetric dual's paired correction on \(E\).
Aleksandrov–Peller's [operator-Lipschitz survey](https://arxiv.org/pdf/1611.01593) was opened as an additional lead, without a consumed theorem or full audit.
These are discovery and applicability notes, not new accepted source dependencies or bibliographic registrations.

<a id="yin_c_f0102"></a>
## 2. A Precise Sufficient Local Estimate

Fix, for each \(i\), an expansion from Yin_C_F0039,
\[
\overline{k_i(z,w)}=\sum_{n\ge1}a_{in}(z)b_{in}(w),
\qquad a_{in},b_{in}\in W^*(X_i),\qquad
\sum_n\|a_{in}\|\|b_{in}\|<\infty.
\tag{1}
\]
Here \(k_i(z,w)=(\bar z-\bar w)/(z-w)\) off the null diagonal.
Consider the following additional, genuinely local condition.
There are projections \(e_k\in E\), with \(\tau(1-e_k)\to0\), such that \(e_kb_{in}\in E\) for every \(i,n,k\), and
\[
L_{i,k}:=\sum_n\|a_{in}\|
 \bigl\|a\longmapsto D_i(ae_kb_{in})\bigr\|_{\mathcal M_\infty\to H}
<\infty
\qquad(i,k).
\tag{2}
\]
Each individual orbit norm in (2) is finite by closability, but the summability is an extra condition.

**Complete sufficient-condition deduction.**
Under (2), all conclusions of Yin_C_F0029 hold for the original duals on \(E\), with no separate adjoint-domain premise.

Indeed, let \(F\) be the complex span of \(\bigcup_k\mathcal M e_k\).
It is a dense left module contained in \(E\), and Yin_C_F0086's graph-core restriction argument gives
\[
\overline{D_i|_F}=\overline{D_i},
\qquad (D_i|_F)^*=D_i^*.
\tag{3}
\]
For \(v\in F\), define
\[
Q_i v=\sum_n D_i(vb_{in})a_{in}.
\tag{4}
\]
Condition (2), first on one \(\mathcal M e_k\) and then on finite sums, proves convergence in \(H\).
Since (4) is the actual series on its input vector, its value does not depend on the finite-sum presentation of \(v\).
For fixed \(v\in F\), the map \(a\mapsto Q_i(av)\) is bounded from operator norm to \(H\).
Its values converge weakly on uniformly bounded strongly convergent nets of \(a\): use the original dual's weak orbit continuity term by term, then the uniform summable tail supplied by (2).

The Yin_C_F0039 right-multiplier calculation applies to the bounded Hilbert-Schmidt commutators from Yin_C_F0037.
Passing through (4) gives, on \(F\),
\[
[Q_i,X_j]=[D_i,X_j^*]^*,\qquad
[Q_i,X_j^*]=[D_i,X_j]^*.
\tag{5}
\]
In particular, multiplication of the two spectral phases gives one off the null diagonal; it is not a scalar inverse of a Hilbert-Schmidt operator.

Now repeat the Yin_C_F0086 cross-form argument with
\[
b_i(p,q)=\langle p,D_iq\rangle+\langle Q_ip,q\rangle,\qquad p,q\in F.
\]
The only properties of \(Q_i\) used there are that it is \(H\)-valued, has bounded weakly continuous orbits, and satisfies (5).
Its closability is not needed for this adaptation.
These properties give balance for all \(\mathcal M\), normal corner densities, and the measure-glued \(\xi_i\in L^0(\mathcal M)\).
For
\[
V_i=\{p\in F\cap\mathcal M:p\xi_i^*\in H\},
\]
the simultaneous linear graph of \(D_i,Q_i\) admits the two left-cutoff approximations of Yin_C_F0086.
Its norm closure is a weakly closed linear subspace of \(H^3\), whether or not it is the graph of an operator.
Consequently these approximations still give the required \(D_i\)-graph core and the simultaneous limits in the common-positive-factor pairing.
One obtains
\[
\langle p,D_iq\rangle
=\langle p\xi_i^*-Q_ip,q\rangle
\quad(p\in V_i,\ q\in F).
\]
Equation (3) extends the test to every \(q\in E\).
Thus \(V_i\subseteq\operatorname{Dom}D_i^*\) is a dense left module, and Yin_C_F0029 applies to the original domains.
This proves the conditional deduction.
It does **not** establish (2) from (1).

There is a useful directly checkable case: for each \(i\), suppose \(E\) contains projections \(e_{i,k}\) tending to one in trace and commuting with \(W^*(X_i)\).
If \(c_{i,k}=\|a\mapsto D_i(ae_{i,k})\|_{\infty\to2}\), then
\[
D_i(ae_{i,k}b_{in})=D_i(ab_{in}e_{i,k}),\qquad
L_{i,k}\le c_{i,k}\sum_n\|a_{in}\|\|b_{in}\|<\infty.
\tag{2a}
\]
The above proof runs separately on \(F_i=\operatorname{span}\bigcup_k\mathcal M e_{i,k}\), because Yin_C_F0029 permits different adjoint test modules \(V_i\).
Thus a single common projection family is not essential.
This condition applies to the canonical analytic-arc expansion without a graph-growth estimate beyond closed graph, but the existence of such commuting projection windows is an additional hypothesis, not a consequence of mere density.

## 3. Why Projective Summability Alone Does Not Establish (2) or (4)

The following short construction disproves the general auxiliary assertion that a projective expansion automatically acts term by term on unbounded duals once a common dense left module has been found.
It is not a counterexample to Q1.

Take \(\mathcal M=L(\mathbb F_2)\) with free Haar generators \(U,V\).
Let \(B_1,B_2\) be the bounded terminal-deletion duals, with the project convention \([B_i,X_j]=\delta_{ij}P\) for \(X=(U,V)\), as checked in MSY23 Proposition 6.3 and the source audit cited above.
In \(W^*(V)\cong L^\infty(\mathbb T)\), choose a positive finite-a.e. function \(\eta\) that is not in L1, for example \(\eta(e^{it})=|t|^{-2}\), \(-\pi<t\le\pi\), with an arbitrary finite value at \(t=0\).

This is a closed densely defined affiliated operator, despite its infinite integral.
Put
\[
E=\operatorname{Dom}\rho(\eta),\qquad
D_1=B_1+\rho(\eta)\text{ on }E,\qquad
D_2=B_2|_E.
\tag{6}
\]
The domain \(E\) is a fixed dense left \(\mathcal M\)-module, chosen **before** any tensor expansion.
Both duals are closable; \(D_1\) is closed, and its extra right multiplier commutes with every left coordinate.
Hence the actual normalized dual identities hold on \(E\).
Also \(\operatorname{Dom}D_1^*=E\); the example has no adjoint-module failure.

Let
\[
F=\{v\in H:vU^r\in E\text{ for every }r\in\mathbb Z\}.
\tag{7}
\]
By Yin_C_F0086 this is a dense left module and a graph core for the original duals.
Every elementary paired term with coefficients \(U^r,U^{-r}\), and the usual unitary phase term, is defined on \(F\).

Set \(c_m=2^{-m}\).
Let \(z_K=\min(\eta,K)\), \(\mu_K=\tau(z_K)\).
The algebras \(U^{-n}W^*(V)U^n\), \(n\ge1\), are free: a reduced product of nonzero powers of their generating words expands into a nontrivial word in \(U,V\), and NS06 Proposition 5.11 applies, followed by bounded approximation.
In particular their centered L2 vectors are orthogonal, so
\[
\left\|\frac1N\sum_{n=1}^N U^{-n}z_KU^n-\mu_K1\right\|_2
=\frac{\|z_K-\mu_K1\|_2}{\sqrt N}.
\tag{8}
\]
Because \(\mu_K\uparrow\infty\), choose \(K_m\) with \(c_m\mu_{K_m}\ge2m\), and then choose a finite \(N_m\) so that the right side of (8), multiplied by \(c_m\), is at most \(1/m\).

Define the positive affiliated finite sum
\[
A_m=\frac{c_m}{N_m}\sum_{n=1}^{N_m}U^{-n}\eta U^n.
\]
For every nonzero projection \(e\in F\), all \(eU^{-n}\eta U^n\) are in \(H\).
Positivity, (8), and Cauchy–Schwarz therefore give
\[
\begin{aligned}
\tau(eA_me)
&\ge c_m\mu_{K_m}\tau(e)-\frac{\|e\|_2}{m}\\
&\ge2m\tau(e)-\frac{\sqrt{\tau(e)}}m,
\end{aligned}
\]
and hence
\[
\|eA_m\|_2\ge2m\sqrt{\tau(e)}-\frac1m\longrightarrow\infty.
\tag{9}
\]
All traces here involve an L2 product with bounded factors, so they are finite.
No trace of the uncompressed \(\eta\) is used as a finite quantity.

For each \(m\), form the finite tensor block
\[
T_m=\frac{c_m}{N_m}\sum_{n=1}^{N_m}U^n\otimes U^{-n}.
\]
Insert its elementary terms followed by all their negatives, in that order.
The resulting ordered series has zero sum in \(W^*(U)\widehat\otimes_\pi W^*(U)\), with total sum of elementary norm products at most \(2\sum_m c_m<\infty\).
Append these cancelling blocks after the ordinary phase term \(-U\otimes U\).
This is a valid projective expansion of the **same** conjugate unitary phase \(-zw\), uniformly on \(\mathbb T^2\).

At the end of the positive \(m\)-th block, its paired action on a projection \(e\in F\) is
\[
\frac{c_m}{N_m}\sum_{n=1}^{N_m}D_1(eU^{-n})U^n
=eA_m+
\frac{c_m}{N_m}\sum_{n=1}^{N_m}B_1(eU^{-n})U^n.
\]
The final term has norm at most \(c_m\|B_1\|\|e\|_2\), while (9) diverges.
At the end of the following negative block, the added paired action is exactly zero.
Thus the paired series fails to be Cauchy on every nonzero projection in \(F\).
It cannot converge on a dense left submodule of \(F\), because Yin_C_F0032 supplies nonzero projections in every such submodule.

This proves failure of the auxiliary continuity assertion under actual closable normalized dual relations on a fixed dense left domain.
The original adjoint domains are well behaved, and the finite unitary phase representation works.
The defect is using an arbitrary infinite representation on an unbounded multiplier, not the mathematical automatic-adjoint conclusion.

## 4. Canonical Analytic Expansions: Remaining Obligation

The cancelling-block example does not decide what happens for Yin_C_F0039's specific local Taylor expansion on an analytic arc.
It also does not refute the existence of some better paired operator, or a reconstruction after removing a right-affiliated summand.
No broader claim is drawn from the artificial representation.

For \(X=r(S)\), Yin_C_F0039's rectangle expansion has right coefficients of the form
\[
1_{I_\ell}(S)(S-c_\ell)^n,
\]
and coefficient estimates from a complex Taylor radius \(R>0\).
On a small domain the missing estimate is therefore explicit: find sufficiently large projections \(e_k\) for which these right products belong to \(E\), and obtain, on each relevant spectral cell,
\[
\bigl\|a\mapsto D_i\bigl(ae_k1_{I_\ell}(S)(S-c_\ell)^n\bigr)\bigr\|_{\infty\to2}
\le C_{i,k,\ell}r_{i,k,\ell}^{\,n}
\quad\text{with }r_{i,k,\ell}<R.
\tag{10}
\]
Then Cauchy's coefficient estimate, followed by summation in the other Taylor index, proves (2).
Countable intersections alone provide the individual domains; they do not provide the growth bound (10).
Mere closability gives finite orbit norms for each \(n\), with no rate.

For the quadratic graph \(r(t)=t+\mathrm i\varepsilon t^2\), the canonical conjugate phase is
\[
\frac{1+\mathrm i\varepsilon(s+t)}{1-\mathrm i\varepsilon(s+t)}
=-1+\frac{2}{1-\mathrm i\varepsilon(s+t)}.
\tag{11}
\]
This suggests using the resolvent of the left/right \(S\)-sum on the paired operator instead of an arbitrary tensor representation.
Its bounded action on \(H\) or on bounded operators is insufficient to define it on the present \(D_i:E\to H\); an actual local domain or a prior removal of the right-affiliated component still has to be proved.
Finite rational approximants do not resolve that domain question merely because their scalar kernels converge uniformly.

Current outcome: the conditional criterion (2) is proved by explicit adaptation of the reviewed local argument, and the universal representation-continuity shortcut is refuted by (6)–(9).
The automatic derivation of (2), or an intrinsic alternative for the canonical analytic kernel, remains open in this record.
At the original candidate stage, these deductions awaited independent review.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:15 |
| status | proved |
| reason | Adopt the exact actual original finding at its disclosed unknown initial-context relationship. Preserve mathematical status, statement, selected proof, dependencies and historical decisions; no new mathematical proof version or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0102) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0112_v1.md#6-analytic-continuation-boundary-and-verification-limits) | Whole conditional local-orbit criterion, coordinate-commuting window case, complete cancelling-block obstruction and the canonical analytic continuation limitation. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0102) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0112_v1.md#current-isolated-finding) | Whole conditional local-orbit criterion, coordinate-commuting window case, complete cancelling-block obstruction and the canonical analytic continuation limitation. |

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
| argument | [Exact material](#yin_c_f0102) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0112_v1.md#6-analytic-continuation-boundary-and-verification-limits) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0112_v1.md#6-analytic-continuation-boundary-and-verification-limits).

Material covered by that review: [Exact material](Yin_C_F0102_v1.md).
