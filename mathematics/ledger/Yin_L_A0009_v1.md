---
author: Yin
---
# Sufficient conditions for scalar dimension induction over torsion-free groups

Date: 2026-11-11 (Asia/Hong_Kong).
The main research agent and two development helpers carried out this investigation for Yin under [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract).
The question is whether sufficient conditions allow induction reducing matrix size to one, with torsion-freeness supplying the scalar base case.
This concerns matrix dimension rather than the polynomial-degree reduction in [L_A0008](Yin_L_A0008_v1.md).
Three concrete preserved structures are examined: rows with at most two group monomial terms, constant row or column factorization with certified pivots, and an injective positive real part preserved by affiliated Schur complements.
The first gives an exact integer kernel dimension for a sparse class over every torsion-free group, without an indicability hypothesis.
The other two give independently justified scalar pivot chains in their stated classes.
These are explicit applications and refinements of the retained cyclic, Schur, transport and energy mechanisms, not a new Atiyah group class or historical-novelty claim.
All matrix traces are unnormalized and all affiliated products are closed products in the actual algebra.
The [independent review findings](../audits/reviews/Yin_R_A0011_v1.md#combined-outcome) together cover the complete body and the original-border application, with their exact source and foundational limits retained.

## The scalarization already available for a bordered pencil

Let \(G\) be torsion-free, let \(U=\mathcal U(\mathcal N(G))\), and use the canonical faithful trace.
For the original bordered pencil with \(N\ge1\), constant complex borders \(u,v\), and an affine \(L\in M_N(\mathbb CG)\) independently proved invertible in \(M_N(U)\),
\[
Q=\begin{pmatrix}0&u\\v&L\end{pmatrix},\qquad r=uL^{-1}v,
\]
the [existing exact Schur identity](Yin_L_A0004_v1.md#proof-of-the-linear-and-bordered-equivalences) already gives
\[
\operatorname{rk}_G Q=N+\operatorname{rk}_G r,\qquad
\dim_G\ker Q=\dim_G\ker r.
\]
Thus a scalar rational expression is already available; the missing step is an independently controlled class containing that scalar.
A useful size induction must guarantee both a justified scalar pivot and preservation of such a class, rather than merely producing a smaller rational expression.
The [complementary-block reduction](Yin_L_A0005_v1.md#complementary-block-reduction-and-the-scalar-obstruction) supplies another exact size reduction, but does not assert that its remaining affine block has a certified pivot.

## The exact size-reducing step

Let \(U=\mathcal U(\mathcal N(G))\), with its unnormalized matrix ranks, and let
\[
L=\begin{pmatrix}a&b\\c&D\end{pmatrix}\in M_n(U),
\qquad a\in U^\times.
\]
The unit premise on \(a\) must have an independent justification.
Define
\[
S=D-ca^{-1}b.
\]
Direct multiplication in the displayed order gives
\[
\begin{pmatrix}1&0\\-ca^{-1}&I\end{pmatrix}
L
\begin{pmatrix}1&-a^{-1}b\\0&I\end{pmatrix}
=\operatorname{diag}(a,S).
\tag{S1}
\]
Both outer matrices are actual units independently of whether \(S\) or \(L\) is a unit.
Consequently,
\[
\operatorname{rk}_G L=1+\operatorname{rk}_G S,
\qquad
\dim_G\ker L=\dim_G\ker S.
\tag{S2}
\]
All products mean closed affiliated products.
The second equality concerns closed kernel dimensions and does not assert an unrestricted pointwise map between Hilbert-space kernels using an unbounded multiplier.

The matrix size decreases, but the expression class usually changes.
Even for a scalar constant pivot \(a=1\), affine off-diagonal entries \(b=x\) and \(c=y\) produce the quadratic Schur correction \(yx\).
For a nonconstant cyclic pivot, \(a^{-1}\) generally produces rational entries.
Thus a size induction needs a preserved certificate class, not merely the assertion that the input matrix was affine.
The retained [depth-one obstruction](../ledger/Yin_L_A0002_v1.md#precise-continuation-point) already has this form with its cyclic denominator independently justified.

## A concrete sufficient condition closed under elimination

Let \(G\) be torsion-free and let \(A\in M_{m,n}(\mathbb CG)\).
Assume every row of \(A\), as a row expression in the input coordinates, is a sum of at most two terms of the form
\[
c\lambda(g)x_i,\qquad c\in\mathbb C^\times,\quad g\in G.
\]
The two terms are allowed to use the same coordinate, and a row may have only one term or be zero.
The hypothesis counts group monomials in the whole row, not merely nonzero matrix entries.
In particular, an entry that is a sum of several group elements does not automatically satisfy it.

A two-term row in distinct coordinates can be normalized by an independently invertible scalar group monomial to
\[
x_i-q_e x_j=0,
\qquad q_e=z_e\lambda(k_e),\quad z_e\in\mathbb C^\times.
\tag{T1}
\]
A two-term row in the same coordinate gives a loop equation \((1-q_e)x_i=0\).
A one-term row gives a pin \(x_i=0\) after the same normalization.
Zero rows impose no constraint.
All these row normalizations and their inverses are bounded group-ring operators.

Form the finite graph on the \(n\) coordinates using the distinct-coordinate rows as edges, and retain loops and pins at their vertices.
Include isolated vertices among its connected components.
For a connected component \(C\), choose a root and a spanning tree.
The tree equations determine scalar group units
\[
W_i=\alpha_i\lambda(h_i),\qquad \alpha_i\in\mathbb C^\times,
\qquad W_r=I,
\]
such that the tree constraints are equivalent to \(x_i=W_i\xi\).
No assumption \(|\alpha_i|=1\) is made.
For a remaining edge or loop with equation (T1), the resulting root equation is
\[
(1-T_e)\xi=0,
\qquad T_e=W_i^{-1}q_eW_j=z'_e\lambda(k'_e).
\tag{T2}
\]
Every pin becomes an invertible scalar group monomial times \(\xi=0\), hence forces \(\xi=0\).

Call a component unpinned and flat if it has no pin and every residual transport \(T_e\) in (T2) is the actual identity.
Equivalently, it has no pin and every closed-walk transport, including its complex amplitude, is the identity.
Let \(f\) be the number of such components.
Then
\[
\boxed{\dim_G\ker A=f,\qquad\operatorname{rk}_G A=n-f.}
\tag{T3}
\]
If \(m=n\), the matrix is an actual affiliated unit exactly when \(f=0\).
These statements include tree components, isolated vertices, parallel edges, loops, repeated labels and exact cancellation of a same-coordinate row.

## Scalar base case supplied by torsion-freeness

For \(z\in\mathbb C^\times\) and \(k\in G\), consider
\[
b=1-z\lambda(k).
\]
If \(k=e\), this is zero exactly when \(z=1\), and otherwise it is a nonzero scalar unit.
If \(k\ne e\), torsion-freeness makes \(k\) infinite order.
The restriction of \(\lambda(k)\) to each right coset of \(\langle k\rangle\) is a bilateral shift, so it has no eigenvectors.
Thus \(b\) is injective, and finite trace makes it an actual affiliated unit.
For \(|z|\ne1\), injectivity also follows immediately from unitarity, without using torsion-freeness.
This is precisely the retained [cyclic regular-representation input](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), not a scalar injectivity assertion for arbitrary group-ring polynomials.

Consequently every residual scalar in (T2) is either zero or an independently certified actual unit.
This is the base case that closes the dimension induction.
It checks a specific binomial class, rather than assuming that every nonzero entry of a rational closure is a unit.
The torsion-free premise is essential for this uniform base case: if \(k\) has finite order \(q>1\), the kernel projection of \(1-\lambda(k)\) is \(q^{-1}\sum_{j=0}^{q-1}\lambda(k)^j\), whose canonical trace is \(1/q\).
This finite-order comparison is outside the torsion-free Task and identifies exactly the obstruction removed by its hypothesis.

## Strict size descent and kernel-dimension preservation

Equivalently, the induction can be performed literally by removing a leaf of the selected spanning tree.
Normalize its tree row to \(x_i-qx_j=0\), solve it as \(x_i=qx_j\), and remove that row and the leaf coordinate using its scalar identity pivot.
Substitution in any remaining row preserves the bound of two group monomials, because each substituted term is multiplied by the single scalar group monomial \(q\).
Two terms may move into the same coordinate and become a loop, or cancel completely; a pin remains a pin.
The remaining selected tree spans the smaller component, so this operation can be repeated until only its root coordinate remains.
Thus the invariant is the number of additive monomial terms per row, not a bound on their word lengths.

First use the bounded diagonal coordinate change \(x_i=W_i y_i\) and appropriate bounded row normalizations.
The selected tree rows then become ordinary differences \(y_i-y_j\).
Root the tree and introduce one coordinate \(z_i=y_i-y_{\mathrm{parent}(i)}\) for each nonroot vertex, retaining \(y_r\) as the last coordinate.
This is an invertible complex triangular coordinate change after ordering vertices from root to leaves, with inverse given by finite path sums.
The tree rows are now the coordinates \(z_i\), up to signs.

Eliminate those coordinates one by one using their identity pivots and triangular row operations.
Each pivot removes one row and one input coordinate, contributes exactly one to the original rank and leaves the kernel dimension unchanged.
All factors used up to this point are polynomial group-ring units whose inverses are explicit and bounded.
After \(|C|-1\) eliminations, the component has a single remaining input coordinate and its residual rows are (T2) and normalized pins.

If all residual rows are zero and there is no pin, the final column has rank zero and kernel dimension one.
Otherwise select a pin or one nonzero residual binomial.
Its independent unit proof above permits a final pivot, and triangular row operations clear the other entries of that single column.
This gives rank one and kernel dimension zero for the residual column.
The inverse of a cyclic binomial may be unbounded, so this final elimination is performed in the actual affiliated algebra using [rank invariance under actual units](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement).
No unrestricted pointwise substitution involving that inverse is used.

Summing over components gives (T3).
As a direct check on the flat-component dimension, the map
\[
J_C\xi=
\left(\sum_{i\in C}|\alpha_i|^2\right)^{-1/2}
(W_i\xi)_{i\in C}
\]
is an equivariant isometry onto its kernel.
The diagonal entries of \(J_CJ_C^*\) have traces \(|\alpha_i|^2/\sum_j|\alpha_j|^2\), whose sum is one.
Thus arbitrary nonunit amplitudes do not introduce a fractional component dimension.

The group words in the residual transports may be longer than the words in the original entries.
The induction reduces matrix size, not word length in the original chosen generators.
Its scalar endpoint is linear in the single actual holonomy group element, which is enough for the cyclic base case.
This is why the induction succeeds without preserving the original affine presentation literally.

## An ordered three-state example

Let \(a,b,c\in\mathbb C^\times\) and \(g,h,k\in G\), and set
\[
L=\begin{pmatrix}
1&-a\lambda(g)&0\\
0&1&-b\lambda(h)\\
-c\lambda(k)&0&1
\end{pmatrix}.
\tag{T4}
\]
Pivoting in the first and then the second coordinate uses only the scalar unit \(1\).
The final Schur element, with the third coordinate retained as root, is
\[
s=1-abc\lambda(kgh).
\tag{T5}
\]
The order \(kgh\) follows from \(x_3=c\lambda(k)x_1\), \(x_1=a\lambda(g)x_2\), and \(x_2=b\lambda(h)x_3\).
Therefore
\[
\operatorname{rk}_G L=2+\operatorname{rk}_G s,
\qquad
\dim_G\ker L=\dim_G\ker s.
\]
If \(abc=1\) and \(kgh=e\), then \(L\) has rank two and kernel dimension one.
In every other case \(L\) is an actual affiliated unit by the independently checked scalar base case.
No global integer character, ordering or Atiyah theorem for \(G\) is used.

## Application to the original rational border

Return to the original \((N+1)\)-square border with \(N\ge2\), \(u,v\ne0\), and the independently invertible denominator \(L\).
Use the constant changes in the [complementary-block reduction](Yin_L_A0005_v1.md#complementary-block-reduction-and-the-scalar-obstruction) to obtain its actual \((N-1)\)-square affine complementary block \(A\).
Suppose this actual block satisfies the two-monomial row condition above, and let \(f\) count its unpinned flat components.
The two independent rank identities then give
\[
\operatorname{rk}_G Q=2+\operatorname{rk}_G A=N+1-f,
\qquad
\operatorname{rk}_G r=1-f.
\tag{T6}
\]
Because a scalar affiliated rank lies in \([0,1]\), the independently known denominator admissibility forces \(f\le1\).
If \(f=1\), faithfulness gives \(r=0\); if \(f=0\), finite trace gives an actual affiliated inverse of \(r\), which lies in the same actual rational closure by inverse closure.
Thus this explicit condition on the original complementary block excludes the forbidden interval without a border-matching or positivity hypothesis.
An outcome \(f>1\) would contradict the stated denominator admissibility, rather than give a new fractional-rank case.
The case \(N=1\) and the zero-border cases retain the elementary conclusions already recorded in the complementary-block reduction.

## A sufficient condition that preserves affineness

Fix the same finite tuple \(X\) of actual group labels throughout this paragraph, and suppose every entry of \(L\) is affine in \(X\).
Suppose there exists a constant complex column \(v\in M_{n-1,1}(\mathbb C)\) such that
\[
c=va.
\tag{S3}
\]
The actual identity (S3) is a hypothesis to verify; it is not inferred from support similarities.
Then the constant elementary row operation gives
\[
\begin{pmatrix}1&0\\-v&I\end{pmatrix}
L
=\begin{pmatrix}a&b\\0&D-vb\end{pmatrix}.
\tag{S4}
\]
The smaller matrix \(D-vb\) remains affine in the original tuple, since only constant linear combinations of its entries were taken.
After the independently certified pivot \(a\) is eliminated, (S2) holds with
\[
S=D-vb.
\]
The computation of this smaller affine matrix itself requires no inverse.

There is a symmetric sufficient condition.
If a constant complex row \(u\in M_{1,n-1}(\mathbb C)\) satisfies
\[
b=au,
\tag{S5}
\]
then the constant column operation
\[
L\begin{pmatrix}1&-u\\0&I\end{pmatrix}
=\begin{pmatrix}a&0\\c&D-cu\end{pmatrix}
\tag{S6}
\]
leaves the affine smaller matrix \(S=D-cu\), again with (S2).
Constant invertible changes of row and column bases and constant permutations may be made before each step, since they preserve affine dependence and analytic rank.
The conditions (S3) and (S5) can therefore be sought after such changes, but their existence is an additional structural condition on the actual pencil.

## The torsion-free scalar base and a complete sufficient induction

If \(G\) is torsion-free and \(w\ne e\), every nonzero Laurent polynomial in \(w\) is an actual affiliated unit by the retained [bilateral-shift proof](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions).
In particular, for distinct \(g,h\in G\), the nonzero binomial
\[
\alpha g+\beta h
=g(\alpha+\beta g^{-1}h)
\tag{S7}
\]
is an actual unit whenever \((\alpha,\beta)\ne(0,0)\).
If one coefficient vanishes, this is a scalar multiple of a group unit; otherwise it follows from the infinite order of \(g^{-1}h\).
The same certificate permits finite products of such units and their already defined inverses, without assuming closure under arbitrary addition.

Here is a precise sufficient inductive hypothesis for an affine \(n\)-square pencil.
At every nonzero stage of size at least two, require a constant row and column basis change after which the upper-left scalar entry is independently certified by (S7), the cyclic Laurent test, or another already proved scalar-unit test, and either (S3) or (S5) holds.
Replace the matrix by the explicitly computed smaller affine matrix in (S4) or (S6).
At the terminal scalar stage, require either the exact zero identity or an independently certified scalar unit.
One may also stop at an exactly zero matrix of any size.

This hypothesis is sufficient because each step contributes rank exactly one by (S2), while the remaining matrix stays in the class to which the next structural test applies.
The size decreases by one, so the process terminates after at most \(n-1\) eliminations before the scalar stage.
If the process ends with the scalar \(s\), then
\[
\operatorname{rk}_G L=n-1+\operatorname{rk}_G s,
\qquad
\dim_G\ker L=\dim_G\ker s.
\tag{S8}
\]
The two permitted scalar outcomes give respectively rank \(n-1\) or rank \(n\), and kernel dimension one or zero.
If it stops earlier at a zero matrix of size \(k\), the same rank accounting gives rank \(n-k\) and kernel dimension \(k\).

Applied to an \((N+1)\)-square bordered matrix, a successful chain reaching a scalar zero or unit therefore excludes the forbidden interval \(N<\operatorname{rk}_G Q<N+1\).
Every inverse used by the diagonalizing multipliers was certified before its use, while the smaller affine matrices were calculated by constant operations alone.
This is more concrete than assuming that every successive rational Schur entry is a unit: the cyclic pivot identities and constant proportionality conditions are explicit sufficient tests on each actual smaller pencil.
It is not a proof that every torsion-free group-ring pencil admits such a chain.

## A pencil outside every constant weighted energy test

Let \(g,h\in G\) be distinct, set \(a=g-h\), and let \(b\in\mathbb CG\) be any affine entry in the chosen label tuple.
Consider
\[
L=\begin{pmatrix}a&b\\a&a+b\end{pmatrix}.
\tag{S9}
\]
There is no hypothesis that \(b\) is nonzero or invertible.
The constant operation subtracting the first row from the second gives
\[
\begin{pmatrix}1&0\\-1&1\end{pmatrix}
L
=\begin{pmatrix}a&b\\0&a\end{pmatrix}.
\tag{S10}
\]
The first pivot and final scalar are both the cyclic unit \(a\), so (S8) proves \(\operatorname{rk}_G L=2\) for every torsion-free \(G\) under the stated distinctness condition.
Equivalently, the upper triangular matrix in (S10) has the actual inverse
\[
\begin{pmatrix}
a^{-1}&-a^{-1}ba^{-1}\\0&a^{-1}
\end{pmatrix}.
\tag{S11}
\]
This supplies a direct inverse certificate using only the already justified \(a^{-1}\).

For a precise comparison with the energy criterion, specialize to \(G=F(g,h,k)\) and \(b=k\).
The character sending each free generator to one implements trace-preserving automorphisms \(\alpha_\theta\) with
\[
\alpha_\theta(L)=e^{i\theta}L.
\]
There is no nonzero scalar \(z\) and no constant positive definite \(W\in M_2(\mathbb C)\) such that
\[
H=\operatorname{Re}(zWL)\ge0.
\tag{S12}
\]
Indeed \(\alpha_\pi(H)=-H\) is positive whenever \(H\) is positive, hence \(H=0\).
Applying \(\alpha_{\pi/2}\) to this zero identity yields \(\operatorname{Re}(izWL)=0\), so both real and imaginary parts of \(zWL\) vanish.
Since \(z\) and \(W\) are invertible, this would give \(L=0\), contrary to \(a\ne0\).
This argument concerns the specified affine pencil and constant weights; it does not exclude energy tests after a different actual invertible transformation.

The example is already settled by cyclic units and constant triangular elimination, rather than by a new group-class theorem.
Its role is to show that this sufficient dimension induction can succeed even when every constant phase and positive weight fails the direct real-part test on the original pencil.
The character is used only for this comparison; the positive conclusion (S10)--(S11) requires no indicability assumption.

## Another closed class: injective positive real part

Let \(M\) be a finite von Neumann algebra with faithful normal tracial state \(\tau\), let \(U=\mathcal U(M)\), and let \(R\subset U\) be the actual rational closure of a unital star subalgebra.
Consider \(L\in M_n(R)\) with
\[
H=\operatorname{Re}L\ge0,
\qquad \operatorname{rk}_M H=n.
\tag{P1}
\]
No uniform positive lower spectral bound is assumed, and the entries of \(L\) may be unbounded.
The square roots and kernel projections used below belong to the ambient affiliated algebra or von Neumann algebra; only the elimination entries are claimed to remain in \(R\).
The accepted [finite-affiliated polar foundations](../audits/literature/MSY23/Yin_U004.md#ambient-algebra-domains-and-foundational-inputs) imply properness \(X^*X=0\Rightarrow X=0\) and \(\operatorname{rk}(X^*X)=\operatorname{rk}X\), including rectangular affiliated \(X\).
Indeed, polar decomposition identifies \(X^*X\) with \(|X|^2\), whose support is that of \(|X|\).

Write
\[
L=\begin{pmatrix}a&b\\c&D\end{pmatrix}.
\]
Since \(H^{1/2}\) is an actual unit, the column \(H^{1/2}e_1\) has rank one.
Hence
\[
\operatorname{Re}a=e_1^*He_1=(H^{1/2}e_1)^*(H^{1/2}e_1)
\]
is positive and has rank one.
It follows that \(a\) is an actual unit independently of the target \(L\).
To check this for an unbounded \(a\), let \(p\) be its right-kernel projection.
The identities \(ap=0\) and \(pa^*=0\) imply \(p(\operatorname{Re}a)p=0\), hence \(((\operatorname{Re}a)^{1/2}p)^*((\operatorname{Re}a)^{1/2}p)=0\).
Properness and the invertibility of \((\operatorname{Re}a)^{1/2}\) force \(p=0\), and finite trace gives \(a^{-1}\in U\).
Actual inverse closure gives \(a^{-1}\in R\).

Now form the Schur complement and its elimination column
\[
S=D-ca^{-1}b,
\qquad
V=\binom{-a^{-1}b}{I_{n-1}}.
\]
The exact affiliated identity \(LV=\binom{0}{S}\) yields
\[
\operatorname{Re}S=V^*HV=(H^{1/2}V)^*(H^{1/2}V)\ge0.
\tag{P2}
\]
The bottom identity block of \(V\) is a left inverse witness, so \(\operatorname{rk}V=n-1\).
Multiplication by the unit \(H^{1/2}\) preserves this rank, and the Gram-rank identity gives \(\operatorname{rk}(\operatorname{Re}S)=n-1\).
Thus \(S\) satisfies (P1) in size \(n-1\), and all its entries are in \(R\).
The exact Schur equivalence gives
\[
\operatorname{rk}L=1+\operatorname{rk}S,
\qquad \dim_M\ker L=\dim_M\ker S.
\tag{P3}
\]
Induction terminates at a scalar with positive injective real part, whose actual inverse was justified above.
Every scalar pivot is certified before its inverse is used.

For an initial group-ring pencil, torsion-freeness can independently establish (P1) through [C_A0003's cyclic or graph energy certificates](../claims/Yin_C_A0003_v1.md#statement).
For example, \(H=\sum_j C_j^*C_j(2-\zeta_jg_j-\overline{\zeta_j}g_j^{-1})\) is injective if every \(g_j\ne e\), \(|\zeta_j|=1\), and \(\bigcap_j\ker C_j=0\).
A positive constant left weight can first be applied to \(L\) when that is how the real-part certificate is supplied.
The induction itself works in any finite affiliated algebra and uses torsion-freeness only through that independent initial certificate.
This is the existing positive-energy conclusion with an explicit dimension-reduction proof and an enlarged rational intermediate class.

## Boundary of the sufficient conditions

The sparse transport class is closed under the indicated tree eliminations because substitutions multiply scalar group monomials and leave at most two transported terms in each remaining row.
A row with three unrelated monomial terms generally becomes a scalar sum with three or more group terms, for which torsion-freeness alone has not supplied the required injectivity proof in this investigation.
Thus the induction does not justify extending the sparse criterion to every affine group-ring row.

The positive-real-part class is closed under scalar Schur complements by (P2), but the Schur complement is generally rational rather than affine.
Insisting that every intermediate matrix stay affine would remove this valid sufficient induction without providing a replacement argument.
Conversely, merely allowing arbitrary rational remainders without a preserved certificate would reintroduce the original division-closure problem.

The unit-phase, unpinned transport case is already contained in C_A0003; arbitrary amplitudes and pins are direct elementary variations of its kernel transport proof.
The present argument adds the explicit strict dimension descent and its independently certified scalar endpoint, without claiming a new Atiyah group class.
The positive class likewise retains its already established energy coverage.
Neither construction proves that every affine matrix can be moved into either class by independently certified transformations.


## Consequence for the general induction attempt

The sparse criterion requires a bound on monomial terms in each entire row, not merely two nonzero entries that may themselves be arbitrary affine sums.
Its group-word tests use actual equality in the given group; no uniform algorithm for an arbitrary group's word problem is asserted.
The constant-proportionality criterion preserves the original affine tuple, whereas the transport criterion permits longer group words and the energy criterion permits rational entries.
Each changes a different complexity while keeping an independently justified scalar test available.

For an arbitrary affine pencil, torsion-freeness alone has not supplied any of these preserved structures.
Already a scalar affine entry in an enlarged support tuple can be any finite complex group-ring sum, and the cyclic no-eigenvector proof does not apply to that entire class.
After an arbitrary Schur step, the missing scalar can instead be a noncommutative rational expression.
Assuming all its nonzero possibilities are invertible would assume the division-ring side of the [MSY23 criterion](Yin_L_A0004_v1.md#setting-and-exact-criteria).
Likewise, replacing an unproved matrix by its positive square does not independently certify injectivity of that square.

The useful next extension is therefore a class that permits more than two additive transport terms while remaining closed under independently justified eliminations, or another explicit source of certified pivots and controlled Schur remainders.
The dense cyclic-pivot example above shows that sparsity is sufficient but not necessary.
Its successful elimination is already covered by cyclic units, and the free-group instance used to exclude the original constant-weight energy test is also a known Atiyah case.
No transformation of every actual affine pencil into these classes has been established, and the full Task remains unresolved.
