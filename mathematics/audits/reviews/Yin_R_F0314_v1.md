---
author: Yin
---

# Independent review of the assembly of relative normal models

## Finding

At 2026-11-16T16:12 UTC an agent outside the development of the proof reviewed the complete candidate of C_F0305 v1 for Yin.
The initial inspection used the fixed candidate, the Task definitions and the mathematical interfaces listed below.
No development notes, proof-generation dialogue, author explanations or earlier conclusions about this candidate were supplied or consulted.
The construction proves both the conditional separation and the equivalence with the family of relative estimates.

The normalization \(\langle\zeta,Z\rangle=1\) gives \(\|\zeta\|_2\ge1\) after scaling \(Z\) to a contraction.
Real rescaling of each coefficient preserves the represented algebra and its zero derivative, including a coefficient already equal to zero.
Differentiating normality determines \(DZ^*\) uniquely because the outer spectral diagonal has zero projection for a diffuse law.
The phase has Hilbert norm one and is the same marginal vector in every trace-preserving enlargement.
For each chosen polynomial, telescoping the words in bounded old and new letters gives uniform continuity of its operator norm difference and of its formal coarse derivative difference.
In the latter estimate the single marked letter contributes a fixed unit or phase and all remaining multipliers are bounded.
Normalized right contraction preserves the resulting error bound.
Thus a fixed positive tolerance exists for each test before its mass is chosen, including when all tests come from one infinite-cost model.
All three upper constraints on the mass can then be met, since the vacuum norm is finite and positive.

The separated spectral disks give the individual block units even at indices tending to infinity, since each fixed disk misses the closure of the others.
Together with the compressed generators these units generate every block and bounded finite truncations recover the product.
The diagonal derivatives respect represented relations after entry evaluation.
Their values at the generators have uniformly bounded normalized coarse norms, so the squared inherited weights \(t_n^2\) and the product rule give a Hilbert tensor at every polynomial.
Comparison with the single-leg weight \(t_n\) gives diagonal vacuum entry \(t_n\zeta_n/\alpha_n\), with squared contributions \(4^{-n}\).
The auxiliary semicircular block has a finite rescaled vacuum.
For \(1\le n<k\) the squared mixed kernel norm is at most \(C4^n t_nt_k\), summable by the mass bounds, and the auxiliary block has a uniform spectral gap from these disks.
The mixed commutator gives exactly the missing unit tensors and phases.
Moving the two multipliers to the unit tensor gives the actual vacuum bound \(2\|L\|_2\|x\|_2\).
The mixed values at the coefficients have finite coarse norm, which is the cost paid when adding noise.

In extending the base derivation by zero on the noises, each cut in a centered alternating word containing noise has a trace leg with zero conditional expectation onto the base.
This follows because the corresponding prefix or suffix meets the cut at a noise block, and holds for each base Hilbert tensor by bounded outer multiplication and tensor approximation.
The enlarged derivation therefore retains the base vacuum.
For the correction at \(S_l\), freeness from the enlarged base of the other noises allows arbitrary base-tensor insertion.
Its vacuum for \(a\otimes b\) is \(a^*S_l b^*\) with the displayed outer actions.
The one-noise word isometry extends this formula to Hilbert tensors, with orthogonal ranges for different \(l\) and zero projection onto the base.
With insertion \(-D_0H_l\), the corrected derivative kills \(Y_l\).
Its surviving generator values are \(1\otimes1\) and the phase of \(Z\), both intrinsic to the target coarse space.
The ordinary noise derivatives also have intrinsic generator values, so on the target polynomial algebra restriction and orthogonal projection of the respective vacua give exactly the actual starred derivations required by the Task.

The projection \(e_n\) belongs to the target through \(Z\), although it need not be central there.
Both the old normalized model and the generated target corner sit trace-preservingly in the ambient normalized corner.
Free compression gives \(\|e_n S_l e_n\|=2\sqrt{t_n}\), since the compressed semicircle has variance \(t_n\) and the corner trace is faithful.
Comparison of the two evaluations uses this common corner, and requires only this marginal noise law.
The old individual coefficients need not be recoverable in the target.
The target relative derivative kills \(e_nY_le_n\) by its stated coefficient-algebra property.
After multiplication by \(\alpha_n\) it has the same generator values on the recentered \(Z_n,Z_n^*\) as in the formal comparison, giving \(a_{e_n}\ge b_n/(4\alpha_n)\).
The right contractions in the common corner agree on each of the two Hilbert subspaces with the respective intrinsic contractions.

For any fixed null sequence of cutoff radii, finite global cost \(a\) bounds each ambient cutoff by \(3a\) on the operator unit ball.
Consequently \(k(F_n)+B_{e_n}\le6a\), while the relative theorem bounds this sum below by \(t_n^{3/2}a_{e_n}>2^{n-2}\).
Infinite cost excludes every bare system by normal uniqueness and boundedness of the canonical core slice for such a system.
Conversely, every distinguished coordinate of an actual normal tuple is diffuse and its derivative kills both real components of each omitted coordinate.
These components generate the same starred core together with the distinguished coordinate, with the zero coefficient available in dimension one.
Apply the assumed relative estimates also to the adjoint tuple, using the flip-adjoint derivations with their actual adjoint vacua.
The right bounds in that orientation give the left bounds in the original orientation by tracial involution.
The two-slice theorem gives both full canonical domains, and the normal comparison supplies the generator-first system with the correct sign.
The constants may depend on the finite number of coefficients in each application.
The existence of an unbounded relative ratio and the truth of the unrestricted implication remain open.

The review checked the indicated dependency statements and their hypotheses at these uses.
The external compression formula was used at its recorded statement-and-applicability depth, without a new proof audit of its combinatorial derivation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0305_v1.md#decision-candidate) | Fixed 2026-11-16T16:08 candidate reviewed before adoption. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0305_v1.md#statement) | Conditional single-tuple separation, contraction normalization and universal equivalence for all fixed coefficient counts. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0305_v1.md#argument) | Entire proof including tolerance selection, actual star derivations, intrinsic target estimates and the converse. |
| [Finding](#finding) | [Task definitions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual starred ACSY, existential bare full-domain duals and the generator-first strong system. |
| [Finding](#finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Outer spectral diagonal, unique phase for diffuse distinguished coordinates, and zero starred derivative at omitted actual coordinates. |
| [Finding](#finding) | [One-generator assembly](../../claims/Yin_C_F0210_v1.md#the-actual-derivation-on-countably-many-corners) | Diagonal Hilbert weights and vacuum, and square-integrable mixed commutator kernel. |
| [Finding](#finding) | [Noise insertion](../../claims/Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) | Free selfadjoint insertion for a base Hilbert tensor and its actual one-noise vacuum. |
| [Finding](#finding) | [Free compression](../literature/NS06/Yin_U004.md#ns06-u004) | Compressed semicircular variance and operator norm under the normalized corner trace. |
| [Finding](#finding) | [Spectral corner](../../claims/Yin_C_F0301_v1.md#statement) | Coefficient algebra containing compressed omitted variables, normalized derivative and lower cutoff estimate. |
| [Finding](#finding) | [Global cutoffs](../../claims/Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Normal extensions at fixed positive radii and the uniform \(3a\) operator-to-Hilbert bound. |
| [Finding](#finding) | [Bare dual](../../claims/Yin_C_F0070_v1.md#statement) | Every normal bare system gives the bounded right slice of the unique normalized core derivative. |
| [Finding](#finding) | [Normal comparison](../../claims/Yin_C_F0075_v1.md#statement) | Adjoint tuple orientation, generator-first sign and recovery of the strong dual system. |
| [Finding](#finding) | [Two slices](../../claims/Yin_C_F0072_v1.md#statement) | Bounds on both contractions yield full original canonical and adjoint domains. |
