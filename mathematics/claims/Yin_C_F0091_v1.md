---
author: Yin
---

# Dimension-two regular polynomial ring fails bounded descent

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Yin_C_F0091: A Regular Two-Dimensional Polynomial Algebra Can Fail Bounded Closure

<a id="statement"></a>
<a id="yin_c_f0091"></a>

Date: 2026-09-11.
Agent contribution: another AI agent; root allocated Yin_C_F0091 under Yin_T_F0003/Yin_S_F0013.
Provenance: project application of the standard elementary quotient \(x^2/(x^2+y^2)\) and the continuous-inverse argument already used for Yin_C_F0088.
Mathematical assessment at authorship: complete proof draft.
Review assessment: self-reviewed; independent review pending.
No optional Role or novelty claim is assigned.

Let \(K=\{(s,t)\in\mathbb R^2:s^2+t^2\le1\}\), let \(\mu\) be normalized planar area, and let \(x(s,t)=s\), \(y(s,t)=t\) in \(\mathcal M=L^\infty(K,\mu)\).
Then \(A=\mathbb C[x,y]\subset C(K)\) is an adjoint-closed Noetherian integrally closed domain of Krull dimension two (indeed the regular polynomial ring in two variables), but
\[
f=\frac{x^2}{x^2+y^2}
\in\operatorname{Div}_{L^0(\mathcal M)}A\cap\mathcal M
\setminus\operatorname{Div}_{\mathcal M}A.
\tag{48.1}
\]
Here the value of \(f\) at the origin can be chosen arbitrarily.
In particular Yin_C_F0090 cannot be extended merely by deleting its dimension bound, even for a regular polynomial algebra and a full-support diffuse measure.

### Reuse and accepted source inputs

The continuous inverse mechanism comes from [Yin_C_F0088](Yin_C_F0088_v1.md#yin_c_f0088); that result's singular cusp is not needed as a premise.
Local searches for normal domains, polynomial factorization and planar quotients were followed by primary-source inspection of the relevant The26b passages on 2026-09-11:

- [Lemma 10.120.10, tag 0BC1](https://stacks.math.columbia.edu/tag/0BC1) says a polynomial ring over a field is a unique factorization domain; [Lemma 10.120.11, tag 0AFV](https://stacks.math.columbia.edu/tag/0AFV) says a unique factorization domain is normal.
- [Lemma 10.31.3, Section 10.31, tag 00FM](https://stacks.math.columbia.edu/tag/00FM) supplies Noetherianity of a finite type algebra over a field.
- [Lemma 10.114.1 and Proposition 10.114.2, Section 10.114, tag 00OO](https://stacks.math.columbia.edu/tag/00OO) give regularity and dimension two of the local rings at maximal ideals of \(\mathbb C[s,t]\); hence its Krull dimension is two.

Their displayed statements and applicability were checked in the primary HTML.
The short unique-factorization/normality proofs were read; the foundational dimension-theoretic dependencies were not recursively audited.
These established ring facts are accepted inputs.
The elementary quotient below is a familiar multivariable-calculus example, with no claim of a new formula or historical priority.

<a id="yin_c_f0091-p1"></a>
### Proof Yin_C_F0091-P1

Polynomial evaluation \(\mathbb C[s,t]\to C(K)\) is injective: if a polynomial vanishes on the disk, fix \(t\) in an interior interval and use the infinitely many values of \(s\) to show that every coefficient polynomial in \(t\) vanishes; their vanishing on an interval makes them zero.
Thus the abstract polynomial-ring properties cited above apply to \(A\).
Complex conjugation fixes the coordinates and conjugates coefficients, so \(A\) is adjoint closed.

The denominator \(q=x^2+y^2\) vanishes only at the origin, a set of area zero.
Therefore \(q^{-1}\) is an affiliated inverse, and the displayed fraction lies in the affiliated division closure.
Off the origin it lies between zero and one, proving its boundedness.

Next, \(C(K)\) is division closed inside \(\mathcal M\).
Indeed, if \(g\in C(K)\) has an inverse in \(\mathcal M\), then \(|g|\ge c>0\) almost everywhere.
If \(|g(z)|<c\) at any point, continuity would give a nonempty relatively open set where that strict inequality holds; full support would give it positive measure, a contradiction.
Thus \(|g|\ge c\) everywhere and \(g^{-1}\in C(K)\).
Consequently
\[
\operatorname{Div}_{\mathcal M}A\subset C(K).
\tag{48.2}
\]

Suppose a continuous \(g\) on \(K\) represents \(f\).
On the punctured disk, both \(g\) and the quotient \(s^2/(s^2+t^2)\) are continuous and agree almost everywhere.
Their difference must be zero at every punctured point, since a nonzero value would persist on a nonempty relatively open set of positive area.
Hence, for \(0<|a|<1\),
\[
g(a,0)=1,\qquad g(0,a)=0.
\]
Both families approach the origin, contradicting continuity of \(g\).
Thus \(f\) has no continuous representative, and (48.2) proves (48.1).
QED.

### Scope and self-review

The obstruction concerns the bounded-intersection equality alone and is independent of an L2-to-bounded claim.
It preserves all of Yin_C_F0090's ring and measure assumptions except dimension at most one.
It is not a counterexample under the full independent dual relations for a two-coordinate tuple: the coordinates commute, and such relations on a common dense invariant domain would give \(0=[D_x,xy-yx]=Py-yP\).
This bounded operator is nonzero, since it sends the vacuum to \(-y\) under the area trace.
Thus the required two-coordinate dual system is absent.
The existing free-field counterexample Yin_C_F0012 retains its distinct role.

Self-review checked the polynomial injection, normality versus principal-ideal distinctions, the single null denominator zero, the difference between a pointwise discontinuity and absence of any continuous almost-everywhere representative, and the full-support inverse argument.
No computation, formal verification, external human review or priority assessment was performed.
The separate independent audit of the preceding Yin_C_F0090 text remains scoped to that original prefix and excludes Yin_C_F0091.


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
| argument | [Exact material](#yin_c_f0091-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0092_v1.md#planar-obstruction-finding) | Whole C_F0091 dimension-two regular polynomial-ring counterexample, actual affiliated inverse, boundedness, continuous-representative exclusion and absence of the dual assumptions. Actual original finding with unknown initial-context arrangement; historical date and accepted-input depth unchanged. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0091-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0092_v1.md#current-isolated-finding) | Whole C_F0091 dimension-two regular polynomial-ring counterexample, actual affiliated inverse, boundedness, continuous-representative exclusion and absence of the dual assumptions. |

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
| argument | [Exact material](#yin_c_f0091-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0092_v1.md#planar-obstruction-finding) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0092_v1.md#planar-obstruction-finding).

Material covered by that review: [Exact material](Yin_C_F0090_v1.md), [Exact material](Yin_C_F0091_v1.md) (together retain the original whole-source scope).
