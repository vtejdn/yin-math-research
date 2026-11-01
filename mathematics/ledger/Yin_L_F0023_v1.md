---
author: Yin
---

# Extending Miy26 Spectral Formulas

<a id="miy26-spectral-extension"></a>
Date: 2026-09-11.
Author: another AI agent.
Authorization: the user requested autonomous exploration of a broad variable class including free semicircular and circular families for Miy26's spectral formulas.

This record owns the mathematical distinctions, new deduction and selected source applications below.

## 1. Which formula is being extended

Let \((\mathcal M,\tau)\) be a finite von Neumann algebra with a faithful normal tracial state.
Throughout, \(L^0(\mathcal M)\) denotes its affiliated-operator algebra.
A nonexistent affiliated inverse is excluded from any \(L^2\)-resolvent set.

| Target | Existing exact source | What must survive in an extension |
| --- | --- | --- |
| \(\lambda\notin\sigma(f)\iff(\lambda-f)^{-1}\in L^2\) for affiliated rational \(f\) | [Miy26-U003, Corollary 1.2](../audits/literature/Miy26/Yin_U003.md#miy26-u003), using U002 | Every inverse under consideration must be in the rational algebra and every rational \(L^2\) element must be bounded. A Haagerup estimate alone does not provide this. |
| \(r(P)=\lim_n\|P^n\|_2^{1/n}\) | [Miy26-U003, Proposition 3.7 and Remark 3.8](../audits/literature/Miy26/Yin_U003.md#miy26-u003) | A subexponential comparison of operator and \(L^2\) norms along powers is enough; there need be no rational-resolvent theorem. |
| \(\sigma(P(c))=\sigma(P(l))\) for holomorphic polynomials | [Miy26-U005, Corollary 4.2](../audits/literature/Miy26/Yin_U005.md#miy26-u005) | Both spectrum inclusions, including the bounded inverse's membership in the holomorphic subspace. |
| The quadratic six-state spectrum formula | [Miy26-U007](../audits/literature/Miy26/Yin_U007.md#miy26-u007) | The formal coefficient recurrence must characterize actual inverses. Test the specified orbit, not automatically the spectral radius of an unreduced state matrix. |

The new progress below gives a full homogeneous spectral formula for a larger source class, a mixed-degree spectral inclusion, and exact positive applications of the original inverse criterion.
None of these silently resolves all four targets at once.

## 2. A broad full-spectrum class already covered by literature

The [KPZ26 selected audit](../audits/literature/KPZ26/Yin_U001.md#kpz26-selected-audit) supplies the homogeneous full-spectrum formula, its variance normalization, applicable freely infinitely divisible R-diagonal class, examples and exact source-inspection limits.
It is an external theorem specialization, not a project Claim.

The infinitely divisible restriction has mathematical content: a Haar unitary has unit-circle spectrum, while its variance-one creation model has closed-unit-disk spectrum.
R-diagonality alone cannot yield that formula.
Proposition 5.2 provides the specific no-L2-inverse-at-zero property excluding this example.
It does not state the all-shifted-inverse or arbitrary multivariable rational theorem.

## 3. What the mixed-degree comparison gives for Miy26's recurrence

For two normalized iid bounded free R-diagonal inputs and

\[
f=\sum_{i,j=1}^2 a_{ij}b_ib_j+\sum_{i=1}^2\beta_i b_i,
\]

let \(Q_\lambda\) be exactly the six-state matrix with its initial vector \(e_1\) in Miy26-U007, with the coefficient vector there replaced by \(\beta\).
[Yin_C_F0093](../claims/Yin_C_F0093_v1.md#yin_c_f0093) and the audited circular formula give the sufficient resolvent criterion

\[
\lambda\ne0,\quad Q_\lambda^n e_1\longrightarrow0
\quad\Longrightarrow\quad
\lambda\notin\sigma_{\mathcal M}(f).
\tag{9}
\]

Equivalently, \(\sigma(f)\) is contained in the circular model's explicit set.
This conclusion covers arbitrary mixed linear and quadratic terms, but is an inclusion.
Failure of the orbit to decay has not been proved sufficient for membership in \(\sigma(f)\) for an arbitrary R-diagonal family.

For the freely infinitely divisible subclass the homogeneous case has equality by the [KPZ26-U001 homogeneous interface, equations (1)–(3)](../audits/literature/KPZ26/Yin_U001.md#consumed-theorem-and-explicit-spectrum-specialization), including unequal laws and variances after the indicated weighting.
The first unresolved mixed-degree test is the reverse implication in (9) for a genuinely mixed polynomial, including whether \(0\in\sigma(f)\) always holds when the constant coefficient vanishes.
A product factorization or a sum of polynomials in disjoint free subsets can collapse to an already R-diagonal case; it should not be mistaken for the general two-variable test.



## 4. Direct positive families for the all-rational inverse criterion

The original semicircular or Haar rational theorem is inherited by **bounded rational images and subtuples**, without an inverse coordinate change.
Specifically, let \(s\) be a finite semicircular family in \(\mathcal N\), and let \(X_1,\ldots,X_k\) be any bounded elements of

\[
\operatorname{Div}_{L^0(\mathcal N)}\mathbb C\langle s\rangle.
\]

Set \(\mathcal M=W^*(X)\).
Under the usual trace-preserving inclusion \(L^0(\mathcal M)\subseteq L^0(\mathcal N)\), minimality of division closure gives

\[
\operatorname{Div}_{L^0(\mathcal M)}\mathbb C\langle X\rangle
\subseteq
\operatorname{Div}_{L^0(\mathcal N)}\mathbb C\langle s\rangle.
\tag{12}
\]

The inclusion respects the affiliated inverses used in each finite rational expression.
Therefore every element of the left side which is in \(L^2(\mathcal M)\) is bounded by Miy26-U002.
Since it is affiliated with \(\mathcal M\), that bounded operator lies in \(\mathcal M\).
Every existing rational inverse is in the same division closure by its definition.
Consequently the pointwise inverse-\(L^2\) resolvent criterion holds for every rational \(f\) in the left side, counting a nonexistent inverse as failure.
The Haar version uses Miy26-U003, Theorem 3.5, in the identical inclusion argument.
The field property of the original model can be used but is not needed to manufacture a nonexistent inverse.

Examples include arbitrary polynomial images of a free semicircular tuple, the usual circular coordinates, free rate-one Poisson variables \(s_i^2\), and freely independent sums of disjoint sets of these squares.
The square/free-Poisson identification is the standard semicircular pairing specialization; the conclusion (12) only uses the displayed polynomial, even without naming its law.
No inverse coordinate map, freeness of the new tuple, bounded dual for its listed coordinates or absence of algebraic relations is required.
Thus this application also permits nonfree or algebraically dependent images.
It is a direct source specialization, not a new Claim.

This does **not** prove

\[
\operatorname{Div}_{L^0(\mathcal M)}\mathbb C\langle X\rangle\cap\mathcal M
=\operatorname{Div}_{\mathcal M}\mathbb C\langle X\rangle.
\]

That bounded scalar closure is a different target and need not pass to polynomial subalgebras.
The argument above establishes boundedness of an affiliated rational element, without reconstructing it by scalar inverses which are bounded at every stage in the new coordinates.

The later [Yin_C_F0095](../claims/Yin_C_F0095_v1.md#yin_c_f0095) supplies the finite matrix/corner transfer and exact free-Poisson models of rational rates.
More substantially, [Yin_C_F0096](../claims/Yin_C_F0096_v1.md#yin_c_f0096) gives a separate Fock/finite-defect proof for every positive real free-Poisson rate, mixed with semicircular coordinates.
Its key step is to apply the existing Yin_C_F0034 to unnormalized bounded right annihilation; neither normalized bounded duals nor maximal Delta is required.
These new claims have their own proof and review records, rather than being silently absorbed into the earlier direct-source specialization.

## 5. The q-deformed spectral-radius baseline

The already inspected q-Wick bound in [Yin_C_F0020](../claims/Yin_C_F0020_v1.md#yin_c_f0020), for every fixed \(|q|<1\), reads

\[
\|W(\xi_m)\|\le C_q(m+1)\|\xi_m\|_q.
\]

Distinct particle levels are orthogonal in the actual q-inner product.
Therefore the proof of Miy26 Proposition 3.7 applies to every polynomial \(P\) in a finite q-Gaussian tuple: decompose a degree-\(N\) polynomial by particle level, use Cauchy--Schwarz to bound its norm by \(C_q(N+1)^{3/2}\) times its \(L^2\) norm, and use \(\deg P^n\le n\deg P\).
This proves the same \(L^2\)-power spectral-radius formula, as a direct use of the already audited general rapid-decay mechanism.

This does not solve the multivariable q-rational \(L^2\)-to-bounded problem.
The missing input remains compatibility of rational residual coefficients with q-Gram geometry, as recorded in Yin_C_F0020 and Yin_C_F0015's application notes.
Orthogonal particle **levels** are enough for the radius formula; an orthonormal free-word **basis with finite residuals** is a stronger requirement.
No assertion that the six-state circular matrix is unchanged for nonzero q is made.

## Search evidence and continuation

Existing knowledge checked first: Miy26-U002/U003/U004/U006; Yin_C_F0015, Yin_C_F0017, Yin_C_F0020 and Yin_C_F0021; the R-diagonal obstruction Yin_C_F0019; the application and route records linked above.
The previously inspected local literature did not already supply a new arbitrary-polynomial spectral theorem for R-diagonals.
Primary-source web queries for free R-diagonal polynomial spectra, creation models, Haagerup estimates and Meixner rational boundedness located KPZ26; the selected audit records its exact PDF and the discovered HTML date discrepancy.
Further resolvent queries located Haagerup--Kemp--Speicher and the established HL00 interfaces, without establishing a new pointwise shifted-inverse theorem.
No claim of novelty or absence from the literature is made.

The DHH+25 primary-source branch was reopened after Yin_C_F0093 supplied the previously missing upper spectrum bound.
The initial use of its Theorem 1.27 as a lower support bound for Yin_C_F0094 remains conditional; the [preserved proof history and positivity repair](../claims/Yin_C_F0094_v1.md#yin_c_f0094-proof-v1-history) identify the checked support-containment gap and the complete replacement argument.
The versioned PDF's pp. 13-15 and selected proof interfaces on pp. 84-87 were inspected; the source record preserves both the valid specialization and the general \(k=1\) warning.

The next useful mathematical checks are: independently review Yin_C_F0093 and Yin_C_F0094; test the reverse inclusion for other mixed-degree polynomials in the freely infinitely divisible R-diagonal class; and determine whether a selected source theorem supplies shifted inverse \(L^2\) divergence or an operator-valued resolvent criterion.
Yin_C_F0094 closes the full-spectrum problem for the displayed product family.
A Brown-support formula, homogeneous permanence or a finite formal coefficient recurrence alone cannot discharge the pointwise inverse-integrability obligation.
