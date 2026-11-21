---
author: Yin
---
# Independent review of the finite free-translate spanning bound

An agent outside proof development reviewed C_A0007_v9 from its fixed statement and argument on 21 November 2026.
The reviewer received no development discussion or prior v9 verdict.
The earlier v8 review concerns a different construction.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0007_v9.md#statement) | Full spanning and norm estimates, finite constraint nullities, free-calibration limitations and constant-edge restriction. |
| [Whole finding](#whole-finding) | [Proof](../../claims/Yin_C_A0007_v9.md#argument) | All steps including the finite expected support, three-term estimate, trace conventions, successive sizes and examples. |
| [Whole finding](#whole-finding) | [Norm estimate](../../claims/Yin_C_A0007_v9.md#a-norm-estimate-with-explicit-constants) | Creation, diagonal and annihilation terms on the reduced free-product space, centering in the corner and positive lower bound. |
| [Whole finding](#whole-finding) | [Source interface](../literature/BBL21/Yin_U001.md#bbl21-u001) | Scalar meet and trace identity when the expected kernel is strictly positive, as used in the free-projection calibration. |

## Whole finding

The final result follows under the stated assumptions.
Free-product normal forms yield scalar freeness of the distinct conjugate subgroups; centering matrix entries and compressing by the constant support give the required amalgamated freeness.
The faithful expectation gives \(p\le q\) and the positive lower constant in its nonzero finite-dimensional support.
The reduced-word first-letter projections commute with the base and the centered variable maps the complementary summand to the appropriate first-letter summand.
Orthogonality of these images, the compressed second moment and the diagonal bound establish the three terms in the norm estimate.
The placement of the conditional Gram factors gives the claimed order inequality once \(m\lambda>(1+\sqrt2)^2\).
For \(m=\lceil6/\lambda\rceil\) the lower constant is \(5-2\sqrt6>0\).
The proof covers the zero projection separately.

In the constrained group-ring matrix the first \(ma\) equations select the \(m\) original kernel copies and the last \(n\) rows impose their sum.
The range projection of that sum has unnormalized trace \(d\); its polar initial support has the same trace.
Subtraction gives exactly \(mt-d\), and successive nullities differ by \(t\).
A separate integrality certificate for those actual nullities is still necessary.
The scalar free-projection calculation gives truncated addition of traces under joins and accepts any real projection trace in the stated measurable model.
The diagonal comparison shows why \(\lambda\) cannot be discarded.
Neither example is asserted to realize a fractional nullity of a finite torsion-free group-ring matrix.
The two conditional expectations in the final restriction give \((b-c)C(b-c)^*=0\), which forces \(bq=cq\) without selfadjointness of \(b\).

The inspection checked the required reduced-product interfaces against Ricard–Xu arXiv v2, Sections 1 and 5, and checked BBL21 arXiv v2 Theorem 3.5(vii) at the needed strictly positive scalar expectation.
The underlying external theories were accepted at these interfaces.
