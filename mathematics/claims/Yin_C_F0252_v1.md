---
author: Yin
---

# Canonical domains for two graphs with a closed set of tangential contacts

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_n)\) be bounded normal generators of a finite von Neumann algebra with faithful normal probability trace \(\tau\) satisfying the [actual starred ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Suppose that in fixed translated and rotated plane coordinates the spectrum of \(Z=X_i\) is contained in the union of the two graphs \(x+i f_j(x)\), \(j=1,2\), on a compact nondegenerate real interval \(I\).
Assume \(f_1,f_2\in C^{1,1}(I;\mathbb R)\), so their derivatives are Lipschitz up to the endpoints.
The hypotheses include compact \(C^2\) graphs.
On the closed contact set \(F=\{x\in I:f_1(x)=f_2(x)\}\) require
\[
                          f_1'(x)=f_2'(x)\qquad(x\in F),                  \tag{1}
\]
using one-sided derivatives at endpoints.
There is no restriction on the number of components of \(F\) or on its mass for the distinguished spectral law.

On the represented starred polynomial core \(P\) of the original tuple the distinguished right slice \(E=(\mathrm{id}\otimes\tau)\delta_i\) satisfies
\[
         \sum_k\|Ep_k\|_2^2\le B^2\Big\|\sum_kp_k^*p_k\Big\|
                          \qquad (p_k\in P,\ \text{finite columns})        \tag{2}
\]
for a finite constant \(B\) depending on the law and graphs.
The adjoint tuple has finite right column cost at its distinguished coordinate.
On \(H=L^2(M,\tau)\) with \(\Omega=1\), the closure of the original \(E\) and its actual Hilbert adjoint both have domains containing \(M\Omega\), and the negative closure supplies the generator-first strong commutator at \(i\).
The other coordinates may have arbitrary correlations and spectra.
When each coordinate has such a carrier, actual ACSY implies the full strong dual condition for the tuple.

## Argument

### Upper and lower graphs

Translate the real parameter interval to \(I=[0,R]\).
Write \(g=(f_1+f_2)/2\), \(k=(f_1-f_2)/2\) and \(d=|k|\).
By (1), \(k=k'=0\) wherever \(d=0\).
Consequently \(d\) is differentiable there with derivative zero, and off \(F\) its derivative is \(\operatorname{sign}(k)k'\).
This derivative is Lipschitz with constant at most \(\operatorname{Lip}(k')\).
For same-sign endpoints this follows from the formula for the derivative and the Lipschitz bound for \(k'\).
For endpoints of opposite signs, or when one lies in \(F\), use an intervening zero where \(k'=0\) and add the two distance bounds.
Thus the upper and lower heights \(g+d\) and \(g-d\) are \(C^{1,1}\) on all of \(I\) and their derivatives have bounded variation.

Use the full upper branch \(U\), including its points over \(F\), and the lower branch \(L\) only over \(I\setminus F\).
Their images are disjoint Borel sets giving marginal spectral projections \(e_U+e_L=1\).
For \(F=I\) there is only the single upper graph and the same-branch argument below applies.
For \(F=\varnothing\) the two compact graphs have positive separation, so each same-branch argument and the [positive-distance cross estimate](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) suffice.
In the rest of the proof take \(F\ne\varnothing,I\).
The coding and estimates below use the sorted upper and lower heights even if \(f_1-f_2\) changes sign at contacts.

### The real parameter on the complementary intervals and the contact set

On every component of \(I\setminus F\) choose one interior point.
Starting there in each direction, take consecutive steps of length \(c\,d(x)\) from the current point \(x\).
Choose one \(c>0\) with \(c\operatorname{Lip}(d)<1/4\).
A step towards a zero endpoint stays strictly inside the component, since \(d(x)\le\operatorname{Lip}(d)\operatorname{dist}(x,F)\).
The successive points tend to the zero endpoint, because an interior limit with positive height would give steps bounded away from zero.
A step towards a nonzero endpoint of \(I\) is truncated at that endpoint if it reaches or passes it.
It reaches that endpoint in finitely many steps since the height has a positive lower bound in its vicinity.
There are at most two such exterior ends.
The resulting nondegenerate closed tiles \([a,b]\) cover \(I\setminus F\), meeting only at adjacent ends.
Their lengths \(\ell=b-a\) satisfy uniform bounds
\[
                         c_1 d(x)\le\ell\le c_2 d(x)
                                  \qquad(x\in[a,b])                       \tag{3}
\]
for constants depending on the construction.
For a full step, the variation of \(d\) from its value at the starting point is at most \(c\operatorname{Lip}(d)\) times that value.
Any final shortened step has positive length and positive minimum and finite maximum of \(d\) on its closure, so these at most two tiles only change the constants.
All complement components and tiles together are countable since disjoint open intervals in the line are countable.

For \(a<x<b\) encode the upper and lower points on this tile by
\[
       F_U(x)=10a+\ell+(x-a),\qquad F_L(x)=10a+4\ell+(x-a).              \tag{4}
\]
For every \(x\in F\) use the single upper label \(F_U(x)=10x\).
This assignment retains every point of the contact set, including when it carries positive spectral mass.
Delete from the two noncontact branches only the countable tile endpoints, which have zero spectral projection by [diffuseness](Yin_C_F0076_v1.md#statement).
All filled parameter intervals are disjoint from one another and from \(10F\).
The assignment thus has a bounded Borel inverse on its assigned image.
The errors \(\epsilon_U=F_U-10x,\ \epsilon_L=F_L-10x\) obey \(|\epsilon_j(x)|\le C_1d(x)\) by (3), including \(\epsilon_U=0\) on \(F\).

Here is a Lipschitz forward map \(h:[0,10R]\to\mathbb C\) agreeing with the decoding.
Send \(10x\), \(x\in F\), to \(x+i g(x)\).
On a tile put these same midline values at the two outer parameters \(10a,10b\), put the two graph parametrizations on the closed intervals filled by (4), and interpolate linearly on the three gaps.
These gaps have lengths \(\ell,2\ell,5\ell\).
Their planar endpoint separations are bounded by \(C_2\ell\), since horizontal changes are at most \(\ell\), midline changes are at most \(\operatorname{Lip}(g)\ell\), and the two heights obey (3).
Together with the uniform Lipschitz bounds on the filled intervals this gives a uniform Lipschitz bound on each whole tile.
On one component the bound extends through the shared tile endpoints and to its limiting ends by continuity, since the midline is continuous and both the tile diameters and heights tend to zero at a zero end.
For arbitrary two parameter points with \(10F\) between them, use the first and last points of \(10F\) in the intervening interval.
Each outer segment has the component bound, and the middle endpoint values are those of the single Lipschitz midline on \(10F\).
The triangle inequality proves the global Lipschitz bound without any assumption that \(F\) has measure zero.

Define \(S\) by the bounded Borel coding of \(Z\) just constructed, assigning arbitrary real values in \([0,10R]\) at the deleted points.
Then \(S=S^*\), \(W^*(S)=W^*(Z)\) and \(h(S)=Z\).
In the original plane axes compose the decoder with the fixed translation and rotation.
In applying the [actual real parameter construction](Yin_C_F0248_v2.md#real-parameters-near-a-tangential-contact), the relevant hypotheses are conull injectivity and the forward Lipschitz bound.
Indeed each equal-mesh cell in the parameter hull, intersected with the assigned image, has a disjoint old spectral projection and its planar image has diameter at most \(\operatorname{Lip}(h)\) times the mesh.
The [marginal packing estimate](Yin_C_F0233_v1.md#statement) bounds the \(L^3\) norms of the parameter histograms uniformly.
Their weak limits identify an \(L^3\) density for the parameter law, and the [scalar real-graph criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) gives its actual scalar vacuum.
The [invariance of liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) under a conull Borel change identifies the distinguished liberation measure under the decoding.
Its inverse real-gap energy is finite since \(|h(s)-h(t)|\le\operatorname{Lip}(h)|s-t|\) and the old inverse planar-gap energy is finite.
The [inverse-gap criterion](Yin_C_F0238_v1.md#statement) supplies the new distinguished vacuum, and the omitted coordinates retain their original scalar vacua and liberation energies.
Thus the tuple replacing \(Z\) by \(S\) has actual ACSY and its distinguished right slice has finite column cost on its full mixed core \(P_S\). [Real-coordinate column](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column)

### Localizing the cross-branch multiplier in the horizontal variable

For \(x\) on \(U\) and \(y\) on \(L\), let \(v=x-y,\ d_x=d(x),\ d_y=d(y),\ w=d_x+d_y\) and
\[
 G(x,y)=\int_0^1g'\big(\theta x+(1-\theta)y\big)\,d\theta,\quad
 D=(1+iG)v+iw,\quad
 K=\frac{F_U(x)-F_L(y)}{D}
     =\frac{10v+\epsilon_U(x)-\epsilon_L(y)}{D}.                          \tag{5}
\]
Here \(d_y>0\) and \(d_x\) can be zero.
The two planar points are always different on this cross rectangle.
We estimate the measurable Schur norm of \(K\) for the upper and lower branch measures in these real labels.

The function \(\sqrt d\) is Lipschitz on \(I\).
For a direct justification extend \(d\) nonnegatively to a slightly larger interval, as a \(C^{1,1}\) function.
At a zero endpoint use the constant zero extension since \(d'=0\) there, and at a positive endpoint use a linear extension over a sufficiently short interval on which the extension remains positive.
Write \(M\) for a Lipschitz constant of the extended derivative.
With a fixed positive collar width available, choose \(M_1\ge\max(1,M)\) large enough that the test point \(x-d'(x)/M_1\) stays in the extended interval for every \(x\in I\).
Taylor's upper inequality and nonnegativity give \(0\le d(x)-|d'(x)|^2/(2M_1)\).
Consequently \(\sqrt d\) has uniformly bounded derivative on \(\{d>0\}\), extends continuously to zero on \(F\), and is Lipschitz across different components by splitting at intervening zeros.
Fix \(L_0\ge1\) bounding its Lipschitz constant.

Partition \(I\) into finitely many equal-mesh Borel intervals, using half-open cells except for the final endpoint.
Use closures for the distance tests.
The mesh can be chosen as small as needed below.
Nonneighboring cells have positive horizontal separation, hence give positive-distance cross rectangles.
For a same-cell or neighboring-cell pair let \(J\) be the closed hull of the two cells.
If \(J\cap F=\varnothing\), its minimum height is positive, and the upper and lower graphs over this hull are disjoint compact sets.
In all these positive-distance pairs the smooth cutoff representation of \(1/(z-z')\) has finite Schur norm, as in the [positive-distance rectangle proof](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple).
Multiplication by the difference of the bounded labels \(F_U(x)-F_L(y)\) preserves this bound.
We treat the finitely many remaining hulls with \(J\cap F\ne\varnothing\).
For these, \(\sup_J d\le \tfrac12\operatorname{Lip}(d')|J|^2\), by Taylor's inequality at a point of \(F\).

Freeze the midline slope at \(m=g'(x_0)\) for \(x_0\in J\), and set \(p=1+im\).
On \(J^2\) one has \(\|G-m\|_{\rm Schur}\le C_3 |J|\operatorname{Lip}(g')\).
Indeed extend \(g'\) off \(I\) by constants, multiply \(g'(\inf J+|J|t)-m\) by a fixed smooth cutoff supported in \((-1,2)\) and equal to one on \([0,1]\), and periodize.
Both its \(L^\infty\) norm and the \(L^2\) norm of its weak derivative on a fixed period are bounded by a constant times \(|J|\operatorname{Lip}(g')\).
Cauchy–Schwarz on its Fourier coefficients against \((1+n^2)^{-1/2}\) makes their absolute sum bounded by the same quantity.
The character evaluated at the rescaled convex combination \(\theta x+(1-\theta)y\) factors into unitaries on the two legs.
Integrating in \(\theta\) proves the estimate.
This is the [small-interval divided-difference estimate](Yin_C_F0248_v2.md#a-schur-bound-from-separation-in-height) applied to the slope difference from a frozen value.
When the mesh is small, \(K_0=(1+iG)^{-1}\) has Schur norm at most \(2/|p|\) on \(J^2\), by factoring out \(p\) and summing the Neumann series for \(i(G-m)/p\).

### Height decomposition with zero-height spectral mass

If \(\sup_Jd=0\) there is no lower branch in this hull.
Otherwise put \(D_*=\sup_Jd>0\), \(\delta_j=2^{-j}D_*\), and label the positive height bands by \(\delta_j/2<d\le\delta_j\).
Keep the upper zero-height set as a separate measurable set.
At comparable positive heights, meaning that the two band indices differ by at most one, put \(D_m=pv+iw\).
There is the factorization
\[
 \frac{\sqrt{d_xd_y}}{D_m}
   =\frac{-i}{p}\int_0^\infty
        \sqrt{d_x}e^{-\lambda d_x/p+i\lambda x}
        \sqrt{d_y}e^{-\lambda d_y/p-i\lambda y}\,d\lambda .               \tag{6}
\]
It follows by integration since \(\operatorname{Re}(1/p)>0\).
Each factor has \(L^2(d\lambda)\) norm \((2\operatorname{Re}(1/p))^{-1/2}\), giving a Schur norm at most \(|p|/2\) by [Hilbert-space Schur factorization](../audits/literature/AP25/Yin_U001.md#measurable-schur-factorization).
On a pair of comparable bands \(1/4\le d_x/d_y\le4\), with rectangularly bounded separated factors \(\sqrt{d_x/d_y}\) and its inverse.
Thus \(w/D_m\) and \((\epsilon_U(x)-\epsilon_L(y))/D_m\) have uniform Schur bounds, the latter by \(|\epsilon_j|\le C_1 d\).
The identity \(v/D_m=p^{-1}(1-iw/D_m)\) gives a common bound for \(v/D_m\) depending only on the slope bound.
By the horizontal mesh choice the Schur norm of \(i(G-m)v/D_m\) is at most \(1/2\), so \(D_m/D=(1+i(G-m)v/D_m)^{-1}\) is uniformly bounded in Schur norm.
Equation (5) now gives the same conclusion for \(K\) and hence for \(K-10K_0\) on these comparable rectangles.
For each of the three fixed band offsets the domain projections in the columns are disjoint, as are the range projections in the rows.
The multiplied operator on their union is the orthogonal direct sum of the multiplied blocks, with norm at most the supremum of their norm bounds times the input operator norm.
Thus each comparable offset costs a finite amount on the entire hull, also for countably many bands.

In the other rectangles let the higher positive height be in \(\delta/2<d\le\delta\) and collect all lower heights \(0\le d\le\delta/4\) present on the other leg.
Either leg may be the higher one.
This includes an upper zero height against every positive lower height, while the lower branch contains no zero height.
Writing \(b=(1/\sqrt2-1/2)/L_0>0\), the square-root Lipschitz bound gives \(|v|\ge b\sqrt\delta\).
By the [off-gap Fourier estimate](Yin_C_F0248_v2.md#a-schur-bound-from-separation-in-height) there is a symbol \(L_\delta\) equal to \(1/v\) on the rectangle and of Schur norm at most \(C_b/\sqrt\delta\).
Explicitly, rescale the function \(\chi(t)/t\) for a smooth even cutoff equal to one on \(|t|\ge1\) and vanishing near zero.
That function belongs to \(H^1(\mathbb R)\), hence has integrable Fourier transform by Cauchy–Schwarz, giving the asserted separated norm after dilation.

On the rectangle \(w\) has separated norm at most \(2\delta\).
By shrinking the horizontal mesh at the outset one ensures \(\|iK_0 wL_\delta\|_{\rm Schur}\le1/2\) for every such \(\delta\), since \(D_*\le \tfrac12\operatorname{Lip}(d')|J|^2\).
On this rectangle, (5) gives
\[
 K-10K_0
    =\big(\epsilon_U(x)-\epsilon_L(y)-10iK_0w\big)
         L_\delta\,K_0(1+iK_0w L_\delta)^{-1}.                           \tag{7}
\]
Its Schur norm is \(O(\sqrt\delta)\), because the first factor has Schur norm \(O(\delta)\) by (3)–(4), including when the height is zero.
The constants here can be chosen uniformly for all chart hulls, using \(|p|\le1+\|g'\|_\infty\).
Sum (7) in both orientations over the height levels, at total cost \(O(\sum_j\sqrt{\delta_j})<\infty\).
Adding the comparable offsets and the single baseline \(10K_0\) gives a bounded Schur symbol on the whole upper-to-lower rectangle of the selected cells.
The real partition has finitely many cell pairs, so \(K\) is a bounded measurable Schur multiplier on the full cross rectangle.
Each truncation of the height rectangles is bounded pointwise and the shell sums converge on every coarse input by domination of inner spectral measures by product law. [Coarse spectral calculus](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core)
The upper zero-height rectangles retain the whole spectral mass on \(F\) in these limits.

### Recovery on mixed words and finite columns

The cross symbol in the real labels, extended by zero off \(e_U\otimes e_L\), has a finite column bound for its insertion in \(\delta_S\) on \(P_S\) by the [measurable Schur column estimate](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice).
Pullback between the Borel-coded pieces and their actual measures preserves the multiplier estimate.
The transposed symbol has the same bound for the reversed rectangle, since the inverse divided difference is symmetric, and the reflected graphs give the corresponding adjoint estimates.

The [original-core graph transfer](Yin_C_F0248_v2.md#original-mixed-domains-and-finite-assembly) applies with this forward Lipschitz decoder.
In detail, the [mixed column graph approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) supplies \(P_S\)-columns converging in the derivation graph to each fixed \(P\)-column of norm at most one, with input norms having limit superior at most \(1+\varepsilon\).
The bounded cross symbol at \(Z\) times its forward divided difference is the rectangle indicator, and at \(Z^*\) it gives this indicator times the original phase \((\bar z-\bar w)/(z-w)\).
It kills the omitted starred letters, and the product rule gives equality to the original rectangle-inserted derivation on the whole mixed core. [Forced normal phase](Yin_C_F0076_v1.md#statement)
Translation cancels in the secant and rotation supplies its reciprocal unit scalar in the inserting symbol.
The bound passes through these graph limits and then \(\varepsilon\downarrow0\) gives both off-diagonal terms of (2).

For the two same-branch rectangles use separate interval charts and the [BV single-piece restriction](Yin_C_F0248_v1.md#restricting-the-graph-kernel-on-the-parameter-core) with its [original-core transfer](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple).
Specifically, put the full upper graph on one model interval and the lower graph over \(I\setminus F\) on a separate copy of \(I\) a positive distance away.
Extend across unassigned points on the second copy by the Lipschitz map \(x\mapsto x+i(g(x)-d(x))\), and interpolate on the separating gap.
This forward map is Lipschitz and one-to-one on the assigned set, even if both filled model intervals have images over \(F\).
The real parameter argument and the graph restrictions can therefore be applied with a piece consisting of any of the assigned Borel subsets of either interval.
Each selected single graph has slope of bounded variation by the upper and lower graph calculation, so using \(e=f=e_U\) or \(e=f=e_L\) bounds the corresponding original column.
The four rectangles sum to one on the coarse marginal square.
This proves (2).

Complex conjugation preserves (1) and exchanges the upper and lower ordering.
The argument may assign the reflected contact set to its own upper branch, since the resulting rectangle sum is again the identity.
The actual flip-adjoint derivation at the adjoint tuple gives the original left one-input bound by tracial involution. [Normal companion](Yin_C_F0076_v1.md#statement)
The [two-slice theorem](Yin_C_F0072_v1.md#statement), part B, puts every bounded vector in both the canonical closure domain and its actual adjoint domain.
Graph approximation extends \(E(X_jp)-X_jE(p)=\delta_{ij}\tau(p)1\) from the core, giving the strong commutators with the negative closure.

## Scope

The separation by height and its Schur estimate for an isolated tangential vertex are from [the finite-network theorem](Yin_C_F0248_v2.md#a-schur-bound-from-separation-in-height).
The coordinating agent proposed retaining the entire shared set on one branch and freezing a possibly nonzero midline slope.
The present construction supplies the coding and Lipschitz gluing on every complementary component, the zero-band estimates and their mixed-core use with nonzero common-set mass.
Hypothesis (1) excludes a transverse crossing even when other contacts accumulate nearby.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:41 |
| status | open |
| reason | Fix the shared-contact-set theorem, its encoding on closed sets and the full mixed-core estimates for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite right column costs in both orientations and the original bounded-vector domains for two \(C^{1,1}\) graph carriers with an arbitrary closed tangential contact set. |
| argument | [Argument](#argument) | Sorting the two graphs, real encoding retaining the common-set measure, localized height bands with slope freezing and original mixed-column recovery. |
| dependency | [Forced normal phase and companion](Yin_C_F0076_v1.md#statement) | Part 1, diffuse spectral laws, prescribed starred values, and the adjoint tuple. |
| dependency | [Positive-distance and same-branch localization](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Separated planar cutoffs, graph-restricted generator checks and the original mixed-core limit. |
| dependency | [Single-piece BV restriction](Yin_C_F0248_v1.md#restricting-the-graph-kernel-on-the-parameter-core) | Right column bound on any Borel subrectangle of one BV graph in its parameter core. |
| dependency | [Tangency real-parameter argument](Yin_C_F0248_v2.md#real-parameters-near-a-tangential-contact) | Conull Borel real encoding with forward Lipschitz map, scalar packing and liberation energy, now with every common-set label retained. |
| dependency | [Height-band estimates](Yin_C_F0248_v2.md#a-schur-bound-from-separation-in-height) | Horizontal Fourier control of a slowly varying slope after subtraction of its frozen value, and the off-gap reciprocal bound on separated-height rectangles. |
| dependency | [Tangency core transfer](Yin_C_F0248_v2.md#original-mixed-domains-and-finite-assembly) | Bounded cross kernel on a real parameter core transferred to the actual original starred-generator values and graph limits. |
| dependency | [Scalar interval packing](Yin_C_F0233_v1.md#statement) | Part 1 for disjoint preimages of equal intervals on the encoded parameter line. |
| dependency | [Scalar real graph criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Existence of the actual scalar vacuum on the compact real parameter with \(L^3\) density. |
| dependency | [Liberation under relabelling](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Invariant liberation and transport of its spectral measure at every distinguished or omitted coordinate. |
| dependency | [Inverse-gap vacuum criterion](Yin_C_F0238_v1.md#statement) | Finiteness of old inverse-gap liberation energy and recovery of an actual vacuum in the encoded parameter tuple. |
| dependency | [Coarse product measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Dominated convergence for bounded spectral symbols, including zero-height labels. |
| dependency | [Real-coordinate column](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Finite right column cost at the encoded real coordinate of an actual tuple. |
| dependency | [Measurable Schur factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001) | Hilbert-space two-leg bound for the resolvent with frozen complex slope. |
| dependency | [Old-core Schur bound](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Column estimate for an arbitrary bounded measurable Schur symbol inserted in the real distinguished derivation. |
| dependency | [Relabelled mixed-core approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Norm-controlled core columns and derivative convergence before inserting bounded localized multipliers. |
| dependency | [Canonical full domains](Yin_C_F0072_v1.md#statement) | Part B for the two original bounded-vector domains and closure of the canonical slice. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:46 |
| status | proved |
| reason | Adopt the closed tangential contact set theorem after independent review of the full mixed-core proof. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite right column costs in both orientations and the original bounded-vector domains for two \(C^{1,1}\) graph carriers with an arbitrary closed tangential contact set. |
| argument | [Argument](#argument) | Sorting the two graphs, real encoding retaining the common-set measure, localized height bands with slope freezing and original mixed-column recovery. |
| dependency | [Forced normal phase and companion](Yin_C_F0076_v1.md#statement) | Part 1, diffuse spectral laws, prescribed starred values, and the adjoint tuple. |
| dependency | [Positive-distance and same-branch localization](Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Separated planar cutoffs, graph-restricted generator checks and the original mixed-core limit. |
| dependency | [Single-piece BV restriction](Yin_C_F0248_v1.md#restricting-the-graph-kernel-on-the-parameter-core) | Right column bound on any Borel subrectangle of one BV graph in its parameter core. |
| dependency | [Tangency real-parameter argument](Yin_C_F0248_v2.md#real-parameters-near-a-tangential-contact) | Conull Borel real encoding with forward Lipschitz map, scalar packing and liberation energy, now with every common-set label retained. |
| dependency | [Height-band estimates](Yin_C_F0248_v2.md#a-schur-bound-from-separation-in-height) | Horizontal Fourier control of a slowly varying slope after subtraction of its frozen value, and the off-gap reciprocal bound on separated-height rectangles. |
| dependency | [Tangency core transfer](Yin_C_F0248_v2.md#original-mixed-domains-and-finite-assembly) | Bounded cross kernel on a real parameter core transferred to the actual original starred-generator values and graph limits. |
| dependency | [Scalar interval packing](Yin_C_F0233_v1.md#statement) | Part 1 for disjoint preimages of equal intervals on the encoded parameter line. |
| dependency | [Scalar real graph criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Existence of the actual scalar vacuum on the compact real parameter with \(L^3\) density. |
| dependency | [Liberation under relabelling](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Invariant liberation and transport of its spectral measure at every distinguished or omitted coordinate. |
| dependency | [Inverse-gap vacuum criterion](Yin_C_F0238_v1.md#statement) | Finiteness of old inverse-gap liberation energy and recovery of an actual vacuum in the encoded parameter tuple. |
| dependency | [Coarse product measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Dominated convergence for bounded spectral symbols, including zero-height labels. |
| dependency | [Real-coordinate column](Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Finite right column cost at the encoded real coordinate of an actual tuple. |
| dependency | [Measurable Schur factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001) | Hilbert-space two-leg bound for the resolvent with frozen complex slope. |
| dependency | [Old-core Schur bound](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Column estimate for an arbitrary bounded measurable Schur symbol inserted in the real distinguished derivation. |
| dependency | [Relabelled mixed-core approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Norm-controlled core columns and derivative convergence before inserting bounded localized multipliers. |
| dependency | [Canonical full domains](Yin_C_F0072_v1.md#statement) | Part B for the two original bounded-vector domains and closure of the canonical slice. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0261_v1.md#finding) | Coding of every contact, the frozen-slope factorization, zero and positive height bands, finite columns, both original bounded-vector domains and the generator-first commutator. |
