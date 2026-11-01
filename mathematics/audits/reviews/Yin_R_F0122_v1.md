---
author: Yin
---

# Ordered Affine Minimax: Independent Proof Review

Date: 2026-09-12.
Reviewer: the reviewing agent.
Author of the reviewed proof: root.
Target: the ordinary deductions in [Affine Scalar Minimax](../../claims/Yin_C_F0122_v1.md), within the offline [Yin_T_F0008](../../tasks/Yin_T_F0008_v1.md#yin_t_f0008) exploration.
No Claim IDs or theorem Roles are assigned by this review.

Review state: **independently reviewed, with shared-input collaboration disclosed**.
The reviewer wrote the separate [spectral-potential module](../../claims/Yin_C_F0123_v1.md), whose elementary Poisson-kernel inversion interface is consumed by the isotropic extension.
The reviewer did not write the minimax argument.
Root sent the proposed isotropic formulas before review; the complete written proof was then independently read and checked.
This is an internal mathematical review, not an external or formally verified assessment.

Inspected artifacts:

- Initial scalar and commuting proof, equations (1)-(7).
- Full proof including isotropic covariance, equations (1)-(15).

Outcome: **passed within the stated scalar, commuting, and isotropic-covariance scopes**.
All mathematical dependencies needed by these formulas are supplied by the locally reviewed Dyson primitive, the scalar semicircular potential, and the explicit calculations in this proof.
No general covariance minimax, unrestricted saddle point, novelty claim, or completion of the broad affine-capacity objective is certified.

## Isotropic covariance calculations

The hypothesis is exactly \(\eta(b)=\sigma\operatorname{tr}_m(b)I_m\), \(\sigma>0\), with all coefficient matrices selfadjoint.
It does not require their commutation.
The following checks concern arbitrary selfadjoint drift, every real spectral argument, repeated eigenvalues, support edges, and possible closing gaps.

| Obligation | Decisive check |
| --- | --- |
| Inner maximizer and pole behavior | \(I(p,q)\) strictly decreases with \(q^2\). Its positive solution has \(I=1/\sigma\), and the zero maximizer occurs precisely when \(I(p,0)\le1/\sigma\). At an atom of mass \(w\), \(w/q^2\le1/\sigma\) forces \(q^2\ge\sigma w\). A positive branch therefore cannot meet zero at an atom. This gives the claimed continuity and correct endpoint behavior. |
| Finitely many transitions | Away from finitely many poles, \(I(p,0)=1/\sigma\) is a nonconstant rational equation with finitely many solutions. The positive-\(q\) set is bounded because \(I(p,0)\to0\) at infinity. An isolated zero at a closing gap is included among these transition points. |
| Strictly increasing real map | From \(I=1/\sigma\), implicit differentiation gives \(q'=-C/(qB)\). Differentiating the real resolvent integral gives \(X'=2\sigma(q^2B+C^2/B)>0\) on positive branches. On open zero branches \(X'=1-\sigma I>0\). Continuity and finitely many exceptional endpoints yield strict increase globally, including closing gaps. The asymptotic \(X(p)=p+O(1/p)\) proves surjectivity. |
| Reduced objective | The derivative is \((X(p)-x)/\sigma\); continuity across endpoints follows from nonzero denominators and the continuous maximizing \(q\). Consequently strict convexity, coercivity, unique minimization, and attainment follow without assuming a raw convex-concave saddle. |
| Physical branch and uniform bounds | The scalarized Dyson equation gives \(\varepsilon=q(1-\sigma I)\), hence \(I<1/\sigma\). Cauchy-Schwarz gives \(|g|^2\le I<1/\sigma\). Each eigenvalue has mass at least \(1/m\), so \(|w-\lambda_k|\ge\sqrt{\sigma/m}\). Both boundedness and uniform pole separation hold for every positive imaginary spectral part. |
| All real boundary points | Every subsequential limit has \(q=0\) with \(I\le1/\sigma\), or \(q>0\) with equality. These are exactly the inner maximizer conditions. The real equation is \(X(p)=x\); its unique solution identifies every subsequence, including edges and closing gaps. The same argument for varying real parts proves continuity of the boundary values. |
| Primitive and determinant | The normalized matrix trace of \(\eta(G)G\) equals \(\sigma g^2\), not \(m\sigma g^2\). Thus equation (13) has the correct coefficient. Substituting \(g=(x-p-iq)/\sigma\) gives the ordered objective. Pole separation makes its limit finite, and monotone spectral integration identifies it with the operator logarithmic determinant. |
| Whole spectral measure | The uniform bound \(|g|\le1/\sqrt\sigma\) allows dominated convergence in each Poisson-kernel inversion integral and forces all atoms to vanish. The continuous boundary imaginary part yields \(q(X^{-1}(x))/(\pi\sigma)\). Identifying all interval masses excludes a residual singular continuous component as well as atoms. Faithfulness gives equality of spectral support and spectrum because this operator is selfadjoint. |
| Determinant normalization | Exponentiating the normalized logarithm produces precisely equation (15). The scalar exponential multiplying the \(m\)-by-\(m\) matrix needs no extra \(m\) factor. For zero drift, \(\operatorname{cap}(\eta)=\sigma^m\), by the arithmetic-geometric mean inequality for the eigenvalues of positive trial matrices; the displayed value is therefore \(e^{-1/2}\sqrt\sigma\). |

## Inputs, attribution, and limits

The Yin_C_F0119 logarithmic primitive and its scalar semicircular specialization were read in the existing ledger and review.
The spectral inversion used here was also checked directly from the scalar Poisson kernel, as recorded in the reviewer's spectral module.
Thus the isotropic proof does not depend on an unverified global subordination theorem or a pre-existing variational theorem whose source was not inspected.

The isotropic scalarization is the familiar semicircular-convolution mechanism.
The proof explicitly leaves comparison with known variational formulations for a future authorized attribution check.
This review establishes mathematical validity at the stated scope and does not certify source completeness for a future manuscript's historical discussion.
No network search was used; no novelty search, numerical experiment, formal proof, or external expert review was performed.

The proof does not justify replacing its scalar trial variables by arbitrary noncommuting matrices.
It also does not claim that the raw objective has a global saddle.
Those are separate remaining research obligations rather than gaps in the proved ordered formulas.

## Relationship arrangement

The original reviewer authored the separate spectral module; dependency authorship alone does not decide the target relationship.
The record additionally states that root sent the proposed isotropic formulas before review, which supplies shared target mathematical development context for the isotropic finding and makes that finding self-reviewed.
The original 2026-09-12 review, source limits and attribution limits remain intact.
The [original scalar/commuting unknown finding](Yin_R_F0181_v1.md#scalar-and-commuting-calculations) and [later isolated isotropic finding](Yin_R_F0181_v1.md#f0080-isotropic-and-whole-spectral-measure-finding) retain their separate dates and relationships.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#isotropic-covariance-calculations) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#isotropic-covariance-calculations) | [C_F0122 statement](../../claims/Yin_C_F0122_v1.md#statement) | Full isotropic-covariance extension, equations (8)–(15), in the scalar/commuting context: arbitrary selfadjoint drift, all real spectral arguments including edges and closing gaps, strict reduced convexity, physical branch and pole separation, exact determinant and whole continuous spectral measure. No arbitrary noncommutative covariance minimax is certified. |
| [Original finding](#isotropic-covariance-calculations) | [Isotropic selected argument](../../claims/Yin_C_F0122_v1.md#identifying-the-physical-solution-and-the-determinant) | Full isotropic-covariance extension, equations (8)–(15), in the scalar/commuting context: arbitrary selfadjoint drift, all real spectral arguments including edges and closing gaps, strict reduced convexity, physical branch and pole separation, exact determinant and whole continuous spectral measure. No arbitrary noncommutative covariance minimax is certified. |
