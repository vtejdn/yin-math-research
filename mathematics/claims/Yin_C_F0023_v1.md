---
author: Yin
---

# Bounded normalized duals for all finite-dimensional q-Gaussian tuples with abs(q)<1

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Bounded Normalized Duals from Degree-Weighted Conjugate Expansions

<a id="statement"></a>

<a id="yin_c_f0023"></a>
## Yin_C_F0023: Simultaneous Bounded Duals for the Full q-Gaussian Interval

Date: 2026-09-09.
Context: the user requested a re-examination of the main rationality theorem under MS23-type polynomial-domain duals or conjugate variables.
Provenance: project deduction by another AI agent, using the fully audited MS23 conjugate expansion and a polynomial-degree triangular reconstruction proved here.
the coordinating agent allocated Yin_C_F0023 for this deduction.
Initial assessment: complete proof draft and author self-check, awaiting independent review of this written artifact.
The [selected assessment](#decision-candidate-0002) records the mathematical and review assessments; independent review evidence must be recorded separately.
No source priority, historical novelty, formal verification or human-review claim is made.

## 1. Statement

Fix a finite integer $d\geq1$ and a real parameter $-1<q<1$.
Let $A=(A_1,\ldots,A_d)$ be the canonical variance-one selfadjoint q-Gaussian tuple, and let

\[
M=\Gamma_q(\mathbb R^d),\qquad
H=L^2(M,\tau)=\mathcal F_q(\mathbb C^d),\qquad
\Omega=1,\qquad P=P_\Omega.
\]

The trace is the faithful vacuum trace, and elements of $M$ act on $H$ by left multiplication.
Let $D_i$ be MS23's normalized dual on the algebraic Fock space, equivalently on $\mathcal A=\mathbb C\langle A\rangle\Omega$:

\[
D_i\Omega=0,\qquad
[D_i,A_j]=\delta_{ij}P\quad\text{on }\mathcal A.
\tag{1}
\]

Then every $D_i$ has a unique bounded extension $B_i\in B(H)$.
The complete tuple of extensions satisfies

\[
B_i\Omega=0,\qquad
[B_i,A_j]=\delta_{ij}P\quad\text{on all }H.
\tag{2}
\]

Here is an explicit convergent bound.
Put $t=|q|$, and retain the constants from [MS23-U003](../audits/literature/MS23/Yin_U003.md#ms23-u003):

\[
C_t=\prod_{k\geq1}(1-t^k)^{-1},\qquad
c=w(q)^{-1/2},\qquad
w(q)^2=(1-t^2)^{-1}\prod_{k\geq1}\frac{1-t^k}{1+t^k}.
\tag{3}
\]

For $[m]_t!=\prod_{j=1}^{m}(1+t+\cdots+t^{j-1})$ and $[0]_t!=1$,

\[
\boxed{\displaystyle
\|B_i\|\leq
C_t^{3/2}\sum_{m\geq0}
(2m+1)(2m+2)d^m t^{m(m+1)/2}
c^{m+1}\sqrt{[m]_t!}<\infty.}
\tag{4}
\]

At $q=0$, take $0^0=1$; only the $m=0$ summand survives.
The estimate is not asserted to be sharp or uniform as $|q|$ approaches one or $d$ increases.
No assertion is made at $q=\pm1$.

The same construction proves the general sufficient condition in Section 2: conjugates with an absolutely convergent polynomial expansion whose operator norms remain summable after multiplication by polynomial degree admit bounded normalized duals.
Boundedness of the conjugates alone is not the hypothesis of that result.

## 2. A General Polynomial-Degree Criterion

Let $X=(X_1,\ldots,X_d)$ be bounded selfadjoint generators of a finite von Neumann algebra $(M,\tau)$ with faithful normal tracial state.
Assume that the tuple is algebraically free and has conjugate variables $\xi_i\in L^2(M)$, with the convention

\[
\tau(\xi_i p)=(\tau\otimes\tau)(\partial_i p),
\qquad p\in\mathcal A:=\mathbb C\langle X\rangle,
\qquad \partial_i X_j=\delta_{ij}1\otimes1.
\tag{5}
\]

Suppose that, for each $i$, there are polynomials $a_{i,r}$ and nonnegative integers $N_{i,r}$ such that

\[
\deg a_{i,r}\leq N_{i,r},\qquad
\xi_i=\sum_{r\geq0}a_{i,r}\quad\text{in }L^2(M),
\qquad
\sum_{r\geq0}(N_{i,r}+1)\|a_{i,r}\|<\infty.
\tag{6}
\]

The last condition implies convergence in operator norm to an element of $C^*(X)$.
Its $L^2$ limit agrees with the specified conjugate, so $\xi_i$ is that bounded element.
Define on the dense polynomial vector space

\[
D_i p=(\mathrm{id}\otimes\tau)(\partial_i p).
\tag{7}
\]

Then $D_i$ has a bounded extension $B_i$ with

\[
\|B_i\|\leq\sum_{r\geq0}N_{i,r}\|a_{i,r}\|,
\qquad B_i\Omega=0,
\qquad [B_i,X_j]=\delta_{ij}P.
\tag{8}
\]

The extra one in (6) handles constant polynomials and ensures the asserted operator-norm convergence before any triangular truncation is performed.
The summands need not be homogeneous or selfadjoint.
Only their degree bounds and the displayed summability are required.

### 2.1. The adjoint identity

Use an inner product linear in its second variable, $\langle a,b\rangle=\tau(a^*b)$.
The polynomial space is dense in $H=L^2(M)$ because $X$ is selfadjoint and generates $M$.
Formula (7) implies $D_i1=0$ and

\[
[D_i,X_j]p=\delta_{ij}\tau(p)\Omega.
\tag{9}
\]

Conjugate variables for selfadjoint tuples are selfadjoint: applying (5) to $p^*$, conjugating, and using the flip-star relation for the difference quotient gives the same conjugate identity for $\xi_i^*$, and density gives equality.
For $a,p\in\mathcal A$, expand

\[
\partial_i(a^*p)=(\partial_i a^*)(1\otimes p)+(a^*\otimes1)\partial_i p.
\]

The first term has scalar trace $\langle D_i a,p\rangle$, by the flip-star relation for $\partial_i a^*$.
The second has scalar trace $\langle a,D_i p\rangle$.
Equation (5) and traciality therefore give

\[
\langle D_i a,p\rangle
=\langle a,p\xi_i-D_i p\rangle.
\tag{10}
\]

All vectors on the right belong to $L^2(M)$ because $p$ is bounded and $\xi_i\in L^2(M)$.
Thus $p\in\operatorname{dom}D_i^*$ and

\[
D_i^*p=p\xi_i-D_i p.
\tag{11}
\]

This directly reconstructs the adjoint interface in [MS23-U001, Equation (5)](../audits/literature/MS23/Yin_U001.md#ms23-u001).
In its commutator notation, the additional simplification is $[D_i,p^*]^*\Omega=D_i p$.
Once (6) identifies $\xi_i$ as bounded, (11) becomes

\[
(D_i+D_i^*)p=\rho(\xi_i)p\quad(p\in\mathcal A),
\tag{12}
\]

where $\rho(a)v=va$ denotes right multiplication.
This is initially an identity on the polynomial domain, not an assumption that $D_i$ is already bounded.

### 2.2. Orthogonal polynomial degree

Let $V_n\subset H$ be the span of polynomial vectors of degree at most $n$, let $V_{-1}=\{0\}$, and set

\[
H_n=V_n\ominus V_{n-1},\qquad P_n=P_{H_n}.
\]

Each $V_n$ is finite dimensional, $\mathcal A=\bigoplus_{n\geq0}^{\mathrm{alg}}H_n$, and $H=\bigoplus_{n\geq0}H_n$.
Formula (7) lowers polynomial degree, so

\[
D_i H_n\subseteq V_{n-1}.
\tag{13}
\]

For $v\in H_n$ and $w\in H_l$ with $l\leq n$, (13) gives $\langle w,D_i^*v\rangle=\langle D_iw,v\rangle=0$.
Consequently $P_lD_i^*P_n=0$ when $l\leq n$.
Combining this with (12)-(13) determines every matrix block of $D_i$:

\[
P_lD_iP_n=
\begin{cases}
P_l\rho(\xi_i)P_n,&l<n,\\
0,&l\geq n.
\end{cases}
\tag{14}
\]

Thus $D_i$ is the strict degree-lowering part of $\rho(\xi_i)$.
This block identity does not yet prove boundedness: unrestricted triangular truncation on $B(H)$ cannot be used as a bounded map here.

### 2.3. A bounded polynomial has finite degree bandwidth

Let $a\in\mathcal A$ have degree at most $N$.
Right multiplication satisfies $\|\rho(a)\|=\|a\|$ and maps $V_n$ into $V_{n+N}$.
Hence $P_l\rho(a)P_n=0$ when $l>n+N$.

For the other side, take $v_l\in H_l$ and $v_n\in H_n$ with $l+N<n$.
Traciality gives

\[
\langle v_l,v_na\rangle
=\tau(v_l^*v_na)
=\tau(av_l^*v_n)
=\langle v_la^*,v_n\rangle=0,
\tag{15}
\]

because $v_la^*\in V_{l+N}\subset V_{n-1}$.
Selfadjointness of the generators ensures that $a^*$ still has degree at most $N$.
Therefore

\[
P_l\rho(a)P_n=0\qquad\text{if }|l-n|>N.
\tag{16}
\]

This proof uses the orthogonal polynomial filtration and traciality, without a Fock orthonormal-word assumption.

### 2.4. Extracting finitely many lowering diagonals

For $T\in B(H)$ and an integer $k\geq1$, define

\[
E_k(T)=\sum_{n\geq k}P_{n-k}TP_n.
\tag{17}
\]

The series converges strongly on every vector.
Indeed, its summands have mutually orthogonal ranges, and for $v\in H$,

\[
\sum_{n\geq k}\|P_{n-k}TP_nv\|^2
\leq\|T\|^2\sum_{n\geq k}\|P_nv\|^2
\leq\|T\|^2\|v\|^2.
\tag{18}
\]

Thus $\|E_k(T)\|\leq\|T\|$.
Put $L_0(T)=0$ and $L_N(T)=\sum_{k=1}^{N}E_k(T)$ for $N\geq1$.
Then

\[
\|L_N(\rho(a))\|\leq N\|a\|.
\tag{19}
\]

When $\deg a\leq N$, (16) shows that $L_N(\rho(a))$ contains exactly all blocks $P_l\rho(a)P_n$ with $l<n$, and no other blocks.
There is no infinite-diagonal norm estimate in (19).

### 2.5. Reconstructing the bounded dual

Under (6), the series

\[
B_i=\sum_{r\geq0}L_{N_{i,r}}(\rho(a_{i,r}))
\tag{20}
\]

converges in operator norm by (19), with the bound in (8).
For each pair $l<n$, its $(l,n)$ block is

\[
P_lB_iP_n
=\sum_rP_l\rho(a_{i,r})P_n
=P_l\rho(\xi_i)P_n.
\tag{21}
\]

In the first equality, a summand with $n-l>N_{i,r}$ is zero by (16).
The second equality is justified by the operator-norm convergence in (6).
For $l\geq n$, all blocks of $B_i$ are zero by construction.
Comparing with (14), $B_i$ and $D_i$ agree on each $H_n$, hence on $\mathcal A$.
To identify their vectors it suffices to compare every orthogonal projection $P_l$, whose ranges span $H$; no interchange involving an unbounded $D_i$ is used.

Equation (9) now gives $[B_i,X_j]=\delta_{ij}P$ on the dense polynomial space.
Both operators in this equality are bounded, so the identity extends to all $H$.
Also $B_i\Omega=D_i\Omega=0$.
The bounded extension is unique because $\mathcal A$ is dense.
This proves (8) and the general criterion.

As a useful special case, a conjugate given by an absolutely convergent noncommutative power series at some radius $R>\max_j\|X_j\|$ satisfies (6) when its coefficient norm $\sum_w|c_w|R^{|w|}$ is finite.
Writing $r=\max_j\|X_j\|$, one has $\sum_w(|w|+1)|c_w|\|X_w\|\leq\sup_{n\geq0}(n+1)(r/R)^n\sum_w|c_w|R^{|w|}<\infty$.
The explicit q-Wick estimate below already supplies (6), so this analytic-series corollary is not needed for Yin_C_F0023.

## 3. Applying the Criterion to MS23

The consumed source interfaces are precise:

- [MS23-U001](../audits/literature/MS23/Yin_U001.md#ms23-u001), published pp. 5-10, supplies the q-Fock conventions, bounded generators and faithful trace, triangular Wick evaluation, the polynomial-domain dual/conjugate interface, and bounded free right deletion.
- [MS23-U002](../audits/literature/MS23/Yin_U002.md#ms23-u002), Proposition 4.5 and its complete proof, published pp. 14-22, identifies the normalized dual with the special crossing-partition formula and verifies (1).
- [MS23-U003](../audits/literature/MS23/Yin_U003.md#ms23-u003), Theorem 4.6 and Corollary 4.7, published pp. 22-26, gives the conjugate expansion and the homogeneous operator-norm majorant used below.

The source audit retains q-Fock positivity, the uniform deletion bound and the homogeneous Haagerup estimate as established inputs at its stated original-proof inspection depths.
This deduction does not silently upgrade those inspection depths or require a new result from the source's later Lipschitz or Gibbs-potential sections.

Write $r_j$ for MS23's bounded free right deletion, with $\|r_j\|\leq c$.
For a word $w$ of length $m$, $r_{iw}=r_i r_w$ deletes $m+1$ letters, and its q-adjoint $r_{iw}^*$ raises particle degree by $m+1$.
Let $W$ be the Wick map from a finite particle vector to its polynomial in $A$.
Set

\[
\eta_{i,m}=(-1)^m q^{m(m+1)/2}\sum_{|w|=m}r_{iw}^*e_w,
\qquad a_{i,m}=W(\eta_{i,m}).
\tag{22}
\]

The vector $\eta_{i,m}$ lies in particle degree $2m+1$, so $a_{i,m}$ is a polynomial of degree at most $2m+1$.
Triangular Wick evaluation identifies particle degree with the orthogonal polynomial degree used in Section 2.
In particular no assertion that the individual tensor words $e_w$ are orthonormal in the q-inner product is made.

MS23-U003, Equations (2), (8)-(10), establishes

\[
\xi_i=D_i^*\Omega=\sum_{m\geq0}a_{i,m}\quad\text{in }L^2(M)\text{ and operator norm},
\tag{23}
\]

and, taking absolute values for negative $q$,

\[
\|a_{i,m}\|
\leq (2m+2)C_t^{3/2}d^m t^{m(m+1)/2}
c^{m+1}\sqrt{[m]_t!}.
\tag{24}
\]

To recall the complete estimate, each $r_{iw}^*e_w$ has q-norm at most $c^{m+1}\sqrt{[m]_t!}$; there are $d^m$ words; and the homogeneous Haagerup inequality in degree $2m+1$ contributes $(2m+2)C_t^{3/2}$.
The powers of $q$ in (22) come from the compulsory quadratic crossing count in the source, while the norm estimate (24) uses $t=|q|$.

For $0<t<1$, the positive summands in the right side of (4), without the common factor $C_t^{3/2}$, have consecutive ratio

\[
t^{m+1}dc\sqrt{[m+1]_t}\,
\frac{(2m+3)(2m+4)}{(2m+1)(2m+2)}
\longrightarrow0,
\tag{25}
\]

since $[m+1]_t\leq(1-t)^{-1}$.
The same conclusion holds with the factor $2m+1$ replaced by $2m+2$, so (24) verifies all of (6) with $N_{i,m}=2m+1$.
At $t=0$, (22) has only its $m=0$ term, and the convergence assertion is immediate.

The construction (20) now reads explicitly

\[
\boxed{\displaystyle
B_i=\sum_{m\geq0}\sum_{k=1}^{2m+1}
\sum_{n\geq k}P_{n-k}\rho(a_{i,m})P_n.}
\tag{26}
\]

The innermost sum converges strongly by (18); the sum over $k$ is finite; the outer sum converges in operator norm by (4).
These prescribed convergence modes define an everywhere bounded operator.
The proof of Section 2 identifies it with the normalized dual on the polynomial space, and (24)-(25) give exactly (4).
This proves the all-q statement (2).

## 4. Consequences and Scope of the Update

For the canonical tuple, the already reviewed [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013) now applies throughout $-1<q<1$ and every finite $d$.
In particular, with $F_A=\operatorname{Div}_{U(M)}\mathbb C\langle A\rangle$,

\[
F_A\cap M
=\{f\in M:\operatorname{rank}[B_i,f]<\infty\text{ for every }i\}.
\tag{27}
\]

The affiliated part of Yin_C_F0013 retains its bounded cleared-denominator defects; it is not replaced by a literal commutator of two unbounded operators.
Equation (27) neither proves $F_A\cap L^2(M)\subseteq M$ nor identifies $F_A\cap M$ with $\operatorname{Div}_M\mathbb C\langle A\rangle$.
Those analytic rationality questions have additional content.

[Yin_C_F0020 A](Yin_C_F0020_v1.md#yin_c_f0020) remains a valid, distinct construction using the projective kernel inverse to correct right q-annihilation in a quantitative small-q range.
Yin_C_F0023 instead recovers the normalized dual from the conjugate's degree expansion and covers the full interval.
The source's free deletion, right q-annihilation, and normalized dual remain different operators when $q\ne0$.

The MS23 source audit correctly isolated its vacuum and conjugate norm estimates from an estimate for $D_i$ itself.
After that audit, the present additional triangular reconstruction supplies the missing passage to the whole operator.
Accordingly, an earlier research assessment that only the small-q bounded-dual range was established is superseded by Yin_C_F0023 once its independent proof review is accepted.
This is a new project deduction from the audited source inputs, not a claim that the published proof explicitly contained (26), and not an alteration of the previously recorded Yin_C_F0020 or MS23 audit artifacts.

## 5. Checks and Review Boundary

The author checked the adjoint convention, both sides of the degree-bandwidth estimate, strong convergence of individual diagonals, norm convergence of the outer series, and the blockwise identification before extending any commutator.
At $q=0$, the only conjugate term is $a_{i,0}=A_i$, and its degree-lowering right-multiplication part is the standard free right annihilator, recovering the normalized semicircular dual.
For negative $q$, the signed coefficients in (22) are unchanged; only the estimates use $|q|$.
Finite dimension is used in the finite-dimensional polynomial layers and the factor $d^m$.

The general proof explicitly avoids inferring boundedness of an unrestricted triangular truncation merely from $\xi_i\in M$.
It also avoids estimating the non-vacuum partition sum directly or applying an unbounded right multiplier.
Every $\rho(a_{i,m})$ and $\rho(\xi_i)$ used in the operator-norm argument is bounded.

An exploratory web search for q-Gaussian bounded duals and triangular conjugate constructions did not identify a relevant priority reference in the inspected results.
It supplied no mathematical dependency and does not establish novelty or absence of an earlier theorem.
The proof uses the local audited MS23 units at the explicit locators above.
No numerical test, formal verification, external human review or author confirmation has been performed for Yin_C_F0023.
An independent agent was assigned to review the complete written proof; its final report and actual inspected scope are recorded in the separate proof review selected by this Claim.


## Assessment history


### Decision candidate-0002

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
| argument | [Exact material](#2-a-general-polynomial-degree-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0011_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:41 |
| status | proved |
| reason | Select the actual retained findings and their individual checking relationships, with unchanged mathematical status, statement and argument. Original findings, dates, accepted-source depths and historical decisions remain intact; this is no new mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#2-a-general-polynomial-degree-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0011_v1.md#degree-weighted-duals-original-finding) | Original complete proof reconstruction after relevant preliminary mathematical contribution; original source and nonconclusion boundaries retained. |
| review | [Retained finding](../audits/reviews/Yin_R_F0011_v1.md#fresh-adversarial-recheck-after-the-users-challenge) | Separately organized fresh-context whole-argument adversarial recheck with no inherited discussion/prior conclusions, no authoring/editing and both constructions checked. |

## Historical assessments


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

Review: [Exact material](../audits/reviews/Yin_R_F0011_v1.md).

Material covered by that review: [Exact material](Yin_C_F0023_v1.md).
