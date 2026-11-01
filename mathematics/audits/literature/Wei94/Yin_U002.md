---
author: Yin
---

# The tensor-algebra bimodule resolution of length one

## Wei94-U002

Source: [Wei94, retained Chapter 9](../../../literature/pdf/Wei94--chapter-9.pdf), the 1994 book's Cambridge Core chapter PDF hosted by MIT.
Inspection: 2026-10-15, the ACSY-to-full-domain exploration agent for Yin, direct statement and local proof checking; self-review, not an independent source audit.

### Inspected statement and proof mechanism

Proposition 9.1.6, printed pp.303–304 / PDF pp.4–5, considers the tensor algebra T=T(V) of a module V over a commutative ground ring k.
Its proof uses the exact sequence of T-bimodules

\[
0\longrightarrow T\otimes_k V\otimes_k T
 \mathop{\longrightarrow}^{d}T\otimes_k T
 \mathop{\longrightarrow}^{\mu}T\longrightarrow0,
\qquad
d(t\otimes v\otimes t')=tv\otimes t'-t\otimes vt',
\]

where mu is multiplication.
The source concludes that Hochschild homology vanishes outside degrees zero and one, and obtains the degree-one exact sequence with boundary b(m tensor v)=mv-vm.
The subsequent explicit cyclic-word formula for coefficients T is not used here.

The proof identifies the image of d with the kernel of multiplication and asserts injectivity by the word-degree decomposition.
The omitted check is elementary and was checked here: at total word length n, the domain has one copy of V to the tensor power n for every position of the distinguished letter (n copies), while the codomain has one for every division into a left and right word (n+1 copies).
The map is the successive-difference map of a path, which is injective over any k-module and whose image is the kernel of the summation map.
Taking the direct sum over n proves exactness, including n=0.
This verifies the local mechanism without any von Neumann-algebra or Hilbert-domain assertion.

For k=C all three tensor products are algebraic.
Choosing a vector-space basis of V makes the first two terms free modules over the enveloping algebra, hence projective.
Lemma 9.1.4 and Corollary 9.1.5 on printed p.303 were also read: they distinguish the source's relative homology from absolute Tor/Ext and justify the field specialization.
The general relative-homological formalism was not reaudited.

### Exact interface and limits

The retained interface is the displayed bimodule resolution, with its stated multiplication order.
The exact sequence is also split as a sequence of right T-modules because mu has right-module section t mapped to 1 tensor t.
Consequently tensoring it over its right T-action with any left T-module preserves exactness.
This immediate specialization is used in the [module-splitting investigation](../../../drafts/Yin_D_F0003.md#algebraic-module-splitting-does-not-erase-the-range-obstruction).

A resolution of length one does not say that Ext to the power one vanishes, that every module is projective or injective, or that a linear map taking values in an algebraic dual takes values in a Hilbert space.
The project-specific rank-one extension and those limitations belong to the linked draft.
No result about full-domain dual systems is attributed to Weibel.

The inspection covers the proposition's statement, the displayed resolution, its local proof and the field specialization.
It does not cover the full chapter, all consequences of Proposition 9.1.6, the earlier bar-resolution formalism, whole-book errata or a formal proof assistant.
Existing Wei94-U001 retains its earlier, separate definition-level scope.

## Source and inspection

[Source and edition notes](readme.md).

Source edition: Wei94, 1994 book; retained Cambridge Core Chapter 9 PDF hosted by MIT, 69 pages, as registered.

Passages: Proposition 9.1.6 and its proof, printed pp.303–304 / PDF pp.4–5; Lemma 9.1.4 and Corollary 9.1.5, printed p.303 / PDF p.4.

Inspection: Direct extracted-text statement and local proof inspection on 2026-10-15; the word-degree injectivity check and field specialization were verified. Self-review only, with the explicit limits above.
