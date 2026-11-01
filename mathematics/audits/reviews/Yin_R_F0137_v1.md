---
author: Yin
---
# Independent review of elliptic unitary coordinates and full-domain duals

Review performed and recorded: 2026-10-14T13:24.
Human record author: Yin.
The acsy_rationality_check agent carried out a separately organized whole-argument mathematical review of the fixed candidate described below.
No personal human inspection or formal verification is claimed.

## Arrangement and exact inputs

The exact input is [C_F0130 v1](../../claims/Yin_C_F0130_v1.md), dated 2026-10-14T13:19, its Statement and complete Argument, Sections 1-7.
The reviewer read the complete fixed candidate without modifying it.
Root had supplied a preliminary outline identifying the inner tensor action, the projective series and the intended two Neumann inversions; the author subsequently supplied the fixed path and a list of interfaces needing attention.
The reviewer had not developed this elliptic-coordinate proof.
The review was not blind: shared comparison context and the preliminary outline were available before the fixed candidate was read.

The reviewer reconstructed the coefficient orders, adjoint pairings, series estimates and scalar example directly.
The precise accepted statements of C_F0069 Part A and C_F0071 v2 Part D were checked, including the current independently reviewed decision of C_F0071 v2.
C_F0018 Section 1 was read to compare the projective correction on B(H) with the new use on B(M,H).
The ACSY24-U001 source boundary was consulted.
No new whole-source audit of the ACSY24 PDF or recursive re-audit of the accepted upstream proofs was performed; the finite unitary-tensor adjoint interface needed here is proved and checked directly in the candidate.

## Current relationship clarification

The original dated independent wording remains the historical description.
Before reading the fixed candidate the reviewer received a preliminary outline identifying the inner tensor action, projective series and two Neumann inversions, together with shared comparison context.
A fixed short proof or proof outline and a list of review interfaces are legitimate inputs.
The retained description does not establish whether that outline/context was only such a fixed proof input or additional substantive author development/explanation.
The current whole-finding relationship is therefore unknown; no mathematical contribution or failed isolation is guessed from the word outline alone.
No reviewer-supplied repair is recorded.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0130 Statement](../../claims/Yin_C_F0130_v1.md#statement) | Four-condition equivalence for arbitrary generating unitary tuples under the strict elliptic coefficient inequality, the quantitative actual-vacuum bound and stated limits. |
| [Conclusion](#conclusion) | [C_F0130 Argument](../../claims/Yin_C_F0130_v1.md#argument) | Complete Sections 1-7: common algebra, projective coefficients, actual adjoints, both derivation implications, both full-domain implications and strict scope example. |
| [Conclusion](#conclusion) | [C_F0071 v2 Statement](../../claims/Yin_C_F0071_v2.md#statement) | Accepted Part D equivalence for arbitrary unitary generating tuples; no freeness premise. |
| [Conclusion](#conclusion) | [C_F0069 Statement](../../claims/Yin_C_F0069_v1.md#statement) | Accepted Part A automatic M-operator-norm-to-H boundedness, applied separately to each normal diagonal coordinate. |
| [Conclusion](#conclusion) | [C_F0018 correction mechanism](../../claims/Yin_C_F0018_v1.md#1-algebra-norms-and-the-correction-lemma) | Product order, right multipliers and projective norm estimates; their B(M,H) adaptation is checked directly below. |
| [Conclusion](#conclusion) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Exact starred derivation and actual vacuum condition; the finite unitary-tensor adjoint estimate is independently reconstructed from the vacuum pairing. |

## Common algebra and two distinct tensor actions

The inverse formula
\[
 U_j=\frac{\overline{\alpha_j}X_j-\beta_jX_j^*}
 {|\alpha_j|^2-|\beta_j|^2}
\]
is correct by expansion of \(X_j=\alpha_jU_j+\beta_jU_j^*\).
Its denominator is strictly positive.
Thus the represented star algebras, and hence the generated von Neumann algebras, agree.
Each \(X_j\) is normal because it is a polynomial in one unitary and its adjoint.
The argument never assumes that different \(U_j\) commute or are free.

The projective product is \((a\otimes b)(c\otimes d)=ac\otimes db\).
The inner coefficient operator \(I_{c\otimes d}(a\otimes b)=ac\otimes db\) commutes with the outer bimodule actions.
Its norm is at most \(\|c\|\|d\|\), so the projective extension is legitimate.
In particular \(I_w I_z=I_{zw}\): it acts by right multiplication of the coefficient tensor.
The proof only needs this identity on the displayed projective series or commuting marginal coefficients, where \(I_{J_i}q_i=q_iJ_i=1\) and \(I_{q_i}J_i=J_iq_i=1\).

The outer action \(\eta\mapsto U_j^*\eta U_j^*\), used to solve the derivation equation, is a different operator.
It is unitary on the coarse Hilbert space.
Iterating it on \(1\otimes1\) produces exactly \((U_j^*)^n\otimes(U_j^*)^n\).
Its Neumann solution therefore agrees with the image of the projective series \(q_j\).
No injectivity of the map from the completed projective tensor product to the Hilbert tensor product is required.

## Actual unitary-tensor adjoints and the infinite series

For an outer derivation \(\gamma\) with actual vacuum \(\xi\), expand \(\gamma(v^*pw^*)\) for unitaries \(v,w\in A\).
The middle term paired with \(1\otimes1\) is \(\langle v\otimes w,\gamma(p)\rangle\).
The vacuum term is bounded by \(\|\xi\|_2\|p\|_2\).
In the first remaining term, contraction gives the pairing of \(p\) with a unitary multiple of the left contraction of \(\gamma(v^*)\); in the last, it gives the pairing with a unitary multiple of the right contraction of \(\gamma(w^*)\).
Each slice map has norm one.
This proves exactly
\[
 \|\gamma^*(v\otimes w)\|_2
 \le\|\xi\|_2+\|\gamma(v^*)\|_2+\|\gamma(w^*)\|_2
\]
as an actual Hilbert-adjoint conclusion, without assuming reality.

For the unitary-coordinate derivation, the product and inverse rules give \(n\) elementary unitary tensors for the derivative of \(U_i^{-n}\), and hence the upper bound \(n\).
The resulting estimate at \(U_i^n\otimes U_i^n\) is \(\|\xi_i\|_2+2n\), including \(n=0\).

For A(X) to A(U), the derivation equation in the candidate has the correct inverse-rule sign.
Applying \(I_{J_i}\) normalizes the generator values.
The actual vacuum is the finite expression with coefficients \(\overline{\alpha_i},-\overline{\beta_i}\), since \(I_{U_i^*\otimes U_i^*}^*(1\otimes1)=U_i\otimes U_i\).

For A(U) to A(X), \(I_{q_i}\theta_i\) is Hilbert-valued and retains the Leibniz rule because the inner action commutes with the outer actions.
Its generator values are correct.
The adjoint vectors in the proposed infinite series have a summable upper bound
\[
 \frac1{|\alpha_i|}
 \sum_{n\ge0}
 \left|\frac{\beta_i}{\alpha_i}\right|^n
 (\|\xi_i\|_2+2n).
\]
Both the tensor series and the representing-vector series converge in their actual Hilbert spaces, so their pairings with every fixed core element can be interchanged.
This verifies the actual vacuum, not merely a formal adjoint expression.
Summing the two series gives exactly
\[
 \frac{\|\xi_i\|_2}{|\alpha_i|-|\beta_i|}
 +\frac{2|\beta_i|}{(|\alpha_i|-|\beta_i|)^2}.
\]

## Projective correction on B(M,H)

The change from B(H) to bounded maps from \(M\) with its operator norm into \(H\) is valid.
Right multiplication by \(b\) preserves \(M\) with norm at most \(\|b\|\), and right multiplication by \(a\) preserves \(H\) with norm at most \(\|a\|\).
Thus \(Q_{a\otimes b}(E)=\rho(a)E\rho(b)\) has the claimed norm bound.

With \(z=a\otimes b\) and \(w=c\otimes d\), direct multiplication gives
\[
 Q_wQ_z(E)=\rho(ac)E\rho(db)=Q_{zw}(E).
\]
The tracial pairing also gives
\[
 Q_w(aPb)=acPdb=\kappa(zw).
\]
These are the orders needed in both corrections.
All maps are continuous in the projective norm, so the identities extend to the completed coefficients.
Right multipliers commute with bounded left multiplication by every \(y\in M\), giving the commutator identity on all \(M\Omega\).

For F(U) to F(X), the inverse commutator is \([E_i,U_j^*]=-\delta_{ij}U_j^*PU_j^*\), so the coefficient is \(J_i\).
C_F0069 supplies the required Banach-space boundedness of \(E_i=-D_i\) because \(U_i\) is normal and its diagonal commutator is \(P\).
Correcting by \(Q_{q_i}\) yields \(\kappa(J_iq_i)=P\).

For F(X) to F(U), the same accepted automatic-continuity input applies because each \(X_i\) is normal.
The map \(K\mapsto U_j^*KU_j^*\) is an isometry on B(M,H): the input and output multipliers are unitary on their respective norms.
Hence the Neumann inversion of the displayed equation for \(K_{ij}\) is justified in precisely that Banach space.
It gives \(K_{ij}=\delta_{ij}\kappa(q_i)|_M\).
The correction \(Q_{J_i}\) then yields \(\kappa(q_iJ_i)=P\).
The sign convention \(E_i=-D_i\) produces the required generator-first duals.
No Hilbert-space adjoint or closability of the supplied full-domain maps was used.

Combining these independently checked implications with the accepted unitary equivalence proves all four conditions equivalent.
The accepted input has no freeness assumption, so no such condition has entered the assembly.

## The scalar example and scope limits

On the Haar Fourier basis, the proposed bounded backward operator satisfies \([E,U]e_n=\delta_{n0}e_0\), including the boundary indices \(n=-1,0,1\).
Thus the example has the required full-domain condition.

Every element obtained from \(\mathbb C[X]\) using scalar sums, products and admissible inverses in \(M\) is represented by a rational function of \(X\).
If \(X^*=R(X)\), the displayed linear relation would make \(U\) rational in \(X\).
An almost-everywhere equality of these rational functions on the circle becomes a rational-function identity after clearing denominators; a nonzero rational function cannot vanish on this infinite set.
The automorphism \(z\mapsto r/z\) fixes \(z+r/z\) and does not fix \(z\).
It therefore excludes \(z\in\mathbb C(z+r/z)\), proving the strict failure of the bounded-division-adjoint hypothesis.
This is a comparison of scopes, not a separation of A and F.

The proof correctly excludes equal-modulus coefficients from its coordinate equivalence.
Translations have zero derivation and commutator contributions.
Interchanging a unitary with its adjoint treats the reversed strict inequality by the same argument.
No finite-rank preservation is claimed for an infinite projective correction.

## Conclusion

The complete fixed C_F0130 v1 Statement and Argument pass this separately organized independent review, with no required mathematical correction.
The result supports the four-condition equivalence and stated vacuum bound for the precise elliptic unitary-coordinate class.
If adopted by the responsible author, this finding can support proved / independently reviewed for the identified candidate.

The review does not settle either implication for arbitrary correlated normal tuples, identify arbitrary supplied full-domain operators with canonical closures, or assert finite-rank preservation under infinite projective coefficients.
The accepted upstream unitary equivalence and automatic-continuity theorems were reused at their checked interfaces; their complete original proof chains and all source papers were not recursively re-audited.
No novelty, priority or formal-verification claim is made.
