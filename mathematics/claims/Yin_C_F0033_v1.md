---
author: Yin
---

# Local normal commutation and the fundamental defect identity

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Yin_C_F0033: Local Normal Commutation and the Cleared-Defect Identity

<a id="statement"></a>
<a id="yin_c_f0033"></a>

Role: lemma.
Role origin: agent-proposed; the user explicitly authorized this extraction.
Provenance: project deduction, extracted from the argument identified below.
Mathematical status at authorship: proof draft.
Review status at authorship: self-reviewed; independent review pending.
Current proof: candidate [yin_c_f0033-p1](#yin_c_f0033-p1), dated 2026-09-10.

### Extraction Provenance and Authorization

The source is [Yin_C_F0029, Sections 4 and 7](Yin_C_F0029_v1.md#yin_c_f0029), specifically the local commutation/module argument and the bounded fundamental identity preceding tensor descent.
The present statement assumes the cleared defects already have bounded finite-rank extensions.
It therefore does not repeat the separate extension, fraction-algebra, maximal-Delta, or division-ring descent arguments.
Yin_C_F0029 is extraction provenance, not a logical dependency of yin_c_f0033-p1.
The [batch authorization](../ledger/Yin_L_F0014_v1.md#authorization) covers this extraction and its intended uses.

### Statement and Scope

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, and put \(H=L^2(M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
Use the inner product linear in its second variable.
Let \(\mathcal E\subseteq H\) be a dense left \(M\)-module.
Let \(X_1,\ldots,X_d\in M\) be bounded normal elements generating \(M\) as a von Neumann algebra.
Suppose closable complex-linear maps \(D_i:\mathcal E\to H\), with domain exactly \(\mathcal E\), satisfy
\[
D_i(X_jz)-X_jD_i z=\delta_{ij}Pz
\quad(z\in\mathcal E).
\tag{33.1}
\]
There is no vacuum-domain or right-invariance hypothesis.
The only adjoint-domain requirement for this lemma is the dense adjoint domain implicit in closability.
In particular, a consumer may verify it by giving a dense left module \(V_i\subseteq\operatorname{Dom}D_i^*\), but this lemma needs no invariance or norm estimate for those adjoint test vectors.

Apply Yin_C_F0032 to the targets \(Y_j=X_j\), obtaining \(e_n,p_n\).
Put \(R_i=\rho(X_i)\), and define only on \(Mp_n\)
\[
K_nz=\sum_i\bigl(R_iD_i z-D_i(zX_i)\bigr),\qquad
C_nz=K_nz+Pz.
\tag{33.2}
\]
Then every term is defined, \(C_n\) is bounded from operator norm to Hilbert norm, and
\[
C_n(az)=aC_nz
\quad(a\in M,\ z\in Mp_n).
\tag{33.3}
\]

Let \(s,a,b,t\in M\) satisfy \(sb=at\).
Suppose bounded finite-rank operators \(T_i\in B(H)\) satisfy
\[
T_i z=sD_i(bz)-aD_i(tz)
\quad(z\in\mathcal E).
\tag{33.4}
\]
Then the bounded operator identity
\[
\boxed{\ \sum_{i=1}^d[R_i,T_i]=aPt-sPb\ }
\quad\text{holds on }H.
\tag{33.5}
\]
Regularity of \(s,t\), or existence of an affiliated fraction represented by them, is not needed for this identity.
In a fraction application, the equality \(sb=at\) is the exact coefficient condition to check.
Finiteness of the ranks is assumed for the intended downstream applications; the proof of (33.5) itself uses only boundedness of the \(T_i\).

The lemma does not assert that (33.4) has bounded extensions under its other hypotheses, nor that arbitrary finite-rank expressions are closable.
It also does not prove maximal Delta or affiliated rationality.
Those are separate interfaces.

### Proof Dependencies of yin_c_f0033-p1

The only direct project-claim dependency is [Yin_C_F0032, proof yin_c_f0032-p1](Yin_C_F0032_v1.md#yin_c_f0032-p1).
Its hypotheses hold because the present \(\mathcal E\) is a dense left module, all \(X_j\) are bounded, and the \(D_i\) are closable.
Its conclusions supply the windows, density, local bounds, and bounded-set weak continuity used below.

The accepted analytic inputs in addition are Banach-valued holomorphy of norm-convergent exponential series, scalar Liouville applied through continuous linear functionals, normal functional calculus for exponentials, and Kaplansky density followed by norm approximation in \(C^*(X)\).
Generation of \(M\) verifies the last input's applicability.
No original-source re-audit is claimed here.

There is no dependency on Yin_C_F0031: bounded finite-rank representatives are explicit hypotheses.
There is no dependency on Yin_C_F0029's conclusion, any maximal-Delta theorem, or a free-field realization theorem.

<a id="yin_c_f0033-p1"></a>
### Proof yin_c_f0033-p1

Yin_C_F0032 gives \(Mp_nX_i\subseteq Me_n\subseteq\mathcal E\), so (33.2) is defined.
It also bounds each map \(z\mapsto D_i z\), \(z\mapsto D_i(zX_i)\), and \(z\mapsto(D_i z)X_i\) on \(Mp_n\) in the two indicated norms.
Therefore \(C_n\) is bounded and has bounded-set weak continuity on that window.

Fix \(z\in Mp_n\) and a coordinate \(X_j\).
Both \(X_jz\) and \(z\) lie in the window; the inputs \(zX_i\) and \(X_j(zX_i)\) belong to \(\mathcal E\).
Using (33.1) at \(z\) and \(zX_i\) gives
\[
\begin{aligned}
C_n(X_jz)-X_jC_nz
&=\sum_i\bigl((D_i(X_jz)-X_jD_i z)X_i\\
&\hspace{35mm}-(D_i(X_j(zX_i))-X_jD_i(zX_i))\bigr)
  +(PX_j-X_jP)z\\
&=(R_jP-PR_j)z+(PX_j-X_jP)z\\
&=0.
\end{aligned}
\tag{33.6}
\]
The last equality is traciality:
\[
(R_jP-PR_j)z=\tau(z)X_j-\tau(zX_j)\Omega
=(X_jP-PX_j)z.
\]
This calculation never asserts that \(D_i(zX_i)\) exists for every \(z\in\mathcal E\); it is performed only on \(Mp_n\).

Fix \(n,j\), write \(x=X_j\), and consider
\[
\mathcal L(\zeta)
=\lambda(e^{\zeta x^*})\,C_n\,\lambda(e^{-\zeta x^*}),
\qquad \zeta\in\mathbb C.
\tag{33.7}
\]
Left multiplication by every element of \(M\) preserves \(Mp_n\).
Consequently (33.7) is entire with values in \(B((Mp_n,\|\cdot\|),H)\).
Equation (33.6) and norm-convergent exponential series imply that \(C_n\) intertwines exponentials of \(x\).
Since \(x\) is normal,
\[
\mathcal L(\zeta)
=\lambda(e^{\zeta x^*-\bar\zeta x})\,C_n\,
 \lambda(e^{-\zeta x^*+\bar\zeta x}).
\tag{33.8}
\]
The exponents are skew-adjoint, so the two exponentials are unitary.
Their left actions are isometries on \(H\) and on \(Mp_n\) with its operator norm.
Thus \(\|\mathcal L(\zeta)\|\leq\|C_n\|\) uniformly.
Applying scalar Liouville through every continuous linear functional on the operator Banach space makes \(\mathcal L\) constant.
Differentiation at zero yields \([C_n,x^*]=0\).

It follows that \(C_n\) intertwines left multiplication by every starred polynomial in the \(X_j\).
For \(a\in M\), choose uniformly bounded starred polynomials \(a_\alpha\to a\) in \(L^2\).
For fixed \(z\in Mp_n\), \(a_\alpha z\) remains in that window, has uniformly bounded operator norm, and converges in \(L^2\) to \(az\).
The bounded-set weak continuity supplied by Yin_C_F0032 gives
\[
C_n(a_\alpha z)\rightharpoonup C_n(az).
\]
On the other side, \(a_\alpha C_nz\to aC_nz\) in \(H\).
To justify the latter convergence, first approximate the fixed vector \(C_nz\) by \(w\in M\).
Uniform boundedness controls the approximation error, while \(\|(a_\alpha-a)w\|_2\leq\|w\|\|a_\alpha-a\|_2\to0\).
Taking limits in \(C_n(a_\alpha z)=a_\alpha C_nz\) proves (33.3).
No expression \(C_n\Omega\) has been used.

For the cleared-defect identity, fix \(z\in Mp_n\).
Equation (32.1) gives \(zX_i\in\mathcal E\), so the value \(T_i(zX_i)\) can be replaced by (33.4).
Moreover \(bz,tz\in Mp_n\) by left invariance of the window.
Right multiplication commutes with the bounded left coefficients, so
\[
\begin{aligned}
\sum_i[R_i,T_i]z
&=sK_n(bz)-aK_n(tz)\\
&=sC_n(bz)-aC_n(tz)+(aPt-sPb)z\\
&=(aPt-sPb)z.
\end{aligned}
\]
The last line uses (33.3), since the two \(C_n\) terms are \((sb-at)C_nz=0\).
The first and last lines are bounded operators on \(H\).
They agree on every \(Mp_n\); Yin_C_F0032 supplies density of the union even without monotonicity.
This proves (33.5).

### Checks, Version, and Intended Consumers

Normality is used only in the bounded entire-function argument (33.8).
Generation of \(M\) is used only when extending starred-polynomial commutation to all bounded left coefficients.
The local-domain and defect calculations require neither a vacuum input nor right invariance of the original domain.
In the specialization \(s=t=1\), \(a=b=f\), equation (33.5) reads
\[
\sum_i[R_i,T_i]=fP-Pf,
\]
which fixes the commutator sign.

The candidate yin_c_f0033-p1 is self-reviewed; peer review is pending.
The older review of the complete Yin_C_F0029 argument is provenance evidence, not automatic certification of this extracted statement or its Yin_C_F0032 invocation.

Intended future consumers are lemma-based proof versions of Yin_C_F0029, Yin_C_F0024, and Yin_C_F0030.
For Yin_C_F0029, the domain hypotheses supply closability, and a separate extension lemma supplies (33.4) when the cleared defects have finite rank.
For Yin_C_F0024 and Yin_C_F0030, \(\mathcal E=M\), so \(e_n=p_n=1\) may be used and the local module identity becomes a global one on \(M\).
The relevant fraction equality gives \(sb=at\) in each case.
Any tensor identification and division-ring descent after (33.5) remain separate proof steps.
These interfaces describe intended uses; no original proof or its historical dependency list is changed by this file.

The actual project dependency direction is yin_c_f0032-p1 to yin_c_f0033-p1.
A future parent proof may invoke these versions without a reverse dependency on the parent's conclusion.
The original complete Yin_C_F0029 artifact and its review remain intact.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.
Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0033-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0020_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:45 |
| status | proved |
| reason | Select the actual retained finding scopes and their known mathematical-development relationships, preserving status, authorized role, exact statement/proof/dependency selections and all historical decisions. No new mathematical review is asserted. |

Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0033-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0020_v1.md#local-normal-commutation-finding) | Actual original complete or auxiliary scope stated by that finding; unchanged versions and original source-depth/nonconclusion boundaries. |

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
Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0020_v1.md).

The original whole-source review covered the local test-space and normal-commutation lemmas, their extraction interfaces and proposed uses in the parent criterion.
The exact findings and their source-depth limits remain in the cited review.
