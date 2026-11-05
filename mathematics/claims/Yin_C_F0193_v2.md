---
author: Yin
---

# Haar affine determinant limits through an invertible complementary corner

This is the complementary-corner extension of the [proved first version of C_F0193](Yin_C_F0193_v1.md#decision-conditional-schur-reviewed).
It addresses the same [Haar affine-pencil contract](../tasks/Yin_T_F0015_v1.md#contract), with a weaker inverse hypothesis and an explicit larger positive-FK, unbounded-inverse class.
The analytic input is exactly the retained [conditional Haar-additive statement](Yin_C_F0193_v1.md#conditional-haar-additive-statement), as adopted at [decision-conditional-schur-reviewed](Yin_C_F0193_v1.md#decision-conditional-schur-reviewed).
Its complete proof remains in the first version.
The [independent complementary-corner review](../audits/reviews/Yin_R_F0198_v2.md#independent-complementary-corner-proof) supports this extension at its exact stated scope.

<a id="statement"></a>
## Exact complementary-corner statement

Fix integers \(m,r\ge1\), fixed matrices \(A_0,\ldots,A_{r-1}\in M_m(\mathbb C)\), and a fixed nonzero rank-one matrix \(A_r=pq^*\), with \(p,q\in\mathbb C^m\).
For every \(N\), let \(U_1^{(N)},\ldots,U_{r-1}^{(N)},V_N\) be independent Haar matrices on the full group \(U(N)\).
They may have any dependence between dimensions on their common probability space.
Set
\[
 B_N=A_0\otimes I_N+\sum_{j=1}^{r-1}A_j\otimes U_j^{(N)},
 \qquad L_N=B_N+(pq^*)\otimes V_N.
\]
Let \(u_1,\ldots,u_{r-1},v\) be free Haar unitaries in a finite von Neumann algebra \((M,\tau)\) with faithful normal tracial state, and let \(B,L\in M_m(M)\) be the corresponding free pencils.
Write \(\tau_m=\operatorname{tr}_m\otimes\tau\), with normalized matrix trace, and use the ordinary determinant convention including all zero spectral mass.

Put \(\kappa=\|p\|\|q\|>0\).
Choose fixed auxiliary unitaries \(P,Q\in U(m)\) satisfying
\[
 Pp=\|p\|e_1,\qquad Qe_1=q/\|q\|,
 \qquad P(pq^*)Q=\kappa E_{11}.
\]
For \(m\ge2\), write
\[
 B'=(P\otimes1)B(Q\otimes1)
   =\begin{pmatrix}a&b\\c&D\end{pmatrix},
\]
where \(a\in M\), \(b\in M_{1,m-1}(M)\), \(c\in M_{m-1,1}(M)\), and \(D\in M_{m-1}(M)\).
Assume only that \(D\) has a bounded inverse and define
\[
 h=a-bD^{-1}c,\qquad e=h/\kappa\in M.
\]
For \(m=1\), omit the complementary corner and its inverse assumption and put \(h=(P\otimes1)B(Q\otimes1)\), \(e=h/\kappa\).
No normalized trace on a zero-dimensional matrix algebra is used.

Let \(\mu\) be the spectral distribution of \(|e|\) under \(\tau\).
Assume the two strict moment inequalities
\[
 \int_{[0,\infty)}t^2\,d\mu(t)>1,
 \qquad
 \int_{[0,\infty)}t^{-2}\,d\mu(t)>1.
 \tag{Corner-bulk}
\]
Here \(0^{-2}=+\infty\), and the second integral is an extended nonnegative integral.
It is a moment of the modulus distribution, not an assumption that an inverse operator for \(e\) exists.
In particular \(e\) is allowed to have nonzero kernel.

Then \(\Delta_{\tau_m}(L)>0\), \(L\) has no bounded inverse, and every allowed cross-dimensional coupling satisfies
\[
 \frac1{mN}\log|\det L_N|
 \longrightarrow\log\Delta_{\tau_m}(L)\in\mathbb R
 \quad\text{almost surely}.
 \tag{Corner-limit}
\]
The probability-one event may depend on the fixed coefficient tuple and its coupling.
This proves both the full-limit and upper-limit assertions in both coupling regimes of F0015 for the stated class.
For \(m\ge2\), the exact free normalization is
\[
 m\log\Delta_{\tau_m}(L)
 =(m-1)\log\Delta_{\operatorname{tr}_{m-1}\otimes\tau}(D)
  +\log\kappa+\log\Delta_\tau(e+v).
 \tag{Corner-free}
\]
For \(m=1\), the first term is omitted and the identity is \(\log\Delta(L)=\log\kappa+\log\Delta(e+v)\).
No inverse of the full background \(B\), of \(h\), or of \(e\) is assumed.

The result contains the [earlier rank-one affine class](Yin_C_F0193_v1.md#affine-schur-statement), with the same actual scalar deformation on that common domain.
It also directly contains the first version's scalar strict-triangle class through the empty-corner case.
The proof below gives an original two-input matrix example where both one-input full backgrounds fail to be invertible but the complementary corner is boundedly invertible.

## Exact retained inputs

The [proved v1 conditional Haar-additive theorem](Yin_C_F0193_v1.md#conditional-haar-additive-statement), under its [selected proved decision](Yin_C_F0193_v1.md#decision-conditional-schur-reviewed), supplies the physical-size logarithmic limit after the background guard is established.
Its probability quantifiers, conditional uniformity, singular-law target and logarithmic integrability are reused at exactly that scope.
The first version's independent review does not itself review the new block reduction or new inverse hypotheses here.

The [strong Haar background interface](../ledger/Yin_L_F0062_v1.md#haar-pencils), with the [CM14 source note](../audits/literature/CM14/readme.md), supplies fixed-coefficient strong convergence and the bounded-inverse approximation argument.
The [accepted HZ25 bulk interface](../audits/literature/HZ25/Yin_U001.md#subordination-neighborhood), Theorem 2.3 and formulas (2.4)--(2.6) in arXiv v4, verifies the strict moment test and its exceptional atom condition for the actual deformation.
The [ordinary bounded FK product theorem](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) is used for bounded elimination factors, including possible zero determinant of a remaining factor.
The [triangular interface in Luc22 Theorem 14.18](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant) is used only for unipotent factors with identity diagonal maps, where its injectivity and dense-range hypotheses hold.
The direct-sum determinant formula is obtained from block diagonal spectral functional calculus.

<a id="argument"></a>
## Complete complementary-corner argument

### Exact unitary normalization

Choose the first row of \(P\) to be \(p^*/\|p\|\), and complete it to an orthonormal row basis.
Choose the first column of \(Q\) to be \(q/\|q\|\), and complete it to an orthonormal column basis.
Then \(q^*Q=\|q\|e_1^*\), giving the displayed normalization with positive real \(\kappa\).
The matrices are deterministic and applied at every dimension and to the free tuple.
Their left and right multiplication preserves the singular values of the full finite pencil and the modulus spectral distribution of the full free pencil.
It therefore preserves the ordinary determinant magnitude and ordinary FK determinant.
It changes no input law or cross-dimensional coupling.

Different orthonormal completions change the complementary corner only by fixed left and right auxiliary unitaries.
Explicitly, replacing \(P,Q\) by \(\operatorname{diag}(1,W)P\) and \(Q\operatorname{diag}(1,Z)\) sends \((b,c,D)\) to \((bZ,Wc,WDZ)\).
Thus bounded invertibility of the complementary corner and the scalar value \(h=a-bD^{-1}c\) are unchanged by those completion choices.

### Rational background and the actual conditional guard

Write the finite transformed background in the matching blocks
\[
 (P\otimes I_N)B_N(Q\otimes I_N)
 =\begin{pmatrix}a_N&b_N\\c_N&D_N\end{pmatrix}.
\]
For \(m\ge2\), \(D_N\) has physical dimension \((m-1)N\) and is a fixed-coefficient polynomial in the background Haar inputs.
Strong Haar convergence and the bounded inverse of \(D\) give eventual invertibility of \(D_N\) with a deterministic eventual inverse bound on one probability-one event.
This follows from the common spectral gap and uniform polynomial approximation of the reciprocal on that gap.
The same approximations show that
\[
 h_N=a_N-b_ND_N^{-1}c_N,\qquad E_N=h_N/\kappa
\]
converge strongly to \(h,e\).
In particular \(E_N\) has a deterministic eventual norm bound and its singular empirical distribution converges almost surely to \(\mu\).
For an early background where \(D_N\) is not invertible, define \(E_N=0\) solely to make it a measurable statistic at every dimension.
This convention agrees eventually almost surely with the displayed rational expression.

For \(m=1\), put \(E_N=a_N/\kappa\); the same norm and singular-law facts follow directly from fixed-coefficient Haar convergence.
At each dimension, \(E_N\) is measurable with respect to the background generated by only \(U_1^{(N)},\ldots,U_{r-1}^{(N)}\).
Conditioning on that dimension's background leaves \(V_N\) Haar on the full physical group \(U(N)\).
The complete background sequence is not conditioned on.
Thus the exact eventual guard and conditional Haar hypotheses of the retained v1 theorem hold under every allowed coupling.

### Determinant identities with a possibly singular Schur factor

For every sufficiently large finite input at which \(D_N\) is invertible, define
\[
 F_N=\begin{pmatrix}I_N&0\\-D_N^{-1}c_N&I_{(m-1)N}\end{pmatrix},
 \qquad
 G_N=\begin{pmatrix}I_N&-b_ND_N^{-1}\\0&I_{(m-1)N}\end{pmatrix}.
\]
Direct multiplication gives
\[
 G_NL_N'F_N=\operatorname{diag}(h_N+\kappa V_N,D_N),
 \qquad L_N'=(P\otimes I_N)L_N(Q\otimes I_N).
\]
Both finite elimination determinants are one, and the fixed unitaries have determinant magnitude one.
Consequently
\[
 |\det L_N|
 =|\det D_N|\,\kappa^N|\det(E_N+V_N)|.
 \tag{Corner-finite}
\]
The computation has used no inverse of \(h_N+\kappa V_N\).

The free elimination factors are bounded unipotent matrices because \(D^{-1}\) is bounded.
Their ordinary FK determinants are one by the retained triangular theorem applied only to their identity diagonal blocks.
The Schur operator is not supplied as a diagonal premise of that triangular theorem.
The ordinary determinant of the resulting block diagonal operator is computed directly from its spectral direct sum, even if a block has kernel or ordinary determinant zero.
Applying bounded ordinary FK multiplicativity yields (Corner-free).
Its \(D\) contribution and \(\log\kappa\) are finite, so the equality remains meaningful if the last logarithm is \(-\infty\).
For \(m=1\) the scalar identity \(L_N'=\kappa(E_N+V_N)\) gives both formulas with the complementary contribution omitted.

### Strict bulk, possible kernel and the actual free target

The first inequality in (Corner-bulk) implies \(\mu\ne\delta_0\).
If \(\mu\) were any one-radius point mass \(\delta_t\), its second and inverse-square moments could not both exceed one.
Therefore its symmetrization is supported at more than two points.
For the Haar unitary, \(|v|=1\) has zero mass at zero.
The exceptional zero-atom condition in the accepted HZ25 interface is therefore \(\mu(\{0\})+0\ge1\).
It is excluded by \(\mu\ne\delta_0\), so no assumption \(\mu(\{0\})=0\) is needed.
In the inverse-square moment test, a nonzero kernel merely makes the second integral infinite.
The two strict moment inequalities place zero in the required regular bulk of the symmetrized singular convolution with the Haar unitary.

Apply the retained v1 conditional theorem to \(E_N+V_N\).
It gives a full almost-sure logarithmic limit and a weak singular-value limit with finite logarithmic integral under every allowed cross-dimensional coupling.
The retained theorem expresses its free target through a positive operator of law \(\mu\), whereas the actual \(e\) here may be nonnormal or have kernel.
Strong convergence of the original Haar tuple, with the bounded rational approximations already established, independently identifies the singular-law limit of \(E_N+V_N\) with that of \(|e+v|\).
Uniqueness of the weak limit therefore matches the actual free target with the retained theorem's integrable logarithmic target.
Hence
\[
 \frac1N\log|\det(E_N+V_N)|
 \longrightarrow\log\Delta_\tau(e+v)\in\mathbb R
 \quad\text{almost surely}.
\]
No replacement of \(e\) by \(|e|\) inside the original pencil is performed.

For \(m\ge2\), the bounded inverse of \(D\) also gives
\[
 \frac1{(m-1)N}\log|\det D_N|
 \longrightarrow
 \log\Delta_{\operatorname{tr}_{m-1}\otimes\tau}(D)
\]
almost surely, by a continuous logarithmic spectral test on the eventual common gap.
Divide (Corner-finite) by \(mN\), combine the two limits, and use (Corner-free).
The weights are exactly \((m-1)/m\), \(1/m\), and \(1/m\), respectively.
The empty-corner convention gives the same conclusion when \(m=1\).
This proves (Corner-limit).

The regular-bulk bound gives finite \(\log\Delta(e+v)\) and a positive limit of the negative imaginary Cauchy transform at zero.
The latter excludes a spectral gap of \(|e+v|\) at zero, since such a gap would make that imaginary transform tend to zero.
Thus \(e+v\) has positive ordinary FK determinant and no bounded inverse.
The bounded unipotent equivalence of \(L'\) with \(\operatorname{diag}(\kappa(e+v),D)\) transfers both conclusions to \(L\).
This remains valid when \(e\) itself is noninjective.

<a id="earlier-class-containment"></a>
## Containment of the earlier rank-one compression class

Assume the first version's full-background and scalar-compression inverse hypotheses for the same selected coefficient \(pq^*\).
Its scalar compression is
\[
 c_{\mathrm{old}}=(q^*\otimes1)B^{-1}(p\otimes1).
\]
Under the fixed normalization above,
\[
 (B'^{-1})_{11}
 =\frac1{\|p\|\|q\|}(q^*\otimes1)B^{-1}(p\otimes1)
 =c_{\mathrm{old}}/\kappa.
\]
This upper-left corner is boundedly invertible.
Apply bounded block elimination to \(B'^{-1}\) using that pivot.
The lower Schur complement is boundedly invertible because \(B'^{-1}\) is invertible.
The lower-right block of its inverse \(B'\), namely \(D\), is the inverse of that Schur complement, and is therefore boundedly invertible.
With this \(D\), the ordinary inverse formula for \(B'\) gives \((B'^{-1})_{11}=h^{-1}\).
Consequently
\[
 c_{\mathrm{old}}=\kappa h^{-1},\qquad
 d_{\mathrm{old}}=c_{\mathrm{old}}^{-1}=h/\kappa=e.
\]
The old and new bulk hypotheses are the same tests on the same scalar operator on this common domain.
For \(m=1\) the complementary inverse condition is absent and the same scalar identity follows directly.
Thus the new inverse hypothesis contains the earlier rank-one class, while the preceding proof additionally allows a singular full background and a noninvertible scalar Schur deformation.

The first version's optional coefficient-position permutation may still be applied before this reduction.
It preserves the actual finite and free determinant questions by [C_F0192_v1](Yin_C_F0192_v1.md#coefficient-gauge).
The complementary corner and bulk conditions must then be checked on the actual transformed ordered tuple.

<a id="explicit-corner-example"></a>
## Explicit original pencil and exact corner matching

Consider two independent Haar inputs at each dimension and fixed scalar parameters \(\alpha,\beta,\gamma,\delta\), with \((\beta,\delta)\ne(0,0)\):
\[
 M_N=\begin{pmatrix}I_N+\alpha U_N&\beta V_N\\
                    \gamma U_N&I_N+\delta V_N\end{pmatrix}.
\]
Its fresh coefficient is \(A_2=(\beta,\delta)^T(0,1)\).
Put \(\kappa=\sqrt{|\beta|^2+|\delta|^2}\), \(\varepsilon_0=\alpha\delta-\beta\gamma\), and choose
\[
 P=\frac1\kappa
   \begin{pmatrix}\overline\beta&\overline\delta\\-\delta&\beta\end{pmatrix},
 \qquad
 Q=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Both are unitary, \(P(\beta,\delta)^T=\kappa e_1\), and \(Qe_1=e_2\).
The transformed background blocks are
\[
 a_N'=\frac{\overline\delta}\kappa I_N,
 \quad
 b_N'=\frac{\overline\beta I_N+
               (\overline\beta\alpha+\overline\delta\gamma)U_N}{\kappa},
 \quad
 c_N'=\frac\beta\kappa I_N,
 \quad
 D_N'=-\frac{\delta I_N+\varepsilon_0U_N}{\kappa}.
\]
If \(|\delta|\ne|\varepsilon_0|\), this is a boundedly invertible complementary corner.
Commuting scalar functional calculus in \(U_N\) gives the exact physical Schur deformation
\[
 \frac{a_N'-b_N'(D_N')^{-1}c_N'}\kappa
 =\frac{I_N+\alpha U_N}
        {\delta I_N+(\alpha\delta-\beta\gamma)U_N}.
\]
The numerator calculation is
\[
 \overline\delta(\delta+\varepsilon_0 z)
 +\beta\bigl(\overline\beta+
        (\overline\beta\alpha+\overline\delta\gamma)z\bigr)
 =\kappa^2(1+\alpha z).
\]
This identifies the actual corner and scalar deformation; no distinct polynomial witness is substituted.
There is no requirement \(|\alpha|\ne1\).

Now take \(\alpha=\beta=\delta=1\) and \(\gamma=1/2\).
Then the original coefficients and transformed objects are
\[
 A_0=I_2,\qquad
 A_1=\begin{pmatrix}1&0\\1/2&0\end{pmatrix},\qquad
 A_2=\begin{pmatrix}0&1\\0&1\end{pmatrix},
\]
\[
 \kappa=\sqrt2,\qquad
 D'=-\frac{1+u/2}{\sqrt2},\qquad
 h'=\sqrt2\frac{1+u}{1+u/2},\qquad
 e=\frac{1+u}{1+u/2}.
\]
The corner has a bounded inverse because \(|1+z/2|\ge1/2\) on the unit circle.
The exact moments are
\[
 \int_{\mathbb T}|e(z)|^2\,dm(z)=\frac43,
 \qquad
 \int_{\mathbb T}|e(z)|^{-2}\,dm(z)=+\infty.
\]
For the first equality use \(e(z)=1+(z/2)/(1+z/2)\), expand the geometric series, and sum its squared Fourier coefficients.
For the second, \(1+z\) has a simple zero at \(z=-1\) while \(1+z/2\) is nonzero there, so its inverse-square circle integral diverges.
That single zero has Haar measure zero.

For either choice of a fresh rank-one input in this example, the full one-input background has a triangular diagonal factor \(1+u\) or \(1+v\).
It has no bounded inverse because a Haar unitary has the entire circle as spectrum.
The earlier full-background inverse hypothesis therefore fails, while the complementary-corner hypothesis and strict bulk hold.
An optional coefficient-position permutation cannot remove this failure: after a rank-one position is selected, the other two positions are \(I_2\) and the remaining rank-one matrix, and their single-Haar pencil is unitarily equivalent to \(I_2+A_j\otimes w\), whose nonzero scalar eigenvalue is one.
Hence its factor \(1+w\) still has no bounded inverse.
This is a strict enlargement of the earlier rank-one compression class.

The single-Haar scalar factor \(1+u/2\) has circle logarithmic integral zero, so
\[
 \log\Delta(D')=-\tfrac12\log2,
 \qquad\log\kappa=\tfrac12\log2.
\]
The complementary and scalar normalizing contributions cancel, giving
\[
 2\log\Delta(M)=\log\Delta(e+v).
\]
This agrees with the direct off-diagonal unitary-pivot reduction and supplies a positive-FK, unbounded-free-inverse example under the original fixed coefficients and coupling requirements.

## Remaining Task scope

The extension requires a selected rank-one coefficient and an invertible complementary corner in its actual normalized background.
It supplies no such corner automatically for every dense tuple.
For a higher-rank selected coefficient the Schur block contains a repeated tensor-Haar input rather than the physical full Haar input of the retained conditional theorem.
The excluded bulk boundary and general higher-rank regimes remain outside the present result.

## Current assessment
[Selected decision](#decision-complementary-corner-reviewed)

## Assessment history

### Decision complementary-corner-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:05 |
| status | open |
| reason | The complementary-corner extension weakens the full-background inverse requirements while retaining the proved v1 conditional Haar-additive input; its complete new reduction, kernel convention, class containment and exact original example await separate review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complementary-corner theorem](#statement) | Fixed rank-one selected coefficient, boundedly invertible complementary corner, strict extended modulus moments, full almost-sure ordinary determinant limit under every coupling, positive FK determinant and no bounded inverse, including the empty-corner case and the stated containment and example. |
| argument | [Complete new complementary-corner proof](#argument) | Exact auxiliary unitaries, rational background guard, ordinary finite/free elimination without a singular-diagonal premise, actual nonnormal free target, normalization, kernel convention, old-class containment and explicit new pencil. |
| dependency | [Proved conditional Haar-additive lemma](Yin_C_F0193_v1.md#conditional-haar-additive-statement) | Only the analytic conditional logarithmic and weak singular limits under the exact background and regular-bulk hypotheses, as adopted at v1 decision-conditional-schur-reviewed. Its proof is reused without duplication. |
| dependency | [Strong Haar background interface](../ledger/Yin_L_F0062_v1.md#haar-pencils) | Only fixed-coefficient strong convergence under the stated coupling quantifier and its bounded inverse, rational approximation and continuous logarithmic consequences for the actual complementary corner. |
| dependency | [HZ25 accepted bulk interface](../audits/literature/HZ25/Yin_U001.md#hz25-u001) | Only Theorem 2.3, formulas (2.4)--(2.6), and the regular-bulk convention in the inspected arXiv v4, used to verify the strict extended modulus moments and the exceptional zero-atom condition. |
| dependency | [Ordinary bounded FK products](../audits/literature/FK52/Yin_U001.md#fk52-u001) | Only bounded ordinary multiplicativity, including zero determinants, for the displayed unipotent elimination and scalar factors. |
| dependency | [Identity-diagonal triangular factors](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only Theorem 14.18 for bounded unipotent factors with identity diagonal maps, with all required injectivity and dense-range hypotheses. |
| dependency | [Coefficient-position symmetry](Yin_C_F0192_v1.md#coefficient-gauge) | Only the optional initial coefficient permutation and the explicit comparison of the original example with prior full-background hypotheses; it does not establish a complementary inverse or bulk condition. |

### Decision complementary-corner-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:23 |
| status | proved |
| reason | Independent review checked the complete complementary-corner theorem and all declared inputs, including the weaker inverse hypothesis, possible kernel, empty corner, class containment and exact original example; no mathematical gap remains in this restricted statement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complementary-corner theorem](#statement) | Fixed rank-one selected coefficient, boundedly invertible complementary corner, strict extended modulus moments, full almost-sure ordinary determinant limit under every coupling, positive FK determinant and no bounded inverse, including the empty-corner case and the stated containment and example. |
| argument | [Complete new complementary-corner proof](#argument) | Exact auxiliary unitaries, rational background guard, ordinary finite/free elimination without a singular-diagonal premise, actual nonnormal free target, normalization, kernel convention, old-class containment and explicit new pencil. |
| dependency | [Proved conditional Haar-additive lemma](Yin_C_F0193_v1.md#conditional-haar-additive-statement) | Only the analytic conditional logarithmic and weak singular limits under the exact background and regular-bulk hypotheses, as adopted at v1 decision-conditional-schur-reviewed. Its proof is reused without duplication. |
| dependency | [Strong Haar background interface](../ledger/Yin_L_F0062_v1.md#haar-pencils) | Only fixed-coefficient strong convergence under the stated coupling quantifier and its bounded inverse, rational approximation and continuous logarithmic consequences for the actual complementary corner. |
| dependency | [HZ25 accepted bulk interface](../audits/literature/HZ25/Yin_U001.md#hz25-u001) | Only Theorem 2.3, formulas (2.4)--(2.6), and the regular-bulk convention in the inspected arXiv v4, used to verify the strict extended modulus moments and the exceptional zero-atom condition. |
| dependency | [Ordinary bounded FK products](../audits/literature/FK52/Yin_U001.md#fk52-u001) | Only bounded ordinary multiplicativity, including zero determinants, for the displayed unipotent elimination and scalar factors. |
| dependency | [Identity-diagonal triangular factors](../audits/literature/Luc22/Yin_U001.md#luc22-u001) | Only Theorem 14.18 for bounded unipotent factors with identity diagonal maps, with all required injectivity and dense-range hypotheses. |
| dependency | [Coefficient-position symmetry](Yin_C_F0192_v1.md#coefficient-gauge) | Only the optional initial coefficient permutation and the explicit comparison of the original example with prior full-background hypotheses; it does not establish a complementary inverse or bulk condition. |
| review | [Independent complementary-corner finding](../audits/reviews/Yin_R_F0198_v2.md#independent-complementary-corner-proof) | Complete exact restricted theorem, proof, direct dependencies, containment and original strict-enlargement example. |

