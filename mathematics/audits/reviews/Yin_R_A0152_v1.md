---
author: Yin
---
# Independent review of affiliated ratios and eigenvalue kernels across free factors

## Whole finding

At 2026-11-22T04:13 UTC a reviewer outside the development of C_A0115_v1 independently checked its statement and all three proof sections for Yin, including the final section on iterating with the same coefficient algebra.
The reviewer received the Claim and its scope, without development dialogue, author explanations or a prior verdict on this Claim.
The graph identity holds for nonnormal unbounded inputs, and the stated zero, invertibility and eigenvalue alternatives hold under their respective freeness and coefficient hypotheses.

### The common graph and its trace

For \(x\in L^0(M_1)\), \(s_x=(1+xx^*)^{-1/2}\) has trivial kernel and inverse \((1+xx^*)^{1/2}\) in the affiliated algebra.
The polar decomposition gives a bounded extension of \(s_xx\) with norm at most one, and \(s_x(xx^*+1)s_x=1\) makes the bounded row \(L_x\) a coisometry.
The common kernel of the two bounded rows on \(U^2\) consists precisely of \((v,xv)^t\) for \(v\in\ker_U(x-y)\), as left multiplication by \(s_x\) or \(s_y\) can be canceled in \(U\).
The graph map and the first coordinate are inverse right-module maps.
Each kernel is the module of its kernel projection by polar decomposition, and isomorphic finite projection modules have equal trace dimension.
This gives the required equality of nullities without identifying a vector in the domain of a closed difference with a vector in the domains of both original operators.

In [the two-row formula](../../claims/Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel), the proof of (4) and its maximality use only the freeness of the two matrix algebras over the matrix algebra of constants and the trace-preserving expectation.
For the present freely independent subalgebras the entrywise trace gives that expectation, and expansion of each centered alternating matrix product verifies the required freeness.
Both rows have rank one, so projections of rank zero and two give zero in the maximum.
The vertical line gives \(1-1-1=-1\).
On the line \((1,\lambda)^t\), the restricted \(x\)-row is a nonzero scalar multiple of \(s_x(x-\lambda)\), of rank \(1-\nu(x-\lambda)\), and the same calculation applies to \(y\).
All constant lines occur in this list, giving (1) with the positive part, even if every eigenspace in one factor is trivial.

### Affine denominators and scalar equality

In the group case reduced alternating words have zero identity coefficient, giving freeness of the vertex group algebras and hence their von Neumann closures in the regular representation.
For \(a\ne0\), multiplication by the unit \(a\) identifies the point kernel of \(a^{-1}b\) at \(\lambda\) with the kernel of \(b-\lambda a\).
The latter element belongs to the original coefficient algebra \(D_j(H_1)\), so it is zero or a unit under \(P_j(H_1)\).
Thus a ratio either is scalar or has zero kernel at every scalar.
For \(c\ne0\), applying (1) to the two ratios gives nullity one precisely when both equal the same scalar, and zero otherwise.
With \(x=a^{-1}b\) and \(y=c^{-1}d\), the Schur complement is \(c(y-x)\).
For \(c=0\) the complement is \(d\), with the zero case exactly the zero second row.

If \(E\) is a unit in the coefficient factor, \(Ew+F=E(w-(-E^{-1}F))\) is a unit by (1) and the absence of point kernels for \(w\).
If \(E=0\) the affine expression is \(F\).
Applied first to the nonzero denominator row and then to \((A-\lambda C,B-\lambda D)\), this proves (2) and its asserted coefficient-span extension.
Right multiplication by the denominator preserves rank since it is an affiliated unit.
The infinite-order group unitary has Haar spectral law, and a nonconstant output remains point-kernel-free when used against an additional free factor in a joint free product.

### Iteration over the same coefficient algebra

For a defined prefix \(pq^{-1}\), the next denominator in the expression before clearing is \((Cp+Dq)q^{-1}\), so its invertibility is equivalent to that of \(Cp+Dq\).
Clearing on the right gives \((Ap+Bq)(Cp+Dq)^{-1}\).
Stacking the two coefficient rows of the cleared fraction gives the new update matrix times the previous prefix matrix.
They stay in \(D_j(H_1)^2\).
Testing each bottom row against the original \(w\) proves the prefix criterion, including a prefix following a scalar output.
Testing the top row minus \(\lambda\) times the bottom row proves the scalar criterion and the absence of all point kernels in the other case.
For a continued-fraction update \(\left(\begin{smallmatrix}0&1\\A_i&B_i\end{smallmatrix}\right)\), the equations \(v=h,\ A_i u+B_i v=k\) have unique solution \(u=A_i^{-1}(k-B_i h)\), \(v=h\).
The products are invertible over the affiliated algebra, so their bottom rows are nonzero and their top rows cannot be complex multiples of their bottom rows.
The conclusions therefore hold at every finite prefix with no freeness assumption between successive coefficient matrices.
The reviewed argument uses the two-row maximization theorem as an established input and gives the stated result for expressions with a common original free variable in the two rightmost affine forms.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0115_v1.md#statement) | General affiliated eigenvalue-kernel identity, two free-factor Schur and affine ratio alternatives, and all finite prefixes. |
| [Whole finding](#whole-finding) | [Two bounded graph rows](../../claims/Yin_C_A0115_v1.md#two-bounded-graph-rows) | Affiliated graph modules, matrix freeness and maximization over all constant projections. |
| [Whole finding](#whole-finding) | [A step from one inverse layer to the next](../../claims/Yin_C_A0115_v1.md#a-step-from-one-inverse-layer-to-the-next) | The ratio point-kernel dichotomy, singular rows, coefficient-span version, group examples and fresh-factor iteration. |
| [Whole finding](#whole-finding) | [Reusing one coefficient algebra](../../claims/Yin_C_A0115_v1.md#reusing-one-coefficient-algebra-through-arbitrary-inverse-depths) | Ordered prefix multiplication, exact denominator and scalar criteria, and nonsingularity at every finite continued-fraction step. |
| [Whole finding](#whole-finding) | [Two-row maximization](../../claims/Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) | Formula (4) and maximality for arbitrary bounded rows over the two free subalgebras, with scalar amalgamation. |
