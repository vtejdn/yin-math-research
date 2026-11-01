---
author: Yin
---

# Ultraweak Closure of Multilinear Balancing Relations

## CS89-U001

## Source and inspection

[Source and edition notes](readme.md).

Source edition: [CS89, published article](../../../literature/pdf/CS89.pdf), Christensen and Sinclair, *On the vanishing of H^n(A,A*) for certain C*-algebras*, Pacific Journal of Mathematics 137(1) (1989), 55--63, DOI 10.2140/pjm.1989.137.55. The article occupies PDF pp.2--10 of the retained publisher PDF;

Passages: Section 2, normal-part construction and Lemma 2.2, printed pp.56--58 / PDF pp.3--5; Lemma 2.3 and its proof, printed p.58 / PDF p.5.

Inspection: Direct text reading on 2026-10-16 by the authoring AI agent for Yin. State: Read. The statements, normal-part interface and substitution below are locally checked and accepted for this scope. Foundational extension and decomposition results are not independently checked; no full-paper audit is claimed.


### Source statements and dependencies

Let R be a von Neumann algebra.
Section 2 associates to every bounded (k+1)-linear form omega on R a normal part omega^n, obtained by extending to R** and restricting along the normal central-summand embedding R -> R**.
Lemma 2.2 states that omega^n is separately ultraweakly continuous and equals omega when omega is already separately ultraweakly continuous.

Lemma 2.3 states the following.
Fix adjacent positions i,i+1 and a subset V of R.
If

\[
 \omega(r_0,\ldots,r_i v,r_{i+1},\ldots,r_k)
 =\omega(r_0,\ldots,r_i,v r_{i+1},\ldots,r_k)
 \quad(v\in V),
\]

then

\[
 \omega^n(r_0,\ldots,r_i a,r_{i+1},\ldots,r_k)
 =\omega^n(r_0,\ldots,r_i,a r_{i+1},\ldots,r_k)
 \quad(a\in\overline V^{\mathrm{ultraweak}}).
\]

The other arguments are arbitrary elements of R.
The source assumes no selfadjointness or multiplicative closure of V.
It concludes closure of this subset, rather than generation of an algebra.
The proof first establishes the relation on V for omega^n using the bounded net approximating the normal central projection, then uses separate ultraweak continuity.
For a form already separately ultraweakly continuous, the result is the direct closure of its balancing relation.

The foundational extension result cited as [13, Theorem 5.3, p.402] and the normal/singular decomposition cited as [15] were not independently checked.
The local reading does not audit their proofs or the paper's cohomology results.

### Hilbert-space map application

Let R act normally on a Hilbert space H, and let T:R -> H be a bounded ultraweak-to-weak continuous linear map.
Use the inner product linear in the second variable.
For eta in H, define

\[
 \omega_\eta(r,z):=\langle r^*\eta,Tz\rangle
 \qquad(r,z\in R).
\]

This is a bounded bilinear form, separately ultraweakly continuous: the first variable gives a vector functional and the second uses the continuity of T.
If T(az)=aTz for every a in a subset V and every z in R, then

\[
 \omega_\eta(ra,z)=\langle r^*\eta,aTz\rangle
 =\omega_\eta(r,az).
\]

Lemmas 2.2--2.3 extend this identity to a in the ultraweak closure of V.
Setting r=1 and testing against every eta gives T(az)=aTz on that closure.
In particular, if the relation is known on a unital starred algebra, it extends to the generated von Neumann algebra.

This source supplies the closure step.
It does not, by itself, turn commutation with normal generators into commutation with their adjoints, or prove continuity from closability of T on a Hilbert-space domain.
Those are distinct inputs.
In the already continuous case, applying the source introduces bilinear-form and normal-part notation in place of a direct continuity argument.
