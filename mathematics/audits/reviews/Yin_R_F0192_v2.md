---
author: Yin
---

# Independent whole-proof review of the complex symmetric shift estimate

## Inputs

[Exact statement](../../claims/Yin_C_F0188_v2.md#statement) is the finite-variance real Wigner estimate with deterministic complex symmetric shifts and its stated extensions.
[Complete argument](../../claims/Yin_C_F0188_v2.md#argument) is the fixed v2 proof, including both structured-vector branches, the entire counting argument, and the final extensions.
The primary external input is [Ngu12a, arXiv:1105.5733v1](../../literature/pdf/Ngu11--arxiv-v1.pdf), identified from its title page as Hoi H. Nguyen, *A continuous variant of the inverse Littlewood--Offord problem for quadratic forms*.
The inspected passages are Condition 1 and Theorem 1.3 on PDF pages 2--3, the quadratic concentration definition on page 3, and Theorem 1.8 on page 5.

## Review arrangement and scope

The review act was completed at 2026-11-05T01:09, with Yin as the human record author and a separately organized agent as the reviewer.
This was a fresh independent review of the whole fixed v2 argument by an agent outside its substantive development.
The supplied mathematical input was the fixed Claim and the designated primary source; no development draft, proof-generation dialogue, separate author explanation, previous R finding or other review conclusion was consulted.
The Claim's own provenance prose was read as part of the fixed artifact, without using its assertions about earlier work as proof evidence.
Obligations were taken from the exact statement and checked through every substantive local derivation.
The primary-source statements were checked in extracted text and rendered pages.
The original proofs of the two inverse Littlewood--Offord theorems were accepted as external inputs after statement and applicability checks; they were not re-audited.
The review does not claim formal verification, novelty verification, a review of other physical Claim versions, or completion of the broader research Task.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#finding) | [Exact statement](../../claims/Yin_C_F0188_v2.md#statement) | All stated hypotheses, uniform deterministic-shift quantifiers, small-singular-value conclusion, independent diagonal extension, normalization, conditional random-shift use and almost-sure consequence. |
| [Whole-proof finding](#finding) | [Complete argument](../../claims/Yin_C_F0188_v2.md#argument) | The complete local argument from the two identified external inverse theorems, including truncation, both structured-vector branches, every probability-counting regime, parameter order, cofactor reduction, rank removal and extensions. |

<a id="finding"></a>
## Whole-proof finding

No unresolved mathematical gap was found in the fixed v2 proof under its exact hypotheses and the explicitly accepted external inputs.
The statement is supported at its stated complex symmetric shift scope.
The following checks give the decisive interfaces behind this conclusion.

### External inputs and finite-variance truncation

The source linear theorem permits coefficients in fixed-dimensional real Euclidean space, an arbitrary positive radius, and any exception count between a fixed positive power of the coefficient count and that count.
Its progression is proper and symmetric, with size at most the maximum of a constant times the inverse concentration divided by the square root of the exception count and one.
Its generators have coordinates equal to the application radius times an integer divided by a common nonzero integer, with the stated polynomial bounds.
The source explicitly permits dependence on the fixed coefficient dimension and the three anti-concentration constants.
The quadratic concentration definition takes a supremum over arbitrary vector-valued linear coefficients, and Theorem 1.8 supplies the integer row combinations, exceptional rows and selector-symmetrized real law used in the Claim.
Thus identifying complex coefficients with real two-dimensional vectors is legitimate while retaining real scalar randomness.

Finite second moment gives the stated entrywise truncation cost by a union bound and Markov's inequality.
Conditioning on the product truncation event preserves independence and the common truncated law.
Nondegeneracy and total-variation convergence give uniform Condition 1 constants.
For the selector-symmetrized law, a nonzero difference in the original annulus paired with an independent zero-selector outcome gives uniform anti-concentration as well.
The source uses neither centering nor a prescribed variance in these applications.
Increasing the working entry-bound exponent to absorb fixed factors does not affect the required moment assumption or the order in which later parameters are chosen.

### Structured vectors and complex algebra

In the large transformed-row branch, division by a row norm at least \(n^{-a}\) changes the inverse-theorem radius from \(n^{-2a+O(1)}\) to at most \(n^{-a+O(1)}\).
The prescribed larger integer-power radius supplies rational generators independently of that possibly irrational row norm.
Rounding the exceptional coordinates separately and using \(\|D\|_{\max}\le n^K\) gives the claimed polynomial loss in each row product.
The identity \(\operatorname{adj}(D)D=(\det D)I\), together with symmetry of \(D\), makes the normalized row combination bilinearly orthogonal to every row outside its bounded support indices.
Complex conjugation is neither needed nor permissible in that identity.

In the small transformed-row branch, a column of the normalized adjugate has norm at least \(m^{-1/2}\).
The integer relations approximate its nonexceptional entries by bounded integer combinations of the selected column entries divided by the nonzero integer \(k\).
Keeping the selected indices exceptional makes the rounding construction consistent.
The resulting progression has bounded rank and polynomially bounded box lengths, and the rational lattice together with \(|k|\le n^{O(1)}\) gives the claimed rational heights.
The Euclidean approximation error is \(n^{-a+O(1)}\).
Multiplication by \(\lceil1/\|v\|\rceil=O(\sqrt n)\) preserves the polynomial bounds and places the norm between one and two for sufficiently large \(n\).
Column adjugate orthogonality leaves only one unconstrained row before approximation.
These checks establish a structural constant independent of the later precision exponent \(a\).

### Coarse counting, row exposure and degenerate vectors

The coarse entropy has an \(n\log n\) coefficient independent of \(a\): boundedly many generators and box dimensions cost polynomially many choices, while only \(O(n^\varepsilon)\) exceptional coordinates use the full precision-dependent rational grid.
The constructions supply polynomial box bounds even when their image progressions are not proper.
Adding a largest coordinate as a generator and moving the exceptional coordinates require only \(\exp(o(n))\) choices.

The support-disk covering argument supplies a polynomial lower bound for all tail concentration functions and for the rounded vectors actually used.
After conditioning on edges to the complement, exposing the bulk rows leaves the strictly upper entries independent.
Their factors are \(\rho_{i+1}\), so conversion to the full product loses \(\rho_1^{-1}\) and at most one additional inverse factor per omitted row.
This proves (26) with only a fixed polynomial loss, despite a deterministic diagonal and nonconsecutive omitted rows.
A surviving coordinate of magnitude comparable to \(n^{-1/2}\), together with Condition 1, bounds each relevant tail concentration by a fixed number below one at sufficiently small radius.

For the degenerate regime, normalize a nonzero subset before applying the linear inverse theorem and rescale afterwards.
The size bound is eventually one, so the symmetric proper progression is \(\{0\}\), and at least half the subset coefficients have modulus at most \(t_*\).
The quantifier over every \(q\)-subset therefore forces at most \(\lfloor q/2\rfloor\) large bulk coordinates.
Rounding those coordinates and the nonbulk coordinates gives \(\exp(O_K(q\log n))=\exp(o(n))\) possibilities, preserves a large coordinate, and increases the row tolerance to at most \(3n^{-4}\).
The direct exponential exposure bound then controls the union.

### Reservoir order and the multiscale profile count

The nondegenerate reservoir has concentration below \(q^{-1/2+\kappa}\); adding the largest coordinate cannot increase it.
With the specified exponents this is eventually at most \(n^{-b_0}\), uniformly for the scales up to \(t_*\).
The fixed v2 proof correctly applies the coarse low-product estimate again after each prescribed reservoir permutation.
It does not infer a lower bound for the new ordered product from the old order.
The \(\exp(o(n))\) choices of reservoir and prescribed permutation are absorbed by the negative \(n\log n\) exponent in that additional union bound.
For the remaining vectors the new full product is at least \(n^{-C_1n}\), which implies the same lower bound for its first \(p\) factors and justifies the telescoping argument for (28).

Tail concentration is nondecreasing with the initial index, hence each profile bin is one consecutive block and the number of profiles is polynomial.
Every tail used in the inverse theorem has length at least \(q\), whereas \(n'=\lfloor n^{1-2\varepsilon}\rfloor\) is within the permitted exception range for a fixed admissible theorem exponent.
The lower concentration bound, stated in the ambient size, remains a fixed polynomial bound in these tail lengths.
For a tail of norm \(\sigma\), normalization uses radius \(t_\ell/\sigma\), and rescaling the source generators cancels \(\sigma\) exactly.
The steps are therefore \(t_\ell p_{ij}/p\), with polynomially bounded integers; the integer-power mesh makes the number of progression choices polynomial.
Equation (27) ensures that the right side of (29) eventually exceeds one, so the maximum with one causes no missing case.

The exceptional positions and values contribute \(\exp(o(n))\), and the regular coordinate choices give (30).
The chosen representative witness is selected from a deterministic candidate set before any matrix event, so no conditional independence is lost.
Coordinatewise rounding changes every tail sum and every matrix row product by at most a constant times \(n^{K+1}t_\ell\).
The factor \(L=n^{K+3}\) absorbs both errors in the comparison with radius \(t_{\ell+1}\).
Combining (26), (28) and the bin upper endpoints gives (31), whose profile factors cancel those of (30).
The resulting exponent is \(-(1/2-\varepsilon)p+2\varepsilon n\), with \(p=n-o(n)\), so (32) follows for \(\varepsilon=1/100\).
The structural constants, coarse entropy coefficient and scale count are fixed before \(a\); all later precision-dependent constants enter only polynomial, exponential-in-\(n\), or \(\exp(o(n))\) factors.
There is no circular demand on \(a\).

### Cofactors, rank removal and final quantifiers

For the block form \(M=\begin{pmatrix}d&x^T\\x&D\end{pmatrix}\), the relevant adjugate row is \((\det D,-x^T\operatorname{adj}D)\).
A row expansion of \(\det D\) and Cauchy--Schwarz bound its squared norm by \(2n^{2K+1}\|\operatorname{adj}D\|_F^2\).
Together with \(\|\operatorname{adj}M\|_F\ge n^A|\det M|\), this yields (33) and a nonzero minor adjugate on the invertible small-singular-value event.
The determinant conditioned on \(D\) has exactly the allowed symmetric quadratic coefficient matrix, with the deterministic shift producing only arbitrary complex linear and constant terms.
The low conditional concentration costs \(n^{-b}\), while the complementary case is covered by the structured-vector estimate for the principal minor.
Choosing \(b>B+3\) absorbs the union over deleted indices.

For each realized matrix, \(\det(M+tI)\) is a monic polynomial and has finitely many real zeros.
Tonelli therefore supplies an arbitrarily small deterministic positive \(t\) for which the translated matrix is invertible almost surely.
The least singular value is 1-Lipschitz under this scalar perturbation, and the deterministic-shift estimate is uniform in the chosen \(t\).
The existing polynomial slack absorbs the diagonal increment, so this step covers singular matrices of every rank without an additional rank theorem.
Restoring the truncation error gives the required arbitrary polynomial failure exponent.

Conditioning on the independent diagonal and discarding its finite-second-moment tail proves the diagonal extension uniformly.
The identity \(X_n/\sqrt n+F=(X_n+\sqrt n F)/\sqrt n\) gives precisely the stated exponent changes.
For an independent random shift, the deterministic result holds conditional on that shift wherever its prescribed bound holds; in particular the joint probability of failure and the shift-bound event is at most \(Cn^{-B}\) times the probability of that event.
For a fixed sequence within the prescribed uniform polynomial bound, summability for \(B>1\) and the first Borel--Cantelli lemma give the eventual polynomial floor without any independence between matrix sizes.
These extensions introduce no higher moment, density or non-atomicity assumption and do not establish the excluded general-pencil or complex-Hermitian cases.
