---
author: Yin
---
# A local saturation test for a ramified characteristic-zero lift of a product table

## Statement

Fix finite nonempty supports \(A,B\) in a group \(G\), a prime \(p\), and a full-support solution \(\xi\) of the actual product equations over a finite field of characteristic \(p\).
Normalize one coordinate on each side to one.
Let \(R\) be the Laurent polynomial ring over \(\mathbb Z_{(p)}\) on the remaining coordinates.
For each \(g\in AB\) put \(P_g=\sum_{xy=g}U_xV_y\), set \(I=(P_g:g\in AB)\subset R\), and let \(\mathfrak m\) be the maximal ideal of evaluation at \(\xi\).
Residue coordinates are understood up to the indicated embedding of \(R/\mathfrak m\) into a residue field.
Write \(I:p^\infty=\{f:p^j f\in I\text{ for some }j\ge0\}\).
The following are equivalent.

1. \(I:p^\infty\subseteq\mathfrak m\).
2. There is an exact full-support zero product with coefficients in a number field, integral units at a place above \(p\), reducing there to the specified point after a residue-field embedding.
3. For arbitrarily large \(n\) there are finite extensions \(L_n/\mathbb Q_p\) and full-support unit solutions in \(\mathcal O_{L_n}/p^n\mathcal O_{L_n}\) reducing to that point modulo the maximal ideal.

Consequently a finite identity \(p^j f=\sum_g H_g P_g\) in \(R\), with \(f(\xi)\ne0\), excludes every characteristic-zero specialization through this residue point.
It even excludes item 3 at every \(n>j\), regardless of ramification degree.
The precision in item 3 is measured in powers of \(p\).
Such an identity can be sought by saturation and reduction modulo the specified evaluation ideal, using the complete finite multiplication table.
Solutions with another reduction remain a separate question.
If the first condition holds on verified supports of a torsion-free group, any complex embedding of the number field in item 2 gives a scalar counterexample to [A0001](../tasks/Yin_T_A0001_v1.md#contract).

## Horizontal specialization

The containment in item 1 says exactly that \((R/I)_{\mathfrak m}[1/p]\ne0\), with localization at the image of \(R\setminus\mathfrak m\).
Indeed this localization vanishes exactly when \(p^j f\in I\) for some \(j\) and some \(f\notin\mathfrak m\).
When it is nonzero choose a prime \(\mathfrak q\) maximal among the primes containing \(I\), contained in \(\mathfrak m\), and avoiding \(p\).
Such primes exist by localization, and maximality is available since \(R\) is Noetherian.
Put \(S=R/\mathfrak q\) and \(D=S_{\mathfrak m/\mathfrak q}\).
This is a local domain in which \(p\) is a nonzero nonunit and every nonzero prime contains \(p\).

The domain \(D\) has dimension one.
Otherwise its maximal ideal has height at least two, and the finitely many minimal primes of \(pD\) have height one by the principal ideal theorem.
Choose an element of the maximal ideal outside their union by prime avoidance.
A minimal prime over the principal ideal of this element has height one and cannot contain \(p\), since in that case it would be one of the excluded primes.
This contradicts the choice of \(\mathfrak q\).

The base \(\mathbb Z_{(p)}\) is a universally catenary discrete valuation ring, \(S\) is a finite-type domain over it, and its residue at \(\mathfrak m/\mathfrak q\) is a finite field.
The dimension formula gives \(1=1+\operatorname{trdeg}_{\mathbb Q}\operatorname{Frac}S\), so \(K=\operatorname{Frac}S\) is a number field.
Apply the discrete valuation specialization lemma to the generic and closed points of \(\operatorname{Spec}D\), choosing the unchanged generic field \(K\).
It gives a discrete valuation ring in \(K\) dominating \(D\).
The valuation is a finite place above \(p\) because \(p\) belongs to its maximal ideal.
The images of the coordinates and their inverses in \(D\) give item 2.
These two standard commutative algebra inputs are the [dimension formula](https://stacks.math.columbia.edu/tag/02II) and the [valuation specialization lemma](https://stacks.math.columbia.edu/tag/054F).

Completion of \(K\) at this place and reduction modulo \(p^n\) give item 3, even with one fixed extension.
Conversely, when item 1 fails choose the displayed identity with \(f(\xi)\ne0\).
In every purported solution of precision \(n>j\) the image of \(f\) is a unit, and \(p^j\) is nonzero modulo \(p^n\mathcal O_{L_n}\).
The left side of the identity is nonzero while the right side vanishes.
This proves the claimed equivalence without requiring compatibility of the successive finite-precision solutions.
The scalar rank implication follows because \(\lambda(a)\) is nonzero and kills \(b\delta_e\ne0\), so its kernel projection has trace strictly between zero and one.

## A group table that requires ramification at the marked point

Let \(G=C_4\times C_2\), with generators \(g,h\) of orders four and two, respectively.
Use row labels \(1,g,h,g^3h\) and column labels \(1,g^3,g^2h,g^3h\).
Take the all-ones point in characteristic two.
With \(i^2=-1\) the row coefficients \((1,1,i,i)\) and column coefficients \((1,-1,i,-i)\) on these supports give
\[
 a=(1+g)(1+i g^3h),\qquad
 b=-g^3(1-g)(1-i g^3h).
\]
Their product is \(-g^3(1-g^2)(1+g^2)=0\).
All coefficients are units at \(1-i\) in \(\mathbb Z[i]\) and reduce there to one.
This also verifies the marked point directly.

Nevertheless the same point has no lift modulo \(4\) in the integers of any finite unramified extension of \(\mathbb Q_2\).
Number rows and columns from zero and normalize \(U_0=V_0=1\).
Multiplying the labels, the entire fibers at \(1,g,g^2h\) are \(\{(0,0),(1,1)\}\), \(\{(1,0),(3,2)\}\) and \(\{(0,2),(3,1)\}\).
Their equations give \(U_1V_1=-1,\ U_1=-U_3V_2,\ V_2=-U_3V_1\), hence \((U_3 V_1)^2=-1\).
In the unramified rings every element reducing to one has the form \(1+2s\), whose square is one modulo four.
The three equations contradict this identity since \(1\ne-1\) modulo four.
Their six cells also give the parity obstruction of the [unramified incidence test](Yin_C_A0038_v1.md#the-incidence-matrix-and-lifting).
Thus an actually inconsistent first unramified lifting step can coexist with an exact number-field lift of the same full group-product table through the same residue point.
This finite group has torsion and serves only to distinguish the two lifting tests.

For the [positive-characteristic construction](../ledger/Yin_L_A0034_v1.md#scope-for-the-group-ring-product) the saturation test needs the actual support elements after collecting coefficients and their entire product fibers.
An individual simultaneous-step component of the graph need not be an entire fiber.
No such local saturation or ramified lift of that construction is asserted here.

## Assessment history

### Decision ramified-lifting

| Field | Value |
| --- | --- |
| date | 2026-11-17T01:56 |
| status | proved |
| reason | Independent mathematical review covers the statement, argument and their stated limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The saturation test at the marked point, number-field and finite-precision equivalences, and the ramification example. |
| argument | [Proof](#horizontal-specialization) | Complete argument with its actual hypotheses and scope. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0070_v1.md#whole-argument-finding) | Independent review of the proof and its direct inputs. |

## Current assessment

[Selected decision](#decision-ramified-lifting)
