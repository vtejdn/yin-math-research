---
author: Yin
---

# AP18: Affiliation and Adjoint Domains

Current responsible source home, 2026-10-21: [AP18-U003](../audits/literature/AP18/Yin_U003.md#ap18-u003) retains this selected source content at its original reading dates and inspection limits.
The dated L account and its original consumers remain inspectable; U preparation performs no new original-source review.


<a id="affiliation-interface"></a>
Date: 2026-09-11.
Reviewer: the dual-domain research agent.
Scope: a source-interface check for Yin_T_F0002, not a Chapter 7 audit.
Bibliographic identity: AP18, the undated Anantharaman-Popa author draft.

The [author-hosted PDF](https://www.math.ucla.edu/~popa/Books/IIun.pdf) was reopened as a 338-page document.
Parsed primary text was inspected at Definition 7.2.2 and its surrounding conventions, printed p. 103 / PDF p. 109, and Theorem 7.2.8(i), printed p. 105 / PDF p. 111.
Screenshot requests did not expose inspectable image content in this tool session, so no visual formula review is claimed.

Definition 7.2.2 defines affiliation with a represented von Neumann algebra by equality of the operators after commuting with every unitary in its commutant; equality includes equality of domains.
It also states the equivalent formulation using commutation with every bounded element of that commutant.
Theorem 7.2.8(i) states that the adjoint of a closed densely defined affiliated operator remains affiliated, in the finite-tracial setting used here.
Their statements and applicability are accepted; the book's underlying unbounded spectral theory and original proofs were not re-audited.

In [Yin_C_F0037](../claims/Yin_C_F0037_v1.md#yin_c_f0037), the represented algebra is the **right commutant** \(\lambda(\mathcal M)'\).
The proof first establishes commutation of a specified closed operator with all of \(\lambda(\mathcal M)\), including domain invariance.
The bicommutant identity then supplies exactly the definition's hypothesis.
The adjoint-domain consequence is also checked directly by Hilbert-space pairing in that project proof.
This does not identify either dual itself as affiliated: affiliation is asserted only for its difference from a bounded reference dual.

The right-multiplication interpretation follows from the standard tracial commutant \(\lambda(\mathcal M)'=J\lambda(\mathcal M)J\), with the conventions already checked in [the Tomita source record](Yin_L_F0040_v1.md#tomita-foundational-reference).
No square-integrability of the resulting right-affiliated multiplier, or membership of the vacuum in its domain, is asserted.

<a id="l1-predual-interface"></a>
## Additional L1 Interface for Yin_C_F0045

The same primary draft was subsequently inspected as parsed text at Theorem 7.4.5, printed pp. 114-115 / PDF pp. 120-121, and its Radon-Nikodym restatement Theorem 7.4.9, printed p. 116 / PDF p. 122.
Theorem 7.4.5 identifies \(a\in L^1(\mathcal M,\tau)\) with the normal functional \(x\mapsto\tau(ax)\), gives equality of its functional norm and \(\|a\|_1\), and states completeness of this L1 space.
Theorem 7.4.9 records uniqueness of that density for every normal functional.
The surrounding convention is the same general finite-tracial standard representation, with no factoriality assumption.

[Yin_C_F0045](../claims/Yin_C_F0045_v1.md#yin_c_f0045) applies the norm identity and completeness to an explicit Cauchy sequence of L2 densities.
Thus normality is obtained by constructing the L1 limit; it is not inferred from an unverified topology characterization.
Only these established statements and their applicability were checked, without a new audit of the original Lp construction or theorem proofs.
