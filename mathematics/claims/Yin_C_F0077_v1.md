---
author: Yin
---
# Weighted partial liberation contractions from uniformly square-integrable kernel rows

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(M\) be a finite von Neumann algebra with a faithful normal probability trace \(\tau\), \(H=L^2(M,\tau)\), and \(N=W^*(Z)\), where \(Z\in M\) is bounded and normal.
Write \(K=\sigma(Z)\) and \(\mu\) for its spectral law.
Let \(\mathcal B\subseteq M\) be a unital star algebra such that
\[
 \mathcal A=\operatorname{alg}(\mathbb C[Z,Z^*],\mathcal B)
\]
is weakly dense in \(M\).
Assume the partial liberation derivation is well defined on this represented algebra:
\[
 \gamma(n)=n\otimes1-1\otimes n
 \quad(n\in\mathbb C[Z,Z^*]),\qquad \gamma(b)=0\quad(b\in\mathcal B).
\]
Assume that the actual Hilbert adjoint of the real outer derivation \(\beta=\mathrm i\gamma\) has \(1\otimes1\) in its domain, and put \(\zeta=\beta^*(1\otimes1)=\zeta^*\).
No freeness of \(N\) and \(\mathcal B\) is assumed.
Inner products are linear in the second variable, and \(\rho(a)p=pa\).

Let \(\nu\) be the joint spectral measure of \(\zeta\) for left and right multiplication by \(Z\).
Then \(\nu\ll\mu^2\).
The graph closure of the restriction of \(\beta^*\) to marginal polynomial tensors has domain exactly
\[
 L^2(\mu^2)\cap L^2(\nu)
\]
and action (S1) below.
This assertion concerns that graph closure, not an unproved identification with the entire marginal intersection of \(\operatorname{Dom}\beta^*\).

Suppose \(g\) is a real symmetric kernel such that
\[
 g\in L^2(\mu^2)\cap L^2(\nu),\qquad
 m=\mathop{\rm ess\,sup}_{z\sim\mu}
 \left(\int|g(z,v)|^2d\mu(v)\right)^{1/2}<\infty.
 \tag{1}
\]
For \(p\in\mathcal A\), define
\[
 \beta_g(p)=\mathrm i I_g\gamma(p),\qquad
 I_g(a\otimes b)=a g b,\qquad
 E_{g,0}p=(\mathrm{id}\otimes\tau)\beta_g(p).
\]
The insertion is evaluated on the finite algebraic expansion of \(\gamma(p)\); it is not required to be bounded on the whole coarse correspondence.

Then \(\beta_g\) is a well-defined closable real derivation with actual vacuum \(\eta_g=\beta^*g=S_g\zeta\), where \(S_g\) is the left/right spectral action on \(H\).
The contraction \(E_{g,0}\) is closable, \(\mathcal A\subseteq\operatorname{Dom}E_{g,0}^*\), and
\[
 M\Omega\subseteq\operatorname{Dom}\overline{E_{g,0}}
                  \cap\operatorname{Dom}E_{g,0}^*.
 \tag{2}
\]
Explicit bounds are (B2)--(B3) below.
Thus these are the original canonical closure and actual adjoint, not independently chosen extensions.

The final section supplies an abstract absolutely continuous symmetric spectral weight and a real symmetric Hilbert kernel \(g\) with \(\|T_g\|<1\) and \(g\in L^2(\nu)\), but \(g\circ g\notin L^2(\nu)\).
Its row-square-integrability is not uniform.
No realization of that abstract weight as a liberation-vacuum measure is claimed; it is only an obstruction to deducing the requisite kernel iteration from the weighted L2 domain alone.

## Argument

### Scope and attribution check

The development originated in the normal-tuple branch of the normal-domain investigation.
The local reuse pass examined C_F0044's coordinate-only curvature estimate, C_F0055's scalar theorem, C_F0058's free-product end-module estimate, C_F0063 Appendix A and L_F0011.
Their stated conclusions do not provide the correlated weighted-kernel estimate below.
A targeted search of fixed C/L/U materials and the local literature registry/contents found no source unit for Voiculescu's 1999 liberation article and no retained theorem identifying the following liberation-vacuum spectral measure.
The author's publication list identifies that article as *Advances in Mathematics* 146 (1999), 101--166, but its original text was not obtained in this bounded search.
No theorem from it is silently imported.

The underlying closable-inclusion/absolute-continuity principle is standard.
A primary-source attribution was checked in [Tar16, arXiv v2](../literature/pdf/Tar16--arxiv-v2.pdf), first page, Section 1, and the formulation around (2.3) in Section 2: an absolutely continuous pair of finite measures gives a closable inclusion between the associated L2 spaces.
The argument below directly proves the needed continuous-polynomial-core version and its graph closure.
The source is attribution for that established operator/measure mechanism, not an additional unproved premise or a whole-paper audit.

### The marginal restriction of the actual liberation adjoint

Use the actual real liberation derivation \(\beta=\mathrm i\gamma\), and set \(\zeta=\beta^*(1\otimes1)=\zeta^*\).
Let \(K=\sigma(Z)\), \(N=L^\infty(K,\mu)\), and let \(\nu\) be the finite joint spectral measure of \(\zeta\) for the commuting left and right actions of \(N\):
\[
 \nu(A\times B)=\|1_A(Z)\zeta1_B(Z)\|_2^2.
\]
For a marginal function \(q\), write \(S_q\) for that left/right spectral action; on a separated polynomial tensor \(q=\sum a\otimes b\), \(S_q\zeta=\sum a\zeta b\).
Define
\[
 \operatorname{row}(q)(z)=\int q(z,v)\,d\mu(v),\qquad
 \operatorname{col}(q)(v)=\int q(z,v)\,d\mu(z).
\]
The polynomial-tensor adjoint formula and \(\beta(n)=\mathrm i(n\otimes1-1\otimes n)\) give
\[
 \beta^*q=S_q\zeta+
 \mathrm i\{\operatorname{col}(q)-\operatorname{row}(q)\}.
 \tag{S1}
\]
For example, the two corrections at \(a\otimes b\) are \(-\mathrm i(a-\tau(a))b-\mathrm ia(\tau(b)-b)\), which give (S1).
The row/column correction has norm at most \(2\|q\|_{L^2(\mu^2)}\).

It follows that \(\nu\ll\mu^2\).
To prove this directly, if a Borel set \(B\subseteq K^2\) has \(\mu^2(B)=0\), choose polynomial tensors \(q_n\) converging to \(1_B\) in \(L^2(\mu^2+\nu)\).
Such approximation follows from regularity of the two finite Borel measures, density of continuous functions and Stone--Weierstrass on the compact spectral space.
Then \(q_n\to0\) in \(L^2(\mu^2)\), whereas (S1) converges in \(H\) to \(S_{1_B}\zeta\).
Closedness of the actual \(\beta^*\) forces the latter vector to vanish.
Therefore \(\nu(B)=0\).

Moreover the closure of **the marginal polynomial-tensor restriction** of \(\beta^*\), as an operator from \(L^2(\mu^2)\) to \(H\), has exactly the domain
\[
 L^2(\mu^2)\cap L^2(\nu)
\]
and action (S1).
Indeed the graph norm is equivalent to the norm on \(L^2(\mu^2+\nu)\), because the correction in (S1) is bounded and \(\|S_q\zeta\|_2=\|q\|_{L^2(\nu)}\).
Polynomial tensors are dense in that weighted L2 space.
This statement is about the graph closure of this restriction; it does not assert, without an additional argument, that it is every vector in the intersection of \(\operatorname{Dom}\beta^*\) with the marginal Hilbert tensor space.

In particular, for real symmetric \(g\in L^2(\mu^2)\cap L^2(\nu)\), the outer derivation
\[
 \beta_g(p)=\mathrm i I_g\gamma(p)
\]
on the original algebraic core has the actual vacuum
\[
 \eta_g=\beta^*g=S_g\zeta.
 \tag{S2}
\]
Its inner insertion is a finite sum of bounded outer coefficients multiplying the vector \(g\); it is not assumed bounded on the full coarse space.
Formula (S2) follows first on finite tensors by tracial cyclicity and then by the adjoint graph approximation just proved.
Reality follows from the real symmetry of \(g\).
The usual algebraic tensor adjoint formula then makes \(\beta_g\) closable and gives
\[
 E_{g,0}^*p=p\eta_g-E_{g,0}p,\qquad
 E_{g,0}=(\mathrm{id}\otimes\tau)\beta_g.
 \tag{S3}
\]

### Uniform row L2 bounds close the kernel-composition hierarchy

Assume in addition
\[
 m=\mathop{\rm ess\,sup}_{z\sim\mu}
       \left(\int|g(z,v)|^2d\mu(v)\right)^{1/2}<\infty.
 \tag{B1}
\]
Symmetry gives the same column bound.
Write
\[
 H_g=\|g\|_{L^2(\mu^2)},\quad r=\max(1,H_g),\quad
 B=\|\eta_g\|_2+H_g,\quad
 C=2\|\zeta\|_2m^2+2H_gr+r^2,\quad
 K_g=B+\sqrt{B^2+C}.
 \tag{B2}
\]
The contraction estimates are
\[
 \|E_{g,0}p\|_2\le2K_g\|p\|,\qquad
 \|E_{g,0}^*p\|_2\le(\|\eta_g\|_2+2K_g)\|p\|.
 \tag{B3}
\]
Consequently both the closure of the original contraction and its actual adjoint contain \(M\Omega\), by the bounded Kaplansky/closed-graph argument detailed below.
The next paragraphs give the full proof, first for finite kernels and then for the stated general kernel.

**Finite kernels and actual enlarged core.**
It is convenient to allow bounded measurable marginal factors.
This does not change the original closures: a bounded \(n\in N\) has uniformly bounded original marginal polynomial approximants converging strongly and in L2.
Their liberation derivatives converge to \(\mathrm i(n\otimes1-1\otimes n)\).
The outer actions of uniformly bounded strongly convergent factors converge strongly on the coarse correspondence.
Thus every finite word in bounded \(N\) factors and original other-coordinate factors lies in the actual liberation graph, with its Leibniz derivative.
For a fixed finite bounded marginal kernel \(q\), the same argument applies to \(\beta_q\), because multiplication of the fixed Hilbert vector \(q\) by those bounded outer approximants converges in L2.
The actual vacuum pairing and (S3) extend to this enlarged core by the same bounded graph approximation.
For finite bounded kernels, all derivative images and their partial traces are algebraic tensors over this enlarged core; hence the iterates used below have their actual domains there.

Let \(q\) be a finite real symmetric bounded marginal tensor, with row bound at most \(m\), Hilbert norm at most \(H_g\), and put \(T_qf(z)=\int q(z,v)f(v)d\mu(v)\).
Then \(\|T_q\|\le H_g\le r\).
Its composition powers satisfy
\[
 \|q^{\circ k}\|_2\le H_gr^{k-1},\qquad
 \|q^{\circ k}\|_\infty\le m^2r^{k-2}\quad(k\ge2).
 \tag{B4}
\]
For the second estimate, factor the kernel as a row of \(q\), the operator \(T_q^{k-2}\), and a column of \(q\), and apply Cauchy--Schwarz.
All powers are again finite real symmetric marginal tensors.
Formula (S1) therefore gives
\[
 \|\eta_{q^{\circ k}}\|_2
 \le \|\zeta\|_2m^2r^{k-2}\quad(k\ge2).
 \tag{B5}
\]


**The exact finite-kernel defect and energy calculation.**
For any finite real symmetric bounded marginal kernel \(b\), put \(a_b=\operatorname{row}(b)\), \(\ell_b=b\circ b\), and
\[
 D_b=(\beta_b\otimes1)\beta_b-(1\otimes\beta_b)\beta_b,\qquad
 C_b=(\mathrm{id}\otimes\tau\otimes\tau)D_b.
\]
The two mixed terms in the Leibniz rule cancel, so \(D_b\) is an outer derivation.
It vanishes on \(\mathcal B\).
On a marginal function \(f\), direct expansion gives
\[
 D_b f(z,w,v)=-(f(z)-f(v))
 \{b(z,v)b(z,w)+b(z,v)b(w,v)-b(z,w)b(w,v)\}.
 \tag{B0a}
\]
Tracing the middle leg gives the marginal weight \(b(z,v)(a_b(z)+a_b(v))-\ell_b(z,v)\).
The inner insertion identity, and \(E_b(pa_b)-pE_b(a_b)\) for insertion on the second leg, yield on the enlarged core
\[
 C_bp=\mathrm i\{E_b(p)a_b+E_b(pa_b)-pE_b(a_b)-E_{\ell_b}p\}.
 \tag{B0b}
\]
For a unitary \(u\), the actual adjoint formula \(E_b^*u=u\eta_b-E_bu\) and \(\tau(E_b(a_b))=\tau(\eta_ba_b)\) imply
\[
 \operatorname{Re}\langle u,C_bu\rangle
 =-2\operatorname{Im}\tau(a_bu^*E_bu)
  +\operatorname{Im}\langle u,E_{\ell_b}u\rangle.
 \tag{B0c}
\]
To check the first term directly, if \(t=\tau(a_bu^*E_bu)\), the first three scalar terms inside braces in (B0b) reduce to \(t-\bar t\).
Multiplication by \(\mathrm i\) then gives \(-2\operatorname{Im}t\).

Here is the energy identity and its domain justification.
For a polynomial core element \(p\), its \(E_bp\) lies in the enlarged core.
Actual iterates and the vacuum on the second tensor leg give \(E_b^2p=C_bp+\Theta(\beta_bp)\eta_b\), where \(\Theta(x\otimes y)v=x\tau(yv)\).
Pair this with \(p\) and use \(E_b^*p=p\eta_b-E_bp\).
Expanding \(\beta_b(p^*p)\) by the Leibniz rule gives
\[
 \|E_bp\|_2^2
 =2\operatorname{Re}\langle E_bp,p\eta_b\rangle
  -\operatorname{Re}\langle\beta_b(p^*p),1\otimes\eta_b\rangle
  -\operatorname{Re}\langle p,C_bp\rangle.
 \tag{B0d}
\]
For \(u=a+\mathrm i\sqrt{1-a^2}\), with \(a=a^*\) in the original core and \(\|a\|<1\), the binomial series converges in norm and in every first-derivative seminorm in (B0d), including the seminorm of \(D_b\), because these are outer derivations.
The bound for the derivative of \(a^k\) is \(k\|a\|^{k-1}\) times its value at \(a\).
Thus the limit of the middle term is zero, since \(u^*u=1\).
The remaining terms give
\[
 \|E_bu\|_2^2
 =2\operatorname{Re}\langle E_bu,u\eta_b\rangle
  -\operatorname{Re}\langle u,C_bu\rangle.
 \tag{B0e}
\]
This argument does not claim that \(u\) belongs to the original domain of a second iterate.
It uses only the final polynomial identity and the stated first-derivative limits, as in C_F0043 Sections 3.1--3.2.
Finally
\[
 |\tau(a_bu^*E_bu)|\le\|a_b\|_2\|E_bu\|_2
 \le\|b\|_2\|E_bu\|_2.
\]
Equations (B0c)--(B0e) therefore prove (B6) below.


Fix an analytic-core unitary \(u=a+\mathrm i\sqrt{1-a^2}\), where \(a=a^*\) is in the original polynomial core and \(\|a\|<1\).
The finite-kernel calculation (B0c)--(B0e) and the triangle inequality give, for every such finite real symmetric kernel \(b\),
\[
 \|E_bu\|_2^2
 \le2(\|\eta_b\|_2+\|b\|_2)\|E_bu\|_2+
       \|E_{b\circ b}u\|_2.
 \tag{B6}
\]
Its extension from polynomials to \(u\) uses the final energy expression and first-derivative power series: each defect is an outer derivation with algebraic values.
Thus no original twice-iterated domain at \(u\) is presumed.

Set \(q_n=q^{\circ 2^n}\), \(v_n=\|E_{q_n}u\|_2\) and \(w_n=v_n/r^{2^n}\).
For \(n\ge1\), (B4)--(B6) give
\[
 w_n^2\le A w_n+w_{n+1},\qquad
 A=2\left(\|\zeta\|_2m^2/r^2+H_g/r\right).
 \tag{B7}
\]
This sequence is bounded for the fixed \(u\): the finite Leibniz expansion of \(\gamma(a)\), followed by the norm-convergent differentiated binomial series, gives \(\|E_bu\|_2\le c_u\|b\|_2\) for every marginal Hilbert tensor \(b\).
Here \(c_u\) can depend on the fixed algebraic expression for \(a\), but not on \(b\) or \(n\).
By (B4), \(w_n\le c_uH_g/r\).

A bounded nonnegative sequence satisfying (B7) must satisfy \(w_n\le A+1\).
Otherwise, once \(w_n>A+1\), the inequality \(w_{n+1}\ge w_n(w_n-A)\) makes the sequence strictly increasing;
if it had a finite limit \(L>A+1\), passing to the limit would give \(L^2\le(A+1)L\), a contradiction.
Hence
\[
 v_1\le r^2(A+1)=C.
\]
Using (B6) once more at \(n=0\) yields
\[
 \|E_qu\|_2
 \le \|\eta_q\|_2+H_g+
       \sqrt{(\|\eta_q\|_2+H_g)^2+C}.
 \tag{B8}
\]
This uniform estimate does not divide by the spectral radius, so it remains valid along approximations whose integral-operator norms tend to zero.

**Passage to the general kernel.**
First clamp the real symmetric \(g\) pointwise to \([-R,R]\), producing \(g_R\).
This preserves (B1), does not increase \(H_g\), and \(g_R\to g\) in \(L^2(\mu^2+\nu)\).
Thus (S1)--(S2) give actual \(\eta_{g_R}\to\eta_g\).

Choose finite measurable partitions increasing to the Borel sigma field modulo \(\mu\), and conditionally average \(g_R\) in both variables.
The resulting finite bounded real symmetric kernels \(q_j\) satisfy \(\|q_j\|_\infty\le R\), \(\|q_j\|_2\le H_g\), and row bound at most \(m\), by two applications of conditional Jensen.
They converge to \(g_R\) in \(L^2(\mu^2)\).
A subsequence converges \(\mu^2\)-almost everywhere and hence \(\nu\)-almost everywhere, since \(\nu\ll\mu^2\); the uniform bound gives convergence in \(L^2(\nu)\).
Therefore \(\eta_{q_j}\to\eta_{g_R}\).

For the fixed analytic unitary \(u\), the already proved estimate \(\|E_bu\|_2\le c_u\|b\|_2\) passes (B8) first to \(g_R\) and then to \(g\), giving \(\|E_gu\|_2\le K_g\).
This passage uses pointwise convergence at each original core/analytic-core vector and uniform estimates.
It does not claim convergence of the approximating contractions in their operator-norm-to-L2 norms.

Apply the same bound to \(u^*\), average to recover \(a=(u+u^*)/2\), rescale an arbitrary selfadjoint core element, and split its real and imaginary parts.
This gives (B3).
Formula (S3) gives the adjoint bound.
For completeness, take uniformly operator-norm-bounded core approximants to a bounded element of M, converging strongly and in L2.
The two bounds (B3) make their images under E_{g,0} and E_{g,0}^* bounded in H.
Weakly convergent subnets give graph points of the corresponding closed operators, because closed linear graphs are weakly closed.
Their first coordinates converge to the specified bounded element.
Thus that element belongs to both the original contraction closure and its actual adjoint, with the stated bounds.
This is the C_F0027 Section 5 bridge; it uses neither normality of the other generators nor a derivative commutator in this application.
The general kernel need not have algebraic tensor values or an actual second derivative; its proof obtains the bounds through the finite-kernel energy approximants.

### Why an arbitrary weighted adjoint domain does not support the bootstrap

The uniform row bound is substantive.
An abstract symmetric measure/kernel example shows that \(g\in L^2(\mu^2)\cap L^2(\nu)\) and even a strict integral-operator spectral-radius bound do not force \(g\circ g\in L^2(\nu)\).

Take Lebesgue probability measure on \([0,1]\), with disjoint triples of measurable sets \(A_n,B_n,C_n\), each of measure \(d_n=2^{-3n}\), for \(n\ge1\).
Their total measure is \(3/7<1\).
Put the real symmetric kernel \(g\) equal to \(t_n=2^{2n}\) on
\[
 A_n\times B_n,\ B_n\times A_n,\ B_n\times C_n,\ C_n\times B_n
\]
and zero elsewhere.
Let \(\nu=w\mu^2\), where \(w\) is supported on \(A_n\times C_n\) and its transpose, and those two rectangles together have \(\nu\)-mass \(2^{-n}\).
Equivalently \(w=2^{-n}/(2d_n^2)\) there.
Then \(\nu\) is a finite symmetric absolutely continuous measure,
\[
 \|g\|_2^2=4\sum_{n\ge1}2^{-2n}<\infty,\qquad
 \|g\|_{L^2(\nu)}=0.
\]
On each three-block normalized constant-function space, \(T_g\) is \(t_nd_n\) times the adjacency matrix of the three-vertex path.
Thus \(\|T_g\|=\sup_n\sqrt2\,2^{-n}=1/\sqrt2<1\).
But \(g\circ g= t_n^2d_n=2^n\) on \(A_n\times C_n\) and its transpose, so
\[
 \|g\circ g\|_{L^2(\nu)}^2
 =\sum_{n\ge1}2^{2n}2^{-n}=\infty.
\]
Its row L2 norms are unbounded.
Scaling \(g\) by any nonzero constant does not repair this failure.

This \(\nu\) is only an abstract spectral-weight model; it has not been realized as the liberation-vacuum measure of a tracial joint law.
It is therefore not a counterexample to the normal Task or to a potential theorem using additional liberation-specific constraints.
It precisely blocks the proposed implication from the weighted L2 graph-domain condition alone to compositional vacuum propagation.


## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:24 |
| status | open |
| reason | Complete candidate spectral-adjoint interface, uniform-row kernel-composition bootstrap, actual finite-kernel approximation, and precisely limited abstract failure retained for independent review. |

Recorded authoring stage: proof draft.
Recorded review label: self-reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact represented partial-liberation hypotheses, spectral graph closure, real symmetric row-bounded kernel and canonical actual full domains. |
| argument | [Argument](#argument) | Complete adjoint/spectral proof, real defect identity, bounded-sequence bootstrap, approximation and abstract composition-domain failure. |
| dependency | [C_F0063 Appendix A](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Actual real-liberation tensor-adjoint and closability mechanism; its abstract final formulation applies to the stated algebraic liberation derivation and actual vacuum. |
| dependency | [C_F0043](Yin_C_F0043_v1.md#statement) | Controlled real-energy and analytic-unitary first-derivative limiting mechanism, with the new weighted defect fully computed here. |
| dependency | [C_F0027](Yin_C_F0027_v1.md#statement) | Section 5 bounded core and adjoint estimates imply the actual all-bounded-vector domains; the generic weak closed-graph argument is explicitly rechecked here. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:37 |
| status | proved |
| reason | Adopt the complete fixed proof after R_F0050 independently checked the spectral graph domain, actual weighted vacua, finite-kernel energy and iteration, both canonical domains, and the precise nonrealization limit of the abstract obstruction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact represented partial-liberation hypotheses, spectral graph closure, real symmetric row-bounded kernel and canonical actual full domains. |
| argument | [Argument](#argument) | Complete adjoint/spectral proof, real defect identity, bounded-sequence bootstrap, approximation and abstract composition-domain failure. |
| dependency | [C_F0063 Appendix A](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Actual real-liberation tensor-adjoint and closability mechanism; its abstract final formulation applies to the stated algebraic liberation derivation and actual vacuum. |
| dependency | [C_F0043](Yin_C_F0043_v1.md#statement) | Controlled real-energy and analytic-unitary first-derivative limiting mechanism, with the new weighted defect fully computed here. |
| dependency | [C_F0027](Yin_C_F0027_v1.md#statement) | Section 5 bounded core and adjoint estimates imply the actual all-bounded-vector domains; the generic weak closed-graph argument is explicitly rechecked here. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0050_v1.md#conclusion) | Exact statement, complete argument and all three declared dependency scopes; no unrestricted normal comparison is claimed. |

