---
author: Yin
---
# Independent review of full regular rank from a two-dimensional unitary deformation

## Whole finding

At 2026-11-22T04:41 UTC a reviewer acting for Yin independently checked the statement and all three proof sections of C_A0118_v1.
The reviewer received the fixed proof and its review scope, had no role in its development and consulted no proof-generation dialogue, author explanations or prior finding about this Claim.
The full-rank criterion holds for all the indicated vertex-supported \(u,v\), including under the stated extension hypothesis for a quotient.
The double realizes the criterion, and its concrete torsion-free quotient admits precisely two phases of the specified family.

The diagonal edge action commutes with \(D_t\), so agreement on the edge gives the asserted representation by the universal property of the amalgam.
For an admissible quotient phase the same calculation starts with its actual representation of the quotient.
On the \(h\)-fiber the intertwining identity follows from \(\pi_t(gh)\pi_t(h)^*=\pi_t(g)\).
The entries of the twisted matrix are finite sums of left translations, so its closed range projection belongs to the output matrix von Neumann algebra.
For each output coordinate, \(W_t^*\) fixes the two vectors over the group identity, so the trace of that projection equals the sum of the two identity-fiber expectations of the ordinary amplified range projection in that coordinate.
These give two copies of the ordinary unnormalized matrix rank after summing over coordinates.
This argument uses Hilbert-space unitary conjugacy of the range projections and the identity-fiber trace formula, with no right-equivariance requirement on \(W_t\).

To check all entries after the permutations, put \(B=L_{22}+R_{22}\).
In the prescribed column order \(x_1,y_1,y_2,x_2\), the four polynomial rows are
\[
\begin{aligned}
 &(tL_{21}+R_{21},\ tU_{21},\ tU_{22},\ tB),\\
 &(V_{21},\ -tL_{21}-R_{21},\ -tB,\ tV_{22}),\\
 &(V_{11},\ -A,\ -L_{12}-tR_{12},\ tV_{12}),\\
 &(A,\ U_{11},\ U_{12},\ L_{12}+tR_{12}).
\end{aligned}
\]
The scalar case has rows \((tL_{21}+R_{21},tB)\) and \((A,L_{12}+tR_{12})\).
At zero the diagonal entries of the four-row matrix are \(R_{21},-R_{21},-L_{12},L_{12}\) and those of the two-row matrix are \(R_{21},L_{12}\).
Each such scalar with full range rank has zero kernel by polar decomposition and faithfulness, so the successive equations force every coordinate of a kernel vector to vanish.
For either square matrix polynomial \(Q\), full rank at zero gives injectivity on all input coordinates there.
If a vector polynomial of degree at most \(N-2\) is nonzero, its lowest nonzero coefficient stays nonzero after multiplication by \(Q\).
The product has degree at most \(N-1\), and therefore its evaluations at \(N\) distinct phases determine it by Vandermonde inversion.
This gives the required dimension inequality by injecting \(N-1\) copies of the input space into the direct sum of the closed ranges at those phases.
Invertible row scalings and permutations there give \(4(N-1)\le 2N\operatorname{rk}_G M\) and \(2(N-1)\le 2N\operatorname{rk}_G p\).
Arbitrarily large \(N\) gives the respective upper bounds \(2\) and \(1\) as equalities.
Full rank gives a two-sided affiliated inverse for \(p\), and elimination of the lower left block followed by the upper right block leaves the diagonal \(p,-p-vp^{-1}u\).
The second entry is \(-p[1+(p^{-1}v)(p^{-1}u)]\), giving rank one in precisely the displayed factor order.

Gardam's description gives the normal \(\mathbb Z^3\), its index four, the distinct cosets of \(1,a,b,ab\) and the torsion-freeness of \(P\). [Gardam, Section 3.1, pp. 4–5](../../literature/pdf/Gar21--arxiv-v4.pdf#page=4).
The amalgam acts without inversions on its Bass–Serre tree, so a finite cyclic subgroup fixes a vertex and is trivial by torsion-freeness of the vertex group.
The abelianized relators impose only \(4a_1=4a_2=4b=0\), proving the abelianization and character assertions, including the obstruction to a retraction onto an infinite cyclic group.
The proposed vertex matrices satisfy the relators since their squares are respectively \(I,-I\).
In the amalgam, \(a_1,a_2\) lie in distinct vertex complements while \(1,b\) are distinct edge elements.
The coefficients of \(a_1,a_2,1\) force \(\alpha+\beta=\alpha+\gamma=\alpha+\beta+\gamma=0\), hence independence.
Only \(\lambda_G(a_1)\) contributes to \(L_{12}\) and only \(\lambda_G(a_2)\) to \(R_{21}\).
On the edge vectors \(\delta_{b^n}\) the commutator sends distinct orthonormal inputs to the distinct vectors \(\delta_{a_1b^n}\), since it retains precisely the left vertex term there.
The folding kernel meets every conjugate of a vertex group trivially by normality and vertexwise injectivity, hence acts freely on the tree and is free.
The quotient is virtually abelian, and Linnell's torsion-free, free-by-elementary-amenable theorem therefore supplies the claimed integral ranks for the whole double.

For the concrete quotient, conjugation by \(a\) inverts \(\langle b^2\rangle\), so conjugation by \(a^{-1}\) acts on it by the same inversion.
Inverting the second defining relation gives \(b^{-1}a^{-2}b=a^2\).
Thus \(a\mapsto a^{-1}, b\mapsto b\) is an involutive automorphism, and the two vertex maps into \(P\times P\) are injective with the specified common image of \(b\).
The image subgroup is torsion-free, and \(a_1\ne a_2\) by the second coordinate while the first separates both from \(1,b\), giving the same coefficient independence.
In either quotient the mixed commutation relator forces equality of the diagonal products \(\operatorname{diag}(t^{-1},t)\) and \(\operatorname{diag}(t,t^{-1})\).
In the concrete quotient the first projection gives \(t=1\).
The character \(i^{\eta(g)-\eta(h)}\) takes the values \(1,-1,1\) on \(a_1,a_2,b\), respectively, so twisting gives \(t=-1\).
Both representations also pull back to the quotient defined by adjoining the mixed relator.
These are the only admissible phases of this vertex family there.
This restriction prevents the limit in the Vandermonde argument on those quotients and gives no counterexample to an endpoint rank.
The general three-coefficient Schur problem and Task A0001 remain open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0118_v1.md#statement) | Both exact regular ranks, the ordered Schur expression, arbitrary vertex inputs and the infinite-phase assumption. |
| [Whole finding](#whole-finding) | [Trace and specialization](../../claims/Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization) | The identity-fiber calculation, every polynomial entry, triangular kernels, rank interpolation and affiliated elimination. |
| [Whole finding](#whole-finding) | [Cyclic-edge double](../../claims/Yin_C_A0118_v1.md#a-double-over-an-infinite-cyclic-subgroup) | Group structure, explicit vertex representations, coefficient independence, infinite ordinary commutator rank and Linnell's hypotheses. |
| [Whole finding](#whole-finding) | [Mixed relation](../../claims/Yin_C_A0118_v1.md#a-mixed-relation-allowing-exactly-two-phases) | Both quotients and both directions of the admissible-phase test, preservation of the vertices and independent coefficients in the concrete quotient. |
| [Whole finding](#whole-finding) | [Polynomial rank bound](../../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | Degree-one case at zero for any finite set of distinct admissible phases. |
| [Whole finding](#whole-finding) | [Schur problem](../../claims/Yin_C_A0116_v1.md#statement) | Comparison with the three-coefficient residual in its original factor order. |
| [Whole finding](#whole-finding) | [Linnell's theorem](../literature/Lin93/Yin_U001.md#group-class-and-exact-theorems) | Applicability of Theorem 1.3 to the folding kernel and quotient, using its recorded statement. |
