---
author: Yin
---
# Independent review of integral elimination for three left labels

## Whole finding

Reviewed on 2026-11-21 at 05:05 UTC for Yin by an agent outside the development of the proof.
The inputs were the fixed [statement](../../claims/Yin_C_A0101_v1.md#statement) and [argument](../../claims/Yin_C_A0101_v1.md#argument), including the infinite cyclic example, and the cited mathematical sources.
No proof-development discussion, author explanation or earlier review conclusion was used.
I find the whole stated result proved.

In the rows indexed by \(g_iB\), column \(h\) contributes \(X_i\) at row \(h\) and, after setting the remaining variable to zero, contributes \(X_j\) at row \(g_i^{-1}g_jh\) if that label belongs to \(B\).
This second map has indegree and outdegree at most one, and a cycle of length \(s>0\) would give \((g_i^{-1}g_j)^s=1\).
The ordering along its paths triangularizes the minor with diagonal \(X_i\), giving \(X_i^b\) over every field.
Thus any projective row with a missing coordinate has a nonzero maximal minor.

The diagonal \(T\) in the third minor makes its degree-\(b\) equation monic, so reduction in the basis \(1,\ldots,T^{b-1}\) commutes with base change.
In column \(j\), the product \((D_1+D_2)T^j\) has total degree \(b+j\), and the coefficient of \(T^i\) after reduction has degree \(b+j-i\) whenever it is nonzero.
Every determinant term consequently has degree \(b^2\).
On either coordinate axis the third minor reduces to \(T^b\), and multiplication in that quotient has diagonal \(u^b\) or \(v^b\), respectively.
The resulting two pure coefficients equal one over \(\mathbb Z\) and remain one after reduction modulo every prime.
This verifies the norm construction and its specialization, including the degree and reciprocal integrality properties after any permutation of the labels. [Stacks Project, Lemma 31.18.6](https://stacks.math.columbia.edu/tag/0BD2)

Fix \(x_0\) over an algebraically closed field.
For \(q\) distinct admissible ordinates, the evaluation matrix on \(1,T,\ldots,T^{q-1}\) has nonzero Vandermonde determinant.
These \(q\) evaluations vanish on the image of multiplication by \(D_1+D_2\) because each ordinate satisfies both minor equations individually.
Extending the evaluations to a basis of the dual produces a constant invertible row transformation whose first \(q\) rows are divisible entrywise by \(x-x_0\).
Thus each fiber accounts for at least its cardinality in the multiplicity of the specialized norm polynomial, even in positive characteristic or at a repeated root of the third minor.
Summing those multiplicities bounds the total number of distinct rows by \(b^2\).
For the cyclic example, the rows of the full matrix in the order \(z^{-1},1,z,z^2\) are \((u,0),(T,u),(v,T),(0,v)\).
Their three specified minors give the stated norm and \(D_1(1,i,y)=1\), which excludes both proposed complex candidates.
The number \(b^2\) is an upper bound on admissible rows, with no asserted example attaining it.

The rational and prime-field degree estimates count the embeddings of the finite separable joint coordinate field, since distinct embeddings give distinct pairs of generators and preserve the vanishing of every maximal minor.
In characteristic zero an exact-support kernel vector after extension makes each coordinate functional nonzero on the kernel over the row field by extension of a kernel basis.
Their product is a nonzero polynomial in the basis coordinates, and the infinite row field contains a point where this product is nonzero.
At any chosen finite place, rescaling a nonzero row-field witness by a right coefficient of least valuation gives integral coefficients and at least one nonzero residue.
All normalized left coordinates are units at that place, so all three survive reduction.
The rational specialization gives signs, in agreement with the primitive-coefficient argument in [Abdollahi and Taheri, Theorem 1.1 and its proof, pp. 2–3](https://arxiv.org/pdf/1905.09494#page=2).

For each embedding, vanishing of the full minors gives a complex kernel witness with actual support contained in \(B\).
The phase-adjusted Hermitian part of any compressed translation on this support splits into path matrices with off-diagonal entries \(1/2\) after diagonal conjugation.
The sine eigenvectors on a path with \(s\) vertices give largest eigenvalue \(\cos(\pi/(s+1))\leq\cos(\pi/(b+1))=c\).
Expanding the squared norm of the sum of the two largest terms therefore bounds the squared modulus of the smallest coefficient below by \((r-cM_0)^2+(1-c^2)M_0^2\).
This checks the use of the [finite-chain estimate](../../claims/Yin_C_A0099_v1.md#the-finite-chain-estimate), also when a kernel coordinate vanishes.
Every conjugate of each ratio occurs under an embedding of the row field, so elementary symmetric functions give the stated finite, effectively enumerable set for fixed \(b\).
The separate [pure-pair conclusion](../../claims/Yin_C_A0099_v1.md#statement) applies to the exact support of a complex witness.
For \(b=1\), the three output labels are distinct and no admissible row exists.
For arbitrary \(b\), the argument leaves existence of a zero product on a torsion-free group open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0101_v1.md#statement) | All fields, ordered ratios, joint count, arithmetic descent, reduction and complex coefficient bounds. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0101_v1.md#argument) | All three minors, norm and its specializations, fiber multiplicities, cyclic calibration, field and valuation arguments, chain estimate and source comparisons. |
