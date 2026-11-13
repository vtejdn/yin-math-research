---
author: Yin
---
# Two coordinate derivations exclude nonconstant normal elements of the common commutant from their joint domain

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X_1,\ldots,X_d\), \(d\ge2\), be bounded generators of a finite von Neumann algebra \(M\) with faithful normal probability trace and \(H=L^2(M)\).
Fix distinct indices \(i,j\).
On the represented star-polynomial algebra let \(\delta_i,\delta_j:H\supset\mathcal P\to H\otimes_2 H\) be closable outer derivations with \(\delta_l X_m=\delta_{lm}1\otimes1\) for \(l,m\in\{i,j\}\).
If \(a\in M\) is normal, commutes with \(X_i,X_j\), and lies in both Hilbert graph domains \(\operatorname{Dom}\overline{\delta_i},\operatorname{Dom}\overline{\delta_j}\), then \(a\) is scalar.
The coordinates \(X_i,X_j\) may be nonnormal.
Separate graph approximations for the two derivations suffice.

Consequently, for every [actual ACSY tuple](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) of length at least two, \(C^*(X)\) has no nontrivial central projection.
In particular a tracial direct sum of tuples separated by a central projection in the generated \(C^*\)-algebra cannot assemble a counterexample from two-coordinate laws with unbounded dual costs.
This applies, for example, whenever a coordinate has disjoint compact spectra on the two summands, so that its holomorphic spectral projection separates them.
For a projection only known to lie in \(W^*(X)\), the joint-domain condition is still required in this argument.

## Argument

### Commuting graph-domain elements

Write \(K_l=\overline{\delta_l}a\).
For each \(l\) choose polynomials \(a_n\) converging to \(a\) in the graph of \(\overline{\delta_l}\).
For \(m=i,j\), the inputs \([a_n,X_m]\) converge to zero in \(H\).
Deriving by the outer Leibniz rule gives the Hilbert tensor limit
\[
         K_l X_m-X_m K_l+\delta_{lm}(a\otimes1-1\otimes a).
\]
The two terms involving \(a_n\) converge in Hilbert norm since the derivative of the generator is either the unit tensor or zero.
The multipliers of \(\delta_l a_n\) are fixed bounded operators.
Closability therefore makes the displayed limit zero.
This is the [graph commutator calculation](Yin_C_F0206_v1.md#the-mixed-tensor-blocks-and-the-generator-first-sign) with \(a\) in place of a central projection.

Suppose \(a\) is nonconstant and normal.
Choose disjoint closed disks about two different points of its spectrum, of radii less than one quarter of the distance between their centers, with spectral projections \(p,q\) respectively.
Both projections have positive trace because the enclosed open neighborhoods meet the spectrum and the trace is faithful.
Each commutes with \(X_i,X_j\): a bounded operator commuting with a normal operator commutes with its spectral projections by Fuglede's theorem, used at the same bounded-operator interface in [C_F0211](Yin_C_F0211_v1.md#compression-by-small-singular-value-projections).
Compress the first leg by \(v\mapsto pvp\) and the second by \(v\mapsto qvq\).
These Hilbert projections preserve the relevant multiplier actions.
On the resulting space use product normalized corner traces and identify it linearly with \(L^2(\mathcal B)\), \(\mathcal B=pMp\bar\otimes(qMq)^{\mathrm{op}}\), by sending \(v\otimes w\) to \(v\otimes w^{\mathrm{op}}\).
Traciality makes this an isometry in the normalized tensor norms, which differ from the inherited norm by a fixed positive factor.
Put \(D_m=pX_mp\otimes q-p\otimes(qX_mq)^{\mathrm{op}}\), \(D_a=pap\otimes q-p\otimes(qaq)^{\mathrm{op}}\), and let \(k_l\) denote the compressed \(K_l\).
The graph identities now read
\[
            D_m k_l = \delta_{lm}D_a\qquad (l,m\in\{i,j\}).
\]
The two bounded terms of \(D_a\) are normal and on their respective legs differ from the corresponding disk centers by at most the disk radii.
Thus \(D_a\) is a nonzero scalar multiple of the corner unit plus an operator of strictly smaller norm and is invertible in \(\mathcal B\).

Regard the Hilbert vectors \(k_l\) as elements of the affiliated algebra of this finite corner tensor product.
Since \(D_i k_i=D_a\), \(D_i\) has a right inverse \(k_i D_a^{-1}\).
By [finite-tracial invertibility](../audits/literature/MSY23/Yin_U004.md#msy23-u004) it has a two-sided affiliated inverse.
Indeed its range support is full by the right inverse, the initial support then has full trace by polar decomposition, and spectral inversion gives the two-sided inverse.
The equation \(D_i k_j=0\) forces \(k_j=0\), contradicting \(D_j k_j=D_a\).
This proves the scalar assertion without any domain assumption on \(p,q\) or on inverses of \(D_i,D_j\).

### Separated components

Under the actual vacuum hypothesis the [dense core-tensor adjoint test](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) gives closability of both derivations.
A central projection \(e\) of \(C^*(X)\) is central in the generated von Neumann algebra by strong density.
The same cutoff result puts \(e\) in both closed domains, so the scalar assertion gives \(e=0\) or \(1\).
If the coordinate spectra on a two-part direct sum are disjoint compact sets, a function holomorphic on their disconnected neighborhood and equal to one near the first and zero near the second evaluates to the separating central projection.
Its value belongs to the unital \(C^*\)-algebra of the coordinate by holomorphic calculus.
Thus the mechanism used for [single-generator separated sums](Yin_C_F0210_v1.md#statement) cannot give an actual ACSY tuple of length at least two with such a separation.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T15:17 |
| status | open |
| reason | Fixed the obstruction to simultaneous mixed coordinate equations on separated spectral corners and its consequence for a multivariable assembly. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A normal simultaneous commutant element in two coordinate graph domains is scalar, with exclusion of central projections in the generated \(C^*\)-algebra. |
| argument | [Argument](#argument) | Independent graph approximation, spectral-corner equations, one affiliated inverse and the central cutoff application. |
| dependency | [Graph commutator](Yin_C_F0206_v1.md#the-mixed-tensor-blocks-and-the-generator-first-sign) | Leibniz calculation with a commuting graph-domain input, extended here to arbitrary bounded normal commuting elements. |
| dependency | [Bounded spectral commutation](Yin_C_F0211_v1.md#compression-by-small-singular-value-projections) | Bounded Fuglede commutation with adjoints and spectral projections of a normal operator. |
| dependency | [Finite affiliated inverses](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | A bounded element with an affiliated right inverse has a two-sided affiliated inverse in a finite tracial von Neumann algebra. |
| dependency | [Actual graph and central cutoffs](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Dense adjoint core tensors and the common graph-domain inclusion for central projections in the generated \(C^*\)-algebra. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T15:21 |
| status | proved |
| reason | Adopt the scalarity theorem and its exclusion of separated multivariable sums after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A normal simultaneous commutant element in two coordinate graph domains is scalar, with exclusion of central projections in the generated \(C^*\)-algebra. |
| argument | [Argument](#argument) | Independent graph approximation, spectral-corner equations, one affiliated inverse and the central cutoff application. |
| dependency | [Graph commutator](Yin_C_F0206_v1.md#the-mixed-tensor-blocks-and-the-generator-first-sign) | Leibniz calculation with a commuting graph-domain input, extended here to arbitrary bounded normal commuting elements. |
| dependency | [Bounded spectral commutation](Yin_C_F0211_v1.md#compression-by-small-singular-value-projections) | Bounded Fuglede commutation with adjoints and spectral projections of a normal operator. |
| dependency | [Finite affiliated inverses](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | A bounded element with an affiliated right inverse has a two-sided affiliated inverse in a finite tracial von Neumann algebra. |
| dependency | [Actual graph and central cutoffs](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Dense adjoint core tensors and the common graph-domain inclusion for central projections in the generated \(C^*\)-algebra. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0230_v1.md#whole-proof-finding) | Separate graph domains, spectral separation in the opposite algebra, finite-trace inversion and the central cutoff for nonnormal coordinates. |
