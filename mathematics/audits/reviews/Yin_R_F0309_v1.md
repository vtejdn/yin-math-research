---
author: Yin
---

# Review of the relative conjugate variable and slice in a spectral corner

## Finding

At 2026-11-16T15:46 UTC a separately assigned agent for Yin independently checked the complete [C_F0301 v1 candidate](../../claims/Yin_C_F0301_v1.md#decision-candidate), fixed at 15:44 UTC.
The reviewer took no part in its development and received the fixed argument and its dependencies without development dialogue, exploration notes, author explanations or previous findings on this candidate.
The construction gives the actual relative vacuum on the full coefficient core, and both estimates relating the core slice to the same-corner test hold as stated.

A bounded strong-star approximant to \(e\) has liberation derivative converging to \(e\otimes1-1\otimes e\) in coarse Hilbert norm.
On a word the remaining bounded left and right multipliers converge strongly on that Hilbert space, so the closed liberation graph also identifies the derivative of each represented word independently of its expression.
In \(eQe\), splitting at every occurrence of \(Z_e\) or its adjoint leaves compressed blocks from \(A_{\rm out}\); this gives precisely the stated weakly dense core.
The inner cut kills the liberation derivative of each exterior marginal letter and of \(e\), hence kills every compressed coefficient.
The additional outer supports on corner words place its range in the four-sided corner.
The formal divided difference recovers this cut liberation after multiplication by \(u\), including on \(Z_e^*\); both one-leg spectral actions are normal for the restricted marginal, so the inner diagonal annihilates their Hilbert tensor product.
This proves descent through every represented relation without imposing an algebraic independence assumption on the coefficients.

The unnormalized inclusion scales one-leg Hilbert norms by \(\sqrt t\) and coarse norms by \(t\).
At the marginal tensor \(e\otimes e\) the two corrections to the liberation adjoint cancel.
At \(h=1_{F\times F}\bar k_r\), the bounded Borel symbol lies in the adjoint graph domain for both measures, and the corrections instead give \(2t eB_r^F\) by antisymmetry.
Testing on graph approximants and dividing by \(t^2\) thus gives the two normalized adjoint pairings.
In the latter pairing the global off-diagonal vector converges in norm to \(e(\xi-\xi_B)e\); the restricted scalar correction converges weakly after testing against the marginal projection of the corner input.
Changing the one-leg trace gives coefficient \(t^{-1}\) on the first term and coefficient one on the scalar vacuum.
Joint spectral compression preserves orthogonality to the diagonal.
After multiplication by \(t^3\), the off-diagonal contribution is exactly its squared global compression norm, and the scalar contribution is at most an absolute multiple of \(G(\mu|_F)\).
Disjoint \(F\) give orthogonal compressions and disjoint curvature cubes; for arbitrary masses tending to zero the integrals over \(F\) and \(F^3\) tend to zero by absolute continuity, as does the off-diagonal vector mass by normality.

For the slice, first slicing the doubly cut tensor with the ambient trace gives \(tT_r^e(x)\).
Right compression of the output imposes the first inner cut.
In the missing second-leg block use \(x=xe\): the term differentiated at \(x\) has second leg in \((1-e)L^2(M)e\) and its trace vanishes.
The term differentiated at \(e\) contributes \(x eT_r(e)e\), since the doubly cut liberation of \(e\) is zero.
Graph approximation identifies the ambient slice on these words with the original normal cutoff.
The resulting expression extends normally to the full corner, since multiplication of an input by a fixed Hilbert vector is normal as a map into the weak Hilbert topology.
On the marginal the ambient map is the scalar cutoff, giving the uniform error \(B_e\le3a_\mu\).
For a corner contraction \(p\), the multiplier \(k_ru\) tends strongly to one on the coarse space and the right-hand error has global norm at most \(B_e\).
This gives \(t^{3/2}a_e\le k(F)+B_e\), including infinite cost.
For finite \(a_e\), the product rule bounds each separated unitary insertion by \(2a_e\) on a contraction by norm approximation of continuous marginal functions.
Averaging over the Gaussian probability mixture for \(1-k_ru\), then subtracting, gives \(3a_e\).
Bounded density and normality preserve this estimate on the full corner, which gives the converse inequality with the same trace scaling.
The cited localization result applies for each prescribed null sequence and \(d\ge3\); a spectral point has positive mass in every open neighborhood because the trace is faithful.
All calculations also apply after passage to the adjoint tuple, with its own orientation.

The six dependency interfaces below were checked at their indicated uses.
Their upstream proofs were not recursively re-audited.
This finding establishes neither boundedness of every relative slice nor the unrestricted implication from starred conjugate variables to full dual domains.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0301_v1.md#decision-candidate) | Fixed 15:44 UTC decision identifying the reviewed statement, proof and dependency scope. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0301_v1.md#statement) | The actual relative distinguished derivation, orthogonal vacuum, energy, compression identity and localized single-input equivalence in both orientations. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0301_v1.md#argument) | The full argument from Borel graph approximation through normal extension and core-to-cutoff estimates. |
| [Finding](#finding) | [Measurable spectral blocks](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Graph approximation for discontinuous marginal factors and cancellation for a symmetric projection pair. |
| [Finding](#finding) | [Marginal adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Weighted graph domain for bounded Borel tensors and signs of the row and column terms. |
| [Finding](#finding) | [Inverse-gap recovery](../../claims/Yin_C_F0238_v1.md#argument) | Injectivity on the coarse correspondence, normalized vacuum decomposition inputs, scalar weak limit and probability Fourier representation. |
| [Finding](#finding) | [Geometric energy](../../claims/Yin_C_F0255_v1.md#statement) | Quantitative equivalence and scalar bounded-vector domains for the original and restricted probability measures. |
| [Finding](#finding) | [Normal cutoffs](../../claims/Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Normal bounded original extension, scalar uniform cutoff estimate and passage from bounded core contractions to the full algebra. |
| [Finding](#finding) | [Same-corner test](../../claims/Yin_C_F0299_v1.md#statement) | Unboundedness on every neighborhood of one spectral point in the stated dimension range and orientation. |
