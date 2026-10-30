---
author: Yin
---

# Fug50-U001: Bounded normal commutation from the exact original theorem

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Published 1950 article, identified by PMC metadata; Theorem I read from the author-uploaded extracted full text after the official PDF returned a challenge. |
| source-locator | Theorem I, printed p. 35; Sun14 Theorem 0.1 p. 1 only an initial identification aid. |
| inspection | 2026-09-10 exact theorem hypotheses/conclusion and bounded specialization checked; original proof not re-audited, no separability condition imported from the secondary aid. |

<a id="fug50-u001"></a>
## Retained selected source content

<a id="bounded-commutation"></a>
- Date and reviewer: 2026-09-10; the coordinating agent, scoped source-interface check.
- Purpose: identify the standard bounded normal-commutation input.
- Bibliographic identities and online artifacts: [Fug50 and Sun14 in references.bib](../../../literature/references.bib).
  No whole-paper audit or new project Claim is assigned.

## Accepted statement and sources

Let \(H\) be a complex Hilbert space and \(N,T\in\mathcal B(H)\), with \(N\) normal.
Then \(NT=TN\) implies \([N^*,T]=0\).
Both operators are bounded; no trace or dual system is needed.

The [PMC publication record](https://pmc.ncbi.nlm.nih.gov/articles/PMC1063127/) verifies Fug50's bibliographic identity.
Its PDF endpoint returned an access challenge.
The original article's [author-uploaded full text](https://www.researchgate.net/publication/7191089_A_Commutativity_Theorem_for_Normal_Operators) was then inspected as extracted text: Section 1, **Theorem I, printed p. 35**, including its hypotheses and adjoint conclusion.
The original proof was not re-audited.

Theorem I assumes a bounded operator \(B\) and a normal operator \(N\), which may be unbounded, on a Hilbert space.
From \(BN\subseteq NB\), it obtains commutation with the spectral projections and, in particular, \(BN^*\subseteq N^*B\).
The statement imposes no separability or tracial assumption.
Set \(B=T\) and restrict to bounded \(N\): all four products have domain \(H\), so both inclusions become equalities.
Its conclusion is exactly \([N^*,T]=0\).
Thus **Fug50, Theorem I, p. 35** directly supplies the stated bounded result without an additional project argument.

[Sun14](https://www.imsc.res.in/~sunder/fug.pdf), Theorem 0.1, p. 1, was inspected as an initial identification aid.
Its standing convention assumes separability.
Its reference page range differs from the PMC record, which supplies the bibliography used here.

## Proof evidence and application

The project's existing [Yin_C_F0005 review](../../reviews/Yin_R_F0004_v1.md) and [Yin_C_F0013 review](../../reviews/Yin_R_F0063_v1.md#affiliated-criterion-finding) independently checked the exponential/Liouville proof.
That historical evidence remains available.
This pass does not attribute the exponential method to Fug50 or re-audit Sunder's different proof.

In the [Yin_C_F0005 commutant argument](../../../claims/Yin_C_F0005_v1.md#yin_c_f0005), \(T=C\) is bounded, each \(N=X_j\) is a bounded normal operator, and Jacobi's identity has already established \([C,X_j]=0\).
The conclusion supplies commutation with the adjoints.
No ledger proof, Claim status or current proof selection changes.
