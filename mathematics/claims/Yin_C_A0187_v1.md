---
author: Yin
---

# Winding numbers at an extremal cyclic phase

## Statement

Let \(s,t\) lie in a discrete group \(G\), with \(t\) of infinite order, and let \(M(z)\in{\rm GL}_h(\mathbb C(z))\).
Use the unnormalized matrix trace and write \(\nu=\dim_G\ker(sI_h-M(t))\).
Suppose there is an integer character \(\chi:\langle s,t\rangle\to\mathbb Z\) with \(a=\chi(s)\), \(b=\chi(t)\ne0\), and put \(n=|b|/\gcd(|a|,|b|)\).
Then \(\nu\le h/n\).
**If \(n\) does not divide \(h\), this inequality is strict.**
In particular when \(h=2\) and \(n=4\), a half-dimensional kernel is impossible for every such rational matrix, even without scalar group-ring injectivity or a hypothesis on other matrix sizes.

More generally suppose \(C=(s^{-1}I_h) M(t)\) satisfies \(C^r=I_h\) for \(r\ge1\), as at the [finite-window endpoint](Yin_C_A0183_v1.md#transfer-matrices-and-equality).
Put \(t_i=s^its^{-i}\) for \(0\le i<r\), \(F=\langle t_0,\ldots,t_{r-1}\rangle\), and \(g=s^r\), which belongs to \(F\) by the ordered product below.
For a character \(\psi:F\to\mathbb Z\) put \(b_i=\psi(t_i)\) and \(c=\psi(g)\).
Suppose all \(b_i\ne0\).
Let \(f(z)=\det M(z)\) and write \(w_f(R)\) for its winding number along the positively oriented circle of radius \(R\) when it has no zero or pole there.
For every \(\rho>0\) for which \(M\) and \(M^{-1}\) have no pole on any circle of radius \(\rho^{b_i}\),
\[
                     h c=\sum_{i=0}^{r-1} b_i\,w_f(\rho^{b_i}).
 \tag{1}
\]
In particular the order \(k\) of \(f\) at zero equals its degree at infinity (numerator degree minus denominator degree), and \(h c=k\sum_i b_i\).
The statements use ordinary rational determinants of coefficient matrices and the regular trace on the group.

## Extending the unitary twists

Conjugate successive copies of \(M(t)\) past \(s^{-1}I_h\) in the stated order.
The equality \(C^r=I_h\) gives
\[
                 M(t_{r-1})\cdots M(t_0)=g I_h .
\]
The entries on the left belong to \(U(F)\), so the bounded translation on the right belongs to \(\mathcal N(F)\) and its Fourier support puts \(g\) in \(F\).
The subgroup trace preserves the identity in \(U(F)\).
For \(|z|=1\) the character twist in \(\mathcal N(F)\), extended to affiliated operators, gives
\[
           M(z^{b_{r-1}}t_{r-1})\cdots M(z^{b_0}t_0)=z^c g I_h .
 \tag{2}
\]
Here the powers of \(z\) scale translations as complex numbers and do not change the order of the factors.

To extend (2) to every \(z\ne0\), write \(M=P/q\) with \(P\) a polynomial matrix and \(q\) a nonzero scalar polynomial.
Use \(r\) input blocks \(x_0,\ldots,x_{r-1}\) and the bounded equations
\[
 q(z^{b_i}t_i)x_{i+1}=P(z^{b_i}t_i)x_i,\qquad x_r=z^c g x_0 .
\]
For each \(z\ne0\) their left-hand denominators are affiliated units, since each \(t_i\) acts as a bilateral shift.
At fixed \(z\), the first coordinate identifies the joint kernel with the kernel of the difference between the two sides of (2).
In particular its dimension is at most \(h\), and on the unit circle it is \(h\).
The bounded matrix of these equations becomes a matrix polynomial in \(z\) on multiplying by a scalar monomial to clear negative exponents.
The [polynomial rank bound](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) bounds its rank at any nonzero value by its common rank \(rh-h\) at arbitrarily many distinct unit phases.
Indeed the comparison on \(k\) distinct unit phases bounds \((k-d)\) times the rank at the chosen value by \(k(rh-h)\), where \(d\) is the polynomial degree.
Let \(k\) tend to infinity.
The joint kernel therefore has dimension \(h\) at every nonzero value, and faithfulness of the trace gives (2) as an affiliated identity there.

## Differentiating inside the regular trace

Fix an admissible radius \(\rho\).
Near \(\rho\) every matrix in (2) and its inverse is bounded and norm differentiable along the positive real axis, by rational functional calculus of each cyclic unitary.
Take the logarithmic derivative of the product, meaning its ordinary derivative with respect to \(\log\rho\) followed by multiplication by its inverse on the right.
The trace of each product-rule term is the trace of the logarithmic derivative of that factor by cyclicity.
The right side has trace \(hc\).
In the cyclic algebra of \(t_i\), the normalized group trace integrates against Haar probability on the circle.
Jacobi's formula for the ordinary determinant gives for the \(i\)-th trace
\[
 \frac{b_i}{2\pi}\int_0^{2\pi}
      \frac{\rho^{b_i}e^{i\theta} f'(\rho^{b_i}e^{i\theta})}
           {f(\rho^{b_i}e^{i\theta})}\,d\theta
     = b_i\,w_f(\rho^{b_i}).
\]
This proves (1).
For sufficiently large and sufficiently small radii, the winding number equals respectively the degree at infinity and the order at zero.
Subtracting the two versions of (1) gives the difference of those integers times \(\sum_i |b_i|\) equal to zero, proving the assertions on \(k\).

## When the finite phase comes from an integer character

For \(\chi\) on \(\langle s,t\rangle\), twisting at the \(|b|\)-th roots of unity fixes \(t\) and multiplies \(s\) by \(n\) distinct phases.
The right eigenspaces of \(C\) at these phases have equal dimension \(\nu\).
Their sum is algebraically direct by scalar polynomial interpolation and has dimension \(n\nu\le h\).
At equality the sum fills the affiliated module: it is the image of a finite matrix of eigenspace generators and its final support has full trace.
Consequently \(C^n=I_h\).
The preceding result applies with \(r=n\), \(\psi=\chi|_F\), \(c=na\), and all \(b_i=b\).
There exist admissible radii since a rational matrix and its inverse have only finitely many poles.
Formula (1) gives \(h a/b=w_f(\rho^b)\in\mathbb Z\).
The reduced denominator of \(a/b\) is \(n\), so equality requires \(n\mid h\).
This proves strictness, with no assertion of a uniform gap below \(h/n\).

For example take \(\langle s,t\mid s^4=t^3\rangle\).
This is a torsion-free amalgam of two infinite cyclic groups along the indicated power subgroups, by the reduced-word normal form applied to powers of cyclically reduced words.
Its character with \(a=3,\ b=4\) has \(n=4\).
The global quotient after killing \(t\) really has order four, yet equality at \(1/2\) in size two would require an integral winding number \(3/2\).
Thus this example passes the order-four quotient test and is excluded by the regular trace calculation.

## Assessment history

### Decision winding-and-lifted-phases

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:23 |
| status | proved |
| reason | The independent review verified the full argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Integer winding constraint and strictness at a lifted finite phase. |
| argument | [Extending the unitary twists](#extending-the-unitary-twists) | Noncommutative cyclic polynomial equations at every nonzero complex parameter. |
| argument | [Differentiating inside the regular trace](#differentiating-inside-the-regular-trace) | The unnormalized group trace and ordinary cyclic winding numbers. |
| argument | [When the finite phase comes from an integer character](#when-the-finite-phase-comes-from-an-integer-character) | Dimension equality and the divisibility criterion. |
| review | [Winding and lifted phases](../audits/reviews/Yin_R_A0177_v1.md#winding-and-lifted-phases) | Independent review of the stated result and its argument. |

## Current assessment

[Selected decision](#decision-winding-and-lifted-phases)
