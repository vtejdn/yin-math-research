---
author: Yin
---
# Independent whole-proof review of coordinate-local paired quadratic identities

Review performed and recorded: 2026-10-16T03:20.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and exact scope

This is an initial independent review of the complete fixed [C_F0158 v2](../../claims/Yin_C_F0158_v2.md#statement), including its positive-square identities and finite-family conclusion.
The reviewer did not develop either version and did not edit the Claim.
The assignment supplied the fixed candidate and intended review obligations, and stated that exploration notes and proof-generation dialogue had not been supplied.
No such notes, author-development dialogue, auxiliary draft or informal explanation was consulted.
The development account inside the Claim was read as part of the artifact and was not used as correctness evidence.
The v1 proof was not consulted and supplies no evidence for this review.

The reviewer first read the v2 statement and argument, enumerated its obligations, and independently recalculated the identities below.
The exact interfaces of C_F0076 Part 1, C_F0043 Section 3, Mai15-U003 and the mixed-coordinate passage of C_F0071 v2 were read before the conclusion was formed.
After the initial mathematical checks, the selected C_F0076 decision and the arrangement and first-section evidence of its R_F0049 review were read to confirm the existing accepted-input boundary.
No earlier review conclusion for C_F0158 was consulted.

The reviewed artifact is the working-copy physical v2 whose initial decision is dated 2026-10-16T03:11, as inspected on 2026-10-16T03:20.
It was uncommitted when inspected; repository HEAD was 1b0009e237e11d309456540e58d828f2e2156e25, which does not identify the new Claim bytes.
The starting assessment was proof draft with self-reviewed review status.
The whole statement and argument are covered, including arbitrary elements of the represented mixed starred core and arbitrary finite families.
No manuscript, Task completion or unrestricted normal-tuple implication from A to S is reviewed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0158 v2 statement](../../claims/Yin_C_F0158_v2.md#statement) | Entire coordinate-local statement: actual one-sided adjoints, S1-S3 identities, exact constant S4, finite-family S5-S6 and all scope restrictions. |
| [Conclusion](#conclusion) | [C_F0158 v2 argument](../../claims/Yin_C_F0158_v2.md#argument) | Entire argument: other starred-generator vanishing, actual domains, real twist, defect energy, original-adjoint transport, positive square, opposite algebra, constant and finite sums. |
| [Conclusion](#conclusion) | [C_F0076 Part 1](../../claims/Yin_C_F0076_v1.md#statement) | Full normal ACSY hypotheses imply zero derivative at every other starred generator and elementary-tensor adjoint domains; no Part 2-3 conclusion is imported. |
| [Conclusion](#conclusion) | [C_F0076 first argument section](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Differentiated normality, coarse-space injectivity and actual tensor-adjoint interface at their used scope, with the existing accepted source premises. |
| [Conclusion](#conclusion) | [C_F0043 Section 3](../../claims/Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Equations 6-13: real inner twist, actual vacuum and core adjoint, exact first-order defect and energy; the zero-derivative extension to arbitrary other normal coordinates was independently checked. |
| [Conclusion](#conclusion) | [Mai15-U003](../literature/Mai15/Yin_U002.md#mai15-u002) | Real, algebraic-range, coassociative actual-vacuum hypotheses and the exact quadratic identity for arbitrary core elements, with corrected L2 codomain and right aa* orientation. |
| [Conclusion](#conclusion) | [C_F0071 v2 mixed-coordinate passage](../../claims/Yin_C_F0071_v2.md#reverse-implication-for-mixed-selfadjointunitary-tuples) | Existing zero-derivative mixed-coordinate adjoint and defect calculation, checked as an interface comparison; arbitrary-normal applicability additionally uses C_F0076. |

## Hypotheses and actual domains

The full ACSY premise is imposed on the represented full starred algebra of the entire normal generating tuple.
Consequently C_F0076 Part 1 applies to every other normal coordinate.
Its proof uses the full premise to exclude atomic marginals, differentiates normality, and uses injectivity of the coarse difference operator to force off-coordinate starred derivatives to vanish.
This deduction does not weaken that premise to existence of a single distinguished derivation with uncontrolled other starred derivatives.
The actual tensor-adjoint conclusion places every elementary core tensor in Dom(delta*), so both one-sided maps are actual Hilbert adjoints throughout the stated core.

At a selfadjoint distinguished coordinate, the derivative agrees with the reversed tensor involution on every starred generator and is therefore real.
At a unitary coordinate the inverse product rule gives delta(U*)=-U* tensor U*.
Together with the off-coordinate zero values, finite Leibniz expansion gives algebraic tensor range on the whole mixed core.
Neither freeness nor a spectral restriction on the other coordinates is introduced.
The inner multiplier for beta commutes with the outer actions and is unitary on the Hilbert tensor space.
Its actual adjoint uses delta* at U* tensor 1, whose domain membership has already been established.

For positive b in the core, delta(X_i)=1 tensor 1 gives
\[
 \langle X_i,T_\ell(b)\rangle
 =\langle1\otimes1,b\otimes1\rangle
 =\tau(b)
 =\langle X_i,T_r(b)\rangle.
\]
This verifies Q2 and, for unitary X_i, Q3 with unit constant.
No bounded H-to-H extension is used.

## Real twist and defect energy

The formulas beta(U)=i U tensor 1 and beta(U*)=-i 1 tensor U*, with zero on every other starred generator, prove reality on the whole algebra.
The algebraic range makes both iterated algebraic derivatives defined there.
The difference of the iterates is a derivation into the outer triple module because its mixed Leibniz terms cancel.
On U it equals -U tensor 1 tensor 1; on U* it equals 1 tensor 1 tensor U*; on every other starred generator it is zero.
These are exactly the values of i kappa beta, verifying Q6 without an additional hypothesis on the other coordinates.

The actual tensor-adjoint formula gives
\[
 T_\ell(U^*)=U^*\xi-1,\qquad
 \zeta=-\mathrm iT_\ell(U^*)=\mathrm i(1-U^*\xi).
\]
Reality makes zeta selfadjoint and the pairing with beta(1)=0 gives tau(zeta)=0.
For B=(id tensor tau) beta, the same formula gives B*(q)=q zeta-Bq on the whole core.
In particular Bq is a bounded core element, so using the actual adjoint at Bq in the energy calculation is justified.
No derivative of zeta or B*(q) is taken.

Put b=q*q and T_beta=B* on the core.
Taking real parts in C_F0043 equation 13 and expanding the adjoint square gives
\[
 \|T_\beta(q)\|_2^2
 =\|q\zeta\|_2^2
  -\operatorname{Re}\langle\beta(b),1\otimes\zeta\rangle
  -\operatorname{Re}\langle\mathrm iBq,q\rangle.
\]
Since b and zeta are selfadjoint and beta is real, the real part of the middle pairing equals the real part of the pairing against zeta tensor 1.
The first two terms are therefore Re<T_beta(b),zeta>.
Also Re<i q zeta,q>=0 because tau(zeta q*q) is real.
Substitution of Bq=q zeta-T_beta(q) changes the last term to plus Re<i T_beta(q),q>.
This independently verifies Q8 and its sign with inner products linear in the second variable.
All products of an L2 vacuum have bounded coefficients.

## Actual transport, positive square and opposite algebra

The identity Bq=i(Eq)U, where E=(id tensor tau)delta, gives E=-i rho(U*)B on the same dense core.
Right multiplication by U is unitary and preserves that core.
Taking actual adjoints gives T_ell(a)=i B*(aU).

The product rule gives [B,U]=i U P_Omega, with left multiplication by U.
Its actual adjoint pairing on core vectors gives
\[
 [B^*,U^*]=\mathrm iP_\Omega U^*.
\]
For b=a*a this implies
\[
 B^*(U^*bU)=-\mathrm iU^*T_\ell(b)+\mathrm i\tau(b)1.
\]
The scalar term pairs to zero with zeta.
Apply Q8 to q=aU and use i U zeta=xi-U, respecting the inner-product convention, to obtain
\[
 \|T_\ell(a)\|_2^2
 =\operatorname{Re}\langle T_\ell(b),\xi-U\rangle
  +\operatorname{Re}\langle T_\ell(a),aU\rangle.
\]
Q2 gives Re<T_ell(b),U>=tau(b)=||a||2 squared.
Expansion of the residual norm now gives exactly S2.
No defect sign is discarded.

For the opposite algebra, delta_op=flip delta is an outer derivation with the same actual vacuum xi.
The linear Hilbert-tensor flip is unitary, fixes 1 tensor 1, and sends a tensor 1 to 1 tensor a.
Thus its actual left one-sided adjoint is the original T_r.
The opposite products a* times a and a times U are the original aa* and Ua.
Its twist vacuum is i(1-xi U*)=U zeta U*, which is selfadjoint, and its completing vector remains the same Hilbert vector 2xi-U.
The left proof therefore gives exactly S3, with its stated right product order.
No reality assumption on the original unitary derivation is used.

## Selfadjoint identity, constant and finite families

For a selfadjoint distinguished coordinate, the generator check gives reality, algebraic tensor range and zero coassociativity defect on the full mixed core.
The core is weakly dense because the tuple generates M, and the vacuum and elementary adjoint domains are actual.
These are exactly the Mai15-U003 hypotheses for its arbitrary-element identity with L2-valued adjoint.
Changing the source's inner-product convention leaves the real-part identity unchanged.
The selfadjoint vacuum and T_r(a)=T_ell(a*)* then give the right aa* identity by traciality.
No theorem for a general nonreal or merely completed-tensor-valued derivation has been substituted.

The actual vacuum pairing gives <xi,U>=1 and ||U||2=1.
Therefore
\[
 \|2\xi-U\|_2^2=4\|\xi\|_2^2-3,\qquad
 \|\zeta\|_2^2=\|1-U^*\xi\|_2^2=\|\xi\|_2^2-1.
\]
The constant in S4 is real and at least one, including zeta=0.
The square of the earlier sufficient constant minus its square is 4||zeta||2, so the stated improvement is correct.
No general optimality is inferred.

Finite summation uses only actual core values and complex linearity.
The common vector v is unchanged as the family varies.
The differences in the first unitary inequalities are exactly the stated sums of residual squared norms; the selfadjoint first inequalities are equalities.
Cauchy-Schwarz with C=||v||2 gives S5-S6 for every positive integer n, including zero entries and n=1.
No infinite-family passage, matrix ampliation, minimax step or new domain assertion occurs.

## Dependency and source boundary

C_F0076 is already proved and independently reviewed at its selected decision.
Its Part 1 hypotheses and used mechanism were checked here; its original ACSY24 and MSY23 premises remain accepted inputs at their recorded scope.
This is not a new audit of those external papers or of C_F0076 Parts 2-3.
C_F0043 equations 6-13 and the corresponding C_F0071 v2 passage were recalculated directly.
The later analytic approximation, curve transfer and all-M graph arguments in C_F0043 are unused.

The complete Mai15-U003 unit was read, including the algebraic-range requirement, corrected L2 codomain, exact identity, convention and separate stronger vacuum-regularity hypotheses.
Its retained source identification and inspection supply the accepted external interface.
The primary Mai15 PDF was not reopened, and its original proof is not claimed to have received a new independent source audit.
The project adaptation and hypothesis match were independently checked.
No missing mathematical input or source-applicability correction was found in this scope.
This is not an exhaustive novelty or historical-priority search.

## Conclusion

The entire fixed C_F0158 v2 statement is supported by its complete argument and the resolved inputs at the scopes above.
No mathematical correction is required for S1-S6, their actual domains or coordinate-local quantifiers.
This independent whole-proof finding supports adoption as proved with independently reviewed review status for exactly this physical version.
The Claim's own selected decision must make that adoption; this R does not change any C, T, S or E decision.

The conclusion concerns a distinguished selfadjoint or unitary coordinate of an arbitrary normal tuple satisfying the full ACSY premise.
It gives no paired-estimate assertion for another unrestricted normal coordinate and does not complete the unrestricted A-implies-S problem.
It supplies no proof-assistant formalization, external human peer review, manuscript assessment or Task-completion audit.
