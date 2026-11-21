---
author: Yin
---
# Positive commutator frequencies from the affine Serre relations

## Scope

This development concerns the normality criterion in [C95](../claims/Yin_C_A0095_v1.md#statement) for the [complex zero-divisor task](../tasks/Yin_T_A0002_v1.md#contract).
It derives a positive quadratic form, a spectral triangularity condition, and a conditional nilpotence bound from the two affine \(\mathfrak{sl}_2\) Serre relations.
The arguments apply in any finite von Neumann algebra with a faithful trace, not only to group algebras.
They do not classify its representations or establish normality of a scalar group-ring element.
This is a proof development and comparison, not an independent review.

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, and let \(D\in M\) satisfy
\[
                         [D,[D,[D,D^*]]]=0.                    \tag{1}
\]
Taking adjoints also gives \([D^*,[D^*,[D^*,D]]]=0\).
Put
\[
 C=[D,D^*]=C^*,\qquad
 T=\tfrac12(L_C-R_C)\quad\hbox{on }L^2(M,\tau),
 \qquad E_n=T^nD\quad(n\ge0),                                \tag{2}
\]
where \(L_CX=CX\), \(R_CX=XC\), and the Hilbert inner product is
\(\langle X,Y\rangle_2=\tau(Y^*X)\), linear in its first argument.
The bounded operator \(T\) is self-adjoint.
All \(E_n\) lie in \(M\).

## The exact Serre-to-current interface

Use the classical Serre presentation of the positive part of the affine Lie algebra with Cartan matrix
\[
                         \begin{pmatrix}2&-2\\-2&2\end{pmatrix}.
\]
It identifies the Lie algebra on two generators \(a,b\), with defining relations
\((\operatorname{ad}a)^3b=(\operatorname{ad}b)^3a=0\), with the following subalgebra of \(\mathfrak{sl}_2\otimes\mathbb C[t]\):
\[
 \mathfrak n_+
 =\operatorname{span}_{\mathbb C}
 \{e\otimes t^n,\ f\otimes t^{n+1},\ h\otimes t^{n+1}:n\ge0\},
 \qquad a=e\otimes1,\quad b=f\otimes t.                      \tag{3}
\]
Here \([e,f]=h\), \([h,e]=2e\), and \([h,f]=-2f\).
The central extension of the full loop algebra contributes no term to these positive-root brackets.

The original passage used is [Kol15, arXiv:1310.0782v1, §2.1, pp.4–5](../literature/pdf/Kol15--arxiv-v1.pdf#page=4), also available as the [public original](https://arxiv.org/pdf/1310.0782v1).
Its formulas (2.1)–(2.4) give the loop realization, the generators \(e_1=e\otimes1,\ e_0=f\otimes t\), and this Cartan matrix.
The proof of Proposition 2.1 explicitly recalls that the positive part is defined by the Serre relations.
This presentation theorem is the algebraic input here; it is not proved anew in this ledger.
The source inspection covers the selected loop and presentation passage, not a full audit of Kolb's paper or of its cited proof of the Serre presentation.
The source's Proposition 2.1 itself concerns the different, inhomogeneous Onsager relations.
Those relations, and finite-dimensional tridiagonal-pair classification, are not being applied to \(D,D^*\).

The presentation, rather than merely verifying the relations in one loop representation, is essential.
It gives a Lie homomorphism from (3) to the commutator Lie algebra of \(M\), sending \(a\) to \(D\) and \(b\) to \(D^*\).
In (3), \(C\) corresponds to \(h\otimes t\), and therefore \(E_n\) corresponds to \(e\otimes t^n\).
For the adjoints,
\[
 E_n^*=\left(-\tfrac12\operatorname{ad}_C\right)^n D^*
\]
corresponds to \(f\otimes t^{n+1}\).
Consequently the elementary loop brackets give
\[
 [E_i,E_j]=0,\qquad [E_i^*,E_j^*]=0,\qquad
 [E_i,E_j^*]=H_{i+j+1},                                    \tag{4}
\]
\[
 H_m=[E_{m-1},D^*]=H_m^*,\qquad
 [H_m,E_j]=2E_{m+j},\qquad
 [H_m,E_j^*]=-2E_{m+j}^*,\qquad [H_m,H_n]=0.                \tag{5}
\]
Here \(i,j\ge0\) and \(m,n\ge1\).
For example, self-adjointness follows because the adjoint of \([E_i,E_j^*]\) is \([E_j,E_i^*]\), and both have the same current index.
In particular
\[
                             [D,E_n]=0\quad(n\ge0).          \tag{6}
\]
No finiteness of the dimension of \(L^2(M,\tau)\) or of the generated algebra has been used.

## A positive quadratic form and its moment identities

Let \(S=\operatorname{ad}_D\) on \(L^2(M,\tau)\).
Traciality gives \(S^*=\operatorname{ad}_{D^*}\), and the Jacobi identity gives
\[
                           2T=SS^*-S^*S.
\]
Thus, for every \(Z\in L^2(M,\tau)\),
\[
 2\langle TZ,Z\rangle_2=\|S^*Z\|_2^2-\|SZ\|_2^2.            \tag{7}
\]
If \(p(t)=\sum_{i=0}^r a_i t^i\) and \(Z=p(T)D\), equation (6) makes \(SZ=0\).
Hence
\[
 \boxed{\displaystyle
 \langle T p(T)D,p(T)D\rangle_2
   =\tfrac12\|[D^*,p(T)D]\|_2^2
   =\tfrac12\left\|\sum_{i=0}^r a_iH_{i+1}\right\|_2^2
   \ge0.}                                                  \tag{8}
\]
This is an exact identity of tracial quantities, not an asymptotic approximation.

For comparison with a finite polynomial calculation, put
\[
                         c_n=\tau(E_nD^*)=\langle T^nD,D\rangle_2.
\]
Self-adjointness of \(T\) and (4)–(5) yield
\[
 \tau(E_iE_j^*)=c_{i+j},\qquad
 \tau(H_mH_n)=2c_{m+n-1}.                                  \tag{9}
\]
For the second identity, cyclically move the commutator in \(H_m=[E_{m-1},D^*]\):
\[
 \tau(H_mH_n)=\tau(E_{m-1}[D^*,H_n])
             =2\tau(E_{m-1}E_n^*).
\]
Both finite Hankel matrices \((c_{i+j})_{i,j=0}^r\) and
\((c_{i+j+1})_{i,j=0}^r\) are therefore positive semidefinite.
Their Gram vectors are \(E_i\) and \(H_{i+1}/\sqrt2\), respectively.
The first low-degree moments are
\[
 c_0=\|D\|_2^2,\qquad
 c_1=\tfrac12\tau(C^2),\qquad
 c_2=\tfrac14\|[C,D]\|_2^2.
\]

## Nonnegative frequencies, spectral triangularity, and flux

Let \(\mathcal K=\overline{\operatorname{span}}\{T^nD:n\ge0\}\).
It is invariant under the bounded self-adjoint \(T\), hence reducing.
Equation (8), first on polynomial vectors and then by continuity, says that \(T|_{\mathcal K}\) is positive.
Equivalently the spectral measure
\[
                   \mu_D(B)=\langle1_B(T)D,D\rangle_2
\]
is supported on \([0,\infty)\).
This measure has total mass \(\|D\|_2^2\); it is not normalized unless that norm is one.
Writing \(a=\min\sigma(C)\), \(b=\max\sigma(C)\), its support is more precisely contained in
\[
                              [0,(b-a)/2]\subset[0,\|C\|].
                                                                    \tag{10}
\]

To obtain the operator meaning, \(L_C\) and \(R_C\) are commuting bounded self-adjoint operators.
Their joint spectral projection for a rectangle \(I\times J\) sends \(X\) to
\[
                         1_I(C)X1_J(C).
\]
Its joint spectral measure at \(D\) is supported where \(x\ge y\), since \(\mu_D\) is its image under \((x,y)\mapsto(x-y)/2\).
For every real \(t\), the rectangle \(x<t\le y\) therefore has zero mass.
Faithfulness of the \(L^2\)-norm gives
\[
 \boxed{\displaystyle 1_{(-\infty,t)}(C)D1_{[t,\infty)}(C)=0.}        \tag{11}
\]
Thus \(D\) preserves every upper spectral subspace of \(C\).
The direction in (11) is fixed by the convention \(C=DD^*-D^*D\).

Set \(P=1_{[t,\infty)}(C)\) and \(Q=1-P\).
Equation (11) says \(QDP=0\), so \(D\) has block form
\[
                         D=\begin{pmatrix}PDP&PDQ\\0&QDQ\end{pmatrix}.
\]
The \(P\)-corner of \(DD^*-D^*D\) is
\((PDP)(PDP)^*-(PDP)^*(PDP)+(PDQ)(PDQ)^*\).
Taking its trace cancels the first two terms and gives the exact flux identity
\[
 \boxed{\displaystyle
              \tau(PC)=\|PD(1-P)\|_2^2.}                    \tag{12}
\]
The spectral projections in (11)–(12) belong to \(M\); they are not asserted to have finite group support.

## A uniform positive frequency gap implies nilpotence

Assume additionally that \(\mu_D\) is supported in \([\delta,\infty)\) for some \(\delta>0\).
This excludes a zero-frequency component as well as frequencies arbitrarily close to zero.
The joint spectral measure is now supported where \(x-y\ge2\delta\).
For every real \(r\),
\[
                   1_{(-\infty,r+2\delta)}(C)
                   D1_{[r,\infty)}(C)=0.                    \tag{13}
\]
Indeed every point of the indicated rectangle has \(x-y<2\delta\).
Consequently \(D\) maps the upper spectral subspace starting at \(r\) into the one starting at \(r+2\delta\).
Start at \(r=a=\min\sigma(C)\), where the upper spectral projection is the identity, and iterate (13).
The range of \(D^m\) lies in \(1_{[a+2m\delta,\infty)}(C)\mathcal H\) in a faithful Hilbert-space representation.
This projection is zero if \(a+2m\delta>b\).
Thus
\[
                 D^m=0\qquad\text{whenever }2m\delta>b-a.    \tag{14}
\]
The strict inequality includes possible spectral atoms at the endpoints.
A gap only in the positive part of \(\mu_D\), while permitting an atom at zero, does not suffice: adding a scalar to a nonzero square-zero matrix gives an immediate counterexample to that stronger claim.

## Concrete calibrations

Let \(E=E_{12}\in M_2(\mathbb C)\) and
\[
                          D=E\otimes I+2I\otimes E
\]
in \(M_4(\mathbb C)\) with normalized trace.
The two summands and their opposite-factor adjoints commute.
If \(h=\operatorname{diag}(1,-1)\), then
\[
 C=h\otimes I+4I\otimes h,\qquad
 T(E\otimes I)=E\otimes I,\qquad
 T(I\otimes E)=4I\otimes E.
\]
It follows directly that the Serre relation holds and
\[
                    \mu_D=\tfrac12\delta_1+2\delta_4,\qquad
                    c_n=\tfrac12+2\cdot4^n.
\]
The first five moments are \(5/2,17/2,65/2,257/2,1025/2\).
Also \(D^2=4E\otimes E\ne0\) and \(D^3=0\).
This checks both the signs and the factor \(1/2\) in the positive form and the current identities.

The condition is restrictive for general bounded matrices.
Take
\[
                         W=\begin{pmatrix}0&1&0\\0&0&2\\3&0&0\end{pmatrix}.
\]
Its self-commutator is \(\operatorname{diag}(-8,3,5)\).
For the corresponding \(T_W\), the spectral measure at \(W\) is
\[
                    \tfrac13\delta_{-11/2}
                    +\tfrac43\delta_{-1}
                    +3\delta_{13/2}.
\]
The polynomial \(p(t)=(t-13/2)(t+11/2)\) kills the first and third atoms and gives
\[
              \langle T_Wp(T_W)W,p(T_W)W\rangle_2
                       =-\frac{6075}{4}.
\]
Thus (8) excludes this matrix from the Serre class.
All these numbers follow from the displayed diagonal self-commutator and its three matrix entries; they require no floating-point spectral calculation.

Finally a positive frequency gap is not automatic even for finite-support matrices over a torsion-free group.
For the generator \(z\) of \(\mathbb Z\), put
\[
 D=\begin{pmatrix}0&1+z\\0&0\end{pmatrix}
 \in M_2(\mathbb C[\mathbb Z]),\qquad
 P=(1+z)(1+z^{-1})=2+z+z^{-1}.
\]
Then \(D^2=0\), so the Serre relation holds, while \(C=\operatorname{diag}(P,-P)\) and \(T^nD\) has upper-right entry \(P^n(1+z)\).
Using normalized matrix trace and Haar measure on the circle,
\[
 \mu_D(B)=\frac12\int_0^{2\pi}
 (2+2\cos\theta)\,
 1_B(2+2\cos\theta)\,\frac{d\theta}{2\pi}.
\]
Its support is the entire interval \([0,4]\).
There is no atom at zero, but every interval \((0,\varepsilon)\) has positive mass.
Thus finite support and the Serre relations do not supply the extra gap in (14).

## What remains for the scalar group-ring question

For \(D\in\mathbb C[G]\), the derived elements \(E_n,H_n\) remain finite-support elements, so (8)–(9) are exact group-coefficient calculations using the canonical trace.
Equations (10)–(12) impose an additional analytic order on any proposed nonnormal solution of the criterion in C95.
They do not force \(C=0\).
The matrix calibrations already show why positivity and the Serre relations alone cannot give universal normality in a finite tracial algebra.

To turn this development into a scalar torsion-free obstruction, one would need a new argument showing that a nonzero scalar self-commutator cannot have this one-sided action on its spectral subspaces, or another actual group-ring constraint forcing the positive quadratic form to vanish.
No such argument has been established here.
In particular no finite-support formula for the projections \(P_t\), no automatic positive frequency gap, and no extension of finite-dimensional representation classification to arbitrary group von Neumann algebras is asserted.
