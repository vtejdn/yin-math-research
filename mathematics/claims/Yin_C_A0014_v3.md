---
author: Yin
---
# Global filter obstruction and local kernel correlation criteria

This revision tests the bounded coefficient-mass route of [C14 v2](Yin_C_A0014_v2.md#bounded-coefficient-mass-suffices-without-norm-convergence) for [A0001](../tasks/Yin_T_A0001_v1.md#contract).
The earlier sufficient conditions remain correct at their fixed scopes.
The new conclusions show that global heat and Euler filters impose an additional Banach spectral property even on inputs already invertible in the regular representation.
They replace that universal target by an exact local-kernel correlation criterion, while explicitly retaining its unresolved estimate.
No concrete group or numerical example is probed, and no general amenable solution is asserted.

## Statement

### Global filter boundedness on invertible inputs

For any discrete group \(G\), let \(A=\ell^1(G)\) with convolution, \(B=\mathbb CG\), and \(C=C_r^*(G)\).
For \(0\ne a\in B\), write \(H=a^*a\) and \(M=\|H\|_C\).
The following are equivalent:

1. \(G\) is [quasi-Hermitian](../audits/literature/SW20/Yin_U001.md#spectral-definitions): every self-adjoint \(x\in B\) has real spectrum in \(A\).
2. For every \(a\in B\cap GL(C)\),
   \[
   \liminf_{n\to\infty}\|(1-H/M)^n\|_A<\infty.
   \tag{1}
   \]
3. For every \(a\in B\cap GL(C)\),
   \[
   \liminf_{t\to\infty}\|e^{-tH}\|_A<\infty.
   \tag{2}
   \]

When the first condition holds, the norms in (1) and (2) actually decay exponentially for each such \(a\).
Conversely, if \(x=x^*\in B\) and \(r+iy\in\sigma_A(x)\) with \(y\ne0\), then for every \(0<\varepsilon<|y|\),
\[
a=x-r-i\varepsilon,\qquad
H=(x-r)^2+\varepsilon^2,\qquad c=y^2-\varepsilon^2>0
\tag{3}
\]
satisfy
\[
H\ge\varepsilon^2I\text{ in }C,\qquad -c\in\sigma_A(H),
\]
and
\[
\|e^{-tH}\|_A\ge e^{ct},\qquad
\|(1-H/M)^n\|_A\ge(1+c/M)^n.
\tag{4}
\]
The corresponding regular operator norms decay exponentially.
In addition, \(c(H+c)^{-1}\), formed in \(C\), does not belong to \(A\).

Thus even a subexponential global-norm requirement would exclude some already-invertible inputs in every non-quasi-Hermitian group.
In particular the obstruction applies to every torsion-free finitely generated elementary amenable group of exponential growth, by the exact [SW20 structural interface](../audits/literature/SW20/Yin_U001.md#elementary-amenable-growth).
This is not a failure of the Atiyah conclusion for those inputs or groups.

### Positive time averaging does not remove a negative Banach spectral point

Suppose \(H\in B\) is positive in \(C\) and \(-c\in\sigma_A(H)\) for some \(c>0\).
Let \(\nu_j\) be probability measures on \([0,\infty)\) such that the Bochner integrals
\[
u_j=\int_0^\infty e^{-tH}\,d\nu_j(t)
\tag{5}
\]
exist in \(A\).
Put \(f_j(x)=\int_0^\infty e^{-tx}\,d\nu_j(t)\).
If \(f_j(x_0)\to0\) for one \(x_0>0\), then
\[
\|u_j\|_A\ge\int_0^\infty e^{ct}\,d\nu_j(t)\longrightarrow\infty.
\tag{6}
\]
Finite positive heat mixtures and actual Bochner Cesaro averages are included.
This assertion does not apply to rational resolvents obtained by analytic continuation when the positive heat integral fails to converge in \(A\).

### Finite-window kernel correlation criterion

Now let \(G\) be finitely generated torsion-free amenable, \(0\ne a\in B\), and \(p=1_{\{0\}}(a^*a)\), \(\alpha=\tau(p)<1\).
Fix a symmetric word metric, write \(B_w\) for its radius-\(w\) ball, choose \(w\) with \(\operatorname{supp}a\subset B_w\), and use the inner boundary
\[
\partial_wF=\{x\in F:B_wx\not\subset F\}.
\]
For finite nonempty \(F\subset G\), define
\[
K_F=\{\xi\in\mathbb C[F]:a\xi=0\},\qquad k_F=\dim_{\mathbb C}K_F.
\]
Let \(Q_F\) be the orthogonal projection onto \(K_F\), as a matrix on \(\mathbb C[F]\).
For any orthonormal basis \(\xi_1,\ldots,\xi_{k_F}\) of \(K_F\), set
\[
b_F=\frac1{|F|}\sum_{i=1}^{k_F}\xi_i\xi_i^*\in B.
\tag{7}
\]
The group-ring multiplication in (7) is convolution, rather than the rank-one matrix product on \(\mathbb C[F]\).
This element is basis independent, and
\[
b_F(g)=\frac1{|F|}
\sum_{\substack{x\in F\\gx\in F}}Q_F(gx,x),\qquad
\operatorname{supp}b_F\subset FF^{-1}.
\tag{8}
\]
It satisfies
\[
ab_F=0,\quad 0\le b_F\le p,\quad
\tau(b_F)=\frac{k_F}{|F|},\quad
\|p-b_F\|_2^2\le\alpha-\frac{k_F}{|F|}
\le\frac{|\partial_wF|}{|F|}.
\tag{9}
\]
The last inequality is the existing complete amenable kernel-localization estimate.

Define the two finite correlation sums
\[
\mathcal C_F=
\frac1{|F|}\sum_{g\in FF^{-1}}
\left|\sum_{\substack{x\in F\\gx\in F}}Q_F(gx,x)\right|
=\|b_F\|_A,
\qquad
\mathcal D_F=\frac1{|F|}\sum_{x,y\in F}|Q_F(y,x)|.
\tag{10}
\]
Then
\[
0\le\mathcal C_F\le\mathcal D_F\le\sqrt{k_F}.
\tag{11}
\]
For any left Følner sequence \((F_j)\), the following are equivalent:
\[
p=0,\qquad
\liminf_j\mathcal C_{F_j}<\infty,\qquad
\liminf_j\mathcal D_{F_j}<\infty.
\tag{12}
\]
If \(p\ne0\), both correlation sums tend to infinity along every such sequence.
Nevertheless, the elementary upper bound in (11) is already sublinear in \(|F|\), so an unspecified sublinear bound is insufficient.

These criteria automatically hold for every injective input, including one with continuous spectrum at zero and one whose global filters have the Banach spectral obstruction (4).
They therefore remove the extraneous all-input quasi-Hermitian requirement.
Equation (12) alone is an equivalent reformulation, not a proof that the required finite correlation bound follows from amenability or torsion-freeness.

There is also an exact norm limitation.
If \(0<\alpha<1\), then for every finite nonempty \(F\),
\[
\|p-b_F\|_{B(\ell^2(G))}=1.
\tag{13}
\]
Thus (9) cannot be upgraded to an operator-norm approximation by these exact kernel averages.

## Current assessment

[Selected decision](#decision-reviewed-global-obstruction)

## Assessment history

### Decision reviewed-global-obstruction

| Field | Value |
| --- | --- |
| date | 2026-11-12T14:00 |
| status | proved |
| reason | The global-filter equivalence, exponential Banach-spectral obstruction, positive-time extension, local correlation criterion and exact norm failure have passed independent review; no uniform correlation estimate or general amenable injectivity theorem is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact v3 statement](#statement) | All equivalences, quantitative bounds, structural class consequences and finite-window assertions under their explicit hypotheses. |
| argument | [Complete v3 argument](#argument) | Spectral mapping, positive-time character estimates, Bessel normalization, kernel localization, coefficient limits and the reduced-algebra projection obstruction. |
| review | [Whole-v3 finding](../audits/reviews/Yin_R_A0044_v1.md#whole-argument) | Independent inspection of the whole fixed statement, argument, necessary direct interfaces and unresolved-scope distinctions. |
| dependency | [SW20 interface](../audits/literature/SW20/Yin_U001.md#sw20-u001) | Definition 1.3, Theorem 4.7(iv) and Corollary 4.11 at their exact finite-support and elementary amenable scopes; substantial source proofs accepted externally. |
| dependency | [Scalar finite-window localization](Yin_C_A0001_v2.md#rational-kernel-localization) | Equation (2) with one input column and no auxiliary state, using the displayed inner-boundary convention. |
| dependency | [Bounded coefficient-mass criterion](Yin_C_A0014_v2.md#bounded-coefficient-mass-suffices-without-norm-convergence) | A bounded coefficient-mass subsequence and L2 convergence identify an actual Banach-algebra kernel projection. |
| dependency | [BCM04 trace interfaces](../audits/literature/BCM04/Yin_U001.md#bcm04-u001) | Scalar Banach-algebra idempotents and the separate reduced-C*-assembly trace range, with no inverse-closedness assumption. |
| dependency | [HK97 assembly interface](../audits/literature/HK97/Yin_U001.md#hk97-u001) | Countable amenable assembly surjectivity used only in the scalar reduced-algebra projection obstruction. |

The fixed [v2](Yin_C_A0014_v2.md#decision-reviewed-bounded-mass) remains correct at its sufficient-condition scope.
This selection rejects its global heat/Euler boundedness condition as a universal target and retains the local correlation estimate as an unresolved geometric input.

## Argument

### Spectral invariance and the shifted-square obstruction

[SW20, Theorem 4.7(iv)](../audits/literature/SW20/Yin_U001.md#finite-support-spectral-invariance) gives
\[
\sigma_A(f)=\sigma_C(f)\qquad(f\in B)
\tag{14}
\]
when \(G\) is quasi-Hermitian.
The finite-support restriction is retained; no assertion about every element of \(A\) is needed.
If \(a\in GL(C)\), then for some \(\delta>0\),
\(\sigma_A(H)=\sigma_C(H)\subset[\delta,M]\).
Polynomial spectral mapping gives
\[
r_A(1-H/M)\le1-\delta/M<1.
\]
The spectral-radius formula implies exponential decay of the powers in \(A\).
Entire-functional-calculus spectral mapping similarly gives
\(r_A(e^{-H})\le e^{-\delta}<1\).
Integer-time exponential decay follows by the same formula.
For \(t=n+s\), \(n\in\mathbb Z_{\ge0}\), \(0\le s<1\), use
\(\|e^{-sH}\|_A\le e^{\|H\|_A}\)
to obtain continuous-time exponential decay.

If quasi-Hermitianity fails, its definition supplies the self-adjoint finite-support \(x\) in (3).
Its regular image is self-adjoint, so \(x-r-i\varepsilon\) is invertible in \(C\) and \(H\ge\varepsilon^2I\).
Polynomial spectral mapping in \(A\) sends \(r+iy\) to \(-c\).
Applying spectral mapping again and bounding spectral radius by Banach norm proves (4).
In \(C\), the spectrum of \(H\) is contained in \([\varepsilon^2,M]\), giving the asserted exponential operator-norm decay.
This proves both reverse implications and the three-way equivalence.

Since \(0\in\sigma_A(H+c)\), this element is not invertible in \(A\).
If the regular element \(c(H+c)^{-1}\) were in \(A\), dividing by \(c\) and using faithfulness of the regular representation would supply a two-sided inverse in \(A\), a contradiction.
The stated elementary amenable class follows directly from [SW20, Corollary 4.11](../audits/literature/SW20/Yin_U001.md#elementary-amenable-growth).
The original interpolation and group-structure proofs remain established external inputs at the recorded source scope.

### Why random positive times retain the obstruction

Let \(A_H\) be the closed unital subalgebra of \(A\) generated by \(H\).
It is a commutative Banach algebra, and \(-c\in\sigma_A(H)\) implies \(-c\in\sigma_{A_H}(H)\).
The standard character description of the spectrum in a unital commutative Banach algebra supplies a character \(\chi\) of norm one with \(\chi(H)=-c\).
Each heat exponential belongs to \(A_H\), and its Bochner integral in (5) remains there.
Applying \(\chi\) under this norm-convergent integral gives
\[
\chi(u_j)=\int e^{ct}\,d\nu_j(t),
\]
which proves the lower bound in (6).
For every fixed \(R>0\),
\[
\nu_j([0,R])\le e^{x_0R}f_j(x_0)\longrightarrow0.
\]
Hence the probability mass escapes every bounded time interval.
The exponential moment is at least \(e^{cR}\nu_j((R,\infty))\).
First letting \(j\to\infty\), and then letting \(R\to\infty\), proves divergence.

For a positive regular \(H\ne0\), any such normalized positive filters converging in \(L^2\) to its kernel projection satisfy \(f_j(M)\to0\).
Indeed monotonicity in \(x\) gives
\[
(1-\alpha)f_j(M)^2
\le\int_{(0,M]}f_j(x)^2\,d\mu_H(x)\longrightarrow0.
\]
Thus the suppression premise is automatic for the intended positive-filter approximation; it is not an unrelated extra demand.
Analytically continued rational functions are excluded from this argument precisely because the asserted \(A\)-valued integral need not exist.

### Positivity, finite propagation and the exact kernel average

Expanding the coefficient of \(g\) in \(\xi_i\xi_i^*\) gives
\[
\sum_x\xi_i(gx)\overline{\xi_i(x)}.
\]
Summing the orthonormal basis yields (8), and also proves basis independence and the support assertion.
Positivity and \(ab_F=0\) follow directly from (7).

For \(\eta\in\ell^2(G)\),
\[
\bigl(\lambda(\xi_i)^*\eta\bigr)(z)
=\sum_{h\in F}\overline{\xi_i(h)}\eta(hz).
\]
For fixed \(z\), Bessel's inequality in \(\mathbb C[F]\) bounds the sum over \(i\) of the squared absolute values by
\(\sum_{h\in F}|\eta(hz)|^2\).
Summing over \(z\) gives
\[
\sum_i\|\lambda(\xi_i)^*\eta\|_2^2
\le |F|\|\eta\|_2^2.
\]
Thus \(b_F\le I\).
Its range is contained in \(\ker a\); self-adjointness gives \(pb_F=b_Fp=b_F\), hence \(0\le b_F\le p\).
The identity coefficient in each \(\xi_i\xi_i^*\) is \(\|\xi_i\|_2^2=1\), proving the trace formula.

Since \(0\le p-b_F\le p\), its square is at most itself.
Therefore
\[
\|p-b_F\|_2^2\le\tau(p-b_F)=\alpha-k_F/|F|.
\]
The final bound in (9) is [C1 v2, equation (2)](Yin_C_A0001_v2.md#rational-kernel-localization), used only at its scalar group-ring specialization.
No affiliated inverse is used to build \(b_F\).

### Correlation bounds and their precise force

The first inequality of (11) is the triangle inequality in the grouped sum (8).
For the second, finite-dimensional Cauchy--Schwarz and the projection identity give
\[
\frac1{|F|}\sum_{x,y\in F}|Q_F(y,x)|
\le\left(\sum_{x,y\in F}|Q_F(y,x)|^2\right)^{1/2}
=\sqrt{\operatorname{Tr}Q_F}=\sqrt{k_F}.
\]
Along a Følner sequence, (9) supplies \(b_{F_j}\to p\) in \(L^2(\tau)\).
A bounded subsequence of \(\mathcal C_{F_j}\) therefore gives \(p\in\ell^1(G)\) by the [bounded-coefficient-mass argument](Yin_C_A0014_v2.md#bounded-coefficient-mass-suffices-without-norm-convergence).
The [BCM04 scalar-idempotent input](../audits/literature/BCM04/Yin_U001.md#amenable-projective-trace) then gives \(p=0\).
A bounded subsequence of \(\mathcal D_{F_j}\) implies the same by (11).
Conversely, if \(p=0\), every \(K_F\) is zero, and both sums vanish identically.
This proves (12) and, by contraposition, divergence when \(p\ne0\).

Finally suppose \(0<\alpha<1\) and \(\|p-b_F\|<1\).
The positive element \(b_F\), supported in the corner \(p\), is then bounded below by a positive multiple of \(p\).
Its spectrum is separated into zero and a compact positive set, so its support projection \(p\) belongs to \(C_r^*(G)\) by continuous functional calculus.
This contradicts the [HK97/BCM04 scalar projection interface](../audits/literature/BCM04/Yin_U001.md#assembly-trace) for torsion-free countable amenable groups.
The opposite bound \(\|p-b_F\|\le1\) follows from \(0\le p-b_F\le p\), proving (13).

## What has and has not been reduced

The global heat or Euler bounded-subsequence target is ruled out as a universal amenable strategy by an exact structural equivalence on already-invertible inputs.
The obstruction concerns extraneous Banach spectrum, and positive random time averaging does not cure it.
The original C14 v2 implications remain valid sufficient conditions, but they cannot be imposed universally.

The local correlation criterion depends on finite kernels with the original equal-label coefficients intact.
It automatically passes all injective inputs and so carries no additional quasi-Hermitian requirement.
However, the equivalence (12) does not itself make the domain problem easier: no uniform correlation bound is derived from amenability and torsion-freeness.
The only automatic bound proved here is (11), which does not suffice.
The exact norm failure (13) identifies another invalid upgrade of complete kernel density.
These are rigorous route restrictions and an explicit remaining geometric estimate, not new Atiyah group-class coverage or a complete solution.
