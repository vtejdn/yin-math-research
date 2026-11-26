---
author: Yin
---

# A Euclidean lattice bound for positive cyclotomic character weights

## Statement

Let \(H=\langle s,t\rangle\) have abelianization \(C_{p^a}\), with \(p\) prime and \(s\) of infinite order mapping to a generator.
Write \(N=[H,H]\), \(M=N_{\rm ab}\), \(S=\operatorname{Ad}(s)\), and for \(\ell=p^j,\ 1\le j\le a\), put
\[
 L=\ell/p,\qquad d=(p-1)L,\qquad M_\ell=M/\Phi_\ell(S)M .
\]
The group \(M_\ell\) is finite by the [cyclic module calculation](Yin_C_A0212_v1.md#finiteness-and-the-cyclic-module).
Let \(V_d\) denote the Euclidean volume of the unit ball of dimension \(d\), let \(\gamma_d=\max(1,\log d)\), and use the natural logarithm.
If
\[
              |M_\ell|>
              \frac{p^{L/2}(2p^2\gamma_d)^{d/2}}{V_d},                 \tag{1}
\]
then \(M_\ell\) has an additive character whose orbit has strictly positive representatives with sum one on each of the \(L\) slices.
For any complex coefficient matrices of size \(h\) with \(\det(B-yD)\) nonzero as a polynomial, the regular nullity of \(B+At-s(D+Ct)\) is then at most \(h/p\), with unnormalized matrix traces.
For \(d\ge3\) the factor \(\gamma_d\) is \(\log d\).

At the torsion-free scalar-injective order-25 marking \(\chi(s)=1,\chi(t)=7\), a two-by-two four-site rectangle of regular rank \(3/2\) consequently requires
\[
                              |N_{\rm ab}|<18^{20}.
\]
In particular a simple cyclotomic quotient of its commutator abelianization of order \(q^4\), with \(q\) prime, must have \(q<18^5\).

## A short lift in the exact character lattice

Choose an integer \(b\) representing the marked image of \(t\) when \(s\) represents one, and write \(u\) for the image of \(ts^{-b}\) in \(M_\ell\).
Its \(S\)-orbit generates \(M_\ell\), as in the [character-orbit construction](Yin_C_A0212_v1.md#a-short-character-and-its-cyclic-translates).
For an additive character \(\eta\) use the orbit \((\eta(S^iu))_{0\le i<\ell}\) in \((\mathbb R/\mathbb Z)^\ell\).
The evaluation map on the dual is injective.
The sum in each residue class modulo \(L\) is zero modulo one by \(\Phi_\ell(S)=1+S^L+\cdots+S^{(p-1)L}=0\) on this module.

In \(\mathbb R^\ell\) let \(V\) be the subspace on which the sum in each residue class modulo \(L\) vanishes as a real number.
It has dimension \(d\).
Let \(\Delta=V\cap\mathbb Z^\ell\), and let \(\Lambda\subset V\) consist of the exact lifts of the above character orbits modulo \(\Delta\), that is, the vectors whose reduction coordinatewise modulo one is an orbit.
Every orbit has such a lift, by subtracting an integer from one entry per slice to achieve exact sum zero.
There are exactly \(|M_\ell|\) different orbits because a finite abelian group and its character group have the same order.
Thus \(\Delta\subset\Lambda\), with \([\Lambda:\Delta]=|M_\ell|\).
Both are lattices of rational vectors in \(V\), invariant under cyclic coordinate shifts.
In a slice the vectors \(e_i-e_{p}\) for its first \(p-1\) indices relative to its last one have Gram matrix \(I_{p-1}+\mathbf 1\mathbf 1^{\mathsf T}\), of determinant \(p\).
Different slices are orthogonal, so the covolume of \(\Lambda\) in the induced Euclidean metric is \(p^{L/2}/|M_\ell|\).

Set \(R=\sqrt{2/(p^2\gamma_d)}\).
Under (1) the open ball of radius \(R/2\) in \(V\) has volume greater than that covolume.
Projecting its pieces into a fundamental parallelepiped gives two points differing by a nonzero lattice vector: otherwise the projection would preserve their total volume inside a parallelepiped of smaller volume.
Their difference \(x\in\Lambda\) has \(0<\|x\|_2<R\).
For the cyclic coordinate shift \(T\), the rational subspace \(V\cap\mathbb Q^\ell\) is annihilated by \(\Phi_\ell(T)\).
Its irreducibility over \(\mathbb Q\) makes the minimal polynomial of the nonzero rational vector \(x\) equal to \(\Phi_\ell\).
Thus \(T^jx\) for \(0\le j<d\) form a rational basis and also a real basis of \(V\).

## Simultaneously positive representatives by rounding

Take \(v\in V\) with all coordinates \(1/p\) except for one distinguished coordinate in each slice, from which one is subtracted.
Express \(v=\sum_{j=0}^{d-1}\theta_j T^jx\) with real coefficients.
Independently round each coefficient to one of its two neighboring integers, choosing the probabilities so that its mean is \(\theta_j\); an integral coefficient stays fixed.
Writing the rounded integers as \(n_j\), the vector \(y=\sum_j n_j T^jx\) always belongs to \(\Lambda\).
Upon restoring one to the distinguished coordinate in each slice, every coordinate of \(y\) becomes \(1/p+E_i\), where
\[
            E_i=\sum_{j=0}^{d-1}(n_j-\theta_j)(T^jx)_i,\qquad
            s_i=\sum_{j=0}^{d-1}(T^jx)_i^2 .
\]
The sum on each slice now equals one exactly.

For \(s_i>0\), independent bounded summands give
\[
                    \Pr(E_i\le-1/p)\le \exp[-2/(p^2s_i)].
\]
Indeed a centered variable supported on an interval of length \(l\) has log moment generating function at \(t\) at most \(t^2l^2/8\).
Its second derivative is the variance under the exponentially tilted distribution, at most \(l^2/4\) by comparison to the squared deviation from the interval midpoint, and its value and first derivative vanish at zero.
The summands here have interval lengths at most \(|(T^jx)_i|\).
Apply the bound to their negative sum using independence and exponential Markov, optimized at \(t=4/(ps_i)\).
For \(s_i=0\) the probability is zero.

The \(d\) positions contributing to a fixed \(s_i\) are distinct modulo \(\ell\), so \(s_i\le\|x\|_2^2\); summing over \(i\) gives \(\sum_i s_i=d\|x\|_2^2\).
Put \(A_0=2/(p^2\|x\|_2^2)>\gamma_d\).
For \(0<v'\le1\), the inequality \(1/v'-1\ge-\log v'\) gives \(\exp(-A_0/v')\le v'\exp(-A_0)\) since \(A_0\ge1\).
Using \(v'=s_i/\|x\|_2^2\), the union bound shows that the probability of any nonpositive restored entry is at most \(d\exp(-A_0)<1\).
Some rounding therefore gives strictly positive entries on all slices.
Since each slice has \(p\ge2\) entries of sum one, they all lie strictly between zero and one and give representatives of an actual character orbit.
The [finite-phase interpolation for this orbit](Yin_C_A0212_v1.md#statement) gives \(\dim_H\ker(B+At-s(D+Ct))\le h/p\) under the stated pencil hypothesis.

## Numerical consequence for the twenty-fifth component

At \(p=5,\ell=25\) one has \(L=5,d=20\) and \(V_{20}=\pi^{10}/10!\).
The right side of (1) equals \(25\sqrt5\,10!(50\log20/\pi)^{10}\).
It is strictly less than \(18^{20}\): use \(\sqrt5<9/4\), \(\pi>157/50\), and \(\log20<3\) (the sum of the first nine Taylor terms of \(\exp(3)\) exceeds 20).
The remaining integer comparison is
\[
            225\cdot 10!\cdot7500^{10}<4\cdot157^{10}\cdot18^{20}.
\]
At half nullity the [corner condition](Yin_C_A0201_v1.md#statement) supplies the required invertible \(B\); the [fifth-quotient exclusion](Yin_C_A0215_v1.md#statement) and the [cyclotomic annihilator](Yin_C_A0216_v1.md#the-remaining-prime-divisors) identify \(M=M_{25}\).
Since \(1/2>2/5\), (1) cannot hold, proving the announced size bounds.
Below that size condition the lattice argument need not produce the required character.

## Assessment history

### Decision volume-and-randomized-rounding-of-character-orbits

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:36 |
| status | proved |
| reason | Independent review verified the lattice index, covariance estimates, strictly positive weights and the strict order bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All prime powers and the improved size threshold at twenty-five. |
| argument | [A short lift in the exact character lattice](#a-short-lift-in-the-exact-character-lattice) | Integral slice lattice, covolume, volume comparison and the translated basis. |
| argument | [Simultaneously positive representatives by rounding](#simultaneously-positive-representatives-by-rounding) | One-sided tail bounds, weighted sum and positivity on every slice. |
| argument | [Numerical consequence for the twenty-fifth component](#numerical-consequence-for-the-twenty-fifth-component) | The exact comparison with the twentieth power of eighteen. |
| review | [Volume and randomized rounding of character orbits](../audits/reviews/Yin_R_A0192_v1.md#volume-and-randomized-rounding-of-character-orbits) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-volume-and-randomized-rounding-of-character-orbits)
