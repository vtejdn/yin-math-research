---
author: Yin
---

# Summable terminal losses for two real Wigner laws with regular components

<a id="statement"></a>
## Brown convergence and terminal probabilities

Use independent real symmetric Wigner matrices \(A_N,B_N\) as in [the fourth-moment model](Yin_C_F0186_v26.md#statement), with finite fourth moments for the two centered variance-one raw strict upper laws, arbitrary centered finite-second-moment diagonal laws, and arbitrary coupling across dimensions.
Set \(P_N=A_NB_N+2B_NA_N\) and \(P=s_1s_2+2s_2s_1\).
Suppose that each strict upper law can be written \(p_i\nu_i+(1-p_i)\eta_i\), with fixed \(p_i>0\), \(p_i\le1\).
For some \(d>1\), suppose both component laws satisfy
\[
 Q_{\nu_i}(e^{-t})\le C_i t^{-d}\qquad(t\ge1),\qquad
 Q_\nu(a)=\sup_{x\in\mathbb R}\nu([x-a,x+a]).
\]
The residual laws can be atomic.
Every raw law with a nonzero absolutely continuous component admits such a choice by restricting its density to a positive-mass subset where it is bounded.

Under every cross-dimensional coupling the empirical eigenvalue measures of \(P_N\) converge weakly almost surely to the Brown measure of \(P\).
For \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\), decreasing singular values, every disk \(D_R=\{|z|<R\}\) of fixed integer radius and every \(v>0\),
\[
 \sum_{N\ {\rm large}}
 \Pr\!\left\{\frac1N\int_{D_R}\sum_{j>N-q_N}\log^-s_j(P_N-zI)\,dA(z)>v\right\}<\infty .
\]
Assign any finite values on the finite eigenvalue set when taking the planar integral.

The first projection step below applies to every original nondegenerate strict upper law, including a law supported at two points.
The later projection step and the interior determinant comparison use the respective positive-mass components.

<a id="argument"></a>
## The original cross block

Choose \(1/d<\theta<1\) and put \(T_N=N^\theta\).
Use the [minor trims and normalization](Yin_C_F0351_v1.md#minor-trims) with even \(k=2\lfloor\log^3(N+3)/2\rfloor\), a prescribed \(k\)-site set \(I\), its complement \(J\) of size \(n=N-k\), \(h=q_n\) and \(M=A_{JJ}B_{JJ}+2B_{JJ}A_{JJ}\).
Write \(g_1,\ldots,g_k\) for the raw columns of \(\sqrt N B_{JI}\).
Their entries have the original iid real law of the second color, and all these columns are independent of \(M\).
Let \(C\) be the compression of \(M\) onto their real orthogonal complement, complexified when taking its shifted determinant.
The [original cross-block rank bound](Yin_C_F0196_v4.md#statement) supplies full rank outside a summable event.
All the estimates below concern fixed \(z\) in \(|z|\le R,\ |\operatorname{Im}z|\ge\delta>0\), uniformly over that parameter region before planar integration.
The original polynomial norm guard \(\|M\|\le N^5\) and the raw column guards \(\|g_i\|\le N^2\) fail with total probability \(O((1+k)N^{-3})\) by the second-moment estimates in [the Gaussian case](Yin_C_F0351_v1.md#minor-trims), which use only the raw variances for these guards.

Let \(t_1\le\cdots\le t_n\) be the singular values of \(M-zI\), and \(b_j=N^{-1}\sum_{i>j}\log t_i\).
Use the [largest-gap rule](Yin_C_F0351_v1.md#adaptive-gap): take the largest \(1\le r\le 2h\) for which \(t_r/t_{r+1}<N^{-40h}\), or \(r=0\) when none exists.
For each sample omit the finitely many eigenvalues of all real compressions along the column sequence when dividing determinants.
Fubini permits the corresponding null sections in the estimates for fixed \(z\).
The choice of \(r\) depends only on \(M,z\).

<a id="discrete-overlaps"></a>
## The first \(r\) columns for arbitrary entry laws

For \(r>0\), every unit vector in either bottom \(r\)-dimensional singular subspace of \(M-zI\) has residual at most \(t_r\) for this matrix or its adjoint.
On the norm guard \(t_r\le (N^5+R)N^{-40h}\).
For both subspaces use the [partial-alphabet exclusion](Yin_C_F0196_v3.md#statement) with \(\gamma=1/3,\ \alpha=9/10\) and fixed positive approximation and residual constants.
For the left subspace exchange \(A,B\) and conjugate \(z\), since the transpose of \(AB+2BA\) is \(BA+2AB\).
The scaling \(M=(n/N)P_n^{\rm can}\) changes the canonical parameter to \(zN/n\) and the residual bound by \(N/n\).
The [compact-parameter version](Yin_C_F0186_v29.md#argument) permits these shifts with an exceptional probability \(C_{R,\delta}e^{-c_{R,\delta}n^{1/8}}\).
Thus, outside this event, no such unit vector on any set of at least \(n/3\) coordinates lies within \(a_0/\sqrt n\) of a vector taking at most \(n^{9/10}\) complex values.

Fix either bottom singular frame \(F\).
At step \(j\le r\) choose a unit \(c\in\mathbb C^r\) orthogonal to \(F^*g_i,\ i<j\), measurably from the minor and earlier columns.
The complex vector \(v=Fc\) lies in the stated near-null class.
Apply the [geometric linear inverse Littlewood--Offord theorem](../audits/literature/Ngu12a/Yin_U001.md#real-scalar-geometric-inverse) to the real two-dimensional coefficients representing \(\bar v_i\).
Their squared norms sum to one.
The variance-one raw entry law satisfies the source's difference condition for two independent copies, since the difference has positive probability in some compact annulus away from zero.
If \(\sup_w\Pr\{|v^*g_j-w|\le N^{-5}\}\ge n^{-5/4}\), take \(n'=\lfloor n/2\rfloor\) in that theorem.
At least \(n-n'\) coefficients are within \(N^{-5}\) of a progression of size \(O(n^{5/4}/\sqrt{n'})=O(n^{3/4})\).
Conjugating back gives an approximation in Euclidean norm at most \(\sqrt n\,N^{-5}<a_0/\sqrt n\), contradicting the exclusion.
This conditional bound is uniform over the choice of \(c\), and uses the actual independence of the fresh column.
Gram--Schmidt and the column norm guard now give both complementary determinant overlaps at least \(N^{-7r}\), except with probability \(O(h n^{-5/4})\) in addition to the two preceding guards.
The two overlap events use the same columns.
The [compound-matrix comparison](Yin_C_F0351_v1.md#adaptive-gap) then gives a log determinant at least \(Nb_r-O(h\log N)\) after these first \(r\) deletions.
For \(r=0\) this is the original determinant.

<a id="quadratic-matchings"></a>
## Subsequent compressions with mixed laws

Given the previous columns, write \(U\) for a real orthonormal frame of the surviving subspace of dimension \(d'\ge n-k\), and \(T=U^{\mathsf T}MU-zI\).
Conditional on the minor and past columns, the next raw column \(g\) still has independent entries with the original second law.
The next unit normal in subspace coordinates is \(U^{\mathsf T}g/\|U^{\mathsf T}g\|\) when the projection is nonzero.
By the [cofactor identity](Yin_C_F0351_v1.md#later-hyperplanes), the determinant ratio equals \(g^{\mathsf T}Kg/\|U^{\mathsf T}g\|^2\), where
\[
 K=U T^{-\mathsf T}\big(\operatorname{sym}(U^{\mathsf T}MU)-zI\big)T^{-1}U^{\mathsf T},
 \qquad \operatorname{sym}(D)=(D+D^{\mathsf T})/2 .
\]
All \(d'\) nonzero singular values of this complex symmetric matrix are at least \(\delta/\|T\|^2\).
Indeed the real symmetric middle matrix before shifting has real eigenvalues and each outside inverse factor has least singular value \(1/\|T\|\).
On the norm guard the lower bound exceeds \(c_\delta N^{-10}\).

Form a graph on the \(n\) coordinate indices, allowing loops, with an edge for \(|K_{ij}|\ge c_\delta N^{-12}\), decreasing \(c_\delta\) if needed.
A maximal collection of disjoint edges and loops has at least \(d'/4\) members.
If there are \(l\) of them, their endpoints cover the graph and number at most \(2l\).
The entries incident to those endpoints form a matrix of rank at most \(4l\) (a sum of a row-supported and a column-supported matrix).
The remaining entries form a matrix with norm at most \(n c_\delta N^{-12}\), smaller than the \(d'\)-th singular value.
The rank approximation inequality gives \(4l\ge d'\).

Expose independent mixture labels for \(g\) only after selecting this matching.
The probability of retaining no edge whose endpoints all carry the regular label is at most \((1-p_B^2)^{\lfloor d'/4\rfloor}\).
This also covers loops.
After revealing the labels and all entries with residual labels, the quadratic polynomial in the independent remaining entries has a monomial coefficient at least \(c_\delta N^{-12}\), since the squared term or mixed term \(2K_{ij}\) on a retained edge survives.
Apply the [fixed-degree product small-ball estimate](Yin_C_F0186_v31.md#product-polynomial-sublevel) at degree two to the component law with its finite first moment, normalizing by the maximum coefficient of the resulting polynomial.
A first moment holds by positive mass and the fourth moment of the original mixture.
The logarithmic concentration hypothesis gives, for all large \(N\), conditional failure \(O(T_N^{-d}+n e^{-cT_N}+e^{-c n})\) for \(|g^{\mathsf T}Kg|<e^{-2T_N}\), since polynomial factors in \(N\) are absorbed at this threshold.
On the column norm guard each successful deletion costs at most \(2T_N+4\log N\) in the logarithm.
A zero projection counts as a failed numerator test.
There are at most \(k\) deletions and \(kN^{-d\theta}\) is summable.

<a id="interior"></a>
## Interior matching and planar passage

The [two-trim comparison](Yin_C_F0351_v1.md#minor-trims) holds under the stated original fourth moments.
Combining its estimates with the preceding deletions and the deterministic adjacent-ratio bound gives on the good sections
\[
 N^{-1}\log|\det(C-zI)|\ge
 b_{2h}(z)-\frac{2h}{N}\log^-t_{2h+1}(z)-o(1).
\]
The deterministic error is \(O((h^3\log N+kT_N)/N)\).
Per-parameter failure probabilities are summable uniformly on the compact region separated from the real line.
Thus the exceptional areas tend to zero almost surely by Fubini, Markov and first Borel--Cantelli.
The two-trim limit and the local square-integrability argument in the [planar transfer](Yin_C_F0351_v1.md#planar-transfer) give the required compression lower comparison on good parameter sets.

For the transfer back to the full determinant use the [matched-monomial construction and factorization](Yin_C_F0186_v33.md#argument), with the same even \(k\).
The [cross-block bounds](Yin_C_F0196_v4.md#statement) give full rank with \(|\log(2^k\det(B_{JI}^{\mathsf T}B_{JI}))|=O(k\log N)\) outside summable exceptions, as detailed in C186v33.
Split \(I\) into halves and find a perfect matching among regular first-color entries, with failure at most \(Ce^{-ck}\) by that construction.
After revealing the unmatched values and labels the interior determinant is a polynomial of individual degree four in each matched raw variable, with joint top coefficient \(N^{-k}\).
At a fixed admissible \(z\), successively take the fourth leading coefficient in each matched variable.
By [the monic-ratio proof](Yin_C_F0186_v33.md#argument) each resulting ratio in the reverse exposure order is a monic quartic with conditional lower log tail bounded by \(4Q_{\nu_A}(e^{-T_N/4})\) at height \(T_N\).
Its nonzero denominator holds on almost all sections by atomlessness of \(\nu_A\).
Outside probability \(O(kT_N^{-d})\), all these ratios cost at most \((k/2)T_N\) in total, in addition to \(k\log N\).
The exact determinant factorization therefore bounds the normalized full log from below by the compression log divided by \(N\), up to \(o(1)\), away from exceptional parameter sets whose areas tend to zero almost surely.
This uses only the monic identity and the actual independent matched variables from C186v33.

For clarity on discarded sets, the negative part of any normalized characteristic log, for the original matrix or its smaller compression with denominator \(N\), is bounded by \(N^{-1}\sum_j\log^-|z-\lambda_j|\).
Its planar square integral on any disk is bounded by \(\int_{|w|<1}\log^2|w|\,dA(w)\) by Jensen, with at most \(N\) summands.
The fixed free potential is also locally square integrable.
The integrated lower deficit relative to \(u(z)=\tau\log|P-z|\) thus tends to zero by the good-set bound, (3) of the minor-trim proof, and Cauchy--Schwarz on the exceptional sets.
First work on each disk excluding \(|\operatorname{Im}z|<1/j\), then let \(j\to\infty\) on the intersection of those events.
The [regularized upper bounds](Yin_C_F0186_v4.md#regularized-potentials) give convergence of the positive overshoot in local area integral by decreasing the regularizer.
This proves local \(L^1\) convergence of the true potentials and hence full almost-sure Brown convergence under each allowed coupling.
Applying the [terminal equivalence](Yin_C_F0186_v36.md#statement) proves the stated summability for the original marginal laws.

## Current assessment
[Selected decision](#decision-mixed-components-reviewed)

## Assessment history

### Decision mixed-components-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:27 |
| status | open |
| reason | The candidate extends the Gaussian compression argument to the original mixture laws by arithmetic exclusion and a high-rank quadratic matching. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two components](#statement) | Every-coupling Brown convergence and summable integrated terminal losses in the stated fourth-moment mixture model. |
| argument | [Proof](#argument) | Arithmetic overlap, regular labels, compression and interior transfer. |

### Decision mixed-components-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T06:33 |
| status | proved |
| reason | Independent review confirmed the two-component raw-law argument, including atomic residuals and the full terminal deviation series. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete stated conclusions under the specified hypotheses. |
| argument | [Proof](#argument) | Full mathematical argument for this version. |
| support | [Linear overlaps](#discrete-overlaps) | The first r column tests include arbitrary nondegenerate iid raw entries. |
| support | [Later compressions](#quadratic-matchings) | Many disjoint coefficients and fresh regular mixture labels in the new column. |
| support | [Planar comparison](#interior) | The original interior matching, integration and the untrimmed Brown conclusion. |
| dependency | [Original trims](Yin_C_F0186_v36.md#statement) | Trimmed potentials and every-coupling terminal criterion. |
| dependency | [Minor trims](Yin_C_F0351_v1.md#minor-trims) | Two trimming ranks at the mildly rescaled old minor. |
| dependency | [Arithmetic exclusion](Yin_C_F0196_v3.md#statement) | The near-mode exclusion on a positive fraction of coordinates. |
| dependency | [Matched determinant](Yin_C_F0186_v33.md#argument) | Original interior monic coefficient and true compression factorization. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0358_v2.md#mixed-components-whole-proof) | Complete fixed statement, proof and applicability boundaries. |
