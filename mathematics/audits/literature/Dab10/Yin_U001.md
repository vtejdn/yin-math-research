---
author: Yin
---

<a id="dab10-u001"></a>
# Dab10-U001: The Finite-Fisher Factoriality Interface

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Inspected online: [12-page PDF](https://arxiv.org/pdf/0804.2906) and [versioned HTML](https://arxiv.org/html/0804.2906v2). |
| source-locator | Theorem 1 and its proof, pp. 3–4, were read in parsed primary text; Theorem 13, p. 10, was statement-checked. |
| inspection | Coverage: `Read`; accepted theorem input, not a full proof audit. |

- Record: 2026-09-09, the star-interface source reader; targeted primary statement and applicability check for [Yin_T_F0001](../../../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
- Source: [Dab10 in the bibliography](../../../literature/readme.md), [arXiv:0804.2906v2](https://arxiv.org/abs/0804.2906v2), revised 2009-07-13.
  Inspected online: [12-page PDF](https://arxiv.org/pdf/0804.2906) and [versioned HTML](https://arxiv.org/html/0804.2906v2).
  No local PDF was retained.
- Coverage: `Read`; accepted theorem input, not a full proof audit.
  Theorem 1 and its proof, pp. 3–4, were read in parsed primary text; Theorem 13, p. 10, was statement-checked.
  The surrounding definitions on p. 2 were inspected.

## Exact Accepted Input and Source Qualifications

For n>=2 bounded selfadjoints X in a tracial von Neumann algebra with faithful normal probability trace,

\[
\Phi^*(X_1,\ldots,X_n)<\infty
\quad\Longrightarrow\quad W^*(X_1,\ldots,X_n)\text{ is a factor}.
\]

Theorem 1 omits n>=2 locally; its proof uses a different index j!=i.
A single semicircular generator excludes n=1.
Theorem 13 explicitly imposes n>=2 and says all bounded central sequences are asymptotically scalar.
Applying it to a constant central sequence also gives the displayed conclusion.
The quantity Phi* is non-microstates Fisher information, despite the shorter inconsistent label in those theorem statements.
These qualifications resolve the applicability issue.
The closed-derivation/regularization foundations and the proof of Theorem 13 are accepted, not re-audited here.
Non-Gamma and entropy consequences are not required for the current use.

## Conversion from the Project's Bounded Dual Convention

This is a local adaptation of the previously audited [Voi98-U005, Section 5.10](../Voi98/Yin_U005.md#voi98-u005).
It does not assume that the project's D_i are selfadjoint or that they annihilate the vacuum.

Suppose X_j=X_j* generate N, act on H=L2(N,tau), and bounded D_i satisfy `[D_i,X_j]=delta_ij P_Omega`.
Taking adjoints and using selfadjointness of X_j gives

\[
[D_i^*,X_j]=-\delta_{ij}P_\Omega.
\]

Set

\[
K_i=\tfrac12(D_i-D_i^*),\qquad Y_i=-iK_i.
\]

Then K_i is skew-adjoint, Y_i is bounded selfadjoint, `||Y_i||<=||D_i||`, and

\[
[X_j,Y_i]=i\delta_{ij}P_\Omega.
\]

These are exactly the source dual relations, with scalar base algebra.
The audited Voi98 conjugate-variable construction supplies

\[
\xi_i=i(JY_iJ-Y_i)\Omega\in L^2(N),
\qquad\|\xi_i\|_2\le2\|D_i\|.
\]

The generated-algebra hypothesis ensures that the vectors lie in the required L2 space.
The audited construction includes the polynomial conjugate relation and its algebraic-freeness interface; no preexisting normalization of D_i Omega is used.
Consequently,

\[
\Phi^*(X)=\sum_i\|\xi_i\|_2^2
\le4\sum_i\|D_i\|^2<\infty.
\]

For n>=2, the accepted Dab10 input therefore makes N a factor.
In particular, a selfadjoint generating tuple of length at least two in a nonfactor cannot have a bounded dual system with the project's relations.
This deduction does not apply to a merely normal tuple without a justified selfadjoint-coordinate conversion.

## Intended Use and Verification Limits

The intended consumer is the [scaled-semicircular exploration](../../../ledger/Yin_L_F0002_v1.md).
Its nonfactoriality must be proved independently; an affiliated free-field embedding alone does not establish or contradict factoriality.
Once nonfactoriality is known, this unit excludes bounded duals.
The stronger strict-intersection construction remains a separate project argument.

Search on 2026-09-09 was restricted to the exact arXiv identifier, theorem locators, and publication metadata.
The [arXiv record](https://arxiv.org/abs/0804.2906v2) and [publisher record](https://www.sciencedirect.com/science/article/pii/S0022123610000686) identify the published article; the publisher PDF was not compared.
The versioned PDF URL initially returned a cache miss; the current PDF and explicit v2 HTML were readable.
There was no whole-paper audit, numerical computation, formal verification, external human review, or priority assessment.
Sole bibliographic registration remains in `mathematics/literature/readme.md`.
