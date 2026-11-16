---
author: Yin
---

# Independent review of finite alternating depth and transported free slices

## Finding

On 2026-11-16T18:13 UTC a reviewer outside proof development checked the [candidate decision](../../claims/Yin_C_F0330_v1.md#decision-candidate) dated 2026-11-16T18:10.
The reviewer received the fixed claim and its scope without development dialogue or previous findings on this candidate.
The example has the asserted exact free moments through alternating length \(2N-1\), the discrepancy at length \(2N\), and both norm and slice properties with each \(N,r\) fixed.

The law \(1+2r\cos(N\theta)\) is a positive probability density with nonconstant moments only at orders \(\pm N\), both equal to \(r\).
Its bounded density and unit-circle support yield finite maximal linear density and total squared curvature, hence an actual scalar vacuum.
For \(Y=X^*V\), Haar absorption and exchange give identical Haar marginals.
The phase \(h(X)=X\) has energy one and gives full joint actuality.

At a junction between consecutive \(Y\) blocks separated by \(X^\ell\), opposite signs leave intervening \(X\)-power \(\ell\), while equal signs give \(\ell-1\) or \(\ell+1\).
Thus a vanished intervening exponent joins only like-signed \(V\)-letters.
Within each \(Y\) block its own distinct letters are separated by a nonzero \(X\)-power, so any uninterrupted \(V\)-run uses at most one letter from each \(Y\) block.
For fewer than \(N\) such blocks every resulting \(V\)-power has nonzero exponent of modulus below \(N\).
It is centered, giving vanishing by free reduction.
Exchange handles the words having fewer than \(N\) blocks from the other marginal.
For a nonempty alternating word of length below \(2N\) these cases cover every possible choice of the endpoint factors.
Centered Fejér approximants preserve the supremum bound and converge in the Haar \(L^2\) norm in each variable.
Telescoping under the trace therefore extends the identity to all the stated bounded Borel marginal letters.
Expanding by centering and merging adjacent letters gives the unrestricted trace matching at those lengths.
Inner products of words of at most \(N-1\) blocks have at most \(2N-2\) blocks, giving the claimed Gram matching.
At length \(2N\), \((XY)^N=V^N\) has trace \(r\), while its free-pair trace is zero.

The angular vacuum satisfies \(H^*=r(V^{-N}-V^N)\), so \(\|H\|_\infty\le2r\) and \(\|H\|_2^2=2r^2\) because the \(2N\)-th moment vanishes.
The identities \(\eta_0=X^*HX-H\) and \(d\nu_{\eta_0}=\|H\|_2^2|z-w|^2dm^2\) give \(4r\) and \(8r^2\) as the respective bounds.
The joint vacuum norm is \(\sqrt{1+2r^2}\), so the normalized phase estimate also bounds the true column costs uniformly.
These conclusions transfer to the second coordinate by exchange.
The monotone angular map has derivative equal to the density and displaces each angle by at most \(2r/N\).
Its pushforward is Haar, and freeness from \(X\) followed by absorption gives the claimed operator-norm coupling.

The substitution \(v=ab\) has inverse \(b=a^{-1}v\) in the group algebra.
The factors in both representations have infinite supports and their algebraic free product is faithful, so evaluation is well-defined on the same Laurent polynomial expressions.
The conjugates of the \(v\)-algebra by distinct powers of the free Haar \(a\) are free in each representation.
Each \(\operatorname{Re}w_j\) has second moment \(1/2\), and its mean is \(r\) in the actual pair and zero in the free pair.
Cycling the last square of a product of contractions and using freeness from the preceding factors multiplies the individual second moments.
This gives the two exponential squared-norm ratios in the proof, excluding a finite Hilbert comparison in either direction.

Applied to the centered copies of \(v^N\), the free-conjugate sum bound makes \(P_n-r\) tend to zero in actual operator norm, while \(P_n\) tends to zero in the free norm.
In the free slice calculation every positive cut in \(aw_j=a^{j+1}(ab)^N a^{-j}\) retains a \(b\) in the suffix.
At position \(i\) of the final \(a^{-j}\), the inverse derivative gives suffix \(a^{-(j-i+1)}\) and contributes a minus sign.
The selected Fourier index \(-(j-i+1)\) makes the word output \(a^{j+1}(ab)^N a^{-(j+1)}=w_{j+1}\).
This verifies polynomial re-evaluation at each fixed cutoff.
The negative Fourier partial sums tend to \(-d_0/2\) by absolute summability, symmetry and the vanishing sum, with \(d_0>0\).
Since the actual trace of every \(w_{j+1}\) is \(r\), the transported output trace at \(x_n=a(P_n-r)\) tends to \(-r d_0/2\).
For the unregularized free slice the output is exactly \(-r1\).
The true slice and its fixed-radius cutoff both send these actual inputs to zero in trace Hilbert norm by the column estimate and its cutoff factor three.
The transported operator and its difference from the true operator are therefore unbounded in the claimed input and output norms for each fixed pair.

For semicircular reparametrization the inverse \(h(s)=e^{2\pi i G(s)}\) is continuous with Lipschitz constant at most two, since the semicircle density is at most \(1/\pi\).
The conull marginal inverse preserves the Borel moment comparisons and the first discrepancy is witnessed by the corresponding marginal unitaries.
Uniform polynomial approximation of \(h\) and its conjugate transfers any hypothetical Hilbert comparison on ordinary semicircular polynomials back to the Haar core, contradicting the computed ratios.
The scalar semicircular vacuum is the coordinate and \(J(h)\le4\).
The phase criterion therefore bounds the squared joint-vacuum deviation by \(8r^2\).
Bounded omitted-marginal approximation transfers its represented derivative and vacuum to the reparametrized pair, and exchange supplies the other coordinate.
Liberation on the two marginal algebras and its vacuum are preserved by bounded marginal graph approximation, so pushforward on both spectral legs preserves the domination constant.
The transported free-slice assertion was established in the Haar coordinates.
The review checked the eleven direct dependency locators at the interfaces below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0330_v1.md#decision-candidate) | Whole fixed candidate and its eleven direct inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0330_v1.md#statement) | Exact moments and Gram comparisons for Borel blocks, small gradients and coupling, fixed-law norm and transported-slice obstructions, and the semicircular conclusions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0330_v1.md#argument) | Free-factor junctions, Fejér approximation, first discrepant cycle, exponential products, suffix selection and graph transfer. |
| [Finding](#finding) | [Scalar criterion](../../claims/Yin_C_F0255_v1.md#statement) | Actual scalar vacuum from the bounded density and finite curvature of the circle law. |
| [Finding](#finding) | [Haar exchange](../../claims/Yin_C_F0315_v1.md#actuality-of-the-product-law) | Second Haar law, exchanging automorphism and marginal liberation graph. |
| [Finding](#finding) | [Phase criterion](../../claims/Yin_C_F0265_v1.md#statement) | Full actuality, domain conclusions and exact distinguished vacuum norm from phase energy. |
| [Finding](#finding) | [Fourier vacuum](../../claims/Yin_C_F0316_v1.md#a-fourier-decomposition-of-the-terminal-derivative) | Strict positive and negative modes and the sign of \(H^*\) at this density. |
| [Finding](#finding) | [Liberation vacuum](../../claims/Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Operator-norm control and exact two-leg spectral measure of the gradient. |
| [Finding](#finding) | [Haar absorption](../../claims/Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | Construction in the same algebra of a free Haar comparison pair. |
| [Finding](#finding) | [Uniform phase estimate](../../claims/Yin_C_F0320_v1.md#statement) | Uniform bounds for true column costs, including adjoint orientations, and reparametrized-core use. |
| [Finding](#finding) | [Conjugate averages](../../claims/Yin_C_F0245_v1.md#the-correlated-and-free-word-norms) | Faithful Laurent word cores, freeness across different conjugate slots and centered sum norm bound. |
| [Finding](#finding) | [Free fixed cutoff](../../claims/Yin_C_F0245_v1.md#free-right-slices-at-a-fixed-cutoff) | Fourier suffix selection at every positive radius and the unregularized case. |
| [Finding](#finding) | [True cutoff](../../claims/Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | The true finite-column norm controls the actual cutoff norm uniformly. |
| [Finding](#finding) | [Core transfer](../../claims/Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Original derivative and vacuum under measurable reparametrization of the omitted marginal. |
