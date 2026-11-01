---
author: Yin
---
# Actual ACSY derivations solve every finite polynomial relation obstruction

Human author: Yin.
Root proposed removal of the scalar-null coefficient blocks and the use of maximal Delta to verify the remaining rectangular block's left-kernel condition.
The general ACSY-to-full-domain branch checked the full block reduction and Hilbert--Schmidt trace identity, supplied and checked the bounded polynomial-linearization transfer, and fixed the complete argument.
Both are developers, not independent reviewers.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace, H=L2(M), and X=(X_1,...,X_d) a bounded generating tuple.
On the represented star algebra cal A=C<X,X*> suppose there are complex-linear outer derivations delta_i:cal A->H tensor_2 H with
\[
 \delta_i X_j=\delta_{ij}1\otimes1,\qquad
 1\otimes1\in\operatorname{Dom}\delta_i^*,
 \qquad i,j=1,\ldots,d .
\]
Thus the actual ACSY condition is assumed, with arbitrary compatible Hilbert starred values and no reality premise.
Inner products are linear in the second variable.

For any positive integers r,m, any r by m holomorphic polynomial matrix P in X, and any bounded column a in M_(m,1)(M) satisfying Pa=0, put
\[
 g_i(P,a)=(\mathrm{id}\otimes\tau)
                      \bigl((\delta_iP)\mathbin{\cdot}a\bigr)\in H^r.
 \tag{1}
\]
The derivative is entrywise, multiplication by a uses the outer right tensor actions and matrix contraction, and id tensor tau acts entrywise afterward.
Since P is holomorphic, delta_iP is a finite polynomial tensor matrix, so (1) is an actual Hilbert column and is fixed by the prescribed unstarred values.

For every such a and i there exists z in H^m with
\[
 Pz=-g_i(P,a).
\]
For each fixed P and i, z can be selected by a complex-linear bounded map
\[
 \Phi_{P,i}:\ker(P)\cap M_{m,1}(M)\longrightarrow H^m,
 \qquad
 \|\Phi_{P,i}(a)\|_{H^m}\le C_{P,i}\|a\|_{M_{m,1}(M)}
\]
for some finite constant C_(P,i).
Here ker(P) refers to the bounded column equation Pa=0, with the operator column norm on its indicated bounded domain.

This removes every finite holomorphic polynomial-relation range obstruction to a bare dual.
Indeed any E_i:M->H with [E_i,X_j]=delta_ij P_Omega must satisfy P(E_i(a_j))=-g_i(P,a).
The result does not produce one coherent E_i valid for all columns and all matrices, does not give a bound uniform over P, and does not settle the general A-to-F implication.

## Reuse and exact dependencies

The [positive-compression matrix inverse-trace criterion C_F0154](Yin_C_F0154_v1.md#statement) is applied only after its regularity and strict-positivity hypotheses have been proved for a compressed affine block.
[ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) gives maximal Delta from the actual derivation hypotheses above, without a normality premise.
[MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) identifies maximal Delta with the absence of nonzero finite-rank cycles and supplies Lemma 3.4's two-kernel-vector calculation.
Its rectangular adaptation and the needed trace identity are checked below; no general bounded-inverse statement is inferred from maximal Delta.

For polynomial transfer, [MSY23-U003](../audits/literature/MSY23/Yin_U003.md#msy23-u003), Theorem 4.3's polynomial construction and Lemma 4.8, give affine unit-upper-triangular pencils with polynomial inverses.
The rectangular assembly uses constant coordinate inclusions as in that source record.
No unbounded rational pivot or unverified rational-domain extension is used.

The local search and predecessor C_F0154 isolate the unresolved singular-compression case.
The present argument resolves the contracted finite-relation right-hand sides by scalar block reduction; it does not claim a new general theorem on Sobolev domains of kernel projections.
The source inspection limits remain those of the cited fixed units.

## Argument

### 1. Removing scalar-null blocks for finite affine constraints

The strictly positive compression in C_F0154 can be obtained on the part relevant to an affine relation, without asserting inverse-trace integrability for the entire pencil.
Root proposed this reduction; this branch checked its exact scalar blocks, the rectangular finite-rank-cycle argument and the resulting range solution.

Let L=A_0+sum_i A_i X_i be any n by m affine pencil, and let p be its right-kernel projection.
No regularity of LL* is assumed in this paragraph.
Put C=(id tensor tau)p, K_0=ker C, and B=sum_i A_i C A_i*.
The ACSY premise gives maximal Delta through [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
The finite-rank-cycle criterion and the two-kernel-vector calculation are reused from [MSY23-U002, Lemma 3.4](../audits/literature/MSY23/Yin_U002.md#lemma-34-from-two-kernel-vectors-to-a-finite-rank-cycle), with its inner-product convention converted to linearity in the second variable.

For a scalar column u, ||p u||_(H^m)^2=u*Cu.
Thus p kills K_0 and, after a constant unitary change of columns,
\[
 p=\begin{pmatrix}0&0\\0&p_1\end{pmatrix},
 \qquad C=\begin{pmatrix}0&0\\0&C_1\end{pmatrix},
 \qquad C_1>0\quad\hbox{on }K_0^\perp.
 \tag{2}
\]
The assertion is an operator block identity: p u=0 as a Hilbert column has zero bounded entries, and multiplication by arbitrary bounded elements on the right gives the full column block.

For a scalar v in ker B, positivity gives p A_i* v=0 for every i>=1.
Also p L* v=0.
Since the column A_i*v is scalar, the order in this latter equation can be written
\[
 pA_0^*v+\sum_i p(A_i^*v)X_i^*=0.
 \tag{3}
\]
Hence pA_0*v=0 as well.
All scalar columns A_i*v, including i=0, belong to K_0.
A constant unitary row change puts ker B first and its orthogonal complement R last.
With the already chosen columns, every coefficient and the pencil itself have block form
\[
 A_i=\begin{pmatrix}A_{i,00}&0\\A_{i,10}&A_{i,11}\end{pmatrix},
 \qquad
 L=\begin{pmatrix}L_{00}&0\\L_{10}&L_{11}\end{pmatrix},
 \qquad
 B_{11}=\sum_i A_{i,11}C_1A_{i,11}^*>0
       \quad\hbox{on }R .
 \tag{4}
\]
Here the top row size is dim ker B and the first column size is dim K_0; they need not agree.
If R is zero, all derivative coefficient blocks on K_0^perp vanish and every affine forced right-hand side below is zero.
This case requires no inverse.

Assume now r=dim R>0, and write ell=dim K_0^perp.
The right kernel of the r by ell pencil L_11 is exactly p_1: a vector z is in that kernel precisely when (0,z) is in ker L.
Let q be the left-kernel projection of L_11.
For any e in qH^r and f in p_1H^ell define the finite-rank operators
\[
 T_i(e,f)=\sum_{j=1}^r\sum_{k=1}^{\ell}
       (A_{i,11})_{jk}\,|f_k\rangle\langle e_j|.
 \tag{5}
\]
The rectangular version of the MSY calculation uses L_11 f=0 and L_11* e=0 to give T_0+sum_i X_i T_i=0 and T_0+sum_i T_i X_i=0.
No equality of the row and column sizes, or independence of components, is used.
Thus sum_i[T_i,X_i]=0.
Maximal Delta implies T_i=0 for every i>=1.

Take f to be each column of p_1 and e to be each column of q, viewed as Hilbert vectors.
Summing the Hilbert--Schmidt squared norms gives, for each i,
\[
 0=\sum_{a=1}^{\ell}\sum_{b=1}^r
            \|T_i(qe_b,p_1e_a)\|_{\mathrm{HS}}^2
   =\operatorname{Tr}_r
        \bigl((\mathrm{id}\otimes\tau)(q)\,
                A_{i,11}C_1A_{i,11}^*\bigr).
 \tag{6}
\]
Explicitly, the sum of the f Gram entries is tau((p_1)_(k',k)), and that of the e entries in the reverse order is tau(q_(j,j')); these give the displayed trace, with no transpose missing.
Summing (6) over i and using B_11>0 forces (id tensor tau)(q)=0 and hence q=0 by faithfulness.
Therefore Q_11=L_11L_11* is regular.
C_F0154 applies to this block and puts every bounded R-column in the actual range L_11 H^ell.

Now let a in M^m be bounded and La=0.
By (2), its K_0 component vanishes.
For each i the scalar column A_i tau(a) consequently has zero top-row component in (4).
Choose z_0=0 and use the actual polar right inverse of L_11 to solve
\[
 L_{11}z_1=-A_{i,11}\tau(a_1).
 \tag{7}
\]
Then L(z_0,z_1)=-A_i tau(a).
Undoing the constant unitaries proves the same assertion in the original coordinates.
The zero-R case has the solution z=0.
For a fixed pencil and i these choices give a bounded linear map from its bounded kernel columns to H^m: tau is contractive from bounded columns to scalar Euclidean columns, and the chosen Hilbert right inverse on the lower block has the fixed C_F0154 bound.
No uniform constant over all pencils is claimed.

### 2. Passing finite compatibility through polynomial linearization

The exact [MSY23-U003 polynomial construction](../audits/literature/MSY23/Yin_U003.md#theorem-43-constructive-existence-of-representations) and its [Lemma 4.8 interface](../audits/literature/MSY23/Yin_U003.md#lemma-48-linearization-preserves-an-existing-inverse-domain) give, entrywise and with constant coordinate inclusions, a representation of any rectangular holomorphic polynomial matrix P as P=U D^-1 V, with U,V constant and D affine unit upper triangular.
Its inverse is a polynomial matrix, so every bounded evaluation and every product below is actually bounded.
Form
\[
 L=\begin{pmatrix}0&U\\-V&D\end{pmatrix},
 \qquad J=\binom{I}{D^{-1}V},
 \qquad LJ=\binom{P}{0} .
 \tag{8}
\]
The affine relation result just proved applies to L, including all its scalar-null blocks.
For a bounded a with Pa=0, b=Ja is bounded and Lb=0.
If A_i^L is the coefficient of X_i in L, choose u in the appropriate Hilbert column space with Lu=-A_i^L tau(b).

All entries of J are holomorphic polynomials.
Differentiate the exact polynomial identity (8), multiply its second tensor legs by a, and contract with id tensor tau.
With
\[
 g_i(P,a)=(\mathrm{id}\otimes\tau)(\delta_iP\mathbin{\cdot}a),
 \qquad
 t=(\mathrm{id}\otimes\tau)(\delta_iJ\mathbin{\cdot}a),
\]
this gives
\[
 \binom{g_i(P,a)}0
       =A_i^L\tau(b)+Lt,\qquad
 t_{\rm top}=0,\qquad
 L(u-t)=-\binom{g_i(P,a)}0.
 \tag{9}
\]
Every contraction is Hilbert because delta_iP and delta_iJ have finitely many bounded polynomial tensor legs and a is bounded; delta_i is not applied to a or to b.
The lower block of (9) yields (u-t)_aux=D^-1 V u_top, and the upper block therefore gives
\[
 P u_{\rm top}=-g_i(P,a).
 \tag{10}
\]
Thus every bounded holomorphic polynomial-matrix relation has the required actual Hilbert range solution.
For a fixed P and i, the construction is linear and bounded in the bounded-column norm: b=Ja is bounded by ||J||||a||, and the affine solution map has a fixed bound.
In fact it uses finitely many scalar trace functionals of the entries of Ja.
This is finite compatibility, not one coherent E_i on all M.

The result uses scalar-block reduction and a bounded polynomial linearization to control the contracted relation right-hand sides.
It does not assert a separate uncontracted weighted-tensor domain for the kernel projection.
Passing from all finite compatibilities to a single Hilbert-valued dual still needs an additional argument; ordinary finite solvability alone does not give Hilbert compactness or a uniform norm bound across all systems.


## Necessary finite identities and the remaining global step

For completeness, if an E_i as in the statement exists, repeated use of its commutator identities on bounded vectors gives
\[
 E_i(P_j a)=P_jE_i(a)+\Theta(\delta_iP_j)a,
 \qquad
 \Theta(u\otimes v)a=u\,\tau(va)
\]
for a scalar holomorphic polynomial P_j.
Applying this entrywise to Pa=0 gives exactly the forced equation in the statement.
No starred value of E_i or derivation on the bounded column is used.

The construction above assigns a solution separately to each fixed polynomial matrix.
Even though each such choice is bounded and linear in a, its choice and bound depend on that matrix.
No compatibility among the choices for different matrices has been proved.
An infinite system in a Hilbert space need not be solvable merely because each finite subsystem is solvable: coordinate equations prescribing infinitely many unit coordinates already show the absence of an automatic Hilbert compactness principle.
This elementary warning is not a counterexample to the current operator-algebra problem; it identifies the precise additional step still required for a global dual.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:03 |
| status | open |
| reason | Complete developer-checked scalar-block reduction, rectangular finite-rank-cycle regularity and bounded polynomial-linearization transfer solve each finite polynomial relation obstruction with a bounded linear selection for a fixed matrix. Independent review is pending; no global coherent dual is constructed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every bounded holomorphic polynomial-matrix relation has the required actual Hilbert range solution, with a bounded linear choice for each fixed P,i; no uniform or global extension is claimed. |
| argument | [Argument](#argument) | Scalar-kernel compression including degenerate cases, rectangular cycle and HS trace calculation, C_F0154 range application, and bounded unitriangular polynomial transfer. |
| dependency | [Positive-compression inverse criterion](Yin_C_F0154_v1.md#statement) | Actual Hilbert right inverse on bounded columns once the compressed affine block is shown regular with strictly positive scalar B. |
| dependency | [Actual ACSY maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 for arbitrary bounded generating tuples with full starred-core derivations and actual vacua, used to obtain maximal Delta. |
| dependency | [Finite-rank cycles](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal Delta excludes nonzero finite-rank cycles; Lemma 3.4's two-kernel-vector calculation is adapted with explicit rectangular indices. |
| dependency | [Polynomial linearization](../audits/literature/MSY23/Yin_U003.md#msy23-u003) | Theorem 4.3 polynomial construction and Lemma 4.8: affine unit upper triangular D, polynomial D inverse, constant U,V and entrywise rectangular assembly. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T21:07 |
| status | proved |
| reason | Adopt the complete finite polynomial-relation theorem after R_F0163 independently checked the entire statement, both proof sections, degenerate cases and all four direct inputs. The fixed-matrix bounded choice is established; no coherent global dual or uniform bound is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every bounded holomorphic polynomial-matrix relation has the required actual Hilbert range solution, with a bounded linear choice for each fixed P,i; no uniform or global extension is claimed. |
| argument | [Argument](#argument) | Scalar-kernel compression including degenerate cases, rectangular cycle and HS trace calculation, C_F0154 range application, and bounded unitriangular polynomial transfer. |
| dependency | [Positive-compression inverse criterion](Yin_C_F0154_v1.md#statement) | Actual Hilbert right inverse on bounded columns once the compressed affine block is shown regular with strictly positive scalar B. |
| dependency | [Actual ACSY maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 for arbitrary bounded generating tuples with full starred-core derivations and actual vacua, used to obtain maximal Delta. |
| dependency | [Finite-rank cycles](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal Delta excludes nonzero finite-rank cycles; Lemma 3.4's two-kernel-vector calculation is adapted with explicit rectangular indices. |
| dependency | [Polynomial linearization](../audits/literature/MSY23/Yin_U003.md#msy23-u003) | Theorem 4.3 polynomial construction and Lemma 4.8: affine unit upper triangular D, polynomial D inverse, constant U,V and entrywise rectangular assembly. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0163_v1.md#conclusion) | Whole statement and argument, all scalar block and rectangular cycle details, exact trace order, actual bounded linear selection, polynomial transfer and all four direct interfaces. |

