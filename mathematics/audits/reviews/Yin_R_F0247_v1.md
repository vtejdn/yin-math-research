---
author: Yin
---

# Independent review of normal conjugate-variable recovery and its column estimates

## Finding

The complete statement and argument of [C_F0238 v1, decision candidate](../../claims/Yin_C_F0238_v1.md#decision-candidate) are supported under the stated diffuse marginal hypotheses.
An agent outside the development of this proof completed the independent review for Yin at 2026-11-14T10:23.
The reviewer inspected the fixed candidate, the definitions and the five declared mathematical inputs, without exploration notes, proof-generation dialogue, author explanations or previous findings on this candidate.

**Descent and necessity.**
For a simple vector in the coarse Hilbert tensor product, the joint measure of the right marginal action on the first leg and the left marginal action on the second is a product of two measures absolutely continuous with respect to \(\mu\).
Consequently the spectral projection of the diagonal kills every simple vector, so it vanishes and multiplication by \(u=z-w\) is injective.
The formal \(D\) has bounded phase \(\bar u/u\) on \(Z^*\).
Inner multiplication by \(u\) commutes with the outer actions and gives \(\gamma\) on every generator, hence on every word.
It follows that a relation killed by the represented liberation derivation is killed by \(D\).
In the forward direction, differentiating each normal relation uses the corresponding *outer* difference multiplier, also injective by diffuseness, and determines the distinguished phase and all the zero starred values even for a single actual coordinate.
On the marginal core these values give \((p(z)-p(w))/(z-w)\), and restriction of the vacuum pairing gives \(\xi_N\) by orthogonal projection.
The adjoint corrections at \(Z^*\otimes1\) and \(1\otimes Z^*\) are both \(-1\), yielding \(\eta=Z^*\xi-\xi Z^*=S_{\bar u}\xi\).
The spectral theorem gives \(\nu_\eta=|u|^2\nu_\xi\) and bounds the inverse-gap integral by \(\|\xi\|_2^2\).

**Recovery on the full represented core.**
The real derivation \(i\gamma\) has adjoint vacuum \(-i\eta\), so the adjoint formula in C_F0077 gives row minus column for \(\gamma^*\).
Its absolute-continuity conclusion applies to \(\nu_\eta\), since multiplication of the vector by \(-i\) preserves its spectral measure.
The adjoint of \(I_{k_r}\) sends \(1\otimes1\) to \(\bar k_r\), a continuous marginal kernel in the closed adjoint graph.
Swapping its arguments changes its sign, hence the correction is \(2B_r\).
The coarse multiplier in (3) tends strongly to the identity because its only exceptional points lie on the null coarse diagonal.
On the joint spectral space of \(\eta\), the multiplier \(\bar k_r\) tends off the diagonal to \(1/\bar u\), with squared modulus bounded by \(|u|^{-2}\).
The inverse-gap hypothesis therefore gives norm convergence of the spectral term, whose limit is orthogonal to the whole diagonal.
For marginal tests the spectral term vanishes in the pairing.
The right side then tends to the marginal vacuum pairing, and the scalar soft-transform estimate at \(t=r^2\) bounds \(\|2B_r\|_2\) by \(2\|\xi_N\|_2\).
Polynomial density gives weak convergence to \(\xi_N\) on \(L^2(N)\), hence against every vector of \(H\) by projection.
Testing (3) on the full core now gives the Hilbert adjoint at \(1\otimes1\).
Its two orthogonal summands give (1) and identify the entire diagonal component of this particular vacuum.
This argument also covers \(\eta=0\) and requires no identification of the entire diagonal subspace with \(L^2(N)\).

**Columns and quantifiers.**
On a product \(pw\), traciality turns the right tensor leg of \(\theta(p)w\) into left insertion of \(w\) before slicing.
Right multiplication of the result by \(v\) yields the stated difference \(L(pw)v-pL(w)v\).
Finite column cost first extends \(L\) by operator-norm continuity to \(C^*(X)\), then extends the finite-column inequality to a norm limit in \(w\).
For unitary \(v,w\), right multiplication by \(w\) preserves the column norm, and \(\sum_j\|p_j L(w)v\|_2^2\le\|\sum_jp_j^*p_j\|\,\|L(w)v\|_2^2\).
The triangle inequality therefore gives the factor \(2c(L)\) for each separated character.
The Gaussian density has derivative \(L^1\)-norm proportional to \(s^{-1/2}\).
Integrating against \(e^{-sr^2}\) yields a Fourier measure with variation \(O(r^{-1})\) for \(k_r\), while the normalized positive Gaussian mixture for the complementary multiplier has mass one.
Integration of each fixed finite-column vector against these measures preserves the bounds.

The centered reduced-word vacuum test of C_F0208 extends the single old derivation by zero across the two Haar factors, and the extended algebraic liberation has the same commutator vacuum.
The abstract liberation bound in C_F0063 Appendix A thus gives a finite operator-norm-to-\(L^2\) bound \(K\) on the enlarged slice.
The Haar encoding has input norm at most twice the original column norm, and orthogonality gives its output norm as the Hilbert sum of the original sliced outputs.
It follows that \(c(C\gamma)\le 2K\) before taking any limit in \(r\).
For finite \(c(E)\), the complementary multiplier costs at most \(2c(E)\), which gives \(3c(E)\) after adding \(E\).
For each finite column, strong coarse convergence gives convergence of the whole output column.
Taking its norm before the supremum gives the claimed lower limit even for \(c(E)=\infty\).
Thus divergence to infinity characterizes infinite original cost, and cutoff boundedness for each coordinate of each full ACSY tuple has exactly the universal implication in C_F0208.
The bound may depend on the tuple and coordinate.

**Source scope.**
The declared C inputs supply the normal phase and full-system diffuseness, liberation slice estimate, marginal adjoint graph, scalar soft-transform estimate, and two-Haar criterion in the scopes recorded below.
The review checked those interfaces against their stated hypotheses and the relevant arguments, taking their established results as inputs.
The selfadjoint commutator comparison agrees with Voiculescu's trace-pairing convention after converting to the adjoint vacuum. [Voi99, Sections 5.10–5.12](../literature/Voi99/Yin_U003.md#liberation-derivation-and-gradient)
The normal inverse and cutoff bounds follow from the candidate's reasoning.
This review leaves the universal finiteness of the original costs open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0238_v1.md#statement) | The three necessary and sufficient conditions, vacuum norm and diagonal projection, and all cutoff and universal-equivalence assertions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0238_v1.md#argument) | Full represented-core descent, necessity, adjoint recovery, both limit arguments and all column estimates. |
| [Finding](#finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#statement) | Forced starred values under diffuse marginals, scalar restriction, and diffuseness when the full ACSY system is given. |
| [Finding](#finding) | [Liberation bounds](../../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Two adjoint corrections at the distinguished generator and the abstract slice estimate applied on the free product. |
| [Finding](#finding) | [Marginal adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Adjoint sign conversion, absolute continuity and continuous marginal kernels in the adjoint domain. |
| [Finding](#finding) | [Soft Cauchy estimate](../../claims/Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Uniform marginal Hilbert norm at parameter \(t=r^2\), also for the conjugate kernel. |
| [Finding](#finding) | [Two-Haar criterion](../../claims/Yin_C_F0208_v1.md#statement) | Preservation of an old coordinate vacuum, input and output bounds for the encoding and the per-tuple universal column criterion. |
