---
author: Yin
---

# Polynomial corank tails for real Wigner matrices with arbitrary complex shifts

This version develops the lower-rank full-matrix branch of the same cofactor problem as [C_F0194_v1](Yin_C_F0194_v1.md#statement).
The first version retains its complete cofactor and isolated-minor assertions at their [reviewed decision](Yin_C_F0194_v1.md#decision-isolated-minor-reviewed), without any expansion of that review's scope.
The new corank-tail deduction reuses its complete nonsymmetric-offset structured-vector counting module, rather than repeating the old cofactor proof.
The [independent complete corank review](../audits/reviews/Yin_R_F0200_v2.md#finding) supports this version at its exact declared scope.
No nonsingularity, positive least-singular-value floor, nonzero-shift logarithmic limit or Brown-measure conclusion is asserted.

<a id="statement"></a>
## Exact deterministic-shift assertion

Fix a real off-diagonal law \(\xi\) with \(\mathbb E\xi=0\), \(\mathbb E\xi^2=1\), and a real diagonal law \(\zeta\) with \(\mathbb E|\zeta|^2<\infty\).
For every \(n\), let \(X_n\) be raw real symmetric Wigner: its strict upper entries are independent copies of \(\xi\), its diagonal entries are independent copies of \(\zeta\), and these families are independent.
The lower entries equal the corresponding upper entries.
No moment above two, density or non-atomicity is assumed; the diagonal law may be zero and need not be centered.
For every \(\gamma,B>0\), fixed \(C,n_0>0\), depending only on the laws, \(\gamma,B\), satisfy
\[
 \sup_{\substack{F\in M_n(\mathbb C)\\\max_{i,j}|F_{ij}|\le n^\gamma}}
 \mathbb P\{\operatorname{rank}(X_n+F)\le n-2\}
 \le Cn^{-B},\qquad n\ge n_0.
 \tag{Rank-tail}
\]
The offset \(F\) is deterministic and need not be symmetric.
Rank is over \(\mathbb C\), and \(\operatorname{corank}M=n-\operatorname{rank}M\).

<a id="random-shift-statement"></a>
## Independent random shifts and coupling consequence

For a random \(F_n\) independent of \(X_n\) in this dimension, the same constants satisfy
\[
 \mathbb P\left\{\operatorname{rank}(X_n+F_n)\le n-2,
                  \ \max_{i,j}|(F_n)_{ij}|\le n^\gamma\right\}
 \le Cn^{-B}.
 \tag{Random-rank-tail}
\]
Without that guard in the event, add \(\mathbb P\{\max_{i,j}|(F_n)_{ij}|>n^\gamma\}\) to the right side.
If these guard failures are summable and \(B>1\), then \(\operatorname{corank}(X_n+F_n)\le1\) eventually almost surely under every cross-dimensional coupling with the stated within-dimension laws and independence.
The probability-one event may depend on the laws, shifts and coupling.
No independence between dimensions is required.

<a id="product-statement"></a>
## Exact three-real-Wigner product consequence

For \(j=1,2,3\), fix real off-diagonal laws \(\xi_j\) with \(\mathbb E\xi_j=0\), \(\mathbb E\xi_j^2=1\), and real diagonal laws \(\zeta_j\) with finite second moments.
Let \(W_j^{(N)}=X_j^{(N)}/\sqrt N\), where \(X_j^{(N)}\) has the preceding raw Wigner construction with the \(j\)-th fixed laws.
The three factors are independent within every dimension and may have arbitrary dependence across dimensions on one probability space.
For every fixed \(z\in\mathbb C\setminus\{0\}\) and every \(B>0\), the consequence is
\[
 \mathbb P\left\{\operatorname{corank}
    \bigl(W_1^{(N)}W_2^{(N)}W_3^{(N)}-zI_N\bigr)\ge2\right\}
 \le C_{z,B}N^{-B},\qquad N\ge N_{z,B}.
 \tag{Product-rank-tail}
\]
Consequently that product has corank at most one eventually almost surely under every allowed cross-dimensional coupling, for the fixed \(z\).
This is a lower-rank reduction for [F0012](../tasks/Yin_T_F0012_v3.md#contract), leaving corank exactly one and the well-conditioned or clustered principal-minor floor branches unresolved.

## Exact retained inputs and source scope

The [reviewed first version's truncation argument](Yin_C_F0194_v1.md#truncation) supplies uniform (AC) constants for independent cutoffs of the fixed real laws.
Its [structured class](Yin_C_F0194_v1.md#counting-class), [complete nonsymmetric-offset profile count](Yin_C_F0194_v1.md#structured-vector-counting), and [linear inverse-theorem rounding interface](Yin_C_F0194_v1.md#inverse-rounding) are reused at their exact proof scopes.
The universal-kernel consequence, measurable choices, two-form border calculation and rank chain are proved below without an isolated-minor or determinant-ratio premise.
The vector-valued linear inverse Littlewood--Offord input remains [Ngu12a, arXiv:1105.5733v1, Condition 1 and Theorem 1.3, PDF pp. 2--3](../audits/literature/Ngu12a/readme.md), with the [retained conventions](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001).
Its coefficient dimension two represents complex coefficients while the random scalar law remains real, and its original proof retains the recorded external-input inspection limits.
The [proved C_F0188_v2 floor](Yin_C_F0188_v2.md#statement) is used only at zero shift for the second and third individual Wigner factors in the product consequence.
It is not invoked for a nonsymmetric shift.
[CTV06](../audits/literature/CTV06/readme.md) supplies attribution for the recognized rank-growth mechanism, not a probability theorem with the present offset, law or coupling hypotheses.
No source-proof or independent review is inherited for the new deduction.

<a id="argument"></a>
## Complete corank argument

<a id="kernel-anticoncentration"></a>
## Universal kernel anti-concentration from the existing counting module

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
Apply the same dimension-two linear inverse theorem and [rational rounding interface](Yin_C_F0194_v1.md#inverse-rounding) used in the fixed proof, identifying complex coefficients with two-dimensional real vectors while the scalar randomness stays real.
Its structural rank, progression size and exceptional-count constants depend on \(b\), the chosen fixed exception exponent, and the uniform (AC) constants, rather than on the eventual fine precision \(a\).
It gives a vector \(w\) of norm between \(1/2\) and two, with \(\|w-u\|_\infty\le C m^{-a}\), in the rational progression class of [C_F0194_v1](Yin_C_F0194_v1.md#counting-class).
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

<a id="border-rank"></a>
## Bordered rank and its measurable kernel choices

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

<a id="rank-chain"></a>
## One leading-principal chain gives the full rank tail

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
## Conditional shifts and the original three-factor object

For an independent random \(F_n\), condition on its realization in this dimension only.
On its polynomial entry-bound event, the deterministic-shift estimate is uniform over that realization.
Integrating proves (Random-rank-tail), and adding the guard failure gives its unconditional formulation.
For \(B>1\) and summable guard failures, first Borel--Cantelli gives eventual corank at most one under every cross-dimensional coupling.
The proof does not condition on a complete cross-dimensional shift sequence.

For each of the second and third normalized real Wigner factors, the [accepted zero-shift case of C_F0188_v2](Yin_C_F0188_v2.md#statement) gives, for every desired \(b_1>0\), a fixed \(A>0\) such that
\[
 \mathbb P\{s_{\min}(W_2^{(N)})\le N^{-A}
              \text{ or }s_{\min}(W_3^{(N)})\le N^{-A}\}
 \le CN^{-b_1}.
 \tag{Factor-guard}
\]
Enlarging \(A\) accommodates both fixed laws.
On the complementary event both factors are invertible and
\[
 \|(W_2^{(N)}W_3^{(N)})^{-1}\|
 \le\|(W_3^{(N)})^{-1}\|\,\|(W_2^{(N)})^{-1}\|
 \le N^{2A}.
\]
For the fixed nonzero \(z\), put
\[
 M_N=W_1^{(N)}-z(W_2^{(N)}W_3^{(N)})^{-1}.
\]
Define the shift to be zero when either of the last two factors is singular, solely to make it measurable at every dimension.
This agrees with the intended expression on (Factor-guard)'s good event and is independent of \(W_1^{(N)}\) within the dimension.
Multiplying \(M_N\) by \(\sqrt N\) makes its Wigner part raw and bounds the conditional shift's operator norm by \(|z|N^{2A+1/2}\) on that event.
For all sufficiently large \(N\), every shift entry is therefore at most \(N^{2A+2}\).
Apply (Random-rank-tail) with this fixed exponent and add (Factor-guard)'s failure probability.
Taking both requested failure exponents larger than \(B\) gives the desired bound.
Indeed the exact identity
\[
 W_1^{(N)}W_2^{(N)}W_3^{(N)}-zI_N
 =M_N W_2^{(N)}W_3^{(N)}
\]
shows that right multiplication by the last two invertible factors preserves rank.
This proves (Product-rank-tail).
For \(B>1\), first Borel--Cantelli gives its eventual corank-at-most-one consequence under every allowed cross-dimensional coupling.
No estimate excluding corank one or controlling positive small singular values has been supplied.

<a id="rank-growth-attribution"></a>
## Actual known mechanism and this adaptation's boundary

The rank-growth mechanism is already present in Costello--Tao--Vu, *Random symmetric matrices are almost surely non-singular*, arXiv:math/0505156v1, Section 2, equation (1), Lemma 2.4 on PDF p. 3, and its proof on pp. 11--12.
The selected original is retained as [CTV06--arxiv-v1.pdf](../literature/pdf/CTV06--arxiv-v1.pdf), with its [edition and source note](../audits/literature/CTV06/readme.md).
Their singular-border argument concerns symmetric matrices and Bernoulli borders, and its proof explicitly uses symmetry to infer a rank increase of two from a rank-increasing column.
The nonsymmetric deterministic-offset argument here separately controls both a right-kernel and a transpose-left-kernel linear form by the reviewed C_F0194 counting module.
The source's full nonsingularity proof also needs the separate invertible-border quadratic step, which is not imported here.
The source's phrase almost surely means probability tending to one in that paper, whereas the arbitrary-cross-size almost-sure consequence above uses its own summable bounds and first Borel--Cantelli.
Only this mechanism attribution and the stated passages were checked; no novelty claim or whole-paper proof audit is made.


## Current assessment
[Selected decision](#decision-corank-tail-reviewed)

## Assessment history

### Decision corank-tail-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T10:10 |
| status | open |
| reason | A complete candidate corank-tail argument is fixed for fresh review, including universal kernel anti-concentration, measurable choices, shared-border rank growth, one uniformly truncated principal chain, conditional shifts and the original three-factor consequence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact corank-tail assertions](#statement) | Raw real finite-second-moment Wigner laws, arbitrary polynomially bounded nonsymmetric complex shifts, independent random-shift guards, and fixed-nonzero-shift three-factor product consequence under every stated coupling. |
| argument | [Complete rank argument](#argument) | Universal kernel anti-concentration, measurable selection, same-border union bound, rank increase two, common truncated-law principal chain, parameter order and product normalization. |
| dependency | [Reviewed nonsymmetric counting modules](Yin_C_F0194_v1.md#structured-vector-counting) | The structured class, full profile count, truncation uniformity and linear rounding interfaces linked in the input section; not the isolated-minor probability assertion. |
| dependency | [Accepted linear inverse theorem conventions](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) | Only arXiv:1105.5733v1 Condition 1 and Theorem 1.3 at the exact scope recorded in the source notes linked by this unit: dimension-two coefficients, real scalar law and rational progressions; original proof not newly audited. |
| dependency | [One-factor real Wigner floors](Yin_C_F0188_v2.md#statement) | Only zero-shift normalized floors for the second and third factors, giving the product shift guard; no nonsymmetric-shift use. |

### Decision corank-tail-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T10:18 |
| status | proved |
| reason | Independent review checked the complete corank-tail deduction, all declared inputs, universal kernel and measurability interfaces, shared-border rank growth, uniform truncated-law chain and the original three-factor consequence without an unresolved mathematical gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact corank-tail assertions](#statement) | Raw real finite-second-moment Wigner laws, arbitrary polynomially bounded nonsymmetric complex shifts, independent random-shift guards, and fixed-nonzero-shift three-factor product consequence under every stated coupling. |
| argument | [Complete rank argument](#argument) | Universal kernel anti-concentration, measurable selection, same-border union bound, rank increase two, common truncated-law principal chain, parameter order and product normalization. |
| dependency | [Reviewed nonsymmetric counting modules](Yin_C_F0194_v1.md#structured-vector-counting) | The structured class, full profile count, truncation uniformity and linear rounding interfaces linked in the input section; not the isolated-minor probability assertion. |
| dependency | [Accepted linear inverse theorem conventions](../audits/literature/Ngu12a/Yin_U001.md#ngu12a-u001) | Only arXiv:1105.5733v1 Condition 1 and Theorem 1.3 at the exact scope recorded in the source notes linked by this unit: dimension-two coefficients, real scalar law and rational progressions; original proof not newly audited. |
| dependency | [One-factor real Wigner floors](Yin_C_F0188_v2.md#statement) | Only zero-shift normalized floors for the second and third factors, giving the product shift guard; no nonsymmetric-shift use. |
| review | [Independent complete corank finding](../audits/reviews/Yin_R_F0200_v2.md#finding) | Entire deterministic and independent-random-shift theorem, all direct dependencies, coupling consequences and the fixed-nonzero-shift three-factor reduction. |
