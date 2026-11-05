---
author: Yin
---

# Almost-sure Brown limits for affine products of two finite-variance real Wigner matrices

<a id="statement"></a>
## Exact two-factor conclusion

Let \(W_1^{(N)},W_2^{(N)}\) be independent real Wigner matrices at each size, with the fixed centered variance-one off-diagonal laws and independent fixed finite-second-moment real diagonal laws in [the active Task](../tasks/Yin_T_F0012_v3.md#contract).
No independence between different sizes is required.
For fixed \(\alpha,\beta\in\mathbb C\) and a fixed one-variable complex polynomial \(g\), put
\[
 A_N=(W_1^{(N)}+\alpha I)(W_2^{(N)}+\beta I),
 \qquad a=(s_1+\alpha)(s_2+\beta).
\]
Then, on an event of probability one,
\[
 \mu_{g(A_N)}\Longrightarrow\mu_{g(a)}^{\mathrm{Br}}
 \quad\text{weakly on }\mathbb C.
\]
On that event convergence holds for every bounded continuous real test function.
The event may depend on the fixed laws, coupling, shifts and polynomial, as in the Task.
For every fixed \(z\in\mathbb C\), the unregularized normalized logarithmic determinants of \(A_N-zI\) also converge almost surely to the finite free logarithm.
The almost-sure event in this last fixed-parameter statement may depend on \(z\).
No expectation convergence of these unregularized logarithms is asserted.

This is a new nonnormal special case within the C_F0186 polynomial-convergence family.
The [reviewed controls and cyclic subclasses](Yin_C_F0186_v4.md#statement) remain separately valid at their broader complex-Hermitian input scope.
The present result does not assert general nonselfadjoint polynomial convergence or the same product theorem for every complex off-diagonal Wigner law.
The full Task remains unresolved.

<a id="inputs"></a>
## Exact project inputs

The finite-variance Hermitized weak limits, positive logarithmic tails, local planar potential bounds and Brown identification use [C_F0186_v4](Yin_C_F0186_v4.md#decision-finite-variance-reviewed).
The intermediate singular-value input is [C_F0187_v2](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed), used only on its real-input subcase and uniformly over independent complex shifts.
The small-value input is the exact [complex-symmetric shift statement](Yin_C_F0188_v1.md#statement), including independent finite-variance diagonals and normalized matrices.
That input is a candidate at this version's initial registration; this candidate may not be adopted unconditionally until the input's proof and applicable review are accepted.
The two inverse Littlewood--Offord theorems used by that input retain their stated external-proof boundary.

<a id="argument"></a>
## Proof from the stated inputs

### A fixed-parameter polynomial floor

Fix \(z\in\mathbb C\), and fix a desired failure exponent \(B>2\).
Write
\[
 T_N=W_2^{(N)}+\beta I.
\]
Apply the complex-symmetric shift theorem with the constant shift \(\beta I\).
It gives an exponent \(b_2\) such that
\[
 \mathbb P\{s_{\min}(T_N)<N^{-b_2}\}=O(N^{-B}).
 \tag{F1}
\]
On its complementary event, \(T_N\) is invertible and its inverse norm is at most \(N^{b_2}\).
Since \(T_N^T=T_N\), its inverse is complex symmetric.
The conditional shift
\[
 F_N=\alpha I-zT_N^{-1}
\]
is therefore complex symmetric, independent of \(W_1^{(N)}\), with entries bounded by \(N^{b_2+1}\) for all sufficiently large \(N\), after increasing the exponent if needed.
Define it to be zero off the good event when a globally defined random shift is needed.
Conditioning on \(T_N\) and using the uniform theorem gives some \(b_1\) with
\[
 \mathbb P\{s_{\min}(W_1^{(N)}+F_N)<N^{-b_1},
                  \ s_{\min}(T_N)\ge N^{-b_2}\}=O(N^{-B}).
 \tag{F2}
\]
The laws of the two independent matrices need not agree.
On the good invertibility event,
\[
 A_N-zI=(W_1^{(N)}+\alpha I-zT_N^{-1})T_N.
 \tag{Factor}
\]
The elementary inequality \(s_{\min}(UV)\ge s_{\min}(U)s_{\min}(V)\) yields
\[
 \mathbb P\{s_{\min}(A_N-zI)<N^{-b_z}\}=O(N^{-B}),
 \qquad b_z=b_1+b_2.
 \tag{Floor}
\]
This bound is summable, so the polynomial floor holds eventually almost surely under every cross-size coupling.

### Intermediate values and their product inequality

Write increasing singular values as \(a_r(M)=s_{N-r+1}(M)\), and set \(q_N=\lceil N^{3/4}\rceil\).
The intermediate theorem, first for \(T_N\), then conditionally for \(W_1+F_N\), gives on a common good event
\[
 a_r(T_N),\ a_r(W_1+F_N)\ge c(r-1)/N,
 \qquad q_N+1\le r\le N.
 \tag{Middle}
\]
The constant can be the smaller of the two constants for the two fixed laws.
The failure probabilities are at most \(CN^2e^{-cN^{1/4}}\), together with the probability in (F1), and are summable.
The intermediate bound has no norm condition on the conditional shift.

For any square matrices \(U,V\) and \(r+s-1\le N\),
\[
 a_{r+s-1}(UV)\ge a_r(U)a_s(V).
 \tag{Product}
\]
To prove this, choose subspaces on which \(U\) and \(V\) have norm lower bounds \(a_r(U)\) and \(a_s(V)\), of codimensions at most \(r-1\) and \(s-1\).
Intersect the latter with the inverse image under \(V\) of the former.
A linear inverse image does not increase codimension, so the intersection has codimension at most \(r+s-2\).
Both lower bounds hold successively there, and the singular-value min-max principle gives (Product).
This proof also allows singular matrices.

Take \(r=\lfloor(k+1)/2\rfloor\) and \(s=k-r+1\).
For \(k\ge2q_N+2\), both indices are at least \(q_N+1\), and (Factor)--(Product) give
\[
 a_k(A_N-zI)\ge c_1(k/N)^2.
 \tag{Product-middle}
\]
All estimates (Floor) and (Product-middle) hold eventually on one probability-one event for each fixed \(z\).

### Removing the negative logarithm

Fix a path in this event, and put \(k_N=2q_N+2\).
The lowest \(k_N\) singular values contribute at most
\[
 \frac1N\sum_{r\le k_N}(-\log a_r(A_N-zI))_+
 \le \frac{k_N}{N}b_z\log N\longrightarrow0.
 \tag{Bottom}
\]
For \(k_N<r\le\varepsilon N\), (Product-middle) gives
\[
 \frac1N\sum_{k_N<r\le\varepsilon N}(-\log a_r(A_N-zI))_+
 \le C\varepsilon+\frac2N\sum_{r\le\varepsilon N}\log(N/r).
\]
The limsup is at most \(C\varepsilon+2\varepsilon(1-\log\varepsilon)\), by the elementary Riemann-sum bound or the integral comparison for the decreasing function \(\log(1/t)\).
For each fixed \(\varepsilon>0\), all indices \(r\ge\varepsilon N\) have \(a_r\ge c_2\varepsilon^2\) eventually.
Thus choosing a singular-value cutoff below \(c_2\varepsilon^2\), then sending \(\varepsilon\downarrow0\), proves
\[
 \lim_{\delta\downarrow0}\limsup_N
 \frac1N\sum_{a_r(A_N-zI)<\delta}|\log a_r(A_N-zI)|=0
 \quad\text{almost surely}.
 \tag{Negative-UI}
\]
Exact zeros are absent eventually by (Floor).
No quantitative weak-convergence rate, higher moment or limiting-density estimate enters this argument.

### Potentials, one event and polynomial pushforward

The fixed-parameter Hermitized weak limit and positive logarithmic control in C_F0186_v4 apply to the scalar polynomial \((x+\alpha)(y+\beta)-z\).
Together with (Negative-UI), they yield
\[
 \frac1N\log|\det(A_N-zI)|\longrightarrow\tau\log|a-z|
 \quad\text{almost surely}.
\]
The free logarithm is finite: truncated logarithm convergence and the uniform negative-tail bound imply its negative integrability, while the bounded free operator controls its positive part.
This reasoning requires no assertion of expected unregularized logarithmic convergence, which can fail for discrete laws.

The potentials and their convergence events are measurable in the probability and planar variables.
For each fixed \(z\) the event has probability one, so Fubini on countably many disks gives a single event of planar almost-everywhere potential convergence.
The same polynomial's pathwise local \(L^2\) bounds from C_F0186_v4 give uniform integrability on every compact disk.
Hence convergence is in local planar \(L^1\) on that event.
The distributional Laplacian and the already proved tightness yield the required weak Brown-measure convergence for \(A_N\).
No cross-size independence was used at any stage.

Finally, finite-dimensional spectral mapping with algebraic multiplicity gives \(\mu_{g(A_N)}=g_*\mu_{A_N}\).
The [bounded FK factorization proof](Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction) establishes \(\mu_{g(a)}^{\mathrm{Br}}=g_*\mu_a^{\mathrm{Br}}\) for every bounded element \(a\) and one-variable polynomial \(g\).
A bounded continuous test composed with \(g\) remains bounded and continuous, so the weak limit passes to these pushforwards.
Constant \(g\) is immediate.

## Current assessment

[Selected decision](#decision-two-factor-candidate)

## Assessment history

### Decision two-factor-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:56 |
| status | open |
| reason | The complete two-factor deduction is fixed for review; unconditional adoption awaits acceptance of its complex-symmetric small-value input and review of this entire combination. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Affine two-factor conclusion](#statement) | Almost-sure logarithmic and Brown limits under finite second moments and arbitrary size coupling, including polynomial pushforwards. |
