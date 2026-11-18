---
author: Yin
---

<a id="han26b-u002"></a>
# Brown measure convergence for polynomials with adjoints

For every fixed scalar noncommutative polynomial \(P\) in independent Wigner matrices, including non-self-adjoint polynomials, Theorem 1.4 of [Han26b, arXiv v1](readme.md#yin-v1) gives weak convergence in probability of the empirical eigenvalue measure to the Brown measure of \(P(s_1,\ldots,s_n)\).
The \(s_\ell\) are free semicircular elements of variance one.
Theorem 1.1 gives the analogous conclusion for arbitrary scalar \(*\)-polynomials in independent iid matrices and their adjoints, with free circular limits normalized by \(\tau(c_\ell c_\ell^*)=1\).
In both cases the empirical eigenvalues carry weight \(1/N\) with algebraic multiplicity.
The results use the [density and independence assumptions](Yin_U001.md#entry-models) and a finite \(2+\varepsilon\) moment of the iid or Wigner off-diagonal atoms for some \(\varepsilon>0\).
The Wigner diagonal laws need only a second moment in addition to centering and their bounded real density.

Write \(P_N\) and \(P_\infty\) for the matrix evaluation and its free counterpart, and put \(U_N(z)=N^{-1}\log|\det(P_N-zI)|\) and \(U(z)=\tau(\log|P_\infty-z|)\).
In the [finite tracial convention](../BZ22/Yin_U001.md#brown-measure-convention), \(\mu^{\rm Br}_{P_\infty}=(2\pi)^{-1}\Delta U\).
The proof gives both
\[
 U_N(z)\xrightarrow{\mathbb P} U(z)\quad\text{for each fixed }z\ne P(0),
 \qquad
 \mathbb E\int_K |U_N(z)-U(z)|\,d^2z\longrightarrow0
 \quad\text{for every compact }K\subset\mathbb C .
\]
The second statement includes compact sets containing \(P(0)\).

The proof inspection completed at 2026-11-18T10:02 UTC covers Sections 7.1–7.7, pp. 30–42, together with the [least singular value proof in Sections 1–6](Yin_U001.md#han26b-u001) and the cited-source identifications on pp. 42–43.
The calculations below close the proof of both probability limits.
The two external theorems used in the Gaussian comparison were checked at the level of their statements and applicability.

<a id="finite-variance-hermitization"></a>
## Weak singular-value convergence and the upper tail

Let \(\nu_N^z\) be the empirical law of the squared singular values of \(P_N-zI\), and let \(\nu^z\) be the tracial law of \((P_\infty-z)(P_\infty-z)^*\).
Weak convergence of \(\nu_N^z\) in probability holds for every fixed \(z\) under finite second moments, including for Wigner inputs in Lemma 7.6.
For bounded atoms the leading terms in the normalized trace expansion come from trees whose edges are traversed once in each direction.
Directed iid entries force opposite adjoint markings to use the same atom.
Unordered Wigner edges contribute \(\mathbb E|\zeta|^2=1\), and a diagonal loop loses a spatial index.
In the covariance calculation a shared atom connects the two walks, costing at least one power of \(N\).
This identifies the circular or semicircular moments and yields convergence in probability for bounded atoms.

For a matrix \(Z\), let \(\Pi_T Z\) cap its singular values at \(T\).
It is the Hilbert–Schmidt projection onto the operator-norm ball and satisfies \(\operatorname{rank}(Z-\Pi_T Z)\le T^{-2}\|Z\|_{\rm HS}^2\).
A polynomial of degree at most \(D\) changes rank by at most a fixed multiple of the sum of the input rank changes, by telescoping its words.
It has norm at most \(C_Q T^D\) on the capped inputs for \(T\ge1\).
Consequently Lemma 7.1 gives
\[
 \mathbb E\,\#\{j:s_j(Q(Z))>M\}\le C_Q NM^{-2/D},\qquad M\ge1,\quad D\ge1 .
\]
For finite-variance laws, compare \(P(Z)\) and the bounded-atom polynomial by capping both sets of input matrices.
The two rank errors vanish as \(T\to\infty\).
For fixed \(T\) the middle difference is bounded in normalized Hilbert–Schmidt norm by a constant depending on \(T\) times the input coupling error, which vanishes as the atom cutoff tends to infinity.
The same argument works under conjugate reflection of a Wigner upper triangle, with the diagonal second-moment error weighted by \(1/N\).
This justifies the passage to weak singular laws even when high polynomial moments are infinite.
Applying Lemma 7.1 to \(P-zI\) and integrating its tail gives (7.11) for the positive logarithm.

<a id="free-and-gaussian-count"></a>
## The Gaussian reference count

For nonconstant \(P\), \(Q_z=(P-z)(P-z)^*\) is a nonconstant scalar self-adjoint polynomial in free semicirculars.
Indeed its leading term is \(P_dP_d^*\ne0\) in the free algebra.
For circular letters the invertible change of variables \(c_\ell=(s_{\ell,1}+is_{\ell,2})/\sqrt2\) preserves this conclusion.
SS15, Theorem 1.1(2), (5), (6) and Corollary 1.2, supply absence of an atom at zero and a local Puiseux expansion for the Cauchy transform.
The bound \(|g(i\eta)|\le1/\eta\) excludes powers below \(-1\), and the absence of an atom excludes a nonzero pole of order one.
With \(g(w)=\int (x-w)^{-1}d\nu^z(x)\), the inequality \(\nu^z([0,x])\le2x\Im g(ix)\) then gives \(\nu^z([0,x])\le C_z x^\theta\) for some \(\theta>0\). [SS15, Theorem 1.1 and Corollary 1.2](https://arxiv.org/pdf/1305.1920#page=2)

AGZ10, Lemma 5.5.4, compares the expected normalized resolvent trace of a fixed self-adjoint polynomial in independent normalized GUE matrices with its free resolvent trace.
At \(i\eta\) the error is at most \(C N^{-2}\eta^{-b_1}\) down to \(N^{-b_0}\) for constants depending on the polynomial and strip.
The Gaussian iid model has the required GUE-pair realization and the Wigner reference is already GUE.
Decreasing the polynomial range allows the error to be absorbed in \(C\eta^{\theta-1}\).
This verifies (7.4) and (7.21) in the two models.
The audit accepts these external statements for the indicated polynomials.
Their original proofs were outside the scope of this reading. [AGZ10, §5.5, Lemma 5.5.4](https://www.wisdom.weizmann.ac.il/~zeitouni/cupbook.pdf)

On the Gaussian event of bounded operator norms, the word-chain elimination factors are bounded.
If \(\Delta_z=\operatorname{diag}(P_N-zI,I)\), then \(s_j(\Delta_z)\le C s_j(L_z)\) for the linearizing pencil \(L_z\).
At a sufficiently small threshold, the identity block contributes no mass.
Together with the Gaussian norm tail, this transfers the Gaussian count to the Hermitization \(\mathcal H_z=\left(\begin{smallmatrix}0&L_z\\ L_z^*&0\end{smallmatrix}\right)\), whose normalized Stieltjes transform is denoted by \(m\) after expectation.
Summing the kernel on dyadic intervals gives \(\Im m(i\eta)\le C\eta^{\kappa-1}\), with \(0<\kappa<\min(2\theta,1)\), down to a fixed inverse power of \(N\).

<a id="whole-atom-comparison"></a>
## Non-Gaussian comparison and the Wigner covariance

Set \(\alpha=\min(\varepsilon,1)\).
For a single iid atom or one Wigner off-diagonal atom together with its conjugate, the Hermitized affine perturbation has bounded rank and norm \(O(|v|/\sqrt N)\).
With \(\eta=\Im w>0\), a normalized trace contributes a further \(N^{-1}\) in the derivative bounds.
Interpolating the quadratic and cubic bounds on the Taylor remainder gives \(C N^{-2-\alpha/2}\eta^{-3-\alpha}|v|^{2+\alpha}\) per atom.
Centering and matching the entire two-dimensional real covariance cancel the linear and quadratic terms in expectation.
Summing \(O(N^2)\) errors proves the first replacement in Lemmas 7.2 and 7.4.
The \(O(N)\) independent Wigner diagonal atoms need only a first-order expansion, with a total second-moment remainder \(O(N^{-1}\eta^{-3})\).
This identifies where the \(2+\varepsilon\) assumption enters, even after the bottom singular value is already controlled.

For iid Gaussian atoms, the nonconjugate pairings in the difference of covariance maps act by \(N^{-1}\) times spatial transpose on each fixed coefficient block, by \(\sum_{a,b}E_{ab}QE_{ab}=Q^T\).
For Wigner atoms, (7.17) instead gives the strictly upper and lower parts of \(Q^T\) weighted separately by \(\rho_\ell\) and \(\overline{\rho_\ell}\), plus a diagonal correction.
The bound \(\|\operatorname{tri}_{\pm}(Q^T)\|\le\|Q\|_{\rm HS}\le\sqrt N\|Q\|\) gives an \(O(N^{-1/2})\) covariance error, which suffices even for nonreal \(\rho_\ell\).
Gaussian differentiation inserts the difference of the two fixed covariance maps between resolvents, costing at most \(\eta^{-3}\).
The argument uses no inverse covariances and includes real Gaussian entries.
For Wigner inputs the expected Hermitized mass on \([-\eta,\eta]\) is thus at most
\[
 C\bigl(\eta^\kappa+N^{-\alpha/2}\eta^{-2-\alpha}+N^{-1/2}\eta^{-2}\bigr).
\]
Choosing \(a_2>0\) with \(a_2(\kappa+2+\alpha)<\alpha/2\), \(a_2(\kappa+2)<1/2\), and within the Gaussian range absorbs both errors for \(\eta\ge N^{-a_2}\).
Lemma 7.3 gives the smaller \(N^{-1}\eta^{-2}\) last term for directed iid entries.

<a id="logarithms"></a>
## Removing the logarithmic cutoffs

For the transfer from the non-Gaussian pencil back to the polynomial, write \(L_z=A_L\Delta_z A_R\).
In (7.9) Han sets the singular values above \(M\) of the polynomial factors \(A_L,A_R\) to zero.
Their expected discarded rank is \(O(NM^{-r_*})\) for some \(r_*>0\) by Lemma 7.1.
The truncated product has \(s_j\le M^2s_j(\Delta_z)\), and rank interlacing bounds the cost of restoring the factors.
With \(M=x^{-1/8}\), the new pencil threshold \(M^2\sqrt x=x^{1/4}\) lies in the comparison range for all \(N^{-a}\le x\le x_*\) and a sufficiently small \(a>0\).
This proves the unconditional expected fraction bound \(\mathbb E\nu_N^z([0,x])\le Cx^\vartheta\) in (7.10) and (7.19), with \(\vartheta=\min(\kappa/4,r_*/8)>0\).

Take \(x_N=N^{-a}\) and the event \(F_N=\{s_{\min}(P_N-zI)\ge N^{-B_z}\}\) at a fixed \(z\ne P(0)\).
On \(F_N\), the part of the negative logarithm below \(x_N\) costs at most \(2B_z\log N\) times \(\nu_N^z([0,x_N])\), giving an expected cost \(O(N^{-a\vartheta}\log N)\) on this event.
Integration of the count between \(x_N\) and \(\delta\) costs \(O(\delta^\vartheta(|\log\delta|+1/\vartheta))\).
Markov's inequality adds \(\mathbb P(F_N^c)\) once, with no multiplier \(\log N\).
Together with (7.11), weak singular convergence now applies to \(\tfrac12\int\log x\,d\nu_N^z(x)=U_N(z)\).
This argument explains why the [rate qualification on p. 29](Yin_U001.md#wigner-localization-rate) has no effect on either Brown theorem.

For the planar step (7.13), the eigenvalue product inequalities bound \(\sum_j(\log^+|\lambda_j(P_N)|)^2\) by \(\sum_j(\log^+s_j(P_N))^2\).
The expected normalized latter sum is bounded by Lemma 7.1.
Integrating \(|\log|z-\lambda||^2\) over a compact set costs \(C_K(1+(\log^+|\lambda|)^2)\), so Jensen gives a uniform spatial second-moment bound for \(U_N\).
Fixed-\(z\) probability convergence for almost every \(z\) implies convergence in measure on the finite product of probability space and \(K\).
Uniform integrability there yields the expected spatial \(L^1\) convergence above.
The distributional Laplacian gives convergence for smooth compactly supported tests, and tightness extends it to bounded continuous tests.

<a id="f0012"></a>
## The GUE question and the finite-variance Wigner contract

Taking exact GUE inputs in Theorem 1.4 directly answers the weak-in-probability question for every scalar polynomial, including polynomials with repeated letters and arbitrary complex coefficients.
Equivalently, paired GUEs produce a complex Ginibre variable, and its real and imaginary GUE components are linear combinations of that variable and its adjoint.
Theorem 1.1 allows both of these letters, closing the obstruction identified for the June [Han26, Question 1.8](../Han26/Yin_U001.md#gue-boundary) in the present density and moment classes.
CKMYZ26 had already obtained the GUE conclusion by a separate argument. [CKMYZ26, Theorem 1.1](https://arxiv.org/abs/2611.12785)

The active [F0012 v3 contract](../../../tasks/Yin_T_F0012_v3.md#contract) also allows discrete or singular entry laws, deterministic zero diagonals, and off-diagonal laws with only a finite second moment.
It asks for full-sequence weak convergence almost surely under every coupling across sizes.
The density-based bottom singular-value proof, the fractional moment for the mesoscopic count, and the convergence-in-probability conclusion each mark a separate limit to applying Han26b to that contract.
The repository's [almost-sure GUE case](../../../claims/Yin_C_F0186_v3.md#statement) has its own proof and stronger convergence mode.
The project subsequently adapted the Wigner trace observations to [arbitrary diagonal laws and positive continuous components in the upper laws](../../../claims/Yin_C_F0186_v45.md#statement), using the separate finite-variance clipping estimate for the almost-sure conclusion.
