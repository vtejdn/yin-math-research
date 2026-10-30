---
author: Yin
---

# GS14: Selected Analytic Transport Input

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Inspected artifact: [arXiv:1204.2182v3](https://arxiv.org/pdf/1204.2182), 2013-10-08, 37 pages. |
| source-locator | Locators: Sections 2.1 and 2.5, pp. 8-11; Theorems 3.15-3.16, pp. 27-28; Theorem 4.2, p. 29. |
| inspection | Coverage state: **Read**. |

<a id="gs14-u001"></a>
## GS14-U001: Small Analytic Transports and an Analytic Inverse

Source identity: GS14 in the sole literature registry (private lookup: `../../../literature/registry.md#regularity-route-intakes`).
Inspected artifact: [arXiv:1204.2182v3](https://arxiv.org/pdf/1204.2182), 2013-10-08, 37 pages.
Locators: Sections 2.1 and 2.5, pp. 8-11; Theorems 3.15-3.16, pp. 27-28; Theorem 4.2, p. 29.
Page numbers are one-based PDF/printed pages.

Record: 2026-09-09, the affiliated-generalization agent.
Coverage state: **Read**.
Exact statements, conventions and applicability are checked and accepted for use.
The original transport proof is **not fully re-audited**.
Independent source-interface confirmation by the q-Gaussian mechanism agent is recorded in the [Yin_C_F0018 review](../../reviews/Yin_R_F0064_v1.md#projective-dual-correction-finding).

### Accepted Source Input

Write $\mathcal A^{(R)}$ for noncommutative series with finite absolute coefficient norm $|p|_R=\sum_w|p_w|R^{|w|}$.
For finite standard semicircular $S$ and fixed $A>A'>4$, sufficiently small selfadjoint $W\in\mathcal A^{(A+1)}$, measured by $|W|_{A+1}$, gives
\[
Y=F_W(S)=S+f_W(S),\qquad f_W\in(\mathcal A^{(A')})^d.
\]
The correction satisfies $|f_{W,j}|_{A'}\to0$ as $|W|_{A+1}\to0$.
The selfadjoint tuple $Y$ has the free Gibbs law for $\frac12\sum_j Z_j^2+W$.
After further smallness there is a convergent analytic inverse $S=H(Y)$.

The selfadjoint-potential hypothesis is retained from the surrounding construction, even where the later theorem statement suppresses it.
The source's spatially positive Hessian is not used as a substitute for the stronger tensor-norm condition below.

### Local Applicability and Separate Deduction

For this application set $M=W^*(S)$ with its semicircular trace.
The substantive extension is [Yin_C_F0018](../../../claims/Yin_C_F0018_v1.md#yin_c_f0018), not an additional source theorem.
Its absolute-coefficient estimate gives, in the **usual Banach projective tensor norm**,
\[
\sum_k\|(\partial_k f_{W,j})(S)\|_\pi
\le \frac{|f_{W,j}|_{A'}}{A'-2}.
\]
There are finitely many coordinates.
The accepted convergence therefore allows a further perturbation threshold making
\[
\frac{\sum_j|f_{W,j}|_{A'}}{A'-2}<1.
\]
Consequently the evaluated Jacobian has a Neumann inverse in the matrix algebra over $M\widehat\otimes_\pi M^{\mathrm{op}}$.
Yin_C_F0018 proves that this inverse corrects the original semicircular bounded duals to bounded duals for $Y$, with the opposite-product order explicitly checked there.

Both directions of the analytic coordinate representation converge in operator norm, so $C^*(Y)=C^*(S)$ and $W^*(Y)=W^*(S)$.
The selfadjoint tuple thus has the bounded-dual and generation hypotheses needed in [Yin_C_F0013](../../../claims/Yin_C_F0013_v1.md#yin_c_f0013).

These deductions do not identify the rational fields in the two coordinate systems and do not prove rational $L^2$ boundedness or bounded scalar reconstruction.
Yin_C_F0018 gives an explicit reason that an infinite projective expansion need not preserve finite rank.
The unresolved general analytic questions are owned by [Yin_S_F0010](../../../strategies/Yin_S_F0010.md#s_f0010).

### Inspection, Dependencies and Stopping Point

The trigger was the user's analytic free-transport route and its need for an actual bounded-dual applicability theorem.
The already registered primary arXiv source was used.
Its title/version record and the specified norm and theorem passages were read as parsed primary text; the core theorem statements were reopened when this unit was extracted from the ledger's source record.
The surrounding smallness and inverse-map discussion was inspected for applicability.
This does not constitute review of the complete fixed-point construction, its full differential-operator estimates, the Gibbs uniqueness inputs or all references.

The ledger independently proves the tensor correction and derivative estimate; the established GS14 transport and inverse statements are accepted external inputs under the [repository policy](../../../../framework/rules/literature-audits.md#accepted-external-inputs).
No unresolved objection affects this selected use.
A complete original-proof audit is not asserted by acceptance.

The publisher endpoint timed out during the revisit; journal metadata remains owned by the previously checked registry.
No local PDF was downloaded, replaced or changed.
No successful rendered-page inspection is claimed here.
Search stopped after the selected norms, convergence and inverse statements resolved the input needed by Yin_C_F0018.
No numerical verification, formalization, outside human review, errata search or priority assessment was performed.
