---
author: Yin
---

# Algebraic tensor equalizer over a division subring

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Yin_C_F0035: The Algebraic Tensor Equalizer of a Division Subring

<a id="statement"></a>
<a id="yin_c_f0035"></a>

Role: lemma.
Provenance: project deduction extracted from existing complete proofs.
Extraction origin: agent-proposed shared-lemma organization, explicitly authorized by the user in the [authorization record](../ledger/Yin_L_F0014_v1.md#authorization).
Proof version: [Yin_C_F0035-P1](#yin_c_f0035-p1), candidate, review pending.

### Extraction Provenance

The basis-functional argument appears in [Yin_C_F0029, Section 7](Yin_C_F0029_v1.md#yin_c_f0029), and [Yin_C_F0013, Section 6](Yin_C_F0013_v1.md#yin_c_f0013).
These record where the argument was extracted.
Neither Yin_C_F0029 nor Yin_C_F0013 is a logical input to the proof below.

### Statement and Scope

Let \(U\) be a unital ring, and let \(F\subseteq U\) be a division subring with the same identity element \(1_F=1_U\neq0\).
Give the first copy of \(U\) its right \(F\)-module structure and the second copy its left \(F\)-module structure, both by ring multiplication.
Form the algebraic balanced tensor product \(U\otimes_F U\).
Then, for every \(u\in U\),
\[
u\otimes_F1=1\otimes_Fu
\quad\Longleftrightarrow\quad u\in F.
\tag{35.1}
\]
Equivalently, the equalizer in \(U\) of the two additive maps \(u\mapsto u\otimes_F1\) and \(u\mapsto1\otimes_Fu\) is exactly \(F\).

No commutativity or centrality of \(F\), absence of zero divisors in \(U\), analytic structure, topology, operator representation or normality is assumed.
The tensor product is algebraic, not completed.

### Proof Dependencies for Yin_C_F0035-P1

The proof uses only the balancing relation for the algebraic tensor product and extension of a right-linearly independent set to a basis over a division ring.
The latter is the ordinary algebraic basis theorem, with its usual choice principle.
There is no project-claim dependency and no dependence on Yin_C_F0031 or Yin_C_F0034.

<a id="yin_c_f0035-p1"></a>
### Yin_C_F0035-P1: Complete Candidate Proof

If \(u\in F\), the balancing relation gives
\[
u\otimes_F1=(1u)\otimes_F1
=1\otimes_F(u1)=1\otimes_Fu.
\tag{35.2}
\]
This proves one implication.

For the converse, suppose \(u\notin F\).
The elements \(1,u\) are right-\(F\)-linearly independent in \(U\).
Indeed, assume
\[
1a+ub=0,\qquad a,b\in F.
\]
If \(b\neq0\), multiplication on the right by \(b^{-1}\in F\) gives
\[
u=-ab^{-1}\in F,
\]
contrary to the assumption.
If \(b=0\), the relation reduces to \(a=0\).
Thus only the trivial right-linear relation exists.

Since \(F\) is a division ring, \(U\) is a right vector space over \(F\).
Extend the independent set \(\{1,u\}\) to a right-\(F\) basis \(\mathcal B\) of \(U\).
Every \(x\in U\) then has a unique finite expansion
\[
x=\sum_{b\in\mathcal B}b\alpha_b,\qquad \alpha_b\in F.
\]
Define \(\phi:U\to F\) by taking the coefficient of the basis element \(u\):
\[
\phi(x)=\alpha_u.
\]
Uniqueness of the basis expansion makes \(\phi\) well-defined, additive and right-\(F\)-linear, with
\[
\phi(1)=0,\qquad \phi(u)=1.
\tag{35.3}
\]

Define on pairs of elements of \(U\) the biadditive map
\[
(x,y)\longmapsto\phi(x)y\in U.
\]
For every \(f\in F\), right linearity of \(\phi\) gives
\[
\phi(xf)y=\phi(x)fy=\phi(x)(fy).
\]
The map is therefore \(F\)-balanced and induces an additive map
\[
\Psi:U\otimes_FU\longrightarrow U,
\qquad \Psi(x\otimes_Fy)=\phi(x)y.
\tag{35.4}
\]
If the equality in (35.1) held, applying \(\Psi\) would yield
\[
1=\phi(u)1
=\Psi(u\otimes_F1)
=\Psi(1\otimes_Fu)
=\phi(1)u=0,
\]
contradicting \(1_U\neq0\).
Thus the equality cannot hold for \(u\notin F\), proving the converse and completing Yin_C_F0035-P1.

### Checks, Limits and Review Status

Right linearity is essential to the orientation in (35.4); no left-\(F\)-linearity or commutation of coefficients is used.
The proof needs no cancellation by a nonzero element of \(U\) outside \(F\), so zero divisors in \(U\) are allowed.
The basis functional is purely algebraic and need not be continuous under any topology a particular application gives to \(U\).
An application must supply its division subring \(F\) and its tensor equality independently; this lemma does not prove free-field realization or construct that equality.

Yin_C_F0035-P1 awaits separate mathematical review.
No formal verification, computational verification or historical novelty claim is made.

<a id="yin_c_f0035-hun74-source-supplement"></a>
### Yin_C_F0035-P1: Hun74 Source Supplement, 2026-09-10

Record kind: source attribution and verification of existing standard proof inputs.
Authorization: the user's requested Hun74 Chapter IV audit and import of useful definitions/theorems.
This supplement adds precise sources without changing the statement, argument, proof version or extraction provenance above.

| Existing input in Yin_C_F0035-P1 | Accepted primary source and applicability |
| --- | --- |
| Extension of the independent set {1,u} to a right F-basis | [Hun74 IV.2.4, p. 183](../audits/literature/Hun74/Yin_U002.md#division-ring-bases). The printed left-module theorem applies to right modules via F-opposite. The same-unit inclusion makes U a unitary right F-vector space; no commutativity is needed. |
| Right-linear coordinate functional phi | [Hun74 IV.4.11, p. 204](../audits/literature/Hun74/Yin_U004.md#algebraic-dual), with the explicit right-sided conversion in the audit. The proof uses a single coordinate functional, not finite dimensionality of U or a basis of its full dual. |
| Balanced tensor and induced additive map Psi | [Hun74 IV.5.1–5.2, pp. 208–209](../audits/literature/Hun74/Yin_U005.md#balanced-tensor). Right F-linearity of phi proves balancing of (x,y) to phi(x)y, exactly as checked in (35.4). The tensor is an abelian group with the stated natural right/left factor actions. |

These sources identify the logical standard inputs already used by P1.
Yin_C_F0029 and Yin_C_F0013 remain its **extraction sources**, not proof premises.
Hun74 does not state the particular tensor equalizer as a numbered theorem; the deduction (35.1) remains the project argument.
The alternate tensor presentation qualified on p. 212 and the basis-induced action in IV.5.12 are not used here.

The preceding candidate-stage “review pending” sentences are historical author-stage metadata.
The [completed independent review](../audits/reviews/Yin_R_F0021_v1.md#yin_c_f0034-yin_c_f0035-fraction-tensor-review) and [selected assessment](#decision-candidate-0002) already accept Yin_C_F0035-P1.
This source supplement is root's self-review of the new attribution and applicability; it does not extend the earlier review's byte-level artifact scope or claim a new independent review.
The complete statement and proof text preceding this supplement is preserved.


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
| argument | [Exact material](#yin_c_f0035-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0021_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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
| argument | [Exact argument](#yin_c_f0035-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0021_v1.md#division-equalizer-finding) | Actual original complete or auxiliary scope stated by that finding; unchanged versions and original source-depth/nonconclusion boundaries. |

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

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0021_v1.md).

Material covered by that review: [Exact material](Yin_C_F0034_v1.md), [Exact material](Yin_C_F0035_v1.md) (together retain the original whole-source scope).
