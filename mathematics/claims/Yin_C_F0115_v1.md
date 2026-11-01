---
author: Yin
---

# The inverse of a sum of at least three free square-zero matrix units is unbounded

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## The inverse of a sum of free square-zero matrix units is unbounded

<a id="statement"></a>

Kind: Claim/proof.
Date: 2026-09-16.
Human record author: Yin.
Proof developed by the coordinating research agent; independent review is recorded separately.
Consumer: [T_F0007 v1](../tasks/Yin_T_F0007_v1.md#decision-candidate-0001).
This resolves a specific reciprocal test, not free-product bounded-closure permanence.
The earlier exploratory sketch is preserved separately.

<a id="free-square-zero-sum-hermitization"></a>
## 1. Statement and accepted inputs

Let n>=3 and let (M,tau) be the reduced free product of n copies of (M2(C),tr2).
Put x_i=e12 in the ith copy and s=sum_i x_i.
Then s is injective, has a two-sided inverse in L0(M), and that inverse is unbounded.
In the matrix amplification with its faithful normalized trace, write

    H = [[0,s],[s*,0]].

Its scalar Cauchy transform satisfies

    lim_(eta downarrow0) G_H(i eta) = -i (n-1)/(n sqrt((n-2)/2)).             (1)

Consequently zero belongs to the spectrum of H but has zero spectral mass.
This is enough for the asserted inverse conclusion; no assertion about a density on a neighborhood, Brown measure, or a complete spectrum is needed.

The only non-elementary scalar-law input is [NS06-U002's formal scalar-law interface](../audits/literature/NS06/Yin_U002.md#cumulant-additivity-and-formal-inverse-cauchy-interface): cumulant additivity and the formal inverse-Cauchy/R-transform identities of Proposition 12.3 and Theorems 12.5/12.7 in the inspected publisher edition.
The compact-support analytic germ and upper-half-plane continuation are local reasoning in Section 3, with the actual primary-reading depth and separate analytic checks retained in [R_F0099](../audits/reviews/Yin_R_F0099_v1.md#independence-and-source-inspection-depth).
The existing [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004) gives the finite-algebra interface between injectivity and affiliated invertibility.
The prior [two-generator result](Yin_C_F0112_v1.md) is comparison only and is not used to establish (1).

## 2. The hermitized summands really are scalar-free

Set H_i=[[0,x_i],[x_i*,0]] and B=M2(C), with conditional expectation E_B=id tensor tau on M2(M).
For k>=1,

    H_i^(2k)=diag(p_i,q_i),  p_i=x_i x_i*, q_i=x_i* x_i,
    E_B(H_i^(2k))=(1/2) I_2,  E_B(H_i^(2k+1))=0.

Thus the scalar law of H_i is

    nu=(1/4) delta_-1+(1/2) delta_0+(1/4) delta_1,                         (2)

and E_B(P(H_i)) equals its scalar trace times I_2 for every scalar polynomial P.
In particular a scalar-centered polynomial in H_i has all its matrix entries tau-centered and lying in M_i.

For scalar-centered P_1(H_(i1))...,P_k(H_(ik)) with adjacent indices different, every entry of their matrix product is a finite sum of products of centered entries from the corresponding alternating free factors.
Each has trace zero by the original scalar freeness of M_i.
Hence the scalar trace of that product vanishes.
This verifies the definition of scalar freeness for H_1,...,H_n directly.
It avoids the generally false assertion that arbitrary scalar variables from amplified free factors must be scalar-free.

The scalar law rho of H=sum H_i is therefore the n-fold additive free convolution of (2), and is symmetric, since its odd cumulants vanish.
Direct evaluation gives

    G_nu(u)=(u^2-1/2)/(u(u^2-1)).                                       (3)

## 3. From a local inverse series to the actual upper-half-plane branch

Let w(z)=G_H(z) for Im z>0.
The actual Cauchy transform is analytic with Im w(z)<0; in particular it never vanishes.
Define on the entire upper half-plane

    u(z)=(z+(n-1)/w(z))/n.                                               (4)

Since Im(1/w)>0, formula (4) implies Im u(z)>0.
Near infinity, the accepted inverse-Cauchy identities and R additivity give

    z=R_H(w)+1/w=n R_nu(w)+1/w,
    u=R_nu(w)+1/w,
    w=G_nu(u).                                                          (5)

These hold for sufficiently large z in an open portion of the upper half-plane: for each compactly supported probability law mu with Cauchy transform G_mu, g_mu(t)=G_mu(1/t)=t+O(t^2) is analytic near zero, so its local analytic inverse yields the inverse-Cauchy germ K_mu(w)=1/g_mu^(-1)(w).
The [formal source identities](../audits/literature/NS06/Yin_U002.md#cumulant-additivity-and-formal-inverse-cauchy-interface) identify K_mu(w)=1/w+R_mu(w); this compact-support analytic upgrade is local reasoning, as checked in [R_F0099, item 4](../audits/reviews/Yin_R_F0099_v1.md#complete-argument-checks).
Both sides of the last equality are analytic on the entire upper half-plane, since u takes values there and G_nu has only real poles.
The identity theorem therefore extends

    w(z)=G_nu(u(z))                                                      (6)

to that whole domain.
No arbitrary algebraic branch has been chosen.

By symmetry, for z=i eta with eta>0 write w=-i h, where

    h=integral eta/(eta^2+t^2) drho(t)>0.

Formula (4) gives u=i v, where v=(eta+(n-1)/h)/n>0.
Substitution in (3) and (6) yields

    h=(v^2+1/2)/(v(v^2+1)),
    eta=v (v^2-a^2)/(v^2+1/2),  a=sqrt((n-2)/2)>0.                       (7)

The positive left side forces v>a.
Let F(v)=v(v^2-a^2)/(v^2+1/2).
Its derivative is

    F'(v)=[v^4+(a^2+3/2)v^2-a^2/2]/(v^2+1/2)^2.

For v>=a the numerator is at least 2a^4+a^2>0.
Thus F maps [a,infinity) continuously and strictly increasingly from zero to infinity.
Equation (7) fixes its unique positive branch v=F^(-1)(eta), and v tends to a as eta decreases to zero.
Hence

    h -> (a^2+1/2)/(a(a^2+1)) = (n-1)/(n a),

which proves (1).

## 4. The spectral and affiliated conclusions

The elementary spectral formula

    eta h(eta)=integral eta^2/(eta^2+t^2) drho(t)

and bounded convergence give rho({0})=lim eta h(eta)=0.
Faithfulness of the normalized matrix trace therefore implies ker H=0.
Since H acts on a pair of vectors by H(xi,zeta)=(s zeta,s* xi), both s and s* are injective.
The finite-algebra affiliated inverse criterion now gives s^(-1) in L0(M).

If zero were outside the spectrum of H, some interval (-c,c) would have zero rho-mass, and h(eta)<=eta/c^2 would tend to zero.
This contradicts the strictly positive finite limit in (1).
Hence H is not boundedly invertible.
If s^(-1) were bounded, the block matrix [[0,(s*)^(-1)],[s^(-1),0]] would be a bounded inverse of H.
This is impossible.
Thus s^(-1) is unbounded.

For n=3 the limit h is 2 sqrt(2)/3.
The calculation proves the positive Poisson boundary value and absence of an atom; it does not infer a pointwise density merely by selecting a formal cubic root.

## 5. Consequence for the open Task

The natural expression (x_1+...+x_n)^(-1) belongs to the affiliated division closure but is unbounded.
It therefore cannot serve as a bounded counterexample to the original closure equality, nor can it directly disprove the positive-word support condition for bounded outputs.
Other expressions may behave differently.
No full n-factor permanence statement is asserted by this proof.

Source statement/application inspection was performed using the already registered local NS06 artifact.
No numerical experiment, rendered PDF check, proof-assistant verification, or historical novelty claim is made.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T14:17 |
| status | open |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#free-square-zero-sum-hermitization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: For every finite n at least three, the sum of n free normalized M2 square-zero matrix units is affiliated invertible but its actual inverse is unbounded; scalar hermitization fixes the analytic Cauchy branch.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T14:20 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#free-square-zero-sum-hermitization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0099_v1.md) | Entire finite-n reciprocal theorem and attached primary-source interface; no general free-product permanence conclusion. |

Recorded mathematical summary: For every finite n at least three, the sum of n free normalized M2 square-zero matrix units is affiliated invertible but its actual inverse is unbounded; scalar hermitization fixes the analytic Cauchy branch.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0003

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-19T13:54 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#free-square-zero-sum-hermitization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0094-applicability) | Yin_C_F0115 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope. No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: For every finite n at least three, the sum of n free normalized M2 square-zero matrix units is affiliated invertible but its actual inverse is unbounded; scalar hermitization fixes the analytic Cauchy branch.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-applicability

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:13 |
| status | proved |
| reason | Select the same actual applicability finding at its responsible R home, with its original date, exact per-Claim scope and known shared mathematical context, preserving statement, argument, dependencies and mathematical assessment. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#free-square-zero-sum-hermitization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0103_v1.md#c-f0094-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/NS06/Yin_U002.md).

Entire finite-n reciprocal theorem and attached primary-source interface; no general free-product permanence conclusion.

Review: [Exact material](../audits/reviews/Yin_R_F0099_v1.md).

Material covered by that review: [Exact material](../audits/literature/NS06/Yin_U002.md); [Exact material](Yin_C_F0115_v1.md).

Yin_C_F0115 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope.
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0094-applicability).

Material covered by that review: [Exact material](../audits/literature/NS06/Yin_U002.md); [Exact material](Yin_C_F0115_v1.md).
