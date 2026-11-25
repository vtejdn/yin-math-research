---
author: Yin
---

# Principal right ideals and kernel projections after extension to affiliated operators

For [A0003](../tasks/Yin_T_A0003_v3.md#contract), the kernel projection criterion asks whether \(p_x\), the orthogonal projection onto \(\ker x\), belongs to the division closure for every element \(x\) of that ring.
On 2026-11-25 a delegated researcher for Yin examined the image of the right annihilator of \(x\) after extension of scalars.
The resulting quotient measures precisely what can be lost when kernel vectors span a dense subspace.

## The obstruction for one principal right ideal

Let \(U\) be the affiliated algebra of a finite von Neumann algebra with faithful normal finite trace \(\tau\).
Let \(D\subseteq U\) be a unital division-closed \(*\)-subring and \(x\in D\).
Put \(I=\operatorname{ann}_D(x)\) and let \(IU\) denote the right ideal of finite sums of products \(yu\) with \(y\in I\), \(u\in U\).
There are natural right \(U\)-module identifications
\[
 \operatorname{Tor}^{D}_1(D/xD,U)
 \ \cong\ \ker\!\big(xD\otimes_D U\longrightarrow U\big)
 \ \cong\ p_x U/IU .
\]
The first identification follows from the exact sequence \(0\to xD\to D\to D/xD\to0\), because \(D\) is free over itself.
For the second, multiplication by \(x\) identifies \(xD\) with \(D/I\), so \(xD\otimes_D U\cong U/IU\).
The map induced by \(xD\hookrightarrow D\) sends \(v+IU\) to \(xv\).
The kernel of multiplication by \(x\) on \(U\) is \(p_x U\), by polar decomposition.

The three equivalent conditions
\[
 p_x\in D,\qquad p_x\in IU,\qquad
 \operatorname{Tor}^{D}_1(D/xD,U)=0
\]
therefore concern one specified element of \(D\).
Indeed \(p_x\in D\) implies \(I=p_xD\), which gives \(IU=p_xU\).
Conversely, if \(p_x\in IU\), write \(p_x=\sum_{i=1}^r y_i u_i\) with \(y_i\in I\) and \(u_i\in U\).
The left support of each \(y_i\) is dominated by \(p_x\), and their join is \(p_x\) since it fixes the displayed sum on the left.
Thus \(Y=\sum_i y_i y_i^*\) has support \(p_x\).
The positive element \(S=x^*x+Y\in D\) has zero kernel, so is a unit in \(U\) and has inverse in \(D\).
Multiplication by \(p_x\) gives \(p_xS=Y\), proving \(p_x=YS^{-1}\in D\).
The case \(p_x=0\) takes \(Y=0\).
This finite-span argument uses the same projection formula as the [annihilator criterion](../claims/Yin_C_A0133_v1.md#recovering-a-kernel-projection-from-generators).

Consequently \(D\) is regular if and only if every inclusion of a principal right ideal \(xD\hookrightarrow D\) stays injective under \(-\otimes_D U\).
Indeed recovery of every \(p_x\) gives an inner inverse of \(x\) by \((x^*x+p_x)^{-1}x^*\), and regularity gives all these projections by the [same scalar criterion](../claims/Yin_C_A0133_v1.md#argument).
These tests are also equivalent to flatness of the left \(D\)-module \(U\).
Flatness implies each test by definition, and over a von Neumann regular ring all left modules are flat.
For \(D=D_G\), this identifies [complete deletion](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected) with preservation of injectivity for these principal ideals.

## Rank density in the amenable case

Now let \(G\) be finitely generated amenable, \(A=\mathbb CG\), \(D=D_G\), and \(x\in D\).
The [amenable localization theorem](../claims/Yin_C_A0001_v2.md#rational-kernel-localization) gives density of \(\{a\delta_e:a\in A,\ xa=0\}\) in \(\ker_{\ell^2(G)}x\), including unbounded \(x\).
For finite \(F\subset I\cap A\), let \(q_F\) be the join in \(\mathcal N(G)\) of the left support projections of the elements of \(F\).
Each \(q_F\le p_x\), and their increasing net has supremum \(p_x\) by the stated density.
For the finite row \(C\) consisting of the elements of \(F\), multiplication by its affiliated Moore–Penrose inverse gives \(CC^{[-1]}=q_F\).
It follows that \(q_FU=\sum_{y\in F}yU\subseteq IU\).
Given \(v\in p_x U\), the approximants \(q_Fv\in IU\) satisfy
\[
       \operatorname{rk}(v-q_Fv)\leq \tau(p_x-q_F)\longrightarrow 0,
\]
where rank is the trace of the left support.
Thus \(IU\) is dense in \(p_xU\) for the rank metric.
Actual vanishing of the obstruction requires \(p_x\in IU\), that is, an exact finite sum.
For example, in the measurable functions on \(\mathbb N\) with weights \(2^{-n}\) for \(n\ge1\), the ideal of finite-support functions is rank dense and excludes the constant \(1\).
This illustration concerns the implication from density to equality for ideals.

## Matrix detection can leave part of a scalar kernel unseen

Consider a probability measure on \([1,2]\sqcup\{\star\}\sqcup\mathbb N\) which restricts to a positive multiple of Lebesgue measure on the interval and assigns positive mass to each listed atom.
In the affiliated algebra of complex measurable functions take the subring \(D\) consisting of triples
\[
       \big(r(t),\ r(0),\ (r(0)+f_n)_{n\ge1}\big),
       \qquad r\in\mathbb C(t)\ \text{regular at }0,\quad
       f\in\mathbb C^{(\mathbb N)} .
\]
Rational functions are identified almost everywhere on the interval.
This unital subring is closed under complex conjugation.
If a triple is an affiliated unit, its value \(r(0)\) is nonzero at \(\star\), its finitely many exceptional coordinates are nonzero, and its inverse has the same form with rational part \(1/r\).
Thus \(D\) is division closed and contains the indicator \(e_n\) of each individual atom \(n\).

Every finite rectangular matrix \(B\) over \(D\) with nonzero Hilbert kernel admits a nonzero kernel column over \(D\).
To see this, a deficient column rank at \(\star\) occurs also at every sufficiently large \(n\), since each entry there equals its value at \(\star\).
If column rank is deficient on a positive-measure subset of the interval, all full-column minors vanish identically as rational functions, hence vanish also at zero.
When there are fewer rows than columns the rank is deficient everywhere.
It follows in every case that \(B\) has deficient column rank on at least one atom \(n\).
Multiplying a nonzero constant vector in that fiber kernel by \(e_n\) supplies the required column.

For the scalar \(x=(t,0,0)\), a rational annihilator must vanish on the interval because \(t\ne0\) there.
Its rational part therefore vanishes identically and its value at \(\star\) is zero, giving \(\operatorname{ann}_D(x)=\bigoplus_n\mathbb C e_n\).
The projection onto the closed span of all these annihilator ranges is supported on \(\mathbb N\), while \(p_x\) also contains the atom \(\star\).
The trace deficit is the positive mass assigned to \(\star\).
This separates matrix detection from scalar kernel density for abstract division-closed \(*\)-subrings of finite tracial affiliated algebras.
The example leaves the group division-closure question in A0003 open.

Removing \(\star\) from the measure space and its coordinate from the triples gives a division-closed ring with dense rational kernel ranges at every matrix size and a nonzero scalar Tor obstruction.
Indeed, an affiliated unit still has \(r(0)\ne0\), because that value occurs at all but finitely many positive-mass atoms.
For a finite matrix, take a basis of its interval kernel over \(\mathbb C(t)\), clear denominators and multiply the resulting polynomial columns by \(t\).
These bounded columns, extended by zero at every atom, belong to the subring and span the full fiber kernel almost everywhere on the interval, by the nonzero minors of the matrix and of the basis.
The projections onto their closed ranges therefore span the interval kernel, and columns supported on the individual atoms span the atomic kernel.
Yet for \(x=(t,0)\) the full kernel is all of \(\mathbb N\), whereas \(\operatorname{ann}_D(x)U\) consists only of finitely supported functions.
Its scalar Tor quotient is \(\mathbb C^{\mathbb N}/\mathbb C^{(\mathbb N)}\).
Thus even density at every matrix size leaves an exact obstruction in this commutative example.

## An orthogonality criterion for semisimplicity

For the same amenable \(G\), \(D_G\) is semisimple Artinian if and only if there is no infinite sequence of nonzero \(z_j\in A\) with \(z_i^*z_j=0\) for \(i\ne j\).
In particular the absence of such a sequence suffices for complete deletion.
The conclusion about semisimplicity is stronger than the regularity needed by A0003.

To prove sufficiency, fix \(x\in D\) and start with \(S_0=x^*x\).
Whenever \(S_k=x^*x+\sum_{i=1}^k z_i z_i^*\) is a nonunit, choose \(0\ne z_{k+1}\in A\) with \(S_k z_{k+1}=0\) by amenable kernel localization.
Positivity of the summands gives \(xz_{k+1}=0\) and \(z_i^*z_{k+1}=0\) for \(i\le k\).
The absence of an infinite orthogonal sequence forces termination at an affiliated unit \(S_k\), so \(p_x=(\sum_{i=1}^k z_i z_i^*)S_k^{-1}\in D\).
Hence \(D\) is regular.

In this regular \(*\)-subring the left support of each \(y\in D\) belongs to \(D\) and generates \(yD\), since the [relative inverse](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected) belongs to \(D\).
Suppose the right module \(D\) were not a finite sum of simple modules.
Starting with \(q=1\), each projection \(q\) for which \(qD\) is not a finite sum of simple modules has a proper nonzero principal subideal \(yD\subsetneq qD\).
Its generating support projection \(e\) satisfies \(0<e<q\).
At least one of \(eD\) and \((q-e)D\) is again not a finite sum of simple modules.
Continuing inside that summand and retaining the other projection at each step gives infinitely many nonzero mutually orthogonal projections \(p_j\in D\).
Applying amenable kernel localization to \(1-p_j\) gives \(0\ne z_j\in A\) with \(z_j=p_j z_j\) for every \(j\).
Then \(z_i^*z_j=0\) for \(i\ne j\), contrary to the hypothesis.
Thus \(D\), as a right module over itself, is a finite sum of simples, proving that it is semisimple Artinian.

Conversely, a sequence of nonzero mutually orthogonal \(z_i\) as above gives an internal direct sum of the nonzero right ideals \(z_iD\).
In a relation \(\sum_{i=1}^r z_i d_i=0\), multiplication on the left by \(z_j^*\) gives \(z_j^*z_jd_j=0\), whence \((z_jd_j)^*(z_jd_j)=0\) and \(z_jd_j=0\).
An infinite direct sum of nonzero right ideals cannot occur in the finite-length regular module of a semisimple Artinian ring.
This completes the equivalence, leaving the general torsion-free case dependent on the scalar kernel projection test.
