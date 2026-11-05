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

## Fixed cofactor controls

The [reviewed cofactor theorem](../claims/Yin_C_F0194_v1.md#decision-isolated-minor-reviewed) owns the complete symmetrized-adjugate identity, its exact failed row-to-kernel inference example, and the isolated-minor probability bound.
Its [fixed proof](../claims/Yin_C_F0194_v1.md#argument) supplies the rank-one factorization, complete nonsymmetric-offset profile adaptation, parameter order and summable arbitrary-coupling conclusion.
The theorem controls only its explicitly isolated or exactly corank-one principal-minor branches.
The argument below retains the actual full-product assembly and its uncovered cases, rather than duplicating the fixed proof.

## Full three-factor assembly and the first remaining unsupported step

For the original product, condition on the polynomial norm and invertibility events for \(W_2,W_3\), and set \(F=-z(W_2W_3)^{-1}\).
The accepted one-factor floors make the complements of these events arbitrarily summable, and \(F\) has a fixed polynomial norm bound.
If \(W_1W_2W_3-zI\) has an excessively small singular value, the factorization above and the lower singular bound for \(W_2W_3\) force an excessively small singular value of \(M=W_1+F\).
Apply the raw-scaled minor tests to \(\sqrt N M\), absorbing that factor into the polynomial exponents.
When \(M\) is invertible, cofactor-row expansion for this arbitrary matrix still gives an index \(i\) and a nonzero \(\operatorname{adj}D_i\) for which \(|\det M|/\|\operatorname{adj}D_i\|_F\) is polynomially small, as in the accepted cofactor reduction with the same polynomial entry losses.
That elementary expansion does not require equality of the deterministic off-diagonal shifts.
For full \(M\) of corank one, choose an omitted row whose removal preserves its rank; deleting the matching column then leaves a principal minor of corank at most one, so its adjugate is nonzero and the determinant ratio is zero.
The separate [candidate lower-rank reduction](#corank-one-candidate) below addresses full corank at least two by a leading-principal rank chain; it is not part of the isolated-minor theorem or a proof of nonsingularity.

If this selected minor satisfies the exact hypotheses of the reviewed C_F0194_v1 isolated-minor theorem, that bound excludes the event at the desired summable scale.
The first unsupported step in a complete argument is coverage of the complementary minors: their least singular value can be too large to suppress the \(a\det D\) term, or more than one small singular direction can contribute substantially to the normalized adjugate.
In the former branch the scalar diagonal term need not be negligible, so the reviewed zero-product union is unavailable.
In the latter branch the cofactor quadratic form need not factor into two linear forms.
Neither branch is resolved merely by the symmetrized-adjugate norm bound or by the accepted intermediate estimate.
A continuation must establish an arithmetic recovery statement for those actual quadratic forms or a separate bottom-logarithm mechanism.

<a id="corank-one-candidate"></a>
## A separate high-probability reduction to full corank at most one

The following candidate addresses only the lower-rank full-matrix branch.
It uses the complete nonsymmetric-offset counting module already proved inside [C_F0194_v1](../claims/Yin_C_F0194_v1.md#structured-vector-counting), without assuming an isolated singular value or a determinant-ratio event.
It is ordinary proof development and has not received an independent review.

Let \(X_n\) have exactly the raw real symmetric Wigner laws in [C_F0194_v1's statement](../claims/Yin_C_F0194_v1.md#statement), and let \(F_n\) be deterministic complex matrices with \(\max_{i,j}|(F_n)_{ij}|\le n^\gamma\).
The proposed conclusion is that for every fixed \(\gamma,B>0\),
\[
 \mathbb P\{\operatorname{rank}(X_n+F_n)\le n-2\}\le Cn^{-B}
 \tag{Rank-tail}
\]
for all sufficiently large \(n\), uniformly over these shifts.
It neither excludes corank exactly one nor estimates a positive smallest singular value.

### Universal kernel anti-concentration from the existing counting module

Fix an arbitrary exponent \(b>0\) and a polynomial entry exponent \(K\).
Work first in the independently truncated model used by the fixed proof: its real scalar off-diagonal law \(\xi_n\) has the uniform symmetrized anti-concentration property (AC), and every matrix entry is bounded by \(m^K\) at the size \(m\) under consideration.
Diagonal entries can be conditioned on because the counting bound is uniform over all deterministic diagonal values in this range.
For a unit complex vector \(u\in\mathbb C^m\), define
\[
 \rho_{m^{-a},\xi_n}(u)
 :=\sup_{z\in\mathbb C}\mathbb P\left\{
       \left|\sum_{j=1}^m u_j\xi_{n,j}-z\right|\le m^{-a}\right\},
\]
where the \(\xi_{n,j}\) are independent copies of the truncated real law.
There is a fixed sufficiently large precision exponent \(a\), selected after \(b,K\), for which a measurable exceptional event \(\mathcal R_m\) has probability at most \(Ce^{-cm}\) and, on its complement,
\[
 \begin{split}
 Du=0,\quad\|u\|_2=1
 &\quad\Longrightarrow\quad \rho_{m^{-a},\xi_n}(u)\le m^{-b},\\
 D^Tv=0,\quad\|v\|_2=1
 &\quad\Longrightarrow\quad \rho_{m^{-a},\xi_n}(v)\le m^{-b}.
 \end{split}
 \tag{Kernel-AC}
\]
Here \(D\) is a random size-\(m\) principal block with an arbitrary nonsymmetric deterministic offset in the polynomial bound.
The quantifier in (Kernel-AC) is over all unit kernel vectors, not only an adjugate or singular-vector choice.

To check this consequence, suppose that a unit right-kernel vector \(u\) has concentration greater than \(m^{-b}\) at radius \(m^{-a}\).
Apply the same dimension-two linear inverse theorem and [rational rounding interface](../claims/Yin_C_F0194_v1.md#inverse-rounding) used in the fixed proof, identifying complex coefficients with two-dimensional real vectors while the scalar randomness stays real.
Its structural rank, progression size and exceptional-count constants depend on \(b\), the chosen fixed exception exponent, and the uniform (AC) constants, rather than on the eventual fine precision \(a\).
It gives a vector \(w\) of norm between \(1/2\) and two, with \(\|w-u\|_\infty\le C m^{-a}\), in the rational progression class of [C_F0194_v1](../claims/Yin_C_F0194_v1.md#counting-class).
For all rows,
\[
 \|Dw\|_\infty
 =\|D(w-u)\|_\infty\le C m^{K+1-a}.
 \tag{Kernel-rounding}
\]
Enlarge its fixed structural constant to exceed \(K+2\), absorbing the fixed factor \(C\).
Then (Kernel-rounding) is within the row tolerance of that counting class.
The complete profile count excludes existence of such a \(w\) with probability at most \(Ce^{-cm}\).
The same argument for \(D^T\) gives the second line of (Kernel-AC).
There is no rank-one approximation in this deduction: the residual is zero because \(u\) is an actual kernel vector.
Take \(\mathcal R_m\) to be the union of those two finite structured-candidate existence events.
This makes it measurable and covers every possible high-concentration unit kernel vector without a measurability assumption on a supremum over kernels.
The noncircular parameter choice is precisely the one in the fixed counting module: structural constants first, then the sufficiently fine \(a\), with all later exceptional-coordinate costs subexponential.

### Bordered rank and its measurable kernel choices

For any singular complex \(m\)-by-\(m\) matrix \(D\), choose unit vectors \(u(D)\in\ker D\), \(v(D)\in\ker D^T\) measurably.
One explicit choice is to stratify by rank, take the lexicographically first nonzero maximal minor with row set \(I\) and column set \(J\), and take the first \(j_0\notin J\).
Set the \(j_0\)-th free coordinate to one, the other free coordinates to zero, and solve
\[
 u_J=-D_{I,J}^{-1}D_{I,j_0}.
\]
The rows indexed by \(I\) span the row space, so this vector lies in the full kernel; normalize it by its positive Euclidean norm.
For rank zero use \(e_1\).
The rank strata and maximal-minor choices are Borel, and the displayed coordinate functions are rational on each such stratum, giving the required measurable choice.
Apply the same construction to \(D^T\) for \(v\).

Consider the bordered matrix
\[
 M=\begin{pmatrix}D&c\\r^T&a\end{pmatrix}.
\]
If \(r^Tu\ne0\), then \(r^T\) is outside the row space of \(D\).
If \(v^Tc\ne0\), then \(c\) is outside the column space of \(D\).
When both hold,
\[
 \operatorname{rank}M=\operatorname{rank}D+2,
 \tag{Border-rank}
\]
regardless of \(a\).
Indeed choose invertible row and column transformations carrying \(D\) to \(\operatorname{diag}(I_q,0)\), eliminate the identity block, and inspect the remaining block
\[
 \begin{pmatrix}0_{(m-q)\times(m-q)}&c_0\\r_0^T&a'\end{pmatrix}.
\]
The two nonzero vectors \(c_0,r_0\) make its rank exactly two.
This calculation is over \(\mathbb C\); the transpose rather than adjoint in the left-kernel condition is intentional.

For a Wigner border, write \(r=x+f\), \(c=x+g\), where the coordinates of \(x\) have law \(\xi_n\) and are independent of \(D\); the shifts \(f,g\) can differ.
On the complement of \(\mathcal R_m\), the failure of (Border-rank) is contained in
\[
 \{u(D)^T(x+f)=0\}\ \cup\ \{v(D)^T(x+g)=0\}.
\]
Conditional on \(D\), its probability is at most \(2m^{-b}\) by (Kernel-AC).
The two linear forms use the same \(x\); only a union bound is used, not an independence assertion.
Including the exceptional guard gives
\[
 \mathbb P\{D\text{ singular and }
        \operatorname{rank}M<\operatorname{rank}D+2\}
 \le 2m^{-b}+Ce^{-cm}.
 \tag{Border-failure}
\]
The diagonal border variable plays no role in this bound.

### One leading-principal chain gives the full rank tail

Choose a raw cutoff exponent \(\kappa\) so the probability that any full size-\(n\) raw Wigner variable exceeds \(n^\kappa\) is at most \(Cn^{-B-2}\), by the finite-second-moment union bound.
Condition on all those independent cutoffs simultaneously.
The upper off-diagonal variables remain independent with the single law \(\xi_n\), while all diagonal values can be conditioned on.
Set \(k_0=\lfloor n/3\rfloor\), and let \(M_k\) be the leading size-\(k\) principal block of \(X_n+F_n\), for \(k_0\le k\le n\).
These blocks are taken within this one matrix; no consistency between different physical sizes is assumed.
For all large \(n\), \(n/k\le4\) on the chain.
Thus \(n^\gamma\le k^{\gamma+1}\), \(n^\kappa\le k^{\kappa+1}\), and one fixed entry exponent \(K\) works for every block and exposed border on the chain.
The (AC) constants of \(\xi_n\) are uniform in \(n\).
The counting proof and inverse theorem use only those constants and the polynomial entry bound, so the same \(a,b,K\) and exponential-count constants work for all these blocks, even though the cutoff is indexed by \(n\) rather than \(k\).
In particular the two offsets in each border are deterministic and polynomially bounded, and the remaining border randomness is independent of the current principal block.

Choose \(b>B+4\) and apply (Border-failure) to every step from \(k\) to \(k+1\).
A union bound makes their total failure probability at most \(Cn^{1-b}+Ce^{-c'n}\).
On the complementary event, write \(d_k=k-\operatorname{rank}M_k\).
If \(d_k>0\), then (Border-rank) gives \(d_{k+1}=d_k-1\).
If \(d_k=0\), rank monotonicity gives \(d_{k+1}\in\{0,1\}\).
Once the deficiency is at most one, it therefore stays at most one.
Starting from \(d_{k_0}\le k_0\), it reaches that region within at most \(k_0\) steps, and \(n-k_0\ge k_0\).
Consequently \(d_n\le1\).
Adding the discarded full raw-entry tail proves (Rank-tail), with room in the requested exponent.
The argument is uniform over \(F_n\); no symmetry of that deterministic offset was used.

<a id="product-corank-reduction"></a>
### Consequence for the original three-factor object

An independent random \(F_n\) is treated by conditioning on its dimensionwise realization on the polynomial-bound event and adding that event's failure probability.
For the original fixed nonzero \(z\), set
\[
 M_N=W_1^{(N)}-z(W_2^{(N)}W_3^{(N)})^{-1}.
\]
The accepted one-factor norm and inverse bounds make the shift polynomially bounded outside arbitrarily summable failures, and it is independent of \(W_1^{(N)}\) within each dimension.
Apply (Rank-tail) after multiplying by \(\sqrt N\), which affects only its fixed polynomial exponent.
Right multiplication by the invertible \(W_2^{(N)}W_3^{(N)}\) preserves rank, so the same tail controls
\[
 \operatorname{corank}(W_1^{(N)}W_2^{(N)}W_3^{(N)}-zI_N)\ge2.
\]
For an exponent \(B>1\), first Borel--Cantelli would give eventual corank at most one under every allowed cross-dimensional coupling.
This completes the proposed lower-rank reduction, conditional only on the already accepted counting interface used explicitly above, and awaits fresh scrutiny as a new deduction.
It leaves the full corank-one and the well-conditioned or clustered-minor floor branches unresolved.

<a id="rank-growth-attribution"></a>
### Actual known mechanism and this adaptation's boundary

The rank-growth mechanism is already present in Costello--Tao--Vu, *Random symmetric matrices are almost surely non-singular*, arXiv:math/0505156v1, Section 2, equation (1), Lemma 2.4 on PDF p. 3, and its proof on pp. 11--12.
The selected original is retained as [CTV06--arxiv-v1.pdf](../literature/pdf/CTV06--arxiv-v1.pdf), with its [edition and source note](../audits/literature/CTV06/readme.md).
Their singular-border argument concerns symmetric matrices and Bernoulli borders, and its proof explicitly uses symmetry to infer a rank increase of two from a rank-increasing column.
The nonsymmetric deterministic-offset argument here separately controls both a right-kernel and a transpose-left-kernel linear form by the reviewed C_F0194 counting module.
The source's full nonsingularity proof also needs the separate invertible-border quadratic step, which is not imported here.
The source's phrase almost surely means probability tending to one in that paper, whereas the arbitrary-cross-size almost-sure consequence above uses its own summable bounds and first Borel--Cantelli.
Only this mechanism attribution and the stated passages were checked; no novelty claim or whole-paper proof audit is made.

## A paired-cofactor identity for the complementary branch

This is a continuing algebraic lead, without an adopted small-value conclusion.
For an actual minor D put S=(D+D^T)/2 and K=(D-D^T)/2, and assume S is invertible.
With Q=sym adj D as in the fixed theorem, direct multiplication gives
\[
 T=D S^{-1}D^T=S-KS^{-1}K,\qquad TQ=(\det D)I.
\]
Indeed the fixed identity D^T Q=S adj D implies the second equality after multiplying by D S^{-1} on the left.
Expanding (S+K)S^{-1}(S-K) proves the first equality.
There is also an exact complex-symmetric block realization:
\[
 \mathcal B=\begin{pmatrix}S&-K\\K&-S\end{pmatrix},
 \qquad \mathcal B^T=\mathcal B.
\]
Its Schur complement about \(-S\) is \(S-KS^{-1}K=T\).
Writing \(y=S^{-1}Kq\), the equation \(Tq=(\det D)a\) becomes the coupled system
\[
 S q-Ky=(\det D)a,\qquad Kq-Sy=0.
\]
For \(D=X+F\), the random part of this block pencil is \(\operatorname{diag}(X,-X)\).
It consists of two coupled copies of the same Wigner matrix, so complex symmetry alone does not make it an iid Wigner matrix of size \(2N\) to which the scalar symmetric-shift floor applies.
Treating \(Ky\) as a free center when \(K\) has full rank retains a full-dimensional precision cost.
In the actual product-inverse setting the coefficients \(S,K\) also depend on the independent second and third Wigner inputs; exploiting that randomness would require a justified joint count rather than conditioning it away and then assuming a bounded-dimensional correction.
No such joint count is asserted here.
Thus, if a future inverse-concentration step supplies a structured vector q=Q a with a supported on a bounded set J, then
\[
 S q=K S^{-1}Kq+(\det D)a.
\]
Outside J, its right side lies in the fixed range of K.
The symmetric-part floor and polynomial norm events control the magnitude of this correction by a fixed power of dimension times the norm of q.
For bounded rank K, this suggests a finite-dimensional center parameter in a structured-vector row count.
The corresponding count and its exact inverse-theorem interface have not been supplied here.
For the actual product-inverse shift, K can have rank proportional to dimension, so the bounded-rank observation does not close that original case.
Indeed, for invertible real symmetric B,C and nonzero z, the skew part of F=-z(BC)^{-1} has the same rank as CB-BC, by multiplication with the invertible factors of \((BC)^{-T}((BC)^T-BC)(BC)^{-1}\).
Take B diagonal with distinct nonzero entries and C invertible real symmetric tridiagonal with every adjacent off-diagonal entry nonzero.
Their commutator is skew tridiagonal with nonzero adjacent entries, so it has rank N for even N and N-1 for odd N, as seen by its even-dimensional principal determinants.
The resulting polynomial nonidentity gives these ranks almost surely for two independent GOE inputs, with their own almost-sure invertibility.
Thus bounded skew rank fails even within an allowed Gaussian model of the original product.
A parameter grid for a full-dimensional correction can introduce leading entropy depending on the fine precision, which the current profile argument does not absorb.
The useful next test is whether the original product-inverse structure constrains this correction more strongly than its ambient rank suggests.

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
