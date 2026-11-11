---
author: Yin
---
# Relations-compatible analytic and algebraic ranks

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Prove that the actual affiliated rational closure of a complex group ring is a division ring, using the MSY23 equivalence with integer matrix rank. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Use the preserved degenerate-energy certificate where available, and isolate zero-or-unit tests for rationally conjugated row separations in inverse-difference elimination. |

## Mechanism and obstruction

Use [MSY23, Theorem 5.25](../audits/literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence): integer analytic rank for all polynomial matrices in a bounded tuple is equivalent to its actual rational closure, or equivalently its division closure, in the affiliated algebra being a division ring.
The [survey's analytic probe](../ledger/Yin_L_A0001_v1.md#relation-sensitive-analytic-probe) specifies the trace convention and the direct specialization to a tuple of regular group generators and their inverses.
This criterion already supplies the analytic-algebraic bridge; no free-field realization or algebraic freeness is required.
The remaining problem is to prove that every nonzero element of the actual rational closure is invertible, using an analytic argument that respects the group's relations.
An abstract division-ring embedding alone still does not identify this actual closure.

## Current findings

The [noncyclic path investigation](../ledger/Yin_L_A0011_v1.md#a-pair-of-conditions-preserved-by-scalar-elimination) gives a closed sufficient class preserving a semidefinite real part and a positive injective imaginary compression on its explicitly specified zero coordinates.
Its [concrete next pivot](../ledger/Yin_L_A0011_v1.md#a-noncyclic-positive-rational-sum-produced-by-the-first-pivot) is independently certified by the classical positive parallel-sum identity, although its two path coefficients do not commute.
The Promislow calibration [excludes every original constant positive weight and phase with an injective positive real part](../ledger/Yin_L_A0011_v1.md#a-screen-excluding-every-direct-full-rank-constant-weight-real-part), so this extends the previous original-pencil sufficient condition while retaining known energy and group-class coverage.
An [inverse-difference Schur identity](../ledger/Yin_L_A0011_v1.md#one-inverse-difference-schur-step) separately factors a two-path sum into six already controlled differences, with no commutation assumption.
For central column parameters, the [preserved shape](../ledger/Yin_L_A0011_v1.md#a-shape-invariant-with-central-column-parameters) leaves the exact three-square defect in one difference of two rationally conjugated row parameters; original pairwise binomial invertibility does not certify that new difference.
The [Klein bottle collision](../ledger/Yin_L_A0011_v1.md#an-actual-torsion-free-collision-after-one-step) has rank two and shows why an induction must allow exact mergers, while the [relative-path trace comparison](../ledger/Yin_L_A0011_v1.md#individual-diffuse-path-laws-do-not-suffice) excludes individual Haar laws and abstract torsion-freeness as substitutes for joint regular-trace control.

The [three-term investigation](../ledger/Yin_L_A0010_v1.md#group-and-selected-pencil) selects a Promislow pencil whose identity-pivot reduction leaves \(1+a+b\), outside the specified direct cyclic, constant-weight energy and supporting-subgroup integer-grading tests.
Its [actual four-coset model](../ledger/Yin_L_A0010_v1.md#actual-finite-index-matrix-model) has a complete independently certified scalar pivot chain in the translation subgroup's rational function field, so it supplies an explicit calibration within known virtually abelian coverage.
A different three-term pencil has a [preserved cyclic coefficient field between group-monomial row and column factors](../ledger/Yin_L_A0010_v1.md#an-explicitly-preserved-coefficient-class), giving strict dimension descent and an original-border zero/unit conclusion without requiring its original coefficients to commute or admit a character.
The first pencil [cannot be brought into a cyclic Laurent group ring by those diagonal monomial factors](../ledger/Yin_L_A0010_v1.md#a-concrete-limit-of-the-cyclic-gauge-condition), so the two certificates have genuinely different stated scopes.
Neither supplies a new rank constraint outside the known cyclic or finite-index mechanisms.
The [identity-pivot row splitting](../ledger/Yin_L_A0010_v1.md#an-elementary-row-splitting-step) converts every group-ring matrix to whole rows of at most three monomials with unchanged kernel dimension; an unrestricted three-term integrality theorem is therefore equivalent to the full Task.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0012_v1.md#whole-artifact-finding) covers both examples, all exclusions, the preserved class, original-border application and row-splitting equivalence at their stated source and foundational scope.

The [scalar dimension-induction investigation](../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step) identifies sufficient conditions that certify each pivot before its inverse is used and preserve the closed kernel dimension at every decrease in matrix size.
For [rows with at most two group monomial terms](../ledger/Yin_L_A0009_v1.md#a-concrete-sufficient-condition-closed-under-elimination), tree elimination preserves that row condition and leaves one scalar transport variable per component.
Torsion-freeness makes each nonzero residual binomial an actual unit, giving rank equal to the number of columns minus the number of unpinned components with identity loop transports, without a character assumption.
For an original border whose complementary block has this structure, the [direct application](../ledger/Yin_L_A0009_v1.md#application-to-the-original-rational-border) gives \(\operatorname{rk}_G Q=N+1-f\); denominator admissibility forces \(f\in\{0,1\}\), resolving the scalar rational value as respectively a unit or zero without a matching-energy assumption.
The [constant-proportionality condition](../ledger/Yin_L_A0009_v1.md#a-sufficient-condition-that-preserves-affineness) instead preserves the original affine tuple; its dense cyclic-pivot example works even when the specified pencil has no constant weighted positive-real-part certificate.
The [positive-real-part class](../ledger/Yin_L_A0009_v1.md#another-closed-class-injective-positive-real-part) is preserved by affiliated Schur complements and permits rational intermediate entries, with every scalar pivot independently justified.
These give explicit elimination interfaces for the retained cyclic, transport and energy mechanisms, not a new Atiyah group class or a reduction of all affine pencils to controlled scalar cases.
The [independent main and supplemental findings](../audits/reviews/Yin_R_A0011_v1.md#combined-outcome) together cover the complete dimension-induction investigation and its original-border application.

The [degree-reduction investigation](../ledger/Yin_L_A0008_v1.md#a-single-exact-lowering-step) gives an explicit terminating induction to affine matrices using only independently invertible triangular factors, with the exact rank shift and unchanged closed kernel dimension.
This is the classical [Coh06 Higman construction](../audits/literature/Coh06/Yin_U002.md#coh06-u002), specialized to the actual evaluation and rank interface.
Its [ordered one-variable form](../ledger/Yin_L_A0008_v1.md#an-efficient-ordered-one-variable-version) preserves the invertibility question for each extreme coefficient, while increasing matrix size.
An [explicit unit completion](../ledger/Yin_L_A0008_v1.md#a-unit-completion-instead-of-assuming-an-invertible-extreme-coefficient) proves that the polynomial rank is at least the rank of either extreme coefficient in an actual cyclic direction, but does not force the remaining defect to be integral.
The exact example \(A(1+t)\) in [the coefficient obstruction](../ledger/Yin_L_A0008_v1.md#degree-one-still-contains-fractional-coefficient-defects) shows that arbitrary degree-one cyclic matrices already retain the coefficient group's Atiyah problem.
The [earlier concrete families](../ledger/Yin_L_A0008_v1.md#a-singleton-extreme-support-term-and-the-earlier-examples) now require only that \(\langle g,h\rangle\) be indicable, rather than that both selected elements have degree one.
The complete complex-parameter and ordered-product cases follow from independently invertible singleton or cyclic extreme coefficients and remain covered by known cyclic-extension theory.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0010_v1.md#whole-artifact-finding) supports this complete degree-reduction investigation, including its coefficient and inverse-domain limits.

The [completed complementary-block screen](../ledger/Yin_L_A0007_v1.md#actual-setting-and-the-first-complementary-block) identifies the complex-phase numerator and removes the resolvent commutator by constant pivots followed by the existing cyclic test.
For the free-group complex-phase and anticommutator numerators, explicit finite-support vectors exclude every scalar-phase positive-real-part certificate; the stated original matrix realizations also fail their specified constant-weight tests.
An [independent character-orbit certificate](../ledger/Yin_L_A0007_v1.md#the-character-orbit-certificate) combines the already audited MSY23 Lemma 5.19 dimension sum with a trace-preserving phase orbit to exclude nonzero eigenvalues of a homogeneous affiliated matrix.
The [companion reduction](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials) extends this to one-sided graded polynomials with an independently invertible extreme coefficient.
Under a common grading assigning degree one to the two selected elements, these certificates supply the missing actual-unit multipliers, resolve the full complex reciprocal-ratio parameter family and the anticommutator, and preserve the exact affiliated kernel dimensions.
Their positive conclusions already belong to the [known cyclic-extension rank mechanism](../ledger/Yin_L_A0007_v1.md#scope-and-continuation), and the free-group examples have complete Lin93 coverage.
The extra grading is not implied by torsion-freeness, and a noninvertible or unproved extreme coefficient cannot be discarded by companion notation.
The [independent complete review](../audits/reviews/Yin_R_A0009_v1.md#whole-artifact-finding) supports the whole screening and character-companion investigation, with all degenerate cases and its source-foundation limits explicit.

The [kernel-preserving normalization tests](../ledger/Yin_L_A0006_v1.md#coupled-pencil-normalization) give an explicit unmatched off-diagonal inverse entry that becomes a matched diagonal compression after right multiplication by a unit independently certified through a cyclic factorization.
In the selected free-group example, a character orbit excludes every exact-value positive matched realization, while the same-denominator transfer preserves the scalar and bordered kernel dimensions through affiliated rank invariance.
The original border nevertheless already has a direct cyclic complementary-block proof, so this successful transfer supplies no additional independent rank constraint.
The [reciprocal-ratio calibration](../ledger/Yin_L_A0006_v1.md#secondary-calibration-a-reciprocal-ratio-schur-complement) gives a second ordered transfer and a positive-real parameter family whose multipliers are independently certified by the existing cyclic or energy tests.
Its endpoint is the previously established positive resolvent sum; the later character certificate above resolves its complex-parameter branch under a common grading, while the unrestricted torsion-free branch remains unresolved.
The original coupled-pencil and positive-real reciprocal-ratio conclusions hold in every torsion-free group under their stated hypotheses, while the later complex-parameter extension retains its additional grading assumption.
The [independent whole-artifact review](../audits/reviews/Yin_R_A0008_v1.md#whole-artifact-finding) checks both calibrations, all parameter cases, closed affiliated kernel dimensions and the exact limits of these conclusions.

The [energy and regular-transport result](../claims/Yin_C_A0003_v1.md#statement) excludes the forbidden interval for matched constant borders when a positive real part has no kernel left invisible to the border.
Its cyclic certificate reduces that condition to a finite complex-matrix rank test using the absence of eigenvectors for infinite-order regular group unitaries.
Its finite labeled-graph certificate computes the kernel dimension as the number of components with identity transport around every closed walk.
An injective positive real part also proves denominator admissibility without a spectral gap, independently of the general Atiyah property.
The [companion investigation](../ledger/Yin_L_A0005_v1.md) fixes the exact scalar reduction, domain interface and limits of finite-support and compression approaches.
Even uniformly accretive denominators with polynomial bounded inverses encode every scalar group-ring injectivity problem when the two borders are unmatched.
An actual bounded-denominator border over a free group has a one-dimensional analytic kernel with no nonzero finite-support vector; its allowed endpoint rank does not refute an extraction principle restricted to the forbidden interval.
The [independent Claim review](../audits/reviews/Yin_R_A0007_v1.md#claim-finding) and [complete exploration review](../audits/reviews/Yin_R_A0007_v1.md#exploration-finding) support these exact scopes and retain the unresolved arbitrary-border problem.

The [linear-pencil investigation](../ledger/Yin_L_A0004_v1.md#setting-and-exact-criteria) specializes MSY23 Theorem 5.25 and proves the equivalent linear-only integer-rank, division-closure-fullness and restricted bordered criteria.
The rational-closure-fullness equivalence is already in MSY23; the additional formulations are direct consequences of its linearization mechanism.
Fullness over the actual rational or division closure cannot simply be replaced by fullness over the group ring.
The [Laurent counterexample](../ledger/Yin_L_A0004_v1.md#a-group-ring-full-linear-pencil-that-is-analytically-singular) is a three-by-three affine pencil over \(\mathbb C[\mathbb Z^3]\) with group-ring inner rank three and analytic rank two, although this group satisfies the complete complex Atiyah property.
The direct augmentation-ideal proof verifies the Laurent adaptation of Cohn's classical polynomial example.
The [independent whole-argument review](../audits/reviews/Yin_R_A0006_v1.md#whole-argument-finding) supports the complete investigation at its stated source and affiliated-foundation scope, without claiming a new positive group class.

The [first mechanism tests](../ledger/Yin_L_A0002_v1.md) establish cyclic rational invertibility, mixed resolvent sums with nonzero scalar real part, and a noncommutative Klein bottle calibration.
They also exhibit a general finite-tracial obstruction to deriving rational invertibility from scalar polynomial injectivity alone.
The actual proofs, coefficient and domain limits, Ore obstruction and source qualifications remain in that fixed record.
These tests provide no new group-class coverage.

The [Ele03 matrix deduction](../claims/Yin_C_A0001_v1.md#statement), with its [independent whole-argument review](../audits/reviews/Yin_R_A0002_v1.md#whole-argument-finding), settles the proposed scalar-kernel extraction for finitely generated amenable groups and the stated scalar-denominator Schur complements.
The boundary estimate has error equal to the number of input components times the Følner boundary fraction.
If a nonzero Schur complement has a kernel, the polynomial block matrix yields a nonzero group-ring element with an analytic kernel.
This reduces that amenable case to scalar analytic injectivity; it neither derives amenability nor scalar injectivity from torsion-freeness.

The [index-two investigation](../ledger/Yin_L_A0003_v1.md#results-and-source-scope) now completes the faithful actual crossed product, matrix-level inverse closure and full rational norm criterion.
For \(G=\langle x,y,z\mid x^2y^2z^2=1\rangle\) with its parity kernel, a leading-coefficient reduction excludes all rational norm solutions.
The parity character has no integer lift, so this improves on that particular elementary test, but the group is already free-by-cyclic and covered by Lin93.
The residue argument uses an independent cyclic quotient and known free-group division closures; it does not derive the required structure from torsion-freeness alone.
The complete worked investigation has the [independent review](../audits/reviews/Yin_R_A0005_v1.md#whole-argument-finding), with its accepted foundations and unresolved general scope explicit.

## Strategic reassessment

The 10 November 2026 reassessment retained this route as the main approach and selected a structured finite-extension test over unrestricted depth-one experiments.
Yin's subsequent request returns the immediate focus to the MSY23 linear-full characterization; its exact group specialization and coefficient-ring limits are now established above.
The finite-extension investigation remains a completed calibration and potential application of the linear rank criterion.
The amenable extraction and the [completed JZ19 tensor argument](../claims/Yin_C_A0002_v1.md#statement) close two specific interfaces; neither provides the missing implication from torsion-freeness to rational invertibility.
The tensor argument works for arbitrary affiliated operators, so its conclusion alone does not distinguish the group-ring setting.
For a scalar rational element \(r\), its centralizer lower bound gives
\[
\dim_{G\times G}C_{HS}(r)\geq\bigl(\dim_G\ker r\bigr)^2.
\]
This is compatible with a proper nonzero kernel unless an independent upper bound or discreteness statement is established.
The [JZ19 upper-bound mechanism](../audits/literature/JZ19/Yin_U001.md#hilbert-schmidt-mechanism) excludes eigenvalues outside the coefficient field through sofic product-group approximation and strict eigenvalue finiteness; it does not exclude zero, which already belongs to that field.
Its [strong Atiyah assembly](../audits/literature/JZ19/Yin_U001.md#base-change-proof) obtains the needed integer-rank input from the additional algebraic-coefficient Atiyah premise.
Consequently, further general cutoff or tensor refinements are support work when a specific application requires them, rather than the default candidate for the missing group-specific mechanism.

The retained [finite-tracial obstruction](../ledger/Yin_L_A0002_v1.md#why-infinite-orbits-and-scalar-injectivity-do-not-finish-the-argument) rules out an argument based only on finite trace and scalar polynomial injectivity, without refuting the canonical group-ring conjecture.
A useful continuation must exploit additional information about actual rational expressions, the group's relations or its canonical trace.
The [JZLA20 reduction](../audits/literature/JZLA20/Yin_U001.md#general-torsion-free-boundary) illustrates the distinction: the cyclic quotient of the finite source subgroup and its compatible rank extension make rational-complexity induction work.
Torsion-freeness alone does not supply that reduction, and relabeling the expression complexity does not replace it.

## Next discriminating step

Seek an independent constraint excluding
\[
N<\operatorname{rk}_G\begin{pmatrix}0&u\\v&L(X)\end{pmatrix}<N+1,
\qquad L(X)\in GL_N\bigl(\mathcal U(\mathcal N(G))\bigr),
\]
for every affine linear pencil in group generators and their inverses, with scalar row \(u\) and column \(v\).
The [bordered equivalence](../ledger/Yin_L_A0004_v1.md#proof-of-the-linear-and-bordered-equivalences) identifies this exact forbidden interval with a proper nonzero analytic rank of the scalar rational Schur complement.
The equivalence itself gives no torsion-free mechanism, bounded inverse or uniform bound on pencil size.
This formulation avoids first classifying fullness over an unknown closure, but the admissibility of \(L\) remains an actual affiliated-invertibility condition.
Do not replace it by formal free fullness or group-ring inner-rank equality, both of which fail the retained tests.

The present positive mechanism can be tested on specific rational realizations through a positive energy certificate or a justified kernel-preserving transformation using independently known invertible factors.
Preserve the exact border matching and real-part hypotheses of [the proved argument](../claims/Yin_C_A0003_v1.md#argument), including the extra admissibility premise when the positive part has a kernel.
Do not seek a universal exact-value-preserving conversion into that class: its scalar values lie in a rotated accretive half-plane, while a nonidentity regular group unitary does not, as shown in the [realization obstruction](../ledger/Yin_L_A0005_v1.md#a-positive-realization-restricts-the-scalar-value).
Replacing \(L\) by \(L^*L\) changes the border and does not provide that conversion.
The [complementary-block reduction](../ledger/Yin_L_A0005_v1.md#complementary-block-reduction-and-the-scalar-obstruction) shows that already a two-state denominator retains a scalar analytic zero-divisor problem.
Apply that reduction before investing in another normalization, and select a complementary block whose rank is not already supplied by the cyclic, coefficient-dominance or positive-energy certificates.
Then test for the [graded extreme-coefficient reduction](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials), including its known natural-extension coverage.
Use the [stable degree-reduction induction](../ledger/Yin_L_A0008_v1.md#terminating-induction-for-word-polynomials) to reach a specified matrix base class, keeping its size increase and exact kernel dimension explicit.
An independently invertible extreme coefficient is already covered; the two-resolvent and ordered-product families are now covered for every indicable supporting subgroup.
Do not substitute scalar entry tests or a fixed-size assertion for the required all-size affine matrix statement.
For size reduction, first test the [closed scalar-induction classes](../ledger/Yin_L_A0009_v1.md#consequence-for-the-general-induction-attempt): two monomial terms in each entire row, constant proportionality with a certified pivot, or an independently injective positive real part.
Then test the [explicit cyclic row and column factors](../ledger/Yin_L_A0010_v1.md#an-explicitly-preserved-coefficient-class) and any already justified finite-index coefficient-field realization before treating a three-term example as unresolved.
For a semidefinite real part with explicit zero coordinates, test the [preserved imaginary-compression condition](../ledger/Yin_L_A0011_v1.md#a-pair-of-conditions-preserved-by-scalar-elimination) before treating a noncyclic next pivot as unresolved.
The energy branch still needs a separate certificate when that compression has uncontrolled kernel or loses the specified positivity.
For inverse-difference arrays with central column parameters, target the exact [transformed row separation](../ledger/Yin_L_A0011_v1.md#a-shape-invariant-with-central-column-parameters), distinguishing a certified merger from a nonzero separation whose actual rank remains unknown.
Any relative-path spectral alternative must certify the relative operator's joint trace information, not merely individual diffuseness or an abstract torsion-free presentation.
The [three-term equivalence](../ledger/Yin_L_A0010_v1.md#an-elementary-row-splitting-step) rules out treating row sparsity alone as a weaker intermediate conjecture; it does not rule out a successful structural induction.
Keep matrix size, word length, additive term count and rational inverse domain distinct; a decrease in one does not establish a decrease or a certificate for the others.
Select a specific remaining expression with no usable character reduction, or with an extreme coefficient whose actual invertibility requires a separate argument.
Check characters on the subgroup carrying the expression's coefficients; failure of a character to extend to the whole ambient group is not an obstruction to the subgroup calculation.
For each proposed multiplier, identify its independent actual-invertibility proof before using its inverse; a formal expression or an application of the whole group's known Atiyah theorem does not supply the requested new constraint.
The [indicable-support comparison](../ledger/Yin_L_A0008_v1.md#a-singleton-extreme-support-term-and-the-earlier-examples) separates the enlarged completed scope from the remaining general torsion-free multiplier problem, without asserting a new open problem or excluding other methods.
Further finite-propagation work needs a mechanism sensitive to actual rationality and to the strict fractional interval, beyond bounded graph cutoffs or unrestricted finite-support extraction.

The [index-two finite-extension probe](Yin_S_A0001.md#first-discriminating-step) retains its completed actual-closure and norm interfaces as a structured comparison.
Its first calibration is finished; further investment needs a concrete extension beyond known finite-extension coverage or an invariant that works when the demonstrated cyclic reduction is unavailable.
The retained Promislow example has no nonzero ambient homomorphism to \(\mathbb Z\), providing a distinct possible mechanism test whose positive Atiyah result is already known.
A merely conditional restatement of the absence of rational norm solutions still supplies no new constraint.
An actual norm solution would now have the [explicit finite-matrix obstruction](../ledger/Yin_L_A0003_v1.md#complete-norm-criterion-and-the-half-rank-witness), once its rational representation and group hypotheses were verified.
No such solution or new positive group class has been obtained.

Retain the earlier depth-one family as a comparison problem:
\[
r=(1-f)-(1-h)(1-g)^{-1}(1-k),
\qquad g\ne e,
\]
whose cyclic denominator is justified directly by torsion-freeness.
Return to this family when explicit relations suggest a group-ring elimination or canonical-trace argument that forces \(r=0\) or \(\ker r=0\).
The [continuation analysis](../ledger/Yin_L_A0002_v1.md#precise-continuation-point) states the corresponding block matrix and the original scalar kernel-extraction question.
The amenable scope is now covered above; the arbitrary torsion-free scope remains unresolved.
Assuming integer rank of that block matrix would be circular; generic expression induction and arbitrary finite-support kernel extraction have already failed the recorded tests.
Keep the complex-phase two-resolvent numerator only in cases not already settled by the graded or other retained reductions, without claiming an established open or novel status.
Any successful restricted test must subsequently be extended to arbitrary rational presentations before it can resolve the selected group's full Task.

## Decision conditions and contribution

Continue if the construction supplies an independent invertibility or kernel-vanishing argument applicable to the actual rational closure beyond an already known class, or removes a specific obstruction in the infinite-edge route.
Pause if it merely restates the known closure equivalence, assumes the desired matrix integrality, or imposes free-field realization incompatible with the group's relations.
The exact equivalence is established source input; a new mechanism proving its division-ring side and a new positive case remain unresolved.

## Source-audit findings

Yin's requested audits of Ele03, JZ19, JZLA20 and Lin93 have now read their complete selected editions.
Lin06 has the requested localization, Proposition 2.2 and Theorem 2.6 inspection, and Bar19 has the full Kielak appendix with its necessary preceding construction.
The actual source proofs, corrections, accepted foundations and unverified steps remain in their responsible units.

| Source | Consequence for this route |
| --- | --- |
| [Ele03](../audits/literature/Ele03/Yin_U001.md#boundary-proof) | Finite propagation makes the finite restriction possible; the Følner limit turns positive kernel dimension into a finite-support witness. Rational inverses need block linearization and cannot inherit finite propagation directly. |
| [JZLA20](../audits/literature/JZLA20/Yin_U001.md#general-torsion-free-boundary) | Rational tree complexity is usable only with its lower-complexity invertibility hypotheses and a suitable regular ambient comparison. Local indicability supplies the cyclic quotient of the expression's finite source subgroup; Hughes freeness identifies the actual analytic envelope. |
| [Lin93](../audits/literature/Lin93/Yin_U001.md#transfer-boundaries) | The free-tree finite-rank defect and the elementary amenable extension machinery supply the missing rank information for their stated classes, without scalar Ore localization. |
| [Lin06](../audits/literature/Lin06/Yin_U001.md#scope-for-schur-complements) and [Kielak's appendix](../audits/literature/Bar19/Yin_U001.md#affiliated-applicability-boundary) | Classical scalar fractions require the explicit Ore/domain hypotheses. For a field group algebra known to be a domain, nonamenability excludes Ore localization but does not exclude an actual rational division closure. |
| [JZ19](../audits/literature/JZ19/Yin_U001.md#affiliated-and-schur-applicability) | Coefficient change and canonical ranked envelopes transfer established matrix-rank information. The strong Atiyah deduction retains soficity and the algebraic-coefficient Atiyah premise. |

The [JZ19 cutoff tensor step](../claims/Yin_C_A0002_v1.md#statement) now has a complete domain-sensitive proof and the independent review selected there.
Its [source supplement](../audits/literature/JZ19/Yin_U001.md#lemma-910-2-completion) makes spectral distinctness explicit and replaces the unsupported cutoff-space codomain by the full Hilbert tensor product.
This resolves the selected analytic checking gap and proves the centralizer lower bound for arbitrary affiliated operators; it does not supply the separate upper bounds or integer ranks needed by the Atiyah argument.
The later coefficient-change assembly and its other external inputs are not independently re-reviewed by this local completion.
The source units also retain local statement/formula repairs without treating them as refutations of the main theorems.

Reuse the existing MSY23 and Lin00 proof inspections at their documented scopes.
Beyond the amenable test, a useful continuation must supply a replacement for the vanishing-boundary argument or the local-indicability reduction, rather than assuming the desired block-matrix integrality.
