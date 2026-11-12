---
author: Yin
---
# Rank-one height recurrences and compressed transport

Date: 2026-11-11 (Asia/Hong_Kong).
This investigation serves [S_A0006](../strategies/Yin_S_A0006.md) under the unchanged [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
The preceding [invertible-outer-coefficient argument](../claims/Yin_C_A0004_v3.md#height-layer-certificate) determines every layer from a fixed number of boundary layers and forces zero kernel.
Here both extreme coefficients are the scalar rank-one projection on the first of two coordinates.
The middle coefficient is specified explicitly, and the lost second-coordinate constraint is retained rather than counted as an automatic free parameter.
Provenance: project deduction by the main agent with two development helpers, using the accepted finite-trace, affiliated-rank and graded-companion interfaces below.
The independently responsible object is this two-coordinate recurrence and its exact residual formula; the earlier incidence-model versions retain their own statements.
No historical priority, new Atiyah group class or Task completion is asserted.

## Statement

**Definition (rank-one height model and trace convention).**
Let \(\varphi:G\to\mathbb Z\) be onto, let \(N=\ker\varphi\), and choose \(t\in G\) with \(\varphi(t)=1\).
Put \(M=\mathcal N(G)\), \(M_0=\mathcal N(N)\), \(\sigma=\operatorname{Ad}(t)\), and use the unnormalized matrix trace.
For bounded \(a=a^*,c=c^*,b\in M_0\), define
\[
P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
A=\begin{pmatrix}a&b\\b^*&c\end{pmatrix},\qquad
H=Pt+A+t^{-1}P
 =\begin{pmatrix}t+t^{-1}+a&b\\b^*&c\end{pmatrix}.
\tag{1}
\]
In \(Pt\), the group element acts on both coordinates before multiplication by \(P\).
Both extreme coefficients are exactly \(P\), of unnormalized rank one.
The group-ring subfamily is obtained by taking \(a,b,c\in\mathbb CN\).
Let \(\nu_G(H)=(\operatorname{Tr}_2\otimes\tau_G)(1_{\{0\}}(H))\).

1. For the Dirichlet compression \(H_m\) to \(m\) consecutive height layers, with \(m\ge2\),
   \[
   \left|\dim_N\ker H_m-m\nu_G(H)\right|\le2,\qquad
   \nu_G(H)=\lim_{m\to\infty}\frac{\dim_N\ker H_m}{m}.
   \tag{2}
   \]
   This exact limit has error at most \(2/m\), without amenability of \(N\), a spectral gap or closed-range assumptions.
   It does not replace the \(N\)-dimensions in its numerator by ordinary integers.
2. Define in the actual affiliated algebra
   \[
   r=1_{\{0\}}(c),\quad B=br,\quad
   f=\operatorname{supp}(BB^*),\quad s=\operatorname{supp}(B^*B),
   \quad p=1-f,\quad q=r-s,
   \]
   \[
   h=a-bc^\dagger b^*,\qquad
   \mathcal A=t+t^{-1}+h,\qquad R=p\mathcal A p\in\mathcal U(pMp).
   \tag{3}
   \]
   Here \(\dagger\) is the relative inverse, and \(R\) is the closed affiliated compression.
   The trace on the corner is the restriction of \(\tau_G\), without renormalization.
   Then
   \[
   q=1_{\ker b\cap\ker c}=1_{\{0\}}(b^*b+c^2),\qquad
   \boxed{\nu_G(H)=\tau_N(q)+\nu_p(R).}
   \tag{4}
   \]
   The last term denotes the trace of the kernel projection inside the \(p\)-corner, and is zero when \(p=0\).
3. The actual overlap defect \(\Delta=p\wedge\sigma^{-1}(1-p)\) gives
   \[
   \tau_N(q)\le\nu_G(H)\le\tau_N(q)+\tau_N(\Delta).
   \tag{5a}
   \]
   If
   \[
   p\wedge\sigma^{-1}(1-p)=0,
   \tag{5}
   \]
   then the residual term vanishes and the actual complete kernel projection is
   \[
   P_{\ker H}=\operatorname{diag}(0,q),\qquad \nu_G(H)=\tau_N(q).
   \tag{6}
   \]
   Sufficient stronger conditions are \(\sigma(p)=p\) and \(\|p-\sigma(p)\|<1\).
   When \(c^\dagger,B^\dagger\) are bounded and the latter norm is less than one, a bounded finite-layer argument proves (6).
   The weaker condition (5) is handled by the accepted affiliated graded criterion, without an unbounded Hilbert-space graph substitution.
4. For \(c=0\) and \(b=q_0=q_0^*=q_0^2\), set \(p_0=1-q_0\).
   The full bounded graph projection and the finite-orbit path formula (13)--(15) below hold.
   Two explicit group-ring models with identical ranks of all three coefficient blocks have kernel dimensions \(1/2\) and \(3/4\).
5. For every bounded selfadjoint \(Z\in M_0\), the genuinely coupled family
   \[
   H_Z=\begin{pmatrix}t+t^{-1}+Z&Z\\Z&Z\end{pmatrix}
   \quad\text{satisfies}\quad
   \nu_G(H_Z)=\dim_N\ker Z.
   \tag{7}
   \]
   Positive transport energy supplies the explicit values in (17); an arbitrary \(Z\) retains its coefficient-group kernel problem.
   The fractional comparison groups have torsion and do not refute A0001.

## Current assessment

[Selected decision](#decision-reviewed-rank-one-recurrence)

## Assessment history

### Decision reviewed-rank-one-recurrence

| Field | Value |
| --- | --- |
| date | 2026-11-11T15:10 |
| status | proved |
| reason | Independent whole-argument review supports the finite-section limit, singular-middle residual identity, overlap-defect and exact transport criteria, finite-orbit computations and coupled residual obstruction, with all stated trace, domain and group-ring limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete five-part statement for the two-coordinate rank-one height model, including (5a), all conditional exact formulas and the torsion-free-contract boundary. |
| argument | [Argument](#argument) | Formulas (1)--(17) and (5a), finite-section estimates, affiliated elimination, bounded graph projection, compressed transport, finite paths and both coefficient-group examples. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0018_v1.md#whole-artifact-finding) | Exact complete statement and argument, with explicit bindings to all sensitive subsections, dependency interfaces, degeneracies and conclusion limits. |
| dependency | [Bounded height certificate](Yin_C_A0004_v3.md#height-layer-certificate) | Finite-layer graph and trace mechanism, applied with the explicitly checked bounded outer maps on equal-trace projection layers. |
| dependency | [Finite-trace support facts](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Rectangular polar decomposition, support traces and finite affiliated matrix and corner foundations; no arbitrary group-ring integrality premise. |
| dependency | [Relative inverses](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | The relative inverse and support identities at the regular-closure definitions subsection, used in the actual affiliated algebra without a smaller-closure membership claim. |
| dependency | [Affiliated rank invariance](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) | Rank preservation by actual affiliated units and domain-safe block elimination, distinguished from unbounded Hilbert-space substitutions. |
| dependency | [Graded companion criterion](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials) | Full rank of an affiliated polynomial with independently invertible constant term and positive remaining degrees, applied in the fixed projection corner. |
| dependency | [Singular coefficient bound](../ledger/Yin_L_A0008_v1.md#a-unit-completion-instead-of-assuming-an-invertible-extreme-coefficient) | The constant-coefficient rank lower bound for the actual graded polynomial Rt, supplying the quantitative transported-overlap estimate. |

## Argument

<a id="finite-section-formula"></a>
### Exact finite sections and their arithmetic limitation

Identify the layer \(t^nN\) with \(N\) by left multiplication by \(t^n\).
Every identification intertwines the same right \(N\)-action.
For \(a_n=\sigma^{-n}(a)\), and similarly \(b_n,c_n\), the complete recurrence is
\[
x_{n-1}+x_{n+1}+a_nx_n+b_ny_n=0,\qquad
b_n^*x_n+c_ny_n=0.
\tag{8}
\]
Thus the forward and backward coefficient maps are both \(P\); their second rows vanish, but the second equation in (8) generally does not.
The compression \(H_m\) acts on \(\ell^2(N)^{2m}\), with \(x_0=x_{m+1}=0\).
Write \(d_m=\dim_N\ker H_m\), let \(\chi_m\) be the layer cut, and let \(Q=1_{\{0\}}(H)\).
Let \(E_m\) also denote the projection onto the first coordinate at each of the two endpoints, an \(N\)-module of dimension two.
Define the closed subspace
\[
V_m=\ker((I-E_m)H_m).
\]
The restriction of \(H_m\) to \(V_m\) has kernel \(\ker H_m\) and range in \(E_m\).
Rectangular polar decomposition, with closure of the range when necessary, gives \(\dim_N V_m\le d_m+2\).
The range of \(\chi_mQ\chi_m\) lies in \(V_m\), since cutting a global kernel vector produces errors only in the two first-coordinate endpoint equations.
This positive contraction therefore has trace at most \(d_m+2\).
Right \(G\)-equivariance of \(Q\) gives the same diagonal trace at every \(\delta_{t^n}\), hence
\[
m\nu_G(H)=\operatorname{Tr}_N(\chi_mQ\chi_m)\le d_m+2.
\tag{9}
\]

Conversely, impose \(x_1=x_m=0\) on \(\ker H_m\).
These two bounded coordinate constraints reduce \(N\)-dimension by at most two.
Zero extension of any resulting vector solves every global equation, including the two exterior equations, because the only crossing coefficient is \(P\).
The projection onto this zero-extended subspace is bounded above by both \(Q\) and \(\chi_m\), and hence by the positive compression \(\chi_mQ\chi_m\).
It follows that \(d_m-2\le m\nu_G(H)\), proving (2).
Neither estimate requires a closed range for \(H_m\) or for an intermediate map.

There is also the elementary bound \(\nu_G(H)\le1\).
Ignoring the second equation of (8), a restriction to \(m\) layers is determined by its first two \(x\)-coordinates and its \(m\) \(y\)-coordinates, through a bounded finite recurrence.
The resulting closed graph has \(N\)-dimension at most \(m+2\), so the same positive-compression trace argument and \(m\to\infty\) give the bound.
This agrees with the accepted [singular extreme-coefficient rank inequality](../ledger/Yin_L_A0008_v1.md#a-unit-completion-instead-of-assuming-an-invertible-extreme-coefficient).
It is an upper bound, not an integer-dimension conclusion.
Formula (2) improves the finite-layer information to an exact limit, but \(H_m\) is still a matrix over \(M_0\), of growing size.
No coefficient-group integrality input has disappeared.

<a id="singular-middle-reduction"></a>
### Exact reduction of the singular middle coefficient

All operations in this subsection are closed operations in \(\mathcal U(M)\) and its matrix or projection corners.
The [relative inverse and support identities](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions) and the [affiliated rank invariance](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) are accepted at their recorded scopes.
These facts give rank identities even when the relative inverses are unbounded.
They do not assert that singular relative inverses lie in the smaller group-ring rational closure.

Use the triangular affiliated unit
\[
L=\begin{pmatrix}1&-bc^\dagger\\0&1\end{pmatrix}.
\]
Since \(cc^\dagger=c^\dagger c=1-r\), direct multiplication gives
\[
LHL^*=\begin{pmatrix}\mathcal A&B\\B^*&c\end{pmatrix}.
\tag{10}
\]
The invertible support part of \(c\), on \(1-r\), splits off.
Also \(s\le r\), so \(q=r-s\) is a projection and is a zero summand of the remaining saddle operator.
The equation \(by=cy=0\) is exactly \(y\in q\ell^2(G)\), proving the first identity in (4).
The positive sum \(b^*b+c^2\) has the same kernel, proving the second description of \(q\).

On the remaining \(p\oplus f\oplus s\) corners, the saddle operator is
\[
\begin{pmatrix}
p\mathcal A p&p\mathcal A f&0\\
f\mathcal A p&f\mathcal A f&B\\
0&B^*&0
\end{pmatrix}.
\]
The map \(B:s\to f\) is an affiliated unit between its support corners.
On \(f\oplus s\), the lower-right block has inverse
\[
\begin{pmatrix}
0&(B^*)^{-1}\\
B^{-1}&-B^{-1}f\mathcal A f(B^*)^{-1}
\end{pmatrix}.
\tag{11}
\]
Multiplication verifies both inverse identities in the indicated noncommuting order.
Its upper-left entry is zero, so the Schur correction to \(p\mathcal A p\) vanishes exactly.
Thus
\[
\operatorname{rk}_G H=(1-\tau_N(r))+2\tau_N(s)+\operatorname{rk}_p R.
\]
Since \(\tau_N(s)=\tau_N(f)\), subtracting this identity from two gives (4).
When a support corner is zero, the corresponding block is absent and the same formula holds.

If both \(c^\dagger\) and \(B^\dagger\) are bounded, all these equations also give an actual bounded kernel parametrization.
Let \(k=1_{\{0\}}(R)\le p\) and set
\[
W=\binom{I}{-c^\dagger b^*-B^\dagger\mathcal A}.
\]
Then the kernel vectors are \(Wx+(0,z)\), with \(x\in k\ell^2(G)\) and \(z\in q\ell^2(G)\).
The first lower-coordinate term lies in \(1-r\), the second in \(s\), and both are orthogonal to \(q\).
Coordinate restriction and projection onto \(q\) give a bounded inverse parametrization.
Consequently the full orthogonal projection is
\[
P_{\ker H}=\operatorname{diag}(0,q)+
Wk[kW^*Wk]^{-1}_{k}kW^*.
\tag{12}
\]
The corner inverse exists because \(kW^*Wk\ge k\).
No such bounded graph formula is asserted when either relative inverse is unbounded.

<a id="compressed-transport-certificate"></a>
### The geometric condition on compressed height transport

The overlap defect also gives a quantitative bound when it is nonzero.
Regard \(R\) as an affiliated operator on the full space, zero on \(1-p\).
The polynomial
\[
Rt=p\sigma^{-1}(p)+(php)t+p\sigma(p)t^2
\]
has homogeneous degrees zero, one and two.
The accepted [singular constant-coefficient rank inequality](../ledger/Yin_L_A0008_v1.md#a-unit-completion-instead-of-assuming-an-invertible-extreme-coefficient) gives
\(\operatorname{rk}_G R=\operatorname{rk}_G(Rt)\ge\operatorname{rk}_G(p\sigma^{-1}(p))\).
Since \(p\sigma^{-1}(p)=(ptp)^*t\), its rank equals the rank of \(ptp\), namely \(\tau_N(p)-\tau_N(\Delta)\).
Subtracting from \(\tau_N(p)\) and applying (4) proves (5a).
This bounds the actual remaining contribution by the transported overlap defect rather than by the full omitted coordinate.

Suppose first \(p\ne0\), and put \(K=ptp\in pMp\).
Its kernel projection in the corner is \(p\wedge\sigma^{-1}(1-p)\): a vector in \(p\) is killed precisely when its translate by \(t\) lies in \(1-p\).
Under (5), finite-trace polar decomposition shows that both supports of \(K\) equal \(p\), so \(K\) has an affiliated inverse in \(pMp\).
The trace-preserving character action fixes \(M_0\), hence \(p,h\), and multiplies \(K\) by \(e^{i\theta}\).
In that corner,
\[
R(K^*)^{-1}
=p+(php)(K^*)^{-1}+K(K^*)^{-1}
\]
has homogeneous degrees zero, one and two, with independently invertible constant coefficient \(p\).
Apply the accepted [affiliated graded-companion criterion](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials) to the finite corner with normalized trace \(\tau_G/\tau_G(p)\).
It makes this expression an affiliated unit and gives \(\nu_p(R)=0\).
Rescaling the trace back changes no injectivity conclusion.
For \(p=0\), the same conclusion is immediate.
Formula (4) gives \(\nu_G(H)=\tau_N(q)\).
The visibly contained subspace \(0\oplus q\ell^2(G)\) already has this full dimension, so trace faithfulness proves the actual projection identity (6).

The stronger condition \(\kappa=\|p-\sigma(p)\|<1\) makes the compressed transport boundedly invertible:
\[
K^*K\ge(1-\kappa^2)p,\qquad KK^*\ge(1-\kappa^2)p.
\]
For example, \(\|(1-\sigma^{-1}(p))p\|\le\kappa\) gives the first inequality, and the other is analogous.
Assume additionally \(c^\dagger,B^\dagger\) bounded, so \(h\) is bounded.
In layer coordinates, \(p_n=\sigma^{-n}(p)\), and the extreme map from \(p_{n+1}\) to \(p_n\) is projection onto \(p_n\).
The two inequalities make it a bounded isomorphism.
The recurrence for \(R\) therefore determines all subsequent layers from its first two \(p\)-layers.
The [bounded finite-layer trace argument](../claims/Yin_C_A0004_v3.md#height-layer-certificate) applies to these varying but equal-trace modules and gives
\[
m\nu_p(R)\le2\tau_N(p).
\]
It proves zero residual kernel and hence the exact formula (6) by the finite-layer method itself.
Invariance \(\sigma(p)=p\) is the particularly simple case \(\kappa=0\).
Without bounded relative inverses or a bounded inverse for the compressed hopping, the preceding affiliated argument supplies the conclusion instead of an unjustified extension of this graph proof.

Two useful degenerate cases require no separate transport analysis.
If \(c\) is injective, then \(r=B=q=0\), \(p=1\), and (6) gives zero kernel even when \(c^{-1}\) is unbounded.
If \(c=0\) and \(b\) is injective, then finite-trace support equality gives \(p=q=0\), again giving zero kernel.
For example, \(b=1-v\) with \(v\in N\) of infinite order supplies the latter case by the regular-shift argument, without a lower spectral bound on \(b^*b\).

<a id="projection-middle-and-finite-orbits"></a>
### Projection middle coefficient and finite transport orbits

Take \(c=0\), \(b=q_0=q_0^*=q_0^2\), and \(p_0=1-q_0\).
Then (3) gives \(p=q=p_0\), \(h=a\), and
\[
\nu_G(H)=\tau_N(p_0)+\nu_{p_0}\bigl(p_0(t+t^{-1}+a)p_0\bigr).
\tag{13}
\]
Directly, the kernel equations say \(x=p_0x\), \(p_0(t+t^{-1}+a)p_0x=0\), and \(q_0y=-q_0(t+t^{-1}+a)x\).
Thus \((x,z)\mapsto(x,z-q_0(t+t^{-1}+a)x)\), with \(z=p_0z\), is a bounded equivariant kernel isomorphism.
This proves (13) and specializes (12) without any affiliated-domain issue.

Suppose a finite commutative subalgebra \(\mathcal D=\bigoplus_{i\in I}\mathbb C e_i\subseteq M_0\) has pairwise orthogonal projections summing to one and \(\sigma(e_i)=e_{\pi(i)}\).
Let \(q_0\) be a sum of these projections and \(a=\sum_i a_i e_i\), with real \(a_i\).
For an orbit \(O\) of \(\pi\), let \(m_O=|O|\), \(E_O=\sum_{i\in O}e_i\), and \(w_O=\tau_N(E_O)\).
Every \(e_i\) in this orbit has trace \(w_O/m_O\).
If \(q_0E_O=0\), the whole orbit remains in \(p_0\), and its invariant-corner height recurrence has zero kernel.
Otherwise the selected sites in \(p_0E_O\) split into maximal cyclic runs \(C\), each ending at deleted sites.
For a run of length \(\ell\), let \(J_C\) be the ordinary \(\ell\)-by-\(\ell\) matrix with diagonal the successive \(a_i\) and adjacent entries one.
Then
\[
\boxed{\nu_G(H)=\tau_N(p_0)+
\sum_{O:q_0E_O\ne0}\frac{w_O}{m_O}
\sum_{\text{runs }C\subset O}\dim_{\mathbb C}\ker J_C.}
\tag{14}
\]
Indeed, if \(e_0\) starts the run, the map
\((x_0,\ldots,x_{\ell-1})\mapsto\sum_{j=0}^{\ell-1}t^jx_j\)
from \((e_0\ell^2(G))^\ell\) to \(E_C\ell^2(G)\) is an equivariant unitary.
The projections \(t^je_0t^{-j}\) are exactly the distinct successive run projections.
This unitary conjugates the compressed residual on the run to \(J_C\otimes I\).
The exterior edges vanish under \(p_0\), so no boundary equation is omitted.
An ordinary kernel direction therefore contributes one copy of the \(e_0\)-module, of trace \(w_O/m_O\), proving (14).

Every \(J_C\) has kernel dimension at most one, since its first row and then its successive rows determine a kernel vector from its first coordinate.
Its determinant satisfies
\[
D_0=1,\quad D_1=a_1,\quad D_j=a_jD_{j-1}-D_{j-2}.
\tag{15}
\]
The run contributes precisely when \(D_\ell=0\).
At \(a=0\), this is exactly the condition that \(\ell\) be odd.
These are direct finite-path calculations; no random-cluster or spanning-forest theorem is being imported.

<a id="same-ranks-different-transport"></a>
### Same coefficient ranks and different exact dimensions

Let \(N=C_2\times C_2=\langle u,v\mid u^2=v^2=1,\ uv=vu\rangle\), set \(q_0=(1+u)/2\), \(p_u=(1-u)/2\), and choose \(a=0,c=0,b=q_0\).
For \(G_0=N\times\mathbb Z\), the projection \(p_u\) is invariant under \(t\), so (13) gives \(\nu_{G_0}(H)=1/2\).
For \(G_1=N\rtimes\mathbb Z\), use \(tut^{-1}=v\), \(tvt^{-1}=u\).
Write \(p_v=(1-v)/2\), \(e=p_up_v\) and \(d=p_u(1-p_v)\).
The projection \(e\) is invariant, while the translate of \(d\) is orthogonal to \(p_u\).
Consequently
\[
p_u(t+t^{-1})p_u=e(t+t^{-1}),\qquad
\nu_{p_u}\bigl(p_u(t+t^{-1})p_u\bigr)=\tau_N(d)=\tfrac14,
\]
\[
\nu_{G_0}(H)=\tfrac12,\qquad \nu_{G_1}(H)=\tfrac34.
\tag{16}
\]
On \(e\), the unit-outer height recurrence gives zero kernel; on \(d\), the residual vanishes identically.
In both models the ranks of the forward, middle and reverse coefficient blocks are respectively \(1,1,1\), since \(\operatorname{rk}A=2\tau_N(q_0)=1\).
Those three ranks therefore do not determine the kernel dimension.

The extra modes in the swapping model are \((x,-(t+t^{-1})x)\), \(x\in d\ell^2(G)\).
They are orthogonal to \((0,y)\), \(y\in p_u\ell^2(G)\), since \((t+t^{-1})d\) lies in \(q_0\).
Their orthogonal projection is the graph projection in (12), with a corner inverse of \(d(1+(t+t^{-1})^2)d\).
For this \(N\) and action, \(d\) commutes with \(t^2\), and that inverse on \(d\) is \((3+t^2+t^{-2})^{-1}d\).
It has infinite height propagation: its scalar Laurent multiplier is \(1/(3+z+z^{-1})\), which is not a Laurent polynomial.
Thus the projection is nonlocal even though its trace \(1/4\) is fixed by the finite orbit geometry.
Both groups have torsion; this is a mechanism obstruction, not an A0001 counterexample.

<a id="coupled-residual-and-energy"></a>
### A coupled arbitrary residual and a positive-energy certificate

For selfadjoint \(Z\in M_0\), use \(H_Z\) from (7) and the bounded constant unit
\[
W_0=\begin{pmatrix}1&0\\-1&1\end{pmatrix}.
\]
Direct multiplication in the indicated order gives
\[
W_0^*H_ZW_0=\operatorname{diag}(t+t^{-1},Z),\qquad W_0^*PW_0=P.
\]
The bilateral-shift operator \(t+t^{-1}\) is injective, since \(t\) has infinite order and its cyclic Fourier multiplier \(2\cos\theta\) vanishes only on a null set.
Hence (7) follows, and the actual kernel is \(0\oplus\ker Z\).
There is no commutation requirement between \(t\) and \(Z\).
For \(Z\ne0\), this is an explicitly coupled middle coefficient with the same rank-one extremes.
Even an arbitrary torsion-free coefficient group \(N\) is allowed, by taking \(G=N\times\mathbb Z\).
Thus a universal integer formula for this restricted family already has to resolve every selfadjoint scalar coefficient-group kernel it contains.
This is a scalar obstruction; it is not an equivalence with the complete all-matrix A0001 contract.

A geometric subclass is
\[
Z=\sum_{j=1}^k(1-h_j)^*(1-h_j),\qquad h_j\in N,\quad K_0=\langle h_1,\ldots,h_k\rangle.
\]
The energy identity makes \(\ker Z\) the common invariant space of the actual left translations \(h_j\).
Its vectors are constant on every left \(K_0\)-orbit in \(N\).
If \(K_0\) is infinite, square summability forces zero.
If \(K_0\) is finite, the kernel projection is \(|K_0|^{-1}\sum_{h\in K_0}h\).
Therefore
\[
\nu_G(H_Z)=
\begin{cases}
0,&K_0\text{ infinite},\\
|K_0|^{-1},&K_0\text{ finite}.
\end{cases}
\tag{17}
\]
The empty or trivial generating system gives \(K_0=\{1\}\) and dimension one.
For torsion-free \(N\), this subclass has dimension zero when some label is nonidentity and dimension one otherwise.
Its two-coordinate probability atom has half the displayed mass.
The argument reuses the actual regular-transport mechanism of [C_A0004_v2](../claims/Yin_C_A0004_v2.md#collective-holonomy-condition), now applied to the residual energy.
It controls that residual independently rather than postulating its integer kernel dimension.

## Dependencies, source scope and continuation

The direct inputs are the [bounded height proof](../claims/Yin_C_A0004_v3.md#height-layer-certificate), [finite-trace support facts](../audits/literature/MSY23/Yin_U004.md#msy23-u004), [relative-inverse conventions](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions), [affiliated rank invariance](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement), and [graded companion theorem](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials).
Their actual interfaces and previously recorded review scopes are reused; no prior review is presented as a review of the present deductions.
The [earlier singular-extreme examples](../ledger/Yin_L_A0008_v1.md#degree-one-still-contains-fractional-coefficient-defects) identify the existing coefficient-rank limitation and motivate the explicit transport comparison here.
The block elimination, finite-section error bound, projection-orbit calculations and coupled residual identities are supplied in full above.
No new external theorem is needed for those direct calculations, and no new historical attribution is asserted.

The finite-layer method gives an exact asymptotic formula for the whole specified model and an exact closed formula when compressed transport excludes the residual kernel.
Integer arithmetic additionally requires an independent integer value for \(\tau_N(q)\), or for the weighted finite-cluster contribution when (5) fails.
For arbitrary von Neumann coefficients those traces can be fractional; for torsion-free group-ring inputs the admissibility and dimensions of nontrivial coefficient projections are substantive questions.
The next useful step is to control a compressed transport with a nonzero overlap defect that does not close into a finite projection orbit.
A proposed extension must specify that actual defect module and its residual equations, and distinguish finite-cluster contributions from any remaining infinite component.
The coupled family (7) prevents treating a formal residual trace or a coefficient-rank count as a solution of that problem.
