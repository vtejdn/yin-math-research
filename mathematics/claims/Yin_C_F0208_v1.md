---
author: Yin
---
# A one-sided column criterion for normal duals after adjoining two free Haar unitaries

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be a finite tuple of bounded normal generators in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Assume the actual starred ACSY condition \(\mathsf A(X)\) of [F0011](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Write \(P=\mathbb C\langle X,X^*\rangle\), \(H=L^2(M,\tau)\), \(\Omega=1\) and \(P_\Omega h=\langle\Omega,h\rangle\Omega\).
For a fixed \(i\), let \(\delta_i\) be the coordinate derivation, \(\xi_i=\delta_i^*(1\otimes1)\), and \(E_i=(\mathrm{id}\otimes\tau)\delta_i\) on \(P\).
Both the derivation and its vacuum are unique on this core by the forced starred values in [C_F0076, Part 1](Yin_C_F0076_v1.md#statement).
Define the extended real number
\[
 c_i(X)=\sup\left\{\left(\sum_{k=1}^m\|E_ip_k\|_2^2\right)^{1/2}:
 m\ge1,\ p_k\in P,\ \left\|\sum_{k=1}^m p_k^*p_k\right\|\le1\right\}.
 \tag{1}
\]
Adjoin two Haar unitaries \(U,V\) that are free from each other and jointly free from \(M\), and put \(Z=(X,U,V)\) and \(\widetilde M=W^*(Z)\) with its free product trace.
Let \(\beta_i(Z)\) be the [C_F0201 optimum](Yin_C_F0201_v1.md#statement) for the single old coordinate \(i\), the infimum of the operator-norm-to-\(L^2\) norms of linear \(T:\widetilde M\to L^2(\widetilde M)\) satisfying \([T,L_{Z_j}]a=\delta_{ij}P_\Omega a\) for all bounded \(a\), with \(T1\) unrestricted.

The augmented finite normal tuple satisfies \(\mathsf A(Z)\) with the old vacua \(\xi_i\) and the new vacua \(U,V\).
For every old \(i\),
\[
                 c_i(X)/4\ \le\ \beta_i(Z)\ \le\ c_i(X).       \tag{2}
\]
In particular, if the ratios in (1) diverge along finite columns for one normal ACSY tuple and coordinate, this same two-unitary enlargement has no bare full-domain dual system.
Finite \(c_i(X)\) is also equivalent to existence of a state \(\varphi_i\) on \(C^*(X)\) and a finite \(c\ge0\) with
\[
                   \|E_i p\|_2^2\le c^2 \varphi_i(p^*p)
                         \qquad(p\in P).                         \tag{3}
\]
The smallest such \(c\) is \(c_i(X)\), attained when finite.

On the class of all finite bounded normal generating tuples, the universal assertions \(\mathsf A\Rightarrow\mathsf F\), \(\mathsf A\Rightarrow\mathsf S\), and finiteness of (1) for every coordinate of every tuple satisfying \(\mathsf A\) are equivalent.
The conclusion gives a test of the universal implications and does not assert that (1) is always finite.
The \(p_k\) in (1) range over the represented starred core.

## Argument

### Vacuum preservation and the right slice on reduced words

Use the three free factors \(M,W^*(U),W^*(V)\) with cores \(P,\mathbb C[U,U^*],\mathbb C[V,V^*]\).
The algebraic free product of these cores embeds as the full starred polynomial core of \(Z\) by the orthogonal decomposition into centered reduced tensors in the pointed tracial free-product representation.
We use the [free-product representation in Voi98, Sections 5.5–5.8](../audits/literature/Voi98/Yin_U005.md#voi98-u005) at that Hilbert-space scope.
On a Haar factor with generator \(u\), the derivation on Laurent polynomials is fixed by \(\delta u=1\otimes1\) and \(\delta u^*=-u^*\otimes u^*\).
Its double trace on \(u^n\) is \(1\) for \(n=1\) and zero for every other integer \(n\), giving the vacuum \(u\).

Extend each chosen factor derivation to the algebraic free product by zero on the other two factors and the outer Leibniz rule, including its two-leg target in the full coarse Hilbert space.
For the vacuum identity test a centered reduced word of length at least two.
Each differentiated block belongs to the chosen factor, while at least one of its prefix or suffix is nonempty and adjacent to that block in a different factor.
On this side, multiplying the reduced segment by any Hilbert vector from the chosen factor gives zero scalar trace, first on bounded vectors by freeness and then by continuity.
Thus the double trace of every cut vanishes, also for completed two-leg tensors by density.
The reduced word is orthogonal to the old factor Hilbert space, including its vacuum vector \(\xi_i\), or to the corresponding Haar factor when testing a new derivation.
The single-block and constant identities follow in the factors, since each vacuum is centered.
This proves the claimed actual adjoint identities on the full core.

Now treat \(M\) as one factor and \(N=W^*(U,V)\) as the other.
Choose orthonormal bases of their centered Hilbert spaces by applying Gram–Schmidt to the centered star monomials spanning each centered core and skipping zero remainders.
Every centered core element then has a finite basis expansion.
Let \(\mathcal W\) consist of \(1\) and the products of alternating centered basis letters ending in an \(N\)-letter.
The free-product representation gives a unitary from \(\ell^2(\mathcal W)\otimes H\) to \(L^2(\widetilde M)\) by \(e_w\otimes b\mapsto wb\).
Every full-core polynomial \(y\) has a finite expansion \(y=\sum_w w b_w\) with \(b_w\in P\).
In particular, the conditional expectation onto \(M\) satisfies \(\mathbb E_M(w^*w')=\delta_{ww'}1\), as is seen by testing the unitary against all bounded old-factor vectors.
Consequently \(\sum_w b_w^*b_w=\mathbb E_M(y^*y)\), of norm at most \(\|y\|^2\).
Equivalently, this last bound follows by applying the expansion to \(ya\) for arbitrary \(a\in M\) and taking the operator norm of left multiplication on \(H\).

Let \(\widetilde E_i\) be the old coordinate's right slice on the augmented core.
Any cut in an old-factor letter within \(w\) has a remaining centered reduced suffix that starts and ends in \(N\).
The trace of this suffix times \(b_w\) and an old right tensor leg vanishes by freeness and Hilbert continuity.
Cuts of \(N\)-letters vanish by definition.
Hence
\[
 \widetilde E_i(y)=\sum_w w E_i b_w,\qquad
 \|\widetilde E_i(y)\|_2^2=\sum_w\|E_i b_w\|_2^2
             \le c_i(X)^2\|y\|^2                                      \tag{4}
\]
when \(c_i(X)<\infty\).
This argument uses a whole correlated factor \(M\) in the right-module decomposition.

The actual vacuum gives closability of \(\widetilde E_i\) by [ACSY24, Theorem 3.4](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
For \(a\in\widetilde M\), [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) gives core approximants \(y_n\to a\) in \(L^2\) with \(\|y_n\|\le\|a\|\), testing strong density at \(\Omega\).
Take a weak cluster point of the bounded \(\widetilde E_i(y_n)\).
The weakly closed graph of the closure puts \(a\) in its domain with that value, of norm at most \(c_i(X)\|a\|\).
Along the same subnet the core identity \(\widetilde E_i(Z_jy_n)=Z_j\widetilde E_i(y_n)+\delta_{ij}\tau(y_n)1\) has a weak limit, and \(Z_jy_n\to Z_ja\) in \(L^2\).
Applying the graph again proves the full commutator at \(a\).
Restriction of this closure to bounded inputs gives the upper bound in (2).

### Encoding finite columns by two Haar unitaries

For every positive integer \(k\) put \(u_k=U^kVU^{-k}\).
The \(u_k\) form a free Haar family.
Indeed every product of nonzero powers of successively distinct \(u_k\) expands to a nonidentity reduced word in \(U,V\) with nonzero powers of \(U\) separating successive powers of \(V\), and therefore has zero trace.
The family is jointly free from \(M\).
For a finite column \(b_1,\ldots,b_m\in P\) put \(y=\sum_k u_kb_k\) and \(Q=\|\sum_k b_k^*b_k\|^{1/2}\).
Then
\[
               Q\le\|y\|\le2Q,\qquad
               \|\widetilde E_i y\|_2^2=\sum_k\|E_i b_k\|_2^2.          \tag{5}
\]
The slice identity follows by \(\delta_i u_k=0\) and \(\mathbb E_M(u_k^*u_l)=\delta_{kl}1\), including for Hilbert-valued sliced coefficients by bounded approximation.
The same expectation applied to \(y^*y\) gives the lower norm bound.

To prove the upper norm bound work in the tracial free product of \(M\) and the \(m\) abelian factors individually generated by the \(u_k\).
Its left representation is faithful, so it gives the norm of \(y\) in \(\widetilde M\).
Let \(K_k\) be the subspace of reduced tensors beginning in factor \(k\), and let \(P_k\) be its orthogonal projection.
The subspaces \(K_k\) are mutually orthogonal and \(L_{u_k}(1-P_k)\) has range in \(K_k\), since \(u_k\) is centered.
Thus for any Hilbert vector \(z\),
\[
 \Big\|\sum_k L_{u_k}(1-P_k)L_{b_k}z\Big\|_2^2
       \le\sum_k\|L_{b_k}z\|_2^2\le Q^2\|z\|_2^2 .
\]
For the remaining sum, the input support of \(P_kL_{b_k}\) lies in
\(S_k=K_k\oplus(H_M^0\otimes K_k)\), where \(H_M^0=H\ominus\mathbb C1\).
Indeed multiplication by \(b_k\) preserves the initial \(k\)-letter only through its scalar trace and can expose one after removing an initial \(M\)-letter only when the next letter is in factor \(k\).
On \(S_k\) this map to \(K_k\) is the row consisting of \(\tau(b_k)\) on the first summand and the scalar functional \(x\mapsto\tau(b_k x)\) on \(H_M^0\), tensored with the identity on \(K_k\).
It has norm \((|\tau(b_k)|^2+\|b_k-\tau(b_k)1\|_2^2)^{1/2}=\|b_k\|_2\).
The \(S_k\) are mutually orthogonal.
Writing \(\Pi_k\) for their projections gives
\[
 \Big\|\sum_k L_{u_k}P_k L_{b_k}z\Big\|_2
 \le \sum_k\|b_k\|_2\|\Pi_k z\|_2
 \le \Big(\sum_k\|b_k\|_2^2\Big)^{1/2}\|z\|_2
 \le Q\|z\|_2 .
\]
Adding both terms proves (5).

### Arbitrary single-coordinate witnesses

Take any bounded full-domain witness \(T\) for the single old index \(i\), and set \(T_0(a)=T(a)-aT(1)\).
Then \(T_0(1)=0\), \(\|T_0\|\le2\|T\|\), and its commutators agree with those of \(T\).
The single-coordinate argument of [C_F0070](Yin_C_F0070_v1.md#statement-and-interfaces) gives the Hilbert–Schmidt commutator with \(Z_i^*\) as the forced normal phase and gives zero commutators with \(Z_j^*\) for \(j\ne i\) by the homogeneous bounded-map Fuglede identity.
By [C_F0076, Part 1](Yin_C_F0076_v1.md#statement) these are exactly the commutators of the actual canonical slice on the core, using the Hilbert–Schmidt formula in ACSY24 Theorem 3.4.
The two normalized maps agree on \(1\) and then, by the generator and adjoint-generator identities, on every represented starred word of the augmented tuple.
This comparison uses a single witness and permits starred coefficients in (5).
Now
\[
     \left(\sum_k\|E_i b_k\|_2^2\right)^{1/2}
     =\|T_0(y)\|_2\le 2\|T\|\|y\|\le4\|T\|Q .
\]
Taking the supremum of the column ratios and the infimum over \(T\) proves the lower bound in (2), including the infinite case.
Bare full-domain witnesses for a normal coordinate with its nonzero prescribed commutator are automatically bounded from the operator norm to \(L^2\) by [C_F0069, Part A](Yin_C_F0069_v1.md#statement).
In particular an infinite \(c_i(X)\) disproves \(\mathsf F(Z)\) even when arbitrary algebraic bare witnesses are allowed.

### State domination and the universal implications

A domination (3) immediately bounds (1) by \(c\).
Conversely suppose \(c=c_i(X)\) is finite.
For a finite list \(p_1,\ldots,p_m\in P\) consider the compact convex set of vectors
\[
 \left(c^2\varphi(p_k^*p_k)-\|E_ip_k\|_2^2\right)_{k=1}^m
\]
as \(\varphi\) varies over all states on \(C^*(X)\).
If this set missed the closed positive orthant, finite-dimensional strict separation would yield nonnegative weights \(\lambda_k\) for which the supremum of their pairing with this set was negative.
That supremum equals \(c^2\|\sum_k\lambda_k p_k^*p_k\|-\sum_k\lambda_k\|E_i p_k\|_2^2\), because states norm positive elements.
It is nonnegative by (1) applied with coefficients \(\sqrt{\lambda_k}p_k\).
The state space is weak-star compact, so the finite intersection property gives one state satisfying all tests with the optimal \(c\).

If every normal ACSY tuple has bare full-domain duals, apply this to the finite tuple \(Z\).
Automatic boundedness and the lower bound in (2) give finite column constants for the original \(X\).
Conversely, universal finiteness of the column constants supplies all old-coordinate full-domain witnesses on the enlargement by (4).
For \(a\in M\), restrict each witness to \(a\), project its value onto \(L^2(M)\), and negate the result for the generator-first convention of \(\mathsf F\).
That projection fixes \(\Omega\) and commutes with left multiplication by every old generator, so the compressed maps witness \(\mathsf F(X)\).
Finally [C_F0075, Parts 2–3](Yin_C_F0075_v1.md#statement) identifies this universal normal implication with \(\mathsf A\Rightarrow\mathsf S\), using the adjoint tuple as well.
No general endpoint bound has been assumed in the converse direction.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:39 |
| status | open |
| reason | Fixed candidate comparing one-sided column domination with a full-domain single-coordinate optimum on a finite free augmentation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Augmented ACSY, two-sided quantitative comparison, one-state domination and equivalence of the universal normal implications. |
| argument | [Argument](#argument) | Reduced-word extensions and bounds, both parts of the Haar norm estimate, single-coordinate rigidity, state separation and universal reduction. |
| dependency | [Forced normal derivatives](Yin_C_F0076_v1.md#statement) | Part 1 identifies the starred-generator phases and their uniqueness on each actual normal core. |
| dependency | [Reduced free-product representation](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | The pointed Hilbert-space decomposition, centered reduced-word inner products and the factor actions in Sections 5.5–5.8. |
| dependency | [Canonical contraction](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4 gives closability and the Hilbert–Schmidt core commutators under the actual vacuum hypothesis. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Operator-norm-controlled approximation at the vacuum in the augmented starred core. |
| dependency | [Single-coordinate starred commutator](Yin_C_F0070_v1.md#statement-and-interfaces) | The individual inhomogeneous normal phase and homogeneous bounded-map Fuglede identities for a bounded witness. |
| dependency | [Automatic boundedness](Yin_C_F0069_v1.md#statement) | Part A applies to every bare map with its distinguished normal coordinate on the whole bounded algebra. |
| dependency | [Normal strong systems](Yin_C_F0075_v1.md#statement) | Parts 2–3 identify the two universal normal implications using the bare hypotheses on both adjoint tuples. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:48 |
| status | proved |
| reason | Adopt both column bounds, optimal state domination and the universal normal reduction after whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Augmented ACSY, two-sided quantitative comparison, one-state domination and equivalence of the universal normal implications. |
| argument | [Argument](#argument) | Reduced-word extensions and bounds, both parts of the Haar norm estimate, single-coordinate rigidity, state separation and universal reduction. |
| dependency | [Forced normal derivatives](Yin_C_F0076_v1.md#statement) | Part 1 identifies the starred-generator phases and their uniqueness on each actual normal core. |
| dependency | [Reduced free-product representation](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | The pointed Hilbert-space decomposition, centered reduced-word inner products and the factor actions in Sections 5.5–5.8. |
| dependency | [Canonical contraction](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4 gives closability and the Hilbert–Schmidt core commutators under the actual vacuum hypothesis. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Operator-norm-controlled approximation at the vacuum in the augmented starred core. |
| dependency | [Single-coordinate starred commutator](Yin_C_F0070_v1.md#statement-and-interfaces) | The individual inhomogeneous normal phase and homogeneous bounded-map Fuglede identities for a bounded witness. |
| dependency | [Automatic boundedness](Yin_C_F0069_v1.md#statement) | Part A applies to every bare map with its distinguished normal coordinate on the whole bounded algebra. |
| dependency | [Normal strong systems](Yin_C_F0075_v1.md#statement) | Parts 2–3 identify the two universal normal implications using the bare hypotheses on both adjoint tuples. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0216_v1.md#finding) | Both inequalities, all actual vacua, starred witness rigidity, state criterion, universal equivalences and seven direct inputs. |
