---
author: Yin
---

# Exact ranks of interval kernel generators in a cyclic extension

## Statement

Let \(G=H\rtimes\langle t\rangle\) be a countable discrete group with height \(\phi(t)=1\), \(\ker\phi=H\).
Write \(U_J\) for the ring affiliated to the group von Neumann algebra \(\mathcal N(J)\), and \(D_J\) for the division closure of \(\mathbb CJ\) in \(U_J\).
For \(L\in M_{m,k}(\mathbb CG)\) put \(\nu=\dim_G\ker L\) and \(r=\operatorname{rk}_G L=k-\nu\), using unnormalized matrix traces.
Choose integers \(a\leq b\) containing all heights in the entries' supports in \([a,b]\), and put \(w=b-a\).
For \(n\geq1\) let \(K_n\) be the Hilbert kernel vectors supported on heights \(0,\ldots,n-1\), let \(d_n=\dim_H K_n\), and put \(e_n=d_n-d_{n-1}\) with \(d_0=0\).
Denote by \(W_n\) the closed span of all right \(G\)-translates of \(K_n\).
Then
\[
 \dim_G W_n=e_n,\qquad e_n\uparrow\nu,\qquad
 \sum_{n\geq1}(\nu-e_n)\leq wr .
\]
When \(D_H\) is regular, the bounded positive rational matrix produced from this interval by [the coamenable construction](Yin_C_A0134_v1.md#lifting-kernel-columns) has exactly rank \(e_n\).
For a bordered Schur realization the same rank is obtained after projection onto the original input coordinates.
Thus one interval captures the full rank exactly when its increment reaches the limiting value.
If all interval dimensions lie in \(\delta\mathbb Z\) for some \(\delta>0\), every \(n>wr/\delta\) already achieves the limit.

The following two universal statements are equivalent.

1. Every finitely generated torsion-free group satisfies the strong Atiyah conjecture over \(\mathbb C\).
2. For every finitely generated torsion-free \(G\) surjecting onto \(\mathbb Z\), the interval increments eventually stabilize for every full-row-rank matrix \(L\) over \(\mathbb CG\), using this surjection for the height.

Every matrix in condition 2 already has rational kernel projection by scalar Gram inversion.
Thus universal finite-interval capture even for this restricted class would imply the strong Atiyah conjecture.
For [A0003](../tasks/Yin_T_A0003_v3.md#contract) the required rational kernel projection may be obtained by other means.

## Argument

### Interval overlap and the trace estimate

Consider the closed sum \(V_j\) of the copies of \(K_n\) shifted to intervals beginning at heights \(0,\ldots,j-1\) by right multiplication by the respective powers of \(t\).
These shifts preserve right \(H\)-invariance and \(H\)-dimension since conjugation by \(t\) preserves the group trace.
For \(j\geq1\) the intersection of \(V_j\) with the next copy on \([j,j+n-1]\) consists exactly of the kernel vectors supported on \([j,j+n-2]\).
Indeed \(V_j\) is supported up to height \(j+n-2\), and the entire overlap kernel lies already in the immediately preceding copy.
For \(n=1\) the overlap is zero.
The dimension formula for the closed sum of two Hilbert modules gives
\[
 \dim_H V_j=d_n+(j-1)e_n .
\]

The orthogonal projection onto \(K_n\) in its finite window is a finite matrix over \(\mathcal N(H)\).
Lift its columns by replacing each column of \(H\)-operators supported at heights \(i\) by the finite coset sum with left factors \(t^i\).
The resulting bounded matrix \(Y\) over \(\mathcal N(G)\) has closed image \(W_n\): on a single input height the closure of the image is the corresponding right shift of \(K_n\), and the finite-height inputs are dense.
This is the [coset column construction](Yin_C_A0134_v1.md#lifting-kernel-columns), which for bounded columns only needs a projection over \(\mathcal N(H)\).
For the restriction of \(Y\) to \(j\) consecutive input heights, the image has closure \(V_j\).
The restricted kernel is contained in the global kernel and is supported on \(j\) heights, giving the first bound below by [coset trace compression](Yin_C_A0134_v1.md#finite-coset-matrices).
The image lies in the global image closure and is supported on \(j+n-1\) heights, giving the second.
Hence
\[
 j\operatorname{rk}_G Y\ \leq\ d_n+(j-1)e_n\
 \leq (j+n-1)\operatorname{rk}_G Y.
\]
Division by \(j\) and passage to infinity give \(\dim_G W_n=e_n\).

Since \(W_n\subseteq W_{n+1}\subseteq\ker L\), the \(e_n\) increase and are bounded above by \(\nu\).
On \(n\) input heights the image of \(L\) is supported on \(n+w\) heights, so its \(H\)-dimension is at most \((n+w)r\) by the same trace compression.
Subtracting from the input dimension gives \(d_n\geq n\nu-wr\).
Consequently \(\sum_{i=1}^n(\nu-e_i)=n\nu-d_n\leq wr\) for every \(n\).
This proves convergence of \(e_n\) to \(\nu\) as well as the series bound.

If \(D_H\) is regular the window kernel projection has entries in \(D_H\) and the lifted \(Y\) has entries in \(D_G\).
For a Schur realization \(P=A-BQ^{-1}C\) with \(L=\left(\begin{smallmatrix}A&B\\C&Q\end{smallmatrix}\right)\) and \(Q\) injective, projection onto the upper input coordinates is injective on \(\ker L\) and hence on \(W_n\).
The dimension of its closed image on \(W_n\) remains \(e_n\) by polar decomposition.
If \(Y'\) denotes the upper rows of \(Y\), the bounded positive rational matrix \(Y'Y'^*\) annihilated by \(P\) therefore has rank \(e_n\).
For scalar \(P\), equality \(e_n=\nu\) recovers its kernel projection by the [attainment formula](Yin_C_A0134_v1.md#attaining-the-kernel-dimension).
If the \(d_n\) belong to \(\delta\mathbb Z\), the monotone bounded increments in that same lattice eventually equal \(\nu\).
While \(e_n<\nu\), each of the first \(n\) deficits is at least \(\delta\), giving \(n\delta\leq wr\).

There is also a bound when \(D_H\) is regular and the trace of every nonzero projection in \(M_k(D_H)\) is at least \(\delta>0\).
The closure of the image of \(K_n\) under extraction of its height-zero coordinate has a projection in \(M_k(D_H)\) by matrix regularity applied to the corresponding rows of the window projection.
The coordinate extractor on \(K_n\) has kernel the translated copy of \(K_{n-1}\), so its closed image has \(H\)-dimension \(e_n\).
These images increase and every strict increase has dimension at least \(\delta\), by taking the difference of their projections.
This gives eventual stabilization and the same bound \(n>wr/\delta\).
In particular a semisimple Artinian \(D_H\) has this lower bound at each fixed size, since its finitely many simple projective types have positive trace and every nonzero projection contains a simple direct summand.

### Strict growth with a rational kernel in the lamplighter group

Let \(G=(\bigoplus_{\mathbb Z}C_2)\rtimes\langle t\rangle\), let \(g\) be the nonidentity lamp at height zero, and put \(p=(1+g)/2\), \(q=1-p\).
The base \(H=\bigoplus_{\mathbb Z}C_2\) has regular division closure: its complex group ring is a directed union of algebras of functions on finite sets, hence is already regular and division closed in \(U_H\).
For the group-ring row \(L=[\,1-tp,\,-tq\,]\), Fourier transform in the lamps gives independent Bernoulli coordinates \(p_i=t^{-i}pt^i\) with means \(1/2\).
In one window its fiber equations are
\[
 u_0=0,\qquad u_{i+1}=p_i u_i+(1-p_i)v_i\quad(0\le i<n),\qquad u_n=0.
\]
When every \(p_i=1\), all \(v_i\) are free.
Otherwise the single endpoint condition sets \(v_j=0\) at the last index with \(p_j=0\).
Integrating these finite matrix ranks gives
\[
 d_n=n-1+2^{-n},\qquad e_n=1-2^{-n},\qquad \nu=1.
\]
The rank of \(L\) is \(1\) since it has two columns and nullity \(1\), so \(LL^*\) is an affiliated unit.
The full projection \(1-L^*(LL^*)^{-1}L\) has entries in \(D_G\), although every interval gives strictly smaller rank.
The individual lamps have order two.

### The universal stabilization obstruction for torsion-free groups

If the complex strong Atiyah conjecture holds for all finitely generated torsion-free groups, each window matrix over \(\mathbb CH\) has integer kernel dimension.
Indeed its finite support lies in a finitely generated torsion-free subgroup, and subgroup trace preservation gives the same kernel dimension in \(H\).
The discrete-increment bound proves condition 2.

Conversely, suppose some finitely generated torsion-free group \(K\) fails the complex strong Atiyah conjecture.
The [division-closure characterization](../ledger/Yin_L_A0001_v1.md#formulation-and-algebraic-interface) gives a nonzero nonunit \(x\in D_K\).
Set
\[
 a=\tfrac12 x^*x(1+x^*x)^{-1}\in D_K\cap\mathcal N(K).
\]
This positive contraction of norm at most \(1/2\) has the same kernel as \(x\), and its support has trace \(\theta\) strictly between zero and one.
Take the restricted wreath product \(G=(\bigoplus_{i\in\mathbb Z}(K\times K))\rtimes\langle t\rangle\) with the shift action and denote its base by \(H\).
This group is generated by \(t\) and the generators in the two height-zero factors, and it is torsion-free by projection to \(\mathbb Z\) and torsion-freeness of \(H\).
Use the letters \(a,c\) for the copies of the displayed element in the two distinct factors at height zero.
The rational row
\[
 P=[\,1-ta,\,-tc\,]
\]
has full row rank since \(1-ta\) is invertible even as a bounded operator.
In height coordinates on the base, write \(a_i=t^{-i}at^i\), \(c_i=t^{-i}ct^i\).
They all commute and their joint trace distribution is the product of the individual distributions because they lie in distinct group direct factors.
The interval system for \(P\) imposes \(u_0=0\), the recursion \(u_{i+1}=a_i u_i+c_i v_i\), and the endpoint \(u_n=0\).
In the joint abelian spectral representation, \(u_n\) is a scalar linear form in \(v_0,\ldots,v_{n-1}\).
Let \(s_i\) be the probability that the form at index \(i\) is nonzero.
The form at \(i+1\) is nonzero whenever \(c_i\ne0\); if \(c_i=0\), it is nonzero exactly when \(a_i\ne0\) and the preceding form is nonzero.
The variables at index \(i\) are independent of the earlier ones, and \(a_i,c_i\) have support probability \(\theta\).
Ordinary matrix rank in this joint representation computes the unnormalized \(H\)-trace rank, since the kernel projection is a bounded spectral function of the finite matrix Gram operator in the same abelian matrix algebra.
Thus
\[
 s_0=0,\qquad s_{i+1}=\theta+\theta(1-\theta)s_i,\qquad
 d_n(P)=n-s_n,\qquad e_n(P)=1-\theta[\theta(1-\theta)]^{n-1}.
\]
These increments never reach the global kernel dimension \(1\).

It remains to implement the row by a group-ring matrix while retaining every interval kernel dimension.
Choose scalar realizations \(a=\alpha_aQ_a^{-1}\beta_a\), \(c=\alpha_cQ_c^{-1}\beta_c\) over the corresponding copy of \(\mathbb CK\), with injective square group-ring blocks and constant rows and columns. [Affine realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Take \(A=[1,0]\), \(B=[t\alpha_a,t\alpha_c]\), \(Q=\operatorname{diag}(Q_a,Q_c)\), \(C=\operatorname{diag}(\beta_a,\beta_c)\) and \(L=\left(\begin{smallmatrix}A&B\\ C&Q\end{smallmatrix}\right)\).
Then \(P=A-BQ^{-1}C\).
All entries of \(C,Q\) have height zero, so the lower block produces outputs on the input window itself.
Its square pivot there is a diagonal sum of the \(n\) conjugates of \(Q\), each an affiliated unit over \(U_H\).
The upper block uses output heights \(0,\ldots,n\).
Rectangular Schur elimination in \(U_H\) on these finite input and output sets therefore gives the restricted row \(P\) and the invertible restricted pivot as diagonal blocks, with any exterior zero rows removable.
This proves \(d_n(L)=d_n(P)\) for every \(n\), even with unbounded pivot inverses.
The same elimination in \(U_G\) gives full row rank of \(L\); in particular \(LL^*\) is an affiliated unit and its matrix inverse lies over \(D_G\) by scalar Gram elimination.
The resulting full-row-rank group-ring matrix violates condition 2 while \(1-L^*(LL^*)^{-1}L\) is rational.
This conditional construction proves the converse implication without assuming the existence of a torsion-free counterexample.

## Assessment history

### Decision interval-increments

| Field | Value |
| --- | --- |
| date | 2026-11-25T09:38 |
| status | proved |
| reason | Trace compression identifies the exact interval ranks, and the two finite-window constructions prove the obstruction to universal finite stabilization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Interval ranks, summable losses, the discrete bound and the equivalence of universal stabilization with the complex strong Atiyah conjecture. |
| argument | [Argument](#argument) | Overlapping windows, trace bounds, the lamplighter calculation and the conditional torsion-free wreath construction. |
| dependency | [Finite coset kernels](Yin_C_A0134_v1.md#lifting-kernel-columns) | Lifting the interval projection into a rational positive annihilator when the subgroup division closure is regular. |
| review | [Independent proof review](../audits/reviews/Yin_R_A0167_v1.md#cyclic-windows) | Overlapping windows, trace bounds, the lamplighter calculation and the conditional torsion-free wreath construction. |

## Current assessment

[Selected decision](#decision-interval-increments)
