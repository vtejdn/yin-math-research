---
author: Yin
---

# Independent review of the uniform slice estimate for measurable phase models

## Finding

On 2026-11-16T17:25 UTC a reviewer outside proof development checked the full [candidate decision](../../claims/Yin_C_F0320_v1.md#decision-candidate) dated 2026-11-16T17:22.
The reviewer received the fixed claim and its scope without development dialogue or earlier findings on this candidate.
The argument proves the absolute column bound on the represented core at each coordinate and in each orientation.
It also proves the stated bound for the single-input supremum of every actual common generating reparametrization in the Haar product model.

The scalar geometric criterion gives finite maximal linear density at \(\nu\)-almost every point with square integral against \(\nu\).
On each bounded-density level set the arc covering argument dominates the restricted measure by a constant times Haar measure.
Arc differentiation then gives \(\int\rho^3\,dm=\int\rho^2\,d\nu\le C\int(M_1\nu)^2\,d\nu\).
I checked the Laurent operator in the published Voi99, Sections 8.7–8.9, printed pp.130–132.
Its tensor formula is \(w(f(z)-f(w))/(z-w)\), so the angular vacuum defined by its double trace is the candidate's \(H\).
With normalized Haar probability and an \(L^3(m)\) density, Corollary 8.8 gives precisely \(3\|H\|_2^2=\int\rho^3\,dm-1\).
This use of the squared norm is invariant under the signed-vector correction in the source unit.
The \(L^3\) boundedness of the circle Hilbert transform is the classical input used there.
The Abel projections converge in \(L^3(m)\), and \(\|g\|_{2,\nu}\le\|g\|_{3,m}\|\rho\|_{3,m}^{1/2}\) transfers that convergence.
On Laurent polynomials the difference cancels the kernel pole uniformly, and bilinear Fourier transposition yields \(H^*=P_-\rho-P_+\rho\) on the support of \(\nu\), fixing the sign independently.
Together these facts give (4), including its representative-independent extension to bounded \(f\).

For each maximal bad arc its parent bounds its mean density by four, and dyadic differentiation bounds the density by two on the complement.
The convex defect \(\phi(r)=r^3-3r+2\) is at least four at every mean \(r\ge2\).
Jensen thus even gives \(4m(D_0)\le\Delta\).
The identity \(\rho^3=\phi(\rho)+3\rho-2\) and the upper bound on the mean give \(\int_{D_0}\rho^3\,dm\le6\Delta\) with the candidate's constants, and Hölder gives the corresponding \(O(\Delta)\) integral of \(\rho^2\).
Averaging \(A_f\) with respect to \(m\) on the bad arcs and keeping its good part costs at most two from \(L^2(m)\) to \(L^2(\nu)\).
The good-input multiplication and negative projection cost at most \(\sqrt2\) from \(L^2(\nu)\) to \(L^2(m)\), proving (5).

For (6), the multiplication term uses \(\int(\rho-1)^2\rho\,dm\le\Delta\).
For the projected bad input, its \(L^2(m)\) and cubed \(L^3(m)\) integrals on the input support are \(O(\Delta)\) on the unit ball of \(L^\infty(\nu)\).
The \(L^3\) projection estimate followed by Hölder on the bad output region therefore contributes \(O(\Delta)\) to the squared output norm.
On each selected arc \(I\) the input \(1_G\rho f\) has uniform bound two.
Its restriction to the triple arc has \(L^3(m)\) norm \(O(m(I)^{1/3})\), including when the triple arc covers the circle.
For the far restriction the difference of kernel values between two points in \(I\) is bounded by the arc length times the inverse square angular distance.
Integration from a distance comparable to the arc length gives an absolute oscillation bound.
Subtracting the mean, summing (7) over disjoint arcs and applying Hölder with \(\int_{D_0}\rho^3\,dm=O(\Delta)\) proves the remaining squared bound.
All estimates use either \(\rho f\) or the value of \(f\) on the support of \(\nu\), so zero sets of the density are allowed.

Centering leaves the \(R_1\) Hilbert norm at most \(\sqrt8\), and the supremum-norm input centering costs at most two for \(R_2\).
The cubic identity converts the \(O(\sqrt\Delta)\) remainder into \(O(\|H\|_2)\).
The earlier terminal factor proof uses precisely these two map norms and the scalar functional represented by \(H\).
The \(R_1\) action on the noise Hilbert leg uses the marginal column estimate on the other leg, costing an absolute multiple of \(\|\xi_\mu\|_2\).
The centered \(R_2\) and scalar outputs cost an absolute multiple of \(\|H\|_2\sqrt J\).
The free reference term adds at most \(36\|\xi_\mu\|_2\), and strong inner cutoff convergence on each finite target column gives the original estimate.
The exact vacuum norm controls the sum by Cauchy–Schwarz for non-Haar \(\nu\).
Haar absorption handles \(\nu=m\) directly even at infinite \(J\).

At \(Y\), rotation gives the actual vacuum \(h^*\xi_V\) and the original column bound \(\sqrt{4/\pi}\,a_V\), where the scalar weight controls \(a_V\) by \((2+\sqrt2)\|\xi_V\|_2\).
Conjugating the adjoint pair implements the same model with the reflected law of \(V^*\) and preserves the respective vacuum norms and phase energy.
For the common reparametrization, actuality supplies the scalar product vacuum, the inverse identifies both marginal algebras, and the original-core transfer and exchange give the claimed single-input bound on all four slices.
The review checked all eleven direct dependency locators and used the previously inspected circle Hilbert-transform theorem at its \(L^3\) scope.
Uniform boundedness for arbitrary exchange-symmetric normal pairs remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0320_v1.md#decision-candidate) | Entire decision and its eleven declared dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0320_v1.md#statement) | Absolute full-column bound for both phase-model coordinates and orientations, and the original single-input cost for the Haar product reparametrizations. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0320_v1.md#argument) | Density and cubic defect, Fourier projections, maximal dyadic arcs, local oscillation, terminal decomposition, cutoff removal, Haar case and transfer. |
| [Finding](#finding) | [Maximal density](../../claims/Yin_C_F0255_v1.md#statement) | Square-integrable maximal linear density for the actual scalar normal vacuum and its circle-density consequence. |
| [Finding](#finding) | [Unitary Fisher information](../literature/Voi99/Yin_U004.md#voi99-u004) | Source operator, normalized Haar convention, \(L^3\) transform input and the cubic squared-norm identity. |
| [Finding](#finding) | [Phase criterion](../../claims/Yin_C_F0265_v1.md#statement) | Base vacuum norm and finite phase energy for actual non-Haar models. |
| [Finding](#finding) | [Rotated coordinate](../../claims/Yin_C_F0265_v1.md#the-rotated-unitary-coordinate) | Right column estimate and actual rotated vacuum at the second coordinate. |
| [Finding](#finding) | [Angular vacuum](../../claims/Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Laurent derivative, double trace, exact \(H\), and vanishing at Haar law. |
| [Finding](#finding) | [Original cutoff](../../claims/Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | Reference constant, actual inner-cutoff convergence on the target core and Haar absorption. |
| [Finding](#finding) | [Adjoint orientation](../../claims/Yin_C_F0265_v1.md#adjoints-and-the-strong-duals) | Conjugation of the adjoint model, reflected density and preservation of the appropriate norms. |
| [Finding](#finding) | [Terminal estimates](../../claims/Yin_C_F0316_v1.md#estimating-all-mixed-words) | The two centered map norms and scalar vacuum bound suffice on full finite columns. |
| [Finding](#finding) | [Marginal bridge](../../claims/Yin_C_F0316_v1.md#the-marginal-kernel-on-a-terminal-base-factor) | Cutoff marginal-kernel identity and uniform column norm in terms of \(\|\xi_\mu\|_2\). |
| [Finding](#finding) | [Scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Single-input scalar unitary slice bound with constant \(2+\sqrt2\). |
| [Finding](#finding) | [Product-law transfer](../../claims/Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Automatic product vacuum, omission of the reparametrized marginal, normal extension, original-core restriction and exchange. |
