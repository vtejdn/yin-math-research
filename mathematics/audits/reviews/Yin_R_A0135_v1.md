---
author: Yin
---
# Phase rigidity and translation-chain bounds for three left labels

At 2026-11-21T05:03 UTC a separate reviewer for Yin independently checked the statement, all proof sections and the source comparisons of C_A0099_v1.
The reviewer took no part in the proof development and received the fixed claim and the review assignment without development notes or a prior verdict.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0099_v1.md#statement) | All conclusions for finite exact supports, three distinct left labels and an actual complex zero product in a torsion-free group. |
| [Whole finding](#whole-finding) | [Maximal-modulus argument](../../claims/Yin_C_A0099_v1.md#the-maximal-modulus-argument) | Pure-pair rigidity, restriction to components and distinct forced triple outputs at maximal coefficients. |
| [Whole finding](#whole-finding) | [Saturation](../../claims/Yin_C_A0099_v1.md#saturation-forced-by-three-rows) | Real deformations, integral saturation and its rank, phase orders and the exact normalized solution count. |
| [Whole finding](#whole-finding) | [Signs and finite characters](../../claims/Yin_C_A0099_v1.md#signs-and-finite-characters-are-separate-requirements) | Sign extension, the odd-index case, group-character scope and the characteristic-two example. |
| [Whole finding](#whole-finding) | [Finite-chain estimate](../../claims/Yin_C_A0099_v1.md#the-finite-chain-estimate) | Numerical radius on each path, the norm identity, strict triangles and the four-vertex example. |
| [Whole finding](#whole-finding) | [Literature and remaining scope](../../claims/Yin_C_A0099_v1.md#literature-and-remaining-scope) | The stated uses of AT21 and ASM19, and the hypotheses delimiting the mixed-fiber conclusions. |

## Whole finding

In an actual product fiber at most one cell comes from each row, and its columns are distinct by group cancellation.
At a column maximizing \(|v_b|\), a row of strictly largest modulus cannot cancel with one other term.
If exactly two rows attain the largest modulus, a pair containing a maximal term from one must have a maximal partner from the other.
With only pair fibers this would make the nonidentity translation \(g_j^{-1}g_i\) permute the finite nonempty set \(B_{\max}\).
Any periodic point of that translation implies finite order by cancellation.
This proves equality of the three moduli for pure pairs, after which the modulus equations propagate along each column component.
The restriction to a component retains both cells of every incident fiber.

In the tied case with triples allowed, write \(x=g_j^{-1}g_i\).
At the last vertex \(c\) of a maximal \(x\)-chain in \(B_{\max}\), a pair at \(g_i c\) would require \(xc\in B_{\max}\) or a right coefficient of modulus greater than \(M_0\) in the third row.
At the first vertex \(d\) a pair at \(g_jd\) similarly requires \(x^{-1}d\in B_{\max}\) or an excessive right modulus.
An equality \(g_i c=g_jd'\) between any two forced outputs of opposite types requires \(xc=d'\in B_{\max}\), contradicting the definition of \(c\).
For outputs of the same type, cancellation recovers the endpoint.
This verifies the count even for one-vertex chains.

For a real functional annihilating \(L\), the two entries in a pair have the same deformation exponent.
Applying left-modulus equality before and after the deformation with scale factor two shows that the functional kills all row differences.
The real double-annihilator identity places these differences in the real row span of the integer relation matrix.
Gaussian elimination over \(\mathbb Q\) places each integral vector of that span in its rational span, hence in \(S\).
Each edge then gives a column difference in \(S\), and paths supply all differences within a component.
Conversely the row sum and all component sums vanish on every relation and on its saturation.
Fixing one reference label in each of these \(1+t\) blocks gives an integral basis for the subgroup cut out by those sums, consisting of the differences with the corresponding reference labels.
This proves (2) and gives rank \(2+|B|-t\).

The given solution restricts to a character \(\chi\) with value \(-1\) on each oriented pair difference, including after reversing the orientation.
Since \(eS\subset L\) and \(\chi^2=1\), all prescribed ratios have order dividing \(2e\).
The original character supplies one extension on \(S\).
The quotient of any two extensions factors uniquely through \(S/L\), whose finite cyclic factors each have as many complex characters as their orders.
The reference labels span an integral complement to \(S\), and normalization assigns one to each basis vector of that complement.
This gives precisely \([S:L]\) normalized solutions and uses the assumed existence of a full-support solution.

A sign extension factors through \(M/2M\).
Its necessary and sufficient compatibility condition is triviality of \(\chi\) on the kernel \(L\cap2M\) of the reduction map from \(L\), since a functional on the image extends over \(\mathbb F_2\).
When \([S:L]\) is odd, \(2m\in L\) implies \(m\in S\) and then \(m\in L\), which proves the stated sufficient condition.
The argument assigns characters to a lattice of coefficient labels and supplies no verification of additional relations in \(G\).
For the example with seven cyclic group elements, the characteristic-two factors multiply to \(1+z^7\).
Over \(\mathbb C\) a cubic on exponents \(0,1,3\) that vanished at three distinct seventh roots would force their sum to vanish, contradicting the minimal polynomial of a primitive seventh root.
Its partner of degree at most four would have to vanish at the five or more remaining roots.
This confirms the asserted field distinction in the stated torsion example. [C93](../../claims/Yin_C_A0093_v1.md#a-fiber-with-exceptional-characteristic)

For \(x=g_i^{-1}g_j\), the compression to \(B\) splits into path shifts because \(x\) has infinite order and \(B\) is finite.
On a path of \(q\) vertices a diagonal change of phase puts every rotated Hermitian part in the form of the adjacency matrix divided by two.
The sine eigenvectors give maximum eigenvalue \(\cos(\pi/(q+1))\), including zero for \(q=1\).
Maximizing over phase gives the absolute quadratic-form bound, attained for the shift on a longest path.
Expanding \(\|a_i g_i\beta+a_j g_j\beta\|_2^2=r_k^2\|\beta\|_2^2\) gives the cross term with inner product \(\langle\beta,\lambda(x)\beta\rangle\).
Its absolute value is bounded by the path estimate, and the cosine is strictly smaller than one.
Thus \((r_i-r_j)^2<r_k^2<(r_i+r_j)^2\).
For \(i=2,j=3\) in the example, \(161/200>1/\sqrt{2}\) excludes \(m_{23}\le3\).

The rational three-term theorem permits all fiber multiplicities and applies prime reduction after clearing denominators and taking primitive integral factors.
The complex regularity criterion assumes \(2\|\alpha\|_2^2\ge\|\alpha\|_1^2\) and has no right-support parameter.
These are accurate comparisons with the inspected statements and, for the rational result, its Section 2 argument. [AT21, Theorem 1.1](https://arxiv.org/pdf/1905.09494#page=2) and [ASM19, Theorem 1.1](https://arxiv.org/pdf/1905.00951#page=2)

The complete argument establishes the stated necessary conditions.
The projective pruning and previously used lattice-character arguments serve as comparisons, and the path eigenvalue calculation can be checked directly on the scalar path.
For a triple equation, arbitrary deformation exponents on its three terms need not preserve cancellation.
Accordingly the phase classification applies to pure pairs, and the general zero-divisor problem in the [A0002 contract](../../tasks/Yin_T_A0002_v1.md#contract) remains open.
