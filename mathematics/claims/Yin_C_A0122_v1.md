---
author: Yin
---

# A four-dimensional rank test descending through a mixed commutation relation

## Statement

Let
\[
 G=\langle b,k,a_1,a_2\mid[k^{-1}a_1 k,a_2]=1\rangle,\qquad
 V_1=\langle b,k,a_1\rangle,\quad V_2=\langle b,a_2\rangle,\quad H=\langle b\rangle .
\]
The group is torsion-free, and it is a proper quotient of \(V_1*_H V_2\) retaining the indicated vertex groups.
For \(p=1-b+a_1+a_2\), any \(u\in\mathbb C V_1\) and any \(v\in\mathbb C V_2\), the regular matrix
\[
                   M=\begin{pmatrix}p&u\\v&-p\end{pmatrix}
\]
has rank two, \(p\) has rank one and \(1+(p^{-1}v)(p^{-1}u)\) is an affiliated unit.
The two-weight unitary deformation with both corner pivots invertible can achieve this on four auxiliary coordinates.
It cannot achieve those two pivots on two auxiliary coordinates for this presentation.
These dimension assertions concern that particular test.

## A bend on the quotient

Substitute \(d=k^{-1}a_1 k\) in the presentation.
The result is \(\langle d,a_2\mid[d,a_2]=1\rangle*F(b,k)\), proving torsion-freeness.
The normal form identifies \(\langle d,b,k\rangle\) with a free group of rank three, and replacing \(d\) by \(kdk^{-1}\) preserves this vertex subgroup.
The other vertex is the free group on \(b,a_2\); the two intersect in \(\langle b\rangle\) by the same free-product normal form.
Their amalgam is free on the four original letters, where the added commutator is nontrivial.

On \(\mathbb C^2\otimes\mathbb C^2\) put \(J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) and let \(S\) swap the two tensor factors.
Use the representations of the two vertices sending \(b\) to the identity, \(k\) to \(S\) and each \(a_i\) to \(J\otimes I\).
On the second vertex conjugate by \(D_t=\operatorname{diag}(t,1)\otimes I\) for \(|t|=1\).
The conjugated image of \(a_2\) acts on the first tensor factor, while the image of \(k^{-1}a_1k\) is \(I\otimes J\).
They commute at every phase, so these representations are defined on the quotient \(G\).
For \(p_L=1-b+a_1,\ p_R=a_2\), the two off-diagonal pivots in the regular twist are \(\lambda(a_1)\otimes I_2\) and \(\lambda(a_2)\otimes I_2\).
The [equal block calculation](Yin_C_A0121_v1.md#the-regular-rank-computation) requires only infinitely many admissible phases and full pivots.
Its specialization gives the two asserted ranks and the Schur conclusion on \(G\), without transferring a kernel from the group before imposing the relator.
For instance \(u=1+k+a_1,\ v=1+a_2\) give three independent coefficients by comparison at \(k,b,a_2\), and the supports generate \(G\).

## The obstruction in dimension two

In dimension two the weights are two lines; choose their basis so \(D_t=\operatorname{diag}(t,1)\).
For any proposed vertex representations, let \(A,B,K\) denote the matrices for \(a_1,a_2,k\).
The common edge generator preserves the lines in the two-weight test.
Hence its contribution to the off-diagonal pivot of \(p_L\) vanishes, so the test requires \(A_{12}\ne0\) and \(B_{21}\ne0\).
For the mixed relator to hold at infinitely many phases, \(K^{-1}AK\) must commute with each Laurent coefficient of \(D_tBD_t^{-1}\).
In particular it commutes with \(B_{21}E_{21}\).
A two-by-two unitary commuting with \(E_{21}\) is scalar: equating entries gives a lower triangular matrix with equal diagonal entries, and unitarity kills its strict lower entry.
Thus \(A\) is scalar, contradicting \(A_{12}\ne0\).
The extra tensor factor permits a nontrivial unitary commutant while retaining invertible off-diagonal pivots.
This calibration is within the known free-product closure of torsion-free Atiyah groups, since \(G\cong\mathbb Z^2*F(b,k)\). [Finite-edge permanence](../ledger/Yin_L_A0001_v1.md#known-positive-results)

## Assessment history

### Decision four-coordinate-mixed-relation

| Field | Value |
| --- | --- |
| date | 2026-11-22T04:54 |
| status | proved |
| reason | Independent review verifies the full statement and argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A genuine mixed relator allowing a four-coordinate full-rank test, while two auxiliary lines cannot provide its two required corners. |
| argument | [Proof](#a-bend-on-the-quotient) | Group normal form, tensor-factor swap, regular rank comparison and the two-dimensional unitary commutant. |
| review | [Whole finding](../audits/reviews/Yin_R_A0159_v1.md#whole-finding) | Independent whole-argument finding at the stated scope. |

## Current assessment

[Selected decision](#decision-four-coordinate-mixed-relation)
