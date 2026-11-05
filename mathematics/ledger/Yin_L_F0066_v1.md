---
author: Yin
---

# Finite-radius cofactor matching and large Riccati-fiber obstructions

This investigation concerns the original arbitrary-law [matrix-limsup](../tasks/Yin_T_F0013_v1.md#contract), [scalar-limsup](../tasks/Yin_T_F0014_v1.md#contract), and [Brown-convergence](../tasks/Yin_T_F0012_v3.md#contract) questions.
It retains strategic exploration developed by an assigned agent for Yin on 2026-11-05, mathematical counterexamples supplied or checked within proof development, and the responsible main agent's allocation judgment.
It is not an independent review, a novelty claim, or a solution of those full contracts.
The actual probability deductions and their assessments belong to the [fixed many-index and matching argument](../claims/Yin_C_F0194_v3.md#statement), rather than to this comparison.

## A different source of information from the earlier alternatives

The [reviewed complete Haar theorem](../claims/Yin_C_F0192_v2.md#argument) and [GOE theorem](../claims/Yin_C_F0186_v9.md#argument) use continuous-measure tube probabilities and quantitative resolvent comparison.
Their common transferable algebraic information includes the eventual-even real-symmetric nonidentity statement, but their probability inputs do not cover arbitrary atomic finite-second-moment laws.
The [existing atomic tube obstruction](Yin_L_F0061_v1.md#atomic-tube-obstruction) prevents substituting a degree-only product-measure tube estimate.
The [earlier strategy comparison](Yin_L_F0063_v1.md) already rejects the inspected positive-moment, unsupported smoothing, and coefficient-product shortcuts.

The finite-radius alternative instead examines the actual quadratic cofactor polynomial after exposing a row of the original Wigner matrix.
For a principal minor D, put A=adj D and Q=(A+A^T)/2.
Its exposed determinant has an arbitrary constant and linear part and a quadratic part -x^TQx in raw row coordinates, or -x^TQx/n for normalized Wigner inputs.
The [accepted MNV16 interval theorem](../audits/literature/MNV16/Yin_U001.md#mnv16-u001) controls a multilinear fair-sign polynomial through disjoint off-diagonal monomials above a fixed coefficient threshold.
The [complete two-copy conditioning](../claims/Yin_C_F0194_v3.md#two-copy-matching) supplies the real-law and complex-projection adaptation, including diagonal quadratic terms and the normalized factor 1/n.
Its proof is retained there without duplication here.
High spectral rank alone is not the matching hypothesis: a diagonal Q can give a constant quadratic form on Rademacher inputs.

For finite free target c, the [exact marginal criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion) requires the lower-deviation probabilities to have lower limit zero under the arbitrary-coupling contract.
A positive constant probability of a good determinant still does not suffice.
The matching estimate has a genuine finite-radius probability decay, but even a matching of size proportional to n gives only a vanishing bound such as C sqrt(log n)n^(-1/9).
An existence-only choice among n principal indices would destroy this bound under a union over the indices.
The [fixed random many-index reduction](../claims/Yin_C_F0194_v3.md#spread-and-average) addresses that loss through independent rectangular blocks and right-vector spread.
It retains the exact average probability of low-matching actual minors, rather than assuming that those minors are rare.

## Symmetric-part floors do not force many usable indices

For even n>=4 and 0<epsilon<=1, set
\[
 B_\varepsilon=\begin{pmatrix}0&1\\\varepsilon&0\end{pmatrix},
 \qquad J=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad M_\varepsilon=\operatorname{diag}(B_\varepsilon,J,\ldots,J).
\]
Then ||M_epsilon||=1, s_min(M_epsilon)=epsilon, and S=(M_epsilon+M_epsilon^T)/2 has s_min(S)>=1/2.
Every principal D_i has rank n-2 and hence nonzero rank-one adjugate.
For i in the first block, its adjugate Frobenius norm is one, whereas for every other i it is epsilon.
Since |det M_epsilon|=epsilon, the normalized determinant ratios equal epsilon at exactly two indices and equal one at every other index.
Thus a bounded norm, a uniformly invertible symmetric part, and exact corank-one principal minors do not imply a positive proportion of usable indices.
The independent random Wigner entries are not part of this deterministic example, so it is an obstruction to that proposed reduction rather than a counterexample to the Tasks.


For indices in the first block, D_i is the direct sum of one zero scalar and invertible J blocks, so its unique nonzero adjugate entry has modulus one.
For every other index, D_i contains B_epsilon, one zero scalar, and the remaining J blocks, so that entry has modulus epsilon.
These direct-sum descriptions verify all the stated adjugate norms and ranks.
The [random rectangular proof](../claims/Yin_C_F0194_v3.md#rectangles) uses independent Wigner coordinates missing from this example; it is not a consequence of the symmetric-part floor.

<a id="low-matching-structure"></a>
## The remaining low-matching structure

Fix \(A\ne0\) and \(h>0\), and make a graph with an edge \(ij\), for \(i\ne j\), when \(|Q_{ij}|\ge h\|A\|_F\).
The following structural complement retains the whole cofactor matrix, instead of using the [failed structured-row-to-kernel inference](../claims/Yin_C_F0194_v1.md#cofactor-identity).
If the threshold graph has no matching of size r, endpoints of a maximal matching form a vertex cover I with |I|<2r.
Hence Q has an approximation Q_0 consisting of its diagonal and the rows or columns meeting I, with
\[
 \|Q-Q_0\|_F\le n h\|A\|_F.
\]
For fixed r, this describes O(rn) complex coordinates rather than an arbitrary n-by-n matrix of structured entries.
The approximation's diagonal remains an essential unrestricted part.
The remaining discriminating investigation is whether the actual identities
\[
 D^TQ=S\operatorname{adj}D,
 \qquad DQD^T=(\det D)S,
 \qquad S=(D+D^T)/2
\]
exclude this diagonal-plus-few-rows-and-columns class with a sufficiently small probability.
No count or entropy gain for the actual Wigner minor is proved here.
A fine grid on O(rn) unconstrained coordinates combined with only exp(-cn) row probabilities would still fail at arbitrarily fine precision.
One must obtain additional independent constraints, a controlled inverse description, or another genuine gain.

## A large-fiber obstruction to a naive Riccati inversion

The suggestion to keep the whole Q leads, when S is invertible, to
\[
 T=DS^{-1}D^T=S-KS^{-1}K,
 \qquad K=(D-D^T)/2,
 \qquad TQ=(\det D)I.
\]
A uniform finite-to-one assertion for S to T, or even for S to Q at fixed K, is false despite fixed norm and invertibility bounds.
Here is a direct family showing this.
Let n=2q, let J=[[0,1],[-1,0]], and fix K=diag(J,...,J).
Fix alpha>1, put beta=alpha^(-1), and let t=alpha+beta.
For any real orthogonal projection P commuting with K and having fixed rank 2r, with 0<r<q, put
\[
 S=\alpha P+\beta(I-P),\qquad D=S+K.
\]
Since K^2=-I and S commutes with K,
\[
 KS^{-1}K=-S^{-1},\qquad T=S+S^{-1}=tI.
\]
The matrix S has its least singular value beta, and D is invertible because its Hermitian part S is positive definite.
A real orthonormal basis respecting the K-complex structure gives
\[
 \det D=(\alpha^2+1)^r(\beta^2+1)^{q-r},
 \qquad Q=(\det D/t)I.
\]
Thus the whole Q is also constant on this fixed-rank family.
The allowed P form the complex Grassmannian of r-dimensional subspaces of C^q, with real dimension 2r(q-r), which is of order n^2 for proportional r.
This dimension statement follows from the local graph chart, an arbitrary complex (q-r)-by-r matrix.
All displayed norm and inverse bounds depend only on alpha, and not on n.

This example rejects the proposed general small-fiber premise, rather than the actual Wigner probability problem.
Its fiber still has a large codimension inside the full real-symmetric space.
It therefore leaves open a count using independent Wigner coordinates or special structure of the original product-inverse K.
The raw Riccati identity alone supplies neither that count nor an entropy reduction.

## Source comparisons that prevent false propagation

Alt, Erdos, Kruger and Nemish, [arXiv:1706.08343v3](https://arxiv.org/pdf/1706.08343), were read beyond the earlier abstract-only comparison.
Definition 2.1 on PDF p. 4 includes the fixed-matrix-coefficient Wigner setting, and Assumptions 2.3, equations (2.9)--(2.12), on pp. 5--6 require bounded moments of every order.
Theorem 2.4 on p. 6 and Theorem 4.7 on p. 21 give spectral exclusion away from the self-consistent spectrum.
This degeneracy-tolerant exterior result does not supply the interior negative-logarithmic lower bound.
The statements and assumptions were inspected, not their full proofs; no theorem from the paper is adopted here.

The author-hosted 2023 [Kwan--Sauermann quadratic paper](https://mkwn.github.io/RQLOP.pdf), Remark 2.2 on PDF p. 10, explicitly identifies the small-ball adaptation of robust-rank inheritance as a difficulty.
Grebennikov and Kwan, [arXiv:2505.24699v1](https://arxiv.org/html/2505.24699v1), Theorems 1.1--1.2 and the concluding small-ball discussion, give bounded-Chow-rank point bounds and explicitly leave difficulties with the finite-radius analogue.
Jin, Kwan, Sauermann and Wang, [arXiv:2505.23335v1](https://arxiv.org/html/2505.23335v1), Theorem 1.11 and the introductory rank discussion, were inspected only as a point-concentration comparison.
Their point bounds are not substituted for the finite-radius interval bound.
The Meka--Nguyen--Vu interval theorem is the actual new finite-radius source input in this exploration.


## Allocation consequence and exact remaining test

Compared with the earlier comparison, the substantive change is finite-scale disjoint coefficients of the actual quadratic polynomial, followed by preservation of the whole low-matching matrix structure.
It is neither a new positive-moment bound nor independent noise manufactured by multiplying deterministic coefficients.
The [fixed probability reduction](../claims/Yin_C_F0194_v3.md#polynomial-shift-consequence) identifies the current discriminating question: find a fixed polynomial threshold and a growing matching size for which the mean probability of low-matching actual principal minors tends to zero, or supply a different bound on that complement.
The many-index loss has a separate explicit deduction; it need not be posed again as the missing estimate.
The large fibers above show why a generic finite-to-one parametrization of the Riccati map cannot supply the remaining count.
They do not exclude a count using the independent Wigner entries or the original product-inverse shift structure.
No such low-matching estimate, full nonsymmetric-shift floor, or propagation to general matrix-coefficient pencils is established in this comparison.
The responsible route may test that concrete complement without treating it as necessary for every possible proof of the original Tasks.
