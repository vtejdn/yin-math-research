---
author: Yin
---
# Whole-proof review of the two free-Haar packing obstructions

## Whole-proof finding

At 2026-11-13T17:42 UTC the check_defect agent for Yin independently reviewed the [statement](../../claims/Yin_C_F0235_v1.md#statement) and [complete argument](../../claims/Yin_C_F0235_v1.md#argument) of C_F0235 v1, candidate dated 2026-11-13T17:40.
Both obstructions for the fixed four-value shift and the exact optimum for the orthogonal family hold as stated.
The reviewer had worked on other free-Haar transformations and on spectral-coordinate changes in F0011, but had no role or shared development context in this candidate's construction, its packing examples or its proof.
The check used the fixed claim, its six declared inputs and the original HL00 theorem, without consulting exploration notes, author explanations or prior review conclusions about the claim.

### Positive mass and the numerical range

The Haar Laurent-word computation and the reduction of mixed centered words give the actual vacua at both coordinates.
The free-normal strong-domain theorem applies to the pair and separately to its adjoint pair.
Multiplying \(U\) on the left by any \(w^*\in N\) with \(w\) unitary preserves its Haar law and its freeness from \(N\).
In a test word expanded into \(U^{\pm1}\), a switch from a positive to a negative power across a centered \(N\)-block preserves that centered block.
The reverse switch conjugates it by \(w\), which preserves centering.
At intervening equal signs a scalar term can merge powers only with the same sign.
Every surviving reduced term has at least one nonzero \(U\)-power and zero trace, including terms with exterior \(N\)-coefficients by the reduced-word conditional expectation.
This justifies the assertion for arbitrary measurable \(w\in N\).

In the retained 33-page HL00 author preprint, printed and PDF p. 14, Theorem 4.4(i) describes the entire rotation-invariant Brown support of a Haar unitary times a free positive modulus with non-Dirac law.
For modulus \(h^{-1}\) its inner and outer radii are \(1/\sqrt{65/32}\) and \(\sqrt{65/8}\), respectively.
They lie strictly on either side of one.
The claim uses inclusion of Brown support in the operator spectrum to deduce noninvertibility at one.
The free product with the nonconstant modulus satisfies the hypotheses of the support computation. [HL00, Theorem 4.4(i)](../../literature/pdf/HL00.pdf)
Multiplying by \(h\) preserves noninvertibility.
Finiteness turns a polar isometry with full initial support into a unitary, so noninvertibility implies zero belongs to the spectrum of the modulus.
If a positive-radius cutoff had zero trace, faithfulness and spectral calculus would make the modulus bounded below, a contradiction.
The omitted-shift kernel result separately gives decay of the cutoff traces to zero.

Conjugation by \(W\) gives the real part of \((VW^*)^*(U-b)\).
The symmetry of \(S=\operatorname{Re}(w^*U)\) persists jointly with \(q\) by freeness, so the normalized corner law of \(qSq\) is symmetric.
Its second moment is \(\tau(q)\tau(S^2)=1/4\), giving a negative spectral endpoint at most \(-1/2\).
Subtracting the \(q\)-corner of \(\operatorname{Re}(w^*b)\) shifts that bound upward by at most \(1/4\).
Thus no fixed half-plane tolerance \(\kappa r\) works as \(r\downarrow0\), even when the two unitaries vary with \(r\).

### Conditional projections and the optimum

On each of the two atoms of \(B\), the sign takes both values on equal arcs and \(h\) is constant, giving \(\mathbb E_B b=0\).
Reduced words in \(B*W^*(V_0)\) containing a centered Haar power have zero expectation onto \(N\).
At the junction of two such words separated by \(x\in N\ominus B\), the new \(N\)-letter \(b_1xb_2\) has zero trace, and so their product again has zero conditional expectation.
With the other word fixed and bounded, multiplication and conditional expectation are continuous in \(L^2\), so successive approximation covers all the bounded inputs in (2).

Writing \(k=\mathbb E_B e\), the two conditional identities yield \(\mathbb E_N(exe)=kxk\) for \(x=c-\mathbb E_B c\).
The bound \(k\le2t\) uses the trace \(1/2\) of each \(B\)-atom.
It gives \(\|exe\|_2^2\le2t\|xe\|_2^2\) by commutation in \(N\).
The uncompressed and compressed mixed products against \(c_Be\) and \(ec_Be\) have zero trace by conditioning onto \(B\), so the same orthogonality holds after left multiplication by \(1-e\).
The commutator thus contributes at least \(\sqrt{1-2t}\|xe\|_2\).
The approximation term contributes at least \(\|(b-x)e\|_2\), and their sum is at least \(\sqrt{1-2t}\|be\|_2\), as \(0\le\sqrt{1-2t}\le1\).
Here \(\|be\|_2\ge\sqrt t/4\).
Taking \(c=b\) proves the asserted divergence with the indicated normalization.
For any spectral partition, \(t=\sum_l t_l\) and \(t_l\ge0\), giving \(m=t^2/\sum_l t_l^2\ge1\).
Inserting both errors into the definition of \(R\) gives the claimed lower bound.

For \(b=\lambda Y\), all exact projections are spectral arcs of the single Haar unitary \(Y^*U\), free from \(N\).
Their traces and pairwise disjointness follow from the half-angle \(2\arcsin(r/2)\) and the stated centers and radii.
Freeness gives \(t\|b-c\|_2^2\) for the squared approximation error and \(2t(1-t)\|c-\tau(c)\|_2^2\) for the squared commutator error, including complex-valued \(c\in N\).
For \(t\le1/2\), subtracting the scalar part of \(b-c\) contracts its norm and \(b\) is centered.
The triangle inequality then gives an error sum at least \(\sqrt t\,\|b\|_2=\sqrt t\).
The zero approximant with its one-piece partition attains equality and \(m=1\), giving the infimum \(1+1/r\).
For the orthogonal family itself \(V=-b\) gives a nonnegative real part, as \(\operatorname{Re}(b^*U)\le1\).
The examples test the sufficiency hypotheses for estimates in C_F0231 and C_F0233.
They establish divergence of the approximation cost on the selected tests.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0235_v1.md#statement) | Both fixed-shift conclusions, the free-pair domains, exact nonzero cutoffs tending to zero in trace and the separate orthogonal family. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0235_v1.md#argument) | Haar multiplication, Brown support, corner symmetry and moments, conditional word orthogonality, the norm bounds and scalar attainment. |
| [Whole-proof finding](#whole-proof-finding) | [Haar vacuum computation](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Laurent powers and vacuum extension on the free-product core. |
| [Whole-proof finding](#whole-proof-finding) | [Free normal coordinates](../../claims/Yin_C_F0162_v1.md#statement) | Part B giving actual strong domains both for the Haar pair and after taking adjoints. |
| [Whole-proof finding](#whole-proof-finding) | [HL00 support interface](../literature/Miy26/Yin_U004.md#miy26-u004) | Theorem 4.4(i) with the nonconstant invertible modulus \(h^{-1}\), and inclusion of its annular Brown support in the operator spectrum. |
| [Whole-proof finding](#whole-proof-finding) | [Omitted-shift singular law](../../claims/Yin_C_F0229_v1.md#statement) | Absence of kernel for \(U-b\), implying the cutoff traces tend to zero. |
| [Whole-proof finding](#whole-proof-finding) | [Half-plane criterion](../../claims/Yin_C_F0231_v1.md#statement) | Fixed \(\kappa\), independently variable omitted unitaries, and the allowed tolerance \(-\kappa r\). |
| [Whole-proof finding](#whole-proof-finding) | [Finite-spectrum criterion](../../claims/Yin_C_F0233_v1.md#statement) | Item 2, both errors in \(R\), partition multiplicity \(m\), and the one-piece scalar choice. |
