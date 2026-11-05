---
author: Yin
---

# Phase-line Hermitian Wigner invertibility under complex nonsymmetric shifts

This version extends the [reviewed real-input result](Yin_C_F0194_v5.md#decision-nonsymmetric-floor-reviewed) to the stated phase-line model.
Its [independent whole-proof review](../audits/reviews/Yin_R_F0200_v6.md#finding) covers the complete new argument and every subsidiary assertion at its precise scope.
The earlier physical versions retain their mathematics and actual review scopes.
This is a project deduction without a novelty or priority claim.
The real-input final probability theorem is not used as a probability theorem for complex entries.

<a id="statement"></a>
## Exact main statement and subsidiary assertions

Fix a real law eta with E eta=0 and E eta^2=1, a real diagonal law zeta with E|zeta|^2 finite, and a fixed complex c with |c|=1 and Re c nonzero.
For every N, let W_N be Hermitian with independent strict upper entries c eta_jk/sqrt(N), independent diagonal entries zeta_j/sqrt(N), and conjugate lower entries, with the diagonal and upper families independent.
For every gamma,B>0 there are fixed A,C_B,C,N0, depending only on c, the two laws, gamma and B, such that
\[
 \sup_{\max_{jk}|F_{jk}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}\,N^{-1/18},
 \qquad N\ge N0.
 \tag{Phase-floor}
\]
The supremum is over arbitrary deterministic complex matrices, with no symmetry condition, and F may vary with N.
For an independent random F_N and Gamma_N={max|F_N,jk|<=N^gamma}, the same right side bounds P(s_min(W_N+F_N)<=N^(-A), Gamma_N); add P(Gamma_N^c) for the unguarded probability.
Only independence within each size is required; all sizes may have arbitrary coupling.
No density, non-atomicity or moment above two is assumed.
The displayed main error tends to zero and is not claimed summable.
The constants may depend on the fixed phase c, and no uniformity as Re c tends to zero is asserted.

This statement includes the following auxiliary assertions at the full hypotheses, dimensions, thresholds and constants stated in their named sections.

- The [fixed-cutoff complex distance estimate](#complex-distance), for any fixed centered variance-one complex law and arbitrary coordinatewise conjugate orientations, and the real-block distance estimate in the [majority-orientation lemma](#majority-orientation-lemma).
- The [majority-orientation singular-direction and row bound](#majority-orientation-lemma) for a complex law with positive real-part variance, and the [central-strip actual-minor exclusion](#central-strip-diagonal-exclusion) for that broader complex law, m in [N/2,N], r_N log(N)=o(N), and the fine threshold chosen after the shift, norm and symmetric-floor scales.
- The [cyclic unitary gauge](#phase-line-gauge), [weighted coefficient and matching estimates](#phase-line-coefficient-control), and [simultaneous low-weighted-matching minor-ratio implication](#phase-line-low-matching), for the phase-line model with Re c nonzero and with the original normalization sqrt(N).
- The [finite-phase progression count](#phase-envelope-count) and [universal omitted-row and near-kernel anti-concentration](#phase-envelope-kernel-interface), for every unit-modulus c, independent truncated real amplitudes and any deterministic edge-phase pattern in {c,bar c} with mirrored lower phases; these are uniform in prescribed finitely many omitted rows and deterministic complex offsets in the stated polynomial bound.
- The [arbitrary-power corank-at-least-two tail](#phase-line-rank-tail), [raw and normalized second-smallest floors](#phase-line-second-floor), and [restricted raw isolated-minor probability estimate](#phase-line-isolated-minor), for every unit-modulus c, including the purely imaginary phase.
- The [odd-size counterexample](#odd-skew-obstruction), showing that the main all-size floor cannot include every purely imaginary phase-line law.

The main conclusion is restricted to phase-line laws with Re c nonzero.
The broader auxiliary assertions do not imply a least-value floor for every phase, nor a theorem for an arbitrary complex entry law.
No almost-sure full-sequence least-value floor, Brown-measure conclusion or completion of the general matrix-pencil or scalar-polynomial determinant Tasks is asserted.

<a id="argument"></a>
## Complete proof and exact input interfaces

The [symmetric-shift theorem](Yin_C_F0188_v2.md#statement) is used only on genuinely symmetric parts, whose real random off-diagonal marginal has positive fixed variance.
It is never applied conditionally on the correlated imaginary entries.
The [complex projection proof](Yin_C_F0187_v2.md#argument) supplies its accepted bounded-product convex concentration inequality and the elementary negative-second-moment/Gram-inverse calculation.
The fixed-cutoff complex and real-block distance consequences needed here are proved below, rather than inferred from an insufficient moving-cutoff exponent.

The [structured class](Yin_C_F0194_v1.md#counting-class), [full profile proof](Yin_C_F0194_v1.md#structured-vector-counting), and [linear inverse rounding interface](Yin_C_F0194_v1.md#inverse-rounding) provide the precise rational-progression setup and accepted inverse-theorem output being adapted.
The new finite-phase envelope and every altered entropy/probability step are supplied below.
The external linear input is only [Ngu12a-U001](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001), arXiv:1105.5733v1 Condition 1 and Theorem 1.3, PDF pp. 2--3, with real scalar amplitudes and dimension-two coefficient vectors.
Its original proof is accepted at the inspection depth stated in its source notes, not newly audited here.
The deterministic [isolated-row rank-one product calculation](Yin_C_F0194_v1.md#isolated-row-reduction) is reused with a newly supplied phase-line near-kernel input; the old real-input isolated probability theorem is not invoked.

The deterministic measurable kernel choice and two-form rank increment come from the [fixed bordered-rank calculation](Yin_C_F0194_v2.md#border-rank).
The phase-line probability guard is proved here, rather than imported from the old real-law corank theorem.
The [row-adjugate inequality](Yin_C_F0194_v3.md#row-adjugate), [rectangular argument](Yin_C_F0194_v3.md#rectangles), and [pointwise spread and average](Yin_C_F0194_v3.md#spread-and-average) are reused after the complex fixed-cutoff distance input has been checked below.
The [complete normalized real-border matching proof](Yin_C_F0194_v3.md#two-copy-matching) applies after the exact unitary gauge makes the exposed border real.
Its source input is [MNV16-U001](../audits/literature/MNV16/Yin_U001.md#mnv16-u001), Definition 1.5 and Theorem 1.6 of the 2016 Theory of Computing edition, PDF p. 3, only at its real-coefficient fair-sign, degree-two, arbitrary length-one-interval scope.
That source's original proof is accepted without a new full-proof audit.
No quadratic inverse theorem for complex scalar randomness is assumed.

<a id="odd-skew-obstruction"></a>
## An admissible complex law defeats the unchanged all-size floor

Let epsilon be a fair sign, set xi=i epsilon, take the real diagonal law zeta=0, and use the deterministic shift F_N=0.
These are fixed laws with E xi=0, E|xi|^2=1, and finite diagonal second moment, and the Hermitian convention puts xi/sqrt(N) above the diagonal and its conjugate below.
Consequently every realization satisfies
\[
 W_N^*=W_N,\qquad W_N^T=-W_N.
\]
For every odd N,
\[
 \det W_N=\det W_N^T=\det(-W_N)=(-1)^N\det W_N=-\det W_N,
\]
so det W_N=0 and s_min(W_N)=0 surely.
For every fixed A>0 the probability of s_min(W_N)<=N^(-A) is therefore one along all odd sizes.
In particular the main least-value conclusion cannot be extended unchanged to all admissible complex Hermitian laws, even for zero shift and a bounded two-point law.
No counting improvement can prove that false all-size conclusion.

This is not a counterexample to an original determinant-limsup Task, to Brown-measure convergence, or to a theorem restricted to even sizes or a suitable deterministic subsequence.
A single forced zero has empirical mass 1/N; this determinant calculation supplies neither a positive limiting mass bound nor a positive-probability failure of weak convergence.
A limsup can be obtained on a subsequence.
The calculation gives no least-value bound on the remaining even sizes.
In particular even-size control and direct determinant-limsup methods remain separate research possibilities.

<a id="complex-distance"></a>
## The fixed-cutoff distance input does survive

Fix a centered complex law xi with E|xi|^2=1 and fix rho in (0,1].
Let x in C^p have independent coordinates, each with the law of xi or its conjugate, with an arbitrary deterministic orientation at each coordinate.
There are c,C,p_0>0, depending only on the law and rho, such that, for every p>=p_0, every deterministic complex linear subspace V of complex codimension at least rho p, and every deterministic f in C^p,
\[
 \mathbb P\{\operatorname{dist}(x+f,V)\le c\sqrt p\}
       \le C\exp(-cp).
 \tag{Complex-fixed-distance}
\]
In particular the components of one complex entry need not be independent and its real covariance need not be nonsingular.

Here is the complete fixed-cutoff adaptation of the [complex projection proof](Yin_C_F0187_v2.md#argument), using exactly its bounded-product convex concentration input.
Choose a fixed sufficiently large R so that
\[
 q_R=\mathbb P\{|\xi|>R\}<\rho/16,
 \qquad v_R=\operatorname{Var}(\xi\mid |\xi|\le R)\ge1/2.
\]
Such an R exists by finite second moment and nondegeneracy.
If J={j:|x_j|<=R}, the binomial Chernoff estimate gives
\[
 \mathbb P\{|J^c|>\rho p/4\}\le\exp(-c_\rho p).
\]
Conditional on J, the retained coordinates are independent with the corresponding truncated law or its conjugate.
Their conditional means are the appropriate mu_R or its conjugate, and their centered complex variances all equal v_R.
Project V onto J and enlarge its image by the single vector f_J+mu_J.
The resulting complex linear space V_J' has codimension at least rho p-|J^c|-1>=rho p/2 eventually on the displayed good event.
For centered retained coordinates y=x_J-mu_J,
\[
 \operatorname{dist}(x+f,V)\ge\operatorname{dist}(y,V_J')=\|Py\|,
 \qquad \mathbb E\|Py\|^2=v_R\operatorname{Tr}P\ge\rho p/4,
\]
where P is the orthogonal complex projection onto (V_J')^perp.
The expectation uses E bar(y_a)y_b=v_R 1_{a=b}; no condition on E xi^2 is inserted.
The function ||Py|| is convex and 1-Lipschitz in the product of independent real two-dimensional coordinate blocks, each of support diameter at most 2R.
The fixed input concentration inequality gives variance O(R^2), mean-minus-median O(R), and hence median at least c_rho sqrt(p) for large p.
Its lower tail below half that median is at most C exp(-c_rho p/R^2).
Combining with the discarded-coordinate estimate proves (Complex-fixed-distance), uniformly in the subspace, shift and orientations.
The external bounded-product concentration theorem is reused at the accepted inspection depth of C_F0187_v2 rather than newly audited here.

The cross-rectangles of a Hermitian Wigner matrix have independent columns after conditioning on the other columns, and each column has independent coordinates with these xi/conjugate-xi orientations.
Therefore the rectangular-distance and support-union portions of [C_F0194_v3](Yin_C_F0194_v3.md#spread-and-average) retain their exponential input for complex laws.
The deterministic row-adjugate inequality in that argument is unaffected by the entry law.
This identifies a surviving many-index mechanism before its scalar matching and actual-minor inputs; it is not a complex least-value theorem.

<a id="positive-real-variance"></a>
## A positive real-part variance preserves only the symmetric-part marginal

Write xi=a+ib and suppose sigma_R^2=E a^2>0.
Since xi is centered, a is a centered real law, and
\[
 \operatorname{sym}(W_N+F_N)
 =W_N^{(a)}+\operatorname{sym}F_N,
\]
where W_N^(a) is the real symmetric matrix with upper entries a/sqrt(N) and the original real diagonal.
After division by sigma_R, its off-diagonal law has variance one.
The [real symmetric-shift theorem](Yin_C_F0188_v2.md#statement) consequently supplies its polynomial floor, with adjusted law-dependent constants and exponents, for every deterministic polynomially bounded F_N.
This is an unconditional marginal application, and also applies to each actual internal symmetric part before conditioning on its correlated imaginary entries.
It requires no independence between a and b.
If sigma_R=0, then a=0 almost surely, and a zero diagonal makes this random symmetric part identically zero, as in the obstruction above.

Conditioning on all imaginary entries does not justify applying the real theorem to the remaining real entries.
For xi=(1+i)epsilon/sqrt(2), b determines a exactly, so that conditional real-entry law is deterministic despite sigma_R>0.
The diagonal law and the independence of a separate shift do not repair that loss of conditional randomness.

<a id="complex-internal-row"></a>
## The exact internal-row map has conjugate variables

Place an internal index j first and write an actual shifted Hermitian minor as
\[
 D=\begin{pmatrix}a_0&b_0\\c_0&B\end{pmatrix},
 \quad b_0=\bar z^T/\sqrt N+f^T,
 \quad c_0=z/\sqrt N+g.
\]
Here z is the independent internal column with deterministic xi/conjugate-xi orientations; it is independent of B, and f,g are fixed and may differ.
Let A=adj D, Q=sym A, and suppose det B is nonzero.
Polynomial cofactor expansion gives Q_jj=det B and
\[
 Q_{-j,j}=-\frac12\left[(\operatorname{adj}B)c_0
                    +(\operatorname{adj}B)^Tb_0^T\right].
\]
These polynomial identities hold also for singular B; division below is used only when det B is nonzero.
Substitute adj B=(det B)B^(-1) and put R=B^(-1) to obtain
\[
 -\frac{Q_{-j,j}}{\det B}
   =\frac{Rz+R^T\bar z}{2\sqrt N}
      +\frac{Rg+R^Tf}{2}.
 \tag{Complex-internal-row}
\]
Writing z=x+iy and T=(R-R^T)/2, S=(R+R^T)/2, the random map is
\[
 \Phi(z)=\frac{Rz+R^T\bar z}{2}=Sx+iTy.
\]
For real entries this becomes Sx, whose coefficient floor follows from S=B^(-T)(sym B)B^(-1).
For complex entries the second term can cancel the first on the actual support of z.

<a id="majority-orientation-lemma"></a>
## A majority orientation restores a positive number of directions

There is a quantitative partial repair that retains dependent real and imaginary parts.
Let xi=a+ib be centered with finite second moment and alpha=sqrt(E a^2)>0.
Let R be an arbitrary complex m-by-m matrix, write S=sym R and T=skew R, and assume s_min(S)>=kappa>0.
Let the independent coordinates of z have the law of xi on one orientation group and conjugate xi on the other.
Suppose the majority group has p coordinates and the minority group q, with p+q=m and p>q.
Delete k_+ coordinates from the majority group, retain the remaining index set U of size t=p-k_+, and condition on every z-coordinate outside U.
Set
\[
 d_0=p-q-2k_+>0,\qquad r=\lceil d_0/2\rceil.
\]
Then, as a real-linear function of independent whitened coordinate blocks, the retained output Phi(z)_U has at least r singular values at least alpha kappa/sqrt(2).
In particular, for each fixed rho>0, if r>=rho t, there are c,C,t_0>0, depending only on xi and rho, such that
\[
 \sup_v\mathbb P\left\{
 \left\|\frac{\Phi(z)_U}{\sqrt N}+v\right\|
        \le c\alpha\kappa\sqrt{t/N}
        \;\middle|\;z_{U^c}\right\}
       \le C\exp(-ct),\qquad t\ge t_0.
 \tag{Majority-row}
\]
The constants are uniform in R,kappa,N, the conditioned coordinates and the affine center v.
The norm is the usual complex Euclidean norm, identified with its real Euclidean norm.
No upper bound for R and no conditional independence between a and b is required.

Here is the full argument.
The complement U^c has q+k_+ indices.
The kernel of S_{U^c,U} has dimension at least t-(q+k_+)=d_0.
On this kernel ||S_UU x||=||S_{[m],U}x||>=kappa||x||, by extension by zero.
The complex singular-value min-max principle gives at least d_0 singular values of S_UU at least kappa.

Whiten the fixed real two-dimensional law by writing
\[
 a=\alpha\eta_1,\qquad
 b=\beta\eta_1+\gamma\eta_2,
 \quad
 \beta=\frac{\mathbb E ab}{\alpha},\qquad
 \gamma^2=\mathbb E b^2-\beta^2.
\]
If gamma>0, define eta_1=a/alpha and eta_2=(b-beta eta_1)/gamma.
The real block (eta_1,eta_2) is centered with covariance I_2, although its components may be dependent.
If gamma=0, the displayed relation holds almost surely with the single centered variance-one variable eta_1 and no eta_2 coordinate.
Both cases have finite second moment and independent blocks across indices.
On U all orientations are the same sigma in {1,-1}, so its random output has the form
\[
 K\eta_1+i\sigma\gamma T_{UU}\eta_2,
 \qquad K=\alpha S_{UU}+i\sigma\beta T_{UU}.
\]
In particular K+K^T=2 alpha S_UU.
The singular-value sum inequality with the two indices both equal to r gives
\[
 2\alpha\kappa
 \le s_{2r-1}(K+K^T)
 \le s_r(K)+s_r(K^T)=2s_r(K),
\]
since 2r-1<=d_0.
Thus s_r(K)>=alpha kappa.

The real-input matrix C_1=[Re K; Im K], of size 2t-by-t, satisfies
\[
 s_r(C_1)\ge s_r(K)/\sqrt2.
\]
Indeed, pack the best real rank-(r-1) approximation to C_1 into a complex t-by-t matrix K_0.
Its complex rank is at most r-1, because the real right factors remain valid complex right factors.
If the real approximation error has operator norm e, then ||(K-K_0)(x+iy)||<=e(||x||+||y||)<=sqrt(2)e||x+iy|| for real x,y.
The complex rank approximation principle gives s_r(K)<=sqrt(2)e.
Adding the eta_2 columns to the real coefficient matrix can only increase its first r singular values, by the positive-semidefinite comparison of its left Gram matrix.
This proves the asserted real-linear singular-value count.

It remains to justify exponential concentration at its good directions.
For independent copies of a fixed centered real block eta of dimension d in {1,2}, with covariance I_d and finite second moment, every fixed rho>0 admits constants c,C such that
\[
 \mathbb P\{\operatorname{dist}((\eta_j)_{j=1}^t,H+u)
                  \le c\sqrt t\}\le C\exp(-ct)
 \tag{Real-block-distance}
\]
uniformly over real affine subspaces of real codimension at least rho t.
Choose a fixed sufficiently large cutoff L so that the covariance of eta conditioned on ||eta||<=L is at least I_d/2 and its bad-block probability is less than rho/(16d).
The probability of more than rho t/(4d) bad blocks is at most exp(-ct).
Projecting the affine space onto the remaining blocks loses at most d times this number in codimension.
Conditional retained blocks stay independent, have support diameter at most 2L, and have conditional covariance at least I_d/2.
For the distance function its conditional second moment is at least half the retained codimension, including any center or conditional mean.
The bounded-product convex concentration inequality used in C_F0187_v2 gives variance O(L^2), mean-minus-median O(L), and the lower tail exp(-ct) below c sqrt(t).
This proves (Real-block-distance) without assuming independent components inside a block.

Finally take r good left singular directions of the real coefficient map for Phi(z)_U and divide the corresponding coordinates by their singular values.
The event that its output plus v has norm at most epsilon implies distance at most sqrt(2)epsilon/(alpha kappa) to a fixed real affine subspace of the block input of codimension r.
Apply (Real-block-distance) with epsilon=c alpha kappa sqrt(t), and divide the whole map by sqrt(N).
This proves (Majority-row).
The strict positive imbalance d_0 is part of this assertion; no corresponding positive-direction bound is asserted when the two groups are balanced.

<a id="central-strip-diagonal-exclusion"></a>
## A genuine complex actual-minor consequence away from a central strip

The majority lemma proves an analogue of uncovered-diagonal exclusion for the unweighted Q=sym adj D graph, with a fixed central strip excluded.
This is a subsidiary result, not the complex main-floor claim.
Fix eta in (0,1/8), B_0>0, K>=0 and gamma>0, and let D be an actual m-by-m shifted complex Hermitian Wigner minor normalized by sqrt(N), with m in [N/2,N], deterministic shift max|F_ab|<=N^gamma, and a fixed centered law xi with E|xi|^2=1 and E(Re xi)^2>0.
Its independent real diagonal law has finite second moment.
Retain the inherited increasing order of its m coordinates and define the deterministic central strip
\[
 Z_\eta=\{j\in[m]:|2j-m-1|<\eta m\}.
\]
Its cardinality is at most eta m+2.
There is a fixed L, depending only on the laws,gamma,B_0, such that for every fixed J>=0 and H>J+L+2K+1, and every deterministic integer r_N with r_N log(N)=o(N), the probability is at most
\[
 C_{B_0}N^{-B_0}+C\exp(-c_\eta N)
 \tag{Complex-diagonal-error}
\]
that there exist I subset of [m], |I|<2r_N, and j outside I union Z_eta for which
\[
 \begin{split}
 &A=\operatorname{adj}D\ne0,\quad Q=\operatorname{sym}A,
       \quad\|D\|\le N^K,\\
 &|Q_{ab}|<N^{-H}\|A\|_F
       \quad(a\ne b,\ a,b\notin I),\\
 &|Q_{jj}|\ge N^{-J}\|A\|_F.
 \end{split}
 \tag{Complex-uncovered-diagonal}
\]
Constants and the sufficiently large size are uniform over the displayed m and shifts; the size may depend on J,H,K,eta and the sequence r_N.

To prove this, apply the positive-real-variance symmetric-part marginal above to all B_j=D with row and column j removed.
The raw matrix sqrt(N) sym B_j, divided by alpha=sqrt(E(Re xi)^2), has a fixed real variance-one off-diagonal law and a deterministic complex symmetric polynomial shift.
Write d=m-1, so N/3<=d<=N for large N.
After division by alpha, the raw symmetric shift has entries bounded by a fixed multiple of N^(gamma+1/2), hence by d^(gamma+2) eventually, and the real diagonal law is zeta/alpha.
Apply C_F0188_v2 at exponent gamma+2 and failure exponent B_0+4.
For some fixed a_s its normalized floor is alpha d^(-a_s)/sqrt(N).
Choose L>a_s+1, absorbing the fixed alpha; this floor is at least N^(-L) for all sufficiently large N.
A union over at most N choices of j bounds the symmetric-part exception by C_B0 N^(-B0-3), in particular by C_B0 N^(-B0-2).
This applies to the unconditional marginal of each B_j and imposes no conditional hypothesis on its imaginary part.

Fix I,j and condition on B=B_j in this guard.
On the displayed large-diagonal event det B=Q_jj is nonzero.
Its inverse R satisfies s_min(sym R)>=N^(-L-2K)=kappa by the same factorization as the real proof.
The two orientation groups in the exposed internal column have sizes j-1 and m-j, so their imbalance is |2j-m-1|>=eta m.
Retain the majority group outside I and condition on all other row coordinates.
For sufficiently large N the majority lemma has d_0>=eta m-4r_N>=eta m/2, t>=m/3, and r>=rho_eta t for a fixed rho_eta>0.
The off-diagonal bounds and |det B|>=N^(-J)||A||_F force
\[
 \left\|Q_{U,j}/\det B\right\|
              \le\sqrt t\,N^{J-H}.
\]
By (Complex-internal-row) this is the event in (Majority-row), at a radius smaller than c alpha kappa sqrt(t/N) eventually, because H>J+L+2K+1.
Its conditional probability is at most C exp(-c_eta N), uniformly in the coefficients, affine center and conditioned coordinates.
Dropping the norm, cover and large-diagonal conditions after making this implication is legitimate: they were used only to force membership in this fixed-center row event.
The number of pairs I,j is at most N^(2r_N+2)=exp(o(N)); union them and add the common symmetric-floor exception.
This proves (Complex-diagonal-error).

Accordingly, if the unweighted graph has matching less than r_N, take its maximal-matching cover I and enlarge it by Z_eta.
Except with the displayed error, Q is the sum of a matrix supported on the rows or columns of I union Z_eta and an error of Frobenius norm at most
\[
 \bigl(\sqrt m\,N^{-J}+mN^{-H}\bigr)\|A\|_F.
\]
The supported matrix has rank at most 2|I union Z_eta|<4r_N+2 eta m+4<m eventually.
On the additional guard s_min(sym D)>=N^(-L0), the same exact identity DQD^T=(det D)sym D and singular-value rank approximation give
\[
 \frac{|\det D|}{\|A\|_F}
 \le N^{2K+L0}\bigl(\sqrt m\,N^{-J}+mN^{-H}\bigr).
\]
That additional guard again follows from the positive-real-variance marginal, outside arbitrary polynomial failure probabilities.
The estimate can be made smaller than any prescribed inverse polynomial by choosing J,H in that order.
This is a complete low-unweighted-matching actual-minor refinement for positive-real-variance complex laws; the high-matching event needed for the actual complex border is different, as explained next.

<a id="phase-line-gauge"></a>
## A cyclic unitary gauge identifies the correct phase-line graph

For this algebraic section impose the fixed law xi=c eta, where |c|=1 and eta is a fixed centered variance-one real law.
The gauge identities hold for every such phase, including Re c=0; the subsequent symmetric-part floors and low-matching probability implication require Re c nonzero.
The diagonal law zeta is fixed and real with finite second moment and is independent of the strict upper family.
Let M_N=W_N+F_N with the usual Hermitian convention and a deterministic arbitrary complex shift max|F_ab|<=N^gamma.
Fix an omitted index i and put D_i=M_N[[N] minus {i}], A_i=adj D_i, using the inherited increasing order on its coordinates.
The raw random lower column at i equals Z_i x, where x has independent coordinates of law eta and
\[
 (Z_i)_{jj}=\begin{cases}c,&j<i,\\\bar c,&j>i.\end{cases}
\]
Let P_i be the real permutation matrix whose columns list the remaining indices in the cyclic order
\[
 i+1,\ldots,N,1,\ldots,i-1.
\]
Define
\[
 U_i=Z_iP_i,\quad
 \widehat D_i=U_i^*D_iU_i,\quad
 \widehat A_i=U_i^*A_iU_i=\operatorname{adj}\widehat D_i,
 \qquad
 Q_i^{\rm wt}=\operatorname{sym}(Z_i^*A_iZ_i),
 \quad \widehat Q_i=P_i^TQ_i^{\rm wt}P_i.
 \tag{Phase-gauge}
\]
The adjugate equality follows first for invertible D_i and then by polynomial continuity, so it has no rank hypothesis.
Since P_i is real, one has widehat Q_i=sym widehat A_i.

Here the cyclic order is essential.
Before permutation, an upper random entry of Z_i^*D_iZ_i has phase c when both endpoints lie on the same side of i, and phase bar c when they straddle i.
For straddling endpoints u<i<v the latter assertion is the calculation bar c times c times bar c=bar c.
In the cyclic order the straddling entry moves below the diagonal, whose conjugate has phase c.
All other upper entries retain phase c.
Consequently widehat D_i is exactly a standard phase-line Hermitian Wigner matrix of size N-1, still normalized by sqrt(N), plus the deterministic shift U_i^*F_iU_i.
Its independent real raw amplitudes and real diagonal entries retain their original laws, and their independence is unchanged.
There is no required invariance of the eta law under multiplication by minus one.

The shift transformation is only a permutation and multiplication of individual entries by unit-modulus constants, so its entry guard remains N^gamma.
All singular values, the operator norm and the adjugate Frobenius norm are preserved, and
\[
 \det\widehat D_i=\det D_i,
 \quad\|\widehat A_i\|_F=\|A_i\|_F,
 \quad\frac{|\det\widehat D_i|}{\|\widehat A_i\|_F}
          =\frac{|\det D_i|}{\|A_i\|_F}\quad(A_i\ne0).
 \tag{Gauge-norms}
\]
These are exact identities rather than polynomial comparisons.

Apply the same unitary similarity diag(1,U_i) to the full bordered matrix after placing i first.
Its random off-diagonal border becomes x'=P_i^Tx, which is an iid real eta vector independent of widehat D_i:
\[
 \widehat M_i=
 \begin{pmatrix}
 a_i&(x'/\sqrt N+\widehat f_i)^T\\
 x'/\sqrt N+\widehat g_i&\widehat D_i
 \end{pmatrix},
 \qquad \det\widehat M_i=\det M_N.
 \tag{Real-border-gauge}
\]
The two shift vectors are arbitrary deterministic complex vectors, and the exposed diagonal a_i may be conditioned on independently.
Thus the actual border uses the weighted graph from (Phase-gauge), with quadratic part -(x')^T widehat Q_i x'/N.
No random-coefficient replacement or conditional independence between correlated real and imaginary parts is being assumed in this phase-line construction.

<a id="phase-line-coefficient-control"></a>
## The weighted coefficient norm and minor ratio have no gauge loss

For the coefficient-floor and low-matching estimates assume Re c is nonzero.
Put widehat S_i=sym widehat D_i.
Its random off-diagonal part has the fixed real law (Re c)eta/sqrt(N), so the [positive-real-variance marginal](#positive-real-variance) gives its polynomial floor outside arbitrary polynomial failure probabilities, uniformly over the displayed shifts.
The same holds simultaneously for its internal symmetric parts, by the internal union already used above.
The constants may deteriorate as Re c tends to zero; c is fixed throughout.

For every complex matrix D the polynomial adjugate identities imply
\[
 D^T\operatorname{sym}(\operatorname{adj}D)
       =(\operatorname{sym}D)\operatorname{adj}D,
 \qquad
 D\operatorname{sym}(\operatorname{adj}D)D^T
       =(\det D)\operatorname{sym}D.
\]
Writing A=adj D, the first follows from D^T A^T=(AD)^T=(det D)I and DA=(det D)I.
For the second use DAD^T=(det D)D^T and DA^TD^T=D(DA)^T=(det D)D.
Apply them to widehat D_i.
On the guard s_min(widehat S_i)>=N^(-L0) and ||D_i||<=N^K, the first identity gives
\[
 \|Q_i^{\rm wt}\|_F=\|\widehat Q_i\|_F
           \ge N^{-L0-K}\|A_i\|_F.
 \tag{Weighted-noncancellation}
\]
Indeed widehat A_i=widehat S_i^(-1) widehat D_i^T widehat Q_i.
Thus the real quadratic coefficient norm cannot vanish relative to the actual adjugate norm on this symmetric-part guard.
No lower bound for s_min(D_i) is used in this assertion.

For h>0 define the correct graph by edges j!=k with
\[
 |(Q_i^{\rm wt})_{jk}|\ge h\|A_i\|_F.
 \tag{Weighted-graph}
\]
Declare the high-matching event H_i^(wt)(h,r) to require A_i nonzero and a matching of at least r edges in this graph.
The permutation P_i does not change its matching size.
By (Real-border-gauge), the [exact real-border two-copy proof](Yin_C_F0194_v3.md#two-copy-matching) applies with the real law eta and the actual adjugate widehat A_i.
For some fixed c_*,C>0 depending only on eta, every r>=2 gives
\[
 \mathbb P\left\{
   |\det M_N|/\|A_i\|_F\le c_*h/N
       \;\middle|\;D_i,a_i\right\}
 \le C\left[e^{-c_*r}+\sqrt{\log(2+r)}\,r^{-1/9}\right]
 \tag{Weighted-matching-row}
\]
on H_i^(wt)(h,r).
This uses the existing complete two-copy proof, including its common real-or-imaginary projection, independent endpoint survival and MNV16 degree-two theorem.
The quadratic coefficient is 2(widehat Q_i)_jk/N before its real two-copy endpoint factors, so the radius is h||A_i||_F/N.
There is neither an extra adjugate norm loss nor a missing normalization factor.
The conditional center and lower-degree coefficients remain arbitrary.

<a id="phase-line-low-matching"></a>
## Low weighted matching forces an arbitrarily small actual-minor ratio

Fix gamma>0, K>=0, B_0>0 and a target exponent T_0>0.
Let r_N>=2 be deterministic integers with r_N log(N)=o(N).
There is an exponent H>0, selected after these data and the fixed laws, such that, outside an event of probability at most
\[
 C_{B_0}N^{-B_0}+C\exp(-cN),
 \tag{Weighted-low-exception}
\]
every omitted index i simultaneously has the following implication:
\[
 \begin{split}
 &A_i\ne0,\quad\|D_i\|\le N^K,
       \quad H_i^{\rm wt}(N^{-H},r_N)\text{ fails}\\
 &\hspace{15mm}\Longrightarrow\quad
 \rho_i:=\frac{|\det D_i|}{\|A_i\|_F}\le N^{-T_0},
       \qquad s_{\min}(D_i)\le\sqrt{N-1}\,N^{-T_0}.
 \end{split}
 \tag{Weighted-low-ratio}
\]
Constants are uniform over deterministic shifts max|F_ab|<=N^gamma and may depend on the displayed exponents, c,eta,zeta and the fixed sequence r_N.
The sufficiently large size may depend on that sequence.
For an independent random shift the same assertion holds on its polynomial entry guard, after conditioning on its realization within each size.
No independence across physical sizes is used or concluded.

Here is the parameter order and the complete deduction from the previous lemmas.
Use the fixed central-strip parameter eta_0=1/16 in [the actual-minor exclusion](#central-strip-diagonal-exclusion), and request its failure exponent B_0+3 for each widehat D_i.
Let L be its common internal symmetric-floor exponent and let L0 be the symmetric-floor exponent for widehat D_i itself, also selected with enough margin for the N-index union.
Both depend only on the laws,gamma,B_0, and are chosen before the fine coefficient exponents.
Choose fixed J,H in the order
\[
 J>2K+L0+T_0+1,\qquad
 H>\max\{J+L+2K+1,\ 2K+L0+T_0+2\}.
 \tag{Weighted-parameter-order}
\]
In the cyclic ordering, take the endpoints I of a maximal matching for widehat Q_i.
When its matching size is less than r_N, one has |I|<2r_N and every off-diagonal entry outside I is smaller than N^(-H)||A_i||_F.
Except with the actual-minor exclusion probability, all its diagonals outside I and the fixed central strip are smaller than N^(-J)||A_i||_F.
The fixed strip is determined by the cyclic order and is not chosen adaptively or counted in the cover union.
The support on its union with I has matrix rank at most
\[
 4r_N+2\eta_0(N-1)+4<N-1
\]
eventually.
The remaining error has Frobenius norm at most
\[
 e_N\|A_i\|_F,
 \qquad e_N=\sqrt{N-1}\,N^{-J}+(N-1)N^{-H}.
\]
The second identity above, applied to widehat D_i and this low-rank approximation, gives
\[
 \rho_i\le N^{2K+L0}e_N\le N^{-T_0}
\]
eventually by (Weighted-parameter-order).
If D_i is invertible, then rho_i=(sum_j s_j(D_i)^(-2))^(-1/2), so s_min(D_i)<=sqrt(N-1)rho_i.
If D_i is singular and A_i is nonzero, it has exactly corank one and both quantities on this last inequality are zero.
This proves the full implication at one i.
Union its error bounds over N choices of i, using the B_0+3 margin, to obtain (Weighted-low-exception).
The same proof is uniform over the deterministic shift, which justifies the independent random-shift form.

This establishes a useful correctly weighted low-matching exclusion for the phase-line submodel with Re c nonzero.
It does not bound the probability that H_i^(wt) fails without the small-ratio alternative, and it does not supply the complex isolated-minor or second-smallest estimates needed for a least-value theorem.

<a id="phase-line-remaining-event"></a>
## The remaining full-matrix event is now explicit

The [surviving complex rectangular-distance mechanism](#complex-distance) and the deterministic cofactor averaging of C_F0194_v3 give constants delta,a,C_1>0 as follows.
For fixed K>=0, let
\[
 \begin{split}
 E_N(K,\varepsilon)&=\{\|M_N\|\le N^K,
       \ \operatorname{rank}M_N\ge N-1,
       \ s_{\min}(M_N)\le\min(\varepsilon,a/(4\sqrt N))\},\\
 G_i(K,\varepsilon)&=\{A_i\ne0,\ \|M_N\|\le N^K,
       \ |\det M_N|/\|A_i\|_F
              \le C_1N^{2K+1}\varepsilon\}.
 \end{split}
\]
Outside a common exp(-cN) event, E_N forces at least delta N/2 of the events G_i, by the identical pointwise spread and row-adjugate proof.
This use of C_F0194_v3 is restricted to that deterministic averaging and to the rectangular-distance argument whose complex-law exponential input was proved above.
It does not reuse a real-input rank exception as a complex-input rank theorem.

Choose H from (Weighted-parameter-order) and put h_N=N^(-H).
For every epsilon_N with C_1N^(2K+1)epsilon_N<=c_*h_N/N, the weighted matching bound and (Weighted-low-ratio) imply
\[
 \begin{split}
 \mathbb P(E_N(K,\varepsilon_N))
 &\le C\psi(r_N)+C_{B_0}N^{-B_0}\\
 &\quad+\frac C N\sum_{i=1}^N
 \mathbb P\{G_i(K,\varepsilon_N)\cap
        (H_i^{\rm wt}(h_N,r_N))^c\cap\{\rho_i\le N^{-T_0}\}\},\\
 \psi(r)&=e^{-cr}+\sqrt{\log(2+r)}\,r^{-1/9}.
 \end{split}
 \tag{Phase-line-reduction}
\]
The exponentially small common exceptions have been absorbed into the polynomial term.
The proof is pointwise averaging over the usable indices, splitting each G_i by H_i^(wt), applying (Weighted-matching-row) to the high part, and applying the simultaneous low-ratio implication to the other part.
It does not union the matching probability over N indices.
For example epsilon_N=N^(-A) satisfies the scale condition eventually if A>H+2K+2.

The displayed terminal event is deliberately retained.
It involves both the small full-matrix cofactor ratio and an arbitrarily fine small actual-minor ratio; a low-matching assertion alone is not being treated as its probability bound.
Removing the rank-at-least-N-1 guard, proving a suitable second-smallest minor floor, and controlling this terminal event require phase-line inputs in addition to this reduction.
The accepted real-Wigner profile count is not automatically valid for its phase-oriented Hermitian matrix.
The finite-phase count and explicit transfers below provide the additional developed arguments; this reduction alone does not supply a least-value theorem.

<a id="phase-envelope-count"></a>
## A finite-phase envelope repairs the profile count

There is a further phase-line counting repair, separate from the cyclic gauge and requiring only the accepted real-scalar linear inverse theorem.
This paragraph and the following proof concern any fixed unit-modulus c, including Re c=0; they do not assert a least-value floor in the parity-obstructed case.
Let eta_n be the independently truncated real law eta conditioned on |eta|<=n^kappa.
Nondegeneracy supplies fixed a_*,b_*,p_*>0 with P(a_*<=|eta-eta'|<=b_*)>=p_* for independent copies.
The truncated law converges to eta in total variation, so the same anti-concentration bound, with p_*/2, holds uniformly for eta_n eventually.
These are the uniform (AC) constants used by the accepted real-scalar inverse theorem.
Let D have independent raw upper amplitudes eta_n, deterministic edge phases omega_jk in {c,bar c}, mirrored lower phases bar omega_jk, deterministic diagonal, and an arbitrary deterministic complex shift.
Assume all resulting entries, raw amplitudes, shift entries and relevant row norms have a common polynomial bound n^K after enlarging K.
The constants below are uniform in this deterministic phase pattern.
In particular a simultaneous row-and-column permutation remains in this class, even though its complex upper-entry laws need not be identical.

For a deterministic vector u and a coordinate subset J define
\[
 \mathcal R_J(u,t)=
 \max_{e\in\{c,\bar c\}^{J}}
 \sup_{z\in\mathbb C}
 \mathbb P\left\{\left|\sum_{j\in J}e_ju_j\eta_{n,j}-z\right|\le t\right\}.
 \tag{Phase-envelope}
\]
The maximum is attained since its phase set is finite.
For J contained in J', convolution with the extra independent variables gives R_J'(u,t)<=R_J(u,t).
Thus the tail envelopes R_i(u,t)=R_{[i,n0]}(u,t) are nondecreasing in i, exactly as the scalar tail concentrations in the fixed count.
Adding a reservoir coordinate never increases its envelope.
All phases have modulus one, so the support-disk lower bound and the single-large-coordinate bound are uniform over phase assignments.

Here is a complete check of the counting changes.
Fix epsilon=1/100, a structural constant C_0 and a sufficiently fine integer a, and put beta_0=n^(-a+C_0)=n^(-s).
Replace the initial rational structured class by vectors u with 1/2<=||u||<=2 for which all but C_0 n^epsilon coordinates belong to
\[
 \Gamma Q,\qquad \Gamma=\{1,c,\bar c\},
\]
where Q is a rational complex progression with the same bounded rank, polynomial integer-box size and generator-height bounds as the accepted class.
The exceptional coordinates are on the ordinary rational complex lattice at the stated fine precision.
The progression and exceptional grid have exactly the same polynomial descriptions as in the fixed count; the fixed factors in Gamma are not required to be rational.
The coordinatewise phase labels cost at most 3^n choices, and hence the total coarse number is still
\[
 n^{C_*n+O_a(n^\epsilon)+O_a(1)},
 \tag{Envelope-coarse-count}
\]
with C_* independent of the fine precision a.
An extra bounded number of rational generators or a larger fixed structural constant is harmless here.

Choose a bulk of size n0=n-O(n^epsilon) containing a largest coordinate, and place that coordinate last, with |u_n0|>=1/(2sqrt(n)).
If the largest coordinate was exceptional, adjoin its ordinary rational value as one additional generator of Q; it then belongs to the Gamma=1 part of Gamma Q.
If it was already nonexceptional, its existing phase label places it in Gamma Q without an additional irrational generator.
This explains the inclusion of 1 in Gamma and avoids imposing false rationality on phase-rotated coordinates.
The generator-size changes, exceptional-index choices and bulk permutations retain the same coarse entropy order.

Write R_i(u,t) for the resulting tail envelope and retain any prescribed set of at least n-C_0 row constraints.
Expose entries joining the bulk to its complement, then expose its rows in increasing order.
The unexposed random part in row i is a sum of independent eta_n variables with coefficients omega_ij u_j, with each omega_ij in {c,bar c}.
Its conditional concentration is at most R_(i+1)(u,t), irrespective of the deterministic orientation pattern.
The usual product rule, the polynomial support-disk bound R_i>=n^(-D0), and the at most C_0 omitted rows give
\[
 \mathbb P\{|(Du)_i|\le t\text{ on the prescribed rows}\}
       \le n^{D0(C_0+1)}\prod_{i=1}^{n0}R_i(u,t),
       \qquad \beta_0\le t\le1.
 \tag{Envelope-row-product}
\]
The shift and already exposed entries only change the center.
For t<=c_0/sqrt(n), every R_i is at most the same p_0<1, by the large coordinate and the uniform (AC) bound.
These statements remain valid after every candidate-dependent permutation, because the deterministic phase pattern is allowed to change inside the same finite set.
This replaces the invalid requirement that such a permutation preserve identical complex upper-entry laws.

Choose C_1>C_*+10 and discard candidates with product_i R_i(u,beta_0)<n^(-C_1 n), using the coarse count and (Envelope-row-product).
Their total probability is at most n^(-cn).
Set q=ceil(n^(1-epsilon)), theta=epsilon/10 and t_*=n^(-K-5), as in the fixed profile count.
Call a candidate degenerate if every q-coordinate subset J of its bulk satisfies R_J(u,t_*)>=q^(-1/2+theta).
For any such subset choose a phase assignment attaining its envelope and apply the accepted real-scalar, complex-coefficient linear inverse theorem to the coefficients e_j u_j.
With allowed exception count floor(q/2), its progression-size bound is eventually one.
The progression is proper and symmetric and therefore equals {0}.
Consequently at least ceil(q/2) coordinates of that subset have |u_j|<=C t_*, since |e_j|=1; the harmless fixed closeness constant is absorbed into C.
It follows that at most floor(q/2) bulk coordinates have modulus greater than C t_*.
Round these coordinates and the nonbulk coordinates at mesh t_* and set the others to zero.
The resulting family has exp(O_K(q log n))=exp(o(n)) elements, its largest coordinate survives, and its row tolerance is at most C n^(-4) when s is large.
The direct p_0^(n0-C_0-1) row bound proves an exp(-cn) total probability for this branch.
No union over phase assignments of a degenerate subset is needed: its maximizing assignment is used only to deduce the small-coordinate property.

For a nondegenerate candidate select a q-subset with envelope smaller than q^(-1/2+theta), add the largest coordinate if needed, and put this reservoir at the end of the bulk.
Its size q0 is q or q+1, and the number of choices and prescribed permutations is exp(O(q log n))=exp(o(n)).
Every tail containing it has envelope at most its reservoir envelope, uniformly over all phase assignments.
For p=n0-q0=n-o(n), this gives
\[
 R_i(u,t)\le n^{-b_0},\qquad
 b_0=1/2-3\epsilon/4,
 \quad i\le p,\ t\le t_*.
\]
As in the accepted repaired count, rerun the coarse low-product classification after this permutation.
The discarded post-permutation low-product candidates again cost n^(-cn), since (Envelope-row-product) holds uniformly for the new deterministic phase pattern.
Do not transfer the earlier product between orders.
For the remaining candidates, pi_(beta_0)=product_(i=1)^p R_i(u,beta_0)>=n^(-C_1 n).

Put R_n=n^(K+3), t_l=R_n^l beta_0 and L_*=ceil(C_1/epsilon)+2.
Choose a large enough that t_(L_*+1)<=t_*.
There is an l in [0,L_*] with
\[
 \prod_{i=1}^p R_i(u,t_{l+1})
       \le n^{\epsilon n}\prod_{i=1}^p R_i(u,t_l).
 \tag{Envelope-stable-scale}
\]
Otherwise iteration would exceed one.
Partition the envelopes R_i(u,t_l), between their polynomial lower bound and n^(-b_0), into intervals [r_h,n^epsilon r_h) with power-of-n endpoints.
Monotonicity makes each bin a consecutive block, of length m_h, and there are only a fixed number H of bins and polynomially many profiles.

At the first tail in each block choose a phase assignment attaining its envelope and apply the real-scalar inverse theorem, now with exception count n'=floor(n^(1-2epsilon)).
Its tail length is at least q, so this is a permitted exception count.
The theorem gives a rational complex progression Q_h of bounded rank with
\[
 |Q_h|\le C r_h^{-1}n^{-1/2+\epsilon}.
\]
The normalized-tail norm cancels from the relative-radius generators exactly as in C_F0194_v1: after rescaling, each generator coordinate has the form t_l p_j/p with polynomially bounded integers.
Hence the generator choices are polynomial in n, with constants allowed to depend on the fixed a.
Each nonexceptional original coordinate is approximated at radius C t_l by either c^(-1)Q_h or bar(c)^(-1)Q_h.
Absorb the fixed closeness constant in the rounding and later scale slack.
Recovery from phase-multiplied coefficients costs at most two choices per coordinate, not a choice for every matrix entry.
Across the profile the total extra cost is at most 2^p=exp(O(n)).
Rounding all exceptional, reservoir and nonbulk coordinates on a polynomial complex grid costs exp(o(n)), exactly as before.
The resulting count for one profile is therefore
\[
 \exp(O(n)+o(n))\,
 n^{-(1/2-\epsilon)p}\prod_h r_h^{-m_h}.
 \tag{Envelope-profile-count}
\]
Possible incompatibility of phase assignments chosen in overlapping tails is irrelevant: ignoring those consistency constraints enlarges the counted set and already gives this upper bound.

Select one original deterministic witness u for each rounded vector u' in its fixed profile before imposing the random row equations.
Coordinatewise approximation is O(t_l), so the error in every tail sum, for every phase assignment, is at most C n^(K+1)t_l.
For t'=beta_0+C n^(K+1)t_l, the enlarged scale t_(l+1) consequently gives
\[
 \mathcal R_{[i,n0]}(u',t')
       \le\mathcal R_{[i,n0]}(u,t_{l+1})
\]
for all sufficiently large n, simultaneously for every i.
Taking the maximum preserves this inequality because the comparison holds separately for each phase assignment with the same error bound.
The row-product estimate, (Envelope-stable-scale), and the profile upper endpoints bound the probability for this rounded vector by
\[
 n^{O_{s,K,C_0}(1)}n^{2\epsilon n}\prod_h r_h^{m_h}.
 \tag{Envelope-profile-probability}
\]
Multiplication by (Envelope-profile-count) cancels the concentration factors exactly and gives at most n^(-n/3) eventually, since p=n-o(n).
The polynomial number of profiles, bounded scales, subexponential reservoirs and initial low-product cases preserve an exp(-cn) final bound.

Thus existence of a vector in this finite-phase rational-progression class satisfying the prescribed n-C_0 approximate row constraints has probability at most C exp(-cn), uniformly over the allowed deterministic phases, diagonals and nonsymmetric shifts.
The parameter order remains structural constants, coarse entropy C_*, product threshold C_1, scale count L_*, and only then the fine precision a.
The proof introduces no factor of the form 2^(n^2) or n^(C n) from the phase recovery; its only new leading-coordinate factor is a fixed constant to the power n.
This is project development using the inspected real-scalar inverse theorem, not an independent review of either the new deduction or the source proof.

<a id="phase-envelope-kernel-interface"></a>
## Consequence for omitted-row and near-kernel anti-concentration

The finite-phase count supplies the exact linear inverse interface previously missing for phase-line matrices.
Fix b,K>0 and a fixed integer s0>=0.
For the independently truncated phase-pattern matrix D above there are fixed a,L>0 and an exceptional event of probability at most C exp(-cn) such that, outside that event, every unit vector u satisfying
\[
 |(Du)_j|\le n^{-L}
       \quad\text{on any prescribed set of at least }n-s0\text{ rows}
\]
has R_[n](u,n^(-a))<=n^(-b).
The same assertion holds for D^T, uniformly over all such prescribed row sets.
In particular it covers exact kernels and a kernel with one omitted row.

To verify this interface, if the envelope is larger than n^(-b), choose its maximizing phase assignment and apply the accepted real-scalar linear inverse theorem to e_j u_j.
Its structural constants depend on b and the fixed exception exponent, not the final fine precision a.
Round its progression representatives, recover u_j by the fixed inverse phase, and round its exceptional coordinates on the ordinary rational grid.
The resulting w lies in the finite-phase class above, has norm between 1/2 and two, and satisfies ||w-u||_infinity<=C n^(-a).
Since |e_j|=1, the rounding does not change that accuracy.
For every prescribed row,
\[
 |(Dw)_j|\le n^{-L}+C n^{K+1-a}.
\]
Choose the class's fixed structural slack greater than K+2 and s0, select a sufficiently large for its count, and then L>a+1.
The displayed tolerance is inside the counted class.
The count excludes existence of any such rounded candidate with probability C exp(-cn).
This finite candidate event is measurable and covers all possible unit witnesses, without a measurable selection from the set of actual kernels.
The at most n^s0 row-set choices are absorbed in the same exponential bound, and D^T has phases in the same set.

This proves a linear, omitted-row and near-kernel ingredient at the phase-line scope.
The following sections check its actual rank-growth, rectangular second-value and isolated-minor interfaces and their parameter conversions explicitly.
They develop the new assembly rather than applying the real-input final theorem as an unchanged input.

<a id="phase-line-rank-tail"></a>
## Phase-line corank tails from the actual two border forms

The following auxiliary result uses only the finite-phase count and is valid for every fixed |c|=1, without assuming Re c is nonzero.
For raw phase-line Hermitian X_n and every gamma,B>0 there are C,n0 such that
\[
 \sup_{\max|F_{jk}|\le n^\gamma}
 \mathbb P\{\operatorname{rank}(X_n+F)\le n-2\}
       \le Cn^{-B},\qquad n\ge n0.
 \tag{Phase-rank-tail}
\]
The diagonal law is fixed real finite-second-moment, and the offset is any deterministic complex matrix.
This is the rank-growth deduction of [C_F0194_v2](Yin_C_F0194_v2.md#rank-chain) with its actual scalar anti-concentration input replaced and verified here; the real-input probability theorem is not being cited as a phase-line theorem.

Choose a raw cutoff kappa>(B+4)/2 and condition on all |eta_jk|,|zeta_j|<=n^kappa, discarding probability at most Cn^(-B-2).
The remaining eta_n variables are independent with uniform (AC) constants; fix the diagonal values by conditioning.
Use the leading-principal chain M_k, floor(n/3)<=k<=n, within this one physical matrix.
The ratio n/k is bounded by four for all large n, so one polynomial entry bound k^K and the same uniform truncated-law (AC) constants apply throughout the chain.
The count above depends on those constants, not on whether the original truncation parameter is indexed by k or by n.

For a singular current block D of size k, choose unit u in ker D and v in ker D^T measurably by rank strata and the lexicographically first maximal nonzero minor, solving the first free coordinate and normalizing.
At rank zero use a coordinate vector.
This is the explicit Borel construction already given in [C_F0194_v2](Yin_C_F0194_v2.md#border-rank).
The actual new border has row r^T and column d, with
\[
 r_j=e_j\eta_{n,j}+f_j,\qquad
 d_j=\bar e_j\eta_{n,j}+g_j,
       \quad e_j\in\{c,\bar c\}.
\]
For a standard leading chain all e_j may be the same, but the envelope covers either pattern.
The shifted row and column share their real amplitudes, and no independence between the two resulting forms is used.
Outside the current block's exp(-ck) count exception, the kernel interface gives, for any desired fixed b,
\[
 \mathbb P\{r^Tu=0\mid D\}\le k^{-b},\qquad
 \mathbb P\{v^Td=0\mid D\}\le k^{-b}.
\]
Exact zero is contained in the allowed positive-radius small-ball event, and its deterministic shifts are arbitrary centers.
When both forms are nonzero, the deterministic complex border-rank calculation increases rank by exactly two, regardless of the new diagonal entry.
Its failure probability is at most 2k^(-b)+C exp(-ck) after integrating over D.
Choose b>B+4 and union over the chain steps.

On the complementary event, if d_k=k-rank M_k>0 then d_(k+1)=d_k-1; if d_k=0 then d_(k+1) is zero or one by rank monotonicity.
Starting from deficiency at most floor(n/3), the chain has enough steps to enter deficiency at most one and remain there.
Thus its final rank is at least n-1.
Adding the chain and raw-cutoff failures proves (Phase-rank-tail).
Multiplying W_n+F by sqrt(n) changes the shift exponent from gamma to at most gamma+1 and leaves rank unchanged, giving the normalized version.
The same proof and uniformity permit independent random shifts on their polynomial guard.
This corank-at-most-one conclusion is compatible with the pure-imaginary odd-size obstruction.

<a id="phase-line-second-floor"></a>
## The projected row and omitted-row kernel give a second-value floor

For every fixed |c|=1, gamma,B>0 there is a finite A_2>0 such that the raw model satisfies
\[
 \sup_{\max|F_{jk}|\le n^\gamma}
 \mathbb P\{s_{n-1}(X_n+F)\le n^{-A_2}\}\le Cn^{-B}.
 \tag{Phase-raw-second}
\]
Singular values are ordered decreasingly.
The normalized model W_n+F has the same assertion after changing A_2.
No least-value estimate is part of this auxiliary statement.

Use the independent raw cutoffs with kappa>(B+4)/2 and choose a fixed entry exponent K for all size-(n-1) principal blocks and borders.
Work conditionally on the bounded real diagonal values, keeping independent eta_n amplitudes with uniform (AC) constants.
Choose b>B+4 and a according to the one-omitted-row case of the envelope kernel interface, uniformly for sizes m=n-1 and law eta_n.
Let M=X_n+F and retain its first n-1 rows as the rectangular matrix B0.
For each retained row i, delete coordinate i from that row and the other retained rows, calling the projected row z_i and the projected other-row matrix C_i.
The entries of z_i are independent of D_i=M[[n] minus {i}], since their mirrored partners are exactly in the deleted coordinate i.
Here C_i is D_i with the row of original index n omitted, and z_i is the actual exposed row projected onto the remaining coordinates.
The initial projection is a contraction, so
\[
 \operatorname{dist}((B0)_i,\operatorname{rowspan}(B0)_{-i})
    \ge\operatorname{dist}(z_i,\operatorname{rowspan}C_i).
\]

Use the deterministic monomial unitary U_i=Z_iP_i from (Phase-gauge), now at raw normalization.
Right multiplication by U_i preserves row distances and transforms the random part of z_i into iid real eta_n entries.
Write C_i=R_l D_i, where R_l deletes the row corresponding to original index n.
Then
\[
 C_iU_i=R_l U_i\widehat D_i=L_i R_{\widehat l}\widehat D_i,
\]
where widehat l is the cyclic coordinate of that row and L_i is an invertible monomial unitary on the retained row indices.
The equality follows because R_l U_i is a selection of all but one of the rows of a monomial unitary.
Its left factor L_i only reorders and rescales those selected rows by unit-modulus constants, so it preserves their row span.
Therefore rowspan(C_iU_i) is exactly the span of all rows of widehat D_i except widehat l.
This verifies both sides of the unitary change; there is no assumption that omitting a row commutes literally with conjugation.

Choose a bilinear unit normal u_i to these rows measurably by the same rectangular rank-stratum and first-free-column construction.
It satisfies (widehat D_i u_i)_j=0 except at widehat l.
Outside the widehat D_i-measurable exp(-cm) kernel exception, its envelope at radius m^(-a) is at most m^(-b).
Ordinary real-eta concentration is no larger than this envelope: choose the constant phase e_j=c in (Phase-envelope), which only rotates the complex disk.
Conditional on D_i, the random entries of z_iU_i are independent real eta_n copies plus a fixed center and are independent of u_i.
Since n^(-a)<=m^(-a),
\[
 \mathbb P\{|(z_iU_i)u_i|\le n^{-a}\mid D_i\}\le m^{-b}
\]
on that guard.
The complex Hilbert normal is bar u_i, and Cauchy--Schwarz gives distance(z_iU_i,rowspan C_iU_i)>=|(z_iU_i)u_i|.
The diagonal entry at i was deleted and creates no conditional randomness issue.
Consequently each retained full-row distance is greater than n^(-a), outside probability m^(-b)+C exp(-cm).

Union the n-1 retained rows.
On their good event B0 has full row rank, and the elementary rectangular Gram-inverse identity gives
\[
 \sum_{j=1}^{n-1}s_j(B0)^{-2}
   =\sum_{i=1}^{n-1}\operatorname{dist}((B0)_i,
                  \operatorname{rowspan}(B0)_{-i})^{-2}
   \le n^{2a+1}.
\]
Thus s_(n-1)(B0)>=n^(-a-1/2).
Adding the final row is a positive-semidefinite Gram perturbation, so s_(n-1)(M) has the same lower bound.
Choose A_2>a+1/2 and restore the discarded raw-entry tail to prove (Phase-raw-second).
For normalized W_n+F, use the raw matrix sqrt(n)(W_n+F), with shift exponent at most gamma+1, and divide its singular values by sqrt(n).
This proves the normalized assertion with another fixed exponent.
It applies uniformly to actual principal minors after the same comparable-dimension conversion, and to independent random shifts on their guard.

<a id="phase-line-isolated-minor"></a>
## The isolated-minor branch after a real-border gauge

There is a phase-line counterpart of the exact restricted isolated-minor estimate, again valid for every fixed |c|=1.
Work in raw size n with deterministic shift entry bound n^gamma.
For every requested B>0 there are fixed A_0,L_iso>0 such that the probability is at most C_B n^(-B) that some actual D_i has nonzero adjugate and
\[
 \frac{|\det M|}{\|\operatorname{adj}D_i\|_F}\le n^{-A_0},
\]
while D_i is either exactly corank one or is invertible with
\[
 t_1(D_i)\le n^{-L_{\rm iso}},\qquad
 t_1(D_i)/t_2(D_i)\le n^{-L_{\rm iso}}.
 \tag{Phase-isolation}
\]
Here t_1<=t_2 are the two smallest values.
The original real-input theorem is not being applied to a complex entry law; its deterministic rank-one product calculation is reused with the following verified phase-line concentration input.

Choose a raw cutoff kappa>(B+4)/2, then K controlling the exposed diagonal, both shifted border norms, and all minor entries on the cutoff event.
Choose b>B+4, and let a_lin,L_ker be the near-kernel envelope exponents for size m=n-1 at this b,K, for D and D^T.
Choose a0>a_lin+1, put A_0=2a0, and finally choose
\[
 L_{\rm iso}>\max\{L_{\rm ker}+1,\ 2a0+2K+3\}.
\]
The choices are fixed before the actual random minor or border is exposed.
For every i, the gauge gives widehat D_i with the same singular values and a real iid eta_n border x, with arbitrary deterministic offsets f,g and the same full determinant and adjugate norm.
The transformed minor's shift and independent diagonal remain within the polynomial guard, so the near-kernel count applies to widehat D_i and its transpose.

For an invertible isolated minor its singular-value decomposition gives unit u,v with
\[
 \|\widehat D_i u\|=\|\widehat D_i^Tv\|=t_1,
 \quad
 \frac{\widehat A_i}{\|\widehat A_i\|_F}=\alpha uv^T+E,
 \quad |\alpha|\ge1/2,
 \quad\|E\|_F\le\sqrt m\,t_1/t_2,
 \quad\frac{|\det D_i|}{\|A_i\|_F}\le t_1.
\]
The amplitude bound holds for all sufficiently large n under the displayed relative isolation.
For exactly corank-one D_i, take E=0, |alpha|=1 and both residuals zero.
On the polynomial border bounds, the exact determinant formula divided by ||A_i||_F differs from
\[
 -\alpha\,[u^T(x+f)]\,[v^T(x+g)]
\]
by at most n^K t_1+n^(2K) sqrt(m)t_1/t_2, or by zero in the exact singular branch.
The chosen L_iso makes this at most n^(-2a0-1) eventually.
Hence the tiny full-ratio event forces at least one linear form to have modulus at most 2n^(-a0).
No independence between those two forms is assumed.

Their coefficient vectors have near-kernel residuals at most n^(-L_iso), inside the universal envelope interface for widehat D_i and its transpose.
Outside its exp(-cm) exception both have ordinary real-eta concentration at most m^(-b), because ordinary concentration is bounded by the phase envelope.
The radius 2n^(-a0) is eventually below m^(-a_lin), and the affine shifts are allowed centers.
Conditional on the minor, the probability of the product-small event is therefore at most 2m^(-b).
Measurable singular vectors may be chosen on finite spectral-rank strata; the universal near-kernel assertion in any case covers every such choice.
Integrate the minor exception, union n choices of i, and restore the cutoff tail.
This proves the restricted isolated-minor estimate at the displayed parameter order and scale.

<a id="in-probability-floor"></a>
## Complete in-probability floor assembly

Here is the full assembly and parameter order, retaining all normalization changes.
First choose a raw cutoff exponent kappa>(B+6)/2 and a norm exponent K>max{kappa+1/2,gamma+1}, enlarging for fixed constants.
The finite-second-moment union bound and ||F||<=N^(gamma+1) give P(||M||>N^K)<=C_B N^(-B-2), with M=W_N+F.
The phase-line rank-tail argument, applied to sqrt(N)M with raw shift exponent gamma+1, also makes P(rank M<=N-2)<=C_B N^(-B-2).
The complex-distance proof above applies to every cross-rectangle coordinate with law c eta or bar c eta, without requiring independent real and imaginary components.
Together with the unchanged deterministic row-adjugate and support-union proof it therefore gives the many-index averaging used in (Phase-line-reduction), on the remaining norm and rank guards.

Next apply (Phase-raw-second) to the raw matrices sqrt(N)D_i, whose dimension is N-1 and whose shift entries are bounded by N^(gamma+1/2)<= (N-1)^(gamma+2) eventually.
Choose its failure exponent with margin for the N-minor union and its final division by sqrt(N).
There is a fixed L_2>0 outside probability C_B N^(-B-1) on which
\[
 t_2(D_i)\ge N^{-L_2}\quad\text{for every }i.
\]
Choose A_0,L_iso in the raw phase-line isolated-minor estimate with shift exponent gamma+1 and requested failure exponent B+2.
These exponents are selected before the fine low-matching precision.

Choose the symmetric-part exponents L,L0 in the weighted low-matching proof with enough probability margin for all N transformed principal minors and all their internal row deletions, at most N^2 in total.
This use of the real C_F0188_v2 theorem is legitimate exactly because the cyclically gauged minor has standard phase-line law with nonzero Re c.
No conditional-on-imaginary-entries use is made.
Choose
\[
 T_0>L_{\rm iso}+L_2+2,
 \quad J>2K+L0+T_0+1,
 \quad H>\max\{J+L+2K+1,\ 2K+L0+T_0+2\},
\]
and put h_N=N^(-H), r_N=floor(sqrt(N)).
Then r_N log(N)=o(N), and the simultaneous weighted low-matching implication holds outside probability C_B N^(-B-1)+C exp(-cN), using stronger requested exponents there if necessary.
For a nonzero-adjugate low-matching minor it gives rho_i<=N^(-T_0) and therefore t_1(D_i)<=sqrt(N-1)N^(-T_0).
If it is invertible, the raw absolute and relative thresholds follow from
\[
 t_1(\sqrt N D_i)\le N^{-T_0+1},
 \qquad
 \frac{t_1(\sqrt N D_i)}{t_2(\sqrt N D_i)}
      \le N^{-T_0+1/2+L_2}.
\]
Both are at most N^(-L_iso) eventually by the chosen T_0.
If D_i is singular with nonzero adjugate, it is exactly corank one and already belongs to the singular isolated branch.
This verifies the smallness and gap requirements, rather than treating a small minor ratio as isolation by itself.

Finally choose
\[
 A>\max\{H+2K+2,\ A_0+2K+2,\ 1\}.
\]
For epsilon_N=N^(-A), the usable-index event G_i has full normalized cofactor ratio at most C_1 N^(2K+1-A), within the weighted matching radius c_*h_N/N eventually.
Its raw isolated-minor ratio satisfies the exact identity
\[
 \frac{|\det(\sqrt N M)|}
 {\|\operatorname{adj}(\sqrt N D_i)\|_F}
     =N\,\frac{|\det M|}{\|A_i\|_F}
     \le C_1N^{2K+2-A}\le N^{-A_0}
\]
eventually.
The factor is N because the raw determinant has degree N and the raw minor adjugate has degree N-2.
Unitary gauge and cyclic permutation introduce no further factor.

Split the pointwise many-index average by H_i^(wt)(h_N,r_N).
The high-matching contribution is at most C psi(r_N), by (Weighted-matching-row), with no union factor N.
On all retained low-matching and second-value guards, every remaining G_i implies one of the raw restricted isolated-minor events just proved.
The probability of their union is at most C_B N^(-B-2); the mean of their indicator probabilities is no larger than this union probability.
Adding norm, rank, symmetric-part, low-matching and second-value exceptions proves
\[
 \mathbb P\{s_{\min}(M)\le N^{-A}\}
       \le C_BN^{-B}+C\psi(\lfloor\sqrt N\rfloor),
\]
which is the main bound (Phase-floor).
The conditional independent-random-shift form follows by integrating the uniform deterministic estimate within this dimension, without conditioning on an entire cross-size sequence.

The proof uses the existing accepted real-scalar inverse theorem, bounded-product concentration theorem and MNV16 theorem only at their inspected scopes.
All finite-phase envelope, cyclic gauge, kernel, second-value and probability-transfer steps are the developed local arguments above.
No independent review is inherited for these new arguments from the accepted real-input Claims.

## Current assessment
[Selected decision](#decision-phase-line-floor-reviewed)

## Assessment history

### Decision phase-line-floor-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T11:58 |
| status | open |
| reason | A complete phase-line least-value argument and its precisely scoped auxiliary assertions are fixed for fresh independent review, including cyclic gauge, finite-phase profile count, omitted-row kernels, rank and second-value guards, isolated minors and the parameter-ordered weighted matching assembly. No summability or general complex-law Task conclusion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact main and auxiliary assertions](#statement) | The nonzero-real-part phase-line in-probability floor and independent random-shift guard, with the separately stated broader auxiliary ranges and the pure-imaginary odd-size boundary. |
| argument | [Complete phase-line candidate proof](#argument) | All new projection, majority and strip, cyclic weighted adjugate, phase-envelope count, kernel, rank, rectangular second-value, isolated-minor and final normalization interfaces. |
| dependency | [Symmetric-part floors](Yin_C_F0188_v2.md#statement) | Only real-Wigner floors under complex symmetric shifts, applied to symmetric parts after fixed real-variance scaling and the displayed minor unions. |
| dependency | [Accepted complex projection input](Yin_C_F0187_v2.md#argument) | Only bounded-product convex concentration on independent real Euclidean blocks and the Gram-inverse identity; all new fixed-cutoff distance bounds are proved here. |
| dependency | [Fixed structured class](Yin_C_F0194_v1.md#counting-class) | Rational progression descriptions, polynomial boxes and finite omitted-row row constraints, expanded explicitly to a finite union of phase rotations. |
| dependency | [Accepted profile mechanism](Yin_C_F0194_v1.md#structured-vector-counting) | The complete reservoir, post-permutation low-product restart, multiscale profile and witness argument; the new envelope replacements and phase entropy are proved in full here. |
| dependency | [Linear inverse rounding interface](Yin_C_F0194_v1.md#inverse-rounding) | Exact dimension-two inverse output and relative-radius rational rounding for the real scalar amplitude law, with structural constants fixed before the fine precision. |
| dependency | [Real-scalar inverse source](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) | Only arXiv v1 Condition 1 and Theorem 1.3 for real scalar laws with vector-valued coefficients, at the recorded accepted original-proof inspection depth. |
| dependency | [Deterministic isolated-row product](Yin_C_F0194_v1.md#isolated-row-reduction) | Only its bordered determinant, adjugate rank-one approximation and product-small set inclusion; no real-law probability theorem is transferred unchanged. |
| dependency | [Measurable bordered rank algebra](Yin_C_F0194_v2.md#border-rank) | Borel kernel choices and rank increase two when both left and right kernel forms are nonzero; all phase-line anti-concentration and rank-chain probabilities are supplied here. |
| dependency | [Deterministic row-adjugate bound](Yin_C_F0194_v3.md#row-adjugate) | The arbitrary complex matrix inequality, invertible least-vector ratio and exactly-corank-one branch, independent of the entry law. |
| dependency | [Rectangular support argument](Yin_C_F0194_v3.md#rectangles) | Conditional column-distance, negative-second-moment and support-entropy steps using the new complex-coordinate exponential distance bound. |
| dependency | [Pointwise spread and averaging](Yin_C_F0194_v3.md#spread-and-average) | Only the deterministic many-usable-index implication and its average under explicit norm and rank guards; no real-input rank tail is imported. |
| dependency | [Exact normalized real-border matching](Yin_C_F0194_v3.md#two-copy-matching) | The complete finite-radius two-copy proof at coefficient scale h/N, applied after the border gauge; arbitrary conditional minor, center and lower-degree coefficients remain allowed. |
| dependency | [Matching-rank source theorem](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) | Only the original 2016 degree-two fair-sign finite-interval estimate and its matching rank definition, with original-proof inspection limits retained. |

### Decision phase-line-floor-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T12:12 |
| status | proved |
| reason | Independent whole-proof review verifies the main phase-line probability floor and every separately stated auxiliary assertion, including the complete finite-phase count, complex distance and majority estimates, cyclic gauge, rank and second-value guards, isolated minors and final normalization. All thirteen direct input interfaces are resolved at their stated scopes; the main error remains nonsummable and the general complex-law Tasks remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact main and auxiliary assertions](#statement) | The nonzero-real-part phase-line in-probability floor and independent random-shift guard, with the separately stated broader auxiliary ranges and the pure-imaginary odd-size boundary. |
| argument | [Complete phase-line proof](#argument) | All new projection, majority and strip, cyclic weighted adjugate, phase-envelope count, kernel, rank, rectangular second-value, isolated-minor and final normalization interfaces. |
| dependency | [Symmetric-part floors](Yin_C_F0188_v2.md#statement) | Only real-Wigner floors under complex symmetric shifts, applied to symmetric parts after fixed real-variance scaling and the displayed minor unions. |
| dependency | [Accepted complex projection input](Yin_C_F0187_v2.md#argument) | Only bounded-product convex concentration on independent real Euclidean blocks and the Gram-inverse identity; all new fixed-cutoff distance bounds are proved here. |
| dependency | [Fixed structured class](Yin_C_F0194_v1.md#counting-class) | Rational progression descriptions, polynomial boxes and finite omitted-row row constraints, expanded explicitly to a finite union of phase rotations. |
| dependency | [Accepted profile mechanism](Yin_C_F0194_v1.md#structured-vector-counting) | The complete reservoir, post-permutation low-product restart, multiscale profile and witness argument; the new envelope replacements and phase entropy are proved in full here. |
| dependency | [Linear inverse rounding interface](Yin_C_F0194_v1.md#inverse-rounding) | Exact dimension-two inverse output and relative-radius rational rounding for the real scalar amplitude law, with structural constants fixed before the fine precision. |
| dependency | [Real-scalar inverse source](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) | Only arXiv v1 Condition 1 and Theorem 1.3 for real scalar laws with vector-valued coefficients, at the recorded accepted original-proof inspection depth. |
| dependency | [Deterministic isolated-row product](Yin_C_F0194_v1.md#isolated-row-reduction) | Only its bordered determinant, adjugate rank-one approximation and product-small set inclusion; no real-law probability theorem is transferred unchanged. |
| dependency | [Measurable bordered rank algebra](Yin_C_F0194_v2.md#border-rank) | Borel kernel choices and rank increase two when both left and right kernel forms are nonzero; all phase-line anti-concentration and rank-chain probabilities are supplied here. |
| dependency | [Deterministic row-adjugate bound](Yin_C_F0194_v3.md#row-adjugate) | The arbitrary complex matrix inequality, invertible least-vector ratio and exactly-corank-one branch, independent of the entry law. |
| dependency | [Rectangular support argument](Yin_C_F0194_v3.md#rectangles) | Conditional column-distance, negative-second-moment and support-entropy steps using the new complex-coordinate exponential distance bound. |
| dependency | [Pointwise spread and averaging](Yin_C_F0194_v3.md#spread-and-average) | Only the deterministic many-usable-index implication and its average under explicit norm and rank guards; no real-input rank tail is imported. |
| dependency | [Exact normalized real-border matching](Yin_C_F0194_v3.md#two-copy-matching) | The complete finite-radius two-copy proof at coefficient scale h/N, applied after the border gauge; arbitrary conditional minor, center and lower-degree coefficients remain allowed. |
| dependency | [Matching-rank source theorem](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) | Only the original 2016 degree-two fair-sign finite-interval estimate and its matching rank definition, with original-proof inspection limits retained. |
| review | [Independent whole-proof phase-line finding](../audits/reviews/Yin_R_F0200_v6.md#finding) | Complete exact statement, all subsidiary assertions and argument, every declared input, conditional independence, finite-phase entropy, parameter order, raw scaling and boundaries; no unresolved mathematical gap in this scope. |
