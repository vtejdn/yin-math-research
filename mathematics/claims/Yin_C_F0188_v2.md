---
author: Yin
---

# Finite-variance real Wigner invertibility under complex symmetric shifts

<a id="statement"></a>
## Exact small-singular-value assertions

Let \(X_n\) be real symmetric with zero diagonal and independent upper off-diagonal entries having a fixed real law \(\xi\), where \(\mathbb E\xi=0\) and \(\mathbb E\xi^2=1\).
For every \(\gamma,B>0\), there are \(A,C,n_0>0\), depending only on \(\xi,\gamma,B\), such that
\[
 \sup_{\substack{F=F^T\in M_n(\mathbb C)\\ \max_{ij}|F_{ij}|\le n^\gamma}}
 \mathbb P\{s_{\min}(X_n+F)\le n^{-A}\}
 \le Cn^{-B},\qquad n\ge n_0.
 \tag{CS}
\]
The diagonal of \(F\) is arbitrary and deterministic within the same polynomial bound.
The same conclusion holds when \(X_n\) instead has independent real diagonal entries of a fixed law with finite second moment, independent of the off-diagonal family; constants may additionally depend on that law.
It holds in normalized form for \(W_n=X_n/\sqrt n\) after changing the polynomial exponents.
Consequently it also applies conditionally to an independent complex symmetric random shift, on any event where that shift satisfies the prescribed deterministic polynomial bound.
No moment above two, density, or non-atomicity is assumed.
For a fixed sequence of such shifts, choosing \(B>1\) gives an eventual almost-sure polynomial floor under every cross-size coupling.
This statement does not cover general fixed matrix-coefficient linear pencils or complex Hermitian Wigner off-diagonal laws.

## Inputs and provenance

This version repairs the order-dependent high-product passage in [the initial candidate](Yin_C_F0188_v1.md#argument).
The proof now separates the low-product case again after each reservoir permutation before starting the multiscale profile argument.
The theorem statement and external inputs are unchanged; the original proof remains fixed for its actual review findings.
The [initial independent whole-proof objection](../audits/reviews/Yin_R_F0192_v1.md#finding-whole-proof) and [key-step finding](../audits/reviews/Yin_R_F0193_v1.md) preserve the failed order-transfer implication and its counterexample.
The selected assessment below relies on the fresh independent review of this repaired version, not on the earlier conditional profile checks.

This is a project adaptation of the inverse-concentration and probability-profile method, with the precise two external vector-valued inverse Littlewood--Offord inputs inspected in [Ngu12a](../audits/literature/Ngu12a/readme.md).
The selected mathematical edition is arXiv:1105.5733v1: Condition 1 and Theorem 1.3 on PDF pp. 2--3, and the quadratic concentration definition and Theorem 1.8 on pp. 3 and 5.
The original proofs of those theorems are accepted external inputs rather than independently re-audited here.
Their coefficient dimension is two, identifying complex coefficients with vectors in \(\mathbb R^2\), while the random scalar variables remain real.
Their anti-concentration constants, exceptional-set bounds, progression sizes, relative rational generators and arbitrary quadratic linear terms are used explicitly below.
The [source progression and concentration conventions](../audits/literature/Ngu12a/Yin_U001.md) specify the complete definitions used here.
The [Ngu12 published real-shift theorem](../audits/literature/Ngu12/readme.md) motivates the cofactor mechanism, but no unproved complex-shift extension or ORSV15 personal-communication assertion is invoked as a theorem.
The exact new complex profile count, deterministic-diagonal adjustment and rank-removal argument are supplied here.
No claim of novelty, priority, or general [F0012 completion](../tasks/Yin_T_F0012_v3.md#contract) is made.

<a id="argument"></a>
## Proof

All constants below may be enlarged finitely many times; the small exponent \(\varepsilon=1/100\) is fixed throughout.
Every exponent specifying a coordinate-rounding precision is chosen to be an integer.
The fractional exponents used for exception counts and probability bins do not specify coordinate meshes.

Choose an integer \(K\) larger than \(\gamma+2\) and \((B+5)/2\).
The probability that any raw off-diagonal entry exceeds \(n^K\) is \(O(n^{2-2K})\).
Conditional on their all being bounded, the entries remain independent with common law \(\xi_n=(\xi\mid |\xi|\le n^K)\).
The laws \(\xi_n\) have uniform constants in
\[
 \mathbb P\{c_1\le|\xi_n-\xi_n'|\le c_2\}\ge c_3>0,
 \tag{22}
\]
because \(\xi\) is nondegenerate and \(\xi_n\) converges in total variation to \(\xi\).
The same statement holds for the symmetrized law \(\eta(\xi_n-\xi_n')\) with an independent nontrivial Bernoulli selector \(\eta\).
The inverse theorems' constants depend only on their displayed anti-concentration constants, the fixed coefficient dimension two, and their fixed exponents, so they apply uniformly to these truncated laws.
Neither centering nor variance renormalization of \(\xi_n\) is needed in these inverse-theorem uses.
Absorb fixed factors into \(K\), so every entry of the truncated matrix \(M=X_n+F\) has absolute value at most \(n^K\).

## Structured-vector consequence of quadratic concentration

Let \(D\) be a complex symmetric \(m\)-by-\(m\) matrix with entries bounded by \(n^K\), where \(m=n-1\).
Write \(C_D=\operatorname{adj}D\), assume \(C_D\ne0\), and put \(A_D=C_D/\|C_D\|_F\).
Suppose a quadratic form with quadratic coefficients \(A_D\), arbitrary complex linear coefficients, and iid real \(\xi_n\) variables has concentration at least \(n^{-b}\) in a disk of radius \(n^{-2a}\), where \(a\) is a positive integer.
Then there is an integer constant \(C_0\), depending on \(b,K,\varepsilon\) and (22) but not on \(a\), and a vector \(u\in\mathbb C^m\), with the following properties when \(a\) is sufficiently large:

- \(1/2\le\|u\|\le2\), and \(|(Du)_i|\le n^{-a+C_0}\) for all but \(C_0\) rows.
- All but \(C_0n^\varepsilon\) coordinates of \(u\) belong to a generalized arithmetic progression of rank at most \(C_0\) and size at most \(n^{C_0}\).
- Each real and imaginary coordinate of \(u\), and of the progression's generators, is rational with numerator and denominator bounded by \(n^{a+C_0}\).

Here a progression is a finite integer box mapped into \(\mathbb C\); properness is unnecessary for the counting consequence.
To establish the assertion, apply the vector-valued quadratic inverse theorem to \(A_D\in M_m(\mathbb R^2)\).
It gives a nonzero integer \(k\), a bounded list of rows indexed by \(I_0\), and integers \(k_{ij}\), all bounded by \(n^{O_b(1)}\), such that for all but \(O(n^\varepsilon)\) row indices
\[
 r_i'=k r_i(A_D)+\sum_{j\in I_0}k_{ij}r_j(A_D)
\]
has linear concentration at least \(n^{-O_b(1)}\) at radius \(n^{-2a+O_b(1)}\) for the symmetrized variables.
If one such \(r_i'\) has norm at least \(n^{-a}\), normalize it and apply the vector-valued linear inverse theorem.
This gives the progression and rational grid at resolution \(n^{-a+O_b(1)}\), including separate grid rounding of the exceptional coordinates.
Use a deterministic larger radius \(n^{-a+C}\) in this application, with integer \(C\), so the grid scale is an integer power of \(n\), hence rational and independent of the row's possibly irrational norm.
The adjugate identity \(A_DD=(\det D/\|C_D\|_F)I\) shows that the original normalized row is bilinearly orthogonal to all but \(|I_0|+1\) rows of \(D\).
Coordinate approximation changes each of these row products by at most \(n^{K+1}\) times the approximation error.

If every \(r_i'\) has norm below \(n^{-a}\), choose a column of \(A_D\) with norm at least \(m^{-1/2}\).
Its entries outside the exceptional index set are, within \(n^{-a+O_b(1)}\), integer combinations of the bounded list of selected column entries divided by \(k\).
Round the selected entries and exceptional coordinates on a complex rational lattice, and use those integer relations to define the other coordinates.
Keep the bounded index set \(I_0\) among the exceptional coordinates when making this definition, so no selected generator is overwritten by a relation.
The resulting vector approximates that column at norm error \(n^{-a+O_b(1)}\), has a progression of bounded rank and polynomial size, and has rational coordinates of the asserted height.
Multiply it by the integer \(\lceil1/\|v\|\rceil\), which is at most \(O(\sqrt n)\), to place its norm between one and two.
The adjugate identity gives bilinear orthogonality of the original column to all but one row, and the same error estimate applies.
All tolerances and rational heights are absorbed into \(C_0\).
The use of \(\lceil1/\|v\|\rceil\) avoids a zero multiplier when rounding makes \(\|v\|\) slightly larger than one.
These arguments use \(\sum|c_{ij}|^2\) for the Frobenius norm and \(\sum_jD_{ij}u_j\) for adjugate orthogonality; no Hermitian conjugation is inserted into that algebraic identity.

## Uniform counting of the resulting complex vectors

We prove that a truncated random complex symmetric \(M\), with real iid off-diagonal randomness satisfying (22) and arbitrary deterministic complex entries bounded by \(n^K\), has such a vector with probability at most \(\exp(-cn)\), once \(a\) is chosen sufficiently large.
This argument works equally for a principal minor, since replacing \(n\) by \(n-1\) only changes fixed polynomial factors.
Let \(\beta_0=n^{-a+C_0}=n^{-s}\).
The number of possible vectors described above is
\[
 n^{C_*n+O_a(n^\varepsilon)+O_a(1)},
 \tag{23}
\]
with \(C_*\) independent of \(a\): the generators and box lengths have polynomially many choices, the nonexceptional coordinates have at most \(n^{C_0}\) choices each, and only \(O(n^\varepsilon)\) coordinates use the full rational grid.
The choice of exceptional indices is included in (23).

Add a largest coordinate of \(u\) as one additional progression generator if necessary.
This changes its size by a factor at most three and its rank by one.
Choose a bulk set of size \(n_0=n-O(n^\varepsilon)\), all of whose coordinates lie in the progression, containing that coordinate.
After a permutation determined by the exceptional set and the largest coordinate, suppose the bulk occupies \(1,\ldots,n_0\) and
\[
 |u_{n_0}|\ge(2\sqrt n)^{-1}.
 \tag{24}
\]
The number of these choices and permutations is \(\exp(o(n))\).
We retain an arbitrary set of at least \(n-C_0\) row constraints; it need not be a consecutive set.
There are at most \(n^{O(C_0)}\) choices of the omitted row indices, which are included in the union bounds below.

For a deterministic coefficient vector define
\[
 \rho_i(u,t)=\sup_{z\in\mathbb C}
 \mathbb P\left\{\left|\sum_{j=i}^{n_0}u_j\xi_{n,j}-z\right|\le t\right\}.
\]
These numbers are nondecreasing in \(i\).
For \(\beta_0\le t\le1\), covering the support disk of radius \(O(n^{K+1})\) by disks of radius \(t\) gives a uniform lower bound
\[
 \rho_i(u,t)\ge n^{-D},
 \tag{25}
\]
where \(D=O(s+K)\), also for coefficient vectors within distance \(O(\beta_0)\) coordinatewise of the norm-bounded vectors considered here.
The same lower bound, with an enlarged \(D\), applies to every rounded vector below.

Condition first on entries connecting the bulk to its complement, and then expose the bulk rows in increasing order.
The random part left in row \(i\) consists of strictly upper entries, so its conditional small-ball bound is \(\rho_{i+1}(u,t)\).
Omitting the at most \(C_0\) unconstrained rows and using (25) proves
\[
 \mathbb P\{|(Mu)_i|\le t\text{ on the prescribed rows}\}
 \le n^{D(C_0+1)}\prod_{i=1}^{n_0}\rho_i(u,t).
 \tag{26}
\]
This is the precise deterministic-diagonal adjustment: the shifted product starting at \(\rho_2\) loses only \(\rho_1^{-1}\), not one loss per row.
By (22) and (24), for \(t\le c/\sqrt n\), each tail concentration is at most a fixed \(p_0<1\).
The direct row-exposure bound is consequently \(p_0^{n_0-C_0-1}\) at this resolution.

Choose \(C_1>C_*+10\).
For vectors with \(\prod_{i=1}^{n_0}\rho_i(u,\beta_0)<n^{-C_1n}\), (23) and (26) already give total probability \(n^{-cn}\).
It remains to count vectors with the reverse inequality.
Put
\[
 q=\lceil n^{1-\varepsilon}\rceil,\qquad
 \kappa=\varepsilon/10,\qquad
 t_*=n^{-K-5}.
\]
Call a vector degenerate if every \(q\)-element subset of its bulk coordinates has concentration at least \(q^{-1/2+\kappa}\) at radius \(t_*\).
For each such subset, apply the linear inverse theorem with allowed exception count \(\lfloor q/2\rfloor\).
The progression-size bound becomes
\[
 |Q|\le\max\{Cq^{-\kappa},1\}=1
\]
eventually, so the proper symmetric progression is \(\{0\}\).
Thus at least \(\lceil q/2\rceil\) coordinates in every \(q\)-subset have modulus at most \(t_*\).
It follows that at most \(\lfloor q/2\rfloor\) bulk coordinates have modulus greater than \(t_*\), since otherwise a \(q\)-subset with too many such coordinates could be chosen.

Round these exceptional coordinates and the coordinates outside the bulk on a complex lattice of mesh \(t_*\), and set every other coordinate to zero.
There are at most \(\exp(O_K(q\log n))=\exp(o(n))\) resulting vectors \(u'\).
Their coordinate errors are at most \(2t_*\), so the row tolerance becomes at most
\[
 \beta_0+2n^{K+1}t_*\le3n^{-4}
\]
when \(s\) is large.
The large coordinate in (24) survives this rounding.
The direct bound \(p_0^{n_0-C_0-1}\) and a union bound therefore give \(\exp(-cn)\) for the degenerate vectors.
No order structure on \(\mathbb C\) is used.

For a nondegenerate vector, select a \(q\)-subset with concentration below \(q^{-1/2+\kappa}\), and include the large coordinate if it is not already in that set.
Place this set at the end of the bulk; its size is \(q_0\in\{q,q+1\}\).
This costs only \(\exp(O(q\log n))=\exp(o(n))\) choices.
Set \(p=n_0-q_0=n-o(n)\).
Every tail starting at \(i\le p\) contains the selected subset, so for every \(t\le t_*\),
\[
 \rho_i(u,t)\le n^{-b_0},\qquad
 b_0=1/2-3\varepsilon/4>1/2-\varepsilon.
 \tag{27}
\]
Let \(\pi_t(u)=\prod_{i=1}^p\rho_i(u,t)\).
The coordinate permutation can change the product of tail concentrations, so the earlier high-product classification is not reused after this permutation.
For each fixed choice of reservoir and its prescribed permutation, apply the coarse count (23) and the row-exposure bound (26) again in the new order.
The permuted matrix still has independent identically distributed real off-diagonal randomness and a deterministic complex symmetric shift in the same bound; (26) is uniform over that shift.
If the newly ordered full product satisfies \(\prod_{i=1}^{n_0}\rho_i(u,\beta_0)<n^{-C_1n}\), its total contribution is bounded by
\[
 \exp(o(n))\,n^{C_*n+O_a(n^\varepsilon)+O_a(1)}
 n^{D(C_0+1)}n^{-C_1n}=n^{-c n}
\]
for all sufficiently large \(n\).
Here the first factor includes all reservoir and prescribed permutation choices, and the leading entropy coefficient \(C_*\) is unchanged by permutation.
Discard this post-permutation low-product case.
For the remaining vectors, the newly ordered full product is at least \(n^{-C_1n}\), and removing its last \(q_0\) factors, each at most one, gives \(\pi_{\beta_0}(u)\ge n^{-C_1n}\) in the current order.
Take \(L=n^{K+3}\), \(t_\ell=L^\ell\beta_0\), and \(L_0=\lceil C_1/\varepsilon\rceil+2\).
Choose \(s\) so large that \(t_{L_0+1}\le t_*\).
For at least one \(0\le\ell\le L_0\),
\[
 \pi_{t_{\ell+1}}(u)\le n^{\varepsilon n}\pi_{t_\ell}(u),
 \tag{28}
\]
since otherwise iteration from \(n^{-C_1n}\) would exceed one.

Fix this \(\ell\), and partition the possible values of \(\rho_i(u,t_\ell)\) into bins \([r_h,n^\varepsilon r_h)\), with endpoints powers of \(n\), between the lower bound in (25) and the upper bound in (27).
There are only \(H=O_{s,K}(1)\) bins.
Monotonicity in \(i\) makes their index sets consecutive blocks, with sizes \(m_h\) summing to \(p\).
There are at most \((n+1)^H\) such profiles.
At the first index of each block apply the vector-valued linear inverse theorem to the entire corresponding tail, with exception count
\[
 n'=\lfloor n^{1-2\varepsilon}\rfloor.
\]
The tail has length at least \(q\), so this exception count lies in the permitted range of that theorem.
Rescale the tail if necessary; its norm is at most two, and the zero-norm case is immediate.
All but \(n'\) entries of that block can be rounded within \(t_\ell\) to a progression \(Q_h\) of bounded rank and size
\[
 |Q_h|\le C r_h^{-1}n^{-1/2+\varepsilon}.
 \tag{29}
\]
The maximum with one in the inverse theorem is harmless here: (27) implies the right side of (29) is at least a positive power of \(n\).
For clarity, if the tail norm is \(\sigma>0\), apply the inverse theorem to its normalized coefficients at radius \(t_\ell/\sigma\).
Each coordinate of a normalized generator has the form \((t_\ell/\sigma)p_{ij}/p\), so rescaling the generator by \(\sigma\) gives exactly \(t_\ell p_{ij}/p\).
The possibly irrational norm therefore cancels, and \(\sigma\le2\) bounds the integers \(p_{ij}\) and \(p\) polynomially in \(n\).
Since \(t_\ell\) is an integer power of \(n\), these rescaled real and imaginary generator coordinates are rational of polynomial height.
Thus the finitely many progressions have only polynomially many choices.
Round the at most \(Hn'+q_0+(n-n_0)=o(n)\) remaining coordinates on the complex \(t_\ell\)-lattice.
The choices of their positions and values contribute \(\exp(o(n))\), since their number is \(O(n^{1-\varepsilon})\) and the mesh has polynomial precision.

Consequently the number of rounded vectors for this profile is at most
\[
 \exp(O(n)+o(n))\,
 n^{-(1/2-\varepsilon)p}\prod_h r_h^{-m_h}.
 \tag{30}
\]
Every such rounded vector has at least one original witness in the fixed profile.
Choose one witness for each rounded vector.
This choice is made from the deterministic coefficient candidate set, before any random row-orthogonality event is imposed.
Its row tolerance is at most \(t'=\beta_0+Cn^{K+1}t_\ell\).
For every tail, comparing the rounded vector with that witness changes the sum by at most \(Cn^{K+1}t_\ell\), hence
\[
 \rho_i(u',t')\le\rho_i(u,t_{\ell+1})
\]
for all large \(n\).
Use (26), discard the last \(q_0\) tail factors, and apply (28) and the profile upper endpoints.
The probability for each rounded vector is at most
\[
 n^{O_{s,K,C_0}(1)}n^{2\varepsilon n}\prod_h r_h^{m_h}.
 \tag{31}
\]
Multiplying (30) and (31) cancels the concentration factors exactly.
Since \(p=n-o(n)\), the result is at most
\[
 \exp(O(n)+o(n))\,
 n^{-(1/2-\varepsilon)p+2\varepsilon n}
 \le n^{-n/3}
 \tag{32}
\]
eventually.
The polynomial number of profiles, bounded number of scales, and \(\exp(o(n))\) reservoir/permutation choices do not change this conclusion.
This completes the structured-vector counting bound uniformly over every allowed deterministic complex shift and deterministic diagonal.

The parameter order is noncircular.
First fix \(b,K,\varepsilon\), then the structural constant \(C_0\) and leading entropy constant \(C_*\), then \(C_1,L_0\), and finally choose \(a\) so that \(s=a-C_0\) meets the scale requirements.
Constants from the later linear inverse applications may depend on \(a\), but they affect only the polynomial number of progressions, fixed multiplicative constants to the power \(n\), and the \(\exp(o(n))\) exceptional-coordinate factors.
They do not alter the negative \(n\log n\) coefficient in (32).

## From the counting lemma to the smallest singular value

First restrict to invertible \(M\).
If \(s_{\min}(M)\le n^{-A}\), then \(\|\operatorname{adj}M\|_F\ge n^A|\det M|\).
For some row index, after paying a factor \(n\) in a union bound, its squared cofactor-row norm is at least \(n^{2A-1}|\det M|^2\).
Delete the corresponding row and column to obtain \(D\).
Cofactor expansion and Cauchy--Schwarz, with \(\max|M_{ij}|\le n^K\), give
\[
 \|r_i(\operatorname{adj}M)\|^2
 \le 2n^{2K+1}\|\operatorname{adj}D\|_F^2.
\]
Therefore \(\operatorname{adj}D\ne0\) and
\[
 \frac{|\det M|}{\|\operatorname{adj}D\|_F}
 \le\sqrt2\,n^{-A+K+1}.
 \tag{33}
\]
Choose \(A\ge2a+K+3\), so the last quantity is at most \(n^{-2a}\).
Conditional on \(D\), the off-diagonal entries of the deleted row are independent of \(D\), and the determinant divided by \(\|\operatorname{adj}D\|_F\) is a quadratic form whose quadratic matrix is, up to sign, \(A_D\).
Its linear and constant coefficients may be complex and are allowed to be arbitrary.
If its conditional concentration is below \(n^{-b}\), the event in (33) costs at most \(n^{-b}\).
Otherwise the structural consequence above produces one of the vectors counted in (23)--(32) for \(D\).
Taking \(b>B+3\) proves an \(O(n^{-B-1})\) bound for the event that \(M\) is invertible and has the stated small singular value, uniformly over \(F\).

To include matrices of every rank, no rank-boost extension is needed.
For each fixed realization of \(M\), the polynomial \(t\mapsto\det(M+tI)\) is monic of degree \(n\), so it has only finitely many real zeros.
Tonelli implies that for almost every deterministic real \(t\) in any nonempty interval, \(M+tI\) is invertible almost surely.
Choose such a \(t\) with \(0<t\le n^{-A-1}\).
The Lipschitz inequality for the least singular value gives
\[
 \{s_{\min}(M)\le n^{-A-1}\}
 \subseteq
 \{s_{\min}(M+tI)\le2n^{-A-1}\}.
\]
Apply the invertible estimate to the deterministic symmetric shift \(F+tI\), whose entries satisfy the same polynomial bound with a harmless exponent increase.
The constants are uniform in this choice of \(t\).
This proves the desired estimate for all \(M\), after increasing the final exponent by one.
Add the discarded probability \(O(n^{2-2K})\) to obtain (CS) for the original finite-variance entries.

## Independent diagonal laws and normalization

Let the raw diagonal entries instead be independent copies of a fixed real law \(\zeta\), independent of the off-diagonal variables, with \(\mathbb E|\zeta|^2<\infty\).
For any prescribed \(B\), choose \(K_d\) so large that
\[
 \mathbb P\{\max_i|\zeta_i|>n^{K_d}\}
 \le n^{1-2K_d}\mathbb E|\zeta|^2=O(n^{-B-2}).
\]
Conditional on any diagonal realization in this event's complement, absorb that diagonal into \(F\) and use the uniform deterministic-diagonal theorem.
This proves the same arbitrary polynomial failure bound for these diagonal laws, including deterministic zero diagonals.
Replacing \(X_n\) by \(W_n=X_n/\sqrt n\) only increases the deterministic-shift exponent by \(1/2\) before application and changes the final singular-value exponent by \(1/2\).
Thus the theorem applies to the normalized real-Wigner conditional shifts in the two-factor product route.

## Current assessment
[Selected decision](#decision-complex-shift-reviewed)

## Assessment history

### Decision profile-repaired-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T01:00 |
| status | open |
| reason | The profile-order gap is repaired by a second low-product classification after each reservoir permutation; the complete modified argument awaits independent recheck. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unchanged complex-symmetric theorem](#statement) | The original finite-variance shift assertion, with the same diagonal and normalization scope. |

### Decision complex-shift-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T01:12 |
| status | proved |
| reason | A fresh isolated independent whole-proof inspection checked the repaired post-permutation classification and every affected interface, with no remaining gap under the two explicitly accepted inverse-concentration inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complex-symmetric shift theorem](#statement) | Arbitrary polynomial failure exponents at fixed real second moments, with the stated diagonal, normalization, independent-shift and almost-sure extensions. |
| argument | [Complete repaired argument](#argument) | Both structural branches, all counting regimes, parameter order, cofactor reduction and rank removal. |
| review | [Fresh independent whole-proof finding](../audits/reviews/Yin_R_F0192_v2.md#finding) | Exact v2 statement and complete argument, including the repair, with original inverse-theorem proof limits disclosed. |

