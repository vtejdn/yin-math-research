---
author: Yin
---

# Review of localization to two spectral points and divergence on every infinite subsum

## Finding

At 2026-11-16T15:07 UTC an agent outside proof development independently reviewed the [C_F0295 v1 candidate](../../claims/Yin_C_F0295_v1.md#decision-candidate) dated 2026-11-16T15:03.
The reviewer examined the statement, complete argument and the direct inputs below, without development dialogue, exploration notes, author explanations or earlier findings on this candidate.
The stated localization and simultaneous obstruction hold for each deficient orientation and each prescribed positive null sequence.

With \(C=\mathrm{id}\otimes\tau\), the two terms contributed by the inner multiplier \(z-w\) on \(a\otimes b\) are \(aZ\otimes b-a\otimes Zb\).
Cyclicity in the second leg consequently gives the negative sign on \(CI_{m_r}\gamma(x)\) in the right multiplication error.
In the left error only the derivative of \(Z\) remains, giving a coarse vector of norm at most \(\|x\|\) before the contractive slice.
For \(\gamma\), the single-input separated estimate has cost at most \(2B\): in the product identity each term costs at most \(B\) on a unit input and two unitary factors.
This uses the one-input norm \(B\), even when the full column norm is larger.
Subtracting its probability average from \(C\gamma\) costs at most \(3B\), and the remaining \(xT_r Z\) costs at most \(\|x\|\).
Normality and weak lower semicontinuity extend the inequalities to bounded inputs.
In each inverse iteration the boundary-supported remainder costs \(2^{-k}\|T_r\|\|x\|\); the errors sum to \(L\|x\|/s\).
The remainder only needs to vanish with \(r\) fixed.
If every point of the compact product had a bounded output rectangle, the finite partition of the spectrum by the sides of a finite subcover would bound every output block and hence the total norm.
This contradicts core convergence and unboundedness on core contractions.
At the resulting pair, the two off-support bounds apply separately to the left and right discarded input terms and bound their compressed outputs uniformly.
Thus every doubled-ball corner in the proof retains unbounded cutoff norms.

A simultaneous \(C^1\) polynomial approximation on a convex box gives uniform control of the differences of secant kernels by the gradient error, for either denominator \(z-w\) or \(\bar z-\bar w\); the diagonal is product-null.
On mixed products the bounded outer actions and the Leibniz rule give convergence of both derivatives in the coarse Hilbert norm and bounded limits in the opposite spatial algebra.
The same applies after multiplying an expression by a smooth spectral character.
The separated multiplier identity then bounds the character slice by \(K+b\) under the proposed punctured bound \(K\), since the character preserves the support and norm of the input.
The marginal estimate applies to the character by norm and graph approximation, using the actual marginal vacuum obtained by restriction and orthogonal projection.
Averaging and subtracting bounds all cutoffs by \(2K+b\).
Bounded polynomial approximants exist by Kaplansky density; in the finite tracial representation bounded strong convergence gives tracial \(L^2\) convergence, also of adjoints, hence bounded strong-star convergence.
Smooth contractions can be chosen to tend to one on the doubled balls except at the two points while supported compactly inside the punctured neighborhood.
Sandwiching the approximants in these cuts recovers any contraction of the doubled-ball corner because the two singleton projections vanish.
Fixed-radius weak continuity now contradicts the unbounded norms already proved for that corner.

For a selfadjoint enlarged expression \(h\), polynomial functions of \(h\) retain simultaneous norm and coarse approximation.
Consequently the Neumann inverse calculation of C_F0285 applies to its resolvent, whose opposite-tensor derivative is the bounded derivative of \(h\) multiplied on the left by the two outer resolvent factors (with a minus sign).
The sliced norm has integrable majorant \(\|\Phi(\delta h)\|\|R\|_2\|R\|_1\) at good thresholds, including for every inner cutoff since its opposite multiplier is a contraction.
Both actual forward graph limits and both adjoint limits follow as in that input: bounded strong convergence controls multiplication on the vacuum, while the opposite forward value converges in Hilbert norm.
The exceptional thresholds for each of \(h,-h\) have measure zero by the scalar mass criterion.
Strict upper cuts at \(t>0\) are supported within the support corner of \(h\), since the complementary block is zero.
For a fixed adjoint test, the two scalar spectral layer integrals of these cuts give the pairing with \(h\); good thresholds suffice, and a common bound \(D\) on their forward values gives a bound \(2D\) by density of adjoint tests.
Real and imaginary parts of the punctured contractions are still in that class, so this contradicts the already unbounded forward norms.

For each large actual value a unit adjoint test detects it with arbitrary strict slack by density.
Convergence at that one projection permits an index later than all previous indices.
The next neighborhood can simultaneously miss its compact support and bound both current normal functionals by one on the entire corner unit ball: approximate each tracial \(L^1\) density by a bounded one, then use the vanishing corner trace.
Every later subsum lies in that corner, whereas the preceding terms cost at most the indicated sum of finite individual norms.
Testing at each selected index therefore gives unbounded scalar pairings for both the actual adjoint tests and the cutoffs of the same infinite subsum.
The former contradict forward domain membership because the tests are unit vectors; the latter force unbounded cutoff norms along the prescribed sequence.
Finite sums retain all four domains and cutoff convergence by linearity, and the nonzero orthogonal atoms generate the asserted abelian algebra on their sum.
Conversely a finite core bound gives uniformly bounded cutoff norms by C_F0282, excluding such a family; C_F0075 makes the corresponding failure in either orientation incompatible with the strong condition.
This is a necessity and a conditional obstruction, without an example of a deficient actual tuple or a resolution of F0011.
Established inputs were checked at their stated interfaces; no new verification of the original source proofs is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0295_v1.md#decision-candidate) | Complete 2026-11-16T15:03 candidate with eight declared direct inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0295_v1.md#statement) | Order of the sequence, pair, neighborhood and subsum quantifiers; both defects and the converse. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0295_v1.md#argument) | The multiplication estimates, spectral corner, punctured graph tests, spectral layers and simultaneous diagonal selection. |
| [Finding](#finding) | [Actual starred hypothesis](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual vacuum on the represented starred core, without a full-domain assumption. |
| [Finding](#finding) | [Liberation and Gaussian multipliers](../../claims/Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Bounded liberation slice, single-input separated identity and positive Fourier probability for the complementary symbol. |
| [Finding](#finding) | [Normal cutoffs](../../claims/Yin_C_F0282_v1.md#statement) | Normal bounded extension at fixed radius, convergence on the core and the uniform bound under finite single-input cost. |
| [Finding](#finding) | [Mixed spectral cuts](../../claims/Yin_C_F0285_v1.md#statement) | Almost-everywhere good thresholds, four graph domains and both strong cutoff limits; extension to the enlarged expressions checked above. |
| [Finding](#finding) | [Sliced resolvents](../../claims/Yin_C_F0285_v1.md#slices-of-resolvents-of-a-mixed-polynomial) | Opposite spatial bound and resolvent derivative with two outer factors for the extension argument. |
| [Finding](#finding) | [Marginal phase](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness, divided differences on both oriented cores, closability and reversal. |
| [Finding](#finding) | [Scalar estimate](../../claims/Yin_C_F0267_v1.md#statement) | Uniform scalar right-slice estimate from the integrable marginal weight, applied by approximation to the characters. |
| [Finding](#finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Contraction approximation in the generated finite algebra; bounded strong-star refinement in the tracial representation. |
| [Finding](#finding) | [Tracial predual](../literature/AP18/Yin_U003.md#ap18-u003) | Integrable densities for both normal tests, specifically the retained predual interface. |
| [Finding](#finding) | [Tracial predual interface](../literature/AP18/Yin_U003.md#l1-predual-interface) | Norm approximation by bounded densities for restriction to shrinking corners. |
| [Finding](#finding) | [Normal domain comparison](../../claims/Yin_C_F0075_v1.md#statement) | Both oriented right bounds characterize the strong normal-tuple condition. |
