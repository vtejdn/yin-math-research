---
author: Yin
---

# Original-group tests for a Schur kernel of dimension one half

For [A0001](../tasks/Yin_T_A0001_v1.md#contract), write \(U(G)\) for the affiliated algebra, \(D_j(G)\) for the actual scalar inverse layers starting at \(\mathbb CG\), and \(T_G\) for the center-valued trace normalized on one coordinate.
Take \(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) over \(\mathbb CG\) with \(a\) an affiliated unit, set \(S=d-ca^{-1}b\), and let \(P\in\mathcal N(G)\) be its kernel projection.
The [free cyclic extension construction](../claims/Yin_C_A0124_v1.md#the-kernel-projection-and-its-approximants) produces the exact projection at depth two upstairs if \(\tau(P)=1/2\).
The tests below use information about \(S\) or \(G\) to work in the original representation.

## Central Fourier coefficients and finite index

Affiliated Schur elimination identifies the kernel module of \(A\) with \(P U(G)\), and this identification respects every central cut.
Consequently \(T_G(P)=h_{A^*}\) in the notation for the [center-valued dimension of a group-ring cokernel](../claims/Yin_C_A0016_v1.md#statement).
In particular the coefficient of \(T_G(P)\) at a nonidentity element \(g\) of finite conjugacy class vanishes if there are a finite-index subgroup \(g\in H\le C_G(g)\) and a homomorphism \(H\to\mathbb Z\) nonzero on \(g\).
Central square-summable coefficients vanish on every infinite conjugacy class.
If the stated test applies to each nonidentity element of finite conjugacy class, it follows that \(T_G(P)=\tau(P)1\).
This includes groups with infinite conjugacy classes for all nonidentity elements.
At trace one half it excludes a central \(P\), since \(\tfrac12 1\) is not idempotent, and it gives equal center-valued dimensions for \(P\) and \(1-P\) even when the group von Neumann algebra has center.

Suppose \(K\le G\) has finite index \(n\) and satisfies the complex strong Atiyah conjecture.
Restrict regular left multiplication to its \(n\) left coset coordinates as a right \(K\)-module.
On group elements the diagonal coefficient at the identity in each coset gives \(n\) times the original trace on the image, and normality extends this identity to the von Neumann algebra.
The resulting embedding maps \(\mathbb CG\) into \(M_n(\mathbb CK)\).
As \(D_\infty(K)\) is a skew field, Gaussian elimination shows that a matrix over this skew field which is invertible in \(M_n(U(K))\) has inverse in \(M_n(D_\infty(K))\).
Induction therefore maps each scalar inverse layer of \(G\) into \(M_n(D_\infty(K))\).
All its scalar nullities belong to \(n^{-1}\mathbb Z\), and the same conclusion holds for the unnormalized nullities of arbitrary finite matrices over these layers.
An odd index already excludes nullity one half for \(S\).

For even index such a lower bound can still produce an exact finite-depth expression when \(T_G(P)=\tfrac12 1\).
Here are the tests to which discreteness applies.
Set \(q=1-P\), \(x=S^*S\), and take a partial isometry \(V\) with \(V^*V=P,\ VV^*=q\), using projection comparison.
Approximate \(V\) in the trace two-norm by \(h_0\in\mathbb CG\).
The kernel projection \(e\) of \(qh_0P\) within \(P\) satisfies \(\tau(e)=\|Ve\|_2^2\le\|V-h_0\|_2^2\), since \(qh_0e=0\).
Set \(h=h_0+\lambda1\) for \(|\lambda|>\|h_0\|\), which leaves \(qhP=qh_0P\) and makes \(h\) a bounded unit.
Positivity identifies \(e\) with the kernel projection of \(x^2+h^*xh\).
When \(\|V-h_0\|_2^2<1/n\), discreteness forces \(e=0\).
The positive Schur formula for \(P\) uses \(y=h^*xh\) and the one inverse of \(x^2+y\), so \(P\in D_2(G)\).
More generally a positive gap in the nullities of this specific family suffices.
Unrestricted finite-extension closure calculations also follow from the Artinian crossed-product mechanism, as detailed at [index two](Yin_L_A0003_v1.md#division-and-rational-closure-comparison).
The test here locates one inverse over the particular group-ring Schur scalar.

There is a separate exclusion for a central kernel projection when bounded norm calculus applies.
If \(a\) has a bounded inverse and the resulting bounded \(S\) has closed range, then \(S\in C_r^*(G)\) by spectral permanence and \(P\in C_r^*(G)\) by continuous functional calculus on the spectrum of \(S^*S\).
For torsion-free \(G\), every central projection of \(C_r^*(G)\) is zero or one.
Indeed its square-summable Fourier coefficients are constant on conjugacy classes, hence supported on the subgroup \(\Delta\) of elements with finite conjugacy class.
The subgroup expectation, obtained on finite sums by discarding terms outside \(\Delta\), therefore fixes the projection and puts it in \(C_r^*(\Delta)\).
Every finitely generated \(J\le\Delta\) has center of finite index \(n\), by intersecting the centralizers of its generators.
Left multiplication on the \(n\) cosets gives a matrix representation of \(J\) over the commutative ring \(\mathbb C Z(J)\).
Its determinant kills commutators and sends every central \(z\) to \(z^n\).
For \(h\in[J,J]\) one has \(h^n\in Z(J)\), and taking its determinant gives \(h^{n^2}=1\).
Torsion-freeness makes each such \(J\) abelian, so \(\Delta\) is torsion-free abelian.
Its compact dual is connected, and \(C_r^*(\Delta)\) consequently has only the two constant projections.
This rules out the central closed-range case with bounded pivot inverse. It uses the location of \(P\) in the reduced group algebra in the operator norm.

## A finite orbit of the denominator

Let \(K\le G\) satisfy the complex strong Atiyah conjecture, and let \(J=\langle\operatorname{supp}a\rangle\).
Suppose each coset \(sK\) for \(s\in\operatorname{supp}b\) has finite orbit for the left action of \(J\) on \(G/K\).
Equivalently, each \([J:J\cap sKs^{-1}]\) is finite.
For \(S\ne0\), its kernel in \(\ell^2(G)\) has zero intersection with \(\ell^2(K)\).
In particular \(P\in\mathcal N(K)\) and \(0<\tau(P)<1\) are incompatible under these hypotheses.

Indeed let \(F\) be the finite union of those orbits and choose representatives \(t_f\) of its cosets.
The case \(F=\varnothing\) gives \(S=d\) and the following coset calculation applies directly to \(d\).
Otherwise \(a\) acts on the invariant \(\bigoplus_{f\in F}t_f\ell^2(K)\) by a square group-ring matrix \(a_F\) over \(K\).
It is injective there because \(a\) is injective on the entire Hilbert space.
Thus its actual inverse has entries in \(D_\infty(K)\) by skew-field elimination.
Writing \(b=\sum_{f\in F}t_f b_f\) and multiplying the finite column \((b_f)\) by \(a_F^{-1}\) expresses \(a^{-1}b\) as \(\sum_{f\in F}t_f z_f\), \(z_f\in D_\infty(K)\).
This identity in \(U(G)\) follows by multiplying the displayed sum on the left by \(a\).
Multiplication by \(c\) and subtraction from \(d\) now give a finite expansion \(S=\sum_o t_o s_o\), where the \(t_oK\) are distinct and \(s_o\in D_\infty(K)\).
To verify independence of the cosets over \(U(K)\) on the right, clear any finite list of affiliated coefficients by a common bounded right denominator that is a unit in \(U(K)\).
Applying the bounded identity to \(\delta_e\) separates the different cosets by orthogonality.
Consequently \(SQ=0\) for a projection \(Q\in\mathcal N(K)\) forces \(s_oQ=0\) for each \(o\).
At least one \(s_o\) is a unit since \(S\ne0\), proving \(Q=0\).
If the Hilbert-space intersection above contained a nonzero vector, the closed span of its right \(K\)-translates in \(\ell^2(K)\) would define a nonzero such \(Q\).
The closed span of all its right \(G\)-translates is the range of the canonically embedded \(Q\) on \(\ell^2(G)\), and invariance of the kernel gives \(SQ=0\).
In particular a positive \(P\) belonging to \(\mathcal N(K)\) would give \(Q=P\).
This test can use an amenable \(K\) satisfying scalar injectivity by [amenable kernel localization](../claims/Yin_C_A0001_v2.md#proof-of-complete-rational-kernel-localization).

## Transverse kernels of an operator and its adjoint

At trace one half the projection for \(\ker S^*\) also has trace one half.
If \(\ker S\cap\ker S^*=\{0\}\), then the positive \(W=SS^*+S^*S\) has zero kernel and is an affiliated unit.
In the positive block matrix with rows \((W,S),(S^*,1)\), elimination at \(1\) leaves \(S^*S\), and elimination at \(W\) leaves \(B=1-S^*W^{-1}S\).
Thus \(\operatorname{rk}B=1/2\), \(0\le B\le1\) and \(BP=PB=P\).
Equality of traces forces \(P=B\in D_2(G)\).

In particular if \(S^2=0\), its closed range equals \(\ker S\) by containment and equality of their traces, interpreted equivalently as the range support in \(U(G)\).
Then \(\ker S^*=(1-P)\ell^2(G)\), and \(SS^*,S^*S\) have complementary support.
In this case \(P=SS^*W^{-1}\) as well.
These conditions test a proposed Schur expression without requiring a freely placed group element.
For a selfadjoint \(S\) with nonzero kernel, the two kernels coincide, so the first test does not give an inverse.

## All Ore fractions can fail to move a half-trace projection

Take \(G=(\bigoplus_{k\in\mathbb Z}\mathbb Z)\rtimes\mathbb Z\) with the shift action.
This group is torsion-free and elementary amenable.
A nonzero finitely supported lamp configuration has infinitely many shifts, and an element with nonzero shift component has infinitely many distinct conjugates by single-site lamp configurations, proving the ICC property.
Thus the group satisfies [complex strong Atiyah](Yin_L_A0001_v1.md), hence scalar injectivity, and each nonzero group-ring element is an affiliated unit.
The [right Ore fraction description](Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) applies by amenability.
Let \(P\) be the spectral projection of the lamp at site zero on a half-circle in its Haar distribution.
It has trace one half and scalar center-valued trace.
All its group conjugates are the same half-circle projection at translated lamp sites, and the projections at distinct sites commute and have product trace equal to the product of their traces.

Fix any \(h=uv^{-1}\in D_\infty(G)\) with \(u,v\in\mathbb CG\), \(v\ne0\).
Take the meet \(e\) of \(g^*Pg\) over \(g\in\operatorname{supp}u\cup\operatorname{supp}v\).
This is the product over a finite nonempty set of sites, so \(\tau(e)>0\).
For every such \(g\) one has \(Pge=ge\).
It follows that \(Pve=ve\), \(Pue=ue\), and \((1-P)hPve=(1-P)ue=0\).
The vector module \(veU(G)\) has trace dimension \(\tau(e)>0\) because \(v\) is an affiliated unit.
Hence \((1-P)hP\) has nonzero kernel inside \(P\) for every Ore fraction \(h\).
The obstruction persists through all scalar inverse layers for this projection.
Since this group itself satisfies strong Atiyah, the lamp projection cannot be the half-dimensional kernel projection of a group-ring Schur scalar.
The distinction identifies precisely where a test using an arbitrary half-trace projection loses an input from [A0001](../tasks/Yin_T_A0001_v1.md#contract).
