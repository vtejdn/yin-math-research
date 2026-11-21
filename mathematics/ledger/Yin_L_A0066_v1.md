---
author: Yin
---
# Fourier tensor bounds and augmentation obstructions to constant-field splitting

This 21 November 2026 development concerns the biquadratic splitting equations in [C104v2](../claims/Yin_C_A0104_v2.md#statement) under the rational-square hypothesis of [A0001](../tasks/Yin_T_A0001_v1.md#contract).
It uses the actual diagonal group embedding, with the canonical Fourier coefficients and trace.
The results below give sufficient regularity obstructions; they do not show that arbitrary rational affiliated inputs possess that regularity.
They also distinguish a constant-field splitting obstruction from the existence of a quaternion subalgebra itself.
This is development and comparison, without a new selected assessment or independent review.

## The coproduct as a Hilbert tensor

Let \(M=\mathcal N(G)\), with its canonical trace, and let
\[
 \Delta:M\longrightarrow M\overline\otimes M,\qquad \Delta(g)=g\otimes g.
 \tag{1}
\]
The [actual diagonal-subgroup argument](Yin_L_A0027_v1.md#the-diagonal-map-and-the-exact-tensor-identity) makes this an injective normal trace-preserving star homomorphism.
It extends to affiliated operators and isometrically to \(L^2\).
For \(x\in L^2(M)\), write \(x_g=\tau(g^{-1}x)\).
Then
\[
 \Delta(x)=\sum_{g\in G}x_g\,g\otimes g
 \quad\text{in }L^2(M)\otimes_2L^2(M).
 \tag{2}
\]

Reshape this Hilbert tensor as the Hilbert--Schmidt map
\[
 T_x:\overline{\ell^2(G)}\longrightarrow\ell^2(G),\qquad
 T_x(\overline{\delta_g})=x_g\delta_g.
 \tag{3}
\]
Its nonzero singular values are precisely the numbers \(|x_g|\).
Consequently
\[
 \operatorname{rank}T_x=|\{g:x_g\ne0\}|,\qquad
 \|T_x\|_{S_1}=\sum_g|x_g|,
 \tag{4}
\]
with infinite values allowed.
The second quantity is also the projective Hilbert-tensor norm of (2).
It is not the trace-class norm of the convolution operator \(\Delta(x)\) on \(\ell^2(G^2)\).
Keeping these two operator interpretations separate is essential.

Thus finite Hilbert tensor rank of \(\Delta(x)\) is equivalent to \(x\) having finite Fourier support.
Finiteness of its Schmidt \(S_1\)-norm is equivalent to \(x\in\ell^1(G)\).
In the latter case the Fourier series converges absolutely in operator norm, so the original affiliated \(x\) is the bounded convolution operator given by that series.
These assertions require no Atiyah hypothesis.

## Finite affiliated decompositions of an \(L^2\) tensor

The preceding finite-rank assertion also applies when a finite tensor decomposition is initially presented with affiliated factors.
For finite von Neumann algebras \(M,N\), one has, inside the affiliated algebra of their product,
\[
 L^2(M\overline\otimes N)\cap
       \bigl(U(M)\otimes_{\mathrm{alg}}U(N)\bigr)
 =L^2(M)\otimes_{\mathrm{alg}}L^2(N).
 \tag{5}
\]
Here the algebraic tensor product is over \(\mathbb C\), with its natural spatial affiliated realization.

We give the bounded-denominator and slice justification.
First this algebraic tensor realization is injective.
For a minimal nonzero sum \(\sum_i a_i\otimes b_i\), both lists can be taken complex linearly independent.
Choose bounded affiliated units \(c\in M,\ d\in N\) such that all \(ca_i\) and \(db_i\) are bounded.
For example, the common left bounded transform of the corresponding affiliated row has this property.
Multiplication by these units preserves linear independence.
The tensor \(\sum_i ca_i\otimes db_i\) is then nonzero as a Hilbert tensor, as is seen by applying bounded coordinate functionals to its independent factor lists.
Hence the initial affiliated sum was nonzero.

Now suppose
\[
 X=\sum_{i=1}^r a_i\otimes b_i\in L^2(M\overline\otimes N)
 \tag{6}
\]
is a minimal decomposition, and choose \(c,d\) as above.
The bounded \(db_i\) have an invertible finite \(L^2(N)\)-Gram matrix.
There are bounded elements \(\beta_k\), in their complex span, with
\(\tau_N(\beta_k^*db_i)=\delta_{ki}\).
The slice
\[
 y_k=(\operatorname{id}\otimes\tau_N(\beta_k^*\,\cdot\,))
                 ((1\otimes d)X)
 \tag{7}
\]
belongs to \(L^2(M)\).
Indeed \(d\) is bounded and the slice is a bounded map from the Hilbert tensor product to \(L^2(M)\).
After multiplication by the bounded \(c\), all factors in the finite expansion are bounded, and the same slice gives
\[
 c y_k
 =(\operatorname{id}\otimes\tau_N(\beta_k^*\,\cdot\,))
       \left(\sum_i ca_i\otimes db_i\right)
 =c a_k.
 \tag{8}
\]
Cancellation of the affiliated unit \(c\) gives \(a_k=y_k\in L^2(M)\).
This is equality in the affiliated algebra, not application of an unbounded inverse to an arbitrary Hilbert-space vector.

For a version using bounded cuts explicitly, let \(e_m\uparrow1\) be common left spectral cuts making each \(e_m a_i\) bounded.
Taking the same slice of \((e_m\otimes d)X\) gives \(e_my_k=e_ma_k\).
Their difference has left support orthogonal to every \(e_m\), and hence is zero.
This gives the same conclusion without an assertion that a slice is defined directly on the unbounded summands.

Interchanging the two factors and using bounded duals to the independent \(ca_i\) proves \(b_k\in L^2(N)\).
Every slice in this argument is applied to an \(L^2\) element, and every displayed finite expansion used to evaluate it has been made bounded.
The reverse inclusion in (5) is immediate.
This proves (5).

In particular, if \(x\in L^2(M)\) and
\[
 \Delta(x)=\sum_{i=1}^r a_i\otimes b_i,\qquad a_i,b_i\in U(M),
 \tag{9}
\]
then (5) and (4) show that \(x\in\mathbb C[G]\) and its Fourier support has at most \(r\) elements.
No conclusion is asserted here for a general affiliated \(x\notin L^2(M)\).
Nor does finite Fourier support of an element of the rational division closure by itself identify its Fourier coefficients as rational.

## Matrix units cannot all have summable coproduct tensors

The absolutely summable group algebra has its genuine augmentation character
\[
 \varepsilon:\ell^1(G)\longrightarrow\mathbb C,\qquad
 \varepsilon\left(\sum_g x_g g\right)=\sum_gx_g.
 \tag{10}
\]
Absolute convergence makes it a unital algebra homomorphism, with
\(|\varepsilon(x)|\le\|x\|_1\).
This does not extend augmentation to arbitrary bounded or affiliated operators.

Suppose \(X,Y\in U(G)\) satisfy the two-square matrix-unit relations
\[
 X^2=Y^2=0,\qquad XY+YX=1.
 \tag{11}
\]
They cannot both belong to \(\ell^1(G)\).
Otherwise their augmentations have square zero in \(\mathbb C\), and hence both vanish, whereas the last relation has augmentation one.
It suffices, therefore, that both are in \(L^2\) and that their coproduct tensors have finite Schmidt \(S_1\)-norm to rule out (11).
The finite affiliated tensor decompositions in (9) are a stronger sufficient condition.
In particular a unital splitting system of matrix units cannot have this regularity for both off-diagonal entries.

There is a uniform quantitative version.
For arbitrary \(X,Y\in\ell^1(G)\), put
\[
 \eta_1=\|X^2\|_1,\qquad
 \eta_2=\|Y^2\|_1,\qquad
 \eta_3=\|XY+YX-1\|_1.
\]
Applying (10) gives
\[
 1\le 2\sqrt{\eta_1\eta_2}+\eta_3.
 \tag{12}
\]
Indeed \(|\varepsilon(X)|^2\le\eta_1\),
\(|\varepsilon(Y)|^2\le\eta_2\), and
\(|2\varepsilon(X)\varepsilon(Y)-1|\le\eta_3\).
Thus the three relation errors cannot all be less than \(1/3\).
The common bound \(1/3\) is sharp: \(X=Y=1/\sqrt3\) gives all three errors equal to \(1/3\).
By (4), the same assertion can be phrased in the Schmidt \(S_1\)-norms of the coproducts of these errors.
Approximation merely in operator norm or \(L^2\) is not covered by this estimate.

This obstruction concerns the matrix units in the constant-field splitting, not every quaternion generating pair.
The next two tests apply directly to the pair of equations in C104v2.

## Augmentation-compatible rational denominators

Assume the rational-square hypothesis of [C104v2](../claims/Yin_C_A0104_v2.md#statement), and write
\(D=\operatorname{Div}_{U(G)}(\mathbb Q[G])\).
Consider the subring \(\mathcal R_{\mathrm{aug}}\subset\ell^1(G)\) obtained from \(\mathbb Q[G]\) by finite ring operations and entries of matrix inverses that exist in the relevant matrix algebra over \(\ell^1(G)\).
It has the property
\[
 \varepsilon(\mathcal R_{\mathrm{aug}})\subseteq\mathbb Q.
 \tag{13}
\]
For every inverse step, apply (10) entrywise: the augmentation of the inverse is the inverse of a rational matrix and has rational entries.
Induction proves (13).
Under the present hypothesis \(\mathcal R_{\mathrm{aug}}\subset D\): a matrix over \(D\) that is invertible in the affiliated algebra is already invertible over the division ring \(D\), by Gaussian elimination.

Let \(a,b\in\mathbb Q^\times\) have independent square classes.
There are no \(u,v\in\mathcal R_{\mathrm{aug}}\) satisfying
\[
 uv+vu=0,\qquad u^2+a v^2=b.
 \tag{14}
\]
Their rational augmentations \(r,s\) would satisfy
\[
 2rs=0,\qquad r^2+a s^2=b.
 \tag{15}
\]
If \(s=0\), then \(b\) is a rational square; if \(r=0\), then \(b/a\) is one.
Both contradict the square-class hypotheses.
This test allows arbitrary noncommuting supports and imposes no cyclic-subgroup assumption.
A finite matrix denominator with an explicit \(\ell^1\) Neumann bound is one verifiable sufficient input for the required inverse step.

An element of \(D\) that happens to belong to \(\ell^1(G)\) has not thereby been given such an augmentation-compatible rational realization.
The conclusion (13) must not be assigned to all of \(D\cap\ell^1(G)\) without a separate argument.
Likewise an inverse existing only in \(U(G)\), or only in the reduced group \(C^*\)-algebra, need not be an \(\ell^1\) inverse.

## Real coefficients, nonskew inputs and the bounded skew case

There is a stronger sign-specific test that does not need the denominator condition (13).
Complex conjugation in the canonical group basis is an antiunitary \(J\) with
\[
 JxJ=x\qquad(x\in D).
 \tag{16}
\]
It fixes \(\mathbb Q[G]\) and preserves the closed affiliated ring operations and actual inverses, so (16) holds throughout the division closure.
Consequently any \(x\in D\cap\ell^1(G)\) has real Fourier coefficients and real augmentation.

If \(a>0\) and \(b<0\), there are no \(u,v\in D\cap\ell^1(G)\) with \(u^2+a v^2=b\).
Their real augmentations would have a sum of nonnegative squares equal to a negative number.
No normality, skew-adjointness or anticommutation is needed for this conclusion.
In particular it applies when one or both rational inputs are nonskew, provided the absolute Fourier summability is independently established.

For any skew-adjoint \(x\in D\cap\ell^1(G)\), one also has
\[
 \varepsilon(x)=0.
 \tag{17}
\]
Its augmentation is real by (16), while the star relation makes it purely imaginary.
Equivalently its real Fourier coefficients satisfy \(x_{g^{-1}}=-x_g\), and absolute convergence allows their cancellation.
Thus two such skew-adjoint inputs cannot satisfy \(u^2+a v^2=b\) for any nonzero rational \(b\), regardless of the sign of \(a\).

For the important sign choice \(a>0,b<0\), skew-adjointness supplies the \(L^2\) premise automatically.
The relation becomes
\[
 u^*u+a v^*v=-bI.
 \tag{18}
\]
Positivity implies that both operators are bounded, with
\(\|u\|\le\sqrt{-b}\) and \(\|v\|\le\sqrt{-b/a}\).
Hence if both coproducts admit finite affiliated tensor decompositions, (5) makes the two inputs finite Fourier sums and (17) contradicts (18) after augmentation.
The weaker assumption of finite Schmidt \(S_1\)-norm for both coproducts gives the same contradiction.

For skew-adjoint \(U,V\in\ell^1(G)\) with real Fourier coefficients, even an approximate constant-square relation has the exact lower bound
\[
 \|U^2+aV^2-bI\|_1\ge |b|,
 \tag{19}
\]
by augmentation.
This identifies the topology in which finite Fourier truncations cannot approximate the required relation.
It does not preclude approximation in \(L^2\).
Knowing only \(u^2,v^2\in\ell^1(G)\) would not define the augmentations of \(u,v\), so it does not suffice for these arguments.
For a nonamenable group, positivity in the regular representation also does not by itself imply positivity of an augmentation value.

## An actual group-ring quaternion pair

It would be incorrect to conclude that canonical group algebras admit no quaternion structure.
Consider the torsion-free Klein bottle group
\[
 G_0=\langle g,h\mid hgh^{-1}=g^{-1}\rangle
       \cong\mathbb Z\rtimes\mathbb Z.
 \tag{20}
\]
It is among the [already controlled group classes](Yin_L_A0001_v1.md#known-positive-results); see also the [earlier Klein bottle calculation](Yin_L_A0002_v1.md).
Its direct powers are torsion-free elementary amenable and have the known complex Atiyah property.
Set
\[
 u=g-g^{-1},\qquad v=h-h^{-1}.
 \tag{21}
\]
Both are nonzero finite rational group-ring elements, skew-adjoint and affiliated-invertible by the cyclic Haar calculation.
The defining relation gives
\[
 uv=-vu.
 \tag{22}
\]
Their squares commute with both generators of this algebra:
\[
 s=u^2=g^2+g^{-2}-2,\qquad
 t=v^2=h^2+h^{-2}-2.
 \tag{23}
\]
The subgroup \(\langle g,h^2\rangle\) is \(\mathbb Z^2\).
Its independent Haar coordinates show that the two displayed nonconstant functions are algebraically independent over \(\mathbb Q\).
Thus \(F=\mathbb Q(s,t)\) is an actual central field for the subalgebra generated by \(u,v\).

The four elements \(1,u,v,uv\) are linearly independent over \(F\).
The sign automorphism for the quotient by \(\langle g,h^2\rangle\) separates the terms \(A+Bu\) and \((C+Du)v\).
In the even abelian algebra, inversion of \(g\), fixing \(h^2\), fixes \(F\) and changes \(u\) to \(-u\).
It therefore forces \(A=B=0\), and, after cancellation of the unit \(v\), forces \(C=D=0\).
This argument is valid in the affiliated abelian field as well as for bounded elements.
The resulting four-dimensional \(F\)-algebra has exactly the quaternion relations
\[
 u^2=s,\qquad v^2=t,\qquad uv=-vu.
 \tag{24}
\]
It lies in the known rational division ring of \(G_0\), so it has no zero divisors and is a quaternion division algebra.

Both \(\Delta(u)\) and \(\Delta(v)\) have finite tensor rank two.
Thus finite coproduct rank does not exclude quaternion generators themselves.
Here \(s,t\) are algebraically independent: there is no relation \(s+a t=b\) with rational constants as in (14).
Nor does this example provide the constant-field splitting or matrix units of C104.
It complements, rather than contradicts, the [individual Cayley-transform exclusion](../claims/Yin_C_A0102_v1.md#exclusion-for-cayley-transforms-of-actual-group-elements).

## The remaining implication

The [earlier diagonal tensor investigation](Yin_L_A0027_v1.md#conditional-expectations-and-a-precise-projection-calibration) already showed that correct trace marginals and diagonal-overlap inequalities alone need not force integral or vanishing kernel mass.
The present tests use additional information: Fourier summability, a finite tensor decomposition with an \(L^2\) input, or an actual augmentation-compatible rational denominator.
No argument here obtains one of those properties from rationality in \(D\), from the dimension saturation \(s^2=4\), or from the existence of an arbitrary affiliated splitting.
For a proposed matrix-unit construction it is enough to establish the indicated regularity of its two off-diagonal entries.
For the specific biquadratic equations, the denominator and sign tests above give separate, directly verifiable sufficient exclusions.
The unrestricted nonskew affiliated pair remains outside these exclusions.
