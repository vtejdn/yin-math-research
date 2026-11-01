---
author: Yin
---

# Bounded canonical duals from a bounded conjugate-derivative contraction

This general deduction is distinct from the degree-weighted q-Gaussian construction in [C_F0023](Yin_C_F0023_v1.md#2-a-general-polynomial-degree-criterion).
It uses the polynomial adjoint and coassociativity interfaces, not a bounded second conjugate variable or a smallness assumption.

## Statement

Let \(X=(X_1,\ldots,X_d)\), \(d\geq1\), be bounded selfadjoint generators of a finite von Neumann algebra \((M,\tau)\) with faithful normal tracial state.
Put \(A=\mathbb C\langle X\rangle\), \(H=L^2(M,\tau)\), and \(\Omega=1\).
Use the outer-bimodule free difference quotients \(\partial_iX_j=\delta_{ij}1\otimes1\), with their Hilbert-space closures \(\overline\partial_i:H\to H\otimes_2H\).
Assume conjugate variables \(\xi_i\in H\) exist, with
\[
 \tau(\xi_i p)=(\tau\otimes\tau)(\partial_i p)\quad(p\in A).
\]
The standard algebraic-freeness and closability interfaces are used as in [C_F0022](Yin_C_F0022_v1.md#1-statement-and-the-meaning-of-finite-rank) and the [inspected conjugate-variable source](../audits/literature/Voi98/Yin_U002.md#conjugate-variables).
For a fixed coordinate \(i\), suppose additionally that
\[
 \xi_i\in\operatorname{Dom}\overline\partial_i,\qquad
 B_i=(\mathrm{id}\otimes\tau)\overline\partial_i\xi_i\in M.
\]
Here the partial trace is the bounded contraction on the Hilbert tensor product; the last inclusion is an additional boundedness hypothesis.
Let
\[
 D_{i,0}p=(\mathrm{id}\otimes\tau)\partial_i p,\qquad p\in A.
\]
Then its Hilbert-space closure \(D_i\) is bounded on all \(H\), and
\[
 D_i\Omega=0,\qquad [D_i,X_j]=\delta_{ij}P_\Omega,\qquad
 B_i\geq0,\qquad D_iD_i^*=\rho(B_i),\qquad
 \|D_i\|^2=\|B_i\|.
\]
The right multiplier \(\rho(B_i)\) acts by \(a\Omega\mapsto aB_i\).
If these hypotheses hold for every coordinate, the bounded extensions form a simultaneous normalized dual system.
If moreover \(\overline\partial_i\xi_i\) belongs to the bounded spatial tensor product, then
\[
 \|D_i\|\leq\|\overline\partial_i\xi_i\|_\infty^{1/2}.
\]
This is the Lipschitz-conjugate specialization, with no uniformity or smallness assertion.

## Argument

### Polynomial adjoints and graph multiplication

Fix \(i\) and omit its index.
With the inner product linear in the second variable, the standard polynomial adjoint formula gives
\[
 E_0p:=\partial^*(p\otimes1)=p\xi-D_0p,\qquad E_0\subseteq D_0^*.
\]
Indeed \(\langle D_0a,p\rangle=\langle\partial a,p\otimes1\rangle\) for \(a,p\in A\).
The finite conjugate-variable setting supplies the actual adjoint formula, and \(A\) is dense because the generators are selfadjoint.
Thus \(D_0\) and \(E_0\) are densely defined and closable.

Take polynomial graph approximants \(\xi_n\to\xi\), \(\partial\xi_n\to\overline\partial\xi\) in the respective Hilbert spaces.
For each \(p\in A\), the Leibniz identity yields
\[
 \overline\partial(p\xi)=p\,\overline\partial\xi+(\partial p)\cdot\xi.
\]
All terms converge: \(\partial p\) has finitely many bounded tensor factors, and multiplication of its second factors by an \(L^2\) vector is continuous for those fixed factors.
Applying the Hilbert-space partial trace to the same approximants proves \(p\xi\in\operatorname{Dom}D\), where \(D=\overline{D_0}\).
No boundedness of \(\xi\) is used here.

### Coassociativity and the positive bounded multiplier

Write \(\partial p=\sum_k a_k\otimes b_k\).
Conjugacy, the trace property and polynomial coassociativity give
\[
 \begin{aligned}
 D(p\xi)
 &=pB+\sum_k a_k\tau(b_k\xi)\\
 &=pB+(\mathrm{id}\otimes\tau\otimes\tau)(\mathrm{id}\otimes\partial)\partial p\\
 &=pB+(\mathrm{id}\otimes\tau\otimes\tau)(\partial\otimes\mathrm{id})\partial p\\
 &=pB+D_0^2p.
 \end{aligned}
\]
Since \(D_0p\in A\), it follows that \(E_0p\in\operatorname{Dom}D\) and \(DE_0p=pB\).
The adjoint relation therefore gives
\[
 \|E_0p\|_2^2=\langle p,DE_0p\rangle
 =\tau(p^*pB)\leq\|B\|\|p\|_2^2.
\]
The quadratic form on the right is nonnegative on dense \(A\).
Since right multiplication by \(B\) is bounded on \(H\), its quadratic form is nonnegative on all \(H\).
Hence \(\rho(B)\) is positive, and its faithful right representation implies \(B\geq0\).

### Bounded extension and exact norm

The estimate extends \(E_0\) uniquely to a bounded operator \(E^{\mathrm b}\) on \(H\).
The polynomial adjoint relation implies \(D_0\subseteq(E^{\mathrm b})^*\).
Since \(A\) is dense and the operator on the right is bounded, the graph closure of its restriction to \(A\) is the full bounded operator.
Thus \(D=(E^{\mathrm b})^*\) on all \(H\), so \(D^*=E^{\mathrm b}\).
The equality \(DE_0p=pB\) extends by density to \(DD^*=\rho(B)\).
Consequently \(\|D\|^2=\|\rho(B)\|=\|B\|\).
The polynomial dual relation and \(D_0\Omega=0\) extend by boundedness to the stated identities on \(H\).
For bounded spatial-tensor derivatives, contractivity of the normal partial trace gives \(\|B\|\leq\|\overline\partial\xi\|_\infty\).

### Bounded second conjugate comparison

If additionally \(\xi\in M\) and \(\overline\partial\xi\) is bounded in the spatial tensor product, the same graph approximants and the adjoint formula give
\[
 \mathcal J_{2,i}=\partial_i^*(1\otimes\xi_i)
 =\xi_i^2-(\tau\otimes\mathrm{id})\overline\partial_i\xi_i\in M.
\]
For the limiting step, \(1\otimes\xi_n\to1\otimes\xi\), while
\(\partial^*(1\otimes\xi_n)=\xi\xi_n-(\tau\otimes\mathrm{id})\partial\xi_n\) converges in \(H\), using boundedness of \(\xi\).
Closedness of \(\partial^*\) proves the formula.
This comparison uses the other tensor leg and is not needed for the bounded-dual proof.

## Inputs and limits

The source-side adjoint/coassociativity mechanism and its actual Dab10 passage inspection are retained in [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#1-conventions-and-the-exact-source-interfaces).
The argument here is an additional project deduction, not a claim that its exact theorem is printed in Dab10.
[MS23-U005](../audits/literature/MS23/Yin_U005.md#ms23-u005) retains the all-\(|q|<1\) Lipschitz input for q-Gaussians; applying the theorem uses that exact bounded-derivative scope rather than its vacuum-functional estimate alone.
The degree-weighted proof of C_F0023 remains a separate argument.
No renewed primary-source inspection, rational-\(L^2\) boundedness theorem, or scalar bounded-division-closure equality is asserted.

## Current assessment
[Selected decision](#decision-reviewed)

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-01T06:57 |
| status | open |
| reason | Retain the general contraction-based bounded-dual argument at its responsible Claim home, with precise hypotheses and an actual new review still required for adoption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Bounded canonical dual and exact positive right-multiplier norm identity under a bounded partial-trace derivative; simultaneous and Lipschitz specializations. |
| argument | [Argument](#argument) | Polynomial adjoint, graph-product limits, coassociativity, positivity, bounded extension and optional second-conjugate comparison. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-01T07:04 |
| status | proved |
| reason | Adopt the actual whole-candidate mathematical finding at its disclosed self-reviewed relationship and retained foundational inspection depths; no new independent review is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete single-coordinate theorem, exact positive right-multiplier and norm identities, simultaneous duals and Lipschitz specialization. |
| argument | [Argument](#argument) | Entire polynomial-adjoint, graph-product, coassociativity, positivity and bounded-extension argument, including the optional second-conjugate comparison. |
| review | [Whole-candidate finding](../audits/reviews/Yin_R_F0095_v1.md#whole-candidate-finding) | Complete exact statement and argument; self-reviewed because the separately assigned reviewer encountered the earlier source-review conclusion before its initial finding, with actual source and application limits retained. |
