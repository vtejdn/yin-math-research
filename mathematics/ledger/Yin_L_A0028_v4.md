---
author: Yin
---
# A nonsquare-residue completion with an isotropic Promislow form

This investigation serves [T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [route seven](../strategies/Yin_S_A0007.md).
The development on 2026-11-11 uses the exact rational form and crossed-product equivalence of [L_A0028_v2](../ledger/Yin_L_A0028_v2.md#why-the-quadratic-condition-is-necessary-and-sufficient) and the necessary valuation condition of [L_A0028_v3](../ledger/Yin_L_A0028_v3.md#every-henselian-valued-extension-with-quadratically-closed-residue-loses-anisotropy).
The proposed completion preserves U as a valuation unit with nonsquare residue, but its odd residue form has an explicit isotropic vector and the full form has an explicit formal isotropic lift.
The lift uses a square root absent from the original rational field, so the calculation excludes this completion as an anisotropy certificate without settling rational anisotropy.

## Calibration purpose and exact question

The known Promislow class tests whether a concrete mechanism can independently establish division of the actual crossed product, rather than merely invoke its known group-theoretic division theorem.
An anisotropic extension of the original rational form would imply anisotropy over the original field and would therefore discharge the exact mixed norm and rational rank-divisibility obstruction in L_A0028_v2.
An isotropic extension only rules out that sufficient certificate; it gives no rational solution unless the vector descends.
Even a successful independent Promislow proof would leave T_A0001's arbitrary torsion-free groups, arbitrary finite complex-coefficient matrices, general division-closure mechanism and full review criterion unresolved.
This test accordingly asks only whether the particular extension below is anisotropic and, if not, exactly what prevents its displayed solution from descending.

Let U, V, T be algebraically independent over the complex numbers, and set
\[
 L=\mathbb C(U,V,T),\qquad
 W=\frac{T^2}{UV},\qquad
 d=\frac{4(V-W)}{(1-V)(1-W)},\qquad
 e=\frac{4U}{1-U}.
\]
The nondegenerate diagonal form in question is
\[
 Q=d(H_1^2-UH_2^2)-U(R_1^2-VR_2^2)+e(S_1^2-WS_2^2).
 \tag{1}
\]
All its coefficients and denominators are nonzero rational functions.
No known division theorem for the Promislow group is used below.

## The embedding and its residue forms

Let U and Z be algebraically independent over the complex numbers, put \(k=\mathbb C(U,Z)\), and equip
\[
 E=k((V))
\]
with its V-adic discrete valuation, normalized by \(v(V)=1\).
Its valuation ring is \(k[[V]]\), its residue field is k, and it is complete of residue characteristic zero.
The substitution \(T=ZV\) embeds L into E: already \(\mathbb C(U,V,T)\cong\mathbb C(U,V,Z)\) by \(Z=T/V\), and the latter rational field embeds in its V-adic Laurent-series field.
In particular this is an injective change of rational parameters followed by completion, not the imposition of a relation on three unchanged rational variables.
The residue of U is U in k and is nonsquare, since the U-adic valuation on \(\mathbb C(Z)(U)\) assigns U the odd value one.
Thus the necessary condition from L_A0028_v3 is satisfied.

For compact notation set
\[
 A=U-Z^2,\qquad D=(1-V)(1-Z^2V/U).
\]
Then
\[
 W=\frac{Z^2V}{U},\qquad d=V\delta,
 \qquad \delta=\frac{4A}{UD}.
 \tag{2}
\]
Here U, e, A, D and delta are valuation units, and D has residue one.
Without rescaling any coordinate, (1) is the orthogonal sum
\[
 Q=q_0\perp Vq_1,
 \qquad
 q_0=\langle -U,e\rangle,
 \qquad
 q_1=\left\langle\delta,-U\delta,U,-\frac{4Z^2}{1-U}\right\rangle,
 \tag{3}
\]
where the coordinate orders are \((R_1,S_1)\) and \((H_1,H_2,R_2,S_2)\), respectively.
The last coefficient follows from \(-eW=-4Z^2V/(1-U)\).
Reducing the unit coefficients modulo V therefore gives exactly
\[
 \overline q_0=\left\langle-U,\frac{4U}{1-U}\right\rangle,
 \qquad
 \overline q_1=
 \left\langle\frac{4(U-Z^2)}U,-4(U-Z^2),U,-\frac{4Z^2}{1-U}\right\rangle.
 \tag{4}
\]

The even residue form is anisotropic over k.
Indeed, a nonzero solution of \(-Ur^2+4Us^2/(1-U)=0\) has \(s\ne0\) and would give
\[
 (r/s)^2=\frac4{1-U}.
\]
The right side has valuation minus one at the irreducible divisor \(U=1\) of \(\mathbb C(Z)(U)\), whereas every nonzero square has even valuation.

The odd residue form is isotropic over k.
Its explicit nonzero vector is
\[
 (H_1,H_2,R_2,S_2)=\left(Z,1,\frac{2A}{U},0\right).
 \tag{5}
\]
Substitution gives
\[
 \frac{4A}{U}(Z^2-U)+U\left(\frac{2A}{U}\right)^2
 =-\frac{4A^2}{U}+\frac{4A^2}{U}=0.
\]
The second coordinate is one, so this is not the zero vector.
Consequently the proposed attempt to establish anisotropy of both residue forms fails at an exact algebraic identity.

## An explicit isotropic lift, with no theorem needed for existence

There is a unique power series \(r\in k[[V]]\) with constant term one and \(r^2=D\).
For completeness, write \(D=1+d_1V+d_2V^2\) and \(r=1+\sum_{n\ge1}c_nV^n\).
Coefficient comparison defines
\[
 c_n=\frac12\left(d_n-\sum_{j=1}^{n-1}c_jc_{n-j}\right),
 \qquad d_n=0\quad(n>2).
 \tag{6}
\]
This recursion is valid because k has characteristic zero and proves the asserted identity coefficient by coefficient.
The unit r is invertible in \(k[[V]]\).

Set
\[
 (H_1,H_2,R_1,R_2,S_1,S_2)
 =\left(Z,1,0,\frac{2A}{Ur},0,0\right)\in E^6.
 \tag{7}
\]
Using (2), direct substitution into (1) yields
\[
 Q=\frac{4VA}{UD}(Z^2-U)
      +UV\frac{4A^2}{U^2r^2}
   =-\frac{4VA^2}{UD}+\frac{4VA^2}{UD}=0.
 \tag{8}
\]
This is an exact formal-series identity, not a finite-jet or numerical calculation.
The coordinate H_2 is one, so Q is isotropic over E.
It follows that preserving U as a unit with nonsquare residue is insufficient for an anisotropic valued-extension certificate.

The same identity gives a useful slightly broader boundary.
For any field extension M of L containing a nonzero element r with
\[
 r^2=(1-V)(1-W),
\]
the vector
\[
 (H_1,H_2,R_1,R_2,S_1,S_2)
 =\left(\frac TV,1,0,\frac{2(V-W)}{Vr},0,0\right)
 \tag{9}
\]
is isotropic over M.
Indeed \(T^2/V^2-U=-U(V-W)/V\), and the two nonzero contributions to Q are \(-4U(V-W)^2/[V(1-V)(1-W)]\) and its negative.
In particular, a henselian valued extension with residue characteristic different from two and with \(v(V)>0\) and \(v(W)>0\) has such an r: the residue polynomial of \(X^2-(1-V)(1-W)\) has the simple root one.
This last use is exactly the simple-root lifting property specified in L_A0028_v3; no assertion about its converse is made.

## Why the formal vector does not descend

In the original rational field L, use the discrete valuation at the irreducible polynomial \(V-1\) in \(\mathbb C(U,T)(V)\).
One has
\[
 (1-V)(1-W)=\frac{(1-V)(UV-T^2)}{UV}.
 \tag{10}
\]
At V = 1, the factors UV and \(UV-T^2\) are units, since U and \(U-T^2\) are nonzero in \(\mathbb C(U,T)\).
Thus (10) has valuation one and is not a square in L.
The element r in (7) therefore does not belong to the embedded copy of L.
Since A and U are nonzero elements of that copy, the coordinate \(2A/(Ur)\) cannot belong to it either.
Moreover, every projective rescaling of (7) defined over L would, after normalizing its nonzero H_2 coordinate to one, reproduce (7), so the displayed isotropic line does not descend either.
This only concerns the constructed vector and line; it neither excludes another rational isotropic vector nor proves one exists.

## Source attribution and inspection boundary

The local search reused L_A0028_v2/v3 and found no retained source inspection of Springer's residue criterion among the relevant ledger, source-audit and bibliographic matches.
The checked external comparison is Kne09, Manfred Knebusch, *Specialization of Quadratic and Symmetric Bilinear Forms*, translated by Thomas Unger, preliminary version dated 22 November 2009, [Section 1, printed p. 4, PDF p. 16](https://www.math.uni-bielefeld.de/lag/man/372.pdf#page=16).
Its theorem attributed to Springer 1955 assumes a complete discretely valued field with residue characteristic different from two and a nondegenerate symmetric bilinear form decomposed into unit and uniformizer-times-unit parts.
It states that anisotropy forces both residue forms to be anisotropic, and gives the converse construction from anisotropic residue forms.
Our field E, uniformizer V, residue field k and diagonal form satisfy the displayed hypotheses.
The isotropic odd residue in (5) therefore agrees with the source's obstruction to anisotropy.
Here that theorem is attribution and comparison, not an existence premise for (7), whose formal recursion and substitution give the complete direct proof.
The title page, contents and the stated Section 1 passage were inspected through the public university-hosted PDF; the original Springer proof and the rest of the monograph were not audited.
The publicly available university-hosted original was acquired on 2026-11-12 (Asia/Hong_Kong) as [Kne09--preliminary.pdf](../literature/pdf/Kne09--preliminary.pdf), with 244 pages and the matching title-page author, translator and preliminary-version date.
The canonical bibliography records this inspected preliminary edition; no publisher edition or general redistribution licence was inferred from public access.

## Remaining route question

The test supplies a second explicit way completion can destroy the rational obstruction, now while the residue of U remains nonsquare.
It cannot prove the mixed norm exclusion, division of the actual crossed product, or fourfold rank divisibility over the original field.
A future anisotropy certificate must avoid both the earlier square-root mechanisms in L_A0028_v3 and the square root of \((1-V)(1-W)\) displayed here, or use a genuinely global rational argument.
The unresolved original problem remains the anisotropy of (1) over L, equivalently the full mixed norm obstruction of L_A0028_v2.
No new group class and no completion of T_A0001 is claimed.
