---
author: Yin
---

# A radius-five test for a half-dimensional coordinate in the original group

## Statement

Let \(p\) be a projection in the regular group von Neumann algebra with trace \(\alpha\), put \(q=1-p\), and fix a scalar affiliated operator \(z\).
For a finite set \(B\subset G\) maximize \(\operatorname{rk}(q(z+v)p)\) over \(v\in\mathbb C B\), and denote the maximum by \(r\).
Suppose there are real coefficients \(c_g\), supported in \(B\), satisfying \(\sum_g c_g=1\), such that \(\mathcal T=\sum_g c_g\operatorname{Ad}(g)\) has norm at most \(\kappa\) on the trace-zero subspace of \(L^2(\mathcal N(G))\).
Then
\[
   (\alpha-r)(1-\alpha-r)
       \ \le\ \kappa^2(1-\alpha+r)(\alpha+r).
\]
Almost every complex choice of the coefficients of \(v\) attains the maximum.
At \(\alpha=1/2\) this gives \(r\ge\tfrac12-\kappa/(1+\kappa)\).
For an actual two-by-two Schur input, taking \(p=p_{\ker S}\) and \(z=a^{-1}b_0\) gives the excess \(b-h\) in the [original-group shear test](Yin_C_A0257_v1.md#kernel-images-and-the-positive-polynomial-test).
When \(z=0\) it is the excess for a single extra equation \(y=v x_i\) if the original kernel has image \(pU\) at coordinate \(i\).

Suppose \(a_0,b_0'\) freely generate \(F_2\) in \(G\) and \(C_{F_2}(g)\) is cyclic or trivial for every \(1\ne g\in G\).
Use for \(B\) the 364 freely reduced words of lengths one, three and five in that pair.
Then one can take \(\kappa=9\sqrt3/122<1/7\).
In particular for a half-dimensional Schur kernel, one of the shears with integer coefficients between \(1\) and \(3640\) on precisely these words has \(b-h>27/80>1/3\).
The original Schur coefficients may use the two generators.

In any finitely generated torsion-free group with this free-pair property, strong Atiyah is equivalent to the following restricted rank test.
Take the supremum of \((b-h)_+\) over all original polynomial kernels, distinguished coordinates \(x_i\), and rows \(y=v x_i\) on one new unknown with \(v\) on the same list of 364 words and coefficients in \(\{1,\ldots,23296\}\).
The test requires this supremum to be strictly less than \(1/3\).
Equivalently one can require absence of an individual test with \(b-h\ge1/3\), since in the division-ring case all excesses vanish.
For the universal conjecture it suffices to test groups of the form \(K*F_2\), with \(K\) finitely generated and torsion-free.
Only the added row has the fixed support and coefficient bounds; the input polynomial matrix is unrestricted.

## What maximal rank on a fixed support forces

Right-multiply \(q(z+v)p\) by the affiliated unit \(t=(1+(qzp)^*(qzp))^{-1/2}\), which commutes with \(p\).
The resulting affine family on \(p\) is bounded and has unchanged rank.
The [polynomial rank sublevel theorem](Yin_C_A0128_v1.md#statement) gives a maximal rank attained outside a countable union of proper algebraic sets of coefficients, hence almost everywhere.
At a maximizer let \(P\) be the kernel projection within \(p\) before right regularization, and let \(E\) be the residual image projection within \(q\), the complement of the range there.
Their traces are \(u=\alpha-r,\ w=1-\alpha-r\).

For every \(g\in B\) one has \(E g P=0\).
Indeed write \(P'\) for the restricted kernel after regularization; the affiliated image of \(tP'\) is \(PU\).
At the selected matrix vary the coefficient of \(g\) by a complex number \(\lambda\).
Split the bounded domain into its initial support and \(P'\) inside \(p\), and the target into its final support and \(E\) inside \(q\).
For \(\lambda\ne0\) divide the second output block row by \(\lambda\); this preserves rank.
At zero the rescaled operators converge in norm to a lower triangular block matrix.
Its first diagonal entry is the initial-to-final part of the selected operator and its second is \(E g tP'\).
The first entry has an affiliated inverse between its supports, so the limit rank is \(r+\operatorname{rk}(EgtP')\).
Lower semicontinuity gives rank of this limit at most the maximal rank \(r\). [Triangular perturbation calculation](Yin_C_A0232_v1.md#adding-one-monomial-in-the-original-group)
It follows that \(EgP=0\), as asserted.

Consequently \(\tau(E\mathcal T(P))=0\), also for signed coefficients.
Subtract the traces from both projections and apply the norm hypothesis to obtain
\[
          uw\le \kappa\sqrt{u(1-u)w(1-w)} .
\]
Squaring and cancelling nonzero factors yields the inequality in the statement; it also holds if either trace vanishes.
At half trace \(u=w\), giving the stated bound.
For the extra polynomial row the joint coordinate image is the graph on \(pU\), of dimension \(\alpha\), and the sum of the separate images is \(pU+vpU\), of dimension \(\alpha+\operatorname{rk}(qvp)\).

## Signed averages on the two free generators

Use the symmetric simple-walk conjugation average \(C\) on the four letters.
Its norm on the trace-zero subspace is at most \(\theta=\sqrt3/2\) by the [cyclic-stabilizer orbit estimate](Yin_C_A0264_v1.md#two-fixed-choices-in-the-marked-group).
For the two-sided norm, positivity of its matrix entries gives \(|\langle Cf,f\rangle|\le\langle C|f|,|f|\rangle\) on the nonidentity group elements; the upper form bound therefore suffices.
For the degree-\(n\) Chebyshev polynomial \(T_n\) of the first kind, apply the selfadjoint polynomial
\[
        T_n(C/\theta)/T_n(1/\theta).
\]
Its coefficients as a finite group average sum to one by evaluation on the identity vector.
They may be signed, and their support consists of words of length at most \(n\) with the parity of \(n\).
On the centered subspace its norm is at most \(1/T_n(1/\theta)=2/(3^{n/2}+3^{-n/2})\), from the Chebyshev formulas on \([-1,1]\) and at \(1/\theta=(\sqrt3+1/\sqrt3)/2\).
For \(n=5\) the support list has \(4+36+324=364\) words and the bound is \(9\sqrt3/122\).
At \(\alpha=1/2\), the maximal rank is therefore strictly greater than \(3/8\).

For any finite list of \(N\) words and a grid of \(M\ge2\) distinct integer coefficient values in each variable, some grid point has rank at least \((1-1/M)^N r\).
Start at a maximizer and successively replace one coefficient by a grid value.
On each such bounded affine line, the [finite-parameter rank estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) gives total rank on the grid at least \(M-1\) times the line supremum, which is at least the current rank.
Right regularization permits its use also for the initial affiliated coefficient.
Taking \(M=10N\) gives a factor at least \(9/10\) by Bernoulli's inequality, proving the half-kernel grid bound.

## A restricted test for the whole group

The centralizer condition makes \(G\) ICC: every nontrivial element has infinitely many conjugates already under the free pair because a cyclic subgroup has infinite index in \(F_2\).
For \(G=K*F_2\) the condition follows from malnormality and free-group centralizers, as in the same [orbit estimate](Yin_C_A0264_v1.md#two-fixed-choices-in-the-marked-group).
Suppose strong Atiyah fails in this group and use the [two possible structures for its scalar regular closure](Yin_C_A0259_v1.md#statement).
In the minimal projection case \(R=M_n(D)\) with \(n\ge2\).
Choose a projection of trace \(\lfloor n/2\rfloor/n\).
In the case without a minimal projection choose a projection in \(R\) with trace in \([2/5,1/2]\), by the [finite packing argument](Yin_C_A0259_v1.md#packing-without-minimal-projections).
Realize each such projection as the image of one coordinate of a group-ring kernel via the [graph construction](Yin_C_A0158_v1.md#group-ring-equations-for-a-regular-closure-matrix).

Except for \(n=3\) the selected trace lies in \([2/5,1/2]\).
For \(r\le17/50\), put \(c=\alpha(1-\alpha)\ge6/25\).
The quotient
\[
       \frac{c-r+r^2}{c+r+r^2}
\]
is nondecreasing in \(c\) and decreasing in \(r\) on this range since \(r^2<c\).
At \(c=6/25,\ r=17/50\) it equals \(39/1739>1/49\).
The maximal-rank inequality above requires this quotient to be at most \(\kappa^2<1/49\), so \(r>17/50\).
Taking \(M=64N=23296\) in the integer grid keeps a fraction at least \(63/64\) and gives \(b-h>(17/50)(63/64)>1/3\).

If \(n=3\), the chosen trace is \(1/3\), and the inequality with \(\kappa<1\) gives \(r>0\).
The grid still gives positive rank.
All these ranks are multiples of \(1/3\) since the inputs and their range projections are over \(M_3(D)\), so this grid already attains at least \(1/3\).
Conversely strong Atiyah implies that the regular closure is a division ring and every [two-coordinate excess vanishes when positive parts are taken](Yin_C_A0255_v1.md#central-projections-and-the-two-coordinate-inequality).
Finally failure in any torsion-free group has a finitely generated input subgroup \(K\).
Regular subgroup inclusion preserves that rank in \(K*F_2\), giving the asserted universal reduction.

## Assessment history

### Decision maximal-shears-on-a-fixed-free-ball

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:44 |
| status | proved |
| reason | Whole-proof review verified the centered norm argument, supports, integer grids and both directions of the universal criterion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The correlation inequality, explicit radius-five support, finite integer grid and universal test. |
| argument | [What maximal rank on a fixed support forces](#what-maximal-rank-on-a-fixed-support-forces) | Affine regularization, triangular perturbations and test of every individual word. |
| argument | [Signed averages on the two free generators](#signed-averages-on-the-two-free-generators) | Two-sided free-orbit bound, Chebyshev polynomial and the integer grid. |
| argument | [A restricted test for the whole group](#a-restricted-test-for-the-whole-group) | Selection of the starting trace, discrete denominator three and the uniform supremum. |
| review | [Maximal shears on a fixed free ball](../audits/reviews/Yin_R_A0206_v1.md#maximal-shears-on-a-fixed-free-ball) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-maximal-shears-on-a-fixed-free-ball)
