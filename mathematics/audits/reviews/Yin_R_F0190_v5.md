---
author: Yin
---

# Conditional independent review of affine two-factor Brown limits

## Review arrangement and exact inputs

Review act: 2026-11-05T01:02.
Human record author: Yin.
This is a separately organized independent inspection of the whole local deduction in [C_F0186_v5](../../claims/Yin_C_F0186_v5.md#argument), against its [exact statement](../../claims/Yin_C_F0186_v5.md#statement) and the [finite-variance Task contract](../../tasks/Yin_T_F0012_v3.md#contract).
The reviewer did not participate in development of that deduction and received its fixed mathematical inputs, requested scope and current rules, without proof-generation discussion or development drafts.
The local findings below were formed before consulting earlier review conclusions.
The earlier reviews of the unchanged spectral controls and intermediate theorem were then read to identify the exact evidence reused.
The coordinating agent reported that the small-value input remained unresolved; its separate review and repair development were not read.
This review does not inspect or accept that input's complete proof.

The exact mathematical inputs are:

- [C_F0186_v4](../../claims/Yin_C_F0186_v4.md#argument), whose relevant statement and proof were read: Hermitized weak limits, positive logarithmic tails, eigenvalue tightness, local planar potential bounds, Brown identification and polynomial Brown mapping.
  Its [independent review](Yin_R_F0190_v4.md#finite-variance-controls) is reused at these unchanged scopes.
- [C_F0187_v2](../../claims/Yin_C_F0187_v2.md#statement), whose statement and proof were read: the real-input subcase of the intermediate singular-value bound, uniform over arbitrary independent complex shifts.
  Its [independent review](Yin_R_F0191_v2.md#complex-intermediate-bound-reviewed) is reused for the complete input theorem and its source boundary.
- [C_F0188_v1](../../claims/Yin_C_F0188_v1.md#statement), used only as an unresolved mathematical premise: the normalized real-Wigner least-singular-value estimate, uniformly over polynomially bounded complex symmetric shifts, including independent finite-second-moment diagonals.
  No proof acceptance for this premise is supplied or inferred here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conditional two-factor finding](#conditional-two-factor-deduction) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conditional two-factor finding](#conditional-two-factor-deduction) | [Exact two-factor statement](../../claims/Yin_C_F0186_v5.md#statement) | All stated conclusions follow conditionally on the exact unresolved C_F0188_v1 small-value assertion; this is not unconditional acceptance. |
| [Conditional two-factor finding](#conditional-two-factor-deduction) | [Whole local argument](../../claims/Yin_C_F0186_v5.md#argument) | Conditioning, product min-max bound, both negative logarithmic ranges, finite free logarithm, Fubini, local L1 convergence, Brown identification and polynomial pushforward. |
| [Conditional two-factor finding](#conditional-two-factor-deduction) | [Reviewed spectral and potential input](../../claims/Yin_C_F0186_v4.md#argument) | Applicability of the retained Hermitized, positive-tail, tightness, planar and bounded-FK mapping arguments; prior independent coverage is reused. |
| [Conditional two-factor finding](#conditional-two-factor-deduction) | [Reviewed intermediate input](../../claims/Yin_C_F0187_v2.md#statement) | Real Wigner matrices with independent real diagonals and shifts independent of the relevant Wigner matrix, with uniform constants and no shift norm restriction. |
| [Conditional two-factor finding](#conditional-two-factor-deduction) | [Unresolved small-value premise](../../claims/Yin_C_F0188_v1.md#statement) | Exact hypothesis and conclusion match at both uses, including normalization and random-shift conditioning; no audit or acceptance of its proof. |
| [Conditional two-factor finding](#conditional-two-factor-deduction) | [Task contract](../../tasks/Yin_T_F0012_v3.md#contract) | Quantifier comparison only: this two-real-factor subclass does not complete the general polynomial Task. |

<a id="conditional-two-factor-deduction"></a>
## Conditional finding

The whole local deduction is mathematically complete as an implication from the stated small-value assertion and the two reviewed inputs.
No additional local gap was found in C_F0186_v5.
Its unconditional statement remains unsupported while the required C_F0188_v1 premise is unresolved.
This finding therefore supplies conditional review evidence, not an unconditional proved assessment of C_F0186_v5 or completion of T_F0012_v3.

### Conditioning, normalization and the polynomial floor

Fix the laws, shifts and a planar parameter \(z\).
For \(T_N=W_2^{(N)}+\beta I\), the scalar complex shift is symmetric and satisfies any fixed positive polynomial entry bound for all sufficiently large \(N\).
The normalized form explicitly included in C_F0188_v1 supplies (F1) for any fixed failure exponent \(B>2\), including the Task's independent diagonal law.
On its good event, the inverse is complex symmetric because transposition commutes with inversion.
Every inverse entry has modulus at most its operator norm, so
\[
 \max_{i,j}|(\alpha I-zT_N^{-1})_{ij}|
 \le |\alpha|+|z|N^{b_2}
 \le N^{b_2+1}
\]
eventually, after a harmless fixed exponent enlargement if needed.
The threshold in \(N\) may depend on the fixed shifts and \(z\); the asserted conclusion allows this.

Define the shift to be zero off the good event.
It is then a measurable function of \(W_2\) alone, hence independent of \(W_1\), and it remains symmetric and polynomially bounded everywhere.
Conditioning on \(W_2\) preserves the full \(W_1\) law, including its diagonal independence.
Uniformity in the deterministic shift therefore yields (F2) after integration, without an assumption that the two off-diagonal or diagonal laws agree.

The multiplication order is correct:
\[
 (W_1^{(N)}+\alpha I-zT_N^{-1})T_N=A_N-zI.
\]
The least-singular-value product inequality gives the exponent \(b_1+b_2\) in (Floor).
Union bounds combine the two failures, and their summability gives an eventual floor by the first Borel--Cantelli lemma.
No independence across sizes is used.

### Intermediate values and the product min-max inequality

The translation between the decreasing notation of C_F0187_v2 and the increasing notation of this candidate is \(j=r-1\).
Its complete range \(q_N\le j\le N-1\) is exactly \(q_N+1\le r\le N\), where \(q_N=\lceil N^{3/4}\rceil\).
The theorem applies first to \(T_N\) and then conditionally to \(W_1+F_N\).
The second application needs neither symmetry nor a norm bound on \(F_N\), and its uniform constants survive conditioning.
The smaller lower-bound constant for the two fixed laws works simultaneously.
Its exponential failure bound and the failure of (F1) remain summable.

For arbitrary square \(U,V\), select a right-singular subspace \(E\) for \(U\) of codimension at most \(r-1\) and a right-singular subspace \(H\) for \(V\) of codimension at most \(s-1\), on which their respective lower bounds are \(a_r(U)\) and \(a_s(V)\).
The space \(H\cap V^{-1}E\) has codimension at most \(r+s-2\), because the map into the quotient by \(E\) has rank at most \(\operatorname{codim}E\).
For every vector \(x\) in this intersection,
\[
 \|UVx\|\ge a_r(U)\|Vx\|
 \ge a_r(U)a_s(V)\|x\|.
\]
The min-max principle gives \(a_{r+s-1}(UV)\ge a_r(U)a_s(V)\), in the direction used in (Product).
This argument is valid even when \(V\) is singular.

For \(r=\lfloor(k+1)/2\rfloor\) and \(s=k-r+1\), one has \(r+s-1=k\).
When \(k\ge2q_N+2\), both indices lie in the intermediate range and both \(r-1\) and \(s-1\) are bounded below by a fixed positive multiple of \(k\).
Consequently (Product-middle) follows with a fixed positive constant.
Only sufficiently large \(N\) matter, so the temporary possibility \(2q_N+2>N\) creates no endpoint problem.

### Negative logarithmic tails and the finite free logarithm

On the fixed-parameter probability-one event, every singular value is eventually at least \(N^{-b_z}\).
The lowest \(k_N=2q_N+2\) values thus contribute at most
\[
 \frac{k_N}{N}b_z\log N
 =O(N^{-1/4}\log N)\longrightarrow0.
\]
For \(k_N<r\le\varepsilon N\), the intermediate estimate gives
\[
 (-\log a_r)_+\le C+2\log(N/r).
\]
The normalized sum is bounded in the limit by
\[
 C\varepsilon+2\varepsilon(1-\log\varepsilon),
\]
which tends to zero with \(\varepsilon\).
For \(r\ge\varepsilon N\), the same lower bound keeps \(a_r\) above a fixed positive multiple of \(\varepsilon^2\), eventually.
Choosing the singular-value cutoff below that quantity and then sending \(\varepsilon\) to zero proves the displayed negative uniform integrability.
The floor also rules out exact zero singular values eventually.

The Hermitized weak convergence in C_F0186_v4 gives weak convergence of the singular-value measures after the continuous square-root map.
Negative logarithmic uniform integrability makes their eventual negative logarithmic integrals uniformly bounded.
Applying weak convergence to bounded continuous truncations of \((-\log s)_+\) and then monotone convergence shows that the limiting singular-value law has finite negative logarithmic integral, in particular no mass at zero.
The same truncation argument, using the vanishing tails, gives convergence of these negative logarithmic integrals.
The reviewed positive-tail control supplies the other half of the logarithm, and the bounded free operator has finite positive logarithmic part.
Thus the finite fixed-\(z\) limit is exactly \(\tau\log|a-z|\).
This argument establishes the stated pathwise convergence and does not assert convergence of expectations of unregularized logarithms.

### One event, planar convergence and polynomial mapping

The finite-size potentials are jointly measurable in the matrix randomness and \(z\); their extended value at a zero determinant causes no problem.
The deterministic free potential is measurable, and the event of convergence to it is expressed using countable limit conditions.
Since every fixed \(z\) has probability-one convergence, Tonelli/Fubini applied on each integer-radius disk gives one probability-one event of planar almost-everywhere convergence.
Uniform exponents or a common initial pointwise event for uncountably many \(z\) are not required.

Intersect this event with the reviewed pathwise control event of C_F0186_v4 for the fixed polynomial \(P(x,y)=(x+\alpha)(y+\beta)\).
The eventual uniform local \(L^2\) bound implies uniform integrability on every compact disk by Cauchy--Schwarz.
Almost-everywhere convergence therefore upgrades to local \(L^1\) convergence, and finitely many initial sizes do not affect that conclusion.
The distributional identity \(\Delta u_N=2\pi\mu_{A_N}\) passes to the limit against compactly supported smooth tests.
The Brown-potential identity identifies the limit, and the reviewed tightness upgrades this to weak convergence of probability measures on the same event.
Weak convergence on that event already includes every bounded continuous real test function; no uncountable intersection over tests is being taken.

At finite size, spectral mapping with algebraic multiplicity gives \(\mu_{g(A_N)}=g_*\mu_{A_N}\), including nonnormal matrices.
The bounded-FK factorization in C_F0186_v4 establishes the corresponding identity for the Brown measure of every bounded element \(a\), not only its cyclic subclass.
Its extended-real potential calculation allows zero determinants because the positive parts are bounded on the compact Brown support.
Thus its exact scope includes the present \(a=(s_1+\alpha)(s_2+\beta)\).
Composition of a bounded continuous test with \(g\) remains bounded and continuous, giving the claimed pushforward limit.
Constant \(g\) gives a fixed point mass directly.

## Source reuse and remaining limit

The source and prior-review reuse is explicit rather than a new audit of all external proofs.
R_F0190_v4 supplies the checked scope of Gui12 Section 2.3, Theorem 4, the ordinary bounded-differences input in War16 arXiv v1, and the retained bounded finite-tracial FK and Brown-potential interfaces.
R_F0191_v2 supplies the checked applicability of GNT14 arXiv v1, Theorem 3.7 and Corollary 3.8 on page 30, including its independent-coordinate formulation and the unchanged real-input case used here.
Those original source pages were not reopened in this review.
The new product inequality and the logarithmic deductions were checked from their displayed local proofs; the elementary min-max, Borel--Cantelli, Fubini and distributional identities are used at the interfaces explained above.

The exact two inverse Littlewood--Offord inputs identified by C_F0188_v1 remain within that unresolved premise's source and proof boundary.
This review supplies neither a proof of their adaptation nor a verdict on the separate small-value argument.
An accepted replacement small-value input would require checking its exact statement and applicability before this conditional evidence could support an unconditional two-factor decision.
The reviewed subclass uses two real Wigner inputs with fixed complex scalar shifts and one-variable polynomial pushforwards.
It makes no claim for arbitrary complex Hermitian entry laws, general nonselfadjoint polynomials, formal verification, expectation convergence of unregularized logarithms or completion of the full Task.
