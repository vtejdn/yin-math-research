---
author: Yin
---

# Full almost-sure determinant limits for arbitrary Haar affine pencils

This version extends the [reviewed structural Haar results](Yin_C_F0192_v1.md#decision-haar-structural-reviewed) to the complete coefficient scope of [F0015](../tasks/Yin_T_F0015_v1.md#contract).
Its new mechanisms are a fixed-dimensional unitary-frame repair, a randomly centered Cayley-chart algebraic tube estimate, and quantitative logarithmic cutoff removal.
The first version and the [conditional Schur variants](Yin_C_F0193_v2.md#statement) retain their exact mathematics and evidence.
The [independent complete Haar review](../audits/reviews/Yin_R_F0197_v2.md#independent-full-haar-proof) supports the complete statement and its exact source interfaces.
No novelty or priority conclusion is made.

<a id="statement"></a>
## Exact full Haar determinant statement

Fix integers \(m,r\ge1\) and arbitrary complex matrices \(A_0,\ldots,A_r\in M_m(\mathbb C)\), independent of \(N\).
For every \(N\), let \(U_1^{(N)},\ldots,U_r^{(N)}\) be independent matrices with probability Haar law on the full complex group \(U(N)\).
All dimensions live on one probability space with arbitrary cross-dimensional dependence.
Let \(u_1,\ldots,u_r\) be free Haar unitaries in a finite von Neumann algebra with faithful normal tracial state \(\tau\).
Set
\[
 L_N=A_0\otimes I_N+\sum_{j=1}^rA_j\otimes U_j^{(N)},
 \qquad L=A_0\otimes1+\sum_{j=1}^rA_j\otimes u_j,
 \qquad \tau_m=\operatorname{tr}_m\otimes\tau,
 \quad\operatorname{tr}_m=m^{-1}\operatorname{Tr}.
\]
Use the [ordinary Fuglede--Kadison determinant](../audits/literature/MS24/Yin_U001.md#determinant-convention), including all zero spectral mass, with \(\log0=-\infty\).
Then
\[
 U_N:=\frac1{mN}\log|\det L_N|
 \longrightarrow u:=\log\Delta_{\tau_m}(L)\in[-\infty,\infty)
 \quad\text{almost surely}.
 \tag{Full-Haar-limit}
\]
For \(u=-\infty\), convergence means eventual decrease below every fixed real threshold.
The constant coefficient may be singular or zero; no irreducibility, rank-one coefficient, regular-bulk or bounded-free-inverse hypothesis is imposed.
The probability-one event may depend on the fixed tuple and coupling.
In particular the full-limit and upper-limit assertions of F0015 hold for both arbitrary coupling and independent dimensions.

If \(u\) is finite, the proof also gives a polynomial least-singular-value floor outside summable failures.
More precisely, for every \(q>0\) there are fixed \(B,C,N_0\) such that
\[
 \mathbb P\{s_{\min}(L_N)<N^{-B}\}\le C N^{-q},\qquad N\ge N_0.
 \tag{Haar-floor}
\]
No convergence of the expectation of the unregularized logarithmic determinant is asserted.

## Exact mathematical inputs and source scope

The [fixed-dimensional polynomial-map error bound](Yin_C_F0186_v1.md#error-bound) supplies only its bounded-coordinate real algebraic distance inequality; the unitary constraints and lift are proved here.
The [uniform-ball algebraic tube bound](Yin_C_F0186_v1.md#tubes), including its proved regular-level extension for nonzero nonnegative polynomials, supplies only (T1)--(T2), not a Gaussian law for Haar inputs.
The [reviewed Haar generic-rank argument](Yin_C_F0192_v1.md#haar-generic-rank) supplies eventual nonidentity of the unitary determinant when the free kernel is zero.
The [retained Haar moment interface](../ledger/Yin_L_F0062_v1.md#haar-pencils) supplies almost-sure fixed-coefficient weak singular convergence under the actual coupling quantifier.
The [singular-value Frobenius inequality](Yin_C_F0186_v3.md#singular-value-perturbation) supplies the deterministic spectral-statistic Lipschitz step.

[Par22-U001](../audits/literature/Par22/Yin_U001.md#par22-u001) supplies Corollary 1.1 of arXiv:2005.13834v2 at arbitrary fixed matrix amplification, and Proposition 5.1 at its exact conditional special-unitary center.
[SS15-U001](../audits/literature/SS15/Yin_U001.md#ss15-u001) supplies Theorem 1.1(5)(6) of the actual retained arXiv:1305.1920v1 for selfadjoint matrix polynomials in free Haar unitaries, with zero atoms treated separately.
These external statements and applicability are accepted at their recorded source-inspection scopes; their foundational proofs have not been newly re-audited in full.
The earlier accepted polynomial-distance and tube-source proofs retain their recorded scope as well.
All new geometric, central-phase and logarithmic arguments are supplied below.

<a id="argument"></a>
## Complete Haar affine argument

<a id="unitary-repair"></a>
## Uniform unitary backward error

Fix auxiliary size \(m\), input count \(r\), and complex coefficients \(A_0,\ldots,A_r\in M_m(\mathbb C)\).
For \(U=(U_1,\ldots,U_r)\in U(N)^r\), put \(L_N(U)=A_0\otimes I_N+\sum_jA_j\otimes U_j\).
Let \(Z_N\) be the set of tuples at which \(L_N\) is singular, with the product Hilbert--Schmidt distance.
We prove that fixed \(C,\alpha,\varepsilon_0>0\), independent of \(N\), satisfy
\[
 s_{\min}(L_N(U))\le\varepsilon\le\varepsilon_0
 \quad\Longrightarrow\quad
 \operatorname{dist}_{\mathrm{HS}}(U,Z_N)\le C\varepsilon^\alpha.
 \tag{Unitary-repair}
\]
When Z_N is empty, this implication asserts that the displayed small-value event is empty.
This is an adaptation of the accepted fixed-coordinate [polynomial-map error bound](Yin_C_F0186_v1.md#error-bound), not an application of a Gaussian law to Haar matrices.
The real coordinate map is supplied explicitly below.

## Compression of the input and output frames

Take a unit complex vector v=(v_1,...,v_m) with ||L_N(U)v||<=epsilon.
Let W=span_C{v_1,...,v_m}, let k=dim W<=m, and choose an isometry X:C^k -> C^N with range W.
Write v_a=X w_a, so w=(w_1,...,w_m) has norm one.
Let K=W+sum_j U_j W and q=dim K, with k<=q<=min(N,(r+1)m).
Choose an isometry T:C^q -> C^N onto K, and define
\[
 F=T^*X,\qquad G_j=T^*U_jX.
\]
Every F,G_j is a q-by-k isometry, and
\[
 (A_0\otimes F)w+\sum_j(A_j\otimes G_j)w
\]
is exactly the residual in the orthonormal output coordinates T.
It has norm at most epsilon.
Only the two integers k,q vary, and there are finitely many possible types depending on fixed m,r.

Use real and imaginary coordinates of F,G_1,...,G_r,w.
Form the real polynomial map consisting of the real and imaginary residual coordinates, the Hermitian-coordinate equations F^*F-I_k=0 and G_j^*G_j-I_k=0, and ||w||^2-1=0.
It has degree at most two in 2(r+1)qk+2mk real variables.
The original coordinate vector lies in a fixed compact ball because all frame norms are sqrt(k) and ||w||=1.
Its map value has norm at most epsilon.
The coefficients and compact coordinate bound depend only on the original fixed pencil, m and r.
The accepted polynomial-map distance inequality gives exact zeros (F',G_j',w') within C epsilon^alpha for each nonempty-zero-set type, with a common alpha>0 for the finitely many types.
For a type with empty zero set, compactness gives a positive lower bound on the residual, excluding that type for small epsilon.
The corrected frames are isometries and ||w'||=1.
It remains to extend their corrected actions to nearby full unitaries.

<a id="frame-extension"></a>
## A quantitative extension of two nearby isometric frames

Let Y,Z:C^k -> C^N be isometries with delta=||Y-Z||_HS sufficiently small.
Put P=YY^*, Q=ZZ^*, and
\[
 B=ZY^*+(I-Q)(I-P).
\]
Then BY=Z and
\[
 B^*B=P+(I-P)(I-Q)(I-P).
\]
Since ||P-Q||<=2delta, B^*B is boundedly invertible for sufficiently small delta.
Its polar unitary R=B(B^*B)^(-1/2) satisfies RY=Z.
Indeed B^*B acts as the identity on ran P, and B maps its orthogonal complement into ran(I-Q).
Also
\[
 \|B-I\|_{\mathrm{HS}}
 \le\|(Z-Y)Y^*\|_{\mathrm{HS}}+\|Q(I-P)\|_{\mathrm{HS}}
 \le2\delta.
\]
Here ||Q(I-P)||_HS=||(I-P)Z||_HS<=||Z-Y||_HS.
The identity B^*B-I=B^*(B-I)+(B^*-I) gives ||B^*B-I||_HS<=C delta.
On its fixed spectral interval about one, the scalar function t^(-1/2) has bounded derivative.
Spectral calculus therefore gives ||(B^*B)^(-1/2)-I||_HS<=C delta, and hence
\[
 \|R-I\|_{\mathrm{HS}}\le C\delta.
\]
All constants are independent of N and k.
These estimates are direct bounded matrix calculations and apply also when the orthogonal complements have dimension zero.

## Lifting the polynomial correction

Put X'=TF', X_j'=TG_j'.
Both are full physical isometric frames with k columns.
The original equalities U_jX=TG_j and the polynomial correction imply
\[
 \|U_jX'-X_j'\|_{\mathrm{HS}}
 \le\|F'-F\|_{\mathrm{HS}}+\|G_j'-G_j\|_{\mathrm{HS}}
 \le C\varepsilon^\alpha.
\]
Apply the frame-extension calculation with Y=U_jX' and Z=X_j' to obtain a unitary R_j with R_jU_jX'=X_j' and ||R_j-I||_HS<=C epsilon^alpha.
Set U_j'=R_jU_j, so U_j' is unitary and ||U_j'-U_j||_HS has the same bound.
The vector \(v'=(X'w'_1,\ldots,X'w'_m)\) has norm one and is an exact kernel vector, because its residual is \(T\) applied to the corrected polynomial residual.
Thus U' belongs to Z_N and proves the backward error with the product extrinsic Hilbert--Schmidt distance.
If an intrinsic Riemannian distance is used instead, a unitary sufficiently close to identity has a principal logarithm with ||log R_j||_HS<=C||R_j-I||_HS.
The path exp(t log R_j)U_j has that length, giving the same distance estimate up to a fixed constant.


<a id="haar-tube-statement"></a>
## Quantitative intrinsic tube statement

Fix positive integers \(m,r,N\) and arbitrary complex matrices \(A_0,\ldots,A_r\in M_m(\mathbb C)\).
Write \(G_N=U(N)^r\), equipped with probability Haar measure \(\mu_N\), and define
\[
 L_N(U)=A_0\otimes I_N+\sum_{j=1}^rA_j\otimes U_j,
 \qquad F_N(U)=\det L_N(U),
 \qquad Z_N=\{U\in G_N:F_N(U)=0\}.
 \tag{H1}
\]
Suppose that \(F_N\) is not identically zero on \(G_N\).
Use the product Hilbert--Schmidt Riemannian metric with tangent norm
\[
 \|(X_1,\ldots,X_r)\|^2=\sum_{j=1}^r\operatorname{Tr}(X_j^*X_j),
 \tag{H2}
\]
without division by \(N\).
Put \(n=rN^2\) and \(D=2mrN\).
For \(0<\varepsilon\le1/4\), the following bound holds:
\[
 \begin{split}
 \mu_N\{U:\operatorname{dist}_{G_N}(U,Z_N)\le\varepsilon\}
 &\le4\sum_{k=1}^{n}\binom nk
       (4D\varepsilon)^k(1+2\varepsilon)^{n-k}\\
 &\le16nD\varepsilon\,
       \exp\bigl(2n(2D+1)\varepsilon\bigr).
 \end{split}
 \tag{H3}
\]
An empty \(Z_N\) has tube probability zero.
In particular, for fixed \(m,r\), there are constants \(c,C>0\), independent of \(N\) and of the numerical coefficient values, such that
\[
 \mu_N\{\operatorname{dist}_{G_N}(U,Z_N)\le\varepsilon\}
 \le C N^3\varepsilon,
 \qquad 0<\varepsilon\le cN^{-3}.
 \tag{H4}
\]
The bound is coefficient-uniform subject only to the stated nonidentity hypothesis.
If the metric is instead divided by \(\sqrt N\), its radius \(\varepsilon\) corresponds to the radius \(\sqrt N\varepsilon\) in (H3), giving \(CN^{7/2}\varepsilon\) in the corresponding small-radius regime.
The same proof gives (H3) for the product ambient chordal Hilbert--Schmidt distance, which is at most the Riemannian distance.

<a id="haar-tube-argument"></a>
## Complete tube argument

The only geometric source input is the [accepted uniform-ball algebraic tube bound (T1)--(T2), including its nonzero nonnegative-polynomial regular-level extension](Yin_C_F0186_v1.md#tubes).
Its underlying primary result is Lotz, arXiv:1210.3742v4, Theorem 1.1, p. 1, as recorded in the [retained edition note](../audits/literature/Lot15/readme.md).
In particular, if \(q\) is a nonzero nonnegative real polynomial of degree at most \(D\) in \(n\) real variables and \(H\) is uniform in the Euclidean unit ball, that accepted input gives
\[
 \mathbb P\{\operatorname{dist}(H,q^{-1}(0))\le\rho\}
 \le4\sum_{k=1}^{n}\binom nk(2D\rho)^k(1+\rho)^{n-k}
 \le8nD\rho\exp\bigl(n(2D+1)\rho\bigr).
 \tag{H5}
\]
The empty-zero-set case is immediate.
The regular-level extension is needed because a squared complex determinant can have a singular zero set or a real zero set of codimension larger than one.
No smoothness or complete-intersection hypothesis on the original determinant zero set is introduced here.

Choose a real Hilbert--Schmidt orthonormal basis of \(\operatorname{Herm}_N^r\), identifying it isometrically with \(\mathbb R^n\).
Let \(H=(H_1,\ldots,H_r)\) be uniform in its closed unit ball, and independently let \(W=(W_1,\ldots,W_r)\) have product Haar law on \(G_N\).
For Hermitian \(H_j\), set
\[
 C(H_j)=(I_N+iH_j)(I_N-iH_j)^{-1},
 \qquad U_j=W_jC(H_j).
 \tag{H6}
\]
Conditional on every fixed value of \(H\), multiplication by \((C(H_1),\ldots,C(H_r))\) preserves product Haar measure.
Consequently \(U\) has exactly the desired product Haar law after averaging over \((W,H)\).
This observation uses no comparison between Haar density in a Cayley chart and Euclidean density.

Fix \(W\) for the remainder of the local calculation.
For a unitary matrix \(X\) with \(-1\) outside its spectrum, the inverse Cayley map is
\[
 C^{-1}(X)=-i(X-I_N)(X+I_N)^{-1}.
 \tag{H7}
\]
Because \(\|H_j\|\le\|H_j\|_{\mathrm{HS}}\le1\), the matrices \(X_j=C(H_j)\) satisfy
\[
 s_{\min}(I_N+X_j)
 =s_{\min}\bigl(2(I_N-iH_j)^{-1}\bigr)\ge\sqrt2.
 \tag{H8}
\]
Suppose that \(U\) is at Riemannian distance at most \(\varepsilon\le1/4\) from \(Z_N\), and choose \(V\in Z_N\) attaining that distance.
Compactness supplies this choice when \(Z_N\) is nonempty.
The chordal Hilbert--Schmidt distance is at most the Riemannian distance, so
\[
 \sum_{j=1}^r\|W_j^*V_j-X_j\|_{\mathrm{HS}}^2
 =\sum_{j=1}^r\|V_j-U_j\|_{\mathrm{HS}}^2\le\varepsilon^2.
 \tag{H9}
\]
In particular, \(s_{\min}(I_N+W_j^*V_j)\ge\sqrt2-\varepsilon>1\), and therefore each \(H_j'=C^{-1}(W_j^*V_j)\) exists and is Hermitian.
The resolvent identity in (H7) gives, for \(Y_j=W_j^*V_j\),
\[
 \begin{split}
 \|H_j'-H_j\|_{\mathrm{HS}}
 &=2\|(Y_j+I_N)^{-1}(X_j-Y_j)(X_j+I_N)^{-1}\|_{\mathrm{HS}}\\
 &\le\frac{2}{\sqrt2(\sqrt2-\varepsilon)}
       \|Y_j-X_j\|_{\mathrm{HS}}
 \le2\|Y_j-X_j\|_{\mathrm{HS}}.
 \end{split}
 \tag{H10}
\]
The equality is an equality of norms, so the harmless scalar factor of modulus one from (H7) has been omitted.
Summing squares yields \(\|H'-H\|_{\mathrm{HS}}\le2\varepsilon\).
The same calculation starts directly from a chordal distance bound, establishing the chordal variant stated above.

To express the repaired zero set as a degree-controlled real algebraic set, put \(M=mN\), \(R_j(H)=I_m\otimes(I_N-iH_j)\), and
\[
 B_W=A_0\otimes I_N-\sum_{j=1}^rA_j\otimes W_j.
\]
Consider the \((r+1)M\)-dimensional affine block pencil
\[
 K_W(H)=
 \begin{pmatrix}
 B_W&2A_1\otimes W_1&2A_2\otimes W_2&\cdots&2A_r\otimes W_r\\
 -I_M&R_1(H)&0&\cdots&0\\
 -I_M&0&R_2(H)&\cdots&0\\
 \vdots&\vdots&\vdots&\ddots&\vdots\\
 -I_M&0&0&\cdots&R_r(H)
 \end{pmatrix}.
 \tag{H11}
\]
Every \(R_j(H)\) is invertible for real Hermitian coordinates.
Taking their Schur complement and using \(C(H_j)=2(I_N-iH_j)^{-1}-I_N\) gives the exact identity
\[
 \det K_W(H)
 =\left(\prod_{j=1}^r\det(I_N-iH_j)^m\right)
       F_N\bigl(W_1C(H_1),\ldots,W_rC(H_r)\bigr).
 \tag{H12}
\]
Thus the zero set of \(q_W(H):=|\det K_W(H)|^2\) on the entire Hermitian coordinate space is precisely the Cayley preimage of \(Z_N\) in this chart.
The determinant \(\det K_W\) has total degree at most \(rM\), since the first \(M\) rows of (H11) are constant and every remaining row is affine in the real coordinates.
Consequently \(q_W\) is a nonnegative real polynomial of degree at most \(2rM=D\).
It is nonzero for every \(W\).
Indeed the image of the full Cayley chart is the dense open subset of \(G_N\) where each \(I_N+W_j^*U_j\) is invertible.
A continuous nonzero \(F_N\) has a nonempty open nonzero locus, which meets this dense chart, and the denominator in (H12) never vanishes on real Hermitian coordinates.

The repaired tuple \(H'\) above belongs to \(q_W^{-1}(0)\) by (H12).
We have therefore proved, for every fixed \(W\), the deterministic inclusion
\[
 \{H\in\overline B_1:
   \operatorname{dist}_{G_N}(WC(H),Z_N)\le\varepsilon\}
 \subseteq
 \{H\in\overline B_1:
   \operatorname{dist}_{\mathbb R^n}(H,q_W^{-1}(0))\le2\varepsilon\}.
 \tag{H13}
\]
The Euclidean tube permits its nearest zero outside the sampling ball, so no boundary error is needed.
Apply (H5) to the right side with \(\rho=2\varepsilon\), condition on \(W\), and then average over \(W\).
The exact Haar marginal in (H6) gives (H3).
Since \(nD=2mr^2N^3\) and \(n(2D+1)=O_{m,r}(N^3)\), taking \(\varepsilon\le cN^{-3}\) gives (H4).
This completes the tube argument.


<a id="quantitative-resolvent"></a>
## Exact Hermitization comparison

Put \(H_N=\begin{pmatrix}0&L_N\\L_N^*&0\end{pmatrix}\) and \(H=\begin{pmatrix}0&L\\L^*&0\end{pmatrix}\), with traces normalized by \(2mN\) and \(\operatorname{tr}_{2m}\otimes\tau\), respectively.
Write \(\mathcal H_N=H_N\) and \(\mathcal H_\infty=H\) in the calculations below.
The [exact Par22 Hermitization specialization](../audits/literature/Par22/Yin_U001.md#haar-hermitization-match) encodes the fixed coefficient matrices as deterministic variables in auxiliary dimension 2m.
Those variables need not commute with one another.
It yields
\[
 |\mathbb EG_{H_N}(it)-G_H(it)|
 \le C N^{-2}\log^2N(t^{-5}+t^{-2}),\qquad0<t\le1,\quad N\ge2.
\]
Here \(G(z)\) is the normalized trace of \((z-H)^{-1}\), with negative imaginary part in the upper half-plane.
No singular constant term or degenerate coefficient space is excluded by this input.
Write \(\nu_N\) for the normalized singular-value law of \(L_N\) and \(\nu\) for that of \(L\).
The branch \(u=-\infty\) is treated after the finite branch and requires no floor.

<a id="haar-concentration"></a>
## From the source's conditional center to the full Haar mean

Use the product unnormalized chordal Hilbert--Schmidt metric on \(G_N=U(N)^r\), and let \(f:G_N\to\mathbb C\) be \(L\)-Lipschitz.
For \(W_j\) independently Haar on \(SU(N)\), write
\[
 g(U)=\mathbb E_W f(W_1U_1,\ldots,W_rU_r).
\]
For any fixed \(U,V\), choose \(\theta_j,\phi_j\in[0,2\pi)\) with \(e^{i\theta_j}=\det U_j\), \(e^{i\phi_j}=\det V_j\), and factor
\[
 U_j=e^{i\theta_j/N}S_j,
 \qquad V_j=e^{i\phi_j/N}T_j,
 \qquad S_j,T_j\in SU(N).
\]
Right invariance on \(SU(N)\) gives
\[
 g(U)=\mathbb E_W f(e^{i\theta_1/N}W_1,\ldots,e^{i\theta_r/N}W_r),
\]
with the analogous representation for \(g(V)\) using the same random \(W\).
For each \(j\),
\[
 \|(e^{i\theta_j/N}-e^{i\phi_j/N})W_j\|_{\mathrm{HS}}
 \le\frac{|\theta_j-\phi_j|}{\sqrt N}\le\frac{2\pi}{\sqrt N}.
\]
Consequently
\[
 |g(U)-g(V)|\le d_N,
 \qquad d_N:=2\pi L\sqrt{r/N}.
 \tag{H16}
\]
If \(V\) is product Haar on \(U(N)^r\), then \(\mathbb E_Vg(V)=\mathbb Ef(V)\), by invariance under each fixed left multiplier \(W\).
Averaging (H16) over \(V\) therefore gives the pointwise bound \(|g(U)-\mathbb Ef(U)|\le d_N\).
Combining this with the exact source Proposition 5.1 yields, for \(\delta>0\),
\[
 \mathbb P\{|f(U)-\mathbb Ef(U)|\ge d_N+\delta\}
 \le4r\exp\left(-\frac{N\delta^2}{4r^2L^2}\right).
 \tag{H17}
\]
This proof uses the actual conditional center and does not apply special-unitary curvature to the missing central direction.
It requires only the within-dimension product Haar law.

For a real \(L_h\)-Lipschitz function \(h:[0,\infty)\to\mathbb R\), put
\[
 \Phi_{N,h}(U)=\frac1{mN}\sum_{k=1}^{mN}h(s_k(L_N(U))),
 \qquad \kappa_A^2=\sum_j\|A_j\|_{\mathrm{HS}}^2.
\]
The tensor Hilbert--Schmidt inequality gives
\[
 \|L_N(U)-L_N(V)\|_{\mathrm{HS}}
 \le\kappa_A\left(\sum_j\|U_j-V_j\|_{\mathrm{HS}}^2\right)^{1/2}.
\]
The [accepted singular-value Frobenius inequality](Yin_C_F0186_v3.md#singular-value-perturbation) and Cauchy--Schwarz thus give
\[
 \operatorname{Lip}(\Phi_{N,h})\le\frac{\kappa_A L_h}{\sqrt{mN}}.
 \tag{H18}
\]
For \(\kappa_A>0\), substituting (H18) into (H17) yields fixed constants \(C_A,c_A>0\), depending only on the pencil, \(m,r\), such that
\[
 \mathbb P\{|\Phi_{N,h}-\mathbb E\Phi_{N,h}|
              \ge C_A L_h/N+\delta\}
 \le4r\exp\left(-c_A\frac{N^2\delta^2}{L_h^2}\right).
 \tag{H19}
\]
If \(\kappa_A=0\), the statistic is deterministic and no concentration argument is necessary.
The deterministic \(O(L_h/N)\) shift is retained rather than silently removed.

<a id="haar-mesoscopic-mass"></a>
## Mesoscopic count matching without a bulk hypothesis

Suppose that the free square pencil \(L_\infty=A_0\otimes1+\sum_jA_j\otimes u_j\) has finite ordinary normalized logarithmic determinant.
Its symmetric Hermitization law then has no atom at zero.
The [accepted SS15 matrix-polynomial algebraicity and Puiseux input](../audits/literature/SS15/Yin_U001.md#matrix-algebraicity-and-puiseux), with this zero atom excluded separately, gives some fixed \(\beta,C>0\) with
\[
 c_\infty(t):=t|\operatorname{Im}G_{\mathcal H_\infty}(it)|\le Ct^\beta,
 \qquad 0<t\le1.
\]
One may decrease \(\beta\) if needed.
The resolvent bound \(|G(it)|\le1/t\) excludes Puiseux powers below \(-1\).
Since \(itG(it)\) tends to the zero-atom mass, absence of that atom excludes a nonzero coefficient of power \(-1\).
The remaining rational powers have exponent strictly larger than \(-1\), proving the displayed positive power.
One may take \(0<\beta\le1\).
For
\[
 c_t(s)=\frac{t^2}{s^2+t^2},
\]
Hermitization gives the exact identity
\[
 \Phi_{N,c_t}=-t\operatorname{Im}G_{\mathcal H_N}(it).
\]
The Par22 comparison therefore gives
\[
 \mathbb E\Phi_{N,c_t}
 \le C\left(t^\beta+N^{-2}\log^2N\,t^{-4}\right),
 \qquad 0<t\le1,
 \tag{H20}
\]
since the additional comparison term \(N^{-2}\log^2N\,t^{-1}\) is smaller on this interval.
Because \(\nu_N([0,t])\le2\Phi_{N,c_t}\), this also bounds the expected singular-value mass at zero.
Choose
\[
 0<\gamma<\min\left\{\frac{2}{4+\beta},\frac1{1+\beta}\right\},
 \qquad t_N=N^{-\gamma}.
 \tag{H21}
\]
The same strict first inequality gives \(\mathbb E\nu_N([0,t])\le Ct^\beta\) uniformly for \(t_N\le t\le1\), because the ratio of its comparison term to \(t^\beta\) is maximal at \(t=t_N\).
It absorbs the logarithmic factor in (H20), giving \(\mathbb E\Phi_{N,c_{t_N}}\le C t_N^\beta\) for all sufficiently large \(N\).
Since \(\operatorname{Lip}(c_t)\le2/t\), the shift in (H19) is \(O(N^{\gamma-1})=o(t_N^\beta)\) by the strict second inequality in (H21).
Taking \(\delta=t_N^\beta\), the exceptional probabilities are bounded by
\[
 4r\exp\bigl(-cN^{2-2\gamma(1+\beta)}\bigr),
\]
which are summable.
First Borel--Cantelli gives
\[
 \nu_N([0,t_N])\le C't_N^\beta
 \quad\text{eventually almost surely under every cross-dimensional coupling}.
 \tag{H22}
\]
The clipped logarithm \(h_N(s)=\log\max(s,t_N)\) also has Lipschitz constant at most \(N^\gamma\).
For any \(0<\zeta<1-\gamma\), (H19) with \(\delta=N^{-\zeta}\) has vanishing deterministic shift and summable exceptional probabilities, proving convergence of that statistic to its expectation at the moving cutoff.

<a id="clipped-logarithm"></a>
## Removing the clipping and treating zero free determinant



For finite u, the free kernel is zero.
The [reviewed generic-rank argument](Yin_C_F0192_v1.md#haar-generic-rank) gives eventual nonidentity of the finite determinant on the full unitary tuple space.
Compose (Unitary-repair) with the proved bound (H4) at radius C epsilon^alpha.
For sufficiently small epsilon with N^3 epsilon^alpha bounded, the resulting failure probability is at most C'N^3 epsilon^alpha.
Choosing B with B alpha>4, and increasing B so B>gamma, gives
\[
 \sum_N\mathbb P\{s_{\min}(L_N)<N^{-B}\}<\infty.
\]
Hence the polynomial floor holds eventually almost surely under every coupling.
For the probability assertion (Haar-floor) at any prescribed \(q>0\), take \(B\alpha>q+3\) in the same bound \(CN^3\varepsilon^\alpha\).
Increasing \(B\) preserves this assertion and the summable floor just obtained.

Put V_N(t)=(mN)^(-1)sum_k log max(s_k(L_N),t).
Its scalar test has Lipschitz constant 1/t.
At t=t_N, the concentration tail at each fixed positive deviation is summable and the expectation-center shift tends to zero.
A countable intersection gives V_N(t_N)-E V_N(t_N)->0 almost surely.
All L_N satisfy the deterministic norm bound ||L_N||<=||A_0||+sum_j||A_j||.
The accepted Haar moment convergence therefore implies, for every fixed epsilon>0,
\[
 \mathbb EV_N(\varepsilon)\longrightarrow
 v(\varepsilon)=\int\log\max(s,\varepsilon)\,d\nu(s),
\]
where nu is the law of |L|.
No positive logarithmic tail estimate is needed beyond this deterministic norm bound.
Layer integration and the uniform expected-mass bound following (H21) give
\[
 0\le\mathbb E[V_N(\varepsilon)-V_N(t_N)]
 =\int_{t_N}^{\varepsilon}\mathbb E\nu_N([0,t))\,dt/t
 \le C\varepsilon^\beta.
\]
Since v(epsilon) decreases to finite u, the clipped means converge to u and V_N(t_N)->u almost surely.
On the eventual polynomial floor,
\[
 0\le V_N(t_N)-U_N
 \le B\log N\,\nu_N([0,t_N])\longrightarrow0.
\]
This proves the full limit at a finite free value.

For u=-infinity, fix a decreasing sequence epsilon_k->0.
The accepted almost-sure Haar weak convergence and deterministic norm bound give V_N(epsilon_k)->v(epsilon_k) almost surely for every k.
Since U_N<=V_N(epsilon_k) and v(epsilon_k) decreases to -infinity, U_N->-infinity through every dimension.
This branch needs neither nonidentity nor a floor.
All normalizations above are by mN for L_N and by 2mN for H_N, so no auxiliary power or determinant root has been lost.


## Current assessment
[Selected decision](#decision-full-haar-reviewed)

## Assessment history

### Decision full-haar-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:25 |
| status | open |
| reason | The full arbitrary-coefficient Haar determinant argument is fixed for independent review, including unitary repair, coefficient-uniform Cayley tubes, quantitative comparison, the true concentration center and logarithmic cutoff removal. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete Haar assertion](#statement) | Full extended-real ordinary logarithmic limit for every fixed coefficient tuple and every coupling, with the stated finite-target probability floor. |
| argument | [Complete affine Haar proof](#argument) | Fixed-dimensional unitary repair, exact centered Cayley tube, generic nonidentity, resolvent and Puiseux count, conditional-center correction, summable floors, clipping and the zero-target case. |
| dependency | [Polynomial-map error bound](Yin_C_F0186_v1.md#error-bound) | Only the accepted bounded-coordinate real polynomial-map distance inequality; the new isometric constraints and unitary lift are proved here. |
| dependency | [Uniform-ball algebraic tubes](Yin_C_F0186_v1.md#tubes) | Only (T1)--(T2) and the nonzero nonnegative-polynomial regular-level extension; no Gaussian distribution is substituted for Haar measure. |
| dependency | [Eventual Haar nonidentity](Yin_C_F0192_v1.md#haar-generic-rank) | Accepted zero-free-kernel implication for every sufficiently large full-unitary input dimension. |
| dependency | [Haar weak convergence](../ledger/Yin_L_F0062_v1.md#haar-pencils) | Almost-sure fixed-coefficient moment and continuous spectral-test convergence under every allowed cross-dimensional coupling, with the deterministic coefficient norm bound. |
| dependency | [Singular-value Frobenius inequality](Yin_C_F0186_v3.md#singular-value-perturbation) | Only the deterministic squared singular-value perturbation inequality used for the normalized statistic's global Lipschitz constant. |
| dependency | [Quantitative Haar source](../audits/literature/Par22/Yin_U001.md#par22-u001) | Exact arXiv v2 Corollary 1.1 with fixed noncommuting matrix coefficients and Proposition 5.1 at its actual conditional SU center. |
| dependency | [Free Haar algebraicity](../audits/literature/SS15/Yin_U001.md#ss15-u001) | Theorem 1.1(5)(6) at the inspected Haar selfadjoint matrix-polynomial scope; a zero atom is separately excluded by finite ordinary free logarithm. |

### Decision full-haar-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:34 |
| status | proved |
| reason | Independent whole-proof review checked the complete arbitrary-coefficient Haar determinant limit and every declared input, including the geometric tube and repair, exact quantitative sources, concentration center, all coupling quantifiers and zero free determinant, without an unresolved mathematical gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete Haar assertion](#statement) | Full extended-real ordinary logarithmic limit for every fixed coefficient tuple and every coupling, with the stated finite-target probability floor. |
| argument | [Complete affine Haar proof](#argument) | Fixed-dimensional unitary repair, exact centered Cayley tube, generic nonidentity, resolvent and Puiseux count, conditional-center correction, summable floors, clipping and the zero-target case. |
| dependency | [Polynomial-map error bound](Yin_C_F0186_v1.md#error-bound) | Only the accepted bounded-coordinate real polynomial-map distance inequality; the new isometric constraints and unitary lift are proved here. |
| dependency | [Uniform-ball algebraic tubes](Yin_C_F0186_v1.md#tubes) | Only (T1)--(T2) and the nonzero nonnegative-polynomial regular-level extension; no Gaussian distribution is substituted for Haar measure. |
| dependency | [Eventual Haar nonidentity](Yin_C_F0192_v1.md#haar-generic-rank) | Accepted zero-free-kernel implication for every sufficiently large full-unitary input dimension. |
| dependency | [Haar weak convergence](../ledger/Yin_L_F0062_v1.md#haar-pencils) | Almost-sure fixed-coefficient moment and continuous spectral-test convergence under every allowed cross-dimensional coupling, with the deterministic coefficient norm bound. |
| dependency | [Singular-value Frobenius inequality](Yin_C_F0186_v3.md#singular-value-perturbation) | Only the deterministic squared singular-value perturbation inequality used for the normalized statistic's global Lipschitz constant. |
| dependency | [Quantitative Haar source](../audits/literature/Par22/Yin_U001.md#par22-u001) | Exact arXiv v2 Corollary 1.1 with fixed noncommuting matrix coefficients and Proposition 5.1 at its actual conditional SU center. |
| dependency | [Free Haar algebraicity](../audits/literature/SS15/Yin_U001.md#ss15-u001) | Theorem 1.1(5)(6) at the inspected Haar selfadjoint matrix-polynomial scope; a zero atom is separately excluded by finite ordinary free logarithm. |
| review | [Independent full Haar finding](../audits/reviews/Yin_R_F0197_v2.md#independent-full-haar-proof) | Complete exact statement, argument, every direct dependency and original F0015 four-part scope, including all coefficient and zero-target cases. |

