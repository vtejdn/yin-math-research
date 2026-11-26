---
author: Yin
---

# Finite orbit tests for four power subgroups in the original group

## Statement

Use the torsion-free, scalar-injective [order-24 half-kernel hypotheses](Yin_C_A0288_v1.md#statement), with normalized marks \(s,t\), and put \(t_j=s^jts^{-j},\ g=s^4,\ F=\langle t_0,t_1\rangle\).
For every \(m\ge2\) let
\[
          L_m=\langle t_{-1}^m,t_0^m,t_1^m,t_2^m\rangle\le F.
\]
Then there are \(0\le c,d<m\) such that
\[
                   t_2^c g t_{-1}^d\in L_m,\qquad
                   c+d+3\equiv0\pmod{\gcd(m,6)} .
\]
Thus \(g\in\langle t_2\rangle L_m\langle t_{-1}\rangle\) for each \(m\).
At \(m=2\), at least one of the two explicit elements \(t_2g,\ gt_{-1}\) belongs to \(L_2\).
These are ordinary subgroup membership conditions; no finite-index condition on \(L_m\) enters the proof.

More generally let \(F\) act on any set \(\Omega\), write \(v,w\in\Omega\), and suppose that \(t_0^m,t_{-1}^m\) fix \(v\) and \(t_1^m,t_2^m\) fix \(w\).
Let \(E_a\) be the part of \(M(z)=(Az+B)(Cz+D)^{-1}\) of character \(a\bmod m\) under \(m\)-th-root rotations of \(z\), and \(B_c\) the corresponding part of \(M(z)^{-1}\).
A left pair \((a,b)\) is active when \(E_a(z)E_b(z')\) is nonzero as a rational matrix in two independent scalar variables.
Define an active right pair using \(B_c(z)B_d(z')\).
With indices taken modulo \(m\), the following two events are equivalent:
\[
 \begin{aligned}
    &w=t_1^a t_0^b v\quad\text{for at least one active left pair},\\
    &w=t_2^c t_3^d g v\quad\text{for at least one active right pair}.
 \end{aligned}
\]
The orbit lengths at the specified points may be proper divisors of \(m\), and different pairs may end at the same point.

## Comparing two products on their individual domains

The neighboring infinite cyclic groups in \(H\) have trivial intersection.
Indeed otherwise the [cyclic intersection theorem](Yin_C_A0240_v1.md#the-common-rational-matrix-on-neighboring-cyclic-groups) makes \(\langle t^k\rangle\) normal in \(H\) for some \(k\ge1\).
The [periodic-image theorem](Yin_C_A0288_v1.md#statement) makes the quotient by it cyclic, so \(H\) is solvable and then cyclic by the [solvable quotient theorem](Yin_C_A0278_v1.md#statement).
This contradicts torsion-freeness and \(H_{\rm ab}=C_{24}\).
Conjugation gives the assertion at each neighboring pair.

On \(\ell^2(\Omega)\otimes\ell^2(F)\) use the unitaries \(\widetilde x\) acting by \(x\) on both coordinates.
On the basis the change \((v,h)\mapsto(h^{-1}v,h)\) makes them copies of the regular representation; hence they generate a normal faithful copy of the finite group von Neumann algebra, also at matrix size two.
The [middle transfer identity](Yin_C_A0280_v1.md#two-factors-in-the-actual-finite-regular-twist) gives the equality of affiliated products
\[
 L_1T_0=L_2T_3,\qquad
 L_1=M(\widetilde t_1),\ T_0=M(\widetilde t_0),\
 L_2=M(\widetilde t_2)^{-1},\ T_3=M(\widetilde t_3)^{-1}\widetilde g.
\]

For any \(\xi\in\operatorname{Dom}T_0\cap\operatorname{Dom}T_3\) and \(\eta\in\operatorname{Dom}L_1^*\cap\operatorname{Dom}L_2^*\), this equality implies
\[
                    \langle L_1^*\eta,T_0\xi\rangle
                       =\langle L_2^*\eta,T_3\xi\rangle .
\]
Here is a bounded reduction proving the implication despite possible poles.
The two columns \(Z=(T_0,T_3)^{\mathsf T}\) and \(Y=(L_1^*,L_2^*)^{\mathsf T}\) on their respective common domains are closed and densely defined.
Density follows inside the finite algebra by intersecting spectral truncation domains; finite amplification or the unitarily equivalent copies preserve these domains.
Put \(D_Z=(I+Z^*Z)^{-1/2},\ D_Y=(I+Y^*Y)^{-1/2}\).
The images of these bounded operators are precisely the respective common domains by the graph norm identity.
All entries of \(ZD_Z,YD_Y\) are bounded.
In the finite algebra multiply the displayed affiliated identity by \(D_Y,D_Z\) on the left and right.
The resulting bounded equality is the equality of the products \((L_j^*D_Y)^*(T_k D_Z)\) for the two pairs of indices.
Writing \(\eta=D_Y\eta',\ \xi=D_Z\xi'\) proves the scalar product identity without requiring \(\xi\) to belong to either composite domain.

## Local Fourier blocks and separation of repeated endpoints

On the finite orbit of a point fixed by \(t_i^m\), the operator \(M(\widetilde t_i)\) on that orbit tensored with \(\ell^2(F)^2\) is the sum of the \(m\) permutations \(t_i^a\) on the orbit tensored with \(E_a(t_i)\).
Indeed the cyclic permutation has spectrum in the \(m\)-th roots of unity, and on each eigenspace one evaluates \(M(\omega t_i)\) for a root \(\omega\).
All denominators are affiliated units on the second factor by the infinite order of \(t_i\).
The same formula applies to the inverse transfer and, by taking adjoints, to row evaluations at a finite orbit.

In the scalar product identity use source vectors at \(v\) and target vectors at \(w\).
The \(t_3\)-orbit at \(gv\) is finite since \(t_3^m g=g t_{-1}^m\).
Choose a common bounded right denominator in the second algebra so that all rightmost blocks on both sides, including the last factor \(g\), are bounded after multiplication by it.
Likewise choose a common bounded denominator for the finitely many adjoint blocks at \(w\).
These denominators can be taken as the bounded transforms of the corresponding stacked columns just used, and are affiliated units.
This gives admissible source and target vectors from arbitrary second-coordinate vectors.
Expanding the two finite orbit equations and cancelling the denominators in the finite affiliated algebra of \(F\) gives
\[
 \sum_{t_1^a t_0^b v=w} E_a(t_1)E_b(t_0)
   =\left(\sum_{t_2^c t_3^d g v=w} B_c(t_2)B_d(t_3)\right) g .
\]
Indices in these finite sums are the chosen representatives from zero through \(m-1\).

For a neighboring pair \(x,y\), the linear map
\(\mathbb C(z)\otimes_{\mathbb C}\mathbb C(z')\to U(F)\) sending \(f\otimes h\) to \(f(x)h(y)\) is injective.
For a finite sum choose a common nonzero denominator in the first variable on the left and one in the second variable on the right.
The cleared tensor is a Laurent polynomial in two variables whose monomials map to distinct group elements \(x^i y^j\) because \(\langle x\rangle\cap\langle y\rangle=1\).
Fourier independence proves injectivity.
No multiplicative extension of this map to a two-variable rational field is needed.
Entrywise, the tensors for distinct pairs \((a,b)\) lie in distinct simultaneous character spaces for rotations in the two separate variables.
Consequently a sum at a single endpoint is nonzero exactly when it contains at least one nonzero tensor there.
Apply this separately to the two sides of the last identity and use that \(g\) is a unit.
This proves the orbit test.

## Four powers and the identity coset

Use the left action of \(F\) on \(F/L_m\) and take both points to be the identity coset.
The left pair \((0,0)\) is active, since the zero block \(E_0\) is an invertible rational matrix.
For two invertible denominator corners this follows from the [zero-frequency polynomial](Yin_C_A0287_v1.md#the-missing-products-and-the-numerical-residue), and for one singular denominator corner it follows from the [rank-one Fourier calculation](Yin_C_A0280_v1.md#which-finite-frequencies-must-contribute), including parameter inversion and order two.
The orbit test supplies a right pair with \(t_2^c t_3^d g=t_2^c g t_{-1}^d\in L_m\).
Under the actual character \(F\to C_6\) each \(t_i\) has degree one and \(g\) has degree three, whereas degrees of \(L_m\) lie in the subgroup of multiples of \(m\).
This gives the congruence and the two choices for \(m=2\).

## Assessment history

### Decision two-finite-local-orbits-at-each-end

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:12 |
| status | proved |
| reason | Local finite-orbit expansion and the two-variable tensor injection prove the ordinary subgroup test without any finite-index assumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The matched endpoint test and the four powers. |
| argument | [Comparing two products on their individual domains](#comparing-two-products-on-their-individual-domains) | Normal absorption and the two common graph domains. |
| argument | [Local Fourier blocks and separation of repeated endpoints](#local-fourier-blocks-and-separation-of-repeated-endpoints) | Finite orbit expansions, the last translation and separation of bidegrees. |
| argument | [Four powers and the identity coset](#four-powers-and-the-identity-coset) | The identity-coset test and the degree congruence. |
| review | [Two finite local orbits at each end](../audits/reviews/Yin_R_A0214_v1.md#two-finite-local-orbits-at-each-end) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-two-finite-local-orbits-at-each-end)
