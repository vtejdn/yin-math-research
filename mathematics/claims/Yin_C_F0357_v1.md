---
author: Yin
---

# Ordinary determinants at real shifts of the sum of two squares and their commutator

<a id="statement"></a>
## Scalar and three-channel determinants

Let \(A,B\) be independent real symmetric Wigner matrices with fixed centered laws, variance one above the diagonal, finite second moments on and above the diagonal, independent upper-triangular entries, and normalization \(N^{-1/2}\).
This includes two independent matrices with the original independent Rademacher signs on and above the diagonal.
Put \(P_N=A^2+B^2+AB-BA\), let \(p\) be its evaluation at two free standard semicircular elements, and put \(u(z)=\tau\log|p-z|\).
Use the affine pencil
\[
 L_N(z)=\begin{pmatrix}-zI&A&B\\ A+B&-I&0\\-A+B&0&-I\end{pmatrix}
\]
and its free evaluation \(L(z)\).
Its two variable coefficients have rank two, and they and its constant matrix are linearly independent, also at \(z=0\).

For every prescribed real \(z\), \(N^{-1}\log|\det(P_N-zI)|\) tends to \(u(z)\) in probability in all dimensions and almost surely along \(N=2^j\) under every coupling across sizes.
Its all-dimension limsup equals \(u(z)\) almost surely under every such coupling.
The corresponding assertions for \((3N)^{-1}\log|\det L_N(z)|\) have target \(\log\Delta_{\operatorname{tr}_3\otimes\tau}(L(z))=u(z)/3\).
The target is finite, and ordinary determinants count exact zeros with \(\log0=-\infty\).
The event may depend on the prescribed shift.
The [two-coordinate restoration theorem](Yin_C_F0351_v11.md#statement) covers the nonreal parameters and planar Brown convergence for this same polynomial.

More precisely, for \(h_N=\lceil\log(N+3)\log\log(N+3)\rceil\), write \(t_i(D)\) for the singular values in increasing order.
For either \(D=P_N-zI\) of dimension \(mN=N\) or \(D=L_N(z)\) of dimension \(mN=3N\), define
\[
 H_N(D)=\frac1{mN}\sum_{i\le h_N}\log^-t_i(D),\qquad
 E_{N,b}(D)=\frac1{mN}\sum_i\log\frac{\max(t_i(D),N^{-b})}{t_i(D)}
 \quad (b>0).
\]
Use \(+\infty\) for either loss at a zero singular value and consider dimensions \(N>h_N\).
For each \(\epsilon,b>0\) the probabilities that either loss exceeds \(\epsilon\) tend to zero, and their sums along \(N=2^j\) are finite.
For any deterministic \(\eta_N\downarrow0\), the same conclusions hold for the normalized sum of \(\log^-t_i(D)\) over all \(t_i(D)\le\eta_N\).
The singularity probabilities and the probabilities of each fixed positive absolute deviation of the ordinary normalized log determinant from its target are likewise summable along \(2^j\).
The assertion uses no independence between dimensions.

On every compact subset of \(\{z\in\mathbb C:\operatorname{Re}z\le|\operatorname{Im}z|\}\), the same ordinary normalized scalar potentials in fact converge uniformly almost surely in all dimensions, including on either boundary ray and at zero.
The exact factor \(1/3\) gives the uniform limit for the displayed pencil as well.

<a id="argument"></a>
<a id="joint"></a>
## Two independent Wigner matrices have no common approximate eigenvector at bounded energies

We use deterministic principal minors of size \(l=N-o(N)\), still normalized by \(N^{-1/2}\), denoted here by \(X,Y\).
For any fixed \(J_0<\infty\), outside summable probabilities, the following holds at every one of the at most \(N\) prescribed nested sizes needed below, with \(\alpha,\beta\in[-J_0,J_0]\) and all complex unit \(v\):
\[
 \|(X-\alpha)v\|+\|(Y-\beta)v\|\ge N^{-3}.
 \tag{1}
\]
The Frobenius Markov bound \(\|A\|,\|B\|\le N^2\) costs \(O(N^{-3})\) once for the whole chain.

To see (1), choose \(0<\gamma<1/2\) small enough for the [affine finite-variance singular count](Yin_C_F0186_v40.md#argument) at \(\delta=N^{-\gamma}\).
The constants for \(X-\alpha\) are uniform for \(\alpha\) in the fixed compact interval enlarged by one and \(l/N\to1\).
Indeed these scalar full pencils, with variable coefficient \(\sqrt{l/N}\), form a compact full family on replacing \(l/N\) by the range \([1/2,1]\), as in the [principal-minor comparison](Yin_C_F0186_v42.md#old-trim).
Choose \(\gamma\) strictly below the admissible exponent to account for \(l/N\).
Hence the expected normalized eigenvalue count for \([\alpha-2\delta,\alpha+2\delta]\) is \(O(\delta^\eta)\) for some \(\eta>0\).
On a \(\delta\)-grid of centers covering \([-J_0,J_0]\), [bounded-rank row concentration](Yin_C_F0186_v4.md#row-concentration) bounds every such count by \(l/\log^2 N\) outside \(O(N^{1+\gamma}\exp(-cN/\log^4 N))\) after summing over all centers and minors.
Here the bound \(l/\log^2 N\) refers to the unnormalized count.

Condition on \(X\), fix a real unit vector \(w\) in any one of these spectral subspaces, and select half the sites carrying at least half its squared norm, rounding the size up.
On the opposite half condition on the principal block of \(Y\) there.
The rows of the remaining rectangle are independent and have the strict upper law.
Uniformly in \(\beta\) and the conditional row shifts, the [finite-variance rectangular row estimate](Yin_C_F0196_v6.md#truncated-core) bounds \(\Pr\{\|(Y-\beta)w\|\le c_0\}\le Ce^{-cl}\) for some \(c_0>0\).
In that estimate the squared centered weighted row sums are uniformly integrable after fixing their coefficient norm, by truncation in \(L^2\).
Symmetrization and their variance lower bound give a fixed escape probability from each interval at the row scale, so a positive proportion of the independent rows escape with the stated probability.
Take an \(N^{-3}\)-net in each real unit sphere, of size \(\exp(O(l/\log N))\), and a fixed mesh smaller than \(c_0/8\) in \(\beta\).
On the single norm guard the net approximation costs \(O(N^{-1})\).
Thus every unit vector in each real slice has residual at least \(c_0/2\) for all tested energies, after decreasing \(c_0\) if necessary.
The same lower bound holds on its complexification by summing the squared residuals of real and imaginary parts.
The union over all nets, centers and minors has exponentially small conditional error on the slice-rank guard, in addition to the previously charged norm error.
If \(\|(X-\alpha)v\|<N^{-3}\), the projection of \(v\) off the slice at a nearest grid center has norm at most \(N^{-3}/\delta\) by the spectral theorem.
On the norm guard its contribution to \((Y-\beta)v\) is \(O(N^{-1+\gamma})\), proving (1).

<a id="real-trim"></a>
## Trimming at a prescribed real parameter

Fix \(z\) in a bounded real interval.
Write \(Q=\left(\begin{smallmatrix}1&1\\-1&1\end{smallmatrix}\right)\) for the quadratic tensor.
Take either \(P=P_*\) or its transpose polynomial.
For every complex unit \(w\),
\[
 \operatorname{Re}\langle w,P(X,Y)w\rangle=\|Xw\|^2+\|Yw\|^2 .
\]
Thus if \(\|(P(X,Y)-z)w\|\le1\), the real scalars \(\alpha=\langle w,Xw\rangle,\ \beta=\langle w,Yw\rangle\) lie in a compact interval depending only on the bound on \(|z|\).
With \(E_w=I-ww^*\), (1) bounds \(\|E_wXw\|+\|E_wYw\|\) from below by \(N^{-3}\).

Here is how this replaces the nonreal-parameter step in the [quadratic companion border estimate](Yin_C_F0186_v42.md#border).
Use the displayed three-channel linearization with factorization \(Q=UV,\ U=I,\ V=Q\), and for the transpose use \(U=Q^{\mathsf T}, V=I\).
Both factors are invertible with fixed norm and inverse norm.
If a unit left vector \((v,y)\) of the companion has residual at most \(\tau=N^{-12}\), its equations give \(y=U^{\mathsf T}(Xv,Yv)^{\mathsf T}+O(\tau)\), \(\|v\|\ge cN^{-2}\) and \(\|(P^{\mathsf T}-z)v\|\le CN^2\tau\).
The normalized physical vector therefore satisfies the preceding energy bound.
In the notation of the border estimate, \(Z_i=\sum_jQ_{ji}X_j\), taking \(X_1=X,\ X_2=Y\) and the transposed tensor in the transposed calculation.
Invertibility of that tensor gives \((\sum_i\|E_{v/\|v\|} Z_iv\|^2)^{1/2}\ge cN^{-3}\|v\|\).
For any unit border direction \((a_0,a')\) with \(|a_0|\le c_1N^{-2}\), the \(Ua'\) term times \(v\) dominates the terms proportional to \(a_0\), by the upper bound on \(y\) and sufficiently small \(c_1\).
For \(|a_0|>c_1N^{-2}\), projection away from the line of \(v\) leaves a norm at least \(cN^{-5}\|v\|-C\tau\).
These two alternatives give a floor \(N^{-8}\) on the raw directional map on either near-null space for large \(N\).

With these two polynomial powers in place of the powers in the cited proof, each paired border retains its original logarithmic cost \(O(\log N)\).
Indeed the tail projections supply at least a constant fraction of the current deficit \(q\) singular directions at the stated polynomial floor, or the retained product gains from singular values exceeding \(\tau\).
The projection and net estimates in [the paired border calculation](Yin_C_F0186_v42.md#border) give conditional errors \(CN^C e^{-cq}+CN^{-3}\) when the current minor satisfies its directional guard.
Test a failure only when that current guard holds and pay the probability of any failed guard separately using (1).
All nested residuals use the original independent physical row at that step.
The [trim initialization and transfer](Yin_C_F0186_v42.md#old-trim), starting \(\lfloor n/\log^3(n+3)\rfloor\) rows below a target \(n=N-o(N)\), use compact full pencils at these real shifts as well.
The initial expected clip comparison, fixed-clip upper bound and triangular-factor comparison there use fullness and boundedness of the coefficient family, including at \(z=0\), since \(P_*-z\) is a nonzero free polynomial.
Summing the step errors with \(q\ge h_n\) gives a summable series in \(N\), and the cumulative normalized cost tends to zero.
In particular for \(n=N\) and \(n=N-2\lfloor\log^3(N+3)/2\rfloor\), writing \(T=P(A_{[n]},B_{[n]})-zI\) and \(p_j\) for the product of the largest \(j\) singular values, under each coupling almost surely
\[
 N^{-1}\log p_{n-j}(T)\longrightarrow u(z)\quad(j=h_n,2h_n),\qquad
 (h_n/N)\log^-t_{2h_n+1}(T)\longrightarrow0 .
 \tag{2}
\]
The last assertion follows by subtracting the two trimmed products on \(t_{2h_n+1}<1\).

<a id="real-restoration"></a>
## A single real shift in the two-coordinate restoration

Set \(k=2\lfloor\log^3(N+3)/2\rfloor,\ n=N-k,\ h=h_n\).
For a fixed \(N\) and Lebesgue almost every real \(z\), the original old minor \(T\) is nonsingular almost surely, by Fubini applied to its monic characteristic polynomial.
At such a shift take the bottom left and right frames and the adaptive gap \(r\le2h\) of the [initial rank perturbation](Yin_C_F0351_v11.md#initial).
At real \(z\) all singular spaces can be framed over \(\mathbb R\).
For \(r>0\), every selected bottom unit vector has residual at most \(C_R N^4N^{-a h}\) for \(T\) or its transpose on the norm guard.
The [finite-variance sparse-vector bound](Yin_C_F0186_v42.md#word-spread) applies directly with \(H=P_*-z\) or \(P_*^{\mathsf T}-z\), since the \(x^2\) coefficient is one.
Thus, outside \(O(N^{-J})\) for any prescribed \(J\), every such real vector stays \(K^{-C}\) from supports of size \(c n/\log K\), where \(K=C_J\log^3(N+2)\), uniformly in each prescribed shift on the bounded interval.
After removal of any such set the remaining vector has norm at least \(K^{-C}\).
Successive largest remaining coordinates therefore give at least \(c n/\log K\) individual coordinates of magnitude at least \(K^{-C}/\sqrt n\), reducing \(c\) to handle rounding.

At each Gram--Schmidt stage choose a real unit vector in the frame orthogonal to the preceding projected raw columns.
The [one-dimensional basis Fourier bound](Yin_C_F0351_v6.md#border-tests) on these large coordinates, after multiplying by \(N^{b_0-1}\) for the exponent \(b_0=20\cdot12+10\) of the initial rank comparison, gives
\(\Pr\{|w^{\mathsf T}g|\le N^{-b_0}\}\le C\sqrt{\log K/n}\) for the fresh raw column \(g\).
The choices depend only on the minor and the preceding columns.
On the raw norm guards, Gram--Schmidt gives exactly the overlap \(N^{-(b_0+2)r}\) required there on each side, outside \(O(h\sqrt{\log K/n}+hN^{-3}+N^{-J})\).
This includes any fixed centered strict upper law of positive variance.

The [exact graph compression](Yin_C_F0351_v11.md#square) removes the fresh square and identifies the initial determinant with the one from these positive rank perturbations divided by \(\det(I+V^{\mathsf T}V)\).
All later initial updates and [paired restorations](Yin_C_F0351_v11.md#restoration) use the same real rows, normal bounds and rank comparisons at a real shift.
For clarity, the four old inverse kernels are the transpose-symmetric parts of \(R,\ R(A_0-B_0),\ (A_0+B_0)R,\ (A_0+B_0)R(A_0-B_0)-I\), where \(R=T^{-1}\).
They are real at a regular real shift.
The [polynomial specialization](Yin_C_F0351_v11.md#kernels) makes their scalar numerators, modulo scalars, \(1,d,c,cd\), with denominator \((c^2+d^2)/2-z\).
No nonzero linear combination of these numerators is a multiple of the denominator, by the coefficients of \(c^2,d^2\), also at \(z=0\).
This supplies the four real directions modulo scalars on a single real node.
Continuity in measure of the inverses of the full free polynomial on a compact real interval gives the uniform free corner spread by the [distinct-site corner argument](Yin_C_F0351_v9.md#kernels).
The corresponding physical estimate uses bounded approximants, inverse regularization and rank errors from clipping at a fixed small singular threshold on each prescribed shift.
Fullness gives a uniform free small mass on the compact interval by the [free power estimate](Yin_C_F0352_v1.md#statement) applied to its companion and bounded free Schur factors.
Thus the finite comparison costs the same exponentially small old-minor probabilities and permits the same additional \(O(k)\)-rank errors as in the [physical kernel transfer](Yin_C_F0351_v11.md#kernels).
Real directions alone suffice for the one-node test.

At regular incoming steps the two-panel quadratic test costs \(O(n^{-1/8})\) per positive rank update and the four-panel determinant test costs \(O(n^{-1/32})\) per restoration, as in those two proofs with one assigned shift.
In the latter test the fourth-panel coefficient of the \(11\) kernel is the first pair's \(00\) value, which has small-ball probability \(O(n^{-1/2})\) before the four Cartesian differences.
The four real kernel directions just verified give conditional spread when that coefficient exceeds the fixed threshold, also after removal of the finitely many other pairing directions.
The chronological union bound charges a zero outgoing determinant at its first failed ratio and does not condition on future columns.
Together with the preceding initial bound, the rectangular floor and the norm guards, this proves the [undivided determinant inequality](Yin_C_F0351_v11.md#terminal)
\[
 |\det(P_N-zI)|\ge e^{-C(h^3+k)\log N}\,
 p_{n-2h}(T)\min(1,t_{2h+1}(T))^{2h}
 \tag{3}
\]
outside \(O(h\sqrt{\log K/n}+k n^{-1/32})\) plus summable guard probabilities, with constants uniform on that compact interval, for almost every prescribed real shift.
Any exceptional prescribed real \(z\) is the limit of real shifts for which this estimate holds, taken in a slightly larger compact interval.
Both sides of (3) are continuous at every \(z\) for every realization, including the poles.
Fatou's lemma for indicators of strict violation therefore preserves the probability bound at every prescribed real \(z\).

<a id="limits"></a>
## Ordinary determinants and the bottom singular values

The right-hand side of (3) has normalized logarithm tending almost surely to \(u(z)\) by (2).
The failure probabilities vanish and are summable on powers of two.
The [fixed-clip upper bound](Yin_C_F0186_v4.md#regularized-potentials) supplies the all-dimension almost-sure upper limit.
This proves the scalar convergence in probability and the dyadic almost-sure convergence, and the dyadic lower limit gives the stated almost-sure limsup.
The unit triangular Schur factors with auxiliary pivot \(-I_{2N}\) identify the full finite absolute determinants exactly, and the free factors have determinant one, giving the stated normalization at both levels.
Finiteness follows from [fullness and the free power bound](Yin_C_F0352_v1.md#statement).

Subtract the ordinary logarithm from the trim at \(n=N,j=h_N\) in (2).
The two differ by the bottom negative logs up to the omitted positive logs, which are \(O(h_N\log N)\) on the norm guard.
This gives the convergence to zero of \(H_N\) in probability and almost surely on powers of two for the scalar matrix.
The three-channel triangular factors and their inverses have norms bounded by a fixed power of \(N\) on the same guard.
Every ordered singular value therefore compares within such a factor to the corresponding value of \(\operatorname{diag}(P_N-zI,-I_{2N})\), with zeros preserved.
The sum of its first \(h_N\) negative logs equals that of the scalar matrix, since inserting ones leaves this sum unchanged.
The resulting \(O(h_N\log N)\) error gives the assertion for the pencil with physical normalization \(3N\).

For either matrix use a fixed lower clip \(d\in(0,1)\).
For all sufficiently large \(N\) its \(N^{-b}\)-clipped normalized logarithm lies between the ordinary normalized logarithm and its \(d\)-clipped counterpart.
The latter converges almost surely to its free clipped counterpart by the [finite-variance singular law and positive-log tails](Yin_C_F0186_v4.md#regularized-potentials), applied to the respective matrix or scalar polynomial.
As \(d\downarrow0\) this counterpart decreases to the finite ordinary target for either matrix.
Taking the difference from the ordinary log proves the asserted convergence of \(E_{N,b}\) in probability and almost surely on powers of two.

For \(0<d<1\) one has \(\log^-t\le2\log^+(d/t)\) on \(t\le d^2\).
For each such fixed \(d\), eventually \(\eta_N\le d^2\).
Bound the literal bottom loss by twice the difference of the fixed-\(d\) clipped log and the full log and then decrease \(d\) to zero.
This proves its convergence in probability and almost surely along the dyadic sizes.

All convergence statements so obtained apply in particular to the product of the prescribed dimension marginals.
Under that coupling the events of a prescribed deviation in distinct dimensions are independent.
Converse Borel--Cantelli therefore gives summability of each dyadic deviation probability, including the losses and ordinary log deviations, from their almost-sure dyadic limits.
A zero determinant forces infinite loss, so the singularity series on powers of two is finite as well.
These are marginal probability statements and hence apply to the original arbitrary coupling.

<a id="sector"></a>
## Uniform convergence up to the two boundary rays

Let \(G=(A+iB)/\sqrt2,\ H=GG^*,\ J=G^*G\), so that \(P_N=(1+i)H+(1-i)J\).
For \(\operatorname{Re}z\le|\operatorname{Im}z|\) choose \(\theta=\pi/4\) or \(-\pi/4\) with \(\operatorname{Re}(e^{i\theta}z)\le0\).
The Hermitian part of \(e^{i\theta}(P_N-zI)\) dominates \(\sqrt2 J\) in the first case and \(\sqrt2 H\) in the second.
On the span of eigenvectors of this positive matrix with eigenvalues above a threshold, the norm of \((P_N-zI)v\) dominates the corresponding quadratic form on each unit \(v\).
The singular-value min--max formula therefore gives \(t_i(P_N-zI)\ge\sqrt2\,t_i(G)^2\) for every \(i\).
At any lower clip \(d>0\) this bounds the full normalized scalar clipping loss by twice the normalized clipping loss of \(G\) at \(2^{-1/4}\sqrt d\), uniformly on the entire indicated region.

Apply the [additive ordinary determinant theorem](Yin_C_F0186_v24.md#statement) to \(A+iB\) at zero and rescale by \(1/\sqrt2\).
The normalized ordinary log for \(G\) converges almost surely in all dimensions to a finite target.
The [finite-variance singular law](Yin_C_F0186_v4.md#finite-variance-weak) and [positive-tail control](Yin_C_F0186_v4.md#positive-tail) give the corresponding fixed-lower-clip limits.
Taking countably many clips decreasing to zero shows that the limsup of the clipping loss of \(G\) tends to zero almost surely.
For the scalar polynomial at any fixed positive clip the same two inputs give pointwise almost-sure convergence of the clipped potentials.
These functions and their free counterparts are Lipschitz in \(z\) with constant \(1/d\), by the singular-value perturbation bound and the Lipschitz property of the lower-clipped logarithm (or its tracial singular-number version).
Consequently convergence at a countable dense set is uniform on every compact set for each of the countably many clips.
The uniform clipping estimate for \(G\) makes the limiting clipped functions uniformly Cauchy on each compact subset of the stated region, since their finite-dimensional differences have this bound.
Their pointwise decreasing limit is \(u(z)\) by the definition of the ordinary free determinant.
The same uniform clipping estimate gives uniform convergence of the ordinary potentials there in all dimensions.

## Current assessment
[Selected decision](#decision-real-axis-reviewed)

## Assessment history

### Decision real-axis-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:15 |
| status | open |
| reason | The finite-variance common approximate eigenvector estimate supplies the real-shift border bound and real one-node restoration controls the ordinary determinant. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [The real-shift determinants](#statement) | Original fixed real finite-variance models, each prescribed real shift, dyadic losses and the three-channel normalization. |
| argument | [Joint approximate eigenvectors](#argument) | Small spectral slices and independent rectangular rows on nested minors. |
| support | [Real trims](#real-trim) | Energy identity and directional border floor for the two real orientations. |
| support | [Ordinary determinant comparison](#real-restoration) | Real sparse overlap, four real symmetric kernels and continuity at old-minor poles. |
| support | [Limits and loss](#limits) | Coupling-uniform convergence and marginal dyadic summability. |
| support | [Full-sequence sector estimate](#sector) | Singular-value domination and uniform clipping up to the boundary rays. |
| dependency | [Two-channel restoration](Yin_C_F0351_v11.md#terminal) | The undivided inequality with the original principal minor and the graph denominator. |
| dependency | [Quadratic principal-minor argument](Yin_C_F0186_v42.md#old-trim) | Trim assembly once the directional estimate holds. |

### Decision real-axis-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:18 |
| status | proved |
| reason | The exclusion of common approximate eigenvectors gives real-shift trims, and the one-node restoration and clipping estimates prove the ordinary determinant and bottom-loss limits for both normalizations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Two-square scalar polynomial and three-channel pencil](#statement) | Every prescribed real shift, dyadic deviations, and the closed-region uniform assertion. |
| argument | [Complete proof from the joint approximate-vector estimate](#argument) | Finite-second-moment real Wigner matrices on every required principal minor. |
| support | [Real restoration](#real-restoration) | Original-law physical kernels and a continuous comparison at possible old-minor poles. |
| support | [Ordinary and bottom logarithms](#limits) | Both trace normalizations, exact zeros and dyadic summability. |
| support | [Full-sequence convergence on compact sets](#sector) | Uniform control of all shifts in the indicated closed region. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0365_v1.md#real-axis-whole-proof) | Fixed theorem, dependencies, and application of the same clipping deduction to prescribed nonreal shifts. |
