---
author: Yin
---

# Review of the single exchange-symmetric pair criterion

## Finding

At 2026-11-16T16:47 UTC a separately assigned agent for Yin independently reviewed the full C_F0313 v1 candidate fixed at 16:47 UTC.
The reviewer had no role in developing this proof and received its fixed mathematical inputs without development dialogue, author explanations, exploration notes or prior findings on this candidate.
Both the small-corner operator norm estimate and the equivalence with a single exchange-symmetric pair hold.

In the free-product Hilbert decomposition every word containing noise has a unique initial optional \(R\)-letter before its first centered noise letter.
On that summand, compressing left multiplication by \(e\) to the initial \(L^2(B)\) gives \(tI\), since \(\mathbb E_B(e)=t1\).
Consequently \(\|eQ\|\le\sqrt t\).
A reduced word from \(B,W^*(S)\) containing noise maps \(L^2(R)\) into the range of \(Q\), even if its final \(B\)-letter times the input has a scalar part.
On the rest of the orthogonal complement of \(Q\), the initial \(R\)-letter is orthogonal to \(L^2(B)\).
Left multiplication by a bounded \(B\)-letter preserves this orthogonality, so the neighboring noise letters remain separated by a centered \(R\)-letter.
The output again lies in the range of \(Q\).
Subtracting \(\mathbb E_B\) from bounded approximating polynomials extends the resulting vanishing compression to every \(d_0=d-\mathbb E_Bd\) by normality.
The two terms in \(ed_0e=eQd_0e+e(1-Q)d_0Qe\) then give (1).
Simultaneous negation sends the gapped sign to its negative, and the odd part of \(B\) is spanned by \(J\).
Contractivity of expectation yields \(|b-1|\le\|J'-J\|<1/2\) for one fixed noise level because the free joint law and the norm bound on the semicircular generator are common to all models.
Dividing (1) by \(b\) gives the claimed error \(8\sqrt t\).

Unbounded finite-witness ratios in the sign-symmetric models permit fixing each polynomial expression and its telescoping tolerance before choosing \(t_n\).
The affine rescaling preserves its normalized ratio and the original marginal phase in the normalized corner.
For each distinct pair of nonauxiliary blocks \(n<k\) the mixed kernel has squared norm bounded by a constant times \(4^n t_nt_k\), with a summable double series under the stated mass bounds.
The auxiliary spectrum stays a positive distance from their union.
The auxiliary coefficient is a centered symmetry with a killed diagonal derivative, as required both for the block calculation and the sign involution.
The diagonal vacuum squares sum to a finite auxiliary contribution plus \(\sum_n4^{-n}\).
The mixed inner derivation has a finite vacuum and finite value on \(J\).
Inserting \(-D_0J/\epsilon\) at the independent semicircular cancels the derivative of \(J+\epsilon S\) with finite vacuum norm for this fixed \(\epsilon\).
Norm approximation of the sign by polynomials of that gapped selfadjoint element gives zero derivative in the graph.
The product rule and projection of the vacuum therefore give the actual relative derivative on the generated algebra.
Simultaneous negation fixes \(Z\) and reverses the sign there.

The conditional expectation of each block unit onto \(B\) is \(t_n1\) because every block symmetry is centered, including the auxiliary one.
The real spectral intervals are separated for each fixed block, so \(C^1\) approximation of its cut gives both norm convergence of the inputs and coarse convergence of their derivatives.
The inner double cut kills both \(e_n\) and \(J'\), and sends the affine copy of \(Z_n\) to the normalized unit tensor after multiplication by \(\alpha_n\).
The ambient normalized corner contains both the old coefficient \(J_n\) and the new one \(b^{-1}e_nJ'e_n\) within the fixed tolerance.
Its trace on the old block is the original trace, so the lower bound \(b_n/2\) on the formal right slice applies to the actual new corner polynomial.
In the reverse comparison, boundedness of the original slice with cost \(a\) passes to the simultaneous norm and graph limits by taking limits on each fixed input.
Slicing the two inner cuts costs a factor \(t_n\) from the second trace and \(\sqrt{t_n}\) from the first Hilbert norm.
The product identity bounds their combined ambient norm by \(2a\|x_n\|\le4a\).
This would give \(4a\ge b_n/(2^{n+1}\|\zeta_n\|_2)>2^{n-1}\) for every \(n\).

Finally the even-algebra identity is pointwise for this one assembled model.
When both coordinate costs equal \(c<\infty\), it bounds the full sign-model cost by \(\sqrt2 c\) using orthogonality and the two contractive parity coefficients.
Thus the assembled pair has infinite cost at both original coordinates, and the bare-dual criterion excludes a bare system on precisely this generated algebra.
The converse follows for any such pair under the same full actuality hypothesis.
This establishes the equivalences while leaving the finiteness of the universal constant open.
The source and earlier project results were checked at their eight specified interfaces.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0313_v1.md#decision-candidate) | Fixed 16:47 UTC decision with both conclusions and their exact inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0313_v1.md#statement) | Single-law and exchange-pair equivalences, failure of bare duals and the quantitative free perturbation estimate. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0313_v1.md#argument) | Entire proof, including the Hilbert decomposition, sign expectation, common fixed noise level, graph limits, corner norms and final model. |
| [Finding](#finding) | [Free Hilbert decomposition](../literature/Voi98/Yin_U005.md#voi98-u005) | Pointed tracial free-product representation through centered reduced tensors in Sections 5.5 through 5.8 of the inspected work. |
| [Finding](#finding) | [Sign and exchange models](../../claims/Yin_C_F0311_v1.md#statement) | Unbounded sign-symmetric test ratios and the pointwise parity identity with the two actual exchanged coordinates and equal costs. |
| [Finding](#finding) | [Finite witness](../../claims/Yin_C_F0305_v1.md#fixing-the-witnesses-before-the-masses) | Rescaling and telescoping of fixed polynomial and sliced derivative in an enlarged trace-preserving corner. |
| [Finding](#finding) | [Countable assembly](../../claims/Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Diagonal vacuum weights, summable distinct-block inner kernel and finite derivative at the symmetry. |
| [Finding](#finding) | [Free-noise insertion](../../claims/Yin_C_F0305_v1.md#restoring-all-normalized-coordinate-derivatives) | Arbitrary base tensor inserted at the independent semicircular generator and its finite vacuum norm. |
| [Finding](#finding) | [Spectral cut](../../claims/Yin_C_F0308_v1.md#encoding-the-coefficients-in-a-spectral-projection-of-a-noisy-operator) | Adjoining the sign with zero derivative and obtaining the represented target vacuum by projection. |
| [Finding](#finding) | [Corner comparison](../../claims/Yin_C_F0308_v1.md#direct-comparison-of-the-original-and-compressed-slices) | Graph approximation for separated cuts, phase and four supports in the corner, and exact trace factors in the slice comparison. |
| [Finding](#finding) | [Bare domains](../../claims/Yin_C_F0070_v1.md#statement) | Boundedness of the original canonical slice on core contractions from a bare full-domain system on a normal pair. |
