---
author: Yin
---

# Complex scalar inverse concentration: bounded source preparation

Preparation date: 2026-11-05.
This ordinary research preparation follows the [real-scalar interface gap](Yin_D_F0027.md#inverse-count-interface).
It asks for an inverse Littlewood--Offord statement for a fixed centered complex law with positive finite variance, allowing dependent real and imaginary parts, and complex deterministic coefficients.
The intended use is a finite-entropy approximation in the Hermitian row/profile argument, not a new all-size least-singular-value theorem.
No Claim, formal review or completed complex profile count is asserted here.

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
The remaining source obligation is to establish the precise componentwise version needed for adoption, or replace that use with a separately justified finite-net argument.

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
These deductions check the proposed block application against the exact source statement; they do not complete the subsequent Hermitian row-exposure proof, its choice of representatives, or all scale and orientation bookkeeping.
Uniform use of the source theorem over polynomial concentration ranges and the controlled truncated laws must be retained at this explicit scope in that proof.

The proposed split of a mixed xi/conjugate-xi sum into two independent orientation groups is a research lead: convolution bounds each group's concentration below by that of the combined sum, and conjugating one group converts its scalar law to xi.
A complete argument still has to check group normalization, permitted exception counts for short groups, the two progression descriptions, monotone tail concentrations after each permutation, and the exact entropy/probability cancellation.
Neither this lead nor the two source statements establishes that profile count here.
The separate Hermitian quadratic coefficient and low-matching issues remain outside this bounded source preparation.

## Preparation outcome

The selected NO15 arXiv v4 and TV08 arXiv v5 originals were obtained in the existing private logical PDF store and their title pages and relevant statements were read.
The initial versioned NO15 web endpoint failed, but the unversioned primary endpoint returned the verified v4 original, so no original-acquisition failure remains for these selected editions.
NO15's earlier 45-page author layout was not substituted for the 57-page adopted edition.
The existing NO15 bibliography was reused, the distinct TV08 work was added, and no source U, Claim, review, Task, strategy or index was created or revised by this preparation.
The substantive unresolved work is the exact complex arithmetic interface or an alternative encoding proof, followed by the orientation-aware Hermitian application; source discovery alone does not settle it.
