---
author: Yin
---

# Compatible nondense local dual tests give an aggregate rationality criterion

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Compatible Nondense Dual Tests and Aggregate Finite Rank

<a id="statement"></a>
<a id="yin_c_f0110"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: root.
Record kind: a concrete Q4 continuation for [Yin_T_F0005](../tasks/Yin_T_F0005_v1.md#yin_t_f0005).
Initial assessment: complete candidate argument, pending independent review.

The local test spaces below may all be nondense.
Cross-adjoint compatibility and collective totality assemble an actual densely defined dual, so [Yin_C_F0029](Yin_C_F0029_v1.md#yin_c_f0029) applies.
This is an explicit replacement for density of each individual test space; it retains aggregate Hilbert density.
It neither removes aggregate separation nor settles the different polynomial-core question Q3.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0110** after [complete independent review](../audits/reviews/Yin_R_F0120_v1.md#4-outcome-and-verification-limits).
The cross-compatible local-family criterion and mixed-rank characterization are proved, including the proper-window and shortcut-obstruction examples.
This supersedes the initial pending assessment.
Aggregate Hilbert density is retained; no result on non-total factor tests or the bare polynomial-core converse is claimed.

## 1. Reuse and exact setting

The inputs inspected before this deduction were Yin_C_F0029's exact domain and fraction criterion, [Yin_C_F0031](Yin_C_F0031_v1.md#yin_c_f0031), and the density obstruction in [Yin_C_F0084](Yin_C_F0084_v1.md#yin_c_f0084).
Yin_C_F0029 already supplies all affiliated-algebra and normal-coordinate arguments.
The remaining assembly is proved by elementary Hilbert-space pairings and finite-dimensional separation below; no new external theorem or source-priority claim is needed.

Let \(H=L^2(M,\tau)\), with faithful normal probability trace, \(\Omega=1\), \(P=P_\Omega\), and inner product linear in its second argument.
Let the bounded normal tuple \(X=(X_1,\ldots,X_d)\) generate \(M\).
Put
\[
 A_X=\mathbb C\langle X_1,\ldots,X_d\rangle,\qquad
 F_X=\operatorname{Div}_{L^0(M)}A_X.
\]
Adjoints are not adjoined to this algebra.

Let \(E_\alpha\subset H\) be complex-linear left \(M\)-modules, and, for each \(i\), let \(V_{i,\beta}\subset H\) be another family of such modules.
Neither family is assumed directed; its members need not be closed or contain bounded vectors.
Assume only collective totality:
\[
 \overline{\sum_\alpha E_\alpha}=H,\qquad
 \overline{\sum_\beta V_{i,\beta}}=H \quad(1\le i\le d).
 \tag{1}
\]
Sums mean algebraic finite sums.
Suppose there are complex-linear maps
\[
 D_{i,\alpha}:E_\alpha\longrightarrow H,\qquad
 S_{i,\beta}:V_{i,\beta}\longrightarrow H
\]
satisfying, for every choice of indices and vectors,
\[
 \langle p,D_{i,\alpha}z\rangle
   =\langle S_{i,\beta}p,z\rangle,
 \qquad p\in V_{i,\beta},\ z\in E_\alpha,
 \tag{2}
\]
and
\[
 D_{i,\alpha}(X_jz)-X_jD_{i,\alpha}z
       =\delta_{ij}\langle\Omega,z\rangle\Omega.
 \tag{3}
\]
Every composition in (3) exists by left-module invariance.
The \(S_{i,\beta}\) are explicitly supplied companion maps, not an assumed single-valued Hilbert adjoint of a nondensely defined operator.

## 2. Cross-pairing assembles actual operators and adjoints

Set \(E=\sum_\alpha E_\alpha\) and \(V_i=\sum_\beta V_{i,\beta}\).
Define
\[
 D_{i,0}\Big(\sum_{\alpha\in A_0}z_\alpha\Big)
       =\sum_{\alpha\in A_0}D_{i,\alpha}z_\alpha.
 \tag{4}
\]
If the sum of the \(z_\alpha\) is zero, pairing the proposed value against any \(p\in V_{i,\beta}\) and using (2) gives zero.
Totality of \(V_i\) makes the proposed value zero.
Thus (4) is independent of every finite decomposition, not merely consistent on pairwise intersections.

The same argument, pairing against the total family \(E_\alpha\), shows that
\[
 S_{i,0}\Big(\sum_\beta p_\beta\Big)
       =\sum_\beta S_{i,\beta}p_\beta
\]
is well defined on \(V_i\).
Equation (2) extends by finite sums to
\[
 \langle p,D_{i,0}z\rangle=\langle S_{i,0}p,z\rangle
 \quad(p\in V_i,\ z\in E).
 \tag{5}
\]
Because \(E\) is dense, this is precisely \(V_i\subset\operatorname{Dom}D_{i,0}^*\) and \(D_{i,0}^*|_{V_i}=S_{i,0}\).
In particular \(D_{i,0}\) is closable.
The module properties and (3) pass to finite sums.

All exact hypotheses of Yin_C_F0029 now hold for \(E,V_i,D_{i,0}\).
Consequently \(\Delta(X)=d\), the affiliated division algebra is the embedded free field, and the complete Yin_C_F0029 fraction criterion applies.
This step reuses that result; it does not reproduce its substantial normality, projection-window or tensor arguments.

## 3. A criterion using only mixed local test matrices

Fix \(u\in L^0(M)\) and any bounded fractions
\[
 u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,\quad s,t\text{ regular}.
 \tag{6}
\]
For \(z\in E_\alpha\) the local cleared defect is
\[
 T_{i,\alpha}z=sD_{i,\alpha}(bz)-aD_{i,\alpha}(tz).
 \tag{7}
\]
It is the restriction of the global defect \(T_{i,0}=sD_{i,0}b-aD_{i,0}t\).
Its pairing against \(p\in V_{i,\beta}\) can be read entirely from local companion data:
\[
 \gamma_i(p,z)
 =\langle S_{i,\beta}(s^*p),bz\rangle
  -\langle S_{i,\beta}(a^*p),tz\rangle
 =\langle p,T_{i,\alpha}z\rangle.
 \tag{8}
\]
The vectors \(s^*p,a^*p\) lie in the same test module.

Then \(u\in F_X\) if and only if, for every \(i\), there is a finite integer \(r_i\) such that every mixed rectangular matrix
\[
 \bigl(\gamma_i(p_k,z_\ell)\bigr)_{1\le k\le m,\ 1\le\ell\le n}
 \tag{9}
\]
has rank at most \(r_i\), where each row and each column may use a different local module.
The bound is uniform over the lengths, vectors and all local indices.
The criterion holds for some, equivalently every, fraction pair (6).

To prove the rank assertion, suppose \(\operatorname{ran}T_{i,0}\) has dimension at least \(r_i+1\).
Its range is spanned by images of vectors drawn individually from the \(E_\alpha\), so choose \(r_i+1\) independent such images \(y_\ell=T_{i,\alpha_\ell}z_\ell\).
Pairings by the union of \(V_{i,\beta}\) separate their finite-dimensional span: a vector annihilated by that union is annihilated by its dense span and is zero.
These functionals therefore span the full finite-dimensional dual.
Select \(r_i+1\) individual test vectors giving an invertible pairing matrix.
This contradicts (9).
Conversely a rank-\(r_i\) operator gives rank at most \(r_i\) in every such matrix.

This proves that (9) is equivalent to finite algebraic rank of the assembled cleared defect.
Yin_C_F0029 gives exactly the claimed rationality equivalence, independence of fractions, and unique bounded finite-rank extension.
No separate uniform operator-norm estimate on local defects is assumed.

For completeness, boundedness here is legitimate: for \(p\in V_i\), the adjoint witness for \(T_{i,0}\) is
\[
 b^*D_{i,0}^*(s^*p)-t^*D_{i,0}^*(a^*p)\in H.
\]
Thus \(T_{i,0}\) is closable on dense \(E\); the accepted closable finite-rank result Yin_C_F0031 gives its bounded extension.
An arbitrary algebraically finite-rank form without this compatibility has no such automatic conclusion.

For bounded \(f\in M\), set \(s=t=1\) and \(a=b=f\).
Formula (8) becomes
\[
 \gamma_i^f(p,z)
 =\langle S_{i,\beta}p,fz\rangle
   -\langle S_{i,\beta}(f^*p),z\rangle
 =\langle p,[D_{i,\alpha},f]z\rangle.
 \tag{10}
\]
Thus \(f\in F_X\cap M\) exactly when all mixed matrices from (10) have uniform finite rank.
Yin_C_F0029 also gives invariance of every assembled closed domain and the corresponding bounded finite-rank commutators there.

## 4. Proper windows with a proper dense aggregate

There are actual dual systems satisfying these hypotheses with every individual domain nondense and their aggregate missing the vacuum.
Start with one standard semicircular variable \(S\), its abelian algebra \(M=W^*(S)\), and its bounded canonical normalized dual \(D\).
This is the accepted \(q=0,d=1\) specialization of [Yin_C_F0023](Yin_C_F0023_v1.md#yin_c_f0023).

Choose pairwise orthogonal spectral projections \(e_n\ne0\) with \(\sum_{n\ge1}e_n=1\) strongly, and no finite partial sum equal to \(1\).
Such projections are obtained by partitioning the nonatomic semicircular probability interval into measurable sets of positive measure.
Set
\[
 E_n=V_n=M e_n,\qquad D_n=D|_{M e_n},\qquad S_n=D^*|_{M e_n}.
 \tag{11}
\]
They are left modules and (2)-(3) hold by restriction.
Each \(M e_n\) has closure \(H e_n\ne H\).
The aggregate \(\sum_n M e_n\) is dense, since bounded vectors multiplied by finite partial sums converge in \(L^2\).
It does not contain \(\Omega\): every aggregate vector has right support below a finite partial sum, whereas \(\Omega\) has right support \(1\).

This is a genuine family of proper local domains and a proper aggregate domain, not a finite decomposition whose algebraic sum already equals \(M\).
The proof of Sections 2-3 does not assume a bounded reference dual; the reference is used only to demonstrate that the hypotheses are realizable.

## 5. Why the mixed and compatibility clauses matter

Individual rank bounds are insufficient.
In the same orthogonal-window Hilbert decomposition choose unit vectors \(h_n\in H e_n\), and let \(Q\) be the bounded orthogonal projection onto the closed span of all \(h_n\).
The restriction of \(Q\) to \(M e_n\) has rank at most one, with norm at most one, while \(Q\) has infinite rank on the aggregate dense domain.
Choosing \(h_n=e_n/\sqrt{\tau(e_n)}\) makes these rank-one restrictions nonzero and gives mixed identity matrices of every size.
This is an obstruction to the rank-inference shortcut, not a counterexample involving a rationality defect of an actual dual.

Agreement only on pairwise intersections is likewise insufficient to assemble linear maps.
On three distinct lines spanned by \(e_1,e_2,e_1+e_2\) in \(\mathbb C^2\), prescribe zero on the first two and a nonzero value at \(e_1+e_2\) on the third.
Every pairwise intersection is zero but the sum prescription is inconsistent.
Condition (2), together with totality, controls all finite linear relations and rules this out.
This is an elementary assembly example, not an operator-algebra counterexample to (1)-(3).

Finally, the procedure does not bypass Yin_C_F0084 by replacing aggregate density with large trace or a nonzero support.
Collective totality is exactly the separation used both to obtain an actual Hilbert adjoint and to detect every finite-dimensional range.
Whether one non-total, factor-specific test space can suffice under other structural hypotheses remains a separate question.

## 6. Author check and remaining scope

The author checked inner-product conjugations in (2), (8) and (10), independence from arbitrary finite decompositions, all left-module compositions, actual adjoint membership and closability, finite-dimensional separation for mixed matrices, both directions of the Yin_C_F0029 application, and the infinite proper-window example.
No approximation of local unbounded maps or assumption of a Hilbert adjoint on a nondense domain occurs.

This provides the compatible-family alternative requested in Q4.
It retains density of the assembled domain and does not solve Q1-Q3, remove collective separation, or establish a theorem for non-total factor-specific tests.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:49 |
| status | proved |
| reason | Adopt the exact original finding at its disclosed unknown initial-context relationship. Preserve the mathematical statement, status, selected proof, dependencies and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-cross-pairing-assembles-actual-operators-and-adjoints) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0120_v1.md#4-outcome-and-verification-limits) | Whole six-section compatible nondense local-test family theorem: cross-pairing assembly on finite sums, actual dense adjoints, aggregate finite rank via mixed matrices, proper-window and shortcut-obstruction examples. Aggregate Hilbert density and exact C_F0029 interfaces remain essential. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-cross-pairing-assembles-actual-operators-and-adjoints) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0120_v1.md#current-isolated-finding) | Whole six-section compatible nondense local-test family theorem: cross-pairing assembly on finite sums, actual dense adjoints, aggregate finite rank via mixed matrices, proper-window and shortcut-obstruction examples. Aggregate Hilbert density and exact C_F0029 interfaces remain essential. |

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
| argument | [Exact material](#2-cross-pairing-assembles-actual-operators-and-adjoints) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0120_v1.md#4-outcome-and-verification-limits) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0120_v1.md#4-outcome-and-verification-limits).

Material covered by that review: [Exact material](Yin_C_F0110_v1.md).
