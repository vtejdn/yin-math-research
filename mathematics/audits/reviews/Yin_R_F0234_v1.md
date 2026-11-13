---
author: Yin
---
# Independent review of radial univalent circular changes and the Koebe endpoint

## Whole-proof finding

At 2026-11-13T16:12 UTC a reviewer independent of this proof's development checked all four parts of the [statement](../../claims/Yin_C_F0224_v1.md#statement) and the entire [argument](../../claims/Yin_C_F0224_v1.md#argument) fixed at 2026-11-13T16:04.
The reviewer had encountered circular Fock methods through other results and had worked on a separate group-algebra construction.
The reviewer had no substantive development context for this candidate and consulted neither its exploration draft nor a prior review of it.
The four conclusions hold with the stated hypotheses, constants and input norms.

For \(F(\zeta)=1/f(1/\zeta)\), the normalized exterior difference quotient equals \(d(z)d(w)/g(z,w)\) at \(z=1/\zeta,\ w=1/\eta\).
The minus sign in the exterior logarithm therefore gives the positive sign in the exponential factor of \(g\).
Krushkal's stated coefficient normalization makes \(T_{mn}=\sqrt{mn}\,b_{mn}\) a contraction.
The norm squares of \(v(z)\) are finite in the open disk, and exponential-vector inner products yield precisely the Hardy kernel.
This gives the isometric embedding of the entire Taylor space and the compression with coefficient kernel \(\exp(\sum b_{mn}z^mw^n)\).
The right multiplier is the Taylor-basis transpose, which preserves operator norm even for complex coefficients.
Belyaev's disk growth bound gives \(\sup |z/f(z)|\le4\), proving the norm bound \(16\).
For Koebe, direct subtraction gives \(g(z,w)=(1-z)^2(1-w)^2/(1-zw)\), hence \(A_f=(I-S)^2(I-S^*)^2\) has norm \(4^2\).

Univalence on \(|z|<1/t\) puts the inverse in a neighborhood of the filled Jordan image of each smaller closed disk.
Its complement is connected, so polynomial Runge approximation supplies exactly the inverse hypothesis of the circular change theorem.
The map and its inverse approximation recover \(B\) in operator norm.
The normalization \(f_t'(0)=1\) gives the attained least vacuum \(c\) and the fixed-law theorem supplies a whole-Hilbert-space dual.
The pointwise forced commutator at \(c\) is \(J_+ W_tA_fW_t J_-^*\), since \((J_-^*a)_n=\tau(c^na)\).
Strong convergence follows from both diagonal contractions tending strongly to the identity.

The extra phase in \(D_\theta\) cancels the inverse rotation of \(c\) in the commutator.
The \(m,n\) entry of the resulting kernel has rotation degree \(m+n\), so Poisson averaging produces the same two-sided radial scaling.
On a fixed input polynomial the relevant trace coefficients are finite in number by the rotation degrees, and the pointwise norm continuity on \(B\) justifies the integral of each output.
The radial kernel times the divided difference of \(f_t\) is \(1\), and exponential coefficient decay together with \(\|c^n\|\le n+1\) gives absolute convergence of the corresponding operator products.
The resulting commutator with \(Z_t\) on \(B\) has the rank-one form needed for the central-summand bidual transfer.
Applying the construction at radii \(s/t\) yields monotonicity without requiring the transferred map to extend the original one pointwise.
When the radial costs have finite supremum, weak compactness of the product of the pointwise balls gives an endpoint map on \(B\), and the strong forced-kernel limit identifies its commutator.
If the radial costs are unbounded, the previously proved upper bound by \(b_f\) gives the same extended-real equality.

The shift intertwining identities give \(K_{z^k,t}=J_+P_tM_{k,t}P_t^*J_-^*\), with both shift powers on the indicated sides of \(D_t\).
Alternating unit vectors supported on an initial segment are approximate \(-1\) eigenvectors for both shifts.
At \(t=1\) their limiting norm under this product is \(16k\), attaining the upper bound in operator norm.
At \(t<1\), the supports in each inner product for \(N=2k\) overlap in at least \(N/2\) coordinates.
Every additional shift from \(P_t,P_t^*\) changes the alternating-vector sign and its coefficient sign together, so retaining the two constant factors gives the lower bound \(kt^{4k}/2\).
The circular power has Hilbert norm one and the strong Haagerup bound gives operator norm \(O(\sqrt{k})\).
The commutator of any whole-Hilbert dual therefore gives the stated lower rate by \(k=\lfloor(-\log t)^{-1}\rfloor\).
For the matching upper rate the suffix spaces of \(Q_n\) are mutually orthogonal on the input, with output projection onto words ending in \(u^n\).
Thus \(T_tT_t^*\) has norm \((1-t^4)^{-1}\) by testing on arbitrarily long \(u\)-words.
The one noncommuting left-right pair in \(Q_n\) contributes \(r_u^nP_\Omega(r_v^*)^n\), including the vacuum case \(n=0\).
Multiplication by the two outer factors in \(B_t\) therefore gives exactly the required radial kernel and then the unit commutator at \(Z_t\).

The shifted-circular \(R\)-transform and inverse relation give \(sh(1+h)^2=1-(\lambda^2-1)h\) on the negative resolvent axis, first at large \(s\) and throughout \(s>0\) by real analyticity.
The two tracial squared-singular laws are the same by polar decomposition.
Positivity and the resolvent bound give \(h(s)\le\min(s^{-1/3},s^{-1})\).
Integration against \(s^{-1/2}/\pi\) gives \(8/\pi\), and rotation and scaling give the stated \(16/\pi\) bound on \(y_a\) in \(H^\infty\).
The lower-radius series bound covers \(w=0\) as well.

At the endpoint \(S^*S=I\) gives the sine recurrence, including the first two boundary values.
The sine image of a bounded analytic \(y\) has pointwise bound \(\sqrt{2/\pi}\|y\|_\infty\), obtained first on dilates.
For the analytic \(p\), the mutually orthogonal output spaces \(u^jV_-\) give square bounds for all the tails \(h_j(1)\) and \(h_j(-1)\) from approximate shift eigenvectors.
The coefficient at \(l\) in \(d_p\) sums the terms \(p_{|l|+1+2m}\), so Parseval counts each positive \(|l|\) twice and gives the stated \(\sqrt 2\) bound on the full circle.
Evenness converts that estimate to \(\|M_{p,1}\|_{H^\infty\to H^2}\le2\|p(c)\|\) with the declared sine normalization.
For the radial integral, on \(e_m\) the phase of \(S^j V_\theta(S^*)^{k-1-j}\) is \(e^{i(m+j-k+1)\theta}\) whenever the vector survives.
This agrees with the half-angle formula including its scalar \(e^{-i(k-1)\theta/2}\), and circular rotation preserves the polynomial norm.
The two polynomial factors have the claimed Hardy bounds since \(\|S^*\|_{H^\infty\to H^\infty}\le2\).
This establishes the uniform estimate on bounded inputs even though the individual Hilbert operator norms of the endpoint monomial kernels grow as \(16k\).
The estimate governs analytic commutators and leaves the behavior of the full Koebe bounded-input costs unresolved within this argument.

The review checked the weighted Grunsky contraction and logarithm convention in Krushkal §1.3, the normalized growth inequality in Belyaev Theorem 3.2.11, and the squared-shift \(R\)-transform and inversion in Haagerup–Kemp–Speicher, arXiv v1, Theorem 2.2 and (1.3), (2.11).
Those external results were used at statement and applicability depth, with their original proofs outside this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0224_v1.md#statement) | All four parts, equality examples, the extended-real endpoint, the Hilbert asymptotic and the bounded-input scope. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0224_v1.md#argument) | Coefficient compression, radial averaging, weak limits, both Hilbert estimates, resolvent bound and general polynomial sine transform. |
| [Whole-proof finding](#whole-proof-finding) | [Univalent circular changes](../../claims/Yin_C_F0218_v1.md#statement) | Radial inverse approximation, generation, fixed-law Hilbert dual, actual least vacuum and forced first commutator. |
| [Whole-proof finding](#whole-proof-finding) | [Analytic commutator series](../../claims/Yin_C_F0218_v1.md#convergent-power-series-and-simultaneous-commutators) | Circular powers, absolute summation and multiplication by the divided difference. |
| [Whole-proof finding](#whole-proof-finding) | [Central-summand transfer](../../claims/Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) | Domain transfer after obtaining the rank-one generator commutator, with no increase in norm. |
| [Whole-proof finding](#whole-proof-finding) | [Polynomial Runge theorem](../literature/GW25/Yin_U001.md#gw25-u001) | Connected-complement compact image and holomorphic inverse on a neighborhood. |
| [Whole-proof finding](#whole-proof-finding) | [Strong Haagerup inequality](../literature/KS07/Yin_U001.md#ks07-u001) | Homogeneous circular power, its unit Hilbert norm and the square-root degree bound. |
| [Whole-proof finding](#whole-proof-finding) | [Exterior Grunsky input](../../claims/Yin_C_F0224_v1.md#exterior-grunsky-input) | Exterior normalization, logarithm sign, square-root weighting and contraction for all normalized univalent maps. |
| [Whole-proof finding](#whole-proof-finding) | [Disk growth input](../../claims/Yin_C_F0224_v1.md#disk-growth-input) | Lower growth estimate for the normalized disk map and the multiplier bound. |
| [Whole-proof finding](#whole-proof-finding) | [Shifted circular input](../../claims/Yin_C_F0224_v1.md#shifted-circular-input) | Unit-variance real-shift formula, its Cauchy inverse branch and the induced trace-norm bound. |
