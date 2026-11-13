---
author: Yin
---
# Column bounds on the cyclic bimodules of a normal coordinate and its adjoint

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be a finite tuple of bounded normal generators in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, satisfying [actual ACSY](../tasks/Yin_T_F0011_v1.md#contract).
Let \(\mathcal P=\mathbb C\langle X,X^*\rangle\), \(H=L^2(M,\tau)\), and use inner products linear in their second entry.
Fix \(i\), let \(\delta=\delta_i\) be the coordinate derivation with vacuum \(\xi=\delta^*(1\otimes1)\), and put \(N=W^*(X_j:j\ne i)\), \(x=X_i-\mathbb E_N X_i\), and \(H_x=\overline{\operatorname{span}(NxN)}^2\).
On \(\operatorname{Dom}\bar\delta\) write \(Ep=(\mathrm{id}\otimes\tau)\bar\delta p\).
Let \(\mathcal D_b\) consist of the bounded \(p\) admitting a uniformly operator-bounded net from \(\mathcal P\) converging strongly-star to \(p\) and in the Hilbert graph of \(\bar\delta\).
In particular \(\mathcal P\subset\mathcal D_b\).

1. Let \(P_1\) project onto \(L^2(N)\oplus H_x\).
   For every finite column in \(\mathcal D_b\),
   \[
      \left(\sum_j\|P_1 E p_j\|_2^2\right)^{1/2}
       \le \big(\|\xi\|_2+\|h^{-1/2}\|_2\big)
                \left\|\sum_jp_j^*p_j\right\|^{1/2}
       \le 2\|\xi\|_2 \left\|\sum_jp_j^*p_j\right\|^{1/2},
   \]
   where \(h\) is the faithful cyclic density in [C_F0217, (4)](Yin_C_F0217_v1.md#statement).
   Formula (L1) below identifies the projected slice itself.
   On the linear span of \(N,NxN,NxNxN\), with arbitrary bounded coefficients in \(N\), these estimates hold for \(E\) without projection.
   On the full original core the [column cost](Yin_C_F0208_v1.md#statement) is finite if and only if the cost after projection by \(I-P_1\) is finite.
2. Put \(A=N\bar\otimes N^{\rm op}\subset\mathcal B=M\bar\otimes M^{\rm op}\), with product traces, let \(\mathbb E_A:\mathcal B\to A\) be the trace-preserving conditional expectation and let \(\Phi(c\otimes d)=c\otimes d^{\rm op}\) identify the coarse Hilbert space with \(L^2(\mathcal B)\).
   Set \(t=\mathbb E_A(\Phi(\bar\delta x^*))\).
   If \(\|t\|<1\), let \(P_{\pm}\) project onto \(L^2(N)\oplus\overline{\operatorname{span}(NxN+Nx^*N)}^2\).
   Then every finite column in \(\mathcal D_b\) satisfies
   \[
         \left(\sum_j\|P_{\pm}E p_j\|_2^2\right)^{1/2}
           \le \left(1+\frac{2\sqrt2}{1-\|t\|}\right)\|\xi\|_2
                    \left\|\sum_jp_j^*p_j\right\|^{1/2}.
   \]
   In particular finiteness of the full core column cost in this case is equivalent to finiteness for \((I-P_{\pm})E\).

## Argument

### Pairing against the first cyclic span

Use \(N=W^*(X_j:j\ne i)\), \(x=X_i-\mathbb E_N X_i\), \(H_x=\overline{NxN}^{\,2}\) (closed linear span), \(A=N\bar\otimes N^{\rm op}\), and the polar data \(W,h\) of [C_F0217](Yin_C_F0217_v1.md#polar-decomposition-and-the-integrable-inverse-density).
Let \(P_1\) be the Hilbert projection onto \(L^2(N)\oplus H_x\), and regard \(W^*:L^2(A)\to H_x\) as the isometry onto the coarse summand.
Write \(\delta=\delta_i\), \(\xi=\delta^*(1\otimes1)\), \(Ep=(\mathrm{id}\otimes\tau)\bar\delta p\), and \(\epsilon(a)=(\delta(a^*))^\dagger\), where \(\dagger\) flips and takes adjoints.
By the [normal phase formula](Yin_C_F0076_v1.md#statement), \(K=\bar\epsilon(x)=(\bar\delta x^*)^\dagger\) is in the abelian marginal tensor algebra and its phase has modulus one almost everywhere.
Here both closed derivations kill \(N\) and intertwine its left and right actions by the [omitted-algebra graph argument](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra).
Map a Hilbert tensor into \(L^2(\mathcal B)\), \(\mathcal B=M\bar\otimes M^{\rm op}\), by the linear unitary \(\Phi(c\otimes d)=c\otimes d^{\rm op}\).
Set \(K_0=\Phi(K)^*\), which takes adjoints in both legs, with no additional flip.
On the abelian marginal tensor subalgebra \(\Phi\) preserves multiplication as well as the trace and the adjoint, so \(K_0\) is unitary in \(\mathcal B\).
With \(\mathbb E_A:\mathcal B\to A\) the product-trace-preserving conditional expectation, put
\[
                    V_p=\mathbb E_A\big((p\otimes1)K_0\big)\in A .
\]
For every bounded \(p\) which admits uniformly operator-bounded original core approximants converging strongly-star to \(p\) and in the graph of \(\bar\delta\), one has
\[
                 P_1 Ep=P_1(p\xi^*)-W^*\big(V_p h^{-1/2}\big).            \tag{L1}
\]
This includes every original starred polynomial.

To verify (L1), take \(q=\sum_j a_j\otimes b_j^{\rm op}\in N\odot N^{\rm op}\) and \(y=qx=\sum_j a_jxb_j\).
The bounded products \(y^*p\) belong to \(\operatorname{Dom}\bar\delta\) with the product rule.
Indeed bounded strong-star approximations to \(a_j,b_j,\mathbb E_NX_i\) by omitted-coordinate core polynomials have identically zero derivatives.
Such approximations exist by [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001), using the norm density of the polynomials in their \(C^*\)-algebra.
They approximate \(y^*\) in its graph by the polynomial product rule, since bounded strong-star convergence of outer factors acts strongly on the coarse Hilbert space.
Multiplying by the stipulated approximants for \(p\) gives the stated product rule in the closure.
Pair the rule for \(y^*p\) with the vacuum tensor and use its actual adjoint.
For \(y=axb\) the resulting endpoint term \((\tau\otimes\tau)((\bar\delta y^*)p)\) equals \(\langle a\otimes b^{\rm op},(p\otimes1)K_0\rangle_{L^2(\mathcal B)}\), with the inner product linear in its second entry.
Indeed if \(K=c\otimes d\) then \(\bar\delta y^*=b^*d^*\otimes c^*a^*\), so the two factors after tracing are \(\tau(a^*p c^*)\) and \(\tau(b^*d^*)\).
The two sides are continuous in the Hilbert tensor \(K\) for these fixed bounded elements, giving the identity for the actual phase.
Summing and projecting onto \(A\) gives
\[
                 \langle qx,Ep\rangle=\langle qx,p\xi^*\rangle
                                        -\langle q,V_p\rangle_{L^2(A)} .
\]
By the cyclic-module formula \(W(qx)=q h^{1/2}\), where \(W\) vanishes on its kernel summand, and both \(h^{1/2},h^{-1/2}\) are in \(L^2(A)\).
Thus \(\langle qh^{1/2},V_p h^{-1/2}\rangle=\tau_A(q^*V_p)\), by tracial cycling of the two \(L^2\) factors and \(h^{-1/2}h^{1/2}=1\).
This proves (L1) against \(H_x\) by density, even when \(H_x\) contains a singular summand.
Testing instead against \(N\) gives \(\mathbb E_N(Ep)=\mathbb E_N(p\xi^*)\) by the same product rule with zero endpoint term.
Orthogonality proves (L1) against the full range of \(P_1\).

Conditional Schwarz, positivity of \(\mathbb E_A\), and unitarity of \(K_0\) give for any finite column
\[
 \sum_j V_{p_j}^*V_{p_j}
 \ \le\ \mathbb E_A\!\left(K_0^*\big((\textstyle\sum_j p_j^*p_j)\otimes1\big)K_0\right)
 \ \le\ \left\|\sum_j p_j^*p_j\right\|1_A .
\]
Pairing with the normal positive functional \(a\mapsto\langle h^{-1/2},a h^{-1/2}\rangle\) bounds the column of correction terms in (L1).
Projection is contractive and \(\sum_j\|p_j\xi^*\|_2^2\le\|\xi\|_2^2\|\sum_j p_j^*p_j\|\).
The Hilbert direct-sum triangle inequality therefore yields
\[
   \left(\sum_j\|P_1Ep_j\|_2^2\right)^{1/2}
    \le\big(\|\xi\|_2+\|h^{-1/2}\|_{2,A}\big)\left\|\sum_jp_j^*p_j\right\|^{1/2}
    \le 2\|\xi\|_2\left\|\sum_jp_j^*p_j\right\|^{1/2}.               \tag{L2}
\]
The last inequality is the actual inverse-density estimate in C_F0217.
Consequently the full [polynomial column cost](Yin_C_F0208_v1.md#statement) is finite exactly when the complementary cost for \((I-P_1)E\) is finite.

In particular (L2) bounds the entire slice on finite columns from the linear span of \(N,NxN,NxNxN\), allowing arbitrary bounded coefficients in \(N\).
The approximants above apply to each such word, since \(\bar\delta x=1\otimes1\), and also to every term in its finite product rule.
For \(a,b,d\in N\) one has \(E(axbxd)=a\,\tau(bxd)+axb\,\tau(d)=axb\,\tau(d)\), as \(\mathbb E_Nx=0\).
The slices on \(N\) and \(NxN\) lie in \(L^2(N)\).
Thus \(P_1\) fixes the full slice on all these inputs.
For unrestricted mixed words the new bound leaves only the component orthogonal to both the omitted algebra and its cyclic \(x\)-bimodule.
No estimate on that remaining component has been deduced here.

### The joint span of \(x\) and \(x^*\) under a phase gap

There is a further estimate on \(H_{x,x^*}=\overline{\operatorname{span}(NxN+Nx^*N)}^{\,2}\) when \(t=\mathbb E_A(k)\), \(k=\Phi(\bar\delta x^*)\), satisfies \(\|t\|<1\).
The scalar phase is symmetric in the two spectral variables, so \(k\) is unitary, \(\Phi(\bar\epsilon x)=k^*\), and \(K_0=k\) in (L1).
Write \(y=qx+rx^*\) for \(q,r\in N\odot N^{\rm op}\) and let \(\pi(a\otimes b^{\rm op})v=avb\) on \(L^2(M)\).
Taking \(\Phi\) of the two derivatives gives \(q+rk\) and \(qk^*+r\), respectively.
The actual vacuum \(\xi\) of \(\delta\) and the actual vacuum \(\xi^*\) of \(\epsilon\) therefore give
\[
 \langle y,\xi\rangle=\tau_A(q^*+t^*r^*),\qquad
 \langle y,\xi^*\rangle=\tau_A(tq^*+r^*) .
\]
Let \(P_{x,x^*}\) project onto this joint cyclic span and set \(\eta_1=P_{x,x^*}\xi,\ \eta_2=P_{x,x^*}\xi^*\).
On the closed joint cyclic span of \(\eta_1,\eta_2\) under \(\pi(N\odot N^{\rm op})\), the action extends normally to \(A\).
To check this without assuming a spatial tensor action on the whole ambient Hilbert space, close the restriction \(T:y\mapsto q+rk\) into \(L^2(\mathcal B)\).
It is a well-defined closable map by the graph of \(\bar\delta\), and the polar isometry intertwines the two \(N\)-actions from \((\ker T)^\perp\) into the left regular action on \(L^2(\mathcal B)\), by the unitary graph argument in C_F0217.
The latter action of \(A\subset\mathcal B\) is normal.
Its closed range subspace \(\overline{\operatorname{ran}T}\) reduces this action since it reduces both factor actions.
Thus the equivalent action \(\pi\) on \((\ker T)^\perp\) is normal on \(A\).
Both projected vacua lie there, since the two vacuum pairings against \(y\) are the pairings of \(Ty\) with \(1,k\), respectively, and hence extend to zero on \(\ker T\).

For a bounded \(p\) with the approximants used in (L1), write \(V_p=\mathbb E_A((p\otimes1)k)\) and \(U_p=\mathbb E_A(p\otimes1)\).
The two endpoint computations on \(qx\) and \(rx^*\) give
\[
 \langle y,p\xi^*-Ep\rangle=\tau_A(q^*V_p+r^*U_p).
\]
The \(x^*\)-term uses \(\bar\delta x=1\otimes1\) in \(\bar\delta((rx^*)^*)\).
Set
\[
 G=\begin{pmatrix}1&t\\t^*&1\end{pmatrix}\in M_2(A),\qquad
 \binom{a_p}{b_p}=G^{-1}\binom{V_p}{U_p}.
\]
This is a bounded inverse of norm at most \((1-\|t\|)^{-1}\) by the norm of its off-diagonal part.
For \(a,b\in A\) the vacuum pairings above give
\[
 \langle y,\pi(a)\eta_1+\pi(b)\eta_2\rangle
  =\tau_A\!\left(q^*(a+tb)+r^*(t^*a+b)\right).
\]
For algebraic coefficients this follows by moving their adjoints onto \(y\), and bounded ultraweak approximation proves it for all \(a,b\) using normality on the projected vacua and normal tracial pairings on \(A\).
Consequently \(P_{x,x^*}(p\xi^*-Ep)=\pi(a_p)\eta_1+\pi(b_p)\eta_2\).
For any finite column, conditional Schwarz gives \(\sum_j(V_{p_j}^*V_{p_j}+U_{p_j}^*U_{p_j})\le2\|\sum_j p_j^*p_j\|1_A\).
Applying \((G^{-1})^*G^{-1}\le(1-\|t\|)^{-2}I_2\) between each coefficient column and its adjoint gives
\[
 \sum_j(a_{p_j}^*a_{p_j}+b_{p_j}^*b_{p_j})
 \le 2(1-\|t\|)^{-2}\left\|\sum_jp_j^*p_j\right\|1_A .
\]
Since both projected vacua have norm at most \(\|\xi\|_2\), the same triangle and projection argument gives the joint projected column bound with constant \(\big(1+2\sqrt2/(1-\|t\|)\big)\|\xi\|_2\), including the orthogonal \(L^2(N)\)-summand.
This estimate controls the right slice on every original starred polynomial after projection to \(L^2(N)\oplus H_{x,x^*}\).
The squared norms of the joint projection and its complement add on each core column, giving the claimed equivalence of finiteness.

## Scope and provenance

The first projection estimate requires no phase gap.
The second uses the stated gap on the conditional expectation of the phase.
The two results leave the complementary outputs on general mixed core words open.
The responsible main agent proposed the second-layer investigation of [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
The check_defect agent developed both polar and phase calculations for Yin in the [normal endpoint draft](../drafts/Yin_D_F0006.md#first-output-layer-and-two-occurrence-inputs) and prepared this fixed candidate.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:00 |
| status | open |
| reason | The projected slice identities and column bounds, including the full two-occurrence input calculation and the conditional joint span, are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both projected column estimates, the full unstarred two-occurrence inputs and reductions to the complementary outputs. |
| argument | [Argument](#argument) | Bounded graph approximants, exact vacuum endpoints, inverse-density pairing, conditional Schwarz and the spatial action on the joint projected vacua. |
| dependency | [Normal derivatives](Yin_C_F0076_v1.md#statement) | Part 1 gives closability, symmetric modulus-one marginal phase and actual reversed vacuum. |
| dependency | [Omitted-coordinate graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Both derivations vanish on the omitted algebra and their closed graphs intertwine bounded left and right multiplication by it. |
| dependency | [Cyclic polar data](Yin_C_F0217_v1.md#polar-decomposition-and-the-integrable-inverse-density) | First-span polar isometry, pointed vector, faithful inverse density, vacuum norm control and the graph-unitary intertwining argument. |
| dependency | [Bounded strong approximation](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Kaplansky approximation of bounded coefficients in the omitted algebra by uniformly bounded strongly-star convergent core polynomials. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:09 |
| status | proved |
| reason | Adopt both first-layer column estimates and the two-occurrence domain assertion after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both projected column estimates, the full unstarred two-occurrence inputs and reductions to the complementary outputs. |
| argument | [Argument](#argument) | Bounded graph approximants, exact vacuum endpoints, inverse-density pairing, conditional Schwarz and the spatial action on the joint projected vacua. |
| dependency | [Normal derivatives](Yin_C_F0076_v1.md#statement) | Part 1 gives closability, symmetric modulus-one marginal phase and actual reversed vacuum. |
| dependency | [Omitted-coordinate graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Both derivations vanish on the omitted algebra and their closed graphs intertwine bounded left and right multiplication by it. |
| dependency | [Cyclic polar data](Yin_C_F0217_v1.md#polar-decomposition-and-the-integrable-inverse-density) | First-span polar isometry, pointed vector, faithful inverse density, vacuum norm control and the graph-unitary intertwining argument. |
| dependency | [Bounded strong approximation](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Kaplansky approximation of bounded coefficients in the omitted algebra by uniformly bounded strongly-star convergent core polynomials. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0231_v1.md#whole-proof-finding) | Both projections, strong-star graph products, conditional phase gap and the full slice on two-occurrence inputs. |
