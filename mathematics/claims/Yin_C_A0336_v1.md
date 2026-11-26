---
author: Yin
---

# Twenty determinant lines for failure of the index-four character test

## Statement

Use the [noncyclic order-twenty marking](Yin_C_A0333_v1.md#statement) of a torsion-free scalar-injective group \(H=\langle s,t\rangle\), a half-nullity two-square rectangle \(K=P(t)-sQ(t)\), and its polynomial \(f(x,y)=\det(P(y)-xQ(y))\).
Let \(N\) be the kernel of the two signs, and \(R_N\in M_4(\mathbb CN)\) the [commutator of the two signed involutions, translated into \(N\)](Yin_C_A0331_v1.md#two-involutions-with-a-polynomial-commutator).
Either a scalar character of \(N\) gives \(R_N\) numerical rank at least three, or \(f\) belongs to twenty explicitly determined projective coefficient lines.
In the first case the group-ring inner rank of \(R_N\) is at least three and is exactly two over the second actual scalar inverse layer, by the [normalized kernel basis](Yin_C_A0331_v2.md#statement).

In the second case, after a choice of mark orientation, inversion of a mark if needed and a unitary character twist, one has, up to a nonzero constant multiplier,
\[
 f(x,y)=-1+\sigma\sqrt5\,y-2y^2+x^2(2-\sigma\sqrt5\,y+y^2),\qquad \sigma=\pm1.
\]
The transfer \(M(y)=P(y)Q(y)^{-1}\) in this orientation is traceless.
It is holomorphic on a neighborhood of the closed unit disk, and its inverse is bounded on the unit circle.
Its square is a scalar finite Blaschke product of degree two times the identity.
Consequently a failure of the five character tests confines the oriented transfer to this explicit analytic class.
No existence of a half kernel on these lines is asserted.

## Character ranks and zero orders on the grid

In the marked quotient the twenty characters give five squares \((x,y)=(\epsilon z,\eta z^2)\) for \(z^5=1\) and two independent signs.
The restriction to \(N\) is the same for all four members of each square.
At such a character the two specialized involutions in the commutator formula preserve their commutator kernel and commute there.
Their four joint eigenspaces are precisely the intersections of the two signed planes, as in the [original calculation](Yin_C_A0331_v1.md#two-involutions-with-a-polynomial-commutator).
The dimensions of the intersections are the nullities of the four numerical rectangles in that square.
Thus the numerical rank of \(R_N\) on \(N\) is four minus the sum of these four nullities.
This computation uses ordinary matrices and still applies to a singular value of either cyclic pencil.

All four corner coefficients of \(f\) are nonzero, by the [two mixed extremal deformations](Yin_C_A0311_v1.md#the-two-ends-in-the-equality-case).
At most one of the twenty numerical matrices \(P(y)-xQ(y)\) can be the zero matrix.
Indeed the row of monomials \((1,y,x,xy)\) is different and linearly independent at any two distinct points.
Two zero matrices would therefore put the four numerical coefficient matrices in a common span of dimension at most two.
This span contains an invertible matrix, for instance \(B\).
Multiplication by its inverse and a constant similarity put the whole span in upper triangular form, since a single additional numerical matrix can be triangularized.
The two diagonal group-ring entries are nonzero: each has nonzero coefficient at the identity after normalization to \(B=I\), and the four group labels have different binary degrees.
Both are units in \(U(H)\) by scalar injectivity.
The triangular rectangle would be invertible there, a contradiction.

If all five character ranks are at most two, then each square has at least two distinct zeros of \(f\), except possibly one square containing a zero matrix.
At a zero matrix both first partial derivatives of its determinant vanish.
Multiplication of both mark coordinates by the values of an actual character permutes the grid transitively, preserves the corner condition and moves that point to \((1,1)\).
The exceptional possibility is thus included in the test with \(f=f_x=f_y=0\) there and two prescribed distinct zeros in each other square.

## The coefficient lines

Use the monomial basis \(x^iy^j,\ 0\le i,j\le2\).
For two prescribed zeros on each square take their ten evaluation rows.
For a zero matrix at \((1,1)\) take the three evaluation and derivative rows there and the eight evaluation rows from the other four squares.
The [exact sign-square verifier](../computations/programs/Yin_J_A0010/verify_fifth_sign_squares.py) solves these systems over the fifth cyclotomic field.
Of the \(6^5=7776\) two-zero choices, \(120\) allow all four corner coefficients to be nonzero and give just twenty distinct projective coefficient vectors.
For the \(6^4=1296\) derivative choices none allows all four corners to be nonzero.
Reduction modulo \(101\) detects full rank by a nonzero minor; the surviving systems are checked in characteristic zero.
The calculation over the cyclotomic field also applies to complex coefficients by extension of scalars.

Here is an explicit identification of all twenty vectors.
In the original grid, \(x^2=y^{-4}\) and \(y^2=x^4\).
For the family even in \(x\), replace \(h=t\) by \(t^{-1}\) and multiply the rectangle on the right by \(t^{-1}\), so that the cyclic polynomials become \(yP(y^{-1}),yQ(y^{-1})\).
For the family even in \(y\), take the adjoint orientation \((g,h)=(t^{-1},s^{-1})\) as in the [adjacent-edge proof](Yin_C_A0333_v1.md#adjacent-nonzero-values-on-the-five-sign-squares).
In either description the resulting character set is \(y\in\mu_{10},\ x^2=y^4\), and the normalized polynomial is even in \(x\).
For completeness one can identify the list by exhibiting twenty distinct lines passing the counted tests, without assuming the parity in advance.

Choose a primitive fifth root \(\zeta=\exp(2\pi i/5)\).
In these oriented coordinates let \(f_\sigma(x,y)\) be the two displayed polynomials in the statement.
Substitution of \(x^2=y^4\) gives
\[
     y^6-\sigma\sqrt5\,y^5+2y^4-2y^2+\sigma\sqrt5\,y-1.
\]
Its roots are \(1,-1,\zeta,\zeta^{-1},-\zeta^2,-\zeta^{-2}\) for \(\sigma=1\); for \(\sigma=-1\) negate all six roots.
Indeed the product for the first list is \((y^2-1)(y^2-(\zeta+\zeta^{-1})y+1)(y^2+(\zeta^2+\zeta^{-2})y+1)\).
The two remaining labels \(x=\pm y^2\) both give zeros at each of these six values.
Thus there are four zeros on exactly one sign square and two on each of the others.
Rotating \(y\) by any fifth root \(\kappa\) and \(x\) by \(\kappa^2\) moves the unique four-zero square through all five positions.
The two signs have different root sets at fixed position.
Pull these ten lines back along each orientation above, allowing complex conjugation of coefficients when taking the adjoint.
Ten are even in the original first variable with a nonzero odd coefficient in the second, and ten have the reversed parity.
They are distinct, so they exhaust the exact count.

## A circle-valued scalar square of the transfer

In the normalized coordinates \(f(y_0,y)=\det Q(y)\big(y_0^2-y_0\,{\rm tr}\,M(y)+\det M(y)\big)\).
Comparison with the two prototypes gives \({\rm tr}\,M=0\) and, by the characteristic identity,
\[
               M(y)^2=\frac{1-\sigma\sqrt5\,y+2y^2}{2-\sigma\sqrt5\,y+y^2}\,I .
\]
The roots of the numerator have modulus \(1/\sqrt2\), and those of the denominator have modulus \(\sqrt2\), as the real quadratics have negative discriminants and the products of their conjugate roots are \(1/2\) and \(2\), respectively.
The denominator is the reversal of the numerator.
The scalar is the product of the two elementary disk factors for the numerator roots, with value \(1/2\) at zero.
In particular it has unit modulus and no zeros or poles on the unit circle.
The polynomial \(\det Q\) is a nonzero constant multiple of this denominator, so every entry of \(M\) is holomorphic on the asserted neighborhood.
Likewise \(\det P\) is a nonzero constant multiple of the numerator, proving the boundary assertion for \(M^{-1}\).
Both have absolutely summable Laurent coefficients on the circle by analyticity on an annulus containing it.
