---
author: Yin
---

# MSY23: Definition Recheck

- Date and reviewer: 2026-09-10, the free-field algebra agent.
- Source: [MSY23, published MSY23.pdf](../literature/pdf/MSY23.pdf), JFA 285 (2023), 110016, 50 pages.
  Printed and PDF page numbers agree.
- Existing units: [U001, rank](../audits/literature/MSY23/Yin_U001.md#msy23-u001), [U002, finite-rank cycles](../audits/literature/MSY23/Yin_U002.md#msy23-u002), [U003, representations and closures](../audits/literature/MSY23/Yin_U003.md#msy23-u003), [U004, affiliated realization](../audits/literature/MSY23/Yin_U004.md#msy23-u004), and [U005, strong Atiyah property](../audits/literature/MSY23/Yin_U005.md#msy23-u005).
  Exact existing definition homes are linked below.
- Scope: a definition and convention sidecar, not a new source unit or project claim.
  The relevant existing audit sections were reread; primary definition passages on pp. 8, 10–13, 20–25, 29 and 42 were freshly checked, with surrounding statements used only to delimit their meaning.
  Rendered pp. 13, 21, 24, 25, 29 and 42 were inspected.
  This is not a fresh complete proof audit of those sections.
- Preservation: the existing units and source PDF are unchanged.
  Their proof assessments, repairs and declared external inputs remain authoritative.
  This note follows the [definition rules](../definitions/readme.md) and [reuse rule](../../framework/rules/knowledge-reuse.md#reuse-before-proof).

## Existing General Definition Homes

| General entry | Exact existing home | Published locator and convention checked |
| --- | --- | --- |
| Inner rank, rank factorization and fullness | [U001, definitions and elementary matrix arguments](../audits/literature/MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.1, p. 8. For a nonzero \(m\times n\) matrix over a unital complex algebra, inner rank is the least factorization size \(r\); zero has rank zero. Full means rank \(\min(m,n)\). The base algebra belongs to the definition. |
| Stable finiteness, also called weak finiteness | [Same U001 section](../audits/literature/MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.2, p. 8: for every finite \(N\), \(AB=I_N\) implies \(BA=I_N\). This is a matrix condition, not merely the scalar direct-finiteness condition. |
| Hollow square matrix | [Same U001 section](../audits/literature/MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.8, p. 10: an \(N\times N\) matrix has a zero \(K\times L\) block with \(K+L>N\). |
| Linear matrix | [Same U001 section](../audits/literature/MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.9, p. 10: \(A=A_0+\sum_j A_jx_j\), with constant coefficient matrices. “Linear” includes the constant term; invertibility of \(A_0\) is not required. |
| Central eigenvalues relative to complex scalars | [Same U001 section](../audits/literature/MSY23/Yin_U001.md#definitions-and-elementary-matrix-arguments) | Definition 2.12, pp. 11–12: \(\lambda\in\mathbb C\) such that \(\rho(P-\lambda I_N)<N\). The chosen scalar field is not replaced by the entire center of an arbitrary coefficient algebra. |
| Linear representation of a free-field element | [U003, conventions and dependency boundary](../audits/literature/MSY23/Yin_U003.md#conventions-and-dependency-boundary) | Definition 4.2, p. 21: \(r=uA^{-1}v\), with \(A\) full and affine linear over \(\mathbb C\langle x\rangle\), \(u\in M_{1,N}(\mathbb C)\), \(v\in M_{N,1}(\mathbb C)\). Neither minimality nor regularity at zero is part of this definition. |
| Representation domain and free-field function domain in a chosen algebra | [U003, Theorem 4.4 and Definition 4.5](../audits/literature/MSY23/Yin_U003.md#theorem-44-and-definition-45-consistency-on-the-chosen-domain) | Definition 4.5, pp. 22–23. A representation is evaluable when its pencil is invertible in the specified matrix algebra; the function domain is the union over its representations. Theorem 4.4 supplies consistency for stably finite ambient algebras. |
| Matrix rational closure and scalar division closure for a general inclusion | [U003, Definitions 4.7 and 4.10](../audits/literature/MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra) | Definition 4.7, p. 24, and Definition 4.10, p. 25. These are general constructions for a unital subalgebra in a fixed unital ambient algebra. |
| Complete division closure | [U003, complete division closure](../audits/literature/MSY23/Yin_U003.md#complete-division-closure-and-proposition-411) | Discussion and Proposition 4.11, pp. 26–27. Inverse closure at every matrix size gives the alternative formulation of matrix rational closure retained in U003. The equivalence is an accepted result, not an additional project definition or a request for a new proof. |
| Analytic rank | [U004, Lemmas 5.1–5.5](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) | Definition 5.4, p. 29. See the normalization check below. |
| Strong Atiyah property | [U005, setting and closure conventions](../audits/literature/MSY23/Yin_U005.md#setting-and-closure-conventions) | Definition **5.22**, p. 42: every polynomial matrix evaluated at the tuple has integral analytic rank. Theorem 5.23 is a consequence under maximal \(\Delta\), not the definition's number. |

The universal free field discussed in Section 4.1, pp. 20–21, is the universal division ring of fractions of the free polynomial algebra.
The more explicit general definition is already housed in [Yin20-U001, free fields and localization](../audits/literature/Yin20/Yin_U001.md#3-free-fields-and-the-retained-localization-interface).
MSY23 Theorem 4.1 supplies the retained fullness and inner-rank-preservation interface.
Neither that theorem nor an affiliated realization is incorporated into the definition of a linear representation.

## Fixed-Ambient Closure Conventions

The [existing U003 home](../audits/literature/MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra) contains the complete general definitions.
With letters standardized to \(A\subseteq B\):

- \(\operatorname{Div}_B(A)\) closes under inverses of scalar elements that are units in \(B\).
- \(\operatorname{Rat}_B(A)\) collects entries of inverses of all finite square matrices over \(A\) that are invertible over \(B\).

This paragraph records a notation conversion, not new definitions for particular parameters.
Taking \(A=\mathbb C\langle X\rangle\), \(B=M\), or \(B=\mathcal U(M)\) belongs at the consuming statement.
Adding generator adjoints changes the chosen \(A\), rather than the general closure operation.
A division-closed subalgebra need not be a division ring.

Source uses of “rational closure” for scalar inverse closure, including the formal-series terminology in Reu96 and CR94, must be converted explicitly.
The name alone does not identify that construction with matrix rational closure in every ambient algebra.

Theorem 4.4 and Lemma 4.8 operate in the algebra already specified by the domain or rational-closure premise.
They do not change that algebra after observing that one matrix compression is bounded.
The precise source and counterexample boundary remains in the [separate bounded-linearization recheck](Yin_L_F0018_v1.md#bounded-linearization-recheck).
Proposition 4.11's division-ring hypothesis concerns the closure in that same ambient algebra.

<a id="delta-finite-rank-cycles"></a>
## The General Finite-Rank-Cycle Definition of Delta

The existing [U002 setting](../audits/literature/MSY23/Yin_U002.md#setting-delta-and-the-three-conditions) records the cycles and maximality criterion but does not display the entire dimension formula.
This is the supplemental definition home, transcribed from the unnumbered definition on published pp. 12–13.

**Definition (MSY23 convention).**
Let \((M,\tau)\) be a tracial \(W^*\)-probability space with faithful normal tracial state, let \(H=L^2(M,\tau)\), and let \(X=(X_1,\ldots,X_d)\in M^d\).
Write \(\lambda\) for left multiplication and \(J\) for the conjugate-linear isometry extending \(a\mapsto a^*\).
Then

\[
\mathcal C_X=
\left\{(T_1,\ldots,T_d)\in\operatorname{Fin}(H)^d:
  \sum_{j=1}^d[T_j,J\lambda(X_j^*)J]=0\right\},
\qquad
\Delta(X)=d-\dim_{M\bar\otimes M^{\mathrm{op}}}
                  \overline{\mathcal C_X}^{\,\mathrm{HS}}.
\]

Here \(\operatorname{Fin}(H)\) consists of operators with finite-dimensional complex range, and the closure is in \(\mathrm{HS}(H)^d\) with its Hilbert-Schmidt norm.
The dimension is the von Neumann module dimension for the standard Hilbert-Schmidt \(M\bar\otimes M^{\mathrm{op}}\)-module, using the product trace induced by \(\tau\).
The \(d\)-fold ambient module has dimension \(d\).
The operator \(J\lambda(X_j^*)J\) is right multiplication by \(X_j\).

There is no normality, selfadjointness, dual-system assumption, or requirement that this tuple generate all of \(M\) in this definition.
The closure of finite-rank cycles is essential; it is not replaced by the space of all Hilbert-Schmidt solutions or an operator-norm closure.
The number \(d\) is not divided out.
The equivalence of \(\Delta(X)=d\) with absence of a nonzero finite-rank cycle is the faithful-dimension observation retained in U002, rather than a different definition.

No first-introduction claim is made.
MSY23 attributes the invariant and its homological origin in its discussion on pp. 12–13; the present task verifies MSY23's formulation, not that attribution's historical priority.

<a id="analytic-rank-normalization"></a>
## Analytic Rank, Matrix Size, and Representation Dimension

The definition itself remains in [U004](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness).
Definition 5.4, p. 29, uses

\[
\operatorname{rank}_{\mathrm a}(P)
 =(\operatorname{Tr}_N\otimes\tau)
      (p_{\overline{\operatorname{ran}P}})
 =N-(\operatorname{Tr}_N\otimes\tau)(p_{\ker P}),
 \qquad P\in M_N(\mathcal U(M)).
\]

\(\operatorname{Tr}_N\) is the **unnormalized** matrix trace, so \(\operatorname{rank}_{\mathrm a}(I_N)=N\) and values lie in \([0,N]\).
The preceding use of normalized \(\operatorname{tr}_N\) to equip a matrix amplification with a tracial state does not change this convention.

| Notion | Meaning and normalization |
| --- | --- |
| Polynomial inner rank \(\rho_A(P)\) | Least algebraic factorization size over the specified \(A\). |
| Analytic rank \(\operatorname{rank}_{\mathrm a}(P)\) | Trace of the range projection using \(\operatorname{Tr}_N\otimes\tau\); need not be an integer without hypotheses. |
| Finite-rank operator rank | Complex dimension of an operator's range on \(H\); this is the rank of finite defects and dual commutators. |
| Representation dimension \(N\) | Size of a particular linear representation. A minimum over an explicitly specified representation class is a separate minimality notion. |
| “Rank of a rational series” in CR94/Reu96 terminology | Minimal dimension in the relevant representation class; it is not MSY23 analytic rank. The minimum is taken in the specified representation class. |

Theorem 5.6's equality of evaluated analytic rank with polynomial inner rank has substantive hypotheses; it is not a definitional identification.
The strong Atiyah property in Definition 5.22 requires nonnegative integral analytic ranks for all finite sizes and polynomial matrices.
It does not require equality with their original polynomial inner ranks.

## Citation and Reuse Disposition

<a id="tomita-conjugation"></a>
### Follow-up: Tomita's Conjugation Operator

Date and reviewer: 2026-09-10; the coordinating agent, scoped definition/source check.
The published MSY23, Section 3, p. 13, immediately after the definition of Delta, explicitly identifies \(J\) as Tomita's conjugation operator: the conjugate-linear isometric extension of \(x\mapsto x^*\) from \(M\) to \(L^2(M,\tau)\).
The page was read and visually checked.
The published [ACSY24](../literature/pdf/ACSY24.pdf), p. 29, also uses that name and states \(J(x)=x^*\); its passage was checked in extracted text.

In tracial GNS notation this is exactly \(J(x\Omega)=x^*\Omega\).
The involution property \(J^2=I\) follows on the dense subspace \(M\Omega\) from \((x^*)^*=x\), then on all of \(H\) by continuity.
MSY23, p. 13, supplies the definition and terminology, with ACSY24 as corroboration.
This is the tracial conjugation operator; no nontracial modular-domain assertion is imported.
No new definition or Claim ID is allocated, and no whole-source proof review is claimed.

<a id="tomita-foundational-reference"></a>
### Follow-up: Foundational Reference for the Tracial Conjugation

Date/reviewer: 2026-09-10; the coordinating agent, self-review following the user's request for a foundational reference beyond MSY23 and ACSY24.
The already registered [AP18 author draft](https://www.math.ucla.edu/~popa/Books/IIun.pdf) supplies the required construction.
Section 7.1.1, printed pp. 97-98 / PDF pp. 103-104, treats a general tracial von Neumann algebra and extends \(J\widehat{x}=\widehat{x^*}\) to an antilinear surjective isometry.
Section 7.1.3, printed p. 100 / PDF p. 106, explicitly gives \(J\pi(x)\xi_0=\pi(x^*)\xi_0\); taking the tracial GNS representation and \(\xi_0=\Omega\) gives \(J(x\Omega)=x^*\Omega\).

The source calls this the **canonical conjugation operator**.
It is a suitable foundational exposition citation, not an origin attribution; the chapter does not require a factor assumption.
Search stopped after these passages supplied the exact construction and applicable hypotheses.
Scope: extracted source text and notation checked, no independent whole-chapter proof audit.
The online 338-page draft is undated; the registry key does not verify a 2018 revision.

### Earlier Citation Disposition

MSY23 is a suitable candidate for the labels **current formulation**, **notation**, or **standard interface**, with the exact locators above.
It is not labeled **origin** by this recheck.
Known evaluation consistency, complete-closure equivalence, and rank-preservation results can be used at their existing audited interfaces when their hypotheses match; no new C identifier or reconstruction is required merely to use them.

The [Claim definition-use record](Yin_L_F0004_v1.md#claim-definition-uses), attached from the Claim registry, records the adopted precise links and distinguishes statement, proof and comparison use.
It does not alter historical theorem dependencies.
Dual-system definitions are handled by the other source group and are not duplicated here.

## Current source homes

At 2026-10-21T01:35, the complete definition/convention reading was retained at [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-definition-recheck), reusing the sufficient general U definitions linked there.
The actual AP18 conjugation construction is retained at [AP18-U002](../audits/literature/AP18/Yin_U002.md#tomita-foundational-reference).
The original account above remains the fixed historical input used for the tracial-conjugation interface in [R_F0046](../audits/reviews/Yin_R_F0046_v1.md#arrangement-and-inspected-scope), with its source locators, reading dates and depth unchanged.
The additional review formerly named R_A0019 has no verified local or original-source correspondence in this account; no current review identity or coverage is inferred from that historical name.
This relocation neither opens the source again nor renews the earlier mathematical reviews.
