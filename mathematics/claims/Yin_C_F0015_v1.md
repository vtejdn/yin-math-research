---
author: Yin
---

# Finite residuals and subexponential homogeneous estimates imply boundedness

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Finite Residual Spaces and Subexponential Homogeneous Bounds

<a id="statement"></a>

<a id="yin_c_f0015"></a>
## Yin_C_F0015: A Reusable L2-to-Boundedness Lemma

Date: 2026-09-09.
Provenance: project deduction by another AI agent, abstracting the mechanisms already audited in [Miy22-U002](../audits/literature/Miy22/Yin_U002_v1.md#miy22-u002), [Miy22-U004](../audits/literature/Miy22/Yin_U004_v1.md#miy22-u004), and [Miy26-U002](../audits/literature/Miy26/Yin_U002_v1.md#miy26-u002).
Authorization: the user requested a precise reusable sufficient condition for the proposed L2 extension after [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
The completed goal is not reopened.
Initial assessment: complete proof draft awaiting independent review.
The [selected assessment](#decision-isolated-review-20261022) records the mathematical and review assessments.
No novelty claim is made.

## 1. Statement

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal tracial state, $H=L^2(M,\tau)$, and $\Omega=1$.
Fix a finite alphabet $\mathcal A=\{1,\ldots,d\}$, $d\ge1$, and its free monoid $\mathcal A^*$, including the empty word $\varepsilon$.

Suppose bounded elements $P_w\in M$, indexed by $w\in\mathcal A^*$, satisfy:

1. $P_\varepsilon=1$ and the vectors $(P_w\Omega)_{w\in\mathcal A^*}$ form an orthonormal basis of $H$.
2. There are positive constants $K_m$, $m\ge0$, such that for every scalar coefficient family on words of length $m$,
   \[
   \left\|\sum_{|w|=m}c_wP_w\right\|_M
   \le K_m\left(\sum_{|w|=m}|c_w|^2\right)^{1/2},
   \qquad
   \limsup_{m\to\infty}K_m^{1/m}\le1.
   \tag{1}
   \]

The indexing does not assume $P_{uv}=P_uP_v$.
In applications the $P_w$ may be orthogonal word polynomials; their actual multiplication rules must be treated separately.

Let $f\in L^2(M,\tau)$, regarded also as its canonical affiliated operator, and write
\[
\widehat f=f\Omega=\sum_{w\in\mathcal A^*}\alpha_wP_w\Omega,
\qquad
\sum_w|\alpha_w|^2=\|f\|_2^2<\infty.
\tag{2}
\]
Assume its right residual space is finite dimensional:
\[
V_\alpha=\operatorname{span}_{\mathbb C}
\{R_v\alpha:v\in\mathcal A^*\},
\qquad
(R_v\alpha)(w)=\alpha_{wv},
\qquad
\dim V_\alpha<\infty.
\tag{3}
\]

Then its homogeneous expansion converges absolutely in operator norm:
\[
\sum_{m=0}^{\infty}
\left\|\sum_{|w|=m}\alpha_wP_w\right\|_M<\infty.
\tag{4}
\]
Its norm sum equals the affiliated operator $f$.
In particular,
\[
f\in
\overline{\operatorname{span}_{\mathbb C}\{P_w:w\in\mathcal A^*\}}^{\,\|\cdot\|_M}
\subseteq C^*(P_w:w\in\mathcal A^*)\subseteq M.
\tag{5}
\]
If every $P_w$ is a polynomial in a fixed bounded tuple $X$, this includes $f\in C^*(X)$.

Condition (3) is equivalent to finite algebraic rank of the coefficient Hankel matrix $(\alpha_{uv})_{u,v\in\mathcal A^*}$ and to a finite scalar linear realization of the coefficients.
These equivalences are proved below, so either condition can replace (3).

This is a scalar boundedness lemma.
It assumes neither a dual system nor algebraic rationality of $f$ in the original generators, and needs no estimate for an entire inverse matrix.
An application starting with affiliated rationality must separately prove (3) in its chosen orthonormal basis.

## 2. Hankel Rank and Finite Linear Realizations

For an arbitrary sequence $\alpha$ on $\mathcal A^*$, form
\[
\mathsf H_\alpha(u,v)=\alpha_{uv}.
\tag{6}
\]
Its algebraic rank is the supremum of the ranks of finite submatrices.
This equals the dimension of its column span as functions on $\mathcal A^*$.
Indeed, any $r$ independent columns remain independent on a finite set of row coordinates: coordinate evaluations separate their finite-dimensional span, and finitely many already have zero common kernel.
Conversely, every finite submatrix rank is bounded by the full column-span dimension.
These columns are exactly $R_v\alpha$, proving the equivalence with (3).

A finite linear realization means
\[
\alpha_w=\lambda A_w\gamma,\qquad
A_w=A_{i_1}\cdots A_{i_m}\quad(w=i_1\cdots i_m),
\qquad A_\varepsilon=I_n,
\tag{7}
\]
for finitely many matrices $A_i\in M_n(\mathbb C)$, a scalar row $\lambda$, and a scalar column $\gamma$.
The row uses ordinary complex matrix multiplication, not an implicit conjugate transpose.

If (3) holds and $\alpha\ne0$, use $V_\alpha$ as the state space.
For any coefficient function $v$, set $(R_i v)(w)=v(wi)$.
The space is invariant under these maps because
\[
R_iR_v\alpha=R_{iv}\alpha.
\]
Take $A_i$ to be their matrices in a basis of $V_\alpha$, let $\gamma$ represent $\alpha=R_\varepsilon\alpha$, and let $\lambda(v)=v(\varepsilon)$.
The suffix order satisfies
\[
R_{i_1}\cdots R_{i_m}=R_{i_1\cdots i_m},
\qquad
\lambda R_w\alpha=\alpha_w,
\]
so this gives (7).
Conversely, (7) gives
\[
(R_v\alpha)(w)=\lambda A_w(A_v\gamma).
\]
Thus the residuals are in the image of one linear map from $\mathbb C^n$ to functions on words, and $\dim V_\alpha\le n$.

The column-space realization has the smallest possible dimension, namely $\dim V_\alpha$.
It is reachable, since the states $R_v\alpha$ span it.
It is observable, since $\lambda R_wv=v(w)=0$ for all $w$ implies $v=0$.
These are finite scalar state-space properties, not assertions about bounded multiplier realizations in $M$.
When $\alpha=0$, the residual space and Hankel rank are zero and all conclusions hold directly; a one-dimensional zero-output realization is also available.

Under (2), every residual is in $\ell^2(\mathcal A^*)$ because its coefficients are a subset of the original sequence.
Finite algebraic Hankel rank then also means that (6) extends to a bounded finite-rank operator on $\ell^2(\mathcal A^*)$.
To see this, choose residual columns $c_1,\ldots,c_r$ forming a basis and finitely many row-coordinate evaluations determining coordinates in that basis.
Each coefficient of the $v$th column in this basis is a finite linear combination of rows $v\mapsto\alpha_{uv}$.
Each such row is in $\ell^2$, since prefixing a fixed word is injective.
Those coefficient functionals are therefore bounded on finitely supported inputs, and the column expansion gives a bounded finite-rank operator, of rank $r$.
Conversely, finite rank of such an operator bounds its column span.

The further equivalence with rationality of the formal series $\sum_w\alpha_w z^w$ is the source-statement-verified Schuetzenberger interface in [Miy22-U002](../audits/literature/Miy22/Yin_U002_v1.md#miy22-u002), Theorem 2.5.
It is not needed for this proof.
Its formal variables $z_i$ must be distinguished from operator generators.

## 3. Degree Energy: Finite Recurrence and Exponential Decay

For a nonzero $\alpha$, choose any finite realization (7), and put
\[
e_m=\sum_{|w|=m}|\alpha_w|^2,\qquad
B=\sum_{i=1}^d A_i\otimes\overline{A_i},\qquad
c=\lambda\otimes\overline{\lambda},\qquad
b=\gamma\otimes\overline{\gamma}.
\]
Expanding the matrix power over all words gives
\[
e_m=cB^m b\qquad(m\ge0).
\tag{8}
\]
Here products of tensor matrices satisfy
\[
(A_{i_1}\otimes\overline{A_{i_1}})\cdots
(A_{i_m}\otimes\overline{A_{i_m}})
=A_w\otimes\overline{A_w},
\]
which verifies both the ordering and conjugation in (8).

Cayley-Hamilton supplies a constant-coefficient recurrence of order at most $n^2$.
If $N=n^2$ and
\[
\chi_B(t)=t^N+\sum_{j=0}^{N-1}\beta_jt^j,
\]
then
\[
e_{m+N}+\sum_{j=0}^{N-1}\beta_je_{m+j}=0
\qquad(m\ge0).
\tag{9}
\]
The scalar generating function is rational:
\[
E(z)=\sum_{m\ge0}e_mz^m=c(I-zB)^{-1}b.
\tag{10}
\]

Since $e_m\ge0$ and $\sum_me_m=\|f\|_2^2<\infty$, this power series is holomorphic in the open unit disk and uniformly bounded there by $\|f\|_2^2$.
Reduce the scalar rational function by canceling common factors.
It has no pole inside that disk, by holomorphy of the agreeing power series.
Nor can it have a pole at a point $\zeta$ of the unit circle: a genuine pole would make $|E(r\zeta)|$ diverge as $r\uparrow1$, contrary to the uniform bound.

The reduced function is therefore holomorphic on some disk of radius $R>1$.
Choose $1<r<R$ and apply Cauchy's coefficient estimate:
\[
0\le e_m\le Cr^{-m}=C\rho^{2m},\qquad
C=\max_{|z|=r}|E(z)|,\qquad
\rho=r^{-1/2}\in(0,1).
\tag{11}
\]
If $E$ is a polynomial, choose any finite $r>1$ instead.
Thus finite-support sequences and nilpotent cases are included.
For $\alpha=0$, take $C=0$ and any $0<\rho<1$.

This concerns the active scalar energy sequence.
It does not assert that $B$ in an arbitrary nonminimal realization has spectral radius below one: unused or canceled states can contain irrelevant growth.
Nor is a decay bound at the exact largest active eigenvalue modulus claimed.
The strict choice of radius in (11) accommodates repeated poles and their polynomial coefficient factors.

## 4. Operator-Norm Convergence and Affiliated Identification

Write
\[
F_m=\sum_{|w|=m}\alpha_wP_w.
\]
The assumed homogeneous estimate and (11) give
\[
\|F_m\|_M\le\sqrt C K_m\rho^m.
\tag{12}
\]
Choose $1<\sigma<\rho^{-1}$.
The limit superior in (1) provides a finite constant $C_\sigma$ with $K_m\le C_\sigma\sigma^m$ for every $m\ge0$: the eventual bound follows from the limit superior, and the finite initial segment is absorbed into the constant.
Hence
\[
\sum_{m\ge0}\|F_m\|_M
\le\frac{\sqrt C C_\sigma}{1-\sigma\rho}<\infty.
\tag{13}
\]

The norm sum $a=\sum_mF_m$ belongs to the norm-closed linear span in (5).
Since the trace is normalized, $\|x\|_2\le\|x\|_M$ for bounded $x$, so the same partial sums converge in $L^2$ to $a\Omega$.
Their orthonormal expansion (2) converges in $L^2$ to $\widehat f$.
Uniqueness of that Hilbert-space limit gives $a\Omega=\widehat f$.
The canonical inclusion of $L^2(M,\tau)$ into the finite affiliated algebra is injective, so $f=a$ as affiliated operators.
This proves (4)-(5).

Absolute convergence is asserted for homogeneous blocks.
It does not assert absolute summability of the individual norms $\|\alpha_wP_w\|$ over all words, or arbitrary rearrangement of that stronger sum.
Each homogeneous block is finite because the alphabet is finite.

## 5. A Stable Backward-Shift Structure and Its Stein Identity

The residual condition has a concrete Hilbert-space interpretation.
On the coefficient space $\ell^2(\mathcal A^*)$,
\[
\|v\|_{\ell^2}^2
=|v(\varepsilon)|^2+\sum_{i=1}^d\|R_iv\|_{\ell^2}^2.
\tag{14}
\]
Indeed, each nonempty word has exactly one last letter.
When $V_\alpha$ is finite dimensional, set $T_i=R_i|_{V_\alpha}$ and $\ell(v)=v(\varepsilon)$.
Its inherited Hilbert norm gives the finite-dimensional Stein identity
\[
I=\ell^*\ell+\sum_iT_i^*T_i.
\tag{15}
\]
In an arbitrary scalar coordinate basis this reads
\[
G=\lambda^*\lambda+\sum_i A_i^*GA_i
\]
for the positive definite Gram matrix $G$ of the residual basis.
Thus a positive energy norm is supplied by the actual coefficient-space geometry, not postulated merely from formal matrices.

Observability gives a finite $N\ge1$ for which the functionals $\ell T_w$ with $|w|<N$ have zero common kernel.
All word-coordinate evaluations separate $V_\alpha$; a finite selection already does in finite dimension, and $N$ may exceed their lengths.
Compactness of the unit sphere then gives $\delta>0$ such that
\[
\sum_{|w|<N}|\ell T_wv|^2\ge\delta\|v\|^2
\qquad(v\in V_\alpha).
\tag{16}
\]
For the zero state space, this discussion is unnecessary.

Iterating (14) gives
\[
\|v\|^2
=\sum_{|w|<N}|\ell T_wv|^2
+\sum_{|w|=N}\|T_wv\|^2.
\tag{17}
\]
The suffix order can be grouped by successively prepended letters during iteration; the set of all words of each length is unchanged.
Equations (16)-(17) imply $0<\delta\le1$ and
\[
\sum_{|w|=N}\|T_wv\|^2
\le(1-\delta)\|v\|^2.
\tag{18}
\]
This is a uniform strict contraction of the state energy after a fixed finite number of steps.

If $\delta=1$, every length-$N$ state product vanishes, so the coefficient sequence has finite support.
If $\delta<1$, iterating (18) gives geometric decay every $N$ steps.
For intermediate steps the total state energy cannot increase by (14), and $|\ell v|\le\|v\|$.
In particular, applying these estimates to the initial state $\alpha$ also proves exponential degree-energy decay.

This independently explains Section 3 through finite-dimensional reachability, observability, and a positive Gramian.
It concerns the chosen coefficient shifts.
A finite family of affiliated rational states in $L^2(M)$ need not be invariant under those shifts and does not, by itself, supply (14)-(18).

## 6. Reuse and Scope Boundaries

For a standard free semicircular tuple, the Wick/Chebyshev word polynomials provide the orthonormal basis and $K_m=m+1$, as reconstructed in [Miy22-U004](../audits/literature/Miy22/Yin_U004_v1.md#miy22-u004).
[Miy26-U002](../audits/literature/Miy26/Yin_U002_v1.md#miy26-u002) separately proves that an affiliated rational L2 element has finite residual dimension in that basis.
Combining those two model-specific inputs with this lemma recovers its boundedness mechanism.

A polynomial Haagerup estimate $K_m\le C_0(m+1)^s$, with fixed $C_0>0$ and $s\ge0$, satisfies (1).
Subexponential growth is sufficient because the energy decay is exponential.
If only exponential evaluation growth is known, the same proof works for a particular coefficient sequence whenever its actual decay makes $\sum_mK_m\rho^m$ finite.
That exponential evaluation bound alone does not give the universal conclusion stated here.

The Hankel rank is the rank of the coefficient matrix (6), not automatically a dual commutator rank.
An application using commutators must establish its coefficient identity with the appropriate domains and word order, as Miy26-U002 does.

Algebraic rationality in generators $X$ and recognizability of coefficients in the $P_w$ basis are distinct assertions.
The map $z^w\mapsto P_w(X)$ need not be multiplicative.
Therefore a free-field expression for $f$ does not automatically give the finite coefficient realization (7).
The [Yin_C_F0014 obstruction](Yin_C_F0014_v1.md#yin_c_f0014) also excludes treating algebraic rationality and an abstract L2 assumption as sufficient in every bounded-dual model.

The conclusion proves scalar boundedness and norm-closed-algebra membership.
It does not alone prove
\[
f\in\operatorname{Div}_M\mathbb C\langle X\rangle.
\]
That stronger conclusion may require a bounded rational representation and a separate elimination argument.
Estimates for an entire inverse matrix belong to that further problem; they are not hypotheses of this scalar lemma.

## 7. Verification Boundary

The proof directly establishes the residual/Hankel/linear-realization equivalences, finite recurrence, exponential decay including zero and finite-support cases, norm convergence, and stable backward-shift/Gramian interpretation.
The further equivalence with formal rational series retains the source-verification scope of Miy22-U002 and is not used in the argument.

The author checked suffix order, the tensor-conjugate energy identity, the distinction between active poles and unused states, the affiliated identification, and the word partition in the Stein identity.
Initial review status is a complete draft awaiting independent mathematical review.
No computation, new source acquisition, formal verification, external human review, or novelty assessment is claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:32 |
| status | proved |
| reason | Select the exact retained finding with its actual relationship and original mathematical scope. The statement, argument, status, original review date and historical decisions remain unchanged; no new whole-proof review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#2-hankel-rank-and-finite-linear-realizations) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0063_v1.md#finite-residual-finding) | Complete orthonormal expansion, finite residual realization, energy recurrence, decay, boundedness and norm-closed span theorem with all stated inputs; no automatic rational-to-residual or scalar-division conclusion. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:53 |
| status | proved |
| reason | Adopt the actual context-isolated whole-argument review after complete comparison with the old finding, retaining fixed mathematics, exact assumptions and historical adoption facts. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-hankel-rank-and-finite-linear-realizations) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0063_v1.md#residual-boundedness) | Complete coefficient/Hankel realization, active energy recurrence and decay, norm convergence, affiliated identification and Stein structure under the stated hypotheses; no automatic rational-to-residual or scalar division conclusion. |

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
| argument | [Exact material](#2-hankel-rank-and-finite-linear-realizations) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0063_v1.md#finite-residual-finding) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0063_v1.md#finite-residual-finding).

Material covered by that review: [Exact material](Yin_C_F0015_v1.md).
