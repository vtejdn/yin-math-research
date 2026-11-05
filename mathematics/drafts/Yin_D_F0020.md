---
author: Yin
---

# Conditional deformed-single-ring input for a two-Haar determinant pilot

This Preparation concerns [Task F0015](../tasks/Yin_T_F0015_v1.md#contract) and the continuing two-effective-cycle investigation in [D_F0013](Yin_D_F0013.md).
The question is whether the deterministic deformed single ring local law can be applied uniformly, after conditioning on one Haar input, to \(R(U_N)+V_N\).
This is ordinary source preparation and mathematical development, not an independent proof review.

## Inspected work and edition

Ching-Wei Ho and Ping Zhong, *Deformed single ring theorems*, is formally published in *Journal of Functional Analysis* **288**(5) (2025), article 110797, DOI [10.1016/j.jfa.2024.110797](https://doi.org/10.1016/j.jfa.2024.110797).
The publisher's article record and [Zhong's research page](https://sites.google.com/view/pzhong/research) were checked for that identity.
No earlier same-work canonical registration was found in the selected bibliography/source-note search.
Thus HZ25 is the publication-year key proposed for first registration; the DOI's 2024 and the preprint's version year do not make the publication year 2024.
The precise mathematical edition inspected is [arXiv:2210.11147v4](https://arxiv.org/pdf/2210.11147v4), with its retained original at [HZ25--arxiv-v4.pdf](../literature/pdf/HZ25--arxiv-v4.pdf).
The PDF has 33 pages and a title-page date of December 17, 2024, while its arXiv version stamp is December 13, 2024.
The experimental HTML rendition currently displays a different internal date, so the retained PDF controls the page and formula locators here.

The selected passages are Proposition 2.2 on PDF p. 9, Theorem 2.3 and Definition 2.4 on p. 10, Theorem 2.8 and stochastic-domination Definition 2.6 on p. 12, Theorem 3.2 on pp. 14--15, Theorem 4.1 on pp. 15--17, and Lemmas 4.3--4.4 on pp. 18--19.
Theorem statements and the stated application interfaces were read; their original external proofs and all cited foundational papers were not recursively audited.

## Current source-applicability question

Assume \(R\) is a fixed rational function with no pole on the unit circle and nonconstant \(|R|\) there.
For independent Haar \(U_N,V_N\), put \(D_N=R(U_N)\) and \(a=R(u)\), where \(u\) is a free Haar unitary independent of another free Haar unitary \(v\).
The intended strict-bulk assumptions are
\[
 \int_{\mathbb T}|R(z)|^2\,dm(z)>1,
 \qquad
 \int_{\mathbb T}|R(z)|^{-2}\,dm(z)>1,
\]
allowing the second integral to be infinite.
A source theorem for deterministic inputs is not by itself a theorem for these random normal deformations; the conditional uniformity and the probability-one guard must be established explicitly.

<a id="conditional-haar-additive-statement"></a>
## Candidate conditional Haar-additive logarithmic lemma

Let \(\mathcal F_N\) be a background sigma algebra, let \(D_N\in M_N(\mathbb C)\) be \(\mathcal F_N\)-measurable, and assume that the conditional law of \(V_N\) given \(\mathcal F_N\) is Haar probability on \(U(N)\).
No relation between the sigma algebras or matrices at distinct dimensions is assumed.
Suppose that some fixed \(M<\infty\) and deterministic probability measure \(\mu\) on \([0,M]\) satisfy
\[
 \|D_N\|\le M\quad\text{eventually almost surely},
 \qquad \mu_{|D_N|}\Longrightarrow\mu\quad\text{almost surely}.
 \tag{Background}
\]
Put \(\nu=\widetilde\delta_1\boxplus\widetilde\mu\).
Assume that \(\widetilde\mu\) is supported at more than two points and that zero lies in the regular bulk of \(\nu\) as defined in Ho--Zhong Definition 2.7.
Let \(d\ge0\) have law \(\mu\), and let \(v\) be a Haar unitary free from \(d\), in a finite tracial von Neumann algebra.
Then the candidate conclusion is
\[
 \frac1N\log|\det(D_N+V_N)|
 \longrightarrow c=\log\Delta(d+v)=\int\log|x|\,d\nu(x)\in\mathbb R
 \quad\text{almost surely}.
 \tag{Conditional-log}
\]
The singular-value measures also converge weakly almost surely to the positive-half singular law corresponding to \(\nu\).
This is a project deduction from the accepted source inputs specified below, awaiting review of its complete local adaptation.

<a id="conditional-haar-additive-argument"></a>
## Complete candidate resolvent argument

### A fixed neighborhood controls the empirical free convolution

Write \(\rho_N=\mu_{|D_N|}\), and denote \(\nu_\rho=\widetilde\delta_1\boxplus\widetilde\rho\) for any probability measure \(\rho\) supported on \([0,M]\).
For the limiting pair, regular bulk at zero means that both subordination values at zero are finite and have strictly positive imaginary parts, by Ho--Zhong Theorem 2.3.
The continuous boundary extensions in Proposition 2.1 and their ordinary upper-half-plane continuity give a bound and a positive lower bound for the relevant subordination denominator on the compact segment \(i[0,1]\).
Proposition 2.2 then implies
\[
 \sup_{0\le\eta\le1}|G_{\nu_\rho}(i\eta)|\le C
 \quad\text{whenever }d_{\mathrm L}(\rho,\mu)\le b,
 \tag{Free-neighborhood}
\]
for some fixed \(b,C>0\), with the same support bound \(M\).
Here is the needed passage from sequential convergence to an actual neighborhood.
If no such neighborhood existed, choose \(\rho_k\) supported in \([0,M]\) with \(d_{\mathrm L}(\rho_k,\mu)\to0\) and a violating value of \(\eta\in[0,1]\).
Bounded support makes this weak convergence equivalent to convergence of all moments.
Realize positive operators with those laws in one commutative finite tracial algebra, and apply Proposition 2.2 with \(\lambda=0\), \(K=\{0\}\), and \(K'=i[0,1]\).
Its uniform convergence of the two subordination functions contradicts the violation, using the correct identity \(G_{\nu_\rho}(z)=(\omega_{1,\rho}(z)+\omega_{2,\rho}(z)-z)^{-1}\).
The source's displayed denominator in the proof of Lemma 4.3 repeats the first subordination index; the governing relation (2.1) uses the sum of the two indices.
No quantitative convergence rate is used in this neighborhood argument.

Shrink \(b\) so that Theorem 2.8 also applies to the fixed pair \((\delta_1,\mu)\) and \(I=\{0\}\).
Define the within-dimension good background event
\[
 E_N=\{\|D_N\|\le M,\ d_{\mathrm L}(\rho_N,\mu)\le b\}.
\]
Assumption (Background) says that \(E_N\) holds eventually almost surely.
It does not require the probabilities of \(E_N^c\) to be summable.

### Conditional local law with a common deterministic bound

Conditional on \(\mathcal F_N\), singular-value decomposition of \(D_N\) reduces the singular values of \(D_N+V_N\) to those of \(\Xi_N+W_N\), where \(\Xi_N=\operatorname{diag}(s_j(D_N))\) and \(W_N\) remains Haar.
A single Haar matrix has the same distribution as a product of two independent Haar matrices, so this is the Ho--Zhong model with \(\Sigma_N=I_N\).
Theorem 2.8 supplies a uniform stochastic bound over the bounded deterministic inputs in its fixed Lévy neighborhood:
\[
 |G_N(i\eta)-G_{\nu_{\rho_N}}(i\eta)|
 \prec\frac1{N\eta(1+\eta)}.
 \tag{Conditional-local}
\]
The constants depend on the fixed limiting pair, support bound, spectral set, and chosen stochastic exponents, rather than on a convergence rate for \(\rho_N\).
Its fixed-neighborhood formulation permits each admissible finite input to be embedded into a deterministic sequence by filling other dimensions with bounded quantile approximations to \(\mu\).
Thus it is applicable inside \(E_N\) after conditioning on the background of this dimension.

For every fixed \(\eta>0\), (Conditional-local), (Free-neighborhood), and the convergence \(\rho_N\Rightarrow\mu\) give almost-sure convergence \(G_N(i\eta)\to G_\nu(i\eta)\), after intersecting a countable dense set of positive \(\eta\)'s.
The singular values are at most \(M+1\) eventually.
Compactness of probability measures on this interval, together with uniqueness of the Stieltjes transform on the positive imaginary axis for symmetric measures, identifies every weak subsequential limit with \(\nu\).
This proves the claimed almost-sure weak singular-value limit and hence convergence of every fixed positive-regularizer logarithm.
In particular, no extra random-matrix weak-convergence theorem is needed for the sum \(D_N+V_N\) once (Background) is supplied.

Only the within-dimension background is conditioned on.
Conditioning on the entire sequence of backgrounds could change the conditional Haar law under an arbitrary cross-dimensional coupling and is not used.
For any local-law failure event \(B_N\), uniformity gives
\[
 \mathbb P(E_N\cap B_N)
 =\mathbb E[1_{E_N}\mathbb P(B_N\mid\mathcal F_N)]
 \le N^{-D}.
\]
First Borel--Cantelli applies to these joint events, followed by the eventual almost-sure guard.
This is the step that preserves the contract's arbitrary-coupling quantifier.

### Integrating the local law instead of multiplying a floor by a count

Let \(h_N(\eta)=-\operatorname{Im}G_N(i\eta)\ge0\).
Fix \(\varepsilon\in(0,1)\) and a large fixed \(L\), and use the dyadic grid \(\eta_j=2^jN^{-L}\) up to one.
The number of grid points is \(O(\log N)\), and (Conditional-local) and (Free-neighborhood) imply, on \(E_N\) outside summable failures,
\[
 h_N(\eta_j)\le C+\frac{N^\varepsilon}{N\eta_j}.
 \tag{Grid}
\]
Choose the stochastic exponent \(D\) larger than three before the finite union over this grid.
For \(a\le\eta\le2a\), the spectral formula gives
\[
 \frac{\eta}{s^2+\eta^2}\le\frac{2a}{s^2+a^2},
 \qquad h_N(\eta)\le2h_N(a).
\]
Summing the grid intervals therefore gives, for each fixed \(\delta\in(0,1]\),
\[
 \int_{N^{-L}}^\delta h_N(\eta)\,d\eta
 \le C'\delta+O(N^{-1+\varepsilon}\log N)
 \quad\text{eventually almost surely}.
 \tag{Middle-integral}
\]
A final partial interval can be estimated by the same factor-two bound.

For the remaining ultra-small segment, Lemma 4.4 applies with \(\Sigma=I\), so its inverse condition holds for any fixed positive \(\alpha\).
Theorem 3.2 and the proof of Lemma 4.4 show that the constants are uniform over the deterministic additive deformation.
Consequently, for fixed positive \(c_0,C_0\),
\[
 \mathbb E\!\left[\int_0^{N^{-L}}h_N(\eta)\,d\eta
       \mid\mathcal F_N\right]
 \le N^{-c_0L/2+C_0}.
 \tag{Tiny-expectation}
\]
Choose \(L\) so large that \(c_0L/2-C_0>4\).
Markov's inequality at threshold \(N^{-1}\) and first Borel--Cantelli then show that this integral tends to zero almost surely, with no cross-dimensional independence.
The same least-singular-value bound, by sending its threshold to zero at fixed \(N\), gives invertibility almost surely, so the ordinary logarithms and the following defect identity are well defined on one countable intersection event.

Put \(Z_N=D_N+V_N\) and
\[
 \ell_{N,\delta}=\frac1{2N}\operatorname{Tr}\log(Z_N^*Z_N+\delta^2I),
 \qquad \ell_N=\frac1N\log|\det Z_N|.
\]
Direct differentiation of the finite spectral formula yields
\[
 \ell_{N,\delta}-\ell_N=\int_0^\delta h_N(\eta)\,d\eta.
 \tag{Defect}
\]
Combining (Middle-integral) and (Tiny-expectation) gives \(\limsup_N(\ell_{N,\delta}-\ell_N)\le C'\delta\) almost surely.
The fixed-regularizer limit \(\ell_{N,\delta}\to c_\delta\) follows from the already established compactly supported weak singular-value limit.
The regular-bulk bound near zero makes \(c_\delta\downarrow c\in\mathbb R\).
Thus
\[
 c_\delta-C'\delta\le\liminf_N\ell_N
 \le\limsup_N\ell_N\le c_\delta,
\]
and sending a countable sequence of \(\delta\)'s to zero proves (Conditional-log).

## Matching the rational normal pilot

For \(D_N=R(U_N)\), pole-freeness on the unit circle supplies the deterministic bound \(\|D_N\|\le\|R\|_{\infty,\mathbb T}\).
The single-Haar empirical spectral theorem supplies (Background) with \(\mu=|R|_*m_{\mathbb T}\), under every cross-dimensional coupling at its already accepted probability scope.
The two strict squared-norm inequalities displayed above put zero in \(\Omega(v,R(u))\).
The exceptional set \(S(v,R(u))\) is empty at zero because \(|v|\) has no atom at zero, and a nonconstant rational function has no positive Haar-measure zero set on the circle.
Theorem 2.3 therefore supplies the regular-bulk condition.
If \(|R|\) is nonconstant, its symmetrized law has more than two support points, as required by Theorem 2.8.
The same conditional lemma can be applied to nonnormal deformations, provided their norm and singular-law guard are actually proved; normality was used here only to verify the displayed rational pilot's background facts.

This completes the proposed source-to-conditional-lemma interface, but does not by itself verify an affine-pencil Schur reduction or complete F0015.
Those original finite/free determinant identities and the full candidate adoption and review belong to the consuming Claim.
