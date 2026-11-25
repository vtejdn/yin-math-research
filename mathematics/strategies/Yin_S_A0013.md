---
author: Yin
---

# Kernel projections and the unrestricted finite-rank equation

## Task associations

| Task | Scope |
| --- | --- |
| [A0003](../tasks/Yin_T_A0003_v3.md#contract) | Decide how far the local commutation condition can be removed for finitely generated torsion-free groups. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Determine when the zero-kernel spectral projection of a bordered group-algebra pencil has its last diagonal coefficient in the division closure. |

## Mechanism and current evidence

The unrestricted equation detects rationality exactly for groups whose division closure contains its scalar kernel projections. [Unrestricted criterion](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected)
It suffices to work with a bounded affine pencil with injective leading block and constant border and to recover one diagonal coefficient of its kernel projection.
The coefficient and the kernel projection of the original scalar rational element determine one another by explicit rational operations. [Corner reduction](../ledger/Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil)
Complete deletion passes in both directions across a finite-index inclusion, which supplies a positive answer for virtually locally indicable groups. [Finite-index transfer](../ledger/Yin_L_A0073_v1.md#ascent-and-descent-of-kernel-projections)

The sharpened finite-rank criterion constructs its test matrix from the fraction and the solution tuple. [Prescribed witness space](../claims/Yin_C_A0131_v4.md#statement)
On the original freely chosen subspace, any sublinear cutoff on the ranks of test operators can be satisfied by adjoining translates along one infinite cyclic subgroup.
An arbitrary tuple can fail the full local condition even for a rational element of the two-torus. [Rank cutoffs and the torus example](../ledger/Yin_L_A0074_v1.md#restricting-the-rank-of-local-test-operators)

## Next investigation

For a bordered pencil \(B\) with last coordinate inclusion \(J\), consider \(J^*\varepsilon(B^*B+\varepsilon I)^{-1}J\) for \(\varepsilon>0\).
Each such compression is rational by scalar Gram elimination and spectral calculus gives strong convergence to the desired coefficient as \(\varepsilon\) decreases to zero.
The unresolved step is an algebraic formula for this particular limit using inverses of affiliated units.
If a nonzero scalar polynomial \(q\) satisfies \(q(B^*B)J=0\), the spectral measure on the range of \(J\) is supported on the finite set of nonnegative roots of \(q\).
Polynomial interpolation gives a scalar polynomial equal to one at zero and zero at every positive root, so applying it to \(B^*B\) and compressing by \(J\) gives the required kernel coefficient in the group algebra.
Group-algebra coefficients can recover the kernel corner for some pencils of infinite spectral support, but a pencil over the free group \(F_2\) has rational kernel corner and admits no such relation of any degree. [Formula and obstruction](../ledger/Yin_L_A0075_v1.md#a-free-group-pencil-with-no-right-polynomial-relation)
For a specified pencil the remaining analytic question is whether its compressed resolvent has a rational expression all of whose inverses are defined at zero. [Regular specialization](../ledger/Yin_L_A0075_v1.md#regular-specialization-of-the-compressed-resolvent)
A single maximal-rank fiber suffices for matrices over a central free abelian direct factor, with the rank loss giving the exact error at every other fiber having a rational kernel projection. [Fiber formula](../claims/Yin_C_A0132_v1.md#argument)
For amenable groups, target finite generation of the right annihilator of a scalar rational element. [Exact algebraic criterion](../claims/Yin_C_A0133_v1.md#the-amenable-case)
Right coherence of the original group algebra suffices, whereas a free-group pencil shows why finitely supported solutions need not span the required kernel outside the amenable case. [Kernel generators](../ledger/Yin_L_A0076_v1.md#amenable-groups-with-a-right-coherent-complex-group-algebra)
For a coamenable subgroup with regular division closure, [finite coset matrices](../claims/Yin_C_A0134_v1.md#lifting-kernel-columns) give positive rational annihilators with ranks approaching the full kernel dimension.
The remaining step is attainment of that rank by one rational annihilator, equivalently the exact finite membership \(p_{\ker x}\in \operatorname{ann}_{D_G}(x)U_G\). [Principal-ideal obstruction](../ledger/Yin_L_A0077_v1.md#the-obstruction-for-one-principal-right-ideal)
In a cyclic quotient the exact rank captured at interval length \(n\) is the increment of its subgroup kernel dimension.
Demanding finite stabilization even on all torsion-free examples of full row rank is equivalent to the universal complex strong Atiyah conjecture. [Exact ranks and obstruction](../claims/Yin_C_A0136_v1.md#statement)
An odd-run scalar in the lamplighter group has a rational kernel projection given by one inverse across all run lengths, and every bounded Laurent width omits positive trace. [Rational odd-run formula](../ledger/Yin_L_A0078_v1.md#a-rational-formula-on-all-odd-runs)
Seek rational inverses that operate across arbitrarily long intervals, taking the finite-dimensional vanishing formulation as a separate route to the full group question.
In that formulation one distinguished value must vanish for solutions of (1), whereas division-closure membership is equivalent to finding a space on which the whole map vanishes.
For every \(k\ge1\), promotion of the distinguished value to rational membership with at most \(k\) auxiliary vectors is equivalent, across finite markings, to rationality of kernel projections of group-ring matrices with \(k\) input columns. [Exact matrix-size comparison](../claims/Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors)
For two columns \(B,w\), use finite group-ring relations \(Z\) with \(\ker Z=\overline{\operatorname{ran}B}\) when available: the remaining scalar to test is \(w^*Z^*Zw\).
For the presentation gradient a positive first \(L^2\)-Betti number precludes such a finite family. [Block reduction](../claims/Yin_C_A0139_v1.md#statement)
Agreement with the regular trace on finite balls, even together with scalar injectivity and exact coordinate subgroup traces, can coexist with a nonrational two-column kernel projection in another representation. [Tracial obstruction](../claims/Yin_C_A0140_v1.md#statement)
In the regular representation a coproduct slice with a positive rational density can already take a rational two-column kernel entry outside the division closure. [Fourier multiplier obstruction](../ledger/Yin_L_A0080_v1.md#a-positive-rational-density-on-the-two-torus)
The remaining intrinsic test admits a formal variable: for \(T=X^*X\), each entry of \(z(T+zI)^{-1}\) is a power series in the scalar division closure over \(\mathbb CG[z]\), with constant term the corresponding kernel entry.
Investigate whether those particular constant terms can be represented by constant series in the same closure, starting with two columns where finite elimination is unavailable. [Constant terms and constant series](../claims/Yin_C_A0141_v1.md#statement)
The [lamplighter encoding](../claims/Yin_C_A0138_v1.md#encoding-the-input-columns) supplies a scalar test for the same kernels at every width, with torsion in the auxiliary factor.
For an additive matrix on an amalgam, use operator-valued free additive convolution to obtain a maximizing edge projection.
When that projection is rational over the edge and both vertex division closures are regular, one Gram inverse recovers the entire kernel and gives an expression for its scaled resolvent defined at zero. [Recovery of the zero atom](../claims/Yin_C_A0142_v1.md#statement)
The central series admit asymptotic evaluation in measure to every order, even in examples where their pointwise sums diverge.
For a pencil \(zI-X\), test stabilization of \(\ker X^m\) to determine whether its analytic inverse at the central shift comes from the formal ring. [Laurent asymptotics](../claims/Yin_C_A0143_v1.md#statement)
In the sofic case a single parameter escaping finite exceptional sets makes two ordinary matrix ranks in the same finite permutation models sufficient for the kernel projection test. [Finite-model witnesses](../claims/Yin_C_A0144_v1.md#statement)
Test whether the scalar case can be lifted by one column over a torsion-free group, analyzing the relative inverse on the kernel left by the preceding columns.
On the original finite-rank witnesses a single positive denominator suffices, while fixing it spectrally or choosing a least-norm solution fails already for the two-torus. [Single denominator](../claims/Yin_C_A0135_v1.md#statement) and [least-norm obstruction](../ledger/Yin_L_A0079_v1.md)
A negative resolution requires proving nonmembership of the actual coefficient for a specified torsion-free group.
The finite-index result excludes proposed counterexamples commensurable with groups already known to admit complete deletion.
