---
author: Yin
---

# Review of directional Cauchy energy and the transverse slice

## Finding

At 2026-11-16T17:22 UTC a separately assigned agent for Yin independently reviewed C_F0318 v1 in full at its candidate decision of 17:18 UTC.
The reviewer did not develop the proof and received the fixed mathematical inputs without development dialogue, author explanations, exploration notes or prior findings on this candidate.
The matrix identity, its sharp directional bound, the generator defect and the transverse identity on analytic unitaries hold.

For each restricted measure \(\lambda\), both the maximal-density integral and the squared curvature are bounded by the corresponding quantities for \(\mu\).
The hard truncations converge almost everywhere by the principal-value theorem, hence weakly in \(L^2(\lambda)\) by uniform \(L^2\) boundedness on a finite measure space.
The norm limit in the same theorem upgrades convergence to strong convergence.
The reviewer checked these hypotheses, the curvature coefficient \(1/6\) and the positive-density rectifiable reduction in the published [Tolsa--Verdera Theorem 2, p. 481](https://www.acadsci.fi/mathematica/Vol31/tolsa.pdf#page=3).
The graph calculation uses \(g=d\lambda/d\mathcal H^1\) for ordinary arclength and gives the coefficient \(\pi^2g^2/3\), as verified against [Lemma 8 and its flat calculation in the authors' version, pp. 8--9](https://mat.uab.cat/~xtolsa/xv2.pdf#page=8).
Thus \(g\) agrees almost everywhere on the positive-density part with the limit using \(2r\) in the denominator.
The input here is the published theorem and its graph normalization.

For the soft kernel, the mixing density integrates to one and has mass \(a^2/(a^2+d^2)\) above any fixed \(d>0\).
Its average of the absolute value of the hard kernels at separation \(d\) is \(d/(d^2+a^2)\le1/(2a)\), so the interchange for fixed \(a\) is justified.
The uniform bounds on the hard fields and concentration at zero give the asserted strong limit.
For \(A=z_1-z_2\), \(B=z_1-z_3\), multiplying the three projected kernel products by their common denominator gives the constant term \(|(e^TA)B-(e^TB)A|^2=|e|^2\det(A,B)^2\).
The coefficient of \(a^2\) is half the sum over all three squared projected chords.
Permutation invariance of the triple integral supplies the factor three on the left, and the constant term tends by domination to \(|e|^2 c^2(\lambda)/4\).
With \(v_\mu=2C\mu\), this gives exactly the isotropic part \(c^2(\lambda)I_2/3\) in the matrix of squared vacuum components and the positive remainder in (6).

For a disjoint Borel partition, keeping only triples in a single member increases to a matrix bounded above by the matrix on the union.
For each restriction, ball differentiation makes its trace the integral of the same \((4\pi^2/3)\theta_\mu^2\) on that set.
The trace of the positive difference therefore tends to zero and proves countable additivity entrywise.
The density of the resulting matrix measure with respect to its trace is positive and has trace one.
The positive trace is carried by the rectifiable part, where arclength-null parameter sets are also null for the trace.
On a differentiability piece with uniformly controlled radius and derivative direction, the unit graph chords deviate by at most \(\rho\) from a common line, using that the graph parametrization has first coordinate equal to its parameter.
For every Borel subset of that piece the normal component of the positive matrix in (6) is bounded by \(\sin^2(\rho)\) times its trace.
Applying this on countably many pieces and tolerances proves that the density annihilates the actual normal direction almost everywhere.
Positivity and trace one then force the tangent projection, and the zero-density part has trace zero.
The disk example has \(\xi_\mu(z)=2z\) and \(\theta=0\), so the directional bound is an equality with strictly positive right side.

The projected imaginary vacuum is controlled by \(\eta+\epsilon\).
The conjugate phase on \(Z\) under the reversal and the vacuum tested on \(Z-Z^*\) give \(\|\delta_y Z\|_2^2=\operatorname{Re}\langle\xi,iY\rangle\).
The real part at \(\xi=Z\) is \(\eta^2\), giving the asserted defect by Cauchy--Schwarz.
On the actual joint tensor-leg graph, the difference \(A_x-A_y\) is half the sum of the two pure associators.
Each is zero by C_F0076, so the contracted \(y\)-defect is half of the contracted total.
The signed curvature contraction in (20) of C_F0078 gives \(F^j(u)/2\) for the total real pairing, hence \(F^j(u)/4\) for this component.

For the single-component energy calculation, write \(T=T_y\), \(\zeta=\zeta_y\) and initially write \(\delta_y p=\sum a\otimes b\) on tensor approximants.
The second summand after slicing \(\delta_y(p^*)\cdot p\) is \(\sum b^*\tau(a^*p)\).
Its real pairing with \(\zeta\) equals \(\operatorname{Re}\langle p,\Theta(\delta_y p)\zeta\rangle\) by trace cyclicity and selfadjointness of \(\zeta\).
The other summand from \(\delta_y(p^*p)\) gives \(\operatorname{Re}\langle Tp,p\zeta\rangle\).
Substitution in \(T^*(Tp)=(Tp)\zeta-T^2p\) using the actual tensor approximants yields exactly the two cross terms, the negative contracted associator and the negative pairing of \(T(p^*p)\) with \(\zeta\).
At \(u=h\pm i\sqrt{1-h^2}\), the binomial polynomial sequence converges in norm and first-derivative graph.
Its product with its adjoint converges in that graph to one, so the last pairing vanishes.
The contracted defect passes to this analytic evaluation as a sliced outer derivation.
Completing the square now gives the first formula (4).
Summing it and inserting \(F^0+F^1=D+H\) gives the second with the positive sign of \(H\).
Its integral is at most \(2c^2(\mu)\), hence at most \(6(\eta+\epsilon)^2\).

The six dependency interfaces below were checked at their stated uses.
The general uniform bound for the negative part of \(D\) remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0318_v1.md#decision-candidate) | Fixed 17:18 UTC candidate and its precise scalar and mixed conclusions. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0318_v1.md#statement) | Directional matrix formula, sharp rotated bound, actual generator defect and transverse energy on exchange-symmetric tests. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0318_v1.md#argument) | Complete proof, including soft directional symmetrization, tangent localization, actual tensor domains and analytic-unitary contraction. |
| [Finding](#finding) | [Hard Cauchy transform](../../claims/Yin_C_F0267_v1.md#hard-cauchy-transforms-and-the-original-core) | Vacuum normalization by twice the conjugated transform and finite geometric integrals. |
| [Finding](#finding) | [Exact scalar energy](../literature/TV06/Yin_U002.md#tv06-u002) | Published Theorem 2, arclength coefficient in Lemma 8, rectifiable positive-density reduction and strong hard-truncation limit. |
| [Finding](#finding) | [Disk law](../../claims/Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Scalar vacuum, positive curvature and zero arclength density for the equality example. |
| [Finding](#finding) | [Phase and coassociativity](../../claims/Yin_C_F0076_v1.md#statement) | Reversed unit phase, actual four tensor-leg domains on the core, and vanishing of both pure associators. |
| [Finding](#finding) | [Mixed energy](../../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Actual core adjoint and second iterate, individual real-component pairing, analytic limiting identity and the coefficient of the total curvature contraction. |
| [Finding](#finding) | [Signed difference](../../claims/Yin_C_F0314_v1.md#statement) | Matched forms and their signed sum, prescribed analytic tests and the integral formula for the nonnegative inner term. |
