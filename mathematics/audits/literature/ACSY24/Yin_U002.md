---
author: Yin
---

# ACSY24: Matrix Models and Group Atiyah Interfaces

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Source: ACSY24, the retained 73-page published [PDF](../../../literature/pdf/ACSY24.pdf) |
| source-locator | Exact coverage: Definition 2.16, p. 19; Lemma 2.20 and proof, p. 21; Theorem 2.31 and Remark 2.32, p. 29; Theorem 4.1 and proof, pp. 39-41; Remark 4.2 and Proposition 4.3 with proof, pp. 41-42; Corollary 4.4 and surrounding finite-group argument, pp. 42-43. |
| inspection | Method: the complete selected passages were text-read from the retained published PDF with Calibre `pdftotext`, and the rank normalizations and group/Laurent interfaces were reconstructed. |

<a id="acsy24-u002"></a>
## ACSY24-U002: Selected Rank and Group Statements

- Date and reviewer: 2026-09-11; the polynomial-core research agent, following the independent review of the finite-vertex reproduction.
- Source: ACSY24, the retained 73-page published [PDF](../../../literature/pdf/ACSY24.pdf)
- Exact coverage: Definition 2.16, p. 19; Lemma 2.20 and proof, p. 21; Theorem 2.31 and Remark 2.32, p. 29; Theorem 4.1 and proof, pp. 39-41; Remark 4.2 and Proposition 4.3 with proof, pp. 41-42; Corollary 4.4 and surrounding finite-group argument, pp. 42-43.
- Method: the complete selected passages were text-read from the retained published PDF with Calibre `pdftotext`, and the rank normalizations and group/Laurent interfaces were reconstructed.
  No whole-paper audit or page-by-page visual review is claimed.

This unit is separate from [ACSY24-U001](Yin_U001.md#acsy24-u001), which concerned Proposition 3.5.
The earlier small-core audit did not establish the group matrix-model interfaces below.

## 1. Rank Conventions and Linearization

The source uses a Sylvester rank function normalized on the scalar identity, \(\operatorname{rk}(1)=1\), and **unnormalized** on larger matrix identities: \(\operatorname{rk}(I_s)=s\).
For finite tracial operator algebras this is the trace of the range projection with the unnormalized matrix trace.
Passing to a probability trace on \(M_n(\mathcal M)\) introduces a separate factor \(1/n\).

Definition 2.16 assigns to a scalar rational expression R a formal linear representation \((u,Q,v)\) of finite size k.
Q is an affine linear k-by-k matrix over the free polynomial algebra, u and v have complex scalar entries, and the source's sign convention is
\[
R(Z)=-uQ(Z)^{-1}v.
\]
The definition includes the domain requirement: wherever R is evaluable in a complex algebra, the whole evaluated Q is invertible there.
It is a construction for a specified expression with all its intermediate inverses defined, not a theorem that any bounded affiliated rational output has a bounded inverse representation.

For an input tuple Z over \(M_s(\mathcal B)\), Lemma 2.20 gives, with the display \(L=\begin{pmatrix}0&u\\v&Q\end{pmatrix}\),
\[
\operatorname{rk}_{\mathcal B}R(Z)+sk
=\operatorname{rk}_{\mathcal B}L(Z).
\tag{1}
\]
The proof multiplies L by invertible block matrices and obtains the diagonal matrix with entries \(R(Z)\) and \(I_{sk}\).
Thus the subtraction is sk, not merely k when s is greater than one.
The proof needs the actual inverse of \(Q(Z)\); maximal rank in an arbitrary unital ring is not silently used to supply one.

For a group-algebra matrix built from unitary generators and their inverses, introduce the diagonal generators \(I_s\otimes u_i\) and constant matrix units as extra input variables.
Every requested inverse exists in \(M_s(\mathcal N(G))\).
After evaluating the matrix units, the display has entries polynomial in the unstarred generators.
Equation (1) therefore transfers polynomial-matrix rank integrality to Laurent/group-algebra matrices.
Padding by zeros handles rectangular matrices without changing their rank.

## 2. Theorem 4.1: A Common Denominator Matrix Model

Let \(X_1,\ldots,X_d\) be *-free bounded normal variables in a tracial \(W^*\)-probability space.
Assume **one common integer** n makes every atomic mass of every marginal an integer multiple of \(1/n\).
The nonatomic parts are arbitrary; all-atomless marginals permit n=1.

For coordinate i, repeat its atoms according to their multiplicities and form a diagonal n-by-n matrix \(\overline D_i\).
Its remaining diagonal entries are fresh free indeterminates, one for each unfilled position.
Let \(\overline U_i\) be n-by-n generic matrices whose entries are additional, mutually free indeterminates.
All these variables lie in one free skew field \(\mathbb F\).
The generic matrices are full and invertible over \(\mathbb F\), and set
\[
\overline X_i=\overline U_i\overline D_i\overline U_i^{-1}.
\]
For **every** positive integer m and every m-by-m unstarred polynomial matrix A, the source proves
\[
\operatorname{rk}_{\mathcal M}A(X)
=\frac1n\operatorname{rk}_{\mathbb F}A(\overline X)
\in\frac1n\mathbb Z.
\tag{2}
\]
The matrix on the right has size nm and ordinary integer skew-field rank.
Its possible ranks give values between zero and m on the left.
Neither m nor n may be dropped from their respective roles.

The second part of Theorem 4.1 matches domains of rational expressions in \(L^0(\mathcal M)\) and \(M_n(\mathbb F)\), and computes the corresponding atomic masses through the normalized rank of \(\lambda-R(\overline X)\).
Inverse existence is in these specified ambient algebras.
This is not an assertion about bounded inverses in \(\mathcal M\).

The inspected proof constructs compressed free Haar unitary matrices and diagonal variables having the desired atomic/non-atomic law.
The entries of the Haar matrices and the diffuse diagonal coordinates jointly maximize Delta.
The source's Theorem 2.31/Remark 2.32, imported from MSY23, then identify their affiliated rational algebra with a free field and preserve matrix ranks.
The free-conjugation construction has the desired joint law, so trace ranks agree.
The source's Proposition 3.9 supplies the relevant matrix/scalar freeness step.
These cited foundations are retained inputs, not independently reproved by this unit.

The source temporarily calculates some amplified ranks with the unnormalized matrix trace.
Formula (2) is the final probability-trace normalization; it must remain explicit when extracting an Atiyah denominator.

## 3. Proposition 4.3: Entire Vertex Algebras Are Modeled

In the exact source setting, let \(\gamma_1,\ldots,\gamma_\ell\) lie in a tracial \(W^*\)-probability space with
\[
\Delta(\gamma_1,\ldots,\gamma_\ell)=\ell.
\]
Let \(A_1,\ldots,A_d\) be complex subalgebras of the **same** \(M_n(\mathbb C\langle\gamma_1,\ldots,\gamma_\ell\rangle)\), with the trace inherited from that ambient representation.
The source permits \(\ell=0\), in which case these are subalgebras of \(M_n(\mathbb C)\).
It does not require the \(\gamma_j\) themselves to be normal.

Maximal Delta makes the evaluation map \(\Phi:\mathbb C\langle y\rangle\to\mathbb C\langle\gamma\rangle\) an isomorphism, so it can be inverted entrywise.
In a free field containing the y variables and the fresh entries of generic matrices \(\overline U_i\), define
\[
\overline A_i=\overline U_i\Phi^{-1}(A_i)\overline U_i^{-1}
\subseteq M_n(\mathbb F).
\]
Proposition 4.3 identifies the represented tracial free product of the original algebras with the algebra generated by the \(\overline A_i\), preserving matrix ranks.
With probability traces, the model side again uses \(1/n\) times the ordinary skew-field rank.
The proposition retains **all relations inside each \(A_i\)**.
It is stronger than a theorem only about separately chosen scalar marginal variables.

The short proof was read completely.
It replaces the generic matrices by the compressed Haar unitary matrices of Theorem 4.1, whose conjugated algebras are free with their original traces, and uses the same maximal-Delta rank-preserving evaluation.
The general matrix-freeness and free-field foundations remain accepted at the source interfaces described above.

Two limitations of this model matter.
First, an abstract strong-Atiyah algebra is not automatically supplied as an \(A_i\) inside this particular polynomial matrix model with its analytic rank.
Second, independent conjugation of two copies of a nontrivial edge algebra does not preserve their prescribed identification.
Proposition 4.3 is an ordinary free-product result; it does not assert the corresponding amalgamation over an arbitrary finite-dimensional edge algebra or an HNN extension theorem.

## 4. Corollary 4.4 and the Closures It Actually Addresses

For finite groups \(G_1,\ldots,G_d\), let \(n=\operatorname{lcm}_i|G_i|\).
Represent \(\mathbb CG_i\) by its regular matrices, repeated \(n/|G_i|\) times.
The normalized matrix trace then equals its canonical group trace.
Proposition 4.3 with \(\ell=0\) applies to these full group algebras, not only to cyclic subgroups.
Corollary 4.4 proves strong Atiyah for \(G_1*\cdots*G_d\), with denominator n and an explicit normalized free-field matrix rank model.

This is an existing external theorem and needs no project Claim proving it again.
It improves the product-denominator construction to the least common multiple in this case.

The continuation on p. 43 describes corresponding rational/division closures in the affiliated group algebra and in the free-field matrix model, obtained from rank preservation and the specialization argument behind Corollary 2.22.
The scalar division closures correspond because the maps preserve the relevant scalar inverse operations.
The slash notation is not used here to assert a general equality of matrix rational closure and scalar division closure.

In particular:

- An algebra embedded in \(M_n(\mathbb F)\) need not itself be a division ring when torsion is present.
- Invertibility in \(M_n(\mathbb F)\) or in the affiliated algebra does not imply bounded invertibility in \(\mathcal M\).
- The source does not supply \(\operatorname{Div}_{L^0(\mathcal M)}A\cap\mathcal M=\operatorname{Div}_{\mathcal M}A\) from these rank models alone.
- The finite-group result is proved over \(\mathbb C\), and therefore holds on matrices over any \(K\subseteq\mathbb C\) by restriction.
  No arbitrary-vertex base-change theorem from K to \(\mathbb C\) is thereby obtained.

## 5. Acceptance and Review Boundary

The exact statements, the selected linearization/Schur proof, the common-dimension normalization, and the finite-group and Laurent applicability checks are accepted for the recorded consumers.
A separate finite-vertex application review also checked the selected source passages.
That review is evidence for that application, not a whole-source proof audit.

No new manuscript definition index, main theorem, Claim ID, or bibliography identity is created by this unit.
No numerical experiment, formal verification, external human review, or historical-priority claim is made.
The original published PDF and U001 remain unchanged.
