---
author: Yin
---

# The remaining nonsymmetric product-inverse shift for three Wigner factors

This continuing investigation concerns the real-input part of [F0012](../tasks/Yin_T_F0012_v3.md#contract).
The complete symmetric-carrier extension and its outer-polynomial and ordered-product deductions are now fixed in [the reviewed C_F0186_v7 theorem](../claims/Yin_C_F0186_v7.md#decision-symmetric-carrier-reviewed), with its [full argument](../claims/Yin_C_F0186_v7.md#argument).
The fixed material owns its proved assessment and independent review, while this Draft retains only the continuing nonsymmetric question.
The [complex symmetric shift theorem](../claims/Yin_C_F0188_v2.md#statement) and [arbitrary-complex-shift intermediate theorem](../claims/Yin_C_F0187_v2.md#statement) retain their exact accepted scopes.

<a id="candidate"></a>
## Fixed carrier finding and remaining question

The fixed theorem covers \(R=(x_1+Q)H\) when the entire carrier is reversal symmetric and has the displayed finite conditional-shift product certificate.
Examples include \(x_1x_2x_3x_2\) and \((x_1+Q)h(x_2+Q_2)\).
Its root-factorization argument also covers the zero-shift logarithmic determinant of any finite ordered product of the displayed classes.
Consequently the zero-shift determinant of \(R=x_1x_2x_3\) is covered by that deduction; its nonzero shifts and Brown-measure convergence are the present unresolved test.

## The actual nonsymmetric shift

For real symmetric inputs, \(H=W_2W_3\) is generally not symmetric, even though both factors are.
For \(z\ne0\), conditioning on \(W_2,W_3\) and using their polynomial invertibility events gives
\[
 W_1W_2W_3-zI
 =\bigl(W_1-z(W_2W_3)^{-1}\bigr)W_2W_3.
\]
The actual shift \(-z(W_2W_3)^{-1}\) is generally not complex symmetric, so C_F0188_v2 cannot be invoked.
The accepted intermediate estimate already applies to this independent arbitrary complex shift, and its product inequality supplies the growing intermediate range of the output.
What is missing in this approach is a summable polynomial least-singular-value floor, or a weaker estimate sufficient for the bottom negative-logarithmic contribution, for this actual product-inverse shift.
The statement is an unresolved interface rather than a universal arbitrary-shift conjecture or a necessary condition for every possible proof.

## Existing source boundary

The [retained ORSV15 inspection](../ledger/Yin_L_F0061_v1.md#two-wigner-factors-are-an-informative-benchmark) gives a two-real-Wigner product theorem with additional \(2+\tau\) moments and its precise conditional-symmetry mechanism.
It does not discharge this three-factor finite-variance interface.
The focused new search and its actual source-inspection limits are recorded below.
No claim that this exact interface is a publicly named open problem is made.

<a id="symmetrized-adjugate"></a>
## A quantitative cofactor noncancellation identity

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

<a id="isolated-minor-factorization"></a>
## An isolated tiny minor reduces the bottom event to two linear forms

The following deterministic estimate bypasses recovery of a kernel vector from a single symmetrized cofactor vector.
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

## Entropy and conditioning for the isolated-minor branch

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

The counting argument in C_F0188_v2 extends to these near-kernel events for \(D=W+F\) with nonsymmetric deterministic \(F\).
As in that proof, first truncate by conditioning every independent raw entry on its polynomial bound, paying its second-moment union-bound tail; this retains independent upper entries with the uniform anti-concentration constants used there.
Condition on the independent diagonal values before the row count.
This is a proof-level adaptation, not an invocation of its symmetric-shift theorem at a larger scope.
Its row exposure uses only independent upper off-diagonal variables and the equality of the random lower variable with its upper partner.
The deterministic entry \(F_{ij}\) enters only as an arbitrary center in a linear small-ball probability; it is never replaced by \(F_{ji}\).
Each simultaneous row-and-column permutation preserves independence of the random upper family, the deterministic polynomial entry bound, and the same arbitrary-center row estimate.
The coarse count, low-product split, reservoir reorder, second low-product split, profile bins and cancellation of concentration factors therefore remain unchanged.
Apply the same argument to \(D^T=W+F^T\) for the transpose-kernel branch.
No unobserved independent witness is inserted: the union bound runs over the deterministic rational candidate set, and each rounded vector's profile witness is chosen before its random row event, exactly as in the repaired accepted count.
For \(a_0\) large after fixing \(b,K,\varepsilon\), the probability that either vector in (Structured-kernel) exists is consequently \(O(e^{-cn})\).

It follows that the determinant small-ball event restricted to (Isolated-input) has probability at most
\[
 2n^{-b}+O(e^{-cn})
\]
plus the discarded polynomial row-norm tail, when its minor has the displayed isolated tiny singular value.
A finite union over deleted row indices costs at most a factor \(n\).
This is a candidate restricted bottom-range estimate with an explicit argument; it has not undergone a separate mathematical review.
It rules out that isolated-minor mechanism at arbitrarily summable failure probability, but does not assert that every small singular value of the full matrix supplies such a minor.

## Full three-factor assembly and the first remaining unsupported step

For the original product, condition on the polynomial norm and invertibility events for \(W_2,W_3\), and set \(F=-z(W_2W_3)^{-1}\).
The accepted one-factor floors make the complements of these events arbitrarily summable, and \(F\) has a fixed polynomial norm bound.
If \(W_1W_2W_3-zI\) has an excessively small singular value, the factorization above and the lower singular bound for \(W_2W_3\) force an excessively small singular value of \(M=W_1+F\).
Apply the raw-scaled minor tests to \(\sqrt N M\), absorbing that factor into the polynomial exponents.
When \(M\) is invertible, cofactor-row expansion for this arbitrary matrix still gives an index \(i\) and a nonzero \(\operatorname{adj}D_i\) for which \(|\det M|/\|\operatorname{adj}D_i\|_F\) is polynomially small, as in the accepted cofactor reduction with the same polynomial entry losses.
That elementary expansion does not require equality of the deterministic off-diagonal shifts.
For full \(M\) of corank one, choose an omitted row whose removal preserves its rank; deleting the matching column then leaves a principal minor of corank at most one, so its adjugate is nonzero and the determinant ratio is zero.
The lower-rank full-matrix branch needs its own reduction and is not silently included in the invertible cofactor argument.

If this selected minor satisfies (Isolated-input), the preceding bottom-range estimate excludes the event at the desired summable scale.
The first unsupported step in a complete argument is coverage of the complementary minors: their least singular value can be too large to suppress the \(a\det D\) term, or more than one small singular direction can contribute substantially to the normalized adjugate.
In the former branch the rank-one product is centered at a potentially nonzero value, so the zero-product union in (Product-small-ball) is unavailable.
In the latter branch the cofactor quadratic form need not factor into two linear forms.
Neither branch is resolved merely by the symmetrized-adjugate norm bound or by the accepted intermediate estimate.
A continuation must establish an arithmetic recovery statement for those actual quadratic forms or a separate bottom-logarithm mechanism.

<a id="prepared-fixed-statement"></a>
## Precisely quantified statement prepared for a separate cofactor mechanism

The following is prepared mathematical content for a fixed candidate, not a new assessment or a reservation of a material number.
The deterministic assertion is exactly (Sym-adj)--(Sym-adj-norm).
The probabilistic assertion below is restricted to the actual isolated-minor branch and awaits independent review of the counting adaptation.

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

Candidate isolated-minor assertion.
For every \(\gamma,B>0\), there exist constants \(A,L,C,n_0>0\), depending only on the fixed laws, \(\gamma,B\), such that for all \(n\ge n_0\), uniformly over the displayed deterministic shifts,
\[
 \mathbb P\!\left\{\exists i:\ \operatorname{adj}D_i\ne0,\quad
 \frac{|\det M_n|}{\|\operatorname{adj}D_i\|_F}\le n^{-A},\quad
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

### Parameter order and complete proof interfaces

Choose an integer raw-entry cutoff exponent \(\kappa\) large enough that the second-moment union-bound error from \(|\xi|>n^\kappa\) or \(|\zeta|>n^\kappa\) is \(O(n^{-B-2})\).
Conditional on all these independent cutoffs, the strict upper entries remain iid with the conditional law \(\xi_n\), whose accepted anti-concentration constants are uniform for large \(n\).
Choose an integer \(K\) after \(\gamma,\kappa\) so all exposed row norms and diagonal magnitudes are at most \(n^K\), and every minor entry has the same polynomial bound.
Condition on the independent diagonal values in applying the counting argument.
Choose \(b>B+3\), then its linear inverse-theorem structural constants and the profile-counting constants, and finally choose \(a_0\) sufficiently large for that fixed counting setup.
Set
\[
 A=2a_0,\qquad L\ge2a_0+2K+3.
\]
The extra unit in \(L\), compared with (Isolated-input), absorbs the factor \(\sqrt n\) in (Rank-one-data).

For each fixed \(i\), condition on its minor \(D_i\).
The remaining strict off-diagonal row coordinates are independent copies of \(\xi_n\), independent of that minor, and the different deterministic row and column shifts are fixed.
If \(\mathcal I_i(L)\) holds, (Rank-one-data) or the exact singular branch gives the required rank-one decomposition.
Equations (Exposed-det)--(Product-small-ball) bound the conditional determinant event by the sum of two linear concentrations.
If both are below \(n^{-b}\), this costs at most \(2n^{-b}\).
If either is at least \(n^{-b}\), the linear inverse theorem and rounding supply a vector in (Structured-kernel), for \(D_i\) or \(D_i^T\), respectively.
The preceding entropy and row-exposure adaptation bounds the probability of either existence event by \(O(e^{-cn})\), uniformly over the nonsymmetric deterministic shift.
Those are unions over deterministic candidate vectors; conditioning on a random near-kernel vector is never substituted for the candidate-set union bound.
Thus each \(i\) contributes at most \(2n^{-b}+O(e^{-cn})\) in the truncated model.
The union over its at most \(n\) indices and the discarded raw-entry tail give (Isolated-minor-bound).
The order of constants keeps the inverse and counting structural constants fixed before the fine precision \(a_0\) is chosen, as in the repaired accepted profile argument.

### Exact input and review boundary for the prepared assertion

The only external theorem used in its entropy step is the vector-valued linear inverse Littlewood--Offord input already accepted at [Ngu12a's recorded statement and applicability scope](../audits/literature/Ngu12a/readme.md).
The existing [C_F0188_v2 argument](../claims/Yin_C_F0188_v2.md#argument) supplies its rational-grid formulation and the complete repaired counting proof.
The adaptation to nonsymmetric deterministic offsets is justified above by its actual arbitrary-center row uses, both matrix orientations, and its unchanged post-permutation low-product split.
Its old independent review is not relabeled as review of this extension.
The final candidate requires independent inspection of the exact quantified assertion and these proof interfaces before it is selected as proved.

## Bounded primary-source search and actual inspection limits

On 2026-11-05 the new question was searched under symmetric random matrices with arbitrary nonsymmetric deterministic perturbations, products of three Wigner matrices, and rank-two quadratic or product-of-two-linear-forms Littlewood--Offord concentration.
The queries repeatedly returned the symmetric-shift Nguyen theorem, the already inspected two-Wigner product benchmark, and general quadratic anticoncentration results.
The [Nguyen author-hosted 23-page preprint](https://people.math.osu.edu/nguyen.1261/cikk/singular-noLO.pdf), Theorem 1.3 on PDF p. 2 and its cofactor outline on pp. 4--8, was directly reread.
Its deterministic perturbation is symmetric, and its scalar iid arbitrary-matrix theorem in Theorem 1.1 is a different random input model.
The already retained published Ngu12 edition and theorem number remain distinguished in [its source notes](../audits/literature/Ngu12/readme.md).
An attempted web opening of ORSV15 arXiv:1403.6080v3 failed at that interface; its adequate existing retained inspection was reused rather than inferring a source change.

The publisher HTML of Matthew Kwan and Lisa Sauermann, [Resolution of the quadratic Littlewood--Offord problem](https://doi.org/10.1112/S0010437X25102789), was inspected at its abstract and introduction.
It gives quadratic point-anticoncentration in terms of robust dependence, not the finite-radius controlled-entropy near-kernel recovery needed above.
No theorem or proof from that source is adopted in this Draft, and no conclusion about absence of a suitable theorem elsewhere is asserted.
The search stopped after those scope checks because the direct adjugate and isolated-product calculations supplied the next discriminating local mechanism.