---
author: Yin
---

# Free unitary conjugation of one member of a commuting normal pair

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X,Y\) be commuting bounded normal elements with diffuse spectral laws in a finite von Neumann algebra with faithful normal probability trace \(\tau\).
Write \(A=W^*(X,Y)\), and let \(w\) be a unitary free from \(A\).
Set \(m=\tau(w)\), \(Z=wYw^*\), \(P=\mathbb C\langle X,Z,X^*,Z^*\rangle\), and \(M=W^*(X,Z)\).
The joint spectral probability of \(X,Y\) in the abelian algebra \(A\) is arbitrary.

1. If \(m\ne0\), then \(M=W^*(A,w)\), and neither coordinate of \((X,Z)\) admits its distinguished actual ACSY derivation on \(P\).
   In particular the noncommuting example with both ordered two-block tests bounded in [C_F0240](Yin_C_F0240_v1.md#commuting-and-noncommuting-realizations) fails actual ACSY at both coordinates.
2. If \(m=0\), then \(W^*(X)\) and \(W^*(Z)\) are free.
   In this case actual ACSY for the pair is equivalent to actual scalar vacua for the two marginal laws, and when these exist the pair has strong duals with both original bounded-vector domains.

Here a distinguished actual derivation at \(X\) is a complex-linear outer derivation on the represented starred core with \(\delta X=1\otimes1,\ \delta Z=0\), whose Hilbert adjoint contains \(1\otimes1\) in its domain.
Diffuseness forces its starred values by the normal relations.
The definition at \(Z\) interchanges the two roles.
The only condition on the freely adjoined unitary in the dichotomy is its first moment.

## Argument

### Recovering the abelian algebra and the conjugating unitary

Work in \(B=W^*(A,w)\) with its free product trace, and let \(\mathbb E_A:B\to A\) be the trace-preserving conditional expectation.
For every Haar unitary \(u\in A\) and \(t\in B\),
\[
       \frac1n\sum_{k=1}^n u^ktu^{-k}\longrightarrow\mathbb E_A t
       \quad\text{in }L^2(B).                                             \tag{1}
\]
Indeed the [free-product Hilbert decomposition](../audits/literature/Voi98/Yin_U005.md#voi98-u005) identifies \(L^2(B)\ominus L^2(A)\) with a sum of outer \(A\)-bimodules \(L^2(A)\otimes K\otimes L^2(A)\).
Here \(K\) runs over the reduced tensor spaces beginning and ending in a centered \(W^*(w)\)-letter, and the two outer factors allow a scalar endpoint.
The identification by concatenation is isometric by expanding each endpoint into its scalar and centered parts.
On a simple tensor the inner product of its \(k\)-th conjugate with another simple tensor tends to zero as \(k\to\infty\), since \(u^k\) converges weakly to zero in \(A\).
For this last fact, pairing with any \(L^1(A)\) density first projects it onto \(W^*(u)\), where the pairing is a Fourier coefficient of an integrable function on the circle.
Density gives the same weak convergence on the entire complement, so conjugation has no nonzero fixed vector there.
Conjugation fixes \(L^2(A)\) because \(A\) is abelian.
The Hilbert mean ergodic theorem, or telescoping on the range of \(1-\operatorname{Ad}u\) and then taking its closure, proves (1).

Assume \(m\ne0\).
For any \(b\in W^*(Y)\), expansion of \(w=m1+w_0\) with \(\tau(w_0)=0\) gives
\[
       \mathbb E_A(wbw^*)=|m|^2b+(1-|m|^2)\tau(b)1 .
\]
The terms linear in \(w_0,w_0^*\) are orthogonal to \(A\), as is \(w_0(b-\tau(b))w_0^*\), by the reduced-word decomposition.
Take in (1) a Haar unitary from \(N=W^*(X)\), which exists by diffuseness.
Since \(wbw^*\in W^*(Z)\), each average belongs to \(M\), and its \(L^2\) limit belongs to \(L^2(M)\).
The displayed bounded limit thus belongs to \(M\), so \(W^*(Y)\subset M\) and \(A\subset M\).
Take now a Haar unitary \(v\in W^*(Y)\) and put \(h_k=wv^kw^*\), \(b_k=h_kv^{-k}\).
Both factors of \(b_k\) belong to \(M\).
By (1),
\[
       \frac1n\sum_{k=1}^n b_k
       =w\,\frac1n\sum_{k=1}^n v^kw^*v^{-k}
       \longrightarrow \bar m w
       \quad\text{in }L^2(B).                                             \tag{2}
\]
Thus \(w\in M\), proving the generation assertion.

### The closed liberation derivation on one conjugating letter

Suppose \(0<|m|<1\) and that a distinguished actual derivation exists at \(X\).
By the [normal liberation criterion](Yin_C_F0238_v1.md#statement), the outer derivation \(\gamma\) on \(P\) given by \(\gamma a=a\otimes1-1\otimes a\) on the \(X\)-marginal and zero on the \(Z\)-marginal has an actual vacuum \(\eta=\gamma^*(1\otimes1)\).
Write \(H=L^2(M)\), \(H_{\rm c}=H\otimes_2H\) and \(\Gamma(t)=t\otimes1-1\otimes t\).
The map \(\Gamma:H\to H_{\rm c}\) is bounded and satisfies the outer derivation rule on \(M\).
The operator \(\gamma\) is closable.
Indeed its core values are algebraic tensors and for \(a,b,p\in P\) one expands \(\gamma(a^*p b^*)\) by Leibniz and pairs with \(1\otimes1\).
The middle term is \(\langle a\otimes b,\gamma p\rangle\).
The other two terms are bounded functionals in \(\|p\|_2\), as is \(\langle\eta,a^*p b^*\rangle\).
Thus all \(a\otimes b\) are in the adjoint domain, a dense set in \(H_{\rm c}\).
The bounded perturbation \(D=\gamma-\Gamma\) is closable with \(\bar D=\bar\gamma-\Gamma\) on \(\operatorname{Dom}\bar\gamma\).

The derivation \(D\) kills the \(X\)-marginal polynomials.
Its closed graph is therefore invariant under their left and right multipliers and their adjoints, acting diagonally on source and outer target.
Normality gives both actions of all of \(N\) on the graph.
The [diffuse graph argument](Yin_C_F0202_v1.md#the-diffuse-coordinate-and-the-graph-of-the-derivation) now gives \((a,0)\in\operatorname{graph}\bar D\) whenever \(a\in N'\cap M\).
Indeed the graph projection takes \((a,0)\) to an \(N\)-central pair, whose coarse component vanishes by diffuseness.
The orthogonal remainder has zero coarse component, so density of the first-coordinate domain forces this remainder to vanish.
As \(A\subset M\) is abelian and contains \(N\), this shows \(\bar\gamma a=\Gamma(a)\) for every \(a\in A\).
The same multiplier invariance for \(\gamma\), which kills the \(Z\)-marginal polynomials, shows that \(\operatorname{graph}\bar\gamma\) is a left and right \(W^*(Z)\)-module with the outer actions on the target.

In particular \(v^{-k}\in\operatorname{Dom}\bar\gamma\) with \(\bar\gamma v^{-k}=\Gamma(v^{-k})\), and \(h_k\in W^*(Z)\) acts on this graph.
It follows that
\[
      \bar\gamma b_k=b_k\otimes1-h_k\otimes v^{-k}.                       \tag{3}
\]
The vectors \(h_k\otimes v^{-k}\) are orthonormal for \(k\ge1\) because \(v\) is Haar and \(h_k\) is unitary.
Their Cesàro means tend to zero in \(H_{\rm c}\).
Together (2), (3), closedness and \(m\ne0\) give \(\bar\gamma w=w\otimes1\).
Every use of a product in (3) comes from a bounded multiplier preserving a closed graph.

### A coarse component with strictly positive product spectral mass

For \(a,b\in N\), the left and right \(N\)-invariance of the graph of \(\bar D\) gives \(\bar D(awb)=a(\bar Dw)b=a\otimes wb\).
Adding \(\Gamma\) and using the actual vacuum pairing in the closed graph yields
\[
 \begin{aligned}
    \langle\eta,awb\rangle
       &=(\tau\otimes\tau)\big(a\otimes wb+awb\otimes1-1\otimes awb\big)\\
       &=m\,\tau(a)\tau(b).
 \end{aligned}                                                           \tag{4}
\]
The last equality uses freeness of \(w\) and \(A\).
Since \(\bar\gamma(ab)=\Gamma(ab)\) has zero double trace, (4) also gives \(\langle\eta,aw_0b\rangle=m\,\tau(a)\tau(b)\), where \(w_0=w-m1\).
Use inner products linear in the second argument and set \(s=1-|m|^2>0\).
The centered free-product Hilbert decomposition gives
\[
     \langle a_1w_0b_1,a_2w_0b_2\rangle
       =s\,\langle a_1,a_2\rangle\,\langle b_1,b_2\rangle
       \qquad(a_j,b_j\in N).
\]
Thus \(\mathcal K=\overline{\operatorname{span}}^{\,2}Nw_0N\) is a coarse \(N\)-bimodule and the orthogonal projection of \(\eta\) onto \(\mathcal K\) is \(\bar m w_0/s\) by (4).
The subspace \(\mathcal K\) reduces both marginal actions, so the joint spectral measure \(\nu_\eta\) of left and right multiplication by \(X\) dominates that of this projection.
For \(\mu\) the law of \(X\), testing rectangles with the displayed tensor inner product gives
\[
              \nu_\eta\ \ge\ \frac{|m|^2}{1-|m|^2}\,\mu\otimes\mu .       \tag{5}
\]
The [critical planar energy bound](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) gives \(\int_{z\ne z'}|z-z'|^{-2}\,d\mu(z)d\mu(z')=\infty\) for every diffuse compactly supported probability \(\mu\) on \(\mathbb C\).
Consequently (5) contradicts the finite inverse-gap integral required by [C_F0238](Yin_C_F0238_v1.md#statement).

To treat the distinguished \(Z\)-coordinate, simultaneously conjugate the pair by \(w^*\) and put the distinguished generator first.
The resulting pair is \((Y,w^*Xw)\) in the same construction with \(X,Y\) exchanged and unitary \(w^*\) of mean \(\bar m\).
Simultaneous tracial conjugation transports the actual derivation by the induced Hilbert and tensor unitaries, preserving the vacuum tensor.
The contradiction therefore applies to that coordinate as well.

### Endpoints and the conditional two-block example

If \(|m|=1\), faithfulness and \(\|w-m1\|_2^2=0\) make \(w\) scalar, so \(Z=Y\) commutes with \(X\).
The derivation at \(X\) applied to the represented relation \([X,Z]=0\) gives \(1\otimes Z-Z\otimes1=0\), which would make \(Z\) scalar.
Likewise the distinguished \(Z\)-derivative forces \(X\) scalar.
Both conclusions contradict diffuseness.

If \(m=0\), every alternating centered word from \(W^*(X),wW^*(Y)w^*\) expands into a reduced word in centered letters from \(A,W^*(w)\), since \(w,w^*\) are centered.
This proves freeness regardless of the joint law in \(A\).
For actual ACSY the two scalar vacua are necessary by restriction to each marginal and orthogonal projection of its vacuum.
Conversely, extending the two scalar derivations by zero on the other factor preserves their vacua by the [centered free-word pairing](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor).
The [free normal estimate](Yin_C_F0162_v1.md#statement), Part B, then gives the strong duals for both coordinates.

The [noncommuting realization in C_F0240](Yin_C_F0240_v1.md#commuting-and-noncommuting-realizations) takes two diffuse commuting disk coordinates for \(X,Y\) and uses \(w=\cos\theta+i\sin\theta\,v\), where \(v\) is a centered free symmetry and \(0<\theta<\pi/2\).
Its mean \(m=\cos\theta\) is in the strict range of (5).
Even though both ordered two-block vacuum functionals are bounded, neither extends to the distinguished actual vacuum on the full represented starred core.

## Provenance

For [T_F0011](../tasks/Yin_T_F0011_v1.md#contract), the check_defect agent developed recovery of the two hidden factors by averaging and the product spectral mass obstruction.
The coordinating agent contributed the closed-graph recovery of the derivative of \(w\), removing a preliminary assumption about a vacuum on its unitary marginal.
The criterion for conjugating a copy of the same normal element by a free unitary appears in [C_F0239](Yin_C_F0239_v1.md#a-conjugated-copy-of-a-normal-marginal).
Here the obstruction applies to every joint spectral law in the abelian base and detects a component outside the ordered two-block tests of C_F0240.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:38 |
| status | open |
| reason | Fix the generated-algebra identity, the obstruction at both coordinates for nonzero unitary mean and the free endpoint for whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary diffuse commuting normal marginals, their unitary conjugation dichotomy and the C_F0240 realization. |
| argument | [Argument](#argument) | Two Cesàro recoveries, graph invariance, the one-letter coarse projection, critical inverse-gap energy and both endpoints. |
| dependency | [Normal liberation criterion](Yin_C_F0238_v1.md#statement) | Necessity for a distinguished actual coordinate, existence of the liberation vacuum and finiteness of its inverse-gap integral. |
| dependency | [Diffuse graph argument](Yin_C_F0202_v1.md#the-diffuse-coordinate-and-the-graph-of-the-derivation) | Bimodule invariance for a closed graph, vanishing of central coarse vectors and inclusion of the relative commutant in its kernel. |
| dependency | [Free-product Hilbert decomposition](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Orthogonality and inner products of centered reduced tensors, the two outer factor actions and the one-letter component. |
| dependency | [Planar critical energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Infinite inverse squared distance energy of a nonzero diffuse compactly supported planar measure. |
| dependency | [Free-core vacuum extension](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | The centered-word pairing when extending a factor derivation by zero on the other factor. |
| dependency | [Free normal bound](Yin_C_F0162_v1.md#statement) | Part B on strong duals for free normal marginals with actual scalar vacua. |
| dependency | [Noncommuting realization](Yin_C_F0240_v1.md#commuting-and-noncommuting-realizations) | The two diffuse disk coordinates, the free two-point unitary and boundedness of both ordered two-block tests in the stated example. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:53 |
| status | proved |
| reason | Adopt the conjugation dichotomy at both coordinates and the full-word obstruction in the disk example after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary diffuse commuting normal marginals, their unitary conjugation dichotomy and the C_F0240 realization. |
| argument | [Argument](#argument) | Two Cesàro recoveries, graph invariance, the one-letter coarse projection, critical inverse-gap energy and both endpoints. |
| dependency | [Normal liberation criterion](Yin_C_F0238_v1.md#statement) | Necessity for a distinguished actual coordinate, existence of the liberation vacuum and finiteness of its inverse-gap integral. |
| dependency | [Diffuse graph argument](Yin_C_F0202_v1.md#the-diffuse-coordinate-and-the-graph-of-the-derivation) | Bimodule invariance for a closed graph, vanishing of central coarse vectors and inclusion of the relative commutant in its kernel. |
| dependency | [Free-product Hilbert decomposition](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Orthogonality and inner products of centered reduced tensors, the two outer factor actions and the one-letter component. |
| dependency | [Planar critical energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Infinite inverse squared distance energy of a nonzero diffuse compactly supported planar measure. |
| dependency | [Free-core vacuum extension](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | The centered-word pairing when extending a factor derivation by zero on the other factor. |
| dependency | [Free normal bound](Yin_C_F0162_v1.md#statement) | Part B on strong duals for free normal marginals with actual scalar vacua. |
| dependency | [Noncommuting realization](Yin_C_F0240_v1.md#commuting-and-noncommuting-realizations) | The two diffuse disk coordinates, the free two-point unitary and boundedness of both ordered two-block tests in the stated example. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0252_v1.md#finding) | The two averaging limits, represented closed graphs, coarse spectral mass, critical divergence, and both trace endpoints. |
