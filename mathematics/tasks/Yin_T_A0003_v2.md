---
author: Yin
---

# A finite-rank commutator criterion for the division closure of a group algebra

## Contract

Let \(G=\langle g_1,\ldots,g_d\rangle\) be a finitely generated discrete group, let \(M=\mathcal N(G)\) act on \(H=\ell^2(G)\), and put \(U=L^0(M)\).
Write \(D_G=\operatorname{Div}_{U}(\mathbb CG)\) for the closure of the group algebra under ring operations and inverses of elements invertible in \(U\).
Establish a criterion of the finite-rank commutator type of F0001 for \(u\in D_G\), for every \(u\in U\) and every finitely generated torsion-free \(G\).
A result covering every finitely generated group gives the same criterion in greater generality.
Finite generation and, if needed, torsion-freeness are the full group hypotheses.

In the reference equation \(\rho_j\) denotes right multiplication by \(\lambda(g_j)\) and \(P_e\) projects onto \(\mathbb C\delta_e\).
For some \(s,a,b,t\in M\) with \(s,t\) invertible in \(U\) and \(u=s^{-1}a=bt^{-1}\), one seeks operators \(T_j\) of finite complex rank satisfying
\[
             \sum_{j=1}^d [\rho_j,T_j]=sP_e b-aP_e t. \tag{1}
\]
The desired characterization may adapt this equation or specify which finite-rank witnesses are admissible.
State the criterion in terms of the regular representation and its operators, with explicit quantifiers and conditions on the witnesses that can be formulated independently of the membership being tested.
Prove both necessity and sufficiency for affiliated \(u\), including unbounded elements and all finite rational inverse depths.
The argument must apply without assuming that \(D_G\) is a division ring or imposing the strong Atiyah conjecture.

## Existing results

One criterion retains (1) and asks for a finite-dimensional subspace \(V\) containing \(s\delta_e\) and all witness ranges.
Every finite-rank operator that vanishes on \(s\delta_e\) and commutes with the right translations on \(V\) must vanish throughout \(V\).
These two conditions characterize \(D_G\) for every finitely generated group. [Statement and proof](../claims/Yin_C_A0131_v3.md#statement)

An alternative specifies the witness ranges by a row of Hilbert space vectors satisfying an injective group-algebra pencil equation. [Pencil and range criterion](../claims/Yin_C_A0131_v2.md#statement)

For the particular choice of (1) with unrestricted finite-rank witnesses, the [exact condition](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected) is that \(p_{\ker x}\in D_G\) for every \(x\in D_G\).
This identifies the [earlier kernel-projection question](Yin_T_A0003_v1.md#contract) as the specialization that asks for (1) verbatim.

## Current decision
[Selected decision](#decision-finite-rank-characterization)

## Lifecycle and completion

### Decision revised-objective

| Field | Value |
| --- | --- |
| date | 2026-11-25T07:24 |
| status | proposed |
| authority | Yin specified the objective of A0003 and its maximal group hypothesis. |
| reason | The target is a finite-rank commutator characterization of division-closure membership, allowing variants of the reference equation over the full stated class of groups. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Finite-rank criterion](#contract) | A finite-rank commutator criterion for every affiliated element of every finitely generated torsion-free group, allowing coverage of all finitely generated groups. |
| support | [Finite-rank commutation on a subspace](../claims/Yin_C_A0131_v3.md#decision-local-commutation) | The fraction equation and a local commutation test using only finite-rank operators as test maps on the regular Hilbert space. |
| support | [Criterion with a range condition](../claims/Yin_C_A0131_v2.md#decision-division-closure-criterion) | An established variant valid for every finitely generated group in its regular representation. |

### Decision finite-rank-characterization

| Field | Value |
| --- | --- |
| date | 2026-11-25T07:45 |
| status | completed |
| authority | Yin requested a completion determination for the revised finite-rank objective. |
| reason | The fraction equation together with the local commutation condition is necessary and sufficient for division-closure membership of every affiliated element of every finitely generated group. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [A0003 objective](#contract) | A finite-rank commutator criterion in the regular representation under at most torsion-freeness. |
| support | [Finite-rank characterization](../claims/Yin_C_A0131_v3.md#statement) | Both directions for every affiliated element, including unbounded elements, using the same fraction pair, witnesses and finite-dimensional subspace. |
| dependency | [Affine realizations and scalar pivots](../claims/Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Realization at all finite inverse depths and inversion of injective positive group-algebra matrices by scalar division closure. |
| dependency | [Fraction and finite-rank witnesses](../claims/Yin_C_A0131_v2.md#constructing-the-finite-rank-operators) | Common bounded denominators, an affine row and solutions of the fraction equation with the specified ranges. |
| review | [Independent completion review](../audits/reviews/Yin_R_A0165_v4.md#completion-of-a0003) | Full proof of the characterization, its required inputs and coverage of the revised contract. |
