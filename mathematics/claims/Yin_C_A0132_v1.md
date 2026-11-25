---
author: Yin
---

# Rational kernel projections from a maximal-rank torus fiber

## Statement

Let \(H\) be a countable discrete group, \(d\geq1\), and \(G=H\times\mathbb Z^d\).
Write \(U_J=L^0(\mathcal N(J))\) and \(D_J=\operatorname{Div}_{U_J}(\mathbb CJ)\).
Under Fourier transformation in \(\mathbb Z^d\), a rectangular matrix \(A\in M_{m,n}(\mathbb CG)\) gives a Laurent polynomial \(A(z)\) over \(\mathbb CH\) on \(\mathbb T^d\).
Use unnormalized matrix traces for all ranks.
Let \(\rho=\max_z\operatorname{rk}_H A(z)\).
The following conditions are equivalent.

1. \(p_{\ker A}\in M_n(D_G)\).
2. There exists a point \(w\) of rank \(\rho\) such that \(p_{\ker A(w)}\in M_n(D_H)\).
3. For Haar-almost every \(w\), the fiber has rank \(\rho\) and \(p_{\ker A(w)}\in M_n(D_H)\).

Consequently \(D_G\) is von Neumann regular if and only if \(D_H\) is von Neumann regular.
For finitely generated \(H\), this is precisely invariance of the sufficiency of [the unrestricted finite-rank equation](Yin_C_A0131_v1.md#which-rationality-is-detected) under taking a direct product with \(\mathbb Z^d\).
The regularity equivalence also holds with any finitely generated virtually abelian direct factor in place of \(\mathbb Z^d\).
All assertions allow zero divisors in the division closures.

## Argument

The [generic rank theorem](Yin_C_A0012_v2.md#exact-generic-rank-for-rectangular-laurent-matrices) gives the existence of the maximum, its almost-everywhere attainment and \(\operatorname{rk}_G A=\rho\).
Fourier transformation identifies the group von Neumann algebra with \(\mathcal N(H)\overline\otimes L^\infty(\mathbb T^d)\) with its product trace.
Finite affiliated sums, products and adjoints are fiberwise, and a square affiliated matrix is a unit exactly when its fiber is a unit almost everywhere.
For the latter assertion use the measurable kernel and cokernel projections and the faithful integrated trace, and obtain the fiberwise inverse by polar decomposition.
In particular a fixed finite rational expression over \(\mathbb CG\) that is defined in \(U_G\) is simultaneously defined over \(U_H\) at almost every \(z\), where it takes values in \(D_H\).
This assertion specializes the expression on a conull set common to its finitely many inverse operations.
The kernel projection of the bounded matrix \(A\) has fibers \(p_{\ker A(z)}\), by bounded spectral calculus.
These facts give \(1\Rightarrow3\Rightarrow2\) and also \(D_G\cap U_H=D_H\) for the constant copy of \(U_H\).

Fix a point \(w\) where \(p_0=p_{\ker A(w)}\) has entries in \(D_H\), and put \(r=\operatorname{rk}_H A(w)\).
The projection \(f\) onto the closure of the image of \(A(w)\) has the formula
\[
 f=A(w)\big(A(w)^*A(w)+p_0\big)^{-1}A(w)^* .
\]
The denominator is an affiliated unit, and the formula follows on the kernel and its orthogonal complement by polar decomposition.
Inverses of square matrices over \(D_H\) that are units over \(U_H\) have entries in \(D_H\).
Indeed, [scalar Gram elimination](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) applies also to matrices with affiliated entries: the first \(j\) columns of a unit have zero affiliated kernel, their Gram matrices are units, and each successive Schur complement is a scalar affiliated unit in the division closure.
Thus \(f\) is a bounded projection in \(M_m(D_H)\).

Regard \(f\) as constant and form the bounded Laurent matrices
\[
 C(z)=fA(z),\qquad K(z)=1-f+C(z)C(z)^*.
\]
The matrix \(K(w)\) has zero kernel since \(C(w)=A(w)\) has closed image span \(f\).
Applying the generic rank theorem to \(K\) shows that \(K\) is a unit in \(M_m(U_G)\).
Its inverse has entries in \(D_G\) by scalar Gram elimination.
The initial support of \(C\) and the resulting projection are
\[
 q=C^*K^{-1}C,\qquad P=1-q\in M_n(D_G).
\]
Indeed \(K\) commutes with \(f\), and \(CC^*\) is a unit on the corner \(f\) because \(K\) is a unit and agrees with \(CC^*\) there.
Polar decomposition gives \(P=p_{\ker C}\) and \(\operatorname{rk}_G C=(\operatorname{Tr}_m\otimes\tau_H)(f)=r\).
The inclusion \(\ker A\subseteq\ker C\) now gives the exact error
\[
 P\geq p_{\ker A},\qquad
 (\operatorname{Tr}_n\otimes\tau_G)(P-p_{\ker A})=\rho-r .
\]
At a maximal-rank point, faithfulness of the trace gives \(P=p_{\ker A}\), proving \(2\Rightarrow1\).

### Consequences for the unrestricted equation

If \(D_H\) is regular, its matrix rings are regular, and the inherited positive definite involution puts the ambient kernel projections of rectangular matrices over \(D_H\) in those rings. [Regularity and matrix amplification](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions)
For example, apply square-matrix regularity to the off-diagonal block of the rectangular matrix in a larger square matrix and take the diagonal kernel corner.
The fiber equivalence therefore puts all rectangular group-ring kernel projections over \(G\) in matrices over \(D_G\).
The [bordered-pencil criterion](../ledger/Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil) then puts \(p_{\ker x}\) in \(D_G\) for every \(x\in D_G\).
Its proof needs only the finitely many group elements in an expression for \(x\), so this argument applies also to countable groups with no finite generating set.
This proves regularity of \(D_G\).
If \(D_G\) is regular and \(x\in D_H\), its constant kernel projection belongs to \(D_G\cap U_H=D_H\), proving the converse.
For a finitely generated virtually abelian direct factor \(V\), choose a free abelian subgroup \(\Lambda\) of finite index and apply [finite-index transfer](../ledger/Yin_L_A0073_v1.md#ascent-and-descent-of-kernel-projections) to \(H\times\Lambda\le H\times V\), of index \([V:\Lambda]\).
Rank zero for this abelian subgroup just gives the finite-index assertion itself.

For a further application, suppose \(\alpha\in\operatorname{Aut}(H)\) and \(\alpha^k\) is conjugation by \(h\in H\) for some \(k>0\).
In \(H\rtimes_\alpha\langle t\rangle\), the element \(h^{-1}t^k\) centralizes \(H\), has infinite order and generates a subgroup meeting \(H\) trivially, as seen in the quotient \(\mathbb Z\).
The index-\(k\) subgroup generated by \(H\) and \(t^k\) is consequently \(H\times\mathbb Z\).
Regularity of the division closure of this semidirect product \(H\rtimes_\alpha\mathbb Z\) is equivalent to regularity for \(H\).

### A test in the relative commutant of a cyclic extension

Write \(J=H\rtimes_\alpha\langle t\rangle\).
If \(\mathcal N(H)'\cap\mathcal N(J)\) strictly contains \(Z(\mathcal N(H))\), then \(D_J\) is regular exactly when \(D_H\) is regular.
Indeed, such a strict inclusion holds exactly when some \(g t^k\), \(g\in H\), \(k\ne0\), has a finite orbit under conjugation by \(H\).
To see this, choose an element of the relative commutant outside \(\mathcal N(H)\), using \(\mathcal N(H)'\cap\mathcal N(H)=Z(\mathcal N(H))\).
Its square-summable Fourier coefficients are constant on \(H\)-conjugacy orbits and at least one coefficient outside \(H\) is nonzero.
Its orbit must be finite.
Conversely the group-ring sum over such an orbit belongs to the relative commutant, with Fourier support outside \(H\).
Let \(K=C_H(g t^k)\), which has finite index in \(H\) by the orbit formula.
The group generated by \(K\) and \(g t^k\) is their direct product, since the latter generator centralizes \(K\) and has nonzero height.
Its index in \(J\) is \(|k|[H:K]\) by intersecting with \(H\) and projecting onto \(\mathbb Z\).
Applying finite-index transfer to both \(K\le H\) and \(K\times\langle g t^k\rangle\le J\), and using central direct-product transfer, proves the assertion.
Thus an example in which regularity fails to pass between \(H\) and its cyclic extension must have \(\mathcal N(H)'\cap\mathcal N(J)=Z(\mathcal N(H))\).

## Assessment history

### Decision maximal-fiber

| Field | Value |
| --- | --- |
| date | 2026-11-25T09:22 |
| status | proved |
| reason | The maximal rank of a torus fiber determines whether its rational image projection gives the full integrated kernel by Gram inversion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The single-fiber rationality test, the almost-everywhere version and regularity of direct products with finitely generated virtually abelian groups. |
| argument | [Argument](#argument) | Fiberwise specialization, the exact trace defect, ascent, descent and the finite conjugacy orbit criterion for cyclic extensions. |
| dependency | [Generic operator rank](Yin_C_A0012_v2.md#exact-generic-rank-for-rectangular-laurent-matrices) | Almost-everywhere maximal rank for bounded rectangular Laurent polynomials over a finite tracial von Neumann algebra. |
| dependency | [Bordered-pencil reduction](../ledger/Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil) | Passage from group-ring kernel projections to regularity of the scalar division closure. |
| dependency | [Scalar Gram pivots](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Reconstruct the inverse of a square affiliated unit using scalar inverses in the division closure. |
| dependency | [Unrestricted equation](Yin_C_A0131_v1.md#which-rationality-is-detected) | Equivalence of complete deletion and regularity of the division closure. |
| dependency | [Finite-index transfer](../ledger/Yin_L_A0073_v1.md#ascent-and-descent-of-kernel-projections) | Ascent and descent for virtually abelian factors and virtually inner cyclic actions. |
| review | [Independent proof review](../audits/reviews/Yin_R_A0166_v1.md#maximal-rank-fibers) | Entire fiber criterion, defect formula, direct products and cyclic extensions. |

## Current assessment

[Selected decision](#decision-maximal-fiber)
