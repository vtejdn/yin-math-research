---
author: Yin
---

# Any finite free family of projections with arbitrary traces satisfies bounded division-closure equality — isolated current inspection

- Date and human attribution: 2026-10-22T22:40 UTC; Yin is the responsible human record author.
- Review arrangement: separate isolated independent inspection of the fixed target at the scope below.
  The inspecting agent did not develop or repair the target proof and received no author-development dialogue or earlier target verdict before the initial finding.
- Initial mathematical finding: 2026-10-22T22:26 UTC, with any later scope extension expressly distinguished below.
- Inputs and sequence: The fixed target mathematics and necessary direct dependency and source interfaces were inspected first; earlier findings and C assessment/recorded-scope material for this target were compared only after the initial inspection at the declared scope.
- Verification and limits: the mathematical derivations and necessary actual interfaces described below were checked directly.
  The new act does not repeat historical native computation, formal verification or the original reviewers' source inspections.
  Historical source-depth and access facts in the retained account remain facts of the original act, not new primary-source claims.
- Target and records: [C_F0105 fixed statement](../../claims/Yin_C_F0105_v1.md#statement) and its exact selected argument, bound below.
- Scope: Whole nine-section finite free-projection proof: arbitrary traces including scalar endpoints, exact rank-two defects and residual columns, minimal full-state energy, homogeneous operator bounds, bounded resolvent and finite bounded scalar Schur inverses; excludes diffuse or general finite-dimensional-factor permanence.
- Starting assessment: this act assesses the fixed mathematical statement and proof; the older current assessment was not used as mathematical evidence before the initial finding.

## Current isolated finding

Whole §§1–8 arbitrary finite free projections theorem checked.
Centered Bernoulli words form ON basis; bounded terminal deletion has exact rank<=2 boundary defect.
[C_F0034](../../claims/Yin_C_F0034_v1.md) exact all-H finite-defect interface gives bounded rational finite commutators.
Selected columns with different terminal factor yield all residuals; minimality makes all state entries l2 and μ_i²=0.
Direct creation/annihilation/one-diagonal expansion gives n+1+nκ scalar bound, including orthogonal Q_i blocks.
Positive finite-state map gives exponential decay, forbidden products ensure truly homogeneous V powers, positive Schur pivots reconstruct bounded scalar inverses and faithful vacuum identifies f.
Scalar endpoints are removed before taking the nontrivial centered-word basis; this preserves the endpoint cases.
No general diffuse-factor permanence is asserted.
Existing [C_F0105](../../claims/Yin_C_F0105_v1.md) Ricard–Xu scoped source account retained; local exact estimate independently verified, no full RX proof audit.

The stated conclusion is supported at this exact scope and with the displayed hypotheses and conditions.
No substantive mathematical repair was made during this inspection.
The original fixed mathematical version and proof remain the inputs.

## Comparison and retained original evidence

After the initial findings, the complete original [R_F0046 account retained below](#8-boundary-cases-and-final-acceptance) was read and compared scope by scope.
No disagreement requiring a mathematical correction was identified.
The retained original finding keeps its original mathematical coverage, date precision, source-access limits and actual relationship.
The complete original natural account follows as historical evidence; its first-person wording, original verdict wording, source checks and correction history refer to that older act.
Its relationship is given explicitly in the combined tables below and is not upgraded by the new independent finding.
No historical day-only date is assigned an invented minute.
<a id="original-f0046-account"></a>

## Independent Review: Bounded Rational Reconstruction for Free Projections

- Date/reviewer: 2026-09-11; the reviewing agent, independently reviewing the complete continuation authored by another subagent.
- Target: [Yin_C_F0105_v1.md](../../claims/Yin_C_F0105_v1.md), Sections 1-9 in full.
- Verdict: **pass at the stated finite freely independent projection-family scope; no mathematical correction required.**
  This audit does not allocate the proposed Claim ID, a mathematical Role, or shared-index status.

## 1. Statement and dependency boundaries

The target proves
\[
 \operatorname{Div}_{L^0(M)}A\cap M
       =\operatorname{Div}_M A,
 \qquad A=\mathbb C\langle p_1,\ldots,p_d\rangle,
\]
for every finite freely independent family of projections generating the finite tracial von Neumann algebra M.
Traces may be arbitrary in [0,1].
Faithfulness makes the endpoint-trace projections scalar, so removing them and renumbering the remaining family is valid.
The empty remaining tuple generates only the scalar algebra.
For nontrivial traces, the centered normalization and the coefficient kappa_i in target (2) give exactly x_i squared equal to 1 plus kappa_i x_i, with mean zero and L2 norm one.
The original and normalized polynomial algebras coincide.

The argument does not presume that its affiliated division closure is a division ring.
It needs no maximal Delta or normalized dual system for these atomic variables.
In particular the rank-two auxiliary defects are not incorrectly substituted into a theorem requiring a vacuum rank-one dual identity.

The reviewer checked the exact hypotheses and assertion 4 of [Yin_C_F0034](../../claims/Yin_C_F0034_v1.md#yin_c_f0034), together with its [independent acceptance](Yin_R_F0021_v1.md).
That lemma permits arbitrary finite-rank generator commutators and retains its stated affiliated-fraction foundations.
The [Miy22 finite-residual and minimal-representation interface](../literature/Miy22/Yin_U002.md#miy22-u002) was reread at its precise source acceptance level.
The original formal-series monograph remains an external foundation; the minimal-state consequences are checked directly below.

The [Ricard-Xu primary preprint](https://arxiv.org/pdf/math/0505302) was checked at the free-product representation on PDF pp. 2-3 and Theorem 2.5 with its upper-bound decomposition on pp. 6-7.
The [arXiv metadata](https://arxiv.org/abs/math/0505302) confirms the 2006 journal reference and the 27 February 2016 v2 revision.
These selected statements motivate the operator decomposition.
The target proves its particular scalar coefficient bound directly, so no unverified identification with the source's operator-space norm is needed.
Neither a whole-source nor a publication/preprint identity audit is claimed.

## 2. The Fock basis and the rank-two defects

The reduced free-product Hilbert decomposition applies with a one-dimensional centered Hilbert space for each nontrivial two-point factor.
Its alternating word vectors are orthonormal and complete.
Equivalently, the trace of x_v* x_w is computed by matching centered letters from the middle, with the variance-one factor at each match; freeness kills a mismatch and all unmatched centered reduced words.
This justifies the basis and the left action in (5)-(6), including unequal trace parameters.

Terminal deletion R_i is a partial isometry: its initial basis consists of words ending in i and its image consists of the corresponding shortened words, with no duplicate image.
Thus it is bounded on the whole Hilbert space, and its actual adjoint is everywhere defined.

The defect computation holds on every basis vector.
On the vacuum the commutator [R_i,x_j] gives delta_ij Omega.
On e_i with j=i it gives kappa_i Omega minus e_i.
On a distinct one-letter vector it vanishes.
For length at least two, left creation or cancellation commutes with terminal deletion.
In the length-two cancellation case, both orders yield the same vacuum and one-letter diagonal contribution; this boundary case introduces no extra defect.

The operator
\[
 K_i=P+\kappa_i P x_i-x_i P x_i
\]
has exactly those values.
Its two trace functionals vanish on longer reduced words, so it is supported on the span of Omega and e_i.
Hence the claimed finite rank, including the signs of the two correction terms, is correct.

For the Yin_C_F0034 application, E=H and V_i=H are dense left M-modules, and R_i as well as R_i* are bounded everywhere.
Every cleared defect is thus defined on the specified whole domain.
The lemma's general finite-defect inverse-closed algebra contains all x_j by the preceding calculation, and therefore contains their affiliated division closure.
For a bounded f the fraction choice s=t=1, a=b=f identifies its defect with the actual bounded commutator [R_i,f].
This supplies (9) without applying R_i to an undefined unbounded vector or assuming boundedness of an affiliated inverse.

## 3. The cut formula supplies every right residual

For a fixed alternating polynomial word v, the Leibniz expansion of [R_i,x_v] over its cuts v=u i q is valid.
At such a cut, both x_u x_i and x_i x_q remain reduced.
The vacuum trace at the first term selects w=q reversed.
The two correction terms select w=q reversed followed by i, with output kappa_i e_u minus e_(ui).
These are exactly the two alternatives in target (14).

The selected columns in (12) have w empty or with terminal letter different from i.
This removes the correction alternative entirely.
The remaining first alternative occurs at the cut v=u i w reversed, proving the stated right-residual order.
Dropping the terminal-letter restriction would give a false formula, but the proof retains it at every use.

Passage to bounded f uses only finite Fourier sums converging in L2.
For a fixed word w, right multiplication by x_w is bounded on L2, so f_N e_w tends to f e_w.
The same applies to the fixed vector R_i e_w, which is either zero or another word vector.
Boundedness of R_i therefore gives convergence of the corresponding commutator column.
On the coefficient side, extracting the coordinates indexed by u i w reversed is a contraction of the coefficient l2 space, because that word insertion is injective.
This proves the limit formula without operator-norm boundedness of the Fourier truncations.

Each nonempty alternating suffix t can be written i q, with the first letter of q different from i when q is nonempty.
Choosing w=q reversed is therefore always an allowed column.
Nonalternating suffixes have zero residual under the explicit zero extension of beta to the entire free monoid.
Every resulting residual still has zero coefficients at nonalternating prefixes, so its identification with an H-vector loses no information.
The empty suffix contributes f Omega.
Thus (15) bounds the whole formal residual span by the finite sum of the indicated commutator ranges and the vacuum coefficient vector.

## 4. Minimality gives full-state energy and forbids repeated letters

The accepted finite-residual theorem now applies to the actual coefficient function on the free monoid.
It produces a finite linear representation, and a minimal one can be chosen.
No equality between formal rational substitution and evaluated operator multiplication has been assumed at this point.

In a minimal representation, finitely many reachable columns mu(q) gamma form a basis and finitely many observable rows lambda mu(p) form the dual test basis after scalar linear combinations.
Pairing these bases with mu(w) expresses each state entry as a fixed finite linear combination of beta_(p w q).
For each fixed p,q, insertion of w is injective on the full monoid.
The square-summability of beta therefore implies square-summability of every state-entry sequence, with finite constants from the chosen bases.
Summing finitely many entries proves the Hilbert-Schmidt energy (17).
This step would fail for arbitrary padded, nonminimal states, which are not used.

Every coefficient beta_(p i i q) is zero, irrespective of p and q.
The same spanning rows and columns then show that every matrix element of mu_i squared is zero.
Thus mu_i squared is the zero matrix.
This is an identity on the entire state space, not merely a vanishing output lambda mu_i squared gamma.

Consequently every nonalternating matrix word mu(w) vanishes before the operator word x_w is reduced.
This is the crucial justification that the powers of V in (31) are homogeneous alternating sums.
In particular no lower-length contribution from x_i squared equal to 1 plus kappa_i x_i has been overlooked.

## 5. The homogeneous operator bound is exact at the stated constant

The partial creation identity x_i=L_i+L_i*+kappa_i Q_i follows directly from the basis action.
For adjacent distinct letters, each forbidden product in (21) vanishes by its first-letter support.
A nonzero term in the expansion of a reduced word must therefore have all creations first and all annihilations last, with at most one diagonal factor between them.
Any other pattern has one of the displayed forbidden adjacent pairs.
This proves the complete 2n+1 term expansion (22), including the endpoint cuts and the n=0 identity case.

For a fixed prefix length, the operators L_u have pairwise orthogonal ranges and norm at most one.
Their row operator is a contraction, as follows by summing the squares of these orthogonal outputs.
Its adjoint column operator is also a contraction.
No common full initial space or unitary property of the partial creators is required.

At a cut without a diagonal term, the coefficient matrix has entries c_(u v reversed), zero when the concatenation is not reduced.
The correspondence between reduced words and these coefficient positions is injective and exhaustive at that cut.
Factoring through the row and column contractions gives a norm bound by the coefficient matrix norm, which is at most its Hilbert-Schmidt norm and hence the scalar coefficient l2 norm.

At a fixed diagonal cut, factor through the same row and column contractions.
The remaining block operator is the sum over i of kappa_i C_i tensor Q_i.
Since the Q_i are pairwise orthogonal projections, its norm is the maximum of |kappa_i| times ||C_i||.
Each ||C_i|| is at most the Hilbert-Schmidt norm of its own coefficient slice, and that slice is at most the full coefficient l2 norm.
Thus each diagonal cut contributes at most kappa times that norm.
Coefficients at nonalternating concatenations are interpreted as zero here as well.

There are n+1 cuts of the first type and n of the second.
Their sum proves
\[
 \left\|\sum_{|w|=n}c_w x_w\right\|
 \le (n+1+n\kappa)\left(\sum_{|w|=n}|c_w|^2\right)^{1/2}.
\]
The proof introduces no exponential trace-dependent loss in n.
All these are operators on the actual infinite reduced free-product Hilbert space; no finite-dimensional compression is involved.

## 6. The positive state map yields an actual bounded inverse

For Phi(T)=sum mu_i T mu_i*, induction gives Phi^n(I) as the sum of mu(w)mu(w)* over words of length n, in the same multiplication order as the representation.
Its ordinary finite matrix trace is precisely the energy in (26).

The finite total state energy implies norm convergence of Q=sum Phi^n(I): all terms are positive and their norms are bounded by their summable traces.
Q is at least I and satisfies Phi(Q)=Q-I.
If Q=I, every positive mu_i mu_i* vanishes, so all transition matrices are zero and the construction is constant.
Otherwise ||Q||>1 and c=1-||Q|| inverse belongs to (0,1).
The inequality I>=Q/||Q|| yields Phi(Q)<=cQ.
Positivity and induction then yield Phi^n(I)<=c^n Q, including n=0.
This proves (29), not just a claimed spectral-radius condition.

Each entry of V^n is a homogeneous alternating scalar sum by Section 4.
Applying the preceding operator estimate entry by entry and using the total Hilbert-Schmidt coefficient energy gives the safe matrix bound with factor N in (32).
For example the matrix operator norm is at most N times the largest entry norm, and every such coefficient energy is bounded by the total energy.
The factor is independent of the word length.

The resulting geometric factor c^(n/2) dominates the linear word-length factor.
Hence the Neumann series converges in the actual matrix operator norm, even if ||V|| itself exceeds one.
Multiplication of its finite partial sums on either side by I-V gives I minus V to the next power, whose norm tends to zero.
This proves both inverse identities in M_N(M).
The constructed B is a new finite linear pencil for the coefficient series; the proof makes no claim about an arbitrary original affiliated linearization.

## 7. Positive Schur pivots use only bounded scalar inverses

The original algebra A is a unital *-algebra because its generators are projections.
Its bounded scalar division closure is also *-closed: induction on expressions uses the fact that the adjoint of a bounded inverse is the bounded inverse of the adjoint.
Thus B*B has entries in the permitted algebra and satisfies B*B>=delta I for the stated positive delta.

For the block matrix in (34), the scalar pivot a is at least delta times the identity, so its inverse belongs to M and is allowed in Div_M A.
For y in the remaining Hilbert direct sum, insert the vector (-a inverse b y,y) into the positive quadratic form.
Its value is the form of the Schur complement S at y, and it is at least delta times the sum of the two component squared norms.
In particular S>=delta I.
This argument verifies the same lower bound at every successive pivot; it does not only establish positivity or affiliated invertibility.

The displayed Schur inverse formula has the correct factor order in the noncommutative ring.
Recursing down to a scalar uses finitely many bounded scalar inverses; rebuilding upward uses additions and products of already admissible entries.
Therefore every entry of (B*B) inverse is in Div_M A, and multiplication by B* gives the same assertion for B inverse.
This proves scalar division-closure membership directly, rather than substituting a general matrix rational-closure claim for it.

The scalar output g=lambda B inverse gamma consequently lies in Div_M A.
Finite Neumann sums give exactly the truncated reduced-word coefficient sums, including the constant coefficient lambda gamma.
Their left side converges in operator norm to g, while their action on Omega converges in L2 to f Omega.
The trace is faithful, so Omega is separating for the left M action and g=f.
The reverse closure inclusion follows because every bounded inverse is also the corresponding affiliated inverse.

The additional characterization (39) is also proved.
Its reverse direction uses only finite rank of the actual bounded commutators and the already checked reconstruction.
Its forward direction follows from the bounded product and inverse commutator formulas beginning with (8).
It is correctly described as a deletion-operator criterion, not a normalized dual criterion for atomic variables.

## 8. Boundary cases and final acceptance

Scalar endpoint projections, the empty tuple, a single nontrivial projection, and constant or zero f are all accommodated by the separate reductions in the proof.
No step presumes factorality or excludes central atomic summands of the free product.
The parameters kappa_i may have either sign and may be large; only their finite maximum for the given finite family enters the norm bound.
No estimate uniform in degenerating trace parameters is asserted.

The result is limited to finitely many freely independent projections.
The finite alphabet, one-dimensional centered factors, exact cut formula, and full-state repeated-letter identities have all been used.
They have not been proved here for diffuse factors or multi-atom factors of higher centered dimension.
The result therefore does not by itself establish general free-product permanence of the closure equality.

**The complete candidate passes independent mathematical review without mathematical corrections.**
The two actual closure inclusions and the finite-rank characterization have complete dependency chains at the stated source acceptance levels.
Verification consists of the symbolic, norm, domain and selected source checks described above.
No numerical check, proof-assistant formalization, external human review, or novelty assessment is certified by this audit.
The reviewer did not edit the target.

## Coordinated verification-record correction, 2026-09-11

After the mathematical review, root required either preservation of the script underlying the author's reported finite integer checks or removal of those unaccompanied counts.
The author chose the latter and deleted exactly the single Section 9 paragraph beginning `An additional finite exact integer check in Python`.
No statement or argument in Sections 1-8 changed, and the remaining Section 9 text is unchanged.

The reviewer checked that the only change was removal of that paragraph and its following blank line.
The acceptance above applies to this revised artifact.
This is a correction to the verification record, with no mathematical gap or change in the proved scope.

## Actual review arrangement

The reviewer reconstructs the fixed projection proof and the disclosed RX06 passages.
The later exact deletion of the unretained-program integer-check paragraph changes only the verification account.
No shared target-proof repair is shown, but the original record does not establish initial isolation from the author-development or earlier target-review context.
The original 2026-09-11 date and all mathematical and source-inspection limits remain intact.
This maintenance performs no new review or isolated-context certification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Current isolated finding](#current-isolated-finding) | independently reviewed |
| [Original finding](#8-boundary-cases-and-final-acceptance) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Current isolated finding](#current-isolated-finding) | [C_F0105 statement](../../claims/Yin_C_F0105_v1.md#statement) | Whole nine-section finite free-projection proof: arbitrary traces including scalar endpoints, exact rank-two defects and residual columns, minimal full-state energy, homogeneous operator bounds, bounded resolvent and finite bounded scalar Schur inverses; excludes diffuse or general finite-dimensional-factor permanence. |
| [Current isolated finding](#current-isolated-finding) | [C_F0105 argument](../../claims/Yin_C_F0105_v1.md#2-alternating-words-and-bounded-end-deletion-operators) | Whole nine-section finite free-projection proof: arbitrary traces including scalar endpoints, exact rank-two defects and residual columns, minimal full-state energy, homogeneous operator bounds, bounded resolvent and finite bounded scalar Schur inverses; excludes diffuse or general finite-dimensional-factor permanence. |
| [Original finding](#8-boundary-cases-and-final-acceptance) | [C_F0105 statement](../../claims/Yin_C_F0105_v1.md#statement) | Whole nine-section finite free-projection proof: arbitrary traces including scalar endpoints, exact rank-two defects and residual columns, minimal full-state energy, homogeneous operator bounds, bounded resolvent and finite bounded scalar Schur inverses; excludes diffuse or general finite-dimensional-factor permanence. |
| [Original finding](#8-boundary-cases-and-final-acceptance) | [C_F0105 argument](../../claims/Yin_C_F0105_v1.md#2-alternating-words-and-bounded-end-deletion-operators) | Whole nine-section finite free-projection proof: arbitrary traces including scalar endpoints, exact rank-two defects and residual columns, minimal full-state energy, homogeneous operator bounds, bounded resolvent and finite bounded scalar Schur inverses; excludes diffuse or general finite-dimensional-factor permanence. |

