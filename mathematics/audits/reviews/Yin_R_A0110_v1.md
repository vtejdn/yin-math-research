---
author: Yin
---

# Review of signed returns for a kernel projection supported on the whole group

At 2026-11-17T03:50 UTC an agent outside the development of Yin_C_A0074_v1 independently checked the fixed statement, both proof sections and the exact interfaces below for Sheng Yin.
The reviewer had previously reviewed other projection-decay results in this task, including C58, and had received no development outline, draft proof or earlier verdict on C74.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0074_v1.md#statement) | Group and metric, row and nullity, independent shifts, failure of the finite tests, both phases, all three bounds and the narrower unsigned divergence assertion. |
| [Whole-argument finding](#whole-argument-finding) | [Resolvent and product fibers](../../claims/Yin_C_A0074_v1.md#resolvent-of-the-original-product-fibers) | Exact polar decomposition on the row space, signed coefficients, positive heat-kernel majorant, positive identity coefficient and the full subgroup forced by the translated input. |
| [Whole-argument finding](#whole-argument-finding) | [Signed limits and spatial tails](../../claims/Yin_C_A0074_v1.md#taking-the-signed-time-sum-at-its-endpoint) | Orientation of the signed time difference, positive denominators, finite-time error uniform in the endpoint, and strict weighted square-tail exponent. |
| [Whole-argument finding](#whole-argument-finding) | [Trace sublevel comparison](../../claims/Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group) | Order on positive operators in the finite trace algebra and the cyclic shift spectral distribution. |
| [Whole-argument finding](#whole-argument-finding) | [Definition of the signed means](../../claims/Yin_C_A0067_v1.md#argument) | First-return generating series, finite first means, stationary padding, both polarized coefficients and endpointwise convergence. |
| [Whole-argument finding](#whole-argument-finding) | [Closed-range criterion](../../claims/Yin_C_A0067_v1.md#two-stronger-tests-characterize-closed-range) | Exact Abel identity and divergence of the timewise absolute test for nonclosed range on good four-line groups at \(\beta>3\). |
| [Whole-argument finding](#whole-argument-finding) | [Finite-power test](../../claims/Yin_C_A0069_v1.md#statement) | Its sufficient finite-support conclusion for each positive integer power, constant unitary and \(M>\|A\|^2\). |
| [Whole-argument finding](#whole-argument-finding) | [Extended statement](../../claims/Yin_C_A0074_v1.md#statement) | Single real \(00\) coordinate, divergence of the smaller temporal sign mass on every exterior for \(\beta>3\), and unbounded ratios for the stated exponential rates. |
| [Whole-argument finding](#whole-argument-finding) | [Cancellation in the single coordinate](../../claims/Yin_C_A0074_v1.md#cancellation-in-the-single-coordinate-with-nonzero-residual-at-every-endpoint) | Uniform operator-norm lower bound in that corner, reality, coefficientwise domination, divergence and the positive denominator at all nonidentity endpoints. |
| [Whole-argument finding](#whole-argument-finding) | [Rapid-decay shell estimate](../../claims/Yin_C_A0057_v1.md#interchanging-the-scales-forces-a-spectral-gap) | Operator-norm approximation by finite balls from a uniform weighted square bound, extended to square-summable Fourier series by truncation on a good four-line group. |

## Whole-argument finding

Surjectivity of \(T\) gives \(\operatorname{im}A=\operatorname{im}a\).
On the right cosets of the infinite cyclic subgroup \(\langle u\rangle\), the left regular action of \(a\) has circle symbol \((1-e^{it})^d\).
This has zero set of measure zero and essential infimum of its modulus zero, so \(a\) is injective with dense nonclosed range.
The coisometry \(V=(TT^*)^{-1/2}T\) identifies the complement of the kernel with one copy of the regular space, giving the unnormalized trace \(h\) for the kernel.
The ordering \(aa^*\le AA^*\le(1+4h)aa^*\) and the cyclic distribution give the needed sublevel bound with exponent \(1/(2d)\).
Both \(aS^{1/2}\) and its adjoint are injective, so polar equivalence carries this bound to \(C\), including the absence of a zero atom.
The normalized real resolvent acts as the identity on the kernel and as the conjugate of \(\lambda(\lambda+C)^{-1}\) on its complement.
Summation over dyadic sublevels bounds the positive remainder's trace by \(O(\lambda^{1/(2d)})\), since \(1/(2d)<1\).
Every individual entry at every pair of endpoint vectors is bounded in absolute value by that trace by positivity, Cauchy–Schwarz and invariance of the diagonal under right translation.
For \(z\ge1/2\), \(\lambda\le2M(1-z)\), yielding the asserted uniform additive error before the fixed-endpoint limit.

The strictly contractive convolution expansion of \(S^{-1}\) has nonnegative probabilities, with \(L(g)>0\) for every \(g\) because the walk generates the group.
At \(g\ne e\) the \(00\) entry of the projection is exactly \(-L(g)\).
At \(e\) it is the trace of the nonzero positive operator \(I-S^{-1}\), which is strictly positive by faithfulness and \(TT^*\ne I\).
Thus an individual entry already has full group support and retains that support under left and right shifts, contradicting the finite-support conclusion of each admissible C69 test.
For the input row, the first entry has nonzero coefficients at both \(e\) and \(u\), including \(d=1\).
For \(s_j\notin\langle u\rangle\), the two right cosets \(\langle u\rangle,\langle u\rangle s_j\) are disjoint, leaving nonzero coefficients at \(e\) and \(s_j\).
For each entry a common right translation cancels from its within-entry left differences, and the row's sole left translation conjugates all of them uniformly.
The subgroup forced by those differences is therefore the whole \(G\), including the possibility that some generators already belong to \(\langle u\rangle\).
This input assertion concerns the subgroup required to contain the translated supports of a finite matrix.

The signed limit has numerator \(\operatorname{Re}(\zeta\widehat p(g)_{ij})\) and denominators tending to the two padded masses of the unit root, each in \([1/2,1]\).
Indeed the total masses of the first-return series both equal one, and division of their difference by \(1-z\) yields the mean of the minus series minus the mean of the plus series in the limit.
The two finite first moments justify this calculation at each endpoint.
Thus the coefficientwise majorant \(E_{ij}\) gives the factor four for either phase, and the real \(00\) component yields the lower bound \(L(g)\) despite its negative Fourier sign.
The walk's unit propagation gives an exponentially weighted \(\ell^1\) bound on \(L\) for every \(0\le\sigma<\log(1/\theta)\), inherited by its finitely shifted majorants.
Squaring yields the \(2\sigma\) weighted \(\ell^2\) bound, and the positive margin \(2\sigma-c\) absorbs any fixed polynomial weight on the exterior.
This summation applies to the limiting coefficients after their endpointwise limits.
The timewise absolute divergence uses only the stronger C67 criterion on a good four-line group with \(\beta>3\).
It does not follow by summing the spatially uniform finite-time error.
The full statement and both proof sections pass at the fixed scopes above.

At 2026-11-17T03:59 UTC the same reviewer independently checked the extension of the statement and the new third proof section.
Since the first entry of \(T\) is \(I\), the \(00\) entry of \(R_z-p\) equals \(S^{-1/2}\lambda(\lambda+C)^{-1}S^{-1/2}\).
The positive operator \(C=D^*D\) has zero in its spectrum by the dense nonclosed range and injectivity of \(D\).
Thus \(\|\lambda(\lambda+C)^{-1}\|=1\) for each \(\lambda>0\), and the norm of the displayed corner is at least \(1/\|S\|\) by multiplication on both sides by \(S^{1/2}\).
The coefficients in that corner and in \(p_{00}\) are real because the original row, the real-parameter resolvent and the kernel projection commute with coefficient conjugation.
All coefficients of the remainder tend to zero individually by its positive trace bound.

For the one real probe pair at a fixed \(g\ne e\), subtraction at \(z=1\) bounds the absolute Abel contrast by \(V_g=\sum_n n|f_n^--f_n^+|\).
The product of the padded denominators is at most one, so \(V_g\) dominates the entire real \(00\) coefficient of \(R_z\) at \(g\).
The identity coefficient is bounded independently.
If \(V\) belonged to weighted \(\ell^2\) with \(\beta>3\), the rapid-decay estimate on dyadic shells would give a spatial operator-norm error tending uniformly to zero for the truncations of this corner.
The estimate for finitely supported coefficients extends by truncation and trace \(\ell^2\) identification, and the limiting \(p_{00}\) has the same spatial control by its Green coefficient bound.
Together with coefficient convergence on finite balls this would contradict the corner norm lower bound.
Each \(V_g\) is finite by the two finite first moments, so deleting any finite ball preserves divergence of its weighted square norm.
The signed sum \(d_1=U_g^+-U_g^-\) has finite weighted square norm, while \(V_g=U_g^++U_g^-\).
The identity \(2\min(U_g^+,U_g^-)=V_g-|d_1|\) therefore gives the claimed divergence even for the smaller sign mass, without making any assertion of divergence at an individual endpoint.
For \(0<\eta<\log(1/\theta)\) the earlier Green bound gives a finite weighted square norm for \(e^{\eta |g|}d_1\), by choosing a strictly larger allowed exponential rate.
Since \(|d_1|\ge L(g)>0\) off the identity, boundedness of the stated ratios on any exterior would contradict the divergence just proved.
The extended statement and its new proof section pass at the indicated good-four-line scope.
