# Pop03: strict positive defects and positive-map stability

On 2026-10-10 the literature-reading agent for Yin inspected [Pop03, arXiv:math/0310113v1](../../../literature/pdf/Pop03--arxiv-v1.pdf), 37 pages, submitted 8 October 2003.
The canonical work was published in Journal für die reine und angewandte Mathematik 561 (2003), pp. 87–129.
The selected reading covers the introduction, Lemma 5.5 on printed/PDF p. 24, Lemma 5.8 and Theorem 5.9 on pp. 25–26, and their displayed proofs.
This is a selected statement and proof-mechanism reading, not an independent whole-paper audit.
All mathematical locators here refer to the retained preprint.

Lemma 5.5 states that a positive linear map \(\phi\) on \(\mathcal B(H)\) is similar, by conjugating its matrix arguments, to a positive map of norm less than one exactly when there is an invertible positive \(R\) with invertible positive defect \(R-\phi(R)\).
Theorem 5.9, for a weak-star-continuous positive map, relates this strict contractive similarity to \(r(\phi)<1\) and solvability of \(X-\phi(X)=R\) for every positive invertible \(R\).
The positive solution is unique and equals the norm-convergent series \(\sum_{k\geq0}\phi^k(R)\).
Weak-star continuity is automatic on finite matrix algebras; complete positivity is sufficient but is stronger than the source's positivity assumption.

A strict positive defect is a certificate of spectral radius below one, which gives a positive Neumann-series inverse for \(I-\phi\).
For example, a positive invertible D satisfying \(D-\mathcal S(D)=G_0^2>0\), with G_0 Hermitian and invertible, supplies such a certificate for \(\mathcal S\).
The source criterion neither constructs that certificate nor identifies a physical Dyson solution or proves a gap for a semicircular pencil.
The strict defect, rather than a merely nonnegative one, is essential.

One local typographical issue was checked in Lemma 5.5's forward proof: from \(\phi(QQ^*)\leq cQQ^*\), with \(c<1\), the displayed \(R-\phi(R)=(1-c)R\) must be the lower bound \(R-\phi(R)\geq(1-c)R\).
That lower bound is exactly what the proof needs, so this does not obstruct the criterion or its use here.
No unrelated part of the source was re-audited because of this issue.

The bounded search followed the strict-defect/Stein-equation connection after checking existing local sources, then read the primary preprint and the publisher-deposited DOI metadata.
It stopped after the exact criterion and finite-dimensional applicability were established.
No claim of earliest attribution is made.
