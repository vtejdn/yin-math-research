---
author: Yin
---
# Independent review of the nonsquare-residue completion

Review performed at 2026-11-11T19:55 for Yin.
The principal input is the whole fixed [L_A0028_v4](../../ledger/Yin_L_A0028_v4.md), including its source-use claims and limitations.
The reviewer was outside substantive proof development and received only the fixed input, necessary dependency locators, review assignment and execution metadata.
No development drafts, proof-generation dialogue, mathematical development summary or previous review conclusions were supplied or consulted before initial findings were formed.
The reviewer made no mathematical repair to the candidate.

The reviewer directly read all of [L_A0028_v2](../../ledger/Yin_L_A0028_v2.md), [L_A0028_v3](../../ledger/Yin_L_A0028_v3.md) and the [T_A0001 contract](../../tasks/Yin_T_A0001_v1.md#contract).
After forming initial findings, the reviewer read [R_A0037_v2](Yin_R_A0037_v2.md#whole-input-finding) and [R_A0037_v3](Yin_R_A0037_v3.md#whole-input-finding).
Their unchanged coverage is compatible with the present use and is reused for the older full Promislow-model chain and the earlier valuation limitation.
This review directly checks the interfaces below without claiming a fresh audit of every earlier group-theoretic, affiliated-algebra or Albert-form prerequisite.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-input finding](#whole-input-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-input finding](#whole-input-finding) | [L_A0028_v4](../../ledger/Yin_L_A0028_v4.md) | Whole fixed version: field embedding, valuation, residues, square classes, isotropic vectors, formal recursion, general square-root condition, non-descent, source use and bounded conclusion; the title accurately states isotropy. |
| [Whole-input finding](#whole-input-finding) | [Original quadratic form](../../ledger/Yin_L_A0028_v2.md#the-complete-exterior-square-equation) | Direct check that the six coefficients and rational field used in v4 are exactly those of equation (17), without specialization of the original independent variables. |
| [Whole-input finding](#whole-input-finding) | [Original rational equivalence](../../ledger/Yin_L_A0028_v2.md#why-the-quadratic-condition-is-necessary-and-sufficient) | Direct check of the anisotropy and mixed-norm interface; R_A0037_v2 is reused for the unchanged complete supporting chain. |
| [Whole-input finding](#whole-input-finding) | [Earlier valuation limitation](../../ledger/Yin_L_A0028_v3.md#every-henselian-valued-extension-with-quadratically-closed-residue-loses-anisotropy) | Direct check of the necessary nonsquare-unit condition and simple-root lifting property, with unchanged full coverage reused from R_A0037_v3. |

## Whole-input finding

No mathematical gap or outstanding source-use defect was found in the whole reviewed input.
The title and body accurately state isotropy, without asserting that the form is hyperbolic.
The construction gives an injective valued-field extension preserving U as a unit with nonsquare residue, but both the odd residue form and the full form have the displayed exact isotropic vectors.
The square root required by the constructed vector is absent from the rational field, and the normalized isotropic line does not descend.
The broader square-root condition and its henselian specialization are valid.
The inspected external passage supports the attributed comparison, with no source proof substituted for the explicit local lift.

The result excludes this completion as an anisotropy certificate and establishes that the earlier necessary condition on U is insufficient.
It does not settle rational anisotropy, exclude every mixed norm solution, establish a new group class or complete T_A0001.
This review supplies neither a new independent proof of known division coverage nor proof-assistant verification.

## Field and residue calculation

Setting \(Z:=T/V\) is a birational change of independent variables with inverse \(T=ZV\).
The image of L is therefore exactly \(\mathbb C(U,Z,V)\) inside \(E=\mathbb C(U,Z)((V))\), with no imposed algebraic relation among the original three generators.
Every nonzero rational function in V has a Laurent-series expansion over \(k=\mathbb C(U,Z)\), giving the asserted injection.
The V-adic valuation has valuation ring \(k[[V]]\), residue field k and residue characteristic zero.

The U-adic valuation on \(\mathbb C(Z)(U)\) assigns U value one, proving its residue nonsquare.
The elements \(U-Z^2\), \(1-U\), \(1-V\) and \(1-Z^2V/U\) are nonzero in the stated rational fields.
Thus every claimed unit has V-value zero, and D has residue one; a specialization such as \(U=Z^2\) is inadmissible.

The original six coefficients are \(d,-Ud,-U,UV,e,-eW\).
Substitution gives \(d=4V(U-Z^2)/(UD)\) and \(-eW=-4Z^2V/(1-U)\).
Grouping the coordinates \((R_1,S_1)\) and \((H_1,H_2,R_2,S_2)\) gives exactly (3), and reduction gives (4), without unrecorded coordinate scaling.

A nonzero zero of the even residue form must have \(s\ne0\) and would give \(r^2/s^2=4/(1-U)\).
Its valuation at \(U=1\) is minus one, so that form is anisotropic.
For the odd residue form, substitution of (5) gives \(-4A^2/U+4A^2/U=0\), and its second coordinate is one.
The earlier L_A0028_v3 sign cases for v(U) make a nonsquare residue of the unit U necessary for a henselian anisotropy certificate in residue characteristic different from two.
The present extension satisfies that condition but has the displayed zero, proving insufficiency without using a converse.

## Exact lift and generalized square-root condition

For \(r=1+\sum_{n\ge1}c_nV^n\), the coefficient of \(V^n\) in \(r^2\) is \(2c_n+\sum_{j=1}^{n-1}c_jc_{n-j}\).
Formula (6) therefore proves existence and uniqueness coefficient by coefficient.
Characteristic zero permits division by two, and the constant coefficient one makes r invertible.
No analytic convergence or finite-jet extrapolation is used.

The two possibly nonzero summands in (7) are
\[
 d(Z^2-U)=-\frac{4VA^2}{UD},
 \qquad
 UV\left(\frac{2A}{Ur}\right)^2=\frac{4VA^2}{UD}.
\]
They cancel exactly because \(r^2=D\).
The H2-coordinate is one, and the odd coordinates reduce to (5).

For any extension containing \(r\ne0\) with \(r^2=(1-V)(1-W)\), the coordinates in (9) are defined because V is nonzero.
The identity \(T^2/V^2-U=-U(V-W)/V\) gives H-term \(-4U(V-W)^2/[V(1-V)(1-W)]\), and the R2-term is its additive inverse.
If \(v(V)>0\) and \(v(W)>0\), the right side of the square equation is a unit with residue one.
In residue characteristic different from two, the residue root one of the monic polynomial has nonzero derivative two.
The stated henselian simple-root property applies, with no discrete or rank-one assumption needed for this generalized claim.

## Rational and projective non-descent

View L as \(\mathbb C(U,T)(V)\).
At the divisor \(V-1\), UV and \(UV-T^2\) reduce to U and \(U-T^2\), both nonzero in the coefficient field, so they are units.
Hence \((1-V)(1-W)\) has valuation one and cannot be a square in L.
This is the same square-class obstruction after the birational parameter change because \(Z=T/V\) belongs to L.

The numerator \(2A/U\) is nonzero in the embedded rational field.
If \(2A/(Ur)\) were rational, division would recover r, contradicting the nonsquare calculation.
Any rational projective representative of the displayed line could be normalized by its nonzero H2-coordinate and would reproduce the original vector.
Thus neither this vector nor its line descends.
The argument gives no conclusion about another possible rational isotropic line.

## Sources and scope

The reviewer inspected the title page and the complete printed p. 4, PDF p. 16, of [Kne09, preliminary version dated 22 November 2009](../../literature/pdf/Kne09--preliminary.pdf#page=16).
The author, title, translator and preliminary date match the canonical bibliography.
The theorem page was read from the original PDF and visually inspected.
Its Springer 1955 theorem concerns a complete discretely valued field of residue characteristic different from two and a nondegenerate symmetric bilinear form decomposed into a unit part and a uniformizer-times-unit part.
The necessary anisotropy statement and converse existence statement are represented accurately in the candidate.
Here E is complete, V is a uniformizer, the summand coefficients are units and all diagonal coefficients are nonzero.
In characteristic zero, the associated diagonal symmetric bilinear form and Q have the same isotropic vectors.
Thus the theorem applies to the comparison, while (6)--(8) establish existence independently.
The original Springer proof and the rest of Knebusch's monograph were not audited; no exhaustive priority or novelty search is claimed.

Known coverage was checked against [CG23 arXiv v1, Section 3.1, pp. 4--5, and Proposition 5.1, pp. 10--11](../../literature/pdf/CG23--arxiv-v1.pdf#page=4).
Section 3.1 invokes the torsion-free virtually abelian domain theorem before introducing the Ore division field; Proposition 3.3 identifies the relevant complex closures with it.
The Promislow passage supplies the finite translation extension and the four-dimensional translation-field algebra.
These are comparisons with existing coverage, and none is a premise for the new isotropic vectors.
The underlying cited division theorem and the whole CG23 paper were not re-audited.

The inherited L_A0028_v2 equivalence concerns only the original rational field L.
Anisotropy in an extension would imply anisotropy in L by injectivity, but the present isotropy and non-descent imply neither rational isotropy nor rational anisotropy.
The all-groups and all-finite-rectangular-complex-matrices quantifiers of T_A0001 remain untouched.
The candidate correctly retains the unresolved global rational obstruction and does not treat this completion calculation as a solution of that contract.
