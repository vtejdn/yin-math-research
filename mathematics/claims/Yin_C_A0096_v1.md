---
author: Yin
---
# Removing complex coefficients by alternation on finite direct powers

## Statement

Let \(G\) be a torsion-free discrete group and let \(G^j\) denote its ordinary direct power.

1. If \(u,v\in\mathbb C[G]\) are nonzero, \(uv=0\), and their supports have sizes \(a,b\), then \(\mathbb Z[G^a]\) has a zero product whose left factor has \(a!\) coefficients in \(\{1,-1\}\) and whose nonzero right factor is supported on at most \(b^a\) elements.
   In \(G^{a q}\), where \(q=\binom{a+b-1}{a}\), both factors can be taken with all their nonzero coefficients in \(\{1,-1\}\).
   In this latter construction the signed factors depend only on the two ordered supports.
   Their reductions remain nonzero and multiply to zero in every characteristic.
2. If every rational group-ring matrix over every \(G^j\) has integral regular rank, then every complex group-ring matrix over \(G\) has integral regular rank.
   In particular, across all torsion-free groups [A0001](../tasks/Yin_T_A0001_v1.md#contract) is equivalent to its integral-coefficient formulation, and [A0002](../tasks/Yin_T_A0002_v1.md#contract) is equivalent to excluding signed integral zero products.
   These equivalences may change the group to a finite direct power.
3. For matrices of a fixed size whose entries use \(s\ge1\) distinct complex coefficients, a single explicitly bounded power suffices in part 2.
   Let \(r=\min(m,n)\) for an \(m\times n\) input, \(M_0=1\), and define recursively
   \[
      k_i=\min\{k\ge1:2^k>\tbinom{kM_i+s}{s}\},\qquad
      M_{i+1}=k_iM_i\quad(0\le i<r).
   \]
   It suffices to assume rational matrix integrality on \(G^J\) for \(J=\binom{M_r+s}{s}\).
   No algebraicity, choice of transcendence basis or specialization of the complex coefficients is needed.

## Argument

### An integral annihilator on a direct power

For elements \(x_1,\ldots,x_d\) in a complex group ring define
\[
 {\cal A}(x_1,\ldots,x_d)=
 \sum_{\pi\in S_d}\operatorname{sgn}(\pi)
 x_{\pi(1)}\otimes\cdots\otimes x_{\pi(d)}
\]
using the ordinary group identification of algebraic tensor products over \(\mathbb C\) with the group ring of a direct product.
This multilinear alternating expression vanishes on a linearly dependent list.
It is nonzero on an independent list, for example by applying coordinate functionals on their finite-dimensional span.

Write \(\{g_i\}\) for the support of \(u\), and \(\{h_j\}\) for that of \(v\).
Put \(P={\cal A}(g_1,\ldots,g_a)\).
Its signed basis terms are distinct.
Since \(uv=0\), the \(g_i v\) are linearly dependent, so
\[
                  P v^{\otimes a}={\cal A}(g_1v,\ldots,g_av)=0 .
\]
The vector \(v^{\otimes a}\ne0\) is supported on \(\{h_1,\ldots,h_b\}^a\).
Left multiplication by \(P\) on those finite input and output supports is an integer matrix with nontrivial complex kernel.
Rational row reduction and denominator clearing give a nonzero integral null vector on the same allowed support.

For the two signed factors, index by the \(q\) multiplicity vectors \(\mu\in\mathbb Z_{\ge0}^b\) of total size \(a\).
Let \(U_\mu\in\mathbb Z[G^a]\) be the sum of the distinct basis tuples in which the \(h_j\) occur with multiplicities \(\mu_j\).
These elements have coefficients one and disjoint, nonempty supports.
Expanding \(v^{\otimes a}\) in the \(U_\mu\) gives a nonzero linear relation among the \(P U_\mu\).
Fix any ordering of the \(q\) classes.
Consequently the two integral elements
\[
           P^{\otimes q},\qquad {\cal A}(U_1,\ldots,U_q)
\]
have zero product.
Within each tensor position the support determines its unique multiplicity class, so no terms from different permutations coincide in the second factor.
All listed basis coefficients of either factor are \(1\) or \(-1\), and both supports are nonempty.
An integral zero product on those same signed lists therefore reduces to a nonzero pair over every field.
This complements [the transfer from infinitely many bounded-support prime characteristics](../audits/literature/MD26/Yin_U001.md#proposition-83-and-its-quantifiers).
It does not provide a signed witness for any already known positive-characteristic example.

### Alternation in actual affiliated rings

Let \(U(G)\) be the algebra of operators affiliated to the finite group von Neumann algebra.
Write \(D_j\) for the division closure of \(\mathbb Q[G^j]\) in \(U(G^j)\).
For torsion-free groups rational matrix integrality is equivalent to \(D_j\) being a division ring.
We use the [fixed-group division-closure criterion](../tasks/Yin_T_A0001_v1.md#contract) at its rational coefficient scope, as in [Lück and Linnell, Theorem 2.3(3)](https://arxiv.org/pdf/1602.06906v3#page=10).
The standard coordinate inclusions of \(U(G)\) in \(U(G^j)\) preserve affiliated algebra operations, adjoints and bounded projections.
Their images for distinct coordinates commute, by the spatial tensor representation, including for closed affiliated products.
In particular coordinate inclusions send \(D_1\) into \(D_j\), by closure under the actual inverses used in forming the division closure.

Suppose \(D_j\) is a division ring and \(x_1,\ldots,x_j\in D_1\) are linearly independent over \(\mathbb C\) in \(U(G)\).
The alternating expression formed by the \(j\) coordinate inclusions lies in \(D_j\) and is nonzero.
To see the latter even for unbounded inputs, take the affiliated row \(R=(x_1,\ldots,x_j)\) and its common left clearing factor \(h=(1+RR^*)^{-1/2}\).
This is a bounded affiliated unit and the \(h x_i\) are bounded.
They remain linearly independent as vectors in \(L^2(\mathcal N(G))\).
Multiplying the alternating expression on the left by \(h^{\otimes j}\) gives the ordinary alternating tensor of these bounded entries; its value on the identity vector is nonzero by independence in the Hilbert tensor product.
Thus the original alternating expression is an affiliated unit because it is a nonzero member of \(D_j\).

For any nonzero \(x=\sum_{i=1}^j c_i x_i\) with scalar complex \(c_i\), let \(p=P_{\ker x}\).
The equality \(xp=0\) is an affiliated identity, so the \(x_i p\) are linearly dependent if any \(c_i\) is nonzero.
By multilinearity and commutation of independent coordinates,
\[
              {\cal A}(x_1,\ldots,x_j)\,p^{\otimes j}
                        ={\cal A}(x_1p,\ldots,x_jp)=0 .
\]
The unit on the left forces \(p^{\otimes j}=0\), hence \(p=0\) by its product trace.
In a finite tracial algebra an affiliated operator with zero kernel has dense range and an affiliated inverse.
For a dependent initial list in a finite combination, choose a complex basis from that very list and apply the same argument at the resulting arity.

### Finite coefficient extensions inside the affiliated algebra

Assume first rational matrix integrality on every \(G^j\).
Then \(D=D_1\) is itself a division ring.
For scalars \(c_1,\ldots,c_s\) used by a given finite complex matrix, let \(E\) be the subring generated inside \(U(G)\) by \(D\) and those scalars.
Every nonzero member of \(E\) is a finite complex linear combination of elements of \(D\), hence is an affiliated unit by the preceding test.
In particular \(E\) is a domain.
It is an image of \(D[T_1,\ldots,T_s]\) with central commuting variables and therefore is left and right Noetherian by the central-variable Hilbert basis theorem.
It is an Ore domain: if nonzero right ideals \(aE,bE\) had zero intersection, the sum of \(b^i aE\), \(i\ge0\), would be direct by consecutive cancellation, violating the ascending chain condition.
The left-handed argument is identical.
The fraction division ring of \(E\) embeds in \(U(G)\) because all its denominators are affiliated units.
Thus the given matrix reduces by Gaussian operations in the actual affiliated algebra to an identity block and a zero block.
Its regular rank is the size of the identity block, using invariance of the finite tracial rank under invertible affiliated row and column operations.
Recall that [restriction of scalars on the original group alone](../ledger/Yin_L_A0030_v1.md#the-precise-limit-of-restriction-of-scalars) can lose a fractional-rank obstruction.
Here the extra input is rational integrality on direct powers, with separate spatial coordinates.
[JZ19's same-group coefficient transfer](../audits/literature/JZ19/Yin_U001.md#jz19-u001) instead uses its stated sofic and algebraic-coefficient hypotheses.

Integral and rational matrices have the same integrality test by clearing scalar denominators.
Finite direct powers of a torsion-free group are torsion-free, proving the two universal equivalences.

### A bound for the direct power needed by a prescribed size

Under the rational integrality premise on \(G^J\), the same holds for each \(G^j\) with \(1\le j\le J\) by the coordinate subgroup inclusion and invariance of trace under subgroup induction.
For \(M\ge0\), let \(V_M\subset U(G)\) be the right \(D\)-linear span of the scalar monomials in the \(c_i\) of total degree at most \(M\).
Then \(V_0=D\), \(\dim_D V_M\le\binom{M+s}{s}\), and \(V_M V_N\subset V_{M+N}\) since the scalar monomials commute with \(D\).
Each nonzero element of \(V_{M_r}\) is an affiliated unit: its expansion is a complex linear combination of at most \(J\) elements of \(D\), and one uses alternation at the actual independent length of that expansion.

The input entries lie in \(V_1\).
At step \(i\), with entries in \(V_M,\ M=M_i\), discard a zero residual matrix or move a nonzero pivot \(a\) to position \((1,1)\).
The pivot is an affiliated unit.
Since the binomial bound grows polynomially in \(k\), the defining \(k=k_i\) exists.
For some \(0\le l<k\) one has \(2\dim_D V_{lM}>\dim_D V_{(l+1)M}\); otherwise iteration from \(\dim_D V_0=1\) would contradict \(2^k>\binom{kM+s}{s}\).
For each other pivot-row entry \(b\), the right \(D\)-linear map
\[
       V_{lM}\oplus V_{lM}\longrightarrow V_{(l+1)M},
                       \qquad (u,v)\longmapsto a u-b v
\]
has a nonzero kernel vector.
Its \(v\ne0\) by injectivity of \(a\), and \(v\) is an affiliated unit by the established arity bound.
After Schur elimination, right multiplication of this residual column by \(v\) replaces its entries by \(M_{ij}'v-M_{i1}'u\), where \(M_{ij}'\) are entries of the current matrix.
They belong to \(V_{(l+1)M}\subseteq V_{M_{i+1}}\).
These operations preserve regular rank except for the one separated pivot.
At most \(r\) iterations are required, proving the explicit finite-power criterion.
The bound concerns the number of group coordinates; it gives no general integrality result for the rational matrices on that power.

## Assessment history

### Decision alternating-coefficients

| Field | Value |
| --- | --- |
| date | 2026-11-21T04:36 |
| status | proved |
| reason | Independent review verified both universal reductions and bounded elimination inside the actual affiliated rings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One- and two-sided signed witnesses, universal integral formulations and the finite arity bound. |
| argument | [Proof](#argument) | Finite-support alternation, affiliated tensor separation, fraction fields and the explicit filtration bound. |
| review | [Whole finding](../audits/reviews/Yin_R_A0132_v1.md#whole-finding) | Complete independent inspection at the mathematical and source scope stated in the finding. |

## Current assessment

[Selected decision](#decision-alternating-coefficients)
