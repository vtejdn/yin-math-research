---
author: Yin
---
# Independent review of kernel-preserving Schur-complement normalizations

Review time: 2026-11-11T01:30 (UTC).
Human record author: Yin.
The review covers the whole fixed [Yin_L_A0006_v1](../../ledger/Yin_L_A0006_v1.md), including its introduction dated 2026-11-11 (Asia/Hong_Kong), primary coupled-pencil example, all secondary sections and stated limitations.
The notation in this review refers to the corresponding local notation of that artifact; its closed affiliated algebra and unnormalized trace conventions are retained.

## Arrangement and inputs

A separately organized reviewing agent, outside substantive development of this artifact, performed an initial independent whole-argument review.
No development drafts, proof-generation dialogue, author explanations, other agents' mathematical messages or previous opinions about this artifact were supplied or consulted before the initial findings.
The fixed artifact, its necessary fixed mathematical dependencies, applicable rules and the human-request scope were supplied or read directly.
The fixed dependencies include their own source-inspection and assessment information; those prerequisite records were not treated as previous opinions about the new artifact.
No earlier R material was opened.
The reviewer did not edit the reviewed mathematics or supply a substantive repair.

The inspected project inputs were the [weighted energy statement](../../claims/Yin_C_A0003_v1.md#statement), its [bounded proof](../../claims/Yin_C_A0003_v1.md#bounded-energy-calculation) and [coupled graph example](../../claims/Yin_C_A0003_v1.md#a-coupled-example-without-a-spectral-gap-premise); the [cyclic argument](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), [mixed resolvent sum](../../ledger/Yin_L_A0002_v1.md#mixed-resolvent-sums-with-a-scalar-real-part) and [coefficient boundary test](../../ledger/Yin_L_A0002_v1.md#the-first-additive-scalar-tests); and the [complementary-block reduction](../../ledger/Yin_L_A0005_v1.md#complementary-block-reduction-and-the-scalar-obstruction) and [half-plane necessity](../../ledger/Yin_L_A0005_v1.md#a-positive-realization-restricts-the-scalar-value).
Their arguments were checked at these actual invoked scopes, without reviewing unrelated portions of those materials.

The accepted source interfaces were [MSY23-U004, finite-affiliated foundations and Lemmas 5.1--5.5](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness), its [local domain-aware rank proof](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof), and [MSY23-U003, actual rational closure and complete division closure](../literature/MSY23/Yin_U003.md#complete-division-closure-and-proposition-411).
The [Lin93 affiliated-rank interface](../literature/Lin93/Yin_U001.md#affiliated-closure-and-rank-conventions) and [exact group-class theorems](../literature/Lin93/Yin_U001.md#group-class-and-exact-theorems) were read for the stated rank attribution and known-coverage comparison.
The general existence and associativity of the finite affiliated algebra, its polar decomposition and support theory, and Lin93's established group theorem are accepted at these retained source scopes.
Their original external foundational proofs and Lin93's complete proof chain were not re-audited in this review.
The local rank, closure and project-interface arguments actually needed here were checked directly.

## Whole-artifact finding

The whole argument is mathematically valid under the declared finite-affiliated foundations.
No actionable mathematical defect was found in the exact hypotheses, identities, domain conventions, rank conclusions, parameter boundaries or source-scope comparisons.
The finding covers all of the following obligations, rather than only the primary example.

### Primary factors, denominator and ordered normalization

The hypotheses \(g\ne h\) and torsion-freeness make both \(g^{-1}h\) and \(gh^{-1}\) nonidentity elements of infinite order.
The bilateral-shift argument therefore proves that \(b=g(1+g^{-1}h)\) is injective, and finite-trace polar decomposition supplies its actual affiliated inverse independently of the Schur value.
The expansion \(bb^*=2+gh^{-1}+hg^{-1}\) verifies the order and coefficient of every term in \(P=2a-bb^*\).
The positive real part \(2-q-q^{-1}=(1-q)^*(1-q)\) is injective, so the bounded quadratic-form proof supplies the actual inverse of \(P\) without a commutation or spectral-gap premise.
The displayed incidence matrix satisfies \(D^*D=\operatorname{Re}L\), and its two zero equations reduce to the same infinite-order fixed-vector obstruction.
This independently proves the denominator \(L\) admissible.

The triangular factorization (9) and inverse (10) were multiplied in their displayed order.
They give \(r=P^{-1}b\) and \(rb^{-1}=P^{-1}=\frac12 e_1^*L^{-1}e_1\), with no interchange of \(b\) and \(P\).
Actual inverse entries and rational-closure algebra operations justify membership in \(R\), while \(r^{-1}=b^{-1}P\) and \(\widehat r^{-1}=P\) justify the stronger assertion \(r,\widehat r\in R^\times\).
The right multiplier is constructed before any use of \(r^{-1}\) or full rank of the original border.
The matched data of \(Q_+\) satisfy the weighted energy theorem with its original denominator \(L\).
The scalar denominator \(P\) gives the stated smaller realization, and adjoining \(q,q^{-1}\) as actual group labels preserves their relation to \(g,h\).
The argument never evaluates an abstract free-field expression at an unjustified inverse.

The positive part of this construction allows \(g=e\), \(h=e\) or \(k=e\) whenever the stated distinctness \(g\ne h\) is preserved.
It requires no additional assumption on \(k\), on relations among the labels, or on the group's global Atiyah property.

### Closed affiliated rank and Hilbert-space kernels

The rank inequalities in the cited MSY23 interface apply to closed affiliated products, by closure-of-range inclusion and inclusion of the kernel of the right factor.
Applying them to \(AZB\) and to \(Z=A^{-1}(AZB)B^{-1}\) gives rank equality for actual square units, including unbounded units and unbounded inverses.
The independent principal-right-ideal calculation \((tc)U=tU\) supplies the same right-unit conclusion through the left support projection.
Polar decomposition identifies the trace of that support with analytic rank and gives the rank-plus-kernel-dimension identity.
Thus the kernel preservation claimed in the artifact is an equality of von Neumann dimensions of closed kernels.
No unsupported pointwise action of \(B^{-1}\) on every Hilbert-space kernel vector is used.

Schur elimination with an already invertible denominator gives the exact shift \(N+\operatorname{rk}_G(uA^{-1}v)\), without assuming the scalar Schur value invertible.
This proves all rank comparisons (4)--(6), including the one-unit rank difference for the smaller border and the equality of kernel dimensions across its change of size.
The additional bounded kernel proof for \(Q\) is correct: its first row kills \(w_1\), its second row and injectivity of \(b\) kill \(w_2\), and its third row then kills \(f\).
The complementary scalar block is \(-b\), so the claim that this primary rank conclusion was already covered by the complementary-block and cyclic arguments is exact.

### Realization obstruction and known group coverage

For the specified original borders, \(uv=0\) contradicts \(u=\gamma v^*W\) with \(W>0\), \(v\ne0\) and \(\gamma\ne0\).
The artifact correctly separates this realization-specific failure from its stronger free-group assertion about the value.
On \(F(g,h,k)\), the displayed character exists, its diagonal unitary implements a trace-preserving automorphism, and the transformations of \(a,b,P,L,r,\widehat r\) in (13) have the correct phases.
The automorphism extends to closed affiliated operations and preserves positivity.
If \(\operatorname{Re}(zr)\ge0\), the phase \(\pi\) makes its negative positive, forcing it to vanish; the phase \(\pi/2\) then forces the other Cartesian part to vanish.
This contradicts the independently proved nonvanishing of \(P^{-1}b\).

Expanding \(H=(WA+A^*W)/2\) verifies the half-plane identity in the correct noncommutative order.
Its right side is the square of the affiliated column \(H^{1/2}A^{-1}v\), hence positive.
Consequently the obstruction excludes every exact-value positive matched realization of the free-group value, regardless of denominator size and even without the stronger energy-kernel condition.
This conclusion does not extend silently to torsion-free quotients without the stated characters.

The source comparison with Lin93 is applicable: the free group may itself be the normal free subgroup, with trivial elementary amenable quotient, and it also belongs to class \(\mathcal C\).
The division-ring conclusion gives integer matrix ranks by elimination over that division ring inside the actual affiliated algebra, so the stated full complex-coefficient Atiyah coverage is justified.
This established group result is a comparison, not a premise of the elementary normalization.
The artifact accurately makes no claim of a new positive group class, general multiplier algorithm, historical novelty or resolution of the Task.

### Reciprocal-ratio calibration

In the reset secondary notation, the nonidentity hypotheses give actual units \(a,b\), while \(g\ne h\) separately gives the actual unit \(c=b-a=g-h\).
The two displayed triangular inverse blocks verify \(L_0^{-1}\), and its constant compression is exactly \(a^{-1}b-b^{-1}a\).
Its unmatched-border conclusion follows from \(u_0v_0=0\) and is correctly restricted to this specified realization.

Expanding the ordered product gives
\[
(b-a)(a^{-1}+b^{-1})=ba^{-1}-ab^{-1}=brb^{-1}.
\]
This verifies the claimed multipliers \(A=c^{-1}b\), \(B=b^{-1}\), their independent unit premises and \(ArB=t\).
The diagonal matched denominator has positive injective real part, so the invoked energy conclusion supplies the unit \(t\), and then the unit \(r\), at the stated actual-affiliated scope.
The rank shifts for the borders of sizes five and three, and their equivalence by affiliated units after adjoining \(I_2\), follow from the same justified eliminations and multipliers.
There is no missing denominator or target-inverse premise in this stabilization.

The cyclic identity \(a^{-1}+(a^{-1})^*=1\), and its \(b\) analogue, give \(t+t^*=2I\), agreeing with the earlier mixed resolvent-sum endpoint and its bounded inverse estimate.
For \(h=g^{-1}\) in the infinite cyclic group, direct cancellation gives \(r=g-g^{-1}\); its circle zeros make the inverse unbounded.
This correctly distinguishes preserved kernel dimension from spectral gap or bounded conditioning.

### Positive real parameters and complex boundary

The expansion of (S1) cancels the two middle scalar terms without commuting \(a,b\), and remains an algebraic identity for complex \(q\).
For \(0<q<1\), multiplication of the displayed bracket by \(-h\) gives exactly \(c_q=(1-q)+qg-h\); its positive real part has an injective summand with coefficient \((1-q)/2>0\).
For \(q>1\), multiplication of the second bracket by \(qg\) gives the same \(c_q\), and its injective summand has positive coefficient \((1-q^{-1})/2\).
The other summand may vanish when \(g=h\), without affecting either proof.
At \(q=1\), the separate cyclic factorization applies exactly when \(g\ne h\).
Thus every use of \(c_q^{-1}\) in (S2) has an independent actual-unit proof in its claimed range.

The matched border with \(v_+=(1,\sqrt q)^{\mathsf T}\) represents \(t_q=a^{-1}+qb^{-1}\), and the denominator's positive real part satisfies the energy hypotheses.
The scalar-real-part identity \(t_q+t_q^*=(1+q)I\) gives the stated inverse norm bound \(2/(1+q)\).
The modified \(u_0\) realizes \(r_q\), remains unmatched, and has the asserted scalar rank and five-by-five bordered rank in every nonexceptional case.
When \(g=h\), cancellation gives \(r_q=(1-q^2)I\), so \(q=1\) is exactly the excluded zero case, with bordered rank four and no admissible \(c_q^{-1}\).
No other zero or fractional-rank case is left under the positive-real hypotheses.

At \(q=i\), the three distinct group coefficients of \(c_i\) have moduli \(\sqrt2,1,1\), outside the earlier coefficient-dominance condition.
The positive-real proof of \(c_q\) and the positive-weight matched representation of \(t_q\) do not apply to that displayed branch.
The artifact leaves the multiplier unproved there and does not infer its inverse from notation or from a formal identity.
Its statement that a known group theorem could supply a different input, while no general impossibility of another certificate is claimed, is appropriately limited.

## Source completeness and review limits

The sources and fixed local arguments needed for the displayed proofs are identified, with the correct hypotheses and actual-affiliated meanings.
The known group coverage and rank attribution are supported at the exact retained Lin93 source interfaces.
This is not a new literature search, an independent re-audit of all underlying external proofs, a historical-priority assessment, a proof-assistant verification or a completion review of [Yin_T_A0001](../../tasks/Yin_T_A0001_v1.md#contract).
No finite-dimensional numerical substitute or structural checker was used to establish the mathematical conclusions.
The review establishes the stated concrete normalizations and their limitations; it supplies no new general constraint excluding the unresolved fractional-rank interval beyond those examples.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Whole fixed artifact](../../ledger/Yin_L_A0006_v1.md#kernel-preserving-normalizations-of-unmatched-rational-schur-complements) | Complete dated introduction, all statements, arguments, comparisons and limitations in the physical v1 inspected here. |
| [Whole-artifact finding](#whole-artifact-finding) | [Coupled-pencil normalization](../../ledger/Yin_L_A0006_v1.md#coupled-pencil-normalization) | Exact hypotheses and all assertions (1)--(7), actual rational units and realization sizes. |
| [Whole-artifact finding](#whole-artifact-finding) | [Primary proof](../../ledger/Yin_L_A0006_v1.md#proof-of-the-coupled-pencil-normalization) | All subsections: independent admissibility, ordered inverse, affiliated rank and closed kernels, original border and exact-value obstruction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Coverage and limitation](../../ledger/Yin_L_A0006_v1.md#coverage-and-limitation-of-the-primary-test) | Known free-group coverage, universal torsion-free expression scope and absence of a new general rank or group-class conclusion. |
| [Whole-artifact finding](#whole-artifact-finding) | [Secondary calibration](../../ledger/Yin_L_A0006_v1.md#secondary-calibration-a-reciprocal-ratio-schur-complement) | Entire reciprocal-ratio construction, ordered transfer, stabilization, known endpoint and unbounded-inverse example. |
| [Whole-artifact finding](#whole-artifact-finding) | [Positive real parameter family](../../ledger/Yin_L_A0006_v1.md#a-positive-real-parameter-family) | Both independent factor tests, matched endpoint, inverse estimate and every stated degenerate case. |
| [Whole-artifact finding](#whole-artifact-finding) | [Complex-parameter boundary](../../ledger/Yin_L_A0006_v1.md#the-complex-parameter-bottleneck) | Formal identity versus actual-unit admissibility, coefficient comparison and exact unresolved scope. |
