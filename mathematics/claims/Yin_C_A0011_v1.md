---
author: Yin
---
# Arbitrary coefficient kernels inside normal zero-potential transport

This argument serves [S_A0006](../strategies/Yin_S_A0006.md) under the unchanged [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
It tests whether normal compressed hopping with an actual finite group-ring origin still contains every coefficient-matrix kernel.
The construction below gives the reduction with every inverse independently certified and the singular Gram block handled in the affiliated algebra.
The earlier coefficient-potential investigation is retained separately in [C_A0010 v2](../claims/Yin_C_A0010_v2.md).

## Statement

Let \(H\) be any torsion-free group and let \(A\in M_{r,m}(\mathbb CH)\), with \(r,m\ge1\).
The construction below gives an actual torsion-free group
\[
G=\bigl(H\times\mathbb Z^4\bigr)\rtimes_\sigma\langle t\rangle,
\]
an explicit finite matrix \(M\in M_{m+r,\,2m+r}(\mathbb CN)\), where \(N:=H\times\mathbb Z^4\), and its complete bounded rational kernel projection \(p\).
Writing \(n:=2m+r\), \(B_0:=M^*M\), and
\[
\mathcal H_\varepsilon:=
\begin{pmatrix}
(t+t^{-1}+\varepsilon)I_n&B_0\\
B_0&0
\end{pmatrix}\in M_{2n}(\mathbb CG),
\qquad \varepsilon\in\mathbb R,
\tag{1}
\]
the exact conclusions are
\[
\begin{aligned}
\varepsilon\ne0:\qquad&
P_{\ker\mathcal H_\varepsilon}=\operatorname{diag}(0,p),
&
\dim_G\ker\mathcal H_\varepsilon&=m,\\
\varepsilon=0:\qquad&&
\dim_G\ker\mathcal H_0&=m+\dim_H\ker A.
\end{aligned}
\tag{2}
\]
The compressed hopping \(K:=ptp|_p\) is normal.
Its actual common kernel is an isometric image of \(\ker A\), even though \(\ker M\) itself has the known integer dimension \(m\).
Every matrix supplied as input to (1) is finite over the specified group ring.
Neither \(p\) nor its defect is supplied as an arbitrary measurable input.

Consequently integrality of the zero kernel for this specified zero-potential family, for every torsion-free \(H\) and every rectangular \(A\), is equivalent to the complete all-matrix A0001 assertion.
The equivalence remains true if one additionally requires nonzero normal hopping and noncommutation of \(p\) and \(\sigma(p)\), by the explicit scalar stabilization below.
This is a limitation of the normal-hopping mechanism, not an integer-rank proof or a fractional-kernel example.

All matrix traces are unnormalized.
All unbounded products and inverses mean closed operations in the actual affiliated algebra.
We use the [normal compressed-hopping theorem](../claims/Yin_C_A0008_v1.md#normal-homogeneous-hopping-and-scalar-potentials), the [affiliated saddle reduction](../claims/Yin_C_A0005_v1.md#singular-middle-reduction), and [affiliated unit rank invariance](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) at their stated scopes.
In particular, a bounded Gram inverse on \(1-p\) is not assumed.

<a id="argument"></a>
## Actual group, Fourier denominator and rational unitary

Let \(x_0,x_1,x_2,x_3\) generate the \(\mathbb Z^4\) direct factor of \(N\).
They commute with one another and with every element of \(H\).
Define the automorphism by
\[
\sigma|_H=\mathrm{id},
\qquad
\sigma(x_j)=x_{j+1\pmod4}.
\tag{3}
\]
Its inverse is the reverse permutation, and \(\sigma^4=\mathrm{id}\).
The semidirect product \(G=N\rtimes_\sigma\mathbb Z\) has its actual normal form \(nt^k\), with \(tnt^{-1}=\sigma(n)\).
The direct product \(N\) is torsion-free.
An element of finite order in \(G\) projects trivially to its infinite cyclic quotient, and hence lies in \(N\) and is trivial.
Thus \(G\) is torsion-free without an assumption about any Atiyah property.

Equivalently, \(G\) is the direct product of \(H\) with \(\Gamma:=\mathbb Z^4\rtimes_\sigma\mathbb Z\).
The subgroup \(\mathbb Z^4\times4\mathbb Z\) has index four in \(\Gamma\), so the auxiliary factor is virtually abelian.
This does not put arbitrary \(H\), or its product with this factor, into a newly proved Atiyah class.

Set
\[
f:=x_0-i x_1-x_2+i x_3.
\tag{4}
\]
Under the Fourier identification \(\mathcal N(\mathbb Z^4)=L^\infty(\mathbb T^4)\), this is the multiplier
\[
f(z_0,z_1,z_2,z_3)=z_0-i z_1-z_2+i z_3.
\]
For any fixed three last coordinates, its zero set in the \(z_0\)-circle has at most one point.
Fubini's theorem therefore gives Haar measure zero for the full zero set.
Thus \(f\) and \(f^*\) are injective in the regular representation of \(\mathbb Z^4\).
The subgroup regular-representation decomposition, or directly the product representation of \(N\), preserves this assertion in \(G\).
Finite-trace polar decomposition independently supplies their actual affiliated inverses.
This is the same abelian Fourier denominator mechanism used in [C_A0005 v3](../claims/Yin_C_A0005_v3.md#finite-coefficient-origin-and-the-surviving-finite-orbit-certificate), here with an explicit one-coordinate proof.

Define
\[
w:=f(f^*)^{-1}.
\tag{5}
\]
The affiliated product is the measurable multiplier \(f/\overline f\) off the null zero set.
It has modulus one almost everywhere, so its closed realization is a bounded unitary.
Its inverse is \(f^*f^{-1}=w^*\).
It belongs to the actual rational closure of \(\mathbb CN\) in its affiliated algebra, because the inverses of the finite scalar inputs \(f,f^*\) were independently established.
No formal free-field evaluation is involved.

Direct coefficient comparison gives \(\sigma(f)=if\) and \(\sigma(f^*)=-if^*\).
Uniqueness of the affiliated inverse consequently gives
\[
\sigma(w)=(if)(-if^*)^{-1}=-w,
\qquad
\sigma^2(w)=w.
\tag{6}
\]
The scalar \(w\) commutes with all matrices over \(\mathcal N(H)\).
It need not be a group element, and no regular-word assertion is inferred merely from its unitarity.

## A bounded rational frame from an arbitrary finite matrix

Define
\[
C:=A^*A,\qquad d:=I_m+C,\qquad g:=I_r+AA^*,
\]
\[
R:=(I_m-C)d^{-1},\qquad B:=2Ad^{-1}.
\tag{7}
\]
The positive operators \(d\ge I_m\) and \(g\ge I_r\) have bounded inverses, independently of the kernel of \(A\).
They are actual matrices over the rational closure of \(\mathbb CH\).
The selfadjoint matrices \(C,d,d^{-1},R\) commute with one another.
The ordered identity \(gA=Ad\) implies
\[
g^{-1}A=Ad^{-1}.
\tag{8}
\]
Also
\[
B^*B=4d^{-1}Cd^{-1}=4Cd^{-2},
\]
\[
R^2+B^*B
=\bigl((I_m-C)^2+4C\bigr)d^{-2}
=I_m.
\tag{9}
\]
In particular \(R\) and \(B\) are bounded contractions.
The only inverses used in (7)--(9) are the independently bounded positive inverses of \(d,g\).

The rational normalization in (9) is a classical bounded Cayley mechanism, not a new unitary-conversion principle.
For the selfadjoint finite block
\[
S:=\begin{pmatrix}0&A^*\\A&0\end{pmatrix},
\]
the first block column of \((I+iS)(I-iS)^{-1}\) is \(\binom R{iB}\).
Multiplying its lower block by \(-i\) gives \(\binom R B\).
The bounded Cayley inverse and unitarity argument is exactly the interface already checked in [C_A0006, initial certificates and source scope](../claims/Yin_C_A0006_v1.md#initial-inverse-certificates-and-canonical-trace), with its [Feld18 source comparison](../claims/Yin_C_A0006_v1.md#source-scope-and-remaining-question).
The direct identities above retain all multiplication orders needed here; no unbounded Cayley-domain theorem is used.

Put
\[
F:=\frac1{\sqrt2}
\begin{pmatrix}I_m\\wR\\B\end{pmatrix}
\in M_{n,m}(\mathcal N(N)),
\qquad
p:=FF^*.
\tag{10}
\]
The centrality of \(w\), its unitarity and (9) imply
\[
F^*F=\tfrac12(I_m+R^2+B^*B)=I_m.
\]
Thus \(F\) is a bounded equivariant isometry, \(p\) is its actual range projection, and
\[
(\operatorname{Tr}_n\otimes\tau_N)(p)=m.
\tag{11}
\]
Every entry of \(F\) and \(p\) belongs to the actual rational closure of \(\mathbb CN\).
Their boundedness has been proved separately; boundedness of \((f^*)^{-1}\) is neither true nor needed.

Since \(\sigma\) fixes \(A,R,B\) and sends \(w\) to \(-w\),
\[
F^*\sigma(F)
=\tfrac12(I_m-R^2+B^*B)
=B^*B
=:Q=4C(I_m+C)^{-2}.
\tag{12}
\]
The operator \(Q\) is positive, bounded by the identity and fixed by \(\sigma\).
Its kernel projection is exactly \(e:=P_{\ker_H A}\), transported to the containing regular representation.
Indeed its scalar spectral function is \(4s/(1+s)^2\), whose only zero for \(s\ge0\) is zero.
Equivalently the independently invertible \(d^{-1}\), commuting with \(C\), preserves the zero spectral projection in \(Q=4Cd^{-2}\).
No assertion about the trace arithmetic or rational-closure membership of \(e\) is used.

## Finite group-ring origin of the complete projection

The required finite matrix is
\[
M:=
\begin{pmatrix}
-f(I_m-C)&f^*(I_m+C)&0_{m,r}\\
-2A&0_{r,m}&I_r+AA^*
\end{pmatrix}
\in M_{m+r,n}(\mathbb CN).
\tag{13}
\]
All entries are finite group-ring expressions in the original input \(A\) and the four group generators.
Its first displayed pivot \(f^*d\) is an actual affiliated unit because \(f^*\) is injective and \(d\) is a bounded unit.
The other pivot \(g\) is independently boundedly invertible.
Neither inverse presupposes the kernel of \(A\) or the final transport residual.

For Hilbert-space coordinates \((x,y,z)\), of sizes \(m,m,r\), the second bounded equation of \(M(x,y,z)=0\) gives
\[
z=2g^{-1}Ax=Bx.
\]
The vector \(wRx\) is defined for every \(x\), because \(wR\) is bounded.
Using centrality of \(f,w\) and the commuting coefficient functions in (7), one has the bounded identity
\[
f^*d\,wR=f(I_m-C).
\tag{14}
\]
Therefore the first equation of \(M(x,y,z)=0\) is
\[
f^*d\,(y-wRx)=0.
\]
Injectivity of \(f^*d\) forces \(y=wRx\).
Conversely (14) and (8) show directly that every \((x,wRx,Bx)\) is killed by \(M\).
Hence
\[
\ker M
=\left\{\begin{pmatrix}x\\wRx\\Bx\end{pmatrix}:x\in\ell^2(G)^m\right\}
=\operatorname{ran}F,
\qquad P_{\ker M}=p.
\tag{15}
\]
This argument uses a bounded graph and cancellation of an injective bounded operator; it does not apply \((f^*d)^{-1}\) to an arbitrary Hilbert vector.
The coordinate inverse is bounded, and the known normalization in (10) makes the graph isometric.

Consequently \(B_0=M^*M\) is finite, positive and has the complete kernel projection \(p\).
On \(q:=I_n-p\), its restriction \(b:=B_0|_q\) is an actual affiliated unit by finite-trace polar decomposition.
No bounded inverse of \(b\) is claimed.
The relative inverse of \(B_0\) is used below only in the ambient affiliated algebra, and no additional rational-closure assertion for that relative inverse is required.

The missing bounded inverse is a real feature.
For the allowed input \(A=0\), (13) gives
\[
MM^*=\operatorname{diag}(2|f|^2 I_m,I_r).
\tag{16}
\]
The continuous Fourier polynomial \(f\) vanishes at \((1,1,1,1)\), and neighborhoods of that point have positive Haar measure.
Thus the first block in (16) has no positive lower bound.
The row rank of \(M\) is full in the affiliated algebra by the two independently injective pivots.
The nonzero support parts of \(M^*M\) and \(MM^*\) are unitarily equivalent by polar decomposition.
It follows that \(B_0|_q\) has no bounded inverse in this example.
The bounded Gram premise of C_A0008's explicit star formula, and of C_A0010's bounded finite-matrix consequence, cannot be imported here.

## Normal hopping and its exact coefficient defect

The relation \(tF=\sigma(F)tI_m\) and (12) give
\[
F^*KF=Qt,\qquad
F^*(K+K^*)F=Q(t+t^{-1}).
\tag{17}
\]
Since \(tQ=Qt\), both products of \(Qt\) and its adjoint equal \(Q^2\).
Thus \(K\) is normal.
Its kernel and adjoint kernel coincide, with projection
\[
\delta=FeF^*,
\qquad
(\operatorname{Tr}_n\otimes\tau_G)(\delta)
=(\operatorname{Tr}_m\otimes\tau_H)(e)
=\dim_H\ker A.
\tag{18}
\]
For example, \(\ker(Qt)=t^{-1}\ker Q=\ker Q\), since \(t\) commutes with \(Q\) and its spectral projection.
This verifies the actual kernel identification, not just a rank equality.

The subgroup generated by \(H\) and \(t\) is the actual direct product \(H\times\mathbb Z\).
They commute, and normal form in \(G\) makes \(ht^k=1\) imply \(h=1,k=0\).
Restriction of the regular representation to each subgroup right coset is a copy of its regular representation.
Consequently the canonical trace and kernel dimensions of all coefficient inputs are preserved, and the commuting \(H\)- and height algebras have the canonical tensor-product trace.
There is no imposed abstract joint law.

Let \(T_\varepsilon:=(t+t^{-1}+\varepsilon)I_n\) and let \(R_\varepsilon:=pT_\varepsilon p|_p\).
The normal homogeneous theorem in C_A0008 now applies to this coefficient projection, with no finite-group-ring hypothesis on \(p\).
It yields
\[
P_{\ker R_\varepsilon}
=\begin{cases}
0,&\varepsilon\ne0,\\
\delta,&\varepsilon=0.
\end{cases}
\tag{19}
\]
The same conclusion follows directly from the product spectral calculus for \(Q(t+t^{-1})+\varepsilon I_m\): for each positive coefficient spectral value \(s\), the equation \(2s\cos\theta+\varepsilon=0\) holds on a Haar-null set of height phases.
The coefficient value \(s=0\) contributes exactly when \(\varepsilon=0\).
Both proofs leave the unknown mass of \(e\) unchanged.

## Affiliated saddle elimination without a bounded graph inverse

Decompose each copy of \(\ell^2(G)^n\) as the \(p\)- and \(q\)-ranges.
The lower \(p\)-coordinate of \(\mathcal H_\varepsilon\) is a zero direct summand.
On the remaining ordered coordinates \(p\oplus q\oplus q\), the operator is
\[
\begin{pmatrix}
R_\varepsilon&pT_\varepsilon q&0\\
qT_\varepsilon p&qT_\varepsilon q&b\\
0&b&0
\end{pmatrix}.
\tag{20}
\]
All blocks in this displayed matrix are bounded.
The \(q\oplus q\) saddle block
\[
\mathcal D_\varepsilon:=
\begin{pmatrix}qT_\varepsilon q&b\\b&0\end{pmatrix}
\]
has the independently certified affiliated inverse
\[
\mathcal D_\varepsilon^{-1}
=
\begin{pmatrix}
0&b^{-1}\\
b^{-1}&-b^{-1}(qT_\varepsilon q)b^{-1}
\end{pmatrix}.
\tag{21}
\]
Multiplication in both orders gives the identity of the \(q\oplus q\) corner; no commutation of \(b\) and \(qT_\varepsilon q\) is used.
The inverse's upper-left block is zero, so the Schur correction to \(R_\varepsilon\) is exactly
\[
(pT_\varepsilon q\ \ 0)\,
\mathcal D_\varepsilon^{-1}
\binom{qT_\varepsilon p}{0}=0.
\tag{22}
\]
This is the same support-saddle mechanism as C_A0005, now written at the present amplified sizes.
Its triangular elimination factors are actual affiliated units before the rank of \(R_\varepsilon\) is considered.

Affiliated rank invariance therefore gives
\[
\operatorname{rk}_G\mathcal H_\varepsilon
=2\tau_n(q)+\operatorname{rk}_pR_\varepsilon,
\]
\[
\dim_G\ker\mathcal H_\varepsilon
=[2n-2(n-m)]-\operatorname{rk}_pR_\varepsilon
=m+\dim_p\ker R_\varepsilon,
\tag{23}
\]
where \(\tau_n:=\operatorname{Tr}_n\otimes\tau_G\) and \(\tau_n(p)=m\).
Together with (18)--(19), this proves the dimension assertions in (2).
These are identities for closed affiliated ranks and the kernels of the original bounded matrices.
They do not identify a Hilbert-space kernel by applying the possibly unbounded \(b^{-1}\) to every vector in the residual kernel.
In particular no everywhere-defined zero-potential graph parametrization or bounded graph projection is asserted.

For \(\varepsilon\ne0\), the complete projection nevertheless follows from bounded equations alone.
If \(\mathcal H_\varepsilon(x,y)=0\), the lower equation gives \(x=px\).
Applying \(p\) to the upper equation gives \(R_\varepsilon x=0\), hence \(x=0\) by (19).
The remaining upper equation gives \(B_0y=0\), so \(y=py\).
The converse inclusion is immediate.
This proves the projection in (2), independently of any unrestricted unbounded-vector substitution.
The probability-normalized zero atoms of the \(2n\)-square matrices are respectively \(m/(2n)\) and \((m+\dim_H\ker A)/(2n)\).

## Nonzero hopping and genuine noncommutation can be imposed

The frame has \(\sigma^2(F)=F\), hence \(\sigma^2(p)=p\).
This construction has a projection orbit of period at most two, unlike C_A0008's infinite-orbit star.
A finite orbit alone does not make its projections commute.
Indeed
\[
F^*\sigma(p)F=Q^2.
\tag{24}
\]
If \(p\) commuted with \(\sigma(p)\), then \(p\sigma(p)p\) would be a projection, forcing \(Q^2\) to be a projection.
Since \(Q\ge0\), functional calculus would make \(Q\) itself a projection.
Thus any input for which \(Q\) is not a projection yields \([p,\sigma(p)]\ne0\).

To impose this uniformly without changing the unknown kernel, replace the arbitrary input by
\[
\widetilde A:=\operatorname{diag}(A,2)
\in M_{r+1,m+1}(\mathbb CH).
\tag{25}
\]
Then \(\ker\widetilde A\cong\ker A\), while the added scalar block of \(\widetilde C\) is \(4\), and that of \(\widetilde Q\) is \(16/25\).
Hence \(\widetilde Q\ne0\) and is not a projection.
The resulting hopping is nonzero and normal, and the coefficient projection does not commute with its translate.
Its orbit has period exactly two.
Formula (23) becomes
\[
\dim_G\ker\widetilde{\mathcal H}_0
=(m+1)+\dim_H\ker A.
\tag{26}
\]
This preserves the all-matrix equivalence even within that additional geometric restriction.
The argument is a direct projection-compression test; it uses neither a coefficient division ring nor a presumed integer defect.

## All-matrix equivalence and exact comparison with previous work

Assume first the full A0001 assertion.
The group \(G\) is torsion-free and \(\mathcal H_0\) is an explicit finite matrix over \(\mathbb CG\), so its kernel dimension is an integer.
Conversely, suppose every zero-potential matrix in the specified family has integer kernel dimension.
For an arbitrary torsion-free \(H\) and arbitrary rectangular \(A\), formula (2) then gives
\[
\dim_H\ker A=\dim_G\ker\mathcal H_0-m\in\mathbb Z.
\tag{27}
\]
This is exactly the original all-size contract.
If the normal nonzero/noncommuting restriction is imposed, use (25)--(26) and subtract \(m+1\) instead.
No assertion that every nonzero block is invertible is needed; arbitrary integer partial ranks remain allowed.

| Existing result | Actual retained scope | Present difference |
| --- | --- | --- |
| [C_A0005 v1, singular middle reduction](../claims/Yin_C_A0005_v1.md#singular-middle-reduction) | Affiliated saddle elimination with exact compressed residual and a separate bounded-graph hypothesis. | The same proven elimination applies to the finite Gram block here; it supplies the analytic dimension identity without a bounded inverse. |
| [C_A0005 v1, coupled residual](../claims/Yin_C_A0005_v1.md#coupled-residual-and-energy) | Its displayed two-coordinate family retains an arbitrary selfadjoint scalar coefficient kernel. | The present rectangular input yields the full all-matrix equivalence while retaining normal compressed zero-potential hopping. |
| [C_A0005 v3](../claims/Yin_C_A0005_v3.md#statement) and [v4](../claims/Yin_C_A0005_v4.md#statement) | Finite rational projection origin over torsion-free abelian coefficients, commuting-orbit arithmetic or the rank-two classification over the actual coefficient field. | Here \(H\) is arbitrary; no coefficient-field or division hypothesis is assumed, and period two need not mean commuting translates. |
| [C_A0006](../claims/Yin_C_A0006_v1.md#exact-scope-of-the-obstruction) | An arbitrary coefficient matrix is retained by an actual rational-unitary inverse-difference array and an explicit finite clearing. | This is another all-matrix obstruction, now inside the normal zero-potential transport family; it does not supersede or solve that coefficient obstruction. |
| [C_A0008](../claims/Yin_C_A0008_v1.md#specified-group-and-finite-regular-transport-input) | A finite star with finite group-ring frame and bounded polynomial Gram inverse retains the scalar trinomial kernel, with a noncommuting infinite orbit. | Here an arbitrary matrix kernel is retained, the frame is bounded rational, the input matrix is still finite, the orbit has period at most two, and the Gram inverse can be unbounded. |
| [C_A0010 v2](../claims/Yin_C_A0010_v2.md#statement) | A noncommuting coefficient potential controls the actual defect through its compression, with an independent bounded Gram premise for its Hilbert-space graph formulas. | Nonzero scalar potential removes this residual by C_A0008; zero potential retains the arbitrary coefficient kernel, and (20)--(23) supplies the required affiliated replacement for the bounded Gram step. |

The finite input, bounded rational frame, normality and complete integer trace of \(p\) do not by themselves determine the arithmetic of its common hopping defect.
On that defect the residual \(R_\varepsilon\) is exactly \(\varepsilon\delta\).
If \(\delta\ne0\), the affiliated inverse for nonzero \(\varepsilon\) restricts there to \(\varepsilon^{-1}\delta\), so the family permits a singular zero-parameter limit.
No uniform inverse control or zero-potential injectivity follows from the nonzero-parameter result.

The normal theorem, saddle/rank interfaces, abelian Fourier denominator test and bounded Cayley conversion have been reused at exact local scopes.
The present finite realization, its ordered identities and the strengthened restricted-family equivalence are direct deductions.
No historical novelty or new group-wide Atiyah theorem is claimed.

## Assessment history

### Decision reviewed-normal-kernel-encoding

| Field | Value |
| --- | --- |
| date | 2026-11-11T18:21 |
| status | proved |
| reason | Independent whole-artifact review supports the actual finite realization, domain-correct affiliated saddle reduction and equivalence of the specified normal zero-potential family with the unchanged all-matrix Task. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary rectangular coefficient kernel, all scalar potentials, nonzero normal hopping with noncommuting period-two projections, and both equivalence directions. |
| argument | [Argument](#argument) | Complete finite origin, independently certified inverses, actual group and trace, closed affiliated elimination, singular Gram example, stabilization and source limits. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0035_v1.md#whole-artifact-finding) | Entire fixed statement and argument with exact dependency and comparison scopes. |

## Current assessment

[Selected decision](#decision-reviewed-normal-kernel-encoding)

