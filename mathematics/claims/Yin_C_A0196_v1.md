---
author: Yin
---

# Galois conjugacy of two saturated lifts to a cyclic quotient of order 32

## Statement

Let \(G=\langle s,t\rangle\) be torsion-free with a surjection \(\pi:G\to C_{32}\), and assume every nonzero scalar of the complex group ring acts injectively in the regular representation.
For arbitrary two-by-two complex matrices \(A,B,C,D\), the regular rank of
\[
                         K=B+At-s(D+Ct)
\]
cannot be \(3/2\).
Consequently the [prescribed four-column family](Yin_C_A0184_v1.md#statement) with two copies of each label admits no half-dimensional constant-column increment.
The [bound for orders at least 33](Yin_C_A0180_v1.md#a-short-pair-of-exponents) thus extends to order 32.
The statement allows arbitrary complex coefficients even when they have no prescribed number field of definition.

## Saturation, companion matrices and augmentation

First take \(\pi(s)=1,\ \pi(t)=-7\) in additive notation modulo \(32\), and suppose the regular rank is \(3/2\).
Use each exponent pair
\[
                     (a,b)=(1,-7),\quad (5,-3),\quad (4,4).
\]
Their residues are \(1,5,4\) times the marked pair; for each, \(d=|a|+|b|=8\).
Remove negative exponents from \(K(z)=B+z^b At-z^a s(D+z^b Ct)\) by multiplying by \(z^{-\min(0,a,b,a+b)}\), obtaining a bounded group-ring matrix polynomial \(L(z)\) of degree at most eight.
All 32 distinct roots of unity have rank \(3/2\), and the generic rank is the integer \(R=2\) by the [integer lift and rank-deficit bound](Yin_C_A0180_v1.md#an-integer-rank-for-a-formal-circle-parameter).
The 32 deficits already sum to 16.
The [finite evaluation inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) bounds the sum of the deficits at any finite set by \(8R=16\).
Adding zero to the set therefore forces \(L(0)\) to have rank two.
The same argument for \(z^8L(1/z)\) gives rank two at the top coefficient.
For \((1,-7)\) the two extreme terms consist of single translations with weights \(A,-D\); for \((4,4)\) their weights are \(B,-C\).
Thus all four constant matrices are invertible and in all three lifts the leading coefficient is invertible over the group ring.
In particular \(\det B\ne0\).

For each of the first two lifts, normalize \(L\) to be monic by multiplying on the left by its leading coefficient inverse.
Use the ordinary companion matrix \(T\) over \(\mathbb CG\), with identity superdiagonal blocks and last row the negatives of the polynomial's monic coefficients in ascending powers.
At any scalar \(\lambda\), projection to the first coordinate identifies \(\ker(T-\lambda I)\) over the affiliated algebra with \(\ker L(\lambda)\); a vector in the latter lifts to \((v,\lambda v,\ldots,\lambda^7v)\).
The 32 kernel dimensions at the roots of unity sum to \(32/2=16\), the whole domain dimension.
They are in algebraic direct sum by scalar polynomial interpolation in \(T\).
Their combined image is the range of a finite matrix of affiliated kernel projections, so it equals its support module, which has full dimension.
It follows that \(T^{32}=I_{16}\) in the affiliated algebra and hence in the faithfully represented matrix group ring.
The augmentation sends \(T\) to an ordinary complex matrix satisfying the same identity.
This complex companion is diagonalizable with eigenvalues among the 32nd roots, since \(z^{32}-1\) has simple roots.
Here both the companion construction and its augmentation use only genuine group-ring entries.

## The two primitive directions

Let \(\zeta=\exp(2\pi i/32)\) and put
\[
 F(X,Y)=\det\bigl(B+YA-X(D+YC)\bigr),\quad
 r_j=\dim_{\mathbb C}\ker\bigl(B+\zeta^{-7j}A-\zeta^j(D+\zeta^{-7j}C)\bigr)
 \qquad(j\bmod 32).
\]
The bidegree of \(F\) is at most \((2,2)\).
For the first two lifts the respective monic characteristic polynomials of the augmented companions are the monic normalizations of
\[
                z^{14}F(z,z^{-7}),\qquad z^6F(z^5,z^{-3}).
\]
Indeed the determinant of \(zI-T\) for a monic complex block companion is the determinant of the monic matrix polynomial: elimination of the superdiagonal identity blocks proves the identity, with leading coefficient one.
The monomial used on the two-by-two polynomial multiplies its determinant by the square of that monomial.
At the root \(\zeta^j\) the two algebraic multiplicities equal \(r_j,r_{5j}\), respectively, by the kernel identity and diagonalizability.
The multiplication of indices by five uses \(-7\cdot5\equiv-3\bmod32\).

The first monic polynomial therefore has coefficients in \(\mathbb Q(\zeta)\), because it is \(\prod_{j=0}^{31}(z-\zeta^j)^{r_j}\).
The second equals its Galois conjugate by \(\zeta\mapsto\zeta^{5^{-1}\bmod32}\).
In particular their sets of nonzero powers agree.
This applies to the monic characteristic polynomials even for transcendental original coefficients; no field automorphism of the input coefficients is used.

Before cancellation, the possible powers in the first polynomial are
\[
                 \{0,1,2,7,8,9,14,15,16\};
\]
in the second they are
\[
                 \{0,3,5,6,8,10,11,13,16\}.
\]
The first polynomial's coefficient at power 14 is a nonzero multiple of \(\det B\): among \(0\le i,j\le2\), \(14+i-7j=14\) requires \(i=j=0\).
The second has no term at power 14.
This contradicts Galois conjugacy and excludes regular rank \(3/2\).

## All surjections onto the quotient

Multiplication of both marked residues by any unit modulo 32 amounts to a change of quotient generator.
At least one residue is odd.
If needed interchange the roles of the labels: taking the adjoint of the original rectangle gives another rectangle on \((t^{-1},s^{-1})\), with constant matrices changed, and preserves square regular rank.
Either label can also be inverted individually, since right multiplication by \(t^{-1}\) or left multiplication by \(-s^{-1}\) exchanges corresponding constant coefficients and gives the same kind of rectangle.
Thus it suffices to test \((1,r)\) for \(0\le r\le16\).

For \(0\le r\le6\), the lift \((1,r)\) has \(4d<32\).
For \(r=8,10,11,12,13,14,15,16\), suitable lifts in that order are
\[
          (4,0),(3,-2),(3,1),(3,4),(5,1),(2,-4),(2,-2),(2,0).
\]
Each is congruent to a multiple of \((1,r)\) and has \(d<8\).
In each case the integer \(R\) of the finite evaluation bound would have to be two if the given rank were \(3/2\), contradicting \(2d/32<1/2\).
The remaining residues are \(7,9\).
Inversion changes \(7\) to \(-7\).
Interchanging the labels at \(9\) and renormalizing gives \(9^{-1}=25\equiv-7\pmod{32}\).
The primitive-direction contradiction therefore covers every remaining marking, and the four-column equivalence gives the claimed consequence.

## Assessment history

### Decision galois-comparison-at-order-32

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:48 |
| status | proved |
| reason | The independent whole-proof inspection verified the result with its stated assumptions and limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every marking of the cyclic quotient of order 32. |
| argument | [Saturation, companion matrices and augmentation](#saturation-companion-matrices-and-augmentation) | Both extreme coefficients, semisimple companions and complex augmentation. |
| argument | [The two primitive directions](#the-two-primitive-directions) | Character permutation, Galois conjugacy and the missing exponent. |
| argument | [All surjections onto the quotient](#all-surjections-onto-the-quotient) | Reductions by inversion and exchange and the short lifts. |
| review | [Galois comparison at order 32](../audits/reviews/Yin_R_A0182_v1.md#galois-comparison-at-order-32) | Independent inspection of the full statement and proof. |

## Current assessment

[Selected decision](#decision-galois-comparison-at-order-32)
