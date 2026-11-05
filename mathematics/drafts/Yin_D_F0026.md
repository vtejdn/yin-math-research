---
author: Yin
---

# DoS: finite-radius matching tests and large Riccati fibers for actual Wigner cofactors

This continuing strategic investigation concerns the original arbitrary-law [matrix-limsup](../tasks/Yin_T_F0013_v1.md#contract), [scalar-limsup](../tasks/Yin_T_F0014_v1.md#contract), and [Brown convergence](../tasks/Yin_T_F0012_v3.md#contract) questions.
It develops one possible refinement of the actual nonsymmetric-shift test in [D_F0011](Yin_D_F0011.md#the-actual-nonsymmetric-shift), not a solution of those contracts or a replacement of their original hypotheses.
The algebraic deductions below are development by the assigned agent-S for Yin, with ordinary direct checking and without independent review.
The bounded source comparisons were performed on 2026-11-05.

## What the new continuous-model results transfer

The [complete Haar theorem](../claims/Yin_C_F0192_v2.md#argument) and [complete GOE theorem](../claims/Yin_C_F0186_v9.md#argument) combine finite-dimensional backward repair, continuous-measure tube bounds, quantitative Hermitization comparison, and logarithmic cutoff removal.
For the current discrete question, their common transferable content is algebraic structure and the real-symmetric eventual-even nonidentity statement.
Neither their tube probabilities nor their quantitative resolvent inputs are a theorem for arbitrary atomic finite-second-moment entries.
The [existing atomic tube counterexample](../ledger/Yin_L_F0061_v1.md#atomic-tube-obstruction) already rules out a degree-only product-measure replacement.
Thus further Gaussian or Haar subclasses provide no propagation to the original missing lower recurrence without new information about the actual discrete determinant.

For a finite free logarithm c, [the exact marginal criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion) requires the lower-deviation probabilities to have lower limit zero.
A fixed positive probability of a good determinant remains insufficient under arbitrary coupling.
The present matching proposal aims at actual lower-tail probabilities, rather than positive determinant moments or an independent-dimensions recurrence criterion.

## A finite-radius input and the actual matching quantity

Let M have real independent Wigner off-diagonal randomness and an independent polynomially bounded arbitrary complex shift, as in the [reviewed cofactor theorem](../claims/Yin_C_F0194_v1.md#statement).
Condition on one actual principal minor D and the exposed diagonal a.
Put A=adj D and Q=(A+A^T)/2, and assume A is nonzero.
The exposed determinant is a quadratic polynomial in the remaining independent real coordinates x:
\[
 \det M=a\det D-(x+f)^T A(x+g).
\]
Its quadratic part is -x^T Qx, while all linear and constant terms are allowed.
For a threshold h>0, make a graph on the exposed coordinates with an edge ij, i different from j, when
\[
 |Q_{ij}|\ge h\|A\|_F.
 \tag{Matching-threshold}
\]
The relevant rank is the size of a matching in this graph, not spectral rank of Q.
For example, a high-rank diagonal Q gives a constant quadratic form on Rademacher inputs.

Meka, Oanh Nguyen and Van Vu, [Anti-concentration for Polynomials of Independent Random Variables](https://theoryofcomputing.org/articles/v012a011/v012a011.pdf), Theory of Computing 12(11), 2016, Definition 1.5 and Theorem 1.6 on PDF p. 3, directly give a finite-interval estimate for real multilinear polynomials.
For degree two, r disjoint quadratic monomials whose coefficients have modulus at least one give a bound C sqrt(log r) r^(-1/9) for every interval of length one.
This is a checked source statement and not an audit of its proof.
Theorem 1.8 on PDF p. 4 has a separate general-distribution interface, but the following exact conditioning instead reuses the Rademacher theorem.
No statement from this source has yet been adopted as support for a completed project theorem.

## Exact two-copy conditioning for a real finite-variance law

For each exposed coordinate, sample independent copies xi_i^(0), xi_i^(1) of its original real law and an independent fair sign epsilon_i.
Set
\[
 c_i=(\xi_i^{(0)}+\xi_i^{(1)})/2,
 \qquad b_i=(\xi_i^{(0)}-\xi_i^{(1)})/2,
 \qquad x_i=c_i+b_i\varepsilon_i.
\]
Unconditionally x has exactly its original independent-coordinate law.
Nondegeneracy gives fixed b_0,p_0>0 with P(|b_i|>=b_0)>=p_0.
For a fixed matching of r edges, these edge-survival events use disjoint pairs of coordinates and are independent.
A direct binomial concentration bound therefore retains a fixed positive fraction of those edges, except with probability exp(-c r).

First retain at least half of the original matching for which one common projection, either real part or imaginary part, of Q_ij has modulus at least |Q_ij|/sqrt(2).
Condition on all the two-copy variables.
Each diagonal term x_i^2 becomes affine in epsilon_i because epsilon_i^2=1.
Each surviving projected off-diagonal coefficient has modulus at least sqrt(2) h b_0^2 ||A||_F.
After division by this scale the source theorem applies, with all lower-degree coefficients and the center unrestricted.
Consequently, for a law-dependent constant c_0>0 and sufficiently large r, the conditional cofactor event on (Matching-threshold) satisfies the development bound
\[
 \mathbb P\{|\det M|\le c_0 h\|A\|_F\mid D,a\}
 \le e^{-c r}+C\sqrt{\log r}\,r^{-1/9}.
 \tag{Matching-small-ball}
\]
The probability here includes the exact two-copy representation; the final bound concerns the original exposed row law.
The diagonal and deterministic linear terms cause no extra loss, and a det D need not be discarded.
This is currently a real-entry-law statement with arbitrary complex cofactor coefficients.
For genuinely complex off-diagonal laws, Hermitian conjugation changes the conditioned quadratic coefficients; the displayed graph based on sym adj D is not silently asserted to cover that case.

## The two missing bridges and the first tests

Even if r is proportional to n, (Matching-small-ball) is too weak for the existing union over n possible omitted indices.
The [current assembly](Yin_D_F0011.md#full-three-factor-assembly-and-the-first-remaining-unsupported-step) supplies existence of an index, rather than a positive proportion of usable indices.
Multiplying the source bound by n destroys its decay.
For the weaker determinant limsup objective, a useful first investigation is therefore a quantitative many-index or weighted-cofactor reduction for an excessively small singular value of the actual product-inverse shift.
It must justify choosing a random omitted index with nonvanishing probability of reaching the normalized determinant event; citing a near-kernel vector or incompressibility without that precise cofactor implication is insufficient.
Failure of such a reduction would leave this direct bound as a conditional minor estimate only.

There is also a structural complement that differs from the earlier structured-row-to-kernel inference.
If the threshold graph has no matching of size r, endpoints of a maximal matching form a vertex cover I with |I|<2r.
Hence Q has an approximation Q_0 consisting of its diagonal and the rows or columns meeting I, with
\[
 \|Q-Q_0\|_F\le n h\|A\|_F.
\]
For fixed r, this describes O(rn) complex coordinates rather than an arbitrary n-by-n matrix of structured entries.
The approximation's diagonal remains an essential unrestricted part.
The second discriminating investigation is whether the actual identities
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
Their point bounds are not substituted for (Matching-small-ball).
The Meka--Nguyen--Vu interval theorem is the actual new finite-radius source input in this exploration.

Compared with [L_F0063](../ledger/Yin_L_F0063_v1.md), the substantive proposed change is to exploit disjoint finite-scale off-diagonal coefficients of the actual quadratic polynomial, then preserve the entire low-matching matrix structure.
It is neither another moment bound, Gaussian smoothing, nor coefficient products treated as new independent noise.
The many-index loss and the remaining structured-minor count are unresolved, so this is an exploratory lead rather than a supported replacement for the full original routes.
The large Riccati fibers give a useful new rejection test for one possible implementation of that lead.
