---
author: Yin
---

# Every neighboring pair generates the subgroup of index four at cyclic order twenty-four

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity, and let \(\chi:H\twoheadrightarrow C_{24}\) have degrees \(3,4\) on the ordered marks.
Put \(t_i=s^its^{-i}\) and \(F=\ker(\chi\bmod4)\).
If the complex two-by-two four-site rectangle \(B+At-s(D+Ct)\) has regular rank \(3/2\), then
\[
       F=\langle t_i,t_{i+1}\rangle
        =\langle t_i,t_{i+1}\rangle\cap\langle t_{i+2},t_{i+3}\rangle
                        \qquad(i\in\mathbb Z).
\]
In particular this also holds when consecutive cyclic subgroups intersect trivially and the subgroup they generate has finite abelianization.
It strengthens the [integer-character criterion for a disjoint pair](Yin_C_A0256_v1.md#statement) in that case.
The result gives an original-group condition for each of the [five residual marked metabelian quotients](Yin_C_A0265_v1.md#statement).

## Comparing two copies over the intersection

Set \(A_0=\langle t_0,t_1\rangle,\ A_2=\langle t_2,t_3\rangle,\ J=A_0\cap A_2\), and \(M(z)=(Az+B)(Cz+D)^{-1}\).
The case \(\langle t_0\rangle\cap\langle t_1\rangle\ne1\) follows from the [common-power generation theorem](Yin_C_A0258_v1.md#statement).
Assume the intersection is trivial.
The [four-step middle cut](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) gives \(F=\langle A_0,A_2\rangle\), elements \(a\in A_0,b\in A_2\) with \(s^4=ba\), and
\[
                       M(t_1)M(t_0)a^{-1}\in M_2(\mathcal U(J)).
\]

Form the amalgamated free product \(\Gamma=A_0*_J A_0\) with its two injective maps \(i_1,i_2\).
For each \(l=1,2\) use the injective group map \(A_0\to\Gamma\times A_0\), \(x\mapsto(i_l(x),x)\).
Each induces a trace-preserving inclusion on group von Neumann algebras, by regular coset decomposition, and on their affiliated algebras by the corresponding operator calculus.
The two inclusions agree on \(\mathcal U(J)\) because they agree on \(J\).
Write \(u_j=i_1(t_j),v_j=i_2(t_j)\) for \(j=0,1\), \(d=i_2(a)^{-1}i_1(a)\), and suppress the coordinate inclusions in \(\Gamma\times A_0\).
The middle-cut matrix has equal images, so cancelling the final common second-coordinate translation \(a^{-1}\) gives
\[
                  M(u_1t_1)M(u_0t_0)=M(v_1t_1)M(v_0t_0)d .
\]
All rational factors are defined at infinite-order elements, by their second coordinates.
Thus
\[
          M(v_1t_1)^{-1}M(u_1t_1)=M(v_0t_0)d M(u_0t_0)^{-1}.
\]
The two sides are respectively affiliated over \(\Gamma\times\langle t_1\rangle\) and \(\Gamma\times\langle t_0\rangle\).
The [affiliated intersection formula](Yin_C_A0168_v2.md#equality-and-the-relative-norm) puts their common matrix in \(M_2(\mathcal U(\Gamma))\) because the two cyclic groups in \(A_0\) intersect trivially.
Denote this matrix by \(Q\).

## Comparing the first two coefficients at a cyclic translation

We show that whenever \(x\) generates an infinite cyclic group, \(u,v\in\Gamma\) and \(T\in M_2(\mathcal U(\Gamma))\) satisfy
\[
                       M(ux)=M(vx)T
                  \quad\text{in }M_2(\mathcal U(\Gamma\times\langle x\rangle)),
\]
one has \(u=v\).
The variable \(x\) commutes with \(\Gamma\), but there is no commutation assumption between \(u,v,T\).

Write \(M(y)=P(y)/d_0(y)\) with common polynomial denominator \(d_0(y)=\det(Cy+D)\).
Multiply the identity on the left by \(d_0(vx)\) and on the right by \(d_0(ux)\).
This gives the polynomial identity
\[
                 d_0(vx)P(ux)=P(vx)T d_0(ux).
\]
The coefficients of distinct powers of \(x\) are independent over \(\mathcal U(\Gamma)\).
Indeed a common left denominator makes the finitely many affiliated coefficients bounded, and their group Fourier supports then belong to disjoint \(\Gamma\)-cosets.
We may consequently replace \(x\) by a central indeterminate and compare formal coefficients.

If \(D\) is invertible, the denominator has nonzero constant coefficient and the identity can be expanded at zero.
Write \(M(y)=H_0+yH_1+y^2H_2+\cdots\).
The [cyclic transfer formula](Yin_C_A0245_v1.md#two-fourier-blocks-of-the-rational-transfer) gives
\[
         H_1=(A-BD^{-1}C)D^{-1},\qquad
         H_2=-(A-BD^{-1}C)D^{-1}CD^{-1}.
\]
Here \(H_1\) is invertible by the invertible assembled block matrix, and \(H_2\ne0\) since \(C\ne0\).
Comparing linear coefficients gives \(T=v^{-1}u I\).
The quadratic coefficients then give \(u^2=v^2v^{-1}u=vu\), using a nonzero constant entry of \(H_2\).
Thus \(u=v\).
If \(D\) is singular, \(C\) is invertible and \(D\ne0\) by the same cyclic transfer result.
Apply the zero-parameter proof to \(M(y^{-1})=(By+A)(Dy+C)^{-1}\), with \(x,u,v\) replaced by their inverses, to obtain \(u^{-1}=v^{-1}\).
These coefficient comparisons allow poles of \(M\) on the unit circle.

## Recovering the two generators

Apply the coefficient comparison with \(x=t_1,\ u=u_1,\ v=v_1,\ T=Q\).
Then \(i_1(t_1)=i_2(t_1)\), which gives \(t_1\in J\) by the normal form of the amalgamated free product.
Cancel the common left factor in the two-copy product to obtain \(M(u_0 t_0)=M(v_0 t_0)d\).
The same comparison with \(T=dI\) now gives \(i_1(t_0)=i_2(t_0)\), so \(t_0\in J\).
Hence \(A_0=J\subseteq A_2\), and \(s^4=ba\in A_2\).
Conjugating this inclusion by \(s^2\) gives \(A_2\subseteq s^4A_0s^{-4}\subseteq A_2\).
Therefore \(A_2=s^4A_0s^{-4}\), and conjugating back by \(s^4\in A_2\) gives \(A_0=A_2=F\).
Conjugation by \(s^i\) gives every other adjacent pair.

## Assessment history

### Decision coefficient-comparison-in-the-diagonal-embeddings

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:07 |
| status | proved |
| reason | The linear and quadratic coefficients at the cyclic translation distinguish the two copies of each generator. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The full stated result with its hypotheses. |
| argument | [Comparing two copies over the intersection](#comparing-two-copies-over-the-intersection) | Agreement of the diagonal embeddings on the common subgroup. |
| argument | [Comparing the first two coefficients at a cyclic translation](#comparing-the-first-two-coefficients-at-a-cyclic-translation) | Noncommutative denominator clearing and comparison of two coefficients. |
| argument | [Recovering the two generators](#recovering-the-two-generators) | Passage back to all adjacent pairs. |
| review | [Coefficient comparison in the diagonal embeddings](../audits/reviews/Yin_R_A0208_v1.md#coefficient-comparison-in-the-diagonal-embeddings) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-coefficient-comparison-in-the-diagonal-embeddings)
