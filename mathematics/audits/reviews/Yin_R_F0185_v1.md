---
author: Yin
---
# Atiyah property through graded subordination: independent correction review

## Review act and inputs

Review act: 2026-11-02T04:39 UTC.
Human record author: Yin.
A separately organized agent outside the substantive development of this proof performed the independent mathematical correction review.
The reviewer received the fixed candidate, required scope, applicable rules and original source-interface objection, without proof-development dialogue, author explanations or an earlier verdict on the candidate.
The reviewer read the whole candidate and reconstructed its obligations before comparing the source records' historical and access limits.
The reviewer supplied no repair and changed neither the candidate nor its U inputs.
This is mathematical correction review, not conformity-maintenance acceptance.

The inspected mathematical input is the 2026-11-02 working-tree [C_F0181 v1](../../claims/Yin_C_F0181_v1.md), whose candidate decision is dated 2026-11-02T04:28.
Coverage comprises its complete statement, trace/kernel definitions and full graded-subordination proof, including equations (1)-(7) and the polynomial-matrix linearization.
The binding concerns that actual mathematical content, not a later proof with changed hypotheses or steps.
A later change only to candidate/adoption prose does not itself change the inspected mathematics.

Primary-source reading covered BBL21 arXiv:1903.09002v2, dated 15 May 2020: pp.1-2 for edition, invertibility and operator-valued conventions; pp.6-10 for Theorems 3.2 and 3.5, equation (3.7), Proposition 4.1, Lemma 4.2 and Corollary 4.3; pp.12-13 for Lemma 4.7 and Proposition 4.8.
The reviewer directly read ACSY24's retained 73-page published edition at pp.19-21 for Definition 2.16 and Lemma 2.20, and pp.43-44 for Definition 4.5 and Theorem 4.7 with its proof.
BBL21 p.8 and ACSY24 p.44 were additionally rendered and visually inspected.
The analytic foundations of BBL21's subordination theorems are accepted external inputs at their stated hypotheses, not independently re-proved here.
No previous project proof review supplies a premise for the conclusion below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole candidate finding](#whole-candidate-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole candidate finding](#whole-candidate-finding) | [C_F0181 statement](../../claims/Yin_C_F0181_v1.md#statement) | Every matrix size, arbitrary polynomial matrices, bounded free selfadjoint inputs and arbitrary additive subgroup containing the integers and all marginal atomic weights. |
| [Whole candidate finding](#whole-candidate-finding) | [C_F0181 complete proof](../../claims/Yin_C_F0181_v1.md#graded-subordination-proof) | Entire argument and definitions: both full-square support cuts, trace normalizations, invertible expected kernels, exact subordination boundary values, off-diagonal symmetry, structural parity cancellation, spectral-minor formula and matrix linearization. |
| [Whole candidate finding](#whole-candidate-finding) | [BBL21-U001](../literature/BBL21/Yin_U001.md#bbl21-u001) | Exact v2 analytic statements and their applicability here; comparison with Corollary 4.3, Lemma 4.7 and Proposition 4.8, without identification of unavailable final journal Corollary 3.3. |
| [Whole candidate finding](#whole-candidate-finding) | [ACSY24-U002 linearization](../literature/ACSY24/Yin_U002.md#1-rank-conventions-and-linearization) | Definition 2.16 and Lemma 2.20 as applied to a matrix polynomial via additional scalar matrix inputs, with actual auxiliary inverse and integer size offset. |
| [Whole candidate finding](#whole-candidate-finding) | [ACSY24-U003 Atiyah interface](../literature/ACSY24/Yin_U003.md#atiyah-property-convention) | Theorem 4.7's full hypothesis/conclusion match and the mathematical effect of the local reconstruction, distinguished from the final-edition source-attribution limit. |

## Whole candidate finding

No mathematical gap was found in the complete inspected local proof.
It establishes the full stated Atiyah property for two bounded free selfadjoint variables and an arbitrary additive subgroup of the reals containing the integers and every marginal atomic weight.
It uses neither division closure nor topological closure of that subgroup.

### Square cuts and trace conventions

For a square operator in a finite tracial von Neumann algebra, polar decomposition equates the traces of its right and left kernel projections.
The candidate consistently uses unnormalized matrix trace for nullity and rank, while BBL21's tracial-state identity is multiplied by the full matrix size.

If q supports the scalar matrix E_n(p_T), faithfulness gives p_T at most q.
The kernel of Tq is the orthogonal direct sum of p_T and 1-q.
Its expected kernel is therefore E_n(p_T)+(1-q), which is invertible in the full scalar matrix algebra.
This also covers q=0 and q=I without a nonzero-kernel premise.

Applying the same argument to U* for U=Tq yields the scalar support r and S=rTq.
The left-kernel expectation of S is invertible by that second cut.
Its right-kernel expectation dominates the already invertible expectation for U.
Polar decomposition then gives exactly the integer nullity shift in (2).
Both matrices remain n by n; neither equal support ranks nor a rectangular-corner trace convention is used.

### Subordination hypotheses and grading

The doubled coefficients and constant b are selfadjoint, and Proposition 4.1 applies because the original two variables are scalar-free and selfadjoint.
They are free over B=M_2n(C) for E_2n.
The doubled kernel is \(p_{S^*}\oplus p_S\), so its expected kernel is invertible by the two cuts.
The ambient probability trace is tr_2n tensor tau.
Thus every hypothesis of the accepted v2 Theorem 3.5 is available.

Theorem 3.2's proof constructs the actual selfadjoint norm limits of the same subordination functions appearing in (3.7).
The proof does not merely choose arbitrary selfadjoint decompositions of b.
For z=b+iyI, the grading J satisfies JzJ=-z* and JHJ=-H.
The trace-preserving expectation onto W*(B,H_j) is J-bimodular and adjoint preserving because J belongs to B.
Applying it to the full resolvent symmetry and using (3.7) gives the resolvent symmetry for the individual subordinate resolvent.
Inversion is valid for y>0 and yields J omega_j(z) J=-omega_j(z)*.
The selfadjoint norm limits therefore anticommute with J and have zero diagonal blocks.

Consequently every b_j-H_j has square off-diagonal blocks D_j and D_j*.
Polar decomposition in the finite n by n algebra makes its unnormalized nullity exactly twice the nullity of D_j.
The same identity holds for H-b and S.
Multiplication of Theorem 3.5(vii) by 2n followed by substitution cancels a common factor of two in a real equality.
Equation (6) follows before any subgroup membership is inferred.
This is the required strengthening over using only the source's displayed doubling conclusion.

### One-variable reduction and all polynomial matrices

A scalar square pencil with complex coefficients has its maximal rank outside a finite real set: a nonzero minor of maximum attained size has only finitely many real zeros.
The zero-rank case is constant.
Spectral functional calculus realizes D_j in M_n(W*(X_j)) as that matrix-valued function of the real spectral parameter.
Its right-kernel dimension is the integrand in (7), including for nonselfadjoint coefficients.
The exceptional corrections and the minimum nullity are integers.
Only finitely many marginal atomic masses enter, so their integer combination belongs to Gamma without a limit argument.

Equation (6), the integer cut correction and rank equal to n minus nullity establish the linear-pencil result.
A given m by m polynomial matrix can be expressed as a scalar polynomial expression evaluated on I_m tensor X_1, I_m tensor X_2 and finitely many constant matrix units.
After evaluating those constants, a formal linear representation's display is a square scalar-coefficient pencil in X_1,X_2.
Definition 2.16 supplies an actual inverse for its auxiliary block because the polynomial expression is defined at the given tuple.
Lemma 2.20's block elimination therefore applies with integer offset mk for representation size k.
The display size is \(m(k+1)\); its auxiliary identity block has size \(mk\).
This verifies the formula used by the candidate without relying on the apparent display-size typo in the published Theorem 4.7 proof.
The resulting rank belongs to Gamma for every original matrix size m.

### Source comparison and remaining limits

The exact local statement preserves ACSY24 Theorem 4.7's boundedness, freeness, selfadjointness, arbitrary matrix quantifiers and arbitrary subgroup Gamma.
BBL21 v2 Corollary 4.3 alone has the invertible expected-kernel and selfadjoint-pencil requirements.
Its Proposition 4.8 states a weaker output-atom conclusion and does not itself permit division by two in arbitrary Gamma.
Those observations remain correct about the inspected edition.
The local proof supplies the missing cuts and grading argument rather than attributing an unstated theorem to either item.

The remaining identification of the final journal Corollary 3.3 is unverified.
The inspected preprint has Remark 3.3, which by itself establishes no error in final journal numbering.
The U record reports unsuccessful final-text retrieval and access redirects; the present review did not obtain that text or repeat those network attempts.
Accordingly this finding supplies sufficient local mathematical support for the full conclusion while preserving that separate source-attribution/access limit.
It does not certify that the published corollary says the same thing as v2.

The accepted analytic subordination foundations, the general existence theorem for formal linear representations and their external references were not independently re-audited beyond the exact statement, construction and application interfaces identified above.
There is no formal verification claim.
The ACSY24 Lemma 3.3 tensor-adjoint input used by C_F0146 and C_F0149 is outside this review and is unaffected by this particular source-interface objection.
This finding changes no C/T decision, edits no U source material and clears no shared erratum or maintenance item.
