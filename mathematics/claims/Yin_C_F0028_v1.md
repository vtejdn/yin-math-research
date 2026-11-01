---
author: Yin
---

# One normal coordinate: weak and closed-domain criterion with exact rank

## Current assessment
[Selected decision](#decision-finding-owned-review)

## One Normal Coordinate with Duals Defined on a Polynomial Core

<a id="statement"></a>

<a id="yin_c_f0028"></a>
## Yin_C_F0028: Complete Coordinate Criterion under Bounded Starred Commutators

Date: 2026-09-10.
Human author: Yin.
Proof development: the coordinating agent, following the completed [Yin20 Chapters III-IV audit](../audits/literature/Yin20/readme.md) and the user's request to retry the small-core problem.
The claim is a project deduction combining the audited domain-preserving inversion mechanism, the spectral argument of [Yin_C_F0004](Yin_C_F0004_v1.md#yin_c_f0004), and the closed-domain calculus of [Yin_C_F0027](Yin_C_F0027_v1.md#yin_c_f0027).
It does not modify the earlier statements or assert historical novelty.
The [selected assessment](#current-assessment) records the mathematical and review assessments.

## 1. Setting and Statement

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal probability trace, $H=L^2(M,\tau)$, $\Omega=1$ and $P=P_\Omega$.
Use the inner product linear in its second variable.
Let $X=(X_1,\ldots,X_d)$ be a finite bounded normal generating tuple and put
\[
\mathcal A=\mathbb C\langle X,X^*\rangle\subset H.
\]
Suppose complex-linear $D_{i,0}:\mathcal A\to H$ satisfy
\[
\Omega\in\operatorname{Dom}D_{i,0}^*,\qquad
[D_{i,0},X_k]=\delta_{ik}P\quad\hbox{on }\mathcal A,
\tag{1}
\]
and every $[D_{i,0},X_k^*]$ on that core has a bounded extension to $H$.
Compactness and Hilbert-Schmidt membership of these extensions are not assumed.
Neither dual boundedness nor an all-$M$ domain inclusion nor vacuum normalization is assumed.
Section 2 proves closability and $\mathcal A\subseteq\operatorname{Dom}D_{i,0}^*$; write $D_i=\overline{D_{i,0}}$.

For $f\in M$, define
\[
\beta_i^f(p,q)=\langle D_{i,0}^*p,fq\rangle-
                 \langle f^*p,D_{i,0}q\rangle,
\qquad p,q\in\mathcal A.
\tag{2}
\]
A bounded finite-rank representative means an operator $T_i\in B(H)$ of finite rank with $\beta_i^f(p,q)=\langle p,T_iq\rangle$ on these tests.
This is stronger than algebraic finite rank of a possibly unbounded form.

Fix $j$ and assume $f\in N_j=W^*(X_j)$.
The following are equivalent:

1. The single form $\beta_j^f$ has a bounded finite-rank representative on the full core $\mathcal A$.
2. There are $p,q\in\mathbb C[z]$ such that $q$ has no zero on $\sigma(X_j)$ and $f=p(X_j)q(X_j)^{-1}$.
3. For every $i$, multiplication by $f$ preserves $\operatorname{Dom}D_i$, and $D_if-fD_i$ there extends to a bounded finite-rank operator on $H$.
4. Every $\beta_i^f$ has a bounded finite-rank representative.

In condition 3, the commutator is zero for $i\ne j$.
For nonconstant reduced $f=p(X_j)/q(X_j)$, the representative and the actual commutator for $i=j$ have rank
\[
\operatorname{rank}T_j=\max\{\deg p,\deg q\}.
\tag{3}
\]
Constants have rank zero, with zero represented by $p=0,q=1$.

When $d=1$, these conditions are also equivalent to
\[
f\in\mathcal F_X\cap M
 =\operatorname{Rat}_M\mathbb C[X]
 =\operatorname{Div}_M\mathbb C[X],
\qquad \mathcal F_X=\operatorname{Div}_{U(M)}\mathbb C[X].
\tag{4}
\]
The equality in (4) is asserted for one normal generator only.
No analogous intersection equality or bare-core converse for general jointly dependent $f$ is asserted.

## 2. Adjoint Domains and Absence of Spectral Atoms

The product rule on the invariant core gives a bounded extension $T_{i,a}$ of $[D_{i,0},a]$ for every $a\in\mathcal A$.
Applying the vacuum adjoint identity to $a^*q$ gives
\[
D_{i,0}^*a=aD_{i,0}^*\Omega-T_{i,a^*}^*\Omega.
\tag{5}
\]
The right side represents the adjoint functional on the whole core, so $a$ belongs to the adjoint domain.
Since $\mathcal A$ is dense, each $D_{i,0}$ is closable.

For completeness, atomlessness follows already under the bounded starred-commutator hypothesis.
Fix $j$, write $D=\overline{D_{j,0}}$, and let $B$ extend $[D_{j,0},X_j^*]$.
Bounded core commutators extend to the graph domain of $D$ by graph approximation.
Their adjoint identities then imply invariance of $\operatorname{Dom}D^*$ under both $X_j$ and $X_j^*$.
Thus on $H\oplus H$ the selfadjoint operator and bounded diagonal multiplier
\[
S=\begin{pmatrix}0&D^*\\D&0\end{pmatrix},
\qquad Z=\operatorname{diag}(X_j,X_j)
\]
satisfy the bounded domain commutator
\[
[S,Z]=C=\begin{pmatrix}0&-B^*\\P&0\end{pmatrix}.
\]
The bounded regularization identity proved in Yin_C_F0027, also used before any compactness assumption in Yin_C_F0025, is
\[
[SR_t,Z]=R_tCR_t-tSR_tCSR_t,
\qquad R_t=(1+tS^2)^{-1}.
\tag{6}
\]
The spectral theorem gives $R_t\to I$ strongly and $\sqrt t\,SR_t\to0$ strongly with norm at most $1/2$.
Equation (6) therefore converges strongly to $C$.
Its lower-left block says that the bounded operators
\[
V_t=D(1+tD^*D)^{-1}
\quad\hbox{satisfy}\quad [V_t,X_j]\longrightarrow P
\quad\hbox{strongly}.
\tag{7}
\]
Only boundedness of $B$ is used in this argument.

If $E=1_{\{\lambda\}}(X_j)\ne0$, put $\eta=E\Omega$ and $Q=|\eta\rangle\langle\eta|$.
Normality makes $\eta$ a joint eigenvector for $X_j$ and $X_j^*$, hence $QX_j=X_jQ$.
Trace cyclicity for a finite-rank operator and bounded operators gives
\[
\operatorname{Tr}(Q[V_t,X_j])=0.
\]
Taking the limit in the rank-one pairing using (7) gives
\[
0=\operatorname{Tr}(QP)=|\langle\Omega,E\Omega\rangle|^2=\tau(E)^2>0,
\]
a contradiction.
Thus every scalar spectral measure of a coordinate induced by $\tau$ is nonatomic.
This argument needs neither the full MSY23 free-field theorem nor compactness.

## 3. Weak Covariance Determines a One-Coordinate Kernel

Let condition 1 hold, with representative $T=T_j$.
Because $f$ commutes with $X_j$, the core relation and its adjoint give
\[
\beta_j^f(a,X_jb)-\beta_j^f(X_j^*a,b)
 =\langle a,(Pf-fP)b\rangle,
\qquad a,b\in\mathcal A.
\tag{8}
\]
Indeed $D_{j,0}X_jb=X_jD_{j,0}b+Pb$ and $D_{j,0}^*X_j^*a=X_j^*D_{j,0}^*a-Pa$.
Substituting these two identities into the left side leaves $\langle Pa,fb\rangle-\langle f^*a,Pb\rangle$, which is the displayed right side.
Every adjoint test remains in $\mathcal A$; no vector $fb$ is required to lie in $\operatorname{Dom}D_j$.
Density and boundedness imply
\[
TX_j-X_jT=Pf-fP.
\tag{9}
\]

Let $H_j=L^2(N_j,\tau)$ and let $Q_j:H\to H_j$ be its orthogonal projection.
The space $H_j$ is reducing for $X_j$, $f$ and their adjoints, and contains $\Omega$.
Compressing (9) gives the same equation on $H_j$ for the finite-rank $T'=Q_jT|_{H_j}$.
This compression is of a bounded representative, so it invokes no unproved assertion about compressions of closed unbounded duals or adjoint cores.

Identify $N_j=L^\infty(S_j,\mu_j)$, where $S_j=\sigma(X_j)=\operatorname{supp}\mu_j$ is compact and $\mu_j$ is nonatomic by Section 2.
A finite-rank operator on $L^2(\mu_j)$ has a separated kernel
\[
K(z,w)=\sum_{k=1}^{r}a_k(z)b_k(w),\qquad a_k,b_k\in L^2(\mu_j),
\quad r=\operatorname{rank}T'.
\]
Using a bilinear kernel convention, the conjugates representing the input functionals are included in $b_k$.
Equation (9) becomes
\[
(w-z)K(z,w)=f(w)-f(z).
\]
The diagonal has product measure zero, so
\[
K(z,w)=\frac{f(z)-f(w)}{z-w}
\quad\hbox{almost everywhere}.
\tag{10}
\]

The finite-column argument in Yin_C_F0004 Sections 3-4 now applies to this kernel without any boundedness assumption on the original dual.
Here is the decisive algebra.
For almost every $w$, the divided-difference column in (10) lies in $\operatorname{span}\{a_1,\ldots,a_r\}$.
If $r>0$, choose $r+1$ distinct such points $w_l$ and coefficients $c_l$, not all zero, giving a column relation.
Multiplication by $\prod_l(z-w_l)$ yields $b(z)f(z)=a(z)$ almost everywhere, where
\[
b(z)=\sum_l c_l\prod_{k\ne l}(z-w_k),\qquad
a(z)=\sum_l c_l f(w_l)\prod_{k\ne l}(z-w_k).
\]
At an index with $c_l\ne0$, $b(w_l)=c_l\prod_{k\ne l}(w_l-w_k)\ne0$, so $b$ is a nonzero polynomial.
Both degrees are at most $r$.
Its finite zero set is null, hence $f=a/b$ almost everywhere.
For $r=0$, (9) compressed gives $Pf=fP$, and application to $\Omega$ shows that $f$ is scalar.

## 4. Bounded Output Removes All Reduced Scalar Poles

Cancel the common factors to write the nonzero output as $p/q$ with coprime polynomials.
If $q(\lambda)=0$ for some $\lambda\in S_j$, then $p(\lambda)\ne0$.
In a sufficiently small punctured neighborhood of $\lambda$, $|p/q|$ exceeds any chosen essential bound for $f$.
That punctured neighborhood has positive $\mu_j$ measure because $\lambda$ is in its support and the singleton has measure zero.
This contradicts the equality $f=p/q$ almost everywhere and boundedness of $f$.
Thus $q$ has no zero on $S_j$.
Compactness gives $\inf_{S_j}|q|>0$, so $q(X_j)^{-1}\in N_j$ is bounded.
This proves condition 2 from condition 1.

This step uses cancellation of scalar polynomial factors in one complex variable.
It is not an inference from boundedness of an arbitrary compression of a multivariable inverse pencil.
The [Yin20 formal algorithm](../audits/literature/Yin20/Yin_U001.md#yin20-u001), with its repaired inverse sign, can now linearize this genuinely bounded-domain expression, producing a pencil whose entire inverse is bounded.

## 5. Forward Domains, All Coordinates and Exact Rank

Assume condition 2.
It is a finite expression formed from polynomials in the original tuple and a scalar inverse already bounded in $M$.
The hypotheses in (1) and the bounded starred commutators give exactly the closable-core setting of Yin_C_F0027.
Its closed-domain inverse calculus proves that $p(X_j)$, $q(X_j)^{-1}$ and their product preserve every $\operatorname{Dom}D_i$.
The actual commutator there has bounded extension
\[
[D_i,f]=[D_i,p(X_j)]q(X_j)^{-1}
 -f[D_i,q(X_j)]q(X_j)^{-1}.
\tag{11}
\]
Polynomial commutators are finite sums of bounded polynomial multipliers of $P$, so (11) has finite rank.
For $i\ne j$ both polynomial commutators are zero, giving the asserted vanishing.
This proves condition 3.

For $a,b\in\mathcal A$, condition 3 puts $fb$ in $\operatorname{Dom}D_i$ and the adjoint pairing identifies (2) with the bounded commutator in (11).
This proves condition 4, which implies condition 1.
The four-way equivalence is complete.

Every term of (11) for $i=j$ is supported on $H_j$ in both its output and input functional, because its rank-one factors are bounded functions of $X_j$ applied to $\Omega$.
Its unique weak representative therefore equals $Q_jT_jQ_j$, so its rank equals the compressed rank used in (10).
For reduced nonconstant $p/q$, the column argument gives $\max(\deg p,\deg q)\leq\operatorname{rank}T_j$.
Uniqueness of reduced fractions follows because a polynomial vanishing on a full-measure set for a nonatomic measure is zero.
For the reverse bound put $n=\max(\deg p,\deg q)$ and expand the polynomial
\[
\frac{p(z)q(w)-p(w)q(z)}{z-w}
 =\sum_{k=0}^{n-1}z^k b_k(w).
\]
Dividing by $q(z)q(w)$ gives at most $n$ separated bounded factors on the compact spectrum, hence rank at most $n$.
This proves (3) with precisely the same kernel argument as the reviewed Yin_C_F0004 refinement.

## 6. The Single-Generator Free Field and the Remaining General Problem

For $d=1$, atomlessness makes every nonzero polynomial in $X$ injective and invertible in $U(M)$.
The classical field $\mathbb C(z)$ therefore evaluates injectively by $p/q\mapsto p(X)q(X)^{-1}$.
Its image is a division subring containing $\mathbb C[X]$ and consists entirely of finite affiliated fractions, so it equals $\mathcal F_X$.
Every bounded element of that image has a reduced quotient whose denominator avoids $\sigma(X)$, by Section 4.
It consequently belongs to $\operatorname{Div}_M\mathbb C[X]$.
For the other inclusions, the same-ambient results audited in Yin20-U004 give
\[
\operatorname{Div}_M\mathbb C[X]
\subseteq\operatorname{Rat}_M\mathbb C[X]
\subseteq\operatorname{Rat}_{U(M)}\mathbb C[X]\cap M
=\mathcal F_X\cap M.
\]
The last equality uses the division-ring case of Proposition IV.5.7 inside $U(M)$: its division closure is the scalar field image just identified.
Together with the preceding inclusion $\mathcal F_X\cap M\subseteq\operatorname{Div}_M\mathbb C[X]$, this proves all the equalities.
This proves (4).

For a general tuple the theorem applies to bounded $f$ in any one coordinate algebra $W^*(X_j)$.
It makes no claim that an arbitrary jointly dependent element of $\mathcal F_X\cap M$ admits a one-variable reduced quotient.
The Yin_C_F0012 obstruction to general bounded inverse representations is unchanged.
The full Yin_S_F0011 converse for jointly dependent bounded affiliated rational elements, and a general affiliated criterion using arbitrary bounded denominators on a small core, remain unresolved.

The proof uses the exact closed-domain inversion theorem of Yin_C_F0027, the spectral-kernel argument of Yin_C_F0004 after establishing its weak-form interface, and elementary one-variable cancellation.
It neither imports Yin_C_F0025's compactness-based general converse machinery nor assumes that a weak test core is automatically a core for an adjoint.
Independent review must check the full artifact before promotion; no numerical experiment or formal proof-assistant verification is claimed.


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
| argument | [Exact material](#2-adjoint-domains-and-absence-of-spectral-atoms) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0017_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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
| argument | [Exact argument](#2-adjoint-domains-and-absence-of-spectral-atoms) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0017_v1.md#one-coordinate-small-core-finding) | Full one-normal-coordinate weak/rational/actual-domain equivalence, exact reduced rational-degree rank, off-coordinate zero commutators, scalar affiliated/rational closure equality and every stated limitation, including the final precision passages. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0017_v1.md).

Material covered by that review: [Exact material](Yin_C_F0028_v1.md).
