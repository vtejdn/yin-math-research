---
author: Yin
---
# Independent review of bounded transverse singularities and projection arithmetic

Review act: 2026-11-12T01:23, in UTC minutes, for Yin.
The inspected input is the complete working-tree [C_A0012 v4](../../claims/Yin_C_A0012_v4.md), dated 2026-11-12 in Asia/Hong_Kong and unselected during this inspection.
This separately assigned reviewer was outside substantive proof development and received the fixed candidate path, exact review scope, applicable rules and operational work-round facts.
No proof-generation dialogue, development draft, author explanation or mathematical development summary was supplied or consulted.
Initial findings were formed from the entire candidate and its necessary mathematical interfaces before consulting [R_A0038 v3](Yin_R_A0038_v3.md#whole-artifact-finding) or the strategy's prior review conclusions.
Those earlier findings concern their earlier fixed inputs; they do not supply automatic coverage of v4.
No substantive repair was proposed or incorporated, and this reviewer changed no Claim, strategy or assessment.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete artifact](../../claims/Yin_C_A0012_v4.md) | Every stated result, proof step, displayed formula, countertest, finite group-ring construction, trace comparison, source attribution and continuation limitation in this fixed artifact. |
| [Whole-artifact finding](#whole-artifact-finding) | [Statement](../../claims/Yin_C_A0012_v4.md#statement) | The exact bounded semisimple split and compressed derivative hypotheses, punctured-disk inversion, residue, actual contour idempotent, range and finite-trace identity, including absent corners. |
| [Whole-artifact finding](#whole-artifact-finding) | [Argument](../../claims/Yin_C_A0012_v4.md#argument) | The complete bounded Schur calculation and all subsequent tests, exclusions, original-input realization, C*-projection arithmetic, regularization boundary and final conditional chain. |

## Inputs and coverage

The [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract) requires integer unnormalized kernel dimension for every finite rectangular complex group-ring matrix over every torsion-free discrete group, or an actual counterexample.
The present review checks the complete v4 artifact against those quantifiers and confirms that its conditional local theorem is not a completion of that contract.
The exact reused interfaces read were the [v1 compatible-specialization statement](../../claims/Yin_C_A0012_v1.md#statement), the full [v2 arbitrary-kernel singular realization](../../claims/Yin_C_A0012_v2.md#a-compatible-singular-fiber-retaining-an-arbitrary-kernel), and the [v3 square-zero pencil and positive Laurent square](../../claims/Yin_C_A0012_v3.md#a-degree-minimal-symmetric-finite-pencil).
The new use of the transport construction is also verified directly below, without importing an unchecked affiliated inverse.
The [route-five continuation boundary](../../claims/Yin_C_A0007_v5.md#complete-chain-attempt-known-coverage-and-continuation-boundary) and [known-positive-results comparison](../../ledger/Yin_L_A0001_v1.md#known-positive-results) were checked at their stated comparison scopes.
This review is not a new whole-proof audit of unused earlier Claim sections or of the positive-class literature summarized there.

## Bounded split, inverse and logarithmic residue

A bounded idempotent \(e\) gives closed complementary ranges \(e\mathcal H\) and \((1-e)\mathcal H\), with bounded coordinate maps even when the ranges are not orthogonal.
Thus the corner block calculation is valid in the corresponding bounded Banach algebras; it does not require \(e\mathcal M e\) to be a selfadjoint corner.
The identities \(F_0e=eF_0=0\) and invertibility of \(d_0\) identify \(e\mathcal H\) with the complete kernel of \(F_0\).
In particular, equality of the first and second algebraic kernels alone supplies none of the bounded inverse needed here.

Writing \(w:=z-z_0\), the three vanishing blocks at zero give \(b(w),c(w)=O(w)\), so their ordered Schur product is \(O(w^2)\).
Consequently \(s(w)=w h(w)\), with \(h(0)=eF_1e\) a unit in the \(e\)-corner.
Both inversions used in the factorization follow from local norm-convergent Neumann series.
Multiplication of the three displayed factors in (9), in their stated order, recovers every block of \(F(z)\).
Their inverse triangular factors equal the identity modulo \(O(w)\).
Together with \(h(w)^{-1}=a_1^{-1}+O(w)\), this proves that the sole negative Laurent term of \(F(z)^{-1}\) is \(w^{-1}a_1^{-1}\), with holomorphic remainder and the stated \(C/|w|\) estimate.
No unbounded operator or closure of a product occurs.

The residue after multiplication by \(F'(z)\) is exactly \(Q_F=a_1^{-1}F_1\), with the multiplication order retained.
The identities \(eQ_F=Q_F\) and \(Q_Fe=e\) imply \(Q_F^2=Q_F\) and \(\operatorname{ran}Q_F=e\mathcal H=\ker F_0\).
In general this contour idempotent is neither the original \(e\) nor an orthogonal projection; the candidate correctly uses its actual residue.
For its orthogonal range projection \(p_0\), \(p_0Q_F=Q_F\) and \(Q_Fp_0=p_0\), so the off-diagonal difference has trace zero by traciality.
This proves the exact equality with \(\operatorname{tr}(p_0)\), without an integer-valued dimension premise.
The finite trace is bounded, which justifies moving it through the norm integral.
When \(e=0\), ordinary local inversion gives zero residue; when \(1-e=0\), the factorization reduces to \(F(z)=w h(w)\).
The absent-corner conventions therefore include both boundary cases correctly.

## Countertests and excluded encodings

For the two-square test (10), direct multiplication verifies both inverse formulas (11).
The kernel of \(F(0)\) has ordinary dimension one and its complement has a unit restriction, but the compressed derivative is zero.
The Schur expression is \(-w^2\); the logarithmic residue is \(I_2\), of trace two.
Thus the failure concerns the necessary distinction between full derivative invertibility and kernel-corner transversality, even with a genuine initial spectral gap.

For \(A=\operatorname{diag}(0,1-u)\), Fourier transformation gives \(T=\operatorname{diag}(0,2-2\cos\theta)\).
The second multiplier has essential spectrum \([0,4]\) and a Haar-null zero set.
Hence the complete kernel projection is \(\operatorname{diag}(1,0)\), its trace is one, and the positive complementary spectrum approaches zero.
The noninvertible parameters of \(T-(z-1)I\) are exactly \([1,5]\); every sufficiently small circle about one meets them.
The segment meets the unit circle only at one, where the first coordinate gives the stated nonzero kernel.
This verifies all four distinct properties used in the test: torus isolation, compressed derivative invertibility, equality of algebraic kernels and failure of a complex resolvent gap.

For arbitrary \(T=A^*A\), bounded noninvertibility of \(F_A(z)\) is equivalent to \(z-1\in\sigma(T)\).
This proves both directions of (14), including \(T=0\) and boundedly invertible \(T\), and the spectral theorem identifies its gap with (2).
On a nonzero kernel the inverse is \(-(z-1)^{-1}p\), so pointwise bounded inversion is not uniform inversion as the parameter approaches one.

A nonzero square-zero \(N_A\) cannot admit the split (3): its complementary restriction would be simultaneously square-zero and invertible, forcing that corner to vanish and then forcing \(N_A=0\).
For a Laurent positive square \(Q=P^\sharp P\), \(P(\zeta)p_\zeta=0\) and \(p_\zeta P(\zeta)^*=0\) annihilate both terms of the compressed derivative (15).
If the positive operator \(Q(\zeta)\) admitted (3), that idempotent would be its unique Riesz projection at zero, hence the orthogonal kernel projection used in (15).
The calculation therefore excludes the theorem's transversality hypothesis, rather than merely testing an unrelated chosen projection.
The v3 singular kernels are nonzero because their first block has dimension at least one.
For \(A=0\), the unsquared v3 pencil is scalar with simple local roots, and the geometric and contour multiplicities already agree as stated.

## Actual finite transport and trace preservation

The groups \(N=H\times\langle x\rangle\) and \(G=N\rtimes_\sigma\langle t\rangle\) have the asserted embedded coefficient groups and infinite cyclic height quotient.
Any finite-order element has zero height and therefore lies in torsion-free \(N\); this proves torsion-freeness of \(G\).
The finite matrices \(C(x)=T+(1+x)I_n\), \(M=(C\ \ 0)\), \(D=M^*M\) and the \(4n\)-square selfadjoint matrix in (17) all belong to the displayed group rings.
Their identity-specialization row Gram is \((T+2I_n)^2\ge4I_n\), meeting the exact v1 premise independently of the original kernel.

For every torus value \(x\ne-1\), positivity of \(T\) makes \(T+(1+x)I_n\) boundedly invertible.
Its integrated kernel is therefore zero and the complete coefficient kernel is \(p_{\mathrm{gen}}=\operatorname{diag}(0_n,I_n)\).
This constant projection commutes with \(t\).
The height sum \(t+t^{-1}\) is injective by the infinite cyclic Fourier multiplier on subgroup right-coset copies.
The lower equation for the finite block matrix puts its first vector in \(p_{\mathrm{gen}}\); compressing the upper equation forces that vector to zero, and then its second vector lies exactly in \(p_{\mathrm{gen}}\).
This directly verifies the full kernel \(\operatorname{diag}(0_{2n},p_{\mathrm{gen}})\) and trace \(n\).

The coefficient map \(x\mapsto-1\), fixing \(H,t\), respects both the involution and \(txt^{-1}=x^{-1}\).
It is a finite group-ring specialization into the specified direct-product group ring, without an asserted extension to all measurable or affiliated operators.
Its coefficient kernel is separately computed as \(p_-=\operatorname{diag}(p,I_n)\), since \(D_-=\operatorname{diag}(T^2,0_n)\).
In the target group the height generator commutes with \(p_-\), and the same bounded equations give the entire specialized kernel \(\operatorname{diag}(0_{2n},p_-)\).
Canonical subgroup trace preservation yields the exact value \(n+\kappa_A\) with unnormalized matrix trace.
Thus the local contour calculation, when applicable, identifies the existing correction \(\kappa_A\); it does not remove that correction or recover it by evaluating an undefined inverse.

## C*-membership and the remaining arithmetic

For \(R>\|T\|\), functional calculus gives the norm estimate (18) on the positive complementary spectrum, and the approximants equal the identity on the kernel.
Each is a finite group-ring matrix, proving \(p\in M_n(C_r^*(H))\) under the gap.
For this pencil, \(a_1=-p\) and \(F_1=-I_n\), so the actual logarithmic contour idempotent is \(p\).

For the general C*-valued theorem, the split gives the resolvent \((\lambda I-F_0)^{-1}\) the residue \(e\) at zero.
Every ambient bounded inverse of a C*-algebra element belongs to that same unital C*-algebra: positivity and a Neumann series give the inverse of \(X^*X\), and the displayed product gives \(X^{-1}\).
Therefore the resolvent integral puts \(e\) in the C*-algebra.
On \(\operatorname{ran}e\), the equality \(ex=x\) and Cauchy--Schwarz imply \(\|e^*x\|\ge\|x\|\); on its orthogonal complement \(ee^*\) vanishes.
The stated norm-polynomial limit of \(ee^*\) consequently gives its range projection \(p_0\) in the same C*-algebra.
The nonorthogonal case is thus covered without assuming \(e=e^*\).

These membership statements supply no trace arithmetic by themselves.
Condition (19), or its separately justified instance for this actual projection, would supply exactly the missing integer trace on the gapped subclass.
The artifact does not assert that condition for all torsion-free groups or identify it with the complete Task.
For the characteristic-projection test, the explicit inverse of \((1-q)-wI\) gives logarithmic residue \(q\), whose trace is any prescribed \(0<\theta<1\).
All analytic premises hold, while this nontrivial characteristic function is neither a finite Laurent polynomial nor a continuous function on the circle.
The test therefore invalidates a purely analytic integer-winding inference without supplying a group-ring counterexample.

If the original finite support lies in a torsion-free abelian subgroup, it generates a finitely generated group isomorphic to \(\mathbb Z^d\).
The gap is preserved on subgroup regular-representation copies and puts the projection in \(M_n(C(\mathbb T^d))\).
Its continuous integer pointwise rank is constant on the connected torus, so integration and subgroup trace preservation give the claimed integer trace, including the trivial-subgroup case.
The comparison with already controlled abelian and abelian-by-cyclic groups does not assert new coverage of products with arbitrary \(H\).

## Regularization exclusion and source limits

If positive spectral points of \(T\) accumulate at zero, spectral mapping sends a sequence avoiding the finitely many nonzero roots of a nonzero scalar polynomial \(f\), with \(f(0)=0\), to nonzero spectral points of \(|f(T)|\) tending to zero.
Thus a polynomial preserving this kernel cannot create a bounded complementary inverse.
The identically zero polynomial instead changes the complete kernel unless \(T=0\).

A complementary positive gap for \(A^*A\) is equivalent to a lower bound for \(A\) on its kernel's orthogonal complement, and hence to closed range, using the bounded inverse theorem in the converse direction.
The range of \(A\oplus I_k\) is closed exactly when the range of \(A\) is closed.
Bounded invertible right multiplication leaves the range unchanged, and bounded invertible left multiplication preserves its closedness.
This proves the entire stated stabilization and bounded-normalization exclusion for the nongapped example, without claiming to cover every finite group-ring transformation.
An affiliated unbounded inverse does not meet these bounded hypotheses.

The local original [Kat95](../../literature/pdf/Kat95.pdf) was inspected directly: its front matter identifies the 1995 reprint of the corrected 1980 second edition, and printed pp.178--180 correspond to PDF pp.201--203.
I read and visually checked Theorem 6.17, its spectral splitting argument, and formulas (6.27)--(6.34), including the footnote requiring isolation in the spectrum itself.
They support the stated distinction among the spectral idempotent, quasinilpotent part and bounded reduced resolvent.
Kato uses \((T-\zeta)^{-1}\), explaining the minus sign in its contour convention compared with the candidate's explicitly chosen \((\lambda I-F_0)^{-1}\).
No finite-dimensional multiplicity conclusion is imported into finite von Neumann trace, and no original theorem about a transverse parameter pencil is claimed to follow from that source.
The candidate proves its needed Schur and trace identities directly.
No broader source-proof audit, priority search, numerical proof or proof-assistant verification is claimed.
Bounded spectral calculus, Neumann-series inversion, the bounded inverse theorem, finite traciality, Haar integration and subgroup regular-representation decomposition are accepted foundational inputs at their stated scopes.

## Whole-artifact finding

The complete statement and argument of C_A0012 v4 are supported by this independent inspection.
I found no unresolved mathematical defect in the nonorthogonal bounded split, inverse expansion, logarithmic contour idempotent, trace identity, countertests, exclusion of the earlier encodings, finite transport realization, C*-membership arguments or regularization boundary.
The exact original-input chain remains conditional first on a genuine complementary spectral gap and then on an independently justified integer trace for the actual resulting projection.
The first premise fails for the explicit finite torsion-free input (12), and the second is not established here for arbitrary torsion-free groups even on the gapped subclass.
Thus the artifact supplies a valid local theorem and useful precise obstructions, while leaving A0001 unresolved.
This finding concerns the exact v4 artifact and inspected interfaces, selects no Claim assessment or Task decision, and does not extend earlier review findings to different inputs.
