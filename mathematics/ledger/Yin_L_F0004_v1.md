---
author: Yin
---

# Definition Use and Source Normalization

<a id="definition-usage-normalization"></a>
Record kind: research operation and definition-use metadata for preserved claims.
Date and owner: 2026-09-10, root, with source rechecks by another AI agent, another AI agent and another AI agent.
Authorization: the user requested re-examination of literature definitions, creation of the concept-group index, and normalization of definition use after approving the definition rules.
Context: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), its supporting source studies, and the registered Yin_C_F0001-Yin_C_F0035 records.

## Scope and Ownership

The [definition index](../definitions/index.md#group-index) locates general definitions and their precise source homes.
The [source-study index](../audits/literature/index.md) locates the actual source inspections and their limits.
This record supplies explicit definition-use references for the preserved Claim artifacts, attached to each Claim's registry entry.
It does not replace their statements, proofs, current assessments or proof-version map.
Source definitions stay in their audits; project constructions stay in their existing mathematical sections.

The references below are added on this date.
They identify the definitions actually adopted by the displayed formulas and hypotheses; they do not pretend that historical proofs already contained these source citations.
The original complete mathematical and audit artifacts are preserved byte for byte.
The [existing version map](Yin_L_F0014_v1.md#proof-version-map) still selects Yin_C_F0029-P2 and the Yin_C_F0030-P2/Yin_C_F0024-P2 criterion specializations, with the specified P1 auxiliaries; Yin_C_F0013 and Yin_C_F0022 retain P1.

## Clarifications Adopted in This Pass

1. **Closure operations.**
   Use scalar division closure and matrix rational closure for their respective general constructions in an inclusion of unital rings.
   The choice of $M$, $\mathcal U(M)$ or the initial generated algebra is recorded in the consuming theorem.
   Formal-series uses of the phrase "rational closure" are read according to the source's actual inverse operation.
   Equality of different closures, or identification with a free field, is a theorem input with hypotheses, not a definition.
   The refuted bounded-intersection assertion in Yin_C_F0001 is not reinstated.
2. **Expressions and representations.**
   Distinguish a finite expression, a field element, an algebraic representation, an affine linear representation and a domain-preserving formal representation.
   A monic pencil and minimal state dimension are extra restrictions where stated.
   A bounded scalar evaluation does not, by definition, make every inverse pencil bounded.
3. **Duals and domains.**
   The project's $[D_i,X_j]=\delta_{ij}P$ is compared explicitly with source commutator signs.
   Vacuum normalization is absent from the bounded-dual hypotheses of Yin_C_F0001/Yin_C_F0002/Yin_C_F0013, present in MS23's polynomial-domain definition, and need not even be meaningful on Yin_C_F0029's domain.
   Domain containment, normality and adjoint tests stay in each theorem, without separate registrations for every variant.
4. **Derivatives and tensors.**
   Algebraic free difference quotients, their specified graph closures, maximal bounded Hilbert-Schmidt commutator domains, and weak commutator forms are distinguished.
   The inner product is linear in its second variable where the project states that convention.
   Opposite multiplication and the placement of the conjugation in the Hilbert-Schmidt identification are retained.
   A vector-gradient closure is not silently identified with the intersection of component closure domains.
5. **Ranks.**
   Ordinary complex dimension of an operator range, algebraic Hankel rank, inner rank over a ring, and the unnormalized tracial rank of an affiliated matrix are separately identified.
   The finite-rank-cycle invariant $\Delta(X)$ is not the cleared defect sometimes denoted $\Delta_i(s,a,b,t)$.
   Matrix size and minimal representation dimension are not substitutes for any of these ranks.
6. **Models and coefficient spaces.**
   Haar, semicircular and R-diagonal conditions keep their standard definitions.
   A circular or R-diagonal element is not made normal by terminology.
   Full/q-Fock word vectors, free deletion and q-annihilation retain their actual actions and scaling.
   Formal word coefficients and membership in a holomorphic $L^2$ subspace are not automatically interchangeable for an arbitrary operator tuple.
7. **Known facts.**
   Standard equivalent descriptions, including division-closure recursion and recognizability characterizations, are cited as established inputs where needed.
   This pass creates no Claim or obligation to reprove them.
   Previously recorded self-contained proofs remain valid historical work; no novelty is inferred from them.

## Definition References Used Below

These short local links are navigation to exact definition homes, not duplicate definitions or newly numbered entities.
Source versions, locators and inspection limits are retained in the linked source rechecks.

| Reference | Exact definition home and adoption boundary |
| --- | --- |
| <a id="probability"></a>Probability setting and models | [Probability space](../audits/literature/NS06/Yin_U002_v1.md#probability-space), [freeness](../audits/literature/NS06/Yin_U002_v1.md#free-independence), [Haar](../audits/literature/NS06/Yin_U002_v1.md#haar-unitary), [semicircular](../audits/literature/NS06/Yin_U002_v1.md#semicircular), [R-diagonal](../audits/literature/NS06/Yin_U002_v1.md#r-diagonal). Only the models actually specified in a claim are assumed. |
| <a id="scalar-division"></a>Scalar division closure | [General definition and its matrix counterpart](../audits/literature/MSY23/Yin_U003_v1.md#definitions-47-and-410-two-closures-in-one-ambient-algebra); [same-ambient convention recheck](../audits/literature/MSY23/Yin_U002_v2.md#fixed-ambient-closure-conventions). |
| <a id="matrix-closure"></a>Matrix rational closure | [Same general closure section](../audits/literature/MSY23/Yin_U003_v1.md#definitions-47-and-410-two-closures-in-one-ambient-algebra); [Property I is a separate algebra property](../audits/literature/PV23/Yin_U001_v2.md#matrix-domain-property-i). |
| <a id="expressions"></a>Expressions and evaluation | [Rational syntax and ambient domains](../audits/literature/Yin20/Yin_U001_v1.md#2-rational-syntax-and-evaluation-domains). Parameter substitutions remain at the point of evaluation. |
| <a id="representations"></a>Representations | [Algebraic/linear and formal representations](../audits/literature/Yin20/Yin_U001_v1.md#4-algebraic-representations-and-formal-representations), [minimality and state families](../audits/literature/CR94/Yin_U001_v1.md#cr94-u001). |
| <a id="free-field"></a>Free field | [Universal field and localization formulation](../audits/literature/Yin20/Yin_U001_v1.md#3-free-fields-and-the-retained-localization-interface). Its realization by a particular tuple is a theorem, not part of this definition. |
| <a id="ranks"></a>Matrix ranks and Delta | [Inner rank/fullness](../audits/literature/MSY23/Yin_U001_v1.md#definitions-and-elementary-matrix-arguments), [analytic-rank normalization](../audits/literature/MSY23/Yin_U002_v2.md#analytic-rank-normalization), [Delta](../audits/literature/MSY23/Yin_U002_v2.md#delta-finite-rank-cycles). |
| <a id="affiliation"></a>Affiliated setting and regular-fraction conventions | [Affiliated setting](../audits/literature/Miy22/Yin_U006_v1.md#shared-setting-and-trust-boundary), [regular fractions](../audits/literature/Miy22/Yin_U006_v1.md#miy22-u006). These passages use the standard affiliation foundation; they do not spell out its commutant/domain definition. A bounded regular denominator is a unit in the affiliated algebra; its inverse need not lie in $M$. |
| <a id="bounded-dual"></a>Bounded dual relation | [MSY23 Definition 6.1 and sign conversion](../audits/literature/MSY23/Yin_U005_v1.md#definition-61-and-proposition-62-the-dual-system-route); [Voi98's selfadjoint convention](../audits/literature/Voi98/Yin_U002_v2.md#bounded-dual-systems). |
| <a id="polynomial-dual"></a>Normalized polynomial dual | [MS23's actual domain and normalization](../audits/literature/MS23/Yin_U001_v2.md#normalized-polynomial-domain-duals); [canonical contraction](../audits/literature/ACSY24/Yin_U001_v2.md#canonical-contraction-dual). Neither definition supplies an all-$M$ extension. |
| <a id="derivatives"></a>Derivations and graph closure | [Free quotient and closure](../audits/literature/Voi98/Yin_U002_v2.md#difference-quotients-and-closure), [general coarse-valued derivation](../audits/literature/ACSY24/Yin_U001_v2.md#coarse-valued-derivation). |
| <a id="conjugates"></a>Conjugates and Fisher information | [Relative conjugates](../audits/literature/Voi98/Yin_U002_v2.md#conjugate-variables), [Fisher information](../audits/literature/Voi98/Yin_U002_v2.md#fisher-information), [Lipschitz convention](../audits/literature/Dab14/Yin_U002_v1.md#lipschitz-conjugate-condition). |
| <a id="fock"></a>Fock and coefficient models | [Full Fock and word basis](../audits/literature/Miy22/Yin_U001_v1.md#mathematical-setting), [q-Fock/Wick](../audits/literature/MS23/Yin_U001_v2.md#q-fock-and-wick-model), [free right deletion](../audits/literature/MS23/Yin_U001_v2.md#free-right-deletion). |
| <a id="series"></a>Rational series and residuals | [Formal-series interfaces](../audits/literature/Miy22/Yin_U002_v1.md#formal-series-and-exact-interfaces), [representations/residuals](../audits/literature/BR10/Yin_U002_v1.md#representations-and-residuals), [algebraic Hankel rank](../audits/literature/BR10/Yin_U002_v1.md#formal-hankel-rank). |
| <a id="holomorphic"></a>Holomorphic closures | [Source algebra and Hilbert subspaces](../audits/literature/KS07/Yin_U001_v2.md#holomorphic-subspaces); [Yin_C_F0021's actual one-variable choices](../claims/Yin_C_F0021_v1.md#1-statement). |
| <a id="analytic-norms"></a>Analytic and projective norms | [Absolute coefficient norm](../audits/literature/GS14/Yin_U001_v2.md#analytic-coefficient-norm), [Jacobian/opposite product](../audits/literature/GS14/Yin_U001_v2.md#cyclic-gradient-jacobian), [Yin_C_F0018's Banach projective norm and action](../claims/Yin_C_F0018_v1.md#1-algebra-norms-and-the-correction-lemma). |
| <a id="commutator-domain"></a>Maximal bounded commutator derivative | [Yin_C_F0002, Statement (3), equation (M)](../claims/Yin_C_F0002_v1.md#statement). This is the preserved project definition of $\mathcal B_D$ and $\partial^D$, not the minimal polynomial graph closure. |
| <a id="cleared-defect"></a>Cleared-denominator defect | [Yin_C_F0013, Section 1, equation (4)](../claims/Yin_C_F0013_v1.md#1-statement-and-exact-scope); [Yin_C_F0034's general domain formulation](../claims/Yin_C_F0034_v1.md#yin_c_f0034). Yin_C_F0029-P2 uses this construction with its stated left-module domain. |
| <a id="weak-form"></a>Weak commutator and bounded representative | [Yin_C_F0025, Section 1, equations (2)-(3)](../claims/Yin_C_F0025_v1.md#1-exact-hypotheses-and-conclusion); [Yin_C_F0014's $L^2$ target and tests](../claims/Yin_C_F0014_v1.md#yin_c_f0014). The target and test domains remain explicit in each application. |
| <a id="balanced-tensor"></a>Algebraic balanced tensor product | [Hun74 IV.5.1–5.2](../audits/literature/Hun74/Yin_U005_v1.md#balanced-tensor), added in the subsequent 2026-09-10 Chapter IV audit; [Yin_C_F0035's stated right/left module convention](../claims/Yin_C_F0035_v1.md#yin_c_f0035) remains its concrete instance. The [dated source supplement](../claims/Yin_C_F0035_v1.md#yin_c_f0035-hun74-source-supplement) identifies the previously used standard inputs. It is not a Hilbert or Banach completion. |

<a id="claim-definition-uses"></a>
## Definition Uses by Claim

Each row attaches definition references to the unchanged statement/proof named in its first cell.
`Statement`, `proof`, `auxiliary` and `comparison` describe different uses, not extra logical dependencies.
A source recheck is not an automatic new theorem input.
Ordinary finite rank below means complex dimension of the actual operator range; bounded extension from a dense domain is asserted only where the corresponding Claim proves it.

| Claim and preserved mathematical home | Definition uses and precise boundary |
| --- | --- |
| <a id="yin_c_f0001-definitions"></a>[Yin_C_F0001](../claims/Yin_C_F0001_v1.md#yin_c_f0001) | Statement: [scalar division closure](#scalar-division) in $M$ of the listed generators, [bounded duals](#bounded-dual) without vacuum normalization, ordinary finite operator rank. Normality/generation are the stated hypotheses. The conjecture remains refuted. |
| <a id="yin_c_f0002-definitions"></a>[Yin_C_F0002](../claims/Yin_C_F0002_v1.md#yin_c_f0002) | Statement/proof: [bounded duals](#bounded-dual), [free quotient](#derivatives), [scalar division closure](#scalar-division). The tensor convention is in its Setting section; equation (M) defines the [maximal commutator domain](#commutator-domain). The minimal-closure assertion has only its stated one-way domain inclusion. |
| <a id="yin_c_f0003-definitions"></a>[Yin_C_F0003](../claims/Yin_C_F0003_v1.md#yin_c_f0003) | Statement/comparison: [division closure](#scalar-division) with the explicitly starred initial algebra and the unchanged [bounded-dual](#bounded-dual) relation. Adjoining generators is a parameter change; it does not supply commutator identities for their adjoints. The rejected variant remains refuted. |
| <a id="yin_c_f0004-definitions"></a>[Yin_C_F0004](../claims/Yin_C_F0004_v1.md#yin_c_f0004) | Statement/proof: normality and scalar spectral law, [division closure](#scalar-division), ordinary finite-rank kernels and one-variable rational degree. Classical [Hankel terminology](../audits/literature/Par88/Yin_U001_v2.md#hankel-symbol-conventions) is comparison only; this proof does not require the Hardy-space Kronecker theorem for an arbitrary spectral measure. |
| <a id="yin_c_f0005-definitions"></a>[Yin_C_F0005](../claims/Yin_C_F0005_v1.md#yin_c_f0005) | Statement/proof: [affiliation](#affiliation), [division closure](#scalar-division), [free field](#free-field), [Delta](#ranks), [bounded duals](#bounded-dual) and algebraic balanced tensors. The identified free field is an accepted maximal-Delta consequence, not a definition of every division closure. |
| <a id="yin_c_f0006-definitions"></a>[Yin_C_F0006](../claims/Yin_C_F0006_v1.md#yin_c_f0006) | Statement/proof: [division closure](#scalar-division) and [bounded duals](#bounded-dual) under the specified generator changes; [full Fock](#fock) supplies the retained model examples. No invariance under arbitrary analytic coordinates is inferred. |
| <a id="yin_c_f0007-definitions"></a>[Yin_C_F0007](../claims/Yin_C_F0007_v1.md#yin_c_f0007) | Statement/proof: [free field](#free-field), [linear representations and state families](#representations), [derivatives](#derivatives), [affiliated/L2 evaluation](#affiliation), [Delta/rank interfaces](#ranks). Rational state vectors, their square integrability, and boundedness of an entire inverse remain separate assertions. |
| <a id="yin_c_f0008-definitions"></a>[Yin_C_F0008](../claims/Yin_C_F0008_v1.md#yin_c_f0008) | Statement/proof: [scalar and matrix closures](#matrix-closure) in the same bounded ambient algebra, with the explicitly adjoint-closed division closure needed for positive pivots. PV23 Property I is a terminology comparison, not a retroactively added proof dependency. |
| <a id="yin_c_f0009-definitions"></a>[Yin_C_F0009](../claims/Yin_C_F0009_v1.md#yin_c_f0009) | Statement/proof: [linear representations](#representations), state dimension and [division closure](#scalar-division). The chosen full pencil and complementary scalar pivots retain their actual invertibility hypotheses; general matrix size two is not a new rationality definition. |
| <a id="yin_c_f0010-definitions"></a>[Yin_C_F0010](../claims/Yin_C_F0010_v1.md#yin_c_f0010) | Statement/proof: [representations](#representations), [bounded duals](#bounded-dual) and [affiliated L1/L2 states](#affiliation). Vacuum normalization in a separate diagnostic is not an assumption on every bounded dual or a bound on the inverse pencil. |
| <a id="yin_c_f0011-definitions"></a>[Yin_C_F0011](../claims/Yin_C_F0011_v1.md#yin_c_f0011) | Statement/proof: [free-field realization](#free-field), [two ambient closure instances](#scalar-division), [bounded-dual conversion](#bounded-dual) and [finite Fisher information](#conjugates). The absence of bounded duals is part of this example's boundary, not a contradiction of their definition. |
| <a id="yin_c_f0012-definitions"></a>[Yin_C_F0012](../claims/Yin_C_F0012_v1.md#yin_c_f0012) | Statement/proof: [bounded scalar closure](#scalar-division), [bounded duals](#bounded-dual), [free semicircular/Fock model](#fock), and ordinary operator rank. Its explicit fractions are not a definition equating bounded affiliated values with admissible bounded expressions. |
| <a id="yin_c_f0013-definitions"></a>[Yin_C_F0013-P1](../claims/Yin_C_F0013_v1.md#yin_c_f0013) | Statement/proof: [affiliation and regular fractions](#affiliation), [division closure/free-field realization](#free-field), [bounded duals](#bounded-dual) and the [cleared defect](#cleared-defect). Its cofinite-domain supplement keeps its own test spaces; this pass does not replace them with a weak form. |
| <a id="yin_c_f0014-definitions"></a>[Yin_C_F0014](../claims/Yin_C_F0014_v1.md#yin_c_f0014) | Statement/proof: [affiliated L2 values](#affiliation), [weak forms on the displayed bounded tests](#weak-form), [cleared defects](#cleared-defect) and [bounded duals](#bounded-dual). An L2 element does not automatically define a bounded weak-commutator representative. |
| <a id="yin_c_f0015-definitions"></a>[Yin_C_F0015](../claims/Yin_C_F0015_v1.md#yin_c_f0015) | Statement/proof: [right residuals, realizations and algebraic Hankel rank](#series) of the chosen word coefficients. The orthonormal basis and homogeneous bounds are theorem assumptions; $P_{uv}=P_uP_v$ is not assumed. Known equivalence proofs remain preserved without being presented as novel definitions. |
| <a id="yin_c_f0016-definitions"></a>[Yin_C_F0016](../claims/Yin_C_F0016_v1.md#yin_c_f0016) | Statement/proof and separately marked model discussion: [conjugates, Fisher information and Lipschitz conditions](#conjugates), [dual and graph-domain](#derivatives) conventions, and [affiliated L2](#affiliation). Retain the original source's simultaneous/component closure wording at each use. |
| <a id="yin_c_f0017-definitions"></a>[Yin_C_F0017](../claims/Yin_C_F0017_v1.md#yin_c_f0017) | Statement/proof: [R-diagonal cumulants](../audits/literature/NS06/Yin_U002_v1.md#r-diagonal), [holomorphic closures](#holomorphic), [recognizable weighted coefficients](#series), [scalar/matrix evaluation](#matrix-closure). Normalized holomorphic words span their indicated subspace, not all $L^2(M)$. |
| <a id="yin_c_f0018-definitions"></a>[Yin_C_F0018](../claims/Yin_C_F0018_v1.md#yin_c_f0018) | Statement/proof: [analytic coefficient norm, Jacobian and projective tensor action](#analytic-norms), [bounded duals](#bounded-dual). The cyclic derivative in GS14 is not the Hilbert-space dual operator. Projective continuity alone does not preserve finite rank. |
| <a id="yin_c_f0019-definitions"></a>[Yin_C_F0019](../claims/Yin_C_F0019_v1.md#yin_c_f0019) | Statement/proof: [Haar/freeness/R-diagonality](#probability), [affiliated inverse and L2](#affiliation), [bounded duals](#bounded-dual) for the separate normal generating pair. The resulting R-diagonal element itself need not be normal. |
| <a id="yin_c_f0020-definitions"></a>[Yin_C_F0020](../claims/Yin_C_F0020_v1.md#yin_c_f0020) | Statement/proof: [q-Fock/Wick](#fock), [right q-annihilation and defect kernel](../audits/literature/Dab14/Yin_U002_v1.md#q-model-and-defect-kernel), [projective action](#analytic-norms), [q-Hermite normalization](../audits/literature/BKS97/Yin_U001_v2.md#q-hermite), and scalar closure in the one-coordinate application. Small-q tuple estimates and all-q marginal conclusions remain separate. |
| <a id="yin_c_f0021-definitions"></a>[Yin_C_F0021](../claims/Yin_C_F0021_v1.md#yin_c_f0021) | Statement/proof: [nonzero R-diagonal element](../audits/literature/NS06/Yin_U002_v1.md#r-diagonal), [positive-power L2 and norm closures](#holomorphic), [division closure](#scalar-division), and [recognizability](#series) derived in the proof. Normality/injectivity are not required, but R-diagonality is. |
| <a id="yin_c_f0022-definitions"></a>[Yin_C_F0022-P1](../claims/Yin_C_F0022_v1.md#yin_c_f0022) | Statement/proof: [finite Fisher information](#conjugates), [canonical polynomial dual and its closure](#polynomial-dual), [affiliated fractions](#affiliation), [cleared defects](#cleared-defect). All-$M$ domain containment is established through the recorded estimates, not imported from the source definition. |
| <a id="yin_c_f0023-definitions"></a>[Yin_C_F0023](../claims/Yin_C_F0023_v1.md#yin_c_f0023) | Statement/proof: [q-Fock/Wick](#fock), [normalized polynomial dual](#polynomial-dual), and [conjugates](#conjugates). Bounded extension of the whole dual is the project conclusion; it is not included in MS23's definition. The [separate Lipschitz route](../audits/literature/Dab10/Yin_U002_v1.md#4-a-reconstructed-bounded-dual-consequence-of-lipschitz-conjugates) gives the same conclusion, but is not an input to this degree-weighted proof. |
| <a id="yin_c_f0024-definitions"></a>[Yin_C_F0024](../claims/Yin_C_F0024_v1.md#yin_c_f0024) | Statement/current P2: [affiliation](#affiliation), [division/free field](#free-field), [Delta](#ranks), [cleared defects](#cleared-defect), with $E=V_i=M$ in Yin_C_F0029-P2. P1 Sections 7-8 retain the auxiliary [finite-Fisher](#conjugates) construction and example. No vacuum normalization is added to the main statement. |
| <a id="yin_c_f0025-definitions"></a>[Yin_C_F0025](../claims/Yin_C_F0025_v1.md#yin_c_f0025) | Statement/proof: [coarse-valued derivations](#derivatives), [canonical contraction](#polynomial-dual), [weak bounded finite-rank representatives](#weak-form), [Delta](#ranks), and [affiliated scalar closure](#scalar-division). The starred test algebra differs from the unstarred algebra in the rationality conclusion. |
| <a id="yin_c_f0026-definitions"></a>[Yin_C_F0026](../claims/Yin_C_F0026_v1.md#yin_c_f0026) | Statement/proof: the displayed closed operator domain, [regular denominators](#affiliation) and the local dual commutator relation in its own statement. The operator is unbounded; this does not adopt the boundedness premise of the source bounded-dual definition. Comparison with [ACSY24's core](../audits/literature/ACSY24/Yin_U001_v2.md#starred-core-application-boundary) does not assert that this counterexample satisfies its Hilbert-Schmidt hypotheses. |
| <a id="yin_c_f0027-definitions"></a>[Yin_C_F0027](../claims/Yin_C_F0027_v1.md#yin_c_f0027) | Statement/proof: [matrix rational closure](#matrix-closure) and [affine linear representations](#representations) with bounded complete inverse, actual closed-domain commutators in Sections 2-4, and [graph closures](#derivatives). The two norm estimates are theorem conditions supplying an extension; they are not part of the general dual definition. |
| <a id="yin_c_f0028-definitions"></a>[Yin_C_F0028](../claims/Yin_C_F0028_v1.md#yin_c_f0028) | Statement/proof: [scalar division closure](#scalar-division), [rational expressions](#expressions), [affiliated fractions](#affiliation), [domain-preserving representations](#representations), [weak bounded finite rank](#weak-form), and ordinary rational-degree/operator-rank conventions. The commutator equivalences apply to $f\in W^*(X_j)$ in a normal tuple; the displayed whole-field intersection equality is stated only for $d=1$. |
| <a id="yin_c_f0029-definitions"></a>[Yin_C_F0029](../claims/Yin_C_F0029_v1.md#yin_c_f0029) | Statement/current P2: [Delta](#ranks), [affiliated scalar closure/free field](#free-field), [cleared defects](#cleared-defect) and [balanced tensors](#balanced-tensor). Dense left-module dual/adjoint domains are the displayed hypotheses, not new indexed definitions or implicit vacuum-containing cores. |
| <a id="yin_c_f0030-definitions"></a>[Yin_C_F0030](../claims/Yin_C_F0030_v1.md#yin_c_f0030) | Statement/current P2: the same general constructions as [Yin_C_F0029](#yin_c_f0029-definitions), with $E=M$ and the specified dense adjoint test modules. P1's auxiliary certificates retain their own scope. |
| <a id="yin_c_f0031-definitions"></a>[Yin_C_F0031-P1](../claims/Yin_C_F0031_v1.md#yin_c_f0031-p1) | Statement/proof: closable Hilbert-space operator, adjoint and finite-dimensional range on its actual dense domain. No tracial probability model, free field, or dual-system definition is an assumption of this abstract lemma. |
| <a id="yin_c_f0032-definitions"></a>[Yin_C_F0032-P1](../claims/Yin_C_F0032_v1.md#yin_c_f0032-p1) | Statement/proof: finite-tracial $L^2$ setting, dense left module and the specified projection/test spaces. These are parameters and module conditions within the lemma, not a new family of dual-system definitions. |
| <a id="yin_c_f0033-definitions"></a>[Yin_C_F0033-P1](../claims/Yin_C_F0033_v1.md#yin_c_f0033-p1) | Statement/proof: the dense left-module domain and closable maps, the displayed dual relation, and the [cleared-defect](#cleared-defect) algebraic identity. No separate adjoint-module hypothesis is imposed. Normality is its hypothesis; no parent criterion is used as a definition. |
| <a id="yin_c_f0034-definitions"></a>[Yin_C_F0034-P1](../claims/Yin_C_F0034_v1.md#yin_c_f0034-p1) | Statement/proof: [regular affiliated fractions](#affiliation), [cleared defects](#cleared-defect) on the actual module, and inverse closure. Normality, free-field realization and the canonical polynomial dual are not assumptions. |
| <a id="yin_c_f0035-definitions"></a>[Yin_C_F0035-P1](../claims/Yin_C_F0035_v1.md#yin_c_f0035-p1) | Statement/proof: a same-unit division subring and the [algebraic balanced tensor product](#balanced-tensor). No operator, trace, topology or normality is imposed. Free-field realization is used only by later consumers to verify this input. |

## Coverage, Outcome and Remaining Boundaries

The source-recheck index records exactly which primary pages were inspected.
Reference books were checked at relevant definition passages; no whole-book audit is inferred.
The existing Shl24 formula locator and Xia23 disk example were reviewed as already accepted source context, with no new independent definition needed.
Unt20's undefined domain, regularity and Delta terminology stays explicitly unresolved in its existing reading record; this pass does not fill missing manuscript hypotheses by conjecture.

This pass registers no C/D IDs, changes no mathematical Role, and selects no new proof or main theorem.
The added convention links do not strengthen any Claim.
In particular, the existing Yin_C_F0029/P2 domain hypotheses and Yin_C_F0023 bounded-dual conclusion retain their separate proof evidence.
Source checks and documentation review are reported in their actual scopes, not as a fresh review of every mathematical proof.

The index is a starting coverage map of definitions used or explicitly treated by the current source audits.
A source-local proof notation or unused technical construction may remain in its existing section without becoming a separate concept entry.
Citation candidates are marked by purpose; none is asserted to establish first introduction.

The actual [definition, locator and applicability review findings](../audits/reviews/Yin_R_F0055_v2.md#definition-use-documentation-findings) retain their original 2026-09-10 scopes, corrections and relationship limits.
