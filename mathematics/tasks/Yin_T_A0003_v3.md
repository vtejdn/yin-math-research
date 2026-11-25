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
