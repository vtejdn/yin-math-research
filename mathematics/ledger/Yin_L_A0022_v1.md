---
author: Yin
---
# Central winding, rational matrix projections and a fixed-point parity constraint

Date: 2026-11-12 (Asia/Hong_Kong).
This continuing investigation serves [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [route seven](../strategies/Yin_S_A0007.md).
The fixed input is [the actual central-winding decomposition](../ledger/Yin_L_A0019_v1.md), including its matrix extension and trace normalization.
The scalar adjacency conclusion in that input is not being reproved here.

The matrix question has a positive answer in the calibration case \(G_{2,2}\), by a rational projection specialization that forces an even matrix rank before the trace is divided by two.
This gives an independent matrix constraint without assuming the Atiyah conclusion for that group.
The group is already covered by established results, so this is a mechanism test, not new group-class coverage.
An explicit projection family then shows that finite winding, analyticity, the correct monodromy and the actual quotient trace do not suffice without the rational specialization property.
The extension of that property beyond the virtually cyclic quotient remains unresolved.

## A rational projection lemma

Let \(F=\mathbb C(u,w)\), where \(u,w\) are algebraically independent commuting variables.
Put
\[
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 S_n=I_n\otimes S,\quad D_n=I_n\otimes D.
\]
Suppose \(P\in M_{2n}(F)\) is an idempotent whose evaluations on the two-dimensional torus are orthogonal projections almost everywhere and which satisfies
\[
 P(u,w^{-1})=S_nP(u,w)S_n,
 \qquad
 P(-u,w)=D_nP(u,w)D_n.
 \tag{1}
\]
Then \(\operatorname{rank}_F P\) is even.

First, each entry of \(P\) has no pole along \(w=1\), considered as a rational function of \(w\) over \(\mathbb C(u)\).
Indeed, a pole of order \(k>0\) would give an expression \((w-1)^{-k}h(u,w)\), where \(h\) is regular at \(w=1\) and \(h(u,1)\) is a nonzero rational function of \(u\).
Outside a finite set of \(u\) on the unit circle, specialization preserves the nonzero leading coefficient and produces an actual pole as \(w\) approaches \(1\) on the unit circle.
Fubini's theorem allows such a \(u\) for which the projection bound holds for almost every \(w\).
That bound is \(|P_{ij}(u,w)|\leq1\), which contradicts the pole on an arc of positive measure.
Consequently
\[
 P_0(u):=P(u,1)\in M_{2n}(\mathbb C(u))
\]
is well defined.

Specialization preserves \(P_0^2=P_0\).
Over a field of characteristic zero, the trace of an idempotent equals its rank, so
\[
 \operatorname{rank}_{\mathbb C(u)}P_0
 =\operatorname{Tr}P_0
 =\operatorname{Tr}P
 =\operatorname{rank}_F P.
 \tag{2}
\]
This is preservation of the rank of the projection, not an assertion that the kernel of a specialized original matrix has unchanged dimension.
The latter assertion can fail and is not needed.

The first identity in (1) gives \(P_0S_n=S_nP_0\).
Let \(V_+\) and \(V_-\) be the two \(S_n\)-eigenspaces over \(\mathbb C(u)\), each of dimension \(n\), and let \(r_+,r_-\) be the ranks of the restrictions of \(P_0\) to those spaces.
The second identity in (1), together with \(D_nS_nD_n=-S_n\), identifies the \(u\mapsto-u\) transform of one restriction with the other.
A field automorphism preserves matrix rank, hence \(r_+=r_-\).
Equation (2) now gives
\[
 \operatorname{rank}_F P=2r_+.
 \tag{3}
\]
The proof uses boundedness only to make a rational specialization legitimate; the divisibility comes from the two compatible symmetries at the fixed point.

## The actual matrix model for the torsion-free group \(G_{2,2}\)

Write
\[
 G=\langle a,b\mid a^2=b^2\rangle,\qquad z=a^2=b^2,
 \qquad r=ab^{-1}.
\]
The relations give \(ara^{-1}=r^{-1}\) and \(b=r^{-1}a\), so
\[
 G\cong\langle r,a\mid ara^{-1}=r^{-1}\rangle
   =\mathbb Z\rtimes_{-1}\mathbb Z.
\]
Thus \(G\) is torsion-free and \(\langle r,z\rangle\cong\mathbb Z^2\) has index two.
These normal forms also show that the two commuting variables used below are independent.

For the quotient \(Q=C_2*C_2=\langle s,t\mid s^2=t^2=1\rangle\), set
\[
 T(w)=\begin{pmatrix}0&w^{-1}\\w&0\end{pmatrix}.
\]
Its standard index-two cyclic-subgroup model is
\[
 s\longmapsto S,\qquad t\longmapsto T(w),\qquad
 st\longmapsto\operatorname{diag}(w,w^{-1}).
\]
The trace is one half of the integral of the ordinary matrix trace over \(|w|=1\).
This follows directly on the normal forms \((st)^j\) and \((st)^js\): nonidentity rotations have zero integrated diagonal trace and reflections have zero diagonal trace.
It is therefore the faithful regular trace, not a finite-dimensional character approximation.

The central-winding model becomes
\[
 a\longmapsto uS,\qquad b\longmapsto uT(w),\qquad
 z\longmapsto u^2I_2,
 \tag{4}
\]
with \(u=e^{i\theta/2}\).
Using the full unit circle for \(u\) counts the central parameter twice with equal traces, since \(u\mapsto-u\) is conjugation by \(D\).
Equivalently, the normal forms \(r^ja^k\) verify directly that
\[
 \tau_G(x)=\frac12\int_{\mathbb T^2}\operatorname{Tr}_2(x(u,w))\,du\,dw,
 \qquad x\in\mathbb CG,
 \tag{5}
\]
where both Haar measures have total mass one.
The matrix kernel identity follows either from the matrix extension in L19 or by applying bounded functional calculus to \(A^*A\) and then monotone convergence for its kernel projection.

Let \(A\in M_{m,n}(\mathbb CG)\), and denote its image under (4) by \(\mathcal A\in M_{2m,2n}(\mathbb C[u^{\pm1},w^{\pm1}])\).
Then
\[
 \mathcal A(u,w^{-1})=S_m\mathcal A(u,w)S_n,
 \qquad
 \mathcal A(-u,w)=D_m\mathcal A(u,w)D_n.
 \tag{6}
\]
The first identity is checked on \(S,T(w)\); the second follows because both generators change sign.
They extend to inverses of the group generators and then to every finite group-ring matrix.

## Producing the rational orthogonal kernel projection

On \(F=\mathbb C(u,w)\), use the involution that conjugates complex coefficients and sends \(u,w\) to \(u^{-1},w^{-1}\); combine it with matrix transpose to obtain \(\star\).
Choose a column basis \(V\) over \(F\) for \(\ker_F\mathcal A\), of dimension \(d\).
For \(d=0\) put \(P=0\); otherwise put
\[
 P=V(V^\star V)^{-1}V^\star.
 \tag{7}
\]
The Gram matrix in (7) is invertible over \(F\).
To see this, outside the zero sets of finitely many nonzero Laurent polynomials on \(\mathbb T^2\), the evaluated columns of \(V\) are independent, so their ordinary Hermitian Gram matrix is positive definite.
Such Laurent-polynomial zero sets have measure zero by the one-variable root bound and Fubini's theorem.
Hence the rational Gram determinant is not zero.

The same generic set has \(\operatorname{rank}\mathcal A=2n-d\), and (7) is its actual orthogonal kernel projection there.
In particular, \(P\) has rational entries, satisfies \(P^2=P\), has rank \(d\), and obeys the uniform projection bound on the torus almost everywhere.
The two unitary conjugacies in (6) give the corresponding identities (1) for \(P\) on that generic set.
Equality there is equality of rational functions, so the rational projection lemma applies.
Therefore \(d\) is even, and (5) gives the complete matrix conclusion
\[
 \boxed{\dim_G\ker A=\frac d2\in\mathbb Z.}
 \tag{8}
\]
Every rank, kernel and inverse used in (7) belongs first to a specified commutative rational field; its almost-everywhere evaluation is then compared with the actual regular representation.
No inverse of an unbounded operator is treated as an everywhere-defined pointwise operator.
No prior Atiyah conclusion for \(G\) or arbitrary identification of an abstract division ring with its affiliated closure is used.

## Why finite winding and monodromy alone still fail

The following construction takes place in the actual \(\mathcal N(Q)\) for \(Q=C_2*C_2\).
Let \(\alpha\) be the trace-preserving character automorphism \(\alpha(s)=-s,\alpha(t)=-t\), and set
\[
 p=\frac{1+s}{2},\qquad q=1-p,\qquad x=qtp.
\]
In the preceding cyclic-subgroup matrix model with \(w=e^{i\varphi}\), use the orthonormal vectors
\[
 \xi_+=2^{-1/2}(1,1)^T,\qquad
 \xi_-=2^{-1/2}(1,-1)^T.
\]
Then
\[
 x(\varphi)=-i\sin\varphi\,\xi_-\xi_+^*.
\]
Its polar partial isometry is therefore
\[
 v(\varphi)=-i\operatorname{sgn}(\sin\varphi)\,\xi_-\xi_+^*
\]
almost everywhere, and it satisfies \(v^*v=p\), \(vv^*=q\).
Since \(\alpha(x)=-x^*\), uniqueness of polar decomposition gives \(\alpha(v)=-v^*\).
Consequently
\[
 J=v+v^*,\qquad J^*=J,\quad J^2=1,\quad sJ=-Js,
 \quad\alpha(J)=-J,\quad\tau_Q(J)=0.
\]

Define
\[
 e_\theta=\frac12\left(1+\cos(\theta/2)s+\sin(\theta/2)J\right).
 \tag{9}
\]
The anticommutation identity shows that every \(e_\theta\) is an orthogonal projection, and
\[
 \tau_Q(e_\theta)=\frac12,\qquad
 e_{\theta+2\pi}=\alpha(e_\theta).
 \tag{10}
\]
This is an operator-norm real-analytic family with only the central frequencies \(0,1/2,-1/2\), precisely the monodromy allowed by the actual \(G_{2,2}\) central decomposition.
The selfadjoint family \(1-e_\theta\) has a zero atom of mass \(1/2\) for every \(\theta\).
There is no exceptional parameter set whose removal repairs the proposed integer-rank inference.

These are also genuine bounded affiliated data for \(G\), rather than merely an abstract family of unrelated representations.
Choose a Borel square root \(u(z)\) of the central unitary \(z\) in \(\mathcal N(G)\).
The unitaries \(u(z)^{-1}a\) and \(u(z)^{-1}b\) are selfadjoint involutions and have the quotient fibers \(s,t\).
Apply the bounded polar construction above to them, and use the central real and imaginary parts of \(u(z)\) as the two scalar coefficients in (9).
This constructs the projection with fibers \(e_\theta\) in the actual \(\mathcal N(G)\); its trace is \(1/2\) by L19.

The finite group-ring hypothesis fails in an identifiable way.
In the cyclic-subgroup model,
\[
 J(\varphi)=
 \begin{pmatrix}
 0&-i\operatorname{sgn}(\sin\varphi)\\
 i\operatorname{sgn}(\sin\varphi)&0
 \end{pmatrix}.
 \tag{11}
\]
Every element of the actual rational closure of \(\mathbb CQ\) has entries in \(\mathbb C(w)\) in this model.
Indeed, the initial group algebra has Laurent-polynomial entries, and an ambient-invertible matrix of rational functions has a nonzero rational determinant and a rational inverse by the ordinary adjugate formula after taking the cyclic-subgroup matrix representation.
Thus the rational matrix algebra is closed under all such actual inverses.
A bounded rational function on the circle has only removable possible poles there and hence a continuous extension across them.
The jump in (11) is incompatible with that property, so \(J\) is not in this actual rational closure.
For \(\sin(\theta/2)\ne0\), neither is \(e_\theta\).

More strongly, \(e_\theta\) at such a parameter cannot be the kernel projection of a finite matrix over that rational closure whose domain is one copy of the regular module.
The one-variable version of (7) makes every such kernel projection a matrix of rational functions of \(w\), whereas (11) prevents this for \(e_\theta\).
The jump is exactly the failure of the fixed-point specialization \(w=1\) used in (2), even though the family retains the correct two symmetries away from that fixed point.

## Coverage, source scope and the remaining general matrix obligation

The positive conclusion (8) lies in an established group class: \(G\cong\mathbb Z\rtimes\mathbb Z\) is abelian-by-cyclic.
The applicable existing source coverage is [Lin93, Theorem 1.3 and the induction mechanisms recorded in its audit](../audits/literature/Lin93/Yin_U001.md#routine-lemmas-and-induction).
The norm-equation approach is also already available through [the actual index-two embedding and complete division criterion](../ledger/Yin_L_A0003_v1.md#complete-norm-criterion-and-the-half-rank-witness).
For comparison, its coefficient field here is \(\mathbb C(r,z)\), the involution sends \(r\) to \(r^{-1}\) and fixes \(z\), and the twisting square is \(a^2=z\).
The \(z\)-adic valuation is invariant under this involution, so a putative norm equation \(c\alpha(c)=z\) would imply \(2v_z(c)=1\).
That independently excludes a rational norm solution and gives the same known Atiyah conclusion through the cited actual-closure criterion.
The new investigation isolates a different matrix-level step, namely a removable rational singularity followed by a symmetry-enforced even rank; no priority claim is made for the elementary argument.

The derivation uses L19's actual trace decomposition, elementary Laurent-polynomial zero-set facts, finite-dimensional rational linear algebra, polar decomposition and the cited fixed-ambient index-two facts.
It does not require a generic-parameter theorem for arbitrary finite von Neumann algebras or an extension of the scalar free-additive-atom theorem to matrices.
No such unverified theorem is being used as a substitute for the missing divisibility step.
The AER26 and BBL21 source inputs stay at exactly the scope already recorded in L19; the positive matrix calculation and the negative family above do not strengthen their audited scope.

For \(G_{p,q}\) with a non-virtually-cyclic quotient \(C_p*C_q\), the exact trace disintegration still supplies
\[
 \dim_G\ker A
 =\frac1{2\pi}\int_0^{2\pi}
    (\operatorname{Tr}_n\otimes\tau_{C_p*C_q})
    P_{\ker\rho_\theta(A)}\,d\theta.
\]
The argument above does not supply a faithful finite matrix model over a commutative rational field for those quotient fibers, nor does it prove an appropriate projection specialization or rank-preserving replacement.
Without that input, the fixed-point parity proof does not extend.
Generic constancy of a fiber trace, even if separately established in a chosen family, would only make the displayed average equal to that constant and would not establish its integrality.
The explicit family (9) excludes deriving integrality from that analytic and monodromy information alone.

Even a proposed specialization of all actual rational coefficients at a quotient character is unavailable in general.
For an infinite-order \(g\) sent to \(1\) by the proposed character, \(g-1\) is invertible in the actual affiliated algebra, since its regular kernel is zero on every infinite cyclic coset.
Its rational inverse cannot be mapped by a unital ring homomorphism to an inverse of zero.
The successful argument therefore specializes a bounded rational projection after proving its singularity removable; it does not specialize every rational inverse used to construct that projection.

The next substantive target for this route is a projection-specific replacement for the removable-singularity and symmetry argument in a noncommutative quotient model.
Such a replacement must preserve the actual regular trace, prove its divisibility conclusion independently of Atiyah for the ambient group, and survive every rational inverse introduced by elimination.
The present calculation gives a complete calibration and a concrete obstruction to weakening that requirement; it does not resolve that remaining target or A0001.
