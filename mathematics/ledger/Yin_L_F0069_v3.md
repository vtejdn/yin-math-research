---
author: Yin
---

# An exterior with one deleted scalar direction for the words \(x^q y+yx\)

<a id="partial"></a>
## Exact partial linearization at every fixed degree

Fix \(q\ge2\), put \(P_q=1+x^q y+yx\), and use real symmetric inputs \(X,Y\).
The [projected-pair energy and sign obstruction](Yin_L_F0069_v2.md#energy) concern the earlier exposure for \(q=2\).
The [proved cubic restoration](../claims/Yin_C_F0362_v2.md#restoration) instead keeps \(Y\) fixed and restores fresh \(X\)-columns.
The following identities determine which parts of that construction survive as \(q\) increases.

Use \(q\) channels.
The first block row of \(K_q(w)\) begins \(((1-w)I+YX,X)\).
For \(2\le j\le q\) put \(-I\) on diagonal block \(j\); for \(2\le j<q\) put \(X\) on block \((j,j+1)\).
Put \(XY\) on block \((q,1)\), and set all other blocks to zero.
Successive elimination of the auxiliary channels gives scalar Schur complement \(P_q(X,Y)-wI\).
On two sites \(e,u\) with \(u\) supported outside the deleted sites, replace \(X\) by \(X+eu^{\mathsf T}+ue^{\mathsf T}\).
For a physical vector \(a\) define \(F(a)\) by its \(q+1\) columns: \(a\) on channel one, \(Ya\) on channel one, and \(a\) separately on each of channels \(2,\ldots,q\).
Then
\[
 \Delta K_q=F(e)D F(u)^{\mathsf T}+F(u)D F(e)^{\mathsf T},
\]
where \(D\) has ones at \((2,1),(1,3),(3,4),\ldots,(q,q+1),(q+1,2)\), omitting the consecutive pairs when \(q=2\).
It is a permutation matrix.
Multiplication gives \(Y(eu^{\mathsf T}+ue^{\mathsf T})\) at the top left, \((eu^{\mathsf T}+ue^{\mathsf T})Y\) at \((q,1)\), and the plain increment on each superdiagonal block.

For deleted sites \(I\) let \(J=I^c\), \(V=Y_{JI}\), and take the same exterior on both sides, orthogonal to the columns of \(F(e_i)\) for \(i\in I\).
All \(q\) physical channels are supported on \(J\), the first is perpendicular to \(V\), and the other \(q-1\) channels are free there.
The two mixed principal-block increments are \(V X_{IJ}\) at the top left and \(X_{JI}V^{\mathsf T}\) at the bottom left.
These disappear on the indicated sides of the restriction.
Eliminating the auxiliary pivot on these spaces gives
\[
  Q^{\mathsf T}\bigl(P_q(X_{JJ},Y_{JJ})-wI\bigr)Q
\]
for a real orthonormal frame \(Q\) of \(\operatorname{ran}(V)^\perp\) in \(J\).
Thus each new background column corresponds to just one initial scalar deletion.
The identity holds also at an odd initial gap.

<a id="residues"></a>
## An invertible matrix detected by commuting residues

At commuting values \(x,y\), the scalar denominator is \(f(x,y)-w=1+(x^q+x)y-w\).
At a regular parameter the inverse of \(K_q\) is the sum of a polynomial auxiliary-pivot term and an outer product divided by \(f-w\).
This is the block inverse formula; the lifted right mode is \((1,x^{q-1}y,\ldots,xy)\) and the lifted left mode is \((1,x,\ldots,x^{q-1})\).
After applying \(F\) on each side, the unscaled numerator vectors become
\[
       l=(1,y,x^{q-1}y,\ldots,xy)^{\mathsf T},\qquad
       r=(1,y,x,\ldots,x^{q-1})^{\mathsf T}.
\]
Transpose-symmetrization in the physical coordinates does not change a commuting scalar evaluation.

For \(w\ne1\) and \(x>0\) specialize to the pole \(y=(w-1)/(x^q+x)\).
The \(q+1\) components of each vector are independent functions of \(x\).
For \(l\), clearing the denominator leaves one degree-\(q\) polynomial and the full span of monomials of degrees zero to \(q-1\).
For \(r\), a dependence would give \((x^q+x)p(x)+a=0\) for a polynomial of degree at most \(q-1\) and a constant \(a\), implying that both vanish.
There are therefore \(q+1\) positive sampling points \(x_j\) at which both evaluation matrices are invertible.
Indeed each of the two determinants is a nonzero rational function of the sampling points and their simultaneous nonvanishing occurs on a nonempty open set.
For \(y_j=(w-1)/(x_j^q+x_j)\), the sum \(\sum_j l(x_j,y_j)r(x_j,y_j)^{\mathsf T}\) is their matrix product and is invertible.

In any free rational relation modulo scalars among finitely many distinct shifts, specializing to commuting values and taking the residue at this node annihilates each of these outer products under pairing with the relation coefficients for that node.
The polynomial pivot term and the other nodes are regular there.
This verifies an invertible commuting-residue direction for each nonunit node.
To conclude the [fixed-number-of-directions probability bound](../claims/Yin_C_F0363_v3.md#statement) one still needs suitable basis kernels with joint spread on actual physical corners and the independent-panel estimates.
The residue test alone does not establish those properties or any low-singular-value probability estimate.

For \(q>2\), one also needs initial principal trims strong enough to seed this exterior, or a replacement estimate valid for its actual initial near-kernel.
The cubic proof of such trims uses a two-window argument particular to its [four-channel linearization](../claims/Yin_C_F0362_v1.md#direction).
The formulas above extend the exterior and one algebraic test to arbitrary fixed \(q\); full Brown and ordinary determinant limits for these higher words remain open here.
