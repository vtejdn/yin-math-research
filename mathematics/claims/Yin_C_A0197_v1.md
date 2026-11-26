---
author: Yin
---

# A finite-support kernel column at a saturated finite-phase bound

## Statement

Let \(H\) be a discrete group for which every nonzero element of \(B=\mathbb CH\) acts injectively in the regular representation, and use the unnormalized matrix trace for von Neumann dimension.
Consider \(Q(z)=\sum_{j=0}^d Q_j z^j\) with \(Q_j\in M_h(B)\), \(d\ge1\).
If \(Q_d\) is invertible over \(B\), and at least one \(m\)-th root of unity \(\omega\) has \(0<\dim_H\ker Q(\omega)<1\), then
\[
                \sum_{\omega^m=1}\dim_H\ker Q(\omega)\ \le\ hd-1 .
\]
The same conclusion holds if \(Q_0\) is invertible over \(B\).
There is a second sufficient condition: the maximal regular rank of \(Q\) is \(h\), and \(Q_0\) or \(Q_d\) has rank at most \(h-1\).
Under this condition the inequality holds without an assumption on group-ring scalars or a fractional kernel.

Now let \(H=\langle s,t\rangle\) be torsion-free with the stated scalar injectivity, let \(H\twoheadrightarrow C_m\), and consider the four-site matrix \(K=B_0+At-s(D+Ct)\) with complex two-by-two coefficients.
At \(m=23\) and at every \(m\ge27\), \(K\) cannot have rank \(3/2\).
The same orders exclude a half-dimensional constant-column increment in the [four-column pencil with two occurrences of each label](Yin_C_A0184_v1.md#statement).
The [integer-character result](Yin_C_A0179_v1.md#statement) therefore leaves only finite abelianization of exponent at most 26 for such a half increment, and exponent 23 is also excluded.

## The companion and a column over the original group ring

Suppose \(Q_d^{-1}\in M_h(B)\).
The degree-\(d\) monic block companion \(T\in M_{hd}(B)\) has \(I_h\) on its first block superdiagonal and last row \((-Q_d^{-1}Q_0,\ldots,-Q_d^{-1}Q_{d-1})\).
For any scalar \(\omega\), projection onto the first block is an isomorphism from its affiliated right eigenmodule at \(\omega\) to the kernel of \(Q(\omega)\).
The remaining blocks are \(\omega^i\) times the first, in order, as follows from the shift equations and the last row.
The kernel of \(T^m-I\) is the direct sum of these eigenmodules over the \(m\)-th roots of unity.
Indeed interpolation for \(z^m-1\) gives complementary idempotents on its kernel, even when \(T\) has other spectrum on the ambient module.

If \(T^m=I\), the interpolation operators
\[
                  E_\omega=m^{-1}\sum_{j=0}^{m-1}\omega^{-j}T^j
\]
are matrices over \(B\) on the whole space, and their images are exactly the respective eigenmodules.
For a root with positive nullity some column of \(E_\omega\) is nonzero.
Its first block is a nonzero column \(v\in B^h\) with \(Q(\omega)v=0\).
One coordinate of \(v\) is a nonzero scalar of \(B\), hence an affiliated unit.
The right image \(vU(H)\) consequently has dimension one.
This contradicts the chosen nullity below one.

Thus \(T^m-I\) has a nonzero entry in \(B\).
That entry has regular rank one and is a submatrix, so the whole matrix has rank at least one.
Rank-nullity and the direct sum give the asserted deficit.
For an invertible constant coefficient apply this argument to \(z^dQ(z^{-1})\), which has the same collection of nullities at the roots.

If the maximum rank is \(h\), the [finite-evaluation inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) bounds the sum of deficits at any finite set of complex values by \(dh\).
Apply it at the roots and also at zero.
If the rank at zero is at most \(h-1\), this additional evaluation already accounts for at least one unit of the deficit.
Reversing the polynomial gives the same argument for the leading coefficient.
The maximal rank of the reversal is still \(h\), since the original maximum is attained away from zero and the reversal agrees with it under inversion there.

## A common deficit at the roots of unity

Use the [finite-phase rectangle construction](Yin_C_A0180_v1.md#an-integer-rank-for-a-formal-circle-parameter).
If \(\operatorname{rk}_H K=3/2\), any nonzero integer lift \((a,b)\) of a multiple of the marked character gives an integer maximal rank at least \(3/2\), hence two, for
\[
          B_0+z^bAt-z^a sD-z^{a+b}sCt .
\]
At all \(m\)-th roots the rank stays \(3/2\) by actual unitary twists.
Shift exponents by a scalar monomial to obtain a polynomial of degree at most \(d=|a|+|b|\).
The finite-evaluation inequality always gives \(m/2\le2d\).
When \(a b\ne0\), the lowest and highest exponents in the rectangle each come from a single corner, including when two intermediate exponents coincide.
Take an outer coefficient at one of these exponents, using width \(d\) even if that coefficient vanishes.
If its constant matrix is singular, its regular rank is at most one.
Otherwise it is an invertible constant matrix times a single group element, and its inverse belongs to \(M_2(B)\).
In either case the preceding result gives the stronger necessary inequality
\[
                            m/2\le2d-1.                 \tag{1}
\]
A missing highest coefficient can equivalently be handled by reversing with the full prescribed width \(d\).
At the marking \((1,-7)\) modulo 32, use \(d=8\): the necessary inequality would read \(16\le15\).

## Short marked lifts

The [marked lattice](Yin_C_A0180_v1.md#a-short-pair-of-exponents) of all lifts has index \(m\) in \(\mathbb Z^2\) and contains \(m\mathbb Z^2\).
There is a nonzero lift of width at most \(\lfloor\sqrt{2m}\rfloor\).
Indeed an open diamond of radius \(R/2\) in the \(\ell^1\) norm has area \(R^2/2>m\) when \(R>\sqrt{2m}\).
Translating its pieces into a fundamental parallelogram of area \(m\) gives two distinct points differing by a nonzero lattice vector.
This vector has width less than \(R\), and the widths are integers.

For \(m=29,30,31\) the lift has width at most seven, so \(m/2>2d\).
For \(m=27,28\) its width is at most seven, for \(m=32\) at most eight, and for \(m=23\) at most six.
In these four cases a width strictly below the indicated limit already gives \(m/2>2d\).
At the limit, \(m/2>2d-1\), so it suffices to obtain a lift of that width with two nonzero coordinates.
A shortest nonzero pure-axis width divides \(m\), since \(m\mathbb Z^2\) is in the lattice.
This excludes a pure-axis shortest width of seven for \(m=27\) or six for \(m=23\).
For \(m=28,32\) suppose a shortest vector is on an axis, which after coordinate interchange gives \((d,0)\) with \(d=7,8\), respectively.
The lattice then has a basis \((d,0),(c,4)\): the second-coordinate projection is generated by \(m/d=4\) by the index formula.
Reduce \(c\) modulo \(d\) to have \(|c|\le\lfloor d/2\rfloor\).
If \(c=0\) there is a shorter vector; otherwise the second basis vector has both coordinates nonzero and width at most \(d\).
This proves the assertions through order 32, and [the earlier bound](Yin_C_A0180_v1.md#statement) applies at every larger order.
The rectangle conclusion passes to increments by the four-column reduction.
The estimates stated here leave open contributions from orders below 27 other than 23.

## Assessment history

### Decision a-finite-kernel-column

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:48 |
| status | proved |
| reason | The independent whole-proof inspection verified the result with its stated assumptions and limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One unit of rank deficit and the stated excluded orders. |
| argument | [The companion and a column over the original group ring](#the-companion-and-a-column-over-the-original-group-ring) | Interpolation, finite support and scalar injectivity. |
| argument | [A common deficit at the roots of unity](#a-common-deficit-at-the-roots-of-unity) | Singular end evaluations and reversal. |
| argument | [Short marked lifts](#short-marked-lifts) | The numerical boundary and nonaxial directions. |
| review | [A finite kernel column](../audits/reviews/Yin_R_A0182_v1.md#a-finite-kernel-column) | Independent inspection of the full statement and proof. |

## Current assessment

[Selected decision](#decision-a-finite-kernel-column)
