---
author: Yin
---
# Independent review of the general Atiyah linear criteria and fullness obstructions

Review act: 2026-11-10T18:47, in UTC, recorded for Yin.
This is an initial independent whole-argument inspection of the 2026-11-11 (Asia/Hong_Kong) revision of [Yin_L_A0004_v1](../../ledger/Yin_L_A0004_v1.md#setting-and-exact-criteria).
The reviewer did not participate in its substantive development and received the fixed argument, assignment, necessary dependencies and current rules without inherited proof-development discussion or author explanations.
The complete ledger argument was read and its obligations identified before consulting the source-audit conclusions.
Those source units were then used at the explicit scopes below, while every local implication and both counterexamples were checked directly.
No prior project finding about this investigation was supplied or relied on.
The [Task contract](../../tasks/Yin_T_A0001_v1.md#contract) was read to compare the quantifiers and completion scope; this review neither selects a Claim assessment nor completes that Task.

## Inputs and accepted foundations

The mathematical input is the complete fixed ledger revision, including the Laurent fullness proof, the all-matrices Atiyah premise for the example, and the final route limitation.
[MSY23-U001](../literature/MSY23/Yin_U001.md#proposition-23-and-lemma-24) supplies the exact stable-finite Schur criterion.
[MSY23-U003](../literature/MSY23/Yin_U003.md#lemma-48-linearization-preserves-an-existing-inverse-domain) supplies linearization preserving an already existing inverse domain, and its [closure argument](../literature/MSY23/Yin_U003.md#complete-division-closure-and-proposition-411) supplies rational inverse closure, \(D\subseteq R\), and equality when either closure is a division ring.
[MSY23-U004](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) supplies the finite affiliated-algebra foundations, unnormalized rank and full-rank invertibility; its [rank argument](../literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof) supplies invariance under invertible affiliated multiplication.
The affine rational-closure criterion in [MSY23-U005](../literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence) was compared with the local specialization.
The source units' general affiliated-algebra, polar-decomposition and matrix-amplification foundations are accepted inputs; their original foundational proofs were not re-audited.
The actual local uses of stable finiteness, block elimination, inverse closure, division-ring elimination and rank inequalities were checked independently.

The retained primary [MSY23 article](../../literature/pdf/MSY23.pdf) was freshly read in text at published pp. 6--7, 24--26, 33--34 and 43--44.
These passages verify Theorems 1.2 and 5.25, the scalar rows and columns and existing inverse domain of Lemma 4.8, Proposition 4.11, and Remark 5.11's polynomial-ring warning.
The corrected inverse-closure argument in U003 is used in place of the printed missing inverse and sign on p. 26.
The original general realization and affiliated-algebra literature was not recursively audited.

The retained primary [Coh06 book](../../literature/pdf/Coh06.pdf) was freshly read in text at the title/copyright pages and printed pp. 290, 297 and 299, corresponding to PDF pp. 314, 321 and 323 for the mathematical passages.
This confirms the 2006 NetLibrary edition, Section 5.5 equation (1), its Koszul-resolution explanation, and Exercise 5.5.4.
These are attribution checks, not reliance on an unchecked assertion that polynomial fullness survives localization.
No complete audit of Cohn's chapter or of the Koszul-resolution foundations was performed or needed for the local augmentation proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Exact criteria](../../ledger/Yin_L_A0004_v1.md#setting-and-exact-criteria) | All seven conditions, fixed ambient closures, matrix-size quantifiers, rectangular ranks and arbitrary-group reduction. |
| [Whole-argument finding](#whole-argument-finding) | [Source interfaces](../../ledger/Yin_L_A0004_v1.md#source-ingredients-and-rank-conventions) | Actual inverse domains, closure inclusions, stable finiteness, unnormalized rank and source applicability. |
| [Whole-argument finding](#whole-argument-finding) | [Equivalence proof](../../ledger/Yin_L_A0004_v1.md#proof-of-the-linear-and-bordered-equivalences) | Every implication, block identity, nonzero scalar step and global division-closure condition. |
| [Whole-argument finding](#whole-argument-finding) | [Formal fullness obstruction](../../ledger/Yin_L_A0004_v1.md#why-formal-free-algebra-fullness-cannot-be-retained) | Formal fullness, evaluated factorization and analytic rank one for the inverse-generator tuple. |
| [Whole-argument finding](#whole-argument-finding) | [Group-ring obstruction](../../ledger/Yin_L_A0004_v1.md#a-group-ring-full-linear-pencil-that-is-analytically-singular) | Complete Laurent augmentation proof, analytic rank, all-matrices Atiyah premise, actual closures and explicit factorization. |
| [Whole-argument finding](#whole-argument-finding) | [Obstruction attribution](../../ledger/Yin_L_A0004_v1.md#source-attribution-for-the-obstruction) | Cohn's exact displayed matrix and variable conversion, edition and locators, MSY23 warning and local-adaptation boundary. |
| [Whole-argument finding](#whole-argument-finding) | [Route consequence](../../ledger/Yin_L_A0004_v1.md#consequence-for-the-research-route) | Strict strength of the global group-ring-full invertibility condition, bordered rank interval and the remaining all-groups obstruction. |

## Seven-way equivalence and ambient checks

The tuple includes the inverses of the fixed group generators, so its polynomial image is exactly \(B=\lambda(\mathbb CG)\).
The group trace is faithful and normalized on the finite von Neumann algebra, while matrix rank uses the unnormalized matrix trace.
For an \(m\)-by-\(n\) matrix, rank equals \(n\) minus kernel dimension, so the rectangular formulation has the intended normalization.
Rectangular statements follow either by division-ring elimination or by padding a rectangular matrix into a square matrix with zero rows or columns.
No algebraic freeness, selfadjointness, invertible constant term or bounded inverse is used.

Lemma 4.8 applies to each element of the actual rational closure and yields an affine denominator invertible in the same \(U\).
Its inverse belongs to \(M_N(R)\) by the definition of \(R\), which justifies performing the Schur operations over \(R\) as well as \(U\).
The general inequalities \(\operatorname{rk}_G(P)\leq\rho_R(P)\leq\rho_D(P)\leq\rho_B(P)\) have the correct direction because \(B\subseteq D\subseteq R\subseteq U\).
The first inequality follows from a factorization through \(k\) coordinates and the affiliated rank inequality; it needs no integrality assumption.

Division of \(R\) gives Gaussian elimination, hence the rectangular rank equality, condition 1, and condition 3.
Proposition 4.11 gives \(D=R\) and the equivalence with condition 6, and then condition 4 follows.
Condition 1 implies condition 2 because each pencil is a group-ring matrix.
For condition 2 implying condition 7, the border is affine and its invertible \(N\)-by-\(N\) block gives rank at least \(N\); the size gives rank at most \(N+1\).
Thus integer rank leaves exactly the two claimed values.

Direct multiplication verifies the displayed three-factor identity with \(-r\) and \(I_N\), including the order of every noncommuting factor.
Both exterior factors are invertible over \(R\), so the border has rank \(N+\operatorname{rk}_G(r)\).
For \(r\ne0\), faithfulness gives \(0<\operatorname{rk}_G(r)\leq1\).
Condition 7 therefore forces scalar rank one, affiliated invertibility, and then inverse closure puts the inverse in \(R\).
This proves condition 5 without assuming that nonzero group-ring elements were already invertible.

For condition 3 implying condition 5, the stable-finite Schur argument is sufficient without any general additivity theorem for inner rank over arbitrary rings.
A factorization of \(\operatorname{diag}(I_N,-r)\) through \(N\) coordinates gives square top factors \(P_0Q_0=I_N\); stable finiteness gives the reverse identity, and the zero off-diagonal blocks force the remaining row and column to vanish.
This would give \(r=0\), a contradiction.
Fewer coordinates can be padded to \(N\), so the nonzero border is full of size \(N+1\).
Condition 3 gives its inverse over \(U\), and the same block identity and inverse closure give \(r^{-1}\in R\).
Finally, \(R\)-fullness implies \(D\)-fullness by the rank inequalities, so condition 4 implies condition 3.
The reverse implication goes through the now proved division-ring conclusion; it is not a pointwise equality of fullness predicates before that conclusion.
These implications cover all seven conditions without a cycle or an omitted converse.

For arbitrary torsion-free discrete \(G\), every finite matrix is supported in a finitely generated torsion-free subgroup \(H\).
The decomposition of \(\ell^2(G)\) over right cosets \(Ht\) makes each convolution block a copy of the operator over \(H\), and the diagonal trace at the identity is the \(H\)-block trace.
Thus its kernel dimension agrees over \(H\) and \(G\), including for an uncountable group.
This supplies precisely the finite-support reduction used in the Task; it asserts the finite-tuple conditions for every finitely generated subgroup, without requiring a finite generating set for \(G\) itself.

## Counterexamples and the Laurent proof

For the formal two-variable matrix, specialization at \(a=b=0\) is invertible and rules out a one-coordinate factorization over the free algebra.
Its evaluation at \((g,g^{-1})\) has the displayed one-coordinate factorization and an entry equal to \(1\), so its analytic rank is exactly one.
This defeats formal free-algebra fullness even in the one-generator abelian group and leaves the actual rational-closure criterion intact.

For the Laurent example, both kernel identities for \(k=(z,-y,x)^{\mathsf T}\) hold by direct multiplication.
The minor \(x^2\ne0\) and the kernel vector give field rank exactly two.
If \(T=PQ\) through two coordinates, that field rank makes \(P\) injective and \(Q\) surjective over \(F\), so the two kernel identities imply \(k^{\mathsf T}P=0\) and \(Qk=0\).
The quotient description of \(B/\mathfrak m^2\) is valid because each \(1+x,1+y,1+z\) is a unit modulo the square ideal.
Reducing each displayed syzygy modulo \(\mathfrak m^2\) leaves the three constant coefficients multiplying independent classes \(z,-y,x\), forcing every entry of \(P\) and \(Q\) into \(\mathfrak m\).
Their product then has every entry in \(\mathfrak m^2\), contradicting \(T_{12}=x\).
Padding covers all smaller factorization dimensions, so the proof establishes Laurent inner rank three directly.

The Fourier representation gives analytic rank two almost everywhere, since the determinant vanishes and \(x^2\) vanishes only on a Haar-null set.
The stated induction for any nonzero Laurent polynomial is complete: after clearing negative powers, at least one coefficient polynomial is nonzero, its null set contains the common coefficient-zero set, and outside that exceptional set the one-variable polynomial has finitely many roots.
Fubini then proves the required null-set assertion.
A maximal nonzero minor determines the almost-everywhere rank of each nonzero rectangular polynomial matrix, and the zero matrix has rank zero.
Consequently the example satisfies the full all-matrices complex Atiyah premise, not merely integrality for the particular \(T\).

Every nonzero element of \(B\) is a unit of \(U\), yielding a faithful copy of \(F\).
A singular matrix over \(F\) retains a nonzero kernel vector in \(U\), whereas a nonsingular matrix has its inverse in \(F\); this proves rational closedness in the actual ambient algebra and hence \(D=R=F\).
The final displayed factorization multiplies to \(T\), including the cancellation in its bottom-right entry, so \(\rho_R(T)=2\).
This gives the asserted strict failure of the global group-ring-full invertibility condition while satisfying the retained rational-closure criterion.
The final route sentence correctly distinguishes that stronger global condition from the pointwise fullness predicate, whose group-ring version is weaker by rank monotonicity.

## Whole-argument finding

The complete argument is mathematically supported at the stated scope, with no substantive gap found.
The seven equivalent criteria, rank equality, arbitrary-group reduction and both counterexamples pass independent inspection under the explicit accepted affiliated foundations.
The checked source attribution is accurate: the rational-closure criterion is MSY23 Theorem 5.25, announced as Theorem 1.2, and the polynomial obstruction is Cohn's displayed example under the stated signed permutation of variables.
The linear-rank and bordered formulations follow from the same existing-domain linearization mechanism; the Laurent extension is proved locally and is not inferred from polynomial fullness alone.
No source-completeness defect was identified in these cited substantive uses, and no novelty or historical-priority conclusion is inferred.

This is a proof and source-applicability review of the complete investigation, not a proof of the general Atiyah conjecture or a whole-source audit.
The remaining mathematical task is exactly the excluded bordered rank interval for all admissible pencils in torsion-free groups; the equivalence supplies neither that exclusion nor a uniform finite size bound or bounded inverse.
No numerical computation, proof-assistant formalization or manuscript layout/build verification was performed or used as evidence.
