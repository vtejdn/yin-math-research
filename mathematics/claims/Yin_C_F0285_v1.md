---
author: Yin
---

# Mixed spectral projections in both canonical domains outside a set of dimension at most two thirds

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a finite bounded normal generating tuple with [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Fix a coordinate \(Z=X_i\), its derivation \(\delta\) on \(P=\mathbb C\langle X,X^*\rangle\), its vacuum \(\xi\), and its original right slice \(E=(\mathrm{id}\otimes\tau)\delta\) on \(P\).
Let \(E^\#\) be the right slice for this coordinate of the adjoint tuple, with \(\delta^\#p=(\delta(p^*))^\dagger\), where \(\dagger\) flips and takes adjoints on both legs.
Write \(E_r,E_r^\#\) for the normal bounded extensions of the right slices suppressed in the inner spectral variables of the coordinate by \(|z-w|^2/(|z-w|^2+r^2)\), \(r>0\).
For any selfadjoint \(p\in P\), put \(\mu=\operatorname{law}(p)\) on \(\mathbb R\) and define
\[
 F_t(s)=\mu([t-s,t+s]),\quad
 H_t=\int_0^\infty F_t(s)^{3/2}\,\frac{ds}{s^2},\quad
 e_t=1_{(-\infty,t)}(p).
\]
Writing \(\Phi(a\otimes b)=a\otimes b^{\rm op}\), put \(L=\|\Phi(\delta p)\|_{M\bar\otimes M^{\rm op}}\), which is finite.
If \(H_t<\infty\), \(\mu(\{t\})=0\) and \(e_t\) belongs to all four domains \(\operatorname{Dom}\bar E,\operatorname{Dom}E^*,\operatorname{Dom}\overline{E^\#},\operatorname{Dom}(E^\#)^*\).
For an absolute \(C<\infty\),
\[
 \sup_{r>0}\max\{\|E_re_t\|_2,\|E_r^\#e_t\|_2\}
       \le C L H_t,\qquad
       E_re_t\longrightarrow\bar E e_t,\quad
       E_r^\#e_t\longrightarrow\overline{E^\#} e_t
         \quad\text{in }L^2 \text{ as }r\downarrow0.                       \tag{1}
\]
The original adjoint value satisfies \(E^*e_t=e_t\xi-\overline{E^\#}e_t\), with the analogous conjugate formula.
The exceptional set \(\{t:H_t=\infty\}\) has Hausdorff dimension at most \(2/3\).
This conclusion and (1) apply on the original algebra for mixed \(p\) of arbitrary degree.

For these same projections put \(\mathcal J_p(t)=\int_0^\infty
       \|(p-t-is)^{-1}\|_2\,\|(p-t-is)^{-1}\|_1\,ds\).
There are absolute positive constants \(c,C'\) such that
\[
                           c H_t\le\mathcal J_p(t)\le C'H_t.              \tag{2}
\]
The exponent \(2/3\) cannot be reduced for this integral criterion on general scalar spectral laws.
There is an actual normal pair with both full canonical domains and a selfadjoint mixed polynomial for which the exceptional set of the integral criterion has dimension exactly \(2/3\).
This sharpness concerns (2).
The threshold \(t\) need not cut any prescribed trace, and finite constants in (1) need not be uniform as \(p\) varies.

## Argument

### Slices of resolvents of a mixed polynomial

Use the linear unitary \(\Phi\) into the tracial Hilbert space of \(\mathcal B=M\bar\otimes M^{\rm op}\), under which both outer multipliers act from the left and inner multipliers act from the right, with the order on the second leg reversed. [Opposite tensor representation](Yin_C_F0229_v1.md#argument)
In these conventions \(V=\Phi(\delta p)\) is bounded.
Indeed the normal [starred values](Yin_C_F0076_v1.md#statement) are either zero, the unit, or the bounded marginal secant phase in the product of two abelian spectral algebras.
The identification with the opposite second algebra preserves the scalar marginal phase norm by commutativity on that marginal.
Every differentiated mixed word is a finite sum of these bounded tensors multiplied from the left by its bounded word prefix and its opposite suffix.
This proves the assertion at the level of \(\mathcal B\) itself.
Flip and adjoint take a simple tensor \(a\otimes b^{\rm op}\) to \(b^*\otimes(a^*)^{\rm op}\), extending to an antilinear isometric multiplicative map on \(\mathcal B\).
One can see this by composing the two adjoint identifications with the opposite algebras and interchanging the spatial tensor factors.
Thus the corresponding \(L\) is the same for \(\delta^\#p\) since \(p=p^*\).

Let \(V_r=V g_r\), where \(g_r(z,w)=|z-w|^2/(|z-w|^2+r^2)\) in the two inner spectral legs.
Then \(\|V_r\|\le L\) and \(V_r\to V\) in trace Hilbert norm, since \(Z\) has diffuse law and the diagonal has zero product trace.
Use \(g_r=1\) when considering the unsuppressed operator.
For \(s>0\) set \(R_\pm=(p-t\mp is)^{-1}\).
The resolvent lies in the closed derivative graph, with derivative \(-(R_\pm\otimes R_\pm^{\rm op})V\) under \(\Phi\).
In fact \(R_\pm=(p-t\pm is)((p-t)^2+s^2)^{-1}\) admits norm-convergent polynomial approximants in \(p\) with graph convergence by a Neumann series at a scalar strictly larger than \(\|(p-t)^2+s^2\|\).
The differentiated series converges because its \(n\)-th product derivative is bounded by a constant times \(nq^{n-1}\) for a fixed \(q<1\).
Differentiating the inverse identity gives the displayed sign and order, as in the [resolvent graph computation](Yin_C_F0229_v1.md#argument).
Slicing the graph approximation and applying the bounded inner multiplier proves the same formula for the sliced resolvents, with \(V_r\) in place of \(V\).
The fixed-radius extension agrees there by its operator-norm continuity on \(M\). [Normal cutoff extensions](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra)

For every \(V'\in\mathcal B\) and \(R\in M\), tracial slicing on the second leg gives
\[
 \|(\mathrm{id}\otimes\tau^{\rm op})((R\otimes R^{\rm op})V')\|_2
       \le \|R\|_2\,\|R\|_1\,\|V'\| .
\]
Indeed the slice before the first \(R\) is the normal functional \(b\mapsto\tau^{\rm op}(R^{\rm op}b)\) applied in the second variable, of norm \(\|R\|_1\).
Testing between unit vectors in the first-leg representation gives the usual norm bound for this slice map (first on vector functionals in the second leg, then by polar decomposition of the functional).
Multiplication by the first \(R\) gives the claimed Hilbert norm.
The bound applies uniformly to both signs, both orientations and every \(r\).

### The mass integral and the projection graph limit

Put \(s_j=2^j s\) for \(j\ge0\).
For \(b=1,2\) the restriction to \(|x-t|\le s\) gives \(\|R_+\|_b\ge F_t(s)^{1/b}/(\sqrt2\,s)\).
Splitting the complement into dyadic annuli gives
\[
 \|R_+\|_b\le \frac{2}{s}
          \left(\sum_{j\ge0}2^{-bj}F_t(s_j)\right)^{1/b}.
\]
It follows that the product has lower bound \(F_t(s)^{3/2}/(2s^2)\) and upper bound
\[
   \frac4{s^2}\sum_{j,k\ge0}2^{-j-k}F_t(2^j s)F_t(2^k s)^{1/2}.
\]
In the integral of the upper bound with measure \(ds/s^2\) on the sum, Hölder with exponents \(3/2,3\) bounds each product integral by \(2^{(2j+k)/3}H_t\).
The remaining coefficients \(2^{-j/3-2k/3}\) are summable.
This proves (2), including the case of infinite integrals.
Finiteness forces no atom at \(t\).

The bounded function of \(p\)
\[
 b_{\epsilon,A}=\tfrac12 1-\frac1{2\pi}\int_{\epsilon}^{A}(R_++R_-)\,ds
\]
converges strongly-star to \(e_t\) as \(\epsilon\downarrow0,\ A\uparrow\infty\), when the atom is zero.
Indeed the integrand is \(2(p-t)((p-t)^2+s^2)^{-1}\), whose scalar integral is the difference of two arctangents, with absolute value at most \(\pi\).
On a compact integration interval the resolvent and each graph derivative depend continuously on \(s\) in their Hilbert norms.
Riemann sums, the polynomial approximants above and graph closure put each \(b_{\epsilon,A}\) in all the indicated forward graphs.
The bound on \(\mathcal J_p(t)\) now gives absolute convergence in \(H\) of the integrals of the sliced resolvents up to both endpoints, uniformly in the tail estimates over \(r\) and over both orientations.
Strong convergence of the bounded inputs and closedness of the original right slices give \(e_t\) in both forward domains with the integral as output.
For fixed \(r\), normality on bounded inputs identifies the output with \(E_re_t\) in the same formula.
For each fixed \(s>0\), \(V_r\to V\) in \(L^2(\mathcal B)\) gives convergence of the two sliced resolvents.
Dominated convergence with the integrable bound in (2) proves the strong limits in (1).

On \(P\), the [actual slice-adjoint identity](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) and [reversal of the derivation](Yin_C_F0073_v1.md#statement) give \(E^*x=x\xi-E^\#x\).
For each resolvent above all approximants converge in operator norm with their two graph values, so this adjoint formula passes to each compact integral by closedness and Riemann sums.
The bounded strong-star limit \(b_{\epsilon,A}\to e_t\) gives \(b_{\epsilon,A}\xi\to e_t\xi\).
The opposite forward values converge in norm, hence so do the actual adjoint values.
Closedness gives the asserted adjoint domain and identity.
Using the adjoint tuple gives its second adjoint formula with \(\xi^*\).

### Size of the exceptional thresholds

Fix \(2/3<\alpha<1\).
If \(F_t(s)\le s^\alpha\) for all sufficiently small \(s\), then \(H_t<\infty\) since \(3\alpha/2>1\) and \(F_t\le1\).
For an exceptional \(t\) there are arbitrarily small radii \(s\) at which \(F_t(s)>s^\alpha\).
Choosing a dyadic radius \(2^{-j}\in[s,2s)\), the ball around \(t\) of this radius has mass greater than \(2^{-\alpha}2^{-j\alpha}\).
One of at most four closed dyadic intervals of length \(2^{-j}\) covering that ball has mass at least a fixed multiple of \(2^{-j\alpha}\).
There are at most \(C_\alpha2^{j\alpha}\) such heavy intervals at scale \(j\) since their overlap multiplicity is at most two.
Their fivefold dilates cover the possible centers \(t\) for that scale.
For each \(\beta>\alpha\) the sum of \(\beta\)-powers of these diameters over \(j\ge n\) tends to zero as \(n\to\infty\).
This proves zero \(\beta\)-dimensional Hausdorff measure of the exceptional set.
Letting \(\alpha\downarrow2/3\) proves the dimension bound.

For sharpness, start with two closed subintervals of \([0,1]\) of relative length \(\lambda=2^{-3/2}\), one at each end.
Repeat the replacement in each interval and give each child half its parent's mass.
Let \(K\) be the compact limit and \(\sigma\) the resulting nonatomic probability.
For \(\lambda^{j+1}<s\le\lambda^j\) and \(t\in K\), the interval \([t-s,t+s]\) contains a level \(j+1\) interval of mass \(2^{-(j+1)}\).
It meets only a bounded number of level \(j\) intervals because these have length \(\lambda^j\), disjoint interiors, and the testing interval has length at most \(2\lambda^j\).
It follows that \(c s^{2/3}\le\sigma([t-s,t+s])\le C s^{2/3}\) there.
The upper mass bound gives \(\dim_H K\ge2/3\) by summing over any interval cover, and the level covers give the opposite inequality.
Thus \(H_t=\infty\) on \(K\), while it is finite off \(K\) by the positive distance to the support.

Let \(Z=x+iy\) have product law given by uniform \(x\in[0,1]\) and independent \(y\sim\sigma\).
Its ball mass is uniformly \(O(s^{5/3})\) for \(0<s\le1\), so dyadic annuli give \(\sup_z\int |z-w|^{-1}d\mu_Z(w)<\infty\) on its support.
The scalar divided difference on the marginal starred algebra has bounded vacuum by symmetrizing its two traces: the pairing is \(\int f(z)\,2\int (z-w)^{-1}d\mu_Z(w)\,d\mu_Z(z)\).
Its integral is absolute for bounded \(f\), so the complex conjugate of the bounded coefficient is the required actual Hilbert vacuum.
The derivative is defined on represented polynomials by their divided differences, well-defined off the product-null diagonal.
Adjoin one freely independent Haar unitary \(u\), which has an actual scalar vacuum.
Both scalar marginals have finite columns in both orientations by the [scalar column theorem](Yin_C_F0267_v1.md#statement), and the [one-free-coordinate theorem](Yin_C_F0278_v1.md#statement) gives actuality and both original full domains for the pair.
The selfadjoint mixed polynomial \(p=u(\operatorname{Im}Z)u^*\) has law \(\sigma\).
This realizes the exact dimension for the integral criterion even on a tuple where all projections lie in both canonical domains.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:20 |
| status | open |
| reason | Fix simultaneous original domain inclusion and strong cutoff convergence for sharp mixed spectral cuts using local one-dimensional mass. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cutoff and actual domain conclusions in both orientations, mass criterion, exceptional dimension and scope. |
| argument | [Argument](#argument) | Bounded opposite tensors, tracial resolvent slices, dyadic integral, graph limits and the exceptional-set dimension estimate. |
| dependency | [Forced normal symbols](Yin_C_F0076_v1.md#statement) | Diffuse coordinate laws and bounded scalar spectral phases on all starred generators. |
| dependency | [Opposite tensor and graph resolvents](Yin_C_F0229_v1.md#argument) | Coarse tensor convention and polynomial graph approximation of a resolvent of a bounded positive polynomial. |
| dependency | [Normal fixed-radius slices](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | The suppressed core maps extend normally and continuously to bounded inputs. |
| dependency | [Polynomial slice adjoint](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Actual adjoint identity on the original starred polynomial domain. |
| dependency | [Flip and adjoint](Yin_C_F0073_v1.md#statement) | The opposite right slice in the polynomial adjoint formula and its actual vacuum. |
| dependency | [Scalar columns](Yin_C_F0267_v1.md#statement) | Actual scalar normal vacua give finite columns in both orientations for the sharpness example. |
| dependency | [Free enlargement](Yin_C_F0278_v1.md#statement) | One free Haar coordinate preserves actuality and yields the full canonical domains in the example. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:25 |
| status | proved |
| reason | The independent review verifies the mass criterion, simultaneous sharp-cut domains, strong regularization limits and the optimal exceptional dimension for the integral. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cutoff and actual domain conclusions in both orientations, mass criterion, exceptional dimension and scope. |
| argument | [Argument](#argument) | Bounded opposite tensors, tracial resolvent slices, dyadic integral, graph limits and the exceptional-set dimension estimate. |
| dependency | [Forced normal symbols](Yin_C_F0076_v1.md#statement) | Diffuse coordinate laws and bounded scalar spectral phases on all starred generators. |
| dependency | [Opposite tensor and graph resolvents](Yin_C_F0229_v1.md#argument) | Coarse tensor convention and polynomial graph approximation of a resolvent of a bounded positive polynomial. |
| dependency | [Normal fixed-radius slices](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | The suppressed core maps extend normally and continuously to bounded inputs. |
| dependency | [Polynomial slice adjoint](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Actual adjoint identity on the original starred polynomial domain. |
| dependency | [Flip and adjoint](Yin_C_F0073_v1.md#statement) | The opposite right slice in the polynomial adjoint formula and its actual vacuum. |
| dependency | [Scalar columns](Yin_C_F0267_v1.md#statement) | Actual scalar normal vacua give finite columns in both orientations for the sharpness example. |
| dependency | [Free enlargement](Yin_C_F0278_v1.md#statement) | One free Haar coordinate preserves actuality and yields the full canonical domains in the example. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0294_v1.md#finding) | The seven inputs, opposite tensor orientation, the resolvent slice inequality, both graph limits, the covering estimate and the actual Cantor example. |
