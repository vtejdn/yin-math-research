---
author: Yin
---

# Review of the cubic bound for a narrow cone of marginal secants

## Finding

At 2026-11-14T13:58 UTC an agent outside proof development independently checked the whole [C_F0272 v1 candidate](../../claims/Yin_C_F0272_v1.md#decision-candidate) dated 2026-11-14T13:46 and its five declared dependency interfaces.
The reviewer received the fixed proof and its review scope without exploration notes, proof-generation dialogue, author explanations or previous findings on this candidate.
The proof establishes the uniform cubic estimate under the stated strict cone bound, including the Lipschitz graph application.

The graph calculation applies to each \(T=Z-b\) with \(b\in N\), since the omitted algebra and its adjoints have zero derivative in the closed graph and both kernels of \(T,T^*\) vanish.
For \(R=(T^*T+s^2)^{-1}\) one has \(h=s^2R\), \(V=sTR\), \(Th=sV\), and \(hT^*=sV^*\).
Inverse differentiation therefore gives the two negative summands in \(s\delta h\), with \(V\) on the opposite leg of the term containing \(k\) and \(V^*\) on the first leg of the other.
The inclusion of the marginal product algebra in \(M\bar\otimes M^{\rm op}\) preserves its operator norm, so the essential phase bound in the product spectral law gives \(\|k-\lambda 1\|_\infty\le\varepsilon\) in the tensor estimates.
For the product trace the two error multipliers have trace norms \(A^2\) and \(HA\), since \(|V|=a_s(P)\) and the opposite leg has the same singular-value law.
The trace on the opposite leg is complex linear, so substituting the constant phase gives the two traced derivatives \(H^2-\lambda m^2\) and \(-H(\lambda m+\bar m)\), respectively.
The uniform pairing errors after multiplication by \(s\) are bounded by \(s^2D(s)\), since both scaled absolute values \(|V|/s\) and \(h/s\) are dominated by \(\min(1/s,1/P)\) in spectral calculus.

Writing \(y=\sqrt\lambda\,m\) gives \(|\lambda m+\bar m|=2|\operatorname{Re}y|\) and \(\operatorname{Re}(\lambda m^2)\le(\operatorname{Re}y)^2\).
When \(H>d_s\), division of the second trace bound by \(H\) costs at most \(d_s\) in the error.
The Euclidean triangle inequality in the first bound then gives \(H\le\sqrt{\varepsilon+\varepsilon^2/4}\,A+\sqrt5\,d_s/2\), which also holds for \(H\le d_s\).
The requirement \(c=\sqrt{\varepsilon+\varepsilon^2/4}<1/\sqrt3\) gives precisely the stated upper endpoint and leaves room to choose \(\beta\) strictly above \(2/3\), also for \(\varepsilon=0\).

At \(t>0\), substituting \(u=ty\) gives the full Mellin integral before truncation as \((\pi/2)t^{-\beta}(\csc(\pi\beta/2)-c\sec(\pi\beta/2))\).
It is nonnegative, and removing an initial interval preserves the sign because the integrand is negative only below \(c\).
On \(0\le t\le1\) and \(u\ge1\) the unweighted kernel is at least \((1-c)/2\), giving the cutoff factor \((1-c)/(2\beta)\).
Integration at a fixed shift is justified by boundedness on the left and \(D(s)\le\|\xi\|_2/s\) on the right.
Taking the supremum afterwards gives the claimed monotone envelope even when the optimizing shifts vary with radius.

On \(s\ge\eta\), the scaling \(s^{2/3}D(s)\) incurs the integrable factor \(y^{-2/3}\) against \(dy/y\), giving the factor \(\sqrt{3/2}\) after taking a square root.
The change \(s=ru\) takes the truncated domain into \(s\ge\eta u\), and multiplying by \(r^{-2/3}\) contributes \(u^{2/3}\), yielding exactly \(1/(\beta-2/3)\) in the scale average.
For the generalized inverse \(Q(t)=\inf\{r\ge\eta:F(r)>t\}\), layer integration gives \(I_\eta=(3/2)\int_0^1 t^2/Q(t)^2\,dt\).
In the matching formula for \(J_\eta\), Hölder with exponents \(4,4,2\) and \(\|H_\xi(t)/t\|_2\le2\|v_\xi\|_2\) give the claimed factor \(3(2I_\eta/3)^{1/4}\sqrt2\,\|\xi\|_2^{3/2}\).
Substitution leaves \(I_\eta^{1/4}\) bounded by a constant depending only on \(\varepsilon\) times \(\|\xi\|_2^{1/2}\), proving the integral estimate upon taking the fourth power and letting \(\eta\) decrease to zero.

Any two distinct graph points have distinct real coordinates, so their phase in graph coordinates equals \((1-iu)/(1+iu)\) for a real secant slope \(|u|\le L\).
Its distance from one is \(2|u|/\sqrt{1+u^2}\), and rotation multiplies every phase by the same unit scalar.
This argument covers graphs over compact subsets and uses diffuseness to discard the diagonal.
The finding covers the cubic obstruction under the strict cone bound.
Optimality at its endpoint and control of the full mixed column cost remain open here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0272_v1.md#decision-candidate) | Entire fixed candidate dated 2026-11-14T13:46 and the five direct interfaces below. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0272_v1.md#statement) | Strict marginal secant bound, all omitted shifts, cubic integral and the rotated Lipschitz graph criterion. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0272_v1.md#argument) | Both original graph tests, elimination of the complex mean, threshold, scale integration before the supremum, nonlinear estimate and graph geometry. |
| [Finding](#finding) | [Shifted resolvent graph](../../claims/Yin_C_F0229_v1.md#argument) | Arbitrary bounded omitted shift, unitary polar decomposition and original closed graph for the two resolvent tests. |
| [Finding](#finding) | [Two resolvent identities](../../claims/Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal) | Tensor order, scalar phase, adjoint on the first leg and signs of both traced derivatives. |
| [Finding](#finding) | [Rearrangement bound](../../claims/Yin_C_F0269_v1.md#simultaneous-choice-of-scales) | Simultaneous fixed-radius pairing bounds against the same vacuum, uniform over the family \(N\). |
| [Finding](#finding) | [Positive scale average](../../claims/Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test) | Mellin sign, lower cutoff bound and integrability for the selected \(c,\beta\). |
| [Finding](#finding) | [Truncated integral bounds](../../claims/Yin_C_F0261_v2.md#closing-the-cubic-integral) | Dilation on truncated domains, layer and Hardy constants, homogeneity and monotone passage to the full integral. |
