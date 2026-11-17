---
author: Yin
---

# A finite return moment for a kernel without finite flows

At 2026-11-17T02:55 UTC an agent outside the development of C64 reviewed its fixed statement and all three proof sections for Sheng Yin.
The reviewer had developed C62, which C64 invokes only to deduce the schedule threshold after establishing the positive spectral exponent and the spatial decay of this particular kernel.
The reviewer checked that application at its stated scope, using the [existing independent finding on C62](Yin_R_A0098_v1.md#whole-argument-finding).
The reviewer read C64, the relevant C59 and C62 interfaces, and their review scopes, without seeing C64 development dialogue, preliminary arguments or an earlier finding on C64.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [C64 statement](../../claims/Yin_C_A0064_v1.md#statement) | Group hypotheses, nonclosed range, dimension and absence of finite kernel vectors, support under translations, one-moment tail bound and spectral exponent. |
| [Whole-argument finding](#whole-argument-finding) | [C64 row and kernel](../../claims/Yin_C_A0064_v1.md#the-row-map-and-its-kernel) | Tree orientation, Gram bounds and constants, range of the power and finite-flow argument. |
| [Whole-argument finding](#whole-argument-finding) | [C64 subgroup recovery](../../claims/Yin_C_A0064_v1.md#recovering-the-generating-polynomial-from-the-projection) | Coordinate map, lack of a bounded inverse, signed right-inverse equation and recovery by a bounded strong limit under independent row and column translations. |
| [Whole-argument finding](#whole-argument-finding) | [C64 moment estimate](../../claims/Yin_C_A0064_v1.md#a-tail-estimate-from-one-finite-moment) | Polar decomposition, exact trace error, propagation and shell bounds, exponential weight, positive singular measure and schedule threshold. |
| [Whole-argument finding](#whole-argument-finding) | [C59 free letters](../../claims/Yin_C_A0059_v1.md#statement) | Scope of the freely generating pair on individual realizations of the specified event and its stated intersection with the finite-quotient exclusion. |
| [Whole-argument finding](#whole-argument-finding) | [C62 schedule criterion](../../claims/Yin_C_A0062_v1.md#statement) | Applicability of its established two-sided power-law criterion with exponent \(1/(2d)\) and finite spatial moment to the specific C64 matrix. |

## Whole-argument finding

Left translation by \(u,v\) preserves each right coset of their free subgroup.
For each unoriented edge of the four-regular tree the adjacency form has two conjugate terms.
Orienting toward an end gives one parent and three children, so the weighted two-term inequality contributes a total of \(3/\sqrt 3+\sqrt 3=2\sqrt3\) at each vertex.
This gives \(DD^*\ge(4-2\sqrt3)I\).
The right inverse first solves for the pair of flow coordinates and then adds \(Vb\) to the first target.
Its norm is bounded by \(1+2/\sqrt\gamma\), using \(\|V\|\le1\).
The sum of the squared norms of the two row maps is at most ten, so \(cI\le TT^*\le10I\) with the stated \(c\).
Left multiplication of the second row by \((1-u)^d\) preserves the kernel and gives precisely the claimed range since \(T\) is onto and \(u\) has infinite order.
Surjectivity gives nullity one.
Each finite pair of flow coefficients determines finitely many oriented edges, with divergence \(b(g)-b(u^{-1}g)+h(g)-h(v^{-1}g)\) at \(g\).
A nonempty finite forest has a leaf, where the nonzero incident coefficient cannot cancel.
Thus the Hilbert kernel has no nonzero finitely supported vector.

The second-coordinate map \(E\) on the kernel is injective by the first row and the injectivity of \(1-v\).
Its polar isometry has initial dimension one and hence final projection the entire one-dimensional target module by faithfulness.
This proves that \(EE^*=p_{22}\) is injective.
If it were bounded below, the bounded right inverse of \(E\) would give \(1-u=(1-v)L\) by taking for \(L\) the *negative* of its third coordinate.
Then \(DD^*\le(1+\|L\|^2)(1-v)(1-v)^*\), contradicting the positive lower bound on \(DD^*\) along approximate invariant vectors for the cyclic shift.

The identity coefficient of the nonzero positive \(p_{22}\) is strictly positive.
It puts \(g_2h_2\) in the putative subgroup, and therefore the conjugated \(C=h_2^{-1}p_{22}h_2\) is in its von Neumann algebra.
The first row gives \(p_{12}=Vp_{22}\), so the translated data also give \(ZC\) there for \(Z=g_1Vh_2\).
Functional calculus gives \(C(C+\varepsilon I)^{-1}\to I\) strongly since \(C\) is injective.
Multiplication on the left by the bounded \(Z\) thus recovers \(Z\) in the subgroup von Neumann algebra.
The support of \(Z\) forces the subgroup to contain \(h_2^{-1}s h_2\) for every generator \(s\).
The input entry \(-V\) already gives this support test before considering the kernel.
These arguments use independent left row and right column translations.
They require a finite generating support with the identity, and the analytic arguments require an actual free pair.
In the probabilistic application C59 supplies that pair on its stated event, including the indicated further restricted family. [Independent review of C59](Yin_R_A0095_v1.md#whole-argument-finding)

The polar factor \(U\) is a coisometry, so finite geometric summation gives \(p^{(k)}-p=U^*H^kU\).
Cyclicity of the unnormalized rectangular matrix traces and \(UU^*=I_2\) give squared trace-\(L^2\) error \(\tau_2(H^{2k})\).
This equals two at \(k=0\), as required for the initial approximation \(I_3\).
For \(k\ge1\), the longest summand has propagation \(w+2(k-1)w+w=2kw\).
On the strict exterior of that radius the coefficient mass of the projection is therefore bounded by the same trace error.
The Gram bounds with \(M=16\) give \(0\le H\le(1-c/16)I\).
Summing over the successive shells with their outer endpoint weights yields (1), and replacing the polynomial weight by the exponential one gives exactly the ratio \(e^{2aw}\theta^2\).
Computing \(t_k\) uses the true group endpoints of each half product before squaring; the four-line application concerns fixed groups where these product equalities are meaningful.

Finally the Gram congruence uses normality of \(1-u\) to identify its power times its adjoint with \(|1-u|^{2d}\).
The circle spectral measure gives positive mass comparable to \(t^{1/(2d)}\) below \(t\).
Trace comparison for spectral sublevels transfers this exponent across the two Gram bounds, and the rectangular polar decomposition transfers the positive mass to the column Gram matrix.
The exponential shell estimate supplies every polynomial spatial moment required by C62.
Its geometric schedule criterion consequently gives exactly \(\kappa>2d\beta\), with divergence at equality.
The proof supports the whole C64 statement at the indicated scopes.
