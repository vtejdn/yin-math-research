---
author: Yin
---

# Almost-sure determinant limits for matrix-coefficient Haar unitary pencils

## Contract

### Input model and ordinary determinant

Fix integers \(r,m\ge1\) and arbitrary matrices \(A_0,A_1,\ldots,A_r\in M_m(\mathbb C)\), independently of \(N\).
For each \(N\ge1\), let \(U_1^{(N)},\ldots,U_r^{(N)}\) be independent matrices with Haar probability law on the full complex unitary group \(U(N)\).
All dimensions are realized on one probability space.
Let \(u_1,\ldots,u_r\) be free Haar unitaries in a finite von Neumann algebra with faithful normal tracial state \(\tau\), and set
\[
 L_N=A_0\otimes I_N+\sum_{j=1}^r A_j\otimes U_j^{(N)},\qquad
 L=A_0\otimes1+\sum_{j=1}^r A_j\otimes u_j,\qquad
 \tau_m=\operatorname{tr}_m\otimes\tau.
\]
Here \(\operatorname{tr}_m=m^{-1}\operatorname{Tr}\).
The coefficients need not be selfadjoint, and \(A_0\) may be singular or zero.

Use the [ordinary Fuglede--Kadison determinant](../audits/literature/MS24/Yin_U001.md#determinant-convention), including zero spectral mass, and put
\[
 \ell_N=\frac1{mN}\log|\det L_N|,\qquad
 \ell=\log\Delta_{\tau_m}(L)
     =\int_{[0,\infty)}\log t\,d\mu_{|L|}^{\tau_m}(t).
\]
The measure in the integral is the spectral distribution of \(|L|\) under \(\tau_m\).
Use \(\log0=-\infty\) and \(\exp(-\infty)=0\); singular finite pencils remain in scope.
The ordinary finite determinant root is \(\Delta_{mN}(L_N)=|\det L_N|^{1/(mN)}\).

### Almost-sure limit, upper limit and coupling quantifiers

Determine the truth of both assertions
\[
 \ell_N\longrightarrow\ell\quad\text{almost surely},
 \tag{H-limit}
\]
and
\[
 \limsup_{N\to\infty}\ell_N=\ell\quad\text{almost surely}.
 \tag{H-limsup}
\]
Equivalently, these assert convergence, respectively equality of the upper limit, of \(\Delta_{mN}(L_N)\) to \(\Delta_{\tau_m}(L)\).
The limits run through every positive integer \(N\), with no selected dimensional subsequence.

Determine each assertion under each of the following two explicit requirements.

| Coupling requirement | Quantifier |
| --- | --- |
| Arbitrary coupling across dimensions | For every fixed \(r,m,A_0,\ldots,A_r\) and every joint law of the sequence of tuples whose \(N\)-th marginal is the product of \(r\) Haar laws on \(U(N)\), the asserted equality has probability one. |
| Independence across dimensions | For every fixed coefficient tuple, the asserted equality has probability one when the entire tuples at distinct dimensions are independent, in addition to independence within each dimension. |

The probability-one event may depend on the fixed tuple and the chosen joint law.
No event simultaneous for all uncountably many coefficient tuples is required.
A proof for arbitrary couplings covers the independent model; a proof for the independent model alone does not cover arbitrary couplings.
A full-limit proof also resolves the corresponding upper-limit question, but a counterexample to the full limit does not by itself refute the upper-limit equality.
No preferred coupling, such as a nested construction, is implicit.

### Scope and completion criteria

Resolve these two assertions in the two coupling regimes by complete proofs or rigorous counterexamples, with applicable review against this exact contract.
One argument may settle several assertions through the stated logical implications; separate proof documents are not required.
A negative resolution identifies fixed coefficient matrices, a joint law satisfying the relevant requirements, and failure with positive probability.
If an arbitrary-coupling assertion is false, the corresponding independent-coupling assertion remains an explicit obligation unless the same example already satisfies independence across dimensions.
An upper bound alone, convergence in probability alone, or a result only for monic, scalar, single-variable or strictly stable coefficients is partial progress.
A probability limit may nevertheless resolve the upper-limit assertion when supplemented by the applicable almost-sure upper bound, as explained in the [literature comparison](../ledger/Yin_L_F0062_v1.md#wigner-status).

This contract concerns affine pencils in \(u_1,\ldots,u_r\), without additional adjoint terms.
Adjoint pencils or higher-degree matrix polynomials may be investigated separately, retaining the dependence of \(u_j^*\) on \(u_j\), but are not completion requirements here.
Expectation convergence, uniformity over coefficient sets and Brown-measure convergence are not required.

## Starting evidence and separate objectives

The [Haar literature comparison](../ledger/Yin_L_F0062_v1.md#haar-pencils) retains the upper-semicontinuity direction, the zero-FK-determinant and bounded-inverse cases under the stated convergence inputs, and the exact domains of newer determinant-moment formulas.
The [single-Haar reduction](../ledger/Yin_L_F0062_v1.md#single-haar) provides the classical one-variable case.
Those findings retain their actual source and review scope; positive determinant moments alone supply no negative-logarithm uniform integrability.
The main general gap identified by that survey is positive free determinant without a bounded inverse.

The [reviewed Haar structural theorem](../claims/Yin_C_F0192_v1.md#decision-haar-structural-reviewed) now proves full limits for at most two effective coefficient positions, sparse support components with at most one cycle, and the stated simultaneous triangular extensions.
It includes an irreducible four-entry example with positive determinant and an unbounded free inverse.
For the unrestricted coefficient tuple it proves eventual almost-sure invertibility whenever the free kernel is zero, without controlling the small positive singular values.
The [reviewed coupling criteria](../claims/Yin_C_F0190_v1.md#decision-coupling-criteria-reviewed) show that full almost-sure convergence under independent dimensions would already imply it under arbitrary coupling, while their upper-limit criteria remain different.
Those structural arguments alone leave the general positive-determinant logarithmic-tail obligation unresolved.

The [reviewed conditional Haar-additive and Schur theorem](../claims/Yin_C_F0193_v1.md#decision-conditional-schur-reviewed) proves full logarithmic limits for its strict-bulk rank-one coefficient class with the displayed bounded background and compression inverses.
Its direct scalar corollary includes \(1+U+V\) and every three-term scalar tuple in the stated strict squared-triangle region.
These classes have positive free determinant and an unbounded free inverse; their proofs do not cover arbitrary higher-rank coefficients or the excluded bulk regimes.
The [reviewed complementary-corner extension](../claims/Yin_C_F0193_v2.md#decision-complementary-corner-reviewed) removes the full-background inverse assumption in its exact rank-one class.

This random-matrix approximation objective is distinct from the [single-Haar variational and coefficient-analysis Task](Yin_T_F0010_v1.md#contract) and the [Wigner-pencil Task](Yin_T_F0013_v1.md#contract).
Their completion decisions do not complete this Task.
The [permutation Laurent-polynomial Task](Yin_T_F0016_v1.md#contract) instead uses uniform permutation inputs and a kernel-removed finite determinant.

## Resolution and independent full-chain follow-up

The [proved complete affine Haar theorem](../claims/Yin_C_F0192_v2.md#decision-full-haar-reviewed) resolves all four original assertions affirmatively.
It proves the full almost-sure ordinary logarithmic determinant limit for every fixed matrix coefficient tuple under every allowed cross-dimensional coupling, including singular constant terms and a zero free determinant.
The [independent whole-contract finding](../audits/reviews/Yin_R_F0197_v2.md#independent-full-haar-proof) checked its complete proof, exact inputs and comparison with this unchanged contract.
The [independent post-completion audit](../audits/reviews/Yin_R_F0197_v2.md#post-completion-full-haar-chain) checked the actual selected contract, proved support and complete necessary input chain and found no remaining mathematical obligation.

## Current decision
[Selected decision](#decision-completed-full-haar-limit)

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-11-05T05:07 |
| status | active |
| authority | Yin explicitly requested a separate Task for matrix-coefficient linear pencils evaluated at independent Haar unitary matrices, with explicit almost-sure, upper-limit and cross-dimensional coupling requirements. |
| reason | The Haar approximation problem has its own input law and singular-value obstruction; its full limit and upper-limit assertions must retain separate coupling quantifiers. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Haar-pencil determinant contract](#contract) | Ordinary normalized logarithmic determinant limit and upper-limit assertions for all fixed affine matrix coefficients, separately under arbitrary coupling and independence across dimensions. |

### Decision completed-full-haar-limit

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:34 |
| status | completed |
| authority | Yin authorized parallel exploration and advancement of F0012 through F0016 within their unchanged contracts and completion criteria. |
| reason | The independently reviewed full affine Haar theorem proves the ordinary logarithmic determinant limit for all fixed coefficients and every allowed coupling, including singular constant terms and zero free determinant; this resolves both assertions under both original coupling requirements. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Original complete Haar contract](#contract) | Full limit and upper-limit equality under arbitrary coupling and independent dimensions, through every dimension, with all coefficient and ordinary-determinant conventions unchanged. |
| support | [Complete affine Haar theorem](../claims/Yin_C_F0192_v2.md#statement) | Full extended-real ordinary normalized logarithmic limit for all fixed matrix coefficients and arbitrary cross-dimensional coupling, hence all four original assertions. |
| review | [Independent whole-contract finding](../audits/reviews/Yin_R_F0197_v2.md#independent-full-haar-proof) | Original contract, complete selected theorem and its full proof and direct-input interfaces, with all coupling, coefficient and zero-target cases. |
