---
author: Yin
---
# Independent review of modular kernel counts and finite annihilators

An agent outside the development of C39 v3 inspected its statement, proof and necessary inputs for Yin, without receiving development discussions, author explanations or previous findings about this proof.
The review covered the original argument at 03:58 UTC, the residual eigenvalue at 04:02 UTC and the finite adjoint-orbit criterion at 04:03 UTC on 21 November 2026.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0039_v3.md#statement) | All assertions for the fixed integral element, including the conditional source applications. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0039_v3.md#argument) | Complete proof from the Smith formula through the integral adjoint-orbit criterion. |
| [Whole finding](#whole-finding) | [Residual eigenvalue](../../claims/Yin_C_A0039_v3.md#a-rational-eigenvalue-in-the-subgroup-of-the-residual-element) | Both finite annihilator directions, analytic nullity, restriction to the residual subgroup and dependence on the lift. |
| [Whole finding](#whole-finding) | [Finite adjoint orbit](../../claims/Yin_C_A0039_v3.md#a-finite-adjoint-orbit-test-for-an-exact-annihilator) | Ordered commutator recursion, integral lattice and exact lift of the marked residue. |
| [Whole finding](#whole-finding) | [Fixed-residue correction](../../claims/Yin_C_A0039_v2.md#all-precisions-from-one-modular-right-inverse) | Telescoping construction for every positive precision. |
| [Whole finding](#whole-finding) | [Mghirbi–Douglas witnesses](../literature/MD26/Yin_U001.md#md26-u001) | Theorem C and Proposition 7.11 in the fixed torsion-free group. |

## Whole finding

The complete statement holds under its stated hypotheses.
In Smith normal form, each nonzero invariant factor \(d_i\) contributes \(p^{\min(e,v_p(d_i))}\) choices to the modular kernel, and each free coordinate contributes \(p^e\).
The product of the \(d_i\) divides a nonzero maximal-rank minor of absolute value at most \(L^{r_T}\), giving the uniform error \((\log_p L)/e\) and monotone convergence after taking suprema.
The analytic kernel projection has constant diagonal \(\tau_G(p_A)\), and its compression fixes each vector of the finite kernel, giving \(\rho\le\tau_G(p_A)\).

A basis of the translates \(ct\) covers \(CT\), and a unit row minor of its lifts embeds a free module of rank at least \(|CT|/s\) in the modular kernel on \(D_eT\).
The resulting cardinality comparison gives (1).
Left Følner sets for the finitely many elements of \(H_e\) in the coset decomposition give the stated bound separately at each precision, including finite \(H_e\).
When \(L=1\), \(A\) is a signed group element.

Any finite complex left annihilator would yield a primitive integral one whose nonzero reduction contradicts \(ab=1\).
A finite complex right inverse would yield a rational two-sided inverse by descent and direct finiteness.
If \(p\) divides its least denominator, the integral numerator vanishes modulo \(p\) by multiplication on the right by \(b\).
Otherwise reduction gives a two-sided inverse of \(a\), contradicting \(ba\ne1\).
The augmented matrix for \(AB_e=1\bmod p^e\) has a nonzero minor divisible by \(p^e\) and of absolute value at most \(L^r\), even when the original columns have a rational dependence.
The geometric corrections telescope on the stated side, also at \(e=1\).
The review checked the protected nonzero \(c\), \(ab=1\), \(ac=0\) and the torsion-free group directly on [MD26 arXiv v1, p. 30](../../literature/pdf/MD26.pdf#page=30), accepting the geometric existence theorem at its stated scope.

For every lift \(B\), the congruence \(f=AB=1-pD\equiv1\bmod p\) rules out a nonzero finitely supported complex annihilator on either side by primitive integral descent.
Polar decomposition and range inclusion give \(\nu_G(f)\ge\nu_G(A)\), kernel inclusion gives \(\nu_G(f)\ge\nu_G(B)\), and the product of two injective operators is injective.
For \(H=\langle\operatorname{supp}D\rangle\), the blocks on right cosets \(Ht\) are copies of the regular action on \(H\), with the same kernel projection at the identity coordinate.
Positive nullity of \(A\) therefore forces \(0<\nu_H(f)<1\) and an actual eigenvalue \(1/p\) of \(D\).
Thom's theorem applies to the scalar integer convolution operator without a self-adjointness hypothesis, so one sofic subgroup supporting any representative \(D-AW\) suffices to exclude this possibility for the fixed \(A\).
The review checked the eigenvalue theorem in its original statement and accepted it as an external input. [Thom, arXiv v3, Theorems 1.1(i) and 4.2(i), pp. 1 and 6](https://arxiv.org/pdf/math/0701294#page=6).
The example distinguishing annihilator directions applies to suitable free product group algebras. [Handelman and Lawrence, Theorem 1, p. 453](https://doi.org/10.1017/S0004972700022887).

With \(F=AC_0/p\) and \(\partial X=DX-XD\), multiplying the recursion by \(A\) gives \(AZ_{j+1}=-p\partial(AZ_j)\), while reduction gives \(Z_j\bmod p=(-1)^j c\).
The finite-dimensional rational orbit span has finite total support and carries a full integral lattice preserved by \(\partial\).
Its monic characteristic polynomial gives \(AV=0\) and \(V\bmod p=(-1)^kc\), including the degree-zero choice when \(F=0\).
Thus the criterion yields an exact integral right annihilator, and a single rational dependence among the initial iterates suffices.
For the Mghirbi–Douglas witnesses the required coset compression and finite-dimensionality of the adjoint orbit remain unverified.
