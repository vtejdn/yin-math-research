---
author: Yin
---

# Independent review of planar bilipschitz invariance of the geometric vacuum energy

For Yin I reviewed the entire [candidate dated 2026-11-14T12:02](../../claims/Yin_C_F0256_v1.md#decision-candidate), its registered inputs and the cited formulas in Tolsa's published paper.
I took no part in developing this version and received no development dialogue, author explanation, exploration notes or previous finding about the candidate.

## Finding

At 2026-11-14T12:04 UTC I found that (1) holds for all compactly supported finite positive planar Radon measures, including the two-sided comparison of the extended energies.
The scalar and mixed vacuum conclusions hold in both directions and compare the squared norms by constants depending only on the indicated coordinate's bilipschitz constant.

### The weighted estimate for Tolsa's constructed top family

I checked the argument against the 2005 journal edition, including the construction's stated hypotheses, the actual split of the packing sum, the terminal-square remark and the image-square conventions. [Tolsa, *Bilipschitz maps, analytic capacity, and the Cauchy integral*, Annals of Mathematics 162, pp. 1243–1304](https://annals.math.princeton.edu/wp-content/uploads/annals-v162-n3-p03.pdf)

For the compact measure with unit growth and finite curvature, Main Lemma 3.1 on p. 1250 supplies the specific top family constructed in the proof and a finite value of its entire weighted sum \(P\).
Its \((16,5000)\)-doubling squares include a root containing the support.
The parameters giving the intermediate estimates belong to this same family.
Equation (5.7) on p. 1270 absorbs the very concentrated part using the fixed high-density threshold and yields \(P\le2P'\).
Equation (5.8) on p. 1271 divides each remaining square's mass among the three terms used in the candidate.
For low-density stops (5.9) and (5.10) give the coefficient \(\eta\) on \(P'\), with \(C_{17}\eta\le1/2\).
For high-curvature stops (5.11) sums the masses of \(Q\) against the squared density of the parent \(R\).
The union of the \(4Q\)'s in (5.8) costs at most the sum of their masses, each bounded by a fixed multiple of the mass of \(Q\) by doubling.
The restriction to parents outside the very concentrated class only decreases the nonnegative sum.

Lemma 5.2(d) on pp. 1268–1269 bounds the pointwise number of sets \(G_{1/2}(R)\) containing a fixed support point.
These are exactly the sets integrated in the third term of (5.8) and in (5.12).
For \(x\in G_{1/2}(R)\subset R/2\), the inclusion \(R\subset B(x,2\ell(R))\) gives \(\theta_\sigma(R)^2\le4(M_1\sigma(x))^2\).
Tonelli and the pointwise overlap bound now give \(4N_1D(\sigma)\) for the entire good-set sum.
Consequently \((1-C_{17}\eta)P'\le C c^2(\sigma)+4C_{17}N_1D(\sigma)\), and (5.7) gives the proposed bound on \(P\).
Remark 5.4 on p. 1272 explicitly uses a terminal contribution in (5.13) to establish the original finite packing estimate by truncation.
The present subtraction is valid on the full family because (3.1) has already established \(P<\infty\) under the original hypotheses.
Its original mass bound is used only for finiteness at this point, so the sharpened numerical estimate uses the three terms just checked.

### Image squares, restrictions and the extended comparison

In §8 the length of an image square is defined to be the original side length, while its density is \(\sqrt2\) times its image mass divided by its actual diameter.
It follows that \(L^{-1}\theta_\sigma(Q)\le\theta_{\phi_\#\sigma}(\phi Q)\le L\theta_\sigma(Q)\).
Every dilation of an image square is the image of the corresponding dilation in the source, so the doubling bounds, root containment and the defining stopping incidences transfer.
The image curves are Ahlfors–David regular with constants controlled by \(L\), and they contain the image good points up to null sets.
The annular integral in Main Lemma 8.1(b) has the same annular domain after pullback and is at most \(L\) times the old integral by the lower distance bound.
The length ordering in 8.1(c) is preserved exactly by the image-square convention, and its density bound follows by the displayed density comparison.
Finally, ball containment gives image growth constant at most \(L\).
These checks verify the hypotheses of Main Lemma 8.1 and the use of its curvature bound in §8.1 on pp. 1290–1291.
The large-scale term in §8.2 on p. 1292 is bounded by the squared root density times the mass of the image support, exactly the mass of its root square.
Thus the entire image curvature is bounded by the strengthened packing sum with a constant depending only on \(L\).

For finite \(G(\mu)\) the centered maximal density is finite almost everywhere.
For open balls of each fixed radius its numerator is lower semicontinuous under translations by Fatou's lemma, so the maximal function is Borel.
Whenever \(B(a,r)\) has positive \(\mu_n\)-mass, it contains a retained point \(x\), and \(B(a,r)\subset B(x,2r)\) gives \(\mu_n(B(a,r))\le2nr\).
This supplies the all-center growth condition even when \(a\) is not a retained point.
The restrictions are finite Radon measures supported in the original compact set.
Replacing \(\mu_n\) by \(\mu_n/(2n)\) multiplies each curvature integral by \((2n)^{-3}\), and the same factor occurs in \(D\) because the maximal function scales linearly and the integration measure supplies the third power.
The normalized estimate therefore gives an image curvature bound independent of the threshold.
The product of the three retained-set indicators increases to one almost everywhere for \(\mu^3\), since each triple with finite maximal densities is retained as soon as \(n\) exceeds their maximum.
Positivity of squared curvature gives the limit by monotone convergence.
For the zero measure the inequalities are immediate.
The centered maximal-density integral transforms by a factor at most \(L^2\) in each direction.
Applying the same curvature and maximal-density estimates to \(\phi^{-1}\) rules out a finite image energy when the source energy is infinite.
Atoms have infinite maximal density and persist under the homeomorphism, consistent with this extended comparison.

### Original scalar and mixed starred cores

The fixed scalar criterion compares the squared norm of the actual marginal vacuum to \(G\) with absolute constants whenever the vacuum exists.
Its equivalence with finite \(G\) therefore gives both directions and the norm comparison for compact probability laws.
For a finite actual tuple, the coordinate homeomorphisms restrict to bounded Borel bijections of compact spectra and preserve each marginal von Neumann algebra.
The invariant-liberation argument extends the marginal prescriptions on bounded graph approximants and restricts the resulting vacuum pairing to each original represented target starred core.
Consequently its joint left-right spectral measure at coordinate \(i\) is exactly the pushforward of the original one by \((\phi_i,\phi_i)\).
Injectivity preserves the diagonal and the two distance bounds put its inverse-gap integral between \(L_i^{-2}I_i\) and \(L_i^2I_i\).
The fixed joint criterion compares the squared mixed vacuum norm with \(G(\mu_i)+I_i\) and reconstructs the actual vacuum on that core.
Applying it separately at every coordinate and then to the inverse homeomorphisms proves the tuple equivalence, including simultaneous changes of correlated coordinates.
Only \(L_i\) enters the comparison at the selected coordinate.

This review checked Tolsa's cited intermediate results and the new use of their combination, taking the construction of the regular curves and the proofs of its high-curvature, low-density and final tree estimates as published inputs.
The operator conclusion concerns actual starred ACSY and leaves the unrestricted mixed problem for the strong bounded-vector domains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0256_v1.md#decision-candidate) | Both geometric energy comparisons and the actual scalar and mixed vacuum consequences. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0256_v1.md#statement) | Extended energies for compact finite positive measures, two-way vacuum existence and coordinatewise norm bounds on original cores. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0256_v1.md#argument) | Full-family weighted estimate, image-square geometry, growth normalization, monotone triple limit, inverse and mixture of marginal and liberation energies. |
| [Finding](#finding) | [Tolsa edition](../literature/Tol05/readme.md#yin-edition) | Independently inspected the 2005 published PDF at the printed pages identified above. |
| [Finding](#finding) | [Tolsa corona input](../literature/Tol05/Yin_U001.md#tol05-u001) | Main Lemma 3.1 including (3.1), Lemma 5.2(d), (5.7)–(5.13), Remark 5.4, Main Lemma 8.1, the image-square conventions and the root bound in §8.2. |
| [Finding](#finding) | [Scalar and joint vacuum criterion](../../claims/Yin_C_F0255_v1.md#statement) | Absolute two-sided scalar norm bounds, diffuse marginals at finite energy and reconstruction on the whole mixed starred core with the additional gap energy. |
| [Finding](#finding) | [Invariant liberation](../../claims/Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Preservation of the actual liberation vacuum under simultaneous Borel relabelling and its transported joint spectral measure. |
