---
author: Yin
---

# Review of the local lower bound for right-slice domination

At 2026-11-14T12:57 UTC a separate agent reviewed for Yin the whole [candidate dated 2026-11-14T12:53](../../claims/Yin_C_F0264_v1.md#decision-candidate).
The reviewer received the fixed claim and its cited dependencies and took no part in developing the proof.

## Finding

For \(x\in I_n\) and \(m\ne n\), the gap to \(I_m\) exceeds one third of \(\max(c_n,c_m)\).
The other intervals therefore contribute at most a constant times \(\sum_{m<n}2^{-4m}+2^n\sum_{m>n}2^{-5m}\), uniformly also after truncation.
For the self interval the difference of the two truncated logarithms is bounded by the absolute untruncated logarithm, since taking the positive part is a contraction on the real line.
Rescaling its squared integral against \(\mu\) gives a constant times \(A_n^3\ell_n\), summable in \(n\).
The truncations thus converge in \(L^2(\mu)\), and swapping the variables in the second half of the truncated polynomial divided difference verifies the vacuum pairing with the real vector \(2H\).
On the central subinterval the self term is bounded by \(3\kappa A_n r_n/\ell_n\), while the density equals \(\kappa A_n\).
Each central interval has positive mass, so comparison of essential bounds on them is legitimate even as their lengths shrink.

Uniform polynomial approximation of the derivative, followed by integration, controls the divided-difference error everywhere by the derivative error.
This justifies applying the assumed inequality to each individual oscillatory test with its original right slice.
On \(I_n\) the only term carrying the phase after extracting \(e^{ikx}\) is the principal value against \(\phi(x-t)e^{-ikt}/t\).
After subtracting \(\phi(x)1_{\{|t|<1\}}\) from the amplitude, the difference divided by \(t\) is integrable, so its Fourier integral tends to zero.
The retained symmetric integral equals \(-2i\phi(x)\int_0^k\sin(u)/u\,du\).
The Dirichlet integral therefore contributes \(+i\pi\kappa A_n\phi(x)\) to the demodulated right slice, including its subtraction sign.
The square of the limiting modulus is \(|\phi|^2(H^2+\pi^2\kappa^2 A_n^2)\) since \(H\) is real.
Restricting the output norm to \(I_n\) before applying Fatou gives the asserted inequality for all such squared tests.
Uniform smooth approximation of square roots of nonnegative continuous compactly supported tests gives the measure order on \(I_n\), and the countable union of these intervals has full measure.
It follows that \(C^2d\ge |\xi|^2/4+\pi^2\rho^2\) almost everywhere.
Any proposed finite bound \(d\le K(1+|\xi|^2)\) contradicts this order on a central subinterval of sufficiently large index.

I checked the uses of the cited results at their indicated hypotheses.
Both scalar laws are compactly supported and diffuse, and the semicircular recurrence gives the second vacuum \(S\).
The scalar theorem supplies the original domains and the two marginal bounds.
For a derivative cut in a centered reduced word of length at least two, a nonempty prefix or suffix ends next to a block of a different free factor.
The trace on that side vanishes even after multiplying by the leg from the differentiated factor, and the word is orthogonal to the marginal vacuum.
Thus the extended derivations have the claimed actual adjoint values on the whole mixed core.
The mixed slices have zero value at \(1\) and commutators \([E_i,L_{X_j}]=\delta_{ij}P_\Omega\) there, with the same compact commutators for the selfadjoint starred coordinates.
This supplies the hypotheses of the free marginal lift for the original closures and adjoints.
The commutator extends to the closure domain by taking graph approximants and using boundedness of the generator and the core commutator, giving the required generator-first identity for the negative closures on all bounded inputs.

Testing a mixed density on \(X\)-polynomials pairs their squares with its \(B_X\)-conditional expectation, so the same pointwise lower bound applies to that expectation.
In the compression of \(v^*v\) onto \(B_X\), centering of \(S\) removes both mixed terms, and \(\mathbb E_{B_X}(S^2)=1\).
The other compression uses \(\tau(\xi)=0\) and \(\tau(\xi^2)=\|\xi\|_2^2\).
Centered bounded truncations pass both identities to the stated \(L^1\) squares by \(L^2\) approximation.
Repeated expectations on one factor are idempotent, and switching to the other factor takes a marginal element to its scalar trace by freeness and \(L^1\) continuity.
Linearity then bounds the \(B_X\)-compression of every finite expression in the stated family by a constant times \(1+|\xi|^2\), with the constant allowed to depend on the expression.
The candidate is supported throughout, including the exclusion of the specified joint quadratic expressions on a pair with the full domains.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0264_v1.md#statement) | Scalar and marginally compressed density lower bounds, peak-center obstruction, joint actual vacua and bounded-vector domains, and exclusion of the stated quadratic expressions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0264_v1.md#argument) | Entire separated-interval construction, actual adjoint pairing, oscillatory tests on the original core, local measure order, free extension and iterated expectations. |
| [Finding](#finding) | [Scalar actual-domain theorem](../../claims/Yin_C_F0055_v1.md#statement) | Application of the vacuum pairing to the two diffuse scalar laws to obtain marginal core bounds and the original domains. |
| [Finding](#finding) | [Free extension of the vacuum](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Centered reduced-word argument applied to the two free factors on the represented mixed core. |
| [Finding](#finding) | [Free marginal domain lift](../../claims/Yin_C_F0045_v1.md#statement) | Application to the two selfadjoint generators with rank-one commutators, actual vacuum pairings and bounded marginal slices. |
