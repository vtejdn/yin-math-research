---
author: Yin
---

# Finite-dimensional tracial free factors satisfy bounded division-closure equality — isolated current inspection

- Date and human attribution: 2026-10-22T22:40 UTC; Yin is the responsible human record author.
- Review arrangement: separate isolated independent inspection of the fixed target at the scope below.
  The inspecting agent did not develop or repair the target proof and received no author-development dialogue or earlier target verdict before the initial finding.
- Initial mathematical finding: 2026-10-22T22:26 UTC, with any later scope extension expressly distinguished below.
- Inputs and sequence: The fixed target mathematics and necessary direct dependency and source interfaces were inspected first; earlier findings and C assessment/recorded-scope material for this target were compared only after the initial inspection at the declared scope.
- Verification and limits: the mathematical derivations and necessary actual interfaces described below were checked directly.
  The new act does not repeat historical native computation, formal verification or the original reviewers' source inspections.
  Historical source-depth and access facts in the retained account remain facts of the original act, not new primary-source claims.
- Target and records: [C_F0106 fixed statement](../../claims/Yin_C_F0106_v1.md#statement) and its exact selected argument, bound below.
- Scope: Whole nine-section finite-dimensional-factor proof: faithful tracial von Neumann free product, complex structure constants, terminal-factor residual restrictions, same-factor forbidden state products, matrix diagonal homogeneous bound and bounded scalar reconstruction, including original finite-spectrum normal coordinates; excludes proper non-star subalgebras and diffuse factors.
- Starting assessment: this act assesses the fixed mathematical statement and proof; the older current assessment was not used as mathematical evidence before the initial finding.

## Current isolated finding

Whole §§1–8 finite-dimensional faithful tracial free-factor extension checked.
Real Gram–Schmidt gives selfadjoint centered complex basis; actual γ=τ(xa xb xc) may be complex, no spurious conjugation.
Rank<=2 terminal boundary formula, Pauli i-sign, selected-column restriction by factor and all residuals checked.
Minimality gives μ_(i,a)μ_(i,b)=0 before reducing physical words.
Diagonal actions within a factor are estimated jointly by Cauchy–Schwarz, orthogonal factor supports give finite C0 and linear homogeneous bound.
[C_F0105](../../claims/Yin_C_F0105_v1.md) state energy and positive scalar-pivot reconstruction apply with exact hypotheses; Lagrange spectral projections restore original finite-spectrum unstarred coordinates.
No descent to proper non-star subalgebras or diffuse factors.

The stated conclusion is supported at this exact scope and with the displayed hypotheses and conditions.
No substantive mathematical repair was made during this inspection.
The original fixed mathematical version and proof remain the inputs.

## Comparison and retained original evidence

After the initial findings, the complete original [R_F0043 account retained below](#8-coordinated-wording-correction-and-verification-record) was read and compared scope by scope.
No disagreement requiring a mathematical correction was identified.
The retained original finding keeps its original mathematical coverage, date precision, source-access limits and actual relationship.
The complete original natural account follows as historical evidence; its first-person wording, original verdict wording, source checks and correction history refer to that older act.
Its relationship is given explicitly in the combined tables below and is not upgraded by the new independent finding.
No historical day-only date is assigned an invented minute.
<a id="original-f0043-account"></a>

## Independent Review: Finite-Dimensional Free-Product Closure

- Date/reviewer: 2026-09-11, the reviewing agent, independently reviewing the complete candidate authored by another AI agent.
- Goal: [Yin_T_F0007](../../tasks/Yin_T_F0007_v1.md#yin_t_f0007).
- Target: [Yin_C_F0106_v1.md](../../claims/Yin_C_F0106_v1.md), all nine sections.
- Verdict: **passed after an explicit von Neumann free-product wording clarification; no mathematical correction required.**
  This audit assigns no Claim ID, mathematical Role or shared-index assessment.

## 1. Exact conclusion and accepted inputs

The target proves

\[
\operatorname{Div}_{L^0(\mathcal M)}A\cap\mathcal M
 =\operatorname{Div}_{\mathcal M}A,
\qquad
A=\operatorname{alg}_{\mathbb C}(1,\mathcal B_1,\ldots,\mathcal B_s),
\]

where the finitely many factors are finite-dimensional complex unital C*-algebras with faithful tracial probability states and M is their tracial **von Neumann** free product.
The full factor algebras are contained in A, so A is a star algebra.
Scalar inverses, rather than a change to matrix rational closure, occur on both sides.
No affiliated closure is presumed to be a division ring.
Neither factorality of M nor commutativity of the finite-dimensional factors is assumed.

The reviewer read the exact general finite-defect assertion of [Yin_C_F0034](../../claims/Yin_C_F0034_v1.md#yin_c_f0034), its [independent review](Yin_R_F0021_v1.md#yin_c_f0034-yin_c_f0035-fraction-tensor-review), and the precise [Miy22-U002](../literature/Miy22/Yin_U002.md#miy22-u002) finite-residual/minimal-representation interface.
The affiliation foundations and the formal-series theorem retain their existing source acceptance levels.
Normalized rank-one dual relations, maximal Delta and selfadjoint freeness of every basis letter are not substituted for the actual hypotheses of these inputs.

The complete [Yin_C_F0105 proof](../../claims/Yin_C_F0105_v1.md) and its [independent review](Yin_R_F0115_v1.md#original-f0046-account) were read as preparation.
The present target depends on the energy and finite scalar-pivot arguments in that proof, with their hypotheses re-established for the new alphabet.
It does not assert that the earlier projection statement itself already implies the finite-dimensional-factor conclusion.

The general free-product Hilbert representation and creation/annihilation/diagonal decomposition reuse the specified RX06 passages already source-checked in Yin_C_F0105 and its review: [arXiv v2](https://arxiv.org/pdf/math/0505302v2), Section 1 on PDF pp.2-3 and the upper-bound proof of Theorem 2.5 on pp.6-7.
The current author reports revisiting those passages.
This reviewer reuses that accepted source inspection and does not claim another whole-source audit.
The exact new scalar estimate is independently verified below, rather than importing an operator-space estimate without checking its scalar specialization.
No additional literature-priority or exhaustive-search conclusion is certified here.

## 2. Selfadjoint bases and complex multiplication

On the real vector space of centered selfadjoint elements of a factor, traciality makes tau(ab) real and symmetric and faithfulness makes tau(a squared) positive definite.
Real Gram-Schmidt therefore supplies a selfadjoint orthonormal basis.
Every centered element is a complex linear combination of centered selfadjoint elements, so this is also a complex basis of the centered factor.
It is not necessary that the factor be abelian.

For these basis elements, the expansion of x_b x_c has scalar coefficient delta_bc and coefficient at x_a equal to tau(x_a x_b x_c).
This is the correct coefficient because x_a is selfadjoint and the Hilbert inner product is linear in its second variable.
Taking the adjoint and cycling the tracial product gives conjugate(gamma_bc^a)=gamma_cb^a.
There is no general reality assertion.
The Pauli example in the target has x_1 x_2=i x_3, hence the indicated commutator on e_2 equals i Omega, with the stated positive sign.
This checks the concrete convention without requiring a numerical computation.

The reduced Fock words alternate **factor labels**, not merely individual basis letters.
The standard Hilbert decomposition gives their orthonormality and completeness.
Their operator products act on Omega as exactly those basis words, and adjoint reverses a word because each letter is selfadjoint.
This justifies the bilinear trace pairing used later without identifying noncommuting letters within a factor as independent variables.

The left action in target (8) follows directly from the finite factor product: when the first factor agrees, the scalar coefficient deletes that first letter and the centered coefficients replace it.
Otherwise left multiplication creates a new first letter.
This holds with arbitrary faithful central trace weights and with complex multiplication coefficients.

## 3. Finite-rank commutators and all domain hypotheses

Terminal deletion is a partial isometry: distinct initial reduced words ending in a fixed letter have distinct shortened outputs, each of norm one.
It extends boundedly to all of H, as does its actual Hilbert adjoint.

For the same factor, the commutator on Omega is delta_ab Omega.
On e_c it is gamma_bc^a Omega minus delta_ac e_b.
For different factors it vanishes on these short words.
On every word of length at least two the left multiplication and right deletion commute.
In particular, when a two-letter word permits both a first-letter cancellation and a last-letter deletion, both orders give the same scalar vacuum contribution and the same centered first-factor terms.
The length-two boundary introduces no additional defect.

The formula

\[
[R_{i,a},x_{i,b}]
=\delta_{ab}P+\sum_c\gamma^{i,a}_{bc}P x_{i,c}
 -x_{i,b}P x_{i,a}
\]

has precisely these short-word values and vanishes on longer words.
Its image is contained in the span of Omega and e_(i,b); its rank is at most two irrespective of the centered dimension of the factor.
The middle coefficient is gamma, not its conjugate, since the displayed operator acts complex linearly.
The cross-factor commutator is zero.

The Yin_C_F0034 invocation takes its domain and every adjoint-test module to be H itself.
These are dense left M-modules and all auxiliary operators and actual adjoints are everywhere bounded.
There are only finitely many basis letters.
Thus finite-rank commutators on this finite generating family imply finite-rank actual commutators for every bounded element of the affiliated scalar division closure.
This is the existing cleared-fraction implication; no undefined composition with an unbounded rational inverse enters the proof.

## 4. The cut identity and the minimal state space

For a fixed reduced polynomial word, the Leibniz expansion is over occurrences of every basis letter in the selected factor.
At a cut v=u(i,b)q, reducedness ensures that the products x_(i,c)x_q and x_u x_(i,b) are still reduced.
The vacuum trace therefore gives exactly the three terms in target (15): the delta_ab term selects w=q reversed, the gamma term selects w=q reversed followed by (i,c), and the last term selects w=q reversed followed by (i,a).
All products and coefficients have the stated order.

Restricting w to the empty word or to a word whose **terminal factor** differs from i kills both correction alternatives.
A condition merely excluding the specific terminal letter (i,a) would fail, but is not used.
The surviving delta_ab term yields exactly the coefficients beta_(u t w reversed), with t=(i,a).
This proves the selected-column identity with its correct suffix order.

For a bounded f, finite Fourier sums converge in L2.
For each fixed word w, right multiplication by the bounded x_w preserves this convergence.
The same applies to R_t e_w, which is zero or a fixed word vector.
Boundedness of R_t then gives convergence of each commutator column, without requiring norm convergence or uniform norm bounds of the Fourier sums.
On the coefficient side, insertion of the fixed suffix is injective, so the residual extraction is an l2 contraction.
Both sides therefore pass to the limit.

Every nonempty reduced suffix is captured by an allowed column, and every nonreduced suffix has zero residual in the explicitly zero-extended free-monoid series.
The empty residual contributes just f Omega.
Thus the entire residual span lies in the sum of finitely many finite-dimensional commutator ranges and one additional vector.
The accepted finite-residual theorem applies to this actual series.

In a minimal representation, finitely many reachable columns and observable rows span the state space and its dual.
Pairing these bases with mu(w) expresses every matrix entry as a fixed finite linear combination of beta_(p w q).
The insertion maps w to p w q are injective, so l2 summability of beta gives summability of every state entry and hence the full Hilbert-Schmidt state energy.
Arbitrary padded representations with invisible growing states are not used.

Minimality also turns beta_(p(i,a)(i,b)q)=0 for every p,q into the actual matrix equality mu_(i,a)mu_(i,b)=0.
This is required for **every pair within the same factor**, including distinct basis letters.
Consequently every nonreduced matrix word vanishes before its operator word is multiplied or reduced.
This validates the later homogeneous powers of V; no lower-degree correction from an internal factor product is missing.

## 5. The matrix diagonal term and the homogeneous bound

The compression T_(i,a)=Q_i x_(i,a) Q_i keeps exactly the centered replacement part of the first-factor action.
The scalar cancellation exits the Q_i subspace and is killed by the compression.
Thus x_(i,a)=L_(i,a)+L_(i,a)*+T_(i,a), and the compression has norm at most the norm of the letter.

For adjacent letters in different factors, each forbidden product in target (21) vanishes by its first-factor support.
Every nonzero term in a reduced-word expansion must therefore consist of creations followed by annihilations, with at most one diagonal factor between them.
Any other ordering contains one of the forbidden adjacent pairs.
This verifies the complete 2n+1 cut expansion, including endpoint cuts and n=0.

At a fixed length the partial creators have pairwise orthogonal ranges and are contractions.
Their row operator and the adjoint column operator are consequently contractions.
A cut without a diagonal term factors through the coefficient matrix indexed by prefix u and reversed suffix v; its Hilbert-Schmidt norm is exactly the word coefficient l2 norm.
This bounds each of the n+1 such cuts.

For a diagonal cut, the middle matrix is the sum over i,a of C_(i,a) tensor T_(i,a).
Every T_(i,a) is supported on Q_i on both sides.
The Q_i are mutually orthogonal, so the middle operator splits into factor blocks and is zero on the vacuum component.
**The different letters within a fixed factor are not asserted orthogonal.**
Instead, the target applies the triangle inequality and Cauchy-Schwarz inside that factor:

\[
\left\|\sum_a C_{i,a}\otimes T_{i,a}\right\|
\leq
\left(\sum_a\|T_{i,a}\|^2\right)^{1/2}
\left(\sum_a\|C_{i,a}\|_{\mathrm{HS}}^2\right)^{1/2}.
\]

At the fixed cut, the coefficient indices correspond uniquely to reduced words, so the second factor is at most the full word coefficient l2 norm.
Taking the maximum of the first factor over the finitely many factors gives exactly C0.
Row and column contractions preserve this bound.
Summing the n diagonal cuts and the n+1 other cuts yields the claimed n+1+n C0 estimate.
It has no hidden exponential dimension or trace-weight loss in n.
Finiteness of the alphabet and C0 is essential; no uniform bound as the faithful weights degenerate is required.

## 6. Actual bounded inverse and scalar reconstruction

The hypotheses needed from Yin_C_F0105 are now fully available: square-summable full state energy, zero state products on forbidden words, and a homogeneous operator bound with only linear word-length growth.
The reviewer checked the re-stated energy argument as well.
The finite matrix positive series Q converges because its summable traces bound its term norms.
It satisfies Q at least I and Phi(Q)=Q-I.
Unless all transition matrices vanish, c=1 minus the reciprocal of the norm of Q belongs to (0,1), and positivity gives Phi to the n of I at most c to the n times Q.
The scalar or zero element is handled by the constant case.

The entries of V to the n are genuinely reduced homogeneous sums because the forbidden state products already vanish.
Applying the new scalar bound entrywise and using the energy estimate gives the stated safe factor N and a summable geometric-times-linear norm bound.
The Neumann series therefore converges in the actual matrix operator norm and gives a two-sided inverse of I-V.
This does not require the norm of V itself to be less than one, and it does not assert boundedness of an arbitrary original affiliated linearization.

The remaining passage uses the original star algebra A.
For G=B*B at least delta I, each first scalar pivot is at least delta and is boundedly invertible.
Testing the positive form on (-a inverse b y,y) makes the Schur complement at least delta I as well.
The same bound persists down the finite recursion.
The block inverse formula has the correct noncommutative factor order.
Since the bounded scalar division closure of a star algebra is star-closed, all entries in the recursion remain in that closure; taking an adjoint of an inverse takes the inverse of the adjoint.

Thus the entries of B inverse are obtained by finitely many **bounded scalar** inverses, not by declaring the infinite series a rational expression or replacing scalar closure with matrix closure.
The scalar output g lies in the required closure.
Its truncated Neumann expressions have exactly the truncated Fourier coefficients of f.
Norm convergence on the output side and L2 convergence on Omega give g Omega=f Omega.
Faithfulness of the trace makes Omega separating for M, hence g=f.
The reverse inclusion follows from the agreement of every bounded inverse with its affiliated inverse.
Both inclusions are proved.

The additional bounded finite-rank criterion also follows: its forward implication uses the generator defect and bounded product/inverse commutator identities; its reverse implication starts directly from the selected residual columns and the reconstruction.
No normalized dual system for atomic generators is asserted.

## 7. Original-coordinate applications and limits

For a normal variable with finite spectrum, Lagrange interpolation gives each spectral projection as the stated polynomial in that variable alone.
The variable's adjoint is then the finite scalar combination of these projections with conjugated eigenvalues.
Therefore its ordinary unital polynomial algebra is already its full finite-dimensional abelian star algebra.
This proves the application's equality in the **original** polynomial variables; no additional adjoints are silently introduced.
Distinct spectral values make every displayed scalar denominator nonzero, and faithfulness gives positive weights at nonzero spectral projections.

A finite-dimensional factor may have arbitrary finite matrix blocks and arbitrary positive central trace weights.
A selfadjoint generating tuple generates its factor as an ordinary polynomial algebra: that algebra is star-closed and is a linear subspace of a finite-dimensional space, hence already closed.
This validates writing the reconstructed expressions in such original generators.
Freeness is between the factor algebras; no freeness within a matrix factor is needed.

Scalar factors can be omitted.
The empty remaining family, a single remaining factor, zero f and constant f require no additional inverse or convergence argument.
The single-factor reduced words have length at most one and are compatible with the same proof.
Central atomic summands of the free product are not excluded by any step.

The exact boundary is preserved: an arbitrary proper non-star algebra inside a matrix factor need not contain the chosen selfadjoint basis or the adjoints used in the scalar-pivot procedure.
The result does not prove descent to that algebra.
Diffuse factors do not have the finite centered orthonormal alphabet needed here, and finite generation by itself does not supply one.
Accordingly the full diffuse or non-star permanence problem in Yin_T_F0007 remains open.
The reviewed result is a sufficient family, not completion of the general goal.

## 8. Coordinated wording correction and verification record

Before acceptance, the reviewer requested that Section 1 explicitly specify the von Neumann algebra: a reduced free product of C*-algebras can otherwise mean only the C*-free product.
The author coordinated the change with root and replaced exactly

`Form their reduced tracial free product`

by

`Form their tracial von Neumann free product, namely the von Neumann closure of the reduced C*-free product in its trace representation:`

No other target bytes changed.
The reviewer reread the final artifact and checked that this exact substitution was its only change.
This clarifies the ambient algebra for L0(M) and the faithful normal tracial representation, without changing the intended mathematics.

**Final assessment:** the full finite-dimensional-factor extension passes independent mathematical review at the stated source acceptance levels.
The verification consists of the exact symbolic identities, Hilbert-space and matrix norm arguments, domain/interface checks, original-coordinate scope checks and final artifact correspondence described here.
No numerical test, proof-assistant formalization, external human review, whole-source audit or novelty certification is claimed.
The reviewer did not edit the proof or any shared index.

## Actual review arrangement

The reviewer reads the prior projection argument as a dependency and reconstructs the new factor extension.
Its requested wording specifies the intended tracial von Neumann closure rather than changing a proof inference or adding a new mathematical hypothesis.
The original record does not establish initial isolation from target-author development or prior target-review conclusions; the dependency review alone does not determine that relationship.
The original 2026-09-11 date and all mathematical and source-inspection limits remain intact.
This maintenance performs no new review or isolated-context certification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Current isolated finding](#current-isolated-finding) | independently reviewed |
| [Original finding](#8-coordinated-wording-correction-and-verification-record) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Current isolated finding](#current-isolated-finding) | [C_F0106 statement](../../claims/Yin_C_F0106_v1.md#statement) | Whole nine-section finite-dimensional-factor proof: faithful tracial von Neumann free product, complex structure constants, terminal-factor residual restrictions, same-factor forbidden state products, matrix diagonal homogeneous bound and bounded scalar reconstruction, including original finite-spectrum normal coordinates; excludes proper non-star subalgebras and diffuse factors. |
| [Current isolated finding](#current-isolated-finding) | [C_F0106 argument](../../claims/Yin_C_F0106_v1.md#4-bounded-end-deletion-and-the-finite-rank-boundary-defect) | Whole nine-section finite-dimensional-factor proof: faithful tracial von Neumann free product, complex structure constants, terminal-factor residual restrictions, same-factor forbidden state products, matrix diagonal homogeneous bound and bounded scalar reconstruction, including original finite-spectrum normal coordinates; excludes proper non-star subalgebras and diffuse factors. |
| [Original finding](#8-coordinated-wording-correction-and-verification-record) | [C_F0106 statement](../../claims/Yin_C_F0106_v1.md#statement) | Whole nine-section finite-dimensional-factor proof: faithful tracial von Neumann free product, complex structure constants, terminal-factor residual restrictions, same-factor forbidden state products, matrix diagonal homogeneous bound and bounded scalar reconstruction, including original finite-spectrum normal coordinates; excludes proper non-star subalgebras and diffuse factors. |
| [Original finding](#8-coordinated-wording-correction-and-verification-record) | [C_F0106 argument](../../claims/Yin_C_F0106_v1.md#4-bounded-end-deletion-and-the-finite-rank-boundary-defect) | Whole nine-section finite-dimensional-factor proof: faithful tracial von Neumann free product, complex structure constants, terminal-factor residual restrictions, same-factor forbidden state products, matrix diagonal homogeneous bound and bounded scalar reconstruction, including original finite-spectrum normal coordinates; excludes proper non-star subalgebras and diffuse factors. |

