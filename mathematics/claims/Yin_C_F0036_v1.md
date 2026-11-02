---
author: Yin
---

# Bounded reference dual makes the adjoint module automatic on dense left modules

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Yin_C_F0036: A Bounded Reference Dual Makes the Adjoint Module Automatic

<a id="statement"></a>
<a id="yin_c_f0036"></a>

Provenance: project deduction, extending the all-\(\mathcal M\) comparison in Yin_C_F0030 Section 6 to arbitrary dense left modules.
Mathematical assessment at authorship: proof draft; complete candidate below.
Review assessment at authorship: self-reviewed; independent review pending.
Current candidate proof: [yin_c_f0036-p1](#yin_c_f0036-p1).

Let \((\mathcal M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, and put \(H=L^2(\mathcal M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
Use the inner product linear in its second variable.
Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of \(\mathcal M\).
Suppose there is a bounded reference dual system \(B_i\in B(H)\) satisfying \([B_i,X_j]=\delta_{ij}P\) on \(H\).
Let \(\mathcal E\subset H\) be any dense left \(\mathcal M\)-module, and let closable operators
\[
D_{i,0}:\mathcal E\longrightarrow H,
\qquad [D_{i,0},X_j]z=\delta_{ij}Pz\quad(z\in\mathcal E)
\tag{37.1}
\]
have domain exactly \(\mathcal E\).
No hypothesis on \(\operatorname{Dom}D_{i,0}^*\) other than the density implicit in closability is imposed.

Then, writing \(C_{i,0}=D_{i,0}-B_i|_{\mathcal E}\), one has:

1. \(C_{i,0}(az)=aC_{i,0}z\) for every \(a\in\mathcal M\), \(z\in\mathcal E\).
2. \(C_i=\overline{C_{i,0}}\) is a closed densely defined operator affiliated with the right commutant \(\lambda(\mathcal M)'\), and its adjoint domain is a dense left \(\mathcal M\)-module.
3. For the specified closure \(D_i=\overline{D_{i,0}}\),
   \[
   D_i=B_i+C_i,
   \qquad D_{i,0}^*=D_i^*=B_i^*+C_i^*,
   \qquad\operatorname{Dom}D_i^*=\operatorname{Dom}C_i^*.
   \tag{37.2}
   \]
   Thus the entire adjoint domain itself supplies the test module required in Yin_C_F0029.
4. For every bounded fraction pair \(u=s^{-1}a=bt^{-1}\) in \(L^0(\mathcal M)\),
   \[
   sD_{i,0}(bz)-aD_{i,0}(tz)
   =(sB_i b-aB_i t)z\qquad(z\in\mathcal E).
   \tag{37.3}
   \]
   Consequently all the conclusions of Yin_C_F0029, including numerical-rank independence and the specified closed-domain criterion for bounded elements, hold for these duals.
   In fact every cleared defect has a bounded extension, regardless of whether its rank is finite.

This does not assert that closability alone constructs a bounded reference dual, or that every dual satisfying an algebraic generator relation is closable.
The reference-dual hypothesis is a substantive restriction on the tuple.
The result applies, for example, to the canonical all-\(|q|<1\) q-Gaussian tuples using [Yin_C_F0023](Yin_C_F0023_v1.md#yin_c_f0023), and to the already checked Haar and semicircular bounded-dual models.

### Dependencies and Difference from Known Inputs

The proof reuses the Banach-Liouville mechanism of Yin_C_F0033, but applies it to the orbit map of an arbitrary vector \(z\in\mathcal E\), which need not be bounded or a vacuum vector.
The passage from commutation with all bounded left multipliers to affiliation is exactly [AP18 Definition 7.2.2](../audits/literature/AP18/Yin_U003.md#affiliation-interface).
Closed graph, scalar Liouville, Kaplansky density and bounded perturbation of a closed operator are the standard analytic inputs already used in Yin_C_F0032/Yin_C_F0033.
The resulting criterion can invoke Yin_C_F0029 directly; alternatively (37.3) reduces its finite-rank equivalence to [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013).

<a id="yin_c_f0036-p1"></a>
### Proof yin_c_f0036-p1

Fix \(i\) and abbreviate \(C_0=C_{i,0}\), \(B=B_i\).
Since \(B\) is bounded, \(C_0\) is closable.
The prescribed relations give
\[
C_0(X_jz)=X_jC_0z\qquad(z\in\mathcal E).
\tag{37.4}
\]

Fix an arbitrary vector \(v\in\mathcal E\), and define
\[
T_v:\mathcal M\longrightarrow H,\qquad T_v(a)=C_0(av).
\]
This map is defined on all of the Banach space \((\mathcal M,\|\cdot\|)\) by left invariance.
It has a closed graph: if \(a_n\to a\) in operator norm and \(C_0(a_nv)\to w\) in \(H\), then \(a_nv\to av\) in \(H\); closedness of \(\overline{C_0}\), and \(av\in\mathcal E\), give \(C_0(av)=w\).
Therefore \(T_v\) is bounded from operator norm to Hilbert norm.
Its bound may depend on \(v\).

For each coordinate \(x=X_j\), (37.4) says \(T_vL_x=\lambda(x)T_v\), where \(L_x\) is left multiplication on the Banach space \(\mathcal M\).
Consider
\[
F_v(\zeta)=\lambda(e^{\zeta x^*})T_vL_{e^{-\zeta x^*}},
\qquad \zeta\in\mathbb C.
\]
Norm-convergent exponential series make this an entire function with values in \(B(\mathcal M,H)\).
Intertwining the exponentials of \(x\), and then using normality of \(x\), gives
\[
F_v(\zeta)=\lambda(e^{\zeta x^*-\bar\zeta x})
T_vL_{e^{-\zeta x^*+\bar\zeta x}}.
\]
Both exponentials are unitary.
Their left actions are isometries on the respective spaces, so \(\|F_v(\zeta)\|\leq\|T_v\|\).
Scalar Liouville, applied through continuous linear functionals on \(B(\mathcal M,H)\), shows that \(F_v\) is constant.
Differentiating at zero yields
\[
T_vL_{x^*}=\lambda(x^*)T_v.
\]
Consequently \(T_v(q(X,X^*))=q(X,X^*)C_0v\) for every starred polynomial \(q\).

For \(a\in\mathcal M\), Kaplansky density followed by norm approximation in \(C^*(X)\) supplies uniformly bounded starred polynomials \(q_\alpha\) converging strongly to \(a\) in the standard representation.
Thus
\[
q_\alpha v\longrightarrow av,
\qquad C_0(q_\alpha v)=q_\alpha C_0v\longrightarrow aC_0v
\]
in \(H\).
The graph of \(\overline{C_0}\) is closed also for nets.
Since \(av\in\mathcal E\), this proves \(C_0(av)=aC_0v\).
The argument uses the boundedness of the orbit map \(T_v\); it never applies bounded Fuglede to the possibly unbounded \(C_0\).

Let \(C=\overline{C_0}\).
For \(z\in\operatorname{Dom}C\), choose \(z_n\in\mathcal E\) converging in the graph norm.
For every \(a\in\mathcal M\),
\[
az_n\to az,
\qquad C_0(az_n)=aC_0z_n\to aCz.
\]
Hence \(a\operatorname{Dom}C\subseteq\operatorname{Dom}C\) and \(Caz=aCz\).
For unitaries, application to the inverse gives equality of domains.
By the bicommutant theorem and the checked affiliation definition, \(C\) is affiliated with \(\lambda(\mathcal M)'\).

For completeness, the adjoint-module property follows directly.
If \(\eta\in\operatorname{Dom}C^*\), \(a\in\mathcal M\) and \(z\in\operatorname{Dom}C\), then
\[
\langle a\eta,Cz\rangle
=\langle\eta,a^*Cz\rangle
=\langle\eta,C(a^*z)\rangle
=\langle C^*\eta,a^*z\rangle
=\langle aC^*\eta,z\rangle.
\]
Thus \(a\eta\in\operatorname{Dom}C^*\) and \(C^*(a\eta)=aC^*\eta\).
This domain is dense because \(C\) is closed and densely defined.
Bounded perturbation gives (37.2), so it is also the whole adjoint domain of the dual closure.

Finally, left invariance defines all terms in (37.3), and the already proved module property gives
\[
sC_0(bz)-aC_0(tz)=(sb-at)C_0z=0.
\]
This proves (37.3).
Density of \(\mathcal E\) makes its bounded extension unique, and the rank on \(\mathcal E\) equals the rank of that extension whenever either is finite: a bounded map sends a dense set densely into its range closure, and a finite-dimensional subspace is closed.
Either Yin_C_F0029 with the now-automatic adjoint module, or Yin_C_F0013 applied to \(B_i\), gives the affiliated finite-rank criterion.
For the bounded-element closed-domain assertion, use the same graph-approximation argument with \(D_i\) and its specified core \(\mathcal E\), exactly as in Yin_C_F0029-P2 Step 4.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:54 |
| status | proved |
| reason | Adopt the exact actual original finding at its complete reviewed scope while preserving the mathematical assessment, fixed argument, dependencies and historical decisions. The original initial context-isolation fact remains unknown; no new or redated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0036-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0036-bounded-reference-and-automatic-adjoint-module) | Actual original complete C_F0036 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained original finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and selected argument; retain all original assessments, source depths and useful negative boundaries at their historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0036-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New whole-proof finding](../audits/reviews/Yin_R_F0066_v1.md#fresh-c37-whole) | Actual isolated whole-proof inspection at this exact fixed input, including all necessary accepted-input applicability and stated limits; historical findings remain separately unknown. |

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
| argument | [Exact material](#yin_c_f0036-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0036-bounded-reference-and-automatic-adjoint-module) | Original selected finding; its actual scope and limits remain in the cited review. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0036-bounded-reference-and-automatic-adjoint-module).

The original whole-source review included the bounded-reference comparison, the normal starred-commutator argument and the selfadjoint L1-density construction.
Its accompanying source context and complete original scope remain in the cited finding.
