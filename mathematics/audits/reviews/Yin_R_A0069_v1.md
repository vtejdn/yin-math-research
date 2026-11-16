---
author: Yin
---

# Binary incidence obstructions and lifting a fixed zero product

A separate reviewing agent checked the fixed C_A0038_v1 for Yin on 2026-11-16T17:50 UTC.
The reviewer did not participate in developing this Claim and received or consulted no development discussion, author explanation or earlier verdict on its proof before forming the findings.
Earlier work by this reviewer on the comparison theorem C_A0029 concerns varying residue characteristics and supplies no step in the proof inspected here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0038_v1.md#statement) | Fixed-support lifting criterion, implication for complex scalar convolution and the distinct sufficient test on source occurrences. |
| [Whole-argument finding](#whole-argument-finding) | [Incidence and lifting](../../claims/Yin_C_A0038_v1.md#the-incidence-matrix-and-lifting) | Normalization, row dependencies, every extension of a specified lift, the sufficient ideal test, branch extraction, field embedding and unramified scope. |
| [Whole-argument finding](#whole-argument-finding) | [Three fibers](../../claims/Yin_C_A0038_v1.md#a-three-fiber-obstruction) | Actual fibers and contradiction on a group with torsion. |
| [Whole-argument finding](#whole-argument-finding) | [Simultaneous-step system](../../claims/Yin_C_A0038_v1.md#the-simultaneous-step-system-in-ope26f) | Occurrences, root survival, the component right-hand side and failure of pointwise additive separation on the full type family. |
| [Whole-argument finding](#whole-argument-finding) | [A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract) | Nonintegral canonical kernel trace for a nonzero convolution operator with a nonzero finitely supported kernel vector, when the group is torsion-free. |

## Whole-argument finding

Expanding a product of two coordinates lifted from odd integers gives the full linear correction modulo \(2^{n+1}\), since its quadratic correction is divisible by \(2^{2n}\).
In the resulting binary equation each occurrence of either variable contributes one, independently of the previous odd coefficient of its partner.
Evenness of every fiber makes the sum of the columns on either side zero, including when a side consists of just one column.
Removing the two chosen columns therefore preserves the image and the row dependencies.
The binary left nullspace consists exactly of unions with even degree at every vertex.
For the initial all-ones lift the value on such a dependence is the total number of cells divided by two, reduced modulo two.
This gives both directions of the divisibility-by-four test.
The same dependence remains an obstruction in a residue field extension with uniformizer \(2\), with no implication from that calculation for arbitrary ramified lifts.

For the sufficient ideal test, each chosen independent row has the same derivative at every odd lift.
The selected equations can therefore be solved successively with all normalizations, and substitution of odd units into the stated Laurent identities over \(\mathbb Z_{(2)}\) forces every omitted equation at each level.
In the general test, every deeper solution has a chain of reductions up to the fixed point.
Finite branching thus gives a compatible infinite branch, even if the initially available deeper solutions were unrelated.
The resulting finitely generated subfield of \(\mathbb Q_2\) embeds in \(\mathbb C\) by extending an embedding of a rational function field across a finite algebraic extension.
This is an abstract field embedding and requires no comparison between the two topologies.
The distinct group labels and odd units ensure a nonzero complex coefficient at every prescribed support position.
For \(ab=0\) the nonzero \(b\delta_e\) is in the regular kernel of \(a\), while \(a\delta_e\ne0\).
The faithful normalized scalar trace is strictly between zero and one on that kernel projection.

For the example in \((\mathbb Z/2)^3\), the six different unordered off-diagonal sums are the three basis vectors and the three distinct sums of two basis vectors.
The three chosen off-diagonal fibers contribute two cells at each of three vertices on either side and six cells in total.
The same three complex coefficient equations require pairwise opposite nonzero ratios on a triangle, an impossibility in characteristic zero.
The example has the stated torsion and supplies no torsion-free case.

The review used the outgoing signed labels, inverse matching, projective lines and extra sets on [pp. 2–4 of Ope26f](../../literature/pdf/Ope26f.pdf#page=2).
It also checked the root-component factors, the stated root separation, component parity and the nonexplicit choice of matchings in [§6, p. 24](../../literature/pdf/Ope26f.pdf#page=24).
The source's formula (1.1) sums over *vertices* in the two selected components.
Its proof in §6 invokes Proposition 5.1 for uniqueness of each root's contribution to the identity and does not claim that the other group labels are pairwise distinct.
The Claim handles the two consequences separately.
Collecting the odd multiplicities before applying the fixed-support test gives the actual characteristic-two support.
Vanishing of the finer simultaneous-component sums implies vanishing after collection in characteristic zero, and the two root coefficients still survive even if other labels merge.

For the component calculation, \(1\) and \(129\) both give zero modulo two after subtracting one and dividing by two, whereas adding the two common extras contributes one.
Each undirected simultaneous edge contributes exactly once to the sum over selected signed labels, since its two readings are inverse and the orientation selects one of them.
Subtracting the sum of the local half-degree corrections from the edge count gives half the number of vertices, by the degree sum.
This recovers the required residue, including multiplicities.
On the full empty-extra line family symmetry on pairs of distinct lines forces the sum of the row and column parameters with the same line index to be constant.
At any point, comparison of the three off-diagonal entries from three different incident lines then forces all three column parameters to agree and the orientation bit at that point to equal the constant.
The source pairs \(16513-3\) ordinary letters among themselves, so the resulting constant assignment cannot be an orientation.

The proof supports every stated conclusion.
The reviewer checked the preprint's cited graph construction and the application of its stated root-separation and torsion-freeness results, without auditing the underlying random-graph and asphericity proofs.
The preprint supplies existence of matchings and the even component sizes.
Neither that input nor the full-type obstruction decides the first lift for the actual root-component table, gives a complex zero product for its group, or selects an assessment of A0001.
