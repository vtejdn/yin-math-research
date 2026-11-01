---
author: Yin
---

# Bounded-inverse forward calculus and a two-core-estimate bridge

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Small-Core Forward Implications and an Analytic Extension Bridge

<a id="statement"></a>

<a id="yin_c_f0027"></a>
## Yin_C_F0027: Closed-Domain Inversion and the Core-Estimate Form of the Main Theorem

Date: 2026-09-10.
Authorization: the user requested that the full main theorem be reconsidered with duals initially defined only on the ACSY24 starred polynomial core.
Human author: Yin.
Proof development: another AI agent, at the request of the coordinating agent.
This module records two ingredients for the developing small-core package; the coordinating agent allocated Yin_C_F0027 after the initial draft.
It does not modify the hypotheses or recorded proof of [Yin_C_F0024](Yin_C_F0024_v1.md#yin_c_f0024).
The [complete review](../audits/reviews/Yin_R_F0016_v1.md) records the inspected version and outcome; the [selected assessment](#current-assessment) records the mathematical and review assessments.

## 1. Setting and the Two Supported Conclusions

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal probability trace, and put $H=L^2(M,\tau)$, $\Omega=1$, and $P=P_\Omega$.
Use the inner product linear in its second variable.
Let $X=(X_1,\ldots,X_d)$ be a finite bounded normal generating tuple, and distinguish
\[
A=\mathbb C\langle X\rangle,
\qquad \mathcal A=\mathbb C\langle X,X^*\rangle.
\]
The analytic core $\mathcal A$ is dense in $H$.
The holomorphic rational algebra below starts with $A$ and does not silently adjoin the generator adjoints.

Suppose $D_{i,0}:\mathcal A\to H$ are complex-linear closable operators satisfying
\[
[D_{i,0},X_j]=\delta_{ij}P
\quad\text{on }\mathcal A,
\qquad
[D_{i,0},X_j^*]\text{ has a bounded extension to }H.
\tag{1}
\]
Write $D_i=\overline{D_{i,0}}$.
The ACSY24 hypotheses imply these assumptions, with Hilbert-Schmidt extensions, and also give $\mathcal A\subseteq\operatorname{Dom}D_{i,0}^*$.
The latter inclusion will be required explicitly for the analytic bridge in Section 5.
The exact source interface and the regularization argument are recorded in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).

The first conclusion uses only (1): every element of $\operatorname{Rat}_M A$ preserves $\operatorname{Dom}D_i$ and has a bounded finite-rank commutator with $D_i$, for every $i$.
Here $\operatorname{Rat}_M A$ is the rational closure formed using matrix inverses that are bounded in matrix algebras over $M$.
In particular the conclusion holds for $\operatorname{Div}_M A$ and for every expression $uL(X)^{-1}v$ whose complete matrix inverse is bounded.

The second conclusion is a sufficient bridge to the full affiliated theorem.
For this conclusion only the core generator identity in (1), normality, and the following conditions are needed; bounded adjoint-generator commutators are not required:
\[
\mathcal A\subseteq\operatorname{Dom}D_{i,0}^*,
\qquad
\|D_{i,0}p\|_2\le c_i\|p\|,
\qquad
\|D_{i,0}^*p\|_2\le c_i'\|p\|
\quad(p\in\mathcal A),
\tag{2}
\]
with finite constants $c_i,c_i'$, then the actual closures satisfy
\[
M\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*.
\tag{3}
\]
Their generator identities hold on all of $M$, and Yin_C_F0024 applies to their restrictions to $M$.
Thus (2) supplies the full affiliated finite-defect equivalence, including all bounded fraction choices, rather than only the bounded matrix-inverse subcase.

Neither estimate in (2) is claimed to follow from the present general ACSY24 normal-tuple assumptions.
In particular, this module does not deduce the adjoint estimate from the first estimate.

## 2. Closed-Domain Commutators and Selfadjoint Doubling

Fix $i$ and write $D_0=D_{i,0}$ and $D=D_i$.
The product rule extends (1) to bounded commutators
\[
[D_0,a]=T_a\in B(H)\qquad(a\in\mathcal A)
\]
on the common core.
For $z\in\operatorname{Dom}D$, take $z_n\in\mathcal A$ with $z_n\to z$ and $D_0z_n\to Dz$ in $H$.
Then $az_n\to az$ and $D_0(az_n)=aD_0z_n+T_a z_n$ converges to $aDz+T_a z$.
Closedness therefore gives
\[
a\operatorname{Dom}D\subseteq\operatorname{Dom}D,
\qquad [D,a]=T_a\quad\text{on }\operatorname{Dom}D.
\tag{4}
\]
Applying this to $a^*$ and using adjoint pairing gives
\[
a\operatorname{Dom}D^*\subseteq\operatorname{Dom}D^*,
\qquad [D^*,a]=-T_{a^*}^*.
\tag{5}
\]
This step uses the closed operator's entire adjoint domain and does not require the polynomial core to be a core for that adjoint.

On $H\oplus H$, put
\[
S=\begin{pmatrix}0&D^*\\D&0\end{pmatrix},
\qquad
\operatorname{Dom}S=\operatorname{Dom}D\oplus\operatorname{Dom}D^*.
\]
The standard selfadjoint-doubling theorem makes $S$ selfadjoint.
For a bounded $a\in M$, write $\widetilde a=\operatorname{diag}(a,a)$.
Let $\mathcal L_S$ consist of those $a\in M$ for which $\widetilde a$ preserves $\operatorname{Dom}S$ and $[S,\widetilde a]$ has a bounded extension $C_a$.
Equations (4)-(5) show that $\mathcal A\subseteq\mathcal L_S$.
The product rule makes $\mathcal L_S$ a unital algebra.
Selfadjointness and adjoint pairing show that it is closed under adjoints, with $C_{a^*}=-C_a^*$.

For $t>0$, put
\[
R_t=(1+tS^2)^{-1},
\qquad S_t=SR_t,
\qquad B_t=\sqrt t\,SR_t.
\]
The resolvent calculation checked in ACSY24-U001 gives
\[
[S_t,\widetilde a]=R_t C_aR_t-B_t C_aB_t.
\tag{6}
\]
It follows directly from the commutator formula for $(S-z)^{-1}$ and the identity
\[
S_t=\frac{(S-i/\sqrt t)^{-1}+(S+i/\sqrt t)^{-1}}{2t}.
\]
Only invariance of $\operatorname{Dom}S$ is used, rather than unproved invariance of $\operatorname{Dom}S^2$.
Spectral calculus gives $R_t\to I$ strongly, $B_t\to0$ strongly, $\|R_t\|\le1$, and $\|B_t\|\le1/2$.
Hence for every $a\in\mathcal L_S$,
\[
[S_t,\widetilde a]\longrightarrow C_a
\quad\text{strongly},
\qquad
\sup_{t>0}\|[S_t,\widetilde a]\|\le\tfrac54\|C_a\|.
\tag{7}
\]

## 3. Bounded Inversion Preserves the Closed Domain

Suppose $a\in\mathcal L_S$ is invertible in $M$.
Every $S_t$ is bounded, so the ordinary inverse commutator formula gives
\[
[S_t,\widetilde a^{-1}]
=-\widetilde a^{-1}[S_t,\widetilde a]\widetilde a^{-1}.
\tag{8}
\]
For $\zeta\in\operatorname{Dom}S$, one has $S_t\zeta\to S\zeta$.
Equations (7)-(8) imply
\[
S_t\widetilde a^{-1}\zeta
\longrightarrow
\widetilde a^{-1}S\zeta
-\widetilde a^{-1}C_a\widetilde a^{-1}\zeta.
\tag{9}
\]
Meanwhile $R_t\widetilde a^{-1}\zeta\to\widetilde a^{-1}\zeta$ and $S(R_t\widetilde a^{-1}\zeta)=S_t\widetilde a^{-1}\zeta$.
Closedness of $S$ applies to this graph limit and proves
\[
\widetilde a^{-1}\operatorname{Dom}S\subseteq\operatorname{Dom}S,
\qquad
[S,\widetilde a^{-1}]
=-\widetilde a^{-1}C_a\widetilde a^{-1}.
\tag{10}
\]
Thus $\mathcal L_S$ is inverse closed in $M$.
This argument proves actual domain invariance rather than only a formal algebraic inverse rule.

The same proof applies after every finite matrix amplification.
For a matrix $L$ with entries in $\mathcal L_S$ and with bounded inverse in $M_n(M)$, its inverse preserves the amplified domains and satisfies the corresponding bounded matrix commutator formula.
Indeed the entrywise action of the bounded matrix preserves the direct-sum domain, its commutator matrix is bounded, and the preceding argument applies on $(H\oplus H)^n$.

## 4. Finite Rank for Bounded Rational Representations

Apply Sections 2-3 for every $i$.
Consider the elements of $\bigcap_i\mathcal L_{S_i}$ whose lower-left commutators $[D_i,f]$ have bounded finite-rank extensions for every $i$.
This is a unital algebra: products preserve the closed domains and obey the ordinary Leibniz formula there.
It contains the holomorphic polynomial algebra $A$ because the generator commutators are rank one.
For an element invertible in $M$, equation (10) gives
\[
[D_i,f^{-1}]=-f^{-1}[D_i,f]f^{-1},
\]
so bounded inversion preserves the finite-rank property.

The matrix statement is equally direct.
For a matrix $L$ whose entries belong to this algebra and whose inverse belongs to $M_n(M)$, write $D_i^{(n)}$ for the direct sum of $n$ copies of $D_i$.
Every entry of $[D_i^{(n)},L]$ is bounded finite rank, so this commutator is a bounded finite-rank operator on $H^n$.
The amplified inverse formula is
\[
[D_i^{(n)},L^{-1}]
=-L^{-1}[D_i^{(n)},L]L^{-1}.
\tag{11}
\]
It is bounded finite rank, and every entry of $L^{-1}$ preserves both of the required scalar closed domains.
Products and sums of these entries retain the same properties.
By the definition of rational closure, this proves
\[
f\in\operatorname{Rat}_M A
\quad\Longrightarrow\quad
f\operatorname{Dom}D_i\subseteq\operatorname{Dom}D_i,
\quad [D_i,f]\text{ has a bounded finite-rank extension}
\quad\text{for every }i.
\tag{12}
\]

In particular, if $f=uL(X)^{-1}v$ with scalar row and column vectors $u,v$ and the complete inverse bounded, then
\[
[D_i,f]=-uL(X)^{-1}[D_i^{(n)},L(X)]L(X)^{-1}v.
\tag{13}
\]
The usual affine linear representations in [MSY23-U003](../audits/literature/MSY23/Yin_U003.md#msy23-u003) preserve precisely this existing bounded-inverse assumption.
They are not used to infer boundedness of an entire matrix inverse from boundedness of its scalar compression.

For comparison with polynomial weak tests, suppose $\mathcal A\subseteq\operatorname{Dom}D_i^*$ and define, for bounded $f$,
\[
\beta_i^f(p,q)
=\langle D_i^*p,fq\rangle-\langle f^*p,D_iq\rangle,
\qquad p,q\in\mathcal A.
\tag{14}
\]
The finite-rank extension $T_i$ in (12) satisfies $\beta_i^f(p,q)=\langle p,T_iq\rangle$.
This follows from the actual domain invariance already proved.
No converse from the weak tests to full-domain invariance is asserted merely because $\mathcal A$ is a core for $D_i$.
Such a converse must also address the adjoint test domain, and $\mathcal A$ has not been shown to be a core for $D_i^*$.

## 5. The Two Core Estimates Restore the Entire Bounded Domain

Assume (2).
Fix $x\in M$ and $\varepsilon>0$.
Kaplansky density for the weakly dense star algebra, followed by norm approximation inside $C^*(X)$, supplies a net $p_\alpha\in\mathcal A$ with
\[
p_\alpha\longrightarrow x\text{ in }L^2,
\qquad \|p_\alpha\|\le\|x\|+\varepsilon.
\tag{15}
\]
The first estimate in (2) bounds $D_{i,0}p_\alpha$ in $H$.
Choose a weakly convergent subnet with limit $v$.
The pairs $(p_\alpha,D_{i,0}p_\alpha)$ then converge weakly in $H\oplus H$ to $(x,v)$.
The graph of the closed linear operator $D_i$ is a norm-closed linear subspace and hence weakly closed.
Consequently $x\in\operatorname{Dom}D_i$ and $D_i x=v$.

Apply the second estimate in (2) to the same bounded approximants and choose a weakly convergent subnet of their adjoint images.
The operator $D_{i,0}^*$ is already closed, and it equals $D_i^*$.
Weak closedness of its graph proves $x\in\operatorname{Dom}D_i^*$.
The weak lower semicontinuity of the Hilbert norm and then $\varepsilon\downarrow0$ give
\[
\|D_i x\|_2\le c_i\|x\|,
\qquad
\|D_i^*x\|_2\le c_i'\|x\|
\qquad(x\in M).
\tag{16}
\]
All values here are values of the actual Hilbert closure and its actual adjoint.
No arbitrary Banach-space extension from the polynomial algebra is selected.

If a uniformly operator-norm-bounded net $x_\alpha\in M$ converges to $x\in M$ in $L^2$, adjoint pairing first gives
\[
\langle\eta,D_i x_\alpha\rangle
=\langle D_i^*\eta,x_\alpha\rangle
\longrightarrow
\langle D_i^*\eta,x\rangle
\]
for $\eta\in\operatorname{Dom}D_i^*$.
This test domain is dense, and (16) bounds the images uniformly, so $D_i x_\alpha\rightharpoonup D_i x$ against every Hilbert test vector.
The same argument for $D_i^*|_M$ uses the dense domain of $D_i$ and proves its analogous bounded-set weak continuity.

Apply this continuity to the approximants in (15), to $X_jp_\alpha$, and to their core generator identity.
The limits give
\[
D_i(X_jx)-X_jD_i x=\delta_{ij}\tau(x)\Omega
\qquad(x\in M).
\tag{17}
\]
Thus the restrictions $D_i|_M$ satisfy every hypothesis of Yin_C_F0024.
Moreover $\mathcal A\subseteq M\subseteq\operatorname{Dom}D_i$ and $\mathcal A$ is a core for $D_i$ by definition, so the closure of $D_i|_M$ is the original $D_i$.
The bounded-element full-domain formulation supplied by Yin_C_F0024 consequently concerns precisely the operators used here.

Writing $F=\operatorname{Div}_{U(M)}A$, Yin_C_F0024 now gives for every $u\in U(M)$ and bounded fractions $u=s^{-1}a=bt^{-1}$ the equivalence
\[
u\in F
\quad\Longleftrightarrow\quad
z\longmapsto sD_i(bz)-aD_i(tz),\quad z\in M,
\text{ has finite rank for every }i.
\tag{18}
\]
The condition is independent of the bounded fraction choice, and its finite-rank defects have unique bounded extensions.
The remaining affiliated and bounded conclusions of Yin_C_F0024 transfer with their original scope.

## 6. Dependencies and the Remaining Forward Obligation

The bounded rational forward proof uses only closed-operator adjoints, selfadjoint doubling, resolvents, spectral calculus, and finite-rank algebra.
Normality of the coordinates is not needed in Sections 2-4 themselves.
Normality is retained in the setting because the full bridge invokes the normal-tuple Yin_C_F0024 theorem.
The analytic bridge additionally uses Kaplansky density and weak closedness of a closed operator graph.

For a selfadjoint tuple with L2 conjugate variables, [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002) supplies (2), with the sufficient constants $4\|\xi_i\|_2$ and $5\|\xi_i\|_2$ and its recorded one-variable reduction.
The primary proof of the contraction estimate uses both reality and coassociativity.
Those properties and estimates must not be transferred without verification to arbitrary derivations in the ACSY24 normal setting.
The ACSY24 adjoint formula contains the separate term $T_{i,p^*}^*\Omega$, so a bound for $D_{i,0}p$ alone has not been shown here to control $D_{i,0}^*p$.

The inclusion in (12) concerns bounded matrix-inverse representations.
It does not prove the forward implication for every bounded element of $\operatorname{Div}_{U(M)}A$ under (1) alone.
Such an element may be bounded even though intermediate inverses in its affiliated rational expression are unbounded.
The existing [Yin_C_F0012 example](Yin_C_F0012_v1.md#yin_c_f0012) prohibits replacing this issue by an assumption that every bounded affiliated rational output already has a bounded matrix-inverse representation over the original generators.
Indeed matrix algebras over $C^*(X)$ are inverse closed in matrix algebras over $M$, so such a representation would place its output in $C^*(X)$, contrary to that example.
Likewise, the present small core does not by itself let arbitrary bounded fraction coefficients act as inputs or adjoint tests for the defects in (18).

No counterexample to the full forward implication under the exact ACSY24 Hilbert-Schmidt hypotheses is asserted.
The unresolved obligation is either to prove an adequate analytic extension from those hypotheses or to establish the full affiliated rational forward implication directly with a justified smaller-domain defect formulation.
The two proved ingredients above do not settle that remaining step.

This module is a mathematical deduction rather than a numerical experiment or proof-assistant verification.
It retains the source foundations and previously recorded inspection limits and makes no historical-priority claim.

Revision, 2026-09-10: the coordinating agent allocated Yin_C_F0027 and clarified that the core-estimate bridge itself does not require the bounded adjoint-generator commutators used by the separate bounded-inversion argument.


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
| argument | [Exact material](#2-closed-domain-commutators-and-selfadjoint-doubling) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0016_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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
| argument | [Exact argument](#2-closed-domain-commutators-and-selfadjoint-doubling) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0016_v1.md#bounded-inversion-core-estimates-finding) | Complete bounded matrix-inverse domain calculus without normality, and separately the two-core-estimate bridge for normal tuples to the same actual all-M closures and complete affiliated criterion; no automatic bare-core estimates. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0016_v1.md).

Material covered by that review: [Exact material](Yin_C_F0027_v1.md).
