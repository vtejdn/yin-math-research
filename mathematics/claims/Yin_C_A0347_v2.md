---
author: Yin
---

# A diffuse Brown component and exponential growth for algebraic signed commutator products

## Statement

Let \(G\) be a torsion-free sofic group whose nonzero complex group-ring scalars are regularly injective.
For \(X\in M_k(\overline{\mathbb Q}G)\) either \(X\) is annihilated by a nonzero scalar polynomial with algebraic coefficients, or its probability Brown measure has diffuse mass at least \(1/k\).
In the first case it is purely atomic with finite algebraic support.
More precisely if its measure is concentrated on the zero set of a scalar polynomial \(p\in\overline{\mathbb Q}[z]\), then \(p(X)^k=0\).

For the [two-sign product of involutions](Yin_C_A0345_v1.md#four-step-words-and-the-commutator-kernel) \(A=J_gTJ_hT^{-1}\), assume the group is sofic and \(T\) is a fixed invertible four-square matrix with algebraic coefficients.
If the two-square rectangle has noninteger nullity \(\delta\), then \(\mu_A\) has diffuse mass at least \(1/4\).
There is \(s_T\in(0,1]\), depending on the numerical assembly and independent of the group, such that with \(R=r(A)^2\),
\[
                 \frac{s_T^2}{8}\le (R+1)^2(R^2+1-4\delta).
\]
Thus at a half kernel \(r(A)\ge(1+s_T^2/72)^{1/4}>1\).
If \(r(A)=1\), then \(\delta\le1/2-s_T^2/128\).
These tests apply at every numerical character rank and after every coefficient embedding of an algebraic rectangle, with constant taken for the embedded assembly.

## Generalized kernels and diffuse mass

For any algebraic polynomial \(p\), put \(Y=p(X)\).
Polynomial spectral mapping for Brown measure gives \(\mu_Y(\{0\})=\mu_X(p^{-1}(0))\); this follows directly by factoring \(p(z)-w\) in the logarithmic potential formula at each \(w\) and using determinant multiplicativity.
If \(Y^j\ne0\), some entry is a nonzero group-ring scalar and the unnormalized regular rank of \(Y^j\) is at least one.
Unless a power vanishes, the [Brown atom formula](Yin_C_A0347_v1.md#statement) therefore gives \(\mu_X(p^{-1}(0))\le1-1/k\).
All atoms of \(\mu_X\) are algebraic by that same result.
If the total atomic mass exceeds \(1-1/k\), finitely many algebraic atoms already exceed it.
Taking their distinct linear factors as \(p\) gives a vanishing power.
Conversely a polynomial identity makes the spectrum finite and algebraic, hence contains the Brown support.
For the exponent assertion, if \(j\) is the least positive exponent with \(Y^j=0\), each successive increment from \(\ker Y^{i-1}\) to \(\ker Y^i\), \(1\le i\le j\), has dimension at least \({\rm rk}(Y^{j-1})\).
Indeed the map from the last quotient \(\ker Y^j/\ker Y^{j-1}\) into the \(i\)-th quotient induced by \(Y^{j-i}\) is injective, and the last quotient has dimension \({\rm rk}(Y^{j-1})\).
This is a statement of affiliated modules.
The latter rank is at least one by scalar injectivity, so summing gives \(j\le k\).

## Absence of a polynomial annihilator for the signed product

Write \(J=J_g,\ L=TJ_hT^{-1}\).
The product \(A=JL\) has a nonzero eigenspace at one, since its graph intersections include the \((+,+)\) space of dimension \(\delta>0\).
If a nonzero polynomial annihilated \(A\), take the polynomial primary idempotent for the root one and multiply it by the highest power of \(A-I\) which is nonzero on its range.
This gives a nonzero group-ring matrix with image in \(\ker(A-I)\), hence in \(\ker(A^2-I)\).
On that kernel \(J,L\) commute, and the four polynomial joint idempotents split it into spaces of dimension \(\delta<1\).
At least one idempotent applied to the matrix gives a nonzero group-ring matrix in such a space.
Its regular rank is at least one by scalar injectivity, a contradiction.
Thus the first part gives the claimed diffuse component and \(Q=A^4-I\) has no vanishing power.

## A quantitative lower bound for the spectral radius

Apply the [uniform logarithmic estimate](Yin_C_A0347_v1.md#logarithmic-tails-for-roots-of-all-powers) to the fixed group-ring word expression \(Q\) and its marked quotients, obtaining constants \(C\ge0,L_0\ge1\).
For every \(j\) the measure \(\nu_j\) of \(|Q^j|^{1/j}\) assigns positive singular values mass at least \(1/4\) by scalar injectivity and the absence of nilpotence.
Take \(s_T=\exp(-8(C+\log L_0+1))\).
There is mass at least \(1/8\) in the closed interval \([s_T,L_0]\), both for each \(\nu_j\) and for its weak limit.
Thus \(\int|w|^2\,d\mu_Q(w)\ge s_T^2/8\).

The word trace gives \(t(A^2)=0\) in normalized four-coordinate trace, and \(\ker(A^2-I)\) has normalized dimension \(\delta\).
Put \(\mu=\mu_{A^2}\).
Its support lies in the disk of radius \(R\); its first moment is zero and its atom at one has mass at least \(\delta\) by the generalized-kernel formula.
As \(A\) is conjugate to its inverse, \(R\ge1\).
The Brown measure of \(Q\) is the image of \(\mu\) under \(z\mapsto z^2-1\).
Consequently
\[
 \frac{s_T^2}{8}\le\int |z^2-1|^2\,d\mu(z)
 \le(R+1)^2\!\left(\int |z+1|^2\,d\mu(z)-4\mu(\{1\})\right)
 \le(R+1)^2(R^2+1-4\delta).
\]
At \(R=1\) this gives the stated gap.
At \(\delta=1/2\) and \(R\le2\) it implies \(R^2\ge1+s_T^2/72\).
For \(R>2\) the spectral radius conclusion already holds.
Sofic coefficient-embedding invariance preserves the rank of the original algebraic rectangle, allowing the same conclusions on each embedded set of coefficients.
