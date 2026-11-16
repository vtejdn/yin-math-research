---
author: Yin
---

# Review of the local spectral mass reduction for signed curvature

## Finding

Review time (UTC) 2026-11-16T19:06.
A reviewer outside the development of C_F0337 checked the entire candidate dated 2026-11-16T19:01 against the ten direct inputs below, starting from the fixed materials without development dialogue, exploration notes, author explanations or previous findings on this candidate.
The change-of-measure square estimate, the unconditional bound on the selected disks and the feature criterion for both oriented slices hold under the stated assumptions.

For finite \(G(\mu)\) the reweighting factor \(f=M_1\mu+b\) is positive and finite almost everywhere, with a positive lower bound on the support by bounded diameter.
For any disk with positive mass, each point in it sees that entire mass at radius \(2r\), proving the upper linear growth of \(\sigma=\mu/f\).
On the part of \(Q^3\) where \(f(x)\) is the smallest of the three factors, the curvature integral for the reweighted measure is at most \(\int_Q b(x)^2 f(x)^{-3}d\mu(x)\le \sigma(Q)\).
Assigning ties once or overcounting them gives the required factor of three.
This is uniform over the sets \(Q\), including the testing squares.

I checked Tolsa, Theorem 19.1, on p. 102 of the retained version of arXiv:1408.6979v2, Lacey and Martikainen, (1.1)–(1.2) and Theorem 1.3 on pp. 1–2 of arXiv:1308.4571v1, and García-Cuerva and Martell, Definition 2.1 and Theorem 2.7, on printed pp. 614, 617 and 626 for the growth, kernel and mapping assumptions.
I used these published or preprint theorem statements at the cited interfaces.
The original proofs of those theorems are outside this project-proof inspection.
Tolsa's theorem on \(\sigma|_Q\) gives a global sharp square bound \(C\sigma(Q)\) because both its growth constant and its curvature per unit mass are bounded.
Averaging sharp differences at the dilated scales \(sr\) against \(s(-\psi'(s))ds\) and applying Cauchy–Schwarz preserves that uniform bound for the smooth differences.
Restriction to \(Q\times(0,\ell(Q))\) tests precisely the indicator of \(Q\) relative to \(\sigma\).
The kernel bounds \(C/r,\ C/r^2\) on its support of radius \(4r\) give the vertical theorem's size and second-variable regularity estimates, including when only the second evaluated kernel is nonzero.
For the scale Hilbert space, integrating the squared size and derivative bounds gives \(C/d\) and \(C|x-x'|/d^2\) respectively at distance \(d\), with the analogous second-variable bound.
The growth estimate makes each integral Hörmander sum geometric.
Finite \(\sigma\) and positive distance off the support justify the vector-integral representation.
After a fixed normalization of the growth constant these are exactly the vector-valued theorem's hypotheses.
Its \(L^3\) estimate followed by Hölder costs \(C_\psi\|f\|_{L^3(\sigma)}^3=C_\psi\int f^2\,d\mu\le 2C_\psi G(\mu)\).
The finite \(L^2\) and \(L^3\) norms permit the same input \(f\) for the operator and the components of \(f\sigma\).

On \(B(a,r)\), write \(\theta_j=\theta(x,2^jr)\).
The centered annular bound gives \(T(B)/r\le C_0\sum_j2^{-j}\theta_j\), and the constant contribution \(2C_0\theta_0\) is less than half of \(T(B)/r\) on the selected disks since \(r\theta_0\le\mu(3B)\).
The remaining telescoping sum is at most \(C\sum_i2^{-i}|\theta_i-\theta_{i+1}|\).
Weighted Cauchy–Schwarz, then integration over the possible centers, supplies the factor \(\pi r^2\) against \(dr/r^3\), leaving exactly the \(dr/r\) density square integral.
For two endpoints only \(r\ge |z-w|/2\) is possible, giving a disk integral bounded by \(C|z-w|^{-2}\).
The liberation commutator implies \(d\nu=|z-w|^2d\nu_\xi\), so there is no diagonal mass and its inverse-gap integral is at most \(\|\xi\|_2^2\).
The marginal vacuum is obtained by projection, hence its geometric energy is bounded at the same scale.
These implications only use the distinguished derivative on the marginal and zero values on the omitted starred letters.
Collecting the two angular components and the third vertex bounds the disk kernel by \(C T(B)\).
Its absolute signed contribution is therefore integrable on the selected disks by \(\sqrt{LN}+L\), using \(\mu(B)\le T(B)\).
This estimate applies to the collected kernel before taking absolute values.

For a rectangle with masses \(t=\mu(E)\ge s=\mu(F)>0\), a countable cover of the essential feature image of total squared diameter below \(\epsilon\) partitions \(F\) up to a null set.
On a cell of mass \(s_i\) its self-mass is at most \(s_i^2\) times the squared diameter.
The smaller-endpoint estimate thus leaves \(2s\nu(E^2)/t^2\) and the two cross masses divided by \(t\), at an additional cost at most \(2t\epsilon\).
The symmetric cross-mass domination contributes at most \(2/t\) times the feature integral over \(E\times F\).
Averaging the squared triangle inequality for two points of \(E\) through a point of \(F\) bounds the first term by another \(8/t\) times that integral.
Using any constant feature vector gives the stated \(20\int_B\|\phi-c\|^2d\mu\) bound, since \(s/t\le1\).
This argument permits zero masses and uses no parameter-dependent choice of cover in the resulting integrand.

The positive level-pair area for fixed third site and disk is at most half the square of the oscillation of that angular component.
Integration in the third site supplies \(C T(B)\), so on the complementary disks averaging \(c\) over \(3B\) cancels the normalizing mass by \(T(B)\le K\mu(3B)\).
The remaining center area is at most \(\pi r^2\) and the pair distance is at most \(4r\), producing the inverse-square kernel in \(J_\phi\).
Truncation in radius gives bounded kernels on each fixed analytic test; the gap-weighted \(L^2\) majorant for the full curvature kernel passes both generator tensors and the test pairing to the limit.
The real-component energy inequality then bounds both oriented slices, and bounded approximation on the actual core gives the canonical closure, its adjoint and the stated commutators.
In the exact-density case the feature energy is the inverse-gap integral itself.
For unrestricted normal tuples the negative signed contribution on the complementary disks remains a separate obligation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0337_v1.md#decision-candidate) | Complete candidate dated 2026-11-16T19:01 with its ten direct inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0337_v1.md#statement) | Square inequality, unconditional disk estimate, feature hypothesis, both orientations, exact density and original-domain conclusions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0337_v1.md#argument) | Reweighting, both operator estimates, annular absorption, smaller-endpoint subdivision, disk integration and graph limits. |
| [Finding](#finding) | [Sharp density testing](../literature/Tol17/Yin_U001.md#tol17-u001) | Theorem 19.1 on each uniformly linearly growing finite restriction, with the correct cubic rescaling. |
| [Finding](#finding) | [Vertical square testing](../literature/LM17/Yin_U001.md#lm17-u001) | Theorem 1.3, both pointwise kernel estimates and the local vertical indicator test uniform over squares. |
| [Finding](#finding) | [Vector kernel](../literature/GM00/Yin_U001.md#gm00-u001) | Definition 2.1, both Hilbert-valued kernel differences, off-support integration, global \(L^2\) bound and Theorem 2.7 at \(p=3\). |
| [Finding](#finding) | [Scalar vacuum and inverse gap](../../claims/Yin_C_F0255_v1.md#statement) | Geometric energy of the marginal with its projected vacuum and the joint spectral integral. |
| [Finding](#finding) | [Relative vacuum](../../claims/Yin_C_F0238_v1.md#statement) | The liberation commutator, zero diagonal mass and inverse-gap control at the distinguished coordinate. |
| [Finding](#finding) | [Curvature disks](../../claims/Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Positive representation by disks and angular threshold rectangles, normalization and finite-radius testing. |
| [Finding](#finding) | [Localized cost](../../claims/Yin_C_F0297_v1.md#a-localized-kernel-in-the-liberation-energy) | Absolute signed kernel estimate localized on both legs of the same marginal disk. |
| [Finding](#finding) | [Endpoint partition](../../claims/Yin_C_F0332_v1.md#subdivision-by-cubes) | Explicit unequal-mass rectangle coefficients and passage through a countable smaller-endpoint partition. |
| [Finding](#finding) | [Signed energy](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Matched gap-tensor convergence and the lower signed-form bound controlling both actual oriented core slices. |
| [Finding](#finding) | [Domain passage](../../claims/Yin_C_F0078_v2.md#the-original-canonical-operators) | Core adjoint identity, bounded graph approximants and the extension of generator commutators. |
