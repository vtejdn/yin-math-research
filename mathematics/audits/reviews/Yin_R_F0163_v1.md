---
author: Yin
---
# Independent complete review of finite polynomial relation compatibility

Review performed and recorded: 2026-10-14T21:05.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and inspected scope

The complete fixed [C_F0155 v1](../../claims/Yin_C_F0155_v1.md), initial decision dated 2026-10-14T21:03, and all four exact direct dependency interfaces were read.
This review covers the full statement, both proof sections, the necessary finite identities and the final finite-versus-global qualification.
It checks the scalar block reduction, rectangular finite-rank cycle, Hilbert--Schmidt trace order, actual compressed range, polynomial matrix transfer and bounded linear selection for each fixed P,i.

Root and the general branch developed the proof.
The reviewer did not participate in its scalar-null peeling, rectangular regularity or polynomial transfer, and did not read D_F0003 development for this review.
The assignment supplied the intended interfaces and proof outline before the fixed candidate.
The reviewer had previously developed the row-resolvent argument C_F0148, which is an exact input to the separate matrix criterion C_F0154.
That earlier development is not an independent review of itself.
C_F0154's fixed full proof, its stated interface, and the initial interface checks in its separately performed R_F0162 were read here.
This review relies on the accepted C_F0154 theorem only after checking all its present hypotheses; it does not supply a new independent classification for C_F0148 or replace C_F0154's independent review.
No contribution to C_F0155's new argument was made by this reviewer before the fixed text was inspected.

## Current relationship clarification

The assignment supplied proof-outline information before the fixed candidate, without retaining enough of its actual contents to distinguish a legitimate fixed short proof from additional substantive author-development context.
The exact initial relationship of this whole C151 finding is therefore unknown, not inferred self from the word outline.
The reviewer’s authorship of the accepted C144 dependency chain is separately disclosed and is not itself a self relationship to this new theorem.
All original calculations, mathematical conclusions, dates and finite-versus-global limits remain unchanged; no reviewer repair is recorded.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0155 statement](../../claims/Yin_C_F0155_v1.md#statement) | Every bounded holomorphic polynomial-matrix kernel column has the specified actual Hilbert range solution, with a complex-linear bounded choice for each fixed P,i and no uniform or global-dual conclusion. |
| [Conclusion](#conclusion) | [C_F0155 argument](../../claims/Yin_C_F0155_v1.md#argument) | Complete scalar-block reduction, all degenerate cases, rectangular finite-rank cycle and trace identity, application of the compressed inverse criterion, bounded polynomial Schur linearization and the necessary finite compatibility identities. |
| [Conclusion](#conclusion) | [C_F0154 statement](../../claims/Yin_C_F0154_v1.md#statement) | Actual bounded-column Hilbert right inverse for an affine block with regular LL* and strictly positive scalar compression; these two hypotheses are proved before use. No inverse-trace conclusion for the entire original pencil is imported. |
| [Conclusion](#conclusion) | [ACSY24-U001](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Actual represented starred-core derivations with compatible Hilbert starred values and actual vacuum imply maximal Delta without normality or reality. No full bounded-vector domain is imported from this source. |
| [Conclusion](#conclusion) | [MSY23-U002](../literature/MSY23/Yin_U002.md#msy23-u002) | Maximal Delta is equivalent to absence of nonzero finite-rank left-generator commutator cycles; Lemma 3.4's two-kernel calculation is checked explicitly with rectangular sizes and the second-slot-linear convention. No general rectangular bounded-inverse theorem is assumed. |
| [Conclusion](#conclusion) | [MSY23-U003](../literature/MSY23/Yin_U003.md#msy23-u003) | Polynomial part of Theorem 4.3 and Lemma 4.8: constant compression of an affine unit upper triangular pencil, polynomial inverse at every bounded evaluation, and rectangular entrywise assembly. No unbounded rational pivot or affiliated-to-bounded inverse inference is used. |

## 1. Scalar kernel compression and the entire zero block

The right-kernel projection p belongs to the bounded matrix algebra.
For a scalar column u the identity ||p u|| squared=u* C u follows from p squared=p and the entrywise trace.
Thus a scalar u in ker C gives a zero Hilbert column p u.
Each entry is bounded and has zero L2 norm, hence is zero by faithfulness.
The resulting bounded matrix annihilates that whole scalar column block; right multiplication by an arbitrary Hilbert or bounded entry preserves the zero identity.
Selfadjointness of p supplies the zero row block as well.
This proves the operator identity (2), not just a statement about scalar test vectors.

For v in ker B, positivity of each summand in v* B v forces p A_i* v=0 for every i at least one.
The equality p L*=0 holds as a bounded matrix identity.
Since A_i* v is scalar, the variable X_i* can be placed on the right of that scalar column before p is applied.
Thus (3) correctly gives p A_0* v=0 as well.
This step would not be valid for arbitrary operator-valued coefficient columns, but the present coefficients are scalar.

After constant unitary changes, all A_i including A_0 have zero upper-right block.
The upper row size and left column size need not agree.
Since C vanishes on the first column block, the lower scalar compression is exactly sum A_i,11 C_1 A_i,11*, and it is strictly positive on the chosen orthogonal complement of ker B.
In particular the original compression is not being declared positive on its null space.

Every actual kernel vector of L lies in the range of p, so its first column block is zero.
Conversely L(0,z)=(0,L_11 z), proving that the right kernel of L_11 is precisely p_1.
This identification is needed to use the same C_1 in C150, and it holds without any assumption about the other diagonal block L_00.

## 2. Rectangular cycles and the exact trace identity

Use the convention |f><e| x=f<e,x>, with the inner product linear in its second variable.
The row equations L_11 f=0 give T_0+sum X_i T_i=0.
In the adjoint kernel equations the coefficient is the conjugate of A_i,jk; placing that vector in the conjugate-linear first slot of <e,x> changes it back to A_i,jk.
Therefore L_11* e=0 gives T_0+sum T_i X_i=0 with exactly the same T_i.
Subtraction gives the asserted finite-rank cycle.
Both identities allow unrelated row and column sizes and arbitrary components, including dependent or zero ones.
Only the absence of finite-rank cycles is used, not the source's stronger square full-matrix criterion.

For clarity, expand the squared Hilbert--Schmidt norm of T_i as

    sum_(j,k,l,m) conjugate(A_i[j,k]) A_i[l,m]
                     <f_k,f_m> <e_l,e_j>.

Take f=p_1 e_a and e=q e_b and sum over a,b.
Traciality and the projection identities give

    sum_a <f_k,f_m> = tau(p_1[m,k]),
    sum_b <e_l,e_j> = tau(q[j,l]).

Consequently the sum is Tr(tau(q) A_i,11 C_1 A_i,11*), exactly (6).
This confirms the opposite ordering of the two Gram factors and the absence of an extra transpose or conjugate.
The matrix trace is unnormalized, consistently with C150.

Maximal Delta makes every T_i zero for i at least one.
Summing the nonnegative trace expressions gives Tr(tau(q) B_11)=0.
The matrix tau(q) is positive, and B_11 is at least a positive scalar multiple of the identity on its nonzero row space.
Hence tau(q)=0; the faithful matrix trace then gives q=0.
This proves regularity of L_11 L_11*, at the exact scope required by C150.

All vectors used here are actual Hilbert columns; the selected columns of p_1 and q are even bounded.
No derivation or canonical operator is applied to a kernel projection, and no domain theorem for those projections is assumed.

## 3. The actual affine range and its bounded linear choice

For a surviving nonzero row block, the coefficients A_i,11 are scalar, its right kernel is p_1, its scalar trace compression is C_1, its B is strictly positive, and its LL* is regular.
Thus every C150 hypothesis is verified.
Its rectangular polar formula gives a specified linear right inverse on bounded columns using Q_11 inverse square root, with a finite operator-column-norm-to-Hilbert bound.
It does not use the potentially undefined expression L_11* Q_11 inverse on an arbitrary bounded column.

If La=0, then a=(0,a_1) in these coordinates.
Therefore A_i tau(a)=(0,A_i,11 tau(a_1)), and solving (7) followed by z_0=0 solves the full affine equation, including its top rows and the L_10 term.
Constant unitaries undo the change of coordinates without altering existence or boundedness.

Entrywise trace is contractive on columns: sum |tau(a_j)| squared is at most tau(sum a_j* a_j), hence at most the squared operator column norm.
Composition with the fixed scalar A_i,11 and fixed polar right inverse is therefore complex-linear and bounded.
This establishes the exact choice needed later, rather than choosing unrelated solutions separately for each a.

The degenerate cases are also covered.
If C=0, then p=0 and the only kernel column is zero.
If the surviving row space R is zero, the derivative blocks on ker C perpendicular are zero, so the forced affine column is zero and z=0 works.
A positive-dimensional surviving row space cannot have a zero-dimensional surviving column space, since then its B_11 would be zero rather than strictly positive.
Thus no inverse of an empty or zero block is invoked.
No inverse-trace claim is made for L_00 or for the whole original pencil.

## 4. Polynomial linearization preserves all bounded domains and orders

The polynomial construction in MSY23-U003 uses only constants, generators, sums and products.
Its triangular pencils have polynomial inverses; entrywise assembly by constant coordinate inclusions gives P=U D inverse V for rectangular P.
For P of size r by m and D of size N by N, the displayed L has size (r+N) by (m+N), and J has size (m+N) by m.
Direct multiplication gives LJ=(P,0) as a vertical block column with the signs shown.
All evaluated entries of D inverse and J are bounded holomorphic polynomials.

For bounded a satisfying Pa=0, b=Ja is a bounded column in ker L.
The established affine result produces u with Lu=-A_i^L tau(b), by a choice linear and bounded in b.
Differentiating LJ, which is an identity of polynomial matrices, gives (delta_i L) J+L delta_i J.
Multiplication by a occurs afterward in the right tensor leg.
Since delta_i L=A_i^L tensor 1, its contraction is exactly A_i^L tau(Ja).
The other contraction is Lt.
This proves (9) with its stated order.
Neither delta_i a nor delta_i b is used or required.

The top block of J is the constant identity, so t_top=0.
The lower block of L(u-t)=-(g,0) gives

    (u-t)_aux = D inverse V u_top.

Substitution in the top block yields P u_top=-g.
This checks why the final answer is u_top, rather than a vector requiring subtraction of an unbounded correction.
Every multiplication in this step is bounded on the relevant Hilbert column, and D inverse is the actual polynomial inverse after evaluation.

For each fixed P and i the final selection is the top-coordinate projection of the affine solution map applied to Ja.
It is therefore a complex-linear map with norm bounded by the fixed affine constant times ||J||.
Although t is used to verify the equation, no extra bound for t is needed to bound this final selection; its actual Hilbert existence follows directly from the finite tensor derivative of J.
Zero or constant polynomial matrices are included by the same triangular construction or directly by their zero derivatives.

## 5. Necessary identities and finite versus global quantifiers

Repeated use of [E_i,X_j]=delta_ij P_Omega on bounded inputs gives [E_i,P_j]=Theta(delta_i P_j) for each holomorphic scalar polynomial.
The word Leibniz order agrees with Theta(u tensor v)a=u tau(va).
Applying E_i to the finite row sums Pa=0 therefore gives P(E_i(a_j))=-g_i(P,a).
This necessity uses only the bare unstarred commutators and linearity, with no derivative on the bounded entries a_j.

The proved selection depends on the fixed polynomial matrix and coordinate.
It does not make those selections agree when the same bounded vector appears in different systems, and its constants may change with P.
Thus the theorem removes the explicitly formulated finite range obstruction while leaving the global coherent Hilbert-valued map open.
No inverse-limit, compactness or uniform-boundedness principle is silently invoked to obtain F.
The final warning about infinite Hilbert coordinate equations correctly illustrates that logical gap and is not presented as an operator-algebra counterexample.

## Source and verification limits

C150's complete fixed proof was read and its exact compressed applicability checked; its independent R169 supplies the separate review of the matrix theorem.
ACSY-U001's small-core-to-maximal-Delta interface and MSY-U002's finite-cycle interface retain their published-source and reconstructed-proof boundaries.
This review does not newly inspect the entire ACSY or MSY PDFs.
MSY-U003's polynomial triangular construction is used at its checked bounded algebraic scope; its broader free-field foundations, rational realization questions and original Cohn proofs are not re-audited or needed as new analytic domain assertions.
The rectangular cycle and matrix contraction adaptations are verified explicitly above.
No computational test, new external theorem or formal verification is used as proof evidence.

## Conclusion

**Pass: complete fixed C_F0155 v1 independently reviewed.**
The full statement and argument, all four exact direct inputs, all matrix orders and actual domains, the degenerate blocks, and the bounded linear choice for each fixed P,i are covered by this review.
No mathematical correction was found.

The accepted scope is the stated finite holomorphic polynomial-relation range compatibility under actual ACSY derivations.
A single coherent full-domain dual, a bound uniform over polynomial matrices, and the general A-to-F implication remain unproved by this result.
This is not a Task completion review.
