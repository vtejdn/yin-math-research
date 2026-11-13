---
author: Yin
---

# Full dual domains on a closed curve with weighted summable Fourier coefficients

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Use the [three full-core conditions](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) and the [original column cost](Yin_C_F0208_v1.md#statement) for a finite bounded normal generating tuple \(X\) in a finite von Neumann algebra with faithful normal probability trace.
Suppose that \(\sigma(X_i)\subseteq r(\mathbb T)\), where \(r:\mathbb T\to\mathbb C\) is injective, its angular derivative never vanishes and its Fourier series satisfies
\[
        r(z)=\sum_{n\in\mathbb Z}c_n z^n,\qquad
                   \sum_n(1+n^2)|c_n|<\infty .                         \tag{1}
\]
This includes every regular \(C^3\) embedded closed plane curve.
Under \(\mathsf A(X)\), \(c_i(X)<\infty\) and the original right slice \(E_{i,0}\) on the represented starred polynomial core satisfies
\[
             M\Omega\subseteq\operatorname{Dom}\overline E_{i,0}
                            \cap\operatorname{Dom}E_{i,0}^* .
\]
Other coordinates may have arbitrary normal spectra and may be correlated with \(X_i\).

If every coordinate admits either the closed carrier (1) or the [finite disjoint regular arc cover](Yin_C_F0234_v1.md#statement), use the unitary inverse parameter for each closed carrier and the selfadjoint inverse parameter for each arc cover.
The resulting mixed tuple \(Z\) generates \(M\) and
\[
  \mathsf A(X)\ \Longleftrightarrow\ \mathsf A(Z)\
  \Longleftrightarrow\ \mathsf F(Z)\
  \Longleftrightarrow\ \mathsf F(X)\
  \Longleftrightarrow\ \mathsf S(X).
\]
The closed-curve assumption concerns each entire parameter circle even if only a subset carries the marginal law.

## Argument

### The two circle multipliers

On \(\mathbb T^2\) write \(J(z,w)=(r(z)-r(w))/(z-w)\) away from the diagonal and \(J(z,z)=(iz)^{-1}(d/d\theta)r(e^{i\theta})|_{e^{i\theta}=z}\).
For \(n>0\), the secant of \(z^n\) is \(\sum_{a=0}^{n-1}z^{n-1-a}w^a\).
For \(n=-m<0\) it is \(-\sum_{a=0}^{m-1}z^{-1-a}w^{a-m}\).
These expansions agree with the diagonal derivatives and have \(|n|\) terms, each of whose two exponents \(j,k\) satisfies \(|j|+|k|\le |n|+1\).
Thus \(J=\sum_{j,k}a_{jk}z^jw^k\) converges with \(\sum(1+|j|+|k|)|a_{jk}|<\infty\), by (1).
It agrees everywhere with the displayed secant by uniform convergence of the differentiated series.
Its continuous absolute value has positive minimum by injectivity, regularity and compactness.
The [torus Wiener lemma](../audits/literature/Den09/Yin_U002.md#den09-u002), in the recorded Example 20 interface for \(\mathbb Z^2\), gives \(K=1/J=\sum b_{jk}z^jw^k\) with \(\sum|b_{jk}|<\infty\).
In particular both kernels give projective tensor multipliers when evaluated on the unitary parameter.
A \(C^3\) angular parametrization satisfies (1) by the [weighted one-dimensional Fourier estimate](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates), using Parseval for the third derivative.

Put \(h=r^{-1}\) on the image loop.
Condition (1) gives a \(C^2\) angular parametrization.
A local real projection with nonzero derivative gives a local \(C^1\) angle coordinate, and its exponential extends \(h\) into a plane neighborhood of that chart.
Compactness and injectivity allow charts that meet only the corresponding parameter patch.
A smooth partition of unity and a cutoff therefore extend \(h\) to a complex \(C^1\) function on a plane rectangle containing the loop, as in the [inverse chart construction](Yin_C_F0234_v1.md#parameters-on-disjoint-arcs).
The extension need only be circle-valued on the carrier itself.
Hence \(U=h(X_i)\) is unitary, \(r(U)=X_i\) and \(W^*(U)=W^*(X_i)\).

### Transport to the unitary parameter

Assume \(\mathsf A(X)\) and fix its distinguished derivation \(\delta\) with vacuum \(\xi\).
Use the [graph approximation for smooth inverse parameters](Yin_C_F0234_v1.md#transporting-the-actual-derivation-to-a-selfadjoint-coordinate), applied to the real and imaginary parts of \(h\).
Indeed real \(C^1\) polynomial approximation on the rectangle gives uniform approximation of the marginal differences divided by \(z-w\), by integration along the straight chord in the rectangle.
The original derivation evaluates those differences off the null diagonal by the [normal marginal phase](Yin_C_F0076_v1.md#statement), Part 1.
It follows that \(U\) has norm and graph approximants and that \(\bar\delta U=K(U\otimes1,1\otimes U)\).
The same argument applies to every \(U^j\) by extending its function from the carrier using \(h^j\) for positive powers and \(\bar h^{-j}\) for negative powers.
On the carrier, \(|z^j-w^j|\le |j||z-w|\) in unit circle coordinates.
Consequently \(\|\bar\delta U^j\|_2\le |j|\|K\|_\infty\), also for negative \(j\).

Products of the bounded graph approximants converge in the graph with the Leibniz rule.
Omitted-coordinate replacements have zero derivative by the same approximation with omitted polynomials.
On the mixed represented core with \(U\) in place of \(X_i\), possibly with other parameters replaced, apply the inner multiplier \(I_J\), where \(I_{a\otimes b}(v\otimes w)=va\otimes bw\).
It commutes with outer multiplication, and the new derivation \(\theta=I_J\bar\delta\) takes value \(1\otimes1\) at \(U\) since the two marginal kernels multiply to one.
Its value at \(U^*\) equals \(-U^*\otimes U^*\) by the inverse rule, and its values at every omitted starred generator vanish.
For \(U^j\otimes U^k\) the [actual tensor-adjoint calculation](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) gives
\[
 \|\delta^*(U^j\otimes U^k)\|_2\le \|\xi\|_2+(|j|+|k|)\|K\|_\infty.
\]
It applies via the bounded graph approximants just constructed, also for the adjoint powers used to expand the vacuum identity on \(U^{-j}pU^{-k}\).
Thus \(I_J^*(1\otimes1)\) belongs to the actual adjoint domain by the weighted series for \(J\), and testing on the new core gives the actual vacuum of \(\theta\).
For an unchanged omitted distinguished derivation on replacing another coordinate, all powers or local parameter approximants of that replaced coordinate still have zero derivative.
Its restriction to the new core retains its old vacuum by graph closure.
When an arc parameter is distinguished instead, the same product argument permits replacing omitted coordinates by either type of parameter, and the arc multiplier and vacuum calculation of C_F0234 apply unchanged.
These constructions give \(\mathsf A(Z)\) when all coordinates have the indicated covers.

### Transport back to the original domains

For the distinguished unitary the [unitary polynomial-core calculation](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds), as verified with arbitrary omitted normal coordinates in the [unitary-coordinate proof](Yin_C_F0158_v2.md#the-unitary-coordinate-and-its-real-twist), applies to \(\theta\) on the mixed core.
Its only other generator inputs are the zero derivatives of the omitted generators and their adjoints.
It gives the closed canonical operator \(E^U\) and its adjoint on all bounded vectors with operator-norm-to-Hilbert bounds, with operator-first commutator \(P_\Omega\) at \(U\) and zero at the other generators.
The extension of the core commutators to all bounded inputs follows by the bounded graph argument in [the full-domain transport](Yin_C_F0234_v1.md#full-domain-witnesses-and-their-transport).
For the arc coordinates of a mixed parameter tuple the same argument there supplies the corresponding selfadjoint witnesses.

Using the finite Laurent sums for \(r\), the inverse rule for the commutator with \(U^{-1}\), and (1), we obtain on all bounded vectors
\[
                 [E^U,L_{X_i}]=\Theta(J),\qquad \Theta(a\otimes b)=aP_\Omega b .
\]
Indeed the coordinate operators converge in norm, and the uniformly convergent secants give convergence of the kernels in coarse and hence Hilbert–Schmidt norm.
Omitted commutators remain zero under these Laurent approximations and under the polynomial approximations for the real arc parameters.
The [projective correction formula](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) therefore gives \(Q_K(E^U)\) with commutator \(P_\Omega\) at \(X_i\) and zero at the others.
Here \(Q_{a\otimes b}(E)=\rho(a)E\rho(b)\) for right multiplication \(\rho(a)\).
Absolute projective convergence for \(K\) and the bounded restriction of \((E^U)^*\) yield an actual adjoint on all bounded vectors by the reversed, conjugated series.
Negation gives the generator-first strong witness.
This applies equally when \(\mathsf A(Z)\) is given directly, and the arc restoration in C_F0234 covers the remaining coordinates in this case.

Adjoining two free Haar unitaries leaves the distinguished carrier unchanged and preserves its original vacuum by [the column criterion](Yin_C_F0208_v1.md#statement).
The construction just given supplies a bounded witness on the enlargement, so \(c_i(X)<\infty\) by that theorem.
Apply it also to the tuple of adjoints, whose conjugated loop still satisfies (1) and whose actual conjugate companion exists by C_F0076, Part 1.
The right cut for the companion on an adjointed input is the tracial adjoint of the original left cut.
Hence both original cuts are bounded, and [C_F0072, Part B](Yin_C_F0072_v1.md#statement) gives the two domains of the original canonical slice itself.

Finally if \(\mathsf F(X)\) holds, the [bare normal commutator theorem](Yin_C_F0070_v1.md#statement), Part A, gives the normalized bounded maps and their forced marginal starred kernels.
Applying the same plane \(C^1\) approximations to the inverse circle and arc parameters gives the commutator \(\Theta(K_i)\) at the distinguished new coordinate and zero at the others.
Projective correction by \(J_i\) gives a normalized bare witness at each new parameter.
Thus \(\mathsf F(Z)\) holds, which is equivalent to \(\mathsf A(Z)\) for this mixed unitary and selfadjoint tuple by [C_F0071, Part D](Yin_C_F0071_v2.md#statement).
Restriction gives \(\mathsf S(X)\Rightarrow\mathsf F(X)\), and C_F0070, Part C, gives \(\mathsf S(X)\Rightarrow\mathsf A(X)\).
This proves all the stated comparisons.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:46 |
| status | open |
| reason | The weighted Fourier condition on a regular loop, the distinguished original domains and the joint mixed-carrier comparison are fixed for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The single-coordinate full column and canonical domains under (1) and the equivalences for mixed arc and loop carriers. |
| argument | [Argument](#argument) | Weighted Laurent secants, inverse Wiener multiplier, graph and adjoint transport, reconstruction and the mixed bare converse. |
| dependency | [Torus Wiener lemma](../audits/literature/Den09/Yin_U002.md#den09-u002) | Example 20, invertibility in the unweighted Fourier algebra of the two-torus for a nonvanishing function with absolutely summable coefficients. |
| dependency | [Weighted Fourier estimate](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | The one-dimensional Parseval estimate verifying (1) for a periodic regular C3 parametrization. |
| dependency | [Arc coordinate theorem](Yin_C_F0234_v1.md#statement) | Arc parameters, local inverse charts, graph limits, actual vacua and bounded witness transport for arc coordinates, including mixed cores with zero omitted derivatives. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Part 1, diffuse law, normal marginal divided difference, closability and conjugate companion. |
| dependency | [Actual tensor adjoint](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Adjoint bounds for elementary tensors with bounded graph approximants and convergence in the adjoint graph. |
| dependency | [Unitary core bounds](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | The single-coordinate unitary calculation and actual original unitary domains in that core. |
| dependency | [Omitted normal coordinates](Yin_C_F0158_v2.md#the-unitary-coordinate-and-its-real-twist) | The same unitary calculation with arbitrary other coordinates at which the derivation vanishes on generators and adjoints. |
| dependency | [Projective correction](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) | Formulas (G10)–(G12) for commutators and reversed adjoints on all bounded inputs. |
| dependency | [Column criterion](Yin_C_F0208_v1.md#statement) | Two-Haar preservation of the old vacuum and the lower bound on the enlarged bounded-dual cost. |
| dependency | [Original canonical domains](Yin_C_F0072_v1.md#statement) | Part B for both original bounded cuts. |
| dependency | [Bare normal commutators](Yin_C_F0070_v1.md#statement) | Parts A and C, normalized starred kernels under the bare condition and actual vacua under the strong condition. |
| dependency | [Mixed bare comparison](Yin_C_F0071_v2.md#statement) | Part D, equivalence of actual ACSY and bare full-domain duals for the parameter tuple. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:50 |
| status | proved |
| reason | Independent review verifies the weighted Laurent secant, the reciprocal Fourier multiplier, actual adjoints and the mixed arc and loop equivalence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The single-coordinate full column and canonical domains under (1) and the equivalences for mixed arc and loop carriers. |
| argument | [Argument](#argument) | Weighted Laurent secants, inverse Wiener multiplier, graph and adjoint transport, reconstruction and the mixed bare converse. |
| dependency | [Torus Wiener lemma](../audits/literature/Den09/Yin_U002.md#den09-u002) | Example 20, invertibility in the unweighted Fourier algebra of the two-torus for a nonvanishing function with absolutely summable coefficients. |
| dependency | [Weighted Fourier estimate](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | The one-dimensional Parseval estimate verifying (1) for a periodic regular C3 parametrization. |
| dependency | [Arc coordinate theorem](Yin_C_F0234_v1.md#statement) | Arc parameters, local inverse charts, graph limits, actual vacua and bounded witness transport for arc coordinates, including mixed cores with zero omitted derivatives. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Part 1, diffuse law, normal marginal divided difference, closability and conjugate companion. |
| dependency | [Actual tensor adjoint](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Adjoint bounds for elementary tensors with bounded graph approximants and convergence in the adjoint graph. |
| dependency | [Unitary core bounds](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | The single-coordinate unitary calculation and actual original unitary domains in that core. |
| dependency | [Omitted normal coordinates](Yin_C_F0158_v2.md#the-unitary-coordinate-and-its-real-twist) | The same unitary calculation with arbitrary other coordinates at which the derivation vanishes on generators and adjoints. |
| dependency | [Projective correction](Yin_C_F0137_v1.md#projective-correction-of-full-domain-operators) | Formulas (G10)–(G12) for commutators and reversed adjoints on all bounded inputs. |
| dependency | [Column criterion](Yin_C_F0208_v1.md#statement) | Two-Haar preservation of the old vacuum and the lower bound on the enlarged bounded-dual cost. |
| dependency | [Original canonical domains](Yin_C_F0072_v1.md#statement) | Part B for both original bounded cuts. |
| dependency | [Bare normal commutators](Yin_C_F0070_v1.md#statement) | Parts A and C, normalized starred kernels under the bare condition and actual vacua under the strong condition. |
| dependency | [Mixed bare comparison](Yin_C_F0071_v2.md#statement) | Part D, equivalence of actual ACSY and bare full-domain duals for the parameter tuple. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0245_v1.md#whole-proof-finding) | Complete proof, including the original single-coordinate column and both canonical domains and the converse for mixed parameter tuples. |
