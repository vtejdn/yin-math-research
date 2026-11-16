---
author: Yin
---
# Rank along analytic families of cancelling coefficients and a three-term phase test

## Statement

Let \(M\) be a connected complex manifold. Let \(a(p),b(p)\) be finite sums of fixed elements of a discrete group \(G\) with holomorphic coefficient functions on \(M\).
Use scalar left convolution and the canonical regular rank.
If \(a(p)b(p)=0\) for every \(p\in M\), then
\[
                    r(a(p))+r(b(q))\le1\qquad(p,q\in M).                 \tag{1}
\]
In particular, if both ranks are \(1/2\) at one point, every specialization of either factor in this family has rank at most \(1/2\).
The factors in (1) may be evaluated at different points.

For a finite product table this yields the boundary and phase tests below, including for three or more representations in overlapping double cosets of the [four-coset problem](Yin_C_A0020_v1.md#statement).
The curve can preserve a three-term equation while changing the ratios of its terms, even when the full table admits no useful additive grading.

## Argument

For \(n\ge0\) let \(V_n\) be the complex span of all monomials of total degree at most \(n\) in the finitely many coefficient functions of both factors, including the constant function.
Set \(d_n=\dim_\mathbb C V_n\).
These positive integers are nondecreasing and bounded above by a polynomial in \(n\), by counting formal monomials. Thus \(\liminf d_{n+1}/d_n=1\).
Give each \(V_n\) any Hilbert norm. Multiplication by the family \(T=a\) or \(b\) gives a bounded right-equivariant map \(T_n: V_n\otimes\ell^2(G)\longrightarrow V_{n+1}\otimes\ell^2(G)\).
In a basis this is a finite group-ring matrix.
Evaluation at any point sends its output to the operator \(T(p)\) applied to the evaluation of its input. Evaluation at all points separates the vector-valued functions, by linear independence of a basis and scalar Hilbert-space pairings.

We claim \(r(T_n)\ge d_n r(T(p))\) for every \(p\).
Fix \(\varepsilon>0\) and \(E=1_{[\varepsilon,\infty)}(|T(p)|)\).
On a neighborhood of \(p\), norm continuity makes \(T(z)\) bounded below by \(\varepsilon/2\) on \(E\ell^2(G)\).
If \(T_n\) kills a vector in \(V_n\otimes E\ell^2(G)\), its input function vanishes throughout that neighborhood.
Taking scalar pairings and applying the identity theorem on \(M\) shows that the input vanishes everywhere.
The restriction is injective there and its closed range has dimension \(d_n\tau(E)\) by polar decomposition.
Letting \(\varepsilon\downarrow0\) gives the claimed bound.
Since \(a_{n+1} b_n=0\), closed-range containment in the middle module gives
\[
       d_{n+1} r(a(p))+d_n r(b(q))\le d_{n+1}.
\]
Taking a subsequence with \(d_n/d_{n+1}\to1\) proves (1).
This argument allows arbitrary holomorphic coefficients on \(M\); no positive lower bound on the nonzero spectrum is assumed.

## A boundary with a nonhomogeneous triple

Write \(a=\sum_{x\in A}a_x x,\ b=\sum_{y\in B} b_y y\), with every coefficient nonzero.
Assign integers \(u_i,v_i\) to each row and column label, treating the two label sets separately.
Multiply each coefficient with label \(i\) by \(s^{u_i}t^{v_i}\).
For each \(w\in AB\), denote the resulting coefficient by \(F_w(s,t)\).
Assume that for some \(N\ge1\) and nonzero \(\gamma_0,\gamma_1,\gamma_2\) with sum zero, every \(F_w\) is divisible in \(\mathbb C[s^{\pm1},t^{\pm1}]\) by
\[
                  \gamma_0+\gamma_1s^N+\gamma_2t^N.                    \tag{2}
\]
The zero polynomial is allowed.
In particular this hypothesis arises when all fibers but one preserve their full equations by common monomial factors and the last, nonhomogeneous triple has (2) as its equation up to a monomial factor.
With several large fibers, divisibility is checked on each actual coefficient sum.

Here is one sufficient finite test for the construction in the single-triple case.
Put \(e_{xy}=e_x+e_y\) in the rational vector space on the row and column labels.
Quotient by the span of all equal-product differences \(e_{xy}-e_{x'y'}\) from the other fibers.
If the two differences from the first term of the triple to its other terms are independent in this quotient, pick two rational linear forms dual to them and clear all their denominators by a common \(N\).
These give the two label weights. The three coefficients \(\gamma_j\) are their original nonzero summands ordered to give (2).

The projective plane curve \(\gamma_0 Z^N+\gamma_1 S^N+\gamma_2 T^N=0\) is smooth, including the case \(N=1\).
In the chart \(Z=1\), the polynomial in \(t\) is irreducible by Eisenstein at any simple root in \(s\) of \(\gamma_0+\gamma_1s^N\).
The chart is connected: away from these simple roots it is the cover of the punctured \(s\)-plane given by an \(N\)-th root, and continuation around one simple root cycles through all \(N\) branches.
Removing finitely many additional points from this smooth connected curve preserves connectedness.

At \(s=0\), choose **any** root \(t_0\) of \(t_0^N=-\gamma_0/\gamma_2\).
Subtract the smallest row \(u\)-weight from all row weights and the smallest column \(u\)-weight from all column weights. These separate scalar monomials leave the product zero on the punctured curve.
On the connected chart with \(t\ne0\) the resulting families are holomorphic even at \(s=0\); the product remains zero by continuity.
At \((1,1)\) they are the original factors.
Thus (1) implies that both boundary factors have rank \(\le1/2\) if the original pair has both ranks \(1/2\).
The row boundary factor is
\[
        a_{0,t_0}=\sum_{u_x=\min_A u} a_x t_0^{v_x} x,                  \tag{3}
\]
with the corresponding formula for the column factor.
The same argument at \(t=0\) selects the minima of \(v\). In the chart \(S=1\) use \(Z/S=1/s,\ T/S=t/s\) to see that \(Z=0\) selects the maxima of \(u+v\) on each side.
The supports selected on the two sides multiply with no uniquely represented element, since the boundary factors are nonzero and multiply to zero.
In a torsion-free group a boundary support lying in at most two cosets of an infinite cyclic subgroup already contradicts the [two-coset rank bound](Yin_C_A0019_v1.md#consequences-for-group-ring-products).
For example this excludes a row weight strictly monotone along the support points of each of four occupied cyclic cosets, since it leaves at most four points and the [four-point rank bound](Yin_C_A0027_v1.md#statement) is strict at \(1/2\).

## Averaging the boundary phases

Write \(A_0=\{x:u_x=\min_A u\}\), \(c_x=a_xt_0^{v_x}\), \(m=\sum_{A_0}|c_x|^2\), and \(\omega=\exp(2\pi\mathrm i/N)\).
All \(N\) boundary factors \(\sum_{A_0}c_x\omega^{jv_x}x\), \(0\le j<N\), must pass the same rank bound.
For each one, Cauchy–Schwarz on the support of \(T T^*\) gives \(m^2\le r(T)\tau((TT^*)^2)\).
Uniformly averaging over these \(j\) and using finite Fourier orthogonality in the group coefficients of \(TT^*\) therefore gives the necessary inequality
\[
 \sum_{g\in A_0 A_0^{-1}}\ \sum_{k\bmod N}
 \left|\sum_{\substack{xx'^{-1}=g\\v_x-v_{x'}\equiv k\bmod N}}
                         c_x\overline{c_{x'}}\right|^2 \ \ge\ 2m^2.      \tag{4}
\]
Here both \(x,x'\) range over \(A_0\).
For example, if for each \(g\ne e\) the residues distinguish its ordered representations, the left side is \(2m^2-\sum_{A_0}|c_x|^4\), which violates (4).
Partial separation also suffices whenever the actual left side is smaller than \(2m^2\).
This probability measure samples only specializations reached on the connected cancelling curve.
The construction requires the divisibility or independence hypothesis; the remaining product tables need not supply such a curve or a violating boundary moment.

## Assessment history

### Decision analytic-triple

| Field | Value |
| --- | --- |
| date | 2026-11-17T00:51 |
| status | proved |
| reason | The independent review covers the full fixed statement, proof and stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cross-parameter rank, deformations preserving a nonhomogeneous triple and boundary-phase tests. |
| argument | [Proof](#argument) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0059_v1.md#whole-argument-finding) | Independent mathematical review of the result and its limitations. |

## Current assessment

[Selected decision](#decision-analytic-triple)
