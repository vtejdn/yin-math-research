---
author: Yin
---

# Terminal logarithmic loss for the real quadratic Wigner polynomial

The [trimmed potential calculation](../claims/Yin_C_F0186_v36.md#statement) treats \(P_N=A_NB_N+2B_NA_N\) under real fourth off-diagonal and second diagonal moments.
Its [paired step](../claims/Yin_C_F0186_v36.md#one-step), [rank comparison](../claims/Yin_C_F0186_v36.md#rank-loss) and [initial normalization](../claims/Yin_C_F0186_v36.md#initial-product) supply the singular product above the last \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\) values.
The underlying projection estimate is fixed in [C347](../claims/Yin_C_F0347_v1.md#statement).
The remaining investigation concerns the frequency and planar size of the bad sets of these last factors under the original entry law.

<a id="one-step"></a>
<a id="rank-loss"></a>
The [fixed one-step and truncation proofs](../claims/Yin_C_F0186_v36.md#one-step) include the actual shared borders and the fourth-moment sparse-graph comparison.
The earlier power-scale cutoff from [C198](../claims/Yin_C_F0198_v1.md#sparse-truncation) gives \(O(N^\beta)\) terminal factors for each fixed \(\beta>0\) by taking its altered-entry rank \(o(N^\beta)\).
The logarithmic rank estimate uses the actual medium-entry graph.

<a id="terminal-area"></a>
## A test using the area of an extreme sublevel set

On a disk \(K\) write \(Y_N=N^{-1}\sum_{j>N-q_N}\log^-s_j(P_N-z)\), with arbitrary finite values at the eigenvalues.
Under every allowed coupling, almost surely \(\sup_N\|Y_N\|_{L^2(K)}<\infty\).
Indeed \(Y_N\) is bounded above by the negative logarithmic sum over all singular values, divided by \(N\).
The latter equals the positive logarithmic sum minus the actual eigenvalue potential.
The positive sum is uniformly bounded on \(K\) eventually by the [positive tail estimate](../claims/Yin_C_F0186_v4.md#log-statistics) at zero and \(s_j(P_N-zI)\le s_j(P_N)+|z|\).
The potential is uniformly bounded in planar \(L^2(K)\) on the [pathwise control event](../claims/Yin_C_F0186_v4.md#noncompact-planar).
The finitely many initial matrix potentials are locally square integrable.

Thus the terminal condition of C186v36 is equivalent to requiring, for every integer-radius disk and all rational \(\varepsilon,\delta>0\),
\[
 \sum_N\Pr\big\{\,|\{z\in K:Y_N(z)>\varepsilon\}|>\delta\,\big\}<\infty ,
\]
where the inner absolute value denotes planar area.
In fact on the common control event convergence in area of \(Y_N\) to zero is equivalent to convergence of its integral to zero, by Cauchy--Schwarz on the exceptional set and Markov's inequality in the other direction.
Use first Borel--Cantelli for arbitrary coupling and second Borel--Cantelli for the independent coupling to obtain the complete-convergence formulation.

A sufficient estimate involving only the least singular value is
\[
 \sum_N\Pr\Big\{\,\big|\{z\in K:
    s_{\min}(P_N-zI)<\exp(-\varepsilon N/q_N)\}\big|>\delta\,\Big\}<\infty .
\]
Indeed \(Y_N(z)\le(q_N/N)\log^-s_{\min}(P_N-zI)\).
A summable bound for the expected area of this sublevel set would imply the displayed estimate, but the threshold permits a much smaller singular value than a polynomial floor.
The [single exceptional chain](../ledger/Yin_L_F0067_v3.md#terminal-loss) shows how an order-one disk loss can survive a floor whose failure probability merely tends to zero.
The [mixed-law compression theorem](../claims/Yin_C_F0351_v2.md#decision-mixed-components-reviewed) proves terminal summability under its component hypotheses, and the [fine-grid argument](../claims/Yin_C_F0351_v4.md#dyadic-example) includes fixed countably supported laws.
The [finite-support investigation](Yin_D_F0044.md) treats the remaining terminal tests, including the interior coefficient on the sign cube and restrictions on the first physical minor.
