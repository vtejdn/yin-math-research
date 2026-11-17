---
author: Yin
---

# One dimensional subsequence for the ordinary determinant at quasi-every nonreal shift

<a id="statement"></a>
## Summable deviation probabilities on common dimensions

Fix the entry laws and polynomials in either [symmetrizer class](Yin_C_F0358_v1.md#statement), put \(P_N=P(W^{(N)})\), \(p=P(s)\), and write \(u(z)=\tau\log|p-z|\).
This free logarithm is finite off the real axis.
Given any deterministic infinite sequence of increasing sizes, in particular \(2,4,8,\ldots\), one can select sizes \(N_j\) from it and a deterministic [polar set](Yin_C_F0348_v1.md#polar-convention) \(E\) with the following property.
For each fixed \(z\in\mathbb C\setminus(\mathbb R\cup E)\), the ordinary logarithm \(X_N(z)=N^{-1}\log|\det(P_N-zI)|\) satisfies
\[
  \sum_{j\ge1}\mathbb P\{|X_{N_j}(z)-u(z)|>2/j\}<\infty .
\]
Both the sizes and \(E\) depend only on the marginal laws and the chosen starting sizes.
Consequently \(X_{N_j}(z)\to u(z)\) almost surely under every coupling across sizes, with the probability-one event allowed to depend on \(z\).

In the product class \(P=AB\), use the [Hermitian comparison and compression](Yin_C_F0358_v3.md#statement) \(C_N=|A_N|^{1/2}B_N|A_N|^{1/2}\) and \(D_N(z)=I_{Q_N}+2zQ_N(C_N-zI)^{-1}Q_N\) on the negative spectral subspace of \(A_N\).
Write \(Y_N(z)=N^{-1}\log|\det(C_N-zI)|\) and \(H_N(z)=N^{-1}\log|\det D_N(z)|\), with the determinant of the empty compression equal to one.
The same \(N_j,E\) give
\[
  \sum_{j\ge1}\mathbb P\bigl\{|Y_{N_j}(z)-u(z)|>1/j
                    \ \text{or}\ |H_{N_j}(z)|>3/j\bigr\}<\infty .
\]
At a zero determinant the absolute deviation from any finite target is infinite.

<a id="selection"></a>
## Choosing the sizes from the marginal laws

Let \(\rho_N=N^{-1}\sum_{\operatorname{Im}\lambda\ne0}\delta_\lambda\) count the nonreal eigenvalues of \(P_N\) with algebraic multiplicities and put \(V_N(z)=\int\log^-|z-w|\,d\rho_N(w)\), where \(\log^- r=\max(0,-\log r)\) and \(\log^-0=+\infty\).
The [real-root decomposition](Yin_C_F0358_v2.md#loss) gives \(X_N=u+e_N-V_N\), where the finite continuous error \(e_N\) is the explicitly defined sum of the real-root potential minus \(u\) and the nonreal positive-log contribution.
On each compact subset of \(\mathbb C\setminus\mathbb R\), \(e_N\to0\) uniformly almost surely.
Also \(0\le\rho_N(\mathbb C)\le1\) and its mass tends to zero almost surely by the [real-root count](Yin_C_F0358_v2.md#argument), hence in expectation.

Set \(K_j=\{z:|z|\le j,\ |\operatorname{Im}z|\ge 1/j\}\).
For each fixed \(j\) the marginal probability of \(\sup_{K_j}|e_N|>1/j\) tends to zero, as does that of \(\sup_{K_j}|Y_N-u|>1/j\) in the product class by the [Hermitian comparison](Yin_C_F0358_v3.md#comparison).
The suprema are measurable by continuity and compactness.
Choose \(N_j>N_{j-1}\) recursively in the starting sequence so that the probability of the union of the applicable events is at most \(2^{-j}\) and \(j\,\mathbb E\rho_{N_j}(\mathbb C)\le 2^{-j}\).
Almost-sure convergence under any one coupling suffices for these choices because the conditions use only single-size probabilities.

<a id="polar"></a>
## The exceptional set of the mean nonreal-root measure

The deterministic measure \(\eta=\sum_{j\ge1}j\,\mathbb E\rho_{N_j}\) has finite mass.
By Tonelli,
\[
 F(z)=\int\log^-|z-w|\,d\eta(w)=\sum_{j\ge1}j\,\mathbb E V_{N_j}(z).
\]
The set \(E=\{F=+\infty\}\) is Borel since the kernel is nonnegative and lower semicontinuous.
To see that \(E\) is polar, suppose a compact subset carries a finite-log-energy probability \(\sigma\).
The negative part of \(\log(1/|z-w|)\) is bounded on the square of that compact set, so the potential \(L_\sigma(y)=\int\log^-|y-x|\,d\sigma(x)\) is finite \(\sigma\)-almost everywhere.
For some finite \(M\), the closed subset \(K\) of this compact set where \(L_\sigma\le M\) has positive \(\sigma\)-mass.
Put \(\gamma=\sigma|_K\).
For any \(w\) choose a nearest point \(y\in K\).
Then \(|x-y|\le2|x-w|\) for \(x\in K\), hence \(L_\gamma(w)\le L_\gamma(y)+\gamma(K)\log 2\le M+\log 2\).
Tonelli gives \(\int F\,d\gamma=\int L_\gamma\,d\eta<\infty\), contradicting \(F=+\infty\) on \(K\).
This uses the [finite-energy characterization of positive capacity](Yin_C_F0348_v1.md#polar-convention) and includes atoms of every mean divisor.

For \(z\notin E\), Markov's inequality gives \(\sum_j\mathbb P\{V_{N_j}(z)>1/j\}\le F(z)\).
In particular a nonreal atom at this \(z\) with positive probability at even one selected size would force \(F(z)=+\infty\).
Each fixed nonreal \(z\) belongs to \(K_j\) eventually, so the error bounds and the exact decomposition yield the asserted series for \(X\).
In the product class \(Y_N\) is finite at every nonreal \(z\) and the [exact determinant identity](Yin_C_F0358_v3.md#argument) gives \(H_N=X_N-Y_N\), also when \(X_N=-\infty\).
The triangle inequality on the event of finite, controlled deviations proves the other series.
The first Borel--Cantelli lemma applies under every coupling.

<a id="scope"></a>
## Fixed shifts and exact pencils

The [mean-potential envelope](Yin_C_F0348_v1.md#statement) gives a favorable deterministic subsequence that may depend on the parameter at contact points outside a polar set.
Here the sparse nonreal roots give one subsequence for all the nonreal shifts outside \(E\), together with summable marginal bounds.
The proof leaves open whether \(i\in E\) for any specified model.
For \(t>0\), replacing \(B\) by \(tB\) sends \(C_N\) to \(tC_N\) and gives \(D_N^{(tB)}(tz)=D_N^{(B)}(z)\).
Simultaneous dilation therefore preserves the entire compressed determinant at the corresponding shift, including a possible zero.

For an [exact scalar word-chain linearization](../ledger/Yin_L_F0061_v2.md#linearization-transfer) of \(P-z\) of fixed auxiliary size \(m\), its \(1/(mN)\)-normalized ordinary logarithm and its free logarithm are \(X_N(z)/m\) and \(u(z)/m\), respectively.
The same subsequence and polar exception thus give summable deviation probabilities at threshold \(2/(mj)\) for these [F0013 pencils](../tasks/Yin_T_F0013_v1.md#contract).
The result leaves a preassigned exceptional parameter in [F0014](../tasks/Yin_T_F0014_v1.md#contract) and general affine pencils in F0013 unresolved.

## Current assessment
[Selected decision](#decision-common-subsequence-reviewed)

## Assessment history

### Decision common-subsequence-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-18T00:49 |
| status | open |
| reason | The vanishing nonreal mass yields a finite weighted mean measure on a single subsequence, giving summable deviations outside its polar exceptional set. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Common dimensions](#statement) | Ordinary nonreal logarithms for both symmetrizer classes and the product compression. |
| argument | [Marginal choice](#selection) | Compact error bounds and mass summability from any starting sizes. |
| support | [Finite-energy proof](#polar) | Deterministic polar exception, coincidence atoms and summable deviations. |
| support | [Dilation and pencil transfer](#scope) | Prescribed shifts and the exact auxiliary normalization. |

### Decision common-subsequence-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:53 |
| status | proved |
| reason | A weighted mean measure of exceptional roots gives summable probabilities on one deterministic subsequence outside a deterministic polar set. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed theorem](#statement) | A weighted mean measure of exceptional roots gives summable probabilities on one deterministic subsequence outside a deterministic polar set. |
| argument | [Complete proof](#selection) | The stated parameter, normalization and coupling requirements. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0366_v4.md#common-subsequence-whole-proof) | Entire fixed statement and its exact scope. |
