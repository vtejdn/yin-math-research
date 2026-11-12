---
author: Yin
---
# A scalar nullity gap and the ICC rank dichotomy

## Statement

Let \(G\) be a nontrivial torsion-free ICC group, \(R=\mathbb C[G]\), \(N=\mathcal N(G)\), \(U=\mathcal U(G)\), and \(D=D(R,U)\) the actual scalar division closure.
Write \(\nu(B)\) for the regular dimension of the right kernel and \(r(B)\) for the range dimension, using the canonical trace and unnormalized matrix traces.
Define a number from single positive affiliated operators by
\[
 g_D=\inf\bigl(\{1\}\cup\{\nu(d):d\in D,\ d\ge0,\ 0<\nu(d)<1\}\bigr).
\]
For any finite matrix \(A\) over \(R\) of rank \(r\) and any positive integer \(m\) with \(mr\notin\mathbb Z\),
\[
                  g_D\le \lceil mr\rceil-mr .
\]
Consequently \(g_D>0\) gives a common integer denominator for all finite matrix ranks over \(R\).
For a single \(A:R^b\to R^a\), suppose \([C]=k[D]\) in \(G_0(D)\), with \(C=\operatorname{coker} A_D\).
Its signed sum of induction defects at the identity is \(S=k-(a-r(A))\), by the [exact-sequence calculation](../audits/literature/KLS17/Yin_U001.md#why-condition-3-has-not-been-cleared).
Thus \(g_D\le\lceil mS\rceil-mS\) whenever \(mS\notin\mathbb Z\), since \(S-r(A)\) is an integer.
If \(g_D>0\), then \(a-r(A)=k\) and every signed sum witnessing that fixed expression is zero.
Under journal KLS17 Theorem 3.7(3), either \(g_D=1\) and (4) holds, or \(g_D=0\) and regular nullities of positive finite matrices over \(R\) are dense in \([0,\infty)\).
In the latter case positive scalar elements of \(D\) have strictly positive nullities arbitrarily close to zero.
These alternatives give no unconditional exclusion of the second case.
The trivial group has \(D=\mathbb C\) and integral ranks directly.

## From one matrix to small positive kernels

Fix \(m\) as above, put \(T=A^{\oplus m}\), \(\ell=\lceil mr\rceil\) and \(\delta=\ell-mr\in(0,1)\).
The final projection \(p\) of \(T\) has trace \(mr\).
Projection comparison in a finite amplification of the factor supplies \(V\in M_{\ell,ma}(N)\) with \(V^*V=p\) and \(VV^*\le I_\ell\).
By Kaplansky density in matrix corners and norm density of the group ring in its reduced completion, take a uniformly bounded net \(V_j\in M_{\ell,ma}(R)\) converging strong-* to \(V\).
The positive matrices \(B_j=(V_jT)(V_jT)^*\) converge strongly and uniformly boundedly to \(B=(VT)(VT)^*\).
Each \(B_j\) has rank at most \(mr\), and \(V\) is isometric on the closed range of \(T\), so \(r(B)=mr\).
Thus \(\nu(B_j)\ge\delta=\nu(B)\).
For fixed \(t>0\) the continuous function \(f_t(s)=(1+ts)^{-1}\) majorizes \(1_{\{0\}}\) on the common spectral interval and its traces on \(B_j\) converge to its trace on \(B\).
Letting \(t\to\infty\) gives \(\limsup_j\nu(B_j)\le\delta\).
In particular, arbitrarily close upper approximations to \(\delta\) are nullities of actual positive group-ring matrices.
The comparison partial isometry only enters the limiting estimate.

Let \(H\) be a positive square matrix over \(D\) with \(0<\nu(H)=\eta<1\).
Its leading entry \(b=i^*Hi\), for the first-coordinate inclusion \(i\), is positive.
In affiliated matrices, \(b=(H^{1/2}i)^*(H^{1/2}i)\), so \(i\) takes \(\ker b\) into \(\ker H\).
Here kernels can be taken on free \(U\)-modules using support projections, and the square root is only needed over \(U\).
If \(\nu(b)>0\), then \(0<\nu(b)\le\eta\).
Otherwise \(b\) has full support and is invertible in \(U\), whence \(b^{-1}\in D\).
Writing \(H=\left(\begin{smallmatrix}b&v\\v^*&W\end{smallmatrix}\right)\), triangular congruence over \(D\) gives \(b\oplus(W-v^*b^{-1}v)\).
Positivity follows from congruence in affiliated matrices, and invertible right and left multipliers preserve the \(U\)-kernel dimension.
The Schur complement has nullity \(\eta\) and size one less.
Iteration gives a positive scalar \(d\in D\) with \(0<\nu(d)\le\eta\).
Applying this to the \(B_j\) with nullity less than one and passing to the infimum proves the inequality.

## Arithmetic of one cokernel class

If \(r\) is irrational, positive multiples approach an integer from below with arbitrarily small strictly positive errors.
If \(r=u/q\) in lowest terms with \(q>1\), choose \(m\) with \(mu\equiv -1\pmod q\) to obtain \(g_D\le 1/q\).
Thus for \(g_D>0\) a common denominator is \(\operatorname{lcm}(1,\ldots,\lfloor1/g_D\rfloor)\).
Linnell and Schick's uniform denominator theorem now makes the extended division closure \(E(R,U)\) semisimple Artinian. [LS12, journal Theorem 2.7, pp. 319–321](https://archive.intlpress.com/site/pub/files/_fulltext/journals/pamq/2012/0008/0002/PAMQ-2012-0008-0002-a001.pdf#page=7)
Its additional central idempotents must be central in \(U\), where the only ones are 0 and 1, so \(E(R,U)=D\).
All short exact sequences of \(D\)-modules now split.
Consequently tensoring the one class relation with \(U\) and taking dimension is legitimate, giving \(a-r(A)=k\).
Indeed every term of the [signed witness](../audits/literature/KLS17/Yin_U001.md#why-condition-3-has-not-been-cleared) already has zero defect at this stage.
This exactness is a consequence of the gap argument.

For instance, if one finite-index subgroup \(H\le G\) independently has all its finite group-ring matrix ranks in \(L^{-1}\mathbb Z\), restriction of scalars multiplies each rank by \([G:H]\).
The common denominator \(L[G:H]\) for \(G\) then yields the same single-class conclusion by LS12.
This uses a uniform assertion about \(H\), whereas the [coprime restriction argument](Yin_C_A0016_v1.md#finite-index-detection-and-coprime-restrictions) tests two covers for an individual matrix.

## Using global generation

Torsion-freeness reduces (3) to generation of \(G_0(D)\) by \([D]\).
If a common denominator exists, the preceding Artinian conclusion applies even when the denominator was obtained by another argument.
For \(D=\prod_{j=1}^s M_{n_j}(F_j)\) the simple classes give \(G_0(D)=\mathbb Z^s\) and \([D]=(n_1,\ldots,n_s)\).
Generation forces \(s=1=n_1\).
Over the resulting skew field every finite matrix reduces to an identity block and a zero block, also after embedding in \(U\), and the only scalar nullities are 0 and 1.

Conversely, if (3) holds and (4) fails, the full set of finite group-ring ranks cannot have a common denominator.
It contains an irrational rank or rational ranks of unbounded reduced denominator.
The positive compressions above thus give actual group-ring matrices \(B_j\) with \(0<\eta_j=\nu(B_j)\to0\).
For any \(t>0\), taking \(\lfloor t/\eta_j\rfloor\) copies gives positive matrices with nullities tending to \(t\).
Positive Schur elimination gives the stated scalar witnesses in \(D\).
Their \(D\)-cokernel classes have the form \(k_j[D]\), so their signed defects are congruent to \(-\nu(d_j)\) modulo \(\mathbb Z\), independently of the choice of \(k_j\).
Finally, integral ranks for all group-ring matrices force the actual \(D\) to be a skew field by [KLS17, Theorem 1.7](https://arxiv.org/pdf/1605.09069v2#page=4), so \(g_D=1\) in that case.
The proof neither deduces a positive gap from cyclic generation alone nor produces a torsion-free group in the dense alternative.
