---
author: Yin
---

# Almost-sure Brown limits from conditional complex symmetric Wigner shifts

<a id="statement"></a>
## Exact polynomial classes and conclusion

Use independent real Wigner inputs with the fixed centered variance-one off-diagonal laws, independent fixed finite-second-moment real diagonal laws, and arbitrary cross-size couplings of [the active Task](../tasks/Yin_T_F0012_v3.md#contract).
<a id="word-reversal"></a>
Definition (word reversal).
For a scalar noncommutative polynomial, let \(\operatorname{rev}\) reverse every word without conjugating its complex coefficient.
Thus \(Q(X)^T=Q(X)\) for real symmetric tuples whenever \(\operatorname{rev}Q=Q\).
Consider either of the following fixed polynomial classes:
\[
 R(x)=x_1+Q(x_2,\ldots,x_d),\qquad \operatorname{rev}Q=Q,
 \tag{Single}
\]
or, for \(d\ge2\),
\[
 R(x)=\bigl(x_1+Q_1(x_2,\ldots,x_d)\bigr)
       \bigl(x_2+Q_2(x_3,\ldots,x_d)\bigr),
 \qquad \operatorname{rev}Q_1=Q_1,\quad\operatorname{rev}Q_2=Q_2.
 \tag{Two}
\]
Polynomials in an empty variable set are arbitrary complex constants.
Put \(A_N=R(W^{(N)})\) and \(a=R(s)\).
For every fixed one-variable complex polynomial \(g\), on an event of probability one,
\[
 \mu_{g(A_N)}\Longrightarrow\mu_{g(a)}^{\mathrm{Br}}
 \quad\text{weakly on }\mathbb C.
\]
On that event convergence holds for every bounded continuous real test function.
The event may depend on the fixed laws, coupling and polynomials, as in the Task.
For every fixed \(z\in\mathbb C\), the unregularized normalized logarithmic determinant of \(A_N-zI\) also converges almost surely to its finite free logarithm; this event may depend on \(z\).
No expectation convergence of unregularized logarithms is asserted.

These classes include all scalar complex linear combinations of real Wigner inputs and their one-variable polynomial images, \(x_1+i x_2^k\), and every affine product \((x_1+\alpha)(x_2+\beta)\).
A nonzero leading complex scalar is absorbed by rescaling \(Q\) and the outer polynomial \(g\).
In (Two), \(Q_1\) may depend on \(x_2\); the factors need not be independent.
The [reviewed controls and cyclic subclasses](Yin_C_F0186_v4.md#statement) remain separately valid at their broader complex-Hermitian input scope.
The full Task for arbitrary nonselfadjoint polynomials remains unresolved.

<a id="inputs"></a>
## Exact project inputs

The finite-variance Hermitized weak limits, positive logarithmic tails, local planar potential bounds and Brown identification use [C_F0186_v4](Yin_C_F0186_v4.md#decision-finite-variance-reviewed).
The intermediate singular-value input is [C_F0187_v2](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed), used only on its real-input subcase and uniformly over independent complex shifts.
The small-value input is the exact [complex-symmetric shift statement](Yin_C_F0188_v2.md#statement), including independent finite-variance diagonals and normalized matrices.
The [selected small-value decision](Yin_C_F0188_v2.md#decision-complex-shift-reviewed) adopts its exact repaired proof and independent review.
The two inverse Littlewood--Offord theorems used by that input retain their stated external-proof boundary.

<a id="argument"></a>
## Proof from the stated inputs

### Polynomial norm events from second moments

For every fixed scalar polynomial \(Q\) and every prescribed \(B>0\), some \(M>0\) satisfies
\[
 \mathbb P\{\|Q(W)\|>N^M\}=O(N^{-B}).
 \tag{Norm}
\]
Indeed, for degree \(D\ge1\), the expected singular counting bound (Tail) of C_F0186_v4 gives
\[
 \mathbb P\{\|Q(W)\|>t\}
 \le N\,\mathbb E\mu_{|Q(W)|}((t,\infty))\le C_QNt^{-2/D}.
\]
Choose \(M\) sufficiently large; constant polynomials are immediate.
No almost-sure bounded operator norm or entry moment above two is used.

### Conditional polynomial floors

Fix \(z\in\mathbb C\) and a desired failure exponent \(B>2\).
For (Single), condition on all inputs except \(W_1\).
The shift \(Q(W_2,\ldots,W_d)-zI\) is complex symmetric and independent of \(W_1\).
On the norm event (Norm) it has a fixed polynomial entry bound, so the uniform complex-symmetric shift theorem gives a polynomial least-singular-value floor for \(A_N-zI\), with failure \(O(N^{-B})\).
The omitted norm event has the same prescribed polynomial failure bound.

For (Two), put
\[
 U_N=W_1+Q_1(W_2,\ldots,W_d),\qquad
 T_N=W_2+Q_2(W_3,\ldots,W_d),\qquad A_N=U_NT_N.
\]
Conditioning first on \(W_3,\ldots,W_d\), the same theorem and (Norm) give an exponent \(b_2\) with
\[
 \mathbb P\{s_{\min}(T_N)<N^{-b_2}\}=O(N^{-B}).
 \tag{F1}
\]
On its complementary event, \(T_N\) is invertible with inverse norm at most \(N^{b_2}\).
Both \(T_N\) and its inverse are complex symmetric.
Condition now on all inputs except \(W_1\).
The shift
\[
 F_N=Q_1(W_2,\ldots,W_d)-zT_N^{-1}
\]
is complex symmetric and independent of \(W_1\).
The good event for \(T_N\) and a polynomial norm event for \(Q_1\) give a fixed polynomial bound on its entries.
Define the shift to be zero off that intersection if a globally bounded random shift is needed.
The conditional theorem therefore gives some \(b_1\) with
\[
 \mathbb P\{s_{\min}(W_1+F_N)<N^{-b_1},
       \text{ both preceding good events hold}\}=O(N^{-B}).
 \tag{F2}
\]
Dependence of \(Q_1\) on \(W_2\) is harmless, since only \(W_1\) is still exposed.
The two off-diagonal laws need not agree.
On the good events,
\[
 A_N-zI=(W_1+F_N)T_N.
 \tag{Factor}
\]
Combining \(s_{\min}(UV)\ge s_{\min}(U)s_{\min}(V)\) with these estimates proves, for either class and a suitable \(b_z\),
\[
 \mathbb P\{s_{\min}(A_N-zI)<N^{-b_z}\}=O(N^{-B}).
 \tag{Floor}
\]
The bound is summable, so the floor holds eventually almost surely under every cross-size coupling.

### Intermediate values and their product inequality

Write increasing singular values as \(a_r(M)=s_{N-r+1}(M)\), and set \(q_N=\lceil N^{3/4}\rceil\).
For (Two), apply the intermediate theorem conditionally on \(W_3,\ldots,W_d\) to \(T_N\), and conditionally on \(W_2,\ldots,W_d\) to \(W_1+F_N\).
On a common good event it gives
\[
 a_r(T_N),\ a_r(W_1+F_N)\ge c(r-1)/N,
 \qquad q_N+1\le r\le N.
 \tag{Middle}
\]
The constant can be the smaller of the two constants for the two fixed laws.
The failure probabilities are at most \(CN^2e^{-cN^{1/4}}\), together with the probabilities of the preceding good-event complements, and are summable.
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
For (Single), condition on all other inputs and apply the same intermediate theorem directly to \(A_N-zI\).
It gives the stronger lower bound \(a_k\ge c(k-1)/N\), and hence also (Product-middle) for \(k\ge2q_N+2\).
Thus (Floor) and (Product-middle) hold eventually on one probability-one event for each fixed \(z\), for either class.

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

The fixed-parameter Hermitized weak limit and positive logarithmic control in C_F0186_v4 apply to the fixed scalar polynomial \(R-z\).
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
[Selected decision](#decision-conditional-shift-classes-reviewed)

## Assessment history

### Decision conditional-shift-classes-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T01:08 |
| status | open |
| reason | The deduction now includes polynomial complex symmetric conditional shifts and dependent two-factor products with the stated variable order. It awaits whole-chain review and acceptance of the repaired small-value input. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conditional-shift polynomial classes](#statement) | The two displayed classes, one-variable polynomial images, fixed-parameter logarithms and arbitrary-coupling almost-sure Brown convergence. |

### Decision conditional-shift-classes-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T01:16 |
| status | proved |
| reason | Independent review covers the complete broadened deduction, and the repaired small-value input now has its own fresh independent whole-proof acceptance. The exact single-factor and dependent two-factor classes are established under finite second moments; the general Task is not completed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact polynomial classes](#statement) | Both displayed classes, polynomial images, fixed-parameter finite logarithmic limits and arbitrary-coupling almost-sure Brown convergence. |
| argument | [Complete argument](#argument) | Polynomial norm events, successive conditioning, floors, intermediate values, logarithmic UI and the one-event planar passage. |
| dependency | [Finite-variance controls](Yin_C_F0186_v4.md#argument) | Hermitized weak convergence, positive tails, planar potential control, tightness and Brown polynomial mapping. |
| dependency | [Intermediate singular values](Yin_C_F0187_v2.md#statement) | Uniform real-input specialization for the independent conditional shifts. |
| dependency | [Complex symmetric small values](Yin_C_F0188_v2.md#statement) | The accepted repaired theorem, including normalization and independent diagonal laws. |
| review | [Independent complete-chain finding](../audits/reviews/Yin_R_F0190_v6.md#polynomial-shift-classes) | Exact v6 statement and argument and applicability of all accepted dependencies, with prior-review reuse and source limits disclosed. |

