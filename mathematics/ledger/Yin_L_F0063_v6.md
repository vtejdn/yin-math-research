---
author: Yin
---

<a id="extreme-pole-definite-background-test"></a>
# Extreme actual inverse poles against a definite residual background

This ordinary development for Yin, dated 2026-11-06T10:05 UTC, continues the free-gap probability investigation for [F13](../tasks/Yin_T_F0013_v1.md#contract).
It tests whether the very largest single inverse poles necessarily require the unresolved complete-coefficient argument from [L63v5](Yin_L_F0063_v5.md#complete-pole-next-interface).
On the same actual-minor setup, a definite residual background permits a direct complete-polynomial estimate for either pole sign once its magnitude exceeds a fixed multiple of \(N^4\).
In particular this includes the same-sign extreme poles that were outside the earlier sign-coercivity argument.
The result is an original-law probability bound intersected with an explicit minor branch, not a proof that the branch covers the actual free-gap model.
The remaining same-sign single-pole resonance is restricted to a polynomial range of pole magnitudes; indefinite backgrounds and multiple strong poles remain separate.
This is ordinary exploration and authoring self-checking, without independent review or a new Claim assessment.

<a id="actual-model-and-event"></a>
## Actual model, conditioning and the event being tested

Use exactly the [real size-three positive-frame free-gap model](Yin_L_F0063_v4.md#model), with original fixed centered variance-one off-diagonal laws and centered finite-second-moment diagonal laws, arbitrary cross-size coupling, one common deterministic real shift tending to zero and a fixed physical deletion bound.
The exposed minor has physical size \(n=N-O(1)\) and the original \(N^{-1/2}\) normalization.
For the actual minor-measurable decomposition, retain
\[
 Z=M^{-1}=E+\lambda ee^T,\qquad
 Ee=0,\quad \|e\|=1,\quad
 \frac{\|E\|_F^2}{N}\le K,
 \tag{Extreme-pole-decomposition}
\]
where \(K\ge1\) is fixed, \(E\) is real symmetric, \(e\) is a real inverse eigenvector and \(\lambda\) is its signed real inverse eigenvalue.
The sigma-field \(\mathcal F\) contains the actual retained input minors and exposed original diagonal coordinates; the original border remains independent of it with its original laws.
Use the [L63v5 definitions and complete identity](Yin_L_F0063_v5.md#strong-pole-complete-polynomial-test)
\[
 \begin{gathered}
 S_E=A_0+\theta_NI_3+D_i-R^TER,
 \qquad z=\sqrt N\,R^Te,\\
 S=S_E-\frac\lambda Nzz^T,
 \qquad \Gamma_E=I_3+R^TE^2R,\\
 \Gamma=\Gamma_E+\frac{\lambda^2}{N}zz^T,
 \qquad F=\Gamma^{-1/2}S.
 \end{gathered}
 \tag{Extreme-pole-complete-objects}
\]
Here \(F\) is the actual normalized graph block, not a frozen quadratic approximation.

The measurable branch includes the actual-minor rectangle event, its norm guard \(B_0\sqrt N\), and the good-background and exposed-diagonal events of L63v5.
Consequently its measurable matrix \(B=B_E+D_i\) and fixed constants \(b,C_K>0\) satisfy
\[
 s_{\min}(B)\ge b,\qquad \|B\|\le C_K,
 \qquad
 \mathbb E[\|S_E-B\|\mid\mathcal F]\le q_N(K)\longrightarrow0.
 \tag{Extreme-pole-residual-input}
\]
Impose the additional measurable condition that \(B\) is definite: there is \(\sigma\in\{-1,1\}\) with \(\sigma B\succeq bI_3\).
No relation between \(\sigma\) and the sign of \(\lambda\) is assumed.
Definiteness is not asserted for every free-gap background.

For any one fixed real unit auxiliary direction \(a\), the [original-law linear estimate](Yin_L_F0063_v5.md#opposite-sign-complete-schur) gives fixed \(c_3,c,C>0\) such that
\[
 \mathbb P\{|a^Tz|\le c_3N^{-3/2}\mid\mathcal F\}
 \le Ce^{-cN}+C\sqrt{\log N}\,N^{-1/5}.
 \tag{Extreme-pole-linear-input}
\]
Its hypotheses use the actual-minor rectangle and norm events and \(|\lambda|\ge c_0N\), but do not use the opposite-sign condition imposed later in that earlier calculation.
The magnitude assumption below is stronger and supplies that eigenvector-residual threshold for all sufficiently large \(N\).
This input is obtained from the original scalar laws by two-copy pairing and the degree-one MNV estimate; no moment above two or fresh-row event is inserted into \(\mathcal F\).
Also, with \(\Lambda=\sum_j\|A_j\|^2\), the original second moments give
\[
 \mathbb E[\operatorname{Tr}\Gamma_E\mid\mathcal F]
 \le 3+\Lambda K.
 \tag{Extreme-pole-graph-moment}
\]

<a id="complete-extreme-pole-bound"></a>
## The complete determinant and graph scale

Put \(C_*=C_K+b/2\) and choose a fixed \(\Lambda_0>2C_*/c_3^2\).
Further restrict the measurable branch to
\[
 |\lambda|\ge\Lambda_0N^4.
 \tag{Extreme-pole-magnitude}
\]
Intersect, without conditioning on, the three fresh-row events
\[
 \|S_E-B\|\le b/2,\qquad
 |a^Tz|>c_3N^{-3/2},\qquad
 \operatorname{Tr}\Gamma_E\le N.
 \tag{Extreme-pole-fresh-events}
\]
Their complementary conditional probability is at most
\[
 \beta_N:=\frac{2q_N(K)}b+Ce^{-cN}
       +C\sqrt{\log N}\,N^{-1/5}
       +\frac{3+\Lambda K}{N}\longrightarrow0.
 \tag{Extreme-pole-error}
\]
The first and third errors are Markov bounds, and the second is (Extreme-pole-linear-input).

On these events \(S_E\) is definite with the same sign as \(B\), its least singular value is at least \(b/2\), and \(\|S_E\|\le C_*\).
Writing \(r=\|z\|\) and \(q=z^TS_E^{-1}z\), one has
\[
 r>c_3N^{-3/2},\qquad
 |q|\ge r^2/C_*,\qquad
 \operatorname{sgn}(q)=\sigma,
 \qquad
 \left|\frac\lambda Nq\right|>2.
 \tag{Extreme-pole-no-resonance}
\]
For real \(x\) with \(|x|>2\), \(|1-x|\ge|x|/2\), whether \(x\) is positive or negative.
The exact matrix determinant lemma therefore gives
\[
 \begin{split}
 |\det S|
 &=|\det S_E|\left|1-\frac\lambda Nq\right|\\
 &\ge \frac{b^3}{16C_*}\,\frac{|\lambda|r^2}{N}.
 \end{split}
 \tag{Extreme-pole-full-numerator}
\]
This treats the full original-row Schur polynomial, including all residual-dependent terms.
The only use of \(S_E-B\) is fixed-tolerance definiteness and boundedness; no rate allowing a shrinking-window proxy comparison is needed.

The exact rank-one graph identity in dimension three yields
\[
 \det\Gamma=\det\Gamma_E
       +\frac{\lambda^2}{N}z^T\operatorname{adj}(\Gamma_E)z.
 \tag{Extreme-pole-exact-graph}
\]
Since \(\Gamma_E\) is positive definite and \(\operatorname{Tr}\Gamma_E\le N\), one has \(\det\Gamma_E\le N^3\) and \(\|\operatorname{adj}(\Gamma_E)\|\le N^2\).
Consequently
\[
 \sqrt{\det\Gamma}
 \le N^{3/2}+|\lambda|\sqrt N\,r
 \le 2|\lambda|\sqrt N\,r
 \tag{Extreme-pole-graph-upper}
\]
for all sufficiently large \(N\), because \(|\lambda|r\ge\Lambda_0c_3N^{5/2}\ge N\).
Combining the exact numerator and denominator gives a fixed \(c_*>0\) such that
\[
 |\det F|=\frac{|\det S|}{\sqrt{\det\Gamma}}
 \ge\frac{b^3}{32C_*}\frac r{N^{3/2}}
 >c_*N^{-3}.
 \tag{Extreme-pole-normalized-determinant}
\]
The cancellation of \(|\lambda|\) is exact at this estimate, and there is no upper bound on the pole magnitude.
Thus, uniformly over good actual conditionings in this branch,
\[
 \mathbb P\{|\det F|\le c_*N^{-3}\mid\mathcal F\}
 \le\beta_N.
 \tag{Extreme-pole-complete-probability}
\]

On the additional full-parent norm event \(\|L_{\rm parent}^{\theta}\|\le B_0\sqrt N\), the actual graph compression has \(\|F\|\le B_0\sqrt N\).
It follows from \(|\det F|\le s_{\min}(F)\|F\|^2\) that
\[
 \mathbb P\left\{s_{\min}(F)\le c_*B_0^{-2}N^{-4},\quad
       \|L_{\rm parent}^{\theta}\|\le B_0\sqrt N
       \,\middle|\,\mathcal F\right\}\le\beta_N.
 \tag{Extreme-pole-distance-intersection}
\]
The full-parent norm event is only intersected with the bad-distance event; it is not part of the conditioning.

<a id="actual-average-and-remaining-probability"></a>
## The actual probability contribution and what remains

Let \(\mathcal H_{T,i,N}\) be the actual minor-and-diagonal measurable branch just specified, including definiteness and (Extreme-pole-magnitude).
Integrating the conditional estimate gives
\[
 \mathbb P\{\mathcal H_{T,i,N},\ |\det F_{T,i,N}|\le c_*N^{-3}\}
 \le\beta_N\mathbb P(\mathcal H_{T,i,N})\le\beta_N.
 \tag{Extreme-pole-original-law-intersection}
\]
The same holds for the distance-and-parent-norm intersection, uniformly over the fixed deletion range and the removed physical index.
In particular averaging these intersections over the physical index has error at most \(\beta_N\), with no factor \(N\) and no reconditioning by the probability of the branch.
This is a bound for an actual-model event, although it does not estimate the complementary branch probability.

For a definite stable background, the earlier [opposite-sign calculation](Yin_L_F0063_v5.md#opposite-sign-complete-schur) handles every strong single pole of that sign, and the present calculation handles both signs above \(\Lambda_0N^4\).
Within the same single-pole setup, the remaining same-sign resonance therefore lies in
\[
 c_0N\le |\lambda|<\Lambda_0N^4.
 \tag{Extreme-pole-remaining-band}
\]
The restriction does not supply the complete-coefficient estimate on that band, prove that a single pole is typical, or treat an indefinite \(B\) or several strong poles.
The [finite-variance pairing obstruction](Yin_L_F0063_v5.md#paired-coefficient-l2-obstruction) still prevents assuming a finite untruncated squared coefficient average in those remaining tests.

The bounded attempt to derive the total negative-logarithmic loss from deleting large original coordinates found no new unconditional implication.
The adequate existing [favorable dimensional subsequence argument](../drafts/Yin_D_F0033.md#favorable-subsequence-tail-rank) already gives the vanishing rank-times-log error under the actual finite-second-moment laws and every cross-size coupling.
Its transfer applies to clipped logarithms; removing the lower clipping still needs control of the extreme singular values of both outputs, and its truncated laws vary with dimension.
The [actual vanishing-entry example](../drafts/Yin_D_F0010.md#vanishing-entry-truncation-norm-obstruction) also shows that the truncated operator norm can diverge along that same favorable subsequence.
Neither the new single-pole intersection estimate nor those existing truncation controls prove the actual inverse-tail or total-negative-log-loss probability required for the full free-gap branch.
The next discriminating work is the actual probability or complete-polynomial behavior of the remaining same-sign band, indefinite backgrounds and multiple strong poles, or a direct total-loss estimate bypassing that decomposition.
