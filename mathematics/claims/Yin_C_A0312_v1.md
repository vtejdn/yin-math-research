---
author: Yin
---

# Five numerical fibers and two cyclic axes exclude a bounded transfer at cyclic order twenty

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity and a character of order twenty of degrees \((1,8)\).
If the complex two-square rectangle \(P(t)-sQ(t)\), \(P(z)=Az+B,\ Q(z)=Cz+D\), has regular nullity \(1/2\), then \(M=PQ^{-1}\) and \(M^{-1}\) both have actual poles on the unit circle.

Use the equivalent degrees \((3,4)\) for the same ordered generators by multiplying the character by three.
The [order-twenty corner restrictions](Yin_C_A0311_v1.md#statement) give invertible \(A,D\).
The [four-coset theorem](Yin_C_A0310_v1.md#statement) applies via reduction modulo four; it gives trivial intersection of consecutive \(C_j=\langle t_j\rangle\), where \(t_j=s^jts^{-j}\), and rules out a Laurent monomial for either \(p=\det P\) or \(q=\det Q\).
Write \(g=s^4,\ W=M(t_1)M(t_0)\).
The quartic endpoint gives \(W^{-1}=s^{-2}Ws^{-2}\), hence the same singular value distribution.
If one transfer were bounded and the other had a circle pole, its bounded two-factor product would contradict the [one-factor lower tail](Yin_C_A0290_v1.md#singular-value-bounds-for-two-cyclic-factors) for its counterpart.
Assume then that both transfers are bounded.

## The five numerical fibers

The entries of \(M\) are rational without boundary poles and therefore have absolutely summable Laurent coefficients.
The ordered product \(M(t_3)M(t_2)M(t_1)M(t_0)=s^4 I\) holds in the ordinary group convolution algebra.
The order-five characters of the index-four phase subgroup send every \(t_j\) to \(\zeta\) and \(s^4\) to \(\zeta^3\) for \(\zeta^5=1\).
Thus \(M(\zeta)^4=\zeta^3 I\) at all five points.

We claim that these five identities force \({\rm tr}\,M(z)=0\) identically.
Put \(D_*(w)=\det(B+w^4 A-w^3 D-w^7 C)\); its exponents lie in \(\{0,3,4,6,7,8,10,11,14\}\).
It is nonzero, since identically vanishing would give four distinct eigenvalues \(w^3\) for a fixed generic \(M(w^4)\) by changing \(w\) to the four fourth roots of that same fourth power.
For each of the five fibers \(w^4=\zeta,\ w^{20}=1\), select two of the four \(w\)'s with multiplicities corresponding to the eigenvalues \(w^3\) of \(M(\zeta)\).
The degree-ten product \(L(w)\) of their linear factors divides \(D_*\).
Indeed \(B+w^4 A-w^3 D-w^7 C=(M(w^4)-w^3 I)Q(w^4)\) even at a removable singularity of \(M\).
If the eigenvalues coincide, the separable equation \(M(\zeta)^4=\zeta^3I\) makes the matrix scalar and all four entries on the left vanish, giving at least a double determinant root.

For \(D_*/L\) of degree at most four, vanishing of each forbidden coefficient imposes a homogeneous equation on its five coefficients.
The matrix for indices \(i=1,2,5,9,12,13\) has entries \(L_{i-j}\), \(0\le j\le4\), extended by zero outside \(0,\ldots,10\).
All its five-square minors must vanish in \(\mathbb Z[\zeta_{20}]\), since a nonzero complex solution exists.
Reduce modulo \(101\) with \(\zeta_{20}\mapsto32\).
The [five-fiber verifier](../computations/programs/Yin_J_A0010/verify_five_fibers.mjs) exhausts the ten choices in each fiber, counting matrices of rank below five by the number of fibers with opposite selected \(w\)'s.
In order from zero to five opposite pairs the counts are \(0,0,0,0,60,32\) out of \(100000\) choices.
The test uses only necessary rank deficiency under reduction.
All characteristic-zero candidates thus have at least four fibers with opposite eigenvalues.
The trace numerator has degree at most two, so those four zeros make the trace identically zero.
At the five points the characteristic identity of a traceless two-square matrix now gives
\[
                        m(\zeta)^2=\zeta^3,\qquad m=p/q .
\]

## A grid supported on two translates of cyclic groups

Let \(\alpha\ne0\) be any finite root of \(q\), and set \(N=P\,{\rm adj}\,Q\).
Its three coefficient matrices are independent, since a generically invertible pencil in a constant span of dimension at most two has a constant point correspondence by normalizing at an invertible value and taking an eigenline.
This is ruled out by the [constant point criterion](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).
Hence \(N(\alpha)\ne0\).
It is traceless and singular since \(\det N=pq\); make it a nonzero multiple of \(e_{12}\) by constant similarity.
The entries \(N_{11},N_{21}\) are divisible by \(z-\alpha\) with quotient polynomials of degree at most one.
The two quotients are independent, for otherwise the first column of \(M\) lies in a constant line.

Writing the product's lower left entry with independent left and right variables \(z,w\), its numerator is consequently a nonzero constant multiple of \((z-w)(z-\alpha)(w-\alpha)\).
This follows by antisymmetrizing the two independent quotient polynomials, using \(N_{22}=-N_{11}\).
On the \(W\) side the denominator is \(q(z)q(w)\).
With \(q_0=q/(z-\alpha)\) of degree at most one, the scalar kernel is a nonzero multiple of \((z-w)/(q_0(z)q_0(w))\), the difference of a single rational function in \(z,w\) up to a constant factor.
For nonconstant \(q_0\) use \(1/q_0\); for constant \(q_0\) use \(z\).
Here \(q_0\) has no boundary zero: a zero of \(q\) on the circle would have given \(N(\alpha')=0\) there by boundedness, contradicting coefficient independence.
Thus \(W_{21}\) has group Fourier support in \(C_1\cup C_0\).

On the \(W^{-1}\) side the variables are \(t_0,t_1\) in that order.
The inverse is \(-N/p\), so the scalar kernel there is a nonzero multiple of the antisymmetrized product of \(G(z)=(z-\alpha)/p(z)\) and \(zG(z)\).
The polynomial \(p\) likewise has no circle zero by boundedness of \(M^{-1}\).
Let \(v_i\in\mathbb C^2\) be the pair of Laurent coefficients of \(G,zG\) at \(i\).
The coefficient on \(t_0^i t_1^j\) is nonzero exactly when \(v_i,v_j\) are independent, by the determinant formula and the trivial consecutive intersection.
Every such label satisfies
\[
                          t_0^i t_1^j g\in C_{-2}\cup C_{-1}
\]
by the translate of \(W_{21}\).
For fixed \(j\), at most one \(i\) can give membership in \(C_{-1}\) since a quotient of two would be in \(C_0\cap C_{-1}\).
For fixed \(i\), at most one \(j\) can give membership in \(C_{-2}\), since the right quotient in the order first inverse times second would be in \(g^{-1}C_1 g\cap C_{-2}=C_{-3}\cap C_{-2}\).
Consequently sets of indices \(I,J\) for which every cross pair of vectors is independent satisfy \(|I||J|\le |I|+|J|\) whenever both sets are finite.

If infinitely many \(v_i\) are nonzero, some one line contains all but at most one of them.
Indeed infinitely many distinct lines would allow two sets of three on disjoint lines.
With finitely many lines, one line occurs infinitely often, and two vectors outside it would form a forbidden rectangle with three vectors on it.
A linear functional killing this line gives \((a+bz)G(z)=c z^k\) for some \(c\ne0\): at most one Fourier coefficient remains, and \(G,zG\) are independent as functions.
Since \(\alpha\ne0\), the polynomial identity \((a+bz)(z-\alpha)=cz^k p(z)\) implies \(p(\alpha)=0\).
If there are just finitely many nonzero \(v_i\), then \(G\) is Laurent polynomial.
Since \(p\) has at least one nonzero finite root by nonmonomiality, all such roots must equal \(\alpha\).
In either case every nonzero finite root of \(q\) is a root of \(p\).

The reverse inclusion follows by the same proof applied to \((s^{-1},t_1,M^{-1})\) in place of \((s,t,M)\).
Its quartic transfer \(sM(t_1)^{-1}\) is the conjugate by \(s^2\) of \((s^{-1}M(t))^{-1}\).
The cyclic-intersection assumption and the traceless identity persist, and this grid argument uses neither the marking nor the invertibility of any numerical corner.

## The determinant restriction

If \(p,q\) have two distinct nonzero finite roots, they are proportional quadratics, contradicting \(m(\zeta)^2=\zeta^3\).
Otherwise their common nonempty set of such roots consists of a single point \(\alpha\) off the circle.
Since \(A,D\) are invertible, \(p\) has degree two and \(q(0)\ne0\), so
\[
                  m(z)=c z^{2-r}(z-\alpha)^{r-k},
                       \qquad r,k\in\{1,2\},\ c\ne0 .
\]
All five boundary values have modulus one.
The five points cannot all be equidistant from the fixed nonzero \(\alpha\), so \(r=k\).
Then \(2(2-r)\) would equal \(3\bmod5\), which holds for neither value of \(r\).
This excludes the bounded transfer.

## Assessment history

### Decision five-fibers-and-a-bounded-transfer

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:23 |
| status | proved |
| reason | The five numerical fiber constraints and the two-axis support identity exclude circle-bounded transfers. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The five numerical fiber constraints and the two-axis support identity exclude circle-bounded transfers. |
| argument | [The five numerical fibers](#the-five-numerical-fibers) | The five numerical fibers. |
| argument | [A grid supported on two translates of cyclic groups](#a-grid-supported-on-two-translates-of-cyclic-groups) | A grid supported on two translates of cyclic groups. |
| argument | [The determinant restriction](#the-determinant-restriction) | The determinant restriction. |
| review | [Five fibers and a bounded transfer](../audits/reviews/Yin_R_A0220_v1.md#five-fibers-and-a-bounded-transfer) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-five-fibers-and-a-bounded-transfer)
