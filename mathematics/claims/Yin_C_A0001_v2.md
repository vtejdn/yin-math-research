---
author: Yin
---
# Complete amenable kernel localization and scalar obstruction descent

This revision extends [the original finite-propagation extraction](Yin_C_A0001_v1.md#statement) to complete kernels of matrices in the actual affiliated rational closure.
It gives a finite descent from a noninteger matrix rank to an actual scalar group-ring zero divisor, a conditional finite matrix whose closed range is the whole Hilbert kernel, and a homological interface for the remaining scalar obstruction.
The equivalence between the amenable Atiyah problem and the group-ring domain problem is established prior knowledge, retained in [the existing amenable comparison](../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation).
No new group-class coverage or solution of the torsion-free amenable zero-divisor problem is asserted.

## Statement

Let \(G\) be a finitely generated amenable group, \(B=\mathbb CG\), \(N=\mathcal N(G)\), and \(U=\mathcal U(N)\), with the faithful left regular representation and the canonical trace.
All matrix traces are unnormalized.
Write \(\nu(P)=\dim_G\ker_{\ell^2}P\) and \(\operatorname{rk}_G P=n-\nu(P)\) for \(P\in M_{m,n}(U)\), with affiliated products interpreted as their closures.
Let \(\mathcal R\) be the actual rational closure of \(B\) inside \(U\), obtained from entries of inverses of matrices over \(B\) that are invertible in the actual ambient algebra.

### Rational kernel localization

Every \(P\in M_{m,n}(\mathcal R)\) admits a finite realization
\[
P=A-B_1Q^{-1}C,\qquad
A\in M_{m,n}(B),\quad B_1\in M_{m,k}(B),\quad
C\in M_{k,n}(B),\quad Q\in M_k(B)\cap GL_k(U).
\tag{1}
\]
For any such realization, put \(L=\begin{pmatrix}A&B_1\\ C&Q\end{pmatrix}\) and let \(w\) be a propagation width of \(L\).
For every finite nonempty \(F\subset G\), with the [right-invariant metric and inner boundary convention](../audits/literature/Ele03/Yin_U001.md#folner-and-propagation),
\[
\nu(P)-(n+k)\frac{|\partial_wF|}{|F|}
\ \le\
\frac{\dim_{\mathbb C}(\ker_{\ell^2}P\cap\mathbb C[F]^n)}{|F|}
\ \le\ \nu(P).
\tag{2}
\]
In particular
\[
\ker_{\ell^2}P=\overline{\ker_{\ell^2}P\cap B^n}^{\,\ell^2}.
\tag{3}
\]
Neither \(Q^{-1}\) nor \(P\) is required to be bounded, and no spectral gap is assumed.

### Finite scalar descent and a complete conditional kernel witness

For every \(A_0\in M_{m,n}(B)\) with noninteger analytic rank, a finite sequence of column deletions and finite-support kernel extractions yields \(0\ne x,z\in B\) with \(xz=0\).
For \(0\ne r\in\mathcal R\) that is not invertible in \(U\), write \(\alpha=\nu(r)\).
Then \(0<\alpha<1\), and a scalar realization (1) yields \(0\ne x\in B\) with
\[
rx=0,\qquad \operatorname{rk}_G x\le\alpha,\qquad
\nu(x)\ge1-\alpha.
\tag{4}
\]
One may choose \(x\) from a finite set \(F\) satisfying
\[
(k+1)|\partial_wF|<\alpha|F|,
\tag{5}
\]
and then choose \(0\ne z\in B\) with \(xz=0\) from a finite set \(F'\) satisfying
\[
|\partial_{w_x}F'|<(1-\alpha)|F'|.
\tag{6}
\]

If \(B\) is a domain, then for every \(A_0\in M_{m,n}(B)\) there is an integer \(d=\nu(A_0)\) and a matrix \(V\in M_{n,d}(B)\) such that
\[
A_0V=0,\qquad \ker_{\ell^2}V=0,\qquad
\ker_{\ell^2}A_0=\overline{\operatorname{im}_{\ell^2}V}.
\tag{7}
\]
For \(d>0\), its orthogonal kernel projection is the bounded affiliated product
\[
p_{A_0}=V(V^*V)^{-1}V^*.
\tag{8}
\]
For \(d=0\), \(p_{A_0}=0\).
Consequently, for amenable \(G\), all complex group-ring matrices have integer kernel dimension if and only if \(\mathbb CG\) is a domain.
These qualitative conclusions also hold for amenable groups not assumed finitely generated.
Equation (7) asserts finite generation after Hilbert-space closure, not finite generation of the algebraic kernel over \(B\).

### The finite projective resolution interface

For \(0\ne a\in B\), write \(K_a=\{x\in B:ax=0\}\), a right \(B\)-module.
Suppose it has an exact finite resolution
\[
0\longrightarrow P_s\longrightarrow\cdots\longrightarrow P_0
\longrightarrow K_a\longrightarrow0,
\qquad P_i=E_iB^{r_i},\quad E_i^2=E_i\in M_{r_i}(B).
\tag{9}
\]
Then
\[
\nu(a)=\sum_{i=0}^s(-1)^i(\operatorname{Tr}\otimes\tau)(E_i).
\tag{10}
\]
For torsion-free amenable \(G\), the established [BCM04 projective-trace theorem](../audits/literature/BCM04/Yin_U001.md#amenable-projective-trace) makes each summand an integer.
Thus in this group class, if every \(K_a\), \(a\ne0\), has such a resolution, then \(B\) is a domain and the full all-matrix Atiyah conclusion holds.
Conversely, a domain has \(K_a=0\), so the indicated finite-resolution property holds trivially.
This last equivalence isolates an unresolved homological obligation; amenability and torsion-freeness alone are not proved here to imply (9).

## Current assessment

[Selected decision](#decision-reviewed-complete-localization)

## Assessment history

### Decision reviewed-complete-localization

| Field | Value |
| --- | --- |
| date | 2026-11-12T12:20 |
| status | proved |
| reason | The complete rational localization, finite descent, conditional Hilbert-kernel witness and finite-projective-resolution formula have passed independent review under their explicit hypotheses; neither the general amenable domain conjecture nor the full Task is resolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every stated quantitative and qualitative assertion, including the additional domain or finite-resolution premises where required. |
| argument | [Complete argument](#argument) | Actual inverse realizations, affiliated domains, finite-set estimates, finite descent, arbitrary amenable group passage and weakly exact Hilbert completion. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0002_v2.md#whole-argument-finding) | Independent inspection of the whole statement and argument and their exact direct interfaces. |
| dependency | [Earlier matrix boundary estimate](Yin_C_A0001_v1.md#matrix-boundary-estimate) | The rectangular finite-propagation inequality, with its stated inner-boundary convention. |
| dependency | [Actual rational-closure interface](../audits/literature/MSY23/Yin_U003.md#msy23-u003) | Definitions 4.7 and 4.10 and Lemma 4.9: entries of actual invertible group-ring matrices and finite block realizations. |
| dependency | [Finite-trace affiliated facts and rank calculus](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Lemmas 5.1–5.5 and 5.9: generalized inverses, injectivity versus invertibility, closed affiliated products, actual rank invariance and kernel/range dimension comparisons. |
| dependency | [BCM04 projective trace](../audits/literature/BCM04/Yin_U001.md#bcm04-u001) | Established integer canonical trace for finite projective modules over torsion-free amenable complex group rings; statement and applicability checked, assembly proof accepted externally. |

The earlier physical version and its selected decision remain fixed at their original scope.
The present acceptance supplies no unconditional existence theorem for the finite resolutions in (9).

## Argument

### Actual realizations and affiliated domains

The precise rational-closure input is [MSY23, Definitions 4.7 and 4.10 and Lemma 4.9](../audits/literature/MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra).
Its inverse-entry characterization and block sum/product constructions apply to the actual inclusion \(B\subset U\).
For each of the finitely many entries of \(P\), select an inverse-entry realization, take the block diagonal sum of its denominators, and select its input and output coordinates by matrices over \(B\).
This gives (1), with a sign absorbed into \(B_1\); polynomial entries may instead be put in \(A\).
If no state is needed, one may adjoin \(Q=(1)\), \(B_1=0\), \(C=0\).
Every denominator is already known to be invertible in \(U\).
No abstract free-field evaluation or newly presumed scalar inverse is involved.

The [finite-trace affiliated interfaces](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness) and the [domain-aware rank calculus](../audits/literature/MSY23/Yin_U004.md#lemma-59-a-local-domain-aware-proof) are used throughout.
They supply closed products, generalized inverses, invertibility of injective square matrices, and invariance of rank under actual affiliated units.
For an affiliated matrix \(T\), let \(p_T\) be its kernel projection and \(T^\dagger\) its affiliated generalized inverse.
The identity \(T^\dagger T=1-p_T\) implies, for a bounded column \(x\) over \(B\),
\[
Tx=0\text{ in }U
\quad\Longrightarrow\quad
(1-p_T)x=0.
\]
The latter is a bounded-operator identity, so the vector \(x\delta_e\) belongs to the actual Hilbert kernel of \(T\), including its operator domain.
Conversely, if the finite-support vector \(x\delta_e\) belongs to that kernel, right invariance puts every right translate in the kernel.
The range of the bounded operator \(x\) therefore lies in that closed kernel, and \(Tx=0\) in \(U\).
This justifies identifying finite-support Hilbert-kernel vectors with algebraic affiliated annihilation without applying an unbounded operator to an unjustified vector.

### Proof of complete rational kernel localization

Actual affiliated triangular elimination gives
\[
\begin{pmatrix}I_m&-B_1Q^{-1}\\0&I_k\end{pmatrix}
L
\begin{pmatrix}I_n&0\\-Q^{-1}C&I_k\end{pmatrix}
=
\begin{pmatrix}P&0\\0&Q\end{pmatrix}.
\tag{11}
\]
Hence \(\operatorname{rk}_G L=k+\operatorname{rk}_G P\), and \(\nu(L)=\nu(P)\).
The [proved finite-propagation estimate](Yin_C_A0001_v1.md#matrix-boundary-estimate) applied to \(L\) gives
\[
\dim_{\mathbb C}W_F
\ge \nu(P)|F|-(n+k)|\partial_wF|,
\qquad
W_F=\ker L\cap\mathbb C[F]^{n+k}.
\tag{12}
\]
For \((x,y)\in W_F\), the group-ring equalities \(Ax+B_1y=0\) and \(Cx+Qy=0\) imply \(y=-Q^{-1}Cx\) and \(Px=0\) in \(U\).
If \(x=0\), then \(Qy=0\), so \(y=0\).
Thus coordinate projection \(W_F\to\mathbb C[F]^n\), \((x,y)\mapsto x\), is injective and lands in the Hilbert kernel by the preceding domain argument.
This proves the lower bound in (2).
Projection monotonicity and the constant diagonal of the invariant kernel projection prove the upper bound.

Let \(K_0\) be the Hilbert closure of all finite-support vectors in \(\ker P\).
It is right invariant and is contained in \(\ker P\).
For each \(F\), local projection dimension gives
\[
\dim_{\mathbb C}(\ker P\cap\mathbb C[F]^n)/|F|
\le\dim_G K_0\le\nu(P).
\]
Along a Følner sequence, (2) forces equality of the two invariant-subspace dimensions.
Faithfulness of the finite trace then gives \(K_0=\ker P\), proving (3).
In particular the same statement applies to every eigenkernel of \(P\) by replacing \(P\) with \(P-\lambda I\).

### Finite column descent

First, for \(0\ne a\in B\), noninjectivity on \(\ell^2(G)\) is equivalent to the existence of \(0\ne b\in B\) with \(ab=0\).
One implication is immediate and the other is the finite-propagation extraction.
Thus a domain hypothesis is exactly what certifies every nonzero scalar pivot as an actual unit of \(U\).

Suppose a current group-ring matrix \(D\) has nonzero Hilbert kernel.
Choose \(0\ne v\in B^q\) with \(Dv=0\), and choose an index \(j\) with \(v_j\ne0\).
If \(v_j\) is injective, it is a unit in \(U\), and
\[
D_j=-\sum_{i\ne j}D_i v_i v_j^{-1}.
\tag{13}
\]
Delete column \(j\) to obtain the actual group-ring matrix \(D'\).
Equation (13) gives \(D=D'H\) for an affiliated matrix \(H\), while the coordinate inclusion gives \(D'=DJ\).
Rank monotonicity in both directions yields \(\operatorname{rk}_G D'=\operatorname{rk}_G D\).
There is no need to assert that the intermediate coefficients of \(H\) lie in \(B\), and every matrix to which finite propagation is applied is still the literal column submatrix \(D'\) of \(A_0\).

If \(\operatorname{rk}_G A_0\) is noninteger, every such submatrix of the same rank has nonzero kernel.
Deleting columns with certified scalar units cannot continue to an injective matrix or to the zero-column matrix, since either has integer rank.
After finitely many steps a chosen nonzero coordinate \(x=v_j\) must be noninjective.
Scalar finite-support extraction supplies \(0\ne z\in B\) with \(xz=0\), proving the first descent assertion.
This is a finite existence procedure; no decidable test for equality or injectivity in an arbitrary presented group is asserted.

Under the domain assumption, every chosen nonzero coordinate is a unit, so deletion ends at an injective matrix with \(k\) columns, possibly \(k=0\).
Rank preservation gives \(\operatorname{rk}_G A_0=k\) and \(\nu(A_0)=n-k=d\).
At each deletion, embed its relation \(v\) in the original \(n\) coordinates by putting zero in all previously deleted positions.
Let \(V\) be the matrix of these \(d\) embedded relations, in deletion order.
Its rows indexed by the deleted positions form a triangular \(d\times d\) matrix with nonzero unit diagonal and therefore an invertible matrix over \(U\).
It follows that \(V\) has zero affiliated and Hilbert kernel.
Also \(A_0V=0\), so its closed range is contained in \(\ker A_0\) and has dimension \(d=\nu(A_0)\).
Faithful trace gives equality of these closed subspaces.
The polar-support identity then gives (8); the inverse of \(V^*V\) may be unbounded, while the closed total product is the bounded orthogonal projection.

Conversely, if \(0\ne a,b\in B\) and \(ab=0\), then \(0<\nu(a)<1\).
Positivity follows from the nonzero kernel vector \(b\), and strict inequality from \(a\ne0\) and faithfulness of the trace on its nonzero range support.
Thus even the scalar matrix violates integer kernel dimension.
This proves the amenable equivalence without invoking an Ore condition or assuming integer-valued rank during elimination.

### Complementary kernel mass for a rational obstruction

Let \(0\ne r\in\mathcal R\) be noninvertible.
In the finite affiliated algebra this means \(0<\nu(r)<1\).
Using (12) for its scalar realization, choose \(F\) as in (5) and a nonzero element \((x,y)\in W_F\).
The injectivity of coordinate projection gives \(x\ne0\), and \(rx=0\).
Equivalently \(p_r x=x\), so the closed range of \(x\) lies in \(\ker r\).
Consequently \(\operatorname{rk}_G x\le\alpha\), giving (4).
Apply the scalar finite-propagation estimate to \(x\) and choose \(F'\) as in (6).
Its finite-support kernel has positive dimension, yielding \(z\ne0\) and \(xz=0\).
Both witnesses lie in the original group ring and use only finite propagation of group-ring matrices, not propagation of an inverse.

### Passage beyond finite generation

Every group-ring matrix and every selected finite realization involves finitely many group elements.
Let \(H\) be the subgroup they generate.
For amenable \(G\), \(H\) is amenable, and the preceding argument applies to \(H\).
Decomposing \(\ell^2(G)\) over right cosets \(Ht\) gives copies of the left regular representation of \(H\).
The kernel projection of a matrix over \(\mathbb CH\) has the same canonical trace whether computed in \(H\) or \(G\).
The same decomposition shows that a denominator \(Q\) is injective over \(H\) if and only if it is injective over \(G\).
Its affiliated inverse is compatible with the inclusion by spectral calculus.
This transfers the qualitative statements and finite witnesses to arbitrary amenable \(G\).
For (9), all finitely many idempotents and differential matrices may likewise be placed in one finitely generated subgroup; exactness need not descend, because the kernel-density conclusion itself already transfers to \(G\).

### Proof of the homological interface

The proof uses complete finite-support kernel density, rather than assuming an undeclared exactness theorem for tensor products.
For a bounded idempotent \(E\in M_r(B)\), its range \(H_E=E\ell^2(G)^r\) is closed.
If \(q_E\) is its orthogonal range projection, then \(q_EE=E\) and \(Eq_E=q_E\).
Writing \(E=q_E+q_EE(1-q_E)\) and using traciality gives
\[
\dim_G H_E=(\operatorname{Tr}\otimes\tau)(q_E)
=(\operatorname{Tr}\otimes\tau)(E).
\tag{14}
\]

Represent each differential in (9) by a matrix \(D_i\) over \(B\), extending it by \(E_i\) on its source.
For \(i\ge1\), one can impose \(D_i=E_{i-1}D_iE_i\).
For \(D_0\), compose the map onto \(K_a\) with \(K_a\hookrightarrow B\), and impose \(D_0=D_0E_0\).
On \(H_i=E_i\ell^2(G)^{r_i}\), its kernel is precisely the Hilbert kernel of the group-ring matrix
\[
\begin{pmatrix}D_i\\I_{r_i}-E_i\end{pmatrix}.
\tag{15}
\]
Complete kernel density for (15) identifies this kernel with the closure of its algebraic kernel inside \(E_iB^{r_i}\).
Algebraic exactness in (9) makes that algebraic kernel the image of the next differential.
Since \(E_{i+1}B^{r_{i+1}}\) is dense in \(H_{i+1}\) and the differential is bounded, its image closure equals the image closure of the Hilbert differential.
At the left endpoint the same argument gives zero Hilbert kernel.
At the right endpoint, (3) for \(a\) identifies \(\overline{K_a}\) with \(\ker_{\ell^2}a\).
Thus (9) completes to a weakly exact finite Hilbert-module complex.

Polar decomposition gives dimension additivity for the kernel and closed range of each bounded differential.
Taking the alternating sum cancels all interior closed-range dimensions and gives
\[
\nu(a)=\sum_i(-1)^i\dim_G H_i.
\]
Combining this identity with (14) proves (10).
For torsion-free amenable \(G\), [BCM04](../audits/literature/BCM04/Yin_U001.md#amenable-projective-trace) identifies the canonical trace of each finitely generated projective module with its augmentation rank.
Each value in (10) is therefore an integer.
Since \(a\ne0\) gives \(0\le\nu(a)<1\), it follows that \(\nu(a)=0\).
If (9) is available for every nonzero \(a\), the scalar and then all-matrix conclusions follow.

## Scope and remaining obstruction

The rational localization estimate and its domain justification extend the earlier Claim; the known amenable domain/Atiyah equivalence is supplied with an explicit finite descent and a complete conditional Hilbert-kernel witness.
The homological calculation explains exactly how an established projective-trace theorem could close the remaining problem.
It does not prove that any nonzero principal annihilator has a finite projective resolution.
In fact, a torsion-free amenable counterexample to the domain conjecture would force its nonzero principal annihilator to fail this finite-resolution property.
Kernel density alone supplies neither that property nor an idempotent over \(B\) representing the kernel projection.
The inverse in (8), even when available, generally belongs only to the affiliated algebra and gives no such group-ring idempotent.
No limit of finite-window ranks is declared integer merely because every numerator is an ordinary integer.
No spectral-gap hypothesis, concrete-example search, or probabilistic independence of group generators is used.

## Revision operation, 2026-11-12

The mathematical scope is extended from a scalar-denominator Schur extraction to arbitrary actual rational-closure matrices, complete kernel localization, finite scalar obstruction descent and the finite-projective-resolution interface.
The fixed [first version](Yin_C_A0001_v1.md) and its [review](../audits/reviews/Yin_R_A0002_v1.md) retain their original statements and evidence.
The present argument reuses their finite-set estimate at the stated group-ring interface and requires a new review for its own extensions.
