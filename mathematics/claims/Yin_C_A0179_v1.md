---
author: Yin
---

# Two-dimensional cyclic transfers for an indicable pair of labels

## Statement

Let \(s,t\) generate a torsion-free discrete group \(H\), with \(t\) of infinite order, and let \(M(u)\in{\rm GL}_2(\mathbb C(u))\).
Use the regular representation with unnormalized matrix trace.
Suppose \(\chi:H\to\mathbb Z\) is nonzero and put \(a=\chi(s)\), \(b=\chi(t)\).
If every nonzero scalar in \(\mathbb C H\) acts injectively, then \(sI_2-M(t)\) has **integer regular rank**.
Consequently if a two-label subgroup is indicable, meaning it surjects onto \(\mathbb Z\), every [four-column pencil with two copies of each label](Yin_C_A0184_v1.md#statement) has integer rank under that scalar hypothesis.
This excludes every proper fractional constant-column increment on the same list, since quotienting by the constant column gives another pencil on the list.
It also excludes an ordinary rank-one commutator sum with two witnesses of ranks at most two on that pair by the [prescribed-list criterion](Yin_C_A0167_v2.md#statement).
The results pass to an arbitrary discrete overgroup by regular subgroup trace preservation.

There are cases with no scalar injectivity assumption at all.
If \(b=0\), the transfer has rank two.
If \(b\ne0\), put \(n=|b|/\gcd(|a|,|b|)\).
For \(n=2\) the transfer has integer rank, and for \(n\ge3\) it has rank two.
In particular, for the [fourth-order phase induced by an integer character](Yin_C_A0187_v1.md#when-the-finite-phase-comes-from-an-integer-character) the two-dimensional rational transfer has zero kernel.
This conclusion uses no assumption on higher matrix ranks and no uniform spectral gap.

## Comparing ranks along a character

Write \(M=P/q\) with a polynomial matrix \(P\) and a nonzero scalar polynomial \(q\).
On the complex parameter line away from zero put
\[
 L(z)=z^a sI_2-M(z^b t).
\]
Its rank equals the rank of the bounded Laurent polynomial matrix \(z^a s q(z^b t)I_2-P(z^b t)\), obtained by multiplying on the right by the affiliated unit \(q(z^b t)\).
Every nonzero rational function evaluated at \(z^b t\) is an affiliated unit, by the bilateral shift model of \(t\).
For \(|z|=1\), twisting by \(\chi\) preserves rank, so the rank is constant there.
The [finite-evaluation inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) shows that this is the maximum rank over \(z\ne0\), after clearing the negative exponents by one scalar monomial.
Indeed any value can be compared with arbitrarily many values on the circle.
The same argument shows that if on a real interval the ranks are all at most one, the rank on the circle is also at most one.

For \(b=0\) we have \(a\ne0\).
Twists fix \(M(t)\) and give infinitely many equal-dimensional eigenspaces of \((s^{-1}I_2)M(t)\) at distinct scalars.
Each finite selection forms an algebraic direct sum by polynomial interpolation, so each eigenspace has dimension zero.

Suppose \(b\ne0\) and replace \(\chi\) by its negative if needed to have \(b>0\).
If \(M\) is a scalar rational matrix \(fI_2\), then \(s-f(t)\) is either zero or an affiliated unit after clearing the right denominator under scalar injectivity.
When \(n\ge2\), its two groups of Laurent exponents in the deformation, congruent to \(a\) and \(0\) modulo \(b\), are disjoint.
The lowest coefficient is a nonzero scalar multiple of a group element, so the normalized operator tends in norm to a unit as \(z\downarrow0\).
This gives rank two on the circle without scalar injectivity.

## Off-diagonal pivot and the coefficients of the remaining scalar

If \(M\) is not a scalar rational matrix, a change of constant basis makes its upper-right entry nonzero as a rational function.
In fact a matrix preserving every constant line is scalar, as is seen on two coordinate lines and their diagonal.
Write its entries in this basis as \(A,B,C,D\) in row order, with \(B\ne0\).
Eliminating the pivot \(-B\) in \(L(z)\) gives rank \(1+\operatorname{rk}T(z)\), where all rational functions in the following expression are evaluated at \(z^b t\):
\[
 T(z)=z^{2a}s B^{-1}s-z^a\bigl(s B^{-1}A+D B^{-1}s\bigr)
                         +(D B^{-1}A-C).
 \tag{1}
\]
The order of every group translation here is fixed.
This scalar is bounded for all sufficiently small positive \(z\).
Each of the four rational coefficient functions has a Laurent series near zero with finite principal part and absolute convergence on sufficiently small circles.
Substitution \(u=z^b t\) gives norm-convergent operator series, since \(t\) is unitary.

At any fixed power of \(z\), the terms from the first summand, the middle pair, and the last summand respectively have the forms
\[
       \lambda s t^j s,\qquad \mu s t^k+\eta t^k s,\qquad \theta t^\ell ,
 \tag{2}
\]
whenever the corresponding degrees \(2a+bj,\ a+bk,\ b\ell\) occur.
In particular every coefficient of the Laurent series of \(T(z)\) lies in \(\mathbb C H\).
If the entire series vanishes, then \(L(z)\) has rank one on a positive interval.
The rank comparisons above and the nonzero off-diagonal pivot give rank exactly one on the unit circle.
Otherwise let \(V\) be the first nonzero coefficient, at degree \(p\).
Then \(z^{-p}T(z)\to V\) in operator norm as \(z\downarrow0\).

When \(V\) is injective this implies \(\liminf_{z\downarrow0}\operatorname{rk}T(z)=1\).
Indeed on the spectral subspace \(1_{[\epsilon,\infty)}(|V|)\) the operator \(V\) is bounded below by \(\epsilon\).
Norm approximation keeps the restriction injective for all sufficiently small \(z\); the traces of these subspaces increase to one as \(\epsilon\downarrow0\).
The maximal rank on the circle is then two.
Scalar group-ring injectivity applies to every possible nonzero \(V\) in (2), also when all three exponent classes overlap.
This proves the integer-rank dichotomy for every nonzero character.

For \(n\ge3\), the three classes \(2a,a,0\) modulo \(b\) are pairwise distinct.
The first summand in (1) has a nonzero coefficient in its own class since \(B^{-1}\ne0\), so the whole series cannot vanish.
Every possible leading coefficient is a monomial or a sum of two monomials by (2).
A nonzero such scalar is injective in a torsion-free regular group: after extracting one translation, distinct terms reduce to a nonzero linear polynomial in a translation of infinite order.
Thus the rank is two.
For \(n=2\), the first and last classes coincide while the middle class is disjoint from them.
Even in the shared class the coefficient has at most two terms.
The same binomial argument gives rank two whenever the series is nonzero, leaving only rank one if it is identically zero.
This proves the unconditional claims.

For the pencil consequence, cyclically contained labels have integer ranks by Fourier transformation.
For the remaining pairs the [four-column reduction and singular-block tests](Yin_C_A0184_v1.md#singular-cyclic-blocks) already give integer rank outside the case of two invertible cyclic blocks.
In that case its rank is two plus the rank of the transfer in the statement, including when the rank under consideration is a fractional value other than seven halves.
An indicable subgroup generated by the two labels has a nonzero character on at least one of them, as used above.
The proof leaves open the general two-label case with finite abelianization.

## Assessment history

### Decision indicable-label-pair

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:23 |
| status | proved |
| reason | The independent review verified the full argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Integer rank of all four-column pencils and the unconditional transfer cases. |
| argument | [Comparing ranks along a character](#comparing-ranks-along-a-character) | Behavior on the unit circle and on a real interval. |
| argument | [Off-diagonal pivot and the coefficients of the remaining scalar](#off-diagonal-pivot-and-the-coefficients-of-the-remaining-scalar) | Ordered Schur scalar, residue classes, spectral subspaces and application to pencils. |
| review | [Indicable label pair](../audits/reviews/Yin_R_A0177_v1.md#indicable-label-pair) | Independent review of the stated result and its argument. |

## Current assessment

[Selected decision](#decision-indicable-label-pair)
