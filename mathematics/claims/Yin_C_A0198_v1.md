---
author: Yin
---

# The order of a finite abelian quotient in the four-site rank test

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free, and assume that every nonzero element of \(\mathbb CH\) acts injectively in its regular representation.
Suppose \(Q\) is a finite abelian quotient of \(H\), of order \(N\) and exponent \(m\).
Take a four-site matrix \(K=B+At-s(D+Ct)\), where its four coefficient matrices are complex two-by-two matrices.
The regular rank uses the unnormalized matrix trace.
If \(N>32\), or if \(29\le N\le31\), then \(\operatorname{rk}_H K\ne3/2\).
In particular the [four-column equivalence](Yin_C_A0184_v1.md#statement) excludes a half-dimensional constant-column increment for the list containing each of the two labels twice.
Here one may use the order of an abelian quotient even when none of its cyclic quotients has order \(33\).

At \(N=28\) and \(N=32\) there is always a character lift of weights \(a,b\) (as defined below) for which either \(4(|a|+|b|)<m\), or \(4(|a|+|b|)=m\) and \(ab\ne0\).
The second possibility locates the borderline at two nonzero weights, so both extreme exponents select single coefficient sites.
Whether the two extreme coefficients are invertible is a separate question.

## The lattice of all finite characters

Fix \(\zeta=\exp(2\pi i/m)\).
For each character of \(Q\) evaluate it on the two marked images as \((\zeta^a,\zeta^b)\).
All resulting exponent pairs form a subgroup of \((\mathbb Z/m)^2\) of order \(N\), since characters distinguish points of a finite abelian group and the marked elements generate \(Q\).
Let \(\Lambda\) be the inverse image of this subgroup in \(\mathbb Z^2\).
It has index \(m^2/N\).

For every nonzero pair in \(\Lambda\) the [finite-phase inequality](Yin_C_A0180_v1.md#an-integer-rank-for-a-formal-circle-parameter) supplies an integer \(R\in\{0,1,2\}\) with
\[
              0\le R-\operatorname{rk}_H K\le R(|a|+|b|)/m .
\]
Indeed the one-parameter lift has group-ring scalar injectivity and an integer-character rank as in that argument.
At the \(m\) distinct parameter values \(\zeta^j\) the ranks all agree with that at \(1\), using the \(j\)-th powers of the chosen character.
This works when some twists as representations coincide: the polynomial estimate counts distinct parameter values.
The Laurent degree after a scalar shift is at most \(|a|+|b|\).
For a putative rank \(3/2\), \(R\) must equal two, so one such pair with \(4(|a|+|b|)<m\) suffices.

Let \(\lambda\) be the least nonzero \(\ell^1\)-length in \(\Lambda\).
The translates by \(\Lambda\) of the open diamond of radius \(\lambda/2\) have disjoint interiors.
Its area is \(\lambda^2/2\), so comparison on a fundamental domain gives
\[
                        \lambda\le m\sqrt{2/N}.
\]
For \(N>32\) this is strictly less than \(m/4\).
At orders \(29,30,31\) the group is cyclic since these orders are square-free, hence \(m=N\).
In each case the integer \(\lambda\le\lfloor\sqrt{2N}\rfloor=7\) also gives strict inequality.

## The two boundary orders

If \(N=32\) and the strict inequality fails, put \(L=m/4\).
Then \(\lambda=L\).
The linear change \((u,v)=(a+b,a-b)\) converts \(\ell^1\) to \(\ell^\infty\) and multiplies covolume by two.
The transformed lattice has shortest sup distance \(L\) and covolume \(L^2\).
Its translates of the closed axis-aligned square of side \(L\) tile the plane: their interiors do not overlap, the fundamental domain has the same area as one square, and a locally finite union of closed squares misses an open set if it misses any point.

Consider the square \([0,L]^2\) and its right edge.
The neighboring squares covering this edge from the right across intervals of positive length all have left edge \(u=L\); otherwise they would overlap the square or leave a gap.
The finitely many exceptional vertices do not affect coverage of the whole open edge by the closures of these intervals.
A single neighbor along the whole edge gives the lattice vector \((L,0)\).
If there is more than one such neighbor, two meet at an interior height, are disjoint in their interiors and have the same left edge and side length.
Their translation vectors differ by \((0,L)\).
Returning to \((a,b)\) gives a lattice vector \((L/2,L/2)\) or \((L/2,-L/2)\).
Both weights are nonzero, and their length is \(m/4\).

For \(N=28\), the two possible exponents are \(14\) and \(28\).
If \(m=14\) the bound \(\lambda\le\sqrt{14}\) gives \(\lambda\le3\).
If \(m=28\), it gives \(\lambda\le7\).
Only \(\lambda=7\) needs consideration.
When an axial shortest vector occurs, interchange coordinates and signs to put \((7,0)\in\Lambda\).
The horizontal sublattice then has period seven.
Since the lattice has covolume 28, its projection to the vertical axis has period four.
Choose \((a,4)\) and adjust by \((7,0)\) so \(|a|\le3\).
This gives the desired nonaxial vector of length at most seven, since \(a=0\) would contradict \(\lambda=7\).
If no axial shortest vector occurs, any shortest vector works.

## Testing simultaneous interpolation in two parameters

There is also a direct simultaneous interpolation test on all \(N\) character points.
Write \(\bar s,\bar t\) for the marked images in \(Q\) and \(\phi(i,j)=\bar s^i\bar t^j\).
For a finite nonempty \(W\subset\mathbb Z^2\) suppose \(\phi\) is injective on \(W+\{0,1\}^2\).
If \(\operatorname{rk}_H K>1\), then
\[
                         2|W|\le N\operatorname{rk}_H K .
\]

Indeed form vector Laurent polynomials with coefficient vectors in \(\ell^2(H)^2\) and frequency support \(W\), and multiply by the two-parameter rectangle \(B+y At-x s(D+y Ct)\).
Evaluate each output at all character points.
If these evaluations vanish, orthogonality of the finite-group characters and the support condition recover every product coefficient as zero.
Choose an integer \(T\) for which \((i,j)\mapsto i+Tj\) is injective on \(W\).
Substitution \((x,y)=(z,z^T)\) gives a one-variable product which vanishes identically.
The corresponding one-parameter lift has integer generic rank by the same integer-character argument; its supremum is at least the rank at \((1,1)\), so its generic rank is two.
At almost every unit phase its kernel is consequently zero, so the specialized input polynomial also vanishes almost everywhere.
Uniqueness of its Fourier coefficients, using the distinct specialized frequencies, makes the original input zero.
The resulting injective equivariant map from \(2|W|\) coordinates lands in the direct sum of the \(N\) closed images of the evaluations, each having rank \(\operatorname{rk}_H K\).
This proves the test.

This particular test would need \(|W|>3N/4\) to rule out \(3/2\).
Let \(u,v\) be the numbers of occupied horizontal rows and vertical columns of \(W\).
Adding \(\{(0,0),(1,0)\}\) gains at least \(u\) sites, and the new set occupies at least \(v+1\) vertical columns.
Adding the vertical two-point set gains at least \(v+1\) more sites.
As \(uv\ge|W|\), injectivity of \(\phi\) gives \(N\ge|W+\{0,1\}^2|\ge(\sqrt{|W|}+1)^2\).
For \(N\le55\) this prevents \(|W|>3N/4\).
This limitation concerns two-parameter interpolation recovering all four-site product coefficients by distinct residues; further relations among those coefficients are outside the counting argument.

## A quotient of order 48 and exponent 12

Take \(H=\langle p,q\mid p q^6p^{-1}=q^{-6},\ q p^2q^{-1}=p^{-2}\rangle\) with labels \(s=q,\ t=pq\).
As in the [Klein bottle amalgam construction](Yin_C_A0180_v1.md#two-labels-with-isolated-phases-of-order-at-most-four), use the vertices on \((p,y)\) and \((q,v)\) with conjugations inverting \(y,v\) respectively, and identify \(p^2=v,\ y=q^6\).
The subgroups generated by \((p^2,y)\) and \((v,q^6)\) are free abelian of rank two by the semidirect product coordinates, so the amalgam embeds both torsion-free vertices and is torsion-free by normal form.
Its abelianization is \(C_4[p]\oplus C_{12}[q]\); the marked labels generate \(H\).
Killing either marked image in the abelianization leaves a cyclic group of order four, and every cyclic quotient has order at most twelve.
The quotient killing \(p\) gives the simultaneous weights \((1,1)\) modulo twelve, of length two.
Thus the rank exclusion follows under the stated scalar injectivity hypothesis, already from \(4\cdot2<12\); the order bound additionally applies uniformly to every generating marking of the abelian quotient.

## Assessment history

### Decision the-full-finite-abelian-quotient

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:48 |
| status | proved |
| reason | The independent whole-proof inspection verified the result with its stated assumptions and limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Quotient cardinality and the precise borderline alternatives. |
| argument | [The lattice of all finite characters](#the-lattice-of-all-finite-characters) | Covolume and the diamond count. |
| argument | [The two boundary orders](#the-two-boundary-orders) | Square tiling, nonaxial lifts and the two possible exponents at 28. |
| argument | [Testing simultaneous interpolation in two parameters](#testing-simultaneous-interpolation-in-two-parameters) | Support injectivity, quotient Fourier sampling and the size restriction. |
| argument | [A quotient of order 48 and exponent 12](#a-quotient-of-order-48-and-exponent-12) | Amalgam construction and actual marked quotient. |
| review | [The full finite abelian quotient](../audits/reviews/Yin_R_A0182_v1.md#the-full-finite-abelian-quotient) | Independent inspection of the full statement and proof. |

## Current assessment

[Selected decision](#decision-the-full-finite-abelian-quotient)
