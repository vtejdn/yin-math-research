---
author: Yin
---

# Review of spectral relabelling from unbounded relative corner ratios

## Finding

At 2026-11-16T16:04 UTC a separately assigned agent for Yin independently reviewed the complete [C_F0304 v1 candidate](../../claims/Yin_C_F0304_v1.md#decision-candidate) fixed at 2026-11-16T16:01 UTC.
The reviewer did not participate in its development and received the fixed claim without development dialogue, proposed repairs or earlier reviews of the candidate.
The implication from unbounded relative ratios, the small changes of the generator and the actual vacuum, the equivalent universal estimate, and its application to both orientations of the Möbius base follow under the stated hypotheses.

The correction at the corner unit gives the exact identity \(b(F)=t^{3/2}\sup_r\|T_r^e\|_{\infty\to L^2(\tau_e)}\).
Core convergence and the relative Gaussian bound compare this with \(t^{3/2}a_F\) in both directions; the two global cutoff terms give \(b(F)\le6a\).
At fixed radius, compressing the witness \(x\) to \(e_lxe_l\) preserves contractivity and gives bounded strong-star convergence.
Normality of the cutoff gives weak Hilbert convergence, which persists under the other bounded strong-star convergent factors by testing against a fixed Hilbert vector.
Consequently a positive witness cost survives deletion of a sufficiently small total trace.
The normalized vacuum pairing on \(eZ\) is one, so an unbounded ratio forces \(t\to0\).
Under passage to a subset, both integrals in the unnormalized scalar energy are monotone, as is the squared norm of the compressed nonmarginal vector; the two-sided norm comparison gives a uniform bound on the new denominator in terms of the old.
After the summable deletions the differences have positive measure, are pairwise disjoint, and retain unbounded ratios.

The weighted squared masses of the relative vacua are summable on this disjoint family, and the two marginal measures of the fixed liberation vector are finite.
Thus the conditions in (3) can be met simultaneously.
The affine images are disjoint even at neighboring scales since each image radius is at most \(2^{-n-5}\); their distance from the old unchanged piece is greater than one.
This gives an injective Borel change with Borel inverse on its image and an \(L^2\) change of the generator bounded by a fixed multiple of \(\sqrt{\mu(B_*)}\).
For the new scalar law the sum of within-piece energies over positive indices is bounded by \(C\sum v_{B_n}^2/\alpha_n^2=O(\delta^2)\).
For a point in the \(n\)-th piece, \(\sum_{m\ne n}t_m/d_{nm}^2\) is uniformly bounded since \(4^{\min(n,m)}\le4^m\) for positive indices.
This bounds both the cross density and the integrated squared curvature of every triple with at least two piece indices: its curvature is at most twice the reciprocal length of any side between distinct pieces.
The scalar geometric criterion therefore applies also at the accumulation point of the disks, where there is no extra atom.

On a positive-index piece the scalar vacuum is the sum of its internal vacuum multiplied by the piece mass and the weak soft Cauchy limit over its complement, with factor two and conjugation as in the scalar adjoint formula.
The internal squared norms sum to \(O(\delta^2)\) and the cross integral is uniformly bounded pointwise.
On \(B_0\) the old and new internal contributions cancel in their common weak limit.
The new cross contribution is bounded by \(2\mu(B_*)\).
For the old law apply the separated multiplier identity to \(f=1_{B_*}\) and restrict to \(B_0\): the term containing \(fS(v)\) vanishes and \(|fv|=|f|\) for every character \(v\).
Both surviving slices have norm bounded by \((2+\sqrt2)\|f\sqrt W\|_2\), uniformly in the radius.
The identity passes from bounded polynomial approximants to \(f\) by the integrable weight bound and fixed-radius normality; the bounded estimates also dominate the character average.
Absolute continuity of \(W\,d\mu\) now makes the old cross contribution small in norm, rather than just weakly small.
For the nonmarginal vector the inverse-gap multipliers agree on \(B_0^2\), cost at most \(\sum v_{B_n}^2/\alpha_n^2\) in squared norm on the other diagonal blocks, and satisfy the weighted two-leg bound (3) off these blocks.
The old vector restricted to rectangles touching \(B_*\) tends to zero since its two leg measures are normal with respect to the old spectral law.
The recovery formula thus gives actual vacua with the asserted strong proximity.
At every unchanged coordinate the same liberation vector, original scalar law and original spectral multiplier give the very same vacuum.

In the \(e_n\)-corner the old and new outside algebras contain \(e_n\) and all omitted generators.
Their complementary spectral generators determine one another by bounded Borel calculus on \(1-e_n\), so their corner coefficient algebras have the same von Neumann closure.
Each coefficient from this closure admits bounded strong-star approximation by old coefficients and by new ones with zero liberation derivative.
The two closed liberation graphs consequently give the same product formula on common words.
The affine relation and positivity of \(\alpha_n\) give \(k_r(\alpha_n u)=\alpha_n^{-1}k_{r/\alpha_n}(u)\), with the same inner spectral projections, so both normal cutoffs compare on the entire corner.
The core limits and uniform Gaussian estimates then compare the potentially infinite costs in both directions.
For finite costs the actual vacuum and the outer product identity put the relative polynomial core in the adjoint domain of its slice, exactly the density needed in the normal-summand argument.
On common words one can replace all coefficients by bounded old or new approximants: the undifferentiated factors converge strongly on both coarse legs and the differentiated distinguished letters are fixed.
The two normal full slices therefore agree up to the factor \(1/\alpha_n\) on a weakly dense algebra, proving the exact equality of norms without a norm-density assumption on the coefficients.

The new corrected global costs are at least \(\delta\,2^{-n}a_{B_n}/\|\xi^{B_n}\|_{2,\tau_{B_n}}\), which diverges.
The normal bare-dual criterion rules out every bare witness in this orientation.
Conversely the proposed estimate at the whole spectrum in both orientations gives a strong system by the normal comparison.
At a Möbius base, relabelling leaves the algebra free from the original Haar unitary and preserves the coupled unitary with its parameter composed with the Borel inverse.
The Möbius equivalence thus excludes amplified costs for a forward relabelling; for the opposite orientation conjugating the relabelled adjoint pair back gives this same class and preserves actuality and strong duality.
The proof does not establish that a tuple with unbounded corner ratios exists.
The direct dependencies were inspected at the interfaces below; the review does not reprove their upstream chains or decide F0011.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0304_v1.md#decision-candidate) | Fixed decision identifying the exact reviewed statement, argument and dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0304_v1.md#statement) | All hypotheses, strong proximity, conditional separation, universal equivalence, and both Möbius orientations. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0304_v1.md#argument) | Complete disjointization, gluing of the scalar and nonmarginal vacua, corner comparison and logical consequences. |
| [Finding](#finding) | [Relative corners](../../claims/Yin_C_F0301_v1.md#statement) | Normalized relative vacuum, disjoint energy, cutoff identity, and uniform relative Gaussian bound. |
| [Finding](#finding) | [Normal cutoffs](../../claims/Yin_C_F0282_v1.md#statement) | Normality and uniform threefold operator bound for a finite single-input cost. |
| [Finding](#finding) | [Scalar geometric criterion](../../claims/Yin_C_F0255_v1.md#statement) | Both directions of absolute comparison of the scalar squared norm with maximal density and curvature. |
| [Finding](#finding) | [Scalar weight](../../claims/Yin_C_F0267_v1.md#statement) | Integrable weight dominating the full scalar right slice on complex weighted inputs. |
| [Finding](#finding) | [Vacuum recovery](../../claims/Yin_C_F0238_v1.md#statement) | Inverse conjugate gap, weak scalar soft limit, and separated multiplier identity underlying the cutoff. |
| [Finding](#finding) | [Liberation invariance](../../claims/Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Bounded Borel marginal words, graph approximation, and invariance at unchanged coordinates. |
| [Finding](#finding) | [Normal extension](../../claims/Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Elimination of the singular summand for a bounded slice with dense Hilbert adjoint. |
| [Finding](#finding) | [Actual adjoint](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Adjoint identity on a weakly dense starred core from the vacuum and outer product rule. |
| [Finding](#finding) | [Normal comparison](../../claims/Yin_C_F0075_v1.md#statement) | Strong duals from both bare orientations, and adjoint stability of the strong condition. |
| [Finding](#finding) | [Bare dual criterion](../../claims/Yin_C_F0070_v1.md#statement) | Every bare full-domain witness forces boundedness of the prescribed right slice. |
| [Finding](#finding) | [Adjoint derivation](../../claims/Yin_C_F0073_v1.md#statement) | Actuality under taking all adjoints. |
| [Finding](#finding) | [Möbius equivalence](../../claims/Yin_C_F0290_v1.md#statement) | Actuality implies strong duality for arbitrary diffuse planar base and measurable disk-valued parameter. |
