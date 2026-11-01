---
author: Yin
---

# Bounded division closure for finitely many free square-zero matrix units

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## Positive support and bounded reconstruction for finitely many free square-zero matrix units

<a id="statement"></a>

Date: 2026-09-16.
Human record author: Yin.
Developed by another AI agent; transcribed and edited by the coordinator.
The original complete proof review is recorded separately with its [input-relationship limits](../audits/reviews/Yin_R_F0097_v1.md#review-relationships).
This statement concerns the specified finite family, not the full general T_F0007 contract.

<a id="finite-free-square-zero-positive-support"></a>

Let m>=1 be finite and let (M,tau) be the reduced tracial free product of m copies of (M2(C),tr2).
Write x_i=e12 in factor i, A=C<x_1,...,x_m>, R=Div_M A, and F=Div_L0(M) A.
Affiliated operators act by actual closed left multiplication on H=L2(M), with vacuum Omega=1.
Let H_+ be the closed span of Omega and reduced words in the x_i.

The conclusions are

    (F intersect M) Omega subset H_+,      F intersect M = R.       (1)

In particular this allows unbounded intermediate affiliated inverses.
All inverse and product arguments below concern their actual operator domains.

## 1. Bounded terminal-block operators

In factor i use the centered orthonormal basis

    z_(i,+)=sqrt(2)e12,  z_(i,-)=sqrt(2)e21,  z_(i,0)=e11-e22.

Its reduced words together with Omega form an orthonormal basis.
Define d_i(a)=a x_i-x_i a.
Traciality gives tau(d_i(a))=0, and direct multiplication gives

    d_i(1)=d_i(z_(i,+))=0,
    d_i(z_(i,-))=-sqrt(2)z_(i,0),
    d_i(z_(i,0))=sqrt(2)z_(i,+).                                  (2)

Thus the centered kernel is C z_(i,+), and its norm is sqrt(2).
Set T_i Omega=0.
On a nonempty reduced word, set T_i=0 if its terminal factor is not i; otherwise set

    T_i(a_1 ... a_n Omega)=a_1 ... a_(n-1) d_i(a_n) Omega.          (3)

For each reduced prefix p empty or ending outside factor i, the three vectors p z_(i,t) Omega form an invariant three-dimensional block.
These blocks are mutually orthogonal, and T_i is zero on the remaining basis vectors.
Consequently ||T_i||=sqrt(2).
No scalar component is created and no terminal block is deleted.
Moreover,

    T_i xi=0 iff all coefficients of xi ending in
    z_(i,-) or z_(i,0) vanish.                                    (4)

## 2. Commutation with the prescribed generators

For every i,j, [T_i,L_(x_j)]=0.
On Omega this follows from d_i(x_i)=0.
On a single block a in factor i, the only same-factor case uses x_i^2=0:

    d_i(x_i a)=x_i a x_i=x_i d_i(a).                            (5)

Taking the centered part of x_i a does not change its image under d_i.
A generator from another factor prefixes a centered block and commutes with (3).
On a single block from a factor different from i, left multiplication can prefix a block or produce a scalar and a centered block in that other factor; T_i kills every resulting term, as it kills the input.

On a word with at least two blocks, left multiplication changes only the first block.
Its centered contribution commutes with the terminal operation.
If a scalar contraction deletes the first block, the terminal factor still remains.
Explicitly the only short boundary is a_1 a_2 with a_2 in factor i and x_j a_1=c1+b in the first factor: applying the two operations in either order gives c d_i(a_2)+b d_i(a_2).
The latter product is reduced since d_i(a_2) is centered.
If the terminal factor is not i both orders are zero.
The same calculation treats longer words.
Density of the basis and boundedness prove the full commutation relation.

## 3. Commutation detects forbidden letters in every position

Suppose f in M commutes with every T_i.
For a reduced basis word w put beta_w(f)=tau(w* f).
If w=v z_(i,t) s with t in {-,0}, the first factor of a nonempty suffix s differs from i.
Therefore the last factor of s* differs from i, and T_i(s* Omega)=0, also when s is empty.
Commutation gives T_i(f s* Omega)=0.
By (4), its coefficient at v z_(i,t) is zero.
Traciality gives, in the indicated order,

    0 = tau((v z_(i,t))* f s*)
      = tau(s* (v z_(i,t))* f)
      = tau((v z_(i,t) s)* f) = beta_w(f).                       (6)

Every forbidden letter can be selected at any position.
Hence

    f in M and [T_i,L_f]=0 for every i imply f Omega in H_+.       (7)

Already the bounded product and bounded inverse commutation identities imply R Omega subset H_+.
This preservation has not been assumed.

## 4. Actual affiliated operations preserve commutation

For any bounded T on H let E_T consist of closed densely defined affiliated operators a such that

    T Dom(a) subset Dom(a),     a T xi=T a xi for xi in Dom(a).    (8)

We show that E_T is a unital subalgebra of L0(M), closed under every inverse existing there.
We use the established finite-trace affiliated-algebra convention: addition and multiplication are closures of the densely defined operator sum and product.
See the existing [measure-topology interface](../audits/literature/FK86/Yin_U001.md#measure-topology-interface) and [affiliation interface](../audits/literature/AP18/Yin_U003.md#affiliation-interface); no new source theorem beyond that foundation is needed.

For a,b in E_T the initial sum domain Dom(a) intersect Dom(b) is T-invariant, and (a+b)T=T(a+b) there.
If xi_n tends to xi and (a+b)xi_n tends to eta along that domain, boundedness gives T xi_n tending to T xi and (a+b)T xi_n tending to T eta.
The graph closure therefore contains (T xi,T eta).
This proves (8) for the closed sum.
Scalar multiples and the identity are immediate.

For multiplication start on the actual domain

    D={xi in Dom(b): b xi in Dom(a)}.

For xi in D, T xi is in Dom(b), and b T xi=T b xi is in Dom(a), so D is T-invariant and ab T xi=a T b xi=T ab xi.
The same graph-limit argument gives (8) for the closed affiliated product.
In particular no equality of formal products has replaced a domain argument.

If a is invertible in L0(M), its actual closed operator is injective with dense range.
Indeed a nonzero kernel projection p would satisfy ap=0 and contradict a^-1 a p=p; a nonzero cokernel projection q would satisfy qa=0 and contradict q a a^-1=q.
The closed affiliated inverse has domain Ran(a).
For eta=a xi, equation (8) gives

    T eta=a T xi in Ran(a),    a^-1 T eta=T xi=T a^-1 eta.         (9)

Thus a^-1 belongs to E_T.
This argument requires neither selfadjointness of T nor commutation with T*.

Section 2 implies A subset E_(T_i).
Division-closedness then yields F subset intersection_i E_(T_i).
For bounded f in F its actual domain is all H, so it commutes with every T_i.
Section 3 proves the support assertion in (1).

## 5. Reconstruction using only bounded scalar inverses in A

We give the finite-m reconstruction, rather than enlarge the three-factor statement [C_F0113 (recorded assessment 2)](Yin_C_F0113_v1.md#decision-candidate-0002) by assertion.
Let B be the polynomial star algebra generated by the full matrix factors.
A subset B, so f in F intersect M lies in Div_L0(M) B intersect M.
Apply the finite-rank and residual mechanism of [C_F0106 (recorded assessment 2)](Yin_C_F0106_v1.md#decision-candidate-0002), whose finite-dimensional tracial factors may form any fixed finite family.
It supplies a minimal recognizable representation of the reduced coefficients,

    beta_w=lambda mu(w) gamma,
    V=sum_t mu_t tensor a_t,    ||V^k|| -> 0,
    f=lambda (I-V)^-1 gamma,                                  (10)

where a_t form the centered selfadjoint orthonormal factor bases.
Products mu_s mu_t from the same factor are zero.
Minimal means both reachable and observable; no uniformity in m is required.

Change each factor's centered Pauli basis to z_(i,+),z_(i,-),z_(i,0).
If z_t=sum_s U_(ts) a_s, with U unitary within the factor, set mu'_t=sum_s conjugate(U_(ts)) mu_s.
This is exactly the Fourier coefficient change.
The old and new transition families span each other, preserving minimality and same-factor zero products.
Furthermore

    sum_t mu'_t tensor z_t
      =sum_(t,s,r) conjugate(U_(ts)) U_(tr) mu_s tensor a_r
      =V.                                                       (11)

The support assertion in Section 4 implies, for every forbidden letter t and all words p,q,

    lambda mu'(p) mu'_t mu'(q) gamma=0.                         (12)

For reduced p t q this is its vanishing Fourier coefficient.
For nonreduced p t q it follows from a same-factor zero product.
Reachability and observability give mu'_t=0: first the reachable vectors mu'(q)gamma span the whole state space, and then all rows lambda mu'(p) separate that space.
Hence

    V=sum_i mu'_(i,+) tensor sqrt(2)x_i in M_N(A),              (13)

with its actual norm decay unchanged.

Use the already audited [DR97-U004](../audits/literature/DR97/Yin_U004.md#dr97-u004) small-power scalar elimination.
Choose q so large that V^q has sufficiently small entries.
Scalar Neumann pivots and Schur elimination invert I-V^q using only bounded scalar inverses of expressions in those entries.
Then

    (I-V)^-1=(I-V^q)^-1 (I+V+...+V^(q-1))                     (14)

has all entries in R.
This construction adjoins no adjoints and no unbounded scalar inverses.
Equation (10) gives f in R.
Conversely a bounded inverse is also its affiliated inverse, so R subset F intersect M.
This completes (1).

## 6. Dependency and scope boundary

The direct Claim premise for reconstruction is C_F0106 (recorded assessment 2).
C_F0113 is proof-method provenance and a previously reviewed three-factor conditional interface; its hypothesis has now been established by a new argument.
The affiliated-algebra foundation and DR97-U004 are reused at their already audited scopes.
The terminal-block proof, including every unbounded inverse domain, is self-contained relative to that foundation.

Each individual algebra C1+C x_i is already division closed in M2 and L0(M2), since any invertible a+b x_i has its inverse in that algebra.
The m=3 instance therefore fits the original binary T_F0007 contract by grouping the first two factors; the accepted [C_F0112 (recorded assessment 2)](Yin_C_F0112_v1.md#decision-candidate-0002) is an earlier independent proof of the two-factor equality.
The theorem itself permits grouping inductively for every finite m.

This proves a family of proper non-star input cases.
It does not establish permanence for arbitrary proper non-star or diffuse inputs.
Neither a support obstruction nor a counterexample to general T_F0007 follows from this result.
No external novelty finding, numerical proof, rendered source validation or full Task completion is asserted.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-16T14:18 |
| status | open |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#finite-free-square-zero-positive-support) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: For every finite family of normalized M2 factors with coordinates e12, bounded terminal-block operators force positive-word support through all actual affiliated rational operations; stable reconstruction proves equality of bounded and affiliated division closures on bounded elements.

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
| argument | [Exact material](#finite-free-square-zero-positive-support) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0106_v1.md#decision-candidate-0002) | Finite-rank residual construction, minimal full-alphabet realization, same-factor zero products and actual state-pencil norm decay for any fixed finite family of finite-dimensional tracial factors. |
| review | [Exact material](../audits/reviews/Yin_R_F0097_v1.md) | Entire finite-family square-zero theorem: positive support, actual inverse domains and bounded scalar reconstruction; general T_F0007 remains open. |

Recorded mathematical summary: For every finite family of normalized M2 factors with coordinates e12, bounded terminal-block operators force positive-word support through all actual affiliated rational operations; stable reconstruction proves equality of bounded and affiliated division closures on bounded elements.

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
| argument | [Exact material](#finite-free-square-zero-positive-support) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0106_v1.md#decision-candidate-0002) | Finite-rank residual construction, minimal full-alphabet realization, same-factor zero products and actual state-pencil norm decay for any fixed finite family of finite-dimensional tracial factors. |
| review | [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0095-applicability) | Yin_C_F0116 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope. No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: For every finite family of normalized M2 factors with coordinates e12, bounded terminal-block operators force positive-word support through all actual affiliated rational operations; stable reconstruction proves equality of bounded and affiliated division closures on bounded elements.

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
| argument | [Exact material](#finite-free-square-zero-positive-support) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0106_v1.md#decision-candidate-0002) | Finite-rank residual construction, minimal full-alphabet realization, same-factor zero products and actual state-pencil norm decay for any fixed finite family of finite-dimensional tracial factors. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0103_v1.md#c-f0095-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Entire finite-family square-zero theorem: positive support, actual inverse domains and bounded scalar reconstruction; general T_F0007 remains open.

Review: [Exact material](../audits/reviews/Yin_R_F0097_v1.md).

Material covered by that review: [Exact material](Yin_C_F0116_v1.md).

Yin_C_F0116 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete mathematical review at its unchanged scope.
The original independent description is historical; the [R_F0097 relationship disclosure](../audits/reviews/Yin_R_F0097_v1.md#review-relationships) retains the unestablished initial input conditions.
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0103_v1.md#c-f0095-applicability).

Material covered by that review: [Exact material](Yin_C_F0116_v1.md).
