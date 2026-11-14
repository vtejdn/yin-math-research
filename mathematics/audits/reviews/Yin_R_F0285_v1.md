---
author: Yin
---

# Review of single-input bounds and finite columns on the original normal tuple

## Finding

At 2026-11-14T14:37 UTC a reviewer for Yin independently checked the entire [C_F0276 v1 candidate](../../claims/Yin_C_F0276_v1.md#decision-candidate) fixed at 2026-11-14T14:34 UTC.
The reviewer received the fixed argument and review scope, without its development dialogue, exploration notes, author explanations or a prior verdict on this candidate.
The argument establishes (1)–(4) with the stated constants and dimensions, including the obstruction to a bare system on the original tuple.
The review checked the eleven declared dependencies at the interfaces below and compared the column definition and the two domain hypotheses with the [finite-column cost](../../claims/Yin_C_F0208_v1.md#statement) and [Task contract](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).

For a Hilbert adjoint test vector \(v\), the normal functional \(x\mapsto\langle E_0^*v,x1\rangle\) pulls back through the representation \(A^{**}\to M\).
It agrees on \(A\) with the pairing of \(v\) against the extended slice, hence on \(A^{**}\) with the pairing against its bidual.
The adjoint tests are dense by ACSY, so the bidual map annihilates the entire kernel of the representation.
The resulting normal extension agrees with the core and has norm \(a\) by restriction in both directions.
The central-summand step of C_F0211 needs only this singleton bound and the actual vacuum.
Pisier's Theorem 8.1 has coefficient one on each term after squaring.
For strong-star approximation in the bidual unit ball, one can apply the selfadjoint part of Kaplansky's theorem to the off-diagonal selfadjoint matrix with entries \(y,y^*\) in the two-by-two amplification and take its upper-right entries.
The bounded approximants have both products converging ultraweakly, and the output norm is weakly lower semicontinuous.
Restricting the resulting normal states on the bidual to the summand gives two positive normal functionals, each of mass at most one, with the stated \(L^1\) densities.

For an omitted polynomial \(n\), the derivation vanishes at \(n\), including the adjoint generators.
The identity \(E(nx)=nE(x)\) passes first to all \(x\), then to all \(n\in N\) by separate normality and normality of the left action on \(H\).
Thus \(x\mapsto ux\) fixes the norm and the column square and conjugates only the row density in (1).
For a bounded positive truncation \(l\), the orthogonal projection of every point in the \(L^2\)-closed convex hull of its orbit to the invariant subspace equals that of \(l\).
Uniqueness makes the minimum-norm point invariant, and the affiliated polar decomposition identifies the invariant vectors with \(L^2(N'\cap M)\).
This identifies the minimum with \(\mathbb E_C l\).
The same finite convex average applied to \(l\) and \(k_0\) incurs at most \(\|k_0-l\|_1\) of additional error, and taking the expectation incurs at most that error again.
Together with \(\|\cdot\|_1\le\|\cdot\|_2\) this proves the \(L^1\) approximation to \(k=\mathbb E_C k_0\) and preserves positivity and mass.

When \(C\) is scalar, the resulting column density is \(h+\tau(k)1\), of mass at most two.
Testing on a unit finite column bounds its squared output by \(2a^2\), while singletons give \(a\le c\) even in the extended reals.
Two distinct omitted coordinates already have scalar relative commutant, so the reduction holds for every \(d\ge3\).
The flip-adjoint derivation supplies actuality for the adjoint tuple on the same starred core.
For the original tuple, a bare system would give the unique starred derivations with operator-norm-bounded normalized slices by C_F0070, including agreement with the given actual slices on the core.
Hence \(c=\infty\) excludes every original bare system in this dimension.
The concentration theorem permits a different, possibly nonnormal omitted shift at each radius, and gives \(24c^2\le48a^2\) when \(a<\infty\).
For \(a=\infty\) the asserted integral inequality is the extended-real bound.

For \(d\ge2\) one omitted diffuse coordinate supplies a Haar unitary \(u\).
The polynomial commutator is Hilbert–Schmidt by the ACSY identity, and its restriction to \(M\) agrees with the commutator there by normality, including normality of the embedding \(M\to H\) tested against any vector of \(H\).
A nonzero Hilbert–Schmidt operator fixed under conjugation by \(L_u\) would yield a finite-dimensional invariant eigenspace of its positive square \(K^*K\), whereas \(L_u\) has no eigenvectors.
For \(b\in D'\cap M\), the mean ergodic theorem therefore makes the commutator of a sufficiently long unitary average of each bounded polynomial approximant arbitrarily small in Hilbert–Schmidt norm.
The averages stay bounded and converge to \(b\) in \(L^2\), since each conjugate preserves the \(L^2\) error.
This gives strong convergence on \(H\) by density of bounded vectors and ultraweak convergence in \(M\).
At fixed \(x\in M\), the two terms of the commutator consequently converge weakly to \(E(bx)\) and \(bE(x)\), respectively, proving equality.

In particular each \(q_R\) commutes with the slice as a left multiplier.
Applying (1) to \(q_Rx\) bounds the row term by \(R\tau(x^*x)\) through \(q_Rkq_R\le R1\), giving a finite column bound \(a\sqrt{\tau(h)+R}\) for the truncated map.
For \(s=1-q_R\), the contractions \(\|x\|\le1\) satisfy \(0\le x^*sx\le1\) and \(\tau(x^*sx)=\tau(sxx^*)\le\tau(s)\).
Truncating \(h\) at \(L\) bounds the squared remainder uniformly by \(a^2[L\tau(s)+\tau((h-L1)_+)+\tau(ks)]\).
At each fixed \(L\) the first and last terms tend to zero as \(R\to\infty\), and integrability of \(h\) makes the middle term tend to zero as \(L\to\infty\).
The maps themselves use only the cutoff of \(k\).
If the complementary slice at any fixed \(R\) also had finite column cost, the triangle inequality on each Hilbert-space column would give finite cost for their sum \(E\).
The argument leaves finiteness of the singleton bound under the sole vacuum hypothesis open.

The retained primary texts were checked at Pisier Theorem 8.1, Blackadar III.5.2.9, ACSY Theorem 3.4 and Anantharaman–Popa Theorems 2.3.1 and 7.4.9.
These established results were used at statement and applicability depth.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0276_v1.md#decision-candidate) | Entire candidate fixed at 2026-11-14T14:34 UTC. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0276_v1.md#statement) | Normal two-density domination, original and adjoint-tuple comparisons, original bare-system obstruction, concentration and uniform single-cutoff convergence. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0276_v1.md#argument) | Normal central compression, conjugation averages, both constants, commutation for relative-commutant multipliers and the uniform two-limit estimate. |
| [Finding](#finding) | [Two-state inequality](../literature/Pis12/Yin_U002.md#pis12-u002) | Unit coefficients on the two squared state terms for the bounded complex-linear map on \(C^*(X)\). |
| [Finding](#finding) | [Bidual summand](../literature/Bla06/Yin_U002.md#bla06-u002) | Normal quotient onto the tracial closure and isometric central-summand identification. |
| [Finding](#finding) | [ACSY adjoint and commutators](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Dense Hilbert adjoint tests and the Hilbert–Schmidt extension for commutators on the represented starred core. |
| [Finding](#finding) | [Compression of a bounded slice](../../claims/Yin_C_F0211_v1.md#removing-the-singular-part-of-an-optimal-state) | Vanishing on the singular summand via dense adjoint tests, using the singleton bound at that step. |
| [Finding](#finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong-star approximation via the selfadjoint matrix amplification, and bounded polynomial approximation in the tracial representation. |
| [Finding](#finding) | [Tracial densities](../literature/AP18/Yin_U003.md#ap18-u003) | The additional L1 interface gives positive \(L^1\) representatives of the compressed normal functionals, with mass equal to evaluation at the identity. |
| [Finding](#finding) | [Relative commutant and compact averaging](../../claims/Yin_C_F0202_v1.md#argument) | Trivial relative commutant of two distinct coordinates and the single diffuse-coordinate Cesàro argument at its bounded normal slice interface. |
| [Finding](#finding) | [Adjoint stability](../../claims/Yin_C_F0073_v1.md#statement) | Actual vacuum and normalized derivations on the adjoint tuple by flip and involution. |
| [Finding](#finding) | [Normal bare duals](../../claims/Yin_C_F0070_v1.md#statement) | Normalization of any original full-domain bare system gives bounded right slices agreeing on the starred core. |
| [Finding](#finding) | [Uniform concentration](../../claims/Yin_C_F0258_v1.md#statement) | Uniform omitted-shift integral with constant \(24c^2\) for finite original column cost. |
| [Finding](#finding) | [Forced normal symbols](../../claims/Yin_C_F0076_v1.md#statement) | Diffuseness of each omitted marginal and vanishing derivatives of its unstarred and starred generators. |
