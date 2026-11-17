---
author: Yin
---

# Fixed-shift determinant upper limits from logarithmic potentials of mean spectral measures

<a id="statement"></a>
## Upper limits at fixed spectral parameters

Fix the entry laws of [F0013](../tasks/Yin_T_F0013_v1.md#contract) and a square matrix polynomial \(P\) of fixed coefficient size \(m\) in the Hermitian inputs, including \(m=1\) and every matrix affine pencil.
Put \(A_N=P(W^{(N)})\), \(a=P(s)\), \(n=mN\), and let \(\bar\mu_N\) be the expectation of the empirical eigenvalue probability measure of \(A_N\), with algebraic multiplicities.
Write \(\mu\) for the Brown measure of \(a\) under the normalized matrix trace tensored with the free trace, and write \(U_\rho(z)=\int\log|z-w|\,d\rho(w)\).
Let \(G\) be the unbounded connected component of \(\mathbb C\setminus\operatorname{supp}\mu\).

There is a deterministic polar set \(E\) such that for each fixed \(z\in G\setminus E\) and every coupling across dimensions,
\[
 \limsup_N\frac1n\log|\det(A_N-zI_n)|=U_\mu(z)=\log\Delta(a-z)\qquad\text{almost surely}.
\]
If a deterministic subsequence of \(\bar\mu_N\) converges weakly to \(\mu\), the same conclusion holds on the whole plane outside a deterministic polar set.
More precisely, for any weak cluster measure \(\nu\) of the deterministic sequence \(\bar\mu_N\), the conclusion holds quasi-everywhere on its contact set \(\{z:U_\nu(z)=U_\mu(z)\}\).
At each such point of finite free logarithm there is a deterministic, possibly point-dependent, subsequence with convergence of the normalized ordinary logarithms in \(L^1\).
At free logarithm \(-\infty\) the full sequence converges almost surely in the extended sense by the upper bound.
The exceptional set and the favorable dimensions use only the marginal laws.
The almost-sure event may depend on the parameter and the coupling.

<a id="polar-convention"></a>
A Borel set is polar if every compact subset has logarithmic capacity zero.
A compact set has positive logarithmic capacity exactly when it carries a probability measure with finite logarithmic energy \(\iint\log(1/|z-w|)\,d\sigma(z)d\sigma(w)\).
We use the usual meaning of quasi-everywhere, namely outside a polar set.
These conventions are stated in [Saff, Section 1, pp. 171--172](https://arxiv.org/pdf/1010.3760#page=7).

<a id="argument"></a>
## Marginal upper bounds and the cluster measure

With \(X_N(z)=n^{-1}\log|\det(A_N-zI_n)|\) and \(u(z)=U_\mu(z)\), use
\[
 X_N(z)\le X_{N,\delta}(z)=\frac1{2n}\operatorname{Tr}\log((A_N-zI_n)^*(A_N-zI_n)+\delta^2 I_n).
\]
For fixed \(z\in\mathbb C\) and \(\delta>0\), the [matrix Hermitized weak law](Yin_C_F0186_v4.md#finite-variance-weak) and [positive log tails](Yin_C_F0186_v4.md#positive-tail) give convergence in \(L^1\) of \(X_{N,\delta}(z)\) to the free regularization \(u_\delta(z)\).
Indeed the lower part of the regularized test is bounded, and truncation above has vanishing expected error uniformly in \(N\).
The pathwise tail control of [C186v4](Yin_C_F0186_v4.md#statement) gives almost-sure convergence by the same truncation under every coupling.
Both arguments apply to fixed matrix coefficients by using the normalized trace on the \(mN\)-dimensional Hermitian square.
As \(u_\delta\downarrow u\), a countable sequence of regularizers gives the pathwise upper bound and, wherever \(u(z)>-\infty\), the marginal estimate
\[
 \mathbb E(X_N(z)-u(z))_+\longrightarrow0 .
\]
The latter follows by first taking the upper limit at fixed \(\delta\), bounded by \(u_\delta(z)-u(z)\), and then sending \(\delta\) to zero.

The [eigenvalue-to-singular-value estimate](Yin_C_F0186_v4.md#noncompact-planar) and the expected positive-log square bound of the same work give
\(\sup_N\int(\log^+|w|)^2\,d\bar\mu_N(w)<\infty\).
In this estimate the finite-dimensional determinant inequality holds for every matrix size and the preceding tail estimate uses the fixed \(m\).
This ensures tightness and uniform integrability at infinity of the first positive logarithmic moment.
Fix a subsequence on which \(\bar\mu_N\Rightarrow\nu\).
The same second logarithmic moment bound holds for \(\nu\) by lower semicontinuity.

Set \(v_N=U_{\bar\mu_N}\).
Tonelli on the two parts of the logarithm gives \(v_N(z)=\mathbb E X_N(z)\), allowing \(-\infty\).
Along the chosen subsequence \(v_N\to U_\nu\) in planar \(L^1_{\rm loc}\) by the [cutoff-kernel proof](Yin_C_F0186_v25.md#subsequence-potentials) applied to the deterministic probability measures \(\bar\mu_N\).
For each \(z\), the regularized upper bound gives \(\limsup v_N(z)\le u(z)\).
Taking a further planar almost-everywhere convergent subsequence gives \(U_\nu\le u\) almost everywhere.
The inequality holds at every point by taking shrinking disk means of the two subharmonic representatives.
For each \(r\) exceeding a disk radius containing the Brown support, the circle mean of \(U_\nu\) is \(\int\log\max(r,|w|)\,d\nu(w)\ge\log r\), the circle mean of \(u\).
The two means agree by the upper inequality.
In particular \(\nu\{|w|>r\}=0\), and on the common exterior the two harmonic potentials agree by the circle means and the pointwise ordering.
On \(G\), \(U_\nu-u\) is subharmonic, nonpositive and vanishes on the exterior.
The maximum principle gives \(U_\nu=u\) throughout \(G\).
This argument applies the [exterior comparison](Yin_C_F0186_v25.md#unbounded-component) to deterministic mean measures and gives compact support of every \(\nu\).

<a id="lower-envelope"></a>
## From the deterministic envelope to fixed-shift probabilities

Use the compact-support lower-envelope theorem stated in [Djalil Chafaï, 2008 single-author manuscript, Appendix A, Theorems A.3--A.4](https://hal.science/hal-00310528v1/file/cirmar.pdf#page=20).
The inspected statement uses \(-\log|z-w|\), so for the sign used here its conclusion is \(\limsup U_{\rho_j}=U_\nu\) quasi-everywhere when \(\rho_j\Rightarrow\nu\) and all supports lie in a common compact set.
Only this deterministic statement is used from that source.

For a disk \(|z|\le R\) with \(R\ge1\), choose \(L>2R+2\) so large that \(\nu\) is supported in \(|w|<L-1\).
Collapse the restriction of \(\bar\mu_N\) to \(|w|>L\) to an atom of the same mass at \(2L\).
The mass tends to zero on the chosen subsequence, so the resulting probabilities have common compact support and still converge to \(\nu\).
The change of potential on the disk is at most \(C_{R,L}\int_{|w|>L}(1+\log^+|w|)\,d\bar\mu_N(w)\), uniformly in \(z\), with identical negative singularities for the two potentials.
This bound tends to zero by Cauchy--Schwarz and the second logarithmic moment bound.
The lower-envelope theorem and a countable exhaustion by disks now give
\[
 \limsup_{N\ \mathrm{in\ the\ chosen\ subsequence}}\mathbb E X_N(z)=U_\nu(z)
\]
outside a deterministic polar set.
A countable union of Borel polar sets is polar, since restrictions of a compactly supported finite-energy measure to sets of positive mass still have finite energy after normalization.

Fix a contact point outside that set with finite \(u(z)\).
Choose a further deterministic subsequence on which \(\mathbb E X_N(z)\to u(z)\), retaining only finite expectations.
The identity
\[
 \mathbb E|X_N(z)-u(z)|=2\mathbb E(X_N(z)-u(z))_++u(z)-\mathbb E X_N(z)
\]
gives \(L^1\) convergence along this subsequence.
A further subsequence with summable deviation probabilities combined with the pathwise upper bound gives the asserted almost-sure upper limit under every coupling, by the [marginal criterion](Yin_C_F0190_v1.md#coupling-criterion).
One deterministic cluster measure suffices for the exterior assertion.
When \(\nu=\mu\), every point is a contact point.

## Consequences for the three Tasks

For every fixed finite-variance matrix pencil the first conclusion applies to scalar shifts of its constant coefficient throughout the unbounded component, up to a polar set.
Taking the scalar-polynomial specialization gives the corresponding [F0014](../tasks/Yin_T_F0014_v1.md#contract) conclusion.
Whenever an [F0012](../tasks/Yin_T_F0012_v3.md#contract) model has Brown convergence in probability along some deterministic subsequence, bounded continuous tests give weak convergence of the expected eigenvalue measures along it, which suffices for the whole-plane conclusion.
In particular this applies to the [thin filled-support class](Yin_C_F0186_v25.md#statement) and to [the real fourth-moment model \(P(x,y)=xy+2yx\)](Yin_C_F0186_v26.md#statement).
The latter application strengthens the set of shifts for the upper-limit equality from full planar measure to the complement of a polar set.
The present argument allows a prescribed shift, including zero, to lie in the exceptional set and gives no full-sequence almost-sure Brown limit in an unresolved model.

## Assessment history

### Decision polar-envelope-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T04:58 |
| status | proved |
| reason | Independent review verified the mean-measure argument, the exact deterministic envelope input and the passage to almost-sure upper limits for every coupling. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed-shift conclusion](#statement) | Exterior and contact-set equalities outside a polar set, with point-dependent favorable dimensions. |
| argument | [Mean measures](#argument) | Deterministic cluster compactness, potential ordering and exterior equality. |
| support | [Envelope passage](#lower-envelope) | Common compact support reduction, sign convention, probability extraction and examples. |
| dependency | [Hermitized law](Yin_C_F0186_v4.md#finite-variance-weak) | Fixed matrix polynomial singular-value tests. |
| dependency | [Positive tails](Yin_C_F0186_v4.md#positive-tail) | Uniform integrability in expectation. |
| dependency | [Pathwise tail](Yin_C_F0186_v4.md#log-statistics) | Upper bound under every coupling. |
| dependency | [Spectral moment bound](Yin_C_F0186_v4.md#noncompact-planar) | Control of escaping eigenvalues. |
| dependency | [Potential cutoff](Yin_C_F0186_v25.md#subsequence-potentials) | Local planar convergence for deterministic measures. |
| dependency | [Fourth-moment real quadratic](Yin_C_F0186_v26.md#statement) | Convergence of the mean eigenvalue measures in the quadratic application. |
| dependency | [Coupling criterion](Yin_C_F0190_v1.md#coupling-criterion) | Deterministic probability subsequence and the almost-sure upper bound. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0357_v1.md#finding) | Full argument, source edition and scope of the exceptions. |

## Current assessment

[Selected decision](#decision-polar-envelope-reviewed)
