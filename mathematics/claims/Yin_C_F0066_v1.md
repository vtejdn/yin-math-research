---
author: Yin
---

# Failure of the existential original regular commutator criterion on polynomial domains

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Failure of the existential original regular commutator criterion

<a id="existential-original-regular-commutator-counterexample"></a>

Permanent Claim and proof material, 2026-10-01, Asia/Hong_Kong.
Human record owner: Yin.
Construction: root; initial separate conversational check: existential_domain_audit.
Provenance: project deduction in the standard semicircular model, with its checked source interface cited below.
The user authorized promotion of the working draft into ledger and recording its relationships with existing mathematical materials.
[Yin_C_F0066](#decision-candidate-0002) owns assessment and selected review.
No Task lifecycle or manuscript theorem selection is changed by this promotion.

The [complete independent agent review](../audits/reviews/Yin_R_F0038_v1.md#c_f0066-existential-domain-review) covers the fixed proof, source interface and comparison boundaries.
Its review arrangement and actual inspection limits are stated there.

The [earlier two-model result](Yin_C_F0065_v1.md) did not decide the existential-only question in [T_F0001](../tasks/Yin_T_F0001_v5.md).
The construction below gives a different two-variable witness: a rational affiliated element for which every bounded fraction pair has zero natural domain.
Thus the forward implication also fails when the supplied polynomial-domain duals are permitted.
Closed supplied duals remain a separate scope.

## Statement

There exist a finite von Neumann algebra with faithful normal probability trace, two bounded selfadjoint generators \(X_1,X_2\), and densely defined supplied operators \(D_1,D_2\) whose exact domains are the starred-polynomial vectors, such that \(D_i\Omega=0\), \(\Omega\in\operatorname{Dom}D_i^*\), and both \([D_i,X_j]\) and \([D_i,X_j^*]\) equal \(\delta_{ij}P_\Omega\) on their polynomial domains.
The operators are closable, with everywhere-defined bounded adjoints.
Nevertheless, the genuinely unbounded rational element \(u=X_1^{-1}X_2\) has natural domain \(\mathcal E_i(s,a,b,t)=\{0\}\) for every bounded regular left/right fraction pair and every \(i\).
Consequently rationality does not imply existence of a pair satisfying the dense-domain bounded finite-rank condition below, even when compact starred commutators are required.

## Meaning of the finite rank condition

For bounded coefficients with regular denominators,
\[
u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,
\]
the supplied operator has the exact natural domain
\[
\mathcal E_i=\{q\in H:bq,tq\in\operatorname{Dom}D_i\},
\qquad \Delta_iq=sD_i(bq)-aD_i(tq).
\]
The investigated condition retains T_F0001's requirement that every \(\mathcal E_i\) be Hilbert dense and that \(\Delta_i\) agree on its whole natural domain with a bounded finite-rank operator.
It is the existence of a single fraction pair satisfying this condition that is tested.
Finite-dimensional range on a zero domain is not sufficient.

## The supplied dual system

Let
\[
H=\mathcal F(\mathbb C^2)=\mathbb C\Omega\oplus\bigoplus_{n\ge1}(\mathbb C^2)^{\otimes n}.
\]
Write \(\ell_j\) and \(r_j\) for left and right creation by the standard basis vector \(e_j\).
Put
\[
X_j=\ell_j+\ell_j^*,\quad M=W^*(X_1,X_2),\quad
\tau(x)=\langle\Omega,x\Omega\rangle.
\]
This is the standard variance-one free semicircular tracial model, with faithful normal trace and \(H=L^2(M,\tau)\).
The checked local source interface is [Voi98-U005](../audits/literature/Voi98/Yin_U005.md#voi98-u005), especially its semicircular model and sign calculation.
That source supplies the standard model and attribution; the new domain obstruction below is a direct calculation.

Set \(\mathcal P=\mathbb C\langle X_1,X_2\rangle\Omega\), identifying bounded elements with their vacuum vectors.
Because the generators are selfadjoint, this is precisely the starred-polynomial domain.
Highest tensor-degree components of \(p(X)\Omega\) recover the highest-degree word coefficients of \(p\).
Thus evaluation of free polynomials is injective; triangular induction also shows that \(\mathcal P\) is exactly the span of all finite Fock words and is dense.

Specify the actual operators by
\[
\operatorname{Dom}D_i=\mathcal P,\qquad D_i=r_i^*|_{\mathcal P},\quad i=1,2.
\]
Direct word action gives
\[
[r_i^*,\ell_j]=\delta_{ij}P_\Omega,\qquad [r_i^*,\ell_j^*]=0.
\]
Consequently
\[
[D_i,X_j]p=[D_i,X_j^*]p=\delta_{ij}P_\Omega p\quad(p\in\mathcal P).
\]
All starred commutators therefore have finite-rank compact extensions.
Moreover
\[
D_i\Omega=0,\qquad D_i^*=r_i\text{ on all }H,\qquad D_i^*\Omega=e_i.
\]
These are actual Hilbert adjoints: restriction of a bounded operator to a dense domain has the full bounded adjoint.
The supplied operators are closable but not closed, and their closures are \(r_i^*\).
No closure is substituted into the natural-domain definition.

## A rational witness with no usable fraction pair

The semicircle law has no atom at zero, so \(X_1\) is regular in \(U(M)\).
Take
\[
u=X_1^{-1}X_2\in\operatorname{Div}_{U(M)}\mathbb C\langle X_1,X_2\rangle.
\]
A bounded left fraction is \(s=X_1,a=X_2\).
A bounded right fraction exists, for example
\[
t=(1+u^*u)^{-1/2},\qquad b=ut.
\]
Affiliated functional calculus makes \(t\) bounded and regular and \(b\) bounded; both belong to \(M\).
Thus the universal claim over fraction pairs below is not vacuous.

Consider any bounded right fraction \(u=bt^{-1}\) with \(t\) regular.
In \(U(M)\), and hence as an equality of bounded operators,
\[
X_1b=X_2t.
\]
If \(q\in\mathcal E_i\), write
\[
bq=R(X)\Omega,\qquad tq=Q(X)\Omega
\]
for free polynomials \(R,Q\).
The bounded equality implies
\[
X_1R(X)\Omega=X_2Q(X)\Omega.
\]
Polynomial injectivity gives the formal identity \(x_1R=x_2Q\).
Every word on the left starts with \(x_1\), and every word on the right starts with \(x_2\).
Linear independence of free words therefore forces \(R=Q=0\).
Since \(t\) is regular, \(tq=0\) forces \(q=0\).
Hence
\[
\boxed{\mathcal E_i(s,a,b,t)=\{0\}\quad\text{for every legal fraction pair and each }i.}
\]
The rational element \(u\) cannot satisfy the existential finite-rank condition, because no such pair has dense natural domains.
The argument does not depend on the chosen left coefficients.

The witness is genuinely unbounded.
Otherwise \(X_2=X_1u\) would imply
\[
X_2^2=X_1uu^*X_1\le\|u\|^2X_1^2.
\]
For \(e_\varepsilon=1_{[-\varepsilon,\varepsilon]}(X_1)\), freeness and variance one give
\[
\tau(e_\varepsilon X_2^2)=\tau(e_\varepsilon)>0,
\]
whereas the preceding inequality bounds it by \(\|u\|^2\varepsilon^2\tau(e_\varepsilon)\).
Small positive \(\varepsilon\) gives a contradiction.

## Interpretation and remaining questions

The obstruction is that \(x_1\mathbb C\langle x_1,x_2\rangle\cap x_2\mathbb C\langle x_1,x_2\rangle=\{0\}\).
In particular \(x_1^{-1}x_2\) has no scalar right quotient by nonzero polynomial numerator and denominator.
Any nonzero raw-domain vector would have supplied exactly such polynomial data.

This directly refutes rationality implying the SOME-only condition under the original supplied-domain assumptions, even with normalization, closability, and finite-rank starred commutators.
It does not decide the reverse implication separately.
If density is removed and only algebraic range dimension is counted, the zero-domain expression has rank zero; that is a different criterion.

Replacing the supplied operators by their closures gives everywhere bounded duals \(r_i^*\); natural domains then equal \(H\), and the existing bounded-dual criterion applies.
Thus requiring that supplied operators be closed, or that they equal the closures of their polynomial restrictions, remains a separate strengthened question.
A sufficient replacement must supply domain control for rational fraction inputs, not just generator commutator estimates.

## Dependencies and relationships

The direct external source interface is [Voi98-U005](../audits/literature/Voi98/Yin_U005.md#voi98-u005) for the standard tracial Fock model and creation-operator conventions.
Polynomial injectivity, supplied adjoints, the bounded right fraction, the zero-domain argument and the unbounded witness calculation are proved above.
No earlier project Claim is a mathematical premise of this counterexample.
The following links are comparisons and scope relationships, not logical dependency edges.

| Related material | Exact relationship |
| --- | --- |
| [T_F0001 v8](../tasks/Yin_T_F0001_v5.md#decision-candidate-0008), [contract and resolution](../tasks/Yin_T_F0001_v5.md) | Uses precisely the supplied-domain and dense bounded-extension convention. Settles the existential-only forward implication left undecided by the 2026-09-30 witnesses. This is a subsequent result; it does not rewrite that historical completion evidence or reactivate the Task. |
| [C_F0065 v2](Yin_C_F0065_v1.md#decision-candidate-0002), [two-model proof](Yin_C_F0065_v1.md) | C_F0065 exhibits a good and a bad pair for one rational element and disproves fraction independence. Here every pair is bad for a different rational element. C_F0065's closed supplied-operator model remains a distinct stronger-closedness observation; the present duals are not closed. |
| [C_F0026 v3](Yin_C_F0026_v1.md#decision-candidate-0002), [small-core domain obstruction](Yin_C_F0026_v1.md) | Earlier small-domain warnings alone did not disprove a dense natural-domain criterion. The present proof computes the whole natural domain for all fraction choices, eliminating that gap. |
| [C_F0063 v2](Yin_C_F0063_v1.md#decision-candidate-0002), [intrinsic criterion](Yin_C_F0063_v1.md) | Its hypotheses hold for this polynomial dual system, and its intrinsic finite-rank witnesses exist because u is rational. Its construction is not the literal zero-domain expression considered here. This gives a concrete separation without challenging C_F0063. |
| [C_F0064 v2](Yin_C_F0064_v1.md#decision-candidate-0002), [bounded weak-form criterion](Yin_C_F0064_v1.md) | The present witness is unbounded and the failed criterion requires agreement on literal composition domains. The bounded polynomial weak-form theorem retains its stated scope. |
| [C_F0013 v3](Yin_C_F0013_v1.md#decision-candidate-0002), [bounded-dual criterion](Yin_C_F0013_v1.md) | Replacing the supplied restrictions by their bounded closures gives its hypotheses and restores the original finite-rank criterion. The substitution changes the supplied operators and is not allowed in the present target. |
| [S_F0011](../strategies/Yin_S_F0011.md#s_f0011) | Refines the completed route's boundary for any later authorized domain-reduction question. A successor positive criterion must exclude this polynomial-domain obstruction. No new run or objective is selected here. |

The reverse implication from the existence condition to rationality is not decided separately.
Closed supplied operators, equality with the closed polynomial restriction, and suitable module or adjoint compatibility remain distinct possible strengthened hypotheses.
None is asserted sufficient by this proof.

## Promotion and review history

2026-10-01: the user asked whether replacing every fraction pair by some pair could restore equivalence.
Root constructed the present two-variable obstruction.
The separate agent existential_domain_audit checked the Fock signs, actual domains and adjoints, compact starred commutators, existence of bounded fractions, the all-pair zero-domain argument, and genuine unboundedness.
That conversational feedback preceded fixed-material acceptance.

2026-10-01: the user authorized ledger registration and links to related mathematical materials.
The working draft was promoted to this permanent version, preserving its proof and adding the precise statement and relationship map.
The resulting Claim is distinct from C_F0065 because its existential conclusion is materially stronger in quantifiers and uses a different witness.
Review and current assessment is recorded in the canonical Claim record; this history does not independently assign them.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-10-01T14:10 |
| status | open |

Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Recorded mathematical summary: A two-variable free semicircular example has normalized closable supplied duals with exact polynomial domains, full bounded adjoints and finite-rank starred commutators, but the genuinely unbounded rational element X1^-1 X2 has zero natural composition domain for every bounded regular fraction pair.
Thus even the existential original dense-domain finite-rank criterion fails; closed supplied duals remain a separate scope.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-10-01T14:20 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#existential-original-regular-commutator-counterexample) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0038_v1.md) | Whole fixed proof v1: standard tracial Fock model and variance, exact supplied polynomial domains, actual adjoints, all dual and starred commutators, nonvacuous bounded fraction pairs, zero natural domain for every pair, genuine unboundedness, Voi98-U005 source interface, and comparison-only relationships and closed-domain boundaries. Separate agent review; no Task completion, formal verification, or personal human inspection asserted. |

Recorded mathematical summary: A two-variable free semicircular example has normalized closable supplied duals with exact polynomial domains, full bounded adjoints and finite-rank starred commutators, but the genuinely unbounded rational element X1^-1 X2 has zero natural composition domain for every bounded regular fraction pair.
Thus even the existential original dense-domain finite-rank criterion fails; closed supplied duals remain a separate scope.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:18 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#existential-original-regular-commutator-counterexample) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0038_v1.md#c_f0066-existential-domain-review) | Independent fixed-input whole-proof review with no mathematical correction: all legal bounded fractions have zero natural domains for the genuinely unbounded rational witness. |

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/Voi98/Yin_U005.md).

Whole fixed proof v1: standard tracial Fock model and variance, exact supplied polynomial domains, actual adjoints, all dual and starred commutators, nonvacuous bounded fraction pairs, zero natural domain for every pair, genuine unboundedness, Voi98-U005 source interface, and comparison-only relationships and closed-domain boundaries.
Separate agent review; no Task completion, formal verification, or personal human inspection asserted.

Review: [Exact material](../audits/reviews/Yin_R_F0038_v1.md).

Material covered by that review: [Exact material](../audits/literature/Voi98/Yin_U005.md); [Exact material](Yin_C_F0066_v1.md).
