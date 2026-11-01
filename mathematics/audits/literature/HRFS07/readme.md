# HRFS07: half-plane uniqueness for the operator-valued quadratic equation

On 2026-10-10 the literature-reading agent for Yin inspected the published [HRFS07](../../../literature/pdf/HRFS07--journal.pdf), IMRN 2007, article rnm086, and compared the relevant passages with the retained [arXiv v1](../../../literature/pdf/HRFS07.pdf).
The published version has 15 pages; the preprint has 14.
The published locators used below are Section 2.1 on p. 4, Theorem 2.1 and Remark 2.2 on p. 5, and Section 3, including Theorem 3.1 and Proposition 3.2 and their application, on pp. 6–8.
Corresponding preprint locators are pp. 4–7.
The strict-half-plane definition and the displayed hypothesis on the map were also visually checked in both versions.
This is a selected statement, applicability and proof-mechanism reading, not a whole-paper proof audit.

Theorem 2.1 solves \(VW+\eta(W)W=I\) uniquely in the strict right half-plane of a unital C*-algebra and gives convergence of the iteration \(W\mapsto[V+\eta(W)]^{-1}\).
Its printed setting assumes \(\operatorname{Re}V>0\), an analytic map from the strict right half-plane into itself, and boundedness of that map on norm-bounded sets.
Section 3 obtains contraction in a holomorphically invariant metric on suitable bounded domains, by the Earle–Hamilton theorem stated there; it does not claim ordinary operator-norm contraction on the entire half-plane.
Remark 2.2 explicitly uses uniqueness to identify two Cauchy transforms satisfying the same equation and the same positivity condition.
The source's references for Earle–Hamilton and the Cauchy-transform example were not independently audited in this reading.

For a matrix Dyson equation with Hermitian A, positive linear Theta, and Im(w)>0, write \(Z=wI-A\), \(G^{-1}=Z-\Theta(G)\), and set \(W=iG\), \(V=-iZ\).
For Im(G)<0, \(\operatorname{Re}W=-\operatorname{Im}G>0\), \(\operatorname{Re}V=\operatorname{Im}Z>0\), and the equation becomes \(VW+\Theta(W)W=I\).
A degenerate positive linear map need not map the strict right half-plane into itself, so literal applicability requires one additional, elementary substitution: choose \(0<\delta<\lambda_{\min}(\operatorname{Re}V)\), put \(V'=V-\delta I\), and put \(\eta'(W)=\Theta(W)+\delta I\).
The pair \((V',\eta')\) satisfies the printed hypotheses and gives exactly the same equation and fixed-point map.
Thus no strict positivity assumption on the covariance map is needed for this application.
Independently, the estimates in Proposition 3.2 use only \(\operatorname{Re}\Theta(W)\geq0\), with strictness supplied by \(\operatorname{Re}V>0\).

This is a direct established reference for the existence/uniqueness framework and for identification of a physical Cauchy-transform solution.
Uniqueness alone does not imply invertibility of the linearized Dyson equation; that requires a separate stability estimate, such as a strict weighted row/column contraction.
The selected source interface supplies no affine determinant variational formula, Hessian formula or spectral-gap criterion.

The bounded search began with the canonical bibliography and the already identified public primary paper.
It checked the published author PDF and arXiv version rather than adding secondary sources.
No comprehensive priority search or proof review of the source's applications and numerical sections is claimed.
