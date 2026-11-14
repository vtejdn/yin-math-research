---
author: Yin
---

# Canonical domains for two planar arcs with power-order tangency

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be a finite tuple of bounded normal generators of a finite von Neumann algebra with faithful normal probability trace \(\tau\), satisfying the [actual starred ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
In a coordinate system obtained by a fixed translation and rotation, suppose the spectrum of \(Z=X_i\) lies on the union of the arcs
\[
      z_\pm(x)=x+i\big(g(x)\pm d(x)\big),\qquad 0\le x\le R,\quad R>0.
\]
Here \(g,d\) are real \(C^2\) functions on the compact interval, \(g(0)=g'(0)=d(0)=0\), and for some \(\kappa>1,\ 0<c\le C<\infty\),
\[
                       c\,x^\kappa\le d(x)\le C\,x^\kappa
                              \qquad(0<x\le R).                           \tag{1}
\]
Thus both outgoing tangents at the origin coincide, and the planar separation at the same real parameter is \(2d(x)\).
The spectrum may be any closed subset of this union, with either branch carrying zero mass.
There is no assumption on the spectra of the other normal coordinates or on joint correlations.

The canonical right slice \(E=C_0\delta_i\), \(C_0=\mathrm{id}\otimes\tau\), on the original represented starred polynomial core \(P\) satisfies
\[
         \sum_j\|E p_j\|_2^2
                 \le B^2\Big\|\sum_j p_j^*p_j\Big\|
                    \qquad (p_j\in P,\ \text{finite columns}) .             \tag{2}
\]
The constant can depend on the geometry and law.
The adjoint tuple has finite distinguished right column cost as well.
Consequently the closure of \(E\) and its Hilbert adjoint both have domains containing all bounded vectors, and the negative closure supplies the generator-first strong commutator at this coordinate.
This includes \(x\pm ix^2\) and pairs with a curved common midline satisfying (1).
If each coordinate has such a carrier, then \(\mathsf A\Rightarrow\mathsf S\) for the tuple.

## Argument

### A real parameter interleaving the two branches

We calculate in the translated and rotated axes of the statement.
A constant translation cancels in each divided difference, and a rotation multiplies the forward difference and its inverse by reciprocal complex unit scalars.
The absolute estimates and generator checks below therefore give the claimed estimates also in the initial axes.

Set \(p=1/(\kappa-1)\), \(x_n=R n^{-p}\) for \(n\ge1\), \(\ell_n=x_n-x_{n+1}\), and \(I_n=(x_{n+1},x_n)\).
There are positive constants depending only on \(R,\kappa\) such that \(\ell_n\) is comparable to \(x^\kappa\) throughout \(\overline I_n\).
Indeed the mean value theorem gives \(\ell_n\) comparable to \(R n^{-p-1}\), and \(p\kappa=p+1\).
On the two copies of \(I_n\) assign real coordinates
\[
 F_+(x)=10x_{n+1}+\ell_n+(x-x_{n+1}),\qquad
 F_-(x)=10x_{n+1}+4\ell_n+(x-x_{n+1}).                                  \tag{3}
\]
Their images are the disjoint open subintervals at offsets \((1,2)\ell_n\) and \((4,5)\ell_n\) inside \([10x_{n+1},10x_n]\).
All assigned intervals are disjoint across signs and indices.
The errors \(\epsilon_\pm(x)=F_\pm(x)-10x\) obey \(|\epsilon_\pm(x)|\le A_0 x^\kappa\) since \(0<x-x_{n+1}<\ell_n\).

On each closed copy of an assigned interval define a map \(h\) by linear decoding of \(x\) from (3), followed by \(z_+(x)\) or \(z_-(x)\) on that copy, respectively.
Between these intervals interpolate the complex endpoint values by straight lines, and set \(h(0)=0\).
At the top extend constantly over any final gap up to \(10R\).
This gives a Lipschitz map \(h:[0,10R]\to\mathbb C\).
In fact its Lipschitz constants on filled intervals are bounded by \(1+\|g'\|_\infty+\|d'\|_\infty\).
The within-tile gap has length \(2\ell_n\) and joins endpoints with horizontal separation \(\ell_n\) and vertical separation bounded by \(\|g'\|_\infty\ell_n+d(x_n)+d(x_{n+1})\), which is \(O(\ell_n)\).
The gap across the boundary of two successive tiles has length \(5\ell_{n+1}+\ell_n\).
It joins the endpoint of the minus interval in tile \(n+1\) and the start of the plus interval in tile \(n\), both at \(x_{n+1}\), with planar separation \(2d(x_{n+1})=O(\ell_n)\).
Thus the interpolating slopes are uniformly bounded.
Any interval bounded away from zero meets only finitely many such intervals and gaps.
The bound extends to zero by continuity, since all the endpoints and the interpolated segments there converge to zero.

Remove the countable set of points \(z_\pm(x_n)\) and the common apex from the original carrier.
It has zero spectral projection by the [diffuse normal generator law](Yin_C_F0076_v1.md#statement).
The assignment \(z_\pm(x)\mapsto F_\pm(x)\) is injective with Borel inverse \(h\) on this conull set.
It defines a bounded selfadjoint \(S\) by spectral calculus, and \(W^*(S)=W^*(Z),\ h(S)=Z\).
On the new parameter hull the interior points of the gaps have zero spectral mass.
Assignments at the removed points do not affect \(S\) or its law.

The tuple obtained by replacing \(Z\) with \(S\) has actual ACSY.
Here is the argument for this countable encoding.
In an equal-mesh partition of the parameter hull, restrict each cell to the assigned intervals, and let \(e_J\) be the old spectral projection of its Borel image.
These projections are disjoint by injectivity on the assigned sets.
For a cell of length \(t\), its image is in a disk of radius \(\operatorname{Lip}(h)t\).
The [scalar packing inequality](Yin_C_F0233_v1.md#statement), part 1, bounds \(\sum_J\tau(e_J)^3/t^2\) independently of the mesh.
Taking the dyadic histograms in weak \(L^3\) therefore gives an \(L^3\) density for the real parameter law, as in [the real chart construction](Yin_C_F0248_v1.md#a-real-parameter-for-a-selected-chart).
The [scalar real-parameter criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) supplies its scalar vacuum.
The [invariant Borel liberation calculation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) keeps the liberation vacuum and transports the joint spectral measure by this conull change.
Since \(|h(s)-h(t)|\le\operatorname{Lip}(h)|s-t|\), the inverse squared real gap at the distinguished coordinate has finite liberation energy by the original actual inverse-gap condition.
The omitted coordinates retain their original energies and scalar vacua.
The [actual inverse-gap criterion](Yin_C_F0238_v1.md#statement) now applies at every coordinate of the parameter tuple.
Write \(\delta_S\) for its real distinguished derivation.
Its right slice has finite column cost on its entire mixed core \(P_S\). [Real-coordinate column bound](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column)

### The inverse secant between different branches

The bounded parameter-space kernel needed between the upper first leg and the lower second leg, written in decoded \(x,y\) coordinates, is
\[
 \begin{split}
 D(x,y)&=x-y+i\big(g(x)-g(y)+d(x)+d(y)\big),\\
 K(x,y)&=\frac{F_+(x)-F_-(y)}{D(x,y)}
   =10+\frac{\epsilon_+(x)-\epsilon_-(y)
                    -10i(g(x)-g(y)+d(x)+d(y))}{D(x,y)} .                 \tag{4}
 \end{split}
\]
We prove that it is a measurable Schur multiplier on this rectangle, extended by zero outside.
All estimates apply to the separate branch measures, allowing arbitrary restrictions of their supports.
The same multiplier bound holds with the legs exchanged by transposition, since the inverse secant is symmetric on the full variable pair.
Complex conjugation preserves the bound.

Let \(r_j=2^{-j}R,\ j\ge0\), and use the disjoint radial shells \((r_j/2,r_j]\) on each branch.
First take \(x\) in shell \(j\) and all \(0<y\le r_j/8\).
Their real difference is at least \(3r_j/8\).
The reciprocal \(D^{-1}=\int_0^\infty e^{-\lambda D}\,d\lambda\) has an integral representation by separated factors of total supremum-norm product at most \(8/(3r_j)\), as its two-variable real exponential bound is \(e^{-3\lambda r_j/8}\), also after taking the two separate suprema.
The numerator of the correction in (4) is a sum of functions of \(x\) and of \(y\), of total separated norm at most \(A_1(r_j^2+r_j^\kappa)\), by \(g(0)=g'(0)=0\), the bounded second derivative, and (1), (3).
The correction on this rectangle thus costs \(A_2(r_j+r_j^{\kappa-1})\) in Schur norm.
This is summable over \(j\).
For \(y\) in shell \(k\) and \(x\le r_k/8\), use the negative of \(D\) in the real-part Laplace representation and sum in \(k\) with the same bound.
These two families cover all shell indices with \(|j-k|\ge3\), and contain no comparable shell pair.

It remains to bound \(K\) uniformly on the rectangles \(|j-k|\le2\).
Put \(v=\max(r_j,r_k)\), \(d_x=d(x),\ d_y=d(y)\) and \(D_0=x-y+i(d_x+d_y)\).
Both \(x\) and \(y\) lie in \((v/8,v]\).
The positive numbers \(d_x,d_y\) are therefore comparable to \(v^\kappa\) there, uniformly in these rectangles.
The kernel \(\sqrt{d_xd_y}/D_0\) has the Hilbert-space factorization
\[
 \frac{\sqrt{d_xd_y}}{D_0}
   =-i\int_0^\infty
       \sqrt{d_x}\, e^{-\lambda d_x+i\lambda x}
       \sqrt{d_y}\, e^{-\lambda d_y-i\lambda y}\,d\lambda .               \tag{5}
\]
Each leg has \(L^2(d\lambda)\) norm \(1/\sqrt2\), so the Schur norm is at most \(1/2\). [Measurable factorization](../audits/literature/AP25/Yin_U001.md#measurable-schur-factorization)
Multiplication by one bounded factor on each variable preserves a Schur bound with the product of their sup norms.
Thus \((d_x+d_y)/D_0\) has bounded Schur norm here by writing it as the sum of the two products with \(\sqrt{d_x/d_y}\) and \(\sqrt{d_y/d_x}\).
The ratios have bounded separated cost on a comparable rectangle.
Consequently \((x-y)/D_0=1-i(d_x+d_y)/D_0\) has a uniform Schur bound \(A_3\).
The same argument gives a uniform bound for \((\epsilon_+(x)-\epsilon_-(y))/D_0\), using \(|\epsilon_\pm(u)|\le A_0u^\kappa\).

We next control the common midline on small rectangles.
The symbol
\[
             g^{[1]}(x,y)=\int_0^1 g'\big(\theta x+(1-\theta)y\big)
                                     \,d\theta
\]
has Schur norm at most \(A_4 v\) on \((v/8,v]^2\) when \(2v\le R\).
To verify this, multiply \(g'(v t)\) by a fixed smooth cutoff in \((0,2)\) equal to one on \([1/8,1]\), extending it by zero to a fixed period interval.
Its \(H^1\) norm is at most \(C_1 v\|g''\|_\infty\), since \(g'(0)=0\) and its derivative in \(t\) is \(v g''(vt)\) where used.
Cauchy–Schwarz on the Fourier coefficients with \(\sum_n(1+n^2)^{-1}<\infty\) bounds their absolute sum by the same norm times a fixed constant.
Each character at \((\theta x+(1-\theta)y)/v\) separates into two unitaries, so integration over \(\theta\) gives the asserted bound.
Using
\[
              \frac{D}{D_0}=1+i\,g^{[1]}(x,y)\frac{x-y}{D_0},
\]
the second term has Schur norm at most \(A_3 A_4 v\).
For \(v\) sufficiently small this is less than \(1/2\), so the Neumann series gives Schur norm at most two for \(D_0/D\).
Indeed composition of kernel multipliers is pointwise multiplication and operator-norm summation agrees with the pointwise reciprocal by uniform convergence of the geometric series.
Combining this with the preceding estimates gives a uniform bound for
\[
   K=\left(10\,\frac{x-y}{D_0}
                    +\frac{\epsilon_+(x)-\epsilon_-(y)}{D_0}\right)\frac{D_0}{D}
\]
on the small comparable rectangles.

Only finitely many comparable rectangles remain.
Their closed branch images are disjoint compact sets because coincidence requires \(x=y\) by real parts and would then give \(d(x)=0\) at a positive parameter.
The reciprocal \(1/(z-w)\) on each product has finite separated Fourier norm by inserting smooth planar cutoffs with disjoint supports, as in the [positive-distance calculation](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple).
The bounded functions \(F_+(x),F_-(y)\) act on their respective legs, proving finite Schur norm for these rectangles also.

At each fixed offset \(k-j\) with \(|k-j|\le2\), the first supports of these rectangles are disjoint and so are the second supports.
A multiplier which has Schur norm at most \(A_5\) on each rectangle then has norm at most \(A_5\) on their union, with zero elsewhere.
Indeed for an integral operator the multiplied diagonal blocks form an orthogonal direct sum, and each has norm at most \(A_5\) times the original operator norm.
For countably many blocks the assertion follows directly by the direct sum or by truncation on square-integrable kernels.
It applies also to \(K-10\).
Adding these five offsets, the absolutely summable far corrections and the single constant upper-to-lower rectangle gives the asserted full Schur symbol (4).
No mutual absolute continuity of the two branch measures enters the factorization.

### Recovery of the original columns

Let \(e_\pm\) be the projections of the two open branches, with their countable subdivision endpoints omitted.
For the cross rectangle use the Schur symbol \(k\) just proved in the encoded real parameter, zero off \(e_+\otimes e_-\).
Then \(C_0 I_k\delta_S\) has finite column cost on \(P_S\) by the [old-core Schur estimate](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice), since \(C_0\delta_S\) has finite cost.
The inner multiplication \(I_{a\otimes b}(u\otimes v)=ua\otimes bv\) is by the two marginal variables before the right trace.
Finite truncations of the symbol on the shell rectangles converge on every coarse input by their uniform pointwise bound and product-law domination of the coarse spectral measures. [Coarse measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core)

The forward map \(h\) in (3) is Lipschitz, including across all the encoding gaps.
The [norm-controlled mixed-core approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) thus supplies \(P_S\)-approximants with convergent coarse derivatives to every fixed original \(P\)-column of norm at most one and limit superior of input column norms at most \(1+\varepsilon\), for each \(\varepsilon>0\).
On \(P\),
\[
                    I_k\bar\delta_S= I_{e_+\otimes e_-}\delta_i .          \tag{6}
\]
At \(Z=h(S)\) the parameter derivative is its forward divided difference, so multiplying by \(k\) gives \(e_+\otimes e_-\).
At \(Z^*\) the same multiplication gives this rectangle times the original marginal phase \((\bar z-\bar w)/(z-w)\).
Both derivations vanish on the omitted starred generators and agree by the product rule. [Normal phase](Yin_C_F0076_v1.md#statement)
In the rotated axes the ratio \(k\) is multiplied by the inverse rotation, as required to obtain the identical normalization at the original \(Z\).
Boundedness of \(k\) passes the old-core column bound through the graph limit, then \(\varepsilon\downarrow0\) proves the original cross bound.
Transposition gives the reverse rectangle by the same proof.

Each same-branch rectangle has finite cost by the [single-piece chart argument](Yin_C_F0248_v1.md#restricting-the-graph-kernel-on-the-parameter-core) and its [localized core transfer](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple).
For clarity, use a separate real parameter with one copy of \([0,R]\) for the selected branch and a disjoint copy a positive distance away for the other.
Its forward map is Lipschitz and injective away from the null common vertex, so the real-parameter argument above applies again.
The selected graph \(g\pm d\) has derivative of bounded variation on its compact interval.
Extend that graph over the whole parameter hull and use the same-piece bound of the cited argument with \(e=f=e_\pm\).
Those steps use the selected single chart and the Lipschitz forward map on the remaining pieces, and require no condition on the outgoing angle of a discarded cross rectangle.
This choice avoids the artificial jumps of the encoding (3) on each single branch.

The four rectangles sum to the identity on the coarse marginal square, because the removed set is null in either leg.
Summing their bounds proves (2).
Reflection preserves (1) after interchanging the branches and replacing \(g\) by \(-g\).
The [actual flip-adjoint companion](Yin_C_F0076_v1.md#statement) therefore gives a right bound also at \(Z^*\), hence an original left bound by tracial involution.
The [two-slice theorem](Yin_C_F0072_v1.md#statement), part B, supplies both domain conclusions.
Graph approximation in the identity \(E(X_jp)-X_jE(p)=\delta_{ij}\tau(p)1\) gives the asserted commutator of the negative closure on bounded vectors.

Condition (1) ensures the comparable-shell height ratios in (5) and the summable separated correction at distant scales.
The argument leaves open the case of general positive separations with no such power comparison, including two branches with contact flatter than every power.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:28 |
| status | open |
| reason | The power-order tangency estimate, real encoding and norm-controlled original-core proof are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual distinguished right columns and both canonical domains under a two-branch power-order contact, including the quadratic cusp and its adjoint orientation. |
| argument | [Argument](#argument) | Interleaved real intervals with Lipschitz decoding, real parameter vacuum, Laplace and midline estimates for the cross Schur multiplier, disjoint shell sum, and recovery of the target mixed columns. |
| dependency | [Forced normal generators](Yin_C_F0076_v1.md#statement) | Diffuseness, starred generator values for the localized core verification and actual flip-adjoint companion. |
| dependency | [Scalar interval packing](Yin_C_F0233_v1.md#statement) | Part 1 on the disjoint spectral images of equal-mesh real parameter cells under a Lipschitz decoding map. |
| dependency | [Real parameter chart](Yin_C_F0248_v1.md#a-real-parameter-for-a-selected-chart) | Histogram argument and finite real inverse-gap mechanism applied here after verifying the countable parameter map and null exceptions. |
| dependency | [Real scalar vacuum](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | A compactly supported real \(L^3\) density has a scalar actual vacuum. |
| dependency | [Borel liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Its vacuum is invariant under conull injective Borel changes, with transported gap energies, also at the omitted coordinates. |
| dependency | [Inverse-gap vacuum identity](Yin_C_F0238_v1.md#statement) | The finite old distinguished energy and construction of the real distinguished vacuum under finite new energy and scalar vacuum. |
| dependency | [Coarse spectral measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Domination by the product law for bounded truncations of the rectangle multipliers. |
| dependency | [Old selfadjoint column](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | The canonical right slice at the real distinguished parameter has finite column cost on all mixed words. |
| dependency | [Measurable Schur factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001) | The bounded Hilbert-valued two-leg factorization yields the Schur bound in (5). |
| dependency | [Positive-distance and mixed-core localization](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Separated Fourier multipliers on disjoint compact planar pieces and passage of a bounded chart-restricted kernel to the original generators. |
| dependency | [Old-core measurable multiplier estimate](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Finite column bound for inserting a bounded measurable Schur kernel in the real parameter derivative. |
| dependency | [Column graph approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Norm-controlled finite columns approximating the original mixed inputs under a forward Lipschitz change before localized insertion. |
| dependency | [Single-branch localization](Yin_C_F0248_v1.md#restricting-the-graph-kernel-on-the-parameter-core) | The same-piece BV restriction with a separate parameter chart and Borel rectangle cutoffs on the old core. |
| dependency | [Canonical domain theorem](Yin_C_F0072_v1.md#statement) | Part B on the original canonical slice and its actual Hilbert adjoint once both one-input estimates are supplied. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:36 |
| status | proved |
| reason | Adopt the two-branch power-order tangency theorem after independent review of the interleaved parameter and the cross multiplier. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual distinguished right columns and both canonical domains under a two-branch power-order contact, including the quadratic cusp and its adjoint orientation. |
| argument | [Argument](#argument) | Interleaved real intervals with Lipschitz decoding, real parameter vacuum, Laplace and midline estimates for the cross Schur multiplier, disjoint shell sum, and recovery of the target mixed columns. |
| dependency | [Forced normal generators](Yin_C_F0076_v1.md#statement) | Diffuseness, starred generator values for the localized core verification and actual flip-adjoint companion. |
| dependency | [Scalar interval packing](Yin_C_F0233_v1.md#statement) | Part 1 on the disjoint spectral images of equal-mesh real parameter cells under a Lipschitz decoding map. |
| dependency | [Real parameter chart](Yin_C_F0248_v1.md#a-real-parameter-for-a-selected-chart) | Histogram argument and finite real inverse-gap mechanism applied here after verifying the countable parameter map and null exceptions. |
| dependency | [Real scalar vacuum](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | A compactly supported real \(L^3\) density has a scalar actual vacuum. |
| dependency | [Borel liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Its vacuum is invariant under conull injective Borel changes, with transported gap energies, also at the omitted coordinates. |
| dependency | [Inverse-gap vacuum identity](Yin_C_F0238_v1.md#statement) | The finite old distinguished energy and construction of the real distinguished vacuum under finite new energy and scalar vacuum. |
| dependency | [Coarse spectral measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Domination by the product law for bounded truncations of the rectangle multipliers. |
| dependency | [Old selfadjoint column](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | The canonical right slice at the real distinguished parameter has finite column cost on all mixed words. |
| dependency | [Measurable Schur factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001) | The bounded Hilbert-valued two-leg factorization yields the Schur bound in (5). |
| dependency | [Positive-distance and mixed-core localization](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Separated Fourier multipliers on disjoint compact planar pieces and passage of a bounded chart-restricted kernel to the original generators. |
| dependency | [Old-core measurable multiplier estimate](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Finite column bound for inserting a bounded measurable Schur kernel in the real parameter derivative. |
| dependency | [Column graph approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Norm-controlled finite columns approximating the original mixed inputs under a forward Lipschitz change before localized insertion. |
| dependency | [Single-branch localization](Yin_C_F0248_v1.md#restricting-the-graph-kernel-on-the-parameter-core) | The same-piece BV restriction with a separate parameter chart and Borel rectangle cutoffs on the old core. |
| dependency | [Canonical domain theorem](Yin_C_F0072_v1.md#statement) | Part B on the original canonical slice and its actual Hilbert adjoint once both one-input estimates are supplied. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0259_v1.md#finding) | Full original columns and both bounded-vector domains, the two-branch model including the quadratic example, and the role of comparable heights. |
