---
author: Yin
---

# Independent internal review: Yin_C_F0050 annulus-local dual domains

Mathematical review completed: 2026-09-16T13:01.
Human record author: Yin.
Reviewer: separately organized Codex research subagent the reviewing agent; proof author: research subagent another AI agent; coordinator: root.

Reviewed Claim: [Yin_C_F0050_v1](../../claims/Yin_C_F0050_v1.md#decision-candidate-0001).
Consumer scope: the original normal polynomial-core domain question; this identifies scope rather than a logical proof dependency.

Selected statement and complete supporting proof: [annulus-local-dual-domains.md, anchor annulus-local-dual-domains](../../claims/Yin_C_F0050_v1.md#annulus-local-dual-domains), Sections 1--8.
No additional earlier proof is selected as auxiliary support.

**Verdict: pass for assertions A and B, including the mixed-pairing compatibility stated in Section 7.**
Assertion C is explicitly unresolved and is not accepted as a theorem.
The proof establishes original local dual and adjoint domains and a full affiliated criterion on a common dense module.
It does not establish the original polynomial weak-form converse or equality of the original closure with the closure of the module restriction.

This was a separately organized internal AI review, not blind review or external human review.
Before reading the author's complete A/B argument, the reviewer independently investigated the original-closure bridge and communicated a conditional vacuum graph-approximation argument to root.
The reviewer did not write the A/B proof, propose its local lifting estimates, or modify the author's artifact.
The earlier bridge discussion is disclosed because Section 7 concerns the same unresolved interface.

## Artifact correspondence and fixed direct inputs

The reviewer inspected the complete diff between the initial draft and the final material.
The changes were to opening provenance/status text, the semantic anchor, relative links and layout; the inspected mathematical text was unchanged.
The mathematical pass rests on the reasoning below.

All Claim inputs below have repository UID `a8c6a9c0-1862-4303-917f-cd13f3e71b59`.
These are the complete direct Claim interfaces used in the displayed proof:

| Fixed direct dependency | Exact scope used |
| --- | --- |
| [Yin_C_F0025_v1](../../claims/Yin_C_F0025_v1.md#decision-candidate-0002) | Exact compact starred-core hypotheses; normalization; canonical marginal divided differences; actual polynomial adjoint and bounded-generator domain invariance. |
| [Yin_C_F0029_v1](../../claims/Yin_C_F0029_v1.md#decision-candidate-0002) | Full affiliated criterion on a common dense left module with dense left-module adjoint tests; fraction independence and bounded-element criterion for the closure of that restriction. The selected proof is [P2](../../claims/Yin_C_F0029_v1.md#yin_c_f0029-p2); the same Claim retains the [authoritative statement](../../claims/Yin_C_F0029_v1.md#yin_c_f0029) and [strict noncommuting example](../../claims/Yin_C_F0029_v1.md#8-a-strict-noncommuting-example). |
| [Yin_C_F0045_v1](../../claims/Yin_C_F0045_v1.md#decision-candidate-0002) | Sections 3--5: full original-core right-module decomposition, conditional-expectation column estimate, marginal normalized vacuum, and actual direct-sum closure/adjoint formulas, before the global marginal norm hypothesis is used. |
| [Yin_C_F0047_v1](../../claims/Yin_C_F0047_v1.md#decision-candidate-0002) | Radial midpoint sufficient criterion, including arbitrary positive-radius atoms, applied to a fixed annular probability. |
| [Yin_C_F0048_v1](../../claims/Yin_C_F0048_v1.md#decision-candidate-0002) | Measurable-density sufficient transfer on that annular probability, with its original closed and adjoint domains; no C1 density converse is used. |
| [Yin_C_F0049_v1](../../claims/Yin_C_F0049_v1.md#decision-candidate-0002) | Sections 2--3 annular finite-measure normalization and original-graph smooth cutoff argument; each use needs only the selected annular bounds, and the proof reconstructs the adapted interface. |

The directly used external source interfaces remain [Pis12-U001](../literature/Pis12/Yin_U001.md#pis12-u001), and [VV16-U001](../literature/VV16/Yin_U001.md#vv16-u001).
Their recorded source identification, statements and application scopes were checked.
Their historical theorem proofs were not newly audited, and no fresh web acquisition is claimed.
Ordinary Hilbert adjoint/closed-graph facts, Kaplansky density, finite-trace projection inequalities and conditional expectation are used as the accepted functional-analytic foundations already specified in the direct Claim inputs.

Input disclosure: the reviewer had the shared task scope, earlier bridge discussion, and the coordinator's notice about the corrected radial-support quantifier.
Before initial A/B findings, the reviewer read the complete target and relevant direct proof inputs, and consulted the earlier C_F0045 complete review and the two source-interface records.
This is an independent reconstruction of the new A/B assembly with disclosed prior context, not a blind review or a new full audit of every upstream theorem.

## 1. Exact hypotheses and annular input

The corrected probability condition is `sigma_j((0,R_j])=1`; the text expressly allows zero in its topological support.
Thus the statement does not inadvertently impose a positive minimum radius.
Only the selected annulus supplies positive upper and lower density bounds.
The global measure outside that annulus enters the cutoff calculation solely through kernels separated from the cutoff support.

The reviewer read the exact compact-core hypotheses and normalization in C_F0025; the full-core decomposition and actual adjoint calculation in C_F0045; C_F0049's annular normalization and cutoff recovery; the measurable sufficient direction in C_F0048; and the radial criterion statement in C_F0047.
For a restricted probability on `a<r<c`, the radial midpoint quantity is at most `1/a`, including arbitrary positive-radius atoms.
The C_F0048 sufficient direction requires only measurable density, so it applies with the annulus-specific constants.
Multiplication by the mass `t` restores the unnormalized integral operator, without changing domains or adjoints when the Hilbert measure is multiplied by the same positive scalar.

There is no use of C_F0049's later global necessity estimate, no assumption of a global angular comparison constant, and no circular appeal to the new conclusion.

## 2. Original marginal graph and actual adjoint

For smooth compactly supported `h` in the selected annulus, the C1 polynomial approximants converge uniformly together with their real first derivatives on a convex square.
The difference of divided differences is bounded by the derivative error.
Consequently the canonical integral outputs converge in L2 for every finite measure, and `h b` for polynomial `b` lies in the original marginal closure with the displayed output.

The split (10) has the correct exterior minus sign.
Both cross terms have uniformly separated kernels because only values on the compact support of `h` survive.
The annular internal estimate and separated cross terms therefore prove (11) with a finite constant independent of `b`.

Uniformly bounded polynomial approximations to bounded measurable `b` exist by bounded continuous approximation for the compact Borel measure and uniform approximation by starred polynomials.
The argument identifies the weak operator-output limit with the original closed graph; it does not choose another extension.

For the actual adjoint, the polynomial formula is `e_0^* b=b xi-J e_0 J b`.
A real cutoff ensures `J(hb)=h overline(b)`.
C1 approximation of `h`, followed by closedness of the actual adjoint, proves (12) for polynomial `b`.
Bounded almost-everywhere polynomial approximation then makes `hb xi` converge strongly by dominated convergence, while (11) controls the other term and its original-graph weak limit.
This proves the actual adjoint inclusion and (13), without asserting that the polynomial core is an adjoint graph core.

## 3. Free-product lifting and both original nonnormalized operators

C_F0045 identifies the entire original starred polynomial algebra with the algebraic direct sum of marginal polynomial cores, using reduced prefixes ending outside the chosen coordinate.
It also proves the actual direct-sum adjoint, not merely a formal adjoint.
The conditional-expectation identity is

`E_(B_j)(p^*p)=sum_u b_u^*b_u`,

so the coefficient column-square norm is at most `||p||^2`.
The prefix vectors are not assumed unitary.

For the new cutoff maps, `T_h b=e(hb)` and `T'_h b=e_0^*(hb)` are bounded complex-linear maps on the commutative algebra `C*(X_j)=C(spectrum(X_j))`.
Thus the exact already accepted complex little Grothendieck inequality applies to the finite family `(b_u)` with squared constant `4/pi`.
No normality, complete boundedness, or identification of its factorization measure with the spectral measure is needed.
The reviewer read the precise source interface in Pis12-U001 and the complete C_F0045 review; no new source theorem is imported by this review.

The finite expansion of `p q_l` has coefficients `b_u q_l`.
C1 convergence of `q_l` to `h` gives strong convergence of all marginal operator outputs and, by the actual adjoint identity, of the marginal adjoint outputs.
On the original polynomial core the two exact corrections are `q eta` and `q eta^*`.
Operator-norm convergence of `p q_l` makes both corrections converge in L2 even when `eta` is a mixed L2 vector.
The two closed graphs therefore give (18) for precisely the original `D_j` and original actual `D_(j,0)^*`.

This step avoids the invalid rule that the closure of a sum of unbounded operators automatically equals the sum of their closures.
The Grothendieck bounds then give both estimates in (19), uniformly over the number and lengths of the reduced words.

Uniformly bounded polynomial approximants to any `a in M` follow from Kaplansky density and norm approximation inside `C*(X)`.
Their norm bounds can approach `||a||`.
The pair of original outputs is bounded in a product Hilbert space.
Weak subsequences and weak closedness of the two original graphs prove the actual-domain claim for `a h`; lower semicontinuity supplies the displayed constants.

## 4. Common module and the exact C_F0029 interface

For each `e_(j,n)`, a real smooth radial cutoff can equal one on every spectral radius at least `1/n` while vanishing near zero.
Therefore `f=f h(X_j)` for `f in M e_(j,n)`, and the already proved `M h(X_j)` result gives assertion A.

The coordinate spectral projections increase to one.
Their finite meets increase too, and finite-trace subadditivity gives (20).
Hence the increasing union `E=union_n M p_n` is linear, a left M-module, and Hilbert-dense.
The order relation `p_n<=e_(j,n)` gives `M p_n subset M e_(j,n)` with the required right support; no commutation of the different coordinate projections is assumed.

Every original generator preserves `Dom D_j` and satisfies its original bounded commutator there by graph approximation from the specified polynomial core.
Restriction to E is legitimate because E is a left M-module.
Also `E subset Dom D_j^* subset Dom (D_j|E)^*`.
Consequently C_F0029 applies with the same dual module E and all adjoint test modules equal to E.
Its fraction calculus yields exactly (7), fraction independence, finite-rank bounded representatives, and full-domain invariance for `closure(D_j|E)`.

The proof correctly retains the latter closure in the final assertion.
Density in H alone does not identify it with D_j.

## 5. Mixed pairings and unresolved original-core bridge

For `p in Dom D_j^*` and `q in E`, (23) gives (24) directly.
For `p in E`, the vectors `p` and `f^*p` both lie in the original adjoint domain.
Pairing (23) against p on the dense module yields

`D_j^*(f^*p)-f^*D_j^*p=-T_j^*p`,

with the sign in (25).
This is an equality of original Hilbert-space values and extends (24) to `E x Dom D_j`.
The text does not pass from either mixed identity to `P x P` by Hilbert density, so no boundary term or adjoint-core issue is hidden.

For the continuation, the reviewer has checked the following **conditional bridge**, which is not proved under the present A/B hypotheses.
It is not part of the registered Yin_C_F0050 statement or selected support; any future mathematical reuse should organize and review it separately.
If the common projections additionally satisfy

`sup_n ||D_j p_n||_2 < infinity` for every j,

then `D_j p_n` converges weakly to `D_j 1`.
Indeed pairing against `Dom D_j^*` proves convergence on a dense set, and the uniform bound extends it to every Hilbert test.
Mazur convex combinations in the finite product Hilbert space give positive contractions `z_n in E` such that `z_n -> 1` and `D_j z_n -> D_j 1` strongly for every j.
For every starred polynomial p, the original bounded commutator gives

`D_j(p z_n)=p D_j z_n+[D_j,p] z_n -> p D_j 1+[D_j,p]1=D_j p`.

Thus E is a graph core for each original D_j, since P already is; C_F0029's full-domain commutator conclusion then implies the original polynomial weak-form converse.
No adjoint graph-core assertion is needed.
More generally, direct vacuum graph approximants in E suffice, even without a projection estimate.

The local constants in (5) may diverge with n.
The present proof supplies neither the displayed uniform bound nor those vacuum graph approximants, and this review does not infer them.
Under normalization, uniformly bounded projection or convex-combination inputs would also control the correction `z_n eta`, since bounded strong convergence to one implies `z_n eta -> eta` in L2.

## 6. Scope of acceptance

Assertions A and B and the stated mixed compatibility pass the analytic review at their exact scope.
General singular angular laws, correlated tuples, the unrestricted original polynomial converse, and bounded scalar rational reconstruction remain outside the conclusion.
Source completeness is accepted for the external inputs actually used, at the recorded statement/applicability depths above.
Internal mathematical review and direct-input checks were performed.
Numerical experiments, manuscript compilation, formal verification, external human review and novelty or priority assessment were not performed and are not needed for this scoped analytic pass.
No theorem Role, Task completion or lifecycle transition, canonical metadata edit, or publication action is assigned by this file.

## Relationship arrangement

The original dated separate/independent wording is retained historically.
Before the A/B review this reviewer investigated and communicated an actual conditional vacuum graph-approximation argument for the same original-closure interface discussed in the target's Section 7; that substantive mathematical bridge and earlier discussion were available in the review context.
This is known target-related development context, not merely a fixed checklist or authorship of an upstream dependency, so the current whole finding is self-reviewed.
The recorded conditional bridge remains a separate unadopted observation and does not resolve the missing graph-core hypothesis.
No independently identified gap was repaired into assertions A/B in this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#6-scope-of-acceptance) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#6-scope-of-acceptance) | [Statement](../../claims/Yin_C_F0050_v1.md#statement) | Whole selected Sections 1–8 assertions A and B plus actual mixed pairings, local original domains and common dense-module affiliated criterion. Original polynomial-core converse and the extra conditional graph-bridge observation are not adopted. |
| [Original finding](#6-scope-of-acceptance) | [Complete selected module](../../claims/Yin_C_F0050_v1.md#annulus-local-dual-domains) | Whole selected Sections 1–8 assertions A and B plus actual mixed pairings, local original domains and common dense-module affiliated criterion. Original polynomial-core converse and the extra conditional graph-bridge observation are not adopted. |
