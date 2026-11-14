---
author: Yin
---

# Planar bilipschitz invariance of the geometric vacuum energy and actual normal ACSY

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(\mu\) be a compactly supported finite positive Radon measure on the plane and let \(\phi:\mathbb C\to\mathbb C\) be a bilipschitz homeomorphism with bi-Lipschitz constant \(L\ge1\).
Put \(M_1\mu(x)=\sup_{r>0}\mu(B(x,r))/r\), write \(c^2(\mu)\) for the integral of squared Menger curvature with respect to \(\mu^3\), and set \(G(\mu)=c^2(\mu)+\int(M_1\mu)^2\,d\mu\).
Then
\[
 c^2(\phi_\#\mu)\le C_L G(\mu),\qquad
 C_L^{-1}G(\mu)\le G(\phi_\#\mu)\le C_L G(\mu).                       \tag{1}
\]
The comparisons include infinite energies and use an enlarged \(C_L\) in the second estimate.
There is no uniform linear-growth assumption on \(\mu\).

For a compactly supported probability measure, an actual scalar conjugate variable exists for \(\mu\) if and only if one exists for \(\phi_\#\mu\).
Their squared norms are comparable up to constants depending only on \(L\).
More generally, let \(X=(X_i)_{i=1}^d\) be bounded normal generators of a finite von Neumann algebra with faithful normal probability trace, and set \(Y_i=\phi_i(X_i)\) for globally bilipschitz plane homeomorphisms \(\phi_i\).
Then \(X\) satisfies actual starred ACSY if and only if \(Y\) does, and the squared joint vacuum norms at coordinate \(i\) are comparable with constants depending only on the bi-Lipschitz constant of \(\phi_i\).
The result concerns the original represented mixed starred cores of the two tuples with arbitrary correlations.
The canonical bounded-vector domains in the unrestricted mixed case remain open.

## Argument

### Estimating the good sets in Tolsa's packing sum

Write \(D(\sigma)=\int(M_1\sigma)^2\,d\sigma\).
First suppose that a nonzero compactly supported finite measure \(\sigma\) has finite curvature and satisfies \(\sigma(B(x,r))\le r\) for every center and radius.
Apply Main Lemma 3.1 of [Tolsa's corona construction](../audits/literature/Tol05/Yin_U001.md#tol05-u001) to obtain his top squares, regular curves and stopping families.
For \(\theta_\sigma(R)=\sigma(R)/\ell(R)\), the original packing theorem gives
\[
                    P=\sum_{R\in{\rm Top}}\theta_\sigma(R)^2\sigma(R)<\infty.
\]
We use this finiteness from the published theorem before seeking an estimate of \(P\) by \(c^2(\sigma)+D(\sigma)\).
It justifies absorption of finite totals in the same family.
In particular the terminal-square estimate of Remark 5.4 already serves its original purpose of establishing finiteness.

Let \(P'\) be the sum over top squares outside the very concentrated class \(VC\).
The source's (5.7) gives \(P\le2P'\).
For these remaining squares, (5.8) splits their mass among low-density stops, high-curvature stops and a good set \(G_{1/2}(R)\) in \(R/2\).
After multiplication by \(\theta_\sigma(R)^2\) and summation, (5.10) bounds the low-density contribution by \(\eta P'\) before its factor \(C_{17}\) in (5.8).
The stopping parameters are chosen as in the source so that \(C_{17}\eta\le1/2\).
For the high-curvature contribution, doubling gives \(\sigma(4Q)\le C\sigma(Q)\) for the stopping squares \(Q\), so (5.11) supplies a bound \(C c^2(\sigma)\) including the factor in (5.8).
These constants are fixed for unit growth.

For \(x\in G_{1/2}(R)\) the ball \(B(x,2\ell(R))\) contains \(R\).
Thus \(\theta_\sigma(R)\le2M_1\sigma(x)\).
Lemma 5.2(d) bounds \(\sum_R1_{G_{1/2}(R)}(x)\) by an absolute \(N_1\) on the support.
Keeping the density inside this sum in place of the global bound in (5.12) gives
\[
 \sum_R\theta_\sigma(R)^2\sigma(G_{1/2}(R))
       \le4\int(M_1\sigma)^2\sum_R1_{G_{1/2}(R)}\,d\sigma
       \le4N_1D(\sigma).
\]
Hence \(P'\le C_{17}\eta P'+C c^2(\sigma)+4C_{17}N_1D(\sigma)\).
Absorbing in \(P'\) first and then applying (5.7) gives
\[
                            P\le C\big(c^2(\sigma)+D(\sigma)\big).       \tag{2}
\]
The coordinating agent identified the weighted replacement for (5.12) and the normalized restrictions used below.
The agent preparing this argument observed that the original finite packing theorem allows the weighted summation on the full family without a second terminal-square argument.

### Curvature of the push-forward and removal of the growth bound

The measure \(\widetilde\sigma=\phi_\#\sigma\) has linear growth with constant at most \(L\).
Use the very same image family in §8.1 of [Tolsa's proof of Theorem 1.3](../audits/literature/Tol05/Yin_U001.md#tol05-u001).
The image root contains its support and the doubling property persists because dilations of image squares there are defined by images of the original dilations.
Bi-Lipschitz distortion preserves Ahlfors–David regularity of the comparison curves and carries their good points to the image curves.
Containment and intersection with the enlarged stopping squares are preserved, and replacing each inverse distance in the source's annular integral by its image costs at most \(L\).
The density bound on squares meeting good points or the specified stops is preserved up to a constant depending on \(L\), since image side lengths and densities are comparable to the original ones.
These are the hypotheses (a)–(c) of Main Lemma 8.1 with the transported family.
The lemma gives the image curvature bounded by its image packing sum, and this sum is at most \(C_L P\) by the diameter comparison.
The separate largest-scale term in §8.2 is included through the root contribution \(\theta_{\widetilde\sigma}(\phi(R_0))^2\widetilde\sigma(\mathbb C)\).
Thus (2) estimates the whole image curvature by \(C_LG(\sigma)\).

Now let \(G(\mu)<\infty\) and put \(\mu_n=1_{\{M_1\mu\le n\}}\mu\) for positive integers \(n\).
The centered maximal density is Borel, as follows from lower semicontinuity of the mass of an open ball under translation and the supremum over radii.
For any ball \(B(a,r)\) with positive restricted mass, take \(x\in B(a,r)\) with \(M_1\mu(x)\le n\).
Then \(\mu_n(B(a,r))\le\mu(B(x,2r))\le2nr\).
This proves growth for every center, including points in the closure of the retained set.
Each \(\mu_n\) has compact support and \(c^2(\mu_n)\le c^2(\mu)\) by positivity.
For nonzero \(\mu_n\) apply the unit-growth estimate to \(\sigma=\mu_n/(2n)\).
Both curvature and \(D\) are homogeneous of degree three in the measure, so multiplication by \((2n)^3\) yields
\[
        c^2(\phi_\#\mu_n)\le C_LG(\mu_n)\le C_LG(\mu).                  \tag{3}
\]
The last inequality also uses \(M_1\mu_n\le M_1\mu\).
The sets in these restrictions increase to a set of full \(\mu\)-measure because \(D(\mu)<\infty\).
In the triple integral for image curvature, the product of the three restrictions increases to one \(\mu^3\)-almost everywhere.
Monotone convergence in (3) therefore includes all triples, even those whose three points enter at different thresholds.
The first inequality of (1) follows for finite \(G(\mu)\), and is immediate as an extended inequality otherwise.
Finally \(M_1(\phi_\#\mu)(\phi(x))\le L M_1\mu(x)\) by ball containment, and the same estimate applies to \(\phi^{-1}\).
This gives both inequalities for \(G\).

### Scalar and joint conjugate variables

For a probability law the [geometric scalar vacuum criterion](Yin_C_F0255_v1.md#statement) equates finite \(G\) with an actual represented scalar vacuum and compares \(G\) with its squared norm, proving the asserted scalar conclusions.
If \(X\) has full actual ACSY, each transformed marginal therefore has an actual scalar vacuum.
On the compact spectra each \(\phi_i\) restricts to a bounded Borel change with Borel inverse.
The [invariant liberation argument](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) supplies the same partial liberation vacuum on the new mixed core, with joint spectral measure \((\phi_i,\phi_i)_*\nu_i\).
Thus the new inverse-square-gap energy lies between \(L_i^{-2}\) and \(L_i^2\) times its original value, with \(L_i\) the bi-Lipschitz constant of \(\phi_i\).
The [joint criterion and norm comparison](Yin_C_F0255_v1.md#statement) now give the forward ACSY implication and the comparison at each coordinate.
Applying the same argument to the inverse homeomorphisms proves the reverse implication.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:02 |
| status | open |
| reason | Fix the weighted packing estimate, curvature transfer without a uniform density bound and the scalar and joint vacuum consequences for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two-sided geometric energy bounds for global bilipschitz homeomorphisms and coordinatewise preservation of actual scalar and mixed vacua. |
| argument | [Argument](#argument) | Weighted good sets, absorption in the nonconcentrated class, transported corona geometry, cubic normalization of restrictions, all-triple limit and invariant liberation. |
| dependency | [Tolsa's published construction](../audits/literature/Tol05/Yin_U001.md#tol05-u001) | Main Lemmas 3.1 and 8.1, Lemma 5.2(d), equations (5.7)–(5.12), and the image family in §8.1 under normalized growth. |
| dependency | [Geometric scalar and joint vacuum criteria](Yin_C_F0255_v1.md#statement) | Scalar equivalence and norm comparison, and the joint criterion including the inverse-gap energy at each coordinate. |
| dependency | [Invariance of partial liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Preservation of the liberation vacuum and push-forward of its left-right spectral measure upon changing all coordinates on their original mixed cores. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:06 |
| status | proved |
| reason | Adopt planar bilipschitz invariance of the geometric energy and the actual scalar and mixed vacua after independent review of the weighted corona argument. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two-sided geometric energy bounds for global bilipschitz homeomorphisms and coordinatewise preservation of actual scalar and mixed vacua. |
| argument | [Argument](#argument) | Weighted good sets, absorption in the nonconcentrated class, transported corona geometry, cubic normalization of restrictions, all-triple limit and invariant liberation. |
| dependency | [Tolsa's published construction](../audits/literature/Tol05/Yin_U001.md#tol05-u001) | Main Lemmas 3.1 and 8.1, Lemma 5.2(d), equations (5.7)–(5.12), and the image family in §8.1 under normalized growth. |
| dependency | [Geometric scalar and joint vacuum criteria](Yin_C_F0255_v1.md#statement) | Scalar equivalence and norm comparison, and the joint criterion including the inverse-gap energy at each coordinate. |
| dependency | [Invariance of partial liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Preservation of the liberation vacuum and push-forward of its left-right spectral measure upon changing all coordinates on their original mixed cores. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0265_v1.md#finding) | The sharpened top-square packing estimate, image geometry, cubic restriction limit and both directions on the original mixed cores. |
