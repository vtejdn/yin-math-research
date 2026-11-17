---
author: Yin
---

<a id="aekn19-u001"></a>
# Stable local law for the physical diagonal blocks

The [inspected edition](readme.md) gives its vector Dyson equation (3.26) on p. 12, the Kronecker model (4.2) and its independence and moment requirements on pp. 14–15, and the stability region and block error (B.1)–(B.2) in Lemma B.1(i) on p. 28.

<a id="stable-block-law"></a>
## Application to fixed Hermitian coefficient matrices

The selfadjoint input uses independent Hermitian Wigner colors with independent centered entries up to reflection, variances \(O(1/N)\), uniformly bounded moments of the normalized raw coordinates, and a fixed finite number of uniformly bounded coefficient matrices.
Real symmetric Rademacher matrices have these properties, including the source's diagonal variance bounds.
Source normalization uses the resolvent \((H-z)^{-1}\).
For a deterministic site-independent drift \(C=C^*\) and coefficient matrices \(A_j=A_j^*\), when all entry variances are \(1/N\), the positive-imaginary-part solution is constant across sites and satisfies
\[
 -M(z)^{-1}=zI-C+\sum_j A_j M(z)A_j .
\]
The stability operator is identity on mean-zero site vectors and is \(T\mapsto T-M(z)(\sum_j A_jTA_j)M(z)\) on constant site vectors.
This follows directly by substitution into the variance map in (3.26), or into its matrix form (3.29).
The fixed auxiliary dimension makes its Hilbert--Schmidt operator norm equivalent to any fixed-dimensional matrix norm on that constant subspace.

If \(M(E+i\eta)\) and the inverse stability operator are bounded uniformly for \(\eta>0\), the vertical ray above \(N^{-1+\gamma}\) at the prescribed \(E\) belongs to (B.1) for every fixed \(\gamma>0\).
In (B.2) the diagonal resolvent block error is then stochastically dominated by \(C((N\eta)^{-1/2}+N^{-1/2}+(N\eta)^{-1})\) for \(N^{-1+\gamma}\le\eta\le2\).
Using Definition 4.2 with a sufficiently small stochastic-domination exponent gives a uniform constant bound on all its diagonal blocks at a polynomial number of specified scales, except with probability \(O_D(N^{-D})\) for each fixed \(D\).
The input is the stable-regime local law at its stated hypotheses; its long proof and the paper's conclusions for non-Hermitian spectra were not independently re-audited.
