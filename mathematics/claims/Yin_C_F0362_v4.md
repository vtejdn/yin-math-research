---
author: Yin
---

# Brown convergence for every fixed unequal-length word \(1+x^q y+yx\)

<a id="statement"></a>
## Original real laws with finite second moments

Fix an integer \(q\ge2\) and let \(X_N,Y_N\) be independent real symmetric Wigner matrices under the [fixed-law finite-second-moment contract](../tasks/Yin_T_F0012_v3.md#contract).
All strict upper entries are centered with variance one before division by \(\sqrt N\), the independent diagonal laws are centered with finite second moments, and all dimensions may be coupled arbitrarily.
Put \(P_q=1+x^q y+yx\), \(P_N=P_q(X_N,Y_N)\), \(p=P_q(s_1,s_2)\), and \(u(w)=\tau\log|p-w|\) at two free standard semicirculars.
Almost surely under each permitted coupling,
\[
 \frac1N\log|\det(P_N-\cdot I)|\longrightarrow u
          \quad\hbox{in }L^1_{\mathrm{loc}}(\mathbb C),
 \qquad \mu_{P_N}\Longrightarrow\mu_p^{\mathrm{Br}}.
\]
With \(h_N=\lceil\log(N+3)\log\log(N+3)\rceil\), ascending singular values and every \(R,\epsilon>0\),
\[
 \sum_{N>h_N}\Pr\left\{\frac1N\int_{|w|\le R}
       \sum_{j\le h_N}\log^-s_j(P_N-wI)\,dA(w)>\epsilon\right\}<\infty .
\]
The constants in the proof may depend on the fixed integer \(q\) and the input laws.
In particular \(1+x^3y+yx\) has this full-sequence Brown limit with only two real second moments.

For each fixed ordinary scalar polynomial \(g\in\mathbb C[t]\), the empirical eigenvalue measures of \(g(P_N)\) converge weakly almost surely to the Brown measure of \(g(p)\), and their ordinary potentials converge almost surely in local planar \(L^1\).
The parameter events in the [previous cubic result](Yin_C_F0362_v3.md#statement) keep their established scope.
The result here asserts planar limits for the entire fixed-\(q\) family; the kernel-stratum argument is not a fixed-shift determinant theorem for all \(q\).

<a id="argument"></a>
## Unequal borders supply the principal trims

Use the \((q+2)\)-channel affine companion and the two principal trims in [C367v1](Yin_C_F0367_v1.md#statement).
Its full left directional estimate is obtained by conditioning on \(X\) and viewing \(Y\mapsto XYu+YX^q u\) as a linear image of independent strict upper entries.
The covariance has a scalar polynomial part on two macroscopic spectral intervals of \(X\), a rank-four correction, and a diagonal removal with bounded normalized trace cost.
The resulting high-rank input projection gives exponential small-ball bounds from the original finite-variance law.
Nets over the thin spectral subspaces complete the left estimate.

On the right retain only the fresh channel indices \(0,q-1,q,q+1\).
A non-negligible leading direction forces the physical vector and its \(Y\)-image into at most \(q\) thin spectral slices of \(X\), which the independent-row test excludes.
For a small leading direction the remaining relation is an approximate \(Y\)-eigenvector equation.
At a prescribed nonreal parameter its scalar residual contradicts the real expectation of \(X^qY+YX\).

There are \(q+2\) useful columns on the left and four useful rows on the right.
The [rectangular singular-product inequality](Yin_C_F0366_v1.md#statement) gains \(q+6\) retained singular values on an extension with \(q+2\) new coordinates, so the deficit decreases by four.
No lower bound on the discarded right direction is required in this argument.
Iteration gives the full-size trim at \(h_N\), the near-full original principal trim at \(2h_n\), and the adjacent logarithmic bound, in precisely the physical normalization in C367v1.
The comparison uses actual original minors before exposing each new column; dependence of the two borders is handled by a union bound.

<a id="assembly"></a>
## Initial compression and the restored determinant

The [restoration theorem](Yin_C_F0363_v4.md#statement) applies to the same polynomial and the same two real laws.
Its initial exterior uses the columns of \(Y_{JI}\) and has scalar Schur complement \(Q^{\mathsf T}(P_q(X_{JJ},Y_{JJ})-w)Q\).
Thus it matches the original principal minors in C367v1.
For sufficiently large \(N\), off exceptional parameter sets with summable positive-area deviations, its undivided inequality bounds the full determinant below by
\[
 e^{-C_{q,R}(h_n^3+k)\log N}
 p_{n-2h_n}(P_q(X_{JJ},Y_{JJ})-wI)
 \min(1,t_{2h_n+1}(w))^{2h_n},
 \qquad k=2\lfloor\log^3(N+3)/2\rfloor .
\]
All three conditions (2) of that theorem are the established conclusions of C367v1.
Its conditional assembly therefore gives the ordinary local planar potential limit, the almost-sure weak Brown limit, and the normalized marginal deviation series stated here.
Every preceding assertion applies under each coupling, so the independent-size coupling can be used for the necessary marginal summability step.

For \(g(P_N)\) use the finite spectral mapping theorem and continuous mapping of probability measures.
Factor \(g(t)-w\) into scalar linear factors.
Multiplicativity of the FK determinant identifies its potential with the potential of the pushforward of \(\mu_p^{\mathrm{Br}}\), hence its Brown measure is that pushforward.
A constant \(g\) gives a point mass directly.
The [finite-variance positive logarithmic tails and planar criterion](Yin_C_F0186_v4.md#remaining-defect) applied to the fixed scalar polynomial \(g(P_q)\) give the additional local \(L^1\) convergence.

<a id="scope"></a>
## Conditions transferable to another cyclic realization

The argument uses three separately verifiable ingredients.

1. Initial principal trims come from directional bounds on selected incoming and outgoing channels.
   If a physical step adds \(p\) coordinates and the two selected volumes have sizes \(a,b\), a retained-product gain of \(a+b>p\) decreases the deficit by \(a+b-p\).
2. An exterior compatible with those principal minors gives the first undivided determinant comparison, with independent original columns and summable overlap errors.
3. The resolvent corner array modulo scalar functions admits joint node detectors whose matrices are invertible.
   This algebraic condition is used together with compact generic basis patches, nonzero free physical corners and their finite-Wigner transfer, the actual conditional product law of the panels, and the projected-output estimates of the [complete quotient argument](Yin_C_F0363_v4.md#quotient).
   That full hypothesis package turns a fixed number of restored directions into a summable bad-area probability.

The deterministic failure of the full right directional floor in the [quartic test](../ledger/Yin_L_F0069_v4.md#counterexample) persists.
The selected smaller right volume meets the strict gain condition and supplies the required proof.
For a general cyclic linearization, the existence of the three ingredients above remains to be verified.

## Current assessment
[Selected decision](#decision-fixed-power-reviewed)

## Assessment history

### Decision fixed-power-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T20:55 |
| status | open |
| reason | The unequal-volume trims supply the exact hypotheses of the joint-quotient restoration for every fixed power. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full planar convergence](#statement) | Original real two-moment laws, each fixed exponent and outer scalar polynomial. |
| argument | [Principal trim supply](#argument) | The unequal volumes reduce the deficit while retaining the original principal minors. |
| support | [Complete assembly](#assembly) | The exact conditional determinant comparison and its three supplied hypotheses. |
| support | [Transferable conditions](#scope) | Channel gain, compatible exterior and joint kernel detectors. |

### Decision fixed-power-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T20:57 |
| status | proved |
| reason | The reviewed unequal-border trims supply every hypothesis of the reviewed joint-quotient restoration, giving the full planar Brown limit and terminal series for each fixed power. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed unequal-length words](#statement) | Real independent Wigner laws with finite second moments, arbitrary coupling, and fixed outer scalar polynomial images. |
| argument | [Complete proof from the principal trims](#argument) | Compatible normalization and selected left and right channels. |
| support | [Ordinary scalar limit](#assembly) | The undivided comparison, planar passage and polynomial mapping. |
| review | [Independent whole-proof assessment](../audits/reviews/Yin_R_F0370_v4.md#fixed-power-whole-proof) | The exact theorem and all separately reviewed dependencies. |
