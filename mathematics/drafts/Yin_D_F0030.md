---
author: Yin
---

# Complex scalar inverse concentration and orientation-envelope profile count

Preparation date: 2026-11-05.
This ordinary research preparation follows the [real-scalar interface gap](Yin_D_F0027.md#inverse-count-interface).
It asks for an inverse Littlewood--Offord statement for a fixed centered complex law with positive finite variance, allowing dependent real and imaginary parts, and complex deterministic coefficients.
The intended use is a finite-entropy approximation in the Hermitian row/profile argument, not a new all-size least-singular-value theorem.
The continuation below develops a complete generic complex orientation-envelope count and its near-kernel consequence, with TV08 supplying the finite-net input and MNV16 supplying a degree-one bound.
This is proof development, without a new Claim or independent review; it does not by itself assert a least-singular-value floor or a completed Task.

The bounded search first reused Ngu12a and the existing NO15 source notes, and inspected the local Nguyen--Vu inverse-theorem and erratum statements.
The latter still use real scalar randomness, even when the coefficient space is real dimension two.
The repository's TV06 is Tolsa--Verdera, and the inspected local TV07 is Totik--Varju; neither is a Tao--Vu inverse-concentration source.
External queries used the phrases "inverse Littlewood-Offord" with "complex random variable" and "generalized arithmetic progression".
They identified the two primary works below; the search stopped once their exact relevant statements and present use limits were located.
This is not an absence-of-literature or priority claim.

<a id="no15-interface"></a>
## NO15: a complex scalar progression statement

Use [the retained arXiv v4 edition and inspection limits](../audits/literature/NO15/readme.md#yin-complex-linear-inverse-theorem-passages).
Theorem 3.1, PDF p. 10, takes complex coefficients with sum |a_i|^2=1, fixed 0<epsilon<1 and B>0, any beta>0, and concentration gamma>=n^(-B).
For n^epsilon<=n'<=n it asserts a proper symmetric GAP Q with rank O_(B,epsilon)(1), size at most max{O_(B,epsilon)(gamma^(-1)/sqrt(n')),1}, and at least n-n' coefficients within beta of Q.
Its constants may also depend on the scalar law.
Corollary 3.3, PDF p. 11, explicitly gives this conclusion for iid complex xi satisfying E|xi|^2=1 and E xi=E[Re(xi)Im(xi)]=0, without independence of the components.
These are direct primary-statement observations, with the exact arithmetic qualification below.

<a id="arithmetic-wording"></a>
### The exact arithmetic clause needs clarification before use

The displayed Theorem 3.1(ii), visually checked on p. 10, literally asserts
\[
 g_i=\beta p_i/p,\qquad
 p\in\mathbb Z\setminus\{0\},\quad |p|=O(\sqrt{n'}),\qquad
 p_i\in\mathbb Z,\quad |p_i|=O(\beta^{-1}\sqrt{n'}).
\]
This makes every displayed generator real and cannot literally give the claimed complex-coefficient conclusion.
For example, with iid real Rademacher xi, even n, a_i=i/sqrt(n), beta=n^(-2), and n'=floor(n/2), the unit coefficient vector has concentration of order n^(-1/2) at zero but none of its coefficients is beta-close to a real progression.
This simple test concerns the printed arithmetic wording, not the existence of a complex inverse theorem.

The source's own applications on pp. 17 and 23 instead specify complex rational coordinates of the form p/q+i p'/q' with polynomial bounds.
Appendix A identifies C with R^2 on p. 49, rounds to (Z/(Dk))^2 on p. 50 and constructs the final scaled GAP on pp. 51--52.
These passages strongly indicate a coordinatewise integer formulation, rather than a restriction of the progression to R.
They do not by themselves constitute a complete independent verification of every constant and precision clause after passage from Theorem 3.2 to Corollary 3.3.
The same p. 11 literally prints |p|,|q|=O(beta) in the rational approximation preceding Corollary 3.4; for beta tending to zero this cannot bound a nonzero integer denominator.
Do not silently use either literal formula as the already verified C_F0194_v1 arithmetic interface.

The local Nguyen--Vu erratum, PDF pp. 1--2, explicitly writes each real coordinate as beta p_ij/p and repairs an approximation step in the continuous corollary.
That is useful evidence for the intended coordinate convention, but its random scalar is real and it supplies no automatic verification of NO15's complex adaptation.
The present check read NO15's stated conclusions and selected appendix endpoints, not the complete Appendix A proof or its additive-combinatorial inputs.
A future use of this rational-generator interface would still require verification of the precise componentwise version.
The finite-net argument below replaces that use, so this unresolved wording is not a pending source input to the present proof.

<a id="fixed-phase"></a>
### Removing the covariance condition uses one fixed phase

For the actual fixed centered unit-variance complex law, put m=E(xi^2).
If m is nonzero choose theta=-arg(m)/2, and otherwise take theta=0.
Then eta=exp(i theta)xi has the same second absolute moment and mean, and
\[
 E[\operatorname{Re}\eta\operatorname{Im}\eta]
 =\tfrac12\operatorname{Im}(e^{2i\theta}m)=0.
\]
For fixed coefficients u_j set a_j=exp(-i theta)u_j, so sum a_j eta_j=sum u_j xi_j and their squared coefficient norms agree.
This is a deterministic phase depending only on the fixed law, with no N-dependence or new independence assumption.
Multiplying a resulting progression by exp(i theta) preserves rank, size and approximation error; a componentwise rational description becomes a grid in one fixed rotated coordinate system, which has no extra counting entropy.
This elementary scalar substitution does not rotate a Hermitian matrix while preserving its prescribed entry model, and it does not prove a matrix floor.
Uniformity for the dimension-dependent laws produced by entry truncation is a separate issue: the unqualified distribution dependence of NO15's constants cannot simply be declared uniform.

<a id="tv08-interface"></a>
## TV08: a direct finite-net alternative

Use [arXiv:0708.2895v5 and the retained original](../audits/literature/TV08/readme.md).
Definition 2.2 calls a complex scalar x controlled when, for a fixed kappa>=1,
\[
 E|x|^2\le\kappa,\qquad
 E[(\operatorname{Re}(zx-w))^2\mathbf1_{\{|x|\le\kappa\}}]
 \ge\kappa^{-1}(\operatorname{Re}z)^2
 \quad(z,w\in\mathbb C).
\]
Lemma 2.4 states that every fixed complex law of finite nonzero variance has this property after a fixed phase rotation.
Theorem 3.2, PDF p. 11, gives the following finite-count statement for this genuinely complex scalar law.
For 0<epsilon<=1, beta>=exp(-n^(epsilon/2)) and p=n^(-O(1)), the set
\[
 \left\{v\in\mathbb C^n:\|v\|_2=1,\quad
 \sup_a\mathbb P\left(\left|\sum_jv_jx_j-a\right|\le\beta\right)\ge p\right\}
\]
has an l-infinity beta-net of cardinality at most
\[
 n^{(-1/2+\epsilon)n}p^{-n}+\exp(o(n)).
\]
Thus fixed polynomial precision beta=n^(-A) lies in the theorem's allowed radius range for sufficiently large n.
The statement does not require independent real and imaginary parts and does not require a moment above two.
The inverse theorem's full proof was not audited here.

The controlled-second-moment interface is also suited to a uniform truncation check.
If y already has the displayed kappa property and y_N is its law conditioned on |y|<=N^kappa_0, then for sufficiently large N the truncated expectation over |y_N|<=kappa is the corresponding original expectation divided by P(|y|<=N^kappa_0), so its lower bound is preserved.
Its total second moment is at most 2kappa once that probability exceeds one half; increasing the control constant to 2kappa also preserves the lower-bound inequality.
This verifies a common control constant for that specific conditional-law family, without asserting an unchanged NO15 distribution-dependent constant or an unproved uniform profile theorem.

<a id="profile-limit"></a>
## Relation to the required profile count

The [existing real-scalar count](../claims/Yin_C_F0194_v1.md#structured-vector-counting) uses more than a global net.
At the start of each profile block it applies an inverse theorem to an entire tail, then encodes only the block's m_h coordinates using a common GAP with polynomially many generator choices.
This gives the factor r_h^(-m_h) in equation (30), which cancels the matching factor in the row probability (31).
TV08's tail net instead counts all coordinates of that tail and has an exponent equal to the whole tail length.
Restricting those net points to a shorter block does not automatically improve that exponent to m_h.
Consequently Theorem 3.2 is a verified candidate finite-entropy source but is not a direct replacement for equations (29)--(31) without a new encoding argument.
One must also retain deterministic representatives and control how coefficient rounding changes each row's concentration at the next scale.

<a id="blockwise-net-route"></a>
### Applying the net theorem to each large block instead

There is a concrete way around the preceding tail-length problem at the level of the required linear source interface.
For independent sums X and Y, conditioning on Y gives sup_a P(|X+Y-a|<=t)<=sup_a P(|X-a|<=t).
Thus a profile block contained in the tail has concentration at least the tail's lower bound p, so the source theorem can be applied to the block itself rather than to the entire tail.
Fix 0<delta<1 and call a block large when its length m satisfies n^(1-delta)<=m<=n.
For beta=n^(-A), polynomially small p>=n^(-D) is also m^(-O(1)), and beta/2>=exp(-m^(epsilon/2)) eventually for every fixed source epsilon>0.
These are exactly the small-ball and precision ranges required by TV08.

For blocks of norm at most 2, the nonunit block norm can be handled without a progression.
If its norm sigma is less than beta, the zero vector approximates the whole block within beta in l-infinity.
Otherwise bin sigma in [s,s+beta) with s a positive multiple of beta and sigma<=2.
There are O(beta^(-1)) bins.
The normalized coefficient vector has concentration at least p at radius beta/s, because beta/s>=beta/sigma.
Choose a TV08 net at radius beta/s, and multiply its points by s.
For a unit witness v and its net point w,
\[
 \|\sigma v-sw\|_\infty
 \le |\sigma-s|\|v\|_\infty+s\|v-w\|_\infty
 \le2\beta.
\]
The total number of approximants for this block is therefore bounded by
\[
 O(\beta^{-1})
 \left[m^{(-1/2+\epsilon)m}p^{-m}+\exp(o(m))\right],
\]
and the multiplicative bin cost is polynomial in n for each fixed precision exponent A.
For a fixed number of profile blocks that cost does not change the leading n log n entropy coefficient.

For 0<epsilon<1/2, the first term is at most
\[
 n^{-(1/2-\epsilon)(1-\delta)m}p^{-m}.
\]
If the reservoir bound is p<=n^(-b_0) with b_0=1/2-3 epsilon_0/4 as in the existing count, choosing the source epsilon=epsilon_0 makes the first term at least n^(epsilon_0 m/4), since m<=n.
It then absorbs the additive exp(o(m)) term for sufficiently large n.
The loss relative to the original half-power gain is only epsilon_0+delta/2-epsilon_0 delta, which can be kept small before choosing the fine precision.
Blocks of size less than n^(1-delta), when there are a fixed number of blocks, contain o(n) coordinates altogether and can instead be encoded on the polynomial grid at exp(o(n log n)) cost.

At the initial full-vector inverse step, TV08's cardinality for p=n^(-b) likewise has a leading n log n entropy coefficient independent of the fine exponent in beta=n^(-A).
This is the specific feature needed to replace the rational structured-class coarse count.
These source-level deductions check the proposed block application against the exact source statement.
The complete row-exposure proof, representative choices, uniform truncation and scale bookkeeping are supplied in the [generic continuation](#generic-envelope-interface) below.

For a mixed xi/conjugate-xi sum, splitting its two independent orientation groups makes convolution bound each group's concentration below by that of the combined sum, and conjugating one group converts its scalar law to xi.
The continuation implements this fact with finite nets, direct grids for short groups and a separate degree-one treatment of the degenerate branch.
The separate Hermitian quadratic coefficient and low-matching issues remain outside this linear argument.

## Source preparation boundary

The selected NO15 arXiv v4 and TV08 arXiv v5 originals were obtained in the existing private logical PDF store and their title pages and relevant statements were read.
The initial versioned NO15 web endpoint failed, but the unversioned primary endpoint returned the verified v4 original, so no original-acquisition failure remains for these selected editions.
NO15's earlier 45-page author layout was not substituted for the 57-page adopted edition.
The existing NO15 bibliography was reused, the distinct TV08 work was added, and no source U, Claim, review, Task, strategy or index was created or revised by this preparation.
The exact complex arithmetic interface remains unresolved and is not used in the continuation below.
The continuation supplies an alternative encoding proof directly from the finite-net theorem; neither source discovery alone nor that linear argument supplies the separate Hermitian quadratic assembly.

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

The proof below uses the exact [TV08 finite-net interface](#tv08-interface) and [MNV16-U001](../audits/literature/MNV16/Yin_U001.md#matching-rank) at degree one.
It adapts the accepted [phase-envelope profile mechanism](../claims/Yin_C_F0194_v6.md#phase-envelope-count), replacing its progression descriptions by block nets and proving the new scalar-law interfaces explicitly.
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
This is the same exact sign mechanism as [the accepted unary argument](../claims/Yin_C_F0194_v4.md#argument), specialized here to complex linear scalar laws with the new uniform difference check.

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

This completes the developed generic complex linear interface needed by the [non-line full-adjugate reduction](Yin_D_F0027.md#nonline-full-adjugate-return).
It applies even to phase-line and pure-imaginary laws, since a kernel's low linear concentration is compatible with a parity-forced singularity.
The non-line quadratic matching estimate, rank-growth deductions, second-smallest singular-value estimate and isolated-minor assembly are separate consuming arguments, not consequences asserted without their own proofs here.
Independent mathematical review and any fixed Claim adoption remain outstanding for this new development.
