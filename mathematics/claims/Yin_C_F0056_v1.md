---
author: Yin
---

# Scalar vacuum energy restores original mixed-polynomial coassociativity for normal derivations

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Original Triple-Domain Coassociativity for Normal Polynomial Derivations

<a id="statement"></a>
<a id="normal-phase-original-coassociativity"></a>

Date: 2026-09-29.
Human record author: Yin.
A research agent developed the proof; `counterexample` performed a separate complete mathematical review.
Consumer: [T_F0001 current contract](../tasks/Yin_T_F0001_v2.md).
This is a new ordinary Claim proof, not a manuscript theorem designation or formal extraction.
The canonical Claim record owns the mathematical and review assessments.
General correlated-tuple contraction remains open.

The setting is a finite von Neumann algebra `(M,tau)` with faithful normal probability trace, `H=L2(M,tau)`, and a finite bounded normal generating tuple `X`.
Inner products are linear in the second variable.
Hilbert tensor powers and their closed operators are distinct from algebraic tensor cores and from the bounded spatial tensor-algebra elements used as multipliers below.
The operators `partial_i tensor I` and `I tensor partial_i` mean the Hilbert closures of their operators on `P tensor_alg P`, not maximal measurable difference operators.
Coassociativity means precisely equality (7) with membership in these specified domains.

Reuse before proof covered C_F0025, C_F0028, C_F0029, C_F0050, C_F0054, S_F0011, the local method index, and the scalar argument now accepted as C_F0055 (recorded assessment 2).
The direct mathematical inputs are C_F0025 (recorded assessment 3) and C_F0055 (recorded assessment 2).
The approximation below uses finite geometric sums; no new external approximation theorem is imported.
The named free-difference-quotient coassociativity mechanism is already source-checked in [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002).
That source's selfadjoint contraction theorem is not applied to the normal tuple here; the missing mixed-contraction interface is retained in Section 6.

## 1. Exact inputs and conclusion

Use [C_F0025_v1](Yin_C_F0025_v1.md#decision-candidate-0002)'s original normal-tuple hypotheses and normalized coarse derivations partial_i on P=C<X,X*>.
Each partial_i p is a finite sum of bounded spatial tensors: partial_i Xi=1 tensor 1 and

`partial_i Xi* = k_i`,   `k_i(z,w)=(bar z-bar w)/(z-w)`

in the coordinate abelian tensor subalgebra; k_i has modulus one off its null diagonal.
Other-coordinate derivatives vanish.
The derivations are closable: the vacuum adjoint and the Leibniz rule put P tensor P in the actual adjoint domain.
This is the C_F0025/ACSY24 interface, rather than an assumed maximal extension of a difference operator.

[C_F0055_v1](Yin_C_F0055_v1.md#decision-candidate-0002), in its [proof Sections 4--5](Yin_C_F0055_v1.md#soft-cauchy-vacuum-free-normal-criterion), supplies, for the spectral measure mu_i and its actual scalar vacuum eta_i, the following two bounds.
With three distinct points and

`x=|z-w|^2`, `y=|v-w|^2`, `r=|z-v|^2`,
`A=x+t`, `B=y+t`, `R=r+t`,
`H=2xy+2yr+2rx-x^2-y^2-r^2`,

it proves

`integral H/(x y r) dmu_i^3 <= 6 ||eta_i||2^2`,                    (1)

`S_t=[H+t(x+y+r)]/(2 A B R) >=0`,
`integral S_t dmu_i^3 <= 3 ||eta_i||2^2`.                          (2)

Here eta_i is the actual marginal vacuum, obtained by restricting the full conjugate variable to its coordinate algebra; in particular its norm is no larger than that of the full vacuum xi_i.
The two inequalities are accepted inputs from that independently reviewed proof; no curvature or regularization assumption is added here.

The conclusion is that k_i lies in the **original closed** domains of both partial_i tensor I and I tensor partial_i, with their common three-variable second divided difference as value.
This extends to genuine coassociativity on every mixed starred polynomial.
It does not itself prove the contraction estimate on mixed words.

## 2. A bounded smooth approximation of the normal phase

Suppress i and put

`k_t(z,w) = (bar z-bar w)^2/(|z-w|^2+t)`.

These are smooth, have absolute value at most one, and tend almost everywhere and in L2(mu^2) to k.
They belong to the original closed partial-derivative domains, as follows without a new multidimensional approximation theorem.

Choose C larger than the maximum of |z-w|^2+t on the spectral square and use the finite geometric sums for 1/(|z-w|^2+t).
Their products with (bar z-bar w)^2 are algebraic tensors of starred polynomials.
The sums and their first real derivatives converge uniformly to k_t on the square, since the geometric ratio is uniformly less than one.
The approximants have norm at most one: the finite sum equals k_t times
`1-(1-(|z-w|^2+t)/C)^(N+1)`.

First divided differences of the approximants therefore converge uniformly.
Graph closure of partial tensor I identifies its value at k_t with

`L_t(z,v,w)=[k_t(z,w)-k_t(v,w)]/(z-v)`.                            (3)

The other-leg argument is identical.
The scalar coordinate tensor embeds isometrically into the full coarse Hilbert tensor powers; consequently these are statements about the original full-tuple partial_i domains too.

## 3. Uniform triple-L2 estimate

Write a=z-w and b=v-w.
The numerator in (3), put over A B, is

`bar a^2 (y+t)-bar b^2 (x+t)`
` = bar a bar b (bar a b-bar b a)+t(bar a-bar b)(bar a+bar b)`.

The exact planar identity `|bar a b-bar b a|^2=H` and the elementary two-term square bound give

`|L_t|^2 <= 2 x y H/(r A^2 B^2)`
`             +4 t^2(x+y)/(A^2 B^2)`
`         <= 2 H/(r x y)+4 t^2(x+y)/(A^2 B^2)`.                  (4)

Because r<=2(x+y),

`t R/(A B) <= 5`,

where the deliberately nonoptimal constant follows by bounding the three terms of `t[2x+2y+t]/(A B)` separately.
Therefore

`4 t^2(x+y)/(A^2 B^2)`
` <=20 t(x+y+r)/(A B R) <=40 S_t`.                               (5)

Equations (1), (2), (4), (5) imply

`||L_t||2^2 <=132 ||eta_i||2^2`.                                 (6)

For distinct z,v,w, L_t tends to the actual second divided difference

`L(z,v,w) = [k(z,w)-k(v,w)]/(z-v)`.

Its squared magnitude is exactly H/(x y r), not just bounded by it.
Its norm is consequently at most sqrt(6)||eta_i||2 by (1).
The uniform estimate (6) is needed for graph recovery, not for this final constant.

## 4. Recovery of the original iterated domain

Take t_n down to zero.
The graph pairs (k_{t_n},L_{t_n}) are bounded in the two Hilbert spaces, with first coordinate strongly converging to k.
Any weak cluster of the second coordinate equals L.
To justify that identification, test first against bounded functions supported where all three pairwise distances exceed a fixed positive epsilon; there the kernels converge uniformly.
The union of these test spaces is dense because the collision diagonals have zero product measure.
Uniform L2 boundedness then determines all remaining pairings.

The graph of the original closed partial tensor I is weakly closed, so it contains (k,L).
The same proof in the other leg gives its corresponding divided-difference value.
Symmetry of scalar second divided differences makes the two values equal with the standard ordered triple-tensor conventions.
Thus the original domain membership and equality are both proved.

For later product rules one may also obtain algebraic-tensor graph approximants of k which remain uniformly bounded in spatial operator norm.
First approximate each k_t by its finite geometric sums, with error small in both graph norms.
The resulting sequence is weakly convergent in the product of the input and the two graph-output Hilbert spaces.
Convex combinations of tails converge strongly to the same limit: otherwise separation of the closed convex hull from the limit by a Hilbert-space linear functional would contradict weak convergence.
Choose one such finite convex combination for each error 1/n.
Their spatial norms stay at most one.
This provides a single sequence for both iterated domains, with no uncontrolled derivative of a limiting phase.

## 5. Extension to mixed starred polynomials

Fix i.
In each term of partial_i p the only nonalgebraic tensor is k_i; the other factors are bounded polynomial left and right multipliers.
Use the uniformly bounded graph approximants of Section 4 to apply the actual closed product rule on these terms.
All extra derivatives of polynomial factors are bounded spatial tensors, so products with the L2-convergent approximants converge in L2.
Products with the derivative of k_i are bounded left/right multipliers of an L2 triple tensor.
This checks all domain inclusions required by the formal Leibniz calculation.

On Xi the two iterated derivatives vanish.
On Xi* they agree by Section 4.
On Xj,Xj* for j!=i both are zero, since their coordinate polynomial approximants are annihilated by partial_i.
The difference

`A_i(p)=(partial_i tensor I)partial_i p`
`          -(I tensor partial_i)partial_i p`

obeys the ordinary outer Leibniz rule on products.
Indeed the two product expansions contain the same cross term `(partial_i p)_{12}(partial_i q)_{23}`, which is bounded and cancels.
Induction on starred words therefore yields

`(partial_i tensor I)partial_i p`
`       =(I tensor partial_i)partial_i p`,   `p in P`,             (7)

with every term in its original closed Hilbert domain.
No freeness of the coordinate algebras was used.

As a consequence, if E_{i,0}=(id tensor tau)partial_i and E_i is its original closure, then E_{i,0}p lies in Dom E_i.
One can first contract the second factor of an original graph approximation of partial_i p to show that this contraction belongs to Dom closure(partial_i), then contract its derivative again.
Thus E_i(E_{i,0}p) is an actual vector and is given by the double contraction of either side of (7).
This restores the iterated-contraction domain used in a possible coupled adjoint identity.

## 6. Phase adjoints and the unresolved mixed energy estimate

Define the conjugate derivation on the original starred core by

`partial_i^dagger(p)=(partial_i(p*))^dagger`,

where tensor dagger is flip followed by adjoint.
Its actual vacuum adjoint is xi_i*: this follows directly by conjugating the original trace pairing.
The inner bimodule unitary

`U_i=(rho(X_i*) tensor I-I tensor lambda(X_i*))`
`       /(rho(X_i) tensor I-I tensor lambda(X_i))`

is defined by the normal spectral calculus off a null kernel and commutes with all outer M-actions.
Checking every starred generator gives

`partial_i^dagger=U_i* partial_i`.

In particular `U_i(1 tensor 1)` is in the actual partial_i-adjoint domain and has adjoint value xi_i*.
Thus both the unphased and phased vacuum vectors are available; no unproved adjoint-domain transfer by a unitary is being assumed.

Let F_{i,0}=(id tensor tau)partial_i^dagger.
The genuine core adjoint formula is

`E_{i,0}* p = p xi_i-F_{i,0}p`,
`F_{i,0}* p = p xi_i*-E_{i,0}p`.                                 (8)

Ordinary coassociativity (7) controls E_i^2 and the analogous F_i^2, where F_i is the original closure of F_{i,0}.
The latter statement follows by antiunitary conjugation and reversal of both original tensor domains in (7).
The norm of the first expression in (8), however, brings in the *mixed* iterate E_i F_{i,0}p.
Reality in the usual coarse involution would identify E and F; here it does not.
A legitimate mixed positivity identity or mixed-defect bound remains to be supplied.
The scalar soft Cauchy proof suggests such a bound, but no noncommutative mixed-word estimate is established here.

Consequently this proof repairs the previously unresolved triple-domain obligation using the accepted scalar curvature theorem.
It does not by itself complete the correlated-tuple contraction or T_F0001's full criterion.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T17:52 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-phase-original-coassociativity) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Under the exact original normal polynomial-core hypotheses, the normal phase lies in both original iterated derivation domains; actual coassociativity and squared contraction domains hold on all mixed starred polynomials without freeness.
Mixed adjoint energy remains open.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T17:58 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-phase-original-coassociativity) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original starred polynomial core, canonical normal phase, actual vacuum adjoints and diffuse marginal laws. |
| dependency | [Exact material](Yin_C_F0055_v1.md#decision-candidate-0002) | Soft Cauchy energy and finite total marginal curvature used to recover the original iterated tensor domains. |
| review | [Exact material](../audits/reviews/Yin_R_F0036_v1.md) | Complete six-section proof, original Hilbert tensor closures, controlled geometric polynomial approximation, soft kernel estimates, weak and strong graph recovery, mixed starred product rules, actual squared contractions and phased vacuum adjoints. No arbitrary-domain coassociativity or general correlated contraction is asserted. |

Recorded mathematical summary: Under the exact original normal polynomial-core hypotheses, the normal phase lies in both original iterated derivation domains; actual coassociativity and squared contraction domains hold on all mixed starred polynomials without freeness.
Mixed adjoint energy remains open.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:07 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-phase-original-coassociativity) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original starred polynomial core, canonical normal phase, actual vacuum adjoints and diffuse marginal laws. |
| dependency | [Exact material](Yin_C_F0055_v1.md#decision-candidate-0002) | Soft Cauchy energy and finite total marginal curvature used to recover the original iterated tensor domains. |
| review | [Original finding](../audits/reviews/Yin_R_F0036_v1.md#verdict-and-exact-scope) | Actual original independent complete six-section iterated-domain/coassociativity finding, including unchanged antiunitary-domain explanation; all original domain and correlated-contraction exclusions retained. |

## Recorded review scopes

Complete six-section proof, original Hilbert tensor closures, controlled geometric polynomial approximation, soft kernel estimates, weak and strong graph recovery, mixed starred product rules, actual squared contractions and phased vacuum adjoints.
No arbitrary-domain coassociativity or general correlated contraction is asserted.

Review: [Exact material](../audits/reviews/Yin_R_F0036_v1.md).

Material covered by that review: [Exact material](Yin_C_F0056_v1.md).
