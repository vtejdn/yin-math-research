---
author: Yin
---
# Independent whole-argument review of the global filter obstruction and local kernel criteria

Date of review: 2026-11-12T13:57.
Human record author: Yin.

## Review arrangement and scope

This is a separately organized initial whole-argument review of [C14 v3](../../claims/Yin_C_A0014_v3.md#statement).
The reviewing agent did not participate in its substantive proof development and received the fixed statement, argument, requested scope, necessary fixed mathematical dependencies and administrative authorization.
No exploration drafts, proof-generation conversation, proposing-agent mathematical summary, previous R findings or prior verdict about v3 were supplied or consulted before the initial findings.
The existing C1 v2 and C14 v2 dependency materials were read directly; their assessment sections were visible, but no earlier review conclusion was used to establish the new assertions.
The reviewer formed the mathematical findings from the fixed inputs and then checked the saved clarification of equation (13) to the ambient operator norm.
That clarification changes no hypothesis, estimate or proof step, and this reviewer supplied no substantive proof repair.

The scope is every assertion in v3's Statement, Argument and What has and has not been reduced, including the converse implications, positive-time quantifiers, constants, finite-set bounds and limitations.
The dependencies below are checked only at the interfaces actually invoked.
This is not a new whole-proof audit of C1 v2 or C14 v2, an audit of the original assembly or interpolation proofs, or completion of the all-group and all-matrix Task.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-v3 finding](#whole-argument) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-v3 finding](#whole-argument) | [C14 v3 statement](../../claims/Yin_C_A0014_v3.md#statement) | Every stated implication, constant, quantifier and finite-window identity, including equation (13) in the ambient operator norm. |
| [Whole-v3 finding](#whole-argument) | [C14 v3 argument](../../claims/Yin_C_A0014_v3.md#argument) | Complete Banach-spectral, positive-time, local-kernel and projection-norm arguments under their stated hypotheses. |
| [Whole-v3 finding](#whole-argument) | [C14 v3 scope](../../claims/Yin_C_A0014_v3.md#what-has-and-has-not-been-reduced) | Route obstructions and equivalent conditional criterion, with no unconditional correlation estimate or new group-class coverage. |
| [Whole-v3 finding](#whole-argument) | [SW20 definitions](../literature/SW20/Yin_U001.md#spectral-definitions) | Finite-support self-adjoint real-spectrum definition of quasi-Hermitianity for every discrete group. |
| [Whole-v3 finding](#whole-argument) | [SW20 spectral invariance](../literature/SW20/Yin_U001.md#finite-support-spectral-invariance) | Theorem 4.7(iv) for finite-support elements; no inverse-closedness assertion for all of the Banach algebra is adopted. |
| [Whole-v3 finding](#whole-argument) | [SW20 structural consequence](../literature/SW20/Yin_U001.md#elementary-amenable-growth) | Corollary 4.11 applied to finitely generated elementary amenable groups of exponential growth. |
| [Whole-v3 finding](#whole-argument) | [C1 v2 localization](../../claims/Yin_C_A0001_v2.md#rational-kernel-localization) | Equation (2) at the scalar group-ring specialization, with one column and no auxiliary state, giving boundary coefficient one. |
| [Whole-v3 finding](#whole-argument) | [C1 v2 localization argument](../../claims/Yin_C_A0001_v2.md#proof-of-complete-rational-kernel-localization) | Identification of its finite-set kernel estimate and upper dimension bound at the scalar finite-propagation interface; no new affiliated-algebra extension is invoked. |
| [Whole-v3 finding](#whole-argument) | [C14 v2 bounded mass](../../claims/Yin_C_A0014_v2.md#bounded-coefficient-mass-suffices-without-norm-convergence) | Bounded subsequence of coefficient mass together with L2 convergence implies that the limiting kernel projection belongs to the Banach group algebra. |
| [Whole-v3 finding](#whole-argument) | [C14 v2 coefficient-limit proof](../../claims/Yin_C_A0014_v2.md#variational-identities-and-spatial-convergence) | Finite coefficient sums, their bounded limit and faithful regular identification; no Christoffel or rate assertion is needed here. |
| [Whole-v3 finding](#whole-argument) | [BCM04 Banach idempotent interface](../literature/BCM04/Yin_U001.md#amenable-projective-trace) | Integral Kaplansky trace on K0 of the Banach group algebra for torsion-free amenable groups, applied only to the scalar projection p. |
| [Whole-v3 finding](#whole-argument) | [BCM04 reduced-algebra trace](../literature/BCM04/Yin_U001.md#assembly-trace) | Theorem 6.3 and the torsion-free integral trace range, combined with the separately identified assembly surjectivity. |
| [Whole-v3 finding](#whole-argument) | [HK97 assembly surjectivity](../literature/HK97/Yin_U001.md#amenable-assembly) | Corollary 1.3 for countable amenable discrete groups; finite generation supplies countability in v3. |

## Verified obligations

### Global heat and Euler bounds

Under quasi-Hermitianity, SW20 gives spectral equality for the particular finite-support positive element \(H\).
For an invertible regular input, its spectrum lies in \([\delta,M]\) for some \(\delta>0\), so polynomial and entire spectral mapping give radii at most \(1-\delta/M<1\) and \(e^{-\delta}<1\), respectively.
The Banach spectral-radius formula gives an exponential norm bound after enlarging a constant to cover finitely many initial powers.
This includes the endpoint \(\delta=M\).
Writing \(t=n+s\), with \(0\le s<1\), and using the uniform bound \(e^{\|H\|_A}\) for the remaining short-time factor supplies exponential decay at every real time, not merely at integer times.

For the converse, a nonreal spectral point \(r+iy\) of a self-adjoint finite-support \(x\) is exactly what failure of the stated definition supplies.
For every \(0<\varepsilon<|y|\), the shifted element \(a=x-r-i\varepsilon\) is regularly invertible, while its square \(H=(x-r)^2+\varepsilon^2\) has the Banach spectral point \(-c\), with \(c=y^2-\varepsilon^2>0\).
The same spectral mapping gives the precise lower bounds \(e^{ct}\) and \((1+c/M)^n\).
Here \(M\ge\varepsilon^2>0\), so the normalization and the strict exponential growth factors are valid.
In the regular representation the spectrum is instead contained in \([\varepsilon^2,M]\), yielding exponential decay.
Thus either proposed bounded-subsequence condition, when imposed on all regularly invertible finite-support inputs, implies quasi-Hermitianity.

The resolvent exclusion is also valid.
If \(c(H+c)^{-1}\) belonged to \(A\), its division by \(c\) would be a two-sided inverse of \(H+c\) in \(A\), because the regular representation is faithful.
This contradicts \(0\in\sigma_A(H+c)\).
SW20's elementary amenable corollary applies with the usual word-growth meaning in the finitely generated case.
It establishes the claimed structural obstruction without asserting a zero divisor or a failure of Atiyah integrality.

### Positive random times

The closed unital algebra generated by \(H\) is commutative, and its spectrum contains the spectrum computed in \(A\).
Consequently the point \(-c\) has a norm-one character evaluating \(H\) to \(-c\).
The assumed Bochner integral remains in that closed algebra, and a continuous character commutes with its integral.
Its value is the nonnegative exponential moment \(\int e^{ct}\,d\nu_j(t)\), which is finite whenever the stated Bochner integral exists and is bounded above by \(\|u_j\|_A\).

The suppression hypothesis at just one \(x_0>0\) gives
\[
\nu_j([0,R])\le e^{x_0R}f_j(x_0)\longrightarrow0
\]
for every fixed \(R\).
The resulting lower bound \(e^{cR}\nu_j((R,\infty))\), followed first by the limit in \(j\) and then by arbitrary \(R\), proves divergence of the whole sequence.
No uniform-in-\(R\) exchange of limits is required.
The argument includes finite positive mixtures and Bochner Cesaro averages but requires exactly the integral existence stated in the claim.

For a nonzero positive regular \(H\), faithfulness gives positive spectral mass \(1-\alpha>0\).
Since every normalized positive-time Laplace transform equals one at zero and decreases on the positive real axis, L2 convergence to the kernel projection bounds \((1-\alpha)f_j(M)^2\) by the squared L2 error.
This proves the claimed automatic suppression premise.
An analytically continued rational resolvent need not be such an \(A\)-valued integral and is correctly excluded.

### The finite-window average and its normalization

Expanding \(\xi_i\xi_i^*\) gives the coefficient at \(g\) as \(\sum_x\xi_i(gx)\overline{\xi_i(x)}\).
Summing over the orthonormal basis identifies the entries \(Q_F(gx,x)\), proving basis independence, the coefficient formula and support in \(FF^{-1}\).
The convolution product is essential and is not confused with the rank-one matrix on \(\mathbb C[F]\).
Each summand is positive, and \(a\xi_i=0\) gives \(ab_F=0\).

For each fixed \(z\), Bessel's inequality bounds the sum of the squared quantities \(\sum_{h\in F}\overline{\xi_i(h)}\eta(hz)\) by \(\sum_{h\in F}|\eta(hz)|^2\).
After summation over \(z\), every \(h\) contributes \(\|\eta\|_2^2\).
Thus the divisor \(|F|\) gives exactly \(b_F\le I\), with no extra dimension factor.
The range inclusion and self-adjointness give \(pb_F=b_Fp=b_F\), hence \(0\le b_F\le p\).
The identity coefficient of each summand is one, so \(\tau(b_F)=k_F/|F|\).

The contraction \(p-b_F\) has square bounded above by itself, proving the squared L2 estimate with coefficient one.
For the last inequality, the scalar group-ring case of C1 v2 uses one input column and no auxiliary state.
Its propagation boundary is precisely \(\{x\in F:B_wx\not\subset F\}\), giving
\[
0\le\alpha-k_F/|F|\le|\partial_wF|/|F|.
\]
The use requires neither an affiliated inverse nor a spectral gap.
A left Følner sequence makes this boundary ratio tend to zero, so the asserted L2 convergence follows.

### Correlations, equivalence and the operator norm obstruction

The triangle inequality after grouping by \(g=yx^{-1}\) proves \(\mathcal C_F\le\mathcal D_F\).
There are \(|F|^2\) matrix entries, so Cauchy--Schwarz cancels exactly the factor \(|F|^{-1}\).
The Hilbert--Schmidt square of the projection matrix is its rank \(k_F\), yielding \(\mathcal D_F\le\sqrt{k_F}\).
This includes \(k_F=0\).

A bounded subsequence of \(\mathcal C_{F_j}=\|b_{F_j}\|_A\), together with the established L2 limit, puts every finite sum of absolute Fourier coefficients of \(p\) under one common bound.
The resulting element of \(A\) has the same regular operator as \(p\).
BCM04's integer trace consequence and \(0\le\tau(p)=\alpha<1\) force \(p=0\).
The \(\mathcal D\) implication follows from \(\mathcal C\le\mathcal D\); the converse follows because an injective input has \(K_F=0\) for every finite \(F\).
For nonnegative sequences, failure to tend to infinity would give a bounded subsequence.
This proves both the equivalence and the stated full divergence conclusion when \(p\ne0\).

Since \(k_F\le|F|\), the available estimate is already of order at most \(\sqrt{|F|}\).
Merely asking for an unspecified sublinear upper bound therefore gives no additional criterion.
Injective inputs have identically zero local correlations regardless of a continuous spectral endpoint or the global Banach-spectral obstruction.
No new bound for a hypothetical nonzero kernel is proved or silently assumed.

Finally, if \(0<\alpha<1\) and \(\|p-b_F\|_{B(\ell^2(G))}<1\), positivity in the corner gives \(b_F\ge\varepsilon p\) for some \(\varepsilon>0\).
Thus its positive spectrum is separated from zero and its support projection is exactly \(p\).
Continuous functional calculus for \(b_F\in C_r^*(G)\) then puts \(p\) in that reduced algebra.
Finite generation gives countability, so the cited HK97 surjectivity and BCM04 trace-range theorem apply and exclude such a scalar projection.
The upper bound one follows from \(0\le p-b_F\le p\), proving the exact ambient norm equality for every finite nonempty \(F\).

## Source scope and remaining limits

SW20, BCM04 and HK97 are used as established published inputs at the exact statements and applicability scopes retained in their U records.
Those records identify the inspected editions and passages and disclose that the substantial interpolation, group-structure and assembly proofs were not audited end to end.
This review checks their use without enlarging that proof-inspection scope.
In particular, the Banach-algebra idempotent result and the reduced-algebra scalar projection result are separate inputs; neither is obtained by assuming that \(A\) is inverse closed in \(C\).

The ordinary Banach spectral mapping and character facts, Bessel's inequality, finite-dimensional Cauchy--Schwarz, trace faithfulness and continuous functional calculus are used at their standard stated settings.
No computational experiment, numerical test or formal proof-assistant verification is used.
The source identification and hypothesis matching needed by the actual invoked specialized results are accounted for; this is not a historical novelty search.

## Whole argument

The complete fixed v3 statement and argument are mathematically supported under their explicit hypotheses, including the exact positive-time and finite-window bounds and the operator norm limitation.
No substantive gap remains in the inspected scope.
The conclusion supports the global obstruction and the equivalent local correlation criterion, while preserving the unresolved task of deriving a sufficient uniform correlation bound from the group hypotheses.
It proves neither the general torsion-free amenable domain conclusion nor the full [Atiyah Task](../../tasks/Yin_T_A0001_v1.md#contract).
