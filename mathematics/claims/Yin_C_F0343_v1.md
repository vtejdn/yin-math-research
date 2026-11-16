---
author: Yin
---

# Finite matrix algebras cannot realize a nontrivial trace-half lattice liberation

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(D=\operatorname{span}\{e_1,\ldots,e_m\}\) for a finite partition of unity into nonzero projections, \(P\) a projection and \(N=W^*(D,P)\) a finite-dimensional algebra with faithful tracial probability.
If \(\tau(P)=1/2\), the represented outer derivation
\[
           \gamma(e_i)=e_i\otimes1-1\otimes e_i,\qquad \gamma P=0
\]
into the coarse correspondence exists exactly when \(D=\mathbb C1\).
The relative trace-half [lattice problem](Yin_C_F0339_v1.md#statement) therefore has no nontrivial model in any finite direct sum of full matrix algebras, even before imposing the vacuum bound.
This assertion concerns finite-dimensional \(N\); finite-dimensionality of \(D\) alone is part of the original unrestricted lattice setting.

More generally, without the trace-half condition, write \(N=\bigoplus_\alpha M_{d_\alpha}(\mathbb C)\) and put \(r_{i\alpha}=\operatorname{rank}(e_i|_\alpha)\), \(q_\alpha=\operatorname{rank}(P|_\alpha)\).
The displayed derivation exists if and only if for every ordered pair of summands,
\[
 \sum_i r_{i\alpha}r_{i\beta}
       =q_\alpha(d_\beta-q_\beta)+(d_\alpha-q_\alpha)q_\beta+
                       {\bf1}_{\{\alpha=\beta\}} .                        \tag{1}
\]
If it exists its vacuum is automatic, and every \(d_\alpha\) is odd.

## Argument

### Two spaces of intertwiners

The represented word algebra is all of \(N\) by finite dimension.
Every outer derivation \(\gamma\) on this algebra into its coarse correspondence has the form \(\gamma x=x\cdot K-K\cdot x\).
Indeed put \(K=\int u^*\cdot\gamma(u)\,du\) over the compact unitary group of \(N\) with Haar probability.
Linearity on a finite-dimensional space gives continuity.
Replacing \(u\) by \(uv\) for each fixed unitary \(v\) and using the product rule gives \(K=v^*\cdot\gamma(v)+v^*\cdot K\cdot v\).
The asserted formula follows on unitaries and therefore on their linear span, which is \(N\).

Identify the coarse space linearly with \(\mathcal L=N\otimes N^{\rm op}\) by \(b\otimes c\mapsto b\otimes c^{\rm op}\), with its product trace Hilbert norm.
The outer bimodule relations \(x\cdot K=K\cdot x\) become equality of the left multiplications of \(K\) by \(x\otimes1\) and \(1\otimes x^{\rm op}\).
For the entire marginal \(D\) the space of such intertwiners is \(p_D\mathcal L\), and for \(P\) it is \(p_P\mathcal L\), where
\[
 p_D=\sum_i e_i\otimes e_i^{\rm op},\qquad
 p_P=P\otimes P^{\rm op}+(1-P)\otimes(1-P)^{\rm op}.
\]
For example the left support of any vector intertwining the partition has zero product components with unequal labels, and the converse is immediate.
The required generator values are equivalent to \(1-K\in p_D\mathcal L,\ K\in p_P\mathcal L\).
The two spaces on the right are right ideals.
Their sum contains the unit exactly when \(p_D\vee p_P=1\), using finite dimension to identify the sum with \((p_D\vee p_P)\mathcal L\).
Conversely decomposing the unit in that sum constructs \(K\) and the desired derivation on all of \(N\).
Finite dimension puts every coarse vector in the domain of the Hilbert adjoint.

On the simple spatial component \((\alpha,\beta)\), the two projections act on \(\operatorname{Hom}(\mathbb C^{d_\beta},\mathbb C^{d_\alpha})\) by retaining equal labels or equal \(P\)-eigenvalues, respectively.
Their ranks are \(\sum_i r_{i\alpha}r_{i\beta}\) and \(q_\alpha q_\beta+(d_\alpha-q_\alpha)(d_\beta-q_\beta)\).
The intersection consists of simultaneous intertwiners for all the \(e_i,P\), hence for the two representations of \(N\), since these elements generate \(N\).
Its dimension is one at \(\alpha=\beta\) by the scalar commutant of the full matrix algebra and zero otherwise by the distinct central units.
The dimension formula for the sum of two vector subspaces makes \(p_D\vee p_P=1\) equivalent to (1) on every block.
On a diagonal pair, (1) gives \(\sum_i r_{i\alpha}^2=2q_\alpha(d_\alpha-q_\alpha)+1\).
The left side is congruent modulo two to \(\sum_i r_{i\alpha}=d_\alpha\), proving oddness.

### Opposite scalar summands at trace one half

Let \(w_\alpha>0\) be the central trace weights summing to one.
Multiply (1) by \(w_\alpha w_\beta/(d_\alpha d_\beta)\) and sum.
With \(t_i=\tau(e_i)\), this gives
\[
          \sum_i t_i^2=2\tau(P)(1-\tau(P))+\sum_\alpha w_\alpha^2/d_\alpha^2 .
\]
At trace one half this exceeds \(1/2\).
Since \(\sum_i t_i=1\), there is a label \(i_0\) with \(t_{i_0}>1/2\).
The two meets \(e_{i_0}\wedge P\) and \(e_{i_0}\wedge(1-P)\) both have positive trace by the projection dimension inequality.
Each is a central projection of \(N\) because it commutes with \(P\) and every \(e_i\).
On each such projection all generators are scalar, so it is the unit of a one-dimensional summand.
These are distinct summands with the same label and opposite \(P\)-values.

Let \(\beta\) be any further simple summand.
Applying (1) to its pairs with these two characters requires both \(r_{i_0\beta}=d_\beta-q_\beta\) and \(r_{i_0\beta}=q_\beta\).
This forces \(d_\beta\) even, contradicting the diagonal parity condition.
Thus only the two characters remain and \(e_{i_0}=1\).
If \(D=\mathbb C1\), the zero derivation realizes all the prescriptions on the algebra generated by \(P\).
This proves the trace-half classification.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:24 |
| status | open |
| reason | Fix the finite-dimensional intertwiner criterion and its trace-half obstruction for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact dimension criterion, odd simple summands and exclusion of every nontrivial finite-dimensional trace-half lattice realization. |
| argument | [Argument](#argument) | Innerness by Haar averaging, two right ideals and their blockwise ranks, and opposite scalar summands forced by the global trace condition. |
| dependency | [Lattice model](Yin_C_F0339_v1.md#statement) | Exact generator prescriptions and trace convention to which the finite-dimensional exclusion applies. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:28 |
| status | proved |
| reason | R_F0346 checked both directions of the finite-dimensional rank test on every matrix block, including the parity, central characters and exact trace-half exclusion, and the declared lattice interface. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact dimension criterion, odd simple summands and exclusion of every nontrivial finite-dimensional trace-half lattice realization. |
| argument | [Argument](#argument) | Innerness by Haar averaging, two right ideals and their blockwise ranks, and opposite scalar summands forced by the global trace condition. |
| dependency | [Lattice model](Yin_C_F0339_v1.md#statement) | Exact generator prescriptions and trace convention to which the finite-dimensional exclusion applies. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0346_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
