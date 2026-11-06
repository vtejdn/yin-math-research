---
author: Yin
---

# Single-input row coefficients for the two-channel Wigner pencil

This continuing calculation was developed for Yin on 2026-11-05 for the [matrix-coefficient F0013 contract](../tasks/Yin_T_F0013_v1.md#contract).
It gives exact conditional coefficient formulas and deterministic diagnostics for the [typical-minor energy test](Yin_D_F0010.md#typical-minor-energy-matching).
The [bounded actual-minor singular atom](../ledger/Yin_L_F0066_v5.md#actual-minor-singular-atom) rules out a floor uniform over every conditioned actual minor; no such assertion is made here.
The coefficient calculations use elementary block inversion, determinant expansion and sign orthogonality.
Their probabilistic application now reuses the [reviewed bounded-model physical and residual spread theorem](../claims/Yin_C_F0187_v4.md#decision-bounded-two-channel-reviewed) at its exact two-channel scope; this does not give an independent review of the coefficient calculations below.
The coefficient-to-small-ball conversion remains the accepted [MNV16 interface](../audits/literature/MNV16/Yin_U001.md#matching-rank) used at the exact scope retained in D_F0010.
Fixed results now cover the high-effective-rank and dominant-mode energy branches and the graph-normalized matrix conversion; their remaining minor probabilities are unresolved.

<a id="single-input-schur"></a>
## Actual minor and exact quadratic Schur entries

Set \(\alpha=\sqrt2\), fix a nonzero real \(K\), put \(n=N-1\), and write the real symmetric inputs as
\[
 W=\begin{pmatrix}a&x^T\\x&C\end{pmatrix},\qquad
 B=\begin{pmatrix}b_0&b^T\\b&D\end{pmatrix},\qquad
 L_N=\begin{pmatrix}W+B&KI_N\\KI_N&W+\alpha B\end{pmatrix}.
\]
Condition on the full original second input \(B\), the first-input minor \(C\), and its diagonal entry \(a\).
The remaining original first-input row \(x\) is independent under this conditioning.
For the coefficient calculation on atomic support assume the first off-diagonal law is the symmetric sign law, so \(x_i=\varepsilon_i/\sqrt N\) with independent fair signs.
The raw polynomial identities preceding restriction to that support hold for every real \(x\).
There is no conditioning on either mixed factor \(W+B\) or \(W+\alpha B\).

After placing the two first physical coordinates together, the actual retained minor is
\[
 \mathcal M=\begin{pmatrix}X&KI_n\\KI_n&Y\end{pmatrix},
 \qquad X=C+D,\quad Y=C+\alpha D.
\]
On its invertible branch write
\[
 \mathcal M^{-1}=\begin{pmatrix}G&H\\H^T&J\end{pmatrix},
 \qquad G^T=G,\quad J^T=J,\quad T=(H+H^T)/2.
\]
Put \(u=x+b\) and \(v=x+\alpha b\).
Its two-by-two Schur complement is exactly
\[
 S(x)=\begin{pmatrix}
 a+b_0-u^TGu&K-u^THv\\
 K-u^THv&a+\alpha b_0-v^TJv
 \end{pmatrix},
 \qquad \det L_N=\det\mathcal M\det S(x).
 \tag{Single-Schur}
\]
The ordering change permutes rows and columns together, so it introduces no determinant sign.
No bound on \(\mathcal M^{-1}\) has been used in this identity.

Define
\[
 g=Gb,\qquad j=\alpha Jb,\qquad \ell=\alpha Hb+H^Tb,
\]
\[
 A=a+b_0-b^TGb,\qquad
 B_*=a+\alpha b_0-\alpha^2b^TJb,\qquad
 C_*=K-\alpha b^THb.
\]
The entries of \(S\) are the three quadratic polynomials
\[
 f(x)=A-2g^Tx-x^TGx,\qquad
 h(x)=B_*-2j^Tx-x^TJx,\qquad
 r(x)=C_*-\ell^Tx-x^TTx,
\]
and \(p(x):=\det S(x)=f(x)h(x)-r(x)^2\).
In particular its raw homogeneous degree-four part is
\[
 p^{\rm raw}_4(x)=(x^TGx)(x^TJx)-(x^TTx)^2.
 \tag{Raw-fourth}
\]
The conditioned background border \(b\) and both diagonal entries affect only lower raw degrees.
They do not alter the actual degree-four sign coefficients, although they can determine the true highest surviving degree after support restriction.

<a id="all-sign-layers"></a>
## All five layers after the exact sign restriction

For \(i<j\), write the three restricted quadratic polynomials as
\[
 f=f_0+\sum_i f_i\varepsilon_i+\sum_{i<j}f_{ij}\varepsilon_i\varepsilon_j,
\]
with analogous notation \(h_S,r_S\), where
\[
 \begin{array}{lll}
 f_0=A-N^{-1}\operatorname{Tr}G,&f_i=-2g_i/\sqrt N,&f_{ij}=-2G_{ij}/N,\\
 h_0=B_*-N^{-1}\operatorname{Tr}J,&h_i=-2j_i/\sqrt N,&h_{ij}=-2J_{ij}/N,\\
 r_0=C_*-N^{-1}\operatorname{Tr}T,&r_i=-\ell_i/\sqrt N,&r_{ij}=-2T_{ij}/N.
 \end{array}
 \tag{Quadratic-coefficients}
\]
Pair subscripts are unordered, and absent coefficients are zero.
Every repeated sign is removed using \(\varepsilon_i^2=1\).
Consequently the exact coefficient of \(\varepsilon_S\) in \(p\) is
\[
 p_S=\sum_{A'\triangle B'=S}
       (f_{A'}h_{B'}-r_{A'}r_{B'}),\qquad |A'|,|B'|\le2.
 \tag{Sign-convolution}
\]
Here the empty subscript denotes the constant coefficient, and \(\triangle\) is symmetric difference.
This is a direct product expansion, not an approximation that discards repeated indices.
It gives the following complete layer formulas.

For four distinct indices and \(S=\{i,j,k,l\}\), sum over its three unordered partitions into pairs \(e,e'\):
\[
 p_S=\sum_{e\sqcup e'=S}
       (f_eh_{e'}+f_{e'}h_e-2r_er_{e'}).
 \tag{Sign-fourth}
\]
For three distinct indices,
\[
 p_{ijk}=\sum_{a\in\{i,j,k\}}
 \bigl(f_a h_{\{i,j,k\}\setminus\{a\}}
       +h_a f_{\{i,j,k\}\setminus\{a\}}
       -2r_a r_{\{i,j,k\}\setminus\{a\}}\bigr).
 \tag{Sign-third}
\]
For two distinct indices,
\[
 \begin{split}
 p_{ij}={}&f_0h_{ij}+h_0f_{ij}-2r_0r_{ij}
        +f_i h_j+f_jh_i-2r_ir_j\\
 &+\sum_{k\notin\{i,j\}}
       (f_{ik}h_{jk}+f_{jk}h_{ik}-2r_{ik}r_{jk}).
 \end{split}
 \tag{Sign-second}
\]
The degree-one and constant terms are
\[
 p_i=f_0h_i+h_0f_i-2r_0r_i
       +\sum_{j\ne i}(f_jh_{ij}+f_{ij}h_j-2r_jr_{ij}),
 \tag{Sign-first}
\]
\[
 p_0=f_0h_0-r_0^2+\sum_i(f_i h_i-r_i^2)
                      +\sum_{i<j}(f_{ij}h_{ij}-r_{ij}^2).
 \tag{Sign-constant}
\]
These exhaust all possible symmetric differences of two sets of size at most two.
Orthogonality follows because the expectation of a product of independent signs is zero unless every exponent is even; hence distinct \(\varepsilon_S\) have zero inner product.
Thus the squared coefficient sums are exactly their sign-space squared norms, and not Gaussian polynomial norms before support reduction.

<a id="fourth-energy-row-load"></a>
## Fourth-layer energy and a deterministic coordinate-load bound

For \(S=\{i,j,k,l\}\) with distinct indices, define
\[
 \Theta_S=\sum_{e\sqcup e'=S}
       (G_eJ_{e'}+J_eG_{e'}-2T_eT_{e'}),
 \qquad p_S=\frac4{N^2}\Theta_S.
 \tag{Pairing-tensor}
\]
The notation \(G_{\{a,b\}}=G_{ab}\) is used only for distinct indices.
Set
\[
 \mathcal E_4=\sum_{|S|=4}|\Theta_S|^2,\qquad
 \sigma_4^2=\frac{16}{N^4}\mathcal E_4,
 \qquad
 L_i^{(4)}=\sum_{\substack{|S|=4\\i\in S}}|p_S|^2.
\]
When \(\mathcal E_4>0\), its normalized maximum load is
\(\tau_4=\max_iL_i^{(4)}/\sigma_4^2\).
If \(\mathcal E_4=0\), there is no fourth layer and the lower layers above must be tested instead.

For a real symmetric matrix \(Z\), put
\[
 E(Z)=\sum_{a<b}|Z_{ab}|^2,\qquad
 \ell_i(Z)=\sum_{a\ne i}|Z_{ia}|^2.
\]
Expanding the three pairings gives six \(GJ\) products and three \(-2TT\) products.
The elementary inequality \(|\sum_{a=1}^9z_a|^2\le9\sum_{a=1}^9|z_a|^2\) therefore gives
\[
 \boxed{\quad
 L_i^{(4)}\le\frac{144}{N^4}
   \bigl(\ell_i(G)E(J)+\ell_i(J)E(G)
                          +4\ell_i(T)E(T)\bigr).
 \quad}
 \tag{Fourth-load}
\]
Indeed, in each product the fixed index \(i\) occurs in one of its two edges.
Summing over its partner bounds that edge's squared entries by the corresponding \(\ell_i\), and summing over the disjoint other edge is bounded by \(E\).
Removing the distinctness restrictions only increases these nonnegative sums.
Each \(TT\) product occurs once with the edge containing \(i\), while the two possible \(GJ\) assignments give the first two terms.
This proves the bound without an entrywise delocalization assumption or a random-matrix estimate.

Since \(E(Z)\le\|Z\|_{\rm F}^2/2\) and \(\ell_i(Z)\le\|Z\|^2\), it implies
\[
 L_i^{(4)}\le\frac{C}{N^4}
       \|\mathcal M^{-1}\|^2\|\mathcal M^{-1}\|_{\rm F}^2
 \tag{Fourth-load-coarse}
\]
with a numerical constant \(C\).
The block norms and the norm of \(T\) are at most \(\|\mathcal M^{-1}\|\), and
\(\|G\|_{\rm F}^2+\|J\|_{\rm F}^2+\|T\|_{\rm F}^2
\le\|\mathcal M^{-1}\|_{\rm F}^2\), which verifies this last substitution.

A concrete conditional consequence is the following.
If \(\|\mathcal M^{-1}\|\le M\) and \(\sigma_4^2\ge cN^{-2}\) for constants \(M,c>0\), then
\[
 \tau_4\le\frac{C M^4}{cN},
 \tag{Bounded-inverse-load}
\]
because \(\|\mathcal M^{-1}\|_{\rm F}^2\le2nM^2\).
On this branch a fourth-layer energy lower bound already supplies the required load decay; it is unnecessary to prove a separate entrywise spread statement.
This does not say that a bounded inverse is a typical event at a spectral parameter in the limiting bulk.
No such assertion follows from the existing weak or mesoscopic interfaces.

More generally, (Fourth-load) is useful when inverse norms grow but individual row energies remain spread.
For example, an explicitly proved bound
\(\mathcal E_4\ge c\|\mathcal M^{-1}\|_{\rm F}^4\)
would give from the coarse version
\[
 \tau_4\le\frac{C}{c}\,
 \frac{\|\mathcal M^{-1}\|^2}{\|\mathcal M^{-1}\|_{\rm F}^2}.
\]
Neither that noncancellation bound nor divergence of the displayed effective rank is assumed to hold for actual minors.
The distinct-mode section below shows why this particular energy normalization can be inappropriate when one inverse mode dominates.

<a id="offdiagonal-gram-test"></a>
## A finite off-diagonal Gram test in the bounded-inverse regime

There is a further deterministic reduction of the fourth energy.
Let \(A=\operatorname{off}(G)\), \(B_1=\operatorname{off}(J)\), and \(C_1=\operatorname{off}(T)\), where \(\operatorname{off}\) sets the diagonal to zero without changing other entries.
These are real symmetric zero-diagonal matrices, and let
\(\kappa=\max\{\|A\|,\|B_1\|,\|C_1\|\}\).
Use the real Frobenius inner product \(\langle U,V\rangle_{\rm F}=\operatorname{Tr}(U^TV)\), and put
\[
 \begin{split}
 \mathcal G={}&\|A\|_{\rm F}^2\|B_1\|_{\rm F}^2
        +\langle A,B_1\rangle_{\rm F}^2
        +2\|C_1\|_{\rm F}^4\\
       &-4\langle A,C_1\rangle_{\rm F}
                    \langle B_1,C_1\rangle_{\rm F}.
 \end{split}
\]
Then, uniformly over these matrices and the dimension,
\[
 \left|\sigma_4^2-\frac4{N^4}\mathcal G\right|
       \le \frac{C n\kappa^4}{N^4}
 \tag{Fourth-Gram}
\]
for a numerical constant \(C\).
The expression \(\mathcal G\) is nonnegative: it equals twice the squared Hilbert-space tensor norm of
\(\tfrac12(A\otimes B_1+B_1\otimes A)-C_1\otimes C_1\), with the Frobenius inner product on each matrix factor.
This tensor expression describes a coefficient-space norm, not multiplication of the matrices.

The [fixed coefficient expansion](../claims/Yin_C_F0187_v6.md#rank-refined-four-cycle-error) gives the stronger deterministic error \(C\kappa^2B_\Sigma^2/N^4\), where \(B_\Sigma^2:=\|A\|_{\rm F}^2+\|B_1\|_{\rm F}^2+\|C_1\|_{\rm F}^2\).
This algebra applies to arbitrary real symmetric \(G,J,T\), independently of the probability model used later in that Claim.
Since \(B_\Sigma^2\le3n\kappa^2\), it also proves the displayed norm-only error.
That fixed proof retains every pairing, shared-vertex and four-cycle contribution.

For example, if \(\kappa\) stays bounded and the normalized Gram entries
\[
 \gamma_{UV}=n^{-1}\langle U,V\rangle_{\rm F},
 \qquad U,V\in\{A,B_1,C_1\},
\]
have limits for which
\[
 \gamma_{AA}\gamma_{B_1B_1}+\gamma_{AB_1}^2
       +2\gamma_{C_1C_1}^2
       -4\gamma_{AC_1}\gamma_{B_1C_1}>0,
 \tag{Noncollapsed-Gram}
\]
then \(\sigma_4^2\ge cN^{-2}\) eventually.
Together with a bounded inverse this gives \(\tau_4=O(N^{-1})\) by (Bounded-inverse-load).
A probabilistic version requires these conditions outside a separately controlled exceptional set; it is not supplied by the deterministic identity.

The missing information is sharper than a generic appeal to inverse delocalization.
For instance
\[
 \langle\operatorname{off}(G),\operatorname{off}(J)\rangle_{\rm F}
   =\operatorname{Tr}(GJ)-\sum_iG_{ii}J_{ii}.
\]
Thus even an available limit for the normalized full trace still leaves the coordinate-diagonal product and the noncancellation in (Noncollapsed-Gram) to justify.
The six real normalized Gram entries, with their actual inverse normalization and diagonal subtractions, provide a concrete next diagnostic.
If \(\kappa\) grows, the error in (Fourth-Gram) remains valid but need not be negligible relative to \(\mathcal G\); one cannot silently use the bounded-inverse consequence in that regime.

<a id="distinct-inverse-modes"></a>
## Only distinct inverse modes contribute to the raw fourth degree

Let \(\lambda_a\) be the nonzero eigenvalues of the real symmetric \(\mathcal M\), with orthonormal real eigenvectors \(w_a=(u_a,v_a)\in\mathbb R^n\oplus\mathbb R^n\).
For the row map
\[
 R_x=\begin{pmatrix}x^T&0\\0&x^T\end{pmatrix},\qquad
 z_a(x)=\binom{u_a^Tx}{v_a^Tx},
\]
one has
\[
 R_x\mathcal M^{-1}R_x^T
       =\sum_a\lambda_a^{-1}z_a(x)z_a(x)^T.
\]
Expanding its two-by-two determinant and grouping the terms with indices \(a,b\) and \(b,a\) gives exactly
\[
 p^{\rm raw}_4(x)=
 \sum_{a<b}\frac{
   \bigl((u_a^Tx)(v_b^Tx)-(u_b^Tx)(v_a^Tx)\bigr)^2}
                   {\lambda_a\lambda_b}.
 \tag{Distinct-mode-pairs}
\]
The terms with equal indices cancel individually.
This is the two-dimensional determinant expansion; no additional external exterior-power theorem is needed.
The coefficients \((\lambda_a\lambda_b)^{-1}\) can have different signs, since the actual pencil need not be positive definite.
Therefore the formula supplies no positivity lower bound on \(\mathcal E_4\) by itself.
Its purpose is to identify the actual pairs of inverse modes and their possible cancellations.

In particular, replacing \(\mathcal M^{-1}\) by a rank-one term \(qww^T\), with \(w=(u,v)\), gives
\[
 G=quu^T,\qquad J=qvv^T,\qquad
 T=\tfrac q2(uv^T+vu^T),
 \qquad p^{\rm raw}_4(x)=0
\]
for every \(x\).
This rank-one term is a component or approximation of an actual inverse, not itself the inverse of a full-size nonsingular minor.
If \(\mathcal M^{-1}=qww^T+E\) with \(\|w\|=1\), put \(F=R_xER_x^T\) and \(z=R_xw\).
The direct two-by-two identity
\(\det(F+qzz^T)=\det F+qz^T\operatorname{adj}(F)z\)
and \(\|\operatorname{adj}(F)\|=\|F\|\) yield
\[
 |p^{\rm raw}_4(x)|
 \le\bigl(\|E\|^2+|q|\|E\|\bigr)\|x\|^4.
 \tag{One-pole-cancellation}
\]
There is no \(q^2\) term.
Thus normalization solely by the square of the largest inverse mode can manufacture a vanishing quartic energy even when the next mode is the relevant scale.
A viable matrix-distance normalization must retain these distinct-mode products, the determinant of the conditioned minor and the actual graph factors.
The present algebra does not perform that matrix-event conversion.

<a id="single-pole-residual-test"></a>
## A single-pole normalization using only the residual off-diagonal blocks

The [distinct-mode expansion](#distinct-inverse-modes) admits a sharper conditional energy/load test when one inverse mode is large.
Write
\[
 \mathcal M^{-1}=qww^T+\mathsf E,\qquad
 w=\binom uv,\quad \|w\|=1,\quad q\in\mathbb R,
 \qquad
 \mathsf E=\begin{pmatrix}F&H_0\\H_0^T&J_0\end{pmatrix},
 \quad T_0=(H_0+H_0^T)/2.
\]
One may choose \(q\) and \(w\) from an eigenmode of the actual inverse, in which case \(\mathsf Ew=0\); the following algebra does not need that extra identity.
For each polynomial in \(x\), let \(\Pi_4\) denote its degree-four sign component after the exact substitution \(x_i=\varepsilon_i/\sqrt N\).
Set
\[
 s(x)=(u^Tx)^2(x^TJ_0x)+(v^Tx)^2(x^TFx)
                   -2(u^Tx)(v^Tx)(x^TT_0x),
\]
\[
 e(x)=(x^TFx)(x^TJ_0x)-(x^TT_0x)^2,
 \qquad s_4=\Pi_4s,\quad e_4=\Pi_4e.
\]
The rank-one square cancels identically, so the fourth layer of the full Schur determinant satisfies
\[
 \Pi_4p=q s_4+e_4.
 \tag{Pole-layer-decomposition}
\]
All lower raw degrees of the full Schur determinant have sign degree at most three and hence do not change this equality.

Define the residual scale and coordinate energies by
\[
 \begin{split}
 \mathcal R^2={}&\|\operatorname{off}(F)\|_{\rm F}^2
       +\|\operatorname{off}(J_0)\|_{\rm F}^2
       +\|\operatorname{off}(T_0)\|_{\rm F}^2,\\
 \rho_i={}&\sum_{j\ne i}(|F_{ij}|^2+|(J_0)_{ij}|^2+|(T_0)_{ij}|^2),
 \qquad \eta_i=u_i^2+v_i^2.
 \end{split}
\]
Then \(\sum_i\rho_i=\mathcal R^2\) and \(\sum_i\eta_i=1\).
Only off-diagonal residual entries enter this scale: on the sign cube the diagonal part of every quadratic form is the constant \(N^{-1}\operatorname{Tr}\), and its product with another quadratic form has degree at most two.
Consequently a diagonal term cannot contribute to any fourth coefficient in either \(s_4\) or \(e_4\).
This is a support identity, not a claim that a large diagonal inverse is negligible for the other layers or the matrix distance.

For a fourth-layer sign polynomial \(h_4=\sum_{|S|=4}h_S\varepsilon_S\), write
\[
 \sigma(h_4)^2=\sum_{|S|=4}|h_S|^2,\qquad
 L_i(h_4)=\sum_{\substack{|S|=4\\i\in S}}|h_S|^2.
\]
There are universal constants for which
\[
 \begin{split}
 L_i(s_4)&\le\frac C{N^4}(\eta_i\mathcal R^2+\rho_i),\\
 L_i(e_4)&\le\frac C{N^4}\rho_i\mathcal R^2,\qquad
 \sigma(e_4)\le\frac{C_0\mathcal R^2}{N^2},\\
 L_i(\Pi_4p)&\le\frac C{N^4}
       \left(q^2\eta_i\mathcal R^2+(q^2+\mathcal R^2)\rho_i\right).
 \end{split}
 \tag{Pole-load-bounds}
\]
No bound on \(|q|\) is imposed.

The complete [fixed coefficient proof](../claims/Yin_C_F0194_v13.md#dominant-coefficients) retains these load estimates, the residual fourth norm and their exact independent-sign normalization.
The displayed formulas remain here as the interface used by the continuing spectral-gap calculation.

Here is a precise sufficient condition retaining the unbounded pole.
Assume \(\mathcal R>0\), fix \(c>0\), and suppose
\[
 \sigma(s_4)^2\ge\frac{c\mathcal R^2}{N^4},\qquad
 |q|\ge K_c\mathcal R,\qquad
 K_c:=\max\{1,2C_0/\sqrt c\}.
 \tag{Pole-noncollapse}
\]
The sign-space triangle inequality in (Pole-layer-decomposition) then gives
\[
 \sigma_4:=\sigma(\Pi_4p)
 \ge |q|\sigma(s_4)-\sigma(e_4)
 \ge\frac{\sqrt c\,|q|\mathcal R}{2N^2}>0.
\]
Combining this with the last load bound gives
\[
 \tau_4\le\frac{C'}c
       \left(\max_i\eta_i+\frac{\max_i\rho_i}{\mathcal R^2}\right).
 \tag{Pole-load-decay}
\]
Thus a delocalized physical eigenvector and spread residual off-diagonal row energy suffice for vanishing fourth-layer load under the stated cross-energy and dominance conditions, even when \(|q|\) grows faster than every polynomial.
The dominance constant depends explicitly on the noncollapse constant; a fixed arbitrary lower bound on \(|q|/\mathcal R\) cannot replace it.
If \(\mathcal R=0\), both \(s_4\) and \(e_4\) vanish, and the fourth-layer route supplies nothing; a lower-degree test is required.

The coefficient lemma remains conditional on (Pole-noncollapse).
For \(K=1\), the [fixed bounded real two-channel theorem](../claims/Yin_C_F0187_v4.md#statement) now controls its two spread quantities for independent fixed bounded real Wigner inputs with the theorem's bounded centered diagonal laws, including zero diagonals and a Rademacher first input.
For a closest-to-zero real unit eigenmode \(w\), with \(q\) its inverse eigenvalue, it gives \(\max_i\eta_i\to0\), \(\max_i\rho_i/\mathcal R^2\to0\), and \(\mathcal R^2\ge c_*\|\mathsf E\|_{\rm F}^2>0\) in the stated probability sense, uniformly over all single physical minors with the original \(N^{-1/2}\) normalization.
These are bounds on bad events intersected with invertibility, averaged over both inputs; they neither establish invertibility with high probability nor give a uniform assertion for every frozen second input.
On the additional cross-energy and dominance event in (Pole-noncollapse), this supplies vanishing fourth-layer load through (Pole-load-decay).
The [reviewed actual cross-energy theorem](../claims/Yin_C_F0187_v5.md#actual-cross-energy-statement) now supplies the lower bound on \(\sigma(s_4)\) with probability tending to one in this bounded model, using the inverse mode, residual blocks and actual pencil identities.
The probability of failure of \(|q|\ge K_c\mathcal R\), or another treatment of comparable inverse modes, still requires control before integrating this whole-layer sign small-ball argument.
The [fixed graph-area calculation](../claims/Yin_C_F0194_v13.md#pole-area) now matches the scale \(|q|\mathcal R\) to the actual distance normalization under the stated bounded-model size conditions.
The six-Gram bounded-inverse branch above remains available at its own hypotheses.

<a id="auxiliary-mode-transversality"></a>
## Distinct large modes can still share one auxiliary direction

Even the product of the two largest inverse singular values need not be the relevant raw fourth scale.
For a deterministic two-channel-form test let \(P\) be an orthogonal projection of rank at least two, \(0<\varepsilon<1\), \(K=1\), \(D=0\), and
\[
 C_\varepsilon=(\varepsilon-1)P,\qquad
 \mathcal M_\varepsilon=
    \begin{pmatrix}C_\varepsilon&I\\I&C_\varepsilon\end{pmatrix}.
\]
The symmetric and antisymmetric auxiliary channels give
\[
 U_\varepsilon=(C_\varepsilon+I)^{-1}
        =(I-P)+\varepsilon^{-1}P,
 \qquad
 V_\varepsilon=(C_\varepsilon-I)^{-1}
        =-(I-P)+(\varepsilon-2)^{-1}P.
\]
Thus \(\|\mathcal M_\varepsilon\|\le2\), and at least two different inverse modes have magnitude \(\varepsilon^{-1}\).
Their pair product is \(\varepsilon^{-2}\), but they all lie in the same symmetric auxiliary channel, so their determinants in (Distinct-mode-pairs) vanish identically.
Indeed the inverse blocks are
\(G=J=(U_\varepsilon+V_\varepsilon)/2\) and
\(H=T=(U_\varepsilon-V_\varepsilon)/2\), whence
\[
 p^{\rm raw}_4(x)
   =(x^TU_\varepsilon x)(x^TV_\varepsilon x),\qquad
 |p^{\rm raw}_4(x)|\le\varepsilon^{-1}\|x\|^4.
\]
The two-largest-mode product therefore overestimates this raw fourth scale by a factor tending to infinity.
This is an exact deterministic diagnostic inside the algebraic pencil form, not a claim that these matrices are admitted or typical conditioned minors for a specified fixed entry law.
The mode-pair normalization has to retain auxiliary transversality as well as spectral magnitude.

<a id="inverse-block-identities"></a>
## Relations retained by the actual affine minor

The inverse blocks cannot be assigned independently.
Both products \(\mathcal M\mathcal M^{-1}=I\) and \(\mathcal M^{-1}\mathcal M=I\) imply
\[
 H=K^{-1}(I-GX),\qquad
 T=K^{-1}\bigl(I-(GX+XG)/2\bigr),\qquad
 J=K^{-2}(XGX-X).
 \tag{Actual-inverse-relations}
\]
For example \(GX+KH=I\) gives the first equality, and \(XH+KJ=0\) gives the third; no inverse of \(X\) is taken.
Consequently, writing \(q_Z=x^TZx\),
\[
 K^2p^{\rm raw}_4
 =q_Gq_{XGX}-q_{(GX+XG)/2}^2
       -q_Gq_X+2\|x\|^2q_{(GX+XG)/2}-\|x\|^4.
 \tag{Actual-fourth-rewrite}
\]
On the sign cube \(\|x\|^2=n/N\) is deterministic, so the last two terms have degree at most two after restriction.
The remaining fourth-layer question is therefore a precise cancellation problem in these actual inverse-block relations, not an unconstrained triple of quadratic forms.
For instance \(X=0\) forces \(H=T=K^{-1}I\) and \(J=0\), making the entire raw fourth part a multiple of \(\|x\|^4\) and eliminating its fourth sign layer.
This recovers the relevant collapse in the fixed actual-minor counterexample without importing its rare atom as a typical event.

<a id="spectral-information-boundary"></a>
## What coordinate-free spectral controls cannot determine

The following deterministic comparison isolates information missing from a conclusion stated only in terms of joint normalized traces and singular-value bounds.
It is not asserted to be a pair of typical Wigner minors, or a counterexample with the same original entry law.
The deterministic matrices need not lie in the support of the conditioned minor for a prescribed fixed entry law; only the claimed insufficiency of coordinate-free data is being tested.
Take \(n=2r\), \(N=n+1\), \(B=0\), \(a=0\), \(K=1\), and \(C=2R\), where \(R\) is a real symmetric involution.
Then
\[
 \mathcal M=\begin{pmatrix}2R&I\\I&2R\end{pmatrix},\qquad
 G=J=\frac23R,\qquad H=T=-\frac13I,
\]
and \(\|\mathcal M\|=3\), \(\|\mathcal M^{-1}\|=1\).
Compare
\[
 R_{\rm diag}=\bigoplus_{a=1}^r\begin{pmatrix}1&0\\0&-1\end{pmatrix},
 \qquad
 R_{\rm pair}=\bigoplus_{a=1}^r\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
They are orthogonally conjugate, block by block using
\(2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\).
Thus all joint normalized trace words in \(C,D=0\), all eigenvalues of their actual two-channel pencils, and the displayed norm and inverse bounds coincide.

For \(R_{\rm diag}\), the restricted form \(x^TRx\) is identically zero because each squared sign is one and \(\operatorname{Tr}R=0\).
Hence every nonconstant coefficient of \(p\), including its fourth layer, vanishes.
For \(R_{\rm pair}\), put \(Z_a=\varepsilon_{2a-1}\varepsilon_{2a}\) and \(g=2/3\).
Then \(x^TRx=2N^{-1}\sum_a Z_a\), and
\[
 p(\varepsilon)=\frac{4g^2}{N^2}
       \left(r+2\sum_{a<b}Z_aZ_b\right)
           -\left(1+\frac n{3N}\right)^2.
\]
The nonzero fourth coefficients are \(8g^2/N^2\), one for each union of two distinct coordinate pairs.
For \(r\ge2\),
\[
 \sigma_4^2=\frac{64g^4}{N^4}\binom r2,
 \qquad \tau_4=\frac2r=\frac4n.
 \tag{Same-spectra-different-layer}
\]
Thus one family has zero fourth layer, while the conjugate family has energy of order \(N^{-2}\) and vanishing maximum load.
Even every joint trace word and the complete pencil spectra do not determine these coefficients in the original independent-sign basis.
This comparison does not exclude a proof using the original Wigner independence together with those spectral controls; that extra coordinate-sensitive randomness is exactly what would have to be used.

<a id="auxiliary-gram-gap"></a>
## Fixed auxiliary Gram separation

The [reviewed bounded-model theorem](../claims/Yin_C_F0187_v5.md#decision-auxiliary-cross-energy-reviewed) now contains the complete [joint approximate-mode proof](../claims/Yin_C_F0187_v5.md#joint-gap-proof) and [all-eigenmode Gram argument](../claims/Yin_C_F0187_v5.md#gram-gap-proof).
Its probability conclusion is uniform over the full pencil and every single physical deletion, including singular matrices and arbitrary eigenspace choices.
The original normalization and fixed bounded real laws remain part of that theorem.

<a id="cross-layer-kernel"></a>
## Fixed generic cross-layer kernel

The [complete deterministic construction](../claims/Yin_C_F0187_v5.md#kernel-proof) preserves the exact residual kernel, its large residual energy, physical and residual row spread, auxiliary Gram gap and pole dominance.
The fixed construction applies to every dimension divisible by four, including the power-of-two dimensions used in this development.
Its [statement and limits](../claims/Yin_C_F0187_v5.md#generic-kernel-statement) distinguish a genuine bounded symmetric matrix from the prescribed identity-block pencil and from any fixed Wigner law.
The actual-pencil coercivity below uses the additional inverse-block identities that this generic construction lacks.

<a id="next-probabilistic-test"></a>
## Next probabilistic test and unchanged limitations

For the real Rademacher first input, the highest surviving layer is now explicitly computable from the actual conditioned minor and background border.
In the bounded-inverse branch, a probabilistic lower bound on \(\mathcal E_4\) at order \(N^2\) automatically supplies fourth-layer load decay by (Fourth-load).
In an unbounded-inverse branch, use the actual row energies in that inequality and the distinct-mode identity rather than assuming that its coarse inverse-norm normalization is sharp.
The [single-pole residual test](#single-pole-residual-test) gives an explicit alternative scale and load criterion, while the [same-channel comparison](#auxiliary-mode-transversality) excludes replacing the scale solely by the two largest inverse modes.
The [fixed physical leverage and residual row-spread conclusions](../claims/Yin_C_F0187_v4.md#statement) resolve the two load-side inputs of (Pole-load-decay) in their bounded real \(K=1\) model, using fresh-coordinate concentration in the original basis.
The [actual residual coercivity argument](#actual-residual-cross-coercivity) now supplies the cross-layer lower bound at the bounded-model closest-mode scope, with its [uniform probability deduction](#actual-cross-energy-probability).
It uses the [auxiliary Gram development](#auxiliary-gram-gap) together with actual inverse-block identities, which are absent from the [generic cross-layer kernel](#cross-layer-kernel).
The [fixed whole-layer theorem](../claims/Yin_C_F0187_v6.md#statement) controls cancellation above a sufficiently large fixed effective inverse rank, while the dominant branch uses (Pole-noncollapse).
The [combined matrix reduction](../claims/Yin_C_F0194_v13.md#combined-branch-statement) makes the remaining minor event explicit.

If the fourth layer vanishes or has inadequate energy, the exact cubic, quadratic and linear formulas above define the necessary fallback rather than treating the formal raw degree as sufficient.
The fixed rare-atom construction demonstrates that a degree-one layer can carry all the surviving randomness in one coordinate.
A typical-minor argument must bound the probability of such unfavorable conditioned profiles, or retain further independent coordinates, before integrating the conditional MNV16 estimate.
The fixed spread theorem supplies neither a typical bounded real inverse nor a large effective inverse rank.
Complete fourth-layer control in the remaining low-effective-rank region is still unresolved.
The [reviewed graph normalization and averaging](../claims/Yin_C_F0194_v13.md#statement) remove the matrix-distance conversion gap on its explicit energy branches.
Singular minors, the complementary coefficient region, bottom logarithmic control and extension to the original finite-second-moment laws remain open.
Middle logarithmic control for general coefficient degeneracy and the stronger full-sequence F0012 conclusion remain separate obligations.

<a id="actual-residual-cross-coercivity"></a>
## Fixed actual residual cross-energy bound

The [reviewed actual-pencil theorem](../claims/Yin_C_F0187_v5.md#decision-auxiliary-cross-energy-reviewed) now supplies the complete [deterministic coercivity argument](../claims/Yin_C_F0187_v5.md#actual-residual-cross-coercivity) and its probability assembly.
It controls the cross term defined in (Pole-layer-decomposition), using the actual inverse identities in addition to the Gram and residual regularity estimates.
Its constants are independent of the inverse norm, and its dimensional error is absorbed through the residual energy divided by the physical dimension tending to infinity.

<a id="coercive-tensor-projection"></a>
### Projection and actual tangent control

The [fixed projection proof](../claims/Yin_C_F0187_v5.md#coercive-tensor-projection) contains the dimension-free symmetric-product estimate, perpendicular block control and the actual residual identity that bounds the remaining tangent directions.
The near-zero eigenvalue restriction and the uniform auxiliary Gram gap are explicit there.

<a id="distinct-index-transfer"></a>
### Transfer to the original sign coefficients

The [fixed distinct-index transfer](../claims/Yin_C_F0187_v5.md#distinct-index-transfer) retains all six repeated-index errors, the physical diagonal-block energy and the exact factor of 24 in the squared Walsh coefficient normalization.
This requires physical diagonal-energy negligibility in addition to row spread; the latter alone does not control the removed tensor entries.

<a id="actual-cross-energy-probability"></a>
### Closest modes and the remaining whole-layer issue

The [fixed probability statement](../claims/Yin_C_F0187_v5.md#actual-cross-energy-statement) gives the cross-energy lower bound uniformly over all closest-to-zero modes and all full or single-deletion pencils, as an unconditional bad-event bound intersected with invertibility.
It assumes no pole-dominance ratio.
The coefficient functional is formal for general bounded laws and for the full-size pencil; its actual fresh-row Walsh interpretation requires a single deletion and a Rademacher first input.
The [complete assembly and full fourth-layer decomposition](../claims/Yin_C_F0187_v5.md#actual-cross-energy-probability) leave cancellation between the cross and residual fourth terms unresolved.
The sufficient dominance condition in (Pole-noncollapse), or another treatment of comparable inverse modes, is still needed for the whole-layer argument.
Matrix-distance normalization, singular minors, logarithmic control and extension to arbitrary finite-second-moment laws also remain outside this fixed result.

<a id="homogeneous-inverse-zero-locus"></a>
## Exact zeros of the homogeneous inverse contribution

The [actual fourth-layer rewrite](#inverse-block-identities) isolates the polynomial
\[
 \mathcal H_{G,X}(x)
 :=(x^TGx)(x^TXGXx)
       -\bigl(x^T(GX+XG)x/2\bigr)^2,
 \qquad G=G^T,\quad X=X^T.
\]
For arbitrary real symmetric \(G,X\), this polynomial vanishes identically if and only if
\[
 \operatorname{rank}G\le1
 \quad\hbox{or}\quad
 (X-cI)G=0\ \hbox{for some }c\in\mathbb R.
 \tag{Homogeneous-inverse-zero-locus}
\]
This is an exact algebraic diagnosis of the homogeneous inverse contribution.
It is not a quantitative separation estimate and does not concern the fourth Walsh layer after the remaining terms and repeated indices are included.

Write \(A(x):=x^TGx\), \(B(x):=x^T(GX+XG)x/2\), and \(C(x):=x^TXGXx\).
If \(G=r aa^T\) has rank one, then
\(A=r(a^Tx)^2\), \(B=r(a^Tx)((Xa)^Tx)\), and \(C=r((Xa)^Tx)^2\), so \(AC=B^2\).
The zero matrix is immediate.
The second alternative also gives \(B=cA\) and \(C=c^2A\), and hence vanishing.

Conversely, suppose \(AC=B^2\) and \(\operatorname{rank}G=r\ge2\).
Complexify this real polynomial identity and make an invertible linear change of variables reducing \(A\) to \(z_1^2+\cdots+z_r^2\).
Every zero of \(A\) is a zero of \(B\).
Evaluating \(B\) at \(e_i+ie_j\) and \(e_i-ie_j\), for distinct \(i,j\le r\), shows that all its active diagonal coefficients are equal and all active off-diagonal coefficients are zero.
For each radical index \(k>r\), use \(e_i\pm ie_j+t e_k\) for arbitrary complex \(t\).
The linear and quadratic coefficients in \(t\) show that every active-radical coefficient and each radical diagonal coefficient of \(B\) vanish.
Replacing \(e_k\) by an arbitrary vector in the radical then eliminates its remaining quadratic coefficients.
Thus \(B=cA\); the original real coefficients imply \(c\in\mathbb R\).
The identity and \(A\ne0\) give \(C=c^2A\).

Now diagonalize the real symmetric \(X\), with eigenvalues \(x_i\).
The two quadratic identities imply, entry by entry,
\[
 \frac{x_i+x_j}{2}G_{ij}=cG_{ij},
 \qquad x_i x_jG_{ij}=c^2G_{ij}.
\]
Whenever \(G_{ij}\ne0\), these equations force \(x_i+x_j=2c\) and \(x_i x_j=c^2\), so \(x_i=x_j=c\).
Therefore \((X-cI)G=0\), proving the equivalence.

For the actual invertible \(K=1\) pencil, the second alternative has an additional consequence.
The first block column of \(\mathcal M\mathcal M^{-1}=I\) gives
\[
 (I-YX)G=-Y.
\]
If \(Gz=\gamma z\) with \(\gamma\ne0\) and \((X-cI)G=0\), then \(Xz=cz\) and
\[
 \gamma z=(c\gamma-1)Yz.
\]
The scalar \(c\gamma-1\) cannot vanish.
Thus \(z\) is an exact common eigenvector of \(X,Y\), and hence of
\(C=(\alpha X-Y)/(\alpha-1)\) and \(D=(Y-X)/(\alpha-1)\).
On the bounded-input event, their eigenvalues lie in a fixed bounded interval, so the [no-common-approximate-mode argument](#auxiliary-gram-gap) excludes this second alternative with nonzero G with probability tending to one.
This does not exclude the rank-one alternative, give a lower bound away from either algebraic alternative, or control cancellation with the term \(-q_Gq_X\) in (Actual-fourth-rewrite).
The sign restriction can also remove nonzero raw monomials through repeated indices.
Those quantitative and atomic-support issues remain before this diagnosis can yield a small-ball or logarithmic estimate.

<a id="actual-pencil-sign-collapse"></a>
## An actual-pencil sign collapse far from the homogeneous zero alternatives

The following deterministic family satisfies the exact identity off-diagonal pencil constraint and has a large effective rank.
Its homogeneous inverse contribution is not identically zero as a real polynomial, but its complete fourth Walsh layer vanishes exactly.
It is a diagnostic of atomic support and physical diagonal energy, not a fixed-law Wigner counterexample.

Take an even \(n\ge4\), put \(N:=n+1\), and choose
\[
 X:=\operatorname{diag}(\underbrace{1,\ldots,1}_{n/2},
                      \underbrace{-1,\ldots,-1}_{n/2}),
 \qquad e:=n^{-1/2}(1,\ldots,1)^T,\qquad f:=Xe.
\]
Then \(X=X^T\), \(X^2=I_n\), \(\operatorname{Tr}X=0\), and \(e,f\) are orthonormal.
For a real parameter \(t\ge4\), define
\[
 G:=t(I_n+ee^T),\qquad
 G^{-1}=t^{-1}(I_n-ee^T/2),\qquad
 Y:=(X-G^{-1})^{-1}.
 \tag{Sign-collapse-construction}
\]
The parameter may vary with \(n\); all estimates below are uniform for \(t\ge4\).
The matrix \(X-G^{-1}=X(I_n-XG^{-1})\) is invertible, because \(\|XG^{-1}\|=1/t\le1/4\).
Thus \(Y\) is real symmetric and
\[
 \|X\|=1,\qquad \|Y\|\le(1-1/t)^{-1}\le4/3.
 \tag{Sign-collapse-bounded-inputs}
\]
The real symmetric pencil
\[
 \mathcal M:=\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix}
\]
is invertible: its Schur complement over the invertible \(Y\) is \(X-Y^{-1}=G^{-1}\).
The exact inverse is
\[
 \mathcal Z:=\mathcal M^{-1}
 =\begin{pmatrix}G&H\\H^T&J\end{pmatrix},
 \qquad
 H=I_n-GX,\qquad J=XGX-X.
 \tag{Sign-collapse-inverse}
\]
For instance block inversion gives \(H=-GY^{-1}=I_n-GX\) and
\[
 J=Y^{-1}+Y^{-1}GY^{-1}
   =(X-G^{-1})+(X-G^{-1})G(X-G^{-1})
   =XGX-X.
\]
Thus these blocks are genuinely linked by the actual pencil equations, rather than an arbitrary inverse triple.
They can also be written as
\[
 G=tI_n+tee^T,\quad
 H=I_n-tX-tef^T,\quad
 J=tI_n-X+tff^T,\quad
 T:=(H+H^T)/2=I_n-tX-\tfrac t2(ef^T+fe^T).
 \tag{Sign-collapse-blocks}
\]
In particular \(\|\mathcal Z\|\le C t\), while \(\|\mathcal M\|\le1+\max\{\|X\|,\|Y\|\}\le7/3\).

<a id="exact-sign-collapse-calculation"></a>
### Raw polynomial versus the actual sign restriction

For \(x_i=\varepsilon_i/\sqrt N\), set
\[
 a_0:=\|x\|^2=n/N,\qquad z:=e^Tx,\qquad h:=f^Tx .
\]
The diagonal involution satisfies \(x^TXx=\operatorname{Tr}X/N=0\) on this entire sign support.
Consequently
\[
 x^TGx=t(a_0+z^2),\qquad
 x^TJx=t(a_0+h^2),\qquad
 x^TTx=a_0-tzh.
\]
The full raw homogeneous fourth part of the Schur determinant therefore restricts to
\[
 \begin{split}
 p_4^{\rm raw}(x)
 &=(x^TGx)(x^TJx)-(x^TTx)^2\\
 &=(t^2-1)a_0^2+t^2a_0(z^2+h^2)+2ta_0zh .
 \end{split}
 \tag{Exact-support-reduction}
\]
Since \(a_0\) is constant and \(z,h\) are linear in the original signs, this has only sign degrees zero and two.
All lower raw degrees of the full Schur determinant have sign degree at most three.
Hence, for every conditioned background border and exposed diagonal for which that determinant is formed,
\[
 \Pi_4p=\Pi_4p_4^{\rm raw}=0 .
 \tag{Actual-pencil-zero-Walsh-layer}
\]
This says nothing by itself about the lower surviving layers or exact singularity of the full bordered matrix.

This collapse does not put \(\mathcal H_{G,X}\) in its raw polynomial zero set.
Indeed \(G\) has full rank and \(X\) is not scalar on its range, so neither alternative in (Homogeneous-inverse-zero-locus) holds.
Directly, for coordinate vectors \(e_i,e_j\) with opposite diagonal signs of \(X\), one has
\[
 \mathcal H_{G,X}(e_i+e_j)=t^2(4+8/n)>0.
\]
On the sign cube, however,
\[
 \mathcal H_{G,X}(x)
   =t^2\bigl(a_0^2+a_0(z^2+h^2)\bigr),
\]
which also has no fourth Walsh layer.
Thus even quantitative separation from the raw zero alternatives would not by itself control the atomic fourth layer.

<a id="sign-collapse-rank-and-directions"></a>
### Large effective rank and two explicit separation measures

The eigenvalues of \(G\) are \(2t\) on \(e\) and \(t\) on \(e^\perp\).
Its stable rank is therefore
\[
 \frac{\|G\|_{\rm F}^2}{\|G\|^2}
    =\frac{n+3}{4}\longrightarrow\infty.
 \tag{Sign-collapse-stable-rank}
\]
Moreover
\[
 \inf_{\operatorname{rank}B\le1}\|G-B\|_{\rm F}^2
    =t^2(n-1).
 \tag{Distance-from-rank-one}
\]
For the lower bound, the kernel of any rank-at-most-one \(B\) has dimension at least \(n-1\), and \(G\succeq tI_n\) gives squared norm at least \(t^2\) on each vector of an orthonormal basis of that kernel.
The choice \(B=2tee^T\) attains equality.
Thus the Frobenius distance from rank one is comparable to the entire Frobenius norm, uniformly in \(t\).

The direction defect for the second raw-zero alternative is also macroscopic:
\[
 \inf_{c\in\mathbb R}\|(X-cI_n)G\|_{\rm F}^2
    =t^2(n+3)=\|G\|_{\rm F}^2 .
 \tag{Distance-from-scalar-direction}
\]
Indeed \(G^2=t^2(I_n+3ee^T)\), and \(\operatorname{Tr}(G^2X)=t^2(\operatorname{Tr}X+3e^TXe)=0\).
Using \(X^2=I_n\), the squared norm before minimization equals \((1+c^2)\operatorname{Tr}G^2=(1+c^2)t^2(n+3)\).
Consequently a positive lower bound on this normalized direction defect, together with any large-stable-rank assumption, still cannot imply a positive full fourth Walsh energy without additional information in the original coordinate basis.

<a id="sign-collapse-violates-typicality"></a>
### The exact typicality conditions that this family violates

Let \(\operatorname{off}_{\rm ph}\) remove the rank-two physical diagonal blocks of a \(2n\)-by-\(2n\) matrix.
The explicit inverse blocks give
\[
 \|\mathcal Z\|_{\rm F}^2=4t^2(n+3)+3n,\qquad
 \|\operatorname{off}_{\rm ph}\mathcal Z\|_{\rm F}^2
       =4t^2(1-1/n).
 \tag{Diagonal-dominated-inverse}
\]
To check the first identity, the squared block norms are
\[
 \|G\|_{\rm F}^2=t^2(n+3),\qquad
 \|H\|_{\rm F}^2=\|J\|_{\rm F}^2=n(1+t^2)+3t^2.
\]
For the second, the off-diagonal parts of \(G,J,H\) are respectively the off-diagonal parts of \(tee^T,tff^T,-tef^T\), each of squared norm \(t^2(1-1/n)\).
The two off-diagonal auxiliary blocks are both counted in the full physical Frobenius norm.

Remove any real unit eigenmode of \(\mathcal M\), writing
\[
 \mathsf E:=\mathcal Z-qww^T,\qquad
 \mathcal M w=q^{-1}w.
\]
Since \(|q|\le\|\mathcal Z\|\le Ct\) and the spectral decomposition is orthogonal,
\[
 \|\mathsf E\|_{\rm F}^2
      =\|\mathcal Z\|_{\rm F}^2-q^2
      \asymp nt^2
 \tag{Counterexample-residual-size}
\]
uniformly over the removed mode, for all sufficiently large \(n\).
Also
\[
 \|\operatorname{off}_{\rm ph}\mathsf E\|_{\rm F}
 \le\|\operatorname{off}_{\rm ph}\mathcal Z\|_{\rm F}
       +|q|\|\operatorname{off}_{\rm ph}(ww^T)\|_{\rm F}
 \le Ct .
\]
The physical diagonal-block energy consequently satisfies
\[
 \frac{\mathcal D(\mathsf E)}{\|\mathsf E\|_{\rm F}^2}
 =1-\frac{\|\operatorname{off}_{\rm ph}\mathsf E\|_{\rm F}^2}
          {\|\mathsf E\|_{\rm F}^2}
 =1-O(1/n).
 \tag{Counterexample-diagonal-energy}
\]
For its visible off-diagonal residual scale,
\[
 \mathcal R^2\le
       \|\operatorname{off}_{\rm ph}\mathsf E\|_{\rm F}^2
       \le Ct^2,\qquad
 \frac{\mathcal R^2}{\|\mathsf E\|_{\rm F}^2}=O(1/n).
 \tag{Counterexample-offdiagonal-comparison}
\]
These statements hold even when the removed mode is chosen closest to zero.
They are incompatible with both the [physical diagonal-energy negligibility](../claims/Yin_C_F0187_v4.md#spectral-residual-spread) and the [residual off-diagonal comparability](../claims/Yin_C_F0187_v4.md#actual-residual-blocks) established with high probability in the actual bounded Wigner model.
Thus this example does not contradict the reviewed spread chain or the preceding cross-coercivity deduction, which uses those additional conditions.
If \(t=t_n\to\infty\), the residual squared norm divided by \(n\) diverges, but these two failures remain.

Finally set
\[
 C:=\frac{\alpha X-Y}{\alpha-1},\qquad
 D:=\frac{Y-X}{\alpha-1},\qquad \alpha:=\sqrt2.
\]
These real symmetric bounded matrices satisfy \(C+D=X\) and \(C+\alpha D=Y\), giving the exact original-input algebraic pencil form.
They are a chosen deterministic family depending on \(n,t\), not matrices sampled from two independent fixed Wigner entry laws with the original normalized coordinates.
No probability or support claim for such a fixed-law ensemble is supplied.
For example, vectors in either eigenspace of \(X\) orthogonal to \(e\) are exact common eigenvectors of \(X,Y\), and therefore of \(C,D\), when those subspaces are nonzero.
This also illustrates the absence of the independent-input no-common-approximate-mode property.
The family refutes a deterministic inference based only on the pencil algebra, bounded \(X,Y\), effective rank and the two displayed raw-zero separation measures.
It neither refutes the original determinant Tasks nor excludes a proof using their additional probabilistic and coordinate-sensitive inputs.

<a id="full-layer-high-effective-rank"></a>
## Fixed whole-layer result above a constant effective rank

The complete argument is now fixed in [C187v6](../claims/Yin_C_F0187_v6.md#decision-whole-layer-rank-reviewed), with [independent whole-proof coverage](../audits/reviews/Yin_R_F0191_v6.md#whole-layer-fixed-rank).
In the stated bounded real model, it proves a complete fourth-layer energy lower bound and vanishing coordinate loads on the branch
\[
 r_Z:=\|Z\|_{\rm F}^2/\|Z\|^2\ge r_*,
\]
where \(r_*\) is a sufficiently large fixed constant.
It does not assert that this branch or invertibility has high probability.
The exact model, uniform full/single-deletion scope, and formal-sign versus actual-row distinction belong to the [fixed statement](../claims/Yin_C_F0187_v6.md#statement).

<a id="rank-refined-four-cycle-error"></a>
### Fixed rank-sensitive fourth-layer expansion

The [fixed coefficient and four-cycle proof](../claims/Yin_C_F0187_v6.md#rank-refined-four-cycle-error) retains the exact normalization, shared-vertex terms, all four-cycle contributions and row-load bound.
Its error has scale \(C\|Z\|^2\|Z\|_{\rm F}^2/N^4\), giving relative error \(C/r_Z\) at the quartic Frobenius scale.

<a id="actual-six-gram-coercivity"></a>
### Fixed actual six-Gram coercivity

The [fixed deterministic argument](../claims/Yin_C_F0187_v6.md#actual-six-gram-coercivity) uses the actual inverse identities and the independent-input approximate-mode gap to force the six-Gram term.
It distinguishes the tensor product in the Hilbert space of symmetric matrices from the fully symmetrized fourth-coordinate tensor.

<a id="whole-layer-physical-transfer"></a>
### Fixed physical and probability transfer

The [fixed transfer proof](../claims/Yin_C_F0187_v6.md#whole-layer-physical-transfer) deduces full-inverse row and diagonal spread from the exact residual estimates, and assembles the fixed-rank energy/load conclusions without dividing by the probability of invertibility.

<a id="finite-effective-rank-boundary"></a>
### Remaining bounded-effective-rank region

The [fixed boundary](../claims/Yin_C_F0187_v6.md#remaining-boundary) retains the failure of finite-rank approximation from bounded effective rank alone, with its explicit diagonal example.
The two fixed extensions below cover bounded effective rank through either an operator gap or comparable largest inverse modes.
Their conclusions use the actual inverse identities and physical spread inputs; the failure of finite-rank approximation alone does not obstruct that separate argument.

<a id="spectral-gap-cross-orthogonality"></a>
## Fixed operator-gap energy and load estimate

The complete mixed fourth-Walsh inner-product proof is retained in [C187v7](../claims/Yin_C_F0187_v7.md#mixed-fourth-inner-product), with its [independent adoption](../claims/Yin_C_F0187_v9.md#decision-operator-gap-reviewed).
For one symmetric rank-two quadratic factor and three residual factors of operator norm at most \(m\) and Frobenius norm at most \(R\), it gives the dimension-free bound \(CmR^2/N^4\).
The [fixed coefficient argument](../claims/Yin_C_F0187_v7.md#operator-gap-coefficients) then proves complete fourth-layer energy at scale \(|q|\|E\|_{\rm F}/N^2\) when \(\|E\|\le\gamma_*|q|\), without Frobenius dominance.
Its load conclusion uses a fixed effective-rank upper bound.
The [three-branch consequence](../claims/Yin_C_F0187_v7.md#three-branch-proof) retains the older high-rank and dominant thresholds exactly.
The remaining comparable-mode regime is handled by the next fixed result.

<a id="comparable-mode-raw-separation"></a>
## Fixed comparable-mode separation

The complete deterministic result and proof are retained in [C187v8](../claims/Yin_C_F0187_v8.md#comparable-mode-raw-separation), with [independent adoption](../claims/Yin_C_F0187_v9.md#decision-comparable-modes-reviewed).
For bounded \(X,Y\) with a fixed joint approximate-mode gap, an actual inverse \(Z\) with sufficiently large operator norm and \(s_2^\downarrow(Z)\ge\gamma\|Z\|\) has raw quartic sphere supremum at least \(c\|Z\|^2\).
This raw statement has no Frobenius or effective-rank restriction.

<a id="three-operator-gram-limit"></a>
### Actual identities in the limiting operator construction

The [fixed three-operator construction](../claims/Yin_C_F0187_v8.md#three-operator-gram-limit) retains two nonzero orthonormal inverse modes by convergence of a countable family of Gram entries.
It passes the actual inverse identities, common-mode exclusion and raw polynomial identity to bounded selfadjoint operators.
It requires neither compactness in Frobenius norm nor a negligible finite-rank tail.

<a id="infinite-space-zero-transfer"></a>
### Finite restrictions determine the limiting zero classification

The [fixed finite quadratic-product lemma](../claims/Yin_C_F0187_v8.md#finite-quadratic-product) includes rank two, indefinite forms and radical coordinates.
Its [Hilbert-space transfer](../claims/Yin_C_F0187_v8.md#infinite-space-zero-transfer) forces a common \(X,Y\) eigenvector from raw vanishing and two surviving modes, contradicting the joint gap.
The separate finite actual-pencil zero classification and sign-collapse example earlier in this draft retain their own scope and diagnostic content.

<a id="comparable-mode-walsh-transfer"></a>
## Fixed original-coordinate transfer

The [fixed collision estimate](../claims/Yin_C_F0187_v8.md#comparable-mode-walsh-transfer) controls all repeated physical indices by \(C\|Z\|_{\rm F}^2(\mathcal D(Z)+\max_i d_i(Z))\).
At bounded effective rank, the proved physical diagonal and row spread makes that loss negligible at scale \(\|Z\|^4\).
The exact coefficient normalization then gives complete fourth-layer squared energy at least \(c\|Z\|^4/N^4\) and vanishing coordinate load.

<a id="comparable-mode-probability-scope"></a>
### Complete invertible-minor coverage and the remaining interface

The [fixed exhaustive assembly](../claims/Yin_C_F0187_v8.md#actual-model-and-three-regimes) covers every invertible full or single-deletion minor in the bounded real model, with the original normalization.
For the low-effective-rank branch \(r_Z\le K\), the identity \(\|Z\|_{\rm F}^2=r_Z\|Z\|^2\) and the accepted divergence give the stronger size observation \(\|Z\|^2/n\to\infty\) in the same uniform invertible-branch sense.
The [graph consequence](../claims/Yin_C_F0187_v8.md#complete-graph-assembly) requires a Rademacher first off-diagonal law and leaves only the average probability of singular physical minors at matrix scale \(cN^{-5}\).
No singular-minor probability, logarithmic conclusion or extension beyond the bounded model is established by that fixed version.
The separate [middle-value investigation](Yin_D_F0010.md#balanced-two-channel-middle) and whole-parent scalar-shift route address the remaining bounded-model assembly.


<a id="high-amplitude-path-resonance"></a>
## High-amplitude path resonance: Gram degeneration and the distinct fourth layer

The following ordinary development tests which parts of the bounded-minor argument can survive a growing input norm.
It is an exact deterministic identity-coupled pencil, not a probability statement for independent fixed Wigner laws.
Unlike the earlier [bounded sign-collapse family](#actual-pencil-sign-collapse), it isolates a high-amplitude path and explicitly compares its two opposite auxiliary slopes, raw quartic and original-coordinate distinct layer.

Fix \(\alpha:=\sqrt2\), put \(\beta:=\sqrt\alpha\), and let \(R>\sqrt2\).
On four physical coordinates define real symmetric matrices \(C_R,D_R\) by
\[
 (C_R)_{12}=(C_R)_{21}=(C_R)_{34}=(C_R)_{43}:=R,
 \qquad
 (D_R)_{23}=(D_R)_{32}:=b_R:=(R^2-1)/\beta,
\]
with all other entries zero.
Set
\[
 X_R:=C_R+D_R,\qquad Y_R:=C_R+\alpha D_R,\qquad
 M_R:=\begin{pmatrix}X_R&I_4\\I_4&Y_R\end{pmatrix}.
 \tag{Path-resonant-pencil}
\]
Its input and pencil norms are unbounded as \(R\to\infty\), with \(\|M_R\|\asymp R^2\).
The latter follows from the upper bound by the block norms and the identity \(D_R=(Y_R-X_R)/(\alpha-1)\), since \(\|D_R\|=b_R\asymp R^2\).

### Exact kernel and auxiliary Gram determinant

For \(\sigma\in\{+1,-1\}\), put
\[
 e_\sigma:=(e_1+\sigma e_4)/\sqrt2,\qquad
 f_\sigma:=(e_2+\sigma e_3)/\sqrt2,\qquad
 a_R:=\bigl((1+\alpha)(1+R^{-2})\bigr)^{-1/2}.
\]
The two reflection sectors are invariant.
In the physical basis \((e_\sigma,f_\sigma)\), the input matrices are
\[
 C_R=\begin{pmatrix}0&R\\R&0\end{pmatrix},
 \qquad
 D_R=\begin{pmatrix}0&0\\0&\sigma b_R\end{pmatrix}.
\]
Define
\[
 u_\sigma:=a_R(e_\sigma-\sigma\beta f_\sigma/R),\qquad
 v_\sigma:=a_R(\sigma\beta e_\sigma-f_\sigma/R),\qquad
 w_\sigma:=\binom{u_\sigma}{v_\sigma}.
 \tag{Path-zero-modes}
\]
Substitution into \(X_Ru_\sigma+v_\sigma=0\) and \(u_\sigma+Y_Rv_\sigma=0\) uses exactly \(\beta b_R=R^2-1\) and proves \(M_Rw_\sigma=0\).
The normalization gives \(\|w_\sigma\|=1\), and the two modes are orthogonal because they belong to different reflection sectors.

These are the entire kernel.
Indeed, reorder each sector with its two endpoint auxiliary coordinates first.
The endpoint block is \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\), its boundary to the two internal coordinates is \(RI_2\), and the internal block is
\[
 K_\sigma:=\begin{pmatrix}\sigma b_R&1\\1&\sigma\alpha b_R\end{pmatrix}.
\]
Its determinant is \(\alpha b_R^2-1=R^2(R^2-2)>0\).
The endpoint Schur determinant has numerator \((1-R^2)^2-\alpha b_R^2=0\).
Its off-diagonal entry is \(1+R^2/\det K_\sigma>0\), so the endpoint Schur matrix has rank one.
Thus each reflection sector contributes exactly one zero mode.

The auxiliary Gram entries are
\[
 \|u_\sigma\|^2=a_R^2(1+\alpha R^{-2}),\qquad
 \|v_\sigma\|^2=a_R^2(\alpha+R^{-2}),\qquad
 \langle u_\sigma,v_\sigma\rangle
   =\sigma\beta a_R^2(1+R^{-2}).
\]
Their Gram matrix has trace one and determinant
\[
 \Delta_R
 :=\|u_\sigma\|^2\|v_\sigma\|^2
        -\langle u_\sigma,v_\sigma\rangle^2
 =\frac{(\alpha-1)^2}
 {R^2(1+\alpha)^2(1+R^{-2})^2}
 \longrightarrow0.
 \tag{Path-Gram-degeneration}
\]
Both auxiliary component norms remain bounded away from zero.
The degeneration comes from their becoming proportional:
\[
 v_\sigma-\sigma\beta u_\sigma
       =a_R(\alpha-1)f_\sigma/R.
\]
Consequently the low-energy block identities alone cannot give the old uniform all-mode Gram bound once the fixed norm premise is removed.
This does not contradict the [bounded-model Gram theorem](../claims/Yin_C_F0187_v5.md#statement).

### Two-pole projection: raw energy and original sign coefficients

Put
\[
 P_0:=w_+w_+^T+w_-w_-^T,\qquad
 \mathcal B(x):=\begin{pmatrix}x&0\\0&x\end{pmatrix},
 \qquad x\in\mathbb R^4.
\]
This is the first-input border map with zero second-input border.
Write \(P_0=\begin{pmatrix}G&H\\H^T&J\end{pmatrix}\) and \(T:=(H+H^T)/2\).
Its raw fourth polynomial is
\[
 h_{P_0}(x)
 :=(x^TGx)(x^TJx)-(x^TTx)^2
 =\det(\mathcal B(x)^TP_0\mathcal B(x)).
\]
Let \(W\) be the matrix with columns \(w_+,w_-\).
Since \(P_0=WW^T\), \(h_{P_0}(x)=\det(W^T\mathcal B(x))^2\).
Using the coordinates \(\langle e_\sigma,x\rangle\) and \(\langle f_\sigma,x\rangle\) in the two rows of \(W^T\mathcal B(x)\) gives
\[
 \det(W^T\mathcal B(x))
 =a_R^2\left[
 -\beta(x_1^2-x_4^2)
 +\frac{1+\alpha}{R}(x_1x_3-x_2x_4)
 +\frac{\beta}{R^2}(x_2^2-x_3^2)
 \right].
 \tag{Path-projection-determinant}
\]
In particular
\[
 h_{P_0}(e_1)=\alpha a_R^4
 \longrightarrow\frac{\alpha}{(1+\alpha)^2}>0.
 \tag{Path-raw-noncollapse}
\]
Thus the opposite auxiliary slopes preserve a nonzero raw quartic.

For the formal sign normalization put \(x_j:=\varepsilon_j/\sqrt N\).
Here \(N\ge4\) is the normalization parameter; an actual single-deletion parent of this four-point minor has \(N=5\).
All squared-coordinate differences in (Path-projection-determinant) vanish on the sign cube, so
\[
 h_{P_0}(\varepsilon/\sqrt N)
 =\frac{a_R^4(1+\alpha)^2}{R^2N^2}
       (2-2\varepsilon_1\varepsilon_2\varepsilon_3\varepsilon_4).
\]
Its only distinct fourth coefficient is therefore
\[
 c_{1234}(P_0)
 =-\frac{2a_R^4(1+\alpha)^2}{R^2N^2}
 =-\frac{2R^2}{(R^2+1)^2N^2}.
 \tag{Path-distinct-fourth-loss}
\]
The squared coefficient norm is \(c_{1234}(P_0)^2\), while the coefficient norm itself is its absolute value.
The maximum relative coordinate load is exactly one.

For a small positive scalar shift define
\[
 Z_\theta:=(M_R+\theta I_8)^{-1},\qquad
 Q_\theta:=\|Z_\theta\|.
\]
At each fixed \(R\), the nonzero spectrum of \(M_R\) is separated from zero.
Thus \(Q_\theta=\theta^{-1}\) for sufficiently small \(\theta>0\), and \(Z_\theta/Q_\theta\to P_0\).
For any real symmetric block matrix \(Z\), write \(h_Z(x):=\det(\mathcal B(x)^TZ\mathcal B(x))\), and let \(\sigma_4(Z)\) be the Euclidean norm of the distinct fourth coefficients of \(h_Z(\varepsilon/\sqrt N)\).
Define the ball graph-area scale
\[
 A_\theta:=
 \sup_{\|x\|\le2}
 \sqrt{\det(I_2+\mathcal B(x)^TZ_\theta^2\mathcal B(x))}.
\]
Finite-dimensional continuity, uniformly on that compact ball, gives
\[
 \frac{A_\theta}{Q_\theta^2}\longrightarrow
 A_R^{\rm graph}:=
 \sup_{\|x\|\le2}\sqrt{h_{P_0}(x)}.
\]
The bounds \(\beta a_R^2\le A_R^{\rm graph}\le4\) follow respectively by taking \(x=e_1\) and from \(\|\mathcal B(x)^TP_0\mathcal B(x)\|\le\|x\|^2\).
Consequently,
\[
 \lim_{\theta\downarrow0}
 \frac{N^2\sigma_4(Z_\theta)}{A_\theta}
 =\frac{2R^2}{(R^2+1)^2A_R^{\rm graph}}
 \asymp R^{-2}
 \quad(R\to\infty).
 \tag{Path-graph-normalized-loss}
\]
This is precisely a loss against the radius-two graph normalization appearing in the [finite-variance conditional bridge](../claims/Yin_C_F0194_v14.md#statement).
It does not say that the graph area on every discrete sign support is the same as the ball supremum.

### A small perturbation leaving only one exact zero mode

Perturb the first input by
\[
 C_{R,\delta}:=C_R+\delta e_-e_-^T,\qquad
 M_{R,\delta}:=
 \begin{pmatrix}C_{R,\delta}+D_R&I_4\\
 I_4&C_{R,\delta}+\alpha D_R\end{pmatrix},
 \qquad \delta>0.
\]
This is still an exact real identity-coupled pencil.
The perturbation is \(\delta\operatorname{diag}(e_-e_-^T,e_-e_-^T)\).
It annihilates the positive reflection sector, so \(w_+\) remains an exact zero mode.

At fixed \(R\), the negative reflection sector's simple zero eigenvalue has a continuous eigenvector \(w_{-,\delta}\to w_-\) and an eigenvalue
\[
 \lambda_-(\delta)
 =\frac{\delta}{1+R^{-2}}+O_R(\delta^2).
 \tag{Path-simple-pole-splitting}
\]
For completeness, this is the simple root of a finite characteristic polynomial; differentiating its normalized eigenvector equation at \(\delta=0\) gives
\[
 \lambda_-'(0)
 =w_-^T\operatorname{diag}(e_-e_-^T,e_-e_-^T)w_-
 =a_R^2(1+\alpha)=\frac1{1+R^{-2}}>0.
\]
The other nonzero eigenvalues remain separated from zero at fixed \(R\).

Now let \(\delta\downarrow0\) and \(\theta>0\) satisfy \(\theta/\delta\to0\).
Put
\[
 Z_{\theta,\delta}:=(M_{R,\delta}+\theta I)^{-1},\qquad
 q_+:=\theta^{-1},\qquad
 q_-:=(\lambda_-(\delta)+\theta)^{-1}.
\]
The spectral decomposition has the form
\[
 Z_{\theta,\delta}
 =q_+w_+w_+^T+q_-w_{-,\delta}w_{-,\delta}^T+O_R(1)
\]
in operator norm.
Each rank-one full inverse term has identically zero raw fourth polynomial.
The mixed two-pole term is therefore the leading one after division by \(q_+q_-\).
Since \(q_+,q_-\to\infty\), terms involving the bounded remainder vanish in that normalization.
It follows, uniformly on bounded \(x\)-sets and hence coefficientwise, that
\[
 \frac{h_{Z_{\theta,\delta}}(x)}{q_+q_-}
 \longrightarrow h_{P_0}(x).
\]
Similarly, spectral orthogonality and the two-dimensional determinant expansion give
\[
 \frac{
 \sup_{\|x\|\le2}
 \sqrt{\det(I+\mathcal B(x)^TZ_{\theta,\delta}^2\mathcal B(x))}}
 {|q_+q_-|}
 \longrightarrow A_R^{\rm graph}.
\]
Indeed the leading determinant is \(q_+^2q_-^2\) times the squared determinant of the two projected modes, while every term involving the bounded spectral remainder has a vanishing ratio.
Thus the same coefficient loss (Path-graph-normalized-loss) survives this single-dominant-pole regime.
The limit order is fixed \(R\), then \(\delta\downarrow0\) with \(\theta/\delta\to0\), then \(R\to\infty\).
No uniform estimate permitting an arbitrary simultaneous choice of \(R,\delta,\theta\) is asserted.

### Interpretation and the next discriminating test

The four-point construction has relative fourth load one and physically concentrated zero modes.
It therefore does not satisfy the [reviewed physical-spread conditions](../claims/Yin_C_F0187_v10.md#statement) for actual finite-variance Wigner minors.
It is not a counterexample satisfying all of those conditions.
Nor does it specify fixed independent entry laws or prove a positive probability of any displayed resonance in such an ensemble.
Its role is to disprove a purely algebraic restoration of the old fixed Gram bound and to show that raw noncollapse can coexist with a growing original-coordinate distinct-layer loss.

The next useful test is to examine copies or perturbations of this actual-pencil family while keeping the original physical basis and explicitly tracking physical leverage, inverse diagonal energy, fourth load and the graph-area scale.
The decisive quantity is
\[
 \frac{N^2\sigma_4(Z)}
 {\displaystyle\sup_{\|x\|\le2}
   \sqrt{\det(I+\mathcal B(x)^TZ^2\mathcal B(x))}}.
\]
One should determine whether the soft physical-spread conditions force the observed \(R^{-2}\) loss to disappear, or whether an actual-pencil family can retain that loss while meeting all of them.
A common orthogonal change of physical coordinates preserves the pencil algebra but changes the independent-coordinate sign functional and does not preserve a Wigner law.
Such a rotation must therefore be treated as a separate deterministic diagnostic, not as a proof of actual-model typicality.
This test distinguishes a full-fourth-layer route from an attempt to make the old all-mode Gram conclusion a necessary intermediate target.

<a id="flat-two-mode-slope-test"></a>
### Flat physical modes do not by themselves prevent a small auxiliary slope difference

The following exact two-mode test separates a small raw determinant from the repeated-index loss in the four-point path.
Let \(n=2m\ge4\), choose signs \(s_i\in\{-1,1\}\) with \(m\) of each sign, and put
\[
 h_1:=n^{-1/2}(1,\ldots,1)^T,\qquad
 h_2:=n^{-1/2}(s_1,\ldots,s_n)^T,\qquad
 x_1:=R,\quad x_2:=R+1,\quad R>1.
\]
The physical vectors \(h_1,h_2\) are orthonormal.
Take real symmetric \(X,Y\) satisfying
\[
 Xh_j=x_jh_j,\qquad Yh_j=x_j^{-1}h_j
 \quad(j=1,2).
\]
For this test, define both matrices to be zero on the common orthogonal complement of \(h_1,h_2\).
Then \(M:=\begin{pmatrix}X&I_n\\I_n&Y\end{pmatrix}\) has exactly two zero modes
\[
 w_j:=\frac{1}{\sqrt{1+x_j^2}}\binom{h_j}{-x_jh_j},\qquad
 P_0:=w_1w_1^T+w_2w_2^T.
\]
Indeed, each two-dimensional auxiliary block has eigenvalues \(0\) and \(x_j+x_j^{-1}>0\), while the complementary blocks have eigenvalues \(1,-1\).
This is an exact pencil of the same algebraic form because
\[
 C:=\frac{\alpha X-Y}{\alpha-1},\qquad
 D:=\frac{Y-X}{\alpha-1}
\]
give \(X=C+D\) and \(Y=C+\alpha D\).
Its deterministic complementary blocks do not supply a Wigner bulk law.

With the same border map \(\mathcal B(x)\), now on \(\mathbb R^n\), define
\[
 d_R:=\frac{x_1-x_2}{\sqrt{(1+x_1^2)(1+x_2^2)}}.
\]
The two projected rows immediately give
\[
 h_{P_0}(x)=d_R^2(h_1^Tx)^2(h_2^Tx)^2,
 \qquad
 \sup_{\|x\|\le2}\sqrt{h_{P_0}(x)}=2|d_R|.
 \tag{Flat-mode-raw-slope-loss}
\]
The last equality follows from \((h_1^Tx)^2+(h_2^Tx)^2\le4\), with equality at equal absolute components.
In particular \(|d_R|\asymp R^{-2}\); here the raw quartic itself degenerates.

For \(x:=\varepsilon/\sqrt N\), the coefficient of a distinct quadruple \(I\) is
\[
 c_I(P_0)=\frac{4d_R^2}{n^2N^2}\sum_{\{i,j\}\subset I}s_is_j.
\]
The sum is \(6\) when all four signs agree, \(0\) for a three-to-one split, and \(-2\) for a two-to-two split.
There are respectively \(2\binom m4\) and \(\binom m2^2\) nonzero quadruples of the first and third types.
Consequently, for every scalar \(q>0\),
\[
 \begin{split}
 \sigma_4(qP_0)^2
 &=\frac{q^4d_R^4}{n^4N^4}
       \left(1152\binom m4+64\binom m2^2\right)\\
 &=\frac{4q^4d_R^4}{N^4}
       \frac{(n-2)(n^2-8n+18)}{n^3}.
 \end{split}
 \tag{Flat-mode-distinct-energy}
\]
The coefficient norm is positive for every even \(n\ge4\).
Permutations within the two sign classes and exchange of the classes act transitively on coordinates and preserve the squared coefficients.
Since each quadruple contributes to exactly four coordinate loads, the relative maximum load is exactly \(4/n\).
Each mode has physical coordinate leverage \(1/n\), and the two-mode projection has physical leverage at most \(2/n\).

For each fixed \(n,R\), the scalar-shift inverse \(Z_\theta:=(M+\theta I)^{-1}\) satisfies \(Z_\theta=qP_0+O_{n,R}(1)\), with \(q:=\theta^{-1}\) as \(\theta\downarrow0\).
The same compact-ball determinant calculation as above yields graph area \(2q^2|d_R|(1+o(1))\).
Hence
\[
 \lim_{\theta\downarrow0}
 \frac{N^2\sigma_4(Z_\theta)}
 {\displaystyle\sup_{\|x\|\le2}
       \sqrt{\det(I_2+\mathcal B(x)^TZ_\theta^2\mathcal B(x))}}
 =|d_R|\sqrt{\frac{(n-2)(n^2-8n+18)}{n^3}}.
 \tag{Flat-mode-graph-loss}
\]
Taking \(n\to\infty\) after this fixed-dimensional limit leaves \(|d_R|\), which then tends to zero as \(R\to\infty\).
No uniform simultaneous limit is needed or claimed.

Thus flat physical modes and small relative fourth load alone do not supply a uniform graph-normalized fourth-energy lower bound.
This calculation provides no fixed independent entry laws, typical-event probability, required weighted free spectral mass, or uniform controls for all deleted physical minors.
It uses a zero second-input border and does not settle the graph-area condition with an arbitrary actual conditioned second border.
It therefore does not refute a bound using all of the finite-variance soft controls together with further actual-model geometry.
The next unresolved test is whether the weighted bulk and simultaneous-minor information excludes this common-direction, nearly equal auxiliary-slope mechanism.

<a id="favorable-subsequence-tail-rank"></a>
## Finite variance supplies a favorable subsequence at the rank-times-log scale

This elementary observation uses the dimensional-subsequence freedom in [the determinant marginal criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion).
It addresses the size of a truncation perturbation, not a polynomial floor or the unregularized determinant itself.

Let \(\mathcal X\) be any fixed finite collection of real or complex random variables with finite second moments.
For every fixed \(\varepsilon>0\), define
\[
 F_\varepsilon(N):=
 \sum_{X\in\mathcal X}\mathbb P\{|X|>\varepsilon\sqrt N\}.
\]
The integer tail-sum formula gives
\[
 \sum_{N\ge1}F_\varepsilon(N)
 \le\varepsilon^{-2}\sum_{X\in\mathcal X}\mathbb E|X|^2<\infty.
\]
Therefore
\[
 \liminf_{N\to\infty}N\log N\,F_\varepsilon(N)=0.
 \tag{Subsequence-tail-gain}
\]
Otherwise \(F_\varepsilon(N)\ge c/(N\log N)\) for all sufficiently large \(N\), contradicting convergence of its sum.

Choose any deterministic \(\varepsilon_k\downarrow0\).
For each \(k\), (Subsequence-tail-gain) permits a deterministic \(N_k>N_{k-1}\), as large as desired, such that
\[
 N_k\log N_k\,F_{\varepsilon_k}(N_k)\le2^{-3k}.
 \tag{Selected-tail-subsequence}
\]
The choice depends only on the prescribed laws and not on the sampled matrices.

In finitely many Wigner inputs of size \(N_k\), replace every raw coordinate of modulus greater than \(\varepsilon_k\sqrt{N_k}\) by zero, and perform the corresponding conjugate replacement below the diagonal.
Include all needed off-diagonal and diagonal laws in \(\mathcal X\).
Let \(\widetilde W_j^{(N_k)}\) denote the resulting matrices, and put
\[
 R_k:=\sum_j\operatorname{rank}
           (W_j^{(N_k)}-\widetilde W_j^{(N_k)}).
\]
There are at most a fixed multiple of \(N_k^2\) independent raw coordinates.
Changing one off-diagonal coordinate and its mirror has rank at most two; changing a diagonal coordinate has rank at most one.
Consequently
\[
 \mathbb E\left[\frac{R_k\log N_k}{N_k}\right]
 \le C N_k\log N_k\,F_{\varepsilon_k}(N_k)
 \le C2^{-3k}.
 \tag{Subsequence-rank-log-gain}
\]
In particular \(R_k\log N_k/N_k\to0\) in probability.
Markov's inequality at threshold \(2^{-k}\) gives summable exceptional probabilities.
First Borel--Cantelli therefore also gives
\[
 R_k\log N_k/N_k\longrightarrow0
 \quad\text{almost surely under every cross-size coupling}.
\]
No independence across sizes is needed.

The [fixed polynomial rank telescope](../claims/Yin_C_F0186_v4.md#rank-stability) transfers this estimate to every fixed matrix polynomial of the inputs.
For example, after Hermitization, a logarithm clipped below at \(N_k^{-A}\) and above at \(N_k^B\), for fixed \(A,B>0\), has total variation \(O((A+B)\log N_k)\).
The rank comparison therefore makes the corresponding normalized clipped-logarithm difference tend to zero along this subsequence.
This is stronger than a bare rank-\(o(N)\) comparison and meets the rank-times-log scale exposed by [the direct-transfer obstruction](Yin_D_F0010.md#finite-variance-minor-guard-boundary).

The inference stops before the unregularized logarithm.
Removing the lower clipping still needs suitable polynomial floors or another bottom-logarithm estimate for both compared outputs.
Moreover, the raw truncated laws vary with \(k\), their bounds grow like \(\varepsilon_k\sqrt{N_k}\), and their means need not remain zero.
The [fixed bounded-law theorem](../claims/Yin_C_F0186_v18.md#statement) cannot be applied to this triangular array merely because each individual truncation is bounded.
The coordinatewise truncation preserves independence within each input, but the argument supplies no bounded operator-norm core.
It also gives no fresh-row independence after any additional sample-dependent selection of a surviving principal minor.
These are genuine remaining interfaces, not conclusions of the subsequence selection.

<a id="flat-two-row-slope-test"></a>
## Two original rows improve the flat-mode loss by one power, but do not remove it

This ordinary development calculation for Yin, dated 2026-11-05, tests the [flat two-mode example](#flat-two-mode-slope-test) with both original independent input rows retained.
It is not an independent review or a Wigner counterexample.
The [two-row conditional theorem](../claims/Yin_C_F0194_v12.md#statement) already treats fixed inverse guards, while the [growing-guard calculation](Yin_D_F0032.md#polynomial-minor-inverse-guard) retains its unresolved actual-minor probability.
The question here is whether the second row alone removes the graph-normalized fourth-layer obstruction without an inverse guard.

### Actual projected determinant with both original rows

Keep \(\alpha=\sqrt2\), \(n=2m\ge4\), \(N=n+1\), the two balanced flat vectors \(h_1,h_2\), and the pencil \(M\) defined in the preceding flat-mode test.
Thus \(Xh_1=Rh_1\), \(Xh_2=(R+1)h_2\), \(Yh_j=x_j^{-1}h_j\), where \(x_1=R\), \(x_2=R+1\), and \(R>1\).
Both matrices vanish on the common orthogonal complement.
Its two zero modes and their projection are
\[
 w_j=\frac1{\sqrt{1+x_j^2}}\binom{h_j}{-x_jh_j},
 \qquad W=(w_1\ w_2),\qquad P_0=WW^T.
\]
For arbitrary original row vectors \(x,y\in\mathbb R^n\), put
\[
 u=x+y,\qquad v=x+\alpha y,\qquad
 \mathcal B(x,y)=\begin{pmatrix}u&0\\0&v\end{pmatrix}\in M_{2n,2}(\mathbb R).
\]
For a general symmetric inverse \(Z=\left(\begin{smallmatrix}G&H\\H^T&J\end{smallmatrix}\right)\), the actual homogeneous fourth Schur polynomial is
\[
 p_Z^{(4)}(x,y)=(u^TGu)(v^TJv)-(u^THv)^2.
 \tag{Two-row-actual-fourth}
\]
This retains the actual bilinear form \(u^THv\); no symmetry assumption on \(H\) and no replacement of it by \((H+H^T)/2\) is used.

Write
\[
 a=h_1^Tx,\quad b=h_2^Tx,\quad c=h_1^Ty,\quad d=h_2^Ty,
\]
\[
 \delta:=\alpha-1,\qquad \beta:=\alpha+1,\qquad
 T:=\delta(2R+1),\qquad
 D_R:=\sqrt{(1+R^2)(1+(R+1)^2)}.
\]
The two projected rows give exactly
\[
 \det(W^T\mathcal B(x,y))=\frac{F(a,b,c,d)}{D_R},
\]
\[
 \begin{split}
 F&=R(b+d)(a+\alpha c)-(R+1)(a+c)(b+\alpha d)\\
  &=-ab-\alpha cd+\frac{T-\beta}{2}bc-\frac{T+\beta}{2}ad.
 \end{split}
 \tag{Two-row-flat-numerator}
\]
Since \(P_0\) has rank two,
\[
 p_{qP_0}^{(4)}(x,y)
 =q^2\det(\mathcal B(x,y)^TP_0\mathcal B(x,y))
 =\frac{q^2F(a,b,c,d)^2}{D_R^2}.
 \tag{Two-row-flat-raw}
\]
In particular the new leading term of \(F\) is proportional to \(R(bc-ad)\), instead of the one-row slope difference of order one in its unnormalized numerator.

### Exact finite-dimensional distinct-four energy

Now use the \(2n\) independent formal signs
\(x=\varepsilon/\sqrt N\), \(y=\eta/\sqrt N\).
Let the signs defining \(h_2\) be \(s_i\in\{-1,1\}\), with \(m\) of each sign, as in the earlier construction.
Partition the independent coordinates into the four groups
\[
 x_+:\varepsilon_i\ (s_i=1),\quad
 x_-:\varepsilon_i\ (s_i=-1),\quad
 y_+:\eta_i\ (s_i=1),\quad
 y_-:\eta_i\ (s_i=-1).
\]
Every group has \(m\) coordinates.
For instance, the product of the unweighted and signed \(\varepsilon\)-sums gives the \(-ab\) term after division by \(nN\).
The coefficients of edges between different independent coordinates in the quadratic polynomial \(nNF\) are consequently encoded by
\[
 E=\begin{pmatrix}
 -2&0&-\beta&T\\
 0&2&-T&\beta\\
 -\beta&-T&-2\alpha&0\\
 T&\beta&0&2\alpha
 \end{pmatrix}.
 \tag{Two-row-edge-table}
\]
The entry \(E_{gg}\) describes two distinct coordinates in group \(g\), not the coefficient of a coordinate square.
Coordinate-square terms cannot contribute to the fourth multilinear layer after squaring.

For a four-set of distinct independent coordinates whose group labels are \(g_1,g_2,g_3,g_4\), its coefficient in \((nNF)^2\) is
\[
 K(g_1,g_2,g_3,g_4)
 =2\left(E_{g_1g_2}E_{g_3g_4}
        +E_{g_1g_3}E_{g_2g_4}
        +E_{g_1g_4}E_{g_2g_3}\right).
 \tag{Two-row-distinct-coefficient}
\]
Each term is one pairing of the four coordinates, with a factor two for the order of the two quadratic edges.
For \(r=(r_1,r_2,r_3,r_4)\) with nonnegative integer entries and \(\sum r_j=4\), let \(g(r)\) be any list containing \(r_j\) copies of label \(j\).
Then the following finite sum over the thirty-five occupation patterns is an exact count, with \(\binom mr=0\) when \(r>m\):
\[
 S_m(T):=
 \sum_{r_1+\cdots+r_4=4}
       \left(\prod_{j=1}^4\binom m{r_j}\right)K(g(r))^2.
 \tag{Two-row-finite-count}
\]
Thus the complete distinct-four energy, including quadruples that contain both input coordinates at a common physical position, is
\[
 \boxed{\displaystyle
 \sigma_4(qP_0)^2=\frac{q^4}{D_R^4n^4N^4}S_m(T).}
 \tag{Two-row-flat-distinct-energy}
\]
Distinctness here is in the original \(2n\) independent coordinates, not in their physical-index labels.

Expanding the finite count at \(\alpha=\sqrt2\) gives
\[
 S_m(T)=A_4T^4+A_2T^2+A_0,
\]
\[
 A_4=4m^2(3m^2-4m+2),
\]
\[
 A_2=8m^2\left[(39+6\alpha)m^2-72m+36-4\alpha\right],
\]
\[
 A_0=4m\left[(339+156\alpha)m^3-(956+336\alpha)m^2
                         +(994+192\alpha)m-360\right].
 \tag{Two-row-energy-polynomial}
\]
The edge table and finite sum supply a direct reproduction of every coefficient without requiring an asymptotic collision argument.
As a check on the leading term, the only \(T\)-edges join groups \((1,4)\) and \((2,3)\), with opposite signs.
The two occupation types having two coordinates in each of one such pair contribute \(32\binom m2^2T^4\), and one coordinate in every group contributes \(4m^4T^4\).
Their sum is exactly \(A_4T^4\).
Moreover the coefficient for one coordinate from every group is \(-2(T^2+\beta^2)\), so the full energy is strictly positive for every admitted \(m,R\).

Permutations within each group preserve the squared coefficients.
Simultaneously exchanging the two physical sign classes sends the edge table to its negative and again preserves every squared coefficient.
These transformations are transitive on the \(n\) first-input coordinates and separately on the \(n\) second-input coordinates.
Each coordinate therefore has the average load within its input family, and the sum of the loads in either family is at most four times the total energy.
Consequently
\[
 \tau_4(qP_0)\le4/n.
 \tag{Two-row-flat-load}
\]
This estimate does not assert equality of the loads of the two different input families.
The physical leverage of the modes remains \(1/n\) for each mode and at most \(2/n\) for their projection.

### Exact double-ball graph-area limit

Impose only the separate bounds \(\|x\|\le2\), \(\|y\|\le2\).
Projection onto \(\operatorname{span}(h_1,h_2)\) leaves \(F\) unchanged and cannot increase either norm.
For fixed \(c,d\), the quadratic part of \(F\) in \(a,b\) is \(-ab\), with indefinite Hessian; the same holds for \(-F\).
Thus a maximum of \(|F|\) on the first disk can be taken on its boundary.
The corresponding quadratic part in \(c,d\) is \(-\alpha cd\), also indefinite, so both projected norms can be taken equal to two.
Write
\[
 (a,b)=2(\cos\theta,\sin\theta),\qquad
 (c,d)=2(\cos\phi,\sin\phi),\qquad
 p=\theta+\phi,\quad q_0=\theta-\phi.
\]
Substitution in (Two-row-flat-numerator) gives
\[
 F=2\left[T\sin q_0+\delta\cos p\sin q_0
                       -\beta\sin p(1+\cos q_0)\right].
\]
At fixed \(q_0\), maximizing the absolute value over \(p\) gives the absolute constant term plus the Euclidean norm of its sine and cosine coefficients.
Since \(T>0\), putting \(z=\cos q_0\) therefore yields the exact expression
\[
 B_R:=\sup_{\|x\|,\|y\|\le2}|F|
 =2\max_{-1\le z\le1}
 \left[T\sqrt{1-z^2}
       +\sqrt{\delta^2(1-z^2)+\beta^2(1+z)^2}\right].
 \tag{Two-row-ball-supremum}
\]
Taking \(z=0\) gives \(B_R\ge2T\), while the second square root is bounded by a constant depending only on \(\alpha\).
Consequently \(B_R=2T+O_\alpha(1)\) as \(R\to\infty\).

For each fixed \(n,R\), set \(Z_\theta=(M+\theta I)^{-1}\), with \(q=\theta^{-1}\) and \(\theta\downarrow0\).
The actual spectral decomposition gives \(Z_\theta=qP_0+O_{n,R}(1)\).
Define
\[
 \mathcal A_\theta:=
 \sup_{\|x\|,\|y\|\le2}
 \sqrt{\det(I_2+\mathcal B(x,y)^TZ_\theta^2\mathcal B(x,y))}.
\]
On this fixed-dimensional compact double ball, \(q^{-2}Z_\theta^2\to P_0\) uniformly in the resulting two-by-two matrices.
Dividing the determinant by \(q^4\), taking its continuous nonnegative square root, and then taking the supremum gives
\[
 \mathcal A_\theta=q^2\frac{B_R}{D_R}(1+o(1)).
 \tag{Two-row-flat-area}
\]
Likewise every fourth coefficient of the actual polynomial is \(q^2\) times its \(P_0\) coefficient plus \(O_{n,R}(q)\).
Positivity of the finite-count energy therefore gives
\[
 \boxed{\displaystyle
 \lim_{\theta\downarrow0}
       \frac{N^2\sigma_4(Z_\theta)}{\mathcal A_\theta}
   =\frac{\sqrt{S_m(T)}}{D_Rn^2B_R}.}
 \tag{Two-row-flat-graph-ratio}
\]
Here \(\sigma_4(Z_\theta)\) is the full fourth coefficient norm in the original two independent sign families for (Two-row-actual-fourth).
It is not the one-row coefficient functional from the preceding test.

The parameter order is first \(\theta\downarrow0\) at fixed \(n,R\), then even \(n\to\infty\) at fixed \(R\), and finally \(R\to\infty\).
The finite polynomial gives
\[
 \frac{S_m(T)}{n^4}\longrightarrow
 \frac34T^4+\frac{39+6\alpha}{2}T^2+\frac{339+156\alpha}{4}.
\]
Since \(T\sim2\delta R\), \(D_R\sim R^2\), and \(B_R\sim2T\), it follows that
\[
 \lim_{R\to\infty}R\left[
 \lim_{\substack{n\to\infty\\n\text{ even}}}
 \lim_{\theta\downarrow0}
       \frac{N^2\sigma_4(Z_\theta)}{\mathcal A_\theta}\right]
 =\frac{\sqrt3(\alpha-1)}2.
 \tag{Two-row-flat-one-power-loss}
\]
No uniform simultaneous limit is needed or claimed.
The old one-row ratio decayed like \(R^{-2}\); two original rows improve it to \(R^{-1}\), while it still tends to zero.

### Remaining actual-model obligation

This deterministic test has nonzero full fourth energy, vanishing relative coordinate load and flat physical modes, but no uniform coefficient-to-double-ball-area lower constant.
Both large inverse modes have upper auxiliary mass \((1+x_j^2)^{-1}\asymp R^{-2}\), so retaining another original row does not remove their concentration in one auxiliary channel.
The [C194v12 anti-diagonal witness](../claims/Yin_C_F0194_v12.md#anti-diagonal-witness) prevents the whole polynomial from being identically zero in its zero-diagonal case; it does not provide the missing uniform graph normalization.
The [C194v14 bridge](../claims/Yin_C_F0194_v14.md#statement) retains an explicit coefficient-to-area hypothesis and currently exposes only the first input row.
Using its method with both original rows would additionally require the actual two-input conditioning, amplitude thinning and double-ball support argument.

The concentration mechanism is measured, for actual minor inverse eigenpairs \((q_j,w_j)\), by the inverse-energy fraction
\[
 \frac{\displaystyle\sum_{j:\,
       \min(\|\Pi_1w_j\|^2,\|\Pi_2w_j\|^2)<\varepsilon}q_j^2}
      {\displaystyle\sum_jq_j^2}
 \tag{Auxiliary-concentrated-inverse-energy}
\]
on the invertible branch.
The [reviewed low-mode Gram bound](../claims/Yin_C_F0187_v13.md#decision-finite-variance-low-mode-gram-reviewed), with energy range \([-1,1]\), now supplies a fixed \(g_1>0\) such that every mode in that range has both component squared norms at least \(g_1\), outside one uniform \(o(1)\) exception.
For \(0<\varepsilon<g_1\), every mode in the numerator then has \(|q_j|<1\), so the numerator is at most \(2n\).
The [full inverse divergence](../claims/Yin_C_F0187_v10.md#finite-variance-residual-splitting) gives \(\|M^{-1}\|_{\rm F}^2/n\to\infty\) uniformly over invertible full and single-deletion minors.
Their combination makes the displayed fraction tend to zero in probability, uniformly on that branch, without dividing by the probability of invertibility.
This excludes the displayed one-channel concentration mechanism in the actual finite-variance model.
It is not by itself sufficient for general fourth-layer coercivity, since cancellation between inverse modes of different signs and the coefficient-to-area comparison still require control.

The matrices in this test satisfy the pencil's algebraic form but have no specified fixed independent Wigner entry laws or actual-model probability.
They do not supply the required weighted free bulk mass or the complete simultaneous-deletion conclusions of those theorems.
Accordingly the test neither refutes the Wigner determinant objective nor proves failure under all of its soft probabilistic controls.
It identifies the remaining quantitative geometry/probability obligation, and prevents replacing that obligation by raw nonvanishing or small coordinate load alone.

<a id="finite-variance-low-subspace-six-gram"></a>
## Reviewed low-subspace six-Gram argument and its remaining scope

The complete signed low-subspace comparison, direction estimate, projected inverse identities and high-tail transfer are fixed in [C187v14](../claims/Yin_C_F0187_v14.md#low-subspace-six-gram).
Its [proved decision](../claims/Yin_C_F0187_v14.md#decision-finite-variance-high-rank-reviewed) selects the independent review of the approximate-mode, raw tensor and high-effective-rank fourth-layer assembly.
This draft was the development home of that argument; its complete proof is now retained at the fixed Claim.

The strict spectral-window condition \(\rho<\sqrt g\) supplies a positive direction gap, and the signed compression must be used without assuming positive inverse weights.
The raw tensor in that calculation is not the fully symmetrized fourth-coordinate tensor.
Its lower bound therefore needs the separate rank-sensitive coefficient calculation before it supplies a high-rank fourth-layer lower bound.

The earlier bounded-model cross proof used a bound on \(Xv\), while the comparable-mode construction controlled words in the full input operators.
Those steps do not transfer solely from a Frobenius guard or the raw six-Gram estimate.
The separate [reviewed low-rank theorem](../claims/Yin_C_F0187_v15.md#argument) replaces them using whole-subspace injection and a compactness argument with a uniform operator-norm tail.
Its actual review and the exhaustive shifted matrix assembly remain separate from C187v14's accepted scope.

<a id="low-subspace-comparable-candidate"></a>
## Comparable-mode continuation boundary

The complete proof is fixed in [C187v15's comparable-subspace lemma](../claims/Yin_C_F0187_v15.md#comparable-subspace-lemma).
Its quantitative constant depends on the whole-subspace Gram constant, a fixed effective-rank upper bound and a fixed lower ratio for the second inverse singular value.
The proof handles signed weights by restricting to their nonzero spectral support, and passes to the limit using a uniform operator-norm tail rather than a uniformly small Frobenius tail.
It does not supply a uniform constant for an effective-rank cutoff tending to infinity.
The continuing all-regime use must choose one fixed cutoff from the high-rank theorem before applying this branch.
The [proved adoption](../claims/Yin_C_F0187_v15.md#decision-shifted-finite-variance-low-rank-reviewed) selects the independent whole-proof finding at this exact scope.

<a id="low-subspace-cross-candidate"></a>
## Cross-energy continuation boundary

The complete proof is fixed in [C187v15's cross-subspace lemma](../claims/Yin_C_F0187_v15.md#cross-subspace-lemma).
Its perpendicular injection replaces the old tangent-inversion need for a uniform bound on \(Xv\).
The [complete-layer assembly](../claims/Yin_C_F0187_v15.md#low-rank-energy-load) includes the mixed coefficient estimate controlling cancellation between the cross and residual layers.
The continuing graph application must use the complete fourth layer and its load bound, not only the nonzero raw cross tensor.
The [proved adoption](../claims/Yin_C_F0187_v15.md#decision-shifted-finite-variance-low-rank-reviewed) selects the independent whole-proof finding at this exact scope.

<a id="finite-variance-low-rank-assembly"></a>
## Reviewed all-regime finite-variance assembly and its limits

The [reviewed low-rank theorem](../claims/Yin_C_F0187_v15.md#statement) treats every deterministic scalar shift \(\theta_N\to0\), all full and single-deletion minors, and every fixed effective-rank cutoff.
Its [shifted whole-subspace argument](../claims/Yin_C_F0187_v15.md#shifted-whole-subspace) applies the adopted approximate-mode assertion at the unshifted center \(-\theta_N\).
Its own matrix reduction retains singular or high-rank minors.

The [complete reviewed assembly C186v20](../claims/Yin_C_F0186_v20.md#decision-finite-variance-two-channel-reviewed) supplies the shifted high-rank branch at the same actual minors and uses one atom-avoiding parent shift for all deletions.
Its full proof owns the exhaustive coefficient bounds, actual second-border average, \(N^{-6}\) floor and return to the unshifted matrix, together with the logarithmic probability limit and every-coupling limsup.
The second-border guard is an averaged weak-law exception; a simultaneous bound over every border is not asserted.
This result concerns the fixed real two-channel pencil with identity coupling and \(\alpha=\sqrt2\).
General matrix coefficients, complex inputs, broader parameters and full-sequence Brown convergence remain outside that theorem.


<a id="three-channel-low-rank-probe"></a>
## Conditional low-rank interfaces and the actual three-channel assembly

The [fixed conditional theorem C187v21](../claims/Yin_C_F0187_v21.md#statement), under its [proved decision](../claims/Yin_C_F0187_v21.md#decision-three-channel-low-rank-reviewed), owns the complete low-rank argument developed here.
It retains the true two-original-border Schur polynomial, the exposed corner and common parent shift, whole-head combined Gram, eigenvalue signs, explicit pole-gap thresholds and all coefficient-normalization limits.
The [actual finite and free determinant identities](Yin_D_F0010.md#three-channel-propagation-probe) connect this fixed real path tuple to F0013 and to \(P(C,D)=(C+\sqrt2D)(C+D)C-2C-\sqrt2D\) at zero in F0014.

Its [quadratic](../claims/Yin_C_F0187_v21.md#quadratic-head) and [quartic](../claims/Yin_C_F0187_v21.md#quartic-head) homogeneous bounds have scales \(q_1\) and \(q_1q_2\) under their respective first- and second-pole gaps and small-corner hypotheses.
The finite-second-moment diagonal laws supply that small corner uniformly in probability.
The [third-pole-gap argument](../claims/Yin_C_F0187_v21.md#third-pole-gap) gives the full raw sixth layer at scale \(q_1q_2q_3\) when \(q_4\le\delta_3q_3\), without a lower bound on \(q_3/q_1\).
The [original-model applicability](../claims/Yin_C_F0187_v21.md#inputs) supplies whole-head Gram only when the indicated inverse modes lie in the permitted fixed low spectral window; it does not supply those pole gaps or exhaustive branch coverage.

The [sixth-layer collision and graph interface](../claims/Yin_C_F0187_v21.md#graph-and-collision) requires
\[
 \|Z\|_F^4\bigl(\mathcal D(Z)+d_*(Z)\bigr)
       =o\bigl((q_1q_2q_3)^2\bigr).
\]
The [complete-inverse physical theorem](../claims/Yin_C_F0187_v20.md#inverse-and-truncation) supplies spread relative to \(\|Z\|_F^2\), which alone does not imply this product-scale condition when \(q_2q_3/q_1^2\to0\).
C187v21 retains the exact error comparison, graph-area bound and complete sixth-layer loads at their conditional scope.

Its same fixed [Walsh reduction](../claims/Yin_C_F0187_v21.md#graph-and-collision) explains why raw quadratic or quartic noncancellation does not establish the corresponding complete lower Walsh energy: repeated coordinates from higher homogeneous degrees can contribute and cancel there.
The [remaining-scope calculation in C187v21](../claims/Yin_C_F0187_v21.md#remaining-scope) retains the signed mixed-sixth identities; some clusters lacking a third-to-fourth pole gap are now covered at the raw level by the [proved C187v22](../claims/Yin_C_F0187_v22.md#decision-mixed-head-residual-reviewed).
At fixed whole-support Gram constant \(g>0\), \(0<d\le1\) and \(K\ge1\), its [one-head branch](../claims/Yin_C_F0187_v22.md#statement) assumes \(q_2\le\delta q_1\), \(q_3\ge dq_2\) and \(\sum_{j\ge2}q_j^2\le Kq_2^2\), and gives raw scale \(q_1q_2^2\).
Its two-head branch assumes \(q_3\le\delta q_2\) and \(\sum_{j\ge3}q_j^2\le Kq_3^2\), and gives raw scale \(q_1q_2q_3\).
Both require whole-support combined Gram on the spectral support being used and allow \(q_4\) comparable to \(q_3\).
For the original-model application using the established Gram theorem, restrict that support to the permitted low spectral subspace, and check the [tail comparison to the complete inverse](../claims/Yin_C_F0187_v22.md#three-channel-use-and-limits) at the product scale.
The later [mixed high-residual theorem](../claims/Yin_C_F0187_v23.md#statement) covers the residual regimes not supplied by these earlier conditional results.
The [all-scale physical assembly](../claims/Yin_C_F0187_v24.md#statement) supplies compatible complete-inverse energy and loads through refined head-residual estimates, without assuming the stronger coarse product-scale spread condition displayed above.
The [adopted original-row bridge](../claims/Yin_C_F0194_v16.md#decision-three-channel-sixth-bridge-reviewed) then converts the complete top layer into an unconditional probability floor for the fixed pencil and its cubic.
The earlier lower-Walsh cancellation warning remains valid; this successful assembly uses the sixth layer.
Middle logarithmic control, determinant limits, arbitrary coefficients, complex inputs and Brown convergence remain outside these results.

<a id="mixed-high-residual-tensor-candidate"></a>
## Mixed high-residual theorem and its complete-inverse application

The complete argument developed here is fixed in [C187v23](../claims/Yin_C_F0187_v23.md#statement), under its [proved decision](../claims/Yin_C_F0187_v23.md#decision-mixed-high-residual-reviewed) adopting independent whole-proof review.
The fixed [one-head](../claims/Yin_C_F0187_v23.md#one-head-high-residual) and [two-head](../claims/Yin_C_F0187_v23.md#two-head-high-residual) estimates have raw tensor scales \(q_1\|A\|_F^2\) and \(q_1q_2\|A\|_F\), respectively, under their residual effective-rank and head-to-residual gap hypotheses.
The [ordered all-scale assembly](../claims/Yin_C_F0187_v23.md#all-scale-assembly) gives the \(q_1q_2q_3\) tensor bound on a spectral support satisfying the whole-space Gram condition.
The [weaker two-branch interface](../claims/Yin_C_F0187_v23.md#weaker-residual-interface) instead requires only head-space Gram, a global stack upper bound and quadratic Frobenius separation for the complete residual.
It does not remove the whole-space Gram hypothesis from the all-scale assertion.

For the continuing physical application, the [precise transfer limits](../claims/Yin_C_F0187_v23.md#physical-transfer-limit) remain essential.
A complete physical mode space cannot satisfy the whole-space Gram hypothesis.
The existing bounded-operator-tail comparison in sphere supremum does not automatically bound the difference of sixth-order tensors in Frobenius norm.
The [proved complete-inverse theorem C187v24](../claims/Yin_C_F0187_v24.md#decision-all-scale-physical-reviewed) now verifies the weaker residual interface on the original model and supplies a compatible all-scale physical coefficient assembly.
Its [mixed collision proof](../claims/Yin_C_F0187_v24.md#mixed-physical-collisions) uses each residual's own normalized spread and the physical delocalization of the retained heads, avoiding the coarse product-scale condition from C187v21.
The resulting complete sixth-layer energy, grouped loads and bounded-boundary graph-area scale retain their precise [original-law coefficient scope](../claims/Yin_C_F0187_v24.md#statement).
The separate [adopted original-row application](../claims/Yin_C_F0194_v16.md#decision-three-channel-sixth-bridge-reviewed) supplies graph-distance probabilities and an unshifted \(N^{-17/2}\) probability floor for the fixed pencil and ordered cubic.
The separate [adopted middle theorem](../claims/Yin_C_F0187_v25.md#decision-three-channel-middle-reviewed) and [complete determinant assembly](../claims/Yin_C_F0186_v21.md#decision-finite-variance-three-channel-reviewed) now supply the fixed-model logarithmic probability limit and every-coupling limsup; these coefficient statements and the floor alone do not imply those conclusions or Brown convergence.

<a id="three-channel-middle-frobenius-obstruction"></a>
## The middle trace requires additional random geometry

The complete [deterministic retained-kernel counterexample](../ledger/Yin_L_F0066_v8.md#three-channel-middle-frobenius-obstruction) fixes the failure of a uniform three-channel covariance trace bound from Frobenius or operator-norm upper control alone.
Its actual retained-row kernel has dimension \(3m\), while the center-direction observed trace is arbitrarily small relative to \(m\).
This is ordinary checked exploration, not an independent review or a counterexample to the Wigner Tasks.
The [fixed random-geometric comparison](../ledger/Yin_L_F0066_v8.md#what-the-random-geometric-inputs-do-and-do-not-supply) identifies the missing transfer from the available approximate-mode theorem to the actual retained-row kernel.
The [adopted large-block joint-gap argument](../claims/Yin_C_F0187_v25.md#retained-kernel-trace) now supplies the needed random-geometric estimate for the fixed three-channel path before invoking the middle-row concentration mechanism.

<a id="three-channel-middle-random-bridge-candidate"></a>
## Reviewed joint-gap route to the three-channel middle range

The complete argument developed here is fixed in [C187v25](../claims/Yin_C_F0187_v25.md#statement), under its [proved assessment](../claims/Yin_C_F0187_v25.md#decision-three-channel-middle-reviewed) and [independent whole-proof finding](../audits/reviews/Yin_R_F0191_v25.md#three-channel-middle-whole-proof).
Its [large-principal-block joint gap](../claims/Yin_C_F0187_v25.md#large-block-joint-gap) covers all real scalar centers with weight \(1+|\beta|\), any deterministic family of at most \(N^2\) blocks of size at least \(N/3\), and one common tail exception.
The [actual retained-kernel bridge](../claims/Yin_C_F0187_v25.md#retained-kernel-trace) uses that random input and a Frobenius guard to obtain \(H_a\ge cN(m/N)^6\) uniformly over the genuine two-input covariance directions.
It does not identify a retained-row kernel with a low spectral space or weaken the [fixed deterministic obstruction](../ledger/Yin_L_F0066_v8.md#three-channel-middle-frobenius-obstruction).
The [fresh-row and index argument](../claims/Yin_C_F0187_v25.md#fresh-row-middle-indices) gives the profile \((j/N)^{7/2}\) above cutoff \(N^{5/6}(\log N)^{1/6}\), with all local guards measurable under the true deleted-row conditioning.
Its [logarithmic calculation](../claims/Yin_C_F0187_v25.md#middle-logarithms) combines that estimate with the separately proved C194v16 floor to remove the omitted bottom range in probability.
The fixed Claim owns every necessary proof and probability detail, with the review relationship retained in R.
The separate [adopted determinant assembly](../claims/Yin_C_F0186_v21.md#decision-finite-variance-three-channel-reviewed) supplies the fixed-model logarithmic conclusions; the broader Task contracts remain unresolved.

<a id="positive-frame-bounded-inverse-energy"></a>
## Complete Schur control when normalized inverse energy stays bounded

The complete argument developed here is fixed as the [adopted C194v18 theorem](../claims/Yin_C_F0194_v18.md#decision-low-inverse-energy-reviewed), with [independent whole-proof review](../audits/reviews/Yin_R_F0200_v20.md#low-inverse-energy-whole-proof).
Its [exact statement](../claims/Yin_C_F0194_v18.md#statement) covers arbitrary fixed real symmetric coefficient dimensions and the original real finite-second-moment laws, without a positive frame assumption.
For an actual invertible minor, bounded normalized inverse energy \(\|M^{-1}\|_F^2/N\) supplies a nonzero complete Schur numerator and explicit conditional graph-distance and normalized-determinant tails.
The [fixed-eta leave-one-out proof](../claims/Yin_C_F0194_v18.md#fixed-eta-identity) derives the actual mean-Schur inverse relation and returns to zero on the random energy branch through a deterministic trace-norm estimate.
It uses no external Dyson theorem or local law and never changes the original fresh-row conditioning.
The [slow-threshold deduction](../claims/Yin_C_F0194_v18.md#slow-thresholds) gives one deterministic \(K_N\to\infty\), at most logarithmic, with vanishing marginal and averaged low-branch distance errors at every fixed inverse-power threshold.
It preserves one real vanishing parent shift and all fixed deletion sizes without claiming a simultaneous-minor event.
The [remaining high-energy boundary](../claims/Yin_C_F0194_v18.md#remaining-scope) retains the separate head/residual physical and original-law probability obligations; divergence of the whole inverse energy alone does not establish them.
No parent least-value floor, determinant theorem or general Task completion follows from this branch alone.

<a id="positive-frame-divergent-free-inverse-energy"></a>
## Physical spread from a divergent free inverse-square integral

The complete geometric argument and its exact source applications are fixed and adopted in [C187v26](../claims/Yin_C_F0187_v26.md#decision-positive-frame-spectral-spread-reviewed), with independent whole-proof review.
Its [statement](../claims/Yin_C_F0187_v26.md#statement) covers arbitrary fixed real symmetric coefficient dimensions with positive complex-direction frame, original real finite-second-moment inputs, a common deterministic real vanishing shift, and zero in the free spectral support.
The [C95 applicability check](../claims/Yin_C_F0187_v26.md#free-gap-criterion) reuses the adopted matrix rational inverse criterion to identify finite free inverse-square energy exactly with a free spectral gap; it makes no new rational-boundedness claim and does not require the positive frame.
The [full imaginary-resolvent covariance](../claims/Yin_C_F0187_v26.md#full-imaginary-covariance) and [physical projector argument](../claims/Yin_C_F0187_v26.md#physical-projectors) replace path-specific linear low-window mass by \(J(h)=\int(x^2+h^2)^{-1}\,d\mu(x)\), with fixed-\(h\) summable original-row errors.
The [capped residual energy](../claims/Yin_C_F0187_v26.md#residual-energy), separate [row and diagonal splittings](../claims/Yin_C_F0187_v26.md#residual-spread), and [cutoff/head consequences](../claims/Yin_C_F0187_v26.md#cutoff-and-heads) supply the stated almost-sure fixed-deletion and finite-mode-removal geometry.
For the intended \(m=3\) application, the fixed-\(d\) local-factor and complete sixth-coefficient transfer is [adopted in C187v27](../claims/Yin_C_F0187_v27.md#decision-positive-frame-complete-sixth-reviewed), and the common-shift probability and logarithmic assembly is [adopted in C186v22](../claims/Yin_C_F0186_v22.md#decision-positive-frame-spectral-point-assembly-reviewed).
Actual high inverse energy in the complementary free-gap case remains separate, as explained in [the exact remaining scope](../claims/Yin_C_F0187_v26.md#remaining-scope).
No general-coefficient least-value floor, determinant theorem or Task completion is inferred here.

<a id="positive-frame-fixed-d-sixth-coefficients"></a>
## Fixed-input-count physical sixth coefficients on the free spectrum

The complete statement and argument are fixed in [C187v27](../claims/Yin_C_F0187_v27.md#statement), under its [proved decision](../claims/Yin_C_F0187_v27.md#decision-positive-frame-complete-sixth-reviewed) and independent whole-proof review.
Its [actual local maps](../claims/Yin_C_F0187_v27.md#whole-space-local-maps), [mixed physical collisions](../claims/Yin_C_F0187_v27.md#mixed-physical-collisions), and [complete spectral allocation](../claims/Yin_C_F0187_v27.md#complete-spectral-allocation) use the adopted C187v26 geometry and fixed raw coefficient inputs on the complete inverse.
The [sixth-layer calculation](../claims/Yin_C_F0187_v27.md#complete-sixth-layer) retains all \(dn\) individual variables, physical groups of size \(d\), the exact \(6!\) counting and the complete grouped loads.
The [graph-area application](../claims/Yin_C_F0187_v27.md#graph-area-and-probability-interface) matches the adopted conditional C194v19 bridge with \(a_i=(1+4d\Lambda)^{3/2}q_1q_2q_3\), after a separate common real vanishing shift makes the required actual minors invertible.
The [adopted C186v22 assembly](../claims/Yin_C_F0186_v22.md#decision-positive-frame-spectral-point-assembly-reviewed) now supplies that common shift, the quantitative unshifted return, the probability logarithmic limit and the every-coupling almost-sure limsup at this precise spectral-point scope.
Actual high inverse energy in the complementary free-gap case remains outside this branch.
The coefficient theorem itself retains its conditional interface; C186v22 supplies the parent and logarithmic conclusions only within its stated spectral-point scope, and the general Task remains unresolved.
