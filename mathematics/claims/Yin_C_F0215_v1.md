---
author: Yin
---
# An ACSY generator in a field of matrices of order at most two is normal

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be an essentially bounded measurable field \(t\mapsto X_t\) in matrices of order \(k(t)\in\{1,2\}\) over a probability space \((T,\nu)\).
Equip the field algebra with the integral of the normalized fiber traces and \(M=W^*(X)\) with its restricted faithful normal probability trace.
Thus the result also applies to a generator of any finite tracial von Neumann algebra given by a direct integral of type \(\mathrm I_1\) and \(\mathrm I_2\) fibers, and to a generator admitting such a faithful trace-preserving representation.

If \(X\) satisfies the [actual one-coordinate ACSY condition](../tasks/Yin_T_F0011_v1.md#contract), it is normal almost everywhere, \(M\) is abelian, and \(X\) satisfies the strong and bare full-domain dual conditions.
The proof of normality only requires an outer derivation
\[
 \delta:\mathbb C\langle X,X^*\rangle\longrightarrow
 L^2(M)\otimes_2L^2(M),\qquad \delta X=1\otimes1,
 \tag{1}
\]
on the represented star algebra and the assumption that \(X-\lambda1\) has zero kernel for every \(\lambda\in\mathbb C\).
Under actual ACSY the latter assumption follows from maximal \(\Delta\).
There is no holomorphic polynomial centrality hypothesis, restriction on the dimension of the parameter space, regularity of its measure, or uniform spectral-gap or eigenbasis bound.

On any positive-measure nonnormal part with distinct eigenvalues, (1) would locally force \(\|\delta X^*(t,s)\|\ge c/|\lambda(t)-\lambda(s)|\) for a selected eigenvalue branch and almost every pair in a positive-measure subset.
On a nonnormal repeated-root part the forced lower bound near the eigenvalue diagonal has order \(c/|\lambda(t)-\lambda(s)|^3\).
Both lower bounds contradict square integrability under the no-kernel hypothesis.
Here the fiber norm is the Hilbert tensor norm for the two normalized Hilbert--Schmidt traces.

## Argument

### Eigenvalue distributions and central polynomials in the represented algebra

The [ACSY maximal-\(\Delta\) implication](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) and the [affiliated invertibility of full polynomials](../audits/literature/MSY23/Yin_U001.md#exact-introductory-interfaces) imply that \(X-\lambda1\) is injective for every complex \(\lambda\).
Indeed the corresponding one-variable polynomial is nonzero and full of size one.
In the argument below one may instead assume injectivity directly.
In particular no fixed complex number is an eigenvalue of \(X_t\) on a set of positive measure.
The kernel projection is \(\mathbf1_{\{0\}}((X-\lambda)^*(X-\lambda))\in M\), and its trace integrates the normalized dimensions of the fiber kernels.

Only the nonnormal order-two parameter set \(D\) needs inspection.
Use the ordinary, unnormalized two-by-two matrix trace \({\rm Tr}\) for algebraic identities.
For \(C=[X,X^*]\), the matrices \(C_t\) are selfadjoint and traceless; Cayley--Hamilton gives \(C_t^2=c(t)I\) with \(c(t)>0\) on \(D\).
The polarized two-by-two Cayley--Hamilton identity with a traceless \(C_t\) reads
\[
 A C_t+C_t A=({\rm Tr}A)C_t+{\rm Tr}(A C_t)I .
\]
For \(A=X_t^j\), cyclicity gives \({\rm Tr}(X_t^j C_t)=0\).
Consequently the three represented star polynomials
\[
 Z_0=C^2,\qquad Z_j=(X^j C+C X^j)C\quad(j=1,2)
\]
are scalar fiberwise everywhere, including zero on scalar fibers.
They are central elements of the original polynomial algebra.
On \(D\) their scalar values form \(z(t)=c(t)(1,{\rm Tr}X_t,{\rm Tr}X_t^2)\).
Its law restricted to \(D\) has no atom because fixing this triple fixes the two traces since \(c>0\), hence fixes the unordered roots of the characteristic polynomial, contradicting the no-eigenvalue-atom property if the triple had positive mass.
Thus for almost every \((t,s)\in D^2\) at least one \(Z_j\) has different scalar values at the two endpoints.
Likewise the spectra of \(X_t\) and \(X_s\) are disjoint for almost every pair, since at a fixed \(s\) there are at most two eigenvalues to exclude at \(t\), and Fubini applies since the condition of a common characteristic root is measurable.

### The localized Sylvester equation

Include \(L^2(M)\) isometrically in the ambient Hilbert space of square-integrable matrix fields and similarly include its coarse bimodule in the product field with fibers \(M_{k(t)}\otimes_2 M_{k(s)}\).
The outer difference for a polynomial \(a\) is the linear operator \(D_a=L_{a(t)}\otimes I-I\otimes R_{a(s)}\), where \(L,R\) mean left and right matrix multiplication.
Take simultaneous representatives of the finitely many vectors for \(a=X,X^*,Z_0,Z_1,Z_2\) and their differentiated commutation identities.
Differentiating \(Z_j a=a Z_j\) gives
\[
     (Z_j(t)-Z_j(s))\,\delta a(t,s)=D_a\,\delta Z_j(t,s).
\]
Here \(Z_j(t)\) in the scalar difference denotes its scalar value.
On each pair where at least one difference is nonzero, divide the corresponding \(\delta Z_j\) by that scalar to obtain a fiber tensor \(h\) with
\[
        D_Xh=I\otimes I,\qquad
        \delta X^*(t,s)=D_{X^*}h .                         \tag{2}
\]
Only pointwise division is needed.
On the disjoint-spectrum pairs the Sylvester operator \(D_X\) is invertible, as also follows from the two explicit inverse formulas below on the respective sets being tested.
In particular the forced \(h\) on these sets is independent of the separating central polynomial chosen.
The proof uses fibers and spectral idempotents to test (2) and never applies the original derivation to a measurable spectral field.

### Simple eigenvalues

Suppose the nonnormal simple-spectrum subset of \(D\) has positive measure.
The space of complex two-by-two matrices is separable, and at every such matrix a neighborhood admits continuous distinct eigenvalue labels \(\lambda_1,\lambda_2\) and continuous rank-one idempotents \(P_1,P_2\).
For example \(P_1=(X-\lambda_2 I)/(\lambda_1-\lambda_2)\) and \(P_2=I-P_1\).
We may restrict to a positive-measure subset lying close to a single nonnormal simple-spectrum matrix by taking local neighborhoods as chosen below and a countable subcover.
These idempotents are only required to be bounded on that neighborhood.

On the selected pairs, the commuting operators \(L_{P_i(t)}\otimes R_{P_j(s)}\) give the spectral decomposition of \(D_X\).
Its inverse on \(I\otimes I\) is
\[
 h=\sum_{i,j=1}^2
      \frac{P_i(t)\otimes P_j(s)}
           {\lambda_i(t)-\lambda_j(s)} .
\]
Write \(P=P_1,\ \lambda=\lambda_1\).
Filter (2) by **right** multiplication by \(P(t)\) on its first leg and **left** multiplication by \(P(s)\) on its second leg.
These two multipliers commute with \(D_{X^*}\), and the idempotent identities eliminate every term of \(h\) except \(i=j=1\).
The resulting tensor is
\[
 \frac{X_t^*P(t)\otimes P(s)-P(t)\otimes P(s)X_s^*}
      {\lambda(t)-\lambda(s)} .                             \tag{3}
\]
At identical endpoints \(X_t=X_s=x\), with the chosen idempotent \(p\), the numerator is nonzero.
Were \(x^*p\otimes p=p\otimes p x^*\), equality of these simple tensors with \(p\ne0\) would imply \(x^*p=\alpha p\) for some scalar \(\alpha\), also when both sides vanish.
The eigenline \({\rm ran}(p)\) would then be invariant under both \(x\) and \(x^*\).
Its orthogonal complement would be a second invariant line, making the two-by-two matrix \(x\) normal, a contradiction.
By continuity at \((x,x)\), shrink the neighborhood so the numerator norm is at least \(b>0\) for all pairs in it and both projector norms are at most \(L<\infty\).
Since the filtering operator has norm at most \(L^2\), (3) yields the asserted bound with \(c=b/L^2\) on the chosen positive-measure subset.

### Repeated eigenvalues

If the nonnormal repeated-root subset has positive measure, then \(X_t=\lambda(t)I+N_t\) there with \(\lambda(t)={\rm Tr}(X_t)/2,\ N_t^2=0,\ N_t\ne0\).
These assignments are continuous on the repeated-root locus.
For disjoint-spectrum pairs put \(d=\lambda(t)-\lambda(s)\) and \(K=L_{N_t}\otimes I-I\otimes R_{N_s}\).
Then \(K^3=0\) and \((dI+K)^{-1}=d^{-1}I-d^{-2}K+d^{-3}K^2\).
In (2) this gives
\[
 h=\frac{I\otimes I}{d}
     -\frac{N_t\otimes I-I\otimes N_s}{d^2}
     -\frac{2N_t\otimes N_s}{d^3}.
\]
Multiply the second equation of (2) by \(d^3\).
Since \(D_{X^*}=\bar d I+L_{N_t^*}\otimes I-I\otimes R_{N_s^*}\), the resulting continuous expression is
\[
 (\bar d I+L_{N_t^*}\otimes I-I\otimes R_{N_s^*})
 \big(d^2 I\otimes I-d(N_t\otimes I-I\otimes N_s)-2N_t\otimes N_s\big).
 \tag{4}
\]
At identical \(x=\lambda I+N\) its value is \(-2(N^*N\otimes N-N\otimes NN^*)\ne0\).
Indeed \(N^*N\) has positive trace while the nonzero \(N\) has zero trace, so these first factors are linearly independent and \(NN^*\ne0\).
By continuity on this locus, a sufficiently small neighborhood of \(x\) gives a uniform positive lower bound on the norm in (4).
Take a countable cover by such neighborhoods and select one with positive measure.
Division by \(|d|^3\) gives the claimed estimate for almost every pair there.
This argument allows arbitrary variation of the eigenvectors, nilpotent amplitudes and parameters.

### Planar divergence and dual domains

The pushforward of the restricted positive measure by the chosen eigenvalue map is a finite nonzero diffuse measure \(\eta\) on a bounded subset of \(\mathbb C\).
Diffuseness follows from the no-eigenvalue-atom property.
For completeness, a grid of \(O(r^{-2})\) squares of diameter at most \(r\) covers its support at every sufficiently small \(r>0\).
The sum of the squared masses of these squares is at least \(c_\eta r^2\) by Cauchy--Schwarz, using a disjoint grid partition.
Therefore \((\eta\otimes\eta)\{0<|z-w|\le r\}\ge c_\eta r^2\).
Integrating against \(2r^{-3}\,dr\) proves \(\int_{z\ne w}|z-w|^{-2}\,d\eta^2=\infty\), as in the [central polynomial diagonal estimate](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation).
The same integral with exponent six diverges even on \(|z-w|\le1\).
Thus either positive-measure nonnormal case contradicts \(\delta X^*\in L^2(M)\otimes_2 L^2(M)\).
Normality holds almost everywhere and \(W^*(X)\) is abelian.

For actual ACSY, the [scalar normal canonical-domain theorem](Yin_C_F0055_v1.md#statement) now gives full domains for the canonical right contraction and its actual adjoint.
Indeed diffuse scalar normality forces the starred derivative to equal the phase \((\bar z-\bar w)/(z-w)\) by differentiating \(XX^*=X^*X\) off the product-null diagonal, so the derivation is the scalar divided difference on the represented star core.
The actual scalar vacuum hypothesis is precisely the original vacuum pairing there.
The negative canonical contraction has the generator-first commutator on all bounded inputs, by the core identity and bounded strong approximation using the closed graph.
It is a strong dual, hence also a bare full-domain dual.

## Scope

This argument for [T_F0011](../tasks/Yin_T_F0011_v1.md#contract) extends the [single diffuse Jordan example](../ledger/Yin_L_F0049_v1.md#a-diffuse-jordan-operator-also-fails-the-starred-derivation-premise) using central star polynomials particular to size two.
The spectral values may vary without a prescribed holomorphic polynomial relation across the fibers.
The argument leaves higher dimensions and the unrestricted general implication open.

## Assessment history

### Decision two-dimensional-fibers-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:19 |
| status | open |
| reason | Complete candidate forcing normality from simple-root and Jordan singularities of the starred derivative in all tracial matrix fields of order at most two. Independent review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual ACSY implies normality, strong and bare domains; the weaker normalized-derivation normality result and both local pole lower bounds. |
| argument | [Argument](#argument) | Central trace polynomials, null spectral collisions, outer and opposite-leg filters, simple and repeated spectrum, planar divergence, and scalar canonical domains. |
| dependency | [ACSY maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 gives maximal Delta from the actual ACSY premise in the general bounded one-generator setting. |
| dependency | [Affiliated invertibility](../audits/literature/MSY23/Yin_U001.md#msy23-u001) | Theorem 1.1 gives injectivity of each nonzero scalar polynomial from maximal Delta. |
| dependency | [Planar diagonal energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Grid lower bound for the order-two energy of a finite nonzero diffuse bounded planar measure, also proved directly here. |
| dependency | [Scalar canonical domains](Yin_C_F0055_v1.md#statement) | Actual scalar divided-difference vacuum supplies the bounded-input closure and adjoint domains, including the canonical core commutator. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:30 |
| status | proved |
| reason | Adopt normality and the two explicit pole bounds for fields of order at most two after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual ACSY implies normality, strong and bare domains; the weaker normalized-derivation normality result and both local pole lower bounds. |
| argument | [Argument](#argument) | Central trace polynomials, null spectral collisions, outer and opposite-leg filters, simple and repeated spectrum, planar divergence, and scalar canonical domains. |
| dependency | [ACSY maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 gives maximal Delta from the actual ACSY premise in the general bounded one-generator setting. |
| dependency | [Affiliated invertibility](../audits/literature/MSY23/Yin_U001.md#msy23-u001) | Theorem 1.1 gives injectivity of each nonzero scalar polynomial from maximal Delta. |
| dependency | [Planar diagonal energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Grid lower bound for the order-two energy of a finite nonzero diffuse bounded planar measure, also proved directly here. |
| dependency | [Scalar canonical domains](Yin_C_F0055_v1.md#statement) | Actual scalar divided-difference vacuum supplies the bounded-input closure and adjoint domains, including the canonical core commutator. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0223_v1.md#whole-proof-finding) | All four inputs, the two spectral filters, both pole orders, critical planar energy and the scalar adjoint domains. |
