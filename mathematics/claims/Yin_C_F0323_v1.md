---
author: Yin
---

# The four-point Gram measure for three alternating marginal factors

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z_0,Z_1\) be a bounded normal generating pair with full actual starred conjugate variables in a finite tracial von Neumann algebra \((M,\tau)\), with faithful probability trace.
Assume the [product trace condition](Yin_C_F0321_v1.md#statement) \(\tau(ab)=\tau(a)\tau(b)\) for \(a\in A=W^*(Z_0)\), \(b\in B=W^*(Z_1)\).
Write \(Z=Z_0\), \(\mu=\operatorname{law}(Z)\), \(\Lambda=\mu\otimes\mu\), \(e(S)=1_S(Z)\), \(E=(\mathrm{id}\otimes\tau)\delta_0\), and \(\xi=\delta_0^*(1\otimes1)\).
Let \(b_1,\ldots,b_m\in B\) be centered unitaries orthonormal for the trace inner product, with \(m\) any finite positive integer.
Let \(P_H\) project onto \(H=\overline{\sum_i A b_i A}^{\,2}\), and let \(\Gamma\) be the positive \(m\)-by-\(m\) matrix measure on the spectral product given on rectangles by
\[
                 \Gamma_{ij}(S\times T)=\tau(b_i^*e(S)b_je(T)).
\]
Write \(\Gamma=G\Lambda+\Gamma_s\) for its Lebesgue decomposition relative to \(\Lambda\); \(\operatorname{tr}\) on matrices is unnormalized.
Then \(G\) is positive definite \(\Lambda\)-almost everywhere and
\[
 \int\operatorname{tr}(G+G^{-1}-2I)\,d\Lambda+
       \operatorname{tr}\Gamma_s(\mathbb C^2)
   =\sum_{j=1}^m\|P_H b_j[\xi,Z^*]\|_2^2
   \le m\|[\xi-Z,Z^*]\|_2^2.                                          \tag{1}
\]
In particular \(\int\operatorname{tr}(G^{-1})\,d\Lambda\le m(1+\|[\xi,Z^*]\|_2^2)\).
The right side of (1), divided by \(m\), is at most \(4\|Z\|^2\|\xi-Z\|_2^2\).

Suppose in addition \(\Gamma_s=0\) and \(\ell I\le G\le L I\) almost everywhere for \(0<\ell\le L<\infty\).
Let \(W\) be the [scalar marginal weight](Yin_C_F0267_v1.md#statement) with \(\tau(W)=\|\mathbb E_A\xi\|_2^2\).
For finite sums \(x=\sum a b_i c\) with \(a,c\) marginal starred polynomials one has
\[
             \|Ex\|_2\le (2+\sqrt2)\sqrt{L/\ell}\,\|x\sqrt W\|_2 .
                                                                         \tag{2}
\]
For arbitrary \(x\) on the original starred polynomial core,
\[
       \|P_H Ex\|_2\le\|x\xi^*\|_2+\sqrt{2L/\ell}\,\|x\sqrt W\|_2.     \tag{3}
\]
The graph values in (2) also allow \(b_i\) that are bounded Borel functions of the omitted generator.
These bounds include \(G=I,\ \Gamma_s=0\) and have no factor depending on \(m\).

There are actual exchange-symmetric pairs with both marginals Haar and exact product two-marginal trace for which, with \(b_1=Z_1,b_2=Z_1^*\), the smallest eigenvalue of \(G\) tends to zero.
On these pairs a polynomial in the span \(A b_1 A+A b_2 A\) has norm tending to zero and right slice of norm one orthogonal to \(L^2(A)\).
Thus the two marginal vacuum norms alone do not bound this mixed slice on the represented operator-norm ball.
Both full strong duals exist for these examples, and the normalized joint slice-to-vacuum bound is finite uniformly in this family.

## Argument

### A commutator that represents product measure

Let \(S\) be the scalar right slice of the marginal \(Z\) and \(S^\#\) its reversed scalar right slice.
On a marginal polynomial \(c\), \(Sc(z)=\int (c(z)-c(w))/(z-w)\,d\mu(w)\) off the product-null diagonal, and \(S^\#=JSJ\), where \(J\) is scalar conjugation.
These formulas follow from the [normal marginal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability).
The original derivatives in both orientations kill the omitted algebra on bounded strong-star graph limits by the [omitted-algebra graph calculation](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra).
For products with one \(b_i\), take uniformly bounded polynomial approximants to \(b_i\) in the omitted algebra and use strong-star convergence on the outer legs in the finite product rule.
This gives simultaneous graph approximation of \(a b_i c\) and of its product with \(Z\).
The identity \(E^*y=y\xi-E^\#y\) on the core passes to these approximants by closedness, since their bounded strong convergence also gives convergence after multiplication on \(\xi\).

For centered \(b\in B\) one has \(E(a b c)=a b Sc\).
Indeed the derivative at \(a\) takes values in the marginal coarse space, and tracing its second leg times \(bc\) gives zero since \(\mathbb E_A b=0\).
The derivative at \(b\) vanishes and the derivative at \(c\) gives the displayed result.
The same conclusion holds with \(E^\#,S^\#\) in place of \(E,S\).
Since \(S(cZ)-(Sc)Z=\tau(c)1\), this gives
\[
             E((a b c)Z)-(E(a b c)) Z = a b\,\tau(c).
\]
Test with \(b_j\), using the inner product linear in its second argument.
One has \(E^*b_j=b_j\xi\) and \(E^*(b_jZ^*)=b_j Z^*\xi-b_j\) since \(S^\#(Z^*)=1\).
Moving the right multiplications across the Hilbert inner products and applying product trace to \(a\) and \(b b_j^*\) proves
\[
          \langle b_j(1+[\xi,Z^*]),a b_i c\rangle
                  =\delta_{ji}\tau(a)\tau(c).                            \tag{4}
\]

The commuting left and right spectral actions of \(Z\) on \(L^2(M)\) give a joint projection-valued measure.
Its matrix coefficients on the \(b_i\) define the positive measure \(\Gamma\) above.
For a vector \(f\) of finite sums of separated polynomial functions on the two marginal spectra let \(U f\) send the \(i\)-th term \(a(z)c(w)\) to \(a b_i c\), summing over \(i\).
Then \(\|Uf\|_2^2=\int f^*d\Gamma f\).
This representation extends to an isometry of the matrix-weighted space onto \(H\).
For example use \(\operatorname{tr}\Gamma\) as a scalar dominating measure, quotient by the pointwise kernel of its density, and complete in the indicated norm.
Separated polynomials are dense by uniform approximation of continuous functions on the compact product and density in the corresponding finite scalar measure.
The represented range is \(H\), also by approximating bounded marginal factors strongly-star.
Formula (4) identifies the product integral \(\int f_j\,d\Lambda\) with the functional represented by \(P_Hb_j(1+[\xi,Z^*])\).

### The inverse density and the singular mass

Write \(h_j\) for the representing field in the matrix-weighted space.
Measurable representatives exist in the finite-dimensional fibers by applying the pointwise inverse square root on the support of the matrix density to vectors in the ordinary direct integral.
For vector tests as above,
\[
      \int h_j^*\,d\Gamma\,f=\int f_j\,d\Lambda .
\]
The row-valued measure on the left is finite by Cauchy--Schwarz in the weighted norm.
Agreement on the dense continuous test algebra gives equality of measures.
Separating their absolutely continuous and singular parts gives \(G h_j=\mathbf e_j\) \(\Lambda\)-almost everywhere, while the singular part of \(h_j\) has zero weighted norm.
Here \(\mathbf e_j\) is the \(j\)-th standard vector.
The \(m\) equations together force \(G>0\) almost everywhere, and \(\|h_j\|^2=\int (G^{-1})_{jj}\,d\Lambda\).
Since \(b_j\in H\) is unitary and \(\tau([\xi,Z^*])=0\), the square of its representing vector also equals
\[
       \|P_H b_j(1+[\xi,Z^*])\|_2^2
          =1+\|P_H b_j[\xi,Z^*]\|_2^2 .
\]
Summing and using \(\int\operatorname{tr}G\,d\Lambda+\operatorname{tr}\Gamma_s(\mathbb C^2)=m\) proves (1), including its normalized bound since \([Z,Z^*]=0\).
Both terms on the left of (1) are nonnegative by scalar functional calculus for positive matrices.

### Bounds on the slice and its projection

For polynomial vector tests, \(E(Uf)=U(S_w f)\), where \(S_w\) acts in the terminal argument \(w\) of each component.
Here \(U\) is applied to the resulting Hilbert field, and for each separated term it gives exactly \(a b_i Sc\) by the spectral representation.
Indeed \(Sc\) is bounded for fixed polynomial \(c\) by its Lipschitz constant on a containing box.
Right marginal multiplication corresponds to multiplying the field by the same function of \(w\).
Under \(\ell I\le G\le L I\) and \(\Gamma_s=0\), \(U\) identifies the ordinary product space \(L^2(\Lambda;\mathbb C^m)\) with \(H\), with squared norm comparison \(\ell,L\).
The scalar estimate for \(S\) with weight \(W\) then gives
\[
  \|E(Uf)\|_2^2\le L(2+\sqrt2)^2\int |f(z,w)|^2 W(w)\,d\Lambda
                \le (L/\ell)(2+\sqrt2)^2\|(Uf)\sqrt W\|_2^2 .
\]
The last equality of weights follows by bounded truncations of \(\sqrt W\) in the spectral representation.
This proves (2).

For a test \(y=Uf\), the actual adjoint pairing gives
\[
       \langle y,Ex\rangle=\langle y,x\xi^*\rangle
                                -\langle U(S^\#_w f),x\rangle
\]
on every original core input \(x\).
As in the [ordered output estimate](Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs), the second term can be bounded using the scalar adjoint of \(S^\#\), whose norm from \(L^2((1+W)\mu)\) to \(L^2(\mu)\) is bounded pointwise by \(\sqrt2\|\cdot\sqrt W\|_2\).
This follows first on marginal polynomials by the scalar adjoint estimate and then by weighted polynomial approximation and closedness.
To see the constants, put \(h=U^{-1}P_Hx\).
In the product space the second pairing equals \(\langle S^\#_w f,Gh\rangle\).
Right marginal multiplication commutes with \(P_H\) because \(H\) reduces it.
Using \(G^2\le L G\) pointwise and then truncating \(\sqrt W\) gives \(\|(Gh)\sqrt W\|_{L^2(\Lambda)}\le\sqrt L\,\|x\sqrt W\|_2\).
Apply the scalar adjoint test inequality in each terminal fiber and integrate by Cauchy--Schwarz, using \(\|f\|_{L^2(\Lambda)}\le\ell^{-1/2}\|Uf\|_2\).
The second term has absolute value at most \(\sqrt{2L/\ell}\|y\|_2\|x\sqrt W\|_2\).
The first term costs at most \(\|y\|_2\|x\xi^*\|_2\).
Density of the tests gives (3).

### An actual pair with degenerating four-point density

Take a Haar unitary \(X\) and a free unitary \(V\) with a bounded diffuse density on the unit circle, invariant under multiplication by \(-1\) and supported within angular distance \(0<\delta<\pi/4\) of \(1,-1\).
One can use normalized arclength on the union of the two arcs.
Then \(\tau V=0\) and \(\tau(V^2)\to1\) as the widths tend to zero.
The scalar law of \(V\) has bounded maximal linear density and finite curvature, giving an [actual scalar vacuum](Yin_C_F0255_v1.md#statement).
Put \(Y=X^* V\).
The [phase coupling criterion](Yin_C_F0265_v1.md#statement) with \(h(X)=X\) gives actual conjugate variables and strong duals for the pair \(X,Y\), since its scalar secant quotient has modulus one.
The [exchange calculation](Yin_C_F0315_v1.md#actuality-of-the-product-law) shows that \(Y\) is Haar and the pair is exchange-symmetric.
For \(l>0\) the word \(Y^l=(X^*V)^l\) has only centered \(V\)-letters separated by centered \(X^*\)-letters, so its expectation onto \(W^*(X)\) is zero by reduced words.
The same holds for \(l<0\) by adjunction.
This proves exact product trace for the marginal algebras by normality.

Take \(b_1=Y,b_2=Y^*\), two orthonormal centered unitaries for the Haar law.
For bounded marginal tests \(a,c\), the diagonal Gram pairings are \(\tau(a)\tau(c)\) by freeness and centering of \(V\).
For example the first is \(\tau(V^* a V c)=\tau(a)\tau(c)\).
The other diagonal has the same value after moving the terminal \(X\) factors by cyclicity.
The off-diagonal pairing is \(\tau(V^* X a V^* X c)=\tau(V^{*2})\tau(Xa)\tau(Xc)\) by expansion into centered free words.
Consequently there is no singular part and
\[
       G(z,w)=\begin{pmatrix}1&\tau(V^{*2})zw\\
                   \tau(V^2)\bar z\bar w&1\end{pmatrix}.
\]
Its eigenvalues are \(1\pm|\tau(V^2)|\), giving the asserted failure of a uniform pointwise lower bound.
In fact (1) gives \(\|[\xi,X^*]\|_2^2\ge |\tau(V^2)|^2/(1-|\tau(V^2)|^2)\).

In the original polynomial core \(x=XYX-Y^*=(V-V^*)X\) satisfies \(\|x\|\le2\sin\delta\), while the distinguished product rule gives \(Ex=XY+\tau(YX)1=V\).
Freeness and \(\tau V=0\) give \(\mathbb E_{W^*(X)}Ex=0\).
Thus even for joint product two-marginal trace, the right slice of a three-factor linear combination, after removing its marginal output, can be arbitrarily large on contractions with fixed Haar marginal vacuum norms.
The [uniform phase-coupling theorem](Yin_C_F0320_v1.md#statement) bounds the slice relative to the actual joint vacuum throughout this family.
The uniform normalized comparison for general pairs with product marginal trace remains open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:40 |
| status | open |
| reason | Fix the four-point Gram identity, comparability bounds and the three-factor example for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Matrix inverse density, singular mass, trace defect and projected and three-factor slice estimates, with an actual degenerating family. |
| argument | [Argument](#argument) | Commutator representing the product integral, spectral disintegration, scalar adjoint duality and the two-channel free unitary calculation. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Scalar divided differences, the reversed coordinate and the actual starred derivative. |
| dependency | [Omitted algebra](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Joint bounded approximants for Borel factors of the omitted coordinate. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Complex scalar forward and adjoint estimates and mass of the integrable marginal weight. |
| dependency | [Ordered output pairing](Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs) | Core adjoint pairing and weighted adjoint duality, here applied in the terminal variable of the matrix spectral measure. |
| dependency | [Scalar actuality criterion](Yin_C_F0255_v1.md#statement) | Bounded diffuse circle densities admit the scalar divided-difference vacuum. |
| dependency | [Phase coupling](Yin_C_F0265_v1.md#statement) | Actuality and full strong duals on the finite secant-energy free phase model. |
| dependency | [Exchange of Haar marginals](Yin_C_F0315_v1.md#actuality-of-the-product-law) | The product law construction gives a Haar second marginal and a trace-preserving exchange involution. |
| dependency | [Phase-coupling bound](Yin_C_F0320_v1.md#statement) | The unbounded slice on contractions in the example is controlled after normalization by the joint vacuum. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:46 |
| status | proved |
| reason | Adopt the exact four-point Gram identity, its three-factor bounds under comparability, and the limits of marginal-only control after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Matrix inverse density, singular mass, trace defect and projected and three-factor slice estimates, with an actual degenerating family. |
| argument | [Argument](#argument) | Commutator representing the product integral, spectral disintegration, scalar adjoint duality and the two-channel free unitary calculation. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Scalar divided differences, the reversed coordinate and the actual starred derivative. |
| dependency | [Omitted algebra](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Joint bounded approximants for Borel factors of the omitted coordinate. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Complex scalar forward and adjoint estimates and mass of the integrable marginal weight. |
| dependency | [Ordered output pairing](Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs) | Core adjoint pairing and weighted adjoint duality, here applied in the terminal variable of the matrix spectral measure. |
| dependency | [Scalar actuality criterion](Yin_C_F0255_v1.md#statement) | Bounded diffuse circle densities admit the scalar divided-difference vacuum. |
| dependency | [Phase coupling](Yin_C_F0265_v1.md#statement) | Actuality and full strong duals on the finite secant-energy free phase model. |
| dependency | [Exchange of Haar marginals](Yin_C_F0315_v1.md#actuality-of-the-product-law) | The product law construction gives a Haar second marginal and a trace-preserving exchange involution. |
| dependency | [Phase-coupling bound](Yin_C_F0320_v1.md#statement) | The unbounded slice on contractions in the example is controlled after normalization by the joint vacuum. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0331_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
