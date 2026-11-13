# F0012 Revision Requests

These requests concern the current working-tree manuscript inspected in the [whole-manuscript review](review.md).
The earlier accepted corrections remain in the text.

## R9. State the quadratic-map hypothesis in the added-coordinate estimate

**Location:** [affine.tex](sections/affine.tex), lines 42–50, subsection `subsec:global-floor`.

**Finding:** The passage introduces “a map \(F\) on \(\mathbb R^p\) with empty zero set” and then asserts that \((x,y)\mapsto(yF(x),y(y-1))\) has degree at most three and gives exponent \(E_F=3\cdot15^p\).
These assertions use the fact that \(F\) is one of the quadratic compressed maps \(F_{k,\ell}\).
The local statement leaves that hypothesis implicit and reads more generally than the estimate supports.

**Revision:** Introduce \(F\) explicitly as one of the quadratic maps \(F_{k,\ell}:\mathbb R^p\to\mathbb R^r\) with empty zero set, then retain the displayed construction and exponent.

**Basis:** Necessary hypotheses and [precise object names](../../../../../framework/rules/writing.md#precise-object-names).
Priority: P2.

## R10. Cite the pencil formulation at its first substantive introduction

**Location:** [introduction.tex](sections/introduction.tex), lines 51–64, Definition `def:pencil`.

**Finding:** The affine-pencil formulation is an established specialized definition, but its definition environment has no source citation.
The complete formula resolves its meaning while leaving Yin's first-use citation requirement unsatisfied.
The later Han26 citation accompanies the linearization construction.

**Revision:** Add a precise applicable reference at Definition `def:pencil`.
The retained [Han26 inspection](../../../../audits/literature/Han26/Yin_U001.md#linearization) covers the affine form in Section 2 and the identity-constant form of Theorem 1.5.
Its use can support those formulations while the paper explicitly adopts its Hermitian-input restriction and the convention that \(A_0=I_m\) is called monic.

**Basis:** Yin's [first-use citation rule for specialized definitions](../../../../../profiles/Yin/writing/readme.md#definition-citations).
Priority: P2.

## R11. Give the core input conventions a labelled definition

**Location:** [introduction.tex](sections/introduction.tex), lines 3–8, the GUE and free semicircular setup.

**Finding:** The GUE density, variance-one semicircular law and free-independence condition are defined in ordinary prose.
They specify the principal objects of the main theorems and are used throughout the argument, so they meet Yin's criterion for a core definition.
The audience exemption concerns the term von Neumann algebra and does not override that presentation criterion.

**Revision:** Collect the input-law conventions in a compact labelled definition without an optional bracketed title, preserving the density, trace normalization, semicircular law, freeness condition and their source citations.
Keep the arbitrary coupling across sizes explicit in the standing setup.
The proof-local measures, norms and coordinate maps can retain their current local presentation.

**Basis:** Yin's [definition-environment criteria](../../../../../profiles/Yin/writing/readme.md#definition-environments) and [definition-writing standards](../../../../../profiles/Yin/writing/readme.md#definition-statements).
Priority: P2.

## R12. Name the fixed coefficients directly

**Location:** [affine.tex](sections/affine.tex), line 6, “If all the random coefficients vanish”.

**Finding:** The matrices \(A_j\) are fixed coefficients; the evaluated GUE matrices are random.
Calling the coefficients random obscures the deterministic case being separated.

**Revision:** Replace the condition with “If \(A_1=\cdots=A_d=0\)”, retaining the conclusions and the following nonzero-coefficient assumption.

**Basis:** [Precise object names](../../../../../framework/rules/writing.md#precise-object-names).
Priority: P3.

## R13. Identify and normalize the Laplacian at first use

**Location:** [introduction.tex](sections/introduction.tex), lines 21–24, Definition `def:brown-measure` (currently Definition 1.1).

**Finding:** The symbol \(\Delta\) is used to define Brown measure, but the following sentence only says that it acts in the sense of distributions on \(\mathbb C\).
It does not identify the operator as the planar Laplacian or fix its sign and normalization.
The later identity \(\Delta\log|z|=2\pi\delta_0\) in [brown.tex](sections/brown.tex), line 166, makes the intended convention inferable after its first use.

**Revision:** At the first definition write that, for \(z=x+\mathrm i y\), \(\Delta:=\partial_x^2+\partial_y^2\) is the planar Laplacian, interpreted distributionally.
The distributional convention is \(\langle\Delta u,\varphi\rangle:=\langle u,\Delta\varphi\rangle\) for \(\varphi\in C_c^\infty(\mathbb C)\).
A concise local explanation suffices for this elementary operator.

**Basis:** [Contextual notation](../../../../../framework/rules/writing.md#notation-in-context) and [unambiguous definitions](../../../../../framework/rules/writing.md#definition-statements).
Priority: P2.

## R14. State the consequence of introducing the Ginibre adjoints

**Location:** [introduction.tex](sections/introduction.tex), lines 31–34, especially the sentence beginning “Writing a general GUE polynomial”.

**Finding:** The paragraph explains the GUE-to-Ginibre pairing and notes that rewriting a general GUE polynomial introduces adjoints, then cites Han26 Question 1.8.
Its intended consequence is that Han26 Theorem 1.2, which treats polynomials without adjoint variables, does not directly establish the general GUE conclusion.
The text leaves that consequence implicit, and “a case discussed” does not state the mathematical role of the cited question.
The [retained source inspection](../../../../audits/literature/Han26/Yin_U001.md#gue-boundary) supports this applicability distinction.

**Revision:** Name the paired Ginibre matrices explicitly, state why the appearance of their adjoints prevents direct application of Han's theorem, and identify Question 1.8 as raising that extension.
A suitable replacement is:

```tex
A general polynomial in the GUE inputs involves both the paired Ginibre matrices and their adjoints, so Han's theorem does not directly apply.
The extension to polynomials involving adjoints is raised in \cite[Question~1.8]{Han26}.
```

**Basis:** [Explicit relationships between results](../../../../../framework/rules/writing.md#direct-result-connections), [precise mathematical comparisons](../../../../../framework/rules/writing.md#mathematical-comparisons), and Yin's [introduction policy](../../../../../profiles/Yin/writing/readme.md#default-policy).
Priority: P2.
