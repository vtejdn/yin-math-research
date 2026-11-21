---
author: Yin
---
# Regular ranks from modular twists in the Gardam group

## Whole finding

At 2026-11-21T07:12 UTC a reviewer outside the development of C_A0109_v1 independently checked its [statement](../../claims/Yin_C_A0109_v1.md#statement) and [complete argument](../../claims/Yin_C_A0109_v1.md#argument) for Yin.
The assignment supplied the fixed Claim and the review scope, without proof-generation discussion, author explanations, exploration notes or a previous verdict on this Claim.
The reviewer consulted the cited inputs, the source audit of JZ19 and an adjacent review of the triangle-building action.
The argument proves the two support criteria over arbitrary complex coefficients, both finite-annihilator exclusions in characteristics zero and two, and the stated number-field refinement.
Its matrix inequalities hold for the specified residual tower with the stated input and output dimensions.

### The finite and complex rank inequalities

For each element of \(K\setminus\{1\}\), the core in \(G\) of an excluding normal subgroup of \(p\)-power index in \(K\) is the intersection of at most \(|D|\) conjugates.
The quotient of \(K\) by their intersection embeds in a product of finite \(p\)-groups.
Taking successive intersections and applying separation to all pairwise differences in a finite support proves the required simultaneous separation.
In the Gardam application the map onto \(C_3\), residual \(2\)-finiteness and the values of \(\psi\) are the input of [C_A0108_v1](../../claims/Yin_C_A0108_v1.md#statement).
In the order \(acb,add,afg,bbf,cef,cdg,eeg\) the seven integer label sums are \(7,14,14,7,7,7,7\), which verifies the character relators directly.

Let \(P=P_n\), \(Q=Q_n\) and \(I=\ker(k[P]\to k)\).
For a central \(z\in P\) of order \(p\), nilpotence in \(P/\langle z\rangle\) gives \(I^t\subseteq(z-1)k[P]\) for some \(t\), hence \(I^{tp}=0\).
Choosing one representative \(b_i\) of each coset \(b_iP\) expresses the operator as a matrix between free right \(k[P]\)-modules.
The quotient \(b_i a\mapsto d(b_i)\varepsilon(a)\) intertwines this matrix with left convolution on \(k[D]\).
For an invertible \(r\)-rowed minor of the latter scalar matrix, its lifted square block becomes \(1+E\) after left multiplication by the inverse scalar minor.
If \(I^N=0\), every entry of \(E^N\) vanishes, so the block has ordinary rank \(r|P|\) even for nonabelian \(P\).
This proves (1) with the normalization \(|Q|=|P||D|\).
Twisting is an automorphism of \(k[G]\), and a nonzero vector with finite support remains nonzero after twisting and passage to any sufficiently deep quotient.
Thus full input rank excludes a finite kernel vector.
For a scalar the finite square operator is invertible, giving a two-sided unit in \(k[Q]\) and excluding a nonzero left annihilator by the same separation.

The finitely generated complex coefficient field, enlarged by the \(e\)th roots of unity, embeds in \(\overline{\mathbb Q}_p\) by successively choosing algebraically independent elements in \(\mathbb Q_p\) and extending over a finite algebraic extension.
After division by a coefficient of minimum valuation, one coefficient survives and all coefficients are integral.
For \(p\nmid e\), the \(e\) roots in the embedded field reduce bijectively to \(\mu_e(\overline{\mathbb F}_p)\) by separability of the reduced polynomial.
This lifts the selected residue character to a fixed unitary complex character.
Finite quotient matrices of the normalized twist reduce entrywise, so every nonvanishing residue minor gives a complex minor of the same size.
The character need only be defined on \(G\) because the quotient is applied to the already twisted matrix.

Theorem 1.3 of Jaikin-Zapirain gives rank convergence for every fixed rectangular matrix over any complex subfield on any sofic approximation.
For a free presentation \(F\twoheadrightarrow G\), choose a finite matrix lift to \(F\) and take the quotient regular right \(F\)-sets \(Q_n\).
A word trivial in \(G\) fixes every point of every \(Q_n\), and any fixed word nontrivial in \(G\) eventually fixes none, by residual separation.
Inversion of the group indices sends the left column matrix \(A\) to the right row matrix with entries \(B_{ji}=\sum_g (A_{ij})_g g^{-1}\).
It fixes the identity basis vector in each summand and preserves both finite ranks and the unnormalized matrix trace dimension.
Conjugating by the diagonal unitary with entries \(\chi(h)\) implements the twist on the infinite left regular representation and also fixes \(\delta_1\).
Thus the complex ranks tend to \(\operatorname{rk}_G A\), which dominates the limsup of the normalized residue ranks, yielding (2).
The source theorem is accepted at its statement and hypotheses after checking the [GAFA edition, pp. 469–470](../../literature/pdf/JZ19.pdf#page=6) and the [rank conventions](../literature/JZ19/Yin_U001.md#rank-and-approximation-definitions).
This review did not re-audit the published proof.
When a scalar has rank one, faithfulness of the finite trace gives vanishing kernel and cokernel projections, and the inverse on its dense range is closed and affiliated.

### The support conditions and the reductions

On \(k[C_3]\), evaluation at the three cube roots identifies a unit with three nonzero coordinates.
Consequently a *single* \(\eta\in\mu_7(k)\) works for all three coordinates exactly when \(N(Y)=\prod_{\tau^3=1}F(\tau,Y)\) is nonzero in \(k[C_7]\).
For a single type, nonempty surviving support with distinct \(\psi\)-degrees gives a nonzero sum in the basis \(1,Y,\ldots,Y^6\).
At least one seventh root therefore gives a nonzero value.
For three survivors with two distinct \(\psi\)-degrees, the singleton degree has nonzero coefficient for each fixed \(\tau\).
The coefficient of the repeated degree may vanish.
If it persists, the binomial has at most one root in \(\mu_7\) because the nonzero difference of degrees is invertible modulo seven.
The union of the three zero sets excludes at most three characters.

For three distinct labels and two types, the cube of the pair \(aY^i+bY^j\) has four nonzero terms, with degrees forming a progression of length four and nonzero step \(j-i\bmod 7\).
The cube of the singleton can cancel at most one when forming the product over the three cube roots.
For three types the product is \(U^3+V^3+W^3+UVW\), since the usual coefficient of \(UVW\) is \(-3=1\) in characteristic two.
The cube degrees are pairwise distinct modulo seven and at most one can coincide with the mixed degree.
In both cases a nonzero coordinate of the product gives the required common character.
These arguments allow any nonzero reduced coefficients.

If precisely two coefficients survive normalization, their distinct group elements have ratio \(u\ne1\).
The [building input](../../claims/Yin_C_A0106_v2.md#combining-the-exceptional-and-nonexceptional-supports) gives a free vertex action and a fixed point for each finite-order element.
The seven cyclic triangle relators have distinct ordered initial pairs, with second-letter sets \(cdf,abf,bde,adg,efg,bcg,ace\) in first-letter order.
These seven three-point lines meet pairwise in one point and give the required plane of order two.
The resulting Cayley building has type shifts given by \(d\). [Cartwright and Młotkowski, pp. 348–349](../../literature/pdf/CM94.pdf#page=4).
A nonidentity finite-order element would preserve a simplex and cyclically permute the vertices of a triangle, since a fixed vertex forces identity and a nonzero type shift has no invariant proper subset of the three types.
Its cube then fixes a vertex.
Conjugating to move a triangle vertex to the identity and taking the inverse if necessary gives a positive neighbor \(s\) with \(s^3=1\).
In the [complete rewriting system](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) the only doubled positive initial pairs come from \(dda,bbf,eeg\).
They reduce to the inverse of a different letter, and the other doubled words stay irreducible.
Thus \(ss\) and \(s^{-1}\) have different normal forms for each \(s\), excluding finite order.
The review uses the established normal-form and building theorems at these interfaces.

The orders \(m_n\) of \(u\) in \(Q_n\) tend to infinity, by simultaneous separation of \(u,\ldots,u^M\) for each \(M\).
The scalar \(1+cu\) acts on \(|Q_n|/m_n\) cycles with kernel dimension at most one on each, since the first coordinate determines all others.
The lower bound \(1-1/m_n\) on residue rank proves full complex rank with the trivial twist even when the two \(\psi\)-labels coincide.
A single surviving term is already a unit.
At a residue-degree-one place of the coefficient number field, normalized nonzero residues are all \(1\).
When all three survive and at most two types occur, the type counts have exactly one odd entry, giving a unit monomial in \(\mathbb F_2[C_3]\).
This covers the constant-\(\psi\) case in the additional assertion, including rational coefficients.

For the two main support conditions in characteristic two, every original coefficient survives scalar extension to the algebraic closure and the finite-unit argument applies on both sides.
A characteristic-zero finite zero product descends to its finitely generated coefficient field, which embeds in \(\mathbb C\) with all indicated coefficients nonzero.
An affiliated unit there excludes either order of multiplication.
The earlier [bound of 361 on right support](../../claims/Yin_C_A0106_v3.md#statement) supplies the comparison only.
The unrestricted group-algebra and matrix-rank conjectures remain open within this argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0109_v1.md#statement) | Both support classes, the two coefficient characteristics and annihilator sides, and the residue-degree-one refinement. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0109_v1.md#argument) | The block-rank inequality, lifting characters and ranks, all Fourier and support-loss cases, torsion-freeness and descent. |
| [Whole finding](#whole-finding) | [Separating quotients and labels](../../claims/Yin_C_A0108_v1.md#statement) | Finite 2-group quotients separate elements of the type kernel and the seven displayed labels define the character quotient. |
| [Whole finding](#whole-finding) | [Triangle-building action](../../claims/Yin_C_A0106_v2.md#combining-the-exceptional-and-nonexceptional-supports) | The free action on vertices, cyclic type shifts and CAT(0) fixed-point argument for finite-order elements. |
| [Whole finding](#whole-finding) | [Triangle normal forms](../../claims/Yin_C_A0105_v2.md#a-finite-complete-rewriting-system) | The complete normal forms distinguish the square of each positive letter from its inverse. |
| [Whole finding](#whole-finding) | [Sofic rank approximation](../literature/JZ19/Yin_U001.md#rank-and-approximation-definitions) | Finite right quotient actions and convergence for rectangular complex matrices with normalization by the size of the quotient. |
