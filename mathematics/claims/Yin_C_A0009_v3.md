---
author: Yin
---
# Finite joint-word bounds for a trinomial kernel

This argument concerns the actual operator \(T=1+u-v\) in the regular algebra of an arbitrary torsion-free group \(G\), with distinct labels \(e,u,v\).
Write \(K=\ker T\), let \(p\) be its orthogonal projection, and put \(\delta=\tau(p)\).
The question is whether finitely many actual group translates of \(K\), with their full joint multiplication laws, yield a dimension amplification beyond the [coefficient-angle bound](../claims/Yin_C_A0009_v2.md#statement) and [diagonal tensor estimates](../ledger/Yin_L_A0027_v1.md).
The investigation begins from the exact bounded equation \(vp=(1+u)p\), without assuming that \(p\) is rational or that pairwise moment data imply independence.
The [cyclic regular-representation certificate](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) and the [ordered-quotient and normality screen](../ledger/Yin_L_A0021_v1.md) delimit the available prior coverage.

## Statement

The first three translates have an exact dimension collapse: \(K,uK,vK\) are pairwise transverse, but their closed sum has dimension \(2\delta\), not \(3\delta\).
For arbitrary powers, the actual group relation gives the dichotomy \(K\cap u^kK=0\) when \([u^k,v]\ne e\), and \(u^kK=K\) when \([u^k,v]=e\).
Neither conclusion establishes injectivity of a synthesis map with three or more independently chosen translates.

A separate finite joint-word test does improve the numerical bound under an explicit additional hypothesis.
Put \(X=T^*T\) and \(m_j=\tau(X^j)\).
If
\[
 (m_1,m_2,m_3,m_4)=(3,15,87,543),
\tag{M1}
\]
then
\[
 \boxed{\delta<\frac14.}
\tag{M2}
\]
A sufficient finite group hypothesis for (M1) is that no nonempty freely reduced word of length at most eight in the fixed labels \(u^{\pm1},v^{\pm1}\) represents the identity.
This is a hypothesis on the given operator's labels, not permission to replace them by powers or by another generating pair.
More generally, matching the free-word moments through \(m_{2d}\) gives \(\delta\le2/(3d+2)\).
For arbitrary short relations, with the integer \(\Gamma=113(m_2-15)-18(m_3-87)+(m_4-543)\), the exact bound is \(\delta<1/4+\Gamma/256\).
In particular \(\Gamma\le21\) strictly improves the earlier \(1/3\) bound.
The arguments below prove these statements and their exact collision and source scope.
They do not establish the moment hypothesis for every torsion-free group.

<a id="argument"></a>
## The first translate configuration closes at two copies

All operators in this section are bounded elements of \(M=\mathcal N(G)\), acting in the actual regular representation.
The trace is the canonical probability trace, and dimensions of closed right-\(G\)-invariant subspaces are traces of their projections.
The equation \(vp=(1+u)p\) gives
\[
 a=pup,\qquad a+a^*=-p,\qquad pvp=p+a=-a^*.
\tag{T1}
\]
In particular \(a\) is normal in \(pMp\).

Suppose \(\eta\in K\) and \(u\eta\in K\).
Then \(a\eta=u\eta\), so \(\|a\eta\|=\|\eta\|\).
Normality gives \(\|a^*\eta\|=\|\eta\|\), and \(a^*\eta=pu^*\eta\).
Since \(p\) is an orthogonal projection and \(u^*\) is unitary, equality of these norms forces \(u^*\eta\in K\).
Consequently (T1) gives
\[
 (1+u+u^*)\eta=0.
\]
The nonzero cyclic Laurent polynomial \(1+z+z^{-1}\) has only finitely many circle zeros.
The actual regular spectral law of \(u\) therefore forces \(\eta=0\).
Thus
\[
 K\cap uK=0.
\tag{T2}
\]
This proves injectivity of the bounded map \(K\oplus K\to\ell^2(G)\), \((\xi,\eta)\mapsto\xi+u\eta\).
Its polar decomposition gives
\[
 \dim_G\overline{K+uK}=2\delta,
\tag{T3}
\]
without requiring the algebraic sum to be closed or its inverse to be bounded.

The same norm argument applies whenever the compression of a unitary is normal with a fixed scalar real part and the corresponding cyclic polynomial is injective.
Here \(pvp=-a^*\) has real part \(p/2\), and
\[
 p(u^*v)p=p+a^*=-a
\]
also has real part \(p/2\).
Both \(v\) and \(u^{-1}v\) are nonidentity elements of the torsion-free group.
The polynomial \(1-z-z^{-1}\) is nonzero, so the argument proves
\[
 K\cap vK=0,\qquad uK\cap vK=0.
\tag{T4}
\]
Nevertheless \(vK\subset K+uK\) by the original kernel equation.
More precisely, the bounded synthesis map
\[
 F:K^3\longrightarrow\ell^2(G),\qquad
 F(\xi_0,\xi_1,\xi_2)=\xi_0+u\xi_1+v\xi_2
\]
satisfies
\[
 \ker F=\{(-\eta,-\eta,\eta):\eta\in K\}.
\tag{T5}
\]
Indeed \(F(\xi_0,\xi_1,\xi_2)=(\xi_0+\xi_2)+u(\xi_1+\xi_2)\), and (T2) forces both summands to vanish.
Thus its kernel has dimension \(\delta\), and its closed range has dimension \(2\delta\).
The pairwise transversality in (T2)--(T4) supplies no third independent copy in this configuration.
These bounded compression facts already hold under the corresponding relative Haar assumptions, so this first calculation does not extract an additional canonical joint-word restriction.

## A genuine joint-word intersection dichotomy

For any integer \(k\), the translate \(u^kK\) is the kernel of
\[
 u^kTu^{-k}=1+u-u^kvu^{-k}.
\]
If \(\xi\in K\cap u^kK\), subtraction of the two bounded kernel equations gives
\[
 (v-u^kvu^{-k})\xi=0.
\tag{T6}
\]
If \(u^kvu^{-k}\ne v\), this is a nonzero group binomial.
Factoring out \(v\) leaves \(1-w\), where \(w=v^{-1}u^kvu^{-k}\ne e\).
Torsion-freeness makes \(w\) infinite order, so its bilateral-shift regular representation proves the binomial injective.
If \(u^kvu^{-k}=v\), then \(u^k\) commutes with \(T\) and its adjoint, hence preserves the kernel projection.
Consequently
\[
 \boxed{
 K\cap u^kK=
 \begin{cases}
 \{0\},&[u^k,v]\ne e,\\
 K,&[u^k,v]=e,
 \end{cases}
 \qquad
 [u^k,v]=e\Longrightarrow u^kK=K.}
\tag{T7}
\]
Translating (T7) gives the corresponding conclusion for every pair \(u^jK,u^kK\).
This uses an actual mixed group word and its independently certified cyclic binomial, rather than pairwise traces or a rationality assumption on \(p\).
It still does not control the kernel of a synthesis row \((p,up,\ldots,u^{m-1}p)\) with \(m\ge3\).
A proof of its injectivity requires a joint condition on all columns; separate two-column injectivity is insufficient.
The explicit kernel (T5) shows why counting pairwise transverse translates cannot be the missing argument.
No positive-\(\delta\) realization is asserted by that observation.

## A polynomial certificate using four actual moments

Because \(e,u,v\) are distinct, \(\tau(X)=3\).
Let
\[
 q(s)=1-\frac9{16}s+\frac1{16}s^2.
\tag{M3}
\]
Functional calculus gives \(q(X)p=p\), and
\[
 q(X)^2-p=q(X)^2(1-p)\ge0.
\tag{M4}
\]
This is a bounded positive-operator argument.
It follows that
\[
 \delta\le\tau(q(X)^2)
 =1-\frac98m_1+\frac{113}{256}m_2
   -\frac{18}{256}m_3+\frac1{256}m_4.
\tag{M5}
\]
Under (M1), the right-hand side is \(1/4\).

Equality in (M5) is impossible for this particular polynomial in the actual group algebra.
Indeed equality and faithfulness of the trace would imply \(q(X)^2=p\), hence
\[
 q(X)^4=q(X)^2.
\tag{M6}
\]
Both sides of (M6) are elements of the finite-support group algebra \(\mathbb CG\).
The left regular representation is faithful on that algebra, so (M6) would be an algebraic group-ring identity.
The ordinary augmentation \(\varepsilon:\mathbb CG\to\mathbb C\) satisfies \(\varepsilon(T)=1\), \(\varepsilon(X)=1\), and \(q(1)=1/2\).
Applying augmentation to (M6) would give \(1/16=1/4\), a contradiction.
This does not require augmentation to extend continuously to \(\mathcal N(G)\), and it does not assume \(p\) belongs to a rational closure.
Only the equality case would have placed \(p=q(X)^2\) in the finite-support group algebra.
Therefore
\[
 \boxed{\delta<\tau(q(X)^2)}
\tag{M7}
\]
for every such actual-group trinomial, proving the strict form (M2) when (M1) holds.

For arbitrary joint relations define the integer
\[
 \Gamma=
 113(m_2-15)-18(m_3-87)+(m_4-543).
\tag{M8}
\]
Each moment is an integer because \(X\) has integer group-ring coefficients.
Equations (M5)--(M7) give the exact general bound
\[
 \boxed{\delta<\frac14+\frac{\Gamma}{256}.}
\tag{M9}
\]
Thus \(\Gamma\le21\) is a sufficient finite joint-word test for a strict improvement on \(1/3\).
In particular, a hypothetical kernel with \(\delta\ge1/4\) requires \(\Gamma>0\), and one with \(\delta=1/3\) requires \(\Gamma\ge22\).
These are necessary short-word conditions on a hypothetical large kernel, not an assertion that positive \(\Gamma\) produces a kernel.
No upper bound \(\Gamma\le21\), or further collision estimate forcing zero kernel, has been proved from torsion-freeness alone.

## The exact free-word moments and a sufficient collision hypothesis

Let \(F_2=\langle a,b\rangle\), let \(T_0=1+a-b\), and put \(X_0=T_0^*T_0\).
Consider the bounded selfadjoint operator
\[
 B=\begin{pmatrix}0&T_0\\T_0^*&0\end{pmatrix}
\]
on two copies of \(\ell^2(F_2)\).
Its underlying unsigned graph is the bipartite graph with an edge of each label \(e,a,b\) from every vertex to the opposite part.
Contracting the \(e\)-labelled matching edges gives the ordinary Cayley tree of \(F_2\).
Splitting those vertices back along the matching therefore gives a \(3\)-regular tree.
The minus sign on the \(b\)-edges can be removed by assigning vertex signs along unique paths from a chosen root.
Equivalently, every closed walk traverses each tree edge equally often in both directions and has positive sign.
Thus the identity coefficient of \(X_0^j\) is the number of closed walks of length \(2j\) from a root of the \(3\)-regular tree.

The distance from the root follows a Dyck path.
An outward step from the root has three choices, every outward step elsewhere has two, and every inward step has one.
A Dyck path of length \(2j\) with \(r\) excursions from the root therefore contributes \(3^r2^{j-r}\).
For \(j=1,2,3,4\), the numbers of such paths, indexed by \(r=1,\ldots,j\), are respectively
\[
 (1),\quad(1,1),\quad(2,2,1),\quad(5,5,3,1).
\]
The resulting moments are
\[
 3,\quad6+9=15,\quad24+36+27=87,\quad
 120+180+162+81=543.
\tag{M10}
\]
These finite counts were also checked by direct exact free-word multiplication; the displayed walk derivation supplies the mathematical certificate.

Let \(\pi:F_2\to\langle u,v\rangle\) send \(a\) to \(u\) and \(b\) to \(v\).
Every monomial in \(X_0^j\), after free reduction, has word length at most \(2j\).
If no nonempty freely reduced word of length at most eight lies in \(\ker\pi\), then no additional identity coefficient appears for \(j\le4\).
Therefore the actual canonical moments equal (M10), proving (M1).
Moment matching itself is weaker than this sufficient no-collision hypothesis, since signed contributions from additional identity words could cancel.
The correction (M8) records the actual signed moments and does not presume that all relation contributions are positive.

## Arbitrary finite depth: an explicit shrinking conditional bound

Fix an integer \(d\ge1\).
Suppose the actual moments \(m_j\) agree with the free-word moments for \(0\le j\le2d\), where \(m_0=1\).
A sufficient group hypothesis is that no nonempty freely reduced word in the fixed labels of length at most \(4d\) represents the identity.
Then
\[
 \boxed{\delta\le\frac{2}{3d+2}.}
\tag{M11}
\]
Here is a direct construction of the certificate, including its constants.

Let \(f_j\) be the normalized indicator of the sphere of radius \(j\) around the root in the unsigned \(3\)-regular tree.
The sphere sizes are \(1\) and \(3\cdot2^{j-1}\) for \(j\ge1\).
The adjacency operator \(A\) satisfies
\[
 Af_0=\sqrt3\,f_1,\qquad
 Af_1=\sqrt3\,f_0+\sqrt2\,f_2,\qquad
 Af_j=\sqrt2\,f_{j-1}+\sqrt2\,f_{j+1}\quad(j\ge2).
\tag{M12}
\]
Define real polynomials \(r_j\) by \(r_j(A)f_0=f_j\), using these recurrences.
They are orthonormal for the root spectral measure of \(A\), have parity \(j\), and satisfy
\[
 r_0(0)=1,\qquad r_{2j+1}(0)=0,\qquad
 r_{2j}(0)=(-1)^j\sqrt{\frac32}\quad(j\ge1).
\tag{M13}
\]
The first two steps give \(r_1(x)=x/\sqrt3\) and \(r_2(x)=(x^2-3)/\sqrt6\).
Every later even value at zero is the negative of the preceding even value by (M12), proving (M13).

Let \(h_j(s)\) be the polynomial determined by \(h_j(x^2)=r_{2j}(x)\).
The \(h_j\) are orthonormal for the root spectral measure of \(A^2\), which has the moments of \(X_0\).
Put
\[
 \kappa_d=\sum_{j=0}^d h_j(0)^2=1+\frac{3d}{2},
 \qquad
 q_d(s)=\frac{\sum_{j=0}^d h_j(0)h_j(s)}{\kappa_d}.
\tag{M14}
\]
Then \(q_d(0)=1\), \(\deg q_d=d\), and orthonormality gives
\[
 \tau_{F_2}\bigl(q_d(X_0)^2\bigr)=\kappa_d^{-1}.
\tag{M15}
\]
Only moments through order \(2d\) enter this equality.
The assumed moment matching transfers its right-hand side to \(\tau_G(q_d(X)^2)\).
The same bounded positivity argument as (M4) gives (M11).
For \(d=2\), this construction is exactly (M3), and the preceding augmentation argument gives the strict bound \(1/4\).
No strictness assertion for every other \(d\) is needed here.

For completeness, these are the optimal bounds among certificates \(|f(X)|^2\) with \(\deg f\le d\), \(f(0)=1\), and the specified free moments.
If \(f=\sum_{j=0}^d\alpha_jh_j\) and \(f(0)=1\), then Cauchy--Schwarz gives
\[
 1=\left|\sum_{j=0}^d\alpha_jh_j(0)\right|^2
 \le\left(\sum_{j=0}^d|\alpha_j|^2\right)\kappa_d.
\]
Equality is attained by the coefficients of \(q_d\).
This optimality concerns that finite polynomial class, not all possible kernel estimates under those moments.

## Source attribution, known coverage and remaining joint requirement

The polynomial minimization in (M14)--(M15) is the classical Christoffel variational principle.
The checked primary attribution is [Sim08, arXiv:0806.1528v1](../literature/pdf/Sim08--arxiv-v1.pdf), Section 9, Theorem 9.2 and equations (9.6)--(9.7), printed/PDF p. 15.
The source's finite-moment, orthonormal-polynomial hypothesis applies to the compactly supported tree spectral measure used here.
Its statement and short argument were inspected; the displayed recurrence and Cauchy--Schwarz calculation independently supply the needed specialization.
Theorem 9.7, printed/PDF p. 17, also identifies the limiting reciprocal diagonal kernel with the spectral atom.
That comparison explains why using the actual unbounded sequence of moments without an additional estimate would simply retain the original zero-atom question.
No general source audit, historical-priority claim or new random-walk theorem is asserted.

The [ordered-quotient and normality certificates](../ledger/Yin_L_A0021_v1.md) remain stronger whenever their additional hypotheses already give zero kernel.
No such quotient, normality relation, globally free generating pair or known Atiyah class is assumed in (M1) or (M11).
The finite no-collision condition is not asserted to imply any of those global hypotheses, and no explicit example outside every known coverage class has been selected.
If it holds for arbitrarily large \(d\) for the same pair \(u,v\), that pair freely generates its subgroup, so letting \(d\to\infty\) returns the known free-group case.
For a fixed pair with a relation, the available no-collision depth is finite.
Selecting another pair with longer relations does not preserve the kernel of the original \(T\).

The bounded progress is therefore a genuine additional finite joint-word bound, conditional on the explicitly checked moments, together with the exact obstruction (M8)--(M9) when collisions occur.
The translate calculation supplies no universal increasing direct sum.
A continuation must control the weighted collision corrections for the given pair, or prove a genuinely stronger multi-column injectivity statement for actual translated kernel subspaces.
Torsion-freeness certifies the individual binomials in (T6), but supplies neither of those further joint conditions by itself.
The all-group trinomial kernel question and the original all-matrix Task remain unresolved.

## Assessment history

### Decision reviewed-joint-word-bounds

| Field | Value |
| --- | --- |
| date | 2026-11-11T18:44 |
| status | proved |
| reason | Independent whole-artifact review supports the exact translate collapse, actual joint-word intersection dichotomy, strict four-moment bound, finite-depth Christoffel certificates and signed collision corrections at their explicit conditional scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Fixed-label trinomial, all translated-subspace conclusions, four-moment and finite-depth hypotheses, exact signed correction and numerical bounds. |
| argument | [Argument](#argument) | Complete bounded compression, actual binomial inverses, trace and augmentation reasoning, tree recurrence, constants and source limitations. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0028_v2.md#whole-artifact-finding) | Entire fixed statement and argument, exact hypotheses, every formula and source/coverage interface. |

## Current assessment

[Selected decision](#decision-reviewed-joint-word-bounds)

