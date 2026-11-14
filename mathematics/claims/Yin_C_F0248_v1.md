---
author: Yin
---

# Canonical domains on finite planar networks of regular arcs

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite von Neumann algebra with faithful normal probability trace \(\tau\), satisfying the [actual starred ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Assume the spectrum of the distinguished coordinate \(Z=X_i\) is contained in a finite planar network with the following geometry.

* The edges are compact regular injectively parametrized \(C^2\) arcs with nonvanishing derivative up to the endpoints.
  Their relative interiors are pairwise disjoint, and distinct edges intersect only at common endpoints.
* At each vertex the outgoing unit tangent vectors of its incident ends are pairwise distinct.
  Opposite tangent vectors are allowed.

A finite subdivision may be made before imposing these hypotheses.
The spectrum may occupy an arbitrary closed subset of the network.
The hypotheses include every finite union of compact straight segments, with collinear overlaps merged and crossings subdivided, and include networks containing cycles.
There is no requirement of joint independence or geometric assumption on the spectra of the omitted coordinates.

Write \(P=\mathbb C\langle X,X^*\rangle\), \(\delta=\delta_i\), \(C=\mathrm{id}\otimes\tau\), \(H=L^2(M,\tau)\), and let \(E_0 p=C\delta p\) on \(P\Omega\), \(\Omega=1\).
There is a finite constant \(B\) for this coordinate and law such that
\[
           \sum_k\|E_0p_k\|_2^2\le B^2\Big\|\sum_k p_k^*p_k\Big\|
               \qquad(p_k\in P,\ \text{finite columns}).                    \tag{1}
\]
The adjoint tuple also has finite right column cost at the distinguished coordinate.
The original canonical closure and its adjoint have \(M\Omega\) in both domains, and \(-\overline E_0\) satisfies the generator-first strong commutators at \(i\).
Consequently \(\mathsf A\Rightarrow\mathsf S\) when each coordinate has such a network carrier.

## Argument

### A finite subdivision admitting pairwise graph charts

In each regular arc use arclength, so the outgoing tangent at a vertex means the derivative along that end away from the vertex.
For two distinct unit tangents \(v,w\) the unit direction \(d=(v-w)/|v-w|\) has \(d\cdot v>0>d\cdot w\), where the dot denotes the real Euclidean inner product on the plane.
This remains true on a sufficiently short initial portion of both ends by continuity of the derivatives.
There are finitely many incident pairs.
One can therefore choose a short end piece at each original end on which all the required individual projection inequalities hold with a positive lower bound in magnitude.
Choose the pieces disjoint in the interiors of each old edge, leaving a nonempty middle part.
On each such middle part subdivide into finitely many sufficiently short pieces, using uniform continuity of the unit tangent so that its variation in direction on any middle piece is less than \(1/4\) in Euclidean norm.
Shorten the original end pieces first to meet this same single-piece condition on them.
At each added vertex inside an original edge a projection onto its tangent direction is strictly monotone with derivative bounded away from zero on the two adjacent pieces in their common arclength orientation.
Each single piece also admits such a projection.
At the original vertices use the directions already chosen separately for each incident pair.
This subdivision ensures that neighboring pieces share at most one vertex, including when two original edges joined the same two vertices.

For a single piece or two pieces incident at one vertex, this gives a translation and rotation in which the chosen piece or pair is represented over one real interval \(J\) as \(s+i g(s)\).
In the pair case both parameter spans include the common projected vertex and otherwise lie on opposite sides of it.
Each inverse projection chart is \(C^2\) up to its endpoints, by its derivative lower bound.
Thus \(g\) is piecewise \(C^2\) on \(J\), continuous through a common vertex, and its slope has finite variation including the possible jump there.
In the original coordinates write the chart as
\[
                   h_0(s)=a+\omega(s+i g(s)),\qquad |\omega|=1.            \tag{2}
\]
Two distinct pieces which have no common vertex are disjoint compact sets and hence have positive distance.
Every ordered pair of pieces is now either a same-piece or incident chart pair, or a pair at positive distance.

For straight segments, collinear unions split at finitely many original endpoints and the different supporting lines meet in at most one point each.
Splitting at their actual intersections and using disjoint subsegments on each line gives the required edges.
Distinct incident outgoing rays are then distinct unit directions.
Isolated points can be ignored by diffuse spectral law, and polygonal cycles are covered by the same subdivision.
A regular simple closed curve may likewise be subdivided at distinct points to fit the edge convention.

### A real parameter for a selected chart

Put \(N=W^*(Z)\), and denote the spectral law of \(Z\) by \(\mu\).
It is diffuse under actual ACSY. [Forced normal derivatives](Yin_C_F0076_v1.md#statement)
Assign to each open edge piece its Borel spectral projection in \(N\).
The vertices of the subdivision have zero spectral projections, so these projections form a finite partition of the identity.
Ignore zero projections.

Fix for now a single piece or one incident pair and use its chart \(J\) from (2).
Assign each remaining piece a distinct compact real parameter interval of its arclength, positively separated from \(J\) and from all the other new intervals.
On these intervals use an arclength parametrization.
On the resulting finite union \(\mathcal I\) of intervals, define \(h:\mathcal I\to\mathbb C\) by the chosen parametrizations, including \(h=h_0\) on \(J\).
It is Lipschitz with some finite constant \(L\), by the derivative bounds within each interval and positive separation between distinct intervals.
Linear interpolation on the intervening gaps gives a Lipschitz extension to their convex hull.
Its restriction to the interiors of the individual pieces, with their parameter endpoints removed, is injective with Borel inverse there.
Two different intervals may send endpoints to the same point of the network, but the removed finitely many vertices carry no mass.
Define \(S=h^{-1}(Z)\) with arbitrary bounded Borel values on vertices.
It is selfadjoint, \(W^*(S)=N\), \(h(S)=Z\), and its law \(\lambda\) is diffuse.

Let \(\xi=\delta^*(1\otimes1)\), \(\xi_N=\mathbb E_N\xi\).
The real parameter law has an \(L^3(ds)\) density.
In fact for an equal-mesh interval partition of the convex hull, intersect each cell with the union of the open parameter pieces.
The associated spectral projection is the original \(Z\) projection of the Borel image of that intersection.
That image lies in a disk of radius \(L\ell\), where \(\ell\) is the mesh, using the same extension of \(h\) on the gaps.
The [packing inequality for positive weights](Yin_C_F0233_v1.md#statement), part 1 with separate centers, therefore gives
\[
                         \sum_A\lambda(A)^3/\ell^2
                           \le C_0 L^2\|\xi_N\|_2^2.                        \tag{3}
\]
The associated dyadic histograms are bounded in \(L^3\) and converge against continuous tests to \(\lambda\), so weak compactness gives the claim.
The [scalar graph criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) applied to the identity real graph now gives an actual scalar vacuum for \(S\).

Replace \(Z\) by \(S\) in the generating tuple and denote its represented starred core by \(P_S\).
The [invariant liberation and inverse-gap criterion](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) applies to this conull Borel relabelling.
More explicitly, the distinguished liberation vacuum \(\eta\) stays the same, because the distinguished marginal algebra and all omitted marginal algebras are unchanged.
If \(\nu\) is its joint left-right measure in the \(S\) parameter, its push-forward under \((h,h)\) is the original measure in \(Z\).
Since \(|h(s)-h(t)|\le L|s-t|\) and conull injectivity holds for the two spectral legs, one has
\[
            \int_{s\ne t}|s-t|^{-2}\,d\nu(s,t)
            \le L^2\int_{h(s)\ne h(t)} |h(s)-h(t)|^{-2}\,d\nu(s,t)<\infty .
\]
The final integral is finite by the [old actual inverse-gap identity](Yin_C_F0238_v1.md#statement).
At each omitted coordinate its scalar law and inverse-gap integral remain unchanged, again by invariance.
The parameter tuple thus has full actual ACSY.
Let \(\delta_S\) be its distinguished derivation.
The parameter and even its joint vacuum may change from one chart to the next.

### Restricting the graph kernel on the parameter core

Extend \(g\) from \(J\) to the whole parameter hull by straight lines using its one-sided endpoint slopes.
Its derivative still has bounded variation.
Put \(H_0(s)=s+i g(s)\) for this extended graph and \(k(s,t)=(s-t)/(H_0(s)-H_0(t))\) off the diagonal, setting \(k=0\) on the diagonal.
It is bounded by one and symmetric in \(s,t\).
On \(P_S\), \(\theta=I_k\delta_S\) is an outer derivation since the marginal inner calculus commutes with the outer actions.
Here \(I_{u\otimes v}(a\otimes b)=au\otimes vb\), extended by the inner marginal spectral calculus.
Equation (9) of the [BV graph column estimate on the old core](Yin_C_F0246_v1.md#integration-over-vertices-and-the-target-mixed-core) gives \(c(C\theta)<\infty\), where \(c\) denotes the optimal bound for finite columns.
It also applies to the conjugate graph with symbol \(\bar k\).
The old derivation \(\delta_S\) is real and \(k\) is symmetric, so
\[
       (\tau\otimes\mathrm{id})\theta(p)
           =\left(C I_{\bar k}\delta_S(p^*)\right)^* .
\]
Indeed flip-adjoint interchanges the inner spectral variables and conjugates the symbol.
Hence both slices of \(\theta\) have finite operator-norm-to-Hilbert-norm bounds on \(P_S\).
The [two-slice theorem](Yin_C_F0072_v1.md#statement), parts A and B, gives an actual vacuum for \(\theta\) and a closable right slice \(G=C\theta\).

For two bounded Borel marginal projections \(e,f\), the product rule gives on \(P_S\)
\[
                    C I_{e\otimes f}\theta(p)
                       =(\bar G(p f)-p\bar G(f))e ,                        \tag{4}
\]
with column cost at most \(2c(G)\).
Here is the domain argument for these projections.
The [bounded measurable product-identity proof](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice), equations (2)–(3), uses only the original column bound, closability of \(G\), the product rule and traciality.
Matrix Kaplansky approximation and weak closedness of its graph extend the same column bound to columns of bounded elements.
On bounded balls, strong-star convergence of inputs gives weak convergence of their images under \(\bar G\), since every weak cluster point is the unique graph value.
Thus the trace product identity for marginal polynomials in place of \(f\) passes to bounded strong-star approximants to \(f\), whose inner actions on the fixed \(\theta(p)\) converge strongly.
Applying the extended column bound to \(p_k f\) and \(\sum_k\|p_k\bar G(f)\|_2^2\le\|\sum_k p_k^*p_k\|\|\bar G(f)\|_2^2\) gives (4)'s bound.

Let \(e,f\) now be the projections of the selected ordered pieces, taking \(f=e\) in the single-piece case.
On their spectral rectangle,
\[
                 \frac{s-t}{h(s)-h(t)}=\bar\omega\,k(s,t)
                  \quad\text{for }s\ne t .                                  \tag{5}
\]
Consequently \(C I_{\bar\omega\,1_e(s)1_f(t)k(s,t)}\delta_S\) has finite right column cost on the parameter core by (4).
This argument uses the extended BV graph only for its old-core estimate.
The actual map from \(S\) to \(Z\) remains the Lipschitz map \(h\) on all pieces.

### Returning the localized derivation to the original tuple

The [norm-controlled column approximation on the relabelled core](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) applies to the bounded Lipschitz \(h\) on the parameter carrier.
In particular \(Z=h(S),Z^*\) and the mixed original words have bounded graph approximants for \(\delta_S\).
This step uses Lipschitz bounds on \(h,\bar h\), regardless of the behavior of the inverse between different intervals.
For any finite \(P\)-column with norm at most one, the same approximation supplies columns in \(P_S\) with converging coarse derivatives and limit superior of column norms at most \(1+\varepsilon\), for every \(\varepsilon>0\).
The truncation of a column by a smooth function of its squared modulus used there takes place before insertion of any ratio kernel.

On \(P\), the two localized outer derivations satisfy
\[
                   I_{\bar\omega\,1_e\otimes1_f\, k}\bar\delta_S
                       = I_{e\otimes f}\delta .                            \tag{6}
\]
To verify (6), check the generators.
Indeed \(\bar\delta_S Z=(h(s)-h(t))/(s-t)\) and \(\bar\delta_S Z^*=(\bar h(s)-\bar h(t))/(s-t)\) by that graph approximation.
Insertion of the bounded symbol on the left gives \(1_e\otimes1_f\) at \(Z\) by (5), and the same rectangle times \((\bar h(s)-\bar h(t))/(h(s)-h(t))\) at \(Z^*\).
These are precisely the localized values of the original actual derivation by the [forced normal phase](Yin_C_F0076_v1.md#statement).
Both sides kill the omitted starred letters, and the outer product rule proves (6).
A diagonal set has zero coarse spectral projection by diffuseness and the [coarse product measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core).
In particular (6) requires the inverse secant only on the selected rectangle.
Since its extended symbol is bounded, (4)–(6) and the approximating column norms give the desired localized estimate on \(P\) after \(\varepsilon\downarrow0\).

For two pieces at positive distance, use directly the partial liberation \(\gamma=I_{z-w}\delta\) for the original \(Z\).
Its rectangle slice \(C I_{e\otimes f}\gamma\) has finite column cost by the [measurable liberation block estimate](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block).
There are smooth compact cutoffs on the plane equal to one on the respective closed pieces and supported at positive distance from one another.
Their product times \(1/(z-w)\) extends smoothly with compact support on the product of the two planes.
Periodizing in a sufficiently large box and applying \((1-\Delta)^3\) gives an absolutely summable Fourier expansion in four real variables, since \(\sum_{m\in\mathbb Z^4}(1+|m|^2)^{-3}<\infty\).
Its characters separate into continuous marginal unitaries.
For the rectangle-inserted liberation, each such character after the right trace costs at most twice the original rectangle column norm by the [separated multiplier identity](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm).
Thus its sum on the rectangle supplies \(C I_{e\otimes f}\delta\) with finite cost, using \(\gamma=I_{z-w}\delta\).
The cutoffs concern only this pair and may intersect other pieces.

Summing over all ordered pairs of the finite spectral partition gives (1).
Conjugating the network reflects its tangents and preserves the geometry.
The adjoint tuple is actual by the [flip-adjoint companion](Yin_C_F0076_v1.md#statement), so the same proof bounds its right slice and hence the original left slice on single inputs.
The two-slice theorem, part B, gives both original canonical bounded-vector domains.
The identity \(E_0(X_jp)-X_jE_0(p)=\delta_{ij}\tau(p)1\) extends to the closure by graph approximation and gives the indicated generator-first commutators for the negative closure.

### Tangency at a vertex

If two outgoing unit tangents agree, no linear projection can have nonzero derivatives of opposite signs there.
For example the arcs \(z_\pm(x)=x\pm i x^2\), \(0\le x\le1\), meet with the same outgoing unit tangent.
Assigning separate signed arclength parameters from that vertex to the two branches gives a parameter difference comparable to \(2x\) for \(z_+(x),z_-(x)\), while their planar separation is \(2x^2\).
The corresponding local inverse secant is unbounded.
The proof above supplies no two-branch bound at such a tangency, and the example does not decide the domain implication for those carriers.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:10 |
| status | open |
| reason | The finite-network theorem, pair-dependent real charts, localization on the original mixed core and precise scope at vertices are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Distinguished right columns, both original canonical bounded-vector domains and the full-tuple consequence on finite regular networks, including finite segment configurations. |
| argument | [Argument](#argument) | Tangent separation, real parameter vacuum on each chosen chart, restriction of a BV graph on its old core, original mixed-core transport on a rectangle, positive-distance pairs and the same-tangent limitation. |
| dependency | [Normal generator formulas](Yin_C_F0076_v1.md#statement) | Part 1, diffuse marginals, the distinguished star phase, vanishing omitted star values, and the actual flip-adjoint tuple. |
| dependency | [Scalar packing](Yin_C_F0233_v1.md#statement) | Part 1 for the disjoint Borel preimages of a parameter interval partition and separate ambient disk centers. |
| dependency | [Inverse-gap recovery](Yin_C_F0238_v1.md#statement) | The finite original liberation inverse-gap energy and the actual conjugate-variable criterion for the parameter tuple. |
| dependency | [Coarse product measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Domination of coarse spectral measures by the product law, including the marginal diagonal. |
| dependency | [Invariant actual liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Conull Borel parameter relabelling at the distinguished and omitted coordinates preserves the actual liberation vacuum and pushes forward its spectral measures. |
| dependency | [Scalar real-parameter criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Actual vacuum at the identity real graph of a compactly supported \(L^3\) probability density. |
| dependency | [BV graph on the reference core](Yin_C_F0246_v1.md#integration-over-vertices-and-the-target-mixed-core) | Equation (9) before target-core transfer, on the selfadjoint parameter tuple and for both the extended graph and its reflection. |
| dependency | [Bounded measurable product identity](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Equations (2)–(3), using the column and closability hypotheses for the auxiliary outer derivation and its right slice. |
| dependency | [Relabelled mixed-core approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Graph approximation for forward Lipschitz functions of the real parameter and column norm restoration before inserting a bounded localized kernel. |
| dependency | [Measurable liberation rectangles](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (6) at two disjoint spectral projections for positive-distance pieces. |
| dependency | [Separated Fourier multipliers](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | The right-trace product identity at continuous marginal unitaries and their column norm bound on the localized outer derivation. |
| dependency | [Canonical domains from both slices](Yin_C_F0072_v1.md#statement) | Parts A and B for closability and vacuum of the auxiliary weighted derivation and the two bounded-vector domains of the original canonical operator. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:16 |
| status | proved |
| reason | Adopt the finite regular-network theorem after independent review of its pairwise charts and localized original-core argument. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Distinguished right columns, both original canonical bounded-vector domains and the full-tuple consequence on finite regular networks, including finite segment configurations. |
| argument | [Argument](#argument) | Tangent separation, real parameter vacuum on each chosen chart, restriction of a BV graph on its old core, original mixed-core transport on a rectangle, positive-distance pairs and the same-tangent limitation. |
| dependency | [Normal generator formulas](Yin_C_F0076_v1.md#statement) | Part 1, diffuse marginals, the distinguished star phase, vanishing omitted star values, and the actual flip-adjoint tuple. |
| dependency | [Scalar packing](Yin_C_F0233_v1.md#statement) | Part 1 for the disjoint Borel preimages of a parameter interval partition and separate ambient disk centers. |
| dependency | [Inverse-gap recovery](Yin_C_F0238_v1.md#statement) | The finite original liberation inverse-gap energy and the actual conjugate-variable criterion for the parameter tuple. |
| dependency | [Coarse product measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Domination of coarse spectral measures by the product law, including the marginal diagonal. |
| dependency | [Invariant actual liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Conull Borel parameter relabelling at the distinguished and omitted coordinates preserves the actual liberation vacuum and pushes forward its spectral measures. |
| dependency | [Scalar real-parameter criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Actual vacuum at the identity real graph of a compactly supported \(L^3\) probability density. |
| dependency | [BV graph on the reference core](Yin_C_F0246_v1.md#integration-over-vertices-and-the-target-mixed-core) | Equation (9) before target-core transfer, on the selfadjoint parameter tuple and for both the extended graph and its reflection. |
| dependency | [Bounded measurable product identity](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Equations (2)–(3), using the column and closability hypotheses for the auxiliary outer derivation and its right slice. |
| dependency | [Relabelled mixed-core approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Graph approximation for forward Lipschitz functions of the real parameter and column norm restoration before inserting a bounded localized kernel. |
| dependency | [Measurable liberation rectangles](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (6) at two disjoint spectral projections for positive-distance pieces. |
| dependency | [Separated Fourier multipliers](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | The right-trace product identity at continuous marginal unitaries and their column norm bound on the localized outer derivation. |
| dependency | [Canonical domains from both slices](Yin_C_F0072_v1.md#statement) | Parts A and B for closability and vacuum of the auxiliary weighted derivation and the two bounded-vector domains of the original canonical operator. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0257_v1.md#finding) | All finite segment networks, the distinct-outgoing-tangent condition for regular arcs, both canonical domains, and the limits of the calculation at tangency. |
