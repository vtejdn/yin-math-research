---
author: Yin
---

# Lifting the binary lamps through an abelian kernel

## Statement

Write \(\Gamma=B\rtimes\langle s\rangle=C_2\wr\mathbb Z\), where \(B\) is the additive group of \(\mathbb F_2[X,X^{-1}]\) and \(s\) acts by multiplication by \(X\).
Consider a countable group extension
\[
       1\longrightarrow A\longrightarrow G
        \stackrel{\pi}{\longrightarrow}\Gamma\longrightarrow 1 .
\]
Write \(U_H=L^0(\mathcal N(H))\) and \(D_H=\operatorname{Div}_{U_H}(\mathbb CH)\) for a discrete group \(H\).

1. If \(A\) is central and has no element of order two, \(G\) contains a subgroup \(J\cong\Gamma\) for which \(A\times J\) has index two in \(G\) and \(D_G\cap U_J=D_J\).
   Thus the positive integral group-ring element from the [two-run calculation](Yin_C_A0173_v1.md#statement) has a kernel projection outside \(D_G\) when formed in this copy of \(\Gamma\).
   For finitely generated \(G\) that projection satisfies [the unrestricted finite-rank equation](Yin_C_A0131_v1.md#statement) and attains the [inclusive probability threshold](Yin_C_A0174_v1.md#statement) \(1/2\), while every lift fails the strict threshold.
2. If \(A\) is torsion-free abelian of finite rational rank \(d=\dim_{\mathbb Q}(A\otimes_{\mathbb Z}\mathbb Q)\), the lamps can act on \(A\) by conjugation.
   Even then \(G\) contains a copy of \(\Gamma\) whose lamps project isomorphically onto an ideal of codimension at most \(2d\) in \(B\).
   Consequently a torsion-free extension of \(\Gamma\) by an abelian group requires infinite rational rank in its kernel.
   For every torsion-free \(G\) with abelian kernel, \(D_G\) is a division ring by [Linnell's theorem](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems).
   Hence in the finitely generated case the unrestricted equation already characterizes membership in \(D_G\).
3. Suppose instead that \(a,b\) are distinct elements of any torsion-free group with \(a^2=b^2=z\).
   Then \(\langle a,b\rangle\) is a Klein bottle group.
   In its regular representation at each central character \(z\mapsto\zeta\in\mathbb T\), divide both \(a,b\) by one scalar square root of \(\zeta\).
   The resulting selfadjoint unitaries are freely independent, each taking the values \(1,-1\) with equal trace weights.
   For each choice of signs, the intersection of the two corresponding eigenspaces is zero.
   Thus common squares in a torsion-free group preclude the adjacent joint sign projection used to mark the start of a lamplighter cell.

## Argument

### The subgroup over even lamp configurations

Choose lifts \(t,a_0\) of \(s\) and the lamp \(X^0\) and set \(a_i=t^ia_0t^{-i}\).
If \(A\) is central, all \(a_i^2\) are equal to \(a_0^2\), and \([a_i,a_j]\in A\) since the lamps commute in the quotient.
Consequently \([a_i,a_j]^2=[a_i^2,a_j]=1\), and the assumption on \(A\) makes the \(a_i\) commute.
The elements \(b_i=a_{i+1}a_i^{-1}\) are commuting involutions with images \((X-1)X^i\).
These images form a basis of the ideal \((X-1)B\), since multiplication by \(X-1\) is injective on the Laurent polynomial ring.
In particular \(t\) shifts the \(b_i\), and \(\pi\) maps \(J=\langle b_0,t\rangle\) isomorphically onto \((X-1)B\rtimes\langle s\rangle\).
Indeed any relation has zero height and then reduces to a relation among the indicated basis vectors.
Evaluation at \(X=1\) identifies the quotient of \(B\) by this ideal with \(\mathbb F_2\).
It follows that \(A J\) is the full preimage of this index-two subgroup, and centrality together with \(A\cap J=\{1\}\) gives \(A J=A\times J\).

Finite-index restriction gives \(D_G\cap U_{A\times J}=D_{A\times J}\). [Coset coefficients](../ledger/Yin_L_A0073_v1.md#the-finite-index-coefficient-matrices)
For the direct product, Fourier transformation on \(A\) makes elements of \(U_J\) constant fields over its compact dual with Haar probability measure.
Each finite scalar rational expression over \(\mathbb C[A\times J]\) defined in \(U_{A\times J}\) can be evaluated in \(U_J\) almost everywhere.
Indeed coefficients are finite sums of characters times elements of \(\mathbb CJ\), products and sums are fiberwise, and an affiliated unit has zero kernel and cokernel on almost every fiber.
Evaluating a rational expression for a constant field at a point where all these gates are defined and the result equals the field gives \(D_{A\times J}\cap U_J=D_J\). [Fiber evaluation argument](Yin_C_A0132_v1.md#argument)
Combining the intersections proves the assertion about \(D_G\).
The trace-preserving inclusion of the subgroup algebra preserves spectral projections, so the projection from the two-run calculation remains the kernel projection of the same positive element of \(\mathbb ZJ\subseteq\mathbb ZG\).
It belongs to the \(*\)-regular closure of \(\mathbb CG\), which gives the claimed equation and the inclusive threshold by their respective criteria.

### The square classes of lifts

Now let \(A\) be torsion-free abelian, written additively when discussing \(A/2A\).
Conjugation on \(A\) factors through \(\Gamma\).
The kernel \(B_0\) of the action of \(B\) on \(A\) is an ideal in \(B\), since the action kernel is invariant under \(s\) and \(s^{-1}\).
Its preimage \(N_0=\pi^{-1}(B_0)\) centralizes \(A\) and is abelian.
In fact for \(v,w\in N_0\), both \(v^2\) and \([v,w]\) lie in \(A\), so centrality in \(N_0\) gives \([v,w]^2=1\).
Squaring in \(N_0\) defines a homomorphism
\[
    \omega:B_0\longrightarrow A/2A,\qquad
    \pi(v)\longmapsto v^2\bmod 2A .
\]
Changing the lift changes its square by an element of \(2A\).
The map intertwines multiplication by \(X\) with the conjugation action of \(t\) on \(A/2A\), where \(t\) is any lift of \(s\).
Each element of \(\ker\omega\) has a unique lift in \(N_0\) whose square is the identity, by dividing any lift by a square root of its square in \(A\) and using \(A[2]=0\).
Thus \(\pi\) identifies the subgroup \(N_0[2]\) with the ideal \(I=\ker\omega\), compatibly with the shift.

When \(d\) is finite, the commuting involutions from \(B\) on \(A\otimes\mathbb Q\) have a simultaneous eigenbasis over \(\mathbb Q\).
One can successively split into sign eigenspaces whenever an operator is nonscalar on a current joint invariant summand, which takes at most \(d-1\) splittings for \(d>0\).
The image lies in the group of \(d\) diagonal signs, so \(B_0\) has codimension at most \(d\), using injectivity of \(A\to A\otimes\mathbb Q\).
Also \(\dim_{\mathbb F_2} A/2A\le d\).
Indeed a rational dependence among lifts of mod-two independent elements would give an integral dependence with relatively prime coefficients after clearing denominators and dividing their common divisor, using torsion-freeness of \(A\).
Reduction modulo two contradicts independence.
Consequently \(I\) has codimension at most \(2d\) in the infinite-dimensional space \(B\).
As a nonzero ideal in \(\mathbb F_2[X,X^{-1}]\), it has the form \(f B\) for a nonzero Laurent polynomial \(f\).
The shifts of the unique involutive lift of \(f\) are independent commuting involutions by their images \(X^i f\).
Together with \(t\) they give the required copy of \(\Gamma\).

For example, if the entire lamp preimage centralizes \(A\), one has \(B_0=B\) in every rank.
In that case \(G\) is torsion-free exactly when the classes of the squares \(a_i^2\) are linearly independent in \(A/2A\).
Indeed they are the images of the basis \(X^i\) under \(\omega\), and every nonidentity torsion element must have height zero and project to a nonzero lamp of order two.
Its square lies in the torsion-free group \(A\), so it is an involution.
Without the centralizing assumption, every torsion-free \(G\) in an extension with abelian kernel still belongs to Linnell's class \(\mathcal C\).
Both \(A\) and \(\Gamma\) are elementary amenable, as is their extension, and \(\mathcal C\) contains the trivial group and is closed under extensions with elementary amenable quotient.
Linnell's Theorem 1.5 now gives a division ring \(D_G\), proving the assertion about the finite-rank equation.

### Common squares in a torsion-free group

Let \(w=ab^{-1}\).
The common square \(z\) centralizes \(\langle a,b\rangle\), \(w\) has infinite order, and \(awa^{-1}=w^{-1}\).
For the last equality use \(a^2b^{-1}a^{-1}=ba^{-1}\).
If \(w^k=z^\ell\), conjugating by \(a\) gives \(w^{-k}=z^\ell\), so \(k=0\), then \(\ell=0\) since \(a,b\) are distinct and \(z\) has infinite order.
Also no odd power of \(a\) belongs to \(\langle w\rangle\), since conjugation by that power inverts \(w\).
It follows that the normal forms \(w^k a^j\), \(k,j\in\mathbb Z\), are unique, and \(w,a\) generate \(\langle a,b\rangle\).
This gives the Klein bottle presentation and identifies its quotient by \(\langle z\rangle\) with \(C_2*C_2\), generated by the images of \(a,b\).

For each \(\zeta\) the twisted regular representation at \(z=\zeta\) acts on the square-summable functions on the cosets of \(\langle z\rangle\).
With the trace at the identity coset, a group element outside \(\langle z\rangle\) has trace zero because it moves that coset.
For \(r^2=\zeta\), the two operators \(S=a/r,\ T=b/r\) are unitary involutions.
Every nonempty alternating word in \(S,T\) projects to a reduced word in \(C_2*C_2\), so its trace is zero.
The centered elements of the individual two-dimensional algebras are scalar multiples of their respective involutions, which proves freeness and the equal trace weights.
Moreover \(ST=ab^{-1}=w\), whose nonzero powers all have trace zero and whose spectral measure is Haar measure on \(\mathbb T\).
A joint signed eigenvector would give an eigenvector of \(ST\) of sign \(1\) or \(-1\), both of whose spectral projections vanish by faithfulness.
This proves the assertion for each central character.

## Assessment history

### Decision lifts-of-binary-lamps

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:01 |
| status | proved |
| reason | Square classes and the shift exhibit an actual lamplighter subgroup for finite-rank abelian kernels, and common squares in a torsion-free group give a Klein bottle. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Central and finite-rank abelian extensions, rational projection descent and the common-square obstruction. |
| argument | [Argument](#argument) | Even lamp configurations, finite-dimensional character spaces, square classes and the dihedral fibers. |
| dependency | [Two-run projection](Yin_C_A0173_v1.md#statement) | A nonrational kernel projection on the binary lamplighter. |
| dependency | [Unrestricted equation](Yin_C_A0131_v1.md#statement) | Solvability for a kernel projection and the strong Atiyah case. |
| dependency | [Angular criterion](Yin_C_A0174_v1.md#statement) | The inclusive threshold and the strict threshold. |
| dependency | [Linnell's division ring theorem](../audits/literature/Lin93/Yin_U001.md#lin93-u001) | Torsion-free elementary amenable extensions. |
| dependency | [Coset matrices](../ledger/Yin_L_A0073_v1.md#the-finite-index-coefficient-matrices) | Division closure under finite-index restriction. |
| dependency | [Fiber evaluation](Yin_C_A0132_v1.md#argument) | Simultaneous evaluation of the finitely many inverse gates. |
| review | [Lifts of binary lamps](../audits/reviews/Yin_R_A0180_v1.md#lifts-of-binary-lamps) | Independent review of the statement and argument. |

## Current assessment

[Selected decision](#decision-lifts-of-binary-lamps)
