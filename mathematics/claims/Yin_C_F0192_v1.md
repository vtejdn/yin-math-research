---
author: Yin
---

# Haar coefficient gauges, sparse-cycle limits and eventual invertibility

This theorem was developed on 2026-11-05 for the [Haar affine-pencil Task F0015](../tasks/Yin_T_F0015_v1.md#contract).
Its [independent review](../audits/reviews/Yin_R_F0197_v1.md#independent-haar-structural-proof) covers the exact restricted assertions and leaves the unrestricted dense-coefficient determinant contract unresolved.
No novelty or priority claim is made.

<a id="statement"></a>
## Exact statement

Use exactly the fixed coefficients, independent full-complex Haar inputs within each dimension, free Haar tuple, normalized trace and ordinary determinant convention in [F0015](../tasks/Yin_T_F0015_v1.md#input-model-and-ordinary-determinant).
All coefficients and auxiliary dimensions remain fixed as the physical dimension grows.
The following assertions hold.

1. Every permutation of the coefficient positions \(0,1,\ldots,r\) preserves the finite normalized logarithmic determinant marginal laws and the free target.
   The dimensionwise transformations realizing these permutations preserve both allowed cross-dimensional coupling regimes.
2. If \(\ker L=\{0\}\), there is a deterministic \(N_0\) such that \(L_N\) is invertible almost surely at every \(N\ge N_0\).
   Consequently it is eventually invertible on one probability-one event under every allowed coupling, in particular when \(\Delta(L)>0\).
3. If at most two coefficient matrices among \(A_0,\ldots,A_r\) are nonzero, the full normalized logarithmic determinant limit in F0015 holds almost surely under every allowed coupling.
4. The same full limit holds under the following sparse support assumptions.
   Every \(A_j\), \(j\ge1\), has at most one nonzero scalar entry, their supported positions are distinct, and \(A_0\) vanishes at all these random positions.
   In the bipartite support graph, with one vertex per auxiliary row and column and one edge per nonzero block, every connected component contains at most one cycle.
   Components with unequal numbers of row and column vertices are allowed; in that case all finite ordinary determinants and the free ordinary determinant are zero.
5. The same full limit holds after a fixed simultaneous block upper-triangular change of basis of all coefficient matrices when each diagonal coefficient tuple satisfies assertion 3 or the balanced-component case of assertion 4.

Assertions 3--5 use the extended convention \(\log0=-\infty\) and resolve both full-limit and upper-limit equalities in both coupling regimes for their stated classes.
Assertion 2 provides no quantitative floor for positive singular values or logarithmic-tail estimate.
The explicit irreducible four-entry example in the proof has free logarithmic determinant \(\frac12\log\max\{|ad|,|bc|\}\), including the positive-determinant unbounded-inverse case \(|ad|=|bc|\).

## Inputs and inspection limits

The [CM14 source note](../audits/literature/CM14/readme.md) and [retained Haar comparison](../ledger/Yin_L_F0062_v1.md#haar-pencils) supply the accepted fixed-coefficient Haar *-moment convergence interface.
The [BHNY08 source note](../audits/literature/BHNY08/readme.md), Section 4, PDF pp. 15--17, supplies the fixed-point CUE logarithmic mean-zero and variance \(O(\log N)\) input.
The [DM17 source note](../audits/literature/DM17/readme.md), Definitions 2.1--2.2 and Proposition 2.3, journal p. 49, supplies square-blow-up rank divisibility.
The [affine rank argument](Yin_C_F0186_v2.md#generic-rank) is used only for its algebraic maximum-rank identification, independently of its Gaussian estimates.
The triangular extension uses [Luc22-U001](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant), Theorem 14.18, with its dense-range and injectivity hypotheses, and [FK52-U001](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) for bounded multiplicativity.
Those accepted classical inputs retain their recorded source-proof inspection depths.
Kenyon's source supplies attribution for the graph-connection viewpoint, rather than an input theorem for the present Haar limit.
The new application arguments and their exact interfaces are given below.

<a id="argument"></a>
## Complete candidate argument

<a id="coefficient-gauge"></a>
## Permuting the constant coefficient with a Haar coefficient

Fix an index \(k\) with \(1\le k\le r\).
For every \(N\) multiply \(L_N\) on the left by \(I_m\otimes(U_k^{(N)})^*\).
This changes neither singular values nor the absolute determinant and gives
\[
 A_k\otimes I_N+A_0\otimes V_0^{(N)}
 +\sum_{j\ne k} A_j\otimes V_j^{(N)},
 \qquad V_0^{(N)}=(U_k^{(N)})^*,\quad
 V_j^{(N)}=(U_k^{(N)})^*U_j^{(N)}.
\]
The variables V_0^{(N)} and V_j^{(N)}, j≠k, are independent Haar matrices.
Indeed, conditional on U_k^{(N)}, multiplication of the remaining independent Haar matrices by its fixed adjoint preserves their independent Haar laws, and that conditional law does not depend on U_k^{(N)}.
The map is dimensionwise, so it preserves independence across dimensions when that is imposed and sends every arbitrary coupling to another allowed coupling.

The corresponding free tuple \(v_0=u_k^*,\ v_j=u_k^*u_j\) is a free Haar tuple.
One way to verify exactly the needed assertion without a separate free-group result is to use the matrix-coefficient *-moment convergence already invoked in [the Haar starting comparison](../ledger/Yin_L_F0062_v1.md#haar-pencils).
The transformed finite tuples are independent Haar tuples at every N and also are fixed *-polynomials of the original tuples, so their limiting *-moments identify (v_0,(v_j)_{j≠k}) as a free Haar tuple.
Left multiplication of L by the unitary \(I_m\otimes u_k^*\) leaves \(L^*L\) exactly unchanged.
Consequently its ordinary FK determinant is unchanged.

Thus exchanging A_0 with any A_k preserves both the finite normalized logarithmic marginal laws and the free target.
Permuting the random coefficient indices is already allowed by the product Haar law.
The two operations generate all permutations of the r+1 coefficient positions.
No invertibility of a coefficient matrix is assumed.
This symmetry is an exact input reduction and supplies no lower logarithmic estimate for a pencil with three or more effective coefficient positions.

<a id="two-position"></a>
## Complete limit for at most two nonzero coefficient positions

Suppose at most two matrices among A_0,A_1,…,A_r are nonzero.
If there are zero or one nonzero positions, singularity or the determinant magnitude is deterministic and the asserted extended logarithmic limit follows directly.
For two nonzero positions, use the preceding coefficient permutation to put one position at the constant coefficient and the other at a single Haar coefficient.
It is therefore enough to treat
\[
 B_N=B_0\otimes I_N+B_1\otimes V_N,
 \qquad B=B_0\otimes1+B_1\otimes v,
\]
where B_0,B_1 are arbitrary fixed m×m matrices and V_N has Haar law on U(N) at every N.
Neither B_0 nor B_1 is required to be invertible.

Put f(z)=det(B_0+zB_1).
If f vanishes identically, unitary diagonalization of V_N makes B_N a direct sum of singular m×m matrices, so its determinant is zero at every N.
The direct integral representation of the single Haar unitary similarly gives positive kernel trace for B and hence ordinary FK determinant zero.
Thus the normalized logarithms are all minus infinity, including the free target.

If f is nonzero, the [retained single-Haar argument](../ledger/Yin_L_F0062_v1.md#single-haar) applies to this exact scalar polynomial.
For completeness its finite and free identities are
\[
 \frac1{mN}\log|\det B_N|
 =\frac1{mN}\sum_{\lambda\in\operatorname{spec}(V_N)}\log|f(\lambda)|,
 \qquad
 \log\Delta_{\operatorname{tr}_m\otimes\tau}(B)
 =\frac1m\int_{\mathbb T}\log|f(z)|\,dm(z).
\]
The finitely many scalar root factors off the circle have bounded continuous logarithmic tests on the circle.
For a circle root, [BHNY08's inspected fixed-point mean and variance input](../audits/literature/BHNY08/readme.md) gives a summable O(log N/N²) bound on every fixed positive normalized deviation.
The first Borel--Cantelli argument therefore proves the full almost-sure logarithmic limit under every cross-dimensional coupling.
It follows that both H-limit and H-limsup in both coupling regimes hold for this two-position coefficient class.
This is a direct Haar-invariance reduction to the previously retained single-Haar application, rather than a new characteristic-polynomial estimate.

A fixed simultaneous block upper-triangular decomposition with at most two coefficient positions in each diagonal block gives a further possible class.
The finite determinant factors over those blocks; the final section below supplies the free triangular interface needed for that extension.

<a id="haar-generic-rank"></a>
## Eventual almost-sure invertibility when the free kernel is zero

This deduction applies to the full coefficient tuple and removes exact singularity as a possible persistent obstruction.
It supplies no quantitative small-singular-value floor or logarithmic-tail bound.
Assume ker L={0}, which in particular follows when Δ(L)>0.
Let
\[
 r_N=\max_{X_1,\ldots,X_r\in M_N(\mathbb C)}
 \operatorname{rank}\left(A_0\otimes I_N+\sum_jA_j\otimes X_j\right).
\]
The [retained algebraic rank argument](../claims/Yin_C_F0186_v2.md#generic-rank) identifies r_N with the rank of the N-th tensor blow-up of span{A_0,…,A_r}.
The [inspected DM17 rank-regularity input](../audits/literature/DM17/readme.md) implies r_N∈Nℤ.
These are algebraic statements about the fixed coefficient space, independent of whether the random evaluations are Hermitian or Haar.

If r_N<mN for infinitely many N, then mN−r_N≥N for those N.
Every evaluation, including every Haar evaluation, then has empirical squared-singular-value mass at zero at least 1/m along that deterministic subsequence.
Haar *-moment convergence, together with the deterministic operator bound ||L_N||≤Σ_j||A_j||, gives weak convergence of these singular-value measures to the distribution of L*L in probability and hence weak convergence of the expected measures.
The Portmanteau inequality for the closed set {0} would force the limiting distribution to have mass at least 1/m at zero.
That contradicts ker L={0}.
It follows that r_N=mN for all sufficiently large N, so the affine determinant q_N(X_1,…,X_r) is then a nonzero complex polynomial.

A nonzero complex polynomial on M_N(ℂ)^r vanishes on a Haar tuple with probability zero.
Here is an elementary justification suited to this application.
The Cayley transform C(H)=(I+iH)(I−iH)^{-1} maps Hermitian matrices smoothly and bijectively onto the unitary matrices without eigenvalue −1.
That chart has a smooth nonsingular Jacobian for the real manifold dimensions N², so Haar measure in the chart has a density relative to Lebesgue measure on Hermitian coordinates.
The excluded eigenvalue event has Haar probability zero: after multiplication by an independent scalar phase e^{iθ}, any fixed unitary matrix has eigenvalue −1 for only finitely many θ, and scalar rotational invariance preserves Haar law.
After inserting C(H_j) in q_N and clearing powers of det(I−iH_j), one obtains a nonzero polynomial in Hermitian coordinates.
It is nonzero because the rational Cayley map has a rational inverse on a nonempty complex Zariski-open set.
A real basis of Hermitian matrices is also a complex basis of M_N(ℂ), so restriction to its real coordinate space cannot annihilate that nonzero polynomial identically.
Its zero set has Lebesgue measure zero by iterated one-variable polynomial root counting and Fubini.
This proves the Haar zero-probability assertion.

Thus L_N is invertible almost surely for every sufficiently large N.
Taking the countable intersection of these probability-one events proves eventual almost-sure invertibility under every allowed cross-size coupling.
In particular, positive free determinant cannot be accompanied by infinitely many dimensions at which the Haar pencil is identically singular, including an alternating-parity exact-singularity construction.
The remaining positive-determinant problem is quantitative control of small positive singular values.

<a id="graph-gauge"></a>
## Sparse coefficient graphs with at most one cycle per component

The next class can contain several nonzero coefficient matrices without a simultaneous triangular decomposition.
Assume that each random coefficient A_j, j≥1, has at most one nonzero scalar entry, that the supported positions of these nonzero A_j are distinct, and that A_0 vanishes at every random supported position.
Thus every nonzero block of the affine pencil is exactly \(c_eV_e\) with \(c_e\in\mathbb C\setminus\{0\}\) and \(V_e\) either one distinct input \(U_j\) or \(I_N\).
Different random edges use different Haar inputs; deterministic edges may all use I_N.
Form the simple bipartite support graph with row vertices \(\rho_1,\ldots,\rho_m\), column vertices \(\kappa_1,\ldots,\kappa_m\), and one edge for each nonzero block.
Assume every connected component of this graph has at most one cycle.
Then the full logarithmic almost-sure limit in Task F0015 holds under every allowed cross-dimensional coupling, and hence all four assertions hold for this class.

First suppose a connected component has equal numbers b of row and column vertices.
If it is a tree, choose that tree itself; if it has one cycle containing a random edge, delete one such edge e_* to obtain a spanning tree.
If its unique cycle has only deterministic edges, delete any cycle edge and choose a row vertex on that cycle as the root.
Choose unitary block row and column multipliers R_i and C_j along the tree so that
\[
 R_i V_e C_j=I_N
 \quad\text{on every tree edge }e=(\rho_i,\kappa_j).
\]
This is possible recursively from a root multiplier equal to I_N.
Given \(R_i\) set \(C_j=V_e^*R_i^*\), and given \(C_j\) set \(R_i=C_j^*V_e^*\).
The absence of a tree cycle makes the assignments consistent.
All multipliers are fixed words in tree-edge inputs and their adjoints.
Multiplication of the component matrix by the resulting block diagonal unitaries changes neither its singular values nor the absolute determinant.

For a tree, the transformed component is a deterministic scalar b×b matrix tensor I_N.
If a random edge e_* was deleted, the transformed component has the form
\[
 B_0\otimes I_N+B_1\otimes W_N,
 \qquad B_1=c_{e_*}E_{i_*j_*},\quad
 W_N=R_{i_*}U_{e_*}C_{j_*},
\]
with fixed scalar matrices B_0,B_1.
The two tree multipliers are measurable with respect to the other input matrices and are independent of U_{e_*}.
Conditioning on all tree inputs therefore makes W_N Haar, with a conditional law independent of those inputs.
Thus W_N is Haar at each dimension; no cross-dimensional independence is needed.
If the deleted edge and all other cycle edges are deterministic, the chosen root makes every multiplier on the cycle equal to I_N, so its deleted-edge multiplier is also I_N.
That case again gives a deterministic scalar matrix tensor I_N.

Apply the same unitary words to the free pencil.
Unitary multiplication on either side preserves its ordinary FK determinant because its squared modulus changes only by a unitary conjugation.
In the random-chord case the free word w=R_{i_*}u_{e_*}C_{j_*} is Haar.
Indeed the corresponding finite word W_N is Haar at every dimension, while asymptotic *-moment convergence of the original Haar tuple gives its free-word *-moments as the limits of those finite moments.
Therefore the transformed free component is exactly a single-Haar matrix pencil with the same B_0,B_1 as above.
The [two-position argument](#two-position) supplies the full logarithmic limit for that component, including the identically singular case.
For deterministic components the statement is immediate.

If all components are balanced, row and column permutations turn the original matrix into a direct sum of those square components.
For a component of auxiliary size b, its normalized logarithm has weight b/m in the full normalized logarithm.
The same weights hold for the free direct sum under the normalized trace.
There are only finitely many components, so intersection of their probability-one events and addition of their weighted limits proves the full conclusion.
If one target component determinant is zero, its logarithm is minus infinity, the other component logarithms are bounded above by their fixed norm bounds, and the full extended limit is again minus infinity.

If some component is not balanced, the entire square finite matrix is singular for every N by the rectangular component rank bound.
Were the free pencil injective, the [generic-rank argument](#haar-generic-rank) would give eventual almost-sure invertibility, contradicting that deterministic singularity.
Hence the free pencil has nonzero kernel and ordinary FK determinant zero.
Both finite and free logarithms are minus infinity, which completes this case as well.

For an explicit irreducible coefficient example, take m=2 and
\[
 L_N=\begin{pmatrix}aU_1&bU_2\\cU_3&dU_4\end{pmatrix},
 \qquad a,b,c,d\ne0.
\]
Left multiplication by \(\operatorname{diag}(U_1^*,U_3^*)\) and right multiplication by \(\operatorname{diag}(I_N,U_2^*U_1)\) give
\[
 \begin{pmatrix}aI_N&bI_N\\cI_N&dW_N\end{pmatrix},
 \qquad W_N=U_3^*U_4U_2^*U_1.
\]
The word W_N is Haar after conditioning on U_1,U_2,U_3.
Block elimination with the scalar nonzero a gives
\[
 |\det L_N|=|\det(adW_N-bcI_N)|.
\]
The free target and the normalized full limit are therefore
\[
 \log\Delta(L)=\frac12\log\max\{|ad|,|bc|\}.
\]
This includes the critical case |ad|=|bc|, where the free inverse is unbounded while the free determinant is positive.
Indeed bounded block elimination shows that invertibility is equivalent to invertibility of \(adw-bc\), and the Haar unitary \(w\) has spectrum \(\mathbb T\), so the critical equality puts zero in that Schur complement spectrum.
The four coefficient matrices are nonzero scalar multiples of E_11,E_12,E_21,E_22 and have no common nontrivial invariant auxiliary subspace.
Thus this example is not supplied merely by simultaneous triangularization of the coefficients.

### Source comparison for the tree transformation

On 2026-11-05 a bounded source search used the terms “Kenyon spanning tree gauge connection vector bundle graph trivialize spanning tree holonomy determinant”.
The inspected primary source, recorded under [Ken11](../audits/literature/Ken11/readme.md), was Richard Kenyon, [Spanning forests and the vector bundle Laplacian, arXiv:1001.4028v3](https://arxiv.org/pdf/1001.4028v3), Section 3.1, PDF pp. 4–5.
It defines graph connections, vertexwise gauge equivalence and cycle monodromy.
That is attribution for the familiar graph-gauge viewpoint, rather than an input theorem asserting the present Haar block-pencil conclusion.
The bipartite row/column recursion, conditional Haar statement and determinant application are given explicitly above.
No novelty or priority claim is made.
The search stopped once that source identified the existing mechanism; it did not establish a theorem for more than one independent cycle in a connected coefficient component.

<a id="triangular-extension"></a>
## Simultaneous triangular coefficient extensions

Suppose a fixed invertible coefficient-space change of basis makes all coefficient matrices block upper triangular.
Such similarity changes neither the finite determinant nor the free determinant, using [the retained bounded FK multiplicativity interface](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
Assume each diagonal block belongs to the two-position or balanced at-most-one-cycle class already treated.
If every diagonal block has positive free determinant, the diagonal blocks are injective and have dense range in the finite tracial algebra.
The triangular whole matrix is injective by solving the block equations successively from the last row.
Choose the canonical free-group realization of the free Haar tuple; it has the same *-distribution and hence the same squared-singular-value distributions and FK determinants as the original realization.
The triangular determinant formula in [Luc22, Theorem 14.18, as retained in U001](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant) applies to the resulting Hilbert-module maps because the first diagonal map has dense range and the second is injective.
All maps here are injective, so the source's kernel-removed determinant equals the ordinary determinant.
Iterating the two-block identity gives
\[
 m\log\Delta(L)=\sum_\alpha b_\alpha\log\Delta(L_{\alpha\alpha}),
\]
where b_α are the diagonal block sizes and the determinants on the right use their own normalized auxiliary traces.
The finite determinant has exactly the same block product and weights, so the full almost-sure limits already proved for those finitely many diagonal blocks give the whole limit.

For these particular diagonal classes, a zero free determinant occurs precisely when the transformed scalar single-Haar determinant polynomial vanishes identically or when a deterministic transformed block is singular.
In that case the corresponding finite diagonal block is singular at every N, so the full finite pencil is singular at every N.
The [generic-rank contrapositive](#haar-generic-rank) again forces a nonzero free kernel for the whole pencil and hence zero ordinary free determinant.
The full extended logarithmic limit is then minus infinity.
This supplies the formerly isolated triangular interface, without an assumption that the free inverses of the diagonal blocks are bounded.


## Current assessment

[Selected decision](#decision-haar-structural-reviewed)

## Assessment history

### Decision haar-structural-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:28 |
| status | open |
| reason | The structural reductions, restricted full limits and eventual-invertibility deduction are fixed as a candidate for mathematical review; no unrestricted Haar Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Coefficient-position symmetry, eventual invertibility under zero free kernel, two-position and sparse-cycle full limits, and their stated triangular extensions. |
| argument | [Complete candidate argument](#argument) | Haar invariance, single-Haar estimates, blow-up rank, Cayley coordinates, sparse tree gauges and the exact triangular determinant interface. |

### Decision haar-structural-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:38 |
| status | proved |
| reason | Independent review checked all five exact restricted assertions, their complete argument and the stated primary-source interfaces without an unresolved gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Restricted Haar structure and limits](#statement) | Coefficient-position symmetry, eventual invertibility under zero free kernel, and full limits for two-position, sparse-cycle and stated triangular classes. |
| argument | [Complete structural proof](#argument) | Exact Haar transformations, scalar root estimates, rank and zero-set argument, tree reductions and weighted triangular identity. |
| dependency | [Haar moment interface](../ledger/Yin_L_F0062_v1.md#haar-pencils) | Only the inspected fixed-coefficient Haar moment convergence and its continuous-test consequence. |
| dependency | [Single-Haar logarithmic input](../ledger/Yin_L_F0062_v1.md#single-haar) | Scalar determinant reduction and summable fixed-point CUE logarithmic estimate under arbitrary cross-size couplings. |
| dependency | [Algebraic maximum rank](Yin_C_F0186_v2.md#generic-rank) | Only the accepted homogeneous-to-affine maximum-rank identification and blow-up divisibility, with no Gaussian logarithmic estimate. |
| dependency | [Triangular determinant interface](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only Theorem 14.18 and the determinant convention, with the displayed injectivity, dense-range and trace normalizations. |
| dependency | [Bounded FK products](../audits/literature/FK52/Yin_U001.md#fk52-u001) | Only bounded ordinary multiplicativity and its finite-tracial adaptation, used for the fixed similarity. |
| review | [Independent restricted proof finding](../audits/reviews/Yin_R_F0197_v1.md#independent-haar-structural-proof) | Whole exact restricted statement and argument, all five assertions and source applicability; no unrestricted Task-completion conclusion. |
