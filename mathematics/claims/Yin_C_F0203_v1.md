---
author: Yin
---
# Full-domain duals for tuples jointly similar to selfadjoint generators

## Current assessment

[Selected decision](#decision-candidate)

## Statement

Let \(X_1,\ldots,X_d\) generate a finite von Neumann algebra \(M\) with faithful normal probability trace \(\tau\), and put \(H=L^2(M,\tau)\), \(\Omega=1\) and \(P_\Omega a=\tau(a)1\) on \(M\).
Suppose a single invertible \(h\in M\) makes \(Y_j=h^{-1}X_jh\) selfadjoint for every \(j\).
Set \(N=W^*(Y_1,\ldots,Y_d)\subset M\) and \(\kappa=\|h\|\|h^{-1}\|\).
The inclusion may be proper.

On formal holomorphic polynomials in \(d\) letters let \(\partial_i\) denote the word-cut derivation with \(\partial_i x_j=\delta_{ij}1\otimes1\), and set
\[
 \Lambda_i^X(p)=(\tau\otimes\tau)((\partial_i p)(X)).
\]
Write \(\gamma_i(X)\) for the least \(c\ge0\) such that \(|\Lambda_i^X(p)|\le c\|p(X)\|_2\) for every formal \(p\), with value \(+\infty\) if no such \(c\) exists.
The following conditions are equivalent.

1. Every \(\gamma_i(X)\) is finite.
2. The selfadjoint tuple \(Y\) has finite joint non-microstates free Fisher information in \(N\).
3. \(X\) has bare full-domain duals \(\mathsf F(X)\) in \(M\).
4. \(X\) has duals with both actual bounded-vector domains \(\mathsf S(X)\) in \(M\).

Here \(\mathsf F,\mathsf S\) and the starred ACSY hypothesis \(\mathsf A\) have their [F0011 meanings](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct), with generator-first commutators.
In this class \(\mathsf A(X)\) implies all four conditions.
There is a tuple in this class satisfying all four for which \(\mathsf A(X)\) fails.

Under the equivalent conditions, let \(\eta_i\) be the canonical conjugates of \(Y\) in \(L^2(N)\).
Then \(\kappa^{-1}\|\eta_i\|_2\le\gamma_i(X)\le\kappa\|\eta_i\|_2\).
One can choose closed generator-first duals \(D_i^X\) for which, on every \(a\in M\),
\[
 \|D_i^X a\|_2\le4\kappa^2\|\eta_i\|_2\|a\|,
 \qquad
 \|(D_i^X)^*a\|_2\le5\kappa^2\|\eta_i\|_2\|a\|.
\]

## Argument

### Transfer of the holomorphic moment functional

The bounded invertible operator \(W=L_hR_{h^{-1}}\) on \(H\) fixes \(\Omega\), satisfies \(WL_{Y_j}W^{-1}=L_{X_j}\), and preserves the scalar trace pairing with \(\Omega\) by traciality.
Thus \(WP_\Omega W^{-1}=P_\Omega\).
Both \(W\) and \(W^{-1}\) have norm at most \(\kappa\) on \(H\) and on \(M\) with its operator norm.
Their Hilbert adjoints also preserve \(M\) with these bounds, since \(W^*(a)=h^*a(h^{-1})^*\).

For every formal \(p\), \(p(X)=Wp(Y)\).
The two factors in each cut of a word have the same individual traces at \(X\) and \(Y\), giving \(\Lambda_i^X(p)=\Lambda_i^Y(p)\).
Consequently the least constants for the \(L^2\) tests at \(X\) and \(Y\) differ by at most the factor \(\kappa\) in either direction.
Finite constants at \(Y\) give Riesz representatives on \(L^2(N)\), since \(Y\) is selfadjoint and its polynomial algebra is dense there.
The formal selfadjoint conjugate relations give well-defined represented difference quotients with actual vacuum adjoints by [MSW17, Definition 2.1, Propositions 2.3–2.4 and Theorem 2.5](../audits/literature/MSW17/Yin_U001.md#relation-to-condition-a).
These conjugate vectors \(\eta_i\) represent the functionals with the inner product linear in its second argument, so \(\gamma_i(Y)=\|\eta_i\|_2\).
Conversely these conjugates imply the moment bounds by Cauchy–Schwarz.
This proves the first equivalence and the comparison of the least constants.
If \(X\) has actual ACSY derivations \(\delta_i\) with vacua \(\xi_i\), their values on \(p(X)\) are the evaluated formal word cuts by Leibniz.
Hence \(\Lambda_i^X(p)=\langle\xi_i,p(X)\rangle\) and \(\gamma_i(X)\le\|\xi_i\|_2\).

### Construction with both bounded-vector domains

Write \(H_N=L^2(N,\tau|_N)\) and let \(P_N:H\to H_N\) be the orthogonal projection.
For clarity, \(P_Na\) belongs to \(N\) and has operator norm at most \(\|a\|\) for every \(a\in M\).
Indeed \(H_N\) reduces every right multiplication by \(b\in N\), so \((P_Na)b=P_N(ab)\) has Hilbert norm at most \(\|a\|\|b\|_2\).
The map \(b\mapsto(P_Na)b\) therefore extends to a bounded operator on \(H_N\) commuting with all right multiplications.
By the [tracial commutant theorem](../audits/literature/AP18/Yin_U002.md#ap18-u002), it is left multiplication by an element of \(N\) of norm at most \(\|a\|\).
Evaluation at \(\Omega\) identifies that element with \(P_Na\).
This is the usual trace-preserving conditional expectation, described in [Anantharaman–Popa, Theorem 9.1.2 and Remark 9.1.3](https://www.math.ucla.edu/~popa/Books/IIun.pdf).

Assume finite Fisher information for \(Y\).
By [C_F0022, Section 3](Yin_C_F0022_v1.md#3-the-entire-bounded-algebra-lies-in-both-domains), the negative of the closed right contraction gives a closed densely defined generator-first \(D_i^Y\) on \(H_N\) with \([L_{Y_j},D_i^Y]=\delta_{ij}P_\Omega\) on \(N\).
Both \(D_i^Y\) and \((D_i^Y)^*\) have \(N\) in their actual domains and satisfy the bounds \(4\|\eta_i\|_2\) and \(5\|\eta_i\|_2\), respectively, from operator norm to Hilbert norm.
On \(H=H_N\oplus H_N^\perp\) set \(\widetilde D_i=D_i^Y\oplus0\) with domain \(\operatorname{Dom}D_i^Y\oplus H_N^\perp\).
Its adjoint is \((D_i^Y)^*\oplus0\), and \(P_Na\in N\) puts every \(a\in M\) in both domains.
The two norm estimates persist there by the operator norm bound on \(P_Na\).
Since \(Y_j\) is selfadjoint, \(H_N\) reduces \(L_{Y_j}\).
The commutator on \(a\in M\) is therefore the commutator on \(P_Na\) in \(H_N\), which equals \(\delta_{ij}\tau(a)1\).

Define \(D_i^X=W\widetilde D_iW^{-1}\) with domain \(W\operatorname{Dom}\widetilde D_i\).
This is a closed densely defined operator and its Hilbert adjoint is
\[
 (D_i^X)^*=(W^{-1})^*\widetilde D_i^*W^*,
 \qquad
 \operatorname{Dom}(D_i^X)^*=(W^*)^{-1}\operatorname{Dom}\widetilde D_i^* .
\]
Here multiplication on either side of a closed operator by bounded invertible operators gives the displayed adjoint identity including its domain, directly by testing the defining Hilbert pairing on \(W\operatorname{Dom}\widetilde D_i\).
Since \(W^{-1}\) and \(W^*\) preserve \(M\), every bounded vector belongs to both domains and the two operator norm estimates acquire at most a factor \(\kappa^2\).
Applying the similarity to the commutator on \(W^{-1}a\in M\) gives \([L_{X_j},D_i^X]a=\delta_{ij}P_\Omega a\).
This proves \(\mathsf S(X)\), and restriction gives \(\mathsf F(X)\).

### Compression of arbitrary bare duals and strictness

Suppose \(F_i:M\to H\) are arbitrary complex-linear generator-first bare duals for \(X\).
For \(b\in N\) put \(G_i(b)=P_NW^{-1}F_i(Wb)\).
All inputs to \(F_i\) are bounded.
As \(P_N\) commutes with left multiplication by every \(Y_j\), the intertwining and trace identities for \(W\) give
\[
 L_{Y_j}G_i(b)-G_i(Y_jb)
   =P_NW^{-1}[L_{X_j},F_i](Wb)=\delta_{ij}\tau(b)1.
\]
These are bare duals in the generated tracial algebra \(N\).
[C_F0071 v2, Part B](Yin_C_F0071_v2.md#statement) gives finite joint free Fisher information for this selfadjoint tuple, completing the equivalences.
This compression requires only the stated full-domain commutators of the supplied \(F_i\).

For strictness, [C_F0133](Yin_C_F0133_v1.md#statement) takes \(Y=s\,\mathrm{diag}(1,-1)\) in \(M_2(L^\infty(\mu))\) with the positive half-semicircular law for \(s\).
The specified constant invertible matrix \(h\) gives a nonnormal generator \(X=hYh^{-1}\) with a bounded full-Hilbert-space dual, and the represented central relation \([X^2,X^*]=0\) excludes every starred Hilbert-valued coordinate derivation.
Thus the hypotheses of the present similarity class hold and the four equivalent conditions can all hold while the full ACSY condition fails.
The dual construction requires a common bounded invertible similarity and concerns existence of a strong system.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T10:31 |
| status | open |
| reason | Fixed candidate for the bounded-similarity classification, the two domain estimates and strictness of the starred ACSY hypothesis. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Four equivalent conditions, implication from full ACSY, strictness and the quantitative estimates. |
| argument | [Argument](#argument) | Holomorphic moment transfer, actual two-domain similarity, bare compression and strictness. |
| dependency | [Selfadjoint conjugate relations](../audits/literature/MSW17/Yin_U001.md#msw17-u001) | Formal word tests give represented selfadjoint difference quotients with actual conjugate vectors and finite Fisher information. |
| dependency | [Tracial commutant](../audits/literature/AP18/Yin_U002.md#ap18-u002) | On the standard tracial Hilbert space of the subalgebra the commutant of right multiplication consists of left multiplications. |
| dependency | [Selfadjoint full domains](Yin_C_F0022_v1.md#3-the-entire-bounded-algebra-lies-in-both-domains) | Closed selfadjoint-coordinate right contractions, their adjoints, estimates (9) and their commutators on all bounded vectors. |
| dependency | [Selfadjoint bare converse](Yin_C_F0071_v2.md#statement) | Part B gives finite Fisher information from the compressed bare system on the selfadjoint generated algebra. |
| dependency | [Strictness example](Yin_C_F0133_v1.md#statement) | Bounded similarity of a selfadjoint variable with a bounded full-Hilbert-space dual and no starred coordinate derivation. |
