---
author: Yin
---

# Symmetrized adjugates and isolated-minor determinant bounds

This is a complete candidate argument for a separate cofactor mechanism arising in the real finite-variance part of [F0012](../tasks/Yin_T_F0012_v3.md#contract).
The probability theorem concerns specifically isolated principal minors and does not assert an arbitrary-nonsymmetric-shift least-singular-value bound.
The [accepted C_F0188_v2 theorem](../claims/Yin_C_F0188_v2.md#decision-complex-shift-reviewed) retains its exact statement and assessment.
Its repaired counting proof is adapted below only at the deterministic-offset interface its actual row exposure uses.
Its old review does not cover this new statement.

<a id="statement"></a>
## Exact deterministic and restricted probabilistic assertions

For any complex square matrix \(D\), put
\[
 S=\frac{D+D^T}{2},\qquad A=\operatorname{adj}D,\qquad Q=\frac{A+A^T}{2}.
\]
Then, including singular \(D\),
\[
 D^TQ=SA,\qquad
 \|D\|\,\|Q\|_F\ge s_{\min}(S)\|A\|_F.
 \tag{Deterministic}
\]
For \(D\ne0\), division by \(\|D\|\) gives the relative cofactor bound.
The finite example in the proof specifies the inference this bound does not supply.
Fix a real off-diagonal law \(\xi\) with \(\mathbb E\xi=0\) and \(\mathbb E\xi^2=1\), and a real diagonal law \(\zeta\) with finite second moment.
For each \(n\), let \(X_n\) be raw real symmetric Wigner: its strict upper entries are independent copies of \(\xi\), its diagonal entries are independent copies of \(\zeta\), and these families are independent.
Let \(F_n\in M_n(\mathbb C)\) be deterministic, with
\[
 \max_{i,j}|(F_n)_{ij}|\le n^\gamma,
 \qquad \gamma>0,
 \qquad M_n=X_n+F_n.
\]
No symmetry condition on \(F_n\) is imposed.
For \(1\le i\le n\), write \(D_i\) for the principal minor obtained by deleting row and column \(i\), and let \(t_1(D_i)\le t_2(D_i)\) be its two smallest singular values when \(n\ge3\).

Restricted probability assertion.
For every \(\gamma,B>0\), there exist constants \(A_0,L,C,n_0>0\), depending only on the fixed laws, \(\gamma,B\), such that for all \(n\ge n_0\), uniformly over the displayed deterministic shifts,
\[
 \mathbb P\!\left\{\exists i:\ \operatorname{adj}D_i\ne0,\quad
 \frac{|\det M_n|}{\|\operatorname{adj}D_i\|_F}\le n^{-A_0},\quad
 \mathcal I_i(L)\right\}
 \le Cn^{-B},
 \tag{Isolated-minor-bound}
\]
where \(\mathcal I_i(L)\) is the disjunction
\[
 \operatorname{rank}D_i=n-2
\]
or
\[
 D_i\text{ is invertible},\qquad
 t_1(D_i)\le n^{-L},\qquad
 t_1(D_i)/t_2(D_i)\le n^{-L}.
\]
The first branch has exact rank-one adjugate, and the second has the quantitatively isolated smallest singular value specified above.
No estimate for the complement of these branches is included.
In particular (Isolated-minor-bound) is not a bound for \(s_{\min}(M_n)\) without its explicit minor conditions.

The same bound is uniform conditionally on an independent random \(F_n\) whenever its displayed entry bound holds.
Without imposing that entry bound surely, its failure probability is added to the right side after conditioning.
For \(B>1\), the restricted bad event therefore occurs only finitely often almost surely under every cross-size coupling for which those extra failures are summable.


## Exact inputs and source applicability

The vector-valued linear inverse Littlewood--Offord theorem is [Ngu12a, arXiv:1105.5733v1, Condition 1 and Theorem 1.3, PDF pp. 2--3](../audits/literature/Ngu12a/readme.md), at the retained statement-and-applicability inspection depth.
Its original proof remains an accepted external input, not a new source-proof review.
Its coefficient dimension two represents complex coefficients, while its random scalar variables remain real.
The [source conventions](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) specify the progressions and concentration functions used below.

[C_F0188_v2](../claims/Yin_C_F0188_v2.md#argument) supplies the rational-grid formulation and complete repaired profile-counting mechanism.
The nonsymmetric-offset adaptation is given explicitly below; its final symmetric-shift theorem is not invoked for a nonsymmetric shift.
Only the optional consequence of the deterministic identity for \(W+F\) uses that accepted theorem for the genuinely symmetric shift \(W+\operatorname{sym}F\).
The isolated-minor probability proof itself uses the linear inverse theorem and the row count, without the quadratic inverse theorem.

<a id="argument"></a>
## Complete candidate argument

<a id="cofactor-identity"></a>
### The symmetrized-adjugate identity and its exact limitation
For an arbitrary complex square matrix \(D\), put
\[
 S=\frac{D+D^T}{2},\qquad A=\operatorname{adj}D,\qquad
 Q=\frac{A+A^T}{2}.
\]
The adjugate identities imply, even when \(D\) is singular,
\[
 D^TQ=SA.
 \tag{Sym-adj}
\]
Indeed, \(D^TA^T=(AD)^T=(\det D)I\), while \(DA=(\det D)I\); expanding both sides proves the equality.
Thus, if \(D\ne0\),
\[
 \|Q\|_F\ge\frac{s_{\min}(S)}{\|D\|}\|A\|_F.
 \tag{Sym-adj-norm}
\]
Here multiplication on the left by \(S\) controls Frobenius norm by \(s_{\min}(S)\), and multiplication by \(D^T\) costs at most \(\|D\|\).
The same statement is vacuous when \(A=0\).

For \(D=W+F\), where \(W\) is a real Wigner matrix and \(F\) is an independent polynomially bounded complex matrix without a symmetry assumption, the symmetric part is
\[
 S=W+\frac{F+F^T}{2}.
\]
Conditional on \(F\), C_F0188_v2 applies to \(S\), while the second-moment polynomial norm event bounds \(D\).
Consequently, outside an arbitrarily summable polynomial failure probability, (Sym-adj-norm) gives
\[
 \|\operatorname{sym}\operatorname{adj}D\|_F
 \ge N^{-C}\|\operatorname{adj}D\|_F
\]
for an appropriate fixed exponent \(C\).
This also applies to each actual principal minor after the harmless normalization change from \(N\) to \(N-1\).
Thus skew cancellation cannot erase the entire quadratic cofactor scale in the arbitrary-shift problem.
It does not itself supply a near-kernel vector: a row of \(Q\) need not be a row of \(A\), and (Sym-adj) is not the relation \(DQ\approx0\).

For example, take
\[
 D=\begin{pmatrix}1&1\\-1&-1\end{pmatrix},\qquad
 S=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 A=\begin{pmatrix}-1&-1\\1&1\end{pmatrix},\qquad
 Q=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
The symmetric part is well conditioned and the adjugate has exact rank one, but either coordinate row of \(Q\) has residual of norm \(\sqrt2\) under both \(D\) and \(D^T\).
Thus a structured row of the symmetric quadratic coefficient is not automatically a near-kernel vector, even in exact rank one.
This finite deterministic example refutes that particular inference, not invertibility of random Wigner perturbations or the possibility of recovering another structured kernel vector.


<a id="truncation"></a>
### Raw-entry truncation and uniform anti-concentration

Fix the desired failure exponent \(B\) and shift exponent \(\gamma\).
Choose an integer \(\kappa\) so the second-moment union bound over all raw entries gives
\[
 \mathbb P\{\text{some raw entry exceeds }n^\kappa\}=O(n^{-B-2}).
\]
Condition on these independent truncations.
The strict upper entries remain iid with law \(\xi_n=(\xi\mid|\xi|\le n^\kappa)\).
Nondegeneracy of \(\xi\) gives fixed \(c_1,c_2,c_3>0\) such that eventually
\[
 \mathbb P\{c_1\le|\xi_n-\xi_n'|\le c_2\}\ge c_3.
 \tag{AC}
\]
Indeed some bounded positive interval has positive mass for \(|\xi-\xi'|\), and the conditional laws converge in total variation.
The corresponding selector-symmetrized laws in the inverse and counting arguments have the same uniform anti-concentration property.
No centering of the truncated law is required.

Choose an integer \(K\) large after \(\kappa,\gamma\), so every exposed diagonal magnitude and row norm and every truncated minor entry has the bound \(n^K\).
Condition on the independent diagonal values during row counting.
Choose \(b>B+3\) and fix \(\varepsilon=1/100\).
All structural and coarse entropy constants are selected before the fine precision below.

<a id="isolated-row-reduction"></a>
### The isolated-minor row calculation
We use the following deterministic zero-product reduction for an isolated minor.
For the following row and entropy calculations use raw Wigner scaling, so the exposed coordinates are copies of the fixed law rather than its \(1/\sqrt N\) scaling.
Multiplication of the original conditional matrix by \(\sqrt N\) changes only fixed polynomial exponents and is absorbed before this calculation.
Write a row-exposed matrix as
\[
 M=\begin{pmatrix}a&(x+f)^T\\x+g&D\end{pmatrix},
 \qquad
 \det M=a\det D-(x+f)^T(\operatorname{adj}D)(x+g).
 \tag{Exposed-det}
\]
The two deterministic shifts \(f,g\) can differ, while \(x\) has independent real coordinates and is independent of \(D\).
Suppose \(A=\operatorname{adj}D\ne0\), and write
\[
 \frac A{\|A\|_F}=\alpha uv^T+E,
 \qquad \|u\|=\|v\|=1,\qquad |\alpha|\ge\tfrac12.
\]
On an event where
\[
 |a|,\ \|x+f\|,\ \|x+g\|\le n^K,
 \quad
 \frac{|\det D|}{\|A\|_F}\le n^{-L},
 \quad \|E\|\le n^{-L},
 \tag{Isolated-input}
\]
(Exposed-det) differs from
\[
 -\alpha\,[u^T(x+f)]\,[v^T(x+g)]
\]
after division by \(\|A\|_F\) by at most \(2n^{2K-L}\).
Choose \(L\ge2a_0+2K+2\).
Then
\[
 \left\{\frac{|\det M|}{\|A\|_F}\le n^{-2a_0}\right\}
 \cap\{\text{the bounds in (Isolated-input)}\}
 \subset
 \{|u^T(x+f)|\le2n^{-a_0}\}
 \cup
 \{|v^T(x+g)|\le2n^{-a_0}\}.
 \tag{Product-small-ball}
\]
In particular its conditional probability is bounded by the sum of the two linear concentration functions at radius \(2n^{-a_0}\), plus the probability of failure of the row norm bounds.
The two linear forms are not assumed independent.
The set inclusion, rather than a multiplication of their probabilities, is the required argument.

Let \(t_1\le t_2\le\cdots\) be the singular values of \(D\).
If \(D\) is invertible, its singular-value decomposition supplies unit vectors \(u,v\) with
\[
 \|Du\|=\|D^Tv\|=t_1,
 \qquad
 \frac{|\det D|}{\|A\|_F}\le t_1,
 \qquad
 \|E\|_F\le\sqrt n\,t_1/t_2.
 \tag{Rank-one-data}
\]
The amplitude is
\[
 |\alpha|=
 \left(1+\sum_{j\ge2}(t_1/t_j)^2\right)^{-1/2}.
\]
Thus \(t_1\le n^{-L}\) and \(t_1/t_2\le n^{-L-1}\) imply (Isolated-input) and \(|\alpha|\ge1/2\) eventually.
For an exactly rank-\((n-1)\) minor, \(\det D=0\) and the adjugate has exact rank one; take \(E=0\), \(|\alpha|=1\), and both near-kernel residuals zero.
The rank-\((n-2)\)-or-smaller branch has \(A=0\) and is not covered by this particular estimate.

Under the polynomial norm bound \(t_2\le\|D\|\le n^K\), a sufficiently strong relative gap already forces the absolute smallness used above:
\[
 t_1/t_2\le n^{-L-K-1}\quad\Longrightarrow\quad t_1\le n^{-L-1}.
\]
Therefore a sufficiently accurate rank-one approximation of the normalized adjugate cannot coexist with a well-conditioned minor in this bounded-norm setting.
The genuinely nonzero-centered cofactor branch is part of the regime without the required rank-one dominance, rather than an extra rank-one case settled by the same product union.


<a id="counting-class"></a>
### Exact structured class and nonsymmetric-offset interface

For the next module let \(n\) denote its matrix size.
Its use for a size-\((n-1)\) principal minor changes only fixed polynomial slack and sufficiently-large-size constants.
Fix \(C_0,K\) independently of the fine precision \(a\).
This precision is the parameter denoted \(a_0\) in the isolated row calculation and final assembly; set \(a=a_0\) when applying this module.
The structured candidates have norm between \(1/2\) and two, with all but \(C_0n^\varepsilon\) coordinates in a generalized arithmetic progression of rank at most \(C_0\) and size at most \(n^{C_0}\), with the polynomially bounded integer box supplied by the inverse theorem.
Each real and imaginary coordinate of the candidate and the progression generators is rational with numerator and denominator at most \(n^{a+C_0}\).
Let
\[
 \beta_0=n^{-a+C_0}.
\]
The counted event is existence of such a vector satisfying \(|(Du)_i|\le\beta_0\) on at least \(n-C_0\) prescribed rows.
The linear inverse theorem and rounding in the application produce precisely this class.

In the following proof the deterministic entries \(F_{ij}\) enter only as arbitrary centers in linear small-ball probabilities.
No equality \(F_{ij}=F_{ji}\) is used.
A simultaneous row-and-column permutation preserves the iid symmetric random upper family, deterministic diagonal, and the entry bound even when \(F\) is nonsymmetric.
For the transpose branch the same proof applies to \(D^T=X+F^T\).
Every candidate and profile witness is selected from a deterministic coefficient set before a random row-orthogonality event is imposed.
<a id="structured-vector-counting"></a>
### Complete profile count with nonsymmetric offsets

We prove that a matrix \(D=X+F\), with symmetric real iid off-diagonal randomness satisfying (AC), deterministic diagonal, and arbitrary possibly nonsymmetric complex \(F\), all within the polynomial entry bound, has a vector in the structured class defined above with probability at most \(\exp(-cn)\), once \(a\) is chosen sufficiently large.
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
 \rho_i(u,t)\ge n^{-D_0},
 \tag{25}
\]
where \(D_0=O(s+K)\), also for coefficient vectors within distance \(O(\beta_0)\) coordinatewise of the norm-bounded vectors considered here.
The same lower bound, with an enlarged \(D\), applies to every rounded vector below.

Condition first on entries connecting the bulk to its complement, and then expose the bulk rows in increasing order.
The random part left in row \(i\) consists of strictly upper entries, so its conditional small-ball bound is \(\rho_{i+1}(u,t)\).
Omitting the at most \(C_0\) unconstrained rows and using (25) proves
\[
 \mathbb P\{|(Du)_i|\le t\text{ on the prescribed rows}\}
 \le n^{D_0(C_0+1)}\prod_{i=1}^{n_0}\rho_i(u,t).
 \tag{26}
\]
This is the precise deterministic-diagonal adjustment: the shifted product starting at \(\rho_2\) loses only \(\rho_1^{-1}\), not one loss per row.
By (AC) and (24), for \(t\le c/\sqrt n\), each tail concentration is at most a fixed \(p_0<1\).
The direct row-exposure bound is consequently \(p_0^{n_0-C_0-1}\) at this resolution.

Choose \(C_1>C_*+10\).
For vectors with \(\prod_{i=1}^{n_0}\rho_i(u,\beta_0)<n^{-C_1n}\), (23) and (26) already give total probability \(n^{-cn}\).
It remains to count vectors with the reverse inequality.
Put
\[
 q=\lceil n^{1-\varepsilon}\rceil,\qquad
 \theta=\varepsilon/10,\qquad
 t_*=n^{-K-5}.
\]
Call a vector degenerate if every \(q\)-element subset of its bulk coordinates has concentration at least \(q^{-1/2+\theta}\) at radius \(t_*\).
For each such subset, apply the linear inverse theorem with allowed exception count \(\lfloor q/2\rfloor\).
The progression-size bound becomes
\[
 |Q|\le\max\{Cq^{-\theta},1\}=1
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

For a nondegenerate vector, select a \(q\)-subset with concentration below \(q^{-1/2+\theta}\), and include the large coordinate if it is not already in that set.
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
The permuted matrix still has independent identically distributed real off-diagonal randomness and a deterministic complex shift in the same bound; (26) is uniform over that shift.
If the newly ordered full product satisfies \(\prod_{i=1}^{n_0}\rho_i(u,\beta_0)<n^{-C_1n}\), its total contribution is bounded by
\[
 \exp(o(n))\,n^{C_*n+O_a(n^\varepsilon)+O_a(1)}
 n^{D_0(C_0+1)}n^{-C_1n}=n^{-c n}
\]
for all sufficiently large \(n\).
Here the first factor includes all reservoir and prescribed permutation choices, and the leading entropy coefficient \(C_*\) is unchanged by permutation.
Discard this post-permutation low-product case.
For the remaining vectors, the newly ordered full product is at least \(n^{-C_1n}\), and removing its last \(q_0\) factors, each at most one, gives \(\pi_{\beta_0}(u)\ge n^{-C_1n}\) in the current order.
Take \(R_n=n^{K+3}\), \(t_\ell=R_n^\ell\beta_0\), and \(L_0=\lceil C_1/\varepsilon\rceil+2\).
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

<a id="inverse-rounding"></a>
### Exact linear inverse-theorem and rounding interface

The vector-valued linear inverse Littlewood--Offord input already adopted in C_F0188_v2 applies separately to each unit coefficient vector \(u\) or \(v\).
If either concentration in (Product-small-ball) exceeds \(n^{-b}\), it supplies a polynomial-size bounded-rank progression for all but \(O(n^\varepsilon)\) coordinates, at radius \(O(n^{-a_0})\), with the accepted rational-generator description.
Round the exceptional coordinates on the same rational complex lattice and the other coordinates to their progression representatives.
The resulting vector \(w\) has norm between \(1/2\) and two and approximates the corresponding singular vector coordinatewise within \(O(n^{-a_0})\).
Because the entries of \(D\) are at most \(n^K\), (Rank-one-data) gives
\[
 \|Dw\|_\infty\le t_1+O(n^{-a_0+K+1})
 \quad\text{or}\quad
 \|D^Tw\|_\infty\le t_1+O(n^{-a_0+K+1}),
 \tag{Structured-kernel}
\]
respectively.
Choose the structural constant larger than \(K+1\), as in the accepted counting setup.
The candidate set has the same form as C_F0188_v2's structured-vector counting class, with its leading \(n\log n\) entropy coefficient independent of \(a_0\).
The exceptional-coordinate and generator precision costs remain \(\exp(o(n))\) for each fixed chosen \(a_0\).

The full count above applies to each matrix and its transpose, uniformly over their nonsymmetric deterministic offsets.
It therefore bounds the existence of either rounded near-kernel witness by the exponential probability just obtained.
The union is over deterministic candidates, with profile witnesses selected before the corresponding random row events.
The two exposed linear forms are combined by a union bound, without an independence assumption.
<a id="probability-assembly"></a>
### Final parameter order and probability assembly

Choose an integer raw-entry cutoff exponent \(\kappa\) large enough that the second-moment union-bound error from \(|\xi|>n^\kappa\) or \(|\zeta|>n^\kappa\) is \(O(n^{-B-2})\).
Conditional on all these independent cutoffs, the strict upper entries remain iid with the conditional law \(\xi_n\), whose accepted anti-concentration constants are uniform for large \(n\).
Choose an integer \(K\) after \(\gamma,\kappa\) so all exposed row norms and diagonal magnitudes are at most \(n^K\), and every minor entry has the same polynomial bound.
Condition on the independent diagonal values in applying the counting argument.
Choose \(b>B+3\), then its linear inverse-theorem structural constants and the profile-counting constants, and finally choose \(a_0\) sufficiently large for that fixed counting setup.
Set
\[
 A_0=2a_0,\qquad L\ge2a_0+2K+3.
\]
The extra unit in \(L\), compared with (Isolated-input), absorbs the factor \(\sqrt n\) in (Rank-one-data).

For each fixed \(i\), condition on its minor \(D_i\).
The remaining strict off-diagonal row coordinates are independent copies of \(\xi_n\), independent of that minor, and the different deterministic row and column shifts are fixed.
If \(\mathcal I_i(L)\) holds, (Rank-one-data) or the exact singular branch gives the required rank-one decomposition.
Equations (Exposed-det)--(Product-small-ball) bound the conditional determinant event by the sum of two linear concentrations.
If both are below \(n^{-b}\), this costs at most \(2n^{-b}\).
If either is at least \(n^{-b}\), the linear inverse theorem and rounding supply a vector in (Structured-kernel), for \(D_i\) or \(D_i^T\), respectively.
The complete profile count and its nonsymmetric-offset adaptation above bound the probability of either existence event by \(O(e^{-cn})\), uniformly over the nonsymmetric deterministic shift.
Those are unions over deterministic candidate vectors; conditioning on a random near-kernel vector is never substituted for the candidate-set union bound.
Thus each \(i\) contributes at most \(2n^{-b}+O(e^{-cn})\) in the truncated model.
The union over its at most \(n\) indices and the discarded raw-entry tail give (Isolated-minor-bound).
The order of constants keeps the inverse and counting structural constants fixed before the fine precision \(a_0\) is chosen, as in the repaired accepted profile argument.
For an independent random shift, condition on its realization and integrate the uniform estimate on the polynomial-bound event, adding the complementary probability.
First Borel--Cantelli gives the asserted finite occurrence of the restricted bad events under arbitrary cross-size coupling whenever their marginal bounds are summable.


## Limited application boundary

The \(2\times2\) example refutes one transfer from a structured symmetrized cofactor row to a near-kernel vector.
It does not refute the original Brown-measure Task.
The positive theorem excludes only its displayed isolated-minor determinant branch.
It does not establish that every excessively small full-matrix singular value yields such a minor.
Well-conditioned or clustered-bottom minors and a separate lower-rank full-matrix reduction remain outside its assertion.
Thus the actual three-factor shift \(F=-z(W_2W_3)^{-1}\) receives only this restricted estimate on its polynomial norm events, without a full nonzero-shift determinant or Brown theorem.

## Current assessment

[Selected decision](#decision-isolated-minor-candidate)

## Assessment history

### Decision isolated-minor-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T08:04 |
| status | open |
| reason | The deterministic cofactor assertions and complete restricted probability proof are prepared for independent mathematical review, including the nonsymmetric-offset counting adaptation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact cofactor and isolated-minor assertions](#statement) | Deterministic identity and inequality, restricted principal-minor probability bound, independent random-shift extension and summable arbitrary-coupling consequence. |
| argument | [Complete restricted argument](#argument) | Adjugate identities, exact failed-inference example, independent truncation, rank-one factorization, full profile count, linear inverse-theorem rounding and union bounds. |
| dependency | [Linear inverse concentration](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) | Dimension-two linear inverse Littlewood--Offord input at the exact arXiv v1 statement/applicability scope recorded in its source notes; original proof accepted externally. |
| dependency | [Retained repaired mechanism](../claims/Yin_C_F0188_v2.md#argument) | Rational-grid formulation and repaired profile-counting proof, with deterministic-offset adaptation supplied in this argument; no larger-scope use of its final symmetric-shift theorem. |
| dependency | [Exact symmetric-part input](../claims/Yin_C_F0188_v2.md#decision-complex-shift-reviewed) | Only the optional cofactor-noncancellation consequence for W plus an independent symmetric polynomially bounded shift; the main isolated-minor proof does not use a nonsymmetric extension of this theorem. |
