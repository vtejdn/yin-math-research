---
author: Yin
---
# The binary type and matching equations allow both exceptional seven-color parities

Consider the projective-plane types and signed alphabet of [Ope26f, §2.1](../literature/pdf/Ope26f.pdf#page=4).
Fix **any** inverse pairing permitted there.
The three extras are paired with distinct ordinary points \(o_1,o_2,o_3\).
Retain just the following constraints modulo two on the count of each full vertex type in each \(C_7\)-color: the total on each type must have its prescribed parity, and the two ends of each inverse-pair matching must have identical stub counts after the prescribed color shift.
These linear constraints have solutions in which both forward parity indicators are \(D=\{0,1,2,4\}\), for an explicit choice of a surjective increment map.
Inverting the column labels gives the exceptional pair \(D,-D\) of the [seven-fiber test](Yin_L_A0046_v1.md#complete-fibers-with-arbitrary-positive-odd-multiplicities).
This is a limitation of that binary system even with all original type totals imposed.

## A line-code vector for the given inverse pairing

Write \(v=16513\) for the number of points and lines in the projective plane of order \(128\).
Take \(\mathbb F_8=\mathbb F_2(\omega)\) with \(\omega^3+\omega+1=0\).
First construct a sum of line indicators over \(\mathbb F_8\) which vanishes at precisely \(o_1,o_2,o_3\).
The sum of its line coefficients will be one.

For \(j=1,2\) choose three lines \(\ell_{j,i}\), one through each \(o_i\), avoiding the other two special points.
Choose the second triple disjoint as a set of lines from the first.
At each special point there are 129 lines through it and these requirements exclude at most five.
Set \(b_j=\mathbf1+\sum_i\mathbf1_{\ell_{j,i}}\) as a function on all points with binary values.
Each \(b_j\) vanishes at all the special points, and its zero set is contained in its union of three lines.
Since two different projective lines meet in one point, the common zero set \(Z_0\) of \(b_1,b_2\) has size at most nine.

For the third triple choose a line through each \(o_i\) avoiding all other points of \(Z_0\).
At most eight lines through \(o_i\) are forbidden.
Choose an additional line \(L_*\) avoiding \(Z_0\) and distinct from these three lines, possible since at most \(9\cdot129+3<v\) lines are excluded.
Let \(b_3=\mathbf1+\sum_i\mathbf1_{\ell_{3,i}}+\mathbf1_{L_*}\).
At each \(o_i\) this is zero and at each remaining point of \(Z_0\) it is one.
The binary functions \(b_1,b_2,b_3\) thus have exactly the three prescribed common zeros, including when the special points are collinear.

In the binary line span \(\mathbf1\) is the sum of all \(v\) line indicators since each point lies on 129 lines.
That expression has coefficient sum one since \(v\) is odd.
The displayed expressions for \(b_1,b_2\) consequently have coefficient sums zero, and the one for \(b_3\) has coefficient sum one.
Let
\[
       S=\omega b_1+\omega^2 b_2+b_3
        =\sum_L z_L\mathbf1_L,\qquad z_L\in\mathbb F_8.
\]
The independence of \(\omega,\omega^2,1\) shows that \(S\) vanishes only at the three special points, and \(\sum_L z_L=1\).

## Prescribed increments and the two forward indicators

For a binary color vector identify the color-\(c\) entry with the coefficient of \(X^c\) in
\[
 R=\mathbb F_2[X]/(X^7-1)
    \simeq\mathbb F_2\times\mathbb F_8\times\mathbb F_8,\qquad
                             f\longmapsto(f(1),f(\omega),f(\omega^{-1})).
\]
The isomorphism follows from the linear and two cubic factors in [C_A0042](../claims/Yin_C_A0042_v1.md#separating-the-cubic-factors).
Use the binary color histogram \((0,z_L,0)\) on the empty-extra type of each line \(L\) on each of the two forward sides.
Give every other full type the zero vector.
The first coordinate measures parity of the total number of vertices of that type.
It is zero for all these vectors; the prescribed totals on both sides have that parity whenever \(n\) is a multiple of \(4v^2\).
The resulting aggregate stub vector for an ordinary label \(t\) is \((0,S(t),0)\), and for each extra it is zero.

For each ordinary-ordinary inverse pair specify \(d_t\in C_7\) by \(\omega^{d_t}=S(\bar t)/S(t)\), using the negatives on reverse readings.
Both entries are nonzero, so the ratio belongs to \(\mathbb F_8^\times=\langle\omega\rangle\).
At the extra-special pairs both vectors vanish; choose at least one nonzero increment there and assign its negative to the inverse letter.
These prescriptions give a surjection from the free rose group to \(C_7\).
For each type of signed letter, the aggregate stub vector at \(\bar t\) now equals \(X^{d_t}\) times the aggregate stub vector at \(t\), the required matching equation in \(R\).
This holds simultaneously on both forward sides.

The forward sum of all type vectors is \((0,1,0)\) on each side.
It is represented by \(1+X+X^2+X^4\): \(\omega+\omega^2+\omega^4=0\) while the sum of the three inverse powers is one since all six nonidentity powers sum to one.
Thus the odd masks in forward colors are \(D,D\), or \(D,-D\) for the two factor orientations.
Any subsequent independent root-relative shifts translate these masks and leave their two opposite nontrivial Fourier orbits unchanged.

Every individual binary type histogram can be represented by nonnegative integer counts of its *exact* prescribed total for all sufficiently large multiples of \(4v^2\).
Indeed each positive type count grows linearly, has the prescribed even parity, and one may first assign one or two vertices to every color according to its parity, then add the remaining vertices in pairs.
This last operation can even give full occurrence occupancy on both sides.
It need not make the two ends of a matching agree as **integers**; their agreement in this construction is modulo two.
It establishes neither a compatible connected matching nor a quotient of an actual cone group.
The example shows why neither the parity of prescribed type counts nor all the binary stub equations by themselves imply that one of the two parity indicators vanishes.
Integral matching constraints, connectivity, and possible erasure of even occupied classes on collection remain further tests.
