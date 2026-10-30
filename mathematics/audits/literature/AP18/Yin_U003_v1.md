---
author: Yin
---

# AP18-U003: Affiliation, adjoint domains and tracial L1 functionals

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Undated 338-page Anantharaman-Popa author draft identified by the sole AP18 registry account. |
| source-locator | Definition 7.2.2 p. 103 / PDF 109; Theorem 7.2.8(i) p. 105 / PDF 111; Theorems 7.4.5/7.4.9 pp. 114-116 / PDF 120-122. |
| inspection | 2026-09-11 parsed-primary statement/applicability checks; screenshots exposed no inspectable images; no original-proof re-audit. |

<a id="ap18-u003"></a>
## Retained selected source content

<a id="affiliation-interface"></a>
Date: 2026-09-11.
Reviewer: the dual-domain research agent.
Scope: affiliation and adjoint-domain interfaces for a closed operator in the tracial standard representation; not a Chapter 7 audit.
Bibliographic identity: AP18 in the registry (private lookup: `../../../literature/registry.md#contents-ap18`), the undated Anantharaman-Popa author draft.

The [author-hosted PDF](https://www.math.ucla.edu/~popa/Books/IIun.pdf) was reopened as a 338-page document.
Parsed primary text was inspected at Definition 7.2.2 and its surrounding conventions, printed p. 103 / PDF p. 109, and Theorem 7.2.8(i), printed p. 105 / PDF p. 111.
Screenshot requests did not expose inspectable image content in this tool session, so no visual formula review is claimed.

Definition 7.2.2 defines affiliation with a represented von Neumann algebra by equality of the operators after commuting with every unitary in its commutant; equality includes equality of domains.
It also states the equivalent formulation using commutation with every bounded element of that commutant.
Theorem 7.2.8(i) states that the adjoint of a closed densely defined affiliated operator remains affiliated, in the finite-tracial setting used here.
Their statements and applicability are accepted; the book's underlying unbounded spectral theory and original proofs were not re-audited.

In [Yin_C_F0036](../../../claims/Yin_C_F0036_v1.md#yin_c_f0036), the represented algebra is the **right commutant** \(\lambda(\mathcal M)'\).
The proof first establishes commutation of a specified closed operator with all of \(\lambda(\mathcal M)\), including domain invariance.
The bicommutant identity then supplies exactly the definition's hypothesis.
The adjoint-domain consequence is also checked directly by Hilbert-space pairing in that project proof.
This does not identify either dual itself as affiliated: affiliation is asserted only for its difference from a bounded reference dual.

The right-multiplication interpretation follows from the standard tracial commutant \(\lambda(\mathcal M)'=J\lambda(\mathcal M)J\), with the conventions already checked in [the Tomita source record](Yin_U002_v2.md#tomita-foundational-reference).
No square-integrability of the resulting right-affiliated multiplier, or membership of the vacuum in its domain, is asserted.

<a id="l1-predual-interface"></a>
## Additional L1 Interface for Yin_C_F0038

The same primary draft was subsequently inspected as parsed text at Theorem 7.4.5, printed pp. 114-115 / PDF pp. 120-121, and its Radon-Nikodym restatement Theorem 7.4.9, printed p. 116 / PDF p. 122.
Theorem 7.4.5 identifies \(a\in L^1(\mathcal M,\tau)\) with the normal functional \(x\mapsto\tau(ax)\), gives equality of its functional norm and \(\|a\|_1\), and states completeness of this L1 space.
Theorem 7.4.9 records uniqueness of that density for every normal functional.
The surrounding convention is the same general finite-tracial standard representation, with no factoriality assumption.

[Yin_C_F0038](../../../claims/Yin_C_F0038_v1.md#yin_c_f0038) applies the norm identity and completeness to an explicit Cauchy sequence of L2 densities.
Thus normality is obtained by constructing the L1 limit; it is not inferred from an unverified topology characterization.
Only these established statements and their applicability were checked, without a new audit of the original Lp construction or theorem proofs.
