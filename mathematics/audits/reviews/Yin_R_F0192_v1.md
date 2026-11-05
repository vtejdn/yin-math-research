---
author: Yin
---

# Complex symmetric shifts: independent whole-proof review of the first candidate

The review act is dated 2026-11-05T01:01 UTC, with human record author Yin.
The fixed object is [Yin_C_F0188_v1, statement](../../claims/Yin_C_F0188_v1.md#statement) and its complete [argument](../../claims/Yin_C_F0188_v1.md#argument), as inspected in this work round.
The candidate was selected open, and this review makes no Claim or Task decision.

A separately organized reviewing agent read the fixed candidate and the original external inputs without participating in its proof development.
Before its initial findings, no drafts, proof-generation dialogue, author explanations, other agents' mathematical work, or previous verdicts were supplied or consulted.
The reviewer first checked the statement's obligations, read the complete argument, inspected the original source statements, and derived the ordering objection below independently.
After that objection was reported, the main agent described a proposed future correction; that description is not evidence for the fixed v1 input and no repaired candidate is covered here.
No previous R finding or rolling U conclusion was relied on.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#finding-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#finding-whole-proof) | [Exact statement](../../claims/Yin_C_F0188_v1.md#statement) | Finite-second-moment real off-diagonal law, arbitrary polynomially bounded deterministic complex symmetric shifts, all polynomial failure exponents, independent finite-second-moment diagonals, normalization, conditional shifts and the almost-sure consequence. |
| [Whole-proof finding](#finding-whole-proof) | [Complete argument](../../claims/Yin_C_F0188_v1.md#argument) | Entire local proof and its two original-source interfaces inspected; a failed implication in the nondegenerate probability-profile count prevents acceptance. |

<a id="finding-whole-proof"></a>
## Whole-proof finding

The fixed v1 argument is incomplete.
The transition to the reordered nondegenerate reservoir uses a high-product lower bound established for a different coordinate order, and that implication is false.
This is a gap in the proposed proof, not a counterexample to the small-singular-value assertion.
The remaining inspected steps and the accepted source interfaces are described below at their actual scopes.

### Accepted original external inputs

The inspected original is [Ngu12a, arXiv:1105.5733v1](../../literature/pdf/Ngu11--arxiv-v1.pdf), whose title page identifies Hoi H. Nguyen, *A continuous variant of the inverse Littlewood-Offord problem for quadratic forms*, with the arXiv version dated 28 May 2011.
The historical local PDF filename does not change this work identification.
Theorem 1.3 and Condition 1 were checked on printed/PDF pages 2--3; the quadratic concentration definition was checked on page 3 and Theorem 1.8 on page 5.
The relevant pages were inspected both as extracted text and as rendered originals.
The bibliography entry Ngu12a identifies this work and this selected arXiv version.

Theorem 1.3 applies to coefficients in a fixed real vector space, with squared Euclidean norms summing to one, a real scalar law satisfying Condition 1, and concentration at least a fixed inverse polynomial.
For any allowed exception count \(N'\), it gives a proper symmetric progression with
\[
 |Q|\le\max\{C\rho^{-1}/\sqrt{N'},1\}.
\]
Its real coordinate generators have the form \(\beta p_{ij}/p\), with nonzero integer \(p=O(\sqrt{N'})\) and \(|p_{ij}|=O(\beta^{-1}\sqrt{N'})\).
The paragraph following that theorem explicitly permits constants depending on the coefficient dimension and the three anti-concentration constants.
This supplies the asserted uniformity for the truncated laws once those constants are fixed.

The quadratic concentration definition includes a supremum over arbitrary vector-valued linear coefficients and centers.
Theorem 1.8 supplies the bounded list of rows, common nonzero integer multiplier, polynomially bounded integer coefficients, and linear concentration for the symmetrized selector law used by the candidate.
The coefficient dimension two is permitted, so identifying a complex number with its real and imaginary coordinates does not change either theorem's domain.
The scalar variables remain real; no complex Wigner or Hermitian extension of the source theorem is needed.
The original proofs of Theorems 1.3 and 1.8 are accepted external inputs at statement and applicability level and were not independently re-audited.
No concrete objection to those source interfaces was found.
The published Ngu12 real-shift result and any personal-communication extension are not premises of this checked argument.

### Truncation and the structural vector

Finite variance gives the stated discarded probability \(O(n^{2-2K})\).
Conditioning all independent off-diagonal entries to be bounded preserves their independence and common truncated law.
Total-variation convergence to the nondegenerate original law gives a single anti-concentration window for all sufficiently large \(n\).
For the selector-symmetrized law, the positive mass at zero together with positive mass in that window gives another uniform anti-concentration window for its independent difference.
No centering or variance normalization of the truncated law is used by the source theorems.
Fixed multiplicative entry bounds can be accommodated by the available integer exponent margin.

For the large modified-row case, normalizing a row of norm at least \(n^{-a}\) enlarges the quadratic-inverse radius by at most \(n^a\).
The linear inverse theorem can therefore be applied at a deterministic radius \(n^{-a+C}\), with integer \(C\) independent of \(a\).
This choice makes its rational generator grid independent of the possibly irrational row norm.
Rounding the exceptional coordinates on the same polynomial grid preserves the rational-height bound.
The resulting Euclidean approximation error is negligible for the norm bounds once \(a\) is large.

For the small modified-row case, a column of the Frobenius-normalized adjugate has norm at least \(m^{-1/2}\).
The good-index relations express its coordinates within polynomially amplified \(n^{-a}\) error as integer combinations of a bounded set of selected column entries divided by the same nonzero integer \(k\).
Keeping the selected indices among the exceptions avoids overwriting the rounded generators.
The constructed progression has a bounded number of generators and polynomially bounded coefficient boxes.
Multiplication by \(\lceil1/\|v\|\rceil\) is a nonzero integer of size \(O(\sqrt n)\), so it preserves rationality and polynomial progression bounds while putting the norm in the required interval.

For both cases, the algebraic identity
\[
 D\operatorname{adj}D=\operatorname{adj}D D=(\det D)I
\]
gives ordinary bilinear row products, using complex symmetry to pass between the row and column forms.
It does not assert Hermitian orthogonality.
Only a bounded set of row products may be nonzero before rounding, and coordinate errors cost at most a further \(n^{K+1}\) factor.
The exceptional-coordinate count, rank, progression size and leading entropy constant can all be fixed independently of \(a\).
The two explicit constructions supply the bounded coefficient boxes needed by the count in (23); the full rational grid is needed only on \(O(n^\varepsilon)\) coordinates and on a bounded number of generators.
No gap was found in this structural consequence or its initial entropy estimate.

### Deterministic diagonal exposure and the degenerate class

After conditioning the entries joining the bulk to its complement, row \(i\) leaves precisely the independent strictly upper entries with indices \(j>i\).
Thus its small-ball factor is \(\rho_{i+1}\), including when the diagonal is deterministic.
Ignoring the final bulk row and at most \(C_0\) unrequired rows gives
\[
 \prod_{i\in J}\rho_{i+1}
 \le n^{D(C_0+1)}\prod_{i=1}^{n_0}\rho_i,
\]
where the covering lower bound supplies every missing denominator.
This confirms the single extra loss for \(\rho_1\) in (26), rather than a loss on each row.
The large final coordinate and Condition 1 give a fixed concentration ceiling below one at radii \(O(n^{-1/2})\).
For example, if a scalar small-ball probability is \(r\), two independent samples in the same ball have probability \(r^2\), which is bounded above by \(1-c_3\) when the ball diameter is smaller than the anti-concentration window.
The same ceiling holds for all the tails by conditioning their other summands.

The low-product count follows from (23) and (26) for any fixed admissible order.
For the degenerate class, Theorem 1.3 with exception count \(\lfloor q/2\rfloor\) forces progression size one for all sufficiently large \(q\).
Normalization of a nonzero subset cancels when its approximation is returned to the original coefficients; a zero subset is immediate.
Consequently every \(q\)-subset contains at least \(\lceil q/2\rceil\) coordinates of modulus at most \(t_*\), which implies that at most \(\lfloor q/2\rfloor\) bulk coordinates exceed \(t_*\).
Rounding those coordinates and the bulk complement gives \(\exp(O(q\log n))=\exp(o(n))\) possibilities.
The row error is at most \(3n^{-4}\), and the surviving large coordinate still gives the exponential exposure bound.
No real ordering of complex coefficient values is needed.
No gap was found in this degenerate count.

### Failed implication after the nondegenerate permutation

In v1, the low/high-product classification precedes the instruction to put a nondegenerate \(q\)-subset at the end of the bulk.
After that permutation, the candidate asserts
\[
 \pi_{\beta_0}(u)=\prod_{i=1}^{p}\rho_i(u,\beta_0)\ge n^{-C_1n}
\]
from the earlier high-product classification.
The tail concentrations and their product depend on the coordinate order, so that assertion does not follow.
The following example shows the failure within the coefficient class actually being counted.

Let \(\xi\) equal zero with probability \(1/2\) and have the uniform law on \([-\sqrt6,\sqrt6]\) with probability \(1/2\).
It is bounded, centered and has variance one, so for sufficiently large \(n\) truncation leaves it unchanged.
Set \(q=\lceil n^{1-\varepsilon}\rceil\), \(h=\lceil\sqrt q\rceil\), and in the original order take
\[
 u=(\underbrace{h^{-1},\ldots,h^{-1}}_{q\text{ coordinates}},
       \underbrace{0,\ldots,0}_{n-q-1\text{ coordinates}},1).
\]
Its norm lies between one and \(\sqrt2\), its coordinates are rational of polynomial height, and every coordinate lies in the rank-one progression \(\{k/h:|k|\le h\}\) of polynomial size.
The largest coordinate is already last, and the whole set can be the bulk.

Write \(\beta_0=n^{-s}\), with \(s\) fixed independently of \(n\).
For the first \(q\) original tails, a support-interval covering of length \(O(\sqrt q)\) gives \(\rho_i(u,\beta_0)\ge n^{-(s+1)}\) for large \(n\).
For every later tail, the zero atom of the final summand gives \(\rho_i(u,\beta_0)\ge1/2\).
Therefore the original product satisfies
\[
 \prod_{i=1}^n\rho_i(u,\beta_0)
 \ge n^{-(s+1)q}2^{-(n-q)}
 =n^{-o(n)},
\]
so it exceeds \(n^{-C_1n}\) for any fixed positive \(C_1\), eventually.

For the subset consisting of the first \(q\) coordinates, let \(V=h^{-1}\sum_{j=1}^q\xi_j\).
Its all-zero-selector atom has probability \(2^{-q}\).
Conditional on any selector pattern with a continuous summand, the density of that summand is at most \(h/(2\sqrt6)\), and convolution cannot increase this density bound.
It follows that
\[
 \sup_z\mathbb P\{|V-z|\le t\}\le2^{-q}+Cht.
\]
At \(t=t_*=n^{-K-5}\), this is smaller than \(q^{-1/2+\kappa}\) for all large \(n\), so the vector is nondegenerate by the candidate's definition.
Its prescribed reservoir can consist of these \(q\) coordinates together with the final large coordinate.

After moving this reservoir to the end, the first \(p=n-q-1\) coordinates are zero.
Every one of those prefix tails contains the same complete reservoir, and convolution with the final scalar variable gives
\[
 \rho_i(u,\beta_0)\le2^{-q}+Chn^{-s}
       =n^{-s+(1-\varepsilon)/2+o(1)},\qquad i\le p.
\]
Hence the reordered prefix product is at most
\[
 n^{-[s-(1-\varepsilon)/2-o(1)](n-q-1)},
\]
which is below \(n^{-C_1n}\) when, for example, \(s>C_1+2\).
The proposed parameter order permits and in fact requires \(s\) much larger than \(C_1\).
This disproves the exact order-transfer implication used before (28).

Without a valid lower bound in the order used by the profile count, the pigeonhole argument does not establish a scale with (28) among the stated \(L_0+1\) choices.
The proof therefore cannot invoke (31) and its cancellation with (30) for every nondegenerate vector in its asserted remaining class.
The low-product estimate was shown to be valid for each fixed order, but v1 does not perform a new classification in the changed order.
A repair must justify the actual reordered high-product class before the multiscale argument is used.
No repair is incorporated or accepted by this finding.

### The profile computation conditional on its missing premise

Assuming the needed high-product lower bound holds in the fixed reservoir order, the remaining profile calculation was checked directly.
The selected subset gives the stated upper bound \(n^{-b_0}\), because \((1-\varepsilon)(1/2-\kappa)>b_0\).
Every tail has length at least \(q\), so the exception count \(\lfloor n^{1-2\varepsilon}\rfloor\) is within the linear inverse theorem's allowed range.
Monotonicity of tail concentrations makes the probability-bin index sets consecutive.
The number of profiles is polynomial for fixed parameters.

Normalizing a tail of norm \(\sigma\) and then returning its generators to the original scale changes
\[
 (t_\ell/\sigma)p_{ij}/p\quad\text{to}\quad t_\ell p_{ij}/p.
\]
Thus no irrational norm remains in the generator grid.
The tail norm is bounded above, the source's integer bounds are polynomial, and \(t_\ell\) is an integer power of \(n\).
The finitely many progressions and their bounded coefficient boxes therefore have only polynomially many choices.
All remaining coordinate choices cost \(\exp(o(n))\), including their locations.
The factor \(n^{-(1/2-\varepsilon)p}\prod_h r_h^{-m_h}\) in (30) follows from the source's progression-size bound.

The witness for a rounded vector must be selected from its deterministic coefficient/profile preimages, independently of the random matrix whose row events are bounded.
With that ordinary deterministic interpretation, coordinatewise error \(O(t_\ell)\) changes all random sums by at most \(O(n^{K+1}t_\ell)\).
The factor \(L=n^{K+3}\) absorbs both this change and the increased row tolerance.
Equation (26), a valid (28), and the bin endpoints then give (31), with \(n^{2\varepsilon n}\) as asserted.
Multiplication cancels the probability-bin factors, and \(p=n-o(n)\) gives the negative \(n\log n\) coefficient in (32).
Later constants may depend on \(a\) without changing that coefficient.
These checks do not supply the missing reordered high-product premise.

### Cofactors, singular matrices and endpoint consequences

For an invertible matrix, the adjugate singular-value identity gives the required large cofactor row after a union over \(n\) indices.
For a corresponding block decomposition with principal minor \(D\) and off-diagonal row \(x\), the cofactor row is
\[
 (\det D,-x^T\operatorname{adj}D).
\]
The bounds \(\|x\|^2\le n^{2K+1}\) and
\[
 |\det D|\le m^{-1}\|D\|_F\|\operatorname{adj}D\|_F
\]
verify the stated cofactor estimate, including singular \(D\).
A nonzero chosen cofactor row forces \(\operatorname{adj}D\ne0\).
The determinant expansion conditional on \(D\) gives exactly the symmetric adjugate quadratic coefficient matrix and arbitrary complex linear terms allowed by the inspected source.
The low conditional-concentration alternative costs \(n^{-b}\); the high alternative needs the structural-vector count, which is where the identified gap affects the final theorem.

The small scalar perturbation argument is valid conditional on the uniform invertible-matrix estimate.
For each realization, \(\det(M+tI)\) is monic, so its real zero set has Lebesgue measure zero.
Tonelli supplies a deterministic arbitrarily small positive \(t\) for which invertibility holds almost surely.
The singular-value Lipschitz bound transfers the event, with the factor two absorbed for \(n\ge2\).
A polynomial entry margin can be reserved before choosing the final exponent, and the uniform constants then cover the selected shift \(F+tI\).
This removes the rank restriction without a rank-boost theorem.

Conditional on bounded independent diagonal entries, their values can be absorbed into the deterministic shift uniformly.
The finite-second-moment union bound controls the discarded diagonal event at any desired polynomial rate.
The scaling identity for \(X_n/\sqrt n\) changes only the deterministic-shift and singular-value exponents.
Conditional random shifts follow from independence and the uniform deterministic estimate on the event bounding the shift.
Once that estimate is proved, summability with \(B>1\) gives the stated eventual almost-sure floor without any independence across dimensions.
These reductions introduce no higher-moment, density, or non-atomicity assumption, but they cannot replace the missing nondegenerate count.

## Outcome and limits

The full fixed v1 statement and argument were inspected, including both original external theorem interfaces and all local cases and reductions.
One substantive local gap remains: the high-product premise is lost under the nondegenerate reservoir permutation.
Accordingly this R does not support a proved assessment of Yin_C_F0188_v1 or any completion using it.
No counterexample to the theorem itself was established.
No repaired argument, other Claim, Task completion, manuscript, original source proof, or formal verification is covered by this finding.
The candidate files were not modified.
