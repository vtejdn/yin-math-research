---
author: Yin
---

# Testing an affiliated fraction by mixed trace moments

## Statement

Let \(M=\mathcal N(G)\) for a discrete group \(G\), let \(U=L^0(M)\), and write \(D_G\) for the division closure of \(\mathbb CG\) in \(U\).
Given \(u=b_0t_0^{-1}\) with \(b_0,t_0\in M\) and \(t_0\) an affiliated unit, one can test \(u\in D_G\) using mixed trace moments of these two bounded operators and group elements.
The same test applied to a rectangular \(X\in M_{a,k}(\mathbb CG)\) detects whether the kernel projection of \(X\) has entries in \(D_G\).
For this latter test each individual moment is obtained by group-ring multiplication and extraction of the identity coefficient.

Choose \(h\ge1\) and a finite \(F\subset G\) containing the identity.
Use matrices \(L,\alpha,\beta\) with entries in the span of \(F\), with \(L\) of size \(h\times h\).
Assemble the following bounded matrix \(J\) in the chosen test.

| Input | Size of \(\alpha,\beta\) | \(J\) | Number \(s\) of columns after the pivot |
| --- | --- | --- | --- |
| Fraction \(b_0t_0^{-1}\) | \(1\times h,\ h\times1\) | \(\begin{pmatrix} L&\beta t_0\\ \alpha& b_0\end{pmatrix}\) | \(1\) |
| Matrix \(X\) | \(k\times h,\ h\times a\) | \(\begin{pmatrix} L&\beta X\\ X\alpha&X\end{pmatrix}\) | \(k\) |

Let \(T\) be the compact product of closed complex unit disks for the group coefficients of these three matrices, and choose one \(C>0\) bounding the operator norms of \(L\) and \(J\) throughout \(T\).
For a bounded matrix \(B\) from either family use the ordinary unnormalized matrix trace together with the group trace and put
\[
       H_n(B)=(\operatorname{Tr}\otimes\tau)((I-B^*B/C^2)^n).
\]
The criterion, in either row of the table, is that some \(h,F\) give
\[
       \lim_{n\to\infty}\lim_{m\to\infty}
       \min_{T}\max\{H_n(L),\,s-H_m(J)\}=0.                         \tag{1}
\]
Equivalently, for every integer \(j\ge1\) there is an \(n\ge1\) such that for every \(m\ge1\) there are coefficients in \(\mathbb Q(i)\) in the same disks for which both quantities inside the maximum are strictly less than \(1/j\).
Only the orders and coefficients can vary in these tests once \(h,F,C\) are chosen.
The order of the limits is necessary.
Taking the \(n\)-limit first gives zero on every input whenever \(h\ge s\).

## Argument

### Compactness for bounded moments

Let \(r(B)\) denote the unnormalized von Neumann rank and let \(\nu(B)\) denote the number of columns minus \(r(B)\).
The positive contractions \(I-B^*B/C^2\) have powers decreasing strongly to the kernel projection of \(B\), so \(H_n(B)\downarrow\nu(B)\) by normality of the trace.
This is the mass at zero in the spectral measure of \(B^*B\) for the unnormalized trace, or equivalently the trace of the constant coefficient of \(z(z+B^*B)^{-1}\) in its affiliated expansion at zero. [The two resolvent expansions](Yin_C_A0160_v1.md#the-two-expansions-of-the-resolvent)
At finite order the moment is a real polynomial in the real and imaginary coefficient coordinates, with constants given by traces of bounded products.

Fix \(n\).
As \(m\) increases, the continuous objective on \(T\) increases pointwise to \(\max\{H_n(L),r(J)-h\}\).
Its minima increase to the minimum of that limit.
Indeed, if \(d\) is the limit of the minima, the closed sublevel sets at \(d\) of these continuous objectives are nonempty and nested in compact \(T\).
A point of their intersection has limiting objective at most \(d\), and every point has limiting objective at least \(d\).
Next the infimum over \(n\) commutes with the infimum over the coefficients.
Taking the decreasing limit in \(n\) therefore gives
\[
                d=\inf_T\max\{h-r(L),\,r(J)-h\}.                    \tag{2}
\]
For the quantified form, the minimum at each finite \(n,m\) equals the infimum on the dense rational-complex coefficients.
Zero in (1) permits choosing \(n\) so that the inner limit is less than \(1/j\), and then approximating the finite minima with strict slack.
In the reverse direction the quantified inequalities bound the inner limit by \(1/j\) for the chosen \(n\).
Nonnegativity of \(H_n(L)\) finishes the implication.

### Attainment of the rank infimum

The infimum in (2) is attained even when it is positive.
First allow arbitrary complex coefficients.
Scaling \(L,\alpha,\beta\) to \(c^2 L,c\alpha,c\beta\) with \(0<c\le1\) brings any tuple into the disks without changing either rank.
Indeed this multiplies \(J\) on the left and right by invertible scalar block diagonals with first block \(cI_h\).
Thus the infimum on the complex affine parameter space equals the one on \(T\).

The sets \(V_j=\{r(J)\le h+d+1/j\}\) are Zariski closed by the [rank sublevel theorem](Yin_C_A0128_v1.md#statement), since \(J\) is polynomial in the complex coefficients with bounded operator coefficients.
These descending algebraic sets stabilize by Noetherianity of affine space. [Hilbert basis theorem](Yin_C_F0091_v1.md#reuse-and-accepted-source-inputs)
Their eventual value is \(V=\{r(J)\le h+d\}\).
A sequence of parameters with objective tending to \(d\) eventually belongs to \(V\), by using the positive slack at one stabilization index.
Some irreducible component of \(V\) contains a subsequence.
On that component the rank of \(L\) attains its supremum by the same rank sublevel theorem.
The subsequence ensures that this supremum is at least \(h-d\).
At a maximizing parameter the two inequalities give objective at most \(d\), and scaling returns a minimizer in \(T\).

In particular \(d=0\) precisely when there is a tuple with \(r(L)=r(J)=h\).
Here \(r(J)\ge r(L)\) because \(L\) is a compression of \(J\).
Full rank of a square \(L\) gives an affiliated inverse, whose entries lie in \(D_G\) by [matrix inversion](Yin_C_A0132_v1.md#argument).
Schur elimination in the first row of the table gives \(b_0=\alpha L^{-1}\beta t_0\), hence \(u=\alpha L^{-1}\beta\).
Conversely every \(u\in D_G\) has such a [group-ring realization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations), with a finite support and size.
Every affiliated element admits bounded fractions as above, for example \(t_0=(1+u^*u)^{-1/2}\), \(b_0=ut_0\).

For the second row the Schur equation is \(X=XYX\) with \(Y=\alpha L^{-1}\beta\).
Such a rational inner inverse exists exactly when \(p_{\ker X}\) has entries in \(D_G\), by the [inner inverse and projection formulas](Yin_C_A0144_v1.md#inner-inverses-and-the-two-rank-limits).
Thus for a finitely generated \(G\), the commutator equation alone detects \(D_G\) for every \(u\) precisely when (1) here holds for every rectangular group-ring \(X\). [All-column criterion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors)
This gives a group-ring moment formulation of the remaining uniform assertion for torsion-free groups.

### Reversing the order

For fixed \(m\) take \(L=\epsilon I_h\), \(\alpha=\beta=0\), with \(0<\epsilon\le1\).
Write \(B_0\) for the lower right block of \(J\).
Then \(H_n(L)\to0\) as \(n\to\infty\), while \(H_m(J)\to h+H_m(B_0)\ge s\) as \(\epsilon\downarrow0\) if \(h\ge s\).
Taking these bounds in this order gives zero for the inner \(n\)-limit of the minima, at every fixed \(m\).
For a concrete false positive take \(G=\mathbb Z,\ t_0=1\) and \(b_0\) the Fourier multiplier \(1_{\{\operatorname{Re}\zeta>0\}}\) on the unit circle.
Here \(D_{\mathbb Z}=\mathbb C(\zeta)\) since every nonzero Laurent polynomial has zero set of Haar measure zero.
A rational function vanishing on a set of positive Haar measure vanishes identically, so \(b_0\notin D_{\mathbb Z}\).
Even \(h=1,\ F=\{1\}\) gives zero in the reversed order.

## Assessment history

### Decision mixed-trace-moments

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:30 |
| status | proved |
| reason | Compactness takes the higher moment limit at fixed pivot order, and an algebraic rank sublevel attains the resulting infimum. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The two ordered moment tests, rational parameter quantifiers and failures in reversed order. |
| argument | [Argument](#argument) | Monotone compact minimization, attainment of ranks at fixed support, Schur complements and the cyclic example. |
| dependency | [Rank sublevels](Yin_C_A0128_v1.md#statement) | Algebraic closedness and attainment of the maximal pivot rank. |
| dependency | [Inner inverses](Yin_C_A0144_v1.md#inner-inverses-and-the-two-rank-limits) | Equivalence of an exact rational inner inverse and a rational kernel projection. |
| dependency | [Resolvent moments](Yin_C_A0160_v1.md#the-two-expansions-of-the-resolvent) | The constant coefficient of the positive resolvent and its trace. |
| review | [Mixed trace moments](../audits/reviews/Yin_R_A0176_v1.md#mixed-trace-moments) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-mixed-trace-moments)
