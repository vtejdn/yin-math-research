# F0012 Revision Requests

The current agent, acting for Yin, reviewed the manuscript on 2026-11-05.
This is a direct manuscript writing review.
The inspected TeX and document bibliography agree with commit `d08144cfd271975b5808cd7e68d3b86c762b6f56`.
The scope comprises `main.tex`, all five included sections, `references.bib`, the retained generated bibliography text, and the project and document prose.
Locations below refer to the inspected source lines and semantic labels.
These are revision requests; the manuscript sources have not been revised.

## Applicable writing layers

| Layer | Applicable choices |
| --- | --- |
| General | [Mathematical writing rules](../../../../framework/rules/writing.md): precise objects and hypotheses, justified inferences, accurate comparisons and attribution, necessary modifiers and contextual notation. |
| Yin, author-wide | [Writing policy](../../../../profiles/Yin/writing/readme.md): concise abstracts, readable proofs, definition environments for core concepts, defining equality, citation requirements, semantic labels and the adopted bibliography conventions. |
| Yin, free probability | [Subfield policy](../../../../profiles/Yin/writing/free_probability.md): a free-probability and operator-algebra research audience, explicit tracial settings and the applicable notation and terminology choices. |
| Manuscript | [Conventions](../conventions.md): an English article, MSY23 as the primary style model, the paper's own prose, the stated trace normalization and squared-singular-value hermitization. |

Higher layers override only conflicting portions of lower layers.
The retained [MSY23 presentation observations](../../../audits/literature/MSY23/Yin_U005.md#presentation-observations) are evidence for using the selected model, rather than a fifth writing layer.
The free-probability audience exemption for the term von Neumann algebra applies; the actual finiteness and faithful normal tracial-state assumptions still need to be stated, as they are in the introduction.

## R1. Correct the scope of logarithmic mean convergence in the abstract

**Location:** [main.tex](main.tex), line 30, the last sentence of the abstract; compare [introduction.tex](sections/introduction.tex), Theorem `thm:affine`, lines 92–104, and [affine.tex](sections/affine.tex), lines 166–186.

**Reason:** The abstract claims almost-sure and mean convergence of normalized logarithmic determinants without a finiteness hypothesis.
The theorem proves convergence in \(L^1\) for the logarithms only when \(u>-\infty\).
When \(u=-\infty\), it proves almost-sure convergence to minus infinity and convergence of the extended expectations to minus infinity; this is not \(L^1\) convergence to an integrable limit.
The unconditional convergence in \(L^p\) for every \(0<p<\infty\) concerns the determinants themselves.
The abstract currently blurs these different conclusions.

**Revision:** Replace the sentence with a concise formulation that preserves the distinction, for example: “We also prove convergence results for normalized determinants and logarithmic determinants of affine matrix pencils.”
If mean convergence of the logarithms is retained explicitly, qualify it by finiteness of the limiting logarithm.

**Rule:** General accuracy and [comparison strength](../../../../framework/rules/writing.md#mathematical-comparisons), together with Yin's [concise-abstract policy](../../../../profiles/Yin/writing/readme.md#abstract-concision).
Concision does not justify dropping a hypothesis that changes the meaning of a convergence claim.

## R2. Distinguish the convergence problem from the background results

**Location:** [introduction.tex](sections/introduction.tex), lines 10–15 and 30–34.

**Reason:** The sentence “the corresponding limit is given by the Brown measure” precedes both the formulation of the conjecture and the statement of the paper's theorem.
In this position it reads as another established background consequence of moment and norm convergence, although those inputs alone do not settle the nonnormal eigenvalue problem.
The preceding self-adjoint comparison also leaves its convergence mode implicit.

**Revision:** Specify convergence in probability in the self-adjoint comparison.
Introduce the general case as the question of convergence to Brown measure, or explicitly identify it as the conclusion of Theorem `thm:brown` below.
Then use the BSS18 and Han26 paragraph to distinguish the earlier question, the earlier Ginibre result and the present GUE conclusion.
Replace “the full class of GUE polynomials” with the precise class already used in the theorem: fixed scalar polynomials in the GUE inputs.

**Rule:** General [mathematical comparisons](../../../../framework/rules/writing.md#mathematical-comparisons), [direct results and necessary modifiers](../../../../framework/rules/writing.md#direct-results-and-modifiers), and Yin's author-wide requirement to explain the problem, prior results and precise contribution.
The primary style model supports this organization without supplying evidence for a stronger historical claim.

## R3. Give the core pencil convention a labelled definition

**Location:** [introduction.tex](sections/introduction.tex), lines 48–55 and 74–79, equations `eq:pencil` and `eq:affine-pencil`.

**Reason:** The affine pencil and its monic special case organize two of the three main theorems and the entire proof mechanism.
The manuscript currently introduces them only in prose, including “We call such a pencil monic.”
They therefore meet Yin's criterion for an independently stated core definition rather than merely incidental local notation.
The existing Brown-measure and Fuglede–Kadison definitions already follow that criterion.

**Revision:** Put the affine-pencil setup and the convention that the identity constant term is called monic in a labelled definition, without an optional bracketed title.
If they are grouped before Theorem `thm:pencil`, retain both existing equation labels and keep the trace convention close to its first use.
The elementary notation \(s_{\min}\) can remain in prose.
This request does not require a separate definition environment for every auxiliary measure, norm or proof-local symbol.

**Rule:** Yin's [definition-environment criteria](../../../../profiles/Yin/writing/readme.md#definition-environments) and [definition-writing standards](../../../../profiles/Yin/writing/readme.md#definition-statements).
Neither the subfield policy nor the manuscript conventions override this author-wide choice.

## R4. Quantify the constants in the imported operator-norm tail

**Location:** [probability.tex](sections/probability.tex), lines 74–79, immediately before `eq:norm-tail`.

**Reason:** The quoted estimate uses \(D\) and \(c\) without specifying their scope or independence of \(N\).
The uniform first-moment bound and the later summability argument depend on that independence.
The same letter \(D\) has just denoted a polynomial-degree bound in Lemma `lem:gaussian-tube`, which makes this new role harder to identify.

**Revision:** Introduce the estimate with constants, for example, \(C_{\mathrm{op}},c_{\mathrm{op}}>0\) independent of \(N\), and state the range \(N\ge1\), \(t>0\) at that use.
Then derive a single \(M_0\) that bounds the first moments uniformly in \(N\) before applying Gaussian concentration.
Retain the existing precise CGP22 citation.

**Rule:** General [precise objects and hypotheses](../../../../framework/rules/writing.md#general-mathematical-exposition), contextual [notation](../../../../framework/rules/writing.md#notation-in-context), and Yin's [necessary-hypotheses policy](../../../../profiles/Yin/writing/readme.md#necessary-hypotheses-and-special-cases).

## R5. Separate the deterministic zero set from the sampled Gaussian vector

**Location:** [affine.tex](sections/affine.tex), lines 52–60, subsection `subsec:global-floor`.

**Reason:** The phrase “the zero set of” is applied to an expression written with \(g\), which elsewhere denotes the sampled Gaussian vector.
The subsequent distance estimate needs a deterministic subset of the entire coordinate space.
The phrases “empty zero type” and “remaining type” also introduce an unexplained name where the argument concerns the explicitly defined maps \(F_{k,\ell}\) and their zero sets.

**Revision:** For the sufficiently large sizes supplied by the rank argument, define the set directly, using a dummy coordinate vector:

\[
 Z_N:=\{x\in\mathbb R^{dN^2}:\det L_N(N^{-1/2}x)=0\}.
\]

Here the argument of \(L_N\) is interpreted through the already specified Hermitian coordinates.
Then evaluate the distance at the random vector \(g\).
Use “a map with empty zero set” and “a map with a nonempty zero set” in the preceding argument.
Preserve the separate treatment of an empty \(Z_N\).

**Rule:** General [precise object names](../../../../framework/rules/writing.md#precise-object-names), [contextual notation](../../../../framework/rules/writing.md#notation-in-context), and Yin's [proof-readability policy](../../../../profiles/Yin/writing/readme.md#proof-readability).

## R6. Display the free logarithmic limit identified by the probability comparison

**Location:** [brown.tex](sections/brown.tex), lines 129–135, subsection `subsec:brown-as`; compare lines 92–110 and `eq:potential-pointwise`.

**Reason:** Theorem `thm:affine` gives the free logarithmic determinant of \(L_z(s)\) as its limit, while `eq:potential-pointwise` gives \(u_a(z)\) for the scalar polynomial.
The manuscript compresses the identification into “the almost-sure limit of this quantity,” without displaying the former limit or recalling why the latter is finite at the selected shift.
This is the consequential comparison that connects the two arguments and determines the factor of the pencil size.
It merits an explicit equality.

**Revision:** Recall that the limiting logarithmic-tail bound makes \(u_a(z)\) finite for each fixed \(z\ne P(0)\).
Write the conclusion of Theorem `thm:affine` explicitly as

\[
 \frac{u_N(z)}q\longrightarrow
 (\operatorname{tr}_q\otimes\tau)(\log|L_z(s)|)
 \qquad\text{almost surely}.
\]

Then compare with `eq:potential-pointwise` to identify this deterministic limit with \(u_a(z)/q\).
This explains the exact equality obtained by uniqueness of probability limits without introducing another symbol or repeating the truncation proof.
Call \(L_z\) the affine pencil, rather than the “unnormalized pencil”: the determinant used here is still normalized by \(qN\), and the distinction from the monic pencil is already expressed by \(D_z\).

**Rule:** General [explicit relationships between results](../../../../framework/rules/writing.md#direct-result-connections), [precise comparisons](../../../../framework/rules/writing.md#mathematical-comparisons), and Yin's [proof-readability policy](../../../../profiles/Yin/writing/readme.md#proof-readability).
This is an exposition request, not a finding that the stated limit is false.

## R7. Preserve the proper-name capitalization in the BSS18 title

**Location:** [references.bib](references.bib), entry `BSS18`, title field; the corresponding title is also in the [canonical bibliography](../../../literature/references.bib).

**Reason:** The retained `main.bbl` prints “non-hermitian” in this title because the internal capital is not protected from BibTeX's title case conversion.
The manuscript uses “Hermitian” elsewhere, and the retained bibliographic title itself uses that capitalization.
An adapted bibliography style does not preserve an unprotected internal capital automatically.

**Revision:** Protect `Hermitian` in both occurrences in the title field, keeping the canonical entry and the document's typesetting subset coherent.
During the eventual manuscript revision, regenerate the bibliography and check the resulting title text.
Keep the existing cited-edition note and alphabetic-label convention.

**Rule:** Yin's [bibliography policy](../../../../profiles/Yin/writing/readme.md#manuscript-references) and the general [canonical bibliography and typesetting-subset rules](../../../../framework/rules/writing.md#citations-notation-and-versions).

## R8. Identify the manuscript as the owner of the trace convention

**Location:** [conventions.md](../conventions.md), line 7, “The model uses the unnormalized trace …”.

**Reason:** The immediately preceding paragraph calls MSY23 the primary style model.
Consequently, “the model” can refer either to that article or to the GUE probability model, although this sentence is recording the present manuscript's notation.
The owner of the convention should be explicit.

**Revision:** Write “The paper uses the unnormalized trace `\Tr` and normalized trace `\tr_N`.”
Keep the following squared-singular-value and factor-one-half convention unchanged.

**Rule:** General [precise object names](../../../../framework/rules/writing.md#precise-object-names) and the [separation of manuscript choices from source observations](../../../../framework/rules/preferences.md#scope-and-adoption).
The four writing layers apply to the maintained manuscript records as well as the TeX.

## Review limits

All five sections were read for mathematical wording, hypotheses, definition organization, notation, citation placement, proof transitions and the function of modifiers in context.
The citation check compared the current uses, edition locators and bibliography with the existing [citation map](../citation.md); it did not repeat the underlying source-level theorem or proof audits.
The findings above concern the current exposition and bibliography, with the logarithmic convergence distinction in R1 checked directly against the theorem and its written proof.
They do not replace the fixed mathematical reviews linked in the project record.
No compilation, PDF rendering or visual-layout review was performed for this source review.
