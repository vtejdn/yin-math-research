---
author: Yin
---

# Review of conditional product divergences and concentration at limiting correlation one

## Finding

At 2026-11-14T14:46 UTC an agent outside proof development independently reviewed the whole [C_F0281 v1 candidate](../../claims/Yin_C_F0281_v1.md#decision-candidate) fixed at 2026-11-14T14:41 and checked its three declared dependency interfaces.
The reviewer received the fixed candidate and the requested scope without exploration notes, development dialogue, explanations from the proof developers or previous findings on this candidate.
All four conclusions follow at their stated scopes.

The product-density identity represents \(r-1\) by \(P_K\kappa\), with the omitted algebra on the left and the distinguished algebra on the right.
The subspace \(K\) reduces these two actions because their bounded multipliers and adjoints preserve the spanning products.
Thus left restriction by \(1_S(Y)\) and right restriction by \(1_F(Z)\) give the two squared norms in (1).
Testing \(r\gamma=\lambda\) on the countable dense continuous tests in each compact marginal spectrum identifies both fiber derivatives, including their mass one, outside respective marginal null sets.
Tonelli gives both integrals of the fiber squared deviations as \(\int(r-1)^2\,d\gamma\).
Projection contraction gives the upper bounds with \(\kappa\kappa^*\) on the left and \(\kappa^*\kappa\) on the right.
On each finite-divergence fiber the functional of centered tests is represented by the real mean-zero vector \(r-1\).
Bounded centered truncations approach that vector in \(L^2\), giving its squared norm as the optimal constant in (2).
When the vector is zero the means agree and the diffuse product marginal allows nonconstant tests on the fiber.
Writing \(q\) for the singular mass, \(r=0\) on the singular component and \(r=1/f\) on the absolutely continuous component.
The identity \(\int r^2\,d\gamma=\int f^{-1}\,d\lambda\) and \(1\le(\int f\,d\lambda)(\int f^{-1}\,d\lambda)\) yield \(q\le\chi^2/(1+\chi^2)\).

Domination of \(\mu\) on the row fiber gives \(0<\nu_y(F)<1\) when \(0<\beta<1\).
For the indicator of \(F\), the quotient in (2) is bounded above by \(g(y)\) and has the convex expression \(\beta^2/m+(1-\beta)^2/(1-m)-1\) at \(m=\nu_y(F)\).
Evaluating Jensen's bound at \(m=t/\alpha\) and multiplying by \(\alpha\) gives exactly (3), including its factor of \(\alpha\).
Interchanging the two disintegrations proves the column bound, and integration over disjoint row sets retains the common total divergence even when their chosen column sets differ.
In the limiting regime \(\beta_n>0\) eventually since \(t_n>0\).
Both \(t_n/\alpha_n\) and \((t_n-\alpha_n\beta_n)/\alpha_n\) tend to one, so the positive left side of (3) is asymptotic to \(\alpha_n^2/(\alpha_n-t_n)\).
Absolute continuity of the integral of \(g\) forces this reciprocal to vanish and proves (4).

Full starred conjugate variables give diffuse marginals and the represented partial liberation with Hilbert adjoint vacuum \(Z^*\xi_Z-\xi_ZZ^*\) by C_F0238 v1.
In the trace-pairing convention of Voi99-U003, the gradient \(j\) is the negative of this skewadjoint vacuum.
The product rule at \(ab\) gives \(\tau(a)\tau(b)-\tau(ab)\), while the rule at \(ba\) gives the negative of that expression.
Bounded strong-star approximation of \(a,b\) passes the moments to their von Neumann closures against \(j\in L^2(M)\), proving (6).
For the two affiliated selfadjoint tests, their ordered trace coupling has the two given spectral laws and integrates their squared scalar difference to \(\|a_n-b_n\|_2^2\), by truncation and \(L^2\) continuity.
The scalar Lipschitz bound for the clips therefore implies \(\|A_n-D_n\|_2\to0\).
Bounding the commutator by \(2L\|A_n-D_n\|_2\) forces their covariance to zero by (6).
Each clip's variance differs from that covariance by at most its centered \(L^2\) norm times \(\|A_n-D_n\|_2\).
For each marginal the original centering and unit second moment bound the absolute clipped mean by \(1/L\).
Choosing \(L>\max(\epsilon,2/\epsilon)\) and using the vanishing variance then gives convergence in trace measure for both original tests.
Their squared magnitudes on \(\{|a_n|\le L\}\) and \(\{|b_n|\le L\}\), respectively, converge to zero in \(L^1\) by the fixed uniform bound \(L^2\).
Subtracting from the respective unit second moments proves both limits in (5).

For \(\gamma_s\), the three row marginals have densities \(e,(1-s)(1-e),s(1-e)\) relative to Lebesgue probability.
Symmetry gives the column marginals and the diffuse diagonal carries singular mass \(s(1-c)\).
The product term has strictly positive density and its reciprocal integral bound is finite since \(\sum_{n\ge1}(n+1)2^{-n}<\infty\).
The two disintegrations thus have finite integrated divergences, including at \(s=0\) and \(s=1\).
Both within-cell terms together give \(p_n(1-e_n)\) to \(I_n^2\), and the product term contributes \(p_n^2 e_n^2/c\).
Centering and normalizing the cell indicator yields correlation \((1-e_n+p_n e_n^2/c-p_n)/(1-p_n)\to1\).
This verifies the sharpness example for ordered probability data, with realization by an actual starred vacuum outside the conclusion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0281_v1.md#decision-candidate) | Fixed decision dated 2026-11-14T14:41 and all direct input interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0281_v1.md#statement) | All four parts, including exact local divergences, leakage, both marginal concentration statements and the range of singular masses in the probability example. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0281_v1.md#argument) | Both disintegrations, optimal fiber constants, singular-mass estimate, indicator Jensen bound, liberation pairing, spectral clipping, tail energy and the explicit couplings. |
| [Finding](#finding) | [Actual starred hypotheses](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented starred derivations, outer actions and actual Hilbert adjoint vacua for the generating pair. |
| [Finding](#finding) | [Product-density identity](../../claims/Yin_C_F0279_v1.md#statement) | Projection representation of the product density in the ordered Hilbert space and square integrability in the presence of a singular part. |
| [Finding](#finding) | [Partial liberation](../../claims/Yin_C_F0238_v1.md#statement) | Diffuse marginals under the full hypothesis and the represented derivation with the specified commutator as adjoint vacuum. |
| [Finding](#finding) | [Liberation derivation and gradient](../literature/Voi99/Yin_U003.md#voi99-u003) | Signed relation to the Hilbert adjoint vacuum, moment identity on the algebraic core and its extension on bounded marginal tests, as checked in the liberation-derivation section. |
