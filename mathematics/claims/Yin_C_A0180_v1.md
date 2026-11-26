---
author: Yin
---

# Finite cyclic quotients and half rank on four group elements

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free, with every nonzero element of \(\mathbb C H\) injective in the regular representation.
Let \(\pi:H\twoheadrightarrow C_m\) and identify \(C_m=\mathbb Z/m\mathbb Z\).
For complex two-by-two coefficient matrices set
\[
             K=B+At-s(D+Ct).
\]
Take any nonzero integer pair \((a,b)\) congruent to a multiple of \((\pi(s),\pi(t))\) modulo \(m\), and set \(d=|a|+|b|\).
For some \(R\in\{0,1,2\}\) one has
\[
          0\le R-\operatorname{rk}_H K\le R\,d/m .
 \tag{1}
\]
Consequently any cyclic quotient of order **at least 33** excludes a half-dimensional constant-column increment in the four-column family with two occurrences of each label.
Neither label needs to be killed by this character.
For the half problem under scalar injectivity, the [integer-character case](Yin_C_A0179_v1.md#statement) and this bound leave only two-generator subgroups with finite abelianization of exponent at most 32.
This is a sufficient numerical bound.

There is a version for a normalized rectangle without scalar injectivity.
Assume \(t\) has infinite order, \(U(z)=Az+B,\ V(z)=Cz+D\) are both invertible over \(\mathbb C(z)\), \(b\ne0\), and \(|b|/\gcd(|a|,|b|)\ge3\).
Then (1) holds with \(R=2\).
In particular \(m>4d\) excludes half nullity for this rectangle just from torsion-freeness and the indicated finite character.

## An integer rank for a formal circle parameter

Adjoin an independent central infinite cyclic generator \(x\) and use the lifted labels
\(\widehat s=(s,x^a)\) and \(\widehat t=(t,x^b)\) in \(H\times\langle x\rangle\).
The subgroup they generate has a nonzero integer character given by projection onto the second coordinate.
The regular scalar injectivity hypothesis passes from \(H\) to the direct product.
Indeed a nonzero Laurent polynomial in \(x\) with group-ring coefficients has an injective first nonzero coefficient after shifting the exponents to start at zero.
The [polynomial rank estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) therefore gives full scalar rank except at countably many complex evaluations, including almost every point on the circle.
Fourier transformation in the central coordinate expresses its regular kernel as the direct integral of these fiber kernels, and hence its nullity is zero.
Subgroup inclusion preserves the scalar rank.

The [indicable-pair result](Yin_C_A0179_v1.md#statement) now applies to the four-column linearization of the rectangle on the lifted labels.
The [identity-pivot calculation](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) subtracts two from the pencil rank to give an integer \(R\) for the lifted rectangle.
If the two cyclic blocks are invertible and the stated denominator is at least three, \(\widehat t\) still has infinite order and the normalized transfer for \(\widehat s,\widehat t\) has rank two by the unconditional part of the indicable-pair result.
Multiplication by the invertible cyclic block gives \(R=2\) in this case without scalar injectivity.

Fourier transformation in \(x\) gives the bounded fiber matrix
\[
              K(z)=B+z^b A t-z^a s(D+z^b C t).
\]
Its rank equals its supremum outside a countable subset of the complex line with zero removed, by the same polynomial estimate, and hence almost everywhere on the circle.
Thus the direct integral rank \(R\) equals this supremum.
The exponents \(0,a,b,a+b\) span an interval of length \(d\), so a common scalar monomial gives a matrix polynomial of degree at most \(d\).
At every \(m\)-th root of unity the chosen congruence gives a genuine twist of \(H\), preserving the rank at \(z=1\), even when some twists repeat.
The sum of the deficits from the supremum at these \(m\) distinct parameter values is at most \(dR\), proving (1).

## A short pair of exponents

The lattice
\[
 \Lambda=\{(a,b)\in\mathbb Z^2:(a,b)\bmod m
                  \in\langle(\pi(s),\pi(t))\rangle\}
\]
has index \(m\), since surjectivity makes the reduced pair have order \(m\) in \(C_m^2\).
For \(m\ge33\), put \(j=\lfloor(m-1)/8\rfloor\ge4\).
The integer points \((u,v)\) with \(|u|+|v|\le j\) number \(1+2j(j+1)>m\): indeed \(m\le8j+8\) and the strict inequality holds for \(j\ge4\).
Two distinct such points agree modulo \(\Lambda\).
Their difference gives a nonzero pair in \(\Lambda\) with \(4d\le8j<m\).
By (1) the rank cannot be \(3/2\).
The [four-column equivalence](Yin_C_A0184_v1.md#statement) excludes every half increment for the two labels.
A finitely generated abelian group is either indicable or finite, and every finite abelian group has a cyclic quotient of its exponent by its invariant factors.
This yields the bound on the residual abelianizations.

## Two labels with isolated phases of order at most four

Use the group
\[
  H=\langle p,q\mid p q^{18}p^{-1}=q^{-18},\
                       q p^2 q^{-1}=p^{-2}\rangle,
       \qquad s=q,\quad t=p q^5 .
\]
It is the amalgam of the Klein bottle groups on \((p,y)\) and \((q,v)\), with \(pyp^{-1}=y^{-1}\) and \(qvq^{-1}=v^{-1}\), identifying \(p^2=v\) and \(y=q^{18}\).
In their semidirect-product normal forms \(\langle p^2,y\rangle\) and \(\langle v,q^{18}\rangle\) are free abelian of rank two, so these identifications embed the edge groups.
A cyclically reduced word of syllable length at least two has positive syllable length in every positive power, while each vertex is torsion-free.
Amalgam normal form therefore gives torsion-freeness of \(H\).
The elements \(s,t\) generate \(H\) since \(p=t s^{-5}\).

The abelianization in the original generators is \(C_4[p]\oplus C_{36}[q]\).
Killing \(s\) gives a cyclic quotient of order four, and killing \(t\) makes \([p]=-5[q]\), leaving a cyclic quotient of order \(\gcd(20,36)=4\).
There is no nonzero integer character.
Nevertheless the quotient onto \(C_{36}\) killing \(p\) gives weights \(a=1,\ b=5\) for the marked generators.
Here \(d=6\), and for every normalized rectangle of the stated kind its regular nullity is at most \(2\cdot6/36=1/3\).
This bound uses no scalar injectivity assumption.
The example shows how simultaneous finite phases can test regular kernels when each isolated phase bound in size two reaches at best one half.

## Assessment history

### Decision finite-phase-estimate

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:29 |
| status | proved |
| reason | Independent review verified the estimate for arbitrary coefficients and its unconditional normalized example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite cyclic quotient estimate and the normalized case without the scalar assumption. |
| argument | [An integer rank for a formal circle parameter](#an-integer-rank-for-a-formal-circle-parameter) | Central product, subgroup integrality, direct integral and deficit inequality. |
| argument | [A short pair of exponents](#a-short-pair-of-exponents) | Lattice index and the uniform order bound. |
| argument | [Two labels with isolated phases of order at most four](#two-labels-with-isolated-phases-of-order-at-most-four) | Amalgam, abelianization, marked quotient and the explicit nullity bound. |
| review | [Finite phase estimate](../audits/reviews/Yin_R_A0178_v1.md#finite-phase-estimate) | Independent whole-argument review. |

## Current assessment

[Selected decision](#decision-finite-phase-estimate)
