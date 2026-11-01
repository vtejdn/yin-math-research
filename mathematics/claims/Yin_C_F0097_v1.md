---
author: Yin
---

# A one-state actual q-energy sequence has no eventual constant-coefficient recurrence

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## 4. Exact obstruction to a constant finite energy recurrence

<a id="statement"></a>
<a id="yin_c_f0097"></a>

<a id="one-state-energy-obstruction"></a>

Take d=1, 0<|q|<1, and the one-state recognizable coefficient sequence \(\alpha_n=t^n\), t nonzero.
Its actual homogeneous energy is

\[
e_n=|t|^{2n}[n]_q!
=a^n\kappa_n(q),
\qquad
a=\frac{|t|^2}{1-q},
\qquad
\kappa_n(q)=\prod_{k=1}^n(1-q^k).
\tag{4.1}
\]

This sequence has no nonzero eventual constant-coefficient linear recurrence.
Indeed, suppose \(\sum_{j=0}^m b_j e_{n+j}=0\) for all sufficiently large n, with b_m nonzero.
Dividing by e_n gives

\[
\sum_{j=0}^m b_j a^j\prod_{r=1}^j(1-q^r q^n)=0.
\tag{4.2}
\]

The polynomial

\[
F(x)=\sum_{j=0}^m b_j a^j\prod_{r=1}^j(1-q^r x)
\]

vanishes at infinitely many distinct x=q^n.
It is therefore identically zero.
But its coefficient of x^m is \(b_ma^m(-1)^m q^{m(m+1)/2}\ne0\), a contradiction.
The argument includes negative q; only q=0 and t=0 were excluded.

Consequently the scalar energy generating function is not rational, and no fixed finite matrix B with e_n=uB^nv can represent this energy.
Such a representation would imply a constant recurrence by Cayley-Hamilton.
This refutes that proposed intermediate mechanism, not Q5 or Q6.

At the same time, each factor in \(\kappa_n(q)\) is positive and \(\sum_{k\ge1}|q|^k<\infty\), so

\[
0<\inf_n\kappa_n(q)\le\sup_n\kappa_n(q)<\infty,
\qquad
\kappa_n(q)\longrightarrow\kappa_\infty(q)>0.
\tag{4.3}
\]

It follows that \(\sum_ne_n<\infty\) if and only if a<1, and in that case energy decays exponentially.
The exact variable-coefficient recurrence is

\[
e_{n+1}=a(1-q^{n+1})e_n.
\tag{4.4}
\]

Its coefficient approaches a exponentially.
Thus a controlled nonconstant recurrence can work where a fixed finite energy matrix provably cannot.

For positive q, choose \(1-q\le|t|^2<1\): the ordinary coefficients are square summable while the q-series is not.
For negative q, choose \(1\le|t|^2<1-q\): the q-series is square summable while the ordinary coefficients are not.
These are exact normalization diagnostics.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:15 |
| status | proved |
| reason | Adopt the exact actual original finding at its disclosed unknown initial-context relationship. Preserve mathematical status, statement, selected proof, dependencies and historical decisions; no new mathematical proof version or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0097) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0109_v1.md#outcome-and-boundaries) | Complete original one-state nonrecurrence obstruction, exact summability threshold and sign-sensitive examples. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0097) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0109_v1.md#current-isolated-finding) | Complete original one-state nonrecurrence obstruction, exact summability threshold and sign-sensitive examples. |

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
| review-status | independently reviewed |

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
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0097) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0109_v1.md#outcome-and-boundaries) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0109_v1.md#outcome-and-boundaries).

Material covered by that review: [Exact material](Yin_C_F0097_v1.md), [Exact material](Yin_C_F0098_v1.md), [Exact material](../ledger/Yin_L_F0024_v1.md) (together retain the original whole-source scope).
