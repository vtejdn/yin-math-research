---
author: Yin
---
# Independent review of arbitrary-tuple relative maximal Delta

Review performed and recorded: 2026-10-14T09:16.
Human record author: Yin.
The reviewer was a separately assigned AI agent; this is not a personal human review.

## Arrangement, inputs and scope

This is a separately organized initial whole-proof review of [C_F0177 v1](../../claims/Yin_C_F0177_v1.md), dated 2026-10-14, Definitions, Statement, Argument and Source relationship.
The reviewer did not develop, edit, or advise on this relative-Delta proof.
Before this assignment the reviewer worked on the different ACSY24 canonical-domain question.
Shared conversation context included the earlier informal relative-Delta idea and source pointers; the completed author's C_F0177 and CS05-U001 were supplied for review.
This is disclosed shared context, not a blind review.
No previous review verdict was used.

The reviewer first enumerated the obligations from the claimed arbitrary-tuple statement, rechecked the full argument and each displayed formula, and then compared the precise source passages.
The inspected author-hosted CS05 artifact has 39 pages: Lemma 2.16 on p.18, the self-adjoint-set convention on p.19, equations (3.9), (3.11)--(3.13) on p.22, and Theorem 4.11 with its complete proof on p.33.
The retained published MSY23 PDF was read at pp.12--13 and 47--48.
Standard finite von Neumann module dimension, Hilbert-space projection identities, Schatten ideal properties and the locally convex annihilator theorem are accepted functional-analytic foundations; their use and applicability were checked, without auditing all foundational proofs.

## Current relationship clarification

The original dated independent wording is preserved as its historical description.
The reviewer reports no development, editing or advice on this proof and formed the complete initial finding before any previous verdict.
However the shared conversation already included an earlier informal relative-Delta idea.
The retained description does not identify that idea's actual mathematical content sufficiently to establish whether it was only the fixed target/dependency input or additional substantive development about this proof.
The current whole-finding relationship is therefore unknown, not inferred self from the word idea and not inferred independent from the separate assignment.
No reviewer-supplied mathematical repair is recorded.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0177 definitions](../../claims/Yin_C_F0177_v1.md#definitions) | Ambient finite algebra, standard module convention, ordered arbitrary tuples, cycle closures and relative intersection, including closure before intersection. |
| [Conclusion](#conclusion) | [C_F0177 statement](../../claims/Yin_C_F0177_v1.md#statement) | Exact bounded-dual and Hilbert-Schmidt side-commutator hypotheses, maximal relative and absolute conclusions, no normality or generation assumption. |
| [Conclusion](#conclusion) | [C_F0177 argument](../../claims/Yin_C_F0177_v1.md#argument) | Complete displayed formulas (6)--(12), WOT annihilator conversion, Hermitian adjoint correction, coordinate projection, rank-one density and trace-preserving dimension switch. |
| [Conclusion](#conclusion) | [C_F0177 source relationship](../../claims/Yin_C_F0177_v1.md#source-relationship) | Exact relationship to CS05 and MSY23, inspected source locators, sign conventions and bounded literature-comparison limits. |
| [Conclusion](#conclusion) | [CS05-U001](../literature/CS05/Yin_U001.md#cs05-u001) | Exact source hypotheses, relative construction and proof mechanism verified against the author PDF; general absolute comparison verified against MSY23. Search reports assessed as bounded provenance, not exhaustive literature evidence. |

## Definitions and module obligations

The standard-module identification is correct.
On algebraic tensors, the map `a tensor b^op -> a P_Omega b` preserves the trace inner product, since the squared norm is `||a||2^2 ||b||2^2` and polarization gives the cross terms.
The action `(c tensor d^op)T=cTd` corresponds to left multiplication in `M tensor M^op`.
Rank-one operators with vectors from `M Omega` are HS dense.
Consequently the completion is the standard module for `N=M bar_tensor M^op` and has dimension one.

The cycle subspace is invariant under every left and right M multiplier: these commute with the right multiplication operators rho(Z_j).
Its HS closure therefore reduces the represented algebraic tensor *-algebra and its von Neumann closure N.
All dimensions in (1)--(3) are thus dimensions of well-defined closed N-submodules.
The relative definition keeps the HS closure before intersection with the initial-coordinate submodule E.
The inclusion `K_X direct_sum 0 subset K_(X,Y) intersect E` gives the inequalities in (3) with the stated direction.
Empty Y recovers the absolute quantity.
Ordered tuples allow repetitions or linear dependencies; the definition remains meaningful, though the dual hypotheses then impose their own restrictions.
No generating assumption is used for these definitions.

CS05 (3.9) has precisely the same closure/intersection order.
The original source's self-adjoint-set condition means closure under adjoints, not that every displayed member is individually selfadjoint.
MSY23 pp.12--13 has the general absolute cycle definition with `J X_j* J`, agreeing with rho in C_F0177.

## Annihilator, adjoints and projection

For finite-rank T and bounded B,A, trace cyclicity gives `Tr(T[B,A])=-Tr([T,A]B)`.
All terms are trace class.
The WOT continuous dual consists of finite-rank trace functionals, so the WOT closed commutator range is exactly the bilinear annihilator of finite-rank cycles.
Passing from finite-rank cycles to their HS closure is justified by `|Tr(TV)|<=||T||2 ||V||2` for HS T,V.
The WOT closed range intersected with HS is HS closed because HS norm convergence implies WOT convergence.

The adjoint is essential.
Componentwise adjoint sends K_Z to K_(Z*) because `[T,rho(Z)]*=-[T*,rho(Z*)]`.
With the explicitly chosen HS inner product linear in its first argument, `Tr(TV)=<V,T*>_2`.
Thus the bilinear annihilator is `K_(Z*)^perp`, and equivalently `V_(Z*)=K_Z^perp`, exactly (7).
The proof does not assert the generally unjustified identity `V_Z=K_Z^perp`.

The coordinate projection formula (9) is correct for every closed subspace K: the orthogonal complement in E of `pi_X(K^perp)` is exactly `K intersect E`.
Taking the Hilbert closure of the projected range is necessary and is explicitly done.
Dimension additivity in the finite standard module then gives (10).
Neither a closed-range hypothesis nor a commutation between projection and closure was assumed.

## Dual implementation and maximality

For the generator-first convention `[X_j,D_i]=delta_ij P`, the bounded operator `B_i=-J D_i J` satisfies

`[B_i,rho(X_j*)]=J[X_j,D_i]J`,
`[B_i,rho(Y_k*)]=J[Y_k,D_i]J`.

Conjugation by J is conjugate-linear but multiplicative on products of bounded operators; the displayed minus sign and the use of the adjointed tuple therefore agree.
The side commutators remain HS.
Multiplication of B_i on both sides by a,b in M leaves the commutator calculation valid because a and b commute with all right multipliers.
The projection consequently contains every tuple with `a P b` in its i-th coordinate and zero elsewhere.
Varying i,a,b gives an HS-dense spanning set of the entire first-coordinate module.
Formula (10) yields relative dimension d, and (3) then yields absolute dimension d.
This proves the complete statement without normality, adjoint closure, or generation.

## Unstarred numerical formula and source scope

The final numerical formula (12) is valid even though the corresponding subspaces need not coincide.
The antiunitary A:T->T* commutes with coordinate projection and exchanges V_Z and V_(Z*), since `[B,rho(Z)]*=-[B*,rho(Z*)]` and adjoint is WOT continuous.
It intertwines the standard N action by the conjugate-linear multiplicative switch `a tensor b^op -> b* tensor (a*)^op`.

For completeness, its dimension-preserving assertion can be checked directly on projections, rather than inferred from antiunitarity alone.
Under the standard-module identification, A fixes the trace vector P_Omega.
If q is a projection in the commutant, the projection onto the transformed submodule is A q A.
Its canonical trace is `<A q A P,P>=conjugate(<qP,P>)=<qP,P>`, since projection traces are real.
In a matrix amplification sum this identity over the diagonal entries, or over the coordinate trace vectors; A fixes each such vector.
Therefore the corresponding submodules have equal N-dimension.
This verifies the dimension switch invoked in (12).

The checked CS05 passages support the relative construction, annihilator mechanism and bounded-dual rank-one argument.
The local proof removes the source's self-adjoint-family and generation hypotheses by explicitly verifying the arbitrary-tuple module interfaces.
MSY23 Proposition 6.2 supplies exactly the already published arbitrary-tuple absolute statement, with the same generator-first convention.
These uses are correctly separated from a claim that either source states the whole general relative result verbatim.

The audit does not certify exhaustive literature coverage or priority.
CS05-U001's negative search finding is explicitly bounded and is treated as such.
The reviewer independently verified the exact mathematical source passages and applicability, but did not repeat every public search query recorded by the author.
The self-contained proof has no unresolved source-dependent mathematical step.

## Conclusion

The complete C_F0177 v1 definitions, statement, argument and source relationship pass this independently organized review.
No mathematical correction is required.
The result supports a proved / independently reviewed assessment for precisely this fixed statement and argument if the coordinating author adopts this finding.
In particular, the review covers the additional unstarred numerical dimension formula, not merely the maximality statement.

This review does not settle either general implication between the ACSY24 condition and the existence of full-domain duals, does not review a manuscript revision, and makes no task-completion, novelty, formal-verification or layout claim.
The earlier shared-context exploration remains outside these bindings.
