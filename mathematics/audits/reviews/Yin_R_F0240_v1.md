---
author: Yin
---
# Independent review of the supporting-half-plane singular-mass bounds

## Whole-proof finding

At 2026-11-13T17:16 UTC the reviewer independently checked the [statement](../../claims/Yin_C_F0231_v1.md#statement) and the complete [argument](../../claims/Yin_C_F0231_v1.md#argument) fixed at the [candidate decision](../../claims/Yin_C_F0231_v1.md#decision-candidate) of 2026-11-13T17:14.
The reviewer had used C_F0229 in previous work on radial vacuum functionals and had worked with the omitted-coordinate graph in a separate result about two-sided unitary changes.
The reviewer did not develop the supporting-half-plane result and had received no development discussion or earlier findings for its accretive resolvent and exponent iteration.
Both parts hold, including the absolute constant in the finite-scale estimate, the uniform little-order limit, the Gram bound, the finite-\(p\) endpoint and the bounded-vacuum logarithmic estimate.

**Resolvent in the actual graph.**
The accretivity constant is \(g=s-\kappa r=2(1+\kappa)r>0\).
The real parts of \(A,A^*\) give the same \(g\)-lower bound on their Hilbert norms, so \(A\) has closed dense range and bounded inverse in the represented von Neumann algebra.
C_F0217 allows bounded multiplication by every omitted coefficient in the graph of \(\bar\delta_i\) and puts that coefficient in the zero-derivative domain.
It follows that \(\bar\delta_i A=V^*\otimes W\).
For polynomials in \(A\), the bounded strong-star approximations of \(V,W,b\) and their adjoints in C_F0229 can be taken on a joint product net.
Applying the polynomial word rule before the limit leaves only the cuts at \(X\), and bounded strong-star convergence of both outer legs on the coarse Hilbert space gives the graph limit.
The displayed condition on \(C\) makes \(B=1-A/C\) a strict contraction.
The \(n\)-th power has derivative norm at most \(n\|B\|^{n-1}/C\), because \(\|V^*\otimes W\|_2=1\).
Thus both the polynomial Neumann series and its double derivative series converge in their indicated Hilbert norms.
The two sums give \(\bar\delta_i R=-RV^*\otimes WR\) with the factors in that order.
Omitted left and right multiplication gives derivative \(-VRV^*\otimes WRW^*\) on the actual graph vector \(VRW^*\).
Its vacuum pairing is \(-(\tau R)^2\), since both traces are traces of \(R\).
Taking the absolute value gives \(|\tau R|^2/q\) for the normalized vector, where \(q=\|R\|_2>0\).
As \(\operatorname{Re}R=R^*(\operatorname{Re} A)R\), this is at least \(g^2q^3\).

**Mass and packing.**
The small singular projection of \(D\) is \(W^*eW\), of trace \(t\).
Testing \(RA=1\) against it and applying trace Cauchy–Schwarz gives \(t\le q(s+r)\sqrt t\), also allowing \(t=0\).
Cubing the resulting bound \(t\le(s+r)^2q^2\) and squaring the vacuum inequality gives the factor
\[
 \frac{(s+r)^6}{g^4r^2}=\frac{3^6}{2^4}(1+\kappa)^2.
\]
For any finite family the map \(c\mapsto\sum_j c_j u_j\) has squared norm \(\|G\|\).
Its adjoint applied to \(\xi\) controls precisely the sum of the squared vacuum pairings.
This proves the stated packing estimate without requiring any orthogonality of these normalized vectors.
The hypothesis covers the displayed polar-shift example since the real part of \((-v)^*(X-b)\) is \(|b|-\operatorname{Re}(v^*X)\).
The separately cited C_F0211 tests the different hypothesis that the singular projections are orthogonal.

**Uniform limit.**
The finite-scale inequality for \(\kappa=0\) and \(\|u\|_2=1\) gives \(F(x)\le C_0x^{2/3}\) on the entire positive axis with the displayed \(C_0\).
The strict accretive representative \(A\) uses the omitted shift \(b-sVW^*\), so \(F\) controls its lower singular tail with the same \(\xi\), uniformly in the original shift norm.
The invertible polar decomposition makes \(|R|\) unitarily conjugate to \(|A|^{-1}\).
Its open upper tail at \(v\) is bounded by \(F(1/v)\), using the stipulated closed lower cutoff, and also by \(q^2/v^2\).
Splitting the layer integral at \(v_0=(q^2/K)^{1/(2-\gamma)}\) yields terms \(Kv_0^{1-\gamma}/(1-\gamma)\) and \(q^2/v_0\).
Their sum divided by \(q\) gives exactly \(H_\gamma K^{1/(2-\gamma)}q^{-\gamma/(2-\gamma)}\), \(H_\gamma=(2-\gamma)/(1-\gamma)\).
The positive initial constant follows also from \(\langle\xi,X\rangle=1\).
If the mass ratio stays bounded below along \(r\downarrow0\), then \(q\ge\sqrt t/(s+r)\) is bounded below by a positive constant times \(r^{-2/3}\).
Taking \(\gamma=2/3\) controls \(\|u\|_1\) uniformly along this sequence, with limit zero.
Bounded approximation to \(\xi\) in \(L^2\), together with \(\|u\|_2=1\), gives vanishing vacuum pairing there.
This contradicts the finite-scale estimate and proves the uniform limit.

**Higher integrability.**
Interpolation gives \(h=1-2/p\) on the \(L^1\) term because \(1/p'=h+(1-h)/2\).
Hölder, the exact resolvent inequality and the inverse-tail bound give \(g^2q^{3+\alpha}\le\|\xi\|_p H_\gamma^h K^{h/(2-\gamma)}\), with \(\alpha=h\gamma/(2-\gamma)\).
Raising to \(2/(3+\alpha)\) and inserting the mass estimate yields \(f(\gamma)=2(1+\alpha)/(3+\alpha)\), with coefficient bounded by that in (5).
This map is increasing and its difference from \(\gamma\) has the sign of \(2-(3-h)\gamma\).
Its fixed point above \(2/3\) is \(2/(3-h)=p/(p+1)\), so the sequence starting at \(2/3\) increases to that value.
On this interval \(H_\gamma\le2(p+1)\), \(a\le2/3\), \(\lambda=a/(2-\gamma)\le2/3\), and \(a+\lambda\le1\) follows by subtracting the two numerators to obtain \(3(1-h)(2-\gamma)\ge0\).
Consequently \(A_0 2^a B_0^\lambda\le B_0\) when \(B_0\ge\max(1,(2A_0)^3)\).
Taking \(B_0\ge C_0\) initializes (5), and its constants then stay at most \(B_0(p+1)\) through the entire iteration at zero tolerance.
The limit may be taken at each fixed \(x>0\) with this common constant, so it gives the endpoint exponent itself.
One more application of (5) returns to the original tolerance at the cost of \((1+\kappa)^2\).
Because \(\|\xi\|_2\le\|\xi\|_p\), the finite-\(p\) constants have exactly the allowed dependence.
When \(\xi\in M\), \(B_0\) is uniform in \(p\).
With \(p=\max(3,\log(1/r))\), \(r^{-1/(p+1)}\le\exp(1)\) and \(p+1\le4+\log(1/r)\), which gives the asserted \(r\log(\exp(1)/r)\) bound up to \(r=1\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0231_v1.md#statement) | Finite-scale and uniform little-order bounds, Gram packing, extensions for more integrable vacua and the polar-shift example. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0231_v1.md#argument) | Actual graph inverse and vacuum pairing, Gram norm, tail integration and passage to the fixed exponent with uniform constants. |
| [Whole-proof finding](#whole-proof-finding) | [Omitted-coordinate graph actions](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Left and right omitted multiplication on the closed graph and zero derivatives of omitted coefficients. |
| [Whole-proof finding](#whole-proof-finding) | [Shifted polynomial graph argument](../../claims/Yin_C_F0229_v1.md#argument) | Bounded strong-star polynomial approximants, fixed-word Leibniz convergence and the actual graph of the coordinate derivation. |
