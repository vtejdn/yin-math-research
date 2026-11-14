---
author: Yin
---
# Independent review of dyadic column bounds for a normal divided difference

## Whole-proof finding

At 2026-11-14T10:43 UTC the reviewer independently checked the [statement](../../claims/Yin_C_F0242_v1.md#statement) and complete [argument](../../claims/Yin_C_F0242_v1.md#argument) fixed in the [candidate decision](../../claims/Yin_C_F0242_v1.md#decision-candidate) of 2026-11-14T10:41.
The reviewer had independently reviewed the marginal packing theorem C_F0233 and had previously used two-Haar encoding and the normal companion derivation.
The reviewer did not develop the measurable-block identity, dyadic estimates or example in C_F0242 and consulted its fixed text and fixed inputs without reading the exploration draft or receiving development discussion or a prior finding.
Both dyadic estimates, their logarithmic consequences, the conditional canonical-domain assertions and the scalar example hold.

**The Borel block and its column estimate.**
The recovery theorem gives \(\eta=[Z^*,\xi]\), \(\gamma=I_u\delta\) on the represented core, and the exact identity \(V^2=\int_{u\ne0}|u|^{-2}d\nu\).
Multiplication of \(\eta\) by \(-i\) preserves its vector spectral measure.
For \(q=e\otimes e\) with \(e\in N\) a Borel spectral projection, the two marginal corrections in the real liberation adjoint are both \(te\), so the adjoint vector is \(e\zeta e\).
The weighted marginal tensor adjoint applies to this bounded symmetric kernel.
Independently of continuity of the indicator on \(K\), bounded marginal polynomial approximants to \(e\) converge strongly-star and in \(L^2\).
Their liberation derivatives converge by the formula \(n\otimes1-1\otimes n\), and the bounded outer factors converge strongly on the coarse correspondence.
This is enough to put the finite-kernel words and their iterates on the enlarged algebraic core specified in C_F0077.
It does not impose a graph condition on the original distinguished derivative of a discontinuous projection.

In (B0c) the first imaginary part for a unitary \(v\) equals \(t\operatorname{Re}\langle v,G_ev\rangle\), since \(G_e(v)e=G_e(v)\) and traciality cycles the initial \(e\) past the other factors.
Also \(q\circ q=tq\), so the second imaginary part has exactly the same value.
The coefficients in (B0c) are \(-2,+1\), and (B0e) subtracts the resulting real part.
This gives the positive sign on the right of (4).
The signed analytic unitaries built from a strict selfadjoint core contraction satisfy the identity by the convergent binomial first-derivative estimates.
Right support permits replacing \(v\) by \(ve\) in the last pairing, with \(\|ve\|_2=\sqrt t\).
Bounding the other pairing by \(\|G_ev\|_2\|e\eta e\|_2\) gives the coefficient \(2\|e\eta e\|_2+t^{3/2}\).
Averaging the two signs and scaling gives this constant on selfadjoint inputs, and splitting real and imaginary parts gives a factor of two on the full core.

The two-Haar free extension preserves the old distinguished vacuum and hence the old liberation commutator vector, while the new Haar letters and their adjoints have zero derivative.
Encoding an old column multiplies its input norm by at most two, and freeness makes the translated old Hilbert outputs mutually orthogonal.
The preceding arbitrary-input bound thus gives the column constant \(4(2\|e\eta e\|_2+t^{3/2})\) in (5).
For \(e\perp f\), expanding \(G_{e+f}\), subtracting \(G_e\) and multiplying on the right by \(e\) leaves just \(G_{ef}\), because the first inner factor determines the right support after the trace slice.
This step uses orthogonality in \(N\) and works without centrality in \(M\).
The smaller compression \(e\eta e\) is itself a two-sided compression of \((e+f)\eta(e+f)\), which proves (6) for each orientation, with the same bound also in the repeated case.

**Annular estimates and summation.**
The radial cutoffs telescope to one for \(0<|u|\le D\).
After dilation the unregularized symbol has Fourier variation \(O(1/\rho_j)\).
For the regularized symbol, on the fixed annulus its derivatives through order four are \(O(\min(1,(\rho_j/r)^2))\), so applying \((1-\Delta)^2\) gives an integrable Fourier bound in dimension two, with the same dilation factor.
Each character of the difference variable factors into two continuous marginal unitaries.
For a fixed column the multiplier identity has its right multiplier on both output terms.
Norm approximation of the second factor controls the column of \(p_kw\) by \(\|w\|\|\sum p_k^*p_k\|^{1/2}\), while the column with common vector \(G(w)\) uses the positive sum \(\sum p_k^*p_k\).
Integration against the Fourier measure thus costs at most twice the block norm times the total variation.
Since the first Fourier factor commutes with \(e\), all these outputs still lie in \(He\).

For each first grid square only a bounded number of second squares can occur, and the same holds with their roles exchanged.
Orthogonality in the first index and Cauchy–Schwarz in the second give a constant times the sum of squared block costs for the squared shell cost.
The diameter of a neighboring union is at most \((2+2\sqrt 2)\rho_j\).
Each ordered pair of points belongs to only a bounded number of the corresponding union squares in the product space, including when the two points are in the same grid square.
The sum of the squared compressions is therefore bounded by a constant times the stated punctured near-diagonal \(\nu\)-mass, because \(\nu\ll\mu^2\) and \(\mu\) is diffuse.
The contribution from projection traces is bounded by a constant times \(\sum_e\tau(e)^3\) using \((s+t)^3\le4(s^3+t^3)\).
This sum is bounded above by \(\int\mu(\overline B(z,8\rho_j))^2d\mu(z)\) since each square lies in the indicated ball at each of its points.
For the reverse bound each ball intersects only a bounded neighborhood of the square of \(z\), and summing the products of masses uses \(3st^2\le s^3+2t^3\).
Together these prove (7) and allow the packing theorem with radius \(\sqrt2\rho_j\) at each square's center to give \(\sup_j b_j\le C\|\xi_N\|_2\).

For every \(x>0\) the geometrically increasing weights \(\rho_j^{-2}\) summed over \(x\le8\rho_j\) have total \(O(x^{-2})\).
Tonelli gives \(\sum_j a_j^2\le C V^2\).
Both \(\sum m_{j,r}\) and \(\sum m_{j,r}^2\) are \(O(1+\log_+(D/r))\) by counting the unit weights and summing the geometric tail, also for \(r\ge D\).
The marginal contribution consequently grows at most as \(L_r\), and the liberation contribution grows at most as \(\sqrt{L_r}\) by Cauchy–Schwarz.
For the actual slice limits, the partial shell symbols applied to \(\delta(p)\) are bounded by one and tend to one off the diagonal.
Every coarse vector's inner spectral measure is absolutely continuous with respect to \(\mu^2\), so dominated convergence gives convergence on each input, jointly on each finite column.
The regularized limit has the additional bounded factor \(|u|^2/(|u|^2+r^2)\).
Taking the column supremum after the finite-column limits establishes both shell-sum statements, including their extended-real interpretation for \(E\).

In (3) the restriction \(x\le8\rho_j\) implies \(1+j\le C(1+\log(D/x))\).
The same geometric summation then bounds \(\sum(1+j)^{1+\epsilon}a_j^2\) by the weighted energy and scalar Cauchy–Schwarz gives \(\sum a_j<\infty\).
For sufficiently large \(j\), substitution of \(s=8\rho_j\le D/2\) into the growth bound gives \(b_j=O((1+j)^{-1-\epsilon})\).
The finitely many remaining terms are finite.
On adjoint generators the companion gives the same algebraic liberation \(\gamma\), and the joint measure is conjugated in both variables.
Distances, ball masses, and the two numerical sequences are therefore unchanged.
The companion right slice at the adjoint input is the tracial involution of the original left slice.
Boundedness of both original one-input slices gives the actual canonical closure and adjoint domains by C_F0072 Part B, and the bounded rank-one commutator passes to graph limits with the required sign.

**The logarithmic example.**
The displayed distribution function starts at zero and reaches one at \(e^{-5}\).
Its density \(375/(y\log(1/y)^4)\) is decreasing there, so the maximal mass of an interval of length \(2s\) lies at the lower endpoint.
Independence of the horizontal uniform variable then bounds each ball by \(Cs/(1+\log(D/s))^3\) at small scales, and enlarging the constant covers the other scales in (3).
The indicated rectangle lies inside the radius-\(s\) ball centered at \(1/2\) and gives the stated lower bound \(s(5/\log(2/s))^3\).
It exceeds every fixed multiple of \(s^\alpha\) along sufficiently small radii for \(\alpha>1\).
The uniform annular bounds sum to a finite absolute inverse-distance integral since \(\sum(1+j)^{-3}<\infty\).
Thus the scalar represented marginal derivative has an actual bounded vacuum given by the conjugate of twice the indicated Cauchy integral, with the sign following by transposing the two variables in the second term.
The one-coordinate liberation vacuum is zero, so the weighted energy assumption holds identically.
The example satisfies (3), for instance with \(\epsilon=2\), while violating the earlier uniform power-growth hypothesis.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0242_v1.md#statement) | All column and logarithmic estimates, the sufficient endpoint criterion, adjoint orientation and scalar example. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0242_v1.md#argument) | Projection-square identity, Haar encoding, Fourier kernel bounds, both shell measures, geometric summation, actual domains and example. |
| [Whole-proof finding](#whole-proof-finding) | [Liberation recovery](../../claims/Yin_C_F0238_v1.md#statement) | Exact distinguished vacuum splitting, inverse-gap energy and the actual liberation. |
| [Whole-proof finding](#whole-proof-finding) | [Coarse inner calculus](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Inner action, domination of vector measures by \(\mu^2\) and recovery off the diffuse diagonal. |
| [Whole-proof finding](#whole-proof-finding) | [Column multiplier identity](../../claims/Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Right slice of a separated kernel, norm approximation and the two column estimates. |
| [Whole-proof finding](#whole-proof-finding) | [Marginal liberation adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Actual adjoint at \(e\otimes e\), cancellation of equal marginals and absolute continuity of \(\nu\). |
| [Whole-proof finding](#whole-proof-finding) | [Finite-kernel graph and energy](../../claims/Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Borel graph approximation, (B0c) and (B0e) and binomial first-derivative limits. |
| [Whole-proof finding](#whole-proof-finding) | [Two-Haar vacuum extension](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Preserved actual coordinate vacuum and zero new-letter derivatives. |
| [Whole-proof finding](#whole-proof-finding) | [Finite-column encoding](../../claims/Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Factor two for the encoded input and orthogonality of the old Hilbert outputs. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar marginal packing](../../claims/Yin_C_F0233_v1.md#statement) | Part 1 with distinct square centers, giving the uniform mass-cube bound proportional to \(\|\xi_N\|_2^2\). |
| [Whole-proof finding](#whole-proof-finding) | [Adjoint companion](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, the original and companion starred values, actual vacua and diffuse marginals. |
| [Whole-proof finding](#whole-proof-finding) | [Two-slice domain theorem](../../claims/Yin_C_F0072_v1.md#statement) | Part B for the bounded-vector domain of the original canonical closure and actual adjoint. |
| [Whole-proof finding](#whole-proof-finding) | [Power-growth comparison](../../claims/Yin_C_F0078_v1.md#statement) | Scope of the marginal power-growth hypothesis excluded by the example. |
