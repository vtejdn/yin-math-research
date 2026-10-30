---
author: Yin
---

# Correlated Haar coordinates exclude marginal-only mixed-defect bounds

## Current assessment
[Selected decision](#decision-isolated-whole-review-20261023)

## Correlated Haar coordinates obstruct marginal-only mixed-defect bounds

<a id="statement"></a>
<a id="correlated-haar-mixed-defect-obstruction"></a>

Date: 2026-09-29.
Human record author: Yin.
Proof developed by another AI agent; separate complete mathematical review by another AI agent.
Consumer: [T_F0001's current contract](../tasks/Yin_T_F0001_v2.md), specifically its correlated-tuple contraction route after the accepted scalar soft-Cauchy theorem.
This is an ordinary Claim proof, not a manuscript theorem designation or formal extraction.
The canonical Claim record owns its mathematical and review assessments.
This diagnostic does not refute T_F0001.

Direct mathematical inputs are [C_F0025_v1](Yin_C_F0025_v1.md#decision-candidate-0002) for the represented derivatives and [C_F0045_v1](Yin_C_F0045_v1.md#decision-candidate-0002) for the exact right-module construction.
The [C_F0043_v1](Yin_C_F0043_v1.md#decision-candidate-0002) unitary theorem supplies the existing scope boundary, rather than a new proof step in the negative quadratic calculation below.

## 1. Exact claim and boundary

There is a family of pairs (A,B) satisfying the original T_F0001 hypotheses, indeed possessing bounded dual systems, such that:

* both A and B have the same Haar-unitary marginal law throughout the family;
* for the actual normal coarse derivative partial_A, its two ordinary-real components have a sum of coassociativity defects whose contracted quadratic form has arbitrarily large negative values on norm-one polynomials.

Consequently no uniform lower bound for this mixed-defect form can depend only on the marginal laws, their curvature masses, and the operator norm of the input.
A useful estimate must incorporate joint information, such as the full actual vacuum vectors.
This is **not** a counterexample to T_F0001's rationality criterion: the examples have bounded duals, so the established bounded-dual criterion applies to them.

Reuse: C_F0025 for represented normal derivatives and inner bimodule maps; C_F0045 Sections 3--5 for the exact free-product right-module dual construction; C_F0043 for the already established significance of unitary coassociativity defects; C_F0054 for the distinction between a failed estimate and a task refutation.
The elementary Haar contraction formula below is also recorded in C_F0047 and C_F0054.
No new external theorem or historical-priority assertion is used.
The coordinating agent independently checked the bounded-dual transfer formulas before this artifact was drafted; that is not the separate complete-artifact review.

## 2. A free reference pair with bounded duals

Fix 0<r<1.
Let U be a Haar unitary and let V be a unitary, freely independent from U, with Poisson-kernel law on the unit circle:

`dmu_r(z)=w_r(z) dm(z)`,
`w_r(z)=(1-r^2)/|1-rz|^2`,

where m is normalized Haar measure.
Its moments are

`tau(V^l)=r^|l|`,   `l in Z`.                                    (1)

One can verify these directly by multiplying the two convergent geometric series in the denominator.
The constant Fourier coefficient is one, so this is a probability measure.
Its positive density is bounded above and below:

`(1-r)/(1+r) <=w_r<=(1+r)/(1-r)`.

The standard name and Fourier identity were checked in [NIST DLMF 1.15.12--1.15.13](https://dlmf.nist.gov/1.15#E12) on 2026-09-29.
This is exact-statement attribution for the elementary calculation given here, not a new mathematical proof dependency or a whole-source audit.

The Haar canonical dual E_m has, on Laurent monomials,

`E_m(z^n)=z^(n-1)` for n>=1, and `E_m(z^n)=0` for n<=0.

It extends boundedly on L2(m), with norm one.
Moreover the convergent Fourier series gives

`E_m w_r=r/(1-rz)`,

a bounded function.
The canonical scalar operator for mu_r obeys, on Laurent polynomials,

`E_mu_r = E_m M_{w_r}-M_{E_m w_r}`.                              (2)

Indeed subtracting the two defining divided-difference integrals yields exactly `integral (p(z)-p(w))/(z-w) dmu_r(w)`.
Each operator on the right is bounded on L2(m); equivalent measure norms therefore make E_mu_r a bounded operator on L2(mu_r).
Its vacuum adjoint exists automatically, and it has commutator P with coordinate multiplication.

Take the faithful finite-tracial free product M=W*(U,V), H=L2(M).
The exact free-product construction of C_F0045 decomposes each normalized full dual into orthogonal copies of its scalar canonical dual.
Because both scalar duals here are bounded on their Hilbert spaces, the resulting D_U,D_V are bounded on H and satisfy

`[D_U,U]=P`, `[D_U,V]=0`, `[D_V,U]=0`, `[D_V,V]=P`.               (3)

Their starred-generator commutators are bounded finite rank, since the generators are unitary and `[D,W*]=-W*[D,W]W*`.

## 3. Correlated Haar coordinates retain bounded duals

Set

`A=U`,   `B=U* V`.

Both are unitary and generate M, because V=AB.
Their starred polynomial algebra is the same as that of U,V.
Both marginal laws are Haar.
For B, expand `(U*V)^n` after writing each V as its scalar mean plus its centered part.
Every resulting word contains only positive powers of U*, separated by centered V-blocks; the nonzero powers of U* are centered.
Freeness makes each term have zero trace.
Thus tau(B^n)=0 for n>=1, and adjoints give all negative moments too.

Write rho(c) for bounded right multiplication by c.
Define

`D_A=D_U+D_V rho(B)`,   `D_B=rho(A)D_V`.                          (4)

These are bounded operators.
All right multipliers commute with left multipliers.
Direct calculation using (3) gives

`[D_A,A]=P`, `[D_B,A]=0`.

For B=U*V one has

`[D_A,B]=-U* P B+U* P rho(B)=0`,

because traciality gives `P rho(B)=P B`.
Also

`[D_B,B]=rho(A)U* P=U* A P=P`.

Thus A,B possess the required bounded dual system.
Restricting (4) to their starred polynomial algebra gives exactly the original-domain operators of the T_F0001 contract.
Their actual vacuum adjoints exist, and their starred commutators are finite rank by the unitary inverse formula.
No merely formal change of rational variables is being used to infer domain properties.

## 4. The actual mixed coassociativity defect

Let partial=partial_A be the normalized coarse derivation supplied by this dual.
It is defined on P=C<A,A*,B,B*> and satisfies

`partial A=1 tensor 1`,
`partial A*=-A* tensor A*`,
`partial B=partial B*=0`.

Its conjugate derivation is

`partial^dagger(p)=(partial(p*))^dagger`,

where tensor dagger is flip-adjoint.
In particular

`partial^dagger A=-A tensor A`,
`partial^dagger A*=1 tensor 1`,
`partial^dagger B=partial^dagger B*=0`.

Every displayed derivative is an algebraic tensor of bounded polynomials; all iterates below are therefore literally defined on the algebraic core.
Set the ordinary-real components

`delta_x=(partial+partial^dagger)/2`,
`delta_y=(partial-partial^dagger)/(2i)`,

and define their coassociativity defects

`A_x=(delta_x tensor I)delta_x-(I tensor delta_x)delta_x`,
`A_y=(delta_y tensor I)delta_y-(I tensor delta_y)delta_y`.

For any derivation, this difference is itself an outer derivation into the triple tensor module: the two Leibniz expansions have identical cross terms, which cancel.
Hence A_x+A_y is an outer derivation.

On A, one has

`delta_x A=(1 tensor 1-A tensor A)/2`,
`delta_y A=(1 tensor 1+A tensor A)/(2i)`.

Applying the definitions gives separately

`A_x(A)=A_y(A)=(A tensor 1 tensor 1-1 tensor 1 tensor A)/4`.

The same computation, or inverse differentiation, treats A*, while B and B* are annihilated.
Consequently on the **whole mixed polynomial algebra**,

`A_x+A_y = (1/2) iota L_A`,                                     (5)

where L_A is the liberation derivation

`L_A(A)=A tensor 1-1 tensor A`,
`L_A(A*)=A* tensor 1-1 tensor A*`,
`L_A(B)=L_A(B*)=0`,

and `iota(g tensor h)=g tensor 1 tensor h`.
This equality follows by the outer Leibniz rule and equality on every starred generator.
It is the actual normal phase defect, not an unrelated model derivation.

For comparison, three distinct points on the unit circle have squared Menger curvature one; the scalar positive coefficient in the sum of the two real defects is therefore the constant 1/2.
Formula (5) is its exact mixed extension.
Positivity of that scalar coefficient does not imply positivity of its contracted mixed-polynomial form.

## 5. Exact quadratic values on norm-one polynomials

Put

`p_n=(AB)^n=V^n`,   `n>=1`.

These are holomorphic polynomials in A,B and unitary, so their operator norm is one.
Since `L_A V=A tensor B-1 tensor V`, Leibniz gives

`L_A(V^n)=sum_{k=0}^{n-1}`
`   [V^k A tensor B V^(n-1-k)-V^k tensor V^(n-k)]`.              (6)

Freeness of U,V and tau(U*)=0 give

`tau(B V^(n-1-k))=tau(U* V^(n-k))=0`.

Therefore the actual right contraction is

`(id tensor tau)L_A(V^n)=-sum_{k=0}^{n-1} r^(n-k) V^k`.

Pairing with V^n, using the inner product linear in its second variable and tau(V^{-l})=r^l, yields

`Re <p_n,(id tensor tau)L_A p_n>`
` = -sum_{l=1}^n r^(2l)`.

Equations (5)--(6) prove the exact mixed-defect value

`Re <p_n,(id tensor tau tensor tau)(A_x+A_y)p_n>`
` = -(1/2) sum_{l=1}^n r^(2l)`
` = -r^2(1-r^(2n))/(2(1-r^2))`.                                 (7)

For fixed r this decreases to `-r^2/(2(1-r^2))` as n increases.
The lower limit tends to minus infinity as r increases to one, while both coordinate marginals and their curvature masses remain unchanged.
Thus (7) refutes any finite universal lower bound depending solely on those marginal data and `||p_n||=1`.

## 6. Research consequence

The negative term in a prospective sum-of-real-components energy estimate cannot be controlled by scalar curvature mass alone.
The full joint vacuum vectors in this family are allowed to vary and grow with r.
An estimate using those vectors remains plausible and is not disproved by (7).

For each fixed r the quadratic sequence in (7) is bounded below; this example does not assert divergence in n for a single admissible tuple.
There is no contradiction with the unitary all-M theorem or the full bounded-dual affiliated criterion.
No main-goal refutation, correlated contraction theorem, numerical experiment, or proof-assistant check is claimed.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T18:16 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#correlated-haar-mixed-defect-obstruction) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: A family with fixed Haar marginal laws and bounded original dual systems has mixed coassociativity-defect forms unbounded below across the family.
This refutes marginal-only energy bounds, not affiliated rationality or estimates using full joint vacuum data.

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:07 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#correlated-haar-mixed-defect-obstruction) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Identify the actual normal coarse derivative and its conjugate on the original starred core from the displayed bounded dual system. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Exact orthogonal free-product module construction lifts the explicitly bounded Haar and Poisson marginal duals to bounded reference duals on all H. |
| dependency | [Exact material](Yin_C_F0043_v1.md#decision-candidate-0002) | Scope comparison: the existing unitary original-domain theorem applies to every example; the negative mixed defect does not refute affiliated rationality. |
| review | [Original finding](../audits/reviews/Yin_R_F0078_v1.md#verdict-and-achieved-scope) | Actual whole six-section correlated-Haar mixed-defect obstruction at its unknown initial-context relationship; across-family quantifiers and original bounded duals retained, no Task or joint-vacuum refutation. |


### Decision isolated-whole-review-20261023

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:55 |
| status | proved |
| reason | Adopt the newly performed isolated whole-proof finding at its exact scope after initial independent inspection and later historical comparison. Preserve the fixed mathematics, earlier decisions and exact non-review relations; historical checking relationships remain at their actual findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#correlated-haar-mixed-defect-obstruction) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Identify the actual normal coarse derivative and its conjugate on the original starred core from the displayed bounded dual system. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Exact orthogonal free-product module construction lifts the explicitly bounded Haar and Poisson marginal duals to bounded reference duals on all H. |
| dependency | [Exact material](Yin_C_F0043_v1.md#decision-candidate-0002) | Scope comparison: the existing unitary original-domain theorem applies to every example; the negative mixed defect does not refute affiliated rationality. |
| review | [New whole independent finding](../audits/reviews/Yin_R_F0078_v1.md#f0099-whole-independent-20261023) | Complete current fixed proof at the exact hypotheses and limits stated in the new finding; earlier unknown relationships and their historical adoption are not reclassified. |

## Historical assessments

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T18:18 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#correlated-haar-mixed-defect-obstruction) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Identify the actual normal coarse derivative and its conjugate on the original starred core from the displayed bounded dual system. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Exact orthogonal free-product module construction lifts the explicitly bounded Haar and Poisson marginal duals to bounded reference duals on all H. |
| dependency | [Exact material](Yin_C_F0043_v1.md#decision-candidate-0002) | Scope comparison: the existing unitary original-domain theorem applies to every example; the negative mixed defect does not refute affiliated rationality. |
| review | [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0099) | Complete six-section construction: bounded Haar and Poisson reference duals, free-product lift, transferred original duals, both fixed Haar marginals, actual sum of real-component defects, exact negative quadratic family and its quantifiers. Full joint-vacuum estimates and the main rationality criterion are not refuted. |

Recorded mathematical summary: A family with fixed Haar marginal laws and bounded original dual systems has mixed coassociativity-defect forms unbounded below across the family.
This refutes marginal-only energy bounds, not affiliated rationality or estimates using full joint vacuum data.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Complete six-section construction: bounded Haar and Poisson reference duals, free-product lift, transferred original duals, both fixed Haar marginals, actual sum of real-component defects, exact negative quadratic family and its quantifiers.
Full joint-vacuum estimates and the main rationality criterion are not refuted.

Review: [Exact material](../audits/reviews/Yin_R_F0078_v1.md#historical-f0099).

Material covered by that review: [Exact material](Yin_C_F0057_v1.md).
