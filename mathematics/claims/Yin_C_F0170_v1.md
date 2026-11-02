---
author: Yin
---

# Radial Brown mass and degenerate spectral disks for zero pseudo-covariance pencils

## Current assessment
[Selected decision](#decision-adopted-retained-proof)

## Exact retained scope and provenance

<a id="statement"></a>

For centered finite complex semicircular pencils with pseudo-covariance identically zero, retain the concave squared-radius envelope, all radial cumulative-mass formulas, absence of positive-radius circle atoms and every other singular component away from zero, local density bounds, regularized-minimizer slope reconstruction and exact full operator spectral disk.
Positive covariance capacity additionally removes the possible origin atom and gives planar absolute continuity.
No irreducibility or flatness is assumed.
No equality of Brown support with the full spectral disk or uniform convergence rate is asserted.
The complete fixed argument and original mathematical development are [retained below](#argument), including the historical author checks and status statements.
The complete formal self-review, its actual date and checking limits are retained in [R_F0177](../audits/reviews/Yin_R_F0177_v1.md#radial-mass-finding).
This placement preserves existing mathematics; it selects no Task, objective change, new theorem role, novelty or publication claim.

Dated candidate, “draft,” author-check and unadopted-status sentences within the retained text describe the original development.
The selected current decision above owns the present mathematical adoption and exact review evidence.

## Complete retained argument

<a id="argument"></a>

## 1. Setting and a concave radial envelope

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state.
Let \(s_j\) be free standard semicircular elements and let
\[
 T=\sum_j a_j\otimes s_j\in M_m(M),\qquad
 \eta(X)=\sum_j a_jXa_j^*,\qquad
 \rho(X)=\sum_j a_jXa_j=0\quad\text{for every }X.
\]
Use \(\varphi=\operatorname{tr}_m\otimes\tau\), with \(\operatorname{tr}_m=\operatorname{Tr}/m\).
No positivity-improving, irreducibility, invertibility, or positive-capacity assumption is imposed on \(\eta\).
A model of this type is \(T=\sum_k b_k\otimes c_k\), where the \(c_k\) are free standard circular elements; then \(\eta(X)=\sum_k b_kXb_k^*\).
The argument only needs the displayed vanishing of \(\rho\), rather than a chosen circular representation.

For \(R>0\), set
\[
 H_R=I+\eta(R),\quad
 A(R)=\log\det H_R-\log\det R-m,\quad
 B(R)=\operatorname{Tr}(H_R^{-1}R)>0.
\]
At mean \(a=-zI\), the inner equation of C_F0126 has the explicit solution
\[
 Z_R=-zH_R^{-1}R.
\]
Consequently
\[
 u(z):=\log\Delta_\varphi(T-zI)=f(|z|^2),\qquad
 f(s)=\frac1{2m}\inf_{R>0}\{A(R)+sB(R)\}.                 \tag{1}
\]
Thus \(f\) is nondecreasing and concave as a function of the squared radius \(s\).
These are direct properties of an infimum of affine functions with positive slope.
They are not consequences of ordinary joint convexity of the matrix objective.

The potential/Brown-measure interface and its normalization are reused from [C_F0123](Yin_C_F0123_v1.md#brown-measure-and-the-local-source-boundary):
\[
 \mu_T=\frac1{2\pi}\Delta_z u,
\]
where \(\mu_T\) is a compactly supported probability measure.
In particular \(\mu_T\) is rotation invariant.
Its logarithmic potential equals \(u\), with the equality fixed by the normalization at infinity.
Averaging the logarithmic kernel over angles gives, for \(s>0\),
\[
 f(s)=\frac12\int_{[0,\infty)}\log\max\{s,t\}\,d\nu(t),
 \qquad \nu=(w\mapsto |w|^2)_\#\mu_T.                    \tag{2}
\]
For completeness, the angular identity is
\(\frac1{2\pi}\int_0^{2\pi}\log|r-te^{i\theta}|\,d\theta=\log\max\{r,t\}\), obtained by factoring out the larger radius and integrating the convergent logarithmic Fourier series, with the equal-radius case by an integrable limit.
Compact support makes (2) finite for every \(s>0\).
The potential identity also follows distributionally and then pointwise from the canonical subharmonic representatives and their common normalization.
The value at zero may be \(-\infty\).

## 2. Radial mass, absence of circle singularities, and density bounds

Let
\[
 F(s)=\nu([0,s])=\mu_T(\{w:|w|^2\le s\}),\qquad s>0.
\]
The one-sided derivatives computed from (2) are
\[
 f'_-(s)=\frac{\nu([0,s))}{2s},\qquad
 f'_+(s)=\frac{\nu([0,s])}{2s}.                            \tag{3}
\]
Concavity gives \(f'_-(s)\ge f'_+(s)\), whereas the measure inequality gives the reverse.
Therefore \(\nu(\{s\})=0\) at every \(s>0\), \(f\) is continuously differentiable on \((0,\infty)\), and
\[
 F(s)=2s f'(s),\qquad \frac{F(s)}s=2f'(s)\text{ is nonincreasing}.
                                                               \tag{4}
\]
Thus there is no Brown mass on a circle of positive radius.
There may be an atom at zero.

There is a stronger local conclusion.
In the sense of measures on \((0,\infty)\),
\[
 dF=2f'(s)\,ds+2s\,df'(s).
\]
Here \(dF\ge0\), since \(F\) is a distribution function, and \(df'\le0\), since \(f\) is concave.
Hence
\[
 0\le dF\le 2f'(s)\,ds.
\]
This domination proves local absolute continuity of \(F\) and the almost-everywhere inequalities
\[
 0\le F'(s)\le\frac{F(s)}s\le\frac1s.                    \tag{5}
\]
An elementary alternative confirms this conclusion without differentiating measures.
For \(0<s_1<s_2\), monotonicity of \(F(s)/s\) gives
\[
 0\le F(s_2)-F(s_1)
 \le(s_2-s_1)\frac{F(s_1)}{s_1}
 \le\frac{s_2-s_1}{s_1}.
\]
Thus \(F\) is Lipschitz on every compact subinterval of \((0,\infty)\), and passing to derivatives gives (5) directly.
Either this argument or the preceding measure domination proves the local absolute continuity used below.

It also proves \(f\in C^{1,1}_{\mathrm{loc}}((0,\infty))\): solve the preceding measure identity for \(df'\), and use boundedness of \(f'\) and \(1/s\) on each compact positive interval.
Writing \(\alpha=\mu_T(\{0\})\), the entire Brown measure therefore has the form
\[
 \mu_T=\alpha\delta_0+\frac1\pi F'(|z|^2)\,d^2z,
 \qquad
 0\le\frac1\pi F'(|z|^2)
       \le\frac{F(|z|^2)}{\pi|z|^2}
       \le\frac1{\pi|z|^2}\quad\text{a.e. }z\ne0.        \tag{6}
\]
The coefficient \(1/\pi\) follows from \(d^2z=\frac12\,ds\,d\theta\).
The atom is recovered by
\[
 \alpha=\lim_{s\downarrow0}F(s)=\lim_{s\downarrow0}2s f'(s).
\]
There is no assertion of a finite density bound at zero.

If in addition \(\operatorname{cap}(\eta)>0\), the atomlessness consequence in [C_F0172, Section 2](Yin_C_F0172_v1.md#2-positive-covariance-capacity-excludes-every-brown-atom-for-every-mean) excludes the remaining atom at zero.
Combining it with (6) gives the direct corollary
\[
 \rho=0\ \text{and}\ \operatorname{cap}(\eta)>0
 \quad\Longrightarrow\quad \mu_T\ll d^2z.
\]
Indeed C_F0126 gives \(u(0)=\frac1{2m}\log\operatorname{cap}(\eta)-\frac12> -\infty\), whereas an atom at zero would make the compactly supported logarithmic potential there equal to \(-\infty\).
Together with the already proved absence of every other singular component, this establishes planar absolute continuity of the whole Brown measure.
This corollary is for the centered pencil under the standing \(\rho=0\) hypothesis; the atomlessness result alone does not prove planar absolute continuity for general nonzero \(\rho\) or for arbitrary non-scalar deterministic drift.
The combined corollary remains a self-checked draft deduction with the same review limits as its inputs.

Every disk of positive radius has positive Brown mass.
Indeed, if \(F(s_0)=0\) for some \(s_0>0\), then (4) and nonnegativity force \(F(s)/s=0\) for all \(s\ge s_0\), contradicting total mass one.
In particular zero lies in the Brown support.
These arguments do not rule out an annular gap at positive radii.
Nor does monotonicity of the average density \(F(s)/(\pi s)\) imply monotonicity of the pointwise density \(F'(s)/\pi\).

For the last logical distinction, an abstract radial distribution can have
\[
 F(s)=\begin{cases}
 0.4s,&0\le s\le1,\\
 0.3+0.1s,&1\le s\le2,\\
 0.1+0.2s,&2\le s\le4.5,\\
 1,&s\ge4.5.
 \end{cases}
\]
Then \(F(s)/s\) is nonincreasing but the density increases at \(s=2\).
This is solely a counterexample to that inference from concavity; it is not asserted to be realized by one of the present pencils.

## 3. Radial mass from regularized minimizers without differentiation in z

For \(\varepsilon>0\), write
\[
 f_\varepsilon(s)=\log\Delta_\varepsilon(T-zI),\qquad s=|z|^2.
\]
The regularized C_F0126 formula becomes
\[
 f_\varepsilon(s)=\frac1{2m}\min_{Q>0}
 \left\{\log\det C_Q-\log\det Q+\operatorname{Tr}Q-m
       +s\operatorname{Tr}(C_Q^{-1}Q)\right\},
 \quad C_Q=\varepsilon^2I+\eta(Q).                          \tag{7}
\]
It has the unique minimizer
\[
 Q_\varepsilon(s)=\varepsilon^2 E\left[
  ((T-zI)^*(T-zI)+\varepsilon^2I)^{-1}\right],
 \qquad E=\operatorname{id}\otimes\tau.
\]
The objective depends only on \(s\), so uniqueness makes this matrix independent of the argument of \(z\).
Uniform coercivity on bounded \(s\)-intervals and uniqueness justify the ordinary envelope derivative:
\[
 f'_\varepsilon(s)=\frac1{2m}
           \operatorname{Tr}(C_{Q_\varepsilon}^{-1}Q_\varepsilon).
                                                               \tag{8}
\]
One can see the envelope step directly by evaluating the objective at the two neighboring unique minimizers.
Compact sublevel bounds imply convergence of minimizers as the parameter varies; the resulting two difference-quotient bounds have the same limit.

Set
\[
 R_\varepsilon(s)=\varepsilon^{-2}Q_\varepsilon(s)
   =E\left[((T-zI)^*(T-zI)+\varepsilon^2I)^{-1}\right].
\]
Then \(C_{Q_\varepsilon}=\varepsilon^2(I+\eta(R_\varepsilon))\).
Since \(f_\varepsilon\downarrow f\), every \(f_\varepsilon\) is concave, and \(f\) is differentiable at all positive \(s\), their derivatives converge there.
This follows by bounding each derivative between left and right secant slopes at a fixed increment, sending \(\varepsilon\) to zero, and then sending the increment to zero.
Combining (4) and (8) gives
\[
 F(s)=\frac{s}{m}\lim_{\varepsilon\downarrow0}
   \operatorname{Tr}\left[(I+\eta(R_\varepsilon(s)))^{-1}
                             R_\varepsilon(s)\right],\quad s>0.
                                                               \tag{9}
\]
This reconstructs the radial cumulative Brown mass from matrix minimizers, without differentiating either a numerical potential or a Dyson system.
The matrix \(R_\varepsilon\) may diverge in norm on the spectrum; the scalar combination in (9) still has the asserted finite limit.
No convergence rate is supplied.

The positive physical Schur complement in L_F0032 gives
\(C_{Q_\varepsilon}^{-1}-sC_{Q_\varepsilon}^{-1}
 Q_\varepsilon C_{Q_\varepsilon}^{-1}>0\), so the finite-regularization quantity on the right of (9), before taking its limit, lies strictly between zero and one for \(s>0\).
This is an additional normalization check.

## 4. Exact centered spectrum from the attainment theorem

Let \(r(\eta)\) denote the spectral radius of the complex-linear map \(\eta:M_m(\mathbb C)\to M_m(\mathbb C)\).
Then
\[
 \sigma(T)=\{z\in\mathbb C:|z|^2\le r(\eta)\}.             \tag{10}
\]
No irreducibility is needed.
To prove this, C_F0127 identifies resolvent points with critical points of the C_F0126 objective.
At such a critical point it proves
\[
 a=Y^{-*}+\rho(Y^*),\qquad R=Y^*(I+\eta(R))Y.
\]
For \(\rho=0\) and \(a=-zI\), the first equation forces \(z\ne0\) and \(Y=-I/\bar z\).
The second becomes
\[
 (s\operatorname{Id}-\eta)R=I,\qquad R>0,\quad s=|z|^2.
                                                               \tag{11}
\]
If \(s>r(\eta)\), the convergent positive series
\[
 R=\sum_{k=0}^\infty\frac{\eta^k(I)}{s^{k+1}}>0            \tag{12}
\]
solves (11).
With \(Y=-I/\bar z\), it satisfies the inner equation and the critical equation of C_F0127 (the auxiliary matrix \(P\) in its equation (3) is zero).
Thus it is the unique minimizer, and \(z\) belongs to the resolvent.

Conversely, if (11) has a positive solution, the map
\[
 \Psi(X)=s^{-1}R^{-1/2}\eta(R^{1/2}XR^{1/2})R^{-1/2}
\]
is completely positive and obeys
\(\Psi(I)=I-s^{-1}R^{-1}<I\).
Hence \(r(\Psi)\le\|\Psi\|=\|\Psi(I)\|<1\).
Similarity gives \(r(\Psi)=r(\eta)/s\), proving \(s>r(\eta)\).
At \(z=0\), the critical relation \(a=Y^{-*}\) is impossible, so zero always lies in the spectrum.
This includes \(r(\eta)=0\), when the spectrum is exactly \(\{0\}\) and the Brown measure is \(\delta_0\).

At the minimizer for \(s>r(\eta)\), \(H_R=sR\), and direct substitution yields
\[
 f(s)=\tfrac12\log s,\qquad F(s)=1.
\]
Equation (10) concerns the full operator spectrum.
Sections 1--3 alone do not prove that the Brown support fills every point of that disk when \(r(\eta)>0\).

## 5. Deterministic drift: companion derivation

The collaborating brown_envelope agent identified the extension to deterministic drift, and the brown_boundaries agent develops the complete general resolvent certificate, zero-pseudo-covariance spectral-radius test, exterior determinant, and component-mass consequences in [C_F0171](Yin_C_F0171_v1.md).
The centered criterion in Section 4 is its direct specialization.
This draft owns the radial envelope and its Brown consequences; the companion owns the general affine derivation.

## 6. Elementary checks

For a scalar circular variable with variance \(v>0\), \(\eta(R)=vR\).
Formula (1) can be minimized by setting \(t=v+1/R>v\):
\[
 f(s)=\frac12\inf_{t>v}\{\log t-1+s/t\}
 =\begin{cases}
 \frac12(\log v-1+s/v),&0\le s\le v,\\
 \frac12\log s,&s\ge v.
 \end{cases}
\]
Thus \(F(s)=\min\{s/v,1\}\), recovering the uniform disk of radius \(\sqrt v\), with the correct normalization.
When \(\eta=0\), \(T=0\), \(f(s)=\frac12\log s\) and \(\mu_T=\delta_0\); the atom at zero must therefore be permitted.
More generally \(T=\operatorname{diag}(c,0)\) yields a mixture of half the standard circular law and half an atom at zero.

Equations (1), (6), (9), and (10) apply to centered zero-pseudo-covariance pencils.
The companion drift criterion is useful even when radial symmetry is absent.
No newness claim is justified by this derivation.

## 7. Bounded literature comparison and review limits

The retained complete circular proof C_F0167 supplies the regularized minimum and its physical Schur positivity.
C_F0123 supplies the accepted Brown-potential and weak-regularization interface.
The proof above uses these inputs and C_F0126/C_F0127; it does not assume a scalar R-diagonal representation of a matrix-valued circular pencil.

The original [AK20 source reading](../audits/literature/AK20/Yin_U001.md#ak20-u001) records the targeted primary-source check of Alt and Krueger, *Inhomogeneous Circular Law for Correlated Matrices*, author preprint dated 2021-02-25, [arXiv:2005.13533](https://arxiv.org/pdf/2005.13533).
Proposition 2.9, printed p. 8 / PDF p. 8, imposes two-sided flatness \(c\operatorname{tr}_m(R)I\le\eta(R)\le C\operatorname{tr}_m(R)I\) for positive \(R\), and identifies the Brown density with Theorem 2.5.
The latter gives analyticity and positive upper/lower bounds in the disk under those hypotheses.
Those statements are related established results with stronger regularity and stronger covariance assumptions; they do not directly cover the possibly degenerate maps retained here.
Only those statement passages were checked, not the full paper or its proof.
The article is not a mathematical proof dependency of this draft, and this scoped search does not establish novelty or priority for any present formulation.

Self-check covered all constants, the two one-sided derivative directions, the domination of radial derivative measures, the rescaling \(Q_\varepsilon=\varepsilon^2R_\varepsilon\), the zero/noise-free cases, and necessity as well as sufficiency in the centered spectral-radius criterion.
No independent review or convergence rate has been completed.

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
| dependency | [Exact input](Yin_C_F0126_v1.md#setting-and-primary-unregularized-formula) | Whole variational formula and positive real-linear inner solve; its regularized unique optimizer is used for radial slopes. |
| dependency | [Exact input](Yin_C_F0127_v1.md#what-a-critical-point-forces) | Critical point identities and bounded-inverse equivalence used for the exact centered spectral disk. |
| dependency | [Exact input](Yin_C_F0123_v1.md#brown-measure-and-the-local-source-boundary) | Accepted compactly supported Brown potential, normalization and weak regularization, without a general support/spectrum equality. |
| dependency | [Exact input](Yin_C_F0167_v1.md#argument) | Existing circular physical Schur positivity at positive regularization; no unrestricted covariance extension is inferred. |

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
| dependency | [Exact material](Yin_C_F0126_v1.md#setting-and-primary-unregularized-formula) | Whole variational formula and positive real-linear inner solve; its regularized unique optimizer is used for radial slopes. |
| dependency | [Exact material](Yin_C_F0127_v1.md#what-a-critical-point-forces) | Critical point identities and bounded-inverse equivalence used for the exact centered spectral disk. |
| dependency | [Exact material](Yin_C_F0123_v1.md#brown-measure-and-the-local-source-boundary) | Accepted compactly supported Brown potential, normalization and weak regularization, without a general support/spectrum equality. |
| dependency | [Exact material](Yin_C_F0167_v1.md#argument) | Existing circular physical Schur positivity at positive regularization; no unrestricted covariance extension is inferred. |
| review | [Actual finding](../audits/reviews/Yin_R_F0177_v1.md#radial-mass-finding) | Whole centered rho=0 argument: radial concave envelope, logarithmic-potential representation, all one-sided slopes, absence of positive-radius atoms, local absolute continuity and density bounds, positive-capacity whole-measure absolute continuity, regularized-minimizer reconstruction and exact operator spectral disk including degenerate maps. No Brown-support/full-disk equality or convergence rate. |

