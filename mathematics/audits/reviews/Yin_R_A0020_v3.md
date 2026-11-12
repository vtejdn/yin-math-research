---
author: Yin
---
# Independent review of polynomial normalization and finite Laurent boundary certificates

Review time: 2026-11-11T17:33 UTC.
The human record author is Yin.
The reviewing agent was assigned the complete fixed [C_A0007_v3](../../claims/Yin_C_A0007_v3.md), dated 2026-11-12 in Asia/Hong_Kong, and its directly needed source interfaces.
This is an independent initial whole-candidate inspection by an agent outside substantive proof development.
No development drafts, proposing-agent explanations, proof-generation dialogue or previous review verdicts were supplied or consulted.
Only the header and title of the preceding R_A0020 version were read to confirm the existing review family.
Obligations were enumerated from the fixed statement before checking the argument and sources.
No prior project-review finding is relied upon here.

## Inputs

- [C_A0007_v3 statement](../../claims/Yin_C_A0007_v3.md#statement) and [complete argument](../../claims/Yin_C_A0007_v3.md#argument), including its examples, normalization branches, source comparison and continuation limits.
- [BBL21 source interface](../literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface), checked against [arXiv:1903.09002v2](https://arxiv.org/html/1903.09002v2), Theorems 3.1, 3.2 and 3.5, with the bounded-inverse convention in Section 2.
- [Coh06 original](../../literature/pdf/Coh06.pdf), Theorem 1.3.2 on printed p. 74, Propositions 1.4.1 and 1.4.5 on pp. 78--79, Theorem 1.4.7 and its proof on pp. 80--81, and the opening of Section 1.5 on p. 86.
- [MSY23 original](../../literature/pdf/MSY23.pdf), Lemma 5.9 on p. 31 and Theorem 5.25 on pp. 43--45, together with the [Lin93 subgroup and rank account](../literature/Lin93/Yin_U001.md#affiliated-closure-and-rank-conventions).
- [Cyclic rational functions and finite-support obstruction](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), [the degenerate expected-kernel example](../../ledger/Yin_L_A0013_v1.md#full-support-does-not-supply-a-bounded-inverse-even-for-a-group-ring-matrix), [L_A0014](../../ledger/Yin_L_A0014_v1.md), and [C_F0181's graded subordination argument](../../claims/Yin_C_F0181_v1.md#graded-subordination-proof), at the specific source-comparison and interface scopes used by the candidate.
- [The retained tree-transport argument](../../claims/Yin_C_A0003_v1.md#tree-transport-and-actual-loop-operators) and [BGVM20 arXiv v2](https://arxiv.org/html/2008.03318v2), Section 2.2 and Lemma 2.1, for the candidate's limited gauge comparison.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | [Statement](../../claims/Yin_C_A0007_v3.md#statement) | Exact hypotheses and all conclusions, including finite Laurent boundary recovery, integer-nullity conditions, example and asserted limitations. |
| [Whole-candidate finding](#whole-candidate-finding) | [Argument](../../claims/Yin_C_A0007_v3.md#argument) | Complete proof, actual affiliated domains, conditional expectations, source interfaces, example and both normalization boundaries. |
| [Whole-candidate finding](#whole-candidate-finding) | [Source comparison and continuation limit](../../claims/Yin_C_A0007_v3.md#source-comparison-and-continuation-limit) | Limited local comparison, checked algebraic source locators and the distinction between a sufficient witness certificate and an arbitrary-kernel existence theorem. |

## Whole-candidate finding

The complete fixed candidate is mathematically supported under its stated hypotheses.
No gap requiring correction was found.
The additional finite Laurent conclusion is an identity for the actual analytic boundary values, with the analytic existence premise established before its use.
The review establishes neither the existence of suitable polynomial witnesses for arbitrary group-ring matrices nor the Atiyah property of an unrestricted amalgam.

### Obligations obtained from the statement

The statement requires six logically separate checks: the general-base analytic interface and trace convention; the indefinite four-path example; rational boundary recovery from polynomial kernel columns; full-support cyclic normalization and actual congruence invariance; the identity-expectation construction and finite Laurent conclusion; and the exact limits of the rank-deficient and two-variable branches.
The integer-nullity reduction must additionally use ranks in the actual vertex representations, without assuming the desired property for the amalgam.
These obligations were checked individually and then in their complete order of dependence.

### Analytic interface and actual representations

For an actual amalgam, alternating centered finite vertex group-ring products have no coefficient in the edge subgroup by reduced-word normal form.
Entrywise multiplication gives the same statement for matrix entries, and normal closure supplies the matrix-amplified freeness needed here.
The canonical expectation is trace preserving, faithful and bimodular, with base the full matrix algebra over the edge von Neumann algebra.

BBL21 v2 Theorem 3.5 has a general von Neumann base and requires the expected kernel to be positive with a bounded inverse.
Its part (vii) supplies the kernel meet and trace identity; Theorem 3.2's construction identifies the selfadjoint norm limits.
Using the normalized matrix tracial state and multiplying the source identity by the matrix size gives exactly candidate equation (1), with the term \(n\) rather than \(1\).
No finite-dimensional support argument is imported into the diffuse base.
The original analytic foundations are accepted external inputs, not independently re-proved in this review.

The right-coset decomposition of a subgroup's left regular representation identifies the same cyclic denominators and their affiliated inverses inside each larger group algebra.
It also preserves the trace of subgroup projections.
A nonzero Laurent determinant is therefore an actual affiliated-unit certificate, independently of any unknown matrix ranks for the amalgam.
For two bounded matrices related by multiplication by affiliated units, the rank invariance in MSY23 Lemma 5.9 applies in the affiliated algebra.
It makes no claim that an unbounded inverse acts on every Hilbert vector.

### Four-path example and polynomial recovery

The three products of the displayed diagonal gauge entries are \(a,b,a\) in their prescribed order.
The constant path matrix has characteristic polynomial \(x^4-3x^2+1\), and its displayed eigenvector has eigenvalue \(\lambda\).
Thus the asserted simple zero eigenvalue, negative and positive spectrum, projection \(WW^*/c\), and total nullity one follow without a group Atiyah premise.
Distinct free-group words eliminate precisely the off-diagonal expected-projection entries, giving the stated strict lower bound.
Direct multiplication gives \(Y_1W=B_0W\) and \(Y_2W=-B_0W\).
The source kernel inclusion and invertibility of the expected projection then determine the actual limits as \(B_0\) and \(-B_0\).
The two constant two-square rank-one blocks and the remaining zero coordinates give nullities two and three, consistent with the unnormalized trace formula.
The example remains a finite-tree reduction inside a known group class.

For the general witness, finite coefficient extraction puts \(C\) and \(N_j\) in the cyclic group ring.
The equality \(pW=W\) and the analytic kernel inclusion give \(Y_jW=b_jW\), hence \(N_j=b_jC\) in that order.
Full support of positive \(C\) makes its Laurent determinant nonzero: a zero determinant would yield a nonzero rational kernel column, and clearing cyclic denominators would contradict analytic injectivity.
The adjugate formula thus gives its actual rational inverse and proves the asserted recovery formula.
The estimate \(WW^*\le\|W\|^2p\) proves the stronger lower-bound branch.
When \(WW^*\) has support \(p\), faithfulness applied to a kernel projection \(q\) of \(C\) gives \(pq=0\) and hence \(qE(p)q=0\), proving the supplementary full-support observation without a bounded inverse.
The cited two-coordinate example confirms that the two support properties do not provide a uniform lower bound.

### Cyclic normalization and finite Laurent boundary values

The decomposition over distinct cosets \(Hu_\alpha\) is correctly ordered with Laurent coefficients on the left.
It gives \(C=FF^*\) without a normality assumption on \(H\).
Full support forces field row rank \(n\).
The column module of \(F\) is a free submodule of rank \(n\) over the Laurent principal ideal domain; the given coordinate-induction proof does not assume that it is a direct summand.
Expressing a module basis in the original generating columns gives \(D=FS\) and \(F=DF_0\), so cancellation over the cyclic field gives the polynomial right inverse \(F_0S=I_n\).
This yields both the bounded lower estimate for \(F_0F_0^*\) and an actual affiliated inverse for \(D\).
Consequently the finite selfadjoint congruence \(Y'_j=D^*Y_jD\) stays in its correct vertex group ring, annihilates \(W_0\), meets the analytic premise, and preserves the original nullity.

The crucial new construction uses \(Z_0=\sum_\alpha u_\alpha^{-1}S_\alpha\) with the Laurent block to the right of the group unitary.
Expanding \(W_0Z_0\) and applying bimodularity kills all distinct-coset terms and leaves \(F_0S=I_n\).
Thus \(X_0\) is finite, is annihilated by \(Y'\), and has identity expectation.
Positivity of the expectation of \((X_0-I_n)(X_0-I_n)^*\) gives \(E(X_0X_0^*)\ge I_n\), while its kernel range gives \(X_0X_0^*\le\|X_0\|^2p'\).
This independently verifies the strict expected-kernel lower bound.
Only after that verification, the actual analytic boundary inclusion gives \(Y'_jX_0=b'_jX_0\).
Taking expectation yields \(b'_j=E(Y'_jX_0)\), which is a finite Laurent matrix.
Selfadjointness of this possibly nonmanifestly selfadjoint polynomial expression follows from equality with the actual selfadjoint limit.
The resulting \(Q_j\) are therefore finite selfadjoint vertex matrices, and (N14) follows from the source trace identity and congruence invariance.
The same reasoning from a given identity-expectation witness uses no commutativity or principal ideal domain property of the base.

### Integer ranks and boundary cases

For the rational-recovery branch, the known vertex Atiyah hypotheses supply actual division rings, in accordance with MSY23 Theorem 5.25 and the subgroup representation.
The finite-tuple source formulation applies to each finite rational expression; its use does not require the groups to be finitely generated.
Gaussian elimination uses units in these actual affiliated embeddings, so its algebraic rank is the analytic rank and is integral.
The normalized finite-Laurent branch needs only the integer nullities of its two explicit \(Q_j\) matrices.
Neither route assumes the amalgam's desired rank property.

In the deficient-rank branch, Smith reduction gives \(F_0=JV^{-1}\) and hence a lower bound only on \(q=\operatorname{diag}(I_r,0)\).
The bound \(\|V\|^{-2}q\) follows from invertibility of \(V\), and the support is exactly \(q\).
Affiliated invertible factors cannot change this deficient rank.
The warning that compression changes the kernel problem and requires trace corrections is therefore necessary and correct.
For rank zero the witness vanishes.

For the two-variable example, the expected Gram vanishes only at one torus point but approaches zero in positive-measure neighborhoods.
Any nonzero scalar Laurent factor of the specified witness must divide both \(x-1\) and \(y-1\).
Primality of \(x-1\) and evaluation at \(x=1\) force that common divisor to be a Laurent unit.
Such a unit has constant modulus on the torus, so it cannot create a uniform positive lower bound.
This excludes precisely the stated same-size factorization, while leaving alternative witnesses and stabilization open.
The free-tree boundary operator in L_A0002 has a positive-dimensional analytic kernel and no nonzero finitely supported kernel by leaf removal, supporting the candidate's remaining witness-existence limitation.

### Source completeness and limits

The Coh06 printed/PDF page correspondence and the cited principal-ideal, free-submodule and Smith statements match the original text.
The candidate supplies its needed Laurent localization argument and coefficient/order calculations explicitly.
The selected local C_F0181, BBL21 source account and L_A0014 passages support the stated interfaces and comparisons; they do not already state the general polynomial recovery formula in the candidate's form.
The tree-transport antecedent and BGVM20 scalar phase gauge are appropriately limited comparisons, not sources of an unproved arbitrary unitary-weighted index equality.
No unresolved source identification affecting the adopted proof was found.
No historical priority, whole-book review or full analytic-source audit is asserted.

This is an informal mathematical proof review with exact fixed input bindings.
It is not formal verification, an algorithm for an arbitrary word problem, a witness-existence theorem, a proof for rank-deficient witnesses, or a completion review of the overarching Task.
