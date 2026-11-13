---
author: Yin
---
# Independent whole-proof review of the two-Haar column criterion

## Finding

At 2026-11-13T13:43, a reviewer outside the development of the proof completed the check of Yin's [C_F0208 v1 candidate](../../claims/Yin_C_F0208_v1.md#decision-candidate).
The inputs were the fixed statement, argument, definitions and cited dependencies.
The reviewer received no exploration notes, proof-generation discussion, author explanation or earlier verdict on this candidate.

**Free-product derivations and right slice.**
Faithfulness of the reduced tracial product identifies the algebraic free product of the three represented polynomial cores with the represented augmented core.
For a differentiated letter in a centered mixed word, one of the exterior segments is nonempty and meets that letter in a different factor.
The trace functional on the corresponding tensor leg vanishes on that segment multiplied by any vector from the differentiated factor, by reduction of bounded vectors and continuity on its \(L^2\) space.
The double trace therefore vanishes on the whole completed derivative tensor.
This equals the pairing with the factor vacuum by orthogonality of reduced tensors.
On a Haar factor, the positive Laurent powers give a nonzero double trace only for the single letter \(u\), while every inverse-power derivative has negative powers on both legs.
These tests establish the actual vacuum condition for every coordinate.

In the two-factor decomposition, Gram–Schmidt on the countable spanning family of centered starred monomials gives bounded letters and finite expansions on each core.
Grouping a terminal \(M\)-letter or the empty terminal segment gives mutually orthogonal right modules \(wL^2(M)\), each isometric to \(L^2(M)\).
Testing against \(a,b\in M\) gives \(\mathbb E_M(w^*w')=\delta_{ww'}1\).
Every old-factor cut internal to \(w\) has a suffix beginning and ending in the other factor, so its right trace is zero even after adjoining an old terminal coefficient.
Consequently the square sum of the sliced coefficients is the squared \(L^2\) norm of the augmented slice, while the squared column norm of the input is bounded by \(\|\mathbb E_M(y^*y)\|\le\|y\|^2\).
For finite \(c_i\), the vacuum gives closability and the core bound gives weakly convergent image subnets of norm-controlled Kaplansky approximants.
The closed linear graph is weakly closed, and the same subnet identifies the image of \(Z_j a\) by the core commutator.
This proves the upper bound on all bounded inputs.

**Column encoding and lower bound.**
Successively distinct conjugates \(U^k V U^{-k}\) separate nonzero powers of \(V\) by nonzero powers of \(U\), giving joint free Haar moments and freeness from \(M\).
For \(y=\sum_k u_k b_k\), conditional expectation gives \(\mathbb E_M(y^*y)=\sum_k b_k^*b_k\), whose norm is \(Q^2\).
In the norm estimate the terms \(u_k(1-P_k)b_k z\) land in orthogonal initial-letter subspaces and have square sum at most \(Q^2\|z\|_2^2\).
For the other terms \(P_k b_k\) acts on the initial \(k\)-sector and the initial \(M,k\)-sector by the row \((\tau(b_k),x\mapsto\tau(b_kx))\).
The norm of its second entry on the centered space is the \(L^2\) norm of the centered part of \(b_k^*\), giving row norm \(\|b_k\|_2\).
The row input spaces are mutually orthogonal across \(k\), so Cauchy–Schwarz gives the second bound \(Q\|z\|_2\) even though the output spaces after \(u_k\) need not be orthogonal.
Together these estimates give \(\|y\|\le 2Q\) with no row norm of the coefficient family.

Subtracting \(aT(1)\) costs at most \(\|T\|\) in addition to the supplied witness norm.
For this single coordinate, the inhomogeneous normal formula fixes the starred commutator on the distinguished generator, and the homogeneous formula applies separately to every other generator.
The augmented canonical slice has these same commutators and value zero at \(1\), hence agrees with the normalized witness by induction on all starred words.
Testing at \(y\) yields \(c_i\le4\|T\|\), and automatic boundedness rules out algebraic bare witnesses when \(c_i=\infty\).
When \(c_i=\infty\), the upper bound is vacuous and the feasible set for the infimum is empty.

**State and universal conclusions.**
The state space maps to a compact convex subset of the real test-coordinate space.
Strict separation from the closed positive orthant would require nonnegative weights and a strictly negative supremum, contradicted by applying the column inequality to the square-root weighted family.
Weak-star compactness then gives simultaneous domination at the optimal nonnegative constant, and summation against a state proves the reverse bound.
Universal existence of bare systems applies to the augmented ACSY tuple, giving finite constants for all original coordinates by automatic boundedness and the lower estimate.
Conversely, the finite constants supply augmented witnesses, and their compressions to \(L^2(M)\), with sign reversed for the generator-first convention, give the bare system on \(M\).
The universal passage to strong domains uses ACSY stability under taking the adjoint tuple and the two bare hypotheses of C_F0075.

The stated two-sided estimate, optimal state domination and equivalence of the three universal assertions follow.
The final text specifies the centered monomial family for Gram–Schmidt, requires a nonnegative domination constant and negates the compressed maps under the Task convention.
This finding leaves open whether an infinite column constant occurs for any normal ACSY tuple.
The external sources were used at their recorded interfaces, and the project dependencies were checked for applicability at the scopes below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0208_v1.md#statement) | All augmented vacua, both constants, failure criterion, optimal state domination and universal equivalences. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0208_v1.md#argument) | Whole argument from reduced products through compression and the adjoint-tuple implication. |
| [Finding](#finding) | [Task definitions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | The represented starred ACSY condition, bare and strong domains, and the generator-first sign. |
| [Finding](#finding) | [Single-coordinate optimum](../../claims/Yin_C_F0201_v1.md#statement) | Global witness infimum, unrestricted vacuum value and sign. |
| [Finding](#finding) | [Normal derivative phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, diffuseness and uniqueness of starred generator values for a normal ACSY tuple. |
| [Finding](#finding) | [Free products](../literature/Voi98/Yin_U005.md#voi98-u005) | Sections 5.5–5.8, reduced Hilbert spaces and the left factor action. |
| [Finding](#finding) | [Canonical slice](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4, closability and Hilbert–Schmidt commutator on the starred core under an actual vacuum. |
| [Finding](#finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Theorem 2.3.1 at statement depth, strong approximation of bounded inputs by the core with the same norm bound. |
| [Finding](#finding) | [Single-coordinate normal formulas](../../claims/Yin_C_F0070_v1.md#statement-and-interfaces) | Inhomogeneous starred phase for one witness and homogeneous Fuglede identity for its remaining generators. |
| [Finding](#finding) | [Automatic continuity](../../claims/Yin_C_F0069_v1.md#statement) | Part A, a bare witness with the prescribed nonzero projection commutator at a bounded normal generator. |
| [Finding](#finding) | [Strong systems](../../claims/Yin_C_F0075_v1.md#statement) | Parts 2–3, the two bare hypotheses and the universal normal implications. |
