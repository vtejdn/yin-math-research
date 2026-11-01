---
author: Yin
---

# Finite stable resolvent certificates and Brown contour and atom formulas

## Current assessment
[Selected decision](#decision-adopted-retained-proof)

## Exact retained scope and provenance

<a id="statement"></a>

For all finite complex affine semicircular pencils, retain the algebraic equation plus strict completely positive spectral-radius certificate equivalent to the actual resolvent, its unique physical branch, contour Brown masses, circle-mean disk and atom recovery, singular-value kernel limits and localization of every possible Brown atom among the deterministic mean eigenvalues.
With pseudo-covariance zero, retain the exact affine spectral region, exterior determinant in every resolvent component and normalized enclosed eigenvalue count.
Kernel mass, potential minus infinity, Brown atoms and contour mass remain distinct at their stated hypotheses.
The complete fixed argument below is retained from [Yin_L_F0042_v1](../ledger/Yin_L_F0042_v1.md) at 2026-10-21T02:21.
Its original mathematical development, attribution, review dates and historical status statements remain in that fixed L.
This placement preserves existing mathematics; it selects no Task, objective change, new theorem role, novelty or publication claim.

Dated candidate, “draft,” author-check and unadopted-status sentences within the retained text describe the original development.
The selected current decision above owns the present mathematical adoption and exact review evidence.

## Complete retained argument

<a id="argument"></a>

## 1. A finite stable-branch certificate for the resolvent set

Let
\[
T=a_0+\sum_j a_j\otimes s_j,\qquad
a_z=a_0-zI,\qquad
\eta(X)=\sum_j a_jXa_j^*,\quad
\rho(X)=\sum_j a_jXa_j.
\]
For an invertible matrix \(g\), define the completely positive map
\[
\Psi_g(X)=g\eta(X)g^*.
\]
Then the following finite certificate is equivalent to \(z\notin\sigma(T)\):
\[
a_z=g^{-1}+\rho(g),\qquad r(\Psi_g)<1.                 \tag{1}
\]
When it exists, \(g\) is unique and equals \(E((T-zI)^{-1})\).
The unique positive minimizer of C_F0126 is
\[
b_z=(I-\Psi_g)^{-1}(gg^*)
    =\sum_{k=0}^{\infty}\Psi_g^k(gg^*)>0.              \tag{2}
\]
Here \(r\) is the finite-dimensional spectral radius.
Equivalently the strict condition in (1) can be certified by a positive matrix \(Q\) satisfying \(Q-\Psi_g(Q)>0\).

**Proof.**
If \(z\) is in the resolvent set, the stationary identities and positive defect in C_F0127 give (1) with \(g=Y^*\) and
\(b_z-g\eta(b_z)g^*=gg^*>0\).
Similarity by \(b_z^{1/2}\) makes the map strictly subunital, proving its spectral radius is less than one.

Conversely suppose (1).
The convergent positive series (2) solves
\[
b_z=g(I+\eta(b_z))g^*.
\]
Put \(H=I+\eta(b_z)\) and \(Y=g^*\).
Then
\[
HYb_z^{-1}=g^{-1},\qquad HYb_z^{-1}+\rho(Y^*)=a_z.
\]
Thus \(Y\) is the unique inner optimizer from C_F0126.
Moreover
\[
H^{-1}-Yb_z^{-1}Y^*=0,\qquad Y^*HY=b_z.
\]
These identities make the envelope gradient (C_F0127, equation (3)) vanish exactly.
Hence \(b_z\) is a critical point.
C_F0127 implies bounded invertibility and identifies \(Y=E(((T-zI)^*)^{-1})\).
Its uniqueness statement proves uniqueness of both \(g\) and \(b_z\).

For the alternative certificate, a strict positive defect makes the CP map strictly subunital after conjugation and gives spectral radius less than one.
Conversely, if the spectral radius is less than one, \(Q=\sum_{k\ge0}\Psi_g^k(I)>0\) has defect \(I\).
This proves the equivalence.

This criterion replaces a global optimization by an algebraic matrix equation and a strict CP stability test.
The stability condition is essential: an arbitrary algebraic branch need not be the actual expected inverse.
It gives a sufficient Brown-support exclusion because Brown support lies in the operator spectrum; it does not by itself establish equality of those sets.
Strict inequalities can be verified with exact or interval arithmetic, but no numerical certification implementation is supplied here.

## 2. Explicit spectral regions when the pseudo-covariance vanishes

Assume \(\rho=0\).
Equation (1) forces \(g=a_z^{-1}\).
In particular,
\[
\sigma(T)=\sigma(a_0)\ \cup\
\left\{z\notin\sigma(a_0):
r\bigl(X\mapsto(a_0-zI)^{-1}\eta(X)(a_0-zI)^{-*}\bigr)\ge1\right\}.
                                                               \tag{3}
\]
No irreducibility or positive-capacity assumption is needed.
Points with singular \(a_z\) are in the spectrum because a certificate (1) would imply \(a_z=g^{-1}\).

For centered noise \(a_0=0\), this becomes the exact disk formula
\[
\sigma(T)=\{z\in\mathbb C:|z|\le\sqrt{r(\eta)}\}.       \tag{4}
\]
Indeed for \(z\ne0\) the CP map in (3) is \(|z|^{-2}\eta\), and \(z=0\) is always spectral.
Formula (4) includes \(r(\eta)=0\), when the spectrum is \(\{0\}\).

This is a direct corollary of C_F0127, not a claim that the spectral region is new in the circular-operator literature.
A literature comparison is required before any novelty statement.
The Brown measure is supported in the region (3); a Brown-support equality has not been proved in this draft.

There is also an exact exterior potential identity:
\[
u(z)=\frac1m\log|\det(a_0-zI)|,
\qquad z\notin\sigma(T),\quad \rho=0.                    \tag{4a}
\]
Indeed at the unique minimizer, \(Y=a_z^{-*}\) and
\(I+\eta(b_z)=a_zb_za_z^*\).
Hence the determinant ratio in C_F0126 is \(|\det a_z|^2\), while its mean energy is
\(\operatorname{Re}\operatorname{Tr}(a_z^*a_z^{-*})=m\), canceling the constant \(-m\).
This proof uses the attained variational value and does not assume the complement of the spectrum is connected.
Thus (4a) holds in every resolvent component, including bounded holes if present.

## 3. Brown masses enclosed by a resolvent contour

Let \(\Gamma\) be a positively oriented piecewise smooth simple closed curve contained in the resolvent set, and let \(\Omega\) be its bounded interior.
Let \(g_z\) be the unique solution of (1).
Then
\[
\mu_T(\Omega)=-\frac{1}{2\pi i}\int_\Gamma
                         \operatorname{tr}_m(g_z)\,dz.    \tag{5}
\]
Thus the total Brown mass of an isolated spectral component can be computed from the same finite stable branch, without differentiating a singular zero-regularization density in its interior.

**Proof.**
Write \(u(z)=\log\Delta_\varphi(T-zI)\).
The Brown logarithmic potential interface of C_F0123 identifies
\(u(z)=\int\log|z-w|\,d\mu_T(w)\).
Off the operator spectrum both the inverse and the potential are smooth.
If \(S=T-zI\), differentiation under the finite trace gives
\[
\partial_z u(z)=\tfrac12\varphi((S^*S)^{-1}(-S^*))
              =-\tfrac12\varphi(S^{-1})
              =-\tfrac12\operatorname{tr}_m(g_z).
\]
The trace derivative of the logarithm can be justified from its resolvent integral; cyclicity changes the Frechet derivative under the trace to \(\varphi(A^{-1}dA)\) for positive invertible \(A\).
Differentiating the logarithmic-potential representation instead gives
\[
-\operatorname{tr}_m(g_z)=\int\frac{1}{z-w}\,d\mu_T(w).
\]
The curve has positive distance from Brown support.
Integration and the scalar Cauchy integral formula prove (5), with no boundary mass.

This formula measures mass within any such contour, which may enclose more than one component.
It does not detect Brown mass inside a spectral region across which no resolvent contour can be drawn.

In the pseudo-covariance-zero case, equation (5) simplifies further:
\[
\mu_T(\Omega)=\frac{1}{m}
\#\{\text{eigenvalues of }a_0\text{ in }\Omega,
                              \text{ counted algebraically}\}. \tag{5a}
\]
In fact \(-g_z=(zI-a_0)^{-1}\), so the contour integral in (5) is the normalized finite-dimensional argument principle.
This also follows from (4a).
The exact Brown mass of every region bounded by such a resolvent contour is a multiple of \(1/m\) and agrees with the deterministic mean's eigenvalue count.
Individual Brown atoms are not claimed to have this value unless an isolating contour or other argument justifies the passage to the point.

## 4. Circle means recover disk masses and Brown atoms

For a fixed center \(z_0\), define the circle mean directly through the variational objective \(\mathcal V_z\) of C_F0126:
\[
M_{z_0}(r)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+re^{i\theta})\,d\theta
=\frac{1}{4\pi m}\int_0^{2\pi}
             \inf_{b>0}\mathcal V_{z_0+re^{i\theta}}(b)\,d\theta.
                                                               \tag{6}
\]
For every \(r>0\), the mean is finite and equals
\[
M_{z_0}(r)=\int\log\max\{r,|w-z_0|\}\,d\mu_T(w).       \tag{7}
\]
Consequently \(N(t)=M_{z_0}(e^t)\) is convex and its one-sided derivatives are
\[
N'_-(t)=\mu_T(\{|w-z_0|<e^t\}),\qquad
N'_+(t)=\mu_T(\{|w-z_0|\le e^t\}).                       \tag{8}
\]
In particular
\[
\mu_T(\{z_0\})=
\lim_{r\downarrow0}\frac{M_{z_0}(r)}{\log r}
=\lim_{r\downarrow0}\bigl(M_{z_0}(r)-M_{z_0}(r/e)\bigr).
                                                               \tag{9}
\]

**Proof.**
The scalar mean-value calculation for \(\log|z-w|\) gives
\((2\pi)^{-1}\int\log|z_0+re^{i\theta}-w|\,d\theta
=\log\max\{r,|w-z_0|\}\).
Compactness of Brown support controls the positive part.
The negative angular integral is uniformly bounded for fixed \(r>0\), by this identity and the positive-part bound, so the change in integration order is legitimate and (7) is finite.
This calculation also proves (7) even when the potential is negative infinity at individual circle points.

Writing \(s=\log|w-z_0|\), with \(s=-\infty\) at the center, (7) is \(N(t)=\int\max\{t,s\}\,d\mu_T\).
The left and right derivatives of the integrand are the indicators of \(s<t\) and \(s\le t\).
Bounded convergence gives (8).
As \(t\to-\infty\), \(\max(t,s)/t\) tends to the center indicator and is uniformly bounded after choosing a sufficiently negative starting \(t\), because support is compact.
This gives the first limit in (9).
The second follows by bounded convergence applied to \(\max(t,s)-\max(t-1,s)\), which lies in \([0,1]\).

The infimum in (6) is taken separately at each angle.
There is no justified exchange with an infimum over one common trial matrix.
Equations (6)-(9) need no absolute continuity, no support/spectrum equality, and no interchange of a limiting density with a derivative.
They are potential-theoretic consequences of the main theorem, not new Brown-measure foundations.

## 5. Regularization measures kernel mass, not Brown atom mass

For \(S=T-z_0I\), the regularized minimizer is
\[
b_\varepsilon=E((S^*S+\varepsilon^2I)^{-1}).
\]
Finite spectral calculus gives
\[
\lim_{\varepsilon\downarrow0}\varepsilon^2
          \operatorname{tr}_m(b_\varepsilon)
=\varphi(1_{\{0\}}(S^*S)).                               \tag{10}
\]
Likewise, for the regularized potential in C_F0126,
\[
\lim_{\varepsilon\downarrow0}
       \frac{\log\Delta_\varepsilon(S)}{\log\varepsilon}
=\varphi(1_{\{0\}}(S^*S)).                               \tag{11}
\]
For (10), the scalar integrands \(\varepsilon^2/(x+\varepsilon^2)\) lie in \([0,1]\) and tend to the indicator of zero.
For (11), use the singular-value distribution and divide \(\frac12\log(x+\varepsilon^2)\) by \(\log\varepsilon\); compact support gives a uniform bound and the same pointwise limit.

These are singular-value/kernel quantities.
They need not equal the Brown mass at \(z_0\).
The deterministic example allowed by C_F0126,
\[
T=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad z_0=0,
\]
has normalized kernel dimension \(1/2\), whereas its Brown measure is \(\delta_0\).
Indeed \(u(z)=\frac12\log|\det(T-zI)|=\log|z|\), so the Brown atom has mass one; but \(T^*T=\operatorname{diag}(0,1)\), so (10)-(11) give one half.

Nor does \(u(z_0)=-\infty\) by itself generally identify a Brown atom: for a general compactly supported probability measure a nonatomic distribution can have nonintegrable negative logarithmic moment at a point.
Formula (9) is the appropriate unconditional atom interface.
The next section proves that this particular matrix-pencil class has at most finitely many possible infinite-potential points, without asserting that each is an atom.

## 6. All possible Brown atoms lie among the deterministic mean eigenvalues

This argument was proposed by the coordinating agent and checked and written here.
It applies to arbitrary complex coefficients, with no pseudo-covariance or capacity assumption.

**Proposition.**
For \(T=a_0+\sum_j a_j\otimes s_j\),
\[
\det(a_0-zI)\ne0
\quad\Longrightarrow\quad
\log\Delta_\varphi(T-zI)>-\infty.                         \tag{12}
\]
Consequently every Brown atom lies in the finite set \(\sigma(a_0)\), so there are at most \(m\) possible atom locations.
In the centered case \(a_0=0\), the determinant is positive at every nonzero shift and zero is the only possible Brown atom.
No quantization of the atom weights is asserted.

**Step 1: centered potentials are monotone along each ray.**
Let
\(T_0=\sum_j a_j\otimes s_j\), with the real-linear positive definite inner operator \(\mathcal T_b\) from C_F0126.
For \(z=re^{i\theta}\), \(r\ge0\), the source in the inner solve is \(-re^{i\theta}I\).
Real homogeneity gives
\[
\operatorname{Re}\operatorname{Tr}
  \bigl((-re^{i\theta}I)^*\mathcal T_b^{-1}(-re^{i\theta}I)\bigr)
 =r^2 q_\theta(b),\qquad q_\theta(b)\ge0.
\]
All other objective terms are independent of \(r\).
Therefore
\[
u_0(re^{i\theta})=\frac1{2m}\inf_{b>0}
 \{\log\det(I+\eta(b))-\log\det b-m+r^2q_\theta(b)\}
                                                               \tag{13}
\]
is nondecreasing in \(r\) for each fixed angle, including extended-real values.

**Step 2: a compactly supported logarithmic potential is integrable on every nontrivial line segment.**
Rotate and parametrize the segment as \(e^{i\theta}r\), \(r\in I=[\alpha,\beta]\), with \(\alpha<\beta\).
For any \(w\in\mathbb C\),
\[
|re^{i\theta}-w|\ge |r-\operatorname{Re}(e^{-i\theta}w)|.
\]
Since \(x\mapsto\log^-x=\max\{-\log x,0\}\) is nonincreasing,
\[
\int_I\log^-|re^{i\theta}-w|\,dr
\le\int_{-1}^1-\log|t|\,dt=2.                            \tag{14}
\]
This bound is uniform in \(w\).
On a compact set of \(w\), the positive logarithmic part is also uniformly bounded on the fixed segment.
Tonelli's theorem for the negative part, followed by the positive bound, shows that the logarithmic potential of any compactly supported probability measure belongs to \(L^1(I)\).
It may be negative infinity at particular points, but not at every point of a nontrivial segment.

If \(u_0(r_0e^{i\theta})=-\infty\) for some \(r_0>0\), monotonicity in (13) implies \(u_0(re^{i\theta})=-\infty\) throughout \(r\in[r_0/2,r_0]\).
This contradicts (14) applied to the Brown potential representation from C_F0123.
Thus \(u_0(z)>-\infty\) for every \(z\ne0\).

**Step 3: reduce an invertible deterministic shift to the centered case.**
Suppose \(A=a_0-zI\) is invertible.
Then
\[
T-zI=A(I+C),\qquad C=\sum_j A^{-1}a_j\otimes s_j.
\]
The transformed \(C\) is another centered pencil of the same class, so Step 2 at the nonzero shift \(-1\) gives \(\log\Delta(I+C)>-\infty\).
Let \(c>0\) be the smallest singular value of \(A\).
With \(B=I+C\),
\[
(AB)^*(AB)\ge c^2 B^*B.
\]
Add \(\varepsilon^2I\), apply operator monotonicity of logarithm and the normalized finite trace, and let \(\varepsilon\downarrow0\).
This yields
\[
\log\Delta(T-zI)\ge\log c+\log\Delta(I+C)>-\infty,
\]
proving (12).
This comparison avoids requiring a separate determinant-multiplicativity theorem for the deduction.

Finally any Brown atom of positive mass at \(z\) forces the logarithmic potential at \(z\) to be negative infinity: the atom contributes its mass times \(\log0\), and the remaining positive part is bounded by compactness.
Thus (12) confines all atoms to \(\sigma(a_0)\).

The proposition locates possible atoms only.
It does not assert that each deterministic eigenvalue carries an atom, that determinant zero implies an atom, or that an atom has mass in \(m^{-1}\mathbb Z\).
The contour mass quantization in (5a) has the extra hypothesis \(\rho=0\) and an actual isolating resolvent contour.
A separate positive-capacity lower bound removes all atoms when \(\operatorname{cap}(\eta)>0\).

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
| dependency | [Exact input](Yin_C_F0126_v1.md#setting-and-primary-unregularized-formula) | Unrestricted finite variational objective, positive inner real-linear energy and unique physical regularized optimizer. |
| dependency | [Exact input](Yin_C_F0127_v1.md#what-a-critical-point-forces) | Stationary Stein identities, exact positive defect and bounded-inverse attainment/critical-point equivalence. |
| dependency | [Exact input](Yin_C_F0123_v1.md#brown-measure-and-the-local-source-boundary) | Accepted Brown logarithmic potential, compact support, trace convention and containment in the operator spectrum; no general equality. |

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
| dependency | [Exact material](Yin_C_F0126_v1.md#setting-and-primary-unregularized-formula) | Unrestricted finite variational objective, positive inner real-linear energy and unique physical regularized optimizer. |
| dependency | [Exact material](Yin_C_F0127_v1.md#what-a-critical-point-forces) | Stationary Stein identities, exact positive defect and bounded-inverse attainment/critical-point equivalence. |
| dependency | [Exact material](Yin_C_F0123_v1.md#brown-measure-and-the-local-source-boundary) | Accepted Brown logarithmic potential, compact support, trace convention and containment in the operator spectrum; no general equality. |
| review | [Actual finding](../audits/reviews/Yin_R_F0177_v1.md#resolvent-mass-finding) | Whole affine branch and mass argument: equivalent strict CP-stable finite resolvent certificate and unique physical branch; rho=0 spectral region/exterior determinant and contour eigenvalue mass; circle means and atoms; singular-value kernel limits and nilpotent distinction; all possible Brown atoms confined to deterministic mean eigenvalues. Each extra hypothesis and negative boundary retained. |

