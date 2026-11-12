---
author: Yin
---
# Independent review of the stabilized two-variable witness obstruction

Review time: 2026-11-11T18:12 UTC.
Human record author: Yin.
This is an initial independent whole-artifact mathematical review of [L_A0026_v1](../../ledger/Yin_L_A0026_v1.md), in its fixed working-copy revision dated 2026-11-12 (Asia/Hong_Kong).
The reviewing agent took no part in developing the argument and received the fixed candidate, the requested scope and operational metadata, without development drafts, proof-generation dialogue, proposing explanations or prior R findings.
The reviewer derived the obligations from the statement, checked the complete argument and formed initial findings before consulting the two fixed comparison materials below.
No prior review was used as evidence for this finding.

## Inputs

- [L_A0026_v1](../../ledger/Yin_L_A0026_v1.md): the entire candidate, including its exact statement, coefficient calculation, localized module argument, actual analytic premise and application limits.
- [C_A0007_v3, two-variable example](../../claims/Yin_C_A0007_v3.md#why-the-same-polynomial-repair-fails-for-a-two-variable-edge): the scalar predecessor and its witness-specific scope.
  Other parts of this fixed file were available during reading, but the present review does not re-audit its subordination theorem or complete cyclic normalization chain.
- [L_A0023_v1](../../ledger/Yin_L_A0023_v1.md#what-this-does-and-does-not-exclude): the comparison between deficient support under the specified stable shears and the different full-support, nonuniform case here.
  The relevant stable-shear statement and displayed support calculation were inspected for that comparison; the complete free-group proof is not being certified by this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete candidate](../../ledger/Yin_L_A0026_v1.md) | Entire fixed artifact, including introductory comparisons, all formulas and final limitations; the terminology observation below is retained. |
| [Whole-artifact finding](#whole-artifact-finding) | [Exact claim](../../ledger/Yin_L_A0026_v1.md#setting-and-exact-claim) | Every finite integer stabilization size, arbitrary square Laurent polynomial left factor with nonzero determinant, finite group-ring witness and strictly positive expected-Gram bound. |
| [Whole-artifact finding](#whole-artifact-finding) | [Coefficient module](../../ledger/Yin_L_A0026_v1.md#the-coefficient-module-forced-by-the-witness) | Coset coefficient support, injective cancellation, expected Gram, continuity and full-rank evaluation. |
| [Whole-artifact finding](#whole-artifact-finding) | [Local contradiction](../../ledger/Yin_L_A0026_v1.md#the-local-dimension-contradiction) | Localized coefficient module, image freeness and the incompatible residue-space dimensions, together with actual torus support. |
| [Whole-artifact finding](#whole-artifact-finding) | [Application limits](../../ledger/Yin_L_A0026_v1.md#what-this-rules-out-and-what-it-leaves-open) | Coefficient right-inverse consequence and the explicitly witness-specific obstruction; no general support-surgery or kernel impossibility. |
| [Whole-artifact finding](#whole-artifact-finding) | [Scalar predecessor](../../claims/Yin_C_A0007_v3.md#why-the-same-polynomial-repair-fails-for-a-two-variable-edge) | Exact scalar comparison only, including the stated exception for a different witness. |
| [Whole-artifact finding](#whole-artifact-finding) | [Stable-shear comparison](../../ledger/Yin_L_A0023_v1.md#what-this-does-and-does-not-exclude) | Accuracy and limits of the comparison with deficient expected support; no whole-proof re-review of L_A0023. |

## Whole-artifact finding

The complete argument proves the impossibility in (3) for every finite \(\ell\ge0\), with the specified witness \(W_\ell\), coefficient ring and matrix dimensions.
No substantive mathematical gap was found.
The result is stronger than the scalar predecessor precisely by allowing every such stabilization and every resulting square matrix polynomial left factor; it does not quantify over different witnesses for the same kernel.

The decisive obligations and checks are as follows.

1. The coefficient expectation is the actual one for the direct-product group.
   The two distinct cosets represented by \(1,s\) give coefficient matrices \(F_0,F_1\) exactly as displayed, with no cross terms after expectation.
   Thus the Gram is the diagonal matrix in (2), and the coefficient column module is exactly \((x-1,y-1)\oplus R^\ell\).
   The first diagonal symbol is positive away from the single torus point \((1,1)\), so the expected Gram has full support in the regular representation.
   Continuity and vanishing at that point give neighborhoods of positive Haar measure on which the symbol is arbitrarily small, excluding a bounded inverse.

2. For every allowed \(D\), the adjugate identity over the domain \(R\) proves injectivity on coefficient columns.
   Comparing coefficients therefore eliminates every additional coset from any finite proposed \(W_0\), and yields \(F=DF'\) and \(E_H(W_0W_0^*)=F'F'^*\).
   This step uses neither invertibility of \(D\) over \(R\) nor invertibility of its evaluation at \((1,1)\).
   The separate affiliated-invertibility remark is also valid: a nonzero Laurent polynomial has a Haar-null zero set on the torus, as follows by applying the one-variable zero-set fact to fibers outside the zero set of a nonzero coefficient polynomial.
   The adjugate divided by \(\det D\) is therefore the actual measurable matrix inverse almost everywhere.

3. The analytic lower bound implies the required algebraic local surjectivity.
   If the continuous matrix symbol \(F'F'^*\) violated its lower bound at any point, a fixed vector witnessing that violation would continue to do so on a neighborhood of positive Haar measure.
   Consequently the bound holds at \((1,1)\), and a maximal minor of \(F'\) does not vanish there.
   Its determinant is a unit in \(S:=R_{\mathfrak m}\), so the corresponding columns generate \(S^k\).
   Localizing \(F=DF'\) now gives \(\mathcal C_S=DS^k\).
   Injectivity of \(D\) persists over the domain \(S\), making this image isomorphic to the free module \(S^k\).

4. The incompatible residue-space dimensions are computed for that same module and local ring.
   The maximal ideal is \(\mathfrak mS\), and its two displayed generators span its quotient by its square.
   The derivative test is legitimate on all of \(S\), since every denominator is nonzero at the evaluation point.
   Both first derivatives vanish on the ideal square, whereas the generators have derivative vectors \((1,0)\) and \((0,1)\).
   Their residue classes are therefore linearly independent over \(S/\mathfrak mS\cong\mathbb C\).
   It follows that the residue dimension of \(\mathcal C_S\) is \(2+\ell\), while any module isomorphic to \(S^{\ell+1}\) has residue dimension \(1+\ell\).
   This contradiction also covers \(\ell=0\), and involves no cancellation or projective-module theorem.

5. The polynomial right-inverse consequence has the same precise coefficient meaning as in the cyclic normalization comparison.
   An identity \(F'Q=I_k\) over \(R\) would remain an identity at \((1,1)\), forcing the same forbidden full row rank there.
   The example with \(Y=0\) correctly demonstrates the scope limit: the alternate identity witness has identity expected Gram.
   Thus failure of the displayed factorization does not imply failure for every witness of that kernel, an Atiyah counterexample, or failure of all stabilizations or analytic repairs.

There is one nonblocking terminology defect in the final paragraph of the local-dimension section: the phrase "its local field" does not correctly name \(S\), which is a local ring.
The argument actually uses the fraction field for generic rank, the local ring for the module isomorphism and the residue field \(\mathbb C\) for the dimension comparison.
These objects are explicit in the proof, so the terminology does not invalidate its deductions.

## Source and application scope

The scalar antecedent and the stable-shear comparison have the different scopes stated in the candidate.
Neither supplies an omitted premise of the local module contradiction, which is proved directly in L_A0026.
The elementary localization and derivative calculations were checked as written; no unverified projective-module, cancellation or global regular-local-ring theorem is being imported.
The claim that this abelian example supplies no forbidden group-matrix rank is consistent with the usual torus calculation: a maximal nonzero Laurent minor gives the same integer matrix rank almost everywhere.

No external literature or historical-priority search was performed, and this finding makes no novelty claim or whole-library source-completeness claim.
No unresolved external theorem is needed for the stated coefficient-module obstruction.
The recorded mathematical conclusion does not certify the separate subordination theorem, the whole stable-shear proof, a future transformation that changes the coefficient module, or a correction formula for the analytic nullity after such a transformation.
