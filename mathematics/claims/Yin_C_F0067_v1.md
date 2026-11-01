---
author: Yin
---

# Canonical closed-dual raw rationality on the full natural domain

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023)

## Yin_C_F0067: Canonical closed duals on the full natural domain

<a id="statement"></a>
<a id="canonical-closed-dual-raw-rationality"></a>

Date: 2026-10-02, Asia/Hong_Kong.
Human research author: Yin.
Construction: `canonical_raw_reverse`, during the user-authorized T_F0001 run.
Status is owned by the [canonical Claim record](#current-assessment).
This complete proof has a [separate whole-proof and contract review](../audits/reviews/Yin_R_F0079_v1.md#retained-r109-conclusion).
The canonical records own its accepted assessment and the Task lifecycle.

The target is [T_F0001 material v6](../tasks/Yin_T_F0001_v6.md#yin_t_f0001), under its exact selfadjoint finite-Fisher hypotheses and canonical closures.
The proof below discharges its three mathematical obligations (S), (A), and (C), subject to the accepted inputs stated here and independent review.

## 1. Reuse finding and exact inputs

The needed analytic interface is an actual bounded-vector domain for both the normalized closed dual and its Hilbert adjoint.
A targeted local search of the ledger, MS23 source audits, and the method index found the already accepted [C_F0022_v1](Yin_C_F0022_v1.md#decision-candidate-0002), with its [complete proof](Yin_C_F0022_v1.md#yin_c_f0022) and [whole-artifact review](../audits/reviews/Yin_R_F0010_v1.md).
Its exact operators are the canonical closures used in the current contract.
The method index had no more specific competing domain method.
No external search was needed to replace or reprove this accepted project input.

This result had been missed in the recent discussion of the selfadjoint canonical version.
The earlier unresolved all-M boundary concerned general normal tuples and arbitrary supplied operators; it must not be imported into the present selfadjoint canonical problem.

Use precisely the following two direct mathematical dependencies:

1. **C_F0022 (recorded assessment 3), Sections 1, 3, and 5--7.**
   For bounded selfadjoint generators with finite non-microstates Fisher information and the canonical closures below, both actual domains contain every bounded vector.
   Their restrictions to bounded vectors satisfy infinity-to-L2 bounds and bounded-set weak continuity.
   Rationality is equivalent to finite-rank cleared defects on the dense vector space M, for some or every legal bounded fraction pair.
   These defects have unique bounded finite-rank extensions, and their ranks are independent of the pair.
2. **C_F0063 (recorded assessment 2)**, [complete intrinsic criterion and construction](Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion).
   The liberation closure and finite-rank intrinsic representative are the actual objects specified in that result.
   The representative is unique in the finite-rank class; for rational u and every fraction pair it equals the cleared rational-derivative tensor.
   Its hypotheses follow from the present canonical selfadjoint dual identities and adjoint-vacuum condition.

C_F0022's analytic source is [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002), especially Lemma 12's contraction estimate and the actual-closure argument.
Its existing source review includes the one-variable reduction and its closed-real-derivation functional-calculus inspection limit.
That source is retained through C_F0022; this draft does not claim a fresh audit of Dab10 or its entire foundational theory.
C_F0064 is compatible but is not needed as a direct dependency.
No new general contraction theorem is being claimed.

## 2. Statement with the literal operators

Let (M,tau) be finite with faithful normal probability trace.
Let X_1,...,X_d, d finite and positive, be bounded selfadjoint generators with finite non-microstates Fisher information.
Put H=L2(M,tau), Omega=1, P=C<X>Omega, and F=Div_(U(M)) C<X>.
Inner products are linear in the second variable.
Identify M with its bounded-vector subspace M Omega of H.

Define on exactly P

    D_i0(p Omega)=(id tensor tau)(partial_i p) Omega,
    D_i=closure(D_i0).

No larger extension of D_i is used.
For every u in U(M) and every legal bounded fraction quadruple Q=(s,a,b,t),

    u=s^(-1)a=b t^(-1),  s,a,b,t in M,  s,t regular,

define its full natural domain and raw composition by

    E_i(Q)={q in H : bq,tq in Dom D_i},
    Delta_i(Q)q=s D_i(bq)-a D_i(tq).

Then the following assertions hold:

1. M is contained in E_i(Q) for every i, every u and every Q.
   In particular all these natural domains are Hilbert dense, and their finite intersection is Hilbert dense as well.
2. The following are equivalent:
   - u belongs to F;
   - for some single Q, all Delta_i(Q) agree on their entire E_i(Q) with bounded finite-rank operators;
   - for every Q, all Delta_i(Q) have that property.
3. At any such Q, the unique raw bounded extension T_i(Q) is exactly the C_F0063 intrinsic representative:

       T_i(Q)=K_i^int(u;Q)=Theta(s(partial_i^rat u)t),
       Theta(g tensor h)q=g tau(hq).

   Its rank, for each i, is independent of Q.
   If one starts with a raw finite-rank extension before rationality is known, the compatibility calculation below identifies it by the intrinsic tests without first invoking a rational derivative.

## 3. All bounded vectors lie in both actual domains

C_F0022 applies with precisely the same algebra, trace, generating tuple, normalization and initial domain.
Its Sections 2--3 give

    M subset Dom D_i intersect Dom D_i*,
    ||D_i x||_2 <= 4 ||xi_i||_2 ||x||,
    ||D_i* x||_2 <= 5 ||xi_i||_2 ||x||,             x in M.       (1)

They concern the actual Hilbert-space closure and adjoint, not a chosen extension of their values on C*(X).
They imply immediately that bq,tq are in Dom D_i for every bounded vector q.
Hence M subset E_i(Q), including when u is not rational.
This also gives M subset intersection_i E_i(Q).

We shall use the bounded-set weak continuity from the same input:

    x_alpha -> x in L2,  x_alpha,x in M,
    sup_alpha ||x_alpha|| < infinity
       implies D_i x_alpha -> D_i x weakly in H.                (2)

The corresponding adjoint continuity is also established there, although the bridge lemma below only requires its domain inclusion.

## 4. Adjoint testing extends agreement to the full natural domain

The following direct Hilbert-adjoint argument is independent of rationality.

**Bridge lemma.**
Let D be densely defined on H=L2(M,tau), and assume M subset Dom D intersect Dom D*.
Let s,a,b,t belong to M.
Suppose a bounded operator K agrees on M with q -> sD(bq)-aD(tq).
Then it agrees on the entire natural domain E={q:bq,tq in Dom D}.

**Proof.**
For eta in M, the actual adjoint-domain assumption makes s*eta and a*eta elements of Dom D*.
Consequently

    v_eta=b*D*(s*eta)-t*D*(a*eta)                              (3)

is a defined vector in H.
For z in M, the asserted equality and adjoint identities give

    <v_eta,z>=<eta,sD(bz)-aD(tz)>=<eta,Kz>=<K*eta,z>.

Density of M shows v_eta=K*eta.
Now q in E need not be a bounded vector; its two stipulated D inputs nevertheless make the same pairing legitimate:

    <eta,sD(bq)-aD(tq)>=<v_eta,q>=<eta,Kq>.

Since this holds for every eta in the dense vector space M, the two H vectors agree.
This proves the lemma.
No simultaneous graph approximation of bq and tq, adjoint graph-core assumption, or domain invariance under the fraction coefficients was used.
Finite rank was not required.
QED.

## 5. Proof of the raw equivalence and arbitrary-fraction assertion

Suppose u is rational and fix an arbitrary legal Q.
C_F0022 supplies a bounded finite-rank K_i whose restriction to M is precisely the cleared defect sD_i b-aD_i t.
Apply the bridge lemma using (1).
It gives equality with K_i on all of E_i(Q).
Section 3 supplied density; thus Raw(u;Q) holds, proving the universal forward assertion (A).
The same conclusion implies the existential forward assertion.
There is always at least one legal common quadruple for affiliated u, by the standard bounded-fraction construction already included in C_F0022's setting.

Conversely, suppose one common Q satisfies Raw(u;Q).
Since M subset E_i(Q), restrict each raw bounded finite-rank extension to M.
These restrictions are the operators used by C_F0022's criterion.
Its reverse implication gives u in F.
This proves (S), and with the universal forward result gives all three equivalences in Section 2.

Because the extensions agree on M, they are the unique bounded extensions constructed in C_F0022.
Its finite-rank numerical independence therefore also holds for the raw operators.
No rationality conclusion was inferred from the algebraic rank of an operator on an unproved dense domain.

## 6. Coordinate compatibility with the actual intrinsic tests

Fix i and write R_i q=qX_i.
In C_F0063 let

    A_i0=i(R_i D_i0-D_i0 R_i+I) on P,
    A_i=closure(A_i0).

For every x in M, we first establish the actual equality

    A_i x=i(R_i D_i x-D_i(R_i x)+x).                         (4)

Choose uniformly norm-bounded polynomial approximants p_alpha to x in L2; they exist by Kaplansky density and norm approximation in C*(X).
Since R_i is bounded, p_alpha X_i -> xX_i in L2, with uniformly bounded operator norms.
Formula (2), applied both to p_alpha and to p_alpha X_i, gives the weak H convergence

    A_i0 p_alpha -> i(R_i D_i x-D_i(xX_i)+x).

The graph of the actual closed operator A_i is a closed linear subspace of H direct-sum H, hence weakly closed.
The first graph coordinates p_alpha converge strongly, and therefore weakly, to x.
The limit graph pair yields (4).
In particular no equation between closures of formal operator sums was assumed, and the extension in (4) is the actual A_i.

Now suppose at a legal Q that K_i is a bounded operator agreeing on M with sD_i b-aD_i t.
This assumption in particular holds for any raw finite-rank extension, before rationality has been inferred.
For z in M, R_i z is again in M, so both terms of the following calculation are available.
Right multiplication commutes with all left coefficients:

    i[R_i,K_i]z
      = i s(R_i D_i-D_i R_i)(bz)
           -i a(R_i D_i-D_i R_i)(tz)
      = s(A_i-iI)(bz)-a(A_i-iI)(tz)
      = sA_i(bz)-aA_i(tz).                                  (5)

The last equality uses sb=at, which follows from the legal fraction identities in U(M) and is an equality of bounded elements of M.
Every D_i and A_i input in this calculation is a bounded vector.
The left side is a bounded H-operator; the right side is the intrinsic defect on its specified full test domain M.

If K_i is finite rank, (5) says exactly that it represents C_F0063's intrinsic tests.
This proves the raw-to-intrinsic implication directly; no rational derivative was used to define K_i.
The intrinsic theorem can therefore also serve as a second route to the reverse of (S).

Conversely, whenever the intrinsic finite-rank criterion holds for all i, C_F0063 gives u in F.
Section 5 then supplies the full-domain raw extensions for every Q, and (5) identifies their intrinsic tests.
The finite-rank uniqueness in C_F0063 forces the raw extensions to equal its intrinsic representatives.
Its rational tensor identification gives the formula in Section 2 and completes (C), on every full E_i(Q).

## 7. Contract comparison and preserved boundaries

The new argument is the full-domain adjoint bridge and its application to the already accepted selfadjoint C_F0022 theorem, together with the explicit coordinate identification (4)--(5).
The genuinely new bridge is short; the analytic regularity input was already proved in C_F0022 and audited in Dab10-U002.
No claim of a newly discovered finite-Fisher criterion is made.

The result does not alter C_F0063's general-normal intrinsic scope.
Nor does it claim all bounded vectors belong to arbitrary unnormalized, nonclosed, or enlarged supplied dual domains.
C_F0065 and C_F0066 use different operators and retain their original conclusions.
Here the canonical choice is essential for applying C_F0022; replacing it by an arbitrary supplied realization is not part of the proof.

On the standard semicircular model the canonical closures are the bounded right annihilators, so E_i(Q)=H and the result specializes to the familiar bounded-dual raw criterion.
In the present general finite-Fisher case, E_i(Q) may be a proper dense subspace; equality is nevertheless proved at every one of its vectors.
The statement never asserts that D_i is H-bounded or that its domain is all H.

Review requirement: a separate whole-proof review must check the exact C_F0022 and C_F0063 input scopes, the adjoint-test quantifiers, coordinate signs, and all three obligations against Task material v6 before proof acceptance or any completion transition.
The proof itself supplies no such independent acceptance evidence; the canonical records bind the actual review.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-10-02T13:02 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#canonical-closed-dual-raw-rationality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0022_v1.md#decision-candidate-0002) | Exact canonical selfadjoint finite-Fisher duals and their adjoints contain M; bounded-set weak continuity; SOME/ALL rationality and numerical-rank independence for cleared defects on M. |
| dependency | [Exact material](Yin_C_F0063_v1.md#decision-candidate-0002) | Actual liberation closures, intrinsic affiliated rationality criterion and unique finite-rank representatives, with the cleared rational-derivative tensor identification. |

Recorded mathematical summary: Finite selfadjoint tuples with finite free Fisher information: rationality is equivalent to SOME and ALL original cleared defects extending as bounded finite-rank operators on their entire natural domains; all natural domains contain M, and the extensions equal the unique intrinsic representatives.
Reuses C_F0022 with an adjoint-test full-domain bridge and C_F0063 compatibility.

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:18 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#canonical-closed-dual-raw-rationality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0022_v1.md#decision-candidate-0002) | Exact canonical selfadjoint finite-Fisher duals and their adjoints contain M; bounded-set weak continuity; SOME/ALL rationality and numerical-rank independence for cleared defects on M. |
| dependency | [Exact material](Yin_C_F0063_v1.md#decision-candidate-0002) | Actual liberation closures, intrinsic affiliated rationality criterion and unique finite-rank representatives, with the cleared rational-derivative tensor identification. |
| review | [Original finding](../audits/reviews/Yin_R_F0079_v1.md#retained-r109-conclusion) | Unknown initial relationship after construction/applicability summaries of unspecified actual content; complete seven-section canonical full-natural-domain theorem with original accepted-source limits. |


### Decision isolated-whole-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T01:29 |
| status | proved |
| reason | Adopt the fresh isolated whole-proof finding after its initial mathematical judgment and subsequent comparison with the separately preserved original unknown account(s). Preserve the exact statement, proof, mathematical status, all non-review inputs and every historical decision; no Task lifecycle change or mathematical repair. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#canonical-closed-dual-raw-rationality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0022_v1.md#decision-candidate-0002) | Exact canonical selfadjoint finite-Fisher duals and their adjoints contain M; bounded-set weak continuity; SOME/ALL rationality and numerical-rank independence for cleared defects on M. |
| dependency | [Exact material](Yin_C_F0063_v1.md#decision-candidate-0002) | Actual liberation closures, intrinsic affiliated rationality criterion and unique finite-rank representatives, with the cleared rational-derivative tensor identification. |
| review | [Fresh whole-proof finding](../audits/reviews/Yin_R_F0079_v1.md#fresh-c109-whole) | Independently reviewed. Whole Sections 1-7, every full natural domain, SOME/EVERY and numerical ranks, actual canonical closures and intrinsic compatibility. |

## Historical assessments

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-10-02T13:13 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#canonical-closed-dual-raw-rationality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0022_v1.md#decision-candidate-0002) | Exact canonical selfadjoint finite-Fisher duals and their adjoints contain M; bounded-set weak continuity; SOME/ALL rationality and numerical-rank independence for cleared defects on M. |
| dependency | [Exact material](Yin_C_F0063_v1.md#decision-candidate-0002) | Actual liberation closures, intrinsic affiliated rationality criterion and unique finite-rank representatives, with the cleared rational-derivative tensor identification. |
| review | [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r109) | Complete C_F0067_v1 Sections 1-7 and exact C_F0022 (recorded assessment 3)/C_F0063 (recorded assessment 2) interfaces: actual canonical/adjoint domains, all natural-domain vectors, SOME/ALL common-fraction equivalence, intrinsic compatibility without circular rational differentiation, numerical ranks, d=1 and bounded semicircular benchmark; separately organized AI mathematical review with context exposure and accepted-source inspection limits disclosed. |

Recorded mathematical summary: Finite selfadjoint tuples with finite free Fisher information: rationality is equivalent to SOME and ALL original cleared defects extending as bounded finite-rank operators on their entire natural domains; all natural domains contain M, and the extensions equal the unique intrinsic representatives.
Reuses C_F0022 with an adjoint-test full-domain bridge and C_F0063 compatibility.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Complete C_F0067_v1 Sections 1-7 and exact C_F0022 (recorded assessment 3)/C_F0063 (recorded assessment 2) interfaces: actual canonical/adjoint domains, all natural-domain vectors, SOME/ALL common-fraction equivalence, intrinsic compatibility without circular rational differentiation, numerical ranks, d=1 and bounded semicircular benchmark; separately organized AI mathematical review with context exposure and accepted-source inspection limits disclosed.

Review: [Exact material](../audits/reviews/Yin_R_F0079_v1.md#retained-r109).

Material covered by that review: [Exact material](Yin_C_F0067_v1.md).
