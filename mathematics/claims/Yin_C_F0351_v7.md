---
author: Yin
---

# Ordinary sign-matrix determinants of two-sided quadratic products at every prescribed shift

<a id="statement"></a>
## Rademacher laws and fixed parameters

Let \(A_N,B_N\) be independent real symmetric Wigner matrices with all raw upper triangular entries, including the diagonals, independent uniform signs at each size, in the normalization \(N^{-1/2}\).
Fix \(\lambda\in\mathbb R\setminus\{0,-1\}\), \(P_N=A_NB_N+\lambda B_NA_N\), \(p=ab+\lambda ba\) for a free standard semicircular pair, and \(z\in\mathbb C\).
Put \(u(z)=\tau\log|p-z|\).
Then
\[
 N^{-1}\log|\det(P_N-zI)|\longrightarrow u(z)
 \quad\text{in probability through all dimensions}.
\]
On the deterministic even sequence \(N=2^j,\ j\ge1\), this convergence is almost sure under every allowed coupling.
The almost-sure limsup on all dimensions equals \(u(z)\).
The target includes real \(z\) and zero.
Both assertions also hold for any fixed scalar polynomial in \(P_N\) followed by any prescribed scalar shift, with its corresponding free target and the ordinary convention for a zero constant.
For the nonconstant scalar cases and any fixed \(B>0\), the normalized negative-log excess below the cutoff \(N^{-B}\) tends to zero in probability, and almost surely on the same dyadic dimensions.
A finite collection of these assertions can be imposed on one event.
The normalized matrix determinant conclusions apply to their exact word-chain pencils with the [auxiliary trace normalization](../ledger/Yin_L_F0061_v2.md#linearization-transfer).

<a id="argument"></a>
<a id="spectral-gap"></a>
## Separating near-kernel vectors from each input eigenspace at a real shift

Consider original \(n\)-site principal minors \(A,B\) with size-\(N\) normalization, \(0.9N\le n\le N\).
All bounds here are uniform on each fixed bounded parameter set \(|w|\le R\).
Their operator norms are at most a fixed \(K\) outside \(Ce^{-cn}\), by the sign quadratic-form bound and a sphere net in the [original sign argument](Yin_C_F0351_v5.md#sign-flag-area).
For any chosen small \(\epsilon>0\) we may choose a fixed \(\delta>0\) such that each interval of width \(10(1+|\lambda|+|\lambda|^{-1})\delta\) meeting a prescribed bounded spectral range contains at most \(\epsilon n\) eigenvalues of \(A\), outside \(Ce^{-cn}\).
Use finitely many enlarged intervals, the bounded density of the rescaled semicircle and the [row-rank concentration](Yin_C_F0186_v4.md#row-concentration).
Expected count convergence is uniform in \(0.9N\le n\le N\) by compactness of the scaling \(n/N\) and the canonical weak law at continuity points.
The same holds when interchanging \(A,B\).

Condition on \(A\).
For every real \(|d|\le K+1\) use a finite grid of centers \(d'\) within \(\delta\), covering this interval.
Let \(E\) contain the spectral interval of \(A\) at \(d\) of radius \(\delta\), using the enlarged interval at \(d'\).
Let \(F\) contain \(E\) and the interval at \(-\lambda d\) of radius \(\delta\), using the enlarged second interval centered at \(-\lambda d'\).
Here \(E,F\) are spectral subspaces and \(Q\) is the orthogonal projection off \(F\).
The ranks of \(E,F\) are at most \(\epsilon n,2\epsilon n\) with the preceding choices.
For every fixed complex unit vector \(h\) in \(E\),
\[
 \mathbb E_B\|QBh\|^2
 =N^{-1}h^*((\operatorname{Tr}Q)I+Q^{\mathsf T}-\operatorname{diag}Q)h\ge c.
\]
This identity follows by pairing the independent upper signs, counting a diagonal pair only once.
As a function of all raw signs the norm is convex and \(\sqrt{2/N}\)-Lipschitz in Euclidean distance by the Hilbert--Schmidt bound.
The [bounded-product concentration inequality](Yin_C_F0187_v2.md#argument) therefore gives a fixed lower bound except with probability \(Ce^{-cn}\), since its second moment about its median is \(O(N^{-1})\).
Use a fixed fine net of the complex unit sphere in \(E\), then the upper norm bound for \(B\).
Choose \(\epsilon\) small relative to the fixed tail exponent and net radius before choosing \(\delta\).
Outside \(Ce^{-c'n}\), one has \(\|QB h\|\ge c'\|h\|\) simultaneously on all the selected \(E\).

Write \(T=AB+\lambda BA-w\).
If a unit \(h\) satisfies \(\|(A-d)h\|\le\rho\) and \(\|Th\|\le\rho\), then \(\operatorname{dist}(h,E)\le\rho/\delta\) and
\[
 \|QB h\|\le\delta^{-1}\|Q(A+\lambda d)Bh\|
 \le \delta^{-1}\bigl(\rho+|\lambda|K\rho+R\rho/\delta\bigr).
\]
For sufficiently small fixed \(\rho>0\) this contradicts the lower bound on \(E\) and the norm bound for \(B\).
Real \(d\) outside the grid range have a gap by the norm bound, and complex \(d\) reduce to \(\operatorname{Re}d\) by selfadjointness.
Interchanging the inputs and using \(P_N=\lambda(BA+\lambda^{-1}AB)\) gives the same conclusion for the other color.
The transposed product uses the exchanged inputs with the original coefficient.
In particular for all sufficiently small fixed residuals, and unit \((v_1,v_2)\in\mathbb C^2\), both \(\|(v_1A+v_2I)h\|\) and \(\|(v_1B+v_2I)h\|\) are bounded below.
For small \(|v_1|\) use the norm bound directly; otherwise divide by \(v_1\) and use the gap just proved.
This applies also to adjoint near-kernels with shift \(\bar w\).

<a id="trim"></a>
## Trimming at the prescribed shift

The three-channel companion of the [paired border proof](Yin_C_F0186_v36.md#one-step) now has first row \((-wI,A,\lambda B)\) and the same two auxiliary rows as there.
For the left near-kernel the graph coordinates are \(g=Ah+e,\ j=\lambda Bh+f\); on the right they are \(g=Bh+e,\ j=Ah+f\).
At sufficiently small fixed residual the errors are small, \(\|h\|\) is bounded below and its normalized scalar residual for the respective product is small, by the input norm guard.
For each fresh border direction \(v\in\mathbb C^3\), the conditional raw covariance on the left is
\(\|\bar v_2h+\bar v_1j\|^2+\|\lambda\bar v_3h+\bar v_1g\|^2\);
on the right it is
\(\|\bar v_3h+\bar v_1g\|^2+\|\bar v_2h+\lambda\bar v_1j\|^2\).
The preceding affine gaps give both a fixed lower bound on unit \(v\), since \(\lambda\ne0\).
The [projected border and few-small-values argument](Yin_C_F0186_v36.md#concentration), using the same fixed-size block maps with constants depending on \(\lambda\), and the [paired volume inequality](Yin_C_F0347_v1.md#statement) therefore give
\(p_{r+6}(L_{n+1})\ge c\,p_r(L_n)((3n-r)/N)^3\) when the deficit is at least \(C\log N\), outside the summable chain exceptions in that proof.
Here \(p_r\) is the product of the \(r\) largest singular values.
The new spectral-window and norm guards are summed over at most \(N\) stages, without conditioning a fresh row on future guards.

For clarity, start at \(n=\lfloor a_0N\rfloor,\ 0.9<a_0<1\), with deficit \(3(N-n)+s_N\) and finish at deficit \(s_N=q_N\) or \(2q_N\), \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\).
The [fixed-fraction initialization](Yin_C_F0351_v3.md#argument) applies for every deterministic \(w_N\to w\), using canonical parameter \(w_N/(n/N)\) and diagonal scaling with first channel \(\sqrt{n/N}I\).
Every free companion in a compact set of shifts is full, by its unit-triangular Schur pivot and the nonzero scalar polynomial in the [semicircular free field](Yin_C_F0011_v1.md#yin_c_f0011).
The [uniform free power estimate](Yin_C_F0352_v1.md#statement) on this compact family, with zero drift in the physical variables, gives uniform log integrability at zero.
Weak continuity of the free singular laws and the bounded free norm thus give continuity of \(u\) on the whole plane.
The canonical weak law and a fixed lower clip whose free mass is less than \((1-a_0)/a_0\) give the starting lower limit at least \(a_0 u(w/a_0)-O(1-a_0)+3\log a_0\), exactly by the retained-product calculation of the cited initialization.
The total normalized border cost is \(O((1-a_0)(1+|\log(1-a_0)|))\) from summing \(\log(N/i)\) over the \(N-n\) stages.
Let \(a_0\uparrow1\) along a countable sequence.
The opposite bound follows from fixed log clipping and then sending the clip down to zero, with \(s_N=o(N)\).
The [unit-triangular factor comparison](Yin_C_F0186_v36.md#final-product) applies with \(\lambda\) in place of 2, and the uniformly bounded norms make the normalized omitted-log comparison \(o(1)\).
Thus the scalar \(q_N\)- and \(2q_N\)-trimmed logarithms converge almost surely under each coupling at every prescribed convergent \(w_N\), including real limits.

<a id="overlap"></a>
## Initial overlap for a single parameter

A weaker first-column probability suffices for convergence in probability.
On \(\|A\|\le K\) and for a fixed unit complex vector \(h\), the covariance formula above, with \(Q\) replaced by \(A^2,A,I\), gives
\[
 \mathbb E_B\|(AB+\lambda BA-w)h\|^2
 = (n/N)\operatorname{tr}_n(A^2)+\lambda^2(n/N)\|Ah\|^2
 +2\lambda(n/N)\operatorname{tr}_n(A)\operatorname{Re}\langle h,Ah\rangle
 +|w|^2+O_\lambda(K^2/N).
\]
The random part has zero conditional mean.
In this model \(\operatorname{tr}_n A^2=n/N\) and \(|\operatorname{tr}_n A|\le N^{-1/2}\).
The expression is bounded below by a positive constant.
The norm is convex and \(C_{\lambda,K}/\sqrt N\)-Lipschitz in the raw \(B\) coordinates.
The same lower-tail estimate and a fixed-resolution net over all unit vectors supported on at most \(\epsilon n\) prescribed sites, unioned over the site choices with \(\epsilon\) sufficiently small, imply the following.
Except with \(Ce^{-cn}\), every unit vector with sufficiently small scalar residual has distance at least a fixed constant from all such sparse subspaces.
Use \(\|AB+\lambda BA-w\|\le (1+|\lambda|)K^2+R\) on the norm guard for the extension from the nets and then to nearby vectors.
The adjoint has the same property by exchanging colors.
This estimate is uniform in the marginal probability on bounded sets of \(w\).

Each such near-null unit vector has at least \(c n\) coordinates of modulus at least \(c'/\sqrt n\), since otherwise deleting the large coordinates would leave a vector of small norm.
For a fresh iid sign column \(g\), one of the real and imaginary parts therefore has at least \(c n/2\) coefficients of absolute value at least \(c'/\sqrt{2n}\).
After fixing the other coordinates, flipping signs of coefficients makes them positive, and the sign subsets landing in an interval of width \(2N^{-5}\) are an antichain.
The maximal chains counting proof of Sperner's bound gives conditional probability at most \(\binom{l}{\lfloor l/2\rfloor}2^{-l}=O(n^{-1/2})\), where \(l\ge c n/2\).
This is uniform in the center and in the conditioned choice of near-null vector.

Use the [adaptive singular gap and complementary-volume estimate](Yin_C_F0351_v1.md#adaptive-gap) in the \(n=N-k\) principal minor with \(k=2\lfloor\log^3(N+3)/2\rfloor,\ h=q_n\).
If the last gap among the first \(2h\) has ratio below \(N^{-40h}\), its bottom left and right subspaces consist of near-null vectors at the above residual; otherwise start at rank zero.
Sequential Gram--Schmidt for the [two projected frames](Yin_C_F0351_v2.md#discrete-overlaps) now costs probability only \(O(hn^{-1/2})\).
The two overlaps are tested on the same columns and their failures are unioned.

<a id="restore"></a>
## Restoring the ordinary determinant

The remaining flag ratios and the paired restorations use the physical corners of
\(\operatorname{sym}(B^i R B^j),\ i,j\in\{0,1\}\) with \(R=(AB+\lambda BA-w)^{-1}\).
The old flag and two-dimensional extension spaces in [the sign restoration proof](Yin_C_F0351_v5.md#paired-sign-restoration) are unchanged.
In the two-direction restoration update \(FDG^{\mathsf T}+GDF^{\mathsf T}\), take \(D=\left(\begin{smallmatrix}0&1\\\lambda&0\end{smallmatrix}\right)\).
The top raw quartic is now \(\lambda^2N^{-2}\det(F_L^{\mathsf T}F_L)\det(G_0^{\mathsf T}RG_0)\), where \(G_0\) is made from the raw fresh row and its \(B\)-image, before normalization.
The physical Gram factor is bounded below on the [rectangular cross-block guard](Yin_C_F0196_v4.md#statement).
All lower-degree terms disappear under the four physical mixed differences.

For real \(w\), the requisite real kernel family is independent modulo scalars in the free field when \(\lambda\ne1\).
Indeed on scalar inputs \(A=x,B=b\) the kernel numerators are \(1,b,b,b^2\) over \((1+\lambda)bx-w\).
Variation in \(x,b\) leaves only the difference of the middle two kernels in a scalar relation.
This difference is \([R-R^{\mathsf T},B]/2\).
At diagonal \(B=\operatorname{diag}(b_1,b_2)\) and \(A=\operatorname{diag}(x_1,x_2)+u(E_{12}+E_{21})\), its off-diagonal derivative at \(u=0\) is
\[
 \frac{(\lambda-1)(b_2-b_1)^2}
 {2((1+\lambda)b_1x_1-w)((1+\lambda)b_2x_2-w)} .
\]
It is nonzero for distinct nonzero \(b_1,b_2\) and regular choices of \(x_i\).
If \(\lambda=1\), the two middle kernels agree identically by symmetry of \(R\).
The scalar specialization proves independence of the three remaining kernels, and the fourth-difference pairing on them is \(v_{00}u_{11}+v_{11}u_{00}-2v_{01}u_{01}\).
It still has coefficient \(v_{00}\) on \(u_{11}\).
For nonreal \(w\), include both real and imaginary parts of this reduced or full kernel family; the distinct simple poles at \(w,\bar w\) in the scalar test and the same two-site derivative separate the coefficients at the two parameters.
These tests are valid also at real \(w=0\), using regular nonzero scalar specializations.
Nonzero free scalar denominators have affiliated inverses at every such parameter.

Consequently the [physical-corner and disjoint-basis argument](Yin_C_F0351_v5.md#sign-flag-area) gives the single flag-ratio failure \(O(n^{-1/8})\), and the [four-block mixed-difference argument](Yin_C_F0351_v5.md#paired-sign-restoration) gives a single restoration-ratio failure \(O(n^{-1/32})\).
For real parameters these arguments use only real kernels.
When treating the quartic the \(00\) crossing on blocks 1,2 has probability \(O(n^{-1/2})\) to have modulus at most one.
On its complement the coefficient norm on the \(34\) family is at least one, from the \(11\) entry, including the three-kernel case.
The other two pairings have coefficient vectors in the bounded-dimensional subspace already fixed before sampling block 3.
The bounded approximation, original Wigner colored moments and rank transfer in the two cited arguments require only absence of a free kernel and nonscalar independent directional corner tests at this stage.
They apply uniformly on a compact real interval, or a compact complex neighborhood disjoint from the real line, respectively, by continuity of the resolvents in measure and compactness.
These are marginal bounds; the flag and restoration condition on their own chronological histories.

Multiplication with the initial-gap bound gives the [undivided product comparison](Yin_C_F0351_v3.md#fixed-compressions)
\[
 |\det(P_N-w)|\ \ge\ e^{-N e_N}\,p_{n-2h}(M-w)\min(1,t_{2h+1})^{2h},
\]
where \(M=A_{JJ}B_{JJ}+\lambda B_{JJ}A_{JJ}\), \(t_i\) are its ascending shifted singular values and \(e_N=O((h^3+k)\log N/N)\).
Use the deletion thresholds \(N^{-2}\) and restoration thresholds \(N^{-3}\) of the sign proof, decreasing the latter by a fixed factor if necessary.
The exceptional probability is \(O(hn^{-1/2}+kn^{-1/32})\) plus exponentially small or \(O(N^{-3})\) guards.
For each dimension avoid all poles in the intermediate divisions, a finite set across the finitely many sign samples.
The undivided inequality is continuous in \(w\) on both sides.
Approaching an excluded real point through real parameters (or a nonreal point through its chosen neighborhood) transfers the same bound on the probability of strict violation.

The two old-minor trims converge at the prescribed shift even at the normalization \(N\), by homogeneity \(M=(n/N)P_n^{\rm can}\), the moving-shift trim above at \(wN/n\), and bounded multiplicity of \(n=N-k\).
Their difference bounds \(h\log^-t_{2h+1}/N\) up to \(o(1)\) using the bounded input norms.
The product comparison now gives the lower log limit in probability and almost surely along \(2^j\), since its exceptional probabilities are summable there.
The fixed-clip upper bound gives the opposite inequality in both modes under any coupling.
For a scalar polynomial in \(P_N\) factor at the finitely many complex roots after subtracting the chosen shift, and apply finite and free determinant multiplicativity.
The cutoff excess is nonnegative and is bounded above by the fixed-\(d\) clipped log minus the ordinary log for any \(d>N^{-B}\).
Fixed-\(d\) convergence and then \(d\downarrow0\) prove its vanishing in the claimed modes.
The same argument uses clips of the word-chain pencil for its own excess.
All these pointwise results concern the fixed polynomial and fixed shift.

## Current assessment

[Selected decision](#decision-prescribed-sign-candidate)

## Assessment history

### Decision prescribed-sign-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:51 |
| status | open |
| reason | Spectral-window separation and physical incompressibility supply a fixed-shift candidate argument through the real axis for the indicated family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [All fixed shifts](#statement) | The two-sided product family, its scalar compositions and its ordinary deterministic-even-subsequence limits. |
| argument | [Spectral-window separation](#argument) | Uniform individual-input gap on actual principal minors, including real parameters. |
| support | [Two trims](#trim) | Paired volume growth and the fixed-fraction initialization. |
| support | [First overlaps](#overlap) | Physical sparse exclusion and the one-parameter sign small-ball bound. |
| support | [Restorations](#restore) | The physical kernels and the fixed-parameter ordinary determinant, with all poles handled by continuity. |
