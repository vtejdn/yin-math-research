---
author: Yin
---
# Positive spectral mass near zero for matrices on the four-line groups

## Statement

Fix a torsion-free, non-elementary word-hyperbolic group \(G\) with the rose word metric from a pattern-free four-line tuple.
The single-group spectral estimates apply to every finitely generated group having integer unnormalized traces of matrix projections over \(C_r^*(G)\) and the radius-\(r\) ball norm bound \(K_G(1+r)^{3/2}\|\cdot\|_2\).
For the four-line groups these inputs hold on the conditional probability-\(1-o(1)\) event already identified in [L54](../ledger/Yin_L_A0054_v1.md#from-hyperbolicity-to-integral-traces) and [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace).
Constants below may depend on the realized group and matrix.

Let \(B\in M_m(\mathbb CG)\) be a positive contraction in the regular representation, with entries supported in a word ball of integer radius \(w\ge1\).
Write \(\mu\) for its unnormalized trace spectral measure and \(F(t)=\mu((0,t])\) for its positive spectral mass below \(t\).
The measure has total mass \(m\).
The spectrum is a union of at most \(m\) closed intervals, allowing one-point intervals.
If zero is a limit of positive spectral values, then some \([0,\delta]\) lies in the spectrum and
\[
 F(t)\ \ge\ c_B\frac{t^{3/2}}{(1+\log(1/t))^3}
 \quad(0<t<t_B),\qquad
 \limsup_{t\downarrow0}\frac{F(t)}{t^{3/2}}>0.                         \tag{1}
\]
In particular \(F(t)=o(t^{3/2})\) implies a gap above zero.
For any nonzero rectangular matrix \(A\), one can use \(B=A^*A/M\) for any known \(M\ge\|A\|^2\).
The gap criterion gives closed range and integral kernel dimension for that \(A\).

The proof gives a bound on a finite moment expression at every sufficiently large polynomial degree scale.
For \(n\ge2\) and \(t=\sin^2(\theta/2)\), \(0\le\theta\le\pi\), put
\[
 f_n(t)=\left(\frac{\sin(n\theta/2)}{n\sin(\theta/2)}\right)^2,
 \qquad f_n(0)=1,\qquad P_{n,k}=f_n^k(1-f_n^k)\quad(k\ge1).
\]
When zero is a limit of positive spectrum, for all sufficiently large \(n\) and every integer \(k\ge1\),
\[
 \int_{(0,1]} P_{n,k}(t)^2\,d\mu(t)
 \ \ge\ \frac{1}{16K_G^2[1+2k(n-1)w]^3}.                              \tag{2}
\]
The expression is independent of the mass of the atom at zero.
It extends the scalar Fejér calculation of [C14 v2](Yin_C_A0014_v2.md#statement) to matrix inputs on the four-line groups, whose ball volumes grow exponentially.
The norm estimate here depends polynomially on the radius through rapid decay.

For a fixed rectangular word matrix over the free rose group with free nullity \(d\), there is an \(s>0\) independent of the sufficiently large good tuple such that every quotient realization with nonclosed range has \([0,s]\) in its normalized Gram spectrum.
If any \(\lambda\in(0,s]\) is outside that spectrum, there is no spectrum in \((0,\lambda)\), and the quotient nullity equals \(d\).
One finite free-group moment gives \(s\), and a polynomial operator norm bound at one scale can certify the missing point.

## Argument

All spectral projections arising from a partition of \(\sigma(B)\) into finitely many nonempty relatively closed and open sets are continuous functions of \(B\).
They belong to \(M_m(C_r^*(G))\), and each has trace at least one by faithfulness and integrality.
Their sum has trace \(m\), so such a partition has at most \(m\) pieces.
If a compact subset of the line had more than \(m\) components, choose one point in each of \(m+1\) distinct components in increasing order.
A point of the complement between each consecutive pair would give a partition with \(m+1\) pieces.
Thus the components of \(\sigma(B)\) are finitely many closed intervals.
When positive spectral values tend to zero, the one containing zero has positive length.

The Fejér identity expresses \(f_n\) as the squared modulus of \(n^{-1}\sum_{j=0}^{n-1} e^{ij\theta}\).
Expanding and using \(\cos\theta=1-2t\) shows that it is a real polynomial of degree at most \(n-1\), with
\[
             0\le f_n(t)\le\min\{1,(n^2t)^{-1}\}\quad(t>0).
\]
Its first zero occurs at \(t_n=\sin^2(\pi/n)\).
Once \(t_n\le\delta\), the continuous function \(f_n^k\) takes every value from zero to one on a subset of the spectrum.
Consequently \(\|P_{n,k}(B)\|=1/4\).
The entries of this matrix are supported in the ball of radius \(2k(n-1)w\).
For any matrix \(X\) supported in a ball of radius \(r\), amplify the scalar rapid-decay estimate using \(\|X\|\le(\sum_{ij}\|X_{ij}\|^2)^{1/2}\).
This gives \(\|X\|\le K_G(1+r)^{3/2}[(\operatorname{Tr}_m\otimes\tau)(X^*X)]^{1/2}\).
Applying it to \(P_{n,k}(B)\) yields (2), since \(P_{n,k}(0)=0\).
The scalar ball inequality is recorded in [Nica, introduction, inequality for balls](../literature/pdf/Nic17--arxiv.pdf#page=1).

For the first assertion of (1) take \(n=\lceil2/\sqrt t\rceil\), \(k=\lceil2\log(1/t)\rceil\), for small enough \(t>0\).
On \((t,1]\) one has \(f_n\le1/4\), and everywhere \(P_{n,k}\le1/4\).
The integral in (2) is at most \(F(t)/16+m16^{-k}\).
Its lower bound there is at least a fixed positive multiple of \(t^{3/2}/(1+\log(1/t))^3\).
Since \(16^{-k}\le t^{2\log16}\), the term involving \(m\) is smaller than half that multiple for all sufficiently small \(t\).

For the critical limsup, suppose \(F(t)=o(t^{3/2})\) and set \(k=1\).
Using \(P_{n,1}^2\le\min\{1,n^{-4}t^{-2}\}\) and integrating the decreasing majorant against the positive spectral measure gives
\[
 \int_{(0,1]}P_{n,1}^2\,d\mu
 \ \le\ n^{-4}F(1)+2n^{-4}\int_{n^{-2}}^1 F(t)t^{-3}\,dt .
\]
For any \(\eta>0\) use \(F(t)\le\eta t^{3/2}\) on a sufficiently small interval.
The contribution there is bounded by \(4\eta n^{-3}\), and the contribution from the interval bounded away from zero is \(O_\eta(n^{-4})\).
This would give \(o(n^{-3})\), contradicting (2).
For \(A\), a gap of \(A^*A\) above zero gives closed range, and continuous functional calculus and the trace input give the stated integrality.

In (2) the polynomial under the integral has degree at most \(4k(n-1)\).
For \(B=A^*A/M\) the trace uses the equality classes of alternating group words from its factors, up to \(4k(n-1)\) copies of \(A^*A\), with their matrix and complex coefficients.
The true product fibers of the two characteristic-two factors give their pairwise product coefficients.
They do not supply these higher alternating equalities for an arbitrary \(A\).
On a supplied good tuple with word-problem data and exact coefficients, any specified finite set of these moments can be computed by the [group equality decision](Yin_C_A0052_v1.md#bounded-certificates-in-the-cone-presentation).
Inequality (2) concerns the positive spectrum regardless of whether the zero atom has integral trace.

## A common spectral interval for a fixed word matrix

Let \(A\) have \(m\) columns and free regular nullity \(d\).
Use the same known norm bound \(M>0\) for the squared norm on the free group and all its quotients, for instance the square of one plus the sum of the absolute values of all coefficients.
Write \(B_F=A^*A/M\) and \(B_n\) for its image.
The factorization over the free group ring in [L54](../ledger/Yin_L_A0054_v1.md#the-rank-seen-by-a-fixed-matrix) gives \(\mu_n(\{0\})\ge d\), where \(d\) is an integer.
By dominated convergence \((\operatorname{Tr}_m\otimes\tau_F)((1-B_F)^N)\downarrow d\).
Choose one integer \(N\) for which this moment is strictly below \(d+1\).
There is then an \(s\in(0,1)\) with the same moment strictly less than \((d+1)(1-s)^N\).
The marked systole estimate in L54 makes this one polynomial moment identical in every sufficiently large good realization.
Consequently
\[
 d\le\mu_n(\{0\})\le\mu_n([0,s])
 \le (1-s)^{-N}(\operatorname{Tr}_m\otimes\tau_n)((1-B_n)^N)<d+1 .
\]
If \(\lambda\in(0,s]\) is outside the spectrum, \(1_{[0,\lambda)}(B_n)\) belongs to the reduced matrix algebra and has integer trace between \(d\) and \(d+1\), strictly below the latter.
The zero atom already accounts for at least \(d\), so this projection equals the kernel projection by faithfulness.
Every relatively open nonempty subset of the spectrum has positive trace measure, again by faithfulness, so the entire open interval \((0,\lambda)\) is disjoint from the spectrum.
In particular nonclosed range forces the whole interval \([0,s]\), and the cutoff scale in (2) can be chosen uniformly for this fixed matrix.
The same conclusion holds whenever the quotient nullity exceeds \(d\), since a missing point would give equality.

For a finite sufficient test, choose \(n'\ge2\) with \(t_{n'}\le s\).
The polynomial \(P_{n',1}\) takes value \(1/4\) at some explicitly selectable \(\lambda\in(0,t_{n'})\), since \(f_{n'}\) goes from one to zero there.
A verified bound \(\|P_{n',1}(B_n)\|<1/4\) excludes that \(\lambda\), hence certifies exact nullity \(d\) and a gap.
One may use the finite coefficient \(\ell^1\) norm summed over entries as an upper bound, or the finite moment and ball estimate with a supplied valid \(K_{G_n}\).
The group-specific rapid-decay constants in (2) need not be uniform over this family.

## The exponent for positive matrices and the spatial condition

The strictness of the little-oh condition for positive \(B\) can already be seen on the rank-two free group.
The tree density used here is Kesten's spectral law for the simple random walk on a free group, with the transition operator multiplied by four. [Theorem 3, proof on p. 349](../literature/pdf/Kes59.pdf#page=14)
Let \(H\) be adjacency on its degree-four tree and let \(B=(2\sqrt3-H)/(4\sqrt3)\).
Cutting one edge leaves three identical forward branches, whose Schur complement gives the root resolvent \(u(z)=(z-3u(z))^{-1}\) in a forward branch.
At the root of the original tree the four branches give diagonal resolvent \(G(z)=(z-4u(z))^{-1}\).
The solution decaying at infinity is \(u(z)=(z-\sqrt{z^2-12})/6\), with the square root asymptotic to \(z\).
The diagonal spectral density of \(H\) on \((-2\sqrt3,2\sqrt3)\) is consequently
\[
                       \frac{2\sqrt{12-x^2}}{\pi(16-x^2)} .
\]
The resolvent has no poles outside that interval, including the removable candidates at \(\pm4\), and it stays bounded at the two endpoints.
By Stieltjes inversion this accounts for its spectral measure.
Thus \(B\) is a positive contraction with \(F(t)\asymp t^{3/2}\) at zero.
This calibration concerns finite-propagation positive operators in the reduced algebra.
Indeed this \(B\) cannot equal \(A^*A\) for a matrix over the free group ring with one column, since its augmentation is negative whereas the augmentation of \(A^*A\) is nonnegative.

On every good four-line group one can also realize arbitrarily slow positive power laws for Gram matrices with a nonconstant, rapidly decaying kernel projection.
Choose an element \(g\) of infinite order, set \(x=1-g\), and use the row \(A_d=x^d(1,x)\) for any integer \(d\ge1\).
Restriction to \(\langle g\rangle\) preserves its trace spectral measure by the right-coset decomposition.
In the circle representation with \(x=1-e^{i\theta}\), the two eigenvalues of the normalized Gram matrix are zero and \(|x|^{2d}(1+|x|^2)/M\), where \(M=5\cdot4^d\).
Thus \(F(t)\asymp t^{1/(2d)}\) by measuring an arc of length comparable to \(t^{1/(2d)}\) centered at zero.
The row has nonclosed range and its kernel projection almost everywhere equals \(I-(1,x)^*(1,x)/(1+|x|^2)\).
This rank-one projection has nonconstant first diagonal entry \(|x|^2/(1+|x|^2)\).
All entries are rational Laurent functions with denominator \(3-z-z^{-1}\), \(z=e^{i\theta}\), which has no zeros in some open annulus containing the unit circle.
Their Laurent coefficients decay exponentially by Cauchy estimates on a smaller annulus.
The projection is supported on powers \(g^j\) in group Fourier coordinates, and \(|g^j|\le |j|\,|g|\) gives every polynomial spatial moment in [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace).

There is a different obstruction to deducing spatial decay of the kernel projection from its integral trace.
On \(\mathbb Z^2\), take the row \(A=(1-u,1-v)\) for the coordinate generators.
In the torus Fourier representation set \(z=e^{ix},w=e^{iy}\).
The projection onto the row's kernel has trace one almost everywhere, and off \((1,1)\) its first diagonal entry is
\[
               \frac{|1-w|^2}{|1-z|^2+|1-w|^2}.
\]
This function equals one on \(x=0\), \(y\ne0\) and zero on \(y=0\), \(x\ne0\).
Any continuous representative agreeing with it almost everywhere must agree everywhere on the punctured torus because both functions are continuous there and Haar measure has full support.
Thus the kernel projection does not belong to \(M_2(C_r^*(\mathbb Z^2))\), despite its integer trace.
The positive squared singular value is \(|1-z|^2+|1-w|^2\), comparable to \(x^2+y^2\) near the origin, so its range is nonclosed and \(F(t)\asymp t\) for the Gram matrix after normalization.
Cauchy–Schwarz on the \(j\)-th word annulus bounds its coefficient \(\ell^1\) norm by \(C2^j b_j\).
Either projection-tail condition in [L55](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) would therefore ensure an absolutely convergent Fourier series, contradicting the discontinuity.
This example concerns \(\mathbb Z^2\).
Estimate (1) on an individual four-line group constrains its positive spectral measure, leaving the spatial regularity of a nonclosed-range kernel projection as a separate question.

## Assessment history

### Decision nonclosed-spectral-mass

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:24 |
| status | proved |
| reason | The review verified the Fejer bounds, the common interval and the precise scopes of the three calibrations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Positive spectral mass near zero and uniform forbidden-gap tests for fixed four-line matrices. |
| argument | [Proof](#argument) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0092_v1.md#whole-argument-finding) | Independent review of the statement, proof and its direct inputs at the indicated scope. |

## Current assessment

[Selected decision](#decision-nonclosed-spectral-mass)
