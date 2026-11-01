---
author: Yin
---

# Han08: Wigner–Yanase Skew Information

Source/version: the artifact is [arXiv:math-ph/0607049v6](../../../literature/pdf/Han08.pdf), posted 21 February 2008, with revision date 20 February 2008 on the title page.
Its title, author and version were checked.
The 2008 PNAS publication metadata was verified against the author's [institutional research record](https://researchprofiles.ku.dk/da/publications/metric-adjusted-skew-information/) and is held in [references.bib](../../../literature/references.bib).

Scope and state: on 2026-10-10 the assigned comparison agent read the introduction, pp. 1–3, particularly the unnumbered definition on p. 3 and its stated homogeneity and vanishing under commutation.
The PDF text extraction loses some letters, so the actual formula was also checked against the accessible arXiv rendering during the preceding source search.
This is a definition and local applicability check, not a review of Hansen's general metric-adjusted theory or the Wigner–Yanase–Dyson convexity theorem.

For a density matrix `d` and a Hermitian matrix `a`, the definition is `I_WY(d,a)=-Tr([d^{1/2},a]^2)/2`.
For `b>0` and Hermitian `a_0`, direct multiplication gives

\[
 \operatorname{Tr}(ba_0^2)-\operatorname{Tr}(b^{1/2}a_0b^{1/2}a_0)
 =\tfrac12\|[b^{1/2},a_0]\|_{\rm HS}^2
 =\operatorname{Tr}(b)I_{\rm WY}(b/\operatorname{Tr}(b),a_0).
\]

The first equality uses the skew-adjointness of the commutator; the last uses homogeneity.
The difference is zero exactly when `b` commutes with `a_0`.
This identity concerns the covariance-zero trace expressions and does not identify a correction involving nonzero covariance eta with skew information.
With trace-log normalization `1/(2m)`, the corresponding difference has that additional factor.

Search evidence: public searches for the trace difference and Wigner–Yanase skew information located Hansen's exact definition.
The original Wigner–Yanase PNAS article was located bibliographically, but publisher/PMC access did not yield an inspected full text.
The citation therefore points to Hansen, whose definition was directly read; no original-source proof inspection is claimed.
Search stopped after this adequate primary exposition and the local identity check.
