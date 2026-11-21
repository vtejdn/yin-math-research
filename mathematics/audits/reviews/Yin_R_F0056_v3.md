---
author: Yin
---

# Independent review of the quadratic selfadjoint counterexample

Review act: 2026-11-21T14:54 UTC.
The human record author is Yin.
This is an initial independent inspection of the complete statement and argument of [Yin_C_F0012_v3](../../claims/Yin_C_F0012_v3.md#statement), together with its comparison against the selfadjoint test branch of [Yin_T_F0003_v2](../../tasks/Yin_T_F0003_v2.md#contract).
The inspected working revision uses \(X_h=h,X_1=Y_1,X_2=Y_2\) and \(i,j\in\{h,1,2\}\) in the statement of the dual relations.

The reviewer was separately assigned, did not participate in substantive development of this construction, and received the fixed proof, its necessary dependencies, the actual human requirements and the review scope.
No development dialogue, exploration draft, proposing-agent explanation or prior review conclusion for this construction was supplied or consulted.
The reviewer read the fixed v3 statement and argument, inspected the needed v1 Fock-model and scalar-dual arguments and the original sandwich construction for comparison, and formed the findings below directly.
Historical review links and assessments appearing in the v1 claim were not used as proof evidence, and the linked reviews were not opened.
The sole external analytic input was checked against the author's original Hilbert-transform notes as specified below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete example](#quadratic-selfadjoint-finding) | independently reviewed |
| [Comparison and Task scope](#branch-comparison-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete example](#quadratic-selfadjoint-finding) | [Exact statement](../../claims/Yin_C_F0012_v3.md#statement) | All hypotheses, three selfadjoint generators, whole-space bounded duals with the stated bounds, generation, both affiliated witnesses, both norm-distance bounds and matrix rational nonmembership. |
| [Complete example](#quadratic-selfadjoint-finding) | [Complete argument](../../claims/Yin_C_F0012_v3.md#argument) | The entire coloured tracial model, bounded-operator construction, scalar analytic interface, affiliated identities and norm-separation proof. |
| [Complete example](#quadratic-selfadjoint-finding) | [v1 tracial model](../../claims/Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) | The model argument used by v3, including its explicitly checked two-colour extension; no adoption of v1's other conclusions through this row. |
| [Complete example](#quadratic-selfadjoint-finding) | [v1 scalar construction](../../claims/Yin_C_F0012_v1.md#3-a-bounded-dual-for-h-and-its-bounded-correction) | Hilbert-transform normalization, weighted conjugation and last-factor extension, checked with v3's density and its own correction. |
| [Comparison and Task scope](#branch-comparison-finding) | [v3 comparison](../../claims/Yin_C_F0012_v3.md#comparison-and-remaining-question) | Degree and dual-construction simplification, increased generator count and the unresolved two-generator question. |
| [Comparison and Task scope](#branch-comparison-finding) | [Original sandwich statement](../../claims/Yin_C_F0012_v1.md#statement) | The comparison pair \((h,hbh)\), its two selfadjoint generators and cubic degree in \(h,b\); not a new whole-proof review of v1. |
| [Comparison and Task scope](#branch-comparison-finding) | [Original merging operator](../../claims/Yin_C_F0012_v1.md#2-a-bounded-last-two-factor-operator) | The triangular two-factor kernel estimate used for the concrete comparison with v3's single last-factor functional. |
| [Comparison and Task scope](#branch-comparison-finding) | [Current Task contract](../../tasks/Yin_T_F0003_v2.md#contract) | Only the incorporated selfadjoint bounded-dual test branch and its relation to the main sufficient-condition objective; no general Task completion or earlier completion-chain finding. |

## Complete example

<a id="quadratic-selfadjoint-finding"></a>

The complete v3 statement and argument are mathematically supported.
No unresolved gap was found in the inspected construction or its necessary interfaces.
The decisive checks are as follows.

### Standard tracial space

The two displayed linear combinations of \(\ell_1,\ell_2\) are orthonormal creations.
Their sums with their adjoints therefore have variance-one semicircular laws; the centred Wick-word calculation gives their mutual freeness and freeness from the first-factor copy of \(L^\infty(\mu)\).
This supplies the claimed circular normalization of \(z=\ell_1+\ell_2^*\), including \(\|z\|\le2\) and \(\|z\Omega\|=\|z^*\Omega\|=1\).
Products of bounded scalar factors separated by choices of \(z\) or \(z^*\) have arbitrary prescribed elementary tensors as their highest-grade terms, because their creation terms have colours 1 and 2 respectively.
Induction on grade proves vacuum cyclicity on the whole displayed Hilbert direct sum.

For the proposed right operators, \([z,r_1+r_2^*]=0\); the two grade-zero defects in \([z,r_2+r_1^*]\) are \(-P_\Omega\) and \(+P_\Omega\).
They cancel, and the analogous adjoint identities hold.
Left scalar multiplication also commutes with the proposed right generators, including the grade-zero boundary.
The right vacuum orbit is dense by the mirrored highest-grade argument, so the vacuum is separating for the left von Neumann algebra.
The reversal antiunitary, with function conjugation and colour exchange, sends left multiplication by each generator to right multiplication by its adjoint.
Commutation of the left and right actions then gives \(Jx\Omega=x^*\Omega\) for every generator polynomial.
The equality of their norms gives the trace identity by polarization and normal extension; separation gives faithfulness.
Thus the model is the whole standard \(L^2(M,\tau)\), and its right operators are the actual bounded right multiplications.

### Bounded duals and signs

The computation \(\|q\|_2^2=3\) uses the stated probability density \(3t^2\).
The operator \(K_q\) is a direct sum of last-factor contractions with norm \(\sqrt3\), and its adjoint appends \(e_2\otimes q\).
Both are bounded on the entire space.
Their commutation with left \(h\) includes grade one, since that operation retains the first scalar factor.

On grade zero, \([K_q,\ell_j]=\delta_{j2}|\Omega\rangle\langle q|\).
On positive grades the prefix creation and last-factor contraction commute.
For \([K_q,\ell_j^*]\), both orders vanish on grades zero and one; on every higher grade they contract the opposite ends, with the same colour tests.
Taking adjoints consequently gives the minus sign in \([K_q^*,z]=-|q\rangle\langle\Omega|\).
Using the vector identity \(hq=1\) gives
\[
 [K_q^*,u]=-P_\Omega,\qquad [K_q,u^*]=P_\Omega,
 \qquad [K_q,u]=[K_q^*,u^*]=0.
\]
These are bounded-operator calculations and do not use an unbounded multiplier by \(q\).

For the scalar analytic input, the normalized real-line Hilbert transform has multiplier \(-\mathrm i\operatorname{sgn}\), as stated in [Tao06, equation (1), Proposition 1.2 and its following \(L^2\) extension, pp. 1, 3–4](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf).
Zero extension from \((0,1)\) followed by restriction shows that the kernel \(1/(t-s)\) used here is the compression of \(-\pi H\), with norm at most \(\pi\).
This inspection checks the classical theorem's exact normalization and applicability, rather than claiming a new full audit of those lecture notes.

The map \(W\xi=\sqrt w\xi\) is unitary to unweighted \(L^2\), and \(\|\sqrt w\|_\infty^2=3\), so the scalar operator has norm at most \(3\pi\).
For compactly supported smooth \(\xi\), its weighted integral kernel gives
\[
 (D_0h-hD_0)\xi
 =\int_0^1\xi(t)\,d\mu(t)\,1.
\]
Density extends this bounded identity to all of \(K\).
The last-factor extension commutes with both creations and annihilations, including the grade-zero and grade-one cases, while its commutator with left \(h\) is precisely \(P_\Omega\).

The correction in v3 cancels the two defects separately:
\[
 [E_h,u]=P_\Omega z-P_\Omega\rho(z)=0,
 \qquad
 [E_h,u^*]=z^*P_\Omega-\rho(z^*)P_\Omega=0.
\]
The first vacuum identity uses traciality and the second uses equality of the left and right vectors at \(\Omega\).
For the other two duals,
\[
 \begin{array}{c|cc}
  &u&u^*\\ \hline
 [E_1,\,\cdot\,]&P_\Omega&P_\Omega\\
 [E_2,\,\cdot\,]&\mathrm iP_\Omega&-\mathrm iP_\Omega
 \end{array}
\]
gives every diagonal and off-diagonal relation for \(Y_1,Y_2\).
The final substitution \(D_i=-E_i\) gives exactly the requested generator-first convention.
The norm estimates are \(3\pi+2\|z\|\sqrt3\le3\pi+4\sqrt3\) for \(D_h\), and \(2\sqrt3\) for each remaining dual.

### Generation and affiliated membership

The identity \(u=Y_1+\mathrm iY_2\) places \(u\) in the polynomial algebra.
Since \(h\) has zero kernel, the bounded spectral cutoffs used in the proof recover \(z\) as a uniformly bounded strong limit inside \(W^*(X)\).
This proves equality with \(M\), rather than bounded-dual existence only on a larger ambient space.

In the algebra of affiliated operators, \(h^{-1}h=1\) and \(h(h^2)^{-1}h=1\).
Associativity there therefore gives both displayed identities \(h^{-1}u=z\) and \(u^*(h^2)^{-1}u=z^*z\).
The latter inverse need not be an \(L^2\) operator or a bounded operator; neither property is used.
Both expressions use scalar inverses and hence belong to the affiliated matrix rational closure, and their values are bounded, with the second value positive.

### Norm separation and all matrix representations

The small spectral projection has trace \(\varepsilon^3>0\), so the displayed \(\xi_\varepsilon\) is a unit vector and \(\|h\xi_\varepsilon\|\le\varepsilon\).
The append map is an isometry on the direct sum.
Its only defect with \(z\) is the colour-2 contraction on grade zero, exactly \(|\xi_\varepsilon\rangle\langle\Omega|\); it has no defect with \(z^*\) or left \(h\).
Consequently it asymptotically commutes in norm with \(h,u,u^*\), then with every fixed polynomial, and finally with every element of \(C^*(X)\) by the uniform bound \(\|[a,V_\varepsilon]\|\le2\|a\|\).

The range of \(V_\varepsilon\) is orthogonal to grade zero, while the defect of \(z\) has its range there.
Compression by \(1-V_\varepsilon V_\varepsilon^*\) therefore retains a norm-one defect and gives \(\operatorname{dist}(z,C^*(X))\ge1\).
For \(f=z^*z\), the identity \(z^*\xi_\varepsilon=V_\varepsilon\Omega\) gives \([f,V_\varepsilon]=V_\varepsilon P_\Omega\), also of norm one.
The commutator estimate then gives \(\operatorname{dist}(f,C^*(X))\ge1/2\).
These checks cover both constants and all \(a\) in the norm closure, not merely the displayed rational expressions.

Finally, for every finite \(n\), a matrix over the unital C*-algebra \(C^*(X)\) that is invertible in \(M_n(M)\) has its inverse in \(M_n(C^*(X))\).
Indeed, the positive lower bound on its adjoint square gives the inverse of that square by a norm-convergent Neumann series after rescaling, and multiplication by the adjoint gives the matrix inverse.
Thus \(\operatorname{Rat}_M(A)\subset C^*(X)\) for the full matrix rational closure.
The two norm-distance estimates exclude every bounded matrix rational representation of either witness and establish the claimed failure of the bounded rational-closure equality.

## Comparison and Task scope

<a id="branch-comparison-finding"></a>

The comparison is supported at the exact stated scope.
The original pair \((h,hbh)\) has two selfadjoint generators and maximum degree three in the two elementary free inputs \(h,b\).
The new tuple has three selfadjoint generators and maximum degree two in the three elementary free inputs \(h,b_1,b_2\).
Its dual construction replaces the old triangular two-factor kernel estimate by one bounded last-factor functional and its adjoint, together with the explicitly checked scalar-dual correction.
These are concrete simplifications under the alternatives allowed by the selfadjoint test branch.
They do not establish a reduction in generator count or a universal ordering of the complexity of the two examples.

The tuple meets that branch's requirements of selfadjointness, bounded duals on the whole standard space, generation, a bounded affiliated rational witness and exclusion of every bounded matrix rational representation.
Discarding \(h\) would discard the currently proved rational witness formulas; no argument here establishes their affiliated rational membership for the smaller two-generator algebra.
The review therefore supports this specific three-generator simplification while leaving the simpler two-generator search open.

No sufficient-condition theorem for the general equality is proved or reviewed here.
The general objective of Yin_T_F0003_v2, its retained scalar-closure question, its other model-specific obligations and the earlier pending completion-chain inspection remain outside this review's completion scope.
This finding does not select a Claim assessment or a Task lifecycle decision; those adoptions belong to their responsible materials.
No historical priority, numerical experiment or formal verification is asserted.
