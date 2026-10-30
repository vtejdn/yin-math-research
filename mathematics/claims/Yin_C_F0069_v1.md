---
author: Yin
---
# Automatic norm continuity of full-domain normal duals and the scalar converse

Date: 2026-10-14.
Human author Yin.
The bare_dual exploration agent developed this argument; a separate auto_continuity_check agent checked the triangular construction and supplied the elementary no-divisible-subspace proof.
Root organized the fixed statement.
This work addresses the explicitly requested comparison with ACSY24.
It does not assert the general correlated-normal converse.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be finite tracial with faithful normal tracial state, H=L2(M,tau), Omega=1 and P the projection onto C Omega.
Identify a with a Omega.
Commutators are evaluated on M Omega, with no continuity or closability premise.

**A. Automatic continuity.**
If x in M is bounded and normal and E:M Omega -> H is complex linear with [E,x]=P, then x has nonatomic spectral distribution and
\[
 \|E(a\Omega)\|_2\le C\|a\|\quad(a\in M)
\]
for some C<infinity.
Consequently every member of a bare linear full-domain dual system [X_j,D_i]=delta_ij P for a normal tuple is bounded M -> H.
Neither generation nor a vacuum-adjoint assumption is needed.

**B. Scalar converse.**
If x=x*, M=W*(x), and a bare linear D:M Omega -> H satisfies [x,D]=P, the polynomial divided-difference derivation
\[
 \partial:\mathbb C[x]\to H\otimes_2H,\qquad \partial x=\Omega\otimes\Omega
\]
is well-defined and has the actual vacuum-adjoint condition
\[
 \Omega\otimes\Omega\in\operatorname{Dom}\partial^*.
\]
For E(a)=-D(a)+aD(1) and C=||E:M -> H||, one has ||partial*(Omega tensor Omega)||2 <= 2C.
This is the ACSY24 condition for one selfadjoint generator.
For a selfadjoint coordinate of any bare normal dual tuple the same conclusion holds in its marginal algebra after compression onto the marginal L2 space; this does not assert joint conjugate variables.

## Argument

### A. Automatic boundedness

**Proposition.**
Let x be a bounded normal element of a finite tracial von Neumann algebra M.
If a complex-linear map E:M Omega -> H satisfies [E,x]=P on M Omega, then E is bounded as a map M with its operator norm to H.
No closability or adjoint condition is assumed.
Consequently every member of a bare full-domain dual system for a normal tuple is bounded from M to H.

Write N=lambda(x) on H and T(a)=xa on the Banach space M.
First x has diffuse spectral distribution.
Indeed, if p=1_{lambda}(x) is a nonzero spectral projection, then

\[
 (x-\lambda)E(p\Omega)=-\tau(p)\Omega.
\]

Multiplication on the left by p gives 0=-tau(p)p Omega, a contradiction.
Thus N and T have no eigenvalues.

On the Banach space Y=H direct-sum M define

\[
 R=\begin{pmatrix}N&P|_M\\0&T\end{pmatrix},
 \qquad J(a)=(E(a\Omega),a).
\]

The dual relation is precisely RJ=JT.
The map J is so far only algebraic.
We verify the hypotheses of Laursen's Theorem 4.1 rather than presupposing its continuity.

For a smooth function phi on C, put

\[
 \Gamma_\phi=\iint_{z\ne w}
       \frac{\phi(z)-\phi(w)}{z-w}\,dE_x(z)P\,dE_x(w),
 \qquad
 \Phi(\phi)=
 \begin{pmatrix}
    \phi(N)&\Gamma_\phi|_M\\0&L_{\phi(x)}
 \end{pmatrix}.
\]

The double integral is a Hilbert--Schmidt integral: under the spectral tensor realization of P its kernel is the displayed divided difference in L2(mu tensor mu), where mu is the law of x.
On a fixed compact neighborhood of the spectrum its norm is at most the Lipschitz norm of phi.
Restriction to M is bounded into H because ||a||2<=||a||.
The diagonal has zero product measure by diffuseness, so Gamma_z=P and Gamma_1=0.
The elementary divided-difference product identity gives

\[
 \Gamma_{\phi\psi}=\phi(N)\Gamma_\psi+\Gamma_\phi\psi(N),
 \quad \Phi(\phi\psi)=\Phi(\phi)\Phi(\psi),
 \quad \Phi(1)=I,\quad\Phi(z)=R.
\]

This supplies super-decomposability directly.
Given an open cover U_0,U_1 of the spectrum, choose smooth chi_0,chi_1 adding to 1 near the spectrum, with compact supports K_j in U_j.
Put Y_j=closure Ran Phi(chi_j).
Both subspaces are R-invariant, and Phi(chi_0) commutes with R and sends Y into Y_0, while I-Phi(chi_0)=Phi(chi_1) sends Y into Y_1.
If lambda is outside K_j, choose smooth g equal to (z-lambda)^{-1} near K_j.
Multiplicativity shows that Phi(g)|Y_j is an inverse for (R-lambda)|Y_j.
Hence the spectrum of R|Y_j lies in K_j.
This is the definition of super-decomposability, and in particular well-decomposability, used in Laursen's Proposition 3.7.
The input operator T is decomposable: its spectral projections a -> 1_B(x)a split M into closed invariant subspaces for any finite spectral cover.

We next check that R has no nonzero algebraically divisible subspace.
A subspace V is S-divisible if (S-lambda)V=V for every complex lambda.
A bounded normal operator N on a Hilbert space has no nonzero such subspace, by the following elementary argument.
If v lies in one, then v lies in Ran(N-lambda)^2 for every lambda.
With nu_v its finite spectral measure, this implies

\[
 I(\lambda):=\int|z-\lambda|^{-4}\,d\nu_v(z)<\infty
 \quad\text{for every }\lambda.
\]

If nu_v is nonzero, its compact support is the union of the measurable sets A_n={lambda:I(lambda)<=n}, and some A_n has positive nu_v measure.
For lambda in A_n, nu_v(B(lambda,r))<=nr^4.
A grid covers the bounded set A_n by O(r^{-2}) disks of radius O(r), each centered at a point of A_n.
Therefore nu_v(A_n)<=Cnr^2 for all small r, a contradiction.
Thus v=0.
If V is R-divisible, its second-coordinate projection is T-divisible.
The inclusion M -> H sends this to an N-divisible subspace, so that projection is zero.
Now V lies in the first-coordinate copy of H and is N-divisible there; hence V=0.

By [Lau88, Proposition 3.7, printed p. 164](https://dml.cz/bitstream/handle/10338.dmlcz/102208/CzechMathJ_38-1988-1_11.pdf), the algebraic spectral subspace E_R(F) is closed for every closed set F.
Finally, R has no eigenvalues: (R-lambda)(v,a)=0 first implies (T-lambda)a=0, hence a=0, and then (N-lambda)v=0.
Therefore the pair (R,T) has no critical eigenvalues.
[Lau88, Theorem 4.1, printed p. 166](https://dml.cz/bitstream/handle/10338.dmlcz/102208/CzechMathJ_38-1988-1_11.pdf) now makes every algebraic intertwiner from T to R continuous, in particular J.
Its first component is E, proving the proposition.

For the generator-first system of this question apply the proposition to E=-D_i and x=X_i.
This is an operator-norm-to-H bound.
It does not alone assert that D_i is closable as a densely defined operator on H, that Omega belongs to Dom D_i*, or that its closure contains M Omega.

### B. One selfadjoint generator and marginal consequences

Let x=x* generate M and suppose the bare full-domain dual exists.
Identify M=L-infinity(mu), H=L2(mu), with x multiplication by the real coordinate.
Use the preceding proposition and normalize

\[
 E(a)=-D(a)+aD(1),\qquad E1=0,\qquad [E,x]=P.
\]

Then E:M -> H is bounded, say by C.
On polynomials the commutator identity fixes its values as

\[
 E p(s)=\int\frac{p(s)-p(r)}{s-r}\,d\mu(r).
\]

For u_t(s)=exp(its), the same formula holds by uniform polynomial approximation of the exponential and its first derivative on the compact real spectrum.
The divided differences converge uniformly, and E is continuous from the uniform norm into L2.
Define the H-valued Bochner average

\[
 A_T=\frac1{2T}\int_{-T}^{T}u_t^*E u_t\,dt.
\]

The integrand is continuous in H, and ||A_T||2<=C.
Fubini's theorem is valid for finite T because the exponential divided difference is bounded by |t|.
It gives

\[
 A_T(s)=\int
   \frac{1-\operatorname{sinc}(T(s-r))}{s-r}\,d\mu(r),
 \qquad \operatorname{sinc}(u)=\frac{\sin u}{u},\quad\operatorname{sinc}(0)=1.
\]

The kernel is antisymmetric.
Hence, for every complex polynomial p,

\[
 \int p A_T\,d\mu
 =\frac12\iint\frac{p(s)-p(r)}{s-r}
       [1-\operatorname{sinc}(T(s-r))]\,d\mu(s)d\mu(r).
\]

The polynomial divided difference is bounded on the compact square.
Diffuseness makes its diagonal negligible, and sinc(T(s-r)) tends to zero off the diagonal.
Dominated convergence therefore gives

\[
 \lim_{T\to\infty}\int p A_T\,d\mu
 =\frac12(\tau\otimes\tau)(\partial p),
 \qquad
 |(\tau\otimes\tau)(\partial p)|\le 2C\|p\|_2.
\]

Here partial p is the usual polynomial divided difference.
Since a diffuse measure has infinite support, polynomial evaluation is injective and partial is well-defined on C[x].
The displayed estimate is exactly the actual vacuum-adjoint condition: 1 tensor 1 belongs to Dom partial*, with ||partial*(1 tensor 1)||2<=2C.
Thus the ACSY24 condition follows in this scalar selfadjoint case.
By restriction to W*(X_i) and orthogonal projection to L2(W*(X_i)), the same reasoning shows that each real selfadjoint marginal of a bare selfadjoint dual tuple has finite one-variable Fisher information.
It does not yet show joint conjugate variables for a noncommuting tuple.


## Source relationship and unresolved scope

The accepted published inputs are [Lau88, Proposition 3.7 and Theorem 4.1](https://dml.cz/bitstream/handle/10338.dmlcz/102208/CzechMathJ_38-1988-1_11.pdf), at the exact scope of [Lau88-U001](../audits/literature/Lau88/Yin_U001_v1.md#lau88-u001).
The local argument proves each additional premise: diffuseness, decomposability, the triangular smooth calculus, absence of divisible subspaces, and absence of eigenvalues.
The original precursor proof chain of the published automatic-continuity theorem is not re-audited.
Standard spectral calculus, the HS tensor identification, smooth partitions of unity and the Riesz representation theorem are used in their usual bounded-operator settings.

The actual vacuum condition in B is the interface of [ACSY24, Theorem 3.4 and Proposition 3.5](../literature/pdf/ACSY24.pdf), checked in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001).
B proves the required estimate directly; ACSY24 is not applied backwards.
The Fourier average uses neither Hilbert-space closability nor a principal-value theorem.
A bounded search of existing project materials and public dual-system/automatic-continuity literature located Lau88 for A; no exact published scalar converse was verified in that search.
No novelty or priority assertion is made.

Operator-norm continuity alone does not establish Hilbert-space closability, a full starred-core derivation, or a joint L2 vacuum.
The arbitrary correlated normal-tuple converse remains unresolved here.
The scalar or marginal result above must not be promoted to the joint statement.

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14 |
| status | open |
| reason | Complete two-part candidate retained for separate review of the fixed statement, entire argument and exact external interfaces. |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Automatic normal-dual norm continuity and scalar selfadjoint converse, with the exact marginal corollary. |
| argument | [Argument](#argument) | Complete triangular, divisible-subspace and Fourier-average proofs. |
| dependency | [Lau88-U001](../audits/literature/Lau88/Yin_U001_v1.md#lau88-u001) | Accepted Proposition 3.7 and Theorem 4.1 with all local hypotheses checked. |
| support | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001) | Definition and actual adjoint interface only, not an inference of the converse. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T09:27 |
| status | proved |
| reason | A separately organized complete review verified the triangular smooth calculus, all Laursen hypotheses, elementary divisible-subspace argument, Fourier average, actual vacuum estimate and precise marginal boundary. No remaining gap was found. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A and B, including arbitrary normal full-domain continuity and scalar or marginal selfadjoint vacuum. |
| argument | [Argument](#argument) | Complete proof of both parts and the marginal compression, without an assumed Hilbert-space closability or adjoint domain. |
| dependency | [Lau88-U001](../audits/literature/Lau88/Yin_U001_v1.md#lau88-u001) | Accepted Proposition 3.7 and Theorem 4.1, with every local hypothesis verified. |
| support | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001) | Exact actual vacuum-adjoint interface; no converse imported. |
| review | [Independent whole review](../audits/reviews/Yin_R_F0042_v1.md#conclusion) | Complete fixed statement, argument, source hypotheses and unresolved general-tuple boundary. |

