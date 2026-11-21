---
author: Yin
---
# Integral obstructions on finite direct powers

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_A0001_v1](../tasks/Yin_T_A0001_v1.md#contract) | Detect failure of integrality by rational matrices on bounded direct powers of the original group. |
| [Yin_T_A0002_v1](../tasks/Yin_T_A0002_v1.md#contract) | Test signed integral products and the alternating tensor of the left support on powers of one finite right support. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Test whether a noncommuting single-parameter pencil admits a square-group rank certificate, and use finite row coefficients and translate expansion to constrain scalar witnesses. |

[Alternation on direct powers](../claims/Yin_C_A0096_v1.md#statement) removes the complex coefficients in the two universal questions.
A finite set of alternating rational expressions in the affiliated algebras is sufficient for a given complex matrix.
For [number-field coefficients](../claims/Yin_C_A0097_v2.md#statement) of degree \(d\), external tensor products of two consecutive column prefixes give the coordinate count \(j=\lfloor\log_2 d\rfloor+1\) independently of size.
At an actual number-field obstruction, among the explicitly given restriction-of-scalars matrices for some column step and some \(l\le j\), at least one has noninteger rank.
Computing the separate conjugate ranks is unnecessary if an independent rational rank certificate is available.
The missing input is a constraint on these particular rational ranks valid on arbitrary torsion-free direct powers.
For a [central polynomial pencil of degree \(h\) and generic rank \(r\)](../claims/Yin_C_A0096_v2.md#statement), \(rh+1\) coordinates now control every specialization, with at most \(rh\) exceptions to the generic rank.
Two coordinates suffice for the rank-one parameter channel and the stated diagonal factorizations.
For a [subfield in one abelian affiliated algebra](../claims/Yin_C_A0100_v1.md#statement), the two-coordinate common-root argument admits one arbitrary scalar parameter at every polynomial degree and matrix size.
Its tracial example preserves any prescribed finite set of group moments and still fails at a higher power with a noncanonical trace.
To pass beyond the commuting case, an argument must control the individual deficiencies of noncommuting matrix coefficients or exploit the full canonical trace.
For a Galois number field \(K\) and \(j\ge2\), the [matrix-unit calculation](../claims/Yin_C_A0104_v1.md#statement) gives a common denominator \(s\) with \(s^j\mid[K:K\cap D_{\mathbb Q}(G)]\).
This gives full square-group transfer at squarefree Galois degree and isolates possible repeated prime powers in larger degrees.
At degree \(2^j\), the [quaternion representation](../claims/Yin_C_A0102_v1.md#statement) passes all rational rank tests through power \(j\) with its own trace and has a scalar coefficient witness of rank \(1/2\).
For the canonical group labeling the two Cayley transforms of individual group elements cannot satisfy the anticommutation identity used by this model.
The [free word-ball construction](../ledger/Yin_L_A0065_v1.md#scope) preserves the rank tests and a fractional-rank witness while matching the canonical trace on any prescribed finite radius in a fixed five-generator marking.
The recovered witness uses longer words as the radius increases.
For a biquadratic field, assuming rational integrality on the square group, failure is equivalent to [two equations in the actual rational division closure](../claims/Yin_C_A0104_v2.md#statement) and gives a finite matrix of nullity \(1/2\).
For a prescribed rational function of one group element, the [double-coset support and parity tests](../claims/Yin_C_A0104_v3.md#statement) constrain all candidate partners.
On the Klein bottle group a bounded measurable partner exists for the indicated input although every rational partner is excluded.
The [coproduct and augmentation tests](../ledger/Yin_L_A0066_v1.md) impose other restrictions on denominators.
It remains open whether they control an unrestricted pair in the rational division closure.
For the Gardam group, the [biradial rank and spectrum formulas](../claims/Yin_C_A0107_v1.md#statement) compute matrix ranks over the two spherical generators and exclude every affiliated partner for a nonconstant real affine function of the symmetric adjacency operator.
The [finite-quotient rank comparison](../claims/Yin_C_A0109_v1.md#complex-rank-and-the-lift-of-a-character) gives lower bounds for arbitrary complex matrices from ranks over the three-element type quotient after a characteristic-two reduction and a character twist.
It proves full regular rank for every nonzero complex scalar linear combination of the seven positive triangle generators, with unrestricted input vectors in the regular Hilbert space.

## A finite-support test for the signed alternating factor

For distinct \(g_1,\ldots,g_a\in G\) and a nonempty finite set \(B\subset G\), take a unit vector \(v\) supported on \(B\).
The squared norm of \({\cal A}(g_1,\ldots,g_a)v^{\otimes a}\) is \(a!\det\Gamma(v)\), where \(\Gamma(v)\) is the Gram matrix of \(g_1v,\ldots,g_av\).
This follows by pairing the two permutations in the squared norm and summing over their relative permutation.
A zero product with right factor \(v\) and left support contained in the list forces this determinant to vanish.
It is enough here to test tensor powers of the same vector.

For \(i\ne j\) put \(x=g_i^{-1}g_j\).
Partition \(B\) into maximal consecutive segments for left translation by \(x\), and let \(L_{ij}\) be the largest segment size.
These are finite paths because \(x\) has infinite order.
Set \(M_{ii}=0\) and \(M_{ij}=\cos(\pi/(L_{ij}+1))\).
The matrix \(M\) is real symmetric because reversing a path preserves its length.
Compression of left translation by \(x\) to \(\ell^2(B)\) is a direct sum of finite one-step shifts.
For a path with \(L\) vertices, the real part of any unit scalar multiple of its shift is diagonally unitarily equivalent to half the path adjacency matrix.
The largest eigenvalue is \(\cos(\pi/(L+1))\), as follows from its sine eigenvectors.
Maximizing over the scalar phase bounds \(|\Gamma_{ij}(v)|\) by \(M_{ij}\).
Consequently, for every coefficient vector \(c\),
\[
         c^*\Gamma(v)c\ \ge\ \|c\|_2^2-|c|^{\mathsf T}M|c|
                       \ \ge\ (1-\rho(M))\|c\|_2^2 .
\]
Thus \(\rho(M)<1\) excludes every complex zero product on these supports.
This test uses just the actual translation segments, even if there are no real characters on the group.

At \(\rho(M)=1\), suppose both factors have the specified exact supports and their product vanishes.
The first inequality must be an equality term by term, since all entries of \(|c|\) are positive.
If \(L_{ij}>1\), any shorter segment for this pair has strictly smaller numerical radius.
Full support of \(v\) gives positive mass to that segment, so its presence makes \(|\Gamma_{ij}(v)|<M_{ij}\), a contradiction.
In particular three left labels have no such witness if each ratio has segments of length at most two and at least one ratio has both a two-vertex segment and an isolated vertex.
Indeed \(M_{ij}\le1/2\) gives \(\rho(M)\le1\), and the stated pair forces strictness at equality.
For an actual unresolved tuple, test the segment lengths and, in the equality case, the compatibility of the extremal path eigenvectors for the different ratios.
When \(\rho(M)>1\), the displayed lower bound alone gives no exclusion.
For three left labels the [matching argument](../claims/Yin_C_A0098_v1.md#statement) eliminates the entire case of paths of size at most two, including when all three are perfect matchings.
In this exceptional case the two cyclic orientations would give a common finite set stabilized by all quotients of the three oriented translations.
Torsion-freeness prevents it.
The remaining three-label case therefore has an actual translate progression \(b,xb,x^2b\) in the right support for one left-label ratio \(x\).
The [quantitative count](../claims/Yin_C_A0098_v2.md#statement-and-counts) forces at least two labelled progressions and bounds their density below in terms of the expansion of the specified ratio subgroup.
The [modulus and phase tests](../claims/Yin_C_A0099_v1.md#statement) constrain the triple fibers needed by unequal moduli and give finite normalized phases when all fibers are pairs.
The [three-row eliminant](../claims/Yin_C_A0101_v1.md#statement) bounds the actual left ratios by algebraic units and gives at most \(b^2\) projective rows even with triple fibers.
Apply the full translation matrix to any surviving candidate since the determinant norm may have extraneous roots.

## Group scope

For one finitely generated support group \(G\), all its finite direct powers embed as lamp subgroups of the restricted wreath product \(G\wr\mathbb Z\).
This group is finitely generated by a generating set at one lamp and the shift.
It is torsion-free since every torsion element projects trivially to \(\mathbb Z\) and the base is a direct sum of torsion-free groups.
Thus one may use rational integrality on this overgroup as a sufficient input, by restriction to coordinate subgroups.
The construction does not transfer integrality from \(G\) to the overgroup.
