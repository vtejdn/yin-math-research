---
author: Yin
---

# An unconditional rank-two basis over the actual index-four subgroup

## Statement

Use the hypotheses and notation of the [four-sign construction](Yin_C_A0331_v1.md#statement), in particular a half kernel, the index-four binary kernel \(N\), and the group-ring commutator matrix \(R\in M_4(\mathbb CN)\) of regular rank two.
Its kernel has an explicit four-by-two basis \(Y\) over \(D_2(N)\), the second scalar inverse layer inside \(U(N)\), with a constant left inverse.
Thus the inner rank of \(R\) over \(D_2(N)\) is exactly two, and the two compatible norm identities of the earlier construction hold unconditionally over that layer.
For one of the two marks the norm matrix can be chosen already over the group ring:
\[
             V_t=\begin{pmatrix}0&t^{-2}\\1&0\end{pmatrix}.
\]
The second layer suffices whether or not the first layer contains a fractional scalar.
The construction uses the simultaneous one-inverse description of the two complementary signed kernels before passing to the common index-four subgroup.

For any scalar character of \(N\), the ordinary rank of its evaluation on \(R\) bounds the original group-ring inner rank from below.
In particular a rank-three or rank-four such evaluation certifies an actual drop to inner rank two by the second layer.
The lower bound over \(\mathbb CN\) is conditional on that evaluation.

## Even and odd coefficients of a single inverse

Put \(F=\ker(\chi_s)\), where \(\chi_s\) negates \(s\) and fixes \(t\), so \(F/N\) has order two and \(t\) represents the odd coset.
Write \(\iota\) for the sign automorphism negating \(t\) and fixing \(s\), restricted to \(U(F)\).
For any \(b\in D_1(F)\), its decomposition
\[
      b=b_0+t b_1,\qquad b_0=(b+\iota b)/2,\qquad
                       b_1=t^{-1}(b-\iota b)/2
\]
satisfies \(b_0,b_1\in D_2(N)\).
The same holds for the odd coordinate on the right since conjugation by \(t\) preserves these layers.

Indeed represent left multiplication on the two right-module coordinates of \(\mathbb CF=\mathbb CN\oplus t\mathbb CN\).
For an element of \(\mathbb CF\) the resulting two-square matrix has group-ring entries in \(N\), and its first column consists of the two displayed coefficients.
The unitary decomposition of \(\ell^2(F)\) into the two cosets identifies this with the original left representation.
The matrix realization thus extends to affiliated sums and inverses.
For a nonzero \(g\in\mathbb CF\) the matrix for \(g\) is a unit over \(U(N)\) by scalar injectivity.
At least one of its group-ring entries is nonzero, hence an affiliated unit.
Choose it as a first pivot.
The remaining scalar Schur complement is a unit over \(U(N)\), by invertibility of the entire matrix, and lies in \(D_1(N)\).
Inverting it puts every entry of the matrix for \(g^{-1}\) in \(D_2(N)\).
The matrices representing sums and products of the first-layer generators still have entries there.
This proves the assertion without presuming that arbitrary first-layer scalars are invertible.

## Constructing the basis and checking both actions

Use the original constant assembly \(T=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\) and the two involutions \(J,L\) of the [commutator construction](Yin_C_A0331_v1.md#two-involutions-with-a-polynomial-commutator).
Write \(E=\ker R\) as an affiliated module and \(C_\eta=T\binom{\eta t I_2}{I_2}\).
For the true sign changing \(s\) alone, the [rank-one quadratic remainder](Yin_C_A0330_v1.md#the-scalar-norm-on-the-sign-kernel) supplies a column \(Z=(z,1)^{\mathsf T}\) with \(z\in D_1(F)\).
Its range over \(U(H)\) is the sum of \(\ker(P(t)-sQ(t))\) and \(\ker(P(t)+sQ(t))\) because the two complementary scalar idempotents in the same coordinate exhaust that range.
Consequently \(Y_+=C_+ Z\) spans the \(+1\) space of \(L\) inside \(E\).
The column \(Y_-=\iota(Y_+)=C_-\,\iota(Z)\) spans the \(-1\) space of \(L\) there, since \(\iota(J)=J,\ \iota(L)=-L\) and the commutator kernel is invariant under this character.
The two columns together are a basis over \(U(H)\).
Their entries lie in \(D_1(F)\).

Set
\[
      Y_e=(Y_++Y_-)/2,\qquad Y_o=(Y_+-Y_-)t^{-1}/2,\qquad
      Y=[\,Y_e,\ Y_o\,].
\]
The even and odd coefficient calculation gives \(Y\) over \(D_2(N)\).
Both original columns are recovered as \(Y_e\pm Y_o t\).
Thus \(Y\) spans \(E\) over \(U(H)\).
More precisely, let \(w_b,w_a\) be the row functionals selecting the second entry of the bottom, respectively top, coordinate pair after applying \(T^{-1}\).
The second entry of \(Z\) is one, and likewise for \(\iota(Z)\).
It follows that \(w_bY_\pm=1,\ w_aY_\pm=\pm t\), whence \(w_bY=(1,0)\) and \(w_aY=(0,1)\).
The constant matrix \(W\) with rows \(w_b,w_a\) is a left inverse of \(Y\).
For any kernel column over \(U(N)\), its two coordinates in \(Y\) are given by \(W\) and already lie in \(U(N)\).
This also identifies the kernel over the subgroup itself.

After a constant change of coordinates the two rows of \(W\) become coordinate selectors.
An elementary shear over \(D_2(N)\) then takes the two columns of \(Y\) to coordinate columns, since their selected coordinate pair is exactly \(I_2\).
From \(RY=0\) it follows that \(R\) factors through two columns over this layer.
Its regular rank is two, proving the inner rank assertion.
Any original group-ring factorization specializes under every scalar character of \(N\), giving the lower bound in the statement.

Finally \(LY_+=Y_+\), \(LY_-=-Y_-\) imply \(LY_e=Y_o t,\ LY_o=Y_e t^{-1}\), hence \(LY=Y V_t(tI_2)\) with the claimed explicit \(V_t\).
Put \(V_s=W J(s^{-1}I_4){}^s Y\), which lies over \(D_2(N)\).
The invariance of \(E\) and its left inverse give \(JY=Y V_s(sI_2)\).
Squaring and commuting on \(E\) now give
\[
    V_s{}^sV_s=s^{-2}I_2,\qquad V_t{}^tV_t=t^{-2}I_2,\qquad
                V_s{}^sV_t([s,t]I_2)=V_t{}^tV_s .
\]
The first two equalities also give the two inverses in the same layer by direct finiteness of the ambient affiliated matrix algebra.

## Assessment history

### Decision the-explicit-second-layer-basis

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:25 |
| status | proved |
| reason | Restriction of scalars and the two sign columns provide a normalized second-layer basis without any rank assumption on first-layer scalars. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Restriction of scalars and the two sign columns provide a normalized second-layer basis without any rank assumption on first-layer scalars. |
| argument | [Even and odd coefficients of a single inverse](#even-and-odd-coefficients-of-a-single-inverse) | Even and odd coefficients of a single inverse. |
| argument | [Constructing the basis and checking both actions](#constructing-the-basis-and-checking-both-actions) | Constructing the basis and checking both actions. |
| dependency | [Four signed kernels on their common subgroup](Yin_C_A0331_v1.md#statement) | The earlier subgroup and rank conclusions used here. |
| review | [Four signed kernels on their common subgroup](../audits/reviews/Yin_R_A0227_v1.md#four-signed-kernels-on-their-common-subgroup) | Independent inspection of the earlier statement and proof. |
| review | [The explicit second-layer basis](../audits/reviews/Yin_R_A0227_v1.md#the-explicit-second-layer-basis) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-explicit-second-layer-basis)
