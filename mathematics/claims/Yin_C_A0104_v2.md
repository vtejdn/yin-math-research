---
author: Yin
---
# Biquadratic coefficient failure and two equations in the rational division ring

## Statement

Let \(G\) be torsion-free and suppose that every finite matrix over \(\mathbb Q[G^2]\) has integer regular rank for the unnormalized matrix trace.
Write \(U(G)\) for the algebra of operators affiliated with the group von Neumann algebra in its regular representation and put \(D=\operatorname{Div}_{U(G)}(\mathbb Q[G])\).
Take \(a,b\in\mathbb Q^\times\) with independent square classes and fix \(\alpha^2=a,\ \beta^2=b\) in \(\mathbb C\).
Let \(K=\mathbb Q(\alpha,\beta)\) and let \(E=DK\) be the subring generated inside \(U(G)\).
The following conditions are equivalent.

1. Some finite matrix over \(K[G]\) has nonintegral regular rank.
2. \(E\) is isomorphic to \(M_2(V)\) for a division ring \(V\).
3. \(K\cap D=\mathbb Q\) and there are \(u,v\in D\) with
   \[
       uv+vu=0,\qquad u^2+a v^2=b.
       \tag{1}
   \]
4. There is a finite square matrix over \(K[G]\) of regular nullity exactly \(1/2\).

The intersection in condition 3 is taken with the actual scalar operators.
Equivalently one may require \(u,v\ne0\) in (1) and omit the intersection condition.
There is no such pair consisting of rational functions of individual group elements, even when the two elements generate different cyclic subgroups.
There is also no such pair if each member has some positive power equal to a scalar multiple of a group element.
When one member is \(f(g)\) and the other is affiliated with the normalizer of \(\langle g\rangle\), a necessary inversion identity for \(f\) and a norm equation over the centralizer are given below.
The existence of a pair of unrestricted rational affiliated operators satisfying condition 3 remains unresolved here.

## Argument

### The last quadratic extension

The [Galois degree divisor](Yin_C_A0104_v1.md#the-divisor-in-the-galois-case) gives \(E\simeq M_s(V)\) with \(s^2\mid[K:K\cap D]\).
Its [rank calculation](Yin_C_A0104_v1.md#scalar-extension-at-the-first-coordinate) puts all regular ranks over \(K[G]\) in \(s^{-1}\mathbb Z\).
In particular condition 1 implies \(s=2\) and \(K\cap D=\mathbb Q\).
The same two results for the quadratic field \(\mathbb Q(\alpha)\) show that \(L=D[\alpha]\) is a division ring.
If \(K\cap D=\mathbb Q\), then \(1,\alpha\) are a basis of \(L\) over \(D\).
Changing the sign of \(\alpha\) and fixing \(D\) defines an automorphism of \(L\), by \(\alpha^2=a\) and uniqueness of these coordinates.

We claim that \(\beta\notin L\) in this case.
Otherwise write \(\beta=d+e\alpha\), \(d,e\in D\).
Since \(\beta\) is central in \(L\), the sign automorphism sends it to another central root of \(T^2-b\).
The center is a field, so this root is \(\beta\) or \(-\beta\).
Comparing coordinates would give \(\beta\in D\) or \(\beta/\alpha\in D\), each of which is a nonrational scalar in \(K\).
Thus \(1,\beta\) are independent over the division ring \(L\), and evaluation at \(\beta\) identifies
\[
                  E=L[T]/(T^2-b)
\]
for a central indeterminate \(T\).
The quotient is a division ring exactly when \(T^2-b\) is irreducible in \(L[T]\).
Indeed left ideals containing \((T^2-b)\) are principal by division with remainder and correspond to monic right divisors of \(T^2-b\).
If the polynomial is irreducible, every nonzero element of the quotient generates its unit left ideal, and the left inverse obtained this way is two-sided by finite dimension over \(L\).
A proper monic factorization of the quadratic has the form \((T+w)(T-w)\) with \(w^2=b\), by comparison of its two coefficients.
The two linear factors give nonzero zero divisors in the quotient.
Writing \(w=u+\alpha v\) and comparing its square in the \(D\)-basis \(1,\alpha\) gives exactly (1).
This proves the equivalence of conditions 2 and 3.

The [square test](Yin_C_A0096_v2.md#the-square-test-for-a-scalar-affiliated-element) implies that every element of \(D\) algebraic over \(\mathbb Q\) is scalar.
With \(K\cap D=\mathbb Q\), the choices \(v=0\) or \(u=0\) in (1) would therefore put \(\pm\beta\) or \(\pm\beta/\alpha\) in \(D\).
Conversely, if \(K\cap D\ne\mathbb Q\), this intersection contains one of the three quadratic subfields of \(K\).
If \(\alpha\in D\), then \(w=u+\alpha v\in D\) is algebraic and hence scalar, so \(u=w-\alpha v\) commutes with \(v\).
Equation (1) then forces one member of the pair to vanish.
If \(\alpha\notin D\), either \(\beta\) or \(\alpha\beta\) is in \(D\), and consequently \(\beta\) is a central element of \(L\).
In the division ring \(L\), the equation \((w-\beta)(w+\beta)=0\) forces \(w=\pm\beta\).
Comparison in the \(D\)-basis \(1,\alpha\) again gives \(u=0\) or \(v=0\), according as \(\alpha\beta\) or \(\beta\) lies in \(D\).

### A finite matrix with half-dimensional kernel

Under condition 3, the element \(w=u+\alpha v\) belongs to \(L\), whereas \(\beta\notin L\).
Consequently \(e=(1+w/\beta)/2\) is an idempotent distinct from zero and one in \(E=M_2(V)\).
Its image and kernel are complementary one-dimensional \(V\)-spaces, so it is conjugate over \(E\) to a diagonal matrix unit.
The two diagonal units are equivalent and sum to one, giving \(eU(G)\) regular dimension \(1/2\).
Since \(\beta-w=2\beta(1-e)\), its right kernel in \(U(G)\) equals \(eU(G)\).
This identifies the trace of the analytic kernel projection even when the idempotent is not selfadjoint.

Use the [matrix-inverse description of rational closure](../audits/literature/Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures) for \(u,v\in D\), as in the [prime-index witness](Yin_C_A0036_v1.md#the-rank-and-a-finite-matrix-over-the-group-ring).
The rational closure contains the division closure, so there exist matrices \(Q_i\in M_{n_i}(\mathbb Q[G])\), invertible over \(U(G)\), and constant coordinate rows \(l_i\) and columns \(r_i\) with \(u=l_1Q_1^{-1}r_1\), \(v=l_2Q_2^{-1}r_2\).
The finite matrix
\[
              \begin{pmatrix}
               \beta & l_1 & \alpha l_2\\
               r_1 & Q_1 & 0\\
               r_2 & 0 & Q_2
              \end{pmatrix}
              \in M_{1+n_1+n_2}(K[G])
              \tag{2}
\]
reduces by invertible affiliated row and column operations to \(\operatorname{diag}(\beta-w,Q_1,Q_2)\).
It has nullity \(1/2\), proving condition 4, and rank-nullity gives condition 1.
The matrix inverses in this construction allow arbitrary elements of the actual rational division ring without an Ore assumption on \(\mathbb Q[G]\).
Here \(T\) commutes with \(L\), whereas the norm equation in the [prime-index group extension](Yin_C_A0036_v1.md#a-one-dimensional-module-at-a-prime-index-failure) incorporates conjugation by a coset representative.

### Rational functions on two cyclic subgroups

Suppose that \(u=f(g)\), \(v=q(h)\) are a pair as in condition 3, where \(g,h\in G\) and \(f,q\in\mathbb C(T)\) are defined in the respective cyclic affiliated algebras.
A scalar member would commute with the other member and violate (1), so \(g,h\) have infinite order and \(f,q\) are nonconstant.
Evaluation at either element embeds \(\mathbb C(T)\) by the Haar spectral law of an infinite-order group element.

Put \(H=\langle g\rangle\cap\langle h\rangle\).
The normal element \(u^2=b-av^2\) is affiliated with the two cyclic von Neumann algebras.
Thus its spectral projections belong to both bounded algebras, whose intersection is \(\mathcal N(H)\).
Indeed an element of the intersection has Fourier support in both subgroups, so the expectation onto \(\mathcal N(H)\) fixes it.
Consequently \(u^2\) and \(v^2\) are affiliated with \(\mathcal N(H)\).
If \(H\) is trivial, both squares are constant, which is impossible for the given nonconstant rational functions.

Otherwise choose \(z=g^m\) generating \(H\), with \(m>0\), and write \(h^n=z^\epsilon\), \(n>0\), \(\epsilon=\pm1\).
On the circle for \(g\), the rotation \(T\mapsto\zeta T\) at a primitive \(m\)-th root \(\zeta\) fixes the entire affiliated algebra of \(H\).
Thus \(f(\zeta T)^2=f(T)^2\) as rational functions, since equality almost everywhere on the circle implies equality in \(\mathbb C(T)\).
It follows in that field that \(f(\zeta T)=f(T)\) or \(f(\zeta T)=-f(T)\).
In the second case \(m\) is even.
Use \(i=0\) in the first case and \(i=m/2\) in the second.
The function \(T^{-i}f(T)\) is rotation invariant and belongs to \(\mathbb C(T^m)\), the fixed field, as follows by expanding in the basis \(1,T,\ldots,T^{m-1}\) over that field.
Hence \(u=g^i f_0(z)\) with \(f_0(z)\ne0\), and the same calculation for \(h\) gives \(v=h^j q_0(z)\), using \(h^n=z^\epsilon\).
Both rational factors in \(z\) are units commuting with \(g,h\).
Cancellation in \(uv+vu=0\) would give \(g^i h^j+h^j g^i=0\) in the actual complex group ring, although its augmentation is two.
This excludes arbitrary separate cyclic rational functions satisfying both equations (1).
The [Cayley transform argument](Yin_C_A0102_v1.md#exclusion-for-cayley-transforms-of-actual-group-elements) excludes anticommutation alone for its particular two functions.

### One cyclic input and the normalizer

Suppose \(u=f(g)\) as above and \(v\) is affiliated with \(\mathcal N(J)\), where \(J=N_G(\langle g\rangle)\).
This includes the full commensurator of \(\langle g\rangle\) whenever that subgroup normalizes \(\langle g\rangle\).
Write \(C=C_G(g)\).
Every element of \(C\) commutes with \(f(g)\).
If \(J=C\), anticommutation is impossible for a pair of units.
Otherwise \(C\) has index two in \(J\), and an element \(s\in J\setminus C\) conjugates \(g\) to \(g^{-1}\).
Every affiliated operator of \(\mathcal N(J)\) is uniquely \(d_0+d_1s\) with \(d_i\) affiliated with \(\mathcal N(C)\).
Indeed the order-two character of \(J/C\) defines a trace-preserving sign automorphism \(\theta\) of \(\mathcal N(J)\) and its affiliated algebra.
The even and odd parts of \(v\) are \((v+\theta(v))/2\) and \((v-\theta(v))/2\).
The even part and the odd part multiplied on the right by \(s^{-1}\) are fixed by \(\theta\).
The bounded fixed algebra is \(\mathcal N(C)\) by Fourier support, and its affiliated algebra is the affiliated fixed algebra by polar decomposition and the spectral projections of the absolute value.

For \(v=d_0+d_1s\), uniqueness of these two parts in the anticommutator gives
\[
       2 f(g)d_0=0,\qquad d_1\bigl(f(g)+f(g^{-1})\bigr)=0 .
\]
Since \(f(g)\) is a unit, \(d_0=0\).
Since \(v=d_1s\) is a unit, \(d_1\) is an affiliated unit and its inverse is again fixed by \(\theta\).
It follows that \(f(T^{-1})=-f(T)\) identically, by injectivity on \(\mathbb C(T)\).
With \(\delta(d)=sds^{-1}\), the remaining equation becomes
\[
                 d_1\delta(d_1)s^2=(b-f(g)^2)/a .
\]
Conversely these two identities give (1) for \(u=f(g)\), \(v=d_1s\).
For condition 3 the two elements must also lie in \(D\) and the scalar intersection must be \(\mathbb Q\).
In particular membership of the second input in this normalizer excludes the pair whenever the inversion identity fails.
For a commensurator that does not normalize \(\langle g\rangle\), this two-coset argument gives no conclusion about inputs outside \(J\).

### Powers that are group monomials

Put \(t=v^2\) for a pair as in condition 3.
If \(t\) were scalar, the two linear factors of \(T^2-t\) over \(\mathbb C\) and the square test for the nonscalar \(v\) would make \(v^2-t\) an affiliated unit.
Thus \(t\) is nonscalar, and the [single-generator calculation](Yin_C_A0096_v2.md#one-rational-affiliated-generator) embeds \(\mathbb C(T)\) by \(T\mapsto t\).
Suppose \(u^m=cg\) and \(v^n=eh\) with \(m,n>0\), \(c,e\in\mathbb C^\times\), \(g,h\in G\).
Then
\[
                    c^2g^2=(b-at)^m,\qquad e^2h^2=t^n.
\]
The two rational functions on the right are algebraically dependent over \(\mathbb C\) because they belong to \(\mathbb C(t)\).
They are multiplicatively independent modulo constants, by their orders at \(t=b/a\) and \(t=0\), respectively.
Hence \(g^2,h^2\) commute and generate a copy of \(\mathbb Z^2\).
Its two generators are algebraically independent in the regular group algebra by linear independence of the group basis, contradicting the displayed equations.

The [quaternion tracial construction](Yin_C_A0102_v1.md#statement) exhibits fractional ranks with a different trace on the free group algebra.
Its tracial representation supplies no pair in the rational division ring for the canonical group trace.

## Assessment history

### Decision biquadratic-equations

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:15 |
| status | proved |
| reason | The independent review verifies the equivalences in the actual regular representation under rational square-group integrality. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The equivalence for a biquadratic field, a half-nullity matrix and the exclusions on cyclic inputs. |
| argument | [Proof](#argument) | The tower of quadratic extensions, finite matrix realization and cyclic obstructions. |
| review | [Whole finding](../audits/reviews/Yin_R_A0141_v2.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Galois divisor](Yin_C_A0104_v1.md#decision-galois-divisor) | Matrix index and regular rank denominators for quadratic and biquadratic scalar extensions. |
| dependency | [Square test](Yin_C_A0096_v2.md#decision-univariate-degree) | Scalar translates of nonscalar rational affiliated elements and their rational evaluation. |

## Current assessment

[Selected decision](#decision-biquadratic-equations)
