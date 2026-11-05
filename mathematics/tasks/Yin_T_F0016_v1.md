---
author: Yin
---

# Almost-sure reduced determinant limits for Laurent polynomials of uniform permutations

## Contract

### Input model and free target

For every \(N\ge1\), let \(\pi_N\) be uniformly distributed on the symmetric group \(S_N\), and let \(P_N\in U(N)\) be its permutation matrix.
All dimensions are realized on one probability space.
This is one permutation matrix at each dimension, modeling one Haar unitary \(u\) in a finite von Neumann algebra with faithful normal tracial state \(\tau\).
Thus \(\tau(u^k)=0\) for every nonzero integer \(k\), and \(u^*=u^{-1}\).

Fix a nonzero scalar Laurent polynomial
\[
 p(z)=\sum_{k=a}^{b}c_k z^k\in\mathbb C[z,z^{-1}]\setminus\{0\},
 \qquad a,b\in\mathbb Z,\quad a\le b.
\]
Its coefficients and exponents do not vary with \(N\).
The notation \(\mathbb C[u,u^*]\) refers here to this single-variable Laurent algebra.
Allow arbitrary complex coefficients, repeated roots and roots of unity; no algebraicity or Diophantine hypothesis is imposed in the full question.
Put
\[
 \ell(p)=\int_{\mathbb T}\log|p(z)|\,dm_{\mathbb T}(z),
 \qquad M(p)=\exp\ell(p)=\Delta_\tau(p(u)),
\]
where \(m_{\mathbb T}\) is Haar probability measure on the unit circle.
For a nonzero Laurent polynomial this integral is finite, and its finite unit-circle zero set has Haar measure zero.
Consequently the ordinary and kernel-removed free determinants agree at this target.
The [FK--Mahler interface](../audits/literature/Den09/Yin_U001.md#mahler-measure) fixes the normalization.

### Reduced finite determinant

For \(B\in M_N(\mathbb C)\), use the [kernel-removed convention](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant)
\[
 \Delta_N^+(B)
 =\exp\!\left(\frac1N\sum_{s_i(B)>0}\log s_i(B)\right)
 =\left(\prod_{s_i(B)>0}s_i(B)\right)^{1/N},
\]
where \(s_i(B)\) are the singular values counted with multiplicity.
Delete only exact zeros, with no numerical threshold or deletion of small positive singular values.
An empty product is one and an empty sum is zero, so \(\Delta_N^+(0)=1\).
Normalize by the original dimension \(N\), not by the rank of \(B\).
For \(B=p(P_N)\), normality makes this the product of the nonzero absolute eigenvalues with the same normalization.

This is not the ordinary determinant and is not obtained by deleting only the common constant vector.
All zero singular values are omitted, including zeros arising in different permutation cycles.
The polynomial \(p\equiv0\) is excluded from the main comparison with the ordinary free target: its reduced finite determinant is identically one, whereas its ordinary free FK determinant is zero.
If both sides use the reduced convention, that zero-polynomial case is the separate trivial identity \(1=1\).

### Almost-sure limit, upper limit and coupling quantifiers

Set
\[
 \ell_N^+(p)=\log\Delta_N^+(p(P_N)).
\]
Determine the truth of both assertions
\[
 \ell_N^+(p)\longrightarrow\ell(p)\quad\text{almost surely},
 \tag{P-limit}
\]
and
\[
 \limsup_{N\to\infty}\ell_N^+(p)=\ell(p)\quad\text{almost surely}.
 \tag{P-limsup}
\]
Equivalently, these assert convergence, respectively equality of the upper limit, of \(\Delta_N^+(p(P_N))\) to \(M(p)\).
The limits run through all positive integer dimensions.

Determine each assertion under each of the following two explicit requirements.

| Coupling requirement | Quantifier |
| --- | --- |
| Arbitrary coupling across dimensions | For every fixed nonzero \(p\) and every joint law of \((\pi_N)_{N\ge1}\) with uniform marginal on \(S_N\) at each \(N\), the assertion has probability one. |
| Independence across dimensions | For every fixed nonzero \(p\), the assertion has probability one when the variables \(\pi_N\) are independent as \(N\) varies. |

The probability-one event may depend on the fixed polynomial and the chosen joint law.
Simultaneous validity for every complex-coefficient polynomial on one event is not required.
Independence across dimensions is an explicit additional assumption in the second regime, not a consequence of uniform marginals.
A Feller construction or any other specified coupling is a particular joint law and cannot replace the arbitrary-coupling requirement.
A full-limit proof implies the corresponding upper-limit equality; failure of the full limit does not by itself resolve that equality.

### Scope and completion criteria

Resolve both assertions in both coupling regimes by complete proofs or rigorous counterexamples, with applicable review against this exact contract.
Logical implications may settle several assertions using one argument.
Every counterexample must keep \(p\) fixed, specify a lawful joint distribution with uniform marginals, and prove failure with positive probability.
A counterexample asserted for the independent regime must satisfy independence across dimensions.
A negative arbitrary-coupling conclusion leaves the independent regime to be resolved unless the same example already belongs to it.

A proof restricted to roots off the unit circle, algebraic coefficients or the finite-type class is partial progress for the arbitrary-complex-coefficient question.
A deterministic sequence of cyclic permutation matrices is not the uniform random-permutation model.
The ordinary-determinant examples \(p=z-1\) and \(p=z+1\) do not refute the reduced assertions.
An upper bound alone, convergence in probability alone or a subsequential result without the stated full upper-limit conclusion is insufficient.
Expectation convergence, several independent permutation generators, and classification of every individual coupling are outside this Task's completion requirements.

## Starting evidence and resolved arithmetic gap

The [cycle-product comparison](../ledger/Yin_L_F0062_v1.md#permutation-positive-cases) supplies the cycle-count bound and the role of polynomial lower bounds for unit-circle roots.
The [reduced-determinant analysis](../ledger/Yin_L_F0062_v1.md#reduced-determinants) gives the \(p=z-1\) reduced limit and explains the positive cases with roots of unity and suitable separation for the other unit-circle roots.
Those arithmetic starting cases retain their original evidence and review scope.
The [complete classification](../claims/Yin_C_F0189_v1.md#statement) now handles the previously missing irrational roots without a polynomial separation bound, with distinct answers for full limits and upper limits under the two couplings.

The [ordinary-determinant coupling example](../ledger/Yin_L_F0062_v1.md#permutation-coupling) motivates explicit coupling quantifiers without transferring its conclusion to reduced determinants.
The [finite-quotient discussion](../ledger/Yin_L_F0062_v1.md#finite-quotient-counterexample) distinguishes group quotient chains from uniform permutations.
The [single-Haar analytic Task](Yin_T_F0010_v1.md#contract) identifies and studies the free target; it does not settle this random approximation objective.
This Task is also distinct from the [Haar matrix-pencil approximation Task](Yin_T_F0015_v1.md#contract), whose finite inputs are Haar matrices and whose determinant is ordinary.

## Current decision

[Selected decision](#decision-completed-coupling-classification)

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-11-05T05:07 |
| status | active |
| authority | Yin explicitly requested a separate Task for scalar Laurent polynomials modeled by random permutations, using the reduced determinant and specifying almost-sure convergence, upper limits and cross-dimensional coupling. |
| reason | Removing exact zero singular values gives a different approximation problem; the arbitrary-coefficient and coupling requirements must survive the known arithmetic special cases and ordinary-determinant obstructions. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Reduced permutation determinant contract](#contract) | Reduced logarithmic determinant limit and upper-limit assertions for every fixed nonzero complex Laurent polynomial, separately under arbitrary coupling and independence across dimensions, with original-dimension normalization. |

### Decision completed-coupling-classification

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:29 |
| status | completed |
| authority | Yin authorized parallel exploration and advancement of F0012 through F0016, within the unchanged completion criteria. |
| reason | The reviewed classification proves the independent-dimension upper-limit equality for every fixed nonzero Laurent polynomial, refutes full convergence by a fixed independent model, and refutes arbitrary-coupling upper-limit equality by a second fixed polynomial and a lawful coupling. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Original reduced determinant contract](#contract) | Both assertions in both coupling regimes, with exact-zero deletion and original-dimension normalization unchanged. |
| support | [Complete coupling classification](../claims/Yin_C_F0189_v1.md#statement) | Independent upper-limit equality holds universally; full-limit assertions in both regimes and the arbitrary-coupling upper-limit assertion are false by the specified fixed counterexamples. |
| review | [Independent whole-contract finding](../audits/reviews/Yin_R_F0194_v1.md#finding-whole-contract) | Whole original contract and complete classification argument, including source conventions, all quantifiers, probability-one events and exact marginal laws. |

## Resolution and independent full-chain follow-up

The [proved classification](../claims/Yin_C_F0189_v1.md#decision-classification-reviewed) resolves all four original assertions.
Under independent dimensions the upper-limit equality is true for every fixed nonzero Laurent polynomial.
The full limit is false even with independent dimensions, and the upper-limit equality is false under arbitrary coupling.
Both counterexamples keep every finite matrix invertible, so removing exact zeros does not remove their obstruction.
The [independent post-completion audit](../audits/reviews/Yin_R_F0194_v1.md#finding-post-completion-chain) checked this actual selected contract, proved support and complete necessary dependency chain and found no unresolved gap.
