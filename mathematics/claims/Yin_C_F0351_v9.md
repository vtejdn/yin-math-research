---
author: Yin
---

# Two observed directions for quadratic Wigner polynomials with a distinguished input

<a id="statement"></a>
## A finite-variance quadratic family

Use independent real symmetric Wigner colors \(A,Y_1,\ldots,Y_g\) with fixed centered variance-one strict upper laws, fixed centered finite-second-moment diagonal laws and independent upper triangular coordinates at each size, scaled by \(N^{-1/2}\).
Different colors can have different laws and all dimensions may be coupled arbitrarily.
Take real linear forms \(B=b\cdot Y,\ C=c\cdot Y,\ U=u\cdot Y,\ V=v\cdot Y\) and a real affine form \(\ell(A,Y)=\ell_0+\ell_A A+\ell_Y\cdot Y\).
Assume \(b,c\ne0\).
If \(c=\lambda b\), assume \(1+\lambda\ne0\) or \(\ell_A\ne0\).
Consider
\[
 P(A,Y)=AB+CA+CU+VB+\ell(A,Y).
\]
Write \(P_N\) for its Wigner evaluation and \(p\) for its evaluation at independent standard free semicirculars.
With \(q_N=\lceil\log(N+3)\log\log(N+3)\rceil\), decreasing singular values and \(\log^-x=\max(0,-\log x)\), for every \(R,\epsilon>0\),
\[
 \sum_{N:q_N<N}\Pr\left\{\frac1N\int_{|z|<R}
 \sum_{j>N-q_N}\log^-s_j(P_N-zI)\,dA(z)>\epsilon\right\}<\infty.
 \tag{1}
\]
The ordinary potentials converge almost surely to \(u(z)=\tau\log|p-z|\) in local planar \(L^1\), and the empirical eigenvalue measures converge weakly almost surely to the Brown measure of \(p\) under each permitted coupling.
For each prescribed nonreal parameter \(z\) the ordinary normalized logarithms converge to \(u(z)\) in probability and almost surely along \(N=2^j\).
In particular the all-dimension limsup equals \(u(z)\) almost surely there.

For example, with independent real Wigner \(A,B,C\), the choice \(U=C,V=B\) gives \(AB+CA+C^2+B^2+\ell\).
A two-variable example is \(AB+2BA+B^2\).
At each shift its pencil with first row \((-zI,A+B,2B)\) and auxiliary rows \((B,-I,0),(A,0,-I)\) has two variable coefficient matrices of rank two; they and its constant coefficient are linearly independent.
Its finite and free normalized log determinants are the corresponding scalar normalized logarithms divided by three by unit triangular Schur factorization.
Thus for this explicit three-dimensional coefficient space the stated nonreal-parameter result applies to the original signs.

<a id="argument"></a>
<a id="exterior"></a>
## The two exterior spaces and their algebraic scope

Choose \(k=2\lfloor\log^3(N+3)/2\rfloor\) sites \(I\), with \(J=I^c,\ n=N-k,\ h=q_n\).
Put \(M_0=P(A_{JJ},Y_{JJ})\) in the original physical normalization, \(M=P_N\), and write \(P(X)-z\) for \(P(X)-zI\).
The left exterior is the orthogonal complement in \(\mathbb R^N\) of \(e_i,Ce_i\) for \(i\in I\), and the right one uses \(e_i,Be_i\).
Within the \(J\) sites, these are precisely the orthogonal complements of the columns \(C_{JI}\) and \(B_{JI}\).
In the \(JJ\) block the extra terms of \(M\) relative to \(M_0\) are \(A_{JI}B_{IJ}, C_{JI}A_{IJ}, C_{JI}U_{IJ}, V_{JI}B_{IJ}\).
All vanish after the left and right projections.
In particular the resulting square compression of \(M-z\) is the same matrix, in the corresponding frames, as the exterior compression of \(M_0-z\); the two subspaces need not coincide.

More generally, for a background quadratic tensor \(Q_0\) on the \(Y\) colors, its extra term at one deleted site equals \(XQ_0X^{\mathsf T}\), where the columns of \(X\) are the background cross vectors there.
The left normal is \(Xc\), and the right normal is \(Xb\).
Universal cancellation of the background term in these two exterior spaces is equivalent to
\[
 Q_0=c u^{\mathsf T}+v b^{\mathsf T}\quad\text{for some }u,v .
\]
Sufficiency follows by multiplication.
For necessity take \(X\) with orthonormal columns at one site, physically realizable by unrestricted symmetric inputs.
Then the corner from \(b^\perp\) to \(c^\perp\) must vanish, and decomposing the tensor by these two orthogonal projections gives the formula.
An \(A^2\) term contributes \(x x^{\mathsf T}\) for the fresh row \(x\), which in general survives projection away from any fixed such normals from background colors.
These are exact limitations of this exterior identity for the chosen fresh color.

Both \(B_{JI}\) and \(C_{JI}\) have least singular value at least a fixed positive constant except with summable probability by the [finite-variance rectangular argument](Yin_C_F0351_v8.md#cross-block), applied to each marginal after variance normalization.
Their correlation requires only addition of the two errors.
By Frobenius Markov the norms of all inputs and their fixed linear combinations are at most constant multiples of \(N^2\) outside \(O(N^{-3})\).
Use the first \(s\le k\) cross columns on each side to form orthonormal frames of the remaining spaces in \(J\); denote them by \(W_L,W_R\), respectively.
For fixed \(z\) away from the old minor spectrum and with invertible compression, put \(R=W_R(W_L^{\mathsf T}(M_0-z)W_R)^{-1}W_L^{\mathsf T}\).
Its difference from \(R_0=(M_0-z)^{-1}\) has rank at most \(s\), since the range of \(I-(M_0-z)R\) lies in the orthogonal complement of \(W_L\).
No lower bound on the angle between the left and right spaces is needed.

<a id="kernels"></a>
## Free rational tests

Here transpose reverses the order of the formal selfadjoint variables, retaining the scalar spectral parameter.
Use the four scalar kernels
\[
 K_{ij}(z)=\operatorname{sym}(B^i R_0 C^j),\quad i,j=0,1,\qquad
 \operatorname{sym}T=(T+T^{\mathsf T})/2 .
\]
To check relations consider their free rational formulas at \(p-z\) and a tuple of distinct upper-half-plane parameters together with their conjugates.
The rational inverse exists in the [semicircular free field](Yin_C_F0011_v1.md#yin_c_f0011) since the displayed polynomial is nonconstant.
For linearly independent \(b,c\), scalar specialization \(A=x,\ Y=y\) gives numerators \(1,C(y),B(y),B(y)C(y)\) and common denominator
\((B(y)+C(y)+\ell_A)x+(CU+VB+\ell(0,y))-z\).
On a nonempty open set in \(y\), the slope in \(x\) is nonzero, and the poles in \(x\) are distinct for the different shifts.
In any complex linear relation modulo scalars, the residue at each pole is zero.
Varying \(y\) proves that all four coefficients at each parameter vanish.

In the proportional case \(C=\lambda B\), rescale the kernels to \(\operatorname{sym}(B^i R_0 B^j)\).
The slope in \(x\) is still generically nonzero by the hypothesis.
Scalar specialization first leaves only multiples of the difference of the two middle kernels, proportional to \([R_0-R_0^{\mathsf T},B]\).
Set \(T=(1-\lambda)A+V-\lambda U\), so \(P-P^{\mathsf T}=[T,B]\).
If \(T\) is a scalar multiple of \(B\) then \(P=P^{\mathsf T}\) and the middle kernels coincide.
Use their three independent components, since \(1,B(y),B(y)^2\) are independent scalar numerators.
Otherwise choose two-site diagonal input matrices with generically different values \(b_1,b_2\) of \(B\), and choose off-diagonal perturbations of the colors which leave \(B\) fixed and change \(T_{12}\) with derivative one.
Such a real direction exists by linear independence of the corresponding forms.
Writing \(p_i\) for the scalar value of \(P\) at site \(i\), the derivative of the \(12\) entry of \([R_0-R_0^{\mathsf T},B]\) is
\[
 -(b_2-b_1)^2\big/[(p_1-z)(p_2-z)] .
\]
This follows by differentiating the inverse at a diagonal point.
Independent variation of the diagonal \(A\) entries varies \(p_1,p_2\) with nonzero slopes.
Residues in \(p_1\) then exclude any nontrivial relation of these differences across the prescribed shifts.
The specializations use regular choices of denominators.
The resulting real and imaginary kernel directions are independent modulo scalars at the upper-half-plane parameters.

The flag uses an additional generally nonsymmetric kernel.
Choose color indices \(\alpha,\beta\) such that \(b_\alpha c_\beta+c_\alpha b_\beta\ne0\); existence follows because the quadratic polynomial \((b\cdot t)(c\cdot t)\) is nonzero.
For \(S=b_\alpha c_\beta R_0+c_\alpha b_\beta R_0^{\mathsf T}\), the scalar test at distinct poles again excludes scalar relations among its real parts at separated upper-half-plane shifts.
The [free distinct-site corner argument](Yin_C_F0351_v5.md#sign-flag-area) works for this family as well: by permutations of the equal-trace free coordinate projections a vanishing off-diagonal corner of a fixed operator would force all such corners to vanish, giving commutation with a nontrivial free projection and hence a scalar.
Equivalently in the affiliated case apply the argument to the bounded transform after showing commutation with all the partition projections.
The real and imaginary parts here mean entrywise real and imaginary components in the physical model, corresponding to the combinations of the free kernels at \(z,\bar z\).

On compact sets of tuples a positive distance from the real axis and pairwise separated, these tests imply a uniform positive fraction of singular values above a positive threshold for every real unit direction in the relevant corners.
Use continuity in measure of the free inverses and compactness as in [the original-law physical-corner proof](Yin_C_F0351_v6.md#physical-corners).
For the finite model, its colored moment, small-rank clipping and row-concentration arguments apply verbatim to any fixed number of independent original finite-variance colors with the same deterministic coordinate projections.
Indeed bounded raw truncation has the same leading pairings with color matching, and all fixed polynomial rank telescopes and Hilbert--Schmidt approximations have constants depending only on the degree and fixed number of words.
One may clip each old input at a constant above the free norm, regularize the inverse at \(\eta>0\) and compare its small singular subspace with the free one, which has no zero atom.
Each extra left or right power of \(B,C\) contributes only the change of its own rank when returning from clipped inputs to the true kernels.
Thus the physical kernels have bounded approximants with arbitrarily small total error rank compared to the fraction of good singular values, outside \(Ce^{-cn}\) old-minor exceptions, with the stated uniformity on separated tuples.
Passing to later flag or restoration compressions costs only \(O(k)\) further rank in each kernel.
For restorations extend a regular compressed inverse by its left/right frames; comparing the full and padded \(JJ\) pencils and their input factors costs \(O(k)\) rank.
More explicitly if \(R_{\rm old}=W_R(W_L^{\mathsf T}(M-z)W_R)^{-1}W_L^{\mathsf T}\), then \(\operatorname{rank}(I-(M-z)R_{\rm old})\le 2k\).
The direct sum of \(M_0-z\) on \(J\) and an identity on \(I\) differs from \(M-z\) by rank \(O(k)\) by the quadratic cross-term expansion.
Multiplying by the inverse of this direct sum bounds the rank discrepancy of \(R_{\rm old}\) from the padded original inverse even if \(M-z\) is singular.

<a id="flags"></a>
## Left and right flags

Apply the [initial trim and overlap theorem](Yin_C_F0186_v42.md#statement) for the actual real quadratic on \(J\), including the near-one variance normalization.
The first \(r\) columns are selected by the [old-minor gap](Yin_C_F0351_v1.md#adaptive-gap), with threshold as in the initial-overlap theorem, using the left flag for the left singular frame and the right flag for the right singular frame.
The exterior-power calculation uses the top left and right singular volumes against their respective compressed frames and bounds the remaining terms by the second singular value of the exterior power.
It therefore holds also when these two physical flags differ.
It starts the lower comparison with \(N^{-1}\log p_{n-2h}(M_0-z)-(2h/N)\log^-t_{2h+1}\), up to an error tending to zero, outside sets whose positive area-deviation probabilities are summable.
Here \(t_j\) are the ascending old-minor singular values.
The original flag columns have the fixed nondegenerate real marginals specified above, independent of the old minor and independent between sites; the two sides at a site may depend on each other.

Upon one further deletion the absolute determinant ratio, when its incoming determinant is nonzero and the columns add directions, equals
\[
 \frac{|g_R^{\mathsf T}R g_L|}
 {\|W_R^{\mathsf T} g_R\|\,\|W_L^{\mathsf T}g_L\|},
 \quad g_R=\sqrt N B_{Ji},\quad g_L=\sqrt N C_{Ji}.
\]
This is the complementary cofactor identity in orthonormal completions of the two new unit directions.
Outside \(O(kN^{-3})\) the raw column norms do not exceed \(N^2\) up to fixed constants.
In the bad-ratio test require the current norm guard as well and charge failures separately.
For a given set of \(s\) assigned shifts at this step, a ratio below \(N^{-7}\) forces a bounded raw numerator, in fact \(O(N^{-3})\).
Split the sites into two halves.
Use independent resamplings of the \(\alpha\)-color coordinates on the first half and the \(\beta\)-color coordinates on the second half, keeping all other fresh coordinates fixed.
The mixed second difference of the numerator before absolute values is the bilinear form of the two difference vectors on the physical corner of \(b_\alpha c_\beta R+c_\alpha b_\beta R^{\mathsf T}\).
Two Cartesian Cauchy--Schwarz steps, followed by the [bounded approximation, disjoint bases and general real Fourier estimate](Yin_C_F0351_v6.md#border-tests), give \(O(n^{-s/8})\) for the joint original tests, up to an exponentially small term.
The two difference vectors may have different laws, since the output spread and the Fourier step each require only the nondegeneracy of their own law.

<a id="restoration"></a>
## Two-direction restorations

Reveal \(Y,A_{JJ},A_{II}\), then expose the \(A_{Ji}\) one at a time.
At a step let the old left and right spaces be orthogonal respectively to the remaining pairs \((e_i,Ce_i)\) and \((e_i,Be_i)\) including the current site; the new spaces omit this site's pair from those constraints.
Write \(x\) for the current normalized fresh row padded by zero outside \(J\).
Set
\[
 F_L=[e_i,Ce_i],\quad F_R=[e_i,Be_i],\quad
 G_L=[x,Cx],\quad G_R=[x,Bx],\quad
 D=\begin{pmatrix}\ell_A&1\\1&0\end{pmatrix}.
\]
The exact perturbation supplied by this row is \(F_L D G_R^{\mathsf T}+G_L D F_R^{\mathsf T}\).
In particular all future perturbations vanish between the current spaces, and the old compressed matrix is measurable before \(x\) is drawn.
Let \(J_L,J_R\) be isometries onto the two new directions on each side after projecting off the old spaces, and use \(R_{\rm old}\) as above.
The highest possible homogeneous part of the two-dimensional Schur ratio is
\[
 \det(J_L^{\mathsf T} F_L)\det(J_R^{\mathsf T} F_R)
 \det(G_R^{\mathsf T}R_{\rm old}G_L).
\]
Indeed the old-to-new and new-to-old linear blocks produce the quadratic part \(-(J_L^{\mathsf T}F_L)D(G_R^{\mathsf T}R_{\rm old}G_L)D(F_R^{\mathsf T}J_R)\), with \((\det D)^2=1\).
The fresh part of the new diagonal block is affine.
In raw variables the quartic coefficient has another factor \(N^{-2}\).
Each projected two-column map has least singular value at least \(cN^{-2}\) on the rectangular and norm guards, by the full pair map \((g,h)\mapsto(g+B_{II}h,B_{JI}h)\) and the same calculation for \(C\).
Taking distance from the later pairs preserves the lower bound.
Thus the absolute product of the two determinants is at least \(cN^{-8}\).

At \(s\) assigned shifts with regular incoming compressions, test whether all restoration ratios have modulus below \(N^{-12}\).
The [four-site-class mixed difference](Yin_C_F0351_v5.md#paired-sign-restoration) removes every lower-degree term.
It leaves the three pairings of four independent difference vectors in the kernels \(K_{ij}\).
Their common determinant contraction is \(v_{00}w_{11}+v_{11}w_{00}-v_{01}w_{10}-v_{10}w_{01}\).
In the selfadjoint proportional case the rescaled three kernels give a nonzero multiple of \(v_{00}w_{11}+v_{11}w_{00}-2v_{01}w_{01}\); constants from \(\lambda\) are fixed and nonzero.
For completeness, among the first two panel vectors the \(00\) bilinear forms for any prescribed \(d\) shifts have joint probability \(O(n^{-d/2})\) of modulus at most one, by the distinct real \(00\)-corners and the disjoint-basis estimate.
Condition on the first two differences.
For every remaining shift the contraction has coefficient of absolute value at least one in front of its independent \(11\) kernel, up to the fixed proportional-case factor.
The other pairings lie, in the fourth panel, in the span of the kernel images of the first two vectors, of dimension \(O(s)\) fixed before the third vector is sampled.
The same [projected output-spread estimate for general real laws](Yin_C_F0351_v6.md#border-tests) gives joint small-ball probability \(O(n^{-(s-d)/2})\) on the fourth vector after the third, uniformly in these coefficients.
Here the physical cutoff converts the fourfold mixed-difference target to \(O(N^{-2})\) in the unscaled contractions.
Sum over the choices of small first pair, and take the sixteenth root from the four Cartesian differences.
The original joint probability is \(O(n^{-s/32})\) conditioned on the past and the allowed guards.

<a id="terminal"></a>
## Exceptional areas and the ordinary determinant

An intermediate compression between two different spaces can be singular identically as a function of \(z\).
Define a bad transition only at a shift where its incoming determinant is nonzero and the outgoing absolute determinant is below the indicated threshold times the incoming absolute determinant.
If a prescribed tuple has a singular incoming compression at an assigned step, the joint bad transition event for that step is empty.
Thus the preceding estimates apply conditionally without any assumption that every intermediate pencil is regular.
After a successful first gap comparison with an invertible original minor, a zero outgoing determinant must first occur in a bad transition.
This observation applies separately to both chronological filtrations, and their exceptions may be unioned.
Possible failures of the global rectangular floors are charged only once; for the flag filtration one tests the current step on the event that the two projected columns are nonzero, without conditioning on future columns.
The original \(M_0-z\) has finitely many poles per realization and their planar sections may be discarded by Fubini.

Take \(D=64\) separated upper-half-plane shifts, choosing one bad step for each inside the flag or inside the restorations, separately for the two types of exceptional area.
The joint estimate and chronological conditioning give \(C_D k^D n^{-D/32}\) or smaller plus the summable guard errors.
Reflection across the real axis and removal of a strip of arbitrarily small area preserve the area conclusion because all inputs and coefficients are real.
If a bad set in the bounded remaining region has area \(>v\), its separated \(D\)-tuples have product area bounded below by a positive constant depending on \(v,D\): choose the separation radius so the first \(D-1\) excluded disks have total area \(<v/2\).
Fubini proves summability of every fixed positive bad-area deviation.
The flag ends at exactly the compression where the restorations begin, by the exterior identity above.

On the remaining parameters in the disk, the two successive comparisons lose at most \(O(k\log N/N)\) after the initial gap estimate.
On every disk the normalized negative part of the final full characteristic log has a deterministic \(L^2\) bound by Jensen and the translated negative logarithmic kernel.
The free target has the same local square bound from its compactly supported Brown measure.
Consequently the initial two-trim limits, the vanishing exceptional areas and Cauchy--Schwarz give the integrated lower limit of the full potential, in the sense \(\int(u-N^{-1}\log|\det(P_N-z)|)_+\,dA\to0\).
The [trimmed full-matrix potential](Yin_C_F0186_v42.md#statement) and the positive logs of the bottom \(q_N\), divided by \(N\), bound the reverse deficit.
Those positive logs are \(O(q_N\log N/N)\) after normalization on the eventual Frobenius norm guards.
This proves the local \(L^1\) limit, and distributional Laplacians and tightness give weak convergence.
Taking independent dimensions and applying converse Borel--Cantelli to the normalized nonnegative terminal integral gives (1): the full and trimmed potentials differ by that integral up to the same negligible omitted positive logs.
For one prescribed nonreal shift the [one-parameter Fourier estimate inside the initial-overlap proof](Yin_C_F0186_v42.md#initial-overlap) costs \(O(h(n/\log K_N)^{-1/2})\) plus polynomially summable guards, with \(K_N=C\log^3(N+2)\).
The two-trim bounds at the original scaling and \(O(k n^{-1/32})\) for the remaining bad ratios then give the pointwise lower bound in probability and almost surely along \(N=2^j\).
For possibly exceptional prescribed poles use the undivided product inequality as in the [finite-variance pointwise argument](Yin_C_F0351_v8.md#limits); both sides are continuous in \(z\) and the strict violation estimate transfers by Fatou from almost every shift.
The fixed-clip upper bound supplies the reverse pointwise log inequality.

## Current assessment
[Selected decision](#decision-oblique-quadratic-reviewed)

## Assessment history

### Decision oblique-quadratic-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:20 |
| status | open |
| reason | The two exterior spaces isolate an independent fresh color, and the resulting scalar and two-site rational tests supply the terminal comparisons. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Quadratic family](#statement) | Finite-variance real laws, integrated terminal series and the nonreal fixed-shift conclusions. |
| argument | [Two distinguished directions](#argument) | The exterior identity and the exact background-tensor test. |
| support | [Kernel directions](#kernels) | Scalar and two-site proofs for the independent or proportional background forms. |
| support | [Exterior flag](#flags) | Correlated left and right column marginals and the physical mixed test. |
| support | [Paired extensions](#restoration) | The oblique Schur identity and quartic mixed differences. |
| support | [Terminal limits](#terminal) | Valid ratios at singular intermediates, the planar series and dyadic dimensions. |

### Decision oblique-quadratic-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:31 |
| status | proved |
| reason | Distinct left and right observed directions remove the stated quadratic cross terms, permitting the original-law Schur comparison and full Brown convergence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Oblique quadratic restoration](#statement) | The model, exact hypotheses, fixed parameters and coupling requirements. |
| argument | [Complete argument](#argument) | Distinct left and right observed directions remove the stated quadratic cross terms, permitting the original-law Schur comparison and full Brown convergence. |
| support | [Free kernels](#kernels) | Independent and proportional forms at the tested shifts. |
| support | [Oblique flags](#flags) | Regular incoming comparisons and joint testing. |
| support | [Paired sites](#restoration) | Fourth mixed differences with the left and right observations. |
| support | [Terminal conclusions](#terminal) | Summable planar deviations and pointwise nonreal dyadic conclusions. |
| dependency | [Initial quadratic estimates](Yin_C_F0186_v42.md#statement) | Finite-variance two trims and first adaptive overlaps. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0358_v9.md#oblique-quadratic-whole-proof) | All stated conclusions at the indicated interfaces. |
