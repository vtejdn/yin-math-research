---
author: Yin
---

# Independent review of two-sided physical incompressibility

The review act was completed at 2026-11-11T13:38 UTC for human record author Yin.
This is an independent whole-argument inspection of [C0196 v1](../../claims/Yin_C_F0196_v1.md#statement), including its spread and physical-companion consequences.
The reviewer was outside substantive proof development and received the fixed candidate, the review scope, applicable rules and operational authorization metadata, without proof-generation discussion, an author mathematical summary or an expected verdict.
Initial findings were formed from the candidate before any other assessment was consulted.
No other review of this candidate was read or relied upon.
The reviewer reported a count-event wording defect and a missing method-attribution locator to the authoring agent, then independently inspected the actual corrected passages and the affected logical implication.
The reviewer did not edit the Claim or supply a substantive repair.

The reviewed input is the current 2026-11-11 C0196 v1 text with the explicit Chernoff count-good event and Rudelson--Vershynin Lemma 3.5 attribution.
Its selected assessment when inspected was the open [candidate decision](../../claims/Yin_C_F0196_v1.md#decision-incompressibility-candidate).
This R supplies review evidence; it does not itself select a new C assessment or complete F0012.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole candidate finding](#whole-candidate-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole candidate finding](#whole-candidate-finding) | [Exact statement](../../claims/Yin_C_F0196_v1.md#statement) | All stated hypotheses, norm-guarded exponential exclusion, constant dependencies, simultaneous bounded shifts and the explicitly included spread and distance-average consequences. |
| [Whole candidate finding](#whole-candidate-finding) | [Complete argument](../../claims/Yin_C_F0196_v1.md#argument) | Entire complex fourth-moment argument, both lawful exposures, entropy and approximation steps, root spread, companion reduction, physical projection and probability averaging, with the actual corrected Chernoff explanation. |
| [Whole candidate finding](#whole-candidate-finding) | [Method attribution](../../claims/Yin_C_F0196_v1.md#source-comparison) | Checked the cited Rudelson--Vershynin edition and passages, including Lemma 3.5, as method attribution rather than an invoked independent-entry theorem for the product. |

## Mathematical checks

The exact statement requires a common event for every complex compressible unit vector and every shift in a fixed disk, with constants independent of dimension and diagonal law.
It only estimates the intersection with the fixed operator-norm guard.
The argument meets this scope without using cross-size independence or a bound on the probability of the guard's complement.

The centered complex fourth-moment expansion is valid without independence of real and imaginary parts.
Singleton indices vanish, the paired terms are controlled by second absolute moments and the bound on the nonconjugated second moment, and the all-equal terms use the fourth-moment bound.
The independent-copy argument gives a uniform disk concentration bound because the probability that two copies lie in the same disk is the square of the disk probability, while their difference has a fixed positive probability of exceeding the stated radius.
This remains uniform for mixtures of the original entry laws and their conjugates.

For the row tensorization, independent Bernoulli indicators with individual means at least \(p\) have a lower-tail bound at threshold \(pq/2\) of at most \(e^{-pq/8}\).
Since \(q\ge N/5\), the stated constants \(c_0^2=p/160\) and \(c_1=p/40\) are valid.
The corrected text uses the count-good event to imply the norm lower bound, rather than asserting the converse from a lower norm bound.
The affine centers are arbitrary fixed complex numbers, which is sufficient after the second exposure.

The first rectangle uses only off-diagonal coordinates corresponding to distinct unordered pairs between disjoint sets.
Its entries are independent even when their orientation changes which conjugated law is used.
The deterministic complex nets have real dimension \(2s\), and their stated cardinality and the support count have entropy tending to zero per dimension as \(\delta\) decreases.
The first approximation uses only \(\|B\|\le K\), with \(K\eta\le c_0/2\).
The event \(\mathcal B_N\) is measurable with respect to \(B\), which matters for the subsequent conditioning.

In the second exposure, fixing all original coordinates of \(A\) except the unordered \(I\)-\(J\) pairs leaves independent entries in \(A_{I,J}\).
The mirrored \(A_{J,I}\) entries are not separately exposed or used as independent variables.
The support of the test vector is disjoint from both sets, so \(Av\) is fixed under this conditioning and hence all of \(2BAv\) is fixed.
Within the retained \(I\) coordinates, the only remaining random part of \(ABv\) is exactly \(A_{I,J}(Bv)_J\).
The coefficient norm is at least \(\beta\) on the already fixed \(\mathcal B_N\), allowing the affine bound and its integration without conditioning the fresh law on \(\Omega_{N,K}\).

The second net loss satisfies \(3K^2\eta\le c_0^2/4\), leaving the claimed \(\gamma=c_0^2/4\) after the net lower bound \(c_0\beta=c_0^2/2\).
The two support-and-net unions cost at most the stated combined \(2e^{-c_1N/2}\) exception.
Sparse vectors have zero coordinates on the selected output set, so subtracting any scalar shift changes none of those coordinates.
This establishes the all-shifts sparse bound without a shift net.
The operator estimate \(\|P-zI\|\le3K^2+Z\) then gives the strict separation from \(a=\gamma/2\) throughout the stated compressible neighborhood, including its boundary.

The root-spread derivation uses the normalized truncation onto the largest \(s\) coordinates.
Its squared approximation distance is \(2(1-\|u_H\|)\le2\|u_{H^c}\|^2\), so incompressibility forces the required tail mass.
For sufficiently large \(N\), the rounding in \(s=\lfloor\delta N\rfloor\) gives the stated upper coordinate threshold.
Removing the coordinates below the lower threshold and comparing the remaining mass with that upper threshold yields \(p_*N\) indices with the claimed \(p_*=\delta\rho^2/8\).

The three companion residual equations have the displayed signs and reconstruct \((AB+2BA-zI)u\) exactly.
The bounds \(\|u\|\ge c_u\) and \(\|(P-zI)u\|\le(1+3K)\varepsilon\) follow on the same norm guard.
Consequently the chosen \(\varepsilon_*\) permits application of the root-spread result to \(u/\|u\|\), and every selected physical block has the required norm at least \(c_*/\sqrt N\).
The statements are simultaneous in the near-kernel vector and bounded shift because the preceding good event was simultaneous.

For each physical block, projection kills all other columns regardless of dependencies among those columns.
The definition of \(d_i\) therefore gives the stated pointwise bound on every selected block.
A least right singular vector exists in this finite-dimensional square problem, also at \(\varepsilon=0\).
Counting at least \(p_*N\) selected indices on the good event and taking expectations yields the exact fixed-shift distance average, with the guard retained on every summand.
Neither independence among distance events nor a measurable selection of a singular vector is needed for that pointwise event inclusion.

## Attribution and dependency scope

I inspected Rudelson--Vershynin's [arXiv:math/0703503v2](https://arxiv.org/pdf/math/0703503v2), Proposition 2.5 and Lemma 2.6 on PDF pp. 11--12, Lemmas 3.3--3.4 on PDF pp. 15--16, and Lemma 3.5 on PDF pp. 16--17, including their displayed proofs.
The cited passages support the norm-restricted rectangular-net method, compressibility/spread mechanism and scalar distance-average attribution.
The candidate's own proofs supply the complex affine estimate, lawful product exposures and physical-block companion application; no independent-entry invertibility theorem is applied directly to the dependent product.
This source inspection is confined to those methods and passages, without a review of the paper's full theorem chain or a novelty judgment.

The [L0066 v19 companion setup](../../ledger/Yin_L_F0066_v19.md#two-sided-quartic-physical-setup) agrees with the companion used here.
Its [unresolved quartic interface](../../ledger/Yin_L_F0066_v19.md#two-sided-quartic-first-obligation) supplies continuation context, not a premise needed by the present proof.
I inspected those two passages only and did not re-audit the complete quartic calculation or its rank examples.
The positive-frame result cited in C0196 is explicitly a comparison and is not used as a logical dependency.
The present proof is self-contained apart from elementary fourth-moment, concentration and net facts checked at their actual uses above.

<a id="whole-candidate-finding"></a>
## Outcome and limits

No unresolved mathematical gap remains in the reviewed norm-guarded compressible exclusion, simultaneous root and companion spread, or fixed-shift physical distance-average inequality.
The author-corrected count-event implication and supplemented method attribution have both been directly rechecked.
The constants have the stated dependencies, and arbitrary diagonal distributions cause no additional premise because all fresh coordinates used are off-diagonal and diagonal effects remain inside the affine centers or the fixed norm guard.

This finding does not bound the averaged distance probabilities or remove the norm guard.
The conditional polynomial-decay continuation remark is valid only when the matching estimate controls the actual averaged interface, including its background and denominator, and the separate guard-complement requirement is met when an unguarded conclusion is desired.
The proof gives no almost-sure conclusion, summable guard estimate, finite-second-moment replacement for the fourth off-diagonal moment hypothesis, least-value floor, or Brown-measure theorem.
No Task-completion review, numerical experiment or formal proof verification is claimed.
