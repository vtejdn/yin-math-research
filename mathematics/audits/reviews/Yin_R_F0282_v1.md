---
author: Yin
---

# Review of the local secant obstruction at a singular concentration point

## Finding

At 2026-11-14T14:01 UTC an agent outside proof development independently checked the whole [C_F0273 v1 candidate](../../claims/Yin_C_F0273_v1.md#decision-candidate) dated 2026-11-14T13:48 and its five declared input interfaces.
The reviewer received the fixed proof and review scope without its exploration notes, proof-development dialogue or previous findings on the candidate.
Both lower bounds and the finiteness conclusion follow at their stated scopes.

Write \(I_\eta=\int_\eta^\infty F(s)^3\,ds/s^3\).
Under the selection probability, the numerator of the third moment of \(J(2^js)/F(s)\) is bounded by \(2^{2j}\int_{2^j\eta}^\infty J(t)^3\,dt/t^3\), hence by \(27\,2^{2j}I_\eta\).
The zero set of \(F\) has selection probability zero.
For \(2/3<\alpha<1\), Markov's inequality summed over \(j\ge0\) gives the asserted summable exceptional probability, uniformly in \(\eta\).
This leaves positive probability after imposing the original bound \(J(s)\le6F(s)\), the size cutoff and the finitely many adjoint tests.
The common-point extraction therefore still applies and \(A/H\le24\).

Fix an open neighborhood \(O\) of the extracted point and let \(p=1_{K\setminus O}(Z)\).
The two probabilities put vanishing mass on this closed complement.
For \(P\le2^ms\) the ratio \(a_s(P)/h_s(P)\) is at most \(2^m\).
For \(P>2^ms\) the trace of the \(a_s\)-tail divided by \(H\) is bounded by \(4C_\alpha2^\alpha\sum_{j\ge m}2^{-(1-\alpha)j}\), using \(F\le J\) and \(H\ge F(s)/4\).
Traciality gives the same bound after polar conjugation.
Taking the scale limit first and then increasing \(m\) controls both \(\tau(pa)/H\) and \(\tau(pUaU^*)/H\).
For a marginal contraction \(c=pcp\), trace Cauchy–Schwarz applied to \(p\sqrt a\) and \(cpU\sqrt a\) bounds \(\lvert\tau(cUa)\rvert\) by \(\sqrt{\tau(pa)\tau(pUaU^*)}\).
The supremum over \(c\) controls \(\lvert G\rvert(K\setminus O)\), including possible cancellations in the complex measure.

Full support and diffuseness exclude isolated points of \(K\).
The limiting phase set is the nested intersection of nonempty compact closures of local phase sets, so the minimax radius is attained and every larger radius bounds all sufficiently local secants about a minimizing center.
At each finite scale the original marginal law dominates all three leg measures in the sense of absolute continuity.
The diagonal is therefore null for both product variations, although the limiting products can charge \((z_0,z_0)\).
Off \(O^2\) their variations vanish by the one-leg bounds, and on \(O^2\) the substitution of \(\lambda\) for \(k\) costs at most \(\epsilon(A/H)^2\) and \(\epsilon A/H\), respectively.
The unit tensor tests give \(1=\int k\,d(G\otimes G)+o(1)\) and \(0=\int k\,d(R\otimes G)+\overline{G(1)}+o(1)\).
Passing to scalar subsequential limits \(B=\lim A/H,\ q=\lim G(1)\) preserves the point already extracted.
For \(y=\sqrt\lambda\,q\), the second test bounds \(2\lvert\operatorname{Re}y\rvert\) by \(\epsilon B\) and the first gives \(1\le(\operatorname{Re}y)^2+\epsilon B^2\).
Thus \(1\le(e+e^2/4)B^2\) for \(e=e(z_0)\), giving the first constant with \(B\le24\).
Taking the family to be the entire omitted algebra yields the stated contrapositive without requiring a common direction or neighborhood for different points.

For the critical singleton law \(F(s)=\min(s^{2/3},1)\), \(J(2^js)\le3\,2^{2j/3}s^{2/3}\) for all \(s\le1\).
The tail argument thus applies to every common point along the concentrating sequence.
The given distribution function has total mass one on \((0,1)\) and density \(2v^{-1/3}/3\) there.
After dilation, the exponents in the two beta integrals are \(5/6\) for \(A\) and \(1/3\) for \(H\).
The integrals converge and their ratio tends to \(\sqrt3\), giving \(e\ge4/\sqrt3-2\).
The vacuum error is also controlled if the common point is obtained along an arbitrary sequence of radii decreasing to zero at this fixed shift.
Indeed \(H\) is comparable to \(s^{2/3}\), \(A/H\) stays bounded, and \(\|h\|_2,\|V\|_2\le\sqrt H\).
The normalized pairings \(s\langle\xi,h\rangle/H^2\) and \(s\langle\xi,V\rangle/H^2\) tend to zero for bounded \(\xi\) by the trace norms \(H,A\), and the bounds in \(L^2\) extend this convergence to the actual vacuum by density.
The general divergent envelope uses the strengthened scale selection to obtain at least one common point.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0273_v1.md#decision-candidate) | Fixed decision dated 2026-11-14T13:48 with its two angular lower bounds and five input interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0273_v1.md#statement) | One possible limit for every divergent envelope, the local finiteness criterion, and every concentrating limit for the fixed critical law. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0273_v1.md#argument) | Joint dyadic selection, both polar tails, variation at finite scales, both scalar limits and the exact critical ratio. |
| [Finding](#finding) | [Concentration theorem](../../claims/Yin_C_F0269_v1.md#statement) | A common weak limit of both positive spectral states for a fixed or varying shift along the selected radii. |
| [Finding](#finding) | [Simultaneous choice of scales](../../claims/Yin_C_F0269_v1.md#simultaneous-choice-of-scales) | Dilation on the truncated half-line, the original bad-set budgets, mass comparison and adjoint-test errors. |
| [Finding](#finding) | [Two tensor identities](../../claims/Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal) | Unit test signs, placement of the conjugate, finite-scale absolute continuity and the measurable secant multiplier. |
| [Finding](#finding) | [Two scalar tests](../../claims/Yin_C_F0272_v1.md#combining-both-resolvent-tests-at-one-radius) | Direct square-root phase calculation bounding the real part of the normalized squared complex trace. |
| [Finding](#finding) | [Mellin integral](../../claims/Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test) | Beta integral on the positive half-line for exponents \(5/6\) and \(1/3\). |
