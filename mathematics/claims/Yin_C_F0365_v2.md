---
author: Yin
---

# Dyadic ordinary determinants outside a polar set for a shared-input Wigner product

<a id="statement"></a>
## Summability off the real axis and the remaining loss at \(i\)

For \(A=2I+X,\ B=XY+YX+ZYZ,\ P=AB\), take the [fixed real or complex finite-second-moment Wigner laws](../tasks/Yin_T_F0013_v1.md#input-model) and arbitrary coupling across sizes.
Let \(k_N(h)\) count, with algebraic multiplicity, the eigenvalues of \(P_N\) with \(|\operatorname{Im}\lambda|\ge h\).
For each \(h>0\),
\[
                          \sum_{j\ge1}\mathbb E\, k_{2^j}(h)/2^j<\infty .       \tag{1}
\]
Write \(U_N(z)=N^{-1}\log|\det(P_N-zI)|\), taking \(\log0=-\infty\), and \(u(z)=\tau\log|(2+s_x)(s_xs_y+s_ys_x+s_zs_ys_z)-z|\).
There is a deterministic polar set \(E\) such that for each fixed \(z\notin\mathbb R\cup E\),
\[
        U_{2^j}(z)\longrightarrow u(z)\quad\text{almost surely},
        \qquad \limsup_N U_N(z)=u(z)\quad\text{almost surely}.                  \tag{2}
\]
For each such \(z\) and each \(\epsilon>0\), the dyadic marginal probabilities of deviations exceeding \(\epsilon\) sum to a finite number.
The [normalized logarithm of the negative-subspace determinant](Yin_C_F0358_v3.md#statement) converges to zero along the same dyadic sizes at each such \(z\).
The [exact affine word-chain pencil](../ledger/Yin_L_F0061_v2.md#linearization-transfer) has the ordinary and free logarithms divided by its fixed auxiliary dimension.

At the prescribed \(i\), even when \(i\in E\), there is a deterministic subsequence \(N_l=2^{j_l}\) such that on one probability-one event, for every \(b>0\),
\[
 U_{N_l}(i)=u(i)+o(1)-
       \frac1{N_l}\sum_{\lambda\in\operatorname{spec}(P_{N_l})}
                      \log^+\!\left(\frac{N_l^{-b}}{|\lambda-i|}\right).       \tag{3}
\]
The error term may depend on \(b\), and a root at \(i\) contributes \(+\infty\) to the sum.
Hence the ordinary upper-limit equality at \(i\) follows if for some \(b>0\) the probability of any eigenvalue within \(N_l^{-b}\) of \(i\) tends to zero along these sizes or a further subsequence.
Both (1) and (3) hold for arbitrary atomic inputs.
They leave that last probability, or the weaker required bound on the displayed logarithmic sum, open in the general atomic case.

<a id="weighted"></a>
## A dyadic estimate for weighted finite-mean variables

Let at most \(C_0N^2\) independent nonnegative variables \(T_e\) have laws in a fixed finite set with finite first moments.
For nonnegative deterministic weights satisfying \(\sum_e w_e\le C_0,\ \sum_e w_e^2\le C_0/N^2\), the probability of \(\sum_e w_e T_e>L_0\) has an upper bound depending only on \(N,C_0\) and these laws whose sum over dyadic \(N\) is finite.
One can take \(L_0=1+C_0\max_e\mathbb E T_e\).
Indeed for each \(t\ge0\) both the number of terms with \(w_e t>1\) and the sum of \((w_e t)^2\) over \(w_e t\le1\) are bounded by \(C_0\min(N^2,t^2/N^2)\).
The dyadic sum of this minimum is at most \(Ct\), by splitting at \(N=\sqrt t\).
A union bound controls the probability of any discarded term, and Chebyshev's inequality at distance one from the mean controls the independent truncated sum.
Integration separately against each of the finitely many laws proves the assertion.
It also applies conditional on random weights independent of the variables whenever those same deterministic bounds on the weights hold.

<a id="guard"></a>
## Complete dyadic bounds for the quadratic trace

Put \(G=|2I+X|,\ S=G^{1/2},\ M=ZS\), with \(\operatorname{tr}_N=\operatorname{Tr}/N\).
There is a fixed \(L\) such that
\[
       \sum_{j\ge1}\Pr\{1+\operatorname{tr}_N(G+M^*M)>L\}<\infty ,
                       \qquad N=2^j .                                           \tag{4}
\]
First apply the weighted estimate to \(\operatorname{tr}_N X^2\), whose weights are \(2/N^2\) off the diagonal and \(1/N^2\) on it, multiplying the squared raw magnitudes.
Since \(G^2\le 8I+2X^2\), a fixed bound \(\operatorname{tr}_N G^2\le L_1\) fails with summable dyadic probabilities.
When the bound holds, \(\operatorname{tr}_N G\le\sqrt{L_1}\).
In the rest of the calculation condition on any such \(X\).

To bound \(\operatorname{tr}_N M^*M=\operatorname{tr}_N ZGZ\), decompose the raw Hermitian matrix \(\sqrt N Z\) into its independent upper-entry blocks \(H_e\), with an off-diagonal entry and its conjugate forming a single block.
Then \(\operatorname{tr}_N ZGZ=N^{-2}\sum_{e,f}\operatorname{Tr}H_e G H_f\).
The \(e=f\) part is a weighted sum of independent squared raw entries of \(Z\).
Its weights are \((G_{ii}+G_{kk})/N^2\) for \(i<k\) and \(G_{ii}/N^2\) on the diagonal, since the square of a single off-diagonal block is a scalar times \(E_{ii}+E_{kk}\).
They are nonnegative and sum to \(\operatorname{tr}_N G\).
Their squared sum is at most \(C N\operatorname{Tr}G^2/N^4\le C L_1/N^2\), using \(\sum_i G_{ii}^2\le\operatorname{Tr}G^2\).
The weighted estimate gives a uniform summable bound for exceeding a fixed constant.

The contribution of distinct blocks has conditional mean zero and variance at most \(C N\operatorname{Tr}G^2/N^4\).
For details use the standard real Hilbert--Schmidt orthonormal basis of Hermitian matrices, grouped by the upper-entry blocks, and the symmetric real operator \(\mathcal T(H)=(GH+HG)/2\).
Each block has at most two real coordinates with centered covariance bounded by a common constant, since their squared norm is at most twice the squared raw magnitude.
The contribution from \(e<f\), including its reverse term, is \(2N^{-2}\langle H_e,\mathcal T(H_f)\rangle_{\rm HS}\).
Terms belonging to two different unordered pairs are uncorrelated because a centered independent block occurs once.
For a single pair the second moment of the bilinear form is at most a constant times the sum of squares of the corresponding matrix coefficients of \(\mathcal T\), by independence of the two blocks.
Summing over pairs costs at most \(C N^{-4}\|\mathcal T\|_{\rm HS}^2\).
In an eigenbasis of \(G\) with eigenvalues \(g_i\), that squared operator Hilbert--Schmidt norm is \(\sum_{i,k}((g_i+g_k)/2)^2\le N\operatorname{Tr}G^2\).
Chebyshev's inequality therefore bounds the conditional probability of a distinct-block contribution of absolute value bigger than one by \(C L_1/N^2\).
Combining the bounds proves (4).

<a id="count"></a>
## A summable mean count outside each fixed strip

Apply the [trace-norm comparison with the retained spectral modes](Yin_C_F0365_v1.md#compression) for the fixed \(h\), using its choice of \(\delta\).
There \(C=SBS\), the retained matrix is \(C_0\), and the pointwise Schur-basis bound reads \(h k_N(h)/2\le\|C-C_0\|_1\).
The discarded spectral weights \(H_X,H_Y,H_Z\) have [summable normalized dyadic means](Yin_C_F0365_v1.md#tails).
Before cutting \(Y\) at spectral magnitude three, the conditional expected trace-norm error is bounded by \(C(H_X+H_Z)\sqrt{1+\operatorname{tr}_N(G+M^*M)}\).
The subsequent cut costs at most \(C H_Y\) deterministically.
When the quantity in (4) is at most \(L\), integrate the first estimate conditionally on \(X,Z\) and use the unconditional mean for \(H_Y\).
On its complement use \(k_N(h)/N\le1\).
The two summable bounds give (1).

<a id="polar"></a>
## The mean potential on all dyadic sizes

Let \(\rho_N=N^{-1}\sum_{\operatorname{Im}\lambda\ne0}\delta_\lambda\) and \(\rho_N^{[h]}=\mathbf1_{|\operatorname{Im}\lambda|\ge h}\rho_N\).
For \(m\ge1\) the measure \(\eta_m=\sum_{j\ge1}\mathbb E\rho_{2^j}^{[1/m]}\) has finite total mass by (1).
Thus \(\eta=\sum_{m\ge1}2^{-m}\eta_m/(1+\eta_m(\mathbb C))\) is finite as well.
By the [finite-energy argument for the mean measure](Yin_C_F0358_v4.md#polar), \(E=\{z:\int\log^-|z-w|\,d\eta(w)=+\infty\}\) is a deterministic polar set.
For fixed \(z\notin E\) and any \(m\), Tonelli gives
\[
             \sum_{j\ge1}\mathbb E\int\log^-|z-w|\,d\rho_{2^j}^{[1/m]}(w)<\infty .
\]
When \(z\) is nonreal, take \(1/m<|\operatorname{Im}z|/2\).
The remaining nonreal roots each contribute at most \(\log^-(|\operatorname{Im}z|/2)\), and their total normalized mass tends to zero almost surely by the [real-root count](Yin_C_F0358_v2.md#argument).
The [potential decomposition](Yin_C_F0358_v2.md#loss) writes \(U_N=u+e_N-\int\log^-|z-w|\,d\rho_N(w)\) with \(e_N(z)\to0\) almost surely and gives the full-sequence upper bound.
This proves (2), and subtraction of the [convergent Hermitian comparison](Yin_C_F0358_v3.md#comparison) gives the compressed limit.
To see the stated summability at a fixed \(z\), apply (2) to the coupling of independent dyadic samples.
The events of deviation exceeding a given positive \(\epsilon\) are then independent, so the second Borel--Cantelli lemma forces summability of their one-size probabilities.

<a id="fixed"></a>
## The contribution below a polynomial eigenvalue distance

By (1) at \(h=1/2\), choose increasing \(j_l\) with \(\sum_l j_l\,\mathbb E k_{2^{j_l}}(1/2)/2^{j_l}<\infty\).
Indeed the divergence of \(\sum_j1/j\) implies \(\liminf_j j\,\mathbb E k_{2^j}(1/2)/2^j=0\).
Along these sizes \(k_N(1/2)\log N/N\to0\) almost surely for every coupling.
The contribution of the nonreal roots with \(|\operatorname{Im}\lambda|<1/2\) to the normalized negative log distances at \(i\) is at most \((\log2)\rho_N(\mathbb C)\), which tends to zero almost surely.
For every \(b>0\) cap the negative log distance of each of the remaining roots at \(b\log N\).
Their normalized capped sum is at most \(b k_N(1/2)\log N/N\).
Along the chosen sizes these bounds vanish on an event independent of \(b\).
The excess over this cap is exactly the sum in (3) for large \(N\), because real and shallow roots have distance at least \(1/2\) from \(i\).
The potential decomposition proves (3) with the convention at a zero.
If the indicated probability of a root closer than \(N^{-b}\) tends to zero, extract a further subsequence where these probabilities are summable.
The excess in (3) then vanishes eventually almost surely and the whole-sequence upper bound gives equality at \(i\).

## Current assessment
[Selected decision](#decision-dyadic-strip-reviewed)

## Assessment history

### Decision dyadic-strip-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-18T01:41 |
| status | open |
| reason | A summable quadratic-trace bound upgrades the mean strip counts to all dyadic sizes and isolates the uncapped loss at the prescribed shift. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Dyadic counts and ordinary determinants](#statement) | Arbitrary fixed complex and atomic finite-second-moment inputs and every cross-size coupling. |
| argument | [Weighted finite-mean sums](#weighted) | Uniform summability over admissible weights. |
| support | [Quadratic trace](#guard) | Single-block heavy tails and the variance of cross terms. |
| support | [Mean strip count](#count) | Summable normalized counts in all dyadic sizes. |
| support | [Ordinary dyadic limits](#polar) | A deterministic polar exceptional set for fixed nonreal parameters. |
| support | [Remaining loss at \(i\)](#fixed) | A common subsequence for every fixed polynomial clipping exponent. |

### Decision dyadic-strip-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:48 |
| status | proved |
| reason | A dyadically summable quadratic-trace guard controls the strip mean measures and isolates the remaining sub-polynomial root-distance loss at i. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | A dyadically summable quadratic-trace guard controls the strip mean measures and isolates the remaining sub-polynomial root-distance loss at i. |
| argument | [Complete argument](#weighted) | The hypotheses, parameter scope and conclusions of the fixed proof. |
| review | [Independent whole-proof assessment](../audits/reviews/Yin_R_F0372_v2.md#dyadic-strip-whole-proof) | The stated mathematical scope and remaining restrictions. |
