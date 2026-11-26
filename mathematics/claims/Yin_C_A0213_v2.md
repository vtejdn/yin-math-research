---
author: Yin
---

# Reducing an odd-dimensional twisted norm at controlled scalar inverse depth

## Statement

Let \(N\triangleleft J\) have index two and fix \(g\in J\setminus N\).
Put \(u=g^2\in N\) and \(\alpha=\operatorname{Ad}_g\).
Use the [actual scalar inverse layers](Yin_C_A0129_v1.md#statement) in the finite regular affiliated algebras.
Suppose \(j\ge0\) and a matrix \(V\) of odd size \(2k+1\) over \(D_j(N)\) satisfies
\[
                            V\alpha(V)=u^{-1}I .
\]
There is a finite elimination procedure with the following alternative.

* At some step \(i<k\), the procedure exhibits a nonzero scalar in \(D_{j+i}(N)\) of regular rank strictly between zero and one.
* It yields a scalar \(b\in D_{j+i}(N)\) for some \(0\le i\le k\) with \(b\alpha(b)=u^{-1}\).
  Then \(b^{-1}\) is in the same layer and the two complementary idempotents \((1\pm bg)/2\) in \(D_{j+i}(J)\) both have unnormalized scalar trace dimension \(1/2\).

In particular \(P_{j+k-1}(N)\) suffices to force the scalar norm when \(k\ge1\).
At \(k=0\) the input itself is scalar.
Conversely any scalar solution at depth \(j\) gives a solution of every odd size at that same depth, by taking a scalar diagonal.
The forward depth estimate keeps its explicit possible loss of one inverse layer per two coordinates.

For the [order-26 norm](Yin_C_A0199_v1.md#subgroup-coordinates-and-the-odd-dimensional-norm) the alternative gives a fractional-rank scalar on \(N=[H,H]\) at depth at most six or a scalar norm at depth at most seven on \(N\).
In the second branch the half-dimensional idempotent is on the index-13 subgroup \(J\) of the original group \(H\).
At the first step, any failure of scalar injectivity detected by this procedure is already the Schur complement of one two-by-two matrix over \(\mathbb CN\) with a nonzero group-ring pivot.
Here \(N\) starts as the kernel of the character onto \(C_{26}\).
To identify it with the commutator subgroup, apply the [exclusion of all abelian quotient orders at least 27](Yin_C_A0201_v1.md#consequence-for-finite-abelian-quotient-orders) under the torsion-free scalar-injective half-rank hypotheses.
The finitely generated abelianization surjects onto \(C_{26}\), and any larger finite abelianization or infinite finitely generated abelianization would give an excluded quotient.

Under \(P_0(J)\) any resulting scalar \(b\) satisfies a two-sided denominator obstruction: for all \(0\ne r,c\in\mathbb CN\), one has \(rbc\notin\mathbb CN\).
In particular no odd-sized solution can have all its entries in an \(\alpha\)-invariant division subring \(Q\subset U(N)\) in which every element admits such two-sided clearing in \(\mathbb CN\).
A classical fraction field of a suitable \(\alpha\)-invariant right Ore domain in \(\mathbb CN\) is one example.
The unrestricted scalar norm equation and the failure branch remain open.

## Removing a cyclic pair of coordinates

For a current matrix \(W\) on \(n\) coordinates over \(D_l(N)\), consider the additive semilinear map \(T(x)=W\alpha(x)\) on affiliated columns.
It satisfies \(T(xa)=T(x)\alpha(a)\) and
\[
                    T^2(x)=W\alpha(W)\alpha^2(x)=xu^{-1}.
\]
The last equality uses \(\alpha^2(x)=u x u^{-1}\) entrywise.
Let \(e\) be the first standard column and \(w=T(e)\), the first column of \(W\).
If \(w=e b\), then \(e u^{-1}=T^2(e)=e b\alpha(b)\).
This gives the scalar solution immediately; \(b\ne0\).
Indeed \(\alpha(b)u\) is its right inverse, hence its two-sided inverse in the directly finite affiliated algebra, and is in the same scalar layer.

If \(w\) has an off-diagonal entry, choose any one that is nonzero, say at coordinate \(i\ne1\).
If \(w_i\) is not an affiliated unit its scalar rank is strictly between zero and one, giving the first branch.
Otherwise replace the first and \(i\)-th coordinate directions by the pair \(e,w\).
Concretely let \(C\) have first two columns \(e,w\) followed by all standard columns with indices different from \(1,i\).
This is an affiliated unit over \(D_{l+1}(N)\).
For an output \(y\), the second coefficient in this basis is \(w_i^{-1}y_i\); subtracting \(w\) times this coefficient recovers the other coordinates.
Thus the only new scalar inverse used for \(C^{-1}\) is \(w_i^{-1}\).

The matrix \(\widetilde W=C^{-1}W\alpha(C)\) satisfies \(\widetilde W\alpha(\widetilde W)=u^{-1}I\), using \(\alpha^2(C)=u C u^{-1}\).
Its first two columns express \(T(e)=w\) and \(T(w)=eu^{-1}\).
It is block upper triangular with upper left block
\[
                          \begin{pmatrix}0&u^{-1}\\1&0\end{pmatrix}.
\]
The bottom diagonal block therefore satisfies the same norm equation, has two fewer coordinates, and has entries in \(D_{l+1}(N)\).
Iterating proves the stated alternative.
The fixed layers are invariant under the group automorphism and under inclusion into \(U(J)\).

## The regular trace and the first pivot at order 26

From a scalar solution one obtains \((bg)^2=b\alpha(b)u=1\) in \(D_{j+i}(J)\).
The nontrivial sign character of \(J/N\) sends \(bg\) to \(-bg\) and fixes the affiliated coefficients from \(N\).
It preserves the regular trace and interchanges the two algebraic idempotents.
Their finitely generated affiliated images form a direct sum of total dimension one, and the twist gives both images the same dimension.
This proves the half-dimensional conclusion without assuming boundedness of \(b\).

In the order-26 construction write \(Z=(-a_0^{-1}r',I_{13})^{\mathsf T}\) in stacked block notation, meaning that its first row is \(-a_0^{-1}r'\) and its bottom block is \(I_{13}\).
Here \(0\ne a_0\in\mathbb CN\) and all entries of \(r'\) lie in \(\mathbb CN\).
The original norm matrix consists of the bottom thirteen rows of \(L_0\alpha(Z)\) with \(L_0\) over \(\mathbb CN\).
Every entry is a group-ring scalar minus a product of a group-ring entry, the single inverse \(\alpha(a_0)^{-1}\), and another group-ring entry.
Thus a fractional first pivot is exactly a nonzero Schur scalar of the asserted form.
Subsequent nonunit pivots have the bounded depth proved above.
Such a scalar also yields a finite group-ring matrix of noninteger rank by [linearizing the actual rational expression](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations).
The semilinear elimination uses only the original subgroups at every step.

## Two-sided denominators in the scalar branch

Suppose \(b\alpha(b)=u^{-1}\) in \(U(N)\), and suppose \(P_0(J)\).
If \(rbc\) were in \(\mathbb CN\) for nonzero \(r,c\in\mathbb CN\), then
\[
              r(1-bg)\alpha^{-1}(c)=r\alpha^{-1}(c)-(rbc)g
\]
would belong to \(\mathbb CJ\).
Its term in the identity coset of \(N\) is nonzero, since both factors in that term are affiliated units.
Its other term has support in the other coset.
Hence this group-ring scalar would have rank one by \(P_0(J)\).
But the multipliers on either side of \(1-bg\) are units and the sign-character calculation gives rank \(1/2\) for \(1-bg\).
This contradiction proves the obstruction.
It uses no extension of augmentation to a rational layer.

If the entries of the initial odd matrix lie in \(Q\) as in the statement, every nonzero pivot is a unit already in \(Q\).
Basis changes, the twist and all lower diagonal blocks remain over \(Q\).
The procedure produces a scalar \(b\in Q\), violating the assumed denominator property.
In a classical right fraction field \(b=pq^{-1}\) one can take \(r=1,\ c=q\).
This applies whenever a right Ore domain with its actual embedding has an \(\alpha\)-invariant fraction field containing all the entries; it places no Ore assumption on the entire group ring.
The two-dimensional block displayed above is itself always a solution, since \(\alpha(u)=u\), so the odd-size restriction is essential.

## Version history

The [original odd-dimensional calculation](Yin_C_A0213_v1.md#removing-a-cyclic-pair-of-coordinates) gives the same elimination and depth bounds.
This version spells out the order-26 abelianization argument and adds the two-sided denominator obstruction.

## Assessment history

### Decision odd-twisted-norms-and-two-sided-clearing

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:12 |
| status | proved |
| reason | Independent review verified the elimination, the identification of the kernel subgroup and the obstruction to clearing. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The fractional-rank or scalar-norm alternative with its depth bounds. |
| argument | [Removing a cyclic pair of coordinates](#removing-a-cyclic-pair-of-coordinates) | Semilinear quotient by a cyclic coordinate pair using one inverse. |
| argument | [The regular trace and the first pivot at order 26](#the-regular-trace-and-the-first-pivot-at-order-26) | Trace dimension and the first Schur pivot on the commutator subgroup. |
| argument | [Two-sided denominators in the scalar branch](#two-sided-denominators-in-the-scalar-branch) | The scalar group-ring obstruction and its division-ring consequence. |
| argument | [Version history](#version-history) | The subgroup identification added in the fixed revision. |
| review | [Odd twisted norms and two-sided clearing](../audits/reviews/Yin_R_A0190_v1.md#odd-twisted-norms-and-two-sided-clearing) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-odd-twisted-norms-and-two-sided-clearing)
