---
author: Yin
---
# Independent review of bounded drifts of a free semicircular coordinate

## Whole-proof finding

At 2026-11-13T14:02 a separate agent outside proof development reviewed the [statement](../../claims/Yin_C_F0212_v1.md#statement) and [argument](../../claims/Yin_C_F0212_v1.md#argument) of the November 13 candidate.
The reviewer received the fixed proof, the scope of the assignment and the repository context, and consulted the Task definitions and the declared project and literature inputs.
The reviewer had no proof-development dialogue, author explanations or previous findings about this candidate.
The equivalence, vacuum formula, canonical domain assertions and finite columns in both orientations hold under the two oriented column hypotheses on the base.

The single-test bound for the adjoint tuple controls the left slice of the original derivation, because taking adjoints reverses the legs and conjugates the scalar trace.
This furnishes both hypotheses of the canonical domain theorem.
In the free lift, the module decomposition \(w b\) is orthogonal in \(w\), and \(\mathbb E_R(w^*w')=\delta_{ww'}1\).
The cuts inside \(w\) have zero right trace, so the old column estimate applies simultaneously to all terminal coefficients from all tests with their squared column bounded by the conditional expectation.
For a base polynomial \(B'\), multiplying the leftmost letter of a nonempty prefix \(w\) by \(B'\) can remove this letter only when it belongs to the old factor.
In that case a new-factor letter survives, so every resulting prefix still ends in the new factor and the terminal map \(E\) commutes with this multiplication.
The old summand contributes \([E,B']\).
For uniformly bounded strong approximants both coordinates in the graph pairing have the required limits, by weak compactness of the images and uniqueness in the weakly closed graph.
First approximating \(B\), then the input, gives \([L,B]=K e_R\) on bounded vectors under the Hilbert–Schmidt hypothesis.

For necessity the forced marginal phases identify the derivative of every old polynomial inside the larger represented algebra, so the old projection of the target vacuum is exactly \(\xi\).
In the test \(uTv\) the two endpoint terms containing \(s\) have zero double trace and the middle derivative vanishes.
Replacing \(B\) provisionally by \(B'\) in the endpoint identity gives the negative middle term \(-(\tau\otimes\tau)(u(\delta B')v)=-\langle u^*,[E,B']v\rangle\).
Passing to bounded \(B\) uses \(u^*\in\operatorname{Dom}E^*\) and strong convergence of uniformly bounded multipliers on the fixed endpoint legs.
Writing the one-noise projection as \(J_s\kappa\), the pairing gives \(K=-\Theta(\kappa^\star)\) first on old polynomial tests and then on bounded vectors by the same weak graph argument.
In particular the sign and the componentwise adjoint in the formula are fixed even for a complex old derivation.

For insertion, creation in the relative Fock representation prepends \(1\) and its adjoint contracts the first base leg by \(\tau\).
Their sum has the free mixed moments by nested pair closure, with products in \(R\) in their original order.
For degree two the Wick word is \(a_0s a_1s a_2-\tau(a_1)a_0a_2\).
In every higher degree the differentiated contraction cancels exactly the shorter-word correction in the expanded cuts, giving (7) with the prefix and suffix in the stated order.
On degree one the double trace of insertion at \(a s b\) with coefficient \(c\otimes d\) is \(\tau(ac)\tau(db)\), which pairs \(a\otimes b\) against \(c^*\otimes d^*\).
The derivative vanishes in degree zero, and above degree one each cut has a positive-degree side orthogonal to a base coefficient.
Continuity of the finite polynomial insertion in its coefficient extends the actual vacuum formula to Hilbert tensors.

In the right slice only the last cut survives, and reassociating its final tensor is isometric across all positive degrees.
In a bounded orthonormal basis the two coefficient lists for this cut and the insertion have squared norms at most \(\|p\|_2^2\) and \(\|\beta\|_2^2\).
The sum of the products thus converges in \(L^1\) by tracial Hölder and Cauchy–Schwarz.
The base has separable tracial Hilbert space because its finite generating tuple has a countable set of star monomials with dense span.
Bounded input testing of this \(L^1\) estimate gives the actual core adjoint bound with constant \(\|\beta\|_2\).
Expanding the Leibniz rule at \(a^*p\) gives \(F_{\beta,0}^*a=aJ_s(\beta^\star)-F_{\beta^\dagger,0}a\).
Applying this to the reversed coefficient bounds the original slice by \(2\|\beta\|_2\|a\|\) on the core, and bounded approximation restores that core's closure on every bounded vector.
The full-space commutator with \(s\) extends the old \(\Theta(\beta)\) by zero on \(H^\perp\), since its rank-one input and output vectors for elementary coefficients lie in \(H\).

The sum of the old lift and the correction restricted to bounded vectors has the required actual adjoint there by direct pairing with each summand.
Both vanish at the unit, their commutators with \(T\) cancel, and the coefficient \(1\otimes1\) gives the last normalized operator.
Negation yields the generator-first sign required in the Task.
The normal strong-to-vacuum theorem identifies the actual target vacuum with the operator-first adjoint at the unit.
The two contributions in the old coordinates belong to orthogonal degrees, which gives the asserted squared norm and excludes higher-degree terms.
Canonical comparison applies to these densely defined witnesses with the two full bounded-vector domains.

For the final column implication the first enlargement of \(Y\) by two free Haar unitaries uses only its already proved actual vacuum property.
Regrouping the factors makes \(s\) free from \(R'=W^*(X,U,V)\).
The previous column lift applies to each old coordinate of this base.
For each Haar coordinate the scalar estimate extends its slice to \(C^*(U)\) or \(C^*(V)\), where the complex little Grothendieck inequality controls the column, including for the adjoint generator.
The same column lift applies with that Haar factor chosen as the base.
The enlarged shear therefore satisfies the base hypotheses of the equivalence already proved, independently of its eventual column conclusion.
The resulting strong duals have bounded restrictions with respect to the operator norm and give the finite witness costs required by the two-Haar lower bound for \(Y\).
Applying this reasoning to \(X^*\) uses adjoint invariance of the actual premise, the same \(B=B^*\), and the two base bounds in exchanged order.
The argument does not require \(B\) to belong to the derivation domain, and the unrestricted normal implication remains open.
The four literature inputs were checked at their recorded statement and applicability scopes, without a new audit of their original proofs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0212_v1.md#statement) | Equivalence for an arbitrary bounded selfadjoint base drift, exact actual vacua, canonical domains, and both oriented column bounds. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0212_v1.md#argument) | All six sections, including compression, necessity on mixed tests, arbitrary-base Wick insertion, corrected strong duals and column persistence. |
| [Whole-proof finding](#whole-proof-finding) | [Task contract](../../tasks/Yin_T_F0011_v1.md#contract) | Represented star algebra, actual adjoints and generator-first sign. |
| [Whole-proof finding](#whole-proof-finding) | [Adjoint tuples](../../claims/Yin_C_F0073_v1.md#statement) | Reversed coordinate derivation, conjugated vacuum and exchange of oriented slices. |
| [Whole-proof finding](#whole-proof-finding) | [Forced phases](../../claims/Yin_C_F0076_v1.md#statement) | Uniqueness of actual coordinate derivatives on the old star core by their marginal phases. |
| [Whole-proof finding](#whole-proof-finding) | [Canonical domain theorem](../../claims/Yin_C_F0072_v1.md#statement) | Canonical graph and actual adjoint domains from both core slice bounds. |
| [Whole-proof finding](#whole-proof-finding) | [Free extension](../../claims/Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Actual vacuum on the represented free-product core. |
| [Whole-proof finding](#whole-proof-finding) | [Pointed free products](../literature/Voi98/Yin_U005.md#voi98-u005) | Orthogonality and multiplication of reduced words in the pointed representation. |
| [Whole-proof finding](#whole-proof-finding) | [Lifted slice](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Right module formula, conditional expectation and Haar vacua. |
| [Whole-proof finding](#whole-proof-finding) | [Kaplansky density](../literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong polynomial approximants, including selfadjoint approximants to the drift. |
| [Whole-proof finding](#whole-proof-finding) | [Semicircular moments](../literature/NS06/Yin_U004.md#ns06-u004) | Noncrossing pair recursion with coefficients from the noncommutative base. |
| [Whole-proof finding](#whole-proof-finding) | [Last-cut estimate](../../claims/Yin_C_F0145_v1.md#2-a-suffix-cut-gives-an-h-to-l1-estimate) | Cut mechanism and \(L^1\) multiplication estimate as rederived in the relative base. |
| [Whole-proof finding](#whole-proof-finding) | [Reversed insertion](../../claims/Yin_C_F0145_v1.md#3-the-actual-adjoints-and-the-reverse-bound) | Actual slice adjoint and recovery of the opposite estimate for general base coefficients. |
| [Whole-proof finding](#whole-proof-finding) | [Strong to actual vacuum](../../claims/Yin_C_F0070_v1.md#statement) | Part C on the normalized generator-first system. |
| [Whole-proof finding](#whole-proof-finding) | [Normal canonical comparison](../../claims/Yin_C_F0075_v1.md#statement) | Both full domains for the closures from the original target core. |
| [Whole-proof finding](#whole-proof-finding) | [Two-Haar criterion](../../claims/Yin_C_F0208_v1.md#statement) | Enlarged actual vacua and lower bound by one quarter of each original column cost. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar normal estimate](../../claims/Yin_C_F0055_v1.md#statement) | Operator-norm estimate for the scalar Haar right slice with its actual vacuum. |
| [Whole-proof finding](#whole-proof-finding) | [Little Grothendieck inequality](../literature/Pis12/Yin_U001.md#pis12-u001) | Bounded complex Hilbert-valued map on the abelian Haar \(C^*\)-algebra. |
