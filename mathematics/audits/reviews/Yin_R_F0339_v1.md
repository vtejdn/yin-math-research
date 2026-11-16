---
author: Yin
---

# Review of far-point rectangle costs for a striped disk phase

## Finding

At 2026-11-16T18:58 UTC a separately assigned agent for Yin independently reviewed the complete C_F0333 v1 candidate fixed at 18:54 UTC.
The reviewer took no part in developing this candidate and received its fixed proof and dependency locators without development dialogue, author explanations or prior findings on it.
The striped phase has finite secant energy, yet the far-point integral (1) diverges and gives the same obstruction after subdivision of either or both endpoint sets.

Translating a strip of height \(s_n\) and width \(\delta_n\) changes its indicator on area at most \(2(s_n+\delta_n)|y|\).
Summing over its \(K_n\) negative strips and also using twice their area gives the claimed minimum.
Whenever the signs differ, some patch indicator differs, so summing these bounds after the substitution \(w=z+y\) gives an upper bound for the disk secant integral even at the disk boundary.
The radial weight is \(dt/t\).
Splitting at \(s_n/K_n=2\delta_n\) gives cost \(O(s_n^2(1+\log(2/\delta_n)))\), summable since \(\log(1/\delta_n)=2^n+O(n)\) and \(s_n^2=2^{-2n-10}\).
The disk vacuum follows by antisymmetrizing its uniformly absolutely integrable first inverse-distance kernel against a bounded polynomial test.
The Poisson circle law at \(r=1/2\) has bounded maximal linear density and unit squared Menger curvature on distinct triples.
Thus it too admits the scalar vacuum required for C_F0265.
With the finite secant energy this gives the two actual coordinates and the finite original column costs in both orientations.
The angular vacuum norm squared is \(2r^2/(1-r^2)^2=8/9\), so the phase spectral identity gives exactly the stated density with two distinct real phase values.

For \(a\) in the half-side square and \(r\le s_n/8\), the test disk stays inside \(Q_n\).
The indicated angular sector of \(v=a+Re^{i\theta}\) stays in the unit disk.
At \(z\in B(a,r)\), the condition \(r<R/100\) confines \(\arg(z-v)\) near \(\pi+\theta\).
Differentiating the imaginary phase gives \(\partial_{\operatorname{Im}z}p_v=2\cos(2\arg(z-v))\operatorname{Re}(z-v)/|z-v|^2\le-1/R\) and \(|\nabla p_v|\le3/R\).
The vertical basepoint separation \(r\) thus gives a phase difference at least \(r/R\).
Each cap radius \(r/20\) removes at most \(3r/(20R)\) from this difference, leaving a gap \(7r/(10R)\) between the whole cap ranges.
The admissible thresholds in this gap have area at least \(c(r/R)^2\).
A horizontal interval of length \(r/20\) loses at most \(4\delta_n\) on discarding incomplete periods at its ends.
At \(r\ge1000\delta_n\) each cap therefore contains mass \(\gtrsim r^2\) of each sign.
The cross spectral mass is \(\gtrsim r^4\) and the denominator is at most \(r^2\), as required.

The threshold integral and normalized area element \(R\,dR\,d\theta/\pi\) contribute a lower bound \(c r^4\log(1/(800r))\) after integrating \(100r<R<1/8\).
On the large-\(n\) windows the logarithm is positive.
Multiplying by the center area \(s_n^2/4\) and integrating in \(dr/r^5\) gives a difference of squared logarithms times \(c s_n^2\).
The squared logarithm at \(1000\delta_n\) is asymptotic to \(4^n\), whereas at \(s_n/8\) it is \(O(n^2)\).
The disjoint center ranges thus contribute a divergent sum even with the stipulated far-point restriction.

In a subdivided rectangle, the coefficient of the cross spectral mass in the centered bound is exactly \(1/(t_i+s_j)\).
This follows by multiplying the cross multiplier square \(1/(t_i^2s_j^2)\) by \(t_i s_j/(1/t_i+1/s_j)\).
All other cost terms are nonnegative and all refined denominators are at most \(\mu(E)+\mu(F)\).
Countable additivity and \(\nu\ll\mu^2\) give the asserted pointwise lower bound before integration, including disjoint product-null-complete coverings by subrectangles.
For the localized alternative the spectral inequality gives compressed gradient norm \(O(\mu(B))\), so the localized numerical estimate is \(O(r^3)\) at small radii.
The third-point integral of the nonempty threshold area is \(O(r^2(1+\log(1/r)))\) by planar area integration of \(\min(1,r^2/|a-v|^2)\).
These factors cancel the \(r^{-5}\) power to leave an integrable logarithm, and at large radii the center area is \(O((1+r)^2)\).
The review checked all six declared dependency interfaces at their stated uses.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0333_v1.md#decision-candidate) | Fixed 18:54 UTC candidate, its far portion, subdivision scope and actual pair. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0333_v1.md#statement) | Two-valued spectral density, finite secant energy and actual column costs, infinite far integral and obstruction under measurable endpoint subdivisions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0333_v1.md#argument) | Complete translation estimate, phase realization, angular derivative bounds on the caps, squared-logarithm divergence, subdivision and localized alternative. |
| [Finding](#finding) | [Disk representation](../../claims/Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Disk, angular thresholds, center measure and radial exponent in the positive representation. |
| [Finding](#finding) | [Centered rectangular estimate](../../claims/Yin_C_F0326_v1.md#statement) | Nonnegative numerical terms and the exact cross coefficient after expanding the centered kernel. |
| [Finding](#finding) | [Scalar actuality](../../claims/Yin_C_F0255_v1.md#statement) | Actual Poisson scalar vacuum from maximal linear density and finite squared curvature. |
| [Finding](#finding) | [Phase criterion](../../claims/Yin_C_F0265_v1.md#statement) | Full actuality and strong domains of the realized product pair, both original column bounds and the numerical Poisson vacuum norm. |
| [Finding](#finding) | [Explicit liberation measure](../../claims/Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Product density with the exact angular factor and squared sign difference on the disk. |
| [Finding](#finding) | [Localized kernel bound](../../claims/Yin_C_F0297_v1.md#a-localized-kernel-in-the-liberation-energy) | Finite localized total cost under bounded disk area density and bounded product spectral density. |
