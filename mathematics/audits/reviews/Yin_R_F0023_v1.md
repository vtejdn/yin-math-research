---
author: Yin
---

# Independent review: free-product lifting of polynomial-core estimates

Date: 2026-09-11.
Reviewer: the coordinating agent.
Author: the reviewing agent.
Target: [the complete free-product lifting proof](../../claims/Yin_C_F0045_v1.md).

The reviewer proposed the possible right-module/little-Grothendieck route before the author developed the proof, but did not author the target.
This review checks the entire developed argument and its application, rather than counting the initial suggestion as independent evidence.

## Outcome

**Accepted in full at the displayed conditional scope.**
The only requested correction removed the stray comma from the squared norm exponent in (6).
No mathematical hypothesis, inference or conclusion was changed.

The conclusions are the actual original all-M domains and quantitative bounds, the restored affiliated rationality criterion for the original unstarred algebra, and the freely independent geometric examples.
The estimate for an arbitrary marginal and the case of correlated normal coordinates remain open.

## 1. Original core and canonical normalization

The reviewer reread the exact hypotheses and normalization of [Yin_C_F0025](../../claims/Yin_C_F0025_v1.md#yin_c_f0025).
Compactness of the starred generator commutators is present; its spectral argument identifies them with the Hilbert-Schmidt normal phase.
The resulting coarse derivation kills both generators of a different coordinate algebra and restricts to the scalar divided difference on the selected marginal.

Subtracting the original right multiplier does not assume a general rule for the difference of closed operators.
On the polynomial domain its actual adjoint contains every polynomial, with the explicit correction by right multiplication by eta*.
This establishes closability of the normalized operator.
The target correctly restores the original operators only at the later graph step.

Gram-Schmidt on the countable scalar starred monomials yields an algebraic orthonormal basis: each original polynomial is reached after finitely many operations, including when dependent monomials are omitted.
Reduced centered products therefore span the entire original polynomial algebra, not a selected smaller core.
Splitting the last coordinate factor gives the asserted finite right-module expansion uniquely.

## 2. Module orthogonality and the derivative action

In the pointed free-product Hilbert model, appending a centered j-factor to a reduced prefix ending outside j produces a reduced tensor; appending its scalar part leaves the prefix.
These alternatives partition the orthonormal reduced-word basis.
This proves the unitary module decomposition.

Its scalar pairings against two j-polynomials give E_(B_j)(u*v)=delta_(u,v)1.
No prefix is assumed unitary.
Expanding the finite polynomial square then yields the exact conditional-expectation identity in (10), and positivity supplies the operator-norm bound on the sum of coefficient squares.

At an earlier j-cut of the prefix, the following nonempty reduced word begins outside j and ends outside j.
Its conditional expectation onto B_j vanishes.
Multiplying on the right by the last j-factor preserves that vanishing.
The functional y -> tau(y c b) is bounded on H_j and zero on its bounded polynomial subspace, hence zero on all of H_j.
Consequently it also annihilates a completed Hilbert tensor derivative.
This checks the potentially nonalgebraic normal-phase case, not just selfadjoint polynomial tensors.
Only the final j-factor contributes after contraction, proving (14) on the full core.

## 3. Actual adjoints, constants and normalizations

Testing the algebraic direct sum one coordinate at a time identifies the adjoint with the Hilbert direct sum of the marginal adjoints.
Testing all finitely supported vectors gives exactly the square-summability requirement in (15).
Conversely that requirement represents the adjoint functional by Cauchy-Schwarz.
Finite truncation and marginal graph approximation similarly identify the closure.
This is a two-direction domain argument; no adjoint-core hypothesis is inserted.

The vacuum occupies only the empty-prefix coordinate, so its normalized adjoint image is the marginal vector xi_j.
Symmetry of the scalar divided difference gives e_j* b=b xi_j-J_j e_j J_j b, agreeing with the independently reviewed actual-adjoint identity in [Yin_C_F0044](../../claims/Yin_C_F0044_v1.md#5-original-adjoints-and-actual-coordinate-domains).
Thus the single marginal estimate yields the stated second bound.

The reviewer independently retrieved the [Pisier primary PDF](https://arxiv.org/pdf/1101.4195) and checked equation (5.2) and Theorem 5.2(ii), printed pp.20-21/PDF pp.22-23.
They give the complex squared constant 4/pi for any bounded linear map from C(S) to a Hilbert space.
The author records the independent short-proof inspection by another AI agent; this review retains the established theorem rather than claiming a full review of its historical foundations.
The version observation in the target is preserved.

Norm extension from P_j to C*(X_j) is justified by the marginal infinity bound.
The theorem applies separately to the derivative and its marginal adjoint restriction, with no normality or complete-boundedness requirement on these Banach-space maps.
Its finite-family column estimate combined with (10) gives both global bounds in (19).
Commutativity of the coordinate algebra is essential at this application.

The original eta_j need not be marginal.
Its two right-multiplication terms on polynomials have the claimed infinity-to-2 bound.
Therefore (20), and hence (4), concern the original dual and its actual adjoint.
The proof never identifies a sum of closed operators with a closure without justification.

## 4. Closed graphs and the exact rationality consumer

Uniformly bounded polynomial approximation of an arbitrary f in M follows from bounded strong-star density followed by norm approximation in the generated C*-algebra.
The resulting original operator images are bounded in H.
A weakly convergent subsequence of each graph lies in the weakly closed graph of the original closure or actual adjoint.
This proves domain membership and the sharp displayed constants by lower semicontinuity and approximation of the input norm bound.

The same bounded-set graph argument gives weak continuity of the operator images.
Applying it to p_n and X_k p_n extends the generator commutators to M.
The closure of the restriction to M equals the original polynomial closure because both graph inclusions hold.
Its adjoint is therefore the original actual adjoint.

The exact hypotheses of [Yin_C_F0024](../../claims/Yin_C_F0024_v1.md#yin_c_f0024) were reread and match these restrictions.
Its full-domain commutator criterion gives the missing reverse implication for Yin_C_F0025's weak forms.
Normalization invariance was already proved there.
This does not change the rational algebra to its starred enlargement, and it does not establish bounded division-closure equality.

## 5. Geometric application and verification boundary

The constants A_j, K_j and a_j in (22) match the accepted positive-reweighting estimate in Yin_C_F0044.
That result only supplied coordinate domains for a general tuple; the direct-sum argument here supplies the new mixed-word estimate under freeness.

For existence, the scalar constructions in Yin_C_F0044 extend as derivations to the algebraic free product.
Faithfulness of its tracial representation identifies this with the actual polynomial algebra.
The contraction calculation supplies the global vacuum adjoint.
The starred generator defect has its two Hilbert tensor legs in the selected marginal and therefore is the stated Hilbert-Schmidt operator on H, zero on its orthogonal complement.
Arbitrary eta corrections retain the original compact commutators and vacuum-adjoint condition.
The proposed examples consequently satisfy the hypotheses, rather than relying on an unconstructed dual.

The proof and cited consumer statements were checked throughout.
The sole typographic revision was checked.
No numerical experiment or formal proof check was performed or needed for this analytic argument.
Claim registration and navigation are root integration steps, separate from the mathematical review above.

## Actual review arrangement

The coordinating reviewer explicitly proposed the right-module/little-Grothendieck route before the author developed this proof.
That is substantive target-proof development context, despite non-authorship of the finished artifact.
The complete original finding is therefore self-reviewed.
The original 2026-09-11 date, sole comma correction, exact Pisier inspection and conditional/free-product boundaries remain intact.
This maintenance performs no new mathematical review or isolated-context certification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole lifting finding](#outcome) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole lifting finding](#outcome) | [C_F0045 statement](../../claims/Yin_C_F0045_v1.md#statement) | Whole eight-section conditional free-product lifting theorem, complete original polynomial-core module decomposition, actual adjoints, exact little-Grothendieck constants, original graph recovery and free geometric examples; no arbitrary marginal estimate or correlated-normal theorem. |
| [Whole lifting finding](#outcome) | [C_F0045 argument](../../claims/Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Same complete eight-section theorem and applications, with the proposed route shared before author development and all actual external-source boundaries retained. |
