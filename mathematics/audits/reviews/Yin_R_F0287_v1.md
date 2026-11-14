---
author: Yin
---

# Review of the one-coordinate free extension test for column costs

## Finding

At 2026-11-14T14:29 UTC an agent outside proof development independently reviewed the [candidate of 2026-11-14T14:26](../../claims/Yin_C_F0278_v1.md#decision-candidate), its entire argument and the nine declared dependency interfaces.
The reviewer received the fixed candidate and the requested scope without a proof-development discussion.
The stated bounds hold separately for each coordinate, and the two equivalences hold for the specified extension by any free normal marginal with an actual scalar conjugate variable.

The centered alternating tensor representation embeds the algebraic free product of the two represented cores and allows each derivation to vanish on the other factor.
In every differentiated word of length at least two, a centered letter of that other factor occurs on at least one side adjacent to the differentiated block.
This makes the double trace vanish first on simple tensor values and then on the completed coarse tensor space by continuity.
Orthogonality of the same reduced word to the original vacuum vector verifies the adjoint identity.
For the right slice, a cut preceding the final coefficient leaves a reduced suffix beginning and ending in the other factor.
Its trace against the two coefficient-factor multipliers vanishes by freeness.
For \(p=\sum_w w b_w\), conditional expectation gives \(\sum_w b_w^*b_w=\mathbb E_B(p^*p)\), and the right-module isometry gives \(\|\widehat E_i p\|_2^2=\sum_w\|E_i^B b_w\|_2^2\), including Hilbert-valued coefficients.
The resulting norm bound on the core passes to the closed slice by bounded approximation and weak graph closure, also for each generator times the input, which proves the required full-domain commutator.
Applying the scalar inequality before summation gives a bound of \((2+\sqrt2)^2\int W\,d\mu=(2+\sqrt2)^2\|\xi_Y\|_2^2\) for the squared new-coordinate cost.

For \(d\ge2\), a single old omitted marginal supplies \(v\) regardless of its dependence on the other old coordinates.
Diffuseness in both selected factors allows successive measurable bisection into sets of equal mass and hence a measurable uniform angle in each factor.
The associated Borel unitaries \(u,v\) are Haar.
In a product of centered elements of the conjugates \(u^jMu^{-j}\), a change of adjacent index produces a nonzero power of \(u\).
Cyclicity either leaves one further centered power or removes the endpoint power, and in both cases the remaining word has zero trace by freeness.
Including index zero proves joint freeness of \(v_j=u^jvu^{-j}\) from \(M\), as well as their mutual freeness.
The free Haar norm estimate therefore applies with the original correlated \(M\) as coefficient algebra and gives \(\|\sum_jv_jp_j\|\le2\|\sum_jp_j^*p_j\|^{1/2}\).

Normal attainment allows subtraction of \(aT(1)\) at cost at most \(2\beta_i(Z)\).
Starred commutator rigidity fixes this normalized witness on the old core and makes it commute on all bounded inputs with each generator and adjoint in the omitted algebra.
For fixed \(a\), each scalar test of \(b\mapsto T_0(ba)\) is normal since right multiplication by \(a\) is normal.
Each scalar test of \(b\mapsto bT_0(a)\) is a normal vector functional in the left representation.
These facts extend the commutation to the entire omitted von Neumann algebra and thus to the Borel \(v_j\).
The expectation \(\mathbb E_M(v_j^*v_k)=\delta_{jk}1\) gives orthogonality of \(v_j E_i p_j\) by \(L^2\) approximation.
This proves \(c_i(X)\le4\beta_i(Z)\) whenever the optimum is finite and excludes a finite optimum whenever the column cost is infinite.

For \(d=1\) the scalar weight first gives finite \(c_1(X)\), hence a finite optimum by the upper bound.
Restriction of the normalized witness gives \(\|E_1\|_{C^*(X)\to L^2(M)}\le2\beta_1(Z)\) by uniform extension from starred polynomials.
Since \(C^*(X)=C(\sigma(X))\), the finite-family complex little Grothendieck inequality bounds \(c_1(X)^2\) by \(4\|E_1\|^2/\pi\).
Taking square roots yields the stated lower constant \(\sqrt\pi/4\).
Conjugating the derivations by the tracial involution and the tensor flip-adjoint gives the actual vacua for the adjoint tuple and preserves the scalar vacuum norm.
Both orientations therefore have a finite new-coordinate cost.
On the normal tuple the all-index finite-optimum criterion includes algebraic full-domain witnesses and the generator-first sign is obtained by negating each witness.
Applying that criterion in both orientations and the normal strong-domain comparison identifies the bounded-vector domains of the original closed canonical slices and their actual Hilbert adjoints.
For the Haar choice of \(Y\), the Laurent-polynomial derivative has double trace one on \(Y\) and zero on all other integer powers, so \(Y\) itself supplies the required scalar vacuum.
The review establishes the detector conditional on the original column costs and leaves existence of a normal tuple with infinite cost open.
The external commutative inequality was used at the finite-family scope of its existing source inspection.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0278_v1.md#decision-candidate) | Fixed decision of 2026-11-14T14:26 and its nine declared dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0278_v1.md#statement) | Actual vacua, both old bounds with the scalar improvement, new-coordinate bound, adjoint orientation, both equivalences and Haar specialization. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0278_v1.md#argument) | Full reduced-word extension, Borel Haar detection with arbitrary old correlations, scalar lower bound and canonical domain conclusion. |
| [Finding](#finding) | [Free extension](../../claims/Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Represented free cores, double-trace cancellation on completed tensor values and actual vacuum in either factor. |
| [Finding](#finding) | [Slice and Haar estimates](../../claims/Yin_C_F0208_v1.md#argument) | Right-module column bound, closure to all bounded inputs, free Haar norm bound and normalized single-index starred commutators. |
| [Finding](#finding) | [Scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Summation of the weighted complex slice inequality and total weight equal to the squared scalar vacuum norm. |
| [Finding](#finding) | [Marginal laws](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness for each normal marginal admitting the actual coordinate system, used for successive equal-mass partitions. |
| [Finding](#finding) | [Normal attainment](../../claims/Yin_C_F0201_v2.md#statement) | Attainment of the finite optimum by an ultraweak-to-weak continuous map with unrestricted vacuum value. |
| [Finding](#finding) | [Commutative inequality](../literature/Pis12/Yin_U001.md#pis12-u001) | Squared constant \(4/\pi\) on finite families for a complex-linear map from a commutative unital \(C^*\)-algebra into a complex Hilbert space. |
| [Finding](#finding) | [Adjoint conjugation](../../claims/Yin_C_F0073_v1.md#statement) | Actual derivation and adjoint vacuum for each coordinate of the adjoint tuple. |
| [Finding](#finding) | [Bare normal criterion](../../claims/Yin_C_F0201_v1.md#statement) | Equivalence with all finite optima for the normal tuple, including arbitrary algebraic bare systems. |
| [Finding](#finding) | [Strong canonical domains](../../claims/Yin_C_F0075_v1.md#statement) | Both bare orientations give the strong condition and the full bounded-vector domains for the prescribed closed canonical operators and their Hilbert adjoints. |
