---
author: Yin
---

<a id="rectangles-and-total-log-loss"></a>
# A realizable rank-one resonance preserves physical rectangles but loses a fixed logarithmic mass

This ordinary development for Yin, dated 2026-11-06T11:28 UTC, tests a deterministic shortcut for the free-gap branch of [F13](../tasks/Yin_T_F0013_v1.md#contract).
It constructs positive definite size-three pencils with the correct gapped free weak limit, uniformly bounded parent norm, constant lower bounds for all but one eigenvalue, and all small-support physical rectangles through any prescribed fixed number of physical deletions.
Nevertheless one eigenvalue is exponentially small and the normalized total negative logarithmic loss tends to a prescribed positive constant.
One fixed collection of bounded original laws realizes every specified finite matrix with positive probability.
Those probabilities are exponentially small, so the construction is not a probability counterexample to F13 or to an actual-model averaged estimate.
This is ordinary research and authoring self-checking, without independent review or Claim adoption.

The [total-loss formulation in C194v20](../claims/Yin_C_F0194_v20.md#model) is the target of the test.
The [L63v7 matching cancellation](Yin_L_F0063_v7.md#fixed-law-realization-and-rectangle-boundary) fails its rectangle hypothesis, whereas the present construction deliberately retains a lawful rectangle good event.
The two findings concern different failed implications; no cancellation of an entire Schur coefficient layer is asserted here.

<a id="fixed-coefficients-and-uniform-norm"></a>
## Fixed coefficients and a uniform bounded-input norm event

Use physical-first coordinates and the six real symmetric coefficients
\[
 \begin{aligned}
 A_1&=E_{11},&A_2&=E_{22},&A_3&=E_{33},\\
 A_4&=E_{12}+E_{21},&
 A_5&=E_{13}+E_{31},&
 A_6&=E_{23}+E_{32},
 \end{aligned}
 \qquad A_0=300I_3.
 \tag{Resonance-fixed-coefficients}
\]
Every noise coefficient has operator norm one.
The [symmetric-basis argument](Yin_L_F0063_v3.md#positive-frame-physical-boundary) gives the positive complex-direction frame \(\chi_A>0\).
Let \(s_1,\ldots,s_6\) be free centered variance-one semicircular elements in a finite tracial von Neumann algebra with faithful trace \(\tau\), and put \(\tau_3=\operatorname{tr}_3\otimes\tau\).
The corresponding free pencil
\[
 L=300I_3+\sum_{j=1}^6A_j\otimes s_j
\]
has spectrum contained in \([288,312]\), since \(\|s_j\|=2\).
Write \(v=\log\Delta_{\tau_3}(L)\), which is finite.

The norm argument used below is uniform over all centered real off-diagonal laws supported in \([-2,2]\) and centered diagonal laws supported in \([-1,1]\).
For a deterministic real unit vector \(x\), the quadratic form \(x^TW_Nx\) is centered.
Replacing one raw off-diagonal entry changes it by at most \(8|x_ix_j|/\sqrt N\), and replacing one raw diagonal entry changes it by at most \(2x_i^2/\sqrt N\).
Thus the sum of squared replacement bounds is at most
\[
 \frac{64}{N}\sum_{i<j}x_i^2x_j^2+
 \frac4N\sum_i x_i^4\le\frac{36}{N}.
\]
The accepted bounded-differences inequality used in [C187v4's norm argument](../claims/Yin_C_F0187_v4.md#spectral-residual-spread) therefore gives
\[
 \mathbb P\{|x^TW_Nx|>t\}\le2e^{-Nt^2/18}.
\]
For a real \(1/4\)-net of size at most \(9^N\), the elementary quadratic-form net inequality is \(\|W_N\|\le2\max_x|x^TW_Nx|\).
At \(t=10\), a union bound gives
\[
 \mathbb P\{\|W_N\|>20\}
 \le2\exp[-N(100/18-\log9)]\le2e^{-3N}.
 \tag{Uniform-bounded-law-norm}
\]
This derivation checks the needed uniformity directly; no law-dependent constant is silently reused after the later atomic-law construction.
The underlying bounded-differences source is reused only at its accepted scope and inspection depth in C187v4 and [C186v4](../claims/Yin_C_F0186_v4.md#argument).

Let \(B_{j,N}\) be six independent zero-diagonal Rademacher Wigner matrices normalized by \(N^{-1/2}\), and put
\[
 H_N=300I_{3N}+\sum_{j=1}^6A_j\otimes B_{j,N},
 \qquad
 v_N=N^{-1/2}(1,\ldots,1)^T\otimes e_1.
\]
A finite union of (Uniform-bounded-law-norm) gives
\[
 hI_{3N}\le H_N\le HI_{3N},
 \qquad h=180,\quad H=420,
 \tag{Positive-core-norm}
\]
outside probability at most \(12e^{-3N}\).
The tensor expressions are identified with physical-first blocks by the fixed coordinate permutation.

<a id="uniform-rank-one-rectangle-net"></a>
## One deterministic parameter net preserves every required rectangle

Fix any integer \(r\ge0\).
For each deterministic physical deletion set \(T\subset[N]\), \(|T|\le r\), and each deterministic \(\alpha\in[0,H]\), consider
\[
 K_{N,T}(\alpha)
 =(H_N-\alpha v_Nv_N^T)[T^c,T^c].
\]
For this fixed parameter the shift is deterministic, so the [C194v17 rectangle statement](../claims/Yin_C_F0194_v17.md#statement), adopted at [C194v18](../claims/Yin_C_F0194_v18.md#decision-positive-frame-rectangles-reviewed), applies.
Its hypotheses match the original independent Rademacher coordinates, the fixed positive-frame coefficients and an arbitrary deterministic shift.

Write \(n=N-|T|\).
The noise in the actual retained minor is still normalized by \(N^{-1/2}\).
Multiplication of the whole minor by \(\sqrt{N/n}\) puts it in the source theorem's \(n^{-1/2}\) normalization, with the same noise coefficients and a rescaled deterministic shift.
The source has no bound on that shift.
After scaling back, there are fixed \(\delta_0\in(0,1/4]\), \(\kappa,c,C>0\) such that, for every fixed \(\alpha,T\),
\[
 \mathbb P\left\{
 \exists J\subset T^c,\ |J|=\lfloor\delta_0n\rfloor:
 s_{\min}\bigl((H_N-\alpha v_Nv_N^T)[T^c\setminus J,J]\bigr)
       <\frac\kappa{\sqrt N}
 \right\}\le Ce^{-cn}.
 \tag{Fixed-parameter-retained-rectangles}
\]
The constants are uniform over the deterministic shift and hence over \(\alpha\), and the fixed deletion bound only changes the final size threshold.

Choose a deterministic mesh \(\mathcal A_N\subset[0,H]\), including its endpoints, whose spacing is at most \(\kappa/(4\sqrt N)\).
Its cardinality is \(O(\sqrt N)\).
There are \(O_r(N^r)\) permitted deletion sets, so the union of (Fixed-parameter-retained-rectangles) over the mesh and these sets has failure probability at most
\[
 C_r N^{r+1}e^{-cN}\le C_r'e^{-c'N}.
 \tag{Rank-one-net-failure}
\]
The source theorem already includes the union over the physical supports \(J\).

For every disjoint \(I,J\),
\[
 \|[(\alpha-\alpha')v_Nv_N^T][I,J]\|
 \le|\alpha-\alpha'|\,\|v_N[I]\|\,\|v_N[J]\|
 \le|\alpha-\alpha'|.
\]
The variational definition of the least singular value makes it Lipschitz with constant one in operator norm.
Nearest-mesh comparison therefore proves that, on one event with the failure bound (Rank-one-net-failure),
\[
 s_{\min}\bigl((H_N-\alpha v_Nv_N^T)[T^c\setminus J,J]\bigr)
       \ge\frac\kappa{2\sqrt N}
 \tag{All-parameter-retained-rectangles}
\]
simultaneously for every \(\alpha\in[0,H]\), every \(|T|\le r\), and every displayed support \(J\).
The argument first takes a union over deterministic parameters and only then permits a parameter chosen from the observed matrix.
It does not invoke the source theorem directly for an adaptive shift.

The same bound holds when \(1\le|J|\le\lfloor\delta_0n\rfloor\).
Indeed extend \(J\) to a set \(J'\) of the displayed size, restrict the good rectangle's columns to \(J\), and then add the rows in \(J'\setminus J\).
Deleting columns and adding rows cannot reduce the least singular value of this full-column-rank rectangle.

The exceptional probabilities in (Positive-core-norm) and (Rank-one-net-failure) are summable.
Combine their eventual almost-sure conclusions with [C186v4's almost-sure weak law](../claims/Yin_C_F0186_v4.md#statement) for this fixed affine pencil.
Fix one realization of the Rademacher matrices in that probability-one intersection.
It gives a deterministic sequence, still denoted \(H_N\), satisfying all these properties for sufficiently large \(N\).
Because its spectra lie in \([h,H]\), weak convergence also gives
\[
 \frac1{3N}\log\det H_N\longrightarrow v.
 \tag{Positive-core-logarithm}
\]
This fixes a sequence of actual finite coordinate configurations; it changes no probability law in the theorem being investigated.

<a id="exponential-mode-and-exact-loss"></a>
## A single exponential mode and the exact determinant loss

Fix \(\eta>0\), and define
\[
 \varepsilon_N=e^{-3\eta N},\qquad
 q_N=v_N^TH_N^{-1}v_N,\qquad
 \alpha_N=\frac{1-\varepsilon_N}{q_N},\qquad
 M_N=H_N-\alpha_Nv_Nv_N^T.
 \tag{Tuned-positive-rank-one-update}
\]
The core bounds give \(H^{-1}\le q_N\le h^{-1}\), hence \(0\le\alpha_N\le H\).
Consequently (All-parameter-retained-rectangles) applies to the chosen \(\alpha_N\) and to every permitted retained principal minor of \(M_N\).

Put \(u_N=H_N^{-1/2}v_N/\sqrt{q_N}\), which is a unit vector.
The exact congruence is
\[
 M_N=H_N^{1/2}
       [I-(1-\varepsilon_N)u_Nu_N^T]H_N^{1/2}>0.
\]
It gives \(\lambda_{\min}(M_N)\ge h\varepsilon_N\).
Testing its Rayleigh quotient on a multiple of \(H_N^{-1/2}u_N\) gives the opposite bound \(\lambda_{\min}(M_N)\le H\varepsilon_N\).
The rank-one eigenvalue interlacing inequality and \(M_N\le H_N\) show that all other eigenvalues lie in \([h,H]\), while \(\|M_N\|\le H\).
Thus every increasing singular value after the first has a constant lower bound, stronger than the middle-value profile needed by the determinant argument.

Expanding the determinant of the displayed rank-one factor gives the complete identity
\[
 \det M_N=\det H_N(1-\alpha_Nq_N)
          =\det H_N\,\varepsilon_N.
 \tag{Exact-exponential-determinant-ratio}
\]
Therefore
\[
 \frac1{3N}\log\det M_N\longrightarrow v-\eta.
 \tag{Fixed-total-logarithmic-loss}
\]
The empirical spectral distributions of \(M_N\) and \(H_N\) differ by at most \(1/(3N)\) in their distribution functions, so \(M_N\) still has the free weak limit of \(L\).

For any fixed \(0<g<h\), precisely one eigenvalue of \(M_N\) lies below \(g\) eventually, and
\[
 D_N(g)=\frac1{3N}\sum_{\lambda_a(M_N)<g}
                   \log\frac g{\lambda_a(M_N)}
       =\frac1{3N}\log\frac g{\lambda_{\min}(M_N)}
       \longrightarrow\eta.
\]
This is the actual total-loss quantity from C194v20, with its full normalization.
An \(o(N)\) count of exceptional modes, even a single mode with all the rectangle bounds, does not determine its size.

<a id="one-fixed-bounded-law-realization"></a>
## One fixed bounded original law realizes every finite configuration

Increase the fixed starting dimension so that \(N\ge H^2\), and write \(\beta_N=\alpha_N/\sqrt N\in[0,1]\).
Since \(A_1=E_{11}\), the perturbation changes only the first original input:
\[
 \widetilde B_{1,N}=B_{1,N}-\alpha_Nw_Nw_N^T,
 \qquad w_N=N^{-1/2}(1,\ldots,1)^T.
\]
Its required raw off-diagonal coordinates are \(1-\beta_N\) or \(-1-\beta_N\), and its raw diagonal coordinates are \(-\beta_N\).
All other inputs retain their Rademacher off-diagonal coordinates and zero diagonals.
The collection of required first-input off-diagonal values over all dimensions is countable and lies in \([-2,2]\).

Enumerate its distinct symmetric orbits after adjoining the negatives, and assign strictly positive symmetric masses with total mass \(p<1/16\).
Any zero orbit is assigned its mass at zero.
Their total second moment \(w\) is at most \(4p<1/4\).
Place the remaining mass symmetrically at \(\pm b\), where
\[
 b^2=\frac{1-w}{1-p}<\frac{16}{15}.
\]
This defines a single centered variance-one off-diagonal law \(\xi_1\), supported in \([-2,2]\), containing every required coordinate with positive mass.
The construction is valid if a completion atom coincides with an existing atom; their masses are simply added.

Assign positive symmetric masses to the distinct values in \(\{\pm\beta_N:N\ge N_0\}\), with total mass less than one, and put the remainder at zero.
This gives a single centered diagonal law \(\zeta_1\), supported in \([-1,1]\) and having finite second moment, containing every required diagonal value.
Use the Rademacher off-diagonal and zero diagonal laws for the other five inputs.
All laws are fixed after the sequence is selected and do not vary with dimension.
Sampling every upper coordinate and every input independently under those laws makes each finite event specifying the matrix \(M_N\) have strictly positive probability.
Mirroring the lower entries gives exactly the original real Wigner model, with its unchanged \(N^{-1/2}\) normalization.
The construction does not assert positive probability for the entire infinite prescribed sequence under any coupling.

The new laws have variance one off the diagonal and the same fixed coefficient tuple, so their free limit is the same \(L\).
Their own rectangle theorem may supply different sufficient constants \(\delta_1,a_1\).
Choose smaller sufficient constants
\[
 \delta_*\le\min(\delta_0,\delta_1),\qquad
 a_*\le\min(\kappa/2,a_1).
\]
The support-padding argument above both preserves the source probability theorem at the smaller support size and proves that the constructed matrices satisfy these rectangle inequalities, through the prescribed deletions.
This is a legitimate choice of sufficient good-event parameters, not a claim about any unspecified optimal constants or every possible parameter choice for the source theorem.

<a id="rarity-and-fixed-parameter-boundary"></a>
## The configurations are rare, and parameter averaging cannot repair the fixed point

The uniform norm derivation (Uniform-bounded-law-norm) applies to the newly constructed laws, since their actual support and centering satisfy exactly its hypotheses.
Thus the random original pencil under these laws lies between \(180I\) and \(420I\) except with probability at most \(12e^{-3N}\).
The prescribed \(M_N\) has an eigenvalue below \(180\) for all sufficiently large \(N\).
Accordingly its positive-probability realization event has probability at most \(12e^{-3N}\).
No lower bound bounded away from zero, failure probability along all dimensions, or adverse arbitrary-coupling conclusion follows from the construction.
In this deliberately deep positive gap the same norm argument directly controls the typical original model.

There is also a precise limitation on a parameter-averaging shortcut.
For every fixed real \(t\) with \(0<|t|<h/2\), all but one eigenvalues of \(M_N+tI\) have absolute value at least \(h-|t|>h/2\).
The remaining eigenvalue is \(\lambda_{\min}(M_N)+t\), whose absolute value is at least \(|t|/2\) eventually.
The full shifted spectra therefore have a common absolute gap depending on this fixed nonzero \(t\), as do the spectra of \(H_N+tI\) and \(L+t\).

For \(t>0\), \(x\mapsto\log|x+t|\) is continuous and bounded on the common unshifted spectral interval \([0,H]\).
For \(t<0\), the exceptional eigenvalue eventually lies in \([0,|t|/2]\) and all other eigenvalues lie in \([h,H]\).
Choose a fixed bounded continuous extension that agrees with \(\log|x+t|\) on those two disjoint intervals and interpolates across the unused interval between them.
The free and core spectra lie in \([h,H]\), so the same extension agrees with their logarithmic integrand.
Rank-one weak spectral stability and (Positive-core-logarithm)'s weak-limit input then give
\[
 \frac1{3N}\log|\det(M_N+tI)|
       \longrightarrow\log\Delta_{\tau_3}(L+t)
       \qquad(0<|t|<h/2).
\]
At the fixed point \(t=0\), (Fixed-total-logarithmic-loss) still loses \(\eta\).
Thus a statement for almost every parameter, or an average over a small parameter interval, does not by itself return the missing fixed-parameter conclusion even for these bounded, gapped, rectangle-good deterministic configurations.
No random spectral parameter or random dimension is substituted for the original F13 quantifiers.

<a id="total-loss-route-consequence"></a>
## Consequence for the original probability problem

The rejected implication is a deterministic deduction of vanishing total negative-logarithmic loss from the free gap, weak convergence, bounded parent norm, a small exceptional-mode count, the existing intermediate profile and small-support rectangle geometry.
The construction retains all of those controls and computes a positive limiting loss exactly.
It leaves actual original-law probabilities essential: a successful argument must quantify how often the complete resonance is approached, rather than infer a total-loss bound from those controls alone.

The [C194v20 nuclear-approximation premise](../claims/Yin_C_F0194_v20.md#inverse-trace-norm-approximation) is not established by the surviving rectangle conditions.
For the present parent the inverse head associated with its one small eigenvalue has normalized nuclear norm at least \(e^{3\eta N}/(HN)\), which diverges.
That observation only locates the failed sufficient premise on these rare configurations; it does not make that premise necessary for F13.
The [C190v1 marginal criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion) still requires vanishing lower-deviation probability along suitable deterministic dimensions for the arbitrary-coupling limsup.
No such new probability estimate, independent review, general-coefficient extension or Task completion is supplied here.
