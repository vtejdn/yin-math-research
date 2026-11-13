---
author: Yin
---
# Full coordinate domains on finite unions of smooth spectral arcs

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite von Neumann algebra \(M\) with faithful normal probability trace, \(H=L^2(M)\), \(\Omega=1\), and \(P_\Omega a=\tau(a)1\).
Use the [actual starred ACSY, bare and strong conditions](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) \(\mathsf A,\mathsf F,\mathsf S\).
Suppose the spectrum of one distinguished \(X_i\) is contained in a union of finitely many pairwise disjoint compact regular \(C^3\) embedded arcs in \(\mathbb C\).
Each arc here is the injective image of a nondegenerate closed interval by a map admitting a \(C^3\) extension to a neighborhood of that interval and having nonzero derivative everywhere on the interval, endpoints included.
Neither a common projection direction nor joint independence is required.

Under \(\mathsf A(X)\) the represented canonical slice \(E_{i,0}=(\mathrm{id}\otimes\tau)\delta_i\) on \(\mathbb C\langle X,X^*\rangle\) satisfies
\[
 M\Omega\subseteq\operatorname{Dom}\overline E_{i,0}\cap\operatorname{Dom}E_{i,0}^*,
 \qquad c_i(X)<\infty ,
\]
where \(c_i\) is the [full starred-core column cost](Yin_C_F0208_v1.md#statement).
The other normal coordinates have arbitrary spectra.

If every coordinate has such an arc cover, choose disjoint compact real parameter intervals within each coordinate and write \(S_j=h_j(X_j)\) for its real inverse parameter as constructed below.
The selfadjoint tuple \(S\) generates \(M\), and
\[
             \mathsf A(X)\ \Longleftrightarrow\ \mathsf A(S)
             \ \Longleftrightarrow\ \mathsf F(S)
             \ \Longleftrightarrow\ \mathsf F(X)
             \ \Longleftrightarrow\ \mathsf S(X).
\]
The conclusion gives finiteness for each fixed arc cover and law.
No uniform bound as two arcs approach one another is asserted.

## Argument

### Parameters on disjoint arcs

Suppress the coordinate index, and place its finitely many parameter intervals \(I_a\) disjointly in \(\mathbb R\) by affine changes of variable.
Set \(I=\bigcup_a I_a\) and let \(r:I\to\mathbb C\) be the resulting injective map onto the union \(\Gamma\).
Extending each branch a little beyond its endpoints and using disjoint smooth cutoffs gives a compactly supported complex \(C^3\) function on \(\mathbb R\) equal to the given branches on \(I\).
An extension need only agree there.
The inverse \(h\) on \(\Gamma\) extends to a real \(C^1\) function on a plane rectangle containing the spectrum.
Indeed, at each parameter value choose a real linear projection \(\ell:\mathbb C\to\mathbb R\) with \((\ell\circ r)'\ne0\) there.
In a sufficiently small plane neighborhood the arc is parametrized by this projection and the local inverse is \((\ell\circ r)^{-1}\circ\ell\).
The branch extension gives the same inverse at an endpoint.
Compactness and injectivity permit each such neighborhood to miss the image outside the chosen parameter patch, including the other arcs.
Patch finitely many local real inverses with a smooth partition of unity near \(\Gamma\), then cut off inside that neighborhood.
All the local inverse values coincide on the pieces of \(\Gamma\) where the partition is supported.
Continuous functional calculus gives \(S=h(X_i)=S^*\), \(X_i=r(S)\) and \(W^*(S)=W^*(X_i)\).

Set \(J(s,t)=r^{[1]}(s,t)\) on a real rectangle around \(I^2\), with \(J(s,s)=r'(s)\).
The formula \(J(s,t)=\int_0^1 r'(\theta s+(1-\theta)t)\,d\theta\) makes \(J\) of class \(C^2\).
Injectivity on \(I\) and regularity imply \(\min_{I^2}|J|>0\).
Thus \(K=1/J\) is \(C^2\) near \(I^2\), and multiplication by a smooth cutoff supported there extends it to a compactly supported \(C^2\) function on a real rectangle.
This construction controls every cross-branch rectangle.
Periodizing the extensions gives the following two multiplier facts by the [one- and two-dimensional Fourier computations](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates).
The divided difference \(J\) is a sum of integrals of separated exponentials
\[
 J(s,t)=\sum_n in\omega c_n\int_0^1 e^{in\omega\theta s}e^{in\omega(1-\theta)t}\,d\theta,
 \qquad \sum_n(1+n^2)|c_n|<\infty ,
\]
where \(c_n\) are the Fourier coefficients of the periodic extension of \(r\), agreeing with it on the convex hull of \(I\).
The \(C^2\) extension of \(K\) has an absolutely convergent double Fourier series, since its coefficients are square summable with squared weight \((1+m^2+n^2)^2\) and \(\sum_{m,n}(1+m^2+n^2)^{-2}<\infty\).
Both are therefore projective tensor multipliers of bounded functions of \(S\).

### Transporting the actual derivation to a selfadjoint coordinate

Under \(\mathsf A(X)\) let \(\delta=\delta_i\) and \(\xi=\delta^*(1\otimes1)\).
By [the normal phase theorem](Yin_C_F0076_v1.md#statement), this derivation is closable, the distinguished marginal is diffuse and the starred marginal rule is the divided difference with denominator \(z-w\).
Approximate \(h\) uniformly with its first real derivatives on the rectangle by polynomials in \(z,\bar z\), by the [smooth marginal approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests).
The divided differences converge uniformly off the diagonal, since their errors are bounded by the supremum of the real differential error.
Thus \(S\) has approximants in the represented core converging in operator norm and in the graph of \(\delta\), and \(\bar\delta S=K(S\otimes1,1\otimes S)\) as a marginal tensor.
In fact \((h(z)-h(w))/(z-w)=K(h(z),h(w))\) on distinct spectral points.
The same reasoning for \(e^{i\alpha h(z)}\) gives graph approximants to \(e^{i\alpha S}\) and a coarse derivative bound \(|\alpha|\,\|K\|_{\infty,I^2}\).
Conjugate exponentials satisfy the same bounds.
For omitted coordinates having their own arc coordinates replaced, the closed \(\delta_i\) kills the replacements by the same bounded approximation with zero derivatives.

On the mixed algebra generated by \(S\) and the other original normal coordinates and their adjoints, the graph limits of products obey the Leibniz rule.
Indeed approximating each bounded factor in norm and its derivative in coarse norm gives graph convergence for every fixed product.
If more arc coordinates were replaced, this also applies on the resulting mixed core.
Write \(I_{a\otimes b}(v\otimes w)=va\otimes bw\) for the inner action commuting with the outer actions.
The projective multiplier \(I_J\) applied to the restriction of \(\bar\delta\) gives an actual represented derivation \(\theta\) normalized to \(1\otimes1\) at \(S\) and zero on all other generators and their adjoints, since \(JK=1\) on \(I^2\).
Its vacuum exists.
For \(a=e^{i\alpha S},b=e^{i\beta S}\), the original actual adjoint has
\[
 a\otimes b\in\operatorname{Dom}\delta^*,\qquad
 \|\delta^*(a\otimes b)\|_2\le\|\xi\|_2+(|\alpha|+|\beta|)\|K\|_{\infty,I^2}.
\]
This follows by expanding the vacuum identity on \(a^*p b^*\) through the bounded graph approximants as in [the tensor-adjoint calculation](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier).
In that calculation each differentiated-factor term pairs \(p\) against a trace slice with Hilbert norm controlled by the indicated coarse derivative and the other factor's operator norm.
The pairing and vectors vary continuously in the exponential parameters on compact sets, since functions and marginal differences do so in norm and coarse norm.
The weighted series for \(J\) then converges in the adjoint graph when applied as \(I_J^*\) to \(1\otimes1\).
Its coefficients in that adjoint are conjugated, so this establishes the actual vacuum \(\theta^*(1\otimes1)=\delta^*(I_J^*(1\otimes1))\) by testing on the new dense core.
All its values there are finite sums of core elementary tensors by its normalized generator rules.
It is real and coassociative there: reality holds on the complete list of starred generators, and both iterated derivatives of each word sum over ordered pairs of distinct occurrences of \(S\) in the same order.
In particular this proves \(\mathsf A(S)\) when all coordinates are replaced.

### Full-domain witnesses and their transport

At the single distinguished selfadjoint coordinate of the mixed tuple, the [real coassociative contraction estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) bounds both trace slices of \(\theta\) on the full mixed core by \(2\|\theta^*(1\otimes1)\|_2\) times the input operator norm.
The [two-slice domain theorem](Yin_C_F0072_v1.md#statement), Part B, gives a closed canonical operator \(E^S\) and actual adjoint whose domains contain \(M\Omega\), with bounded restrictions from operator norm to Hilbert norm.
On bounded vectors its operator-first commutators with the mixed generators are \(P_\Omega\) at \(S\) and zero at the omitted coordinates.
To see the extension from the core, approximate the bounded input strongly-star on a common ball by mixed core elements using [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) and norm density in the generated \(C^*\)-algebra.
Their \(E^S\) values and those for multiplication by a generator are bounded in Hilbert norm, and the weakly closed graph identifies all weak cluster values with the indicated closed-operator evaluations.
The same reasoning applies to an actual selfadjoint tuple \(S\) if \(\mathsf A(S)\) is given directly.

Approximation of \(r\) in \(C^1\) on the convex hull of \(I\) by complex polynomials gives
\([E^S,X_i]=\Theta(J)\) on \(M\Omega\), with \(\Theta(a\otimes b)=aP_\Omega b\).
The input operators converge in norm and the divided differences converge uniformly, hence in coarse norm and in Hilbert–Schmidt norm after \(\Theta\).
If other coordinates were replaced the same polynomial argument gives zero at their original \(X_j\).
Use \(F=Q_K(E^S)\), where \(Q_{a\otimes b}(E)=\rho(a)E\rho(b)\) and \(\rho(a)x=xa\).
The [projective correction and adjoint formula](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) gives on \(M\Omega\)
\[
 [F,X_j]=\delta_{ij}P_\Omega,\qquad
 F^*\supseteq Q_{K}^{\,\dagger}(E^{S*})|_{M\Omega}.
\]
For \(K=\sum c_\ell a_\ell\otimes b_\ell\), the latter right-hand side is \(\sum\bar c_\ell\rho(b_\ell^*)E^{S*}\rho(a_\ell^*)\).
The projective summability gives both bounds in operator norm to Hilbert norm and justifies the actual adjoint by pairing.
The sign for an operator-second strong witness is \(-F\).
This proves the single distinguished strong witness under \(\mathsf A(X)\), as well as \(\mathsf A(S)\Rightarrow\mathsf S(X)\) in the full-coordinate case.

For the stated column estimate adjoin two jointly free Haar unitaries free from \(X\).
The [two-Haar theorem](Yin_C_F0208_v1.md#statement) preserves actual ACSY and \(c_i(X)\le4\beta_i(X,U,V)\).
The enlarged tuple has exactly the same distinguished spectrum.
The preceding single-coordinate proof supplies a bounded witness there, so \(c_i(X)<\infty\).
Apply the same proof to the adjoint tuple, whose actual normalized derivations and vacua are the conjugate companions of the original ones by C_F0076.
Its distinguished carrier is the complex conjugate arc union.
Hence the right slice of the conjugate companion is bounded on the original starred core as well.
Since this slice on \(a^*\) is the tracial adjoint of the left slice of \(\delta_i\) on \(a\), both original slices are operator-norm-to-Hilbert bounded.
Part B of C_F0072 now applies to the original \(E_{i,0}\) and yields precisely the two claimed canonical domains.

### The bare converse when all coordinates have arc carriers

Suppose \(\mathsf F(X)\).
The [normal bare-dual theorem](Yin_C_F0070_v1.md#statement), Part A, supplies bounded normalized maps \(E_i:M\to H\) and the actual commutator identity \([E_i,L_p]=\Theta(\delta_i p)\) on bounded inputs for all starred-core polynomials \(p\), with the forced marginal phase and zero at omitted starred generators.
Here no vacuum premise is needed.
Apply the preceding \(C^1\) approximants to \(h_j\).
Uniform operator convergence permits passage through the bounded \(E_i\), and uniform convergence of the marginal divided differences gives convergence of the Hilbert–Schmidt commutator kernels.
Thus \([E_i,S_j]=\delta_{ij}\Theta(K_i)\) on \(M\Omega\).
The projective \(J_i\) gives \([Q_{J_i}(E_i),S_j]=\delta_{ij}P_\Omega\), whence \(\mathsf F(S)\).
For selfadjoint tuples \(\mathsf F(S)\Leftrightarrow\mathsf A(S)\) by [the selfadjoint converse](Yin_C_F0071_v2.md#statement), Part B.
Finally strong implies bare by restriction, and strong implies actual ACSY by the vacuum corollary in C_F0070, Part C.
Together with the two forward transports this proves the full chain of equivalences.

## Scope and provenance

This continues the [single analytic arc theorem](Yin_C_F0042_v1.md#statement) and the [single \(C^3\) spectral graph theorem](Yin_C_F0137_v1.md#statement).
The check_defect agent for Yin developed the disjoint-arc parametrization and actual-domain argument during the coordinating agent's investigation of multi-branch examples for [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
The finite disjoint cover is used both for the plane inverse parameter and for the positive lower bound on the divided difference over all rectangles.
Intersecting branches, accumulations of components, and an entire closed curve as a single interval image are outside these hypotheses.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:40 |
| status | open |
| reason | The single-coordinate column and canonical-domain conclusions and the all-coordinate transport equivalence are fixed for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite disjoint \(C^3\) arc carriers, one distinguished column cost and both original domains, and the all-coordinate equivalence. |
| argument | [Argument](#argument) | Plane inverse extension with endpoints, nonvanishing secants, two multiplier bounds, actual vacuum and operator transports, and two-Haar testing. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Part 1, closability, differentiated marginal functions, diffuse marginal, and actual conjugate companion. |
| dependency | [Real \(C^1\) approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform real polynomial approximation with first derivatives on a plane rectangle. |
| dependency | [Fourier summability](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | Weighted one-dimensional Fourier estimate and absolutely summable two-dimensional expansion. |
| dependency | [Actual tensor adjoint](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Graph approximation and exponential tensor-adjoint estimates with differentiated-factor norms. |
| dependency | [Projective correction](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) | Commutation of inner and outer actions, right-multiplier order and actual adjoint on all bounded inputs. |
| dependency | [Real coassociative estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Theorem 4.9 for the two slices of the transformed, algebraic-valued mixed-core derivation. |
| dependency | [Canonical domains](Yin_C_F0072_v1.md#statement) | Part B, both bounded-vector domains and bounded restrictions from the two slice bounds. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Uniformly bounded strongly-star approximants to a bounded input for extending commutators from the canonical core. |
| dependency | [Two-Haar enlargement](Yin_C_F0208_v1.md#statement) | Preservation of actual ACSY and lower bound \(c_i(X)/4\) for the enlarged old-coordinate dual cost. |
| dependency | [Bare normal duals and vacuum](Yin_C_F0070_v1.md#statement) | Parts A and C, starred commutator kernels and automatic boundedness from bare maps, as well as strong implying actual ACSY. |
| dependency | [Selfadjoint bare converse](Yin_C_F0071_v2.md#statement) | Part B, equivalence of bare full-domain duals and actual ACSY on selfadjoint generating tuples. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:44 |
| status | proved |
| reason | Independent review verifies the smooth inverse on disjoint arcs, convergence in the actual adjoint graph and transport in both directions, including the original column and two domains. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite disjoint \(C^3\) arc carriers, one distinguished column cost and both original domains, and the all-coordinate equivalence. |
| argument | [Argument](#argument) | Plane inverse extension with endpoints, nonvanishing secants, two multiplier bounds, actual vacuum and operator transports, and two-Haar testing. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Part 1, closability, differentiated marginal functions, diffuse marginal, and actual conjugate companion. |
| dependency | [Real \(C^1\) approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform real polynomial approximation with first derivatives on a plane rectangle. |
| dependency | [Fourier summability](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | Weighted one-dimensional Fourier estimate and absolutely summable two-dimensional expansion. |
| dependency | [Actual tensor adjoint](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Graph approximation and exponential tensor-adjoint estimates with differentiated-factor norms. |
| dependency | [Projective correction](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) | Commutation of inner and outer actions, right-multiplier order and actual adjoint on all bounded inputs. |
| dependency | [Real coassociative estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Theorem 4.9 for the two slices of the transformed, algebraic-valued mixed-core derivation. |
| dependency | [Canonical domains](Yin_C_F0072_v1.md#statement) | Part B, both bounded-vector domains and bounded restrictions from the two slice bounds. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Uniformly bounded strongly-star approximants to a bounded input for extending commutators from the canonical core. |
| dependency | [Two-Haar enlargement](Yin_C_F0208_v1.md#statement) | Preservation of actual ACSY and lower bound \(c_i(X)/4\) for the enlarged old-coordinate dual cost. |
| dependency | [Bare normal duals and vacuum](Yin_C_F0070_v1.md#statement) | Parts A and C, starred commutator kernels and automatic boundedness from bare maps, as well as strong implying actual ACSY. |
| dependency | [Selfadjoint bare converse](Yin_C_F0071_v2.md#statement) | Part B, equivalence of bare full-domain duals and actual ACSY on selfadjoint generating tuples. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0243_v1.md#whole-proof-finding) | The single-coordinate statement and every implication of the all-coordinate equivalence at the given arc hypotheses. |
