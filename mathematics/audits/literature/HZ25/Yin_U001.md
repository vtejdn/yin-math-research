---
author: Yin
---

# HZ25-U001: Regular-bulk Haar additive local laws and ultra-small logarithms

<a id="hz25-u001"></a>
## Edition, passages and acceptance scope

The exact mathematical edition is the [retained arXiv v4](../../../literature/pdf/HZ25--arxiv-v4.pdf), identified in [the edition note](readme.md).
The selected 2026-11-05 inspection covers the hypotheses and statements of Propositions 2.1--2.2, Theorems 2.3, 2.8, 3.2 and 4.1, and Lemmas 4.3--4.4, with the critical probability-to-integral proof of Lemma 4.4 read through its three ranges.
PDF pages 9, 12, 15, 18 and 19 were visually inspected; the supplied contents and title page on p. 1 were also inspected.
The original proofs of the cited free-probability continuity inputs, the Bao--Erdos--Schnelli local law, and the Rudelson--Vershynin bound are accepted external inputs, not independently re-audited here.
The selected source results are accepted at their exact statements for the bounded deterministic Haar-additive application below.
This is source preparation by a proof developer, not independent review of a resulting project Claim.

<a id="model-and-local-law"></a>
## Model, normalization and exact local law

In Section 2.3, PDF pp. 11--12, the model is
\[
 X_N=U_N\Sigma_NV_N^*+\Xi_N,
 \qquad \|\Sigma_N\|,\|\Xi_N\|\le C,
\]
with independent Haar unitary matrices and deterministic deformations.
The matrix \(H_N=\begin{pmatrix}0&X_N\\X_N^*&0\end{pmatrix}\) has normalized spectral law on dimension \(2N\).
The measures \(\mu_\Sigma,\mu_\Xi\) denote the positive singular-value empirical laws with normalization \(1/N\), and a tilde means symmetrization.
The Cauchy transform convention is \(G_\rho(z)=\int(z-t)^{-1}\,d\rho(t)\).

<a id="regular-bulk-definition"></a>
### Regular bulk of a free additive convolution

Definition 2.7, PDF p. 12, takes two Borel probability measures \(\nu_1,\nu_2\) on \(\mathbb R\), neither a point mass, and denotes by \(f_{\nu_1\boxplus\nu_2}\) the density function of the absolutely continuous part of their free additive convolution.
It defines the bulk by
\[
 \mathcal B_{\nu_1\boxplus\nu_2}
 =\{x\in\mathbb R:
      0<f_{\nu_1\boxplus\nu_2}(x)<\infty,
      \ (\nu_1\boxplus\nu_2)(\{x\})=0\}.
\]
Both the finite positive density condition and the exclusion of an atom at the same point belong to this definition.
The local-law application uses this set for \(\nu_1=\widetilde\delta_1\), \(\nu_2=\widetilde\mu\), and the point \(x=0\); it is distinct from the planar Brown-measure region \(D(T,a)\) defined below.

Theorem 2.8, PDF p. 12, assumes compact limiting probability measures \(\mu_\sigma,\mu_\xi\) on \([0,\infty)\), neither symmetrization a point mass, and at least one symmetrization supported at more than two points.
Fix \(L>0\) and a compact interval \(I\) in the regular bulk of \(\widetilde\mu_\sigma\boxplus\widetilde\mu_\xi\).
Its fixed-neighborhood hypothesis and conclusion are
\[
 \sup_{N\ge N_0}\{d_{\rm L}(\mu_\Sigma,\mu_\sigma)
                    +d_{\rm L}(\mu_\Xi,\mu_\xi)\}\le2b,
 \qquad 0<b\le b_0,
\]
\[
 \left|G_{H_N}(z)-G_{\widetilde\mu_\Sigma\boxplus\widetilde\mu_\Xi}(z)\right|
 \prec\frac1{N\eta(1+\eta)},
 \quad z=x+i\eta,\quad x\in I,\quad0<\eta\le N^L.
 \tag{Local}
\]
The listed dependencies are the limiting measures, \(I,L\), and the uniform norm bound; no quantitative rate of convergence of input empirical measures is imposed.
The comparison is with the free convolution of the finite-dimensional empirical input laws, rather than directly with the limiting convolution.

<a id="stochastic-domination-definition"></a>
### Stochastic domination and uniform parameters

For two sequences \(X_N,Y_N\) of nonnegative random variables, Definition 2.6 on the same page specifies
\[
 X_N\prec Y_N
 \quad\Longleftrightarrow\quad
 \forall\varepsilon>0\ \forall D>0:\ 
 \mathbb P\{X_N>N^\varepsilon Y_N\}\le N^{-D}
\]
for all sufficiently large \(N\), with the usual small-positive and large-positive exponent ranges sufficient.
Uniformity in a parameter means that its threshold \(N_0(\varepsilon,D)\) is independent of that parameter.
Passing to an event simultaneous over a finite grid still requires the corresponding union bound.

Theorem 4.1, PDF pp. 15--17, applies the preceding law to
\[
 Y_N=U_N\Sigma_NV_N^*+A_N,
 \qquad A_N\to a,\quad\Sigma_N\to\sigma
 \quad\text{in star distribution},
 \qquad \|A_N\|,\|\Sigma_N\|\le M.
\]
For the regular region \(D^{(\epsilon)}(T,a)\) and each fixed \(L_0>0\), it states
\[
 \sup_{\lambda\in D^{(\epsilon)}(T,a)}
 |G^\lambda(i\eta)-G_{\widetilde\mu_\Sigma\boxplus\widetilde\mu_{|A_N-\lambda|}}(i\eta)|
 \prec\frac1{N\eta},\qquad \eta>N^{-L_0}.
 \tag{Deformed-local}
\]
The local use at one fixed parameter can instead invoke Theorem 2.8 directly, requiring only its singular-law neighborhood.
The source's global eigenvalue convergence theorems are stated in probability and do not themselves assert summable full almost-sure logarithmic convergence.

<a id="subordination-neighborhood"></a>
## Bulk condition and subordination continuity

Proposition 2.2 on PDF p. 9 says that if \(a_N\to a\) and \(\sigma_N\to\sigma\ge0\) in star distribution, then the subordination functions for \(\widetilde\mu_{|a_N-\lambda|}\boxplus\widetilde\mu_{\sigma_N}\) converge uniformly on compact parameter sets whenever both limiting subordination functions are bounded there.
Proposition 2.1 supplies their continuous boundary extensions.
The exact relation from (2.1) is
\[
 G_{\mu_1\boxplus\mu_2}(z)
   =\bigl(\omega_1(z)+\omega_2(z)-z\bigr)^{-1}.
\]
The displayed denominator in the proof of Lemma 4.3 on p. 18 repeats \(\omega_1\); the consuming argument uses the two-index identity above.
This local displayed-index issue does not alter the stated propositions or estimates.

For an R-diagonal \(T\) free from \(a\), formulas (2.4)--(2.6), Theorem 2.3 and Definition 2.4 on PDF p. 10 use
\[
 \Omega(T,a)=\{\lambda:
   \|(a-\lambda)^{-1}\|_2\|T\|_2>1,
   \quad\|a-\lambda\|_2\|T^{-1}\|_2>1\},
\]
\[
 S(T,a)=\{\lambda:
  \widetilde\mu_{|a-\lambda|}(\{0\})+
  \widetilde\mu_{|T|}(\{0\})\ge1\},
 \qquad D(T,a)=\Omega(T,a)\setminus S(T,a).
\]
In \(D(T,a)\), the density of the singular symmetrization at zero is finite and positive, and both subordination values at zero are finite with positive imaginary part.
The set \(D^{(\epsilon)}\) restricts the absolute values of these two values to \((\epsilon,\epsilon^{-1})\).
At \(T\) Haar, \(|T|=1\), so two strict squared-norm inequalities for a deformation put zero in this regular region provided the exceptional atom condition is excluded.

For measures supported in a common compact interval, weak convergence implies moment convergence.
Thus Proposition 2.2 at \(\lambda=0\) and \(z\in i[0,1]\), with a compactness contradiction, gives a fixed weak neighborhood in which the corresponding empirical free-convolution Cauchy transforms are bounded on this segment.
That last neighborhood argument is a local adaptation, whose complete project proof is retained in [the fixed conditional Haar-additive argument](../../../claims/Yin_C_F0193_v1.md#conditional-haar-additive-argument), rather than claimed as an extra source theorem.

<a id="least-value-and-ultra-small-integral"></a>
## Uniform least-value estimate and the ultra-small integral

Theorem 3.2, PDF pp. 14--15, assumes \(\Gamma\) invertible with \(\|\Gamma^{-1}\|\le N^\alpha\) and states
\[
 \mathbb P\{s_{\min}(U\Gamma+D)<t\}\le t^cN^{c'},\qquad t>0,
\]
where \(c,c'>0\) depend on \(\alpha\) and are independent of the additive deterministic matrix \(D\) and of \(N\).
Its proof explicitly invokes Rudelson--Vershynin with constants uniform in \(D\), then factors \((U+D\Gamma^{-1})\Gamma\).
The inverse bound is automatic with \(\Gamma=I\).

Lemma 4.4, PDF pp. 18--19, states that for each fixed \(\alpha>0\) there are \(c,\widetilde c>0\) such that, for every \(L_1>0\),
\[
 \mathbb E\left|\int_0^{N^{-L_1}}G^\lambda(i\eta)\,d\eta\right|
 \le N^{-cL_1/2+\widetilde c},
 \tag{Tiny}
\]
provided \(\|(A_N-\lambda)^{-1}\|\le N^\alpha\) or \(\|\Sigma_N^{-1}\|\le N^\alpha\).
No invertibility of the additive deformation is needed when \(\Sigma_N=I\).
The critical proof first bounds the integral by
\[
 \frac12\mathbb E\log\bigl(1+(N^{L_1}s_{\min})^{-2}\bigr)
 =\frac12\int_0^\infty
  \mathbb P\{s_{\min}\le N^{-L_1}(e^s-1)^{-1/2}\}\,ds.
\]
The three ranges \((0,N^{-L_1})\), \((N^{-L_1},1)\), and \((1,\infty)\) are controlled respectively by their length, the probability floor at \(N^{-L_1/2}\), and the exponentially decaying threshold in the uniform least-value bound.
This verifies the needed uniform dependence and the exponent form without re-auditing the underlying Rudelson--Vershynin proof.

<a id="conditional-input-boundary"></a>
## Conditional use and limits

For a random deformation independent of a fresh Haar matrix within its own dimension, conditioning on that within-dimension background allows the deterministic statements to be used on a fixed norm and Lévy-distance guard.
The conditional uniformity, summable joint guard-and-failure events, fixed weak-neighborhood argument, dyadic integration, and full ordinary logarithmic limit are project deductions with the complete candidate reasoning in [C_F0193_v1](../../../claims/Yin_C_F0193_v1.md#conditional-haar-additive-argument).
They do not follow merely by citing an in-probability eigenvalue theorem.
Conditioning on the complete sequence of background matrices is not justified under arbitrary cross-dimensional coupling.
For \(D_N=R(U_N)\), pole-freeness gives the norm bound, its singular empirical measure is \(|R|_*\mu_{U_N}\), and the assumed single-Haar empirical theorem supplies the eventual guard.
The rational normal example and more general background-compression hypotheses must be checked in the actual consuming Claim.
