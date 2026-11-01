# AEK19: the linear stability operator of the matrix Dyson equation

On 2026-10-10 the literature-reading agent for Yin inspected [AEK19, arXiv:1604.08188v5](../../../literature/pdf/AEK19--arxiv-v5.pdf), a 61-page preprint of the published PTRF article.
Its arXiv version stamp is 28 February 2018 and its title page says 15 October 2018; the canonical publication year is 2019.
Acquisition and version facts; complete publication fields belong to [references.bib](../../../literature/references.bib).
The selected reading covers the data and norm conventions in Section 2.1, assumptions A1 and A2, Theorem 2.6, and Proposition 4.4 with equations (4.16)–(4.20) and the accompanying explanation.
The published Springer page was also checked for the same numbered stability statements.
Theorem 2.6 and Proposition 4.4 were not independently proved or audited in full.

Section 2.1, preprint p. 4, assumes a selfadjoint matrix \(A\) and a linear map \(\mathcal S\) that preserves positive semidefinite matrices and is selfadjoint for the normalized Hilbert–Schmidt inner product.
Its convention is \(-M^{-1}=zI-A+\mathcal S[M]\), \(\operatorname{Im}M>0\).
The substitution \(M=-G\) and \(\mathcal S=\Theta\) gives \(G^{-1}=zI-A-\Theta(G)\), \(\operatorname{Im}G<0\).
The normalized trace is \(\langle R\rangle=N^{-1}\operatorname{Tr}R\).

Assumption A1, equation (2.7), p. 5, is the order comparison \(p_1\langle R\rangle I\leq\mathcal S[R]\leq P_1\langle R\rangle I\) for every \(R\geq0\), with \(p_1,P_1>0\).
Assumption A2, equations (2.11)–(2.13), pp. 5–6, imposes faster-than-power spatial decay of \(A\) and \(\mathcal S\), up to a mean-field term, on a pseudometric index set with controlled volume growth.
These are additional hypotheses, not consequences of complete positivity.
Order flatness is also different from strict positivity as an operator on Hilbert–Schmidt space: for \(N>1\), the map \(R\mapsto\sigma\langle R\rangle I\), \(\sigma>0\), is flat but has a nontrivial Hilbert–Schmidt kernel.

Proposition 4.4, equation (4.17), p. 17, assumes A1 and \(\|A\|\leq P_0\); it does not require A2.
It gives a quantitative Hilbert–Schmidt operator-norm bound on \((\mathrm{Id}-\mathcal C_M\mathcal S)^{-1}\), where \(\mathcal C_M[X]=MXM\) in (4.16), in terms of the density and distance from the self-consistent spectrum.
Equations (4.18)–(4.20), pp. 17–18, explicitly derive the response equation

\[
(\mathrm{Id}-\mathcal C_M\mathcal S)\nabla_R G(0)=MR
\]

for a perturbation of the MDE.
The following paragraph explains how the quantitative implicit function theorem upgrades linear stability to a local analytic solution.
Theorem 2.6, pp. 6–7, assumes both A1 and A2 and works on \(\mathbb D_\delta=\{z:\rho(z)+\operatorname{dist}(z,\operatorname{supp}\rho)>\delta\}\).
Its analytic response, entrywise maximum-norm Lipschitz estimate and structured derivative are stronger, quantitatively uniform conclusions.

The substitution \(M=-G\) leaves \(MXM=GXG\), so \(\mathrm{Id}-\mathcal C_M\mathcal S\) becomes \(X\mapsto X-G\Theta(X)G\).
Invertibility of this linear operator and the implicit function theorem allow local continuation of a resolvent solution; an inhomogeneous derivative equation is the corresponding linear-response problem.
These algebraic identifications do not by themselves supply AEK19's quantitative estimates.

The quantitative theorems cannot be applied without their extra assumptions.
In particular, a Hermitian block covariance that sends \(\operatorname{diag}(P,0)\) to \(\operatorname{diag}(0,\eta^*(P))\), for nonzero \(P\geq0\), cannot satisfy the lower flatness bound on the full block algebra.
Nor does a fixed-regularization inverse by itself imply a uniform bound as regularization tends to zero.
Strict positivity as an operator on Hilbert–Schmidt space is a separate condition from A1.

The bounded search used the primary arXiv version and the publisher's matching stability section.
It stopped after the exact operator, assumptions and locators were established.
The random-matrix local laws and universality results were outside this reading scope.
