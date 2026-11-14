---
author: Yin
---

# Independent review of marginal domination for a Gaussian Markov slice

A reviewer for Yin examined the entire [candidate dated 2026-11-14T12:34](../../claims/Yin_C_F0262_v1.md#decision-candidate) and the five interfaces it selects.
The reviewer took no part in developing the proof and received the claim locator and scope without development dialogue, exploration notes, author explanations or previous findings on this candidate.

## Finding

At 2026-11-14T12:40 UTC the reviewer found the four conditions equivalent under the stated distinguished derivation hypothesis.
The original mixed core has squared unweighted norm \(H_*\), and for a fixed marginal density the single products have sharp squared constant \(H_*-1+1/s\), including the infinite case.
The disk example has actual starred ACSY, the strong domain condition, and unweighted norm \(\sqrt{2}\).

Symmetry and the Markov condition give unit squared creation norm in the column and row conventions.
The positive coefficient takes the weighted rectangle span densely onto the one-edge space, so the field construction supplies the full one-channel path space for the intrinsic pair even when \(P\) is unbounded.
When \(H_*<\infty\), the adjoint of the terminal integration on a fixed degree adds one edge with coefficient \(1/a\).
Its squared norm on a unit vector supported on a last-endpoint level set is the average of \(H\) against the squared vector.
Normalized indicators of upper level sets in degree zero give squared norms arbitrarily close to \(H_*\), and orthogonality gives the same upper bound on the direct sum.

On positive degrees leading creation leaves the terminal integration variable unchanged.
Leading annihilation and terminal integration vanish in both orders in degrees zero and one.
From degree two onward, fixing the remaining vertices gives an \(L^2\) product kernel in the two outside variables with squared norm \(H\) at the final retained vertex, since the first edge has squared integral one.
This justifies interchanging the two integrations also for two edges sharing the middle vertex.
Acting on a degree-zero \(g\), terminal integration after creation gives the constant \(\int g\,d\mu\).
The commutator with \(T\) is therefore the vacuum projection.
The operator commutes with left base multiplication and annihilates the unit, so the Leibniz formula on words identifies it with the original right slice.
Density of the mixed polynomial vectors then proves the assertion about its closure.

Markov integration gives the unit path norms and the leading annihilation recurrence for the products of successive edge coefficients.
The orthogonal vectors so obtained span all marginal polynomial vectors, giving the semicircular law and \(0<s<4\) for every normal marginal probability density.
For \(p=uTv\), projection of the degree-zero part of \(p^*p\Omega\) onto the constant vector gives the scalar \(\int |u|^2 Q(|v|^2)\,d\mu\).
In degree two the two endpoint integrals against the normalized two-edge vector are complex conjugates by kernel symmetry, giving \(\int |u|^2|Qv|^2\,d\mu\).
All other degrees vanish.
Pairing the conditional square with \(w\) thus weights the row variance by one and the squared row mean by \(s\), also for unbounded \(w\) by \(L^1\) truncation.
The slice on the same product is \(u\int v\,d\mu\).

Uniform approximation of square roots gives all nonnegative continuous tests in the left endpoint from squared base polynomials.
Consequently a fixed scalar domination constant yields the row inequality almost everywhere for each right polynomial.
The rational complex polynomials provide a single conull set, and uniform density extends the inequality there to every continuous right test.
Conversely such a row estimate integrates to the required estimate on each original single product.
On a positive probability row \(\nu_z=P(z,\cdot)\mu\), any representer in the usual row \(L^2\) inner product for integration against \(\mu\) must coincide with \(1/P(z,\cdot)\) by uniqueness of finite measures on continuous tests.
The row Hilbert norm scales the constant component by \(\sqrt s\) and leaves the centered component unchanged.
The representing density has mean one, hence its squared dual norm is \(1/s+H(z)-1\) if \(H(z)<\infty\).
When \(H(z)=\infty\), equivalence of the row norm with the usual \(L^2(\nu_z)\) norm excludes a bounded representer.
These row tests give the sharp essential supremum even if \(H\) is finite on every good row and essentially unbounded.
Taking \(w=1\) yields the unweighted lower bound on the full core in all cases, and \(P\ge c>0\) gives the stated norm bound directly.

On the unit disk, opposite caps witness the essential infimum zero of \(1+x(z)x(v)\).
Integrating out the imaginary coordinate gives the real marginal density \(2\sqrt{1-t^2}/\pi\).
Symmetrization and monotone convergence at the essential endpoints \(|x|=1\) give \(H_*=2\).
The scalar Cauchy row is bounded by integrating \(1/|z-v|\) on the radius-two disk about \(z\), so antisymmetrization gives a bounded scalar vacuum.
The reciprocal covariance integral is at most two.
In the second covariance integral, \(|x(w)(x(v)-x(z))|\le |v-z|\) cancels the endpoint singularity, and integration over the two endpoints gives \(\int H(w)^2\,d\mu(w)\le4\).
Positivity and the row bound supply the other assumptions of the one-channel criterion.
Finally the alternating centered moment for \(x,T\) is \((\int x^2\,d\mu)^2=1/16\), and the commutator has positive squared one-edge norm by diffuseness and positivity.
The source interfaces used here are the selected project results on Gaussian paths, the Markov marginal, the scalar area vacuum and the actual Gaussian criterion.
Their hypotheses and applications were checked at the scopes below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0262_v1.md#decision-candidate) | Complete dated candidate and all its selected mathematical interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0262_v1.md#statement) | Four equivalent conditions, original mixed-core norm and closure, sharp single-product constants and correlated disk example. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0262_v1.md#argument) | All degrees of the terminal integral, marginal projection, simultaneous row tests, reciprocal-density dual norm and both vacuum integrals. |
| [Finding](#finding) | [Field construction and generation](../../claims/Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Unit creation bound for the measurable coefficient and generation from a positive channel. |
| [Finding](#finding) | [Gaussian paths](../../claims/Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction) | Intrinsic path Hilbert structure, endpoint multiplication and the leading creation and annihilation formulas. |
| [Finding](#finding) | [Markov path recurrence](../../claims/Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square) | Orthogonal marginal basis, semicircular law and the projection formula extended to complex endpoints. |
| [Finding](#finding) | [Area-law vacuum](../../claims/Yin_C_F0259_v1.md#a-markov-covariance-with-a-small-transition-probability) | Absolute integrability and antisymmetrization for the scalar divided difference on the disk. |
| [Finding](#finding) | [Gaussian criterion](../../claims/Yin_C_F0209_v1.md#statement) | Actual distinguished derivation under starred ACSY, and both actual ACSY and strong domains from rank and the two integrals in the example. |
