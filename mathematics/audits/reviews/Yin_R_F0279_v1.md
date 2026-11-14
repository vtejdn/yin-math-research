---
author: Yin
---

# Review of normality for omitted additive shifts

## Finding

At 2026-11-14T13:41 UTC an agent outside proof development independently reviewed the [candidate of 2026-11-14T13:35](../../claims/Yin_C_F0270_v1.md#decision-candidate), its entire argument and the seven dependency interfaces listed below.
The reviewer received the fixed proof and review scope without proof-development discussion, exploration notes, author explanations or a prior verdict about this candidate.
The proof establishes both equivalences for uniformly bounded sequences, the exact normality classes and the two stated concentration estimates.

In the coarse space \(L^2(M\bar\otimes M^{\rm op})\), left multiplication by \(1\otimes b^{\rm op}\) acts as outer right multiplication by \(b\).
Expanding \(G(b)\) gives only mixed terms with an omitted factor and a commutator in \(N\), since \(Z\) is normal.
Graph invariance and the vanishing derivative on \(N\) give \(\bar\delta G(b)=A_b^*-A_b k\) with these multiplication orders.
Omitted multipliers and their adjoints act on the graph, so moving the adjoint multiplier across the pairing shows that the original multiplier intertwines the Hilbert adjoint on its domain.
For a fixed marginal polynomial tensor \(u\otimes v\), the vacuum pairing on \(u^*xv^*\) and the two outer Leibniz correction terms bound its pairing with \(\delta x\) by a constant times \(\|x\|_2\).
This verifies the tensor-domain interface for every fixed approximant \(k'\).
For \(u_n=\bar\delta G(b_n)\) and \(u_n'=A_{b_n}^*-A_{b_n}k'\), graph duality gives \(|\langle u_n',u_n\rangle|\le 2K_0(\|\xi\|_2+\|\delta^* k'\|_2)\|G(b_n)\|_2\).
Hence \(\limsup_n\|u_n\|_2^2\le8K_0^2\|k-k'\|_2\), and density of the marginal polynomial tensors gives the claimed convergence with no graph approximation of \(k\) required.
The products of \(A_{b_n}^*\) and \(A_{b_n}k\) with their respective adjoints differ by \(o(1)\) in \(L^2\), using the common operator norm bound and unitarity of \(k\).
Opposite multiplication gives their difference up to sign as \(A_{[b_n,b_n^*]}\), whose squared norm is \(2\|[b_n,b_n^*]\|_2^2\) by traciality.

If all centered slices vanished, the phase would be orthogonal in its second variable to every bounded centered test and therefore depend only on its first variable.
Symmetry would make it constant, and Fubini at one typical \(w\) would put the diffuse law on the corresponding line through \(w\).
Thus in the noncollinear case one fixed bounded centered \(h\) gives a nonzero marginal function \(a\).
With \(k_z(w)=k(z,w)\), slicing the second term of \(A_b k\) gives the function \(z\mapsto\tau(h\,k_z(Z)b)\), bounded by \(\|h\|_1\|b\|\).
This follows first on separated tensors and then by normality of the slice on \(B\bar\otimes B^{\rm op}\) with the second-leg functional \(d^{\rm op}\mapsto\tau(hdb)\).
The first term slices to \(ba\), and the slice of \(A_b^*\) is scalar.
The slice is \(L^2\)-continuous by Cauchy–Schwarz, giving the claimed approximation to \(b_n a\).
Right multiplication by \(a^{-1}p\) on the positive cut \(p=1_{[\varepsilon,\infty)}(|a|)\) approximates \(b_np\) by elements of \(Bp\).
When \(p=1\), this yields vanishing commutators with the diffuse coordinate \(Z\).
For a proper cut, the approximation first controls \((1-p)b_np\), and the trace of \(p[b_n,b_n^*]\) gives the same conclusion for \(pb_n(1-p)\).
The cited commutation result applies to the fixed nonscalar \(Z\) or \(p\) and the original full sequence in \(N\).
The converse follows by discarding the scalar center and bounding each mixed commutator term in \(L^2\) on the common operator norm ball.

On the affine line \(k=\bar\omega^2\) and \(b^*-\bar\omega^2 b=-2i\bar\omega\,\operatorname{Im}(\bar\omega b)\).
The variance identity for \(A_c\) removes the scalar center exactly.
The proposed approximant restores that center and has a normal residual, and its error is the centered imaginary component in \(L^2\).
Bounded multiplication transfers normality in the limit, and constant sequences recover the two exact classes.

For the noncollinear class, the marginal derivative takes values in the marginal coarse space and its vacuum pairing projects \(\xi\) to \(\mathbb E_B\xi\).
Summing the planar weight estimate over a column bounds its squared cost by \((2+\sqrt2)^2\|\mathbb E_B\xi\|_2^2\), since the weight has precisely that vacuum's squared norm as its mass.
In the single-coordinate tuple the omitted algebra is scalar, so its cubic envelope covers every exactly normal shift, including radius-dependent choices.
For the affine-line class \(x=\bar\omega(Z-z_0)\) is selfadjoint, the core is unchanged, and \(\omega\delta\) has value \(1\otimes1\) at \(x\) and adjoint vacuum \(\bar\omega\xi\).
The remaining derivations still have their prescribed generator values.
The selfadjoint vacuum and the mass identity for \(w\) give \(\tau(2(w+(\bar\omega\xi)^2))=4\|\xi\|_2^2\), which bounds the squared joint column cost.
The affine bijection of \(N\) preserves shifted moduli, so the cubic estimate with factor \(24\) gives \(96\|\xi\|_2^2\) for all omitted shifts in this case.
In the noncollinear case the estimate concerns exactly normal residuals, and the qualitative bounded-sequence result supplies no radius-dependent estimate for perturbed residuals.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0270_v1.md#decision-candidate) | Initial decision of 2026-11-14T13:35 and its seven dependency choices. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0270_v1.md#statement) | Both bounded-sequence equivalences, exact classes, normal-shift cubic envelope and stronger all-shift affine-line estimate. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0270_v1.md#argument) | Entire proof through adjoint testing, strong convergence of the differentiated defects, slicing, corner rigidity, affine normalization and both concentration constants. |
| [Finding](#finding) | [Normal starred phase](../../claims/Yin_C_F0076_v1.md#statement) | Diffuse law, symmetric unitary secant phase, vanished omitted starred values and restriction of the vacuum to the marginal. |
| [Finding](#finding) | [Omitted graph invariance](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Bounded omitted left and right factors on the closed graph and the resulting adjoint intertwining. |
| [Finding](#finding) | [Actual vacuum adjoint](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Vacuum pairing and outer product rule putting each fixed polynomial tensor test in the adjoint domain. |
| [Finding](#finding) | [Omitted commutation rigidity](../../claims/Yin_C_F0226_v1.md#statement) | Scalar variance collapse for a uniformly bounded sequence commuting asymptotically with the fixed nonscalar marginal test. |
| [Finding](#finding) | [Cubic concentration](../../claims/Yin_C_F0258_v1.md#statement) | Integral at most \(24c^2\) for the supremum over all omitted shifts, applied to the marginal and the relabelled tuple. |
| [Finding](#finding) | [Planar scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Right-slice coefficient \(2+\sqrt2\) and common weight mass for the marginal finite-column calculation. |
| [Finding](#finding) | [Selfadjoint-coordinate weight](../../claims/Yin_C_F0266_v1.md#statement) | Simultaneous unnormalized weight for original-core finite columns at the rotated coordinate. |
