---
author: Yin
---
# Cauchy boundary residues and probability strategies: independent whole-artifact review

Review act: 2026-11-11T09:15 UTC, recorded for Yin.
The reviewed input is the 2026-11-11 revision of [L_A0015_v1](../../ledger/Yin_L_A0015_v1.md), including every displayed formula (1)--(21), the exact equivalences, the source interfaces and the stated limitations for [A0001](../../tasks/Yin_T_A0001_v1.md#contract).
This is a separately arranged initial whole-artifact mathematical inspection by an agent outside substantive development.
The reviewer received the fixed artifact, its necessary dependencies, the review assignment and administrative authorization metadata, without proof-generation discussion, development summaries or previous review conclusions.
The fixed artifact's own arguments and its identified source records were read as necessary mathematical inputs.
No previous project R finding was used to establish this finding, no substantive correction was supplied, and no strategy revision was inspected.

The evidence below is necessary new independent inspection evidence for this fixed synthesis, rather than a duplicate account of its proofs.
The review covers the complete mathematical artifact and its uses of accepted foundations, not a new proof of the external foundations or completion of A0001.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete Cauchy and probability synthesis](../../ledger/Yin_L_A0015_v1.md) | Complete 2026-11-11 mathematical body, formulas (1)--(21), all asserted equivalences, source applicability and strategy limitations. |
| [Whole-artifact finding](#whole-artifact-finding) | [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract) | Quantifiers, complex coefficients, rectangular matrix sizes, unnormalized kernel dimension and comparison with the original target; no completion finding. |
| [Whole-artifact finding](#whole-artifact-finding) | [Matrix atom equivalence](../../ledger/Yin_L_A0012_v1.md#matrix-atoms-an-exact-formulation-without-rational-inverses) | Both directions, normalized atom masses and rectangular-to-positive-square reduction used by L_A0015. |
| [Whole-artifact finding](#whole-artifact-finding) | [Selfadjoint affine reduction](../../ledger/Yin_L_A0012_v1.md#selfadjoint-affine-linear-tests-suffice) | The block with diagonal entry minus the identity preserves the original nullity and uses its actual enlarged matrix size. |
| [Whole-artifact finding](#whole-artifact-finding) | [Scalar rational law equivalence](../../ledger/Yin_L_A0012_v1.md#scalar-rational-laws-either-a-point-mass-or-no-atoms) | Actual affiliated rational closure, bounded transforms, endpoint projection identity and both directions of the division criterion used in (9) and (14). |
| [Whole-artifact finding](#whole-artifact-finding) | [Linear-pencil equivalence proof](../../ledger/Yin_L_A0004_v1.md#proof-of-the-linear-and-bordered-equivalences) | Integer affine-pencil ranks imply division through the bordered representation and then all matrix ranks; only this adopted reduction is covered. |
| [Whole-artifact finding](#whole-artifact-finding) | [MSY23 linear representation](../literature/MSY23/Yin_U003.md#lemma-48-linearization-preserves-an-existing-inverse-domain) | Accepted inverse-domain-preserving linear representation in the fixed ambient affiliated algebra; local block-interface reasoning checked. |
| [Whole-artifact finding](#whole-artifact-finding) | [MSY23 Theorem 5.25](../literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence) | Accepted exact equivalence of strong Atiyah integrality and division of the actual rational closure; no free-field identification inferred. |
| [Whole-artifact finding](#whole-artifact-finding) | [BBL21 boundary recovery](../literature/BBL21/Yin_U001.md#cauchy-boundary-recovery) | Matching arXiv v2 Lemmas 2.1 and 2.3 directly checked for attribution, topology and the invertible expected-kernel hypothesis. |
| [Whole-artifact finding](#whole-artifact-finding) | [Bia97 source record](../literature/Bia97/readme.md#scoped-reading-on-2026-10-10) | Reused statement and normalization evidence for Section 3, Lemma 2 and Corollary 3; positive variance and transported density coordinate matched. |
| [Whole-artifact finding](#whole-artifact-finding) | [MSY23 entropy interface](../literature/MSY23/Yin_U005.md#section-61-how-entropy-supplies-maximal-delta) | Accepted one-variable non-microstates entropy-dimension formula for bounded selfadjoint variables, with the recorded external analytic boundary. |
| [Whole-artifact finding](#whole-artifact-finding) | [MSW17 conjugate-variable interface](../literature/MSW17/Yin_U001.md#exact-selfadjoint-specialization-of-condition-a) | Reused Theorem 2.5 algebraic-freeness interface for a bounded selfadjoint tuple; applied only to the stated obstruction from a polynomial relation. |

## Obligations and decisive checks

### Boundary recovery and complete matrix quantifiers

The cone bound in (1) is valid because the numerator has modulus at most \(\sqrt{1+C^2}\operatorname{Im}z\), while the denominator has modulus at least \(\operatorname{Im}z\).
Dominated convergence gives the angular residue, and (2) supplies its vertical imaginary-part form with the correct sign for \((z-H)^{-1}\).
The mass is \(\nu_n(p)/n\), so (3) restores integer unnormalized nullity without losing a factor of \(n\).
Applying the condition to \(H-aI\) proves the forward direction; using \(A^*A\) at zero proves the converse for every rectangular \(A\).
The selfadjoint affine test inherited from L_A0012 uses a block of size \(2n\) whose nullity equals that of the original pencil, rather than twice that nullity.
The adopted affine-pencil argument uses an actually invertible denominator and the rank identity for its bordered matrix.
All finite sizes and arbitrary complex coefficients remain quantified.
Finite support and the Task's coset decomposition extend the finitely generated formulation to the stated discrete-group contract.

Strict negativity of the imaginary part of a probability Cauchy transform makes its scalar reciprocal well defined.
Thus (4)--(5) follow from the residue and exhaust the two cases: a positive atom gives finite ratio \(1/m\), and zero mass gives infinite modulus.
The examples \(\delta_1\) at zero and the arcsine endpoint correctly separate a finite angular derivative, the zero boundary value and finite reciprocal slope.
The statements do not infer meromorphic continuation from an atom.

For (6), Cauchy--Schwarz gives the asserted resolvent bound, and tightness plus atomlessness gives uniform decay of mass in intervals of shrinking radius.
An atom obstructs that decay through (1).
Consequently (7) is equivalent to the exact quantized atomic masses: there are at most \(n\) nonzero atoms, their removal leaves a positive atomless remainder, and no additional atom can remain under (6).
The fixed-measure estimate supplies no uniform rate over the tested matrices.

### Positive resolvents, actual rational closure and Schur energy

The integrand in (8) decreases to the indicator of zero as \(\varepsilon\downarrow0\), and the sign in \(-\varepsilon g_K(-\varepsilon)\) is correct.
For an actual affiliated rational element, spectral calculus identifies the endpoint projection of \(q_r\) with the kernel projection of \(r\).
A nonzero square affiliated operator with zero kernel in a finite von Neumann algebra has dense range and an affiliated inverse; inverse closure then places that inverse in the actual rational closure.
This verifies both directions of (9), including the distinction between zero mass at one and atomlessness everywhere.
The scalar example \(q_1=\tfrac12 1\) correctly excludes the stronger false condition.
The argument permits necessary unbounded intermediate inverses and makes no free-field assumption.

The scalar cyclic representation gives (10) by the Schur complement with its displayed sign.
For (11), finite \(E_\lambda\) is exactly the spectral-calculus condition for solving the second eigenvector equation with first coordinate one and squared complementary norm \(E_\lambda\).
Cyclicity removes an eigenvector orthogonal to the cyclic vector, so an additional component in \(\ker(\lambda-D)\) cannot alter the projection mass.
The remaining first-coordinate equation is precisely the stated balance equation.
This proves the reciprocal norm formula for the atom and hence (12).
The two-point example attains arbitrary positive energy, showing why positivity alone gives no required discrete set.
The compressed operator and the cyclic representation of a normalized matrix law are not silently identified with a group-ring convolution or a single diagonal entry.

### Free heat, entropy and logarithmic observables

At positive height, the defining threshold for \(v_t\) is attained and its integral equals \(1/t\).
The estimate \(v_t\leq\sqrt t\) makes the integrand in the mass formula converge pointwise away from the tested atom, and it is bounded by one.
A positive atom forces positive height for all \(t>0\); zero-height subsequences in the atomless case therefore cause no gap in (13).
Biane's density identity yields the factor \(\pi^2\) and the transported coordinate \(\psi_t(x)\).
The scalar semicircular perturbation must be free from the entire normalized tracial algebra, as the artifact states.

The accepted scalar entropy formula gives \(\delta^*=1\) exactly for atomlessness and \(\delta^*=0\) exactly for a Dirac law.
If an atom has mass \(m\in(0,1)\), then the sum of squared atomic masses lies between \(m^2\) and \(m^2+(1-m)^2<1\).
Thus a partial kernel of a rational element forces a strictly intermediate entropy dimension for its bounded transform.
Together with the checked division criterion, this establishes every direction in (14), including sufficiency of testing all \(q_r\).
The proposed power-law density bound with exponent below \(1/2\) implies the exact little-oh condition but is stronger than it.
No such bound is proved here, and the relation \(X^2+Y^2=1\) correctly blocks an ordinary full-tuple conjugate system for real and imaginary parts of a Haar unitary.

In (15), differentiation takes place at each positive regularization parameter, where bounded functional calculus applies.
The logarithmic quotient is uniformly bounded on the fixed bounded support and has the stated pointwise limit, even when the nonzero spectrum is not of determinant class.
The given atomless density integrates to one and has logarithmic integral minus infinity, so determinant vanishing alone does not detect a kernel.
For the positive contraction in (16), both the powers and the Abel kernel are bounded by one and converge to the endpoint indicator.
Differentiating the convergent determinant series gives the sign and factor in the first limit of (17), while the second is the same bounded-support logarithmic argument.
The coefficients remain complex weighted return amplitudes in general, rather than Markov transition probabilities.

### Cyclic arithmetic, counterexample and graph mechanism

For (18), a repeated admissible word forces its primitive index path to close because the letters retain both endpoint indices.
Its group product has a power equal to the identity, so torsion-freeness forces that primitive product to be the identity.
A primitive class of length \(\ell\) contributes exactly \(\ell\) distinct rotations in each power, yielding the displayed negative-logarithm Euler product with the unnormalized matrix trace.
Only finitely many words contribute to each coefficient.
The coefficient ring is therefore \(\mathbb Z[c_e]\), and finite coefficientwise specialization is valid for arbitrary complex weights.
This formal conclusion supplies no analytic boundary-exponent theorem.

The expansion in (19) has coefficient \(-2C_{j-1}\) in degree \(j\), while the atom at four has mass one half.
It is a valid counterexample to the claimed generic implication from integer determinant coefficients and algebraicity to integer atomic mass.
It is explicitly not presented as a group-ring counterexample.
The further need to connect labelled cyclic structure and coefficient specialization to (17) remains unresolved.

The selected positive symmetric weights and real potentials satisfy the hypotheses of the graph input in (20).
The density of states is the average of the \(p\) vertex spectral measures, so the index theorem gives exactly the unnormalized quantity \(p\mu(\{\lambda\})\).
For a nonatom the Aomoto set is empty and the same formula has both sides zero.
The free deck action with \(p\) vertex representatives gives a matrix over the free group's group ring and the same normalized spectral law.
It does not give a law-preserving replacement of a general group by a universal tree.
The four-step return counts in (21) are \(16+12=28\) for the free group and \(6+6+24=36\) for \(\mathbb Z^2\).
Both second moments are four and all odd moments vanish; the difference of logarithmic determinant germs is consequently \(-8t^4/4+O(t^6)\), as stated.

## Accepted foundations and source completeness

The original analytic proofs behind the Bia97 density parameterization, the scalar entropy formula and the MSW17 conjugate-variable obstruction were not independently re-audited.
Their exact stated interfaces and hypotheses were checked against the retained source records identified in the bindings and accepted within those recorded limits.
The same boundary applies to the established affiliated-algebra and rational-closure inputs from MSY23.
The local adaptations, block calculations, spectral consequences and both directions of the resulting reformulations were checked in this review.

The reviewer directly inspected [BBL21 arXiv v2, Lemmas 2.1 and 2.3](https://arxiv.org/html/1903.09002v2), confirming the scaled-resolvent attribution and the positive invertible expected-kernel condition for the reciprocal statement.
The artifact's scalar angular proof is independently supplied by its own dominated-convergence calculation.
The source's stronger operator-valued analytic framework is not being certified in full.

The reviewer directly inspected [Kon11 arXiv v1, Section 1, Step 1](https://arxiv.org/html/1109.2469v1) and [KR14 arXiv v5, Definition 2.1, Proposition 2.2, Corollary 2.3 and Propositions 4.1--4.2](https://arxiv.org/html/1303.3481v5).
These passages support the torsion-free cyclic-root argument and the matrix-word construction, with KR14's zeta function reciprocal to the determinant convention used here.
The separate free-group algebraicity theorem is not accepted as an arbitrary-group input.

The reviewer directly inspected the graph conventions, density-of-states normalization, Aomoto set and [BGVM20 arXiv v2, Theorem 3.1](https://arxiv.org/html/2008.03318v2).
This is the accepted external general index theorem at the selected positive-weight specialization, including embedded eigenvalues; its complete proof was not re-audited.
The reviewer also checked [BBGSS23 arXiv v1, Sections 1--2 and Section 4](https://arxiv.org/html/2309.00437v1), confirming the finite vertex-edge product and its explicit restriction of the index-proof sketch to isolated eigenvalues.
Integer exponents of those factors alone do not justify dropping the source's Puiseux limitation.
The four corresponding entries in [the bibliography](../../literature/references.bib) were checked in their current form for author, title and fixed arXiv-version identity.
No unresolved source-identification or applicability defect was found within this scope.

## Whole-artifact finding

The complete fixed artifact's formulas (1)--(21), asserted equivalences, local derivations and stated source uses are mathematically supported within the accepted-foundation boundaries above.
No substantive mathematical correction is required by this inspection.
The supported result is a set of exact reformulations, checked strategy tests and a correctly delimited known geometric mechanism.
It does not prove a new Atiyah case, a relation-compatible heat or derivative estimate, a universal graph recursion, or integer boundary-exponent rigidity from the cyclic product.
In particular, the full A0001 contract remains unresolved, and this finding supplies no Task-completion evidence.
No numerical experiment or formal proof-assistant verification is claimed.
