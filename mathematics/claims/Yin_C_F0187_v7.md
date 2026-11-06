---
author: Yin
---

# Whole fourth-layer control from an inverse spectral gap

This version continues the bounded two-channel energy branch of the [matrix-coefficient F0013 contract](../tasks/Yin_T_F0013_v1.md#contract).
A mixed fourth-Walsh inner-product estimate controls cancellation when the largest absolute inverse eigenvalue is sufficiently separated from the remaining operator norm.
Its energy conclusion does not require Frobenius dominance, while its load conclusion uses a fixed upper bound on effective inverse rank.
Combining this branch with the fixed high-effective-rank and dominant-mode branches gives a matrix probability reduction with an explicitly smaller remaining minor exception.
The previous branches keep their original thresholds; no probability bound for the remaining exception or logarithmic conclusion is asserted.
The exact statement and argument are adopted by the [operator-gap decision](Yin_C_F0187_v9.md#decision-operator-gap-reviewed) at the current family entrance; the candidate decision below preserves its original assessment.

<a id="statement"></a>
## Exact bounded model and operator-gap conclusions

For \(j=1,2\), let \(W_j^{(N)}\) be independent real symmetric Wigner matrices with independent upper off-diagonal entries distributed as \(\xi_j/\sqrt N\).
The fixed real laws satisfy \(\mathbb E\xi_j=0\), \(\mathbb E\xi_j^2=1\), and \(|\xi_j|\le L\).
The diagonal entries of input \(j\) are independent copies of \(\zeta_j/\sqrt N\), where \(\zeta_j\) is fixed, real, centered and bounded by \(L\).
Zero diagonal laws are allowed.
All raw upper-triangular coordinates and both inputs are independent within each size, and the cross-size coupling is arbitrary.
The finite constant \(L\) covers all four fixed laws.

For \(S\subset[N]\), \(|S|\le1\), set \(n:=N-|S|\), and let \(C_{N,S},D_{N,S}\) be the corresponding principal submatrices of the two inputs with their original \(N^{-1/2}\) normalization.
Set
\[
 \alpha:=\sqrt2,\qquad X:=C_{N,S}+D_{N,S},\qquad
 Y:=C_{N,S}+\alpha D_{N,S},\qquad
 M:=\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix}.
\]
For each invertible \(M\), let \(\mathcal W(M)\) be the set of all real unit eigenvectors whose eigenvalues have smallest absolute value.
For \(w=(u,v)\in\mathcal W(M)\), with \(Mw=\lambda w\), define
\[
 Z:=M^{-1},\qquad q:=\lambda^{-1},\qquad E:=Z-qww^T
   =\begin{pmatrix}F&H_0\\H_0^T&J_0\end{pmatrix},\qquad
 T_0:=(H_0+H_0^T)/2,
\]
\[
 E_F:=\|E\|_{\rm F},\qquad m_E:=\|E\|,\qquad
 r_Z:=\frac{\|Z\|_{\rm F}^2}{\|Z\|^2}
       =1+\frac{E_F^2}{q^2},\qquad |q|=\|Z\|.
\]
The norm without subscript is the operator norm.
For \(n\ge1\), invertibility gives \(q\ne0\) and \(E_F\ge m_E>0\), since deleting one inverse eigenmode leaves \(2n-1\) nonzero modes.

Write the full inverse blocks as
\[
 Z=\begin{pmatrix}G&H\\H^T&J\end{pmatrix},\qquad T:=(H+H^T)/2,
\]
and define
\[
 h(x):=(x^TGx)(x^TJx)-(x^TTx)^2,\qquad
 p_4:=\Pi_4 h.
\]
Here \(\Pi_4\) denotes the fourth multilinear sign component after \(x_i=\varepsilon_i/\sqrt N\) and exact reduction of all \(\varepsilon_i^2\) to one.
For any fourth sign polynomial \(f_4=\sum_{|I|=4}f_I\varepsilon_I\), put
\[
 \sigma(f_4)^2:=\sum_{|I|=4}|f_I|^2,\qquad
 L_j(f_4):=\sum_{\substack{|I|=4\\j\in I}}|f_I|^2.
\]
Set \(\sigma_4:=\sigma(p_4)\), and when \(\sigma_4>0\), put
\[
 \tau_4:=\max_jL_j(p_4)/\sigma_4^2.
\]
Distinct sign monomials are orthogonal, so the coefficient norm is exactly the Walsh \(L^2\) norm.

There are fixed \(\gamma_*\in(0,1/2]\) and \(c_{\rm gap}>0\), depending only on the fixed laws, such that
\[
 \begin{split}
 \mathbb P\{\exists S,\ |S|\le1,\ M\text{ invertible},\quad
    \exists w\in\mathcal W(M):\quad&
 m_E\le\gamma_*|q|,\\
 &\sigma_4^2<c_{\rm gap}q^2E_F^2/N^4\}\longrightarrow0.
 \end{split}
 \tag{Operator-gap-energy}
\]
For every fixed finite \(K\ge1\) and every \(\varepsilon>0\), the same \(\gamma_*\) satisfies
\[
 \begin{split}
 \mathbb P\{\exists S,\ |S|\le1,\ M\text{ invertible},\quad
   \exists w\in\mathcal W(M):\quad&
 m_E\le\gamma_*|q|,\ r_Z\le K,\\
 &[\,\sigma_4=0\text{ or }(\sigma_4>0\text{ and }\tau_4>\varepsilon)\,]\}
 \longrightarrow0.
 \end{split}
 \tag{Operator-gap-load}
\]
The energy statement imposes no upper bound on \(E_F/|q|\); the effective-rank bound is used only for the load conclusion.
The quantifiers include every closest eigenspace choice.
If the largest absolute inverse eigenvalue is tied, then \(m_E=|q|\) for every such choice, so the operator-gap branch is empty.

These are unconditional bad-event bounds intersected with invertibility and the stated branches, not conditional estimates obtained by division by their probabilities.
For general bounded laws and for \(S=\varnothing\), \(p_4\) is a formal sign coefficient functional.
For one physical deletion and a Rademacher first off-diagonal law, it is the actual conditional fourth Walsh layer of the original parent pencil's two-by-two Schur determinant, by the fixed [fresh-row identification](Yin_C_F0187_v6.md#fresh-row-scope).
The second-input border and the exposed diagonals affect only lower raw degrees.

<a id="three-branch-reduction"></a>
## Matrix probability consequence retaining all three branches

For this consequence require additionally that \(\xi_1\) is Rademacher, and put
\[
 L_N:=\begin{pmatrix}W_1+W_2&I_N\\I_N&W_1+\sqrt2W_2\end{pmatrix},
 \qquad Q_N:=(W_1+\sqrt2W_2)(W_1+W_2)-I_N.
\]
Fix the same high-effective-rank threshold \(r_*\) as in [C187v6](Yin_C_F0187_v6.md#statement) and the same dominant-mode threshold \(K_*\) as in [C194v13](Yin_C_F0194_v13.md#dominant-branch-statement).
In particular \(K_*\) is the constant chosen in that fixed proof's [dominant coefficient estimate](Yin_C_F0194_v13.md#dominant-coefficients), not a replacement chosen from the present operator-gap constant.
Neither old threshold is enlarged here.

For each physical index \(i\), let \(M_i\) be the actual retained \(2(N-1)\)-dimensional principal pencil.
On its invertible branch choose a measurable closest-to-zero real unit eigenmode from that minor only, using the same convention as the fixed combined reduction.
Write \(q_i,E_i,E_{F,i},m_i,r_i\) for the quantities just defined, and set
\[
 \mathcal R_i^2:=
   \|\operatorname{off}F_i\|_{\rm F}^2+
   \|\operatorname{off}J_{0,i}\|_{\rm F}^2+
   \|\operatorname{off}T_{0,i}\|_{\rm F}^2.
\]
Define the unresolved minor event
\[
 \begin{split}
 \mathcal B_i:=\{M_i\text{ singular}\}\ \cup
 \{M_i\text{ invertible},\quad
   r_i<r_*,\quad |q_i|<K_*\mathcal R_i,\quad
   m_i>\gamma_*|q_i|\}.
 \end{split}
 \tag{Three-branch-minor-exception}
\]
There are fixed \(c,C>0\), depending only on the fixed laws, such that
\[
 \mathbb P\{s_{\min}(L_N)\le cN^{-5}
                  \text{ or }s_{\min}(Q_N)\le cN^{-5}\}
 \le o(1)+\frac C N\sum_{i=1}^N\mathbb P(\mathcal B_i).
 \tag{Three-branch-matrix-reduction}
\]
The retained invertible good region is exactly the union of the three displayed branch tests
\[
 r_i\ge r_*
 \quad\text{or}\quad |q_i|\ge K_*\mathcal R_i
 \quad\text{or}\quad m_i\le\gamma_*|q_i|,
\]
up to the separate regularity exceptions whose probability tends to zero.
The high-effective-rank branch handles operator-gap modes with \(r_i\ge r_*\); the new load estimate is needed only where \(r_i<r_*\).
There is no assumed implication between the old dominant branch and the new operator-gap branch.

The error \(o(1)\) is unconditional at the fixed-law, dimension-wise scope, with no summability asserted.
The average of \(\mathcal B_i\), including singular minors and the remaining comparable-mode regime, has not been shown to vanish.
Thus this is a probability reduction, not an unconditional polynomial least-value floor or a determinant/logarithmic theorem.

<a id="inputs"></a>
## Exact fixed inputs and extraction scope

The [actual closest-mode cross-energy theorem](Yin_C_F0187_v5.md#actual-cross-energy-statement) supplies
\(\sigma(s_4)^2\ge c_{\rm cross}E_F^2/N^4\) with fixed \(c_{\rm cross}>0\), in its uniform unconditional invertible-branch sense.
The polynomials and their exact decomposition are defined again below.
The [physical projector estimate](Yin_C_F0187_v4.md#fresh-row-projector), its weighted minor-mass input, and the [spectral residual proof](Yin_C_F0187_v4.md#spectral-residual-spread) supply closest-mode leverage, residual physical row spread, norm guards, and the large-\(|q|\) and residual-size conditions used in the probability assembly.
Their original bounded laws and \(N^{-1/2}\) normalization match the present model.

The fixed [pole coefficient bounds](Yin_C_F0194_v13.md#dominant-coefficients) supply the residual row-load estimate before any dominance assumption.
Its [graph-area identity](Yin_C_F0194_v13.md#pole-area) and [general conditional bridge](Yin_C_F0194_v13.md#statement) are used only for the matrix consequence.
The same proof's [dominant probability assembly](Yin_C_F0194_v13.md#dominant-probability-assembly) retains the old \(K_*\) branch with its matched graph scale.
The [whole-layer theorem](Yin_C_F0187_v6.md#statement) supplies the old \(r_*\) branch; its use and graph scale are exactly those in the fixed [combined assembly](Yin_C_F0194_v13.md#combined-probability-assembly).
Both C187v6 and C194v13 have their selected proved decisions at [whole-layer-rank-reviewed](Yin_C_F0187_v6.md#decision-whole-layer-rank-reviewed) and [graph-energy-reviewed](Yin_C_F0194_v13.md#decision-graph-energy-reviewed).
Those reviews do not certify this new version.

The extraction source is [D33's mixed-inner-product development](../drafts/Yin_D_F0033.md#spectral-gap-cross-orthogonality).
That rolling draft is provenance only, not a proof dependency.
The mixed coefficient proof below is self-contained finite-dimensional algebra; no new external source or novelty claim is used.

<a id="argument"></a>
## Complete candidate argument

<a id="mixed-fourth-inner-product"></a>
### A mixed inner product with one rank-two quadratic form

For real symmetric \(n\)-by-\(n\) matrices \(A,B\), define
\[
 \mathcal Q_N(A,B):=\Pi_4[(x^TAx)(x^TBx)],
 \qquad x_i=\varepsilon_i/\sqrt N.
\]
The inner product is the sum of products of fourth Walsh coefficients.
Let \(U:=(ab^T+ba^T)/2\), where \(\|a\|,\|b\|\le1\).
Suppose real symmetric \(A,B,C\) satisfy
\[
 \max\{\|A\|,\|B\|,\|C\|\}\le m,\qquad
 \max\{\|A\|_{\rm F},\|B\|_{\rm F},\|C\|_{\rm F}\}\le R,\qquad
 0<m\le R.
\]
Then there is an absolute \(C_0\) such that
\[
 |\langle\mathcal Q_N(U,A),\mathcal Q_N(B,C)\rangle|
 \le C_0mR^2/N^4.
 \tag{Mixed-fourth-inner-product}
\]
This estimate needs neither positivity nor orthogonality among the matrices.

Remove the diagonals and denote the resulting matrices by tildes.
A diagonal quadratic form is constant on the sign cube, so it cannot contribute to either fourth layer.
The nuclear norm, denoted by \(\|\cdot\|_*\), is the sum of singular values.
The rank-one decomposition of \(U\) gives \(\|U\|_*\le\|a\|\|b\|\le1\), while its diagonal has nuclear norm \(\sum_i|a_i b_i|\le1\).
Therefore
\[
 \|\widetilde U\|_*\le2,\qquad \|\widetilde U\|_{\rm F}\le2.
\]
Each of \(\widetilde A,\widetilde B,\widetilde C\) has operator norm at most \(2m\) and Frobenius norm at most \(R\).
We use the elementary inequality \(|\operatorname{Tr}(VD)|\le\|V\|_*\|D\|\), obtained by expanding a singular-value decomposition of \(V\) into rank-one matrices and bounding each unit-vector matrix coefficient of \(D\).

For four distinct indices forming a set \(I\), the exact coefficient is
\[
 (\mathcal Q_N(A,B))_I
 =\frac4{N^2}\sum_{e\sqcup f=I}(A_eB_f+A_fB_e),
 \tag{Product-fourth-coefficient}
\]
where the sum runs over its three unordered partitions into coordinate edges.
This follows by expanding \(x^TAx\): its off-diagonal sign coefficient is \(2A_{ij}/N\).
In the product of the two fourth-coefficient expressions, equal pairings give pairs of edge inner products, and different pairings give four-cycles.
There are only finitely many assignments, independently of \(n,N\).

For an equal pairing, the unrestricted edge sum is a fixed numerical multiple of
\[
 \langle\widetilde U,\widetilde B\rangle_{\rm F}
       \langle\widetilde A,\widetilde C\rangle_{\rm F}
\]
or the expression with \(B,C\) interchanged.
Its modulus is at most \(C mR^2\), by the nuclear/operator bound on the first factor and Cauchy--Schwarz on the second.
Removing pairs of edges sharing a vertex costs at most a fixed multiple of terms of the form
\[
 \begin{split}
 &\sum_i\left(\sum_j|\widetilde U_{ij}\widetilde B_{ij}|\right)
           \left(\sum_k|\widetilde A_{ik}\widetilde C_{ik}|\right)\\
 &\qquad\le4m^2\sum_{i,j}|\widetilde U_{ij}\widetilde B_{ij}|
 \le4m^2\|\widetilde U\|_{\rm F}\|\widetilde B\|_{\rm F}
 \le8m^2R.
 \end{split}
 \tag{Shared-vertex-mixed-bound}
\]
Permuting the three residual matrices gives the other assignments.
The equal-edge case is included in this nonnegative bound.

For a different pairing, the unrestricted cycle sum is a trace of a product containing \(\widetilde U\) and the other three matrices.
Its modulus is at most \(C m^3\), by the nuclear norm of \(\widetilde U\).
Adjacent vertex coincidences vanish because all diagonals are zero.
For a cycle \(\widetilde U_{ij}V_{jk}W_{kl}D_{li}\), the coincidence \(i=k\) yields
\[
 \sum_i\left(\sum_j|\widetilde U_{ij}V_{ji}|\right)
        \left(\sum_l|W_{il}D_{li}|\right),
\]
and the coincidence \(j=l\) gives the same form with \(V,D\) interchanged.
Here \(V,W,D\) are the three residual matrices in some order.
Both sums satisfy (Shared-vertex-mixed-bound); their intersection is bounded by the same nonnegative sum.
Thus exclusion of repeated vertices costs at most \(C m^2R\).
Since \(m\le R\), all terms are bounded by \(C mR^2\).
The product of the coefficient factors contributes \(16/N^4\), absorbed in \(C_0\), proving (Mixed-fourth-inner-product).

<a id="operator-gap-coefficients"></a>
### Full-layer energy and the load bound

For the actual decomposition \(Z=qww^T+E\), define
\[
 s(x):=(u^Tx)^2(x^TJ_0x)+(v^Tx)^2(x^TFx)
           -2(u^Tx)(v^Tx)(x^TT_0x),
\]
\[
 e(x):=(x^TFx)(x^TJ_0x)-(x^TT_0x)^2,\qquad
 s_4:=\Pi_4s,\qquad e_4:=\Pi_4e.
\]
The full inverse blocks are \(G=quu^T+F\), \(J=qvv^T+J_0\), and \(T=q(uv^T+vu^T)/2+T_0\).
The \(q^2\) term cancels identically, so
\[
 p_4=q s_4+e_4.
 \tag{Full-fourth-decomposition}
\]
Apply the mixed lemma to the three terms of \(s_4\) and the two terms of \(e_4\), using \(U=uu^T,vv^T,(uv^T+vu^T)/2\).
The vectors \(u,v\) have norms at most one.
All residual blocks and \(T_0\) have operator norm at most \(m_E\) and Frobenius norm at most \(E_F\).
Thus
\[
 |\langle s_4,e_4\rangle|\le C_1m_E E_F^2/N^4
 \tag{Cross-residual-inner-product}
\]
for an absolute \(C_1>0\).
This is a bound on the actual sign coefficients, with repeated indices removed.

Outside the uniform bad event from the fixed cross-energy theorem,
\[
 \begin{split}
 \sigma_4^2
 &=q^2\sigma(s_4)^2+2q\langle s_4,e_4\rangle+\sigma(e_4)^2\\
 &\ge(c_{\rm cross}q^2-2C_1|q|m_E)E_F^2/N^4.
 \end{split}
\]
Choose
\[
 \gamma_*:=\min\{1/2,c_{\rm cross}/(4C_1)\},
 \qquad c_{\rm gap}:=c_{\rm cross}/2.
\]
On \(m_E\le\gamma_*|q|\), this proves (Operator-gap-energy).

For coordinate \(j\), define
\[
 \eta_j:=u_j^2+v_j^2,\qquad
 \rho_j:=\sum_{k\ne j}(F_{jk}^2+(J_0)_{jk}^2+(T_0)_{jk}^2),
\]
\[
 \mathcal R^2:=\|\operatorname{off}F\|_{\rm F}^2+
     \|\operatorname{off}J_0\|_{\rm F}^2+
     \|\operatorname{off}T_0\|_{\rm F}^2.
\]
Then \(\mathcal R^2\le E_F^2\) and \(\rho_j\le d_j(E):=\|P_jE\|_{\rm F}^2\), where \(P_j\) is the rank-two projection onto physical coordinate \(j\) in the two auxiliary channels.
The fixed pole coefficient bound, which precedes its dominant-mode specialization, gives
\[
 L_j(p_4)\le\frac C{N^4}
      \bigl(q^2\eta_j\mathcal R^2+(q^2+\mathcal R^2)\rho_j\bigr).
\]
That bound is a deterministic coefficient calculation for any physical size \(n\) and normalizing parameter \(N\); its proof uses no relation \(n=N-1\).
It therefore also applies to the formal full-size probe here.
Dividing by the operator-gap energy lower bound yields
\[
 \tau_4\le C_{c_{\rm cross}}\left[
    \max_j\eta_j+
    \left(1+\frac{E_F^2}{q^2}\right)
              \frac{\max_j d_j(E)}{E_F^2}\right].
 \tag{Operator-gap-coordinate-load}
\]
On \(r_Z\le K\), the parenthesis is at most \(K\).
The fixed closest-mode leverage and residual physical row-spread conclusions make both terms tend to zero, uniformly over all invertible minors and all closest-mode choices.
Combining their bad events with the cross-energy bad event proves (Operator-gap-load).
Every use is unconditional and intersected with invertibility, and involves no inverse-norm truncation.

<a id="three-branch-proof"></a>
### The matrix bridge with the original two branches retained

For each physical index \(i\), use the conditioning
\(\mathcal F_i:=\sigma(W_2,W_1^{(i)},(W_1)_{ii})\) from the fixed general bridge.
The residual first-input row remains a vector of independent fair signs.
The chosen eigenmode, all three branch tests, and the coefficient scales depend on the minor and hence are \(\mathcal F_i\)-measurable.
A Borel choice may be made by ordering eigenvalues, fixing a tie rule, and taking the first nonzero coordinate projection onto the selected eigenspace; the fixed inputs are uniform over this choice.

Use the fixed norm event to choose \(b_0\ge1\) with
\(\mathbb P\{\|L_N\|>b_0\}\le Ce^{-cN}\).
Bounded raw laws give a deterministic \(B_0\) such that every conditional boundary matrix \(\mathcal B_i(\varepsilon)\) has norm at most \(B_0\), uniformly over all remaining first-row signs.
The retained minor norm bound \(\|M_i\|\le b_0\) is \(\mathcal F_i\)-measurable.
Any failure of this bound for a minor is contained in the full norm exception.

For the new branch, the fixed minor spectral mass and residual divergence imply
\[
 |q_i|\ge1,\qquad E_{F,i}\ge1
\]
outside a uniform \(o(1)\) bad event on invertible minors.
The fixed graph-area bound gives, for
\(\Gamma_i:=I_2+\mathcal B_i^TZ_i^2\mathcal B_i\),
\[
 \begin{split}
 \sup_{\varepsilon}\sqrt{\det\Gamma_i(\varepsilon)}
 &\le C_{B_0}(1+|q_i|)(1+m_i)\\
 &\le C_{\rm gap}'\,|q_i|E_{F,i}.
 \end{split}
 \tag{Operator-gap-graph-scale}
\]
This uses \(m_i\le E_{F,i}\), not Frobenius dominance.
On the operator-gap branch, (Operator-gap-energy) gives the matching coefficient scale
\[
 \sigma_{4,i}\ge\sqrt{c_{\rm gap}}\,|q_i|E_{F,i}/N^2.
\]

Choose one deterministic \(t_N\to0\), enlarged to be at least \(N^{-1/2}\), slowly enough for the two old load estimates and (Operator-gap-load) with \(K:=\max\{1,r_*\}\).
Define good conditioning events as follows.
Let \(\mathcal G_i^{\rm high}\) and \(\mathcal G_i^{\rm dom}\) be the minor-measurable good events in the fixed combined assembly, with this common cutoff and the same original \(r_*,K_*\).
They retain the norm guard and their respective energy/load and graph-scale conditions.
Let \(\mathcal G_i^{\rm gap}\) impose invertibility,
\[
 \|M_i\|\le b_0,\qquad r_i<r_*,\qquad m_i\le\gamma_*|q_i|,
 \qquad |q_i|\ge1,\qquad E_{F,i}\ge1,
\]
together with the new energy lower bound and \(\tau_{4,i}\le t_N\).
No first-row-dependent norm condition is used in defining these good events.

Set \(\mathcal G_i:=\mathcal G_i^{\rm high}\cup\mathcal G_i^{\rm dom}\cup\mathcal G_i^{\rm gap}\).
Give the old high branch first priority and the old dominant branch second priority, and choose
\[
 a_i:=
 \begin{cases}
 C_{\rm high}\|Z_i\|_{\rm F}^2,
   &\text{on }\mathcal G_i^{\rm high},\\
 C_{\rm dom}|q_i|\mathcal R_i,
   &\text{on }\mathcal G_i^{\rm dom}\setminus\mathcal G_i^{\rm high},\\
 C_{\rm gap}'|q_i|E_{F,i},
   &\text{on }\mathcal G_i^{\rm gap}
       \setminus(\mathcal G_i^{\rm high}\cup\mathcal G_i^{\rm dom}).
 \end{cases}
 \tag{Three-branch-graph-scale}
\]
Here \(C_{\rm high},C_{\rm dom}\) are adequate fixed graph constants from the old assembly, and \(C_{\rm gap}'\) is adequate for (Operator-gap-graph-scale).
Assign any positive value outside \(\mathcal G_i\).
These scales are measurable and need no inverse-norm bound.
On the union, the graph area, energy and load conditions of C194v13 hold with one \(\kappa_0>0\), the minimum of the three fixed positive coefficient-to-area ratios.

If \(M_i\) is invertible and the regularity conditions hold, failure of the union requires failure of all three branch tests.
Indeed, \(r_i\ge r_*\) enters the high branch, \(|q_i|\ge K_*\mathcal R_i\) enters the old dominant branch, and the remaining case \(r_i<r_*,m_i\le\gamma_*|q_i|\) enters the new branch.
Consequently
\[
 \frac1N\sum_{i=1}^N\mathbb P(\mathcal G_i^c)
 \le \frac1N\sum_{i=1}^N\mathbb P(\mathcal B_i)+o(1).
 \tag{Three-branch-average}
\]
The additional errors are uniform \(o(1)\) probabilities from the fixed inputs and the new operator-gap statements.
No independence across physical indices is used.

Apply the fixed general graph-energy bridge with \(b_N=b_0\).
Its matching error \(C\sqrt{\log r_N}\,r_N^{-1/17}\), with \(r_N:=\lfloor(16t_N)^{-1}\rfloor\), tends to zero.
Adding the exponentially small full norm exception proves the asserted \(L_N\) bound at scale \(cN^{-5}\).
The fixed quadratic conversion in C194v13 gives \(s_{\min}(Q_N)\ge s_{\min}(L_N)\), including simultaneous singularity, so it yields (Three-branch-matrix-reduction).
This uses the same measurable union and scales rather than attempting to subtract a new branch from an old probability inequality.

<a id="remaining-boundary"></a>
## Remaining mathematical boundary

The matrix reduction preserves the previously covered high-effective-rank and dominant-mode regions and additionally covers the operator-gap region.
The new coefficient energy lower bound requires no bound on the largest inverse eigenvalue or on the residual Frobenius norm relative to it.
Its probability of occurrence is not established.

The remaining invertible minors fail all three branch tests, so their effective inverse rank is bounded and at least two absolute inverse eigenvalues are comparable at the fixed \(\gamma_*\) scale.
Bounded effective rank does not by itself imply negligible Frobenius tail after retaining finitely many eigenmodes.
Their signed pair contributions and any diffuse residual energy still require control.
No vanishing estimate is proved for the remaining average or for singular minors.
The \(o(1)\) error is not summable, and even a polynomial least-value floor would leave the applicable intermediate and bottom logarithmic obligations.
The arbitrary matrix-coefficient, full finite-second-moment and Brown-measure Tasks remain unresolved by this version.

## Current assessment

[Selected decision](#decision-operator-gap-candidate)

## Assessment history

### Decision operator-gap-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T20:44 |
| status | open |
| reason | Complete candidate mixed fourth-Walsh inner-product proof, operator-gap energy and bounded-effective-rank load estimates, and a measurable three-branch matrix probability reduction preserving the original high-rank and dominant thresholds. Independent checking of the coefficient normalization, collision bounds, fixed-input interfaces and probability assembly remains required before adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact operator-gap conclusions and three-branch consequence](#statement) | Bounded real two-channel model, all full or single-deletion minors and closest-mode choices; formal sign energy, load with a fixed effective-rank bound, and the Rademacher first-input matrix reduction with explicit remaining minor average. |
| argument | [Complete candidate proof](#argument) | Mixed coefficient inner-product bound, full-layer cancellation estimate, load interface, graph scale and measurable union of all three coefficient branches. |
| dependency | [Actual closest-mode cross-energy](Yin_C_F0187_v5.md#actual-cross-energy-statement) | Uniform cross fourth-layer squared coefficient norm at least c times residual squared Frobenius norm divided by N^4 on invertible bounded real minors. |
| dependency | [Residual physical row spread and norm/size controls](Yin_C_F0187_v4.md#spectral-residual-spread) | Uniform residual physical row energy, residual divergence and fixed norm event in the original-coordinate bounded real model. |
| dependency | [Closest-mode leverage and spectral mass](Yin_C_F0187_v4.md#fresh-row-projector) | Weighted minor mass and physical projector estimates give a closest eigenvalue tending to zero and vanishing leverage uniformly over all stated minors and mode choices. |
| dependency | [Fixed high-effective-rank whole-layer theorem](Yin_C_F0187_v6.md#statement) | The unchanged high-rank threshold and complete fourth-layer energy/load conclusion, used in the combined matrix consequence; its fresh-row identification also fixes the actual sign-border interpretation. |
| dependency | [Pole coefficient bounds and retained dominant threshold](Yin_C_F0194_v13.md#dominant-coefficients) | The pre-dominance residual row-load estimate and the existing dominant coefficient branch at its unchanged K_* threshold. |
| dependency | [General conditional matrix bridge](Yin_C_F0194_v13.md#statement) | Conditional graph-energy hypotheses and norm-guarded matrix reduction with matching error tending to zero. |
| dependency | [Largest-mode graph area](Yin_C_F0194_v13.md#pole-area) | Uniform graph area at most C times (1+abs(q))(1+residual operator norm), with no pole-dominance premise. |
| dependency | [Existing two-branch probability assembly](Yin_C_F0194_v13.md#combined-probability-assembly) | Minor-measurable high-rank and dominant good events, matched graph scales and uniform regularity exceptions, with their original thresholds retained in the new union. |
| dependency | [Original-input quadratic conversion](Yin_C_F0194_v13.md#dominant-probability-assembly) | The exact auxiliary-column swap and inverse-block identity give simultaneous singularity and s_min(Q_N) at least s_min(L_N). |
