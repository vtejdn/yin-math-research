---
author: Yin
---

# Arbitrary formal character values of the same scalar norm solution

## Statement

Let \(H=\langle g,h\rangle\) be torsion-free with regular scalar group-ring injectivity and let a sign negate \(g\) and fix \(h\).
Write \(F\) for its kernel, \(A=\mathbb CF\), and \(\alpha={\rm Ad}_{g^{-1}}\) on \(U(F)\).
Suppose \(K=P(h)-gQ(h)\), for complex two-square linear pencils \(P,Q\), has regular nullity \(1/2\) with unnormalized matrix trace.
The [four-site pencil reduction](Yin_C_A0184_v1.md#statement) implies that both pencils are regular and that both labels have infinite order.
Assume there is a circle character \(\chi\) of \(H\), with \(x=\chi(g),\ y=\chi(h)\), for which both \(P(y)-xQ(y)\) and \(P(y)+xQ(y)\) are invertible.
Put \(\psi=\chi|_F\).
At the noncyclic abelian quotient of order twenty one of the two mark orientations has such a character by the [five sign squares](Yin_C_A0333_v1.md#adjacent-nonzero-values-on-the-five-sign-squares).

Use the original two input coordinates for the [scalar norm solution](Yin_C_A0330_v1.md#the-scalar-norm-on-the-sign-kernel) \(V\in D_1(F)\), so that \(V\alpha(V)=g^2\) and the second coordinate of the positive signed kernel has scalar image \(\frac12(1+Vg^{-1})U(H)\).
For **every** \(r\in\mathbb C\) there is a group-ring scalar \(k_r\) with \(\psi(k_r)=1\) and an explicit expression for this same \(V\) using only \(A\) and \(k_r^{-1}\), for which formal substitution at \(\psi\) gives \(r\).
These expressions are obtained by solving three polynomial rows of the original restricted rectangle.
Each formal substitution is the homomorphism out of the universal algebra adjoining the indicated inverse.
On its actual image inside \(U(F)\) the equal expressions for \(V\) need not remain equal after formal substitution.

One may also fix a **single** denominator \(k\in A\) with \(\psi(k)=1\), independent of \(r\).
In the universal algebra adjoining \(k^{-1}\), the lifts of \(V\) to this algebra have all complex values at the extension of \(\psi\).
There are lifts of \(V,\alpha(V)\) both taking the value zero, so their product minus \(g^2\) has value \(-x^2\ne0\) while it vanishes in \(U(F)\).
Thus a nonzero scalar value of every denominator in a proposed evaluation of this particular norm equation does not suffice to preserve it.

## Restriction and the normalized kernel vector

Use \(A\oplus gA\) as right \(A\)-module coordinates of \(\mathbb CH\).
Write a two-component column as \(E+gO\); the symbols \(E,O\) denote its even and odd coordinate columns on the right of the representatives \(1,g\).
Left multiplication by \(K\) restricts to
\[
       \mathcal K=
         \begin{pmatrix}
              P(h)&-g^2Q(h_{-1})\\
              -Q(h)&P(h_{-1})
         \end{pmatrix},\qquad h_{-1}=g^{-1}hg .
\]
Indeed \(P(h)g=gP(h_{-1})\) and \(gQ(h)g=g^2Q(h_{-1})\).
This is the coset decomposition of the regular operator on two copies of \(\ell^2(F)\) per input coordinate; it extends to affiliated modules.
The unnormalized nullity over \(F\) is twice that over \(H\), since the regular kernel projection has the same diagonal trace contribution on both cosets by right translation.
Thus \(\mathcal K\) has rank three over \(U(F)\).
At \(\psi\), sending \((E,O)\) to \((E+xO,E-xO)\) on both the input and the output transforms \(\psi(\mathcal K)\) into the diagonal sum of the two matrices in the hypothesis.
In particular \(\psi(\mathcal K)\) is invertible.

The [common kernel coordinate](Yin_C_A0330_v1.md#the-common-kernel-coordinate-and-the-inner-rank) gives \(Z=(z,1)^{\mathsf T}\) with \(z\in D_1(F)\) and \(\ker K=Ze_+U(H)\), \(e_+=(1+Vg^{-1})/2\).
The column \(Z(V+g)=2Ze_+g\) lies in this kernel.
In the chosen restriction coordinates it equals
\[
                           (ZV,\ \alpha(Z))^{\mathsf T}
\]
by vertical concatenation, since \(Zg=g\alpha(Z)\) entrywise.
Its second even coordinate is \(V\), and its second odd coordinate is \(1\).
In particular no conjugate of \(V\) is used as the former coordinate.

## Elimination with a prescribed numerical value

Fix \(r\in\mathbb C\), and premultiply \(\mathcal K\) by the invertible numerical matrix
\[
                 (I_4-r e_{24})\,\psi(\mathcal K)^{-1},
\]
where \(e_{24}\) has its single one in row two and column four.
In two-by-two blocks write the result as
\[
             \begin{pmatrix}D(h)&T_1\\ E_0(h)&T_2\end{pmatrix}.
\]
Both blocks of its first column pair are polynomials in \(h\), since they are constant combinations of the rows of \(P(h),-Q(h)\).
At \(\psi\) the whole matrix equals \(I_4-r e_{24}\).
Thus \(b=\det D(h)\) satisfies \(\psi(b)=1\) and is an affiliated unit by scalar injectivity.
The two-square residual
\[
                       A_r=bT_2-E_0(h)\operatorname{adj}D(h)\,T_1
                                     \ \in M_2(A)
\]
has regular rank one: invert the cyclic block \(D(h)\) in the affiliated algebra, eliminate it, and multiply the remaining two rows by \(b\).
The formula uses commutation of \(b\) with \(E_0(h)\) on the left.
At \(\psi\) this residual is \(I_2\).
For its first row \((a,c)\) one has \(\psi(a)=1,\ \psi(c)=0\).

The first row has the same actual right kernel as \(A_r\), since its pivot \(a\) is an affiliated unit and both kernels have dimension one with one contained in the other.
Therefore
\[
          O_r=(-a^{-1}c,1)^{\mathsf T},\qquad
          E_r=-D(h)^{-1}T_1 O_r
\]
give the unique vector in \(\ker\mathcal K\) whose second odd coordinate is one.
Indeed the equation \(A_r O=0\) determines the first odd coordinate from the second, and \(D(h)E=-T_1 O\) determines both even coordinates.
By the preceding section, \(E_r=ZV,\ O_r=\alpha(Z)\) in the actual affiliated algebra.
In particular \((E_r)_2=V\) for all \(r\).
Only \(a^{-1},b^{-1}\) are needed, since \(D(h)^{-1}=b^{-1}\operatorname{adj}D(h)\).
Both inverses are obtained from \(k_r^{-1}\) for \(k_r=ab\), by using \(b(ab)^{-1}\) and \((ab)^{-1}a\).
All these denominators have value one at \(\psi\).

At the numerical character the elimination formulas themselves give \(O_r=(0,1)^{\mathsf T}\) and \(E_r=(0,r)^{\mathsf T}\).
This last evaluation solves the two pivot rows and the first residual row only.
The full specialized matrix is invertible.
This proves the assertions about the original solution and the formal value of the displayed expression.

## One normalized denominator for all values

Keep the preceding expressions at \(r=0,1\), and take the ordered product \(k=k_0 k_1\alpha(k_0)\alpha(k_1)\).
Conjugation by \(g^{-1}\) preserves \(\psi\), as it is the restriction of a scalar character of \(H\), so \(\psi(k)=1\).
In the actual ring adjoining \(k^{-1}\), the inverse of each of the four factors is given by multiplying \(k^{-1}\) by its suffix on the left and its prefix on the right.
Use those same words in the universal algebra \(A\langle X\rangle/(kX=Xk=1)\), which maps to the actual ring by \(X\mapsto k^{-1}\) and to \(\mathbb C\) by the character and \(X\mapsto1\).
The words recover the required inverses after the actual map and evaluate as the correct scalar inverses under the character; the proof only needs these two maps.

Write \(v_0,v_1\) for the lifts of the two constructed expressions for \(V\).
Their images under the actual map are equal, and their character values are zero and one, respectively.
The affine family \((1-r)v_0+rv_1\) has actual image \(V\) and character value \(r\).
Applying \(\alpha\) to the original expression at zero before replacing its denominator gives a lift \(\widetilde v_0\) of \(\alpha(V)\) with value zero.
Hence \(v_0\widetilde v_0-g^2\) has the asserted nonzero character value and zero actual image.
This also shows that the regular inverse of the single scalar \(k\) cannot be given by an element of \(\ell^1(F)\): otherwise the actual one-inverse ring would lie in that faithful convolution algebra, where the bounded character would preserve all equalities.

## Assessment history

### Decision formal-values-of-the-actual-norm-solution

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:52 |
| status | proved |
| reason | Eliminating three rows with a normalized odd coordinate realizes arbitrary formal values of the same actual scalar. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every formal value of one actual norm solution with a fixed denominator. |
| argument | [Restriction and the normalized kernel vector](#restriction-and-the-normalized-kernel-vector) | The second even and odd coordinates. |
| argument | [Elimination with a prescribed numerical value](#elimination-with-a-prescribed-numerical-value) | The cyclic and scalar pivots. |
| argument | [One normalized denominator for all values](#one-normalized-denominator-for-all-values) | The suffix and prefix words and the norm relation. |
| review | [Formal values of the actual norm solution](../audits/reviews/Yin_R_A0230_v1.md#formal-values-of-the-actual-norm-solution) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-formal-values-of-the-actual-norm-solution)
