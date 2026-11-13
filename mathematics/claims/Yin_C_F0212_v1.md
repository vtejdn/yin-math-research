---
author: Yin
---
# Bounded drifts of a free semicircular coordinate and Hilbert–Schmidt commutators

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite von Neumann algebra \(R\) with faithful normal probability trace \(\tau\), put \(H=L^2(R,\tau)\), and use inner products linear in their second variable.
Suppose \(X\) satisfies the [actual ACSY condition](../tasks/Yin_T_F0011_v1.md#contract).
Let \(\delta_i\) be its unique starred coordinate derivation on \(\mathcal P=\mathbb C\langle X,X^*\rangle\), with actual vacuum \(\xi_i=\delta_i^*(1\otimes1)\).
Assume all the [polynomial column costs](Yin_C_F0208_v1.md#statement) are finite for both \(X\) and its adjoint tuple \(X^*\).
Thus, for each canonical right slice \(E_{i,0}=(\mathrm{id}\otimes\tau)\delta_i\) on either tuple, there is a finite \(c\) such that
\[
       \sum_k\|E_{i,0}p_k\|_2^2\le c^2\left\|\sum_k p_k^*p_k\right\|
       \qquad (p_k\in\mathcal P).
\]
Write \(E_i=\overline{E_{i,0}}\) for the original tuple \(X\).
The hypotheses give \(R\Omega\subset\operatorname{Dom}E_i\cap\operatorname{Dom}E_i^*\), as verified below.

In the tracial free product \(\widehat R=R*W^*(s)\) with a standard semicircular \(s=s^*\), take any \(B=B^*\in R\) and put \(T=s+B,\ Y=(X,T)\).
Then \(W^*(Y)=\widehat R\).
The following are equivalent.

1. \(Y\) satisfies \(\mathsf A\) on its original represented star-polynomial core in \(L^2(\widehat R)\).
2. \(Y\) satisfies \(\mathsf S\), with generator-first dual commutators on all bounded vectors and with all these vectors in both the dual and actual adjoint domains.
3. For every \(i\), the map
   \[
             K_i a=E_i(Ba)-B E_i(a),\qquad a\in R,
             \tag{1}
   \]
   extends to a Hilbert–Schmidt operator on \(H\).

There is no derivation-domain assumption on \(B\).
Under these conditions the original canonical duals and their actual adjoints have all bounded vectors in their domains, \(\mathsf F(Y)\) holds, and all column costs for \(Y\) and \(Y^*\) are finite.

Let \(P_\Omega h=\langle\Omega,h\rangle\Omega\).
Use the unitary \(\Theta:H\otimes_2H\to S_2(H)\) defined by \(\Theta(a\otimes b)=aP_\Omega b\), and the isometry \(J_s:H\otimes_2H\to L^2(\widehat R)\) given by \(J_s(a\otimes b)=a s b\) on bounded \(a,b\in R\).
Its range is the one-\(s\) Wick space.
Write \(\gamma^\star\) for the antilinear componentwise adjoint sending \(a\otimes b\) to \(a^*\otimes b^*\), and \(\gamma^\dagger\) for its flip.
Define \(\beta_i=-\Theta^{-1}K_i\) in case 3.
The actual vacua and their norms are
\[
 \xi_i(Y)=\xi_i+J_s(\beta_i^\star),\qquad
 \|\xi_i(Y)\|_2^2=\|\xi_i\|_2^2+\|K_i\|_{\rm HS}^2,\qquad
 \xi_{d+1}(Y)=s .
 \tag{2}
\]
In particular neither a bounded nonlinear drift of arbitrarily high degree nor an arbitrary bounded measurable drift in this class gives a counterexample to the normal implication.

## Argument

### The canonical slices on the base and its free extensions

The right slice for \(X^*\) is the right slice of \(\delta_i^\#(a)=(\delta_i(a^*))^\dagger\) by the [adjoint-tuple rule](Yin_C_F0073_v1.md#statement) and the [forced normal derivatives](Yin_C_F0076_v1.md#statement).
The two column bounds for a single test thus bound both the original right slice and the reversed one on the operator unit ball of \(\mathcal P\).
Equivalently the original right and left slices are bounded there, since tracial adjoint conjugates the left slice to the reversed right slice.
The [canonical domain theorem](Yin_C_F0072_v1.md#statement) gives the stated full domains of \(E_i,E_i^*\) and operator-norm-to-Hilbert bounds on their bounded-vector restrictions.
Write \(\xi=\xi_i,\ \delta=\delta_i,\ E=E_i\) for a fixed old coordinate.

For a free extension by another tracial factor, extend the old derivation to the algebraic free-product core by killing that factor.
Its vacuum remains \(\xi\) by the [centered-word calculation](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor).
The free-product Hilbert space has the [reduced-word decomposition](../audits/literature/Voi98/Yin_U005.md#voi98-u005) used in the [free-factor slice formula](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
In the notation of that formula \(w\) ranges over \(1\) and an orthonormal family of reduced words ending with a centered letter of the new factor.
For an algebraic test \(p=\sum_w w b_w\), its free slice \(L_0\) equals \(\sum_w w E(b_w)\) and \(\mathbb E_R(p^*p)=\sum_w b_w^*b_w\).
The \(b_w\) are old core polynomials, and these are finite sums for algebraic inputs with bases obtained from the factor cores.
For a finite column of tests \(p_j\) with coefficients \(b_{jw}\), it follows that
\[
 \sum_j\|L_0p_j\|_2^2
 =\sum_{j,w}\|E b_{jw}\|_2^2
 \le c_i(X)^2 \left\|\mathbb E_R\Big(\sum_jp_j^*p_j\Big)\right\|
 \le c_i(X)^2\left\|\sum_jp_j^*p_j\right\| .
 \tag{3}
\]
The old tests give the reverse inequality between optimal column costs.
The calculation works for the adjoint tuple as well.
Both normalized free slices are therefore bounded on the operator unit ball, so the canonical \(L=\overline{L_0}\) and \(L^*\) have full bounded-vector domains with bounded restrictions by C_F0072.
The free reference used below is \((X,s)\); the same facts apply when its other factor consists of several free generators.
The algebra generated by \(X,T\) as a von Neumann algebra contains \(R\), then \(s=T-B\), so it is \(\widehat R\).

### Compression of the commutator with a bounded drift

Let \(e_R:L^2(\widehat R)\to H\) be the conditional expectation projection, with \(H\) identified with its embedded subspace.
Suppose (1) has a Hilbert–Schmidt extension \(K\).
For \(a\in R\), the free slice \(L\) acts as \(E\) by the core formula and uniformly bounded strong polynomial approximation in \(R\).
Indeed the images of such an approximating net have weak cluster points by the operator-norm-to-Hilbert bound, and weak closedness of the graphs identifies the unique limits.
Then
\[
                [L,B]v=K e_Rv\qquad(v\in\widehat R).
                \tag{4}
\]
To see this for \(w b\) with \(w\ne1\), first use \(B'\in\mathcal P\) in place of \(B\).
Multiplying the leftmost old letter of \(w\), or adjoining an old letter if \(w\) starts in the new factor, changes only its prefix.
Cancellation can remove an initial old letter but leaves the centered new-factor letter at the end.
Thus \(B'w\) is a finite scalar combination of words in the same nonempty family and every term retains the terminal coefficient \(b\) in \(B'w b\).
Formula (3) for the slice gives \([L,B']w b=0\).
Choose uniformly bounded selfadjoint \(B'\) converging strongly to \(B\) from \(\mathcal P\) by [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001).
The closed graph and bounded restriction give weak convergence of \(L(B'w b)\) to \(L(Bw b)\), proving the same vanishing.
This and the \(w=1\) calculation prove (4) on the polynomial core.
Uniformly bounded strong approximation of every \(v\in\widehat R\), with the same graph argument for \(Lv\) and \(L(Bv)\), proves (4) on all bounded vectors.
The proof applies to any other free factor with the same old right and reversed slice bounds.

### The forced one-noise vacuum component

Assume \(\mathsf A(Y)\), and write \(\zeta\) for its \(i\)-th vacuum.
On \(\mathcal P\) its derivation agrees with \(\delta\) included in the larger coarse space.
Indeed the normal law forces the same unstarred values and the same marginal phase tensors on the starred generators; the Leibniz rule determines all polynomial values.
Consequently \(e_R\zeta=\xi\).
The map \(J_s\) is isometric, since the scalar product of \(u s v\) with \(a s b\) is \(\tau(u^*a)\tau(v^*b)\) by freeness and the normalization \(\tau(s^2)=1\).
Let \(J_s\kappa\) be the orthogonal projection of \(\zeta\) onto this one-noise space.

For \(u,v\in\mathcal P\), expand the actual vacuum pairing on \(uTv\).
The two endpoint Leibniz terms with one \(s\) vanish by centering and freeness, and the middle derivative is zero.
Replacing \(s+B\) with \(B\) in those two terms gives
\[
 \langle\kappa,u\otimes v\rangle
 =(\tau\otimes\tau)\big((\delta u)Bv+uB(\delta v)\big)
                         -\langle\xi,uBv\rangle
 =-\langle u^*, K_i v\rangle .
 \tag{5}
\]
The first equality uses \(\langle\zeta,uBv\rangle=\langle\xi,uBv\rangle\).
For the second, first insert a selfadjoint polynomial \(B'\) in the right-hand expression preceding it.
The old derivation rule gives exactly \(-(\tau\otimes\tau)(u(\delta B')v)=-\langle u^*,[E,B']v\rangle\).
For the last equality the tensor unitary satisfies \(\langle u^*,\Theta(a\otimes b)v\rangle=\tau(ua)\tau(bv)\), first on bounded factors and then by Hilbert density.
Pass to \(B\) using the same bounded strong approximation.
The endpoint coarse multipliers and \(uB'v\) converge strongly on the relevant fixed vectors, and \(\langle u^*,E(B'v)\rangle=\langle E^*u^*,B'v\rangle\) converges because \(u^*\) is in the full adjoint domain.
This proves (5) without applying \(\delta\) to \(B\).

For every tensor \(k\), \(\langle k,u\otimes v\rangle=\langle u^*,\Theta(k^\star)v\rangle\), by tracial cyclicity and the convention above.
Thus on core vectors \(K_i=-\Theta(\kappa^\star)\).
On arbitrary bounded \(v\) approximate by uniformly bounded core elements and use the full adjoint pairing against each \(u^*\) and boundedness of \(B\), or apply weak graph convergence separately to \(E(Bv)\) and \(Ev\).
Hence (1) has the required Hilbert–Schmidt extension and \(\kappa=\beta_i^\star\).
This establishes necessity; exclusion of further vacuum components follows from sufficiency.

### A degree-zero insertion over a noncommutative base

For any \(\beta\in H\otimes_2 H\) define the reference derivation \(d_\beta\) on the algebraic unital free product \(R*\mathbb C[s]\) by \(d_\beta R=0,\ d_\beta s=\beta\).
This algebra embeds in the tracial free product by the reduced-word representation, so the outer rule defines a represented Hilbert-tensor derivation.
Let \(F_{\beta,0}=(\mathrm{id}\otimes\tau)d_\beta\) on this dense core.
We prove the actual vacuum and bounded-vector estimates
\[
 d_\beta^*(1\otimes1)=J_s(\beta^\star),\qquad
 \|F_\beta a\|_2\le2\|\beta\|_2\|a\|,\qquad
 \|F_\beta^*a\|_2\le\|\beta\|_2\|a\|,\qquad a\in\widehat R,
 \tag{6}
\]
where \(F_\beta=\overline{F_{\beta,0}}\).
The proof gives the base of the [relative Wick cut estimate](Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate) directly for this \(R\).

In the relative Wick decomposition the degree-\(n\) Hilbert space is \(H^{\otimes(n+1)}\).
For completeness, on this direct sum let \(R\) multiply the first tensor factor on the left, and let creation prepend \(1\), with annihilation its adjoint contracting the leading factor against \(1\) and vanishing on degree zero.
Their sum is the semicircular field.
The vacuum moments of \(R\) and this field agree with those of \(R,s\), since the vacuum expansion pairs each annihilation with the most recent creation, closing a pair by the scalar trace of the intervening base product.
This is the [free semicircular mixed-moment rule](../audits/literature/NS06/Yin_U004.md#ns06-u004), including the indicated product order in the noncommutative base.
The Wick polynomials \(W(a_0,\ldots,a_n)\), \(a_j\in R\), sending the vacuum to the tensor \(a_0\otimes\cdots\otimes a_n\) are obtained recursively by subtracting that leading contraction.
These tensors are total and their scalar products are the products of their factor scalar products, so the representation agrees unitarily with the tracial Hilbert representation.
Writing \(\partial s=1\otimes1,\ \partial R=0\), the recurrence gives
\[
 \partial W(a_0,\ldots,a_n)
  =\sum_{j=1}^n W(a_0,\ldots,a_{j-1})
                 \otimes W(a_j,\ldots,a_n).
 \tag{7}
\]
In detail, the recurrence for \(n\ge2\) is \(W(a_0,\ldots,a_n)=a_0sW(a_1,\ldots,a_n)-\tau(a_1)W(a_0a_2,a_3,\ldots,a_n)\).
Differentiating the first \(s\) gives the first cut, and applying the recurrence to the differentiated suffix gives the subsequent cuts, canceling the differentiated contraction.
Degree one is \(W(a,b)=asb\), proving the induction seed.
No commutation of base coefficients enters.

First take finite bounded tensors for \(\beta\).
The vacuum trace of \(d_\beta p\) equals \(\langle\beta^\star,\partial p\rangle\).
Only the degree-one term of \(p\) contributes, by (7) and orthogonality, and its single cut is the inverse of \(J_s\).
This proves the first identity in (6), also for arbitrary \(\beta\) by Hilbert approximation on each fixed core test.
For the right slice, a suffix with positive relative degree has zero trace after multiplication by a base coefficient.
Deleting the last \(s\) in (7) therefore gives the only contributing cut.
The map \(C:p\mapsto\) this last cut is an isometry on all positive degrees into \(L^2(\widehat R)\otimes H\), simply reassociating the last base factor, and vanishes on degree zero.
For a bounded orthonormal Hilbert basis \(b_j\) of \(H\), write \(Cp=\sum_j x_j\otimes b_j,\ \beta=\sum_j a_j\otimes b_j^*\).
Then \(F_{\beta,0}p=\sum_j x_j a_j\) in \(L^1\), since \(\tau(b_j^*b_k)=\delta_{jk}\).
The basis exists by orthogonalizing a countable dense collection of bounded elements.
The product series converges by Cauchy--Schwarz and tracial Hölder and has \(L^1\) norm at most \(\|p\|_2\|\beta\|_2\).
Approximation by finite bounded coefficient tensors justifies the identity for completed \(\beta\), since the insertion into the finite cut expression of a core \(p\) is continuous into the coarse Hilbert space.
Pairing this \(L^1\) bound against bounded \(a\) proves \(a\in\operatorname{Dom}F_{\beta,0}^*\) with the last bound in (6).

The reversed derivation has coefficient \(\beta^\dagger\).
Expanding \(d_\beta(a^*p)\) and using the actual vacuum gives on the original core \(F_{\beta,0}^*a=aJ_s(\beta^\star)-F_{\beta^\dagger,0}a\), the [slice adjoint identity](Yin_C_F0145_v1.md#3-the-actual-adjoints-and-the-reverse-bound).
The same identity for \(\beta^\dagger\) and the just proved adjoint bound give \(\|F_{\beta,0}a\|_2\le2\|\beta\|_2\|a\|\) on the core.
Its adjoint is densely defined, and bounded strong approximation and weak closedness extend this estimate to the original closure on every bounded input.
This proves (6).
Its core commutators are zero with \(R\), and \([F_{\beta,0},s]=\widehat\Theta(\beta)\), with \(\widehat\Theta\) the tensor-to-Hilbert–Schmidt identification on \(L^2(\widehat R)\).
Bounded core approximation, (6), and the closed graph give the identities on all bounded inputs.
Here \(\widehat\Theta(\beta)=\Theta(\beta)e_R\) for a tensor from \(H\otimes H\), since the inner vectors specifying the corresponding rank-one operators lie in \(H\).
For \(\beta=1\otimes1\) this is the vacuum projection \(P_{\widehat\Omega}\) of the full Hilbert space.

### Correction and the exact vacuum

Assume condition 3 and use \(\beta=\beta_i\) for the fixed old coordinate.
On the free reference algebra take the densely defined operator \(Q_i=(L+F_\beta)|_{\widehat R\Omega}\).
Both summands have full bounded-vector and adjoint domains.
Pairing their sum with those common bounded test vectors puts every bounded vector in \(\operatorname{Dom}Q_i^*\) and gives \(Q_i^*a=L^*a+F_\beta^*a\) there.
In particular \(Q_i\) is closable; no identification of the closure of an operator sum is needed.
The free reference commutators of \(L\) with \(X_j\) are \(\delta_{ij}P_{\widehat\Omega}\), and \([L,s]=0\), first by the core rule and then by the bounded graph argument.
The correction commutes with \(R\), and (4) and (6) give
\[
        [Q_i,T]=K_i e_R+\Theta(\beta_i)e_R=0 .
\]
The reference \(F_{1\otimes1}\) supplies the last coordinate with commutator \(P_{\widehat\Omega}\) for \(s+B\) and zero commutators on \(R\).
Negating these operators gives \(\mathsf S(Y)\), which implies \(\mathsf A(Y)\) by the [normal strong-to-vacuum theorem](Yin_C_F0070_v1.md#statement).
Every supplied operator is normalized at the unit.
The same theorem identifies its actual target vacuum as the operator-first adjoint at the unit; the old free lift has adjoint vacuum \(\xi\), and (6) gives the correction and last-coordinate vacua.
This proves (2) including absence of any further higher-noise component.
The [normal canonical comparison](Yin_C_F0075_v1.md#statement) gives the full original canonical domain assertions.

### Finite columns on the drifted tuple

Consider \(Y\) satisfying these equivalent conditions and adjoin two independent free Haar unitaries \(U,V\) free from \(\widehat R\).
The enlarged shear has \(\mathsf A\) with unchanged old vacua by [C_F0208](Yin_C_F0208_v1.md#statement).
View it as the same shear with old tuple \(X'=(X,U,V)\), base \(R'=W^*(X,U,V)\), and \(s\) free from \(R'\).
Formula (3) gives both oriented old column costs at the \(X\)-coordinates of \(X'\).
Each new Haar coordinate also has finite costs in both directions, since the scalar right slices for this Haar unitary and its adjoint are bounded on the abelian unitary factor by the [scalar normal estimate](Yin_C_F0055_v1.md#statement), using their [actual Haar vacua](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
For a bounded map from an abelian \(C^*\)-algebra to Hilbert space the [complex little Grothendieck inequality](../audits/literature/Pis12/Yin_U001.md#pis12-u001) gives the finite-column bound, since the sum of the squared absolute values is the column norm squared there.
Apply (3) to those factors with the other free factors grouped together.
Thus \(X'\) satisfies all base hypotheses.
The equivalence already proved, applied to the enlarged shear whose \(\mathsf A\) was just verified, gives \(\mathsf S(Y,U,V)\).
The [two-Haar lower bound](Yin_C_F0208_v1.md#statement) then gives finite \(c_j(Y)\) for every coordinate, since the normalized strong duals restrict boundedly from the algebra to its Hilbert space by canonical comparison and the canonical bounds.
For \(Y^*\), repeat the same argument with the adjoint base \(X^*\) and the same \(B,s\), using actual vacuum invariance under adjoints and the interchanged oriented column hypotheses.
This gives all stated column bounds.

## Scope

The criterion applies to arbitrary bounded selfadjoint elements of the old algebra, including higher Wick polynomials and bounded functions with no finite chaos expansion.
The old tuple here is assumed to have the two oriented column bounds.
The converse from bare \(\mathsf F\) and the unrestricted implication for arbitrary correlated normal tuples remain separate questions.

## Assessment history

### Decision free-shear-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:59 |
| status | open |
| reason | A complete candidate gives the Hilbert–Schmidt criterion for arbitrary bounded old-algebra drifts, exact vacuum cost, both actual domains and persistence of finite oriented column costs. Independent review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full intrinsic equivalence, actual domains, one-noise formula for the vacuum cost and finite column costs in both orientations. |
| argument | [Argument](#argument) | Base column lifts, compression of the drift commutator, intrinsic mixed test, arbitrary-base insertion and construction, and the enlarged-base argument for columns. |
| dependency | [Adjoint tuple](Yin_C_F0073_v1.md#statement) | Reversed derivation, tracial involution and actual vacua of the adjoint tuple. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Unique starred values under the actual ACSY premise, including the old coordinates inside the shear. |
| dependency | [Canonical domain theorem](Yin_C_F0072_v1.md#statement) | Two bounded contraction orientations give the original all-bounded-vector closure and adjoint domains. |
| dependency | [Free vacuum preservation](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Actual old derivation and vacuum on the free-product core by zero extension to the new factor. |
| dependency | [Free-product representation](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Pointed reduced-word sectors, factor actions and scalar products of centered tensors. |
| dependency | [Reduced-word slice](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Suffix expansion and conditional expectation, applied to finite columns, and the normalized actual Haar vacua. |
| dependency | [Bounded strong approximation](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded polynomial approximations from the generating core in the tracial representations. |
| dependency | [Semicircular mixed moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Free semicircular pairings with arbitrary base coefficients for the relative Wick realization. |
| dependency | [Suffix cut](Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate) | Orthogonal last-cut and noncommutative product estimate, proved here for a general tracial coefficient base. |
| dependency | [Adjoint identity](Yin_C_F0145_v1.md#3-the-actual-adjoints-and-the-reverse-bound) | Core adjoint of insertion, flipped contraction and Riesz reverse estimate after verification of the arbitrary-base cut. |
| dependency | [Strong-to-vacuum theorem](Yin_C_F0070_v1.md#statement) | Normalized strong duals provide the actual target vacuum as their operator-first adjoint value at the unit. |
| dependency | [Normal canonical comparison](Yin_C_F0075_v1.md#statement) | Full original canonical bounded-vector domains under the normal strong condition. |
| dependency | [Two-Haar criterion](Yin_C_F0208_v1.md#statement) | Preservation of ACSY on the enlargement and its lower bound for each old column cost from the extended dual norm. |
| dependency | [Scalar normal estimate](Yin_C_F0055_v1.md#statement) | Bounded right slices on each scalar Haar factor in both orientations. |
| dependency | [Abelian Grothendieck estimate](../audits/literature/Pis12/Yin_U001.md#pis12-u001) | Finite-column bound for the bounded scalar Haar slice on its abelian factor. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:05 |
| status | proved |
| reason | Adopt the Hilbert–Schmidt drift criterion and exact vacua on the indicated base class after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full intrinsic equivalence, actual domains, one-noise formula for the vacuum cost and finite column costs in both orientations. |
| argument | [Argument](#argument) | Base column lifts, compression of the drift commutator, intrinsic mixed test, arbitrary-base insertion and construction, and the enlarged-base argument for columns. |
| dependency | [Adjoint tuple](Yin_C_F0073_v1.md#statement) | Reversed derivation, tracial involution and actual vacua of the adjoint tuple. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Unique starred values under the actual ACSY premise, including the old coordinates inside the shear. |
| dependency | [Canonical domain theorem](Yin_C_F0072_v1.md#statement) | Two bounded contraction orientations give the original all-bounded-vector closure and adjoint domains. |
| dependency | [Free vacuum preservation](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Actual old derivation and vacuum on the free-product core by zero extension to the new factor. |
| dependency | [Free-product representation](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Pointed reduced-word sectors, factor actions and scalar products of centered tensors. |
| dependency | [Reduced-word slice](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Suffix expansion and conditional expectation, applied to finite columns, and the normalized actual Haar vacua. |
| dependency | [Bounded strong approximation](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded polynomial approximations from the generating core in the tracial representations. |
| dependency | [Semicircular mixed moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Free semicircular pairings with arbitrary base coefficients for the relative Wick realization. |
| dependency | [Suffix cut](Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate) | Orthogonal last-cut and noncommutative product estimate, proved here for a general tracial coefficient base. |
| dependency | [Adjoint identity](Yin_C_F0145_v1.md#3-the-actual-adjoints-and-the-reverse-bound) | Core adjoint of insertion, flipped contraction and Riesz reverse estimate after verification of the arbitrary-base cut. |
| dependency | [Strong-to-vacuum theorem](Yin_C_F0070_v1.md#statement) | Normalized strong duals provide the actual target vacuum as their operator-first adjoint value at the unit. |
| dependency | [Normal canonical comparison](Yin_C_F0075_v1.md#statement) | Full original canonical bounded-vector domains under the normal strong condition. |
| dependency | [Two-Haar criterion](Yin_C_F0208_v1.md#statement) | Preservation of ACSY on the enlargement and its lower bound for each old column cost from the extended dual norm. |
| dependency | [Scalar normal estimate](Yin_C_F0055_v1.md#statement) | Bounded right slices on each scalar Haar factor in both orientations. |
| dependency | [Abelian Grothendieck estimate](../audits/literature/Pis12/Yin_U001.md#pis12-u001) | Finite-column bound for the bounded scalar Haar slice on its abelian factor. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0220_v1.md#whole-proof-finding) | All base and extension interfaces, arbitrary-base Wick insertion, actual domains and both column orientations. |
