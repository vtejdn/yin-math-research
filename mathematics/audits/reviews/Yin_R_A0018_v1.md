---
author: Yin
---
# Independent review of rank-one height recurrences and compressed transport

Review time: 2026-11-11T15:07.
Human record author: Yin.
The exact target is the saved 2026-11-11 revision of [C_A0005_v1](../../claims/Yin_C_A0005_v1.md#statement) and its complete [argument](../../claims/Yin_C_A0005_v1.md#argument), including formulas (1)--(17), the additional estimate (5a), the opening definition label, all intervening assertions and the final source and scope limitations.
This is a whole-argument mathematical agent review, not proof-assistant verification or Task completion.

## Arrangement and inputs

The reviewing agent was outside substantive development of this proof and received the fixed target, necessary dependency locators, repository rules and the authorized review scope.
No proof-generation dialogue, development draft, development summary or proposed substantive repair was supplied or consulted.
The reviewer enumerated the obligations from the statement, read the complete argument and needed mathematical interfaces, and formed initial findings before consulting the relevant earlier R findings on those dependencies.
Those earlier findings concern the dependencies rather than this new deduction.
No substantive repair was contributed during this review.

The accepted interfaces are the [finite affiliated and polar-support facts](../literature/MSY23/Yin_U004.md#msy23-u004), [relative inverses](../literature/JZ19/Yin_U001.md#regular-closure-definitions), [affiliated rank invariance](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement), [graded companion criterion](../../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials), [singular extreme-coefficient inequality](../../ledger/Yin_L_A0008_v1.md#a-unit-completion-instead-of-assuming-an-invertible-extreme-coefficient), and [bounded height certificate](../../claims/Yin_C_A0004_v3.md#height-layer-certificate).
The [collective-holonomy argument](../../claims/Yin_C_A0004_v2.md#collective-holonomy-condition) is used only as the existing regular-transport mechanism, with the finite subgroup case proved directly in the present target.
Each interface was read with its hypotheses, actual ambient algebra, trace convention and domain limitations.

The recorded dependency checks were consulted at their actual scopes: [R_A0008](Yin_R_A0008_v1.md#closed-affiliated-rank-and-hilbert-space-kernels) for closed-product rank transport, [R_A0009](Yin_R_A0009_v1.md#character-and-companion-certificates) for the affiliated graded theorem, [R_A0010](Yin_R_A0010_v1.md#singular-coefficients-and-the-exact-rank-bound) for the singular coefficient inequality, [R_A0017_v3](Yin_R_A0017_v3.md#height-layers-and-exclusion-of-the-remaining-free-atoms) for the bounded height proof, and [R_A0017_v2](Yin_R_A0017_v2.md#general-sufficient-conditions-and-determinant-limits) for infinite regular-transport orbits.
The present review checks their applicability to this target, without claiming a new whole-artifact review of those older dependencies.
The general construction and associativity of the finite affiliated algebra, its matrix and corner identifications, polar decomposition and relative-inverse existence remain accepted foundations at the source units' recorded inspection scopes.
Their original source proofs were not re-audited.

## Whole-artifact finding

No actionable mathematical gap or unresolved source-applicability problem was found in the inspected statement and complete argument.
The finite-section estimate, exact residual decomposition, overlap-defect bound, no-overlap projection identity, bounded graph formula, finite-orbit calculation, two comparison models and coupled residual family are mathematically supported under the stated hypotheses.
This finding includes both the general affiliated argument and the separately restricted bounded recurrence argument.
It does not turn the coefficient-group dimensions into integers or resolve the [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract).

### Finite sections and dimension normalization

The epimorphism gives the decomposition into height layers, and left multiplication by \(t^n\) identifies the same right \(N\)-action on every layer.
Conjugating a coefficient in \(M_0\) into that identification gives exactly \(\sigma^{-n}\), proving (8) with the displayed order and both second-coordinate constraints retained.
The matrix in (1) is bounded and selfadjoint, and the forward and reverse coefficient projections both have unnormalized rank one.

For \(m\ge2\), the two endpoint first-coordinate modules have total \(N\)-dimension two.
The bounded map \(H_m|_{V_m}\) has kernel \(\ker H_m\) and range closure inside that endpoint module, so rectangular polar decomposition gives \(\dim_N V_m\le d_m+2\) without a closed-range premise.
A cut of a global kernel vector has no other errors, and the positive contraction \(\chi_mQ\chi_m\) is supported on \(V_m\).
Its trace is therefore at most \(d_m+2\).
Right \(G\)-equivariance supplies the identical diagonal traces at all height representatives and proves (9).

Conversely, the two constraints \(x_1=x_m=0\) remove dimension at most two from \(\ker H_m\).
Zero extension then satisfies the interior and both exterior equations.
If \(F\) is the resulting projection, \(F\le Q,\chi_m\) implies \(\chi_mQ\chi_m-F=\chi_m(Q-F)\chi_m\ge0\), justifying the reverse trace estimate.
These inequalities establish both parts of (2), including the error \(2/m\), without an amenability assumption or exchange of spectral limits.

The auxiliary bound \(\nu_G(H)\le1\) follows from a bounded finite recurrence with \(m\) free \(y\)-coordinates and two initial \(x\)-coordinates.
The corresponding graph has dimension at most \(m+2\).
This supplies only a dimension bound and does not assume integral \(N\)-dimensions.

### Singular elimination and the bounded graph projection

For the selfadjoint \(c\), its relative inverse has both support products equal to \(1-r\).
Multiplication of the triangular factors therefore gives (10), with \(\mathcal A=t+t^{-1}+a-bc^\dagger b^*\) and \(B=br\), in the indicated noncommutative order.
The support of \(B^*B\) is contained in \(r\), making \(q=r-s\) a projection.
Its range is exactly \(\ker b\cap\ker c\).
The energy identity for \(b^*b+c^2\) gives the second description of \(q\) in (4).

The \(1-r\) summand of \(c\) is independently invertible on its support.
After splitting it and the zero \(q\) summand, the \(f\oplus s\) saddle block has the two-sided inverse (11).
The inverse's upper-left block is zero, so its Schur correction against the \(p\) block vanishes rather than contributing an unrecorded term.
This gives
\[
\operatorname{rk}_G H=1-\tau_N(r)+2\tau_N(s)+\operatorname{rk}_p R.
\]
Using \(\tau_N(s)=\tau_N(f)\), \(\tau_N(p)=1-\tau_N(f)\) and \(\operatorname{rk}_p R=\tau_N(p)-\nu_p(R)\) gives exactly (4).
Zero support corners are legitimately omitted.
No inverse of the target residual is used to establish this identity.

The rank calculation uses closed affiliated products and actual units, so it remains valid when either relative inverse is unbounded.
It makes no unrestricted pointwise assertion about the action of those inverses on Hilbert-space kernel vectors.
When both relative inverses are bounded, the displayed \(W\) is bounded.
For \(x\in\ker R\subseteq p\), its two lower-coordinate terms lie respectively in \(1-r\) and \(s\), while the free lower vector lies in \(q\).
The second kernel equation follows from \(B^*x=0\), and the first reduces to \(p\mathcal A px=0\).
Conversely the kernel equations give precisely these parameters.
The ranges of \(Wk\) and \(0\oplus q\) are orthogonal, and \(kW^*Wk\ge k\) has a bounded corner inverse.
This proves the full orthogonal projection formula (12) at exactly its declared bounded scope.

### The overlap defect and compressed height transport

As an operator on the full space, \(R\) is zero on \(1-p\).
The identity
\[
Rt=p\sigma^{-1}(p)+(php)t+p\sigma(p)t^2
\]
has the stated homogeneous degrees, including when \(h\) is affiliated and unbounded.
The accepted singular constant-coefficient bound applies to this actual affiliated polynomial.
Right multiplication by \(t\) preserves rank, and \(p\sigma^{-1}(p)=(ptp)^*t\) has the rank of \(K=ptp\).

Inside the \(p\)-corner, the kernel of \(K\) is exactly \(p\wedge\sigma^{-1}(1-p)=\Delta\).
Thus \(\operatorname{rk}_G K=\tau_N(p)-\tau_N(\Delta)\).
Subtracting the resulting rank bound from \(\tau_N(p)\) yields \(0\le\nu_p(R)\le\tau_N(\Delta)\), proving (5a) after (4).
The defect is the actual transported overlap, not the whole omitted coordinate.

When \(\Delta=0\) and \(p\ne0\), finite-trace support equality makes \(K\) an affiliated unit in \(pMp\).
The character action fixes this corner and \(h\), assigns degree one to \(K\), and degree one to \((K^*)^{-1}\).
Consequently
\[
R(K^*)^{-1}=p+(php)(K^*)^{-1}+K(K^*)^{-1}
\]
has degrees zero, one and two with independently invertible constant term \(p\).
The graded companion interface applies to the normalized finite corner and proves zero residual kernel.
Returning to the unnormalized trace preserves that conclusion.
For \(p=0\) it is immediate.
Since \(0\oplus q\) is visibly in the bounded kernel of \(H\), equality of its trace with the entire kernel trace and faithfulness prove the actual projection identity (6).

If \(\kappa=\|p-\sigma(p)\|<1\), the two compression inequalities in the target follow from the norm bounds on the complementary projections.
They make both hopping maps bounded isomorphisms between consecutive equal-trace layer modules.
With the additional bounded relative inverses, \(h\) is bounded and two initial \(p\)-layers determine every finite restriction.
The bounded graph trace argument then gives \(m\nu_p(R)\le2\tau_N(p)\).
This is a valid separate proof at its stronger hypotheses, not an extension of a bounded graph substitution to unbounded coefficients.
The cases \(p=0\), \(p=1\), \(\sigma(p)=p\), injective \(c\), and \(c=0\) with injective \(b\) all satisfy the asserted conclusions.
The infinite-order example \(b=1-v\) requires injectivity but no lower spectral bound.

### Projection middle coefficient, finite paths and comparison groups

For \(c=0\) and \(b=q_0\), the support definitions give \(p=q=p_0\) and \(h=a\).
The direct bounded kernel parametrization proves (13) and agrees with (12).

In a finite permutation orbit, trace preservation assigns equal weight \(w_O/m_O\) to each projection.
An orbit with no deleted site retains the invertible height hopping and hence has zero residual kernel.
Every other retained component is a finite cyclic run bounded by deleted sites.
The map \((x_j)\mapsto\sum_jt^jx_j\) is a right \(G\)-equivariant unitary onto that run because its translated support projections are distinct and orthogonal.
Its conjugated hopping coefficients are exactly one in both directions, and its diagonal coefficients are the successive real \(a_i\).
All exterior edges are killed by the deleted projections.
Thus the residual block is \(J_C\otimes I\), with one kernel direction contributing trace \(w_O/m_O\), proving (14).
This includes empty retained sets, complete retained orbits, singleton runs and orbit lengths one and two.

The first-row recurrence gives \(\dim_{\mathbb C}\ker J_C\le1\), and cofactor expansion gives (15).
At zero potential the determinant vanishes precisely for odd run length.
No probabilistic cluster theorem is needed for these finite matrix calculations.

In the swapping model, \(e=p_up_v\) is invariant and the translate of \(d=p_u(1-p_v)\) lies in the deleted complement of \(p_u\).
The residual is \(e(t+t^{-1})\), injective on \(e\) and zero on \(d\).
Their traces are \(1/4\), giving the dimensions \(1/2\) and \(3/4\) in (16).
Both middle blocks have rank \(2\tau_N(q_0)=1\), so all three coefficient ranks agree between the models.

The extra graph modes and their orthogonality to the free lower \(p_u\)-modes follow from \((t+t^{-1})d\subseteq q_0\).
On \(d\), the graph Gram operator is \(d(3+t^2+t^{-2})d\), bounded below by \(d\).
Since \(d\) commutes with \(t^2\), its inverse is the displayed \((3+t^2+t^{-2})^{-1}d\).
The cyclic multiplier \(1/(3+z+z^{-1})\) is not a Laurent polynomial, so the corresponding nonzero projection block has infinite height propagation.
Both groups contain the specified order-two elements, and neither example is a torsion-free counterexample.

### Arbitrary coupled residual and positive energy

Direct ordered multiplication gives \(W_0^*H_ZW_0=\operatorname{diag}(t+t^{-1},Z)\) and \(W_0^*PW_0=P\).
No \(t,Z\) commutation is used.
The infinite order of \(t\) gives the injectivity of \(t+t^{-1}\) through its bilateral-shift multiplier, so the bounded congruence proves (7).
The original kernel equations also give its actual kernel \(0\oplus\ker Z\).
The case \(Z=0\) has dimension one; the assertion of nontrivial coupling is used only for \(Z\ne0\), as stated in the argument.

For the positive sum, the energy identity makes \(\ker Z\) the simultaneous fixed space of the actual translations \(h_j\).
Every regular \(K_0\)-orbit has cardinality \(|K_0|\).
Infinite orbits admit no nonzero square-summable constant vector, whereas finite orbits give the group-average projection with trace \(1/|K_0|\).
This proves (17), including the empty and trivial generating systems.
The two-coordinate probability trace divides this unnormalized dimension by two.

## Source completeness and conclusion limits

The specialized external interfaces are identified by source units with exact passages and their accepted inspection limits.
The current block, finite-section, path and energy calculations are supplied locally and need no additional unverified external assertion.
The dependency reviews cover the specific interfaces reused here; no later or broader conclusion is inferred from their mere presence.
No historical priority, new Atiyah group class, original-source proof audit, numerical experiment or formal verification is asserted by this finding.

The general model permits bounded von Neumann coefficients, so fractional projection traces are allowed.
In the group-ring subfamily, support projections and singular relative inverses are used in the ambient affiliated algebra; their membership in a smaller rational closure or in the group ring is not assumed.
Formula (2) still contains coefficient-group dimensions, and (4) still contains a genuine compressed residual unless controlled by additional hypotheses.
The coupled family embeds arbitrary selfadjoint scalar coefficient-group kernel problems and does not give an equivalence with all finite matrices in the Task.
The finite-orbit calculation does not classify residuals with nonzero overlap and infinite transport components.
These are correctly retained limitations of the result rather than gaps in the proved assertions.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0005_v1.md#statement) | Complete five-part statement, exact hypotheses, trace conventions, formulas (1)--(7) including (5a), all bounded and affiliated qualifications and torsion-free-contract limits. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0005_v1.md#argument) | Entire saved argument, formulas (8)--(17), all intervening calculations, accepted dependency interfaces and concluding scope limitations. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite sections](../../claims/Yin_C_A0005_v1.md#finite-section-formula) | Both dimension inequalities, endpoint constraints, exact trace identity, no closed-range assumption and the separate bound by one. |
| [Whole-artifact finding](#whole-artifact-finding) | [Singular reduction](../../claims/Yin_C_A0005_v1.md#singular-middle-reduction) | Relative-inverse order, support-corner decomposition, rank subtraction and the bounded graph projection (12), including zero corners. |
| [Whole-artifact finding](#whole-artifact-finding) | [Compressed transport](../../claims/Yin_C_A0005_v1.md#compressed-transport-certificate) | Overlap estimate (5a), exact kernel of compressed hopping, graded corner criterion, complete projection identity, stronger bounded proof and degenerate cases. |
| [Whole-artifact finding](#whole-artifact-finding) | [Finite projection orbits](../../claims/Yin_C_A0005_v1.md#projection-middle-and-finite-orbits) | Direct bounded kernel parametrization, trace weights, all finite run cases, path matrices and determinant criterion. |
| [Whole-artifact finding](#whole-artifact-finding) | [Comparison models](../../claims/Yin_C_A0005_v1.md#same-ranks-different-transport) | Exact dimensions, identical coefficient ranks, extra modes, nonlocal graph projection and torsion boundary. |
| [Whole-artifact finding](#whole-artifact-finding) | [Coupled residual and energy](../../claims/Yin_C_A0005_v1.md#coupled-residual-and-energy) | Ordered bounded congruence, actual kernel, arbitrary scalar residual, finite and infinite subgroup cases, empty generators and probability normalization. |
| [Whole-artifact finding](#whole-artifact-finding) | [Dependencies and limits](../../claims/Yin_C_A0005_v1.md#dependencies-source-scope-and-continuation) | Exact accepted-input scope, remaining coefficient arithmetic, nonzero-overlap continuation boundary and absence of a Task-completion claim. |
