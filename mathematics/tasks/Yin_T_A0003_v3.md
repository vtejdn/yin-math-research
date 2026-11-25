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
