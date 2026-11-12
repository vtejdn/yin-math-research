---
author: Yin
---
# Independent review of the pairwise-Haar three-term kernel model

Review time (UTC): 2026-11-11T17:56.
Human record author: Yin.
The review object is the complete fixed [L_A0025_v1](../../ledger/Yin_L_A0025_v1.md) worktree artifact inspected at this review time; no committed source revision is asserted for that newly created file.

## Arrangement and inputs

An agent outside this construction's substantive development conducted an initial independent whole-artifact mathematical review.
The supplied context contained the fixed candidate path, review scope, applicable authority and framework metadata, but no proof-generation dialogue, development drafts, proposing-agent mathematical summary or previous R finding.
No such additional material or R file was consulted before or during this review.
The reviewer derived the obligations from the candidate's claimed simultaneous Haar laws, positive kernel, regular-word exclusion and scope, then checked the displayed construction directly.
The review used hand derivations of all substantive identities, without a numerical approximation, symbolic checker or formal proof assistant.

The mathematical inputs were the entire [candidate](../../ledger/Yin_L_A0025_v1.md), the [finite-von-Neumann statement and bounded argument in C_A0009_v2](../../claims/Yin_C_A0009_v2.md#statement), and the [joint-word comparison section of C_A0006_v1](../../claims/Yin_C_A0006_v1.md#joint-words-still-contain-the-unknown-input).
The C_A0009 dependency was checked at its abstract pairwise-relative-Haar interface and bounded compression argument; its group-ring applications are not inputs to this construction.
The C_A0006 passage was inspected only to check the stated comparison, not adopted as a proof premise or re-audited as a whole.
No conclusion in a dependency's assessment section was used as evidence for the present construction.

## Whole-artifact finding

The candidate's asserted construction is mathematically valid at its stated scope.
It supplies a faithful normal tracial state on an explicitly specified finite von Neumann algebra, unitaries with all three pairwise relative spectral laws exactly Haar, and a three-term kernel of trace exactly \(1/10\).
The optional central-circle extension also gives all three individual Haar laws.
The specified joint word has trace \(-1/40\), so these particular unitaries with this trace cannot be actual group elements under a canonical regular group trace.
No mathematical correction is required for these claims.

### Matrix component and complete kernel

For both matrices in (1), the squared column norms are \(1/4+b^2=1\), while the column inner products vanish with their displayed signs and circle factors.
Thus they are bounded measurable unitaries in the stated matrix algebra.
The first column of \(I_2+U_b-V_b\) is identically zero, and the second is the vector in (2).
Its first entry vanishes only when \(z=w\); its second then vanishes only when \(z=w=-1\).
Consequently the kernel projection is the constant matrix unit \(e_{11}\) almost everywhere, with the exceptional two-dimensional fiber confined to a Haar-null singleton.
This checks the entire measurable kernel, including its exceptional fiber, and the normalized trace is \(1/2\).

### All moments and spectral measures

For \(|a|<1\), expand both factors of \(|\zeta-a|^{-2}\) in absolutely convergent geometric series on the unit circle.
Integration of the product gives total mass one after multiplication by \(1-a^2\), and its \(n\)-th moment is \(a^{|n|}\).
Therefore the displayed \(\rho_a\) is a probability density with nonzero moments \(a^{|n|}/2\).
At \(|a|=1/2\), the Poisson density ranges between \(1/3\) and \(3\), so \(2/3\leq\rho_a\leq2\), including both signs of \(a\).

The positive powers of each matrix in (1) have polynomial entries in its single circle coordinate.
Haar integration therefore selects exactly the trace of the power of its constant-coefficient matrix.
Those matrices have eigenvalues \((-1/2,0)\) and \((1/2,0)\), respectively, which yields (6) after the factor \(1/2\) from the normalized matrix trace.
This is coefficient extraction, not evaluation of a unitary or a rational expression at zero.
Unitarity supplies the negative moments by conjugation, and the zeroth moment is one.
These moments identify the two probability measures by trigonometric-polynomial approximation.

Direct multiplication gives all four entries in (7).
For \(D:=\operatorname{diag}(1,z^{-1})\), the prescribed conjugation \(D^*(U_b^*V_b)D\) has entries \((1/2,-b\eta;b,\eta/2)\), with \(\eta:=wz^{-1}\).
The coordinate \(\eta\) is Haar, and the constant-coefficient matrix has eigenvalues \((1/2,0)\).
The same positive- and negative-moment calculation gives exactly \(\rho_{1/2}\) for this third relative law.
Thus all three asserted marginal densities are simultaneously realized in one matrix model, are bounded and atomless, and each differs from Haar.

### Compensating probability space and its kernel

Each centered summand in (8) has Haar integral zero on the torus and lies in \([-1/3,1]\).
Their sum lies in \([-1,3]\), proving the positive bounds \(1/4\leq f\leq5/4\) and total mass one.
In particular the new measure is equivalent to Haar, so its integration functional is a faithful normal tracial state on the stated commutative von Neumann algebra.
Integrating in the unused coordinate gives the first two marginals in (10).
For the third, the Haar-preserving substitution \((s,\eta)\mapsto(s,t=s\eta)\) makes the first two centered terms integrate to zero and leaves precisely the stated \(\eta\)-density.
No independence under the weighted measure is assumed or needed.

For \(1+s-t=0\), the condition \(|1+s|=1\) is equivalent to \(\operatorname{Re}s=-1/2\).
There are exactly the two indicated values of \(s\), and each determines a unique circle value of \(t\).
Since these points have zero measure, multiplication by \(1+s-t\) has zero kernel projection.
There is no discarded positive-measure zero set or additional measurable kernel.

### Direct sum, trace, and central-circle extension

Both summands are finite von Neumann algebras with faithful normal tracial states, and both direct-sum weights are strictly positive and sum to one.
The direct-sum functional therefore has all the stated trace properties, with total mass one.
Each of the three spectral measures is the corresponding convex combination in (13), which is identically Haar.
Adjoints have the conjugate Haar measure, giving every ordered pair of distinct members of \((1,U,V)\).
The complete kernel projection is \(e_{11}\oplus0\), with trace \((1/5)(1/2)=1/10\).
The C_A0009_v2 matrix statement applies with \(d=1\) and coefficient moduli \((1,1,1)\), giving the consistent upper bound \(1/3\).
Its abstract proof uses only the stated finite-trace compression and the relative Haar spectral tails, with no additional regular-group premise that this model would violate.

In the tensor extension, the new circle unitary is central and independent in the product trace.
For each nonzero integer exponent, its moment is zero, so all three unitaries in (15) are individually Haar even though the original first summand was the identity.
Centrality cancels the added factor in every relative product, and left multiplication by this unitary leaves the kernel projection unchanged.
The extended model consequently retains the exact kernel trace and all relative laws.

### Regular-word exclusion and scope

Multiplication gives
\[
\operatorname{tr}_2(U_bV_b)
=-\frac18+\frac38z+\frac38w-\frac18zw,
\]
so Haar integration gives \(-1/8\).
In the commuting summand, every term of \(stf(s,t)\) integrates to zero: the terms involving only one density have a free circle coordinate, and the \(t/s\)-term becomes \(s^2\eta\) times a function of \(\eta\).
The weighted trace is therefore exactly \((1/5)(-1/8)+(4/5)0=-1/40\).
For actual group elements \(g,h\), the canonical trace of \(\lambda(g)\lambda(h)=\lambda(gh)\) is the coefficient at the identity and hence belongs to \(\{0,1\}\), regardless of torsion or relations.
This proves the asserted exclusion without presuming that the generated abstract unitary group is torsion-free.
The extended word \(\widetilde U_0^{-1}\widetilde U_1\widetilde U_0^{-1}\widetilde U_2\) is exactly \(UV\), so the same exclusion survives that extension.

A uniform zero-kernel conclusion from only the relative Haar hypotheses would apply to this example and contradict its exact kernel trace.
The same is true after imposing the three individual Haar laws, by the extension.
This establishes the claimed obstruction to that restricted inference, while leaving stronger joint information and the original group problem unresolved.
Neither optimality, sufficiency of imposing only the word \(UV\), an actual torsion-free group-ring fractional rank, nor completion of A0001 follows from the model.
The candidate expressly makes none of those claims.
The comparison with C_A0006 is accurate only at its stated marginal-versus-joint-word distinction; its separate rational construction is not required here.

## Source and verification limits

The construction's substantive numerical and spectral assertions were checked from its displayed bounded matrices, elementary geometric series, exact Haar integrations and direct-sum operations.
Standard circle-measure uniqueness by trigonometric-polynomial approximation and the usual finite-von-Neumann kernel-projection convention were used at the explicit scope above.
No external original, literature-wide attribution search or historical-priority investigation was performed, and no novelty or source-completeness claim beyond the identified local inputs is made.
No dependency's unrelated argument, external-source account, group-ring application, Task contract or full completion chain was reviewed.
This finding concerns mathematical validity of the complete L_A0025_v1 artifact and the specified dependency interfaces; it is neither a manuscript writing audit nor formal verification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete candidate](../../ledger/Yin_L_A0025_v1.md) | Entire fixed v1 artifact: every construction, equation (1)--(18), hypothesis, dependency interface and scope conclusion. |
| [Whole-artifact finding](#whole-artifact-finding) | [Matrix model](../../ledger/Yin_L_A0025_v1.md#a-two-dimensional-kernel-model) | Bounded unitaries, exact complete measurable kernel, null exceptional fiber and normalized trace. |
| [Whole-artifact finding](#whole-artifact-finding) | [Three marginal distributions](../../ledger/Yin_L_A0025_v1.md#exact-three-marginal-distributions) | Poisson densities, all positive and negative moments, relative-product conjugation, uniqueness and density bounds. |
| [Whole-artifact finding](#whole-artifact-finding) | [Commuting model](../../ledger/Yin_L_A0025_v1.md#a-compensating-commuting-model) | Faithful probability density, all three simultaneous marginals and complete zero scalar kernel. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite trace and Haar laws](../../ledger/Yin_L_A0025_v1.md#a-faithful-finite-trace-with-pairwise-relative-haar-unitaries) | Finite-von-Neumann premises, exact direct-sum laws and kernel, inertia compatibility, and central-circle extension. |
| [Whole-artifact finding](#whole-artifact-finding) | [Regular-word failure](../../ledger/Yin_L_A0025_v1.md#the-explicit-failure-of-the-regular-joint-word-condition) | Exact trace -1/40, extended word, regular group-element exclusion and original-group scope limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Strategy consequence](../../ledger/Yin_L_A0025_v1.md#consequence-for-the-strategy) | Logical obstruction to a marginal-only zero-kernel inference; no optimality, single-word sufficiency or group-ring counterexample conclusion. |
| [Whole-artifact finding](#whole-artifact-finding) | [Inertia statement](../../claims/Yin_C_A0009_v2.md#statement) | Only the abstract finite-von-Neumann pairwise-relative-Haar statement, applied with trace mass one and equal coefficient moduli. |
| [Whole-artifact finding](#whole-artifact-finding) | [Inertia argument](../../claims/Yin_C_A0009_v2.md#argument) | Only bounded isotropic compression and Haar-tail derivation of formulas (3)--(9), confirming the model meets every premise; unrelated applications excluded. |
| [Whole-artifact finding](#whole-artifact-finding) | [Joint-word comparison](../../claims/Yin_C_A0006_v1.md#joint-words-still-contain-the-unknown-input) | Comparison-level check of the individual-marginal versus regular-joint-word distinction; no adoption or whole-proof re-review of that construction. |
