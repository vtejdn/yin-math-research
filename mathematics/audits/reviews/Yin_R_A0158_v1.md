---
author: Yin
---

# Independent review of full regular rank in the congruence subgroup double

## Whole finding

At 2026-11-22T04:50 UTC an agent acting for Yin independently reviewed the statement and all four proof sections of C_A0121_v1.
The reviewer took no part in developing the claim and received the fixed claim and the assignment without the development dialogue, an author explanation or an earlier verdict on this claim.
The action obstruction, full ranks for every indicated pair \(u,v\), generating-support example and restriction on the commuting quotient hold as stated.

For an element of prime order \(q\) in the level-three kernel, take \(k\) to be the minimum finite \(3\)-adic valuation of an entry of \(g-I\).
When \(q\ne3\), division of the binomial expansion of \(g^q-I\) by \(3^k\) leaves \(qB\) modulo \(3\).
When \(q=3\), division by \(3^{k+1}\) leaves \(B\) modulo \(3\), since the exponents in the two remaining terms exceed \(k+1\) for every \(k\ge1\).
Either residue is nonzero, which rules out prime-order elements and hence all nontrivial torsion.
The powers of \(b\) exhibit an infinite cyclic edge, and the vertex-type-preserving action on the Bass–Serre tree places each finite-order element inside a conjugate of a torsion-free vertex group.

Corollary 1 on printed page 148 of Shalom's paper gives a positive Kazhdan constant for the unit elementary generators of \(\operatorname{SL}_n(\mathbb Z)\) for \(n\ge3\), including the group needed here.
The review uses this published conclusion at \(n=3\). [Shalom, *Bounded generation and Kazhdan's property (T)*](https://www.numdam.org/article/PMIHES_1999__90__145_0.pdf#page=5)
The finite quotient modulo \(3\) makes the transversal in induction finite.
For a finite test set \(S\), the squared norm of each induced displacement is the average, over representatives \(r\), of terms \(\|\sigma(v)^{-1}\xi-\xi\|^2\) from \(s^{-1}r=r'v\).
A nonzero invariant induced function is constant on the group and its value satisfies the \(V\)-covariance condition, so \(V\) inherits property (T).
Følner indicators for an amenable action give almost invariant vectors also after restriction to \(V_1\).
A nonzero \(V_1\)-fixed vector would be constant on an \(H\)-orbit where it is nonzero, contradicting square summability when \(H\) acts freely.
This applies to every nonempty discrete \(G\)-set, including every coset space in the hypothesis of C_A0119_v1.

The product of matrix units \(E_{12}E_{23}=E_{13}\), with the reverse product and the subsequent mixed terms zero, gives \(a=[b,I+3E_{23}]\).
Thus each scalar character sends \(a\) to \(1\).
In the reduction modulo \(5\), the map \((i,j)\mapsto I+3iE_{12}+4jE_{13}\) is an injective homomorphism from the additive group \(\mathbb F_5^2\).
On each right coset of its image, the restricted left regular representation contains every character of this group once.
In the two copies, the shift of the second character index at fixed first index pairs every first-copy vector with a distinct second-copy vector.
On passing to the sum and difference basis, \(b\) acts by the same fifth root of unity on both vectors in a pair, whereas both off-diagonal coefficients for \(a\) equal \(\omega^l(1-\omega)/2\).
Their absolute values are positive and independent of \(l\), giving bounded inverses for the two \(d\)-dimensional blocks and hence for the regular pivots after tensoring with a group translation.

The change of basis on the right vertex commutes with the edge representation for every unit phase.
The fiberwise unitary intertwiner is the identity over the neutral group element, where the group trace reads the diagonal entries of the closed range projection.
With unnormalized matrix trace this multiplies both original ranks by \(2d\).
To verify the block triangularity, set \(A=L_{11}+R_{11}\), and write \(U,V'\) for the unbent twists of \(u,v\).
After scaling the second auxiliary output in each copy by \(t\), the negative powers disappear and the remaining polynomial has degree at most one.
For the scalar, interchanging the two block rows gives diagonal \(R_{21},L_{12}\) and upper right block zero at \(t=0\).
For the matrix, use the row order \(2,4,3,1\) and column order \(1,3,4,2\) of C_A0118_v1.
At zero the four block rows are
\[
 (R_{21},0,0,0),\quad (V'_{21},-R_{21},0,0),\quad
 (V'_{11},-A,-L_{12},0),\quad (A,U_{11},U_{12},L_{12}).
\]
Thus the two zero evaluations are invertible by successive substitution for arbitrary \(u,v\).
For either polynomial \(F\), multiplication by \(F\) is injective on vector polynomials of degree below \(N-1\), since the first nonzero coefficient survives multiplication by \(F(0)\).
Evaluation on \(N\) distinct phases is injective on the resulting polynomials of degree below \(N\) by Vandermonde interpolation.
The dimension comparison with the sum of the closed evaluation ranges gives the stated factor \(N-1\) for both block sizes.
Dividing by \(2dN\) and taking \(N\) arbitrarily large yields ranks \(1\) and \(2\).
Full rank gives the affiliated inverse of \(p\), and invertible row and column elimination gives the full-rank Schur complement \(-p-vp^{-1}u\).
Left multiplication by \(-p^{-1}\) yields the claimed affiliated unit in precisely the stated product order.

The unit elementary matrices generate \(\operatorname{SL}_3(\mathbb Z)\), and finite index gives a finite Schreier generating set of \(V\).
Adjoining \(a^2\) and removing the identity preserve generation.
The normal form theorem gives \(V_1\cap V_2=H\), while the \((1,3)\) entry distinguishes \(a^2\) from \(a\), the identity and all powers of \(b\).
Comparing the coefficients at \(a_1^2,a_2^2\) kills the two multipliers of the vertex sums.
The remaining coefficient at the identity kills the multiplier of \(p\).

In the commuting quotient, an infinite set of unit phases forces every Laurent coefficient of the matrix commutator to vanish.
Its \(t^{-1}\) coefficient has diagonal entries \(A_{12}B_{21}\) and \(-B_{21}A_{12}\).
The two zero products respectively give \(\operatorname{im}B_{21}\subseteq\ker A_{12}\) in \(E_2\) and \(\operatorname{im}A_{12}\subseteq\ker B_{21}\) in \(E_1\).
Rank-nullity gives both stated bounds, including for unequal multiplicities.
The quotient conclusion concerns the two blocks of this deformation.
The general three-coefficient problem and the Atiyah question for arbitrary matrices on the double remain open in this argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0121_v1.md#statement) | The cyclic double, the action obstruction, both full ranks, the affiliated unit and the generating-support assertion. |
| [Whole finding](#whole-finding) | [Amenable action obstruction](../../claims/Yin_C_A0121_v1.md#the-obstruction-to-an-amenable-action) | Torsion, property (T) and its restriction to a finite-index subgroup, and the Følner-vector contradiction. |
| [Whole finding](#whole-finding) | [Finite quotient](../../claims/Yin_C_A0121_v1.md#the-finite-quotient-detecting-the-commutator) | Commutator identity, finite abelian subgroup, character pairing and the two boundedly invertible blocks. |
| [Whole finding](#whole-finding) | [Regular rank computation](../../claims/Yin_C_A0121_v1.md#the-regular-rank-computation) | All unit phases, amplified trace, triangular specializations, limit, Schur complement and linear independence. |
| [Whole finding](#whole-finding) | [Commuting relation](../../claims/Yin_C_A0121_v1.md#a-commuting-relation-in-the-two-weight-deformation) | The Laurent coefficient and both bounds from complementary domain dimensions. |
| [Whole finding](#whole-finding) | [Two-dimensional calculation](../../claims/Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization) | The intertwiner and block permutations applied here with equal weight multiplicities \(d\). |
| [Whole finding](#whole-finding) | [Vandermonde bound](../../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | The degree-one inequality at zero for the two matrix polynomials. |
| [Whole finding](#whole-finding) | [Coamenable subgroup criterion](../../claims/Yin_C_A0119_v1.md#statement) | The verified obstruction excludes its free-edge action hypothesis. |
| [Whole finding](#whole-finding) | [Three-coefficient problem](../../claims/Yin_C_A0116_v1.md#statement) | Identification of the Schur expression and the scope of this family's conclusion. |
