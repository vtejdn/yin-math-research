---
author: Yin
---
# Closable coordinate derivations exclude nonabelian finite type I summands

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\), \(d\ge1\), generate a von Neumann algebra \(M\) with faithful normal probability trace \(\tau\).
Set \(H=L^2(M,\tau)\) and \(\mathcal A=\mathbb C\langle X_1,\dots,X_d,X_1^*,\dots,X_d^*\rangle\), the represented unital star algebra.
Suppose that, for each \(i\), there is a complex-linear outer-bimodule derivation
\[
  \delta_i:\mathcal A\subset H\longrightarrow H\otimes_2H,\qquad
  \delta_iX_j=\delta_{ij}1\otimes1,
\]
closable as a Hilbert-space operator.
Its values on the adjoints are arbitrary coarse Hilbert vectors consistent with these hypotheses.

* If \(d=1\), the finite type I central summand of \(M\) is abelian and has no atoms.
  In particular, if \(M\) is type I, its generator \(X=X_1\) is normal.
* If \(d\ge2\), the finite type I central summand of \(M\) is zero.

Both conclusions apply under the [actual ACSY condition \(\mathsf A\)](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
For one generator in a finite type I algebra, actual ACSY gives a dual \(D\) with \(M\subset\operatorname{Dom}D\cap\operatorname{Dom}D^*\) and \(XD(a)-D(Xa)=\tau(a)1\) for every \(a\in M\).
Its restriction is bounded from the operator norm to \(L^2\).
The number of homogeneous summands and their matrix sizes can be unbounded.

## Argument

### A closable derivation respects the two kernel projections

Fix one of the derivations and write it as \(\delta\).
For \(q\in\mathcal A\), let \(p\) be the projection onto \(\ker q\) and \(r\) the projection onto \(\ker q^*\).
On the coarse bimodule use left multiplication on the first tensor factor and right multiplication on the second.
We claim
\[
                         r\,\delta(q)\,p=0.                         \tag{1}
\]
For \(t>0\) put \(b=q^*q\), \(g_t=(1+tb)^{-1}\), \(h_t=(1+tqq^*)^{-1}\) and \(f_t=qg_t\).
For fixed \(t\), choose \(c>1+t\|q\|^2\).
The Neumann polynomials \(g_{t,N}=c^{-1}\sum_{k=0}^N(1-(1+tb)/c)^k\) converge in operator norm to \(g_t\).
Their derivatives converge in coarse norm since the derivative of the \(k\)-th power of \(u=1-(1+tb)/c\) has norm at most \(k\|u\|^{k-1}\|\delta u\|_2\) and \(\|u\|<1\).
Differentiating the polynomial geometric-series identity \((1+tb)g_{t,N}=1-u^{N+1}\) and passing to the limit gives \(\bar\delta g_t=-t g_t(\delta b)g_t\).
Multiplying the same approximants by \(q\) gives \(f_t\in\operatorname{Dom}\bar\delta\) and
\[
        \bar\delta f_t=h_t(\delta q)g_t-t f_t(\delta(q^*))f_t .      \tag{2}
\]
Here \(\delta b=(\delta(q^*))q+q^*\delta q\) and \(1-tqg_tq^*=h_t\).
Since \(\|g_t\|,\|h_t\|\le1\) and \(\|f_t\|\le1/(2\sqrt t)\), the inputs converge to zero in operator norm and the derivatives have norm at most \(\|\delta q\|_2+\|\delta(q^*)\|_2/4\).
For \(t\) tending to infinity through integers, every weak cluster point of \((f_t,\bar\delta f_t)\) belongs to the weakly closed graph and has first coordinate zero.
Consequently \(\bar\delta f_t\rightharpoonup0\).
As \(rh_t=r,\ g_tp=p,\ rf_t=f_tp=0\), multiplying (2) by the two projections proves (1).

For every central projection \(e\) and every \(q\in\mathcal A\) with \(eq=0\), one has \(e\le p,r\).
Thus \(e\delta(q)e=0\), and
\[
                 \delta_{i,e}(eq)=e\,\delta_i(q)\,e                   \tag{3}
\]
defines an outer derivation on the represented algebra \(e\mathcal A\) with values in \(eH\otimes_2eH\).
It takes \(eX_j\) to \(\delta_{ij}e\otimes e\).
The construction only needs closability on the original algebra.
Applying (1) to \(q=X_i-\lambda1\) gives \(r\otimes p=0\) for the \(i\)-th derivation.
The polar decomposition in \(M\) gives \(\tau(r)=\tau(p)\), so faithfulness gives \(p=r=0\) for every \(\lambda\in\mathbb C\).

### Homogeneous summands and matrix fibers

The [finite type I structure theorem](#type-i-structure-source) realizes the type I central summand of \(M\) as a product of homogeneous algebras of the form \(L^\infty(T,\nu;M_n(\mathbb C))\), with \(n\) finite on each component.
Only countably many nonzero component units are possible under the faithful finite trace.
Fix one with unit \(e\) and use the finite measure \(\mu(B)=\tau(e\mathbf1_B)\) on its center, equivalent to the displayed component measure.
On this component \(\tau(a)=\int\operatorname{tr}_n(a(s))\,d\mu(s)\), where \(\operatorname{tr}_n=\operatorname{Tr}/n\).
Indeed traciality kills off-diagonal matrix units with central coefficients and gives equal weights on all diagonal units.
The corresponding Hilbert tensor is the square-integrable product field over \(\mu\times\mu\), with normalized Hilbert--Schmidt inner products on the two matrix legs.

In the one-coordinate case put \(x_s=(eX)(s)\).
The represented star words in \(eX\) generate the entire matrix algebra at almost every \(s\).
To see this, \(e\mathcal A\) is dense in \(L^2(eM)\) since \(\mathcal A\) is dense in \(H\).
Approximate each of the finitely many constant matrix units there by polynomials and pass to subsequences converging pointwise almost everywhere in matrix norm.
The linear span of the star words at a fixed \(s\) is a finite-dimensional closed algebra, so it contains every matrix unit off one null set.
For every fixed \(\lambda\), the set of \(s\) for which \(\lambda\in\sigma(x_s)\) has measure zero by the kernel result, since the trace of the corresponding fiber kernel is at least \(1/n\).
In particular, Fubini gives \(\sigma(x_s)\cap\sigma(x_t)=\varnothing\) for almost every \((s,t)\).
The event is measurable, for instance by the resultant of the two characteristic polynomials.

### Splitting the two-point upper triangular representation

Write \(D(p)_{s,t}=(\delta_{1,e}(p(eX,eX^*)))_{s,t}\) for a formal star polynomial, with constants evaluated using unit \(e\).
For a tensor \(a\otimes b\) and indices \(i,j\in\{1,\ldots,n\}\), define its \((i,j)\)-component to be the matrix with entry \(a_{ri}b_{j\ell}\) in position \((r,\ell)\), extending linearly to the fiber.
Write \(D_{ij}(p)\) for this component of \(D(p)_{s,t}\).
These components intertwine the outer actions with matrix multiplication on the left and right.
For fixed \(s,t,i,j\) this gives an algebra representation of formal star polynomials
\[
      \rho(p)=\begin{pmatrix}p(x_s,x_s^*)&D_{ij}(p)\\
                              0&p(x_t,x_t^*)\end{pmatrix}.             \tag{4}
\]
Specifically, choose representatives for the derivatives of the two letters and define the off-diagonal entry by the word rule at every pair where they are defined.
It then represents the original section word by word, simultaneously on a conull set of pairs, by countability.

With \(m=n^2+1\), the image of (4) satisfies
\[
 P(Y,Z)=\sum_{\sigma\in S_m}\operatorname{sgn}(\sigma)
             Y_0 Z_{\sigma(1)}Y_1\cdots Z_{\sigma(m)}Y_m=0.           \tag{5}
\]
Indeed (5) is alternating and multilinear in \(m\) matrices in the \(n^2\)-dimensional space \(M_n\), so holds for all substitutions in \(e\mathcal A\) by fiberwise evaluation.
For substitutions of star words into all \(Y,Z\), (3) gives zero derivative of the resulting represented zero.
Remove the union of the null sets for these countably many substitutions.
For each remaining pair and all \(i,j\), (4) satisfies (5) under arbitrary complex polynomial substitutions by multilinearity in every slot.

Fix such a pair with disjoint spectra and full individual word spans.
The diagonal image in (4) is all of \(M_n\oplus M_n\).
In fact a holomorphic polynomial that is \(1\) modulo the characteristic polynomial of \(x_s\) and \(0\) modulo that of \(x_t\) exists by coprimality.
It realizes \((I,0)\) on the diagonal, and the surjectivity onto each individual matrix algebra now gives both components separately.
The kernel of the diagonal projection on the image of \(\rho\) is a subspace of the upper-right \(M_n\), stable under arbitrary matrix multiplication on both sides by diagonal surjectivity.
A nonzero such subspace contains every matrix unit, by multiplying a nonzero entry by matrix units.
In this case the image would be the whole block upper triangular algebra.

That algebra violates (5).
In its \(2n\)-dimensional matrix notation let \((a_k,b_k)\), \(1\le k<m\), list all \(n^2\) ordered pairs in the first block, and set \(a_m=b_m=n+1\).
Take \(Z_k=E_{a_k b_k}\), \(Y_0=E_{1a_1}\), \(Y_k=E_{b_k a_{k+1}}\) for \(1\le k<m\), and \(Y_m=E_{b_m,n+1}\).
All these units belong to the block upper triangular algebra.
The two neighbors of the \(k\)-th slot require the exact row \(a_k\) and column \(b_k\) of its \(Z\)-entry.
The identity permutation alone contributes, with value \(E_{1,n+1}\ne0\).
Thus the diagonal projection is an isomorphism on the image of \(\rho\).
Its unique lift of the central idempotent \((I,0)\) has form \(\left(\begin{smallmatrix}I&K_{ij}\\0&0\end{smallmatrix}\right)\) and commutes with every \(\rho(p)\).
Comparing upper-right entries gives
\[
              D_{ij}(p)=p(x_s,x_s^*)K_{ij}-K_{ij}p(x_t,x_t^*).       \tag{6}
\]

### The adjoint value and the planar divergence

On the Hilbert space of \(n\times n\) matrices with ordinary Hilbert--Schmidt norm put \(S(C)=x_s C-Cx_t\).
The operator is invertible because \(x_s C=Cx_t\) implies \(C=0\) on applying the separating polynomial used above.
The \((i,j)\)-component of \(\delta_{1,e}(eX)=e\otimes e\) is \(E_{ij}\).
Thus (6) forces \(K_{ij}=S^{-1}(E_{ij})\) and \(D_{ij}(X^*)=S^*S^{-1}(E_{ij})\), since \(S^*(C)=x_s^*C-Cx_t^*\).
The normalized coarse norm is therefore
\[
 \|D(X^*)_{s,t}\|_2^2
 =\frac{1}{n^2}\sum_{i,j}\|S^*S^{-1}(E_{ij})\|_{\rm HS}^2
 \ \ge\ \frac{1}{n^2}\|S^*S^{-1}\|_{\rm op}^2 .                    \tag{7}
\]
This determination of the adjoint value uses only pointwise finite matrices and takes no global integral of \(S^{-1}\).

Assume \(n\ge2\).
Choose a measurable eigenvalue \(\lambda_s\) of \(x_s\) and measurable unit eigenvector \(v_s\).
For example, the multiset of roots is continuous as an unordered multiset in the characteristic coefficients, and ordering by real part followed by imaginary part gives Borel branches.
Normalizing the first nonzero column of the projection onto \(\ker(x_s-\lambda_s)\) gives a measurable unit eigenvector, since this projection is the limit of \((I+k(x_s-\lambda_s)^*(x_s-\lambda_s))^{-1}\).
At every point where the star words span \(M_n\), the line of \(v_s\) cannot reduce \(x_s\), since then it would reduce every matrix.
Thus \(b_s=\|(I-v_sv_s^*)x_s^*v_s\|>0\) there.
Choose a positive-measure set \(B\) and \(c>0\) with \(b_s\ge c\) on \(B\).
For each good pair \((s,t)\in B^2\) choose a unit vector \(u\) with \(x_t^*u=\bar\lambda_t u\).
The matrix \(C=v_su^*\) has Hilbert--Schmidt norm one and \(S(C)=(\lambda_s-\lambda_t)C\).
Left multiplication by \(I-v_sv_s^*\) applied to \(S^*C=x_s^*v_su^*-v_su^*x_t^*\) gives norm \(b_s\).
Hence (7) yields
\[
              \|D(X^*)_{s,t}\|_2\ \ge\ \frac{c}{n|\lambda_s-\lambda_t|}.
                                                                        \tag{8}
\]
The pushforward \(\eta=\lambda_*(\mu|_B)\) is a nonzero diffuse measure with bounded planar support by the kernel result and boundedness of \(X\).
Its integral of \(|z-w|^{-2}\) over \(\eta\otimes\eta\) is infinite by the [planar grid estimate](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation).
Indeed, a grid with \(O(r^{-2})\) cells of diameter at most \(r\) covering its support gives \((\eta\otimes\eta)\{|z-w|\le r\}\ge c'\eta(\mathbb C)^2 r^2\) by Cauchy--Schwarz for \(0<r\le1\).
Integrating against \(2r^{-3}\,dr\) gives the divergence.
Equation (8) contradicts square integrability of \(e\delta(X^*)e\).
All homogeneous pieces with \(n\ge2\) are therefore absent.
An atom in the remaining abelian summand would give a positive-trace kernel for \(X-\lambda\) at its scalar value.
If \(M\) is type I this proves normality of \(X\) in all of \(M\).

### Two or more coordinates

For any nonzero central \(e\), (3) prevents a nonzero holomorphic polynomial relation among the \(eX_i\).
Otherwise take a nonzero such relation of least degree \(k\ge1\).
The evaluations of the words of length strictly less than \(k\), including the empty word \(e\), are linearly independent.
Their elementary tensors are linearly independent in \(eH\otimes_2eH\).
Applying \(\delta_{i,e}\) to the relation gives the sum of its holomorphic word cuts, by (3).
For each word \(w\) of length less than \(k\), the coefficient of \(e\otimes w(eX)\) is exactly the coefficient of \(x_iw\) in the original relation, since that cut has empty prefix.
All nonconstant coefficients must vanish, a contradiction.

For \(d\ge2\), a nonzero homogeneous central piece of rank \(n\) always gives a relation of this kind.
The ordinary alternating sum of products of \(m=n^2+1\) variables vanishes on \(M_n\) by dimension.
Substitute \(x_1x_2^j\) for the \(j\)-th variable, \(1\le j\le m\).
The resulting formal polynomial is nonzero because the lengths of the successive runs of \(x_2\) after each \(x_1\) recover the entire permutation.
It evaluates to zero on the whole homogeneous piece, contradicting (3) and the minimal-degree argument.

### Actual ACSY and full domains in the scalar case

Under actual ACSY, the adjoint vacuum gives closability of each \(\delta_i\) by the [core-tensor adjoint argument](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff).
For single \(X\) in type I, write \(X(z)=z\) in the resulting abelian spectral model with diffuse compactly supported probability law.
Differentiating \(Xp=pX\) gives \(\delta p(z,w)=(p(z)-p(w))/(z-w)\) almost everywhere for each represented star polynomial.
The vacuum hypothesis therefore supplies exactly the actual scalar adjoint identity of the [canonical scalar-domain estimate](Yin_C_F0055_v1.md#statement).
That estimate gives \(M\subset\operatorname{Dom}E\cap\operatorname{Dom}E^*\) for the closure \(E\) of the polynomial right contraction \(E_0=(\mathrm{id}\otimes\tau)\delta\), together with boundedness \(M\to H\).
On polynomials \(E_0(Xa)=XE_0(a)+\tau(a)1\).
Approximating \(a\) by a sequence from its original graph core extends the identity to all \(a\in\operatorname{Dom}E\), including \(Xa\in\operatorname{Dom}E\), since \(X\) is bounded and the trace-vector pairing is continuous on \(H\).
Then \(D=-E\) has the required generator-first sign, full domains and bounded restriction.

## Provenance and scope

This proof was developed for [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
The two-dimensional [central-polynomial and pole calculation](Yin_C_F0215_v1.md#statement) gives a distinct normality argument under explicit injectivity in its weaker derivation formulation.
Here closability supplies central localization, the matrix identity (5) is proved directly, and the adjoint estimate (8) treats all Jordan forms with the same first-order lower bound.
For a single generator the argument leaves the type \(\mathrm{II}_1\) central summand unrestricted.

<a id="type-i-structure-source"></a>
### Source for the finite type I decomposition

Piotr Niemiec and Adam Wegert, *Algebra of operators affiliated with a finite type I von Neumann algebra*, Theorem 2.2 on numbered and PDF p. 3 of [arXiv:1307.4696v1](https://arxiv.org/pdf/1307.4696v1#page=3), state the bounded-algebra product decomposition used here.
The statement and the preceding definitions of its bounded product and matrix-valued measure spaces were checked in that edition.
The authors present it as a classical structure theorem and cite earlier sources for its derivation.
The present source inspection covers that statement and its applicability to the finite type I central summand, without a proof audit of the underlying classification.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:25 |
| status | open |
| reason | The summand exclusion and the actual scalar full-domain consequence are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Type I summands for one or more coordinates under closable derivations and the actual ACSY full-domain consequence. |
| argument | [Argument](#argument) | Kernel truncation and central descent, measurable fibers, the two-point triangular identity and splitting, the adjoint lower bound, planar energy, multi-coordinate polynomial relations and scalar domains. |
| dependency | [Type I structure source](#type-i-structure-source) | Niemiec and Wegert, Theorem 2.2, realizing any finite type I algebra as a product of measurable finite-matrix algebras. |
| dependency | [Critical planar energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Grid lower bound and divergence of inverse-square energy for a finite nonzero diffuse measure of bounded planar support. |
| dependency | [ACSY closability](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | The actual vacuum puts core tensors in the adjoint domain for each possibly nonreal derivation. |
| dependency | [Scalar canonical domains](Yin_C_F0055_v1.md#statement) | The actual divided-difference vacuum gives operator-norm bounds and both bounded-input domains for the scalar right contraction. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:30 |
| status | proved |
| reason | Adopt the type I summand exclusion for closable coordinate derivations and the resulting one-generator positive implication after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Type I summands for one or more coordinates under closable derivations and the actual ACSY full-domain consequence. |
| argument | [Argument](#argument) | Kernel truncation and central descent, measurable fibers, the two-point triangular identity and splitting, the adjoint lower bound, planar energy, multi-coordinate polynomial relations and scalar domains. |
| dependency | [Type I structure source](#type-i-structure-source) | Niemiec and Wegert, Theorem 2.2, realizing any finite type I algebra as a product of measurable finite-matrix algebras. |
| dependency | [Critical planar energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Grid lower bound and divergence of inverse-square energy for a finite nonzero diffuse measure of bounded planar support. |
| dependency | [ACSY closability](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | The actual vacuum puts core tensors in the adjoint domain for each possibly nonreal derivation. |
| dependency | [Scalar canonical domains](Yin_C_F0055_v1.md#statement) | The actual divided-difference vacuum gives operator-norm bounds and both bounded-input domains for the scalar right contraction. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0224_v1.md#whole-proof-finding) | All four direct interfaces, central localization, splitting, matrix norm, eigenline energy, arbitrary ranks and both scalar domains. |
