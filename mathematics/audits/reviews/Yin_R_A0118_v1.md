---
author: Yin
---

# Review of signed shell estimates from collected row products in a free subgroup

At 2026-11-17T04:33 UTC an agent outside the development of Yin_C_A0082_v1 independently checked the fixed statement, all three proof sections and their directly used inputs for Sheng Yin.
The reviewer had independently reviewed the subgroup projection estimate C58 and the shell approximation C76, and had received no draft, development outline or earlier verdict on C82.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0082_v1.md#statement) | Collected row-product condition, powers and projection, ambient spatial decay, integral trace, dyadic bounds and the input-dependent polynomial exponent in the signed shell estimate. |
| [Whole-argument finding](#whole-argument-finding) | [Coset expansion](../../claims/Yin_C_A0082_v1.md#collecting-equal-endpoints-before-applying-a-subgroup-estimate) | Right cosets for left convolution, cancellation in \(E_K(AA^*)\), rectangular matrices, strong limits, shifts and the stage at which the original probes are used. |
| [Whole-argument finding](#whole-argument-finding) | [Spectral and temporal bounds](../../claims/Yin_C_A0082_v1.md#positive-spectral-mass-and-the-finite-first-return-arrays) | Positive spectral measures, treatment of the zero atom, the free Haar Puiseux bound, dyadic traces and the squared error on the exterior. |
| [Whole-argument finding](#whole-argument-finding) | [Walsh example](../../claims/Yin_C_A0082_v1.md#a-row-whose-off-subgroup-products-cancel) | Existence and padding of the difference-generating set, cancellation in the row Gram, nonclosed range and the subgroup required by the translated projection entries. |
| [Whole-argument finding](#whole-argument-finding) | [Free-subgroup kernel projections](../../claims/Yin_C_A0058_v1.md#argument) | Dimension for the square row Gram and exponential localization for the rectangular subgroup matrix, with ambient word length as in the following section of that claim. |
| [Whole-argument finding](#whole-argument-finding) | [Free Haar matrix-polynomial algebraicity](../literature/SS15/Yin_U001.md#matrix-algebraicity-and-puiseux) | Selfadjoint matrix polynomials, the actual Cauchy branch, general zero atom and passage from a normalized probability law to the unnormalized matrix trace. |
| [Whole-argument finding](#whole-argument-finding) | [Signed means](../../claims/Yin_C_A0067_v1.md#statement) | Bounds in both phases for the limiting signed array. |
| [Whole-argument finding](#whole-argument-finding) | [Shell approximation](../../claims/Yin_C_A0076_v1.md#passing-from-finite-returns-to-a-spatial-shell) | Finite-shell approximation under the scalar dyadic hypothesis. |
| [Whole-argument finding](#whole-argument-finding) | [Free marked subgroups](../../claims/Yin_C_A0059_v1.md#statement) | Availability of a free marked pair on the specified realizations. |
| [Whole-argument finding](#whole-argument-finding) | [Finite-power criterion](../../claims/Yin_C_A0069_v1.md#statement) | Finite-support consequence contradicted by the example. |

## Whole-argument finding

Two support terms in a column belong to the same right coset \(Kx\) precisely when their left difference belongs to \(K\).
Thus the within-coset terms give \(FF^*\), and the conditional expectation removes the remaining terms even when \(K\) is not normal.
The hypothesis on the fully collected row Gram identifies the result with \(AA^*\).
The map \(J\) copies and translates coordinates and need not be an isometry.
The proof uses the identity \(A^*(AA^*)^{l-1}A=J^*(F^*F)^lJ\) only for \(l\ge1\), which explains the subtraction from the identity in both transfer formulas and includes zero input columns.
Norm-convergent Abel sums and strong spectral limits preserve those formulas since \(J\) is bounded and fixed.
The original first-return coefficients are then formed from the transferred input moments and original probes.
No linearity of the nonlinear renewal recursion was assumed.
The subgroup-to-ambient regular representation and finitely many fixed translations preserve exponential weighted square summability, possibly with a changed constant or exponent.
The polar trace calculation is \(m-(r-\dim_K\ker FF^*)\), using the unnormalized trace on each matrix size and its invariance under subgroup inclusion.
The zero matrix and trivial subgroup reduce to finite-dimensional constant-matrix calculations.

The nonzero spectral measure transfers by polar equivalence of \(A^*A\) and \(AA^*\), then by equality with the subgroup row Gram and its normalized scaling.
For a nontrivial free group, its free basis gives free Haar unitaries and \(FF^*/M\) is a selfadjoint polynomial matrix in them and their adjoints.
The retained [SS15, Theorem 1.1(5)–(6), PDF p. 2](../../literature/pdf/SS15--arxiv-v1.pdf#page=2) supplies the algebraic Cauchy transform and its analytic or Puiseux expansion at zero for the normalized law.
Multiplying by the matrix size changes no exponent.
On the negative real ray \(s>0\) gives \(h(s)=-sG_\mu(-s)\to\mu(\{0\})\).
The finite limit excludes negative powers and identifies the constant coefficient after that multiplication.
The first remaining nonzero power has positive exponent, which one may decrease below one if necessary.
The lower bound \(s/(t+s)\ge1/2\) on \(0<t\le s\) now gives the stated bound on the positive sublevel mass.
This establishes the conclusion independently of the separate citation to Sauer.
The indexed text of Sauer's Theorem 3.6(i) also states the positive rational or gap alternative for selfadjoint matrices over a complex subfield group ring of a virtually free group.
I inspected that theorem statement, and did not independently audit its proof. [Sauer, published chapter](https://doi.org/10.1142/9789812704443_0020)
Integration against the positive measure after subtracting the kernel mass bounds \(\tau_m(Q^n-p)\) by \(O(n^{-\alpha})\) and hence its nonnegative dyadic differences by \(O(2^{-\alpha j})\).
C67 bounds the limiting signed means by bounded multiples of the polarized projection entries, while C76 bounds the squared weighted exterior error by \(O(R^{-(\kappa\alpha-\beta)})\).
The polynomial spatial weight can be absorbed in a smaller exponential rate for the true projection.
The triangle inequality followed by squaring proves (1).
Choosing \(\kappa\) to meet a desired decay power changes the finite time horizon on each shell and does not give a polynomial operation count for enumerating the entire shell.

For the example, the required two free marked generators exist on the C59 event, and their subgroup is proper since an entire free group would have a characteristic-two group ring without zero divisors.
After replacing a possible \(u^{\pm1}\) by \(u^2,u^5\), the differences within the pairs \(v^k,sv^k\) give a generating list and cannot make a \(u\)-adjacency inside such a pair.
For each old list entry there are only finitely many forbidden \(k\) for coincidence or \(u\)-adjacency, by the infinite order of \(v\).
Repetitions for Walsh padding affect neither the positive support of the first row nor the identity \(\sum_j w_jw_j^*=I\), which follows from orthogonality on the list indices.
In particular \(w_1w_1^*\) has positive coefficients at differences outside \(K\).
Multiplication by the injective factors \(a,a^*\) cannot annihilate its whole off-\(K\) part, and these factors preserve the off-\(K\) support on the corresponding side.
Cancellation in the sum of the column products is genuine.
The initial onto row has \(TT^*=I+bb^*\), giving the claimed dense nonclosed range after multiplication by \(1-u\).
The positive diagonal projection entry \(S^{-1}\) has support all of \(\langle v\rangle\), and its translated left differences force \(gvg^{-1}\) into any subgroup supporting every shifted entry.
The multiplier \(C=-gb^*S^{-1}g^{-1}\) belongs to that subgroup algebra's von Neumann closure and is injective by the infinite-order shift.
The independently right-translated off-diagonal entry supplies \(CZ\); its left multiplier is the same \(g\) because the two inspected entries share their row.
Functional calculus gives \((C^*C+\epsilon)^{-1}C^*CZ\to Z\) strongly, so the translated \(w_1\) also lies in that closure.
Its support differences generate \(gGg^{-1}=G\), whatever right multiplier was chosen.
Hence both the input and the actual infinite-support projection require the full group after the permitted coordinate shifts, and C69's finite-support consequence fails for every admissible test on this example.
The algebraic transfer survives replacement of \(K\) by an arbitrary subgroup, while the general spectral, integrality and decay conclusions use the free-subgroup inputs.
All three proof sections and the fixed statement pass at those scopes.
