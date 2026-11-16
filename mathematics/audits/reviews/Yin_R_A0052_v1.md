---
author: Yin
---
# Laurent kernels on cyclic cosets and expansion under a zero product

A separate reviewing agent inspected the entire [fixed Claim](../../claims/Yin_C_A0021_v1.md) for Yin on 2026-11-16T15:46 UTC.
The reviewer had previously reviewed the cyclic stabilizer result used in this argument and the Fourier estimate cited for context.
The reviewer did not participate in developing the present derivation or receive its development discussion, author explanations, exploration notes or earlier verdicts.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0021_v1.md#statement) | Strict comparison of local and global kernel dimensions, the four-column circuit and expansion for both adjoint orders. |
| [Whole-argument finding](#whole-argument-finding) | [Strict dimension bound](../../claims/Yin_C_A0021_v1.md#strict-dimension-bound-on-a-finite-coset-window) | Laurent fibers, trace equality, Fourier support of the commuting projection and the contradiction on a right coset. |
| [Whole-argument finding](#whole-argument-finding) | [Four-column relation](../../claims/Yin_C_A0021_v1.md#the-four-column-relation) | Minimal column dependence, cofactor vectors, primitive Laurent generator and connectivity. |
| [Whole-argument finding](#whole-argument-finding) | [Combining the factors](../../claims/Yin_C_A0021_v1.md#combining-the-two-factors-on-a-coset-space) | Composition, ranks, parity and adjoint passage for all finite nonempty coset sets. |
| [Whole-argument finding](#whole-argument-finding) | [Cyclic stabilizer](../../claims/Yin_C_A0019_v1.md#the-stabilizer) | Its proof applies to every nonempty finite union of left cosets of an infinite cyclic subgroup in a torsion-free group. |

## Whole-argument finding

All three assertions follow with the given unnormalized trace.
In left coset coordinates the finite matrix has Laurent polynomial entries, since each group element in the support of \(T\) sends a representative to an output representative times a power of \(t\).
Restriction of the convolution to those input cosets therefore has the displayed matrix as its Fourier symbol.
Its fiber rank agrees with its rank over \(\mathbb C(t)\) almost everywhere by the maximal-minor test, including the identically zero case.
Integrating the fiber dimension gives the trace of the window kernel projection.
The compression of the global kernel projection fixes that subspace pointwise and has trace \(|I|\nu(T)\), which proves the weak bound.

Equality would make the compression itself the window kernel projection by positivity and trace faithfulness.
Its idempotence forces the off-diagonal block \((1-e_I)pe_I\) to vanish because the product of its adjoint with itself vanishes.
Taking adjoints gives commutation, so any nonzero convolution entry between \(g\) and \(sg\) places those points on the same side of the window.
Consequently every nonzero Fourier coefficient lies in the setwise stabilizer, and conditional expectation places \(p\) in its group von Neumann algebra.
The cited cyclicity proof uses only the finite coset permutation and torsion-freeness, hence applies to this choice of window.
The assumption \(\nu(T)<1\) gives \(T^*\ne0\), and \(Tp=0\) gives \(pT^*=0\).
On a right coset with a nonzero component of \(T^*\delta_e\), the multiplier of \(p\) therefore annihilates a nonzero Laurent polynomial, which is nonzero almost everywhere.
The scalar version applies to the trivial stabilizer.
Thus equality would force \(p=0\), contrary to \(\nu(T)>0\).

For four occupied cosets, \(b\) supplies a relation with four nonzero coordinates and the strict bound makes the rational kernel one-dimensional.
A relation on a proper subset cannot belong to this line.
Three independent rows have rank three, so their nonzero signed cofactor vector generates that same kernel and has no zero coordinate.
Dividing the coefficients of \(b\) by their Laurent gcd gives a primitive generator, and a Bézout relation for its entries shows that every Laurent vector on the line is its Laurent multiple.
Disconnected column support would separate the rows into disjoint sets and give a relation on a proper subset.
Taking adjoints interchanges the two factors and preserves their regular ranks.

For \(m\) input cosets the strict bound gives \(\operatorname{rank}_F b_X>m/2\), hence rank at least \(\lfloor m/2\rfloor+1\).
The full set \(Y=(\operatorname{supp} b)X\) contains every intermediate coset, so multiplication gives \(a_Y b_X=0\) before extension to the field.
The dimension of \(\ker_F a_Y\) is strictly below \(|Y|/2\) and at least the rank of \(b_X\).
Integrality of \(|Y|\) gives exactly \(|Y|\ge2\lfloor m/2\rfloor+3\), including \(m=1\).
The same argument for \(b^*a^*\) gives the asserted expansion for \(a^*\).
These estimates give necessary conditions on a half-rank zero product and leave its general existence unresolved.
