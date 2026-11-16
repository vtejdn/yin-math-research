---
author: Yin
---
# The Nielsen–Soelberg eight-by-eight product table

A separate reviewing agent inspected the complete [fixed Claim](../../claims/Yin_C_A0031_v1.md) for Yin on 2026-11-16T16:50 UTC.
The reviewer did not develop the argument or receive exploration notes, development discussion, author explanations or an earlier verdict.
The two cited ledger proofs, the authors' presentation and the source and execution of the finite verifier were inspected directly.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0031_v1.md#statement) | Four-coset geometry, shared differences, ambient group and full-support nonvanishing over a commutative domain. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0031_v1.md#argument) | Source hypotheses, both coset orientations, exact fiber certification and the coefficient contradiction. |
| [Whole-argument finding](#whole-argument-finding) | [Actual fibers](../../ledger/Yin_L_A0041_v1.md#the-actual-fibers) | Source multiplicity data and the named three-term fiber. |
| [Whole-argument finding](#whole-argument-finding) | [Forced sign](../../ledger/Yin_L_A0041_v1.md#the-forced-sign) | Ratios of three binomials, final triple and characteristic two. |
| [Whole-argument finding](#whole-argument-finding) | [Image certificate](../../ledger/Yin_L_A0041_v1.md#certification-of-the-three-double-fibers) | Finite representation of the defining presentation and its exact three two-cell fibers. |
| [Whole-argument finding](#whole-argument-finding) | [Two covers](../../ledger/Yin_L_A0042_v1.md#the-two-covers) | Word derivations, exponents, abelianization and coset-separating character. |
| [Whole-argument finding](#whole-argument-finding) | [Double cosets and intersections](../../ledger/Yin_L_A0042_v1.md#double-cosets-in-the-product-and-in-the-rank-test) | Mixed cell multiplicity, repeated differences, Heisenberg image and original conjugate subgroup intersections. |
| [Whole-argument finding](#whole-argument-finding) | [Verifier reproduction](../../computations/programs/Yin_J_A0002/readme.md#reproduction) | Program, relations, complete enumeration of the finite image table and actual rerun. |
| [Whole-argument finding](#whole-argument-finding) | [Author manuscript edition](../literature/NS24/readme.md#author-manuscript) | Section 4, page 8, including (4.1), (4.2), the two-generator presentation, multiplicities and attribution. |

## Whole-argument finding

The author manuscript identifies \(x=a_2,\ y=b_5\), supplies both group presentations, and reports torsion-freeness, eight distinct generators on each side, and the equivalence of the complete collision table to one with two triples and all other fibers of size two.
The same page states the prior nonvanishing result and attributes its verification to Soelberg's thesis.
Those source results are accepted at their stated scope from [Section 4, p. 8](../../literature/pdf/NS24--author.pdf#page=8).
This inspection used the two presentations and the reported complete multiplicities without repeating the authors' full rewriting or torsion computations.

From \(t=(xy)^2\) and \(x^{-1}tx=(yx)^2=t^{-1}\), one gets \(w=t^{-1}x^{-1}\) and \(w^2=x^{-2}\).
The second relator also gives \(xy^{-1}x=t^{-1}y\).
Substituting these in the fourteen cell identities recovers the row and column words and the displayed Laurent exponents.
For instance \(b_6=y^{-1}x^{-2}, b_7=x^{-1}b_6\), so \(b_4^{-1}b_6=b_5^{-1}b_7=w^{-1}x^{-2}=w\) as required on the column side.
The abelianized relation vectors are \((4,4)\) and \((4,0)\), giving \(C_4\oplus C_4\).
The homomorphism \(x\mapsto-2,\ y\mapsto1\pmod4\) kills \(w\) and takes four distinct values on each list of representatives.
Torsion-freeness and the nontriviality of \(x\) give infinite order of \(w\).
Thus the four right cosets for \(A\) have widths \(0,2,1,1\), and the four left cosets for \(B\) have widths \(2,0,1,1\) in the displayed orders.
The shared differences include the generators \(x=a_1^{-1}a_2=b_1b_2^{-1}\) and \(y=a_4^{-1}a_8=b_5b_1^{-1}\).

The mixed double coset of the row and column of greatest width contains the four indicated coset pairs by the relations \(12=23,\ 21=55,\ 33=66\).
All four have residue two and each row can meet only one column of that residue, so this is the exact count of coset pairs.
On testing the individual factors the proper right-coset lists are those of \(A\) and \(B^{-1}\).
Both start with \(1,x\), whose two ordered differences give the same double coset because \(x^{-2}\in H\).

Independent multiplication using the given Heisenberg group law and sign action gives central Heisenberg coordinates \(-1,1,1\) for the translations \((xy)^2,(yx)^2,(xy^{-1})^2\), respectively.
Thus both group relators hold in the image.
For the four conjugate squares the resulting \((p,c)\) vectors, all with \(q=0\), are \((-2,0),(-2,0),(2,-2),(2,2)\) on the row list.
The column-inverse list interchanges the last two vectors.
Nonparallel vectors generate cyclic groups with trivial intersection in this abelian plane, and every conjugate square has infinite order in the image.
This rules out a nonidentity common power for any of the five pairs with nonparallel vectors.
On the parallel pair the conjugate generators have odd powers with third coordinate \(1\) and \(-1\), respectively.
An odd power also has a nonidentity sign pair, so it cannot match an even power.
The even-power subgroups coincide already in \(G_3\) by \(w^2=x^{-2}\).
This proves the exact intersection on that pair and triviality of the other five intersections on each side.

The [finite verifier](../../computations/programs/Yin_J_A0002/verify.py) uses affine permutations modulo three and an additive coordinate modulo four.
Its relator list agrees with all fourteen tuples in (4.1).
An independent execution with standard Python completed successfully, checking both identity assignments and every relator, and enumerating all sixty-four cells.
The selected image fibers were exactly \(\{15,34\},\{62,71\},\{65,74\}\).
Actual fibers refine image fibers, and the published absence of singleton fibers forces each of these three pairs to remain intact.
The relations give \(b_2=a_3=x^{-1},\ b_3=x^{-2}\), so \(12=23=31\), and the published multiplicity bound three exhausts this fiber.
Finally the binomial equations force the ratio of the coefficients at \(12\) and \(31\) to be \(-1\).
Their sum vanishes in the fraction field in every characteristic, leaving the nonzero coefficient at \(23\).
This proves the claimed nonvanishing for the specified full supports.
