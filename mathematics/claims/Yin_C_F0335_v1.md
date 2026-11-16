---
author: Yin
---

# Rank-one bounds from the spectral rows of an actual liberation gradient

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be a distinguished coordinate of a bounded normal tuple with actual starred conjugate variables in a finite von Neumann algebra with faithful tracial probability.
Use its marginal law \(\mu\), \(A=W^*(Z)\), joint and marginal conjugate variables \(\xi,\xi_\mu\), and the real liberation vacuum \(\zeta=(i\gamma)^*(1\otimes1)\).
Write \(\nu\) for the joint left-right \(Z\)-spectral measure of \(\zeta\).
The [liberation criterion](Yin_C_F0238_v1.md#statement) and [marginal adjoint formula](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) give a diffuse \(\mu\), a symmetric density \(h=d\nu/d\mu^2\), and finite energy
\[
      I=\iint_{z\ne w}|z-w|^{-2}d\nu(z,w)
        =\|\xi\|_2^2-\|\xi_\mu\|_2^2 .
\]
For a bounded real symmetric kernel \(q\) and an analytic test \(u=b\pm i\sqrt{1-b^2}\) with \(b\) a strict selfadjoint contraction of the original starred polynomial algebra, put \(F_q(u)=\operatorname{Re}\langle u,(\mathrm{id}\otimes\tau)I_q\gamma(u)\rangle\), with inner insertion.
There is a single \(\mu\)-conull set of \(v\) such that every such \(u\) and every bounded real Borel function \(k\) satisfy
\[
         F_{k\otimes k}(u)\le\left(\int k\,d\mu\right)^2+
                             2\int |k(z)|^2 h(z,v)d\mu(z).               \tag{1}
\]
For each fixed \(u\) the real symmetric kernel representing \(F\) on \(L^2(\mu)\) defines a trace-class operator \(T_u\).
In particular when \(h\le m^2\), one has \(T_u\le P_1+2m^2\,\mathrm{Id}\), uniformly in all tests, where \(P_1\) projects onto constants.
The stronger \(T_u\le P_1\) for every test is equivalent to \(\zeta=0\).

For \(\epsilon>0\) put \(c_{\epsilon,v}(z)=\overline{z-v}/(|z-v|^2+\epsilon^2)\).
Its real Gram kernel
\[
 K_\epsilon(z,w)=\operatorname{Re}\int c_{\epsilon,v}(z)
                              \overline{c_{\epsilon,v}(w)}\,d\mu(v)
\]
obeys the unilateral estimate on the whole test class
\[
                    F_{K_\epsilon}(u)\le \|\xi_\mu\|_2^2+2I.             \tag{2}
\]
Consequently a uniform lower bound for \(F_{g+K_\epsilon}(u)\) at any one \(\epsilon>0\), or along \(\epsilon\downarrow0\), implies both original canonical domain inclusions at this coordinate, with the loss in (2).
Here \(F_g\) is the matched squared Menger curvature form and \(F_{g+K_\epsilon}=F_g+F_{K_\epsilon}\).
More explicitly, it suffices that for some \(\epsilon_n\downarrow0\) there are finite sums \(q_n=\sum_i b_{ni}1_{B_{ni}}^{\otimes2}\) with \(b_{ni}\ge0,\ \mu(B_{ni})>0\), satisfying
\[
 \sup_n\sum_i b_{ni}\,\nu(B_{ni}^2)/\mu(B_{ni})<\infty,\qquad
 (z-w)(q_n-K_{\epsilon_n}-g)\longrightarrow0\quad\text{in }L^2(\mu^2).
\]

There is an additional endpoint conclusion for \(D_+=\{v:\liminf_{r\downarrow0}\mu(B(v,r))/r>0\}\).
For every Borel \(E\subset D_+\),
\[
  \inf_{E=\bigsqcup_i E_i\ \mathrm{mod}\ \mu}
                \sum_i\frac{\nu(E_i^2)}{\mu(E_i)^2}=0,                   \tag{3}
\]
using countable Borel partitions with positive cell masses.
The diagonal of the trace-class kernel described below satisfies \(0\le T_u(v,v)\le1\) for \(\mu\)-almost every \(v\in D_+\), for each \(u\).
These results do not decide the general normal implication.

## Argument

### Shrinking spectral balls

Put \(\sigma=1_{\{z\ne w\}}|z-w|^{-2}\nu\).
This finite measure is absolutely continuous with respect to \(\mu^2\) and gives zero mass to the diagonal.
For \(\mu\)-almost every \(v\), write \(R=B(v,r)\) and \(m_R=\mu(R)>0\).
Then
\[
 \frac{\sigma(R^2)}{m_R}\longrightarrow0,\qquad
 \limsup_{r\downarrow0}\frac{r^2}{m_R}<\infty,\qquad
 d_R:=\frac{\nu(R^2)}{m_R^2}\longrightarrow0 .                          \tag{4}
\]
For the first limit restrict \(\sigma\) to \(\{|z-w|\le1/n\}\) and project to the first marginal.
The resulting measures decrease to zero and have \(\mu\)-densities decreasing to zero almost everywhere.
For fixed \(n\) the quotient in the first limit is bounded, when \(2r<1/n\), by the ball average of that density.
Apply the differentiation theorem for finite Borel measures in the plane and then let \(n\) increase.
The second estimate follows by differentiating planar area with respect to \(\mu\) on a bounded neighborhood of the support, including its singular part by the differentiation theorem for ratios.
Finally \(\nu(R^2)\le4r^2\sigma(R^2)\) proves the last assertion.

For each fixed \(u\), \(\gamma(u)\) admits an expansion \(\sum_j L_j\otimes R_j\) with \(\sum_j\|L_j\|\|R_j\|<\infty\).
Indeed \(\gamma(b)\) is a finite sum of bounded simple tensors and the \(n\)th power has projective tensor norm for its derivative at most \(n\|b\|^{n-1}\|\gamma b\|_\pi\).
The binomial series for the square root converges in this seminorm.
For a simple test kernel the two scalar factors in its pairing are the integrals against \(\mathbb E_A(u^*L_j)\) and \(\mathbb E_A(R_j)\).
Taking the real symmetric part gives a sum of bounded separated real products with summable products of sup norms, representing \(F_q(u)\) for every bounded real symmetric \(q\).
It defines \(T_u\) by an absolutely convergent sum in trace norm.
In particular bounded pointwise convergence almost everywhere of the factors in \(k\otimes k\) suffices to pass to \(F_{k\otimes k}(u)\).
For a fixed \(u\), the diagonal meant in the statement is the sum of these products at \((v,v)\).
Almost everywhere it equals \(\lim_{r\downarrow0}F_{1_R\otimes1_R}(u)/m_R^2\), by differentiation of the countably many factors and uniform absolute summability.
This characterization also ensures independence of the chosen expansion.

### Averaging two rank-one estimates

The [uncentered square bound](Yin_C_F0331_v1.md#the-uncentered-square) and the [projection square identity](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) give
\[
 F_{l\otimes l}(u)\le(\tau l)^2+
       \frac{\iint l(z)^2l(w)^2\,d\nu(z,w)}{\|l\|_2^2},\qquad
 F_{1_R\otimes1_R}(u)\ge-\nu(R^2)/m_R                                  \tag{5}
\]
for any nonzero bounded real marginal \(l\) and any positive-mass spectral set \(R\).
These graph estimates include bounded Borel marginal tests.
Symmetry of \(\nu\) follows from \(\zeta=\zeta^*\), by taking adjoints of corner products.

Take \(l_\pm=k\pm L1_R\), with \(L=\sqrt{\Lambda/m_R}\), choosing \(\Lambda\to\infty\) sufficiently slowly that \(\Lambda(m_R+d_R)\to0\), possible by (4) and diffuseness.
The smaller squared denominator in (5) is \(\Lambda(1+o(1))\) since \(|L\tau(k1_R)|\le\|k\|_\infty\sqrt{\Lambda m_R}\).
Average the two inequalities, and bound both inverse denominators by the inverse of the smaller one, since their numerators are nonnegative.
The left side averages to \(F_{k\otimes k}(u)+L^2F_{1_R\otimes1_R}(u)\).
Removing the second summand from the left costs at most \(\Lambda d_R\).
The mean-square trace term on the right tends to \((\tau k)^2\).
In the mean of the numerators the term with no \(L\) is bounded independently of \(R\), and the fourth-power term divided by \(\Lambda\) equals \(\Lambda d_R\).
Of the three terms with \(L^2\), the one involving both indicators and \(4k(z)k(w)\), divided by \(\Lambda\), has absolute value at most \(4\|k\|_\infty^2\nu(R^2)/m_R\).
The other two divided by \(\Lambda\) equal
\[
                 \frac{2}{m_R}\int_R\int k(z)^2h(z,w)d\mu(z)d\mu(w).
\]
At its differentiation points this converges to the second term of (1).
All these choices are independent of \(u\).

To obtain one conull set of \(v\), differentiate first for a countable rational algebra of bounded step functions based on a countable generating family of planar Borel sets.
Also require \(\int h(z,v)d\mu(z)<\infty\) there.
Every bounded real Borel \(k\) has uniformly bounded approximants in this algebra converging \(\mu\)-almost everywhere, for example from increasing finite partitions and rational rounding.
They also converge almost everywhere for \(h(z,v)d\mu(z)\).
The separated representation above and dominated convergence on the right extend (1) to every \(k\) at each such \(v\).
If \(h\le m^2\), continuity extends its uniform operator bound to \(L^2(\mu)\).

If \(\zeta=0\), (1) gives \(T_u\le P_1\).
Conversely choose a Borel sign \(a\in A\) with trace zero, possible by diffuseness.
For \(\zeta\ne0\), \(a\zeta a\) is a nonzero selfadjoint Hilbert vector.
Choose a bounded selfadjoint original polynomial \(b\) such that \(\langle a\zeta a,b\rangle\) is real and nonzero by trace Hilbert density.
At \(u_t=t b+i\sqrt{1-t^2b^2}\), projective differentiation of the series and the actual vacuum of \(iI_{a\otimes a}\gamma\) give
\[
              F_{a\otimes a}(u_t)=-t\langle a\zeta a,b\rangle+O_b(t^2).
\]
Changing the sign of small \(t\) makes this positive while \((\tau a)^2=0\).
Thus the all-test order bound without the multiplication term forces vanishing of the liberation gradient.

### Cauchy kernels and partition defects

For each fixed \(\epsilon\), take \(k\) to be each of the two real components of \(c_{\epsilon,v}\) in (1), using the common conull set, and then integrate in \(v\).
The separated representation of the signed functional permits Fubini because all kernels are bounded at this cutoff.
The sum of the trace terms integrates to at most \(\|\xi_\mu\|_2^2\) by the [scalar soft Cauchy estimate (14)](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms).
The row terms integrate to at most \(2I\) since \(|c_{\epsilon,v}(z)|\le1/|z-v|\) away from the diagonal.
This proves (2).
For the stated finite sums the second inequality of (5) bounds \(F_{q_n}\) from below uniformly.
The gap convergence and real symmetry give convergence with the conjugated gap too, and hence convergence of \(F_{q_n-K_{\epsilon_n}}\) to \(F_g\) on each analytic test by its generator tensors and convergent differentiated power series.
The [signed curvature and domain implication](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) gives the stated consequence from a uniform lower bound on \(F_{g+K_\epsilon}\) after subtracting (2).

On \(D_+\), (4) gives \(\nu(R^2)/m_R^3\le4(r/m_R)^2\,\sigma(R^2)/m_R\to0\).
Applying both parts of (5) to \(1_R\) and dividing by \(m_R^2\) gives the bounds on the kernel diagonal.
For (3) split \(E\) into countably many disjoint Borel pieces \(E_j\) on each of which the lower density exceeds \(1/j\), discarding empty pieces and a null remainder.
At almost every point of \(E_j\), differentiation of \(1_{E_j}\) gives \(\mu(E_j\cap B(v,r))\ge r/(2j)\) at every sufficiently small radius.
Choose by the Euclidean Vitali covering theorem for finite Borel measures a disjoint countable family of such balls of radii \(r<\delta_j\) covering \(E_j\) modulo \(\mu\)-null sets.
The pieces \(F=E_j\cap B(v,r)\) have
\[
               \frac{\nu(F^2)}{\mu(F)^2}\le16j^2\sigma(F^2).
\]
Their squares are disjoint and lie in \(\{|z-w|<2\delta_j\}\).
As \(\sigma\) gives zero mass to the diagonal, \(\delta_j\) can make the sum at level \(j\) below \(2^{-j}\delta\) for any prescribed \(\delta>0\).
This proves (3) without any pointwise density bound for \(\nu\).
Consequently the smaller-side subdivision in [the rectangle calculation](Yin_C_F0332_v1.md#subdivision-by-cubes) eliminates its entire small-side diagonal cost whenever that side lies in \(D_+\).
The unsplit diagonal and cross terms remain.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:59 |
| status | open |
| reason | Fix the common spectral-row estimate, its Cauchy-kernel consequence and the endpoint partition formula for independent proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Common row order bound, vanishing-gradient converse, Cauchy Gram costs and local partition defects. |
| argument | [Argument](#argument) | Small-ball differentiation, averaged perturbed rank-one tests, the trace-class kernel and the positive-density covering. |
| dependency | [Liberation criterion](Yin_C_F0238_v1.md#statement) | Actual vacuum norm and finite inverse-gap energy. |
| dependency | [Marginal adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Product absolute continuity and Borel rank-one vacua. |
| dependency | [Uncentered square](Yin_C_F0331_v1.md#the-uncentered-square) | Exact upper bound before averaging two localized perturbations. |
| dependency | [Projection square](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Lower projection bound in the signed normalization. |
| dependency | [Scalar soft Cauchy transforms](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Uniform integral of the squared means of the two real test functions. |
| dependency | [Signed curvature](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Lower signed form implies the two original canonical domains. |
| dependency | [Subdivision](Yin_C_F0332_v1.md#subdivision-by-cubes) | The small-side diagonal contribution removed by (3). |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:06 |
| status | proved |
| reason | R_F0340 checked the single conull set and row differentiation, trace-class diagonal, inverse-gap energy bound on Cauchy Gram kernels and positive-density partitions against the declared dependencies. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Common row order bound, vanishing-gradient converse, Cauchy Gram costs and local partition defects. |
| argument | [Argument](#argument) | Small-ball differentiation, averaged perturbed rank-one tests, the trace-class kernel and the positive-density covering. |
| dependency | [Liberation criterion](Yin_C_F0238_v1.md#statement) | Actual vacuum norm and finite inverse-gap energy. |
| dependency | [Marginal adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Product absolute continuity and Borel rank-one vacua. |
| dependency | [Uncentered square](Yin_C_F0331_v1.md#the-uncentered-square) | Exact upper bound before averaging two localized perturbations. |
| dependency | [Projection square](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Lower projection bound in the signed normalization. |
| dependency | [Scalar soft Cauchy transforms](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Uniform integral of the squared means of the two real test functions. |
| dependency | [Signed curvature](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Lower signed form implies the two original canonical domains. |
| dependency | [Subdivision](Yin_C_F0332_v1.md#subdivision-by-cubes) | The small-side diagonal contribution removed by (3). |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0340_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
