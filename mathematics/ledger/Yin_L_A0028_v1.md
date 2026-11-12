---
author: Yin
---
# Formal lifting of the Promislow rank-two specialized projection

Date: 2026-11-12 (Asia/Hong_Kong).
This continuing development serves [T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [S_A0007](../strategies/Yin_S_A0007.md).
The fixed input is [L_A0024](../ledger/Yin_L_A0024_v1.md), particularly its actual matrices and its distinction between specialized covariance and rational liftability.
The question is whether formal lifting or any finite Taylor-jet condition can distinguish its rank-two projection from a genuine original rational equivariant projection.
The first test completes the coefficient field in the coordinate y at one, takes the formal square root with constant term one, and normalizes the actual left multiplication matrix of b by the corresponding diagonal matrix.
The formal and global arguments below have distinct hypotheses and do not identify formal solvability with rational descent.

The construction below gives a convergent formal rank-two projection satisfying every original covariance and cocycle relation, with every compatible finite jet and actual local torus bounds.
Thus finite-order solvability of those equations cannot repair L_A0024's lost rational liftability.
The explicit lift has nontrivial square-root monodromy and is not rational.
A separate elementary global argument excludes every rational lift that also commutes with the left matrix B, while a formal unitary deformation shows that this extra commutation is not forced by the original equations and initial projection.
No argument below excludes all alternate rational lifts.

## Formal coefficient ring and its actual involutions

Put
\[
 K=\mathbb C(x,z),\qquad t=y-1,\qquad
 R=K[[t]],\qquad \widehat F=K((t)),\qquad y=1+t.
\]
This is the completion of \(K[y^{\pm1}]\) at \(y=1\), followed by its fraction field when needed.
The original rational field \(F=\mathbb C(x,y,z)\) embeds into \(\widehat F\) by Laurent expansion at \(y=1\).
In particular, a rational function with zero Laurent expansion is zero.

For \(c\in K\), write \(c^\#(x,z)=\overline c(x^{-1},z^{-1})\), where the bar conjugates constants.
The original scalar torus involution extends continuously to R by
\[
 \left(\sum_{j\ge0}c_jt^j\right)^*
 =\sum_{j\ge0}c_j^\#\left(\frac{-t}{1+t}\right)^j.
 \tag{1}
\]
This is well defined because \(-t/(1+t)\in tR\), and it is an involution because applying the substitution twice gives t.
Use transpose together with (1) for the matrix operation \(\star\).
The two original parameter automorphisms likewise extend continuously:
\[
 \begin{aligned}
 \sigma_a(x,z,t)&=(x,z^{-1},-t/(1+t)),\\
 \sigma_b(x,z,t)&=(x^{-1},z^{-1},t).
 \end{aligned}
 \tag{2}
\]
They remain commuting involutions and commute with the scalar star operation.
Thus the original right semilinear operators from L_A0024 are defined over R; none of the three original square translations has been set equal to one.

There is a unique series with constant term one satisfying
\[
 s^2=1+t,
 \qquad
 s=\sum_{j\ge0}\binom{1/2}{j}t^j.
 \tag{3}
\]
Existence follows by the binomial multiplication identity, or recursively by equating coefficients.
For uniqueness, the coefficient of degree j in the equation determines \(2s_j\) from lower coefficients.
The same uniqueness gives
\[
 s^*=s^{-1},\qquad \sigma_a(s)=s^{-1},\qquad \sigma_b(s)=s.
 \tag{4}
\]
For example, both \(\sigma_a(s)\) and \(s^{-1}\) have square \(y^{-1}\) and constant term one.
All these statements are formal identities, not an assertion that a rational square root of y has been chosen.

## Exact formal projection and every original symmetry

Use the actual four-coset matrices A, B, \(C_a,C_b\) from [L_A0024, equations (1)--(5)](../ledger/Yin_L_A0024_v1.md#the-actual-left-matrices-and-right-semilinear-symmetries).
Write
\[
 Q=B^2=\operatorname{diag}(y,y^{-1},y,y^{-1}),
 \qquad
 D=\operatorname{diag}(s,s^{-1},s,s^{-1}).
 \tag{5}
\]
The notation D represents the formal extension of the original left coefficient representation to the chosen square root: \(D^2=Q\).
It is not scalar multiplication by s on the four-coset coordinate space.
The matrices D and B commute, since each nonzero entry of B joins two positions carrying the same diagonal entry of D.
Define
\[
 H=D^{-1}B,
 \qquad
 \mathcal E=\frac{I_4+H}{2}.
 \tag{6}
\]
For \(c=x^{-1}z\), the complete formula is
\[
 H=
 \begin{pmatrix}
 0&0&s&0\\
 0&0&0&cs\\
 s^{-1}&0&0&0\\
 0&c^{-1}s^{-1}&0&0
 \end{pmatrix}.
 \tag{7}
\]
Therefore \(H^2=I_4\) and \(\operatorname{Tr}H=0\).
Equation (4) gives \(D^\star=D^{-1}\); the original monomial matrix B satisfies \(B^\star=B^{-1}\).
Since D and B commute,
\[
 H^\star=B^{-1}D=H^{-1}=H,
 \qquad
 \mathcal E^2=\mathcal E=\mathcal E^\star,
 \qquad
 \operatorname{Tr}\mathcal E=2.
 \tag{8}
\]
In particular, its rank over \(\widehat F\) is two.
There is also an explicit R-basis of the positive and negative eigenspaces of H:
\[
 se_1+e_3,\quad cse_2+e_4;
 \qquad
 se_1-e_3,\quad cse_2-e_4.
 \tag{9}
\]
The determinant of these four columns is a unit, since c, s and 2 are units in R.
Thus both image and kernel of \(\mathcal E\) are free R-modules of rank two, not merely modules having the desired generic dimension.
At \(t=0\), s and D become one and the identity respectively, so
\[
 \mathcal E\bmod t=\frac{I_4+B|_{y=1}}2=E_y.
 \tag{10}
\]

For the covariance, let \(U=\operatorname{span}\{e_1,e_3\}\) and \(V=\operatorname{span}\{e_2,e_4\}\).
The matrix \(C_a\) interchanges U and V, whereas \(C_b\) preserves them.
Equations (4)--(5) therefore give, directly entry by entry,
\[
 DC_a=C_a\sigma_a(D),\qquad
 DC_b=C_b\sigma_b(D).
 \tag{11}
\]
The original B satisfies the same covariance equations, and invertible products preserve them.
Consequently
\[
 \mathcal E C_a=C_a\sigma_a(\mathcal E),
 \qquad
 \mathcal E C_b=C_b\sigma_b(\mathcal E).
 \tag{12}
\]
The two identities imply covariance for every group word and inverse with the original semilinear composition order.
The right matrices themselves have not been changed, so their complete original identities still hold in R:
\[
 C_a\sigma_a(C_a)=xI_4,
 \quad C_b\sigma_b(C_b)=yI_4,
 \quad C_{ab}\sigma_{ab}(C_{ab})=zI_4,
 \quad C_{ab}=C_b\sigma_b(C_a).
 \tag{13}
\]
All other cocycle and group relations are likewise the original Laurent identities viewed through the embedding into R.
Thus the formal projection does not gain its rank two by omitting a symmetry, killing a square translation or changing the star operation.

## Convergence and actual local torus bounds

The binomial series in (3), and the corresponding series for \(s^{-1}=(1+t)^{-1/2}\), converge for \(|t|<1\), as follows directly from the ratio of successive coefficients.
Choose \(0<\delta<\log2\) and use the inversion-invariant neighborhood
\[
 W_\delta=\{e^w:|w|<\delta\}
\]
of one in \(\mathbb C^\times\).
Here both y and \(y^{-1}\) lie within the convergence disk around one, and the selected branch is \(s(e^w)=e^{w/2}\).
The formula (7) is holomorphic for \((x,z)\in(\mathbb C^\times)^2\) and \(y\in W_\delta\).
It satisfies all identities (8), (11)--(13) as actual analytic identities on this invariant domain, with star interpreted by its coordinate inversion and conjugation rule.

On the local torus
\[
 |x|=|z|=1,\qquad y=e^{i\theta},\quad |\theta|<\delta,
\]
we have \(s=e^{i\theta/2}\), so D and B are ordinary unitary matrices.
Their commuting quotient H is a unitary involution and therefore Hermitian.
Hence \(\mathcal E\) is an actual orthogonal projection of rank two at every such point, and every entry has modulus at most one.
This supplies an actual analytic realization of the formal series and its local bounds; positivity is not being assigned to an abstract formal coefficient field.

## Every finite jet and the limits of polynomial representatives

For each integer \(N\ge0\), put
\[
 R_N=K[t]/(t^{N+1}),
 \qquad \mathcal E_N=\mathcal E\bmod t^{N+1}.
\]
The maps (1)--(2) preserve \((t^{N+1})\), so star and both automorphisms descend to \(R_N\).
Each original monomial generator matrix and its inverse also descends, since its determinant is a monomial unit.
Therefore (8) and (11)--(13) hold exactly over \(R_N\).
Reducing the explicit basis (9) proves that the image and kernel of \(\mathcal E_N\) are free of rank two over \(R_N\).
The reductions for different N are compatible, and every one is the Taylor jet of the actual local bounded projection just constructed.

The ordinary degree-N polynomial representative is not asserted to be an exact projection away from the formal quotient.
For example, replacing s and its inverse in (7) by \(1+t/2\) and \(1-t/2\) gives an ordinary matrix \(H^{[1]}\) with
\[
 (H^{[1]})^2=(1-t^2/4)I_4,
 \qquad
 (\mathcal E^{[1]})^2-\mathcal E^{[1]}=-t^2I_4/16,
 \quad \mathcal E^{[1]}=(I_4+H^{[1]})/2.
 \tag{14}
\]
Its determinant is \(t^4/256\), so even its ordinary generic rank is four.
This does not contradict the rank-two statement over \(R_1\).
For general N, the ordinary Taylor representative satisfies the projection, star and covariance identities with error \(O(t^{N+1})\).
On the stated local torus its distance in matrix norm from \(\mathcal E\) is uniformly \(O(|t|^{N+1})\) in x and z, because its coefficients contain only the displayed torus-modulus-one monomials.
Its norm is consequently at most \(1+C_N|t|^{N+1}\) near one; exact contractivity or exact selfadjointness of that polynomial representative is not claimed.

The precise obstruction result is therefore that no contradiction can be obtained solely from failure to solve these projection, covariance, star and cocycle equations to some finite order, even when the proposed jets must arise from a locally bounded analytic orthogonal projection.
The system has a compatible solution at every order and an actual local realization.
This statement does not exclude a separate global rationality theorem or a degree-bound restriction using additional information.

## Nonrationality and monodromy of this explicit lift

The entry \(\mathcal E_{13}=s/2\) is not in F.
Indeed, the y-adic valuation of a square in \(K(y)\) is even, while \(v_y(y)=1\); hence no rational function squares to y.
Equivalently, a reduced numerator/denominator equation \(p^2=yq^2\) gives an impossible parity of the multiplicity of y.
Thus there is no rational matrix whose full Laurent expansion is this explicit \(\mathcal E\).

Analytic continuation of the branch s once around zero in the y-plane changes s to \(-s\).
Both s and its inverse change sign in (7), so the continuation changes H to \(-H\) and
\[
 \mathcal E\longmapsto I_4-\mathcal E.
 \tag{15}
\]
These are different projections, as already seen from their nonzero off-diagonal entries.
This is a global obstruction to a single-valued rational continuation of the constructed germ.
It does not prove that every different formal or analytic lift of the same zeroth-order projection has that monodromy.

## A global rational constraint under an additional left commutation

There is an elementary global divisibility conclusion with a precise additional hypothesis.
Let \(n\ge1\), \(B_n=I_n\otimes B\), and \(C_{a,n}=I_n\otimes C_a\).
If \(\Pi\in M_{4n}(F)\) satisfies
\[
 \Pi^2=\Pi,\qquad [\Pi,B_n]=0,\qquad
 \Pi C_{a,n}=C_{a,n}\sigma_a(\Pi),
 \tag{16}
\]
then \(4\mid\operatorname{rank}_F\Pi\).
Neither star nor the second covariance is needed for this restricted statement.

To prove it, split the space into the two eigenspaces of \(B_n^2\):
\[
 U_n=\bigoplus_{j=1}^n\operatorname{span}\{e_{j,1},e_{j,3}\},
 \qquad
 V_n=\bigoplus_{j=1}^n\operatorname{span}\{e_{j,2},e_{j,4}\}.
\]
Their eigenvalues are y and \(y^{-1}\), which are distinct elements of F.
Commutation with \(B_n\) implies commutation with \(B_n^2\), so \(\Pi\) preserves this splitting.
On \(U_n\), the operator \(B_n\) has square y, and \(X^2-y\) is irreducible over F by the preceding valuation argument.
Thus \(U_n\) is a vector space over the quadratic field \(F(\sqrt y)\), with \(\sqrt y\) acting as \(B_n\).
Because \(\Pi\) commutes with this action, its image in \(U_n\) is a vector space over that quadratic field.
Its F-dimension \(d_U\) is therefore even.

The semilinear bijection \(C_{a,n}\sigma_a\) exchanges \(U_n\) and \(V_n\).
The last identity in (16) makes it identify their two image spaces, and a field automorphism preserves dimension.
Hence \(d_V=d_U\), giving \(\operatorname{rank}_F\Pi=d_U+d_V=2d_U\in4\mathbb Z\).
For n equal to one, an idempotent satisfying (16) is consequently either zero or the identity.
In particular, no rational idempotent that also commutes with B can be regular at \(y=1\) and specialize to \(E_y\): its constant integer trace would be zero or four, whereas the specialization has trace two.

This excludes all rational lifts within the B-commuting class, not only the explicit formula (6).
It uses a global irreducibility condition that disappears in the completion, without invoking a norm criterion or a known division theorem for P.
Its additional left-commutation hypothesis is not provided for a kernel projection of an arbitrary original group-ring matrix.
Thus it is a restricted global constraint, not a solution of the general rational liftability or original matrix-divisibility problem.

## The additional commutation is not forced by the local equations

The failure of the extra hypothesis to follow from the local data can itself be witnessed explicitly.
Put
\[
 T=(Q-I_4)A,\qquad K_0=T-T^\star,
 \qquad U_0=\exp(K_0)=\sum_{j\ge0}\frac{K_0^j}{j!}.
 \tag{17}
\]
Since \(Q-I_4\in tM_4(R)\), we have \(K_0\in tM_4(R)\), and the exponential is well defined t-adically.
Both T and its star are actual left group-ring matrices, so \(K_0\) satisfies both original covariances.
The exponential inherits them term by term; its inverse is \(\exp(-K_0)\).
Since \(K_0^\star=-K_0\), we also have \(U_0^\star=U_0^{-1}\).
Consequently
\[
 \widetilde{\mathcal E}=U_0\mathcal E U_0^{-1}
 \tag{18}
\]
is another rank-two formal orthogonal projection satisfying every original covariance and having reduction \(E_y\).
It converges on a local complex neighborhood, and its values are orthogonal projections on the same local torus because \(U_0\) is unitary there.

This projection does not commute with B.
For a direct coefficient check, let \(B_0=B|_{y=1}\) and \(J=\operatorname{diag}(1,-1,1,-1)\).
Since \(Q=I_4+tJ+O(t^2)\), write
\[
 K_0=tK_1+O(t^2),\qquad K_1=JA+A^{-1}J.
\]
The original \(\mathcal E\) commutes with B exactly, so
\[
 [\widetilde{\mathcal E},B]
 =t[[K_1,E_y],B_0]+O(t^2)
 =t(K_1-B_0K_1B_0)+O(t^2).
 \tag{19}
\]
Using the displayed actual matrices, the \((1,2)\) entry of the coefficient in (19) is
\[
 (x-1)(1+z^{-1}),
\]
which is a nonzero element of K.
Thus even the full formal equations, actual local bounds and the prescribed initial projection do not force the commutation needed in (16).
The deformation is not claimed to be rational or to admit a rational continuation.

## Bounded conclusion and unresolved scope

The failed implication is now stronger than a zeroth-order specialization failure.
The original three square translations, full right covariance, exact formal star, free rank two, every compatible finite jet and locally bounded analytic realization all coexist for a lift of \(E_y\).
The explicit germ fails rational descent by a square-root valuation obstruction and complementary monodromy.
The restricted B-commuting global theorem cannot be applied to arbitrary lifts, and the deformation (18) shows that its extra hypothesis is absent even locally.

The retained unresolved question is whether some other rational matrix over F, regular at \(y=1\), satisfies all original projection and covariance conditions and specializes to \(E_y\), without the added left commutation.
Known division coverage for P would exclude such a rank-two rational projection after identifying the appropriate actual crossed-product algebra, but no such conclusion is assumed or re-proved here.
This development establishes a precise failure of formal and finite-jet repair, together with the stated restricted global constraint; it does not establish a general replacement for rational liftability or resolve T_A0001.
