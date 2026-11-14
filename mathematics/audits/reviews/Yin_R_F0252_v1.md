---
author: Yin
---

# Review of free unitary conjugation of a commuting normal pair

The independent review on 2026-11-14T10:46 covers the full [candidate in C_F0243 v1](../../claims/Yin_C_F0243_v1.md#decision-candidate), dated 2026-11-14T10:38.
The reviewing agent had no part in developing this proof and received the fixed claim and the review assignment without development dialogue, exploration notes, author explanations or prior findings about the candidate.
The review checked each of the seven direct inputs at the indicated scope.

## Finding

Both conclusions hold for every joint law of the commuting normal generators with the stated diffuse marginals.
The obstruction for nonzero unitary mean applies separately to each distinguished derivation, including when the two ordered tests in the cited disk example are bounded.

**Recovery of the generators.**
Every reduced tensor outside \(L^2(A)\) has a unique middle pattern starting and ending in a centered \(W^*(w)\)-letter after removing its optional \(A\)-endpoints.
The two endpoints therefore carry the ordinary outer \(A\)-actions, including when one or both endpoints are scalar.
For a Haar unitary \(u\in A\), matrix coefficients of \(u^k\) on each endpoint are Fourier coefficients of \(L^1\) densities on the circle and tend to zero.
Conjugation by \(u\) thus has fixed space precisely \(L^2(A)\).
Its Cesàro averages telescope on the range of \(1-\operatorname{Ad}u\), whose orthogonal complement is the fixed space.
The resulting projection sends \(wbw^*\) to \(|m|^2 b+(1-|m|^2)\tau(b)1\), by centering \(w\) and \(b\) and contracting the scalar part.
Averaging with a Haar unitary of \(W^*(X)\) recovers each \(b\in W^*(Y)\) when \(m\ne0\).
The averages lie in \(M\), and their bounded \(L^2\) limit is fixed by the conditional expectation onto \(M\).
After recovering \(A\), averaging \(v^k w^* v^{-k}\) for Haar \(v\in W^*(Y)\) and multiplying on the left by \(w\) places \(\bar m w\) in \(M\).
Neither averaging argument needs a condition on the joint law beyond the abelian base and the two diffuse marginals.

**Closed graphs and the derivative of the unitary.**
In the strict range \(0<|m|<1\), a distinguished actual vacuum supplies a liberation vacuum \(\eta\) and the finite inverse-gap integral by the forward implication of C_F0238.
Expanding the vacuum test on \(a^*pb^*\) leaves bounded linear functionals of \(p\) in the two endpoint terms, since the core liberation values are finite sums of polynomial tensors.
The middle term tests against \(a\otimes b\), so \(\gamma^*\) has dense domain.
Subtracting the bounded map \(\Gamma(t)=t\otimes1-1\otimes t\) gives a closed graph after taking the closure of \(D=\gamma-\Gamma\).
Its projection commutes with the two \(N=W^*(X)\) actions since \(D\) kills the generating starred polynomials of \(N\).
For \(a\in A\subseteq N'\cap M\) the projection of \((a,0)\) has central coarse component, which vanishes by the equal-trace partition estimate of C_F0202.
The remainder \((a-b,0)\) is orthogonal to a graph with dense first-coordinate domain, hence \(a=b\).
This gives \(\bar\gamma v^{-k}=\Gamma(v^{-k})\).
The left action of \(h_k=wv^kw^*\in W^*(Z)\) preserves the graph of \(\bar\gamma\), because \(\gamma\) kills the other marginal polynomials.
For \(b_k=h_kv^{-k}\) the resulting derivative is \(b_k\otimes1-h_k\otimes v^{-k}\).
The second summands are orthonormal by the Haar law of \(v\), so the graph limit of the averages is \((\bar m w,\bar m w\otimes1)\).
In particular \(\bar D w=1\otimes w\), obtained entirely by bounded actions on the two closed graphs.

**Product measure in the liberation vacuum.**
The graph actions of \(N\) on \(\bar D\) give \(\bar D(awb)=a\otimes wb\).
The double trace of \(\Gamma(awb)\) vanishes, so the vacuum pairing is \(m\tau(a)\tau(b)\).
It is unchanged when \(w\) is replaced by \(w_0=w-m1\), since \(\bar\gamma(ab)=\Gamma(ab)\).
Writing \(s=1-|m|^2\), centered-word inner products identify \(aw_0b\) with \(\sqrt{s}\,a\otimes b\) in the coarse \(N\)-module.
With the inner product linear in its second variable, the orthogonal projection of \(\eta\) onto this module is \(\bar m w_0/s\).
Its joint spectral measure is \((|m|^2/s)\mu\otimes\mu\), and the module reduces both \(N\)-actions, giving the claimed lower bound for \(\nu_\eta\).
Off the null diagonal, C_F0204's planar cell estimate gives mass at least \(cr^2\) within distance \(r\) for all sufficiently small \(r\).
Integration against \(2r^{-3}\,dr\) contradicts the required finite integral.
Conjugation of the pair by \(w^*\), followed by interchanging the labels, carries the other actual derivation and its adjoint vacuum test to precisely the problem with \(Y\) distinguished and unitary mean \(\bar m\).

**Endpoints and the application.**
At \(|m|=1\), \(w=m1\) in the faithful tracial algebra, and differentiating the represented commutation relation would force the omitted coordinate to be scalar.
At \(m=0\), writing each centered \(W^*(Z)\)-letter as \(w b w^*\) makes every alternating mixed centered word reduced in the original free product.
Restriction to the distinguished marginal and projection of its vacuum are valid on the represented core.
In the reverse direction the centered-word extension in C_F0205 only uses freeness of the added factor and the zero derivative there, so it applies to an arbitrary second normal marginal.
Once both vacua exist, C_F0162 Part B, equation (S6), gives both original operator and adjoint domains in \(L^2(M)\) and the generator-first commutators.
For the C_F0240 realization, \(m=\cos\theta\) lies strictly between zero and one, while the density term in the spectral coupling keeps both ordered tests bounded.
The two nonzero length-four commutator components in that construction belong to orthogonal reduced-word spaces.

**Sources and limits.**
Voi98-U005 reconstructs the required alternating tensor representation from centered words in the published article's Section 5, items 5.5–5.8.
The source checking here uses that reconstruction, without a fresh audit of the original article.
The Fourier decay and the averaging step match the circle case of Tao's Exercise 12 and the Hilbert space formulation of von Neumann's mean ergodic theorem in Tao's Theorem 2, respectively.
The latter applies on the separable reducing span of any one vector's integer orbit, and shifting the initial index of the average changes it by a term tending to zero in norm. [Tao, 245C Notes 2, Exercise 12](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/#rll), [Tao, 254A Lecture 8, Theorem 2](https://terrytao.wordpress.com/2008/01/30/254a-lecture-8-the-mean-ergodic-theorem/)
This finding covers the stated conjugation family and the indicated direct-input interfaces.
The universal implication for arbitrary correlated normal tuples remains outside its scope.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [C_F0243 statement](../../claims/Yin_C_F0243_v1.md#statement) | Both moment regimes, both distinguished coordinates and the disk example. |
| [Finding](#finding) | [C_F0243 argument](../../claims/Yin_C_F0243_v1.md#argument) | Whole proof, including generation, closed graphs, product spectral mass and endpoints. |
| [Finding](#finding) | [Normal liberation criterion](../../claims/Yin_C_F0238_v1.md#statement) | Forward implication for a single actual derivation and its finite inverse-gap integral. |
| [Finding](#finding) | [Diffuse graph argument](../../claims/Yin_C_F0202_v1.md#the-diffuse-coordinate-and-the-graph-of-the-derivation) | Graph projection, vanishing of central coarse vectors and relative-commutant inclusion. |
| [Finding](#finding) | [Free-product Hilbert decomposition](../literature/Voi98/Yin_U005.md#voi98-u005) | Reduced-word isometry, endpoint actions and orthogonality of different middle patterns. |
| [Finding](#finding) | [Critical planar energy](../../claims/Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Small-ball lower bound and inverse-square divergence off the diffuse diagonal. |
| [Finding](#finding) | [Free-core extension](../../claims/Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Faithful free-word core and preservation of the actual adjoint vacuum under extension by zero. |
| [Finding](#finding) | [Free normal estimate](../../claims/Yin_C_F0162_v1.md#statement) | Part B under the joint actual condition, including both bounded-vector domains in (S6). |
| [Finding](#finding) | [Noncommuting disk example](../../claims/Yin_C_F0240_v1.md#commuting-and-noncommuting-realizations) | Diffuse marginals, strictly positive mean, noncommutation and both ordered two-block bounds. |
