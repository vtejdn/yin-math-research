---
author: Yin
---

# Affiliated rationality from canonical closed duals under finite Fisher information

## Current decision

[Selected recorded decision](#decision-candidate-0010)

## Yin_T_F0001: Canonical Closed Dual Rationality under Finite Fisher Information

<a id="yin_t_f0001"></a>

Human record author: Yin.
Contract revision: 2026-10-01T16:40.
Canonical lifecycle: [Task record](Yin_T_F0001_v7.md#decision-candidate-0011).

<a id="canonical-closed-dual-authorization"></a>
## Authorization and Revised Objective

The user explicitly instructed on 2026-10-02: rewrite and activate T_F0001 under finite Fisher information, to investigate whether the intrinsic necessary-and-sufficient rationality criterion can be fully translated into the original composition criterion for the unique canonical closed dual.
This authorizes a successor contract under the same Task identity.
It replaces the arbitrary supplied-domain target with the precise canonical realization below.

The earlier [Task material v5](Yin_T_F0001_v5.md#yin_t_f0001), [Task decision 9](Yin_T_F0001_v5.md#decision-candidate-0009), completed lifecycle events and their reviews retain their historical scopes.
C_F0063/C_F0064 remain accepted intrinsic and bounded weak-form results.
C_F0065/C_F0066 remain accepted counterexamples to different supplied-domain statements.
This revision does not revoke those conclusions or promote the new target to a theorem.

## Setting and Canonical Operators

<a id="contract"></a>

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace.
Let \(d\geq1\) be finite, and let \(X=(X_1,\ldots,X_d)\) be bounded **selfadjoint** generators of \(M\).
No free independence or special joint distribution is assumed.
Set
\[
H=L^2(M,\tau),\quad \Omega=1,\quad
\mathcal A=\mathbb C\langle X_1,\ldots,X_d\rangle,\quad
\mathcal P=\mathcal A\Omega,\quad
F=\operatorname{Div}_{U(M)}\mathcal A.
\]
Inner products are linear in the second variable.
Elements of \(M\) act by left multiplication; identify \(M\Omega\) with its dense vector subspace of \(H\).
Products and inverses in the affiliated algebra \(U(M)\) use its usual closed-operator operations, not arbitrary everywhere-defined compositions.
Rationality means membership in \(F\), including genuinely unbounded elements.

Assume finite non-microstates free Fisher information:
\[
\Phi^*(X)=\sum_{i=1}^d\|\xi_i\|_2^2<\infty,
\qquad
\tau(p\xi_i)=(\tau\otimes\tau)(\partial_i p)
\quad(p\in\mathcal A).
\]
Here \(\partial_i X_j=\delta_{ij}1\otimes1\), with the Leibniz rule.
Equivalently, all first-order conjugate variables \(\xi_i\in H\) exist.
Their boundedness, Lipschitz regularity, and higher conjugates are not assumed.
The established conjugate-variable interface supplies algebraic freeness and the evaluated difference quotients; see [MS23-U001](../audits/literature/MS23/Yin_U001.md#ms23-u001).

Define the normalized polynomial dual with **exact initial domain** \(\mathcal P\):
\[
D_{i,0}(p\Omega)=(\mathrm{id}\otimes\tau)(\partial_i p)\Omega,
\qquad
\boxed{D_i=\overline{D_{i,0}}.}
\tag{CD}
\]
The conjugate-variable interface proves closability.
Consequently \(D_i\) is closed, \(\mathcal P\) is its graph core, \(D_i\Omega=0\), \(\Omega\in\operatorname{Dom}D_i^*\), and \(D_i^*\Omega=\xi_i\).
The polynomial identity \([D_{i,0},X_j]=\delta_{ij}P_\Omega\) extends by graph approximation to the full domain of \(D_i\), which is invariant under each \(X_j\).
The starred identity is the same because the generators are selfadjoint.

Equivalently, require a normalized dual with the actual adjoint-vacuum condition, the polynomial dual identities, closedness, and \(\mathcal P\) as graph core.
Its polynomial action is forced, so these conditions select exactly (CD).
Existence of this system is equivalent to finite Fisher information in this finite selfadjoint setting; specifying the core selects the realization, not an extra distributional regularity assumption.

The closure in (CD) is the closure of the **contracted polynomial operator**.
Do not identify it without proof with the raw composite \((\mathrm{id}\otimes\tau)\overline{\partial_i}\) on the latter's default domain.
No adjoint graph-core property, all-\(M\) domain, boundedness of \(D_i\), or left-\(M\)-module domain is assumed.
A nonclosed restriction or a larger closed extension is not the operator in this contract.
Cases where the canonical duals themselves are bounded, including the standard semicircular case, remain included; boundedness of a different unnormalized dual does not by itself assert boundedness of (CD).

## Raw Natural Domains and the Finite-Rank Condition

For \(u\in U(M)\), let \(Q=(s,a,b,t)\) be any legal bounded fraction quadruple:
\[
u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,
\qquad s,t\text{ regular}.
\]
Regular means invertible in \(U(M)\), equivalently injective with dense range on \(H\) here.
Fraction coefficients are not required to be rational or polynomial.

For each \(i\), use the full literal natural domain
\[
\mathcal E_i(Q)=\{q\in H:bq,tq\in\operatorname{Dom}D_i\},
\]
and define
\[
\Delta_i(Q)q=sD_i(bq)-aD_i(tq),\qquad q\in\mathcal E_i(Q).
\tag{RC}
\]
Write \(\operatorname{Raw}(u;Q)\) if, for every \(i\), \(\mathcal E_i(Q)\) is Hilbert dense and (RC) agrees on **all of that domain** with a bounded finite-rank operator \(T_i(Q)\in B(H)\).
Density makes \(T_i(Q)\) unique.
Rank means ordinary complex Hilbert-space rank.
Algebraically finite-dimensional range on a nondense domain, or agreement on an unproved smaller core, does not qualify.

SOME means one common quadruple \(Q\) satisfies this condition for every \(i\); ALL means every legal \(Q\) does.
The specified density is per-coordinate.
If a proof uses an intersection of the \(\mathcal E_i\), establish its density separately and still prove agreement on each full natural domain.
Universal density for nonrational \(u\) is not a separate requirement of this contract.

## Three Obligations for Full Translation

The target covers every \(u\in U(M)\) under exactly the setting above.
Track these statements separately:

1. **(S), existential equivalence:**
   \[
   u\in F\quad\Longleftrightarrow\quad
   \exists Q\ \operatorname{Raw}(u;Q).
   \]
2. **(A), arbitrary-fraction forward assertion:**
   \[
   u\in F\quad\Longrightarrow\quad
   \forall Q\ \operatorname{Raw}(u;Q).
   \]
   Together with (S), this gives the complete SOME/ALL equivalence and finite-rank fraction independence.
   Numerical-rank invariance may be recorded if proved, but is not a substitute for these assertions.
3. **(C), compatibility with the intrinsic representatives:** at every pair covered by the positive raw or intrinsic finite-rank criterion, prove that the unique bounded raw extension is the intrinsic representative from C_F0063.
   In particular, for rational \(u\) and every legal \(Q\), prove
   \[
   T_i(Q)=K_i^{\mathrm{int}}(u;Q)
   =\Theta\bigl(s(\partial_i^{\mathrm{rat}}u)t\bigr),
   \qquad
   \Theta(g\otimes h)q=g\tau(hq),
   \]
   with equality between (RC) and this operator on the entire \(\mathcal E_i(Q)\).
   When starting with a raw finite-rank extension for an element not yet known to be rational, prove that it represents the intrinsic tests; do not define it using a rational derivative before establishing rationality.

For clarity, the fixed intrinsic objects use right multiplication \(R_iq=qX_i\) and the actual closures
\[
A_i=\overline{\mathrm i(R_iD_{i,0}-D_{i,0}R_i+I)|_{\mathcal P}},
\qquad
\Phi_i(Q)q=sA_i(bq)-aA_i(tq)\quad(q\in M\Omega).
\]
C_F0063 supplies \(M\Omega\subseteq\operatorname{Dom}A_i\).
An intrinsic finite-rank representative is a \(K_i\in\operatorname{FinRank}(H)\) satisfying
\[
\Phi_i(Q)q=\mathrm i[R_i,K_i]q\qquad(q\in M\Omega).
\]
The representative, when it exists, is unique in the finite-rank class.
Merely proving \(\Phi_i(Q)\) finite rank is insufficient.
Using \(A_i\) or the intrinsic tests as auxiliary objects is permitted; the final raw assertion must concern (CD)/(RC).

## Accepted Inputs, Starting Lead and Counterexample Boundaries

- [C_F0063_v1](../claims/Yin_C_F0063_v1.md#decision-candidate-0002), with its [complete proof](../claims/Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion), supplies the intrinsic affiliated iff criterion, arbitrary-fraction independence and its exact realization.
  Finite Fisher information for selfadjoint tuples meets its hypotheses through the normalized polynomial dual; the starred compact condition is automatic.
  This is the accepted positive baseline, not a proof of (S)/(A)/(C).
- [C_F0064_v1](../claims/Yin_C_F0064_v1.md#decision-candidate-0002), with its [bounded weak-form and graph theorem](../claims/Yin_C_F0064_v1.md#normal-small-core-bounded-rationality), supplies bounded rational domain invariance and finite-rank commutators for the normalized actual closures.
  Its bounded scope alone does not resolve arbitrary unbounded fractions.
- The discussion on 2026-10-02 identified a direct forward lead: for rational \(u\), take \(t=(1+u^*u)^{-1}\), \(b=ut\), \(s=(1+uu^*)^{-1}\), \(a=su\).
  These are bounded rational coefficients.
  C_F0064's graph and adjoint identities are the proposed route to density and full-domain agreement for this pair.
  This new corollary has not been separately registered or accepted as a reviewed result.
  Its precise proof and source interfaces are to be checked before reuse as accepted support; it does not settle the reverse of (S), (A), or full (C).
- [C_F0065_v1](../claims/Yin_C_F0065_v1.md#decision-candidate-0002) and [C_F0066_v1](../claims/Yin_C_F0066_v1.md#decision-candidate-0002) are comparison boundaries, not logical premises for the positive target.
  C_F0066 uses a nonclosed polynomial restriction.
  C_F0065's second model is an unnormalized closed extension with extra graph vectors, and its polynomials are not a graph core.
  Neither gives a counterexample to (CD).
  Their old proofs and acceptance evidence remain unchanged.
- The [standard semicircular affiliated criterion](../audits/literature/Miy22/Yin_U007.md#miy22-u007) is a calibration case: (CD) must recover the bounded right annihilators for that tuple.
  When the canonical \(D_i\) themselves are bounded, [C_F0013_v1](../claims/Yin_C_F0013_v1.md#decision-candidate-0002) applies directly.
  Its theorem for other supplied bounded duals does not identify their canonical normalization as bounded without proof.
  An obstruction created only by shrinking the semicircular canonical domain is outside the new contract.

The active route is [Yin_S_F0011](../strategies/Yin_S_F0011.md#s_f0011).
Prioritize the exact forward lead and the raw-to-intrinsic reverse bridge, then arbitrary-fraction domains.
Any stronger assumptions on conjugates or domains must be labeled as conditional variants and compared with the finite-Fisher target; a stronger variant alone does not resolve it.

## Completion and Review Criteria

A positive completion requires proofs of (S), (A), and (C) with their full quantifiers, actual domains, extension uniqueness and compatibility with the semicircular/bounded-dual benchmark.
Repeating C_F0063's intrinsic theorem or C_F0064's bounded weak theorem alone is insufficient.

A negative completion of the full-translation question requires a rigorous counterexample to a named obligation under **the exact canonical operators (CD)** and finite Fisher information.
Compute the decisive domains and defects.
A rational element with one bad pair refutes (A), not necessarily (S); failure of the forward direction of (S) requires every pair to fail; a nonrational element with one good pair refutes the reverse direction of (S).
Failure of an auxiliary estimate, a missing vacuum vector, or a different supplied operator is not enough.
A witness discrepancy refutes (C) only after both relevant representatives and their asserted domains have actually been justified.

For any negative outcome, state separately which parts of (S), (A), and (C) remain unresolved.
A counterexample to one obligation can decide full translation negatively without being described as refuting every branch.
No such stronger follow-up is silently activated or declared complete.

Before any completion transition, obtain a complete independent mathematical review of the supporting proof or counterexample and its actual dependencies, followed by a comparison with this contract.
This retains the earlier Task's completion-review requirement.
Preserve the distinction between construction, self-review, independent review, and formal verification.
The present rewrite and activation constitute contract maintenance, not mathematical acceptance.

## Historical Scope, Manuscript and Execution

Earlier intrinsic completion, the supplied-domain negative completion, and the C_F0066 follow-up remain in their fixed materials and immutable metadata versions.
Current lifecycle history must append the user-authorized completed-to-active transition; earlier completion events and review bindings must not be rewritten.

This revision does not authorize manuscript revision, designate a new main theorem or alter other Task contracts.

Apply the [execution rules](../../framework/rules/execution.md) when an autonomous run starts.
Contract activation itself creates no execution run and does not resume an old stopped run or import its usage override.
Mathematical lifecycle and execution status remain separate.


## Lifecycle and completion


### Decision candidate-0010

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-10-01T16:45 |
| status | active |
| authority | Explicit user instruction of 2026-10-02 to rewrite and activate T_F0001 under finite Fisher information, recorded in mathematics/tasks/Yin_T_F0001_v6.md#canonical-closed-dual-authorization. |
| reason | Rewrite and reactivate T_F0001 under finite Fisher information with the unique canonical closed duals; separate existential equivalence, arbitrary-fraction independence and intrinsic/raw compatibility while preserving historical completions. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Exact material](#contract) | Exact original contract and success conditions retained in this material. |
| dependency | [Exact material](../claims/Yin_C_F0063_v1.md#decision-candidate-0002) | Accepted intrinsic affiliated rationality iff criterion, arbitrary-fraction independence and canonical finite-rank representatives. Selfadjoint finite-Fisher tuples meet its polynomial-dual assumptions; no raw-domain equivalence is imported. |
| dependency | [Exact material](../claims/Yin_C_F0064_v1.md#decision-candidate-0002) | Accepted bounded weak rationality, normalized original closure graph invariance and bounded finite-rank commutators for bounded rational elements. These are inputs to the proposed forward bridge, not completion of the new affiliated raw criterion. |

Recorded mathematical summary: User-authorized active successor under finite non-microstates Fisher information for finite bounded selfadjoint generating tuples.
Fix the unique normalized closed duals obtained by closing the contracted polynomial difference quotients.
Determine whether the accepted intrinsic affiliated iff criterion fully translates to the original regular commutators on their entire natural domains: separately resolve SOME equivalence, ALL fraction independence, and equality of raw finite-rank extensions with intrinsic representatives.
C_F0063/C_F0064 are accepted baselines; C_F0065/C_F0066 concern different supplied domains.
Earlier completion decisions remain historical and do not resolve this canonical target.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/MS23/Yin_U001.md).

Whole original T_F0001 contract at recorded assessment 5 and prepared Task material v3; complete C_F0063 (recorded assessment 2) main proof and Appendix A, C_F0062 (recorded assessment 2) graph bridge, C_F0064 (recorded assessment 2) bounded companion, actual dependencies and accepted source interfaces.
Every affiliated element and arbitrary bounded fraction pair, both directions and numerical-rank independence are covered under the explicitly permitted intrinsic tensor-test realization.
Literal arbitrary raw composition domains, original all-M dual domains and arbitrary unnormalized full-domain invariance remain unproved strengthenings.
No manuscript designation, formal verification or external review is claimed.

Completion contract: [Exact material](Yin_T_F0001_v3.md#contract).

Review: [Exact material](../audits/reviews/Yin_R_F0031_v1.md).

Material covered by that review: [Exact material](../audits/reviews/Yin_R_F0032_v1.md); [Exact material](../ledger/Yin_L_F0016_v1.md); [Exact material](Yin_T_F0001_v2.md#reorganization-authorization-2026-09-27); [Exact material](Yin_T_F0001_v3.md).

Whole unchanged T_F0001 contract at recorded assessment 7 and successor resolution, complete C_F0065 two-model proof with actual supplied domains and dependencies, exact negative alternative, compact baseline and remaining strengthened/existential-only scopes.

Completion contract: [Exact material](Yin_T_F0001_v5.md#contract).

Review: [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r107).

Material covered by that review: [Exact material](../audits/reviews/Yin_R_F0032_v1.md); [Exact material](../claims/Yin_C_F0065_v1.md); [Exact material](../ledger/Yin_L_F0016_v1.md); [Exact material](Yin_T_F0001_v2.md#reorganization-authorization-2026-09-27); [Exact material](Yin_T_F0001_v5.md).

## Execution boundary

`execution/Yin_E_F0001.md`.
