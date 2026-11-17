---
author: Yin
---

# Summable terminal deviations of the two-sided product for real Wigner inputs with fourth moments

<a id="statement"></a>
## The model and the terminal series

Let \(A_N,B_N\) be two independent real symmetric Wigner matrices of size \(N\).
In each matrix the strict upper entries are independent copies of \(\xi/\sqrt N\) for a fixed centered real law with \(\mathbb E\xi^2=1\) and \(\mathbb E|\xi|^4<\infty\).
The diagonal entries are independent copies of \(\zeta/\sqrt N\) for a fixed centered real law of finite second moment, independent of the strict upper entries.
The two colors may have different laws and all dimensions may be coupled arbitrarily.
Put \(P_N=A_NB_N+2B_NA_N,\ p=ab+2ba\) for free standard semicircular \(a,b\), and \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\).
Order the singular values decreasingly and use \(\log^-x=\max(0,-\log x)\).
For every disk \(\{|z|<R\}\) of fixed positive radius and every \(\epsilon>0\),
\[
 \sum_{N:\,q_N<N}\Pr\left\{\frac1N\int_{|z|<R}
       \sum_{j>N-q_N}\log^-s_j(P_N-zI)\,dA(z)>\epsilon\right\}<\infty .
 \tag{1}
\]
The finite eigenvalue sets may be discarded in the integrals.
For every allowed coupling, the ordinary potentials \(N^{-1}\log|\det(P_N-zI)|\) almost surely converge in local planar \(L^1\) to \(u(z)=\tau\log|p-z|\), and the empirical eigenvalue measures almost surely converge weakly to the Brown measure of \(p\).

In particular the two upper laws may be arbitrary standardized two-point laws.
For probability \(0<p_0<1\) such a law takes \(\sqrt{(1-p_0)/p_0}\) with probability \(p_0\) and \(-\sqrt{p_0/(1-p_0)}\) otherwise, up to an overall sign.
Every fixed centered variance-one law of finite support is also covered, with no common atom or common spacing required between colors.
The proof below uses the [joint tests for sign borders](Yin_C_F0351_v5.md#sign-flag-area) and [paired Schur restoration](Yin_C_F0351_v5.md#paired-sign-restoration) at their deterministic and free-algebraic interfaces.
It supplies the uniform physical-corner and probability estimates for the present laws.

<a id="argument"></a>
<a id="physical-corners"></a>
## Physical corners of the original unbounded minor

Use \(k=2\lfloor\log^3(N+3)/2\rfloor,\ |I|=k,\ J=I^c,\ n=N-k\).
Put \(A_0=A_{JJ}, B_0=B_{JJ}, M_0=A_0 B_0+2B_0 A_0\), with the original \(N^{-1/2}\) scaling.
The flag uses the independent columns of \(\sqrt N B_{JI}\) to delete directions of \(M_0-zI\).
The restorations use the independent rows of \(A_{IJ}\) after \(B,A_{II},A_{JJ}\) have been revealed.
All coordinate colors below are deterministic projections partitioning \(J\) into two halves or four quarters of equal limiting density.

The original pair jointly with these projections has the following fixed-polynomial count convergence.
For any fixed matrix polynomial in the two inputs and the coordinate projections, its expected singular distribution tends weakly to its distribution at a free semicircular pair free from the limiting coordinate algebra.
Indeed for bounded centered raw entries, the [closed-walk calculation with coordinate colors](Yin_C_F0351_v5.md#sign-flag-area) applies.
An edge used just once has zero mean, with independence by site pairs and Wigner color.
The leading tree patterns use each edge twice, so their weights only involve the corresponding strict upper variances.
All other patterns have vanishing normalized weight, including diagonal loops, and \(\sqrt{n/N}\to1\).
For arbitrary finite second moments use the [rank and normalized Hilbert--Schmidt truncation argument](Yin_C_F0186_v4.md#finite-variance-weak) on the Hermitian dilation.
In that argument the centered, raw-truncated colors have variances tending to one.
The normalized mean-square input error tends uniformly to zero with increasing raw cutoff, giving an input difference of small normalized rank plus small operator norm.
Clipping the centered raw-truncated matrices spectrally at a constant greater than 2 costs vanishing normalized rank at each fixed raw cutoff.
Every word comparison in the bounded-norm step and every rank telescope remains valid with any of the deterministic coordinate projections inserted, since they are identical in both evaluations and have norm at most one.
The corresponding bounded free evaluations converge in norm as the truncated standard deviations tend to one.
This proves the expected weak limit including the deterministic colors.
For any fixed polynomial and continuity threshold, a fixed positive deviation of its singular count has probability at most \(C e^{-cn}\) for all sufficiently large \(n\).
Indeed changing one independent upper row group of the original inputs costs bounded rank in that polynomial, giving the [row concentration estimate](Yin_C_F0186_v4.md#row-concentration).

Spectrally clip \(A_0,B_0\) to \([-3,3]\), writing \(A_c,B_c\) for the results and \(M_c=A_c B_c+2B_c A_c\).
For each fixed \(\delta>0\) the sum of the two ranks changed is at most \(\delta n\) outside \(C_\delta e^{-c_\delta n}\), by the one-color count convergence and the support \([-2,2]\) of its limit.
For each fixed polynomial in the clipped pair and the coordinate projections, the same limiting counts with exponentially small fixed deviations follow by comparing the clipped and original polynomial matrices.
The rank cost is at most the sum of the changed ranks times a constant depending on the polynomial.
One can choose \(\delta\) after fixing the polynomial and the desired count margin.
This gives the count concentration without requiring spectral clipping to be rank-Lipschitz under one row replacement.

Take a fixed finite number \(D\) of shifts separated by a fixed positive distance in a compact subset of the open upper half-plane.
For \(T_z=M_0-zI\) use the four kernels
\[
 K_{ab}(z)=\operatorname{sym}(B_0^aT_z^{-1}B_0^b),\qquad
 a,b\in\{0,1\},\qquad \operatorname{sym}X=(X+X^{\mathsf T})/2.
\]
Take the real and imaginary parts entrywise and restrict to corners between distinct coordinate classes.
For the flag one needs only the real parts at \(a=b=0\).
By the [scalar and two-site specializations](Yin_C_F0351_v5.md#paired-sign-restoration), the corresponding free kernels over the shifts and their conjugates are complex-linearly independent modulo scalars.
Thus each unit real combination of the prescribed real and imaginary components is nonscalar.
The [equal-color free corner argument](Yin_C_F0351_v5.md#sign-flag-area) and continuity in measure give \(s,\gamma>0\) for which each such free corner combination has trace at least \(4\gamma\) above singular threshold \(4s\), uniformly in these compact, separated shifts.
The same argument gives uniformly arbitrarily small free mass at the lower singular values of \(M_0-zI\) in the limit.

Here bounded approximants for the physical kernels are obtained by replacing \(B_0\) by \(B_c\) and \(T_z^{-1}\) by \(F_\eta(T_c)\), where \(T_c=M_c-zI\) and \(F_\eta(T)=h_\eta(T^*T)T^*\) for \(h_\eta(x)=1/\max(x,\eta^2)\).
Fix \(\eta>0\) small enough that the total limiting rank cost for the finite family is less than \(\gamma/100\), using small-singular-value counts with slack at \(2\eta\).
The bounded clipped pair permits uniform polynomial approximation of \(F_\eta\) and uniform norm-continuity in the shifts on a compact set.
The clipped polynomial counts just proved yield the lower singular counts for the approximant corners and an upper count below \(\eta\) for \(|T_c|\).
To see uniformity, first use sufficiently fine finite nets for the shifts and coefficient sphere, testing at continuity thresholds inside the available margins at each net point.
Move to nearby points by the common norm-continuity bound for the approximants and the singular-value shift inequality for \(T_c\).
Fixed polynomial approximation errors here are in operator norm and only enter these count estimates.
This reasoning is the [bounded physical-corner transfer](Yin_C_F0351_v5.md#sign-flag-area) with the fixed polynomial counts of \(A_c,B_c\) as its inputs.

For the exact rank comparison, whenever \(T_z\) is invertible,
\[
 \operatorname{rank}(T_z^{-1}-F_\eta(T_c))
 \le \operatorname{rank}(T_z-T_c)+\#\{i:s_i(T_c)<\eta\}.
\]
Multiply the difference by \(T_z\) and use that \(I-T_cF_\eta(T_c)\) vanishes on all left singular directions with singular value at least \(\eta\).
Replacing either outer power of \(B_0\) by \(B_c\) costs at most \(\operatorname{rank}(B_0-B_c)\), irrespective of the sizes of the other factors.
Taking a transpose, entrywise real or imaginary part and a corner changes the rank estimates by at most fixed factors.
The sum of these rank errors can be made smaller than \(\gamma n/10\) by choosing the fixed clipping and count margins above small enough.
By the [flag rank identity](Yin_C_F0351_v5.md#sign-flag-area) and the [paired-extension rank comparison](Yin_C_F0351_v5.md#paired-sign-restoration), all later lifted inverses and their corresponding four kernels add only \(O_D(k)\) to the rank costs.
Consequently on a single old-minor event with complement \(C e^{-cn}\), each family of physical corners throughout all regular steps has bounded approximants \(G_j\), total rank error less than \(\gamma n/5\), and a positive fraction of singular values above a fixed positive threshold in every unit real combination.
The bounded approximants themselves inherit the lower singular counts with slack.
For each realization the spectra of all its successive finite compressions are finite sets.
Fubini excludes their poles on almost every shift tuple for joint-law estimates, also for laws of infinite support.

<a id="border-tests"></a>
## Output spread and disjoint bases for general border laws

We use the two probabilistic steps for a fixed family of real corners \(C_1,\ldots,C_r\) satisfying the preceding estimates; the family size is bounded independently of dimension.
Given independent blocks of iid raw coordinates, Cartesian Cauchy--Schwarz produces independent coordinate differences \(x_i=\xi_i-\xi_i'\).
They are symmetric and nondegenerate for every strict upper law in the statement.
We show that their action on the corners has the same output spread as in the [bounded sign calculation](Yin_C_F0351_v5.md#sign-flag-area).

Choose a constant \(K\) so large that \(\Pr(|x_i|>K)\) is arbitrarily small and the conditional variance on \(|x_i|\le K\) is positive.
Outside probability \(C e^{-cn}\), the set \(T=\{i:|x_i|>K\}\) has fewer than \(\delta n\) members, for any sufficiently small specified \(\delta>0\) after this choice of \(K\).
Condition on \(T\) and the values there, and put \(x_{\rm hi}=1_T x,\ x_{\rm lo}=1_{T^c}x\).
The remaining coordinates of \(x_{\rm lo}\) are independent and bounded, centered by symmetry, and have a common positive conditional variance.
For each output deletion \(S\) of at most \(\alpha n\) coordinates project away those coordinates, all ranges of \((C_j-G_j)^\mathsf T\), and all vectors \(G_j^\mathsf T x_{\rm hi}\).
One may also project away any subspace of bounded dimension fixed before \(x\) is drawn.
Write \(Q_S\) for the resulting projection.
It is fixed under the mask and high-value conditioning.
For every real unit coefficient array \(t\), the map
\[
 Q_S\left(\sum_jt_jG_j^{\mathsf T}\right)1_{T^c}
\]
has at least \(c n\) singular values above a fixed constant.
This follows from the preceding slack and the combined ranks of the domain deletion, output coordinate deletion, error ranges and extra fixed-dimensional spaces, taking \(\delta,\alpha\) small enough.
For clarity the free count and total rank tolerances above can be taken with an arbitrarily large fixed ratio before fixing these two fractions.
The expected squared norm of its value at \(x_{\rm lo}\) is at least \(c'n\) by independence and positive variance.
The [bounded-product convex concentration estimate](Yin_C_F0187_v2.md#argument) applied to this norm gives a lower bound \(c''\sqrt n\) outside \(Ce^{-cn}\).
Its Lipschitz constant is bounded, and integration of the median concentration bound gives bounded second moment about the median, which yields the asserted lower median.
Choose \(\alpha\) small enough to union over all \(S\) within the same exponential rate.
A fixed fine coefficient net extends this to all unit arrays since the truncated vector has norm at most \(K\sqrt n\).
After projection the true linear combination at \(x\) equals the bounded one at \(x_{\rm lo}\).
The resulting lower bound gives the least singular value \(c'''\sqrt n\) for the matrix with rows \(((C_j^\mathsf T x)_i)_j\) after every such output deletion, uniformly over the possible previously fixed subspace.
Here uniformity means an exception bound independent of that subspace for each such conditioning.

The [maximum-volume basis extraction](Yin_C_F0351_v5.md#sign-flag-area) now yields \(L\ge c_r n\) disjoint bases of real output rows \(w_i\), each with least singular value at least \(c_r>0\).
For independent copies \(y_i\) of any fixed nonconstant real random variable \(Y\) these bases imply
\[
 \sup_b\Pr\{\|\textstyle\sum_i y_i w_i-b\|\le1\}\le C L^{-r/2}. \tag{2}
\]
Here is the Fourier estimate for general \(Y\).
Let \(\phi\) be its characteristic function, \(D_0=Y-Y'\) for an independent copy, and choose \(0<d<H\) with \(\rho=\Pr(d\le|D_0|\le H)>0\).
Since \(1-|\phi(t)|^2=2\mathbb E\sin^2(D_0t/2)\), convexity gives, for \(L\ge1\),
\[
 |\phi(t)|^L
 \le \mathbb E\left[\exp\{-L\rho\sin^2(D_0t/2)\}
                     \,\middle|\,d\le|D_0|\le H\right].
\]
Indeed use \((1-v)^{L/2}\le e^{-Lv/2}\), restrict the expectation in \(v\) to the displayed event, then apply Jensen.
For \(Z\) a real standard normal, fixed \(c>0\) and arbitrary \(u\), averaging the right side at \(cZ+u\) costs \(O(L^{-1/2})\).
Condition on \(D_0\): the density of \(D_0(cZ+u)/2\) wrapped modulo \(\pi\) is uniformly bounded for \(d\le|D_0|\le H\), as follows by summing its Gaussian density over periods.
The integral of \(\exp(-L\rho\sin^2 v)\) over one period is \(O(L^{-1/2})\) by the linear lower bound of \(|\sin v|\) near its zeros.
In particular for a law supported at two points with probabilities \(p_0,1-p_0\), one can take a single spacing in this calculation, of difference mass \(2p_0(1-p_0)>0\).
For a finite-support law any two distinct atoms provide a positive difference mass, even if its other spacings are incommensurate.

Use the Gaussian Fourier majorant of the unit ball in the [disjoint-basis proof](Yin_C_F0351_v5.md#sign-flag-area).
After discarding the phase and unused coordinates, apply Hölder with exponent \(L\) across the disjoint bases.
For each basis matrix \(U\), \(UG\) at a standard Gaussian vector \(G\) has covariance dominating \(c_r^2 I\).
Conditioning on its decomposition as an independent Gaussian shift plus \(c_r\) times a standard Gaussian, the preceding one-dimensional estimate in each coordinate gives \(O(L^{-r/2})\) for the expected product of the \(L\)-th powers.
Hölder gives (2).
This includes \(Y=\xi-\xi'\) for either color and any fixed-radius box after a finite covering.

<a id="ratios"></a>
## Deleting hyperplanes and restoring the two physical directions

For the flag, use the previous columns and the original minor as the conditioning and test \(r\) prescribed shifts at a step with fresh raw column \(g\).
Its ratio is \(g^{\mathsf T}R_l(z)g/\|P_{H_l}g\|^2\) in the notation of [the cofactor identity](Yin_C_F0351_v5.md#sign-flag-area).
Column dependence is included in the summable [cross-block exception](Yin_C_F0196_v4.md#statement).
For all \(k\) columns, failure of \(\|g\|\le N^2\) costs \(O(kN^{-3})\) by \(\mathbb E\|g\|^2=n\).
Use, at each tested step, the conjunction of this guard with the ratio events of modulus below \(N^{-7}\), so no conditioning on future columns is required.
The raw quadratic forms then have magnitude at most \(N^{-3}\).
Two Cartesian Cauchy--Schwarz applications to the conjunction isolate the mixed bilinear tests on the differences of the two halves.
The output-spread and disjoint-basis estimates above give a simultaneous small-ball bound \(C n^{-r/2}\) on these differences before taking fourth roots, yielding \(C n^{-r/8}\) for the original tests.
Assign 16 separated bad parameters to steps, multiply the conditional bounds in chronological order and sum over the at most \(k^{16}\) assignments.
The [separated-tuple integration](Yin_C_F0351_v5.md#sign-flag-area) gives a summable probability that the set of shifts on a given disk with some deletion ratio below \(N^{-7}\) has area exceeding any fixed positive tolerance.

For the restorations expose \(B,A_{JJ},A_{II}\) and the earlier \(A_{IJ}\) rows only.
The current fresh \(J\)-row of \(\sqrt N A_{IJ}\) is iid with the actual first upper law.
Use the [paired restoration identity](Yin_C_F0351_v5.md#paired-sign-restoration) for \(F=[e_i,Be_i]\) and its projection \(F_L\) to the new two-dimensional directions in an orthonormal frame.
On the cross-block floor \(s_{\min}(B_{JI})\ge c\) and \(\|B_{II}\|\le N^2\), the least singular value of the full pair map \((h,g)\mapsto(h+B_{II}g,B_{JI}g)\) is at least \(c' N^{-2}\).
Indeed the second component controls \(\|g\|\) and both components together then control \(\|h\|\) with cost \(C(1+\|B_{II}\|)\).
Taking the distance to any later pairs in this bound leaves the same lower bound for \(s_{\min}(F_L)\).
Thus \(\det(F_L^\mathsf T F_L)\ge c''N^{-8}\).
The bound \(\|B_{II}\|\le N^2\) follows outside probability \(O(N^{-3})\) by the expected squared Frobenius norm of \(B\).
These are guards on the already exposed second color.

As a function of the fresh raw row the ratio is degree at most four.
Its quartic is \(4 N^{-2}\det(F_L^\mathsf T F_L)\) times the determinant of the \(2\)-by-\(2\) matrix of quadratic forms with kernels \(\operatorname{sym}(B^a R B^b)\), \(a,b\in\{0,1\}\), for the old lifted inverse \(R\).
All lower-degree terms may be arbitrary given the exposure.
Apply four Cartesian Cauchy--Schwarz steps to the joint events of ratio modulus below \(N^{-12}\).
The sixteen resamplings imply mixed quartic tests of width \(O(N^{-2})\) after division by the raw and geometric factors.
Use the [three-pairing expansion](Yin_C_F0351_v5.md#paired-sign-restoration) in four independent coordinate differences \(u_1,\dots,u_4\).
For an assigned subset of \(s\) shifts where the first-pair \(00\) bilinear coefficient has modulus at most one, condition on \(u_1\) and apply the output-spread bound and (2) to \(u_2\), for probability \(O(n^{-s/2})\).
On each remaining shift this coefficient has modulus above one.
Condition now on \(u_1,u_2\).
The terms using first and second blocks paired with the fourth have their output in a fixed subspace of dimension at most \(16D\) before \(u_3\) is drawn.
In the remaining pairing the real coefficient array for any unit combination of shifts has norm at least one, since its \(11\) component at each shift is multiplied by that shift's first-pair \(00\) coefficient.
Use the full real and imaginary \(34\) kernel family and the extra-subspace form of output spread at \(u_3\), then (2) at \(u_4\).
This bounds the remaining tests by \(O(n^{-(r-s)/2})\), uniformly under this conditioning even when the first-pair coefficients are arbitrarily large.
Summing over the subsets and taking the sixteenth root gives \(C n^{-r/32}\).
Use 64 separated shifts as in the flag integration.
The probability that a set of shifts of area exceeding any fixed positive tolerance contains restoration failures in the sense that each such shift has some ratio below \(N^{-12}\) is bounded by \(C k^{64}n^{-2}\) and the summable guard errors.

<a id="terminal"></a>
## The original-law trims and the planar conclusion

The original-law inputs to the [trim comparison](Yin_C_F0351_v5.md#trim-assembly) are available throughout the stated real fourth-moment upper and second-moment diagonal model.
In particular the [two-trim limit](Yin_C_F0351_v1.md#minor-trims) holds for the slightly rescaled old principal minor, and the [first-column arithmetic overlap estimate](Yin_C_F0351_v2.md#discrete-overlaps) uses any nondegenerate real strict upper law under these moments.
The latter supplies the summable fixed-parameter errors through the old minor's adaptively chosen singular gap, uniformly on compact regions separated from the real axis.
The starting restoration is exactly the final flag compression, by orthogonality to the columns of \(B_{JI}\).
After the initial arithmetic overlaps, the total cost of all later ratios on the good sections is at most \(19 k\log N\).
This is \(o(N)\), and the areas of the bad sections tend to zero almost surely under each coupling.

More explicitly, if \(h=q_n\), \(t_1\le\cdots\le t_n\) are the singular values of \(M_0-zI\), and \(b_j=N^{-1}\sum_{i>j}\log t_i\), the good-set lower bound is
\[
 N^{-1}\log|\det(P_N-zI)|\ge b_{2h}-(2h/N)\log^-t_{2h+1}-o(1).
\]
The two-trim limit gives \(b_{2h}\to u\) in local \(L^1\) and \(\int_D(h/N)\log^-t_{2h+1}\to0\) on each bounded disk \(D\).
The normalized full characteristic logarithm has negative part bounded in local \(L^2\) uniformly in every realization, by Jensen on the translated planar logs of its eigenvalues.
The free potential also belongs to local \(L^2\).
Cauchy--Schwarz therefore treats the bad areas and a vanishing strip around the real axis, first considering countably many regions a positive distance from that axis.
For the upper comparison the [full-matrix trimmed theorem](Yin_C_F0186_v36.md#statement) gives the matching local \(L^1\) limit of the retained logs.
Almost surely eventually \(\|A_N\|,\|B_N\|\le N^2\) by Frobenius Markov bounds with summable failures, so the \(q_N\) omitted positive logarithms divided by \(N\) are \(o(1)\) uniformly on each disk.
This gives the local \(L^1\) limit of the full potential and the weak Brown limit by distributional Laplacians and tightness.
Applying the [terminal equivalence](Yin_C_F0186_v36.md#statement) to independent dimensions gives (1) for the original marginals.
These estimates control the planar terminal series for the specified polynomial.
They leave the almost-sure weak limit for general polynomials and the finite-second-moment upper-law case of [F0012](../tasks/Yin_T_F0012_v3.md#contract) open.

## Current assessment
[Selected decision](#decision-fourth-terminal-reviewed)

## Assessment history

### Decision fourth-terminal-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:14 |
| status | open |
| reason | The general-border concentration and rank comparison supply a complete candidate proof for the real fourth-moment model. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original-law limits](#statement) | The terminal series and arbitrary-coupling Brown limit, including biased signs and finite supports. |
| argument | [Physical corner transfer](#argument) | Spectral clipping, rank control and the finitely many original-law kernel families. |
| support | [Border distributions](#border-tests) | Conditional low-coordinate spread and the Fourier bound for any nonconstant real law. |
| support | [Determinant ratios](#ratios) | Successive quadratic and quartic tests with polynomial guards. |
| support | [Logarithmic assembly](#terminal) | Original-law arithmetic overlaps, trims and the planar terminal comparison. |

### Decision fourth-terminal-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:24 |
| status | proved |
| reason | Independent whole-proof review confirmed the generalized border and physical-corner estimates and the terminal series for all stated real fourth-moment strict upper laws. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Real upper laws and terminal limits](#statement) | The two normalized Wigner laws may differ and may have finite support or unbounded support. |
| argument | [Complete argument](#argument) | Actual-law physical corner transfer, simultaneous sign-difference estimates and removal of the terminal trim. |
| support | [Genuine principal minor](#physical-corners) | Rank approximation under the original input laws. |
| support | [Conditional border estimates](#border-tests) | Large coordinates, disjoint bases and Fourier averaging. |
| support | [Deletion and restoration](#ratios) | Simultaneous tests for the true Schur factors. |
| support | [Terminal series](#terminal) | Integrated deviations and all-coupling Brown convergence. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0358_v6.md#fourth-terminal-whole-proof) | The full two-law statement, including unequal atom probabilities and arbitrary finite supports. |
