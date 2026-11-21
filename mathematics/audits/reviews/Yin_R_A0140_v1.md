---
author: Yin
---
# Independent review of rational ranks and prescribed free word balls

## Whole finding

At 2026-11-21 05:18 UTC an agent outside the proof development reviewed the whole fixed [word-ball construction](../../ledger/Yin_L_A0065_v1.md#scope) for Yin.
The mathematical inputs were the ledger, its cited cyclic-extension argument, and the statements of the commuting comparison and the group-trace question.
The reviewer received no development dialogue, author explanation or earlier finding about this construction.
The stated implication holds for each prescribed radius and each input satisfying the division-ring and fractional-rank hypotheses.

For a nonidentity freely reduced short word of total \(z\)-exponent zero, the successive non-\(z\) letters give a nonempty reduced sequence of height-labelled generators.
Indeed, adjacent inverse letters of the same height would be separated by a power of \(z\) of exponent zero, contradicting free reduction.
Substitution shifts exactly the heights of the \(a,b\) letters by \(L\).
Disjointness of the two height intervals makes the substitution injective on the labelled generators that occur, up to the prescribed correspondence of inverses.
A nonzero final \(z\)-exponent survives directly.
In each resulting word with \(s\) reduced syllables, the degree-\(s\) monomial recording one letter per syllable has nonzero coefficient equal to the product of the exponents.
Contributing two or more letters from any one syllable would produce an adjacent repetition in this monomial.
Truncation at the largest \(s\) therefore separates the entire finite list at once.
The first nonzero homogeneous term detects nonzero powers in \(1+J\), and the degree filtration of the generated group has finitely generated free abelian factors.
Refining these factors gives the cyclic series required for \(Q\) and its finite powers.

At a cyclic extension \(H/N\cong\mathbb Z\), choose a lift \(t\) of \(1\).
Conjugation by \(t\) preserves the coefficient division closure because it preserves its generators and affiliated inverses.
The common left clearing factor makes all polynomial coefficients bounded while retaining zero kernel at both ends.
For width \(h>0\), the two end equations make restriction of a kernel vector to \(h\) consecutive slices injective.
With \(B=M^{\bar\otimes k}\bar\otimes\mathcal N(N)\), each slice is a copy of \(L^2(B)\) as a right \(B\)-module after untwisting by conjugation.
Polar decomposition of the restriction bounds the right \(B\)-dimension of the kernel by \(h\).
For its projection \(e\), each diagonal slice contributes the same trace \(\langle e1,1\rangle\) in the crossed product, since right translation by \(t\) commutes with \(e\).
Summing over the infinite cyclic quotient gives \(e=0\) by faithfulness of the trace.
Finite tracial polar decomposition supplies an affiliated inverse, and a width-zero polynomial is already a unit.
Thus the Ore skew field embeds by actual inverses at each stage, starting with the assumed \(D_k\).
For \(1\leq k\leq j\), every entry of a rational test matrix belongs to the resulting division ring for \(Q^k\).
Elimination there reduces the matrix to an identity block with zeros, and multiplication by affiliated invertible matrices preserves tracial rank.

The regular \(Q\)-coordinate gives zero trace to every nonidentity marked word in the radius-\(R\) ball.
Each recovery word has reduced length \(2L+2\), and its two tensor coordinates are respectively \(U,1\) or \(V,1\).
The substituted matrix is exactly \(P(U,V)\otimes1\), so the normalized product trace preserves its rank.
The marking is fixed, while the quotient and the words evaluating to \(U,V\) may vary with \(R\).
Consequently this construction gives finite trace agreement with a moving fractional-rank witness and leaves the [canonical regular-trace question](../../tasks/Yin_T_A0001_v1.md#contract) open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Scope](../../ledger/Yin_L_A0065_v1.md#scope) | Tracial-model hypotheses, prescribed radius, first \(j\) spatial powers, fractional-rank witness and marking. |
| [Whole finding](#whole-finding) | [Three auxiliary group generators](../../ledger/Yin_L_A0065_v1.md#three-auxiliary-group-generators) | Height separation, simultaneous detection in a truncated integral algebra, torsion-freeness and cyclic series. |
| [Whole finding](#whole-finding) | [Trace and rational ranks](../../ledger/Yin_L_A0065_v1.md#trace-and-rational-ranks) | Product trace, recovery of the input matrix, cyclic extension of each affiliated division ring and integer ranks. |
| [Whole finding](#whole-finding) | [Cyclic fraction-ring argument](../../claims/Yin_C_A0007_v8.md#the-fraction-ring-in-the-regular-representation) | Coefficient clearing, twisted right modules, diagonal traces and Ore localization as applied with a finite tracial tensor factor. |
