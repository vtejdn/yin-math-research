---
author: Yin
---

# The counts of simple boundary poles agree and reciprocal diagonal factors are excluded

## Statement

Use the [order-24 half-kernel hypotheses](Yin_C_A0290_v1.md#statement) for \(M(z)=(Az+B)(Cz+D)^{-1}\).
The numbers of distinct unit-circle poles of \(M\) and \(M^{-1}\) are equal, and each is one or two.
If this common number is one, the residue matrices of the two rational functions at their respective circle poles are proportional rank-one matrices.
These assertions count actual matrix poles.

A further exclusion applies to transfers with rational diagonal factorizations.
Suppose in some constant basis
\[
        M(z)={\rm diag}(1,f(z))E{\rm diag}(1,g(z)),\qquad
                   E=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
where \(ad\ne0\), \(\det E\ne0\), and \(f,g\) are nonconstant scalar rational functions.
Assume that for each nontrivial root of unity \(\eta\), neither \(f(\eta z)\) nor \(g(\eta z)\) is proportional to the corresponding unrotated function.
Then some positive power of \(s\) is central in \(H\).
If \(fg\) is constant, this factorization is impossible.
In particular this excludes the reciprocal pair \(f=(z-\beta)/(z-\alpha),\,g=1/f\) for distinct circle points, where the matrices can have only simple boundary poles.
Neither conclusion uses a specialization of an affiliated inverse to a quotient.

## One pole on a side bounds all residue lines

The [double-pole exclusions](Yin_C_A0300_v1.md#statement) give at least one and at most two circle poles on each side, all simple.
In fact at every boundary determinant zero the corresponding denominator pencil must have rank one.
A zero matrix at that point would give a square determinant zero, and the stacked pencil has rank two there by the [assembled coefficient theorem](Yin_C_A0184_v1.md#statement).
The numerator is therefore injective on the denominator kernel, and the rank-one adjugate gives a nonzero rank-one residue.
Apply the same argument with numerator and denominator interchanged.

Suppose \(M\) has only one circle pole, with residue \(R\).
Choose a nonzero row \(\ell\) and column \(v\) with \(\ell R=0,\ Rv=0\).
Both \(\ell M(z)\) and \(M(z)v\) are bounded on the circle, so \(\ell M(t_1)M(t_0)v\) is bounded.
By the [middle identity](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors), its counterpart \(\ell M^{-1}(t_0)M^{-1}(t_1)v\) is also bounded, since the two scalars differ by unitary group translations on the two sides.
At every circle pole of the inverse with residue \(S\), one has \(\ell S=0\) and \(Sv=0\).
Indeed otherwise a row or column factor would have a simple pole while the other factor spans the relevant two-dimensional space on a regular arc by the absence of a [constant point correspondence](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).
The [arc compression proof](Yin_C_A0292_v1.md#a-scalar-compression-still-detects-a-double-pole) gives a singular value tail at least \(c h^{-1}\) at high levels.
For clarity, its high singular projection has trace at least \(c'/h\) at a simple pole; taking the other column on the compact arc gives positive definite integrated covariance, which retains a fixed positive fraction of that trace at a fixed multiple of the level.
The adjoint gives the same conclusion for a pole in the column.
This contradicts boundedness.
It follows that every \(S\) has the same image and kernel as \(R\).

If there were two different inverse circle poles they would exhaust the two possible finite roots of \(\det(Az+B)\).
Its quadratic coefficient would be nonzero, making \(A\) invertible and \(M^{-1}(z)\) bounded at infinity.
Partial fractions would express \(M^{-1}\) as a constant matrix plus a scalar rational function times the fixed residue direction \(R\).
Such a pencil admits a constant point correspondence: normalize on the left by an invertible member and use an eigenline of the second constant matrix.
This contradicts the cited criterion.
The argument with \(M^{-1}\) on the single-pole side is identical, reversing the order of the neighboring cyclic groups.
It proves both the count and the stated residue alignment.

## Different rational functions on the diagonal

In a fractionally ranked case \(bc\ne0\), since otherwise the transfer is triangular in the indicated constant basis.
Set \(x=s^{-1}\), \(X=ax,\ Y=d g(t)x f(t)\), \(q=bc/(ad)\), \(k=(1-q)^{-2}\), and \(Z=X+Y\).
Conjugate \(xM(t)\) by \({\rm diag}(1,g(t))\), and then make the same constant diagonal conjugation as in the [two-entry calculation](Yin_C_A0300_v1.md#scalar-equations-from-two-off-diagonal-entries).
The resulting fourth-root matrix has rows \((X,X),(qY,Y)\).
Here \(Z\) is an affiliated unit: \(Zx^{-1}=a+d\,g(t)f(t_{-1})\) becomes a nonzero group-ring scalar on clearing the denominator of \(g(t)\) on the left and that of \(f(t_{-1})\) on the right.
Nonvanishing follows by the [injective two-variable tensor map](Yin_C_A0291_v1.md#local-fourier-blocks-and-separation-of-repeated-endpoints), since \(a+d\,g(z)f(w)\) is nonzero in independent variables.
The denominators and cleared scalar are units by scalar injectivity.
The cited calculation applies to these \(X,Y,Z\) without requiring that \(f=g\), and gives
\[
                [Y,P]=0,\qquad Y^2ZX^2=-kZ,\qquad P=kX^{-2}-X^2 .
\]

Use the subgroup \(K\) of elements carrying some positive power of \(s\) to itself or its inverse, and the [two-term commutant theorem](Yin_C_A0300_v1.md#the-commutant-of-a-two-term-laurent-polynomial).
It gives \(Y\in U(K)\), so \(g(t)f(t_{-1})\in U(K)\).
By the [two-factor subgroup argument](Yin_C_A0300_v1.md#the-two-factor-support-forces-the-sign-to-be-positive), this forces \(t\in K\): the two factors obey precisely the nonrotation assumptions and the adjacent cyclics are disjoint.
Thus \(K=H\), with its sign positive on both generators by the normalized abelianization.
In particular \(t\) commutes with some positive power of \(s\), which is central since \(s,t\) generate \(H\).
Again the commutant theorem gives \([Y,s^2]=0\), so cancellation of \(Z\) gives \(Y^2=-kX^{-2}\).

If \(fg=\kappa\in\mathbb C^\times\), then \(Y=d\kappa f(t)^{-1}x f(t)\).
The last square identity implies
\[
                    s^{-2} f(t) s^{-2}=\lambda f(t)
\]
for some nonzero scalar \(\lambda\).
Since \(f(t)\ne0\), preservation of its singular value distribution gives \(|\lambda|=1\).
Its nonzero bounded polar part satisfies the same equation.
Square-summable Fourier coefficients on a nonzero orbit of \(h\mapsto s^{-2} h s^{-2}\) then give a finite orbit and an element of negative sign in \(K\), a contradiction.
This proves the reciprocal exclusion.

## Assessment history

### Decision compression-of-the-simple-residues

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:54 |
| status | proved |
| reason | Compression forces proportional residues when each side has one circle pole, and excludes the specified reciprocal factorization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Compression forces proportional residues when each side has one circle pole, and excludes the specified reciprocal factorization. |
| argument | [One pole on a side bounds all residue lines](#one-pole-on-a-side-bounds-all-residue-lines) | One pole on a side bounds all residue lines. |
| argument | [Different rational functions on the diagonal](#different-rational-functions-on-the-diagonal) | Different rational functions on the diagonal. |
| review | [Compression of the simple residues](../audits/reviews/Yin_R_A0216_v1.md#compression-of-the-simple-residues) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-compression-of-the-simple-residues)
