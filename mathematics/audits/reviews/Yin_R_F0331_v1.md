---
author: Yin
---

# Independent review of the four-point Gram measure and the three-factor slice

## Finding

On 2026-11-16T17:44 UTC a reviewer outside proof development independently checked the [candidate decision](../../claims/Yin_C_F0323_v1.md#decision-candidate) dated 2026-11-16T17:40.
The reviewer received the fixed proof and its scope without development dialogue or prior findings on this candidate.
The proof establishes the matrix inverse-density identity (1), the bounds (2) and (3) under the stated two-sided hypothesis, and the example with fixed Haar marginal vacua.

The product condition gives \(\mathbb E_A b_i=0\).
When the right slice hits a marginal factor on the left of \(a b_i c\), the right trace of each differentiated leg against \(b_i c\) vanishes.
The same calculation holds for the reverse slice.
The closed omitted-algebra graph and bounded strong-star approximants to \(b_i\) justify the product rule in both orientations.
The approximants converge after multiplication on the vacuum, allowing passage in the closed adjoint graph as well.
Consequently \(E(a b_i c)=a b_i Sc\) and \(E^\#(a b_i c)=a b_i S^\#c\).
Using \(S(cZ)-(Sc)Z=\tau(c)\), testing the difference at \(b_j\) moves right multiplication by \(Z\) to right multiplication by \(Z^*\) on the first argument.
The two adjoint terms are \(b_j\xi Z^*\) and \(b_j Z^*\xi-b_j\).
Their difference represents the functional with value \(\tau(c)\tau(a b_i b_j^*)=\delta_{ji}\tau(a)\tau(c)\), giving (4) with the stated commutator sign.

The joint spectral projection of the commuting left and right marginal actions on the vectors \(b_i\) gives the positive matrix Gram measure with the indicated order of its indices.
The isometry on separated polynomial vectors extends onto \(H\) by density for the finite trace measure and bounded marginal approximation.
Each weighted representative \(h_j\) defines a finite row measure by Cauchy–Schwarz.
Equality against separated polynomials therefore identifies that measure on the full Borel product.
Its singular part is zero as a row measure, so \(h_j\) lies in the null space of the singular density almost everywhere there.
On the absolutely continuous part this gives \(G h_j=\mathbf e_j\) almost everywhere.
The common full-measure set for the finitely many \(j\)'s thus has \(G>0\), and the squared representing norm is \(\int(G^{-1})_{jj}\,d\Lambda\).
Unitarity and the tracial commutator identity give \(\langle b_j,P_H b_j[\xi,Z^*]\rangle=0\).
The representing norm is therefore also \(1+\|P_Hb_j[\xi,Z^*]\|_2^2\).
Summation, with the unnormalized matrix trace and \(\operatorname{tr}\Gamma(\mathbb C^2)=m\), gives (1) including the singular mass and inverse-trace estimate.
Since \(Z\) is normal, \(\|[\xi,Z^*]\|_2\le 2\|Z\|\|\xi-Z\|_2\), which proves the asserted normalized upper bound.

Under \(\ell I\le G\le L I\) and zero singular part, the product Hilbert norm and the represented norm are comparable with constants \(\sqrt \ell,\sqrt L\).
Applying the scalar forward estimate in the terminal variable of \(Uf\) gives exactly \((2+\sqrt2)\sqrt{L/\ell}\) in (2).
Right multiplication corresponds to multiplication by terminal functions, including \(\sqrt W\) by bounded truncations.
For (3) the adjoint test is the vacuum pairing minus \(\langle S_w^\# f,Gh\rangle\), with \(h=U^{-1}P_Hx\).
The subspace \(H\) reduces right multiplication by the marginal.
Thus \(G^2\le LG\) and weighted truncation give \(\|(Gh)\sqrt W\|_{L^2(\Lambda)}\le \sqrt L\|x\sqrt W\|_2\).
Weighted polynomial approximation gives the adjoint estimate for almost every terminal fiber of \(Gh\), which lies in \(L^2((1+W)\mu)\) there.
Integration and \(\|f\|_{L^2(\Lambda)}\le\ell^{-1/2}\|Uf\|_2\) give \(\sqrt{2L/\ell}\) without a dimension factor.
The vacuum term is bounded by \(\|Uf\|_2\|x\xi^*\|_2\), and the test vectors are dense in \(H\).

For the normalized arc laws at \(1,-1\), bounded density controls the maximal linear density, and the curvature of a triple of distinct circle points is one.
The scalar vacuum criterion therefore applies at each positive width.
At \(h(X)=X\) the phase energy is one, giving full actuality and strong duals.
The centered \(V\)-letters in nonzero powers of \(X^*V\) make their expectation onto \(W^*(X)\) zero.
This proves the Borel product condition by normality, and the Haar absorption and exchange calculation applies to this pair.
For \(b_1=Y,b_2=Y^*\), expansion by freeness gives diagonal Gram densities one and off-diagonal entry \(\tau(V^{*2})zw\) with its conjugate transpose.
Consequently the eigenvalues are \(1\pm r\), \(r=|\tau(V^2)|<1\), with \(r\to1\) as the arcs shrink.
Substitution of \(\operatorname{tr}G^{-1}=2/(1-r^2)\) in (1) gives the claimed lower bound \(r^2/(1-r^2)\) for the squared commutator norm.
The polynomial \(XYX-Y^*=(V-V^*)X\) has norm at most \(2\sin\delta\).
Its original first slice is \(XY+\tau(YX)1=V\), a unit vector orthogonal to the first marginal.
This proves the divergence on polynomial contractions with fixed scalar marginal vacua.
The phase-model theorem supplies a uniform bound normalized by the joint vacuum for this particular family.
The eight declared dependencies were checked at these interfaces, and the unrestricted comparison for product two-marginal traces remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0323_v1.md#decision-candidate) | Complete candidate and its eight declared dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0323_v1.md#statement) | Matrix positivity and inverse identity, singular mass, constants and domains in both bounds, degenerating family and its two normalizations. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0323_v1.md#argument) | Commutator test, weighted spectral representation, singular and absolutely continuous fibers, terminal adjoint and direct free-word computations. |
| [Finding](#finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Forward and reversed divided differences and vanishing of omitted generator derivatives. |
| [Finding](#finding) | [Omitted graph](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Bounded omitted factors, zero derivative and joint wordwise graph limits. |
| [Finding](#finding) | [Scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Integrable weight of scalar vacuum mass and the forward and adjoint complex estimates. |
| [Finding](#finding) | [Ordered output pairing](../../claims/Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs) | Actual adjoint pairing, weighted density and duality used on each terminal fiber. |
| [Finding](#finding) | [Scalar actuality](../../claims/Yin_C_F0255_v1.md#statement) | Geometric criterion for the bounded arc densities on the unit circle. |
| [Finding](#finding) | [Phase model](../../claims/Yin_C_F0265_v1.md#statement) | Actuality and full strong duals at unit phase energy. |
| [Finding](#finding) | [Haar exchange](../../claims/Yin_C_F0315_v1.md#actuality-of-the-product-law) | Haar law of \(Y\) and the trace-preserving exchange. |
| [Finding](#finding) | [Joint normalization](../../claims/Yin_C_F0320_v1.md#statement) | Uniform slice bound relative to the joint vacuum on the constructed phase family. |
