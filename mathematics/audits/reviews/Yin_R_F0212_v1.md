---
author: Yin
---
# Independent review of normality from a central polynomial

At 2026-11-13T13:13 UTC an agent acting for Yin completed an independent whole-proof inspection of the [fixed central-polynomial claim](../../claims/Yin_C_F0204_v1.md#decision-candidate).
The reviewer took no part in developing the proof and received the fixed artifact and the review scope without development dialogue, drafts, author explanations or prior findings about this claim.
The published theorem interfaces were read in the declared source units.
The scalar conclusion was checked against the fixed project proof and its adopted support.

## Whole-proof finding

Both normality assertions hold, and the actual ACSY hypothesis gives the stated full-domain dual.
The weaker assertion admits atoms away from the critical values and imposes no vacuum condition.

**Spectral and Hilbert-space reduction.**
ACSY24 Proposition 3.5 applies on the represented weakly dense starred core with the stated outer actions and adjoint vacuum.
MSY23 Theorem 1.1 applies to bounded nonselfadjoint tuples and makes a nonzero scalar polynomial, viewed as a full \(1\)-by-\(1\) matrix, invertible after evaluation in the affiliated algebra.
For each fixed \(s\), \(p-s\) is nonzero and the kernel projection of \(p(X)-s\) is precisely the spectral projection of the central normal \(Y\) at \(s\).
Thus every singleton is null under actual ACSY.
For the second assertion the explicit hypothesis removes all non-simple root fibers of positive measure, which is the only use of this spectral exclusion.

Centrality makes \(E_{W^*(Y)}\) tracial as a center-valued moment map by testing against bounded functions of \(Y\) under \(\tau\).
The countable rational positivity tests extend to each finite complex coefficient space by continuity.
They bound both GNS generator actions, and traciality bounds right word multiplication, whose cyclic orbit makes the trace vector separating for the left algebra.
Testing the central polynomial relation on the countable cyclic word vectors gives the operator identity \(p(X_s)=s1\).
The generating hypothesis gives density of those word vectors before decomposition, while their fiber values are total by GNS construction.
Testing the product-space inner products on measurable rectangles therefore realizes the coarse space with the indicated left action on the first leg and right action on the second.

**Diagonal obstruction.**
In the derivative of \(Yw=wY\), the terms involving \(\delta w\) combine to \((s-t)(\delta w)_{s,t}\), and the other side multiplies the second leg of \(B_{s,t}\) on the right by \(w_t\).
The polynomial expression for \(G_w\) defines its diagonal independently of the product-almost-everywhere representative of \(\delta w\).
At each atom the equation holds on the positive-mass product point.
For the nonatomic part, finitely many moments determine \(\|G_w(s,t)\|^2\), so a positive-measure exceptional diagonal would give a positive-measure cell \(A\) on whose square this squared norm has a uniform positive lower bound.
Indeed one can first choose a fixed positive threshold on a level set and then partition the compact moment box by uniform continuity.
Writing \(\nu=\mu|_A\), a grid with at most \(Cr^{-2}\) cells meeting its bounded support gives a sum of squared cell masses at least \(C^{-1}r^2\nu(A)^2\).
Tonelli applied to \(2r^{-3}\mathbf 1_{\{|s-t|\le r\}}\) now yields divergent inverse-square energy off the null diagonal, contradicting square integrability of \(\delta w\).
This applies separately to every word and hence simultaneously on a single conull set.
The planar estimate uses no density or regularity of the law.

**Fiber algebra and the full-domain consequence.**
At every remaining regular value, interpolation in \(p(u)-s\) gives algebraically orthogonal idempotents, including the possibility that some vanish.
After discarding zero idempotents their vectors are linearly independent by left multiplication and separation.
The divided-difference coefficients vanish between distinct roots, and every surviving diagonal coefficient equals the nonzero derivative at its root.
Projection of the first tensor leg onto the orthogonal complement of their span in \(H_s\), followed by independence on the second leg, puts each \(w_sP_\ell\) in that span.
Separation turns these vector identities into operator identities, so summing gives \(X_s^*\) in the same commutative polynomial algebra as \(X_s\).
This step requires no selfadjointness or Hilbert-space orthogonality of the individual idempotents.
Integration and faithfulness give normality in \(M\), and generation by \(X\) then gives commutativity.

The initial citation to C_F0071 v1 Part C led to an open assessment.
The revised argument and dependency row cite [v2 Part C](../../claims/Yin_C_F0071_v2.md#statement), whose proved decision selects the [whole-proof finding](Yin_R_F0044_v1.md#conclusion) covering that scalar implication.
I checked the scalar argument in both versions and the [domain conclusion it uses](../../claims/Yin_C_F0055_v1.md#7-actual-adjoints-and-original-graph-restoration).
In the normal model the law of \(X\) is diffuse under actual ACSY, and differentiating \(XX^*=X^*X\) determines the starred divided difference off the product-null diagonal.
The vacuum therefore supplies exactly the scalar adjoint hypothesis of C_F0055.
The divided-difference contraction satisfies \([E_0,X]=P_\Omega\) on polynomials.
Graph approximation extends this bounded commutator to its closed domain, which contains all bounded functions by the [accepted scalar estimate and domain proof](Yin_R_F0037_v1.md#scalar-findings).
Taking \(D=-\overline{E_0}|_M\) gives \([X,D]a=\tau(a)1\) on all of \(M\), with the requested sign.

The two published theorems are used at their inspected statement and hypothesis interfaces, without a new inspection of their full source proofs.
The critical-energy comparison is present in [Brauchart and Grabner, §3.3, p. 26](https://www.math.tugraz.at/~grabner/Publications/Energy-Designs.pdf), while the grid argument proves the estimate used here directly.
This finding concerns the central-polynomial branch of T_F0011 and leaves the unrestricted one-generator implication open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0204_v1.md#statement) | Both normality assertions and the actual-ACSY generator-first full-domain dual. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0204_v1.md#argument) | Central moment fibers, diagonal obstruction for arbitrary spectral laws, simple-root algebra and scalar dual. |
| [Whole-proof finding](#whole-proof-finding) | [ACSY maximality](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 on the represented starred domain with a Hilbert adjoint vacuum. |
| [Whole-proof finding](#whole-proof-finding) | [MSY affiliated equivalence](../literature/MSY23/Yin_U001.md#msy23-u001) | Theorem 1.1 applied to the nonzero scalar polynomials \(p-s\). |
| [Whole-proof finding](#whole-proof-finding) | [Scalar Part C](../../claims/Yin_C_F0071_v2.md#statement) | Actual ACSY implies a bare full-domain dual for the resulting single normal generator. |
