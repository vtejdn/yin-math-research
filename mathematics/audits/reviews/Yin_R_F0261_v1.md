---
author: Yin
---

# Independent review of the two-graph column estimate with a closed tangential contact set

For Yin I examined the complete [candidate of 2026-11-14T11:41](../../claims/Yin_C_F0252_v1.md#decision-candidate), including its limiting cases and all direct dependencies at the scopes below.
I took no part in developing this version and received no development dialogue, author explanation, exploration notes or previous review conclusion about it.
I had previously reviewed the fixed power-order tangency theorem and examined the present proof of the closed-contact-set extension independently.

## Finding

At 2026-11-14T11:43 UTC I found that the candidate proves the finite original right-column bound, its adjoint-tuple version, both stated bounded-vector domains and the generator-first commutator.
The result permits arbitrary mass on the closed contact set, including a contact set with infinitely many complementary intervals.

At a zero of \(k=(f_1-f_2)/2\), differentiability with \(k'=0\) gives \(|k(x+t)|=o(|t|)\), including at an interval endpoint with the allowed one-sided increments.
At two points of opposite sign split their distance at an intervening zero to estimate the sum of the absolute endpoint derivatives by \(\operatorname{Lip}(k')|x-y|\).
For points with the same nonzero sign the Lipschitz bound on \(k'\) suffices, even if there is a zero in between.
Thus \(d=|k|\) and both sorted graphs have Lipschitz derivatives.
When \(F=I\) one BV graph covers all mass, and when \(F\) is empty the minimum distance between the two compact planar graphs is positive.

On a complementary component, a full step has length \(c d(x)\) and all its heights are within the relative error \(c\operatorname{Lip}(d)<1/4\) of its initial height.
The distance to a zero end exceeds that step, and a limiting point with positive height would contradict convergence of the step lengths to zero.
At most two shortened tiles at exterior ends need separate constants in (3), each finite since its length and minimum height are positive.
The excluded tile endpoints on the noncontact graphs form a countable null set.
The scaled contact set \(10F\) remains assigned to the upper graph, so no diffuseness argument is applied to \(F\) itself.
Each of the three interpolation gaps in a tile has length at least \(\ell\), and its endpoint values are at distance \(O(\ell)\) by (3).
The global Lipschitz estimate holds across infinitely many components by splitting at the first and last contact between the test points and using the midline estimate directly between those contacts.
On the assigned labels the decoded map is one-to-one and Borel with Borel inverse, including on \(10F\).

These facts suffice for the real parameter law and its actual mixed-core derivative.
The image of each occupied mesh cell lies in a disk of radius at most the mesh times the decoder's Lipschitz constant.
The images are disjoint, so the scalar packing estimate with separate centers gives uniform \(L^3\) bounds for the histograms.
Weak identification of the density gives the real scalar vacuum.
The joint liberation vector gives no mass in either leg to an exceptional spectral set, and its inverse real-gap integral is bounded by the squared forward Lipschitz constant times the original inverse-gap integral.
The other coordinates have the same marginal algebras, liberation vacua and energies under the relabelling.
This gives the actual parameter tuple to which the original real-coordinate column estimate applies.

For the height estimate, the constant extension at a zero boundary and the short linear extension at a positive boundary both give nonnegative \(C^{1,1}\) collars.
At \(x-d'(x)/M_1\) the Taylor upper estimate is at most \(d(x)-|d'(x)|^2/(2M_1)\) when \(M_1\ge\operatorname{Lip}(d')\) on the collar.
This proves a uniform derivative bound for \(\sqrt d\) on positive components and hence its Lipschitz bound across intervening zeros.
A cell hull meeting \(F\) has \(D_*=\sup_J d\le\operatorname{Lip}(d')|J|^2/2\) by expansion at a contact.
Nonneighboring horizontal cells have positive planar separation.
On a common hull disjoint from \(F\), coincidence of two branch points would require \(x=y\) and \(2d(x)=0\), so the compact branch pieces also have positive separation.
The positive-distance reciprocal estimate therefore handles these pairs.

On a remaining hull put \(m=g'(x_0)\) and \(p=1+im\).
The cutoff of the rescaled slope minus \(m\) has periodic \(H^1\) norm \(O(|J|\operatorname{Lip}(g'))\), using the constant continuation at a parameter boundary.
Summing its absolutely convergent Fourier series along the convex interpolation of \(x,y\) gives the same Schur bound for \(G-m\) for any two branch measures.
Factoring \(1+iG=p(1+i(G-m)/p)\) proves the asserted estimate for \(K_0\) uniformly over the selected hulls.

For \(D_m=pv+iw\), the integral of the exponentials in (6) without their square-root weights is \((w/p-iv)^{-1}\).
Multiplication by \(-i/p\) gives exactly \(1/D_m\).
Here \(\operatorname{Re}(1/p)=|p|^{-2}\), so each weighted factor has \(L^2(d\lambda)\) norm \(|p|/\sqrt2\) and the prefactor has modulus \(|p|^{-1}\).
The product bound is therefore \(|p|/2\) with either sign of \(m\).
A real orthonormal basis of \(L^2(d\lambda)\) gives the bilinear separated expansion with the required square sums, so the complex exponents in the second leg require no change of slope.
On comparable positive bands the square-root ratios have uniformly bounded separated costs.
Multiplying the weighted resolvent by these ratios gives bounds for \(w/D_m\) and, since \(|\epsilon_j|\le C_1d\), for the coding-error quotient.
The identity \(pv/D_m=1-iw/D_m\) and a small mesh give the norm-convergent Neumann inverse of \(1+i(G-m)v/D_m\).
These estimates hold at \(x=y\) as well since \(w>0\) on the cross rectangle.
Each fixed comparable offset acts on disjoint row and column projection blocks, giving a uniform operator bound for their countable direct sum.

In a separated-height rectangle the square-root Lipschitz estimate gives \(|x-y|\ge b\sqrt\delta\) for either ordering of the horizontal variables.
The scaled smooth cutoff of \(1/(x-y)\) has Fourier \(L^1\) cost \(O(\delta^{-1/2})\) because \(\chi(t)/t\in H^1(\mathbb R)\).
Here \(w\) and the difference of coding errors have separated costs \(O(\delta)\).
Factoring \(D=vK_0^{-1}(1+iK_0 w/v)\) gives (7) with the negative sign on \(10iK_0 w\) and with a uniformly convergent reciprocal.
The \(O(\sqrt\delta)\) remainder is summable over height bands before the baseline \(10K_0\) is added once.
If \(x\in F\), then \(d_x=\epsilon_U(x)=0\), and every \(d_y>0\) belongs to precisely one higher band on the lower leg.
These product rectangles satisfy the same estimates, regardless of the upper measure of \(F\).
When \(D_*=0\) there is no lower leg in the hull.
The uniformly bounded truncated symbols act strongly on coarse vectors by domination by the product law.

Graph approximation of the forward decoder and its conjugate places \(Z,Z^*\) in the parameter derivation graph, and the product rule gives graph approximants to the original mixed words.
Applying the joint column cutoff before the bounded kernel insertion retains limit superior of the input norm at most \(1+\varepsilon\) for a unit original column.
The inserted forward difference at \(Z\) is the rectangle projection, and its value at \(Z^*\) is the same projection times \((\bar z-\bar w)/(z-w)\).
The product rule then identifies the restricted original derivation, including omitted letters, and the inverse rotation factor gives the same normalization in the initial axes.
Transposition exchanges the branch measures and gives the reverse cross bound.
For each same-branch restriction the two separated real copies are injective on their assigned Borel subsets.
The full graphs filling the unused parameter points provide the Lipschitz decoder and the single selected graph has BV slope on its whole compact interval.
The equal-projection restriction thus applies even if the lower subset omits a set of positive parameter measure.
All four resulting estimates are on the same original core.
For complex conjugation the reflected contact mass can again be assigned to the upper graph, since the four rectangles still sum to the identity.
The reflected right bound gives the original left one-input bound by flip-adjoint, and Part B of the two-slice theorem gives both original domains.
Closing the core identity \(E(X_jp)=X_jE(p)+\delta_{ij}\tau(p)\Omega\) gives \([X_j,-\bar E]=\delta_{ij}P_\Omega\) on the closure domain.
Applying the coordinate result to each generator gives the tuple implication without an independence assumption on its coordinates.

The finding covers the specified pair of \(C^{1,1}\) graphs and equality of their slopes at every contact, including one-sided endpoint contacts.
The established supporting results were checked at their interfaces, with the measurable Schur factorization used at its recorded theorem scope.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0252_v1.md#decision-candidate) | Entire closed-contact-set candidate and its original operator assertions. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0252_v1.md#statement) | All contact sets and masses, finite columns, both orientations and domains, commutator and tuple implication. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0252_v1.md#argument) | Sorted heights, encoding and gluing, local complex slope, zero and positive height estimates, original core assembly. |
| [Finding](#finding) | [Actual ACSY and strong conditions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented domain, both bounded-vector inclusions and the generator-first sign. |
| [Finding](#finding) | [Normal phase and companion](../../claims/Yin_C_F0076_v1.md#statement) | Part 1 for diffuseness, starred values and the actual reflected derivation. |
| [Finding](#finding) | [Positive distance and original-core transfer](../../claims/Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Smooth separated planar reciprocal and agreement of localized derivations on all original words. |
| [Finding](#finding) | [BV graph restriction](../../claims/Yin_C_F0248_v1.md#restricting-the-graph-kernel-on-the-parameter-core) | Equal Borel projections for each original branch within its separate auxiliary chart. |
| [Finding](#finding) | [Real parameter near tangency](../../claims/Yin_C_F0248_v2.md#real-parameters-near-a-tangential-contact) | Variable-length coding and the real vacuum transfer, with the new contact gluing checked separately. |
| [Finding](#finding) | [Height-based Schur bound](../../claims/Yin_C_F0248_v2.md#a-schur-bound-from-separation-in-height) | Rescaled Fourier estimates, cutoff of \(1/v\), comparable block summation and the change to frozen complex slopes. |
| [Finding](#finding) | [Tangency core transfer](../../claims/Yin_C_F0248_v2.md#original-mixed-domains-and-finite-assembly) | Bounded cross insertion and finite original-core assembly. |
| [Finding](#finding) | [Scalar packing](../../claims/Yin_C_F0233_v1.md#statement) | Part 1 for the disjoint images of occupied real mesh cells, including the common-set labels. |
| [Finding](#finding) | [Real scalar vacuum](../../claims/Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Sufficiency of compactly supported \(L^3\) parameter density on the identity graph. |
| [Finding](#finding) | [Invariant liberation](../../claims/Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Preservation of all marginal algebras and liberation vacua under the conull Borel relabelling. |
| [Finding](#finding) | [Inverse-gap criterion](../../claims/Yin_C_F0238_v1.md#statement) | Transported energy and actual vacuum at the real distinguished generator. |
| [Finding](#finding) | [Coarse spectral measures](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law domination including positive contact mass in height truncations. |
| [Finding](#finding) | [Real-coordinate column](../../claims/Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Finite distinguished right-column cost on the whole real parameter core. |
| [Finding](#finding) | [Measurable Schur factorization](../literature/AP25/Yin_U001.md#ap25-u001) | Bilinear factors of (6) and precise \(\lvert 1+im\rvert/2\) multiplier estimate. |
| [Finding](#finding) | [Schur insertion on the parameter core](../../claims/Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Cross kernel extended by a rectangle cutoff before the right trace. |
| [Finding](#finding) | [Mixed column graph approximation](../../claims/Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | One joint norm cutoff for finite original columns and convergent coarse derivatives. |
| [Finding](#finding) | [Two-slice theorem](../../claims/Yin_C_F0072_v1.md#statement) | Part B for the actual original closure and its Hilbert adjoint. |
