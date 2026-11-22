---
author: Yin
---
# Independent review of the repeated denominator tests for an inverse layer

## Whole finding

At 2026-11-22T04:20 UTC a reviewer acting for Yin independently checked the whole statement and both proof sections of C_A0117_v1.
The reviewer took no part in developing the proof and received its fixed text and the assignment without its development discussion, author explanations or a previous verdict on C_A0117_v1.
The reviewer also consulted the cited inverse-layer definition, the two Schur realization references and the preceding two-by-two result with its independent review.
The directed union, the signed chain construction and the conditional equivalence with the full next-layer assertion all hold with the stated quantifiers.

Write \(p=s u_i t\) for the prefix, the selected factor and the suffix of the proposed product.
All three are units in the affiliated algebra, including the empty products, so \(t p^{-1}s=t(t^{-1}u_i^{-1}s^{-1})s=u_i^{-1}\).
This proves simultaneous containment for any finite list, and each algebra in the proposed union lies in the next layer by its defining recursion.
The identities \(a=p^{-1}(pa)\) and \(p^{-1}=p^{-1}1\) cover every generator of each expression.
A linear combination with a scalar constant has numerator \(\lambda p+\sum_i\lambda_i a_i\).
Under \(P_k(G)\), a nonzero such numerator and \(p^{-1}\) are both affiliated units.

Put \(P=pI_h\) and \(T=P^{-1}N\) for a chain of length \(h\).
Its factorization \(P-N=P(I-T)\) gives the two-sided inverse \((I+T+\cdots+T^{h-1})P^{-1}\) since \(T^h=0\).
For \(h>1\), the only path from the first to the last state uses \(h-1\) consecutive entries of \(T\), with one additional right factor \(p^{-1}\) from the diagonal.
For \(h=1\) the inverse entry is just \(p^{-1}\).
The minus sign on the initial row entry cancels the minus sign of the Schur term, giving \(v_0p^{-1}v_1\cdots p^{-1}v_h\) in the original order, including signs absorbed in the coefficients.
Disjoint chains have zero cross terms, so their sizes add to the number of inverse occurrences in the chosen expansion.
This count depends on the expansion and asserts no minimal size.
For a general strictly upper triangular \(N\), nilpotence of \(P^{-1}N\) still puts every entry of \(L^{-1}\) in \(B[p^{-1}]\).

For \(S=d-cL^{-1}b\), multiply the bordered matrix on the left by \(\left(\begin{smallmatrix}I&0\\-cL^{-1}&1\end{smallmatrix}\right)\) and on the right by \(\left(\begin{smallmatrix}I&-L^{-1}b\\0&1\end{smallmatrix}\right)\).
The result is \(\operatorname{diag}(L,S)\), so the unnormalized matrix rank is \(q+\operatorname{rk}_G(S)\).
The group trace is faithful and normalized, hence a scalar affiliated operator has rank zero exactly when it vanishes.
At rank one its range and initial supports both equal the identity by polar decomposition and finiteness, giving an affiliated inverse.
Consequently \(P_{k+1}(G)\) gives the required ranks for every test, since \(P_k(G)\) makes each nonzero \(p\in B\) an allowed denominator.
Conversely the disjoint-chain tests cover every expression using at least one inverse, and \(P_k(G)\) already covers the \(q=0\) case.
At \(k=0\) every bordered matrix has entries in \(\mathbb CG\).

At \(q=1\), \(N=0\), so the residual is exactly \(d-cp^{-1}b\).
The three-coefficient reduction of C_A0116_v1 addresses this entire size under the same scalar premise.
It preserves the rank of the residual through the ordered mixed product in that reduction.
Larger \(q\) encodes sums and products with repeated inverses, and their endpoint ranks remain open for general groups under the stated premise.
The comparison to C_A0012_v1 concerns the Schur realization form and imports no specialization hypothesis.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0117_v1.md#statement) | Directed union, one denominator, chain size, both directions of the full next-layer test and its specializations. |
| [Whole finding](#whole-finding) | [Rewriting the actual inverses](../../claims/Yin_C_A0117_v1.md#rewriting-the-actual-inverses) | The ordered inverse product, empty list, normalized generators and linear combinations. |
| [Whole finding](#whole-finding) | [Chain realization and rank](../../claims/Yin_C_A0117_v1.md#chain-realization-and-rank) | Ordered triangular inverse, signed boundaries, disjoint sums, unrestricted triangular converse and endpoint ranks. |
| [Whole finding](#whole-finding) | [Inverse-layer recursion](../literature/Yin20/Yin_U002.md#61-definition-iv55-and-all-parts-of-remark-iv56) | Adjoining exactly the inverses of scalar units present at the preceding stage. |
| [Whole finding](#whole-finding) | [Affiliated elimination](../../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step) | Order of the triangular factors and dimension invariance, applied here to the independently inverted block. |
| [Whole finding](#whole-finding) | [Two-by-two reduction](../../claims/Yin_C_A0116_v1.md#reducing-every-two-by-two-input-to-three-coefficients) | Scope of the three-coefficient normal form at one scalar Schur step. |
| [Whole finding](#whole-finding) | [Polynomial Schur realizations](../../claims/Yin_C_A0012_v1.md#rational-expressions-and-explicit-polynomial-schur-realizations) | Comparison with the general shape of a rational expression realized by a finite Schur complement. |
