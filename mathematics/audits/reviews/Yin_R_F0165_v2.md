---
author: Yin
---
# Independent review of the criterion for bounded Hermitian Gaussian coordinates

Yin is the human record author.
The review was performed at 2026-11-13T13:13 (UTC).
An AI reviewer outside proof development inspected the complete [v2 statement and proof](../../claims/Yin_C_F0157_v2.md#statement) and the interfaces listed below.
The reviewer received the fixed inputs and reviewed them without the exploration notes or development discussion.
The v1 theorem was read as a proof input, and its separate review conclusion was compared only after forming the findings on v2.

## Finding

The equivalence, vacuum formulas, canonical bounds and example hold for the stated row-bounded Hermitian kernels.

**Coordinate and generation.**
On degree zero the creation operator acts by \(f\mapsto a(z,w)f(w)\), so normalized indicators of row-integral level sets give its norm upon taking the supremum.
On every higher degree the same row integral bounds the squared norm by \(\rho(a)^2\).
The clipped Hermitian fields are bounded in operator norm by \(2\rho(a)\), and their vacuum vectors are Cauchy in tracial \(L^2\).
Testing bounded right multiples of the vacuum gives a strong limit in \(M\), and testing adjacent degrees identifies its creation and adjoint blocks.
Conversely any bounded representative has the prescribed action on those degree-zero indicators by right multiplication.
This proves the criterion and both norm inequalities, including the zero kernel case.
The v1 phase multiplier depends only on \(\theta\), which is bounded even when \(a\) is unbounded.
Its action on clipped fields therefore passes to this strong limit.
When \(b>0\) almost everywhere, the product indicators span a dense subspace of \(L^2(b^2\mu^2)\), and multiplication by \(b\) maps this space isometrically onto \(L^2(\mu^2)\) with inverse \(h\mapsto h/b\).
Thus \(S\Omega\) belongs to the target Hilbert space, and the conditional expectation onto the target fixes \(S\).

**Necessity on the intrinsic core.**
Diffuseness makes the outer diagonal null, so the normal relation fixes the two derivations on \(Z^*\).
Compression of the \(Z\) vacuum supplies the scalar vacuum.
Before using generation, the linear test gives the measure identity \(b\,\overline{P_{H_1}\xi_T}=1\), since \(b\) and the projection are in \(L^2\) and products of marginal star polynomials determine measures on the compact product.
Positivity almost everywhere and the inverse-square integral follow.
In the separated-endpoint test, the degree-zero term vanishes and the middle derivative pairs to zero.
Hermiticity gives \(\int b(z,w)^2b(w,v)^2\,d\mu^3\le\rho(b)^4\), which controls the degree-two clipped products in \(L^2\).
The two endpoint derivatives have the difference \(b(w,v)^2-b(z,w)^2\) in that order and denominator \(z-v\).
The separated tests determine locally integrable densities on every pair of disjoint endpoint neighborhoods and hence off the null diagonal.
Taking into account conjugation in the first inner-product slot gives precisely (1).

**Sufficiency and full domains.**
Symmetry and positivity are preserved by clipping, and generation holds for each clip in the same \(M\).
Taking the minimum of \(\log b\) and \(\log m\) decreases the absolute difference of the two edge logarithms on each path or leaves it equal.
The monotonicity of \(\sinh\) gives \(|\chi_{b_m}|\le|\chi_b|\), and \(b_m^{-2}\le b^{-2}+1\) gives domination for the other vacuum.
Both clipped vacuum vectors therefore converge in norm.
At a common operator cutoff, tracial \(L^2\) convergence implies star-moment convergence by telescoping on each word.
The clipped \(E_{j,m}\) have the operator-first commutators used in the dual optima, and taking adjoint matrix elements on bounded vectors gives those commutators for \(-E_{j,m}^*\) at the adjoint tuple.
The estimates on both sets of optima survive by lower semicontinuity.
The normal two-sided criterion gives \(\mathsf S\), Part C of C_F0070 gives \(\mathsf A\), and Part 4 of C_F0075 identifies the original canonical domains.
This also proves \(\mathsf S\Rightarrow\mathsf A\) independently of any integrability hypothesis.

**Vacua and quantitative constants.**
For the positive case every starred generator derivative in a clipped polynomial is a common fixed tensor, since \(T_{b_m}\) is selfadjoint and the phase for \(Z^*\) is fixed.
The bounded polynomial coefficient actions converge strongly on both coarse legs, so the derivatives and both traced contractions converge on the moving cores.
Passing the vacuum pairings identifies all degrees by density, including the absence of higher components.
For the bounds on the whole unit ball, a common pointwise weak subnet of the clipped restrictions and actual adjoints exists by weak compactness of the individual Hilbert balls and product compactness.
The displacement from \(p(X_m)\) to \(p(X)\), tested against \(h\in M\), is bounded by \(\|E_{j,m}^*h\|_2\|p(X_m)-p(X)\|_2\).
This identifies the first limit on the core.
The adjoint pairing first identifies the second limit on \(M\) with the actual adjoint and then identifies the first limit on \(M\) with the canonical closure, using its established full domain.
Weak lower semicontinuity thus preserves the separate constants, including the smaller coefficient for \(E_T^*\).
For the reversed contraction the core formula \(F_Zp=p\xi_Z-E_Z^*p\) extends by bounded strong-star approximation, since the original and adjoint-tuple canonical graphs are weakly closed and their bounded restrictions are operator-norm-to-\(L^2\) bounded.
Using this formula at the clips and at the limit transfers the sharper \(K\|\xi_Z\|_2\) bound for \(F_Z\).
In the normal mixed-energy identity each of the two vacuum pairings is bounded in modulus by \(K\|\xi_Z\|_2^2\), and the squared contraction terms are bounded by \(2K^2\|\xi_Z\|_2^2\) in total.
This gives the stated lower estimate on the analytic-unitary tests of C_F0156.
Transport by the tracial phase automorphism multiplies the first-degree vacuum by \(\theta\), producing \(1/\overline a\), and multiplies the second-degree vacuum by both successive edge phases.
It preserves all four bounded-input norms.

**Strict example.**
The normalized area integral of \(1/|z-v|\) is at most four on the disk, so antisymmetrizing the scalar vacuum functional gives a bounded density.
On a row in \(F_n\) the squared row norm is \(2-t_n\).
The only curvature contributions for that middle point come from opposite sides of the boundary of \(F_n\), in both orders.
Polar integration from boundary distance \(s\) up to radius two yields \(2\log(2/s)\).
Averaging over \(F_n\) adds \(3/2\) inside the logarithmic bound, since \(2\int_0^1 u(-\log(1-u))\,du=3/2\).
The prefactor \(t_n(t_n^{-1/2}-t_n^{1/2})^2=(1-t_n)^2\) is bounded and \(\sum_n t_n(1+|\log r_n|)<\infty\).
Testing \(T_b-T_{b_m}\) on \(1_{F_n}/\sqrt{t_n}\) gives norm \((1-m\sqrt{t_n})_+\), tending to one for each fixed cap.
This proves the asserted strict enlargement and the failure of operator-norm convergence.

The review covers the entire v2 proof and preserves v1 at its bounded-kernel scope.
The foundational compactness results and earlier project claims were used at their stated interfaces.
The original literature proofs were not re-audited.
The converse from bare \(\mathsf F\) and the unrestricted normal implication remain open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0157_v2.md#statement) | Bounded-coordinate characterization, intrinsic equivalence, vacuum formulas, original canonical domains, constants, curvature bound and example. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0157_v2.md#argument) | Entire Wick, necessity, clipping and common-algebra limit argument, including the infinite spectral blocks. |
| [Finding](#finding) | [Task contract](../../tasks/Yin_T_F0011_v1.md#contract) | Definitions of the three conditions, inner products and generator-first sign convention. |
| [Finding](#finding) | [Bounded Hermitian theorem](../../claims/Yin_C_F0157_v1.md#statement) | All clipped conclusions and measurable phase automorphism applied to bounded fields before taking limits. |
| [Finding](#finding) | [Arbitrary abelian base](../../claims/Yin_C_F0153_v1.md#relative-degree-with-an-arbitrary-abelian-base) | Relative Wick spaces, creation, annihilation and degree-zero tests. |
| [Finding](#finding) | [Target tests](../../claims/Yin_C_F0156_v1.md#actual-target-moment-tests) | Forced marginal derivatives, smooth endpoint graph tests and two-term trace identity. |
| [Finding](#finding) | [Bounded-kernel estimates](../../claims/Yin_C_F0156_v1.md#quantitative-bounds-and-curvature-form) | Exact constants, actual adjoint formula, reversed contraction and scope of analytic-unitary tests. |
| [Finding](#finding) | [Closed norm sublevels](../../claims/Yin_C_F0201_v2.md#statement) | Both dual optima at a common cutoff and the normal two-sided criterion at the limit. |
| [Finding](#finding) | [Strong to ACSY](../../claims/Yin_C_F0070_v1.md#statement) | Part C for the normal generating tuple in the target algebra. |
| [Finding](#finding) | [Compactness](../literature/Keh25/Yin_U001.md#keh25-u001) | Product compactness for the simultaneous pointwise weak subnet of restrictions and adjoints. |
| [Finding](#finding) | [Normal mixed energy](../../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | The energy identity on analytic unitaries before the source's separate growth estimate. |
| [Finding](#finding) | [Canonical compatibility](../../claims/Yin_C_F0075_v1.md#statement) | Part 4 for the original closures and both adjoint domains, including the adjoint tuple. |
