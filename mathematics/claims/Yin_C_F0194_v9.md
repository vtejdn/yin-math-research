---
author: Yin
---

# Even skew Wigner floors with an approximately rank-two symmetric shift

This is a project deduction, with no novelty or priority claim.
It extends the [accepted even-skew floor](Yin_C_F0194_v7.md#decision-complex-floor-reviewed) to arbitrary complex shifts whose transpose-symmetric part has rank at most two, or a sufficiently small third singular value.
The [current decision](#decision-rank-two-reviewed) adopts this statement after [independent whole-proof review](../audits/reviews/Yin_R_F0200_v9.md#rank-two-whole-proof), retaining all stated hypotheses and limits.
Earlier physical versions retain their distinct fixed statements and actual review scopes.
The deterministic rank-three example below limits one proposed extension of the proof; it does not refute a random arbitrary-shift theorem.

<a id="statement"></a>
## Exact statement and limits

<a id="model"></a>
### Model, normalization and conventions

Fix a real law eta with E eta=0 and E eta^2=1; no moment above two is assumed.
Let W_N have independent strict upper entries i eta_jk/sqrt(N), conjugate lower entries and identically zero diagonal.
The law is fixed with dimension, and every realization satisfies W_N^*=W_N and W_N^T=-W_N.
Transpose T is complex-linear, with no conjugation, and
\[
 \operatorname{sym}F=(F+F^T)/2,\qquad
 \operatorname{skew}F=(F-F^T)/2.
\]
Singular values s_1>=...>=s_N are decreasing; s_min denotes s_N, and ||.|| is the Euclidean operator norm.
There is no Hermitian or transpose-sign hypothesis on the shift F itself.

<a id="rank-two-even-floor"></a>
### Deterministic and independent-random-shift floors

For every gamma,B>0 there are fixed a,L,C_B,N_0>0, depending only on gamma,B and the eta law, with L=a+1 and N_0>=6, such that for every even N>=N_0,
\[
 \sup_{\substack{F\in M_N(\mathbb C)\\
       \max_{j,k}|F_{jk}|\le N^\gamma\\
       s_3(\operatorname{sym}F)\le N^{-L}}}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-a}\}
 \le C_BN^{-B}.
 \tag{Near-two-rank-floor}
\]
In particular the same uniform estimate holds for every shift in this entry bound with rank(sym F)<=2.
The constants are chosen before the shift and the dimension limit, not for a single prescribed sequence of shifts.
For an arbitrary random F_N independent of the whole W_N, define
\[
 \Gamma_N=\{\max_{j,k}|F_{N,jk}|\le N^\gamma,
                  \ s_3(\operatorname{sym}F_N)\le N^{-L}\}.
\]
Then the same right side bounds P(s_min(W_N+F_N)<=N^(-a),Gamma_N); add P(Gamma_N^c) for the unguarded bound.
Only F_N is conditioned on; neither its guard nor any spectral good event is conditioned on as an additional premise.
No independence between dimensions is required.

The finite-rank determinant and inverse identities, the two-skew-update scalar bounds, and the rank-one specialization proved in [the argument](#finite-rank-identities) are included at their stated deterministic scopes.
The [rank-three boundary](#rank-three-boundary) gives a concrete invertible complex skew A and a rank-three symmetric S=UU^T for which A+S is singular although A and every coordinate-pair update A+/- i UJ_pq U^T are invertible.
The example extends to every even dimension at least six with uniform finite norms and positive least values for those skew matrices.
It refutes that deterministic pairwise-update implication only.

There is no assertion for every odd dimension: the allowed shift F=0 leaves W_N skew, and det W_N=det W_N^T=det(-W_N)=-det W_N forces zero determinant for odd N.
There is no conclusion for every arbitrary complex shift in even dimension, nor any carrier determinant transfer or original Task completion here.
Failure of the [earlier symmetric-quantile guard](Yin_C_F0194_v7.md#quantile-guard-floor) need not imply the small-third-singular-value hypothesis above.

<a id="argument"></a>
## Complete argument and precise direct inputs

The [accepted C_F0194_v7 decision](Yin_C_F0194_v7.md#decision-complex-floor-reviewed) is used only for its [even-skew floor](Yin_C_F0194_v7.md#even-floor), uniformly for complex skew shifts with a fixed polynomial entry bound and any chosen inverse-power failure exponent.
The [accepted C_F0186_v4 second-moment control](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) is used at [its positive-tail input](Yin_C_F0186_v4.md#positive-tail): E tr_N(W_N^2)<=1 for this zero-diagonal variance-one model, giving a polynomial operator-norm probability bound by Markov's inequality.
The [You61 symmetric unitary-congruence input](../audits/literature/You61/Yin_U001.md#symmetric-congruence) is the established source statement at printed p. 694 / PDF p. 1, introduction equation (1), in the retained 1961 edition.
Its statement and applicability were checked directly; its full original proof was not audited.
All further algebraic and singular-subspace comparisons are proved below.
No working draft, general arbitrary-shift floor, or proof from the eighth physical version is a logical input.

<a id="symmetric-factorization"></a>
## Symmetric factorization and approximation

For any complex S with S^T=S, the accepted source form gives
\[
 S=V\operatorname{diag}(s_1(S),\ldots,s_N(S))V^T
\]
with V unitary.
This is equivalent to the source's Q^T S Q=diag(s_j(S)), with V=conjugate(Q).
If rank S<=2, its first two scaled columns, padded by zeros when necessary, give U in M_(N,2)(C) such that
\[
 S=UU^T,\qquad \|U\|^2=\|S\|.
 \tag{Two-column-factor}
\]
For arbitrary symmetric S, keeping those same two diagonal terms gives S_2=UU^T of rank at most two with
\[
 \|S_2\|\le\|S\|,\qquad \|S-S_2\|=s_3(S).
\]
Both V and V^T are unitary, so these norms follow directly from the omitted diagonal terms.
The truncation preserves transpose symmetry.
For max|F_jk|<=N^gamma, both sym F and skew F have norm at most N^(gamma+1), by their entry bounds and the Frobenius norm.
The proof first treats deterministic F, so no measurable choice of factorization is needed for the random-shift conclusion.

<a id="finite-rank-identities"></a>
## Elementary identities for a skew matrix and a symmetric perturbation

Let A be an invertible complex transpose-skew matrix of even order and write S=UU^T with U having r columns.
Then A^(-1) is skew, and
\[
 K=U^T A^{-1}U\quad\text{satisfies}\quad K^T=-K.
\]
For rectangular X,Y, the two Schur complements of the block matrix with diagonal blocks I_N,I_r and off-diagonal blocks X,-Y give det(I_N+XY)=det(I_r+YX).
Consequently
\[
 \det(A+UU^T)=\det A\det(I_r+K).
 \tag{Small-determinant}
\]
When I_r+K is invertible, direct multiplication gives
\[
 (A+UU^T)^{-1}
 =A^{-1}-A^{-1}U(I_r+K)^{-1}U^T A^{-1}.
 \tag{Finite-rank-inverse}
\]
Indeed the additional coefficient after multiplying on the left by A+UU^T is I_r-(I_r+K)(I_r+K)^(-1)=0.
These are exact finite-dimensional algebraic calculations, not probability estimates.

For r=1, skewness gives K=0.
Thus a symmetric rank-one addition leaves det A unchanged and its inverse norm is at most ||A^(-1)||+||A^(-1)||^2||S||.
This already transfers the even-skew floor to every polynomially bounded symmetric rank-one perturbation.

For r=2 put
\[
 J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad K=kJ.
\]
Define two additional skew matrices
\[
 A_+=A+iUJU^T,\qquad A_-=A-iUJU^T.
\]
Their perturbations are complex transpose-skew and have norm at most ||U||^2.
The same rectangular determinant identity gives
\[
 \begin{split}
 \det(I_N\mathbin{\pm}iA^{-1}UJU^T)
 &=\det(I_2\mathbin{\pm}iJK)
 =(1\mp ik)^2,\\
 \det(I_2+K)&=1+k^2=(1-ik)(1+ik),\\
 (I_2+K)^{-1}&=(I_2-K)/(1+k^2)
       \quad\text{when }1+k^2\ne0.
 \end{split}
 \tag{Two-skew-updates}
\]
These identities do not divide two full determinants to estimate an exponentially small quantity.
The next rank comparison gives polynomial control of each scalar factor directly.

If rank R<=2, the largest N-2 singular values of I_N+R are at least one: intersect the whole space with ker R and use singular-value min-max.
Its remaining two singular values are at least s_min(I_N+R), so
\[
 |\det(I_N+R)|\ge s_{\min}(I_N+R)^2.
\]
Apply this to R=+/- iA^(-1)UJU^T and note that
\[
 s_{\min}(A^{-1}A_\pm)\ge s_{\min}(A_\pm)/\|A\|.
\]
Taking nonnegative square roots in (Two-skew-updates) yields the useful bounds
\[
 |1\mp ik|\ge\frac{s_{\min}(A_\pm)}{\|A\|},\qquad
 |1+k^2|\ge\frac{s_{\min}(A_+)s_{\min}(A_-)}{\|A\|^2}.
 \tag{Two-factor-lower-bound}
\]
No assumption that A or its perturbations are normal is used.

<a id="rank-two-proof"></a>
## Probability floor and order of the fixed constants

Fix gamma,B>0.
Use the accepted even-skew floor with shift exponent gamma+3 and failure exponent B+1 to choose b>0 and its fixed constants.
Choose D>gamma+3 with 2D>B+2, and put
\[
 h=5b+4D,\qquad a=h+3,\qquad L=h+4=a+1.
 \tag{Fixed-exponents}
\]
These choices depend only on the stated law and gamma,B.
All dimension thresholds below may be enlarged finitely after these choices.

First let sym F=S=UU^T have rank at most two and put A=W_N+skew F.
The three matrices A,A_+,A_- from (Two-skew-updates) are W_N plus deterministic complex skew shifts.
Their shift entries are at most N^(gamma+3) for all sufficiently large N, since ||U||^2=||S||<=N^(gamma+1).
A union bound over the three accepted skew-floor estimates gives, outside probability C_B N^(-B),
\[
 s_{\min}(A),s_{\min}(A_+),s_{\min}(A_-)\ge N^{-b}.
\]
The three shifted matrices need not be independent.

The selected second-moment control gives E||W_N||_F^2=N E tr_N(W_N^2)<=N, where ||.||_F is the Frobenius norm.
Since ||skew F||<=N^(gamma+1)<=N^D/2 for sufficiently large N, Markov's inequality yields
\[
 \mathbb P\{\|A\|>N^D\}
 \le \mathbb P\{\|W_N\|_F>N^D/2\}
 \le4N^{1-2D}\le C_BN^{-B}.
\]
Also ||U||^2<=N^D deterministically.
On the intersection of these events, (Two-factor-lower-bound) and ||K||<=||U||^2||A^(-1)|| give
\[
 \|K\|\le N^{b+D},\qquad
 |1+k^2|\ge N^{-2b-2D},\qquad
 \|(I_2+K)^{-1}\|\le2N^{3b+3D}.
\]
In particular I_2+K is invertible.
The finite-rank inverse identity proves
\[
 \|(W_N+F)^{-1}\|
 \le N^b+2N^{5b+4D}\le3N^h.
 \tag{Exact-two-rank-inverse}
\]
This already gives the exact rank-at-most-two probability floor.

For general F in the stated class, take the symmetric truncation S_2 and set F_2=skew F+S_2.
Then sym F_2=S_2, skew F_2=skew F, and ||S_2||<=N^(gamma+1).
Although ||F_2|| can be as large as 2N^(gamma+1), the three skew shifts in its preceding argument remain bounded by N^(gamma+3), the exponent at which b was already chosen.
The same D controls A=W_N+skew F and the factor U for S_2.
Thus (Exact-two-rank-inverse) holds for W_N+F_2 with the already fixed h, outside probability C_B N^(-B), without another parameter choice.
The variational formula s_min(M)=inf_(||x||=1)||Mx|| and the triangle inequality imply
\[
 \begin{split}
 s_{\min}(W_N+F)
 &\ge s_{\min}(W_N+F_2)-\|F-F_2\|\\
 &\ge\tfrac13N^{-h}-N^{-h-4}>N^{-h-3}
 \end{split}
\]
for sufficiently large N.
This proves the deterministic assertion and the claimed order of exponents.

If F_N is independent of W_N, integrate this uniform deterministic bound over F_N restricted to Gamma_N.
The probability of the least-value event intersected with Gamma_N is at most C_B N^(-B), and adding P(Gamma_N^c) gives the unguarded form.
This conditioning uses independence of the entire shift from the entire Wigner matrix within each dimension, with no assumption on cross-size coupling.
A background-generated inverse shift may use the result only after verifying the actual entry and small-third-singular-value guards.

<a id="rank-three-boundary"></a>
## A concrete failure of the pairwise deterministic extension at rank three

For three columns the skew compression has the form
\[
 K=\begin{pmatrix}0&x&y\\-x&0&z\\-y&-z&0\end{pmatrix},
 \qquad\det(I_3+K)=1+x^2+y^2+z^2.
\]
This is not the product of the two scalar linear factors present at rank two.
The natural plan of controlling all coordinate-pair skew updates does not resolve it, as the following exact example shows.
Put x=y=z=i/sqrt(3), let U be the 6-by-3 matrix with upper block I_3 and lower block zero, and set
\[
 A=\begin{pmatrix}0&-I_3\\I_3&K\end{pmatrix},\qquad
 A^{-1}=\begin{pmatrix}K&I_3\\-I_3&0\end{pmatrix},\qquad
 S=UU^T=\begin{pmatrix}I_3&0\\0&0\end{pmatrix}.
\]
Direct multiplication verifies the displayed inverse, and A^T=-A.
But det(A+S)=det A det(I_3+K)=0, since 1+x^2+y^2+z^2=0.
For each p<q in {1,2,3}, let J_pq=e_p e_q^T-e_q e_p^T.
The rectangular determinant identity gives
\[
 \det(A\mathbin{\pm}iUJ_{pq}U^T)/\det A
       =(1\mp iK_{pq})^2=(1\mathbin{\pm}1/\sqrt3)^2\ne0.
\]
Thus A and all six coordinate-pair skew updates are invertible, with fixed finite norms and positive least singular values, while the rank-three symmetric addition is singular.
Taking direct sums with copies of the invertible two-by-two skew block J gives the same failure in every even dimension at least six, with uniform deterministic bounds.
This disproves this deterministic implication, not the desired random Wigner theorem: the displayed A is not W_N plus an independent deterministic shift with the required law.
Replacing a deterministic shift by A-W_N would violate that independence.

For general rank r, the exact unresolved denominator is det(I_r+U^T A^(-1)U), or equivalently the least value of this small matrix in the finite-rank inverse identity.
The accepted skew floor controls fixed skew perturbations of A, but the rank-three example prevents inferring this denominator's lower bound merely from the finite list of pairwise updates.
Also, failure of C_F0194_v7's quantile guard does not imply the small-third-singular-value guard in (Near-two-rank-floor): the symmetric part can have rank between three and O(sqrt(N)), or a larger rank with an intermediate tail.
Thus the new result closes only the quantitatively approximate rank-two branch and does not yet exhaust the complementary regime of the original guard.

## Current assessment
[Selected decision](#decision-rank-two-reviewed)

## Assessment history

### Decision rank-two-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T14:59 |
| status | open |
| reason | Complete candidate gives a uniform arbitrary-power even-dimensional floor for complex shifts with exact or sufficiently approximate rank-two transpose-symmetric part, by three accepted skew-floor applications and a two-dimensional inverse comparison. The rank-three example refutes only the pairwise deterministic extension. Independent whole-proof review remains outstanding; no general arbitrary-shift or original Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact rank-two floor and boundaries](#statement) | Fixed finite-second-moment purely imaginary zero-diagonal model, uniform deterministic exact/approximate rank-two floor with L=a+1, independent random shifts and arbitrary cross-size coupling, all subsidiary algebraic bounds, rank-three pairwise counterexample and parity/general-shift limits. |
| argument | [Complete argument](#argument) | Exact source factorization, finite-rank determinant and inverse identities, two-factor bound, three uniform skew-floor applications, operator-norm control, fixed parameter order, approximation and conditioning, and the explicit rank-three example. |
| dependency | [Accepted even-skew floor](Yin_C_F0194_v7.md#decision-complex-floor-reviewed) | Only #even-floor for fixed real centered variance-one finite-second-moment amplitudes, zero diagonal, even N, arbitrary polynomially bounded deterministic complex skew shifts and any fixed inverse-power failure exponent; used three times without conditioning on good events. |
| dependency | [Accepted second-moment control](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Only the one-input E tr_N(W_N^2)<=1 control at #positive-tail, specialized to this zero-diagonal model and converted by Markov into an arbitrary-power operator-norm bound. |
| dependency | [You61 symmetric congruence](../audits/literature/You61/Yin_U001.md#you61-u001) | Printed p. 694 / PDF p. 1, introduction equation (1), 1961 publication edition: arbitrary complex transpose-symmetric matrix has unitary congruence to its nonnegative singular-value diagonal. Exact statement accepted; full source proof not audited. The factorization and rank-two truncation are derived here. |

### Decision rank-two-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T15:16 |
| status | proved |
| reason | Independent whole-proof review supports the uniform exact and approximate symmetric-rank-two floor through even dimensions, every stated deterministic auxiliary, the independent-random-shift extension and the rank-three boundary. All three direct inputs apply at their exact scopes. General complex shifts, odd-dimensional floors, carrier transfers and the original Tasks remain outside this result. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact rank-two floor and boundaries](#statement) | Fixed finite-second-moment purely imaginary zero-diagonal model, uniform deterministic exact/approximate rank-two floor with L=a+1, independent random shifts and arbitrary cross-size coupling, all subsidiary algebraic bounds, rank-three pairwise counterexample and parity/general-shift limits. |
| argument | [Complete argument](#argument) | Exact source factorization, finite-rank determinant and inverse identities, two-factor bound, three uniform skew-floor applications, operator-norm control, fixed parameter order, approximation and conditioning, and the explicit rank-three example. |
| dependency | [Accepted even-skew floor](Yin_C_F0194_v7.md#decision-complex-floor-reviewed) | Only #even-floor for fixed real centered variance-one finite-second-moment amplitudes, zero diagonal, even N, arbitrary polynomially bounded deterministic complex skew shifts and any fixed inverse-power failure exponent; used three times without conditioning on good events. |
| dependency | [Accepted second-moment control](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Only the one-input E tr_N(W_N^2)<=1 control at #positive-tail, specialized to this zero-diagonal model and converted by Markov into an arbitrary-power operator-norm bound. |
| dependency | [You61 symmetric congruence](../audits/literature/You61/Yin_U001.md#you61-u001) | Printed p. 694 / PDF p. 1, introduction equation (1), 1961 publication edition: arbitrary complex transpose-symmetric matrix has unitary congruence to its nonnegative singular-value diagonal. Exact statement accepted; full source proof not audited. The factorization and rank-two truncation are derived here. |
| review | [Independent rank-two whole-proof finding](../audits/reviews/Yin_R_F0200_v9.md#rank-two-whole-proof) | Complete statement and argument, all three direct interfaces, symmetric source factorization, finite-rank identities and two-factor bounds, uniform exponent order, approximation, measurability and conditioning, rank-one specialization and exact rank-three/parity limits. |
