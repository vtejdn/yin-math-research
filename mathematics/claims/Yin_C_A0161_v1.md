---
author: Yin
---

# Ore denominators and finite group-ring generators of rational kernels

## Statement

Let \(G\) be a countable discrete group, \(A=\mathbb CG\), \(U=L^0(\mathcal N(G))\), \(D=\operatorname{Div}_U(A)\), and \(S=A\cap U^\times\).
Use the unnormalized matrix trace for von Neumann dimension and rank.
Say that the kernel of \(X\) is exhausted by group-ring columns if some finite matrix \(Y\) over \(A\) satisfies \(XY=0\) and \(\overline{\operatorname{im}Y}=\ker X\).
For affiliated \(X\), the product is taken in the affiliated ring.

The following conditions on \(G\) are equivalent.

1. \(S\) satisfies the right Ore condition in \(A\), meaning that for every \(s\in S\) and \(a\in A\) there exist \(c\in S\) and \(b\in A\) with \(ac=sb\).
2. Every \(u\in D\) is a single right fraction \(bc^{-1}\) with \(b\in A\) and \(c\in S\).
3. Every rectangular matrix over \(D\) whose orthogonal kernel projection has entries in \(D\) has its kernel exhausted by group-ring columns.
4. The kernels of the group-ring rows \(X=[\,s,\,-a\,]\), for \(s\in S,\ a\in A\), are exhausted by group-ring columns.

For each such row the projection is rational, and finite exhaustion is equivalent to the existence of a single group-ring kernel column \((b,c)^{\mathsf T}\) with \(c\in S\).
For finitely generated \(G\), condition 2 also characterizes when the [finite-dimensional rationality criterion](Yin_C_A0137_v1.md#restriction-to-the-right-module-generated-by-the-input) still detects every \(u\in D\) after requiring its witness space to lie in \(A+uA\).
Under condition 1 one may use a single square group-ring annihilator for each rational kernel projection in the [spectral moment criterion](Yin_C_A0160_v1.md#statement).

There is a test for the analytic zero divisors of an individual group \(K\) using only one denominator in its restricted wreath product \(G=K\wr\mathbb Z\).
Let \(t\) be the shift, embed \(a\in\mathbb CK\) at the zeroth lamp, set \(s=t^{-1}-1\), and write \(\theta=\operatorname{rk}_K(a)\).
Then
\[
             \bigl(\exists b\in\mathbb CG,\ c\in S:\ s^{-1}a=bc^{-1}\bigr)
             \qquad\Longleftrightarrow\qquad \theta\in\{0,1\}.               \tag{1}
\]
The kernel of \(X=[\,s,\,-a\,]\) has dimension one.
For \(n\ge1\), all its Hilbert kernel vectors supported on at most \(n\) consecutive heights, together with their right translates, span a closed subspace of dimension
\[
                            1-\theta(1-\theta)^{n-1}.                          \tag{2}
\]
The zeroth power in (2) is one.
The same number bounds the rank of every finite family of group-ring kernel columns whose individual supports fit in \(n\) consecutive heights, even if the intervals differ between columns.
If \(K\) is amenable it equals the supremum of these ranks.

For finitely generated amenable \(K\), \(\mathbb CK\) is a domain precisely when \(s^{-1}a\) has a group-ring right denominator in \(S\) for every \(a\) in the zeroth lamp.
In particular, the following universal assertions over finitely generated torsion-free amenable groups are equivalent.

- The complex strong Atiyah conjecture holds throughout this class.
- Every complex group algebra in the class satisfies the classical right Ore condition on its algebraic non-zero-divisors.
- For every group in the class, every group-ring matrix with rational kernel projection has its kernel exhausted by group-ring columns.

The general deletion question in [A0003](../tasks/Yin_T_A0003_v3.md#contract) asks for rationality of the projections themselves.
The equivalence above measures the additional strength of requiring group-ring witnesses for projections already known to be rational.

For the lamplighter \(L=C_2\wr\mathbb Z\), take \(a=h-1\) with \(h\) the nonidentity zeroth lamp.
The rank deficit at width \(n\) is exactly \(2^{-n}\), and a finite family of group-ring columns attains the rank \(1-2^{-n}\) at each width.
Over \(L\times S_3\) there is a single positive group-ring element with rational orthogonal kernel projection whose kernel no group-ring annihilator exhausts.
Both examples contain torsion.

## Argument

### A row with one invertible entry

The row \(X=[\,s,\,-a\,]\) has affiliated right inverse \((s^{-1},0)^{\mathsf T}\).
Its kernel has dimension one and its orthogonal projection is \(I-X^*(XX^*)^{-1}X\) over \(D\), since \(XX^*\) is an injective positive scalar in \(A\).
Put \(u=s^{-1}a\).
If \(Y\) is a matrix of group-ring kernel columns, write its rows as \(B=(b_i)\) and \(C=(c_i)\).
In affiliated matrices,
\[
                    B=uC,\qquad Y=\binom{u}{1}C .
\]
Extracting the last row gives the reverse factorization of \(C\) through \(Y\), so \(\operatorname{rk}_G Y=\operatorname{rk}_G C\).
Thus \(Y\) exhausts the kernel exactly when \(c=CC^*=\sum_i c_i c_i^*\) has rank one, equivalently \(c\in S\).
In that case \(b=BC^*\in A\) satisfies \(ac=sb\).
Conversely, given this equation with \(c\in S\), the single column \((b,c)^{\mathsf T}\) has rank one and lies in the kernel.
This proves the assertion for a fixed row and the equivalence of conditions 1 and 4.

If condition 1 holds, the right fractions \(AS^{-1}\subset U\) form a ring.
For two denominators \(s_1,s_2\), take \(s_1c=s_2b\) by right Ore with \(c\in S\).
Since \(s_1c,s_2\in S\), also \(b\in S\), giving a common right denominator and hence closure under addition.
For products, move a numerator across an inverse by \(s^{-1}a=bc^{-1}\).
An affiliated unit \(ac^{-1}\) has \(a\in S\), so its inverse \(ca^{-1}\) is another such fraction.
This ring therefore equals \(D\).
Conversely condition 2 applied to \(s^{-1}a\) gives condition 1.
Under condition 2 and hence condition 1, clear the entries of a rational projection \(p\in M_k(D)\) with one common right denominator \(c\in S\).
The group-ring matrix \(Y=p(cI_k)\) has the same affiliated range as \(p\), and \(XY=0\) whenever \(p\) projects onto \(\ker X\).
This proves condition 3, which applies in particular to the rows of condition 4.
It also supplies the stated square annihilator in the moment criterion.

### Finite height intervals in a wreath product

Write \(H=\bigoplus_{j\in\mathbb Z}K\) for the base group, and \(a_i=t^{-i}at^i\).
The element \(t\) has infinite order, so \(s\) is injective on each bilateral shift orbit and is an affiliated unit.
On the input heights \(0,\ldots,n-1\), write the two coordinates of a vector as \(\sum_i t^i u_i,\sum_i t^i v_i\) with \(u_i,v_i\in\ell^2(H)\).
The equation \(X(u,v)^{\mathsf T}=0\) at height \(-1\) gives \(u_0=0\).
The remaining equations are
\[
                    u_{i+1}-u_i=a_i v_i \quad(0\le i<n),\qquad u_n=0 .
\]
Solving successively identifies this window kernel by a bounded right-\(H\)-equivariant isomorphism with the kernel of the row \([a_0,\ldots,a_{n-1}]\) on \(\ell^2(H)^n\).
The orthogonal complement of that row's closed image is the intersection of the kernels of the \(a_i^*\).
The projections onto these kernels belong to distinct tensor factors of the base group von Neumann algebra.
They commute, each has trace \(1-\theta\), and the canonical trace of their product is \((1-\theta)^n\).
The window kernel therefore has \(H\)-dimension \(d_n=n-1+(1-\theta)^n\).
With \(d_0=0\), the [interval rank formula](Yin_C_A0136_v1.md#interval-overlap-and-the-trace-estimate) gives (2) as \(d_n-d_{n-1}\).
Right multiplication by a power of \(t\) brings each column's height interval to \(0,\ldots,n-1\) and preserves the closed range generated by that column.
Every such finite family consequently has rank at most (2).

If \(K\) is amenable, so is its restricted direct sum \(H\).
The finite window equations form a matrix over \(\mathbb CH\).
Its finitely supported solutions are dense in its Hilbert kernel by [amenable kernel localization](Yin_C_A0001_v2.md#passage-beyond-finite-generation).
Right translates of those finitely supported solutions thus span the same closed global space as the translates of the full window kernel.
Normality of the trace on the increasing net of finite spans of their right translates gives the asserted supremum of ranks.
For arbitrary \(K\), (2) uses all Hilbert window solutions and gives the stated upper bound for polynomial columns.

When \(0<\theta<1\), (2) is less than one at every finite width.
In particular a single right denominator in (1) would supply a finite column of rank one, which is impossible.
If \(\theta=0\), then \(a=0\) and \(c=1,b=0\) work.
If \(\theta=1\), the elements \(a,a_1\) are affiliated units and commute because they lie in different copies of \(K\).
Put
\[
                    b=t a a_1,\qquad c=a_1-ta .
\]
Using \(at=ta_1\) gives \(ac=aa_1-ta_1a=(t^{-1}-1)b\).
The elements \(a,s,b\) are affiliated units, so \(c=a^{-1}sb\) is a group-ring element in \(S\).
This proves (1).

### Torsion-free amenable groups

For amenable \(K\), finite-support kernel density identifies the algebraic non-zero-divisors of \(\mathbb CK\) with the affiliated units in \(\mathbb CK\).
Indeed a noninjective scalar has a nonzero finitely supported vector in its kernel, and an affiliated unit has no one-sided annihilator. [Scalar descent](Yin_C_A0001_v2.md#finite-column-descent)
By (1), all the elements \(s^{-1}a\) for \(a\in\mathbb CK\) have group-ring right denominators in \(S\) precisely when \(\mathbb CK\) is a domain.
For amenable groups this domain property is also equivalent to the complex strong Atiyah assertion of integer matrix ranks in the torsion-free case. [Amenable equivalence](Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness)
Every amenable group algebra that is a domain is an Ore domain. [Linnell, Theorem 2.6](../audits/literature/Lin06/Yin_U001.md#amenable-domain-localization)

Conversely, suppose a finitely generated torsion-free amenable \(K\) fails the complex strong Atiyah conjecture.
There exists \(a\in\mathbb CK\) with \(0<\operatorname{rk}_K a<1\) by the same scalar descent.
The wreath product \(G=K\wr\mathbb Z\) is generated by a finite generating set of the zeroth lamp and the shift.
Its base is a directed union of amenable finite direct products and its quotient is cyclic, so \(G\) is amenable.
Any element of finite order lies in its torsion-free base, so \(G\) is torsion-free.
Equation (1) supplies a pair \(s,a\) in this group violating the classical right Ore condition and a rational graph kernel admitting no finite exhausting family of group-ring columns.
These implications prove the universal equivalence, leaving open whether any such \(K\) exists.

### A scalar example with torsion

For \(K=C_2\) and \(a=h-1\), the trace rank is \(1/2\).
Failure of right Ore for this lamp and shift also follows by taking adjoints in Dicks's theorem in the paper of Linnell, Lück and Schick. [Theorem 11](../audits/literature/LLS03/Yin_U001.md#lls03-u001)
Formula (2) gives the rank \(1-2^{-n}\).
The finite window matrix uses coefficients only from the finite subgroup \(H_n\) generated by the \(n\) lamps in the window.
Its kernel projection is a matrix over \(\mathbb CH_n\), by finite-dimensional spectral calculus on the positive Gram matrix.
Lifting its finitely many columns back to their \(n\) heights gives group-ring kernel columns whose right translates span the full window-generated space. [Window column construction](Yin_C_A0136_v1.md#interval-overlap-and-the-trace-estimate)
This proves attainment at each width.

For a scalar input, use the finite group \(S_3\), whose trivial, sign and two-dimensional standard unitary representations give the \(*\)-isomorphism \(\mathbb CS_3\cong\mathbb C\oplus\mathbb C\oplus M_2(\mathbb C)\).
Thus \(\mathbb C[L\times S_3]\) is the direct product of two copies of \(\mathbb CL\) and \(M_2(\mathbb CL)\), with the corresponding decomposition of the affiliated algebra.
Take the positive element \(x=(1,1,X^*X)\), where \(X=[\,t^{-1}-1,\,-(h-1)\,]\).
Its kernel projection is \((0,0,I_2-X^*(XX^*)^{-1}X)\).
To realize this projection by scalar rational operations, write \(e=(0,0,I_2)\), \(v=(0,0,\binom{X}{0})\) with zero second row, and \(d=(1,1,(XX^*)I_2)\).
These elements belong to the group ring, \(d\) is an affiliated unit, and the displayed projection equals \(e-v^*d^{-1}v\).
If \(y\in\mathbb C[L\times S_3]\) exhausted the kernel with \(xy=0\), the two columns of its last matrix block would exhaust the kernel of \(X\), contradicting the strict deficit at their finite height width.
The same obstruction applies to any finite family of scalar group-ring annihilators by collecting all their last-block columns.

## Assessment history

### Decision ore-graph-kernels

| Field | Value |
| --- | --- |
| date | 2026-11-25T13:34 |
| status | proved |
| reason | A graph kernel with one affiliated-unit entry detects a right denominator, and exact window ranks give the obstruction in a wreath product. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The Ore and graph-kernel equivalences, the exact rank at finite width, the universal amenable criterion, and the scalar example with torsion. |
| argument | [Argument](#argument) | Common denominator construction, independent lamp supports, the domain test and scalar realization on a finite group factor. |
| dependency | [Restricted witness spaces](Yin_C_A0137_v1.md#restriction-to-the-right-module-generated-by-the-input) | Detection of single right fractions. |
| dependency | [Moment criterion](Yin_C_A0160_v1.md#statement) | Square rational annihilators in the trace interval. |
| dependency | [Interval increments](Yin_C_A0136_v1.md#interval-overlap-and-the-trace-estimate) | Ranks generated by translates of each window. |
| dependency | [Amenable scalar descent](Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness) | Domain and integer-rank equivalence, and density on windows. |
| dependency | [Ore localization](../audits/literature/Lin06/Yin_U001.md#lin06-u001) | Ore condition in the amenable domain case. |
| dependency | [Dicks' obstruction](../audits/literature/LLS03/Yin_U001.md#lls03-u001) | Source of the classical finite-lamp obstruction. |
| review | [Ore graph kernels](../audits/reviews/Yin_R_A0173_v1.md#ore-graph-kernels) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-ore-graph-kernels)
