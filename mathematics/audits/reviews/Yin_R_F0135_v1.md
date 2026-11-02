---
author: Yin
---
# Independent review of atomic dense-core dual counterexamples

Review recorded: 2026-10-14T12:15.
Human record author: Yin.
The reviewer was a separately assigned AI agent; no personal human inspection is asserted.

## Arrangement, inputs and scope

This separately organized review covers the complete [C_F0128 v2 statement](../../claims/Yin_C_F0128_v2.md#statement) and [argument, Sections 2--6](../../claims/Yin_C_F0128_v2.md#argument), including source applicability and the supplementary selfadjoint comparison.
The initial fixed [v1](../../claims/Yin_C_F0128_v1.md#argument) was also inspected; its supplementary scope omission is retained below.

Before receiving the completed proof, the reviewer received the proposed disk-plus-atom formulas and requested properties, then independently enumerated the obligations and calculated the commutators, distribution coefficients, actual adjoint pairings, density and atomic obstruction.
These calculations and suggestions were communicated during preparation.
An alternative sequence for a different interval model was suggested but was not adopted; the author's final interval model and sequence were independently checked.
The reviewer also communicated the starred-commutator formula.
This is disclosed preliminary review feedback, not a blind review or a claim of independent invention of the construction.
No earlier review verdict of these counterexamples was supplied or relied on.

The complete draft, fixed v1, and actual v1-to-v2 changes were read.
The v2 correction was checked at its changed interface; the unchanged construction was already checked in full.
The reviewer did not edit either Claim.
The check of the full-domain premise was limited to its stated linear-map and commutator assumptions; it did not review a proof of the maximality implication.

## Current relationship clarification

The original dated independent wording is retained as the historical description.
The actual arrangement includes the reviewer's calculations and mathematical suggestions communicated during preparation, before receiving the complete proof, including the starred-commutator formula used in the written comparison.
Thus the reviewer participated in this target's substantive development, and neither current finding is classified as isolated independent coverage.
The unadopted alternative interval sequence is not used as a reason for this classification.
The v1 finding identified a genuine missing density hypothesis in the supplementary selfadjoint restriction argument; v2 restores the generating scope and the same reviewer checked that repair.
The two complete counterexamples themselves were unchanged.
The preparation feedback and this same agent's recheck do not provide isolated independent coverage of the repaired Section 5 density/regularization chain.
The later [R_F0179 whole-v2 finding](Yin_R_F0179_v1.md#conclusion) supplies that repaired-chain coverage at its stated scope, as selected by [C_F0128 v2](../../claims/Yin_C_F0128_v2.md#decision-isolated-whole-review-adoption).
The original v1 and v2 findings here retain their dates and self-reviewed relationships.
No new mathematical error in either counterexample is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Initial v1 scope finding](#initial-v1-scope-finding) | self-reviewed |
| [Conclusion for v2](#conclusion) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Initial v1 scope finding](#initial-v1-scope-finding) | [C_F0128 v1 argument](../../claims/Yin_C_F0128_v1.md#argument) | Section 5's selfadjoint comparison: the polynomial restriction needs density, and generation was not explicitly assumed there. No whole-v1 pass is asserted. |
| [Conclusion for v2](#conclusion) | [C_F0128 v2 statement](../../claims/Yin_C_F0128_v2.md#statement) | Both existence statements, exact domains, normalization, commutators, adjoints, closability or its failure, nonmaximal Delta and impossibility of any full-domain replacement in the normal example. |
| [Conclusion for v2](#conclusion) | [C_F0128 v2 argument](../../claims/Yin_C_F0128_v2.md#argument) | Complete Sections 2--6, including all displayed calculations, source interfaces, four small-domain implications and the corrected generating scope of the selfadjoint comparison. |
| [Conclusion for v2](#conclusion) | [MSY23-U002](../literature/MSY23/Yin_U002.md#msy23-u002) | Accepted finite-rank-cycle characterization, left/right convention and applicability to a bounded normal single generator; not a new whole-source audit. |
| [Conclusion for v2](#conclusion) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Section 3's bounded starred-commutator regularization, exact core/closure interface and its use in Sections 4.7 and 5. |
| [Conclusion for v2](#conclusion) | [C_F0003 disk calculation](../../claims/Yin_C_F0003_v1.md#counterexample-normal-multiplication-on-the-disk) | Kernel sign, normalized area, Schur bound and vacuum transform reused and directly recalculated in the new proof. |
| [Conclusion for v2](#conclusion) | [Bla06-U001](../literature/Bla06/Yin_U001.md#bla06-u001) | Dense actual adjoint domain implies closability, and the closure has the same adjoint. |

## Initial v1 scope finding

The two counterexample constructions in v1 passed the mathematical checks below.
Its separate Section 5 comparison, however, said only "selfadjoint tuples" before restricting a dual from an arbitrary dense invariant domain to the polynomial domain and invoking a result requiring a dense polynomial core.
Without generation, that polynomial domain need not be dense in the ambient H.
Thus this particular restriction argument lacked an explicit hypothesis at that interface.
This finding did not refute either counterexample or show that the broader selfadjoint conclusion is false.

V2 expressly restricts that comparison to selfadjoint generating tuples with M=W*(X), and states that generation supplies polynomial density.
A common invariant domain containing the vacuum contains every polynomial vector.
Its restriction is closable by graph containment; generation makes that restriction densely defined.
Since each generator equals its adjoint, both kinds of generator commutator are bounded rank-one operators.
The cited regularization therefore applies at exactly the corrected scope.
The v1 finding is resolved in v2 without altering either counterexample.

## Representation, density and the selfadjoint example

Both measures have total mass one, so the displayed half-weighted direct sums are the actual standard Hilbert spaces and the vacuum has norm one.
The coordinate functions generate their respective measurable algebras; the atom is a spectral projection.
A represented polynomial cannot vanish without being the zero polynomial, since the continuous component has interval or disk support.
In the disk case the invertible linear change between real coordinates and z,bar z justifies using independent polynomial symbols and makes all derivative evaluations well-defined.

For the interval model, extension across the gap followed by polynomial approximation gives density in continuous functions on K and hence in L2(mu).
For the disk model, the unital selfadjoint polynomial algebra separates points of the compact closed disk, so Stone-Weierstrass applies.
The finite Borel measure may have an atom; density of continuous functions in its L2 space still holds.
Both domains contain the vacuum and have the stated coordinate invariance.

The polynomial divided difference includes the atomic diagonal.
The identity Q_(tp)(x,y)=x Q_p(x,y)+p(y) gives the required generator-first commutator and D1=0 with the displayed signs.
The sequence p_n(t)=t(1-t/2)^n has p_n(0)=0, p_n'(0)=1, and both p_n and p_n' tend uniformly to zero on [1,2].
Consequently p_n tends to zero in H, the atomic output tends to -1/2, and the continuous output tends uniformly to zero.
Thus Dp_n tends to -eOmega/2, which is nonzero.
This is an actual failure of closability, not merely an unboundedness test.
Its vacuum pairing tends to -1/4, independently proving that the vacuum is outside Dom D*.

## Cauchy operator and exact dual relation

The row and column integrals of the absolute kernel are at most 4.
Weighted Cauchy-Schwarz therefore proves the stated L2 bound with norm at most 4 and justifies the Fubini calculations for polynomial inputs.
The polar integral gives C1=bar z.
Swapping the two integration variables gives the minus sign in integral(Cp)=-integral(bar z p).
No principal-value limit or non-trace-class theorem is used.

The function q is bounded and continuous at zero because its two terms have magnitudes of order |z| and |z|^3.
The quotient (p-p(0))/z is bounded for each polynomial, and 1/|z| is integrable against planar area.
Hence the specified D maps its precise polynomial domain into H.

The differential term commutes with multiplication by z.
The quotient term contributes p(0)/2 and the Cauchy term contributes integral(p)/2 to the continuous commutator.
The atomic formula contributes the same scalar because partial_z(zp)(0)=p(0).
Both coordinates therefore equal tau(p), yielding [X,D]=P_Omega.
Angular integration and C1=bar z give D1=0.
These computations retain the operator's internal factors 1/2 separately from the Hilbert-space weights.

## Distribution coefficients and vacuum adjoint

The polar test-function calculation proves barpartial(1/z)=pi delta_0 with ordinary area measure and the stated Wirtinger derivatives.
The proof correctly avoids treating 1/z^2 as a locally integrable function.
For T=-partial_z(1/z), the boundary term after multiplication by bar z^m is O(epsilon^m); hence bar z^m T is the ordinary locally integrable quotient for every m>=1.

Multiplication by bar z^m annihilates partial_z delta_0 when m>=1.
Successive barpartial derivatives of bar z^3 T consequently give 3 bar z^2 T, 6 bar z T, 6T, and finally -6 pi partial_z delta_0.
The other term has fourth derivative 24/z because all delta products with positive powers of bar z vanish.
Thus the coefficients 1/12 and 1/24 produce exactly

barpartial^4 q_0 = -(pi/2) partial_z delta_0 + 1/z.

The cutoff is identically one near the singularity, so it introduces no additional point-supported terms.
Every derivative of the cutoff is supported away from zero.
The remainder R in (4.16) is smooth and bounded on the disk, vanishes near zero, and cancels 1/z outside the support.
The auxiliary test cutoff therefore permits testing against polynomials without a boundary contribution.
Dividing by pi and applying partial_z delta_0 to p gives the positive partial_z p(0)/2 in (4.17).

Combining this identity with the Cauchy mean calculation cancels both the derivative evaluation and the non-L2 1/z coefficient between the atomic and continuous outputs.
The result is exactly tau(Dp)=(1/2) integral((R-bar z)p)dnu.
With the proof's second-variable-linear Hilbert inner product, the representing vector is (0,conjugate(R)-z), as stated in (4.19).
It is an actual L2 vector.
The vacuum-adjoint assertion is therefore a bounded-functional assertion on the whole stated domain, rather than a formal integration-by-parts symbol.

## Dense adjoint domain and closure

For h_psi=(0,psi) with smooth support compactly contained in the punctured disk, four integrations by parts yield (4.20).
Rechecking the conjugates gives the atomic coordinate (1/2) integral(psi/bar z)dnu and the continuous coordinate in (4.21).
All differential and quotient coefficients are smooth with compact support away from zero; C* is bounded.
The remaining p(0) term is H-bounded because the measure has an atom of weight 1/2.
Thus each h_psi belongs to the actual adjoint domain.

These vectors are dense in the entire continuous summand.
Together with the previously verified vacuum vector they span a dense subspace of H, including approximation of the atomic direction.
The criterion recorded in Bla06-U001 therefore proves closability of this D on exactly its polynomial domain.
No claim that the atomic vector itself belongs to Dom D* is required.

Graph approximation transfers X-invariance and the bounded commutator to the closure.
If eOmega were in its domain, XeOmega=0 would force X closure(D)(eOmega)=Omega/2.
The atomic coordinate of the left side is zero, whereas that of the right side is 1/2.
This proves the asserted exclusion.
The same argument applies to any linear dual whose domain contains eOmega, so changing the implementer cannot produce a full-MOmega dual.

## Delta and the starred-commutator comparison

In each model, multiplication by the atomic projection is a nonzero rank-one operator commuting with X.
The accepted finite-rank-cycle characterization in MSY23-U002 therefore gives nonmaximal Delta.
This use requires neither a claimed exact Delta value nor a free-field theorem, entropy theorem or atomlessness assumption.

The Section 4.7 application of ACSY24-U001 was checked against its actual reconstructed Section 3, including the paragraph on merely bounded starred commutators.
A closable operator on a dense starred polynomial core extends the commutator identities to its closure; the adjointed relations give invariance for its adjoint.
Selfadjoint block regularization then gives strongly convergent bounded commutators, and finite-rank trace tests give maximal Delta.
The vacuum-adjoint premise is unnecessary at this step.
The generator-first sign is converted by negating the dual and does not affect the hypotheses.

Accordingly, boundedness of the additional starred commutator in the disk example would contradict its already established nonmaximality.
The explicit formula (4.26) also has the correct signs and coefficient -4.
Its other terms are bounded: evaluation at the atom is continuous, bar z/z has absolute value one, and the kernel (bar z-bar w)/(z-w) has absolute value one off the diagonal.
The proof correctly bases its unboundedness conclusion on the accepted regularization, without claiming an unproved differential-operator estimate.

The strong example meets both additional domain conditions simultaneously, so it supplies each weaker combination described in Section 5.
The corrected selfadjoint generating comparison has the density needed for the cited restriction argument.
Neither that comparison nor Shl06-U002's separate spectral-truncation statement asserts an all-MOmega domain.
The new example refutes the small-domain-to-full-domain implication and does not refute a converse whose starting hypothesis is an actual full-domain dual.

## Sources and inspection limits

The reviewer read the relevant fixed C_F0003 calculation and Xia23-U001's normalization and inspection limits, MSY23-U002's finite-cycle interface, ACSY24-U001's stated hypotheses and complete regularization section, Bla06-U001's adjoint criterion, and Shl06-U002's form-domain qualification.
The comparisons with C_F0084's nondense module and C_F0026's diffuse denominator obstruction were checked against those statements.
These inputs were accepted at their recorded scopes; the original MSY23, ACSY24, Blackadar, Shlyakhtenko, Xia and Shlyakhtenko--Turowska source proofs were not newly audited in full.

The reviewer independently accessed the parsed 98-page [Yger author-hosted notes](https://www.math.u-bordeaux.fr/~ayger/mht836.pdf), checking the title/course identification and Example 2.18, equation (2.21), printed p.31 / PDF p.35.
This is a selected primary-text inspection, not a visual-page or whole-notes audit.
The local polar proof supplies the exact normalization independently.
The Yge11 acquisition failed certificate verification and produced no local PDF; this review does not claim a retained artifact.
The academic-year identification is not a separate publication-date claim.

Ordinary polynomial and smooth approximation, distribution multiplication and differentiation, spectral calculus and elementary Hilbert-space graph facts are accepted standard foundations at the stated hypotheses.
Their uses were checked; no recursive audit of all foundational proofs is claimed.
No exhaustive literature search, priority assessment, numerical experiment, proof-assistant verification, manuscript revision or task-completion audit was performed.

## Conclusion

C_F0128 physical v2 passes this independently organized whole-argument review at its exact statement and source scope.
Both atomic counterexamples, the actual adjoint and closure assertions, the exclusion of every full-domain replacement, and the corrected supplementary comparison have complete arguments with no remaining mathematical gap found.
This supports a proved / independently reviewed assessment if the coordinating author adopts this finding.

V1 remains retained with the Section 5 scope finding above; it is not retrospectively certified as a completely correct whole argument.
No exact numerical value of Delta, general reverse implication, manuscript acceptance or broader task completion follows from this review.
