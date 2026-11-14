---
author: Yin
---
# Independent review of the ordered two-block vacuum criterion and atomic obstruction

## Whole-proof finding

At 2026-11-14T10:11 UTC the reviewer independently examined the [statement](../../claims/Yin_C_F0239_v1.md#statement) and complete [argument](../../claims/Yin_C_F0239_v1.md#argument) fixed at the [candidate decision](../../claims/Yin_C_F0239_v1.md#decision-candidate) of 2026-11-14T10:10.
The reviewer had used the normal-coordinate phase and had reviewed a conditional phase estimate in separate work.
The reviewer did not develop this conditional two-block criterion, pole argument or conjugation example and used only the fixed candidate and its stated direct inputs, without access to the proof-development discussion or a prior finding.
All three conclusions hold, including the zero-background case and both endpoints of the unitary trace parameter.

**Disintegration, order and exact norm.**
Left multiplication by \(Y\) and right multiplication by \(X\) are commuting normal operators with commuting spectral measures on the tracial Hilbert space.
Their joint law in the vector \(1\) gives \(\tau(1_E(Y)1_F(X))\), and its marginals are the prescribed spectral laws.
The spectra are compact metrizable spaces.
Taking the Radon–Nikodym functionals on a countable uniformly dense rational star algebra yields one common conull set for linearity, positivity on squares and the sup-norm bound.
Continuous extension, Riesz representation and monotone extension then give the stated probability kernel.
For ordered words, traciality moves \(h_1(X)^*\) past the end of the product and gives the inner product integral of \(\overline{g_1(y)h_1(s)}g_2(y)h_2(s)\).
By Stone–Weierstrass this realizes the Hilbert closure of exactly those represented words as \(L^2(\gamma)\), with all null relations taken into account.
For a fixed polynomial the quotient is uniformly bounded off the diagonal by a first real derivative bound, and even for an atomic \(\nu_y\) the \(\nu_y\otimes\mu\) diagonal has zero mass.
Thus every formal test exists.
For a bounded descended functional, Riesz gives \(H\), and testing against \(g(y)\) shows equality of the two \(L^1(\eta)\) densities for each marginal monomial.
Countability and complex linearity give every star-polynomial test on a common conull set, and conversely (2) pairs every formal sum with \(H\) in \(L^2(\gamma)\).
Density gives uniqueness and the norm equality.
For actual normal coordinates C_F0076 makes the first block's derivative zero and gives \(Dh\) on the second block.
After the left multiplication by \(g(Y)\), the double trace of a simple marginal tensor is exactly its integral against \(g(y)\gamma(dy,ds)\mu(dz)\).
Passage to \(Dh\) is continuous in \(L^2(\mu^2)\) by the marginal property of \(\gamma\) and the boundedness of \(g\).
Hence the resulting functional has the claimed bound by the actual vacuum, and its Riesz vector is the appropriate subspace projection.

**The background density and moving atoms.**
By testing the marginal subspace alone and using the \(\mu\) marginal, (2) gives the global scalar vacuum functional on polynomials with representative \(\zeta\in L^2(\mu)\).
For a Lipschitz test, extend the two real components to the plane and mollify them.
The mollifications have bounded Lipschitz constants and converge uniformly on the compact spectrum.
For each smooth test the \(C^1\) polynomial approximation controls its difference quotient uniformly on the rectangle off the diagonal.
Dominated convergence with respect to \(\mu^2\) gives (4) for the original Lipschitz test.
The product rule \(D(p_y h)=p_y(s)Dh+h(z)Dp_y\) then gives the sign and the variable order in (5).
In particular \(B_y\) has \(L^2(\mu)\) norm at most \(C\|\zeta\|_2+L\).
These functions are jointly measurable by the kernel formula with a prescribed diagonal value.
On the eligible set \(p_y\mu\le\nu_y\) and \(p_y^2\le C p_y\), so \(p_y\overline H\) has the required product \(L^2\) bound even where the density vanishes.

The common polynomial conull set allows tests \(P_yg\) with coefficients depending on the fiber.
At \(s=a_j(y)\) its difference quotient gives the positive coefficient \(P_y(z)g(z)/(z-a_j(y))\), whereas its point value on the right of (2) vanishes.
Multiplication by \(P_y\) first turns each pole into a polynomial factor.
The two sides therefore define finite measures after this multiplication, so equality on all \(g\) implies equality of their densities before division away from the finitely many roots.
Diffuseness of \(\mu\) permits that division without any preliminary absolute integrability assertion about the poles.
On a positive-measure subset one selected weight stays bounded below and its location stays a fixed distance from the other finitely many locations, by countable exhaustion.
There, within half that separation of the first location, the sum of the other pole terms is bounded uniformly because their weights sum to at most one.
Outside the neighborhood the selected pole is uniformly bounded itself.
Equation (6) would then give a finite \(\eta\otimes\mu\) square integral of the isolated pole, weighted by \(\lambda_1^2\).
Its push-forward measure \(\sigma=(a_1)_*(1_E\lambda_1^2\eta)\) is nonzero and dominated by \(\mu\), by the conditional marginal identity and \(\lambda_1^2\le\lambda_1\).
The resulting mixed energy dominates the inverse-square self-energy of \(\sigma\).
On a bounded planar set, an \(O(r^{-2})\)-cell partition and Cauchy–Schwarz give \((\sigma\otimes\sigma)\{|u-z|\le r\}\ge c r^2\sigma(\mathbb C)^2\).
Integration with \(2r^{-3}\,dr\) forces divergence, contradicting the finite mixed integral.
This argument applies on the chosen set regardless of the conditional laws outside it and requires no lower bound on the background.

**Conjugation endpoints.**
For \(w=\tau(w)1+w_0\), traciality and freeness remove both single-centered terms in \(\tau(w g(X) w^* h(X))\).
The term with \(w_0,w_0^*\) gives \(\tau(w_0w_0^*)\tau(g(X))\tau(h(X))\) by centering both marginal factors.
The remainder is \(|\tau(w)|^2\tau(g(X)h(X))\), so the conditional law can indeed be chosen as the asserted atom at \(y\) and the constant-density background.
When \(|\tau(w)|>0\) this satisfies the exact finite-pole hypotheses, including the pure graph at \(|\tau(w)|=1\).
At this last endpoint faithfulness makes \(w\) scalar and \(Y=X\).
At trace zero, both \(w,w^*\) are centered, and substituting conjugated centered elements into an alternating centered word between the two copies yields a centered alternating word between \(W^*(w)\) and the original marginal.
Thus the copies are free without any Haar assumption on \(w\).
Transport of the scalar star-core vacuum to the conjugate copy uses their trace-preserving isomorphism.
For each copy the factor derivation extends by zero on the other copy on the faithful algebraic free product, and reduced centered-word orthogonality proves the actual vacuum there.
Conversely the marginal phase makes the restricted derivative marginal-valued and the projected vacuum gives the scalar adjoint identity.
In the generated tracial algebra of the free pair C_F0162 Part B now supplies the two original canonical operator and adjoint domains and the required bounded-vector commutators.
This establishes the stated conclusion about the conjugation construction while the two-block equivalence itself concerns only the indicated ordered subspace.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0239_v1.md#statement) | Exact ordered-subspace norm, conditional finite-atom obstruction and all three conjugation cases. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0239_v1.md#argument) | Conditional kernel, Riesz criterion, marginal Lipschitz identity, square-integrable background, isolated pole, energy divergence and free endpoints. |
| [Whole-proof finding](#whole-proof-finding) | [Normal coordinate phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, diffuse marginal, zero starred omitted values, marginal difference rule and restriction of an actual pair. |
| [Whole-proof finding](#whole-proof-finding) | [Marginal smooth approximation](../../claims/Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Approximation with both first real derivatives followed by the separate Lipschitz mollification limit. |
| [Whole-proof finding](#whole-proof-finding) | [Critical planar energy](../../claims/Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Compact planar grid estimate and logarithmic divergence for the nonzero diffuse push-forward measure. |
| [Whole-proof finding](#whole-proof-finding) | [Free-core vacuum calculation](../../claims/Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Faithful represented free product and vacuum extension by zero to the other free factor. |
| [Whole-proof finding](#whole-proof-finding) | [Free normal domains](../../claims/Yin_C_F0162_v1.md#statement) | Part B, original canonical strong dual operator and adjoint domains for the two free actual normal coordinates. |
