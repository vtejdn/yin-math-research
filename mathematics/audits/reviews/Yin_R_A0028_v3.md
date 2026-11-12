---
author: Yin
---
# Independent review of the short-cycle trinomial bound

Review performed at 2026-11-11T19:24 UTC for Yin.
The inspected fixed artifact is [C_A0009_v4](../../claims/Yin_C_A0009_v4.md), including its entire statement, argument, tables, native enumeration, cyclic counterexample and remaining scope.
This is new independent evidence in the existing R_A0028 topic family; the preceding physical versions retain their own inputs and findings.

## Review arrangement and inputs

The reviewer was outside substantive development of this proof and received only the fixed candidate, the review assignment, applicable rules and operational metadata.
No development dialogue, proof summary, draft or author explanation was supplied or consulted.
The initial findings were formed by reading the complete candidate and necessary fixed mathematical inputs, independently reconstructing the group calculations and reproducing the finite counts with a separately written exact Python calculation.
Only after forming those findings was [R_A0028_v2](Yin_R_A0028_v2.md) read to confirm the existing review family and compare the unchanged moment-certificate interfaces.
Its conclusion supplied no substitute for the current inspection.

The necessary local mathematical inputs were the cyclic regular-representation certificate in L_A0002, the three-support ordered-quotient application in L_A0021, and the weighted defect, strict polynomial estimate and tree moments in C_A0009_v3.
The exact Lin92 source use was followed through C_A0004_v3 and checked against the primary theorem.
The indicated portions of L_A0025 and L_A0027 were read as limitations and comparisons, not as premises of the short-cycle theorem.
The accepted analytic foundations are the canonical group trace, bounded spectral calculus, faithfulness of that trace and the regular representation, and orthogonal decomposition over subgroup cosets.
This review does not reprove those general foundations or re-audit the historical proof of Lin92 Theorem 4.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact statement](../../claims/Yin_C_A0009_v4.md#statement) | The nonzero-kernel moment and weighted-defect restrictions, the unconditional strict scalar bound 8/29, and the necessary configuration when the kernel dimension is at least 1/4. |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete argument](../../claims/Yin_C_A0009_v4.md#argument) | The whole fixed argument, including all actual-quotient exclusions, every finite table and multiplicity, exhaustion, trace interpretation, constants, strictness, optimality and the cyclic counterexample. |
| [Whole-artifact finding](#whole-artifact-finding) | [Cyclic certificate](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) | Infinite-order regular shifts and nonzero Laurent-polynomial injectivity, including passage to ambient subgroup cosets. |
| [Whole-artifact finding](#whole-artifact-finding) | [Degenerate labels](../../ledger/Yin_L_A0021_v1.md#actual-setting-and-fixed-inputs) | The three coincident-label reductions for the actual trinomial. |
| [Whole-artifact finding](#whole-artifact-finding) | [Ordered-quotient certificate](../../ledger/Yin_L_A0021_v1.md#a-nontrivial-right-orderable-quotient-suffices) | The exact scalar Lin92 application: a nontrivial quotient leaves at most two distinct labels in each coefficient fiber, and every such coefficient is independently injective. |
| [Whole-artifact finding](#whole-artifact-finding) | [Common-square interface](../../ledger/Yin_L_A0021_v1.md#normality-of-the-trinomial-itself-has-a-second-exact-collapse) | The identity converting equal squares to inversion of a cyclic generator; the current candidate supplies its own actual-group quotient proof. |
| [Whole-artifact finding](#whole-artifact-finding) | [Primary ordered-quotient use](../../claims/Yin_C_A0004_v3.md#ordered-quotient-source) | Exact identification and hypothesis match for Lin92 Theorem 4 on printed pages 50--51; no coverage of the other C_A0004_v3 arguments is asserted. |
| [Whole-artifact finding](#whole-artifact-finding) | [Earlier weighted defect](../../claims/Yin_C_A0009_v3.md#statement) | The definition of the weighted defect and its strict four-moment inequality, as used by v4. |
| [Whole-artifact finding](#whole-artifact-finding) | [Earlier polynomial argument](../../claims/Yin_C_A0009_v3.md#a-polynomial-certificate-using-four-actual-moments) | M3--M9, including positivity, ordinary augmentation strictness and the implication from dimension at least 1/4 to positive weighted defect. |
| [Whole-artifact finding](#whole-artifact-finding) | [Tree moments](../../claims/Yin_C_A0009_v3.md#the-exact-free-word-moments-and-a-sufficient-collision-hypothesis) | The degree-three-tree counts 3, 15, 87, 543; independently reproduced by free-group convolution. |
| [Whole-artifact finding](#whole-artifact-finding) | [Variational attribution](../../claims/Yin_C_A0009_v3.md#source-attribution-known-coverage-and-remaining-joint-requirement) | Sim08 Theorem 9.2 and equations (9.6)--(9.7) as attribution for the finite polynomial minimization, which the current candidate also proves directly. |

## Whole-artifact finding

The complete fixed argument supports all of C_A0009_v4's stated conclusions.
No unresolved mathematical gap or necessary source-attribution correction was found.
The moment and defect restrictions are conditional on a nonzero kernel; the strict bound on kernel dimension is unconditional after the zero-kernel and coincident-label cases are included.
The result remains a scalar quantitative bound and does not establish injectivity, arbitrary matrix integrality or completion of A0001.

### Regular operators, degeneracies and quotient hypotheses

The kernel of the bounded operator \(T\) equals the zero spectral subspace of \(X=T^*T\), and its projection belongs to the group von Neumann algebra.
Faithfulness makes a nonzero kernel equivalent to positive projection trace.
For \(H\) generated by the two labels, left convolution preserves each right \(H\)-coset and the kernel projection is the corresponding orthogonal direct sum.
Its identity matrix coefficient is therefore the \(H\)-trace of the \(H\)-kernel projection, which justifies equality of the stated scalar dimensions over \(H\) and the ambient group.

The coincident-label cases give \(2-v\), \(u\) or \(1\), respectively, and are injective.
In the first case the Neumann series converges because the unitary \(v\) has norm one and the constant is two.
For a nontrivial cyclic supporting subgroup, the augmentation-one trinomial is a nonzero Laurent polynomial; its finitely many circle zeros give zero regular kernel.
The trivial subgroup is already covered by the degenerate cases.

For a nontrivial quotient of \(H\), the images of the three distinct support labels cannot all coincide because \(a\) and \(b\) generate \(H\).
Every coefficient fiber thus contains one or two distinct group elements and is nonzero.
Factoring a two-term coefficient reduces it to a nonzero scalar times a group unit times \(1+\gamma n\), where \(n\) is a nonidentity element of the torsion-free quotient kernel.
The bilateral-shift certificate makes that coefficient injective on the kernel subgroup's regular Hilbert space.
It consequently annihilates no nonzero von Neumann algebra element, exactly the source hypothesis for the least quotient coefficient.

For the cyclic-normalizer argument, the relation \(x_{n+1}^k=x_n\) makes the cyclic subgroups nested even when \(k\) is negative.
Their union is abelian, and conjugation by \(t\) or its inverse preserves the union.
For \(k=2\) or \(-2\), a positive power of \(t\) in this union would centralize \(x\) while conjugation gives \(x^{k^m}\), forcing a forbidden nontrivial finite power of \(x\) to be the identity.
For \(k=-1\), an equality \(t^m=x^r\) gives \(r=0\) on conjugation by \(t\), then \(t=e\) by torsion-freeness, and finally \(x=e\), again a contradiction in the remaining case.
Thus the cyclic quotient is infinite in precisely the cases used.
When \(x=e\) or \(k=1\), the nontrivial cyclic or finitely generated torsion-free abelian group also maps onto the integers.
This reasoning concerns the actual generated group and survives arbitrary further relations compatible with its hypotheses.
For \(x^2=y^2\), putting \(w=xy^{-1}\) gives \(ywy^{-1}=w^{-1}\); the \(w=e\) case is cyclic and the other case falls under the checked normalizer argument.

### Independent finite enumeration and graph interpretation

For the displayed block operator, the inverse chronological transport from the first part is exactly the alternating word in (4).
A reversal uses the same color twice, so cyclic nonbacktracking is precisely unequal adjacent colors, including the last and first.
The product of edge signs is determined by the parity of color 2.
Free reduction, conjugation and inversion preserve that parity and preserve whether the word is an identity.
This verifies the grouping into free cyclic word classes and the use of a single signed multiplicity for each class.
Additional equalities or conjugacies in the actual group do not justify merging those counted contributions.

The independent calculation represented free words as tuples of signed generator indices, reduced them by a stack, removed inverse end pairs, and compared rotations of both orientations.
It enumerated color strings directly with a separately written implementation, without executing or copying the candidate's JavaScript.
A separate orbit calculation applied all six color permutations, all cyclic rotations and reversal.
The resulting representatives and orbit sizes were exactly the displayed color table:

| Length | Orbit sizes in the candidate's displayed order | Marked strings | Word classes |
| --- | --- | ---: | ---: |
| 4 | 6, 12 | 18 | 6 |
| 6 | 6, 36, 18, 6 | 66 | 13 |
| 8 | 6, 48, 24, 48, 48, 48, 12, 24 | 258 | 36 |

Every signed word-class multiplicity agreed with the candidate's tables and its eighteen-word negative list.
At length eight the positive multiplicities sum to 114 and the eighteen negative multiplicities are each -8, with unsigned total 144.
There was no empty-word class among these cyclically nonbacktracking strings.
The recurrence for the final color in the text independently gives \(2^n+2\) marked proper colorings for even \(n\), so the orbit totals prove exhaustion rather than merely sampling the patterns.
Inspection of the native JavaScript also found its loop, alternating-word conversion, reduction, inverse/rotation convention and signs consistent with this independent enumeration.
No group solver, floating-point estimate or developer-reported run was used to establish the counts.

Every length-four group consequence follows from a displayed power of \(a\), \(b\), \(a^{-1}b\), or a two-letter product, using torsion-freeness only for a power equal to the identity.
The length-six noncyclic alternatives are exactly commutation, equal squares and the two inversion relations.
For the less immediate substitutions, \(c=a^{-1}b\) converts \(AAbAb\) to \(a^{-1}c^2\) and \(AbAbb\) to \(c^2b\), giving respectively \(a=c^2,b=c^3\) and \(b=c^{-2},a=c^{-3}\).
These checks account for every row of both short tables and show that a nonzero kernel excludes every four- or six-cycle.
The graph has no shorter, odd or doubled cycle because it is simple, bipartite and has three distinct labels at every vertex.

At girth at least eight, a closed walk of length at most six reduces completely by deleting reversals.
A length-eight closed walk that does not reduce completely must have reduced cyclic core of length eight and no nonempty tail, since otherwise it would contain a shorter simple cycle.
Thus its whole color string is cyclically nonbacktracking.
All completely reducing walks have positive sign and lift to the universal degree-three tree with the same local color choices.
Independently multiplying \(T^*T\) four times in the free group gives the identity coefficients \(3,15,87,543\), agreeing with the supplied Dyck-excursion derivation.
This proves the exact decomposition (5) and identifies its signed eight-cycle correction with the weighted defect only after the second and third moments have their free values.

### All positive classes and the defect restriction

The length-eight power rows reduce to \(a=e\), \(b=e\), \(a=b\), \(ab=e\), \(b=a^2\), \(a=b^2\) or \(a=b^4\) as stated.
The four rows involving conjugation give precisely the powers 2 or -2 in the normalizer exclusion, with the direction of the conjugation as printed.
For the other excluded rows, the substitutions give \(AABB\) as equality of the squares of \(a\) and \(b^{-1}\), \(AAAbAb\) as \(a^{-2}c^2\), \(AbAbbb\) as \(c^2b^2\), and \(AbAbAbb\) as \(c^3b\).
They therefore yield exactly the displayed common-square or cyclic consequences, and the changed generators still generate \(H\).
This checks all eighteen positive rows individually, including the cases of a trivial changed generator.

The three remaining rows are equivalent to \(b^2=a^3\), \(bab=a^2\) and \(ba^2b=a\), hence exactly the three relations \(R_j\) in (7).
Each makes \(a^3\) central because \(a\) and \(ba^j\) generate \(H\).
Two distinct indices yield \(ba^{j-i}b^{-1}=a^{-(j-i)}\), whereas centrality forces \(a^{3(j-i)}\) to be fixed under the same conjugation.
Torsion-freeness would then give \(a=e\), forbidden by distinct labels.
At most one positive retained class can consequently contribute.

Every negative class contributes either zero or -8 without needing a further group-theoretic exclusion.
The exact sum is therefore \(\Gamma=8(r-n_-)\), with \(r\) equal to zero or one.
This gives integrality in multiples of eight and the upper bound eight.
The strict earlier polynomial estimate gives \(\Gamma>0\) whenever the kernel dimension is at least \(1/4\); the exact sum then forces \(r=1\) and \(n_-=0\) and yields the moments \((3,15,87,551)\).
None of these implications constructs a group or a positive kernel satisfying the necessary conditions.

### Quadratic certificate, strictness and counterexample

Direct exact rational arithmetic gives
\[
q(s)^2=1-s+\frac{41}{116}s^2-\frac3{58}s^3+\frac9{3364}s^4.
\]
The coefficient of the fourth moment is positive, and substitution of \((3,15,87,551)\) gives \(8/29\).
Because \(q(0)=1\), the difference \(q(X)^2-p\) equals \(q(X)^2(1-p)\) and is positive.
Equality of the traces would make that difference zero, and idempotence of \(p\) would give \(q(X)^4=q(X)^2\) inside the faithfully represented finite-support group algebra.
Ordinary augmentation then gives \(q(1)=16/29\), whose square is neither zero nor one.
This contradiction verifies strictness without any extension of augmentation to the von Neumann algebra and without assuming the kernel projection is rational.
The separated zero-kernel cases complete the universal scalar conclusion.

The quadratic moment matrix has positive first diagonal entry and determinant 696, so the normal equations have a unique minimum.
Their solution is exactly \(c=-1/2\) and \(d=3/58\), giving minimum \(1+3c+15d=8/29\).
The real and imaginary polynomial parts commute as functions of \(X\), and the imaginary part contributes a nonnegative squared norm, so complex coefficients cannot improve that minimum.
The stated optimality is only for degree at most two with constant term one and the specified moments.

The cyclic example was independently checked by exact Laurent-polynomial convolution.
It gives \((3,19,141,1107)\), and the weighted defect is
\[
113(19-15)-18(141-87)+(1107-543)=44.
\]
Here the weighted defect is not just \(m_4-543\), since the conditional free values of \(m_2\) and \(m_3\) do not hold.
The underlying augmentation-one Laurent polynomial is injective by the cyclic certificate, so the example disproves an unconditional defect ceiling without contradicting the scalar kernel bound.

### Source completeness and limits

The primary [Lin92 journal scan](https://math.uchicago.edu/~shmuel/L%5E2%20cohomology%20readings/Linnell,%20zerol2.pdf), Theorem 4 on printed pages 50--51, was inspected for its statement, quotient order, left coefficient convention and least-coefficient hypothesis.
The local application matches those hypotheses and uses the theorem only for scalar analytic injectivity.
Its historical proof was not re-audited; the established theorem is accepted at this checked statement-and-applicability scope.

The primary [Sim08 arXiv v1](https://arxiv.org/pdf/0806.1528v1), printed/PDF page 15, supplies the named Christoffel variational principle in Theorem 9.2 and equations (9.6)--(9.7).
The orthonormal expansion and preceding finite-dimensional minimization were inspected.
This attribution matches the finite polynomial problem, whose specialization and constants are proved directly in the candidate and rechecked above.
It supplies no independent assumption needed for the 8/29 calculation.

The pairwise-Haar and tensor materials are correctly treated as comparisons that do not supply the missing actual joint-word information.
No orderability, unique-product property, preservation of Atiyah under quotient, replacement of the original labels, or injectivity of a retained common-power group is assumed.
The conclusions establish neither a newly covered whole-group Atiyah class nor a positive-kernel example.
There is no formal verification or literature-wide novelty finding in this review, and the broader all-matrix Task remains unresolved.
