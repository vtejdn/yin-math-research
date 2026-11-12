---
author: Yin
---
# Independent review of symmetric singular fibers and fixed contour data

Review act: 2026-11-11T19:52, in UTC minutes, for Yin.
The inspected artifact is the complete working-tree [C_A0012 v3](../../claims/Yin_C_A0012_v3.md), dated 2026-11-12 in Asia/Hong_Kong, including its statement, every displayed identity, comparisons and final conditional chain.
The Claim was unselected when inspected.
This separately assigned reviewer was outside substantive proof development and received the fixed candidate path, the requested scope, governing instructions and operational work-round facts.
No development draft, proof-generation dialogue, author explanation or mathematical development summary was supplied or consulted.
The reviewer first read the candidate and its necessary fixed mathematical interfaces and formed the initial findings.
Only afterward were [R_A0038 v2](Yin_R_A0038_v2.md#whole-proof-finding) and the applicable scope of [R_A0038 v1](Yin_R_A0038_v1.md#whole-argument-finding) consulted.
Those findings cover their earlier Claim versions, not the new v3 argument automatically.
No substantive repair was supplied and no candidate text was changed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete artifact](../../claims/Yin_C_A0012_v3.md) | Every statement, construction, formula, example, comparison, source limitation and conditional inference in this fixed version. |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0012_v3.md#statement) | Every torsion-free coefficient group and finite rectangular complex input, fixed-size generic and contour data, minimal degree and width, finite transport realization, singular kernels and the stated limit of the inference. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0012_v3.md#argument) | Complete nilpotent, symmetry, contour, homotopy, compatible-specialization and orbit-representation calculations, traces, all-matrix equivalences and the final conditional chain with its unproved premises. |

## Exact obligations and input scope

The original input is an arbitrary torsion-free discrete group \(H\) and \(A\in M_{r,m}(\mathbb CH)\), with \(r,m\ge1\).
Write \(d=r+m\) and \(\kappa_A=\dim_H\ker A\), using the canonical group trace and unnormalized matrix traces.
Independence from the coefficient matrix means independence for fixed \(r,m,q\); it does not identify traces across different matrix sizes.
The [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract) asks for integrality for every such group and rectangular matrix, or an actual counterexample.
The present artifact proves a finite-family construction and a failure of certain proposed inferences, not either completion criterion.

I checked the exact [v2 generic-rank and total-loss statements](../../claims/Yin_C_A0012_v2.md#statement), its finite-corner and companion argument, and the actual specialization and bounded-kernel interfaces of [v1](../../claims/Yin_C_A0012_v1.md#statement).
The prior R findings supply their retained independent whole-proof coverage; this review checks the new applications and does not claim a new whole-proof audit of every unused v1 example.
In the present family generic invertibility and the final finite kernels also have the direct bounded proofs checked below.
The [C_A0011 comparison](../../claims/Yin_C_A0011_v1.md#all-matrix-equivalence-and-exact-comparison-with-previous-work) concerns its existing arbitrary-kernel encoding and is not a premise of the new contour or kernel calculations.
The [L_A0022 rational projection lemma](../../ledger/Yin_L_A0022_v1.md#a-rational-projection-lemma) and [ACSY24 point-spectrum distinction](../literature/ACSY24/Yin_U004.md#point-spectrum-and-brown-atoms) were read at the comparison scopes used here.

## Finite pencil, kernels and minimality

Direct block multiplication gives \(N_A^2=0\), zero unnormalized trace, and
\[
\ker N_A=\ell^2(H)^r\oplus\ker A.
\]
Consequently its complete orthogonal kernel projection is exactly \(\operatorname{diag}(I_r,k_A)\), with dimension \(r+\kappa_A\).
The argument does not assume that \(k_A\) lies in a rational closure.

For \(P_A=fI_d+gN_A\), multiplication in both orders verifies
\[
(fI_d+gN_A)(f^{-1}I_d-gf^{-2}N_A)=I_d
\]
whenever \(f=1+z^q\ne0\).
All operators here are bounded.
The constant and highest coefficients are respectively \(I_d+N_A\) and \(I_d-N_A\), inverse to each other.
At every root of \(z^q=-1\), the pencil is \(2N_A\), so its loss from full generic rank is \(r+\kappa_A\).
Each of the \(q\) roots is genuinely exceptional since \(r\ge1\).
At every point \(z^q=1\), the value is exactly \(2I_d\).

The coefficient automorphism \(x\mapsto\omega x\) preserves the involution because \(\omega\) is unitary.
This automorphism has order \(q\) and fixes the polynomial in \(x^q\).
It fixes \(H\), and for the identity height action it extends while fixing \(t\).
The evaluation identity \(\epsilon_z\alpha=\epsilon_{\omega z}\) has the stated order.
Its action on the \(q\) roots is transitive, and no group-element interpretation of the scalar multiple \(\omega x\) is needed.

Coefficient comparison in a rotation-invariant ordinary polynomial forces every positive exponent occurring to be a positive multiple of \(q\).
Thus \(q\) is the exact minimum degree in that specified class, including \(q=1\).
This does not assert minimality after rational reparametrization or arbitrary stabilization.

On the unit circle the Laurent involution makes \(Q_A=P_A^*P_A\) positive with exactly the same kernel.
Expanding the two factors gives exponents in \([-q,q]\) and highest coefficient
\[
(I_d+N_A)^*(I_d-N_A).
\]
Both factors are units, so that coefficient and its adjoint lowest coefficient are nonzero.
Every nonconstant selfadjoint Laurent matrix invariant under this rotation has an exponent pair \(\pm jq\), with \(j\ge1\).
Its width is therefore at least \(2q\), attained here.
The regular values \(4I_d\) and singular values \(4N_A^*N_A\) follow directly.

## Contours, homotopies and the precise discrepancy

The explicit bounded inverse is uniformly bounded on each fixed circle \(|z|=R\), \(R\ne1\), and on a sufficiently small contour around one root that meets no root.
Differentiation and multiplication leave the scalar term \((f'/f)I_d\) and one multiple of \(N_A\).
The latter has trace zero.
Thus the integrand in (7) is exactly \(d qz^{q-1}/(1+z^q)\).

The scalar geometric-series calculation on the inner and outer circles gives \(0\) and \(qd\), respectively.
At a simple root of \(1+z^q\), the logarithmic derivative has residue one, so the local contour integral is \(d\).
These are direct scalar integral calculations with the unnormalized trace.
They invoke no assertion that an arbitrary operator-valued determinant or winding invariant is integer-valued.

For \(0\le s\le1\), replacing \(N_A\) by \(sN_A\) in the inverse proves that the displayed homotopy stays in the bounded units at every nonsingular parameter.
On a compact loop avoiding the roots it is a norm-continuous homotopy of invertible loops.
All prescribed regular endpoint values remain \(2I_d\).
Consequently any invariant actually preserved by that homotopy takes the same value as for the scalar loop.
The artifact does not claim a classification of such invariants.

The exact total geometric loss is the finite sum \(q(r+\kappa_A)\).
Using \(d=r+m\) and \(\operatorname{rk}_H A=m-\kappa_A\) gives
\[
qd-q(r+\kappa_A)=q\operatorname{rk}_H A.
\]
The v2 bound applies with Laurent exponent interval \([0,q]\) and generic rank \(d\), hence is exactly \(\Delta_A\le qd\).
Its saturation is equivalent to zero rank of \(A\), and faithfulness makes that equivalent to \(A=0\).
No nilpotent term has been discarded from the ordinary kernel: its square-zero generalized kernel is full, while its ordinary kernel has the stated smaller dimension.

For the trivial coefficient group and \(r=m=1\), \(A=0\) and \(A=1\) give defects two and one with the same claimed fixed data.
This directly refutes uniqueness of the geometric defect from those data and equality with the local contour count.
Both defects remain integers.
More generally, integer defect for every member of this family is equivalent to the original all-matrix assertion by subtracting the fixed integer \(r\).
The forward direction uses only that each specialized finite matrix is over \(\mathbb CH\).

## Complete finite transport and singular specialization

For the identity height action, \(N=H\times\langle x\rangle\) and \(G=N\times\langle t\rangle\) are torsion-free.
The matrices \(M_A=(P_A\ \ 0)\), \(B_A=M_A^*M_A\) and \(\mathcal H_A\) have sizes \(d\)-by-\(2d\), \(2d\)-square and \(4d\)-square and finite group-ring entries.
At \(x=1\), the row Gram is exactly \(4I_d\), independently of \(A\).
The v1 certificate therefore applies with row count \(d\), column count \(2d\), one central variable and zero potential.

The finite exceptional set has Haar measure zero.
The direct inverse of \(P_A(z)\) outside that set gives its zero integrated kernel, hence the complete integrated projection for \(M_A\) is \(\operatorname{diag}(0_d,I_d)\).
It is fixed by either identity or inversion action.
This also makes the claimed generic kernel of \(\mathcal H_A\) independently checkable from bounded equations: the lower equation puts the first vector in this constant projection, the compressed upper equation applies the injective \(t+t^{-1}\), and the second vector is then precisely in the coefficient kernel.
Injectivity of \(t+t^{-1}\) follows from the infinite cyclic Fourier multiplier on subgroup right-coset copies.
Thus the entire kernel projection in (12), and its unnormalized trace \(d\), are correct.

For the identity action, each singular evaluation \(x\mapsto\zeta\), fixing \(H,t\), is an actual finite algebra \(*\)-homomorphism.
At that value,
\[
p_\zeta=\operatorname{diag}(I_r,k_A,I_d).
\]
It is the complete separately computed kernel projection of both the evaluated \(M_A\) and its Gram matrix.
It commutes with \(s=t+t^{-1}\).
The bounded lower equation, followed by the \(p_\zeta\)-compression of the upper equation, therefore forces the first vector to zero, and leaves exactly the second-vector kernel \(p_\zeta\).
This proves (14) without applying any unbounded inverse to a vector.
Subgroup trace preservation gives precisely \(d+r+\kappa_A\).
The character symmetry fixes the entire finite matrix and permutes these singular specializations with their equal kernel dimensions.
No integrated measurable projection or undefined rational syntax is evaluated at an exceptional point.

## Genuine inversion action and orbit trace

For \(q=2\), the inversion action on \(x\) is an actual group automorphism fixing \(H\).
A finite-order element in its infinite cyclic semidirect product has zero height and then is trivial in the torsion-free coefficient subgroup.
The prescribed group \(G_-\) is therefore torsion-free.

With \(J=\operatorname{diag}(I_r,-I_m)\), one has \(JN_AJ=-N_A\).
Multiplying out \(z^2JP_A(z^{-1})J\) gives \(P_A(z)\), including the sign of the nilpotent coefficient.
For nonzero \(z\), these scalar and \(J\) factors preserve rank.
Inversion exchanges \(i,-i\), while its two fixed torus points \(1,-1\) both give \(2I_d\).
The generic constant projection and the v1 certificate continue to apply for this \(GL_1(\mathbb Z)\) action.

A scalar evaluation \(x\mapsto i\) with commuting height cannot satisfy the inversion relation.
The orbit representation corrects this by \(X=\operatorname{diag}(i,-i)\), \(t\mapsto uS\), and \(h\mapsto hI_2\).
Directly, \(SXS=X^{-1}\), all group images are unitary, and \(u\) is an independent central infinite cyclic generator.
Thus the map is a genuine finite matrix \(*\)-representation over \(\mathbb C[H\times\langle u\rangle]\).
It is not an extension to arbitrary affiliated operators.

Since \(X^2=-I_2\), both orbit coordinates of the pencil equal \(2N_A\).
The coefficient kernel is exactly two copies of \(p_\zeta\).
The height sum is \((u+u^{-1})S\); its factors commute, the scalar factor is injective, and it commutes with that repeated kernel projection.
The same bounded equations give the full kernel in the \(8d\)-square image, with unnormalized dimension \(2(d+r+\kappa_A)\).
Using the explicitly defined orbit-average trace divides this number by two.
That normalized trace at one orbit is not asserted to equal the canonical trace of \(G_-\), whose integrated kernel has dimension \(d\).
There is no missing trace or representation identification in these calculations.

## Conditional chain, source limits and finding

Transitive symmetry and rank invariance make each exceptional loss equal to \(\Delta/q\).
To infer integer individual losses from a total requires the independently established form \(\Delta=qk\) with integer \(k\).
A total that is merely an integer supplies no divisibility by \(q\), and an upper bound supplies neither fact.

For the actual original-input transformation, the exact algebraic discrepancy is \(q\operatorname{rk}_H A\).
Its arithmetic divided by \(q\) is the original all-matrix arithmetic again.
Thus the first unsupported original-input inference is precisely independent arithmetic control of this correction, or a genuinely kernel-preserving comparison that avoids it.
If an appropriate independently computed geometric total and its divisibility are supplied, (5) or (14) recovers \(\kappa_A\) by subtracting a known integer.
The finite construction itself has no further hidden group, trace or inverse-domain premise.
The candidate explicitly leaves those additional premises unproved and does not assert that another contour invariant or more copies of the orbit will establish them.

The L_A0022 comparison is exact: its commutative rational projection can be specialized after the absence of a pole is proved, and its trace/rank and paired symmetry give an even rank for that same projection.
It does not preserve the kernel of an original singularly specialized matrix.
The ACSY24 U004 source record identifies the published 73-page Advances in Mathematics 443 (2024), article 109595, Section 2.1, printed/PDF pages 11--12.
It supplies the contextual difference between a nilpotent operator's ordinary kernel weight and its Brown atom.
The present proof does not depend on a Brown-measure theorem, and all its needed contour and kernel identities were directly checked here.
No original literature PDF, general foundational proof, historical priority or global invariant classification was newly audited.
Polar decomposition, bounded spectral calculus, faithful finite traces, Haar integration and subgroup regular-representation decomposition are accepted foundational inputs at their stated scopes.
No numerical calculation or proof-assistant verification is claimed.

## Whole-artifact finding

The complete statement and argument of C_A0012 v3 are supported by this independent inspection.
I found no unresolved mathematical defect in its pencil, minimality, contour or homotopy calculations, its exact finite specializations and complete kernels, the genuine order-two orbit representation and trace conventions, or its final conditional chain.
The artifact proves that the specified generic, symmetry, endpoint, degree and contour data do not determine geometric rank loss or force saturation of the total-loss bound.
It retains the full arbitrary coefficient kernel and proves no new group-wide Atiyah case, counterexample or resolution of A0001.
This finding concerns the exact v3 artifact and its stated interfaces; it neither replaces the earlier R versions' different scopes nor selects any Claim assessment or Task decision.
