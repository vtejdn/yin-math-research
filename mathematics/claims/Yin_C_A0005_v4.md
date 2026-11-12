---
author: Yin
---
# Rank-two rational kernel transport: an exact boundary and a noncommuting witness

Date: 2026-11-12 (Asia/Hong_Kong).
This development serves [A0001](../tasks/Yin_T_A0001_v1.md#contract) by testing noncommuting transport of kernel projections derived from finite group-ring matrices.
It treats the zero-potential residual of [C_A0005 v3](../claims/Yin_C_A0005_v3.md#statement), without assuming that its transported projections commute.
The rank-two, rank-one-hopping case admits an exact common-defect formula, but its proof reduces completely to existing division-coefficient, saddle and graded certificates.
An explicit finite group-ring input realizes noncommuting transport, positive overlap defect and nonzero compressed transport, with an independently invertible residual.
The example therefore passes those three geometric screens but is rejected as a new mechanism after its rational cyclic gauge is exhibited.
No new Atiyah group class or historical priority is claimed.

## Statement

Let \(N\) be torsion-free abelian, let \(\sigma\in\operatorname{Aut}(N)\), and let \(G=N\rtimes_\sigma\langle t\rangle\), where \(t\) has infinite order and \(tnt^{-1}=\sigma(n)\).
Write \(F=\operatorname{Frac}(\mathbb CN)\) for its actual affiliated coefficient field.
The [abelian Fourier argument in C_A0005 v3](../claims/Yin_C_A0005_v3.md#finite-coefficient-origin-and-the-surviving-finite-orbit-certificate) proves this embedding independently: a nonzero Laurent denominator has Haar-null zero set, and every matrix over \(F\) has actual affiliated rank equal to its rank over \(F\).
These coefficient facts do not assume Atiyah for the semidirect product.
All matrix traces are unnormalized.
All unbounded products and inverses below are operations in the actual affiliated algebra; no inverse is applied to arbitrary Hilbert vectors without a domain argument.

Take \(A\in M_{k,d}(\mathbb CN)\) with \(\dim_F\ker_F A=2\), and put \(B=A^*A\).
Let \(V\in M_{d,2}(F)\) have columns forming a basis of \(\ker_F A\).
Then
\[
S=V^*V\in GL_2(F),\qquad p=VS^{-1}V^*
\tag{1}
\]
is the actual orthogonal kernel projection of \(A\), with trace two.
Put
\[
K=ptp\big|_p,\qquad R=p(t+t^{-1})p\big|_p=K+K^*,
\]
\[
\delta_+=p\wedge\sigma^{-1}(I_d-p),\qquad
\delta_-=p\wedge\sigma(I_d-p),\qquad
C=V^*\sigma(V)\in M_2(F).
\tag{2}
\]
The two projections in (2) are the corner kernel projections of \(K\) and \(K^*\), respectively.
Assume
\[
\operatorname{rank}_F C=1.
\tag{3}
\]
Then both defects have trace one, and the exact residual conclusion is
\[
\boxed{P_{\ker(R|_p)}=\delta_+\wedge\delta_-,\qquad
\dim_G\ker(R|_p)=\operatorname{Tr}_d\tau_N(\delta_+\wedge\delta_-)\in\{0,1\}.}
\tag{4}
\]
Thus a positive individual overlap defect does not imply a positive residual kernel.
The intersection in (4), rather than either individual defect, determines this minimal case.

For the actual finite group-ring matrix
\[
\mathcal H_A=\begin{pmatrix}(t+t^{-1})I_d&B\\B&0\end{pmatrix},
\tag{5}
\]
one consequently has
\[
\dim_G\ker\mathcal H_A
=2+\operatorname{Tr}_d\tau_N(\delta_+\wedge\delta_-)\in\{2,3\}.
\tag{6}
\]
The assertion concerns the zero-potential residual in (2).
No assertion is made for an additional arbitrary compressed coefficient \(php\).

## Argument

### Rational frame proof and independently admissible pivots

The Gram matrix in (1) is invertible because the columns of \(V\) have full rank almost everywhere in the abelian Fourier representation.
Its determinant is a nonzero element of \(F\), so this is an independently known actual affiliated inverse.
Choose columns \(Z\) over \(F\) spanning the orthogonal complement of the range of \(V\).
Then \(E=(V\ Z)\in GL_d(F)\), independently of the target residual.
For any operator \(X=pXp\), the affiliated identity
\[
E^*XE=\begin{pmatrix}V^*XV&0\\0&0\end{pmatrix}
\tag{7}
\]
shows that its corner rank equals the rank of \(V^*XV\).
The same construction for stacked operators compares simultaneous kernels.
It uses independently invertible square changes over \(F\), not a bounded-inverse claim for the possibly unbounded frame \(V\).
In particular,
\[
V^*KV=Ct,\qquad V^*K^*V=t^{-1}C^*,\qquad
V^*RV=Ct+t^{-1}C^*.
\tag{8}
\]
The rank of \(Ct\) is one, proving the two individual defect traces in the statement.

Choose a nonzero column \(w\in F^2\) spanning the line \(\sigma^{-1}(\ker_F C)\), and complete it to \(U=(w\ v)\in GL_2(F)\).
The determinant certificate for \(U\) is independent of every subsequent pivot.
The first column of \(C\sigma(U)\) vanishes, so
\[
C'=U^*C\sigma(U)=\begin{pmatrix}0&a\\0&b\end{pmatrix},
\qquad (a,b)\ne(0,0).
\tag{9}
\]
Changing the frame by \(U\) is an actual affiliated congruence, and gives
\[
M'=U^*(Ct+t^{-1}C^*)U
=\begin{pmatrix}
0&at\\ t^{-1}a^*&bt+t^{-1}b^*
\end{pmatrix}.
\tag{10}
\]
The placement of the adjoint term follows from \((C't)^*=t^{-1}C'^*\); coefficients are not commuted past \(t\).

If \(a\ne0\), the scalar \(a\in F^\times\) is an independently certified actual unit.
Thus \(k=at\) is a unit before any inverse of the residual is asserted.
With \(h=bt+t^{-1}b^*\), the ordered saddle inverse is
\[
\begin{pmatrix}0&k\\k^*&h\end{pmatrix}^{-1}
=\begin{pmatrix}
-(k^*)^{-1}hk^{-1}&(k^*)^{-1}\\
k^{-1}&0
\end{pmatrix}.
\tag{11}
\]
Multiplication in either order verifies (11) in the actual affiliated algebra.
Therefore \(R\) has zero corner kernel in this case.

If \(a=0\), then \(b\ne0\), and (10) is the direct sum of zero and
\[
r=bt+t^{-1}b^*.
\]
The scalar \(b\) and its adjoint are independently invertible over \(F\).
Moreover
\[
rt=bt^2+\sigma^{-1}(b^*)
\tag{12}
\]
has homogeneous degrees two and zero for the height character of \(G\), with an independently invertible constant coefficient.
The retained [affiliated graded-companion criterion](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials) therefore proves that \(r\) is an actual affiliated unit.
This remains valid if the coefficient inverse is unbounded.
Hence the residual nullity is exactly one in this case.

For completeness, the alternative in (9) has an intrinsic defect interpretation.
Under the frame \(V\), the kernel of \(K\) corresponds to the \(F\)-line \(\sigma^{-1}(\ker_F C)\), since \(Ct\) annihilates a coefficient column \(x\) exactly when \(C\sigma(x)=0\).
The kernel of \(K^*\) corresponds to the line \(\ker_F C^*\), since multiplication on the left by \(t\) turns its coordinate equation into \(C^*x=0\).
These coefficient-line descriptions also describe the actual affiliated kernels, by rank-one Gaussian elimination over the embedded field \(F\).
The first row of \(C'\) is \(w^*C\sigma(U)=(0,a)\), so
\[
a=0\quad\Longleftrightarrow\quad C^*w=0
\quad\Longleftrightarrow\quad
\sigma^{-1}(\ker_F C)=\ker_F C^*.
\tag{13}
\]
Two distinct lines over \(F\) have zero actual intersection; equal lines have trace one.
One can check this last assertion by the rank of the stacked defining matrices over \(F\), which equals their affiliated rank.
Equations (11)--(13) prove the dimension equality in (4).
The simultaneous kernel of the bounded operators \(K,K^*\) is visibly contained in the kernel of \(R\).
Equality of their finite traces and trace faithfulness then prove equality of the actual orthogonal projections in (4).
This last step avoids treating an unbounded rational frame as an everywhere-defined Hilbert-space isomorphism.

Finally \(B+p\in GL_d(F)\) is independently invertible: it is positive definite on the complement of \(p\) and the identity on \(p\) almost everywhere.
With \(X=(B+p)^{-1}\), the independently invertible congruence \(\operatorname{diag}(I_d,X)\) sends (5) to
\[
\mathcal H_p=\begin{pmatrix}(t+t^{-1})I_d&I_d-p\\I_d-p&0\end{pmatrix}.
\tag{14}
\]
The [bounded kernel parametrization](../claims/Yin_C_A0005_v2.md#path-blocks-and-the-exact-kernel-dimension) of this projection-middle matrix does not use commuting transport: it maps \((x,z)\) to \((x,z-(I_d-p)(t+t^{-1})x)\), for \(x\in\ker(R|_p)\) and \(z\in p\ell^2(G)^d\).
Its bounded inverse reads the upper coordinate and the \(p\)-part of the lower coordinate.
This proves (6) with no domain substitution involving \(X\).

### A finite group-ring witness with genuinely noncommuting transport

Let \(N=\langle x,y,z\mid[x,y]=[y,z]=[z,x]=1\rangle\cong\mathbb Z^3\), and let
\[
\sigma(x)=y,\qquad\sigma(y)=z,\qquad\sigma(z)=x.
\tag{15}
\]
The semidirect product \(G=N\rtimes_\sigma\langle t\rangle\) is torsion-free: a finite-order element maps trivially to the quotient \(\mathbb Z\), and then lies in the torsion-free subgroup \(N\).
Also \(\langle x,y,z,t^3\rangle\cong\mathbb Z^4\) has index three.
This already places the whole group in known virtually abelian coverage, independently of the following calculation.

Put \(\omega=e^{2\pi i/3}\), and define
\[
f=x+\omega^2y+\omega z,\qquad s=f^*f,\qquad
u=f(f^*)^{-1},\qquad D=\operatorname{diag}(1,1,u^2,u).
\tag{16}
\]
The nonzero Laurent polynomials \(f,f^*\) are independently invertible in the actual affiliated algebra by the abelian Fourier argument.
Because they commute, \(u^*u=uu^*=1\), so \(u\) is an actual bounded rational unitary, even though \((f^*)^{-1}\) need not be bounded.
Consequently \(D\) is a bounded rational unitary.
The exact transport identities are
\[
\sigma(f)=\omega f,\qquad \sigma(s)=s,\qquad
\sigma(u)=\omega^2u,\qquad
\sigma(D)=DU_0,\qquad U_0=\operatorname{diag}(1,1,\omega,\omega^2).
\tag{17}
\]

In \(\mathbb C^4\), let \(e_2=(0,1,0,0)^{\mathsf T}\), and put
\[
w_1=\frac1{\sqrt3}(1,0,1,1)^{\mathsf T},\qquad
w_2=\frac1{\sqrt2}(e_2+U_0^2w_1),\qquad
W=(w_1\ w_2),\qquad P_0=WW^*.
\tag{18}
\]
The three columns \(w_1,U_0w_1,U_0^2w_1\) are orthonormal and perpendicular to \(e_2\).
It follows that \(W^*W=I_2\).
Define the actual isometric frame and projection
\[
V=DW,\qquad p=VV^*=DP_0D^*.
\tag{19}
\]
The following specified matrix has finite group-ring coefficients:
\[
A=(I_4-P_0)\operatorname{diag}\bigl(f^2,f^2,(f^*)^2,ff^*\bigr)
\in M_4(\mathbb CN).
\tag{20}
\]
Indeed the constants in \(P_0\) are complex scalars and every displayed diagonal entry is a Laurent polynomial.
In the actual affiliated algebra,
\[
A=f^2(I_4-P_0)D^*,\qquad
B=A^*A=s^2(I_4-p).
\tag{21}
\]
The independent scalar unit \(f^2\) and the bounded unitary \(D\) prove that the actual kernel projection of \(A\) is precisely (19).
Alternatively (21) and the independent injectivity of \(s\) give the same kernel directly.
This construction derives \(p\) from finite coefficients and does not choose an arbitrary measurable projection.

The compressed coefficient is the constant matrix
\[
C=V^*\sigma(V)=W^*U_0W
=\begin{pmatrix}0&1/\sqrt2\\0&1/2\end{pmatrix}.
\tag{22}
\]
For example \(U_0w_2=(e_2+w_1)/\sqrt2\), giving the second column in (22), while the first column vanishes by orthogonality.
Thus \(C\) has rank one.
The compression \(V^*\sigma(p)V=CC^*\) has eigenvalues \(3/4\) and zero.
If \(p\) and \(\sigma(p)\) commuted, their compression \(p\sigma(p)p\) would be a projection and could only have eigenvalues zero and one.
Therefore
\[
[p,\sigma(p)]\ne0.
\tag{23}
\]
This is genuine noncommutation of the actual operator projections, not just a noncommuting choice of frames.
Their orbit has period three, since \(\sigma^3=1\) and (23) rules out a fixed projection.

Since the frame is isometric and (22) is constant, the defect projections are explicitly
\[
\delta_+=V\begin{pmatrix}1&0\\0&0\end{pmatrix}V^*,\qquad
\delta_-=Vhh^*V^*,\qquad
h=\binom{1/\sqrt3}{-\sqrt{2/3}}.
\tag{24}
\]
They both have trace one, and their intersection is zero because their coefficient lines are distinct.
In particular this witness has a nonzero overlap defect and is outside the zero-defect sufficient condition.

The residual is nonzero, and its exact isometric compression and inverse are
\[
V^*RV=
\begin{pmatrix}
0&t/\sqrt2\\t^{-1}/\sqrt2&(t+t^{-1})/2
\end{pmatrix},
\qquad
(V^*RV)^{-1}=
\begin{pmatrix}
-(t+t^{-1})&\sqrt2t\\\sqrt2t^{-1}&0
\end{pmatrix}.
\tag{25}
\]
Both sides of the inverse in (25) are bounded group-ring matrices over the infinite cyclic subgroup \(\langle t\rangle\).
Direct multiplication verifies this inverse, or it follows from (11) with the independently invertible off-diagonal entry \(t/\sqrt2\).
Thus the example is outside the \(p(t+t^{-1})p=0\) case as well.
It has an independently bounded inverse in its residual corner, even though either compressed one-direction transport has a one-dimensional kernel.

For the eight-coordinate finite group-ring matrix (5) with this \(A\), one has the complete bounded kernel identity
\[
P_{\ker\mathcal H_A}=\begin{pmatrix}0&0\\0&p\end{pmatrix},\qquad
\dim_G\ker\mathcal H_A=2.
\tag{26}
\]
Indeed the lower equation gives \(x=px\), and multiplying the upper equation by \(p\) then gives \(Rx=0\).
Equation (25) forces \(x=0\), after which the upper equation gives \(y=py\).
This proof of (26) uses only bounded equations.
The independent affiliated normalization can also be checked explicitly: \(J=\operatorname{diag}(I_4,s^{-2}I_4)\) is an actual unit and \(J\mathcal H_AJ=\mathcal H_p\), by (21).
No conclusion about the kernel was used to justify that normalization.

## What the discriminator establishes and why it stops here

The witness is beyond the commuting-orbit hypothesis of C_A0005 v3, the zero-overlap-defect criterion and the zero-residual two-cycle example.
Its noncommuting transport and positive defect nevertheless reduce by the explicit rational isometric gauge (19) to the cyclic saddle (25).
That reduction is the decisive old-criterion screen, so this example cannot be offered as a new mechanism for controlling noncommuting path addition.
Its whole group is already virtually abelian, and the general abelian-by-cyclic setting above is already within the elementary amenable coverage recorded in the [Lin93 audit](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems).
Neither whole-group result was used as a premise of the explicit inverses or rank calculations.

The rank-two calculation is more informative than another example because it exhausts the rank-one-hopping alternative under the stated rational-frame assumptions.
Every such case reduces to the independently invertible saddle (11), or to a zero channel and the known graded scalar unit (12).
The other hopping ranks are also previously controlled: rank two gives zero defect and the existing graded corner certificate, while rank zero gives \(R=0\).
Thus increasing the apparent complexity of the finite input while retaining a rank-two rational kernel and zero potential cannot escape these existing mechanisms.
The common-defect formula (4) is an exact additional description at this interface, not evidence for a new Atiyah class or a uniform constraint on arbitrary noncommuting projection orbits.

No further escalation of matrix size is part of this bounded test.
A later investigation would need an explicitly changed interface, such as higher kernel rank, a nonzero compressed potential, or a coefficient algebra without the independently available field argument.
None of those changes is claimed to solve the remaining conjecture, and the present calculation supplies no assertion that their next pivots are invertible.

## Source and verification scope

The reused inputs were the actual rational coefficient and Gram proof in C_A0005 v3, the bounded projection-middle kernel parametrization in C_A0005 v2, the zero-defect corner argument in C_A0005 v1, and the affiliated graded-companion proof in L_A0007 v1.
The local Lin93 source audit was inspected only for the stated existing group-class coverage.
No new external theorem, literature acquisition or historical novelty claim is needed for this construction.
The Fourier orthogonality, rational denominators, exact coefficient identities, overlap projections, ordered saddle inverse and bounded complete-kernel argument are proved explicitly above.

## Assessment history

### Decision reviewed-noncommuting-rank-two

| Field | Value |
| --- | --- |
| date | 2026-11-11T16:58 |
| status | proved |
| reason | Independent whole-artifact review supports the rank-one hopping dichotomy for rank-two rational kernel transport, exact common-defect projection, complete finite-matrix nullity and noncommuting finite-input witness at the stated zero-potential scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete formulas (1)--(6), torsion-free abelian coefficient setting, rank and trace conventions, common-defect equality and complete-kernel dimension. |
| argument | [Argument](#argument) | Complete formulas (7)--(26), actual rational frames and units, saddle/graded cases, finite witness, noncommutation, bounded inverse, exact kernel and continuation limitations. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0018_v4.md#finding-rank-two-noncommuting-transport) | Exact saved complete statement, proof, witness, direct dependency interfaces, known-coverage comparison and declared exclusions. |

## Current assessment

[Selected decision](#decision-reviewed-noncommuting-rank-two)

