---
author: Yin
---

# Independent review of canonical domains on finite planar networks

At 2026-11-14T11:14 UTC, an agent outside development of the proof checked the [candidate fixed at 2026-11-14T11:10](../../claims/Yin_C_F0248_v1.md#decision-candidate) for Yin.
This was an initial whole-proof review based on the candidate, the Task's hypotheses and the fixed inputs listed below.
The reviewer received the assignment and the mathematical interfaces to check, with no exploration notes, development dialogue, author explanation or earlier verdict on the candidate.
The seven cited proved Claims were inspected at their points of use, including the proofs where the candidate reuses an intermediate estimate or approximation.
Their underlying results are accepted inputs to this review.

## Finding

The proof establishes the finite right-column bound and both bounded-vector domains for the original canonical operator at the distinguished coordinate under the stated network hypothesis.
Applying it coordinate by coordinate gives the asserted conditional implication for normal tuples.

**Projection charts.**
For distinct outgoing unit vectors \(v,w\), projection onto \(v-w\) gives respective derivatives \(1-v\cdot w\) and \(v\cdot w-1\) at the vertex before normalization.
Continuity and the finite number of incident ends allow all of these inequalities to persist on the chosen short pieces, even though the projection direction depends on the pair.
At a new vertex the tangent belongs to each incident tangent range, so the small tangent variation gives one monotone projection through the two pieces in the original arclength orientation.
The resulting graphs have bounded second derivative on each compact smooth portion and a finite one-sided slope jump at the joint.
Reserving separate short pieces at both ends of each old edge also separates the two vertices of a pair of old edges with identical endpoints.
Disjoint closed pieces have positive distance by compactness.
Splitting at intersections and merging overlapping subsegments gives these cases for a finite arrangement of straight segments, and a cycle needs only the same local charts.

**Parameter and vacua.**
Fixing a chart pair fixes a single Borel parametrization of the entire spectral carrier for that estimate.
The other parameter intervals can be placed at positive distances, so their bounded images and the within-interval Lipschitz bounds give a finite forward Lipschitz constant \(L\).
Off the finitely many vertices the projected chart and the other arclength intervals give a Borel bijection onto the open pieces.
Vertex projections vanish by diffuseness and faithfulness, hence \(W^*(S)=W^*(Z)\) even for an arbitrary closed spectral subset of the network.
For each nonempty mesh cell the image has diameter at most \(L\ell\), and all the corresponding spectral projections are orthogonal.
The separate-center packing estimate bounds the sum of their cubed masses divided by \(\ell^2\).
Testing dyadic histograms against continuous functions identifies a weak \(L^3\) limit with the parameter law.
The identity real graph therefore has a scalar vacuum.
The same liberation vacuum works on both mixed cores since each marginal algebra is unchanged.
Each of its two spectral legs ignores the exceptional parameter endpoints.
On the remaining off-diagonal, \(|s-t|^{-2}\le L^2|h(s)-h(t)|^{-2}\), so push-forward bounds the new energy by the finite original one.
At an omitted coordinate both the scalar law and its liberation energy are unchanged.
This supplies full actual ACSY each time a pair requires a new parameter.

**Localized graph estimate.**
The extended graph on the parameter hull meets the bounded-variation slope hypothesis, including the end slopes.
Equation (9) of C_F0246 on the parameter core bounds the original right slice weighted by \(k\), and reflection gives the bound for \(\bar k\).
The real distinguished derivative on this core kills every omitted starred letter.
Flip-adjoint interchanges the two inner marginal variables, so symmetry of \(k\) converts the reflected one-input estimate into the left-slice estimate for \(I_k\delta_S\).
This outer derivation on the weakly dense star algebra satisfies both hypotheses of C_F0072, giving a closable right slice \(G\).
Matrix Kaplansky approximation and weak closedness of its graph preserve the finite-column bound on bounded elements.
The product identity passes to a Borel projection \(f\) because the inner actions of its bounded marginal polynomial approximants converge strongly on the fixed coarse vector and the two graph values converge weakly.
Right multiplication by \(e\) is contractive, and multiplication of \(\bar G(f)\) by the input column has norm at most the column norm times \(\|\bar G(f)\|_2\).
Together these give the claimed \(2c(G)\) cost, including when \(e=f\).

**Transfer and summation.**
The globally Lipschitz forward map \(h\) gives uniformly bounded marginal graph approximants for \(Z,Z^*\) and converging derivatives of mixed words on the parameter core.
For a unit target column the smooth cutoff of its approximating squared modulus preserves the limiting derivative and restores the \(1+\varepsilon\) column bound before the bounded inner multiplier is applied.
On the selected rectangle the ratio \(\bar\omega k\) cancels the divided difference of \(h\) and leaves the original phase when applied to the divided difference of \(\bar h\).
The two localized derivations agree on omitted starred letters, hence on the original mixed core by the outer Leibniz rule.
The coarse product measure ignores the diagonal.
For a separated pair the two spectral projections are orthogonal, so (6) of C_F0242 supplies finite column cost for rectangle-inserted liberation.
The cutoff reciprocal has summable Fourier coefficients in four real variables since its coefficients decay at least as \((1+|m|^2)^{-3}\).
Its separated characters act with uniformly bounded cost by the tracial product identity, giving the inverse gap on precisely the selected rectangle.
All local estimates now act on the same original core with the same input norm, irrespective of how many real parameters were used.
The finite sum of their constants bounds every finite column, independently of the number of entries.

**Original domain and scope.**
The actual flip-adjoint tuple has the reflected network at the same coordinate, and its right estimate bounds the original left slice on one input under tracial involution.
Part B of C_F0072 then puts \(M\Omega\) in both original canonical domains.
If \(p_n\) converges in that canonical graph, the core identity gives graph convergence of \(X_jp_n\) because \(X_j\) and \(P_\Omega\) are bounded.
This yields \([X_j,-\overline E_0]=\delta_{ij}P_\Omega\) on the closure domain and in particular on \(M\Omega\).
For the same-tangent example the signed parameter gap is of order \(x\) and the planar separation is \(2x^2\), so that chart estimate diverges.
The domain implication at such a tangency and the unrestricted Task implication remain open under this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Network statement](../../claims/Yin_C_F0248_v1.md#statement) | Geometry, arbitrary spectral subset, distinguished and reflected column costs, original domains and coordinatewise full-tuple consequence. |
| [Finding](#finding) | [Network argument](../../claims/Yin_C_F0248_v1.md#argument) | Complete construction, including pair-specific parameters, mixed-core localization and transport, positive-distance pairs, summation and same-tangent limitation. |
| [Finding](#finding) | [Task hypotheses](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual starred-domain ACSY input and existential generator-first full-domain output. |
| [Finding](#finding) | [Normal generator formulas](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness, forced starred values, flip-adjoint companion and reality for the distinguished real coordinate. |
| [Finding](#finding) | [Scalar packing](../../claims/Yin_C_F0233_v1.md#statement) | Part 1 applies to the disjoint mesh projections with separate disk centers and a common radius. |
| [Finding](#finding) | [Inverse-gap criterion](../../claims/Yin_C_F0238_v1.md#statement) | Old finite energy and the criterion for actual vacua on the represented parameter tuple. |
| [Finding](#finding) | [Coarse spectral calculus](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law domination makes the diagonal and null marginal endpoints invisible on coarse vectors. |
| [Finding](#finding) | [Liberation invariance](../../claims/Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Vacuum persistence on the algebra of bounded marginal words and push-forward of its joint measure. |
| [Finding](#finding) | [Scalar graph criterion](../../claims/Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Compactly supported \(L^3\) parameter density supplies the actual scalar vacuum for the identity graph. |
| [Finding](#finding) | [BV graph estimate](../../claims/Yin_C_F0246_v1.md#integration-over-vertices-and-the-target-mixed-core) | Equation (9) on the old real-parameter mixed core, for the extended graph and its reflection. |
| [Finding](#finding) | [Measurable product rule](../../claims/Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Extension of the column bound and trace identity (2)–(3) to Borel factors for the auxiliary closable slice. |
| [Finding](#finding) | [Mixed-core approximation](../../claims/Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Forward Lipschitz marginal graph limits and restoration of the norm of finite columns before localized inner insertion. |
| [Finding](#finding) | [Measurable liberation rectangles](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (6) on the orthogonal projections of a separated pair. |
| [Finding](#finding) | [Separated multipliers](../../claims/Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Uniform cost of continuous separated characters on a rectangle-inserted outer derivation. |
| [Finding](#finding) | [Two-slice theorem](../../claims/Yin_C_F0072_v1.md#statement) | Parts A and B for the auxiliary derivation, and part B for the original canonical operator and its adjoint. |
