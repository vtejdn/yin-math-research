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

<a id="kronecker-pseudospectrum"></a>
## Exclusion of singular values outside the deterministic pseudospectrum

The 18 November 2026 inspection of the [same v3 original](../../../literature/pdf/AEKN19--arxiv-v3.pdf) covers Definition 2.1 and equations (2.6)–(2.12) on pp. 4–6 and the statement and use of Lemma 6.1 on pp. 25–26.
Definition 2.1 permits a sum of arbitrary fixed structure matrices tensored with independent centered Hermitian input matrices whose entries are independent up to reflection.
Consequently one physical variable can occur in several auxiliary blocks of a single structure matrix.
The input bounds (2.9)–(2.12) control the upper variances by a constant times the inverse matrix dimension, bound every moment of the rescaled entries, and bound the finitely many structure matrices and site drifts in operator norm.
For each complex parameter the unique positive-imaginary-part solution of the Hermitized Dyson equation in Lemma 2.2 defines a deterministic law on the real axis.
Write \(D_b\) for the parameters at which the distance from zero to the support of this law is at most \(b\).
For fixed \(0<e\le1,\ d>0\) and \(M>0\), Lemma 6.1 puts the entire \(e\)-pseudospectrum of the finite matrix inside \(D_{e+d}\) with failure probability at most \(C_{e,d,M}N^{-M}\).
Here the finite pseudospectrum includes all parameters with smallest singular value at most \(e\).
The estimate includes the non-Hermitian case and needs no lower variance or irreducibility assumption.
The source theorem is used at statement and applicability depth.
The [balanced companion calculation](../../../ledger/Yin_L_F0070_v2.md#exterior) identifies its deterministic law with the free Hermitization in the equal-variance model.
