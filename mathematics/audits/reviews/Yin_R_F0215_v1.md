---
author: Yin
---
# Independent review of the bounded circular direct-sum dual and its mixed energy

## Finding

At 2026-11-13T13:40 an agent outside proof development independently checked the complete statement and argument of the 2026-11-13 candidate C_F0207_v1 and the two input arguments at their uses below.
The review used the fixed claim, its mathematical inputs and the Task's definitions, without proof-development discussion, exploration notes, separately supplied author explanations or prior review findings on this claim.
The proof establishes every assertion in the statement.

The weights give \(2\sum_{n\ge1}t_n=1\).
In the normalized Fock space the orthogonal letters \(u,v\) give \(\ell_v^*\ell_u=0\), so \(\|c^k\|\le k+1\), while the pure powers on the vacuum give the two orthonormal sequences required for the coefficient matrix.
Right deletion gives the two intrinsic commutators with the claimed generator-first signs.
Between levels \(k>n\), the worst displacement of the right endpoint of the \(k\)-disk costs at most \(5r_k\), and \(2^{-n}-2^{-k}-r_n-5r_k>2^{-n}/4\).
Within level \(n\) the distance between the disks is \(2r_n\varepsilon_n>0\).
An isolating contour has positive distance from zero, so norm convergence of the tail generators to zero gives a uniform upper bound for their resolvents on the contour.
The Riesz projection therefore selects precisely one corner, whose translated and scaled circular generator recovers the corner algebra.
The central projections increase in finite sums to the identity, and the nonzero self-commutator in each corner persists in the product.

For the mixed equation, multiplying the proposed series by \(\Delta+r_a L_{c_a}-r_b R_{c_b}\) cancels each positive degree by Pascal's identity and leaves constant coefficient one.
Absolute summability follows from \((r_a+r_b)/|\Delta|<1\) separately for every ordered pair.
On intrinsic unit vectors, the ambient trace in the input functional and the output norm rescaling together give the factor \(\sqrt{t_at_b}\).
The functionals use the powers of \(c_b^*\), so the squared Hilbert--Schmidt norm really is \(t_at_b\sum_{m,l}|h_{ml}|^2\).
For a bounded solution of the homogeneous equation the intertwining identity transfers to each resolvent on the separating contour.
Its integral gives the identity on the output side and zero on the input side, forcing the intertwiner to vanish.

For \(d=2r(1+\varepsilon)\) within a single pair, the central binomial series gives the squared Hilbert--Schmidt norm \(t^2/(d\sqrt{d^2-4r^2})\), which grows without bound as \(n\) increases since \(t/r=48\).
For the same matrix, the absolute row sum at row \(m\) is \(t(r/(d-r))^m/(d-r)\), with the corresponding column estimate.
Schur's bound gives operator norm at most \(48\) in both directions, which suffices for the direct sum over pairs.
The different-level squared norms sum to at most a constant times \(\sum_k(k-1)t_k<\infty\), so these blocks assemble in Hilbert--Schmidt norm.
The diagonal scaling \(t_a/r_a\) gives exactly the required diagonal compression of \(P_\Omega\).
Equality of all matrix blocks thus proves the bounded commutator identity on the Hilbert sum and supplies both full-domain conditions.

For the starred generator the diagonal commutator vanishes.
On each same-level mixed block the triangle inequality gives \(\|L_{X_a^*}T_{ab}-T_{ab}L_{X_b^*}\|_{\rm HS}\le (d+4r)\|T_{ab}\|_{\rm HS}\), using the scalar difference \(d\) and \(\|c\|\le2\).
The resulting squared bounds sum because \(t_n^2/\sqrt{\varepsilon_n}=(9/4)4^{-n}\).
The Hilbert--Schmidt ideal also controls the different-level commutator.
Consequently every represented star word has a Hilbert--Schmidt commutator by Leibniz, and the coarse identification intertwines the required outer actions.
Pairing with the vacuum gives \(\tau(wD\Omega)-\langle D^*\Omega,w\Omega\rangle=\langle(D\Omega)^*-D^*\Omega,w\Omega\rangle\), using traciality and the isometric involution on \(L^2\).
This is a bounded \(L^2\) functional on the entire dense represented core, as required for the actual adjoint-domain condition.
The example establishes the failure of mixed Hilbert--Schmidt summability as a necessary condition for a bounded dual in this decomposition.
The general implication from actual ACSY to a bare full-domain dual lies outside this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0207_v1.md#statement) | The specified countable product, generation and nonnormality, actual ACSY, bounded dual and divergence of forced mixed energies. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0207_v1.md#argument) | All four proof sections, including spectral separation, both mixed-block norms, bounded assembly and the starred adjoint-domain identity. |
| [Finding](#finding) | [Circular Fock construction](../../claims/Yin_C_F0074_v1.md#argument) | Normalized circular representation, generation, nonnormality and both intrinsic generator-first commutators. |
| [Finding](#finding) | [Central corner gluing](../../claims/Yin_C_F0206_v1.md#argument) | Coarse tensor identification, outer actions, inherited norm scaling and the corner compressions of the ambient vacuum projection. |
