---
author: Yin
---

# The order-twenty-four middle identity excludes a common double pole

## Statement

Under the [order-24 half-rank hypotheses](Yin_C_A0290_v1.md#statement), the two determinant polynomials \(\det(Az+B)\) and \(\det(Cz+D)\) cannot have a double zero at the same point of the unit circle.
Consequently a double zero in either determinant requires two distinct double zeros, one for each determinant, and the [diagonal factorization](Yin_C_A0292_v1.md#the-two-rational-forms) with \(u=(z-\beta)/(z-\alpha)\).
This excludes the whole common-root unipotent case.

## The subgroup detected by the lower left entry

Suppose there were a common double zero at \(\alpha\).
By the [unipotent factorization and its lower left entry](Yin_C_A0292_v1.md#a-group-element-reverses-a-power-in-the-common-root-case), there are nonzero constants \(c,\lambda,\mu\), a constant \(d\), and a nonzero affiliated scalar
\[
             X=d+c^2\big(\mu u(t_1)+\lambda u(t)\big),
     \qquad u(z)=(z-\alpha)^{-1},\qquad
              vXv=\gamma X,\quad v=s^{-2},\quad |\gamma|=1 .
\]
Some \(h\in H\) conjugates a nonzero power of \(s\) to its inverse.
Define
\[
 K=\{k\in H:k s^n k^{-1}=s^{\,\varepsilon n}
                     \text{ for some } n>0,\ \varepsilon\in\{1,-1\}\}.
\]
Since \(s\) has infinite order, the sign is unique; common multiples show \(K\) is a subgroup and the sign gives a homomorphism on it.
It contains \(s\) with positive sign and \(h\) with negative sign.
It does not contain \(t\), for otherwise the sign would be a homomorphism on \(H\) negative somewhere.
Every such homomorphism factors through \(H_{\rm ab}=C_{24}\), and the even mark \(4\) of \(t\) forces its sign to be positive as well.

In fact \(X\) is affiliated over \(K\).
Write \(X=U|X|\).
The spectral projections of \(|X|\) commute with \(v\) by the covariance of \(X\).
Support of their square-summable Fourier coefficients lies on finite conjugation orbits under \(v\), hence in the positive part of \(K\).
Likewise \(vUv=\gamma U\), so the Fourier support of its bounded polar part lies on finite orbits of \(k\mapsto vkv\), which belong to the negative part of \(K\).
Bounded elements with Fourier support in \(K\) belong to the subgroup von Neumann algebra, by its trace-preserving expectation.
These projection and polar inclusions give \(X\in U(K)\).

## Comparing two copies over the subgroup

Form the amalgamated free product \(H*_K H\), with \(a,b\) the images of \(t\) in the two vertex groups.
Their intersection is \(K\) by the group normal form, so \(a\ne b\).
Inclusion in the double preserves the regular affiliated operators by decomposition into subgroup cosets, and the two copies of \(X\) agree because \(X\in U(K)\).
The element \(s\) is the same in the two copies.
Subtracting the two expressions for \(X\) gives
\[
       Y=u(a)-u(b),\qquad sYs^{-1}=-\lambda Y/\mu .
\]
The affiliated scalar \(Y\) is nonzero since \(u(a)=u(b)\) would give \(a=b\) by inversion.
The identity \(u(a)^*=-\alpha-\alpha^2 u(a)\) and its counterpart for \(b\) give \(Y^*=-\alpha^2Y\).
Taking adjoints forces \(-\lambda/\mu\) to be real.
Its modulus is one, since conjugation preserves the singular value distribution and \(Y\) is nonzero.
Thus \(s^2 Y s^{-2}=Y\).

First suppose \(t^j\in K\) for some \(j>0\).
Then some positive power of \(s\) commutes with \(t^{2j}\) by the definition of \(K\).
Set \(n=2j\ge2\), \(b_0=a^n=b^n\in K\), and choose a positive even \(m\) such that \(s^m\) commutes with \(b_0\).
The following finite group-ring element is fixed by conjugation by \(s^m\):
\[
       (b_0-\alpha^n)Y=
               \sum_{i=0}^{n-1}\alpha^{n-1-i}(a^i-b^i).
\]
Its coefficient at \(a\) is \(\alpha^{n-2}\ne0\), since \(a\) has infinite order and \(a\notin K\) cannot coincide with any \(b^i\) in the other vertex group.
Its support is finite, so a power of \(s^m\) commutes with \(a\).
In its original vertex group this implies \(t\in K\), a contradiction.

## A bounded resolvent when the two cyclic copies are free

It remains that \(\langle t\rangle\cap K=\{1\}\).
Every alternating product of nonzero powers of \(a,b\) is then reduced in \(H*_K H\); hence \(a,b\) freely generate.
Let \(F(z)=(1+z)/(1-z)\).
As affiliated operators one has
\[
          T=F(a/\alpha)+F(\alpha b^{-1})=-2\alpha Y .
\]
The sum is skew-adjoint in the finite affiliated algebra, and \(Z=(I+T)^{-1}\) is bounded of norm at most one.
Conjugation by \(s^2\) fixes \(Z\).
We show its group Fourier coefficient at \(a\) is nonzero.

For a complex number \(r\) with \(|r|<1\) put
\[
       Z_r=\big(I+F(ra/\alpha)+F(r\alpha b^{-1})\big)^{-1}.
\]
Each \(F\)-term has positive real part by the scalar disk formula on the unitary spectrum.
The sum with \(I\) has real part at least \(I\), so has an inverse of norm at most one (apply the norm lower bound also to its adjoint).
The matrix coefficient of \(Z_r\) at \(a\) is holomorphic on the disk.
For \(r\) near zero the norm-convergent Taylor expansion uses only positive words in \(a,b^{-1}\); each term of degree \(k\) is homogeneous of word length \(k\) in these two generators.
Its degree-zero term is \(I/3\), and its degree-one term is \(-2r(a/\alpha+\alpha b^{-1})/9\).
By freeness no positive word of any other length represents \(a\).
It follows first near zero and then by holomorphic continuation throughout the disk that the coefficient at \(a\) is \(-2r/(9\alpha)\).

Along real \(r\uparrow1\) the two summands in the inverse denominator converge in measure to their affiliated boundary values by the circle functional calculus, hence so do their sums.
The resolvent identity writes \(Z_r-Z=Z_r(T-T_r)Z\), where \(T_r=F(ra/\alpha)+F(r\alpha b^{-1})\).
Bounded multipliers of norm at most one preserve convergence to zero in measure by the singular value bound, so \(Z_r\to Z\) in measure.
Uniform boundedness implies \(L^2\) convergence for the finite trace, by splitting the squared singular value integral at an arbitrary fixed positive threshold.
Consequently the coefficient of \(Z\) at \(a\) is \(-2/(9\alpha)\ne0\).

Since \(s^2\) fixes this bounded operator by conjugation, its square-summable Fourier coefficients are constant on the conjugacy orbit of \(a\) under \(s^2\).
The nonzero coefficient forces that orbit to be finite.
Thus some nonzero power of \(s\) commutes with \(a\), again giving \(t\in K\) in its original vertex group.
The contradiction covers both possibilities for \(\langle t\rangle\cap K\).

## Assessment history

### Decision excluding-a-common-double-pole

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:12 |
| status | proved |
| reason | The two alternatives in the subgroup double both force a forbidden power centralizer, excluding a common double pole. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The exclusion after the double-pole classification. |
| argument | [The subgroup detected by the lower left entry](#the-subgroup-detected-by-the-lower-left-entry) | The signed conjugacy subgroup and the lower left entry. |
| argument | [Comparing two copies over the subgroup](#comparing-two-copies-over-the-subgroup) | The intersecting cyclic case and the Fourier coefficient after clearing. |
| argument | [A bounded resolvent when the two cyclic copies are free](#a-bounded-resolvent-when-the-two-cyclic-copies-are-free) | The free cyclic case and the nonzero coefficient of a bounded resolvent. |
| review | [Excluding a common double pole](../audits/reviews/Yin_R_A0214_v1.md#excluding-a-common-double-pole) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-excluding-a-common-double-pole)
