# Yin: Author-wide Writing Policy

Human: Yin.
These personal defaults apply to Yin's mathematical writing where relevant, including ordinary algebra.
Select the applicable rules through the [four-layer writing hierarchy](../../../framework/rules/preferences.md#scope-and-adoption).
Manuscript and subfield choices override conflicting portions at their own scope; the remaining rules are inherited.

## Default policy

Write Yin's mathematical manuscripts in English by default.
Explain the problem, relevant existing results, precise contribution and main proof mechanism for the intended audience.
Organize the paper around its argument rather than research-log chronology.
Choose wording, theorem organization and proof detail for the actual paper, checking every assertion, reference and contribution claim when adapting a model.

<a id="compilation-and-layout-checks"></a>
## Compilation and Layout Checks

Scope: Yin's manuscript writing.

After compilation, do not render pages or inspect the visual layout unless the user explicitly requests a layout check.
Check the revised source, references and compilation diagnostics as appropriate to the change.

<a id="abstract-concision"></a>
## Concise Abstracts

Scope: Yin's manuscript abstracts.

Keep abstracts as concise as possible and focus on the key information: the central problem and principal results.
Omit secondary technical details and explanatory qualifications that are unnecessary for understanding those results.
Retain assumptions needed for an accurate statement, and leave further technical detail to the introduction or body.

## Manuscript PDF Tracking

Scope: Yin's manuscripts with a primary document at `paper/main.tex`.

Keep the compiled `paper/main.pdf` eligible for Git tracking through a document-local `.gitignore` exception.
This choice covers that PDF only; other PDFs and non-PDF compilation products retain their applicable defaults.
A more specific document choice may override this default.
Eligibility does not instruct an agent to compile, commit, push or publish the document.

## Talks and Slides

The [talk and slide policy](talk&slides.md) records Yin's activity-specific rules and preferences, including the text format for talk abstracts and the on-demand private archive lookup for prior talks and slides.

## Necessary Hypotheses and Special Cases

Scope: Yin's mathematical writing.

State explicitly the necessary hypotheses on which a conclusion depends.
Mention special cases added to emphasize generality only when the current discussion needs them.

<a id="supplementary-remarks"></a>
## Supplementary Remarks

For limitations, possible confusions or related distinctions that merit an independent explanation, usually give a remark with the relevant reasoning or example rather than an isolated reminder in the main text.
Tailor the explanation to the context and intended readership: keep it concise and focused on the main point, retain key information and necessary setup, and omit familiar facts that the current discussion does not need.
Local notation explanations and short comments directly accompanying a formula may remain in the main text.

<a id="proof-readability"></a>
## Proof Readability

Scope: Yin's manuscript writing.

Keep proofs concise and clear while emphasizing readability: a human reader should be able to follow the logical chain easily.
Explain the purpose of a construction and the reason for a consequential inference where these would otherwise be implicit.
Use short transitions and well-placed formulas to connect the steps; do not compress away logical links or add routine calculations that obscure the argument.

Set the level of detail by what the intended reader needs to understand and verify the argument.
A technical fact's use in the reasoning does not by itself require a separate full statement and proof in the manuscript.
Omit routine steps the reader can readily supply and generalizations with no independent expository purpose.
Such omissions must preserve the validity of the argument and keep hypotheses, domains and closure relations explicit whenever they determine the conclusion.

<a id="result-organization"></a>
## Organizing Result Statements

Scope: Yin's manuscript writing.

Use an appropriate theorem, proposition, lemma or corollary environment for a result with independent mathematical content and explicit hypotheses and conclusions, or one that needs repeated reference later.
Keep background, motivation and transitions in ordinary prose; explanations, comparisons and limitations of results may be organized as remarks.
When a result is already stated fully in the introduction, refer to that statement when presenting its proof in the body and avoid unnecessary repetition.

## Progress Reports

Scope: mathematical progress reports written for Yin, including standalone progress manuscripts.

- Present important mathematical results reported as progress in an appropriate theorem, proposition, lemma or corollary environment, with explicit hypotheses and conclusions, following the [result-organization rule](#result-organization).
- Apply the manuscript [four-layer writing hierarchy](../../../framework/rules/preferences.md#scope-and-adoption) to all mathematical content in a progress report: general mathematical writing rules, Yin's author-wide policy, Yin's applicable subfield policy, and the report-specific choices, in increasing order of priority.
  Report-specific choices occupy the manuscript-specific layer.
  Higher applicable layers override only conflicting portions and inherit the remaining rules.

<a id="representative-examples"></a>
## Representative Examples and Abstract Hypotheses

Scope: Yin's manuscript writing.

When the naturalness or applicability of an abstract condition is not readily apparent, use a representative example to explain it.
Make clear how the example fits the theorem's setting, satisfies its key hypotheses and yields conclusions by applying the theorem.
Distinguish properties already known for the example from those obtained by applying the present paper's results.

<a id="terminology-familiarity"></a>
## When a Term May Be Left Unexplained

Scope: Yin's manuscript terminology, using each document's research project and user-designated primary terminology sources.

Unless the user has explicitly exempted the term, do not treat it as familiar enough to leave unexplained if it appears in neither of these source groups:

- The current research project's external Claim-dependency literature, identified through its recorded claim and proof dependencies.
- The primary terminology sources designated by the user for the document or project.

An agent's own familiarity with a term is not an exemption.
A work's presence in the literature directory or an agent's choice of a style exemplar does not by itself put it in either source group.
Check usage in the intended mathematical meaning; occurrence in a source is not by itself sufficient to waive explanation or citation.

For a simple, familiar notion outside these groups, give its usual definition briefly, preferably at first use.
Keep the prose precise and concise; a short background explanation need not become a separate numbered definition or a historical discussion.
Apply the [definition-environment criteria](#definition-environments) when deciding how to present the concept.
Do not require an external search solely to attach a citation to an elementary definition.
For other terms, consider a targeted search for a suitable external reference, and cite the adopted specialized formulation under the [definition-citation rules](#definition-citations).
Check existing source notes and relevant local passages first, then use the [autonomous search policy](../../../framework/rules/literature-search.md#autonomous-literature-search) when needed.
No whole-source audit or exhaustive proof of a term's absence is required; if familiarity is not established, explain the term.

<a id="operator-spaces-and-complete-terminology"></a>
## Operator Spaces and Complete Terminology

Scope: Yin's manuscript writing when introducing an operator or starting an auxiliary operator argument, including in ordinary algebra or free probability when those objects occur.

Use the complete expression "bounded normal operator" rather than "bounded normal"; keep the noun "operator" explicit.
For example, write "Let \(T,N\in\mathcal B(H)\), with \(N\) a normal operator."
The acting space and relevant operator algebra follow the general [ambient-object rule](../../../framework/rules/writing.md#ambient-objects-and-precise-operator-language), including the distinction between membership in \(M\) and \(\mathcal B(H)\).
Once the local setting is explicit, ordinary subsequent references need not repeat it in every sentence.
Applicable subfield or manuscript overrides affect only the conflicting presentation choice and inherit the remaining rules.

<a id="defining-equality"></a>
## Defining Equality

Scope: Yin's mathematical writing.

When defining a symbol, quantity, set, operator or map, use $:=$, including pointwise definitions and local constructions in proofs.
In an equality chain, use $:=$ for the defining step and $=$ for subsequent identities.
Keep $=$ for hypotheses, fraction representations, tuple-coordinate descriptions and proved identities that do not introduce a definition.

<a id="free-field-terminology"></a>
## Free Field Terminology

Scope: Yin's mathematical writing.

Use **free field** as the standard term for the universal division ring of fractions of a free polynomial algebra.
Do not use **free skew field** for this object.

<a id="mathematical-symbols"></a>
## Mathematical Symbols

Scope: Yin's mathematical writing and presentation slides.

| Object | Preferred notation | Meaning and source boundary |
| --- | --- | --- |
| Free field | Use the user's supplied `\moverlay`, `\plangle` and `\prangle` macros to superimpose round parentheses with `<` and `>`, with the coefficient field in front. | Preserve the formal-field/evaluated-division-closure distinction. |
| Affiliated operators | `L^0(\M)`, with `\M=\mathcal M`. | The *-algebra of closed densely defined operators affiliated with the specified finite tracial von Neumann algebra. Sums and products use affiliated closures; this change of notation adds no domain hypothesis. |
| Algebra-generated GNS vectors | `\M\Omega` for the subspace; `x\Omega` for an individual vector with `x\in\M`. | In a tracial GNS space $H=L^2(\M,\tau)$ with $\Omega=1$, $\M\Omega=\{x\Omega:x\in\M\}$ is a dense subspace used for operator domains. Do not call its elements "bounded vectors"; use $\M\Omega$ or say "vectors of the form $x\Omega$ with $x\in\M$." |
| Finite-rank operators | `\F(H)`, with `\F=\mathcal F`. | The finite-rank bounded operators on H, matching MSY23, p. 13. Do not use this symbol as an abbreviation for the evaluated free field. |
| Finite-dimensional Fuglede-Kadison determinant | Use uppercase `\Delta_m(B)=\lvert\det B\rvert^{1/m}` for `B` in `M_m(\mathbb C)`, and the corresponding dimension subscript for other matrix sizes. Do not use lowercase `\delta` for this determinant. | The subscript records the matrix size and the normalized matrix trace. This changes notation only; Dirac masses, Kronecker symbols and unrelated uses of lowercase delta are unaffected. |
| Random-matrix expectation | Write the composite as `\mathbb E\circ\tr_N`, with the composition sign between the expectation and the normalized trace; do not write the bare product `\mathbb E\tr_N`. | The expectation is applied after the normalized trace, so the composition order is visible. This is a notation choice, not a probability-model hypothesis. |

<a id="formula-emphasis"></a>
## Formula Emphasis

Scope: Yin's manuscript writing.

Do not use boxes to emphasize formulas unless the user explicitly authorizes boxed formulas.
Use ordinary displayed equations, numbering and explanatory prose by default.
A request to highlight or foreground a result does not by itself authorize a box.

<a id="display-equation-numbering"></a>
## Display Equation Numbering

Scope: Yin's manuscript writing.

Place displayed equation numbers on the right.
The AMS document classes default to `leqno`, so pass the `reqno` class option explicitly, as in `\documentclass[11pt,reqno]{amsart}`.
Classes that already number on the right, such as `article`, need no option; do not switch them to `leqno`.

<a id="terminology-and-citations"></a>
## Explicit Elementary Exemptions

The terms group and ring need no routine definition or citation merely for the terms themselves.
Unusual conventions still need explanation.
An exemption for a term never exempts an external theorem, proof, construction or historical assertion.
Specialized definitions and ambient objects follow the general [writing rule](../../../framework/rules/writing.md).

<a id="role-index"></a>
<a id="primary-model"></a>
## Models and Algebra Terminology

These choices are author-wide, conditional on the mathematical objects and kind of exposition, not on a free-probability Task label.

| Work | Role and scope | Source observation |
| --- | --- | --- |
| MSY23 | Primary style model for introductions, definitions, theorem statements, proof exposition and transitions. | [MSY23](../../../mathematics/audits/literature/MSY23/readme.md#presentation-observations) |
| Yin20 | Additional style model for background, definitions and detailed exposition. | [Yin20](../../../mathematics/audits/literature/Yin20/readme.md#presentation-observations) |
| ACSY24 | Additional style model for questions, theorem scope and article exposition; MSY23 remains primary. | [ACSY24](../../../mathematics/audits/literature/ACSY24/readme.md#presentation-observations) |
| Hun74 | Algebraic terminology and definitions: modules, bases, Hom, bimodules, algebraic duals and tensor products. Nonexclusive and not a style model. Other chapters require passage-level checking before mathematical use. | [Module and algebraic-dual conventions](../../../mathematics/definitions/index.md#modules-and-algebraic-duals), [balanced tensor products](../../../mathematics/definitions/index.md#balanced-tensor-products) |

The linked source records describe observed practice, not a fifth policy layer.
No work-specific wording restriction was specified for the designated models; the [personal reuse defaults](#source-role-and-reuse-defaults) retain actual reuse permissions, attribution, source versions and inspection limits.
Manuscript-specific LSW24 and SW26b choices remain at their manuscript homes and are not promoted to these defaults.


## Source Role and Reuse Defaults

Yin's explicit designation of a work as a style model authorizes direct reuse and adaptation of its own prose within the authorized scope.
Actual work, section or passage restrictions take precedence; embedded third-party quotations are not covered.
An agent cannot promote another source to style-model status.
A community-reference designation grants no prose-reuse permission: use independently written explanation, while standard terms, notation, formulas and conventional short expressions remain usable.
Existing manuscript-specific permissions retain their scope.
Attribution and mathematical correctness remain separate obligations.

Use stable semantic TeX labels such as `thm:main`, `lem:bounded-dual` and `eq:resolvent`, with `\label` and `\ref` or their package equivalents, rather than manually maintained theorem numbers.

<a id="definition-environments"></a>
## Using Definition Environments

When a concept needs to be defined or recalled, choose its presentation by its role in the argument and the reader's need to understand and reference it.
The existing [background exemptions](../../../framework/rules/preferences.md#scope-and-adoption) remain applicable.

- Use a definition environment for a core concept that enters the main results, underlies the subsequent argument, or needs repeated reference.
  Also consider a separate definition for an established concept with multiple formulations when the adopted version affects the hypotheses or conclusions.
- Ordinary local notation, brief background explanations and auxiliary notions used only locally may remain in prose.
  Permission to explain a simple notion briefly is not a reason to put every definition in ordinary paragraphs.
- Choose the environment independently of whether the concept is new or established; neither a new name nor a numbered definition implies originality.
  Closely related definitions may be organized together.
  Follow the document's existing numbering and [semantic-label convention](../../../framework/rules/writing.md#citations-notation-and-versions), using labels such as `def:main-concept`.
- Write a definition environment without a bracketed optional title: use `\begin{definition}` with its semantic label, not `\begin{definition}[Name]`.
  The name and notation being defined are introduced inside the statement, as [required below](#definition-statements).
  This choice covers definition environments only; bracketed titles on theorem, proposition, lemma, corollary and remark environments are unaffected.
  A source attribution that would otherwise stand in a definition title belongs in the definition body or the adjacent prose, under the [citation rules](#definition-citations).

<a id="definition-statements"></a>
## Stating and Explaining Definitions

For Yin's manuscripts, apply these presentation choices when drafting definitions, whether numbered or given in prose:

- State the objects, ambient structures, parameters, quantifiers and necessary conditions, together with the name and notation being introduced.
  A definition may refer explicitly to a standing setup; do not mechanically repeat assumptions that are already unambiguous there.
- Keep the defining statement focused.
  Motivation may precede it; examples, comparisons between conventions and explanations of scope may follow it in prose or a remark.
- Distinguish the defining conditions from assertions about the resulting objects.
  Existence, well-definedness, equivalence and independence claims that require justification need an argument or a precise applicable citation; placing them in a definition does not establish them.
  Use the existing [reuse-before-proof rule](../../../framework/rules/knowledge-reuse.md#reuse-before-proof) for established inputs.
- Organize these layers for readability.
  A short explanation or immediate verification need not become a separate remark or lemma.
- At first introduction, identify adopted sources, local changes and the scope of local naming under the [definition citation and attribution rules](#definition-citations).
  Those rules govern both numbered definitions and definitions in prose.

<a id="definition-citations"></a>
## Definitions, Citations and Attribution

At the first substantive introduction or use of an established specialized term or definition, give a suitable literature citation unless covered by an [applicable exemption](../../../framework/rules/preferences.md).
Depending on the reader's needs, state the definition, recall the relevant part, or identify the exact convention being adopted.
A citation does not resolve an ambiguity about which formulation is in force.

Apply any actual author or manuscript [terminology-familiarity choice](../../../framework/rules/preferences.md#scope-and-adoption) before leaving a term unexplained.
Use only the background exemptions actually adopted for the document; do not infer additional exemptions merely from an agent's familiarity.
For a simple familiar notion that the rule requires explaining, a concise usual definition may suffice without a source search.
For other terms, check the relevant literature and consider a targeted external search for the formulation to cite.
State unusual conventions even for familiar terms.
Introducing ordinary local symbols does not require a literature attribution.

For specialized definitions, use a checked reference matching the actual purpose: `current formulation`, `notation`, `standard` or `exposition`.
Prefer an exact definition, section or page locator when it identifies the needed version.
A standard reference is sufficient for that purpose; locating the first publication is not a prerequisite for using the definition.

An assertion such as "introduced by", "first proved by" or "due to" is a historical attribution and needs evidence for that assertion.
A reference consulted for exposition or notation does not establish historical priority.
Preserve established names when appropriate, cite the particular definition or theorem used, and do not infer an originator from a name alone.

For a local adaptation, identify the source and explain the mathematical change.
For a genuinely local construction with no adopted external definition, state the construction directly and cite its relevant antecedents where applicable; do not invent a source.
Failure to locate an antecedent is not evidence of originality.

Each citation should serve a specific mathematical or attribution purpose.
Retain accurate sources for core definitions and substantive external results.
For ordinary linear-algebra operations, state the formula directly when it makes the construction and its well-definedness immediate; do not attach a general theorem merely to certify that the operation is available.
This convention does not waive the source requirements for established specialized definitions or nontrivial assertions.

Usually cite a definition once where it is introduced and then refer to the paper's definition or notation.
Repeat or supplement the citation when a different formulation, result or attribution is used, rather than attaching the same reference to every occurrence of a term.

An exemption from defining or citing a **term** does not exempt an external theorem, proof, specific construction or historical claim involving that term from its own source requirements.
Definitions and citation candidates remain at their [existing authoritative locations](../../../mathematics/definitions/index.md); do not reproduce that index in the paper or in this file.

<a id="manuscript-references"></a>
## Manuscript References and Bibliography

Scope: Yin's mathematical manuscripts.

Use the [EMS entry structure, Mathematical Reviews journal abbreviations and cited-items-only rule](../../../mathematics/manuscripts/bibliography-guidelines.md#ems) as the default reference-list convention.
Combine it with the following settings:

- Use alphabetic author–year labels, following the [AMS alphabetic-label model](../../../mathematics/manuscripts/bibliography-guidelines.md#ams).
- Sort the bibliography alphabetically by author, following the [EMS ordering rule](../../../mathematics/manuscripts/bibliography-guidelines.md#ems) and [LMS sorting guidance](../../../mathematics/manuscripts/bibliography-guidelines.md#lms).
  Order works with the same author list chronologically and use a consistent style-generated tie-break when necessary.
- Display given-name initials followed by complete family names, following the [LMS name convention](../../../mathematics/manuscripts/bibliography-guidelines.md#lms).
- Preserve complete available author information in BibTeX, including verified given and family names, name particles and accents.
  Generate initials and labels through the selected bibliography style rather than shortening the stored author information.

Prepare the reference list with BibTeX under the repository's [bibliographic data and typesetting-subset rules](../../../framework/rules/writing.md#citations-notation-and-versions).
Choose a style that implements this combination and check labels, author sorting and name display in its generated bibliography.
Apply the existing [mathematical citation and attribution rules](#definition-citations) to the purpose, placement and source support of citations.

<a id="style-selection"></a>
## Style and Terminology References

Use [style models](../../../framework/rules/writing.md#style-selection) as the preferred writing exemplars.
This collection is primarily for user-authored papers that the user has designated for that role.
Choose the paper or sections most appropriate to the current document; a user-specified primary model takes priority.
Additional models may guide a particular component, such as the introduction or proof exposition, without imposing inconsistent notation.

Consult the responsible author and manuscript choices for an actual primary-model designation.
Apply it at its recorded scope unless the user has made a different document-specific choice.
An empty framework has no implicit primary model.

Apply user-designated primary terminology sources recorded in the document README before using the broader reference collections for terminology choices.
This role may include works from either collection and is separate from the primary style model.
If these sources use different formulations, choose and state the one matching the mathematics; do not infer a priority among them unless the user has specified one.
The designation does not change citation obligations or text-reuse permissions.

Use [community references](../../../framework/rules/writing.md#use-and-reuse) for terminology, notation, statement conventions and the expected level of explanation wherever the user and approved community rules leave a choice.
Select the formulation appropriate to the current mathematics and make it consistent throughout the paper.
If references disagree, record the chosen convention when the difference matters; frequency in a small collection is not proof of community consensus.

Community papers may also guide style.
When no primary style model is designated and no suitable model is available in the preferred collection, choose a relevant community reference as the principal exemplar.
Its text-reuse restrictions remain in force.

Apply the single [four-layer hierarchy](../../../framework/rules/preferences.md#scope-and-adoption) to every writing choice above.
An applicable manuscript choice takes precedence over author-subfield, author-wide and general choices, with partial inheritance.
Source observations supply no independent priority.
Permissions remain bounded by the actual work/passage instruction; no policy designation changes mathematical validity or supplies historical evidence.

<a id="text-reuse"></a>
## Text Reuse and Mathematical Sources

The default for user-designated [style-model texts](../../../framework/rules/writing.md#default-reuse-permission) is direct reuse followed by adaptation as needed.
This permission is already granted for the designated material; do not request permission again for each passage.
Explicit work-specific or passage-specific limitations control the permitted scope.
The collection's entry records those limitations.

For [community-reference texts](../../../framework/rules/writing.md#use-and-reuse), imitate structure, exposition and disciplinary conventions while composing the paper's own prose.
Do not copy their prose verbatim or make a near-verbatim adaptation by changing only a few words.
Standard terminology, conventional notation and the mathematical statements or formulas needed for a properly attributed discussion are not prohibited by this prose restriction.

Permission to reuse wording does not remove the need to cite an adopted mathematical definition, theorem or proof.
Clearly distinguish previous results, including the user's own published results, from the present paper's contributions.
A model's explicit third-party quotation does not automatically inherit the model's direct-reuse permission.

Prefer mature, concise formulations from an appropriate checked source when its conventions match the current mathematics.
Where direct reuse is permitted, reuse and adapt the wording as needed rather than rewriting it solely to make it different.
Preserve mathematical attribution, and avoid adding terminology or explanation merely as a byproduct of paraphrasing.
MSY23 may be used this way within its applicable designated style-model scope; other works retain their actual reuse restrictions.

After reuse, verify notation, hypotheses, domains, references and contribution statements against the current paper.
Supply author, affiliation, funding and acknowledgement information from the current project rather than inheriting those facts from a model.

A paper used solely as a style exemplar need not appear in the mathematical bibliography for that reason alone.
Cite it when its mathematical content or another source-dependent claim is used.
Record substantial textual reuse compactly in the document README by source key and relevant section; no sentence-by-sentence log is required.

Text-reuse permission governs writing.
Access classification and disclosure of a reference artifact remain governed by the existing [literature rules](../../../framework/rules/literature.md#unpublished-material).
Designation as a model is not a source-proof audit or an automatic change to those classifications.

<a id="whole-manuscript-definition-review"></a>
## Whole-Manuscript Definition and Citation Review

After an overall rewrite, check definition and citation coverage against the final manuscript, section by section, including unchanged passages.
A list of terms noticed during drafting or a review of the diff alone does not establish whole-manuscript coverage.
A local correction may receive a local review, with its scope stated explicitly.
When a definition changes, include its affected uses in that review; this does not automatically require rereading unrelated sections.

1. Inspect the mathematical objects and concepts actually introduced or substantively used, including informal introductions such as "Let J ...", formulas, and constructions outside numbered definition environments.
   Determine whether each is ordinary local notation, an established standard construction or definition, or a project definition/adaptation.
   A new symbol or a displayed formula does not by itself make the underlying construction project-specific.
2. Check organization and use under the [definition-environment criteria](#definition-environments) and [definition-writing standards](#definition-statements).
   Verify that core concepts receive an appropriate independent statement, ordinary notation is not unnecessarily numbered, and defining statements are complete and appropriately separated from motivation, properties and proofs.
   Check introduction before use, consistency of meaning, ambient setting and conventions in subsequent uses, unnecessary duplicate definitions, unexplained changes of formulation and accurate internal references.
3. Check clarity and source compliance separately.
   Verify the meaning, ambient setting and adopted convention; for established specialized definitions, also check the standard name and a suitable precise citation at the first substantive introduction or use.
   Giving the complete defining formula does not satisfy the citation obligation by itself.
   Apply the existing [citation rules](#definition-citations) and [explicit user exemptions](../../../framework/rules/preferences.md#scope-and-adoption); ordinary notation and elementary definitions do not acquire blanket new citation requirements.
4. Recognize constructions by their mathematical content, not only by named-theorem or terminology searches.
   For example, in a tracial GNS space, the formula \(J(x\Omega)=x^*\Omega\) should prompt a check for Tomita's conjugation even if the manuscript never names it.
   Consult the document's designated terminology sources and the existing definition index first, then inspect other local or external sources as needed under the source-search rules.
   Record a suspected identification as unresolved until checked; neither failure to find a name nor absence from the index establishes novelty.
5. In the existing manuscript audit, record the exact revision, whole-manuscript or explicitly limited coverage, applicable exemptions, findings on definition organization, meaning and citations, corrections and remaining unchecked scope.
   Claim whole-manuscript definition/citation review only after completing that coverage.
   A local review must identify its sections or objects and affected uses checked.
   Proof validity, compilation success and a style model's usage do not establish citation completeness.
   If a later omission contradicts an earlier coverage claim, add a dated correction preserving the original review and clarifying what was actually checked.

Keep this evidence compact: a short audit section is sufficient.
Do not create a permanent per-term register or duplicate the definition index.
Record a reusable newly checked definition at its existing source/project home and link it through the normal index when appropriate.
This rule strengthens review coverage; it does not require a full proof audit of each cited source or an exhaustive historical-priority search.

## Document Choices and Final Review

Before drafting, read these rules, the [applicable user preferences](../../../framework/rules/preferences.md#scope-and-adoption), and the relevant collection entries.
At the manuscript's existing conventions or writing-choice home, briefly record:

- The intended audience if it differs from the default, and the primary style model or community fallback, with canonical citation keys and useful section locators.
- User-designated primary terminology sources, and other references used for materially different terminology or notation choices.
- Applicable user-authorized exceptions and any substantial textual reuse with its permitted scope.

Use a short paragraph or a few lines; do not create a second bibliography, permission registry or mandatory per-paragraph log.
If no exemplars have been designated, write using the general and approved community rules.
Do not invent a selection or silently treat an arbitrary literature file as a reusable style model.

When reviewing a draft, apply the [definition and citation coverage check](#whole-manuscript-definition-review), together with any applicable personal familiarity choice, attribution language, adopted conventions, reuse scope and distinction between previous and present contributions.
Use the relevant Claim-dependency records and designated sources for this check; no separate per-term registry is required.
Mathematical proof review and build/layout checks remain governed by the [manuscript review rules](../../../framework/rules/writing.md#mathematical-content-and-review) and [build rules](../../../framework/rules/writing.md#reproducible-local-builds).
A style exemplar supplies no additional proof verification.
Apply these writing rules during preparation or revision; adopting the framework alone does not rewrite an existing manuscript or change its theorem selection.
