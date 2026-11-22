---
author: Yin
---

# Independent review of the mixed commutation relation and the four-dimensional rank test

## Whole finding

At 2026-11-22T04:52 UTC an agent acting for Yin independently checked the complete statement and both proof sections of C_A0122_v1.
The reviewer did not participate in developing this argument and received the fixed proof and its review scope without the development dialogue, author explanations or a prior verdict on this claim.
The full-rank conclusions for all the stated coefficients, the example, and the two assertions about the dimension of the test hold.

Introducing \(d=k^{-1}a_1k\) and eliminating \(a_1\) gives \(G=P*Q\), where \(P=\langle d,a_2\rangle\cong\mathbb Z^2\) and \(Q=F(b,k)\).
Every finite-order element of a free product is conjugate into a factor, so \(G\) is torsion-free.
The first vertex has reduced forms with \(P\)-syllables in \(\langle d\rangle\) and arbitrary \(Q\)-syllables, since \(kdk^{-1}\) and \(d\) generate the same subgroup together with \(Q\).
The second has \(P\)-syllables in \(\langle a_2\rangle\) and \(Q\)-syllables in \(\langle b\rangle\).
Uniqueness of the reduced form and \(\langle d\rangle\cap\langle a_2\rangle=1\) force a common element to lie in \(\langle b\rangle\).
The two vertices are free on the displayed generators since conjugating the free generator \(d\) by \(k\) while fixing \(b,k\) is an automorphism of \(\langle d\rangle*Q\).
The abstract amalgam of these free groups along their common basis letter \(b\) is free on \(a_1,a_2,b,k\).
The word \(k^{-1}a_1k\,a_2\,k^{-1}a_1^{-1}k\,a_2^{-1}\) is reduced there, proving properness of the quotient.

The eigenspaces for the two weights on the first tensor factor each have dimension two.
Conjugation by the swap sends \(J\otimes I\) to \(I\otimes J\), which commutes with \((\operatorname{diag}(t,1)J\operatorname{diag}(t^{-1},1))\otimes I\) for every unit phase.
Thus the twist is a representation of the specified quotient at each such phase.
The two regular corner maps have the unitary group translations \(\lambda_G(a_1)\) and \(\lambda_G(a_2)\) tensored with the identity on the second factor.
For the unnormalized trace, the unitary implementing the regular twist fixes the whole identity fiber, so the phase ranks equal four times the original ranks.
Multiplication of the second weight rows by \(t\) leaves polynomials of degree at most one for the scalar and the matrix.
With the row and column orders of C_A0118_v1, their constant terms are block triangular with diagonal blocks \(R_{21},L_{12}\) and \(R_{21},-R_{21},-L_{12},L_{12}\), respectively.
All alterations contributed by arbitrary \(u\) on the first vertex and \(v\) on the second lie off these diagonals at zero.
Their ranks at zero are therefore four and eight.
The degree-one Vandermonde bound on \(N\) distinct unit phases gives \(4(N-1)\le4N\operatorname{rk}_G p\) and \(8(N-1)\le4N\operatorname{rk}_G M\).
Taking \(N\) arbitrarily large gives the claimed full ranks.
In the finite affiliated algebra the full-rank square scalar \(p\) is a unit, and eliminating it leaves the full-rank scalar \(-p-vp^{-1}u=-p[1+(p^{-1}v)(p^{-1}u)]\), with the factors in the asserted order.
For the explicit example a linear relation among \(p,u,v\) has zero coefficients successively at \(k,b,a_2\) only if all its multipliers vanish.
Their combined supports contain \(a_1,a_2,b,k\).

For the two-dimensional test, diagonalize the two weights in an orthonormal basis.
Preservation of their lines by the edge image removes its off-diagonal contribution.
Invertibility of the specified pivots thus forces \(A_{12}\ne0\) and \(B_{21}\ne0\).
For infinitely many distinct admissible phases, the Laurent polynomial \([K^{-1}AK,D_tBD_t^{-1}]_{\rm add}\) vanishes, where the bracket here denotes the additive matrix commutator.
Its \(t^{-1}\) coefficient implies that \(K^{-1}AK\) commutes with \(E_{21}\).
Solving that commutation equation gives a matrix of the form \(\left(\begin{smallmatrix}c&0\\e&c\end{smallmatrix}\right)\).
The second column of a unitary has norm one, so \(|c|=1\), and the norm of the first then gives \(e=0\).
Consequently \(A\) is scalar in every basis, contrary to the first pivot.
This obstruction uses the two-weight unitary deformation with fixed vertex representations and both prescribed full pivots.
The Atiyah permanence observation uses the existing finite-edge result at its trivial-edge specialization for \(\mathbb Z^2*F(b,k)\).
The present rank calculation is independent of that observation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0122_v1.md#statement) | Quotient and vertex structure, regular ranks for every specified pair, affiliated invertibility and dimension scope. |
| [Whole finding](#whole-finding) | [A bend on the quotient](../../claims/Yin_C_A0122_v1.md#a-bend-on-the-quotient) | Reduced forms, intersection and properness, tensor representation, quotient phases, both pivots and the coefficient example. |
| [Whole finding](#whole-finding) | [Obstruction in dimension two](../../claims/Yin_C_A0122_v1.md#the-obstruction-in-dimension-two) | Arbitrary unitary vertex representations for the two-weight test, the Laurent coefficient and the unitary commutant. |
| [Whole finding](#whole-finding) | [Regular rank computation](../../claims/Yin_C_A0121_v1.md#the-regular-rank-computation) | Equal-weight-multiplicity specialization to the quotient with multiplicity two, identity-fiber rank and affiliated Schur complement. |
| [Whole finding](#whole-finding) | [Triangular specialization](../../claims/Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization) | Orders and signs of the constant blocks of both polynomials and dependence on the unrestricted vertex coefficients. |
| [Whole finding](#whole-finding) | [Polynomial rank inequality](../../claims/Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | Bounded matrix coefficients, degree one and arbitrary finite sets of distinct unit phases. |
| [Whole finding](#whole-finding) | [Known positive results](../../ledger/Yin_L_A0001_v1.md#known-positive-results) | Applicability of the finite-edge theorem to a free product of the two identified torsion-free Atiyah groups. |
