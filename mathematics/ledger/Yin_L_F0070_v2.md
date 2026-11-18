---
author: Yin
---

# The elliptic companion of a correlated Wigner product

<a id="elliptic"></a>
## The free law and spectrum in the original spectral plane

For independent standard free semicircular elements \(s_1,s_2\), let \(u=\alpha\cdot s,\ v=\beta\cdot s\) with linearly independent real vectors \(\alpha,\beta\in\mathbb R^2\).
Put \(\nu=\|\alpha\|_2\|\beta\|_2,\ k=\langle\alpha,\beta\rangle\), so \(|k|<\nu\), and \(r=(\|\beta\|_2/\|\alpha\|_2)^{1/2}\).
For the [correlated sign pilot](Yin_L_F0070_v1.md#spatial) the free product model has the following explicit target.
Define
\[
 Q=\begin{pmatrix}0&ru\\v/r&0\end{pmatrix},\qquad
 C_j=\begin{pmatrix}0&r\alpha_j\\\beta_j/r&0\end{pmatrix}.
\]
Then \(Q=\sum_j C_j\otimes s_j\).
For the conditional expectation \(E=\mathrm{id}\otimes\tau\) the four pair expectations are
\[
 E(QQ^*)=E(Q^*Q)=\nu I_2,\qquad E(QQ)=E(Q^*Q^*)=k I_2 .
\]
Expand an arbitrary word in \(Q,Q^*\) by the free semicircular Wick formula.
Within each noncrossing pairing integrate out an adjacent pair, whose coefficient sum is a scalar matrix by the displayed equations.
Repeating this step leaves the product of the designated pair covariances times the identity.
The resulting scalar star moments agree with those of the elliptic element
\(e=\sqrt{(\nu+k)/2}\,s_1+i\sqrt{(\nu-k)/2}\,s_2\).
Equality of star moments in faithful tracial models identifies their generated tracial algebras and spectra.
Indeed one recovers the norm of every polynomial from the even trace moments of its absolute value and thus obtains an isometric isomorphism of the generated unital C-star algebras, which are inverse closed in their ambient algebras.

The [scalar elliptic theorem and its normalization](../claims/Yin_C_F0123_v1.md#scalar-tests-that-preserve-the-missing-covariance) give uniform Brown measure and spectrum on the filled ellipse of semiaxes \(a=(\nu+k)/\sqrt\nu\) and \(b=(\nu-k)/\sqrt\nu\).
Negative \(k\) simply interchanges the long axis and short axis relative to the positive covariance formula.
The centered semicircular pair \((ru,v/r)\) has a covariance matrix invariant under interchanging the two coordinates.
Its joint star law shares this symmetry, so \(uv\) and \(vu\) have equal spectra and Brown measures.
Since \(Q^2=\operatorname{diag}(uv,vu)\), spectral mapping identifies their common spectrum with the square image of the ellipse.
Ordinary polynomial pushforward of Brown measure follows here by factoring \(Q^2-zI=(Q-wI)(Q+wI)\) for \(w^2=z\) and applying [FK multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
The two block potentials of \(Q^2\) agree, and the equal potentials of \(Q-wI\) and \(Q+wI\) give \(u_P(z)=\log\Delta(uv-zI)=2\log\Delta(Q-wI)\).
The squared boundary \((a\cos\theta+i b\sin\theta)^2\) parametrizes twice the ellipse with center \(2k\), horizontal semiaxis \(d_x=\nu+k^2/\nu\) and vertical semiaxis \(d_y=\nu-k^2/\nu\).
The argument principle gives two preimages counted with multiplicity inside this boundary and none outside.
Away from zero there are two simple inverse branches, each with area Jacobian \(1/(4|z|)\).
Consequently the spectrum and Brown support of \(uv\) equal the filled ellipse
\[
 E_P=\left\{z:\frac{(\Re z-2k)^2}{d_x^2}+\frac{(\Im z)^2}{d_y^2}\le1\right\},
 \qquad d\mu^{\rm Br}_{uv}(z)=\frac{\mathbf1_{E_P}(z)}{2\pi d_y|z|}\,dA(z).
\]
The pushforward has no point mass at zero.
Substitution of \(w^2=z\) into the interior potential (SP14) of the scalar elliptic calculation gives
\[
 u_P(z)=\log\nu-1+\frac{\nu|z|-k\Re z}{\nu^2-k^2},\qquad z\in E_P .
\]
In particular consider \(U=A+2B,\ V=3A+B\), with \(A,B\) independent real sign Wigner matrices.
Here \(\nu=5\sqrt 2,\ k=5\), and at \(i\) the left side defining the ellipse is \(8/9+2/25=218/225<1\).
The fixed target at this genuine interior point is \(\log(5\sqrt 2)-1+\sqrt 2/5\).
The two [exceptional real shifts of the Hermitian stability calculation](../claims/Yin_C_F0356_v3.md#example) equal the two endpoints \(2k\pm d_x\).

<a id="exterior"></a>
## Summable exterior floors for the finite sign companion

Let \(Q_N=\sum C_j\otimes W_j^{(N)}\), with centered independent Hermitian Wigner colors of the contracted form, independent up to reflection within each color, variance \(1/N\) for every entry including the diagonals, and all moments finite for each fixed raw law.
In particular this includes all independent fair signs on and above the diagonal.
For every compact \(K\subset\mathbb C\setminus E_P\) there is a constant \(c_K>0\) such that for every fixed \(M>0\),
\[
 \Pr\{\inf_{z\in K}s_{\min}(U_NV_N-zI)<c_K\}\le C_{K,M}N^{-M}.
\]
The same bound with a positive compact-dependent floor holds for \(Q_N-wI\) on the full inverse image \(K'=\{w:w^2\in K\}\).

The Kronecker representation uses the two original independent physical matrices as inputs, with their nonsymmetric \(C_j\) fixed.
The prescribed dependence between entries of \(U_N\) and \(V_N\) is exactly the repeated use of each input by its structure matrix.
The variance, moment, structure and drift bounds of [AEKN19, Lemma 6.1](../audits/literature/AEKN19/Yin_U001.md#kronecker-pseudospectrum) hold.
In the source Hermitization the selfadjoint coefficient for color \(j\) is \(H_j=\left(\begin{smallmatrix}0&C_j\\C_j^*&0\end{smallmatrix}\right)\).
All variances are \(1/N\), so on constant site vectors the variance map is \(T\mapsto\sum_j H_jTH_j\).
The free Hermitization of \(Q-wI\) has the same drift and covariance, hence its matrix-valued Cauchy transform in the source sign convention solves the Dyson equation at every site by the [operator-valued semicircular formula](../audits/literature/MS17/Yin_U001.md#ms17-u001).
Uniqueness in Lemma 2.2 identifies the source's deterministic law with the free scalar law of that Hermitization.
Faithfulness identifies the support of this scalar selfadjoint law with its spectrum.
The distance of its spectrum to zero for \(w\in K'\) thus equals \(\|(Q-wI)^{-1}\|^{-1}\).
The previous spectral identification and continuity of the inverse give a strictly positive minimum \(g\) on \(K'\).
Take \(0<e\le\min(1,g/4)\) and \(d=e\) in Lemma 6.1.
Then \(K'\) is disjoint from the deterministic \((e+d)\)-pseudospectrum and, with the displayed probability control, from the entire finite \(e\)-pseudospectrum.
As \(K'=-K'\), both factors of \(Q_N^2-zI=(Q_N-wI)(Q_N+wI)\) have least singular value greater than \(e\).
The product has diagonal blocks \(U_NV_N-zI\) and \(V_NU_N-zI\), giving the floor \(c_K=e^2\).

The [finite-variance scalar potential controls](../claims/Yin_C_F0186_v4.md#statement) give locally uniform convergence of the fixed positive regularizations of \(U_NV_N\) under every permitted coupling.
The summable exterior floor makes the error of replacing the ordinary logarithm by \(\tfrac12\log(s^2+\delta^2)\) uniformly at most \(\tfrac12\log(1+\delta^2/c_K^2)\) per singular value, eventually almost surely on \(K\).
The free gap on \(K\) gives the same comparison with its own positive constant.
Letting \(\delta\downarrow0\) on a countable exhaustion gives almost-sure locally uniform convergence of the ordinary normalized log determinant on the full exterior under any cross-size coupling.
The finite and free factorizations give the same conclusion at \(w^2=z\) for the two-channel affine determinant with trace normalization \(1/(2N)\) and limiting potential \(u_P(z)/2\).

The diagonal laws may have arbitrary finite fourth moments and arbitrary variances for these almost-sure exterior conclusions.
Replace all diagonals by independent centered variance-one signs and compare the two \(Q_N\)'s in operator norm.
For a raw diagonal law \(D\) and \(c>0\), finiteness of \(\mathbb E|D|^4\) gives \(\sum_N N\Pr(|D|>c\sqrt N)<\infty\) by summing the integers \(N<|D|^2/c^2\) before taking expectation.
Union over physical sites and Borel–Cantelli make the diagonal replacement norm tend to zero almost surely under every coupling.
With only second diagonal moments, \(N\Pr(|D|>c\sqrt N)\to0\), so the same replacement norm tends to zero in probability.
In this last range the exterior logarithms converge locally uniformly in probability and almost surely on a deterministic subsequence under every coupling, by subsequence extraction over compact exhaustion and the fixed regularizations.
The existing fixed-parameter upper bound on the limsup then gives the [F0014](../tasks/Yin_T_F0014_v1.md#contract) equality on the exterior for each prescribed shift and the associated [F0013](../tasks/Yin_T_F0013_v1.md#contract) equality for its two-channel pencil.

The [earlier exterior argument](../claims/Yin_C_F0194_v30.md#exterior-proof) uses a strong spectral inclusion theorem on its nested input array and obtains a marginal lower bound for another real quadratic.
Here the Kronecker theorem gives a summable exceptional probability in the unmodified all-moment, equal-variance model, and the balanced coefficients explicitly determine the exterior.
At \(i\) the free Hermitization has zero in its spectrum, so its deterministic gap vanishes.
The finite companion has two deterministic zero blocks and uses the same physical edge across several auxiliary entries.
The [scalar elliptic random-matrix theorem](../audits/literature/NO15/Yin_U002.md#elliptic-pair) requires an independent family of mirror pairs and cannot be applied to this companion solely from its free star law.
The [bottom singular-space probability estimate](Yin_L_F0070_v1.md#spatial) remains open in the interior of the ellipse.
