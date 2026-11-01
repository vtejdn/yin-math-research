# AZGL+18: capacity as a geodesically convex optimization problem

On 2026-10-10 the literature-reading agent for Yin inspected [AZGL+18, arXiv:1804.01076v1](../../../literature/pdf/AZGL+18--arxiv-v1.pdf), the 57-page full preprint.
The arXiv submission is dated 3 April 2018; its title page says 3 November 2017, version 1.
The canonical work is the STOC 2018 proceedings article, pp. 172–181.
The author-hosted 10-page proceedings PDF and publisher-deposited Crossref record were inspected for bibliographic identity, DOI and page range, while the mathematical locators below refer to the retained full preprint.

Section 1.1, printed pp. 1–3 (PDF pp. 2–4), defines the positive-definite geodesic \(A^{1/2}(A^{-1/2}BA^{-1/2})^tA^{1/2}\), completely positive operator scaling, and \(\operatorname{cap}(T)=\inf_{X>0,\det X=1}\det T(X)\).
Equation (1.1), printed p. 2, is \(\log\det T(X)-\log\det X\).
The passage explains that this function is geodesically convex and, for positive capacity, its infimum is \(\log\operatorname{cap}(T)\).
It also relates an attained capacity minimizer to scaling the coefficient tuple into doubly stochastic form.
Theorem M1, printed p. 3, is explicitly labelled informal and describes the algorithmic capacity approximation.
The selected reading checked these statements and the surrounding definitions; it did not audit the algorithmic proofs or establish complexity bounds for a new problem.

The source connects homogeneous capacity, positive-definite geodesics, operator scaling and noncommutative optimization.
Its geodesic convexity concerns the homogeneous capacity function.
It does not establish geodesic convexity or an efficient algorithm for a general affine determinant function, and it does not identify capacity attainment with invertibility of an evaluated semicircular pencil.
Its arithmetic and input-size conventions must also be retained before quoting algorithmic complexity.

The bounded search checked the existing Gur04 and GGOW20 context before following this primary geodesic-optimization lead.
The complete ordered author list was retained; the canonical key uses both components of Allen-Zhu's surname.
No priority conclusion or exhaustive operator-scaling survey is claimed.
