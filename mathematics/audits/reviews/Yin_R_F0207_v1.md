---
author: Yin
---
# Independent review of the curvature row criterion for normal canonical domains

## Curvature row criterion

At 2026-11-13T08:55 a separate agent working for Yin reviewed the complete statement and argument of [C_F0078 v2](../../claims/Yin_C_F0078_v2.md#statement) at its November 13 candidate.
The reviewer had no role in its development and received the fixed proof, dependency locators and review scope without proof-development dialogue, author explanations or previous review findings.

For each fixed endpoint the diagonal has zero marginal mass.
Thus the nonnegative polynomial approximants in v1 (12) have row mass at most \(R=1+A\), even when their diagonal values are positive.
Removing one edge of a length-\(k\) path leaves two independent integrals bounded by \(R^{l-1}\) and \(R^{k-l}\), since the right path can be reversed by symmetry.
The triangle inequality and the all-pairs bound on the edge length times its kernel give (3), including paths with a repeated intermediate vertex.
This bound holds on the whole off-diagonal spectrum and the gap multiplier is zero on the diagonal, as required for the joint spectral measure of the actual vacuum.

The partial liberation construction uses the normal phase and actual conjugate variable and gives \(-\mathrm i[Z^*,\xi]\) as its vacuum before any marginal estimates.
For each finite symmetric kernel the row and column corrections cancel in C_F0077 (S1).
In (B0c)--(B0e), Cauchy--Schwarz in the row term retains the norm of the row integral, which is at most \(R^k\) for \(b_k\).
The remaining contraction has kernel \(b_k\circ b_k=b_{2k}\) and coefficient one.
After division by \((2R)^{2k}\), the coefficient of \(w_n\) is \(2(1+kB'\|\xi\|_2/R)/2^k\).
For each fixed \(q,u\), bounding one edge by \(\|q\|_\infty\) and applying the differentiated series at \(u\) bounds \(v_k\) by \(c_u\|q\|_\infty R^{k-1}\).
Should \(w_n>c+1\), the recursion forces all successive values to grow at least geometrically with ratio \(w_n-c>1\).
This proves the uniform estimate (4) without a uniform square-integrable row for \(g\).

I checked the use of the actual tensor-leg graphs against [C_F0076, Parts 1--3](../../claims/Yin_C_F0076_v1.md#statement).
Its hypotheses are the full normal ACSY assumptions in v2.
The bounded smooth phase approximants and their polynomial graph approximations give uniformly spatially bounded approximants in the common graph by convex combinations of the weakly converging graph tuples.
Taking a partial trace gives uniformly bounded approximants to \(T_a p\), so their products with the fixed \(L^2\) vacuum converge by first approximating the vacuum in \(L^2\) by bounded vectors.
Thus the adjoint identity used in v1 (19) concerns the original graphs.
On \(Z\), subtracting the left and right divided differences of the conjugate phase yields \((z-v)\mathfrak c^2\), and conjugation gives the value on \(Z^*\).
The factor \(1/2\) from the two real components and the factor \(\mathrm i\) in the liberation derivation give exactly \(-\mathrm iE_g/2\) in v1 (20).
Bounded convergence of the gap multipliers gives coarse convergence on generators and joint spectral convergence on \(\xi\), also for a spectral measure charging the diagonal.
Leibniz and the summable first-derivative series extend these identities to the analytic unitaries.

In the unitary averaging step, \(u(a)^*=-u(-a)\) supplies the same bound for the adjoint unitary.
The energy inequality therefore controls \(T_x,T_y\) and both complex contractions on the original polynomial core in operator norm.
For bounded Kaplansky approximants \(p_\lambda\) to \(p\in M\), the original adjoint formula also bounds \(E_0^*p_\lambda\).
Weak graph limits yield both domains.
The core relation \(E_0(X_jp_\lambda)=X_jE_0p_\lambda+\delta_{ij}\tau(p_\lambda)\Omega\) identifies the graph limit at \(X_jp\) with the claimed commutator sign for \(D_i=-\overline{E_0}\).
For the converse the full adjoint domain includes \(\Omega\), precisely the additional premise of C_F0070 Part C after restricting the supplied dual to \(M\Omega\).

For the dyadic test, the shell of maximum radius in \((t_j/2,t_j]\) contributes at most \(16\theta_j^2\) to each row.
The resulting linear growth bound \(2Lt\) gives \(8L/r\) for the inner disk and \(16L2^{-m}/r\) for outer annulus \(m\), yielding \(40L/r\).
The logarithmic case follows by summing the squares of \((1+j\log 2)^{-\beta}\), and a power exponent above one gives a geometric bound.
The scalar example cited at the end has a divergent sequence of row lower bounds already at the first power, as asserted in [C_F0143](../../claims/Yin_C_F0143_v1.md#statement).
The complete implication and equivalence hold on the stated marginal class.
This review covers the application of the fixed dependencies at the indicated scopes and leaves the unrestricted Task and the original external-source proofs outside its conclusion.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Curvature row criterion](#curvature-row-criterion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Curvature row criterion](#curvature-row-criterion) | [Statement](../../claims/Yin_C_F0078_v2.md#statement) | All marginal hypotheses, canonical domains and commutators, normal equivalence, dyadic test and its logarithmic and power consequences. |
| [Curvature row criterion](#curvature-row-criterion) | [Argument](../../claims/Yin_C_F0078_v2.md#argument) | Whole path estimate, finite-kernel recursion, passage to actual graphs and both domains, and the marginal estimates. |
| [Curvature row criterion](#curvature-row-criterion) | [Normal growth argument](../../claims/Yin_C_F0078_v1.md#argument) | Transfer of (12), (13), (15), and Sections 5 and 6 including the mixed coefficient, actual graph limits and commutator. |
| [Curvature row criterion](#curvature-row-criterion) | [Weighted liberation](../../claims/Yin_C_F0077_v1.md#argument) | Fixed-kernel vacuum, exact finite energy relation with row integral norm, and fixed-unitary continuity following (B7). |
| [Curvature row criterion](#curvature-row-criterion) | [Strong dual converse](../../claims/Yin_C_F0070_v1.md#statement) | Part C with the bounded-domain restriction and the actual adjoint vacuum test for the normal reverse implication. |
