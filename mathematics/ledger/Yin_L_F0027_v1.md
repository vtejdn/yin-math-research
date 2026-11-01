---
author: Yin
---

# Affiliated Rationality and Additional Analytic Conditions

<a id="affiliated-restart"></a>
Date: 2026-09-09.
Authorization: the user asked whether the Yin_T_F0001 investigation should extend to $L^2(M)$ or $L^0(M)$ and whether the analytic control seen in Miy22 admits a broader formulation.
This is follow-up analysis of the completed [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), not a revision of its original target.
No successor goal is allocated by this note.

## Separate Three Questions

Use the original bounded normal tuple and bounded dual system, and write

\[
U=U(M)=L^0(M,\tau),\qquad
F_X=\operatorname{Div}_U\mathbb C\langle X\rangle,\qquad
\mathcal R_X=\operatorname{Div}_M\mathbb C\langle X\rangle.
\]

The equality of all affiliated operators with the measurable $L^0$ algebra uses the finite trace.
Neither $L^2(M)$ nor $L^0(M)$ means that its elements act as bounded multipliers on $H=L^2(M)$.

| Question | Correct objects and issue |
| --- | --- |
| Algebraic rationality in $U$ | Use finite-rank bounded denominator defects. [Yin_C_F0013](../claims/Yin_C_F0013_v1.md#yin_c_f0013) proves the equivalence, with a separate independent review record. |
| Additional $L^2$ commutator regularity | A weak commutator on bounded test vectors is meaningful, but a bounded extension is an extra condition. [Yin_C_F0014](../claims/Yin_C_F0014_v1.md#yin_c_f0014) supplies an obstruction even for an $L^2$ free-field element. |
| Bounded scalar rational expressions | The missing bounded-intersection property $F_X\cap M=\mathcal R_X$ is refuted in general by Yin_C_F0012. A positive result needs additional analytic or model-specific control. |

The first question can be approached without forcing unbounded operators into the old bounded-commutator notation.
The second and third questions ask for stronger regularity than algebraic membership in the free field.

## The Affiliated Formulation

Every $u\in U$ admits two bounded fractions

\[
u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,
\]

where $s,t$ are regular: they have trivial kernel and dense range, hence affiliated inverses, not necessarily bounded inverses.
For each bounded dual define

\[
\Delta_i(u;s,a,b,t)=sD_i b-aD_i t\in B(H).
\]

This is an everywhere-defined bounded expression.
It does not require $D_i$ to preserve $\operatorname{dom}(u)$.
The finite-rank property is independent of the chosen fractions by bounded common-denominator identities and injective/dense-range cancellation.

Yin_C_F0013 proves the exact equivalence between $u\in F_X$ and finite rank of these defects.
For bounded $u$, the fractions $s=t=1$, $a=b=u$ recover $[D_i,u]$.
Thus this formulation includes the old finite-rank test, while replacing its overly restrictive bounded scalar conclusion by $F_X\cap M$.

The proof uses the existing normal-dual identity and balanced tensors, together with the general fraction identities already audited in [Miy22-U006](../audits/literature/Miy22/Yin_U006.md#miy22-u006).
It does not copy the semicircular bounded-intersection step of Miy22.
In particular, the exact reverse domain inclusion in Miy22 Proposition 4.12 uses special creation-operator identities and is not asserted for arbitrary dual systems.

## What Classical Kronecker Theory Says About L2

The [audited exact Kronecker statement](../audits/literature/Miy22/Yin_U009.md#miy22-u009) concerns a bounded finite-rank Hankel matrix on $\ell^2(\mathbb N_0)$.
Its column states lie in $\ell^2$; finite shift-invariance gives a rational function, and square summability forces the eigenvalues of the backward shift restricted to that column space strictly inside the unit disk.

An equivalent starting point is a square-summable sequence whose Hankel columns span a finite-dimensional space.
The Hankel matrix then extends boundedly: choose finitely many coordinate functionals that determine a vector in that column space; each resulting coefficient row is an $\ell^2$ sequence, since it is a finite combination of shifted copies of the original sequence.
This is a Hankel-structure argument, not a claim that every finite-dimensional range map on a dense domain is bounded.

For an $L^2(\mathbb T)$ symbol, one Hankel operator sees only one Fourier half.
Rationality of the whole symbol requires an analytic/anti-analytic normalization or inspection of both blocks.
Once a scalar rational function is in $L^2$ for circle Lebesgue measure, a genuine pole on the circle is impossible; it is therefore bounded there.
The [Haar two-block calculation](../audits/literature/Miy22/Yin_U009.md#miy22-u009) makes these conventions explicit.

That last gain is measure-dependent.
For the Yin_C_F0012 law $4t^3dt$,

\[
h^{-1}\in L^2(M)\setminus M.
\]

The spectral density vanishes fast enough near zero to make a genuine pole square integrable.
Thus the classical Hardy/circle conclusion cannot be transferred solely by replacing a symbol space with abstract $L^2(M)$.

The stronger Yin_C_F0014 example $u=h^{-1}bh^{-1}\in F_X\cap L^2(M)$ shows that even an $L^2$ rational output need not have bounded weak commutators.
A restricted literal common domain can conceal this failure; it must not replace the specified weak form or the denominator-defect criterion without a separate domain argument.

## Existing Positive L2 Results and Their Mechanism

The already audited [Miy26-U002, Theorem 1.1](../audits/literature/Miy26/Yin_U002.md#miy26-u002) gives a precise positive answer for a finite standard free semicircular tuple $s$:

\[
F_s\cap L^2(M)\subseteq M.
\]

Combining this with the separately established Miy22 bounded-intersection theorem and the finite trace gives

\[
F_s\cap L^2(M)=F_s\cap M=\operatorname{Div}_M\mathbb C\langle s\rangle.
\]

This is an existing source theorem, not a new project claim.
The [Miy26-U003 Haar variant](../audits/literature/Miy26/Yin_U003.md#miy26-u003), using its accepted Lin00 bounded-intersection input, gives the corresponding equality for the finite canonical free Haar tuple in the free group von Neumann algebra.
Freeness, the canonical trace and the specific word structure are retained; an arbitrary collection of Haar-distributed generators is not covered.

Miy26's semicircular proof first regularizes a rational $L^2$ element using bounded rational $a=(1+ff^*)^{-1}$ and $b=af$.
The known Miy22 bounded-intersection theorem supplies their bounded finite-rank commutators.
The Fock coefficient identity then gives finite-dimensional suffix residuals for the original $f$.
Squared coefficients and length aggregation have a finite recurrence; their summability forces exponential decay.
The homogeneous norm bound turns that decay into a norm-convergent expansion, whose canonical $L^2$ vector identifies its bounded sum with $f$.

This suggests a sufficient condition for the same $L^2$-to-bounded implication in another model: every rational $L^2$ element has a recognizable expansion in a graded orthonormal word basis, and homogeneous evaluation satisfies the subexponential estimate below.
The scalar degree-energy argument then proves boundedness of the output directly.
Obtaining that recognizable expansion in the new model is a substantive hypothesis; bounded duals alone do not supply it.
This condition also does not by itself identify bounded scalar division closure.

## A Stronger Package for Bounded Scalar Reconstruction

The property

\[
F_X\cap M=\mathcal R_X
\]

names the exact additional bounded-intersection requirement.
As a hypothesis it is simply the desired bridge, not a practical criterion for establishing it.
More informative sufficient conditions should supply a bounded inverse representation.

One usable structural package, suggested by [Miy22-U004-U005](../audits/literature/Miy22/Yin_U004.md#miy22-u004), consists of the following separately verified inputs:

1. A graded orthonormal polynomial/word expansion in which the finite-rank data yield a recognizable coefficient series.
2. Finite-dimensional realization and regularity estimates giving square-summable coefficients for every entry needed in the inverse realization, not just for its scalar output or a selected row and column.
3. A matrix evaluation estimate
   \[
   \left\|\sum_{|w|=m}c_wS_w\right\|
   \le K_m\left(\sum_{|w|=m}|c_w|^2\right)^{1/2},
   \qquad \limsup_{m\to\infty}K_m^{1/m}\le1.
   \]
   Polynomial growth, such as Miy22's constant times $(m+1)$, is sufficient.
   The bound must cover the required matrix lift, not merely scalar polynomial outputs.
4. A finite matrix realization linking that word evaluation to the original generators, together with bounded scalar elimination where its hypotheses apply.

Here recognizable means that $c_w=\alpha A_w\beta$ for fixed finite scalar matrices.
The degree-energy sequence $e_m=\sum_{|w|=m}|c_w|^2$ has a rational generating function, using the finite matrix $\sum_i A_i\otimes\overline{A_i}$.
If $\sum_m e_m<\infty$, that rational generating function has no uncancelled pole on the closed unit disk.
Therefore $e_m\le C\rho^{2m}$ for some $\rho<1$.
The displayed subexponential evaluation bound then gives

\[
\sum_m\left\|\sum_{|w|=m}c_wS_w\right\|
\le \sqrt C\sum_m K_m\rho^m<\infty.
\]

Applied to all entries of a geometric inverse realization, this proves norm convergence of the whole matrix inverse.
For instance, if $T$ is the corresponding finite matrix over the original algebra and the estimates apply to the entries of $T^m$, then $\sum_mT^m=(I-T)^{-1}$ in operator norm.
One must actually verify that this realization evaluates the intended affiliated element.

For this geometric inverse, the audited Banach-algebra argument in [Miy22-U005, Lemma 3.8](../audits/literature/Miy22/Yin_U005.md#miy22-u005) supplies scalar elimination without adjoining adjoints.
Norm decay of $T^m$ allows a choice of $N$ for which every leading principal block of $I-T^N$ is invertible.
Scalar Schur pivots give its inverse entries in the scalar division closure, and

\[
(I-T)^{-1}=(I+T+\cdots+T^{N-1})(I-T^N)^{-1}
\]

gives the desired entries.
If the analytic input instead supplies an arbitrary bounded matrix inverse without this decaying-power representation, [Yin_C_F0008](../claims/Yin_C_F0008_v1.md#yin_c_f0008) supplies elimination under $\mathcal A^*\subseteq\operatorname{Div}_M\mathcal A$, where $\mathcal A$ is the initial algebra.
Individual normality alone does not imply that adjoint-closure hypothesis.

These conditions provide a proof strategy for broader model classes.
They are not asserted to hold for every bounded dual system, and no new class of tuples is certified by this note.
In particular, Yin_C_F0007's square-integrable left/right states do not establish input 2, and polynomial growth estimates alone do not establish inputs 1 or 4.

## Research Disposition and Evidence

Subsequent user-requested formalization, 2026-09-09: the scalar residual/norm mechanism now has its exact reusable statement and proof in [Yin_C_F0015](../claims/Yin_C_F0015_v1.md#yin_c_f0015).
[Yin_S_F0007](../strategies/Yin_S_F0007.md#s_f0007) is the explicitly authorized active strategy connecting it to structural regularity; [Yin_C_F0016](../claims/Yin_C_F0016_v1.md#yin_c_f0016) records regularity obstructions.
The [scope clarification](Yin_L_F0013_v1.md#rationality-conventions) distinguishes fraction-dependent defects from their invariant ranks and defines bounded scalar expressions.
These later records supersede the earlier unselected-route disposition below without changing Yin_T_F0001's original resolution.

The old Yin_T_F0001 remains completed by its exact counterexample.
Yin_C_F0013 and Yin_C_F0014 have separate claim records because their domains and conclusions differ from Yin_C_F0001.
Their respective proof and review status is owned by the responsible Claim materials and their selected decisions.
Potential further work is to verify the analytic package in a concrete family or characterize additional weak-commutator regularity; neither is automatically selected as a new goal.

The coordinating agent read the existing Miy22 affiliated, Kronecker and scalar-elimination audits, the Miy26 main L2 proof, Yin_C_F0005/Yin_C_F0007/Yin_C_F0008, and the relevant source-interface records.
Independent agents separately examined the affiliated proof and the $L^2$ weak-form obstruction; their actual new proof reviews are linked from those claims.
A third agent independently checked this note's Kronecker interpretation, finite-state energy argument, matrix-versus-output distinction, geometric scalar elimination and exact Miy26 semicircular/Haar scope.

The [Miy22 arXiv abstract](https://arxiv.org/abs/2109.08841) and [Miy26 arXiv abstract](https://arxiv.org/abs/2603.19528) were reopened on 2026-09-09 for source scope; a bounded Kronecker/L2 search added no theorem input.
The existing source audits supply the precise theorem and proof inputs.
No new PDF, broad novelty survey, numerical experiment, or formalization was undertaken.

Integration checks, 2026-09-09: the repository record validator passed on 120 Markdown files and 1,333 local links/anchors; the Git whitespace check found no errors.
The five new proof, review and synthesis files contain English prose.
These are artifact checks, separate from the mathematical reviews above.
Existing unrelated manuscript-rule edits were preserved.
