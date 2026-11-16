---
author: Yin
---

# Review of the liberation gradients after free Poisson conjugation

## Finding

At 2026-11-16T17:48 UTC a separately assigned agent for Yin independently reviewed the whole C_F0324 v1 candidate fixed at 17:46 UTC.
The reviewer did not develop this proof and received its fixed mathematical inputs without development dialogue, exploration notes, author explanations or previous findings on this candidate.
Under the asserted failure hypothesis, one pair satisfies the two small liberation bounds along with the exact marginal trace identity, the semicircular approximation and the two infinite costs.

The inverse automorphism sends \(u\) to \(U=(u-r)(1-ru)^{-1}\), so the two generate the same noise factor.
The nonnegative Laurent moments of \(u\) are its analytic constant terms \(r^n\), and adjunction gives \(r^{|n|}\) at negative exponents.
Conjugation of a centered base symmetry by an independent Haar unitary makes a symmetry free from the base, by reduced words.
The identity \(u-U=r(1-U^2)(1+rU)^{-1}\) yields the claimed \(4r/(1-r)\) error in the conjugated symmetry.
Expanding \(u s_*u^*\) around \(\tau(u)=r\) and using \(\tau(s_*)=0\) gives \(\mathbb E_{\mathcal R}s=r^2s_*\).
The symmetry belongs to \(B_*\vee W^*(U)\), the grading fixes the base coordinate and reverses this symmetry, and its norm is one.
These are all the inputs needed for the four-step expectation and the two successive compressions.
The recovered \(J\)-coefficient is \(r^8\) and the compressed error before dividing by it is at most \(512\sqrt{t_n}\).
With \(\mathbb E_{B_*}g(W)=\tau(g(W))1\), centering \(s-r^2s_*\) yields exactly the regression with quadratic coefficient \(r^4\) in the conditional conjugation.
The unsmoothed matrix identity makes both resulting terms give the product trace for every bounded Borel test.

For the two angular derivations the cuts at \(n>0\) have moment exponents summing to \(n\).
The inverse rule reverses the sign for every cut at \(n<0\), and all its exponents are nonpositive.
Thus either orientation gives the double trace \(nr^{|n|}\).
In the convention that the Hilbert product is linear in the second variable the representing vector is \(-i w_r'/w_r\) in angular coordinates for the Poisson density \(w_r\).
Using the inverse disk automorphism gives \(H_u=r(U-U^*)/(1-r^2)\) with the sign in (2).
Its mean is zero, its operator norm is \(2r/(1-r^2)\), and its trace Hilbert norm is \(\sqrt2\,r/(1-r^2)\) because \(U\) is Haar.
The free extension preserves either vacuum by the centered-word double-trace calculation.

For \(K=a\otimes c\), inner insertion into \(d_R\) gives \(u a\otimes c\) at \(u\) and \(-a\otimes c u^*\) at \(u^*\).
Trace cyclicity changes its double trace at \(x\) to the pairing of \(H_u\) with \(axc\), which yields \(a^*H_uc^*\) as claimed.
For a finite sum, the polarized free-word identity factors each cross inner product into the conjugate base tensor inner product times \(\|H_u\|_2^2\).
Consequently the vacuum assignment extends conjugate-linearly to all of the coarse space.
Each evaluated derivative on a fixed polynomial depends continuously on that tensor through finite bounded outer multiplications.
This justifies the actual vacuum for the possibly unbounded mixed kernel \(K\).
The correction at \(s=u s_*u^*\) cancels \(Ls_*\) with the indicated order of its two products.
The corrected generator and phase belong to the intrinsic coarse space on restriction, and the vacuum error is at most the prior pre-noise error plus \(\|H_u\|_2\|K\|_2\).
The preliminary constraint on \(\sum_n4^nt_n\) bounds \(\|K\|_2\) before choosing \(r\).
One can therefore choose \(r>0\) for both gradient tolerances, the sign error and the vacuum error, and then decrease each \(t_n\) to absorb \(r^{-8}\) in its fixed test tolerance.
This preserves the divergent normalized corner lower bounds.
The quantile comparison applies because \(s_f\) is a centered symmetry free from \(\mathcal R\).
The even-algebra transfer supplies the actual variables on \(Q\), their infinite costs, and the resulting absence of bare duals.

For the liberation calculation, \(d_Lu^*=-u^*\otimes1\) gives \(d_Ls=1\otimes s-s\otimes1\).
Hence \(\operatorname{ad}+d_L\) kills \(s\), acts as \(\operatorname{ad}\) at \(W,W^*\), and has vacuum \(H_u\) in the ambient algebra.
Each \(Q\)-leg projection is \(Q\)-bimodular and preserves its trace.
For \(sWs,sW^*s\) the two tensor legs of the derivative are odd and both projections kill them.
This identifies the first actual partial liberation on the full even polynomial core, with vacuum \(\eta_0=\mathbb E_Q H_u\).
The second partial liberation is the difference between \(\operatorname{ad}\) and the first, hence has vacuum \(-\eta_0\).
Their equality to the two distinguished commutators follows from the actual joint vacua at the original coordinates.
The conditional expectation is contractive in operator norm.

Finally \(W_0\) lies in the matrix base and \(H_u\) is centered and free from that base.
Bimodularity of \(\mathbb E_Q\) on both sides, followed by the polarized free-word inner product, bounds \(\|k_0\eta_0\|_2^2\) by \(\|H_u\|_2^2\int |k|^2\,d\mu^2\) for every finite sum of separated bounded Borel functions.
Taking indicators of finite disjoint rectangle unions and applying finite-measure monotone class gives domination on the full product Borel sigma-algebra.
The exchange automorphism intertwines the marginal actions and carries the first liberation vacuum to the second by uniqueness.
Thus the same density bound holds at \(W_1\), even though it need not lie in the original matrix base.
Taking \(r\) small yields (1) simultaneously with the previous requirements.
The ten declared dependency interfaces were checked at their indicated uses.
Whether the general implication fails remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0324_v1.md#decision-candidate) | Fixed 17:46 UTC decision and all selected conclusions. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0324_v1.md#statement) | Conditional single actual exchange pair with small bounded gradients, domination at every Borel set, product marginal traces, semicircular coupling and infinite slice costs. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0324_v1.md#argument) | Entire Poisson construction, its two angular orientations, tensor insertion, simultaneous parameter choice, actual even liberation and both spectral measures. |
| [Finding](#finding) | [Four matrix corners](../../claims/Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) | Four-step regression from the centered symmetry, free factor and exact conditional mean. |
| [Finding](#finding) | [Two compressions](../../claims/Yin_C_F0322_v1.md#uniform-recovery-on-small-primary-pieces) | Uniform \(512\sqrt{t_n}\) error before compensating the factor \(r^8\). |
| [Finding](#finding) | [Ambient derivative](../../claims/Yin_C_F0322_v1.md#placing-bad-tests-in-the-top-semicircular-interval) | Zero base derivative on \(s_*\) before the inner correction, block estimates and preliminary control of \(K\). |
| [Finding](#finding) | [Good vacuum](../../claims/Yin_C_F0322_v1.md#the-good-vacuum-and-its-approximation-to-the-coordinate) | Original good and tail vacuum errors before replacing the free noise insertion. |
| [Finding](#finding) | [Corner tests and coupling](../../claims/Yin_C_F0322_v1.md#the-bad-mixed-tests-trace-independence-and-the-reference-pair) | Infinite costs from separated cuts, no bare duals and the operator-norm and vacuum comparison with an ambient free semicircular pair. |
| [Finding](#finding) | [Conditional trace law](../../claims/Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | The quadratic conditional expectation for a centered-over-\(B_*\) perturbation. |
| [Finding](#finding) | [Unsmooth matrix traces](../../claims/Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces) | Exact factorization on all Borel marginal pairs for the base matrix symmetry. |
| [Finding](#finding) | [Angular vacuum](../../claims/Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Poisson Laurent moments, angular sign and Haar-coordinate formula, and free extension of the centered vacuum. |
| [Finding](#finding) | [Even-algebra transfer](../../claims/Yin_C_F0311_v1.md#derivations-on-the-even-algebra) | Even core, actual distinguished vacua, exchange and cost transfer. |
| [Finding](#finding) | [Liberation adjoint](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | The actual commutator formula at each original normal coordinate. |
