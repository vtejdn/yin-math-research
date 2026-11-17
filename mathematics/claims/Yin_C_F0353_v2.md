---
author: Yin
---

# Elimination of independent scalar Wigner inputs above a two-dimensional coefficient space

<a id="statement"></a>
## Affine determinants without translation regularity

Fix independent real symmetric Wigner matrices \(W_1^{(N)},\ldots,W_g^{(N)}\) as in [F0013](../tasks/Yin_T_F0013_v1.md#input-model).
Each raw strict upper law is real, centered and has variance one, and each raw diagonal law is real, centered and has finite second moment.
The coordinates are independent above and on the diagonal within a size, have their fixed respective laws, and are divided by \(\sqrt N\).
The complete vectors of inputs at different sizes may be coupled arbitrarily.

Fix \(m\ge1\) and complex \(m\)-square coefficients \(b,A_1,\ldots,A_g\).
Assume there is a subset of colors \(J\) such that
\[
 \operatorname{rank} A_j\le1\ \ (j\in J),\qquad
 \dim_{\mathbb C}\operatorname{span}\bigl(\{b\}\cup\{A_j:j\notin J\}\bigr)\le2 .
 \tag{1}
\]
Let \(L=b+\sum A_jx_j\), \(L_N=L(W^{(N)})\) and \(u=\log\Delta_{\operatorname{tr}_m\otimes\tau}L(s)\) for a free standard semicircular tuple.
If \(L\) is full over the free polynomial algebra, \(u\) is finite and there are \(H,C,N_0>0\) with
\[
 \Pr\{s_{\min}(L_N)\le N^{-H}\}\le C\sqrt{\log(2+N)}\,N^{-1/18}
 \qquad(N\ge N_0).
 \tag{2}
\]
Thus \(U_N=(mN)^{-1}\log|\det L_N|\) converges to \(u\) in probability through all sizes.
Under every allowed coupling \(U_{2^k}\to u\) almost surely, and \(\limsup_N U_N=u\) almost surely.
Along this same deterministic sequence of even sizes the loss of negative logarithms below \(N^{-H}\) is eventually zero almost surely.
If \(L\) is nonfull the finite and free ordinary logarithms are all \(-\infty\).
The sequence of sizes is common to all fixed data; the probability-one event is allowed to depend on the chosen pencil and coupling.

The class contains all homogeneous two-variable matrix pencils, regardless of coefficient size, and the earlier [class with at most one coefficient of rank greater than one](Yin_C_F0353_v1.md#statement).
Assumption (1) also permits arbitrary further independent Wigner directions of rank at most one.
All raw inputs may be Rademacher, with no translation modulus imposed.

<a id="argument"></a>
<a id="terminal-base"></a>
## Scalar shifts in a pencil with two coefficient directions

Use the [original real Wigner polynomial floor](Yin_C_F0194_v5.md#in-probability-floor) for a scalar Wigner matrix \(W\) plus any deterministic complex matrix shift.
The [normalized statement](Yin_C_F0186_v10.md#floor-input) permits an independent shift: on its measurable entry-norm guard \(\max |F_{kl}|\le N^a\) the conditional probability of \(s_{\min}(W+F)\le N^{-h(a)}\) is at most \(C N^{-2}+C\sqrt{\log(2+N)}N^{-1/18}\).
Here the secondary inverse-polynomial failure power is taken to be two.
Also \(\|W_j\|\le N^2\) for every color outside probability \(O(N^{-3})\), by Frobenius Markov and finite second moments.

First suppose \(J\) is empty, and choose \(B,C\) spanning the coefficients, allowing zero matrices in a smaller span.
There are fixed invertible left and right changes of basis under which both \(B,C\) are upper triangular.
For a direct proof, if \(C\) is singular take a nonzero vector \(h\) in its kernel; otherwise take an eigenvector of \(C^{-1}B\).
The images \(Bh,Ch\) lie in a single line, with an arbitrary line allowed if they both vanish.
Choose domain and range orthonormal bases whose first vectors span these lines in the domain and range, respectively.
The first columns then vanish below the first row.
Apply the same construction to the two remaining square lower-right blocks and continue by dimension.
The resulting two-sided changes preserve singular values when chosen unitary.
Consequently \(L\) becomes upper triangular with diagonal scalar affine polynomials \(\ell_i=b_i+\sum_j a_{ij}x_j\).
All diagonal entries are nonzero as polynomials when \(L\) is full: over the free field a triangular matrix is invertible precisely when its diagonal entries are nonzero.

For a nonconstant \(\ell_i\), choose any \(j\) with \(a_{ij}\ne0\).
Conditioning on its other colors expresses \(\ell_i(W)\) as \(a_{ij}(W_j+F_i)\), with independent shift of polynomial norm on the norm guards of those other colors.
A nonzero constant diagonal has a deterministic inverse.
Take the union of the finitely many scalar floor failures; the estimates for different diagonals need no mutual independence.
Then all diagonal inverses have polynomial norm, and the off-diagonal blocks have polynomial norm on the original guards.
Writing the triangular matrix as \(D(I+T)\), its block diagonal \(D\) has polynomially bounded inverse and \(T\) is strictly upper triangular with polynomially bounded blocks.
The finite sum \(\sum_{k=0}^{m-1}(-T)^k\) bounds the inverse polynomially at the error in (2).

<a id="rank-one-step"></a>
## Eliminating a rank-one color

Induct on the number of nonzero coefficients with labels in \(J\).
Fixed invertible left and right changes put one such coefficient in position \(e_1e_1^{\mathsf T}\), preserving (1) in the transformed system.
Write the transformed pencil as
\[
 L=\begin{pmatrix}x_j+d&r\\ c&E\end{pmatrix},\qquad
 L_0=\begin{pmatrix}d&r\\ c&E\end{pmatrix}.
\]
The other blocks omit \(x_j\).
When \(m=1\), use the direct scalar shift estimate.
If \(m>1\) and \(E\) is full, its coefficients are common restrictions of the respective transformed coefficients of \(L\).
Rank at most one and the upper bound two on the dimension of the remaining coefficient space persist under these linear restrictions, with the same partition after omitting \(j\).
The induction hypothesis bounds \(E_N^{-1}\) polynomially.
On this event and the norm guards of the other colors the Schur shift \(d_N-r_N E_N^{-1}c_N\) has polynomial norm and depends only on these other colors.
The shifted-Wigner floor and the two triangular Schur factors then bound the complete inverse polynomially, exactly as in the [full-complement step](Yin_C_F0353_v1.md#argument).

If \(E\) is nonfull the argument must also account for its dimension loss.
Work first over the free field on the active colors, using [invertibility there for full polynomial matrices](../audits/literature/MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments).
The polynomial factorization of \(E\) through at most \(m-2\) columns gives a nonzero right kernel vector \(y\).
Injectivity of \(L\) gives \(ry\ne0\) since \(L\binom{0}{y}=\binom{ry}{0}\).
Thus \(e_1^{\mathsf T}L^{-1}e_1=0\), by multiplying the last preimage on the right by \((ry)^{-1}\).
It follows that \(L^{-1}e_1 x_j e_1^{\mathsf T}\) squares to zero and \(L_0=L(I-L^{-1}e_1x_j e_1^{\mathsf T})\) is invertible over this field.
In particular \(L_0\) is full over the polynomial algebra on the remaining colors, since a smaller factorization there would also hold in the larger field.
Deletion of \(x_j\) preserves (1), so induction bounds \(L_{0,N}^{-1}\) on the original other colors.

At finite size the polynomial factorization gives \(\dim\ker E_N\ge N\).
On the event of invertibility of \(L_{0,N}\), the map \(r_N:\ker E_N\to\mathbb C^N\) is injective and hence onto.
Therefore \(L_{0,N}^{-1}\) has zero first diagonal block by the same preimage argument, now for every vector in \(\mathbb C^N\).
For \(D_N=e_1e_1^{\mathsf T}\otimes W_j\), the entire matrix \(L_{0,N}^{-1}D_N\) is square-zero.
Hence \(L_N^{-1}=(I-L_{0,N}^{-1}D_N)L_{0,N}^{-1}\) obeys a polynomial bound on the same events and the norm guard.
This [finite singular-complement argument](Yin_C_F0353_v1.md#singular-complement) uses only the evaluated polynomial blocks and the invertible \(L_{0,N}\).
Only finitely many floor and norm errors enter the induction.
Increasing the polynomial exponent slightly absorbs all fixed constants and gives (2) with a closed lower threshold.

<a id="logs"></a>
## Removing the last logarithms

For full \(L\) the [free power estimate at zero background](Yin_C_F0352_v1.md#statement) implies \(u>-\infty\).
The [finite-second-moment polynomial-window count](Yin_C_F0186_v40.md#argument), bounded-rank row concentration and positive-log control give almost-sure convergence to \(u\) for \(U_N\) clipped below at singular value \(N^{-H}\), as in [the cutoff comparison before its invocation of (T)](Yin_C_F0186_v40.md#determinant).
Off (2)'s bad event this clipped logarithm equals \(U_N\).
This gives convergence in probability through all dimensions.
The marginal error in (2) is summable for \(N=2^k\), so the two logs agree eventually there almost surely by the first Borel--Cantelli lemma under every coupling.
Since \(U_N\) is bounded above by the clipped statistic at every size, the almost-sure full-sequence upper limit equals \(u\).
For a nonfull pencil, a free polynomial factorization through fewer than \(m\) columns gives a positive trace kernel at the free evaluation and a kernel of dimension at least \(N\) at every finite evaluation.

<a id="scalar"></a>
## Two scalar polynomial classes

For arbitrary disjoint groups of colors \(x=(x_1,\ldots,x_r)^{\mathsf T}\), \(y=(y_1,\ldots,y_s)^{\mathsf T}\), and any fixed complex coefficients, consider
\[
 P=d+\sum_i a_i x_i+\sum_j b_j y_j+\sum_{ij} q_{ij} x_i y_j .
\]
For each prescribed shift \(z\), the [bipartite realization and its proof](Yin_C_F0353_v1.md#scalar) have top left entry \(d-z+\sum_i a_i x_i+\sum_j b_j y_j\), top right \(-x^{\mathsf T}\), bottom left \(Q y\) and bottom right \(I_r\), where \(Q=(q_{ij})\).
All \(x_i\) coefficients occupy only the first row, and all \(y_j\) coefficients only the first column.
The Schur complement is exactly \(P-z\), and the inverse upper-left corner on nonsingular evaluations is \((P-z)^{-1}\).
Thus (2) supplies a polynomial floor for this scalar polynomial and its ordinary logarithms have the same limits, with the finite and free normalized logarithms of the pencil both multiplied by \(r+1\).

The [acyclic formula realization](Yin_C_F0353_v1.md#scalar) also supplies the conclusions of [F0014](../tasks/Yin_T_F0014_v1.md#contract) for any fixed formula built from scalars, addition and ordered multiplication in which all but at most one color occur at most once.
Its unit upper triangular auxiliary block \(I-T\) represents the directed graph path sum by the finite series \(I+T+\cdots+T^{n-1}\).
Each variable leaf is one edge, so all but one coefficient have rank at most one and the exceptional coefficient together with the constant spans at most two dimensions.
In both constructions a nonconstant \(P-z\) is nonzero as a free polynomial, and the same unit triangular Schur reductions make the auxiliary pencil full.
The [unit triangular determinant identities](../ledger/Yin_L_F0061_v2.md#linearization-transfer) give the same auxiliary-size multiplier in the finite and free traces, including \(z=P(0)\).
The scalar log therefore converges in probability through all sizes and almost surely along \(2^k\), and has the claimed full-sequence limsup under each coupling.
Constant polynomials are immediate with the ordinary \(\log0=-\infty\) convention.

## Current assessment
[Selected decision](#decision-two-direction-elimination-reviewed)

## Assessment history

### Decision two-direction-elimination-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:55 |
| status | open |
| reason | The triangular two-direction base and the two rank-one elimination branches give a polynomial inverse bound at the original discrete or continuous laws. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Rank and span condition](#statement) | Polynomial least-value floor and ordinary determinant limits for independent real finite-variance Wigner colors. |
| argument | [Two-direction terminal pencil](#argument) | Joint two-sided triangularization and scalar conditional shifts. |
| support | [Independent rank-one directions](#rank-one-step) | Full and nonfull complements, stable restrictions and actual finite evaluations. |
| support | [Determinant limits](#logs) | Explicit dyadic sizes, all-size convergence in probability and arbitrary cross-size coupling. |
| support | [Scalar applications](#scalar) | Bipartite quadratics and formulas with one possibly repeated variable, at every fixed shift. |

### Decision two-direction-elimination-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:03 |
| status | proved |
| reason | The scalar shift floor, triangular base and rank-one induction prove the least singular value bound and the resulting logarithmic limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Elimination with a residual pencil of dimension at most two](#statement) | The fixed statement with the specified laws, dimensions and coupling quantifiers. |
| argument | [Complete argument](#argument) | The scalar shift floor, triangular base and rank-one induction prove the least singular value bound and the resulting logarithmic limits. |
| support | [Complementary rank](#rank-one-step) | Both complementary blocks and evaluation without a singular rational substitution. |
| support | [Ordinary logarithms](#logs) | Dyadic almost-sure convergence and the all-dimension upper limit. |
| support | [Scalar applications](#scalar) | Bipartite quadratic and variable-occurrence hypotheses. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0361_v1.md#two-direction-elimination-whole-proof) | Hypotheses, conclusions, proof and directly used mathematical interfaces. |
