---
author: Yin
---

# Review of strong duals and product-algebra curvature for reparametrized Haar marginals

## Finding

At 2026-11-16T17:07 UTC a separately assigned agent for Yin independently checked the complete C_F0315 v1 candidate fixed at 17:05 UTC.
The reviewer did not develop this proof and received the fixed candidate and its dependency locators without development dialogue, exploration notes, author explanations or prior findings on this candidate.
The scalar product vacuum, the identities (2) on both product algebras, the strong domains on the original represented core and all three quantitative bounds hold.

Absorption makes \(Y^*=V^*X\) Haar and free from \(V\).
Conjugating the free pair \((Y,V)\) by \(Y\) gives \((Y,YX)\) with the same joint law as \((X,V)\).
These substitutions generate the whole algebra and interchange \(X\) and \(Y\), so their trace-preserving extension has order two.
The common measurable inverse recovers both original Haar marginal algebras.
Bounded marginal approximants converge in the liberation graph at each of \(X,Y\) and their adjoints, with the two values at \(V\) stated in (3).
The kernel propagation calculation applies to \(V-\lambda\) since fixed resolvent polynomials in these graph-approximable letters have the same product rules and limits.
At an atom its compressed double trace for \(\gamma_0\) would be \(-\lambda\tau(e)^2\), since \(\tau(eX)=0\).
A unitary eigenvalue has modulus one, so this proves diffuseness.
For Laurent \(f\) the identity \(w d_{f/v}(v,w)=d_f(v,w)-f(v)/v\) and freeness compute the double trace of \(\gamma_0((f/v)(V))\).
Pairing with the liberation vacuum gives the bounded functional on \(f(V)\) of norm at most \(1+\|\eta_0\|_2\).
Diffuseness makes the divided difference independent of the representative, and density of the Laurent polynomials establishes the actual scalar vacuum.

For \(u=f(V)\) in a liberation graph, multiplication of the polynomial approximants to \(u\) on either side of \(\gamma_jV\) converges with just their \(L^2\) convergence, since (3) uses bounded simple tensors.
The commutator with \(V\) therefore has zero graph value in the limit on the input side and yields the divided-difference equation on the derivative side.
The two outer spectral actions on coarse tensors have measure class dominated by \(\nu^2\).
The cutoff recovers \(\gamma_j u\) in norm by that equation and diffuseness, with no smoothness condition on \(f\).
For an elementary inner tensor \(a\otimes b\) the first matched coefficient is \(\tau(Xa)\tau(bX^*)-\tau(a)\tau(b)\), evaluated in the \(X\)-marginal.
The second is \(\tau(a)\tau(b)-\tau(Y^*a)\tau(bY)\), evaluated in the \(Y\)-marginal.
These factorings use freeness from \(V\) on the respective marginal, including the ordered factors \(Y=X^*V\) and \(X=VY^*\).
Symmetry of \(q\) makes the two coefficients \(-c_q,c_q\).
Normality on each spectral square allows general bounded inner kernels and the bounded outer cutoff.
The sum contains the factor \(\overline{f(v)}(f(v)-f(w))\), whose integral is \(1-|\tau(u)|^2\).
The sum of the two graph derivatives at \(u\) is the inner difference by the same cutoff, and its insertion at \(q_1\) has expectation term \( |\tau(u)|^2\int q\,dm^2\) by freeness.
Subtracting its full contribution gives the minus sign in the second identity.
Exchange carries the matched sum to \(W^*(YX)\), where the same conditional expectations are scalar.
For analytic tests the truncations of the pulled-back curvature kernel pass to the signed scalar limit by integrability and \(\iint g\,d\mu^2\le2\|\xi_\mu\|_2^2\le2s^2\).
This gives \(D(u)\ge-2s^2\) on the stated product algebras.

For \(Z=F(X)\), approximating \(Y,Y^*\) from their omitted algebra extends the actual distinguished derivative at \(Z\) to the \(Z,Y\) core with the same vacuum because this core stays weakly dense.
The rotated-coordinate construction supplies the second actual vacuum using \(\xi_V\), so the phase criterion applies.
In the reverse transfer, polynomials in \(Y,Y^*\) approximating the omitted \(F(Y)\) have zero distinguished derivative.
Their bounded strong-star word approximants have the same limiting differentiated tensors.
The normal bounded slice for \(Z,Y\) takes these inputs to the correct weak limit, so its norm on the whole von Neumann algebra bounds the original right slice even if the approximating polynomial norms exceed the norm of the limiting word.
The flip-adjoint argument transfers the left slice bound by using the reversed orientation.
The two-slice theorem puts every bounded vector in both canonical domains, and graph approximation extends the core generator commutators with the generator-first sign after negating the closure.
Exchange supplies the other coordinate.

For non-Haar \(V\) the phase criterion gives \(\|\xi_\mu\|_2\le s\), \(\sqrt J\le s/\|H\|_2\), and \(\|\xi_V\|_2=\sqrt{1+\|H\|_2^2}\) by centering of \(H\).
Dividing the column bound by \(s\) bounds the reference contribution by \(36\), the angular contribution by \(2\), and the remainder by \(2\sqrt{4/\pi}((2+\sqrt2)\sqrt{1+h^{-2}}+h^{-1})\) for \(\|H\|_2\ge h>0\).
Conjugating the adjoint tuple as in the phase criterion preserves the vacuum norms and the phase energy, since the scalar vacuum is in \(W^*(V)\).
For Haar \(V\) the two marginal algebras are free, giving \(3\) directly.
For Poisson center \(a\) the rotated disk automorphism gives free Haar \(V_0\), and absorption makes \(W=X^*V_0\) Haar free from \(W^*(X)\).
In the disk model \(h^*W=\bar a V_0\), so the output simplifies to \(X^*(a+V_0)(1+\bar a V_0)^{-1}=Y\).
Its base squared vacuum is \(s^2=\|\xi_\mu\|_2^2+2J_{\rm M}\), giving \(3c_0+4K\sqrt{2J_{\rm M}}\le(36+4K)s\) in both orientations.
This estimate is independent of the center, including \(a=0\), and of the generating map \(F\).

The review covered the eleven dependency interfaces at their stated uses.
An upper bound uniform over arbitrary non-Haar product laws as \(\|H\|_2\) tends to zero remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0315_v1.md#decision-candidate) | Fixed decision of 17:05 UTC with both identities, all domain and cost assertions, and declared inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0315_v1.md#statement) | Exchange, scalar vacuum, strong domains, product-unitary curvature identities and the three quantitative bounds. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0315_v1.md#argument) | Whole proof from recovery of the product vacuum through both graph-domain calculations and both orientations of the estimates. |
| [Finding](#finding) | [Exchange curvature criterion](../../claims/Yin_C_F0314_v1.md#statement) | Analytic unitaries, signed cutoff limit and the conditional expectation contribution from the inner difference. |
| [Finding](#finding) | [Phase model](../../claims/Yin_C_F0265_v1.md#argument) | Haar absorption, full actuality on the rotated core, the squared vacuum identity, explicit mixed column bound and its adjoint transfer. |
| [Finding](#finding) | [Marginal graph](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Bounded strong-star approximation in the marginal liberation graph and multiplication on coarse tensors. |
| [Finding](#finding) | [Kernel propagation](../../claims/Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Resolvent proof of the zero outer compression by the left and right kernels of a graph-approximated normal element. |
| [Finding](#finding) | [Liberation adjoint](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | The commutator vacuum representing the double trace on the closed liberation graph. |
| [Finding](#finding) | [Scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Curvature integral at most twice the squared marginal vacuum norm and scalar right-slice bound \(2+\sqrt2\). |
| [Finding](#finding) | [Normal slice extension](../../claims/Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Same-norm ultraweak-to-weak extension from the core for an actual bounded right slice. |
| [Finding](#finding) | [Two-slice theorem](../../claims/Yin_C_F0072_v1.md#statement) | Both bounded-vector domains for the closure and actual Hilbert adjoint on the original core. |
| [Finding](#finding) | [Free normal estimate](../../claims/Yin_C_F0162_v1.md#statement) | Original right and left contraction bounds by three times the vacuum norm for freely independent marginals. |
| [Finding](#finding) | [Poisson transform](../../claims/Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Haar image under the disk automorphism, extended to a complex center by circle rotation. |
| [Finding](#finding) | [Disk model](../../claims/Yin_C_F0290_v1.md#argument) | The Möbius output, base vacuum norm and uniform four-Haar-derivative column bound in both adjoint orientations. |
