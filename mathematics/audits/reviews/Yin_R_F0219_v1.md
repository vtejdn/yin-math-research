---
author: Yin
---
# Independent review of optimal densities and weighted coordinate commutators

## Whole-proof finding

At 2026-11-13T14:01 UTC, a separate agent reviewed the [statement](../../claims/Yin_C_F0211_v1.md#statement) and [argument](../../claims/Yin_C_F0211_v1.md#argument) of Yin's candidate fixed at 2026-11-13T13:57.
The reviewer had no role in developing the proof and received or consulted no development discussion, exploration drafts, author explanations or earlier findings on this candidate.
The full statement holds, including the claim about every optimal state, attainment and uniqueness for a fixed density, and the obstruction for mixed spectral projections.

For \(h\in\operatorname{Dom}E_0^*\), the scalar functional \(b\mapsto\langle h,E_B b\rangle\) on \(B\) is the restriction of \(a\mapsto\langle E_0^*h,a\Omega\rangle\) on \(M\).
The latter is normal, so its composition with the quotient map is the unique normal extension of the scalar functional from \(B\) to \(B^{**}\).
The Hilbert adjoint domain contains the dense represented polynomial core by the actual ACSY vacuum.
Testing with these \(h\) therefore kills the entire kernel of the quotient in the vector-valued bidual map.
For an arbitrary optimal state, the GNS estimate on its cyclic subspace extends to the Hilbert space by continuity and then to inputs in \(B^{**}\) by weak-star density.
Restriction to the central summand representing \(M\) gives domination by a positive normal functional of mass \(m\).
The value \(E(X_i)=1\) excludes \(m=0\).
For \(0<m<1\), normalizing the functional and summing its singleton estimates gives the column constant \(c\sqrt m<c\), since \(c>0\).
Thus the original state assigns full mass to this central summand and has the stated unique normal extension.

For \(Y=X_i-\lambda1\), left multiplication by \(Y\) has norm \(\|Y\|\) on \(L^2(M)\), so both terms in the commutator tested on \(a\) have norm at most \(c\|Y\|\,\|a\sqrt d\|_2\).
Testing at the positive resolvent \(a=(d+\varepsilon1)^{-1}\) gives \(\tau(a)^2\le 4c^2\|Y\|^2\tau(a)\).
A kernel projection of positive trace would contribute its trace divided by \(\varepsilon\) to \(\tau(a)\).
Monotone convergence on the resulting full support gives the asserted inverse estimate for every \(\lambda\), hence also for their infimum.
For \(q_m=1_{[1/m,m]}(d)\), the bounded coefficients \(a q_m d^{-1/2}\) realize \(a q_m\) in \(M\sqrt d\), and \(a q_m\to a\) in \(L^2\).
Strong density in the left representation then gives density of \(P\sqrt d\) by testing approximation on the single vector \(\sqrt d\).
The same cutoffs in both square roots reduce \(\langle d^{-1/2},a\sqrt d\rangle\) to the limit of \(\tau(aq_m)\).
Both vector cutoffs converge in \(L^2\), so the pairing equals \(\tau(a)\) for every bounded \(a\).

The weighted estimate determines a bounded implementer on the dense space, and testing finite columns bounds \(c\) by its norm.
For an arbitrary admissible pair, \(F(a)=T(a\sqrt d)\) is bounded from the operator norm to \(L^2\), vanishes at \(1\), and the trace pairing just checked gives its prescribed commutators with each generator.
The individual-generator formulas of C_F0070 apply to this one map on all bounded inputs.
On a starred generator they give the Hilbert–Schmidt operator of the normal phase for index \(i\) and zero for the other indices.
These are exactly the commutators of the right slice by C_F0076 Part 1 and ACSY24 Theorem 3.4.
Induction by removing the leftmost letter now identifies \(F\) with the slice on every represented starred word.
The density of \(P\sqrt d\) gives uniqueness for this \(d\), and summing the resulting bounds over finite columns excludes a bounded pair when \(c=\infty\).

For each \(b\in N_i\), bounded commutation with the other normal left generators extends to their adjoints and then to their generated von Neumann algebra.
For \(L=X_i-b\), its polar partial isometry identifies the spectral projections of \(|L|\) and \(|L^*|\) on \((r,\infty)\).
The complementary projections \(e\) and \(f\) therefore have equal trace \(s\), even if the kernels differ.
The compressed terms \(L_f T L_{Le}\) and \(L_{fL} T L_e\) each have norm at most \(cr\), since \(\|Le\|,\|fL\|\le r\).
The compressed rank-one operator has norm \(\sqrt s\,\|e d^{-1/2}\|_2\).
The trace identity with \(a=e=e^2\) gives \(\langle e d^{-1/2},e\sqrt d\rangle=s\), so Cauchy–Schwarz yields \(s^3\le4c^2r^2\tau(de)\), also when \(s=0\).
Pairwise orthogonality of the right projections alone permits summing these masses against the state of density \(d\).
Divergence along such finite families forces infinite column constant, precisely the premise for the two-Haar obstruction.

The three project dependencies were checked at the interfaces used here, with their existing reviews of the [column criterion](Yin_R_F0216_v1.md#finding), [individual commutators](Yin_R_F0043_v1.md#conclusion) and [ACSY phase](Yin_R_F0049_v1.md#conclusion).
The three literature inputs were checked against the retained source units at their recorded inspection depths.
The review establishes the conditional obstruction and leaves existence of a tuple with divergent sums open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0211_v1.md#statement) | Normality of every optimal state, inverse bound, weighted realization with attainment and uniqueness for each density, starred-core converse and mixed packing obstruction. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0211_v1.md#argument) | Central summand and optimality, resolvent and density cutoffs, trace pairing, both directions of the commutator test, and compression by distinct left and right projections. |
| [Whole-proof finding](#whole-proof-finding) | [Column and state criterion](../../claims/Yin_C_F0208_v1.md#statement) | Optimal state exists at the exact finite column constant, and an infinite constant for one coordinate excludes bare full-domain systems on its two-free-Haar augmentation. |
| [Whole-proof finding](#whole-proof-finding) | [Bidual representation](../literature/Bla06/Yin_U002.md#bla06-u002) | Universal normal extensions of the tracial and GNS representations and the central kernel complement identified with the tracial range. |
| [Whole-proof finding](#whole-proof-finding) | [Canonical slice](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4 gives the dense adjoint domain and the Hilbert–Schmidt commutator with each element of the represented starred core. |
| [Whole-proof finding](#whole-proof-finding) | [Tracial predual](../literature/AP18/Yin_U003.md#ap18-u003) | The normal positive functional of mass one has a unique positive integrable density of trace one in the given finite tracial algebra. |
| [Whole-proof finding](#whole-proof-finding) | [Individual commutators](../../claims/Yin_C_F0070_v1.md#statement-and-interfaces) | Forced phase in the inhomogeneous case and commutation with the adjoint in the homogeneous case for a single bounded map on \(M\). |
| [Whole-proof finding](#whole-proof-finding) | [Normal ACSY phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1 identifies the starred derivatives of the actual system with the same phase and zero off the specified coordinate. |
