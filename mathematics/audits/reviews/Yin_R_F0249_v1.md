---
author: Yin
---
# Independent review of singular coupling densities and finite-degree vacuum tests

## Whole-proof finding

At 2026-11-14T10:18 UTC the reviewer independently checked the [statement](../../claims/Yin_C_F0240_v1.md#statement) and complete [argument](../../claims/Yin_C_F0240_v1.md#argument) fixed in the [candidate decision](../../claims/Yin_C_F0240_v1.md#decision-candidate) of 2026-11-14T10:17.
The reviewer had independently reviewed the fixed ordered two-block theorem C_F0239 and its planar energy input.
The reviewer did not develop this candidate and used its fixed text and directly needed inputs without receiving a proof-development discussion or earlier finding for C_F0240.
Both parts hold, including the explicit constants, the lower norm bound under moment convergence and the distinct conclusions about the two realizations.

**Stochastic singular background and its scores.**
The row integral of \(K(y,s)=|y-s|^{-\alpha}\) is uniformly bounded by polar integration up to radius two with normalized area measure.
The rank-one correction to \(cK\) is positive and its row integral equals \(1-cq(y)\) since the integral of \(1-cq\) is \(1-cQ\).
Symmetry gives the column integrals.
The correction is bounded and \(K\ge 2^{-\alpha}\) off the diagonal, which gives both comparisons for \(p\).
Absolute convergence of \(G_{p_y\mu}(z)\) uniformly in \(y,z\) follows by splitting according to which of \(|z-s|,|y-s|\) is smaller.
The corresponding bound on each region is the inverse \((1+\alpha)\)-th power of the smaller distance, integrable uniformly because \(\alpha<1\).
The same argument for \(G_\mu\) uses only the inverse first power.

In the conditional difference-quotient integral the \(h(s)\) term gives \(G_\mu(s)\,d\nu_y(s)\).
Reversing the sign and denominator of the \(h(z)\) term gives \(G_{\nu_y}(z)\,d\mu(z)\).
Consequently the score on the atom is exactly \(\overline H(y,y)=G_\mu(y)\), while away from it one divides the latter term by \((1-\lambda)p_y(z)\), obtaining (4).
The absolute estimates justify splitting the terms before combining their Cauchy kernels.
The pole correction in the squared score costs a constant times \(\int |z-y|^{-2}/p_y(z)\,d\mu(z)\), which is uniformly finite by \(p_y(z)\ge c|z-y|^{-\alpha}\) and \(\alpha>0\).
The uniform positive lower bound on \(p_y\) controls the remaining correction.
The integrals define measurable scores by measurable truncation, and the atom is assigned its separate value on the measurable diagonal.
The ordered two-block criterion gives boundedness, with the same reasoning in the opposite order by symmetry.

**Scope of the two realizations.**
In the commuting multiplication model, \(D^*[D,X]=0\), but the proposed canonical cuts give the tensor \(D^*D\otimes1-D^*\otimes D\).
The normal phase rule forces the omitted starred value to be zero for any actual normal tuple.
The double trace is \(1/2\) since normalized disk area has \(\tau(D)=0\) and \(\tau(D^*D)=1/2\).
Thus this degree-three relation, including the three-block word \(D^*XD\), excludes a represented actual vacuum for that model even though each ordered two-block test is bounded.

In the free-product model \(w=\cos\theta+i\sin\theta\,v\) is unitary and \(b=|\tau(w)|^2=\cos^2\theta\).
Centering \(w\), and then the two factors \(g(D),h(X)\) in their common old algebra, gives precisely the convex combination of their old joint coupling and the product of their marginals.
The resulting diagonal weight is \(b\lambda\) and the normalized background is a positive mixture of \(p\) and the constant density with coefficient sum one.
The comparison to \(|y-s|^{-\alpha}\) and the score estimates therefore persist.
The length-four part of \([X,wDw^*]\) is \(\sin^2\theta(XvDv-vDvX)\).
These are centered alternating tensors from the two free factors, with nonzero Hilbert norms and different initial factors.
All other terms reduce to lengths at most three, so cannot cancel this component.
This proves noncommutation while leaving full mixed-word vacuum existence for this realization undetermined.
For a prescribed diagonal mass \(\lambda'\in(0,1)\), taking \(b\in(\lambda',1)\) and \(\lambda=\lambda'/b\) preserves the stated parameter ranges.

**Degree, constants and weak limits.**
The polynomial \(q_n=L^{-1}\sum_{j=0}^{n-1}(1-|d|^2/L)^j\) has highest homogeneous term \((-1)^{n-1}|d|^{2n-2}/L^n\).
Thus the displayed formal test \(F_n\) has total degree \(2n-1\) and vanishes at \(d=0\).
On the support of the target \(|d|\le 2R\), so \(0\le|d|^2 q_n\le1\) and \(\|F_n\|_{L^2(\mu^2)}^2\le A_n\).
The denominator is positive, since \(\mu\) is diffuse and \(q_n>0\) on this difference disk.
The atomic contribution is \(+\lambda A_n\), using \(F_n(y,y)=0\) and division by \(y-z\), and the product contribution has modulus at most \((1-\lambda)\|\zeta\|_2\|F_n\|_{L^2(\mu^2)}\).
Division by \(\sqrt{1-\lambda}\|F_n\|_{L^2(\mu^2)}\) gives the first inequality of (3), without needing its lower bound to be positive at small \(n\).

For \(u=|d|^2/L\in[0,1]\), the exponential estimate and concavity on \([0,1]\) give \(1-(1-u)^n\ge(1-e^{-1})\min(nu,1)\).
For \(0<t\le R\), \(\lceil2\sqrt2 R/t\rceil\le4R/t\), and cells from that many subdivisions on each axis have diameter at most \(t\).
Cauchy–Schwarz on the cell masses gives the probability lower bound \(t^2/(16R^2)\).
The layer integral of the indicator \(|d|\le t\) against \(2t^{-3}dt\) on \([2R/\sqrt n,R]\) is bounded pointwise above by \(\min(n/L,|d|^{-2})\).
Integrating the cell lower bound on this range gives \((8R^2)^{-1}\log(\sqrt n/2)=\log(n/4)/(16R^2)\).
Together these yield the second inequality of (3), with zero logarithm at the included endpoint \(n=4\).

On a fixed operator cutoff, convergence of star moments gives weak convergence of both marginal laws and of the ordered couplings, since separated star polynomials are uniformly dense on the common compact set.
For each fixed \(n\), the polynomial norm converges by the two-block isometry.
The numerator's integrand is continuous away from \(s=z\) and uniformly bounded on the common compact set by the first real derivative bound for the fixed polynomial.
The product of the weakly convergent coupling and the independent marginal converges weakly there.
Although the target coupling charges \(y=s\), its product with the independent diffuse \(z\)-law gives zero mass to \(s=z\).
Bounded almost-everywhere continuity therefore gives convergence of the numerators, and positivity of the target norm gives convergence of the quotients.
For any prescribed lower bound one first chooses \(n\) so that (3) exceeds it strictly and then passes to sufficiently large indices in the sequence of pairs.
The actual distinguished vacuum dominates the observed quotient at each index, so its norms tend to infinity.
The moment-limit conclusion concerns the product-background target in item 2.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0240_v1.md#statement) | Both parts, the coupling range, realization-specific scope, degree, constants and persistence under joint moment limits. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0240_v1.md#argument) | Stochastic normalization, singular score, cubic relation, noncommutation, truncated energy and the two distinct diagonal sets in the limit. |
| [Whole-proof finding](#whole-proof-finding) | [Ordered conditional vacuum test](../../claims/Yin_C_F0239_v1.md#statement) | Ordered norm isometry, conditional scores and the bound by any actual distinguished vacuum. |
| [Whole-proof finding](#whole-proof-finding) | [Conjugated-copy calculation](../../claims/Yin_C_F0239_v1.md#a-conjugated-copy-of-a-normal-marginal) | Free centered expectation computation applied with two old functions, and the product-background coupling at the indicated target. |
| [Whole-proof finding](#whole-proof-finding) | [Normal marginal phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, zero omitted starred derivative for the commuting cubic-relation test. |
| [Whole-proof finding](#whole-proof-finding) | [Free-product Hilbert representation](../literature/Voi98/Yin_U005.md#voi98-u005) | Sections 5.5–5.8, norm and orthogonality of the two centered length-four words. |
| [Whole-proof finding](#whole-proof-finding) | [Planar energy grid](../../claims/Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Cauchy–Schwarz on planar cells and layer integration at finite scales, with constants separately checked here. |
