---
author: Yin
---

# Linear-growth finite-curvature marginals restore original dual and adjoint coordinate domains

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## The normal polynomial core and a global Cauchy estimate

<a id="statement"></a>
<a id="yin_c_f0044"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Record kind: precise reduction, a sufficient-condition proof draft and a stopped broader branch.
Consumer: the separate normal-domain investigation.
No Claim ID or mathematical Role is assigned.
New deductions await independent review.

The global curvature route gives a concrete estimate on each single-coordinate algebra, including the whole algebra when there is one normal generator.
It does not yet give an estimate on mixed noncommutative polynomials.
A second gap is that the existing vacuum-adjoint hypothesis gives a distributional Cauchy functional, rather than a bound on truncated Cauchy transforms.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0044** after [complete independent review](../audits/reviews/Yin_R_F0076_v1.md#scalar-marginal-domain-finding).
Under the exact Yin_C_F0025 core hypotheses, linear growth and finite total curvature of a specified marginal imply that its entire coordinate von Neumann algebra lies in every original dual closure and actual adjoint domain.
For one generator this is all of M.
The canonical scalar construction and the failure of automatic linear growth are also reviewed.
This dated assessment supersedes the initial draft labels; mixed-word bounds and automatic truncation estimates remain unresolved.
No Role or lemma extraction is assigned.

## 1. Exact starting point and local reuse

Use exactly [Yin_C_F0025](Yin_C_F0025_v1.md#yin_c_f0025): a bounded normal generating tuple X in a finite tracial von Neumann algebra M, H=L2(M), and original complex-linear operators D_i0 on

\[
 \mathcal P_X=\mathbb C\langle X,X^*\rangle
\]

with vacuum in their Hilbert-adjoint domains, commutators [D_i0,X_j]=delta_ij P, and compact bounded starred-generator commutators.
Set

\[
 \eta_i=D_{i,0}1,\qquad
 E_{i,0}p=D_{i,0}p-p\eta_i,\qquad
 \xi_i=E_{i,0}^*1.
 \tag{1}
\]

Yin_C_F0025 proves closability, identifies all starred commutators by the normal spectral phase, and constructs the coarse derivations.
The original closures are denoted D_i; their actual adjoints are D_i0*.
Inner products are linear in the second variable.
This record does not replace the original domain by M.

The local reuse check included Yin_C_F0025, [Yin_C_F0026](Yin_C_F0026_v1.md#yin_c_f0026), [Yin_C_F0028](Yin_C_F0028_v1.md#yin_c_f0028), the [earlier Cauchy/T1 search boundary](Yin_C_F0040_v1.md#1-exact-question-and-reuse-check), and [Yin_C_F0043](Yin_C_F0043_v1.md#yin_c_f0043).
Yin_C_F0026 has a noncompact extra starred commutator and cannot refute the present compact-core statement.
Yin_C_F0028 already solves bounded rationality for a single coordinate; it does not assert that every bounded measurable coordinate function belongs to the original dual and adjoint domains.
Yin_C_F0043 supplies full tuple bounds for its analytic closed-curve geometry.
The new estimate below neither uses nor extends that change-of-variables argument.

## 2. What the Cauchy formula actually means

Fix j, write B_j=W*(X_j), and identify B_j with L-infinity(mu), where mu is the compactly supported nonatomic spectral probability measure of X_j.
For every scalar starred polynomial p=p(z,bar z), Yin_C_F0025's derivation on this algebra is

\[
 \partial_j p(z,w)=\frac{p(z)-p(w)}{z-w},\qquad
 E_{j,0}p(z)=
 \int\frac{p(z)-p(w)}{z-w}\,d\mu(w).
 \tag{2}
\]

For i different from j, E_i0 p=0.
To verify (2), its first expression has the outer Leibniz rule and the required values 1 and (bar z-bar w)/(z-w) on z and bar z.
These agree with the canonical coarse derivative.
Contraction of the second leg gives the second expression.
A starred polynomial is Lipschitz on a compact disk containing the spectrum, so its quotient in (2) is bounded off the null diagonal.
There is no principal-value assertion in (2).

Define, for epsilon positive,

\[
 C_\epsilon(f\mu)(z)=
 \int_{|z-w|>\epsilon}\frac{f(w)}{z-w}\,d\mu(w),
 \qquad h_\epsilon=C_\epsilon\mu.
 \tag{3}
\]

The truncated version E_epsilon p of (2) satisfies

\[
 E_\epsilon p=p h_\epsilon-C_\epsilon(p\mu),
 \qquad
 \int E_\epsilon p\,d\mu=2\int p h_\epsilon\,d\mu.
 \tag{4}
\]

The second equality is obtained by swapping z,w in the second double integral; its sign uses the kernel in (3).
The bounded divided difference and atomlessness give E_epsilon p -> E_j0 p in L2 by dominated convergence.
Therefore

\[
 2\lim_{\epsilon\downarrow0}\int p h_\epsilon\,d\mu
   =\langle\xi_j,p\rangle
   =\int \overline{\mathbb E_{B_j}\xi_j}\,p\,d\mu.
 \tag{5}
\]

Here E_Bj is the trace-preserving conditional expectation, equivalently the orthogonal projection in L2.
Thus the exact automatic conclusion is convergence of polynomial pairings to the L2 density

\[
 h=\tfrac12\overline{\mathbb E_{B_j}\xi_j}.
 \tag{6}
\]

Calling (6) “C mu belongs to L2” is legitimate only if this distributional convention is explicitly fixed.
Formula (5) alone proves neither principal-value convergence, nor weak convergence in L2, nor a uniform bound on ||h_epsilon||_2.
Convergence of functionals on a dense polynomial subspace is insufficient for the last inference without a norm bound.
No assertion that the stronger implication is false is made here.

## 3. The selected primary-source interface

A focused search located the exact curvature estimate in Xavier Tolsa, [*Rectifiable measures, square functions involving densities, and the Cauchy transform*, arXiv:1408.6979v2](https://arxiv.org/abs/1408.6979v2), revised 2015-01-31.
Its [primary PDF](https://arxiv.org/pdf/1408.6979) was inspected at Proposition 17.1, printed p. 94, equation (17.5), and Theorem 17.2, printed p. 95.
This is a selected theorem-statement/source-interface check, not a full monograph audit; no canonical PDF was retained.

The proposition attributes the following established identity to Melnikov-Verdera, *A geometric proof of the L2 boundedness of the Cauchy integral on Lipschitz graphs*, IMRN (1995), 325-331.
For a finite positive measure nu with linear growth constant L_nu,

\[
 \left|\|C_\epsilon\nu\|_{L^2(\nu)}^2
           -\tfrac16 c_\epsilon^2(\nu)\right|
 \le a L_\nu^2\,\nu(\mathbb C),
 \tag{7}
\]

where a is absolute and the curvature integral excludes all pairwise distances at most epsilon.
The adjacent T1 theorem requires tests on every square.
Only (7) is imported below; that stronger local-testing theorem is not invoked.
The original 1995 proof was not separately re-audited.

## 4. Positive weights give the exact global estimate needed

Assume a compactly supported probability measure mu has linear growth

\[
 \mu(B(z,r))\le Lr\qquad(z\in\mathbb C,\ r>0)
 \tag{8}
\]

and finite total Menger curvature

\[
 c^2(\mu)=
 \iiint c(z,w,v)^2\,d\mu(z)d\mu(w)d\mu(v)<\infty.
 \tag{9}
\]

For distinct noncollinear points c is the reciprocal circumradius; it is zero on collinear triples.
Diagonals are null under (8).
Equation (7) and monotone convergence show that, under (8), (9) is equivalent to

\[
 \sup_{\epsilon>0}\|h_\epsilon\|_2<\infty.
 \tag{10}
\]

The relevant gain is that these global tests suffice for a uniform infinity-to-2 estimate.
They need not be upgraded to local square tests.

Put \(A=(c^2(\mu)+aL^2)^{1/2}\).
If f is real and ||f||_infinity <=1, set nu=(1+f/2)mu.
This is a positive measure with

\[
 \tfrac12\mu\le\nu\le\tfrac32\mu,\quad
 L_\nu\le\tfrac32L,\quad
 \nu(\mathbb C)\le\tfrac32,\quad
 c^2(\nu)\le(\tfrac32)^3c^2(\mu).
 \tag{11}
\]

Each bound is pointwise or follows by multiplying the three nonnegative densities in the curvature integral.
Applying (7) to nu gives

\[
 \|C_\epsilon\nu\|_{L^2(\nu)}^2
 \le \tfrac{27}{8}A^2,\qquad
 \|C_\epsilon\nu\|_{L^2(\mu)}
 \le \tfrac{\sqrt{27}}2 A.
 \tag{12}
\]

The second estimate uses mu <=2 nu.
Also ||C_epsilon mu||_2 <=A by (7).
Since C_epsilon nu=C_epsilon mu+(1/2)C_epsilon(f mu), subtraction yields

\[
 \|C_\epsilon(f\mu)\|_2
 \le(\sqrt{27}+2)A
 \quad(f\text{ real},\ \|f\|_\infty\le1).
 \tag{13}
\]

Split a complex f into its real and imaginary parts, each of sup norm at most ||f||_infinity.
With \(K=2(\sqrt{27}+2)A\) this proves

\[
 \boxed{\ \sup_{\epsilon>0}
 \|C_\epsilon(f\mu)\|_2\le K\|f\|_\infty
 \qquad(f\in L^\infty(\mu)).\ }
 \tag{14}
\]

This is an estimate from L-infinity to L2.
It is not an L2 operator bound, and no local normalized curvature bound has been deduced.
Positivity in (11) is essential to this short comparison.

Equations (4), (10), (14), and convergence of E_epsilon p give

\[
 \|E_{j,0}p\|_2\le (A+K)\|p\|_\infty
 \quad(p\in\mathbb C[X_j,X_j^*]).
 \tag{15}
\]

The estimate works with a measure carried by a line, a curve, a planar set or a mixture, provided (8)-(9) hold.
There is no analytic parametrization in this proof.

## 5. Original adjoints and actual coordinate domains

On scalar starred polynomials in B_j, the canonical divided difference is symmetric in z,w.
The polynomial adjoint identity from Yin_C_F0025 consequently becomes

\[
 E_{j,0}^*p=p\xi_j-\overline{E_{j,0}(\bar p)}.
 \tag{16}
\]

The conjugation in the second term is conjugation in B_j.
The first term uses the full vector xi_j in H, not just its conditional expectation.
Indeed Yin_C_F0025 gives p xi_j minus Theta(partial_j(p*))^*1; the latter vector is precisely the conjugate in (16) by the symmetric kernel.
This identity tests against the entire original core P_X and is therefore an identity for the actual adjoint, not the adjoint of a newly restricted scalar operator.

For i different from j the same calculation gives E_i0* p=p xi_i, since both scalar coordinate commutators vanish.
Restoring (1), all i satisfy uniform bounds on these scalar polynomials:

\[
 \|D_{i,0}p\|_2\le C_{ij}\|p\|_\infty,\qquad
 \|D_{i,0}^*p\|_2\le C'_{ij}\|p\|_\infty.
 \tag{17}
\]

For i=j one can take C_jj=A+K+||eta_j||_2 and C'_jj=||xi_j||_2+A+K+||eta_j||_2.
For i different from j use ||eta_i||_2 and ||xi_i||_2+||eta_i||_2.
Right multiplication by eta_i has polynomial adjoint p ->p eta_i*; all these are well-defined L2 vectors.

Take f in B_j.
Kaplansky density followed by norm approximation inside C*(X_j) gives scalar starred polynomials p_n converging to f in L2 with a uniform sup-norm bound.
Both sequences in (17) are L2 bounded.
A weakly convergent subsequence of graph pairs for each operator has first component f.
The graphs of D_i and D_i0* are closed linear subspaces of H direct-sum H, hence weakly closed.
They therefore contain the corresponding limiting pairs.
Letting the polynomial norm bound decrease to ||f|| gives the bounds in (17) for f itself.
In particular,

\[
 \boxed{\ B_j\subseteq
 \bigcap_i\bigl(\operatorname{Dom}D_i
                   \cap\operatorname{Dom}D_{i,0}^*\bigr).\ }
 \tag{18}
\]

These are the original closures and actual Hilbert adjoints.
No core assumption for D_i* was inserted.
For d=1, B_1=M and (18) gives the original two all-M domains.
This is a stronger domain statement than the single-coordinate rationality equivalence already proved in Yin_C_F0028.

The canonical scalar construction also exists without initially assuming a dual: given (8)-(9), define E_0 by (2) on scalar starred polynomials.
Its commutators with z and bar z are respectively the rank-one vacuum operator and the Hilbert-Schmidt phase kernel.
Equations (5), (10) and density supply an L2 vacuum-adjoint vector: choose a weak L2 cluster point of h_epsilon, and the polynomial pairings identify it uniquely.
The polynomial adjoint formula then proves closability.
Thus this geometry really supplies examples of the exact compact-core setting, rather than an implication with an unverified existence premise.

## 6. Linear growth is not automatic, even with global truncation bounds

Here is an elementary boundary example, independent of the noncompact Yin_C_F0026 construction.
Fix \(0<\alpha<1/3\), for example alpha=1/4, and let

\[
 d\mu(x)=(1-\alpha)x^{-\alpha}\,dx,\qquad 0<x<1.
 \tag{19}
\]

The coordinate X=x is selfadjoint and its scalar polynomial core is dense.
Define E_0 by (2).
Its commutator with X=X* is P.
For the kernel convention (3), uniformly in epsilon,

\[
 |C_\epsilon\mu(x)|
 \le C_\alpha x^{-\alpha}
       (1+|\log x|+|\log(1-x)|).
 \tag{20}
\]

To check this estimate, subtract the constant density x^(-alpha) inside the integral.
The remaining absolute integral is at most

\[
 x^{-\alpha}\int_0^{1/x}
       \frac{|s^{-\alpha}-1|}{|1-s|}\,ds
 \le C_\alpha x^{-\alpha}(1+|\log x|).
\]

On (0,2) the integrand has an integrable singularity only at zero and a removable one at 1; on (2,1/x) it is bounded by a constant times 1/s.
The truncated constant-density integral has absolute value at most |\log x|+|\log(1-x)|: its two tails cancel when both are present, and when only one is present its logarithmic ratio is no larger than the corresponding endpoint ratio.
This proves (20).

Its square is integrable against mu, since 3 alpha<1.
For each interior x the principal value exists by local smoothness of the density.
Dominated convergence in L2 gives h_epsilon ->h.
Symmetrization (4) gives the vacuum adjoint xi=2h, and the polynomial adjoint formula E_0*p=p xi-E_0p proves closability.
Thus this is a d=1 instance of Yin_C_F0025, even with (10).
But

\[
 \mu((0,r))/r=r^{-\alpha}\longrightarrow\infty.
 \tag{21}
\]

It has no uniform linear-growth constant.
Its Menger curvature is zero because its support is a line.
Therefore one cannot insert (8) as an automatic consequence of the bare dual hypotheses, or even of those hypotheses together with global bounded truncations.
This example does not refute the all-M conclusion, which is already covered in the selfadjoint case.

## 7. Exact remaining interfaces and branch stop

Two separate interfaces remain for a general Yin_C_F0025 tuple.

First, (5)-(6) do not presently supply (10), and linear growth is demonstrably an extra restriction.
The selected curvature theorem has that restriction.
A theorem with a suitable nonuniform growth hypothesis, or a direct estimate from the distributional vacuum data, would be a new input; neither is claimed here.

Second, the scalar Cauchy formula applies to p(X_j,X_j*) only.
A mixed word has, for example,

\[
 E_{j,0}(aX_jb)=
 (\mathrm{id}\otimes\tau)((\partial_j a)\cdot X_jb)
 +a\,\tau(b)
 +(\mathrm{id}\otimes\tau)(aX_j\cdot\partial_j b),
 \qquad a,b\in\mathcal P_X.
 \tag{22}
\]

Its values depend on joint noncommutative products and traces.
Such words cannot be inserted into the scalar formula (2) as functions on the marginal spectrum.
Even if (8)-(9) hold for every marginal, (18) supplies the individual coordinate algebras, not every bounded element of their generated von Neumann algebra.
Neither a uniform estimate on products nor their graph convergence follows just from (17).
No freeness or operator-valued lifting theorem was proved in this bounded search.

The usable new deduction is therefore (14)-(18), conditional only on the displayed geometric assumptions and the selected established curvature identity.
The general Q3 conclusion remains open.
This global scalar branch stops here after producing the precise estimate and both missing interfaces; it is not continued as an unspecified T1 search.
Independent review should check the sign and factor 2 in (4)-(6), the positive weighted-measure comparison, the use of the full xi_j in (16), actual graph closure in (18), and the nonautomatic-growth example (19)-(21).


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:45 |
| status | proved |
| reason | Adopt the exact original finding at its actual unknown relationship. Preserve the mathematical status, statement, selected proof, dependencies and all historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#4-positive-weights-give-the-exact-global-estimate-needed) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0076_v1.md#scalar-marginal-domain-finding) | Exact scalar Cauchy/positive-reweighting estimate, original marginal closure and actual adjoint domains, d=1 all-M case, canonical examples and nonautomatic growth example in Sections 2-6; corrected Section 7 illustrative formula is separately retained in the same R and is not a proof premise. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the new isolated independent scalar/marginal finding for Sections 1–6. Preserve the original unknown scalar finding and the separate self-reviewed Section 7 formula correction in the new R home; the unresolved mixed-word and uniform-truncation interfaces are not accepted as new theorems. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#4-positive-weights-give-the-exact-global-estimate-needed) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0076_v1.md#current-isolated-finding) | Complete scalar mathematics in Sections 1–6: conditional growth/curvature estimate, positive reweighting, actual original marginal closure and adjoint domains, d=1 all-M specialization, canonical examples and failure of automatic growth. The Section 7 reviewer-contributed mixed formula and the unresolved mixed-word/uniform-truncation interfaces are excluded from this independent finding. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#4-positive-weights-give-the-exact-global-estimate-needed) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0076_v1.md#scalar-marginal-domain-finding) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0076_v1.md#scalar-marginal-domain-finding).

Material covered by that review: [Exact material](Yin_C_F0044_v1.md).
