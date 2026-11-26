---
author: Yin
---

# The two determinant pencils share a single nonzero root at every four-coset half kernel

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity.
Write \(t_j=s^jts^{-j}\), \(F=\langle t_0,t_1,t_2,t_3\rangle\), and assume \(\langle t_0,t_1,t_2\rangle s^i,\ 0\le i<4\), are distinct.
If \(P(t)-sQ(t)\) for linear complex two-square pencils has regular nullity \(1/2\), then
\[
       \det P(z)=c_1 z^a(z-\alpha),\qquad
       \det Q(z)=c_2 z^b(z-\alpha),
       \qquad c_1 c_2\alpha\ne0,\quad a,b\in\{0,1\}.
\]
At \(\alpha\) the transfers \(M=PQ^{-1}\) and \(M^{-1}\) have proportional square-zero residues of rank one.
In coordinates where that common direction is \(e_{12}\), put \(h=M_{21}\) and \(w=h/\det M\).
Each of \(h,w\) is a nonconstant affine function of \(z\) or of \(z^{-1}\).
The lower left entries of \(W=M(t_1)M(t_0)\) and \(W^{-1}\) are therefore group-ring scalars supported on at most four group elements each.
The point \(\alpha\) may lie on the unit circle, and the conclusion holds for every marking satisfying the four-coset hypothesis.

## The common double-root case without a sign restriction

The [four-coset construction](Yin_C_A0320_v1.md#checking-the-hypotheses-for-the-fourier-level-sets) gives regular pencils and invertible assembly, trivial intersection of consecutive cyclic subgroups, nonamenability of each adjacent pair, no constant point correspondence for \(M\), and \((s^{-1}M(t))^4=I\).
In particular \(W^{-1}=s^{-2}W s^{-2}\) and \(W=M(t_2)^{-1}M(t_3)^{-1}s^4\).
If both transfers are circle-bounded, the [coefficient level-set theorem](Yin_C_A0318_v1.md#statement) already gives their determinant and residue conclusions.
If just one is circle-bounded, its bounded product and the [one-factor tail lower bound](Yin_C_A0290_v1.md#singular-value-bounds-for-two-cyclic-factors) for the opposite side contradict their equal singular value distributions.
Suppose both have a boundary pole.

The [quartic pole-rank theorem](Yin_C_A0304_v1.md#statement) and the [compressed residue comparison](Yin_C_A0314_v1.md#the-boundary-poles-are-simple-unique-and-at-the-same-point) up to and including identification of the point use precisely these original-group conditions.
For detail, the two maximal orders coincide since one side having only simple poles forces the same on the other, and a quadratic denominator gives order at most two.
Each side has one pole of maximal order with a square-zero rank-one leading coefficient.
Killing its leading matrix on the left and right gives, for a double pole, a two-simple-factor tail \(O(v^{-2/3})\) versus a lower bound \(cv^{-1/2}\) on the inverse compression unless its leading matrix is also killed on both ends.
For a simple pole compare boundedness to the lower bound \(cv^{-1}\).
The inverse compressed arc spans by the absence of a constant point correspondence.
Thus the two leading matrices are proportional.
The three coefficients of \(N=P\,{\rm adj}\,Q\) are linearly independent by the [point correspondence calculation](Yin_C_A0303_v1.md#the-two-residues-occur-at-the-same-point).
The leading matrices are proportional to \(N(\alpha)\) and \({\rm adj}\,N(\beta)\); since they square to zero, coefficient independence forces \(\alpha=\beta\).

If the common pole were double, use the [unipotent factorization and the lower left entry](Yin_C_A0292_v1.md#a-group-element-reverses-a-power-in-the-common-root-case).
That local calculation uses the common square-zero leading direction, quartic identity, absence of constant point correspondence and disjoint neighboring cyclics.
For \(u(z)=(z-\alpha)^{-1}\) it gives a nonzero scalar
\[
              X=d+b\,u(t_1)+c\,u(t_0),\qquad bc\ne0,\qquad
              s^{-2}Xs^{-2}=\gamma X,\quad |\gamma|=1 .
\]
Let \(K\) consist of elements taking some positive power of \(s\) to itself or its inverse, with its [multiplicative sign](Yin_C_A0294_v1.md#the-subgroup-detected-by-the-lower-left-entry).
The bounded polar part of \(X\) has Fourier support on finite \(h\mapsto s^{-2}hs^{-2}\) orbits, hence in the negative coset of \(K\).
Every spectral projection of \(|X|\) is supported on the positive subgroup since it commutes with \(s^2\).
In particular \(X\in U(K)\), and its sign twist in \(U(K)\) sends \(X\) to \(-X\).

If \(t\in K\), then \(K=H\).
The sign must be negative on \(t\), since it is positive on \(s\) and a negative element exists in the support of the nonzero polar part.
It is also negative on \(t_1\).
Taking the even part of the displayed expression for \(X\) gives
\[
          0=d+b\alpha(t_1^2-\alpha^2)^{-1}
                 +c\alpha(t_0^2-\alpha^2)^{-1}.
\]
The two-variable rational tensor on the right is nonzero since \(b,c,\alpha\ne0\).
It remains nonzero in the group by clearing the first denominator on the left and the second on the right, since the labels \(t_1^{2i}t_0^{2j}\) are distinct.
Thus \(t\notin K\).
With this fact the [amalgamated double argument](Yin_C_A0294_v1.md#comparing-two-copies-over-the-subgroup) and its [free resolvent case](Yin_C_A0294_v1.md#a-bounded-resolvent-when-the-two-cyclic-copies-are-free) apply with no abelianization assumption.
The difference of the two cyclic resolvents in the double is fixed by conjugation by \(s^2\), and either a common power or the bounded free resolvent produces a finite \(s^2\)-conjugation orbit of the first copy of \(t\).
That would give \(t\in K\).
This rules out a double boundary pole in every marking.

## A simple boundary pole leaves only finite Fourier supports in the compression

For the common simple pole \(\alpha\), write \(\det Q=(z-\alpha)q,\ \det P=(z-\alpha)p\).
The polynomials \(p,q\) of degree at most one have no circle zeros.
In the common residue basis the [lower left entry calculation](Yin_C_A0316_v1.md#the-two-geometric-sequences-of-coefficients) gives
\[
 h(z)=\kappa(z-\alpha)/q(z),\qquad w(z)=\kappa(z-\alpha)/p(z),
                  \qquad \kappa\ne0 .
\]
Indeed the three regular entries of \(M\) have linear numerators over \(q\), and \(M_{21}(\alpha)=0\) since \(\det M\) is regular but \(M_{12}\) has a simple pole.
Its lower left entry is not identically zero by the point correspondence test.
The same three regular entries of \(M^{-1}\) have linear numerators over \(p\).
The lower left entries of \(W,W^{-1}\), respectively, have the form
\[
 \begin{aligned}
 L &=a h(t_1)+d h(t_0)+b h(t_1)h(t_0),\\
 L'&=a' w(t_0)+d' w(t_1)+b' w(t_0)w(t_1),
 \end{aligned}
\]
where \(a,d,a',d'\) are nonzero.
For example if the intercept in \(M_{11}=a+b_0h\) vanished, its first column would belong to a constant line.
If the intercept in \(M_{22}=d+b_1h\) vanished, its second row would belong to a constant covector line, whose kernel gives a constant point correspondence.
Apply these observations also to the inverse.
Both scalar entries \(L,L'\) have absolutely summable Fourier coefficients and satisfy \(L'=s^{-2}Ls^{-2}\).

Suppose \(h\) has an infinite Fourier tail.
Its nonconstant coefficients then occupy one open half-line with a fixed nonzero geometric ratio of modulus less than one.
If \(b\ne0\), the threshold \(e^{-R}\) for the absolute coefficient of \(L\) gives at least a constant times \(R^2\) labels for large \(R\), from the two-index products on that half-line.
Use \(L=s^2 L' s^2\) as the second presentation.
Its left labels lie along powers of \(t_2\), followed by powers of \(t_3\) and \(s^4\), while those of \(L\) lie along \(t_1,t_0\).
On each side for fixed second index the accepted first indices form a bounded number of intervals and singletons, since \(h\) and \(w\) each have a single geometric tail or only finitely many coefficients.
This remains true on the coordinate axes after including their constant terms.
There are \(O(R)\) possible second indices by exponential decay.
By the [level-set argument on a nonamenable pair](Yin_C_A0318_v1.md#two-independent-translations-of-the-same-finite-set), these sets would be almost invariant under \(t_1,t_2\), a contradiction.
The identical conclusion applies if \(w\) has an infinite tail and \(b'\ne0\), using the same two presentations.
Thus an infinite side has no product term.

Such a side has infinite support on both axes because its two linear coefficients are nonzero and the cyclic groups intersect trivially.
The other side cannot have finite support and therefore also has zero product coefficient.
If the forward tail has sign \(\epsilon\), comparing the support on \(t_1^{\epsilon n}\), \(n\ge1\), with \(L'=s^{-2}L s^{-2}\) gives
\[
              t_{-1}^{\epsilon n}\in C_0s^4\ \cup\ C_1s^4,\qquad
                      C_j=\langle t_j\rangle .
\]
At most one power belongs to the first coset by \(C_{-1}\cap C_0=1\).
Two consecutive powers in the second give \(t_{-1}\in C_1\) and then \(s^4\in C_1\).
Conjugation by \(s^{-1}\) puts \(s^4\) in \(C_0\) as well, contradicting the infinite order of \(s\).

Hence both \(h,w\) have finite Laurent support.
Since \(\alpha\ne0\) and \(p(\alpha),q(\alpha)\ne0\), the linear denominator of each must be constant or a scalar multiple of \(z\).
Each function is a nonconstant affine function of \(z\) or \(z^{-1}\), as claimed.
In the circle-bounded case the same final description follows from the determinant and residue conclusions of the level-set theorem: \(M_{21}\) has a linear numerator over the remaining monomial denominator and its zero at \(\alpha\) follows as above from finite \(\det M(\alpha)\ne0\).
Substitution in \(L,L'\) gives the asserted four-label supports in both cases.

## Assessment history

### Decision finite-support-at-a-general-four-coset-marking

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:50 |
| status | proved |
| reason | Excluding the double boundary pole and both infinite-axis alternatives reduces the scalar identity to two finite supports. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Excluding the double boundary pole and both infinite-axis alternatives reduces the scalar identity to two finite supports. |
| argument | [The common double-root case without a sign restriction](#the-common-double-root-case-without-a-sign-restriction) | The common double-root case without a sign restriction. |
| argument | [A simple boundary pole leaves only finite Fourier supports in the compression](#a-simple-boundary-pole-leaves-only-finite-fourier-supports-in-the-compression) | A simple boundary pole leaves only finite Fourier supports in the compression. |
| review | [Finite support at a general four-coset marking](../audits/reviews/Yin_R_A0223_v1.md#finite-support-at-a-general-four-coset-marking) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-finite-support-at-a-general-four-coset-marking)
