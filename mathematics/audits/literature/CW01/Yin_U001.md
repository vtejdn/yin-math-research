---
author: Yin
---

# CW01: the log-concave polynomial sublevel input at q equals one

<a id="cw01-u001"></a>
## Inspected source and accepted scope

The source is the [Carbery--Wright author version](readme.md#author-version).
Direct visual inspection covered its title page, the real-or-complex Banach-space convention in the introduction on printed/PDF p. 2, and Theorems 7--8 with the following log-concavity definition on printed/PDF p. 13.
The established \(q=1\) instance of Theorem 8 is accepted as an input after checking its precise statement and the application below.
Its original proof, the other parameter ranges, and the cited localization results were not reviewed.
This is source-statement and applicability inspection, not an independent review of a project proof.

<a id="log-concavity-definition"></a>
## Definition: the source's affine-support log-concave law

A probability measure on \(\mathbb R^m\) is log-concave in the source's convention if it is supported on an affine subspace \(L\), and its density relative to Lebesgue measure on \(L\) is \(e^{-h}\), where the effective domain of \(h\) and the restriction of \(h\) to that domain are convex.
An additive normalizing constant may be included in \(h\).
This convention includes the zero-dimensional Dirac case.
A one-dimensional nondeterministic such law has a log-concave density on an interval.
Independent products remain in this class because their affine supports form a product and their negative log densities add.
An invertible affine change of the nondegenerate coordinates preserves the class.
Thus a product containing deterministic coordinates can be treated on its remaining affine support.
These product and coordinate observations are elementary local checks of the definition.

<a id="theorem-eight-q-one"></a>
## Theorem 8 at q equals one

Let \(X\) be a real or complex Banach space with norm \(\|\cdot\|_X\), let \(d\ge1\), and let \(p:\mathbb R^m\to X\) be a polynomial of degree at most \(d\).
For a log-concave probability measure \(\nu\), the inspected \(q=1\) case gives an absolute constant \(C_0\) such that
\[
 \left(\int\|p(x)\|_X^{1/d}\,d\nu(x)\right)
 \alpha^{-1/d}
 \nu\{x:\|p(x)\|_X\le\alpha\}
 \le C_0,\qquad\alpha>0.
\]
The bound is dimension-free and uniform over the coefficients and the Banach norm.
The statement above is the direct \(q=1\) specialization, not an extension inferred from the scalar-real case.
The complex scalar case uses \(X=\mathbb C\) with its modulus.
Restricting a polynomial to an affine support preserves its degree.

<a id="logarithmic-application-interface"></a>
## Checked application interface and limits

If \(p\ne0\) almost surely and \(a=\int|p|^{1/d}\,d\nu\) is finite, then \(a>0\).
Taking \(\alpha=a^d e^{-t}\) in the inspected theorem gives
\(\nu\{\log|p|-d\log a\le-t\}\le C_0e^{-t/d}\).
Markov's inequality applied to \(|p|^{1/d}\) gives the corresponding upper bound \(e^{-t/d}\).
These two substitutions are local deductions from the inspected statement.
The complete row-replacement moment, martingale and planar arguments belong to the consuming project theorem.

For any fixed finite-dimensional polynomial, finite first moments of the coordinates suffice for finiteness of \(a\), since \(|p(x)|^{1/d}\le C_p(1+\|x\|)\).
There is no coefficient-independent upper bound on \(a\); the application instead cancels its deterministic logarithmic center between two original-law copies.
The theorem does not apply to a nontrivial atomic law merely because it has finite moments.
It also supplies no estimate for fluctuations of a conditional center left by separately conditioning on non-log-concave coordinates.

The targeted source search sought the Carbery--Wright polynomial sublevel theorem for general log-concave measures, beyond the Gaussian use already mentioned in the local Han26 inspection.
The author-hosted PDF supplies the necessary theorem directly.
No broader literature search or source-proof inspection is represented by this unit.
