---
author: Yin
---

# Transferring F0001 rationality tests to the strong Atiyah problem

On 22 November 2026 three agent-S delegates examined the dual-system, tensor and approximation methods for [A0001](../tasks/Yin_T_A0001_v1.md#contract).
The following route decisions concern integer kernel dimension in the original regular representation, with complex coefficients and the unnormalized matrix trace.
The first two proposals were taken through explicit tests during this round.

## What transfers from the F tasks

The [fixed F0001 contract](../tasks/Yin_T_F0001_v7.md#canonical-closed-dual-resolution) was completed for selfadjoint generators with finite free Fisher information.
Its proof selects the canonical closed duals, verifies the domains on all bounded vectors and passes between one legal fraction and every legal fraction, including the raw operators on their natural domains. [C_F0067](../claims/Yin_C_F0067_v1.md#canonical-closed-dual-raw-rationality)
The broader mathematical results include [the maximal-\(\Delta\) tensor criterion and the normal dual specialization](../claims/Yin_C_F0068_v1.md#statement).
The first asks whether an affiliated tensor difference is a finite sum of generator differences.
The second enables an ordinary finite-rank commutator test for a bounded element of a normal generator algebra admitting the stated duals.
The [liberation-dual results](../claims/Yin_C_F0079_v5.md) impose their own domain, normalization and spectral hypotheses.
The [F0011 comparison](../tasks/Yin_T_F0011_v1.md#current-results-under-the-original-contract) gives the normal-tuple result and separates assumptions for arbitrary nonnormal tuples.

The implication from an abstract tensor certificate to rationality under maximal \(\Delta\) uses a division ring already realized in the ambient affiliated algebra.
Even with a rationality criterion, the [A0001 Schur scalar](../claims/Yin_C_A0116_v1.md#reducing-every-two-by-two-input-to-three-coefficients) is a defined rational expression at the outset.
Its nonzero kernel is the question.
Moreover, separate injectivity of the generator-difference maps need not give joint injectivity: for the two commuting Haar coordinates \(x,y\) of \(\mathbb Z^2\), let \(w=1\otimes1\).
The differences \(\Psi_x,\Psi_y\) commute, and \((\Psi_y w,-\Psi_x w)\ne0\) is a joint cycle even though this group satisfies the whole conjecture.
This rules out imposing the free-tuple uniqueness conclusion merely from the separate scalar shifts.

## First priority for all matrix sizes

Apply the normal-generator part of F0001 on a single cyclic edge \(H=\langle z\rangle\), where its dual exists explicitly.
For additive matrices on a cyclic amalgam, the [two-vertex formula](../claims/Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) needs the support \(Q\) of the expected kernel graph to transfer to two finite vertex ranks.
With \(P\) the original graph projection, \(J\) the isometric inclusion of the edge coordinates, and \(D\) the projection onto nonnegative Fourier exponents, [the Hardy projection test](../claims/Yin_C_A0120_v1.md#proof-of-the-cyclic-criterion) identifies precisely the quantity to bound:
\[
                  \dim_{\mathbb C} PJ D\big(\ker(PJ)\big).
\]
It is finite exactly when \(Q\) has rational entries.
The noncentral, nonclosed-range calculation there gives this dimension one, although the expected graph projection itself has a nonrational diagonal coefficient and has no spectral gap on its support.
This directs the rationality test to the data actually consumed by the vertex formula.

A second argument obtains edge rationality from the group action, without estimating coefficients of an inverse.
Suppose \(G/K\) admits Følner sets and \(H\) acts freely on it.
Exact kernel vectors living over finitely many \(K\)-cosets, and their right translates, densely span the full kernel: the codimension loss per coset is at most the number of output rows times the relative boundary fraction.
Restrictions of these vectors to \(H\) have finite support, since a translated coset intersects \(H\) at most once.
These Laurent columns span a finite-dimensional space over \(\mathbb C(z)\), whose orthogonal range projection is \(Q\).
This proves [complex-coefficient permanence in this cyclic amalgam class](../claims/Yin_C_A0119_v1.md#amalgams-and-arbitrary-rectangular-matrices), using independent integer ranks at both vertices; adjoining identity pivots covers arbitrary finite matrices.
Neither finite ordinary support of kernel vectors in \(G\) nor a field of definition smaller than \(\mathbb C\) is required.
The fold of the Promislow double is an explicit noncentral test; its total group already lies in Linnell's class.
The [published finite-edge theorem](https://doi.org/10.1007/s00039-025-00710-4) has a different edge hypothesis; no claim of historical priority or of a previously uncovered group is made by this comparison.

The next target in [the graph strategy](../strategies/Yin_S_A0005.md#cyclic-edge-support-through-a-regular-group-action) is finite-dimensionality of the displayed Hardy space of defects on an individual graph outside this Følner argument.
Uniform approximation of \(Q\) by rational projections does not suffice.
For instance the graph projections of the Taylor polynomials for \(e^z\) converge uniformly on the circle to its graph projection, yet the limit is nonrational: the quotient of its \(21\) and \(11\) entries recovers \(e^z\).
If a rational function represented \(e^z\) on the circle, the identity theorem after clearing denominators would give an impossible polynomial-times-exponential identity.
To pass a rank bound through approximation one needs uniform bounds on the ordinary defect ranks or another direct finite-dimensionality argument.

## Second priority for an individual Schur complement

In [the three-coefficient reduction](../claims/Yin_C_A0116_v1.md#reducing-every-two-by-two-input-to-three-coefficients) the group relations can obstruct coordinate duals before one even reaches the rational expression.
For example, if a bounded operator \(D\) commutes with \(\lambda(L)\), then \(D-\lambda(g)D\lambda(g)^*\) commutes with \(\lambda(L\cap gLg^{-1})\).
If that intersection is infinite, its restricted regular representation has no nonzero finite-dimensional invariant subspace: its matrix coefficients vanish at infinity, whereas a finite-dimensional unitary orbit recurs.
Consequently a finite-rank difference of this form must vanish.
Repeated edge translates in the Promislow example give an explicit infinite-rank difference for the original word cut. [Ordinary cut calculation](../claims/Yin_C_A0118_v1.md#a-double-over-an-infinite-cyclic-subgroup)

Instead bend an auxiliary representation along a subgroup on which its two vertex restrictions agree.
Throughout the unitary phase family use \(\lambda_G(g)\otimes\pi_t(g)\); the trace of its kernel is the original one times the auxiliary dimension.
Clear scalar powers of the phase in the finite matrix before specializing at zero.
Surviving corner entries in a triangular specialization give full regular rank even when the single denominator involves both vertices. [Rank calculation](../claims/Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization)
This differs from ordinary character twisting and from treating a finite-dimensional evaluation as a replacement for the regular representation.
It needs neither soficity nor a nonunitary twisting theorem; general twists on sofic groups are studied by [Boschheidgen–Jaikin-Zapirain](https://doi.org/10.1112/blms.13050).

In the doubled Promislow group the resulting scalar has full rank, although the abelianization is finite and the shared edge is noncentral.
Adding a mixed commutation relation leaves only two admissible phases for the displayed bend even in a torsion-free quotient retaining both vertices.
In either example an admissible phase must satisfy **every** relator.
This restriction depends on which words commute.
For \([a_1,a_2]=1\), the coefficient of \(t^{-1}\) forces the product of the two required opposite mixing blocks to vanish at every multiplicity. [Two-weight obstruction](../claims/Yin_C_A0121_v1.md#a-commuting-relation-in-the-two-weight-deformation)
For \([k^{-1}a_1k,a_2]=1\), two auxiliary coordinates still fail, but [four coordinates suffice](../claims/Yin_C_A0122_v1.md#statement): the conjugator interchanges the two tensor factors, so the commuting images act in separate factors.
This second group also has independent known coverage.
The [congruence subgroup double](../claims/Yin_C_A0121_v1.md#statement) separates the two selected routes: a property (T) vertex containing the infinite edge excludes any amenable coset action on which the edge is free, while a suitable finite unitary representation still determines the rank of the tested mixed pencils.
This is an individual-matrix result, without an all-matrix assumption at the vertices.
The [chain calculation](../claims/Yin_C_A0123_v1.md#the-finite-inverse-layer) verifies the propagation step for any finite number of occurrences of the mixed inverse \(p^{-1}\), when the upper entries come from the first vertex, the lower border from the second and the last diagonal is \(p\).
F0001's common left denominator for finitely many affiliated coefficients permits the same rank degeneration for unbounded vertex entries at an arbitrary fixed inverse depth.
The [representation strategy](../strategies/Yin_S_A0012.md#route) takes the next allocation.

## A first-order fallback and its negative controls

For a unitary representation \(\pi\) of \(G\) and a cocycle \(b(gh)=b(g)+\pi(g)b(h)\), form the map \(\partial_b(g)\delta_h=b(g)\otimes\delta_{gh}\).
It differentiates a group-ring word by the twisted product rule and respects its actual relators.
For a finite group-ring matrix \(A\), let \(e=P_{\ker A}\) and \(q_\pi=P_{\ker A_\pi^*}\), where \(A_\pi\) is the regular twist.
One has \(q_\pi\,\partial_b A\,e=0\).
Indeed, truncate \(b\) by metric projection \(F_N\) onto the Hilbert ball of radius \(N\) and put \(V_N\delta_h=F_N(b(h))\otimes\delta_h\).
The difference \(V_N\lambda(g)-(\pi(g)\otimes\lambda(g))V_N\) converges on group basis vectors to \(\partial_b(g)\).
Its norm is at most \(\|b(g)\|\) by equivariance and nonexpansiveness of \(F_N\).
Strong convergence follows, and the two exact kernel projections kill each truncated matrix commutator before passage to the limit.
This calculation keeps all differentiations on the polynomial border, including for the [repeated-denominator tests](../claims/Yin_C_A0117_v1.md#chain-realization-and-rank).

A nonzero cocycle alone gives no rank lower bound.
Coboundaries give the identity through a single bounded implementer \(V\delta_h=\xi\otimes\delta_h\) with the appropriate sign, and limits of coboundaries on the finite input support give limits of the same identity.
On \(\mathbb Z^2\) for the regular representation the two cocycle values in Fourier coordinates satisfy \((1-z_2)\xi=(1-z_1)\eta\).
Writing them as \(((1-z_1)f,(1-z_2)f)\) and truncating \(f\) shows that every such pair is a limit of coboundaries.
For comparison take the genus-two surface presentation \(\langle a,b,c,d\mid [a,b][c,d]=1\rangle\) with \([a,b]=aba^{-1}b^{-1}\).
A regular-representation cocycle constrained to vanish at \(b,d\) has values \(\xi,\eta\) at \(a,c\) satisfying
\[
  (1-\lambda(aba^{-1}))\xi+
    \lambda([a,b])(1-\lambda(cdc^{-1}))\eta=0.
\]
The product rule gives exactly this relation, which also suffices to descend a cocycle on the free presentation.
Both coefficients are injective with dense range since \(b,d\) have infinite order (already in the abelianization).
The resulting row has regular rank one and nullity one; no nonzero solution is supported in just one of its two coordinates.
A coboundary vanishing at \(b\) would have an implementing vector invariant under \(b\), hence would be zero.
This calculation finds coupled directions on the actual presentation; it does not show separation of the kernel and cokernel for the Schur input.
Defer this route until an actual slice of the compressed derivative separates a row and column of a mixed pencil or produces a scalar group-ring witness.
An isolated nonzero finite-rank cut over a free product already has that property in [C111](../claims/Yin_C_A0111_v1.md#argument).

The [F-series generic blow-up rank](../claims/Yin_C_F0186_v2.md#generic-rank) maximizes over unconstrained matrix substitutions; restricting to a finite group representation can decrease rank.
It therefore does not furnish the missing lower bound on the regular rank.
The [resolvent and Brown-measure comparison](../claims/Yin_C_F0171_v1.md) also distinguishes a Brown atom from the trace of a kernel projection, already for a nilpotent two-by-two matrix.
For the present allocation, a random matrix or determinant test must first preserve the group relators and transfer the zero singular-value mass in the needed direction.
