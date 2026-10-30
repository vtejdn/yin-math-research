---
author: Yin
---

# Relative free Fisher information and its inequalities

<a id="voi98-u006"></a>

## Voi98-U006 — Definition, projection, Stam, and Cramer-Rao

- Source: [Voi98](../../../literature/pdf/Voi98.pdf), retained published journal version; artifact metadata belongs to the [literature registry](../../../literature/readme.md).
- Locator: Section 6, Definition 6.1 through Proposition 6.9, printed pp. 213-218 / PDF pp. 25-30.
- Record: 2026-09-08; local proof reconstruction and self-review by the BR10/Fisher-information agent; independent mathematical review by the coordinating agent found no gap in the recorded scope.
- Kind and coverage: definition and related inequality group; audited within the scope and dependencies below.
- Purpose: [Voi98 finite-Fisher source audit](readme.md#voi98-finite-fisher-source-audit); supplies the analytic bounds used in [Voi98-U007](Yin_U007_v1.md#voi98-u007) and Section 7's entropy construction.

### Setting and exact definition

Work in a finite von Neumann algebra \(M\) with faithful normal tracial state \(\tau\).
The tuples \(X=(X_1,\ldots,X_n)\) and \(Y\) consist of bounded selfadjoint elements, \(n\ge1\); coefficient algebras are unital star subalgebras.
For a subalgebra \(D\), \(E_D\) means the orthogonal projection onto \(L^2(W^*(D),\tau)\), equivalently the trace-preserving conditional expectation extended to \(L^2\).
Neither an algebraic coefficient algebra nor its polynomial span is assumed closed.

Write \(B_j=B[X_1,\ldots,\widehat X_j,\ldots,X_n]\), \(N=W^*(B,X_1,\ldots,X_n)\), and \(\xi_j=\mathcal J(X_j:B_j)\).
These are the canonical conjugates in \(L^2(N)\), with moment identity

\[
 \tau(\xi_j P(X))=(\tau\otimes\tau)(\partial_jP(X)),
 \qquad \partial_jX_i=\delta_{ji}1\otimes1,\quad \partial_jB=0.
\]

The first-order definition, its algebraic-freeness convention, and the existence/uniqueness interface are in [Voi98-U002](Yin_U002_v1.md#voi98-u002).
Define

\[
 \Phi^*(X:B)=\sum_{j=1}^n\|\xi_j\|_2^2
\]

when every conjugate exists in \(L^2\), and \(+\infty\) otherwise.
Scalars are the default coefficient algebra when the colon is omitted.
In particular, \(\tau(\xi_j)=0\) and \(\tau(\xi_jX_i)=\delta_{ji}\).
Finite information is strictly positive: each identity with \(i=j\) excludes a zero conjugate.
A tuple consisting entirely of zero operators has infinite information.

### Projection, scaling, and free extension: Remarks 6.2 and Propositions 6.3-6.4

For \(\lambda\in\mathbb R\setminus\{0\}\), direct substitution in the moment relation gives \(\mathcal J(\lambda X_j:B[\lambda X_{\ne j}])=\lambda^{-1}\xi_j\), so \(\Phi^*(\lambda X:B)=\lambda^{-2}\Phi^*(X:B)\).
The converse substitution handles the infinite case.
No formula at \(\lambda=0\) is asserted.

If \(B\subset A\subset M\), the correct projection identity is

\[
 E_{B[X_1,\ldots,X_n]}
 \mathcal J(X_j:A[X_{\ne j}])
 =\mathcal J(X_j:B[X_{\ne j}]).
\]

It follows by testing all polynomials in the smaller generated algebra and using uniqueness; the projection is contractive.
Summing gives \(\Phi^*(X:B)\le\Phi^*(X:A)\), with the infinite case interpreted in the extended order.

**Printed error, p. 214:** Remark 6.2(c) omits \(X_j\) from the expectation's subscript and uses \(X_i\) on the right.
The subscript must contain the entire tuple and the right-hand variable must be \(X_j\).
For \(n=1\), \(B=A=\mathbb C\), and standard semicircular \(X\), the printed expectation would give \(\tau(X)=0\), whereas the conjugate is \(X\).
This is a mathematical projection error, not a harmless notation convention; the stated monotonicity survives the repair.

The free-extension result of Proposition 3.6, checked in [Voi98-U003](Yin_U003_v1.md#voi98-u003), preserves each conjugate when a freely independent coefficient algebra is adjoined.
In particular,

\[
 \Phi^*(X:B\vee C)=\Phi^*(X:B)
 \quad\text{if }C\text{ and }B[X]\text{ are free}.
\]

If \(B[X]\) and \(C[Y]\) are free, applying that result to each coordinate yields

\[
 \Phi^*(X,Y:B\vee C)=\Phi^*(X:B)+\Phi^*(Y:C).
\]

Without freeness the same equality is replaced by \(\ge\), by projecting each joint conjugate onto the appropriate separate generated algebra.
These statements include infinite values: finite joint information would force finite separate information by projection, and free extension gives existence in the reverse direction whenever the separate conjugates exist.
The proof of Proposition 6.3 has minor terminal-index/case slips in its \(Y\)-lists; the coefficient algebra for its \(Y_k\) conjugate contains precisely all other \(Y\)'s and the entire \(X\)-tuple.

### Free Stam inequality: Proposition 6.5

For equal-length tuples with \(B[X]\) free from \(C[Y]\),

\[
 \frac1{\Phi^*(X+Y:B\vee C)}
 \ge \frac1{\Phi^*(X:B)}+\frac1{\Phi^*(Y:C)},
 \qquad \frac1{+\infty}:=0.
\]

The projection formula for sums (Proposition 3.7, [Voi98-U003](Yin_U003_v1.md#voi98-u003)) is the essential input.
Let \(P\) project onto \(L^2(W^*(B,C,X+Y))\), and let \(h_1,h_2\in L^2(M)^n\) be the two separate conjugate vectors when they exist.
Then the conjugate vector of the sum is \(h_3=Ph_1=Ph_2\).
The projections onto the two separate free algebras compose to the scalar expectation.
Since each conjugate is centered, \(h_1\perp h_2\).

Set \(f_i=(1-P)h_i\).
Orthogonality of the projection decomposition gives

\[
 0=\langle h_1,h_2\rangle
   =\|h_3\|_2^2+\langle f_1,f_2\rangle,
 \qquad
 \|f_i\|_2^2=\|h_i\|_2^2-\|h_3\|_2^2.
\]

Cauchy-Schwarz therefore implies, with \(a=\|h_1\|_2^2\), \(b=\|h_2\|_2^2\), and \(c=\|h_3\|_2^2\), \(c^2\le(a-c)(b-c)\), hence \(c(a+b)\le ab\).
All three quantities are positive and finite here, so division yields the claimed reciprocal inequality.

If just one input information is finite, Proposition 3.7 still constructs the sum conjugate by projecting that input; contraction gives \(\Phi^*(X+Y:B\vee C)\le\Phi^*(X:B)\), or its symmetric version.
This is exactly the required inequality with one reciprocal zero.
If both are infinite, the inequality merely says that a nonnegative reciprocal is at least zero.
No undefined subtraction of infinite quantities is used.
The source does not give a characterization of equality in Stam's inequality, and none is inferred here.

### Real linear transformations: Remark 6.6, Lemma 6.7, Corollary 6.8

Let \(A=(a_{ij})\in GL_n(\mathbb R)\) and \(Y=AX\).
Real coefficients preserve selfadjointness, while invertibility gives \(B[X]=B[Y]\).
Checking the values on \(B\) and all generators proves the chain rule

\[
 \begin{pmatrix}\partial_{Y_1}\\\vdots\\\partial_{Y_n}\end{pmatrix}
 =A^{-T}
 \begin{pmatrix}\partial_{X_1}\\\vdots\\\partial_{X_n}\end{pmatrix}.
\]

For finite information, the adjoint-at-\(1\otimes1\) identity gives \(\xi_Y=A^{-T}\xi_X\), equivalently \(\xi_X=A^T\xi_Y\).
This is an identity between vectors in the common \(L^2\) space.
Adjoint-domain membership passes through finite real linear combinations by the defining bounded-functional criterion; no equality between unspecified maximal adjoint domains is needed.
Thus

\[
 \|A^{-1}\|^{-2}\Phi^*(Y:B)
 \le\Phi^*(X:B)
 \le\|A\|^2\Phi^*(Y:B).
\]

Applying the same construction to \(A^{-1}\) shows finite information is equivalent on both sides; the extended inequalities also hold when both values are infinite.
For orthogonal \(A\), the norms are equal.
A complex invertible matrix or a nonlinear change of variables is outside this assertion.
The displayed \(B[Y_1,\ldots,Y_k]\) in Lemma 6.7's opening line must end at \(Y_n\); its proof and statement concern the full tuple.

### Free Cramer-Rao: Proposition 6.9, including equality

Put \(C^2=\tau(\sum_jX_j^2)=\sum_j\|X_j\|_2^2\).
The unambiguous extended formulation is

\[
 \Phi^*(X:B)\ge\frac{n^2}{C^2}\quad(C^2>0),
 \qquad \Phi^*(X:B)=+\infty\quad(C^2=0).
\]

For finite information, apply Cauchy-Schwarz in \(L^2(M)^n\) to the vectors \(\xi\) and \(X\):

\[
 n=\sum_j\tau(\xi_jX_j)
 \le\Bigl(\sum_j\|\xi_j\|_2^2\Bigr)^{1/2}
       \Bigl(\sum_j\|X_j\|_2^2\Bigr)^{1/2}.
\]

When \(C^2=0\), faithfulness forces every \(X_j=0\), which contradicts the defining identity \(\tau(\xi_jX_j)=1\) for a finite conjugate.
The source's multiplicative formulation should not be read as assigning a value to \(0\cdot\infty\).

Equality at finite \(C^2>0\) holds exactly when \(\xi_j=\lambda X_j\) for every \(j\), with a common **positive** \(\lambda\).
Positivity follows from \(\lambda\|X_j\|_2^2=1\); a negative scale is impossible.
The relations also give \(\tau(X_j)=0\) and \(\tau(X_j^2)=\lambda^{-1}\).
For an arbitrary word of length \(m\), the moment recursion is

\[
 \tau(X_jb_0X_{i_1}b_1\cdots X_{i_m}b_m)
 =\lambda^{-1}\sum_{k=1}^m\delta_{j,i_k}
  \tau(b_0X_{i_1}b_1\cdots X_{i_{k-1}}b_{k-1})
  \tau(b_kX_{i_{k+1}}b_{k+1}\cdots X_{i_m}b_m).
\]

Empty variable strings retain their endpoint coefficient, so the first factor at \(k=1\) is \(\tau(b_0)\) and the second at \(k=m\) is \(\tau(b_m)\).

**Printed error, p. 218:** the second trace in Proposition 6.9's recursion starts with \(b_{k+1}\), losing \(b_k\).
The correct tensor cut includes \(b_k\) on the right as above.
For a one-letter word, its loss would already fail the defining relation for arbitrary \(b_0,b_1\).

This recursion determines all joint moments from \(\tau|_B\): by traciality any mixed word containing an \(X\) can be cyclically written with an \(X_j\) first, and each right-hand trace has strictly fewer variable occurrences.
Induction on that number therefore determines the moment.
A centered free semicircular family of common variance \(\lambda^{-1}>0\), free from \(B\), satisfies precisely the same recursion, because its conjugates are \(\lambda X_j\) (Propositions 3.6 and 3.8).
Consequently it has the same joint distribution with the coefficient algebra, proving necessity as well as sufficiency.
Thus the equality family has equal centered nondegenerate semicircle distributions and \(B,\{X_1\},\ldots,\{X_n\}\) free.
This is a statement about joint tracial distribution, not a claimed isomorphism fixing an arbitrary larger ambient algebra.

### Dependencies and verification limits

The proof chain uses the first-order moment/uniqueness and coefficient-projection interfaces in [Voi98-U002](Yin_U002_v1.md#voi98-u002), and the free-extension, free-sum, and semicircular conjugate interfaces in [Voi98-U003](Yin_U003_v1.md#voi98-u003).
Elementary Hilbert-space projection, Cauchy-Schwarz, trace-preserving expectation, and the defining semicircular/free-product moment construction are the other inputs.
In particular the Stam projection onto the algebra of sums is not replaced by projection onto the separate coefficient algebra.

All six relevant local page images and extracted text were inspected on 2026-09-08.
The inequalities, matrix transpose, equality recursion, zero-energy case, and infinite-information cases were reconstructed.
The coordinating agent independently reviewed the unit, reconstructed those arguments, read the relevant source text, and visually rechecked PDF pp. 26 and 30; no gap was found within the recorded scope.
No numerical test is needed to certify these analytic arguments; no formal verification or external human review was performed.
This unit records local corrections, not author-confirmed errata.
It does not assert a general optimality theorem, Stam equality criterion, covariance-matrix refinement, or entropy identity.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Voi98, the retained 39-page published journal article, printed pp. 189-227; printed page = PDF page + 188. Other works retain their separate exact versions and inspection limits in the body. |
| source-locator | Section 6, Definition 6.1 through Proposition 6.9, printed pp. 213-218 / PDF pp. 25-30. |
| inspection | 2026-09-08: projection, scaling, free additivity, Stam, real matrix covariance, Cramer-Rao and its equality case reconstructed, including zero energy and infinite information; the coordinating agent independently reviewed the unit. No general optimality, Stam equality criterion, covariance-matrix refinement, entropy identity, formal verification or external human review is claimed. |
