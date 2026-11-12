---
author: Yin
---
# Central winding and quotient atoms: independent whole-artifact review

Review act: 2026-11-11T16:31.
The human record author is Yin.
The reviewed fixed input is [L_A0019 v1](../../ledger/Yin_L_A0019_v1.md#central-winding-and-the-disappearance-of-torsion-quotient-atoms), including its introduction, all six sections, equations (1)--(11), degeneracies, source scope and continuation limits.
This was an initial independent inspection by an agent outside the substantive development of that input.
No development draft, proof-generation dialogue, author explanation or earlier review of L_A0019 was supplied or consulted.
The reviewer first enumerated the obligations from the fixed artifact, then checked the argument and directly needed fixed mathematical and primary-source passages.
No previous project-review conclusion was used to supply the finding below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [L_A0019 v1](../../ledger/Yin_L_A0019_v1.md#central-winding-and-the-disappearance-of-torsion-quotient-atoms) | Complete fixed artifact, including its introduction, scalar conclusion, source boundaries and absence of a general Atiyah claim. |
| [Whole-artifact finding](#whole-artifact-finding) | [Actual group](../../ledger/Yin_L_A0019_v1.md#the-actual-group-and-the-winding-coordinate) | Presentation, centrality, integer height, unique central normal form, quotient kernel and torsion-freeness for every p,q at least two. |
| [Whole-artifact finding](#whole-artifact-finding) | [Full joint trace](../../ledger/Yin_L_A0019_v1.md#a-full-joint-trace-identity-not-just-a-scalar-moment-fit) | Representations, all-word trace averaging, measurable branches, spectral-law disintegration and dominated boundary-atom passage. |
| [Whole-artifact finding](#whole-artifact-finding) | [Scalar exclusion](../../ledger/Yin_L_A0019_v1.md#independent-atom-exclusion-from-the-winding-fibers) | Cyclic marginal laws, free independence, finite collision set, strict atom threshold, all real spectral values and zero-coefficient cases. |
| [Whole-artifact finding](#whole-artifact-finding) | [Mixed-power example](../../ledger/Yin_L_A0019_v1.md#the-mixed-power-test-and-its-fractional-quotient-atoms) | Both exceptional fibers, their complete atom lists, generic fiber atomlessness and the failure of quotient specialization to preserve the canonical group law. |
| [Whole-artifact finding](#whole-artifact-finding) | [Known coverage](../../ledger/Yin_L_A0019_v1.md#known-coverage-and-what-this-test-does-not-establish) | Unequal and equal exponent height arguments, root-language comparison, matrix trace normalization and the limits of scalar atom exclusion. |
| [Whole-artifact finding](#whole-artifact-finding) | [Source scope and continuation](../../ledger/Yin_L_A0019_v1.md#source-scope-and-continuation-decision) | Applicability of the identified BBL21 and AER26 passages and the bounded scalar conclusion, without inheriting an original-source proof audit or certifying development history. |

## Obligations and decisive checks

### Actual group and canonical trace

The height map respects the defining relation because both powers have image \(pq/\gcd(p,q)\).
Its nonzero value on the central element excludes a finite central order.
Extracting complete powers leaves an alternating reduced word whose image in \(C_p*C_q\) determines every residual syllable.
Equality of two representatives therefore reduces to equality of central powers, and the height map distinguishes their exponents.
This proves uniqueness and the precise quotient kernel without assuming a stronger normal-form theorem.

Cyclic reduction in the free product shows that a finite-order quotient element is conjugate into a factor.
After lifting that conjugation, the original element is a central power times a power of one generator, hence a power of that generator.
The nonzero generator height then excludes nontrivial torsion.
The trivial quotient-image case is included.

Both defining powers of each fiber representation equal the same scalar \(e^{i\theta}\).
A nonempty alternating residual word has zero canonical quotient trace, while a pure central power has trace \(e^{im\theta}\).
Haar integration consequently selects exactly the identity coefficient for every group-ring word, including words with inverses.
Positivity and traciality hold on the full group ring from the actual unitary representations; no extension of each individual fiber state to the reduced group algebra is needed for this calculation.
Replacing \(\theta\) by \(\theta+2\pi\) is a trace-preserving character automorphism of the quotient factors, so it preserves the scalar laws.

### Spectral measures and the boundary limit

The finite coefficient sum bounds the norm of the selfadjoint input and all fiber images on one compact real interval.
Equality of moments gives equality against every continuous function by uniform polynomial approximation.
The fiber operators depend norm-continuously on the chosen interval, so their continuous functional-calculus traces are measurable.
This supplies the asserted measurable spectral-measure average.

For each fixed real \(\lambda\), the functions \(h_{\eta,\lambda}\) lie between zero and one and converge pointwise to the singleton indicator.
Dominated convergence applies to each finite spectral measure and then to Haar integration.
The boundary-atom formula needs no uniform gap, small-singular-value estimate or continuation of a return series.
The later exceptional set is independent of \(\lambda\), so almost-everywhere fiber atomlessness controls every real \(\lambda\), without a union over uncountably many null sets.

### Free scalar summands and parameter cases

The canonical cyclic generator has uniform law on its roots of unity, giving the locations and weights in equation (7) by direct functional calculus.
Alternating products of centered factor elements expand into nonempty reduced words, proving the precise freeness needed for the scalar additive criterion.
For distinct residues, equality of cosine values cannot arise from equal angles modulo \(2\pi\).
The other alternative is the displayed affine condition on \(\theta\), with nonzero slope and finitely many solutions in the bounded interval.
The finite union over pairs in both factors leaves exactly the weights \(1/p\) and \(1/q\) off the exceptional set.
Their sum is at most one, while a positive free-sum atom requires a strict inequality.
This verifies the endpoint \(p=q=2\) as well.

If exactly one coefficient vanishes, the remaining infinite-order generator has Haar spectral law on the circle.
Writing \(\gamma\ne0\) for its coefficient, the real Laurent polynomial \(\gamma u+\bar\gamma u^{-1}\) is nonconstant and has finite level sets, proving atomlessness directly.
If both coefficients vanish, the law is \(\delta_0\), as explicitly excluded from the atomlessness conclusion.
The identification of a scalar atom with kernel dimension uses the canonical scalar trace normalization.

### Complete mixed-power calculation

For \((p,q,c,d_0)=(2,3,1,1)\), the zero-winding marginal supports are \(\{2,-2\}\) with weights \(1/2\), and \(\{2,-1\}\) with weights \(1/3,2/3\).
Only pairs using the weight \(2/3\) exceed the threshold.
Their sums are \(1\) and \(-3\), each with weight \(1/2+2/3-1=1/6\), and there are no other atoms.
At \(\theta=\pi\), the first summand vanishes identically and the second-factor locations are \(1,-2,1\), giving the complete law \((2/3)\delta_1+(1/3)\delta_{-2}\).
The first-factor collision occurs only at \(\pi\), and the second-factor collisions occur only at \(0\) and \(\pi\) modulo \(2\pi\).
Every other fiber has maximal input weights summing to \(5/6\), so is atomless.
Both exceptional fibers have Haar measure zero and contribute no atom to the canonical group law.

Setting the winding variable to one counts every central power, whereas the constant coefficient counts only the zero central power.
The example establishes the claimed obstruction to transferring a quotient atom through this torsion-free central lift.
It does not identify an exceptional representation trace with the original canonical group trace.

### Earlier coverage and matrix limits

The [singleton extreme-support argument](../../ledger/Yin_L_A0008_v1.md#a-singleton-extreme-support-term-and-the-earlier-examples) applies when \(p\ne q\): the positive generator heights differ, so the highest supported term of \(X-\lambda\) is a single nonzero scalar multiple of a group unit.
For \(p=q\), both heights are one, and the extreme term factors as \(a(c+d_0a^{-1}b)\).
The quotient normal form gives \(a^{-1}b\ne e\), so torsion-freeness makes it infinite-order.
The [cyclic Fourier argument](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) gives an actual affiliated inverse for this nonzero binomial factor.
Multiplying by that independently established homogeneous inverse and reversing the height reduces to the [graded companion criterion](../../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials).
The character-orbit step and companion elimination were checked at this interface, including the [bounded-row eigenprojection argument](../literature/MSY23/Yin_U006.md#lemma-519-domain-repair), without a general division-closure premise.
The known-coverage claim is therefore valid for the entire scalar family.

The [root-language comparison](../../ledger/Yin_L_A0016_v1.md#even-cyclic-root-closure-and-positive-moments-do-not-suffice) has the narrower information claimed: its aggregate counts do not form a compatible group identity language.
Its length-one count forces two identity letters, and root closure then leaves at most six length-two identity words, contradicting the required eight.
The current full-word representations supply inverse and multiplication compatibility absent from those aggregate constraints.

For selfadjoint matrix inputs, the same functional-calculus argument uses the finite unnormalized trace of total mass equal to the matrix size.
For an arbitrary rectangular group-ring matrix \(A\), its kernel version follows by applying the argument to \(A^*A\), whose zero spectral projection is the kernel projection of \(A\), globally and in each fiber.
This is the spectral scope of the matrix extension of equations (3)--(5); it assigns no real spectral law to an arbitrary nonnormal matrix.
Trace disintegration alone imposes no integer constraint on its integral, and the scalar sum threshold does not handle general matrix polynomials.
The caution about moving fiber atoms and their level sets is necessary and consistent with the result.

## Source applicability and inspection limits

The reviewer directly read the matching [BBL21 arXiv v2 Introduction](https://arxiv.org/html/1903.09002v2#S1), including the strict scalar threshold, converse, exact trace formula and reference [10] to Bercovici--Voiculescu.
Its hypotheses match the bounded free selfadjoint summands in the faithful finite canonical quotient trace.
The scalar theorem is accepted as an established analytic input; its original proof, the full BBL21 paper and the final journal edition were not independently audited.
The existing [BBL21 source unit](../literature/BBL21/Yin_U001.md#bbl21-u001) was read for the prepared theorem boundary, without adopting its other source-proof or correction findings as this review's work.

The reviewer directly read [AER26 arXiv v1](https://arxiv.org/html/2605.12793v1#S3), Definition 1.3, Lemma 3.1, Corollary 3.2, Definition 3.3 and Section 3.1, together with the presentation identification in Section 8.2.
These passages match the central normal form and constant-winding-coefficient attribution.
The local proof independently supplies uniqueness and torsion-freeness, including the all-exponents-two case treated separately in AER26.
No asymptotic or local-limit conclusion from AER26 is used, and no proof review of those conclusions is claimed.
The artifact's account of its development agents' previous reading is not an independently audited historical fact.
No exhaustive novelty or historical-priority search was performed or required for the artifact's expressly limited claims.

## Whole-artifact finding

No unresolved mathematical gap was found in the complete fixed L_A0019 v1 artifact at its stated scope.
The full-word trace identity, justified atom disintegration, scalar atomlessness, both exceptional-fiber calculations and earlier-height-coverage comparison are valid under the stated hypotheses.
The selected primary sources support the uses and attributions checked here, with the explicit accepted-analytic-input boundary above.
The result is a complete bounded scalar discriminator and a quotient-transfer obstruction; it neither proves new general matrix integrality nor completes the [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract).
This is an independent mathematical review, not formal proof-assistant verification or a full source-proof audit.
