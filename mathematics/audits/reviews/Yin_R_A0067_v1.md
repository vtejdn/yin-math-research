---
author: Yin
---
# A homogeneous unit and a prime denominator in a cyclic extension

A separate agent inspected the complete [fixed Claim](../../claims/Yin_C_A0036_v1.md) for Yin on 2026-11-16T17:50 UTC.
The reviewer shared the general Task context, worked on other mechanisms and took no part in this proof's development.
The Claim and its specified inputs were inspected without exploration notes, substantive development discussion, author explanations or a previous conclusion on this argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0036_v1.md#statement) | Prime-index equivalences, allowed denominators and extraction in a finite quotient. |
| [Whole-argument finding](#whole-argument-finding) | [Restriction and crossed product](../../claims/Yin_C_A0036_v1.md#restriction-to-a-subgroup-and-the-actual-crossed-product) | Trace normalization, finite grading in the affiliated ring, division and rational closures. |
| [Whole-argument finding](#whole-argument-finding) | [One-dimensional module](../../claims/Yin_C_A0036_v1.md#a-one-dimensional-module-at-a-prime-index-failure) | Semisimplicity, orbit of blocks, dimension count and ordered norm. |
| [Whole-argument finding](#whole-argument-finding) | [Rank and finite matrix](../../claims/Yin_C_A0036_v1.md#the-rank-and-a-finite-matrix-over-the-group-ring) | Graded eigenspaces, restriction to the division ring and Schur-complement extraction. |
| [Whole-argument finding](#whole-argument-finding) | [Prime in a finite extension](../../claims/Yin_C_A0036_v1.md#finding-the-prime-in-a-finite-extension) | Sylow restriction and existence of the first failing cyclic step. |
| [Whole-argument finding](#whole-argument-finding) | [Abelianized norm and valuations](../../claims/Yin_C_A0036_v1.md#an-abelianized-norm-obstruction-and-the-limit-of-integer-valuations) | Independence of lift modulo norms and equivalence of the invariant integer valuation test to an integer character lift. |
| [Whole-argument finding](#whole-argument-finding) | [Subgroup embedding](../../ledger/Yin_L_A0003_v1.md#actual-affiliated-embedding) | Separation of distinct cosets after clearing affiliated coefficients. |
| [Whole-argument finding](#whole-argument-finding) | [Laurent realization](../../ledger/Yin_L_A0003_v1.md#a-leading-coefficient-constraint-on-every-rational-solution) | Skew Laurent degree on fractions in the cyclic quotient construction. |
| [Whole-argument finding](#whole-argument-finding) | [Affiliated rank](../literature/Lin93/Yin_U001.md#affiliated-closure-and-rank-conventions) | Rank invariance under invertible operations and bounded denominators. |
| [Whole-argument finding](#whole-argument-finding) | [Rational closure](../literature/Lin06/Yin_U001.md#matrix-localization-and-fixed-ambient-closures) | Representation of a rational element as an entry of a matrix inverse over the chosen ambient ring. |

## Whole-argument finding

All four conditions are equivalent with the indicated orientation of the norm and the unnormalized traces.
Restriction sums diagonal traces at all coset representatives, each equal by commutation with right translations, so the multiplier is the index.
The subgroup representation on right cosets preserves affiliated invertibility.
After a common bounded left denominator is applied to a putative linear relation among grades, each summand at the identity vector is supported in its own right coset.
Separation on that coset forces its coefficient to vanish.
Conjugation preserves \(D\), so the resulting crossed product has right and left dimensions \(p\).
Left multiplication by any ambient-invertible square matrix is injective on the finite-dimensional right \(D\)-space of matrices over this crossed product, and hence reaches the identity.
This proves the inverse closure for all matrix sizes used in the argument.
The torsion-free Atiyah criterion and the agreement of closures in the positive case were checked at statement depth for coefficients \(\mathbb C\). [Lück and Linnell, Theorem 2.3(3)](../../literature/pdf/LL18--arxiv-v3.pdf#page=10)

The \(t\)-conjugates of a left \(D\)-linear projection onto a left ideal remain left \(D\)-linear projections onto that same ideal, because \(t\) acts semilinearly.
The \(p\)-th conjugate recovers the original projection since left multiplication by \(h\) commutes with every left \(D\)-linear map.
The average thus splits the inclusion over \(B\).
The automorphism \(t\mapsto\zeta t\) fixes precisely degree zero.
Any orbit sum of central primitive idempotents must then be one, proving transitivity without a hypothesis on the center of \(D\).
When there are \(p\) blocks each is one-dimensional over \(D\), and for a single nondivision simple block all its isomorphic simple left ideals have the same \(D\)-dimension, so primality forces that dimension to be one.
Writing \(tv=bv\) on this left ideal puts successive conjugates of \(b\) to the left of the earlier factors.
Independently multiplying \((b^{-1}t)^p\) gives the inverse of that ordered product followed on the right by \(h\).
Its degree guarantees exact order \(p\) when the power is one.

The Fourier idempotents for the order-\(p\) homogeneous unit are nonzero by independence of its distinct grades.
They split the algebra into right ideals, and the grading automorphism permutes all these ideals while fixing right scalars in \(D\).
The kernel in the restriction matrix has \(D\)-dimension one, since precisely the eigenvalue one is killed.
Row and column reduction over \(D\) and extension to the affiliated ring preserve the diagonal rank, giving original nullity \(1/p\) after dividing by the index.
For \(b=(Q^{-1})_{ij}\), elimination of the invertible \(Q\) block in the stated group-ring matrix leaves \(t-b\), with the row and column selectors in the required order.
This proves that the finite matrix realizes the claimed nullity even when \(b\) is unbounded as a regular operator.

In a general finite quotient restriction to the inverse Sylow subgroup multiplies the rank by an integer prime to the chosen denominator prime.
The first failing step in the lifted composition series then has a predecessor satisfying Atiyah, as required for the independent prime-index construction.
For the abelianized obstruction a change from \(t\) to \(dt\) changes its \(p\)-th power by \(N[d]\) in the abelianization and the induced action changes by an inner automorphism before abelianization.
An invariant integer valuation provides a character on \(K\) by multiplication by \(p\), and its chosen value on \(t\) respects both conjugation and \(t^p=h\).
Its reduction modulo \(p\) has precisely the required kernel.
Conversely an integer lift supplies the nonzero grading on \(K\), with step \(m\), whose kernel inherits the Atiyah property.
The actual skew Laurent ring embeds by coset separation, and its classical fraction division ring is a division subring of \(D\) containing \(\mathbb C[K]\).
It is therefore all of \(D\).
Least degree multiplied by \(m\) extends over those fractions, retains its group values and is unchanged by \(t\), which preserves the coefficient ring and sends \(s\) to a unit group coefficient times \(s\).
This proves the integer-lift equivalence even when the original group is infinitely generated.
The criterion does not resolve whether a rational homogeneous torsion unit exists in any torsion-free extension of the specified kind.
