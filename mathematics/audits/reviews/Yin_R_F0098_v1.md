---
author: Yin
---

# Independent review: two free square-zero matrix-unit algebras

Date/time: 2026-09-16T13:05.
Human record author: Yin.
Reviewer/method: another AI agent, separately organized full mathematical and source-interface review.

Reviewed Claim statement: [Yin_C_F0112_v1](../../claims/Yin_C_F0112_v1.md#decision-candidate-0001), with the identical mathematical conclusion and proof prepared for its second recorded assessment after the formatting correction below; the retained physical proof is v1.
Consumer contract: [Yin_T_F0007_v1](../../tasks/Yin_T_F0007_v1.md#decision-candidate-0001).
Selected proof: [Yin_C_F0112_v1.md](../../claims/Yin_C_F0112_v1.md#free-square-zero-bounded-closure), complete Sections 1--8.

**Mathematical verdict: pass at the exact stated restricted scope.**
The argument gives bounded scalar reconstruction for the two proper non-star matrix-unit input algebras.
No unresolved mathematical gap or counterexample was found.
It does not complete T_F0007.

**Documentation findings:** equation (14) initially lacked its closing display delimiter.
The coordinator inserted the single line `\]` after its `\tag{14}`; the reviewer verified that deleting exactly this one inserted line recovers the originally submitted proof.
This finding is resolved, and the final reviewed version above includes the correction.
The proof expressly imports the C_F0087 Bezout mechanism.
The fixed input is `Yin_C_F0087 (recorded assessment 3)`.

## 1. Arrangement, supplied context, and review procedure

The reviewer did not develop this square-zero proof, its exploratory notes, or its source searches.
Prior work in this same coordinated run concerned T_F0005 local dual domains.
The review context included the user's broad T_F0005/T_F0007 goals, the coordinator's description of the square-zero special case, the registered proof file, and a list of potentially delicate interfaces to check.
It did not include the author's development dialogue or a prior independent whole-proof verdict.
This is an independent, non-blind agent review; separate-agent status alone is not its evidence.

Starting from the claimed equality, the reviewer enumerated and recomputed its needed implications: the inputs meet the original permanence assumptions;
the central rational algebra is actually evaluable and exhausts the scalar affiliated closure;
boundedness of each gauge component forces an allowed bounded scalar denominator;
and the last possible pole has a nonzero multiple of an unbounded idempotent.
The complete author artifact was read before the prior C_F0087 review was consulted.
Existing external source audits and their recorded review boundaries were then reused to check the precise hypotheses, without a fresh PDF or whole-source audit.

All affiliated products were checked as algebra operations in `L^0(M)`.
Kernel and norm arguments were checked separately on bounded operators, or only after the author explicitly assumes an affiliated expression bounded.
No proof-assistant verification, numerical experiment, manuscript compilation, external human review, or novelty assessment was performed.

## 2. Direct inputs and dependency boundaries

The direct project input is [Yin_C_F0087_v1](../../claims/Yin_C_F0087_v1.md#decision-candidate-0002), specifically its coprime numerator-denominator Bezout cancellation in a possibly noncommutative ambient algebra.
The selected proof file matches the inspected version.
The existing [review, originally described as independent](Yin_R_F0088_v1.md#yin_c_f0087-fraction-collapse-and-principal-ideal-cancellation) was read at the C_F0087 scope after this proof's algebraic step had been recomputed.
The application here does not assume that the corner generator is normal.
The displayed formula in Section 6 also reproduces the exact part of the mechanism needed for continuation.

The directly used accepted source interfaces are:

- [CK14-U001](../literature/CK14/Yin_U001.md#ck14-u001): at both projection traces equal to `1/2`, all character intersections vanish and the generic `pqp` parameter has support `[0,1]`.
  The source audit checked equations (1.5)--(1.7), pp. 3--4, and Section 4.2, p. 45, of the identified author version.
  This review checks the substitution and resulting norm/intersection assertions; it does not re-audit the liberation or transform proofs.
- [MSY23-U004](../literature/MSY23/Yin_U004.md#msy23-u004), Lemmas 5.1--5.5: finite faithful trace makes injectivity equivalent to affiliated invertibility, including corners and finite matrix amplifications.
  The foundational affiliated-algebra convention and matrix identification are retained exactly at that audit's declared scope.
- [MSY23-U006](../literature/MSY23/Yin_U006.md#lemma-519-domain-repair), the repaired Lemma 5.19: for finitely many distinct eigenvalues of any affiliated operator, the sum of eigenprojection traces equals the trace of their join and is at most one.
  This particular lemma has no maximal-Delta premise.
  The reviewer recomputed the audit's bounded-row/Vandermonde repair; no invalid limit through an unbounded operator or eigenspace orthogonality is used.
- The existing [Hun74 inspection](../../ledger/Yin_L_F0020_v1.md#reuse-and-source-check), III.3.9 and III.3.11 on printed pp. 139--140, supplies the polynomial Euclidean/Bezout input consumed through C_F0087.
  Its recorded source and earlier independent review are reused; no new source inspection is claimed here.

C_F0100 and C_F0106 are comparisons and provenance for the previously accepted full-star scope, not direct logical dependencies of this proof.
DR97-U004 is expressly not invoked by the present reconstruction.
The Task contract is a consumer and scope reference, not a mathematical proof premise.
No claim about the complete ordinary spectrum or Brown measure of `t` is needed.

## 3. Input assumptions, actual inverses, and the unbounded idempotent

The input algebras `C1+Cx` and `C1+Cy` are unital, finitely generated, and generate their full matrix factors as von Neumann algebras because adjoints are allowed in that generated von Neumann algebra.
The actual division expressions still do not adjoin those adjoints.
In each finite-dimensional ambient algebra, `alpha+beta x` is invertible precisely for `alpha != 0`, and its inverse remains in `C1+Cx`.
Thus both required input equalities are checked, rather than inferred from the full-star result.

For `p=xx*` and `q=yy*`, the matrix-unit identities give `ker x=pH`, `ker y=qH`, and the free-projection source gives `p meet q=0`.
If `(x+y)xi=0`, the common value `x xi=-y xi` belongs to both ranges and vanishes; the same intersection then forces `xi=0`.
Hence `s=x+y` is injective and affiliated-invertible.
Its square `t` is affiliated-invertible as the product of two units.

The factor orders in the centrality and idempotent identities are correct: `tx=xt=xyx`, `ty=yt=yxy`, `(xy)^2=txy`, and therefore `e=xy t^{-1}` satisfies `e^2=e`, `ex=x`, `ey=0`.
Inverses commute with any element commuting with the original invertible element, so the moves of `t^{-1}` are justified in the affiliated algebra.

The source parameter support at trace `1/2` gives `||pq||=||qp||=1` without requiring an endpoint eigenvector.
If `e` were bounded, `ep=p` and `eq=0`.
Unit vectors in `pH` can have `||q xi_k||` tending to one, so `xi_k-q xi_k` tends to zero while its image under `e` is `xi_k`.
This is a genuine bounded-operator contradiction.
It proves that `e` is unbounded and, in turn, that neither `t^{-1}` nor `s^{-1}` can be bounded.
It does not purport to show that every affiliated idempotent is a projection.

## 4. All scalar central denominators are legitimate

The two factor gauge automorphisms are trace preserving and send `x` to `u x`, `y` to `v y`; their free-product implementation on centered tensors is valid.
They send `t` to `uv t` and conjugate the represented kernel projections by the implementing unitary.

For a nonzero `lambda`, all points on its circle therefore have eigenprojections of the same trace `delta`.
The repaired MSY23 lemma applied to an arbitrarily large finite collection gives `N delta <= 1`, whence `delta=0`.
Faithfulness rules out the kernel.
The zero parameter is separately covered by the preceding injectivity proof.
No maximal-Delta, normality, orthogonality of eigenspaces, or Brown-measure assertion enters this argument.

A nonzero scalar polynomial factors into linear factors, each now an actual affiliated unit.
Thus every such polynomial in `t` is a unit.
In particular no nonzero polynomial vanishes at `t`, so the injection of `C(z)` is justified before its use as a coefficient field.
Centrality here is only relative to `x,y`; no claim that this nonnormal element is central in the factor is needed.

## 5. Four-dimensional localization and inverse closure

Alternating words are nonzero reduced free-product tensors.
Words of distinct length, or distinct starting factors at a fixed length, are orthogonal; all other nonzero words here reduce to the same alternating list.
This verifies the claimed linear independence.

The identities for even and odd alternating words show spanning over `C[t]` by `1,x,y,xy`.
Independence can be checked without a formal localization assumption: odd lengths separate the coefficients of `x,y`;
at positive even lengths, words beginning with `y` determine the corresponding coefficients of `1`;
the vacuum fixes the constant term;
the remaining even words beginning with `x` determine the coefficient of `xy`.
Clearing a nonzero common polynomial denominator, already a unit by Section 4, preserves this independence over `C(z)`.

Under the displayed map to `M_2(C(z))`, the basis images are

\[
I,\quad E_{12},\quad zE_{21},\quad zE_{11}.
\]

They are linearly independent and span; direct multiplication checks the defining relations.
This is only an algebraic identification.
A singular matrix over the field has a nonzero right kernel vector; putting it in one matrix column produces a nonzero right-annihilated matrix.
Its image in the faithfully embedded localization prevents affiliated invertibility.
An affiliated-invertible element of this localization must therefore have its ordinary field-matrix inverse within the same algebra.
Conversely, each of the four rational coefficients is constructed using actual scalar inverses `Q(t)^{-1}`.
Both inclusions in the asserted closure identity follow, with no use of matrix rational closure in place of scalar division closure.

## 6. The corner argument controls the off-diagonal entry

The first factor's full matrix units identify `M` with `M_2(pMp)`.
The commutation equation with `x=E12` alone forces

\[
t=\begin{pmatrix}c&h\\0&c\end{pmatrix}.
\]

It does not require `c` and `h` to commute.
For a reduced scalar fraction `P/Q`, the diagonal blocks of `Q(t)` are `Q(c)`.
A kernel projection of `Q(c)` embedded in the first coordinate would be a kernel projection of `Q(t)`.
Hence `Q(c)` is injective and affiliated-invertible in the finite corner.

Both left and right multiplication of the triangular inverse

\[
\begin{pmatrix}
Q(c)^{-1}&-Q(c)^{-1}h_QQ(c)^{-1}\\
0&Q(c)^{-1}
\end{pmatrix}
\]

against `Q(t)` give the identity in the affiliated matrix algebra; the displayed order of the three off-diagonal factors is essential and correct.
Multiplication by `x` extracts just `r(c)` as the upper-right entry.
Therefore boundedness of `r(t)x` really does give boundedness of `r(c)`.

For coprime `P,Q`, evaluate `UP+VQ=1` at `c` and multiply on the right by `Q(c)^{-1}`.
All polynomials in `c` commute with this inverse, yielding `Q(c)^{-1}=U(c)r(c)+V(c)`.
The right side is bounded.
Every factor in the off-diagonal expression above is now bounded, so `Q(t)^{-1}` is bounded as a whole.
This rules out the otherwise real gap that bounded diagonal entries alone would not control a nonnormal upper-triangular rational function.
It also proves membership in the bounded scalar division closure, not merely boundedness of `r(t)`.
The second-factor argument for `y` is identical at the stated scope.

## 7. Gauge extraction and exclusion of the final pole

The order-three gauge fixes `t,xy` and gives distinct weights `1,omega,omega^{-1}` to the three groups in the four-coefficient expansion.
Its finite Fourier sums separate `a(t)+d(t)xy`, `b(t)x`, and `c(t)y` as bounded operators.
They do not assume the coefficients are bounded beforehand, and the averaging is used only to infer boundedness; final membership is supplied by the subsequent rational reconstruction.

The corner result gives `b(t),c(t)` in the bounded scalar closure of `C[t]`.
Since `x(a+dxy)=a x`, it also gives `a(t)`.
Subtracting yields bounded `g=d(t)xy`; right multiplication by `x` yields `g x=t d(t)x` with the stated factor order.
The same result for `E(z)=z d(z)` supplies a reduced denominator `Q` for which the actual `Q(t)^{-1}` is bounded.

If `Q(0)=0`, write `Q=zQ_1`; the commutative polynomial factors and the inverse identity give `t^{-1}=Q_1(t)Q(t)^{-1}`, contradicting the already established unboundedness.
Thus the scalar value `eta=E(0)` is legitimate even though `t` is not assumed normal and no functional calculus at a spectral point is being used.
Removing this constant leaves `H=(P-eta Q)/(zQ)`, with its numerator divisible by `z`.
Hence `H(t)` has a bounded scalar inverse representation using the same `Q(t)^{-1}`.

Finally `g=eta e+H(t)xy` is an identity in the affiliated algebra.
Both `g` and the second term are bounded.
If `eta != 0`, their difference would give a bounded representative for `e`, contradicting Section 3.
Thus `eta=0` and the fourth coefficient is reconstructed.
The case `E=0` has reduced representation `0/1` and follows as well.
The proof never multiplies an arbitrary Hilbert vector by an undefined unbounded product.

All four coefficients use bounded scalar inverses of polynomials in `t=xy+yx`, which belongs to the original non-star algebra.
This proves the difficult inclusion.
The reverse inclusion is valid because a bounded inverse is also its unique affiliated inverse.

## 8. Final scope and outstanding maintenance

The result is an independently checked positive instance of T_F0007 for the stated pair of proper non-star two-dimensional algebras.
The full diffuse and arbitrary non-star permanence questions remain open.
The candidate unbounded idempotent is rejected as a counterexample at this model, not used to reject the Task itself.

The whole proof and all actually invoked source interfaces have been checked at the scopes above.
There is no unresolved mathematical dependency.
The display-delimiter correction has been verified and is included in the final reviewed version.
Later mathematical changes require a scoped recheck where appropriate; routine maintenance preserves this review’s actual scope.
