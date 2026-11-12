---
author: Yin
---
# Pairwise Haar laws do not remove a three-term kernel

Date: 2026-11-12 (Asia/Hong_Kong).
The [cyclic spectral inertia bound](../claims/Yin_C_A0009_v2.md#statement) uses only the three pairwise relative Haar distributions.
This investigation tests whether those same marginal constraints could by themselves force the remaining kernel to vanish.
An explicit finite tracial model below has all three relative laws Haar and has kernel trace exactly \(1/10\).
Its joint trace fails the regular group-word test at a specified word.
It is therefore an obstruction to the marginal-only inference, not an Atiyah counterexample.

## A two-dimensional kernel model

Write \(b=\sqrt3/2\), and let \(z,w\) be independent circle coordinates with normalized Haar measure.
In \(M_2(L^\infty(\mathbb T^2))\), with normalized matrix trace, put
\[
U_b(z,w)=
\begin{pmatrix}-1/2&bz\\ b&z/2\end{pmatrix},
\qquad
V_b(z,w)=
\begin{pmatrix}1/2&bw\\ b&-w/2\end{pmatrix}.
\tag{1}
\]
Both matrices are unitary: their columns have norm one and are orthogonal, using \(b^2=3/4\).
The first column of \(I_2+U_b-V_b\) is zero, and the second is
\[
\binom{b(z-w)}{1+(z+w)/2}.
\tag{2}
\]
This second column vanishes exactly at \(z=w=-1\), a Haar-null point.
Thus the bounded matrix has rank one almost everywhere and
\[
\tau_b(P_{\ker(I_2+U_b-V_b)})=\frac12.
\tag{3}
\]
No inverse, regular group law or zero-divisor conjecture is used.

### Exact three marginal distributions

For real \(|a|<1\), define the nonnegative Poisson density on the circle by
\[
P_a(\zeta)=\frac{1-a^2}{|\zeta-a|^2},
\qquad
\rho_a(\zeta)=\frac{1+P_a(\zeta)}2.
\tag{4}
\]
Normalized Haar integration of \(P_a\) is one, and its nonzero integer moments are \(a^{|n|}\).
These assertions follow directly by multiplying the two absolutely convergent geometric series for \((1-a\zeta)^{-1}\) and \((1-a\zeta^{-1})^{-1}\).
Hence \(\rho_a\) has nonzero moments \(a^{|n|}/2\).
At \(a=\pm1/2\), the elementary bounds are
\[
\frac23\le\rho_a(\zeta)\le2.
\tag{5}
\]

For each positive integer \(n\), the entries of \(U_b^n\) are polynomials in \(z\), so Haar averaging picks their constant terms.
At \(z=0\), the matrix in (1) is \(\left(\begin{smallmatrix}-1/2&0\\b&0\end{smallmatrix}\right)\), whose \(n\)-th power has trace \((-1/2)^n\).
Consequently
\[
\tau_b(U_b^n)=\frac{(-1/2)^n}{2},
\qquad
\tau_b(V_b^n)=\frac{(1/2)^n}{2}.
\tag{6}
\]
The substitution \(z=0\) is only a device for extracting a polynomial coefficient, not an asserted unitary evaluation or actual rational specialization.
Negative moments are the complex conjugates of the positive ones by unitarity.
Thus the two spectral laws have densities \(\rho_{-1/2}\) and \(\rho_{1/2}\).

The third relative unitary is
\[
U_b^*V_b=
\begin{pmatrix}
1/2&-bw\\ bz^{-1}&z^{-1}w/2
\end{pmatrix}.
\tag{7}
\]
Conjugating by \(\operatorname{diag}(1,z^{-1})\) in the order \(D^*(U_b^*V_b)D\) gives
\[
\begin{pmatrix}1/2&-b\eta\\b&\eta/2\end{pmatrix},
\qquad \eta=wz^{-1}.
\]
The coordinate \(\eta\) is Haar, and the same constant-term calculation gives positive moments \((1/2)^n/2\).
Therefore its spectral density is also \(\rho_{1/2}\).
Equality of all integer moments identifies these circle measures, by density of trigonometric polynomials in continuous functions.
All three densities are bounded and atomless, but none is Haar yet.

## A compensating commuting model

For shortness write \(\rho_-=\rho_{-1/2}\), \(\rho_+=\rho_{1/2}\).
On a second torus with coordinates \(s,t\), define
\[
f(s,t)=
1-\frac14\left[
(\rho_-(s)-1)+(\rho_+(t)-1)+(\rho_+(t/s)-1)
\right].
\tag{8}
\]
Every bracketed summand has integral zero.
By (5), their sum lies in \([-1,3]\), so
\[
\frac14\le f(s,t)\le\frac54,\qquad
\int_{\mathbb T^2}f(s,t)\,ds\,dt=1.
\tag{9}
\]
This is a faithful probability density.
Let \(\tau_g\) be integration against it on the commutative finite von Neumann algebra \(L^\infty(\mathbb T^2,f\,ds\,dt)\), and let \(U_g=s\), \(V_g=t\).

The three marginals of \(s,t,t/s\) under this measure have densities respectively
\[
1-\frac14(\rho_--1),\qquad
1-\frac14(\rho_+-1),\qquad
1-\frac14(\rho_+-1).
\tag{10}
\]
For example, integrating (8) in \(t\) kills both the \(t\)-term and the \(t/s\)-term, yielding the first formula.
For the third, set \(t=s\eta\); Haar measure is unchanged, and integration in \(s\) kills the first two terms.
The second formula follows similarly.
This proves the three marginal identities simultaneously, rather than specifying unrelated individual laws.

The scalar function \(1+s-t\) vanishes at only two points of the torus: \(|1+s|=1\) forces \(s=e^{\pm2\pi i/3}\), and then \(t=1+s\) is determined.
The bounded density \(f\) assigns zero measure to that set.
Therefore
\[
\tau_g(P_{\ker(1+U_g-V_g)})=0.
\tag{11}
\]

## A faithful finite trace with pairwise relative Haar unitaries

Take the direct sum
\[
M=M_2(L^\infty(\mathbb T^2))\oplus
L^\infty(\mathbb T^2,f\,ds\,dt),
\qquad
\tau=\frac15\tau_b+\frac45\tau_g,
\]
and define
\[
U=U_b\oplus U_g,\qquad V=V_b\oplus V_g.
\tag{12}
\]
The trace is faithful, normal and finite, with \(\tau(1)=1\).
The two unitaries and their relative product \(U^*V\) all have exactly Haar spectral law.
Indeed each corresponding density is
\[
\frac15\rho+\frac45\left(1-\frac14(\rho-1)\right)=1.
\tag{13}
\]
The reversed relative products have the conjugate Haar law.
Thus the triple \(U_0=1,U_1=U,U_2=V\) satisfies every pairwise relative Haar premise of the matrix-algebra form of the inertia bound.
Nevertheless (3) and (11) give
\[
\boxed{\tau(P_{\ker(1+U-V)})=\frac1{10}>0.}
\tag{14}
\]
The bound \(1/10\le1/3\) is consistent with that theorem.
The construction is not claimed optimal for the marginal hypotheses.

If individual Haar laws for all three summands are also desired, tensor \(M\) with one independent central circle algebra with Haar generator \(h\).
The three unitaries
\[
\widetilde U_0=h,\qquad
\widetilde U_1=hU,\qquad
\widetilde U_2=hV
\tag{15}
\]
are each Haar, as their nonzero integer moments have a zero central-circle factor.
Their pairwise relative products are the same as those of \(1,U,V\).
Their signed sum is \(h(1+U-V)\), with the same kernel projection and trace \(1/10\).
Thus adding all individual Haar requirements does not remove this obstruction.

## The explicit failure of the regular joint-word condition

The canonical regular trace of an actual group unitary word is one if the word is the identity and zero otherwise.
This model fails that condition at a short word.
Direct multiplication in (1) gives
\[
\tau_b(U_bV_b)=-\frac18.
\tag{16}
\]
All the other trace terms contain \(z,w\) or \(zw\) with nonzero exponent and integrate to zero.
In the commuting component,
\[
\tau_g(U_gV_g)=\int_{\mathbb T^2}st\,f(s,t)\,ds\,dt=0.
\tag{17}
\]
The constant-density, \(s\)-only and \(t\)-only terms vanish by integration in the other coordinate.
For the \(t/s\)-term, put \(t=s\eta\); the remaining factor \(s^2\eta\) has zero integral in \(s\).
It follows that
\[
\boxed{\tau(UV)=-\frac1{40}\notin\{0,1\}.}
\tag{18}
\]
Consequently these specific unitaries with this trace cannot be identified with two actual group elements under any canonical regular group trace.
This exclusion does not depend on whether their generated abstract unitary group has torsion.
For the tensor-enlarged three-summand model, the word
\(\widetilde U_0^{-1}\widetilde U_1\widetilde U_0^{-1}\widetilde U_2=UV\)
has the same forbidden trace.

The inputs are legitimate bounded finite-von-Neumann-algebra unitaries, with exactly computed simultaneous marginal laws and kernel projection.
They are not an admissible replacement for the actual group-ring generators in A0001.
In particular, no fractional group-ring rank over a torsion-free group has been constructed.

## Consequence for the strategy

The coefficient-angle bound can be used as an independent quantitative constraint in the actual group problem.
No proof that uses only its pairwise relative Haar hypotheses, even with all individual Haar laws added, can strengthen the conclusion to zero kernel.
Additional regular joint-word information or an independently certified kernel-preserving algebraic reduction is necessary for that next inference.
Equation (18) identifies exactly one such missing joint constraint; it does not prove that imposing this one word alone would suffice.
This complements the [inverse-difference joint-word obstruction](../claims/Yin_C_A0006_v1.md#joint-words-still-contain-the-unknown-input), now with an explicit nonzero three-term kernel and all relative Haar laws simultaneously enforced.
The construction uses direct polynomial multiplication, bounded spectral measures and the displayed elementary geometric series; no new external theorem or historical priority is asserted.
