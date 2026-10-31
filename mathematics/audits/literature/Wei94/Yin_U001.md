---
author: Yin
---

# Hochschild Boundary with Bimodule Coefficients

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Wei94-U001

Source: [Wei94, retained Chapter 9](../../../literature/pdf/Wei94--chapter-9.pdf), Cambridge Core chapter PDF hosted by MIT, 69 pages.
This source is Chapter 9 of the 1994 book, rather than the complete book.

Inspection date: 2026-10-12.
Reviewer: coordinating agent for Yin; definition, notation and application self-review.
Reading coverage: Read.
Directly inspected extracted text and rendered printed pp.300 and 302 (PDF pp.1 and 3).
No whole-chapter or whole-book audit.

<a id="wei94-hochschild-boundary"></a>
### Source definition and conventions

Section 9.1.1, printed p.300, fixes a commutative ground ring, an algebra R over it and an R-R bimodule M.
The degree-n chain module is M tensor R^{tensor n}, with degree zero M.
Its face maps on m tensor r_1 tensor ... tensor r_n are: the right action mr_1 for face zero; multiplication r_i r_{i+1} for an interior face; and the left action r_n m for the last face.
The chain differential is the alternating sum d = sum_i (-1)^i partial_i.

At degree one, the two face maps are partial_0(m tensor r)=mr and partial_1(m tensor r)=rm.
The displayed arrow from M tensor R to M is explicitly partial_0-partial_1.
Consequently d_1(m tensor r)=mr-rm.
The symbol partial_1 on this source page denotes a face map, not the whole degree-one differential.
The following paragraph identifies H_0(R,M)=M/[M,R].

Printed p.302, before Lemma 9.1.3, defines the enveloping algebra R tensor R^op and explains the conversions between bimodules and its left or right modules.
In particular a right enveloping-algebra action is m(r tensor s^op)=s m r.
This explains the order of the coefficient action used below.
The Tor/Ext comparison in Lemma 9.1.3 and its proof are outside the adopted input.

### Tensor-product bimodule specialization

Let M be a finite von Neumann algebra.
Take ground field C, algebra L0(M), and coefficient space L0(M) tensor L0(M)^op with action a dot k dot b = k(b tensor a^op), for a,b in L0(M) and k in the coefficient space.
Associativity follows from the opposite multiplication; the left and right actions commute.
The ordinary right regular action of the tensor-product algebra gives precisely this bimodule convention.

Substitution in d_1 gives d_1(k tensor x)=k dot x-x dot k=k(x tensor 1-1 tensor x^op).
This is a direct specialization of the definition, not a new theorem or an extension of tracial/L2-homology results to unbounded operators.
All tensor products here are algebraic.
Ordinary left multiplication in the tensor-product algebra is distinct from this coefficient left action.

CS05 Section 3.1.1 equation (3.1) supplies a formula on the linear space associated with a chosen generating tuple.
Wei94 supplies the full Hochschild boundary definition.
Restricting x to a chosen generator subspace is a separate linear restriction; full-boundary membership alone supplies no rationality criterion.
Proposition 9.1.6 about tensor algebras is outside the inspected input.

### Inspection limits

Checked the defining formulas, the degree-one sign, face-map versus differential notation, and the local coefficient action directly.
The full simplicial identities, higher-degree homology results, Tor/Ext comparison, Proposition 9.1.6, historical priority and book-wide errata were not audited.
No formal verification was performed.
No unresolved issue remains for this definition-level use.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Wei94, 1994 book; retained Cambridge Core Chapter 9 PDF hosted by MIT, 69 pages. |
| source-locator | Section 9.1.1, printed p.300 / PDF p.1; enveloping-algebra and bimodule conventions before Lemma 9.1.3, printed p.302 / PDF p.3. |
| inspection | Direct text and visual definition/convention checks; degree-one specialization and coefficient action checked. Self-review only; no whole-chapter, higher-homology or Tor/Ext proof audit. |

<a id="differential-notation-observations"></a>
## Additional differential terminology

On 2026-10-12, the retained chapter's printed pp. 333 and 345 / PDF pp. 34 and 46 were inspected as text and rendered pages.
Definition 9.6.5 names the associated chain complex the Hochschild complex and notes the traditional symbol b for its differential.
The paragraph following Definition 9.8.1 explicitly calls b the Hochschild differential.
Together with Section 9.1.1's d notation, these passages establish coexistence of d and b; the source does not use d exclusively.
The degree-one component d_1 remains distinct from the face map partial_1.
This additional terminology reading supplies no cyclic-homology or mixed-complex theorem audit.
