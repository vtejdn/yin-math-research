---
author: Yin
---
# Independent review of full coordinate domains on disjoint smooth arcs

## Whole-proof finding

At 2026-11-13T17:42 UTC the reviewer independently examined the [statement](../../claims/Yin_C_F0234_v1.md#statement) and the complete [argument](../../claims/Yin_C_F0234_v1.md#argument) fixed at the [candidate decision](../../claims/Yin_C_F0234_v1.md#decision-candidate) of 2026-11-13T17:40.
The reviewer had used the two-Haar column criterion and had checked projective correction for a parabolic change in a different example.
The reviewer did not develop this disjoint-arc theorem and received no development discussion, exploration notes or prior review for it.
The one-coordinate assertion holds with arbitrary spectra for the omitted normal generators, and all five existence conditions in the all-coordinate assertion are equivalent.

**Endpoints, cross-branch secants and multipliers.**
After the disjoint affine placement of the parameter intervals, a compactly supported \(C^3\) extension of \(r\) agrees with the prescribed curve on every interval, using disjoint neighborhoods in parameter space.
For the inverse, at each point a real linear projection with nonzero tangential derivative is locally invertible in the parameter, through the endpoints by the assumed branch extension.
The embedded compact interval is homeomorphic to its image, so each spatial patch can be shrunk to exclude both distant parameters on its own branch and all other branches.
The finite partition of unity therefore gives a real \(C^1\) extension \(h\) with the exact inverse values on the full carrier.
It follows by functional calculus that \(S=h(X_i)\) is selfadjoint and \(r(S)=X_i\), including for partial spectral supports.
The continuous \(J=r^{[1]}\) is nonzero on the compact \(I^2\), by injectivity for distinct parameters, also across branches, and by regularity on the diagonal.
The derivative integral gives two continuous derivatives of \(J\); hence its reciprocal can be cut off on an open neighborhood of \(I^2\) avoiding all zeros.
The periodic extension used for the one-dimensional calculation agrees with the extension of \(r\) on the convex hull of \(I\), so a secant between different intervals is included in the derivative integration formula.
Parseval for three derivatives and Cauchy–Schwarz give \(\sum_n(1+n^2)|c_n|<\infty\).
For the compactly supported reciprocal in two variables, the \(H^2\) Fourier square estimate and \(\sum_{m,n}(1+m^2+n^2)^{-2}<\infty\) give absolute summability.
The separated factors evaluate to bounded operators on the spectrum, yielding both projective multipliers for this particular cover.

**Actual transformed derivation.**
Part 1 of C_F0076 gives the diffuse marginal, closability and the starred phase of the original represented derivation.
Approximation of \(h\) with its first real derivatives on a convex rectangle controls the divided-difference error uniformly off the product-null diagonal by the differential error.
Consequently its polynomial approximants converge both in norm and in the original closed graph, giving \(\bar\delta_i S=K(S\otimes1,1\otimes S)\).
For \(e^{\mathrm i\alpha S}\) and its adjoint the kernel is bounded in coarse norm by \(|\alpha|\|K\|_\infty\) since \(|e^{\mathrm i\alpha s}-e^{\mathrm i\alpha t}|\le|\alpha||s-t|\).
Omitted replacements are similarly norm limits of omitted star polynomials with zero derivatives.
For a finite product of these factors, the graph approximations and their operator-norm bounds pass each outer Leibniz term through the limit.
This defines the restriction on the represented mixed core even though inverse coordinates need not belong to the original star-polynomial core.
The inner action \(I_J\) commutes with the outer actions and sends the marginal \(K\) to the unit tensor.

Expanding the vacuum pairing on \(a^*p b^*\) with exponential unitaries \(a,b\) gives one main term bounded by \(\|\xi\|_2\|p\|_2\) and two derivative terms bounded by \((|\alpha|+|\beta|)\|K\|_\infty\|p\|_2\).
This calculation uses the original graph approximants on both starred factors, so it proves membership in the actual tensor adjoint domain.
The frequencies in each separated term for \(J\) have absolute sum \(|n|\omega\).
Its coefficient already contains \(|n|\omega|c_n|\), so the weighted Fourier estimate sums both graph components of \(I_J^*(1\otimes1)\).
The graph integrals over the interpolation parameter are legitimate by continuity of the exponential factors and their differentiated marginal kernels.
Testing the resulting adjoint vector against the new dense core gives the actual transformed vacuum.
The normalized rules on the full list of mixed starred generators now give algebraic tensor values, reality and coassociativity.
In particular the two iterates cut the same two occurrences in their natural word order, and every other generator and its adjoint have zero derivative.
Relations present no extra descent assumption since the map was already constructed on represented elements.
Mai's Theorem 4.9 therefore gives both slice bounds with constant \(2\|\theta^*(1\otimes1)\|_2\).

**Strong witnesses, the original column and its two domains.**
C_F0072 Part B applies to the weakly dense mixed star core and gives actual bounded-vector domains for the canonical closure and adjoint.
Kaplansky approximation on a fixed ball gives \(L^2\) convergence of both the inputs and their products on the left by a fixed generator.
The restricted slice bounds keep the corresponding canonical outputs bounded.
Using a joint weak cluster subnet and the weakly closed graph therefore passes the polynomial commutator to each bounded input.
Polynomial \(C^1\) approximation of \(r\) on the parameter hull gives \([E^S,X_i]=\Theta(J)\) by the same all-input bound and Hilbert–Schmidt convergence of the kernels.
It gives zero for the other original coordinates whenever they too have been parametrized.
The projective correction \(Q_K(E^S)\) sends that kernel to \(\Theta(1)=P_\Omega\) by \(I_KJ=1\).
On every bounded vector its adjoint series applies the starred right multipliers in reverse order, with conjugate coefficients.
Both series converge by the projective bound and the actual all-bounded-input bounds for \(E^S,E^{S*}\).
Pairing on the dense domain \(M\Omega\) proves actual adjoint membership.
The sign change then gives a strong witness at the distinguished coordinate, or a full strong system if all are covered.

For the original column cost, the preceding construction still supplies a bounded witness for the same distinguished coordinate after freely adjoining the two Haar unitaries.
This uses only the arc cover of that coordinate in the enlarged tuple.
Thus the enlarged optimum is finite and the inequality \(c_i(X)\le4\beta_i(X,U,V)\) controls the full original-core column, with the original canonical right slice.
The adjoint tuple also satisfies actual ACSY by the conjugate companions, and its distinguished spectrum is covered by the conjugate arcs.
Applying that same column argument there bounds its right slice on the identical original star algebra.
Explicitly, on \(a^*\) this slice equals \(((\tau\otimes\mathrm{id})\delta_i(a))^*\), by the flip and adjoint defining the companion.
Both original slices are consequently operator-norm-to-Hilbert bounded.
C_F0072 Part B gives \(M\Omega\) inside the domains of the original right-slice closure and its Hilbert adjoint, and \(E_{i,0}^*=(\overline E_{i,0})^*\).

**All-coordinate converse.**
Under bare full-domain duality for \(X\), C_F0070 Part A and its automatic-continuity interface supply bounded normalized maps with starred commutator kernels on every bounded input.
Applying them to the polynomial approximants to \(h_j\) gives \(\Theta(K_i)\) at the distinguished selfadjoint parameter and zero at the others.
Continuity here uses operator-norm convergence of the inputs and Hilbert–Schmidt convergence of the kernels.
The projective \(J_i\) correction yields bare duals on all bounded inputs for \(S\), with the generator-first sign.
C_F0071_v2 Part B identifies this condition with actual ACSY for the selfadjoint generating tuple.
The forward graph transform proves \(\mathsf A(X)\Rightarrow\mathsf A(S)\), and the actual strong transport gives \(\mathsf A(S)\Rightarrow\mathsf S(X)\).
Strong implies bare by restriction, and C_F0070 Part C supplies \(\mathsf S(X)\Rightarrow\mathsf A(X)\) using the adjoint domains at the unit.
These implications close the asserted chain.
The positive lower secant bound and all multiplier constants are specific to the finite disjoint carrier.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0234_v1.md#statement) | Single-coordinate original column and canonical domains, every implication of the all-coordinate equivalence, and arc geometry including endpoints. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0234_v1.md#argument) | Inverse geometry, secant bounds, vacuum and operator transport, Haar enlargement, conjugate tuple and bare converse. |
| [Whole-proof finding](#whole-proof-finding) | [Normal marginal phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, diffuse, closable original derivations with marginal starred phases and conjugate companions. |
| [Whole-proof finding](#whole-proof-finding) | [Real \(C^1\) approximation](../../claims/Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform polynomial approximation on a plane rectangle with control of the first derivative. |
| [Whole-proof finding](#whole-proof-finding) | [Fourier summability](../../claims/Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | Weighted one-dimensional coefficients of the parametrization and absolutely summable two-variable reciprocal multipliers. |
| [Whole-proof finding](#whole-proof-finding) | [Tensor adjoint](../../claims/Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Exponential graph approximants, actual adjoint vector and frequency-dependent summability. |
| [Whole-proof finding](#whole-proof-finding) | [Projective correction](../../claims/Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) | Inner kernel action, corrected commutators and actual Hilbert adjoint with reversed right multipliers. |
| [Whole-proof finding](#whole-proof-finding) | [Mai's real coassociative estimate](../literature/Mai15/Yin_U002.md#mai15-u002) | Theorem 4.9 on a weakly dense represented star core with algebraic tensor range, actual vacuum, reality and coassociativity. |
| [Whole-proof finding](#whole-proof-finding) | [Canonical domains](../../claims/Yin_C_F0072_v1.md#statement) | Part B on the mixed core and again on the original core, with two bounded trace slices. |
| [Whole-proof finding](#whole-proof-finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Bounded core approximation for extending the canonical commutators to all \(M\Omega\). |
| [Whole-proof finding](#whole-proof-finding) | [Two-Haar enlargement](../../claims/Yin_C_F0208_v1.md#statement) | Preserved actual ACSY and the original-column lower bound on the augmented bounded-dual optimum. |
| [Whole-proof finding](#whole-proof-finding) | [Bare normal duals and vacuum](../../claims/Yin_C_F0070_v1.md#statement) | Parts A and C, all-bounded-input commutators for normalized bare maps and actual ACSY from a full strong system. |
| [Whole-proof finding](#whole-proof-finding) | [Selfadjoint bare converse](../../claims/Yin_C_F0071_v2.md#statement) | Part B, equivalence of bare full-domain duals and actual ACSY on the selfadjoint parameter tuple. |
