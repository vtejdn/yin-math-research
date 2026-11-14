---
author: Yin
---

# Review of a common disk character and the singular mass of a nonnormal residual

## Finding

At 2026-11-14T14:08 UTC a reviewer for Yin independently checked the entire [C_F0275 v1 candidate](../../claims/Yin_C_F0275_v1.md#decision-candidate) dated 2026-11-14T14:05.
The reviewer received the fixed argument and its scope without exploration notes, development dialogue, author explanations or a prior verdict on this candidate.
The three existing dependencies were used at the interfaces below.
The joint character, optimal cutoffs, original canonical domains and quadratic singular asymptotic all follow for the stated range of \(\alpha,c\).

The separated kernel \(b(z,v)=c|zv|^\alpha\) realizes the stated field and is positive almost everywhere.
Its squared row norm is \(c^2|v|^{2\alpha}/(1+\alpha)\), and \(\|1/b\|_2^2=c^{-2}(1-\alpha)^{-2}\).
The drift coefficient vanishes.
The shared intermediate radius cancels from the two ratios in the remaining coefficient of the Gaussian criterion.
For radii \(r>s\), Parseval applied to the geometric series gives the angular mean \(1/(r^2-s^2)\).
The two orderings, radial measures \(2r\,dr,2s\,ds\), and substitution \(s=rt\) give \(4\int_0^1 t(t^\alpha-t^{-\alpha})^2/(1-t^2)\,dt\).
Its orders at the two endpoints are \(t^{1-2\alpha}\) and \(1-t\), respectively.
For the disk the angular Cauchy integral is \(\bar z\), giving the actual scalar vacuum \(2z\) after antisymmetrization.
These checks give the intrinsic starred vacua and full bounded-vector domains of both original canonical duals and their adjoints by the Gaussian criterion.

Freeness and the unit variance of \(S\) give \(\mathbb E_{W^*(Z)}Y^2=c^2D^{2\alpha}/(1+\alpha)\), where \(D=|Z|\).
This nonconstant conditional moment shows dependence, and \(Y\) is centered with positive variance.
For trace \(r^2\) the two minimizations integrate the increasing radial functions \(D^2\) and \(c^2D^{2\alpha}/(1+\alpha)\).
Relative to the disk cutoff, any other region of that area removes inner points and adds an equal area of outer points, where both functions take larger values.
Dividing its two integrals by \(r^2\) gives the specified \(r^2/2\) and \(c^2 r^{2\alpha}/(1+\alpha)^2\).
Each generator and its adjoint tends to zero on the normalized cutoff vectors, so each nonconstant word tends to zero there by boundedness of the prefix.
Evaluation at zero therefore descends to the represented polynomial algebra with norm one and extends multiplicatively to its norm closure.
For \(z=h e^{i\theta}, v=-h e^{i\theta}\) in the disk the phase \((\bar z-\bar v)/(z-v)\) equals \(e^{-2i\theta}\) for every \(0<h<1\).
Taking \(h\) to zero realizes every phase at the character, and continuity off the diagonal gives positive product area for any open angular tolerance in any neighborhood of zero.

For \(T=Z-Y\), the polar unitary \(U\) of \(Z\) commutes with \(D\), whose affiliated inverse exists.
The factor between the two \(D^{1/2}\)'s in \(T\) is at distance at most \(2c<1\) from \(U\), giving an affiliated inverse with unitary polar part.
Multiplying out \(T^{-1}-Z^{-1}\) gives the two exterior weights \(U^*D^{\alpha-1}\) and \(D^{\alpha-1}U^*\) and the middle factor \(cS(1-cD^{2\alpha-1}U^*S)^{-1}\) in the stated order.
The middle norm is bounded by \(K=2c/(1-2c)\).
Writing \(Q=T^{-1}-Z^{-1}\) and \(P=1-e_r\), the bound on \(PQP\) is \(K r^{-2(1-\alpha)}\).
The error \(e_rQ+PQe_r\) has right support of trace at most \(2r^2\), since the first summand has left support at most \(e_r\) and the second has right support at most \(e_r\).
Choosing \(r=(K/t)^{1/(2(1-\alpha))}\) for large \(t\) gives \(F_Q(t)=O(t^{-1/(1-\alpha)})=o(t^{-2})\), where \(F_X(t)=\tau(1_{(t,\infty)}(|X|))\).
Indeed \(Q\) has norm at most \(t\) on the kernel of the error, so the spectral subspace above \(t\) has dimension bounded by the codimension of that kernel.

The intersection of the two low spectral subspaces gives \(F_{A+B}(u+v)\le F_A(u)+F_B(v)\) by the same dimension bound.
For \(0<\varepsilon<1\), applying it in both directions sandwiches \(F_{T^{-1}}(t)\) between \(F_{Z^{-1}}((1+\varepsilon)t)-F_Q(\varepsilon t)\) and \(F_{Z^{-1}}((1-\varepsilon)t)+F_Q(\varepsilon t)\).
Since \(F_{Z^{-1}}(t)=t^{-2}\) for \(t\ge1\), letting \(\varepsilon\) decrease to zero gives coefficient one.
Nearby open cutoffs give the same coefficient for a closed endpoint, and unitary polar equivalence of \(|T^{-1}|\) with \(|T|^{-1}\) yields the asserted closed lower tail.
The disk is noncollinear and \(Y\) is a bounded nonscalar omitted shift of this actual normal tuple, so the classification applies and \(T\) is nonnormal.
For this shift the cubic integrand \(F(s)^3/s^3\) is \(O(s^3)\) near zero and bounded by \(s^{-3}\) at infinity.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0275_v1.md#decision-candidate) | The fixed decision of 2026-11-14T14:05 for the disk and its weighted semicircular shift. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0275_v1.md#statement) | Actual vacua and domains, dependence, common character with all planar marginal phases, both minimizers, nonnormality and the exact fixed-shift lower tail. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0275_v1.md#argument) | Gaussian integrability, normalized cutoff errors, multiplicative evaluation, affiliated inverse identity, spectral dimension comparison and cubic integrability. |
| [Finding](#finding) | [Gaussian covariance criterion](../../claims/Yin_C_F0260_v1.md#statement) | Realization of the field, sufficiency of the scalar vacuum and three coefficient tests, and both original canonical domains on the intrinsic algebra. |
| [Finding](#finding) | [Disk calculation](../../claims/Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Actual scalar vacuum for the normalized disk coordinate with its angular integral and normalization. |
| [Finding](#finding) | [Normal residual classification](../../claims/Yin_C_F0270_v1.md#statement) | Exact normality for scalar shifts only in the noncollinear case of an actual bounded normal tuple. |
