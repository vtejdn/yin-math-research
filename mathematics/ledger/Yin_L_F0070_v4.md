---
author: Yin
---

# A physical residue detector for the commutator cubic

The 19 November 2026 continuation of [the discrete-pencil exploration](Yin_L_F0070_v3.md#continuation) tests \(P=[x,y]x=xyx-yx^2\).
Yin's agent-S supplied the four-channel calculation, and the main agent checked its eigenvectors and coefficient identity.
The result is an algebraic detector for the actual cross-color Schur quadratic term.
It does not establish a random lower bound or a Brown limit for this polynomial.
The [three-channel prototype and its limitations](Yin_L_F0070_v3.md#physical-detector) are retained separately.

<a id="cyclic"></a>
## Four channels with a common final letter

Let
\[
 A=E_{12}+E_{34}+E_{41},\qquad B=-E_{13}+E_{24},\qquad
 T(X,Y)=A\otimes X+B\otimes Y
 =\begin{pmatrix}
 0&X&-Y&0\\
 0&0&0&Y\\
 0&0&0&X\\
 X&0&0&0
 \end{pmatrix}.
\]
For \(z\ne0\), eliminate the last three channels of \(zI-T\).
Their triangular pivot has determinant \(z^{3N}\), and its Schur complement is
\(zI-z^{-2}(XYX-YX^2)\).
Both sides are polynomials in \(z\), so
\[
 \det(zI_{4N}-T(X,Y))=z^N\det(z^3I_N-P(X,Y))              \tag{1}
\]
also holds at zero.
This is an ordinary spectral linearization, with one structural zero eigenvalue per physical site.
For commuting scalar \(x,y\), \(P(x,y)=0\), and the scalar characteristic polynomial of \(xA+yB\) is \(z^4\).
Thus every such specialization misses the variable poles at \(z\ne0\).
The [general cyclic transfer](../claims/Yin_C_F0359_v1.md#statement) explains the scalar spectral use of (1).

<a id="witness"></a>
## A symmetric two-dimensional witness

Use
\[
 X=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 Y=\frac12\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 K=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad Q=T(X,Y).
\]
This is a deterministic rational-identity evaluation, not a replacement input law.
Here \(XYX=-Y\), \(YX^2=Y\), and \(P(X,Y)=-2Y\).
Equation (1) gives
\[
                        \det(zI_8-Q)=z^2(z^6-1).         \tag{2}
\]
In particular \(\lambda=1\) is a simple eigenvalue.
With \(u=(1,-1)^{\mathsf T}\) and \(v=(1,1)^{\mathsf T}\), put
\[
 r=(u,v/2,u,v)^{\mathsf T},\qquad
 l=(u^{\mathsf T},v^{\mathsf T},u^{\mathsf T}/2,v^{\mathsf T}).
\]
Direct multiplication gives \(Qr=r\), \(lQ=l\), and \(lr=6\).
The spectral projector is \(P_1=rl/6\).
Its antisymmetric physical partial trace is
\[
 F_{ab}=\operatorname{Tr}_2(K(P_1)_{ab}),\qquad
 F=\frac16\begin{pmatrix}
 0&-2&0&-2\\
 1&0&1/2&0\\
 0&-2&0&-2\\
 2&0&1&0
 \end{pmatrix}.
\]
Multiplication by the fixed auxiliary coefficients gives
\[
 D:=BFA-AFB
 =\frac16\begin{pmatrix}
 2&0&1&0\\
 0&2&0&1\\
 0&0&2&0\\
 0&0&0&2
 \end{pmatrix},\qquad
                         \det D=\frac1{81}.             \tag{3}
\]

<a id="schur"></a>
## The actual cross-color observation

Let \(R_z=(zI-A\otimes x-B\otimes y)^{-1}\).
The two fresh real columns \(a,b\) in a principal Wigner extension produce the quadratic Schur term
\[
 (A\otimes a^{\mathsf T}+B\otimes b^{\mathsf T})
 R_z(A\otimes a+B\otimes b).
\]
For each auxiliary entry \(i,j\), its physical/color coefficient matrix is
\[
 \mathscr M_{ij,z}=
 \begin{pmatrix}
 (AR_zA)_{ij}&(AR_zB)_{ij}\\
 (BR_zA)_{ij}&(BR_zB)_{ij}
 \end{pmatrix}.
\]
The transpose-symmetric part is the actual quadratic coefficient; transpose here does not conjugate \(z\).
At the witness define \(H=\left(\begin{smallmatrix}0&K\\-K&0\end{smallmatrix}\right)\).
It is symmetric and zero-diagonal, and the trace pairing gives
\[
 \operatorname{Tr}_4(H\,\operatorname{sym}\mathscr M_{ij,z})
 =\operatorname{Tr}_2(K(BR_zA-AR_zB)_{ij}).               \tag{4}
\]
Consequently this observation survives both the quadratic symmetry and removal of diagonal-square terms.
It is a genuine cross-color coefficient functional, not the discarded ambient derivative in a single sign.

Substitute \(x=tX,y=tY\).
At any nonzero node \(z\),
\[
 \operatorname*{Res}_{t=z}(zI-tQ)^{-1}=-P_1.
\]
Apply minus this residue to (4).
The resulting auxiliary matrix is exactly \(D\) in (3), and it is invertible.
It annihilates scalar physical kernels.
For another nonzero node \(w\), it also annihilates its kernel whenever
\[
                        w/z\notin\mu_6,                 \tag{5}
\]
where \(\mu_6=\{\omega\in\mathbb C:\omega^6=1\}\).
Indeed all possible nonzero poles of \((wI-tQ)^{-1}\) occur at \(t=w/\omega\).
Impose (5) for every pair of distinct nodes in the full list, including their conjugates.
These exclusions have planar product measure zero.

As in the [joint quotient argument](../claims/Yin_C_F0363_v4.md#quotient), a formal relation among the kernels modulo scalar physical kernels remains valid at this matrix evaluation.
Taking the selected residue isolates the node and pairs its coefficient with \(D\).
Finite-dimensional annihilator duality therefore supplies a node-supported invertible matrix in the actual joint coefficient image.
Retaining conjugate nodes gives the equivalent statement for the real and imaginary kernel basis.
This is a formal rational-kernel conclusion and does not assert that the corresponding evaluated physical kernel has a uniform lower singular value on random old blocks.

<a id="remaining"></a>
## What this resolves and the next probability test

The test supplies the missing algebraic detector for this particular commuting-zero cubic.
It shows concretely why finite matrix evaluations can do more than commuting residues, while retaining the original physical Schur symmetry.
It gives no general implication from coefficient irreducibility to the existence of such a detector.

At the level of detector dimensions, all four auxiliary rows and columns are available, and the prospective choice \(a=b=4\) has \(a+b=8>p=4\).
This numerical surplus is only the dimension requirement in the [selected-volume route](../strategies/Yin_S_F0035.md).
It does not prove that eight independently testable physical directions exist after conditioning.

The next test must simultaneously establish an exposure-compatible initial principal trim, joint projected spread for the actual cross-color kernels, and quantitative polarization on the original independent signs.
Only then can the full-rank detector enter a restoration inequality.
The [existing old-measurable oversampling estimate](../claims/Yin_C_F0196_v5.md#restricted-small-ball), the [transverse covariance identity](Yin_L_F0070_v3.md#joint-covariance), and the [conditional LCD alternative](../drafts/Yin_D_F0045.md) describe distinct interfaces for this step.
Their hypotheses must be checked on the same physical exposure.
No summable smallest-singular-value estimate, terminal logarithmic bound, or new almost-sure Brown-convergence assertion is made here.
