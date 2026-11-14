---
author: Yin
---

# Review of the two canonical domains for mixed spectral cuts

## Finding

At 2026-11-14T15:23 UTC an agent outside proof development independently reviewed the [C_F0285 v1 candidate](../../claims/Yin_C_F0285_v1.md#decision-candidate) dated 2026-11-14T15:20, its full argument and the seven direct inputs at their points of use.
The reviewer received the fixed material and the requested scope without exploration notes, proof-development dialogue, author explanations or prior findings on this candidate.
The two estimates, all four domain inclusions and the exact dimension example hold under the stated hypotheses.

For a simple tensor \(a\otimes b^{\rm op}\), outer multiplication by \(l,h\) gives \(la\otimes(bh)^{\rm op}\), the product with \(l\otimes h^{\rm op}\) on the left.
Inner multiplication by \(v,w\) gives \(av\otimes(wb)^{\rm op}\), the product with \(v\otimes w^{\rm op}\) on the right.
The flip-adjoint sends the product of \(a\otimes b^{\rm op}\) and \(c\otimes d^{\rm op}\) to \(b^*d^*\otimes(c^*a^*)^{\rm op}\), the product of their images in the same order.
The adjoint identifications of the two spatial factors extend this conjugate-linear isometry, so it preserves the operator norm of the differentiated selfadjoint polynomial in passing to the adjoint tuple.
The forced derivative of each starred generator is bounded in this opposite algebra because its only nonconstant symbol belongs to the abelian marginal tensor algebra.
The finite word Leibniz expansion therefore has bounded value \(V\).
The symmetric real suppressed symbol \(g_r\) has norm at most one and converges to one off the diagonal, which has zero product measure by diffuseness.
Consequently \(Vg_r\to V\) in trace Hilbert norm with \(\|Vg_r\|\le\|V\|\) in both orientations.

For each \(s>0\), the Neumann expansion of \(((p-t)^2+s^2)^{-1}\) uses a positive contraction of norm \(q<1\).
The summable bounds \(O(nq^{n-1})\) for differentiated powers give norm convergence of the inputs and convergence of both derivative values.
The inverse identity gives \(-(R_\pm\otimes R_\pm^{\rm op})V\), and inner suppression replaces only the rightmost factor by \(Vg_r\).
The functional \(b\mapsto\tau^{\rm op}(R_\pm^{\rm op}b)\) is normal of norm \(\|R_\pm\|_1\), by trace duality and polar decomposition.
Its slice of \(Vg_r\) has operator norm at most \(\|R_\pm\|_1\|V\|\).
Left multiplication by \(R_\pm\) then costs at most \(\|R_\pm\|_2\) from operator norm to Hilbert norm.
These estimates are simultaneous in the radius, including the unsuppressed case.

Restriction to \(|x-t|\le s\) gives the product lower bound \(F_t(s)^{3/2}/(2s^2)\).
For the upper bound, the annulus \(2^{j-1}s<|x-t|\le2^js\) costs at most \(2^{1-j}/s\) in resolvent magnitude.
Expanding the product and bounding the square root of the sum by the sum of square roots gives the two indices \(j,k\) in the candidate.
With measure \(ds/s^2\), the \(3/2\) power integral of \(F_t(2^js)\) equals \(2^jH_t\).
Hölder therefore contributes \(2^{2j/3+k/3}H_t\), leaving the summable weights \(2^{-j/3-2k/3}\).
The lower bound covers infinite \(H_t\), and any positive atom forces divergence at zero.

On a compact \(s\)-interval the resolvent approximants and Riemann sums converge in both forward graphs.
The scalar integral of \(R_++R_-\) over \([\epsilon,A]\) tends to \(\pi\operatorname{sgn}(p-t)\) away from the threshold and has magnitude at most \(\pi\).
The absence of an atom at \(t\) thus gives bounded strong-star convergence of \(b_{\epsilon,A}\) to the stated open half-line projection.
Integrability of the product estimate gives Hilbert-norm convergence of the graph outputs and bounds both endpoint tails uniformly over radii.
Normality at a fixed radius gives weak convergence of its values on the bounded inputs and identifies this same norm limit with the cutoff on the projection.
At fixed \(s\), Hilbert convergence of \(Vg_r\) passes through bounded outer multiplication and the tracial slice.
The integrable majorant gives the two strong cutoff limits by dominated convergence.

On the original core the adjoint of the associated Hilbert-Schmidt operator acting on the vacuum takes the flip-adjoint right slice, giving \(E^*x=x\xi-E^\#x\).
Polynomial norm convergence controls the vacuum term, and joint graph approximation passes this identity to each resolvent and each compact integral.
At the projection limit, bounded strong convergence controls \(b_{\epsilon,A}\xi\), and the opposite forward output already converges in \(L^2\).
Closedness of the actual adjoint proves its domain and value there.
The reversed derivation has vacuum \(\xi^*\), so the same argument gives \((E^\#)^*e_t=e_t\xi^*-\bar E e_t\).

For \(2/3<\alpha<1\), a local mass bound \(F_t(s)\le s^\alpha\) makes the near-zero integral finite.
At each dyadic radius witnessing the failure of this bound up to a constant, a fixed dilation of a dyadic interval of mass at least \(c2^{-j\alpha}\) contains the center.
The mass sum is at most two per level, including endpoint atoms, so summing the \(\beta\)-powers of the diameters over all levels \(j\ge n\) costs \(O(2^{-n(\beta-\alpha)})\) for \(\beta>\alpha\).
On the proposed Cantor set, a ball of radius \(\lambda^{j+1}<s\le\lambda^j\) contains one child and meets a bounded number of parents.
Since \(\lambda^{2/3}=1/2\), its mass is comparable to \(s^{2/3}\), yielding logarithmic divergence everywhere on the set and its lower dimension bound.
The level covers give the upper bound, and positive distance from the compact support gives finiteness outside it.

The law of \(x+iy\) has ball growth \(O(s^{5/3})\) by independence and the Cantor upper bound.
Summing \(O(2^{-2j/3})\) over near-diagonal shells bounds the inverse-distance potential uniformly.
Thus the two traces of the divided difference can be interchanged absolutely and give the stated bounded vacuum coefficient on the represented core.
For the free Haar coordinate the Laurent derivative has double trace \(\mathbf 1_{\{k=1\}}\) on \(u^k\), giving the actual scalar vacuum \(u\).
Summing the scalar weighted estimate on columns controls both orientations by applying it also to the adjoint coordinate.
The free enlargement theorem therefore gives actuality and the full original canonical forward and adjoint domains on bounded inputs of the pair.
Unitary conjugation preserves the law of \(\operatorname{Im} Z\), so the exceptional dimension of this mixed polynomial is exactly \(2/3\) even though every one of its spectral projections belongs to both domains.
The independent finding covers sharpness of the mass and resolvent criterion and leaves the general full-domain implication open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0285_v1.md#decision-candidate) | Complete 2026-11-14T15:20 candidate and all seven declared inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0285_v1.md#statement) | Uniform bounds, two strong limits, four actual domains, equivalence of integrals, Hausdorff dimension and its sharpness for the criterion. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0285_v1.md#argument) | Opposite multiplication, resolvent and projection graphs, original adjoints, dyadic estimates and the actual free-pair example. |
| [Finding](#finding) | [Forced normal derivatives](../../claims/Yin_C_F0076_v1.md#statement) | Diffuse marginal, vanishing off-coordinate starred values and bounded marginal secant phase. |
| [Finding](#finding) | [Opposite tensor and resolvent graph](../../claims/Yin_C_F0229_v1.md#argument) | Outer actions as left multiplication and polynomial inverse approximation with a summable differentiated series. |
| [Finding](#finding) | [Normal fixed-radius slices](../../claims/Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Bounded normal extension and bounded-input weak continuity for any chosen positive radius in each orientation. |
| [Finding](#finding) | [Original adjoint identity](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4 in the inspected published edition, formula (5) on the actual polynomial core, applied to the two original slices. |
| [Finding](#finding) | [Adjoint tuple](../../claims/Yin_C_F0073_v1.md#statement) | Flip-adjoint reversal and conjugation of the actual vacuum. |
| [Finding](#finding) | [Scalar columns](../../claims/Yin_C_F0267_v1.md#statement) | Complex weighted estimate and integrable weight for the scalar coordinate and its adjoint on finite columns. |
| [Finding](#finding) | [Free enlargement](../../claims/Yin_C_F0278_v1.md#statement) | Actual vacua and full original canonical and adjoint domains for the free pair from finite scalar oriented column costs. |
