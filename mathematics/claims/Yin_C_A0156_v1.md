---
author: Yin
---

# Rational kernel projections from varying witnesses in amenable group limits

## Statement

Let \(G\) be a finitely generated amenable group with a fixed marking, and let \(X\in M_{a,b}(\mathbb CG)\).
Write \(U_G\) for the affiliated operator algebra and \(D_G\) for the division closure of \(\mathbb CG\) in \(U_G\).
Choose finite word lifts for \(X\) in the free group on the marking.
Take either a sequence of groups \(G_i\) converging to \(G\) in the topology of marked groups or a sofic approximation of \(G\) by finite permutation models \(\Omega_i\).
In the first case write \(r_i\) for unnormalized matrix rank in the canonical group trace of \(G_i\).
In the second case let \(r_i\) be ordinary matrix rank divided by \(|\Omega_i|\).
Evaluate words, sums and products using the marked generators, and denote the resulting evaluation of \(X\) by \(X_i\).

The kernel projection \(p_{\ker X}\) has entries in \(D_G\) if and only if there exist a fixed integer \(h\ge1\), a fixed finite set of words \(W\), and matrices \(L_i,\alpha_i,\beta_i\) of sizes \(h\times h,b\times h,h\times a\), respectively, whose entries are linear combinations of the evaluated words of \(W\), such that
\[
 \lim_i r_i(L_i)=h,\qquad
 \lim_i r_i\begin{pmatrix}L_i&\beta_i X_i\\ X_i\alpha_i&X_i\end{pmatrix}=h. \tag{1}
\]
The complex coefficients of all three matrices may depend arbitrarily on \(i\).
It suffices that (1) holds along a common infinite subsequence.
In particular, if the approximating groups provide exact rational inner inverses with uniform realization sizes and word supports for each \(X\), then \(D_G\) is regular and the [unrestricted equation](../tasks/Yin_T_A0003_v3.md#contract) detects rationality in \(G\).
The bounds may depend on \(X\).
The same conclusion holds under the two limiting rank conditions for each \(X\).

For every rectangular matrix with fixed finite word supports, model rank converges to the canonical \(G\)-rank uniformly over all complex coefficients on those supports.
Along a subsequence, the varying coefficient matrices in (1) admit a single specialization over \(\mathbb C\) preserving both limiting ranks.
The resulting inner inverse uses the same matrix sizes and words.
For approximating groups with division-ring division closure, coordinate submatrices give uniform bounds directly.
In a finite group \(Q\), let \(g\in Q\) have image of order \(d\) in the abelianization.
If an exact inner inverse of \(1-g\) has a realization of size \(h\) whose entries in the pivot, input and output together use \(s\) group elements, then \(d\le s^h+2s^{h+1}\).
Consequently even in cyclic quotients of \(\mathbb Z\), fixed size and bounded support cardinality cannot provide exact inner inverses for all quotient orders.

## Argument

### Rank estimates from a finite window

Consider an \(m\)-by-\(n\) word matrix \(B\).
In \(G\) let \(S\) contain the identity and the images of its supporting words.
For a finite nonempty \(F\subseteq G\) put \(E=SF\), and write \(q\) for the ordinary complex rank of the map \(B_F:\mathbb C[F]^n\to\mathbb C[E]^m\) obtained by restriction of the input.
The [coset compression trace formula](Yin_C_A0134_v1.md#finite-coset-matrices) with the trivial subgroup gives
\[
                   q/|E|\ \le\ r_G(B)\ \le\ q/|F|.                 \tag{2}
\]
In fact the finite image of dimension \(q\) lies inside the global closed image and is supported on \(E\).
The trace of the global range projection compressed to \(E\) is \(|E|r_G(B)\).
Extending finite kernel vectors by zero embeds their \(n|F|-q\) dimensional space into the global kernel on inputs supported on \(F\).
The compressed kernel projection therefore has trace at least \(n|F|-q\), giving the other inequality.
These estimates apply for every coefficient choice.

Fix word representatives of \(F,E\).
Convergence of marked groups preserves all equalities and inequalities in these finite sets and all products of a supporting word with a representative of \(F\) for all sufficiently large \(i\).
Thus the identical finite matrix with the same coefficients computes \(q\) in \(G_i\), and (2) bounds its global rank there as well.
The width of the interval in (2) is at most \(n(1-|F|/|E|)\).
Amenability makes this as small as desired by choosing \(F\), independently of the coefficients and of the approximating groups.

For a finite permutation model, represent the marked generators by permutations, evaluate their inverses by inverse permutations, and evaluate a longer word by composition.
Let \(\delta_i\) be the proportion of roots where these finite sets and products are not reproduced.
Soficity gives \(\delta_i\to0\) for fixed \(F\) and word lists.
At every good root \(v\), the matrix applied to inputs on \(Fv\) is a copy of \(B_F\).
Its image of dimension \(q\) is supported on \(Ev\), and its \(n|F|-q\) dimensional kernel is supported on \(Fv\).
Their dimensions are bounded by the traces of the corresponding global projections compressed to these sets.
For each chosen representative word \(w\), the sum over all roots \(v\) of a diagonal entry at \(wv\) equals the full trace in that coordinate, since the word acts by a permutation.
Summing the lower bounds from good roots, and using nonnegativity at every other root, gives
\[
 (1-\delta_i)q/|E|\ \le\ r_i(B_i)\
      \le\ \delta_i n+(1-\delta_i)q/|F|.                          \tag{3}
\]
The two errors compared with (2) are at most \(n\delta_i\) at their respective endpoints.
First choose a Følner window and then let \(i\) grow to obtain the asserted coefficient-uniform convergence.
In (2) and (3) the coefficients can themselves be polynomial functions of other complex parameters, since the same bounds hold for every value of every coefficient.

### Specializing all the model coefficients

Suppose (1) holds along a common subsequence.
Write the coefficients of the three word matrices as tuples \(c_i\in\mathbb C^s\), choosing one expansion in case the evaluated words are dependent.
Let \(K\subset\mathbb C\) be the countable field generated over \(\mathbb Q\) by the coefficients of \(X\).
List all polynomials in \(K[t_1,\ldots,t_s]\).
By successive infinite subsequences and diagonal selection we can suppose that for every polynomial \(P\) the condition \(P(c_i)=0\) is eventually always true or eventually always false.
The eventually vanishing polynomials form a proper prime ideal \(I\).
Indeed if neither of two factors vanishes eventually, both are nonzero on the same tail, so their product stays nonzero there.
The fraction field of \(K[t_1,\ldots,t_s]/I\) is finitely generated over \(K\).
It embeds in \(\mathbb C\) over \(K\) by sending a transcendence basis to algebraically independent complex numbers and extending across the finite algebraic extension.
Such independent numbers can be chosen successively since the algebraic closure in \(\mathbb C\) of any countable field adjoined finitely many complex numbers is countable.
Let \(c\in\mathbb C^s\) be the images of the coordinate classes.
For each \(P\), vanishing at \(c\) agrees with eventual vanishing at \(c_i\).

In every fixed window the minors of the matrices for \(L\) and the border in (1) are polynomials over \(K\) in the coordinates of \(c\).
Hence their finite ranks at \(c_i\) eventually equal those at \(c\), for both matrices at once.
For each window, (2) and, when needed, (3) put the limiting model rank and the group rank at \(c\) inside the same closed interval.
Letting the window boundary ratio tend to zero gives \(r_G(L(c))=r_G(J(c))=h\), where \(J\) denotes the border in (1).
No convergence of the original complex numbers in the usual topology is required.

### The inner inverse and its uniformity

The square \(L(c)\) is an affiliated unit, so its inverse has entries in \(D_G\) by [scalar Gram elimination](Yin_C_A0132_v1.md#argument).
Schur elimination gives
\[
 r_G(J(c))=h+r_G(X-XYX),\qquad Y=\alpha(c)L(c)^{-1}\beta(c).
\]
The equality of ranks yields \(XYX=X\) by faithfulness.
The idempotent \(I_b-YX\) generates the affiliated kernel of \(X\), and the [orthogonalization of this idempotent](Yin_C_A0144_v1.md#inner-inverses-and-the-two-rank-limits) gives \(p_{\ker X}\) over \(D_G\).
Conversely, a rational kernel projection gives the inner inverse \((X^*X+p_{\ker X})^{-1}X^*\).
Its fixed group-ring realization yields rank \(h\) for both matrices in \(G\) by the same Schur formula.
The uniform approximation proved above sends these fixed ranks to the two limits in (1).
The [matrix kernel criterion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) gives the conclusion concerning all inputs and the unrestricted equation.

For example, suppose each \(D_{G_i}\) is a division ring.
If \(X_i\) has positive rank \(s_i\) over \(D_{G_i}\), choose an invertible \(s_i\)-by-\(s_i\) coordinate submatrix \(A_i\) of \(X_i\).
Insert \(A_i^{-1}\) in the corresponding transposed positions of a \(b\)-by-\(a\) matrix \(Y_i\) and put zero elsewhere.
Elimination on \(A_i\) leaves a zero Schur complement because \(s_i\) is the rank, giving \(X_iY_iX_i=X_i\).
Use \(A_i\) padded by identities to size \(\max(1,\min(a,b))\) and constant coordinate matrices in the realization.
If \(X_i=0\) take an identity pivot and zero output.
These exact witnesses use only the original words and the identity, uniformly in \(i\).

For the finite group assertion, map the realization \(Y=\alpha L^{-1}\beta\) and the inner-inverse identity to \(\mathbb C[Q_{\mathrm{ab}}]\).
The original pivot is invertible in the matrix ring over \(\mathbb CQ\), since \(Q\) is finite, so its image remains invertible.
Write \(u\) for the image of \(g\) and use bars for the images of the coefficient matrices.
In this commutative group algebra put \(\Delta=\det\bar L\), \(P=\bar\alpha\operatorname{adj}(\bar L)\bar\beta\), and \(B=(1-u)P-\Delta\).
The inner-inverse identity gives \((1-u)B=0\) after multiplication by the unit \(\Delta\).
Evaluation at the trivial character sends \(B\) to the negative of the nonzero value of \(\Delta\).
Thus \(B\ne0\) and its coefficient function is constant on cosets of \(\langle u\rangle\), giving at least \(d\) elements in its support.
Let \(V\) be the image in \(Q_{\mathrm{ab}}\) of the union of all entry supports.
Determinant and adjugate expansion put the support of \(B\) inside \(V^h\cup V^{h+1}\cup uV^{h+1}\), where \(V^j\) is the set of products of \(j\) elements of \(V\).
Since \(|V|\le s\), the asserted bound follows.
For \(G=\mathbb Z=\langle g\rangle\) and its order-\(i\) cyclic quotients we have \(d=i\).
Nevertheless the size-one choice \(L_i=1-g,\ \alpha_i=\beta_i=1\) gives both normalized ranks \(1-1/i\), as in the [cyclic quotient calculation](Yin_C_A0144_v1.md#a-singular-pivot-in-every-finite-model).
Thus (1) permits pivot loss tending to zero even when every exact model inner inverse requires growing complexity.
Obtaining bounded witnesses for every group-ring matrix in an arbitrary torsion-free amenable group remains open.

## Assessment history

### Decision amenable-witness-limits

| Field | Value |
| --- | --- |
| date | 2026-11-25T12:59 |
| status | proved |
| reason | Uniform finite-window estimates and simultaneous specialization turn limiting rank witnesses of fixed size and support into one exact inner inverse. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The two model rank limits, coefficient uniformity, the division-ring and finite abelianization consequences. |
| argument | [Argument](#argument) | Finite-window trace inequalities, stabilization of minors, Schur elimination and the finite-quotient support bound. |
| dependency | [Finite windows](Yin_C_A0134_v1.md#finite-coset-matrices) | Trace estimates for finite coset compressions. |
| dependency | [Matrix inverse closure](Yin_C_A0132_v1.md#argument) | Gram elimination of an affiliated unit. |
| dependency | [Inner inverses](Yin_C_A0144_v1.md#inner-inverses-and-the-two-rank-limits) | The bordered rank identity and recovery of the orthogonal kernel projection. |
| dependency | [Complete deletion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) | The all-matrix kernel characterization. |
| review | [Amenable limits](../audits/reviews/Yin_R_A0172_v1.md#amenable-limits) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-amenable-witness-limits)
