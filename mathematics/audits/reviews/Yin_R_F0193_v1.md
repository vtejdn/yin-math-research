---
author: Yin
---

# Independent key-step review of complex inverse-concentration counting

## Review act and scope

The review act is dated 2026-11-05T01:04 UTC.
The human record author is Yin.
A separately assigned agent inspected the fixed [C_F0188_v1](../../claims/Yin_C_F0188_v1.md#argument), specifically its finite-variance truncation, structured-vector consequence, and uniform profile-counting sections.
The reviewer did not develop the candidate proof and received no substantive development dialogue, exploratory drafts, or previous review conclusions before forming initial findings.
Those initial findings used only the fixed candidate, its [Ngu12a source note](../literature/Ngu12a/readme.md), the original source, and applicable rules.
A specific objection concerning the order dependence of the tail-concentration product arrived after those initial findings.
The reviewer then independently checked that objection and obtained the explicit example below.
This sequence is disclosed because it changes the inspected objection context while retaining the separation from proof development.

The inspected original is arXiv:1105.5733v1, retained as [Ngu11--arxiv-v1.pdf](../../literature/pdf/Ngu11--arxiv-v1.pdf).
Condition 1 and Theorem 1.3 on PDF pp. 2--3, the quadratic concentration definition on p. 3, and Theorem 1.8 on p. 5 were read directly using extracted text and rendered page images.
The source proofs are accepted external inputs and were not re-audited.
No equivalence with another edition is asserted.
The review covers the assigned critical steps and their interfaces, rather than the entire smallest-singular-value theorem or the F0012 Task contract.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Source and structured-vector finding](#source-and-structure) | independently reviewed |
| [Profile-count finding](#profile-count) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Source and structured-vector finding](#source-and-structure) | [C_F0188_v1 hypotheses](../../claims/Yin_C_F0188_v1.md#statement) | The real scalar law, finite second moment, complex symmetric coefficient setting, and deterministic polynomial bounds used by the reviewed critical steps; this is not whole-statement acceptance. |
| [Source and structured-vector finding](#source-and-structure) | [C_F0188_v1 argument](../../claims/Yin_C_F0188_v1.md#argument) | The truncation paragraph and complete section Structured-vector consequence of quadratic concentration, with the stated external-input boundary. |
| [Profile-count finding](#profile-count) | [C_F0188_v1 argument](../../claims/Yin_C_F0188_v1.md#argument) | The complete section Uniform counting of the resulting complex vectors: its finite grids and conditional estimates are checked, but the unproved post-permutation high-product bound prevents its conclusion as written. |
| [Source and structured-vector finding](#source-and-structure) | [Ngu12a source note](../literature/Ngu12a/readme.md) | The specified arXiv v1 theorem statements, normalization and dimension-two applicability; no original-proof or other-edition audit. |

<a id="source-and-structure"></a>
## Finding: the source interfaces and structured-vector consequence are supported

Theorem 1.3 assumes normalized vector coefficients, Condition 1 for the real scalar law, and polynomially large concentration.
For a permitted exception count \(N'\), its proper symmetric progression has size at most
\[
 \max\{C\rho^{-1}(N')^{-1/2},1\},
\]
and its step coordinates are \(\beta p_{ij}/p\), where \(0<|p|\le C\sqrt{N'}\) and \(|p_{ij}|\le C\beta^{-1}\sqrt{N'}\).
The source allows constants to depend on dimension and the three anti-concentration constants.
Dimension two changes these constants without squaring the progression size bound.
Theorem 1.8 applies to symmetric vector-valued quadratic coefficients; its concentration definition allows arbitrary vector-valued linear terms.
Its conclusion supplies the polynomially bounded integer row combinations and symmetrized scalar variables used in the candidate.

Finite variance supplies the truncation union bound \(O(n^{2-2K})\).
Nondegeneracy supplies Condition 1 for the original law, and total-variation convergence preserves uniform constants for the conditioned laws.
For the symmetrized selector law, taking one independent selected variable to be zero and the other selected difference in the original annulus gives a uniform annulus probability for the difference of two copies.
No higher moment or recentering of the truncated law is needed by the inverse-theorem applications.

In the large transformed-row branch, division by a norm at least \(n^{-a}\) enlarges the radius \(n^{-2a+O(1)}\) to at most \(n^{-a+O(1)}\).
A deterministic radius \(n^{-a+C}\), with integer \(C\) fixed before \(a\), gives a rational grid independent of the possibly irrational row norm.
The progression rank and size exponents depend on the fixed concentration exponent rather than on \(a\).
The common denominator, polynomial box lengths, and separately rounded exceptional coordinates give coordinate and generator heights \(n^{a+O(1)}\).
The Euclidean and row-product approximation errors are bounded by \(\sqrt n\) and \(n^{K+1}\), respectively, times the coordinate error.
The adjugate identity gives exact bilinear orthogonality before rounding outside the bounded row set.
Symmetry identifies these products with \(Du\), without Hermitian conjugation.

In the small transformed-row branch, a column of norm at least \(m^{-1/2}\) is approximated by bounded-rank integer combinations of the selected entries divided by the nonzero integer \(k\).
Keeping those selected entries exceptional prevents overwriting them.
Rational rounding and the positive integer multiplier \(\lceil1/\|v\|\rceil=O(\sqrt n)\) give the stated norm, height, progression, and row-error bounds.
If rounding makes \(\|v\|>1\), that multiplier is one and the resulting norm is still below two for large \(n\).
Thus a single constant \(C_0\), independent of \(a\), covers the fixed polynomial losses in both branches.

<a id="profile-count"></a>
## Finding: the count has a post-permutation concentration gap

The finite-vector entropy estimate (23), support estimate (25), and deterministic-diagonal exposure estimate (26) are supported.
After removing zero generators, a bounded-rank progression of polynomial cardinality has polynomial box lengths.
It can be recentered at one of its used rational coordinates.
Its generators and this coordinate contribute only \(n^{O_a(1)}\) choices.
The bulk coordinates give the leading \(n^{C_*n}\) cost with \(C_*\) independent of \(a\); the exceptional coordinates cost \(n^{O_a(n^\varepsilon)}\).

For fixed coefficients, successive upper-row exposure leaves the random tail starting at \(i+1\) in row \(i\).
Replacing \(\prod_{i=1}^{n_0-1}\rho_{i+1}\) by \(\prod_{i=1}^{n_0}\rho_i\) loses only \(\rho_1^{-1}\), and omitted row constraints lose a bounded number of further factors.
The support lower bound turns these into a polynomial loss, uniformly over the deterministic diagonal.
A retained largest coordinate gives a fixed upper bound \(p_0<1\) at the required radius by Condition 1.
These estimates require no ordering of complex coefficient values.

The degenerate branch follows from Theorem 1.3 after normalizing each subset and then undoing its norm.
With \(N'=\lfloor q/2\rfloor\), its size bound becomes \(\max\{Cq^{-\kappa},1\}=1\), so the symmetric progression is \(\{0\}\).
Every \(q\)-subset has at most \(\lfloor q/2\rfloor\) coefficients larger than \(t_*\), which implies the same bound for the whole bulk.
The sparse net has \(\exp(O_K(q\log n))=\exp(o(n))\) elements and preserves the largest coordinate, proving the stated exponential estimate for this branch.

In the nondegenerate branch, the proof first excludes
\[
 \prod_{i=1}^{n_0}\rho_i(u,\beta_0)<n^{-C_1n}
\]
in the initial bulk order.
It then moves a selected \(q\)-reservoir to the end and asserts
\[
 \pi_{\beta_0}(u)=\prod_{i=1}^{p}\rho_i(u,\beta_0)\ge n^{-C_1n}.
\]
These last concentrations use the new order.
Dropping final factors preserves a product lower bound only when the order is unchanged.
The earlier classification therefore does not establish this assertion.

An explicit example demonstrates the failure of that inference.
Let \(\xi\) be zero with probability \(1/2\), and uniform on \([-\sqrt6,\sqrt6]\) with probability \(1/2\).
It has mean zero and variance one, is bounded, and satisfies Condition 1.
For \(q=\lceil n^{1-\varepsilon}\rceil\), take
\[
 u=(\underbrace{q^{-1},\ldots,q^{-1}}_{q\text{ entries}},
       \underbrace{0,\ldots,0}_{n-q-1\text{ entries}},1).
\]
Its norm is \(\sqrt{1+1/q}\), and its coordinates belong to a proper symmetric progression of rank two and size nine with generators \(1/q\) and \(1\).
It has no exceptional coordinates and satisfies the rational-height requirements.

Let \(\beta_0=n^{-s}\), with fixed \(s>C_1+2\).
Every initial tail sum is supported in a fixed bounded real interval, so its concentration is at least \(c\beta_0\).
After the first \(q\) positions, each tail sum is just the final variable and has concentration at least \(1/2\).
Hence
\[
 \prod_{i=1}^{n}\rho_i(u,\beta_0)
 \ge (c\beta_0)^q2^{-(n-q)}
 =\exp\{-O(n)-O_s(q\log n)\}
 >n^{-C_1n}
\]
for all sufficiently large \(n\).

The sum of the \(q\) small coordinates has an atom of mass \(2^{-q}\) at zero and a continuous part with density bounded by \(Cq\).
Conditional on at least one continuous summand, convolution cannot increase the \(Cq\) density bound of that scaled uniform summand.
Its concentration at \(t_*=n^{-K-5}\) is at most
\[
 2^{-q}+Cqt_*<q^{-1/2+\kappa}.
\]
Thus these \(q\) coordinates are a permitted nondegenerate reservoir.
Including the large coordinate and moving this reservoir to the end leaves \(p=n-q-1\) zero coordinates first.
All their tail sums have the law
\[
 S=\xi_0+q^{-1}\sum_{j=1}^{q}\xi_j.
\]
This law has an atom \(2^{-(q+1)}\) at zero and a continuous part with density at most \(Cq\).
Consequently
\[
 \pi_{\beta_0}(u)
 \le \bigl(2^{-(q+1)}+Cq\beta_0\bigr)^{n-q-1}
 <n^{-C_1n}
\]
for large \(n\).
An initially high-product vector can therefore become low-product after the allowed permutation.

Conditional on a genuine high-product lower bound in the reordered coordinates, the remaining estimates (27)--(32) are supported.
For a tail of norm \(\sigma\), the normalized generator \((t_\ell/\sigma)p_{ij}/p\) rescales exactly to \(t_\ell p_{ij}/p\).
Its numerator bound is \(C\sigma t_\ell^{-1}\sqrt{N'}\), which is polynomial because \(\sigma\le2\).
No additional irrational grid parameter survives.
The exception range is valid since the tails have length at least \(q\) and \(N'=\lfloor n^{1-2\varepsilon}\rfloor\).
The maximum with one in the progression bound is harmless because \(b_0>1/2-\varepsilon\).
The profile and exceptional-coordinate choices contribute polynomial factors and \(\exp(o(n))\).
The bounded support justifies comparison with a fixed witness at the enlarged radius.
The factors in (30) and (31) cancel, leaving coefficient \(-1/2+3\varepsilon<-1/3\) in front of \(n\log n\).

The parameter order is adequate for these conditional estimates.
The leading structural entropy exponent is fixed before \(a\).
Later \(a\)-dependent ranks and grids contribute fixed polynomial factors, \(O_a(n)\) terms, or \(o(n)\) terms.
This does not establish the missing post-permutation lower bound.
In particular, (28) needs either a valid reordered high-product premise or treatment of the complementary class before it can be used.

## Conclusion and limits

The fixed v1 structured-vector consequence and its two external-source interfaces are supported.
The uniform counting conclusion is not established as written because the post-permutation concentration classification is missing.
The example refutes that intermediate inference, rather than the smallest-singular-value theorem.
The remaining profile estimates are reusable under their actual reordered high-product premise.

No later version or repair is covered.
The cofactor reduction, rank-removal argument, random-diagonal extension, normalization, almost-sure consequence, and whole Task completion are outside this review's accepted scope.
This review changes no C material, selects no Claim assessment, and completes no Task.
