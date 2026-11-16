---
author: Yin
---

# Review of the one-point test for a deficient normal slice

## Finding

At 2026-11-16T15:36 UTC a reviewing agent outside proof development checked the [fixed candidate](../../claims/Yin_C_F0299_v1.md#decision-candidate) of 2026-11-16T15:33 for Yin.
The inspection used the candidate and the directly invoked materials without development dialogue, author explanations or previous findings on this candidate.
The whole argument supports the stated one-point test for tuples of length at least three, the conditional pair result and the universal reduction.

For a pair the omitted von Neumann algebra \(N\) is abelian, so the commutant of \(C=N'\cap M\) inside \(M\) is precisely its center.
For a Haar \(v\in N\), a coarse vector fixed by outer conjugation by \(v\) would be supported on the diagonal of the two spectral copies of \(v\); the diffuse partition estimate makes this vector zero.
Consequently, for each bounded polynomial approximant of \(c\in C\), averaging sufficiently many conjugates makes its coarse derivative as small as desired, independently of how large that derivative was initially.
The input error is at most its original \(L^2\) error because \(c\) commutes with \(v\).
For each such finite average the omitted powers can in turn be approximated by uniformly bounded omitted polynomials and their adjoints.
Strong convergence of the outer actions on the coarse space gives the same derivative limit with those replacements.
The cutoff multiplier and the slice are contractions on the coarse space, so the product-rule error for \(c_lx\) is bounded by \(\|\delta c_l\|_2\|x\|\).
Fixed-radius normality first in \(c_lx\), then in \(x\), yields the claimed left module identity on all bounded inputs without assuming that the unregularized slice is bounded.

For the inner product linear in the second variable, the liberation pairing gives \(\tau(w^*ce)=\tau(c)\tau(e)\), hence by cyclicity it is \(\mathbb E_A(e w^*)=\tau(e)1\) that enters the positive conditional two-by-two matrix.
The lower right entry is \(\mathbb E_A(ww^*)\).
Because \(A\) is abelian, its determinant inequality is a pointwise inequality between measurable functions, valid also for unbounded \(w\in L^2\).
The case \(e=1\) gives \(h\ge1\); the zero trace of the commutator gives \(\tau(h)=1+\|\eta\|_2^2\).
A bounded vacuum makes \(w\) and \(h\) bounded.

The marginal product error is at most twice the scalar cutoff norm, hence at most \(6b_0\) on contractions.
For \(x=xF\), the input \(Fux\) is already in the tested corner; the smaller output projection on the right does not increase its test cost.
Averaging \(\|FuT_j(x)b\|_2^2\) tests \(u^*Fu\) against the integrable positive density of \(T_j(x)b\).
The bounded convex averages therefore converge in this pairing when they converge in \(L^2\).
For at least two omitted indices the resulting expectation is \(\tau(F)1\), and for a pair it dominates \(\tau(F)^2h^{-1}\).
The ball has positive mass by faithfulness of the spectral trace at every spectral point.
The right off-support estimate handles \(x(1-F)\) before the finite covering argument, and orthogonality on the right permits the squared estimates to be added even though the left weight need not commute with the marginal projections.
The tracial Cauchy--Schwarz inequality applies to the product \(h^{1/2}(h^{-1/2}T_jx)\).
Module covariance at \(1_{[1,L]}(h)\) then bounds the low-weight inputs for \(L\ge1\); below one this projection is zero.
These bounds do not remove an unbounded pair weight.

In the unweighted case a global bound on the regularizations gives the core bound by convergence on each polynomial, and the reverse bound is uniform for the prescribed sequence.
Failure therefore supplies a point all of whose neighborhoods have infinite compressed cost, which also forces unbounded uncompressed cutoff norms on the same input corners.
The punctured-neighborhood construction in the cited localization proof only needs these latter norms on arbitrarily small neighborhoods and zero spectral mass of the removed set.
Removing one point satisfies both requirements.
The shrinking corners control the scalar tail pairings independently of the selected subset, so one sequence tests every infinite subsum while finite sums retain the four graph memberships and both cutoff limits.
The construction asserts existence of a suitable point for the specified orientation, without uniqueness or a common choice for both orientations.
Finally, a one-coordinate actual normal tuple has bounded scalar slices, and free extension of a failed pair preserves its polynomial witnesses and their norms in the same orientation.
Neither the local finiteness premise for all tuples nor the universal implication of F0011 is established here.

The dependency checks concern the invoked statements and their operative interfaces.
Kaplansky density was used from the registered statement: bounded strong convergence of these approximants in the tracial representation implies \(L^2\) and bounded strong-star convergence.
No new proof audit of this source, recursive audit of all earlier Claims or formal verification was performed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0299_v1.md#decision-candidate) | The dated candidate and its nine dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0299_v1.md#statement) | Both orientations, one-point test, pair weight, projections and reduction of the universal question. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0299_v1.md#argument) | Bounded module approximation, conditional density, corner averaging, gluing and all infinite subsums. |
| [Finding](#finding) | [Relative commutants](../../claims/Yin_C_F0202_v1.md#statement) | Two distinct omitted coordinates give scalar commutant; diffuse coarse conjugation permits averaging. |
| [Finding](#finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Bounded approximation in the original and omitted polynomial algebras. |
| [Finding](#finding) | [Normal cutoffs](../../claims/Yin_C_F0282_v1.md#statement) | Fixed-radius normality, convergence on the core and the uniform threefold bound on bounded inputs. |
| [Finding](#finding) | [Liberation](../../claims/Yin_C_F0238_v1.md#statement) | The sign and ordering of the vacuum commutator, the inner multiplier and the finite liberation cost. |
| [Finding](#finding) | [Marginal bridge](../../claims/Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Conditional expectation of the right factor, scalar product error, uniform marginal cost and the one-coordinate case. |
| [Finding](#finding) | [Averaging](../../claims/Yin_C_F0276_v1.md#averaging-over-the-omitted-algebra) | Conditional expectation onto the commutant as the Hilbert limit of bounded convex averages. |
| [Finding](#finding) | [Localization](../../claims/Yin_C_F0295_v1.md#argument) | Bound off the doubled ball and the punctured-corner construction through simultaneous subsum failure. |
| [Finding](#finding) | [Domain comparison](../../claims/Yin_C_F0075_v1.md#statement) | Failing the strong hypothesis on an actual normal pair forces an unbounded single-input slice in some orientation. |
| [Finding](#finding) | [Free extension](../../claims/Yin_C_F0278_v1.md#statement) | Free Haar adjunction preserves actual conjugates, original polynomial witnesses and the adjoint orientation. |
