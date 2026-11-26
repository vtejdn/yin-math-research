---
author: Yin
---

# Two short relations with independent exponent sums from the kernel of a four-corner matrix

## Statement

Let \(s,t\) be elements of infinite order in a discrete group \(G\).
Use the left regular representation and fixed invertible complex \(h\)-square matrices \(A,B,C,D\), and put
\[
       K=B+At-sD-stC,\qquad
       L=\|A\|+\|B\|+\|C\|+\|D\|,\qquad
       \beta=\min_{E\in\{A,B,C,D\}}|\det E| .
\]
If \(K\) has positive regular nullity \(\delta\), measured with the unnormalized matrix trace, choose a positive integer \(m\) with
\[
                  H_m=\sum_{j=1}^m j^{-1}>
                       \frac{2}{\delta}\log\frac{L^h}{\beta}.
\]
Among the words of length at most \(4m\) in \(s^{\pm1},t^{\pm1}\) that equal the identity in \(G\), there are two whose signed exponent sums in the two letters are linearly independent over \(\mathbb Q\).
The length counts letters in the given marking.
One may take \(m=\lceil (L^h/\beta)^{2/\delta}\rceil\), since \(H_m>\log m\).

The result applies directly to the original four labels in the [order-twenty half-kernel problem](Yin_C_A0311_v1.md#the-two-ends-in-the-equality-case), where all four corners are invertible, \(h=2\) and \(\delta=1/2\).
In its marking \((1,e_1),(2,e_2)\) the exponent pair \((n_s,n_t)\) of each relation has both entries even and \(n_s+2n_t\equiv0\bmod 5\).
Consequently the absolute determinant of the two exponent pairs is a positive multiple of twenty, at most \(16m^2\).
The certificate is obtained before any Schur inverse, so it also applies in the [visible-character branch](Yin_C_A0344_v2.md#statement).
The bound depends on the numerical corners through the displayed norm and determinant ratio.

## An integral estimate in every direction

Take any nonzero \((a,b)\in\mathbb Z^2\) and assign heights \(a,b\) to the two free letters.
This assignment need not be a character of \(G\).
Form the polynomial operator
\[
 P(z)=L^{-1}z^{-\min(0,a,b,a+b)}
               \big(B+z^bAt-z^a sD-z^{a+b}stC\big)
\]
and use \(\tau_h\), the regular trace divided by \(h\).
For \(|z|=1\) one has \(\|P(z)\|\le1\).
We claim that the integral with respect to normalized circle measure satisfies
\[
           \int_{\mathbb T}\tau_h[-\log(P(z)^*P(z))]\,dz
                     \le\frac{2}{h}\log\frac{L^h}{\beta}.
\]
The positive logarithmic integrand on the circle is understood by increasing regularization, allowing an infinite value at an individual point.

For \(\epsilon>0\) put \(X=P^*P+\epsilon I\).
The function \(\tau_h\log X\) is subharmonic. [Trace-log computation](Yin_C_A0276_v1.md#scaling-and-an-exposed-matching-on-the-universal-tree)
Indeed the derivative of the trace-log is \(\tau_h(X^{-1}\,dX)\), from the resolvent integral for the logarithm and traciality.
Its mixed complex derivative is
\[
    \tau_h\!\left(X^{-1}P'^*(I-PX^{-1}P^*)P'\right)\ge0 .
\]
The middle operator is positive by the singular-value identity \(I-PX^{-1}P^*=\epsilon(PP^*+\epsilon I)^{-1}\); conjugating by \(X^{-1/2}\) under the trace proves the inequality.
The mean over the circle is at least its value at zero.

If both \(a,b\) are nonzero the least height is achieved at just one corner, since it is \(\min(0,a)+\min(0,b)\).
The associated group translation is unitary, so \(\tau_h\log(P(0)^*P(0))\ge(2/h)\log(\beta/L^h)\).
If \(a=0\) or \(b=0\), the least slice consists of two adjacent corners.
After removing an overall translation on the left or right and a sign, it is \(L^{-1}(E+uF)\) with two original corners up to signs and \(u=s\) or \(t\).
The translation \(u\) has Haar distribution by its infinite order.
Thus its trace-log is
\[
 \frac2h\int_{\mathbb T}\log|\det(E+zF)|\,dz-2\log L .
\]
The polynomial has nonzero constant coefficient \(\det E\).
The scalar circle mean inequality for the logarithm of a polynomial, also at circle roots by integrability of their logarithms, bounds this below by \((2/h)\log(\beta/L^h)\).

In both cases this lower bound holds for every regularized value at zero because \(\tau_h\log(P(0)^*P(0)+\epsilon I)\) decreases to the unregularized trace-log.
In the circle inequality let \(\epsilon\) decrease to zero, using monotone convergence for the negatives after adding \(\log 2\) when \(0<\epsilon\le1\).
This proves the integral estimate.

## Detecting the relation in a finite moment

Write \(X(z)=P(z)^*P(z)\) on the circle.
For \(0\le x\le1\),
\[
                 -\log x=\sum_{j\ge1}\frac{(1-x)^j}{j}
                                  \ge H_m(1-x)^m ,
\]
with the usual infinite limit at zero.
The preceding bound gives
\[
     \int_{\mathbb T}\tau_h\!\left((I-X(z))^m\right)\,dz
         \le\frac{2}{hH_m}\log\frac{L^h}{\beta}
         <\frac{\delta}{h}
         \le \tau_h\!\left((I-X(1))^m\right).
\]
The last inequality is spectral calculus on the kernel of \(K\), since \(P(1)=K/L\).

Every summand of this trace polynomial consists of a numerical matrix trace times the regular trace of a group word of length at most \(4m\) and the power of \(z\) equal to the signed height of that word.
The common height shift cancels in \(P^*P\).
The regular trace keeps only words equal to the identity in \(G\), while the circle average also requires their height to be zero.
The strict inequality therefore forces a word of length at most \(4m\) equal to the identity in \(G\) with \((a,b)\cdot(n_s,n_t)\ne0\).
The cutoff is the same for all integral directions.
If the exponent vectors of all such short relators spanned a proper rational subspace, a nonzero integral covector would annihilate all of them, contrary to the preceding conclusion.

Finally the two sign conditions and the fifth-root condition in the order-twenty marking define a sublattice of index twenty in \(\mathbb Z^2\).
Two independent relator vectors in this sublattice have absolute determinant divisible by twenty.
Each has Euclidean norm bounded by its word length, giving the stated upper bound.

## Assessment history

### Decision two-short-relations-of-independent-heights

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:53 |
| status | proved |
| reason | Subharmonic estimates for every height direction and a single finite moment give the two independent bounded-length relations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Subharmonic estimates for every height direction and a single finite moment give the two independent bounded-length relations. |
| argument | [An integral estimate in every direction](#an-integral-estimate-in-every-direction) | An integral estimate in every direction. |
| argument | [Detecting the relation in a finite moment](#detecting-the-relation-in-a-finite-moment) | Detecting the relation in a finite moment. |
| review | [Two short relations of independent heights](../audits/reviews/Yin_R_A0237_v1.md#two-short-relations-of-independent-heights) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-two-short-relations-of-independent-heights)
