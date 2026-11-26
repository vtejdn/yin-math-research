---
author: Yin
---

# The spectral law and two-step returns in the exceptional order-twenty pencils

## Statement

Use the normalized exceptional orientation of the [twenty determinant lines](Yin_C_A0336_v1.md#statement), writing \(g,h\) for its two marks and \(M=P Q^{-1}\).
Character phases are absorbed into the numerical coefficients, so \(g,h\) denote group translations.
There is a matrix \(W\) invertible over the absolutely summable convolution algebra of \(\langle h\rangle\) such that
\[
                  W^{-1}M(h)W=\operatorname{diag}(m(h),-m(h)).
\]
The function \(m\) is a real-analytic orientation-preserving diffeomorphism of the unit circle and \(m(h)\) is a scalar unitary.
The probability law obtained by Haar sampling of \(h\) and giving its two transfer eigenvalues equal weight has density
\[
               \frac{3}{5-4\cos(2\theta)}\,\frac{d\theta}{2\pi}.
\]
The normalized traces of the even powers \(M(h)^{2k}\) are \(2^{-k}\) for \(k\ge0\), and the odd-power traces vanish.

Suppose additionally \(U=g^{-1}M(h)\) is similar by a bounded invertible regular matrix to a unitary.
This holds in particular if a fixed positive definite numerical form \(D\) satisfies \(M(y)^*D M(y)=D\) on the circle.
A half kernel then forces integers \(i,j\ge0,\ i\ne j\), satisfying
\[
                  g^{-1}h^i g^{-1}h^j=1,\qquad
                    (g^{-1}h^i)^2=h^{i-j}\in Z(H)\setminus\{1\}.
\]
Consequently a centerless group, or a group in which equal squares force equal elements, excludes a half kernel under this additional similarity hypothesis on \(U\).
The first similarity concerns only \(M(h)\); its conjugating matrix may fail to commute with \(g\).

## An analytic square root and its eigenlines

Write \(M(y)^2=B(y)I\) with \(B\) the [degree-two Blaschke product](Yin_C_A0336_v1.md#a-circle-valued-scalar-square-of-the-transfer).
It has no zeros or poles in a sufficiently narrow annulus about the circle, and its winding number is two.
There \(B(y)/y^2\) has a holomorphic logarithm since its logarithmic derivative has integral zero around the generator of the annulus.
Multiplying the exponential of half this logarithm by \(y\) gives a holomorphic square root \(m\), unimodular on the circle.
For the disk zeros \(a_1,a_2\) of \(B\), direct differentiation of its two elementary factors gives
\[
       \frac{d}{d\theta}\arg m(e^{i\theta})
            =\tfrac12\sum_{j=1}^2\frac{1-|a_j|^2}{|e^{i\theta}-a_j|^2}>0 .
\]
The winding number of \(m\) is one, proving the asserted diffeomorphism.

The holomorphic idempotents \(E_\pm(y)=(I\pm M(y)/m(y))/2\) each have rank one by the zero trace of \(M\).
The two kernel-line maps on the circle have images of area zero in the complex projective line since each image is covered by finitely many compact smooth arcs in local coordinates.
Choose a constant vector \(v\) whose line belongs to neither image.
The columns \(E_+(y)v,E_-(y)v\) form an invertible matrix \(W(y)\) on the circle and diagonalize \(M(y)\).
Its determinant stays nonzero on a smaller annulus, so \(W,W^{-1}\) both have absolutely summable Laurent coefficients.

The normalized trace of \(M^{2k}=B^k I\) under Haar integration is \(B(0)^k=2^{-k}\) by the mean-value formula.
The odd traces vanish pointwise because the two eigenvalues are opposite.
The displayed density has precisely these moments by the geometric series of the Poisson kernel with parameter \(1/2\) at twice the angle.
Negative Fourier coefficients are conjugates of positive ones for the probability measure.
Uniqueness of the Fourier coefficients proves the formula.

## A necessary group relation for a unitary twisted transfer

Under the constant-form condition, conjugation by \(D^{1/2}\) makes the transfer unitary and commutes with \(g\), proving the sufficient condition for the asserted bounded similarity of \(U\).
Assume this similarity.
The sign character on \(g\) gives eigenspaces at \(1,-1\) each of unnormalized dimension \(1/2\).
If the trace of \(U^2\) were zero, use its unitary representative and normalize the two-coordinate trace to one.
The spectral measure of the square has mass \(1/2\) at one, by the two eigenspaces.
The remaining mass \(1/2\) would have integral \(-1/2\), forcing it all onto \(-1\) by equality in the lower bound on the real part.
Then \(U\) would have positive-dimensional eigenspace at \(i\) or \(-i\), contradicting the [three-eigenspace budget](Yin_C_A0329_v1.md#statement).
Hence the trace of \(U^2\) is nonzero.

Since \(M\) is holomorphic on a neighborhood of the closed disk its Taylor coefficients are absolutely summable and involve exponents \(i\ge0\) only.
Expansion of the two factors of \(U\) shows that only pairs with \(g^{-1}h^i g^{-1}h^j=1\) can contribute to the trace.
At least one such pair exists.
Put \(a=g^{-1}h^i\), so \(a^2=h^{i-j}\).
If \(i=j\), torsion-freeness gives \(a=1\), forcing \(H\) to be cyclic, contrary to its marked quotient.
The nonidentity element \(h^{i-j}\) commutes with \(a,h\), which generate \(H\).
If equal squares imply equality, \((h^{-1}ah)^2=a^2\) also forces \(a\) to commute with \(h\).
Then \(H\) is finitely generated torsion-free abelian, where Fourier transformation gives integer kernel dimension from the generic numerical rank of a Laurent polynomial matrix on the torus.

## Assessment history

### Decision the-spectral-law-and-the-two-step-return

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:54 |
| status | proved |
| reason | The annular eigenline decomposition gives the spectral law, and bounded similarity of the twisted transfer forces an actual central return. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The analytic law and the original-group obstruction under the additional similarity hypothesis. |
| argument | [An analytic square root and its eigenlines](#an-analytic-square-root-and-its-eigenlines) | The annular diagonalization, moments and density. |
| argument | [A necessary group relation for a unitary twisted transfer](#a-necessary-group-relation-for-a-unitary-twisted-transfer) | The spectral mass bound and the actual two-step return. |
| dependency | [Twenty determinant lines](Yin_C_A0336_v1.md#statement) | The preceding character alternative and the two prototypes. |
| review | [Twenty exceptional coefficient lines](../audits/reviews/Yin_R_A0232_v1.md#twenty-exceptional-coefficient-lines) | Independent inspection of the original enumeration and the two prototypes. |
| review | [The spectral law and the two-step return](../audits/reviews/Yin_R_A0232_v1.md#the-spectral-law-and-the-two-step-return) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-spectral-law-and-the-two-step-return)
