---
author: Yin
---

# Which spectral functions of the lamplighter contraction lie in the division closure?

## Statement

Let \(\Gamma=C_2\wr\mathbb Z\), let \(D_\Gamma\) and \(R_\Gamma\) be the division closure and the \(*\)-regular closure of \(\mathbb C\Gamma\) in its affiliated ring, and take the [positive contraction \(H\)](Yin_C_A0177_v1.md#statement).
Concretely, \(b\) records binary edge labels, \(e\) marks the vertices at which zero changes to one, \(g=\nabla(1-e)\), \(P=g(g^*g+e)^{-1}g^*\), and \(H=PbP\).
Its spectral law is purely atomic, with positive mass at every rational number in \([0,1]\).
Put \(S=\mathbb Q\cap(0,1)\).
For every function \(f:S\cup\{0,1\}\to\mathbb C\), possibly unbounded, the affiliated operator \(f(H)\) satisfies the following criteria.

1. \(f(H)\in D_\Gamma\) exactly when a complex rational function with no poles on \(S\) agrees with \(f\) everywhere on \(S\).
2. \(f(H)\in R_\Gamma\) exactly when a complex rational function agrees with \(f\) at all but finitely many points of \(S\), allowing its poles on \(S\) among the exceptions.

In both tests \(f(0)\) and \(f(1)\) are arbitrary.
For bounded \(f\) the rational function in either test has no poles on the entire interval \([0,1]\).
Consequently a spectral projection \(1_T(H)\) belongs to \(D_\Gamma\) precisely when \(T\cap S\) is empty or all of \(S\).
It belongs to \(R_\Gamma\) precisely when \(T\cap S\) or its complement in \(S\) is finite.
By the [unrestricted commutator criterion](Yin_C_A0131_v1.md#statement), the latter condition characterizes solvability of equation (1) for these projections.
The results apply to the binary lamplighter group with its customary torsion lamps.

## Argument

### Reading a spectral value from periodic linear equations

Write \(p_0,p_1\) for the endpoint spectral projections and \(E=1-p_0-p_1\), all in \(D_\Gamma\). [Endpoint projections](Yin_C_A0177_v1.md#rational-and-nonrational-atoms)
Suppose \(f(H)\in R_\Gamma\) and put \(u=Ef(H)\).
Between successive marked vertices a word \(1^n0^m\) has an interior eigenline spanned by the vector taking value \(m\) on the first run and \(-n\) on the second, with eigenvalue \(m/(n+m)\). [Cell calculation](Yin_C_A0177_v1.md#the-edge-projection-on-one-cell)
At a height let the cylinder projection \(c_{nm}\) require the pattern \(0\,1^n0^m\,1\) starting one step before that height.
It selects precisely the start of each matching cell.
On each such cell the diagonal entry at the start of its interior line projection is \(m^2/(nm^2+mn^2)\).
Since \(u\) acts separately on the cells, it follows in the affiliated algebra that
\[
    c_{nm}u c_{nm}=d_{nm}c_{nm},\qquad
    d_{nm}=\frac{m}{n(n+m)}f\!\left(\frac{m}{n+m}\right).
\]

Choose the [single-vector presentation](Yin_C_A0137_v1.md#testing-a-whole-space-or-a-single-vector) for \(u^*\in R_\Gamma\).
It gives a group-ring matrix \(K\), a complex row \(\epsilon\), a complex column \(\gamma\) and an affiliated row \(v\) with \(vK=\epsilon,\ v\gamma=u^*\) and \(yK=0\Rightarrow y\gamma=0\).
Thus \(K^*x=\epsilon^*w\) is solvable for every affiliated \(w\), and \(\gamma^*x=uw\) for every solution.
When \(u^*\) is scalar the same presentation follows directly with \(K=\epsilon=1,\ \gamma=u^*\).

At the periodic word \(1^n0^m\), use \(F=\mathbb C(z)\), where \(z\) denotes translation through one period, and let primes denote periodic evaluation.
The involution conjugates scalars and takes \(z\) to \(z^{-1}\).
The global inclusion \(\ker K\subseteq\ker\epsilon\) follows from \(vK=\epsilon\), and transfers to \(\ker K'\subseteq\ker\epsilon'\) over \(F\) by [finite-height specialization](Yin_C_A0138_v1.md#finite-height-relations-at-a-periodic-configuration).
Indeed, a failure over \(F\) would have a Laurent-polynomial vector witness after clearing denominators, giving a finitely supported counterexample on every configuration in a nonempty cylinder.
The group trace gives each such cylinder positive measure.
The adjoint image is the orthogonal complement of the kernel for finite matrices over \(F\), by nondegeneracy of the standard Hermitian form and the rank identity.
Hence \(K'^*x=\epsilon'^*w\) is solvable for all \(w\).

With \(c=c_{nm}\), a second global kernel inclusion is
\[
    \ker[K^*,-\epsilon^*c]\ \subseteq\ \ker[c\gamma^*,-d_{nm}c].
\]
This follows from the preceding input-output formula and \(cuc=d_{nm}c\) on affiliated columns.
It holds on Hilbert kernels since their projections generate the affiliated kernels.
Every entry of the displayed matrices is in the group algebra for this fixed pair \(n,m\), so the same finite-height transfer applies.
On the periodic word \(c'\) selects height zero.
Taking \(w=\delta_0\), solve \(K'^*x=\epsilon'^*\delta_0\) and read the height-zero value of \(\gamma'^*x\).
This value is \(d_{nm}\) for every solution.
The periodic system uses the same group-ring matrix and constant vectors for every pair \(n,m\).

### Reducing long runs to a fixed number of variables

Choose \(w\ge1\) larger than every shift length and observation radius in \(K^*\).
At height \(i\) the system has the form \(\sum_{j=-w}^w A_{ij}x_{i+j}=g_i\), with \(g_i=0\) except at the source modulo the period.
Use a state \(s_i=(x_{i-w},\ldots,x_{i+w-1})\).
The states \(s_i,s_{i+1}\) must agree on the overlap, and their union supplies all entries of the equation at height \(i\).
When \(g_i=0\) this defines a linear relation on a fixed finite-dimensional state space.
The states at the two ends of a period obey \(s_{n+m}=z^{\pm1}s_0\), with the sign determined by the translation convention.
Together the overlap conditions and this equality reconstruct the periodic vectors and every original row, including the rows that cross the period boundary.

For all sufficiently large \(n,m\), keep the transitions at fixed distances from either interface as individual equations, including the source and the output at zero.
The two long remaining segments have constant labels with constant rows, giving linear relations \(L_1,L_0\) at every step.
Their endpoint conditions are the composed powers \(L_1^{n-a},L_0^{m-b}\), where \(a,b\) count fixed numbers of retained steps.
All retained equations, output coordinate and end identifications have fixed coefficients in \(F\).
To write the composed powers with a fixed number of rows, consider any linear relation \(L\) on a finite-dimensional vector space.
For \(L^j\), its domain and image decrease with \(j\), and its kernel and multivalued part increase.
Here the multivalued part consists of the outputs attainable from the zero input.
Choose \(J\ge1\) beyond stabilization of all four spaces and denote their stable values by \(D,I,K_0,M_0\).
For \(j\ge J\), the relation \(L^j\) induces an isomorphism \(A_j:D/K_0\to I/M_0\).

The map \(I\cap D\to I/M_0\) is onto.
For \(y\in I\), choose \((x,y)\in L^j\), then use \(x\in\operatorname{dom} L^{j+J}\) to find an intermediate value \(y'\in I\cap D\) with \(y-y'\in M_0\).
For \(y\in D\cap M_0\), any pair \((y,v')\in L^J\) composes with \((0,y)\in L^j\) to give \(v'\in M_0\).
Injectivity of \(A_J\) gives \(y\in K_0\).
It follows that \(I\cap D\to D/K_0\) induces a map \(T:I/M_0\to D/K_0\), obtained by choosing a representative in \(I\cap D\).
Composition gives \(A_{j+J}=A_J T A_j\), so \(T\) is invertible, including for zero-dimensional quotients.
In fixed bases the equations for \(L^j\) now require an input \(x\in D\), an output \(y\in I\) and \(y+M_0=A_j(x+K_0)\).
Along each residue class modulo \(J\), the matrices \(A_j\) are given by powers of a fixed invertible matrix times a fixed initial matrix.

Restrict both run lengths to multiples of a common multiple of the two stabilization indices, writing \(n=hN,\ m=hM\).
Then \(n-a,\ m-b\) follow fixed residue classes and tend beyond stabilization.
By Jordan form, the entries of both relations, and hence of the fixed-size system, are exponential polynomials in \(N,M\) over an algebraic closure \(k\) of \(F\).
An exponential polynomial is a finite sum of terms \(p(N,M)\lambda^N\mu^M\) for polynomials \(p\in k[N,M]\) and nonzero \(\lambda,\mu\in k\).
Enlarge \(h\) by a common factor killing the torsion subgroup of the finitely generated multiplicative group of all the bases, since this replaces every base by that power.
The resulting group is free abelian of finite rank, with basis \(\eta_1,\ldots,\eta_d\).
All the coefficients then belong to the Laurent polynomial ring
\[
 \mathcal B=k[N,M,X_1^{\pm1},\ldots,X_d^{\pm1},Y_1^{\pm1},\ldots,Y_d^{\pm1}],
 \qquad X_i=\eta_i^N,\quad Y_i=\eta_i^M .
\]
Evaluation on the pairs \(N,M\) above any fixed lower bounds is injective as a map from \(\mathcal B\) to arrays.
For one variable the sequences \(p(j)c^j\) have independent polynomial coefficients at distinct nonzero bases \(c\).
Indeed the difference \(s(j+1)-c s(j)\) lowers the polynomial degree at base \(c\) and preserves the exact degree at every other base.
Applying sufficiently many such differences eliminates all bases but a selected one and preserves its nonzero term.
Applying independence in \(N\) and then \(M\) proves the stated injectivity.

### A scaling identity and the exceptional slopes

The reduced linear system over \(\operatorname{Frac}(\mathcal B)\) is consistent and has a unique output.
In fact if its coefficient matrix has rank \(r\) over that field, all minors of size \(r+1\) in either its augmentation by the source column or its augmentation by the output row vanish on the integer quadrant under consideration.
This follows from consistency and uniqueness at every evaluated pair, since the rank of the evaluated coefficient matrix is at most \(r\).
They therefore vanish in \(\mathcal B\), giving the two assertions by linear algebra over the fraction field.
Using one nonzero minor of size \(r\), solve on its selected columns with the other unknowns set to zero and evaluate the output.
Wherever that minor stays nonzero, this solution works at the evaluated pair because the ranks of both the coefficient matrix and its augmentation are \(r\).
For \(r=0\) use the empty minor \(1\).
Multiplying the resulting output by \(n(n+m)/m\) gives \(A,B\in\mathcal B\), with \(B\ne0\), such that for all sufficiently large \(N,M\) with \(B(N,M)\ne0\),
\[
                f(M/(N+M))=\frac{A(N,M)}{B(N,M)} .
\]
Here one can keep the chosen minor as a factor of \(B\) before cancellation.

Doubling both indices preserves the left side.
If \(\sigma\) sends \((N,M,X,Y)\) to \((2N,2M,X^2,Y^2)\), fixing \(k\) and squaring coordinatewise, then
\(B\,\sigma(B)\,[A\,\sigma(B)-\sigma(A)\,B]\) evaluates to zero on the quadrant.
Injectivity of evaluation, the domain property and injectivity of \(\sigma\) imply that \(A/B\) is fixed by \(\sigma\).
For each variable \(X_i\) or \(Y_i\) the degree of this fraction as a rational map of that variable doubles under \(\sigma\).
The induced map on the coefficient field of the other variables is injective and preserves both the degrees of a reduced numerator and denominator and their Bézout identity.
Substituting the square of the remaining variable still preserves coprimality and doubles the larger degree.
Thus \(A/B\) belongs to \(k(N,M)\).
In \(k(M/N)(N)\) a rational function invariant under \(N\mapsto 2N\) belongs to \(k(M/N)\).
Over the algebraic closure of \(k(M/N)\), any nonzero finite zero or pole would give an infinite orbit of zeros or poles.
A function with zeros and poles only at zero and infinity is a monomial, and invariance forces exponent zero.
The zero function also satisfies the conclusion.
Write \(A/B=R(M/N)\) in reduced rational form over \(k\).

Only finitely many positive rational slopes \(v/u\), with \(u,v\) positive integers, can make \(B(ju,jv)\) identically zero for all sufficiently large \(j\).
Combine the nonzero terms of \(B\) by their distinct exponent pairs \((\mathbf a,\mathbf b)\) in \(X,Y\).
Two resulting exponential bases in \(j\) coincide only if \(u(\mathbf a-\mathbf a')+v(\mathbf b-\mathbf b')=0\), by multiplicative independence of the \(\eta_i\).
Each pair excludes at most one slope.
Choose one nonzero polynomial coefficient of \(B\) and observe that any of its nonzero homogeneous components vanishes on only finitely many lines \(M=(v/u)N\).
Outside those exceptions, one-variable independence gives \(B(ju,jv)\ne0\) for arbitrarily large \(j\).
Also exclude the finitely many poles of \(R\).
The equality in the fraction field then gives \(f(v/(u+v))=R(v/u)\) on every remaining slope by evaluating the cross-multiplied identity.

The coefficients of the reduced fraction can be taken complex.
For \(d'\) the larger degree of its numerator and denominator, choose \(2d'+1\) distinct permissible rational arguments where its values are complex.
The interpolation equations for a numerator and denominator of degrees at most \(d'\) have complex coefficients and have the given reduced pair as a nonzero solution over \(k\).
For any solution, cross multiplication with the given pair gives a polynomial of degree at most \(2d'\) vanishing at \(2d'+1\) points.
Coprimality and the degree bound therefore make every solution a scalar multiple of the given pair.
The coefficient matrix has the same rank over \(\mathbb C\) as over \(k\), giving a nonzero complex solution and \(R\in\mathbb C(t)\).
Composing with \(s\mapsto s/(1-s)\) yields the required rational interpolant on \(S\) outside finitely many points.

### Detecting the individual exceptions

For a rational interpolant \(a/b\) with coprime \(a,b\in\mathbb C[t]\), the affiliated relative inverse of \(b(H)\) is in \(R_\Gamma\).
Consequently \(a(H)b(H)^{[-1]}\) agrees with \(f(H)\) outside its finitely many exceptions and endpoints whenever the cofinite rationality condition holds.
The projection at each atom \(r\) belongs to \(R_\Gamma\), being the kernel projection of \(H-r\).
Correcting those finitely many scalar values gives \(f(H)\in R_\Gamma\).
This proves the second criterion.

Now suppose \(f(H)\in D_\Gamma\).
Take the interpolant \(a/b\) already proved to exist, and form \(V=E(b(H)f(H)-a(H))\in D_\Gamma\).
Its values vanish except on a finite subset of \(S\).
If its value at any such point \(r\) were nonzero, polynomial interpolation on this finite support would give a polynomial \(l\) with \(l(H)V=1_{\{r\}}(H)\).
This would place that projection in \(D_\Gamma\), contrary to [nonrationality of the interior atoms](Yin_C_A0177_v1.md#rational-and-nonrational-atoms).
Hence \(b(r)f(r)=a(r)\) at every \(r\in S\).
Coprimality prevents \(b\) from vanishing anywhere on \(S\), proving the necessity in the first criterion.

Conversely suppose \(f=a/b\) on all of \(S\) and \(b\) has no zero there.
The element \(b(H)E+1-E\) has no kernel, since the atomic law is supported on the indicated eigenvalues and it equals the identity on the endpoints.
It is an affiliated unit in \(D_\Gamma\), and
\[
        f(H)=a(H)E\,[b(H)E+1-E]^{-1}+f(0)p_0+f(1)p_1
\]
belongs to \(D_\Gamma\).
If \(f\) is bounded, then by density even the cofinite rational interpolant has no pole on the real interval, since values on rational eigenvalues tending to a pole would be unbounded.
Finally, a rational function taking only the values zero and one on a cofinite subset of \(S\) is identically zero or identically one, by the polynomial identity for \(R(R-1)\).
This gives both projection tests.

## Assessment history

### Decision spectral-functions

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:32 |
| status | proved |
| reason | The periodic input-output equations force a single rational function away from finitely many slopes, and the nonrationality of each interior atom excludes all exceptions in the division closure. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Division and regular closure criteria on all affiliated spectral functions, bounded cases and spectral projections. |
| argument | [Argument](#argument) | Periodic equations, fixed-size relations, doubling and exceptional slopes, and recovery of the individual atoms. |
| dependency | [Spectral law and projections](Yin_C_A0177_v1.md#statement) | Positive mass at every rational slope, the two endpoint projections and nonmembership for interior atoms. |
| dependency | [Linear presentation](Yin_C_A0137_v1.md#testing-a-whole-space-or-a-single-vector) | A finite input-output system for an element of the regular closure. |
| dependency | [Periodic kernel inclusions](Yin_C_A0138_v1.md#finite-height-relations-at-a-periodic-configuration) | Transferring solvability and uniqueness to the two-run period. |
| dependency | [Commutator equation](Yin_C_A0131_v1.md#statement) | Its equivalence to membership in the regular closure. |
| review | [Spectral functions](../audits/reviews/Yin_R_A0176_v1.md#spectral-functions) | Two independent reviews of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-spectral-functions)
