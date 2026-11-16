---
author: Yin
---

# Review of the type I obstruction for finite-label liberation

## Finding

Review time (UTC) 2026-11-16T19:40.
I independently inspected the complete C_F0344 candidate dated 2026-11-16T19:38, its example and its seven declared dependency interfaces.
I was outside its proof development and received no development dialogue, author explanation, exploration note or previous finding on this candidate.
The classification of the nonscalar fibers, the global two-label restriction, the trace-half exclusion and the sharp example all hold.

For the lattice model, the adjoint vacuum and the product rule on the represented algebra put polynomial simple tensors in the adjoint domain, giving closability.
For the main implication only closability is assumed.
When a central projection \(z\) kills a core element on the left, it is under the two kernel projections of that element, so the two-kernel lemma annihilates its derivative after outer compression on both sides.
The resulting represented derivation on \(z\mathcal A\) therefore has the same generator prescriptions with unit \(z\).
This step requires no evaluation of an unbounded derivation at an individual nonatomic fiber.

I checked the application of the finite type I decomposition into matrix algebras over the center with the normalized matrix traces integrated against the central trace measure.
On a homogeneous piece, the finitely many constant matrix units can be approximated in trace Hilbert norm by compressed polynomials.
Pointwise subsequences and finite-dimensional closedness then prove full generation on almost every fiber, also after restricting to a positive central set.
For disjoint positive sets \(S,T\), approximation to \(1_S\) in their union uses the same sequence of polynomials on both sides.
A subsequence converges to \(I_n\) on almost every fiber of \(S\) and zero on almost every fiber of \(T\).
Thus the diagonal image contains \((I_n,0)\) almost everywhere on \(S\times T\), and surjectivity to each coordinate gives the full diagonal direct sum.
The countability of the finite word substitutions permits simultaneous evaluation of the multilinear alternating identity outside one product-null set.

For \(n\ge l\), alternation in \(n^2+1\) matrices vanishes on both matrix fibers before differentiation.
Applying the represented compressed derivation to each word substitution shows that its triangular lift satisfies the identity too.
If the kernel of projection onto the diagonal were nonzero, stability under arbitrary left \(M_n\) and right \(M_l\) multiplication would supply every rectangular matrix unit, and surjectivity would give the full upper triangular block algebra.
The \(n^2\) upper-left units and one lower-right diagonal unit violate the identity: the neighboring multipliers select the row and column of each prescribed slot, so only one permutation has a nonzero product.
The bridge crosses from the first block to the second in the allowed upper-right direction.
This argument holds also for \(l=1\) and arbitrary unequal block sizes.
The unique lift of the diagonal central idempotent therefore commutes with the triangular image.
Its upper-right entry \(K\) yields \(L_J(p)=p(s)K-Kp(t)\).

At each label \(J-K\) intertwines the two label representations, while \(K\) intertwines the two \(P\)-values.
This holds for every matrix-unit \(J\), so the two spaces of intertwiners span the rectangle.
Their intersection is zero because a joint intertwiner respects the separating central idempotent \((I_n,0)\).
The labels contribute dimension \(\sum_i r_i u_i\), and the \(P\)-space has dimension \(qv+(n-q)(l-v)\).
Subtracting the latter from \(nl\) gives exactly \(q(l-v)+(n-q)v\) in (1).
A diagonal central atom is a different case: the finite-summand formula adds one for the scalar commutant of that single matrix representation.

In a full fiber of size \(n>1\), a nonzero intersection of a label range with either eigenspace of \(P\) contains a common reducing line for all generators.
Neither eigenspace of \(P\) can be the whole fiber, and \(r_i\le a=\min(q,n-q)\).
Consequently \(\sum_i r_i^2\le an\le 2q(n-q)\), contradicting the extra one at a nonscalar central atom.
Any positive nonscalar rank profile now splits into two positive, disjoint central parts.
Equation (1) makes both inequalities equalities there, so \(q=a=n/2\) and each positive \(r_i=a\).
Exactly two labels are present.
For these complementary labels, a nonzero eigenvector of \(ePe\) in the range of \(e\), together with its image under \(P\), spans a nonzero reducing subspace of dimension at most two.
It follows that \(n=2\), with rank one for \(P\) and both labels.
Against this profile (1) requires an overlap of two labels on every other nonscalar profile and an overlap of one on every scalar profile.
This excludes a third globally nonzero label by faithfulness and the countable positive-measure profile decomposition.
In the abelian case the finite commuting generators give a finite-dimensional algebra; the finite-dimensional trace-half result then requires \(D=\mathbb C1\).

In the example, \(ab\) has diagonal entries \(e^{-it},e^{it}\).
Its real part recovers the full scalar function algebra since cosine is injective on the parameter interval.
The sign of its imaginary part separates the two diagonal coordinates almost everywhere, and \(a\) gives the missing off-diagonal matrix units.
Odd nonempty alternating words have zero matrix trace; even ones have normalized matrix trace \(\cos(kt)\) with \(k\ne0\) and hence zero integral.
The resulting orthonormal reduced words establish faithfulness of the presented sign algebra.
The assigned derivatives annihilate both square relations, and every ordered term of a cut in a nonempty reduced word has a nonempty reduced word in at least one leg.
Its double trace is therefore zero, giving the actual vacuum zero on the represented dense core.
The labels and \(P\) all have trace one half.
This checks the claimed type I realization, while the exclusion at three or more labels gives no classification of type II models.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0344_v1.md#decision-candidate) | Complete candidate dated 2026-11-16T19:38, including the example and all seven direct inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0344_v1.md#statement) | Closability hypothesis, rigidity on all nonscalar type I profiles and the common label pair, trace-half exclusion and two-label sharpness. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0344_v1.md#argument) | Central compression, almost-everywhere separation, rectangular polynomial identity, ranks, irreducibility and actual-vacuum calculation in the explicit model. |
| [Finding](#finding) | [Lattice data](../../claims/Yin_C_F0339_v1.md#statement) | Represented generators, actual adjoint vacuum and finite tracial setting. |
| [Finding](#finding) | [Central descent](../../claims/Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Compression to a central set from the original closable derivative and its two kernel projections. |
| [Finding](#finding) | [Type I structure](../../claims/Yin_C_F0216_v1.md#type-i-structure-source) | Finite homogeneous matrix parts over a measure space with faithful central trace. |
| [Finding](#finding) | [Matrix fibers](../../claims/Yin_C_F0216_v1.md#homogeneous-summands-and-matrix-fibers) | Coarse product sections and matrix-unit approximation to establish pointwise full generation. |
| [Finding](#finding) | [Triangular splitting](../../claims/Yin_C_F0216_v1.md#splitting-the-two-point-upper-triangular-representation) | Alternating identity and inner difference between separate full diagonal images, including the rectangular adaptation. |
| [Finding](#finding) | [Finite summand rank](../../claims/Yin_C_F0343_v1.md#two-spaces-of-intertwiners) | Diagonal rank identity on a nonscalar central atom with its extra scalar intertwiner. |
| [Finding](#finding) | [Trace-half abelian case](../../claims/Yin_C_F0343_v1.md#opposite-scalar-summands-at-trace-one-half) | Finite-dimensional trace-half obstruction applied to a finite abelian generated algebra. |
