---
author: Yin
---

# Rational Difference-Differential Operators

<a id="kv12-u001"></a>

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Kaliuzhnyi-Verbovetskyi–Vinnikov, arXiv:1003.0695v2, 24 May 2010, 29 PDF pages. |
| source-locator | Theorem 4.2, p. 14; Definition 4.4, pp. 15–16; Corollary 4.11, p. 21; §4.4, p. 22, equations (4.6)–(4.7). |
| inspection | Original source reading and clarification dated 2026-10-12; visual inspection at pp. 14, 16, 21 and text inspection at pp. 14–16, 20–22; full proofs were not independently audited. |

<a id="kv12-rational-difference-differential"></a>
## Accepted interface and local convention

Theorem 4.2 (p.14) identifies the restricted two-tuple rational-function class with matrices over the algebraic tensor product of two copies of the free field.
Its scalar case gives the tensor target used here.
Definition 4.4 (pp.15--16) supplies the polynomial difference quotient and its linearity, product and inverse rules.
Corollary 4.11 and the paragraph immediately following it (p.21) state that the construction passes to rational functions, taking values in that algebraic tensor product.
These statements supply difference quotients on the free field, independent of the chosen rational expression.

Let X be a tuple in a finite tracial von Neumann algebra M, let A_X be its generated complex polynomial algebra and U=L0(M), and suppose evaluation identifies the free field with F:=Div_U A_X, as in the maximal-Delta equivalence of MSY23 Theorem 1.1, (i) and (v).
Transport the KV12 maps through this isomorphism.
Then use the linear identification a tensor b -> a tensor b^{op} to obtain partial_i:F -> F tensor_C F^{op}.
Right multiplication on the ordinary second factor becomes left multiplication on its opposite.
Consequently the source rules become
\[
\partial_i(v_1v_2)
=(1\otimes v_2^{\mathrm{op}})\partial_i v_1
 +(v_1\otimes1)\partial_i v_2,
\qquad
\partial_i(v^{-1})
=-(v^{-1}\otimes(v^{-1})^{\mathrm{op}})\partial_i v.
\]
The generator rule is partial_i X_j=delta_ij 1 tensor 1.
No tensor completion or analytic domain hypothesis is introduced.

The authoring agent inspected the named statements and their adjacent text, including visual inspection of pp.14, 16 and 21, and checked the local opposite-factor conversion.
The source theorems are accepted as external inputs; their full proofs were not independently audited.
No new claim review is asserted by retaining this original selected source reading.

<a id="citation-clarity-follow-up-2026-10-12"></a>
## Citation clarity follow-up, 2026-10-12

The authoring agent reread pp.14--16 and 20--22 of the retained preprint.
Section 4.4, p.22, explicitly displays the linear map Delta_j: K^{tensor ell} -> K^{tensor (ell+1)}.
Taking ell=1 gives the required free-field-to-algebraic-tensor map.
Equations (4.6)--(4.7) give the product and inverse rules; Definition 4.4 supplies the polynomial restriction, and Corollary 4.11 with its following paragraph supplies expression independence.
This clarifies the locator without retracting the previously checked interface.
This additional check used text extraction, not new visual inspection or an independent proof audit.

A targeted search for derivation extension through universal localization also found [BD78 Section 2.1, (4)](../BD78/Yin_U001_v1.md#f0001-derivation-extension-20261012).
It allows arbitrary target bimodules and therefore offers an alternative general algebraic justification.
Cohn's Theorem 7.5.17, on ordinary ring-valued derivations, cannot by itself be cited as the desired tensor-valued statement.
