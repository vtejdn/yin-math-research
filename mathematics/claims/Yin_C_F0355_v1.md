---
author: Yin
---

# Symmetric sign pencils in three coefficient directions with two dependent linear forms

<a id="statement"></a>
## A mixed pair of physical variables

Let \(W_1,\ldots,W_g\) be independent real symmetric Wigner inputs with the fixed centered finite-variance laws of [F0012](../tasks/Yin_T_F0012_v3.md#input-model), with strict upper variance one.
For linearly independent \(a,b\in\mathbb R^g\), set \(U=\sum a_jW_j,\ V=\sum b_jW_j\).
Write \(u_0=a\cdot\xi,\ v_0=b\cdot\xi\) for the raw strict upper pair at one site, with \(\xi\) having the independent input laws.
Fix real \(\lambda\notin\{0,-1\}\).
Assume
\[
 \Pr\{\operatorname{Var}(u_0\mid v_0)>0\}>0. \tag{1}
\]
Set \(M=UV+\lambda VU\), \(m_\infty=uv+\lambda vu\) for the corresponding forms in free standard semicirculars, and \(h_N=\lceil\log(N+3)\log\log(N+3)\rceil\).
For every allowed cross-dimensional coupling the normalized potential of \(M\) converges almost surely in local planar \(L^1\) to \(\tau\log|m_\infty-z|\), and the eigenvalue law converges weakly almost surely to the Brown measure.
The normalized disk-integrated sum of the negative logarithms of the last \(h_N\) singular values has summable probabilities of exceeding every fixed positive tolerance.
At each fixed nonreal \(z\), the ordinary normalized log determinant converges in probability and almost surely along \(N=2^j\) to this free value.

For the model with all raw entries independent Rademacher signs up to symmetry, assume also \(\Pr\{\operatorname{Var}(v_0\mid u_0)>0\}>0\).
Then the same pointwise conclusions and the all-size almost-sure dimension-limsup equality hold at **every fixed** \(z\in\mathbb C\), including \(z=0\).
The ordinary scalar determinant statements apply to every fixed scalar polynomial in \(M\), by factorization, with the deterministic constant case interpreted separately.
For every nonconstant such scalar polynomial, and for its exact word-chain pencil, the normalized negative-log excess below any \(N^{-B}\), \(B>0\), vanishes in probability and almost surely along \(2^j\).

In particular these give the ordinary determinant conclusions of [F0013](../tasks/Yin_T_F0013_v1.md#contract) for the fixed pencil
\[
 L(w)=\begin{pmatrix}-z&U&\lambda V\\ V&-1&0\\ U&0&-1\end{pmatrix}
 \tag{2}
\]
under the same fixed-shift conditions, with normalization \(1/(3N)\) and free target \(\tau\log|m_\infty-z|/3\).
Its coefficient space has complex dimension three and every nonzero member has rank at least two.
Indeed a nonzero variable direction has a nonzero top row in the auxiliary columns and a nonzero first column in the auxiliary rows, since \(\lambda\ne0\); when the constant coefficient is used its bottom two-by-two block is invertible.
Independence of \(a,b\) gives the asserted dimension.
For example \(U=X+Y,V=X-Y\) from two independent sign matrices has both conditional-variance properties.
The noncommutative polynomial is then
\((1+\lambda)(X^2-Y^2)+(\lambda-1)(XY-YX)\).
For \(\lambda\ne1\) this includes both squares and a nonsymmetric mixed term.

<a id="argument"></a>
## What remains independent after combining colors

The old minor is formed by restricting all physical inputs before forming the product.
It is a real quadratic in the original independent colors.
Use the [initial two trims and adaptive overlaps](Yin_C_F0186_v42.md#statement) with the same \(V_{JI}\) normals on the two sides, where \(|I|=k=2\lfloor\log^3(N+3)/2\rfloor\) and \(n=N-k\).
These fresh columns have independent nondegenerate entries with the one-dimensional marginal law of \(v_0\) and are independent of the entire old minor.
The rectangular floor for \(V_{JI}\) follows from the [finite-variance rectangular proof](Yin_C_F0351_v8.md#cross-block) after constant variance rescaling.
The normal flag and the reverse restorations can be analyzed under separate exposures.

On the common complement of the columns of \(V_{JI}\) in \(J\), the two extra terms \(U_{JI}V_{IJ}+\lambda V_{JI}U_{IJ}\) in the \(JJ\) block vanish after compression.
In reverse order restore each physical pair \(e_i,Ve_i\).
Freeze \(V,U_{JJ},U_{II}\).
The current vector \(x=U_{Ji}\) is then independent across its coordinates given \(V\), with independent rows across distinct \(i\in I\) at this exposure.
Its conditional laws may depend on the corresponding values of \(V\).
The update on the full matrix is
\[
 F D G^{\mathsf T}+G D F^{\mathsf T},
 \qquad F=[e_i,Ve_i],\quad G=[x,Vx],\quad
 D=\begin{pmatrix}0&1\\ \lambda&0\end{pmatrix},
\]
with \(x\) extended by zero outside \(J\).
Old and future terms from these rows vanish upon the appropriate two-sided projections by the same algebra as the [paired restoration](Yin_C_F0351_v7.md#restore).
The Schur ratio has degree at most four in the current row.
In raw coordinates its top term carries the factor \(\lambda^2N^{-2}\det(F_L^{\mathsf T}F_L)\), with the two-dimensional projected pair \(F_L\) and the determinant of the four quadratic forms of the lifted inverse.
Lower-degree terms may depend on the whole exposure.
On the rectangular floor and \(\|V\|\le N^2\) the geometric factor \(\det(F_L^{\mathsf T}F_L)\ge cN^{-8}\), by taking distance to the span of later pairs.
Frobenius Markov bounds give the polynomial input and column guards outside summable errors.

<a id="masked-panels"></a>
## Choosing independent sites in a conditional law

By (1) there are a measurable set \(S\) of \(v_0\) values of positive probability and constants \(0<d<H,\ p>0,\ K<\infty\) such that
\[
 \mathbb E[u_0^2\mid v_0=v]\le K,\qquad
 \Pr\{d\le|u_0-u_0'|\le H\mid v_0=v\}\ge p \tag{3}
\]
for almost every \(v\in S\), where the two copies have the same conditional law independently.
To see this, cover the positive-variance set up to null sets by countably many choices of rational \(d,H,p\) and integral \(K\), and retain one of positive measure.
This does not require \(v_0\) to have an atom.

Split \(J\) deterministically into four equal-size classes up to rounding.
For each \(i\) choose exactly \(\lfloor n/L\rfloor\) sites from each class where \(\sqrt N V_{ji}\in S\), in their natural order, with a fixed integer \(L>8/\Pr(v_0\in S)\).
The simultaneous choices fail with probability \(O(k e^{-c n})\) by independence of the fresh cross entries.
The selected panels for each \(i\) depend only on the cross block of \(V\).
They are thus independent of the old \(JJ\) inputs even though \(U_{JJ}\) and \(V_{JJ}\) are dependent.
The other entries of the current raw \(U\)-row may be frozen before the four-block comparison.

For either the deterministic flag panels or these chosen restoration panels, the uncompressed kernels are
\(\operatorname{sym}(V_{JJ}^{\,e}(M_0-zI)^{-1}V_{JJ}^{\,f})\) for \(e,f=0,1\).
In the free field the effective generators \(u,v\) are an invertible real linear coordinate change of two directions in the original generator space, completed by any independent remaining directions.
Thus the [scalar and two-site specializations](Yin_C_F0351_v7.md#restore) apply to them, with \(\lambda=1\) using the three symmetric kernels.
For several separated upper-half-plane parameters and their conjugates, the same specialization separates the simple poles at each parameter.
Every real unit combination of the indicated real and imaginary kernels is nonscalar.
For a single real shift only the real kernels are used.
The limiting physical corners between two different panel colors are nonzero by freeness from the coordinate projections, as in the [equal-color proof](Yin_C_F0351_v5.md#sign-flag-area).
The selected panel sizes allow them to be completed to \(L\) classes of equal limiting density.
Condition on the panel choices solely for the probability estimate for the old \(JJ\) data.
Their identities do not affect the marginal count bounds, by invariance of the original Wigner tuple under simultaneous site permutations.
The [bounded approximation and rank argument](Yin_C_F0351_v6.md#physical-corners) applies using the original independent colors, inserting the fixed linear forms \(U,V\) into each word.
It gives positive-proportion singular mass on the original kernel corners, uniformly bounded approximants, and arbitrarily small total rank error relative to the mass margin.
The lifted old inverses add \(O(k)\) rank in every regular restoration.
A union over \(k\) choices is permitted.
This reasoning treats the selected panels as complete positive-density coordinate classes before approximating the inverse; it requires no lower bound on a smallest singular value of a randomly thinned unbounded matrix.

<a id="conditional-tests"></a>
## Fourier bounds for the restored row

The four Cartesian differences leave exactly the three pairings of the determinant Hessian in the [four-block calculation](Yin_C_F0351_v5.md#paired-sign-restoration).
The differences on chosen sites are independent symmetric variables, each with the bounds (3) and second moment at most \(4K\).
For the output-spread test truncate these differences at a sufficiently large fixed \(H'\ge H\).
Condition on the coordinates above \(H'\) and the indicators.
The uniformly bounded second moments and independence give at most a prescribed small fraction of large coordinates except with \(e^{-cn}\) probability.
The remaining symmetric differences are centered, bounded and have variance bounded below by \(pd^2\).
Thus the expected squared norm of any required projected bounded kernel applied to these coordinates is at least a constant times its squared Hilbert--Schmidt norm.
Convex Lipschitz concentration and the unit-direction net yield the same output-spread bound after any small output-coordinate deletion as in [the general border proof](Yin_C_F0351_v6.md#border-tests).
One projects off the errors and the images of the conditioned large vector there, and in the fourth block also off the finite-dimensional nuisance space fixed before testing the third block.

For a fourth-block difference at a selected site, its characteristic function is \(|\phi_v(t)|^2\), where \(\phi_v\) is the conditional characteristic function of the raw \(u_0\).
The proof of the [disjoint-basis Fourier bound](Yin_C_F0351_v6.md#border-tests) applies to nonidentical coordinates here: its one-coordinate Gaussian integral is bounded by \(C l^{-1/2}\) for the \(l\)-th power of this characteristic function.
Indeed restrict \(1-|\phi_v(t)|^2=2\mathbb E\sin^2((u_0-u_0')t/2)\) to the event in (3), use Jensen on the exponential upper bound for \(|\phi_v|^{2l}\), and integrate against a Gaussian with variance bounded below.
The wrapped Gaussian integral is \(O(l^{-1/2})\) uniformly over the translation and all spacings in \([d,H]\).
Products on each basis and Hölder across disjoint bases give \(O(n^{-s/2})\) for \(s\) simultaneous real tests, with no need for identical conditional laws.
The first-pair \(00\) test has the same bound.
If its value is large, the \(11\) coefficient has definite magnitude on the remaining shifts, also for the three-kernel pairing at \(\lambda=1\).
The sixteenth root in the four-block comparison therefore gives \(O(n^{-s/32})\) for \(s\) assigned bad restoration ratios at the same step.
The ordinary flag bound \(O(n^{-s/8})\) uses the iid marginal \(v_0\) on its fresh columns.
The bounds apply at regular incoming determinants.
Starting from the nonzero first compression, any later first zero is detected by a tested bad ratio.
For a fixed separated tuple the required old-corner and panel guards are paid once under each of the two exposures.

Use thresholds \(N^{-7}\) for the flag and \(N^{-12}\) for restoration; the latter makes the width of the raw fourth mixed difference bounded even on the polynomial Gram guard.
With 16 and 64 shifts respectively, summing assignments to the \(k\) steps gives summable \(O(k^{64}n^{-2})\) or smaller errors, apart from the summable original guards.
The separated-tuple area argument and the [quadratic initial-area estimate](Yin_C_F0186_v42.md#initial-overlap) give vanishing exceptional areas almost surely on each disk.
The complement has an ordinary log lower bound by the old \(2h_n\)-trim minus \((2h_n/N)\log^-t_{2h_n+1}\) and a deterministic \(O((h_n^3+k)\log N/N)\), by the [adaptive compound comparison](Yin_C_F0351_v1.md#adaptive-gap) with the larger gap exponent used in C186v42.
The two old trims, local square integrability of the final characteristic potential and the full-matrix trimmed limit yield local \(L^1\) convergence as in [the terminal argument](Yin_C_F0351_v8.md#limits).
Distributional Laplacians and tightness give the weak Brown limit, and independent dimensions with converse Borel--Cantelli give the marginal series.
At each fixed nonreal shift the single-direction initial test in C186v42 costs \(O(h_n\sqrt{\log\log(n+3)/n})\) plus its polynomial guards.
The subsequent single tests cost \(O(kn^{-1/32})\).
These are summable on \(2^j\).
The [undivided product comparison](Yin_C_F0351_v3.md#fixed-compressions) uses continuity to handle prescribed exceptional poles, without assuming a continuous input distribution.
The two old-minor moving trims and the fixed-clip upper bound finish the pointwise conclusions.

<a id="real-signs"></a>
## Fixed real targets in the original sign model

For the real-axis argument the reverse positive conditional-variance assumption is used as well.
The variables \(U,V\) have bounded fixed raw laws and bounded conditional means.
Fix \(0.9N\le n\le N\).
Condition on the old \(V\), and mark each strict upper pair for which its raw \(V\)-value belongs to the set in (3).
With exponentially high probability each column has at least \(cn\) incident marked pairs, by independence before conditioning and a union bound.
On a marked pair the conditional variance of the \(U\)-entry before physical normalization is at least \(p d^2/2\).
The centered perturbation \(U-\mathbb E[U\mid V]\) has independent entries above and on the diagonal conditional on \(V\), with all raw variances bounded.
For any fixed unit \(h\), its expected squared output norm on \(h\) is at least a constant by the column degrees.
The expectation of its squared projection onto any rank-\(l\) space is at most \(Cl/N\): for a unit output vector \(y\), the squared raw coefficient sum in the real symmetric bilinear form is bounded by \(C\|y\|^2\|h\|^2\), by pairing mirrored entries.
Hence for any projection \(Q\) off at most \(\epsilon n\) dimensions, \(\mathbb E[\|QUh\|^2\mid V]\ge c'\) on this degree guard for small fixed \(\epsilon\).
The conditional mean adds a nonnegative square.
The raw bounded-product concentration for this convex norm, of Lipschitz constant \(O(N^{-1/2})\), allows nets on any \(V\)-measurable subspace of dimension at most a sufficiently small fixed fraction of \(n\).
The same conclusion holds with \(U,V\) interchanged using the reverse conditional variance.
The actual norms of both forms are bounded outside exponentially small exceptions by the norm bounds of the original sign inputs.
The fixed-width spectral windows of each form contain at most \(\epsilon n\) sites in spectral dimension outside exponentially small exceptions by its scalar Wigner limit (rescaled by its nonzero raw standard deviation) and row-rank concentration.
These facts prove the [spectral-window separation](Yin_C_F0351_v7.md#spectral-gap) for the actual mixed pair.
The companion covariance in [the real-shift trim proof](Yin_C_F0351_v7.md#trim) is bounded below by the smallest eigenvalue of the raw \(2\)-by-\(2\) covariance of \((u_0,v_0)\) times the sum for independent unit-variance colors.
This eigenvalue is positive by linear independence of \(a,b\).
For concentration of the projected borders use independent bounded original sign inputs and their fixed linear maps.
The fixed-fraction initialization applies since the product is homogeneous in the original inputs and the free companion is full at each shift.
Thus both trims converge at every prescribed real shift, also for real shifts varying toward it, with summable chain exceptions under each coupling.

For the initial overlap at these real shifts, every unit real or complex sparse vector \(h\) on at most \(\epsilon n\) coordinates has a fixed lower residual except on an exponentially small fixed-vector event, uniformly in its support and in bounded shifts.
To see this choose a nonzero ordered monomial \(W_i W_j\) in the quadratic and two disjoint panels of \(\lfloor n/4\rfloor\) sites outside the support.
Take mixed differences in the raw sign rectangles of color \(j\) from the support to the first panel and of color \(i\) from there to the second panel.
The second-panel output retains precisely the nonzero coefficient times the product of these two independent difference rectangles applied to \(h\).
Disjoint physical sites ensure this identity even when \(i=j\).
For any real unit vector the Euclidean output of each rectangle is bounded below by a fixed constant outside \(Ce^{-cn}\), by independent bounded row sums, variance and the fourth-moment estimate.
For complex \(h\) use its larger real or imaginary part.
The four-corner Cauchy--Schwarz inequality now gives the asserted fixed-vector estimate.
A fixed fine net and the input norm bounds yield physical incompressibility for every sufficiently small near-null vector, also for the transpose.
Thus at least \(cn\) of its coordinates have a real or imaginary component of size at least \(c'/\sqrt n\).
For the \(V\) marginal, choose any two different atoms; on a fixed positive fraction of those coordinates the law can be realized as a fair draw on this pair by mixture splitting.
A binomial tail and the [antichain estimate](Yin_C_F0351_v7.md#overlap) give \(O(n^{-1/2})\) conditional small-ball probability at scale \(N^{-5}\).
This suffices for the first \(O(h_n)\) overlaps.
At a prescribed real shift the actual real kernel family in the restoration has the independence checked above under real scalar specializations; use one real parameter rather than an upper/lower conjugate pair.
The regular tests and undivided limit may be taken along the real axis since the old compression here is orthogonal on both sides and all its characteristic polynomials are monic.
This proves the same all-size convergence in probability and dyadic almost-sure limit at real targets, including zero.
For a scalar polynomial in the product use factorization at the finite list of roots, and the common Schur multiplier for (2).
For the bottom-log excess at \(N^{-B}\), compare the full logarithm with each fixed positive clip, use the pathwise convergence of the fixed clip and then send it to zero.
For \(U=X+Y,V=X-Y\), zero of either raw form has probability \(1/2\), and the other form there takes both \(2\) and \(-2\), verifying both conditional assumptions directly.
The proof works on the original product of independent physical sign matrices.

## Current assessment
[Selected decision](#decision-conditional-mixed-reviewed)

## Assessment history

### Decision conditional-mixed-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:25 |
| status | open |
| reason | Positive conditional variance leaves enough fresh sites to apply the original quadratic restoration tests in three coefficient directions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Mixed quadratic and three-direction pencil](#statement) | Finite variance planar result and all fixed shifts in the indicated sign family. |
| argument | [Conditional exposure](#argument) | Original coupling and the unaffected first flags. |
| support | [Conditional panels](#masked-panels) | Independence from the original principal minor and lower rank of true physical corners. |
| support | [Nonidentical fresh draws](#conditional-tests) | Conditional row concentration and the four-block mixed difference. |
| support | [Real shifts](#real-signs) | Conditional spectral-window tests, original sign-model floor-scale excess and dyadic limits. |

### Decision conditional-mixed-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:31 |
| status | proved |
| reason | Conditioning on one mixed form leaves a positive density of usable original coordinates, and the bidirectional sign condition gives the fixed real-shift conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two correlated forms and three coefficient directions](#statement) | The model, exact hypotheses, fixed parameters and coupling requirements. |
| argument | [Complete argument](#argument) | Conditioning on one mixed form leaves a positive density of usable original coordinates, and the bidirectional sign condition gives the fixed real-shift conclusion. |
| support | [Selected site classes](#masked-panels) | Independence from the original principal minor. |
| support | [Conditional row tests](#conditional-tests) | Uniform nonidentical distributions on the chosen panels. |
| support | [Real targets](#real-signs) | The sign model, both conditional variances and the deterministic even sequence. |
| dependency | [Initial quadratic estimates](Yin_C_F0186_v42.md#statement) | Finite-variance two trims and first adaptive overlaps. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0363_v1.md#conditional-mixed-whole-proof) | All stated conclusions at the indicated interfaces. |
