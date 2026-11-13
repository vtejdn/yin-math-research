---
author: Yin
---
# Finite word tests for actual conjugate variables and bounded full-domain duals

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be a bounded generating tuple of a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, \(H=L^2(M,\tau)\) and \(\Omega=1\).
Inner products are linear in the second argument.
Let \(W_n\) be the space of formal star polynomials of degree at most \(n\) and \(V_n=W_n(X)\subset M\subset H\) its represented image.
Write \(Q_n\) for the Hilbert projection onto \(V_n\).
For words use independent formal letters \(x_j,y_j\) evaluated at \(X_j,X_j^*\).
Write \(d_{x_j},d_{y_j}\) for the formal outer word cuts, evaluated on each tensor leg after cutting.
No assumption on the ideal of represented relations is imposed.

For each \(i\) define \(\alpha_{i,n}\) as the smallest \(A\ge0\) satisfying, for all \(p\in W_n\),
\[
 |(\tau\otimes\tau)d_{x_i}p|
 \le A\left(\|p(X)\|_2^2+\sum_j\|d_{y_j}p\|_{H\otimes_2H}^2\right)^{1/2}.                 \tag{1}
\]
Use \(+\infty\) for an unsatisfiable bound.
The increasing limit \(\alpha_i\) is finite precisely when the \(i\)-th actual ACSY coordinate derivation exists on the full represented star algebra.
In that case \(\alpha_i\) is the least value of \((\|\xi_i\|_2^2+\sum_j\|\delta_iX_j^*\|_2^2)^{1/2}\) over that coordinate's witnesses, and the minimum is attained.

Independently let \(\beta_{i,n}\) be the infimum of the norms from \((V_{n+1},\|\cdot\|_M)\) to \(H\) of linear maps \(T:V_{n+1}\to V_{n+1}\) satisfying
\[
 \langle h,T(X_jp)\rangle-\langle X_j^*h,Tp\rangle
   =\delta_{ij}\tau(p)\langle h,\Omega\rangle
 \quad(p,h\in V_n,\ 1\le j\le d).                            \tag{2}
\]
An empty feasible set has infimum \(+\infty\).
The increasing limit \(\beta_i\) is exactly the infimum of the norms \(M\to H\) of bounded full-domain witnesses \(E\) for \([E,X_j]=\delta_{ij}P_\Omega\).
If finite, it is attained by an ultraweak-to-weak continuous witness.
The maps in (2) and the minimizing global witness have unrestricted value at \(1\).
The sign for the Task's generator-first dual is \(D=-E\).

Both tests are determined by the joint star moments.
For fixed \(n\), (1) uses only finitely many moments.
In (2) the norm of an input polynomial is its actual operator norm.
An exact iterated finite-moment formula for \(\beta_i\) is given below.

For normal tuples \(\mathsf S(X)\) holds exactly when all the limits \(\beta_i(X)\) and \(\beta_i(X^*)\) are finite.
More generally, if a nonconstant affine combination \(Y=a_0+\sum_j a_jX_j\) is normal with some \(a_k\ne0\), then \(\mathsf F(X)\) holds exactly when all \(\beta_i(X)\) are finite.
For arbitrary tuples finiteness of all \(\beta_i\) gives \(\mathsf F\).

## Argument

### Actual derivations on the represented quotient

This part extends the word-cut and Riesz argument used for a free target star algebra in [D_F0005](../drafts/Yin_D_F0005.md#an-exact-target-only-functional-reduction).
Given vectors \(K_j\in H\otimes_2 H\), use the word rule on the formal algebra with \(\delta x_j=\delta_{ij}1\otimes1\), \(\delta y_j=K_j\) and outer actions through evaluation.
Denote its values by \(\widetilde\delta p\).
Write \(K^\sharp\) for componentwise conjugate adjoint, taking \(u\otimes v\) to \(u^*\otimes v^*\).
For bounded \(a,b\), tracial cyclicity gives \(\langle 1\otimes1,a K b\rangle=\langle K^\sharp,a\otimes b\rangle\), first on finite tensors and then by Hilbert continuity.
Thus
\[
 \langle1\otimes1,\widetilde\delta p\rangle
 =(\tau\otimes\tau)d_{x_i}p+\sum_j\langle K_j^\sharp,d_{y_j}p\rangle.       \tag{3}
\]
An actual witness with \(\xi_i=\delta_i^*(1\otimes1)\) gives (1) by Cauchy--Schwarz.

Conversely, a finite \(\alpha_i\) defines a bounded linear functional on the image of \(p\mapsto(p(X),(d_{y_j}p)_j)\), of norm \(\alpha_i\).
Riesz representation on the closure of the image gives \((\xi,(L_j)_j)\) of that norm.
Take \(K_j=-L_j^\sharp\) in (3).
Then \(\langle1\otimes1,\widetilde\delta p\rangle=\langle\xi,p(X)\rangle\) on every formal polynomial.
For a represented relation \(r(X)=0\), apply this scalar identity to \(u r v\) for all formal \(u,v\).
The outer derivation rule leaves only \(u(X)(\widetilde\delta r)v(X)\) on the left, and the right side is zero.
Hence \(\widetilde\delta r\) is orthogonal to all \(u(X)^*\otimes v(X)^*\).
These tensors have dense span, so \(\widetilde\delta r=0\).
This proves descent through every relation, and (3) then puts the vacuum tensor in the actual Hilbert adjoint domain with value \(\xi\).
The Riesz norm and the necessary inequality give the claimed attained minimum.

### The Hilbert values and the represented norm

Equation (2) is a finite system on the represented spaces.
If \(m\ge n\), restriction to \(V_{n+1}\) followed by \(Q_{n+1}\) preserves the tests at level \(n\), because both \(h\) and \(X_j^*h\) belong to \(V_{n+1}\).
This proves monotonicity.
Likewise a global bounded solution yields a feasible map of no greater norm at each level.

Suppose \(\beta_i<\infty\).
At every level the minimum is attained by finite dimensionality, closedness of the constraints and compactness of bounded sets of such linear maps.
Choose minimizers \(T_n\).
For every represented word \(p\) the tail \(T_np\) is bounded by \(\beta_i\|p\|_M\).
Diagonal extraction over the countable words gives weakly convergent values on all of them, since \(H\) is separable by density of the star algebra in the tracial Hilbert space.
Taking finite linear combinations gives a well-defined linear \(T\) on the represented star algebra with the same norm bound, including all its linear relations.
Testing (2) against each fixed polynomial \(h\) gives the commutator there by Hilbert density.
Extension in operator norm yields \(T:C^*(X)\to H\) with the same bound and the commutators on \(C^*(X)\).

Put \(B=C^*(X)\) and let \(\pi:B^{**}\to M\) be the normal extension of its represented inclusion.
The [universal-bidual and central-summand theorem](../audits/literature/Bla06/Yin_U002.md#bla06-u002) gives a central projection \(e\) with \(eB^{**}\simeq M\) normally under \(\pi\).
Write \(j:M\to eB^{**}\) for its inverse and \(\iota:B\to B^{**}\) for the canonical inclusion.
Then \(j(X_k a)=\iota(X_k)j(a)\).
The normal extension of \(\tau|_B\) is \(\tau\pi\) by uniqueness.
Since \(H\) is reflexive, \(T^{**}:B^{**}\to H\) is weak-star-to-weak continuous.
The identity on \(B\) consequently extends by weak-star density to
\[
 T^{**}(\iota(X_k)b)-X_kT^{**}(b)=\delta_{ik}\tau(\pi b)\Omega
 \qquad(b\in B^{**}).
\]
Thus \(E=T^{**}j\) is a full-domain witness of norm at most \(\beta_i\).
This transfer only asserts existence of a normal witness on \(M\).
The central summand can discard a singular part of the initially chosen map on \(B\), so no pointwise extension of that map is used.
Combined with the opposite inequality this proves attainment with exact norm, also for a zero optimum.

### Finite moments for the input norm

For \(p\in V_{n+1}\) put \(N_l(p)=\|L_p:V_l\to V_{l+n+1}\|_{2\to2}\), \(l\ge0\).
This is a norm since \(\Omega\in V_l\).
The norms increase to \(\|p\|_M\) by density of the polynomial vectors in \(H\) and faithfulness of the left representation.
For fixed \(n\) this convergence is uniform on the compact operator-norm unit sphere of \(V_{n+1}\) by monotonicity and continuity, equivalently by taking a finite net and using \(|N_l(p)-N_l(q)|\le\|p-q\|_M\).
Define \(\beta_{i,n,l}\) by (2) with \(N_l\) as its input norm.
For every \(\varepsilon>0\) smaller than one and all sufficiently large \(l\),
\[
 \beta_{i,n}\le \beta_{i,n,l}\le(1-\varepsilon)^{-1}\beta_{i,n}.
\]
If the system is infeasible it is infeasible for each input norm.
Therefore \(\beta_i=\sup_n\inf_l\beta_{i,n,l}\).
The Gram matrices for the words, for multiplication on these finite spaces, and for (1) and (2) use only finite joint star moments at each \(n,l\).
Their null spaces encode the actual represented quotients by faithfulness.
The formula takes the inner limit for fixed \(n\).

### Bare and strong systems

On a tuple with the displayed normal combination, let \(E_i\) be any bare system with the above sign.
Then \([E_i,Y]=a_iP_\Omega\).
If \(a_i\ne0\), [C_F0069 Part A](Yin_C_F0069_v1.md#statement) applied to \(E_i/a_i\) gives boundedness from \(M\) to \(H\).
For \(a_i=0\), both \(E_k/a_k+E_i\) and \(E_k/a_k\) have commutator \(P_\Omega\) with \(Y\), so their difference is bounded as well.
This proves the claimed equivalence for bare systems, without any normality premise on the other coordinates.
For a normal tuple also apply this argument to the adjoint tuple and use [C_F0075 Part 2](Yin_C_F0075_v1.md#statement).
If some coordinate is scalar, a bare system and a bounded system are both excluded by testing that coordinate's commutator on \(1\), for the original and adjoint tuple alike.
For general tuples without automatic continuity, a divergent \(\beta_i\) excludes bounded witnesses only.

In particular, on arbitrary correlated normal tuples the remaining implication asks whether simultaneous finiteness of the \(\alpha_i\) forces simultaneous finiteness of the \(\beta_i\) for the tuple and its adjoint.
The test is at the full original class, and supplies no uniform bound in \(n\) from (1).
It neither proves this implication nor supplies a separating law.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T09:35 |
| status | open |
| reason | Complete candidate for joint moment tests for the two norm conditions, with descent through represented relations, central-summand transfer and the stated limits for bare duals. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact two monotone limits and minima, finite moment realizations, bare witnesses with a normal affine combination and the full normal strong criterion. |
| argument | [Argument](#argument) | Word-cut Riesz test with descent, finite weak commutator tests, transfer through the represented summand, norm approximation and applicability. |
| dependency | [Represented summand](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Extension of the nondegenerate representation of the generated C-star algebra to its bidual with normal central summand. |
| dependency | [Automatic continuity](Yin_C_F0069_v1.md#statement) | Part A for an algebraic full-domain map with rank-one commutator with a normal element. |
| dependency | [Adjoint-tuple characterization](Yin_C_F0075_v1.md#statement) | Part 2 for the strong system on an arbitrary normal tuple. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T09:41 |
| status | proved |
| reason | Adopt the two optimal word tests and their stated implications following an independent review of the entire proof and the directly used interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact two monotone limits and minima, finite moment realizations, bare witnesses with a normal affine combination and the full normal strong criterion. |
| argument | [Argument](#argument) | Word-cut Riesz test with descent, finite weak commutator tests, transfer through the represented summand, norm approximation and applicability. |
| dependency | [Represented summand](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Extension of the nondegenerate representation of the generated C-star algebra to its bidual with normal central summand. |
| dependency | [Automatic continuity](Yin_C_F0069_v1.md#statement) | Part A for an algebraic full-domain map with rank-one commutator with a normal element. |
| dependency | [Adjoint-tuple characterization](Yin_C_F0075_v1.md#statement) | Part 2 for the strong system on an arbitrary normal tuple. |
| review | [Whole-proof finding](../audits/reviews/Yin_R_F0209_v1.md#whole-proof-finding) | Both optimal tests including actual descent, central-summand transfer, finite moment limits and the exact normal and general-tuple scope. |
