---
author: Yin
---
# Independent review of central specialization and finite gap creation

Review act: 2026-11-12T01:55, in UTC minutes, for Yin.
The inspected input is the complete working-tree [C_A0012 v5](../../claims/Yin_C_A0012_v5.md), including every statement, displayed formula, auxiliary construction, source interface and limitation.
The candidate was unselected during this inspection.
This separately assigned reviewer was outside substantive proof development and received only the fixed candidate path, exact review scope, applicable instructions and operational work-round facts.
No development draft, proof-generation dialogue, author explanation or mathematical development summary was supplied or consulted.
Initial findings were formed from the full candidate and necessary mathematical dependencies before consulting earlier R conclusions.
The later comparison used [R_A0038 v2](Yin_R_A0038_v2.md#exact-generic-rank), [R_A0038 v4](Yin_R_A0038_v4.md#whole-artifact-finding) and the exact auxiliary-input findings at their existing scopes.
No substantive repair was supplied, and this reviewer changed no Claim, strategy, assessment or Task decision.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete artifact](../../claims/Yin_C_A0012_v5.md) | Every assertion and formula (1)--(18), including the tensor construction, exact complete kernels, gap equivalence, perturbation estimate, central Laurent theorem, local variant, specialization consequence and remaining research limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0012_v5.md#statement) | Exact finite-algebra and rectangular hypotheses, actual integrated operator, generic nullity, exceptional fiber, positive spectral-mass bound, closed-range conclusion and specialization-compatible consequence. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0012_v5.md#argument) | Complete bounded support argument, removal of zero mass, generic-rank interface, norm estimate, measurable functional calculus and Haar integration, with all subsequent domain and scope qualifications. |

## Inputs and original scope

The unchanged [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract) concerns all finite rectangular complex group-ring matrices over all torsion-free discrete groups, with canonical group trace and unnormalized domain matrix trace.
It requires a universal integrality proof or an actual counterexample.
The present artifact gives precise obstructions to a proposed regularization route and supplies neither kind of completion.

I read the [C_A0012 v2 exact generic-rank proof](../../claims/Yin_C_A0012_v2.md#exact-generic-rank-for-rectangular-laurent-matrices), the [v1 finite-coefficient specialization input](../../claims/Yin_C_A0012_v1.md#one-variable-specialization-with-an-affiliated-constant-inverse) and its [actual tensor-product trace interface](../../claims/Yin_C_A0012_v1.md#several-central-variables-and-the-actual-trace).
The new application is to one central variable and bounded rectangular coefficients in an arbitrary finite von Neumann algebra.
It uses no rational inverse at the exceptional fiber.
The earlier v2 independent finding is reused for that established specialization and rank theorem at its recorded scope; its rational extension and unrelated finite realization are not new claims of this review.

The [L_A0006 rank interface](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) supplies the distinction between support dimension and an unjustified pointwise kernel map.
The new perturbation proof uses only bounded operators, polar decomposition and finite traciality.
The auxiliary spectral input is the [C_A0004 v2 degree-four free-tree gap](../../claims/Yin_C_A0004_v2.md#free-projection-and-gap), with its [exact reviewed normalization](Yin_R_A0017_v2.md#weighted-free-tree-matrices-and-isolated-atom) and the retained [tree transform](../../ledger/Yin_L_A0016_v1.md#exact-tree-and-lattice-transforms).
Only that tree bound is needed from the more extensive incidence calculation.

I also read [C_A0012 v4](../../claims/Yin_C_A0012_v4.md), including its explicit bounded closed-range equivalence and separate projection-arithmetic obligation.
The [C_A0007 v5 continuation boundary](../../claims/Yin_C_A0007_v5.md#complete-chain-attempt-known-coverage-and-continuation-boundary) is consistent with the candidate's comparison scope.
It is not a logical premise of the new spectral estimate.

## Auxiliary kernel preservation and its exact gap boundary

For the free row \(d=(1-a\ \ 1-b)\), multiplication gives \(dd^*=4-a-a^{-1}-b-b^{-1}\).
The degree-four tree spectrum supplies the positive lower bound \(\gamma=4-2\sqrt3\), so the inverse in (3) is bounded independently of \(A\).
The operator \(d^*\Delta^{-1}d\) is selfadjoint and idempotent.
Its complementary projection is precisely \(q=P_{\ker d}\).
Rectangular traciality gives
\[
(\operatorname{Tr}_2\otimes\tau_F)(d^*\Delta^{-1}d)
=\tau_F(\Delta^{-1}dd^*)=1.
\]
Thus \(q\) and its complement both have trace one, and \(q\ne0\).
No assumption that \(q\) is a finite group-ring matrix is made.

The direct-product construction gives an actual tensor-product regular representation and product trace.
The matrix \(Q_A\) has \(2n\) rows and columns, while \(R_A\) has \(2r+n\) rows and \(2n\) columns.
The displayed multiplication \(R_A^*R_A=Q_A\) is correct with the indicated consistent coordinate ordering.
All entries of these two matrices are finite group-ring entries, even though \(p\) and \(q\) need not be.

Positivity identifies the kernel of the sum in (4) with the intersection of the two zero spaces.
The commuting tensor summands therefore have complete kernel projection \(p\otimes q\).
Its product trace is \(\nu_H(A)\cdot1\), with no factor of two or omitted rectangular-domain correction.

On the reducing \(q\)-summand, \(Q_A\) is \(T\otimes I_q\).
Since \(q\ne0\), any unit sequence for \(T\) approaching zero on the complement of \(p\) produces the corresponding unit sequence for \(Q_A\) outside \(p\otimes q\).
In the reverse direction, polar decomposition transfers \(\Delta\ge\gamma I\) to \(d^*d\ge\gamma(I_2-q)\).
The \(q\)-summand outside the kernel is bounded below by \(\eta\), while the entire \((I_2-q)\)-summand is bounded below by \(\gamma\).
This verifies both directions of (7) and the lower bound \(\min(\eta,\gamma)\).
For \(p=I_n\), the first complementary piece is absent and the second bound alone applies.
For \(p=0\), the same decomposition applies without a kernel.
The example consequently preserves the entire arbitrary input nullity but creates no new complementary gap.

## Bounded perturbation and removal of the actual zero atom

Both \(p_0\) and \(e=1_{(\varepsilon,\infty)}(|B|)\) act in the \(n\)-coordinate domain, regardless of the number \(m\) of rows.
On \(p_0\mathcal H^n\), the norm estimate gives \(\|Bx\|\le\varepsilon\|x\|\).
For every nonzero \(x\in e\mathcal H^n\), the spectral theorem gives the strict opposite inequality.
Indeed the nonzero scalar spectral measure is supported where the squared spectral value is strictly greater than \(\varepsilon^2\); no uniform extra margin is needed.
Their intersection is therefore zero.

For the bounded operator \((1-e)p_0\), the kernel restricted to \(p_0\mathcal H^n\) is that intersection.
Its initial support is exactly \(p_0\), and its final support is under \(1-e\).
The trace inequality in (8) follows by polar decomposition even when this map has nonclosed range.
This step introduces neither finite-dimensional multiplicity nor a discrete range of possible traces.

The projection \(1_{[0,\varepsilon]}(|B|)\) is the orthogonal sum of the actual kernel projection and \(1_{(0,\varepsilon]}(|B|)\).
Subtracting its kernel trace proves (9) with the correct sign and domain trace.
The inequality is valid when the right side is zero or negative.
Its useful positivity in the later argument comes only from the separately established positive nullity drop.

## Generic fibers and integrated small positive spectrum

Write \(c=\tau(1)\), without assuming \(c=1\).
The v2 theorem gives integrated and almost-everywhere rank equal to the supremum \(\rho\) of the actual fiber ranks.
Consequently the integrated nullity is \(nc-\rho\), almost every fiber has that nullity, and every fiber has nullity at least that value.
Thus the use of \(\kappa_{\mathrm{gen}}\) in (11)--(12) is valid for a general finite trace and rectangular matrix.

The corner argument behind that theorem has the hypotheses required here.
At a chosen fiber \(w\), the compression \(u^*B(z)e\) in its initial-support corner has bounded Laurent coefficients and an actual affiliated unit at \(w\).
The finite-coefficient theorem gives full corner rank generically, compression cannot increase rank, and a sequence approaching the rank supremum gives equality almost everywhere.
This establishes the generic interface without demanding a bounded inverse of the chosen corner or integer corner trace.

For positive, negative and zero Laurent exponents, \(|e^{ijt}-1|\le |j||t|\).
The finite coefficient sum therefore proves (14) exactly with \(L_B\).
If \(L_B=0\), all coefficients with nonzero exponent vanish, making the field constant and contradicting \(\delta>0\).
On the arc \(|t|\le\min(\pi,\varepsilon/L_B)\), (9) applies with \(B_0=B(z_0)\).
Almost everywhere on that arc its right side is precisely \(\delta\).
The exceptional set is Haar-null and cannot remove any of the arc's positive measure.

The actual von Neumann tensor product and normal trace give (15).
Bounded continuous functional calculus first identifies the corresponding fiber integrals; bounded Borel functional calculus then gives the spectral indicator, including its endpoints.
The integrand is measurable, bounded by \(nc\), and nonnegative.
This is an integral of genuine fiber spectral projections and does not evaluate an arbitrary representative of an integrated projection class.

The arc has normalized Haar measure \(\min(\pi,\varepsilon/L_B)/\pi\).
Integration yields (13), with no missing factor of two and with the zero spectral mass already removed.
Its strictly positive value for every \(\varepsilon>0\) rules out a positive complementary gap for \(|\mathcal B|\).
Squaring its positive spectral parameter gives the same conclusion for \(\mathcal B^*\mathcal B\).
The bounded closed-range equivalence read in v4 then proves that \(\mathcal B\) has nonclosed range.

For the local variant, the radius \((\varepsilon/C)^{1/k}\) is at most \(t_0\) under the explicitly stated bound on \(\varepsilon\).
The same support inequality and normalized arc measure give (16).
This requires \(C>0\), \(k>0\), the stated local norm estimate and the almost-everywhere local nullity deficit.
It gives a lower bound, not an asymptotic equality or a universal vanishing order for arbitrary continuous fields.

## Specialization-compatible finite constructions

A finite matrix over \(\mathbb C[K\times\langle u\rangle]\) is an actual finite Laurent matrix with bounded coefficients in \(\mathcal N(K)\).
The product trace agrees with canonical group trace after Fourier transformation of the central cyclic factor.
The direct product is torsion-free when \(K\) is torsion-free.
Neither the generic-rank input nor the perturbation estimate needs commutation among the \(K\)-coefficients.

The input \(1-u\) has zero integrated nullity because its circle multiplier vanishes only at one point.
At \(u=1\) it is the zero scalar matrix, of nullity one with canonical trace.
Thus the two identities (18), with the same additive correction \(c\), give exactly the excess \(\delta=1\).
No identity at every other scalar parameter is needed because generic rank supplies the almost-everywhere value.
Adding a displayed scalar zero block adds one to both input nullities and leaves this excess equal to one.
The obstruction therefore includes an input whose complete kernel is nonzero.

For the stated fixed finite syntax, sums, products and adjoints of Laurent fields remain locally norm-Lipschitz.
A square inverse gate bounded throughout the specified neighborhood preserves this property by
\[
X(z)^{-1}-X(w)^{-1}
=X(z)^{-1}\bigl(X(w)-X(z)\bigr)X(w)^{-1}.
\]
Hence independently bounded inverse gates in that syntax do supply a local estimate of the type used in (16), for instance with \(k=1\), when the local nullity relation is available.
This checks the inverse-gate remark at its stated finite-construction scope.
Mere norm continuity of an unrelated field would not by itself imply a power estimate, and an inverse undefined or unbounded at the special fiber is explicitly outside the premise.
The final output's required finite group-ring membership remains a separate condition.

The obstruction concerns the exact central fibers and the compatible nullity jump.
It says nothing conclusive about a genuinely noncentral extension lacking those fibers or a separately chosen unspecialized output lacking (18).
It supplies no integer trace for a resulting projection.
The candidate's final discussion correctly retains those limitations and the independent arithmetic obligation from v4.

## Source and verification limits

The accepted tree gap, finite-coefficient specialization, generic-rank and support interfaces were checked for their exact hypotheses, normalizations and present uses.
Prior R conclusions were consulted only after the initial whole-artifact findings and retained at their original scopes.
General bounded spectral calculus, polar decomposition, finite traciality, normal tensor-product traces, Fourier transformation and the bounded inverse theorem are accepted foundational inputs.
The original source PDFs and their complete foundational proofs were not newly audited.
No new external theorem or historical novelty identification is asserted by the candidate, and no unresolved source-applicability issue was found in its actual uses.
This review is a mathematical inspection, without numerical experiments, proof-assistant verification or a Task-completion claim.

## Whole-artifact finding

The complete statement and argument of C_A0012 v5 are supported by this independent inspection.
I found no unresolved mathematical defect in the auxiliary finite construction, its full kernel and exact gap equivalence, the rectangular perturbation inequality, the removal of zero mass, the generic-rank interface, the integrated quantitative estimate, the local variant or the specialization-compatible consequence.
The result proves a conditional obstruction to finite gap creation and leaves both the allowed escape constructions and the separate projection-arithmetic problem unresolved.
It neither proves nor refutes A0001.
This finding binds only the inspected v5 artifact and exact reused interfaces, and selects no Claim assessment or Task lifecycle.
