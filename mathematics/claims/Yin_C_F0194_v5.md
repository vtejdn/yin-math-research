---
author: Yin
---

# Polynomial second-value floors and in-probability invertibility for real Wigner shifts

This version combines internal-row cofactor exposure, an omitted-row kernel estimate, and the existing many-index matching argument for a real Wigner matrix plus an arbitrary complex nonsymmetric shift.
The earlier fixed versions retain their complete mathematics and actual review scopes.
The unary estimates of C_F0194_v4 are not proof inputs here.
The result is a project deduction without a novelty or priority claim.
Its [independent whole-proof review](../audits/reviews/Yin_R_F0200_v5.md#finding) covers the complete new argument and its declared input interfaces.

<a id="statement"></a>
## Exact main statement and subsidiary assertions

Fix real laws xi,zeta with E xi=0, E xi^2=1, and E|zeta|^2 finite.
For every N, let X_N be real symmetric, with independent strict upper entries having law xi, independent diagonal entries having law zeta, these two families independent, and mirrored lower entries.
Put W_N=X_N/sqrt(N).
For every gamma,B>0 there are fixed A,C_B,C,N_0, depending only on the laws,gamma,B, such that
\[
 \sup_{\max_{ij}|F_{ij}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}\,N^{-1/18},
 \qquad N\ge N_0.
 \tag{Candidate-floor}
\]
The supremum is over deterministic complex shifts with no symmetry condition, and the shift may vary with N.
For an independent random F_N the same bound holds on its polynomial entry guard; the probability of the complementary guard is added for the unguarded event.
The estimate requires neither a density nor a moment above two.
Its displayed high-matching term tends to zero and is not claimed summable over all sizes.
No independence between physical sizes is needed for this marginal estimate.

This statement also includes the following subsidiary assertions at their full displayed hypotheses and normalizations.

- The [uncovered-diagonal exclusion](#bulk-diagonal-statement) for actual minors with m in [N/2,N], a cover of size less than 2r_N with r_N log(N)=o(N), and a fine threshold selected after the shift, norm and symmetric-floor exponents.
- The [hub and adjugate approximation](#few-hub-consequence) and [small minor determinant ratio and singular value](#small-determinant-minor), with their explicit symmetric-part and norm guards.
- The [one-omitted-row kernel anti-concentration](#one-row-kernel-ac), followed by [raw and normalized polynomial second-smallest floors](#second-smallest-floor) outside arbitrary polynomial failure probabilities.
- The [complete parameter-ordered assembly](#in-probability-floor) of the main bound from the fixed isolated-minor and matching inputs.

No almost-sure full-sequence least-value floor, summability of the displayed main error, general matrix-coefficient pencil theorem or Brown-measure conclusion is part of this statement.

<a id="bulk-diagonal-statement"></a>
## Actual-minor exclusion of a large uncovered diagonal

Fix a centered variance-one real off-diagonal law xi and a real diagonal law zeta with finite second moment.
For every original size N, let m be an integer in [N/2,N] and let D be an m-by-m real Wigner matrix normalized by sqrt(N), plus a deterministic complex shift F.
The raw upper off-diagonal entries have the fixed law xi, the raw diagonal entries have the fixed law zeta, all upper entries are independent, and lower off-diagonal entries mirror the upper ones.
Assume max|F_ab|<=N^gamma for a fixed gamma>0, without any symmetry condition on F.
Write
\[
 A=\operatorname{adj}D,\qquad Q=\operatorname{sym}A,
 \qquad \operatorname{sym}Z=(Z+Z^T)/2.
\]
The larger size N is retained in every normalization and power threshold.
Thus the statement applies directly to an actual principal minor of size N-1 and to its internal minors of size N-2, without changing its input law.

Fix B>0 and K>=0.
There is a finite exponent L>0, depending only on xi,zeta,gamma,B, such that the following assertion holds for every fixed J>=0 and every fixed
\[
 H>J+L+2K+1.
 \tag{Fine-threshold}
\]
Let r_N>=2 be a deterministic integer sequence with r_N log(N)=o(N).
For all sufficiently large N, the probability is at most C_B N^(-B)+C exp(-cN) that there exist a set I subset of [m] with |I|<2r_N and an index j outside I satisfying all of
\[
 \begin{split}
 &A\ne0,\qquad \|D\|\le N^K,\\
 &|Q_{ab}|<N^{-H}\|A\|_F
       \quad(a\ne b,\ a,b\notin I),\\
 &|Q_{jj}|\ge N^{-J}\|A\|_F.
 \end{split}
 \tag{Large-uncovered-diagonal}
\]
The constants and the sufficiently large N are uniform over m in [N/2,N] and over deterministic shifts in the displayed bound.
The sufficiently large N may depend on J,H,K and on the deterministic sequence r_N.
In particular r_N can tend to infinity as slowly as desired, for example logarithmically.
The exponent L is selected before J,H, so this does not require a threshold H chosen independently of the allowed shift scale.

For every low-matching graph, the endpoints of a maximal matching form such a cover I.
Consequently, except with the displayed probability, low matching at the fine threshold forces every diagonal outside any such cover to be smaller than N^(-J)||A||_F.
This is an actual random-minor statement and applies to Rademacher laws as well as laws with three or more support points.
It does not rely on oscillation of the exposed full-matrix row's unary diagonal terms.

<a id="argument"></a>
## Complete nonsymmetric-shift argument and exact fixed inputs

The [reviewed C_F0188_v2 symmetric-shift floor](Yin_C_F0188_v2.md#statement) is applied only to sym B, where B is an internal principal minor of D.
The random part of sym B is still the real Wigner input, and its deterministic shift is genuinely complex symmetric.
It is not used as a floor for B or D with a nonsymmetric shift.
The raw-to-normalized exponents and union over actual internal minors are checked below.

The [fixed linear-codimension distance proof](Yin_C_F0194_v3.md#linear-codimension) supplies an exp(-cp) bound for independent real coordinates near any fixed complex affine subspace with complex codimension at least p/2.
Its constants are uniform over the subspace and center and require only the fixed centered variance-one law xi.
This is the exact accepted input used after internal-row exposure.
The algebraic row identities and singular-value deletion argument are supplied below.
No independence of adaptive covers, randomly selected coefficient vectors, or different minor events is assumed.

The new probability, matrix approximation and second-value arguments are supplied completely below and covered by the independent review.
No unconditional high-matching assertion is used.

<a id="symmetric-floor-guard"></a>
## A simultaneous symmetric-part guard for internal minors

For each j let B_j be D with row and column j deleted, of dimension d=m-1.
For N sufficiently large, d lies between N/3 and N.
The raw matrix sqrt(N) sym B_j is a raw real Wigner matrix with off-diagonal law xi, diagonal law zeta, and deterministic complex symmetric shift sqrt(N) sym F_j.
Every shift entry has modulus at most N^(gamma+1/2), which is at most d^(gamma+2) for all sufficiently large N uniformly over these dimensions.
Apply C_F0188_v2 with shift exponent gamma+2 and failure exponent B+3.
For some fixed a_s>0 it gives
\[
 \mathbb P\{s_{\min}(\operatorname{sym}B_j)
          \le d^{-a_s}/\sqrt N\}
 \le C d^{-B-3}.
\]
Since d<=N, one has d^(-a_s)/sqrt(N)>=N^(-a_s-1/2).
Choose L>a_s+1/2, for example L=a_s+1.
A union over the at most N choices of j gives a measurable event Omega_s with
\[
 \mathbb P(\Omega_s^c)\le C_BN^{-B-2},
 \qquad
 s_{\min}(\operatorname{sym}B_j)\ge N^{-L}
       \quad\text{for every }j\text{ on }\Omega_s.
 \tag{Internal-symmetric-floor}
\]
The extra margin in the probability exponent permits an additional union over N outer principal minors if a simultaneous statement in one full N-by-N Wigner matrix is desired.
For the present one-minor statement only the displayed internal union is used.
No norm or inverse bound for the nonsymmetric B_j was invoked.

<a id="internal-row-identity"></a>
## An internal adjugate row supplies an invertible coefficient map

Fix a deterministic candidate cover I with k=|I|<2r_N and a deterministic j outside I.
Place j first and write
\[
 D=\begin{pmatrix}a&b\\c&B\end{pmatrix},
 \qquad
 b=x^T/\sqrt N+f^T,
 \qquad c=x/\sqrt N+g,
\]
where B=B_j, the real coordinates of x have law xi and are independent of B, and f,g are the fixed, possibly different, complex offsets.
The diagonal a plays no role in the following calculation.
Polynomial cofactor expansion gives
\[
 Q_{jj}=\det B,
 \qquad
 Q_{j,[m]\setminus\{j\}}
    =-\frac12\left(b\operatorname{adj}B
                    +c^T(\operatorname{adj}B)^T\right).
 \tag{Internal-row}
\]
The formula holds for every B by polynomial continuity from the invertible Schur-complement case.

On (Large-uncovered-diagonal), det B is nonzero because A is nonzero and N^(-J)>0.
Set
\[
 U=\operatorname{sym}(B^{-1}).
\]
The exact factorization
\[
 U=B^{-T}(\operatorname{sym}B)B^{-1}
\]
and the norm guard ||B||<=||D||<=N^K imply, on Omega_s,
\[
 s_{\min}(U)\ge N^{-L-2K}=:\kappa_N.
 \tag{Coefficient-floor}
\]
Transpose does not change singular values, so the same lower bound applies to B^(-T) as to B^(-1) in this product estimate.
This calculation uses only the norm of B and the floor for its symmetric part, and no upper bound for B^(-1).

Divide (Internal-row) by the nonzero det B and use adj B=(det B)B^(-1).
Since U is symmetric, the resulting row, transposed into a column, has the form
\[
 -Q_{[m]\setminus\{j\},j}/\det B
            =Ux/\sqrt N+d_B,
 \tag{Row-linear-map}
\]
where d_B is deterministic after conditioning on B.
The constant includes both offsets f,g; its precise value is not restricted.
This equation retains the full nonsymmetric offset and uses ordinary transpose rather than Hermitian adjoint in the cofactor identities.

<a id="deleted-coefficient-map"></a>
## Deleting the cover loses only k singular directions

Let T=[m] minus (I union {j}) and p=|T|=m-k-1.
Identify U with its coordinates on [m] minus {j}, so its indices are I union T.
The p-by-p principal block U_TT has at least p-k singular values at least kappa_N.
To prove this directly, consider the subspace
\[
 V_0=\ker U_{I,T}\subseteq\mathbb C^T.
\]
Its codimension in C^T is at most k.
For every z in V_0, the extension by zero on I satisfies
\[
 \|U_{TT}z\|
 =\|U_{[m]\setminus\{j\},T}z\|
 \ge\kappa_N\|z\|.
\]
The singular-value min-max principle therefore proves the claimed count.
Since k<2r_N=o(N/log N) and m>=N/2, one has p-k>=p/2 and p>=N/3 for all sufficiently large N.

Condition now on B and on the internal row coordinates x_I.
The remaining coordinates x_T are independent with the original real law xi.
The condition that I be a graph cover is not imposed in this conditional law.
Instead, for a fixed deterministic I,j, the event (Large-uncovered-diagonal) is contained in a small-value event for the fixed affine map below.
The ratio |det B|>=N^(-J)||A||_F in (Large-uncovered-diagonal) and its small off-diagonal row give
\[
 \|U_{TT}x_T/\sqrt N+z_{B,x_I}\|
 \le\sqrt p\,N^{J-H}.
 \tag{Small-row-map}
\]
Here z_{B,x_I} absorbs d_B and U_TI x_I/sqrt(N), and is fixed under the displayed conditioning.
The row-dependent adjugate norm has disappeared by the deterministic ratio inequality; it has not been treated as an independent or conditioned coefficient.

Choose a singular-value decomposition of U_TT and retain its right singular subspace V_1 corresponding to singular values at least kappa_N.
It has complex dimension at least p-k>=p/2.
Applying the corresponding left projection and the inverse of those retained singular values to (Small-row-map), there is a fixed z_1 in V_1 for which
\[
 \|P_{V_1}x_T+z_1\|
 \le\kappa_N^{-1}\sqrt{Np}\,N^{J-H}
 \le N^{L+2K+1+J-H}.
 \tag{Affine-projection}
\]
The left side is exactly dist(x_T+z_1,V_1^perp).
Its subspace and shift depend only on the conditioned B,x_I.
One may choose the retained spectral projection measurably by functional calculus for U_TT*U_TT; a measurable pseudoinverse on that spectral subspace supplies z_1, including repeated singular values.

By (Fine-threshold), the final radius in (Affine-projection) tends to zero, and in particular is at most the accepted distance input's c sqrt(p) for large N.
That input bounds its conditional probability by C exp(-cp)<=C exp(-c'N), uniformly in B,x_I and the offsets.
The same conclusion holds on the B-measurable guards det B nonzero, ||B||<=N^K and s_min(sym B)>=N^(-L).
Integrating over B,x_I proves, for every deterministic I,j, an exp(-cN) bound on the required row event under those guards.
All global hypotheses in (Large-uncovered-diagonal) imply these guards or (Small-row-map), so no conditioning on a row-dependent good event is needed.

<a id="cover-union"></a>
## Cover union and uniformity

There are at most
\[
 N\sum_{k<2r_N}\binom mk
 \le N^{2r_N+2}
 =\exp(o(N))
\]
choices of deterministic I,j for all sufficiently large N.
The union of the conditional row bounds therefore still has probability at most C exp(-cN), after decreasing c.
Add Omega_s^c from (Internal-symmetric-floor).
This proves the claimed probability bound in (Large-uncovered-diagonal), with room in the requested N^(-B) exponent.
In particular it applies to the endpoints of a greedy maximal matching, even though that cover was originally defined from the full random Q.
The union over deterministic candidate covers, rather than conditioning on the random cover, is what preserves the row independence used above.

For an independent random F, condition on its realization within this dimension and integrate the uniform bound over the event max|F_ab|<=N^gamma.
Add the probability of the complementary shift guard when an unconditional result is desired.
The proof requires no independence between different sizes.

<a id="few-hub-consequence"></a>
## What remains after the uncovered diagonals are removed

Let Q_I be the matrix obtained from Q by retaining its entries that meet I in a row or column and setting every T-by-T entry, where T=[m] minus I, to zero.
It has rank at most 2|I|<4r_N, since it is the sum of a matrix supported on I rows and one supported on I columns.
Outside the exceptional event just proved, a low-matching graph with this cover satisfies
\[
 \frac{\|Q-Q_I\|_F}{\|A\|_F}
 \le\sqrt N\,N^{-J}+N\,N^{-H}
 =:e_N.
 \tag{Hub-approximation}
\]
The first term counts the at most N uncovered diagonal entries and the second the at most N^2 small off-diagonal entries.
This conclusion includes every law permitted in the statement, including Rademacher.

One may additionally apply the same accepted symmetric-shift floor to sym D itself.
For an exponent L_0 selected from xi,zeta,gamma and the desired failure exponent, its extra exceptional probability is O_B(N^(-B)) and
\[
 s_{\min}(\operatorname{sym}D)\ge N^{-L_0}.
\]
The exact [cofactor identity](Yin_C_F0194_v1.md#cofactor-identity)
\[
 D^TQ=(\operatorname{sym}D)A
\]
then gives a rank-at-most-2|I| matrix
\[
 A_I=(\operatorname{sym}D)^{-1}D^TQ_I
\]
with
\[
 \|A-A_I\|_F\le N^{L_0+K}e_N\|A\|_F.
 \tag{Adjugate-low-rank}
\]
For any desired fixed precision exponent P>0, choose J>L_0+K+P+1 and then H satisfying (Fine-threshold), enlarged if necessary so H>L_0+K+P+1.
The relative error in (Adjugate-low-rank) is then at most 2N^(-P) for large N.
These choices are made after the shift, norm and symmetric-floor exponents; no uniform threshold independent of those exponents is claimed.

This is an approximation consequence, not a contradiction.
If D is invertible, it says that the inverse singular directions outside the first 2|I| contribute negligibly to the inverse Frobenius norm at that chosen precision.
For exactly corank-one D the adjugate is already rank one, and the earlier isolated-minor theorem retains its separate tiny-determinant estimate.
The implication does not turn a structured row of Q into a near-kernel vector of D and does not bypass the failed inference recorded in the existing cofactor comparison.

<a id="small-determinant-minor"></a>
## The same event forces a very small minor singular value

There is a further exact consequence of the same hub approximation.
The algebraic identity
\[
 DQD^T=(\det D)\operatorname{sym}D
\]
holds for every D, including singular D, by the adjugate identities on the two summands of Q.
The matrix DQ_I D^T has rank at most q=2|I|<4r_N, which is less than m for large N.
By the singular-value min-max bound for a rank-q approximation and the symmetric-part floor,
\[
 |\det D|N^{-L_0}
 \le s_{q+1}((\det D)\operatorname{sym}D)
 \le\|D(Q-Q_I)D^T\|
 \le N^{2K}e_N\|A\|_F,
\]
where singular values are ordered decreasingly.
Therefore
\[
 \frac{|\det D|}{\|A\|_F}
             \le N^{2K+L_0}e_N.
 \tag{Small-minor-ratio}
\]
For invertible D this ratio is 1/||D^(-1)||_F, and ||D^(-1)||_F<=sqrt(m)/s_min(D) gives
\[
 s_{\min}(D)\le\sqrt m\,|\det D|/\|A\|_F
       \le N^{2K+L_0+1/2}e_N.
 \tag{Small-minor-singular-value}
\]
If D is singular, A nonzero means exactly corank one and s_min(D)=0, so the same final bound is immediate.

For any fixed desired exponent T_0>0, first choose
\[
 J>2K+L_0+T_0+1,
\]
and then enlarge H to satisfy (Fine-threshold) and H>2K+L_0+T_0+3/2.
The right side of (Small-minor-singular-value) is then at most 2N^(-T_0) for large N.
Thus, at a threshold chosen after the shift, norm, symmetric-floor and desired precision exponents, low matching forces an arbitrarily fine polynomial small-singular-value event in the actual minor, outside the displayed exceptional probabilities.
It does not yet force that smallest direction to be isolated from the second one.
The remaining spectral alternative is a cluster of small directions, rather than a well-conditioned minor.

<a id="one-row-kernel-ac"></a>
## Anti-concentration for a kernel with one omitted row

The [fixed counting class](Yin_C_F0194_v1.md#counting-class) and [complete profile count](Yin_C_F0194_v1.md#structured-vector-counting) explicitly allow at least m-C_0 prescribed row constraints.
The omitted set need not be consecutive, and its polynomial number of choices is included in the count.
In particular, equation (26) there loses at most the polynomial factor m^(D_0(C_0+1)) when those constraints are omitted, before the high-product profile cancellation.
This is a proof-scope fact from that fixed module, rather than an assertion that the statement of C_F0194_v2 already includes the rectangular conclusion below.

Work first under independent raw cutoffs at original size N, so the real scalar law is xi_N=(xi conditioned on |xi|<=N^kappa), with uniform (AC) constants for all sufficiently large N.
Take a square size-m principal block D=X+F with m in [N/2,N], all entries bounded by m^K for some fixed K, and deterministic diagonal values.
The off-diagonal family in D is independent with the one law xi_N, not a separately truncated law at size m.
The fixed count depends only on those uniform (AC) constants, its polynomial entry bound and its fixed structural exponents, so it applies uniformly to this size-comparable family.

Fix b>0 and choose the fine exponent a sufficiently large after b,K and the fixed structural constants of the accepted linear inverse theorem.
Outside a measurable event of probability at most C exp(-cm), the following holds simultaneously for every row index l and every unit u in C^m:
\[
 (Du)_j=0\quad(j\ne l)
 \quad\Longrightarrow\quad
 \sup_{z\in\mathbb C}\mathbb P\left\{
       \left|\sum_{j=1}^m u_j\xi_{N,j}-z\right|\le m^{-a}\right\}
       \le m^{-b}.
 \tag{One-row-kernel-AC}
\]
The independent copies in this small-ball probability have the law xi_N and are separate from D.

Here is the complete reduction to the exact fixed counting class.
If a unit u violating (One-row-kernel-AC) exists, the accepted dimension-two linear inverse theorem and the [fixed rounding interface](Yin_C_F0194_v1.md#inverse-rounding) give a rational progression candidate w with norm between one half and two and coordinate errors at most C m^(-a).
The progression rank, its polynomial-size bound, its exceptional O(m^epsilon) coordinates and the leading entropy constant depend on b,K and the uniform (AC) constants, but not on a.
Enlarge the fixed structural constant C_0 to exceed K+2 and one, and absorb the harmless fixed multiplier in the precision bound.
For every j except l,
\[
 |(Dw)_j|=|(D(w-u))_j|\le C m^{K+1-a}\le m^{-a+C_0}
\]
for all sufficiently large m.
Thus w lies in precisely the fixed rational candidate class and satisfies at least m-C_0 of its prescribed row constraints.
The fixed full count bounds existence of any such candidate by C exp(-cm).
Define the exceptional event to be that finite structured-candidate existence event, including the already allowed omitted-row choices.
This both proves its measurability and covers the universal quantifier over kernel vectors and omitted indices.
The original inverse-theorem and noncircular fine-precision choices are the same as in the accepted module; no new uniformity in arbitrary real coefficient arrays is assumed.
Conditioning on diagonal values is legitimate because that fixed count is uniform over deterministic diagonals in the entry bound.

<a id="second-smallest-floor"></a>
## A polynomial second-smallest floor from one rectangular row deletion

The preceding one-row kernel statement gives the following deduction.
Let X_N be a raw real symmetric Wigner matrix with fixed centered variance-one off-diagonal law xi and fixed real finite-second-moment diagonal law zeta.
For every gamma,B>0 there are fixed A_2,C,N_0 such that, uniformly over deterministic complex F with max|F_ab|<=N^gamma,
\[
 \mathbb P\{s_{N-1}(X_N+F)\le N^{-A_2}\}
                       \le C N^{-B},\qquad N\ge N_0.
 \tag{Raw-second-floor}
\]
Singular values here are ordered decreasingly, so s_(N-1) is the second-smallest singular value.
For W_N=X_N/sqrt(N) and max|F_ab|<=N^gamma, the same assertion holds with a changed exponent A_2 in
\[
 \mathbb P\{s_{N-1}(W_N+F)\le N^{-A_2}\}
                       \le C N^{-B}.
 \tag{Normalized-second-floor}
\]
No symmetric-offset assumption, least-singular-value floor or independence between physical sizes is asserted in this deduction.

Choose a raw cutoff exponent kappa>(B+4)/2.
A finite-second-moment union bound makes the probability any raw matrix variable exceeds N^kappa at most C N^(2-2kappa), which is at most C N^(-B-2).
Condition on all these independent cutoffs.
The off-diagonal coordinates remain independent with the common law xi_N above and uniform (AC) constants.
The diagonal values can now be fixed by conditioning, without affecting those coordinates.
Choose an entry exponent K large enough that all entries of every size-(N-1) principal block of X_N+F are bounded by (N-1)^K.
This K depends only on gamma,kappa; the change from N to N-1 costs a fixed exponent slack, rather than any dimension-dependent parameter.
Select b>B+4 and then a as in (One-row-kernel-AC).

Let M=X_N+F in this raw truncated model and retain its first N-1 rows as an (N-1)-by-N matrix B_0.
For a retained row i, project its row vector and the span H_i of the other N-2 retained rows by deleting coordinate i.
Call the projected row z_i and the projected span H_i'.
Projection is a contraction, hence
\[
 \operatorname{dist}((B_0)_i,H_i)
                   \ge\operatorname{dist}(z_i,H_i').
 \tag{Row-projection-distance}
\]
The matrix of projected other rows is the principal block D_i=M[[N] minus {i}] with the row corresponding to original index N omitted.
It has m=N-1 columns and m-1 rows.
Every bilinear unit normal u_i to those rows therefore satisfies (D_i u_i)_j=0 except possibly at that one omitted row.
There is always at least one such unit normal because there are more columns than rows.

Choose u_i measurably from that rectangular kernel using rank strata and a lexicographically first maximal nonzero minor.
Take the first free column, set its free coordinate to one and the other free coordinates to zero, solve on the pivot columns and normalize by its positive Euclidean norm.
At rank zero use the first coordinate vector.
This is the same finite rank-stratified rational construction as the square measurable kernel choice in C_F0194_v2, applied to the displayed rectangular matrix.
It depends only on D_i, and its coordinate functions are Borel on each stratum.

All coordinates of z_i are raw off-diagonal variables with law xi_N plus their deterministic offsets.
They are independent of D_i because their mirrored partners lie exactly in the deleted coordinate i.
The diagonal variable at i is also deleted and is not used.
On the complement of the D_i-measurable exceptional event in (One-row-kernel-AC), conditioning on D_i therefore gives
\[
 \mathbb P\left\{\left|\sum_j(z_i)_j(u_i)_j\right|
                    \le N^{-a}\ \middle|\ D_i\right\}
 \le (N-1)^{-b}.
\]
The threshold N^(-a) is no larger than (N-1)^(-a), so the displayed small-ball radius is allowed.
The arbitrary deterministic offset is absorbed into the supremum over the center in (One-row-kernel-AC).
Since u_i is a bilinear unit normal, Cauchy--Schwarz gives dist(z_i,H_i')>=|sum_j(z_i)_j(u_i)_j|.
Equivalently its complex Hilbert-space normal is the conjugate of u_i; no unproved real-versus-complex identification is made.
Thus
\[
 \mathbb P\{\operatorname{dist}((B_0)_i,H_i)\le N^{-a}\}
 \le (N-1)^{-b}+C e^{-c(N-1)}.
\]
A union over the N-1 retained rows makes every such row distance greater than N^(-a), outside probability C N^(1-b)+C exp(-c'N).
The rectangular matrix B_0 then has full row rank.
The accepted elementary Gram-inverse identity gives
\[
 \sum_{j=1}^{N-1}s_j(B_0)^{-2}
 =\sum_{i=1}^{N-1}\operatorname{dist}((B_0)_i,H_i)^{-2}
 \le N^{2a+1}.
\]
Therefore s_(N-1)(B_0)>=N^(-a-1/2).
Adding the last row is a positive semidefinite Gram perturbation, so s_(N-1)(M)>=s_(N-1)(B_0).
Choose A_2>a+1/2, and restore the discarded raw-entry event.
The choices b>B+4 and kappa>(B+4)/2 prove (Raw-second-floor), with room in the requested failure exponent.

For (Normalized-second-floor), multiply W_N+F by sqrt(N).
Its raw shift has entries bounded by N^(gamma+1/2), to which the raw statement applies with exponent gamma+1.
Divide the resulting second singular value by sqrt(N) and enlarge A_2 by one.
This proves the normalized assertion.
For an independent random F the uniform deterministic bound may be integrated on its polynomial entry guard, adding the guard-failure probability.

<a id="cluster-assembly"></a>
## Consequence for the remaining cluster branch

Apply the second-floor deduction simultaneously to the actual size-(N-1) principal minors, with polynomial failure exponent enlarged to absorb their union.
The original normalization remains sqrt(N); multiplying a principal minor by sqrt(N) gives a raw size-(N-1) matrix and only a fixed exponent slack in its shift bound.
It then supplies a polynomial lower bound for every t_2(D_i) outside arbitrarily small polynomial failures.
The low-matching implication (Small-minor-singular-value), at a sufficiently fine fixed threshold, makes t_1(D_i) as polynomially small as desired.
For A_i nonzero and D_i singular, it has exactly corank one and is already an isolated-minor branch.
For invertible D_i, choosing that smallness after the t_2-floor exponent gives both absolute and relative hypotheses of the reviewed C_F0194_v1 isolated-minor estimate.
Thus a low-matching actual minor can be treated on its tiny-full-determinant intersection using that fixed estimate, rather than by counting the entire Riccati fiber.

The complete parameter-ordered probability calculation follows.
The high-matching MNV term tends to zero at a polynomially growing matching size, but is not summable merely from the source exponent.
The resulting main floor is an in-probability assertion at the displayed single-Wigner nonsymmetric-shift scope.

<a id="in-probability-floor"></a>
## Complete in-probability floor assembly

Here is the full parameter order and probability calculation.
Fix the laws, gamma and requested B, and first work with deterministic F in its entry bound.
The finite-second-moment raw-entry cutoff and the bound ||F||<=N^(gamma+1) give an exponent K>=0 with
\[
 \mathbb P\{\|M\|>N^K\}\le C_BN^{-B-2},
 \qquad M=W_N+F.
\]
Choose the cutoff exponent larger than (B+4)/2 and then K larger than that exponent plus one half and gamma+1; this is exactly the elementary norm calculation in C_F0194_v3.
The [reviewed C_F0194_v2 corank tail](Yin_C_F0194_v2.md#decision-corank-tail-reviewed), after multiplying M by sqrt(N), also bounds P(rank M<=N-2) by C_B N^(-B-2).
Thus the accepted many-index estimate applies to the remaining event.

Use (Normalized-second-floor) with a failure exponent large enough to sum over all N actual principal minors D_i.
Their raw matrices have size N-1, their normalizing scale is sqrt(N), and their raw shifts have entries bounded by N^(gamma+1/2), at most (N-1)^(gamma+2) for large N.
Consequently there is a fixed L_2>0 and an exceptional probability C_B N^(-B-1) outside which
\[
 t_2(D_i)\ge N^{-L_2}\quad\text{for every }i.
 \tag{All-principal-second-floor}
\]
This is a use of the new complete second-floor proof above, not an expansion of the older intermediate-singular-value statement.

Apply the fixed [raw isolated-minor theorem](Yin_C_F0194_v1.md#statement) to the full raw matrix sqrt(N)M, with shift entry exponent gamma+1 and failure exponent B+2.
Denote its fixed determinant-ratio exponent by A_0 and its absolute and relative isolation exponent by L_iso.
These are selected before the fine low-matching thresholds.

Choose L,L_0 in the internal symmetric-part and full-minor symmetric-part guards above, with failure exponents enlarged to cover all actual D_i and all their internal row deletions, at most N^2 choices in total.
The probability of the union of these symmetric-part failures is then at most C_B N^(-B-1).
All shift bounds stay polynomial after raw scaling, and these exponents are fixed once the laws,gamma,B are fixed.
Choose
\[
 T_0>L_{\rm iso}+L_2+2,
 \qquad J>2K+L_0+T_0+1,
\]
and then
\[
 H>\max\{J+L+2K+1,\ 2K+L_0+T_0+3/2\}.
\]
Put h_N=N^(-H) and r_N=floor(sqrt(N)).
Then r_N log(N)=o(N), so the uncovered-diagonal result and (Small-minor-singular-value) apply.
After increasing their requested failure exponents to allow the outer union, the probability of any actual D_i violating that conclusion is at most C_B N^(-B-1)+C exp(-cN).
In particular, on all these guards, a nonzero-adjugate low-matching minor satisfies
\[
 t_1(D_i)\le2N^{-T_0}.
 \tag{Low-matching-small-minor}
\]

For a singular D_i with nonzero adjugate, rank D_i=N-2, exactly the singular isolated-minor branch.
For an invertible such D_i, raw scaling gives
\[
 \begin{split}
 t_1(\sqrt N D_i)&\le2N^{-T_0+1/2}\le N^{-L_{\rm iso}},\\
 \frac{t_1(\sqrt N D_i)}{t_2(\sqrt N D_i)}
   &=\frac{t_1(D_i)}{t_2(D_i)}
     \le2N^{-T_0+L_2}\le N^{-L_{\rm iso}}
 \end{split}
\]
for large N, by the choice of T_0.
Thus every nonzero-adjugate low-matching actual minor is in the exact isolated-minor class on the retained guards.

Finally choose the full least-singular-value exponent A so large that
\[
 A>H+2K+2,
 \qquad A>A_0+2K+2,
 \qquad A>1.
\]
For epsilon=N^(-A), the accepted C_F0194_v3 event G_i has normalized determinant ratio at most C_1N^(2K+1-A).
Its matching-radius condition C_1N^(2K+1-A)<=c_* h_N/N therefore holds eventually.
For the raw isolated-minor comparison, the exact rescaling is
\[
 \frac{|\det(\sqrt N M)|}
      {\|\operatorname{adj}(\sqrt N D_i)\|_F}
   =N\frac{|\det M|}{\|\operatorname{adj}D_i\|_F}.
 \tag{Ratio-normalization}
\]
The raw numerator has N rows, whereas the adjugate of D_i has homogeneous degree N-2, explaining the factor N rather than sqrt(N).
Thus G_i implies a raw ratio at most C_1N^(2K+2-A)<=N^(-A_0) eventually.

Split the accepted many-index average into G_i intersect H_i(h_N,r_N) and G_i intersect its complement.
The matching half is bounded by C psi(r_N) using the accepted conditional matching theorem; averaging does not introduce a factor N.
For the low-matching half, outside the new guard failures, every G_i forces an event of the reviewed raw isolated-minor theorem with its exact absolute, relative and determinant-ratio thresholds.
The probability of the union of those raw isolated-minor events is at most C_B N^(-B-2).
The mean of their indicator probabilities is no larger than the probability of their union, so this same bound controls the low-matching contribution to the average.
Adding all norm, corank, symmetric-part, uncovered-diagonal and second-floor failures proves
\[
 \mathbb P\{s_{\min}(M)\le N^{-A}\}
                     \le C_BN^{-B}+C\psi(\lfloor\sqrt N\rfloor).
\]
The definition of psi in C_F0194_v3 gives the displayed rate in (Candidate-floor), after absorbing its exponential term and fixed constants.

For an independent random F_N, condition on F_N within this dimension, integrate the uniform estimate on max|F_ab|<=N^gamma, and add the complementary guard probability.
No complete cross-dimensional shift sequence is conditioned on and no independence between physical sizes is needed.
This completes the assembly at its explicitly stated single-Wigner nonsymmetric-shift scope.

The new second-floor, uncovered-diagonal and in-probability floor arguments have independent review at this exact fixed version.
No reduction of arbitrary matrix-coefficient pencils to one independent Wigner plus a shift is used or asserted.


## Current assessment
[Selected decision](#decision-nonsymmetric-floor-reviewed)

## Assessment history

### Decision nonsymmetric-floor-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T11:11 |
| status | open |
| reason | Complete candidate proofs are fixed for fresh review of actual-minor uncovered-diagonal exclusion, hub and small-minor consequences, one-omitted-row kernel anti-concentration, arbitrary-power second-smallest floors and the uniform in-probability least-singular-value bound. The main error is not asserted summable and no Brown or general matrix-pencil completion is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact main and subsidiary assertions](#statement) | Real fixed finite-second-moment Wigner laws, arbitrary polynomially bounded deterministic complex nonsymmetric shifts, independent random-shift guards, actual-minor dimensions and normalization, full second-smallest and in-probability floor scope. |
| argument | [Complete candidate argument](#argument) | Internal-row exposure and cover union, hub rank and minor-ratio consequences, one-omitted-row inverse-concentration counting, measurable rectangular normals, negative-second-moment floor, and full norm/rank/threshold assembly with exact raw scaling. |
| dependency | [Symmetric-part floors](Yin_C_F0188_v2.md#statement) | Only floors for genuinely complex symmetric shifts of real Wigner matrices, applied to sym D and sym B after the displayed raw-to-normalized substitutions and simultaneous-minor unions. |
| dependency | [Exact structured class](Yin_C_F0194_v1.md#counting-class) | Rational progression candidates and at least m-C_0 prescribed row constraints, allowing the new one-row-omitted consequence without expanding the older theorem statement. |
| dependency | [Complete nonsymmetric-offset count](Yin_C_F0194_v1.md#structured-vector-counting) | The fixed profile count, uniform deterministic diagonals, polynomial entry guards, omitted-row choices, and uniform anti-concentration constants of the independently truncated real laws. |
| dependency | [Linear inverse and rounding interface](Yin_C_F0194_v1.md#inverse-rounding) | Exact dimension-two linear inverse-theorem output and rational rounding, at fixed structural constants before the fine precision; the new omitted-row residual check is supplied here. |
| dependency | [Accepted linear source conventions](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) | Only arXiv:1105.5733v1 Condition 1 and Theorem 1.3 for real scalar laws and dimension-two coefficients, at its recorded original-proof inspection limits. |
| dependency | [Isolated-minor probability theorem](Yin_C_F0194_v1.md#statement) | The raw determinant-ratio estimate on exactly corank-one or quantitatively isolated principal minors, invoked only after the new absolute and relative gap hypotheses have been established. |
| dependency | [Fixed linear-codimension distance](Yin_C_F0194_v3.md#linear-codimension) | The exp(-cp) bound uniform over complex affine subspaces of codimension at least p/2 and all centers, applied after internal-row and cover-coordinate conditioning. |
| dependency | [Accepted many-index averaging](Yin_C_F0194_v3.md#spread-and-average) | Only its pointwise many-index implication and probability average under the stated norm and rank guards, without a union loss over omitted indices. |
| dependency | [Accepted finite-radius matching](Yin_C_F0194_v3.md#two-copy-matching) | Only the normalized real-law cofactor matching bound with psi(r), complete two-copy adaptation and the coefficient scale h/N; no unary result of v4 is used. |
| dependency | [Polynomial norm calculation](Yin_C_F0194_v3.md#polynomial-shift-proof) | Only the finite-second-moment raw-entry union bound and normalized polynomial norm guard. |
| dependency | [Reviewed corank guard](Yin_C_F0194_v2.md#decision-corank-tail-reviewed) | Only the full corank-at-least-two tail used in the main assembly after multiplying the normalized matrix by sqrt(N); the new second-value argument is supplied independently here. |

### Decision nonsymmetric-floor-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T11:17 |
| status | proved |
| reason | Fresh independent whole-proof review verifies the complete actual-minor, omitted-row and rectangular-normal deductions and their parameter-ordered assembly against every declared input. This establishes the uniform in-probability least-singular-value bound and the stated arbitrary-power second-smallest floors for real Wigner inputs with arbitrary complex nonsymmetric polynomial shifts, without summability or a broader Task conclusion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact main and subsidiary assertions](#statement) | Real fixed finite-second-moment Wigner laws, arbitrary polynomially bounded deterministic complex nonsymmetric shifts, independent random-shift guards, actual-minor dimensions and normalization, full second-smallest and in-probability floor scope. |
| argument | [Complete candidate argument](#argument) | Internal-row exposure and cover union, hub rank and minor-ratio consequences, one-omitted-row inverse-concentration counting, measurable rectangular normals, negative-second-moment floor, and full norm/rank/threshold assembly with exact raw scaling. |
| dependency | [Symmetric-part floors](Yin_C_F0188_v2.md#statement) | Only floors for genuinely complex symmetric shifts of real Wigner matrices, applied to sym D and sym B after the displayed raw-to-normalized substitutions and simultaneous-minor unions. |
| dependency | [Exact structured class](Yin_C_F0194_v1.md#counting-class) | Rational progression candidates and at least m-C_0 prescribed row constraints, allowing the new one-row-omitted consequence without expanding the older theorem statement. |
| dependency | [Complete nonsymmetric-offset count](Yin_C_F0194_v1.md#structured-vector-counting) | The fixed profile count, uniform deterministic diagonals, polynomial entry guards, omitted-row choices, and uniform anti-concentration constants of the independently truncated real laws. |
| dependency | [Linear inverse and rounding interface](Yin_C_F0194_v1.md#inverse-rounding) | Exact dimension-two linear inverse-theorem output and rational rounding, at fixed structural constants before the fine precision; the new omitted-row residual check is supplied here. |
| dependency | [Accepted linear source conventions](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) | Only arXiv:1105.5733v1 Condition 1 and Theorem 1.3 for real scalar laws and dimension-two coefficients, at its recorded original-proof inspection limits. |
| dependency | [Isolated-minor probability theorem](Yin_C_F0194_v1.md#statement) | The raw determinant-ratio estimate on exactly corank-one or quantitatively isolated principal minors, invoked only after the new absolute and relative gap hypotheses have been established. |
| dependency | [Fixed linear-codimension distance](Yin_C_F0194_v3.md#linear-codimension) | The exp(-cp) bound uniform over complex affine subspaces of codimension at least p/2 and all centers, applied after internal-row and cover-coordinate conditioning. |
| dependency | [Accepted many-index averaging](Yin_C_F0194_v3.md#spread-and-average) | Only its pointwise many-index implication and probability average under the stated norm and rank guards, without a union loss over omitted indices. |
| dependency | [Accepted finite-radius matching](Yin_C_F0194_v3.md#two-copy-matching) | Only the normalized real-law cofactor matching bound with psi(r), complete two-copy adaptation and the coefficient scale h/N; no unary result of v4 is used. |
| dependency | [Polynomial norm calculation](Yin_C_F0194_v3.md#polynomial-shift-proof) | Only the finite-second-moment raw-entry union bound and normalized polynomial norm guard. |
| dependency | [Reviewed corank guard](Yin_C_F0194_v2.md#decision-corank-tail-reviewed) | Only the full corank-at-least-two tail used in the main assembly after multiplying the normalized matrix by sqrt(N); the new second-value argument is supplied independently here. |
| review | [Independent complete nonsymmetric-floor review](../audits/reviews/Yin_R_F0200_v5.md#finding) | Main and every subsidiary assertion, entire new argument, all eleven declared dependency interfaces, normalizations, measurable conditioning, parameter order and limitations; no unresolved mathematical or source-applicability gap in this exact scope. |
