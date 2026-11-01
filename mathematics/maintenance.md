# Unresolved material maintenance

## Voi99-U002 publication-page span

The `source-version` row in [Voi99-U002](audits/literature/Voi99/Yin_U002.md#source-and-inspection) gives the published edition's printed pages as 101–163.
The [edition note](audits/literature/Voi99/readme.md#yin-edition) and the Voi99 entry in the [canonical bibliography](literature/references.bib) give 101–166.
These publication-page annotations are inconsistent; the unit separately identifies its inspected passages as the Introduction and Sections 1–4, printed pp.101–114.
The applicable grounds are [bibliographic and edition responsibilities](../framework/rules/literature-audits.md#organization-and-stable-units) and [truthful inspection scope](../framework/rules/literature-audits.md#coverage-states).
Repair submitted in Voi99-U002's `source-version` row, which now gives printed pp.101–166.
Next action: independent acceptance of the corrected publication-page annotation against the responsible edition and bibliographic evidence, preserving the actual inspected passages, date, depth and limitations.
This discrepancy requires no new whole-source audit and supplies no mathematical-error verdict.

## Current-assessment prose links select historical decisions

The assessment navigation in [C_F0085](claims/Yin_C_F0085_v1.md), line 67, [C_F0086](claims/Yin_C_F0086_v1.md), line 28, and [C_F0090](claims/Yin_C_F0090_v1.md), line 19, calls its target the selected or current assessment but links the historical `candidate-0002` decision.
Each material's actual Current selector chooses a later decision.
This conflicts with [responsible assessment ownership](../framework/rules/records.md#authoritative-files) and [Claim navigation](../framework/rules/claims.md#claim-navigation).
Next action: independently verify the intended reference and repair the navigation or explicitly describe its historical purpose.
Acceptance must preserve all selected decisions, dates, proofs and review scopes while making the prose and target agree.

## Unresolved formula reference after argument extraction

[L_F0015](ledger/Yin_L_F0015_v1.md), line 63, invokes "by (2) after permutation", but this L no longer contains equation (2).
Its scalar-pivot interface now points to [C_F0009](claims/Yin_C_F0009_v1.md#proof-of-the-two-state-pivot-criterion), whose equation (2) defines the complementary pivot and whose complete Schur inverse appears in equation (8).
The [content-retention and consumer-repair rule](../framework/rules/records.md#substantive-material-retention) requires an accurate locator for the actual retained argument.
Repair submitted in L_F0015's two-pivot recovery paragraph, which now links C_F0009, equation (8), after permutation.
Next action: independent acceptance of the repaired formula reference without treating the original broken locator as a mathematical counterexample.
Acceptance must check the actual formula, hypotheses and reference purpose, preserving the mathematical argument.

## Routine tool and identifier-maintenance prose in strategies

[S_F0007](strategies/Yin_S_F0007.md), lines 136–138, retains file/link counts and whitespace/language-check results that supply no continuing mathematical, evidence or execution fact.
The same issue affects the repeated "No old ID or argument was deleted, and no replacement goal was created" sentence in [S_F0001](strategies/Yin_S_F0001.md), line 100; [S_F0002](strategies/Yin_S_F0002.md), line 95; [S_F0003](strategies/Yin_S_F0003.md), line 60; [S_F0004](strategies/Yin_S_F0004.md), line 73; [S_F0005](strategies/Yin_S_F0005.md), line 124; and [S_F0006](strategies/Yin_S_F0006.md), line 65.
These are routine process under the [substantive-retention rule](../framework/rules/records.md#substantive-material-retention).
Repair submitted in S_F0001–S_F0006's resolution paragraphs and the final evidence bullet in S_F0007.
Next action: independent acceptance of the removal of only the unnecessary process prose.
Acceptance must retain useful failures, actual lineage and review facts, including the mathematical inspection immediately before S_F0007's tool-check sentences.

## Routine edited-file lists in fixed reviews

The "Definition-use documentation findings" in [R_F0055 v2](audits/reviews/Yin_R_F0055_v2.md), line 175; [v3](audits/reviews/Yin_R_F0055_v3.md), line 177; [v4](audits/reviews/Yin_R_F0055_v4.md), line 193; and [v5](audits/reviews/Yin_R_F0055_v5.md), line 200, retain the same "The only pre-existing files edited in this pass are ..." list.
This is an editing-process list rather than mathematical content, inspected input scope or a checking relationship, under the [substantive-retention rule](../framework/rules/records.md#substantive-material-retention).
Next action: independently verify and remove the unnecessary list without retiring the review containers.
Acceptance must preserve the adjacent real definition corrections, inspection dates, inputs, scopes and historical relationships without fabricating a new review.

## NS06 contents overgeneralizes the inspected edition

[NS06 contents](literature/contents/NS06.md), line 10, says that the existing source units retain the earlier author's-edition `+13` page correspondence.
The current [NS06-U001](audits/literature/NS06/Yin_U001.md), lines 13–26, and [NS06-U002](audits/literature/NS06/Yin_U002.md), lines 13 and 22–25, instead identify the 434-page publisher layout and `+17` correspondence, consistent with the [source edition note](audits/literature/NS06/readme.md).
This conflicts with [contents responsibilities](../framework/rules/literature.md#searchable-contents) and [precise source scope](../framework/rules/literature-audits.md#organization-and-stable-units).
Next action: distinguish the actual earlier author-edition readings from the two current U records rather than applying one correspondence to all of them.
Acceptance must preserve real historical locators and the distinction between comparing contents and comparing the full texts, without claiming a new original-source inspection.

## Current manuscript records use outdated lemma numbers

The [manuscript review](manuscripts/Yin_T_F0001/review.md), line 125, assigns the finite-rank-solution identification to Lemma 5.6, whereas the current identification lemma is 5.3.
The same review, line 167, and [organization record](manuscripts/Yin_T_F0001/organization.md), line 47, cite "Lemmas 5.1 and 4.1" for Theorem 1.9's closure equivalence; the [current proof](manuscripts/Yin_T_F0001/paper/sections/dual-system-criterion.tex), lines 235–237, uses Lemma 5.1 and the finite-rank-closure Lemma 4.2.
The [current manuscript review rule](../framework/rules/writing.md#manuscript-review-and-citation-records) requires these records to describe the actual current text.
Next action: verify the current labels and correct these three references.
Acceptance must preserve actual review arrangements, findings and limits without presenting numbering maintenance as a new proof review.

## Computation program comments use a different source key

The module descriptions in [J_F0003 main.py](computations/programs/Yin_J_F0003/main.py), line 1, and [J_F0004 main.py](computations/programs/Yin_J_F0004/main.py), line 1, name "Miy23" for Proposition 4.5 and Proposition 5.1 respectively.
Their responsible README, U and canonical bibliography identify the work as `MS23`, with no `Miy23` entry.
The [citation-key rule](../framework/rules/literature.md#3-citations-elsewhere-in-the-repository) applies the same canonical key to code comments.
Next action: confirm the same-work correspondence and correct these explanatory source keys.
Acceptance must verify that program behavior, numerical scope and source edition remain unchanged; a comment correction requires no historical rerun.

## Computation index omits finite scope

The "Title and scope" cells in the [computation index](computations/index.md), lines 8–11, contain only the four slug titles.
They omit the brief finite or exploratory scope required by the [computation-index rule](../framework/rules/computations.md#computation-index).
Next action: derive concise navigation scopes from each actual J README.
Acceptance must preserve exact results, limits and review facts at the responsible J home rather than duplicating them in the index.

## Strategy model-contract references awaiting verification

[S_F0007](strategies/Yin_S_F0007.md), lines 30–36, 93 and 118–120; [S_F0008](strategies/Yin_S_F0008.md), lines 30–38; [S_F0009](strategies/Yin_S_F0009.md), lines 25 and 69; and [S_F0010](strategies/Yin_S_F0010.md), lines 25 and 77, describe current model work as belonging to separate R-diagonal, analytic-transport or q-Gaussian Tasks.
Their formal Task associations locate only the historical T_F0001 v1 expansion, and [T_F0001 v2](tasks/Yin_T_F0001_v2.md), lines 137–139, mentions the transfers without identifying those separate contracts.
The [Strategy responsibility rule](../framework/rules/strategies.md#identifiers-and-files) calls for actual Task associations and applicable scope.
Next action: verify whether a current separate contract is intended, locate it when available, or make the historical or unresolved context explicit.
This is awaiting verification; missing navigation does not establish missing authorization and does not authorize creating, changing or resuming a Task/E.
Acceptance must check the actual association and its historical/current purpose without inventing execution authority.

## General sum-normalization research home awaiting verification

The manuscript's [general sum-normalization lemma and fourth equivalent condition](manuscripts/Yin_T_F0001/paper/sections/liberation-dual-system-criterion.tex), lines 7–43 and 187–225, are presented with a local manuscript self-review in the [project source map](manuscripts/Yin_T_F0001/readme.md), line 20, and [review record](manuscripts/Yin_T_F0001/review.md#normalized-liberation-criterion-20261018).
The linked [C_F0079 v4](claims/Yin_C_F0079_v4.md) retains three equivalent conditions and individual zero-vacuum normalization; [C_F0082](claims/Yin_C_F0082_v1.md) constructs a sum-normalized system under the additional finite-liberation-Fisher-information hypothesis.
Those statements do not themselves identify a responsible research home for the manuscript's general sum-correction argument and added fourth-condition proof.
Targeted C/L/R searches and the inspected interfaces have not located a sufficient home, which is a responsibility question under [mathematical content and manuscript review](../framework/rules/writing.md#mathematical-content-and-review), rather than a finding that the proof is wrong.
Next action: independently verify whether the argument is substantively new and locate adequate existing C content before deciding whether additional responsible retention, assessment and review are needed.
Acceptance must check the actual general hypotheses, complete necessary argument and applicable evidence, then reconcile the manuscript source map and necessary definition navigation without forcing a new identity or inventing independent review.

## Body-level inspection to continue

Continue C-body inspection outside C_F0079_v4, C_F0082_v1, C_F0083_v2 and C_F0084–0091_v1, including the only partially read C_F0009.
The remaining T bodies are T_F0001 v1 and v3–v6.
Continue R bodies outside R_F0055_v5, R_F0081_v1 and R_F0083–0092_v1; the other R_F0055 versions have only been read around the specific process finding.
The remaining U-body groups are ACSY24, CS05, CS77, Con94, DR97, Dab10, Dab14, GS14, Hun74, JMS21, KS07, Kro81, Lau88, Lin00, MS23, MSY23, Mai15, Miy22, Miy26, PV23, Par88, Shl24, TV06, Tol17, Tre17, Unt20, VV16, Voi98, Voi99, Xia23 and Yin20, including passages beyond their locally inspected interfaces.
Follow necessary source, definition and review consumers without replaying every proof or expanding this into an inventory of private originals, execution state, outputs or environments.
