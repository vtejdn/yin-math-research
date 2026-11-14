---
author: Yin
---

# Review of the alternating conditional-expectation bound for mixed columns

## Finding

At 2026-11-14T14:42 UTC an agent outside proof development independently checked the complete [C_F0280 v1 candidate](../../claims/Yin_C_F0280_v1.md#decision-candidate) dated 2026-11-14T14:39 and its four direct dependency interfaces.
The reviewer received the candidate and scope without exploration notes, development dialogue, author explanations or a previous finding on this candidate.
The argument proves (1)–(3) under the stated finite single-input hypothesis, including the kernel tests and the free-pair example.

On marginal polynomials the forced starred symbol and the product rule give the divided difference in \(L^2(B)\otimes_2L^2(B)\).
Testing its vacuum pairing against marginal polynomials gives the scalar vacuum \(\mathbb E_B\xi_Z\), so the scalar weighted bound applies to this same slice.
For an elementary tensor \(s\otimes t\) in the marginal space the operator \(x\mapsto s\tau(tx)\) factors through the orthogonal projection onto \(L^2(B)\) and takes its values there.
This factorization persists under Hilbert–Schmidt norm limits.
Consequently the polynomial commutator depends on \(x\) only through \(\mathbb E_B x\), even for \(x\in M\), since its matrix elements on both sides are normal in \(x\).
Uniformly bounded marginal polynomials converging almost everywhere to a bounded \(q\) converge in both \(L^2(\mu)\) and \(L^2(W\mu)\).
The polynomial images therefore converge strongly to \(Sq\) by the scalar bound and weakly to \(Eq\) by normality.
Applying this identification at \(\mathbb E_Bx\) and then taking the same bounded approximation in \(b\) proves (1) for every bounded Borel multiplier.
Indeed \(b_lx\to bx\) ultraweakly, \(b_l E(x)\to bE(x)\) in \(L^2(M)\), and \((b_l-b)\mathbb E_Bx\to0\) in \(L^2(W\mu)\).

For a unitary \(u\in B\) both scalar terms in (1) are bounded by \(s_0\|(\mathbb E_Bx)\sqrt W\|_2\).
Conditional Schwarz gives \(|\mathbb E_Bx|^2\le\mathbb E_B(x^*x)\), and testing with bounded positive truncations of \(W\) yields \(\|(\mathbb E_Bx)\sqrt W\|_2\le\|x\sqrt W\|_2\).
For \(v\in N\) the omitted left-module identity gives zero commutator.
In the commutator of a word, the prefix multiplies an output on the left and the suffix multiplies \(x\) on the left.
Both operations preserve the respective norms, in particular \(\|(v'x)\sqrt W\|_2=\|x\sqrt W\|_2\) for any unitary suffix \(v'\).
Thus each \(B\)-factor costs at most \(2s_0\|x\sqrt W\|_2\), independently of the lengths of mixed words used as inputs.

Applying the two-state estimate at \(wx\) gives the row density \(w^*kw\) by cyclicity, while its column term still pairs \(h\) with \(x^*x\).
Concavity gives the same bound with any finite probability average of these row densities.
For each marginal algebra \(A\), projecting a bounded positive truncation onto the conjugation-invariant vectors \(L^2(A'\cap M)\) gives the minimum-norm point of the closed convex hull of its orbit.
Contraction and truncation give the corresponding closed convex hull in \(L^1(M)\) for a positive integrable input.
Conjugating \(w^*kw\) by the next unitary \(t\) gives \((wt)^*k(wt)\), so first averaging over \(B\) and then over \(N\) appends \(uv\) in that order.
Applying each finite next average to an earlier approximant adds at most its \(L^1\) error, yielding \((\mathbb E_C\mathbb E_D)^m k\) in the asserted convex hull.
Pairing the limit with the bounded \(xx^*\) proves (2).
When the new density is at most \(K1\), the two summed quadratic bounds for a column with \(\sum_jx_j^*x_j\le1\) are \(\tau(h)+K\) and \(\tau(W)\), respectively.
The Euclidean triangle inequality and \(\tau(W)=\|\xi_B\|_2^2\) give (3).

In the maximal abelian case \(C=N\) and \(D=B\).
Testing against marginal spectral projections identifies the two conditional expectations with integration against \(g(y,z)\) in \(y\) and \(z\), respectively.
Monotone truncation permits positive integrable inputs, and Tonelli gives first \(H(y,y')\) and then \(H_m(y,y')\) for the stated order of composition.
An essential bound on \(H_m\) therefore bounds the output in operator norm by that bound times the input trace.
Estimating one factor in \(H\) with the \(L^\infty\) bound on \(g\) and using the other factor's unit row integral gives \(L\).
Cauchy–Schwarz instead gives \(L^2\) from the uniform \(L^2(\mu)\) row bound.
For either diffuse abelian free factor \(A\), reduced words identify the orthogonal complement of \(L^2(A)\) with coarse \(A\)-bimodules by grouping the subwords that begin and end in the other centered factor.
Conjugation by powers of a Haar unitary in \(A\) tends weakly to zero on these summands, first on simple tensors by decay of the endpoint Fourier coefficients and then by density.
The complement has no nonzero commuting vector, which gives \(A'\cap M=A\), and freeness on two spectral projections gives \(g=1\).
The resulting one-step estimate and the general sufficient tests retain the original hypothesis \(a<\infty\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0280_v1.md#decision-candidate) | Fixed decision dated 2026-11-14T14:39 and its direct mathematical inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0280_v1.md#statement) | Full bounded marginal commutator, arbitrary mixed columns under the finite-iterate condition, and both ordered-density tests. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0280_v1.md#argument) | Weighted Borel extension, word telescoping, convex averaging and its order, Euclidean summation, kernels and the diffuse free-pair example. |
| [Finding](#finding) | [Actual starred hypotheses](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented starred derivation core, vacuum and outer actions for the designated coordinate. |
| [Finding](#finding) | [Normal extension and two densities](../../claims/Yin_C_F0276_v1.md#statement) | Normality on the whole algebra and the two positive trace-controlled densities when \(a<\infty\). |
| [Finding](#finding) | [Omitted-algebra averaging](../../claims/Yin_C_F0276_v1.md#averaging-over-the-omitted-algebra) | Left-module identity on \(M\) and approximation of commutant expectations by convex unitary conjugations in \(L^1\). |
| [Finding](#finding) | [Scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Original marginal slice, weighted bound \(2+\sqrt2\), and the trace identity for \(W\). |
| [Finding](#finding) | [Normal symbol](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness, forced marginal adjoint symbol, and the resulting divided difference on marginal polynomials. |
| [Finding](#finding) | [Free-factor conjugation](../../claims/Yin_C_F0243_v1.md#recovering-the-abelian-algebra-and-the-conjugating-unitary) | Reduced-word coarse decomposition and weak convergence on the complement for each diffuse abelian free factor. |
