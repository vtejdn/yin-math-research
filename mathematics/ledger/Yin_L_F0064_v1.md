---
author: Yin
---

# Alternative Schur pivots and phase anti-concentration boundaries for Haar pencils

These method comparisons were developed for Yin on 2026-11-05 in the fixed-coefficient Haar affine model of [F0015](../tasks/Yin_T_F0015_v1.md#contract).
They retain an alternative determinant reduction and useful quantitative failure boundaries, without duplicating the [full reviewed Haar proof](../claims/Yin_C_F0192_v2.md#argument) or the [reviewed complementary-corner proof](../claims/Yin_C_F0193_v2.md#argument).
The comparisons and source reading are ordinary mathematical development, not an independent review or a public-priority assessment.
The original determinant contract is settled internally by [C_F0192_v2](../claims/Yin_C_F0192_v2.md#statement); the restrictions below describe particular methods rather than remaining gaps in that statement.

<a id="offdiagonal-pivot"></a>
## An off-diagonal pivot bypasses singular one-input backgrounds

Consider
\[
 M_N=\begin{pmatrix}I_N+aU_N&bV_N\\cU_N&I_N+dV_N\end{pmatrix},
 \qquad e=ad-bc,
\]
where \(U_N,V_N\) are independent full Haar matrices within each dimension, the scalar coefficients are fixed, and \(b\ne0\).
Suppose that \(B(z)=d+ez\) has no zero on the unit circle, and put \(A(z)=1+az\), \(R=A/B\).
Assume the modulus law of \(R\) is nonconstant and
\[
 \int_{\mathbb T}|R|^2\,dm>1,
 \qquad \int_{\mathbb T}|R|^{-2}\,dm>1,
\]
allowing the second integral to be infinite.
The ratio \(R\) is bounded because \(B\) is bounded away from zero, but \(R\) is not required to be invertible.
The corresponding determinant conclusion is already covered by [the complementary-corner theorem and its exact ratio matching](../claims/Yin_C_F0193_v2.md#explicit-corner-example).
The following different pivot retains a direct explanation of why neither \(I_N+aU_N\) nor \(I_N+dV_N\) needs an inverse.

Swap the two block columns of \(M_N\), and set \(T_N=I_N+aU_N\), \(S_N=I_N+dV_N\).
The upper-left pivot is now \(bV_N\), which is uniformly boundedly invertible without any condition on \(a\) or \(d\).
Its Schur complement is
\[
 H_N=cU_N-S_N(bV_N)^{-1}T_N.
\]
Because \(S_N\) commutes with \(V_N\),
\[
 bV_NH_N=bcV_NU_N-S_NT_N=-Q_N',
 \qquad Q_N'=I_N+aU_N+dV_N+eV_NU_N.
\]
The finite determinant magnitudes therefore satisfy \(|\det M_N|=|\det Q_N'|\).
The same bounded Schur factorization, the unitary column swap, and [bounded ordinary FK multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) give
\[
 2\log\Delta_{\operatorname{tr}_2\otimes\tau}(M)
 =\log\Delta_\tau(Q')
\]
freely, with no inverse of \(T\), \(S\) or the Schur factor \(H\) used.
Indeed both sides equal \(\log|b|+\log\Delta(H)\), including a possible extended value \(-\infty\).
Now
\[
 Q_N'=A(U_N)+V_NB(U_N)
      =\bigl(R(U_N)+V_N\bigr)B(U_N),
\]
and the free identity has the same order.
The [physical conditional Haar-additive theorem](../claims/Yin_C_F0193_v1.md#conditional-haar-additive-statement), with the strict bulk matching retained in the [complementary-corner proof](../claims/Yin_C_F0193_v2.md#argument), treats \(R(U_N)+V_N\).
The \(B(U_N)\) factor has a bounded continuous logarithmic test, giving the original two-by-two normalized limit with factor \(1/2\), both finitely and freely.
Free-target identification uses the actual joint Haar polynomial and bounded rational expressions; it does not substitute \(|R(u)|\) for \(R(u)\) inside the pencil.

The explicit choice \(a=d=b=1\), \(c=1/2\) gives
\[
 M_N=\begin{pmatrix}I_N+U_N&V_N\\\tfrac12U_N&I_N+V_N\end{pmatrix},
 \qquad R(z)=\frac{1+z}{1+z/2}.
\]
Its moments, positive FK determinant, lack of a bounded free inverse, and failure of both full-background inverse guards are proved at [C_F0193_v2's explicit example](../claims/Yin_C_F0193_v2.md#explicit-corner-example).
The alternative unitary pivot above supplies the same determinant normalization without requiring either failed background inverse.

<a id="physical-haar-boundary"></a>
## The physical Haar-additive method has its own boundary

The [first rank-one Schur class](../claims/Yin_C_F0193_v1.md#affine-schur-statement) requires a boundedly invertible full background and a boundedly invertible scalar compression.
The [complementary-corner class](../claims/Yin_C_F0193_v2.md#statement) weakens this to a boundedly invertible complementary corner and permits a noninvertible scalar deformation.
Its conditional local-law input still needs an eventual deterministic deformation-norm guard and strict regular bulk.
If a scalar compression is inverted without a bounded free inverse, that norm guard is not supplied by bounded rational approximation.
For a rank-\(k\) auxiliary coefficient, rectangular Schur compression leaves a repeated matrix \(I_k\otimes V_N\), rather than Haar measure on the full \(U(kN)\).
The inspected physical Haar-additive theorem does not apply merely by replacing \(N\) by \(kN\).
At equality in either strict bulk moment test, the positive imaginary subordination values used for a fixed weak neighborhood need not remain positive.
Approximating such coefficients by strict-bulk coefficients does not alone justify exchanging that approximation with an unregularized determinant limit.
These explain why a direct extrapolation of that analytic route failed, while the [different unitary-repair, Cayley-tube and logarithmic argument](../claims/Yin_C_F0192_v2.md#argument) proves the original full coefficient statement.

<a id="rank-one-phase"></a>
## Rank-one phase degree does not supply a tube estimate by itself

For fixed \(A_0,\ldots,A_r\in M_m(\mathbb C)\), put
\[
 F_N(U)=\det\left(A_0\otimes I_N+\sum_jA_j\otimes U_j\right).
\]
Its ambient complex-entry degree is at most \(mN\).
For a fixed unit vector \(v\in\mathbb C^N\), replace one input by
\[
 U_j(\theta)=U_j\exp(i\theta vv^*)
 =U_j+(e^{i\theta}-1)U_jvv^*.
\]
The induced change of the pencil has rank at most \(\operatorname{rank}A_j\le m\).
Multilinearity of the determinant in its columns therefore makes the restricted \(F_N\) a polynomial in \(e^{i\theta}\) of degree at most \(\operatorname{rank}A_j\).
This remains true when the determinant at the initial tuple is zero.
It gives no quantitative coefficient lower bound for that one-variable polynomial.

The low phase degree does not by itself bound the probability of an intrinsic zero-set tube or supply dimension-uniform value anti-concentration.
For example, intersection counts with regular levels of \(|F_N|^2\) would first control a hypersurface measure.
Converting that information into a tube-volume estimate still requires control of parallel levels, higher curvature or singular strata; no such conversion was established by this phase-slicing attempt.
The [proved Cayley-chart tube argument](../claims/Yin_C_F0192_v2.md#haar-tube-argument) instead applies the actual coefficient-uniform Euclidean tube theorem to a nonzero coordinate polynomial and then averages exact Haar translates.
Its small-radius estimate and metric conventions are retained at the [fixed tube statement](../claims/Yin_C_F0192_v2.md#haar-tube-statement).
No determinant-value normalization enters that proof.

<a id="fgz-value-bound"></a>
## The inspected Haar value bound loses the exponential determinant scale

On 2026-11-05, the bounded primary-source search for Haar log-determinant variance and single-ring fixed-parameter bounds inspected Fefferman, Ghosh and Zhan, *Anti-Concentration for the Unitary Haar Measure and Applications to Random Quantum Circuits*, ITCS 2026, Theorem 6 and Remark 8.
The exact published original is retained as [FGZ26--ITCS.pdf](../literature/pdf/FGZ26--ITCS.pdf), with its [edition and source-scope note](../audits/literature/FGZ26/readme.md).
Both statements occur on printed p. 57:6, one-based PDF p. 6, and agree with the previously inspected publisher HTML Section 1.2.
This is statement and applicability inspection for the comparison below; the full anti-concentration proof and the quantum-circuit applications were not independently audited.
The source bound is accepted as an established external result at this exact single-Haar polynomial statement, rather than as a determinant-limit theorem.

For \(U\) Haar on \(U(n)\) and a degree-\(d\) polynomial \(F\) in the entries of \(U,U^*\), restrict to the nondegenerate normalization \(\mathbb E|F(U,U^*)|^2>0\).
This condition is needed for the intended use: the literal source display does not state it, but if the squared L2 norm vanished then its non-strict sublevel event would have probability one for every positive \(\varepsilon\).
No such identically-zero-on-the-group application is accepted here.
On the positive-normalization domain used in this comparison, the source inequality is
\[
 \mathbb P\{|F(U,U^*)|^2\le\varepsilon\,\mathbb E|F(U,U^*)|^2\}
 \le C'(n,d)\varepsilon^{C(n,d)},
 \qquad \varepsilon>0.
\]
Remark 8 gives the proved choices
\[
 C(n,d)=\frac1{4n^2d},
 \qquad C'(n,d)=O(n^3d).
\]
For a nonzero degree-\(mN\) determinant polynomial at size \(n=N\), the exponent is \(1/(4mN^3)\).
At an exponential normalized squared-value cutoff \(\varepsilon=e^{-cN}\), its power factor becomes
\[
 \varepsilon^{1/(4mN^3)}=\exp\left(-\frac{c}{4mN^2}\right),
\]
which tends to one, while the displayed prefactor is only bounded by \(O(mN^4)\).
Thus the bound does not force the probability to zero at this determinant scale and does not by this direct invocation supply aggregate negative-logarithm control.
The calculation is a limitation of that proved quantitative bound in this application, rather than a refutation of other uses of Haar polynomial anti-concentration or of a possible sharper exponent.
It already concerns one Haar input and assumes no unproved product-Haar extension.
A normalized determinant-value inequality and an intrinsic zero-set tube inequality have different hypotheses and conclusions; the former's \(\mathbb E|F|^2\) normalization must also be matched before using it for a singular-value statement.
The rank-one physical additive route and the general Cayley-tube route bypass this particular value-bound loss by controlling singular values through different mechanisms.
