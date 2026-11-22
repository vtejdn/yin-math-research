---
author: Yin
---
# Affiliated ratios and eigenvalue kernels across two free factors

## Statement

Let \(M_1,M_2\) be freely independent von Neumann subalgebras in a finite tracial von Neumann algebra \(M\) with faithful normalized trace.
For an affiliated scalar \(x\), write \(\nu(x)\) for the trace of its kernel projection.
Given arbitrary \(x\in L^0(M_1)\), \(y\in L^0(M_2)\), one has
\[
 \nu(x-y)=\sup_{\lambda\in\mathbb C}
          \bigl(\nu(x-\lambda)+\nu(y-\lambda)-1\bigr)_+ .              \tag{1}
\]
The trace concerns actual eigenspaces and allows unbounded nonnormal operators.
This is a two-column application of the [free graph projection formula](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel).

In a regular group representation one may take \(M_i=\mathcal N(H_i)\) for two subgroups whose natural free product embeds in the given group.
Suppose \(P_j(H_i)\) holds at a specified inverse depth, meaning that every nonzero element of \(D_j(H_i)\) is an affiliated unit.
If \(a,b\in D_j(H_1)\), \(c,d\in D_j(H_2)\) and \(a\ne0\), then \(d-ca^{-1}b\) is either zero or an affiliated unit.
It vanishes precisely when the second row is zero or \(b=\lambda a,\ d=\lambda c\) for some complex scalar \(\lambda\).
This applies even when \(a^{-1}\) first appears at depth \(j+1\).

There is a second application with repeated coefficients from one factor.
Let \(w\in L^0(M_2)\) satisfy \(\nu(w-\lambda)=0\) for every \(\lambda\in\mathbb C\).
Take \(A,B,C,D\in D_j(H_1)\) under \(P_j(H_1)\) and \((C,D)\ne(0,0)\).
Then \(Cw+D\) is a unit and
\[
             z=(Aw+B)(Cw+D)^{-1}                                      \tag{2}
\]
has no eigenvalue of positive kernel dimension unless \((A,B)=\lambda(C,D)\) for a complex scalar \(\lambda\), in which case \(z=\lambda\).
The same conclusions hold for arbitrary coefficient scalars in \(L^0(M_1)\) when each nonzero member of \(\operatorname{span}_{\mathbb C}\{A,C\}\) and of \(\operatorname{span}_{\mathbb C}\{B,D\}\) is an affiliated unit.
Under \(P_j(H_1)\), one may compose arbitrarily many transformations (2) using coefficients from the **same** \(D_j(H_1)\) and the same initial \(w\).
For each prefix multiply its two-by-two coefficient matrices in order, with the latest transformation on the left.
Starting with the identity prefix, evaluation succeeds exactly as long as the bottom row of each prefix product is not the zero row.
The output of each defined prefix is scalar precisely when its top row is a complex multiple of its bottom row, and otherwise has no eigenvalue of positive kernel dimension.

## Two bounded graph rows

Work first on right modules over \(U=L^0(M)\), where kernels of affiliated matrices are projection modules with the trace dimensions of their Hilbert kernels.
Set \(s_x=(1+xx^*)^{-1/2}\) and form the bounded row \(L_x=(s_x x,-s_x)\), and likewise \(L_y\).
Here \(s_x\) is an affiliated unit, \(s_xx\) is a contraction by polar decomposition and \(L_x L_x^*=1\).
The kernel of \(L_x\) on \(U^2\) consists of the columns \((v,xv)^t\).
The common kernel of the two rows is isomorphic to \(\ker_U(x-y)\) through its first coordinate, so it has dimension \(\nu(x-y)\).
All operations with the two original variables in this argument use closed affiliated products.

Use the [two-row maximization formula](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) over the common scalar algebra.
Its proof applies to any two bounded rows in the free vertex algebras, through the freeness of their matrix amplifications over \(M_2(\mathbb C)\).
It gives the common kernel dimension as the maximum of
\[
            \operatorname{Tr}_2 Q-\operatorname{rk}(L_xQ)
                                  -\operatorname{rk}(L_yQ)
\]
over constant orthogonal projections \(Q\in M_2(\mathbb C)\).
Ranks zero and two for \(Q\) give value zero, and the vertical line gives value \(-1\) since \(s_x,s_y\) have full scalar rank.
On the line spanned by \((1,\lambda)^t\), the restricted rows have ranks \(1-\nu(x-\lambda)\) and \(1-\nu(y-\lambda)\).
Taking the maximum gives (1).

## A step from one inverse layer to the next

If \(a\ne0\), the point kernels of \(x=a^{-1}b\) are those of \(b-\lambda a\), by multiplication on the left by the affiliated unit \(a\).
Under \(P_j(H_1)\) these dimensions are zero for every \(\lambda\), unless \(b=\lambda a\) and \(x=\lambda\).
Exactly the same dichotomy holds for \(y=c^{-1}d\) when \(c\ne0\).
In that case \(d-ca^{-1}b=c(y-x)\), and (1) implies the claimed alternative and its vanishing criterion.
For \(c=0\) the complement equals \(d\), covering the remaining case.
The freeness assertion for group von Neumann algebras follows by the reduced word theorem and the identity-coefficient trace, followed by bounded approximation.

For (2) use the following consequence of (1).
If \(E,F\in L^0(M_1)\) and \(E\) is a unit, then \(Ew+F\) is injective because \(w\) has no point kernel and \(E^{-1}F\) belongs to the other algebra.
If \(E=0\), the conclusion is determined by \(F\).
This proves invertibility of the denominator.
For each complex \(\lambda\), right multiplication of \(z-\lambda\) by \(Cw+D\) gives
\[
                (A-\lambda C)w+(B-\lambda D).
\]
Its rank equals that of \(z-\lambda\).
The hypotheses make it a unit whenever at least one of the two coefficients is nonzero, giving (2).
For example, \(w\) can be any nonconstant \(D_j(H_2)\) input if \(P_j(H_2)\) is known.
One can also take a single infinite-order group element for \(w\) at any depth without assuming \(P_j(H_2)\), since its regular cyclic spectral law is Haar.
After constructing a nonconstant output it can serve as the input \(w\) for another operation (2) with coefficients from a fresh free factor.
To justify the iteration, the output is affiliated with the algebra generated by the factors already used, which is free from the new factor in a joint free product.

## Reusing one coefficient algebra through arbitrary inverse depths

Write \(p=Ew+F,\ q=Jw+K\) for a previous prefix whose denominator \(q\) is a unit.
For another matrix \(\left(\begin{smallmatrix}A&B\\ C&D\end{smallmatrix}\right)\) over the same \(D_j(H_1)\), applying (2) to \(p q^{-1}\) gives
\[
           (A p+B q)(C p+D q)^{-1}
\]
whenever the new denominator is a unit, because the actual denominator before clearing is \((C p+D q)q^{-1}\).
The coefficients of \(C p+D q\) are \(CE+DJ,CF+DK\), the two entries in the bottom row of the prefix product.
Both are still in \(D_j(H_1)\).
The one-step result for the **original** \(w\) shows that this denominator is a unit exactly when that row is nonzero.
Applying the same calculation to the numerator minus a complex multiple of the denominator proves the prefix assertions, starting with \(w=(1w+0)(0w+1)^{-1}\).
No inverse of a prefix coefficient matrix is required.
For example, the continued fraction obtained by repeatedly replacing an output \(v\) by \((A_i v+B_i)^{-1}\), \(A_i\ne0\), has no singular denominator for any finite number of steps.
Each update has coefficient matrix \(\left(\begin{smallmatrix}0&1\\ A_i&B_i\end{smallmatrix}\right)\), invertible over the ambient affiliated algebra, so every product has two independent rows there and its output remains nonscalar.
Thus every output has zero kernel, although the displayed expressions have arbitrarily many nested inverses and repeatedly use the same coefficients.
The argument uses the presence of one free initial input which occurs in both affine forms in a common rightmost position.
General expressions with repeated internal occurrences of that input need not have such a two-row representation.

## Assessment history

### Decision point-kernels-in-free-factors

| Field | Value |
| --- | --- |
| date | 2026-11-22T04:17 |
| status | proved |
| reason | Independent review verified the full argument at the stated hypotheses and bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Point kernels of differences of free affiliated scalars, the first Schur step with free row factors, and arbitrary finite fractional linear iterations. |
| argument | [Proof](#two-bounded-graph-rows) | The bounded graph rows, the constant projection maximum, original eigenvalues and ordered prefix denominators. |
| review | [Whole finding](../audits/reviews/Yin_R_A0152_v1.md#whole-finding) | Independent whole-argument finding for the stated scope. |

## Current assessment

[Selected decision](#decision-point-kernels-in-free-factors)
