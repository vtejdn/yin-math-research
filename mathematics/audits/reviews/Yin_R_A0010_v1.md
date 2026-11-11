---
author: Yin
---
# Independent review of degree-one reduction and extreme-coefficient rank certificates

Review performed at 2026-11-11T05:17 UTC for Yin.
The reviewer was outside substantive development of the inspected argument and received no inherited mathematical development dialogue, development draft, author explanation or previous conclusion about this artifact.
The inputs were the fixed argument, its exact necessary dependencies, the research question and the applicable rules.
The final corrected normalization uses \(tI_{dn}\), and the reviewed final section includes the distinction between an already affine border and a higher-degree numerator.
No earlier R finding about this artifact was supplied or consulted.
The substantive findings below were formed directly from the argument and its dependencies.

## Inputs and scope

The principal input is the complete 11 November 2026 revision of [Yin_L_A0008_v1](../../ledger/Yin_L_A0008_v1.md), from the single lowering step through the final known-coverage and induction discussion.
The exact [Task contract](../../tasks/Yin_T_A0001_v1.md#contract) is used to distinguish progress from completion, and its [coset argument](../../tasks/Yin_T_A0001_v1.md#reduction-to-finitely-generated-groups) supplies the supporting-subgroup interface.
The review is a whole-artifact mathematical review of L_A0008, not a completion review of that broader Task.

The direct analytic inputs are [L_A0006's affiliated rank argument](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement), [L_A0007's character-orbit certificate](../../ledger/Yin_L_A0007_v1.md#the-character-orbit-certificate) and [its affiliated companion reduction](../../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials).
Their consumed rank, domain and grading steps were rechecked against [MSY23-U004](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof) and the [bounded-row repair of Lemma 5.19](../literature/MSY23/Yin_U006.md#lemma-519-domain-repair).
The finite affiliated algebra, matrix amplification, polar decomposition, trace faithfulness and relative-inverse existence are accepted foundations at their existing recorded scopes.
The [JZ19 relative-inverse input](../literature/JZ19/Yin_U001.md#regular-closure-definitions) is used in the ambient affiliated algebra, without an assertion that singular relative inverses belong to the smaller rational closure.

The other precise comparisons are [L_A0004's all-size affine criterion](../../ledger/Yin_L_A0004_v1.md#setting-and-exact-criteria), [L_A0007's complete complex parameter identities](../../ledger/Yin_L_A0007_v1.md#the-full-complex-parameter-range-under-the-common-grading), [Coh06 Section 5.8](../literature/Coh06/Yin_U002.md#coh06-u002), [MSY23 Theorem 4.3 and polynomial consistency](../literature/MSY23/Yin_U003.md#theorem-43-constructive-existence-of-representations), and [JZLA20's natural extension](../literature/JZLA20/Yin_U001.md#natural-extensions) with [Proposition 3.11](../literature/JZLA20/Yin_U001.md#hughes-free).
The concluding torsion-free/nonindicable comparison was checked at the retained [Promislow calibration](../../ledger/Yin_L_A0003_v1.md#retained-candidate-beyond-the-ambient-cyclic-quotient-test), including the abelianization implication.
These are exact interface and applicability checks, not fresh whole-artifact reviews of the dependency materials or a recursive audit of their literature foundations.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Single lowering step](../../ledger/Yin_L_A0008_v1.md#a-single-exact-lowering-step) | Rectangular block identities, explicit units, affiliated ranks and bounded versus unbounded kernel interfaces. |
| [Whole-artifact finding](#whole-artifact-finding) | [Terminating induction](../../ledger/Yin_L_A0008_v1.md#terminating-induction-for-word-polynomials) | Written complexity, exact strict decrease, all matrix sizes, relation-respecting evaluation and source scope. |
| [Whole-artifact finding](#whole-artifact-finding) | [Ordered one-variable version](../../ledger/Yin_L_A0008_v1.md#an-efficient-ordered-one-variable-version) | Noncommutative multiplication order, nilpotent triangular inverse, stable equivalence and degree boundaries. |
| [Whole-artifact finding](#whole-artifact-finding) | [Endpoint hypotheses](../../ledger/Yin_L_A0008_v1.md#exactly-what-the-degree-one-endpoint-inherits) | Extreme coefficient ranks and units, dimensionally correct normalization, character applicability and coefficient-group boundary. |
| [Whole-artifact finding](#whole-artifact-finding) | [Anticommutator lowering](../../ledger/Yin_L_A0008_v1.md#the-concrete-anticommutator-after-lowering) | Exact numerator, rank shift and common-grading certificate. |
| [Whole-artifact finding](#whole-artifact-finding) | [Base-case obstructions](../../ledger/Yin_L_A0008_v1.md#why-a-scalar-or-fixed-size-base-case-does-not-follow) | Matrix versus scalar base case, determinant size bound and scalar Laurent-unit support width. |
| [Whole-artifact finding](#whole-artifact-finding) | [Unit-completion bound](../../ledger/Yin_L_A0008_v1.md#a-unit-completion-instead-of-assuming-an-invertible-extreme-coefficient) | Both inverse products, fixed supports, graded admissibility, exact defect estimate and top-degree normalization. |
| [Whole-artifact finding](#whole-artifact-finding) | [Fractional and singular examples](../../ledger/Yin_L_A0008_v1.md#degree-one-still-contains-fractional-coefficient-defects) | Projection examples, coefficient-rank insufficiency, common-kernel counterexample and coefficient-group obstruction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Indicable-support examples](../../ledger/Yin_L_A0008_v1.md#a-singleton-extreme-support-term-and-the-earlier-examples) | Singleton extremes, every complex q and eta case, support coincidences, ordered clearing and subgroup passage. |
| [Whole-artifact finding](#whole-artifact-finding) | [Coverage and remaining step](../../ledger/Yin_L_A0008_v1.md#known-coverage-and-the-remaining-induction-step) | Known source applicability, actual inverse domains, nonindicable boundary and absence of Task completion. |

## Whole-artifact finding

No substantive mathematical gap was found in the inspected L_A0008 revision under its stated hypotheses and accepted finite-affiliated foundations.
Its terminating stable linearization, two extreme-coefficient rank bounds, counterexamples to weaker endpoint tests and complete indicable-support parameter conclusions are supported by the displayed arguments.
The conclusions do not establish integer rank for arbitrary affine matrices or complete the general torsion-free Task.

### Lowering, termination and the endpoint

Direct multiplication of (H1) first eliminates the upper-right block and then the lower-left block, giving exactly \(\operatorname{diag}(A+BC,I_k)\).
The triangular factors are units for arbitrary compatible rectangular \(A,B,C\), independently of the target.
The rank shift by \(k\) and increase by \(k\) in the number of columns cancel in the kernel dimension.
The bounded map \(x\mapsto(x,Cx)\) is valid when the entries are bounded; the unbounded case is correctly proved by affiliated rank invariance rather than by that unrestricted Hilbert-space map.

For each chosen word of length \(\ell\ge2\), the new prefix has length \(\ell-1\), and the new final letter and identity have complexity zero.
The written sum of \(\max(\ell-1,0)\) therefore decreases by exactly one without requiring any relation reduction.
The new row and column sizes and the accumulated rank shift are both counted by the actual number of steps.
At zero complexity the representative is affine, including the initially constant or already affine cases.
The stated algorithm uses no optional simplification, so its step count is exactly the initial written complexity.

For (H4), the lower block has \(d-1\) block rows, hence its strictly lower triangular part satisfies \(N^{d-1}=0\).
The stated finite inverse and the entries \(-T,-T^2,\ldots,-T^{d-1}\) of \(D^{-1}C\) give precisely the ordered sum \(A_jTT^{j-1}\).
No coefficient is commuted through \(T\).
The case \(d=2\) has lower block \(I_n\), the case \(d=1\) is defined directly, and a constant polynomial requires no lowering.
The skew relation is compatible with these identities; a central formal variable cannot be evaluated without the stated commutation premise.

The constant coefficient has the claimed diagonal form.
The last-column permutation of the leading coefficient leaves an invertible triangular complement with diagonal blocks \(-I_n\), giving (H8) and the stated equivalence of unit hypotheses.
The normalized term \(H_0^{-1}H_1(tI_{dn})\) is homogeneous of degree one under precisely the stated fixed-coefficient action.
The character-orbit input applies to that actual affiliated matrix, so the full-rank conclusion requires no inverse of the target.
The anticommutator example has \(BC=gh+hg\), and its constant normalization uses the independently invertible diagonal \((2,1,1)\).
It therefore supplies the asserted direct degree-one endpoint when the actual common grading exists.

The scalar-entry counterexample has rank one by its explicit rank-one factorization and its unit upper-left entry.
The determinant obstruction has degree \(nd\) preserved by polynomial-unimodular factors, while an affine \(N\)-square determinant has degree at most \(N\).
The Laurent-unit argument uses additivity of both extreme exponents in a scalar Laurent domain and correctly rules out reducing width three to width at most two by the specified units.
These are restrictions on the stated mechanisms, not exclusions of every possible rational realization.

### Singular coefficients and the exact rank bound

The support identities for the relative inverse make every off-diagonal block in both \(C_0D_0\) and \(D_0C_0\) vanish, while their diagonal blocks are identities.
The action fixes the relative inverse and its support projections by uniqueness.
Thus the graded companion certificate applies to \(C(P)\) with its independently verified constant unit, including singular and zero \(A_0\).
When there are no positive-degree terms, this reduces to the already verified unit \(C_0\).

The off-diagonal support matrix has rank \(2(n-r)\), and the diagonal summand has rank \(\operatorname{rk}_M P+r\).
Rank subadditivity gives \(2n\leq\operatorname{rk}_M P+2n-r\), which is exactly (R1).
Faithful finite trace converts the full-rank square cases into actual affiliated units.
For (R2), multiplying on the right by the given degree-one unit to the power \(-d\) makes the former top coefficient the constant term after reversing the grading.
The argument consequently includes the needed unit and retains the noncommutative order.

The projection pencil \(p(1+t)\) has the exact stated fractional rank because \(1+t\) vanishes only on a null subset of the circle.
The complementary pencil has the displayed inverse, so equal pairs of coefficient ranks indeed permit different pencil ranks.
The order-two group example has the same half-trace projection but falls outside torsion-freeness.
For the three-by-three pencil, the constant coefficient kills only the second coordinate and the linear coefficient kills only the first; their adjoints have respective kernels in the third and second coordinates.
Both common-kernel intersections are therefore zero, while the displayed polynomial kernel vector and two independent columns give rank exactly two.
Finally, \(A(1+t)\) preserves every coefficient-matrix rank because the scalar cyclic factor is an independently known affiliated unit.
This proves the asserted obstruction to treating cyclic degree one as an automatic all-group integer-rank base case.

### Parameters and supporting subgroups

A unique minimum support term becomes a nonzero scalar constant after left multiplication by its group inverse, and all other degrees are positive.
The same argument with the reversed character treats a unique maximum.
The subgroup's character suffices, since the bounded group-ring numerator and its kernel dimension pass to the ambient group through the coset decomposition.

For distinct nonidentity \(g,h\), the degrees \(0,m,n\) always have a singleton extreme unless \(m=n=0\).
The exceptional coefficients at \(q=0,1,-1\) are correctly separated: they yield \(1-h\), \(g-h\), or the remaining three-term numerator with nonzero extreme scalar coefficient.
Torsion-freeness independently certifies the binomial units.
When \(g=h\), the linked exact identities give the only zero cases \(t_q=0\) at \(q=-1\) and \(r_q=0\) at \(q=\pm1\).
The ordered identities and all multiplier placements were checked without commuting \(a\) and \(b\).

For \(p_\eta\) with \(\eta\ne1\), same-sign degrees make the identity an extreme singleton, opposite signs make the individual \(g\) and \(h\) terms extreme, and a zero degree gives the stated cyclic unit as the entire extreme coefficient.
The inequalities in the opposite-sign case keep both product terms strictly between those extremes, including \(m+n=0\).
Coincident products or inverse labels therefore do not cancel the certified extreme terms.
Equal labels reduce to \((1-\eta)(1-g)^2\), consistently with the conclusion.
At \(\eta=1\), the commutator factorization gives zero exactly when the labels commute and a cyclic unit otherwise.
The denominator clearing \((ba)r_\eta(ab)=p_\eta\) is correct for every complex \(\eta\), including zero, and uses only the independently certified \(a,b\).

### Source completeness and retained limits

The exact cited Coh06 passage supplies the elementary enlargement and finite repetition; the artifact supplies its own explicit complexity and analytic rank consequences.
No free-algebra highest-term theorem is applied to a relations quotient.
The cited MSY23 construction is compatible with the polynomial arithmetic, while the inverse domain for a rational representation remains a separate premise.
The JZLA20 natural-extension lower coefficient estimate and Proposition 3.11 match the claimed known cyclic-extension coverage, including merely indicable supporting subgroups rather than locally indicable ambient groups.
The rank inequalities and unit completion do not assume an already existing coefficient division ring.

This review checked the source identification, retained exact passage statements and their applicability at those local source units.
It did not repeat their original whole-source audits, re-run the reported bounded literature search, inspect the original Higman paper, establish historical priority or perform formal verification.
Those unperformed tasks are not needed for the artifact's claimed mathematical scope or its expressly limited attribution.
The remaining all-size affine rank problem, uncontrolled coefficient ranks and nonindicable-support cases are correctly left unresolved.
An already affine bordered pencil obtains no additional rank constraint merely by invoking this lowering construction.
