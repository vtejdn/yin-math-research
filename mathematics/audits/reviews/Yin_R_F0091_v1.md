---
author: Yin
---

<a id="original-normal-curve-account"></a>

# Independent Review of Yin_C_F0090

The complete original account is retained at its original date, exact mathematical scope, accepted source depth and unknown historical context relationship.
The new findings below record a later isolated inspection and do not backfill the old context or date.

Date: 2026-09-11.
Reviewer: the reviewing agent.
The author of Yin_C_F0090 and its proof is root.
The reviewer neither proposed nor wrote that proof.
The reviewer did author the earlier Yin_C_F0087 commutative fraction calculation, which is an explicit input; this review does not serve as independent review of Yin_C_F0087.

Target: [Yin_C_F0090-P1](../../claims/Yin_C_F0090_v1.md#yin_c_f0090-p1), for [Yin_T_F0003](../../tasks/Yin_T_F0003_v1.md#yin_t_f0003) and [Yin_S_F0013](../../strategies/Yin_S_F0013.md#s_f0013).
Starting assessment: complete proof draft, self-checked, awaiting independent review.
Scope: the entire Yin_C_F0090 statement, proof, dependency use and stated limitations.

**Outcome:** Yin_C_F0090-P1 is mathematically complete under its exact assumptions and the checked external inputs.
No correction was required.
The proposed assessment is `proved; independently reviewed`.
This establishes a commutative sufficient condition and does not complete the broader noncommutative Yin_T_F0003.

## Artifacts and External Inputs

- Yin_C_F0090 statement and complete proof (original material now separated into [Yin_C_F0090_v1](../../claims/Yin_C_F0090_v1.md), [Yin_C_F0091_v1](../../claims/Yin_C_F0091_v1.md))
- [The26b local-valuation interface](../literature/The26b/Yin_U001.md#local-valuation-interface); the original 2026-09-11 statement, proof-inspection depth and unpinned-source limit are recorded below.
- Yin_C_F0087 fraction calculation and Yin_C_F0088 comparison (original material now separated into [Yin_C_F0087_v1](../../claims/Yin_C_F0087_v1.md), [Yin_C_F0088_v1](../../claims/Yin_C_F0088_v1.md), [Yin_C_F0089_v1](../../claims/Yin_C_F0089_v1.md), [Yin_L_F0020_v1](../../ledger/Yin_L_F0020_v1.md))

After completing this Yin_C_F0090 review, root allocated Yin_C_F0091 and asked the reviewer to append its separately authored two-dimensional counterexample to the same ledger file.
The previously reviewed Yin_C_F0090 text was retained unchanged.
Yin_C_F0091 is excluded from this independent review; its author cannot supply its independent review.

The reviewer independently reopened the three primary The26b pages on the review date.
Their current statement numbers and interfaces agree with the local source record:

- [Tag 034X, Lemma 10.120.17](https://stacks.math.columbia.edu/tag/034X) gives the discrete valuation local rings at **nonzero** maximal ideals of the assumed Noetherian normal domain of dimension at most one.
  Its field exception is relevant and is preserved in the proof.
- [Tag 00PD, Lemma 10.119.7](https://stacks.math.columbia.edu/tag/00PD) gives unit-times-uniformizer factorization in the local ring and extends the valuation to its fraction field.
  Hence an element outside the local ring has the asserted expression (u\pi^{-k}), with (k\ge1).
- [Tag 00GY, Lemma 10.37.5](https://stacks.math.columbia.edu/tag/00GY) preserves normality on localization.
  The present multiplicative sets are complements of prime ideals and exclude zero.

These are accepted established inputs at the statement and applicability scope.
The source's arguments establishing the valuation factorization and localization identity were read; the underlying dimension-theoretic and Krull-Akizuki inputs were not recursively audited.
The continuously updated source is identified by stable tags, without claiming a pinned whole-project revision.

## Obligations and Decisive Checks

| Obligation | Decisive reasoning | Finding |
| --- | --- | --- |
| Faithful passage from continuous to measurable functions | A nonzero continuous function is bounded away from zero on a nonempty open set. Full support makes that set have positive measure, so the function is nonzero in (L^\infty(K,\mu)). | Valid for the stated compact Hausdorff space and full-support measure. |
| Obtaining one admissible affiliated fraction | In a commutative algebra, products of admissible denominators are admissible; sums and products of fractions remain fractions. If (pq^{-1}) is invertible in the ambient commutative algebra, then (p) is invertible there and its inverse fraction is (qp^{-1}). This is the exact fraction calculation used from Yin_C_F0087. | Valid, even though some other nonzero elements of (A) may have positive-measure zero sets. |
| Local ring at a support point | Evaluation (A\to\mathbb C) is surjective because (A) contains the complex constants, so its kernel is maximal. If that kernel is zero, (a-a(x)1=0) for every (a\in A), which settles the scalar case. Otherwise tag 034X applies. | Valid; no finite-generation or point-separation hypothesis is hidden here. |
| Interpreting a local unit and uniformizer | A fraction with denominator outside the evaluation ideal is continuous on a neighborhood of the point. A unit has nonzero value there; a uniformizer lies in the maximal ideal and vanishes there. These are local continuous functions, without a claim that their denominators have global measurable inverses. | Valid. |
| Excluding negative valuation using an essential bound | If (r=u\pi^{-k}), choose (L>\|f\|_\infty) and a neighborhood with (|u|>c), (|\pi|^k<c/L). On its intersection with the original set ({q\ne0}), the cleared algebraic identity forces both (pi\ne0) and (|p/q|>L). | Valid; the original (q), and only that denominator, is known to be nonzero almost everywhere. |
| Positive measure of the contradictory set | The neighborhood has positive measure by full support. Removing the null zero set of the original (q) preserves its measure. | Valid for atomic as well as nonatomic measures, including isolated points. |
| Local membership gives a finite denominator cover | Membership (r\in A_{\mathfrak m_x}) supplies (p_x,q_x\in A) with (q_x(x)\ne0) and (p_x=q_xr) in the abstract fraction field. Compactness selects finitely many open sets ({q_x\ne0}) covering (K). | Valid; no assumption that the individual (q_x) are admissible global inverses. |
| One globally invertible denominator | Star closure places (Q=\sum q_j^*q_j) and (v=\sum q_j^*p_j) in (A). The covering property makes (Q>0) everywhere; compactness gives a positive minimum. Thus (Q^{-1}\in\mathcal M). | Valid; this is where the adjoint-closed hypothesis is used. |
| Matching the local fractions with the original measurable element | The abstract identities (p_jq=q_jp) hold in (A). Multiplying by the original admissible (q^{-1}) gives (p_j=q_jf), without inverting any (q_j). Summing gives (Qf=v). | Valid; it avoids embedding all of (\operatorname{Frac}(A)) into (L^0(\mathcal M)). |
| Reverse inclusion and continuous representative | A bounded inverse remains its inverse in the affiliated algebra. Conversely the constructed (vQ^{-1}) is continuous and is in the bounded scalar division closure. | Valid for the exact equality and the stronger representation conclusion. |

The proof was checked in the order needed to avoid a denominator circularity.
The abstract fraction (r) is used for local valuations, and only identities cleared inside (A) are passed to the affiliated algebra.
The proof does not first assume that every nonzero continuous element is regular as a measurable operator.
In particular, ring-theoretic lack of zero divisors is not confused with the absence of positive-measure zero sets.

The assumption that (A) is globally Noetherian, normal and of dimension at most one is a sufficient way to obtain the local discrete valuation rings.
The proof itself only uses that condition at the evaluation ideals, together with the explicitly handled zero-ideal case.
No stronger general statement is registered by this audit.

## Scope and Verification Limits

This is a scalar commutative result for an adjoint-closed evaluated algebra.
It does not alter an unstarred coordinate algebra, assert stability under free products, or settle the corresponding noncommutative free-field question.
The use of ring normality is distinct from normality of represented operators.
Yin_C_F0088's cusp serves as a comparison and is not a logical premise of Yin_C_F0090.

The mathematical proof and its cited source interfaces were checked.
No mathematical computation, compilation, formalization, external human review, or novelty assessment was performed or needed for this review.
A whole-repository link check is maintained by the coordinating agent; it is document verification and does not provide evidence for the theorem.

The reviewed proof and shared indexes were not edited by this reviewer.
The responsible Claim material and its selected decision own promotion of the exact artifact above to `proved; independently reviewed`, with this record as review evidence.
Later substantive generalizations require their own review.

## Actual review arrangement

The reviewer neither proposed nor wrote C_F0090.
Its earlier authorship of C_F0087 is an explicit dependency relationship, not authorship of this target proof; C_F0091 is explicitly excluded from this finding.
The account does not establish initial isolation from author-development discussion or earlier-review summaries.
Its actual original full mathematical checks, original day precision and disclosed source limits remain intact; initial context isolation is unknown.
This maintenance performs no new or redated review.

<a id="isolated-local-valuation-finding"></a>
## New isolated inspection of the complete local-valuation theorem

Initial finding formed 2026-10-22T22:30; recorded after comparison 2026-10-22T22:37, in UTC, for human record author Yin.
A separate agent outside proof development received only fixed targets, scope, rules and necessary input locations, without development discussion, mathematical summaries or old target conclusions.
It read all of C_F0090's mathematical statement and proof and the exact C_F0087 fraction, MSY23 closure and The26b local-valuation interfaces.
All six assigned initial findings were complete before any of their old R accounts or current assessment/review-scope sections were read.

**PASS for the complete fixed theorem, including the continuous positive-denominator representation.**
Full support makes continuous-function evaluation faithful, while the commutative fraction calculation supplies one globally admissible denominator q.
Other nonzero functions are not thereby declared regular in the affiliated algebra.
Evaluation has a maximal kernel because constants are present; zero kernel forces the scalar algebra and settles that exception.
For a nonzero evaluation ideal the accepted Noetherian normal dimension-one localization theorem supplies a DVR.
A negative valuation gives a local unit u times a negative power of a uniformizer pi, with locally continuous denominator representatives, u nonzero and pi zero at the support point.
Shrinking the neighborhood makes the fraction exceed any prescribed essential bound wherever the original q is nonzero.
Full support and removal of only that null zero set give the contradiction, including atoms and isolated points.

Thus every evaluation localization contains the abstract fraction.
Compactness gives finitely many local denominators q_j with no common zero.
Star closure puts Q=sum q_j* q_j and v=sum q_j* p_j in A; positivity and compactness make Q boundedly invertible.
Clearing against the original admissible q gives p_j=q_j f without inverting any q_j, hence Qf=v.
This proves the bounded scalar-division inclusion and continuous representative; the reverse inclusion follows from compatibility of bounded inverses.
No embedding of the entire abstract fraction field, point separation, principal ideal condition or free-product stability is used.

The complete original account was compared after the initial findings.
Every obligation, field/atomic exception, source applicability and denominator limit agrees, with no remaining correction.
Its original 2026-09-11 source openings, the reviewer's C_F0087 dependency authorship and exclusion of the separately authored C_F0091 counterexample remain historical facts.
The new inspection uses the retained source interfaces, without claiming to reopen the continuously updated Stacks pages or audit their foundational proofs.
This is a scalar commutative sufficient condition and does not complete the broader noncommutative Task or establish novelty or formal verification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original whole-proof finding](#obligations-and-decisive-checks) | unknown |
| [New isolated local-valuation finding](#isolated-local-valuation-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original whole-proof finding](#obligations-and-decisive-checks) | [Exact statement](../../claims/Yin_C_F0090_v1.md#statement) | Whole C_F0090 local discrete-valuation and positive-denominator theorem, including source tags and all ring/measure/denominator limits. |
| [Original whole-proof finding](#obligations-and-decisive-checks) | [Exact argument](../../claims/Yin_C_F0090_v1.md#yin_c_f0090-p1) | Whole C_F0090 local discrete-valuation and positive-denominator theorem, including source tags and all ring/measure/denominator limits. |
| [New isolated local-valuation finding](#isolated-local-valuation-finding) | [Exact statement](../../claims/Yin_C_F0090_v1.md#statement) | Entire Noetherian normal domain, dimension-at-most-one and full-support-measure theorem, including the everywhere positive denominator and continuous representative. |
| [New isolated local-valuation finding](#isolated-local-valuation-finding) | [Complete P1](../../claims/Yin_C_F0090_v1.md#yin_c_f0090-p1) | Actual affiliated fraction, evaluation/localization field exception, negative-valuation essential-bound contradiction, finite denominator cover and positive star-closed patching; accepted source-proof limits retained. |
