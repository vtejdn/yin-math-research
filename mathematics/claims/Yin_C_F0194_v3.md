---
author: Yin
---

# Many-index cofactor averaging and finite-radius matching for real Wigner shifts

This version develops a new many-index reduction for the same nonsymmetric-shift cofactor problem as [C_F0194_v1](Yin_C_F0194_v1.md#statement).
The [reviewed corank-tail theorem](Yin_C_F0194_v2.md#statement) supplies a separate lower-rank exception in the polynomial-shift consequence below.
Both earlier physical versions retain their complete mathematics and actual review scopes.
The [independent complete averaging and matching review](../audits/reviews/Yin_R_F0200_v3.md#finding) supports this version's exact probability deductions and input interfaces.
The present conditional matching theorem does not assert that large matchings are typical in the actual minors, a polynomial least-singular-value floor, or completion of the original [matrix](../tasks/Yin_T_F0013_v1.md#contract), [scalar](../tasks/Yin_T_F0014_v1.md#contract), or [Brown-measure](../tasks/Yin_T_F0012_v3.md#contract) objectives.

<a id="statement"></a>
## Exact model, many-index theorem and matching reduction

Fix a real law xi with E xi=0 and E xi^2=1.
For each n, let W_n be real symmetric, with strict upper entries independent copies of xi/sqrt(n), mirrored lower entries, and independent real diagonal entries independent of the off-diagonal family.
The diagonal laws in this first assertion may be arbitrary and may vary with n.
Let F be an arbitrary deterministic complex n-by-n matrix, with no symmetry or norm restriction, and put M=W_n+F.
All matrix and vector norms without a subscript are operator and Euclidean norms respectively; ||.||_F is the unnormalized Frobenius norm.
Rank is over C, determinants are ordinary, and sym A=(A+A^T)/2 uses transpose.
For each i let D_i be the principal minor obtained by deleting row and column i, and put
\[
 A_i=\operatorname{adj}D_i,\qquad Q_i=\operatorname{sym}A_i.
\]
The nonzero-adjugate condition below is essential; no determinant ratio or matching graph is assigned to an A_i that is zero.

There are constants delta in (0,1/4), a,c,C_0,C_1,c_*>0 and n_0, depending only on xi, with the following properties.
For every K>=0 and every sufficiently large n, uniformly over deterministic F, there is a measurable event R_n(F) with
\[
 \mathbb P(R_n(F)^c)\le C_0e^{-cn}.
 \tag{Rectangle-probability}
\]
On R_n(F), every unit vector v satisfying
\[
 \|M\|\le n^K,\qquad \|Mv\|\le a/(4\sqrt n)
\]
has more than floor(delta n) coordinates satisfying
\[
 |v_i|>(a/8)n^{-K-1}.
 \tag{Coarse-spread}
\]
Here the lower bound on n may depend on K; no constant depends on the diagonal law or on F.
In particular, on R_n(F), if ||M||<=n^K, rank M>=n-1 and sigma=s_min(M)<=a/(4sqrt(n)), at least delta n/2 indices satisfy
\[
 A_i\ne0,\qquad
 \frac{|\det M|}{\|A_i\|_F}\le C_1n^{2K+1}\sigma.
 \tag{Many-indices}
\]
This includes the exactly corank-one case, where the displayed ratios are zero.

For 0<=epsilon<=a/(4sqrt(n)), define
\[
 E_n(K,\varepsilon)
 =\{\|M\|\le n^K,\ \operatorname{rank}M\ge n-1,
                         \ s_{\min}(M)\le\varepsilon\},
\]
and
\[
 G_i(K,\varepsilon)
 =\left\{A_i\ne0,\quad
       |\det M|/\|A_i\|_F\le C_1n^{2K+1}\varepsilon\right\}.
\]
Then the exact averaging consequence is
\[
 \mathbb P(E_n(K,\varepsilon))
 \le C_0e^{-cn}+\frac{2}{\delta n}
                         \sum_{i=1}^n\mathbb P(G_i(K,\varepsilon)).
 \tag{Average}
\]
This average requires no independence among principal-minor events.

For h>0 and an integer 2<=r<=floor((n-1)/2), let H_i(h,r) be the event that A_i is nonzero and the graph on [n] minus {i}, with edges jk for j different from k satisfying
\[
 |(Q_i)_{jk}|\ge h\|A_i\|_F,
 \tag{Graph-threshold}
\]
has a matching of at least r edges.
A matching means a set of edges with pairwise disjoint vertex sets.
Put
\[
 \psi(r)=e^{-c_*r}+\sqrt{\log(2+r)}\,r^{-1/9}.
\]
There are xi-dependent constants c_*,C_2>0, enlarged or decreased consistently in this definition, such that whenever
\[
 C_1n^{2K+1}\varepsilon\le c_*h/n,
 \tag{Scale-match}
\]
one has
\[
 \mathbb P(E_n(K,\varepsilon))
 \le C_0e^{-cn}+C_2\left[
        \psi(r)+\frac1n\sum_{i=1}^n\mathbb P(H_i(h,r)^c)\right].
 \tag{Matching-average}
\]
The factor 1/n in (Scale-match) is required by the normalized off-diagonal entries.
A second guarded consequence is that the event E_n together with at least (1-delta/4)n indices satisfying H_i has probability at most C_0 exp(-cn)+C_2 psi(r).
No typicality of that many-matching guard is part of this assertion.
All constants remain uniform conditionally on an independent random F in this dimension, and the displayed probability statements hold after integrating over its law.

<a id="polynomial-shift-consequence"></a>
## Finite-second-moment polynomial shifts

Assume additionally that the diagonal entries of W_n are independent copies of zeta/sqrt(n), where the fixed real law zeta has finite second moment and need not be centered.
For every gamma,B>0 there exists K>0, depending only on gamma,B and the laws, such that the following consequence holds.
Let F_n be independent of W_n, and let
\[
 \Gamma_n=\{\max_{i,j}|(F_n)_{ij}|\le n^\gamma\}.
\]
For every fixed H>=0, choose A>H+2K+2.
For every deterministic integer sequence r_n satisfying 2<=r_n<=floor((n-1)/2), the normalized matrices M_n=W_n+F_n satisfy, for all sufficiently large n,
\[
 \begin{split}
 \mathbb P\{s_{\min}(M_n)\le n^{-A}\}
 \le{}& C_Bn^{-B}+\mathbb P(\Gamma_n^c)+C_2\psi(r_n)\\
 &+\frac{C_2}{n}\sum_{i=1}^n
   \mathbb P\{H_i(n^{-H},r_n)^c\cap\Gamma_n\}.
 \end{split}
 \tag{Polynomial-shift-reduction}
\]
Constants and the sufficiently large n may depend on the fixed laws, gamma,B,H,A, but not on the distribution or realization of the independent shift.
The mean low-matching probability in this bound is retained as an unproved quantity for the original product-inverse shift.
If r_n tends to infinity and that mean and P(Gamma_n^c) tend to zero, the displayed probability tends to zero; no summability follows solely from these assumptions.
No independence between physical sizes is needed for any marginal estimate here.

## Exact inputs and proof scope

The [accepted bounded-product convex concentration input and projection proof](Yin_C_F0187_v2.md#argument) supply the source theorem used in the fixed-cutoff distance argument below.
Only that input is reused; the required exp(-cn) distance estimate is derived here with a fixed cutoff, rather than inferred from the earlier moving-cutoff exp(-c n^(1/4)) estimate.
The elementary negative-second-moment identity is justified by the same Gram inverse calculation recorded in that fixed proof.

[MNV16-U001](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) supplies only Definition 1.5 and Theorem 1.6 of the 2016 Theory of Computing edition, equation (1.1) on PDF p. 2 and the theorem on PDF p. 3.
The coefficients are real, the variables are independent fair signs, degree two gives exponent 1/9 in the first bound, and the allowed interval has length one with arbitrary center.
The original proof in Section 3 and its external dependencies are accepted without a new full-proof audit.
The exact real-law two-copy representation and the complex projection are project deductions supplied in full below, not additional source conclusions.

The [reviewed rank-tail theorem C_F0194_v2](Yin_C_F0194_v2.md#decision-corank-tail-reviewed) is used only to remove corank at least two on the polynomial-shift guard in (Polynomial-shift-reduction).
Its raw-to-normalized substitution is checked below.
It is not needed for (Coarse-spread), (Many-indices), (Average), or (Matching-average), which retain their explicit rank-at-least-n-1 event.
No independent review of the present new argument is inherited from those fixed inputs.

<a id="argument"></a>
## Complete averaging and matching proof

<a id="row-adjugate"></a>
### Deterministic row-adjugate inequality

Let M be any complex n-by-n matrix with n>=2, and place index i first by the same row and column permutation.
Write
\[
 M=\begin{pmatrix}a&b\\c&D_i\end{pmatrix}.
\]
Cofactor expansion gives
\[
 \operatorname{row}_i(\operatorname{adj}M)
       =[\det D_i,\,-b\operatorname{adj}D_i].
 \tag{Adj-row}
\]
It follows first from the Schur inverse where both inverses exist and then for every matrix by polynomial continuity.
Also D_i adj D_i=(det D_i)I gives
\[
 \sqrt{n-1}|\det D_i|
       \le\|D_i\|\|\operatorname{adj}D_i\|_F.
\]
The row b and the principal compression D_i have norms at most ||M||, so
\[
 \|\operatorname{row}_i(\operatorname{adj}M)\|_2
 \le\sqrt{1+1/(n-1)}\|M\|\|A_i\|_F
 \le\sqrt2\|M\|\|A_i\|_F.
 \tag{Row-adj}
\]

If M is invertible, let sigma=s_min(M) and choose a unit right singular vector v for sigma.
For R=M^(-1), the spectral decomposition of RR* shows
\[
 \|\operatorname{row}_iR\|_2\ge |v_i|/\sigma,
\]
because the nonnegative term corresponding to v in its diagonal is |v_i|^2/sigma^2.
Using adj M=(det M)R in (Row-adj) gives, at every i with v_i nonzero,
\[
 A_i\ne0,\qquad |\det M|/\|A_i\|_F
                   \le\sqrt2\|M\|\sigma/|v_i|.
 \tag{Usable-index}
\]
This uses only the right singular vector and does not require a singular-value gap or overlap of left and right coordinate supports.
If M has exactly corank one, adj M=eta v u* for unit right and left kernel vectors and a nonzero scalar eta.
For every v_i nonzero, the row norm in (Row-adj) is |eta||v_i|>0, so A_i is nonzero and its determinant ratio is zero.
When the full corank is at least two, adj M=0 and this deterministic proof supplies no such conclusion.

<a id="linear-codimension"></a>
### Fixed-cutoff distance estimate

Let x have p independent coordinates with the fixed law xi.
Uniformly over complex linear subspaces V of C^p with complex codimension at least p/2 and arbitrary deterministic f in C^p, we prove
\[
 \mathbb P\{\operatorname{dist}(x+f,V)\le c\sqrt p\}
                    \le Ce^{-cp}
 \tag{Distance}
\]
for all sufficiently large p.

Fix R>=1 such that P(|xi|>R)<=1/64 and the conditional variance v_R of xi given |xi|<=R is at least 1/2.
The finite second moment ensures such a fixed R exists.
Write mu_R for that conditional mean and G={j:|x_j|<=R}.
Independence and exponential Markov at parameter one give
\[
 \begin{split}
 \mathbb P\{|G^c|>p/8\}
 &\le e^{-p/8}(1+(e-1)/64)^p\\
 &\le e^{-c_3p}.
 \end{split}
\]
Conditional on G, its retained coordinates remain independent with the fixed bounded conditional law.
Project V onto C^G and enlarge the projected space by the single vector f_G+mu_R 1, obtaining V_G'.
When |G^c|<=p/8, its complex codimension is at least p/2-p/8-1>=p/4 for large p.
The coordinate projection is a contraction and that enlargement absorbs the deterministic mean and shift, so
\[
 \operatorname{dist}(x+f,V)
 \ge\operatorname{dist}(x_G-\mu_R\mathbf1,V_G').
\]
Let P_G be the complex orthogonal projection onto the complement of V_G', and put Y=||P_G(x_G-mu_R 1)||.
Centered independent real coordinates give
\[
 \mathbb E(Y^2\mid G)=v_R\operatorname{Tr}P_G\ge p/8.
\]
This identity remains valid for the complex projection because E y_j y_k=v_R delta_jk for the real centered variables.
The distance Y is convex and one-Lipschitz in the independent real coordinate variables, whose support diameters are at most 2R.
The accepted bounded-product concentration inequality therefore gives
\[
 \mathbb P\{|Y-\operatorname{med}(Y)|\ge t\mid G\}
                     \le C_3e^{-c_4t^2/R^2}.
\]
Integrating this inequality yields E((Y-med(Y))^2|G)<=C_4 R^2.
The L^2 triangle inequality implies med(Y)>=sqrt(p/8)-sqrt(C_4)R, which is at least c_5 sqrt(p) for large p.
A second use of concentration bounds P(Y<=c_5 sqrt(p)/2|G) by C exp(-c_6p/R^2).
The cutoff R is fixed, so this and the bad-coordinate estimate prove (Distance), with constants independent of V,f and the specified good set.

<a id="rectangles"></a>
### All small-support rectangular blocks

Fix for the moment any delta<=1/4, put k=floor(delta n), and choose J subset of [n] with |J|=k and I its complement.
For B=sqrt(n) M[I,J], the k columns are independent: every random coordinate is an off-diagonal entry crossing the disjoint sets I and J, so mirrored partners do not occur elsewhere in this rectangle.
Each column has p=n-k independent xi coordinates plus a deterministic complex shift.
Conditional on the other columns, their span has complex codimension at least n-2k+1>=p/2.
Apply (Distance) to each column.
Except with probability Cn exp(-c_7n), all its column distances from the span of the other columns are at least c_8 sqrt(n).
All constants in this assertion are uniform over delta<=1/4 and over F.

On this event B has full column rank.
For its Gram matrix B*B, the j-th diagonal entry of its inverse equals the reciprocal squared distance of column j from the span of the others, by the scalar Schur complement.
Taking the trace gives the negative-second-moment identity
\[
 \sum_{j=1}^k s_j(B)^{-2}
 =\sum_{j=1}^k\operatorname{dist}(B_j,\operatorname{span}\{B_l:l\ne j\})^{-2}
 \le Ck/n.
\]
Consequently s_min(B)>=c sqrt(n/k), and
\[
 s_{\min}(M[I,J])\ge c/\sqrt k\ge c/\sqrt n.
 \tag{Rectangular-floor}
\]
Now choose delta>0 so small that delta log(e/delta)<c_7/4.
For large n there are at most exp(2delta n log(e/delta)) possible supports J.
A union over them preserves an exp(-cn) failure probability.
Let R_n(F) be the event that (Rectangular-floor) holds for all such J, and let a>0 be its constant c, decreased if necessary.
This proves (Rectangle-probability) and defines a measurable event, since only finitely many singular-value conditions occur.

<a id="spread-and-average"></a>
### Coarse spread, principal cofactors and averaging

Fix K>=0 and the norm event ||M||<=n^K.
Put rho_n=(a/8)n^(-K-1/2) and t_n=(a/8)n^(-K-1).
If a unit vector v with ||Mv||<=a/(4sqrt(n)) had ||v_I||<=rho_n for some |J|=k, then ||v_J||>=1/2 for large n and
\[
 \|(Mv)_I\|
 \ge\|M[I,J]v_J\|-\|M[I,I]v_I\|
 \ge\frac a{2\sqrt n}-n^K\rho_n
 =\frac{3a}{8\sqrt n},
\]
contradicting its residual bound.
If at most k coordinates exceeded t_n in modulus, choose J to contain them; then ||v_I||<=sqrt(n)t_n=rho_n, again a contradiction.
This proves (Coarse-spread).

For invertible M, apply it to a right least-singular vector and use (Usable-index).
For exactly corank-one M, apply it to a unit right kernel vector and use the exact singular argument after (Usable-index).
In either case at least delta n/2 indices satisfy (Many-indices), with C_1=8sqrt(2)/a or a larger fixed constant.
It follows pointwise, outside R_n(F)^c, that
\[
 \mathbf1_{E_n(K,\varepsilon)}
 \le\frac{2}{\delta n}\sum_{i=1}^n\mathbf1_{G_i(K,\varepsilon)}.
\]
Expectation proves (Average).
No union over the n possible omitted indices is taken.

<a id="two-copy-matching"></a>
### Complete finite-radius matching estimate

Fix one i and condition on the actual principal minor D_i and on the exposed diagonal entry a of M.
They are independent of the remaining real off-diagonal row coordinates.
After placing i first, write those coordinates as x/sqrt(n), where x has independent entries with law xi, and let f,g be the deterministic, possibly different, complex row and column shifts.
For A=adj D_i and Q=sym A, the exact bordered determinant identity gives
\[
 \det M=a\det D_i-(x/\sqrt n+f)^T A(x/\sqrt n+g).
 \tag{Border-det}
\]
It follows by the Schur complement when D_i is invertible and then by polynomial continuity.
Its quadratic part in the raw coordinates x is -x^TQx/n.
Its linear and constant terms, including a det D_i, are unrestricted.

Assume A is nonzero and the graph (Graph-threshold) contains a matching of r edges.
Choose its first such matching in a fixed lexicographic order, so the choice is measurable in D_i.
For each edge, at least one of |Re Q_jk| and |Im Q_jk| is at least |Q_jk|/sqrt(2).
At least half the edges therefore share one common projection pi, equal either to real part or to imaginary part, at that scale.
Retain those edges and choose that projection by the same fixed tie-breaking rule.

For each raw coordinate, take independent copies xi_j^(0),xi_j^(1) of xi and an independent fair sign epsilon_j, with all these families independent, and write
\[
 c_j=(\xi_j^{(0)}+\xi_j^{(1)})/2,
 \qquad b_j=(\xi_j^{(0)}-\xi_j^{(1)})/2,
 \qquad x_j=c_j+b_j\varepsilon_j.
\]
This gives exactly the original independent-coordinate law of x, because each coordinate selects one of its two independent copies with probability one half.
Since xi is nondegenerate, some b_0,p_0>0 satisfy P(|b_j|>=b_0)>=p_0.
For the retained disjoint matching, the events that both endpoint b-values have modulus at least b_0 are independent and have probability at least p_0^2.
An elementary exponential Markov estimate for independent indicators gives a matching of at least c_9 r surviving edges except with probability at most C exp(-c_9 r), for all sufficiently large r.
For example, compare the indicator sum with a binomial random variable of parameter p_0^2, and apply Markov to exp(-t times that sum) with any sufficiently small fixed t>0.
The finitely many smaller r are absorbed by enlarging C in the eventual bound.

Conditional on all the two-copy values, pi(det M) is a real polynomial of the fair signs.
Because epsilon_j^2=1, every diagonal quadratic term becomes affine in epsilon_j, leaving a multilinear polynomial of degree at most two.
For each surviving edge its quadratic monomial coefficient has modulus at least
\[
 \lambda=\sqrt2\,b_0^2h\|A\|_F/n.
\]
This retains both the factor two in the coefficient of x_j x_k in x^TQx and the factor 1/n from normalized Wigner entries.
There are at least c_9 r disjoint such monomials.
Choose c_*>0 small enough, depending only on b_0, that the event
\[
 |\det M|\le c_*h\|A\|_F/n
\]
places pi(det M)/lambda in an interval of length strictly smaller than one.
Apply the exact MNV16 Theorem 1.6 at degree two, padding that interval to length one.
Its rank is at least c_9 r after scaling, and all lower-degree coefficients and its center are allowed.
After integrating the two-copy variables, we obtain, uniformly over D_i,a,f,g,
\[
 \mathbb P\left\{
    |\det M|/\|A_i\|_F\le c_*h/n
       \ \middle|\ D_i,a\right\}
 \le C\left[e^{-c_*r}+\sqrt{\log(2+r)}\,r^{-1/9}\right]
 \tag{Matching-row}
\]
on H_i(h,r).
The constants in c_* can be decreased to make the exponential and radius conventions agree.
This is an estimate for the original row law because the two-copy representation preserves that law exactly.
No moment beyond nondegeneracy is used by this conditional step.

If (Scale-match) holds, conditioning on D_i,a gives
\[
 \mathbb P(G_i(K,\varepsilon)\cap H_i(h,r))\le C\psi(r).
\]
Split each G_i into that part and its complement in H_i, then apply (Average).
This proves (Matching-average).
If at least (1-delta/4)n events H_i hold, (Many-indices) instead forces at least delta n/4 indices to satisfy G_i and H_i simultaneously.
The same averaging with factor 4/(delta n) proves the stated guarded alternative.
For an independent random F, condition on its realization within the dimension and integrate these uniform estimates; no complete cross-dimensional shift sequence is conditioned on.

<a id="polynomial-shift-proof"></a>
### Norm and corank exceptions at polynomial shifts

Fix gamma,B>0 and first restrict to Gamma_n.
Choose a raw cutoff exponent kappa>(B+2)/2.
The finite second moments and a union bound show that the probability any of the O(n^2) raw Wigner variables exceeds n^kappa in modulus is at most Cn^(2-2kappa)<=C_B n^(-B), after enlarging constants.
On the complementary event,
\[
 \|W_n\|\le n^{\kappa+1/2},\qquad
 \|F_n\|\le n^{\gamma+1}.
\]
Choose a fixed K>max{kappa+1/2,gamma+1}; then ||M_n||<=n^K for large n, outside the stated raw-entry failure probability and Gamma_n^c.
This step requires only the fixed finite second moments of xi,zeta.

Multiplying M_n by sqrt(n) does not change its rank and gives the raw Wigner matrix plus offset sqrt(n)F_n.
On Gamma_n every entry of that offset is at most n^(gamma+1/2), hence at most n^(gamma+1) for large n.
Apply the reviewed C_F0194_v2 rank-tail theorem with exponent gamma+1 and requested probability exponent B.
Conditional on the independent F_n and then integrated over Gamma_n, it gives
\[
 \mathbb P\{\operatorname{rank}M_n\le n-2,\ \Gamma_n\}
                       \le C_Bn^{-B}.
\]
Thus norm and corank exceptions in Gamma_n contribute only C_B n^(-B).

For h=n^(-H), epsilon=n^(-A), and A>H+2K+2, the power inequality in (Scale-match) holds for all sufficiently large n, including its fixed constants.
Also epsilon<=a/(4sqrt(n)).
Apply (Matching-average) conditional on F_n and integrate its inequality only over Gamma_n.
The exceptional low-matching term becomes the mean of P(H_i^c intersect Gamma_n).
Adding the norm, rank and shift-guard exceptions proves (Polynomial-shift-reduction).
The conclusion retains the low-matching probability and its exact normalization instead of treating it as a proved input.

## Scope and remaining question

The new argument replaces the lost union over all principal indices by an average, using genuine randomness of the rectangular off-diagonal blocks.
The actual remaining probability obligation is to control the mean low-matching term, or to handle its diagonal-plus-few-rows-and-columns complement by another mechanism.
This version does not claim that that obligation is necessary for every possible proof of the original Tasks.
No assertion for genuinely complex off-diagonal laws or for arbitrary matrix-coefficient pencils is included.


## Current assessment
[Selected decision](#decision-many-index-reviewed)

## Assessment history

### Decision many-index-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T10:23 |
| status | open |
| reason | The complete many-index cofactor, finite-radius matching and polynomial-shift probability reductions are fixed as a candidate for fresh mathematical review; the mean probability of low-matching actual minors remains explicit and no least-singular-value floor or original Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact many-index and matching assertions](#statement) | Normalized real finite-second-moment off-diagonal Wigner entries, arbitrary independent diagonal laws for the norm-guarded core, arbitrary deterministic complex shifts, independent random shifts, principal-cofactor averaging, and the finite-second-moment polynomial-shift consequence with its retained mean low-matching probability. |
| argument | [Complete candidate proof](#argument) | Deterministic row-adjugate inequality, fixed-cutoff exponential projection estimate, all-small-support rectangular event, coarse right-vector spread, averaging, complete exact two-copy finite-radius matching argument, normalization, norm guard and corank exceptions. |
| dependency | [Accepted projection input](Yin_C_F0187_v2.md#argument) | Only the bounded-product convex concentration input and the elementary Gram-inverse negative-second-moment identity; the stronger fixed-cutoff distance estimate and rectangular union are proved in this argument. |
| dependency | [Exact MNV16 input](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) | Definition 1.5 and Theorem 1.6 of the actual 2016 Theory of Computing publication, at degree two for real multilinear fair-sign polynomials and length-one intervals; source proof accepted without a new full audit. |
| dependency | [Reviewed corank tail](Yin_C_F0194_v2.md#decision-corank-tail-reviewed) | Only the raw real finite-second-moment polynomial-shift corank-at-least-two probability bound, used after the explicit normalized-to-raw substitution to remove the full corank exception in the polynomial-shift consequence. |

### Decision many-index-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T10:30 |
| status | proved |
| reason | Independent whole-proof review checked all many-index, finite-radius matching and polynomial-shift probability reductions and their exact direct inputs without a mathematical gap; the mean low-matching probability remains an explicit uncontrolled term, not an asserted floor or Task resolution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact many-index and matching assertions](#statement) | Normalized real finite-second-moment off-diagonal Wigner entries, arbitrary independent diagonal laws for the norm-guarded core, arbitrary deterministic complex shifts, independent random shifts, principal-cofactor averaging, and the finite-second-moment polynomial-shift consequence with its retained mean low-matching probability. |
| argument | [Complete candidate proof](#argument) | Deterministic row-adjugate inequality, fixed-cutoff exponential projection estimate, all-small-support rectangular event, coarse right-vector spread, averaging, complete exact two-copy finite-radius matching argument, normalization, norm guard and corank exceptions. |
| dependency | [Accepted projection input](Yin_C_F0187_v2.md#argument) | Only the bounded-product convex concentration input and the elementary Gram-inverse negative-second-moment identity; the stronger fixed-cutoff distance estimate and rectangular union are proved in this argument. |
| dependency | [Exact MNV16 input](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) | Definition 1.5 and Theorem 1.6 of the actual 2016 Theory of Computing publication, at degree two for real multilinear fair-sign polynomials and length-one intervals; source proof accepted without a new full audit. |
| dependency | [Reviewed corank tail](Yin_C_F0194_v2.md#decision-corank-tail-reviewed) | Only the raw real finite-second-moment polynomial-shift corank-at-least-two probability bound, used after the explicit normalized-to-raw substitution to remove the full corank exception in the polynomial-shift consequence. |
| review | [Independent complete averaging and matching finding](../audits/reviews/Yin_R_F0200_v3.md#finding) | Entire exact statement, argument, three declared dependencies, singular and conditional cases, normalized matching coefficient and the polynomial-shift bound with its retained low-matching term. |
