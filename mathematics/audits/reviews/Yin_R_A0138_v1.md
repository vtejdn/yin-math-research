---
author: Yin
---
# Independent review of the quaternion models and the exclusion for group elements

## Whole finding

On 2026-11-21 at 05:28 UTC an agent acting for Yin independently checked the [statement](../../claims/Yin_C_A0102_v1.md#statement) and the complete [argument](../../claims/Yin_C_A0102_v1.md#argument) of C102 v1.
The reviewer was outside proof development and received the review scope and notice of a pending addition.
The review used the fixed proof and its cited mathematical inputs, with no proof-generation discussion, author explanation or earlier verdict on this claim.
I find all five assertions proved with their stated trace conventions.

For the simultaneous induction, the two coefficient algebras on \(n-1\) variables have indices \((n-1,I)\) and \((n-1,I\cup\{h\})\), both within the region \(n+|I|\le j\).
Square-class independence survives adjoining rational variables, so the second algebra has the direct decomposition \(B\oplus B\sqrt{c_h}\) over the first.
The involution on these coefficients fixes every earlier factor.
At the simple zero \(c_h\), the coefficient of \(z\) in \(g(c_h+z)\) is \(c=-\prod_{i\ne h}(c_i-c_h)\).
Consequently the substitutions \(z=W^2/c\), \(u_n=d(z)\sqrt{c_h}\) and \(v_n=e(z)W\) have the prescribed squares and anticommute, including the single-factor case with \(c=-1\).
The two powers of \(W\) modulo two separate the two terms of (11), and the two independent summands of \(B\oplus B\sqrt{c_h}\) separate the coefficients within each term.
Expansion over \(B\) is injective on rational dependence on the central variable, as one sees in any basis of \(B\) over its center.
Thus each tensor algebra under the degree bound embeds in a skew Laurent-series division ring and is itself a division algebra by finite dimensionality.

On \(J=[-3,-2]\), the factor \(c_1-t\) is negative and every remaining \(c_i-t\) is positive.
The displayed skew-adjoint matrices therefore realize the quaternion relations at every point.
For product measure the zero set of a nonzero scalar denominator is null by induction and Fubini's theorem for polynomials.
Evaluation extends to the rational coefficient field, and the inverse of each nonzero algebra element evaluates to its two-sided affiliated inverse.
Division-algebra row and column operations take a rectangular matrix of rank \(r\) to an identity block of size \(r\), whose ordinary fiber rank is \(2^n r\).
Thus all the claimed rational matrix ranks at powers \(1,\ldots,j\) are integral.
The inverse Cayley formulas recover \(u,v,t\) and every nonzero polynomial denominator in \(t\) has its inverse in the actual division closure.
Conversely \(Q(t)\) is already division closed there.
Continuous functional calculus on \(tI\) recovers the two constant matrix generators by rescaling \(u,v\), as required for the assertion about \(M_2(C(J))\).

For each sign choice of the square roots the two diagonal terms and the off-diagonal terms of \(Z\) give determinant \(a^2-tb^2-g=0\).
Its off-diagonal entry has magnitude \(\sqrt{-g(t)}>0\), so its fiber rank is one for every sign choice.
The ordered factors \((1+U)^j\) and \(1+V\) in (23) are invertible and carry this rank to the entire evaluated polynomial.
The distinct signed sums forming the conjugates of \(\alpha\) follow from multiquadratic basis independence, so their number is \(d=2^j\) and \(\alpha\) generates \(K\).
Restriction of scalars uses a single copy of the field for the entire exterior tensor.
After complexification there are exactly \(d\) summands, with the same embedding on all \(n\) factors of any one summand.
Each tensor of evaluated copies of \(P\) consequently has fiber rank one in dimension \(2^n\), giving rank \(d/2^n\) under the unnormalized \(d\)-fold matrix amplification.
This proves the first failure at \(n=j+1\), including \(j=1\), and shows why the boundary \(d=2^j\) matters in the comparison. [Degree bound](../../claims/Yin_C_A0097_v2.md#statement)

The right \(D\)-kernel of \(R_1\) has dimension \(d/2\) by the same rank calculation.
A matrix \(W\) of basis columns and its left inverse give an injective fiber map from a space of dimension \(d\) into \(\ker R_1(t)\) almost everywhere.
The latter has dimension \(d\) because the \(d\) conjugate blocks each have one-dimensional kernels, so the map is onto this kernel.
Multiplication by \(\alpha\) has a distinct eigenvalue on each of those lines, and the intertwining equation transports all \(d\) lines to the compressed matrix \(C(t)\).
The trace of each resulting orthogonal kernel projection is \(1/2\) after integration, including when the change of basis is unbounded.
For the quartic example the product over the four sign choices is \((T^2+3)^2+40\).

The regular group argument uses the Haar spectral law of each infinite-order element so that \(g\pm1\) and \(h\pm1\) are affiliated units. [Cyclic calculation](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions)
Anticommutation would make \(h\) commute with \(u^2\) and hence with \(g+g^{-1}\) by (33).
Applying this last identity to \(\delta_e\) forces \(hgh^{-1}\) to equal \(g\) or \(g^{-1}\).
In the first case two commuting units cannot anticommute in characteristic zero.
In the second case conjugation by \(h\) negates \(u\), so conjugation by \(u\) negates \(h\) and sends \(v\) to \(v^{-1}\).
The resulting identity \(v^2=-1\) would yield \(h^2+1=0\), contrary to the regular action on \(\delta_e\).

In the model, the generator moment in (17) is strictly negative, and the central element \(U+U^{-1}\) makes the displayed four-word element vanish.
The four words are distinct in \(F_2\).
These calculations establish precisely where the noncanonical representation loses group-algebra information.
The joint scalar-sample proof assumes coefficients affiliated with one abelian algebra, whereas \(uv=-vu\ne0\) here. [C100](../../claims/Yin_C_A0100_v1.md#common-roots-for-two-independent-samples)
Theorem 9.12 and Corollary 9.13 of JZ19 use sofic approximation, the arithmetic finiteness in Theorem 8.1 and the centralizer estimates to exclude eigenvalues outside the stipulated field.
The quaternion construction leaves the degree-independent transfer question for general canonical group representations open. [JZ19, pp. 528–529](../../literature/pdf/JZ19.pdf#page=65) [Coefficient induction](../literature/JZ19/Yin_U001.md#base-change-proof)

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0102_v1.md#statement) | All five assertions, including every arity and embedding, both trace normalizations, the first failing power and the restriction on canonical group elements. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0102_v1.md#argument) | Skew-series induction, tracial realizations, division closure, Cayley denominators, scalar restriction, kernel compression, nonfaithfulness, the two group-conjugation cases and scope of the source comparisons. |
| [Whole finding](#whole-finding) | [Cyclic rational functions](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) | Affiliated invertibility of the nonzero cyclic denominators in the regular representation. |
