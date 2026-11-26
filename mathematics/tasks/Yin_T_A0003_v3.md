---
author: Yin
---

# Simplifying the finite-rank rationality criterion for torsion-free groups

## Contract

Let \(G=\langle g_1,\ldots,g_d\rangle\) range over finitely generated torsion-free discrete groups.
Put \(M=\mathcal N(G)\), \(H=\ell^2(G)\), \(U=L^0(M)\), and let \(D_G\) be the division closure of \(\mathbb CG\) in \(U\).
Seek a simpler finite-rank criterion for \(u\in D_G\), for every \(u\in U\), under torsion-freeness alone.
In particular, determine whether the local commutation condition in the [completed criterion](../claims/Yin_C_A0131_v3.md#statement) can be dropped altogether.

For \(X_j=\lambda(g_j)\), let \(\rho_j\) be right multiplication by \(X_j\), and let \(P_e\) be the projection onto \(\mathbb C\delta_e\).
The question about deletion is whether \(u\in D_G\) is equivalent to the existence of \(s,a,b,t\in M\) and finite-rank \(T_1,\ldots,T_d\in B(H)\) satisfying
\[
 s,t\in U^\times,\qquad u=s^{-1}a=bt^{-1},\qquad
 \sum_j[\rho_j,T_j]=sP_e b-aP_e t. \tag{1}
\]
All witnesses are chosen for the same \(u\), which may be unbounded.
A positive answer proves the equivalence uniformly.
A negative answer gives a torsion-free group and an affiliated element satisfying (1) outside \(D_G\).
A simpler replacement remains of interest in either investigation.
State which witnesses, tests or quantifiers it eliminates, prove both directions at its actual scope, and distinguish its contribution from a decision on complete deletion.
A special class of groups or a sufficient extra hypothesis gives partial progress on the universal question.

## Starting results

The [earlier completion](Yin_T_A0003_v2.md#decision-finite-rank-characterization) establishes the criterion with a finite-dimensional subspace and a test over finite-rank operators, even for groups with torsion.
For the unrestricted equation, [the group-algebra criterion](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected) reduces the question exactly to whether \(p_{\ker x}\in D_G\) for every \(x\in D_G\).
A group satisfying the complex strong Atiyah conjecture has an affirmative answer in the torsion-free case.
The present target allows zero divisors in \(D_G\).

## Progress on simplification and deletion

The fraction and its finite-rank solution determine the space \(V_0=\mathbb C s\delta_e+\sum_j\operatorname{Ran}T_j\).
One Hilbert space injectivity test for the matrix of relations among a basis of \(V_0\) and its first translates replaces the choice of an auxiliary space and the universal quantifier over test operators. [Proved criterion](../claims/Yin_C_A0131_v4.md#statement)

Complete deletion passes in both directions across finite-index subgroups, in particular giving a positive answer for torsion-free virtually locally indicable groups. [Finite-index transfer](../ledger/Yin_L_A0073_v1.md#scope-of-the-transfer)
For a fixed group the remaining question is equivalent to membership in \(D_G\) of the last diagonal kernel-projection coefficient of every affine bordered pencil with injective leading block and constant border. [Exact reduction](../ledger/Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil)
Even on \(\mathbb Z^2\), two tuples for the same fractions can differ on the local test. [Example](../ledger/Yin_L_A0074_v1.md#a-solution-with-a-nonrational-range-on-the-two-torus)
The uniform deletion question for all finitely generated torsion-free groups remains open here.

For direct products with \(\mathbb Z^d\), a single fiber of maximal rank determines rationality of an entire group-ring kernel projection.
In particular complete deletion holds for \(H\times V\) exactly when it holds for \(H\), for every finitely generated virtually abelian \(V\). [Fiber criterion and transfer](../claims/Yin_C_A0132_v1.md#statement)
For finitely generated amenable \(G\), the outstanding condition is equivalent to finite generation of the scalar right annihilators in \(D_G\). [Annihilator criterion](../claims/Yin_C_A0133_v1.md#statement)
A right coherent group algebra suffices in that class. [Finitely supported kernel generators](../ledger/Yin_L_A0076_v1.md#amenable-groups-with-a-right-coherent-complex-group-algebra)
For any finitely generated group the existence of all rational kernel projections is equivalent to flatness of \(U_G\) as a left \(D_G\)-module.
For a given \(x\), the obstruction is the quotient \(p_{\ker x}U_G/\operatorname{ann}_{D_G}(x)U_G\). [Principal right ideals](../ledger/Yin_L_A0077_v1.md#the-obstruction-for-one-principal-right-ideal)
If \(G\) has a coamenable subgroup with regular division closure, each rational kernel dimension is the supremum of ranks of bounded positive rational annihilators.
For each \(x\in D_G\), attainment of this supremum is equivalent to \(p_{\ker x}\in D_G\). [Finite coset estimates](../claims/Yin_C_A0134_v1.md#statement)
The full deletion question is the finitely generated torsion-free complex case of [Linnell's Problem 4.4](../audits/literature/Lin06/Yin_U001.md#regularity-of-the-rational-closure).

Membership in \(D_G\) now has a criterion with just one finite-dimensional space \(V\subset U\) containing \(1,u\).
A linear map on the first translates of \(V\) that kills \(1\) and respects the marked right translations must kill every vector in \(V\).
Requiring vanishing only at \(u\) instead characterizes solvability of (1).
Restricting \(V\) to \(\mathbb CG+u\mathbb CG\) gives exactly the single group-ring right fractions. [Finite-dimensional criteria](../claims/Yin_C_A0137_v1.md#statement)
Allowing at most \(k\) auxiliary vectors besides \(1,u\), across all finite markings, makes promotion of single-vector vanishing to rationality equivalent to rationality of the kernel projections of group-ring matrices with \(k\) input columns. [Matrix-size equivalence](../claims/Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors)
In the finite-rank formulation every pair of denominators can be replaced by one positive contraction while preserving all witness ranks and the local matrix test. [Positive denominator](../claims/Yin_C_A0135_v1.md#statement)
In a cyclic extension the increase in kernel dimension from one height interval to the next equals the global rank captured by translates of that interval's solutions.
Universal finite stabilization over torsion-free groups, even restricted to full-row-rank matrices whose kernel projections are already rational, is equivalent to the complex strong Atiyah conjecture. [Interval ranks](../claims/Yin_C_A0136_v1.md#statement)

There is now a one-parameter formulation entirely over the original group.
In the scalar division closure of \(\mathbb CG[z]\) inside \(U((z))\), the constant terms of the power series are precisely the solutions of (1), and the constant series are precisely the elements of \(D_G\).
Thus the remaining question is whether taking the constant term as a constant series preserves this scalar division closure for every finitely generated torsion-free \(G\). [Formal constant terms](../claims/Yin_C_A0141_v1.md#statement)
For group-ring matrices one can also encode every input width by positive scalars using the same two-generator lamplighter group as an auxiliary direct factor. [Exact transfer to scalar kernels](../claims/Yin_C_A0138_v1.md#statement)
On the original group a finite set of relations detecting the closed range of a block of columns eliminates those columns and leaves a smaller group-ring kernel test.
For the presentation gradient this reduction is possible precisely at vanishing first \(L^2\)-Betti number. [Elimination of columns](../claims/Yin_C_A0139_v1.md#statement)
Tracial representations with all prescribed finitely many regular moments and injective nonzero scalars can still fail the two-column test. [Marked tracial example](../claims/Yin_C_A0140_v1.md#statement)

In a free product, regularity of both vertex division closures now suffices for complete deletion.
The same recovery of the zero atom works over a finite edge, or over a semisimple Artinian edge division closure when the edge group acts freely on a coamenable coset space of the amalgam. [Free convolution and the kernel projection](../claims/Yin_C_A0142_v1.md#statement)
Every formal rational expression from the one-parameter test can be evaluated outside a countable exceptional set, and its formal coefficients give all orders of its asymptotic expansion in measure.
For a group-ring matrix \(X\), the resolvent at the central shift \(Z\) belongs to the image of this formal ring precisely when the kernels of the powers of \(X\) stabilize.
Even on \(\mathbb Z\), agreement of every asymptotic coefficient can coexist with divergence of the series at each sufficiently small positive argument. [Analytic specialization](../claims/Yin_C_A0143_v1.md#statement)
For a sofic group, rationality of any given matrix kernel projection is equivalent to two normalized ranks in finite models tending to the same prescribed integer for one fixed polynomial witness. [Finite-model test](../claims/Yin_C_A0144_v1.md#statement)

For a fixed group in the contract, deleting the local condition is equivalent to lifting each scalar kernel projection to an exact idempotent in the ring of rational power series in \(z\).
A single rational inverse recovers the projection from any such lift. [Idempotent lifting](../claims/Yin_C_A0147_v1.md#statement)
Finite-order lifts always exist.
They imply exact lifting when their group support, realization size and polynomial degree stay bounded as the order grows, even with varying complex coefficients and inverse pole orders. [Finite determination](../claims/Yin_C_A0149_v1.md#statement)
Whether those bounds exist for each rational input in every finitely generated torsion-free group remains open.
At fixed finite group support and matrix size the polynomial degree may grow sublinearly with the jet order \(N\).
This is still an exact criterion for membership in \(D_G\), while every regular-closure residue admits a realization of degree at most \(N\). [Sublinear degree criterion](../claims/Yin_C_A0151_v1.md#statement)
Allowing the group support to vary gives a quantitative rank approximation whenever size times degree grows sublinearly.
For a full constant jet the error at each admissible scalar parameter is at most \(nd/N\), where \(n\) is the realization size and \(d\) its degree. [Specialization estimates](../claims/Yin_C_A0155_v1.md#statement)
An example over the infinite cyclic group has a rational matrix kernel projection which no rational function of the positive matrix alone can recover.
The joint law with one additional commuting group-ring observable separates the kernel from the positive part. [Spectral separation](../claims/Yin_C_A0154_v1.md#statement)
Requiring every rational element after adjoining a central group generator to arise from a formal Laurent series would imply the complex strong Atiyah conjecture across these groups. [Evaluation and stable kernels](../claims/Yin_C_A0146_v1.md#statement)

The unrestricted equation also suffices for graph groups with regular vertex division closures and finite edges, or under the specified amenable-action and edge-ring hypotheses. [Graph theorem](../claims/Yin_C_A0145_v1.md#statement)
For virtually locally indicable groups and cyclic edges one can recover the expected support of a rational projection from finitely many copies. [Cyclic support theorem](../claims/Yin_C_A0148_v1.md#statement)
A variational formula gives the exact trace still missing after any prescribed number of free copies over an edge algebra. [Free copies](../claims/Yin_C_A0150_v1.md#statement)
Two affiliated vertex commutators of full row rank suffice to recover kernels of additive rational matrices even on a torsion-free cyclic amalgam without an amenable action free on the edge. [Vertex commutators](../claims/Yin_C_A0152_v1.md#statement)

On any one finite marking, complete deletion is equivalent to separation of the ranges of each rank-one commutator sum and its adjoint by right multiplication by a projection of \(D_G\).
Excluding rank-one sums altogether is equivalent, for torsion-free \(G\), to the complex strong Atiyah conjecture. [Rank-one separation](../claims/Yin_C_A0157_v1.md#separating-the-ranges-and-excluding-rank-one)
In an amenable marked limit, two limiting ranks from witnesses of fixed word support and size detect rationality of a kernel projection, even when their complex coefficients vary. [Finite-window test](../claims/Yin_C_A0156_v1.md#statement)
For a torsion-free amenable group, a scalar kernel projection witnessing failure would lie outside the von Neumann algebra of every abelian subgroup and would have the same normalized trace on every nonzero central cut. [Subgroup and center restrictions](../claims/Yin_C_A0158_v1.md#statement)
For a fixed sofic group the full complex question is equivalent to the existence of rational inner inverses for integer group-ring matrices after adjoining finitely many central generators. [Countable coefficient test](../claims/Yin_C_A0159_v1.md#statement)

For \(B=X^*X\), the Christoffel minima computed from its scalar moments bound the normalized trace of the constant term of \(z(z+B)^{-1}\) from above.
Rational matrices \(Y\) with \(XY=0\) give lower bounds from their range ranks.
The kernel projection is rational exactly when the gap tends to zero for witnesses of fixed group support and realization size.
At one fixed two-by-two input over \(\mathbb Z\), every finite list of moments agrees exactly with an invertible input even though the fixed kernel has normalized trace \(1/2\). [Spectral moment criterion](../claims/Yin_C_A0160_v1.md#statement)

For a single row \([s,-a]\) with \(s\) an affiliated unit in the group ring, its rational kernel has a finite set of group-ring columns spanning it after closure exactly when \(s^{-1}a\) has a single right denominator in the group ring.
Requiring finite group-ring exhaustion of every rational kernel throughout the torsion-free amenable class is equivalent to the complex strong Atiyah conjecture throughout that class. [Ore denominators and the wreath-product test](../claims/Yin_C_A0161_v1.md#statement)
Even in one two-generated torsion-free amenable group, some one-dimensional kernels admit a fixed-size rational expression while the smallest nonzero group-ring solution needs arbitrarily many sites. [Sparse solutions and the exact moment gap](../claims/Yin_C_A0163_v1.md#statement)

If maximal rank is attained at rational parameters for every group-ring polynomial matrix over a sofic group, the rational-coefficient test for complete deletion needs no extra central generators. [Coefficient specialization](../claims/Yin_C_A0162_v1.md#statement)
Even asking for one algebraic maximal-rank parameter for each integral affine pencil throughout the torsion-free amenable class is equivalent to the complex strong Atiyah conjecture throughout that class. [Algebraic rank attainment](../claims/Yin_C_A0164_v1.md#statement)

For a symmetric marking, the ranges of one solution of (1) determine a finite complex matrix rank comparison equivalent to \(u\in D_G\).
Its entries use the linear relations of those ranges and their first translates.
One can impose a common positive denominator. [Witness range criterion](../claims/Yin_C_A0171_v1.md#statement)
A second criterion uses mixed trace moments of any bounded right fraction for \(u\).
On rectangular group-ring inputs the same ordered limits test rationality of the kernel projection using only identity coefficients of finite products. [Mixed trace moments](../claims/Yin_C_A0172_v1.md#statement)

Let \(P_u\) be the graph projection and lift \(2P_u-I\) as the constant coefficient of a matrix of rational power series over the group algebra.
Then \(u\in D_G\) precisely when some lift is contractive along a single logarithmic spiral approaching zero.
With the argument sampled uniformly on each small circle, a limiting upper probability strictly greater than \(1/2\) gives the same criterion.
Allowing exactly \(1/2\) characterizes solvability of (1), as does testing any fixed finite list of rays. [Spiral and half-probability criteria](../claims/Yin_C_A0174_v1.md#statement)

For the binary lamplighter group \(C_2\wr\mathbb Z\), the kernel projection of an explicit positive integral scalar satisfies (1) and lies outside \(D_G\).
Thus the inclusive and strict probability tests differ on a specified input with torsion.
On the repeated word \(1^n0^m\), one diagonal projection entry is nonzero exactly when \(n=m\), which is incompatible with a rational realization. [Two-run proof](../claims/Yin_C_A0173_v1.md#argument)
For a group containing \(\mathbb Z\wr\mathbb Z\), no unital map to finite matrices over a commutative field can evaluate its full division closure, although growing generic periods preserve the rank of each fixed rational expression for \(\mathbb Z\wr\mathbb Z\) itself. [Sharp finite-dimensional bounds](../claims/Yin_C_A0175_v1.md#statement)
Adding an independent Haar lamp makes one fixed full matrix singular on every decorated one-marker period.
In the torsion-free construction this uses the additional hypothesis of a nontrivial rational projection in the lamp group. [Endpoint collision formula](../claims/Yin_C_A0176_v1.md#statement)
For the binary lamplighter, one positive rational contraction has an eigenvalue at every rational number in \([0,1]\).
Its endpoint spectral projections belong to the division closure, and each interior atom gives a projection satisfying (1) outside that closure. [Exact spectral law](../claims/Yin_C_A0177_v1.md#statement)
For any affiliated spectral function of this contraction, equation (1) permits finitely many exceptions to agreement with a single complex rational function on the interior rational eigenvalues.
Membership in the division closure requires agreement at every one of them.
The endpoint values are arbitrary in both criteria. [Spectral function classification](../claims/Yin_C_A0178_v1.md#statement)
Whether (1) guarantees the strict inequality for every torsion-free group remains open.

## Current decision

[Reopened research](#decision-reopened)

## Lifecycle and completion

### Decision reopened

| Field | Value |
| --- | --- |
| date | 2026-11-25T08:13 |
| status | active |
| authority | Yin requested reopening A0003 to simplify the criterion for torsion-free groups, with particular attention to eliminating the local condition. |
| reason | The completed criterion imposes local commutation on a finite-dimensional subspace. The revised objective asks how far this requirement can be simplified under torsion-freeness and whether (1) alone suffices. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Simplification for torsion-free groups](#contract) | Simpler finite-rank criteria and the universal question of complete deletion for all affiliated elements. |
| support | [Criterion with the local condition](../claims/Yin_C_A0131_v3.md#statement) | Starting equivalence and explicit local test. |
| support | [Unrestricted equation](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected) | Exact kernel-projection condition for complete deletion. |
