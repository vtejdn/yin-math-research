---
author: Yin
---
# Literature on actual conjugate-variable derivations and their domain consequences

Date: 2026-10-16.
Yin requested a directed literature search and an inventory of retained sources concerning condition A.
Root coordinated three parallel source-reading branches, checked the retrieved artifacts and assembled this comparison.
This is a literature synthesis and collection check, not a new mathematical proof, independent proof review or resumption of autonomous Task execution.
The [T_F0011 contract](../tasks/Yin_T_F0011_v1.md#contract) supplies the exact comparison question.

## Exact condition and scope of the collection

Let $(M,\tau)$ be finite tracial, let $X=(X_1,\ldots,X_d)$ be bounded generators, and put $H=L^2(M,\tau)$ and $\mathcal P=\mathbb C\langle X,X^*\rangle$.
Condition A requires complex-linear outer-bimodule derivations
\[
 \partial_i:\mathcal P\subset H\longrightarrow H\otimes_2H,
 \qquad \partial_i(X_j)=\delta_{ij}1\otimes1,
 \qquad 1\otimes1\in\operatorname{Dom}\partial_i^*.
\]
The last condition concerns the actual Hilbert adjoint on the represented starred algebra.
Neither normality nor reality is imposed.
The values on $X_j^*$ must respect the represented relations but are not separately prescribed by this display.

The selected collection contains 29 works covering the direct condition, its selfadjoint specialization, domain mechanisms, maximal-Delta consequences, Stein comparisons and relevant concrete models.
At the end of this search, all 29 have bibliography entries and 28 have a retained complete source; Voi99 remains unavailable locally.
Eight works were newly registered: Mai15, MSW17, FN17, CFM20, Nel17, KSW23, Kum23 and Yan24.
Eleven previously registered works gained retained sources: Dab10, Dab14, CS05, Shl04, Voi02, BM20, DI16, GS14, SS15, CS16 and Shl24.
Dab14 has separately retained published and arXiv artifacts, so this batch added 20 PDFs for 19 works.
The counts here describe this dated comparison.

## Direct definition, dual and domain sources

| Source | Exact interface and relationship to A | Retained source and inspection boundary |
| --- | --- | --- |
| [ACSY24](../audits/literature/ACSY24/readme.md) | Section 3.2, Theorem 3.4 and Proposition 3.5, published pp.34--36: the full general starred-core condition, canonical closable duals, and maximal $\Delta(X)=d$. No normality or reality premise. | [Published PDF](../literature/pdf/ACSY24.pdf); existing U001 and U004 preserve the exact domain statements and reconstruction; U008 owns the full-source assessment. |
| [Voi98](../audits/literature/Voi98/readme.md) | Section 3, especially Definition 3.1 and Lemma 3.3, and Section 4: selfadjoint conjugate variables, actual vacuum adjoints and closability. Section 5 supplies bounded-dual conventions and examples. | [Published PDF](../literature/pdf/Voi98.pdf); existing U002/U004/U005 give precise selected coverage. The source's bounded/selfadjoint dual convention is not automatically the general unbounded one. |
| [Shl06](../audits/literature/Shl06/readme.md) | Theorem 1 and Corollary 2, preprint pp.3--4: conjugate variables and normalized closable implementers. The initial generating tuple is selfadjoint; ACSY24 explains the starred-core generalization. | [Abel Symposium preprint](../literature/pdf/Shl06--abel-preprint.pdf), 9 pages; existing U001--U004 retain formula corrections and proof limitations. |
| [Mai15](../audits/literature/Mai15/readme.md) | Definition 4.1, Lemma 4.3 and the first part of Lemma 4.7, pp.22--26: general actual adjoint-domain multiplication and dense algebraic-tensor adjoint domain. The latter implication does not use reality. | [arXiv v2](../literature/pdf/Mai15--arxiv-v2.pdf), 44 pages; new U001 checks these interfaces and selected pairings. Theorem 4.9's stronger estimates require reality and coassociativity. |
| [Dab10](../audits/literature/Dab10/Yin_U002.md) | Lemmas 10 and 12 and Remark 11, arXiv pp.8--9: selfadjoint finite-Fisher contraction estimates and the stronger Lipschitz-to-bounded-dual interface. | [arXiv v2](../literature/pdf/Dab10--arxiv-v2.pdf), 12 pages; existing U002 reconstructs the full bounded-vector domains with its recorded review. |
| [MSW17](../audits/literature/MSW17/readme.md) | Theorem 2.5, p.7, and Lemmas 3.3--3.4, p.12: selfadjoint conjugate relations descend to well-defined derivations, exclude algebraic relations and give two contraction estimates. | [arXiv v2](../literature/pdf/MSW17--arxiv-v2.pdf), 26 pages; new U001 records selected reading. The earlier finite-Fisher preprint arXiv:1407.5715 is a precursor, not this retained artifact. |
| [CN21](../audits/literature/CN21/readme.md) | Section 3, Lemma 3.1: actual derivations and the Jacobian adjoint; Theorem 2.10 instead concerns a closed module/dimension. | [arXiv v2](../literature/pdf/CN21--arxiv-v2.pdf), 22 pages; existing U001 includes the restriction and vacuum-projection boundary. |
| [CN25](../audits/literature/CN25/readme.md) | Section 1.3 and Lemma 1.1, pp.3--5: $\operatorname{Der}_{1\otimes1}$, general non-real derivations, actual vacua and evaluation on generators. | [arXiv v2](../literature/pdf/CN25--arxiv-v2.pdf), 22 pages; existing U001 records additional restrictions and extension hypotheses. |

For selfadjoint $X$, A is the usual existence of an $L^2$ conjugate system, equivalently finite non-microstates free Fisher information for a finite tuple.
For general $X$, A imposes prescribed values only on the selected $d$ generators inside a represented starred algebra.
It is not automatically finite Fisher information for a list of $2d$ formally independent coordinates $(X,X^*)$.
Likewise, membership of the relevant coordinate vector in a closure used to define Stein dimension does not supply a derivation with that exact coordinate value and an actual vacuum adjoint.

The selfadjoint estimates in Dab10 and MSW17 are of the form
\[
 \| (\mathrm{id}\otimes\tau)\partial_i(p)\|_2\le C_i\|p\|,
 \qquad
 \|(\tau\otimes\mathrm{id})\partial_i(p)\|_2\le C_i'\|p\|.
\]
They use the operator norm on the input.
They must not be reported as $L^2\to L^2$ boundedness, nor as estimates for every general non-real A derivation.
The present search found no source statement supplying these estimates for all arbitrarily correlated normal tuples under only A.
This is a bounded-search outcome, not a theorem that no such result exists.

## Maximal Delta, rationality and regularity consequences

| Source | Interface and exact boundary | Retained source |
| --- | --- | --- |
| [CS05](../audits/literature/CS05/readme.md) | Section 3.1.1, (3.9)--(3.13), Theorem 4.11: finite-rank boundaries, relative Delta and bounded duals. The source theorem's selfadjoint setting and local arbitrary-tuple interpretation remain distinguished. | [arXiv v1](../literature/pdf/CS05--arxiv-v1.pdf), 39 pages; existing selected U001. |
| Shl04 | Derivation/dual estimates for non-microstates entropy dimension and q-semicircular families; background to the Delta and dual mechanisms, not a general A-to-full-domain theorem. | [arXiv v1](../literature/pdf/Shl04--arxiv-v1.pdf), 13 pages; acquisition and topical screening only in this round. |
| [MSY23](../audits/literature/MSY23/readme.md) | Published Theorems 3.1, 5.6, 5.25 and Proposition 6.2: maximal Delta, full-matrix invertibility, free-field realization and the finite-rank cycle argument. | [Published PDF](../literature/pdf/MSY23.pdf), 50 pages; existing U001--U006. Public arXiv pagination is different. |
| [CMM+24](../audits/literature/CMM+24/readme.md) | Section 2.5, Theorem 16, arXiv p.15: general-coordinate Delta and its free-family additivity, used by ACSY24. Freeness is an additional hypothesis. | [arXiv v4](../literature/pdf/CMM+24--arxiv-v4.pdf), 27 pages; existing U001. |
| [Miy22](../audits/literature/Miy22/readme.md) | Theorems 3.1 and 4.5 and Proposition 4.12: bounded and affiliated rationality criteria for a free semicircular system. This is a particular model satisfying A. | [Published PDF](../literature/pdf/Miy22.pdf), 24 pages; existing U001--U009 retain the inspected scopes and corrections. |
| SS15 | Theorem 3.4, arXiv p.8: normal freely independent variables and the Atiyah property. Neither general A nor its necessity is asserted. | [arXiv v1](../literature/pdf/SS15--arxiv-v1.pdf), 25 pages; existing MSY23 source records contain selected comparison reading. |
| CS16 | Earlier preprint title *Regularity of Polynomials in Free Variables*; Conjecture 5(b), arXiv p.4, and entropy-dimension regularity form the comparison background to MSY23. | [arXiv v2](../literature/pdf/CS16--arxiv-v2.pdf), 10 pages; earlier selected reading remains separate from publication-version coverage. |
| BM20 | Selfadjoint finite-Fisher and stronger Lipschitz-conjugate assumptions yield quantitative regularity of polynomial distributions. This is an application of the selfadjoint specialization, not an equivalence with general A. | [arXiv v3](../literature/pdf/BM20--arxiv-v3.pdf), 33 pages; abstract/setting screening in this collection, with the actual contents transcribed. |
| [Shl24](../audits/literature/Shl24/Yin_U001.md) | *Regularity questions in free probability*, printed pp.1272--1275: a modern exposition of the selfadjoint derivative/dual-commutator formula. | [Complete OWR report](../literature/pdf/Shl24--owr-report.pdf), 58 pages, containing the whole contribution on PDF pp.46--49; existing U001 covers only the stated selected passages. |

The direct published chain for general A is ACSY24 Proposition 3.5 followed by the maximal-Delta/free-field interfaces of MSY23.
That chain does not identify every raw fraction commutator on its full natural domain with an intrinsic boundary representative.
The unrestricted correlated-normal full-bounded-vector domain question of T_F0011 is not closed by the literature checks in this account.

## Stronger hypotheses, Stein comparisons and concrete models

| Source | Relation to A and inspection scope | Retained source |
| --- | --- | --- |
| Voi02 | Survey of free entropy and conjugate-variable foundations; an expository entry, not a substitute for the exact original hypotheses. | [arXiv v1](../literature/pdf/Voi02--arxiv-v1.pdf), 31 pages; acquisition and topical screening. |
| [Dab14](../audits/literature/Dab14/Yin_U001.md) | Definition 1, published p.1405, imposes Lipschitz conjugates; Section 2.2.1 keeps additional coassociativity and regularity assumptions. This is stronger than selfadjoint A. | [Published PDF](../literature/pdf/Dab14--published.pdf), 52 pages, and [arXiv v3](../literature/pdf/Dab14--arxiv-v3.pdf), 57 pages; existing selected audits are version-specific. |
| DI16 | Theorem 1.3, preprint p.3: structural consequences under selfadjoint Lipschitz conjugates. General derivation results retain their real/unbounded/nonamenability assumptions. | [arXiv v1](../literature/pdf/DI16--arxiv-v1.pdf), 31 pages; selected statement comparison, not a whole-paper audit. |
| [GS14](../audits/literature/GS14/Yin_U001.md) | Analytic conjugates close to a semicircular system give free monotone transport; a substantially stronger regularity and perturbative setting. | [arXiv v3](../literature/pdf/GS14--arxiv-v3.pdf), 37 pages; existing source-specific reading has its own scope. |
| [FN17](../audits/literature/FN17/readme.md) | Definition 1.8, p.7: a general matrix Stein kernel pairing with a Jacobian. A variable kernel does not imply the fixed identity/vacuum condition of A. | [arXiv v1](../literature/pdf/FN17--arxiv-v1.pdf), 20 pages; new selected definition record, no whole HSI proof audit. |
| [CFM20](../audits/literature/CFM20/readme.md) | Definition 1.1, p.1, and Theorem 2.1, p.5: Stein kernels under the stated centering condition. Their existence is not a replacement for actual coordinate conjugates. | [arXiv v1](../literature/pdf/CFM20--arxiv-v1.pdf), 10 pages; new selected definition/statement record. |
| [MS23](../audits/literature/MS23/readme.md) | All-q finite-dimensional selfadjoint q-Gaussian conjugate and dual constructions, with Lipschitz regularity; the real-symmetric mixed-Q range has explicit bounds on its parameters. | [Published PDF](../literature/pdf/MS23.pdf) and [arXiv v3](../literature/pdf/MS23--arxiv-v3.pdf); existing U001--U008. |
| [Nel17](../audits/literature/Nel17/readme.md) | Definitions 3.4--3.5, p.12: actual conjugates for derivations and the nonselfadjoint convention $\delta_a(a^*)=0$. The general setting is nontracial with modular assumptions. | [arXiv v3](../literature/pdf/Nel17--arxiv-v3.pdf), 41 pages; new selected definition record, no full factoriality proof audit. |
| [KSW23](../audits/literature/KSW23/readme.md) | Section 1 and Proposition 1.4: q-Araki--Woods models, initially covariance-normalized derivatives and actual dual-adjoint vacuum membership. A tracial specialization and normalization must be checked before using A. | [arXiv v4](../literature/pdf/KSW23--arxiv-v4.pdf), 11 pages; selected setting/statement reading. |
| [Kum23](../audits/literature/Kum23/readme.md) | Theorem 3.4 and Corollary 3.5: mixed q-Araki--Woods conjugates under the stated real-symmetric parameter and orthogonal-action hypotheses. General vacuum states are nontracial. | [arXiv v2](../literature/pdf/Kum23--arxiv-v2.pdf), 22 pages; selected setting/statement reading; full Lipschitz proof not audited. |
| [Yan24](../audits/literature/Yan24/readme.md) | Theorem 4.3, pp.22--23: finite-dimensional twisted Araki--Woods conjugates for compatible braided crossing-symmetric twists of norm below one. Traciality is a separate specialization. | [arXiv v2](../literature/pdf/Yan24--arxiv-v2.pdf), 33 pages; selected setting/statement reading, not a full combinatorial proof audit. |

The three Araki--Woods papers are retained as explicit model and nontracial extension literature.
They do not supply an unqualified theorem for arbitrary finite-tracial normal tuples satisfying A.
Similarly, the general actual-derivation framework in CN21/CN25 is useful for formulating A, but its module closure and dimension conclusions must not be promoted into existence of prescribed actual derivations.

## Remaining unavailable source

Voi99, *Liberation and Mutual Free Information*, is registered but its selected full text is still unavailable.
ACSY24 cites it for unitary-density and free-extension inputs, so the gap is relevant to the construction of examples.
The earlier publisher acquisition failed.
On 2026-10-16 the reader checked the [Berkeley author page](https://math.berkeley.edu/~dvv/), [author publication list, item 41](https://math.berkeley.edu/~dvv/Publications.pdf), and exact-title searches restricted to Berkeley/arXiv.
The bibliographic identity was confirmed but no verifiable public author full-text URL was found.
No new publisher failure is claimed, no theorem from an unseen full text was newly accepted, and no source-contents transcription was invented.
This does not show that a public copy does not exist.

## Search coverage and stopping boundary

The search first matched exact titles, authors, DOI/arXiv identifiers and existing U records, including suffix-named artifacts rather than only same-key filenames.
External searches used combinations of conjugate variables, free Fisher information, actual vacuum adjoint, closable derivations, dual systems, non-selfadjoint/normal tuples, free Stein irregularity/dimension, maximal Delta, free field, rationality, and q-/mixed-/twisted-Araki--Woods models.
The principal backward chain was ACSY24 to Shl06 and Mai15, together with Voi98, Dab10 and MSW17.
The contemporary branches were CN21/CN25 and the 2023--2024 conjugate-system constructions.
Metadata were checked at original arXiv records, author pages and publisher records; search-engine crawl dates were not treated as publication dates.
The source-specific units distinguish statements, selected proof steps and prior reviews; this survey does not enlarge their recorded scope.

The search stops at a coherent direct chain and its useful neighboring formulations, with the one actual source-access gap above.
It does not claim to enumerate every paper mentioning free Fisher information or to have checked every forward citation through 2026.
No verified new general-A theorem from 2026 was found in this bounded search.
Future work should consult the retained source interfaces before attempting new domain estimates; only a concrete new lead or a changed question calls for reopening the search.
