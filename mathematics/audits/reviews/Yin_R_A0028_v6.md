---
author: Yin
---
# Independent review of the weighted fifth-moment condition

Review performed at 2026-11-12T01:20 UTC for Yin.
The inspected fixed artifact is [C_A0009_v7](../../claims/Yin_C_A0009_v7.md), including its complete statement, signed-path argument, polynomial, finite enumeration claims, source attribution and full-Task limits.
This is new independent evidence in the existing R_A0028 family; earlier physical versions retain their own exact inputs and findings.

## Review arrangement and inputs

The reviewer was outside substantive proof development and received the fixed candidate, assignment, applicable rules and operational metadata.
No development dialogue, mathematical summary, draft or author explanation was supplied or consulted.
Initial findings were formed from the whole candidate and its direct mathematical inputs before reading previous review conclusions.
The complete fixed C_A0009_v3, C_A0009_v4 and C_A0009_v6 arguments and the continuing J_A0001 README and native program were read.
Only afterward were R_A0028_v5 and the pertinent input, graph, enumeration and source portions of R_A0028_v3 consulted to check the existing accepted dependency scopes.

The new moment identity, all displayed numerical constants, bounded spectral comparison, augmentation strictness, endpoint consequences and finite minimization were checked directly.
The already independently reviewed v6 girth-ten theorem is accepted at its unchanged scope, with its hypotheses and use checked here.
Its earlier common-power and central-support chain is not claimed as a newly reproduced full dependency audit.
The accepted analytic foundations are bounded functional calculus, the faithful canonical group trace and the faithful regular representation of the finite-support group algebra.
Their application is checked without a new proof audit of those general foundations.

The native computation was inspected and its finite functions were executed in memory with Python 3.14.7 and standard-library exact arithmetic, without changing its program or generated output.
A separately written exhaustive color-string enumeration and a separate Dyck-path enumeration were compared with those native functions.
The computational check is supplementary: none of the class totals at lengths ten or twelve is a premise of the theorem.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact statement](../../claims/Yin_C_A0009_v7.md#statement) | The strict bound under actual simplicity and girth at least ten, the negative ten-cycle necessity at kernel trace at least 2/9, and the signed-count bound at trace at least 4/19. |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete argument](../../claims/Yin_C_A0009_v7.md#argument) | The whole fixed proof, all moment and polynomial constants, augmentation strictness, threshold interfaces, coefficient optimization, finite computation scope and full-Task limitations. |
| [Whole-artifact finding](#whole-artifact-finding) | [Accepted girth theorem](../../claims/Yin_C_A0009_v6.md#statement) | The actual original-label graph is simple and has girth at least ten whenever the same trinomial kernel trace is at least 4/19. |
| [Whole-artifact finding](#whole-artifact-finding) | [Accepted girth review](Yin_R_A0028_v5.md#whole-artifact-finding) | Reuse of the unchanged independently reviewed v6 theorem and its precise earlier accepted dependency scope; no new full audit of the central-support or source proofs. |
| [Whole-artifact finding](#whole-artifact-finding) | [Signed graph convention](../../claims/Yin_C_A0009_v4.md#signed-paths-and-a-complete-finite-counting-convention) | The block adjacency, marked part, alternating labels, path closure and sign convention used in the fifth-moment identity. |
| [Whole-artifact finding](#whole-artifact-finding) | [Short-path interface](../../claims/Yin_C_A0009_v4.md#every-four--or-six-cycle-excludes-a-nonzero-kernel) | The cancellation and tree-lifting mechanism; v7's girth-ten and length-ten case is checked directly. |
| [Whole-artifact finding](#whole-artifact-finding) | [Tree moments](../../claims/Yin_C_A0009_v3.md#the-exact-free-word-moments-and-a-sufficient-collision-hypothesis) | The Dyck-path calculation of moments through order four, independently checked here and extended through the fifth moment used by v7. |
| [Whole-artifact finding](#whole-artifact-finding) | [Existing variational attribution](../../claims/Yin_C_A0009_v3.md#source-attribution-known-coverage-and-remaining-joint-requirement) | The retained Sim08 Section 9, Theorem 9.2 attribution; the weighted finite-dimensional specialization is proved locally and checked here. |
| [Whole-artifact finding](#whole-artifact-finding) | [Prior source and graph inspection](Yin_R_A0028_v3.md#whole-artifact-finding) | Reuse of its unchanged signed-graph and tree-moment checks and its inspected Sim08 attribution, without claiming a new primary-source reading. |
| [Whole-artifact finding](#whole-artifact-finding) | [Continuing computation](../../computations/programs/Yin_J_A0001/readme.md) | The inspected 2026-11-12 finite conventions and stated totals through length twelve; the actual-group and theorem-dependency limitations remain in force. |
| [Whole-artifact finding](#whole-artifact-finding) | [Native program](../../computations/programs/Yin_J_A0001/cycles.py) | The inspected implementation of free reduction, cyclic representatives, proper-color generation, signed counts, tree moments and weighted rational certificate, executed at lengths 4, 6, 8, 10 and 12; no promise of coverage of later program changes. |
| [Whole-artifact finding](#whole-artifact-finding) | [Original Task contract](../../tasks/Yin_T_A0001_v1.md#contract) | Scope comparison only: all torsion-free groups and arbitrary finite rectangular complex group-ring matrices remain beyond this scalar necessary condition. |

## Whole-artifact finding

No mathematical defect or unresolved necessary premise was identified in the whole fixed v7 argument at its stated scope.
It proves
\[
 \delta<\frac29-\frac{C_{10}}{1296}
\]
under the actual simple girth-ten hypothesis and proves both stated threshold consequences by the accepted v6 interface.
The native finite counts quoted in the ancillary computation discussion are correct at the inspected scope.
Their correctness supplies no actual-group relation classification and is unnecessary for the displayed inequality.
No necessary new source-attribution correction was identified; the existing Christoffel attribution is reused at its recorded inspection depth.

### Signed walks and the actual fifth moment

For the convention \(B=\left(\begin{smallmatrix}0&T^*\\T&0\end{smallmatrix}\right)\), the first diagonal block of \(B^{2j}\) is \(X^j\).
The identity coefficient therefore counts all closed length-\(2j\) walks from the marked vertex in the X part, weighted by the product of their edge signs.
The graph is three-regular with the original three edge colors under the stated simplicity hypothesis.
An immediate reversal repeats the same edge sign twice, so removing it preserves the total sign.

At girth at least ten, a closed walk of length at most eight cannot leave a nonempty reduced closed walk, since that would contain a shorter cycle.
For length ten, a reduced surviving walk with a tail would contain a closed portion of length at most eight.
A repeated vertex in a nonbacktracking surviving length-ten walk would likewise cut out a shorter cycle.
Thus every length-ten closed walk either reduces completely or is itself a simple cyclically nonbacktracking ten-cycle.
In particular, no attached-tail contribution or shorter-cycle repetition is omitted from the formula.

Walks reducing completely lift uniquely to closed walks in the three-regular universal covering tree.
Their signs are positive, and the distance process gives the Dyck-path weights \(3^r2^{j-r}\).
For semilength five the excursion counts are \((14,14,9,4,1)\); the composition calculation in the candidate is correct, including the three-excursion split \(3\cdot2+3\).
Their weighted sum is
\[
 672+1008+972+648+243=3543.
\]
Together with the unchanged first four tree counts, this proves exactly \(m_5=3543+C_{10}\) in the actual group.
It does not assume a free joint distribution beyond the moment information supplied by the girth hypothesis.

### Polynomial comparison and strictness

The norm bound \(\|T\|\le3\) gives the actual spectral interval \([0,9]\) for \(X\).
For
\[
 q(s)=1-\frac23s+\frac1{12}s^2,
 \qquad P(s)=(1-s/9)q(s)^2,
\]
one has \(P\ge0\) on that whole interval and \(P(0)=1\).
Consequently \(P(X)-p=P(X)(1-p)\ge0\), where \(p=1_{\{0\}}(X)=P_{\ker T}\).
This uses a bounded polynomial in X and requires neither an inverse nor a domain assumption for an unbounded operator.

Direct rational expansion gives precisely
\[
 P(s)=1-\frac{13}{9}s+\frac{41}{54}s^2
 -\frac{29}{162}s^3+\frac{25}{1296}s^4-\frac1{1296}s^5.
\]
At \((m_1,\ldots,m_5)=(3,15,87,543,3543+C_{10})\), its trace is \(2/9-C_{10}/1296\).
The negative fifth-moment coefficient has the required sign; the candidate does not treat the signed cycle correction as an unsigned count.

Equality in the trace comparison would imply \(P(X)=p\) by faithfulness.
Idempotence then gives \(P(X)^2=P(X)\) as an equality of finite-support group-ring elements, since X and the polynomial coefficients already lie in that algebra.
The faithful regular representation permits interpreting this as an algebraic identity.
Ordinary augmentation gives \(\varepsilon(X)=1\), \(q(1)=5/12\) and \(P(1)=25/162\), contradicting idempotence.
No extension of augmentation to the von Neumann algebra is assumed.
The strict conclusion holds also at the endpoints of the stated threshold implications.

### Thresholds and coefficient choice

The accepted v6 theorem applies to the same torsion-free group, original labels, operator and trace.
Since \(2/9>4/19\), either threshold in v7 supplies its required simplicity and girth-ten hypothesis.
For \(\delta\ge2/9\), the strict inequality forces \(C_{10}<0\).
A negative signed sum contains a negative path, and the preceding girth argument makes it a simple ten-cycle.
For \(\delta\ge4/19\), the same inequality gives
\[
 C_{10}<1296\left(\frac29-\frac4{19}\right)
 =\frac{288}{19}<16.
\]
The number \(C_{10}\) is an integer, so the stated consequence \(C_{10}\le15\) follows.
Neither deduction asserts that a positive kernel or its necessary cycle configuration exists.

The weighted moment vector is exactly \((2,4,16,80,448)/3\).
Its displayed two-by-two matrix has positive leading entry and determinant
\[
 \frac{16\cdot448-80^2}{9}=\frac{256}{3}>0.
\]
Substitution of \((c,d)=(-2/3,1/12)\) solves both normal equations.
The positive definite matrix makes the quadratic functional strictly convex, and the minimum is
\[
 w_0+cw_1+dw_2=\frac29.
\]
The optimization is only within the stated weighted-quadratic family and specified free moments.
It is not an optimality assertion for every polynomial or every actual-group kernel bound.

### Native computation and its precise limits

The inspected program generates every proper cyclic color string exactly once by extending only distinct consecutive colors and checking the closing pair.
Its alternating labels agree with the fixed graph convention.
Stack cancellation, removal of inverse end pairs, rotations and inversion produce the specified free cyclic-word representative.
The parity of the negative color is invariant under these operations, so all members of one free class have a common sign.
The program's corresponding assertion checks that no signed cancellation is hidden within a class.

The native finite functions and a separate enumeration of all \(3^n\) color strings agreed on every signed class multiplicity at each tested length, not just on the aggregate totals.
The independent calculation represented nontrivial labels by signed integers, performed free reduction and cyclic trimming, and compared both cyclic orientations in the same declared lexical alphabet.
The resulting totals were:

| Length | Marked proper color strings | Free cyclic-word classes | Positive multiplicity | Negative multiplicity, absolute value |
| --- | ---: | ---: | ---: | ---: |
| 4 | 18 | 6 | 10 | 8 |
| 6 | 66 | 13 | 38 | 28 |
| 8 | 258 | 36 | 114 | 144 |
| 10 | 1026 | 105 | 542 | 484 |
| 12 | 4098 | 351 | 2026 | 2072 |

An independent exhaustive Dyck-path calculation agreed with the native weighted-distance recurrence through order six, giving \(1,3,15,87,543,3543,23823\).
The native Fraction calculation reproduced all coefficients of P, the determinant \(256/3\), the free value \(2/9\), \(P(1)=25/162\) and the fifth-moment coefficient \(-1/1296\).
The proof-level positivity and strictness arguments were checked mathematically rather than inferred from those finite outputs.
The J README retains the reproduction command and native program; the review does not depend on a disposable checker or generated JSON file.

No word problem in an actual torsion-free group, coexistence of relations, exclusion of negative ten-cycles or analytic kernel dimension was computed.
The program's allowed lengths above twelve were not executed in this review, and the output-publication entry point was not rerun.
The optional proper-power metadata is not a premise of the candidate theorem or the quoted class totals.
The continuing program's later revisions do not inherit this review automatically.

### Sources and the full-Task boundary

The finite minimization is a direct weighted-moment instance of the already attributed Christoffel variational mechanism.
The nonnegative weight \(1-s/9\) is valid on the free measure's spectral interval as well as the actual interval, and the explicit positive matrix supplies all nondegeneracy needed for this finite calculation.
The retained primary attribution is Sim08 arXiv v1, Section 9, Theorem 9.2 and equations (9.6)--(9.7), as inspected in the existing C_A0009_v3 and R_A0028_v3 accounts.
That primary text was not newly read here, and no stronger source-proof or priority claim is made.

The v6 dependency retains its existing independent whole-artifact finding, including the accepted earlier short-cycle and central-support scope.
This review checks its exact threshold and graph interface, and separately verifies every new v7 inference.
There is no cycle in the logical support: v6 supplies girth without using the new fifth-moment inequality or the new free-class totals.

The result supplies a necessary signed-cycle condition for a restricted scalar family.
It establishes neither a strict unconditional 2/9 bound, injectivity for smaller kernels, a reduction of arbitrary matrices to this scalar operator, nor an induction controlling all later rational pivots.
The full A0001 contract is unchanged and remains unresolved.
No formal verification or literature-wide novelty search is claimed.
