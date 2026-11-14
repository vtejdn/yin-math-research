---
author: Yin
---

# Review of the adjoint isometry and scalar column weights at a real coordinate

At 2026-11-14T13:10 UTC, a separate agent reviewed for Yin the whole [fixed candidate of 2026-11-14T13:07](../../claims/Yin_C_F0266_v1.md#decision-candidate).
The reviewer took no part in developing this proof and received its fixed text, the dependency locators and the requested scope.
The review of a different claim, F0264, was visible as a formatting example.
The checks below use F0266 and its five stated inputs.

## Finding

The omitted starred symbols have zero derivative by the normal-coordinate formula, and the real distinguished symbol has derivative \(1\otimes1\).
Thus the derivation has algebraic range on the represented core, respects the adjoint with tensor reversal, and has equal iterated derivatives on each word by cancellation of the two identical cross terms.
The actual vacuum then meets all the hypotheses of Mai's identity.
For \(p\in P\), pairing \(Eq\) with \(p\) for \(q\in P\) identifies \(E^*p=\delta_i^*(p\otimes1)=p\xi-Ep\).
Mai's square identity applies to arbitrary \(p\) and gives the positive quadratic form in the statement with the stated inner-product convention.

For \(q_n\to\xi\) in \(L^2\) with \(q_n\in P\), each functional \(p\mapsto\langle Eq_n,p\rangle\) has an \(L^1\) density.
The bound on \(T\) controls their differences on the polynomial unit ball by \(\|\xi\|_2\|q_n-q_m\|_2\).
The polynomial contractions strongly approximate every contraction in \(M\) by Kaplansky density in \(C^*(X)\), followed by norm approximation and rescaling.
Normality therefore gives the same difference estimate in the predual norm.
The limiting functional is positive by bounded strong-star approximation of square roots, and polarization on \(P\) fixes its normal density uniquely.
At \(p=1\) the identity gives \(\tau(w)=\|\xi\|_2^2\).

The shifted commutator bounds \(|\tau(p)|\) by \(2\|x-\lambda1\|\|p\sqrt w\|_2\) because \(\|(x-\lambda1)p\sqrt w\|_2\le\|x-\lambda1\|\|p\sqrt w\|_2\).
Bounded strong approximation in the normal representation on \(H\) passes both sides to \(M\).
Testing with \((w+\varepsilon1)^{-1}\) bounds its trace uniformly by \(4\|x-\lambda1\|^2\), so a kernel projection of positive trace is impossible and monotone convergence gives the inverse bound.
The spectral cutoffs in F0211 then give both density of \(P\sqrt w\) and its trace pairing with \(w^{-1/2}\).
The isometry is consequently unique, and on this dense subspace its commutator is the bounded rank-one operator in (1), including the minus sign.
For omitted polynomials \(q\), the equations \(Eq=0\) and \(Tq=q\xi\) give, respectively, orthogonality of the range to \(L^2(N)\) and equality of the two square functionals on \(N\).
Left multiplication of (1) by \(V^*\) proves the compressions since \(V^*\Omega=0\).
The triangle inequality for \(p\xi-Tp\), followed by summation, gives the simultaneous column estimate.

Testing the vacuum against scalar polynomials gives the actual marginal adjoint required in F0255.
On each set of bounded maximal linear density, covering a Lebesgue-null set by intervals of arbitrarily small total length forces its restricted mass to vanish.
These sets have full measure in union, and Lebesgue differentiation then bounds \(4\int\rho^3\,dt\) by \(\int(M_1\mu)^2\,d\mu\).
The Voi98 source unit applies with this compactly supported \(L^3\) density and fixes the normalization \(\mathbb E_B\xi=2a\).
Uniform approximation of the derivative of \((z-t)^{-1}\) on a real interval containing the spectrum gives uniform approximation of both the function and its divided difference.
This justifies both adjoint pairings and evaluation of the normal energy functional on the resolvent.
The divided difference is \(p_z\otimes p_z\), so contraction gives \(F(z)p_z\), and vacuum pairing gives \(\tau(\xi p_z)=F(z)^2\).
Thus the cubic is subtracted in the Stieltjes transform of the \(w\)-measure.
The \(L^3(dt)\) boundary limit yields \(L^1(dt)\) convergence of the cubes, while the imaginary parts of the two measure transforms converge by Poisson approximation.
Computing the imaginary part gives \(\mathbb E_B w=\mathbb E_B\xi^2-3a^2+\pi^2\rho^2\) in \(L^1(\mu)\).
In the expansion of \(\mathbb E_B((\xi-2a)^2)\), the two mixed products pass from bounded truncations of \(a\) by \(L^2\)-to-\(L^1\) Hölder and the conditional bimodule identity.
This gives exactly (2), including for a noncommuting \(\xi\).

In the scalar case the energy identity and \(|\xi|^2=4a^2\le4w_0\) give the factor \(3\) before squaring in (3).
For the converse, polynomial \(C^1\) approximation preserves the input norm for every integrable \(d\) and the divided difference in the output.
Regularization gives \(Ef=fa-\pi H_{\mathbb R}(f\rho)\), with the divided difference bounded by the Lipschitz constant and the regularized transforms convergent in \(L^2(\mu)\) by \(L^3(dt)\) convergence.
For a Schwartz function with compact Fourier support the shifted Hilbert multiplier is identically \(-i\) on that support for sufficiently large positive modulation.
Density and the uniform \(L^3\) operator norm extend this limit to \(\phi\rho\), giving limiting squared modulus \(|\phi|^2w_0\) in the integrated test.
Smooth approximation of square roots of continuous positive tests on the compact support yields the measure order \(w_0\,d\mu\le C(d)^2d\,d\mu\) whenever the constant is finite.
Consequently an unbounded ratio, including a zero of \(d\) on a positive-measure set where \(w_0>0\), rules out a finite constant.
Column sums preserve the scalar constant, and testing a correlated tuple on scalar polynomials replaces \(d\) by \(\mathbb E_Bd\) through the trace pairing.
The whole candidate is supported under the stated hypotheses.
The external source results were used at their recorded interfaces, including the \(L^3\) Hilbert-transform theorem.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0266_v1.md#decision-candidate) | Candidate dated 2026-11-14T13:07 with its five selected dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0266_v1.md#statement) | Unique normal energy density and isometry, support and inverse estimate, commutators and compressions, conditional densities and scalar and marginal weight tests. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0266_v1.md#argument) | Entire argument from the represented real derivation through the normal extension, resolvent computation, oscillatory localization and finite columns. |
| [Finding](#finding) | [Normal starred symbols](../../claims/Yin_C_F0076_v1.md#statement) | Actual starred coordinate symbols on a bounded normal generating tuple with the stated vacua. |
| [Finding](#finding) | [Real coassociative energy](../literature/Mai15/Yin_U002.md#mai15-u002) | Adjoint formula, reality, polarized norm identity and operator-norm bound on the weakly dense algebraic core. |
| [Finding](#finding) | [Weighted commutator argument](../../claims/Yin_C_F0211_v1.md#faithfulness-inverse-integrability-and-the-bounded-implementer) | Cutoff proof of weighted polynomial density and inverse-square-root trace pairing. |
| [Finding](#finding) | [Geometric scalar criterion](../../claims/Yin_C_F0255_v1.md#statement) | Necessary maximal-linear-density estimate for the actual scalar vacuum. |
| [Finding](#finding) | [Scalar Hilbert transform realization](../literature/Voi98/Yin_U002.md#voi98-u002) | Normalization of the vacuum, Poisson regularization, Fourier multiplier and \(L^3\) boundedness. |
