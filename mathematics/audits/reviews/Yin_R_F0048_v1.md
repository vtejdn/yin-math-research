---
author: Yin
---
# Independent review of normal strong-domain equivalence and canonical compatibility

Review performed and recorded: 2026-10-14T16:36.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and exact scope

The reviewer did not develop, propose or edit [C_F0075 v1](../../claims/Yin_C_F0075_v1.md).
Root assigned the complete fixed candidate dated 2026-10-14T16:31, identified its four conclusions and main domain/quantifier obligations, and disclosed its preparation self-check.
No proof-generation dialogue, separate exploration notes or informal proof explanations were supplied or consulted.
The reviewer had separately reviewed a nonnormal example, which is not an input to this candidate.
The current candidate and the complete four direct C dependencies were read before this review conclusion was formed; their accepted status was treated as inherited mathematical support, not as verification of the new assembly.

This review covers all four statement items and all five proof sections, including supplied operators on potentially larger domains, their actual Hilbert adjoints, universal implications versus pointwise assertions, and the full natural domains and ranks of fraction operators.
It checks the exact interfaces of C_F0070 Parts A-C, C_F0072, C_F0073 Parts A-B, and C_F0031's finite-rank and dense-restriction facts.
The additional Kat95 attribution was checked in its responsible retained citation note; no new original-PDF or recursive foundational source audit is claimed.

The original comparison contract was consulted for conventions and the limits of the result.
This finding reviews the complete candidate and does not resolve the remaining class-wide universal implications.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0075 statement](../../claims/Yin_C_F0075_v1.md#statement) | All four conclusions: arbitrary-tuple adjoint stability of S; normal S iff F and adjoint F; equivalence of the two universal normal implications; supplied/canonical values, actual adjoints and finite-rank full-domain fraction compatibility. |
| [Conclusion](#conclusion) | [C_F0075 argument](../../claims/Yin_C_F0075_v1.md#argument) | All five proof sections, with adjoint signs, both contraction bounds, actual graph restoration, universal quantifiers, right-multiplication adjoint, graph inclusion directions and whole-natural-domain finite-rank transfer. |
| [Conclusion](#conclusion) | [C_F0070](../../claims/Yin_C_F0070_v1.md#statement) | Parts A-C only: unique represented starred derivatives from normal F, bounded right contractions, actual vacuum under the supplied vacuum-adjoint hypothesis, and the canonical right full domain under A and F. No equality with an arbitrary unclosable bare extension on all M is imported. |
| [Conclusion](#conclusion) | [C_F0072](../../claims/Yin_C_F0072_v1.md#statement) | Two separate operator-norm-to-H contraction bounds imply an actual vacuum and both domains of the specified canonical closure; bounds, weak density and represented starred algebra are matched. |
| [Conclusion](#conclusion) | [C_F0073](../../claims/Yin_C_F0073_v1.md#statement) | Part A adjoint stability of A for arbitrary bounded tuples, and Part B equivalence between left-contraction boundedness and F(X*) under normal F(X). Reversal symmetry and freeness are not assumed or used. |
| [Conclusion](#conclusion) | [C_F0031](../../claims/Yin_C_F0031_v1.md#statement) | Densely defined closable finite-rank operators have bounded all-H closures with the identical actual range and rank; the dense-restriction/full-graph argument is also rechecked for the present fractions. |

## Adjoint stability, including the sign and original domains

Fix an index and suppose S(X).
Since M Omega is dense and contained in Dom D*, D is closable and D** extends D.
For a,b in M, pair the relation (X D-D X)a=P a against b.
With the inner product linear in its second variable, the adjoint rule and selfadjointness of P give

\[
\langle D^*X^*b-X^*D^*b,a\rangle
=\langle Pb,a\rangle.
\]

The first composition is defined because X*b is bounded and belongs to Dom D*, and the second because left multiplication by X* is bounded on all H.
Density of M Omega gives [D*,X*]b=P b.
Therefore D'=-D* has [X*,D']=P on M Omega.
Its domain contains M Omega, and (D')*=-D** has a domain containing Dom D and hence M Omega.
This verifies S(X*) for the actual operators, without changing the originally supplied domains or assuming normality.
Repeating the argument for X* yields the reverse implication.
Restricting these systems to M gives both F(X) and F(X*).

## Both bare conditions recover S for normal tuples

Under normal F(X), C_F0070 Part A supplies the unique represented starred derivations delta_i and the right-contraction bound on A_X*.
The same input applies to X*, which is again a bounded normal generating tuple of the same algebra.
C_F0073 Part B identifies the normalized right contraction of the conjugate derivation as J L_i J.
The involution J preserves the L2 norm and the operator norm on bounded elements, so the right bound for X* gives the required left-contraction bound for delta_i.
It is not inferred from the right bound for X alone.

The algebra A_X* is unital, closed under adjoints and weakly dense because X generates M.
These are precisely the algebraic premises of C_F0072.
Applied coordinatewise with the two available bounds, that result proves actual vacuum adjoints and puts M Omega in both Dom E_i and Dom E_i*, where E_i is the closure of the specified core right contraction.
Thus no closability or vacuum condition on the original bare maps was added silently.

The generator commutator extends from the core to this closure by graph approximation.
In detail, for v in Dom E_i choose core v_n with v_n tending to v and E_i v_n tending to E_i v.
The core identity gives

\[
E_i X_jv_n=X_jE_i v_n+\delta_{ij}P v_n.
\]

The right side converges in H, while X_j v_n tends to X_j v.
Closedness therefore puts X_j v in Dom E_i and gives the identity at v.
This argument needs only bounded X_j and P and the definition of E_i as the core closure.
In particular it applies on M Omega.
Taking D_i=-E_i proves S(X) with the generator-first sign and both actual full domains.

Together with the preceding section this proves item 2.
The formulation using both bounded contractions is the same condition under normal F(X), by the exact C_F0073 equivalence.
Nothing in this argument identifies an arbitrary bare full-domain extension with the canonical closure on all M.

## Universal implication versus a fixed tuple

For every bounded tuple, C_F0073 Part A transforms delta into delta-sharp(a)=(delta(a*)) dagger, where (u tensor v) dagger=v* tensor u*.
The two conjugate-linear operations give a complex-linear outer derivation, normalized on the adjoint tuple.
Its actual vacuum vector is the tracial involution of the original one, so A(X) iff A(X*) with the same generated algebra.
This source interface introduces neither normality nor an additional reality hypothesis.

Now assume the single universal statement that A(Y) implies F(Y) for every bounded normal generating tuple Y.
For a normal X with A(X), apply that statement once to X and separately to X*.
Both applications are legitimate because X* is normal and satisfies A.
Item 2 then yields S(X).
The converse universal implication follows pointwise from S implies F.

The counterexample reduction has exactly the claimed quantifiers: a normal A-but-not-S tuple has not(F(X) and F(X*)); choose the failing tuple among X and X*.
It still satisfies A.
Conversely not F implies not S.
This is not an argument from just A(X) and F(X) at one chosen tuple to S(X).
In particular it does not establish the unresolved general adjoint stability of F.

## Canonical values and actual adjoints for a supplied strong system

Fix a supplied S system and put eta=D Omega.
Restriction to M supplies normal F(X), while Omega in Dom D* gives A(X) and the actual vacuum -D* Omega+eta* by C_F0070 Part C.
Uniqueness in its Part A identifies these derivatives with any other normalized starred derivatives on the represented algebra.
Thus there is a well-defined canonical core operator E_0 for this comparison.

Consider N(a)=a eta on the dense domain M Omega.
For bounded a,b, both eta*a*b and a*b eta* are in L1 (in fact in L2), so traciality applies and gives

\[
\langle N a,b\rangle
=\tau(\eta^*a^*b)=\tau(a^*b\eta^*)
=\langle a,b\eta^*\rangle.
\]

For each fixed b, the last expression is bounded in the H norm of a.
Therefore b is in the actual Dom N*, and N*b=b eta*.
This does not require eta to be bounded and does not replace right multiplication by left multiplication.

Define Efull=-D|_M+N on M Omega.
For every b in M, the original D* b exists, and the same pairing proves

\[
b\in\operatorname{Dom}(Efull)^*,\qquad
(Efull)^*b=-D^*b+b\eta^*.
\]

Its adjoint domain is dense, so Efull is closable.
C_F0070 identifies E_0 with Efull restricted to the entire starred core.
C_F0070 Part B also puts all M Omega in Dom Ecan, where Ecan=closure(E_0), because both A(X) and F(X) have now been verified.

The graph inclusions have the correct directions:

\[
Ecan\subseteq\overline{Efull},\qquad
(Efull)^*\subseteq Ecan^*.
\]

At a in M, Efull(a) already equals the value of its own closure.
Ecan(a) is defined and lies in that same single-valued graph, so Ecan(a)=Efull(a).
At b in M, the adjoint inclusion gives the value Ecan*b=(Efull)*b, as well as actual membership in Dom Ecan*.
Negating Ecan gives exactly

\[
\widehat D(a)=D(a)-a\eta,\qquad
\widehat D^*(a)=D^*(a)-a\eta^*.
\]

This argument legitimately strengthens the supplied-map comparison using S's actual adjoint domains.
It does not infer agreement on M merely from Hilbert density of the starred core, and it does not assert that M is a graph core for the original larger-domain D.

## Fraction operators on their full natural domains

Fix any index and any Q=(s,a,b,t) with bounded coefficients and regular s,t representing one affiliated u.
The affiliated equalities imply sb=at; since these are bounded elements, this is also an equality of bounded operators on H.
Both fraction operators have natural domains containing the dense M Omega.
The canonical value formula therefore yields, for z in M,

\[
(sDb-aDt)z-(s\widehat D b-a\widehat D t)z
=(sb-at)z\eta=0.
\]

The individual natural domains are not replaced by M in the finite-rank assertion.
For any w in M and any v in the full natural domain of the supplied fraction operator G, the adjoint identity is

\[
\langle w,Gv\rangle
=\langle b^*D^*(s^*w)-t^*D^*(a^*w),v\rangle.
\]

All four adjoint inputs are legitimate: s*w and a*w are bounded and lie in Dom D*, while the remaining multipliers are bounded on H.
Hence M Omega is contained in Dom G*, even when v is not a bounded vector.
The same proof applies to the canonical operator using its just-established adjoint full domain.
Both fraction operators are therefore densely defined and closable on their actual natural domains.

Suppose either full natural-domain fraction has finite rank.
C_F0031 gives its bounded, everywhere-defined finite-rank closure T with unchanged range.
The other fraction agrees with T on M Omega.
Given any v in H, choose z_n in M Omega tending to v.
Then Tz_n tends to Tv, so the graph of T is contained in the closure of the other fraction's graph.
That closure is an operator because closability was proved.
Since T already has domain H, graph inclusion forces equality with T, not just an extension relation on a smaller domain.

The image T(M Omega) is dense in the finite-dimensional Ran T and is a linear subspace, hence equals Ran T.
The other original fraction operator contains that restriction and is contained in T.
Its full-domain range must therefore also equal Ran T.
This proves identical ranks, including zero rank, and the same bounded finite-rank closure in both directions.
No graph-core assumption for M, equality of the two natural domains, or equality of the operators associated to different fraction pairs is used.

## Dependency and source boundaries

The complete four fixed C inputs and their current selected assessments were read.
Their statements supply exactly the interfaces above.
C_F0072 and the relevant C_F0073 reductions rely on C_F0070, while C_F0070 does not rely on this new candidate; the assembly is acyclic.
The proof never imports C_F0073's additional reversal symmetry or freely independent special case.

The finite-rank assertion is supplied by C_F0031's complete elementary Hilbert-space proof, which was also rechecked: density of the adjoint domain and finite-dimensional projection give bounded coordinate functionals, hence a bounded extension; density and closedness of the finite-dimensional range preserve the actual range.
The [Kat95 selected source check](../literature/Kat95/Yin_U001.md#selected-citation-check) identifies Problem III.5.18 as a boundedness problem statement on printed p.166 / PDF p.189 and the extension passage in III.2.2 on printed p.145 / PDF p.168.
Its stronger all-H/range consequences are stated as elementary applicability deductions.
That source attribution does not act as a fifth unverified mathematical dependency or claim that the inspected problem includes a proof.
The retained source-reading limits remain unchanged.

The accepted inputs' foundational source proofs are not recursively re-audited here.
This finding records an independent check of the new complete assembly and its actual interfaces.
It is neither a numerical nor a proof-assistant verification and makes no priority claim.

## Conclusion

All four statements and all five argument sections of C_F0075 v1 pass this independently organized review with no required mathematical correction.
The exact dependency and source interfaces are adequate at their recorded scopes.
The result supports proved / independently reviewed for this fixed candidate if adopted by its responsible Claim decision.

The result establishes adjoint stability of S, the normal equivalence S(X) iff F(X) and F(X*), the equivalence of the two class-wide normal A-to-S and A-to-F questions, and the claimed canonical values and finite-rank fraction compatibility for every supplied strong system.
It does not decide whether either universal A implication holds, prove pointwise A plus F implies S without the adjoint-tuple condition, or establish equality of unclosed fraction operators with different domains.
