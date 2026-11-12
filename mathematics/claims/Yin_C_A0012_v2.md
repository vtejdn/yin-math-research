---
author: Yin
---
# Generic operator rank and the loss of a singular specialization

Date: 2026-11-12 (Asia/Hong_Kong).
This argument continues the [compatible specialization investigation](../strategies/Yin_S_A0006.md#compatible-central-variable-specialization) under the unchanged [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
It strengthens [C_A0012 v1](../claims/Yin_C_A0012_v1.md#one-variable-specialization-with-an-affiliated-constant-inverse) from generic invertibility to exact generic rank for rectangular matrices.
They also exhibit a family satisfying that certificate whose compatible singular specialization retains the entire unknown kernel of an arbitrary finite input.
The rank argument therefore supplies no kernel-preserving reduction to the certified class.

## Statement

Let \((\mathcal A,\tau)\) be a finite von Neumann algebra with faithful normal finite trace, \(c=\tau(1)\), and unnormalized matrix traces.
For any finite bounded-coefficient rectangular Laurent matrix \(P(z)\) in \(d\ge1\) central unitary variables, its integrated rank equals
\[
\rho=\sup_{w\in\mathbb T^d}\operatorname{rk}_{\tau}P(w),
\]
and this rank is attained at almost every fiber.
For one variable the exceptional set is countable, and if all exponents lie in \([a,b]\), then
\[
\sum_{z\in\mathbb T}\bigl(\rho-\operatorname{rk}_{\tau}P(z)\bigr)\le(b-a)\rho,
\]
where the sum is the supremum over finite subsets.
For a finite matrix rational expression in these variables and bounded coefficients, assume that all inverse gates of its specified syntax are actual affiliated inverses at at least one torus point.
Its integrated and almost-everywhere ranks then equal the supremum over its gatewise-defined fibers, with countable exception in one variable.

These generic conclusions do not control the loss at an arbitrary singular fiber.
For every torsion-free H and every \(A\in M_{m,n}(\mathbb CH)\), the finite construction (12)--(16) below satisfies the compatible-specialization certificate of v1 and has nullity n, whereas its compatible finite \(*\)-specialization \(x\mapsto-1\) has nullity \(n+\dim_H\ker A\).
All these assertions use actual affiliated ranks and the precise finite constructions below; no integrality of an arbitrary generic rank or singular rank loss is asserted.

<a id="argument"></a>

## Inputs and conventions

Let \((\mathcal A,\tau)\) be a finite von Neumann algebra with faithful normal finite trace, and put \(c:=\tau(1)\) and \(\tau_j:=\operatorname{Tr}_j\otimes\tau\).
We use \(L^0(\mathcal A)\) for its algebra of closed densely defined affiliated operators; every product, sum or inverse in that algebra means the closed affiliated operation.
For a rectangular affiliated matrix \(T\) with \(n\) columns, set
\[
\operatorname{rk}_{\tau}T
:=\tau_n(s(T^*T))
=nc-\tau_n(P_{\ker T}),
\]
where \(s(T^*T)\) is its initial support projection.
Polar decomposition identifies this number with the trace of its final support.
The [domain-aware rank interface](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) supplies the product inequalities and invariance under actual affiliated units.

The proof uses the [finite-coefficient specialization theorem](../claims/Yin_C_A0012_v1.md#several-central-variables-and-the-actual-trace), including its validity with an affiliated rather than bounded inverse at the chosen point.
Its one-variable input is the [finite-trace eigenprojection estimate](../audits/literature/MSY23/Yin_U006.md#lemma-519-domain-repair), with the retained bounded-row proof addressing the unbounded-operator domain issue.
The [explicit rational realizations](../claims/Yin_C_A0012_v1.md#rational-expressions-and-explicit-polynomial-schur-realizations) supply the later rational extension.
These existing inputs give the required method; no external novelty or priority assertion is made.

## Exact generic rank for rectangular Laurent matrices

Let \(d\ge1\), and let
\[
P(z)\in M_{m,n}\bigl(\mathcal A[z_1^{\pm1},\ldots,z_d^{\pm1}]\bigr)
\]
have finitely many bounded coefficients.
All evaluations in this section are ordinary evaluations of that specified finite Laurent expression at points of \(\mathbb T^d\).
Define
\[
\rho:=\sup_{w\in\mathbb T^d}\operatorname{rk}_{\tau}P(w).
\]
Then
\[
\operatorname{rk}_{\tau}P(z)=\rho
\quad\text{for Haar-almost every }z\in\mathbb T^d.
\tag{1}
\]
In particular the supremum is attained.
When \(d=1\), the exceptional set in (1) is at most countable.
Under the actual tensor product
\[
\mathcal B:=\mathcal A\,\overline\otimes\,L^\infty(\mathbb T^d),
\qquad \tau_{\mathcal B}:=\tau\otimes\mu,
\]
the corresponding bounded Laurent matrix satisfies
\[
\operatorname{rk}_{\tau_{\mathcal B}}P=\rho,
\qquad
\tau_{\mathcal B,n}(P_{\ker P})=nc-\rho.
\tag{2}
\]
No integrality of \(\rho\) is asserted.

Fix a point \(w\in\mathbb T^d\), and write the rectangular polar decomposition
\[
P(w)=u|P(w)|,
\qquad e:=u^*u\in M_n(\mathcal A).
\]
If \(e=0\), the desired inequality \(\operatorname{rk}_{\tau}P(z)\ge\operatorname{rk}_{\tau}P(w)\) is automatic.
Otherwise \(eM_n(\mathcal A)e\), acting on \(eL^2(\mathcal A,\tau)^n\), is a finite von Neumann algebra with identity \(e\) and restricted trace \(\tau_n|_e\).
Define the square corner-valued Laurent polynomial
\[
Q_w(z):=u^*P(z)e.
\tag{3}
\]
Its coefficients are bounded and both its left and right supports lie under \(e\), since \(u^*=eu^*\).
At the chosen point,
\[
Q_w(w)=|P(w)|\big|_e.
\]
This positive bounded operator has zero kernel and dense range in the corner Hilbert space.
It therefore has an actual affiliated inverse in \(L^0(eM_n(\mathcal A)e)\), even when its spectrum approaches zero.
The inverse acts on its dense range; it is not asserted to act on every vector.

Apply the C_A0012 specialization theorem in this finite corner to \(Q_w(w_1z_1,\ldots,w_dz_d)\), whose value at the auxiliary identity is the just-certified corner unit.
Coordinatewise rotation preserves Haar measure, so \(Q_w(z)\) has full corner rank \(\tau_n(e)\) almost everywhere.
For \(d=1\), the companion proof gives only countably many exceptional points.
The bounded product in (3) and the rank inequality give
\[
\operatorname{rk}_{\tau}P(z)
\ge \operatorname{rk}_{\tau}Q_w(z)
=\tau_n(e)
=\operatorname{rk}_{\tau}P(w)
\tag{4}
\]
on that good set.
The intermediate corner is used only analytically; no coefficient group ring or division algebra is asserted to contain \(e\) or \(u\).

Choose a sequence \((w_j)_{j\ge1}\) with \(\operatorname{rk}_{\tau}P(w_j)\to\rho\).
Intersect the countably many conull sets supplied by (4).
On their intersection the rank is at least \(\rho\), and the definition of \(\rho\) gives the reverse inequality at every point.
This proves (1), including the countable-exception conclusion for one variable.
The case \(\rho=0\) is immediate and requires no nonzero corner.

For completeness, the kernel-dimension function is measurable because
\[
\kappa(z):=\tau_n(P_{\ker P(z)})
=\lim_{a\to\infty}
\tau_n\!\left((I_n+aP(z)^*P(z))^{-1}\right).
\tag{5}
\]
The functions inside the limit are continuous, bounded by \(nc\), and decrease to the displayed kernel trace by bounded spectral calculus.
The same spectral calculus and the normal tensor-product trace give
\[
\tau_{\mathcal B,n}(P_{\ker P})
=\int_{\mathbb T^d}\kappa(z)\,d\mu(z)
=nc-\rho.
\]
This proves (2) without evaluating an arbitrary measurable projection at a point.

The general finite-algebra setting cannot yield integer rank from (1).
For example, with \(\mathcal A:=L^\infty([0,1])\), Lebesgue trace and \(0<\alpha<1\), the constant scalar polynomial \(P(z):=1_{[0,\alpha]}\) has \(\rho=\alpha\).
This example concerns arbitrary bounded coefficients, not a finite group-ring counterexample to A0001.

## A summable bound for one-variable rank losses

For a one-variable Laurent matrix, suppose all exponents lie between integers \(a\le b\), and put \(\ell:=b-a\).
For \(z\in\mathbb T\), define the nonnegative defect
\[
\delta_P(z):=\rho-\operatorname{rk}_{\tau}P(z).
\]
Then, with the sum interpreted as the supremum over finite sets,
\[
\sum_{z\in\mathbb T}\delta_P(z)\le\ell\rho.
\tag{6}
\]
For \(\ell=0\), the matrix is a scalar monomial times a constant matrix, so every defect is zero.

Suppose \(\ell\ge1\) and \(\rho>0\).
Replace \(P(z)\) by the polynomial \(z^{-a}P(z)\), which has the same rank on \(\mathbb T\), and choose a point \(w\) attaining \(\rho\) by (1).
Form its corner compression (3), with corner trace \(\tau_n(e)=\rho\).
Translate \(z=w+y\) and apply the actual affiliated companion construction of [C_A0012](../claims/Yin_C_A0012_v1.md#one-variable-specialization-with-an-affiliated-constant-inverse), padding zero high coefficients if necessary.
The resulting companion \(T\) acts in the \(\ell\)-fold amplification of that finite corner.
For \(y\ne0\), its Schur identity gives
\[
\dim\ker Q_w(w+y)
=\dim\ker(I_{\ell e}-yT)
=\dim\ker(T-y^{-1}I_{\ell e}),
\tag{7}
\]
where the first dimension uses the corner trace and the others use its unnormalized matrix amplification.
At \(y=0\) the kernel is zero.
The rank inequality gives \(\delta_P(z)\le\dim\ker Q_w(z)\).
Distinct points \(z\ne w\) give distinct scalars \((z-w)^{-1}\), so the finite-eigenprojection estimate bounds any finite sum in (7) by \(\ell\rho\).
Taking the supremum proves (6).
The companion coefficients may be unbounded, and (7) is an affiliated Schur-rank identity rather than a claim about applying those coefficients to arbitrary Hilbert-space vectors.

The estimate controls total defect mass, but it provides no positive lower bound or arithmetic restriction on a nonzero individual defect.
In particular it does not turn countability of the exceptional set into absence of exceptional fibers.

## Rational expressions with actual defined inverse gates

Let \(E\) be an \(m\)-by-\(n\) expression built by finitely many compatible sums, products, adjoints and inverses of square subexpressions, starting from bounded-coefficient Laurent matrices.
Let \(\mathcal D\subseteq\mathbb T^d\) consist of points where every inverse gate in this specified syntax is an actual affiliated inverse.
Assume \(\mathcal D\ne\varnothing\).
Then \(\mathcal D\) contains a conull set, the integrated expression is defined in \(M_{m,n}(L^0(\mathcal B))\), and
\[
\operatorname{rk}_{\tau_{\mathcal B}}E
=\sup_{w\in\mathcal D}\operatorname{rk}_{\tau}E(w)
=\operatorname{rk}_{\tau}E(z)
\quad\text{for almost every }z.
\tag{8}
\]
For one variable, the good set in this statement can be chosen with countable complement.

Choose \(w_0\in\mathcal D\), and use the explicit recursion from C_A0012 to write
\[
E=D-CL^{-1}B,
\qquad
J:=\begin{pmatrix}D&C\\B&L\end{pmatrix},
\tag{9}
\]
where every displayed block is a bounded-coefficient Laurent matrix, and \(L\) has size \(k\)-by-\(k\).
The construction makes \(L(w)\) an actual affiliated unit at every \(w\in\mathcal D\), by induction through the same gatewise-defined expression.
In particular \(L(w_0)\) is a unit.
For a polynomial expression the denominator block may be empty, with \(k=0\).

Apply the specialization theorem to the finitely many polynomial denominators in the recursion, after coordinatewise rotation by \(w_0\).
They are actual integrated affiliated units and actual fiber units on a common conull set; in one variable its complement is countable.
On that set every inverse gate of the original expression is defined by the same block identities.
This gives the promised well-defined integrated expression and the conull subset of \(\mathcal D\).

Whenever \(L\) is a unit, ordered affiliated elimination gives
\[
\begin{pmatrix}I_m&-CL^{-1}\\0&I_k\end{pmatrix}
J
\begin{pmatrix}I_n&0\\-L^{-1}B&I_k\end{pmatrix}
=\begin{pmatrix}E&0\\0&L\end{pmatrix}.
\tag{10}
\]
Both outer triangular factors are actual affiliated units of their respective square sizes.
Consequently, in the integrated algebra and at each \(w\in\mathcal D\),
\[
\operatorname{rk}E=\operatorname{rk}J-kc.
\tag{11}
\]
Let \(\rho_J\) be the supremum of the ranks of the polynomial fibers \(J(w)\) over the whole torus.
The polynomial theorem makes the integrated rank and almost every fiber rank of \(J\) equal to \(\rho_J\).
Formula (11) therefore gives generic and integrated rank \(\rho_J-kc\) for \(E\).
It also bounds every defined fiber rank of \(E\) above by that number.
Since a conull set of defined fibers attains it, (8) follows.

All inverse domains are the actual domains of closed affiliated inverses, as in [C_A0012's inverse-field argument](../claims/Yin_C_A0012_v1.md#rational-expressions-and-explicit-polynomial-schur-realizations).
The argument uses the rank of a bounded polynomial block to avoid assuming norm-continuity of an unbounded rational value.
It defines no evaluation homomorphism on all of \(L^0(\mathcal B)\), and it makes no assertion at a point outside the specified expression's defined locus.

## A compatible singular fiber retaining an arbitrary kernel

Let \(H\) be any torsion-free group and let \(A\in M_{m,n}(\mathbb CH)\), with \(m,n\ge1\), be arbitrary.
In this section every group algebra has its canonical group trace, and every matrix trace is unnormalized.
Define
\[
B:=A^*A,\qquad k_A:=P_{\ker A}=P_{\ker B},
\qquad \kappa_A:=\tau_n(k_A).
\]
Set
\[
N:=H\times\langle x\rangle,
\qquad
\sigma|_H:=\mathrm{id},\quad\sigma(x):=x^{-1},
\qquad
G:=N\rtimes_\sigma\langle t\rangle.
\tag{12}
\]
Here \(\langle x\rangle\cong\langle t\rangle\cong\mathbb Z\), and the defining relation is \(txt^{-1}=x^{-1}\).
The group \(G\) is torsion-free: a finite-order element has zero height in the infinite cyclic quotient, and then belongs to the torsion-free subgroup \(N\).

Define the finite matrices
\[
C(x):=B+(1+x)I_n,
\qquad
M(x):=\bigl(C(x)\ \ 0_{n,n}\bigr)
\in M_{n,2n}(\mathbb CN).
\tag{13}
\]
At the auxiliary identity,
\[
M(1)M(1)^*=(B+2I_n)^2\ge4I_n.
\tag{14}
\]
Thus the bounded Gram hypothesis of C_A0012 holds for every input \(A\), with no knowledge of \(\kappa_A\).
The group action fixes \(H\) and acts on the central auxiliary generator by an element of \(GL_1(\mathbb Z)\), exactly as required there.

For \(z\in\mathbb T\setminus\{-1\}\), the normal operator \(C(z)=B+(1+z)I_n\) is boundedly invertible.
Indeed \(\operatorname{spec}(B)\subseteq[0,\|B\|]\), and the equation \(\lambda+1+z=0\), with \(\lambda\ge0\) and \(|z|=1\), forces \(\lambda=0\) and \(z=-1\).
For each fixed \(z\ne-1\), compactness of \(\operatorname{spec}(B)\) supplies a positive distance from zero.
It follows that the actual integrated kernel projection of \(M\) is
\[
p:=P_{\ker M}=\begin{pmatrix}0_n&0\\0&I_n\end{pmatrix}.
\tag{15}
\]
In particular \(\sigma(p)=p\), the hopping \(ptp|_p\) is a corner unitary, and the overlap matrix \(p\sigma(p)p+(I_{2n}-p)\) is exactly \(I_{2n}\).
No arbitrary measurable projection has been substituted into the finite input.

Put
\[
D:=M^*M,
\qquad
\mathcal H:=
\begin{pmatrix}(t+t^{-1})I_{2n}&D\\D&0\end{pmatrix}
\in M_{4n}(\mathbb CG).
\tag{16}
\]
C_A0012 applies with \(r=n\) and column count \(2n\), and gives
\[
P_{\ker\mathcal H}=\operatorname{diag}(0_{2n},p),
\qquad \dim_G\ker\mathcal H=n.
\tag{17}
\]
This conclusion is independent of the unknown \(\kappa_A\).

Now use the finite group-ring \(*\)-homomorphism
\[
\epsilon_-:\mathbb CG\longrightarrow\mathbb C[H\times\langle t\rangle],
\qquad h\mapsto h,\quad x\mapsto-1,\quad t\mapsto t.
\tag{18}
\]
It respects the relation in (12), since both \(x\) and \(x^{-1}\) map to \(-1\), and \(t\) commutes with \(H\) in both algebras.
It preserves the involution because \(-1\) is unitary.
It is a coefficient specialization, not an asserted group homomorphism sending \(x\) to a group element.
The auxiliary point \(-1\) is fixed by inversion, so this specialization is compatible with the actual action.

Write \(M_-:=\epsilon_-(M)=(B\ \ 0)\), \(D_-:=M_-^*M_-=\operatorname{diag}(B^2,0_n)\), and \(\mathcal H_-:=\epsilon_-(\mathcal H)\).
The complete kernel projection of \(M_-\) and \(D_-\) is
\[
p_-:=\operatorname{diag}(k_A,I_n),
\qquad \tau_{2n}(p_-)=n+\kappa_A.
\tag{19}
\]
This projection is a separately calculated kernel projection of the specialized bounded matrix; it is not obtained by evaluating the rational formula for \(p\) at an undefined inverse gate.

Let \(s:=t+t^{-1}\) on \(\ell^2(H\times\langle t\rangle)\).
Its central circle multiplier is \(2\cos\theta\), whose zero set has Haar measure zero, so \(s\) is injective.
It commutes with \(p_-\).
If \(\mathcal H_-(\xi,\eta)=0\), the lower bounded equation gives \(D_-\xi=0\), hence \(\xi=p_-\xi\).
Compressing the upper equation by \(p_-\) then gives \(s\xi=0\), hence \(\xi=0\).
The remaining upper equation is \(D_-\eta=0\).
The converse inclusion is immediate from the same bounded equations, so
\[
P_{\ker\mathcal H_-}=\operatorname{diag}(0_{2n},p_-),
\qquad
\dim_{H\times\langle t\rangle}\ker\mathcal H_-
=n+\kappa_A.
\tag{20}
\]
Subgroup trace preservation identifies \(\kappa_A\) here with the original \(H\)-kernel dimension.
The calculation uses no inverse of \(B\) or of its nonzero support part.

When \(k_A\ne0\), the row Gram at \(-1\) is \(B^2\) and has a nonzero kernel, so the inverse gate in
\[
I_{2n}-M^*(MM^*)^{-1}M
\tag{21}
\]
is undefined at that point.
On the invariant subspace \(k_A\), the good-fiber inverse of \(C(z)\) is \((1+z)^{-1}k_A\), so there is no uniform bound as \(z\to-1\).
Although the integrated expression (21) equals the constant matrix (15), evaluating that constant expression at \(-1\) produces \(p\), not the larger projection \(p_-\) in (19).
There is no contradiction: equality in the integrated affiliated algebra is equality modulo Haar-null fibers, and the kernel formula (21) has lost its defining inverse at the exceptional point.
In particular no value of an arbitrary \(L^\infty\) class, and no extension of (18) to the whole affiliated algebra, is used.

## Consequence and remaining reduction

For any polynomial family in (1), an original fiber \(w\) obeys the exact numerical identity
\[
\tau_n(P_{\ker P(w)})
=nc-\rho+\bigl(\rho-\operatorname{rk}_{\tau}P(w)\bigr).
\tag{22}
\]
The generic theorem determines the first term and leaves the nonnegative rank-loss term.
In (13), that loss at \(-1\) is exactly \(\kappa_A\), and the same unknown is exactly the full-matrix nullity increase from (17) to (20).
Thus even an independently bounded identity-specialization Gram, a compatible singular evaluation, constant generic kernel projection and vanishing generic hopping defects do not determine the arithmetic of the singular fiber.

This complements [C_A0011's all-matrix obstruction](../claims/Yin_C_A0011_v1.md#all-matrix-equivalence-and-exact-comparison-with-previous-work): that construction retains the arbitrary kernel in the actual zero-potential residual, whereas this construction places it entirely in the lost specialization defect of an otherwise certified family.
Neither finding refutes A0001.
The present obstruction excludes the inference from the stated generic certificate to equality of a singular fiber's kernel dimension; it does not exclude every possible reduction using additional structure.

A successful continuation would need an independently established rank-loss identity or a transformation preserving the original kernel dimension up to a known integer while producing a C_A0012-compatible input.
If the transformation is based on specializing a regularized family, it must control the actual defect in (22), rather than only the generic rank or the values of a simplified rational representative.
No such additional comparison is established here.

## Assessment history

### Decision reviewed-generic-rank

| Field | Value |
| --- | --- |
| date | 2026-11-11T19:19 |
| status | proved |
| reason | Independent whole-proof review verifies exact generic rank and its one-variable total-defect bound, syntax-specific rational specialization, and the finite compatible singular fiber that retains an arbitrary original kernel. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact polynomial and rational generic rank, summable one-variable rank loss, and the arbitrary-input finite singular-specialization obstruction. |
| argument | [Argument](#argument) | Complete finite-corner, companion, Schur, trace and bounded-kernel calculations, degenerate cases, source interfaces and limitations. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_A0038_v2.md#whole-proof-finding) | Entire fixed statement and argument, actual affiliated domains and exact finite specialization. |

## Current assessment

[Selected decision](#decision-reviewed-generic-rank)

