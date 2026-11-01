---
author: Yin
---

<a id="lin00-u004"></a>
# Lin00-U004: External Inputs, Generator Scope, and Version Evidence

Inspected edition: [Yin's source notes](readme.md#yin-edition).

- Source: [Lin00](../../../literature/pdf/Lin00--arxiv-v1.pdf), arXiv:math/9907075v1, submitted 1999-07-12; seven pages, with printed and PDF page numbers equal.
- Locator: introductory assertions and definitions pp. 1-3; Lemma 2.3 pp. 4-5; the DR97 input and bounded regularization in the proof of Theorem 1.1 p. 6; bibliography p. 7.
- Record: 2026-10-10, interface reviewer under Yin.
  This unit records primary-source interface checks and comparisons with existing source audits.
  It does not claim a recursive proof audit of the cited books and papers.

## The bounded input supplied by DR97

For a free group $G=F_X$, let $W=W(G)$, let $P:\ell^2(G)\to\ell^2(E)\oplus\mathbb C$ be the tree unitary, and denote the amplified action on the target by $a^+$.
The precise input needed by Lin00 is

$$
\{a\in W:Pa-a^+P\text{ has finite rank}\}
=\operatorname{Div}_{C_r^*(G)}(\mathbb CG)
=\operatorname{Rat}_{C_r^*(G)}(\mathbb CG).
$$

Here division closure uses inverses of single elements, while rational closure uses entries of inverses of finite matrices.
The source introduces $S(G)$ using the latter convention on p. 3, then identifies the two closures by DR97.
They must not be identified merely by giving them the same name.

For **finite $X$**, this interface is supplied by [DR97-U002](../DR97/Yin_U002.md#dr97-u002), [DR97-U003](../DR97/Yin_U003.md#dr97-u003), and [DR97-U004](../DR97/Yin_U004.md#dr97-u004), with their recorded corrections and accepted external inputs.
In particular, Proposition 5 converts the tree defect into finite residual dimension, and Proposition 9 realizes the resulting square-summable rational series as a bounded element of scalar inverse closure.
This also establishes the bounded criterion for elements initially in $W$, not only for those already known to belong to $C_r^*(G)$.

DR97 uses zero action on the auxiliary scalar summand, whereas Lin00 prescribes identity action.
For each bounded $a$, the two target actions differ by the rank-one scalar projection.
Thus their bounded defects differ by a finite-rank operator and give the same bounded criterion.
This comparison does not make Lin00's identity-summand assignment additive; [U002](Yin_U002.md#lin00-u002) and [U003](Yin_U003.md#lin00-u003) retain the correction in calculations where it matters.

Lin00's English statement on p. 3 says only that $G$ is free, without requiring finite rank; p. 2 explicitly discusses arbitrary Hilbert direct sums.
The existing DR97 audit is deliberately restricted to finitely many generators.
Its finite-residual bound contains the factor $2|X|$, and its formal recognizable/rational equivalence cannot simply be applied to an infinite alphabet.
Consequently that record alone does **not** discharge Lin00's bounded input for an arbitrary-rank free group.
Neither density of finite-support polynomials nor a directed union of finitely generated subgroups suffices: a general bounded group operator can involve infinitely many generators, and finite-rank commutation has to force the required reduction before such an argument can be used.

The present unit therefore accepts the displayed bounded input at finite generator rank.
The proof of Lin00's unbounded theorem may also be read conditionally on that input for a larger free group.
No counterexample to the arbitrary-rank theorem is asserted, and the missing reduction is not silently treated as an established consequence of the finite-generator audit.
The domain argument in U003 itself works for arbitrary sums once its summability condition and the bounded input are supplied.

## Affiliated-operator foundations and the trace step

Lin00 cites Berberian's 1982 article, Theorems 1 and 10, for the regular ring and left/right fraction descriptions, and Dieudonne's book, Section 15.12.6, for the bounded regularization used on p. 6.
Those original proofs were not read in this audit.
An attempted Project Euclid fetch of the Berberian article returned an access-challenge HTML page, not a PDF; it supplies no mathematical inspection evidence.

The already primary-checked [AP18 interface in Miy26-U004](../Miy26/Yin_U004.md#miy26-u004), Theorem 7.2.8 in the author-hosted 338-page draft, gives the $*$-algebra structure of closed affiliated operators for a finite tracial von Neumann algebra, with closure used for sums and products.
This accepted foundational input applies to $W(G)$; factor assumptions are unnecessary.
Standard spectral and polar decomposition, used at their finite-tracial scope, then give the bounded regularizers, regular-denominator injectivity and dense range.
U001 explicitly constructs common left and right denominators using affiliated rows and columns; U002 checks the fraction manipulations and regularization.
Thus the inaccessible historical citation is not treated as a completed proof audit.
AP18's foundational proof remains outside the present inspection.

For Lemma 2.3, the original statement of Lin91, Linnell's 1991 *Zero divisors and group von Neumann algebras*, Lemma 12, printed pp. 356-357, was directly checked in the [publisher PDF](https://msp.org/pjm/1991/149-2/pjm-v149-n2-p09-p.pdf), PDF pp. 9-10.
For projections $e,f\in M_n(W(G))$ with disjoint principal right ideals, it gives $\operatorname{Tr}e+\operatorname{Tr}f=\operatorname{Tr}(e\vee f)$.
This statement has no amenability assumption.
Its relation to the trace-dimension argument, not the paper's separate zero-divisor theorem, is the relevant issue here.
This is an independent consistency and attribution check, not an additional proof premise: U002 supplies the finite-family polar-decomposition argument needed for the distinct-eigenvalue projections.
The 1991 proof's cited weak-isomorphism theorem was not recursively audited.
U002 also corrects the source's placement of an unbounded $u-\lambda$ in $W(G)$.

These are retained foundations with stated scope.
They do not turn every lemma quoted in Berberian, Dieudonne, AP18 or the 1991 article into an independently checked result.

## The division-ring and free-field assertions are separate

Lin00 p. 3 cites Lin93, Linnell's 1993 *Division Rings and Group von Neumann Algebras*, Theorem 1.3, and p. 573.
The primary journal pages were directly inspected in the Gottingen digitization: [printed p. 562](https://gdz.sub.uni-goettingen.de/content/PPN481110151_0005/800/0/00000566.jpg) and [printed p. 573](https://gdz.sub.uni-goettingen.de/content/PPN481110151_0005/800/0/00000577.jpg).

Theorem 1.3 gives a division ring between $\mathbb CG$ and $U(G)$ when $G$ is torsion free with a normal free subgroup and elementary amenable quotient.
Taking that subgroup to be $G$ checks the free-group application.
Page 573 explicitly identifies the division ring generated by a free subgroup with the universal field of fractions of its group algebra, using finitely generated subgroups and a directed union.
These passages verify the reported statements; the proof chain through Hughes and Lewin was not audited.

Theorem 1.1's finite-rank proof defines $D(G)$ as division closure and establishes $D(G)=R(G)$ through inverse closure and bounded regularization.
It does not need the additional assertion that $D(G)$ is a division ring, or its identification with a universal free field.
The 1993 statements therefore supply context and interpretation, rather than a missing premise in that proof.
The directed-union argument for the division-ring property does not establish the arbitrary-rank **bounded finite-rank criterion** discussed above.
Historical originality beyond these explicit source attributions was not investigated.

## Relation to DR97 and Miy22

**DR97's free-group tree model** and **Miy22's finite semicircular Fock model** have related bounded proofs.
Their respective commutators control coefficient residuals; finite residual dimension leads to a finite matrix representation and an analytic rational realization.
Their coefficient bases and commutator operators are different.
This comparison does not identify bounded and unbounded operator criteria.
The precise comparison is already recorded in [DR97-U005](../DR97/Yin_U005.md#dr97-u005) and [Miy22-U003](../Miy22/Yin_U003.md#miy22-u003).

Lin00 supplies the intervening free-group extension to affiliated operators.
Its proof uses bounded fractions, independence of those fractions, algebraic closure operations and bounded regularization.
Miy22 follows this unbounded strategy in the semicircular setting, with right annihilation/creation operators replacing the tree unitary; see [Miy22-U006](../Miy22/Yin_U006.md#miy22-u006), [Miy22-U007](../Miy22/Yin_U007.md#miy22-u007), and [Miy22-U008](../Miy22/Yin_U008.md#miy22-u008).
This relationship does not identify the two operator models or their unbounded domains.

The source's comment after Theorem 1.1, that a test involving only $sPb-aPt$ might suffice, records an unproved possibility at the time of writing.
Neither that comment nor the bounded block equivalence authorizes deleting $sP^{-1}b-aP^{-1}t$ from the unbounded theorem.
No present-day open-problem or priority claim is made.

## Version and search evidence

The [arXiv record](https://arxiv.org/abs/math/9907075) was checked on 2026-10-10.
It lists only v1, submitted 1999-07-12, and still describes the seven-page version as intended for Comptes Rendus.
The retained artifact is that preprint, not a nine-page journal PDF.
The [publisher record](https://www.sciencedirect.com/science/article/pii/S0022123699935267) identifies the eventual JFA publication as volume 171, issue 1, 2000, **115-123**, DOI 10.1006/jfan.1999.3526.
The preprint's publication comment does not alter that bibliographic record.

A bounded search used the exact title with `PDF`, `erratum`, `correction` and `corrigendum`, and inspected the [author's research page](https://personal.math.vt.edu/linnell/research/index.html).
The page, whose displayed revision date is 2016-02-06, lists five other hard-to-find papers and no alternate Lin00 version.
Direct publisher page/PDF requests returned HTTP 403.
No journal PDF, revised author version or correction notice was obtained.
The search therefore does not establish whether the journal printing corrects any issue in the preprint; inspection and corrections in U001-U003 remain version-specific.
It also does not establish the nonexistence of an erratum.

Supporting-source inspection used the publisher's 1991 PDF and two primary 1993 page scans.
The coordinator subsequently retained the validated [Lin91 PDF](../../../literature/pdf/Lin91.pdf).
A ResearchGate journal-PDF record was located but direct download returned HTTP 403; a later bounded publisher-PDF request returned zero bytes.
The usable Lin93 evidence came from the library scans; only that selected online source scope was inspected.
Failed responses and rendering byproducts are not article artifacts.
No author contact, source modification, formal verification or external human review occurred.

## Independent cross-review performed

On 2026-10-10 the interface reviewer independently read the complete U003 reconstruction.
The review checked the common subspace $L=sN=SN$, both exact domain inclusions, equality of inverse values, the two finite-codimension inverse images in the converse, the infinite-sum correction, and the nonadditive scalar convention.
No local implication gap was found.
This checks U003's argument subject to its explicit Theorem 1.1 input; it does not remove the generator-scope limitation of that input.

The same reviewer independently checked the complete U002 reconstruction: the row-operator trace bound, both denominator changes, signs of the rank-one correction terms, scalar closure before reduction to invertible factors, compatible multiplication fractions, the corrected telescoping sum, the two adjoint defects, the bounded block equivalence, and both regularized fractions.
These calculations pass under the stated foundational inputs and bounded DR97 criterion.
In particular, this review does not use Lin00's separate free-field assertion to prove its rationality criterion, or assume that a finite-rank commutator already has a finitely generated group support.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Lin00, arXiv:math/9907075v1, 1999-07-12, seven-page retained preprint. Published JFA pagination 115-123 is separately verified bibliographic metadata; no journal/preprint identity comparison was completed. |
| source-locator | Lin00 pp. 1-3 introductory and closure assertions, pp. 4-5 Lemma 2.3, p. 6 bounded input and regularization, p. 7 references. DR97-U002-U004 and Miy22-U003/U006-U008 retain their original source locators; supporting primary passages are specified in the body. |
| inspection | 2026-10-10: exact bounded-input and generator-scope comparison, primary 1991 Lemma 12 and selected 1993 statements, version/access search, relationship to Miy22, and independent review of the complete local reconstructions in U002 and U003. External foundational original proofs, arbitrary-rank DR97 extension, and journal/preprint comparison remain outside the verified scope. |
