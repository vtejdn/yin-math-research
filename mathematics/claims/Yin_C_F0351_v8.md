---
author: Yin
---

# Terminal logarithms of the real two-sided Wigner product under second moments

<a id="statement"></a>
## The finite-variance real model

Let \(A_N,B_N\) be independent real symmetric Wigner matrices with fixed centered variance-one strict upper laws, fixed centered diagonal laws with finite second moments, independent coordinates up to symmetry and \(N^{-1/2}\) scaling.
The two colors may have different laws.
Write \(P_N=A_NB_N+2B_NA_N\), \(p=ab+2ba\) for free standard semicircular \(a,b\), \(u(z)=\tau\log|p-z|\), and \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\).
For any coupling across dimensions, almost surely the ordinary normalized potentials converge to \(u\) in local planar \(L^1\) and the empirical eigenvalue laws converge weakly to the Brown measure of \(p\).
Here a coupling means any joint law with the given dimensional marginals.
For decreasing singular values and every \(R,\epsilon>0\),
\[
 \sum_{N:\,q_N<N}\Pr\left\{\frac1N\int_{|z|<R}
      \sum_{j>N-q_N}\log^-s_j(P_N-zI)\,dA(z)>\epsilon\right\}<\infty .
 \tag{1}
\]
No moment above two, discrete-law restriction or translation regularity is required.

For each deterministic \(z_N\to z\notin\mathbb R\),
\[
 N^{-1}\log|\det(P_N-z_NI)|\ \longrightarrow\ u(z)
\]
in probability through all dimensions and almost surely on \(N=2^j\) under each allowed coupling.
In particular at every fixed nonreal \(z\) the ordinary dimension limsup equals \(u(z)\) almost surely.
The pointwise assertion for real finite-variance laws at nonreal shifts gives a distinct bound from the planar series.
For sign inputs the [separate all-shift theorem](Yin_C_F0351_v7.md#statement) includes the real axis.

<a id="argument"></a>
## Where the moment assumptions enter the terminal comparison

Use \(k=2\lfloor\log^3(N+3)/2\rfloor,\ n=N-k,\ h=q_n\), and the old minor \(M=A_{JJ}B_{JJ}+2B_{JJ}A_{JJ}\) with its original scaling.
Write \(t_1\le\cdots\le t_n\) for the singular values of \(M-wI\) and \(b_i=N^{-1}\sum_{j>i}\log t_j\).
By the [finite-variance trim theorem](Yin_C_F0186_v41.md#terminal), almost surely on every disk \(b_{2h}\to u\) in \(L^1\) and \(\int(h/N)\log^-t_{2h+1}\to0\) under the given coupling.
The same limits hold pointwise along deterministic parameters tending to a nonreal point, with the first limit evaluated at that point.
The proof uses a polynomial norm guard from Frobenius Markov and a high-dimensional projection of the raw fresh row.
Its initial retained product uses the [polynomial-window count](Yin_C_F0186_v40.md#argument), which already requires only second moments.

The [finite-variance near-kernel overlap estimate](Yin_C_F0196_v6.md#first-overlaps) handles the singular subspaces before the first directions are deleted.
On \(\|M\|\le N^5\), the largest \(r\le2h\) with \(t_r<N^{-40h}t_{r+1}\) can be chosen from the minor alone, using zero when it does not exist.
For the regular parameters used for division, the [compound determinant and adjacent-gap bounds](Yin_C_F0351_v1.md#adaptive-gap) imply that the log determinant after deleting the first \(r\) directions is at least
\[
 Nb_{2h}-2h\log^-t_{2h+1}-O(h^3\log N)
\]
outside probability \(O(h n^{-5/4}+n^{-D}+hN^{-3})\), with \(D\) as large as needed, in addition to the summable norm guard exception.
This is uniform in marginal probability on compact sets separated from the real axis.

<a id="cross-block"></a>
## The rectangular guard under second moments

For \(V=B_{JI}\) the \(n\times k\) cross block, \(s_{\min}(V)\ge c\) outside a summable exception.
For a prescribed real unit \(v\in\mathbb R^k\), a row of \(\sqrt N Vv\) has variance one.
The squares of these row sums are uniformly integrable as the coefficient vector and its dimension vary: center the entries after truncation at a fixed large raw threshold, use the uniform fourth moment for each bounded linear sum, and bound the omitted sum in \(L^2\) by the fixed second tail moment.
Thus a row exceeds some positive absolute threshold in modulus with probability bounded below uniformly.
Independence of rows gives \(\|Vv\|\ge c\) except with \(Ce^{-cn}\).
On \(\|B\|\le N^2\) extend from a real net of mesh \(c/(2N^2)\); its entropy is \(O(k\log N)=o(n)\).
The guard fails with \(O(N^{-3})\) by the expected squared Frobenius norm, and the real least singular value agrees with the complex one.
This proof supplies the precise rectangular input without invoking a higher moment for \(B\).

<a id="ratios"></a>
## The remaining discrete and continuous borders

The [physical-corner comparison](Yin_C_F0351_v6.md#physical-corners) for the old minor uses finite second moments throughout its proof.
Its bounded raw truncations use moment convergence with deterministic coordinate projections.
Passing back uses rank and normalized Hilbert--Schmidt approximation; spectral clipping of each input at a fixed value above the semicircle edge changes \(o(n)\) ranks with exponentially small fixed-fraction deviations by bounded-rank row concentration.
The actual inverse is compared with a bounded regularization by deleting its small-singular subspace.
Thus the finite free-corner estimates hold on all regular steps under the present laws.
No fourth moment appears in the [resulting fresh-border estimates](Yin_C_F0351_v6.md#border-tests): truncating large coordinates of a difference vector uses its tail probability, and a bounded symmetric core has positive variance.
The Fourier estimate uses the positive difference mass of any fixed nonconstant real law in a compact interval away from zero.

Apply the [flag and paired-restoration bounds](Yin_C_F0351_v6.md#ratios), now with the rectangular guard just proved.
The unnormalized column norms and \(\|B_{II}\|\) are polynomial outside summable exceptions by second moments.
For one step at \(d\) separated nonreal shifts, the joint bad-ratio probabilities are \(O(n^{-d/8})\) for the flag and \(O(n^{-d/32})\) for the restoration, on the respective histories and with the polynomial guards treated as in the cited proof.
Their thresholds \(N^{-7},N^{-12}\) cost \(O(k\log N)\) before normalization.
Taking 16 and 64 separated shifts respectively shows that the probabilities of exceptional areas exceeding each positive tolerance on any fixed disk are summable.
These tests allow the first deletion used to vary with \(w\).
The initial projected space of the restorations is exactly the final common flag compression, by cancellation of the two cross terms under projection on both sides.

<a id="limits"></a>
## Pointwise and planar conclusions

Off the union of the exceptional sets, multiplication gives
\[
 |\det(P_N-wI)|\ge \exp[-C(h^3+k)\log N]\,
      p_{n-2h}(M-wI)\min(1,t_{2h+1})^{2h}.
 \tag{2}
\]
Here \(p_j\) denotes the top \(j\) singular-value product.
For a single shift the probability of strict violation is at most
\(C(h n^{-5/4}+k n^{-1/32})+O(n^{-2})\), uniformly on each fixed compact region away from the real axis, first for planar almost every shift.
Both sides in (2) are continuous functions of \(w\) for a fixed realization and the right side contains no division.
Approaching any exceptional prescribed parameter through the full-area set in a slightly larger compact region preserves the probability bound by Fatou's lemma on indicators of strict violations.
Together with the moving two trims this proves the lower log limit in probability and almost surely on the dyadic sequence by first Borel--Cantelli.
The upper log limit holds almost surely in all dimensions by the [fixed-clip bound](Yin_C_F0186_v4.md#regularized-potentials), using fixed-clip Lipschitz continuity in a moving shift.
This proves the pointwise assertions, without an all-dimensions summability claim at a single shift.

For planar convergence use summable initial marginal failures away from the real axis and Fubini to see that their exceptional areas tend to zero almost surely, first on each bounded region \(|\operatorname{Im}w|\ge1/j\).
The two later exceptional areas already have summable fixed-tolerance bounds.
By (2) and the two old-minor trims, the negative deficit of the ordinary potential relative to \(u\) tends to zero in disk integral outside these small sets.
On the sets and the thin real strip use the deterministic uniform disk \(L^2\) bound on the negative part of the normalized characteristic log, by Jensen applied to the translated negative logarithmic kernels.
The compactly supported free Brown measure gives the same local integrability of \(u\).
The [full-matrix trimmed potential](Yin_C_F0186_v41.md#statement) and the \(o(1)\) normalized contribution of its omitted positive logarithms give the reverse comparison.
The latter uses \(\max(\|A_N\|,\|B_N\|)\le N^2\) eventually almost surely by Frobenius Markov.
This proves the local \(L^1\) conclusion under every coupling, hence weak convergence by distributional Laplacians and tightness.
The [finite-variance terminal equivalence](Yin_C_F0186_v41.md#terminal) gives (1) by applying the conclusion to independent dimensions and using converse Borel--Cantelli.

## Current assessment
[Selected decision](#decision-two-moment-terminal-reviewed)

## Assessment history

### Decision two-moment-terminal-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:55 |
| status | open |
| reason | The finite-variance initial trim and near-kernel overlap estimates give the missing inputs to the original-law terminal comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Finite-variance limits](#statement) | Full planar convergence, terminal series and individual nonreal-shift probability limits. |
| argument | [Initial product and overlaps](#argument) | The two new second-moment estimates and the adaptive gap. |
| support | [Cross block](#cross-block) | Finite-variance rectangular lower bound for polylogarithmic codimension. |
| support | [Remaining ratios](#ratios) | Quantitative inputs and moment use in the flag and Schur comparison. |
| support | [Planar and prescribed-shift limits](#limits) | Couplings, singular endpoints and integrated logarithms. |

### Decision prescribed-sign-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:03 |
| status | proved |
| reason | Independent whole-proof review confirmed the real- and complex-parameter result of v7, including the symmetric coefficient and the even dyadic sequence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Sign product at all shifts](Yin_C_F0351_v7.md#statement) | Ordinary convergence in probability, dyadic almost-sure convergence and the dimension upper limit, including scalar compositions. |
| argument | [Prescribed-shift argument](Yin_C_F0351_v7.md#argument) | Physical spectral-window separation and the fixed-parameter proof. |
| support | [Two trimmed limits](Yin_C_F0351_v7.md#trim) | Paired-volume growth including real shifts. |
| support | [Initial sign columns](Yin_C_F0351_v7.md#overlap) | Incompressible vectors and an antichain bound on a fresh projection. |
| support | [Restoration](Yin_C_F0351_v7.md#restore) | Symmetric or nonsymmetric rational kernels and the ordinary limit. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0358_v7.md#prescribed-sign-whole-proof) | The fixed v7 result and its quantitative interfaces. |


### Decision two-moment-terminal-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:03 |
| status | proved |
| reason | The initial finite-variance trim and overlap estimates complete the physical Schur comparison and yield the planar terminal series for arbitrary fixed real finite-variance inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two-moment terminal theorem](#statement) | The fixed statement with the specified laws, dimensions and coupling quantifiers. |
| argument | [Complete argument](#argument) | The initial finite-variance trim and overlap estimates complete the physical Schur comparison and yield the planar terminal series for arbitrary fixed real finite-variance inputs. |
| support | [Rectangular floor](#cross-block) | Original-law lower bound for the cross block at polylogarithmic codimension. |
| support | [Discrete or continuous borders](#ratios) | Conditional ratio estimates and their exceptional areas. |
| support | [Area and fixed shifts](#limits) | Integrated marginal series and the pointwise nonreal probability and dyadic limits. |
| dependency | [Finite-variance trims](Yin_C_F0186_v41.md#terminal) | Old-minor estimates and terminal equivalence. |
| dependency | [First singular overlaps](Yin_C_F0196_v6.md#first-overlaps) | Summable original-law failures at the selected singular gap. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0358_v8.md#two-moment-terminal-whole-proof) | Hypotheses, conclusions, proof and directly used mathematical interfaces. |
