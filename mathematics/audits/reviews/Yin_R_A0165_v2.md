---
author: Yin
---

# The finite-rank and matrix criteria for the division closure of a group algebra

## Division-closure criterion

At 2026-11-25T07:07 I checked the statement and proof for a finitely generated marked group in its regular representation. [Claim](../../claims/Yin_C_A0131_v2.md#statement)

The block for inversion has scalar Schur complement \(0-\alpha L^{-1}(-\beta)=u\), so its upper left inverse entry is \(u^{-1}\) precisely when the given rational operation is defined.
For the converse, inclusion of the first \(k\) coordinates followed by \(L\) is injective on \(H^k\).
Taking its Gram matrix preserves its kernel.
The trace comparison of initial and final support projections gives an affiliated inverse at every square size.
Each step of the subsequent elimination uses the scalar complement of an already invertible leading block, whose invertibility follows by multiplying by two explicit unit triangular matrices over \(U\).
The inverse of that scalar is available by the definition of division closure even in the presence of zero divisors.
This proves the required converse for pencils with coefficients in the adjoint-closed group algebra.
The block realizations and affiliated trace criterion have the stated source scopes. [Algebraic realization](../literature/MSY23/Yin_U003.md#msy23-u003) and [affiliated invertibility](../literature/MSY23/Yin_U004.md#msy23-u004)

I checked the sides of the common denominators, the vacuum projection and the signs against the fraction commutator in F0001.
For \(v,w\in M\), evaluating on an arbitrary \(\xi\in H\) gives the second term in \([\rho_j,vP_e w]\) as \(v\tau(X_jw\xi)\) with a minus sign.
The indices in the first term contract to \((\eta L)_q\), those in the second to \((Lz)_p\), and scalar entries of \(L_0\) give identical summands.
For the reverse implication, a general witness \(\eta\) has entries in \(L^2\).
Its row equation holds in affiliated matrices because the entries of \(L\) are bounded, so right multiplication by the affiliated inverse there is legitimate.
The range of \(\rho_jT_j\) lies in \(WX_j\), and the range of \(T_j\rho_j\) lies in \(W\).
Evaluating at \(t^*\delta_e\) gives a nonzero scalar coefficient \(-\tau(tt^*)\) on \(a\).
Subsequent left multiplication by \(s^{-1}\) is an identity in the affiliated ring.
The division-ring argument for the unrestricted equation uses a right-linear coefficient functional on the first tensor factor and the canonical left module structure of the second.

For \(G=\mathbb Z\) and its generator \(X\), Fourier transform shows that \(1-X\) is injective and has unbounded affiliated inverse.
With \(u=(1-X)^{-1}\) and \(s=t=1-X\) the construction gives \(a=b=\eta=z=1\) and \(T_1=-P_e\), which solves (1) with precisely the manuscript sign.
For the standard generator of the group of order two, \(u=(1+X)/2\) is a nonunit in the group algebra.
Taking \(s=t=1\), \(T_1=-P_e/2\) and the realization row from the triangular generator pencil gives the required range also in this case.
The equivalence is existential in the common fraction pair and asserts a finite-rank criterion on its specified witnesses.
The proof of (1) alone for a torsion-free group uses the stated division-ring hypothesis or the separate kernel-projection criterion. [Unrestricted equation](../../claims/Yin_C_A0131_v1.md#which-rationality-is-detected)

## Review relationships

| Review | Relationship |
| --- | --- |
| [Division-closure criterion](#division-closure-criterion) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Division-closure criterion](#division-closure-criterion) | [Statement](../../claims/Yin_C_A0131_v2.md#statement) | The pencil and range conditions for every group, the quantified fractions and the original equation under the division-ring hypothesis. |
| [Division-closure criterion](#division-closure-criterion) | [Argument](../../claims/Yin_C_A0131_v2.md#argument) | Block realizations, affiliated scalar pivots, both directions of the finite-rank argument and separation over a division ring. |
