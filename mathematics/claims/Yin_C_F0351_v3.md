---
author: Yin
---

# Pointwise trimmed and ordinary logarithms at nonreal shifts of the Wigner quadratic product

<a id="statement"></a>
## Stable fixed-shift limits

Let \(P_N=A_NB_N+2B_NA_N\) in the [real fourth off-diagonal and second diagonal moment model](Yin_C_F0186_v26.md#statement), \(u(z)=\tau\log|s_1s_2+2s_2s_1-z|\), and \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\).
Write \(p_j(T)\) for the product of the \(j\) largest singular values.
For any prescribed deterministic sequence \(z_N\to z\in\mathbb C\setminus\mathbb R\), either \(s_N=q_N\) or \(s_N=2q_N\), and every allowed coupling,
\[
  \frac1N\log p_{N-s_N}(P_N-z_N I)\longrightarrow u(z)
  \quad\text{almost surely}.
\]
The same holds for the leading \(3N-s_N\) singular values of the companion with the original denominator \(N\).
The free potential \(u\) is continuous off the real axis.

If in addition both strict upper laws have the [regular components of C351v2](Yin_C_F0351_v2.md#statement), then
\[
 X_N(z_N)=\frac1N\log|\det(P_N-z_NI)|\longrightarrow u(z)\quad\text{almost surely}
\]
under every allowed coupling.
For each compact \(K\subset\mathbb C\setminus\mathbb R\) and \(\varepsilon>0\),
\[
 \sum_N\sup_{w\in K}\Pr\{|X_N(w)-u(w)|>\varepsilon\}<\infty .
 \tag{Marginal}
\]
In particular the [F0014 upper-limit question](../tasks/Yin_T_F0014_v1.md#contract) has a full-sequence affirmative answer at every fixed nonreal parameter for this polynomial and these component laws.
The supremum in (Marginal) is over individual probabilities.
The trimmed versions obey the same marginal estimate under the original fourth-moment assumptions alone.

<a id="argument"></a>
## Starting from a fixed fraction

Fix \(z_N\to z\notin\mathbb R\) and \(a\in(9/10,1)\).
Use the [three-channel companion, border bound and rank guard](Yin_C_F0186_v36.md#one-step) along the nested physical sites of a size-\(N\) sample, retaining the size-\(N\) normalization at each step.
Let \(n=\lfloor aN\rfloor\), \(m=N-n\), \(a_N=n/N\), \(q_0=3m+s_N\), \(r_0=3n-q_0\).
The [initial scaling identity](Yin_C_F0186_v36.md#initial-product) gives \(L_n(z_N)=S L_n^{\rm can}(z_N/a_N) S\) for \(S=\operatorname{diag}(\sqrt{a_N}I_n,I_n,I_n)\).
Each ordinal singular value of the physical old companion is at least \(a_N\) times its canonical counterpart.

The canonical parameter tends to \(w=z/a\).
The empirical singular measures of the canonical companion converge weakly almost surely to its free singular measure at \(w\), by the [finite-variance weak law](Yin_C_F0186_v4.md#finite-variance-weak) and the singular-value perturbation bound for the shift.
Each canonical dimension occurs at most twice for large \(N\), so the every-coupling result applies to each of two deterministic injective subsequences after extending missing dimensions if needed.
The free normalized logarithm is \(u(w)/3\) by [the Schur identity and finite free logarithm](Yin_C_F0186_v36.md#initial-product).
In particular there is no zero atom.
For this fixed \(a\), choose a continuity point \(0<b<1\) with free mass in \([0,b]\) strictly less than \((1-a)/a\).
Almost surely eventually the finite count below or at \(b\) is at most \(q_0\).
The \(r_0\) top values are consequently unclipped in the test \(\log\max(t,b)\).
The mean of this test converges to its free integral using the [pathwise positive-tail bound](Yin_C_F0186_v4.md#log-statistics).
This includes the convergent moving shift, by the fixed-cutoff Lipschitz estimate.
The free integral is at least \(u(w)/3\).

A single deterministic constant \(C\), independent of \(a\in(9/10,1)\), bounds the positive logarithm of each omitted canonical singular value eventually on the convergence event for this \(a\).
Indeed \(q_0<3n/2\) for large \(N\), so these values are bounded by a median from the bottom.
Weak convergence places that median below any constant strictly larger than the free operator norm.
The free companion norms are bounded uniformly for \(w=z/a\) in this interval.
In a countable sequence of choices of \(a\) take the intersection of their probability-one events.
We obtain
\[
 \liminf_N N^{-1}\log p_{r_0}(L_n(z_N))
 \ge a\,u(z/a)-3C(1-a)+3\log a .
\]
Here the scaling loss \(r_0\log a_N/N\) is at least \(3\log a_N\).

<a id="border-cost"></a>
## Total cost of a positive fraction of borders

Apply the [summable border estimates](Yin_C_F0186_v36.md#rank-loss) at the deterministic parameters \(z_N\), which eventually belong to a compact set separated from the real axis.
The constants depend on this set and the laws, uniformly for the specified chain and all \(a\in(9/10,1)\).
At stage \(j\), \(0\le j<m\), the retained index increases by six and the deficit is \(3(m-j)+s_N\).
Each step lower-bounds its new product by its preceding product times \(c((3(m-j)+s_N)/N)^3\).
All steps succeed eventually almost surely for the fixed \(a\), since \(s_N/\log N\to\infty\).
The normalized logarithmic cost is bounded above by
\[
 \frac{m}{N}|\log c|+\frac{3}{N}\sum_{i=1}^m \log(N/i)
 \le \frac{m}{N}\big(|\log c|+3+3\log(N/m)\big)
\]
by \(\log(m!)\ge m\log m-m\).
Thus the cost tends to zero in the successive limits \(N\to\infty\), \(a\uparrow1\).

There exists a deterministic sequence \(a\uparrow1\) for which \(u(z/a)\to u(z)\).
To check this without a continuity assumption, write \(u\) as the logarithmic potential of its compactly supported Brown probability measure \(\mu\), finite at \(z\).
The average of \(u(tz)\) for \(1\le t\le1+\epsilon\) tends to \(u(z)\).
For \(|w-z|>2\epsilon|z|\) the average negative logarithm of \(|tz-w|\) is at most \(\log^-|z-w|+\log2\).
For \(|w-z|\le2\epsilon|z|\), the proportion of the segment in a radius-\(b\) disk about \(w\) is at most \(\min(1,2b/(\epsilon|z|))\).
Layer integration bounds the average negative logarithm by \(\log^-(\epsilon|z|)+C\le\log^-|z-w|+C'\).
These bounds are \(\mu\)-integrable, and for \(w\ne z\) the kernel averages converge.
The positive logarithms are uniformly bounded on the compact support.
Dominated convergence proves the average assertion, and upper semicontinuity of \(u\) supplies the claimed good sequence.
The initial lower bound and total cost now give the companion lower limit \(u(z)\).
For the upper limit use the full regularized companion logarithm at fixed regularizer, paying \(s_N|\log b|/N\) to omit the last terms at a lower clip \(b\).
Weak convergence, positive-log control and the fixed-regularizer Lipschitz shift bound give the free regularized limit, which decreases to \(u(z)\) at the original normalization.
This proves the companion conclusion.

The [unit triangular Schur factors](Yin_C_F0186_v36.md#final-product) give the scalar conclusion pointwise, including a singular untrimmed matrix.
For an invertible \(d\)-square factor \(F\) with \(|\det F|=1\), one has \(p_{d-s}(F)=p_s(F^{-1})\le\|F^{-1}\|^s\).
Exterior multiplication in both directions therefore changes the retained log product by at most \(O(s_N\log N)\) on the eventual polynomial norm guard for the factors and their inverses.
The diagonal middle matrix appends \(2N\) unit singular values to the original \(N\).
Replacing its omitted \(s_N\) values by the bottom \(s_N\) of the scalar matrix changes only omitted positive logs, bounded by the same \(O(s_N\log N)\) cost.
If there are more than \(s_N\) exact zeros both retained products vanish, and the companion lower limit shows that this case is eventually absent.

<a id="fixed-compressions"></a>
## Removing the trim under the component hypotheses

Keep the polylogarithmic exterior \(n=N-k\) and \(h=q_n\) of [C351v2](Yin_C_F0351_v2.md#argument), write \(M\) for its uncompressed minor output, and \(t_1\le\cdots\le t_n\) for the singular values of \(M-wI\).
For each \(w\) in a fixed compact set away from the real axis, the estimates of [the gap proof](Yin_C_F0351_v1.md#adaptive-gap), [the arithmetic and quadratic column tests](Yin_C_F0351_v2.md#discrete-overlaps) and [the interior matching](Yin_C_F0351_v2.md#interior) give
\[
 |\det(P_N-wI)|\ge e^{-N e_N} p_{n-2h}(M-wI)\,\min(1,t_{2h+1})^{2h}
 \tag{Product}
\]
outside a marginal event of probability at most \(b_N\), where \(e_N\to0\) and \(\sum b_N<\infty\) uniformly over this compact set.
Indeed the deterministic costs are \(O(h^3\log N+kN^\theta+k\log N)\) before division by \(N\), with \(1/d<\theta<1\) as in C351v2.
C351v2 first proves the bound for planar almost every \(w\) to permit division at intermediate stages.
In (Product) both sides are continuous in \(w\) for each realized sample, since ordered singular values are continuous.
For an arbitrary prescribed \(w\) approach it through the deterministic full-area set inside a slightly larger compact neighborhood off the real axis.
The indicator of strict violation at \(w\) is bounded by the lower limit of the violation indicators along the sequence.
Fatou's lemma retains the same \(b_N\) at every prescribed \(w\), including exceptional finite eigenvalues.
No intermediate division at that point is required.

For \(w=z_N\), use first Borel--Cantelli.
Both old-minor trims \(h,2h\) converge to \(u(z)\) after normalized logarithms by the first part, since the old matrix equals \((n/N)P_n^{\rm can}\), the canonical shifts tend to \(z\), and the canonical dimensions have bounded multiplicity as in [C351v1](Yin_C_F0351_v1.md#minor-trims).
Furthermore \(h\log^-t_{2h+1}/N\to0\) by subtracting those two trims and using \(h\log N/N\to0\) on the norm guard, as in the last inequality of that same proof.
Consequently (Product) gives \(\liminf X_N(z_N)\ge u(z)\) almost surely.
The regularized upper bound in [C186v4](Yin_C_F0186_v4.md#regularized-potentials) at fixed regularizer and its locally uniform shift control give the reverse upper bound.

<a id="uniform-marginals"></a>
## Continuity and marginal summability

For any one of the preceding statistics \(Y_N\) under its stated assumptions we have proved \(Y_N(z_N)\to u(z)\) almost surely for every deterministic \(z_N\to z\) off the real axis.
In particular the convergence holds in probability.
Given \(w_j\to w\), choose deterministic \(N_j\) increasing so that \(\Pr(|Y_{N_j}(w_j)-u(w_j)|>1/j)<1/j\).
Extend the sequence of parameters by \(w\) at other indices and use the moving-parameter conclusion to deduce \(u(w_j)\to u(w)\).

Suppose (Marginal) fails and choose \(w_N\in K\) with deviation probability at least half the supremum whenever it is positive.
Divide the compact parameter set into finitely many pieces of diameter at most one and keep one with infinite total deviation probability.
Repeat inside its closure with diameters tending to zero, retaining an infinite tail sum at each stage, using nested compact covers.
By selecting successively disjoint finite index blocks of mass at least one in those nested sets, obtain a deterministic subsequence with divergent sum and \(w_{N_j}\to w\in K\).
Realize independent dimensions, so the second Borel--Cantelli lemma gives infinitely many deviations along it almost surely.
The moving-parameter limit and continuity of \(u\) rule this out.
This proves the summability assertion without selecting an event simultaneous over all shifts.

## Current assessment
[Selected decision](#decision-moving-shifts-reviewed)

## Assessment history

### Decision pointwise-trim-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:36 |
| status | open |
| reason | The fixed-fraction initialization supplies a moving-shift terminal comparison for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Pointwise limits](#statement) | Trimmed original-law and untrimmed component-law conclusions off the real axis. |
| argument | [Proof](#argument) | Initial normalization, total border cost, radial averaging, compression comparison and uniform marginal summability. |

### Decision moving-shifts-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:40 |
| status | proved |
| reason | Independent whole-proof review verified fixed-fraction initialization, stability at moving nonreal parameters and summable marginal deviations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete fixed statement and quantifiers. |
| argument | [Proof](#argument) | Complete fixed mathematical argument. |
| support | [Accumulated border costs and radial means](#border-cost) | Accumulated border costs and radial means. |
| support | [Fixed-shift transfer for the two original component laws](#fixed-compressions) | Fixed-shift transfer for the two original component laws. |
| support | [Compact uniformity of the sums of marginal deviations](#uniform-marginals) | Compact uniformity of the sums of marginal deviations. |
| dependency | [Original-law summable paired growth on a compact off the real axis](Yin_C_F0186_v36.md#rank-loss) | Original-law summable paired growth on a compact off the real axis. |
| dependency | [One-sided transfer with a uniform per-parameter failure envelope](Yin_C_F0351_v2.md#interior) | One-sided transfer with a uniform per-parameter failure envelope. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0358_v3.md#moving-shifts-whole-proof) | All stated conclusions at the specified scope. |
