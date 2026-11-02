---
author: Yin
---

# Ordered matrix minimax for strictly Hilbert--Schmidt-positive covariance and arbitrary selfadjoint drift; exact obstruction outside that class

## Current assessment
[Selected decision](#decision-finding-owned-review)

## An Ordered Variational Formula for a Coupled Diagonal Covariance

<a id="statement"></a>

Record kind: project deduction and research-operation record.
Date: 2026-09-13.
Author: indefinite-variation agent.
Goal: [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
The user authorized local and external literature research and removed usage-based stopping for the resumed run.
This is a restricted extension of the mechanism in [Yin_C_F0122](Yin_C_F0122_v1.md), relevant to the indefinite extension of [Yin_C_F0121](Yin_C_F0121_v1.md).
The opening diagonal derivation is retained as an unregistered historical draft.
The later Yin_C_F0125 continuation has its own [scoped self-review](../audits/reviews/Yin_R_F0125_v1.md#positive-covariance-minimax-finding); current assessments are recorded in the [selected assessment](#decision-finding-owned-review).
No mathematical Role is assigned.

## Source Reuse and Scope

The direct inputs are the operator-valued semicircular Dyson equation and determinant primitive in [Yin_C_F0119](Yin_C_F0119_v1.md), the congruence argument and centered action in [Yin_C_F0120](Yin_C_F0120_v1.md), and the [MS24 determinant and scaling audit](../audits/literature/MS24/Yin_U001.md).
The latter includes bounded determinant multiplicativity when a factor is singular, through its [FK52 dependency audit](../ledger/Yin_L_F0036_v1.md).
The new finite-dimensional argument is written below rather than assumed from stationarity.

A search of the local literature audits for variance profiles and quadratic vector equations found no matching variational input.
External primary-source search identified Ajanki, Erdos and Kruger, [Quadratic vector equations on complex upper half-plane](https://arxiv.org/abs/1506.05095), as a relevant attribution lead.
A search result points to a variational formulation numbered (11.8) in the monograph, but the primary PDF/HTML could not be fetched in this pass.
That lead is not an accepted proof dependency or a verified identification of the formula below.
Their [matrix Dyson paper](https://link.springer.com/article/10.1007/s00440-018-0835-z) discusses the diagonal variance-profile reduction, which is background rather than an imported extremum theorem.
No novelty claim is made.

The result covers all real diagonal drifts for the covariance class stated below, including indefinite pencils, spectral bulk and spectral edges.
It does not cover arbitrary diagonal covariance, arbitrary noncommuting drift, or the full signed-Schur class.
In particular it does not complete Yin_T_F0008 or recover every zero-capacity case of MS24.

<a id="coupled-diagonal-minimax"></a>
## Setting and Formula

Let \(s_1,\ldots,s_n\) be freely independent standard semicircular elements in a finite tracial von Neumann algebra \((M,\tau)\).
Let
\[
 S=A+\sum_{j=1}^n b_j\otimes s_j,\qquad
 A=\operatorname{diag}(a_1,\ldots,a_m),\quad a\in\mathbb R^m,
 \qquad b_j=b_j^*\in M_m(\mathbb C),
\]
and use \(\varphi=\operatorname{tr}_m\otimes\tau\), with normalized matrix trace.
Suppose the covariance \(\eta(B)=\sum_jb_jBb_j\) preserves the diagonal algebra, with
\[
 \eta(\operatorname{diag}x)=\operatorname{diag}(Vx).
\]
Assume \(V\) is real symmetric, entrywise nonnegative and positive definite as a quadratic form.
Put \(K=V^{-1}\), and impose the additional condition
\[
 K_{ij}\le0\qquad(i\ne j).                                      \tag{1}
\]
All these are conditions on fixed finite matrices.
Positivity preservation by itself does not imply either positive definiteness of \(V\) or (1).

For free variables \(u\in\mathbb R^m\), \(v\in[0,\infty)^m\), define
\[
 H_a(u,v)=\frac12(a-u)^TK(a-u)-\frac12v^TKv
                  +\frac12\sum_{i=1}^m\log(u_i^2+v_i^2),
 \qquad \log0=-\infty.                                       \tag{2}
\]
Then the proposed result with complete argument below is
\[
 \log\Delta_\varphi(S)
     =\frac1m\min_{u\in\mathbb R^m}\max_{v\in[0,\infty)^m}
           H_a(u,v).                                         \tag{3}
\]
Both successive extrema are attained, and the value is finite.
The inner maximizing vector is unique for each \(u\).
The reduced objective is convex and coercive.
Outer uniqueness at zero regularization is not needed or asserted here.
The order of extrema is part of (3); a raw global saddle property is not asserted.

## Regularization and the Inner Maximum

Set \(d=V\mathbf1\).
Since \(V_{ii}>0\) and \(V_{ij}\ge0\), every \(d_i>0\).
Write \(D=\operatorname{diag}d>0\).
For \(\varepsilon>0\), use the freely evaluated objective
\[
 H_{a,\varepsilon}(u,v)
 =\frac12(a-u)^TK(a-u)
  -\frac12(\varepsilon d-v)^TK(\varepsilon d-v)
  +\frac12\sum_i\log(u_i^2+v_i^2).                            \tag{4}
\]
The cross term in the second quadratic expression is \(\varepsilon\mathbf1^Tv\), because \(Kd=\mathbf1\).
This particular positive diagonal regularization supplies an interior maximum in every imaginary coordinate.

Fix \(u\), and change variables to \(w_i=v_i^2\ge0\).
Apart from terms independent of \(w\), (4) becomes
\[
 -\frac12\sum_iK_{ii}w_i
 -\sum_{i<j}K_{ij}\sqrt{w_iw_j}
 +\varepsilon\sum_i\sqrt{w_i}
 +\frac12\sum_i\log(u_i^2+w_i).                             \tag{5}
\]
This is strictly concave wherever finite: each logarithm is strictly concave in its coordinate; the geometric mean is concave on the nonnegative quadrant; and the coefficients \(-K_{ij}\) and \(\varepsilon\) are nonnegative.
These facts can also be checked by differentiating in the positive orthant and extending by continuity at finite boundary points.

Positive definiteness of \(K\) gives decay to negative infinity as \(\|v\|\to\infty\), uniformly when \(u\) belongs to a compact set and \(0\le\varepsilon\le1\).
For example the quadratic term is at most \(-c\|v\|^2+C\|v\|\), whereas the logarithms grow at most logarithmically.
The logarithmic extension is upper semicontinuous, and \(v=\mathbf1\) gives a finite value.
Thus a maximum exists and is unique, including when \(\varepsilon=0\).

When \(\varepsilon>0\), this maximum has every \(v_i>0\).
If \(u_i=v_i=0\), the value is negative infinity and cannot maximize.
Otherwise, increasing a zero \(v_i\) gives a positive term \(\varepsilon v_i\); the off-diagonal quadratic changes are nonnegative by (1), while the diagonal quadratic and logarithmic changes are of order \(v_i^2\).
The value therefore increases for small positive \(v_i\).

## Positive Reduced Hessian

At the inner optimizer write
\[
 W=\operatorname{diag}\big((u_i^2+v_i^2)^{-1}\big),\qquad
 L=K-W.
\]
The first-order imaginary equation is
\[
 Lv=\varepsilon\mathbf1.                                     \tag{6}
\]
For every real vector \(x\), direct expansion gives
\[
 x^TLx
 =\sum_{i<j}(-K_{ij})v_iv_j
           \left(\frac{x_i}{v_i}-\frac{x_j}{v_j}\right)^2
   +\varepsilon\sum_i\frac{x_i^2}{v_i}>0
       \quad(x\ne0).                                        \tag{7}
\]
Thus \(L>0\); no unproved spectral-radius selection has been inserted into the feasible set.

Put
\[
 B=K-W+2\operatorname{diag}(v_i^2W_{ii}^2)>0,\qquad
 C=-2\operatorname{diag}(u_iv_iW_{ii}^2).
\]
Differentiating (4), evaluated at its inner maximum, gives
\[
 H_{uu}=B,\qquad H_{vv}=-B,\qquad H_{uv}=C.                  \tag{8}
\]
The implicit-function theorem applies because \(H_{vv}\) is invertible.
Hence the maximizing \(v=v_\varepsilon(u)\) is smooth.
For \(F_{a,\varepsilon}(u)=H_{a,\varepsilon}(u,v_\varepsilon(u))\), the chain rule and differentiated imaginary first-order equation give
\[
 \nabla^2F_{a,\varepsilon}=B+CB^{-1}C>0.                     \tag{9}
\]
In particular the reduced objective is strictly convex on all of \(\mathbb R^m\).
Testing \(v=\mathbf1\) gives the uniform lower bound
\[
 F_{a,\varepsilon}(u)
   \ge \frac12(a-u)^TK(a-u)-C_0,
       \qquad 0\le\varepsilon\le1,                          \tag{10}
\]
because every \(\log(u_i^2+1)\ge0\).
It is coercive and has a unique global minimum when \(\varepsilon>0\).

## Identification with the Determinant

At the unique ordered optimizer for positive \(\varepsilon\), both first derivatives vanish.
Set \(z_i=u_i+iv_i\) and \(r_i=z_i^{-1}\).
Combining those two equations gives
\[
 z=a+i\varepsilon d-Vr,\qquad
 \operatorname{diag}(r)^{-1}=A+i\varepsilon D
                                   -\eta(\operatorname{diag}r).
                                                                  \tag{11}
\]
Every \(v_i>0\), so every \(r_i\) has strictly negative imaginary part.
The unique physical solution of (11) is therefore
\[
 R_\varepsilon=(\operatorname{id}\otimes\tau)
                         ((S+i\varepsilon D)^{-1})
              =\operatorname{diag}r.                         \tag{12}
\]
The required existence, equation and uniqueness reduce to Yin_C_F0119 at a scalar spectral parameter by positive congruence: set \(S'=(\varepsilon D)^{-1/2}S(\varepsilon D)^{-1/2}\), transform every coefficient similarly, and apply the usual upper/lower half-plane resolvent equation to \(S'+iI\).
Thus (12) does not require an additional vector Dyson theorem.

The same congruence gives the determinant primitive directly from Yin_C_F0119:
\[
 m\log\Delta_\varphi(S+i\varepsilon D)
  =-\log|\det R_\varepsilon|
       +\frac12\operatorname{Re}\operatorname{Tr}
                    (R_\varepsilon\eta(R_\varepsilon)).      \tag{13}
\]
Indeed the transformed resolvent is \(R'=(\varepsilon D)^{1/2}R_\varepsilon(\varepsilon D)^{1/2}\).
Its log determinant differs by \(\log\det(\varepsilon D)\), exactly canceled by determinant multiplicativity for the two congruence factors.
The quadratic trace is unchanged by cyclicity.
The lower half-plane formula follows from the upper half-plane formula by adjunction for a selfadjoint pencil.

At (11), the quadratic part of (4) is
\[
 \frac12\operatorname{Re}
        (a+i\varepsilon d-z)^TK(a+i\varepsilon d-z)
       =\frac12\operatorname{Re}(r^TVr),                    \tag{14}
\]
where transpose, rather than conjugate transpose, is intentional.
The logarithmic part is \(-\log|\det R_\varepsilon|\).
Equations (13)-(14), after the global extremum proof above, establish
\[
 \log\Delta_\varphi(S+i\varepsilon D)
  =\frac1m\min_u\max_{v\ge0}H_{a,\varepsilon}(u,v).
                                                                  \tag{15}
\]
The Dyson equation is an output identifying the proven global optimizer, not a condition imposed on trial vectors.

## Removing the Regularization

On a compact set of real trial vectors, all maximizing imaginary vectors for \(0\le\varepsilon\le1\) are uniformly bounded by the coercivity estimate preceding (6).
Since
\[
 H_{a,\varepsilon}(u,v)-H_a(u,v)
       =\varepsilon\mathbf1^Tv
           -\frac{\varepsilon^2}{2}\mathbf1^TV\mathbf1,      \tag{16}
\]
the reduced functions converge locally uniformly: \(F_{a,\varepsilon}\to F_{a,0}\).
This comparison uses only points where the logarithmic value is finite; those are sufficient for every maximum.
In particular \(F_{a,0}\) is finite, continuous and convex.
Estimate (10) proves equicoercivity.
A fixed trial \(u=0\) bounds the minima above, so their minimizers remain in a compact set.
Consequently
\[
 \lim_{\varepsilon\downarrow0}\min_uF_{a,\varepsilon}(u)
                      =\min_uF_{a,0}(u).                    \tag{17}
\]
This also proves attainment of the outer minimum in (3).

For the operator limit set \(Y=D^{-1/2}SD^{-1/2}=Y^*\).
Bounded determinant multiplicativity gives
\[
 \log\Delta_\varphi(S+i\varepsilon D)
   =\frac1m\log\det D
        +\frac12\varphi\log(Y^2+\varepsilon^2I)
   \downarrow \log\Delta_\varphi(S).                        \tag{18}
\]
The last equality uses multiplicativity also for the possibly singular \(Y\); this is precisely within the audited bounded FK52 scope.
Equations (15), (17) and (18) prove (3).
Finiteness follows from the finite coercive optimization, rather than from an unproved determinant-class assumption.

## Centered Recovery at the Level of the Variational Formula

When \(a=0\), the convex reduced function \(F_{0,0}\) is even: \(H_0(-u,v)=H_0(u,v)\).
Hence its minimum is at \(u=0\), and (3) simplifies directly to
\[
 m\log\Delta_\varphi(T)
   =\max_{v>0}\left\{\sum_i\log v_i-\frac12v^TKv\right\},
       \qquad T=\sum_jb_j\otimes s_j.                       \tag{19}
\]
The strict positivity restriction on \(v\) loses nothing at \(u=0\), since a zero coordinate makes the objective negative infinity.

The remaining maximum has the exact convex dual identity
\[
 \max_{v>0}\left\{\sum_i\log v_i-\frac12v^TKv\right\}
 =\min_{q>0}\left\{-\sum_i\log q_i+\frac12q^TVq\right\}-m.
                                                                  \tag{20}
\]
For completeness, the right objective is strictly convex and tends to positive infinity at its domain boundary and at infinity, because \(V>0\).
Its unique minimizer \(q\) satisfies \(Vq=q^{-1}\), coordinatewise.
Set \(v=Vq=q^{-1}>0\).
Then \(Kv=q=v^{-1}\), which is the stationary equation for the strictly concave left objective.
Both values are \(-\sum_i\log q_i-m/2\).
This is an optimization duality proved by existence and global convexity; no Dyson balance is assumed before taking extrema.

Let \(Q=\operatorname{diag}q\).
Its equation says \(\eta(Q)=Q^{-1}\), so it is also a critical point of the full matrix action \(J_0(Q)=-\log\det Q+\tfrac12\operatorname{Tr}(Q\eta(Q))\).
The positive-cone path convexity proved in Yin_C_F0120, with the nonnegative linear drift term omitted, makes every such critical point a global minimizer over all positive matrices: the derivative at the initial point of every connecting exponential path is zero and the path is convex.
Thus the diagonal minimum in (20) equals the full positive-matrix infimum, not merely an infimum over diagonal trials.

Yin_C_F0120's already verified comparison with MS24 now gives
\[
 \operatorname{cap}(\eta)
       =\exp\left(2\min_{q>0}
           \{-\sum_i\log q_i+\tfrac12q^TVq\}-m\right),
 \qquad
 \Delta_\varphi(T)=e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)}.
                                                                  \tag{21}
\]
This is an effective zero-drift reduction of the whole variational formula for the present class.
Here the capacity is necessarily positive and the balancing point is attained.
Consequently (21) is not a treatment of MS24's singular, nonattained or zero-capacity cases outside this class.

## A Noncommuting Example and the Remaining Obstruction

Take \(m=2\) and
\[
 b_1=\sqrt2E_{11},\qquad b_2=\sqrt2E_{22},\qquad
 b_3=E_{12}+E_{21}.
\]
The covariance preserves diagonal matrices and has
\[
 V=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
 K=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]
The matrices \(b_j\) do not commute, and the diagonal covariance has rank two, so this is neither the commuting-coefficient case nor the isotropic rank-one covariance case of Yin_C_F0122.
Formula (3) applies to every drift \(A=\operatorname{diag}(a_1,a_2)\), including \(A=\operatorname{diag}(t,-t)\), and all its real spectral translates.

Condition (1) is used substantively twice: to prove concavity after the change to \(v_i^2\), and to prove (7).
Merely deleting it leaves both steps unsupported.
The signed-Schur covariance relevant to arbitrary complex coefficients typically has a bipartite form on diagonal variables and need not even be positive definite as a quadratic form.
Therefore this restricted result supplies a working reduced-Hessian mechanism, but does not itself complete the reduction from indefinite pencils to arbitrary complex affine pencils.
The next useful test is whether a different inner variable or a different order of extrema handles negative covariance directions while preserving the full centered MS24 optimization.

<a id="yin_c_f0125"></a>
<a id="matrix-positive-hs-minimax"></a>
## Continuation: All Matrix Drifts under Positive Hilbert--Schmidt Covariance

Added 2026-09-13, after the user explicitly requested continued independent exploration and ruled out treating the discovered source formula as the final version.
The preceding proof remains a historical restricted derivation.
The argument below removes the commutative invariant-algebra and inverse-sign assumptions, replacing that mechanism by an auxiliary circular Dyson equation and a completely positive stability comparison.
Root has allocated [Yin_C_F0125](#matrix-positive-hs-minimax) for (22)--(29), together with the exact negative-direction boundary below; current assessment is recorded in the [selected assessment](#decision-finding-owned-review), and its [scoped self-review](../audits/reviews/Yin_R_F0125_v1.md#positive-covariance-minimax-finding) has passed.
No mathematical Role is assigned.
This result does not complete the ongoing unrestricted-covariance objective.
Further unrestricted exploration is recorded separately in [the negative-covariance continuation](../ledger/Yin_L_F0030_v1.md).

Let \(S=a+\sum_jb_j\otimes s_j\), where all coefficient matrices are selfadjoint and \(a\) is now arbitrary in \(M_m(\mathbb C)\).
Assume precisely that
\[
 \eta(X)=\sum_jb_jXb_j
 \quad\hbox{is strictly positive as a Hilbert--Schmidt operator}.
                                                               \tag{22}
\]
Complete positivity and Hilbert--Schmidt positivity are separate hypotheses.
The second one means \(\operatorname{Tr}(X^*\eta(X))>0\) for every nonzero matrix \(X\).
Put \(K=\eta^{-1}\).
For freely chosen Hermitian \(U\) and positive semidefinite \(V\), define
\[
 \mathcal H_a(U,V)
  =\tfrac12\operatorname{Tr}((a-U)K(a-U))
    -\tfrac12\operatorname{Tr}(VK(V))
    +\log|\det(U+iV)|.                                      \tag{23}
\]
The value at a singular \(U+iV\) is \(-\infty\).
The proposed exact ordered formula is
\[
 \log\Delta_{\operatorname{tr}_m\otimes\tau}(S)
   =\frac1m\min_{U=U^*}\max_{V\ge0}\mathcal H_a(U,V).         \tag{24}
\]
Both extrema are attained and the value is finite.
The reduced objective in \(U\) is convex and coercive.
No uniqueness assertion at zero regularization is needed.
The noise matrices and the drift need not commute.

### Positive regularization and absence of boundary maxima

Let \(D=\eta(I)>0\).
To verify strict positivity, a vector in the kernel of \(\eta(I)=\sum_jb_j^2\) would be killed by every \(b_j\), and its rank-one projection would be killed by \(\eta\), contradicting (22).
Set
\[
 \mathcal H_{a,\varepsilon}(U,V)
 =\tfrac12\operatorname{Tr}((a-U)K(a-U))
 -\tfrac12\operatorname{Tr}((V-\varepsilon D)K(V-\varepsilon D))
 +\log|\det(U+iV)|,\qquad \varepsilon>0.                    \tag{25}
\]
Since \(K(D)=I\), its difference from (23) is \(\varepsilon\operatorname{Tr}V-\tfrac12\varepsilon^2\operatorname{Tr}D\).

For fixed \(U\), strict Hilbert--Schmidt positivity of \(K\) makes (25) tend to negative infinity as \(\|V\|_2\to\infty\).
The logarithmic term grows at most logarithmically, and its extension at singular matrices is upper semicontinuous.
Testing \(V=I\) gives a finite value, so the maximum exists.
These bounds are uniform for \(U\) in a compact set and \(0\le\varepsilon\le1\).

Every maximizing \(V\) is strictly positive when \(\varepsilon>0\).
Its determinant is nonzero, and write
\[
 R=(U+iV)^{-1}=P-iQ,\qquad Q\ge0.
\]
The gradient of (25) with respect to \(V\) is \(-K(V)+\varepsilon I+Q\).
A maximum on the positive cone satisfies the first-order conditions
\[
 C:=K(V)-\varepsilon I-Q\ge0,\qquad \operatorname{Tr}(CV)=0.
\]
These follow by testing positive directions and both radial directions; they require no concavity assumption.
Applying \(\eta\) gives
\[
 V=\eta(Q)+\varepsilon D+\eta(C)\ge\varepsilon D>0,
\]
which excludes a boundary maximum.
Thus its imaginary stationary equation is
\[
 V=\eta(Q)+\varepsilon D.                                  \tag{26}
\]

### Uniqueness of the inner maximum through a different semicircular model

For fixed \(U\), every interior stationary point satisfying (26) determines
\[
 G=\begin{pmatrix}iQ&P\\P&iQ\end{pmatrix},
 \qquad
 G^{-1}=\begin{pmatrix}-iV&U\\U&-iV\end{pmatrix}.
\]
The inverse identity follows by conjugating the block matrix by the scalar Hadamard unitary: its two resolvent blocks are \((U-iV)^{-1}=R^*\) and \((-U-iV)^{-1}=-R\).
Define
\[
 \Xi\begin{pmatrix}X&Y\\Z&W\end{pmatrix}
       =\begin{pmatrix}\eta(W)&0\\0&\eta(X)\end{pmatrix}.
\]
This map is completely positive and Hilbert--Schmidt selfadjoint.
A selfadjoint Kraus family consists, for each \(b_j\), of the two matrices with off-diagonal entries \(b_j/\sqrt2,b_j/\sqrt2\) and \(ib_j/\sqrt2,-ib_j/\sqrt2\), respectively.
Equation (26) gives
\[
 G^{-1}=
 \begin{pmatrix}0&U\\U&0\end{pmatrix}
 -i\varepsilon\begin{pmatrix}D&0\\0&D\end{pmatrix}
 -\Xi(G),\qquad \operatorname{Im}G>0.                      \tag{27}
\]
This is a physical Dyson equation for an auxiliary selfadjoint matrix semicircular pencil with positive imaginary drift.
Positive congruence reduces it to Yin_C_F0119's scalar-parameter uniqueness argument.
Therefore it has at most one such \(G\).
Since each global inner maximum supplies one, the maximizing \(V=V_\varepsilon(U)\) is unique.
This auxiliary circular hermitization is a mechanism for proving the inner optimization; it is not a constraint imposed on its trial matrices.

### The matrix reduced Hessian

At an inner stationary point, put
\[
 \mathcal S_R(X)=\tfrac12(RXR^*+R^*XR),\qquad
 \mathcal T_R(X)=\operatorname{Re}(RXR)
                  \quad(X=X^*).
\]
Here \(\operatorname{Re}\) means the Hermitian part.
The map \(\mathcal S_R\) is completely positive and Hilbert--Schmidt selfadjoint.
The inverse identities give \(R^*VR=RVR^*=Q\), so
\[
 \eta\mathcal S_R(V)=\eta(Q)=V-\varepsilon D<V.
\]
The positive-definite strict subinvariant vector implies that the spectral radius of the positive map \(\eta\mathcal S_R\) is less than one, by conjugating with \(V^{1/2}\) and using the positive order-unit norm.
The Hilbert--Schmidt operator \(\eta^{1/2}\mathcal S_R\eta^{1/2}\) is selfadjoint and similar to that product.
In this expression \(\eta^{1/2}\) is the Hilbert--Schmidt positive square root; it is not asserted to be completely positive.
Its spectrum is therefore contained in \((-1,1)\), and
\[
 K-\mathcal S_R>0.
\]
Writing \(R=P-iQ\) also gives
\[
 \mathcal S_R-\mathcal T_R=2\mathcal C_Q\ge0
       \quad\hbox{as Hilbert--Schmidt operators}.
\]
Consequently \(B:=K-\mathcal T_R>0\).
Differentiation of (25) on the real Hilbert space of Hermitian matrices gives
\[
 \mathcal H_{UU}=B,\qquad \mathcal H_{VV}=-B,\qquad
 \mathcal H_{UV}=C_R,\quad C_R(X)=\operatorname{Im}(RXR).
\]
The last map is selfadjoint for the real trace pairing by cyclicity.
The implicit-function theorem and uniqueness from (27) show that \(V_\varepsilon(U)\) is smooth.
The reduced objective has Hessian
\[
 B+C_RB^{-1}C_R>0.                                         \tag{28}
\]
It is therefore strictly convex.
Testing \(V=I\) bounds it below by \(\tfrac12\operatorname{Tr}((a-U)K(a-U))-C_0\), uniformly for \(0\le\varepsilon\le1\).
Hence the outer minimum exists and is unique at positive regularization.

### Identification, zero regularization and centered recovery

At the ordered optimizer, the real stationary equation is \(U=a-\eta(P)\).
Together with (26), this says
\[
 R^{-1}=a+i\varepsilon D-\eta(R),\qquad\operatorname{Im}R<0.
\]
Yin_C_F0119, after positive congruence, identifies \(R=E((S+i\varepsilon D)^{-1})\).
Its primitive gives
\[
 m\log\Delta(S+i\varepsilon D)
  =-\log|\det R|+\tfrac12\operatorname{Re}\operatorname{Tr}(R\eta(R)),
\]
which is exactly (25) at the ordered optimizer.
Thus its minimum-maximum is the regularized determinant, with no unproved global-extremum identification.

Uniform inner bounds on compact sets and the explicit difference following (25) give local uniform convergence of the reduced objectives as \(\varepsilon\downarrow0\).
Testing \(V=I\) gives equicoercivity, so minima converge and the limit is convex, finite and attained.
The operator limit is justified by fixed congruence with \(D^{-1/2}\), selfadjoint spectral calculus and bounded determinant multiplicativity, exactly as in (18).
This proves (24).

At \(a=0\), the limiting reduced objective is even in \(U\), so convexity places its minimum at zero.
Formula (24) reduces to
\[
 \max_{V>0}\{\log\det V-\tfrac12\operatorname{Tr}(VK(V))\}
 =\min_{Q>0}\{-\log\det Q+\tfrac12\operatorname{Tr}(Q\eta(Q))\}-m.
                                                               \tag{29}
\]
Both sides have unique extrema by ordinary strict concavity/convexity under (22).
The positive minimizer on the right satisfies \(\eta(Q)=Q^{-1}\); setting \(V=Q^{-1}\) verifies the left stationary equation and equality of values.
Consequently the entire ordered formula reduces to the centered positive action and its capacity form.
Under (22) this capacity is positive and the balance is attained; this is not yet the full unrestricted MS24 boundary.

The earlier diagonal proof is a special case of (24) whenever the full covariance satisfies (22).
Its separate diagonal argument can also apply when only the restriction to the diagonal algebra is positive definite and the full map is not.
Thus the two scopes should not be silently identified.
The proof mechanism now handles arbitrary noncommuting drift under (22), which is the substantive new step.

<a id="negative-hs-minimax-obstruction"></a>
## Exact Obstruction to Deleting Hilbert--Schmidt Positivity

The straightforward extension of (23)--(24) to an arbitrary invertible completely positive Hilbert--Schmidt selfadjoint covariance is false.
Take
\[
 Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 \eta(B)=ZBZ,\qquad a=tX,\quad t>0.
\]
Here \(K=\eta^{-1}=\eta\), but \(K(X)=-X\).
At the permitted real trial \(U=0\), the inner objective in (23) is
\[
 -t^2+\log\det V-\tfrac12\operatorname{Tr}(VZVZ).
\]
For a positive definite \(V\) with real diagonal entries \(\alpha,\delta\),
\[
 \operatorname{Tr}(VZVZ)=(\alpha-\delta)^2+2\det V.
\]
Since \(\log x-x\le-1\), the inner supremum is exactly \(-t^2-1\), achieved at \(V=I\).
Thus the naive normalized minimum-maximum is at most \(-(1+t^2)/2\).

The actual pencil \(S=tX+Z\otimes s\) satisfies
\[
 S^2=(t^2+s^2)I_2,\qquad
 \log\Delta(S)=\tfrac12\tau\log(t^2+s^2)>-\tfrac12.
\]
The inequality follows from the strict pointwise increase over \(\log(s^2)\), whose semicircular integral is \(-1\).
The proposed extension therefore gives a strictly smaller value than the determinant.
This is an exact failure, not just a missing convexity argument.

There is also a visible loss of inner coercivity away from \(U=0\).
For \(U=uX\), \(u\ne0\), take \(V\) diagonal in the \(X\)-basis with eigenvalues \(r,c/r\), \(c>0\).
The quadratic penalty \(\tfrac12\operatorname{Tr}(VZVZ)=c\) remains fixed, while \(\log|\det(U+iV)|\to+\infty\) as \(r\to\infty\).
Thus some inner maxima become infinite in this simplest negative-direction example.

The next unrestricted candidate must change the order, variables or feasible geometry in negative Hilbert--Schmidt directions.
Merely treating complete positivity as sufficient for the present inverse-covariance action is ruled out.
The new benchmark Yin_C_F0124 can test such candidates, but the current user instruction keeps the independent formula search open.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#uniqueness-of-the-inner-maximum-through-a-different-semicircular-model) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0125_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original review classification and limitations: independently reviewed; root route selection disclosed

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#uniqueness-of-the-inner-maximum-through-a-different-semicircular-model) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0125_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:32 |
| status | proved |
| reason | Select the exact retained finding with its actual relationship and original mathematical scope. The statement, argument, status, original review date and historical decisions remain unchanged; no new whole-proof review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#uniqueness-of-the-inner-maximum-through-a-different-semicircular-model) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0125_v1.md#positive-covariance-minimax-finding) | Entire C_F0125 continuation equations (22)-(29) for strictly Hilbert--Schmidt-positive covariance and arbitrary selfadjoint drift, plus the exact negative-covariance obstruction. The preceding coupled-diagonal draft is expressly excluded. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Original review classification and limitations: independently reviewed; root route selection disclosed

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0125_v1.md).

Material covered by that review: [Exact material](Yin_C_F0125_v1.md).
