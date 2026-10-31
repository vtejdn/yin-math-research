---
author: Yin
---
# Normal strong domains, bare adjoint tuples and canonical compatibility

Date: 2026-10-14T16:31.
Human author Yin.
Root developed and self-checked this assembly under the separate normal-domain investigation, reusing C_F0070, C_F0072, C_F0073 and C_F0031 at their recorded scopes.
The selected decision below records the separately organized fixed-material review and its adoption.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be finite with faithful normal probability trace, H=L2(M,tau), Omega=1, and let X be a finite bounded generating tuple.
Write \(X^*:=(X_1^*,\ldots,X_d^*)\) and \(A_X^*:=\mathbb C\langle X,X^*\rangle\) for the represented star algebra.
Inner products are linear in the second variable.
- S(X) means that densely defined D_i satisfy M Omega subset Dom D_i intersect Dom D_i*, and [X_j,D_i]=delta_ij P_Omega on M Omega.
- F(X) requires only complex-linear D_i:M Omega -> H with those commutators, without an adjoint-domain or closability premise.
- A(X) means that outer derivations delta_i:A_X* -> H tensor_2 H satisfy delta_i(X_j)=delta_ij 1 tensor 1 and actual 1 tensor 1 in Dom delta_i*, using A_X* Omega as Hilbert-space core domain.
The outer actions are a dot (u tensor v) dot b=au tensor vb.
All three conditions are existential.

1. For arbitrary tuples, S(X) iff S(X*).
2. For normal tuples,
\[
 \mathsf S(X)\quad\Longleftrightarrow\quad
 \mathsf F(X)\ \text{and}\ \mathsf F(X^*).
\]
Equivalently, the unique starred derivations supplied by F(X) have both contractions bounded from the operator norm to H.
3. Consequently the two universal statements on normal generating tuples, A implies S and A implies F, are equivalent.
   This is a statement about the entire class, not a pointwise inference from A(X) and F(X) alone.
4. Under S(X) with X normal, every supplied system can be compared with the canonical generator-first operators on all bounded vectors.
   Set eta_i=D_i Omega.
   For the unique actual starred derivatives delta_i, put
\[
 E_{i,0}=(\mathrm{id}\otimes\tau)\delta_i
 \quad\text{on }A_X^*\Omega,\qquad
 \widehat D_i=-\overline{E_{i,0}}.
\]
Then both canonical domains contain M Omega and, for a in M,
\[
 \widehat D_i(a\Omega)=D_i(a\Omega)-a\eta_i,\qquad
 \widehat D_i^*(a\Omega)=D_i^*(a\Omega)-a\eta_i^*.
\]
For every bounded regular fraction pair Q=(s,a,b,t) for u=s^{-1}a=bt^{-1} in L0(M), the fraction commutator Gamma[Q,D]=sDb-aDt has its literal domain {xi in H: b xi,t xi in Dom D}.
The two fraction commutators agree on M Omega.
If either has finite rank on its entire defined domain, both have the same bounded finite-rank closure and the same rank.
Equality of the two unclosed operators on their potentially different natural domains is not asserted.

## Argument

### Adjoint stability of S

For S(X), each D_i is closable since Dom D_i* contains the dense M Omega.
Testing the original dual identity against a,b in M gives
\[
 [D_i^*,X_j^*]b\Omega=\delta_{ij}P_\Omega b\Omega .
\]
Both compositions are defined because X_j* preserves M Omega.
Define D'_i=-D_i*.
Its domain contains M Omega and its adjoint is -D_i**, whose domain contains Dom D_i and hence M Omega.
Thus it satisfies the S(X*) conditions.
Apply the same argument to X* for the reverse implication.
No normality is used.

It follows immediately that S(X) implies F(X) and F(X*).

### Converse for normal tuples

Assume F(X) and F(X*), with every X_j normal.
C_F0070 Part A supplies the unique starred derivatives delta_i for X and bounded right contractions R_i=(id tensor tau)delta_i.
Apply the same input to X*.
C_F0073 Part B identifies the resulting normalized right contractions on the starred core with J L_i J, where L_i=(tau tensor id)delta_i and J(a Omega)=a* Omega.
Its precise statement is that, under normal F(X), F(X*) is equivalent to boundedness of all L_i for the operator norm on the starred core.

Thus both R_i and L_i have the bounds required by C_F0072.
That result supplies actual vacua and the closure E_i of the specified canonical right contraction with
\[
 M\Omega\subseteq\operatorname{Dom}E_i\cap\operatorname{Dom}E_i^*.
\]
Its source core has [E_i,X_j]=delta_ij P_Omega.
To pass this relation to M Omega, take bounded starred-polynomial approximants converging strongly-star to a bounded a.
The two contraction bounds supply a common weakly convergent subnet of the images for a and X_j a; the weakly closed graph and the bounded generator commutator identify the limits.
Equivalently, C_F0070 Part B gives the canonical generator identities on M Omega once the full domain is restored.
Set D_i=-E_i.
This proves S(X).

No vacuum premise was imposed on the original bare systems.
No arbitrary supplied bare system is identified with the canonical closure by this direction.

### Universal implication and counterexample reduction

C_F0073 Part A proves A(Y) iff A(Y*) for every bounded generating tuple.
Suppose A implies F for every normal tuple.
For normal X with A(X), both A(X) and A(X*) hold and hence both F(X) and F(X*) hold.
The preceding equivalence yields S(X).
The reverse universal implication follows from S implies F.

In counterexample form, if a normal X satisfies A(X) but not S(X), at least one of F(X),F(X*) fails.
The corresponding tuple X or X* is normal, satisfies A, and refutes A implies F.
Conversely a normal A-but-not-F example is automatically A-but-not-S.

This reduction does not assert that F(X) alone is adjoint stable, or that A(X) plus F(X) implies S(X) for a fixed tuple without F(X*).

### Canonical values for a supplied strong-domain system

Assume S(X) and normality.
C_F0070 Part A gives the unique delta_i; Part C gives its actual vacuum
\[
 \xi_i=-D_i^*\Omega+\eta_i^*.
\]
Thus any ACSY derivations with the prescribed values coincide with these delta_i by uniqueness.

For one index, define on M Omega
\[
 E^{\mathrm{full}}(a\Omega)=-D(a\Omega)+a\eta,\qquad \eta=D\Omega.
\]
The right-multiplication operator a Omega maps to a eta has adjoint values b Omega maps to b eta* on M Omega.
Indeed for bounded a,b,
\[
 \langle a\eta,b\rangle
 =\tau(\eta^*a^*b)=\tau(a^*b\eta^*)
 =\langle a,b\eta^*\rangle.
\]
The tracial pairings are legitimate since eta is in L2 and the other factors are bounded.
Consequently M Omega is in Dom(Efull)*, with
\[
 (E^{\mathrm{full}})^*(b\Omega)=-D^*(b\Omega)+b\eta^*,
\]
so Efull is closable.

The core E0 is exactly Efull restricted to A_X* Omega by C_F0070.
Part B of that result gives M Omega subset Dom Ecan, where Ecan=closure E0, since the bare full-domain system is present and A holds.
Because
\[
 E^{\mathrm{can}}\subseteq\overline{E^{\mathrm{full}}},
\]
the two operators agree at every a Omega in M Omega, where both are defined.
Also
\[
 (E^{\mathrm{full}})^*\subseteq(E^{\mathrm{can}})^*.
\]
This proves the two displayed canonical formulas after negation, including the actual adjoint domains.
In particular this fills precisely the stronger-interface equality not asserted for an arbitrary unclosable bare extension in C_F0070.

### Fractions and exact finite-rank transfer

Write Q=(s,a,b,t) for u=s^{-1}a=bt^{-1}, with bounded coefficients and regular s,t.
For z in M, the canonical normalization formula gives
\[
 (sDb-aDt)z\Omega-(s\widehat D b-a\widehat D t)z\Omega
 =(sb-at)z\eta=0.
\]
Both fraction operators have dense domain containing M Omega.
Their adjoints contain M Omega: the tested adjoint expression is b* D* s*-t* D* a*, and analogously for the canonical system.
Thus both are closable.

Use the accepted finite-rank closure fact from [C_F0031, Part (1)](Yin_C_F0031_v1.md#statement), with the established source identified as [Kat95 Problem III.5.18](../audits/literature/Kat95/Yin_U001.md#selected-citation-check): a densely defined closable finite-rank operator has a bounded finite-rank closure, of the same rank.
If either fraction operator has finite rank, call that closure T.
Its restriction to the dense M Omega agrees with the other fraction operator there.
Hence the closure of the other contains the graph of T.
Since T is defined on all H and the other closure is an operator, that closure must equal T.
The common restriction has the same finite-dimensional range as T because its range is a dense linear subspace of that finite-dimensional range.
The other unclosed operator therefore also has exactly that range and rank.

The argument is symmetric and applies to each i and each Q.
It does not assert pairwise equality for different Q, nor equality of the natural domains for D and the canonical dual.

## Exact inputs and self-review boundary

- [C_F0070](Yin_C_F0070_v1.md#statement): normal starred uniqueness, actual vacuum from Omega in Dom D*, and restoration of the canonical right full domain under A and F.
- [C_F0072](Yin_C_F0072_v1.md#statement): two contraction bounds imply actual canonical operator and adjoint full domains.
- [C_F0073](Yin_C_F0073_v1.md#statement): A is adjoint stable and, for normal F, left contraction boundedness iff F(X*).
- [C_F0031](Yin_C_F0031_v1.md#statement): finite-rank closure and preservation of the actual range/rank.
  The known-result attribution and exact source-reading scope are retained at the Kat95 interface cited above.
  The fraction-adjoint domain test and full-graph comparison are reconstructed here.

The author self-checked adjoint signs and actual domains, the two contraction input, the universal rather than pointwise implication, the tracial right-multiplication adjoint, canonical core inclusions and the finite-rank full-graph cancellation.
The initial decision retained this preparation state; the subsequent decision records the separate full review and adoption.
No implication A implies F for arbitrary normal tuples, F implies A for arbitrary normal tuples, or either general nonnormal implication is proved here.


## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14T16:31 |
| status | open |
| reason | Complete assembly and canonical compatibility proof retained; separate fixed-material review is pending. |

Recorded authoring stage: proof draft.
Recorded review label: self-reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary-tuple S adjoint stability, normal S versus F and adjoint F, universal ACSY implication reduction and canonical full-domain/finite-rank compatibility. |
| argument | [Argument](#argument) | All five proof sections, with exact domains, signs, quantifiers, graph inclusions and finite-rank transfer. |
| dependency | [C_F0070](Yin_C_F0070_v1.md#statement) | Normal starred uniqueness, actual vacuum, and canonical right full-domain restoration under A and F. |
| dependency | [C_F0072](Yin_C_F0072_v1.md#statement) | Two contraction bounds give actual vacua and both canonical full domains. |
| dependency | [C_F0073](Yin_C_F0073_v1.md#statement) | ACSY adjoint stability and the exact normal left-contraction versus adjoint-tuple F equivalence. |
| dependency | [C_F0031](Yin_C_F0031_v1.md#statement) | Densely defined closable finite-rank operators have bounded finite-rank closures with unchanged range and rank. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T16:39 |
| status | proved |
| reason | Independent complete review verified all four conclusions, both actual canonical domains, universal quantifiers and finite-rank compatibility on the full natural fraction domains. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary-tuple S adjoint stability, normal S versus F and adjoint F, universal ACSY implication reduction and canonical full-domain/finite-rank compatibility. |
| argument | [Argument](#argument) | All five proof sections, with exact domains, signs, quantifiers, graph inclusions and finite-rank transfer. |
| dependency | [C_F0070](Yin_C_F0070_v1.md#statement) | Normal starred uniqueness, actual vacuum, and canonical right full-domain restoration under A and F. |
| dependency | [C_F0072](Yin_C_F0072_v1.md#statement) | Two contraction bounds give actual vacua and both canonical full domains. |
| dependency | [C_F0073](Yin_C_F0073_v1.md#statement) | ACSY adjoint stability and the exact normal left-contraction versus adjoint-tuple F equivalence. |
| dependency | [C_F0031](Yin_C_F0031_v1.md#statement) | Densely defined closable finite-rank operators have bounded finite-rank closures with unchanged range and rank. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0048_v1.md#conclusion) | All four statements, five argument sections, four direct dependency interfaces and the precise canonical fraction compatibility. |

