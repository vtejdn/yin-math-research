---
author: Yin
---

# Central determinant values and bounded-length relations in the order-24 common-power case

## Statement

Use the [order-24 common-power hypotheses](Yin_C_A0258_v1.md#statement) for a rectangle of regular rank \(3/2\).
Write \(t_i=s^its^{-i}\), \(g=s^4\), \(F=\ker(\chi\bmod4)\), \(h=t^k\), and \(t_i^k=h^{\epsilon^i}\) for \(\epsilon\in\{1,-1\}\).
Here \(h\) is central of infinite order in \(F\), and \(\psi=\chi/4:F\to C_6\) has \(\psi(t_i)=1,\ \psi(g)=3\).
For \(M(z)=(Az+B)(Cz+D)^{-1}\), put
\[
 u(z)=\det(Az+B),\quad v(z)=\det(Cz+D),\quad
 D_k(y)=\prod_{x^k=y}u(x)/v(x).
\]
The following scalar rational functions have modulus one on the unit circle after removing any removable singularities:
\[
             D_k(y)\quad(\epsilon=1),\qquad
             D_k(y)D_k(y^{-1})\quad(\epsilon=-1).
\]
The unit-circle zeros of \(u\) and of \(v\), counted with multiplicity, must therefore match on each orbit under multiplication by \(k\)-th roots of unity for \(\epsilon=1\); for \(\epsilon=-1\) include inversion in the orbit.
Both lists are nonempty.
For given coefficients, this tests \(k\) by the orders of the root-of-unity ratios of paired roots, also permitting their products when \(\epsilon=-1\).

There is a group test using only four consecutive cyclic factors.
For \({\bf r}=(r_0,r_1,r_2,r_3)\in\{0,\ldots,k-1\}^4\) define
\[
          P_{\bf r}=t_3^{r_3}t_2^{r_2}t_1^{r_1}t_0^{r_0},\qquad
          e({\bf r})=\sum_{i=0}^3\epsilon^i r_i .
\]
Whenever \(P_{\bf r}=h^nP_{\bf s}\) in \(F\), record the integer \(e({\bf r})-e({\bf s})-kn\); the quotient \(F/\langle h\rangle\) identifies the relevant pairs and \(h\) has infinite order, so each \(n\) is unique.
At least one recorded integer is nonzero.
If \(d\) divides all of them and \(d\ge1\), then
\[
           d-b\gcd(k,d)\ \le\ 8+\lfloor d/2\rfloor,\qquad
   b=\left|\bigcup_{i=0}^3\{\alpha^{k\epsilon^i}:
                              |\alpha|=1,\ v(\alpha)=0\}\right|.
\]
In particular their positive gcd is at most \(16+2bk\), and its largest divisor coprime to \(k\) is at most 20 for the positive sign or 24 for the negative sign.
Thus a coefficient-independent exclusion is available even when some four-factor products collide: it suffices that all the integers vanish, or that their common divisors violate the inequality with \(b=2\) or \(4\), respectively.
The first alternative includes injectivity of \({\bf r}\mapsto P_{\bf r}\langle h\rangle\).
The test uses actual center exponents in this finite collection; it does not require a character on all of \(F\) with the assigned integer values.

## Compression to a central arc

The [ordered group identity](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) is \(M(t_3)M(t_2)M(t_1)M(t_0)=g I_2\).
For a closed arc on the circle disjoint from the finitely many \(k\)-th powers of unit-circle zeros of \(u,v\) and their inverses, let \(E\) be its spectral projection for \(h\).
Inside the corner \(E\mathcal N(F)\), each compressed \(M(t_i)\) and its inverse are bounded by cyclic spectral calculus.
The right side is unitary in the matrix corner.
Multiplicativity of the bounded Fuglede--Kadison determinant for the restricted finite trace therefore gives
\[
                     \sum_{i=0}^3\operatorname{Tr}_2
                         \big(E\log |M(t_i)|\big)=0 ,
\]
where the logarithms are taken on the compressed spaces. [Determinant and trace](../audits/literature/Den09/Yin_U001.md#fk-determinant)
To compute a summand, use the Haar law of \(t_i\).
If its scalar coordinate is \(x\), the coordinate of \(h\) is \(y=x^{k\epsilon^i}\).
Normalized Haar measure disintegrates as the uniform measure on the \(k\) roots over each \(y\).
The ordinary matrix identity \(\operatorname{tr}_2\log|M(x)|=\log|u(x)/v(x)|\) gives the summand as \(1/k\) times the integral over the arc of \(\log|D_k(y^{\epsilon^i})|\).
Varying the arc and using continuity away from the finitely many points proves the modulus assertions there.
The rational functions in the statement extend through their boundary exceptions with modulus one, since a zero or pole after cancellation would contradict the modulus on nearby regular circle points.

For a nonzero polynomial \(v\), the product \(V(y)=\prod_{x^k=y}v(x)\) is a polynomial of degree \(\deg v\); each root \(\alpha\) of \(v\) contributes a root at \(\alpha^k\) with its original multiplicity.
This follows by factoring \(v\) into linear terms.
Applying this calculation to \(u,v\) gives the orbit multiplicities in the statement, including both reciprocal points for the negative sign.
Nonemptiness follows from the [two required unit-circle poles](Yin_C_A0244_v1.md#statement).
In particular \(b\le2\) for \(\epsilon=1\) and \(b\le4\) for \(\epsilon=-1\).

## Substitution on the finite product expansion

The cyclic field \(\mathbb C(t_i)\) has basis \(1,t_i,\ldots,t_i^{k-1}\) over \(\mathbb C(h)\).
Each coefficient of the expansion of \(M(t_i)\) in this basis is a Laurent polynomial in \(h\) divided by \(V(h^{\epsilon^i})\).
Indeed write \(M(z)=(Az+B)\operatorname{adj}(Cz+D)/v(z)\), multiply numerator and denominator by \(\prod_{\eta^k=1,\eta\ne1}v(\eta z)\), and reduce the numerator powers using \(t_i^k=h^{\epsilon^i}\).
Expanding the original ordered identity therefore gives an equality
\[
                            \sum_{\bf r} E_{\bf r}(h)P_{\bf r}=gI_2
\]
over central rational coefficients with possible denominators only from the displayed \(V\)'s.
Distinct cosets modulo \(\langle h\rangle\) are independent over this central field: clear one common denominator and compare the disjoint Fourier supports in the group ring.
Thus \(g=h^{n_*}P_{{\bf r}_*}\) for some tuple, and the coefficient equalities hold separately on every coset.

Fix a positive common divisor \(d\) of the recorded integers, and let \(L\) be a representative of \(k n_*+e({\bf r}_*)\) modulo \(d\) with \(|L|\le\lfloor d/2\rfloor\).
For \(\zeta\in\mu_6\) and \(z\in\mu_d\), set
\[
          h\mapsto \zeta^k z^k,\qquad t_i\mapsto\zeta z^{\epsilon^i}.
\]
These scalars respect \(t_i^k=h^{\epsilon^i}\): for the negative sign one has \(k\equiv-k\bmod6\) by applying \(\psi\) to the original common-power equality.
For \({\bf r},{\bf s}\) in the same central coset with \(P_{\bf r}=h^nP_{\bf s}\), the assigned values of the two sides are equal.
The powers of \(z\) agree by the common divisor hypothesis, and the powers of \(\zeta\) agree by the actual character \(\psi\).
In particular the value assigned to \(g\) is \(\zeta^3 z^L\).
Thus one may evaluate each central coefficient equality at \(\zeta^k z^k\) and sum it with the assigned coset value, provided the finitely many central denominators there are nonzero.
This is a calculation on the four-factor expansion; it asserts no multiplicative extension of this assignment to arbitrary elements of \(F\).

For fixed \(\zeta\), a bad \(z\) must send \(\zeta^k z^k\) to one of the \(b\) boundary points in the statement.
On \(\mu_d\), each point has at most \(\gcd(k,d)\) preimages.
Thus at at least \(d-b\gcd(k,d)\) distinct \(z\) the preceding calculation yields the numerical identity
\[
               M(\zeta z^{\epsilon^3})M(\zeta z^{\epsilon^2})
                 M(\zeta z^\epsilon)M(\zeta z)=\zeta^3 z^L I_2.
\]

## Counting the good phases and returning to the closed chain

Multiply this identity by the product of the four ordinary scalar denominators \(v(\zeta z^{\epsilon^i})\).
Each matrix numerator \((Aw+B)\operatorname{adj}(Cw+D)\) and each denominator \(v(w)\) has degree at most two.
Before the factor \(z^L\), the left and right terms therefore both have Laurent exponents in the interval \([0,8]\) for \(\epsilon=1\), or in \([-4,4]\) for \(\epsilon=-1\).
The difference of the two sides has exponent width at most \(8+|L|\) in each entry.
If the stated bound on good phases failed, each entry would vanish identically.
This argument would apply to every \(\zeta\in\mu_6\).

For each \(\zeta\), form the [polynomial closed chain](Yin_C_A0247_v1.md#four-polynomial-blocks-and-three-unit-pivots) on four two-coordinate inputs.
Use the four scalar sites \(w_i=\zeta z^{\epsilon^i}\) in \(Aw_i+B,Cw_i+D\) and the last boundary value \(\zeta^3 z^L\).
It is a Laurent polynomial matrix in \(z\).
At generic \(z\) the four denominators are invertible and the identity would give rank six by eliminating three two-coordinate blocks.
Every seven-rowed minor would vanish identically and in particular at \(z=1\).
There the sites all equal \(\zeta\), and the boundary is \(\zeta^3\).
The [six-character rank obstruction](Yin_C_A0247_v1.md#a-rank-of-at-least-seven-in-a-scalar-character) gives rank at least seven for at least one \(\zeta\), a contradiction.
Only Laurent polynomial minors were specialized at \(z=1\), including when the ordinary transfer has a pole there.

This proves the inequality for each common divisor.
If all recorded integers vanished, one could take \(d>16+2bk\), impossible since \(\gcd(k,d)\le k\).
Otherwise use their positive gcd itself to obtain the stated bound.
Taking its largest divisor coprime to \(k\) and using \(b\le2\) or \(4\) proves the last numerical restrictions.

## Assessment history

### Decision central-spectral-arcs-and-the-exponent-of-a-collision

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:44 |
| status | proved |
| reason | Whole-proof review verified the bounded spectral restriction, the finite coset computation, the specialization scope and the numerical divisor bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The determinant orbit condition and the divisibility bounds for true central collisions. |
| argument | [Compression to a central arc](#compression-to-a-central-arc) | Bounded invertible transfers on each good arc and the Haar integral. |
| argument | [Substitution on the finite product expansion](#substitution-on-the-finite-product-expansion) | Central denominators and consistency on precisely the recorded cosets. |
| argument | [Counting the good phases and returning to the closed chain](#counting-the-good-phases-and-returning-to-the-closed-chain) | Laurent widths, good roots and specialization of the polynomial minors. |
| review | [Central spectral arcs and the exponent of a collision](../audits/reviews/Yin_R_A0207_v1.md#central-spectral-arcs-and-the-exponent-of-a-collision) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-central-spectral-arcs-and-the-exponent-of-a-collision)
