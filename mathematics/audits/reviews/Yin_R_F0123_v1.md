---
author: Yin
---

# Yin_T_F0008: Positive Certificates and the Circular Signed Schur Minimum

Date: 2026-09-13.
Reviewer: the reviewing agent.
This is a complete internal mathematical review of the two modules identified below, at their stated scopes.
Both pass.
No Claim ID, mathematical Role, priority assertion or goal-completion decision is assigned by this review.

- [Positive-certificate reformulation](../../ledger/Yin_L_F0031_v1.md)
- [Circular signed Schur minimum](../../ledger/Yin_L_F0032_v1.md)

The reviewer did not write either module.
Earlier collaboration included adversarial candidate discussion and development of a paired-matrix reformulation from the root's certificate parameterization.
This is disclosed prior involvement; the review independently reconstructs the root's proof, but does not claim independent discovery.
The reviewer's own [paired-matrix exploration](../../ledger/Yin_L_F0028_v1.md) is excluded from certification here.
The circular author's disclosed preliminary algebra review by another agent is separate from the complete reconstruction below.

## 1. Results and dependency boundaries

| Module | Verified result | Limits |
| --- | --- | --- |
| Positive certificates | The strict Hilbert--Schmidt domain of Yin_C_F0124 is in bijection with all positive matrices; the determinant formula, ordered quadratic maximum and complete centered capacity reduction survive the substitution. | The general determinant equality is a reformulation of Yin_C_F0124, whose [existing independent review](Yin_R_F0124_v1.md) is retained. It is not a second proof of that equality. |
| Circular signed Schur minimum | For every positive regularization, arbitrary affine matrix-valued circular noise admits a global minimum over every positive matrix, with the stated unique optimizer. The ordered Schur formula and the centered zero-capacity limit hold. | The proof is independent of Spe26/Yin_C_F0124. Its vanishing off-diagonal covariance is essential to the formula inspected. Arbitrary complex semicircular coefficients with nonzero pseudo-covariance are not covered. |

For the circular proof, Yin_C_F0119 supplies the moment recursion and logarithmic primitive, and bounded determinant multiplicativity supplies the Schur factorization.
Yin_C_F0119's subsequent centered identification through MS24 is not used.
Its primitive argument applies to every selfadjoint constant matrix and selfadjoint semicircular coefficient family, including the present signed linearization; it does not depend on the zero diagonal blocks of Yin_C_F0119's particular original hermitization.
Yin_C_F0121 supplies the action's provenance and strategy connection, not the new global comparison.

The external Jensen input is precisely [HP03-U001](../literature/HP03/Yin_U001.md#hp03-u001).
Its unital-column statement, selected proof and application were inspected from the primary preprint.
[HLN07-U001](../literature/HLN07/Yin_U001.md#hln07-u001) is related-source reading only.
Neither HLN07 nor a numerical search is a mathematical premise.

## 2. Positive certificates and the full positive cone

Use the root module's notation.
For a positive trial \(b\), the congruence
\[
 \mathcal C_b-\eta
 =\mathcal C_{b^{1/2}}(I-\Psi)\mathcal C_{b^{1/2}},
 \qquad
 \Psi=\mathcal C_{b^{-1/2}}\eta\mathcal C_{b^{-1/2}}
\]
preserves strict Hilbert--Schmidt positivity.
If \(bqb-\eta(q)>0\), then \(W=b^{1/2}qb^{1/2}>0\) satisfies \(W-\Psi(W)>0\).
The similar completely positive map
\[
 X\longmapsto W^{-1/2}\Psi(W^{1/2}XW^{1/2})W^{-1/2}
\]
has value strictly below \(I\) at \(I\), hence operator norm and spectral radius below one.
Similarity preserves the spectrum, and Hilbert--Schmidt selfadjointness of \(\Psi\) gives \(I-\Psi\succ0\).

Conversely, \(I-\Psi\succ0\) controls the largest eigenvalue.
The retained Yin_C_F0124 positive-map argument also bounds the absolute value of each negative eigenvalue by the largest eigenvalue; thus \(\|\Psi\|_{2\to2}<1\).
This additional argument is necessary: it is not an inference for arbitrary selfadjoint linear maps.
The Neumann inverse is completely positive.
Applied to \(b^{-1}>0\), its zeroth term already proves that the normalized certificate
\[
 q=(\mathcal C_b-\eta)^{-1}(I)
\]
is strictly positive.

For a given \(q>0\), the equation \(bqb=I+\eta(q)\) has exactly one positive solution: conjugate by \(q^{1/2}\) and take the unique positive square root.
This proves both compositions of the claimed bijection.
There is no limiting or boundary matrix in this argument.

Determinants of the certificate equation give exactly the exponent \(1/(2d)\) in the root module.
The plus-sign map is strictly positive by the same absolute eigenvalue control.
It preserves Hermitian matrices, so its quadratic completion on the real Hermitian Hilbert space has the stated unique maximum.
The extrema are ordered as written; this review does not interchange them.

For zero mean, determinant monotonicity gives the lower capacity bound.
Testing \(q=tr\), \(t\to\infty\), gives the reverse bound for every fixed \(r>0\), including singular \(\eta(r)\).
Taking an infimum afterwards covers zero capacity and nonattainment.
The extension from selfadjoint to arbitrary complex coefficients invokes Yin_C_F0124's already reviewed hermitization and capacity-square identity.
The factors \(2d\), \(2m\), and \(e^{-1/2}\) are consistent.

## 3. Circular physical inverse and determinant normalization

Let \(S=a+\sum_jb_jc_j\), with circular variance one, and fix \(\varepsilon>0\).
Put \(D=SS^*+\varepsilon^2I\).
Direct multiplication gives
\[
 \begin{pmatrix}\varepsilon^2I&S\\S^*&-I\end{pmatrix}^{-1}
 =
 \begin{pmatrix}
 D^{-1}&D^{-1}S\\
 S^*D^{-1}&-I+S^*D^{-1}S
 \end{pmatrix}.
\]
The bottom-right block is \(-\varepsilon^2(S^*S+\varepsilon^2I)^{-1}\).
This verifies both signs and the formula for \(Q_0\).
Boundedness of \(S\) supplies strictly positive scalar lower bounds for \(P_0\) and \(Q_0\), while \(Q_0\le I\).

The signed pencil is boundedly invertible.
Its inverse expectation \(q_0\) is invertible because its Schur complement over the negative block \(-Q_0\) is \(P_0+Y_0Q_0^{-1}Y_0^*>0\).
Consequently the Dyson identity and the real part of its logarithmic primitive pass continuously to the real gap at zero.
With \(G(0)=-q_0\), linearity of the covariance gives the stated sign \(q_0^{-1}=A-\Theta(q_0)\).
The logarithmic branch contributes only its real part \(\log|\det q_0|\).

Expanding each circular element into two semicircular elements gives (7): the two off-diagonal covariance terms cancel, while the diagonal maps are \(\eta\) and its Hilbert--Schmidt adjoint.
Inverting the resulting block matrix gives all three identities (8) in the written multiplication order.

The signed Schur factorization has diagonal blocks \(D\) and \(-I\), with determinant-one triangular factors.
Thus
\[
 \log\Delta_{\operatorname{tr}_{2m}\otimes\tau}(L_\varepsilon)
 =\frac12(\operatorname{tr}_m\otimes\tau)\log D.
\]
This is the defined regularized logarithmic determinant, not half of it again.
Furthermore,
\[
 -\log|\det q_0|=\log\det C_0-\log\det Q_0,\qquad
 \tfrac12\operatorname{Tr}(q_0\Theta(q_0))
 =-\operatorname{Tr}(P_0\eta(Q_0)).
\]
Multiplying the last equation (8) by \(Q_0\) and tracing gives
\[
 -\operatorname{Tr}(P_0\eta(Q_0))
 =\operatorname{Tr}Q_0+\operatorname{Tr}(Q_0a^*C_0^{-1}a)-m.
\]
These establish (9), with unnormalized finite traces and the factor \(2m\).
This part alone asserts a value at the physical point; the next argument is essential for the global minimum.

## 4. Comparison with every positive trial

The normalization in (10) follows from (8), using \(W=C_0^{1/2}P_0C_0^{1/2}>0\) and the Hilbert--Schmidt adjoint of \(\Phi\).
It does not require \(\Phi\) to be selfadjoint.
Starting from the raw determinant difference displayed after (11), substituting \(Q_0=I-M^*M-\Phi^*(W)\) gives (11) exactly.

For \(h(t)=t-\log t-1\), the primary Jensen statement applies after appending the positive square root of \(I-\Phi(I)\) to a Kraus row and giving it input \(I\).
All input spectra are strictly positive and \(h(1)=0\).
This proves (12) without requiring a finite value of \(h(0)\).
Taking the trace against \(W>0\) preserves the inequality; no commutation with \(W\) is needed.

After splitting with \(W+MM^*=I\), the exact remaining correction in (13) is
\[
 \langle M,(\mathcal D-\log\mathcal D-I)M\rangle_{\rm HS},
 \qquad \mathcal D(X)=R^{-1}XU.
\]
Left multiplication by \(R^{-1}>0\) and right multiplication by \(U>0\) are commuting positive definite operators on the matrix Hilbert space.
Their product is positive definite and their logarithms add.
This assertion concerns commuting multiplication operators; it makes no false claim that \(R\) and \(U\) commute as matrices.
Spectral calculus therefore proves that the correction is nonnegative.

The remaining term \(\operatorname{Tr}(Q_0h(U))\) is nonnegative and vanishes only for \(U=I\).
Hence every positive trial has value at least the physical value, with equality exactly at \(Q_0\).
The already constructed \(Q_0\) proves existence.
No compactness, stationarity-to-minimum inference or unproved matrix convexity is used.

Substitution of the fixed-inertia Schur matrix into the action gives (4).
For a fixed \(Q\), completing the strictly negative quadratic square in \(Z\) gives its unique maximum at \(C_Q^{-1}a\); minimizing the positive logarithmic expression in \(P\) then gives \(P=C_Q^{-1}\).
These two optimizations verify the ordered formula (5).
The optional affine matrix inequality (17) follows at the optimum from \(P_0>0\); it is not a hidden restriction on the original trial set.

## 5. Degeneracies, limits and continuation

Empty noise is included: \(\Phi=0\), \(C_Q=\varepsilon^2I\), and \(Q_0=(I+\varepsilon^{-2}a^*a)^{-1}\);
the minimum becomes \(\log\det(aa^*+\varepsilon^2I)\) before division by \(2m\).
No invertibility of \(a\) is needed.

At zero mean, the objectives decrease pointwise as regularization decreases.
For arbitrary extended-real decreasing functions, the infimum commutes with this limit by testing each fixed trial after the lower bound.
The subsequent scalar scaling \(Q\mapsto tQ\), \(t\downarrow0\), kills \(\operatorname{Tr}Q\) and leaves the determinant ratio fixed.
This proves the full centered circular capacity equality, including singular outputs, zero capacity and unattained limiting infima.
Spectral convergence includes a possible \(-\infty\) logarithmic determinant.

With nonzero mean, the same pointwise monotonicity of the objective is not available.
The displayed scalar example correctly gives a naive zero-regularization infimum \((|a|^2-1)/2\), rather than \(\log|a|\), when \(|a|>1\).
The regularization must remain outside the minimization in the presently proved formula.

Every completely positive covariance map has a circular realization, so the centered recovery reaches every capacity map.
This does not identify an arbitrary affine semicircular pencil with its circular realization: nonzero pseudo-covariance changes the affine law.
The missing coupled off-diagonal term remains the genuine extension problem.
This review does not resolve it or assess a final choice of general formula.

No proof correction was required in either inspected artifact.
Navigation-only later edits do not change the findings; substantive formula, scope or proof changes require renewed scoped review.
Numerical experiments were not rerun and are not evidence for this conclusion.
Formal verification, external expert review and manuscript compilation were not performed.
