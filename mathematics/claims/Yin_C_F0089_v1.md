---
author: Yin
---

# Finite-index transfer; virtually free and uniform finite-spectrum families

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Yin_C_F0089: Finite-Index Transfer and Virtually Free Groups

<a id="yin_c_f0089"></a>

Provenance: project deduction combining established group-algebra and free-group inputs.
Candidate proof version: **Yin_C_F0089-P1** below.
Initial mathematical status: proof draft; review status: awaiting independent review.
No new free-field identification for groups with torsion is asserted.

### Statement

Let \(H\le G\) be a subgroup of finite index \(n\).
Write \(\mathcal N(K)\) for the group von Neumann algebra of a discrete group \(K\), with its canonical faithful normal trace.
Assume:

1. \(\operatorname{Div}_{L^0(\mathcal N(H))}\mathbb CH\) is a division ring.
2. \(\operatorname{Div}_{L^0(\mathcal N(H))}\mathbb CH\cap\mathcal N(H)=\operatorname{Div}_{\mathcal N(H)}\mathbb CH\).

Then
\[
\operatorname{Div}_{L^0(\mathcal N(G))}\mathbb CG\cap\mathcal N(G)
=\operatorname{Div}_{\mathcal N(G)}\mathbb CG.
\tag{16}
\]
Consequently (16) holds whenever \(G\) has a free subgroup of finite rank and finite index, in particular for every finitely generated virtually free group.
It holds for
\[
G=C_{m_1}*\cdots*C_{m_d},\qquad d<\infty,\quad 2\le m_j<\infty.
\tag{17}
\]
For the canonical generating unitaries \(u_j\) of (17), (16) is property (B) for the finite free family \((u_1,\ldots,u_d)\).
It is also property (B) for freely independent selfadjoint variables whose individual laws are uniform on arbitrary finite sets of distinct real numbers.
The finite sets may have different sizes.
An arbitrary nonuniform finite atomic law is not included in this last assertion.

### Accepted source interfaces and search scope

- **Lin00, arXiv v1, p. 3**, the paragraph beginning with the free-group restriction, states that the affiliated division closure of a free group algebra is a division ring; **Theorem 1.1 on the same page** gives its bounded intersection as the scalar inverse closure in the reduced group \(C^*\)-algebra.
  These passages were reread in the [primary preprint](https://arxiv.org/pdf/math/9907075).
  The bounded-intersection interface was already accepted in [Miy26-U004](../audits/literature/Miy26/Yin_U004.md#miy26-u004); the original Lin00 and earlier division-ring proofs are not newly audited here.
  The source's reduced-\(C^*\) conclusion supplies assumption 2 because its scalar closure is contained in the \(\mathcal N(H)\) closure, which in turn is contained in the stated bounded intersection.
- **Yin20, Lemma IV.5.8, printed p. 61 / PDF p. 71**, in the [existing audited unit](../audits/literature/Yin20/Yin_U002.md#yin20-u002), states matrix inverse closure for a unital division subring of a larger algebra.
  This is applied only to the affiliated subgroup division ring, not to an arbitrary bounded output of a pencil.
  The short matrix-kernel verification is recalled below.
- The affiliated algebra and its identification under finite matrix amplification are the retained foundations of [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004).
  The finite-coset representation below is an explicit unitary realization of the usual subgroup matrix representation; all its entries and the final reconstruction are calculated.
- **Lyndon, *Two notes on Rankin's book on the modular group*, Theorem 2, pp. 455-456, and the finite-group remark on p. 457**: the kernel of the map from a finite free product of groups to their direct product is free; for finite factors its index and rank are finite.
  The statement, explicit basis, proof, and finite-group specialization were read in the [four-page publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F0C5A8057DE75A477309E55D6CD7B9B0/S1446788700015433a.pdf/div-class-title-two-notes-on-rankin-s-book-on-the-modular-group-div.pdf).
  The [publisher record](https://doi.org/10.1017/S1446788700015433) verifies Journal of the Australian Mathematical Society 16(4) (1973), 454-457.
  This is a source theorem attributed by Lyndon to Nielsen, with his stated extension from finite cyclic to arbitrary group factors.
  The needed finite-group conclusion is accepted; the original Nielsen proof is not audited.

The new finite-index statement was not found in the scoped local/primary searches described above and is not presented as historically new.
Neither an Atiyah conjecture result alone nor a division-ring assertion for \(G\) is substituted for (16).

### Yin_C_F0089-P1: proof

Choose representatives \(g_1=1,g_2,\ldots,g_n\) of the left cosets \(G/H\).
There is a unitary
\[
W:\bigoplus_{j=1}^n\ell^2(H)\longrightarrow\ell^2(G),
\qquad W(e_j\otimes\delta_h)=\delta_{g_jh}.
\tag{18}
\]
For \(g\in G\), write \(gg_j=g_i h_{ij}(g)\) for the uniquely determined coset index \(i\) and element \(h_{ij}(g)\in H\).
The matrix of \(W^*\lambda_G(g)W\) has entry \(\lambda_H(h_{ij}(g))\) in row \(i\), column \(j\), and zero entries in the other rows of that column.
In particular unitary conjugation gives an injective unital *-homomorphism
\[
\rho:\mathcal N(G)\longrightarrow M_n(\mathcal N(H)),
\qquad \rho(\mathbb CG)\subseteq M_n(\mathbb CH).
\tag{19}
\]
The extension from the group algebra follows by weak operator closure, since the target matrix von Neumann algebra is weakly closed.
The same unitary conjugation sends affiliated operators into the affiliated algebra of the target: the target commutant is contained in the commutant of \(\rho(\mathcal N(G))\), so the defining commutation condition for affiliation still holds.
Using finite matrix amplification, this extends (19) to an injective unital homomorphism
\[
\widetilde\rho:L^0(\mathcal N(G))\longrightarrow
M_n(L^0(\mathcal N(H))).
\tag{20}
\]
It preserves the affiliated sum, product, and inverse operations, since these are transported by the fixed unitary.
No entries are obtained by restricting an arbitrary unbounded operator to a vector outside its domain.

For this proof only, denote the division ring in assumption 1 by \(D\).
The algebra \(M_n(D)\) is inverse closed in \(M_n(L^0(\mathcal N(H)))\), by the accepted Yin20 interface.
Indeed, if a square matrix over \(D\) is not invertible over \(D\), division-ring linear algebra produces a nonzero right kernel column over \(D\); the same column survives in the larger algebra and prevents a two-sided matrix inverse there.

It follows by induction through scalar inverse expressions, starting with (19), that
\[
\widetilde\rho\left(\operatorname{Div}_{L^0(\mathcal N(G))}\mathbb CG\right)
\subseteq M_n(D).
\tag{21}
\]
Now let \(f\) be in the bounded intersection on the left side of (16).
Its matrix \(\rho(f)\) is bounded and has all entries in \(\mathcal N(H)\).
By (21) and assumption 2, every entry belongs to \(\operatorname{Div}_{\mathcal N(H)}\mathbb CH\).

Let \(h_i=\rho(f)_{i1}\).
The first column in the bounded identity (18) gives
\[
f\delta_1=\sum_{i=1}^n\lambda_G(g_i)h_i\delta_1,
\tag{22}
\]
where \(\mathcal N(H)\) is identified with its canonical von Neumann subalgebra of \(\mathcal N(G)\).
Each \(h_i\) lies in \(\operatorname{Div}_{\mathcal N(G)}\mathbb CG\): its scalar rational expression over \(\mathbb CH\) uses bounded inverses that remain inverses in the larger algebra.
Both sides of (22) are values of bounded elements of \(\mathcal N(G)\) on the separating trace vector.
Therefore
\[
f=\sum_{i=1}^n\lambda_G(g_i)h_i
\in\operatorname{Div}_{\mathcal N(G)}\mathbb CG.
\tag{23}
\]
This is a finite scalar reconstruction, not an invocation of a matrix inverse in the target bounded division closure.
The reverse inclusion in (16) is immediate.

For a finite-rank free subgroup \(H\), Lin00 supplies assumptions 1-2.
The trivial free subgroup is also allowed: then \(D=\mathbb C\), and (16) includes finite \(G\).
For (17), Lyndon's Theorem 2 supplies a finite-rank free normal subgroup as the kernel of the map onto \(C_{m_1}\times\cdots\times C_{m_d}\).
No normality of \(H\) was required by the transfer proof.

Finally, \(u_j^{-1}=u_j^{m_j-1}\), so the unstarred algebra generated by these unitaries is precisely \(\mathbb CG\).
The free factors are free for the canonical trace: an alternating product of centered group-algebra elements from distinct factors expands into nonidentity reduced group words and has trace zero.
Each \(u_j\) has the uniform law on the \(m_j\)-th roots of unity.
Choose any \(m_j\) distinct real numbers and map those roots bijectively to them.
Polynomial interpolation gives a selfadjoint \(x_j=p_j(u_j)\) and a reverse polynomial \(u_j=q_j(x_j)\).
Thus the polynomial algebras of the two tuples coincide, and the uniform atomic selfadjoint family inherits (16).
Other faithful realizations with the same joint *-distribution give the same conclusion through the induced trace-preserving isomorphism of their generated von Neumann algebras.

### Limits and author checks

The proof was checked for index one, a trivial subgroup of a finite group, a nonnormal finite-index subgroup, and the order of the coset coefficient reconstruction.
Its actual algebraic input is matrix inverse closure of the affiliated subgroup closure; assuming that closure is a division ring is one sufficient condition.
The target group may have torsion and need not have a division-ring closure itself.
The construction does not give full normalized rank-one duals for finite-spectrum coordinates, which have polynomial relations.

This result supplies a multivariable noncommutative family for (B), but does not establish its stability under free products of arbitrary diffuse one-coordinate laws or under analytic free transport.
It does not establish \(L^2\)-to-boundedness for all virtually free rational elements.
Yin_C_F0015's coefficient obligation and the q-Gaussian and diffuse-normal free-product targets remain separate.


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
| argument | [Exact material](#yin_c_f0089-p1-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0089_v1.md#historical-finite-index-transfer) | Actual original complete C_F0089 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain in the retained original finding. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:33 |
| status | proved |
| reason | Adopt the newly performed isolated complete P1 inspection completed at 2026-10-22T20:28; the two subgroup hypotheses, finite-index theorem, fixed proof and examples are unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Both subgroup assumptions and the finite-index, virtually free, finite cyclic free-product and uniform finite-spectrum conclusions at their exact scope. |
| argument | [Complete P1 argument](#yin_c_f0089-p1-proof) | Entire bounded/affiliated coset representation, division-ring matrix inverse closure, first-column scalar reconstruction and stated examples. |
| review | [Isolated whole finding](../audits/reviews/Yin_R_F0089_v1.md#current-finite-index-transfer) | Actual 2026-10-22 independent whole inspection with the recorded Lin00, Lyndon, Yin20 and affiliated-amplification interfaces, without original-source proof audits or nonuniform-law extension. |

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
| argument | [Exact material](#yin_c_f0089-p1-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0089_v1.md#historical-finite-index-transfer) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Original C_F0089 review finding, dated 2026-09-11: [retained same historical finding](../audits/reviews/Yin_R_F0089_v1.md#historical-finite-index-transfer).
The original mixed R_F0038 account also covered C_F0087, C_F0088 and the intervening coordinate-transfer observation; those are separate findings, not coverage supplied by the retained C_F0089 finding.

Mathematics in that original mixed account: [C_F0087](Yin_C_F0087_v1.md), [C_F0088](Yin_C_F0088_v1.md), [C_F0089](Yin_C_F0089_v1.md) and [coordinate transfer](../ledger/Yin_L_F0020_v1.md).
Earlier C_F0089 decisions continue to select only their applicable original finite-index finding, not the new 2026-10-22 review.
