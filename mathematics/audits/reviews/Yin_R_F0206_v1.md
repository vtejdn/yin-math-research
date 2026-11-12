---
author: Yin
---

# Sparse truncation and planar logarithmic instability: independent whole-proof review

<a id="truncation-stability-whole-proof"></a>
## Whole-proof finding

Review date: 2026-11-11T17:10.
The human record author is Yin.
The reviewed artifact is [C198v1](../../claims/Yin_C_F0198_v1.md#decision-truncation-stability-candidate), at its open candidate decision, including the exact [statement](../../claims/Yin_C_F0198_v1.md#statement) and the entire [argument](../../claims/Yin_C_F0198_v1.md#argument).

This is an independently organized initial whole-proof inspection by an agent outside substantive development of the candidate.
The reviewer received the fixed target, exact dependency locators, review scope and operational metadata, with no proof-development dialogue, mathematical summary, author explanation or prior review of C198 supplied or consulted.
The reviewer first enumerated the statement's obligations, checked the complete argument, and then checked the directly used dependency statements and their interfaces.
The accepted upstream results retain their own review and source boundaries; this finding does not purport to re-audit their entire supporting chains.

**Verdict: the complete candidate is mathematically supported at its stated scope.**
No blocking error or missing premise was found in the sparse truncation, summable fixed-norm guard, complete clipped transfer, or bounded-real-law polynomial instability.
The proof establishes neither unregularized truncation transfer nor the outstanding summable planar defect estimate, and it does not claim either conclusion.
The candidate's adoption remains a decision of C198; this review changes no Claim assessment.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#truncation-stability-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#truncation-stability-whole-proof) | [Candidate decision](../../claims/Yin_C_F0198_v1.md#decision-truncation-stability-candidate) | Exact candidate scope, selected statement, complete argument and declared direct dependencies. |
| [Whole-proof finding](#truncation-stability-whole-proof) | [Exact conclusions](../../claims/Yin_C_F0198_v1.md#statement) | All hypotheses, estimates, coupling and clipping quantifiers, real support construction, resampling interpretation and stated limits. |
| [Whole-proof finding](#truncation-stability-whole-proof) | [Complete argument](../../claims/Yin_C_F0198_v1.md#argument) | Entire sparse-count, expected-norm, concentration, centering, rank, cap, block, determinant, support, rarity and planar argument, including the final unresolved-transfer interface. |
| [Whole-proof finding](#truncation-stability-whole-proof) | [Hermitian rank stability](../../claims/Yin_C_F0186_v4.md#rank-stability) | R2 and R3 and their applicability to squared singular matrices; the elementary min-max and bounded-variation derivation was checked. |
| [Whole-proof finding](#truncation-stability-whole-proof) | [Adopted global clipping theorem](../../claims/Yin_C_F0186_v27.md#statement) | Item 1 and the global subpolynomial clipping definition, reused at their accepted scope after checking the original-law model and normalization. No new whole-chain review of C186v27 is asserted. |
| [Whole-proof finding](#truncation-stability-whole-proof) | [Bounded-product convex concentration](../../claims/Yin_C_F0187_v2.md#argument) | Inequality (9) only, as the accepted external concentration input for independent bounded real coordinates; no use of the intermediate-singular-value theorem. |
| [Whole-proof finding](#truncation-stability-whole-proof) | [Expected matrix norm](../literature/Lat05/Yin_U001.md#lat05-u001) | The accepted real independent-entry Theorem 2, including zero entries and nonidentical laws, and the strict-upper-array applicability boundary. |

## Decisive checks

### Sparse deletion and a fixed norm guard

The expected off-diagonal tail count is bounded by a constant times \(N^2R_N^{-4}=N^{4\delta}\), and the expected diagonal count by a constant times \(NR_N^{-2}=N^{2\delta}\).
Within-size independence permits the displayed exponential-moment estimate for the total altered-coordinate count.
With \(t=(\eta/2)\log N\), its positive error term is lower order than \(N^{4\delta+\eta}\log N\), giving the claimed summable bound.
Neither this step nor its first Borel--Cantelli consequence assumes cross-size independence.

For the norm estimate, the centered strict upper array has independent entries, row and column variance sums at most one, and total fourth moment bounded uniformly in \(N\).
Centering a truncated coordinate changes its fourth moment by at most a universal factor, so the accepted Latała theorem applies to this array.
The passage to a symmetric matrix uses the triangle inequality and does not treat reflected entries as independent.
The raw truncated mean satisfies \(|m_N|\le R_N^{-3}\mathbb E|\xi|^4\), whence its symmetric normalized matrix contribution is at most \(C N^{-1+3\delta}\).
This is bounded under \(\delta<1/4\), and the diagonal contributes at most \(N^{-\delta}\) deterministically.
Thus the expectation bound does not need a fourth diagonal moment or recentering of the actual truncated matrix.

The operator norm is convex and \(\sqrt2\)-Lipschitz in the independent normalized upper coordinates, whose support diameters are at most \(2N^{-\delta}\).
Rescaling inequality (9) therefore gives the stated \(\exp(-ct^2N^{2\delta})\) concentration.
A median at most twice the uniform expected-norm bound supplies a common fixed guard for both colors.
All constants may depend on the fixed laws and chosen exponents, as permitted by the statement.

### Complete clipped comparison and the triangular-array limit

The four-term telescoping identity is exact and gives output rank at most \(4M_N\).
The raw-coordinate cap \(N^2\), finite second moments and a union bound give an exceptional probability \(O(N^{-2})\).
On that cap the input norms are at most \(N^{5/2}\), and both output singular spectra on any fixed compact parameter set lie below \(N^6\) eventually.
The cutoff dimension may depend on that compact set, without changing the exceptional-event constants.

Passing to the squared-singular Gram matrices at most doubles the perturbation rank.
The capped test function has total variation exactly \(L_N+6\log N\), giving the stated coefficient \(8N^{4\delta+\eta-1}(L_N+6\log N)\).
Its convergence to zero follows from \(4\delta+\eta<1\) and \(L_N=N^{o(1)}\).
The two displayed exceptional series prove complete convergence for every fixed compact set and positive threshold.
An intersection over integer disks and rational thresholds yields locally uniform almost-sure comparison for each specified deterministic height sequence under any cross-size coupling.

The original real fourth-moment model satisfies C186v27's third off-diagonal and second diagonal moment assumptions, with the same squared-singular normalization and global clipping height.
Its item 1 therefore applies to the original potentials \(V_N\).
Adding the proved locally uniform comparison transfers their local planar \(L^1\) limit to \(\widetilde V_N\).
This invokes C186v27 on the fixed original laws only; it does not assert that the generally noncentered truncated triangular array satisfies that theorem's model directly.

### Exact real-polynomial instability and probability scope

The Sylvester recursion gives a real orthogonal matrix with the required flat entries.
With the candidate's \(C_n\) and \(G_n\), block multiplication yields \(C_n+2C_n^T=J_n\) and the two stated output blocks.
The sum of the absolute coefficients in every row of \(C_n^T\) is at most one, giving the raw-entry support bound, while \(\|C_n\|\le1\) gives the input norm guard.

The specified reflected one-coordinate change has input operator norm exactly \(h\).
Its two output blocks are \(T'_n\) and an orthogonal conjugate of \((T'_n)^T\), so they have the same eigenvalues and norm.
Expansion along the last row of \(T'_n\) leaves the identity with its first row altered, and its surviving first diagonal entry is \(1+2hf_2\).
Consequently \(|\det T'_n|=|hf_n(1+2hf_2)|\asymp N^{-1}\), with no cancellation or zero determinant.
Together with \(\|T'_n\|\le1+3h\), the arithmetic-geometric mean estimate forces the normalized eigenvalue-square statistic to tend to one, while it vanishes for the nilpotent original output.
The output perturbation has rank at most four and operator norm at most \(3h\), which tends to zero.

The raw entry bounds satisfy \(\sqrt2+1/4<\sqrt3\), so both configurations are interior support points of one fixed uniform off-diagonal law with zero diagonals.
For each size, continuity of the unordered eigenvalue multiset makes the required strict statistic jump persist in product neighborhoods.
The common coordinates and the original and fresh replaced coordinate can all lie in their respective neighborhoods with positive probability.
The same reasoning handles a full independent row-block replacement by restricting its remaining fresh coordinates near their original targets.
Continuity of input norms also keeps these witnesses on one fixed norm guard.

The \(2n(n-1)\) original strict upper coordinates inside the diagonal blocks of the two colors are independent and have zero targets.
Restricting their raw absolute values below \(1/2\) leaves suitable witness neighborhoods of positive probability and bounds their probability above by \((2\sqrt3)^{-2n(n-1)}\).
This proves the stated rarity possibility, without supplying a useful lower bound on a typical influence event.
The failure of a vanishing essential-supremum bound is therefore justified, while no nonsummability or Brown-convergence counterexample follows.

### Planar logarithmic comparison and remaining obligations

The circle-mean computation gives the displayed disk integral for every eigenvalue in the radius-\(R\) disk.
Both constructed spectra lie there for \(R>2\), so the statistic jump yields the signed planar potential integral tending to \(\pi/2\).
Its absolute value lower-bounds the planar \(L^1\) distance.
The bounded output norms and rank-four perturbation give a uniform clipped difference of order \((L_N+1)/N\), which tends to zero at every admitted height.
Since \(D_N-D'_N=(V_N-V'_N)+(u'_N-u_N)\) almost everywhere, the asserted positive sign and limit for the defect integral are correct.
Finite exceptional eigenvalue sets do not change these planar integrals.

The example rules out an unregularized transfer deduced solely from the listed generic perturbation properties.
It is not the literal hard-threshold pair, and the argument does not treat it as one.
The final sufficient complete-convergence condition on \(u_N-\widetilde u_N\) is correctly identified as an additional unproved probabilistic input, alongside a suitable negative-logarithm result for the truncated triangular array.

## Dependency reuse and verification limits

The [Lat05 source unit](../literature/Lat05/Yin_U001.md#lat05-u001) was read for the published Theorem 2 statement and its exact independent-entry applicability.
The [GNT14 source account](../literature/GNT14/readme.md) and C187v2 inequality (9) were read for the accepted bounded-product concentration statement, edition and inspection limits.
This review reuses those accepted primary-source inspections; it does not claim a new reading of the original PDFs or an audit of Latała's underlying Gaussian theorem or the original concentration proof.
The directly relevant [C186v27 clipping argument](../../claims/Yin_C_F0186_v27.md#stretched-clipped-potential) was also read to verify the scope of the reused conclusion; its other defect, geometry and guard-obstruction conclusions are not premises here.

All algebraic identities, probability exponents, norm and rank constants, limit passages, support neighborhoods and planar signs in C198 were checked mathematically.
No numerical experiment or proof-assistant verification is claimed or needed for this exact proof.
The comparison links to L58v1 and L67v1 were not used as premises, and no rolling draft was consulted.
No substantive correction to the reviewed candidate is required by this finding.
