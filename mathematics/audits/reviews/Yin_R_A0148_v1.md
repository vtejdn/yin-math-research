---
author: Yin
---
# Independent review of the rank formula for rows in distinct free factors

## Whole finding

At 2026-11-22T04:09 UTC a reviewer acting for Yin independently checked the complete statement and proof of C_A0111_v1.
The reviewer received the fixed Claim and the review assignment, had no part in developing the proof, and consulted its cited rank identity and the Task contract.
The assignment mentioned a possible grading issue but supplied no mathematical derivation, development dialogue or previous verdict on this Claim.
The formula, the original-row witness and both conclusions about scalar Schur complements hold under their stated hypotheses.

For \(h\in H_k\), the sets \(H_k\) and \(L\setminus H_k\) are invariant under left multiplication by \(h\).
On the second set at least one syllable outside \(H_k\) survives, and the last factor stays the same even when the leading syllable cancels.
On the first set \(D_i\) equals \(1-E\) when \(k=i\) and zero otherwise.
This gives the sign \(hE-Eh\) in (2).
For \(\xi\in\ker N\), the projection onto \(\ker N^*\) kills both terms of the commutator applied to \(\xi\) after projection, using \(N\xi=0\) and \(q_NN=0\).
The only surviving row before projection is \(i\), where \(E\sum_j a_{ij}\xi_j=0\) and \(E\xi_j=\xi_j(e)\delta_e\).
Translating the resulting vector equation first gives an operator equation on a dense set, then translating \(\xi\) gives it at each group coordinate.
This uses the ordinary complex coefficients \(\xi_j(t)\) in the bilinear row-column pairing and requires no grading on the factors.

For \(I=\{i:q e_i\ne0\}\), a vector in \(\ker M^*\) has zero component outside \(I\), since \(e_i^*q=(qe_i)^*\).
Conversely an element of \(\ker M_I^*\) extends by zero to \(\ker M^*\).
These identifications give (4) with unnormalized output trace.
The row density hypothesis forces every extracted scalar to vanish for \(i\in I\), since \(q_Ie_i\) is a nonzero bounded operator killing its range.
Thus each coordinate of a kernel vector lies in the common nullspace \(W_I\).
Pointwise substitution in the convolution sum proves the reverse inclusion, including when \(W_I\) is zero or all of \(\mathbb C^n\).
For an arbitrary \(J\), restricting the domain to its constant coefficient nullspace bounds the row-set rank by \(d_J\), and the omitted output has dimension \(m-|J|\).
Equality for \(I\) therefore attains the minimum.
In the absence of row density, a strict deficit forces the kernel of \(M_I\) to contain a vector outside \(\ell^2(L;W_I)\).
One of its coordinates then produces a nonzero scalar killed by the nonzero \(q_Ie_i\).
The orthogonal coset decomposition gives nondense range already over \(H_i\) and hence a nonzero kernel for the adjoint there.
The same decomposition at \(L\leq G\) preserves the trace used in all these comparisons.

For a nonzero second row in the two-by-two case, each singleton contributes at least two to the minimum.
Rank one occurs precisely when all coefficient rows lie on the same line, whose first coordinate cannot vanish identically because \(a\ne0\).
This gives exactly the simultaneous proportionality stated in the Claim.
A zero second row yields the separate zero-complement case.
At any subsequent step the leading pivots and the new entry depend only on the original rows and columns selected for that border.
All such borders inherit the scalar density assumptions, since deleting columns only decreases the linear span.
After \(k\) legal pivots, unit triangular elimination gives the residual rank as the integer rank of the border minus \(k\).
Rank zero or one for a scalar gives zero or an affiliated unit by faithfulness, polar decomposition and finiteness.
Row and column group translations preserve the ranks of the corresponding submatrices, so the coefficient test can be used on a translated matrix satisfying the hypotheses.
Two identical rows \((1,h)\) over one infinite cyclic factor indeed have rank one and two-dimensional coefficient span.
Consequently this calculation leaves open the unrestricted first Schur complement in A0001.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0111_v1.md#statement) | All row subsets under the free product embedding, density test, converse witness, exact two-row criterion and successive scalar pivots. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0111_v1.md#argument) | The complete proof from right coset decomposition and equation (2) through the witness and both Schur conclusions. |
| [Whole finding](#whole-finding) | [Rank and witness](../../claims/Yin_C_A0111_v1.md#the-rank-formula-and-the-witness) | The uniform upper bound, identifying the extremizing row set and obtaining a scalar in an original row on strict deficit. |
| [Whole finding](#whole-finding) | [Scalar Schur complements](../../claims/Yin_C_A0111_v1.md#scalar-schur-complements) | Vanishing criterion, legal elimination with ordered borders, translations and the cyclic example. |
| [Whole finding](#whole-finding) | [Affiliated rank identity](../../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) | Rank invariance under actual affiliated units and its support-trace interpretation. |
