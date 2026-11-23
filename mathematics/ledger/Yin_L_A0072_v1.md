---
author: Yin
---

# What a positive nullity gap would imply for a fixed Schur matrix

## The group and the quantifiers in the gap

For the [original-group test](../claims/Yin_C_A0125_v2.md#group-ring-witnesses-and-the-exact-projection), a positive gap for one regular group \(G\) and one matrix \(A\) means that some \(\epsilon(G,A)>0\) bounds every strictly positive nullity of \(B(h)^*B(h)\) from below for all \(h\in\mathbb CG\).
A single exact \(h\) leaves the positive nullities of all other inputs to be determined.
For each fixed finite support the [rank-stratum calculation](../claims/Yin_C_A0128_v1.md#exact-and-positive-defects-on-a-fixed-support) identifies a necessary and sufficient constructibility condition.
Even when separate supports satisfy it, their positive lower bounds may tend to zero.

Suppose the Schur kernel actually has trace \(1/2\) in \(G\), and place exactly the same coefficients at the origin of \(W=G\wr\mathbb Z\).
The [binomial shift calculation](../claims/Yin_C_A0127_v1.md#from-finite-blocks-to-the-trace-rank) gives a strictly positive nullity tending to zero with no change of group, matrix \(A\), or three-by-three formula along that sequence.
Only its shift polynomial varies.
One can also embed \(W\) into \(W*\mathbb Z\), retaining all these strict nullities.
The extra free generator there gives an [exact finite-support input](../claims/Yin_C_A0125_v2.md#free-cyclic-extension-at-depth-two) for that same matrix.
Thus the existence of an exact input and the absence of a uniform lower bound on the positive values are compatible consequences of a hypothetical regular half kernel, in a common torsion-free overgroup.

## The scalar hypothesis under wreath extension

Write \(P_0(L)\) for regular injectivity of every nonzero element of \(\mathbb CL\).
Then
\[
             P_0(G\wr\mathbb Z)
           \quad\Longleftrightarrow\quad
             P_0(G^k)\text{ for every finite }k\ge1 .
\]
Necessity follows by subgroup restriction, since the representation on every right coset replicates the subgroup regular representation.
Conversely a nonzero element of the group ring of the base \(\bigoplus_{\mathbb Z}G\) uses finitely many sites, and hence is an affiliated unit under the hypotheses on the direct powers.
Write a nonzero element of the wreath group ring as \(\sum_{j=j_0}^{j_1}a_jt^j\) with \(a_{j_0}\ne0\) and all \(a_j\) in that base group ring.
The bounded polynomial \(\sum_j z^{j-j_0}a_jt^j\) has an affiliated-unit constant coefficient.
The [polynomial rank estimate](../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) gives full rank off a countable set of complex parameters.
On the unit circle the height character twists are implemented in the regular representation and preserve the trace, so the same full rank holds at \(z=1\).

This specifies exactly what is needed for the wreath calculation to retain the scalar hypothesis on the enlarged group.
The implication from \(P_0(G)\) alone to the hypotheses on all its direct powers remains unproved here.
Under the global scalar-injectivity hypothesis for all torsion-free groups, a uniform positive gap for every fixed half-kernel test family in those groups would already rule out every half-dimensional Schur kernel.
Conversely, absence of any half-dimensional Schur kernel makes that universally quantified assertion about half-kernel families vacuous.

## Parity in the second inverse layer

For \(H=G*\mathbb Z\), a half kernel on \(G\) yields \([1]=2[P]\) in \(K_0(D_2(H))\).
The new [odd stabilization test](../claims/Yin_C_A0129_v1.md#odd-stabilization) shows exactly what it would take to exclude even virtual halves, including those not initially given by an actual scalar projection.
One has to exclude a pair of anticommuting involutions at every odd size over this ring.
Such a pair would also [yield a group-ring positive matrix](../claims/Yin_C_A0129_v1.md#a-positive-matrix-over-the-original-group-ring) whose nullity is an odd integer divided by two, with size dependent on the certificate.
It need not be a member of the fixed three-by-three family.
In particular the parity question cannot be settled just by reading a three-by-three gap as a bound at arbitrary sizes.

There is a specific relative group in which a half would be visible.
For torsion-free \(H\), [Ope26g, Corollary 1.2(i) and Section 10](../audits/literature/Ope26g/Yin_U001.md#ope26g-u001) identifies the regular trace image of \(K_0(\mathbb CH)\) with \(\mathbb Z\).
The source check verifies the deduction from the preprint's Bass trace theorem, taking that theorem as an external input.
If \(2z=[1]\) in \(K_0(D_2(H))\), the induced affiliated dimension gives \(\dim z=1/2\), whereas every class extended from \(\mathbb CH\) has integer dimension by that result.
Consequently \(z\) has nonzero image of exact order two in
\[
       K_0(D_2(H))\,/\,\operatorname{im} K_0(\mathbb CH).
\]
Excluding two-torsion in this cokernel would suffice.
The group-ring trace result alone leaves that relative statement open.

The [nonregular comparison](../claims/Yin_C_A0130_v1.md#the-two-behaviors-of-the-fixed-schur-kernel) realizes both phenomena for a fixed two-by-two input in one faithful tracial representation of a torsion-free group satisfying scalar injectivity in that representation.
Its shift gives arbitrarily small positive defects, a different generator acts as the exact input, and the resulting projectives halve the unit.
The missing hypothesis in this comparison is the joint regular trace.
The [Klein bottle calculation](../claims/Yin_C_A0129_v1.md#a-torsion-free-calibration-for-multiplicative-commutators) separately shows why merely finding a pair of invertible anti-commuting scalars, without the involution condition, does not certify an even unit.
