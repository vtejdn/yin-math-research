---
author: Yin
---

# A two-valued phase with finite secant energy and divergent far-point rectangle costs

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

There is a bounded normal pair with actual starred conjugate variables in a finite von Neumann algebra with faithful normal probability trace, whose first marginal \(\mu\) is normalized area on the unit disk.
For its real partial liberation vacuum \(\zeta=(i\gamma)^*(1\otimes1)\), let \(\nu\) be the joint spectral measure under the two actions of this marginal.
There is a two-valued real function \(\phi\) such that
\[
 d\nu(z,w)=|\phi(z)-\phi(w)|^2d\mu(z)d\mu(w),\qquad
 J_\phi=\iint_{z\ne w}\frac{|\phi(z)-\phi(w)|^2}{|z-w|^2}\,d\mu(z)d\mu(w)<\infty.
\]
Its image has zero two-dimensional Hausdorff measure.
Nevertheless, in the [positive disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) the following nonnegative integral is infinite even after restriction to \(|a-v|>100r\):
\[
 \int \frac{\nu(E\times F)+\nu(F\times E)}{\mu(E)+\mu(F)}
       \,d\mu(v)\,\frac{dA(a)\,dr}{r^5}\,dl\,du .
                                                                    \tag{1}
\]
Here \(B=B(a,r)\), \(p_v(z)=\operatorname{Im}((z-v)/(\bar z-\bar v))\), \(E=B\cap\{p_v>u\}\), \(F=B\cap\{p_v<l\}\), and \(-1<l<u<1\).
A zero denominator contributes zero.
Consequently the integral of the numerical cost of the [centered two-block estimate](Yin_C_F0326_v1.md#statement) is infinite for every measurable choice of countable endpoint subdivisions of the rectangles, even when both endpoints are subdivided.
The actual column costs at both coordinates and in both orientations are finite.
This obstruction concerns the specified positive representation and numerical estimate.

## Argument

### Secant energy of a striped sign on the disk

For \(n\ge2\) let \(Q_n\) be the axis-parallel square of side \(s_n=2^{-n-5}\) centered at \(2^{-n}\) on the real axis.
The squares are disjoint and contained in the disk of radius \(1/2\).
Set \(K_n=\lceil\exp(2^n)\rceil\) and \(\delta_n=s_n/(2K_n)\).
On the \(2K_n\) successive vertical strips of width \(\delta_n\) in \(Q_n\), let \(h\) alternate between \(1\) and \(-1\), and set \(h=1\) outside these squares.
Boundaries can be assigned either value.

Write \(S_n\) for the union of negative strips in \(Q_n\).
Translation by \(y\in\mathbb C\) gives
\[
        |(S_n+y)\mathbin{\triangle}S_n|
          \le C\min\{s_n^2,K_n s_n |y|\},
\]
with planar area on the left.
Indeed the symmetric difference of a translated rectangle is at most the displacement times twice the sum of its side lengths, and it is also at most twice its area.
Sum over the strips for the first bound.
Since the \(S_n\) are disjoint, the squared difference of \(h\) at any two points is at most four times the sum of the squared differences of their indicators.
Using the translation bound and planar polar coordinates, the contribution of \(S_n\) to \(J_h\) is bounded by a constant times
\[
 \int_0^2 \min\{s_n^2,K_n s_n t\}\,\frac{dt}{t}
        \le C s_n^2(1+\log(2/\delta_n)).
\]
The sum is finite since \(\log(1/\delta_n)=2^n+O(n)\).

Take \(Z\) with law \(\mu\) and a unitary \(V\) free from it with Poisson law of parameter \(1/2\).
Both scalar vacua exist.
For the disk the bounded density and the uniform integral of \(|z-w|^{-1}\) give the vacuum by symmetrizing the divided-difference pairing.
For the smooth circle law the maximal linear density is bounded and its squared curvature integral is finite, so the [scalar criterion](Yin_C_F0255_v1.md#statement) applies.
The [phase criterion](Yin_C_F0265_v1.md#statement) now gives actuality and strong domains for \((Z,h(Z)^*V)\), with finite column costs in both orientations.
For \(H=\xi_VV^*-1\) one has \(\|H\|_2^2=8/9\) by its Poisson norm formula.
The [phase gradient calculation](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) gives the required spectral measure with \(\phi=\|H\|_2 h\), since the phase factor relating the real and skew liberation vacua preserves the spectral measure.

### A far third point separates two mixed-sign caps

Let \(a\) lie in the concentric half-side square of \(Q_n\), and restrict \(1000\delta_n\le r\le s_n/8\).
For all sufficiently large \(n\) this interval is nonempty, and \(B(a,r)\subset Q_n\).
Take \(v=a+R e^{i\theta}\) with \(100r<R<1/8\) and \(|\theta|<1/20\), so this whole sector is inside the unit disk.
On \(B(a,r)\), the function \(p_v(z)=\sin(2\arg(z-v))\) has \(|\nabla p_v|\le3/R\) and \(\partial_{\operatorname{Im}z}p_v\le-1/R\).
For the latter inequality use \(2\cos(2\arg(z-v))\operatorname{Re}(z-v)/|z-v|^2\) and \(r<R/100\).
Thus the values at \(a-ir/2\) and \(a+ir/2\) differ by at least \(r/R\), with the lower point having the larger value.
Over the disks of radius \(r/20\) about these points the two value ranges remain separated by at least \(7r/(10R)\).
There is hence a triangle of threshold pairs of area at least \(c(r/R)^2\) for which \(E\) contains the entire lower disk and \(F\) the entire upper disk.

Each such disk contains an axis-parallel square of side \(r/20\).
Its horizontal cross-section contains complete periods of width \(2\delta_n\) occupying at least half the cross-section, by \(r\ge1000\delta_n\).
Both signs therefore have mass at least \(c r^2\) in each disk.
It follows that \(\nu(E\times F)\ge c r^4\), whereas \(\mu(E)+\mu(F)\le r^2\).
On the selected parameters the quotient in (1) is at least \(c r^2\).
Integration in the thresholds and then in the third point, using \(d\mu(v)=\pi^{-1}R\,dR\,d\theta\), gives a lower bound \(c r^4\log(1/(800r))\).
The available centers for distinct \(n\) are disjoint, each with area \(s_n^2/4\).
After integration in \(a,r\) the resulting lower bound is
\[
    c\sum_{n\ {\rm large}} s_n^2
       \int_{1000\delta_n}^{s_n/8}\log(1/(800r))\,\frac{dr}{r}
       =\infty .
\]
Indeed the integral is half the difference of the squared logarithms at its endpoints and is at least \(c4^n\) for all sufficiently large \(n\).
The secant energy instead paid only one logarithm per square.

### Subdivision and the scope of the obstruction

For disjoint sets \(E_i,F_j\) of positive marginal masses \(t_i,s_j\), expansion of the squared centered term in the block estimate gives the cross contribution
\[
            \frac{\nu(E_i\times F_j)+\nu(F_j\times E_i)}{t_i+s_j}.
\]
All other contributions to that numerical cost are nonnegative.
If \(E_i,F_j\) partition \(E,F\) up to marginal null sets, then \(t_i+s_j\le\mu(E)+\mu(F)\), and summation gives at least the quotient in (1).
The same argument applies to a disjoint refinement by subrectangles contained in \(E\times F\) that cover it up to marginal product-null sets.
Absolute continuity of \(\nu\) justifies omission of these null sets.
This pointwise lower bound uses no measurability of an optimizing dissection.

On the same example the [localized bounded-kernel estimate](Yin_C_F0297_v1.md#a-localized-kernel-in-the-liberation-energy) on \(B^2\) has cost \(O(\mu(B)^{3/2}+\mu(B)^2)\), since \(\nu(B^2)\le4\|H\|_2^2\mu(B)^2\).
For \(r<1/4\) this is \(O(r^3)\).
The area of levels with both endpoint sets nonempty is \(O(\min(1,r^2/|a-v|^2))\) by angular oscillation in the disk.
Its \(\mu(v)\) integral is \(O(r^2(1+\log(1/r)))\), uniformly over centers within distance \(r\) of the marginal support.
Their area is bounded.
This alternative cost thus has finite small-radius integral since \(\int_0^{1/4}(1+\log(1/r))\,dr<\infty\).
For larger radii the costs and threshold area are bounded and the area of the allowed centers is \(O((1+r)^2)\), giving finite integral against \(dr/r^5\).
The example leaves open whether signed estimates combining different types of localized bounds suffice for arbitrary actual scalar marginals.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:54 |
| status | open |
| reason | Fix a single actual area-law example separating finite two-valued phase energy from every centered endpoint-subdivision cost on the far third points. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite secant energy, exact two-valued spectral density and divergent centered costs after endpoint subdivision in the far portion. |
| argument | [Argument](#argument) | Striped patches, translation estimates, angular separation of two caps, logarithmic radial integral and exact cross-term lower bound. |
| dependency | [Disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | The positive angular thresholds and planar center/radius integration. |
| dependency | [Centered block estimate](Yin_C_F0326_v1.md#statement) | The signed rectangular cost whose expansion gives the nonnegative cross contribution. |
| dependency | [Scalar criterion](Yin_C_F0255_v1.md#statement) | Existence of the actual scalar vacuum for the smooth Poisson law on the circle. |
| dependency | [Phase criterion](Yin_C_F0265_v1.md#statement) | Actuality of the constructed normal pair, finite true columns and the Poisson angular vacuum norm. |
| dependency | [Phase spectral measure](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Equality of the real liberation spectral density with a squared difference of the chosen two-valued function. |
| dependency | [Localized kernel](Yin_C_F0297_v1.md#a-localized-kernel-in-the-liberation-energy) | Finite integral of the alternative localized numerical cost on this specific area law. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:06 |
| status | proved |
| reason | R_F0339 checked the two-valued actual phase construction, finite secant energy, all endpoint subdivisions and the divergent far-point integral, together with all six declared dependency interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite secant energy, exact two-valued spectral density and divergent centered costs after endpoint subdivision in the far portion. |
| argument | [Argument](#argument) | Striped patches, translation estimates, angular separation of two caps, logarithmic radial integral and exact cross-term lower bound. |
| dependency | [Disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | The positive angular thresholds and planar center/radius integration. |
| dependency | [Centered block estimate](Yin_C_F0326_v1.md#statement) | The signed rectangular cost whose expansion gives the nonnegative cross contribution. |
| dependency | [Scalar criterion](Yin_C_F0255_v1.md#statement) | Existence of the actual scalar vacuum for the smooth Poisson law on the circle. |
| dependency | [Phase criterion](Yin_C_F0265_v1.md#statement) | Actuality of the constructed normal pair, finite true columns and the Poisson angular vacuum norm. |
| dependency | [Phase spectral measure](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Equality of the real liberation spectral density with a squared difference of the chosen two-valued function. |
| dependency | [Localized kernel](Yin_C_F0297_v1.md#a-localized-kernel-in-the-liberation-energy) | Finite integral of the alternative localized numerical cost on this specific area law. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0339_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
