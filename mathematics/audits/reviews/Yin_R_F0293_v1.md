---
author: Yin
---

# Review of the canonical slice bounds for alternating matrix products

## Finding

At 2026-11-14T15:19 UTC an agent outside proof development reviewed the complete [C_F0284 v1 candidate](../../claims/Yin_C_F0284_v1.md#decision-candidate) dated 2026-11-14T15:13 and its nine declared dependencies at their points of use.
The reviewer received the fixed proof and the requested scope without development dialogue, exploration notes or previous findings on this candidate.
All three pairs of bounds in (1), their extension to bounded strong-star limits and the dense \(G_\delta\) obstruction follow under the stated hypotheses.

The spectral law is diffuse, and restriction of the joint vacuum identity to marginal tests gives the actual marginal vacuum \(\mathbb E_B\xi\).
The forced value on \(Z^*\), the Leibniz rule and \(\delta Z=1\otimes1\) give the divided difference of every marginal starred polynomial.
On the compact spectral support this kernel is bounded for each such polynomial, since the polynomial is Lipschitz there.
If uniformly bounded \(a_\alpha\) tend to \(a\) in \(L^2(\mu)\), truncating the integrable \(W\) at height \(s\) bounds the weighted squared error by \(s\|a_\alpha-a\|_2^2+\sup_\alpha\|a_\alpha-a\|_\infty^2\int_{\{W>s\}}W\,d\mu\).
This works for nets and makes the polynomial approximants Cauchy in the scalar graph.
Summing the squared scalar bounds gives a single integral of \(W\sum_i|h_i|^2\), hence the column bound \(b\) in every dimension.
For the conjugated tuple the vacuum is \(\xi^*\) and the new marginal vacuum is \((\mathbb E_B\xi)^*\), with the same norm.
The suppression complement has a Fourier probability representation, and each separated unitary multiplier costs at most \(2b\) on these columns.
Adding the original slice gives \(3b\) for the suppressed marginal slice at every \(r>0\).
The fixed-radius coefficient has magnitude at most \(1/(2r)\), so both its integral operator and its multiplication term are bounded on \(L^2(\mu)\).

For a cut \(LB_jR\), the divided difference of an entry \(f\) of \(B_j\) sees only \(\mathbb E_B R_k\) in the matching right entry.
The formula follows first on simple marginal tensors from \(\tau(dR_k)=\tau(d\,\mathbb E_B R_k)\) for \(d\in B\), then by continuity because \(R_k\) is bounded.
The scalar difference \(D(fh)-fD(h)\) integrates that kernel against \(h(w)\).
For polynomial \(h\) this is Leibniz, and bounded approximation extends it to measurable \(h\) by the weighted estimate and the bounded kernel of \(f\).
Inner spectral multiplication commutes with both outer actions, so the calculation at the cut also holds with the fraction \(m_r\) inside this same integral.
The conditional expectation Schwarz inequality sums to \(\sum_k|\mathbb E_B R_k|^2\le\mathbb E_B(R^*R)\).
The rectangular matrix on the left acts on Hilbert sums with its matrix operator norm.
Thus both \(D(B_jh)\) and \(B_jD(h)\) after left multiplication cost at most \(b\|L\|\|B_j\|\|R\|\) each, or \(3b\|L\|\|B_j\|\|R\|\) each at fixed radius.
There is no trace normalization on the intermediate matrix indices.
When \(m=0\), the omitted algebra's polynomial factors are killed in both orientations and at all radii.

Applying the vacuum identity to \(p_i^*a\) gives \(E_0^*p_i=p_i\xi-E_0^\#p_i\).
Applying it to the flip-adjoint derivation gives \((E_0^\#)^*p_i=p_i\xi^*-E_0p_i\).
In both cases \(\sum_i\|p_i\zeta\|_2^2=\langle\zeta,(\sum_i p_i^*p_i)\zeta\rangle\), so the original column norm controls the vacuum term.
These identities concern the actual Hilbert adjoints on the original core and also give closability.
For rectangular measurable factors, Kaplansky approximation of the selfadjoint matrix dilation followed by compression to the off-diagonal corner gives bounded strong-star approximants.
Polynomial norm approximation can be made with vanishing errors, so the limsup of the approximating norms is at most the original norm.
Finite products then converge strongly-star, and weak compactness and weak graph closure identify every right-slice cluster point on the limiting column.
Strong left multiplication on \(\xi,\xi^*\) and the two closed adjoint graphs pass the identities to the limit, retaining the limiting column norm even if cancellation lowers it.
These arguments also apply to a bounded net of measurable sums of cost at most \(K\).
For every fixed \(r>0\), bounded strong-star convergence gives ultraweak convergence, hence weak convergence under the normal cutoff in either orientation.
The common bound \(6bK\) survives taking the supremum over radii after these limits.

For a Haar generator the double trace of the Laurent derivative at exponent \(k\) is \(\mathbf1_{\{k=1\}}\).
The free-product construction therefore gives actual coordinate vacua for the pair, and the free normal theorem gives full canonical forward and adjoint domains on bounded inputs.
In the group model, expansion of a Laurent matrix product yields only words with at most \(2m+1\) syllables, regardless of matrix sizes and cancellations.
The corresponding Fourier subspace is closed under \(L^2\) limits, so measurable products have the same support.
For \(m=0\) its weight \((\ell-1)_+\) vanishes, including on the identity.
For every finite scalar sum of cost at most \(K\), the triangle inequality bounds the weighted image by \(2K\), and weak graph closure retains this bound for any \(L^2\) limit.
For \(w=uv_0\), orthogonality of its powers gives Haar law and \(\ell(w^k)=2|k|\) for \(k\ne0\).
For the upper semicircle projection the squared weighted Fourier coefficient at odd \(k\) is \((2|k|-1)^2/(\pi |k|)^2\), which fails to tend to zero.
It is therefore a trace-\(1/2\) projection outside the maximal domain of this closed diagonal operator.
The algebra \(L(\mathbb F_2)\) is diffuse and the identity has weight zero, so the deficient-domain alternative applies on every trace layer \(0<t<1\).
Its dense \(G_\delta\) complement excludes all finite uniform costs at once.
This obstruction concerns the stated approximation method and is compatible with the full canonical domains of the Haar pair.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0284_v1.md#decision-candidate) | Complete fixed candidate at 2026-11-14T15:13 and all nine declared dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0284_v1.md#statement) | Both orientations, adjoints, dimension-free column bounds, all radii, bounded strong-star limits and fixed-trace approximation obstruction. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0284_v1.md#argument) | Marginal weights, rectangular cuts, graph closures, free Haar domains, Fourier weights and the category argument. |
| [Finding](#finding) | [Scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Complex marginal forward estimate and exact integral of its dominating weight. |
| [Finding](#finding) | [Forced normal derivatives](../../claims/Yin_C_F0076_v1.md#statement) | Diffuse marginal, starred divided differences and vanishing derivatives on omitted generators and their adjoints. |
| [Finding](#finding) | [Suppression formula](../../claims/Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Separated unitary multipliers and Fourier probability for the threefold scalar column bound. |
| [Finding](#finding) | [Normal cutoffs and fixed-trace dichotomy](../../claims/Yin_C_F0282_v1.md#statement) | Normal right slices at each positive radius in both orientations and dense omission on every fixed trace layer. |
| [Finding](#finding) | [Adjoint tuple](../../claims/Yin_C_F0073_v1.md#statement) | Flip-adjoint derivation, actual vacuum and conditional expectation in the reverse orientation. |
| [Finding](#finding) | [Core adjoint identity](../../claims/Yin_C_F0271_v1.md#exact-energy-and-affine-line-rigidity) | Actual Hilbert adjoints, companion right slice and order of the vacuum multiplication on columns. |
| [Finding](#finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Theorem 2.3.1 at its inspected statement and applicability depth, using selfadjoint matrix dilation and rectangular compression. |
| [Finding](#finding) | [Free vacua](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual Haar vacuum and extension to the joint free core by the centered reduced-word test. |
| [Finding](#finding) | [Free normal domains](../../claims/Yin_C_F0162_v1.md#statement) | Both domains on all bounded inputs for the original canonical operators of the free Haar pair. |
