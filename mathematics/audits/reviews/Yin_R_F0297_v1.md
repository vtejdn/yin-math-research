---
author: Yin
---

# Review of dense polynomial spectral cuts of prescribed trace

## Finding

At 2026-11-14T15:59 UTC a reviewer outside proof development independently checked the [fixed candidate of 2026-11-14T15:55](../../claims/Yin_C_F0288_v1.md#decision-candidate), its complete argument and its eight declared direct dependencies at their points of use.
The reviewer received the fixed material and scope without exploration notes, development dialogue, author explanations or previous findings on this candidate.
The proof establishes (1) and (2), both local unboundedness assertions and the category conclusion at the stated scopes.

The omitted coordinate has an atom-free law, so two independent draws are almost surely distinct.
Fubini then gives a direction in which their real projections almost surely differ, and a quantile in that direction supplies the injective \(h\) for every \(0<t<1\).
On the image of \(1_{(-\infty,0)}(h)H\) under \((a^*)^{-1}\), the quadratic form of \(aha^*\) is strictly negative on every nonzero vector.
This image is closed because the map is invertible.
Its range projection is equivalent to the original negative projection and meets the nonnegative spectral space trivially.
The projection dimension inequality and the inverse congruence give equality of the negative traces without a gap in either spectrum.

The product rule factors \(Dp\) as \(A\cdot p+p\cdot B\), placing the right and left spectral variables on \(A\) and \(B\), respectively.
On close same-sign pairs the mean-value estimate for the arctangent ramp uses \(\sup_x |xf_\epsilon'(x)|\le 1/(2\pi)\).
On the remaining pairs the bound by the oscillation of the ramp is uniform after multiplication by the endpoint variable.
The limiting multipliers vanish on the nonzero same-sign quadrants, including their diagonals, and have absolute value at most one on opposite-sign pairs.
The zero axes carry no outer spectral projection because \(p\) is injective.
Strong convergence on \(A,B\) therefore gives the coefficient one in (1).
Polynomial approximation in \(C^1\) followed by a diagonal choice supplies common bounded core approximants for the two coarse graphs.
Slicing gives both forward graph limits, and the identities for the adjoints use the opposite slices and left multiplication of the vacua \(\xi,\xi^*\) by those same approximants.
Bounded strong convergence on \(H\) gives convergence of these products.
For each fixed cutoff radius normality identifies its weak limit with the slice of the inner multiplier applied to the coarse graph value.
The inner spectral measure on a simple tensor is a product of measures absolutely continuous with respect to the atom-free marginal, hence gives zero mass to its diagonal.
Density and contractivity give strong convergence of the inner multipliers to the identity on the entire coarse correspondence.

Factoriality and equality of the complementary traces allow the addition of two partial isometries to obtain a unitary conjugating the original negative projection to an arbitrary target.
I checked Corollary 2.4.11 on printed p. 39 (PDF p. 45) and Theorem 2.3.1 on printed p. 34 (PDF p. 40) in the retained undated 338-page Anantharaman–Popa draft.
I accept their statements and hypotheses for projection comparison in a factor with faithful tracial state and bounded strong approximation from the generating starred algebra, respectively.
The original proofs of these two established inputs were outside the review scope.
Approximation of a bounded selfadjoint logarithm, followed by exponentiation and rational approximation of finitely many coefficients, yields strongly-star convergent approximants within \(1/(n+2)\) in operator norm of exact unitaries.
The norm and inverse norm bounds of two follow from this last error.
For the resulting uniformly bounded selfadjoint congruences, a continuous cutoff of \([-2\eta,2\eta]\) controlling the ramp error tends to zero on the limiting operator's vectors, because its kernel is zero.
This proves density for the same \(h\) throughout the layer.

Weak closedness of each graph and weak compactness of bounded output balls pass bounds from \(Q\) to a whole relative patch or the full layer.
When the core bound is finite, bounded strong approximation from its unit ball gives the lower inequality \(b_D\le a_D\).
The fixed-trace estimate for \(T1=0\) gives the upper constant \(4\max\{(1-m)^{-1},(2m)^{-1}\}\), including \(t=1/2\).
The same patch theorem gives local unboundedness for an infinite slice cost.
The two finite forward costs give both full domains at the chosen coordinate by the opposite-slice adjoint identity.
For an unsliced graph, a patch bound would give a global core bound, also for marginal polynomial contractions.
On that core the two divided differences have equal absolute values.
Passing to marginal Borel signs by bounded approximation and Fatou, then averaging independent signs on dyadic cells, gives \(2\iint_{z\ne w}|z-w|^{-2}\,d\mu(z)d\mu(w)<\infty\).
The cells separate every distinct pair in the limit, and the planar covering estimate gives a lower bound of order \(r^2\) on the mass of off-diagonal pairs within \(r\).
Layer integration contradicts the displayed finiteness for every such marginal.

For each nonzero finite-dimensional centered space the top quantile projection of every unit vector has strictly positive pairing, since equality of the two ordered conditional means forces a scalar.
Compactness gives a positive lower bound for the supremal pairing over the unit sphere.
The corner projections in the argument have equal unnormalized traces \(\lambda t(1-t)\).
Exchanging them keeps exact trace, changes squared distance by \(2\lambda t(1-t)\), and approaches \((1-\lambda)e_0+\lambda t1\) ultraweakly.
The resulting strict gap is uniform on the sphere, so each neighborhood meets the complement of the closed maximizing set.
For a nonscalar represented polynomial the positive-part trace bound also covers arbitrary subprojections of its threshold eigenspace, since those contribute zero to the threshold-shifted pairing.
The represented centered space at each fixed degree is finite-dimensional, and scalar strict cuts miss every interior trace layer.
Countable union now gives the claimed meagreness even for the general diffuse finite algebra.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0288_v1.md#decision-candidate) | Full candidate fixed on 2026-11-14T15:55, including all eight declared direct dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0288_v1.md#statement) | Every exact-trace cut, both graph orientations, quantitative norm tests and local divergence, and the meagreness assertion with threshold eigenspaces. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0288_v1.md#argument) | All four sections from the omitted quantile construction to the countable union of nowhere dense maximizing sets. |
| [Finding](#finding) | [Normal starred symbols](../../claims/Yin_C_F0076_v1.md#statement) | Marginal diffuseness, omitted generators and adjoints, both closable coarse graphs, vacua and marginal divided differences. |
| [Finding](#finding) | [Factoriality](../../claims/Yin_C_F0202_v1.md#statement) | Applicability to at least two normal generators under the actual starred hypothesis. |
| [Finding](#finding) | [Projection comparison in the inspected edition](../literature/AP18/Yin_U004.md#ap18-u004) | Corollary 2.4.11, printed p. 39, PDF p. 45, equivalence of two projections of equal trace in a factor with faithful tracial state. |
| [Finding](#finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Theorem 2.3.1, printed p. 34, PDF p. 40, bounded strong approximation from the starred algebra including its selfadjoint part. |
| [Finding](#finding) | [Fixed-trace theorem](../../claims/Yin_C_F0282_v1.md#statement) | Diffuse corners, projection dimensions, bounded normal cutoffs in both orientations, closed Hilbert graph sublevels, layer constant and bounded-patch implication. |
| [Finding](#finding) | [Critical planar energy](../../claims/Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Cauchy–Schwarz on a planar grid and integration of the diffuse off-diagonal mass lower bound. |
| [Finding](#finding) | [Polynomial adjoints](../../claims/Yin_C_F0271_v1.md#exact-energy-and-affine-line-rigidity) | Vacuum and opposite-slice formulas on the core in the two orientations. |
| [Finding](#finding) | [Normal domain comparison](../../claims/Yin_C_F0075_v1.md#statement) | Finite forward costs in both orientations imply both bounded-vector domain inclusions at the selected coordinate. |
