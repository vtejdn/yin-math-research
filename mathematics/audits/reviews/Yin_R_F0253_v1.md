---
author: Yin
---

# Review of spectral relabelling, column bounds and Lipschitz graphs

## Whole-proof finding

At 2026-11-14T10:55 a separately assigned agent reviewed the entire [fixed candidate](../../claims/Yin_C_F0244_v1.md#decision-candidate), including the three assertions, the final scope observation and the mathematical uses of its direct inputs.
The reviewer had no role in developing this proof and received no development dialogue, drafts, author explanation or prior finding about it.
All three assertions follow under the stated hypotheses.

**Liberation and Borel coordinates.**
An injective conull relabelling with Borel inverse preserves the individual marginal algebra and diffuseness.
On each marginal a bounded strongly-star approximating polynomial net has convergent liberation derivative, since the marginal rule is the difference of two inclusions into the coarse space or zero.
Bounded strong-star convergence on the left and right of each cut in a word yields convergence of its Leibniz sum.
Closedness gives a single value on represented words, and the original vacuum pairing passes to every such limit.
The relabelled core is dense, hence this pairing identifies its liberation vacuum with the original vector.
The new joint spectral measure is the pushforward under the two copies of the relabelling.
The original joint vacuum measure is absolutely continuous with respect to the product of the diffuse marginals, so the exceptional fibres and spectral diagonal carry no weight.
The scalar condition, the inverse-gap integral, the norm identity and the inverse-Lipschitz implication now follow from the distinguished-coordinate criterion, which also allows arbitrary relabellings of the omitted variables.

**Column transfer.**
Matrix Kaplansky approximation and weak closedness of the graph extend the column inequality to finite bounded columns with its original constant.
The weak graph limit is unique on bounded strongly-star convergent nets.
In the separated-symbol identity this gives the limit on the right even when the second factor is merely measurable, while bounded multiplication on a coarse leg gives the strong limit on the left.
The measurable Schur theorem in its unit-ball normalization gives envelopes with product at most the Schur norm by rescaling.
For the first Leibniz term the positive inequality \(\sum_\ell w_\ell^* A w_\ell\le\|A\|\sum_\ell w_\ell^*w_\ell\) applies with \(A=\sum_j p_j^*p_j\).
For the second it applies to the column of \(w_\ell\) alone, followed by left multiplication by the \(p_j\) column.
In both estimates the Hilbert-space row \((x_\ell)\mapsto\sum x_\ell v_\ell\) is bounded by the other square-sum envelope, as seen by computing its adjoint.
This yields the factor \(2\).
The equality of the factorization and the symbol holds product-almost everywhere, which suffices on each coarse vector by the measure-class statement for the inner actions.

The uniformly Lipschitz marginal approximants give convergent divided differences in the coarse norm by dominated convergence off the diagonal.
The same nets approximate adjoints, so finite products give graph approximants to the entries and their adjoints, and hence to \(H_\alpha=b_\alpha^*b_\alpha\).
For the cutoff of this positive element, the polynomial Leibniz rule uses the **outer** actions.
Uniform polynomial approximation of \(f\) and \(f'\) bounds the divided-difference error uniformly, including on the diagonal, and the outer actions for a fixed polynomial converge strongly.
Thus the cutoff derivative converges to zero when the limiting spectrum is in \([0,1]\), even if the approximating spectra extend beyond it.
The bound on \(\sqrt t\,|f(t)|\) restores the required input column norm after polynomial approximation.
The target derivation agrees on every starred letter with the original graph derivative multiplied by the inner inverse secant, proving the transfer on the represented mixed core.
Conjugating both coordinates and the symbol preserves its Schur norm.

**Scalar graph law and the two domains.**
The packing inequality applies to the one-coordinate marginal considered as its own actual system.
For a dyadic partition its localized projections have radius bounded by the mesh times the Lipschitz constant of the graph map.
Summing the resulting inequalities bounds the cubed \(L^3\) norms of the parameter histograms, whose weak limits identify the parameter law on continuous tests.
Conversely, a compactly supported \(L^3\) density lies in \(L^{3/2}\) as well.
I checked the kernel and both boundedness exponents in Muscalu's printed formula on p. 1089, including the use of parameter Lebesgue measure.
The skew transpose in the bilinear pairing retains the off-diagonal kernel.
Cutting out adjacent endpoints gives separated-support commutator pairings, and on each same-interval pairing one may subtract a constant from \(f\).
Hölder on the interval sequence bounds the sum of the remaining operator errors by \(2\ell\,\operatorname{Lip}(f)\|T\|_{3\to3}\|\rho\|_3\|\rho\|_{3/2}\).
The bounded difference kernel on same-interval squares also has vanishing total integral since the parameter law is diffuse.
The resulting bilinear commutator gives \(2\int f\rho T\rho\), and \(\int|T\rho|^2\rho\le\|T\rho\|_3^2\|\rho\|_3\) puts its conjugate representative in the required \(L^2\) space.
This proves the scalar criterion for both the graph and the identity, and the two-sided gap comparison transfers the correlated condition in either direction.
The straight-arc column estimate applies to the selfadjoint starting coordinate.
Right-slice estimates for the graph and its conjugate give both one-input slice bounds because the companion derivative sends \(p\) to \((\delta(p^*))^\dagger\).
The two-slice theorem therefore gives both bounded-vector domains for the original canonical closure and its Hilbert adjoint.
The bounded generator commutator passes along core graph approximants, with the negative closure giving the generator-first convention.
The cited corner example supports the stated limitation on the multiplier test.

I checked the statements and applicability of the external operator results, including Aleksandrov–Peller's Section 4 and the opening of Muscalu's paper, and used the earlier project results at their indicated interfaces.
This review covers the fixed proof and gives no independent reconstruction of the cited external harmonic analysis theorems or general resolution of the normal-dual implication.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0244_v1.md#statement) | All three assertions, both orientations and the corner qualification. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0244_v1.md#argument) | Complete proof and scope of the converse problem. |
| [Whole-proof finding](#whole-proof-finding) | [ACSY and strong domains](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual starred vacuum and generator-first convention. |
| [Whole-proof finding](#whole-proof-finding) | [Column definition](../../claims/Yin_C_F0208_v1.md#statement) | Canonical right slice and finite polynomial columns. |
| [Whole-proof finding](#whole-proof-finding) | [Recovery](../../claims/Yin_C_F0238_v1.md#statement) | Distinguished scalar and liberation criterion, norm, and coarse inner spectral measure class. |
| [Whole-proof finding](#whole-proof-finding) | [Liberation adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Product-law domination for the joint vacuum measure. |
| [Whole-proof finding](#whole-proof-finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Uniformly bounded marginal and matrix approximants. |
| [Whole-proof finding](#whole-proof-finding) | [Canonical contraction](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Closability on the original polynomial core. |
| [Whole-proof finding](#whole-proof-finding) | [Schur factorization](../literature/AP25/Yin_U001.md#ap25-u001) | Operator-norm convention, square-sum constants and product-almost-everywhere equality. |
| [Whole-proof finding](#whole-proof-finding) | [Smooth approximation](../../claims/Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Approximation on a rectangle with first derivatives. |
| [Whole-proof finding](#whole-proof-finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#statement) | Forced starred values, closability and companion derivations. |
| [Whole-proof finding](#whole-proof-finding) | [Packing inequality](../../claims/Yin_C_F0233_v1.md#statement) | Item 1 on the scalar marginal and disjoint interval projections. |
| [Whole-proof finding](#whole-proof-finding) | [Graph Cauchy integral](../literature/Mus14/Yin_U001.md#mus14-u001) | Lebesgue-measure kernel and boundedness at the two dual exponents. |
| [Whole-proof finding](#whole-proof-finding) | [Straight arc](../../claims/Yin_C_F0234_v1.md#statement) | Full starred column for the starting selfadjoint coordinate. |
| [Whole-proof finding](#whole-proof-finding) | [Two canonical domains](../../claims/Yin_C_F0072_v1.md#statement) | Part B from the two single-input slice bounds. |
| [Whole-proof finding](#whole-proof-finding) | [Corner example](../../claims/Yin_C_F0241_v1.md#statement) | Item 3 for a non-Schur inverse secant with finite columns. |
