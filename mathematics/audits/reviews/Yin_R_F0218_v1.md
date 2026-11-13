---
author: Yin
---
# Independent review of the uniform one-generator criterion for bare duals

## Whole-proof finding

At 2026-11-13T13:45 a separate agent outside proof development checked the complete [statement](../../claims/Yin_C_F0210_v1.md#statement) and [argument](../../claims/Yin_C_F0210_v1.md#argument) of the working candidate, including the cutoff-free corollary.
The reviewer inspected the fixed proof, its two declared inputs in C_F0205 v1 and the Task definitions.
No proof-development dialogue, drafts, author explanations or prior findings on C_F0210 were supplied or consulted.
The [existing review of C_F0205](Yin_R_F0213_v1.md#whole-proof-finding) covers the free extension and scalar input used here.
The conditional construction and both quantitative conclusions hold.

For finite costs an unbounded sequence of ratios has an increasing subsequence exceeding \(4^n\), since deleting a finite prefix preserves unboundedness.
At each index all three upper bounds on the positive weight can be met by decreasing it, even for arbitrarily large finite starred derivatives.
For \(1\le a<b\), the gap is at least \(2^{-a-1}\), while \(r_a+r_b\le3\cdot 2^{-a}/32\).
The auxiliary corner has a gap of at least \(3/2\) from each other center.
On a circle surrounding just one disk, the Neumann resolvent bound is uniform in every product coordinate.
Integration gives precisely that central unit, also for nonnormal corner generators.
The affine coordinate generates the whole supported corner, and strong convergence of finite central truncations supplies the product algebra.

On a diagonal tensor block the normalized squared Hilbert norm gains a factor \(t_n^2\), whereas on a single Hilbert leg it gains \(t_n\).
Thus \(r_n^{-1}\delta_n\) on the represented corner polynomial has the prescribed generator value, starred value \(K_n\), and vacuum vector \(t_n\xi_n/r_n\) in the inherited leg.
The bounds on \(t_nK_n\) and \(t_n^{3/2}\xi_n/r_n\) respectively ensure a coarse-valued word rule and a bounded diagonal vacuum functional.
Scaling the standard semicircular by \(1/2\), for example, gives a norm-one auxiliary generator with the original difference quotient multiplied by two and finite vacuum.
Each mixed Sylvester operator has a perturbation of norm at most half its scalar gap, and \(\sum_{a\ge1}4^a t_a<\infty\) bounds the mixed squared norms after summation over the other index.
The resulting inner derivation depends only on the represented input and has the required mixed generator components.
In its vacuum pairing the two adjoint outer actions on \(1\otimes1\) each have norm \(\|p(X)\|_2\), using the probability trace.
The mixed and diagonal bounds therefore give a genuine adjoint vector on the dense represented star algebra.

For an input supported at \(n\), restriction of \(P_\Omega\) followed by output compression sends \(a\) to \(t_n\tau_n(a)1_n\).
The scalar center in \(X_n\) commutes with \(B_n\), yielding the asserted \(t_n/r_n\) multiple of a normalized commutator on the full corner algebra.
Finite signed sums of separate nearly norming inputs lie in the product unit ball.
Sign averaging cancels every cross term before projection, so the bound sums \(t_n\|B_n\|^2\) even if the dual mixes all corners.
The resulting lower series has terms at least \(4^{-n}(4^n)^2=4^n\).
An original infinite cost already supplies the one-generator conclusion directly.
In both cases the accepted C_F0205 implication applies at length one and excludes the algebraic system after adding a free semicircular coordinate, with \(D=-E\) for the Task convention.

Failure of a common constant on the unit ball selects a sequence of actual witnesses covered by the construction.
For a general generator, vacuum testing yields \(1\le\|\xi\|_2\|T\|_2\le\|\xi\|_2\|T\|\).
Thus \(L=\|T\|>0\), and the star algebra of \(T/L\) is the same represented algebra.
The positive scaling takes \(\delta\) to \(L\delta\) and bijects the bounded duals by \(E\mapsto LE\), preserving the freedom in the value at one and scaling the infinite-cost case as well.
On this unit ball generator \(L\|\xi\|_2\ge1\), so \(L\beta(T)\le C(1+L\|\xi\|_2)\le2CL\|\xi\|_2\) under the universal implication.
An unbounded arbitrary-cutoff ratio therefore provides the premise after normalization.
Existence of such a sequence remains open in this review, and the two uses of C_F0205 were checked at their indicated interfaces.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0210_v1.md#statement) | Conditional one- and two-generator conclusions, uniform bounds at norm one and arbitrary cutoff, and unrestricted finite starred costs. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0210_v1.md#argument) | Product generation, represented derivation and actual adjoint, simultaneous corner testing, extension and positive scaling. |
| [Whole-proof finding](#whole-proof-finding) | [Free augmentation](../../claims/Yin_C_F0205_v1.md#statement) | One actual ACSY generator with infinite bounded-dual cost gives a pair failing the bare full-domain condition. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar difference quotient](../../claims/Yin_C_F0205_v1.md#argument) | The scalar semicircular difference quotient has adjoint vacuum \(s\), as required for the rescaled auxiliary probability corner. |
| [Whole-proof finding](#whole-proof-finding) | [Task hypotheses](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented star-algebra domain, outer actions, actual adjoint and sign of the bare commutator. |
