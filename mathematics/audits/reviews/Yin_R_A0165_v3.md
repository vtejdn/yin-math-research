---
author: Yin
---

# Finite-rank commutation on a subspace and division-closure membership

## Finite-rank commutation on a subspace

At 2026-11-25T07:30 I checked both implications of the [finite-rank criterion](../../claims/Yin_C_A0131_v3.md#statement) against the [A0003 objective](../../tasks/Yin_T_A0003_v2.md#contract).
This is a self-review of the argument I developed.
The quantifiers require one fraction pair, its finite-rank solutions and one finite-dimensional subspace, followed by a test over all finite-rank operators on \(H\).

In the forward direction, the affine row equation involves just the vectors \(\eta_i\) and their first right translates.
It is legitimate to apply \(B\) component by component using commutation on \(V\), even if some translates lie outside \(V\).
Afterwards the row \(B(\eta)\) has entries in \(L^2\), so one may multiply the resulting zero equation on the right inside the affiliated ring by \(L^{-1}\). [Construction of the row and the finite-rank witnesses](../../claims/Yin_C_A0131_v2.md#constructing-the-finite-rank-operators)

For the converse, the basis of relations includes linear dependencies involving both the original vectors and all their chosen first translates.
This gives exactly the consistency needed for a map on their finite-dimensional span \(E\).
Extending this map by zero on \(E^\perp\) is bounded and finite rank, regardless of the supports of the vectors \(z_i\).
The first column of \(K\) enforces \(z_1=0\), and \(K^*z^*=(zK)^*\) takes the row kernel to the Hilbert space kernel used in Gram elimination.
For every leading compression \(S_k\) of \(S=KK^*\), a vector in its kernel padded with zeros has zero quadratic form for \(S\).
It is therefore zero by injectivity of \(S\).
Each \(S_k\) then has an affiliated inverse and scalar Schur complements produce entries in \(D_G\), including when these inverses are unbounded.
The matrix \(K^*(KK^*)^{-1}\) is a right inverse, in the order required to solve \(vK=(s,0,\ldots,0)\).
The remaining evaluation at \(t^*\delta_e\) has nonzero coefficient \(-\tau(tt^*)\) on the desired numerator. [Column Gram blocks and scalar inversion](../../claims/Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)

For \(G=\mathbb Z\) with generator \(X\) and \(u=(1-X)^{-1}\), choose \(s=t=1-X\), \(a=b=1\), \(T_1=-P_e\) and \(V=\operatorname{span}\{1,X\}\).
A map in (2) satisfies \(B(1)=B(X)=B(1)X\).
The bilateral shift has no nonzero fixed vector in \(\ell^2(\mathbb Z)\), so both values vanish.
For the group of order two, the nonunit projection \(u=(1+X)/2\) works with \(s=t=1\), \(a=b=u\), \(T_1=-P_e/2\) and \(V=H\).
Commutation with the right shift propagates vanishing on \(1\) to \(X\).
These checks exercise an unbounded rational element and a group algebra with zero divisors.

The statement and argument establish a criterion of the specified type over all finitely generated groups.
The local commutation test is an additional condition on the finite-rank witnesses for (1).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finite-rank commutation on a subspace](#finite-rank-commutation-on-a-subspace) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finite-rank commutation on a subspace](#finite-rank-commutation-on-a-subspace) | [Statement](../../claims/Yin_C_A0131_v3.md#statement) | Both directions for arbitrary affiliated elements, the common choice of fraction pair and subspace, and quantification over finite-rank test operators. |
| [Finite-rank commutation on a subspace](#finite-rank-commutation-on-a-subspace) | [Argument](../../claims/Yin_C_A0131_v3.md#argument) | The affine row implication, extension from all translation relations, scalar Gram elimination and recovery of the numerator. |
| [Finite-rank commutation on a subspace](#finite-rank-commutation-on-a-subspace) | [A0003 contract](../../tasks/Yin_T_A0003_v2.md#contract) | Coverage of every finitely generated torsion-free group by the finite-rank test for the full class of finitely generated groups. |
