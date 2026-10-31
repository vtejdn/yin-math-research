---
author: Yin
---

# F0001 Citation Applications

The current TeX in `paper/` is authoritative for the citation uses recorded here.
Each row is one source-specific use of a citation that appears in the current manuscript; grouped TeX citations have separate entries under each cited work.
The canonical bibliography owns bibliographic fields, and the linked U or other fixed source record owns source statements, inspected editions and source-review limits.
This map records only current citation applications, not consulted or uncited works.

## `ACSY24`

Source evidence: [ACSY24-U001](../../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) records the derivation and actual adjoint-domain condition in the published Proposition 3.5, pp.34--36, with its source-review limits.
[ACSY24-U003](../../audits/literature/ACSY24/Yin_U003.md#derivation-adjoint-and-compression) checks Lemma 3.3's adjoint-domain equivalence on a weakly dense starred algebra, without a reality assumption.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/conjugate-variable-criterion.tex`, introduction to `def:conjugate-variables` | `\cite[Proposition~3.5]{ACSY24}` | Identifies the adopted derivation and actual adjoint-domain condition used in the definition of conjugate variables; it does not supply the manuscript's rationality criterion. |
| `paper/sections/conjugate-variable-criterion.tex`, `lem:conjugate-liberation` proof | `\cite[Lemma~3.3]{ACSY24}` | The actual vacuum adjoint puts the dense algebraic tensor product in the adjoint domain, so each conjugate derivation is closable. The Neumann-series domain check and the proof of nonatomicity are given directly in the manuscript; maximal Delta and Proposition 3.5 are not used for this step. |

## `AP18`

Source evidence: [AP18-U001](../../audits/literature/AP18/Yin_U001.md#ap18-u001) checks Theorem 2.3.1, and [AP18-U002](../../audits/literature/AP18/Yin_U002.md#ap18-u002) checks the tracial commutant and Section 8.4 trace interfaces.
The [AP18-U003, affiliation and domains](../../audits/literature/AP18/Yin_U003.md#affiliation-interface), [square-integrable affiliated-operator interface](../../audits/literature/Miy26/Yin_U004.md#miy26-u004), and [AP18-U002 v2, canonical-conjugation reading](../../audits/literature/AP18/Yin_U002.md#tomita-foundational-reference) retain additional Section 7 evidence at their own scopes.
The inspected artifact is the undated 338-page author draft; 2018 is not a verified draft date.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, setting paragraph before `def:fraction-pair` | `\cite[Theorem~7.3.2]{AP18}` | Identifies \(L^2(\M,\tau)\) with square-integrable affiliated operators in the tracial setting, so that \(H\otimes_{\C}H\subseteq L^0(\M)\otimes_{\C}L^0(\M)^{\mathrm{op}}\); Subsection 2.4 uses this identification for the tensor realization. |
| `paper/sections/conjugate-variable-criterion.tex`, `lem:gradient-liberation` proof | `\cite[Theorem~2.3.1]{AP18}` | Kaplansky density supplies uniformly bounded approximants from the individual algebra \(\mathcal P_i=\operatorname{Alg}(A_i,B_i)\); the two local norm bounds and weakly closed graphs put \(\M\Omega\) in the domains of the actual contraction closure and its adjoint. |
| `paper/sections/dual-system-criterion.tex`, `lem:module-commutation` proof | `\cite[Theorem~2.3.1]{AP18}` | Supplies a uniformly bounded net from the generated unital \(*\)-algebra for the module-commutation extension. |
| `paper/sections/preliminaries.tex`, `subsec:rational-affiliated` | `\cite[Section 7.2]{AP18}` | Supports the definition of affiliation by commutation with commutant unitaries, including domain invariance. |
| `paper/sections/preliminaries.tex`, Hilbert--Schmidt setup in `subsec:finite-rank-tensors` | `\cite[Section 8.4]{AP18}` | Supports the ordinary trace on \(\B(H)\); it is distinct from the canonical trace on a general module commutant. |
| `paper/sections/preliminaries.tex`, `subsec:finite-rank-tensors` | `\cite[Section~7.1.1]{AP18}` | Supplies the tracial standard-representation conjugation \(J(x\Omega)=x^*\Omega\), with the exact construction retained in the linked source record. |

## `BD78`

Source evidence: the [selected source-interface record](../../audits/literature/BD78/readme.md#f0001-derivation-extension-20261012) records Section 2.1, equation (4), and its bimodule-valued derivation scope.
The inspected locator is the published 1978 version; the source record does not claim a whole-paper audit.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/preliminaries.tex`, `subsec:free-field` | `\cite[Section~2.1, (4), pp.~298--299]{BD78}` | Supports unique extension of polynomial free difference quotients to the free field; the algebraic tensor target is separately cited to KV12. |

## `Coh06`

Source evidence: [Coh06-U001](../../audits/literature/Coh06/Yin_U001.md#coh06-u001) records the division-closure terminology.
The specific universal-localization statements were read in the [BD78 source-interface record](../../audits/literature/BD78/readme.md#f0001-derivation-extension-20261012), which records Cohn's exact edition locators and limits.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/preliminaries.tex`, `subsec:free-field` | `\cite[Corollary~7.5.14]{Coh06}` | Identifies the free field as a universal division ring of fractions; no broader localization consequence is inferred from the corollary alone. |
| `paper/sections/preliminaries.tex`, `subsec:free-field` | `\cite[Theorem~7.5.13 and Corollary~7.5.14]{Coh06}` | Supplies the universal localization at full square matrices used in the free-field description. |

## `Coh71`

Source evidence: [Coh71-U001](../../audits/literature/Coh71/Yin_U001.md#coh71-u001) checks the definition and its ambient setting in Section 7.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/preliminaries.tex`, paragraph after `def:rationality` | `\cite[Section~7]{Coh71}` | Supports the related rational-closure terminology; the manuscript defines division closure separately. |

## `Coh85`

Source evidence: [Coh85-U001](../../audits/literature/Coh85/Yin_U001.md#coh85-u001) checks the division-closure definition and its unital convention.
The source intake's [rational-closure comparison](../../audits/literature/Coh85/Yin_U001.md#rational-closure-comparison) records the matrix-inverse definition, containment and stated possibility of strict containment; the exercise's proof tasks and examples were not audited.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/preliminaries.tex`, `def:rationality` | `\cite[Exercise~7.1.4]{Coh85}` | Supports the ambient-algebra definition of division closure. |
| `paper/sections/preliminaries.tex`, paragraph after `def:rationality` | `\cite[Exercise~7.1.4]{Coh85}` | Supports Cohn's stated comparison, including the possibility of strict containment; no exercise proof or example is imported. |

## `Con94`

Source evidence: [Con94-U001](../../audits/literature/Con94/Yin_U001.md#con94-u001) records both the Section IV.5 conjecture and the Section IV.3 operator statement, including their distinct scopes.
The inspected artifact is the registered electronic book; its pagination is not asserted to match every printed edition.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, Connes motivation paragraph | `\cite[Section IV.5, Remark 3]{Con94}` | Supports Connes's free-group rationality conjecture and its finite-rank forward implication; the converse is explicitly a conjecture there. |
| `paper/sections/introduction.tex`, operator formulation in the same paragraph | `\cite[Section IV.3, Proposition 1]{Con94}` | Supports the Hardy-projection commutator formulation on the circle; the manuscript does not attribute this operator statement to Kro81. |

## `CS05`

Source evidence: [CS05-U001](../../audits/literature/CS05/Yin_U001.md#cs05-u001) checks the relative-\(\Delta\) definitions, generator-boundary interface, and Theorem 4.11 within its recorded scope.
The [generator-boundary source check](../../audits/literature/MSY23/readme.md#hochschild-source-check) records the inspection of Section 3.1.1, equations (3.1) and (3.6), in the same arXiv v1.
[CS05-U002](../../audits/literature/CS05/Yin_U002.md#cs05-u002) checks Section 1.1, equations (1.1)–(1.2) and the Hilbert–Schmidt extension in the retained arXiv v1, printed/PDF p. 3.
For these Section 1.1 citations, the paper's \(\Theta\) is the source's \(\Psi\), with the second \(H\) factor identified linearly with its opposite and \(\rho(a)=Ja^*J\).
The source begins with bounded tensor factors; Subsection 2.4 restricts its Hilbert-space extension to algebraic \(L^2\) tensors to obtain all bounded finite-rank operators.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, opening of Subsection 1.1 | `\cite{CS05}` | Gives the historical source for introducing \(\Delta\) through von Neumann-algebra homology; this is not a novelty claim. |
| `paper/sections/introduction.tex`, immediately before `def:psi` | `\cite[Section~3.1.1, equation~(3.1)]{CS05}` | Identifies the right multiplication maps as coordinate components of the source's generator boundary. Definition 1.3 enlarges the coefficient algebra from \(\mathcal M\otimes_{\mathbb C}\mathcal M^{\mathrm{op}}\) to \(L^0(\mathcal M)\otimes_{\mathbb C}L^0(\mathcal M)^{\mathrm{op}}\), preserving the multiplication order and sign. The locator is p.19 in the inspected arXiv v1; the citation supplies the formula, not the manuscript's rationality criterion. |
| `paper/sections/maximal-delta.tex`, `rem:boundary-interpretation` after the proof of `thm:delta` | `\cite[Section~3.1.1, equation~(3.1)]{CS05}` | Supports restricting the degree-one boundary to the generator span with the stated coefficient bimodule. |
| `paper/sections/preliminaries.tex`, `def:delta` | `\cite{CS05}` | Supports the Hochschild \(1\)-cycle interpretation of the finite-rank tuples. |
| `paper/sections/preliminaries.tex`, `def:delta` | `\cite{CS05}` | Supplies the source definition of \(\Delta\); the paper also follows MSY23 Section 3. |
| `paper/sections/preliminaries.tex`, `def:delta` | `\cite[Definition~2.10]{CS05}` | Supplies the general tracial von Neumann module-dimension definition alongside Luc02's named terminology. |
| `paper/sections/preliminaries.tex`, `eq:theta` and its Hilbert–Schmidt extension | `\cite[Section~1.1, equation~(1.1)]{CS05}` | Supplies the rank-one tensor representation and its Hilbert-space isometry. The paper uses \(H\otimes_{\mathbb C}H\) for all bounded finite-rank operators and records the bounded-factor specialization at `eq:theta-bounded`. |
| `paper/sections/preliminaries.tex`, the \(\Theta\) bimodule actions and `eq:tensor-commutator` | `\cite[equation~(1.2)]{CS05}` | Supplies all four tensor-factor actions. The paper combines them and subtracts the two right-multiplication identities with its existing generator-first commutator convention. |

## `CS77`

Source evidence: [CS77-U001](../../audits/literature/CS77/Yin_U001.md#cs77-u001) checks Proposition 1 and the bounded-map specialization, not a closable-domain or von Neumann-closure theorem.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/dual-system-criterion.tex`, `lem:normal-intertwining` | `\cite[Proposition~1]{CS77}` | Supplies adjoint intertwining for the stated bounded map \(\M\to H\); later module extensions are separate local arguments. |

## `Dab10`

Source evidence: [Dab10-U002](../../audits/literature/Dab10/Yin_U002.md#dab10-u002) retains the selfadjoint contraction-method interface and its scope.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/conjugate-variable-criterion.tex`, `lem:gradient-liberation` proof | `\cite[proof of Lemma~12]{Dab10}` | Provides the contraction-method model for the general liberation estimate. The manuscript retains the nonzero coassociativity defect, proves the analytic-unitary approximation and checks both actual bounded-vector domains locally; it does not invoke a coassociative estimate without its hypotheses. |

## `DR97`

Source evidence: [DR97-U003](../../audits/literature/DR97/Yin_U003.md#dr97-u003) checks Theorem 7's finite-generator inverse-closure conclusion and its proof repairs.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, free-group criterion paragraph | `\cite[Theorem 7]{DR97}` | Supports the finite-generator converse and equality of rational and division closures; the manuscript states \(d\geq1\) and makes no arbitrary-rank extension. |

## `Fug50`

Source evidence: [Fug50-U001, bounded commutation](../../audits/literature/Fug50/Yin_U001.md#bounded-commutation) records the primary-source identity, Theorem I statement, bounded specialization and proof-review limits.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/dual-system-criterion.tex`, direct classical commutation sentence before `lem:normal-intertwining` | `\cite[Theorem~I, p.~35]{Fug50}` | For bounded \(S\) and bounded normal \(N\), the source's \(SN=NS\) implication yields \(SN^*=N^*S\); the original proof was not re-audited. |

## `Hun74`

Source evidence: [Hun74-U002](../../audits/literature/Hun74/Yin_U002.md#hun74-u002), [Hun74-U004](../../audits/literature/Hun74/Yin_U004.md#hun74-u004), and [Hun74-U005](../../audits/literature/Hun74/Yin_U005.md#hun74-u005) record the division-ring basis, coordinate-map and balanced-tensor interfaces.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/preliminaries.tex`, `lem:equalizer` proof | `\cite[Theorem~IV.2.4]{Hun74}` | Extends the right-linearly independent pair to a basis over the division ring. |
| `paper/sections/preliminaries.tex`, `lem:equalizer` proof | `\cite[Theorem~IV.2.1 \& Theorem~4.11]{Hun74}` | Supplies the coordinate-map linearity needed for the local tensor-separation map; no analytic continuity is inferred. |
| `paper/sections/preliminaries.tex`, `lem:equalizer` proof | `\cite[Definition~IV.5.1 and Theorem~IV.5.2]{Hun74}` | Supplies the balanced algebraic tensor construction; the displayed nonvanishing conclusion is the manuscript's specialization. |

## `Kat95`

Source evidence: [Kat95 selected citation check](../../audits/literature/Kat95/readme.md) records the retained 1995 reprint, Problem III.5.18, and the distinction between its problem statement and the local application.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/liberation-dual-system-criterion.tex`, `lem:finite-closure` | `\cite[Problem~III.5.18]{Kat95}` | Cites the statement that a closable finite-rank operator is bounded; the problem's proof is not supplied by the cited passage. |

## `Kro81`

Source evidence: [Kro81-U001](../../audits/literature/Kro81/Yin_U001.md#kro81-u001) reconstructs the coefficient rationality criterion in the retained 1897 collected edition.
That edition was not collated with the original 1881 printing, and the citation does not claim priority.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, Connes motivation paragraph | `\cite{Kro81}` | Identifies the scalar Kronecker rationality criterion behind the analogy; Con94 is separately cited for the operator formulation. |

## `KV12`

Source evidence: [KV12 source record](../../audits/literature/KV12/readme.md) checks the retained arXiv v2 statements, the algebraic tensor target, and the opposite-factor conversion.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/preliminaries.tex`, `subsec:free-field` | `\cite[Section~4.4, Definition~4.4 and Corollary~4.11]{KV12}` | Supplies an explicit construction of the extended difference quotients on noncommutative rational functions with algebraic tensor-product values, alongside the unique-extension result cited to BD78; no completed tensor or analytic domain is imported. |

## `Lin00`

Source evidence: [Lin00-U001](../../audits/literature/Lin00/Yin_U001.md#lin00-u001) records the source theorem statement and fraction conventions, and [Lin00-U002](../../audits/literature/Lin00/Yin_U002.md#lin00-u002) reconstructs its finite-generator proof chain.
All theorem and section locators below refer to the retained arXiv v1, not the journal pagination.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, Linnell criterion paragraph | `\cite[Theorem 1.1]{Lin00}` | Supports the affiliated-operator fraction criterion in the finite-generator free-group setting. |
| `paper/sections/preliminaries.tex`, `def:fraction-terminology` | `\cite[Section~1]{Lin00}` | Supports the common-denominator terminology for finite families. |
| `paper/sections/preliminaries.tex`, final paragraph of Subsection 2.3, `subsec:rational-affiliated` | `\cite[Theorem~1.1]{Lin00}` | Supports the characterization of rational affiliated operators by finite-rank conditions on bounded operators obtained from left and right fractions, in the finite-generator free-group setting; the following Miy22 sentence gives the semicircular analogue. |
| `paper/sections/preliminaries.tex`, paragraph before `lem:clearing` | `\cite[Section~1, p.~2 of the arXiv version]{Lin00}` | Supplies the finite-family common-denominator interface; the manuscript proves its own induction. |

## `Luc02`

Source evidence: [Luc02-U001](../../audits/literature/Luc02/Yin_U001.md#luc02-u001) checks §8.2.1 fraction terminology in the retained book manuscript.
It does not record inspection of Definition 1.10; the named module-dimension locator remains an identified source-inspection gap.
The general tracial-algebra dimension construction has its separately cited CS05 support.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/preliminaries.tex`, `def:fraction-terminology` | `\cite[Section~8.2.1]{Luc02}` | Supplies the left/right fraction terminology. |
| `paper/sections/preliminaries.tex`, `def:delta` | `\cite[Definition~1.10]{Luc02}` | Gives the manuscript's named terminology locator, whose primary-source inspection is not established by retained Luc02-U001; the general tracial-algebra construction is separately linked to CS05. |

## `Mai15`

Source evidence: [Mai15-U001 v2](../../audits/literature/Mai15/Yin_U001.md#mai15-u001) checks the actual adjoint-domain multiplication and real adjoint identities in the retained arXiv version.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/conjugate-variable-criterion.tex`, `lem:conjugate-liberation` proof | `\cite[Lemma~4.3]{Mai15}` | Supplies the actual polynomial tensor-adjoint formula yielding \((\gamma_i^\circ)^*(1\otimes1)=[X_i^*,\xi_i]\) for \(\gamma_i^\circ=\Psi_i\partial_i\). No reality of \(\partial_i\) is assumed. |
| `paper/sections/conjugate-variable-criterion.tex`, `lem:gradient-liberation` proof | `\cite[Lemmas~4.6--4.7]{Mai15}` | Supplies the real-adjoint and dense tensor-adjoint-domain identities for \(\delta_i=\mathrm i\gamma_i\), after reality is established on \(A_i,B_i\). These imply closability and the actual core-adjoint formula; the energy estimate and both full bounded-vector domain extensions are proved locally. |

## `Miy22`

Source evidence: [Miy22-U005](../../audits/literature/Miy22/Yin_U005.md#miy22-u005), [Miy22-U006](../../audits/literature/Miy22/Yin_U006.md#miy22-u006), and [Miy22-U007](../../audits/literature/Miy22/Yin_U007.md#miy22-u007) retain the bounded theorem, fraction interfaces and affiliated rationality theorem.
The inspected work is the 24-page 2022 journal PDF; its original foundations remain at the stated unit scopes.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, semicircular criterion paragraph | `\cite[Theorems 3.1 and 4.5]{Miy22}` | Supports the semicircular bounded and affiliated rationality criteria. |
| `paper/sections/preliminaries.tex`, `def:fraction-terminology` | `\cite[Lemma~4.1]{Miy22}` | Supplies the two-element common-denominator construction. |
| `paper/sections/preliminaries.tex`, final paragraph of Subsection 2.3, `subsec:rational-affiliated` | `\cite[Section~4]{Miy22}` | Supplies the semicircular analogue of the preceding Lin00 rationality criterion, using the cleared expressions with bounded right annihilation operators; \(\Gamma[Q,r_i^*]\) is the manuscript's notation for these expressions. |
| `paper/sections/preliminaries.tex`, paragraph before `lem:clearing` | `\cite[Lemma~4.1]{Miy22}` | Supplies the two-element step iterated in the manuscript's finite-family proof. |
| `paper/sections/preliminaries.tex`, `lem:common` proof | `\cite[proof of Lemma~4.1]{Miy22}` | Identifies the source construction of a common multiple; the displayed fraction argument is checked locally. |

## `MSY23`

Source evidence: [MSY23-U002](../../audits/literature/MSY23/Yin_U002.md#msy23-u002), [MSY23-U003](../../audits/literature/MSY23/Yin_U003.md#msy23-u003), [MSY23-U004](../../audits/literature/MSY23/Yin_U004.md#msy23-u004), and [MSY23-U005](../../audits/literature/MSY23/Yin_U005.md#msy23-u005) retain the finite-rank, free-field, affiliated-algebra and bounded-dual interfaces.
These units inspect the 50-page published article; their proof and external-input limits remain as recorded.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, opening paragraph | `\cite[Theorem 1.1]{MSY23}` | Gives the maximal-\(\Delta\) free-field realization context, not the manuscript's new commutator criterion. |
| `paper/sections/introduction.tex`, free-group criterion paragraph | `\cite[Proposition 6.3]{MSY23}` | Provides a bounded-dual example for free Haar unitaries; the source convention's sign is stated in the manuscript. |
| `paper/sections/introduction.tex`, paragraph after Theorem 1.4 | `\cite[Theorem~1.1]{MSY23}` | Supplies the division-ring property used in the \((5)\Rightarrow(1)\) interpretation of the maximal-\(\Delta\) criterion. |
| `paper/sections/examples.tex`, `rem:normality` | `\cite[Proposition~6.2]{MSY23}` | The bounded dual D with [c,D]=P_Omega gives Delta(c)=1 directly; the source allows arbitrary bounded tuples and requires no normality. |
| `paper/sections/maximal-delta.tex`, proof of `thm:delta` | `\cite[Theorem~1.1, (i) and (v)]{MSY23}` | Identifies the evaluated free field with the affiliated division closure under \(\Delta(X)=d\). |
| `paper/sections/preliminaries.tex`, `subsec:rational-affiliated` | `\cite[Section 5.1]{MSY23}` | Supports affiliation through commutation with commutant unitaries, including domain invariance. |
| `paper/sections/preliminaries.tex`, paragraph after `eq:canonical` | `\cite[Section 5.1]{MSY23}` | Supports the affiliated functional-calculus and polar-decomposition facts used to construct a fraction pair. |
| `paper/sections/preliminaries.tex`, `def:rationality` | `\cite[Definition~4.10]{MSY23}` | Supports the division-closure definition in the specified ambient algebra. |
| `paper/sections/preliminaries.tex`, paragraph after `def:rationality` | `\cite[Definition~4.7]{MSY23}` | Supports the rational-closure definition by entries of matrix inverses. |
| `paper/sections/preliminaries.tex`, paragraph after `lem:free-field` | `\cite[Theorem~1.1 and Remark~5.10]{MSY23}` | Supports equality of rational and division closures under maximal \(\Delta\). |
| `paper/sections/preliminaries.tex`, paragraph after `def:regular` | `\cite[Lemmas 5.1--5.2]{MSY23}` | Supports regularity's equivalence with injectivity and dense range in the finite tracial setting. |
| `paper/sections/preliminaries.tex`, `def:delta` | `\cite[Section~3]{MSY23}` | Supports the finite-rank-cycle presentation of \(\Delta\). |
| `paper/sections/preliminaries.tex`, `subsec:free-field` | `\cite[Section~4.1 and Theorem~4.1]{MSY23}` | Supports the free-field convention and universal division-ring identification. |
| `paper/sections/preliminaries.tex`, paragraph before `rem:cycle-characterization` in `subsec:delta-tensor-maps` | `\cite{MSY23}` | Points to the source's finite-rank characterization and free-field realization, made precise by the following citations. |
| `paper/sections/preliminaries.tex`, `rem:cycle-characterization` | `\cite[Section~3 and Remark~3.2]{MSY23}` | Supplies the equivalence between maximal \(\Delta\), vanishing cycles and the commutator-kernel condition. |
| `paper/sections/preliminaries.tex`, `lem:free-field` | `\cite[Theorems 1.1, 3.1 and 5.6]{MSY23}` | Supplies the free-field embedding and image identification under maximal \(\Delta\). |
| `paper/sections/preliminaries.tex`, Tomita-conjugation paragraph in `subsec:finite-rank-tensors` | `\cite[p.~13]{MSY23}` | Supports the Tomita-conjugation terminology; the tensor identification is separately attributed to CS05. |

## `Voi98`

Source evidence: [Voi98-U002](../../audits/literature/Voi98/Yin_U002.md#voi98-u002), [Voi98-U005](../../audits/literature/Voi98/Yin_U005.md#voi98-u005), and [Voi98-U006](../../audits/literature/Voi98/Yin_U006.md#voi98-u006) record the conjugate-variable, dual-system, Fock-model and Fisher-information passages.
The inspected source is the published 39-page article; the exact proof repairs and source limits remain in those units.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, introduction to `def:dual-system` | `\cite[Definition~5.1]{Voi98}` | Gives the original bounded selfadjoint dual-system formulation for selfadjoint generators, with a coefficient algebra and commutators \([X_j,Y_i]=\mathrm i\delta_{ij}P_\Omega\). Taking the coefficient algebra to be \(\mathbb C1\) and setting \(D_i=-\mathrm iY_i\) gives the manuscript's generator-first normalization in that setting. The joint “see also” citation does not attribute the manuscript's arbitrary-generator and unbounded-domain variant to Voi98; the common domain and adjoint-domain assumptions are local. The published Definition 5.1 is on p.208 and is checked in Voi98-U005. |
| `paper/sections/examples.tex`, `rem:normality` | `\cite[5.13]{Voi98}` | Supplies the standard free semicircular Fock model; the circular counterexample and rationality conclusion are local. |
| `paper/sections/preliminaries.tex`, `subsec:free-field` | `\cite[Section~3, pp.~192--193]{Voi98}` | Supplies the polynomial free-difference-quotient convention before its separately cited free-field extension. |

## `Wei94`

Source evidence: [Wei94-U001](../../audits/literature/Wei94/Yin_U001.md#wei94-u001) checks Section 9.1.1's chain differential and the coefficient bimodule convention.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/maximal-delta.tex`, `rem:boundary-interpretation` after the proof of `thm:delta` | `\cite[Section~9.1.1, p.~300]{Wei94}` | Supplies the degree-one Hochschild differential notation \(d_1\); the manuscript's coefficient bimodule is specified locally. |

## `Voi99`

Source evidence: [Voi99-U001](../../audits/literature/Voi99/Yin_U001.md#voi99-u001) checks the published Section 13, pp.160–161, including Definition 13.1 and the bounded selfadjoint commutation conditions.
The [gradient and adjoint unit](../../audits/literature/Voi99/Yin_U003.md#voi99-u003) checks 5.3--5.5 and Proposition 6.1, including the word-moment extension to von Neumann closures and the sign \(\gamma_i^*(1\otimes1)=-j_i\).
The [information unit](../../audits/literature/Voi99/Yin_U004.md#voi99-u004) checks Definition 9.1 and its finite-coordinate norm convention.
The [full-source audit](../../audits/literature/Voi99/readme.md) retains the inspected edition, complete coverage and source corrections.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, immediately before `def:liberation-dual-system` | `\cite[Definition~13.1]{Voi99}` | Identifies the source of the liberation commutation pattern. The manuscript definition is a domain variant for arbitrary tuples \(X\in\mathcal M^d\), with \(\mathcal M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*\). The source requires bounded selfadjoint operators. Neither definition imposes vacuum normalization. The manuscript additionally defines a normalized system by its sum being P_Omega on M Omega; this condition and the normalization construction in Lemma 4.1 are local and are not attributed to Voi99. For a general tuple, the manuscript specifies the displayed generator commutators; it does not assert additional adjoint-generator or von Neumann subalgebra relations. The citation supplies no existence theorem for the manuscript's variant and no replacement for its analytic estimates. |
| `paper/sections/conjugate-variable-criterion.tex`, introduction to `def:liberation-gradients` | `\cite[5.3--5.4 and Proposition~6.1]{Voi99}` | Supplies the liberation prescriptions, gradient moments and signed actual-adjoint characterization. The manuscript adopts the L2 case on each algebra \(\mathcal P_i=\operatorname{Alg}(A_i,B_i)\), and explicitly requires well-definedness of the represented derivations. |
| `paper/sections/conjugate-variable-criterion.tex`, after `def:liberation-gradients` | `\cite[Definition~9.1]{Voi99}` | Identifies the sum of squared coordinate-gradient norms with liberation Fisher information relative to scalars; finiteness does not supply the nonatomicity imposed separately in Proposition 6.3. |
| `paper/sections/conjugate-variable-criterion.tex`, `lem:conjugate-liberation` proof | `\cite[Remark~5.5(c)]{Voi99}` | Extends the polynomial word-moment formula to the coordinate von Neumann algebras by bounded Kaplansky approximation. The current round checked the published pp.115--116 directly. The descent through represented relations and the actual adjoint pairing on every \(p\in\mathcal P_i\) are proved locally, so the source's initial algebraic-freeness convention is not silently assumed. |
