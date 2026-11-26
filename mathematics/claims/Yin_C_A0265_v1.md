---
author: Yin
---

# Alternating cubic characters eliminate the sign factor at cyclic order twenty-four

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity and an abelian quotient of order 24.
Suppose \(K=B+At-s(D+Ct)\) with complex two-by-two coefficients has regular rank \(3/2\).
Use the [normalized ordered marking](Yin_C_A0241_v1.md#statement) of degrees \(3,4\) in \(H_{\rm ab}=C_{24}\).
Then the first factor in the [twenty marked metabelian candidates](Yin_C_A0263_v1.md#statement) is trivial.
In particular \(H'/H''\) is trivial or cyclic of order 5 or 13.
There are five remaining ordered candidates for \(H/H''\): the cyclic group of order 24 and the semidirect products with one of the two square roots of \(-1\) acting on \(C_5\) or \(C_{13}\), with the marking specified there.

More generally, write \(\chi:H\to C_{24}\) for the normalized degree, \(F=\ker(\chi\bmod4)\), \(t_i=s^its^{-i}\) and \(\mu_3\) for the complex cube roots of unity.
The half-rank transfer identity and the absence of a constant point correspondence force \(t_0t_1=t_1t_0\) if for every \(a,b\in\mu_3\) there is a character of \(F\) fixing \(s^4\), with values \(a\) on \(t_0,t_2\) and \(b\) on \(t_1,t_3\).
This equality holds in the original group under these conditions.

## Independent rotations in the four-step identity

Suppose the first factor is nonzero.
It surjects onto \(C_3\) with the cyclic complement acting by negation, for both of the order-nine actions as well as for the order-three action.
The marked quotient from the [explicit list](Yin_C_A0263_v1.md#statement) therefore maps \(s\) to \(\gamma^3\) and \(t\) to \(1\gamma^4\) in \(C_3\rtimes C_{24}\), with \(1\) the additive generator.
The image of \(F\) lies in \(C_3\times\langle\gamma^4\rangle\).
The images of \(t_i\) there are \(((-1)^i,\gamma^4)\) and that of \(s^4\) is \((0,\gamma^{12})\).
Fix a primitive cube root \(\omega\).
The characters \((x,\gamma^{4j})\mapsto\omega^{u x+v j}\), \(u,v\in\mathbb F_3\), fix \(s^4\) and have values \(\omega^{u+v},\omega^{-u+v}\) on the even and odd labels.
The two exponents run independently through \(\mathbb F_3\) since \(2\) is nonzero there.

Use \(M(z)=(Az+B)(Cz+D)^{-1}\).
The [four-step identity](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) is \(M(t_3)M(t_2)M(t_1)M(t_0)=s^4 I\) over the actual affiliated algebra of \(F\).
Each character acts on this algebra by the unitary character twist, so for all \(a,b\in\mu_3\)
\[
             M(bt_3)M(at_2)M(bt_1)M(at_0)=s^4 I .
\]
Every evaluated factor is an affiliated unit, since \(t_i\) has infinite order and \(M\) is an invertible rational matrix.
Fix \(b\) and compare \(a,a'\).
Cancellation at \(t_3\) gives
\[
 M(a't_2)^{-1}M(at_2)
      =M(bt_1)\,M(a't_0)M(at_0)^{-1}\,M(bt_1)^{-1}.
\]
The left side is independent of \(b\).
Comparing \(b,b'\) proves that every left ratio \(M(a't_0)M(at_0)^{-1}\) commutes with every right ratio \(M(b't_1)^{-1}M(bt_1)\).
Both ordered phase pairs vary independently.

## Laurent coefficients of the inverse differences

The [four-site reduction](Yin_C_A0184_v1.md#statement) gives an invertible assembled matrix; denote its inverse by
\[
              \begin{pmatrix} A&B\\ C&D\end{pmatrix}^{-1}
                        =\begin{pmatrix} E&U\\ V&W\end{pmatrix}.
\]
For independent variables \(p,q\) one has
\[
\begin{aligned}
 (M(q)-M(p))(Cp+D)&=(q-p)(A-M(q)C),\\
 (A-M(q)C)^{-1}&=E-qV,\qquad (E-qV)M(q)=qW-U .
\end{aligned}
\]
Indeed \([I,-M(q)]\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)=(A-M(q)C)[I,-qI]\); multiplying by the inverse gives both identities.
Consequently \(M(q)-M(p)\) has a rational inverse \((Cp+D)(E-qV)/(q-p)\).
For distinct \(a,b\in\mu_3\), set
\[
\begin{aligned}
 L_{b,a}(z)&=(M(bz)M(az)^{-1}-I)^{-1}
        =\frac{(Aaz+B)(E-bzV)}{(b-a)z},\\
 R_{b,a}(z)&=(M(bz)^{-1}M(az)-I)^{-1}
        =\frac{(Caz+D)(bzW-U)}{(a-b)z}.
\end{aligned}
\]
For the second formula use \((M(az)-M(bz))^{-1}M(bz)=-(Caz+D)(E-bzV)M(bz)/((b-a)z)\).
These expressions use only the three powers \(z^{-1},1,z\).
By the preceding commutation and invertibility, each \(L_{b,a}(t_0)\) commutes with every \(R_{d,c}(t_1)\), for all \(b\ne a,\ d\ne c\).

Simultaneously multiplying the two phases of any pair by \(\omega\) replaces \(z\) by \(\omega z\) in that family's rational definition.
Taking the three Fourier projections independently on the left and on the right therefore gives
\[
              [P_e t_0^e,Q_j t_1^j]=0\qquad (e,j\in\{-1,0,1\})
\]
for every coefficient \(P_e\) of any \(L_{b,a}\) and every coefficient \(Q_j\) of any \(R_{d,c}\).
These equations are identities of genuine group-ring matrices.

## No invariant line for the numerical ratios

For any fixed nonzero complex \(z\) outside the finite set where some \(M(\omega^jz)\) is singular or has a pole, each of the two numerical families \(L_{b,a}(z)\) and \(R_{b,a}(z)\) has no common invariant line.
Invariance under an inverse difference \((T-I)^{-1}\) is equivalent to invariance under \(T\), since an invertible matrix preserving a line restricts to a bijection of that line.
For the right ratios, a line spanned by a common invariant vector \(c\) would imply \(M(\omega^j z)c\in\mathbb C M(z)c\) for all \(j\).
For the left ratios, take a vector \(d\) in a common invariant line and \(c=M(z)^{-1}d\), giving the same collinearity.
Write \((Ay+B)\operatorname{adj}(Cy+D)=H_0+yH_1+y^2H_2\).
The three values at \(y=z,\omega z,\omega^2z\) imply by the invertible Vandermonde matrix that each \(H_jc\) belongs to the single line \(\mathbb CM(z)c\).
Then \(M(y)\) sends the constant line of \(c\) to a constant line as a rational identity.
This contradicts the [constant point correspondence criterion](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer), since the regular rank of \(M(t)-sI\) is \(3/2\) and \(s\notin\langle t\rangle\) by their degrees.

In particular each family has a nonzero coefficient of exponent \(1\) or \(-1\) in at least one pair.
Otherwise all its inverse differences and hence all its ratios would be constant in \(z\).
For the left family let \(D_1=M(\omega z)M(z)^{-1}\).
Constancy gives \(M(\omega^jz)=D_1^j M(z)\) for \(j=0,1,2\), so all left ratios are powers of \(D_1\) and share an eigenline.
For the right family constancy similarly gives \(M(\omega^j z)=M(z)D_2^j\) for \(D_2=M(z)^{-1}M(\omega z)\), with the same contradiction.

## Commutation of the neighboring translations

Suppose \(t_0\) and \(t_1\) do not commute.
For \(e,j\in\{-1,1\}\), the words \(t_0^e t_1^j\) and \(t_1^j t_0^e\) are distinct.
The two individual group coefficients in the projected commutation identity must vanish, so \(P_e Q_j=Q_j P_e=0\).
Choose a nonzero outer coefficient \(P_e\).
Every constant coefficient \(Q_0\) commutes with \(P_e\), preserving its image, and every \(Q_j\) with \(j=\pm1\) kills that image.
This nonzero subspace is invariant under the whole numerical right family at an admissible \(z\).
By the preceding result the image must be \(\mathbb C^2\), which would make every right outer coefficient zero.
This contradicts the existence of a nonzero one.
Thus \(t_0\) and \(t_1\) commute.

Under half rank the abelianization of the neighboring group \(\langle t_0,t_1\rangle\) is finite, by the [disjoint cyclic case](Yin_C_A0256_v1.md#statement) and the [common-power case](Yin_C_A0258_v1.md#statement).
Commutation would make this group itself finite although it contains the infinite-order element \(t\).
Therefore the alternating characters cannot exist and the first factor vanishes.

## Assessment history

### Decision alternating-cubic-characters-and-the-two-translations

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:44 |
| status | proved |
| reason | Independent reviewers verified the original-group twists, noncommutative ratio identities and elimination of all sign factors. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The five marked groups and the original-group commutation criterion. |
| argument | [Independent rotations in the four-step identity](#independent-rotations-in-the-four-step-identity) | The two independent phases and the order of the left and right ratios. |
| argument | [Laurent coefficients of the inverse differences](#laurent-coefficients-of-the-inverse-differences) | The inverse of each matrix difference and Fourier separation of the three powers. |
| argument | [No invariant line for the numerical ratios](#no-invariant-line-for-the-numerical-ratios) | The constant-line contradiction and the column and row alternatives. |
| argument | [Commutation of the neighboring translations](#commutation-of-the-neighboring-translations) | The two distinct group words and the contradiction with finite abelianization. |
| review | [Alternating cubic characters and the two translations](../audits/reviews/Yin_R_A0207_v1.md#alternating-cubic-characters-and-the-two-translations) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-alternating-cubic-characters-and-the-two-translations)
