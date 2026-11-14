---
author: Yin
---

# A planar common character with a nonnormal residual of quadratic singular mass

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) have normalized area law on the unit disk and let \(S\) be a standard semicircular element free from \(W^*(Z)\) in their finite tracial free product.
For \(1/2<\alpha<1\) and \(0<c<1/2\) put \(Y=c|Z|^\alpha S|Z|^\alpha\).
The pair \((Z,Y)\) has actual starred conjugate variables, and its original canonical duals and their Hilbert adjoints contain all bounded vectors in their domains.
Its marginal algebras are correlated.
The algebra \(C^*(Z,Y)\) admits the character \(Z,Y\mapsto0,0\), at which every marginal secant phase is a limit of phases of chords approaching \(0\).
For every \(0<r<1\), among projections \(e\in W^*(Z)\) of trace \(r^2\), the common minimizer \(e_r=1_{[0,r]}(|Z|)\) gives
\[
 \min_e\frac{\|Ze\|_2^2}{r^2}=\frac{r^2}{2},\qquad
 \min_e\frac{\|Ye\|_2^2}{r^2}
          =\frac{c^2r^{2\alpha}}{(1+\alpha)^2}.
\]
For the fixed omitted shift \(Y\) the residual \(T=Z-Y\) is nonnormal and satisfies
\[
                    \lim_{s\downarrow0}
                     \frac{\tau(1_{[0,s]}(|T|))}{s^2}=1.
\]
In particular its cubic singular concentration integral is finite even though a common character and all marginal secant directions are present at the origin.

## Argument

### The Gaussian kernel and the two vacua

Let \(Z\) be the coordinate on the unit disk with normalized area probability \(\mu\), put \(D=|Z|\), and let \(U\) be its polar unitary.
Take a standard semicircular \(S\) free from \(W^*(Z)\), \(1/2<\alpha<1\), \(0<c<1/2\), and \(Y=cD^\alpha S D^\alpha\).
The tuple \((Z,Y)\) has actual starred conjugate variables and both full dual domains.
Indeed its positive Gaussian amplitude \(b(z,v)=c|zv|^\alpha\) has bounded row norms and square-integrable reciprocal since \(\int_0^1 t^{1-2\alpha}dt<\infty\).
The drift vanishes, and the second base-vacuum kernel in the [Gaussian drift and covariance criterion](Yin_C_F0260_v1.md#statement) has squared modulus
\[
       \frac{((|z|/|v|)^\alpha-(|v|/|z|)^\alpha)^2}{|z-v|^2}.
\]
For \(r=|z|>s=|v|\), the angular mean of the reciprocal denominator is \((r^2-s^2)^{-1}\) by the geometric series in \(s/r\).
Using both radial orderings and substituting \(s=rt\), the double integral is \(4\int_0^1 t(t^\alpha-t^{-\alpha})^2\,dt/(1-t^2)\).
It is finite since the integrand is of order \(t^{1-2\alpha}\) at zero and \(1-t\) at one.
The disk has its [actual marginal vacuum](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density), so the criterion applies.

### The common character and its optimal marginal cutoffs

Let \(e_r=1_{[0,r]}(D)\), of trace \(r^2\), and let the tracial Hilbert space carry the left actions.
Freeness gives \(\mathbb E_{W^*(Z)}(Y^2)=c^2 \tau(D^{2\alpha})D^{2\alpha}=c^2D^{2\alpha}/(1+\alpha)\).
Consequently the unit vector \(e_r/r\) satisfies
\[
 \|Z e_r/r\|_2^2=\|Z^*e_r/r\|_2^2=r^2/2,\qquad
 \|Y e_r/r\|_2^2=c^2 r^{2\alpha}/(1+\alpha)^2 .
\]
Among marginal projections of trace \(r^2\), \(e_r\) minimizes each squared error, by integration of the corresponding increasing radial function.
Both errors tend to zero, so for each starred polynomial \(p\) the vector \((p(Z,Y)-p(0,0))e_r/r\) tends to zero by factoring the last letter of each nonconstant word.
In particular \(|p(0,0)|\le\|p(Z,Y)\|\), and evaluation extends to a character of \(C^*(Z,Y)\).
The same conditional square is nonconstant, so the two marginal algebras are correlated.
Every unoriented chord direction occurs arbitrarily near the common point \(0\).

### Tail comparison for the residual inverse

For the fixed omitted shift \(b=Y\) the residual \(T=Z-Y\) satisfies
\[
                       \tau(1_{[0,s]}(|T|))\sim s^2\qquad(s\downarrow0).
\]
To see this, work in the algebra of tracially measurable affiliated operators, with products and inverses there.
The inverse exists since
\(T=D^{1/2}(U-cD^{\alpha-1/2}SD^{\alpha-1/2})D^{1/2}\), the exterior factor has zero kernel, and the middle factor is invertible by the norm bound \(c\|S\|=2c<1\).
The resolvent identity, or multiplication in the affiliated algebra, gives
\[
 T^{-1}-Z^{-1}
 = c\,U^*D^{\alpha-1} S
           (1-cD^{2\alpha-1}U^* S)^{-1} D^{\alpha-1}U^* .
\]
The middle factor \(cS(1-cD^{2\alpha-1}U^*S)^{-1}\) has norm at most \(2c/(1-2c)\).
Set \(P=1-e_r\).
The compression by \(P\) on both sides of the inverse difference has norm at most \(2c\,r^{-2(1-\alpha)}/(1-2c)\).
Subtracting this compression leaves a sum of two operators, one with left and one with right support of trace at most \(r^2\).
Their sum has right support of trace at most \(2r^2\), by polar decomposition and subadditivity of projection dimension.
Thus the inverse difference \(Q=T^{-1}-Z^{-1}\) satisfies \(\tau(1_{(t,\infty)}(|Q|))=O(t^{-1/(1-\alpha)})\) as \(t\to\infty\), by choosing the cutoff \(r\) with compression norm below \(t\).
Indeed on the kernel of the discarded part the norm is at most \(t\), and this kernel intersects the spectral space above \(t\) trivially.

For any two measurable operators, their sum has tail above \(u+v\) bounded by the sum of their respective tails above \(u,v\), by the same projection-dimension argument on the intersection of the two low spectral spaces.
Here \(1/(1-\alpha)>2\), while \(|Z^{-1}|\) has exact tail \(t^{-2}\) for \(t\ge1\).
Applying the tail inequality to \(T^{-1}=Z^{-1}+Q\) and to \(Z^{-1}=T^{-1}-Q\), allowing \(\varepsilon t\) for the error and then letting \(\varepsilon\downarrow0\), gives \(\tau(1_{(t,\infty)}(|T^{-1}|))\sim t^{-2}\).
The same asymptotic holds with a closed left endpoint by squeezing between nearby open cutoffs.
The unitary polar decomposition identifies this tail with the required lower tail of \(|T|\) at reciprocal radius.
The residual is nonnormal by the [normal-residual classification](Yin_C_F0270_v1.md#statement), since \(Z\) is noncollinear and \(Y\) is nonscalar.
Thus the common character and full spread of marginal secants at the origin coexist with finite cubic concentration for this nonnormal residual.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:05 |
| status | open |
| reason | Fix the actual correlated pair, its common planar character and the exact leading coefficient of the nonnormal residual's singular mass for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Conjugate variables and full canonical domains, the common character, simultaneous marginal minimizers and the quadratic asymptotic at one omitted shift. |
| argument | [Argument](#argument) | Exact angular integral, radial conditional second moment, character from approximate eigenvectors, affiliated inverse expansion and spectral tails. |
| dependency | [Gaussian covariance criterion](Yin_C_F0260_v1.md#statement) | Intrinsic actual conjugate variables, both canonical domains and nonzero-amplitude realization for the first-chaos field after its two required integrals are finite. |
| dependency | [Area disk marginal](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Existence of the scalar vacuum for normalized disk area with its coordinate function. |
| dependency | [Normal residual classification](Yin_C_F0270_v1.md#statement) | A noncollinear actual marginal and a nonscalar omitted shift give a nonnormal residual. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:10 |
| status | proved |
| reason | Independent review verifies the disk model, its common character, the normality obstruction and the exact quadratic asymptotic for the residual singular mass. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Conjugate variables and full canonical domains, the common character, simultaneous marginal minimizers and the quadratic asymptotic at one omitted shift. |
| argument | [Argument](#argument) | Exact angular integral, radial conditional second moment, character from approximate eigenvectors, affiliated inverse expansion and spectral tails. |
| dependency | [Gaussian covariance criterion](Yin_C_F0260_v1.md#statement) | Intrinsic actual conjugate variables, both canonical domains and nonzero-amplitude realization for the first-chaos field after its two required integrals are finite. |
| dependency | [Area disk marginal](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Existence of the scalar vacuum for normalized disk area with its coordinate function. |
| dependency | [Normal residual classification](Yin_C_F0270_v1.md#statement) | A noncollinear actual marginal and a nonscalar omitted shift give a nonnormal residual. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0284_v1.md#finding) | Gaussian energy, common marginal cutoffs, all three input interfaces and the tail comparison in the affiliated algebra. |
