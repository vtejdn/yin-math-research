---
author: Yin
---

# Singular backgrounds and explicit finite-degree tests for a conditional vacuum

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Use the [ordered two-block functional](Yin_C_F0239_v1.md#statement) for normal \(X,Y\), with the \(X\)-derivative tested on finite sums of \(g(Y)h(X)\).
Write \(\gamma(dy,ds)\) for their spectral coupling and \(\mu\) for the diffuse spectral law of \(X\).

1. For every \(0<\alpha<1\) and \(0<\lambda<1\) there is a symmetric coupling of two copies of uniform area probability on the unit disk, of the form
   \[
      \gamma=\lambda\,\mathrm{diag}_*\mu+
                      (1-\lambda)p(y,s)\,d\mu(y)d\mu(s),                 \tag{1}
   \]
   with a doubly stochastic density \(p\) comparable to \(|y-s|^{-\alpha}\) off the diagonal.
   Both ordered two-block vacuum functionals, distinguished at either coordinate, are bounded.
   The commuting realization fails the represented vacuum identity already on an explicit degree-three relation.
   There is also a noncommuting bounded normal realization of a coupling of this form, with nonzero diagonal mass and with both two-block functionals bounded.
   No full mixed-word vacuum conclusion is asserted for this second realization.
2. Suppose \(\mu\) is supported in a disk of radius \(R>0\) about zero and has a scalar actual vacuum \(\zeta\).
   For the coupling \(\gamma_\lambda=\lambda\,\mathrm{diag}_*\mu+(1-\lambda)\mu^2\), \(0<\lambda<1\), define
   \[
       L=4R^2,\qquad q_n(d)=\frac{1-(1-|d|^2/L)^n}{|d|^2},\qquad
       F_n(y,z)=(z-y)q_n(z-y),\qquad
       A_n=\iint q_n(z-y)\,d\mu(y)d\mu(z)                                \tag{2}
   \]
   for integers \(n\ge1\), with \(q_n(0)=n/L\).
   Interpret \(F_n\) as an ordered two-block polynomial by expanding in separated monomials.
   Its total degree is \(2n-1\).
   The two-block functional \(\mathcal L\) satisfies
   \[
     \frac{|\mathcal L(F_n)|}{\|F_n\|_{L^2(\gamma_\lambda)}}
          \ge \frac{\lambda}{\sqrt{1-\lambda}}\sqrt{A_n}
                        -\sqrt{1-\lambda}\,\|\zeta\|_2,\qquad
     A_n\ge \frac{1-e^{-1}}{16R^2}\log(n/4)\quad(n\ge4).                \tag{3}
   \]
   These are fixed finite-degree tests growing at least at order \(\sqrt{\log n}\) as \(n\to\infty\).
   For any sequence of normal actual pairs on a common cutoff whose joint star moments converge to a realization of this target coupling and marginal, the vacuum norm at \(X\) tends to infinity, as witnessed by these same tests with the degree fixed before passing to the moment limit.
   The target includes the [free-unitary conjugation coupling](Yin_C_F0239_v1.md#a-conjugated-copy-of-a-normal-marginal) with \(\lambda=|\tau(w)|^2\).

## Argument

### A stochastic kernel with a power singularity

Let \(\mu\) be normalized Lebesgue area on the closed unit disk, and put \(K(y,z)=|y-z|^{-\alpha}\) off the null diagonal.
Define \(q(y)=\int K(y,z)\,d\mu(z)\), and \(Q=\int q\,d\mu\).
The near-diagonal integral is bounded uniformly because the disk is inside the radius-two disk about each of its points and \(\alpha<2\).
Choose \(c>0\) with \(c\|q\|_\infty<1/2\), and set
\[
        p(y,z)=cK(y,z)+\frac{(1-cq(y))(1-cq(z))}{1-cQ}.
\]
This kernel is positive and symmetric, and its row integral equals \(cq(y)+1-cq(y)=1\).
Its column integral also equals one.
Since \(K\ge2^{-\alpha}\), the second bounded term proves the claimed upper and lower comparisons with \(K\).

For a positive measure \(\sigma\) on the disk, denote by \(G_\sigma(z)=\int(z-s)^{-1}d\sigma(s)\) its Cauchy integral wherever absolutely convergent.
For the present kernel, \(G_\mu(z)\) and \(G_{p_y\mu}(z)\), with \(p_y(s)=p(y,s)\), are bounded in absolute value uniformly in \(y,z\), even after replacing the complex kernel by its absolute value.
For the only additional term one needs
\[
         \sup_{y,z}\int |z-s|^{-1}|y-s|^{-\alpha}\,d\mu(s)<\infty .
\]
On the region \(|z-s|\le |y-s|\) the integrand is bounded by \(|z-s|^{-1-\alpha}\); on its complement use \(|y-s|^{-1-\alpha}\).
Polar integration is uniform since \(1+\alpha<2\).

For \(\nu_y=\lambda\delta_y+(1-\lambda)p_y\mu\), an explicit representative of the two-block functional in the convention \(\int h\overline{H(y,\cdot)}\,d\nu_y\) is given by
\[
 \begin{split}
  \overline{H(y,y)}&=G_\mu(y),\\
  \overline{H(y,z)}&=G_\mu(z)+
       \frac{\lambda/(z-y)+(1-\lambda)G_{p_y\mu}(z)}
                         {(1-\lambda)p_y(z)}\qquad(z\ne y).
                                                                            \tag{4}
 \end{split}
\]
Indeed split \((h(s)-h(z))/(s-z)\) into its two signed terms in the conditional integral (1) of C_F0239.
The first gives \(G_\mu(s)\) on both components of \(\nu_y\), and the second gives \(G_{\nu_y}(z)\,d\mu(z)\), with the displayed positive sign after reversing \(s-z\).
The preceding absolute estimates justify both splittings for bounded \(h\).
The singular correction has uniformly finite conditional squared norm because
\[
      \int\frac{d\mu(z)}{p_y(z)|z-y|^2}
           \le c^{-1}\int |z-y|^{\alpha-2}\,d\mu(z)<\infty
\]
uniformly in \(y\).
The remaining correction is square integrable because \(p_y\ge c2^{-\alpha}\).
Thus (4) lies in \(L^2(\gamma)\); symmetry gives the same result with the coordinates reversed.
The same proof applies to a mixture of \(p\) with a constant positive density, provided its \(p\)-coefficient is positive.

### Commuting and noncommuting realizations

In the abelian tracial algebra \(A=L^\infty(\gamma)\) take \(D(y,z)=y\) and \(X(y,z)=z\).
The represented word \(D^*[D,X]\) vanishes.
Formal differentiation with \(\delta_X X=1\otimes1\), \(\delta_X D=\delta_X D^*=0\) gives double trace \(\tau(D^*D)-|\tau(D)|^2=1/2\).
The vanishing omitted starred value is forced by [the normal marginal phase](Yin_C_F0076_v1.md#statement) under actual ACSY.
Thus the third block in \(D^*XD\) detects failure despite both ordered two-block bounds.

For the second realization, adjoin in the tracial free product a centered selfadjoint unitary \(v\) with \(v^2=1\).
Choose \(0<\theta<\pi/2\), \(w=\cos\theta+i\sin\theta\,v\), \(Y=wDw^*\) and \(b=\cos^2\theta\).
The free centered expansion gives
\[
    \tau(g(Y)h(X))=b\,\tau(g(D)h(X))+(1-b)\tau(g(D))\tau(h(X)).
\]
This follows by separating the scalar and centered parts of \(w,w^*\), with the same contraction as in the [conjugated-copy calculation](Yin_C_F0239_v1.md#a-conjugated-copy-of-a-normal-marginal) for any two bounded functions in the old algebra.
Thus the new coupling has diagonal weight \(b\lambda\), with remaining density
\[
             \frac{b(1-\lambda)p+1-b}{1-b\lambda}
\]
against \(\mu^2\) after normalization.
Formula (4) and its bounds apply.
The pair genuinely fails to commute.
In the [centered free-product word decomposition](../audits/literature/Voi98/Yin_U005.md#voi98-u005), the length-four component of \([X,Y]\) equals
\[
              \sin^2\theta\,(XvDv-vDvX).
\]
Both \(X,D\) are centered and nonzero.
The two displayed words are nonzero reduced tensors with different initial factors and hence orthogonal.
All other summands of the commutator have length at most three.
For any prescribed diagonal weight \(0<\lambda'<1\) one can choose \(b\in(\lambda',1)\) and the initial \(\lambda=\lambda'/b\), so the construction also realizes the prescribed weight noncommutatively.

### The degree tests and the critical scale

From (2), \(q_n=L^{-1}\sum_{j=0}^{n-1}(1-|d|^2/L)^j\).
Hence \(F_n\) is a polynomial, vanishes on the diagonal and obeys \(|d|^2 q_n(d)^2\le q_n(d)\) on the difference disk, since \(0\le |d|^2q_n(d)\le1\).
Its squared norm in the target is consequently at most \((1-\lambda)A_n\) and is positive by diffuseness.
In the atomic part of the functional, \(F_n(y,y)=0\), so division of its difference by \(y-z\) gives \(q_n(z-y)\) with a positive sign.
The contribution of the product part is the scalar marginal vacuum functional on \(F_n(y,\cdot)\), integrated against \(\mu(dy)\), before multiplication by \(1-\lambda\).
Its absolute value before that multiplication is bounded by \(\|\zeta\|_2\|F_n\|_{L^2(\mu^2)}\) by Cauchy–Schwarz.
The triangle inequality and \(\|F_n\|_{L^2(\gamma_\lambda)}=\sqrt{1-\lambda}\|F_n\|_{L^2(\mu^2)}\) give (3)'s first inequality.

For \(0\le |d|\le 2R\), \(q_n(d)\ge(1-e^{-1})\min(n/L,|d|^{-2})\), using \((1-u)^n\le e^{-nu}\) and the chord lower bound on \(1-e^{-x}\) on \([0,1]\).
For \(0<t\le R\) partition the square of side \(2R\) containing the support into at most \((4R/t)^2\) cells of diameter at most \(t\), using \(\lceil2\sqrt2R/t\rceil\) subdivisions on each axis.
Cauchy–Schwarz for their masses gives \(\mu^2\{|y-z|\le t\}\ge t^2/(16R^2)\).
This is the finite-scale grid argument of the [critical planar energy proof](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation).
For \(n\ge4\), integration of this bound against \(2t^{-3}dt\) over \([2R/\sqrt n,R]\) gives at most the integral of \(\min(n/L,|d|^{-2})\), by the layer formula, and at least \(\log(n/4)/(16R^2)\).
Multiplying by \(1-e^{-1}\) gives the stated bound for \(A_n\).

For convergence on a common cutoff, the ordered two-point couplings and both marginal measures converge weakly by convergence of separated star-polynomial integrals, polynomial density and compactness.
For fixed \(n\) the norm of \(F_n\) converges by its polynomial symbol.
The numerator from (1) of C_F0239 is the integral of the bounded difference \((F_n(y,s)-F_n(y,z))/(s-z)\) against the product of the coupling on \((y,s)\) and the distinguished marginal on \(z\).
The product measures converge weakly, and the only possible discontinuities are on \(s=z\).
That set is null in the limiting product because \(z\) is an independent diffuse marginal sample, even though \(y=s\) has positive coupling mass.
A continuous cutoff of a shrinking diagonal neighborhood therefore gives convergence of these integrals.
For every fixed \(n\) the actual vacuum norm bounds the observed quotient by C_F0239.
Letting \(n\) grow after this fixed-degree limit proves divergence at the distinguished coordinate.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:17 |
| status | open |
| reason | The singular-background scores, the commuting and noncommuting realizations and the explicit quantitative test words are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two bounded ordered tests with positive diagonal mass, commuting third-block failure and noncommuting realization, finite-degree quantitative tests and persistence under moment limits. |
| argument | [Argument](#argument) | Construction and normalization of a symmetric stochastic kernel, absolute Cauchy bounds, reduced-word verification, polynomial regularization of the critical energy and fixed-degree moment continuity. |
| dependency | [Ordered conditional vacuum test](Yin_C_F0239_v1.md#statement) | The ordered two-block isometry, the functional and its conditional Riesz representatives, and the norm lower bound on any actual distinguished vacuum. |
| dependency | [Free conjugation coupling](Yin_C_F0239_v1.md#a-conjugated-copy-of-a-normal-marginal) | Centered free-product expansion for the coupling after a free unitary conjugation, directly specialized to two functions in the previous abelian algebra, and the pure-product-background target. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Part 1, zero derivative on the omitted starred coordinate under actual ACSY in the commuting realization. |
| dependency | [Free-product Hilbert representation](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Sections 5.5–5.8, orthogonality and tensor norms of centered reduced words with different factor patterns. |
| dependency | [Critical planar energy grid](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Cauchy–Schwarz for planar cell masses and the truncated layer integral, with the explicit cutoff and constants computed here. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:25 |
| status | proved |
| reason | Adopt the singular disk coupling and finite-degree obstruction after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two bounded ordered tests with positive diagonal mass, commuting third-block failure and noncommuting realization, finite-degree quantitative tests and persistence under moment limits. |
| argument | [Argument](#argument) | Construction and normalization of a symmetric stochastic kernel, absolute Cauchy bounds, reduced-word verification, polynomial regularization of the critical energy and fixed-degree moment continuity. |
| dependency | [Ordered conditional vacuum test](Yin_C_F0239_v1.md#statement) | The ordered two-block isometry, the functional and its conditional Riesz representatives, and the norm lower bound on any actual distinguished vacuum. |
| dependency | [Free conjugation coupling](Yin_C_F0239_v1.md#a-conjugated-copy-of-a-normal-marginal) | Centered free-product expansion for the coupling after a free unitary conjugation, directly specialized to two functions in the previous abelian algebra, and the pure-product-background target. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Part 1, zero derivative on the omitted starred coordinate under actual ACSY in the commuting realization. |
| dependency | [Free-product Hilbert representation](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Sections 5.5–5.8, orthogonality and tensor norms of centered reduced words with different factor patterns. |
| dependency | [Critical planar energy grid](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Cauchy–Schwarz for planar cell masses and the truncated layer integral, with the explicit cutoff and constants computed here. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0249_v1.md#whole-proof-finding) | Both realizations, the degree-three relation in the commuting realization, explicit finite-order lower bounds and the fixed-degree moment limit. |
