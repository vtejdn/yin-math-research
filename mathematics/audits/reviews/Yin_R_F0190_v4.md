---
author: Yin
---

# Finite-variance Wigner polynomial controls and cyclic Brown-measure subclasses

## Review arrangement and exact inputs

Review act: 2026-11-05T00:43.
Human record author: Yin.
This is a separately organized independent whole-proof inspection of [C_F0186_v4](../../claims/Yin_C_F0186_v4.md#statement), with its scope compared against [T_F0012_v3](../../tasks/Yin_T_F0012_v3.md#contract).
The reviewer did not participate in substantive development of this candidate and received its fixed statement, proof, requested scope and current rules.
No development drafts, proof-generation discussion, sibling-agent findings or earlier formal R findings were supplied or consulted.
A targeted locator search displayed older GUE assessment prose; it was not used as evidence for the finite-variance candidate.
Necessary mathematical interfaces in C_F0186_v1 and C_F0186_v3 and the candidate's retained source units were read directly.
The older GUE conclusions and their assessments supply no finite-variance proof premise here.

The review reads the six assertions actually made in C_F0186_v4.
Its fifth assertion is an equivalence with an unproved defect condition, and its sixth assertion is an unconditional cyclic subclass.
It does not assert or review a proof of the general nonnormal Task.
The separate C_F0187 family is not a premise of this inspection.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finite-variance whole-proof finding](#finite-variance-controls) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finite-variance whole-proof finding](#finite-variance-controls) | [Exact candidate statement](../../claims/Yin_C_F0186_v4.md#statement) | All six partial or conditional conclusions, including complex entries, finite second moments and arbitrary cross-size coupling. |
| [Finite-variance whole-proof finding](#finite-variance-controls) | [Complete candidate argument](../../claims/Yin_C_F0186_v4.md#argument) | Rank truncation, concentration, logarithmic and small-power controls, both directions of the planar defect equivalence, and cyclic FK reduction. |
| [Finite-variance whole-proof finding](#finite-variance-controls) | [Broadened Task contract](../../tasks/Yin_T_F0012_v3.md#contract) | Exact quantifier and scope comparison; the general Task is not completed by this candidate. |
| [Finite-variance whole-proof finding](#finite-variance-controls) | [Retained singular-value inequality](../../claims/Yin_C_F0186_v3.md#singular-value-perturbation) | Complete elementary Frobenius perturbation proof and its scalar-shift Lipschitz consequence; no Gaussian conclusion is imported. |
| [Finite-variance whole-proof finding](#finite-variance-controls) | [Bounded FK input](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) | Applicability of bounded multiplicativity, including zero determinants, to the finite tracial algebra and its normalized two-by-two amplification. |

<a id="finite-variance-controls"></a>
## Finding

All six stated conclusions are supported by the complete argument at the accepted external-theorem boundary described below.
No substantive mathematical gap was found.
The result supplies partial progress on T_F0012_v3, together with an exact characterization of the remaining planar logarithmic defect and an unconditional nonnormal subclass.
It does not justify a completed decision for the broader Task.

### Fixed laws, complex entries and the spectral limit

The expected bounded-entry word expansion has the correct normalization \(N^{-1-k/2}\).
For a nonvanishing equality pattern, every colored unoriented edge occurs at least twice, and the connected graph satisfies \(v\le e+1\le k/2+1\).
Equality forces a loop-free tree in which every edge occurs twice.
A closed walk on that tree uses each edge once in each orientation, so its complex contribution is \(\mathbb E|\xi_{j,R}|^2\), with no assumption on \(\mathbb E\xi_{j,R}^2\) or independence of real and imaginary parts.
A diagonal loop cannot occur in a leading graph, so a different bounded diagonal variance is harmless.
The resulting colored noncrossing pairings also give the claimed matrix-coefficient version.

The fixed-law assumption is used exactly where it is needed: the centered entry-tail second moments tend to zero as the fixed cutoff \(R\) increases.
In (T1), the difference entry is the centered discarded tail.
Its variance is bounded by its discarded second moment, and the diagonal contribution has the extra \(1/N\) normalization.
The spectral split (T2) therefore has expected normalized rank at most \(e_R/\eta^2\).

The comparison chain in (T4) uses low rank only for Hermitian polynomial outputs.
Clipping \(W_R\) spectrally at \(M>2\) removes asymptotically negligible expected rank because every truncated limiting semicircle has radius at most two.
The middle comparison has bounded inputs and a norm error of order \(\eta\).
Taking \(R\to\infty\) before \(\eta\downarrow0\) gives the desired resolvent limit; the Stieltjes continuity step has a probability measure as its limiting law.
This proves expected weak convergence without invoking nonexistent higher untruncated moments or an almost-sure norm bound.

For each \(N\), upper-triangular row blocks are independent under the exact contract.
Changing one block changes one Hermitian input by rank at most two, including its diagonal entry.
Polynomial telescoping and min-max therefore give a change of order \(\operatorname{Var}(f)/N\) in the normalized spectral statistic.
There are \(dN\) blocks, so the bounded-differences denominator is of order \(\operatorname{Var}(f)^2/N\).
The resulting exponential tails are summable.
The countable resolvent argument uses only first Borel--Cantelli, so no independence across sizes enters the almost-sure limit.

### Singular tails, clipping and logarithmic concentration

The product and sum singular-value counting inequalities follow from the stated subspace intersections.
For a product, the inverse image of a subspace has codimension no greater than that subspace's codimension, even when the intervening product is singular.
For a word of length at most \(D\), choosing input thresholds of order \(R^{1/D}\) and adjusting fixed constants gives (Tail).
Only the expected normalized input Hilbert--Schmidt square is used.
The same estimate remains valid for raw truncation because it reduces entry moduli.

Clipping raw entries at modulus \(N^2\) has disagreement probability at most a constant times \(N^{-2}\): there are order \(N^2\) entries, each with a second-moment tail bound of order \(N^{-4}\).
Thus equality with the original tuple eventually holds on one probability-one event under every allowed coupling.
The deterministic clipped operator-norm bound \(N^{5/2}\) and polynomial bound \(C_PN^{5D/2}\) have the correct powers.

For a fixed nondecreasing continuous logarithmic-growth test, clipping reduces its relevant variation to order \(1+\log^r N\).
Bounded differences then gives the summable exponent \(N/(1+\log^{2r}N)\).
The expected clipped weak limit is unchanged, and (Tail) supplies the necessary expectation uniform integrability.
This proves (Log-AS), including each fixed positive logarithmic power.
For (Pos-AS), choosing \(R\) so that \(\sqrt R\) exceeds the free squared-singular support makes the limiting integral of \(h_R\) zero, while \(\log x\le2h_R(x)\) for \(x>R\).

The small-power argument has the correct separate exponent.
The variation of \(x^{p/2}\) on the squared-singular spectral interval is at most \(C_PN^{5Dp/2}\), producing \(N^{1-5Dp}\) in (Small-p-conc).
It is summable for every fixed \(0<p<1/(5D)\).
A fixed \(q\) with \(p<q<2/D\) supplies expectation uniform integrability.
This establishes the stated small moment range and does not assert convergence of unrestricted trace moments.

### Regularized potentials and their slow diagonal

For fixed \(\delta>0\), the lower bound for \(\tfrac12\log(x+\delta^2)\) removes the negative-tail problem, while (Tail) controls every positive logarithmic power.
Jensen's inequality therefore gives moments of order greater than any requested finite \(p\), which justify the claimed \(L^p\) convergence.

The retained singular-value proof was checked directly.
Its row and column sub-stochastic bounds and layer-cake finite sums give
\(\sum_i(s_i(A)-s_i(B))^2\le\|A-B\|_{\mathrm{HS}}^2\).
For \(A-zI\) and \(A-wI\), the normalization cancels \(\sqrt N\), and the derivative bound \(1/(2\delta)\) gives exactly the stated planar Lipschitz constant.
The common bound extends convergence on a countable dense set to local uniform convergence.

For \(N^{-a}\le\delta_N\le1\), the clipped logarithm has variation \(O(\log N)\), uniformly on each fixed planar disk.
A net with spacing a fixed small multiple of \(N^{-a}\) has polynomial cardinality, which is dominated by the summable concentration exponent.
Using a countable sequence of error tolerances gives local uniform concentration around clipped expectations.
In the diagonal construction, \(N\ge N_k\ge k^{1/a}\) implies \(1/k\ge N^{-a}\), so the same concentration applies to the piecewise constant choice.
The uniform fixed-regularizer expectation limit and the monotone local \(L^1\) limit \(u_{\delta_k}\downarrow u\) prove (Slow-reg).
No estimate for \(u_{N,\delta_N}-u_N\) follows from this construction, and the candidate correctly makes none.

### Eigenvalue control and both directions of the defect equivalence

The Cauchy--Binet expansion after Schur triangularization contains every squared principal minor.
These terms sum to the left side of (CB), so the displayed inequality has the correct direction.
Tonelli applied to the nonnegative logarithms gives (Eig-log).
The lower bound \(F(x)\ge2(\log x)^2\) for \(x\ge1\), and the logarithmic-growth upper bound, establish (Log2) from (Log-AS).
The positive-power variant follows from the stated integrable scalar kernel for \(0<p<2\).

The local squared logarithmic kernel is uniformly integrable over bounded translation sets, and for distant translations it grows at most quadratically in \(\log^+|\lambda|\).
Jensen and (Log2) therefore prove the eventual pathwise \(L^2\) bound for \(u_N\).
The expectation version follows from (Tail) through (Eig-log).
These estimates concern averaged eigenvalue potentials and do not supply the missing individual small-singular-value logarithmic control.

For sufficiency of (Defect), positivity of the defect gives the triangle estimate between \(u_N\), \(u_{N,\delta}\), \(u_\delta\) and \(u\) in local planar \(L^1\).
First sending \(N\to\infty\) and then \(\delta\downarrow0\) yields \(u_N\to u\).
The distributional Laplacian identity and the already proved tightness yield weak convergence of probability measures on the same event, hence convergence against every bounded continuous real test function.

For necessity, weak eigenvalue-measure convergence gives convergence of the bounded cutoff kernel for each \(z\).
Its uniform bound on a fixed planar disk justifies dominated convergence in \(z\).
The far-eigenvalue contribution is uniformly \(O(1/\log R)\) by (Log2).
The negative-kernel truncation error is uniformly
\[
 2\pi\int_0^{e^{-M}}r\log(e^{-M}/r)\,dr
 =\frac{\pi}{2}e^{-2M},
\]
independently of the probability measure in the eigenvalue variable.
These two errors justify local \(L^1\) convergence of the unregularized potentials from weak convergence in precisely this controlled class.
Fixed-regularizer convergence then identifies each limiting defect with \(\int_K(u_{\delta_k}-u)\), which decreases to zero.
Thus the converse does not rely on the false unrestricted implication from weak measure convergence to untruncated logarithmic-potential convergence.

Integer-radius disks and a countable decreasing regularizer sequence suffice for the equivalence.
The alternative sufficient pointwise logarithmic uniform-integrability hypothesis is also correctly qualified.
Tonelli excludes positive-probability finite-size singularity for almost every deterministic \(z\), Fubini assembles the pointwise almost-sure limits, and the local \(L^2\) bounds give local \(L^1\) convergence.
Neither that extra hypothesis nor (Defect) has been proved for arbitrary \(P\).

### Cyclic subclasses and polynomial pushforwards

For \(P=AC^*C\), set \(U=AC^*\) and \(V=C\).
The finite identity compares \(UV\) with \(VU=CAC^*\), which is selfadjoint.
The Schur-complement argument gives equality of characteristic polynomials, and polynomial continuation includes \(z=0\) and every algebraic multiplicity.
It requires no inverse of \(C\).

In the finite tracial algebra, bounded FK multiplicativity applies even if \(z-uv\) or \(z-vu\) has determinant zero.
The two block factorizations give
\[
 \Delta_{\operatorname{tr}_2\otimes\tau}
 \left(\begin{pmatrix}z&u\\v&1\end{pmatrix}\right)^{2}
 =\Delta_\tau(z-uv)
 =|z|\Delta_\tau(1-vu/z)
 =\Delta_\tau(z-vu),\qquad z\ne0.
\]
The square comes from normalized block trace, and the scalar factor is \(|z|\).
The unitriangular determinant calculation is valid: invertible similarity preserves the determinant, and scaling the off-diagonal entry to zero stays in the invertible set where norm continuity holds.
No division by a zero determinant occurs.
Equality of the locally integrable Brown potentials off the single point zero gives equality of their distributional Laplacians.
For selfadjoint \(CAC^*\), the Brown measure is its spectral law, so the already proved selfadjoint convergence supplies the full Task conclusion for this subclass.

The polynomial pushforward extension also has the needed zero-determinant boundary.
Factoring \(g(t)-z\) and applying bounded multiplicativity gives the Brown-potential formula in the extended real sense; the positive parts are bounded on compact Brown support.
Taking distributional Laplacians proves Brown polynomial spectral mapping.
At finite size, ordinary spectral mapping with algebraic multiplicity gives the same pushforward.
Composition with \(g\) preserves bounded continuity of test functions, so weak convergence passes to \(g(P)\).
Constant \(g\), zero or singular \(C\), and constant \(P\) cause no additional restriction.

## Source verification and limits

The reviewer inspected the retained [Gui12 original](../../literature/pdf/Gui12.pdf), Section 2.3, Theorem 4, PDF pp. 13--14, by text extraction and page images.
It covers real or complex independent Wigner matrices with bounded moments of every order.
Its displayed variance normalization includes diagonal entries; the candidate's explicit local graph proof supplies the harmless different-diagonal-variance and truncated-variance adaptation.
The source is not being used as a finite-second-moment theorem, and no whole-notes proof audit is claimed.

The reviewer inspected the retained [War16 arXiv v1 original](../../literature/pdf/War16--arxiv-v1.pdf), Theorem 1, PDF p. 2, by text extraction and page image.
Its independent-coordinate bounded-differences hypothesis and exponent \(-2t^2/\sum c_k^2\) match the row-block use.
The original McDiarmid proof is accepted at the theorem-statement and applicability level.
No typical-good-set theorem or journal/preprint equivalence is used.

The bounded FK product theorem is reused at the exact [retained finite-tracial interface](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
The local finite-tracial extension and its zero-determinant scope were read and checked for this use.
The original FK52 pages were not reopened, and this review does not claim a new full audit of their proof.

The Brown-potential convention and compact-support framework are reused from [C_F0186_v1](../../claims/Yin_C_F0186_v1.md#polynomial-application) and the linked [retained Brown convention](../literature/BZ22/Yin_U001.md#brown-measure-convention).
The underlying Brown-measure construction is an accepted foundational input, not newly proved here.
The self-contained Frobenius perturbation proof in [C_F0186_v3](../../claims/Yin_C_F0186_v3.md#singular-value-perturbation) was rechecked independently, so no Gaussian estimate or prior GUE convergence verdict is needed for that interface.

This is mathematical proof review, not formal verification, a numerical experiment or a manuscript review.
The source checking covers the explicit inputs above and their application; it is not a novelty or exhaustive attribution search.
No source mismatch affecting the six asserted conclusions was found.
The remaining general defect is an explicit unresolved research obligation, not a gap concealed inside an asserted unconditional theorem.
