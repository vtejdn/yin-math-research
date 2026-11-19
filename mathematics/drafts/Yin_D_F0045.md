---
author: Yin
---

# Joint observations and arithmetic structure in a discrete Schur border

This continuing branch of [F0012](../tasks/Yin_T_F0012_v3.md#contract) asks whether the actual Schur-border coefficients admit a large joint least common denominator.
It complements the [matrix-evaluation and covariance tests](../ledger/Yin_L_F0070_v3.md#continuation).
The sufficient implication below is conditional; no required LCD estimate for a general Wigner polynomial has been proved.

<a id="cubic-physical-columns"></a>
## The actual columns in the commutator-cubic test

Use the [four-channel realization](../ledger/Yin_L_F0070_v4.md#cyclic) of \(P=[x,y]x\), and condition on the old principal blocks of both colors.
For one newly added site let \(a,b\) be its two independent normalized sign columns, each with covariance \(I/N\).
Write old-measurable frames of the tested left and right near-kernels as \(U=(U_1,U_2,U_3,U_4)^{\mathsf T}\) and \(V=(V_1,V_2,V_3,V_4)^{\mathsf T}\), with physical block rows.
The incoming and outgoing border maps are \(F=A\otimes a+B\otimes b\) and \(G=A\otimes a^{\mathsf T}+B\otimes b^{\mathsf T}\).
Their projected observations are exactly
\[
 U^*F=
 \bigl(U_4^*a,\ U_1^*a,\ -U_1^*b,\ U_3^*a+U_2^*b\bigr),
\]
and
\[
 GV=\begin{pmatrix}
 a^{\mathsf T}V_2-b^{\mathsf T}V_3\\
 b^{\mathsf T}V_4\\
 a^{\mathsf T}V_4\\
 a^{\mathsf T}V_1
 \end{pmatrix}.
\]
The common signs in these expressions must remain common throughout any covariance or small-ball calculation.
For a fixed proposed selection, stack the corresponding real and imaginary linear coefficients into a real matrix \(J(U,V)\).
The covariance of that stacked real observation is exactly \(N^{-1}J(U,V)J(U,V)^{\mathsf T}\).
Repeated observations or realification dependencies require an actual quotient or a smaller selection.

The [new invertible residue detector](../ledger/Yin_L_F0070_v4.md#schur) controls algebraic combinations of the ensuing resolvent kernels, not the least eigenvalue of this realized covariance.
The next quantitative test is to find exposure-compatible selected directions with the required volume gain and a lower bound on their nonzero covariance eigenvalues, outside summable original-law failures or a bad parameter set with summable positive-area deviations.
Only old-measurable spaces can be tested directly with the existing oversampling estimate.
After a new compression, establish the new measurability and independence before reusing it; the displayed formulas alone give neither that induction nor the initial principal trims.

## A conditional multi-panel estimate

First fix an old block.
Let \(F\) take values in \(\mathbb R^s\), have total polynomial degree at most a fixed \(d\ge2\), and depend on \(d\) actual independent panels of fair signs.
The old coefficients and target \(u\) are fixed in this conditioning.
Difference \(F\) between independent copies of each of the first \(d-1\) panels, leaving the last panel unchanged.
The resulting alternating sum is
\[
 \Delta F=A(\eta)\epsilon+b(\eta),
\]
where \(\eta\) contains all the exposed pairs and \(\epsilon\) is the last independent sign panel.
Every surviving monomial used at least one variable from each differenced panel, so it has degree at most one in the last panel.
Repeated Cauchy--Schwarz on the indicators of the original sublevel events gives
\[
 p^{2^{d-1}}\le
 \Pr\{\|A(\eta)\epsilon+b(\eta)\|_\infty\le2^{d-1}\delta\},
 \qquad p=\Pr\{\|F-u\|_\infty\le\delta\}.                 \tag{1}
\]
The target cancels after the first difference.

Suppose, outside an event of probability \(\eta_0\) in the paired panels,
\[
 AA^{\mathsf T}\succeq\lambda^2I_s,\qquad
 \operatorname{LCD}_{\alpha,\gamma}(\operatorname{ran}A^{\mathsf T})\ge D.
 \tag{2}
\]
Assume the last panel has more than \(s\) coordinates.
The LCD and concentration conventions are those in [RV09](../audits/literature/RV09/Yin_U001.md#concentration-and-lcd).
Whiten with \((AA^{\mathsf T})^{-1/2}\); the resulting matrix has orthonormal rows and identifies projection onto \(\operatorname{ran}A^{\mathsf T}\).
The infinity ball in (1) is contained in a Euclidean ball of radius \(2^{d-1}\sqrt{s}\delta/\lambda\) after whitening.
Increase the radius to meet the threshold in [Theorem 4.2](../audits/literature/RV09/Yin_U001.md#distance-to-subspace), and enclose closed events in a larger open ball.
For fixed \(s,d,\gamma\), (1) gives
\[
 p\le
 \left[C_{s,d,\gamma}(\delta/\lambda+D^{-1})^s+
       C_s e^{-c\alpha^2}+\eta_0\right]^{1/2^{d-1}}.       \tag{3}
\]
This uses the source only at its inspected statement and normalization scope.

For \(n^q\) tests, choose \(\lambda\ge n^{-a}\), \(D\ge n^L\), and \(\delta=n^{-a-L}\).
If the other two terms in (3) are \(O(n^{-H})\), the union is summable whenever
\[
              \min(Ls,H)>(q+1)2^{d-1}.                  \tag{4}
\]
Any exception already present in the old-block conditioning needs its own summable marginal bound.
Increasing the number of nodes does not establish (2); it can expose exact linear dependencies instead.
Likewise the degree \(d\) must remain fixed in this argument: substituting a growing restoration-block degree changes the decoupling exponent in (4).

## Actual missing input

At a symmetric Wigner border, condition on the old principal block before exposing the cross edges.
The second occurrence of an edge is the same sign; keep it in the polynomial before differencing.
A decoupled linear form with independent replacement coordinates is useful only if it arises by (1) from the actual original-law statistic.

The unproved interface is (2) for the joint coefficient matrix associated with a chosen finite set of spectral nodes and legal Schur observations, together with an exceptional probability strong enough for (4).
A coefficient-algebra detector supplies an algebraic direction but not a large LCD of its realized physical row space.
The [irreducible sign example](../ledger/Yin_L_F0070_v3.md#density-obstructions) and the [projected-area cancellation](../ledger/Yin_L_F0069_v2.md#sign-obstruction) prevent replacing this obligation by a coefficient Gram or Frobenius energy statement.

Before attempting a new arithmetic theorem, test whether the [existing oversampled subspace estimate](../claims/Yin_C_F0196_v5.md#restricted-small-ball) fits the actual exposure.
When it does, only its joint transverse covariance and subsequent volume comparison need new work.
If it does not, identify a specific realization and coefficient row space in (2), and search for its arithmetic obstruction before allocating a general inverse Littlewood--Offord argument.

The inequality (3) was developed by a research delegate and checked in the main-agent assembly on 19 November 2026.
It is retained as a conditional research calculation, without independent review or adoption of an original-law small-singular-value theorem.
