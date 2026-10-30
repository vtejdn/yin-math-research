---
author: Yin
---

# Affiliated rationality via original regular commutators

## Current decision

[Selected recorded decision](#decision-candidate-0009)

## Yin_T_F0001: Affiliated Rationality via Original Regular Commutators

<a id="contract"></a>
<a id="yin_t_f0001"></a>

Human record author: Yin.
Contract revision: 2026-09-29T13:43, preserved below.
Resolution added: 2026-09-30.
Canonical lifecycle and review state: [Task record](Yin_T_F0001_v7.md#decision-candidate-0011).

Subsequent related material, 2026-10-01: [C_F0066 and its relationship map](../claims/Yin_C_F0066_v1.md#dependencies-and-relationships) address the existential-only branch beyond the 2026-09-30 two-model resolution.
The dated contract and completion evidence below retain their original scope.

<a id="raw-commutator-authorization"></a>
## Negative Resolution of the Supplied-Domain Assertion, 2026-09-30

The exact universal assertion (T) below is false, including under the compact polynomial starred-commutator comparison baseline.
The [two explicit counterexamples](../claims/Yin_C_F0065_v1.md#original-regular-commutator-domain-counterexamples) use a single selfadjoint semicircular generator and the genuinely unbounded rational element \(u=X^{-1}\).
No substitution of the supplied dual is made.

- Model 1 has supplied domain exactly the polynomial algebra, an actual adjoint defined everywhere, a normalized closable dual, and a rank-one starred commutator on its whole domain.
  One fraction pair has dense polynomial natural domain and a rank-one extension; another has natural domain exactly zero.
  Thus closability alone does not restore density or fraction independence.
- Model 2 has a closed supplied dual whose domain contains all bounded vectors and is invariant under the generator.
  Both compared natural domains are dense and all fraction coefficients are polynomials.
  One original defect is everywhere bounded of rank one; the other has no bounded extension agreeing on its full natural domain.
  Its polynomial starred commutator still has a rank-one extension.
  The polynomial dual identity is not asserted on the extra supplied-domain vectors.

These models refute rationality implying the every-fraction condition and the equivalence between some and every fractions.
The no-starred-condition package and the compact polynomial-commutator baseline are both refuted.
Strengthening only compactness to a nonzero standard operator ideal containing finite-rank operators cannot exclude the rank-one examples.
Neither example refutes every possible replacement condition.

The combined hypothesis that the supplied operator equals the closure of its polynomial restriction is **not decided** by these counterexamples: Model 1 is not closed, and Model 2 has a proper extra graph extension.
A full-domain dual relation excludes Model 2 but not Model 1; closedness excludes Model 1 but not Model 2.
Their conjunction, suitable actual-adjoint compatibility, and other domain conditions remain separate possible strengthened contracts.
The existential-only equivalence between rationality and some finite-rank fraction is also not refuted by these witnesses, since their exhibited element satisfies both sides.

The original contract and completion criteria below are retained without weakening.
Its negative-result criterion permits completion by this explicit failure of an implication and fraction independence; it does not require refuting every strengthened domain package.
The [whole-proof and contract review](../audits/reviews/Yin_R_F0079_v1.md#retained-r107) owns the independent findings.
The canonical Task record owns acceptance and lifecycle, separately from this mathematical resolution.
Earlier C_F0063/C_F0064 and the [bounded-dual theorem](../claims/Yin_C_F0013_v1.md#1-statement-and-exact-scope) remain unchanged at their recorded scopes.

## Authorization and Relation to the Completed Contract

The user's instruction of 2026-09-29 explicitly revises and reactivates T_F0001.
The new exploration must prove the affiliated rationality equivalence using the original operator expression \(sD_i b-aD_i t\), or give a rigorous counterexample.
The domain of each supplied dual must contain the starred polynomials, and the vacuum must belong to its actual Hilbert-adjoint domain.
Compact extendability of \([D_i,X_j^*]\) may be replaced by a comparable condition; removing that condition entirely is preferred.

This is an authorized stronger successor contract, not a withdrawal of the earlier result.
The unchanged [material v3](Yin_T_F0001_v3.md#yin_t_f0001), [Task decision 6](Yin_T_F0001_v3.md#decision-candidate-0006), [intrinsic resolution](../ledger/Yin_L_F0016_v1.md#t_f0001-intrinsic-criterion-resolution) and [independent completion audit](../audits/reviews/Yin_R_F0031_v1.md) preserve completion of the intrinsic tensor-test criterion and original bounded weak-form companion.
Those achievements do not settle the present original-operator target.

## Retained Setting and Dual Data

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, \(H=L^2(M,\tau)\), \(\Omega=1\), and \(P_\Omega q=\tau(q)1\).
The inner product is linear in the second variable.
Let \(X=(X_1,\ldots,X_d)\), \(d\geq1\), be bounded normal generators of \(M\), with no mutual commutativity or free independence assumed.
Put

\[
\mathcal P=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle,
\qquad A=\mathbb C\langle X_1,\ldots,X_d\rangle,\qquad U=U(M).
\]

The target is the scalar affiliated division closure \(\operatorname{Div}_{U}A\); generator adjoints are not automatically adjoined to \(A\).
Do not presume a free-field embedding under weakened hypotheses before proving or importing an applicable result.

The fixed starting data are complex-linear, densely defined operators
\[
D_i:\operatorname{Dom}(D_i)\subseteq H\longrightarrow H
\]
such that
\[
\mathcal P\subseteq\operatorname{Dom}(D_i),\qquad
\Omega\in\operatorname{Dom}(D_i^*),\qquad
[D_i,X_j]p=\delta_{ij}P_\Omega p\quad(p\in\mathcal P).
\tag{D}
\]
The last identity uses left multiplication by \(X_j\).
No normalization \(D_i\Omega=0\), boundedness on \(H\), all-\(M\) domain, left-\(M\)-module domain, or polynomial graph-core property is part of (D).

The supplied operator and its actual domain are part of the data.
In particular, \(\operatorname{Dom}(D_i)\) need not equal \(\mathcal P\), and \(D_i\) is not silently replaced by \(\overline{D_i|_{\mathcal P}}\), a normalized contraction, or a separately chosen extension.
If closability, closedness, a core property, or compatibility with such a replacement is needed, prove it under the stated hypotheses or identify it explicitly as an additional condition and assess its effect on the target.
The adjoint-vacuum condition alone is not declared a proof of closability of an arbitrary supplied extension.

## Adjustable Adjoint-Generator Hypothesis

Investigate the hypothesis packages explicitly:

1. Preferred strongest assertion: (D) alone, with no extendability or compactness assumption on \([D_i,X_j^*]|_{\mathcal P}\).
2. If necessary, state and test a natural weaker or comparable replacement for the earlier compact-extension condition.
   Specify the ideal, boundedness, graph, or adjoint compatibility condition actually used, and its logical relationship to compact extendability.
   Merely calling a condition analogous is not enough.
3. Retain the earlier condition that every \([D_i,X_j^*]|_{\mathcal P}\) has a compact bounded extension as a comparison baseline.
   A result under this condition remains useful, but must not be described as removing it.

Every theorem or counterexample must identify its exact package.
Bounded duals and the established all-\(M\) or left-module criteria are comparison cases, not substitutes for the requested domain reduction.
A special spectral geometry or freeness assumption likewise gives only a stated special case.

## Original Operator Definition and Desired Equivalence

For every \(u\in U\) and every bounded left/right fraction pair
\[
u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,\qquad s,t\text{ regular},
\]
where regular means invertible in \(U\), use the literal natural composition domain
\[
\mathcal E_i(s,a,b,t)
=\{q\in H:bq\in\operatorname{Dom}(D_i),\
tq\in\operatorname{Dom}(D_i)\}.
\]
Define the original regular commutator by
\[
\Delta_i^D(s,a,b,t)q
=sD_i(bq)-aD_i(tq),\qquad q\in\mathcal E_i(s,a,b,t).
\tag{RC}
\]
This is the actual supplied \(D_i\).
The formal notation \(s[D_i,u]t\) does not justify additional compositions or domain inclusions.

For this contract, the finite-rank condition at a fraction pair means that, for every \(i\), \(\mathcal E_i(s,a,b,t)\) is Hilbert dense and there is a bounded finite-rank operator \(K_i\in B(H)\) agreeing with (RC) on its entire natural domain.
Density makes this extension unique.
Finite rank is ordinary complex Hilbert-space rank.
A finite-dimensional range on a nondense test set, or an arbitrarily selected extension from such a set, does not meet the condition.

The desired theorem, under the precisely stated final dual hypotheses, is
\[
\begin{aligned}
u\in\operatorname{Div}_{U}A
&\quad\Longleftrightarrow\quad
\text{the original finite-rank condition holds for some bounded fraction pair}\\
&\quad\Longleftrightarrow\quad
\text{the original finite-rank condition holds for every bounded fraction pair},
\qquad u\in U.
\end{aligned}
\tag{T}
\]

This includes genuinely unbounded \(u\) and arbitrary bounded fraction coefficients, with no rationality requirement on those coefficients.
Prove the denominator identities and all domain/extension steps needed for fraction independence.
Record numerical-rank invariance if established; it does not replace independence of the finite-rank condition.

The individual natural domains above are the specified domains.
If a proof uses a smaller common domain for several \(i\), justify its density and agreement with each operator on the full domain in (RC); do not assume that an intersection of dense domains is dense.
Universal density for all \(u\) and all pairs is a separate stronger assertion if claimed.
Failure of density for a nonrational \(u\) alone need not contradict (T); a counterexample must identify which assertion it refutes.

For bounded \(f\), the pair \((1,f,f,1)\) gives the actual commutator on \(\operatorname{Dom}(D_i)\cap f^{-1}\operatorname{Dom}(D_i)\).
Weak polynomial forms or full-domain invariance may be compared with this realization, but neither is substituted for it without proof.

## Permitted Methods and Inherited Evidence

The active route is [Yin_S_F0011](../strategies/Yin_S_F0011.md#s_f0011).
Original graph recovery, local modules, direct fraction-domain estimates and counterexample construction are available methods.
All-\(M\) inclusion may be proved as a sufficient route; it is not a mandatory intermediate theorem.

- [C_F0063_v1](../claims/Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion) supplies the accepted intrinsic criterion under its original compact-commutator hypotheses.
  Its auxiliary liberation closures and Hilbert-Schmidt deconvolution are useful only with an actual compatibility proof when used to identify (RC).
  Repeating the intrinsic theorem alone cannot complete this contract.
- [C_F0064_v1](../claims/Yin_C_F0064_v1.md#normal-small-core-bounded-rationality) retains the original bounded polynomial weak-form equivalence at its existing scope.
  It does not identify all raw unbounded fraction domains.
- [C_F0034](../claims/Yin_C_F0034_v1.md#yin_c_f0034) supplies fraction calculus under its explicit dense-module and adjoint-domain hypotheses; check those hypotheses before applying it to (RC).
- [C_F0013](../claims/Yin_C_F0013_v1.md#yin_c_f0013), [C_F0024](../claims/Yin_C_F0024_v1.md#yin_c_f0024) and [C_F0029](../claims/Yin_C_F0029_v1.md#yin_c_f0029) are established bounded-dual, all-\(M\) and local-module comparison cases.
- [C_F0026](../claims/Yin_C_F0026_v1.md#yin_c_f0026) shows that specified fraction inputs may leave the original domain even at the vacuum.
  That fact alone is not a counterexample to the dense-natural-domain criterion (T).
  Recheck the actual domain and extension, and whether the example concerns the supplied operator or its closure.

The earlier alternative-realization allowance does not settle this new target: a distributional tensor test, a deconvolved operator, or an alternative dual can be an auxiliary construction, but the final criterion must concern (RC), with agreement on its specified natural domain established.

## Completion and Review Criteria

1. State the exact final dual hypothesis package, all operator realizations and the arbitrary-\(u\), arbitrary-fraction quantifiers.
   Report explicitly whether compact starred commutators were retained, weakened, replaced, or removed.
2. For a positive result, prove both directions of (T), the natural-domain and bounded finite-rank extension assertions, and fraction independence.
   Explain compatibility with the [bounded-dual regular commutator](../claims/Yin_C_F0013_v1.md#1-statement-and-exact-scope) and the precise use, if any, of C_F0063/C_F0064.
3. For a negative result, give a fully specified tuple and supplied duals satisfying the exact hypothesis package, compute the relevant natural domains and defects, and exhibit failure of an implication or fraction independence.
   A failure of an auxiliary estimate, absence of the vacuum from one domain, or failure only for a substituted dual is not by itself such a refutation.
4. A counterexample without the starred-commutator condition decides only that version; it does not automatically refute the compact baseline or every possible replacement.
   Distinguish a general given-domain obstruction from the more restrictive case of the closed polynomial restriction.
   Preserve the explicit disposition of any remaining hypothesis branches.
5. Obtain a complete independent mathematical review of the final theorem or counterexample and its actual dependencies, followed by comparison with this contract before any completion transition.
   A special-class result, the previous intrinsic completion, or the bounded weak companion alone is insufficient.

## Manuscript, Other Tasks and Execution

This research reactivation does not authorize manuscript revision or a new main-theorem designation.
The normal-domain Task Q1/Q2/Q4, the q-Gaussian boundedness Task, the free-product reconstruction Task and the R-diagonal and analytic-transport Task retain their existing contracts and ownership.

Apply the [execution rules](../../framework/rules/execution.md) when a research run actually starts.
Contract revision and Task activation do not themselves create a run, reopen an earlier stopped execution, or transfer a previous run's usage override.

## Contract and Lifecycle History

- The original contract and its prior revisions remain in [material v1](Yin_T_F0001_v1.md), [material v2](Yin_T_F0001_v2.md) and [material v3](Yin_T_F0001_v3.md).
- 2026-09-29, earlier completion: Task v6 accepted C_F0063 (recorded assessment 2) and C_F0064 (recorded assessment 2) at their recorded scopes.
  That completed contract and its independent review remain valid historical evidence.
- 2026-09-29, current user-directed revision: retain Task identity T_F0001, replace the completed intrinsic target with the stronger original-operator target (RC)/(T), enlarge the allowed starting domain from exactly the polynomial algebra to any specified domain containing it, and allow weakening or removal of the starred-commutator assumption.
- Append the authorized completed-to-active lifecycle transition through the publication tool.
  The new contract receives only an organizational self-review; no new mathematical result or independent proof review is asserted.

- 2026-09-30, negative resolution submitted for independent acceptance: two literal supplied-domain counterexamples refute (T), even with rank-one polynomial starred commutators; the closed polynomial-core and existential-only strengthenings remain explicitly undecided.
  The exact v4 contract is retained above.


## Lifecycle and completion


### Decision candidate-0008

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-30T08:20 |
| status | completed |
| authority | User instruction of 2026-09-30 to use T_F0001 as a Goal and explore the authorized prove-or-counterexample contract; v4 Completion and Review Criteria item 3 and the independent whole-proof/completion audit dated 2026-09-30. |
| reason | Complete the unchanged original-operator contract by independently reviewed counterexamples to rationality implying the every-fraction condition and to fraction independence; retain explicit stronger-domain boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Exact material](#contract) | Exact original contract and success conditions retained in this material. |
| dependency | [Exact material](../claims/Yin_C_F0065_v1.md#decision-candidate-0002) | Complete explicit counterexamples satisfying the unchanged v7 negative-completion alternative: literal supplied domains, genuine rational unbounded witness, some/every failure under compact polynomial starred commutators, with closed polynomial-core and existential-only branches explicitly undecided. |
| dependency | [Exact material](../claims/Yin_C_F0065_v1.md#decision-candidate-0002) | Complete explicit counterexamples satisfying the unchanged v7 negative-completion alternative: literal supplied domains, genuine rational unbounded witness, some/every failure under compact polynomial starred commutators, with closed polynomial-core and existential-only branches explicitly undecided. |
| review | [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r107) | Whole unchanged T_F0001 contract at recorded assessment 7 and successor resolution, complete C_F0065 two-model proof with actual supplied domains and dependencies, exact negative alternative, compact baseline and remaining strengthened/existential-only scopes. |

Recorded mathematical summary: Completed by a rigorous counterexample to the original supplied-domain regular-commutator criterion: for a genuinely unbounded rational element, some/every fraction independence fails even with rank-one compact polynomial starred commutators.
C_F0065 gives a nonclosed polynomial-domain zero-domain model and a closed supplied-extension model with all-M domain, polynomial fractions and dense natural domains but no bounded extension at one pair.
The supplied closed-polynomial-core and existential-only criteria remain undecided; earlier intrinsic/weak-form and bounded-dual results remain valid.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0009

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-10-01T14:24 |
| status | completed |
| authority | User instruction of 2026-09-30 to use T_F0001 as a Goal and explore the authorized prove-or-counterexample contract; v4 Completion and Review Criteria item 3 and the independent whole-proof/completion audit dated 2026-09-30. |
| reason | Complete the unchanged original-operator contract by independently reviewed counterexamples to rationality implying the every-fraction condition and to fraction independence; retain explicit stronger-domain boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Exact material](#contract) | Exact original contract and success conditions retained in this material. |
| dependency | [Exact material](../claims/Yin_C_F0065_v1.md#decision-candidate-0002) | Complete explicit counterexamples satisfying the unchanged v7 negative-completion alternative: literal supplied domains, genuine rational unbounded witness, some/every failure under compact polynomial starred commutators, with closed polynomial-core and existential-only branches explicitly undecided. |
| dependency | [Exact material](../claims/Yin_C_F0065_v1.md#decision-candidate-0002) | Complete explicit counterexamples satisfying the unchanged v7 negative-completion alternative: literal supplied domains, genuine rational unbounded witness, some/every failure under compact polynomial starred commutators, with closed polynomial-core and existential-only branches explicitly undecided. |
| review | [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r107) | Whole unchanged T_F0001 contract at recorded assessment 7 and successor resolution, complete C_F0065 two-model proof with actual supplied domains and dependencies, exact negative alternative, compact baseline and remaining strengthened/existential-only scopes. |

Recorded mathematical summary: Completed on the recorded C_F0065 (recorded assessment 2) counterexamples to the original supplied-domain regular-commutator criterion and fraction independence, including a closed supplied-extension model with dense natural domains but no bounded extension at one pair.
Subsequently, C_F0066 (recorded assessment 2) refutes even rationality implying the existential dense-domain finite-rank condition: normalized nonclosed duals with exact polynomial domains and finite-rank starred commutators admit a genuinely unbounded rational element whose natural domain is zero at every bounded regular fraction pair.
This subsequent result does not change the earlier completion evidence.
The closed supplied-dual existential criterion, the closed polynomial-core branch, and the reverse existential implication are outside these counterexamples; earlier intrinsic, weak-form and bounded-dual results remain valid.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](Yin_T_F0001_v2.md#reorganization-authorization-2026-09-27); [Exact material](../ledger/Yin_L_F0016_v1.md); [Exact material](../audits/reviews/Yin_R_F0032_v1.md); [Exact material](../claims/Yin_C_F0065_v1.md).

Whole original T_F0001 contract at recorded assessment 5 and prepared Task material v3; complete C_F0063 (recorded assessment 2) main proof and Appendix A, C_F0062 (recorded assessment 2) graph bridge, C_F0064 (recorded assessment 2) bounded companion, actual dependencies and accepted source interfaces.
Every affiliated element and arbitrary bounded fraction pair, both directions and numerical-rank independence are covered under the explicitly permitted intrinsic tensor-test realization.
Literal arbitrary raw composition domains, original all-M dual domains and arbitrary unnormalized full-domain invariance remain unproved strengthenings.
No manuscript designation, formal verification or external review is claimed.

Completion contract: [Exact material](Yin_T_F0001_v3.md#contract).

Review: [Exact material](../audits/reviews/Yin_R_F0031_v1.md).

Material covered by that review: [Exact material](../audits/reviews/Yin_R_F0032_v1.md); [Exact material](../ledger/Yin_L_F0016_v1.md); [Exact material](Yin_T_F0001_v2.md#reorganization-authorization-2026-09-27); [Exact material](Yin_T_F0001_v3.md).

Whole unchanged T_F0001 contract at recorded assessment 7 and successor resolution, complete C_F0065 two-model proof with actual supplied domains and dependencies, exact negative alternative, compact baseline and remaining strengthened/existential-only scopes.

Completion contract: [Exact material](#contract).

Review: [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r107).

Material covered by that review: [Exact material](../audits/reviews/Yin_R_F0032_v1.md); [Exact material](../claims/Yin_C_F0065_v1.md); [Exact material](../ledger/Yin_L_F0016_v1.md); [Exact material](Yin_T_F0001_v2.md#reorganization-authorization-2026-09-27); [Exact material](Yin_T_F0001_v5.md).

## Execution boundary

`execution/Yin_E_F0001.md`.
