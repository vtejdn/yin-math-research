---
author: Yin
---

# Independent review of phase spread after coordinate deletion

This independent whole-proof review was completed at 2026-11-13T02:23 UTC for human record author Yin.
I reviewed the fixed [C196v2 candidate](../../claims/Yin_C_F0196_v2.md#decision-phase-candidate) without participating in its development or receiving proof-generation dialogue, an author explanation, or a previous finding on v2.
I had inspected the v1 predecessor and its [v1 review](Yin_R_F0203_v1.md#whole-candidate-finding) before receiving v2; that earlier finding addresses different mathematics.
I checked the rectangular estimate used here directly against its derivation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Deleted phase spread](#deleted-phase-spread-reviewed) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Deleted phase spread](#deleted-phase-spread-reviewed) | [Statement](../../claims/Yin_C_F0196_v2.md#statement) | The guarded sparse lower bound for the real polynomial and the simultaneous deleted real Gram lower bound at one fixed nonreal parameter. |
| [Deleted phase spread](#deleted-phase-spread-reviewed) | [Argument](../../claims/Yin_C_F0196_v2.md#argument) | The four independent differences, sixteen-corner probability, full sparse covering, phase transfer and deletion estimate. |
| [Deleted phase spread](#deleted-phase-spread-reviewed) | [Rectangular estimate](../../claims/Yin_C_F0196_v1.md#affine-small-ball) | The fourth-moment row bound and its independent-row amplification applied to normalized real difference entries on the four panels. |

<a id="deleted-phase-spread-reviewed"></a>
## Whole-proof finding

The selected support and four panels are disjoint for all sufficiently large \(N\), since \(\delta<1/8\) leaves room for four sets of \(\lceil N/5\rceil\) indices.
The two symmetric locations of any fresh coordinate belong to one rectangle and its transpose; different rectangles use distinct unordered pairs.
Conditioning on the complementary entries therefore leaves four independent blocks with their original laws, even when the diagonal distributions are unrestricted.
At each duplication let \(F\) be the product of the indicators at the existing corners.
Given every coordinate except the new one to double, the doubled product has conditional expectation \((\mathbb E[F\mid\mathrm{others}])^2\); its expectation is at least \((\mathbb EF)^2\).
Induction yields the sixteenth power of the one-corner probability as a lower bound, without conditioning any rectangle on the norm guard.

I checked the alternating difference by expanding \(M^2=ABAB+2ABBA+2BAAB+4BABA\).
Any surviving walk must advance from the support through four disjoint panels in four steps; using a transposed step, waiting, or skipping a panel makes that impossible.
Reading from the input end therefore selects \(B,A,B,A\) and only the first word, with coefficient one.
Lower-degree terms cannot survive all four differences.
For each difference block, multiplying a raw difference of the two original unit-variance entries by \(1/\sqrt2\) restores unit variance and preserves a fourth-moment bound depending only on its color.
The v1 fourth-moment expansion and independent-row count thus give a lower bound by a fixed multiple of the input norm, with exponentially small failure, since each output has at least \(N/5\) rows.
Conditioning on preceding blocks on their successive good events makes the next input nonzero and independent of the next block.
The union bound for four failures and \(16t=c_0^4/2<c_0^4\) give the claimed fixed-vector estimate after taking a sixteenth root.
The [two-rectangle proof](../../claims/Yin_C_F0187_v19.md#quadratic-fixed-parameter-gap) is method attribution; its projected quadratic theorem and concentration assumptions are not used.

The net mesh depends on the parameter, the guard and the fixed-vector constants before \(\delta\) is chosen.
The logarithm of the support and net count divided by \(N\) is bounded asymptotically by \(\delta\log(e(1+2/\ell)/\delta)\), which tends to zero with \(\delta\).
Every smaller support embeds in one of cardinality \(\lfloor\delta N\rfloor\).
The two distances of at most \(\ell\) cost at most \(2L\ell\le t/2\) on the guard; no upper-tail probability for the guard is needed.
These checks yield the stated simultaneous sparse exclusion.

For every phase of a normalized near-mode, the real residual equation bounds \(|y|\|v\|\) by \(\|\operatorname{Re}r\|+(3K^2+|x|)\|u\|\), where \(u,v\) are the rotated real and imaginary parts.
Since \(\|u\|+\|v\|\ge1\), the chosen \(b\) gives the phase-independent lower bound \(d_0\) on \(\|u\|\).
Both factors of \(H\) are polynomials in \(M\) and \(H\) is real, so \(Hu=\operatorname{Re}((M-\bar zI)r)\) even though \(M\) need not be normal.
The strict inequality in the choice of \(b\) excludes compressibility of \(u/\|u\|\).
The distance to its normalized truncation is at most \(\sqrt2\) times the deleted complement norm, and a zero truncation leaves the full norm.
Finally the coefficient vectors \((\cos\theta,-\sin\theta)\) exhaust the real unit circle, giving the claimed least Gram eigenvalue separately for every admissible deletion.
All of these deductions are deterministic on the same guarded good event.

I found no unresolved gap within this statement.
The conclusion permits adaptive near-modes, phases and coordinate sets but fixes \(z\); it supplies neither a lower bound on \(\mathbb P(\Omega_K)\) nor a least-singular-value, logarithmic-potential or Brown-measure conclusion.
