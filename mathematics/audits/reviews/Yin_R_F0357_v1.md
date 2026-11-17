---
author: Yin
---

# Fixed-shift determinant upper limits outside a polar set

An agent for Yin performed an initial independent whole-proof review of [C348v1](../../claims/Yin_C_F0348_v1.md#statement) on 2026-11-17T04:56 UTC.
The reviewer had no role in developing the proof and received no proof-development discussion, author explanation or prior finding on this result.
The inputs were the fixed Claim, the cited mathematical dependencies and the original potential-theory statements.
The reviewer checked the corrected attribution to the single-author 2008 edition against its title page and Appendix A.

## Finding

The proof establishes the stated fixed-shift upper-limit equality for every coupling and quasi-every shift in the unbounded component, with the stated contact-set and whole-plane extensions.
For fixed coefficient size \(m\), the Hermitian square has normalized trace \(1/(mN)\), and its regularized logarithm carries the factor \(1/2\).
The matrix-coefficient argument in C186v4 gives weak convergence for bounded cutoffs, a power bound on the expected singular-value tails and almost-sure logarithmic tail control for each fixed shift and regularizer.
Together these imply both \(L^1\) convergence and almost-sure convergence for each regularized statistic.
A decreasing countable sequence of regularizers thus gives the pathwise upper bound even at free logarithm \(-\infty\), and bounds the expected positive overshoot at every finite target.
The constant-polynomial case follows from the same trace identities directly.

The integrated determinant inequality and the expected singular-value tail bound give a uniform second positive logarithmic moment for the mean eigenvalue measures.
Their potentials therefore have finite positive parts at every shift and agree with the ordinary determinant expectations in the extended sense.
The local planar \(L^1\) cutoff argument applies to each deterministic weakly convergent subsequence.
Shrinking disk means extend its almost-everywhere potential order to every point, including logarithmic poles.
For each circle enclosing the Brown support, the integral of the negative part of the circle kernel is uniformly bounded in the source point, including on that circle, by integrability of its angular logarithmic singularity.
The positive part is controlled by the first positive logarithmic moment.
Consequently the circle mean is the integral of \(\log\max(r,|w|)\), which forces the cluster measure inside the disk.
On the common exterior harmonicity, pointwise order and equality of these means imply equality, and the subharmonic maximum principle propagates it throughout the unbounded component.

Appendix A of the 2008 manuscript uses probability mass one and the kernel \(-\log|z-w|\).
Theorems A.3 and A.4 give equality of the lower limit with the limiting potential outside a set of capacity zero.
Changing sign gives precisely the upper limit used here, with no area normalization or factor of \(2\pi\).
Moving the exterior mass to the fixed point \(2L\) puts all measures on a common compact set.
Weak convergence makes this mass vanish, and Cauchy--Schwarz with the uniform second logarithmic moment controls the change of the far potential uniformly on the test disk.
The local singular part is identical even at points where it is infinite.
The polar exceptions can be chosen Borel by taking the failure set of the equality of measurable potentials.
On a compact set carrying a finite-energy probability the energy kernel is bounded below, so positive-mass restrictions still have finite energy, and inner regularity proves the asserted countable-union property.
The external theorems were checked at their stated interfaces. [Chafaï, Appendix A, printed pp. 19--20](https://hal.science/hal-00310528v1/file/cirmar.pdf#page=20) and [Saff, Definition 1.8](https://arxiv.org/pdf/1010.3760#page=8).

At a finite contact value the envelope permits a deterministic subsequence with finite ordinary expectations tending to the free value.
The positive overshoot estimate and the signed first-moment identity then give \(L^1\) convergence.
A further deterministic subsequence has summable deviation probabilities on the prescribed marginal laws and hence converges almost surely under each coupling.
The probability-one event may depend on the fixed shift and coupling, and the exceptional polar set for a specified cluster measure may depend on its chosen approximating subsequence.
One cluster measure suffices on the exterior, while a subsequence converging to the Brown measure suffices on the entire plane.
The thin filled-support and real fourth-moment applications supply that subsequence because bounded continuous tests that converge in probability to constants converge in mean.
A prescribed shift may lie in the exceptional set, so the finding leaves the unrestricted determinant and Brown-measure contracts open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Fixed-shift finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Fixed-shift finding](#finding) | [Claim statement](../../claims/Yin_C_F0348_v1.md#statement) | Fixed model and polynomial, every coupling, polar exceptional sets, contact sets and finite or infinite targets. |
| [Fixed-shift finding](#finding) | [Marginal and cluster argument](../../claims/Yin_C_F0348_v1.md#argument) | Matrix normalization, regularized bounds, mean potentials, compactness, order and equality on the unbounded component. |
| [Fixed-shift finding](#finding) | [Polar conventions](../../claims/Yin_C_F0348_v1.md#polar-convention) | Finite logarithmic energy and the Borel polar exception. |
| [Fixed-shift finding](#finding) | [Envelope and probability argument](../../claims/Yin_C_F0348_v1.md#lower-envelope) | Compact truncation, sign change, countable exhaustion and extraction of favorable dimensions. |
| [Fixed-shift finding](#finding) | [Hermitized weak limit](../../claims/Yin_C_F0186_v4.md#finite-variance-weak) | Fixed selfadjoint matrix polynomials under complex or real finite-second-moment laws. |
| [Fixed-shift finding](#finding) | [Expected singular-value tails](../../claims/Yin_C_F0186_v4.md#positive-tail) | Fixed coefficient size, positive logarithmic moments and expected truncation. |
| [Fixed-shift finding](#finding) | [Almost-sure logarithmic tail](../../claims/Yin_C_F0186_v4.md#log-statistics) | Summable marginal concentration and truncation under arbitrary cross-size coupling. |
| [Fixed-shift finding](#finding) | [Eigenvalue moment comparison](../../claims/Yin_C_F0186_v4.md#noncompact-planar) | Transfer of the singular-value second positive logarithmic moment to eigenvalues. |
| [Fixed-shift finding](#finding) | [Potential cutoff](../../claims/Yin_C_F0186_v25.md#subsequence-potentials) | Local planar convergence for deterministic measures with the second positive logarithmic moment bound. |
| [Fixed-shift finding](#finding) | [Exterior comparison](../../claims/Yin_C_F0186_v25.md#unbounded-component) | Propagation of equality on the connected harmonicity domain. |
| [Fixed-shift finding](#finding) | [Thin filled support](../../claims/Yin_C_F0186_v25.md#statement) | Almost-sure Brown convergence for the scalar thin filled-support class. |
| [Fixed-shift finding](#finding) | [Real fourth-moment model](../../claims/Yin_C_F0186_v26.md#statement) | Brown convergence in probability for the real two-sided product and resulting convergence of mean measures. |
| [Fixed-shift finding](#finding) | [Marginal criterion](../../claims/Yin_C_F0190_v1.md#coupling-criterion) | Summable lower deviations and the fixed-shift every-coupling upper limit. |
