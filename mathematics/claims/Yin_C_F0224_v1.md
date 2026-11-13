---
author: Yin
---
# Dual costs for radial univalent changes of a circular generator

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(c\) be a standard circular generator in its faithful normalized tracial representation, \(M=W^*(c)\), \(H=L^2(M,\tau)\), \(B=C^*(1,c)\), and \(\Omega=1\).
Write \(L_x\) for left multiplication and \(P_\Omega h=\langle\Omega,h\rangle\Omega\), with inner products linear in the second variable.
For \(X\) generating \(M\), let \(\beta(X)\) be the infimum of \(\|E:M\to H\|\) over bounded linear maps satisfying \(E(Xa)-XE(a)=P_\Omega a\) for every \(a\in M\), where \(M\) carries the operator norm.
Let \(\beta_H(X)\) be the corresponding infimum over bounded \(E:H\to H\) satisfying the commutator on \(H\).
No value of \(E\Omega\) is prescribed.

Suppose \(f\) is holomorphic and injective on the open unit disk, \(f(0)=0\) and \(f'(0)=1\).
For \(0<t<1\) put \(f_t(z)=f(tz)/t\), \(Z_t=f_t(c)\), and put
\[
 g(z,w)=\frac{z-w}{f(z)-f(w)}=\sum_{m,n\ge0}g_{mn}z^m w^n,\qquad A_f=(g_{mn})_{m,n\ge0}.
\]
The diagonal is filled by \(1/f'(z)\).
Define isometries \(J_+,J_-:\ell^2(\mathbb N_0)\to H\) by \(J_+e_m=c^m\Omega,\ J_-e_m=(c^*)^m\Omega\).

1. The coefficient matrix satisfies \(\|A_f\|_{\ell^2\to\ell^2}\le16\), with equality for the Koebe function \(f(z)=z/(1-z)^2\).
   Set \(K_f=J_+A_fJ_-^*\).
   On each radial law every bounded \(M\to H\) dual \(E\) satisfies \([E,L_c]a=K_{f_t}a\) for \(a\in M\), and \(K_{f_t}\to K_f\) strongly on \(H\).
2. Let \(b_f\) be the infimum of the norms of bounded \(D:B\to H\) satisfying \([D,L_c]a=K_fa\) on \(\mathbb C\langle c,c^*\rangle\), with empty infimum \(+\infty\).
   Then \(\beta(Z_t)\uparrow b_f\) as \(t\uparrow1\).
   At every \(t<1\) above, \(C^*(1,Z_t)=B\), a bounded Hilbert-space dual exists, and \(c\) is an actual ACSY vacuum attaining the least possible norm \(1\).
   The endpoint \(b_f\) is defined without evaluating \(f(c)\).
3. For the Koebe function, \(\beta_H(Z_t)\asymp(1-t)^{-1/2}\) as \(t\uparrow1\).
   With \(r_u,r_v\) the two right Fock creation operators in the circular model \(c=\ell(u)+\ell(v)^*\), an explicit Hilbert dual is
   \[
    B_t=(I-tL_c)^2\left(\sum_{n\ge0}t^{2n}r_u^n r_u^*(r_v^*)^n\right)(I-tL_c)^2 .
   \]
4. For each analytic polynomial \(p=\sum_k p_k z^k\) define the bounded operator on \(H\)
   \[
    K_{p,t}=\sum_{k\ge1}p_k\sum_{j=0}^{k-1} L_c^j K_{f_t} L_c^{\,k-1-j}
   \]
   for \(0<t\le1\), where \(f_1=f\).
   For Koebe and an absolute \(C\),
   \[
    \|K_{p,t}a\|_2\le C\|p(c)\|_\infty\|a\|_\infty\qquad(a\in M,\ 0<t\le1).
   \]
   For \(t<1\), this operator restricts to \([E,L_{p(c)}]\) for every bounded \(M\to H\) dual of \(Z_t\).
   At \(t=1\) the kernel for \(p(z)=z^k\) has Hilbert operator norm exactly \(16k\) for \(k\ge1\).

These assertions leave the boundedness of \(\beta(Z_t)\) for the Koebe family and the arbitrary-tuple full-domain implication open.

## Argument

### External inputs

<a id="exterior-grunsky-input"></a>

The exterior Grunsky inequality applies to an injective holomorphic \(F(\zeta)=\zeta+a_0+O(1/\zeta)\) on \(|\zeta|>1\).
If the logarithm of \((F(\zeta)-F(\eta))/(\zeta-\eta)\), normalized to vanish at infinity, is \(-\sum_{m,n\ge1}b_{mn}\zeta^{-m}\eta^{-n}\), then \((\sqrt{mn}\,b_{mn})\) acts contractively on \(\ell^2(\mathbb N)\). [S. L. Krushkal, *Quasiconformal Reflections across Polygonal Lines*, §1.3, (6)–(8) and the matrix statement after (10)](https://www.intechopen.com/chapters/72257)

<a id="disk-growth-input"></a>

For the stated normalization on the disk, Koebe's growth theorem gives \(|f(z)|\ge |z|/(1+|z|)^2\). [D. Belyaev, *Conformal Maps and Geometry*, Theorem 3.2.11, pp. 42–43](https://people.maths.ox.ac.uk/belyaev/TCC/lecture_notes.pdf)

<a id="shifted-circular-input"></a>

For a unit-variance circular \(c\) and real \(\lambda>1\), the \(R\)-transform of \(X=(\lambda-c)(\lambda-c)^*\) is \(R_X(z)=(1-z)^{-1}+\lambda^2(1-z)^{-2}\), and \(1/z+R_X(z)\) is the local inverse of its Cauchy transform at infinity. [Haagerup, Kemp and Speicher, *Resolvents of R-diagonal operators*, arXiv:0811.3125v1, (1.3), Theorem 2.2 and (2.11)](https://arxiv.org/pdf/0811.3125v1)

### The Grunsky contraction and the first forced commutator

Take \(F(\zeta)=1/f(1/\zeta)\) in the exterior inequality and write \(T=(\sqrt{mn}\,b_{mn})\).
Injectivity and normalization of \(f\) give precisely the required exterior expansion and univalence.
Put \(v(z)=(z^n/\sqrt n)_{n\ge1}\) and take exponential vectors \(\mathcal E(x)=\bigoplus_{j\ge0}x^{\otimes j}/\sqrt{j!}\) in the symmetric Fock space over \(\ell^2(\mathbb N)\).
Their Gram kernel at \(v(z),v(w)\) is
\[
 \langle\mathcal E(v(z)),\mathcal E(v(w))\rangle
 =\exp\left(\sum_{n\ge1}(\bar z w)^n/n\right)=(1-\bar z w)^{-1}.
\]
This is the Gram kernel of \(e(z)=(1,z,z^2,\ldots)\), whose span is dense in \(\ell^2(\mathbb N_0)\) by uniqueness of Taylor coefficients.
Thus \(e(z)\mapsto\mathcal E(v(z))\) defines an isometry \(V\) on the whole coefficient space.
The contraction \(\Gamma(T)=\bigoplus_{j\ge0}T^{\otimes j}|_{\mathrm{Sym}^j}\) takes \(\mathcal E(v(w))\) to \(\mathcal E(Tv(w))\).
The coefficient generating function of \(V^*\Gamma(T)V\), obtained by testing on \(e(\bar z),e(w)\), is therefore \(\exp(\sum b_{mn}z^mw^n)\).
Algebra in the exterior logarithm gives
\[
 g(z,w)=d(z)d(w)\exp\left(\sum_{m,n\ge1} b_{mn}z^mw^n\right),\qquad d(z)=z/f(z).
\]
The growth theorem gives \(\|d\|_{H^\infty}\le4\).
In Taylor coordinates \(A_f=M_d V^*\Gamma(T)V M_d^{\mathsf T}\), where \(M_d\) is Hardy multiplication and the transpose is in the Taylor basis.
Both outer factors have norm at most four, proving the bound.

Since \(f_t\) is injective on \(|z|<1/t\), for \(1<r<1/t\) the compact image \(f_t(\{|z|\le r\})\) is a filled Jordan domain and the inverse is holomorphic on a neighborhood of that compact set.
The [polynomial Runge theorem](../audits/literature/GW25/Yin_U001.md#gw25-u001) supplies the inverse approximation required by the [fixed univalent circular change theorem](Yin_C_F0218_v1.md#statement).
Its conclusions give the algebra equality by norm approximation in both directions, Hilbert dual existence, and the attained vacuum \(c\), since \(f_t'(0)=1\).
In its circular Fock representation, \(c^m\Omega=u^m,\ (c^*)^n\Omega=v^n\), which gives the stated isometries and \((J_-^*a)_n=\tau(c^na)\) on \(M\).
The inverse divided difference of \(f_t\) is \(g(tz,tw)\), so the same theorem gives \([E,L_c]=K_{f_t}\) on \(M\).
If \(W_t e_n=t^n e_n\), then \(A_{f_t}=W_t A_f W_t\).
Since \(W_t\to I\) strongly and \(\|W_t\|\le1\), the assertion of strong kernel convergence follows.

### Monotonicity and the radial endpoint

An admissible \(D:B\to H\) at the endpoint satisfies its commutator on all of \(B\) by norm density and the boundedness of \(K_f\).
Let \(\alpha_\theta(c)=e^{i\theta}c\) be the trace-preserving rotation and \(U_\theta\) its induced unitary on \(H\).
The rotation is pointwise norm continuous on \(B\) by star-polynomial density and strongly continuous on \(H\).
Set \(D_\theta(a)=e^{i\theta}U_\theta D(\alpha_{-\theta}a)\).
The leading scalar phase cancels the phase of \(c\) in \([D_\theta,L_c]\).
On a core polynomial the induced commutator has coefficients \(e^{i(m+n)\theta}g_{mn}\), since the input trace acquires \(e^{in\theta}\) and the output \(c^m\Omega\) acquires \(e^{im\theta}\).
Integration against the probability Poisson kernel at radius \(t\) gives a linear map \(D^{(t)}:B\to H\) of norm at most \(\|D\|\).
Its commutator with \(c\) equals \(K_{f_t}\) by the Fourier coefficient identity, first on polynomial inputs and individual output coordinates and then by norm density.
The input involves only finitely many columns there because \(\tau(c^na)=0\) for \(n\) exceeding the degree of \(a\), by rotation invariance.

The commutator of \(D^{(t)}\) with \(Z_t\) on \(B\) is \(P_\Omega\).
Indeed, by the product rule, summing the commutators for powers of \(c\) multiplies the kernel \(g(tz,tw)\) by the divided difference of \(f_t\), giving the constant 1.
The coefficient series and their divided differences converge absolutely on a bidisk of radius greater than one, and \(\|c^n\|_\infty\le n+1\) follows from the circular Fock expansion.
These bounds justify all operator products and sums as in the [univalent change proof](Yin_C_F0218_v1.md#convergent-power-series-and-simultaneous-commutators).
The [central-summand transfer](Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) applied to \(B=C^*(1,Z_t)\) now gives a witness on \(M\) with the same upper norm bound.
Starting instead from an \(M\to H\) witness at radius \(t\), restriction to \(B\) and the identical averaging with radius \(s/t\) gives \(\beta(Z_s)\le\beta(Z_t)\) for \(0<s<t<1\).
It follows that \(\sup_{t<1}\beta(Z_t)\le b_f\).

If the supremum is \(C<\infty\), choose near-minimizers at \(t_j\uparrow1\) with norms at most \(C+1/j\).
After restriction to \(B\), product weak compactness of the Hilbert balls for all individual inputs gives a subnet converging pointwise weakly to a linear \(D\) of norm at most \(C\).
Left multiplication is weakly continuous on \(H\), and \(K_{f_{t_j}}\to K_f\) strongly, so the commutators give \([D,L_c]=K_f\) on \(B\).
This proves the reverse inequality and the extended-real identity.

### Koebe powers and the Hilbert lower bound

For Koebe,
\[
 g(tz,tw)=\frac{(1-tz)^2(1-tw)^2}{1-t^2zw},\qquad
 A_{f_t}=P_tD_tP_t^*,\quad P_t=(I-tS)^2,\quad D_te_n=t^{2n}e_n
\]
with \(S\) the unilateral shift, also allowing \(t=1\).
The limiting matrix is \((I-S)^2(I-S^*)^2\) and has norm 16 since Hardy multiplication by \((1-z)^2\) has norm 4.
The moment formula gives \(L_cJ_+=J_+S\) and \(J_-^*L_c=S^*J_-^*\).
Thus
\[
 K_{z^k,t}=J_+P_t M_{k,t}P_t^*J_-^*,\qquad
 M_{k,t}=\sum_{j=0}^{k-1}S^jD_t(S^*)^{k-1-j}.
\]
The product rule proves the claimed commutator identity on \(M\), and on all of \(H\) for a Hilbert-bounded witness by density.
At \(t=1\) this operator has norm at most \(16k\) by the triangle inequality.
The unit vectors \(x_N=N^{-1/2}\sum_{q=0}^{N-1}(-1)^qe_q\) are simultaneous approximate eigenvectors of \(S,S^*\) at \(-1\), so for fixed \(k\) the norm limit on \(x_N\) gives the reverse bound.

For \(0<t<1\) take \(N=2k\).
For \(0\le j<k\) the inner product of \(x_N\) against \(S^jD_t(S^*)^{k-1-j}x_N\) has sign \((-1)^{k-1}\) and absolute value at least
\[
 \frac{N-\max(j,k-1-j)}{N}t^{2(N-1)}\ge\tfrac12 t^{4k}.
\]
Indeed, moving the two shifts to the vectors leaves the diagonal weights on the intersection of two initial segments.
After expanding \(P_t,P_t^*\), each additional shift contributing to a nonzero scalar product changes its sign and also the sign of its scalar coefficient.
Hence all contributions have the same sign, and the constant terms alone give \(\|P_tM_{k,t}P_t^*\|\ge (k/2)t^{4k}\).
The [strong Haagerup inequality](../audits/literature/KS07/Yin_U001.md#ks07-u001) applied to the single circular power gives \(\|c^k\|_\infty\le C_{\rm circ}\sqrt k\), since \(\|c^k\|_2=1\).
For every Hilbert dual the commutator bound is \(2\|E\|\|c^k\|_\infty\), so \(\beta_H(Z_t)\ge\sqrt{k}\,t^{4k}/(4C_{\rm circ})\).
Taking \(k=\lfloor1/(-\log t)\rfloor\) gives \(t^{4k}\ge e^{-4}\) and \(k\asymp(1-t)^{-1}\) near one.

### The explicit Hilbert dual

Put \(Q_n=r_u^n r_u^*(r_v^*)^n\) and \(T_t=\sum_{n\ge0}t^{2n}Q_n\), with norm convergence for \(0<t<1\).
The partial isometry \(Q_n\) replaces a suffix \(uv^n\) by \(u^n\) and vanishes on the other words.
Its initial spaces for different \(n\) are orthogonal by uniqueness of the final run of \(v\)'s.
Its range projection \(F_n\) selects the words ending in \(u^n\), with \(F_0=I\).
It follows that \(T_tT_t^*=\sum_n t^{4n}F_n\), and testing on \(u^N\) as \(N\to\infty\) gives \(\|T_t\|=(1-t^4)^{-1/2}\).
On word vectors \(r_u\) and \(r_v^*\) commute with \(L_c=\ell(u)+\ell(v)^*\), whereas \([r_u^*,L_c]=P_\Omega\) from the vacuum word.
Therefore \([T_t,L_c]=\sum_nt^{2n}r_u^nP_\Omega(r_v^*)^n=J_+D_tJ_-^*\).
For \(B_t=(I-tL_c)^2 T_t(I-tL_c)^2\) the two intertwining identities yield \([B_t,L_c]=K_{f_t}\).
Summing the analytic commutator with \(Z_t\) as above gives \([B_t,L_{Z_t}]=P_\Omega\).
In particular \(\beta_H(Z_t)\le(1+t\|c\|_\infty)^4(1-t^4)^{-1/2}\), completing the two-sided estimate.

### Analytic polynomial commutators on bounded inputs

For \(a\in M\), the Taylor coefficients of \(y_a(w)=\tau((1-wc)^{-1}a)\) are \(\tau(c^na)=(J_-^*a)_n\), using \(\|c^n\|_\infty\le n+1\).
We first show \(\|y_a\|_{H^\infty}\le(16/\pi)\|a\|_\infty\).
For \(X=(\lambda-c)(\lambda-c)^*\), \(\lambda>1\), let \(h(s)=\tau((X+s)^{-1})\) for \(s>0\).
Substitution of the Cauchy transform \(G_X(-s)=-h(s)\) into the [shifted circular formula](#shifted-circular-input) gives
\[
 sh(s)(1+h(s))^2=1-(\lambda^2-1)h(s).
\]
The identity holds first for large \(s\) and then for all \(s>0\) by real analyticity.
Positivity gives \(h(s)\le\min(s^{-1/3},s^{-1})\).
The scalar formula \(x^{-1/2}=\pi^{-1}\int_0^\infty s^{-1/2}(x+s)^{-1}\,ds\) and Tonelli give \(\|(\lambda-c)^{-1}\|_1\le (6+2)/\pi\) by splitting at \(s=1\).
For \(1/2\le |w|<1\), circular invariance and \(1/|w|\le2\) thus give \(\|(1-wc)^{-1}\|_1\le16/\pi\).
For \(|w|\le1/2\), the series and \(\|c^n\|_1\le\|c^n\|_2=1\) give a bound of two.
Tracial duality proves the assertion.

Write \(M_{p,t}=\sum_{k\ge1}p_k M_{k,t}\) and \(J=S+S^*\).
Since \(S^*S=I\), we have \(M_{1,1}=I,\ M_{2,1}=J\) and \(JM_{k,1}=M_{k+1,1}+M_{k-1,1}\) for \(k\ge2\).
The unitary sine transform \(e_j\mapsto \sqrt{2/\pi}\sin((j+1)\theta)\) onto \(L^2(0,\pi)\) diagonalizes \(J\) at \(2\cos\theta\).
By the recurrence \(M_{p,1}\) becomes multiplication by \(d_p(\theta)=\sum_{k\ge1}p_k\sin(k\theta)/\sin\theta\).
For \(y\in H^\infty\), the transform of its Taylor vector is bounded by \(\sqrt{2/\pi}\|y\|_\infty\), using the difference of \(e^{i\theta}y(e^{i\theta})\) and \(e^{-i\theta}y(e^{-i\theta})\) divided by \(2i\) and multiplied by \(\sqrt{2/\pi}\).
Equivalently, first apply the identity to \(y(rz)\), then take the \(L^2\) limit.

For \(j\ge0\) put \(h_j(w)=\sum_{r\ge0}p_{j+r}w^r\).
On the closed span \(V_-\) of the words \(v^N\) the Fock relation \(\ell(v)^*\ell(u)=0\) gives \(p(c)|_{V_-}=\sum_j\ell(u)^j h_j(S^*)\) under \(v^N=e_N\).
The spaces \(\ell(u)^j V_-\) for distinct \(j\) are orthogonal.
Testing the expansion on the first \(N\) coefficients \(\lambda^r/\sqrt N\), simultaneous approximate eigenvectors for polynomials in \(S^*\) at \(\lambda=1,-1\), yields \(\sum_j |h_j(\lambda)|^2\le\|p(c)\|_\infty^2\) at both points.
The Fourier coefficient of \(d_p\) at \(l\in\mathbb Z\) is \((h_{|l|+1}(1)+h_{|l|+1}(-1))/2\), by summing the finite series for \(\sin(k\theta)/\sin\theta\).
Parseval and the preceding two estimates give \(\|d_p\|_{L^2(d\theta/2\pi)}\le\sqrt2\,\|p(c)\|_\infty\) on the circle.
Since \(d_p\) is even, the sine transform gives \(\|M_{p,1}:H^\infty\to H^2\|\le2\|p(c)\|_\infty\).

For \(0<t<1\), \(D_t\) is the Poisson average at radius \(t^2\) of the rotations \(V_\theta e_n=e^{in\theta}e_n\).
The \(j\)-th shift monomial \(S^j(S^*)^{k-1-j}\) has degree \(2j-(k-1)\), so
\[
 \sum_{j=0}^{k-1} S^j V_\theta(S^*)^{k-1-j}
 =e^{-i(k-1)\theta/2}V_{\theta/2}M_{k,1}V_{\theta/2}.
\]
Summing against \(p_k\) makes the integrand \(V_{\theta/2} M_{p_\theta,1} V_{\theta/2}\) with \(p_\theta(z)=e^{i\theta/2}p(e^{-i\theta/2}z)\).
Rotations preserve the two Hardy norms, and \(\|p_\theta(c)\|_\infty=\|p(c)\|_\infty\) by circular invariance.
Thus the same \(H^\infty\to H^2\) estimate holds uniformly in \(t\).
Finally \(\|P_t\|_{H^2\to H^2}\le4\) and \(\|P_t^*\|_{H^\infty\to H^\infty}\le9\), since \(S^*y=(y-y(0))/z\) has supremum norm at most \(2\|y\|_\infty\).
Applying these bounds to \(K_{p,t}=J_+P_t M_{p,t}P_t^*J_-^*\) with the established estimate on \(y_a\) proves the claimed bounded-input inequality.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:04 |
| status | open |
| reason | The radial endpoint, sharp first-kernel bound and Koebe estimates in the two input norms are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All normalized radial univalent laws and the specified Koebe Hilbert and bounded-input estimates. |
| argument | [Argument](#argument) | Exterior compression, bidual radial limit, both Hilbert bounds and the sine-transform estimate on all bounded inputs. |
| dependency | [Univalent circular changes](Yin_C_F0218_v1.md#statement) | Radial inverse approximation, generation, attained least vacuum, fixed-law Hilbert dual and forced inverse divided difference. |
| dependency | [Analytic commutator series](Yin_C_F0218_v1.md#convergent-power-series-and-simultaneous-commutators) | Circular Fock model and norm-convergent analytic series for the radial commutator and polynomial approximation. |
| dependency | [Central-summand transfer](Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) | Transfer of a bounded map on the represented C-star algebra with generator commutator to a bounded-vector dual of no greater norm. |
| dependency | [Polynomial Runge theorem](../audits/literature/GW25/Yin_U001.md#gw25-u001) | Uniform polynomial approximation of the holomorphic inverse on a compact filled Jordan domain. |
| dependency | [Strong Haagerup inequality](../audits/literature/KS07/Yin_U001.md#ks07-u001) | Operator norm upper bound by a constant times the square root of the degree for one normalized circular power. |
| dependency | [Exterior Grunsky input](#exterior-grunsky-input) | Contraction of the square-root-weighted matrix for the exterior normalized map with the stated logarithm sign. |
| dependency | [Disk growth input](#disk-growth-input) | Lower growth bound for a univalent function normalized at zero. |
| dependency | [Shifted circular input](#shifted-circular-input) | Scalar R-transform and the inverse Cauchy-transform identity for the squared singular law at real shifts greater than one. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:15 |
| status | proved |
| reason | Adopt the radial cost identity, sharp kernel bound and Koebe estimates following a whole-proof self-review and a separate independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All normalized radial univalent laws and the specified Koebe Hilbert and bounded-input estimates. |
| argument | [Argument](#argument) | Exterior compression, bidual radial limit, both Hilbert bounds and the sine-transform estimate on all bounded inputs. |
| dependency | [Univalent circular changes](Yin_C_F0218_v1.md#statement) | Radial inverse approximation, generation, attained least vacuum, fixed-law Hilbert dual and forced inverse divided difference. |
| dependency | [Analytic commutator series](Yin_C_F0218_v1.md#convergent-power-series-and-simultaneous-commutators) | Circular Fock model and norm-convergent analytic series for the radial commutator and polynomial approximation. |
| dependency | [Central-summand transfer](Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) | Transfer of a bounded map on the represented C-star algebra with generator commutator to a bounded-vector dual of no greater norm. |
| dependency | [Polynomial Runge theorem](../audits/literature/GW25/Yin_U001.md#gw25-u001) | Uniform polynomial approximation of the holomorphic inverse on a compact filled Jordan domain. |
| dependency | [Strong Haagerup inequality](../audits/literature/KS07/Yin_U001.md#ks07-u001) | Operator norm upper bound by a constant times the square root of the degree for one normalized circular power. |
| dependency | [Exterior Grunsky input](#exterior-grunsky-input) | Contraction of the square-root-weighted matrix for the exterior normalized map with the stated logarithm sign. |
| dependency | [Disk growth input](#disk-growth-input) | Lower growth bound for a univalent function normalized at zero. |
| dependency | [Shifted circular input](#shifted-circular-input) | Scalar R-transform and the inverse Cauchy-transform identity for the squared singular law at real shifts greater than one. |
| review | [Whole-proof self-review](../audits/reviews/Yin_R_F0232_v1.md#whole-proof-finding) | All four statements and eight inputs, including the preliminary Koebe construction in which the reviewer participated. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0234_v1.md#whole-proof-finding) | Entire argument, Grunsky compression, domain transfer, sharp Hilbert norms and analytic-polynomial commutators on bounded inputs. |
