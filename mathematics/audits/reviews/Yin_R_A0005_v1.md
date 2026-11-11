---
author: Yin
---
# Independent review of the index-two crossed product and rational norm descent

Review act: 2026-11-10T18:15 UTC, recorded for Yin.
This is an initial independent whole-argument inspection of the 2026-11-11 (Asia/Hong_Kong) revision of [Yin_L_A0003_v1](../../ledger/Yin_L_A0003_v1.md#results-and-source-scope), including its final Promislow candidate section.
The reviewer did not participate in substantive proof development and received the fixed argument, necessary source inputs, assignment and applicable rules without inherited development discussion.
No working draft, proof-generation dialogue, development-helper explanation or unrelated project R conclusion was consulted.
This finding does not select a Claim assessment or complete [Yin_T_A0001](../../tasks/Yin_T_A0001_v1.md#contract).

## Inputs and accepted boundaries

The artifact is the complete dated L revision, with exact section bindings below.
The Task contract was read only to compare this scope with the original all-groups integrality question.

[Lin93-U001](../literature/Lin93/Yin_U001.md#routine-lemmas-and-induction) was read for the subgroup/crossed-product and Artinian-closure interfaces, together with its [affiliated conventions](../literature/Lin93/Yin_U001.md#affiliated-closure-and-rank-conventions), [theorem statements](../literature/Lin93/Yin_U001.md#group-class-and-exact-theorems) and [free-group input](../literature/Lin93/Yin_U001.md#free-group-proof).
The finite affiliated-ring foundations, bounded regular denominators, polar decomposition and affiliated-rank invariance are accepted at that unit's recorded scope.
Lin93's free-group division theorem and Theorem 1.3 are accepted established inputs after checking the actual kernels and quotients.
Their original proofs and external foundations were not re-audited.

[Lin06-U001](../literature/Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures) was checked for the matrix-inverse description of rational closure and its inclusion of division closure.
[MSY23-U005](../literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence) was checked for the division/integral-rank equivalence in one fixed affiliated ambient algebra.
Finite supports reduce group-ring matrices to finite tuples, and zero padding handles rectangular matrices.
The relevant Atiyah conclusion is the integral-kernel assertion of the torsion-free Task.

[LL18, arXiv v3, Theorem 2.3(3)--(4), p. 10](https://arxiv.org/pdf/1602.06906v3#page=10) was checked directly at statement depth for the comparison citation.
[Gar21, arXiv v4, Section 3.1, pp. 4--5](../../literature/pdf/Gar21--arxiv-v4.pdf#page=4) was read directly in text and rendered pages for the candidate's group structure and conjugation data.
The unit construction elsewhere in Gar21 was not reviewed.
Standard division-ring linear algebra, the subgroup theorem for free groups and the ordinary skew-polynomial fraction construction are accepted at their explicit uses.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../ledger/Yin_L_A0003_v1.md#results-and-source-scope) | Exact general hypotheses, conclusions, calibration and source limits. |
| [Whole-argument finding](#whole-argument-finding) | [Actual embedding](../../ledger/Yin_L_A0003_v1.md#actual-affiliated-embedding) | Subgroup extension, coset faithfulness, matrix model and trace normalization. |
| [Whole-argument finding](#whole-argument-finding) | [Closures](../../ledger/Yin_L_A0003_v1.md#division-and-rational-closure-comparison) | Both inclusions and ambient matrix inverse closure without prior division of the crossed product. |
| [Whole-argument finding](#whole-argument-finding) | [Norm and half rank](../../ledger/Yin_L_A0003_v1.md#complete-norm-criterion-and-the-half-rank-witness) | Full norm equivalence, inverse formulas, zero-divisor alternative, half rank and finite group-ring extraction. |
| [Whole-argument finding](#whole-argument-finding) | [Concrete group](../../ledger/Yin_L_A0003_v1.md#concrete-group-and-existing-coverage) | Presentation isomorphism, free kernels, torsion-freeness, subgroup splitting and source applicability. |
| [Whole-argument finding](#whole-argument-finding) | [Parity obstruction](../../ledger/Yin_L_A0003_v1.md#why-an-invariant-parity-valuation-cannot-settle-this-example) | No integer lift and all invariant integer-valued multiplicative homomorphisms. |
| [Whole-argument finding](#whole-argument-finding) | [Rational descent](../../ledger/Yin_L_A0003_v1.md#a-leading-coefficient-constraint-on-every-rational-solution) | Actual skew fractions, formal series automorphism, residue equation and noncircular free-group contradiction. |
| [Whole-argument finding](#whole-argument-finding) | [Research boundary](../../ledger/Yin_L_A0003_v1.md#consequences-and-remaining-research-boundary) | Calibration conclusion, existing coverage and requirements of the residue mechanism. |
| [Whole-argument finding](#whole-argument-finding) | [Retained candidate](../../ledger/Yin_L_A0003_v1.md#retained-candidate-beyond-the-ambient-cyclic-quotient-test) | Promislow source match, subgroup, twisting, abelianization and screening limits. |

## Decisive verification

### Actual embeddings and closures

The common bounded regular left denominator reduces affiliated coset dependence to orthogonal bounded coset components.
The separating-vector argument annihilates each coefficient and proves faithfulness in the actual ambient algebra.
It also justifies the later finite Laurent sums.
The matrix model has the correct \(\alpha^{-1}\) entries, and its two diagonal compressions give the stated factor of two in the unnormalized trace.
Extending the representation to support projections justifies the affiliated-rank comparison without arbitrary unbounded-domain manipulations.

Subgroup invertibility and its inverse are preserved, giving the inclusion of \(A\) in \(D_G\).
For the opposite inclusion, left multiplication by an ambient-invertible matrix is injective and right \(D(H)\)-linear on finite-dimensional \(M_n(A)\).
Its surjectivity supplies the inverse in that same matrix ring.
Thus both closure equalities hold even before division of \(A\) is established.

### Norm criterion and finite matrix extraction

Both noncommutative factorizations and coefficient orders are correct.
The two defects are related by \(\alpha\), so they vanish together or are simultaneously units.
The left and right inverse formulas agree in the unit case; coset independence makes the annihilating factors nonzero in the other case.
The separate constant case and the normalization by the nonzero \(t\)-coefficient cover every nonzero element, establishing necessity and sufficiency.

Under a norm solution, the matrix factorization and its identity entry give rank exactly one over the coefficient division ring.
Reduction by invertible elementary matrices and the trace comparison then give scalar \(G\)-rank and kernel dimension \(1/2\).
Lin06's actual inverse-entry representation supplies the required \(Q\), and subgroup amplification preserves its ambient inverse.
The signs in the group-ring block matrix give Schur complement \(t+b\), so block elimination gives the asserted finite-matrix rank and kernel dimension.
This is conditional extraction, not an exhibited counterexample.

### Group structure and parity

The substitution \(a=xy\) gives exactly the displayed transformed relator.
The proposed \(\beta,\gamma\) are mutual inverses on every free generator, and eliminating the shifted \(z_i\) in the semidirect presentation recovers precisely that relator.
Thus \(K=\ker\psi\) is the actual indicated free group; the quotient by \(K\) also proves torsion-freeness.

The restriction of \(w\) to \(K\) is onto because of \(z\), while \(s=xz\) belongs to \(H\) and maps to \(1\) under \(\psi\).
These facts justify both the index of \(L\) and the splitting of \(H\), and hence Lin93's hypotheses for all four groups.
Their existing \(\mathcal C\) coverage and the finite-extension limitation are correctly stated.

The abelianized relator excludes an integer lift of \(w\).
For an invariant multiplicative homomorphism, the proposed values on \(H\) and \(z\) respect conjugation and \(z^2=h\).
An odd value on \(h\) would therefore create that forbidden lift.
The conclusion has exactly the stated invariant integer-valued scope.

### Actual rational localization and formal residue

Coset independence identifies the Laurent ring faithfully, and the already known division of \(D(H)\) extends that actual embedding to its skew fraction ring.
The reverse containment follows because this embedded fraction ring is a division subring containing \(\mathbb CH\).
This establishes the actual rational identification rather than substituting an unrelated abstract skew field.

Formal convolution and geometric inversion are well defined coefficient by coefficient.
The substitution determined by \(\theta\) and \(s\mapsto us\) preserves each exponent, with invertible coefficient changes also for negative powers.
Actual conjugation supplies covariance, and the inverse substitution gives bijectivity.
The extended automorphism consequently agrees with \(\alpha\) on the rational subring and induces exactly \(\theta\) on residue.

The norm equation forces value zero because \(z^2\in L\), and its constant term gives the displayed residue equation.
Actual subgroup compatibility places its two nonzero zero-divisor factors inside \(D(K)\), contradicting that free group's division input.
The positive inputs are only \(D(H),D(K),D(L)\); division of \(D(G)\) is not used in this descent.

### Appended candidate

Gardam's structural passage supplies the stated normal subgroup, quotient, torsion-freeness and action.
Its normal forms leave exactly \(N\) and \(Nb\) in \(H_P\).
Eliminating \(Y=b^2\), using independence of \(X,Y,Z\), and checking inversion of \(X,Z\) by \(b\) verifies the claimed semidirect product.
The identity \(ab a^{-1}=Zb^{-1}X^{-1}=XZb^{-1}\) checks the less immediate twisting entry.

The relators abelianize to exactly the two stated order-four relations, excluding a nonzero integer character.
The twisting reverses the Laurent exponent of \(b\).
Virtual abelianness gives existing \(\mathcal C\) coverage.
The appendix correctly leaves its rational norm analysis unperformed.

## Whole-argument finding

The complete fixed L argument is mathematically valid under its explicitly accepted standard and published inputs.
No unresolved mathematical gap or source-applicability defect was found in this scope.
The actual-ambient closure theorem, complete norm criterion, conditional half-rank matrix extraction, concrete residue exclusion and appended screening calculations are all covered by this independent finding.
The cited source roles and existing positive coverage are correctly distinguished from the direct specializations.
This is not a priority assessment, recursive foundational audit or proof-assistant verification.
The ledger supplies a complete worked calibration, leaves the second norm analysis open, and does not resolve the Task for arbitrary torsion-free groups.
