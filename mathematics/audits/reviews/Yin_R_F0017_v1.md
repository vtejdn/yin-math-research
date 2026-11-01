---
author: Yin
---

# Yin_C_F0028: Complete Review of the One-Coordinate Small-Core Criterion

<a id="one-coordinate-small-core-finding"></a>

## Actual review relationship

The reviewer received the complete new proof before review, then supplied the explicit scalar closure-inclusion chain and division-ring justification in Section 6 and checked that written mathematical passage.
The retained final-artifact finding includes that substantive explanatory contribution and is self-reviewed; the original no-prior-contribution statement and review sequence remain intact.
The original independent descriptions, dates and full checked scope are preserved as historical facts; no isolated arrangement or new review is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Retained complete finding](#one-coordinate-small-core-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Retained complete finding](#one-coordinate-small-core-finding) | [Exact statement](../../claims/Yin_C_F0028_v1.md#statement) | Full one-normal-coordinate weak/rational/actual-domain equivalence, exact reduced rational-degree rank, off-coordinate zero commutators, scalar affiliated/rational closure equality and every stated limitation, including the final precision passages. |
| [Retained complete finding](#one-coordinate-small-core-finding) | [Exact argument](../../claims/Yin_C_F0028_v1.md#2-adjoint-domains-and-absence-of-spectral-atoms) | Full one-normal-coordinate weak/rational/actual-domain equivalence, exact reduced rational-degree rank, off-coordinate zero commutators, scalar affiliated/rational closure equality and every stated limitation, including the final precision passages. |

- Date and reviewer: 2026-09-10; the reviewing agent.
- Target: [Yin_C_F0028](../../claims/Yin_C_F0028_v1.md#yin_c_f0028), complete statement and Sections 1–6.
- Author: the coordinating agent.
- Outcome: accepted under the exact stated assumptions; no mathematical or operator-domain correction is required.
- Provenance disclosure: the reviewer authored Yin20-U004 and independently reviewed Yin20-U002 during the preceding source audit, and had reviewed separate earlier small-core arguments.
  The reviewer did not author or contribute to the new Yin_C_F0028 proof before receiving its complete artifact for this review.
  The responsible Claim materials and their selected decisions own its current mathematical and review status.

## Scope and Exact Conclusion

The hypotheses are dual identities on the dense starred polynomial algebra, membership of the vacuum in each adjoint domain, and bounded commutators with all starred generators.
The review confirms that compactness, Hilbert–Schmidt membership, normalization of the vacuum value, boundedness of the duals, and an all-bounded-vectors domain inclusion are unnecessary for this particular coordinate theorem.
The coordinate \(X_j\) is normal and the tested bounded function belongs to \(W^*(X_j)\).

Under these assumptions, finite rank of the bounded representative of the single weak form for \(j\) is equivalent to a reduced scalar rational quotient with denominator nonvanishing on the whole coordinate spectrum.
It is also equivalent to the stated actual closed-domain invariance and bounded finite-rank commutators for every dual.
The off-coordinate commutators vanish.
The exact rank is the maximum reduced numerator/denominator degree, with constants treated separately.
The affiliated intersection equality is claimed and proved only for a single normal generator.

## Adjoint Domains and the Atom Exclusion

The product rule on the invariant starred core gives a bounded extension \(T_{i,a}\) of each core polynomial commutator.
With the inner product linear in its second variable, applying the vacuum adjoint functional to \(a^*q\) gives

\[
\langle a,D_{i,0}q\rangle
=\langle aD_{i,0}^*\Omega-T_{i,a^*}^*\Omega,q\rangle.
\]

Thus formula (5) has the correct order and adjoint, and genuinely proves that every core vector belongs to the adjoint domain.
Its density proves closability of the original dual.
Neither this argument nor the rest of the proof assumes that the polynomial algebra is a graph core for the adjoint.

For the closure \(D\), a graph-convergent polynomial sequence proves domain invariance under \(X_j\) and \(X_j^*\) and extends their bounded commutators to that domain.
Adjoint pairing against the full domain of \(D^*\) then gives its corresponding invariance.
Consequently the standard selfadjoint doubling on \(\operatorname{Dom}D\oplus\operatorname{Dom}D^*\) has commutator block

\[
C=\begin{pmatrix}0&-B^*\\P&0\end{pmatrix}.
\]

The upper-right entry uses the starred core commutator, not an unproved adjoint symmetry of the dual itself.
The regularization identity (6) is the exact identity in [Yin_C_F0027](../../claims/Yin_C_F0027_v1.md#yin_c_f0027).
It can be recomputed by writing \(S(1+tS^2)^{-1}\) as the sum of the two resolvents at \(\pm i/\sqrt t\) and using the bounded domain commutator in their resolvent identities.
This derivation needs invariance of \(\operatorname{Dom}S\), and does not assume invariance of \(\operatorname{Dom}S^2\).

The bounds on \(R_t\) and \(\sqrt t\,SR_t\), together with their stated strong limits, make the regularized commutator converge strongly to \(C\).
Its lower-left block is exactly \([D(1+tD^*D)^{-1},X_j]\), so (7) follows.
For an atom, \(E\Omega\) is a common eigenvector of \(X_j\) and \(X_j^*\); normality is essential here.
The corresponding rank-one operator commutes with \(X_j\).
Cyclicity of the finite-rank trace makes each regularized pairing zero, while the strong limit makes it \(\tau(E)^2\).
Faithfulness gives \(\tau(E)>0\), proving the contradiction.
No compression or action of the unbounded dual on the spectral projection is used.

## Weak Covariance and the Bounded Compression

The reviewer expanded both terms on the left of (8) using

\[
D_{j,0}X_jb=X_jD_{j,0}b+Pb,
\qquad
D_{j,0}^*X_j^*a=X_j^*D_{j,0}^*a-Pa.
\]

All terms containing a dual image cancel because \(f\) commutes with \(X_j\) and \(X_j^*\).
The remaining pairings are \(\langle Pa,fb\rangle-\langle f^*a,Pb\rangle\), which give \(Pf-fP\) with the displayed sign.
The core is invariant under the generator and its adjoint, so the substitution is permitted on every polynomial test.
No step requires \(fb\in\operatorname{Dom}D_j\) at this stage.

The bounded representative then gives the bounded operator identity (9) by density.
The space \(L^2(W^*(X_j))\) reduces the left action of the whole coordinate algebra and contains the vacuum, so compressing (9) preserves every term and does not increase rank.
Crucially, only the bounded finite-rank representative is compressed.
No assertion about a compressed closed dual or a compressed adjoint core is made or needed.

The faithful coordinate spectral model has compact support equal to \(\sigma(X_j)\).
A finite-rank operator in that model has the stated finite \(L^2\)-tensor kernel, with conjugates included in the second factor under the bilinear convention.
The kernels of \(TX_j-X_jT\) and \(Pf-fP\) are \((w-z)K(z,w)\) and \(f(w)-f(z)\), respectively.
Nonatomicity makes the diagonal null, so (10) follows as equality of Hilbert–Schmidt kernels.
This identifies a kernel of the bounded representative, not a kernel of the original dual.

## Rationality, Spectral Poles, and Zero Rank

Fubini supplies one full-measure set of column parameters where the finite separated expression and all required scalar values are defined.
There are at least \(r+1\) distinct such parameters because the measure is nonatomic.
Linear dependence of those \(L^2\) columns and multiplication by their common polynomial denominator give the displayed relation \(bf=a\) almost everywhere.
The finite union of the exceptional null sets and the finite set of selected points remains null.
Evaluation of the explicit polynomial \(b\) at one selected point with nonzero coefficient proves that \(b\) is nonzero; it does not evaluate an almost-everywhere identity at that point.
The resulting numerator and denominator degrees are at most \(r\).

A reduced denominator zero at a support point is a genuine pole because the reduced numerator does not vanish there.
An arbitrarily small punctured neighborhood has positive measure by support and nonatomicity.
The pole therefore contradicts the essential boundedness of \(f\).
This proves nonvanishing on the entire spectrum, after which compactness supplies a bounded inverse.
The zero function and other constants require no degree convention for the zero polynomial.
If the compressed rank is zero, applying \(Pf=fP\) to the vacuum already makes \(f\) scalar in the coordinate algebra.

These arguments reproduce the needed portion of [Yin_C_F0004](../../claims/Yin_C_F0004_v1.md#yin_c_f0004) after proving its new weak-form interface.
They do not reuse that older statement's assumption that the dual itself is bounded.

## Actual Domains, All Coordinates, and Exact Rank

The bounded starred commutators and the proved closability meet exactly the hypotheses of Yin_C_F0027's bounded inverse calculus.
The scalar denominator in condition 2 is already invertible in \(M\), so that calculus proves actual closed-domain invariance before the inverse commutator rule is used.
Formula (11) has the correct noncommutative order and follows from the product rule and the closed-domain inverse identity.
Each polynomial commutator is finite rank; for \(i\ne j\) both polynomial commutators are zero.
Pairing this actual commutator against polynomial tests proves condition 4.
Together with the trivial implication from all weak forms to the single \(j\)-form, this closes the four-way equivalence without inferring domain invariance from weak tests alone.

Every rank-one term in the \(j\)-commutator has output vector in \(L^2(W^*(X_j))\), and its input functional is represented by a vector in the same space.
Multiplication by the bounded scalar rational factors preserves both properties.
The actual commutator therefore equals its two-sided coordinate compression.
Its equality with the originally given weak representative follows from boundedness and density of the tests, establishing equality of the full and compressed ranks.

The finite-column argument bounds the reduced degrees by this common rank.
Two reduced quotients equal almost everywhere are the same rational function because a nonzero polynomial has only finitely many zeros and the measure is nonatomic.
For the opposite rank bound, the polynomial divided numerator has degree at most \(n-1\) in \(z\), where \(n\) is the maximum reduced degree.
Division by the two denominators gives at most \(n\) separated bounded factors on the compact spectrum.
These are legitimate \(L^2\) factors of the already identified kernel, proving the upper rank bound.
Polynomial functions, proper quotients, quotients with polynomial parts, and constants are all covered with the stated conventions.

## Single-Generator Closure Equality and Dependencies

For \(d=1\), nonatomicity makes each nonzero polynomial injective and invertible in the affiliated algebra.
Scalar rational evaluation is injective by the same finite-zero argument and has image a division subring.
That image equals the affiliated division closure: it is inverse closed and contains the polynomials, while each of its fractions is obtained by an allowed affiliated scalar inverse.
The pole argument places every bounded member of the image in the bounded scalar division closure.

For clarity, the remaining inclusion chain implicit in Section 6 is

\[
\operatorname{Div}_M\mathbb C[X]
\subseteq\operatorname{Rat}_M\mathbb C[X]
\subseteq\operatorname{Rat}_{U(M)}\mathbb C[X]\cap M
=\mathcal F_X\cap M.
\]

The equality at the last step is the division-ring case of Yin20-U004 applied in the affiliated ambient, since its division closure is the just-identified scalar field image.
This chain and the reverse inclusion from scalar pole cancellation prove (4).
At the author's request, the reviewer added this explicit chain and its division-ring justification to Section 6 of the target, and changed the column-relation wording to allow coefficients that are not all zero, rather than calling the individual coefficients nonzero.
Both are precision edits to an already valid argument.
The resulting passages were verified after these edits; the remainder of the mathematical target was unchanged.

The dependency texts read for this review were the complete Yin_C_F0027 module, its complete review, and Yin_C_F0004 with its exact-rank refinement and the corresponding dated reviews.
The closed-operator, spectral, and scalar rational arguments above were also checked directly at the exact points Yin_C_F0028 uses them.
The prior Yin20 audit role gives provenance for the same-ambient algebraic interfaces; it is not represented as authorship of this new operator-domain argument.

The result does not settle the jointly dependent multivariable case, does not establish a general bounded inverse representation theorem, and does not make arbitrary bounded fraction coefficients admissible on a small core.
The proof requires bounded representatives of finite rank, not merely finite algebraic rank of unbounded forms.
Within that exact scope, no unresolved proof or domain issue remains.
This is an internal AI mathematical review, not numerical validation, proof-assistant verification, external human review, or a novelty assessment.
