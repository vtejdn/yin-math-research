---
author: Yin
---

# Recognizable holomorphic L2 series for free identically distributed bounded R-diagonals

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Recognizable Holomorphic Series in Free R-Diagonal Variables

<a id="statement"></a>

<a id="yin_c_f0017"></a>
## Yin_C_F0017: L2 Summability Gives Bounded Scalar Rational Evaluation

Date: 2026-09-09.
Provenance: project deduction by another AI agent.
This is a sufficient theorem for the authorized [Yin_T_F0001 follow-up](../tasks/Yin_T_F0001_v1.md#authorized-regularity-follow-up), pursued in [Yin_S_F0009](../strategies/Yin_S_F0009.md#s_f0009).
Initial assessment: complete proof draft pending independent review.
The [selected assessment](#decision-isolated-review-20261022) records the current mathematical assessment and adopted review.
No novelty claim is made.

### 1. Exact statement

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal tracial state.
Let $a_1,\ldots,a_d\in M$, $1\le d<\infty$, be freely independent, identically distributed, nonzero R-diagonal elements.
Set $\sigma=\|a_1\|_2>0$, $b_i=a_i/\sigma$, and $b_w=b_{i_1}\cdots b_{i_m}$ for a word $w=i_1\cdots i_m$, with $b_\varepsilon=1$.
Write
\[
H_{\mathrm{hol}}=\overline{\mathbb C\langle a_1,\ldots,a_d\rangle}^{\,L^2(M)},\qquad
\mathcal A_{\mathrm{hol}}=\overline{\mathbb C\langle a_1,\ldots,a_d\rangle}^{\,\|\cdot\|_M},
\]
where neither generated algebra is required to contain the adjoints.

Suppose a scalar sequence $(\alpha_w)_{w\in\{1,\ldots,d\}^*}$ satisfies
\[
\sum_w|\alpha_w|^2<\infty,\qquad
\dim\operatorname{span}_{\mathbb C}\{w\mapsto\alpha_{wv}:v\in\{1,\ldots,d\}^*\}<\infty.
\tag{1}
\]
Then the L2 series $f=\sum_w\alpha_w b_w$ converges absolutely by homogeneous blocks in operator norm, and
\[
f\in\mathcal A_{\mathrm{hol}}\cap
\operatorname{Div}_M\mathbb C\langle a_1,\ldots,a_d\rangle.
\tag{2}
\]
Here division closure means the smallest unital subalgebra of $M$ containing the indicated polynomials and closed under scalar inverses that exist in $M$.

Equivalently, given unnormalized coefficients $c_w$, assume recognizability of $c$ and the actual weighted Taylor summability
\[
\sum_w |c_w|^2\sigma^{2|w|}<\infty.
\tag{3}
\]
Then $f=\sum_wc_wa_w$ has the conclusion (2).
Letter rescaling changes a realization $c_w=\lambda A_w\gamma$ into $\alpha_w=\sigma^{|w|}c_w=\lambda(\sigma A)_w\gamma$, and conversely.
Thus it preserves finite residual dimension.

No normality or bounded dual system is required for this theorem.
It concerns the displayed holomorphic coefficient expansion.
It does not assert that every affiliated rational element which happens to be in $L^2(M)$ has that expansion.

### 2. Orthogonality and the accepted homogeneous estimate

The normalized monomials $b_w\Omega$ form an orthonormal basis of $H_{\mathrm{hol}}$.
Here is the moment check.
In
\[
\tau(a_v^*a_w)
\]
all starred letters precede all unstarred letters.
Freeness makes a mixed free cumulant zero unless all letters in its block have the same generator index.
R-diagonality makes a remaining cumulant zero unless the adjoint pattern alternates and its length is even.
In this ordered product an alternating block can therefore have only two entries, one of each adjoint type.
A noncrossing pairing of a block of starred letters with a block of unstarred letters exists only when their lengths agree, and is then the unique nested pairing.
The paired generator indices must agree.
Consequently
\[
\tau(a_v^*a_w)=\delta_{v,w}\sigma^{2|w|}.
\tag{4}
\]
The same argument includes a zero-length word: a nonempty entirely holomorphic word has trace zero.
Completeness in $H_{\mathrm{hol}}$ is its definition.

This is also the calculation in KS07, Section 4.1, printed p. 17, equations (4.1)-(4.3).
It does not assert completeness in all of $L^2(M)$.

The external theorem used here is KS07, Definition 1.2 and Theorem 1.3, printed pp. 2-3, for exactly the free identically distributed bounded R-diagonal family above.
There is a finite constant $C_b$ depending on its common distribution such that, for $m\ge1$,
\[
\left\|\sum_{|w|=m}\beta_w b_w\right\|_M
\le C_b\sqrt m
\left(\sum_{|w|=m}|\beta_w|^2\right)^{1/2}.
\tag{5}
\]
For $m=0$, use constant 1.
The source statement and the word-norm calculation have been inspected; the complete proof of the strong Haagerup inequality is an accepted external input, not independently audited here.
Source identity and reading scope are recorded in the [route evidence](../ledger/Yin_L_F0008_v1.md#ks07-selected-input).

### 3. Scalar norm convergence

The finite-residual equivalences and energy argument of [Yin_C_F0015, Sections 2-3](Yin_C_F0015_v1.md#yin_c_f0015) apply to the scalar sequence $\alpha$: there are $C<\infty$ and $0<\rho<1$ with
\[
e_m=\sum_{|w|=m}|\alpha_w|^2\le C\rho^{2m}.
\tag{6}
\]
This part of Yin_C_F0015 is a statement about sequences on the free monoid and does not depend on the ambient Hilbert space being exhausted by the word vectors.
In particular the use here is an explicitly justified closed-subspace version of its final norm argument, not a literal invocation of its full-basis hypothesis.

For completeness, a realization $\alpha_w=\lambda A_w\gamma$ makes
\[
e_m=(\lambda\otimes\overline\lambda)
\left(\sum_iA_i\otimes\overline{A_i}\right)^m
(\gamma\otimes\overline\gamma).
\]
Hence the energy generating function is rational.
Its nonnegative coefficients are summable by (1), so it is bounded on the closed unit disk and its reduced rational function has no pole there.
Cauchy estimates on a slightly larger disk give (6).
When the generating function is a polynomial, choose any $\rho\in(0,1)$ and enlarge $C$ over its finite support.
The zero series is immediate.
This argument makes no stability assertion about unused states in an arbitrary realization.

Combining (5) and (6) gives
\[
\sum_{m\ge0}\left\|\sum_{|w|=m}\alpha_wb_w\right\|_M
\le |\alpha_\varepsilon|+
C_b\sqrt C\sum_{m\ge1}\sqrt m\,\rho^m<\infty.
\tag{7}
\]
By (4) the same degree cutoffs converge in L2 to the specified $f$.
Operator norm convergence implies L2 convergence, so the bounded sum represents exactly $f$.
This proves $f\in\mathcal A_{\mathrm{hol}}$.

### 4. Minimality controls every matrix entry

For a nonzero $\alpha$, choose a minimal finite scalar realization
\[
\alpha_w=\lambda A_w\gamma,\qquad
A_w=A_{i_1}\cdots A_{i_m},\qquad A_\varepsilon=I_n.
\tag{8}
\]
The residual construction in Yin_C_F0015 gives such a reachable and observable realization.
Reachability means that $A_v\gamma$ span $\mathbb C^n$; observability means that the rows $\lambda A_u$ span its dual.
Choose finitely many words so that these columns and rows span, and express the coordinate row $e_i^{\mathsf T}$ and coordinate column $e_j$ as linear combinations of them.
Multiplying these two finite expansions gives constants $d^{uv}_{ij}$ with
\[
(A_w)_{ij}=\sum_{u,v}d^{uv}_{ij}\alpha_{uwv}.
\tag{9}
\]
For every fixed pair $u,v$, concatenation $w\mapsto uwv$ is injective.
It follows that each sequence
\[
\beta^{ij}_w=(A_w)_{ij}
\]
is in $\ell^2$ by (1) and (9).
Each is also recognizable by (8), using the coordinate row and column in place of $\lambda,\gamma$.
The degree energy argument of Section 3 therefore applies separately to every $\beta^{ij}$.
Formula (5) yields
\[
\sum_{m\ge0}
\left\|\sum_{|w|=m}(A_w)_{ij}b_w\right\|_M<\infty
\quad(1\le i,j\le n).
\tag{10}
\]
This step uses minimality.
Adding an unobservable growing state would invalidate it.

### 5. Bounded matrix evaluation and scalar elimination

Put
\[
T=\sum_{k=1}^d A_k\otimes b_k\in M_n(M).
\]
The monomials are multiplicative, so for every $m\ge0$,
\[
(T^m)_{ij}=\sum_{|w|=m}(A_w)_{ij}b_w.
\tag{11}
\]
There are finitely many entries, and a matrix norm is bounded by the sum of their norms.
Equation (10) therefore gives
\[
\sum_{m\ge0}\|T^m\|<\infty,\qquad
(I_n-T)^{-1}=\sum_{m\ge0}T^m.
\tag{12}
\]
In particular this is an actual bounded inverse, rather than a formal resolvent.
By (7), (8) and (11),
\[
f=(\lambda\otimes1)(I_n-T)^{-1}(\gamma\otimes1).
\tag{13}
\]

To verify scalar division closure, rather than assume it equals matrix rational closure, let $D=\operatorname{Div}_M\mathbb C\langle a_1,\ldots,a_d\rangle$.
Every entry of $T$ lies in $D$.
Choose $N$ so large that $Y=T^N$ has
\[
\max_i\sum_j\|Y_{ij}\|<1.
\]
Every leading principal block of $I_n-Y$ is invertible by its Neumann series.
Induct on its size to show that every entry of each block inverse lies in $D$.
Size one uses a scalar inverse existing in $M$.
For a larger block
\[
\begin{pmatrix}L&b\\c&d\end{pmatrix},
\]
the inverse of the leading block $L$ has entries in $D$ by induction.
Its Schur complement $d-cL^{-1}b$ belongs to $D$ and is invertible in $M$, because the whole block and $L$ are invertible.
Thus its scalar inverse is in $D$, and the block inverse formula gives all remaining entries in $D$.
Finally
\[
(I_n-T)^{-1}
=(I_n+T+\cdots+T^{N-1})(I_n-T^N)^{-1}\in M_n(D).
\]
Together with (13) this proves the second part of (2).
This is the explicit small-power scalar-elimination argument already checked in [Miy22-U005, Lemma 3.8](../audits/literature/Miy22/Yin_U005_v1.md#miy22-u005); no new general matrix-closure assumption is introduced.

### 6. Boundaries and examples

A rank-one series $\alpha_w=t_{i_1}\cdots t_{i_m}$ with $\sum_i|t_i|^2<1$ has exact coefficient norm squared $(1-\sum_i|t_i|^2)^{-1}$.
This theorem gives
\[
\sum_w\alpha_wb_w=
\left(1-\sum_i t_i b_i\right)^{-1}\in D,
\]
even when the crude triangle bound $\sum_i|t_i|\|b_i\|<1$ is unavailable.

Formal rationality regular at zero is equivalent to recognizability, by the source interface in [Miy22-U002](../audits/literature/Miy22/Yin_U002_v1.md#miy22-u002).
It supplies the finite-dimensional algebraic condition in (1); it does not supply the weighted summability (3).
Nor does the assertion that a rational evaluation belongs to affiliated L2 identify it with this Taylor expansion.

For a concrete distinction, take one Haar unitary $u$ and $0<|\lambda|<1$.
The rational function $r(z)=(z-\lambda)^{-1}$ is regular at zero, and its evaluation
\[
r(u)=\sum_{n\ge0}\lambda^n u^{-(n+1)}
\]
is a bounded norm-convergent series.
Its Taylor series at zero is instead
\[
-\sum_{n\ge0}\lambda^{-(n+1)}z^n,
\]
whose coefficients are not square summable at $\|u\|_2=1$.
Moreover $r(u)$ is orthogonal to the nonnegative-power holomorphic subspace.
Thus even regularity at zero and bounded evaluation do not identify an operator with its holomorphic Taylor series.

[Yin_C_F0019](Yin_C_F0019_v1.md#yin_c_f0019) gives the stronger obstruction to unrestricted affiliated rational boundedness: a bounded R-diagonal $a$ with $a^{-1}\in L^2(M)\setminus M$, embedded in a normal generating tuple with a bounded dual system.
The sufficient coefficient theorem above remains valid in that same R-diagonal model.

### 7. Verification boundary

The new proof establishes the proper-subspace adaptation, minimal matrix-entry summability, actual bounded resolvent, and scalar division closure, conditional only on the stated established strong Haagerup theorem and the recorded Yin_C_F0015 sequence argument.
The author checked word order, zero and finite-support cases, the rescaling of coefficients, and the small-power Schur steps.
Independent review was pending when this draft was written.
No computation, formal verification, complete KS07 proof audit, or novelty assessment is claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:36 |
| status | proved |
| reason | Select the actual retained finding and its explicit relationship at the unchanged mathematical input and original source boundaries; no new whole-proof review or changed mathematical status is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#2-orthogonality-and-the-accepted-homogeneous-estimate) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0068_v1.md#historical-holomorphic-realization) | Whole seven-section weighted holomorphic recognizable-series theorem, minimal realization, bounded matrix inverse and scalar inverse elimination, with exact KS07 accepted input and positive-subspace boundary. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:33 |
| status | proved |
| reason | Adopt the newly performed isolated whole-proof inspection completed at 2026-10-22T20:28; the fixed weighted theorem and mathematical argument are unchanged, and older findings retain their actual dates and context limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete weighted recognizable holomorphic-series theorem for the stated finite free identically distributed nonzero bounded R-diagonal family. |
| argument | [Complete argument](#2-orthogonality-and-the-accepted-homogeneous-estimate) | Sections 2-6: holomorphic orthogonality, accepted KS07 inequality, scalar energy decay, minimal entry summability, bounded matrix inverse, scalar elimination and boundary examples. |
| review | [Isolated whole finding](../audits/reviews/Yin_R_F0068_v1.md#current-holomorphic-realization) | Actual 2026-10-22 independent whole inspection at the stated KS07 and C_F0015 interfaces; no unrestricted affiliated rational boundedness or full external-proof audit. |

## Historical assessments


<a id="decision-candidate-0002"></a>
### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-orthogonality-and-the-accepted-homogeneous-estimate) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0068_v1.md#historical-holomorphic-realization) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Original review finding, dated 2026-09-09: [retained same historical finding](../audits/reviews/Yin_R_F0068_v1.md#historical-holomorphic-realization).
Its relocation does not substitute the new 2026-10-22 review into earlier decisions.

Material covered by that review: [Exact material](Yin_C_F0017_v1.md).
