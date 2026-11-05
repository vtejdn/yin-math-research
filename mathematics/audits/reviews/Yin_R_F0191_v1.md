---
author: Yin
---

# Independent review of the intermediate singular-value theorem

Review date: 2026-11-05T00:43 UTC.
Human record author: Yin.
The reviewing agent did not participate in the proof's development and received the fixed candidate, the source locator and the review assignment without development dialogue, exploratory drafts, author explanations or previous reviewer conclusions.
This is an initial independent review of the entire stated theorem and its argument.
No other review finding is used as evidence.

## Inputs

- [Exact statement](../../claims/Yin_C_F0187_v1.md#statement): the working revision inspected on the review date, with a fixed real centered variance-one off-diagonal law, arbitrary independent diagonals and arbitrary deterministic complex shifts.
- [Complete argument](../../claims/Yin_C_F0187_v1.md#argument): the finite-variance distance estimate and its application through row deletion and the negative-second-moment identity.

The local original `mathematics/literature/pdf/GNT14--arxiv-v1.pdf` identifies itself as [GNT14, arXiv:1404.7013v1](https://arxiv.org/pdf/1404.7013v1).
Its title page and printed/PDF page 30 were inspected, including a rendered view of the complete latter page.
The external input is the bounded-product convex concentration result stated there as Theorem 3.7 and Corollary 3.8.
Its original proof, attributed there to Maurey, was not re-audited.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole theorem finding](#intermediate-bound-reviewed) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole theorem finding](#intermediate-bound-reviewed) | [Statement](../../claims/Yin_C_F0187_v1.md#statement) | The full intermediate range, constants uniform in every deterministic complex shift and the diagonal laws, summable probability bound, independent random shifts and arbitrary cross-size coupling. |
| [Whole theorem finding](#intermediate-bound-reviewed) | [Argument](../../claims/Yin_C_F0187_v1.md#argument) | Entire argument, including the exact source interface, conditional truncation, complex projection, median estimate, restored row independence, interlacing and negative-second-moment calculation. |

<a id="intermediate-bound-reviewed"></a>
## Whole theorem finding

The stated theorem is supported by the complete argument at the inspected revision.
No substantive mathematical gap was found.
The checks below explain the decisive points; the external concentration theorem is accepted at the expressly limited inspection depth above.

### Bounded-product concentration and finite-variance truncation

Corollary 3.8 on GNT14 page 30 states a two-sided median tail bound \(4\exp(-h^2/4)\) for convex 1-Lipschitz functions under product measures whose coordinate supports have diameter at most one.
Rescaling coordinates of diameter at most \(2b\) gives \(4\exp(-t^2/(16b^2))\), which supplies equation (9) with dimension-free constants.
The norm of a complex orthogonal projection, restricted to real coordinate vectors, is a convex 1-Lipschitz real-valued function on the real Euclidean product space, so no complex-coordinate extension of that theorem is being assumed.

Writing \(p_n:=\mathbb P(|\xi|>n^{1/4})\), the variance normalization gives \(p_n\le n^{-1/2}\).
For \(r_n:=\lceil n^{5/8}\rceil\), the binomial estimate
\[
 \mathbb P(|J^c|\ge r_n)\le (e n p_n/r_n)^{r_n}
 \le \exp(-c n^{5/8}\log n)
\]
holds for all sufficiently large \(n\), with the zero-tail case immediate.
Conditioning on any positive-probability specified set \(J\) imposes separate coordinate events and therefore preserves product independence of its retained coordinates.
Dominated convergence for the first and second truncated moments yields \(m_n\to0\) and \(v_n\to1\).
These facts require no moment beyond the fixed finite second moment.

### Dimension loss, arbitrary complex shifts and the median

Coordinate projection can decrease codimension by at most \(|J^c|\), and adding the complex vector \(f_J+m_n\boldsymbol1\) decreases it by at most one more.
Thus \(q':=\operatorname{codim}_{\mathbb C}H'_J\ge q-|J^c|-1\ge q/2\) for \(q\ge c_0n^{3/4}\) with fixed \(c_0>0\) and sufficiently large \(n\).
Projection contracts distance, enlargement lowers distance, and the added vector absorbs both the deterministic shift and conditional mean; these facts give equation (12) in the stated direction.
No bound on the added vector's magnitude is used.

For real independent centered conditional coordinates \(y_i\), complex orthogonal projection \(Q\), and \(Z:=\|Qy\|\), the identity
\[
 \mathbb E Z^2
 =\sum_{a,b}Q_{ab}\mathbb E(y_a y_b)
 =v_n\operatorname{Tr}Q
 =v_n q'
\]
is valid because \(Q^*Q=Q\) and the conditional covariance matrix is \(v_n I\).
In particular, using real random coordinates does not replace the complex codimension by a smaller unproved quantity.
For sufficiently large \(n\), this second moment is at least \(q/3\).

If \(M\) is a median of \(Z\), integrating the concentration bound gives \(\mathbb E(Z-M)^2\le Cn^{1/2}\) and \(|\mathbb EZ-M|\le Cn^{1/4}\).
Consequently
\[
 \mathbb EZ\ge \sqrt{q/3-Cn^{1/2}},
 \qquad
 M\ge \sqrt{q/3-Cn^{1/2}}-Cn^{1/4}\ge a\sqrt q
\]
for a fixed \(a>0\) and all sufficiently large \(n\).
Choosing the lower-distance threshold below \(a\sqrt q/2\) and applying concentration again gives \(C\exp(-cq/n^{1/2})\).
This is uniform over the subspace, shift and admissible good set; combining it with the bad-set estimate proves equation (10).
The auxiliary threshold may depend on \(c_0\); in the matrix application \(c_0\) is a fixed numerical constant.

### Restored row independence and arbitrary diagonals

For each retained row \(i\), its off-diagonal entries are indexed by the independent unordered pairs containing \(i\).
After coordinate \(i\) is deleted from every other retained row, none of those pairs occurs in the projected other-row matrix.
Entries mirrored from row \(i\) had all occupied that deleted column; entries whose partner row was not retained already occurred only in row \(i\).
All remaining diagonal variables are independent of the whole off-diagonal family by hypothesis.
The projected row's random vector is therefore independent of the projected row space, even though the original rows are not independent.
The diagonal variable of row \(i\) itself has been removed and no diagonal moment or magnitude enters the estimate.

The projected ambient dimension is \(n-1\), and at most \(n-k-1\) other rows span the projected space, so its complex codimension is at least \(k:=\lfloor j/2\rfloor\).
In the stated range, \(k\ge c_0(n-1)^{3/4}\) for a fixed numerical \(c_0>0\) and sufficiently large \(n\).
Equation (10) applies after conditioning on this space, with the deterministic row of \(\sqrt n F_n\) as its unrestricted shift.
Projection cannot increase distance, so the original row distance is at least the controlled projected distance.
A union bound over the retained rows requires no independence between their distance events.

### Singular-value indexing, normalization and probability quantifiers

Positive distance of every row from the span of the others implies that \(B\) has full row rank.
The Gram-matrix Schur complement yields
\[
 ((BB^*)^{-1})_{ii}=\operatorname{dist}(B_i,H_i)^{-2},
 \qquad
 \sum_{r=1}^{n-k}s_r(B)^{-2}\le Cn/k,
\]
with the same identity for complex rows and their complex linear spans.
For decreasing singular values, the indices \(n-j,\ldots,n-k\) contribute \(j-k+1\) values no larger than \(s_{n-j}(B)\).
The proof's weaker count \(j-k\) is therefore valid, including both endpoints of the claimed range.
It gives \(s_{n-j}(B)^2\ge k(j-k)/(Cn)\), and \(k(j-k)\ge c j^2\) for the present \(j\ge2\).

The matrix \(BB^*\) is a principal submatrix of \(AA^*\), where \(A:=\sqrt n(W_n+F_n)\).
Principal-submatrix interlacing gives \(s_{n-j}(A)\ge s_{n-j}(B)\).
Dividing by \(\sqrt n\) therefore yields the required \(c j/n\), with no missing factor of \(n\).
The row and index union bounds give \(Cn^2\exp(-cn^{1/4})\), and this sequence is summable.
The first Borel--Cantelli lemma needs no independence between matrix sizes.

Uniformity means that the same constants work for each deterministic shift; it does not assert one probability-one event simultaneously for all uncountably many shifts.
For a random \(F_n\) independent of \(W_n\), conditioning on that \(F_n\) leaves the required matrix law unchanged and proves the stated conditional estimate.
Summability then gives the eventual almost-sure conclusion for any admissible cross-size coupling.
The sufficiently large threshold and final constants can be chosen to depend only on the fixed off-diagonal law, since every auxiliary codimension constant used in this application is numerical.

### Scope and source limits

The inspection verifies the external concentration statement and its applicability, and the complete local deduction from it.
It does not claim an audit of Maurey's original proof, a novelty or historical-priority search, a least-singular-value estimate, or a result for general matrix-coefficient pencils.
The contextual reference to C_F0186_v4 is not a premise of this theorem and was not consulted.
This finding supplies no Task-completion review and makes no adoption decision for the Claim or Task.
