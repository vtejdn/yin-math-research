---
author: Yin
---

# A cofinite two-factor Fourier support precludes a nonamenable four-position endpoint

## Statement

Let \(G=\langle s,t\rangle\), with \(t\) of infinite order, write \(t_i=s^its^{-i}\), \(Y_i=\langle t_i\rangle\), and suppose \(Y_0\cap Y_1=1\).
Let \(M(z)\in{\rm GL}_h(\mathbb C(z))\).
If \((s^{-1}M(t))^4=I_h\) and the following conditions hold, then \(G\) is solvable.

Choose a constant row \(l\) and column \(v\) so that \(lM,Mv,lM^{-1},M^{-1}v\) have no unit-circle poles.
Let \(a_i,b_j\) be the Fourier coefficients at indices \(i,j\in\mathbb Z\) of \(lM\) and \(Mv\), respectively.
Require \(a_i b_j\ne0\) for all but finitely many pairs in \(\mathbb Z^2\).
The same conclusion holds if both matrices have no circle poles and their matrix Fourier coefficients \(M_i M_j\) are nonzero for all but finitely many pairs.
These tests allow arbitrary dependence of the four group conjugates and require no finite abelian quotient.

In particular for a nonamenable label group satisfying the stated cyclic-intersection condition and the four distinct cosets of the [four-position transfer window](Yin_C_A0183_v1.md#statement), either support test implies
\[
                           \dim_G\ker(sI_h-M(t))<h/4 .
\]
The coefficient example below has \(M(1)^4=I_2\) and still satisfies the strict test.

## The two products differ by only finitely many labels

Under the quartic hypothesis the [middle identity](Yin_C_A0187_v1.md#extending-the-unitary-twists) reads
\[
       M(t_1)M(t_0)=M(t_2)^{-1}M(t_3)^{-1}g,\qquad g=s^4 .
\]
Multiply by \(l,v\) or use the uncompressed matrix version.
Every factor in the resulting two products is bounded with absolutely summable Laurent coefficients, since the relevant rational functions are holomorphic on an annulus containing the unit circle.
Group-coordinate coefficients can therefore be compared directly.
The products \(t_1^i t_0^j\) are distinct by trivial neighboring intersection.
The set \(D=Y_1Y_0\) consequently has all but finitely many of its elements in \(D'=Y_2Y_3 g\), by the given nonvanishing on the left and support containment on the right.

The map \(u\mapsto s^2u^{-1}s^2\) is an involution of the group as a set and interchanges \(D,D'\).
It follows that \(D\triangle D'\) is finite.
For every \(y\in Y_2\) the set \(D'\) is left invariant under \(y\).
Consequently \(D\triangle yD\) is finite, and it is also right invariant under the infinite group \(Y_0\).
Any nonempty such set contains an infinite right orbit.
Hence \(D=yD\).

Put \(A_i=\langle Y_i,Y_{i+1}\rangle\).
The invariance gives \(Y_2\subseteq D\subseteq A_0\).
Also \(Y_2g\subseteq D'\) is infinite and therefore meets \(D\); hence \(g\in A_0\).
Now \(A_1\subseteq A_0\), and its successive conjugates by \(s\) give a descending chain ending at \(A_4=g A_0 g^{-1}=A_0\).
Thus \(A_1=A_0\).
The set \(D\) contains the identity and is left invariant under \(Y_1,Y_2\), which generate \(A_0\).
This gives \(A_0=D\), a product of two cyclic groups, metabelian by [Itô's factorization theorem](https://doi.org/10.1007/BF01180647).
It is normal in \(G\) by invariance under \(s\) and by \(t\in A_0\), and the quotient is cyclic.
This proves solvability.
At the window endpoint the quartic identity is automatic, so nonamenability makes the window inequality strict.

## A split pair of poles with a fourth-order scalar evaluation

For a concrete two-square input take
\[
 Q(z)=\begin{pmatrix}z-1/2&0\\0&z-2\end{pmatrix},
 \qquad P(z)=
 \begin{pmatrix}1-z&(7z-5)/2\\(7-5z)/4&4z-4\end{pmatrix},
 \qquad M(z)=P(z)Q(z)^{-1}.
\]
Its determinant numerator \(\det P(z)\) is \((3/8)(z-1/3)(z-3)\).
Both transfers are bounded on the circle; \(M(1)=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\).
For a rational function bounded at infinity with simple poles at \(1/2\) and \(2\), the negative Fourier coefficients are nonzero scalar multiples of the residue at \(1/2\), and the strictly positive coefficients are nonzero multiples of the residue at \(2\).
This follows by expanding each simple fraction on the unit circle.
For the displayed \(M\) the two residues and the constant Fourier coefficient are
\[
  R_-=\begin{pmatrix}1/2&0\\9/8&0\end{pmatrix},\qquad
  R_+=\begin{pmatrix}0&9/2\\0&4\end{pmatrix},\qquad
  M_0=\begin{pmatrix}-1&5/4\\-5/4&2\end{pmatrix}.
\]
Indeed \(M_0=M(\infty)-R_+/2\).
Both residue columns have both entries nonzero, so every product of two residues is nonzero.
The determinant of \(M_0\) is \(-7/16\), so all nine ordered products formed from \(R_-,R_+,M_0\) are nonzero.
The full-matrix test therefore applies, even though the four-step identity already holds at the scalar evaluation \(s=t=1\).

## Assessment history

### Decision cofinite-products-of-fourier-coefficients

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:56 |
| status | proved |
| reason | The quartic identity and the cofinite coefficient condition force a product of two cyclic groups inside a cyclic extension. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The quartic identity and the cofinite coefficient condition force a product of two cyclic groups inside a cyclic extension. |
| argument | [The two products differ by only finitely many labels](#the-two-products-differ-by-only-finitely-many-labels) | The two products differ by only finitely many labels. |
| argument | [A split pair of poles with a fourth-order scalar evaluation](#a-split-pair-of-poles-with-a-fourth-order-scalar-evaluation) | A split pair of poles with a fourth-order scalar evaluation. |
| review | [Cofinite products of Fourier coefficients](../audits/reviews/Yin_R_A0219_v1.md#cofinite-products-of-fourier-coefficients) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-cofinite-products-of-fourier-coefficients)
