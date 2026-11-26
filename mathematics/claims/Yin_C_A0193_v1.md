---
author: Yin
---

# Finite-rank witnesses over a subgroup division ring

## Statement

Let \(S\) mark a finitely generated group \(G\), let \(H=\langle S_0\rangle\) for \(S_0\subset S\), and assume its division closure \(B=D_H\) in the affiliated operators is a division ring.
Write \(U=U_G\) and use the [finite-rank commutator equation](Yin_C_A0131_v1.md#statement) for \(u\in U\).
Allow arbitrary finite witness ranks on \(S_0\).
For a fixed \(g\in S\setminus S_0\), allow rank at most one on \(g\) and require all remaining witnesses to vanish.
These rank restrictions are equivalent to each of the following descriptions separately:
\[
 u=d^{-1}n,\quad d,n\in B+gB,\ d\in U^\times ,
 \qquad\qquad
 u=n'd'^{-1},\quad d',n'\in B+Bg,\ d'\in U^\times .
\]
With all witnesses outside \(S_0\) zero the elements obtained are precisely \(B\).

Suppose instead that the total witness rank outside \(S_0\) is at most two.
For each occupied label \(g\notin H\), assume every nonzero element of \(B+gB\) and of \(B+Bg\) is an affiliated unit.
Then \(u\in D_G\).
The binomial hypothesis holds, in particular, if \(D_{\langle H,g\rangle}\) is a division ring or if \(\langle H,g\rangle\) has an integer character vanishing on \(H\) and nonzero at \(g\).
The character may be chosen separately for each label.

In a torsion-free \(G\), take \(S_0=\{h\}\) with \(h\ne1\).
Then \(B=\mathbb C(h)\), so a witness of any finite rank at \(h\) and rank at most one in total elsewhere guarantees a lift with contraction probability one on every sufficiently small circle. [Angular criterion](Yin_C_A0174_v1.md#statement)

## Argument

### One rank outside the subgroup

The complex tensor identity for the equation is
\[
 \delta u=\sum_i\Psi_{g_i}(l_i\otimes r_i),\qquad
 \delta u=u\otimes1-1\otimes u,\qquad
 \Psi_g(l\otimes r)=lg\otimes r-l\otimes gr ,
\]
where \(l_i,r_i\in U\) and at most the prescribed operator rank many summands are used at each label.
Conversely, clearing the two common outer denominators gives finite-rank witnesses within the indicated ranks. [Tensor and denominator calculation](Yin_C_A0189_v1.md#endpoint-spaces)
Pass to \(U\otimes_B U\) using the right \(B\)-space in the first factor and the left \(B\)-space in the second.
Every boundary at a label in \(H\) vanishes there.
For \(u\notin B\), the tensor \(\delta_Bu\) has rank two since \(1,u\) are independent on each side over \(B\).
Its first factor space is the right span of \(1,u\), and its second factor space is their left span.
Indeed the images of contractions by linear functionals on the opposite space give these spaces, since functionals on a finite-dimensional subspace over a division ring extend to the whole vector space.
Thus zero exceptional rank forces \(u\in B\).

With a single nonzero exceptional term \(\Psi_g(l\otimes r)\), its first factor space is contained in \(l(B+gB)\) and its second in \((B+Bg)r\).
They both contain \(1,u\), so \(1=ld,\ u=ln\) and \(1=d'r,\ u=n'r\) with the stated coefficients.
Direct finiteness of \(U\) makes \(d,d'\) units.
Both fractions therefore lie in \(D_G\).
If \(u\in B\), take both denominators equal to \(1\).

For the converse, every \(b\in B\) has an expansion of \(\delta b\) in complex tensor boundaries at labels of \(S_0\).
This follows by the derivation rule, the identity \(\delta(a^{-1})=-a^{-1}(\delta a)a^{-1}\), and the definition of the division closure.
All products here use the outer bimodule actions.
If \(u=d^{-1}n\), write \(d=d_0+gd_1,\ n=n_0+gn_1\) with coefficients in \(B\).
In \(\delta u=d^{-1}(\delta n-(\delta d)u)\), the only boundary needed at \(g\) is \(\Psi_g(d^{-1}\otimes(n_1-d_1u))\).
For the other fraction write \(d'=d_0'+d_1'g,\ n'=n_0'+n_1'g\).
In \(\delta u=(\delta n'-u\delta d')d'^{-1}\) the exceptional term is \(\Psi_g((n_1'-u d_1')\otimes d'^{-1})\).

### Two ranks outside the subgroup

Discard terms balanced over \(B\) and terms with a zero factor.
The only remaining case has \(u\notin B\) and exactly two terms with labels \(g_i\notin H\).
Each \(g_i\) is outside \(U_H\), since a bounded group unitary belonging to \(U_H\) would belong to the group von Neumann algebra of \(H\), whose Fourier support lies in \(H\).
Thus \(B+g_iB\) and \(B+Bg_i\) have dimension two on their respective sides.
The unit condition implies the same for
\[
 E_i=l_i(B+g_iB),\qquad F_i=(B+Bg_i)r_i .
\]
Let \(a=\dim_B(E_1+E_2)\) on the right and \(b=\dim_B(F_1+F_2)\) on the left.
The four first factors and four signed second factors express \(\delta_Bu\) as a matrix product through \(B^4\), with factors of ranks \(a,b\).
The dimension formula over the division ring gives \(2\ge a+b-4\).
Hence \(a\le3\) or \(b\le3\).
In the first case choose \(0\ne w=l_1d_1=l_2d_2\in E_1\cap E_2\).
Both \(d_i\in B+g_iB\) are units, so \(E_1+E_2\subset wD_G\).
Since \(1,u\in E_1+E_2\), write \(1=wc,\ u=we\) with \(c,e\in D_G\).
Direct finiteness and division closure give \(w=c^{-1}\in D_G\).
For \(b\le3\) choose a common nonzero vector in \(F_1\cap F_2\) and apply the same argument on the left.

### Rotation of a binomial

Work in \(U_{\langle H,g\rangle}\), which embeds with its units in \(U\).
If \(b_0,b_1\in B\) are both nonzero, right multiplication of \(b_0+gb_1\) by \(b_0^{-1}\) gives \(1+v\) with \(v=gb_1b_0^{-1}\).
The trace-preserving character automorphisms parametrized by the circle fix \(B\) and send \(v\) to \(s^{\chi(g)}v\).
For an affiliated operator, the algebraic right kernels of \(v-\lambda\) for distinct complex scalars \(\lambda\) have direct sum inside the right regular module for every finite set of scalars.
Applying the polynomials \(\prod_{\mu\ne\lambda}(v-\mu)\) to a finite relation isolates its terms.
The sum of their dimensions is consequently at most one.
Since the circle action preserves these dimensions and \(\chi(g)\ne0\), every nonzero eigenvalue has kernel dimension zero.
In particular \(1+v\) is an affiliated unit.
If only one coefficient is nonzero the binomial is already a unit.
The left binomials obey the same proof using \(v=b_0^{-1}b_1g\) after left multiplication by \(b_0^{-1}\).

## Assessment history

### Decision ranks-outside-a-subgroup

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:01 |
| status | proved |
| reason | Balancing over a subgroup division ring places both endpoints in two coefficient spaces, giving a fraction or a common unit denominator. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One exceptional rank with arbitrary subgroup ranks, two under the binomial unit hypothesis, and the cyclic probability-one case. |
| argument | [Argument](#argument) | Contraction of tensors on both sides over a division ring, the endpoint dimension bound and circle rotations of binomials. |
| dependency | [Common denominators](Yin_C_A0189_v1.md#endpoint-spaces) | Passage between complex tensor length and operator rank. |
| dependency | [Finite-rank equation](Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) | The signs and sides of the tensor boundaries. |
| dependency | [Cyclic division field](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) | The coefficient field for a marked infinite cyclic subgroup. |
| dependency | [Constant graph lift](Yin_C_A0174_v1.md#the-angular-probability-bound) | A graph symmetry with unit contraction probability. |
| review | [Ranks outside a subgroup](../audits/reviews/Yin_R_A0180_v1.md#ranks-outside-a-subgroup) | Independent review of the statement and argument. |

## Current assessment

[Selected decision](#decision-ranks-outside-a-subgroup)
