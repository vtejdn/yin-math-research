---
author: Yin
---

# Complex Hermitian entry laws and the scope of nonsymmetric-shift floors

This bounded preparation concerns the complex Hermitian off-diagonal laws permitted by the original [F0012](../tasks/Yin_T_F0012_v3.md#contract), [F0013](../tasks/Yin_T_F0013_v1.md#contract), and [F0014](../tasks/Yin_T_F0014_v1.md#contract) contracts.
It tests the precise scope of the reviewed real-law [C_F0194_v5 theorem](../claims/Yin_C_F0194_v5.md#statement), without changing that fixed proof or assuming it covers complex scalar entry laws.
The existing [complex projection theorem](../claims/Yin_C_F0187_v2.md#argument) and [real symmetric-shift theorem](../claims/Yin_C_F0188_v2.md#statement) have different noise and transpose interfaces.
The next work identifies an actual counterexample to an unchanged extension when available, then separates surviving complex-coordinate estimates from missing inverse-concentration or algebraic steps.
This is development rather than an independent review of any fixed Claim.

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
In particular the real-law C_F0194_v5 conclusion cannot be extended unchanged to all admissible complex Hermitian laws, even for zero shift and a bounded two-point law.
No counting improvement can prove that false all-size conclusion.

This is not a counterexample to an original determinant-limsup Task, to Brown-measure convergence, or to a theorem restricted to even sizes or a suitable deterministic subsequence.
A single forced zero has empirical mass 1/N; this determinant calculation supplies neither a positive limiting mass bound nor a positive-probability failure of weak convergence.
A limsup can be obtained on a subsequence.
The calculation gives no least-value bound on the remaining even sizes.
In particular even-size control and direct determinant-limsup methods remain separate research possibilities.

<a id="transpose-noncancellation-failure"></a>
## The transpose coefficient has a real algebraic failure

In the same example the symmetric part sym W_N=(W_N+W_N^T)/2 is identically zero.
For an invertible even-dimensional realization D of a skew-symmetric matrix, D^(-1) is skew-symmetric and therefore
\[
 A=\operatorname{adj}D=(\det D)D^{-1}\ne0,
 \qquad Q=\operatorname{sym}A=0.
\]
This conditional algebraic statement does not assert that every even random realization is invertible.
It shows that both the symmetric-part floor and the noncancelling sym-adjugate graph used in the real-input proof can disappear in the complex-input model.
For example D=diag(J,...,J), with J=[[0,i],[-i,0]], is an invertible Hermitian skew-symmetric matrix with these properties.
The graph based on Q then has no edges at any positive threshold although A is nonzero.
This failure concerns the real-input transpose mechanism, not merely a weaker exponent in its inverse-concentration input.

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

Here is the complete fixed-cutoff adaptation of the [complex projection proof](../claims/Yin_C_F0187_v2.md#argument), using exactly its bounded-product convex concentration input.
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
Therefore the rectangular-distance and support-union portions of [C_F0194_v3](../claims/Yin_C_F0194_v3.md#spread-and-average) retain their exponential input for complex laws.
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
The [real symmetric-shift theorem](../claims/Yin_C_F0188_v2.md#statement) consequently supplies its polynomial floor, with adjusted law-dependent constants and exponents, for every deterministic polynomially bounded F_N.
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
The same polynomial cofactor expansion as in [C_F0194_v5](../claims/Yin_C_F0194_v5.md#internal-row-identity) gives, with R=B^(-1),
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

<a id="mixed-orientation-cancellation"></a>
## Cancellation remains possible with positive real-part variance

Let c=(1+i)/sqrt(2), xi=c epsilon, and consider two internal coordinates with opposite orientations:
\[
 z=(c\epsilon_1,\bar c\epsilon_2)^T,
 \qquad
 R=\begin{pmatrix}0&1-i\\1+i&0\end{pmatrix},
 \qquad B=R/2.
\]
Since R^2=2I, this B is exactly R^(-1).
Its norm is 1/sqrt(2), and
\[
 \operatorname{sym}B=\frac12\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad s_{\min}(\operatorname{sym}B)=1/2.
\]
For E=diag(1,-1), S=[[0,1],[1,0]] and T=[[0,-i],[i,0]], one has iTE=-S.
As x=(epsilon_1,epsilon_2)^T/sqrt(2) and y=Ex,
\[
 \Phi(z)=Sx+iTEx=0
\]
for every pair of signs.
Thus a floor for sym B, a bound for ||B||, and a positive variance of Re xi do not imply any positive singular rank for the complex internal-row random map at a general index.
Direct sums of these paired blocks give the same cancellation in arbitrary even internal dimension when the two orientation groups have equal size.
This is an exact obstruction to that deterministic bridge, with bounded well-conditioned B and sym B.

The two-coordinate configuration occurs at the middle index j=2 of a three-dimensional Hermitian Wigner matrix, with zero diagonal law and N=3: its internal column has orientations xi and conjugate xi.
Set the two internal diagonal shifts to zero and choose the internal off-diagonal deterministic shifts so that the event epsilon_13=1 makes the internal matrix equal to the displayed B.
Explicitly use F_13=(1-i)/2-c/sqrt(N) and F_31=(1+i)/2-bar(c)/sqrt(N); this is even a Hermitian bounded shift.
The event has probability 1/2 and is independent of the exposed two signs.
This realizes the failed conditional map within an actual minor, rather than using an impossible coefficient matrix.
The construction at one fixed dimension and the direct-sum coefficient example do not show nonvanishing asymptotic failure probability for a full random Wigner minor.
Excluding their higher-dimensional analogues probabilistically would require new information about the actual internal minor.

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
It also explains why the balanced zero-map construction does not contradict this lemma: its p-q is zero.

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
Exactly the dimension conversion and union in [C_F0194_v5](../claims/Yin_C_F0194_v5.md#symmetric-floor-guard), with law-dependent fixed factors absorbed, give an event of complement at most C_B0 N^(-B0-2) on which every sym B_j has least singular value at least N^(-L).
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

<a id="complex-matching-interface"></a>
## The full complex border has a different matching coefficient

In a full-row determinant exposure the quadratic part is -z^*Az/N, rather than -x^T(sym A)x/N.
Use exact two-copy conditioning to write each raw complex coordinate z_j=a_j+b_j epsilon_j with independent fair signs after conditioning on its two samples.
For j<k its sign-product coefficient, before the overall -1/N, is
\[
 \bar b_j A_{jk}b_k+\bar b_k A_{kj}b_j.
 \tag{Complex-sign-coefficient}
\]
The two-copy identity is exact for arbitrary complex laws, and the conditional Rademacher theorem remains a valid theorem about these coefficients.
However their large-matching graph is not controlled in general by the unweighted entries of sym A.
For a phase-line law xi=c eta, |c|=1 and eta real, the raw quadratic matrix is Z^*AZ with Z diagonal having entries c or bar c according to the row orientation.
Its symmetric part, rather than sym A, supplies the sign-product coefficients after scalar two-copy factors.
Thus the preceding unweighted low-matching result alone does not furnish the dichotomy in the real-input main theorem.
A probability estimate for the correctly weighted or sample-dependent coefficient graph remains a separate obligation.

<a id="inverse-count-interface"></a>
## The accepted inverse-counting input has a separate real-scalar boundary

The inspected [Ngu12a conventions](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) and [edition-specific source notes](../audits/literature/Ngu12a/readme.md) concern real scalar random variables with vector-valued coefficients.
Their coefficient dimension two permits complex coefficients multiplying a real scalar; it does not replace the scalar random variable by a complex entry with dependent components.
The original Condition 1 and Theorem 1.3 were already inspected at PDF pp. 2--3 of the retained arXiv v1, and the quadratic theorem at p. 5.
This preparation reuses that exact accepted scope and makes no new claim about their original proofs or a different edition.

At a fixed deterministic coefficient vector, ordinary upper-row exposure still works for a complex Hermitian matrix: every newly exposed strict upper entry has law xi, while lower entries already exposed enter the center.
The difficulty is the structural inverse theorem and the subsequent permutations in the [full profile count](../claims/Yin_C_F0194_v1.md#structured-vector-counting).
For a general complex law there is no declared accepted input here converting large concentration of sum u_j xi_j into the same bounded-rank rational progression description.
Moreover a candidate-dependent reservoir permutation changes some upper entries from xi to conjugate xi.
Unless the law is conjugation invariant, it does not preserve the identical scalar law used to define the common monotone tail concentrations and to rerun the post-permutation profile count.
Even when the law is conjugation invariant, the real-scalar inverse-theorem boundary still has to be addressed.

The exact two-copy representation of a complex xi by a fair real sign is valid after freezing two complex samples.
It then gives random complex coefficients depending on those frozen samples, not the fixed coefficient structure used by the accepted count.
No conditional progression entropy bound or uniform orientation-aware profile argument has been established by that representation alone.
Consequently the [one-omitted-row kernel estimate](../claims/Yin_C_F0194_v5.md#one-row-kernel-ac), the isolated-minor branch and the matching branch cannot be cited unchanged for arbitrary complex laws.
The real-input Claim remains at its exact accepted scope.

<a id="comparison-and-return"></a>
## Consequence for the next bounded route

The [earlier real commutator obstruction](../ledger/Yin_L_F0061_v1.md#real-affine-obstruction) creates a skew-symmetric polynomial or affine pencil from real symmetric inputs.
The present odd-size obstruction already occurs in one complex Hermitian Wigner matrix, with scalar polynomial P(x)=x and shift zero.
The algebraic parity mechanism is the same, but the input class and the purported intermediate floor being tested are different.
Neither obstruction refutes the original dimension-limsup contract.

An admissible next objective is control on even dimensions or an adequate deterministic subsequence for the pure-imaginary law, or a direct determinant-limsup estimate retaining the forced zero modes.
For laws with positive real-part variance the unconditional symmetric-part marginal and the complex projection estimate survive.
The majority-orientation lemma and central-strip exclusion partially repair the internal-row map, but the correct weighted matching graph and scalar inverse-counting gaps above remain explicit.
No all-law complex least-value theorem, Task completion, or extension of the reviewed real proof is claimed here.
