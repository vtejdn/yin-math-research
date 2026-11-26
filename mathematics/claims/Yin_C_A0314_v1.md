---
author: Yin
---

# A cyclic quotient of order twenty excludes a four-site half kernel

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity and suppose \(H\) has a cyclic quotient of order twenty.
No complex two-square rectangle \(B+At-s(D+Ct)\) has regular nullity \(1/2\).
In fact every noninteger nullity is strictly below \(1/2\) by the [order-twenty upper bound](Yin_C_A0311_v1.md#statement).
This statement concerns the cyclic order-twenty quotient.

Assume there is equality.
The [marking and corner reduction](Yin_C_A0311_v1.md#statement) gives \(H_{\rm ab}=C_{20}\), with normalized degrees \((1,8)\) and \(A,D\) invertible.
We use also the degrees \((3,4)\) obtained by multiplying the same character by three.
Write \(t_j=s^jts^{-j},\ g=s^4,\ P(z)=Az+B,\ Q(z)=Cz+D,\ M=PQ^{-1},\ W=M(t_1)M(t_0)\).
By the [bounded-transfer exclusion](Yin_C_A0312_v1.md#statement), \(M\) and \(M^{-1}\) each have a pole on the unit circle.

## The original-group hypotheses for the pole estimates

Reduction modulo four supplies the [four-coset endpoint](Yin_C_A0310_v1.md#statement).
Thus both pencils are regular, their assembled constant matrix is invertible, consecutive cyclics have trivial intersection, \((s^{-1}M(t))^4=I\) and \(W^{-1}=s^{-2}W s^{-2}\).
The group \(H\) is nonamenable by scalar injectivity and [Ore localization](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups).
The subgroup \(F=\langle t_0,t_1,t_2,t_3\rangle\) contains \(s^4\) by the endpoint identity, and is normal of index four by the character.
We verify that each adjacent pair generates \(F\), which is therefore nonamenable.

Put \(A_0=\langle t_0,t_1\rangle,\ A_2=\langle t_2,t_3\rangle,\ J=A_0\cap A_2\).
The [ordered middle cut](Yin_C_A0186_v1.md#cutting-the-ordered-product) gives \(g=ba,\ b\in A_2,\ a\in A_0\), with \(Wa^{-1}\) affiliated and invertible over \(J\).
The [two-factor subgroup theorem](Yin_C_A0272_v1.md#statement) gives \(J=A_0\).
Here is the verification of its numerical rotation conditions, independent of the character order.
There is no constant point correspondence by the [two-dimensional transfer test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).
The three coefficients of \(N=P\,{\rm adj}\,Q\) are therefore independent by normalization at an invertible value, so \(N\) has no common nonconstant polynomial factor.
If \(M(\eta z)=M(z)D_0\) for a nontrivial root of unity of order \(k\), then \(D_0^k=I\) and it may be diagonalized.
The two primitive polynomial lists \(N(\eta z),N(z)D_0\) would be proportional by a constant, by clearing their reduced scalar ratio.
In the eigenbasis each column polynomial has powers in just one residue class modulo \(k\).
For \(k\ge3\) this gives a constant point correspondence; for \(k=2\) and distinct eigenvalues one column is odd, giving the same contradiction.
Equal eigenvalues leave at most two independent coefficients.
This excludes also scalar proportionality as required on the second leg.
Since \(A_0\subseteq A_2\) and \(g\in A_2\), conjugation by \(s^2\) gives \(A_2\subseteq gA_0g^{-1}\subseteq A_2\), whence \(A_0=A_2=F\).
Conjugation proves the assertion for every adjacent pair.

## The boundary poles are simple, unique, and at the same point

Apply the [arbitrary-size pole-rank theorem](Yin_C_A0304_v1.md#statement) with \(h=2\).
The two maximal pole orders are both one or both two: both transfers have a pole, their orders are at most two, and on one side only simple poles force the same on the other.
The rank bound and the ordered products of leading residues show that each side has a unique pole of maximal order and a square-zero, rank-one leading coefficient there.

We give the details relating the two sides, including why the previous common-double-root exclusion applies.
If the order is two, choose a constant row and column killing the leading matrix of \(M\) on the left and right.
The two factors in the resulting scalar compression of \(W\) have at most simple poles, giving tail \(O(v^{-2/3})\) by the [two-end cutoff estimate](Yin_C_A0290_v1.md#singular-value-bounds-for-two-cyclic-factors).
The corresponding compression of \(W^{-1}\) has the identical singular value distribution.
If the row or column failed to kill its leading matrix, the [compact arc estimate](Yin_C_A0292_v1.md#a-scalar-compression-still-detects-a-double-pole) would give a tail bounded below by \(cv^{-1/2}\): the opposite rational factor spans on a regular arc by absence of a constant point correspondence.
Hence the two leading matrices have the same image and kernel, and are proportional.
For order one the same proof uses bounded factors on the first side and a tail bounded below by \(cv^{-1}\) on the other; uniqueness of the circle pole on each side was just proved.
The estimates here require only the disjoint cyclics and the actual middle identity.

At the respective poles \(\alpha,\beta\), the two leading coefficients are proportional to \(N(\alpha)\) and \({\rm adj}\,N(\beta)\) since \(M=N/\det Q,\ M^{-1}={\rm adj}\,N/\det P\) and the polynomial matrix \(N\) does not vanish at any finite point.
As the matrices are proportional and have square zero, \(N(\alpha),N(\beta)\) are proportional.
Comparing the three independent coefficients of the polynomial \(N\) forces \(\alpha=\beta\).

In the double case the [common-root shear factorization](Yin_C_A0292_v1.md#the-two-rational-forms) uses only the common double root, a square-zero leading matrix, regularity and the exclusion of a constant point correspondence.
It gives \(M=(I+\lambda v e_{12})E(I+\mu v e_{12})\) in a constant basis, \(v=(z-\alpha)^{-1}\), \(\lambda\mu E_{21}\ne0\).
The [lower left entry computation](Yin_C_A0292_v1.md#a-group-element-reverses-a-power-in-the-common-root-case) uses just the middle equation and trivial cyclic intersection.
It gives a nonzero scalar \(X=c_0+c_1(\mu v(t_1)+\lambda v(t_0))\) and \(s^{-2}Xs^{-2}=\gamma X\) with \(|\gamma|=1\).
The proof of the [common double pole exclusion](Yin_C_A0294_v1.md#the-subgroup-detected-by-the-lower-left-entry) applies verbatim with the following group check.
The bounded polar part of \(X\) exhibits an element carrying a power of \(s\) to its inverse.
The subgroup of all elements carrying a power of \(s\) to itself or its inverse contains \(s\) positively and cannot contain \(t\), because in \(H_{\rm ab}=C_{20}\) its degree \(8\) is even.
This is the only abelianization input to that argument.
All its other inputs are the preceding scalar equation, \(|\alpha|=1\), and infinite order of \(s,t\): over the double of this subgroup the difference of the two resolvents is fixed by \(s^2\); clearing a common power or taking the bounded free resolvent gives a finite conjugation orbit of the original \(t\), contradicting its exclusion from that subgroup.
Thus the common double case is impossible.
The distinct double case has already been excluded by the proportionality of \(N(\alpha),N(\beta)\), without appealing to an order-24 exclusion.

## Five characters of the bounded lower left entry

Now put \({\rm det}Q=(z-\alpha)q(z),\ {\rm det}P=(z-\alpha)p(z)\), and \(m=p/q\).
Here \(p,q\) have no circle zeros, \(p\) has degree exactly one since \(A\) is invertible, and \(q(0)\ne0\) since \(D\) is invertible.
In a constant basis put the common nilpotent residue in the \(e_{12}\) direction and write
\[
                  M=\begin{pmatrix}f&b\\h&j\end{pmatrix}.
\]
Each of \(f,h,j\) has numerator of degree at most one over \(q\).
The equality \(fj-bh=m\) at the simple pole of \(b\) forces \(h(\alpha)=0\).
Also \(h\not\equiv0\) by the constant line exclusion, so \(h=\kappa(z-\alpha)/q\), \(\kappa\ne0\).
The polynomials \(q,qh\) are independent, and hence
\[
             f=A_0+A_1h,\qquad j=D_0+D_1h,\qquad m=m_0+m_1h,\qquad
             B_1=A_1+D_1 .
\]
Here \(m_0=m(\alpha)\ne0\), and \(A_0\ne0\) since otherwise \(M\) would carry its first input basis vector into a fixed line.
Put \(w=h/m=\kappa(z-\alpha)/p\).
All six functions \(f,h,j,f/m,w,j/m\) have absolutely summable Laurent coefficients.

Abbreviate \(h_i=h(t_i)\), \(w_i=w(t_i)\).
Direct multiplication of the forward and reverse products gives
\[
 \begin{aligned}
              W_{21}&=A_0 h_1+D_0 h_0+B_1h_1h_0,\\
          (W^{-1})_{21}&=-D_0w_0/m_0-A_0w_1/m_0-B_2 w_0w_1,\qquad
          B_2=B_1-(A_0+D_0)m_1/m_0 .
 \end{aligned}
\]
Thus the actual middle identity for this entry holds in \(\ell^1(F)\).
As in the [bounded-entry character calculation](Yin_C_A0303_v1.md#a-matrix-entry-with-absolutely-summable-coefficients), apply the five characters of \(F\) sending all \(t_i\) to \(\zeta\) and \(g\) to \(\zeta^3\), \(\zeta^5=1\).
They give
\[
              h(\zeta)\,{\rm tr}M(\zeta)\,(m(\zeta)^2+\zeta^3)=0 .
\]
Only regular entries or their regular trace sum are evaluated here.

## Opposite Fourier directions for a nonzero trace

If the trace is not identically zero, it has numerator degree at most one, so at least three of the five points satisfy \(m(\zeta)^2=-\zeta^3\).
A constant \(m\) matches at most one.
The nonconstant fractional linear function \(m\) takes modulus one at three circle points and therefore maps the unit circle onto itself, since a fractional linear map takes generalized circles to generalized circles and three distinct points determine one.

At most three of the five points can match.
Indeed a match is \(\zeta p(\zeta)=\pm i q(\zeta)\), using \(\zeta^5=1\).
If four or more points matched, the two quadratic polynomials \(zp\pm i q\) would each have two distinct fifth roots.
Their leading coefficients agree, and their nonzero constant coefficients are opposite.
The ratio of their root products would be \(-1\), which cannot be a fifth root of unity.
Thus there are exactly three matches and both exceptions must occur, one at \(h=0\) and another at a trace zero.
In particular the trace is nonconstant and \(B_1\ne0\).

If \(q\) were constant, \(m\) would be an affine map carrying the unit circle onto itself, hence a scalar times \(z\).
That function matches at most one of the five squared equations.
Otherwise \(q\) has a nonzero finite root \(\gamma\) off the circle.
The unique root of \(p\) is \(1/\overline\gamma\), by the reflection identity \(m(z)\overline{m(1/\bar z)}=1\).
Neither finite pole in \(h,w\) is canceled by their common boundary numerator.
Set \(\rho=\min(|\gamma|,|\gamma|^{-1})\in(0,1)\).
For one sign \(\epsilon\), the nonconstant Laurent coefficients of \(h\) occur at every index \(\epsilon n,\ n\ge1\), and their moduli are \(C_h\rho^n\) for a fixed \(C_h>0\).
For \(w\) the same description holds at \(-\epsilon n\) with a possibly different constant and the same \(\rho\), by the geometric expansions of the simple reciprocal poles.

For each \(n\ge2\), the \(n-1\) forward labels \(t_1^{\epsilon i}t_0^{\epsilon(n-i)}\), \(1\le i<n\), have coefficients of equal modulus \(|B_1| C_h^2\rho^n\).
They are distinct and cannot be affected by terms on the two axes, by the trivial adjacent intersection.
Multiplication by \(s^{-2}\) on both sides translates these to \(n-1\) distinct labels of the inverse entry, with the same coefficient moduli.
On either axis the inverse coefficients are one fixed multiple of the \(w\)-tail, incorporating also its constant term in the product \(w_0w_1\).
Thus at most one point on each axis can have that prescribed nonzero modulus, and there is at most one identity point.
For every sufficiently large \(n\) an interior inverse label must occur.
This rules out \(B_2=0\).
Its two exponents have total unsigned length \(n'\) with
\[
                |B_2|C_w^2\rho^{n'}=|B_1|C_h^2\rho^n .
\]
Strict monotonicity gives one fixed integer \(n'-n\) for all those \(n\).
The marked degree of the translated forward label equals \(4\epsilon n-12\), whereas the inverse label has degree \(-4\epsilon n'\) in \(C_{20}\).
Thus \(\epsilon(n+n')\equiv3\bmod5\) for every sufficiently large \(n\).
With \(n'-n\) fixed, consecutive \(n\)'s contradict this congruence.

## The zero-trace and affine cases

If the trace vanishes identically, \(D_0=-A_0,\ B_1=B_2=0\).
Since \(A_0\ne0\), the lower left identity becomes
\[
           s^{-2}(h(t_1)-h(t_0))s^{-2}
                          =-m_0^{-1}(w(t_1)-w(t_0)).
\]
The Fourier coefficients on distinct nonzero powers of consecutive cyclics do not cancel.
If \(h\) has infinite Fourier support, all positive or all negative powers of \(t_{-1}\) lie in \(C_0s^4\cup C_1s^4\), by translating the coefficients initially at \(t_1^n\).
At most one belongs to \(C_0s^4\) since \(C_{-1}\cap C_0=1\).
Two consecutive powers in \(C_1s^4\) force \(t_{-1}\in C_1\), hence \(s^4\in C_1\cap C_0\) by conjugation.
This is impossible.

If \(h\) has finite Fourier support, it is affine in \(z\) because \(q(0)\ne0\) and its numerator cannot cancel a root of \(q\).
The difference on the left then has exactly two labels of degree \(4-12=12\bmod20\).
The difference for \(w\) on the right must have finite support as well.
Because \(p\) has degree one and its root cannot cancel the numerator, this requires that root to be zero; \(w\) is affine in \(z^{-1}\).
The two labels on the right have degree \(-4=16\bmod20\), again impossible.
This ends the exclusion.

## Assessment history

### Decision excluding-a-cyclic-quotient-of-order-twenty

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:23 |
| status | proved |
| reason | The bounded case and all allowable configurations with poles lead to contradictions in the original regular representation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The bounded case and all allowable configurations with poles lead to contradictions in the original regular representation. |
| argument | [The original-group hypotheses for the pole estimates](#the-original-group-hypotheses-for-the-pole-estimates) | The original-group hypotheses for the pole estimates. |
| argument | [The boundary poles are simple, unique, and at the same point](#the-boundary-poles-are-simple-unique-and-at-the-same-point) | The boundary poles are simple, unique, and at the same point. |
| argument | [Five characters of the bounded lower left entry](#five-characters-of-the-bounded-lower-left-entry) | Five characters of the bounded lower left entry. |
| argument | [Opposite Fourier directions for a nonzero trace](#opposite-fourier-directions-for-a-nonzero-trace) | Opposite Fourier directions for a nonzero trace. |
| argument | [The zero-trace and affine cases](#the-zero-trace-and-affine-cases) | The zero-trace and affine cases. |
| review | [Excluding a cyclic quotient of order twenty](../audits/reviews/Yin_R_A0220_v1.md#excluding-a-cyclic-quotient-of-order-twenty) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-excluding-a-cyclic-quotient-of-order-twenty)
