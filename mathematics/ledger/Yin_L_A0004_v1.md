---
author: Yin
---
# Linear matrix criteria for the general Atiyah property

Date: 2026-11-11 (Asia/Hong_Kong).
This investigation serves [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [route four](../strategies/Yin_S_A0004.md), following the request to generalize MSY23's linear-full-matrix criterion.
The main agent and two development helpers checked the source specialization, elementary consequences and failure of group-ring fullness for Yin.
The exact rational-closure criterion is already MSY23 Theorem 5.25, also announced as Theorem 1.2; it is not a new generalization being claimed here.
The additional linear-rank and bordered tests are direct consequences of its existing linearization proof.
The counterexample below is a Laurent group-ring adaptation of Cohn's classical polynomial example, with the adaptation proved directly.
The complete investigation has an [independent whole-argument review](../audits/reviews/Yin_R_A0006_v1.md#whole-argument-finding), covering all seven equivalences, both counterexamples and the stated source-applicability limits.

## Setting and exact criteria

Let \(G\) be a finitely generated torsion-free group with a fixed finite generating set \(g_1,\ldots,g_d\).
Take the bounded tuple
\[
X=(\lambda(g_1),\ldots,\lambda(g_d),
   \lambda(g_1^{-1}),\ldots,\lambda(g_d^{-1})).
\]
Set \(B=\lambda(\mathbb CG)\), \(U=\mathcal U(\mathcal N(G))\), \(R=\operatorname{Rat}_U(B)\), and \(D=\operatorname{Div}_U(B)\).
These are actual fixed-ambient closures; neither \(D\) nor \(R\) is assumed to be a division ring.
For a unital ring \(S\), the inner rank \(\rho_S(P)\) is the least \(k\) for which \(P=AB\) factors through \(k\) coordinates over \(S\).
A square \(n\)-by-\(n\) matrix is full over \(S\) when \(\rho_S(P)=n\).
Analytic rank \(\operatorname{rk}_G\) uses the unnormalized matrix trace \(\operatorname{Tr}_n\otimes\tau_G\).

An affine linear square pencil in this fixed tuple is
\[
\Lambda(X)=A_0+\sum_{j=1}^{d}A_j\lambda(g_j)
                  +\sum_{j=1}^{d}B_j\lambda(g_j^{-1}),
\qquad A_0,A_j,B_j\in M_n(\mathbb C).
\]
All sizes and all complex coefficient matrices are quantified below.
No invertibility of \(A_0\), homogeneity or selfadjointness is required.

The following conditions are equivalent.

1. Every finite rectangular matrix over \(\mathbb CG\) has integer analytic rank, equivalently integer von Neumann kernel dimension.
2. Every affine linear square pencil in \(X\) has integer analytic rank.
3. Every affine linear square pencil \(\Lambda(X)\) full over \(R\) is invertible in \(M_n(U)\).
4. Every affine linear square pencil \(\Lambda(X)\) full over \(D\) is invertible in \(M_n(U)\).
5. \(R\) is a division ring.
6. \(D\) is a division ring.
7. For every affine linear \(L(X)\in M_N(B)\) invertible over \(U\), and scalar row \(u\in M_{1,N}(\mathbb C)\) and column \(v\in M_{N,1}(\mathbb C)\), the bordered pencil
   \[
   Q(X)=
   \begin{pmatrix}0&u\\v&L(X)\end{pmatrix}
   \]
   has analytic rank in \(\{N,N+1\}\).

Under these conditions \(D=R\), and every matrix \(P\) over \(B\) satisfies
\[
\operatorname{rk}_G(P)=\rho_R(P)=\rho_D(P).
\]
No equality with \(\rho_B(P)\) is asserted.
Condition 3 is the direct group specialization of [MSY23 Theorem 5.25](../audits/literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence).
Conditions 2, 4 and 7 isolate consequences useful for the present investigation.
For an arbitrary torsion-free discrete group, apply the finite-generation statement to every finitely generated subgroup; each matrix has finite support, and coset induction preserves its kernel dimension.
Thus these are equivalent formulations of the original Task, with no new assertion that all groups satisfy them.

## Source ingredients and rank conventions

[MSY23 Theorem 5.6](../audits/literature/MSY23/Yin_U004.md#theorem-56-exact-equivalences) concerns fullness over the formal free algebra and characterizes free-field realization.
[Theorem 5.25](../audits/literature/MSY23/Yin_U005.md#theorem-525-the-complete-equivalence) replaces that fullness by inner rank over the actual evaluated rational closure and characterizes the general strong Atiyah property.
The distinction is already explicit in the published paper and its existing source audits.

The source inputs used below are [Lemma 4.8](../audits/literature/MSY23/Yin_U003.md#lemma-48-linearization-preserves-an-existing-inverse-domain), [Proposition 4.11](../audits/literature/MSY23/Yin_U003.md#complete-division-closure-and-proposition-411), and [Proposition 2.3](../audits/literature/MSY23/Yin_U001.md#proposition-23-and-lemma-24), with the finite affiliated rank facts recorded in [U004](../audits/literature/MSY23/Yin_U004.md#msy23-u004).
Lemma 4.8 gives every \(r\in R\) a representation \(r=uL(X)^{-1}v\) with \(L\) affine linear, actually invertible over \(U\), and \(u,v\) scalar.
The inverse has entries in \(R\), so \(L(X)\) is also invertible over \(R\).
Proposition 4.11 identifies \(D=R\) and division of both whenever either actual closure is a division ring.

Both closures are subrings of the stably finite ring \(U\), so are stably finite.
For every matrix over \(B\),
\[
\operatorname{rk}_G(P)\leq\rho_R(P)\leq\rho_D(P)\leq\rho_B(P).
\]
The first inequality follows by applying the analytic rank inequality to any factorization through \(k\) coordinates.
The other inequalities follow by enlarging the coefficient ring in the allowed factorizations.
These inequalities need no Atiyah premise.

## Proof of the linear and bordered equivalences

If \(R\) is a division ring, Gaussian elimination over \(R\) reduces any matrix over \(B\) to \(\operatorname{diag}(I_k,0)\), with rectangular zero blocks when necessary.
The eliminating matrices and their inverses remain matrices over \(U\).
Invariance of analytic rank under invertible multiplication proves the displayed rank equality and condition 1.
It also proves condition 3 and, because then \(D=R\), condition 4.
Condition 1 immediately implies condition 2, and condition 2 implies condition 7 since \(Q\) is itself affine linear and its rank lies between \(N\) and \(N+1\).

For the converse from condition 7, take \(0\ne r\in R\) and its linear representation \(r=uL(X)^{-1}v\).
The exact block identity is
\[
\begin{pmatrix}-r&0\\0&I_N\end{pmatrix}
=
\begin{pmatrix}1&-uL(X)^{-1}\\0&L(X)^{-1}\end{pmatrix}
\begin{pmatrix}0&u\\v&L(X)\end{pmatrix}
\begin{pmatrix}1&0\\-L(X)^{-1}v&I_N\end{pmatrix}.
\]
Both exterior matrices are invertible over \(R\) and \(U\).
Therefore
\[
\operatorname{rk}_G Q(X)=N+\operatorname{rk}_G r.
\]
Faithfulness of the trace gives \(0<\operatorname{rk}_G r\leq1\).
Condition 7 forces \(\operatorname{rk}_G r=1\), so \(r\) is invertible in \(U\).
Inverse closure of \(R\) then gives \(r^{-1}\in R\), proving condition 5.
This proves that integer ranks of linear pencils alone already imply the full Atiyah property.
It does not require a bound on the pencil size, and supplies no such bound.

To prove condition 3 implies condition 5, use the same \(r,L,Q\).
Schur elimination over \(R\) gives inner rank at least \(N\).
It gives inner rank exactly \(N\) if and only if \(r=0\), by the stably finite Schur criterion.
For clarity, a factorization of \(\operatorname{diag}(I_N,-r)\) through \(N\) would have top factors \(P_0Q_0=I_N\).
Stable finiteness gives \(Q_0P_0=I_N\).
The zero off-diagonal blocks force the remaining column and row factors to vanish, hence force \(r=0\).
Since \(r\ne0\), the inner rank is \(N+1\), so \(Q\) is full over \(R\).
Condition 3 makes \(Q\) invertible over \(U\), and Schur elimination makes \(r\) invertible there and hence in \(R\).

Finally, an \(R\)-full pencil is necessarily \(D\)-full because \(D\subseteq R\).
Thus condition 4 implies condition 3.
The converse follows through conditions 5 and 6, where the two closures coincide as a division ring.
This is equivalence of the global conditions; it does not assert equality of \(D\)-fullness and \(R\)-fullness for individual matrices before the Atiyah property is known.
All seven conditions are therefore equivalent.

## Why formal free-algebra fullness cannot be retained

Already for \(G=\mathbb Z=\langle g\rangle\), use the fixed tuple \((g,g^{-1})\).
The formal affine matrix
\[
\Lambda(a,b)=\begin{pmatrix}a&1\\1&b\end{pmatrix}
\]
is full over \(\mathbb C\langle a,b\rangle\), since its scalar specialization at \(a=b=0\) is invertible and a factorization through one coordinate would survive specialization.
But its actual group-ring evaluation factors as
\[
\begin{pmatrix}g&1\\1&g^{-1}\end{pmatrix}
=\begin{pmatrix}g\\1\end{pmatrix}
 \begin{pmatrix}1&g^{-1}\end{pmatrix}.
\]
It has analytic rank one and is not invertible.
This is a relation-respecting obstruction to retaining formal free fullness, even though \(\mathbb Z\) satisfies the Atiyah property.
It does not obstruct the relative criterion, because the evaluated matrix is already nonfull over \(\mathbb CG\).

## A group-ring-full linear pencil that is analytically singular

The stronger replacement of condition 3 by fullness over \(\mathbb CG\) also fails.
Let
\[
G=\mathbb Z^3,\qquad
B=\mathbb C[u^{\pm1},v^{\pm1},w^{\pm1}],\qquad
x=u-1,\quad y=v-1,\quad z=w-1,
\]
and set
\[
T=
\begin{pmatrix}
0&x&y\\
-x&0&z\\
-y&-z&0
\end{pmatrix},
\qquad
k=\begin{pmatrix}z\\-y\\x\end{pmatrix}.
\]
This is an affine linear pencil in the fixed group generators.
Both \(Tk=0\) and \(k^{\mathsf T}T=0\) hold.
Over the commutative field \(F=\operatorname{Frac}(B)\), its rank is two, since its upper-left minor is \(x^2\ne0\) and it has the displayed nonzero kernel vector.

### Fullness over the Laurent group ring

Let \(\mathfrak m=(x,y,z)\subset B\) be the augmentation maximal ideal.
The classes of \(x,y,z\) form a basis of \(\mathfrak m/\mathfrak m^2\) over \(\mathbb C\).
Indeed \(B/\mathfrak m^2\cong\mathbb C[x,y,z]/(x,y,z)^2\), because \(1+x,1+y,1+z\) are already invertible in the latter quotient.

If \(T\) factored through fewer than three coordinates, padding zero coordinates would give \(T=PQ\) with \(P\in M_{3,2}(B)\) and \(Q\in M_{2,3}(B)\).
Its field rank two implies that \(P\) is injective and \(Q\) is surjective as the corresponding \(F\)-linear maps.
Consequently the two kernel identities imply
\[
k^{\mathsf T}P=0,\qquad Qk=0.
\]
For each column \((p_1,p_2,p_3)^{\mathsf T}\) of \(P\), the first identity is \(zp_1-yp_2+xp_3=0\).
Modulo \(\mathfrak m^2\), independence of \(x,y,z\) forces each \(p_i\in\mathfrak m\).
The same argument applied to each row of \(Q\) forces every entry of \(Q\) into \(\mathfrak m\).
Then every entry of \(PQ\) lies in \(\mathfrak m^2\), contradicting \(T_{12}=x\notin\mathfrak m^2\).
Thus
\[
\boxed{\rho_{\mathbb C[\mathbb Z^3]}(T)=3.}
\]
This proof addresses the Laurent ring directly; fullness over a polynomial ring alone would not justify fullness after localization.

### Actual rank and the complete Atiyah premise

Under Fourier transformation, the canonical representation is multiplication on \(L^2(\mathbb T^3)\).
The same minor is nonzero almost everywhere, while the determinant vanishes identically.
Therefore
\[
\boxed{\operatorname{rk}_{\mathbb Z^3}T=2,\qquad
       \dim_{\mathbb Z^3}\ker T=1.}
\]
Thus \(T\) is full over the group ring but is not affiliated-invertible.

For completeness, every nonzero Laurent polynomial has a Haar-null zero set on \(\mathbb T^3\).
After multiplication by a monomial, this follows by induction on the number of variables: outside the common zero set of the coefficient polynomials, the last-variable polynomial has finitely many roots, and Fubini applies.
For any rectangular matrix of Laurent polynomials, a maximal nonzero minor and the vanishing of larger minors identify its almost-everywhere rank with its rank over \(F\).
Hence all such matrices have integer analytic ranks and kernel dimensions.
This verifies the full complex Atiyah premise for the example, not merely the integer rank of \(T\).

Every nonzero element of \(B\) is affiliated-invertible, so the actual division and rational closures both equal \(F\).
The inclusion \(F\subset U\) is faithful by the same null-zero-set argument.
Conversely \(F\) is rationally closed in \(U\): a matrix over \(F\) singular over \(F\) has a nonzero vector over \(F\) in its kernel and therefore cannot become invertible over \(U\), while a nonsingular matrix has its inverse over \(F\).
In particular,
\[
T=
\begin{pmatrix}0&x\\-x&0\\-y&-z\end{pmatrix}
\begin{pmatrix}1&0&-z/x\\0&1&y/x\end{pmatrix}
\]
is an explicit factorization through two coordinates over the actual rational closure.
Thus \(\rho_R(T)=2\), exactly as the general criterion requires.

### Source attribution for the obstruction

The polynomial prototype is Cohn, [Coh06, Section 5.5, printed p. 290, equation (1)](../literature/pdf/Coh06.pdf#page=314), in the retained 2006 NetLibrary edition.
His displayed matrix is
\(\left(\begin{smallmatrix}0&z&-y\\-z&0&x\\y&-x&0\end{smallmatrix}\right)\), stated to be full and a left and right zero divisor over \(k[x,y,z]\).
The change \((x_{\mathrm{Cohn}},y_{\mathrm{Cohn}},z_{\mathrm{Cohn}})=(z,-y,x)\) gives the matrix used here.
Printed p. 297 explains the example using the Koszul resolution; Exercise 5.5.4 on printed p. 299 asks for a direct proof.
These primary passages were read for attribution; the augmentation proof above is self-contained and additionally verifies the required Laurent variant.
MSY23 Remark 5.11, published pp. 33--34, already warns that polynomial-ring inner rank cannot in general replace fraction-field rank in more than two commuting variables, as retained in [U004](../audits/literature/MSY23/Yin_U004.md#remark-511-commutative-comparison).
No novelty or priority claim is made for the polynomial obstruction or its elementary adaptation.

## Consequence for the research route

The exact linear-full criterion survives for general Atiyah when fullness is computed over the actual rational closure; the actual division closure gives another equivalent global formulation.
The proposed criterion that every group-ring-full linear pencil be affiliated-invertible is strictly stronger than the Atiyah property: it implies the rational-closure criterion by rank monotonicity, but its converse fails even for \(\mathbb Z^3\).
Merely imposing the group relations on the formal free algebra therefore does not repair the free-full criterion.

For continued analytic work, conditions 2 and 7 avoid having to classify fullness over an as-yet-unknown rational closure.
Condition 7 concentrates the remaining obstruction in a concrete rank interval:
\[
N<\operatorname{rk}_G
\begin{pmatrix}0&u\\v&L(X)\end{pmatrix}<N+1,
\qquad L(X)\in GL_N(U).
\]
Excluding that interval for every admissible bordered linear pencil is equivalent to the Task.
The equivalence supplies no argument that torsion-freeness excludes it, no bounded inverse and no finite maximum pencil size.
Further progress must provide an independent group-specific rank constraint on this family, rather than assume free-field rank preservation or group-ring inner-rank equality.
