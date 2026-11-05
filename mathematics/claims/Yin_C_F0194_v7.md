---
author: Yin
---

# Complex Hermitian Wigner least-value floors with law and quantile guards

This version combines a generic complex finite-net count, a non-line full-adjugate matching argument and a purely imaginary symmetric-quantile argument as a new open candidate for fresh independent review.
The earlier physical versions retain their mathematics and actual assessments.
The non-purely-imaginary phase-line main theorem is reused from its reviewed sixth version and is not reproved.
This is a project deduction with no novelty or priority claim.

<a id="statement"></a>
## Exact statement, auxiliary scope and boundary

For the normalized matrix floors, fix a centered complex law xi with E|xi|^2=1 and an independent real diagonal law zeta of finite second moment.
Let W_N be Hermitian with independent strict upper entries xi/sqrt(N), independent diagonal entries zeta/sqrt(N), and conjugate lower entries.
The laws are fixed with N, and the two entry families are independent.
Every shift below is an arbitrary deterministic complex matrix unless its symmetry or independence is explicitly specified.
All constants are uniform over the displayed shift class, and different dimensions may have arbitrary coupling.
No density, non-atomicity or moment above two is assumed.

For every gamma,B>0 the following non-line assertion holds with fixed A,C_B,C,N0 depending only on the laws,gamma,B:
if the support of xi is not contained in a real line through zero, then
\[
 \sup_{\max|F_{jk}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}\,N^{-1/18},
 \qquad N\ge N0.
 \tag{Nonline-main}
\]
The complete new proof is at [the non-line assembly](#nonline-floor).
For an independent random shift F_N, the same right side bounds the event intersected with Gamma_N={max|F_N,jk|<=N^gamma}; add P(Gamma_N^c) for the unguarded probability.

If xi=c eta with |c|=1, Re c nonzero and eta a centered variance-one real law, the same conclusion and random-shift form hold by direct reuse of [C_F0194_v6](Yin_C_F0194_v6.md#statement).
This phase-line branch is an accepted input, not an extension of its hypothesis to c=i.

For the purely imaginary law xi=i eta, with eta real, centered and variance one, retain any fixed real diagonal law zeta of finite second moment, which need not be centered.
For fixed gamma,L0,B>0, put M=W_N+F, D_i=M[[N] minus {i}], S_i=sym D_i=(D_i+D_i^T)/2, r_N=floor(sqrt(N)), and k_N=4r_N+1.
With singular values in decreasing order, define
\[
 \Sigma_N(F,L0)=\bigcap_{i=1}^N\{s_{k_N}(S_i)\ge N^{-L0}\}.
\]
For all sufficiently large N, k_N<=N-1.
There are fixed A,C_B,C,N0 depending only on the laws,gamma,L0,B such that
\[
 \sup_{\max|F_{jk}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A},\ \Sigma_N(F,L0)\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}\,N^{-1/18}.
 \tag{Pure-imaginary-guarded-main}
\]
There is no parity restriction in this guarded estimate.
For F_N independent of the whole W_N, define Gamma_N as above and epsilon_N^guard=P(Gamma_N^c union Sigma_N(F_N,L0)^c).
The unguarded least-value probability is bounded by the same right side plus epsilon_N^guard.
The guard uses the actual symmetric principal minors and may be correlated with the noise diagonal; the proof never conditions on that guard.
No bound for this guard failure is asserted for an arbitrary independent shift.

Every complex transpose-skew matrix has paired positive singular values and even rank, with paired zero values also when its dimension is even.
For pure-imaginary W_N with identically zero diagonal and a complex transpose-skew shift F, every realization W_N+F is transpose-skew, without a Hermitian requirement on F.
For every gamma,B>0 there are fixed A,C_B,N0 such that
\[
 \sup_{\substack{F^T=-F\\\max|F_{jk}|\le N^\gamma}}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
       \le C_BN^{-B}\quad(N\ge N0,\ N\text{ even}).
 \tag{Even-skew-main}
\]
It holds for an independent random complex skew shift on its polynomial entry guard, with that guard failure added otherwise.
Every odd-dimensional realization in this zero-diagonal skew-shift class is singular.
Thus neither the guarded estimate nor the even skew estimate asserts an all-law all-size unguarded floor.

This statement also includes the following auxiliary assertions at their full displayed hypotheses and constants.

- The [generic orientation-envelope interface and full proof](#generic-envelope-interface), for every fixed complex law of finite nonzero variance, possibly noncentered, the same conditional cutoff law xi_N across n in [N/4,N], any fixed Hermitian orientation table, polynomially bounded deterministic complex offsets and diagonals, and every fixed number s0 of omitted row constraints. It controls all unit near-kernel vectors and also D^T outside C exp(-cn).
- The [uniform truncated-law control](#generic-uniform-truncation), [linear oscillation](#generic-linear-oscillation), [deterministic finite-family exclusion](#generic-finite-family-count), and [initial finite covers](#generic-initial-net), with their fine-precision and controlled-moment parameter order.
- The [generic corank tail](#generic-rank), [raw and normalized second-smallest floors](#generic-second-floor), and [restricted raw isolated-minor bound](#generic-isolated-minor), for all fixed complex upper laws of finite nonzero variance and independent fixed real finite-second-moment diagonals. These auxiliary conclusions have arbitrary polynomial failure and do not exclude a parity-forced corank one.
- The [full-adjugate matching estimate](#nonline-full-matching) for a centered variance-one non-line law and arbitrary conditional minor, and the [large uncovered diagonal exclusion](#full-adjugate-low-matching) and [low-matching minor-ratio implication](#full-adjugate-hub-ratio) for every centered variance-one complex law, including line-supported laws, with only the displayed operator-norm guard and no symmetric-part floor.
- The [self-contained skew pairing proof](#singular-pairing), [pure-imaginary internal skew directions](#internal-many-directions), [uncovered-diagonal exclusion](#pure-imaginary-uncovered-diagonal), and [quantile low-matching consequence](#low-matching-quantile), with all fixed thresholds selected in the stated order.

The displayed matching errors tend to zero and are not claimed summable.
No logarithmic determinant limit, scalar-affine synthesis, matrix-polynomial transfer, Brown-measure assertion or completion of an original determinant Task is part of this candidate.

<a id="argument"></a>
## Complete proof and exact fixed inputs

The new complex linear argument uses [TV08-U001](../audits/literature/TV08/Yin_U001.md#tv08-u001): Definition 2.2, Lemma 2.4, Definition 3.1 and Theorem 3.2 of arXiv:0708.2895v5 at the exact complex-scalar scope, common-control uniformity, covering norm, polynomial concentration range and original-proof inspection limits recorded there.
The original inverse theorem is an accepted external input, not re-audited here; all orientation, truncation, block normalization, representative and profile deductions are proved below.
[MNV16-U001](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) supplies its original 2016 degree-one and degree-two real fair-sign finite-interval estimates, with the stated original-proof inspection limits.
The exact two-copy adaptations and complex projections are local arguments below.
No disputed NO15 arithmetic clause or real-scalar inverse theorem for a complex random variable is invoked.

The accepted [C_F0194_v6 complex distance estimate](Yin_C_F0194_v6.md#complex-distance) is used at its full arbitrary-complex-law scope.
The [C_F0194_v3 row-adjugate inequality](Yin_C_F0194_v3.md#row-adjugate), [rectangle mechanism](Yin_C_F0194_v3.md#rectangles) and [pointwise spread and average](Yin_C_F0194_v3.md#spread-and-average) are reused only after the complex conditional column-distance hypotheses have been checked.
The measurable kernel and deterministic two-form rank increment use [C_F0194_v2](Yin_C_F0194_v2.md#border-rank), with all new generic probability inputs supplied here.

The pure-imaginary proof uses the accepted every-phase [cyclic gauge](Yin_C_F0194_v6.md#phase-line-gauge) and [internal cofactor identity](Yin_C_F0194_v6.md#complex-internal-row), together with its [corank tail](Yin_C_F0194_v6.md#phase-line-rank-tail), [second-smallest floor](Yin_C_F0194_v6.md#phase-line-second-floor), and [restricted isolated-minor estimate](Yin_C_F0194_v6.md#phase-line-isolated-minor).
Those auxiliary inputs include c=i, while the sixth version's main floor does not.
After the verified c=i gauge makes the exposed border real, the [accepted real-border matching proof](Yin_C_F0194_v3.md#two-copy-matching) applies at scale h/N.
The non-purely-imaginary phase-line conclusion is reused only at [the sixth version's main statement](Yin_C_F0194_v6.md#statement).
The skew normal form is classically attributed at the [checked You61 passage](../audits/literature/You61/readme.md), printed p. 694, equations (2)-(3); its complete antilinear proof is supplied here, so no uninspected source proof is a premise.

<a id="generic-envelope-interface"></a>
## Generic complex orientation-envelope near-kernel interface

Fix a complex random variable xi with positive finite variance, a truncation exponent kappa_0>0, and positive constants b,K.
The centered variance-one law needed by the consuming Hermitian argument is a special case.
For each original dimension N let xi_N have the conditional law of xi given |xi|<=N^(kappa_0), and let n be any integer with N/4<=n<=N.
This same xi_N, rather than a new truncation at n, is used throughout the statement.
For each unordered pair {j,k}, take one independent copy z_jk of xi_N.
Choose any deterministic orientation e_jk in {+,-} for j<k, set X_jk=z_jk if e_jk=+ and X_jk=conjugate(z_jk) otherwise, and set X_kj=conjugate(X_jk).
Let D=X+F, where the diagonal of X is deterministic and F is any deterministic complex matrix, with no symmetry requirement on F.
Suppose the diagonal and deterministic shift entries are bounded by n^K.
An independent random diagonal or shift is handled by conditioning on its values inside this bound.

For a deterministic coefficient vector u, a subset J and t>0 define
\[
 \mathcal R_J(u,t)=
 \max_{e\in\{+,-\}^{J}}\sup_{z\in\mathbb C}
 \mathbb P\left\{\left|\sum_{j\in J}u_j\xi_{N,j}^{(e_j)}-z\right|\le t\right\},
 \qquad \xi^{(+)}=\xi,\quad \xi^{(-)}=\bar\xi.
 \tag{Complex-envelope}
\]
For every fixed integer s0>=0 there are fixed a,L,c,C>0, depending only on the law, kappa_0,b,K,s0, such that
\[
 \begin{split}
 \mathbb P\{\exists u\in\mathbb C^n:\ &\|u\|_2=1,
       \ |(Du)_j|\le n^{-L}\text{ on at least }n-s0\text{ rows},\\
       &\mathcal R_{[n]}(u,n^{-a})>n^{-b}\}
       \le C e^{-cn}.
 \end{split}
 \tag{Generic-kernel-AC}
\]
The constants and dimension threshold are uniform over n in the stated range, the deterministic orientation pattern, and the bounded shift and diagonal.
They give the same assertion for D^T, whose orientation pattern is reversed on every edge.
The probability assertion is for any fixed deterministic pattern, not one event simultaneously controlling all possible matrices built from every pattern.
The union over the at most polynomially many omitted-row sets is included in the displayed event.
No independence between real and imaginary parts, conjugation invariance, or centering of xi_N is assumed.

The proof below uses the exact [TV08 complex finite-net theorem and controlled-moment conventions](../audits/literature/TV08/Yin_U001.md#tv08-u001) and [MNV16-U001](../audits/literature/MNV16/Yin_U001.md#matching-rank) at degree one.
The complete new orientation-envelope profile proof is supplied below using block nets, with all mixed-law and scalar-law interfaces justified explicitly.
It does not use NO15's arithmetic clause, a complex extension of Ngu12a, or a matrix least-value theorem.

<a id="generic-uniform-truncation"></a>
### Fixed one-dimensional constants suffice for the truncated family

By TV08 Lemma 2.4 choose a fixed phase e^(i theta) and a fixed kappa_1>=1 such that y=e^(i theta)xi has kappa_1-controlled second moment.
For N sufficiently large, N^(kappa_0)>=kappa_1 and P(|y|<=N^(kappa_0))>=1/2.
Writing y_N for the corresponding conditional law gives, for all complex z,w,
\[
 \begin{split}
 E|y_N|^2&\le2\kappa_1,\\
 E[(\operatorname{Re}(zy_N-w))^2\mathbf1_{\{|y_N|\le\kappa_1\}}]
 &=\frac{E[(\operatorname{Re}(zy-w))^2\mathbf1_{\{|y|\le\kappa_1\}}]}
         {P(|y|\le N^{\kappa_0})}
 \ge\kappa_1^{-1}(\operatorname{Re}z)^2.
 \end{split}
 \tag{Uniform-control}
\]
The integrand is nonnegative, so enlarging its cutoff to 2kappa_1 proves that every y_N has 2kappa_1-controlled second moment.
The fixed phase rotation of the coefficients is an isometry and transfers every finite-net statement back to xi_N.
For a sum using conjugate xi_N, conjugate the whole sum and the coefficients first, and apply the same xi_N statement.
This uses one fixed phase for the entire family, not a dimension-dependent rotation of a Hermitian matrix.
The uniform dependence in TV08 Theorem 3.2 is on this control constant, the chosen epsilon and fixed polynomial concentration ranges; its statement permits beta and p to depend on the dimension.
We use its bound uniformly for m tending to infinity, beta>=exp(-m^(epsilon/2)), and m^(-D)<=p<=1 with each D fixed before that use.

There are fixed d,p_*>0 such that for two independent copies of xi_N,
\[
 P\{|\xi_N-\xi_N'|\ge d\}\ge p_*
 \tag{Uniform-difference}
\]
for every sufficiently large N.
Indeed choose two distinct finite support points of xi and disjoint bounded neighborhoods whose pairwise distance is at least d.
Both neighborhoods have positive probability, and for large N both lie inside the conditioning disk.
Their conditional probabilities are their original probabilities divided by the conditioning probability, so their product has a fixed positive lower bound.
Conjugation preserves the difference modulus.
In particular there are fixed r_0>0 and p_0<1 such that the concentration of either xi_N or its conjugate at radius r_0 is at most p_0.
To see this, two independent variables in the same disk of radius r_0 have difference at most 2r_0; take 2r_0<d and use the square of that disk's probability in (Uniform-difference).

Since N<=4n, the raw amplitudes are bounded by N^(kappa_0)<=n^(kappa_0+1) eventually.
Increase the entry exponent once to a fixed K_0>=max{K+1,kappa_0+1,1}, so all matrix entries, raw amplitudes and fixed shifts used below have modulus at most n^(K_0).
This increase precedes every fine-precision choice.
No approximation of an n-coordinate product law by total variation is used.

<a id="generic-linear-oscillation"></a>
### A degree-one bound supplies the degenerate branch

There are fixed c_0,c_1,C_1>0 such that, for any deterministic complex coefficients u_j and any fixed orientations e_j, if at least k>=2 indices satisfy |u_j|>=lambda>0, then
\[
 \sup_z P\left\{\left|\sum_j u_j\xi_{N,j}^{(e_j)}-z\right|\le c_0\lambda\right\}
 \le C_1\bigl(e^{-c_1k}+k^{-1/2}\bigr).
 \tag{Complex-linear-oscillation}
\]
All constants are uniform in N, the number of variables and their orientations.
Take independent pairs z_j^(0),z_j^(1) with the prescribed oriented laws and independent fair signs epsilon_j.
The variables
\[
 \frac{z_j^{(0)}+z_j^{(1)}}2+
 \frac{z_j^{(0)}-z_j^{(1)}}2\epsilon_j
\]
have exactly those independent original laws.
Among the selected k coordinates, each difference has modulus at least d with probability at least p_*, independently across coordinates.
For the survival count S, the elementary exponential-moment estimate
\[
 P\{S\le p_*k/2\}
 \le e^{p_*k/2}E e^{-S}
 \le \exp\{-[1-e^{-1}-1/2]p_*k\}
\]
is exponentially small.
Outside this event at least p_*k/2 sign coefficients u_j(z_j^(0)-z_j^(1))/2 have modulus at least d lambda/2.
At least half of them have one common real or imaginary projection of modulus at least d lambda/(2sqrt(2)).
Condition on the pairs, choose that projection, and divide the projected linear polynomial by d lambda/(2sqrt(2)).
Its degree-one matching rank in MNV16 is at least p_*k/4.
Choose c_0 sufficiently small that the projected disk becomes an interval of length strictly less than one.
MNV16 Theorem 1.6 at degree one gives C/sqrt(k), since its second bound has no logarithmic factor when d=1.
Enlarge C for bounded ranks and k, then integrate the pairs to prove (Complex-linear-oscillation).
The projected axis may depend on the conditioned pairs because the conditional estimate is uniform and is then integrated.
The scalar-law and uniform difference steps needed by this oscillation estimate have all been supplied above.

<a id="generic-finite-family-count"></a>
### Counting any sufficiently economical deterministic family

Fix C_*>0 and s0, and consider any deterministic finite family V_s of vectors with 1/2<=||u||_2<=2 and
\[
 |V_s|\le n^{C_*n+o_s(n)}.
 \tag{Economical-family}
\]
Here s is a fixed positive precision exponent, the error divided by n tends to zero for each fixed s, and the leading constant C_* is independent of s.
The family may depend on N,n,s and their fixed scalar law, but not on the realized matrix entries.
We prove that for all sufficiently large fixed s,
\[
 P\{\exists u\in V_s:\ |(Du)_j|\le\beta_0=n^{-s}
                 \text{ on at least }n-s0\text{ rows}\}\le Ce^{-cn}.
 \tag{Finite-family-count}
\]
The bound is uniform whenever (Economical-family) and its error are uniform in the stated parameters.

Put epsilon=1/100, delta=epsilon, theta=epsilon/10, q=ceil(n^(1-epsilon)), and t_*=n^(-K_0-5).
For each candidate, move a largest coordinate to the last position by a prescribed permutation.
It has modulus at least 1/(2sqrt(n)), and there are only n such choices.
Every simultaneous row-and-column permutation leaves independent unordered edges and a deterministic orientation pattern of the allowed kind.
For the chosen order write R_i(u,t)=R_[i,n](u,t).
Convolution gives R_J'(u,t)<=R_J(u,t) whenever J is contained in J', because the inequality holds for every fixed orientation and its restriction.
Thus R_i is nondecreasing in i, and every tail containing the largest coordinate has R_i(u,t)<=p_0 for t<=r_0/(2sqrt(n)).

For beta_0<=t<=1, the sum's support lies in a disk of radius O(n^(K_0+1)), uniformly over orientations and candidates.
Covering this disk by O((n^(K_0+1)/t)^2) disks gives R_i(u,t)>=n^(-D_0), with a fixed D_0=O(s+K_0+1).
The same lower bound, after increasing D_0 by a fixed constant, holds for all later rounded candidates, whose coordinate moduli remain at most three.
Expose successive strict upper rows in the chosen order.
At row i the unexposed random part has conditional concentration at most R_(i+1)(u,t); already exposed entries, the diagonal and F change only the center.
For a fixed set of at least n-s0 prescribed rows this gives
\[
 P\{|(Du)_j|\le t\text{ on those rows}\}
 \le n^{D_0(s0+1)}\prod_{i=1}^{n}R_i(u,t).
 \tag{Complex-row-product}
\]
The factor removes at most s0 missing tail factors and R_1, rather than one extra factor for every row.
The direct bound p_0^(n-s0-1) also holds when the last coordinate is large and t is below its fixed concentration scale.

Call u degenerate if every q-subset J satisfies R_J(u,t_*)>=q^(-1/2+theta).
If at least ceil(q/2) coordinates in some such subset have modulus greater than t_*/c_0, (Complex-linear-oscillation) bounds its concentration for every orientation by C(q^(-1/2)+exp(-cq)), which is strictly smaller than q^(-1/2+theta) eventually.
Thus every q-subset has fewer than ceil(q/2) such coordinates, and the entire vector has fewer than ceil(q/2) coordinates above that threshold.
Otherwise one could include ceil(q/2) of them in a q-subset.
Round these coordinates on a complex lattice of mesh t_* and set every other coordinate to zero.
The coordinate error is at most C t_*, and there are at most exp(O_(K_0)(q log n))=exp(o(n)) such rounded vectors, including their support choices.
Their row error is at most C n^(K_0+1)t_*=C n^(-4), and their largest coordinate remains at least 1/(4sqrt(n)).
For s sufficiently large, their enlarged row tolerance is within this coordinate's fixed concentration scale.
The direct p_0 row bound and the subexponential count therefore give Ce^(-cn) for all degenerate candidates.
No orientation labels are counted in this branch: the oscillation inequality holds for every orientation and gives an intrinsic sparse approximation.

For a nondegenerate u choose a q-subset with envelope less than q^(-1/2+theta), include its largest coordinate if needed, and put this reservoir last, with that largest coordinate still last.
Use one prescribed permutation for each reservoir and largest index; their total number is exp(O(q log n))=exp(o(n)).
Let its size be q0 in {q,q+1} and put p=n-q0.
For all i<=p and t<=t_* the tail contains the reservoir, so
\[
 R_i(u,t)\le n^{-b_0},\qquad b_0=1/2-3\epsilon/4.
 \tag{Complex-reservoir}
\]
Indeed (1-epsilon)(1/2-theta)>b_0, so the original q-threshold is below n^(-b_0) eventually.

Choose C_prod>C_*+4.
For each reservoir order apply (Complex-row-product) and (Economical-family) to candidates whose newly ordered full product at beta_0 is less than n^(-C_prod n).
Their total contribution, including the subexponential reservoir choices, is n^(-cn).
This classification is made after the permutation; no product from another order is transferred.
For every remaining candidate,
\[
 \pi_{\beta_0}(u):=\prod_{i=1}^pR_i(u,\beta_0)\ge n^{-C_{\rm prod}n}.
\]
Set A_n=n^(K_0+3), t_l=A_n^l beta_0, and L_*=ceil(C_prod/epsilon)+2.
Choose s sufficiently large that t_(L_*+1)<=t_*.
For at least one l in {0,...,L_*},
\[
 \pi_{t_{l+1}}(u)\le n^{\epsilon n}\pi_{t_l}(u).
 \tag{Complex-stable-scale}
\]
Otherwise iterating the reverse inequalities from the preceding lower bound would make a product of probabilities exceed one.

Fix a scale l and partition the values R_i(u,t_l), i<=p, into intervals [r_h,n^epsilon r_h), with endpoints powers of n, between n^(-D_0) and n^(-b_0).
Monotonicity makes each occupied bin a consecutive block B_h of length m_h.
There are at most H=O_(s,K_0)(1) blocks and at most (n+1)^H profiles.
For each block, its envelope is at least that of the first tail in the block and therefore at least r_h.
Choose an orientation attaining that block envelope and split its coordinates into the two orientation groups.
Convolution gives concentration at least r_h for each group's sum at radius t_l, and conjugating the negative group converts it into a sum with the same scalar law xi_N.
Different blocks need no compatible orientation choices: each block is encoded separately, and the total label count is at most 2^p.

Call an orientation group large if its cardinality m is at least n^(1-delta).
For such a group let sigma be its coefficient norm, which is at most two.
If sigma<t_l use the zero approximation.
Otherwise choose s_sigma as the positive multiple of t_l with s_sigma<=sigma<s_sigma+t_l.
There are O(t_l^(-1)) such bins, and the normalized vector has concentration at least r_h at radius t_l/s_sigma, since this radius is at least t_l/sigma.
The source conditions hold: r_h is m^(-O(1)) and t_l/s_sigma>=t_l/2>=n^(-s)/2>=exp(-m^(epsilon/2)) eventually.
Use the fixed phase conversion from (Uniform-control), apply TV08, undo that phase and the possible conjugation, and multiply the net by s_sigma.
The coordinate approximation error is at most 2t_l, because
\[
 \|\sigma v-s_\sigma w\|_\infty
 \le|\sigma-s_\sigma|\|v\|_\infty
       +s_\sigma\|v-w\|_\infty\le2t_l.
\]
The number of approximants is bounded by
\[
 1+O(t_l^{-1})
 \left[m^{(-1/2+\epsilon)m}r_h^{-m}+\exp(o(m))\right].
 \tag{Complex-block-net}
\]
The one accounts for sigma<t_l.
By r_h<=n^(-b_0) and m<=n, its first term inside brackets is at least
\[
 n^{(b_0-1/2+\epsilon)m}=n^{\epsilon m/4},
\]
so it absorbs both the additive exp(o(m)) term and the zero option eventually.
Since m>=n^(1-delta), its upper bound is
\[
 m^{(-1/2+\epsilon)m}r_h^{-m}
 \le n^{-g m}r_h^{-m},
 \qquad g=(1/2-\epsilon)(1-\delta)>0.48.
 \tag{Complex-block-gain}
\]
The O(t_l^(-1)) factors over at most 2H groups are polynomial in n, with fixed exponents allowed to depend on s.

All small orientation groups together have at most 2H n^(1-delta)=o(n) coordinates.
Round these and the q0 reservoir coordinates directly on a complex lattice of mesh t_l inside their bounded coordinate disks.
Their positions and values cost exp(O_s((H n^(1-delta)+q0)log n))=exp(o(n)).
Combining this with (Complex-block-gain), the 2^p labels and the norm bins gives, for a fixed profile and scale, at most
\[
 \exp(O(n)+o(n))\,n^{-gp}\prod_h r_h^{-m_h}
 \tag{Complex-profile-count}
\]
rounded vectors with coordinate error at most C t_l.
To verify the exponent p rather than just the total M of large-group coordinates, put d=p-M=o(n).
Replacing n^(-gM) by n^(-gp) costs n^(gd)=exp(o(n)), and inserting r_h^(-1)>=1 for the omitted small-group coordinates only increases the bound.

Discard rounded vectors that do not approximate an original candidate in this fixed profile and scale, and select one such original witness for each remaining rounded vector v.
These are deterministic finite choices, made before the random row equations are imposed.
If any original candidate that maps to v satisfies the row constraints, v satisfies them at radius
\[
 t'=\beta_0+C n^{K_0+1}t_l.
\]
Every orientation of every tail sum for v differs from that of its chosen witness by at most C n^(K_0+1)t_l, using the bounded raw variables and coordinate approximation.
For large n the resulting enlarged radius is at most t_(l+1), because A_n=n^(K_0+3).
Taking the maximum over orientations therefore gives
\[
 R_i(v,t')\le R_i(u,t_{l+1})
\]
for that witness u and every i.
The row product, removal of the last q0 factors, (Complex-stable-scale) and the profile upper endpoints bound the probability for v by
\[
 n^{O_(s,K_0,s0)(1)}n^{2\epsilon n}\prod_h r_h^{m_h}.
 \tag{Complex-profile-probability}
\]
Multiplying by (Complex-profile-count) cancels every concentration factor and gives
\[
 \exp(O(n)+o(n))n^{-gp+2\epsilon n}\le n^{-n/3}
\]
eventually, since p=n-o(n) and g>0.48.
The polynomial profiles, bounded scales, subexponential reservoir orders and polynomial omitted-row choices preserve this bound up to a harmless factor.
Combining it with the degenerate and low-product cases proves (Finite-family-count).
The choice order is C_*,K_0,s0 and the fixed numerical epsilon,delta,theta, then C_prod,L_*, then sufficiently large s; H and source polynomial-range constants may depend on this final s but remain fixed as n grows.

<a id="generic-initial-net"></a>
### The initial high-concentration class has economical finite covers

For a fixed fine exponent a set beta=n^(-a) and let H_a be the deterministic set of unit vectors with R_[n](u,beta)>=n^(-b).
Choose an orientation attaining its envelope and split the coordinates into its two groups.
Each group has concentration at least n^(-b) at radius beta by convolution.
Use the same large-group cutoff n^(1-delta), norm bins and phase/conjugation conversion as above, with beta in place of t_l.
For each large group of length m, TV08 and norm binning give
\[
 1+O(\beta^{-1})
 \left[m^{(-1/2+\epsilon)m}n^{bm}+\exp(o(m))\right]
 \le n^{O_a(1)}n^{(b+1)m}
\]
eventually.
Every small group is encoded directly on the beta-grid, at cost n^(O_a(n^(1-delta))).
The 2^n orientation labels, the two norm bin choices and the two group nets therefore produce a deterministic O(beta)-cover of H_a with at most
\[
 n^{(b+1)n+o_a(n)}
 \tag{Complex-initial-cover}
\]
points.
In particular its leading entropy coefficient is independent of a.
For each covering point that is used by H_a choose one unit witness from H_a, and replace that point by its witness.
This at most doubles the approximation constant, preserves the cardinality bound, and yields a finite family V_a of unit vectors with ||u-w||_infinity<=C beta for some w in V_a whenever u belongs to H_a.
The family depends only on the scalar law and dimensions, not on the matrix entries, the diagonal, the shift or the edge pattern.
No measurable selection of actual random kernels is involved.

<a id="generic-near-kernel-proof"></a>
### Parameter conversion and conclusion

Use C_*=b+2 in (Economical-family), retaining the fixed K_0 above.
Choose s sufficiently large for (Finite-family-count), then choose
\[
 a=s+K_0+3,\qquad L=a+1.
\]
The family V_a from (Complex-initial-cover), viewed with this fixed a depending on s, meets (Economical-family); its error is o_s(n) and its leading coefficient is still independent of s.
If a unit u violates (Generic-kernel-AC), then u belongs to H_a and has a deterministic representative w in V_a with coordinate error at most C n^(-a).
On each of its at least n-s0 constrained rows,
\[
 |(Dw)_j|\le n^{-L}+C n^{K_0+1-a}\le n^{-s}
\]
for sufficiently large n.
Thus the violating event is contained in the finite measurable event excluded by (Finite-family-count), proving (Generic-kernel-AC).
The violating event itself is measurable as well.
For each fixed orientation, the closed-disk probability is upper semicontinuous in the unit coefficient vector and its center, by the reverse Fatou inequality; the bounded scalar law restricts relevant centers to a compact disk.
Taking the maximum over that disk and the finitely many orientations shows that every non-strict concentration superlevel set on the unit sphere is compact.
For each prescribed row set, projecting the closed row constraints over such a compact set gives a closed set of matrices, and the strict concentration threshold is a countable union of these sets.
The same argument with all edge orientations reversed proves the D^T version, and a union bound gives simultaneous conclusions for these two fixed matrices if needed.
All uniformity in the comparable sizes n and N comes from (Uniform-control), (Uniform-difference), the common polynomial raw-entry bound and fixed source parameters.
The proof never recenters the conditional law or assumes that its exact variance equals the untruncated variance.

This proves the generic complex linear interface used in the following rank, second-value and isolated-minor arguments.
It applies even to phase-line and pure-imaginary laws, since a kernel's low linear concentration is compatible with a parity-forced singularity.
The non-line quadratic matching, rank-growth, second-value and isolated-minor deductions are proved separately below; the linear interface alone is not a matrix least-value theorem.

<a id="generic-rank"></a>
## Generic corank tails

For these three auxiliary probability sections xi may be any fixed complex law of finite nonzero variance, and zeta is a fixed real finite-second-moment diagonal law independent of the upper entries.
Apply the generic linear interface just proved with s0=0 and the required fixed parameters.
No centering, non-line support or real/imaginary independence assumption is needed in these raw auxiliary deductions.
Then for raw Hermitian Wigner X_n with upper law xi and independent fixed real finite-second-moment diagonal law, every gamma,B>0 admits C,n0 such that
\[
 \sup_{\max|F_{jk}|\le n^\gamma}
 \mathbb P\{\operatorname{rank}(X_n+F)\le n-2\}
       \le Cn^{-B},\qquad n\ge n0.
 \tag{Generic-rank}
\]
The offset is complex and may be nonsymmetric.
The requisite universal kernel estimate is supplied by (Generic-kernel-AC), including its common truncated law and orientation uniformity.

Choose kappa>(B+6)/2 and discard the event that any raw off-diagonal or diagonal variable has modulus greater than n^kappa.
Its probability is at most Cn^(2-2kappa)<=C_B n^(-B-4).
Conditional on the complement the unordered off-diagonal samples remain independent with the single law xi_n; fix the bounded diagonal values by conditioning.
Use one leading-principal chain M_k of this same physical matrix for floor(n/3)<=k<=n.
Because k>=n/4 eventually, a fixed entry exponent K, selected after gamma,kappa, works throughout the chain after a fixed exponent slack.
Apply the proved linear interface to each current block and its transpose with q,b>B+5.

For a singular block D of size k choose Borel unit vectors u in ker D and v in ker D^T by the rank-stratified, lexicographically first maximal-minor construction of [C_F0194_v2](Yin_C_F0194_v2.md#border-rank).
The new raw border has row r^T and column d, with
\[
 r_j=\bar z_j+f_j,\qquad d_j=z_j+g_j,
\]
where z_j are independent xi_n/conjugate-xi_n variables, independent of D.
The actual orientation of the row is the opposite of the column orientation and is also included in the envelope.
Outside the linear exceptional event,
\[
 \mathbb P\{r^Tu=0\mid D\}\le k^{-b},\qquad
 \mathbb P\{v^Td=0\mid D\}\le k^{-b}.
\]
The two forms share the z_j; only their union bound is used.
When both are nonzero the deterministic bordered-rank calculation raises rank by two, independently of the exposed diagonal.
Thus the failure at one singular step is at most 2k^(-b)+Ck^(-q).
Union the at most n steps.
On the good event the deficiency d_k=k-rank M_k falls by one when positive and stays in {0,1} once it reaches that set.
Starting with deficiency at most floor(n/3), enough steps remain to end with corank at most one.
Adding Cn^(1-b)+Cn^(1-q) and the raw cutoff failure proves (Generic-rank).
The normalized version follows from sqrt(n)(W_n+F), with shift exponent at most gamma+1; rank is unchanged.

<a id="generic-second-floor"></a>
## Generic second-smallest floor without a gauge

Use (Generic-kernel-AC) at s0=1.
For every gamma,B>0 there is a finite A_2>0 for which
\[
 \sup_{\max|F_{jk}|\le n^\gamma}
 \mathbb P\{s_{n-1}(X_n+F)\le n^{-A_2}\}\le Cn^{-B}
 \tag{Generic-raw-second}
\]
in raw scaling, and the analogous assertion holds for W_n+F with another fixed exponent.
Here singular values are in decreasing order, so this is the second-smallest value.

Take kappa>(B+6)/2, condition on all independent raw cutoffs and then on the bounded diagonal values, and choose K after gamma,kappa to bound all entries of size-(n-1) principal blocks by (n-1)^K.
Use the linear interface at q,b>B+5 and its fixed precision a.
Let M=X_n+F and let B0 consist of its first n-1 rows.
For a retained row i delete coordinate i from it and from the other retained rows, obtaining z_i and C_i.
Then C_i is D_i=M[[n] minus {i}] with the row of original index n omitted.
The row z_i has only off-diagonal xi_n/conjugate-xi_n samples plus its deterministic shift and is independent of D_i; their mirrored partners were all in the deleted coordinate i.
There is no need to rotate z_i to a real row or to transform the other rows.

Choose a Borel bilinear unit normal u_i to C_i using rank strata, a lexicographically first maximal nonzero minor, the first free coordinate, and normalization.
At rank zero use a coordinate vector.
Then (D_i u_i)_j=0 on all but its one omitted row, exactly within the s0=1 interface.
Outside its D_i-measurable exceptional event, conditioning on D_i gives
\[
 \mathbb P\{|z_i u_i|\le n^{-a}\mid D_i\}
       \le(n-1)^{-b},
\]
because n^(-a)<=(n-1)^(-a) and the row's actual pattern is one allowed orientation assignment in the envelope.
The arbitrary complex offset is a center in that envelope.
For a bilinear normal u_i, the Hilbert-space normal is bar u_i and Cauchy--Schwarz yields
\[
 \operatorname{dist}(z_i,\operatorname{rowspan}C_i)\ge|z_i u_i|.
\]
Coordinate deletion is a contraction, so the same lower bound applies to the full retained row's distance from the other retained rows.
Its failure probability is at most (n-1)^(-b)+C(n-1)^(-q).
Union the n-1 retained rows.

On their good event B0 has full row rank.
The Schur complement identifies the i-th diagonal entry of (B0 B0*)^(-1) with the reciprocal squared row distance, and taking its trace gives
\[
 \sum_{j=1}^{n-1}s_j(B0)^{-2}
    =\sum_{i=1}^{n-1}\operatorname{dist}((B0)_i,
                      \operatorname{rowspan}(B0)_{-i})^{-2}
    \le n^{2a+1}.
\]
Thus s_(n-1)(B0)>=n^(-a-1/2).
Adding the final row is a positive-semidefinite Gram perturbation, so s_(n-1)(M) has the same bound.
Choose A_2>a+1/2 and restore the cutoffs; q,b>B+5 give the claimed arbitrary-power error.
For normalized scaling, multiply W_n+F by sqrt(n), use raw shift exponent gamma+1, and divide singular values by sqrt(n).
The resulting statement applies to every actual principal minor by the comparable-dimension conversion and a probability margin for their union.

<a id="generic-isolated-minor"></a>
## Generic isolated-minor estimate with the correct conjugate forms

Use (Generic-kernel-AC) at s0=0.
For raw size n, fixed gamma,B>0 and arbitrary complex shift entries bounded by n^gamma, there are finite A_0,L_iso>0 for which the probability is at most C_B n^(-B) that some actual minor D_i has nonzero adjugate, the full ratio satisfies
\[
 |\det M|/\|\operatorname{adj}D_i\|_F\le n^{-A_0},
\]
and D_i is either exactly corank one or is invertible with
\[
 t_1(D_i)\le n^{-L_{\rm iso}},\qquad
 t_1(D_i)/t_2(D_i)\le n^{-L_{\rm iso}}.
 \tag{Generic-isolated}
\]
Here t_1<=t_2 are the two smallest values.

Choose kappa>(B+6)/2, then K bounding the diagonal, both shifted raw border norms and every entry on the independently truncated event.
Use q,b>B+5 in the linear interface, producing a_lin,L_ker uniformly for size m=n-1, D_i and D_i^T with the same law xi_n.
Choose a0>a_lin+1, set A_0=2a0, and then choose
\[
 L_{\rm iso}>\max\{L_{\rm ker}+1,\ 2a0+2K+3\}.
\]
All these exponents are fixed before the actual minor or border is exposed.

For clarity, the singular-vector directions can be checked explicitly over C.
For invertible D_i=U diag(t_1,...,t_m)V^*, set u=Ve_1 and v=bar Ue_1.
Then
\[
 D_i u=t_1Ue_1,\qquad D_i^Tv=t_1\bar Ve_1,
 \qquad
 \frac{\operatorname{adj}D_i}{\|\operatorname{adj}D_i\|_F}
       =\alpha uv^T+E,
\]
where
\[
 |\alpha|=\left(1+\sum_{j\ge2}(t_1/t_j)^2\right)^{-1/2}\ge1/2,
 \qquad \|E\|_F\le\sqrt m\,t_1/t_2,
 \qquad\rho_{D_i}\le t_1.
\]
The amplitude bound holds for sufficiently large n under the isolation hypothesis.
For exactly corank-one D_i, its normalized adjugate has exact rank one, take |alpha|=1,E=0, and u in ker D_i, v in ker D_i^T.
There is no assertion that the two singular vectors have overlapping coordinate mass or that a transpose-left vector equals a Hermitian left vector.

In the raw bordered determinant formula the rank-one contribution is
\[
 -\alpha\,[u^T(\bar z+f)]\,[v^T(z+g)],
 \tag{Generic-two-forms}
\]
where z has independent xi_n/conjugate-xi_n coordinates and f,g are arbitrary deterministic shifts.
The first form uses the opposite scalar orientation from the second, and both are covered by the full orientation envelope.
After division by the minor adjugate norm, its error is at most
\[
 n^K t_1+n^{2K}\sqrt m\,t_1/t_2
\]
in the invertible branch and zero in the exactly singular branch.
The choice of L_iso makes the error at most n^(-2a0-1) eventually.
Hence the tiny-full-ratio event forces at least one of the two factors in (Generic-two-forms) to have modulus at most 2n^(-a0).

Their vectors satisfy the right and transpose-right near-kernel conditions of the linear input, with residual at most n^(-L_iso), hence below m^(-L_ker).
Outside the minor's linear exceptional events, their conditional concentrations at radius 2n^(-a0)<=m^(-a_lin) are each at most m^(-b).
They use the same raw samples and may be strongly dependent; the union bound gives conditional probability at most 2m^(-b).
For each fixed minor this bound is uniform over every admissible singular-vector choice, so no random vector is being fixed before its matrix is exposed.
Equivalently a Borel SVD selection may be used.
Integrate the exceptional probability C m^(-q), union n indices, and restore the global cutoff event.
This proves the isolated-minor estimate, with no quadratic inverse theorem and no independence assumption inside one entry.
All three generic auxiliary probability estimates also hold for an independent random offset on its polynomial entry guard, by conditioning within this dimension and integrating the uniform deterministic estimate; add that guard failure for the unguarded event.


<a id="cofactor-average"></a>
## Complex rectangles and the deterministic cofactor average

Return to a centered variance-one complex upper law xi and the normalized model M=W_N+F, with arbitrary deterministic complex offset, and put D_i=M[[N] minus {i}].
The [fixed complex-distance input](Yin_C_F0194_v6.md#complex-distance) applies to independent raw coordinates whose law is xi or its conjugate, uniformly over all affine centers and complex subspaces of proportional codimension.
For a support J of k=floor(delta N) coordinates and I its complement, the raw cross-rectangle sqrt(N)M[I,J] has independent columns and independent coordinates within each column, with these orientations.
Condition on the other columns.
Their span has complex codimension at least N-2k+1 in the N-k output coordinates, so each raw column has distance at least c sqrt(N) from the other columns outside probability C exp(-cN), uniformly for delta<=1/10.
The negative-second-moment Gram identity bounds its least singular value below by a fixed positive constant; after normalization the cross-rectangle floor is a/sqrt(N).
Union the k columns and then the at most exp(2delta N log(e/delta)) supports, choosing delta small after the fixed distance exponent.
This gives all the cross-rectangle floors outside C exp(-cN).
These are exactly the column-distance, Gram and support-entropy steps of the accepted [rectangle argument](Yin_C_F0194_v3.md#rectangles), now with its complex-coordinate input verified.

The [deterministic row-adjugate inequality](Yin_C_F0194_v3.md#row-adjugate) and [pointwise spread proof](Yin_C_F0194_v3.md#spread-and-average) then give constants a,delta,C_1>0 for the following events, with A_i=adj D_i:
\[
 \begin{split}
 E_N(K,\varepsilon)&=\{\|M\|\le N^K,\ \operatorname{rank}M\ge N-1,
          \ s_{\min}(M)\le\min(\varepsilon,a/(4\sqrt N))\},\\
 G_i(K,\varepsilon)&=\{A_i\ne0,\ \|M\|\le N^K,
          \ |\det M|/\|A_i\|_F\le C_1N^{2K+1}\varepsilon\}.
 \end{split}
\]
Outside the common rectangle exception, E_N forces at least delta N/2 of the G_i.
The proof uses a right least-singular vector, or a right kernel vector at exact corank one, and the adjugate-row inequality; it requires neither left-right coordinate overlap nor a singular-value gap.
Consequently
\[
 \mathbb P(E_N(K,\varepsilon))\le Ce^{-cN}
       +\frac{2}{\delta N}\sum_{i=1}^N\mathbb P(G_i(K,\varepsilon)).
 \tag{Complex-cofactor-average}
\]
The same pointwise inequality remains valid after intersecting every event with any common guard.
No independence between principal-minor events or between a common guard and the noise is used.


<a id="nonline-full-adjugate-scope"></a>
## Full-adjugate matching for a non-line complex law

This part considers a fixed centered complex law xi with E|xi|^2=1 whose support is not contained in a real line through zero.
In this module W_N has independent strict upper entries xi/sqrt(N), conjugate lower entries and independent real diagonal entries zeta/sqrt(N), for a fixed finite-second-moment law zeta; the diagonal and upper families are independent.
An offset F is deterministic and complex with no symmetry requirement, unless an independent random-offset form is stated explicitly.
Its linear interface is the generic complex count above, rather than a real-scalar phase-line inverse theorem.
The bounded result is a complete quadratic matching estimate using the full adjugate, together with a low-matching actual-minor ratio implication that needs no symmetric-part floor.
The needed complex-distance estimate is the [reviewed fixed-cutoff auxiliary assertion](Yin_C_F0194_v6.md#complex-distance), whose scope includes arbitrary centered variance-one complex laws and coordinatewise conjugation.
The matching source is [MNV16-U001](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) at its exact original real-coefficient fair-sign degree-two scope, with its recorded source-proof inspection limits.
All support, coefficient, column-exposure and probability arguments for this part are supplied below.

<a id="nonline-difference-edge"></a>
## Two noncollinear difference values control every ordered coefficient pair

Let delta=xi-xi' for independent copies.
There are a,b in its topological support such that a is nonzero and Im(bar a b) is nonzero.
Indeed, if the support of delta were contained in a real line L, the real orthogonal projection of xi-xi' onto L^perp would vanish almost surely.
Independence and finite second moment would then give zero variance for that projection of xi.
Centering would make the projection zero, implying xi belongs to L almost surely, contrary to the hypothesis.
Thus the difference support is not contained in any real line, which supplies such a,b.

There are fixed kappa,p>0, depending only on xi, with the following uniform assertion.
Let delta_s and delta_t be independent, each having either the law of delta or its conjugate, in any fixed orientations s,t.
For all u,v in C,
\[
 \mathbb P\{|\bar\delta_s u\delta_t
                 +\bar\delta_t v\delta_s|
                  \ge\kappa\max(|u|,|v|)\}\ge p.
 \tag{Full-edge-survival}
\]
To prove this, put alpha=s(a), beta_1=t(a), beta_2=t(b), where each orientation is either identity or conjugation.
The two coefficient forms at these support values have matrix
\[
 L_{s,t}=\begin{pmatrix}
 \bar\alpha\beta_1&\bar\beta_1\alpha\\
 \bar\alpha\beta_2&\bar\beta_2\alpha
 \end{pmatrix},
 \qquad
 \det L_{s,t}=|a|^2(\beta_1\bar\beta_2-\beta_2\bar\beta_1)\ne0.
\]
The determinant has absolute value 2|a|^2|Im(bar a b)| in all four orientation cases.
Consequently, with kappa_0=min_(s,t) s_min(L_s,t)/sqrt(2)>0 and M=max(|u|,|v|), at least one of the two forms has modulus at least kappa_0 M.
Choose a fixed sufficiently small epsilon>0 so that replacing alpha and beta_l by points within epsilon changes that form by at most kappa_0 M/2.
For example the error is bounded by 2epsilon(|a|+max(|a|,|b|)+epsilon)M.
Both support-ball probabilities p_a=P(|delta-a|<epsilon) and p_b=P(|delta-b|<epsilon) are positive.
The event of the selected pair of balls has probability at least p_a min(p_a,p_b), uniformly in the orientations and in u,v.
Take kappa=kappa_0/2 and p=p_a min(p_a,p_b).
The case M=0 also satisfies the displayed assertion.
This proves the bound without a density, an atom-size bound or independence of the real and imaginary parts.

<a id="nonline-full-matching"></a>
## The actual complex border has a full-adjugate matching estimate

Let M=W_N+F be the normalized Hermitian Wigner matrix with fixed upper law xi and an arbitrary deterministic complex shift.
Fix one omitted index i, condition on its actual principal minor D_i and exposed diagonal a_i, and write A_i=adj D_i.
After placing i first the raw lower column z has independent xi/conjugate-xi coordinates and is independent of this conditioning.
The bordered determinant identity is
\[
 \det M=a_i\det D_i-(z^*/\sqrt N+f^T)
                           A_i(z/\sqrt N+g),
\]
where f,g are arbitrary fixed complex offsets under the conditioning.
Its quadratic part is -z^*A_i z/N.
The identity holds for singular minors by polynomial continuity.

For h>0 define an undirected graph on the minor coordinates by an edge jk, j!=k, when
\[
 \max(|(A_i)_{jk}|,|(A_i)_{kj}|)\ge h\|A_i\|_F.
 \tag{Full-adjugate-graph}
\]
Let H_i^(full)(h,r) require A_i nonzero and a matching of at least r edges.
The Frobenius norm here is that of the full actual adjugate; no symmetric-part normalization is substituted.
There are c_*,C>0, depending only on xi, such that for every r>=2,
\[
 \mathbb P\left\{
    |\det M|/\|A_i\|_F\le c_*h/N
                \;\middle|\;D_i,a_i\right\}
 \le C\left[e^{-c_*r}+\sqrt{\log(2+r)}\,r^{-1/9}\right]
 \tag{Full-adjugate-matching}
\]
on H_i^(full)(h,r), uniformly over the conditional minor, diagonal, center and offsets.

Here is the complete reduction to the accepted real-sign theorem.
Choose a deterministic lexicographically first r-edge matching in the graph, conditional on D_i.
For every raw oriented coordinate take two independent copies z_j^(0),z_j^(1) and an independent fair sign epsilon_j, with all these families independent, and write
\[
 z_j=\frac{z_j^{(0)}+z_j^{(1)}}2
                +\frac{\delta_j}2\varepsilon_j,
 \qquad \delta_j=z_j^{(0)}-z_j^{(1)}.
\]
This represents the original independent coordinate law exactly.
For an edge jk the coefficient of epsilon_j epsilon_k in the determinant is
\[
 -\frac{\bar\delta_j(A_i)_{jk}\delta_k
               +\bar\delta_k(A_i)_{kj}\delta_j}{4N}.
 \tag{Full-sign-coefficient}
\]
The factor 1/4 comes from the two half-differences, and 1/N from normalized Wigner entries.
The difference orientations are precisely those in (Full-edge-survival).
Hence each selected edge has coefficient modulus at least kappa h||A_i||_F/(4N) with probability at least p.
These survival events are independent across the disjoint edges, since they use disjoint two-copy endpoint pairs.
A Chernoff bound leaves at least pr/2 surviving edges outside probability C exp(-cr), with fixed positive c, for sufficiently large r.

Conditional on all two-copy values, choose a common projection pi equal to real part or imaginary part that retains at least half the surviving edges at modulus loss at most sqrt(2).
This choice depends on the two-copy values, not on the remaining fair signs.
The projected determinant is a real polynomial of those independent signs.
Every diagonal term is affine in its single sign, since epsilon_j^2=1, including when its original coefficient was complex.
It is therefore multilinear of degree at most two, with at least pr/4 disjoint quadratic monomials of modulus at least
\[
 \lambda_N=\frac{\kappa h\|A_i\|_F}{4\sqrt2 N}.
\]
Choose c_*<kappa/(16sqrt(2)), decreased also to fit the survival exponent.
The event |det M|<=c_*h||A_i||_F/N places pi(det M)/lambda_N in an interval of length strictly less than one.
The exact MNV16 degree-two theorem then gives C sqrt(log(2+r))r^(-1/9), with unrestricted lower-degree terms and center.
The finitely many small r and the requirement that the retained source rank be at least two are absorbed by increasing C.
Integrating the two-copy values and adding their exponential failure proves (Full-adjugate-matching).
This conditional estimate uses the non-line hypothesis only through (Full-edge-survival).

<a id="full-adjugate-low-matching"></a>
## Low full-adjugate matching excludes a large uncovered diagonal

The next lemma holds for every fixed centered variance-one complex law, including line-supported laws.
The non-line hypothesis is unnecessary for this low-matching half.
Let D be an actual m-by-m shifted Hermitian Wigner minor normalized by sqrt(N), with m in [N/2,N], fixed independent real diagonal law of finite second moment, and an arbitrary deterministic complex shift.
For this local lemma the shift need not have a prescribed bound; retain the event ||D||<=N^K for a fixed K>=0.
Write A=adj D and use the full-adjugate graph (Full-adjugate-graph).
Fix J>=0 and H>J+K+1, and let r_N>=2 have r_N log(N)=o(N).
There are fixed c,C>0 such that the probability is at most C exp(-cN) that some I subset of [m], |I|<2r_N, and some j outside I satisfy
\[
 \begin{split}
 &A\ne0,\quad\|D\|\le N^K,\qquad
       |A_{jj}|\ge N^{-J}\|A\|_F,\\
 &|A_{ab}|<N^{-H}\|A\|_F
            \quad(a\ne b,\ a,b\notin I).
 \end{split}
 \tag{Full-large-diagonal}
\]
The constants are independent of the deterministic shift and of m,N, and the sufficiently large N may depend on the fixed exponents and the sequence r_N.
There is no symmetric-part guard or exceptional polynomial-floor term in this bound.

Fix I,j and condition on B=D with row and column j removed.
The event in question requires det B=A_jj nonzero and ||B||<=N^K; otherwise it is empty.
The exact adjugate column formula, valid polynomially before division, gives
\[
 \frac{A_{-j,j}}{\det B}
       =-B^{-1}(z/\sqrt N+g),
\]
where z has independent raw xi/conjugate-xi coordinates and is independent of B, and g is the fixed lower-column shift.
The exposed upper row, its possibly different shift, and the diagonal at j do not enter this identity.
Put R=B^(-1); then s_min(R)=1/||B||>=N^(-K).
For U=[m] minus (I union {j}), p=|U|=m-|I|-1, the principal block R_UU has at least p-|I| singular values at least N^(-K).
Indeed ker R_IU has dimension at least p-|I|, and on that kernel the full-column lower bound for R is the lower bound for its U-row projection.
For large N, p>=N/3 and p-|I|>=p/2.

Condition also on z_I.
The remaining z_U retain their independent oriented law, and the large-diagonal and small-column conditions force
\[
 \left\|R_{UU}z_U+w\right\|
       \le\sqrt{Np}\,N^{J-H},
\]
for a fixed conditional center w, after multiplying by sqrt(N).
Take at least p/2 left singular directions with singular values at least N^(-K), project the center onto them, and divide their coordinates by the corresponding singular values.
These directions and the affine center may be chosen Borel by the spectral projection above that fixed threshold and its pseudoinverse; ties may all be retained.
The event then forces z_U to lie within
\[
 \sqrt p\,N^{J-H+K+1/2}
\]
of a fixed complex affine subspace of codimension at least p/2.
Since H>J+K+1, this is below the fixed c sqrt(p) distance threshold eventually.
The [reviewed complex fixed-cutoff distance estimate](Yin_C_F0194_v6.md#complex-distance) bounds its conditional probability by C exp(-cp), uniformly over B,z_I and the center.
The norm and adjugate conditions were used only to imply this linear event and need not hold on the larger event to which the distance estimate is applied.
Integrate the conditioning, including the unused exposed diagonal, and union the at most N^(2r_N+2)=exp(o(N)) choices of I,j.
This proves the exponential assertion.

<a id="full-adjugate-hub-ratio"></a>
## A hub approximation now needs only D times adj D

On the complement of the last exceptional event, suppose A is nonzero, ||D||<=N^K and the full-adjugate graph at h=N^(-H) has matching size less than r_N.
The endpoints I of a maximal matching give |I|<2r_N and all uncovered off-diagonal entries of A smaller than N^(-H)||A||_F.
Every uncovered diagonal is smaller than N^(-J)||A||_F by (Full-large-diagonal).
Split A=A_hub+E, where A_hub equals A on all rows or columns in I and is zero elsewhere.
Then
\[
 \operatorname{rank}A_{\rm hub}\le2|I|<4r_N<m,
 \qquad
 \|E\|_F\le e_N\|A\|_F,
 \quad e_N=\sqrt m\,N^{-J}+mN^{-H}.
\]
No fixed central strip is added and no symmetry of A or D is assumed.
The exact identity DA=(det D)I implies, at the first singular-value index beyond rank(D A_hub),
\[
 |\det D|\le\|DE\|
       \le N^K e_N\|A\|_F.
\]
Consequently
\[
 \rho_D:=\frac{|\det D|}{\|A\|_F}
       \le N^K\bigl(\sqrt m\,N^{-J}+mN^{-H}\bigr),
 \qquad s_{\min}(D)\le\sqrt m\,\rho_D.
 \tag{Full-low-ratio}
\]
For invertible D the last inequality follows from rho_D=(sum_l s_l(D)^(-2))^(-1/2).
For singular D with A nonzero both sides in that last inequality are zero.
This argument uses neither s_min(sym D) nor any other floor for a symmetric part.

For any prescribed T_0>0 choose
\[
 J>K+T_0+1,\qquad
 H>\max\{J+K+1,\ K+T_0+2\}.
 \tag{Full-threshold-order}
\]
Then rho_D<=N^(-T_0) eventually on the retained norm and low-matching events, outside probability C exp(-cN).
The choice is made after the desired precision and the norm exponent; there is no new floor exponent to be chosen first.
For all N actual principal minors D_i in one full matrix these implications hold simultaneously outside C exp(-c'N), by a further union over the omitted index.
They are uniform over deterministic shifts; conditioning on an independent random shift within this dimension gives the same norm-guarded assertions.

<a id="nonline-floor"></a>
## Full non-line in-probability floor

Use the generic linear theorem proved above, at each required fixed cutoff, s0=0,1, and all requested b,q,K, for the centered variance-one non-line law xi.
Then for every gamma,B>0 there are fixed A,C_B,C,N0 such that, for the original normalized Hermitian model,
\[
 \sup_{\max|F_{jk}|\le N^\gamma}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C_BN^{-B}+C\sqrt{\log(2+N)}\,N^{-1/18},
       \qquad N\ge N0.
 \tag{Nonline-floor}
\]
The complete generic linear argument is included in this candidate; no unresolved Draft input is selected as its premise.
The offset is arbitrary deterministic complex and may vary with N; for an independent random offset the same estimate holds on its polynomial entry guard, adding the guard failure for an unconditional event.
Only within-size independence is used.
No summability, full-sequence almost-sure floor or original Task completion is claimed.

Here is the complete parameter order.
First choose the raw cutoff kappa>(B+6)/2 and a fixed norm exponent K>max{kappa+1/2,gamma+1}, enlarged to absorb constants.
The ordinary finite-second-moment cutoff gives P(||M||>N^K)<=C_B N^(-B-2), with M=W_N+F.
The generic rank theorem at failure exponent B+2, applied to sqrt(N)M, makes rank M>=N-1 outside the same order of polynomial failure.
The reviewed [complex fixed-distance input](Yin_C_F0194_v6.md#complex-distance) and the deterministic [row-adjugate, rectangle and spread proof](Yin_C_F0194_v3.md#spread-and-average) therefore give the usable-index average for the remaining event.
This step uses the original untruncated centered law xi for its rectangular distance bound; the separate rank, second-value and isolated modules restore their own cutoff failures.

Apply the generic second-value theorem to all raw actual principal minors sqrt(N)D_i, whose shifts are bounded by N^(gamma+1/2)<= (N-1)^(gamma+2) eventually.
Choose its failure exponent with margin for the N-minor union.
There is a fixed L_2>0 outside probability C_B N^(-B-1) on which t_2(D_i)>=N^(-L_2) for every i.
Choose A_0,L_iso from the generic raw isolated-minor theorem with shift exponent gamma+1 and failure exponent B+2.
These are chosen before the fine full-adjugate graph threshold.

Now choose
\[
 T_0>L_{\rm iso}+L_2+2,\qquad
 J>K+T_0+1,\qquad
 H>\max\{J+K+1,\ K+T_0+2\},
\]
and put h_N=N^(-H),r_N=floor(sqrt(N)).
The full-adjugate low-matching proof holds simultaneously for all actual minors outside C exp(-cN), since r_N log(N)=o(N).
On the retained norm guard, a nonzero-adjugate low-matching minor has rho_Di<=N^(-T_0), hence t_1(D_i)<=sqrt(N-1)N^(-T_0).
If it is invertible, the raw isolation thresholds follow from
\[
 t_1(\sqrt N D_i)\le N^{-T_0+1},\qquad
 \frac{t_1(\sqrt N D_i)}{t_2(\sqrt N D_i)}
      \le N^{-T_0+1/2+L_2}\le N^{-L_{\rm iso}}
\]
eventually, and the first bound is also at most N^(-L_iso).
If it is singular with nonzero adjugate, it is exactly corank one and already lies in the singular isolated branch.
No symmetric-part floor, Riccati inversion or left-right support comparison enters this deduction.

Finally choose A>max{H+2K+2,A_0+2K+2,1} and epsilon_N=N^(-A).
The usable-index event G_i bounds the normalized full ratio by C_1N^(2K+1-A), which is within the full-adjugate matching radius c_*h_N/N eventually.
For the raw isolated-minor event its exact ratio is
\[
 \frac{|\det(\sqrt N M)|}
      {\|\operatorname{adj}(\sqrt N D_i)\|_F}
      =N\frac{|\det M|}{\|A_i\|_F}
      \le C_1N^{2K+2-A}\le N^{-A_0}
\]
eventually.
The factor is N, because the raw numerator has degree N and the raw minor adjugate has degree N-2.

Split the usable-index average into H_i^(full)(h_N,r_N) and its complement.
The high-matching contribution is at most C psi(r_N) by the new complete two-copy matching estimate, with no factor N.
On the norm, second-value and low-matching guards, every remaining G_i forces one of the generic raw isolated-minor events.
The probability of the union of those events is at most C_B N^(-B-2), and their mean probability is no larger than this union bound.
Adding all rank, norm, second-value and low-matching failures yields
\[
 \mathbb P\{s_{\min}(M)\le N^{-A}\}
       \le C_BN^{-B}+C\psi(\lfloor\sqrt N\rfloor),
\]
which is (Nonline-floor).
All constants and all precision exponents are fixed after the laws and requested exponents, before N or the offset realization, and no independence between different dimensions was used.

This completes the non-line least-value argument with its generic linear input proved in the same candidate.
It requires no independence between the real components of an entry and no additional covariance hypothesis beyond the stated non-line support for the full-adjugate matching half.


<a id="phase-line-reuse"></a>
## The non-purely-imaginary phase-line branch is an accepted input

If the centered variance-one law is supported on a real line through zero, write xi=c eta with |c|=1 and eta a centered variance-one real law.
For Re c nonzero, the complete [reviewed C_F0194_v6 main theorem](Yin_C_F0194_v6.md#statement) supplies the same in-probability least-value rate under arbitrary polynomially bounded complex shifts and the stated independent random-shift guard.
That main result is reused directly and is not reproved here.
For the purely imaginary line choose c=i by changing the sign of the real amplitude if needed.
The C_F0194_v6 main floor is not applied in that case; only its explicitly every-phase auxiliary results are used in the guarded and skew arguments below.


<a id="pairing-source"></a>
## Classical source and inspected scope

[You61 and its inspected edition](../audits/literature/You61/readme.md) supply a checked primary reference for the classical skew form.
The selected 1961 original is actually retained as [the local PDF](../literature/pdf/You61--CJM.pdf).
Printed p. 694 / PDF p. 1, introduction equations (2)-(3), was read in text and visually from that retained page.
It states unitary congruence of any complex transpose-skew matrix to blocks \(\begin{pmatrix}0&\sigma\\-\sigma&0\end{pmatrix}\), with \(\sigma>0\), and zeros, and records its even rank.
Both congruence factors are unitary, so the displayed blocks give paired positive singular values.
This is attribution for a classical fact, not a novelty claim or a claimed inspection of the entire source proof.
The following self-contained proof is the mathematical argument used here.

<a id="singular-pairing"></a>
## A short antilinear proof covering complex skew matrices

Let \(A\in M_n(\mathbb C)\) satisfy \(A^T=-A\).
No Hermitian or normal hypothesis is imposed.
Write \(C\) for coordinatewise conjugation and \(T=AC\) for the resulting antilinear map.
Since \(A^*=-\overline A\),
\[
 T^2=A\overline A=-AA^*=-H,\qquad H=AA^*\ge0.
\]
Consequently \(T\) commutes with \(H=-T^2\) as real-linear maps.
For each positive eigenvalue \(\lambda\) of \(H\), its complex eigenspace \(E_\lambda\) is therefore invariant under \(T\), and
\[
 (T|_{E_\lambda})^2=-\lambda I.
\]
If \(m=\dim_{\mathbb C}E_\lambda\), write the restriction in a complex basis as \(v\mapsto S\overline v\).
Then
\[
 S\overline S=-\lambda I_m,\qquad
 |\det S|^2=(-\lambda)^m.
\]
The first equation makes \(S\) invertible, so the left side is positive and \(m\) must be even.
Every positive eigenvalue of \(AA^*\), hence every positive singular value of \(A\), has even multiplicity.
Its rank is even, and if \(n\) is even its zero singular value also has even multiplicity.
Writing singular values decreasingly, for even \(n\),
\[
 s_{2j-1}(A)=s_{2j}(A)\quad(1\le j\le n/2),
 \qquad s_n(A)=s_{n-1}(A).
 \tag{Skew-pairing}
\]
For odd \(n\), even rank forces \(s_n(A)=0\).
Equivalently odd-dimensional skew matrices have zero determinant by transposing it.

<a id="even-floor"></a>
## Arbitrary-power floor deduction on even dimensions

Fix a real law \(\eta\) with \(\mathbb E\eta=0\) and \(\mathbb E\eta^2=1\), and let \(W_N\) have upper entries \(i\eta_{jk}/\sqrt N\), conjugate lower entries, and identically zero diagonal.
The upper amplitudes are independent.
Every realization has \(W_N^*=W_N\) and \(W_N^T=-W_N\).
Let \(F\) be any deterministic complex transpose-skew matrix satisfying \(\max|F_{jk}|\le N^\gamma\).
It need not be Hermitian.
Then \(M_N=W_N+F\) is complex skew and, on even dimensions, (Skew-pairing) identifies its least and second-smallest singular values exactly.
Thus the adopted auxiliary statement gives the following deduction: for every \(\gamma,b>0\), some fixed \(A,C,N_0\) satisfy
\[
 \sup_{\substack{F^T=-F\\\max|F_{jk}|\le N^\gamma}}
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A}\}
 \le C N^{-b},
 \qquad N\ge N_0,\quad N\ \mathrm{even}.
 \tag{Even-skew-floor}
\]
Only the adopted auxiliary second-floor statement is used, not the unavailable purely imaginary main least-value theorem.
For independent random skew \(F_N\), the same bound holds on its polynomial entry guard by within-dimension conditioning, and the guard complement is added otherwise.
Every odd-dimensional \(W_N+F_N\) is singular, without a probability exception.
No floor for arbitrary nonskew \(F\) follows from this pairing identity.

<a id="quantile-guard-floor"></a>
## A uniform all-dimension floor on a symmetric-quantile guard

Now let \(W_N\) have independent upper entries \(i\eta_{jk}/\sqrt N\), conjugate lower entries, and independent real diagonal entries \(\zeta_j/\sqrt N\).
Here \(\eta\) is centered with variance one, and \(\zeta\) is any fixed real law with finite second moment, independent of the off-diagonal family.
Centering of \(\zeta\) is not needed for this floor lemma.
Fix \(\gamma,L_0,b>0\), let \(F\) be deterministic with \(\max|F_{jk}|\le N^\gamma\), and put \(M=W_N+F\).
For every omitted index \(i\), define
\[
 D_i=M[[N]\setminus\{i\}],\quad
 A_i=\operatorname{adj}D_i,\quad
 S_i=\operatorname{sym}D_i
   =\operatorname{diag}(\zeta_j/\sqrt N)_{j\ne i}
      +\operatorname{sym}F_i.
\]
Use decreasing singular values, put \(r_N=\lfloor\sqrt N\rfloor\), \(k_N=4r_N+1\), and define the exact guard
\[
 \Sigma_N(F,L_0)
 =\bigcap_{i=1}^N
     \{s_{k_N}(S_i)\ge N^{-L_0}\}.
 \tag{Symmetric-quantile-guard}
\]
For all sufficiently large \(N\), \(k_N\le N-1\).
The complete candidate deduction is that some fixed \(A,C_b,C,N_0\), depending only on the laws and displayed exponents, satisfy
\[
 \mathbb P\{s_{\min}(W_N+F)\le N^{-A},\ \Sigma_N(F,L_0)\}
 \le C_bN^{-b}
       +C\sqrt{\log(2+N)}N^{-1/18},
 \qquad N\ge N_0.
 \tag{Quantile-guard-floor}
\]
The constants are uniform over the entire displayed class of deterministic complex shifts.
There is no parity restriction.

<a id="quantile-guard-failure"></a>
For a random shift \(F_N\) independent of \(W_N\), define
\[
 \Gamma_N=\{\max|F_{N,jk}|\le N^\gamma\},
 \qquad
 \varepsilon_N^{\rm guard}
   =\mathbb P\bigl(\Gamma_N^c\cup
             \Sigma_N(F_N,L_0)^c\bigr).
 \tag{Guard-failure}
\]
Within-dimension conditioning gives the same right side plus \(\varepsilon_N^{\rm guard}\) for the unguarded least-value probability.
This permits an arbitrary random complex matrix shift, including a fixed polynomial of other independent inputs.
It does not condition on the guard itself and requires no independence between that guard and \(W_N\).

<a id="pure-imaginary-weighted-gauge"></a>
### The correct graph and the symmetric guard survive the gauge

Use the exact C_F0194_v6 cyclic gauge with \(c=i\).
Its diagonal phase matrix is \(Z_i=iE_i\), where \(E_i\) is real diagonal with signs, and \(U_i=Z_iP_i=iO_i\), where \(O_i=E_iP_i\) is real monomial orthogonal.
Consequently
\[
 \widehat D_i=U_i^*D_iU_i=O_i^TD_iO_i,\qquad
 \operatorname{sym}\widehat D_i=O_i^TS_iO_i.
 \tag{Pure-imaginary-gauge}
\]
All singular quantiles in \(\Sigma_N\) are preserved exactly.
The gauge also preserves the full determinant, the minor determinant, all singular values and the adjugate Frobenius norm.
The accepted cyclic calculation, not a symmetry assumption on the amplitude law, shows that \(\widehat D_i\) again has upper law \(i\eta/\sqrt N\) and the same independent diagonal law.

The correct outer quadratic coefficients are
\[
 Q_i^{\rm wt}=\operatorname{sym}(Z_i^*A_iZ_i)
     =E_i\operatorname{sym}(A_i)E_i,\qquad
 \widehat Q_i=P_i^TQ_i^{\rm wt}P_i
     =\operatorname{sym}(\operatorname{adj}\widehat D_i).
\]
Thus in this pure-imaginary case the absolute weighted edge values equal the original absolute sym-adjugate entries, up to permutation.
We nevertheless keep the gauge, because its exposed upper and lower borders are the same iid real \(\eta/\sqrt N\) vector plus fixed offsets.
This is the exact hypothesis of the accepted real-border two-copy matching proof.
For the graph with edges \(|(Q_i^{\rm wt})_{jk}|\ge h\|A_i\|_F\), let \(H_i(h,r)\) mean \(A_i\ne0\) and a matching of size at least \(r\).
For some law-dependent \(c_*,C>0\), on this minor event,
\[
 \mathbb P\left\{
 \frac{|\det M|}{\|A_i\|_F}\le c_*h/N
          \ \middle|\ D_i,\ M_{ii}\right\}
 \le C\psi(r),\qquad
 \psi(r)=e^{-c_*r}+\sqrt{\log(2+r)}r^{-1/9}.
 \tag{Pure-imaginary-matching}
\]
This invokes C_F0194_v3's real-border estimate after verifying its deterministic gauge hypotheses.
It does not invoke the nonzero-real-part assumption of C_F0194_v6's low-matching probability theorem.
The \(N^{-1}\) radius is the actual quadratic normalization.

<a id="internal-many-directions"></a>
### A second-value bound suffices in every internal dimension

For invertible B and R=B^(-1), the exact identity skew R=-B^(-T)(skew B)B^(-1) follows from B^(-1)-B^(-T)=-B^(-T)(B-B^T)B^(-1).

Fix an outer index \(i\) and an internal index \(j\) of \(\widehat D_i\).
Let \(B\) be the internal block of size \(p=N-2\), and put \(K_B=\operatorname{skew}B\).
Its random part has zero diagonal and pure-imaginary upper law, irrespective of the real diagonal variables of \(B\):
\[
 K_B=W_{\rm off,sub}+\operatorname{skew}\widehat F_{i,-j}.
\]
The shift in this display is deterministic and skew, and its entries have the original polynomial bound.
The normalized random part is \(\sqrt{p/N}\) times the standard size-\(p\) zero-diagonal model.
Since \(p/N\) stays in \([1/2,1]\), the accepted all-phase second-value theorem, with a fixed exponent slack for the shift and this factor, gives a fixed \(L>0\) with
\[
 s_{p-1}(K_B)\ge N^{-L}
 \tag{Internal-skew-second}
\]
outside any prescribed polynomial failure probability.
The exponent \(L\) can be chosen before all coefficient thresholds, with enough probability margin for the \(O(N^2)\) internal blocks.
This assertion allows odd \(p\): one singular value may vanish.

On \(\det B\ne0\), write \(R=B^{-1}\).
Using the identity already established above and singular min-max under invertible multipliers,
\[
 s_{p-1}(\operatorname{skew}R)
 =s_{p-1}(-B^{-T}K_BB^{-1})
 \ge \frac{s_{p-1}(K_B)}{\|B\|^2}
 \ge N^{-L-2K}
\]
on \(\|B\|\le N^K\).
No inverse-norm bound for \(B\), parity of \(p\), or least-value bound for \(K_B\) is needed.
For the raw internal column \(z=iE\eta\), the exact cofactor coefficient map is
\[
 \mathcal L\eta
  =N^{-1/2}\Phi(z)
  =\frac{i}{\sqrt N}(\operatorname{skew}R)E\eta.
\]
It has at least \(p-1\) complex singular values at least
\(\kappa_N=N^{-L-2K-1/2}\).

If \(q\) input coordinates and the same \(q\) output coordinates are discarded, at least \(p-1-2q\) singular directions of the remaining square block still have that lower bound.
Indeed intersect a good subspace of complex codimension at most one with the retained coordinate space and with the kernel of the discarded output rows.
Its dimension is at least \(p-1-2q\), and on it the retained output has the full output norm.
This is the singular min-max assertion needed for the following row estimate.

<a id="pure-imaginary-uncovered-diagonal"></a>
### Full-row uncovered-diagonal exclusion without a central strip

Fix \(K\) and a polynomial failure exponent \(b_0>0\), choose \(L\) as above, and then choose any fixed \(J\ge0\) and
\[
 H>J+L+2K+2.
 \tag{Pure-imaginary-row-scale}
\]
Outside probability \(C_{b_0}N^{-b_0}+C e^{-cN}\), simultaneously for all \(i\), all covers \(I\) with \(|I|<2r_N\), and all \(j\notin I\), the following configuration is absent:
\[
 \begin{split}
 &\widehat A_i\ne0,\quad\|\widehat D_i\|\le N^K,\\
 &|(\widehat Q_i)_{ab}|<N^{-H}\|A_i\|_F
       \quad(a\ne b,\ a,b\notin I),\\
 &|(\widehat Q_i)_{jj}|\ge N^{-J}\|A_i\|_F.
 \end{split}
 \tag{Pure-imaginary-uncovered-event}
\]
Here \(\widehat A_i=\operatorname{adj}\widehat D_i\).

To prove this, first remove the simultaneous (Internal-skew-second) exceptions, requesting their individual failure exponents with margin for all \(i,j\).
For fixed \(i,I,j\), condition on the internal block \(B\).
The last inequality forces \(\det B=(\widehat Q_i)_{jj}\ne0\), since the adjugate is nonzero.
If \(\det B=0\), the indicated event is empty.
On the block-measurable norm and skew-second guards, the preceding coefficient estimate therefore applies.
Let \(T\) be the internal coordinates outside \(I\), and also fix the raw row amplitudes indexed by \(I\).
The retained amplitudes \(\eta_T\) remain independent copies of the original real centered variance-one law, independent of \(B\).
The deleted diagonal may also be fixed; it does not enter this off-diagonal cofactor map.

The exact internal-row identity reads
\[
 -\frac{(\widehat Q_i)_{-j,j}}{\det B}
   =\frac{i}{\sqrt N}(\operatorname{skew}R)E\eta
          +\frac{Rg+R^Tf}{2},
\]
with deterministic affine offsets after conditioning.
The two displayed coefficient hypotheses force the retained output norm to be at most
\[
 \sqrt{|T|}\,N^{J-H}.
\]
The retained coefficient matrix has at least \(p-1-2|I|\ge |T|/2\) singular directions at scale \(\kappa_N\), eventually.
Project to those good left singular directions and divide by their singular values.
A small-output event then places \(\eta_T\) within distance at most
\[
 \sqrt{|T|}N^{J-H+L+2K+1/2}
\]
of a fixed complex affine subspace of complex codimension at least \(|T|/2\).
The exponent in this display is strictly negative by (Pure-imaginary-row-scale).
The accepted fixed-cutoff distance bound for a real variance-one law near complex affine subspaces consequently makes its conditional probability at most \(C e^{-c|T|}\le C e^{-c'N}\).
All constants are uniform in \(B\), the retained coefficient matrix, the conditioned coordinates and the affine center.
No global row-dependent norm or adjugate event has been conditioned on: these events are used only to imply membership in the fixed-center small-output event.
The number of \(i,j,I\) is at most \(N^{2r_N+3}=\exp(o(N))\).
Union this bound and add the internal-block exceptions to prove the assertion.
There is no majority-orientation requirement or discarded central strip.

<a id="low-matching-quantile"></a>
### A symmetric quantile turns low matching into an isolated minor

Let the matching in \(H_i(N^{-H},r_N)\) fail while \(A_i\ne0\).
Take the endpoints \(I\) of a maximal matching in the cyclic ordering, so \(|I|<2r_N\) and every off-diagonal entry of \(\widehat Q_i\) outside \(I\) is below the edge threshold.
On the last lemma's good event, all its diagonals outside \(I\) are below \(N^{-J}\|A_i\|_F\).
Thus
\[
 \widehat Q_i=Q_{\rm hub}+E,\qquad
 \operatorname{rank}Q_{\rm hub}\le2|I|<4r_N,\qquad
 \|E\|_F\le e_N\|A_i\|_F,
 \quad e_N=\sqrt{N-1}N^{-J}+(N-1)N^{-H}.
\]
The exact adjugate identity is
\[
 \widehat D_i\widehat Q_i\widehat D_i^T
     =(\det D_i)\widehat S_i,
 \qquad \widehat S_i=\operatorname{sym}\widehat D_i.
\]
On \(\Sigma_N(F,L_0)\), the preserved quantile gives
\[
 |\det D_i|N^{-L_0}
 \le s_{k_N}((\det D_i)\widehat S_i)
 \le \|\widehat D_i E\widehat D_i^T\|
 \le N^{2K}e_N\|A_i\|_F,
\]
because \(k_N\) exceeds the hub rank.
Hence
\[
 \rho_i=\frac{|\det D_i|}{\|A_i\|_F}
       \le N^{2K+L_0}e_N.
 \tag{Quantile-low-ratio}
\]
Only the indicated singular quantile is used, not \(s_{\min}(S_i)\).
This remains true if \(S_i\) is singular.
For any prescribed \(T_0>0\), choose
\[
 J>2K+L_0+T_0+2,\qquad
 H>\max\{J+L+2K+2,\ 2K+L_0+T_0+3\}.
\]
Then \(\rho_i\le N^{-T_0}\) eventually.
If \(D_i\) is invertible, the elementary identity
\(\rho_i=(\sum_j s_j(D_i)^{-2})^{-1/2}\)
gives \(t_1(D_i)\le\sqrt{N-1}\rho_i\).
If it is singular with nonzero adjugate, it has exactly corank one and \(\rho_i=t_1(D_i)=0\).

<a id="quantile-assembly"></a>
### Complete parameter order and probability assembly

Fix the requested \(b>0\).
Choose a raw cutoff exponent \(\kappa>(b+6)/2\), then
\(K>\max\{\kappa+1/2,\gamma+1\}\), with fixed slack for constants.
The finite-second-moment entry union bound gives
\(\mathbb P\{\|M\|>N^K\}\le C_bN^{-b-2}\).
Apply the accepted every-phase corank estimate to the raw matrix \(\sqrt N M\), whose shift exponent is at most \(\gamma+1\), to remove rank at most \(N-2\) with probability \(C_bN^{-b-2}\).

Apply the accepted second-value theorem to every actual \(D_i\).
Its size is \(N-1\), its normalization is \(\sqrt N\), and its shift becomes bounded by \((N-1)^{\gamma+2}\) after raw rescaling.
Choosing a larger failure exponent for their union and absorbing the bounded dimension ratio yields a fixed \(L_2\) with
\[
 t_2(D_i)\ge N^{-L_2}\quad\hbox{for every }i
\]
outside probability \(C_bN^{-b-2}\).
Next choose \(A_0,L_{\rm iso}\) from the accepted raw isolated-minor theorem at shift exponent \(\gamma+1\), requesting failure exponent \(b+3\).
These choices precede all fine coefficient thresholds.
Choose the internal skew-second exponent \(L\) with the same margin for the \(O(N^2)\) block union.
Finally select
\[
 T_0>L_{\rm iso}+L_2+3,\qquad
 J>2K+L_0+T_0+2,\qquad
 H>\max\{J+L+2K+2,\ 2K+L_0+T_0+3\},
\]
and take
\[
 A>\max\{H+2K+3,\ A_0+2K+3,\ 2\}.
 \tag{Final-quantile-parameters}
\]
All exponents are fixed before exposing any random minor or row.

The accepted complex-coordinate rectangular-distance argument, with the deterministic cofactor spread and averaging proof, gives constants \(a,\delta,C_1>0\) as follows.
Outside \(C e^{-cN}\), the event
\[
 \|M\|\le N^K,\quad
 \operatorname{rank}M\ge N-1,\quad
 s_{\min}(M)\le\varepsilon_N=N^{-A}
\]
forces at least \(\delta N/2\) indices with
\[
 G_i=\left\{
 A_i\ne0,\quad\|M\|\le N^K,\quad
 \frac{|\det M|}{\|A_i\|_F}
       \le C_1N^{2K+1}\varepsilon_N
 \right\}.
\]
The required preliminary smallness \(\varepsilon_N\le a/(4\sqrt N)\) holds by the final choice of \(A\).
The rectangular input is valid for the pure-imaginary law and its conjugate orientations by C_F0194_v6's complex-distance statement; the spread and averaging implication is deterministic once those rectangles hold.
In particular the probability of the target event intersected with \(\Sigma_N\) is bounded by \(C/N\) times the sum of the corresponding probabilities \(G_i\cap\Sigma_N\), plus the common exceptions.
This is averaging, not a union over the high-matching probabilities.

For high matching, the choice of \(A\) gives
\(C_1N^{2K+1-A}\le c_*N^{-H-1}\)
eventually, so (Pure-imaginary-matching) contributes at most \(C\psi(r_N)\).
The additional symmetric guard can simply be dropped in this upper bound.
For low matching, the simultaneous uncovered-diagonal and skew-second guards and \(\Sigma_N\) give \(\rho_i\le N^{-T_0}\).
If \(D_i\) is invertible, then
\[
 t_1(\sqrt N D_i)\le N^{1-T_0},\qquad
 \frac{t_1(\sqrt N D_i)}{t_2(\sqrt N D_i)}
      \le N^{1/2+L_2-T_0}.
\]
Both are at most \(N^{-L_{\rm iso}}\) eventually.
The singular nonzero-adjugate case is already exactly corank one.

For every usable low-matching index the raw full ratio satisfies the exact scaling identity
\[
 \frac{|\det(\sqrt N M)|}
      {\|\operatorname{adj}(\sqrt N D_i)\|_F}
   =N\,\frac{|\det M|}{\|A_i\|_F}
   \le C_1N^{2K+2-A}\le N^{-A_0}.
\]
The factor is \(N\), since the determinant has degree \(N\) and the minor adjugate degree \(N-2\) in the scalar rescaling.
Gauge similarity introduces no additional factor.
Thus each low contribution lies in the union event of the accepted raw isolated-minor theorem, whose probability is at most \(C_bN^{-b-3}\).
This use checks both its absolute and relative singular thresholds instead of inferring isolation solely from \(\rho_i\).
The average of these low-event indicators is no larger than the indicator of their union.
Adding norm, rank, second-value, internal skew and uncovered-diagonal failures yields
\[
 \mathbb P\{s_{\min}(M)\le N^{-A},\Sigma_N\}
       \le C_bN^{-b}+C\psi(\lfloor\sqrt N\rfloor).
\]
The exponential part of \(\psi\) is absorbed into the polynomial error, and its other part is bounded by \(C\sqrt{\log(2+N)}N^{-1/18}\).
This proves the displayed guarded floor.
All auxiliary guards are combined by set inclusion and union bounds, never by conditioning on their global intersection.
For the random-shift form, condition only on \(F_N\) within this dimension, use the uniform deterministic proof, and add the exact guard failure already defined.
No cross-size independence is used.

## Current assessment
[Selected decision](#decision-complex-floor-candidate)

## Assessment history

### Decision complex-floor-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T13:04 |
| status | open |
| reason | The complete generic complex finite-net and full-adjugate argument, its rank/second-value/isolated auxiliaries, the symmetric-quantile guarded purely imaginary floor, and the skew pairing/even floor are fixed for fresh independent review. The non-purely-imaginary phase-line main branch is reused from reviewed v6. No summability, logarithmic determinant transfer or original Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact law branches and auxiliary assertions](#statement) | The generic finite-variance linear and rank/second/isolated interfaces, non-line and reused non-pure-imaginary phase floors, exact purely imaginary quantile guard/random-shift failure, and zero-diagonal skew even/odd boundary. |
| argument | [Complete complex-law candidate proof](#argument) | Complete orientation-envelope net proof and uniform truncation, full-adjugate high/low matching and generic assembly, direct accepted phase-line reuse, self-contained skew pairing, and the full quantile-guard probability argument. |
| dependency | [Complex inverse-net source](../audits/literature/TV08/Yin_U001.md#tv08-u001) | Only the inspected arXiv v5 controlled-moment definition, fixed-phase lemma and complex finite-net theorem, with common-control and polynomial-range uniformity and the stated source-proof limits; every matrix/profile adaptation is proved here. |
| dependency | [Fair-sign matching source](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) | Only Definition 1.5 and Theorem 1.6 of the 2016 edition, at degrees one and two and arbitrary length-one interval center; exact complex two-copy applications are proved here. |
| dependency | [Deterministic bordered rank](Yin_C_F0194_v2.md#border-rank) | Borel kernel selection and rank increase two when both kernel forms are nonzero; no old real-law corank probability theorem is imported for generic entries. |
| dependency | [Deterministic adjugate rows](Yin_C_F0194_v3.md#row-adjugate) | All-complex matrix row-adjugate inequality and invertible or exactly-corank-one usable-index deduction. |
| dependency | [Rectangular support mechanism](Yin_C_F0194_v3.md#rectangles) | Conditional column distances, Gram inverse and support entropy after the complex-coordinate distance hypotheses have been checked. |
| dependency | [Pointwise spread and average](Yin_C_F0194_v3.md#spread-and-average) | Only deterministic right-vector spread and the cofactor average under explicit norm and rank guards, with no factor N on the matching contribution. |
| dependency | [Exact real-border matching](Yin_C_F0194_v3.md#two-copy-matching) | Only the complete finite-radius real-law estimate after the c=i unitary gauge, including coefficient normalization h/N and arbitrary conditional centers. |
| dependency | [Complex fixed-cutoff distance](Yin_C_F0194_v6.md#complex-distance) | Uniform exponential distance estimate for centered variance-one complex coordinates with arbitrary conjugate orientations, including the real-amplitude specialization. |
| dependency | [Every-phase cyclic gauge](Yin_C_F0194_v6.md#phase-line-gauge) | Exact unitary similarity and cyclic ordering at c=i, preserving determinants, singular values, adjugate norm and the transformed phase-line model. |
| dependency | [Internal complex cofactor identity](Yin_C_F0194_v6.md#complex-internal-row) | Exact sym-adjugate row formula with z and conjugate z and arbitrary distinct shift offsets; the skew coefficient map and its quantitative guards are proved here. |
| dependency | [Every-phase corank auxiliary](Yin_C_F0194_v6.md#phase-line-rank-tail) | Only the accepted c=i corank-at-least-two tail used in the pure-imaginary guarded assembly after raw scaling. |
| dependency | [Every-phase second-value auxiliary](Yin_C_F0194_v6.md#phase-line-second-floor) | Only the accepted c=i raw/normalized second-smallest floor for actual minors and internal skew blocks, and the even skew-floor consequence after singular pairing. |
| dependency | [Every-phase isolated-minor auxiliary](Yin_C_F0194_v6.md#phase-line-isolated-minor) | Only the accepted c=i raw restricted probability theorem after both absolute and relative minor thresholds and the full raw ratio are verified. |
| dependency | [Reviewed non-pure-imaginary phase floor](Yin_C_F0194_v6.md#statement) | Direct reuse only for xi=c eta with c of modulus one and Re c nonzero, arbitrary complex polynomial shifts and its independent random-shift form; no c=i main-floor extension. |
