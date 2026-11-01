---
author: Yin
---

# Independent internal review: three square-zero reconstruction interface

Review completed: 2026-09-16.
Human record author: Yin.
Reviewer: separately organized Codex research subagent the reviewing agent.
Proof author: Codex research subagent another AI agent.

Reviewed Claim: [Yin_C_F0113_v1](../../claims/Yin_C_F0113_v1.md#decision-candidate-0001).
Selected statement and complete supporting argument: [Yin_C_F0113_v1.md](../../claims/Yin_C_F0113_v1.md#three-square-zero-reconstruction-interface), Sections 1--4.
This review binds the complete statement, its support condition and all three proof components, not only an excerpt or a proposed mechanism.

Consumer scope: [Yin_T_F0007_v1](../../tasks/Yin_T_F0007_v1.md#decision-candidate-0001).
The Task is authorization and scope provenance, not an additional mathematical premise.

**Verdict: pass for the scalar polynomial center, the exact noncentral commutator norm, and bounded scalar reconstruction under the stated positive-word Fourier support hypothesis.**
Automatic positive-word support, the full three-generator closure equality and general T_F0007 remain unproved.
The center calculation and the failure of the pair parameter to remain central are not counterexamples to any of those open equalities.

## 1. Review arrangement and version correspondence

The reviewer did not develop, propose, write or edit the author's three-generator proof.
The coordinator assigned the complete candidate for independent examination, specifically requesting checks of the full-series minimal representation, forbidden state products, actual pencil decay, basis-change conventions and the adjoint-free scalar inversion interface.
Before this review, the reviewer had studied T_F0005 domain bridges and reviewed other T_F0005 arguments in the same shared research context.
This provided familiarity with the project's dependency conventions but did not supply the C_F0113 argument.
The review is separately organized internal AI mathematical review with disclosed shared context; it is not blind review or external human review, and its independence is not inferred merely from the agent name.

The initial complete candidate was read before forming a pass verdict.
The reviewer also read the relevant C_F0106 proof chain and the existing DR97-U004 source reconstruction; the accepted Miy22 minimal-representation interface was checked as context for C_F0106.
The present formal review then reread the full final artifact.
Sections 2--3 of the initial candidate and final proof have unchanged mathematical content.
The formal header, links and scope wording were checked separately.
The added Section 1 explanation placing the three-factor test within the binary Task contract is verified below.

The v1 registration snapshot predates the addition of direct dependencies; the exact accepted inputs for this mathematical review are therefore explicitly fixed here and also appear in the current canonical record.
No canonical record, proof, Task or index was edited by the reviewer in preparing this audit.

## 2. Fixed accepted inputs and source depth

| Fixed input | Exact scope used |
| --- | --- |
| [Yin_C_F0112_v1](../../claims/Yin_C_F0112_v1.md#decision-candidate-0002) | Single-factor input equalities and two-generator bounded reconstruction; the central parameter and four-coefficient construction used only for comparison; the grouping of the first two factors as an input satisfying the binary Task hypotheses. |
| [Yin_C_F0106_v1](../../claims/Yin_C_F0106_v1.md#decision-candidate-0002) | Full finite-factor coefficient series, finite residual space and minimal state matrices; same-factor forbidden products; homogeneous estimate and actual operator-norm decay of the state pencil; identification of its bounded resolvent output with the given bounded affiliated-rational element. Its positive-pivot reconstruction in the larger star algebra is not used to reconstruct in the original non-star algebra. |

- [Yin_C_F0112_v1.md](../../claims/Yin_C_F0112_v1.md)
- [Yin_C_F0106_v1.md](../../claims/Yin_C_F0106_v1.md)
- [DR97 analytic realization audit](../literature/DR97/Yin_U004.md#dr97-u004)

Their prior independent reviews are accepted dependency evidence, while the particular interfaces needed here were read directly rather than inferred from the Claim titles.

The additional direct external logical input is **DR97-U004, Lemma 11**, in its general unital Banach-algebra form.
The existing source audit records statement checking and complete local proof reconstruction, independently cross-reviewed on 2026-09-08 against the registered published ten-page source, printed pp. 619--621 / PDF pp. 7--9.
It records corrections to the printed Schur formulas and an explicit small-power scalar-pivot argument.
This reviewer checked that accepted reconstruction and its application here; no new original-PDF acquisition, rendered-page inspection or whole-paper review is claimed in this review.
The group-specific parts of DR97 Proposition 9 are not being applied to the present matrix-unit algebra.
The Miy22 finite-residual/minimality input is inherited through C_F0106 at its recorded source depth; it is not a new direct Claim dependency.
Yin_S_F0016 is strategy context, not a theorem premise.

## 3. Polynomial center and exact commutator

The centered elements `x_i=e_12^(i)` satisfy `||x_i||_2^2=1/2`.
Freeness gives orthogonality of distinct reduced positive words: different factor patterns lie in orthogonal reduced-word summands, and each factor contributes its one fixed centered vector.
A word of length n has squared norm `2^(-n)`.
Words with adjacent equal indices vanish by `x_i^2=0`.
Thus the stated reduced words, together with the vacuum, form a linearly independent polynomial basis; there are no additional polynomial relations hidden in the representation.

For each nonempty reduced word w, a third index k can be chosen different from both its first and last indices.
The word `x_k w` is reduced.
In `x_k h`, its coefficient is precisely the coefficient of w in h: deletion of its first letter is unique, while a term starting in k vanishes rather than reducing to another word.
Every surviving term of `h x_k` ends in k, whereas `x_k w` does not.
Commutation with `x_k` therefore forces that coefficient to be zero.
This proves `Z(A_3)=C1` for arbitrary polynomial h, including sums containing words of different lengths.

The four length-three words in `[x_1x_2+x_2x_1,x_3]` have distinct factor patterns and coefficients of absolute value one.
Their squared norms are all `1/8`.
Consequently the squared commutator norm is exactly `4/8=1/2`.
The proof does not infer a description of the center of the affiliated or scalar division closure.
Scalar polynomial center and the infinitely many linearly independent reduced words do exclude a finite-module presentation over a nonconstant polynomial central parameter of the C_F0112 kind; they do not exclude other rational presentations.

The retained two-letter assertion is legitimate in the three-factor ambient algebra.
For the finite tracial inclusion of the two-factor von Neumann algebra N into M, kernel projections and hence affiliated invertibility are preserved.
Every rational operation on its generators stays affiliated to N.
If the result is bounded in M, its spectral projections show it belongs to N.
C_F0112 then supplies the required bounded scalar expression.
This justifies the statement that an unresolved example must involve all three letters.

The binary Task explanation also passes.
Grouping the first two full M2 factors gives `N_12`; its coordinate algebra `A_12=C<x_1,x_2>` is finitely generated, generates `N_12` as a von Neumann algebra, and has the required input equality by C_F0112.
The third coordinate algebra has its elementary input equality.
Freeness of the grouped algebra from the third factor follows from the reduced free-product construction.
Their generated coordinate algebra is exactly `A_3`.
Thus a positive general binary permanence theorem would settle this test; no ternary hypothesis has been silently added to the original Task.

## 4. The exact C_F0106 representation before reconstruction

Let B denote the full polynomial star algebra of the three M2 factors.
The inclusion `A_3 subset B` puts the given bounded `f in Div_(L0(M)) A_3` within C_F0106's hypothesis, and its Section 4 supplies the required finite-rank auxiliary commutators.
This step is used to obtain a representation, not to identify the two different scalar division closures.

C_F0106 Section 5, equation (13), extends the reduced-word coefficients by zero on all nonreduced words of the **full free monoid**.
Equations (14)--(16) establish a finite residual space and a minimal representation `beta_w=lambda mu(w) gamma` of this full series.
This is stronger than merely representing the coefficients on admissible paths.
The minimality shift identity makes every entry of `mu(w)` a fixed finite combination of coefficients `beta_(p w q)`, giving the square-summability in (17).
The zero coefficients of `p(i,a)(i,b)q`, for arbitrary full-monoid p,q, and the spanning observable rows and reachable columns give the actual identities `mu_(i,a) mu_(i,b)=0` in (18).

C_F0106 Section 7 then uses the positive matrix Q in (27) to obtain exponential state energy decay (28).
All nonreduced matrix coefficients vanish before evaluating the factor words, so (30) has no shorter terms produced by factor multiplication.
The homogeneous estimate yields actual matrix operator-norm decay `V^n -> 0` in (31).
This conclusion precedes the positive `B*B` scalar-pivot step.
The geometric inverse therefore exists independently of that step.
Finally (36), convergence on the vacuum and faithfulness identify its bounded output with f.
All parts of (4) in the reviewed proof are consequently available from the fixed input at the claimed point in its argument.

## 5. Basis change and elimination of unwanted states

The displayed three Pauli elements are centered and orthonormal for normalized matrix trace.
The new basis `z_+=sqrt(2)e_12`, `z_-=sqrt(2)e_21`, `z_0=e_11-e_22` is likewise centered and orthonormal.
If `z_t=sum_s U_(ts)a_s`, the coefficient transformation uses `conjugate(U_(ts))`, exactly as stated.
Tensoring that transformation over each reduced word gives the new matrices `mu_tilde_t=sum_s conjugate(U_(ts)) mu_s`.

The transformation mixes letters only within each factor.
Thus it preserves the same-factor zero products.
Since the old and new transition families linearly span each other within each factor, products in either family linearly span products in the other, and the reachable and observable spaces do not change.
Minimality is retained.

The support hypothesis `f Omega in H_+` makes every new coefficient of a reduced word containing a minus or zero letter vanish.
For arbitrary words p,q, a word `ptq` containing such a letter either is reduced and has zero coefficient by support, or is nonreduced and has zero coefficient by the already proved state zero products.
Hence `lambda mu_tilde(p) mu_tilde_t mu_tilde(q) gamma=0` for all p,q in the full monoid.
The spanning rows and columns then force the matrix `mu_tilde_t` itself to vanish.
No unobserved state or cancellation only at the scalar output survives this argument.

The identity of the actual state pencils is also exact:

`sum_t mu_tilde_t tensor z_t = sum_(s,r)(sum_t conjugate(U_(ts)) U_(tr)) mu_s tensor a_r = sum_s mu_s tensor a_s`.

Thus the proof transfers the previously established operator-norm decay for the identical operator V.
After the unwanted matrices vanish, its entries belong to the original non-star `A_3`, since the only surviving letters are `sqrt(2)x_i`.
No adjoints have been reintroduced through this basis change.

## 6. Scalar inverses in the original alphabet and verdict boundary

Apply the accepted general Banach-algebra Lemma 11 to the actual matrix V over M.
Its hypothesis is satisfied by the verified decay, not by a supposition about an arbitrary original affiliated pencil.
For completeness, a sufficiently high power `V^q` has all entries smaller than `1/(2N)`.
Eliminating `I-V^q` with scalar Schur pivots keeps successive entry bounds below `r_k=1/(2N-k)<1`, so every pivot has an actual bounded inverse in M.
Every expression uses ring operations and scalar inverses of elements built from entries of V, which are in `A_3`.
Multiplication by `I+V+...+V^(q-1)` gives `(I-V)^(-1)` using the same scalar closure.
There is no matrix-inverse-to-scalar-inverse shortcut and no positive `B*B` step that enlarges the alphabet.

Combining these inverse entries with the scalar row and column gives `f in Div_M A_3`.
Zero and constant coefficient series are immediate cases and do not require a positive-dimensional nontrivial state construction.
This completes the conditional reconstruction with exactly its displayed hypothesis.

All three asserted conclusions therefore pass the complete mathematical review.
The proof has not established `f Omega in H_+` for every bounded affiliated-rational f, or shown that this support is necessary for bounded scalar reconstruction.
A support counterexample would defeat this sufficient route alone.
The affiliated invertibility of `x_1+x_2+x_3`, the rational center, diffuse inputs and general T_F0007 remain outside the accepted result.
No numerical test, proof-assistant verification, new novelty conclusion or external human acceptance is claimed.
