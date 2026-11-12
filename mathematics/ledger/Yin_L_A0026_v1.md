---
author: Yin
---
# Zero stabilization does not normalize the specified two-variable witness

Date: 2026-11-12 (Asia/Hong_Kong).
The [two-variable example](../claims/Yin_C_A0007_v3.md#why-the-same-polynomial-repair-fails-for-a-two-variable-edge) excludes a same-size scalar polynomial normalization of a specified finite witness.
This investigation asks whether adjoining finitely many identity witness coordinates removes that particular obstruction.
The answer is negative for every such stabilization, even with a full matrix polynomial left factor.
The conclusion remains about this specified witness and factorization, not every possible witness for a kernel or every analytic repair.

## Setting and exact claim

Let
\[
R=\mathbb C[x^{\pm1},y^{\pm1}],\qquad
H=\mathbb Z^2,\qquad G=H\times\langle s\rangle,
\]
and use the canonical coefficient expectation \(E_H\), amplified entrywise.
Put
\[
W=(x-1)+(y-1)s.
\]
For any integer \(\ell\ge0\), set \(k=\ell+1\) and
\[
W_\ell=\operatorname{diag}(W,I_\ell)\in M_k(\mathbb CG).
\tag{1}
\]
Its expected Gram is
\[
C_\ell=E_H(W_\ell W_\ell^*)
=\operatorname{diag}(|x-1|^2+|y-1|^2,I_\ell).
\tag{2}
\]
It has full support in \(M_k(\mathcal N(H))\), but no bounded inverse.
There do not exist
\[
D\in M_k(R),\quad \det D\ne0,\quad
W_0\in M_k(\mathbb CG),\quad\varepsilon>0
\]
such that
\[
W_\ell=DW_0,\qquad E_H(W_0W_0^*)\ge\varepsilon I_k.
\tag{3}
\]
Every candidate \(D\) is already independently invertible in the actual affiliated algebra by its nonzero Laurent determinant.
The obstruction concerns the stronger finite polynomial factorization and uniform expected-Gram conclusion in (3).

## The coefficient module forced by the witness

Write \(q_1=x-1\), \(q_2=y-1\), and \(I=(q_1,q_2)\subset R\).
The only two \(s\)-coset coefficient matrices in (1) are
\[
F_0=\operatorname{diag}(q_1,I_\ell),\qquad
F_1=\operatorname{diag}(q_2,0_\ell).
\tag{4}
\]
Their concatenation \(F=[F_0\ F_1]\) has column module
\[
\mathcal C:=F R^{2k}=I\oplus R^\ell\subset R^k.
\tag{5}
\]
No normality ambiguity occurs here, since the selected test group is the direct product.
The same coefficient-module obstruction is algebraic and does not depend on a claimed Atiyah failure for this abelian group.

Assume (3).
Since \(D\) has nonzero determinant over the domain \(R\), it acts injectively on every polynomial coefficient column.
The finite expansion of \(W_0\) can therefore have no \(s\)-coset outside \(0,1\): comparing any such coefficient in \(DW_0=W_\ell\) gives \(D F_j'=0\) and hence \(F_j'=0\).
Write
\[
W_0=F_0'+F_1's,\qquad
F'=[F_0'\ F_1']\in M_{k,2k}(R).
\]
Then
\[
F=DF',\qquad E_H(W_0W_0^*)=F'F'^*.
\tag{6}
\]

The matrix symbol \(F'F'^*\) is continuous on the two-torus.
An almost-everywhere lower bound by \(\varepsilon I_k\) therefore holds at every torus point, since failure at a point would persist in a positive-measure neighborhood.
In particular \(F'(1,1)\) has complex row rank \(k\).
Thus a \(k\)-column minor has determinant nonzero at \((1,1)\).

## The local dimension contradiction

Let \(\mathfrak m=(x-1,y-1)\), and let \(S=R_{\mathfrak m}\), the localization at Laurent polynomials not vanishing at \((1,1)\).
Its residue field is \(\mathbb C\).
The chosen minor of \(F'\) is invertible over \(S\), so its columns generate all of \(S^k\).
Localizing (6) therefore gives
\[
\mathcal C_S=D S^k.
\tag{7}
\]
Because \(\det D\ne0\), the map \(S^k\to DS^k\) is injective as well as surjective onto its image.
Thus (7) would make \(\mathcal C_S\) a free \(S\)-module of rank \(k=\ell+1\).
This conclusion does not require \(D(1,1)\) to be invertible.

On the other hand, (5) gives
\[
\mathcal C_S=\mathfrak m S\oplus S^\ell.
\]
Its residue-space dimension is
\[
\dim_{\mathbb C}
\left(\mathcal C_S/\mathfrak m S\,\mathcal C_S\right)
=\dim_{\mathbb C}\left(\mathfrak m S/(\mathfrak m S)^2\right)+\ell
=2+\ell.
\tag{8}
\]
For the last equality, \(x-1,y-1\) generate the maximal ideal, and their classes are independent modulo its square.
Their independence is seen by the two partial derivatives at \((1,1)\): every product of two functions vanishing there has both first derivatives zero, while the derivatives of these two generators are \((1,0)\) and \((0,1)\).
Derivatives are valid on the localized rational functions because the denominators do not vanish at the point.
Thus no theorem about projective modules or cancellation is needed for this dimension computation.

A free \(S\)-module of rank \(\ell+1\) instead has residue-space dimension \(\ell+1\).
This contradicts (8), and proves the impossibility of (3) for every finite \(\ell\).

The full-support assertion in (2) uses the actual regular torus representation: its first diagonal entry vanishes only at \((1,1)\), which has Haar measure zero.
Its lack of a positive lower bound follows by continuity near that point.
Generic rank uses the fraction field of the specified commutative domain, while the local obstruction uses the local ring \(S\) and its residue field \(\mathbb C\); none is identified with an unknown group-matrix rank.

## What this rules out and what it leaves open

The original scalar obstruction survives adjoining any finite number of identity witness blocks and allowing a matrix polynomial left factor of the resulting size.
The failure is local: a uniformly positive expected Gram would make the localized coefficient module free, but that module has one more residue generator than its generic rank.
It also rules out a polynomial right-inverse normalization for this stabilized witness, since such a right inverse would give the same full-rank evaluation and local contradiction.

The calculation does not rule out changing the selected kernel witness, adding different kernel columns, a different stabilization, rational or analytic factors, or a transformation that changes the coefficient module.
For instance, if \(Y=0\) is chosen so that (1) is a kernel witness, the alternative identity witness already has a uniformly positive expected Gram.
No impossibility for the kernel of that \(Y\) follows.
The example is abelian and has established integer group-matrix ranks; it is a failure of the proposed finite normalization procedure.

This complements the [cyclic-edge stable-shear obstruction](../ledger/Yin_L_A0023_v1.md), which concerns deficient expected support rather than the full-support, nonuniform case here.
Neither obstruction supplies a universal failure of support surgery.
The useful continuation requires a transformation with a genuinely different finite coefficient module and an independently justified correction to the original analytic kernel dimension.
