---
author: Yin
---
# Keh25-U001: product compactness for pointwise Hilbert bounds

<a id="keh25-u001"></a>
## Source and inspection

[Source and edition notes](readme.md).

Source edition: Christoph Kehle, Introduction to Functional Analysis, MIT18.102 Spring 2025 notes dated May 2025, the registered 76-page [Keh25.pdf](../../../literature/pdf/Keh25.pdf).
No new edition or artifact was acquired.

Passages: Proposition 1.21, printed/PDF p.7; Theorem 1.22 and proof, p.8; weak topology definitions and Propositions 4.4--4.5, pp.42--43; Theorem 4.12 and proof, p.44.

Inspection: 2026-10-14T21:27: direct local PDF text reading of the statements and the displayed product/FIP and Banach--Alaoglu proofs by the general research branch for Yin.
Standard statements and exact applicability accepted.
This is not an independent whole-source audit, and Zorn's lemma and prior topological foundations are not re-audited.


## Exact accepted interfaces

Proposition 1.21 characterizes compactness by nonempty intersection for every family of closed sets with the finite intersection property.
Theorem 1.22 supplies compactness of an arbitrary product of compact spaces in the product topology; only nonempty compact factors are used here.
The printed proof uses a maximal finite-intersection family and coordinate compactness.

Theorem 4.12 says the closed unit ball of the continuous dual of a normed space is weak-star compact.
Its displayed proof embeds the dual ball into a product of compact scalar discs, checks equality of the weak-star and induced product topologies, and imposes the linearity equations as closed conditions.
The weak topologies are defined through the continuous scalar functionals in the preceding section.

The previously accepted Hilbert representation theorem in the same inspected source, Theorem 5.17 on printed/PDF p.53, identifies a Hilbert space with its continuous dual, with the conjugation adjustment appropriate to the complex inner-product convention.
Thus every finite-radius closed Hilbert ball is weakly compact.
The weak topology on that Hilbert ball corresponds to the weak-star topology on the dual ball because all its scalar inner-product coordinates correspond, up to complex conjugation, to evaluations.

## Application and limits

The [D_F0003 pointwise-radius criterion](../../../drafts/Yin_D_F0003.md#an-exact-pointwise-radius-criterion-for-bare-full-domain-duals) uses a product of these weak compact balls indexed by a finite coordinate index and all bounded input vectors.
Complex linearity and the rank-one commutator identities are finite-coordinate weakly closed constraints.
Its finite-intersection argument is proved in that responsible draft.

These standard compactness inputs do not produce the required pointwise radii.
They do not turn arbitrary finite solvability into a Hilbert-valued global solution or imply an operator-norm bound.
No sequential compactness, separability or countable-index reduction is asserted.
This is a reused foundational source interface, not a new project compactness theorem.
