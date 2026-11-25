---
author: Yin
---

# Laurent asymptotics in measure and rational evaluation at a central group generator

## Statement

Let \(G\) be a finitely generated discrete group, \(A=\mathbb CG\), \(U=L^0(\mathcal N(G))\), and \(S=\operatorname{Div}_{U((z))}(A[z])\), with \(z\) a central formal variable.
For \(J=G\times\mathbb Z\), write \(Z\) for the positive generator of the central infinite cyclic factor.
There is an injective ring homomorphism \(S\to D_J\) extending the coefficient inclusion and sending \(z\) to \(Z\).
Here \(D_J\) is the scalar division closure of \(\mathbb CJ\) in \(U_J=L^0(\mathcal N(J))\).

If \(f=\sum_{j\ge-m}b_jz^j\in S\), fix one scalar rational expression giving \(f\).
Off a countable set of complex numbers \(s\) all its gates are defined in \(U\).
For every integer \(h\ge-m\), its value \(f(s)\) there satisfies
\[
       s^{-h}\left(f(s)-\sum_{j=-m}^h b_j s^j\right)\longrightarrow0
                   \quad\text{in measure as }s\to0.
\]
The same exceptional set works for each \(h\), including on the real line.
On the unit circle the evaluated expression is a representative of the Fourier transform of the image of \(f\).
The statement concerns asymptotic expansions in measure and allows a different exceptional set for another expression.

For a square matrix \(X\) over \(A\), the entries of \((ZI-X)^{-1}\) always belong to \(D_J\).
They all lie in the image of \(S\) if and only if \(\ker X^m=\ker X^{m+1}\) on Hilbert-space columns for some finite \(m\ge0\), with \(X^0=I\).
The least such \(m\) is the pole order of \((zI-X)^{-1}\) in the formal Laurent series ring, taking order zero for a formal power series.
The inclusion can be strict, even for the product of \(G\) with just one central infinite cyclic group.
None of these assertions presupposes that \(D_G\) is a division ring.

## Argument

### Full rank away from a countable set

Suppose \(L(z)\) is a square polynomial matrix over \(U\) invertible over \(U((z))\) and write \(L^{-1}=\sum_{j\ge-m}B_jz^j\), with \(m\ge0\).
For \(N\ge0\) its finite truncation \(K_N=\sum_{j=-m}^N B_jz^j\) satisfies
\[
         LK_N=I+z^{N+1}H_N,\qquad K_N L=I+z^{N+1}\widetilde H_N
\]
with polynomial matrices \(H_N,\widetilde H_N\) over \(U\).
Indeed the Laurent polynomials on the left agree with \(I\) in every degree through \(N\).
The finite products \(L(s)K_N(s)\) converge in measure to \(I\) as complex \(s\ne0\) tends to zero.
Their ranks tend to the full matrix size: for any \(\varepsilon>0\) there is a projection of relative trace at least \(1-\varepsilon\) on which the error from \(I\) eventually has norm less than \(1/2\), using a possibly different projection at each \(s\).
Its intersection with the kernel is zero, giving the rank estimate by the dimension formula for two projections.
The rank of each factor also has supremum the full size.

Every matrix polynomial \(P(s)\) with affiliated coefficients has its maximal rank off a countable subset of the complex plane.
Take \(d=(1+\sum_\ell c_\ell^*c_\ell)^{-1/2}\) for all its scalar coefficients \(c_\ell\).
Right multiplication by \(dI\) preserves each rank and gives bounded coefficients.
The [Vandermonde rank estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) for the resulting polynomial of degree \(e\) bounds the sum of its deficits from the supremum rank on any finite set by \(e\) times that supremum.
One obtains the bound for a supremum by taking reference ranks tending to it.
Thus only countably many parameters have a positive deficit.
This applies also to Laurent polynomial matrices away from zero by multiplication by a power of the parameter.
In particular \(L(s)\) and every \(K_N(s)\) are affiliated units off one countable set because a square matrix of full rank in a finite von Neumann algebra has an affiliated inverse.

### Coefficients of a rational expression

On this set of allowed parameters put \(Q_N(s)=L(s)K_N(s)\).
Then \(Q_N(s)^{-1}\to I\) in measure by continuity of inversion at units. [Measure topology at a unit](../ledger/Yin_L_A0075_v1.md#regular-specialization-of-the-compressed-resolvent)
The identity \(L(s)^{-1}=K_0(s)Q_0(s)^{-1}\) gives \(s^m L(s)^{-1}\to B_{-m}\) in measure.
Using the exact remainder
\[
                       L(s)^{-1}-K_N(s)=-s^{N+1}L(s)^{-1}H_N(s)
\]
and setting \(N=h+m\) now proves the desired expansion of the matrix inverse through degree \(h\).
Indeed \(s^{-h}\) times this remainder tends to zero in measure, since \(s^m L(s)^{-1}\) and \(H_N(s)\) converge in measure and the remaining scalar factor is \(s\).
Subtracting the extra finitely many terms between \(h+1\) and \(N\) preserves the limit.

Every element of \(S\) has the form \(\alpha L^{-1}\beta\) with a polynomial square matrix over \(A[z]\) and constant complex vectors \(\alpha,\beta\). [Formal realizations](Yin_C_A0141_v1.md#recovering-a-laurent-coefficient-from-finitely-many-equations)
Applying the block diagonal, triangular and bordered realizations also at each internal gate shows that the original expression can be evaluated at any parameter where this finite list of pivots is invertible.
Taking the union of their exceptional sets and the exceptions for the truncations of the final pivot therefore suffices.
The matrix inverse expansion gives the stated coefficients after contraction with \(\alpha,\beta\).
The proof also gives entrywise expansions for finite matrices of scalar expressions.

### Preservation of formal identities

Under Fourier transform \(\mathcal N(J)=\mathcal N(G)\,\overline\otimes\,L^\infty(\mathbb T)\), the polynomial pivots give matrices over \(\mathbb CJ\) that are affiliated units by their full fiber rank almost everywhere.
Their inverses have entries in \(D_J\) by [scalar Gram elimination](Yin_C_A0132_v1.md#argument).
For a direct check of vanishing on the unit circle, assume \(\alpha L^{-1}\beta=0\) as a formal series.
A finite-height Hilbert vector \((x,w)\) in the kernel of the row \([L(Z),-\beta]\) has finitely many coefficients in \(L^2(\mathcal N(G))\subset U\).
Its Laurent polynomial columns satisfy \(L(z)x(z)=\beta w(z)\), hence \(\alpha x(z)=0\) by the formal identity.
Finite-height vectors are dense in that Hilbert kernel by [finite-coset localization](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) for the normal subgroup \(G\) of \(J\).
Thus \([\alpha,0]\) annihilates the entire kernel and its generating projection in the affiliated module.
Applying it to the affiliated graph column \((L(Z)^{-1}\beta,1)^{\mathsf T}\) gives \(\alpha L(Z)^{-1}\beta=0\).
Under Fourier transform on the cyclic factor this proves vanishing almost everywhere on the circle.
Consequently the polynomial border \(\left(\begin{smallmatrix}L&\beta\\\alpha&0\end{smallmatrix}\right)\) has rank \(n\) there almost everywhere by Schur elimination, where \(n\) is the size of \(L\).
The same countability result for the border and pivot now gives exact vanishing of the scalar output outside a countable subset of the complex plane.
Apply this to differences of expressions to get a well-defined ring homomorphism by evaluation on a joint conull subset of the unit circle.
The operations of any selected expression then give its evaluated fibers, proving the target assertion.
If the image of \(f\) in \(D_J\) is zero, the border for its realization has rank \(n\) almost everywhere on the circle.
By the complex-plane countability result this equals the maximal rank of the border, since the pivot has maximal rank \(n\) on the same conull set.
It follows that \(f(s)=0\) off a countable set of complex parameters.
The asymptotic expansion then gives \(b_j=0\) successively in the Hausdorff measure topology.
This proves injectivity.

### Formal inversion by scalar pivots

Equip \(U((z))\) for this paragraph with the coefficientwise involution fixing \(z\).
The involution is not needed to define the evaluation homomorphism.
We verify that every square polynomial matrix \(C\) over \(A[z]\) which is invertible over \(U((z))\) already has entries of its inverse in \(S\).
For each leading group of columns \(V\) of \(C\), the corresponding rows of \(C^{-1}\) give a formal left inverse \(J_0\).
Choose \(k\ge1\) so that \(z^k J_0\) has order at least one.
The series \(I-z^{2k}J_0^*J_0\) has a selfadjoint square root \(W\), given by the scalar binomial expansion around \(I\) with finitely many terms in each degree.
As \(J_0V=I\), its Gram matrix satisfies
\[
                  V^*V=z^{2k}I+(WV)^*(WV).
\]

Any Hermitian Laurent matrix of this last form has a formal inverse.
For completeness let \(H=z^{2k}I+Y^*Y\), where \(Y\) can have finitely many negative powers.
The first nonzero coefficient of \(Y^*Y\), when \(Y\ne0\), is \(Y_r^*Y_r\) at twice the first degree \(r\) of \(Y\).
The same argument for a finite sum of squares uses that a sum of \(a_i^*a_i\) vanishes only when every \(a_i=0\).
Thus the least degree \(j\) of a nonempty square \(H\) is at most \(2k\), and its coefficient in degree \(j\) is positive.
Let \(p\) be its support and \(q=I-p\).
The \(p,p\) block of \(H\), divided by \(z^j\), has invertible constant coefficient in its affiliated corner.
The other blocks involving \(q\) have orders at least \(j+1\).
Eliminate the \(p,p\) block in formal series.
The resulting Schur complement on \(q\) has order at least \(j+1\), since the two off-diagonal blocks have order at least \(j+1\) and the pivot inverse has order at least \(-j\).
Moreover this complement retains the form \(z^{2k}q+\sum_i V_i^*V_i\).
Indeed write it as \(H_0^* H H_0\) with \(H_0=(-H_{pp}^{-1}H_{pq},q)^{\mathsf T}\).
For \(B=-H_{pp}^{-1}H_{pq}\), the contribution from \(H_0^*H_0-q\) is \(B^*B\).
The lowest-degree argument can now be iterated on the complement.
A nonzero remaining corner cannot have order greater than \(2k\), and at order \(2k\) its first coefficient dominates its identity and is invertible.
The finite increase in orders proves formal invertibility of \(H\) by reversing elimination.

It follows that each leading principal block of \(C^*C\) is a formal unit.
Ordinary scalar Schur elimination then expresses every entry of \((C^*C)^{-1}\) in \(S\): the scalar Schur complement of an invertible leading block is a unit because the enlarged leading block is a unit.
The entries of \(C^{-1}=(C^*C)^{-1}C^*\) therefore belong to \(S\).

### Resolvent poles and strict inclusion

The polynomial \(zI-X\) has full rank at some ordinary scalar parameter, for example any real \(s>\|X\|\) by bounded inversion.
The countability result shows that \(ZI-X\) is an affiliated unit in \(U_J\), so its inverse has entries in \(D_J\) by scalar Gram elimination.
Its entries come from \(S\) exactly when \(zI-X\) has an inverse over \(U((z))\): one direction follows from injectivity of evaluation and the two inverse identities, the other from formal scalar pivots.

In the finite ring of matrices over \(U\), kernels and images are generated by the kernel and range projections of the corresponding Hilbert operators.
Suppose \(\ker X^m=\ker X^{m+1}\).
The kernels of all higher powers then stabilize by induction.
The affiliated modules \(\operatorname{im}X^m\) and \(\ker X^m\) intersect trivially, since \(X^{2m}v=0\) implies \(X^mv=0\).
Their dimensions add to the full size and their sum is generated by a projection, being the image module of a finite matrix.
Trace faithfulness therefore gives a direct sum equal to the entire module.
The map \(X\) is invertible on \(\operatorname{im}X^m=\operatorname{im}X^{m+1}\), since the inclusion of the second image in the first is between projection-generated modules of equal dimension.
It is nilpotent on \(\ker X^m\).
This splitting gives a power series inverse on the invertible summand and the finite geometric expression in \(z^{-1}\) on the nilpotent summand.
Conversely, if the formal inverse has pole order at most \(m\), take \(v\) in the affiliated kernel of \(X^{m+1}\).
By multiplication its value on \(v\) is \(\sum_{j=0}^m X^jv z^{-j-1}\).
The coefficient of \(z^{-m-1}\) gives \(X^m v=0\).
This proves the exact pole order.

For strict inclusion, in the lamplighter group \(G=C_2\wr\mathbb Z\) take the compressed shift \(v=ptp\), where \(p=(1+a)/2\) is the open-lamp projection and \(t\) shifts the lamps.
On a run of \(\ell\) open sites bounded by closed sites it is a nilpotent shift with index \(\ell\). [Finite runs and their positive probability](../ledger/Yin_L_A0078_v1.md#the-lamp-and-its-finite-paths)
Each length occurs with positive probability.
Consequently \(\ker v^m\subsetneq\ker v^{m+1}\) for every \(m\), so \((ZI-v)^{-1}\) is a scalar in \(D_J\) outside the image of \(S\).
The same proof applies to \(K\wr\mathbb Z\) whenever \(D_K\) contains a projection of trace strictly between zero and one, with the scalar \(v\) now in \(D_G\).
Here \(v\in D_G\) has a finite scalar rational expression, so the constant copy of \(v\) belongs both to \(S\) and to \(D_J\).
At every nonzero scalar parameter \(s\), \(s-v\) is an affiliated unit by its inverses on the finite runs, and Fourier transformation gives the affiliated unit \(Z-v\).
Its inverse belongs to \(D_J\) by scalar division closure.
A preimage under evaluation would give a formal inverse of \(z-v\) by injectivity and would contradict the failure of kernel stabilization.
If \(K\) is finitely generated and torsion-free, then \(G\) is also finitely generated and torsion-free.
This last scope requires the stated rational lamp projection and leaves the unconditional torsion-free deletion question open.

Finally the asymptotic estimates can hold without convergence of the Laurent series in measure at any fixed small nonzero argument.
For \(G=\mathbb Z=\langle g\rangle\), the group-ring element \(a=2-g-g^{-1}\) acts as \(2-2\cos\theta\).
Its kernel projection is zero and the positive spectrum accumulates at zero.
The formal inverse of \(a+z\) has coefficients \((-1)^j a^{-j-1}\) for \(j\ge0\).
For every \(0<s<4\) the set where \(0<a<s/2\) has positive Haar measure and on this set the individual terms of the evaluated expansion grow in modulus with \(j\).
Thus the series fails to converge in measure there even though the full asymptotic conclusion holds.

## Assessment history

### Decision analytic-laurent-specialization

| Field | Value |
| --- | --- |
| date | 2026-11-25T10:49 |
| status | proved |
| reason | Finite truncations of the inverse give exact asymptotic coefficients in measure, and finite-height graph relations preserve formal identities under central specialization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Laurent asymptotics, the injective specialization and the exact criterion for a resolvent to belong to its image. |
| argument | [Argument](#argument) | Countable rank exceptions, two-sided Gram inversion, stabilized kernels of powers and the strict-inclusion examples. |
| dependency | [Parameter rank bound](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | Uniform bound on the sum of rank deficits of a polynomial. |
| dependency | [Formal realizations](Yin_C_A0141_v1.md#recovering-a-laurent-coefficient-from-finitely-many-equations) | Domain-compatible polynomial matrices for scalar rational expressions. |
| dependency | [Finite-coset localization](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) | Density of finite-height vectors in a bounded graph kernel. |
| dependency | [Matrix Gram pivots](Yin_C_A0132_v1.md#argument) | Affiliated matrix inverses and their scalar rational expressions. |
| dependency | [Measure inversion](../ledger/Yin_L_A0075_v1.md#regular-specialization-of-the-compressed-resolvent) | Continuity of inversion in measure at a unit. |
| dependency | [Lamp runs](../ledger/Yin_L_A0078_v1.md#the-lamp-and-its-finite-paths) | Positive-measure intervals of arbitrary finite length. |
| review | [Analytic specialization](../audits/reviews/Yin_R_A0169_v1.md#analytic-specialization) | Independent proof review at the specified scope. |

## Current assessment

[Selected decision](#decision-analytic-laurent-specialization)
