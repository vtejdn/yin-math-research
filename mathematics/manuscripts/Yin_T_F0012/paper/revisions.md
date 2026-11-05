# F0012 Revision Requests

These requests concern the current working-tree manuscript inspected in the [whole-manuscript review](review.md).
The earlier accepted corrections remain in the text.

## R9. State the quadratic-map hypothesis in the added-coordinate estimate

**Location:** [affine.tex](sections/affine.tex), lines 42–50, subsection `subsec:global-floor`.

**Finding:** The passage introduces “a map \(F\) on \(\mathbb R^p\) with empty zero set” and then asserts that \((x,y)\mapsto(yF(x),y(y-1))\) has degree at most three and gives exponent \(E_F=3\cdot15^p\).
These assertions use the fact that \(F\) is one of the quadratic compressed maps \(F_{k,\ell}\).
The local statement leaves that hypothesis implicit and reads more generally than the estimate supports.

**Revision:** Introduce \(F\) explicitly as one of the quadratic maps \(F_{k,\ell}:\mathbb R^p\to\mathbb R^r\) with empty zero set, then retain the displayed construction and exponent.

**Basis:** Necessary hypotheses and [precise object names](../../../../framework/rules/writing.md#precise-object-names).
Priority: P2.

## R10. Cite the pencil formulation at its first substantive introduction

**Location:** [introduction.tex](sections/introduction.tex), lines 51–64, Definition `def:pencil`.

**Finding:** The affine-pencil formulation is an established specialized definition, but its definition environment has no source citation.
The complete formula resolves its meaning while leaving Yin's first-use citation requirement unsatisfied.
The later Han26 citation accompanies the linearization construction.

**Revision:** Add a precise applicable reference at Definition `def:pencil`.
The retained [Han26 inspection](../../../audits/literature/Han26/Yin_U001.md#linearization) covers the affine form in Section 2 and the identity-constant form of Theorem 1.5.
Its use can support those formulations while the paper explicitly adopts its Hermitian-input restriction and the convention that \(A_0=I_m\) is called monic.

**Basis:** Yin's [first-use citation rule for specialized definitions](../../../../profiles/Yin/writing/readme.md#definition-citations).
Priority: P2.

## R11. Give the core input conventions a labelled definition

**Location:** [introduction.tex](sections/introduction.tex), lines 3–8, the GUE and free semicircular setup.

**Finding:** The GUE density, variance-one semicircular law and free-independence condition are defined in ordinary prose.
They specify the principal objects of the main theorems and are used throughout the argument, so they meet Yin's criterion for a core definition.
The audience exemption concerns the term von Neumann algebra and does not override that presentation criterion.

**Revision:** Collect the input-law conventions in a compact labelled definition without an optional bracketed title, preserving the density, trace normalization, semicircular law, freeness condition and their source citations.
Keep the arbitrary coupling across sizes explicit in the standing setup.
The proof-local measures, norms and coordinate maps can retain their current local presentation.

**Basis:** Yin's [definition-environment criteria](../../../../profiles/Yin/writing/readme.md#definition-environments) and [definition-writing standards](../../../../profiles/Yin/writing/readme.md#definition-statements).
Priority: P2.

## R12. Name the fixed coefficients directly

**Location:** [affine.tex](sections/affine.tex), line 6, “If all the random coefficients vanish”.

**Finding:** The matrices \(A_j\) are fixed coefficients; the evaluated GUE matrices are random.
Calling the coefficients random obscures the deterministic case being separated.

**Revision:** Replace the condition with “If \(A_1=\cdots=A_d=0\)”, retaining the conclusions and the following nonzero-coefficient assumption.

**Basis:** [Precise object names](../../../../framework/rules/writing.md#precise-object-names).
Priority: P3.
