---
author: Yin
---

# Positive covariance capacity gives uniform affine determinant bounds and excludes Brown atoms

## Current assessment
[Selected decision](#decision-adopted-retained-proof)

## Exact retained scope and provenance

<a id="statement"></a>

For arbitrary deterministic complex means and finite complex semicircular coefficients, retain the centered determinant lower bound from the nonnegative real-linear mean correction, monotonicity and concavity under real scaling of a fixed mean, positive-capacity atomlessness for every shift and the coefficient-controlled logarithmic disk-mass bound.
The zero-capacity case retains only the extended-real lower bound.
No planar absolute continuity, strict determinant inequality, unique minimizing mean or Brown support/spectrum equality follows.
The complete fixed argument and original mathematical development are [retained below](#argument), including the historical author and limited collaborator checks and status statements.
The complete formal self-review, its actual date and checking limits are retained in [R_F0177](../audits/reviews/Yin_R_F0177_v1.md#capacity-atomlessness-finding).
This placement preserves existing mathematics; it selects no Task, objective change, new theorem role, novelty or publication claim.

Dated candidate, “draft,” author-check and unadopted-status sentences within the retained text describe the original development.
The selected current decision above owns the present mathematical adoption and exact review evidence.

## Complete retained argument

<a id="argument"></a>

## 1. The deterministic mean cannot lower the determinant below the centered value

Let \(T_0=\sum_j a_j\otimes s_j\), with arbitrary complex \(m\)-by-\(m\) coefficients and free standard semicircular elements in a finite von Neumann algebra with faithful normal tracial state.
Use \(\varphi=\operatorname{tr}_m\otimes\tau\), and put
\[
 \eta(x)=\sum_j a_jxa_j^*,\qquad \rho(x)=\sum_j a_jxa_j.
\]
For \(b>0\), let
\[
 H_b=1_m+\eta(b),\qquad
 \mathcal T_b(Z)=H_bZb^{-1}+\rho(Z^*).
\]
C_F0126 proves that \(\mathcal T_b\) is a positive definite selfadjoint operator on the real Hilbert space with pairing
\(\langle X,Y\rangle_{\mathbb R}=\operatorname{Re}\operatorname{Tr}(X^*Y)\).
Thus, for every deterministic matrix \(a\),
\[
 q_a(b)=\langle a,\mathcal T_b^{-1}a\rangle_{\mathbb R}\ge0.
\]
Writing \(A(b)=\log\det H_b-\log\det b-m\), the main formula gives
\[
 \log\Delta_\varphi(a+T_0)
 =\frac1{2m}\inf_{b>0}\{A(b)+q_a(b)\}
 \ge \frac1{2m}\inf_{b>0}A(b)
 =\log\Delta_\varphi(T_0).
 \tag{1}
\]
The last equality is the zero-mean specialization of C_F0126 itself; no separate use of the MS24 determinant theorem is required for this deduction.
Consequently
\[
 \Delta_\varphi(a+T_0)
 \ge e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)}.
 \tag{2}
\]
This holds for all deterministic complex means, including means not commuting with the noise coefficients.
It is meaningful as a positive lower bound precisely when \(\operatorname{cap}(\eta)>0\).
No strict inequality or uniqueness of a minimizing mean is asserted.

There is also a one-parameter consequence.
For any fixed \(a\), real-linearity gives \(q_{ta}(b)=t^2q_a(b)\), \(t\in\mathbb R\).
Hence
\[
 s\longmapsto\log\Delta_\varphi(\sqrt{s}\,a+T_0)
 =\frac1{2m}\inf_{b>0}\{A(b)+s q_a(b)\},\qquad s\ge0,
 \tag{3}
\]
is nondecreasing and concave in the extended-real sense, and finite everywhere when capacity is positive.
This is real scaling of a fixed matrix mean; it does not assert radial invariance for complex scalar rotations when \(\rho\ne0\).

## 2. Positive covariance capacity excludes every Brown atom, for every mean

Fix an arbitrary deterministic \(a_0\) and put \(T=a_0+T_0\).
For any \(z\in\mathbb C\), apply (1)--(2) with mean \(a_0-z1_m\).
If \(\operatorname{cap}(\eta)>0\), then
\[
 u_T(z)=\log\Delta_\varphi(T-z1_m)
 \ge c_\eta:=-\frac12+\frac1{2m}\log\operatorname{cap}(\eta)>-\infty
 \quad(z\in\mathbb C).
 \tag{4}
\]
The Brown potential identity, in the convention already accepted in C_F0123, is
\[
 u_T(z)=\int_{\mathbb C}\log|z-w|\,d\mu_T(w),\qquad
 \mu_T=\frac1{2\pi}\nabla_z^2u_T.
\]
The measure is compactly supported.
If it had a positive atom at any \(z\), its potential at that point would be \(-\infty\), because the positive part of the logarithm is bounded on that compact support.
This contradicts (4).
Therefore
\[
 \operatorname{cap}(\eta)>0
 \quad\Longrightarrow\quad
 \mu_{a_0+T_0}\text{ has no atoms for every }a_0\in M_m(\mathbb C).
 \tag{5}
\]
In particular no invertibility of the shifted operator is needed: its potential can be finite on the spectrum.
The conclusion is stronger than exclusion of atoms just in the resolvent set.

Atomlessness does not imply a density with respect to planar area.
For \(m=1\), \(T=s_1\) has covariance capacity one, while its Brown measure is the semicircular law on the real line, singular with respect to planar area.
No general continuity of the potential, planar absolute continuity, or Brown-support/spectrum equality follows from the argument above.

## 3. A coefficient-controlled logarithmic bound on disk mass

Choose a finite positive bound \(M\ge\|T\|\); for example
\[
 M=\|a_0\|+2\sum_j\|a_j\|
\]
is such a bound, using \(\|s_j\|=2\).
Under positive capacity it is nonzero.
The Brown measure is supported in \(\{|w|\le M\}\).
Fix \(z\), put \(L_z=M+|z|>0\), and take \(0<r<L_z\).
If \(p=\mu_T(\{|w-z|\le r\})\), then
\[
 u_T(z)\le p\log r+(1-p)\log L_z.
\]
Combining this with (4) proves
\[
 \mu_T(\{|w-z|\le r\})
 \le \frac{\log L_z-c_\eta}{\log(L_z/r)}.
 \tag{6}
\]
For \(|z|\le M\), one may replace \(L_z\) by the uniform upper bound \(2M\).
The numerator is nonnegative because (4) and \(u_T(z)\le\log L_z\) both hold.
The bound tends to zero logarithmically as \(r\downarrow0\); it is not a power-law density estimate.

## 4. Reuse and verification boundary

[C_F0126](Yin_C_F0126_v1.md) supplies nonnegativity of the inner quadratic energy and the zero-mean capacity equality.
The normalized Brown potential follows the conventions and source interfaces in [C_F0123](Yin_C_F0123_v1.md).
This material derives consequences of those inputs.
A targeted local search of the current Claims and ledgers found no existing statement of the general atomlessness consequence (5); this limited search is not a priority determination and does not audit the private-source comparisons.

Equation (6) gives a quantitative disk-mass bound; (3) explains the geometric reason for the centered-ray behavior used in the complementary [spectral and atom-location argument](Yin_C_F0171_v1.md).
The [circular radial argument](Yin_C_F0170_v1.md) supplies stronger planar regularity under the separate hypothesis \(\rho=0\), and the [envelope argument](Yin_C_F0169_v1.md) develops regularized density calculations.

Self-checks cover the normalized factor \(1/(2m)\), use of the full real-linear correction rather than complex-linearity, extended-real inequalities when capacity vanishes, and the direction of the disk-mass bound.
The scalar semicircle is an exact control for the capacity constant and for the limitation of the atomlessness conclusion.
No independent whole-argument review is claimed.

The collaborating brown_boundaries agent also read this draft and checked the direction and normalization of the determinant lower bound, the exclusion of atoms, and the disk-mass inequality.
This limited collaborator check found no issue in those arguments; it is not a separately recorded independent source-dependency review and does not change the draft status.

## Assessment history

### Decision retained-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:21 |
| status | open |
| reason | Retain the exact complete argument in its responsible Claim home before selecting its applicable fixed review findings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact scope](#statement) | Exact retained scope and hypotheses above and in the complete original statement below. |
| argument | [Complete retained argument](#argument) | Complete original argument, failed implications and limitations retained below. |
| dependency | [Exact input](Yin_C_F0126_v1.md#setting-and-primary-unregularized-formula) | Positive definite real-linear inner energy and zero-mean capacity specialization, with singular outputs and zero capacity retained. |
| dependency | [Exact input](Yin_C_F0123_v1.md#brown-measure-and-the-local-source-boundary) | Accepted normalized Brown logarithmic-potential identity and compact support; no absolute continuity is imported. |

### Decision adopted-retained-proof

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:24 |
| status | proved |
| reason | Adopt the actual complete self-reviewed internal finding on this unchanged retained argument. Preserve all exact hypotheses, accepted input scopes, failed inferences and remaining independent-inspection boundary; no Task or theorem role changes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact retained scope and hypotheses above and in the complete original statement below. |
| argument | [Exact material](#argument) | Complete original argument, failed implications and limitations retained below. |
| dependency | [Exact material](Yin_C_F0126_v1.md#setting-and-primary-unregularized-formula) | Positive definite real-linear inner energy and zero-mean capacity specialization, with singular outputs and zero capacity retained. |
| dependency | [Exact material](Yin_C_F0123_v1.md#brown-measure-and-the-local-source-boundary) | Accepted normalized Brown logarithmic-potential identity and compact support; no absolute continuity is imported. |
| review | [Actual finding](../audits/reviews/Yin_R_F0177_v1.md#capacity-atomlessness-finding) | Whole deterministic-mean lower-bound argument: nonnegative real-linear mean energy, exact capacity constant, real-scaling monotonicity/concavity, arbitrary-mean positive-capacity atomlessness, coefficient-controlled logarithmic disk-mass bound and scalar semicircle limitation. No area-density or spectral-support equality. |

