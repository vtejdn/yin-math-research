---
author: Yin
---
# Two normal coordinates have scalar relative commutant under conjugate variables or bare full-domain duals

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace and \(d\ge2\).
Write \(H=L^2(M,\tau)\), \(\Omega=1\), \(P_\Omega h=\langle\Omega,h\rangle\Omega\), and \(B=\mathbb C\langle X,X^*\rangle\).
Suppose either that \(X\) admits the actual ACSY conjugate variables of F0011 or that it admits bare duals on every bounded vector as in that Task.
In the first case the source of the coordinate derivations is \(B\) and their Hilbert adjoints have the vacuum tensor in their domains.
In the second case the algebraic maps \(D_k:M\Omega\to H\) satisfy \([X_l,D_k]=\delta_{kl}P_\Omega\) on \(M\Omega\).
Then for every two distinct indices \(i,j\)
\[
                  W^*(X_i,X_j)'\cap M=\mathbb C1.                \tag{1}
\]
In particular \(M\) is a factor.
If a joint tracial law on a bounded normal \(d\)-tuple is a nontrivial convex combination of two distinct joint tracial laws, its generated tracial von Neumann algebra satisfies neither hypothesis.
This applies irrespective of whether a single marginal distinguishes the component laws.

## Argument

### The diffuse coordinate and the graph of the derivation

Assume the ACSY condition and fix \(i\ne j\).
By [C_F0076, Part 1](Yin_C_F0076_v1.md#statement), all marginals are diffuse and \(\delta_i\) is closable with \(\delta_iX_j=\delta_iX_j^*=0\).
Let \(N=W^*(X_j)\) and \(G=\operatorname{graph}\overline{\delta_i}\subset H\oplus(H\otimes_2H)\).
Left multiplication by an element of \(\mathbb C[X_j,X_j^*]\) acts on the first component and on the left coarse leg.
It leaves \(G\) invariant by Leibniz and graph closure.
The same holds for the adjoint multiplier and for the corresponding right actions.
Thus the orthogonal projection \(Q\) onto \(G\) commutes with these actions and, by their normality, with the left and right actions of all of \(N\).

There is no nonzero \(N\)-central vector in the coarse correspondence.
For completeness choose, in the diffuse abelian \(N\), partitions of the identity into \(n\) projections of equal trace (use the nonatomic spectral probability).
On \(H\otimes_2 H\) the projections \(\sum_h L_{e_h}\otimes R_{e_h}\) fix every \(N\)-central vector.
On a simple tensor \(b\otimes c\) with \(b,c\in M\), the squared norm after projection is
\[
 \sum_h\|e_h b\|_2^2\|c e_h\|_2^2
 \le n^{-1}\|b\|_M^2\|c\|_2^2.
\]
These projections are contractions, so density gives strong convergence to zero as \(n\to\infty\).

For \(a\in N'\cap M\), write \(Q(a,0)=(b,\eta)\).
Commutation of \(Q\) with the two \(N\)-actions and centrality of its input relative to \(N\) give \(u\eta=\eta u\) for all \(u\in N\), hence \(\eta=0\).
The difference \((a-b,0)\) is orthogonal to the graph, whose first coordinates contain the dense polynomial core.
It follows that \(b=a\), so \(a\in\operatorname{Dom}\overline{\delta_i}\) with \(\overline{\delta_i}a=0\).
Choose \(p_n\in B\) converging to \(a\) in \(H\) with \(\delta_i p_n\to0\) in the coarse space.
If \(a\) also commutes with \(X_i\), then \([p_n,X_i]\to0\) in \(H\), whereas
\[
 \delta_i[p_n,X_i]=(\delta_i p_n)X_i-X_i(\delta_i p_n)
                      +p_n\otimes1-1\otimes p_n
 \ \longrightarrow\ a\otimes1-1\otimes a .
\]
Closability makes the last vector zero.
Contracting one tensor leg gives \(a=\tau(a)1\), as required.

### Averaging the compact polynomial commutators of a bare witness

Assume the bare full-domain condition and again fix \(i\ne j\).
By [C_F0132, Part A](Yin_C_F0132_v1.md#statement) choose a bounded, ultraweak-to-weak continuous normalized \(E_i:M\to H\) with \([E_i,X_i]=P_\Omega\) and \([E_i,L_b]=0\) for \(b\in N\).
Here \([E_i,L_a](v)=E_i(av)-aE_i(v)\) for \(v\in M\).
By [C_F0070, Part A](Yin_C_F0070_v1.md#statement), \(N\) is diffuse and for \(q\in B\) the map \([E_i,L_q]\) on \(M\) is the restriction of a Hilbert--Schmidt operator \(K_q\) on \(H\).
Indeed \(-E_i\) itself is a bare witness and its normalization in that statement is \(E_i\).

Choose a unitary \(u\in N\) of Haar law by the nonatomic scalar spectral representation.
The unitary \(L_u\) on \(H\) has no eigenvectors, since its point spectral projections vanish.
Conjugation by \(L_u\) on the Hilbert space of Hilbert--Schmidt operators has no fixed vector except zero.
If a nonzero compact \(K\) commuted with \(L_u\), a nonzero positive eigenvalue of \(K^*K\) would supply a finite-dimensional nonzero reducing subspace and hence an eigenvector for \(L_u\).
Consequently the Cesaro averages of these conjugates of any \(K_q\) tend to zero in Hilbert--Schmidt norm.
To see this, the range of \(I-\mathrm{Ad}(L_u)\) is dense by the fixed-vector assertion for the unitary and its adjoint, and the Cesaro averages telescope on that range.

Given \(a\in N'\cap M\), take uniformly operator-norm-bounded \(q_n\in B\) with \(\|q_n-a\|_2\to0\) by [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001).
Choose \(m_n\) so that for \(r_n=m_n^{-1}\sum_{k=1}^{m_n}u^kq_nu^{-k}\) the Hilbert--Schmidt norm of the corresponding averaged commutator is at most \(1/n\).
Commutation of \(E_i\) with both \(u\) and \(u^*\) shows precisely that \([E_i,L_{r_n}]\) on \(M\) is the restriction of this averaged operator.
Since \(u\) commutes with \(a\), \(\|r_n-a\|_2\le\|q_n-a\|_2\) and the \(r_n\) stay uniformly bounded in \(M\).
Thus \(r_n\to a\) strongly in the left representation, by testing first on bounded vectors, and ultraweakly.
For each \(v\in M\), \(r_nv\to av\) ultraweakly, so \(E_i(r_n v)\to E_i(av)\) weakly while \(r_n E_i(v)\to aE_i(v)\) in \(H\).
The commutator bound gives \(E_i(av)=aE_i(v)\).
If \(a\) also commutes with \(X_i\), the two expansions of \([E_i,L_{aX_i}]=[E_i,L_{X_i a}]\) imply \(aP_\Omega v=P_\Omega(av)\) for all \(v\in M\).
At \(v=1\) this gives \(a=\tau(a)1\).
The proof uses the normal representative, without any Hilbert adjoint or graph domain assumption on a supplied bare witness.

### Consequence for mixing laws

Equation (1) contains the center of \(M\) in \(\mathbb C1\).
Suppose that the joint law is \(t\tau_1+(1-t)\tau_2\) for \(0<t<1\), with the component laws understood on a common unital universal C-star algebra for the tuple cutoff.
For completeness each \(\tau_l\) induces a bounded positive trace functional on the represented polynomial algebra, dominated on positives by \(c_l\tau\) for \(c_1=t^{-1}\), \(c_2=(1-t)^{-1}\).
On a represented word combination \(p\), Cauchy--Schwarz gives \(|\tau_l(p)|\le\sqrt{c_l}\|p\|_2\), including well-definedness on the quotient.
Write \(\tau_l(p)=\langle h_l,p\rangle\) with \(h_l\in H\).
For every core \(q\), traciality gives \(\langle h_l,qp\rangle=\langle h_l,pq\rangle\) for all core \(p\), so left and right multiplication by \(q^*\) agree on \(h_l\).
Normality of these actions then makes \(h_l\) central relative to \(M\).
In a finite factor a central tracial Hilbert vector is scalar: as an affiliated operator its polar parts commute with every unitary of \(M\), hence its polar partial isometry and the spectral projections of its absolute value are central.
Therefore \(\tau_l=\tau\) by normalization, contradicting distinctness.
A one-coordinate normal law is outside the assertion.

### Relation to the selfadjoint argument

The graph argument uses the diffuse element in the kernel of a closed difference quotient as in the selfadjoint factoriality argument in [Dabrowski, Theorem 1, Remark 3 and Theorem 4](https://arxiv.org/html/0804.2906v2).
The present proof establishes its graph-domain step for a possibly nonreal normal-coordinate derivation and computes the relative commutant inside the full generated algebra.
The argument for bare duals uses a different averaging calculation since their Hilbert adjoints need not have the vacuum in their domains.
The proof for bare duals and the comparison with mixtures were developed together with a separate research agent.
No non-Gamma statement or implication between the two hypotheses is deduced here.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T10:06 |
| status | open |
| reason | Fixed candidate giving pair-relative commutant triviality under each original hypothesis and the resulting obstruction to mixtures of distinct laws. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Pair-relative commutant in the full algebra under actual ACSY or arbitrary bare witnesses and the consequence for mixing laws. |
| argument | [Argument](#argument) | Closed graph, compact-commutator averaging, normality of the selected representative and exclusion of convex mixtures. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Diffuse marginals, closability and vanishing on the other starred generators under ACSY. |
| dependency | [Normal representative](Yin_C_F0132_v1.md#statement) | Part A supplies the ultraweak-to-weak continuous normalized witness and commutation with left multiplication by omitted coordinates. |
| dependency | [Starred commutators](Yin_C_F0070_v1.md#statement) | Part A gives diffuseness and Hilbert--Schmidt implementers on the polynomial core under bare full-domain duals. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Uniformly operator-norm-bounded approximants from the represented polynomial star algebra. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T10:12 |
| status | proved |
| reason | Adopt the scalar pair-relative commutant result under both hypotheses and the obstruction to convex mixtures after independent review of the full argument. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Pair-relative commutant in the full algebra under actual ACSY or arbitrary bare witnesses and the consequence for mixing laws. |
| argument | [Argument](#argument) | Closed graph, compact-commutator averaging, normality of the selected representative and exclusion of convex mixtures. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Diffuse marginals, closability and vanishing on the other starred generators under ACSY. |
| dependency | [Normal representative](Yin_C_F0132_v1.md#statement) | Part A supplies the ultraweak-to-weak continuous normalized witness and commutation with left multiplication by omitted coordinates. |
| dependency | [Starred commutators](Yin_C_F0070_v1.md#statement) | Part A gives diffuseness and Hilbert--Schmidt implementers on the polynomial core under bare full-domain duals. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Uniformly operator-norm-bounded approximants from the represented polynomial star algebra. |
| review | [Whole-proof finding](../audits/reviews/Yin_R_F0210_v1.md#whole-proof-finding) | Both separate implications, their actual domains and limiting arguments, factoriality and the joint-law mixture obstruction. |
