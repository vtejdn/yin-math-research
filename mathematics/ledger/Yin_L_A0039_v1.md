---
author: Yin
---
# A four-coset higher-moment test in the Promislow group

The [higher-moment rank test](../claims/Yin_C_A0027_v1.md#a-coefficient-test-above-the-fourth-moment-threshold) uses a finite product table with a repeated difference.
This table occurs in the Promislow group, where every homomorphism to \(\mathbb Z\) vanishes.
The group has known integer ranks by its [explicit division certificate](../claims/Yin_C_A0013_v1.md#statement).
The calculation below measures what the two moment tests themselves detect.

## The difference table

Use the [actual group and translation subgroup](Yin_L_A0024_v1.md#fixed-setting-and-proposed-test)
\[
 P=\langle u,v\mid v^{-1}u^2v=u^{-2},\quad u^{-1}v^2u=v^{-2}\rangle,\qquad
 \langle u^2,v^2,z\rangle\cong\mathbb Z^3,\quad z=(uv)^2 .
\]
The presentation gives \(4[u]=4[v]=0\) in the abelianization, so \(\operatorname{Hom}(P,\mathbb Z)=0\).
Let \(H=\langle z\rangle\), and take \(x_1=1,x_2=u,x_3=u^2,x_4=v\).
There is a homomorphism from \(P\) onto the infinite dihedral group of isometries of \(\mathbb Z\), taking \(u\) to the translation \(r:n\mapsto n+1\) and \(v\) to the reflection \(s:n\mapsto-n\).
Indeed \(s^2=1\) and \(s r^2 s=r^{-2}\).
The element \(z\) maps to the identity, and the four images \(1,r,r^2,s\) are distinct, so the four right \(H\)-cosets are distinct.

In \(Y=\{x_i x_j^{-1}\}\), the differences between powers of \(u\) give the five elements \(u^k\), \(-2\le k\le2\).
Among their off-diagonal occurrences, \(u,u^{-1}\) each occur twice and \(u^2,u^{-2}\) once.
The remaining six off-diagonal differences are \(u^i v^{-1}\) and \(v u^{-i}\) for \(0\le i\le2\).
These two elements project to the same reflection \(r^i s\), but are inverses of each other and distinct by torsion-freeness.
The three reflections down in the dihedral quotient are distinct, proving that no additional differences coincide in \(P\).
In particular two cells share the double coset \(HuH\).

The element \(u^4\) lies outside \(Y\).
A product of two of the three dihedral reflections in the image of \(Y\) has translation exponent between \(-2\) and \(2\).
A product of a translation and a reflection is again a reflection.
Thus a product of two elements of \(Y\) projecting to \(r^4\) must have both images equal to \(r^2\).
The only element of \(Y\) over \(r^2\) is \(u^2\), so \(u^4\) has exactly one ordered representation in \(YY\).

## An eight-term input

Take \(t=9999/10000\), \(c=(1,1,1,t)\), \(\epsilon=10^{-9}\), and
\[
       a_\epsilon=\sum_{i=1}^4 (c_i+\epsilon z^i)x_i .
\]
Each of the four cosets now has two support points, and the four Laurent polynomials have different positive exponents.
Normalize each pointwise coefficient vector \(f_\epsilon(\omega)=(c_i+\epsilon\omega^i)_i\), \(|\omega|=1\), by its Euclidean norm to obtain a vector \(g_\epsilon\).
Write \(A_\epsilon=\sum_i g_{\epsilon,i}(z)x_i\), \(X_\epsilon=A_\epsilon A_\epsilon^*\), and \(s_\epsilon=\tau(X_\epsilon^2)\).
The left normalization preserves regular rank and gives \(\|A_\epsilon\|\le2\).

At \(\epsilon=0\), the table above gives
\[
 s_0=2+\frac{1-t^4}{(3+t^2)^2},\qquad
 \widehat{X_0^2-2X_0}(u^4)=\frac{1}{(3+t^2)^2}.
\]
For this \(t\), \(0.000024<s_0-2<0.000026\) and the displayed Fourier coefficient exceeds \(1/16\).
The coefficient vector changes before normalization by at most \(2\epsilon\) in Euclidean norm.
For nonzero vectors \(p,q\), the distance between their unit vectors is at most \(2\|p-q\|/\|q\|\) by the triangle inequality.
Hence \(\sup_{\omega}\|g_\epsilon(\omega)-g_0(\omega)\|_2\le4\epsilon/\sqrt{3+t^2}\).
Multiplication by the column of unitaries \((x_i)_i\), whose norm is two, gives \(\|A_\epsilon-A_0\|<5\epsilon\).
The bounds \(\|A_\epsilon\|,\|A_0\|\le2\) now yield
\[
 \|X_\epsilon-X_0\|<20\epsilon,\qquad |s_\epsilon-s_0|<160\epsilon,\qquad
 \|(X_\epsilon^2-2X_\epsilon)-(X_0^2-2X_0)\|<200\epsilon .
\]
Since each Fourier coefficient has absolute value at most the operator norm, \(0<s_\epsilon-2<0.000027\) and \(|\widehat{X_\epsilon^2-2X_\epsilon}(u^4)|>0.062\).
Consequently \(1/s_\epsilon<1/2\), whereas \(0.062^2>16(0.000027)\) excludes \(r(a_\epsilon)\le1/2\) by [the variance bound](../claims/Yin_C_A0027_v1.md#two-moment-tests).

## Product fibers for a specified second support

Let \(S=\operatorname{supp}a_\epsilon\) and choose \(S^{-1}\) as the second support, as for the actual adjoint.
There are eight representations of the identity in \(SS^{-1}\), one from each point of \(S\).
However, a pair giving \(z^3u^2\) must project to the translation \(r^2\).
Among the four images \(1,r,r^2,s\) this difference forces the first point over \(r^2\) and the second over \(1\).
The corresponding pairs have products \((z^i u^2)(z^j)^{-1}=z^{i-j}u^2\), since \(u^2\) and \(z\) are commuting translations, with \(i\in\{0,3\}\) and \(j\in\{0,1\}\).
The exponent \(3\) occurs just once.
Thus any factors with these two exact supports have a nonzero coefficient at \(z^3u^2\).
The scalar rank calculation concerns \(a_\epsilon\) itself, while this singleton argument concerns this particular choice of second support.
