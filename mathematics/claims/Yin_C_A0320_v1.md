---
author: Yin
---

# The order-sixteen marking of degrees odd and four excludes a four-site half kernel

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity.
If \(H\) has a character to \(C_{16}\) in which \(s\) has odd degree and \(t\) has degree four, no complex two-square rectangle \(K=P(t)-sQ(t)\) has regular nullity \(1/2\).
Here \(P(z)=Az+B,\ Q(z)=Cz+D\), and the matrix trace is unnormalized.

There is also an obstruction for a bounded transfer at any four-coset half kernel.
Put \(t_j=s^jts^{-j}\), \(K_4=\langle t_0,t_1,t_2\rangle\).
Assume \(K_4s^i,\ 0\le i<4\), are distinct and the displayed rectangle has nullity \(1/2\).
If \(M=PQ^{-1}\) and \(M^{-1}\) are regular on the circle, put \(F=\langle t_0,t_1,t_2,t_3\rangle\).
For some \(k\in\{-1,0,1\}\) one must then have
\[
          2[s^4]=k\big([t_3]+[t_2]+[t_1]+[t_0]\big)\quad\text{in }F_{\rm ab}.
\]
In particular \(8[s]=4k[t]\) in \(H_{\rm ab}\), with brackets denoting additive abelianization classes.
Thus any abelian quotient in which all three candidate equalities fail excludes a bounded transfer at this endpoint.

## Checking the hypotheses for the Fourier level sets

The [four-coset reduction](Yin_C_A0310_v1.md#statement) gives infinite-order marks, trivial consecutive cyclic intersections, regular pencils with invertible assembly, and nonmonomial determinants.
The [quartic transfer equation](Yin_C_A0186_v1.md#cutting-the-ordered-product) gives \(M(t_3)M(t_2)M(t_1)M(t_0)=s^4I\), \(s^4\in F\), and normality of \(F\) with cyclic quotient of order dividing four.
A constant point correspondence is excluded by the [two-dimensional test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) since \(s\notin\langle t\rangle\).
The [middle cut and rotation check](Yin_C_A0314_v1.md#the-original-group-hypotheses-for-the-pole-estimates) then give \(F=\langle t_i,t_{i+1}\rangle\) for each \(i\): the analytic cut places the product up to a translation over the intersection of \(\langle t_0,t_1\rangle\) and \(\langle t_2,t_3\rangle\), and the two-factor subgroup theorem recovers the first pair from that intersection.
Conjugation by \(s^2\) gives equality of the two adjacent-pair subgroups, after which normality of \(F\) gives every pair.
That argument only uses trivial consecutive cyclic intersection, the ordered quartic equation and absence of constant point correspondences; its rotation test uses the three independent projective coefficients of a two-square linear transfer.
If \(F\) were amenable, so would its finite extension \(H\) be, contradicting the fractional nullity by scalar injectivity and [Ore localization](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups).
Thus the [Fourier coefficient level-set theorem](Yin_C_A0318_v1.md#statement) applies and gives
\[
                           \det M(z)=c z^k,\qquad k\in\{-1,0,1\}.
\]

## Characters of the actual subgroup and the order-sixteen contradiction

Every entry of the circle-regular \(M\) has absolutely summable Laurent coefficients.
The quartic product over \(F\) is consequently an equality in the matrix algebra over \(\ell^1(F)\), by faithfulness of regular convolution.
The trivial character gives \(M(1)^4=I\), hence \(c^4=1\).
For any circle character \(\lambda\) of \(F\), the ordinary determinant of the evaluated product gives
\[
                 \lambda(s^4)^2
                      =c^4\prod_{j=0}^3\lambda(t_j)^k .
\]
Circle characters separate the points of \(F_{\rm ab}\), which is finitely generated.
This gives the claimed common relation in \(F_{\rm ab}\).
Under its natural map to \(H_{\rm ab}\), all conjugates of \(t\) have the same class and the relation becomes \(8[s]=4k[t]\).

At the stated order-sixteen marking reduction modulo four ensures the four cosets are distinct, since \(K_4\) maps to zero and \(s\) maps to a generator.
The [order-sixteen pole exclusion](Yin_C_A0316_v1.md#statement) supplies exactly the bounded transfer and its bounded inverse.
In the quotient, \(8[s]\) has degree \(8\bmod16\), whereas \(4k[t]\) has degree zero for every \(k\).
This contradiction excludes the half kernel.

## Assessment history

### Decision the-order-sixteen-quotient-obstruction

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:50 |
| status | proved |
| reason | The common monomial and the character determinant give incompatible degrees at the specified cyclic quotient. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The common monomial and the character determinant give incompatible degrees at the specified cyclic quotient. |
| argument | [Checking the hypotheses for the Fourier level sets](#checking-the-hypotheses-for-the-fourier-level-sets) | Checking the hypotheses for the Fourier level sets. |
| argument | [Characters of the actual subgroup and the order-sixteen contradiction](#characters-of-the-actual-subgroup-and-the-order-sixteen-contradiction) | Characters of the actual subgroup and the order-sixteen contradiction. |
| review | [The order-sixteen quotient obstruction](../audits/reviews/Yin_R_A0223_v1.md#the-order-sixteen-quotient-obstruction) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-order-sixteen-quotient-obstruction)
