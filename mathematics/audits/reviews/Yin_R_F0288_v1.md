---
author: Yin
---

# Review of the product density and the weighted ordered two-block test

## Finding

At 2026-11-14T14:30 UTC an agent outside proof development independently checked the entire [C_F0279 v1 candidate](../../claims/Yin_C_F0279_v1.md#decision-candidate) dated 2026-11-14T14:25 and its three direct dependency interfaces.
The reviewer received the fixed candidate and the review scope without exploration notes, proof-development dialogue, author explanations or previous findings about this candidate.
The proof establishes (1)–(3), the sufficient Lipschitz Gram estimate and the asserted range and graph extensions under the stated hypotheses.

The marginal is diffuse, so \([L,M_{\bar z}]a=\tau(a)1\) follows by cancelling \(\bar z-\bar w\) off the diagonal in the divided difference.
Apply the ordered adjoint pairing first to \(u(1\otimes\bar z),1\), then to \(u,Z\).
Moving the final factor around the trace produces \(\xi^*Z\) in the first term, and \(EZ=1\) gives the constant term in the difference.
The remaining scalar commutator therefore represents the product trace by \(P_K(1+\xi^*Z-Z\xi^*)\) with the claimed order and signs.
The joint spectrum of a finite abelian omitted tuple is compact metrizable, so separated continuous tests determine the finite measure represented by this vector.
In the cyclic ordered model the resulting measure equals \(\lambda\), giving \(r\gamma=\lambda\) and \(\int r\,d\gamma=1\).
Consequently \(\int r^2\,d\gamma-1=\|r-1\|_2^2\), and subtracting \(c1\) from \(Z\) in the commutator gives the coefficient \(4\) in (1).
Disintegration on one countable dense set of continuous tests, including \(1\), yields \(r(y,\cdot)\nu_y=\mu\) almost everywhere, including when \(r\) vanishes on a part of \(\gamma\) singular to \(\lambda\).

For \(t=UL_0u\), spectral truncations give \(\langle t,p\rangle=\langle td^{-1/2},p\sqrt d\rangle\) whenever the first vector on the right lies in \(L^2\).
In the converse, bounded strong-star approximation first gives \(M\sqrt d\) in the closure of \(P\sqrt d\).
The cutoffs \(e_k=1_{[1/k,k]}(d)\) increase to \(1\) and \(me_k=(me_kd^{-1/2})\sqrt d\) for every bounded \(m\), proving density.
The bounded functional gives \(h\in L^2(M)\) with \(h\sqrt d=t\) in \(L^1(M)\) by traciality and normality on the weakly dense core.
Right multiplication by \(e_kd^{-1/2}\) identifies \(he_k=te_kd^{-1/2}\), proving equality of the two optimal constants even for an unbounded inverse.
The second marginal of \(\gamma\) is \(\mu\), so a chosen \(\mu\)-null exceptional set for \(d\) is \(\nu_y\)-null for almost all \(y\).
Tests with an arbitrary omitted indicator localize (2) to each fiber, and rational complex coefficients give a countable determining family.
Coefficient convergence and Fatou's lemma preserve every finite proposed bound on the numerator, including when the denominator vanishes.
This proves measurability and the extended-value convention in (3).
Squaring the two terms in the projected slice estimate gives \(2(\xi^*\xi+C^2d)\), with the factor order fixed by \(\|p\xi^*\|_2^2=\tau(\xi^*\xi p^*p)\).

The scalar adjoint bound, conjugated by \(J\) and dualized against polynomials dense for the finite measure \((1+W)\mu\), gives \(\|Lf/\sqrt{1+W}\|_2\le\sqrt2\|f\|_2\).
Uniform polynomial approximation with bounded Lipschitz constants identifies the divided-difference integral for Lipschitz functions by dominated convergence off the diffuse diagonal.
Parseval gives the same estimate on the separable closed span of the range of a Hilbert-valued Lipschitz function.
The set where \(A\) is invertible is relatively open, and norm continuity of inversion there gives measurability of \(\|A^{-1}\|\).
For \(f=Au\), subtracting \(A(z)L_0u(z)\) from \(Lf(z)\) gives the numerator \((A(z)-A(w))u(w)\) in the commutator integral.
Its norm is at most \(b\int\|u\|\,d\mu\le bD\|Au\|_2\) by Cauchy–Schwarz on the conull invertibility set.
The weighted output norm satisfies this same bound since \(1+W\ge1\).
The Gram identity applied to each finite test converts the resulting constant \(\sqrt2+bD\) to (2).
Bounded strong-star approximation controls right multiplication by both Hilbert factors \(\xi^*,\sqrt d\), while graph approximation controls the right slice.
For \(nan'\), bounded omitted polynomial approximants on both sides preserve graph convergence, and contraction of the second marginal tensor leg leaves the entire output in \(K\).
For arbitrary original columns the bound concerns their projection onto \(K\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0279_v1.md#decision-candidate) | Fixed candidate dated 2026-11-14T14:25 with its direct dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0279_v1.md#statement) | Product density and conditional domination, equality of optimal weighted constants and the abelian formula, integrable inverse Gram condition, graph and range assertions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0279_v1.md#argument) | Complete commutator, measure, weighted-duality, fiber-localization, Hilbert-valued estimate and domain arguments. |
| [Finding](#finding) | [Ordered adjoint pairing](../../claims/Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs) | Equation (6) before any lower Gram bound, bounded graph extension, and range for bounded omitted factors on either side of one marginal polynomial. |
| [Finding](#finding) | [Ordered spectral realization](../../claims/Yin_C_F0239_v1.md#the-ordered-product-space-and-disintegrated-test) | Cyclic ordered isometry and disintegration, applied to the compact joint spectrum of the finite abelian omitted tuple. |
| [Finding](#finding) | [Lipschitz approximation](../../claims/Yin_C_F0239_v1.md#a-lipschitz-density-and-the-atomic-terms) | Real-coordinate polynomial approximation on the compact spectrum with a uniform Lipschitz bound. |
| [Finding](#finding) | [Scalar weighted adjoint](../../claims/Yin_C_F0267_v1.md#statement) | Finite \(W\mu\) and the complex \(\sqrt2\) adjoint estimate on the original scalar polynomial core. |
