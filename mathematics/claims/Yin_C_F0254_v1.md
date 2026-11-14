---
author: Yin
---

# Square-Dini changes of planar coordinates preserve actual conjugate variables

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be a bounded normal generating tuple in a finite von Neumann algebra with faithful normal probability trace.
For each \(i\), let \(h_i:\mathbb R^2\to\mathbb R^2\) be a \(C^1\) bi-Lipschitz map onto the plane, identified with \(\mathbb C\).
Assume the derivative of each map has a square-Dini modulus on compact sets.
Precisely, for each compact set \(K\), write
\[
  \omega_K(s)=\sup_{\substack{x,y\in K\\|x-y|\le s}}\|Dh_i(x)-Dh_i(y)\|,
  \qquad \int_0^1\omega_K(s)^2\,\frac{ds}{s}<\infty .
\]
Set \(Y_i=h_i(X_i)\) by normal functional calculus.
Then on their respective represented mixed starred polynomial algebras,
\[
                          \mathsf A(X)\quad\Longleftrightarrow\quad\mathsf A(Y).             \tag{1}
\]
In particular (1) holds for locally \(C^{1,\alpha}\) bi-Lipschitz maps for every \(0<\alpha\le1\), with arbitrary correlations among the normal coordinates.
Here \(\mathsf A\) requires the actual Hilbert adjoint at the tensor vacuum for each distinguished derivation.
The mixed-column estimates needed for the full bounded-vector domains of \(\mathsf S\) are a separate question. [Task hypotheses](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct)

There is a quantitative one-coordinate estimate.
Let \(\mu\) be the diffuse compact law of a distinguished source coordinate with scalar vacuum \(\zeta\), and let \(D=\operatorname{diam}(\operatorname{supp}\mu)>0\).
Write \(h\) for its change of coordinates, take \(a|x-y|\le |h(x)-h(y)|\le L|x-y|\), and put \(\lambda=\min(1,a^2)\).
Take \(\omega=\omega_K\) on the closed convex hull \(K\) of the support and set
\[
   W_D=\sum_{j=0}^{\infty}\omega(2^{-j}D)^2,\qquad
   B_h=\lambda^{-3}\big(\max(2L^4,L^2)+16384 L^2 W_D\big).
\]
The scalar vacuum of \(\sigma=h_*\mu\) exists on its original represented starred polynomial algebra and has squared norm at most \(4B_h\|\zeta\|_2^2\).
For an actual source tuple let \(\xi_i\) be the original mixed vacuum with marginal projection \(\zeta\).
The corresponding new mixed vacuum satisfies
\[
      \|\xi'_i\|_2^2
       \le 4B_h\|\zeta\|_2^2 +a^{-2}\big(\|\xi_i\|_2^2-\|\zeta\|_2^2\big).                 \tag{2}
\]

## Argument

### The soft energy at a fixed geometric scale

For a compact diffuse law \(\mu\), put \(k_t(u)=\bar u/(|u|^2+t)\) and \(C_t\mu(z)=\int k_t(z-w)\,d\mu(w)\).
For three points let \(x,y,s\) be their three squared side lengths and \(H\) be sixteen times their squared area.
The [soft Cauchy symmetrization](Yin_C_F0055_v1.md#4-soft-kernels-and-exact-positive-three-point-formulas) and its [actual-vacuum estimate](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) give
\[
  S_t=\frac{H+t(x+y+s)}{2(x+t)(y+t)(s+t)},\qquad
  \int S_t\,d\mu^3=3\|C_t\mu\|_2^2\le 3\|\zeta\|_2^2.                                     \tag{3}
\]
The equality applies separately to any diffuse image measure, before a vacuum for that measure is known.
Write \(R\) for the diameter of the triple.
On \(r/2<R\le r\), choosing \(t=r^2\) in (3) gives \(S_{r^2}\ge 1/(64r^2)\), using \(x+y+s\ge r^2/4\) and an upper bound \(16r^6\) for the denominator.
Consequently,
\[
   \mu^3\{r/2<R\le r\}\le192r^2\|\zeta\|_2^2,\qquad
   \mu^3\{R\le r\}\le256r^2\|\zeta\|_2^2 .                                                   \tag{4}
\]
The second bound sums the first one over decreasing dyadic radii, with the totally coincident triples null by diffuseness.
For example, the sum of the cubes of the masses of disjoint grid squares of side \(r\) is bounded by the second quantity with radius \(\sqrt2r\).
What the change of coordinates uses is the first bound, which measures triple mass at each separate scale.

### Distortion of the soft triangle energy

Take a triple of distinct points in the support and order the side lengths as \(\ell\le m\le R\), so \(m\ge R/2\).
Use the common endpoint \(z_0\) of a shortest and a longest side as origin, choosing different sides in case of ties.
Write \(u,v\) for their vectors, \(|u|=\ell, |v|=R\), and \(A=Dh(z_0)\).
The two segments lie in \(K\), so the remainders of their images about \(A\) obey \(|e_u|\le\ell\omega(R)\) and \(|e_v|\le R\omega(R)\).
For the signed planar determinant use the identity
\[
 \det(Au+e_u,Av+e_v)
 =(\det A)\det(u,v)+\det(e_u,Av+e_v)+\det(Au,e_v).
\]
The full vector \(Av+e_v\) has length at most \(LR\).
Thus the image value \(H'\) satisfies
\[
    \sqrt{H'}\le L^2\sqrt H+4L\ell R\omega(R),\qquad
    H'\le2L^4H+32L^2\ell^2 R^2\omega(R)^2.                                                    \tag{5}
\]
For each squared side length \(x\), its image value \(x'\) satisfies \(x'+t\ge\lambda(x+t)\) and \(x'\le L^2x\).
Inserting (5) in the image formula (3), and bounding the product \((x+t)(y+t)(s+t)\) below by \(\ell^2m^2R^2\) in the error term alone, gives for every \(t>0\)
\[
   S_t(hz,hw,hv)\le\lambda^{-3}
      \left(\max(2L^4,L^2)S_t(z,w,v)+64 L^2\frac{\omega(R)^2}{R^2}\right).                    \tag{6}
\]
When the derivative is Lipschitz on \(K\), the second term inside the parentheses is bounded by \(64L^2\operatorname{Lip}_K(Dh)^2\).

For general square-Dini modulus put \(r_j=2^{-j}D\).
On each shell \(r_j/2<R\le r_j\), the second factor in (6) is estimated by \(4\omega(r_j)^2/r_j^2\) before its constant \(64L^2\).
By (4),
\[
     \int\frac{\omega(R)^2}{R^2}\,d\mu^3
                \le768\|\zeta\|_2^2\sum_{j\ge0}\omega(r_j)^2 .                                \tag{7}
\]
The term \(j=0\) is finite and monotonicity gives \(\sum_{j\ge1}\omega(r_j)^2\le(\log2)^{-1}\int_0^D\omega(s)^2\,ds/s\), finite also when \(D>1\) by compactness.
After integration of (6) the left side equals \(3\|C_t\sigma\|_{L^2(\sigma)}^2\) in view of (3) for \(\sigma\).
Equations (3) and (7) prove \(\sup_{t>0}\|C_t\sigma\|_2^2\le B_h\|\zeta\|_2^2\).

### The actual adjoints on the two starred algebras

Let \(p\) be a polynomial in \(z,\bar z\) evaluated on the target spectrum.
Antisymmetry gives
\[
  2\int p(z) C_t\sigma(z)\,d\sigma(z)
     =\iint \frac{p(z)-p(w)}{z-w}\frac{|z-w|^2}{|z-w|^2+t}\,d\sigma(z)d\sigma(w).
\]
The divided difference is bounded off the product-null diagonal, using an ambient Lipschitz bound for \(p\) on the convex hull of the image support.
Dominated convergence recovers the unregularized original scalar vacuum functional on the right.
Along any weakly convergent subsequence from \(2\overline{C_{1/n}\sigma}\), its Hilbert weak limit \(\zeta'\) therefore represents that functional on every target starred polynomial, with \(\|\zeta'\|_2\le2\sqrt{B_h}\|\zeta\|_2\).
The inner product here is linear in the second variable.
The divided difference is itself a represented scalar derivation since a polynomial vanishing \(\sigma\)-almost everywhere has vanishing difference on the product measure.
This establishes its actual Hilbert adjoint at \(1\otimes1\).

Assume now \(\mathsf A(X)\).
All source marginals are diffuse, and each has the actual scalar vacuum obtained by projecting the mixed vacuum onto its marginal.
The maps preserve the marginal von Neumann algebras and give bounded Borel changes on the respective compact spectra with bounded Borel inverses there.
The [spectral relabelling criterion](Yin_C_F0244_v1.md#statement), item 1, therefore preserves each distinguished liberation vacuum \(\eta_i\) on the target mixed core, and transports its left-right spectral measure \(\nu_i\) by \((h_i,h_i)\).
For a single such coordinate with map \(h\) the remaining contribution to the squared norm is
\[
   \int_{z\ne w}\frac{d\nu_i(z,w)}{|h(z)-h(w)|^2}
       \le a^{-2}\int_{z\ne w}\frac{d\nu_i(z,w)}{|z-w|^2}
       =a^{-2}\big(\|\xi_i\|_2^2-\|\zeta\|_2^2\big).
\]
The criterion gives a distinguished derivation on the entire target represented mixed starred polynomial algebra, with value \(1\otimes1\) on its own unstarred generator, zero on omitted generators, and actual Hilbert adjoint at \(1\otimes1\).
Its squared vacuum norm is the sum of the displayed target integral and \(\|\zeta'\|_2^2\).
This proves (2) and the forward implication of (1), including unchanged coordinates.

The lower Lipschitz bound gives \(\|Dh(x)^{-1}\|\le a^{-1}\) at every point.
The inverse function theorem gives \(D(h^{-1})(y)=Dh(h^{-1}(y))^{-1}\).
For a compact target set \(K'\), its inverse derivative modulus is at most \(a^{-2}\omega_{h^{-1}(K')}(s/a)\), by the inverse matrix difference identity.
This has finite square-Dini integral at zero.
The inverse map has Lipschitz constants \(L^{-1},a^{-1}\), so the forward argument applied to the inverse maps with the target diameters as starting scales proves the reverse implication.

### Relation to bilipschitz invariance of the Cauchy integral

Tolsa's Theorem 1.3 transfers finite Menger curvature under a planar bi-Lipschitz map for a compactly supported measure with uniform linear growth.
Theorem 1.4 transfers boundedness of the Cauchy operator on the full \(L^2\) space of a nonatomic Radon measure.
The argument here starts from the single actual vacuum and uses square-Dini regularity to compare its soft energies.
The two statements of Tolsa are cited for comparison. [Tolsa, Annals of Mathematics 162 (2005), Theorems 1.3 and 1.4, pp. 1246–1247](https://annals.math.princeton.edu/wp-content/uploads/annals-v162-n3-p03.pdf)

The root agent proposed comparing the soft triangle energies by a shortest-side Taylor expansion for \(C^{1,1}\) changes.
The collaborating agent derived the squared-modulus summation, first by grid packing and then directly from the soft energy on each diameter shell.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:57 |
| status | open |
| reason | The two-way invariance on the original mixed cores and the scalar and mixed vacuum estimates are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Square-Dini bi-Lipschitz invariance of actual ACSY for correlated planar normal coordinates and quantitative one-coordinate vacuum transfer. |
| argument | [Argument](#argument) | Diameter-shell control, shortest-side determinant estimate, soft-energy summation, original scalar adjoint pairing, mixed-core recovery and the inverse derivative modulus. |
| dependency | [Soft symmetrization](Yin_C_F0055_v1.md#4-soft-kernels-and-exact-positive-three-point-formulas) | The nonnegative three-point kernel with its exact area and squared-side numerator. |
| dependency | [Soft vacuum estimate](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | The symmetrized energy identity and the uniform scalar actual-vacuum bound in equations (12) and (14). |
| dependency | [Borel relabelling criterion](Yin_C_F0244_v1.md#statement) | Item 1 for diffuse actual normal marginals, common liberation vacuum, target mixed starred derivation and the orthogonal norm formula in both labellings. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:00 |
| status | proved |
| reason | Adopt the quantitative square-Dini invariance of the actual starred condition after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Square-Dini bi-Lipschitz invariance of actual ACSY for correlated planar normal coordinates and quantitative one-coordinate vacuum transfer. |
| argument | [Argument](#argument) | Diameter-shell control, shortest-side determinant estimate, soft-energy summation, original scalar adjoint pairing, mixed-core recovery and the inverse derivative modulus. |
| dependency | [Soft symmetrization](Yin_C_F0055_v1.md#4-soft-kernels-and-exact-positive-three-point-formulas) | The nonnegative three-point kernel with its exact area and squared-side numerator. |
| dependency | [Soft vacuum estimate](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | The symmetrized energy identity and the uniform scalar actual-vacuum bound in equations (12) and (14). |
| dependency | [Borel relabelling criterion](Yin_C_F0244_v1.md#statement) | Item 1 for diffuse actual normal marginals, common liberation vacuum, target mixed starred derivation and the orthogonal norm formula in both labellings. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0263_v1.md#finding) | The area and shell estimates, quantitative scalar and mixed vacuum bounds, inverse modulus and both implications. |
