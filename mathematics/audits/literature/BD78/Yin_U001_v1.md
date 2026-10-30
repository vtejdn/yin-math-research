---
author: Yin
---

# Derivation Extension to a Universal Localization

<a id="bd78-u001"></a>

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Bergman–Dicks, published 1978 article; the retained source-reading passage was written on 2026-10-12. |
| source-locator | §2.1, equation (4) and its proof, printed pp. 298–299 / PDF pp. 7–8. |
| inspection | The original 2026-10-12 source reading checked the displayed localization/derivation interface and its applicability to T_F0001. |

<a id="f0001-derivation-extension-20261012"></a>
## Bimodule-valued derivation-extension interface, 2026-10-12

The decisive primary source was Bergman--Dicks, *Universal derivations and universal ring constructions*, published version, [publisher PDF](https://msp.org/pjm/1978/79-2/pjm-v79-n2-p02-s.pdf), Section 2.1, equation (4) and proof, printed pp.298--299 / PDF pp.7--8 (one-based).

Equation (4) identifies Omega_K(S) with S tensor_R Omega_K(R) tensor_R S when S is a universal two-sided localization of the K-ring R.
The proof constructs the extended universal derivation and verifies its universal property and uniqueness.
Consequently, for any S-bimodule B, restriction identifies K-derivations S -> B with K-derivations R -> B.
This last formulation is a deduction through the universal property, not a verbatim numbered theorem in the paper.
No heredity, flatness or semisimple-base hypothesis is imposed in Section 2.1.
The inverse rule is equation (8), printed p.299.

Take R to be the free complex polynomial algebra, S its free field, and B=S tensor_C S with its outer bimodule action.
Cohn06 Theorem 7.5.13(e) and Corollary 7.5.14, printed pp.450--451 / local PDF pp.474--475, identify the universal field of a semifir with localization at all full square matrices.
These statements were read locally.
The polynomial difference quotient with values in B then extends uniquely, and the linear identification a tensor b -> a tensor b^{op} gives the target S tensor_C S^{op}.
Under maximal Delta, MSY23 Theorem 1.1 supplies the evaluation isomorphism from the free field to the affiliated division closure of the generated polynomial algebra.

Cohn06 Theorem 7.5.17 and its proof, printed p.451 / PDF p.475, were also read.
Its stated target is the ring itself, so that theorem alone does not directly justify a tensor-valued difference quotient.
Its triangular-matrix proof suggests the generalization, while BD78 supplies the matching bimodule interface explicitly.

Scope: selected text reading and applicability check by the authoring AI agent.
No whole-paper audit or independent proof review is claimed.
A requested web screenshot of BD78 timed out; no successful new visual inspection is recorded.
