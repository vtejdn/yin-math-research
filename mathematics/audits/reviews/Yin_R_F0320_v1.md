---
author: Yin
---

# Independent review of exchange symmetry and the mixed slice output

## Finding

On 2026-11-16T16:46 UTC a reviewer outside proof development independently examined the [candidate decision](../../claims/Yin_C_F0311_v1.md#decision-candidate) of 2026-11-16T16:44.
The fixed claim and its dependencies were the mathematical inputs, with no development discussion or prior findings on this candidate.
The proof establishes all three comparisons in (1), the finite-witness assertion for the full slice, and the projected estimate and exact decomposition in (2).

In the actual doubled model the matrix \(J\) changes the sign of every potentially nonzero entry of the coefficient matrix while preserving its square.
Consequently \(D=\operatorname{diag}(J,-J)\) reverses both diagonal entries and both square-root entries of \(2P_0-1\) and fixes the diagonal generator \(W\).
The free-product action taking \(S\) to \(-S\) sends \(P_0+\varepsilon S\) to its complement about one half.
The spectral gap at one half makes the corresponding projection go to \(1-P\).
Thus the same witness and factor two from the projection reduction belong to the smaller sign-symmetric class, also when the coefficient list is empty.
The opposite bound follows by inclusion.

With \(s=2P-1\), the two sign components of each represented polynomial are \(a\) and \(bs\), with \(a,b\) polynomials in \(Z,sZs\) and their adjoints.
Moving \(s\) through a letter conjugates it, and the sign projections recover the represented coefficients uniquely, with \(\|a\|,\|b\|\le\|a+bs\|\).
The weak closure of the even polynomials is the fixed algebra by normality of sign averaging.
The two Fourier components have the crossed-product multiplication and trace, so this identification also preserves Hilbert norms.

The distinguished relative derivative is sign-equivariant on the starred generators, including \(Z^*\) by projection to the scalar marginal, diffuseness and uniqueness of its coarse phase.
Its vacuum is even by uniqueness in the Hilbert pairing.
On an even polynomial the same-sign tensor sectors are the only ones present.
The projections onto them are bimodule maps over the even algebra, and the inner insertion \(u\otimes v\mapsto us\otimes sv\) takes the odd-odd sector isometrically to the even coarse space.
Only the even-even sector has nonzero double trace.
The distinguished generator tensors and their starred phases are exchanged under \(\operatorname{Ad}_s\), so the two derived vacua are \(\xi\) and \(\operatorname{Ad}_s\xi\).
Tracing \((\delta b)\cdot s\) uses \(\tau(vs)=\tau(sv)\) and gives exactly \((E_1b)s\).
Its orthogonality to \(E_0a\) bounds the sign-model cost by \(\sqrt2\) times the exchange-model cost.
The larger component, transported by the exchange if necessary, gives an actual polynomial contraction with at least \(1/\sqrt2\) of the original output norm.
Together with the first comparison this yields the factor \(1/(2\sqrt2)\) for finite witnesses, up to the additive error already permitted by the projection reduction.

Conversely, in the tracial crossed product of a given exchange pair, the extended derivative on an even word adds the even tensor \(D_0 a\) to the inner insertion of \(D_1 a\).
Exchange covariance makes this expression respect \(sa=(\alpha a)s\) with zero derivative at \(s\).
The distinct Fourier coefficients ensure that it descends to the represented polynomial algebra.
The odd part of any input has derivative with at least one odd leg in every term, giving the original even vacuum and reproducing the first slice on even polynomials.
This realizes the reverse bound for all exchange pairs.

Finally, \(\mathbb E_B s=0\) follows by sign invariance, so multiplication from \(L^2(N)\otimes L^2(B)\) to \(K\) is isometric with both Gram constants one.
The ordered-output proof uses only the distinguished vacuum identity on \(a^*n^*x\) and the marginal adjoint bound on the two components of the projection of \(x\).
Here every \(n\in N\) already belongs to the relative polynomial core.
Right \(B\)-invariance of \(K\) justifies truncating the scalar weight in this argument.
The resulting bound is \(\|x\xi^*\|_2+\sqrt2\|x\sqrt w\|_2\), and the weight mass is \(\|\mathbb E_B\xi\|_2^2\le\|\xi\|_2^2\).
The full slice of each \(nf(Z)n'\) lies in \(K\) because both differentiated legs before multiplication are marginal.
For even \(x\), the \(sL^2(B)\) component vanishes, so the estimate controls precisely the marginal projection of \(E_0x\).
Orthogonal decomposition gives the squared upper bound in (1); first-coordinate and second-coordinate polynomials have zero residual by their generator derivatives.
Exchange gives equal marginal laws, and the comparison with the previously established universal relative criterion proves the asserted finiteness equivalence.
The finiteness of the mixed supremum itself remains undecided.
The review checked the four cited project results at these interfaces.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0311_v1.md#decision-candidate) | Whole proposed decision and all declared dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0311_v1.md#statement) | All four suprema, witness transfer, actual exchange pair, exact slice decomposition, two-block span, marginal residual and universal equivalence. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0311_v1.md#argument) | Sign symmetry of the transferred model, both crossed-product constructions, vacuum identities, orthogonality and weighted estimates. |
| [Finding](#finding) | [Projection reduction](../../claims/Yin_C_F0308_v1.md#argument) | Doubled matrix and spectral gap, factor-two witness on the same output models, and finiteness equivalence for the relative supremum. |
| [Finding](#finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Diffuse marginal restriction and uniqueness of the starred generator values for equivariance and exchange. |
| [Finding](#finding) | [Ordered outputs](../../claims/Yin_C_F0271_v1.md#the-finite-column-on-ordered-two-block-outputs) | Vacuum pairing, Gram constants one, and weighted estimates under the current distinguished relative hypothesis. |
| [Finding](#finding) | [Scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Complex scalar adjoint estimate with constant \(\sqrt2\) and exact marginal vacuum mass. |
