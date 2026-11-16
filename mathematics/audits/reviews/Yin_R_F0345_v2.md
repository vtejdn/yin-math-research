---
author: Yin
---

# Independent review of the uniform slice bound on parallel lines

## Finding

On 2026-11-16T19:41 UTC a reviewer outside this proof's development independently inspected the [version 2 candidate](../../claims/Yin_C_F0340_v2.md#decision-candidate) dated 2026-11-16T19:37, its complete statement and argument, and its ten declared direct mathematical inputs.
The reviewed statement specifies a faithful normal probability trace and zero derivative on the coefficients and their adjoints.
The reviewer received the fixed version and its scope without proof-development dialogue or a prior finding on this candidate.
This inspection covers the new continuous relative theorem and the exact discrete transfer, including freely spaced parallel lines; the earlier [version 1 finding](Yin_R_F0345_v1.md#finding) remains a separate review of its original argument.
Both \(Cm^2\) estimates and the distinguished domain and commutator statements follow.

At the middle height of a noncollinear triangle the absolute horizontal displacements in the area determinant are bounded by the corresponding side lengths.
Squaring the two-term bound and canceling those lengths leaves two terms of the form \(8L^2/(a^2b^2)\), where both sides \(a,b\) are at least the positive height gap \(L\).
Thus each is at most \(32L^{-2}b_L(a)b_L(b)\), with zero-height terms discarded, including triangles with tied heights.
All pairs of sides occur in the symmetric sum defining \(G_L\), and its factor 64 allows for repetition.
The bounded decomposition \(g_L=gG_L/\sum G_{L'}\) allows a separate absolute estimate of each **actual** signed pairing, without using monotonicity of that pairing.
There are finitely many lengths and \(g=0\) when all heights coincide.

At each \(L\), the cell centers deviate from points in their cells by at most \(L/2\), so \(b_L\le C\lambda_{ij}\) there.
Each line contributes at most \(\sum_{k\in\mathbb Z}(1+k^2)^{-1}\) to any weight row or column, irrespective of the distance between lines.
The triangle inequality bounds the smaller of \(\lambda_{ik},\lambda_{jk}\) by \(4\lambda_{ij}\).
This bounds each actual rectangle kernel in supremum norm by \(CL^{-2}\lambda_{ij}(S_i+S_j)\).
The exact liberation commutator gives zero diagonal mass for \(\nu\) and \(I=\|\sigma\|\le\|\xi\|_2^2\); projection onto the marginal gives the scalar vacuum.
Each cell of mass \(t_i\) has diameter at most \(L\), so integrating the squared maximal linear density on it gives at least \(t_i^3/(4L^2)\).
The scalar criterion therefore bounds \(L^{-2}\sum_i t_i^3\) with no dependence on interline separation.

For the rectangle and its transpose, the Borel set used in the localized signed estimate is their two-cell union, with no connectivity requirement.
Its mass is at most \(t_i+t_j\), and the squared norm of its vacuum compression is exactly \(\nu((E_i\cup E_j)^2)\).
The relative proof uses just the distinguished marginal actions and the zero derivatives of all other letters.
For nonnegative exponents \(p,q\) used in the proof with \(p+q=3\), Hölder against \(\lambda_{ij}\) bounds the pair sum by \(CK\|S\|_3^p\|t\|_3^q\), using the row and column sums separately; Jensen gives \(\|S\|_3\le K\|t\|_3\).
The squared-mass part therefore costs at most \(CK^2L^{-2}\sum_i t_i^3\).
In each cross rectangle the endpoint distance is at most \(L(1+d_{ij})\).
For a fixed orientation the cross masses \(\sigma_{ij}\) sum to at most \(I\); Cauchy–Schwarz and \(\lambda_{ij}^2(1+d_{ij})^2\le2\lambda_{ij}\) give \(CK^{3/2}L^{-1}\sqrt I\,\|t\|_3^{3/2}\).
The repeated diagonal masses require summation in the other index first: Cauchy–Schwarz row by row contributes \(K^{1/2}\), the pair bound at \((2,1)\) contributes \(CK^{3/2}\|t\|_3^{3/2}\) after the square root, and \(\sum_i\sigma_{ii}\le I\).
This gives \(CK^2L^{-1}\sqrt I\,\|t\|_3^{3/2}\), also covering the diagonal cell squares.
Since \(K=O(m)\), the absolute cost is \(O(m^2)\|\xi\|_2^2\) per length and \(O(m^4)\|\xi\|_2^2\) in total.
The signed energy inequality, the two analytic unitary signs and the real/imaginary decomposition give \(O(m^2)\|\xi\|_2\) for each oriented slice.
The relative two-slice argument applies on the original represented core and gives both bounded-vector domains and the generator-first commutators.

For a discrete configuration the corner segments remain on the given horizontal lines after rotation, are pairwise separated by at least three quarters of their center distance, and have conditional half-length \(h/8\).
The original spread-marginal estimates need only the minimum spacing and bound its actual distinguished vacuum by \(CB_c\).
Uniform approximation of the slot cuts and their first derivatives gives operator-norm input and coarse graph convergence on fixed words.
Projecting the two legs takes the two independent conditional segment means and commutes with the right slice after projecting its output, producing \(A_h\), not the unaveraged reciprocal.
At unit scale the bounded symmetric displacement gives \(|zA(z)-1|\le1/3\) even for complex \(z\) with \(|z|\ge1/2\).
The reciprocal power series and differentiation give the claimed integrable Sobolev squares after cutoff: the function decays as \(|z|^{-2}\) and its first two derivatives gain one inverse power each.
Weighted Cauchy–Schwarz then gives an integrable planar Fourier transform since \((1+|\theta|^2)^{-2}\) is integrable.
Dilation does not change the Fourier measure variation and \(zA_h(z)=(z/h)A_1(z/h)\).
The multiplier therefore recovers the reciprocal on every distinct slot pair; the same-slot insertion vanishes by the word rule.
The two factors of each Fourier character are unitary elements of \(D\), so the traced product rule costs at most twice the previous one-input bound before integrating the measure.
Equality of generator values and the Leibniz rule finish the exact recovery on all original words.
The constant is independent of \(h\), the maximum occupied distance, masses and algebra; no bound independent of \(m\) is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0340_v2.md#decision-candidate) | Fixed version 2 candidate with the explicit trace and starred coefficient hypotheses. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0340_v2.md#statement) | Both relative orientations, domains and commutators, and absolute \(Cm^2\) discrete bound for arbitrary spacings. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0340_v2.md#argument) | Complete geometry, cell sums, matched energy and segment transfer through the complex Fourier inverse. |
| [Finding](#finding) | [Relative commutator](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | The two starred marginal values, zero liberation diagonal mass and inverse-gap control. |
| [Finding](#finding) | [Marginal geometry](../../claims/Yin_C_F0255_v1.md#statement) | The projected marginal vacuum controls the integral of squared maximal linear density and hence the cubic cell sum. |
| [Finding](#finding) | [Localized bound](../../claims/Yin_C_F0297_v1.md#a-localized-kernel-in-the-liberation-energy) | Uniform absolute signed pairing on an arbitrary Borel union of two cells. |
| [Finding](#finding) | [Relative localization](../../claims/Yin_C_F0337_v1.md#disks-of-small-local-mass) | Applicability with one actual relative coordinate and all omitted starred letters killed. |
| [Finding](#finding) | [Analytic energy](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Curvature sign, factor one half and square-root conversion for both oriented slices. |
| [Finding](#finding) | [Relative domains](../../claims/Yin_C_F0337_v1.md#the-remaining-disks-under-feature-domination) | Original bounded-vector graph and adjoint inclusions with distinguished generator-first commutators. |
| [Finding](#finding) | [Free corner spread](../../claims/Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Conditional segment laws, their scalar means and actual relative liberation in the generated algebra. |
| [Finding](#finding) | [Spread vacuum](../../claims/Yin_C_F0339_v1.md#the-scalar-vacuum-of-the-spread-measure) | Scalar and mixed budgets with arbitrary centers at minimum separation \(h\). |
| [Finding](#finding) | [Slot cuts](../../claims/Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) | Norm and graph convergence and two conditional means, using the segment average rather than the circle identity. |
| [Finding](#finding) | [Separated multipliers](../../claims/Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | The one-input slice bound for integrating separated marginal unitaries against a finite Fourier measure. |
