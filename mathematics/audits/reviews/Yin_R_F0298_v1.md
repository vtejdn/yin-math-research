---
author: Yin
---

# Review of the projection orbit test for the original slice domains

## Finding

At 2026-11-14T16:05 UTC a reviewer outside proof development completed an independent inspection of the [fixed candidate](../../claims/Yin_C_F0289_v1.md#decision-candidate), its entire statement and argument, and all seven declared dependencies at their points of use.
The review used the fixed mathematical materials and the assigned scope without exploration notes, development dialogue, author explanations or previous findings on this candidate.
Equations (1)–(3) and the simultaneous category conclusion hold for every indicated trace, every old unitary and every prescribed positive sequence of radii tending to zero.
For the tuple-wide strong condition, the two oriented tests are applied at every old coordinate, with the same projection and orbit throughout.

The centered polynomial bases span their respective cores algebraically, so every finite vector of old core coefficients represents an enlarged polynomial, and conversely.
In these coordinates the enlarged slice acts entrywise.
Truncation and approximation in the individual graph norms give the full graph of the closure.
Testing one coordinate at a time gives the adjoint domains on the individual copies, and testing finite sums gives precisely square summability of the adjoint outputs.
For either old closed operator \(T\) and any unit \(k\), membership of \(k\otimes h\) in the corresponding direct-sum domain implies \(h\in\operatorname{Dom}T\) by taking a nonzero coordinate of \(k\).
Conversely the squared sum of the outputs is \(\|Th\|_2^2\) for every \(h\in\operatorname{Dom}T\).
The centered letter \(f-t\) contributes only nonempty prefixes after splitting \(u\) into its scalar and centered parts.
The resulting prefix vector \(k_u\) has norm one after division by \(\sqrt{t(1-t)}\).
This identifies \(J_u h=k_u\otimes h\) and puts its entire range perpendicular to the old copy of \(H\), including the old adjoint vacuum.
The scalar term of \(q(u)\) has forward value zero and adjoint value \(t\xi\), which gives both value formulas and their domains.
The adjoint tuple generates the same factors and orbit and admits the same construction with its own slice and vacuum.

For a separated inner multiplier \(v\otimes z\), a cut before a new-factor suffix has right leg of the form \(z\eta s b\), with \(\eta\) an old Hilbert vector, \(s\) a centered reduced word starting and ending in the new factor, and \(b\) the final old coefficient.
Its trace vanishes by freeness and Hilbert continuity.
For a cut in \(b\), the prefix passes unchanged through the multiplier on the inner legs.
Uniform approximation of the continuous fixed-radius kernel on the compact marginal spectrum squared by finite sums of separated functions gives the cutoff identity on every core word.
Bounded strong-star polynomial approximants to \(u,f-t,u^*\), centered exactly in the middle, yield prefixes converging in Hilbert norm and old output coefficients converging weakly by fixed-radius normality.
Their tensor products therefore converge weakly to the right-hand side of (2).
Bounded strong-star convergence of the products identifies the same limit with the normal augmented cutoff on \(q(u)-t1\).
Every radius \(r>0\) is covered because it can be included in a prescribed sequence with limit zero.

For finite \(a\), the old normal extension agrees on \(M\) with the closed graph by bounded strong approximation and weak graph closure, and its norm is \(a\).
Every old contraction is the average of two old unitaries after completing the partial isometry in its polar decomposition.
For at least two coordinates the algebra is a finite factor, so the complementary supports are equivalent because they have equal trace.
I checked this use of Corollary 2.4.11 in the retained undated 338-page Anantharaman–Popa draft, printed p. 39 (PDF p. 45), and accept its statement under the given factor and faithful tracial state hypotheses.
The original proof of that corollary was outside the inspection.
For one normal generator its abelian polar phase extends on the zero set.
Thus finite \(K\) bounds the old core ball by \(K/\sigma\), including when finiteness of \(a\) is initially unknown.
Equation (1) recovers equality when \(a<\infty\).
Equation (2) gives \(B/\sigma=\sup_n\|E_{r_n}\|_{M\to H}\) by the same unitary average.
Core convergence gives its lower bound \(a\), and the separated multiplier estimate gives its upper bound \(3a\) in the finite case.
The column comparison for \(d\ge3\) is a finiteness test via \(a\le c\le\sqrt2\,a\).

For \(x=u^*v\), centering \(x\) gives \(\tau((f-t)x(f-t)x^*)=\sigma^2|\tau(x)|^2\).
The squared orbit distance is \(\sigma^2(1+|\tau(x)|)\) times the squared phase quotient distance, with \(q(u)=q(v)\) precisely when \(u,v\) differ by a scalar phase.
The quotient is complete by successively aligning phases on a subsequence with summable increments and taking its Hilbert limit.
This limit is a unitary because the operator unit ball is Hilbert closed and bounded products and adjoints preserve Hilbert convergence there.
Graph sublevels are closed by weak compactness of the output ball, and cutoff sublevels are closed by fixed-radius normality on bounded inputs.
If either contains a relative open patch, its preimage under \(u\mapsto q(u^*)\) is a neighborhood of an old unitary \(v\).
For all selfadjoint contractions \(h\), the two unitaries \(v(\sqrt{1-\epsilon^2 h^2}\pm i\epsilon h)\) belong to this neighborhood when one sufficiently small \(\epsilon>0\) is fixed.
Their difference uniformly bounds the output at \(vh\), with graph membership in the forward case.
Taking the real and imaginary parts of \(v^*p\) then bounds the entire core unit ball, using core convergence for the cutoff family.
For infinite \(a\) this rules out interior for every sublevel of both types.
Completeness gives a simultaneous dense \(G_\delta\) on the orbit, and bounded cutoff outputs on a nonmeagre subset force finite \(a\) and the old full forward domain.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0289_v1.md#decision-candidate) | Full candidate dated 2026-11-14T15:58, with the explicit all-coordinate quantifier and all seven declared mathematical dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0289_v1.md#statement) | Both domains and values, adjoint orthogonality, all positive radii, extended costs, simultaneous orbit category at interior trace and the strong condition tested at every old coordinate. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0289_v1.md#argument) | Algebraic core, full graphs, normal limits, unitary averages, phase quotient geometry, patch bound and Baire conclusion. |
| [Finding](#finding) | [Free right module](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Polynomial basis expansion, old coefficient isometries, core right-trace cancellation and Haar vacuum. |
| [Finding](#finding) | [Single free extension](../../claims/Yin_C_F0278_v1.md#free-extension-of-a-slice) | Preservation of actual vacua and applicability of the two-factor reduced-word decomposition to one freely adjoined Haar unitary. |
| [Finding](#finding) | [Normal cutoffs](../../claims/Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Bounded normal extension at fixed radius on both tuples, convergence on the old core and uniform bound \(3a\). |
| [Finding](#finding) | [Bounded original map](../../claims/Yin_C_F0276_v1.md#statement) | Norm \(a\) of the normal old extension and the finite-column comparison in dimensions at least three. |
| [Finding](#finding) | [Factoriality](../../claims/Yin_C_F0202_v1.md#statement) | Two or more actual normal coordinates force the finite algebra to be a factor. |
| [Finding](#finding) | [Finite projection comparison](../literature/AP18/Yin_U004.md#ap18-u004) | Corollary 2.4.11, printed p. 39 in the retained edition, gives equivalence of complementary projections of equal trace in the factor. |
| [Finding](#finding) | [Both normal orientations](../../claims/Yin_C_F0075_v1.md#statement) | The two orientations at every old coordinate decide the existential strong condition and both original canonical bounded-vector domains. |
