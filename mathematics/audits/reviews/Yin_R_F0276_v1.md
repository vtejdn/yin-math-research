---
author: Yin
---

# Review of dominating weights for the scalar planar right slice

At 2026-11-14T13:16 UTC, a separate agent reviewed for Yin the whole [candidate dated 2026-11-14T13:14](../../claims/Yin_C_F0267_v1.md#decision-candidate).
The reviewer had no role in its development and received the fixed candidate, the requested scope and the dependency locators, without proof-generation discussion.
A review of a different claim was consulted for its record format.

## Finding

The whole candidate is supported, including the case of positive one-dimensional density.
The scalar vacuum gives a diffuse measure, finite ordered curvature energy and an \(L^2(\mu)\) maximal linear density by F0255.
For Tolsa and Verdera's Theorem 2, the density convention printed on p. 481 uses the radius, while its proof evaluates the contribution on a Lipschitz graph at the derivative with respect to ordinary arclength.
In Lemma 8, equations (9) and (10), ordinary Lebesgue measure on a line gives \(4\int_0^1\log(1+t)\,dt/t=\pi^2/3\).
At almost every point of a rectifiable graph its arclength in a radius-\(r\) ball is asymptotic to \(2r\).
The localization in equations (5)–(7) discards the zero-density part and the off-graph terms in this near-diagonal limit.
Thus the coefficient \(\pi^2/3\) in the energy multiplies the square of the candidate's density with denominator \(2r\).
For the ordered curvature integral the coefficient is \(1/6\) directly in (4).
The source obtains \(C^*\mu\in L^2(\mu)\) from Lemma 7 and (5) on p. 487 before it distinguishes the density regimes.
The hard truncations converge pointwise almost everywhere to the principal value and the errors are bounded by \(2C^*\mu\), giving strong convergence also on the rectifiable part. [Published paper](https://www.acadsci.fi/mathematica/Vol31/tolsa.pdf) and [authors' version](https://mat.uab.cat/~xtolsa/xv2.pdf).

For bounded real \(f\), the bounded positive factor \(1+sf\), with a positive lower bound, preserves both geometric hypotheses and gives equivalent \(L^2\) norms.
Ball differentiation with respect to \(\mu\) gives the claimed density of \((1+sf)\mu\) on the same full-measure set as the density of \(\mu\).
The difference of the hard transforms of \((1+sf)\mu\) and \(\mu\) equals \(sC_\epsilon f\) in the conjugated orientation, identifying both the strong and principal-value limits on \(f\).
Linearity of the cutoffs gives the complex extension.
On the represented polynomial core, boundedness of the divided differences and diffuseness justify passage to the limit in their truncated integrals.
Swapping the two variables doubles the pairing against the conjugated hard transform, so \(\xi=2B\).
F0162 then gives the core adjoint \(Tp=pB+Cp\) and the conjugated slice \(JEJp=pB-Cp\).

In the first and second coefficients of the cubic reweighting, the ordered curvature integral contributes three identical integrals in each case, yielding the factor \(1/2\).
The arclength-density term contributes \(\pi^2\int\theta^2 f\,d\mu\) and \(\pi^2\int\theta^2 f^2\,d\mu\), respectively.
Using \(\xi=2B\) gives the two real identities, and symmetry of \(g\) gives the subtraction of the squared difference with coefficient \(1/4\).
Taking \(f=1\) fixes the mass of \(W\).
The real bound, the triangle inequality for the two real components and \(|\xi|^2\le4W\) give both complex estimates for bounded inputs.
Stone–Weierstrass approximation in \(L^2((1+d+W)\mu)\) consequently passes the polynomial estimate to the very same transform on every bounded Borel input, including indicators.

In the sum of the real adjoint energies over mesh squares the two-variable indicator converges to zero off the null diagonal, and \(g\) is integrable.
For the comparison with the right slice, antisymmetry at a fixed cutoff pairs the same-square indicator with the difference of two values of a Lipschitz test.
Its Lipschitz constant controls the resulting kernel for both limit passages, first removing the cutoff at fixed mesh and then shrinking the mesh.
The real adjoint estimate gives a uniform bound on \(\sum_Q\|C(f1_Q)\|_2^2\), and disjointness bounds the error from replacing \(B\) by the test by a constant times their \(L^2(\mu)\) distance.
Thus the summed cross term tends to zero, as required to recover \(\int d_0 f^2\,d\mu\) also for the right slice.
Testing on indicators yields \(d_0\le C^2d\), including on the zero set of \(d\).
The triangle bound for \(T\) now gives \(3C\) and hence \(18C^2\) for the nonnegative-input curvature form.
Conversely \(g\ge0\) bounds the absolute value of the real form by its value on \(|f|\), and the two real components give the complex bound \(2\sqrt A+\sqrt{2A+K}\) for the slice.
Summing the squared bounds proves the finite-column assertion.

On a straight line every triple has zero curvature.
For normalized disk area the kernel is absolutely integrable and the angular mean of \(1/(z-se^{it})\) is \(1/z\) below \(|z|\) and zero above it.
Integration against \(2s\,ds\) gives the vacuum \(2z\) in the conjugated orientation and \(d_0=|z|^2\).
Outside the radius-\(r\) disk the right slice of its indicator is \(-r^2/z\), yielding annular energy \(2r^4\log(1/r)\) against the mass \(r^4/2\) of the proposed multiplier \(d_0\,d\mu\) on the input disk.
Finally, F0076 fixes the two-variable marginal derivative, and projection of the joint vacuum identifies the actual scalar vacuum by testing pure marginal polynomials.
The trace-preserving conditional expectation of \(D\) has the same pairing with \(|p|^2\) on that algebra, so both necessary tests apply to its compression with the original \(C\).
The external rectifiability and principal-value results underlying Theorem 2 and the previously proved project premises were used at their stated scopes.
The review covers the scalar characterization and the necessary mixed marginal restriction.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0267_v1.md#decision-candidate) | Candidate dated 2026-11-14T13:14 and its four selected direct premises. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0267_v1.md#statement) | Exact real energy, both complex bounds, scalar weight characterization and constants, line and disk conclusions, and necessary mixed marginal condition. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0267_v1.md#argument) | Whole argument including hard cutoffs, positive reweightings, measurable extension and localization, both implications, disk calculation and compression. |
| [Finding](#finding) | [Scalar geometric criterion](../../claims/Yin_C_F0255_v1.md#statement) | Geometric hypotheses from an actual vacuum and scalar bounded-vector domains. |
| [Finding](#finding) | [Tolsa–Verdera energy](../literature/TV06/Yin_U002.md#tv06-u002) | Strong convergence of hard cutoffs and exact energy with the ordered curvature and ordinary arclength normalizations, also after positive reweighting. |
| [Finding](#finding) | [Scalar adjoint orientation](../../claims/Yin_C_F0162_v1.md#1-actual-scalar-operators-and-orientation) | Actual core adjoint and conjugation of the scalar slice on represented polynomials. |
| [Finding](#finding) | [Normal marginal derivative](../../claims/Yin_C_F0076_v1.md#statement) | Forced adjoint-generator symbol and scalar divided difference on the distinguished marginal of the joint derivation. |
