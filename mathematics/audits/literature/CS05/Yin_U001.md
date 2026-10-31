---
author: Yin
---
# CS05 relative Delta and bounded dual systems

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## CS05-U001

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | [CS05, author-hosted 39-page copy](https://alainconnes.org/wp-content/uploads/betti.pdf), *L2-homology for von Neumann algebras*. No identity with the journal typesetting is asserted. |
| source-locator | Lemma 2.16, printed/PDF p.18; Section 3.1.1, p.19; equations (3.7)--(3.13), pp.21--22; Theorem 4.11 and its proof, p.33. Printed and PDF page numbers coincide in this artifact. |
| inspection | 2026-10-14. Root AI agent for Yin inspected these statements, surrounding conventions, the annihilator argument, and the complete short proof of Theorem 4.11. State: Audited within this specified scope, with standard finite von Neumann module dimension properties accepted. This is source inspection by the authoring agent, not an independent project review or a full-paper audit. |

## Exact source scope

Section 3.1.1 assumes a finite self-adjoint generating set: membership of x entails membership of x*.
This does not mean that every displayed element is individually selfadjoint.
The source then introduces absolute and relative Delta via closures of finite-rank commutator cycles in equations (3.9), and via projected transpose ranges in (3.12)--(3.13).
The map sigma(B)=JB*J sends left multiplication by x to right multiplication by x.

For a tuple F of length n and an enlargement F' of length n+m, the relative cycle formula subtracts from n the dimension of the intersection of the HS closure of the F' cycles with HS^n direct-sum zero.
The closure is taken BEFORE intersection with the first-coordinate subspace.
It cannot be replaced by the closure of finite-rank cycles having identically zero final coordinates.
The latter would merely recover the absolute quantity.

Theorem 4.11 assumes bounded duals D_j with [D_j,X_i]=delta_ij P_1 and Hilbert-Schmidt commutators [D_j,Y_k].
It concludes that both the relative and absolute quantities are n.
The proof obtains coordinate copies of P_1 in the projection of the full commutator range; their bimodule spans are dense in HS^n.
The proof mechanism uses boundedness and the Hilbert-Schmidt side commutators; it does not invoke normality or the generation hypothesis after the module formulation is in place.

## General-tuple applicability and pairing correction

Lemma 2.16 uses the complex bilinear pairing sum Tr(T_j B_j) on finite-rank tuples and bounded tuples.
Its WOT annihilator argument applies without selfadjoint coefficients.
When converting this pairing to the Hermitian HS inner product, coordinatewise adjoints must be inserted.
For an arbitrary tuple Z, if K_Z is the HS closure of cycles sum[T_j,rho(Z_j)]=0 and C_Z is the WOT closure of ([B,rho(Z_j)]) intersected with HS, the exact identity is C_Z=(K_{Z*})^perp.
Componentwise adjoint exchanges K_Z and K_{Z*}, and preserves module dimension through the trace-preserving factor flip.
Thus the numerical dimension identities survive.
It would be inaccurate to assert C_Z=K_Z^perp for arbitrary Z without this adjustment.

The local general-tuple statement and complete argument use precisely this adjustment.
The source is credited for the relative definition and the bounded-dual proof mechanism.
The original theorem remains a self-adjoint-family statement; the local argument is an explicit extension, not a newly discovered mechanism.

## Literature comparison and search boundary

The retained [MSY23](../../../literature/pdf/MSY23.pdf), published 50-page version, was checked directly at pp.12--13 and 47--48: it defines absolute Delta for arbitrary tuples and Proposition 6.2 proves bounded dual implies maximal absolute Delta without normality or generation.
Its Section 6.2 expressly adapts the earlier selfadjoint argument to general tuples.
The existing [MSY23-U002](../MSY23/Yin_U002.md) and [MSY23-U005](../MSY23/Yin_U005.md) retain the wider verified interfaces.
A targeted text search in that artifact found no separate relative-Delta theorem.

On 2026-10-14 targeted public searches combined Connes--Shlyakhtenko, relative Delta, dual system, non-selfadjoint, and Theorem 4.11, and followed the primary MSY author/publication pages.
The checked sources provide the original relative mechanism and the arbitrary-tuple absolute case.
No separately stated arbitrary-tuple relative theorem was located in this bounded search.
This finding is not an exhaustive literature claim, a priority claim, or evidence that no such statement exists elsewhere.

Source roles: CS05 is attribution and the verified mechanism being extended; MSY23 supplies the already published general absolute formulation and comparison.
Neither source is cited as having stated the new full relative formulation verbatim.

## Retained 2026-10-11 Hochschild convention check

<a id="hochschild-source-check"></a>
Hochschild terminology follow-up, 2026-10-11: MSY23 published p.13 explicitly calls the finite-rank tuples Hochschild 1-cycles and refers to [18], CS05, for the homological setting; it does not develop the chain-complex identification there.
The coordinating agent directly checked the [author-hosted CS05 preprint](https://alainconnes.org/wp-content/uploads/betti.pdf), arXiv math/0309343v1, 39 pages: Sections 1.1 and 2.2.3 (operator actions), Section 2.3, equation (2.8) (bar boundary), and Section 3.1.1, equations (3.1), (3.6), and (3.8) (generator boundary, commutator identification and finite-rank kernel).
These are preprint locators, not asserted locators in the journal edition.
For the right-multiplication anti-representation rho on tracial L2, the coefficient bimodule action a.S.b = rho(b) S rho(a) gives d_1(sum_i T_i tensor X_i) = sum_i [rho(X_i),T_i].
Thus a tuple with vanishing displayed boundary represents a Hochschild 1-cycle.
This is a selected definition/formula and citation self-review, not a complete CS05 proof audit or a change to the scope of the fixed MSY23-U002 and MSY23-U005 records.
