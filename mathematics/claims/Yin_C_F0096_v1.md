---
author: Yin
---

# All-positive-rate free Poisson and mixed semicircular rational L2 boundedness

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Rational L2 Boundedness for Free Poisson and Semicircular Families

<a id="yin_c_f0096"></a>
Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Goal: [Yin_T_F0004](../tasks/Yin_T_F0004_v1.md).
Strategy: [Yin_S_F0014](../strategies/Yin_S_F0014.md).
Initial assessment: complete candidate proof, awaiting independent review.
No historical novelty claim is made.
The [selected assessment](#current-assessment) records the mathematical and review assessments.

## Statement

Let \(X_1,\ldots,X_d\) be a finite free selfadjoint family in a finite faithful tracial von Neumann algebra \(\mathcal M=W^*(X)\).
Suppose each coordinate is either a semicircular element of positive variance, or a free-Poisson element of arbitrary positive real rate and positive jump size.
Put

\[
\mathcal A_X=\mathbb C\langle X_1,\ldots,X_d\rangle,
\qquad F_X=\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X.
\]

Then

\[
\boxed{F_X\cap L^2(\mathcal M)\subseteq C^*(X_1,\ldots,X_d).}
\tag{1}
\]

Consequently, for every \(f\in F_X\) and \(\lambda\in\mathbb C\),

\[
\lambda\notin\sigma(f)
\quad\Longleftrightarrow\quad
f-\lambda\text{ has an affiliated inverse in }L^2(\mathcal M).
\tag{2}
\]

The spectrum of an unbounded affiliated \(f\) uses its canonical closed realization, with bounded everywhere defined resolvent inverse.
Rates below one are included; \(F_X\) is not asserted to be a division ring in that case.
The existence of the inverse in (2) is part of the condition.

Any bounded tuple of affiliated rational functions in such a family inherits the weaker conclusion that its rational L2 elements are bounded, and hence (2), by the division-closure inclusion argument already recorded for [rational images](../ledger/Yin_L_F0023_v1.md#4-direct-positive-families-for-the-all-rational-inverse-criterion).
In particular this includes circular coordinates, polynomial images, and finite sums of freely independent free-Poisson variables with different jumps.
The latter cover free compound-Poisson laws with finite real jump support, and their sums with semicircular components, by the usual free-cumulant addition rule; negative jumps are obtained by signed scalar polynomial images of the positive-jump coordinates in the statement.
These consequences concern the L2 resolvent criterion; they do not identify the spectrum with a creation-operator model or compute a Brown measure.

## Inputs, provenance and the decisive scope change

The [Yan25 source audit](../audits/literature/Yan25/Yin_U001.md#yan25-fock-interface) supplies the tracial Fock realization, its orthonormal polynomial vectors and the normal-order formula.
[Yin_C_F0015](Yin_C_F0015_v1.md#yin_c_f0015) supplies the finite-residual/subexponential-norm implication.
[Yin_C_F0034](Yin_C_F0034_v1.md#yin_c_f0034) supplies the precise finite-defect closure direction for arbitrary bounded right annihilators.
The initial discovery traced this calculation through Sections 3-4 of Yin_C_F0013, but the registered shared lemma already isolates its weaker hypotheses and is the actual proof dependency used below.
No full Yin_C_F0013 theorem is invoked with weakened assumptions, and no new shared lemma is extracted here.

The first exploration proposed bounded normalized duals for rates greater than one.
That restriction disappears in the current proof: right annihilators themselves have finite-rank generator commutators for every rate, and the necessary finite-defect closure direction needs no normalization, maximal \(\Delta\), conjugate variables or division-ring property.
Its correction on the polynomial core is algebraically invertible even when its Hilbert-space inverse is unbounded or nonexistent.
The complete current proof is below; no theorem was promoted from the initial narrower checkpoint.

<a id="yin_c_f0096-proof"></a>
## Proof

### 1. Normalize and realize the family

Independent nonzero affine changes of the listed selfadjoint generators preserve \(\mathcal A_X\), \(F_X\) and \(C^*(X)\).
We therefore use the normalized Fock realization

\[
X_i=\ell_i+\ell_i^*+a_i\ell_i\ell_i^*,
\qquad a_i\ge0,
\tag{3}
\]

where \(a_i=0\) denotes a standard semicircular coordinate.
For a free-Poisson coordinate of rate \(\lambda_i>0\), \(a_i=\lambda_i^{-1/2}\) and the original jump-one variable is \(a_i^{-1}X_i+a_i^{-2}\).
There is no bound \(a_i<1\) in the argument.

By Yan25's checked specialization, the vacuum state is a faithful normal trace on the generated algebra, and its full Fock space is the canonical \(L^2(\mathcal M)\).
If \(w\) is a word, write \(e_w\) for its orthonormal Fock vector, \(w^{\rm rev}\) for reversal, and \(W_w\in\mathcal A_X\) for its Wick polynomial.
Then \(W_w\Omega=e_w\), \(W_w^*=W_{w^{\rm rev}}\), and \(W_\varnothing=1\).
Equality of the bounded joint star-distributions identifies this model with any faithful tracial realization in the statement.

### 2. A homogeneous norm bound with the correct coefficient norm

The source's normal ordering reads

\[
W_w=\sum_{w=pq}\ell_p\ell_{q^{\rm rev}}^*
+\sum_{w=p i q}a_i\ell_{p i}\ell_{q^{\rm rev}i}^*.
\tag{4}
\]

Fix degree \(n\), coefficients \(\alpha_w\), and a cut length \(|p|=k\).
In the first sum, the operators \(\ell_p\) for fixed \(k\) have mutually orthogonal ranges, as do \(\ell_{q^{\rm rev}}\) for fixed \(n-k\).
Hence that cut's operator norm is at most the Hilbert--Schmidt norm of its finite coefficient matrix, namely \((\sum_{|w|=n}|\alpha_w|^2)^{1/2}\).
This is the matrix between the two orthogonal prefix decompositions, tensored with the identity on the remaining Fock tail; the same argument covers an empty prefix.

For a cut in the second sum, its left words \(pi\) all have length \(k+1\), and its right words \(q^{\rm rev}i\) all have length \(n-k\).
Its coefficient matrix has one entry \(a_i\alpha_{piq}\) for each word, in distinct positions.
Thus its norm is at most \(a_* (\sum|\alpha_w|^2)^{1/2}\), where \(a_*=\max_i a_i<\infty\).
Summing the \(n+1\) ordinary and \(n\) preservation cuts gives

\[
\left\|\sum_{|w|=n}\alpha_w W_w\right\|
\le (n+1+n a_*)
\left(\sum_{|w|=n}|\alpha_w|^2\right)^{1/2}.
\tag{5}
\]

The growth factor in (5) is subexponential for every finite parameter tuple.
This is a scalar Hilbert-space estimate derived from (4), not an unsupported replacement of the input norm in Yan25 Corollary 3.14.

### 3. Polynomial commutators and coefficient residuals

Let \(R_i=r_i^*\) be right annihilation and \(P=P_\Omega\).
Define \(K_i=I+a_iR_i\).
Left and right annihilators commute, and

\[
[R_i,\ell_p]=
\begin{cases}\ell_{p'}P,&p=p'i,\\0,&\text{otherwise}.
\end{cases}
\]

Applying this to (4) gives the exact cut identity

\[
[R_i,W_w]=H_i^{(w)}K_i,
\qquad
H_i^{(w)}e_v=
\begin{cases}e_u,&w=uiv^{\rm rev},\\0,&\text{otherwise}.
\end{cases}
\tag{6}
\]

Indeed the ordinary cuts give \(\sum_{w=p i q}\ell_pP\ell_{q^{\rm rev}}^*\); the preservation cuts give \(a_i\sum_{w=p i q}\ell_pP\ell_{q^{\rm rev}i}^*\), which is the first operator followed by \(a_iR_i\).
In particular

\[
[R_i,X_j]=\delta_{ij}P K_i
\tag{7}
\]

has finite rank for every parameter, although it need not be a normalized dual relation.

### 4. Apply the existing finite-defect closure lemma

Apply [Yin_C_F0034](Yin_C_F0034_v1.md#yin_c_f0034), items 2-4, with the dense left modules \(\mathcal E=V_i=H=L^2(\mathcal M)\) and \(D_{i,0}=R_i\).
These operators and their adjoints are bounded and everywhere defined, so all its module and adjoint hypotheses hold.
It requires only finite-rank generator commutators, supplied by (7), and imposes no normalized dual relation, normality or maximal-Delta hypothesis.

For bounded fractions \(u=s^{-1}b=ct^{-1}\), its defects are the bounded operators

\[
\delta_i(u;s,b,c,t)=sR_ic-bR_it.
\tag{8}
\]

Yin_C_F0034 makes finite rank of (8) independent of fractions and proves that the elements satisfying it form an inverse-closed unital subalgebra of \(L^0(\mathcal M)\).
Consequently

\[
F_X\subseteq\{u:\text{every defect (8) has finite rank}\}.
\tag{9}
\]

For bounded \(u\in F_X\), choose \(s=t=1\), \(b=c=u\), and obtain exactly

\[
u\in F_X\cap\mathcal M\quad\Longrightarrow\quad
[R_i,u]\text{ has finite rank for every }i.
\tag{10}
\]

This is a direct application of Yin_C_F0034's accepted statement.
No assertion that \(F_X\) is a division ring is used.
The earlier full Yin_C_F0013 theorem is not invoked with weakened hypotheses.

### 5. The affiliated L2 residual bridge

Fix \(f\in F_X\cap L^2(\mathcal M)\).
Since the generators are selfadjoint, \(F_X\) is star closed even if it has zero divisors.
The standard rational regularizers

\[
b=(1+ff^*)^{-1},\qquad c=bf
\tag{11}
\]

belong to \(F_X\cap\mathcal M\), with \(b\) injective.
In particular (10) gives bounded finite-rank \([R_i,b]\), \([R_i,c]\).
On the algebraic polynomial core \(\mathcal H_{\rm alg}=\operatorname{span}\{e_v\}\), the products \(f\xi\) and \(fR_i\xi\) are defined: right multiplication by each fixed Wick polynomial preserves L2, and \(R_i\) preserves the core.
The identity

\[
b[R_i,f]\xi=[R_i,c]\xi-[R_i,b]f\xi
\qquad(\xi\in\mathcal H_{\rm alg})
\tag{12}
\]

shows that \([R_i,f]\) has finite-dimensional range on this core, because the right side lies in the sum of two fixed finite-dimensional spaces and \(b\) is injective.
No boundedness or global extension of this unregularized commutator is assumed.

Expand \(f\Omega=\sum_w\alpha_we_w\), and let \(f_N=\sum_{|w|\le N}\alpha_wW_w\).
For each fixed core vector \(e_v=W_v\Omega\),

\[
\|(f_N-f)W_v\|_2\le\|W_v\|\,\|f_N-f\|_2\longrightarrow0,
\]

and the same holds with the fixed polynomial vector \(R_i e_v\).
Thus (6) passes column by column to

\[
[R_i,f]\big|_{\mathcal H_{\rm alg}}=H_i K_i,
\qquad
H_i e_v=\sum_u\alpha_{uiv^{\rm rev}}e_u.
\tag{13}
\]

The coefficient restrictions defining \(H_i e_v\) are L2 contractions, so they converge in this passage.
Although \(K_i^{-1}\) need not be bounded on the full Hilbert space, it **is** an inverse on the algebraic core:

\[
K_i^{-1}\xi=\sum_{r=0}^{N}(-a_iR_i)^r\xi,
\quad \xi\text{ supported on words of length at most }N.
\tag{14}
\]

Both inverse identities follow by telescoping because \(R_i^{N+1}\xi=0\).
Equations (12)-(14) imply \(H_i=[R_i,f]K_i^{-1}\) has finite-dimensional range on the core for **every** \(a_i\ge0\).
Adding \(f\Omega\) to the finitely many ranges \(\operatorname{ran}H_i\) contains every right coefficient residual \(\sum_u\alpha_{uv}e_u\), including the empty suffix.
The coefficient residual space is therefore finite dimensional.

### 6. Conclude boundedness and the resolvent criterion

The orthonormal polynomial basis, (5), and the finite residual space satisfy all hypotheses of Yin_C_F0015.
Hence the homogeneous expansion of \(f\) converges absolutely in operator norm, and its norm sum equals its canonical affiliated realization.
Each partial sum is a polynomial in \(X\), proving (1).

If \((f-\lambda)^{-1}\) exists affiliated and lies in L2, it is in \(F_X\) by inverse closure and hence bounded by (1).
Conversely a bounded resolvent inverse belongs to \(\mathcal M\subseteq L^2(\mathcal M)\).
This proves (2).
Finally a bounded rational-image tuple generates an affiliated division closure contained in the original \(F_X\); its L2 elements are L2 in the larger algebra and bounded by (1), then belong to the smaller algebra by affiliation.
This proves the stated inheritance.
QED.

<a id="yin_c_f0096-review"></a>
## Review scope and remaining boundaries

The author's all-word checks used the exact normal-order formula to derive (6), rather than inferring it from finite data.
The decisive audit points are that (10) needs only bounded finite-rank generator commutators; (12) is asserted only on the polynomial core; and (14) is a finite algebraic inverse, so no threshold \(a_i<1\) is required.
The L2 norm in (5) is justified by orthogonal fixed-length creation ranges.
These arguments do not assume maximal \(\Delta\), which indeed fails in examples with free-Poisson atoms.

The [exact word computation](../computations/programs/Yin_J_F0005/readme.md#retained-mathematical-account) independently compares the recursion and normal ordering in 1,953 finite columns and checks 3,906 commutator columns, with no intermediate truncation.
Its finite scope does not prove the analytic argument.
At the initial candidate checkpoint, a separate review of this complete candidate chain remained pending.

This proof establishes rational L2 boundedness and the pointwise L2 resolvent criterion.
It does not reconstruct a bounded scalar rational expression in the listed generators, nor prove equality of affiliated bounded intersection with bounded division closure.
The full-spectrum creation comparison for general R-diagonal tuples and Brown-support formulas remain separate results.
General multivariate free-Meixner laws beyond these finite free-Poisson/semicircular constructions, and general q-Gaussian rational L2 boundedness, are not claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:05 |
| status | proved |
| reason | Adopt the exact actual original finding and disclosed unknown initial-context relationship, preserving the mathematical assessment, fixed statement and argument, dependencies and historical decisions. No new review or mathematical proof version is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0096-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0110_v1.md#verification-facts-and-limits) | Complete six-section C_F0096 theorem for every positive real free-Poisson rate mixed with semicircular coordinates, rational-image consequences and exact Fock/fraction/residual source interfaces. Actual original finding with unknown initial-context arrangement; historical date and accepted-input depth unchanged. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0096-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0110_v1.md#current-isolated-finding) | Complete six-section C_F0096 theorem for every positive real free-Poisson rate mixed with semicircular coordinates, rational-image consequences and exact Fock/fraction/residual source interfaces. |

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

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0096-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0110_v1.md#verification-facts-and-limits) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0110_v1.md#verification-facts-and-limits).

Material covered by that review: [Exact material](Yin_C_F0096_v1.md).
