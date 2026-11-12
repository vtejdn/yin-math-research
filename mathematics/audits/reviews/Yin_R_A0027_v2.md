---
author: Yin
---
# Independent review of the additive word-chain support obstruction

Review performed at 2026-11-11T18:50 UTC for Yin.
The reviewed object is the whole fixed [L_A0023 v2](../../ledger/Yin_L_A0023_v2.md), including its explicit eight-square matrix, the complete product-chain family and the multiplier-deletion comparison.
This is a new inspection of that physical version, retained in the existing review family without changing the earlier review.

## Review arrangement and inputs

A separately assigned reviewer outside substantive development read the candidate directly and reconstructed its arguments before forming this finding.
No development drafts, proof-generation discussion, author explanations or prior review findings for this candidate were supplied or consulted.
The reviewer received the fixed target, required whole-artifact scope, repository instructions and the main agent's operational metadata.
The mathematical dependencies actually read were the free-boundary and stable-shear arguments in [L_A0023 v1](../../ledger/Yin_L_A0023_v1.md), the exact enlargement identities in [L_A0008](../../ledger/Yin_L_A0008_v1.md#a-single-exact-lowering-step), the retained [Coh06 source unit](../literature/Coh06/Yin_U002.md#coh06-u002), and the full-support premise in [C_A0007 v4](../../claims/Yin_C_A0007_v4.md#statement).
The inspection used exact noncommutative block multiplication, analytic kernel equations, finite-support tree arguments and coefficient extraction.
It did not rely on numerical sampling, free-variable rank assumptions or an independent review of the original external source proofs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-candidate finding](#whole-candidate-finding) | [Whole L_A0023 v2](../../ledger/Yin_L_A0023_v2.md) | Whole fixed candidate, including its stated result, every displayed construction, complete kernels, rank corrections, support maxima, family quantifiers and source-use boundaries. |
| [Whole-candidate finding](#whole-candidate-finding) | [Mixed shear](../../ledger/Yin_L_A0023_v2.md#the-mixed-shear-before-linearization) | Equations (1)--(5), the free-boundary input, complete analytic and polynomial kernels, and nonadditivity for the word ab. |
| [Whole-candidate finding](#whole-candidate-finding) | [Eight-square construction](../../ledger/Yin_L_A0023_v2.md#an-explicit-additive-eight-square-matrix) | Equations (6)--(11), selfadjoint vertex decomposition, independently invertible auxiliary block, nullity two and maximal polynomial expected-Gram rank four. |
| [Whole-candidate finding](#whole-candidate-finding) | [Complete product-chain family](../../ledger/Yin_L_A0023_v2.md#the-complete-product-chain-family) | Equations (12)--(17) for every stated finite letter sequence, including inverse letters and redundant word representations, and the distinction between polynomial support counts and analytic support deficiency. |
| [Whole-candidate finding](#whole-candidate-finding) | [Multiplier deletion](../../ledger/Yin_L_A0023_v2.md#deleting-multipliers-and-the-return-to-the-old-support-cut) | Equations (18)--(22), the complete compression kernel, maximal and actual expected support, and both exact nullity changes. |
| [Whole-candidate finding](#whole-candidate-finding) | [Scope and continuation](../../ledger/Yin_L_A0023_v2.md#comparison-and-continuation-boundary) | Failure of this realization to meet C_A0007 v4, source attribution, stable-shear comparison and limits on the exclusion. |
| [Whole-candidate finding](#whole-candidate-finding) | [Free-boundary input](../../ledger/Yin_L_A0023_v1.md#an-additive-noncentral-boundary-matrix) | Reconstructed analytic rank and zero polynomial kernel at the exact group and trace conventions used by v2. |
| [Whole-candidate finding](#whole-candidate-finding) | [Stable-shear input](../../ledger/Yin_L_A0023_v1.md#a-support-lemma-for-additive-preserving-stable-shears) | Direct identification of the compressed matrix with this family and applicability of its edge-row obstruction; no adoption of unrelated v1 conclusions. |
| [Whole-candidate finding](#whole-candidate-finding) | [C_A0007 v4 statement](../../claims/Yin_C_A0007_v4.md#statement) | Exact additivity and full-support finite-witness premises used for the candidate's inapplicability conclusion, without a fresh review of that theorem's entire proof. |
| [Whole-candidate finding](#whole-candidate-finding) | [L_A0008 lowering identity](../../ledger/Yin_L_A0008_v1.md#a-single-exact-lowering-step) | Ordered elementary identity, independent triangular inverses and bounded nullity interface used as comparison. |
| [Whole-candidate finding](#whole-candidate-finding) | [Coh06-U002](../literature/Coh06/Yin_U002.md#coh06-u002) | Retained source statement, exact elementary identity and arbitrary-ring evaluation boundary; no new inspection of the original book or the 1940 source. |

## Whole-candidate finding

The whole candidate is mathematically supported at its stated scope.
No proof gap was found in the displayed construction, its complete finite product-chain family or the computed deletion and support-cut corrections.
The decisive checks are recorded below.

### Actual free-boundary operator and mixed shear

The equation \(A^*f=0\) makes \(f\) invariant along infinite \(a\)-orbits, so its square summability forces \(f=0\).
Consequently \(\partial=(A\ B)\) has dense range and rank one, and its two-coordinate kernel has unnormalized von Neumann dimension one.
The selfadjoint off-diagonal matrix \(T\) therefore has kernel \(\{0\}\oplus\ker\partial\), rank two and nullity one.
For polynomial vectors, partitioning their finite supports into right cosets of \(F(a,b)\) reduces \(A\eta+B\theta=0\) to a finite cycle on a free Cayley tree.
Leaf removal makes every coefficient zero, so the polynomial kernel of \(T\) vanishes in the actual group \(F(z,a,b)\).

The finite triangular inverse of \(P_c\) transports the complete kernel of \(0\oplus T\) to equation (2), with independent parameters \(f\) and \((\eta,\theta)\in\ker\partial\).
This proves both the analytic nullity two and the complete polynomial factorization by \(W_c\); it does not identify the analytic kernel with the closure of that polynomial module.
With \(s:=Aa+Bb\), multiplication gives \(Tv_c=(s,A^*c,B^*c)^{\mathsf T}\).
The resulting entries agree with equation (4), including the ordered upper-left entry \(s^*c+c^*s\), and substitution in (2) gives \(ry=0\).
For \(c=ab\), the four entries of \(W_c\) are distinct elements of \(F(a,b)\), so their pairwise quotients lie in \(H\) only on the diagonal and the expected Gram is \(I_4\).
The entry \(-A^*ab=ab-b\) has a nonzero coefficient at the mixed reduced word \(ab\), which no element of \(\mathbb CG_1+\mathbb CG_2\) can have.
Thus full expected support occurs before linearization, but the required additive realization does not.

### Exact selfadjoint enlargement and complete kernel transport

Splitting \(s=Aa+Bb\) and its adjoint gives the required selfadjoint vertex decomposition of (6).
Every other nonconstant entry of that matrix belongs individually to one vertex ring.
Its lower-right four-square block is exactly the block in (7), so the stated inverse follows by multiplication on both sides.
Its invertibility is established without the rank of the target matrix.

For the general family, nilpotence of the strictly lower triangular part of \(L\) gives a finite two-sided inverse.
The last component of \(L^{-1}\epsilon_1g_1\) is the ordered product \(g_m\cdots g_1=c\).
These two facts give
\[
\mathcal B J^{-1}\mathcal B^*
=r^*\epsilon_m^*L^{-1}\epsilon_1g_1e_0^*
 +e_0g_1^*\epsilon_1^*(L^*)^{-1}\epsilon_mr
=r^*ce_0^*+e_0c^*r.
\]
The bounded triangular congruence in (13) follows, with auxiliary rank \(2m\) and no auxiliary kernel.
Hence \(\operatorname{rk}K_m=2m+2\) and \(\nu(K_m)=2\).
Specializing to \(m=2\), \(g_1=b\), \(g_2=a\) reproduces every entry of (6) and gives rank six in size eight.

Solving the lower block equations gives precisely (15), and substituting the complete kernel of \(Y_c\) makes \(\lambda=0\).
Thus the complete analytic kernel is
\[
\left\{
(f,cf,af+\eta,bf+\theta,p_1f,\ldots,p_mf,0,\ldots,0)^{\mathsf T}:
f\in\ell^2(G),\ (\eta,\theta)\in\ker\partial
\right\}.
\]
The same finite inverse and the tree obstruction make (16) the complete polynomial generator.
Every multiplier coordinate and the terminal difference \(y_1-t_m\) vanish throughout the analytic kernel.
These \(m+1\) constant rows are independent, so the actual expected kernel projection is deficient, regardless of whether additional analytic relations occur.

### Maximal expected support and all family parameters

For the eight-square example, grouping the entries \(1,ab,a,b,b,ab\) by equality gives the four disjoint indicator columns in (10).
Their squared norms are \(1,1,2,2\), which proves the claimed rank four and positive eigenvalues.
The four constant annihilators in (11) are independent and annihilate the complete polynomial kernel, so every finite polynomial matrix in that kernel has expected Gram supported in the same rank-four constant corner.
The displayed witness attains this bound.
The boundary parameter \(\theta\) need not vanish: if it vanished on all of \(\ker\partial\), injectivity of \(A\) would make that kernel zero, contrary to its dimension one.
This verifies the stated distinction between the first three analytic annihilators in (11) and its fourth, polynomial-only annihilator.

For arbitrary \(m\), expectation groups the coordinates of (16) by actual equality of words because \(H\cap F(a,b)=\{1\}\).
The resulting disjoint indicator columns are linearly independent, so the expected-Gram rank is exactly the number \(q\) of classes.
Constant coordinate differences within a class, together with zero-coordinate rows, span the orthogonal complement of their constant corner and annihilate every polynomial witness.
Bimodularity therefore proves maximality, including for witnesses with arbitrary group-ring right coefficients.
The exact deficit \(4+2m-q\) refers to this maximal polynomial expected support; the candidate separately proves deficiency, without claiming the same exact rank, for the actual analytic expected kernel.
The bounds and all identities remain valid for \(m=1\), inverse letters, cancellations, repeated prefixes and \(c=1\), because no step requires a reduced written representative.
The count uses the actual group elements after cancellation, as stated.

### Multiplier deletion and the exact support cut

Deleting the multiplier rows and columns gives exactly (18); the intermediate product constraints are no longer present.
Writing
\[
u_1:=y_1-t_m,\qquad u_2:=y_2-ay_0,\qquad u_3:=y_3-by_0
\]
gives \(ry=Au_2+Bu_3\), so the quadratic form becomes \((u_1,u_2,u_3)^*T(u_1,u_2,u_3)\).
Together with the free coordinates \((y_0,t_1,\ldots,t_m)\), this is the finite invertible change of coordinates (19).
It proves \(\operatorname{rk}H_m=2\) and \(\nu(H_m)=m+2\), rather than preservation of the original nullity two.
The displayed \(V\) in (21) has exactly the asserted shear form, and its first row is a constant edge row.

The same change of coordinates makes the polynomial kernel precisely (22).
Its finite basis has expected-Gram support consisting of three independent directions from the \(y_0\) column, \(m-1\) intermediate state directions, and the final direction \(y_1+t_m\).
These directions are disjoint, giving rank \(m+3\), while \(y_1-t_m\) annihilates all polynomial and analytic kernel vectors.
For the finite basis matrix \(W\), the inequality \(WW^*\le\|W\|^2P_{\ker H_m}\), followed by expectation, supplies the lower support inclusion.
The analytic annihilator supplies the reverse inclusion, proving that the actual expected kernel support is exactly \(q_H\).
On this corner \(u_1=0\), so \(q_HH_mq_H=0\) and its nullity is \(m+3\).
The remaining row \(r\) has rank one because its adjoint kernel is contained in \(\ker A^*=0\).
Thus the last correction is independently one, and the total correction from \(K_m\) is \(m+1\).
For \(m=2\), the sizes and nullities are exactly \((8,2)\), \((6,4)\) and \((5,5)\).

### Source interface and conclusion limits

The C_A0007 v4 statement requires an additive selfadjoint realization and a finite kernel witness whose expected Gram has full ambient support.
The mixed shear for \(ab\) fails the first premise, and every \(K_m\) fails the second premise even after allowing arbitrary finite polynomial witnesses.
This proves the candidate's inapplicability conclusion without invoking or re-proving the external subordination theorem.

The inspected Coh06 unit identifies Section 5.8, printed page 311 of the retained 2006 edition, and checks the elementary enlargement identity at the arbitrary-ring evaluation scope.
The corresponding L_A0008 identity has the same ordered triangular factors and independent identity pivot.
The candidate correctly treats its selfadjoint chain, kernel transport and support counts as consuming calculations, rather than attributing them to Cohn's passage.
This review reuses that source inspection and makes no claim of a new original-book audit or earliest-priority verification.

The reviewed conclusion excludes the displayed product-chain family and rules out deleting its multipliers as a nullity-preserving repair.
It does not exclude other additive selfadjoint realizations, different auxiliary couplings, arbitrary congruences or other boundary methods.
It supplies no new group-wide Atiyah conclusion, no full-support existence theorem and no Task-completion finding.
