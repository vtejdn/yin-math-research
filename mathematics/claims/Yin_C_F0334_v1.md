---
author: Yin
---

# A normal coordinate free over a two-point marginal algebra from its projection coefficient

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

In a finite von Neumann algebra with faithful normal probability trace let \(Z\) be a bounded normal generator of \(A=W^*(Z)\) with diffuse law \(\mu\).
Let \(s\) be a centered selfadjoint unitary, put \(M=W^*(A,s)\), and on the represented starred polynomial algebra of \(Z,s\) assume an actual relative distinguished derivative \(\delta Z=1\otimes1,\ \delta s=0,\ \xi=\delta^*(1\otimes1)\).
Suppose \(A\) contains a centered Borel sign \(a=a(Z)\) such that \(A\) and \(N=W^*(a,s)\) are free with amalgamation over \(B=W^*(a)\) for the trace-preserving conditional expectation.
This means every alternating product of elements of the two algebras centered over \(B\) has zero \(B\)-expectation.
Let \(e_\pm=(1\pm a)/2,\ \xi_\mu=\mathbb E_A\xi,\ \gamma=I_{z-w}\delta,\ \eta=\gamma^*(1\otimes1)\), and put
\[
 J=\iint_{z\ne w}\frac{|a(z)-a(w)|^2}{|z-w|^2}\,d\mu(z)d\mu(w).
\]

Then \(\eta\in L^2(N)\) and its two diagonal sign blocks vanish.
Its joint spectral measure at \(Z\) is exactly
\[
 d\nu_\eta(z,w)=2\|\eta\|_2^2\,1_{\{a(z)\ne a(w)\}}\,d\mu(z)d\mu(w).
\]
If \(\eta\ne0\), then \(J<\infty\) and \(\|\eta\|_2^2 J/2\le\|\xi\|_2^2-\|\xi_\mu\|_2^2\).
Both oriented original single-input right slices have cost at most
\[
       C\big(\|\xi_\mu\|_2+(1+\|\eta\|_2)\sqrt J\big)                    \tag{1}
\]
with an absolute \(C\).
If \(\eta=0\), \(A\) and \(W^*(s)\) are scalar free, and both costs are at most \(C\|\xi_\mu\|_2\) without a condition on \(J\).
In either case the closure and Hilbert adjoint of the original right slice have all bounded vectors in their domains and the negative closure gives the relative generator-first commutators.

In particular every actual model \(s=uau^*\) with \(u\) any unitary freely independent of \(A\) has these bounded-vector domains, without requiring a scalar conjugate variable for \(u\).
This extends the strong-domain conclusion of the [Poisson conjugation result](Yin_C_F0327_v1.md#statement).
Estimate (1) does not give an absolute normalized cost bound as nonzero \(\|\eta\|_2\) tends to zero.

## Argument

### Locating the liberation vector in the two-symmetry algebra

Write \(\operatorname{ad}x=x\otimes1-1\otimes x\).
The [actual liberation adjoint identity](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) gives \(\eta=[Z^*,\xi]\).
The identity applies with the selfadjoint coefficient \(s\) killed, since the derivation has the normal phase at \(Z^*\) and the two marginal trace corrections cancel, as in the [relative sign calculation](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries).
The actual liberation is closable by its vacuum and the adjoint formula on core tensors.
Bounded strong-star approximation of bounded marginal functions gives their liberation graph values \(\operatorname{ad}f\), and the outer product rule extends to words with such factors. [Borel marginal graph](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block)
In particular we may use the algebraic words in all of \(A\) and in \(N_0=\operatorname{alg}^*(a,s)\), without putting the Borel sign in the graph of \(\delta\).

The derivation \(\Lambda=\operatorname{ad}-\gamma\) on these words vanishes on \(A\) and has its values on \(N_0\) in \(N_0\otimes_{\rm alg} N_0\).
Its vacuum is \(-\eta\).
The \(B\)-expectation of every \(N_0\) word is in \(B\subset N_0\), so reduction into \(B\)-centered alternating words stays inside this domain.
A reduced word with a centered \(A\)-letter is orthogonal to \(L^2(N)\): testing against an \(N\)-letter, split its product with any adjacent end \(N\)-letter into mean and centered part over \(B\), and use amalgamated freeness.
The same statement applies to a reduced prefix ending in a centered \(A\)-letter or suffix beginning with one.
For a cut by \(\Lambda\) at any \(N_0\)-letter of a reduced word containing a centered \(A\)-letter, one of these prefixes or suffixes is nonempty.
Its \(N\)-expectation is zero and each differentiated tensor leg from the cut is in \(N_0\), so the double trace of the cut vanishes.
A single centered \(A\)-letter has derivative zero.
These reduced words together with \(N_0\) span the dense algebra, proving \(\eta\in L^2(N)\).

For either \(e=e_\pm\), inner insertion of \(e\otimes e\) kills \(\gamma a=\operatorname{ad}a\) and \(\gamma s=0\), hence all \(\gamma x\) for \(x\in N_0\).
In the double trace of \(\gamma(exe)\) the terms from the derivatives of the two \(e\)'s cancel, using \(\gamma e=\operatorname{ad}e\) and traciality.
The middle term is the double trace of \(I_{e\otimes e}\gamma x\), so \(e\eta e=0\) by density in the corner \(eNe\).
Moreover \(\eta^*=-\eta\), since \(i\gamma\) is a real derivation and its vacuum \(-i\eta\) is selfadjoint.
The two off-diagonal blocks therefore have equal squared norms.

For \(v=e_+\eta e_-\) and positive \(f,g\in A\), amalgamated freeness gives
\[
 \tau(v^*fv g)=\tau(v^*(\mathbb E_B f)v\,\mathbb E_B g)
              =\|v\|_2^2\,\tau_+(f e_+)\tau_-(g e_-),
\]
where \(\tau_\pm\) are the normalized corner traces.
Indeed approximate \(v\) by bounded off-diagonal \(N\)-elements, which are centered over \(B\), and center \(f,g\) over \(B\) before expanding.
All terms with a centered \(A\)-letter vanish by freeness and bimodularity.
The bounded approximations pass to the Hilbert pairing.
The reverse block interchanges the signs, giving the asserted product density since both sign masses equal \(1/2\).
On the joint left-right spectral calculus \(\eta=(L_{Z^*}-R_{Z^*})\xi\).
The inverse-gap energy of \(\eta\) is the squared norm of the off-diagonal part of \(\xi\) for this calculus, orthogonal to \(L^2(A)\).
Integrating the computed density proves the bound on \(J\) when \(\eta\ne0\).

### The two equal-sign parts of the cutoff

Put \(d=z-w,\ k_r=\bar d/(|d|^2+r^2)\), and \(C_0=\mathrm{id}\otimes\tau\).
For either sign block \(e\) set \(T_{e,r}=C_0 I_{k_r(e\otimes e)}\gamma\).
The inserted derivation kills \(N_0\), as proved above, and on \(A\) its coarse values are marginal.
Its slice maps \(A\) to \(eA\) and is left \(B\)-linear.
The explicit marginal difference formula gives
\[
        T_{e,r}f=t e D_{e,r}(f|_e),\qquad t=1/2,
\]
where \(D_{e,r}\) is the scalar right cutoff for the probability \(\mu_e=t^{-1}\mu|_e\).
The scalar geometric criterion and its cubic scaling give
\(t^3\|\xi_{\mu_e}\|_2^2\le C_0'\|\xi_\mu\|_2^2\), since \(t^3G(\mu_e)=G(\mu|_e)\le G(\mu)\). [Scalar geometric criterion](Yin_C_F0255_v1.md#statement)
On every finite column of bounded Borel \(A\)-inputs the scalar cutoff in normalized trace has cost at most \(3(2+\sqrt2)\|\xi_{\mu_e}\|_2\) by the [scalar cutoff and weight estimate](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word).
Thus in ambient trace the column cost of \(T_{e,r}|_A\) is at most \(C_1\|\xi_\mu\|_2\), uniformly in \(r\), including the factor \(t^{3/2}\) from the slice and output trace.

We check that this estimate still holds on the original mixed algebra.
Reduce a polynomial into a finite sum \(\sum_l w_l f_l\), where \(f_l\in A\) and \(w_l\) is empty or a reduced prefix of centered \(A,N_0\) letters ending in \(N_0\).
All means are taken over \(B\).
If the inserted derivation cuts an \(A\)-letter within \(w_l\), its remaining suffix starts and ends with a centered \(N_0\)-letter.
Its \(A\)-expectation vanishes by freeness.
The second tensor leg from the differentiated marginal belongs to \(L^2(A)\), so the right trace of the cut vanishes, first for bounded marginal simple tensors and then by Hilbert approximation.
Only the terminal factor contributes, giving \(T_{e,r}(w_l f_l)=w_l T_{e,r}f_l\).
The Gram matrix \(b_{lk}=\mathbb E_A(w_l^*w_k)\) takes its entries in \(B\).
Indeed reduce from the joining point of the two prefixes, splitting products into their \(B\)-mean and centered part.
Unless the prefixes cancel completely to a \(B\)-element, a reduced word containing a centered \(N_0\)-letter remains, with zero \(A\)-expectation.
An empty prefix causes no change to this argument.
The matrix is positive by positivity of the matrix conditional expectation.
For \(x=\sum w_l f_l\) write \(g=b^{1/2}(f_l)_l\); then \(\sum_l g_l^*g_l=\mathbb E_A(x^*x)\).
Left \(B\)-linearity gives \(\|T_{e,r}x\|_2^2=\sum_l\|T_{e,r}g_l\|_2^2\).
Applying the marginal column estimate proves the uniform one-input bound on mixed polynomials.
The same reasoning may be applied to a finite column with common prefixes, summing the input squares before taking the norm.

### The opposite-sign term and the zero-vacuum boundary

On opposite signs,
\[
  C_0 I_{k_r1_{\rm off}}\gamma(x)
        =\tfrac12 \big(C_0 I_{k_r(a(z)-a(w))}\gamma(x)\big)a .
\]
This follows because right multiplication of the sliced vector by \(a\) inserts the symbol on the first inner leg.
The kernel in parentheses is symmetric, as both factors change sign on exchanging the variables.
Its real and imaginary parts are real symmetric kernels and its Hilbert norm is at most \(\sqrt J\).
The spectral domination already proved permits \(m=\sqrt2\|\eta\|_2\) in the [symmetric Hilbert-kernel estimate](Yin_C_F0326_v1.md#statement).
Applying that estimate to the real and imaginary parts on core contractions gives \(C_2(1+\|\eta\|_2)\sqrt J\) for this opposite-sign cost.
The sum of the three cutoffs converges on every fixed polynomial to \(C_0\delta x\), since the inner multiplier \(|d|^2/(|d|^2+r^2)\) tends strongly to one on the coarse correspondence with diffuse marginal.
This proves (1).

If \(\eta=0\), put \(v=as,\ m_n=\tau(v^n)\).
Odd words in \(a,s\) have zero trace since a reduced reflection word is conjugate to \(a\) or \(s\).
For \(n\ge1\) the formula \(\gamma v=a\otimes s-1\otimes v\) therefore gives
\(0=(\tau\otimes\tau)\gamma(v^n)=-\sum_{k=0}^{n-1}m_km_{n-k}\).
Starting with \(m_0=1\), induction and adjunction imply that \(v\) is Haar.
All nonconstant alternating centered words of the signs are powers of \(v\), their adjoints, or odd reflection words, so \(a,s\) are scalar free.
It follows that \(s\) is free from \(A\).
For detail, the scalar free product of \(A\) with an independent centered symmetry has the same law on \(a,s\) and hence the same \(B\)-valued moments there by testing against \(1,a\).
Its \(A\) and two-symmetry algebra are free over \(B\) by the [reduced-word amalgamation argument](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners).
Alternating expansion into \(B\)-means and centered parts determines all its mixed traces from these moments and the law on \(A\), giving precisely the input law.
The scalar slice acts on terminal \(A\)-coefficients in free reduced words by the same prefix calculation with scalar means.
Its scalar column bound gives the claimed free case even if \(J\) is infinite.

For \(Z^*\) the reversed derivation has vacuum \(\xi^*\), the same partial liberation on the distinguished marginal and \(s\), and the same gap moduli and \(J\). [Normal phase and reversal](Yin_C_F0076_v1.md#statement)
This orientation bounds the left slice of the original derivative by the flip-adjoint identity.
The [two-slice domain theorem](Yin_C_F0072_v1.md#statement) now gives the original closure and adjoint domains.
The original core commutators from the product rule extend there by graph approximation and boundedness of left multiplication, taking the negative closure for generator-first order.
Finally for \(s=uau^*\) with the whole \(W^*(u)\) free from \(A\), one has \(N\subset B\vee W^*(u)\), so the same reduced-word amalgamation argument proves the hypothesis.
The argument uses neither a Poisson law nor an invertible parametrization of the conjugation.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:55 |
| status | open |
| reason | Fix the two-point amalgamated model, its exact liberation density and bounded original slices for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact sign-block liberation density, bounded original slices and actual domains under two-point amalgamation, including arbitrary free unitary conjugation. |
| argument | [Argument](#argument) | Borel liberation graph, centering over the two signs, terminal same-sign cutoff estimates, symmetric opposite-sign kernel and zero-vacuum identification. |
| dependency | [Liberation adjoint](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Commutator vacuum, inverse-gap spectral action and diffuse coarse diagonal. |
| dependency | [Relative sign calculus](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries) | Use of the actual distinguished derivative and liberation on a relative core with a killed projection. |
| dependency | [Borel marginal graph](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Adjoining bounded marginal functions in the liberation graph and taking products. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Actual scalar restriction with quantitative energy for a sign block. |
| dependency | [Marginal cutoff](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Uniform column estimate on bounded Borel inputs for each scalar marginal cutoff. |
| dependency | [Symmetric kernels](Yin_C_F0326_v1.md#statement) | One-input bound for arbitrary real symmetric Hilbert kernels under product-measure domination. |
| dependency | [Amalgamation](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) | Freeness over a base subalgebra in a scalar free product and determination of the mixed moments. |
| dependency | [Reversal](Yin_C_F0076_v1.md#statement) | Reflected scalar phase and flip-adjoint identification on the represented core. |
| dependency | [Two-slice domains](Yin_C_F0072_v1.md#statement) | Full closure and adjoint domains and the generator-first relative dual. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:06 |
| status | proved |
| reason | R_F0341 checked the amalgamated-word argument, the two sign corners, the cross-kernel bounds, the zero-gradient case and the original domains against all nine direct dependencies. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact sign-block liberation density, bounded original slices and actual domains under two-point amalgamation, including arbitrary free unitary conjugation. |
| argument | [Argument](#argument) | Borel liberation graph, centering over the two signs, terminal same-sign cutoff estimates, symmetric opposite-sign kernel and zero-vacuum identification. |
| dependency | [Liberation adjoint](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Commutator vacuum, inverse-gap spectral action and diffuse coarse diagonal. |
| dependency | [Relative sign calculus](Yin_C_F0327_v1.md#a-derivative-with-prescribed-values-on-the-two-symmetries) | Use of the actual distinguished derivative and liberation on a relative core with a killed projection. |
| dependency | [Borel marginal graph](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Adjoining bounded marginal functions in the liberation graph and taking products. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Actual scalar restriction with quantitative energy for a sign block. |
| dependency | [Marginal cutoff](Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Uniform column estimate on bounded Borel inputs for each scalar marginal cutoff. |
| dependency | [Symmetric kernels](Yin_C_F0326_v1.md#statement) | One-input bound for arbitrary real symmetric Hilbert kernels under product-measure domination. |
| dependency | [Amalgamation](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) | Freeness over a base subalgebra in a scalar free product and determination of the mixed moments. |
| dependency | [Reversal](Yin_C_F0076_v1.md#statement) | Reflected scalar phase and flip-adjoint identification on the represented core. |
| dependency | [Two-slice domains](Yin_C_F0072_v1.md#statement) | Full closure and adjoint domains and the generator-first relative dual. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0341_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |
